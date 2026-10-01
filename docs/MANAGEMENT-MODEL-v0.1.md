# Management model v0.1

Status: proposed model. [Documentation index](README.md) · [Records](RECORDS-AND-LIFECYCLES-v0.1.md)

## The management loop

| Stage | Management work | Output or decision |
|---|---|---|
| Sense | Gather customer, operational, cost, organizational, and external signals | Scoped signals, concerns, and unknowns |
| Frame | Define the situation, affected people, desired outcome, alternatives, and constraints | Outcome and initiative charter |
| Decide | Evaluate alternatives and current evidence; assign an accountable decision owner | Versioned decision and resource commitment |
| Delegate | Assign responsibilities and permitted discretion | Mandate, delegation, commitments, and escalation route |
| Observe | Compare observations against the outcome, guardrails, and assumptions | Evidence assessment and exceptions requiring attention |
| Adapt | Review whether to continue, change, expand, pause, or retire | New decision and any required control requests |

These are management activities, not a single runtime state machine. Observation can continue while a mandate is paused. A policy change can trigger a new decision before the regular review. Urgent intervention need not wait for a complete portfolio review.

## The same loop at different scopes

| Scope | Accountable question | Typical boundary |
|---|---|---|
| Portfolio | Which outcomes and investments deserve resources? | Shared budget, review capacity, priorities |
| Product or service | Which capabilities create value for its users? | Product outcomes, quality, operational ownership |
| Initiative | What bounded experiment or change should happen? | Mandate, resources, acceptance and stop conditions |
| Team or agent mandate | What work can this actor undertake? | Capabilities, targets, duration, delegation limits |

Each child scope references the parent purpose and applicable limits. Local decisions cannot enlarge parent authority. Shared resource ceilings apply across child mandates and retries; splitting work into smaller records does not create more budget.

## Management views

An outcome view explains desired change, progress, evidence, and uncertainties. A portfolio view compares investments and dependencies. A delegation view shows who may do what and until when. A review view presents decisions that need attention and the evidence that changed.

Views are access-filtered projections of records. A concise status can help navigation, but people must be able to inspect the facts behind it. A green initiative label cannot conceal an unresolved material effect.

## Coordination

Commitments identify an owner, expected contribution, due condition, and acceptance evidence. Dependencies identify the work or resource another commitment relies on and who responds if it fails. Handoffs require acknowledgement by the receiving owner; an agent's assignment message alone does not establish a human commitment.

Escalations identify the decision required, urgency, current containment, known effects, and responsible responder. Repeated alerts should be grouped around the underlying condition so management protects human attention while keeping material changes visible.
