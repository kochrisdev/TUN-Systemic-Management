# Proposed specification v0.1

Status: draft requirements; all requirements remain unassessed. [Documentation index](README.md) · [Conformance matrix](CONFORMANCE-MATRIX.md)

## Interpretation

MUST identifies an obligation within this proposed specification. MUST NOT identifies a prohibition. SHOULD identifies a recommendation for which an assessment records any alternative and its reason. MAY identifies an optional approach. These terms do not imply an external standard or certification.

An assessment identifies the management workflow, organization or product scope, source revision, applicable requirements, reviewer, evidence, and limits. Non-applicability needs a reason. Documentation examples do not establish conformance.

## TSM-001 — Outcome and scope

An initiative MUST identify the intended outcome, affected people, accountable human owner, boundaries, assumptions, success evidence, and a review or stopping condition. An unknown baseline MUST be marked unknown and assigned a plan for establishing it before claiming improvement.

## TSM-002 — Accountable decisions

A consequential management decision MUST record its authorized human decision owner, exact subject revision, selected option, material alternatives, evidence, assumptions, rationale, and review trigger. An AI recommendation MUST remain distinguishable from that decision. An organization MAY implement recurring decisions through an approved, bounded policy whose human owner and revision are recorded.

## TSM-003 — Bounded delegation

An active delegation MUST identify its delegator, delegate, accountable human owner, mandate revision, permitted capabilities and targets, data scope, limits, validity, escalation route, and revocation mechanism. It MUST state whether further delegation is allowed. Child authority and combined resource use MUST remain within applicable parent limits.

## TSM-004 — Current authority

A material change to purpose, actor, scope, targets, limits, or validity MUST produce a new reviewable revision. Prior approval MUST NOT silently authorize expanded authority. Effectful integrations MUST enforce current authority at their action boundary; a management record or UI approval alone MUST NOT count as an execution grant.

## TSM-005 — Resources and dependencies

An initiative MUST record its resource ceilings, budget owner, material dependencies, and the basis for cost observations. Effectful automation MUST specify how shared limits are enforced across concurrent work and how delayed or unavailable cost information constrains further dispatch. Increasing a limit MUST require an authorized decision.

## TSM-006 — Evidence-bound claims

A management outcome claim MUST identify its evidence, source, subject, observation window, method, assessment owner or service, and material limitations. Verified operation effects MUST remain distinguishable from product quality, organizational benefit, and causal attribution. Unsupported, stale, or contradictory evidence MUST NOT be presented as a verified success.

## TSM-007 — Review and change

An active initiative MUST have a review owner and scheduled or event-based triggers. A review MUST record the compared criteria, evidence, uncertainties, decision, required follow-up owners, and next review condition. Material mandate changes MUST return through the decision and delegation process.

## TSM-008 — Escalation and intervention

A delegation MUST define actionable escalation conditions, a responsible responder, and the scope of available intervention. Integrations MUST distinguish a requested intervention, its acknowledgement, and evidence that it became effective. Known prior effects and unresolved work MUST remain visible after a pause or revocation.

## TSM-009 — Exceptions

A policy exception MUST identify the affected policy revision, exact scope, authorized human owner, rationale, residual exposure, compensating conditions, expiry, and review trigger. An exception MUST NOT grant authority the approving actor does not possess or bypass an applicable non-overridable constraint. Renewal MUST be a recorded decision.

## TSM-010 — Access and history

Management records and evidence MUST have access, retention, and correction rules appropriate to their scope. Material decisions and assessments MUST preserve their history through linked revisions or events. Access to a summary MUST NOT imply access to its private source. Deletion or loss of evidence MUST be reflected in the limitations of later claims.

## TSM-011 — Learning and retirement

A claimed learning MUST identify the assumption assessed, evidence, limitations, and decision it may inform. Proposed learning MUST NOT silently modify policy or authority. Retirement MUST account for ongoing operations, unresolved effects, credentials or delegations to revoke, retention responsibilities, and an owner for remaining obligations.

## TSM-012 — Scoped assessment

A conformance claim MUST identify the specification revision, workflow and environment, applicable requirement results, evidence, reviewer, date, exceptions, and unresolved limitations. Planned checks and illustrative scenarios MUST NOT be reported as passed validation. A document, schema, test, or demonstration MUST only support the claim it actually establishes.

## Use proportionate records

A small team SHOULD combine related records where that keeps their meanings explicit. Separate responsibilities do not require separate meetings, databases, or services. Evidence collection and review effort SHOULD be measured alongside the value of the decisions they support.
