# Experimental pilot schema profile

[Documentation index](../docs/README.md) · [Pilot guide](../docs/PILOT.md) · [Schema](pilot-v0.1.schema.json)

This JSON Schema Draft 2020-12 profile fixes a narrow record format for the local pilot. It is not the general management model or a stable SDK contract. Use the schema version and the source commit when exchanging records.

## Record families

| Record | Pilot content |
|---|---|
| Initiative | Embedded outcome, owner, beneficiaries, baseline explanation, assumptions, alternatives, metric criteria, USD resource ceiling, review date, stop conditions, dependencies |
| Mandate | Initiative revision reference, purpose, fixture delegate, permitted actions and targets, data scope, resource ceiling, validity interval, escalation, no further delegation |
| Decision | Initiative and exact mandate references, approve/reject/pause/revoke choice, rationale, alternatives, evidence references, next review |
| Observation | Initiative, outcome criterion or operation kind, measured/verified/missing/unknown/contradicted state as applicable, value, source, method, population, window, observation time, limitations, optional predecessor |
| Review | Initiative and window, per-criterion and overall assessment, evidence snapshot, limitations, recommended action, rationale, next review, budget snapshot |
| Reservation | Initiative and mandate references, parameter-bound request identity, action, target, reserved amount |

Each record also carries `schemaVersion`, `recordType`, `id`, positive integer `version`, `scope`, `actor`, `recordedAt`, and `visibility`. The runtime issues these fields. Money is expressed in integer USD cents, with a profile ceiling of 1,000,000,000 cents per initiative or mandate. Resource reservations accumulate until a future settlement/release mechanism is implemented.

## Structure and meaning

The [contract validator](../reference/tsm_pilot/contracts.py) rejects unsupported versions and record families, extra fields, invalid timestamps, duplicate JSON keys, and non-finite JSON numbers. It explicitly enables calendar checks. It uses [jsonschema's validation API](https://python-jsonschema.readthedocs.io/en/stable/validate/) with an application-specific timestamp checker. The profile requires explicit offsets, seconds, and at most six fractional digits; unknown `-00:00` offsets are rejected.

The [host](../reference/tsm_pilot/runtime.py) separately checks scope and record kinds, fixture decision rights, unique criterion IDs, exact current mandate revisions, validity ordering, delegation scope, cumulative reservation ceilings, observation windows, and correction relationships. Structural validation alone cannot establish those facts.

The database format has `user_version = 1`; unsupported versions and unrelated nonempty databases are refused. No migration or import service is supplied. Record revisions remain immutable through the application API. The current mandate projection is separate and can become proposed, active, rejected, paused, or revoked; expiry and future start are evaluated from the clock.

## Review semantics

A review evaluates one exact observation window. Observations retain their own collection times. All current observations for that window are considered, so a caller cannot select only a favorable measurement. An explicit correction must preserve initiative, claim kind, criterion, and window, refer to the current end of its correction chain, and preserve restricted visibility. Earlier observations and reviews remain readable under their original access rules.

For each criterion, fresh matching measurements support the declared threshold. A current adverse measurement or explicit contradiction takes precedence. Missing or unresolved measurements leave the criterion insufficient. Stale or method/population-mismatched observations are excluded with limitations. The overall outcome assessment is contradicted if any criterion is contradicted, otherwise insufficient if any criterion is insufficient, otherwise supported.

`supported` means only that the supplied current measurements satisfy the profile's numeric criteria. It does not establish evidence authenticity, causal improvement, customer benefit, or approval to expand. Operational evidence is preserved separately in evidence references and limitations; an unknown operation can coexist with supported outcome measurements and still requires operational follow-up. Source contents are not fetched.

## Fixtures and checks

[valid-initiative.json](fixtures/valid-initiative.json) is a complete synthetic example. [cases.json](fixtures/cases.json) defines a valid base and eight invalid mutations for versions, fields, dates, budget, and criteria. The [fixture test](../tests/test_schema_fixtures.py) checks those cases, while [runtime tests](../tests/test_pilot.py) exercise semantic relationships and persistence.

Run the tests as described in the [pilot guide](../docs/PILOT.md). The [named validation report](../docs/PILOT-VALIDATION-2026-10-02.md) states the tested environment and limits. Full requirements remain unassessed.
