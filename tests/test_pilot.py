from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from copy import deepcopy
from datetime import timedelta
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import threading
import unittest

from reference.tsm_pilot.contracts import ContractError, loads, ref, validate
from reference.tsm_pilot.fixtures import END, NEXT_REVIEW, NOW, START, initiative_data, mandate_data, observation_data
from reference.tsm_pilot.runtime import AccessDenied, Conflict, Pilot


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "pilot.sqlite3"
        self.time = NOW
        self.owner = self.client("owner-a")
        self.agent = self.client("agent-a")
        self.initiative = self.owner.create_initiative(initiative_data())
        self.mandate = self.owner.propose_mandate(mandate_data(ref(self.initiative)))

    def client(self, principal):
        return Pilot(self.path, principal, clock=lambda: self.time)

    def approve(self, mandate=None):
        return self.owner.decide(ref(mandate or self.mandate), "approve", "Bounded experiment",
                                 ["Current approach"], NEXT_REVIEW)

    def reserve(self, key="reservation-1", amount=10000, mandate=None):
        return self.agent.reserve(ref(mandate or self.mandate), key, "draft", "support-queue", amount)

    def review(self):
        return self.owner.review(ref(self.initiative), START, END, "change", "Review fixture evidence", NEXT_REVIEW)

    def test_history_survives_reopen_and_returned_records_are_copies(self):
        decision = self.approve()
        reservation = self.reserve()
        original = deepcopy(self.initiative)
        self.initiative["data"]["budgetMinor"] = 1
        reopened = self.client("owner-a")
        self.assertEqual(reopened.get(ref(original)), original)
        self.assertEqual(reopened.get(ref(decision)), decision)
        self.assertEqual(reopened.get(ref(reservation)), reservation)
        self.assertEqual(len(reopened.history(ref(original))), 4)

    def test_unapproved_mandate_cannot_reserve(self):
        with self.assertRaises(Conflict):
            self.reserve()
        self.assertEqual(self.owner.budget(ref(self.initiative))["reservedMinor"], 0)

    def test_stale_approval_and_reservation_after_revision_are_blocked(self):
        self.approve()
        data = deepcopy(self.mandate["data"])
        data["targets"] = ["different-queue"]
        revised = self.owner.propose_mandate(data, previous=ref(self.mandate))
        with self.assertRaises(Conflict):
            self.approve()
        with self.assertRaises(Conflict):
            self.reserve()
        self.assertEqual(self.owner.mandate_state(ref(revised)), "proposed")
        self.assertEqual(self.owner.get(ref(self.mandate)), self.mandate)

    def test_repeated_approval_does_not_create_another_decision(self):
        self.approve()
        with self.assertRaises(Conflict):
            self.approve()
        self.assertEqual(len(self.owner.history(ref(self.initiative))), 3)

    def test_pause_blocks_new_reservations_and_preserves_previous(self):
        self.approve()
        reservation = self.reserve()
        self.owner.decide(ref(self.mandate), "pause", "Investigate", ["Continue"], NEXT_REVIEW)
        with self.assertRaises(Conflict):
            self.reserve("new")
        self.assertEqual(self.reserve(), reservation)  # Historical receipt, not new authority.
        self.assertEqual(self.owner.budget(ref(self.initiative))["reservedMinor"], 10000)

    def test_revocation_survives_restart(self):
        self.approve()
        self.owner.decide(ref(self.mandate), "revoke", "End delegation", ["Continue"], NEXT_REVIEW)
        self.assertEqual(self.client("owner-a").mandate_state(ref(self.mandate)), "revoked")
        with self.assertRaises(Conflict):
            self.reserve()

    def test_expiry_boundary_and_future_start(self):
        self.approve()
        self.time = NOW.replace(day=15, hour=0)
        self.assertEqual(self.owner.mandate_state(ref(self.mandate)), "expired")
        with self.assertRaises(Conflict):
            self.reserve()
        self.time = NOW
        data = deepcopy(self.mandate["data"])
        data["startsAt"] = "2026-10-03T00:00:00Z"
        future = self.owner.propose_mandate(data)
        self.approve(future)
        self.assertEqual(self.owner.mandate_state(ref(future)), "not-yet-valid")
        with self.assertRaises(Conflict):
            self.reserve(mandate=future)

    def test_roles_and_scope_are_checked(self):
        with self.assertRaises(AccessDenied):
            self.client("reviewer-a").decide(ref(self.mandate), "approve", "No", ["Wait"], NEXT_REVIEW)
        with self.assertRaises(AccessDenied):
            self.client("owner-b").get(ref(self.initiative))
        with self.assertRaises(AccessDenied):
            self.client("viewer-a").observe(observation_data(ref(self.initiative)))
        with self.assertRaises(AccessDenied):
            self.client("viewer-a").review(ref(self.initiative), START, END, "continue", "No", NEXT_REVIEW)
        with self.assertRaises(AccessDenied):
            self.owner.reserve(ref(self.mandate), "x", "draft", "support-queue", 100)

    def test_wrong_action_and_target_are_rejected(self):
        self.approve()
        for action, target in (("send", "support-queue"), ("draft", "other-queue")):
            with self.assertRaises(AccessDenied):
                self.agent.reserve(ref(self.mandate), "x", action, target, 100)

    def test_idempotent_reservations_require_exact_parameters(self):
        self.approve()
        first = self.reserve()
        self.assertEqual(self.reserve(), first)
        with self.assertRaises(Conflict):
            self.reserve(amount=20000)
        self.assertEqual(self.owner.budget(ref(self.initiative))["reservedMinor"], 10000)

    def test_shared_ceiling_across_mandates(self):
        self.approve()
        other = self.owner.propose_mandate(mandate_data(ref(self.initiative)))
        self.approve(other)
        self.reserve(amount=40000)
        with self.assertRaises(Conflict):
            self.reserve("other", amount=30000, mandate=other)

    def test_budget_carries_over_to_revised_mandate(self):
        self.approve()
        self.reserve(amount=40000)
        data = deepcopy(self.mandate["data"])
        data["budgetMinor"] = 45000
        revised = self.owner.propose_mandate(data, previous=ref(self.mandate))
        self.approve(revised)
        with self.assertRaises(Conflict):
            self.reserve("extra", amount=10000, mandate=revised)

    def test_concurrent_reservations_cannot_double_spend(self):
        self.approve()
        gate = threading.Barrier(2)

        def attempt(key):
            client = self.client("agent-a")
            gate.wait(timeout=10)
            try:
                client.reserve(ref(self.mandate), key, "draft", "support-queue", 40000)
                return "reserved"
            except Conflict:
                return "denied"

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(attempt, key) for key in ("one", "two")]
            self.assertCountEqual([future.result(timeout=15) for future in futures], ["reserved", "denied"])
        self.assertEqual(self.owner.budget(ref(self.initiative))["reservedMinor"], 40000)

    def test_negative_zero_boolean_and_excessive_reservations_fail(self):
        self.approve()
        for amount in (-1, 0, True, 1000000001):
            with self.subTest(amount=amount), self.assertRaises(ContractError):
                self.reserve(amount=amount)

    def test_no_evidence_is_insufficient(self):
        review = self.review()
        self.assertEqual(review["data"]["assessment"], "insufficient")
        self.assertEqual(review["data"]["evidenceRefs"], [])

    def test_verified_operation_is_not_outcome_proof(self):
        data = observation_data(ref(self.initiative))
        data.update(kind="operation", criterionId=None, status="verified", value=None, unit=None)
        self.owner.observe(data)
        review = self.review()
        self.assertEqual(review["data"]["assessment"], "insufficient")
        self.assertTrue(any("not outcome proof" in item for item in review["data"]["limitations"]))

    def test_measurement_threshold_and_conflicting_evidence(self):
        self.owner.observe(observation_data(ref(self.initiative), 98))
        first = self.review()
        self.assertEqual(first["data"]["assessment"], "supported")
        self.owner.observe(observation_data(ref(self.initiative), 90))
        second = self.review()
        self.assertEqual(second["data"]["assessment"], "contradicted")
        self.assertEqual(self.owner.get(ref(first)), first)
        self.assertEqual(len(second["data"]["evidenceRefs"]), 2)

    def test_stale_evidence_is_excluded(self):
        data = initiative_data()
        data["criteria"][0]["maxAgeSeconds"] = 60
        initiative = self.owner.create_initiative(data)
        self.owner.observe(observation_data(ref(initiative), 98))
        review = self.owner.review(ref(initiative), START, END, "change", "Too old", NEXT_REVIEW)
        self.assertEqual(review["data"]["assessment"], "insufficient")
        self.assertTrue(any("Stale" in item for item in review["data"]["limitations"]))

    def test_method_and_population_mismatch_cannot_support_outcome(self):
        for field in ("method", "population"):
            data = observation_data(ref(self.initiative), 98)
            data[field] = "different"
            self.owner.observe(data)
        self.assertEqual(self.review()["data"]["assessment"], "insufficient")

    def test_observation_correction_preserves_history(self):
        data = observation_data(ref(self.initiative))
        data.update(status="unknown", value=None)
        previous = self.owner.observe(data)
        self.assertEqual(self.review()["data"]["assessment"], "insufficient")
        corrected = observation_data(ref(self.initiative), 98)
        corrected["supersedes"] = ref(previous)
        latest = self.owner.observe(corrected)
        review = self.review()
        self.assertEqual(review["data"]["assessment"], "supported")
        self.assertEqual(review["data"]["evidenceRefs"], [ref(latest)])
        self.assertEqual(self.owner.get(ref(previous)), previous)
        with self.assertRaises(Conflict):
            self.owner.observe(corrected)

    def test_correction_cannot_change_claim_or_downgrade_access(self):
        old = self.owner.observe(observation_data(ref(self.initiative)), visibility="reviewers")
        data = observation_data(ref(self.initiative), 98)
        data["supersedes"] = ref(old)
        with self.assertRaises(AccessDenied):
            self.owner.observe(data)
        data["windowStart"] = "2026-09-30T00:00:00Z"
        with self.assertRaises(ContractError):
            self.owner.observe(data, visibility="reviewers")

    def test_restricted_evidence_propagates_to_review_and_decision(self):
        observation = self.owner.observe(observation_data(ref(self.initiative)), visibility="reviewers")
        review = self.review()
        decision = self.owner.decide(ref(self.mandate), "approve", "Review restricted material",
                                     ["Wait"], NEXT_REVIEW, [ref(review)])
        viewer = self.client("viewer-a")
        for record in (observation, review, decision):
            with self.subTest(kind=record["recordType"]), self.assertRaises(AccessDenied):
                viewer.get(ref(record))
        self.assertEqual(len(viewer.history(ref(self.initiative))), 2)
        self.assertEqual(self.client("reviewer-a").get(ref(review)), review)

    def test_cross_initiative_decision_evidence_is_rejected(self):
        other = self.owner.create_initiative(initiative_data())
        evidence = self.owner.observe(observation_data(ref(other)))
        with self.assertRaises(ContractError):
            self.owner.decide(ref(self.mandate), "approve", "Wrong evidence", ["Wait"], NEXT_REVIEW, [ref(evidence)])
        self.assertEqual(self.owner.mandate_state(ref(self.mandate)), "proposed")

    def test_temporal_and_metric_observation_errors(self):
        for changes in ({"observedAt": "2026-10-03T00:00:00Z"}, {"windowStart": "2026-10-03T00:00:00Z"},
                        {"criterionId": "nonexistent"}, {"unit": "seconds"}):
            data = observation_data(ref(self.initiative))
            data.update(changes)
            with self.subTest(changes=changes), self.assertRaises(ContractError):
                self.owner.observe(data)

    def test_draft_review_does_not_activate_or_pause_mandate(self):
        self.approve()
        self.owner.review(ref(self.initiative), START, END, "pause", "Recommendation only", NEXT_REVIEW)
        self.assertEqual(self.owner.mandate_state(ref(self.mandate)), "active")
        self.reserve()

    def test_invalid_mandate_boundaries_and_cross_scope_delegate(self):
        for changes in ({"delegate": "agent-b"}, {"budgetMinor": 60001}, {"furtherDelegation": True},
                        {"startsAt": "2026-10-16T00:00:00Z"}, {"expiresAt": "2026-10-01T00:00:00Z"}):
            data = mandate_data(ref(self.initiative))
            data.update(changes)
            with self.subTest(changes=changes), self.assertRaises(ContractError):
                self.owner.propose_mandate(data)

    def test_unsupported_database_version_and_unrelated_db_are_preserved(self):
        other = Path(self.temporary.name) / "other.sqlite3"
        with closing(sqlite3.connect(other)) as db:
            db.execute("CREATE TABLE unrelated (value TEXT)")
            db.commit()
        with self.assertRaises(Conflict):
            Pilot(other)
        with closing(sqlite3.connect(other)) as db:
            self.assertEqual(db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall(), [("unrelated",)])
            db.execute("PRAGMA user_version = 99")
            db.commit()
        with self.assertRaises(Conflict):
            Pilot(other)

    def test_contract_rejects_versions_extra_fields_and_invalid_dates(self):
        for changes in ({"schemaVersion": "99"}, {"surprise": True}, {"version": 0},
                        {"recordType": "Unknown"}, {"recordedAt": "2026-02-30T12:00:00Z"},
                        {"recordedAt": "2026-10-02T12:00:00"}, {"recordedAt": "2026-10-02T12:00:00-00:00"}):
            record = deepcopy(self.initiative)
            record.update(changes)
            with self.subTest(changes=changes), self.assertRaises(ContractError):
                validate(record)
        record = deepcopy(self.initiative)
        record["data"]["criteria"][0]["threshold"] = float("nan")
        with self.assertRaises(ContractError):
            validate(record)

    def test_strict_json_rejects_duplicate_keys_and_nonfinite_numbers(self):
        for content in ('{"a": 1, "a": 2}', '{"nested": {"x": 1, "x": 2}}', '{"value": NaN}', '{"value": Infinity}', '{"value": 1e999}'):
            with self.subTest(content=content), self.assertRaises(ContractError):
                loads(content)


if __name__ == "__main__":
    unittest.main()
