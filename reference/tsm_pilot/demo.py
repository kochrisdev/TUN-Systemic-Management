"""Run the bounded, deterministic fixture scenario without external effects."""

import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from .contracts import ref
from .fixtures import END, NEXT_REVIEW, NOW, START, initiative_data, mandate_data, observation_data
from .runtime import Conflict, Pilot


def run(path):
    owner = Pilot(path, "owner-a", clock=lambda: NOW)
    agent = Pilot(path, "agent-a", clock=lambda: NOW)
    initiative = owner.create_initiative(initiative_data())
    mandate = owner.propose_mandate(mandate_data(ref(initiative)))
    owner.decide(ref(mandate), "approve", "Permit the bounded fixture experiment",
                 ["Keep the current workflow"], NEXT_REVIEW)
    reservation = agent.reserve(ref(mandate), "demo-reservation", "draft", "support-queue", 35000)
    owner.observe(observation_data(ref(initiative)))
    operational = observation_data(ref(initiative))
    operational.update(kind="operation", criterionId=None, status="unknown", value=None, unit=None,
                       source="synthetic-lost-response", method="fixture-report",
                       limitations=["No provider has been called; this is an unknown-effect fixture"])
    owner.observe(operational)
    review = owner.review(ref(initiative), START, END, "pause", "Quality missed its threshold", NEXT_REVIEW)
    owner.decide(ref(mandate), "pause", "Pause future reservations for review",
                 ["Continue with current scope"], NEXT_REVIEW, [ref(review)])
    try:
        agent.reserve(ref(mandate), "after-pause", "draft", "support-queue", 100)
    except Conflict:
        blocked = True
    else:
        raise AssertionError("A paused mandate allowed a fresh reservation")
    reopened = Pilot(path, "owner-a", clock=lambda: NOW)
    assert reopened.get(ref(review)) == review
    assert reopened.get(ref(reservation)) == reservation
    return {
        "scenario": "Synthetic local pilot; no model, provider, or production identity",
        "fixtureClock": NOW.isoformat(), "initiativeRef": ref(initiative),
        "reviewAssessment": review["data"]["assessment"], "limitations": review["data"]["limitations"],
        "mandateState": reopened.mandate_state(ref(mandate)), "freshReservationBlocked": blocked,
        "budget": reopened.budget(ref(initiative)), "historyRecords": len(reopened.history(ref(initiative))),
        "restartVerified": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, help="New database file to retain; existing paths are refused")
    args = parser.parse_args()
    if args.db:
        args.db.parent.mkdir(parents=True, exist_ok=True)
        try:
            args.db.touch(exist_ok=False)
        except FileExistsError:
            parser.error("Choose a new database path; existing files are never overwritten")
        result = run(args.db)
        result["database"] = str(args.db.resolve())
    else:
        with TemporaryDirectory(prefix="tsm-pilot-") as directory:
            result = run(Path(directory) / "pilot.sqlite3")
        result["database"] = "Temporary fixture database removed after the run"
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
