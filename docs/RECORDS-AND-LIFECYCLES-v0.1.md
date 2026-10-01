# Records and lifecycles v0.1

Status: proposed semantics; no executable schema or supported API. [Documentation index](README.md) · [Specification](SPECIFICATION-v0.1.md)

## Shared record conventions

Use stable record identities and immutable material revision references, such as `{ id, version }`. Keep schema version separate from business revision. Record organizational and access scope, producer, accountable owner, relevant event and observation times with explicit timezones, source references, and supersession relationships.

A reference identifies a record; it does not confer access or authority. Store source material separately when different access and retention rules apply. A historical decision remains a record of what was decided even after its authority expires.

## Core vocabulary

| Record | Meaning and minimum content |
|---|---|
| Outcome | Intended change, beneficiaries, owner, baseline, target or acceptance criteria, timeframe, limitations |
| Initiative | Coordinated work toward an outcome; alternatives, assumptions, resources, dependencies, review and stop conditions |
| Mandate | Assigned purpose and responsibility; owner, assigned actor, outcome and initiative references, scope, acceptance and escalation conditions |
| Delegation | Authority attached to a mandate revision; delegator, delegate, actions, targets, data access, limits, validity, further-delegation and revocation rules |
| Decision | Authorized owner or approved policy reference, subject revision, options, recommendation provenance, selected option, evidence, rationale, dissent, review trigger |
| Commitment | An acknowledged contribution owed by an actor; recipient, due condition, acceptance evidence, dependency references |
| Signal | Information that may require attention; origin, observed subject and time, content reference, access scope, reliability limits |
| Risk | A possible adverse condition; affected outcome, exposure basis, owner, treatment, trigger, residual uncertainty |
| Dependency | A required contribution or resource; supplying and consuming owners, expected condition, failure response |
| Exception | Bounded deviation from a policy revision; authorized owner, scope, reason, expiry, conditions, review |
| Review | Evidence assessment at a decision point; criteria, findings, uncertainties, selected action, follow-ups, next trigger |
| LearningRecord | An assessed assumption; supporting and contrary evidence, limitations, confidence basis, proposed decision impact |

## Supporting measurement records

`MetricDefinition` specifies the metric's purpose, units, population, denominator, window, baseline, method, owner, source, thresholds, and decision relevance. `Observation` supplies a measured value or explicit missing state for a specific metric version and window, with collection time and provenance. `EvidenceAssessment` states which claim an observation supports, contradicts, or leaves unresolved.

An `EngineeringEvidenceReference` should identify the source host, operation, action-record revision, verification claim and scope, observation time, and access-controlled evidence location. It remains a reference to engineering evidence rather than a replacement for the engineering record.

## Independent lifecycles

| Dimension | Illustrative values | Meaning |
|---|---|---|
| Initiative lifecycle | proposed, active, paused, retired | Organizational commitment state |
| Initiative health | healthy, threatened, critical, unknown | Assessment against stated criteria |
| Outcome assessment | unknown, insufficient, supported, contradicted | What evidence supports for a stated claim |
| Decision state | proposed, decided, superseded, due-for-review | Recorded management choice and review eligibility |
| Mandate state | proposed, active, paused, expired, revoked, completed | Current assignment state |
| Delegation eligibility | usable, expired, revoked, constrained | Organizational authority available for evaluation |
| Investment state | proposed, funded, constrained, stopped | Resource allocation state |
| Intervention state | requested, acknowledged, effective, failed, unknown | Evidence of a particular control request |

These values are illustrative, not released enums. A paused initiative may have an unresolved provider effect. A completed mandate may have insufficient evidence of organizational value. A funded initiative may have no usable runtime authorization.

## Relationships to preserve

- A delegation resolves to the mandate revision it governs and to the authority of its delegator.
- A decision references the material subject version reviewed; later edits require a new decision where material.
- Child delegation never expands parent authority or duplicates a shared budget allocation.
- An observation identifies its metric definition version and actual population and window.
- Evidence supports a stated claim; another initiative's success cannot be copied as proof.
- A new review or correction preserves earlier assessments and explains what changed.
- A stop decision and observed runtime intervention retain separate identities and outcomes.

Schemas can eventually check field structure. Authority, access, current eligibility, cross-record meaning, and external effects need additional enforcement and evidence.
