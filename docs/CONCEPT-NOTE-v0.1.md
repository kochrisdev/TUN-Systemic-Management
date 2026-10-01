# Concept note v0.1

Status: proposal. [Documentation index](README.md) · [Scope](SCOPE.md)

## Definition

TUN Systemic Management is a proposed management discipline for directing human and machine intelligence toward valuable outcomes through explicit mandates, bounded delegation, evidence-based decisions, and continuous organizational learning.

It covers both managing AI initiatives and using AI to assist management. The first development boundary is narrower: one initiative, its owner, its delegated work, and a review based on traceable evidence.

## Management responsibilities

| Responsibility | Question | Primary record |
|---|---|---|
| Purpose | What change matters, and to whom? | Outcome |
| Investment | Which initiative merits resources now? | Initiative and Decision |
| Accountability | Who owns the result and the unresolved issues? | Mandate |
| Authority | What may each actor do under which conditions? | Delegation |
| Coordination | Who owes what, and which work depends on it? | Commitment and Dependency |
| Observation | What does the evidence establish? | Signal and Observation |
| Adaptation | What should change in response? | Review and LearningRecord |

## Proposed foundations

Use the loop SENSE → FRAME → DECIDE → DELEGATE → OBSERVE → ADAPT. Give consequential decisions durable records. Separate recommendations, human decisions, organizational authority, runtime authorization, and effects. Version the material meaning of mandates and delegations. Preserve uncertainty and conflicting observations. Include human review time and recovery cost in the economics of an initiative.

The model can be used manually before software exists. A small implementation can hold the management records in one durable store and integrate with one engineering host. It does not require an autonomous management agent, a graph database, or multiple services.

## Initial artifacts

The repository supplies a manifesto, twelve draft requirements, a record vocabulary, operating guidance, three templates, and two illustrative scenarios. General JSON schemas, persistent software, adapters, and organizational validation are future work.

The first pilot should answer: can a team trace a review decision from an outcome and current mandate through relevant evidence, including unresolved operations, without silently increasing authority?

## Development approach

First review the draft against the support initiative and incident scenarios. Then implement the minimum record subset needed for the initiative review. Challenge stale mandates, insufficient evidence, budget exhaustion, lost responses, and failed intervention. Add integrations only after their meaning is explicit. Publish results with their environment, revisions, limitations, and responsible reviewers.

Success means a team can make a better-supported management decision with an understandable amount of work. Schema validity or a successful demonstration alone cannot establish that benefit.
