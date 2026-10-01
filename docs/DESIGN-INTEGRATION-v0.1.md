# Design integration v0.1

Status: proposed mapping; no management presentation adapter is implemented. [Documentation index](README.md) · [Architecture](ARCHITECTURE.md)

## Inspected baseline

This guide uses TUN Systemic Design at [commit f1cc566](https://github.com/kochrisdev/TUN-Systemic-Design/tree/f1cc566c44a04741e51ce642ffaa0feab0bd5b36), including its [architecture](https://github.com/kochrisdev/TUN-Systemic-Design/blob/f1cc566c44a04741e51ce642ffaa0feab0bd5b36/docs/ARCHITECTURE.md) and [React contracts](https://github.com/kochrisdev/TUN-Systemic-Design/blob/f1cc566c44a04741e51ce642ffaa0feab0bd5b36/packages/react/src/contracts.ts). It does not claim compatibility with uninspected revisions or a working integration.

## Potential reuse

| Existing design pattern | Proposed management use | Boundary to preserve |
|---|---|---|
| IntentComposer | Collect outcome and initiative intent | Input does not create an approved mandate |
| ContextPanel and SourceView | Present review basis and permitted evidence | Sources need access checks and honest limitations |
| PlanView | Explain initiative steps, commitments, and dependencies | Reviewing a plan does not grant runtime authority |
| ProposalCard and ApprovalGate | Review a concrete effectful management action, such as activating a bounded delegation | Host owns the canonical proposal and validates the exact version |
| AgentCard | Explain an agent's purpose and declared authority | Displayed authority is a projection of enforced records |
| UncertaintySignal | Explain the limits of a scoped assessment | Status cannot manufacture confidence or proof |
| AgentActivity and ToolActivity | Show relevant observed work | Activity does not establish organizational benefit |
| HumanOverride and RecoveryControl | Request supported operational intervention | Request acknowledgement and actual effect remain separate |
| ActionReceipt | Present a verified operation effect | An action receipt cannot stand in for an outcome review |
| MemoryIndicator | Explain relevant use of retained context | Context use, retention, and training remain separate questions |

## Where management needs additional views

Portfolio comparison, outcome assessment, investment state, and review decisions require management-specific information. Compose views around those records without forcing them into an action receipt or a single operational status.

The inspected ApprovalGate returns a proposal ID, proposal version, and approve/reject decision. Its host must authenticate the reviewer, resolve the material proposal, record the decision, and enforce any resulting action. It is suitable only when the management action can be represented faithfully by that contract.

Keep the approved decision, current mandate eligibility, runtime authorization, and effect assessment visible as distinct facts. A review may recommend continuation while the host denies a specific operation under current policy.

## Future acceptance

Pin the design and host revisions used by an adapter. Exercise stale proposals, restricted evidence, denied execution after approval, unknown effects, and late intervention results. Review accessibility and whether people understand the difference between operational completion and outcome evidence. Component existence alone does not establish acceptance of a management workflow.
