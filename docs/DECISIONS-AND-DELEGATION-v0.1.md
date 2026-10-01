# Decisions and delegation v0.1

Status: draft guidance. [Documentation index](README.md) · [Decision template](../templates/decision-record.md)

## Distinct questions

| Concept | Question |
|---|---|
| Recommendation | What does an analyst, agent, or team suggest? |
| Decision | What did an authorized owner choose, and why? |
| Mandate | What purpose and responsibility were assigned? |
| Delegation | What discretion and capabilities were permitted? |
| Runtime authorization | Is this actor allowed to perform this exact action now? |
| Verification | What effects does the evidence establish? |

A mandate to improve support does not authorize reading every customer record. A budget allocation does not authorize every purchase below that amount. Approval to pilot an agent does not transfer approval to materially changed content or targets.

## A decision worth preserving

Record the problem, subject revision, decision owner, affected stakeholders, viable alternatives, evidence and its limitations, selected option, rationale, dissent, and a review condition. Identify any AI-generated recommendation and the sources behind it. Unaccepted recommendations remain separate from approved decisions.

Routine recurring decisions may use a reviewed policy within explicit limits. Record the policy version and accountable human owner for each resulting decision. An agent cannot create a policy that grants itself additional authority.

## The delegation envelope

Specify the delegator, delegate, accountable human, mandate revision, permitted operations, targets, data scope, resource ceilings, start and expiry times, required approvals, prohibited actions, escalation triggers, and intervention path. Also specify whether the delegate can delegate again and which shared limits apply.

Implementation should resolve the full chain of current authority. A child record cannot extend a parent's expiry, broaden its data access, or treat its remaining budget as a fresh allocation. Shared budget reservations and policy checks belong in the enforcement path.

## Change and revocation

Changing material scope, actor, targets, budgets, or validity creates a new revision and decision where required. Revocation prevents future use according to the host's documented boundary. It does not establish that previously dispatched work stopped or that external effects were undone.

After revocation, inspect ongoing and unresolved operations. Record any requested intervention and its observed result. Reconciliation determines what happened. Correction, compensation, or restoration may require separate authority.

## Exceptions

An exception is a bounded decision about a particular policy and scope. Record its owner, reason, expiry, residual exposure, compensating conditions, and review trigger. The exception owner needs authority to grant it. Constraints declared non-overridable stay in force.

When the evidence needed to justify an exception is unavailable, record that limitation. A model's confidence cannot supply missing permission or evidence.
