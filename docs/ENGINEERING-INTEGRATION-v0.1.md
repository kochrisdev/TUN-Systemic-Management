# Engineering integration v0.1

Status: proposed contract mapping; no management-to-engineering adapter is implemented. [Documentation index](README.md) · [Decisions and delegation](DECISIONS-AND-DELEGATION-v0.1.md)

## Inspected baseline

This guide uses TUN Systemic Engineering at [commit 4aee708](https://github.com/kochrisdev/TUN-Systemic-Engineering/tree/4aee7085f1cc4dd4e95cd3f4a5d8641c8cd90eb9), specifically its [contracts](https://github.com/kochrisdev/TUN-Systemic-Engineering/blob/4aee7085f1cc4dd4e95cd3f4a5d8641c8cd90eb9/docs/CONTRACTS-v0.1.md), [lifecycles](https://github.com/kochrisdev/TUN-Systemic-Engineering/blob/4aee7085f1cc4dd4e95cd3f4a5d8641c8cd90eb9/docs/LIFECYCLES-v0.1.md), and [scope](https://github.com/kochrisdev/TUN-Systemic-Engineering/blob/4aee7085f1cc4dd4e95cd3f4a5d8641c8cd90eb9/docs/SCOPE.md).

That baseline supplies draft general contracts and a narrower experimental publication pilot. It does not establish that the support example in this repository can already execute through those contracts.

## Mapping responsibilities

| Management concept | Engineering relationship | Required preservation |
|---|---|---|
| Outcome and Mandate | Inputs to a scoped IntentContract | Purpose, owner, constraints, stopping conditions |
| Delegation | Input to host policy and DelegationRecord | Actor, operations, targets, data scope, budgets, expiry, revocation |
| Management Decision | Organizational basis for a proposed action or policy | Subject revision and accountable owner; no automatic execution grant |
| Proposed consequential action | ActionProposal and ApprovalDecision where required | Exact material meaning, current identity, and decision rights |
| Runtime permission | AuthorizationDecision and ExecutionGrant | Current host policy and bound operation, actor, target, and validity |
| Execution | OperationRecord and ExecutionAttempt | One logical operation across permitted attempts |
| Operational evidence | VerificationRecord and ActionRecord | Claim, effect scope, source, observation time, unresolved conditions |
| Pause or recovery decision | InterventionRequest or linked RecoveryOperation | Requested control scope, observed result, fresh authority where needed |

Similar terminology does not make the record shapes interchangeable. The adapter resolves and validates each boundary. The management delegation is an organizational source of authority; its host representation still needs current checks at dispatch.

## Proposed evidence flow

Store references from the initiative and mandate revision to the engineering operation and action-record revision. Ingest authenticated verification references into a scoped management assessment. Preserve the distinction between verified subclaims, unresolved effects, and missing evidence.

A verified publication can support “the approved update was published to this provider.” It cannot by itself support “customers understood the update” or “the initiative improved retention.” Those claims need separate observations and analysis.

## Revocation and uncertainty

Define how the host learns that a mandate expired, changed, or was revoked, and what it does when current policy cannot be established. For consequential dispatch, unavailable authority information should prevent new dispatch unless an explicitly valid, bounded offline policy covers that exact circumstance.

After a provider accepts work, cancellation depends on the provider boundary. A management pause does not erase accepted or unknown effects. A lost response stays associated with its original logical operation for reconciliation. A new initiative task or management approval cannot make an unsafe duplicate attempt safe.

## Integration acceptance

The planned pilot should demonstrate denial after revocation, rejection of a stale mandate revision, shared budget limits across concurrent work, and a lost-response path that remains unresolved until evidence supports a result. It should also show a completed operation whose organizational outcome remains insufficiently supported.

Record the tested management, engineering, adapter, and provider revisions and the scope of each result. Tests from a companion repository cannot be transferred as evidence that this integration works.
