# Proposed pilot: AI Initiative Review

Status: planned, not implemented or run. [Documentation index](README.md) · [Support scenario](../examples/ai-support-initiative.md)

## Question

Can a team trace a review decision from an organizational outcome and bounded mandate through scoped evidence, while preserving unknown effects and current authority?

## First implementation boundary

Use one initiative, one accountable human owner, fixture identities, and a durable local store. Support Outcome, Initiative, Mandate, Delegation, Decision, MetricDefinition, Observation, Review, Exception, and LearningRecord only as the selected scenario requires. Commitments, risks, and dependencies may initially be embedded while retaining their semantics.

Start with reviewable local records and synthetic observations clearly marked as fixtures. Then connect one bounded operation to the engineering pilot through a tested adapter. The engineering publication provider can demonstrate a review-summary publication; it does not supply a customer-support provider. Real identity, real customer data, and an external provider require later implementation and separate validation.

## Planned acceptance scenarios

| Case | Expected observable behavior |
|---|---|
| Initial charter and decision | Outcome, owner, assumptions, alternatives, limits, and review criteria remain inspectable |
| Material mandate edit | A prior decision cannot silently approve the changed scope |
| Delegation expiry or revocation | New effectful dispatch is denied under the defined host boundary |
| Shared budget exhaustion | Concurrent commitments cannot each consume the same available capacity |
| Missing or contradictory evidence | Review retains the limitation and cannot present a verified outcome |
| Provider response lost | Original operation remains unresolved until reconciliation supplies evidence; no unsafe duplicate action |
| Pause during accepted work | Stop decision, request, acknowledgement, and observed effectiveness remain separate |
| Review and adaptation | Continue/change/expand/pause/retire decision records evidence, owners, and a next trigger |
| Restart | Decisions, revisions, unresolved effects, and evidence references retain their meanings |
| Restricted evidence | Unauthorized viewers cannot obtain source content through a summary or link |

## What a report would contain

Record the source revisions, environment, fixture boundaries, commands or manual procedures, actual results, failures, limitations, and reviewer. Keep operational acceptance separate from evaluation of whether the workflow improves decisions or is usable for people.

## Second scenario

Use the [incident and mandate pause](../examples/incident-and-mandate-pause.md) to challenge the same records under time pressure, changed authority, and an unknown effect. Extend the model when a concrete scenario exposes a gap.

No acceptance scenario in this plan has been executed by a management runtime. The [conformance matrix](CONFORMANCE-MATRIX.md) lists proposed assessment procedures.
