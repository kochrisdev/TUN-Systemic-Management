# Worked example: an incident and mandate pause

**Fictional alternative scenario.** This is a separate branch of the support example, not an additional reported event in its review data. No provider, runtime, or control has been exercised.

[Documentation index](../docs/README.md) · [Reviews and adaptation](../docs/REVIEWS-AND-ADAPTATION-v0.1.md)

## Trigger

An authorized reviewer approves reply proposal `reply-42`, revision `3`. The host dispatches operation `send-42`. The provider response is lost, and readback is temporarily unavailable. The host cannot establish whether the reply was sent.

Separately, the Support Lead learns that the knowledge-base article used for that reply may contain an incorrect instruction. The management evidence now includes both a possible content problem and an unknown operational effect.

## Management response and runtime response

| Moment | Management fact | Runtime or evidence fact |
|---|---|---|
| Initial escalation | The designated incident responder receives the unresolved case | `send-42` has an unknown effect; timeout does not establish failure |
| Pause decision | Authorized owner pauses new work using the affected article | A decision alone has not stopped a worker or provider |
| Control requested | Application owner requests prevention of new dispatch in the stated scope | Control is requested; accepted work may still complete |
| Acknowledgement | Management sees that the host accepted the request | Acknowledgement does not establish effectiveness |
| Control assessed | Review records evidence that new matching dispatch is blocked | Original send effect remains unknown |
| Reconciliation | A responder inspects the original operation using authorized readback | If unavailable, retain unknown; if found, verify the precise effect |
| Recovery decision | Owner evaluates a correction if the original send is established | Any corrective send is a new linked action with current approval and authorization |

The original unknown send is not retried under a new task ID. Creating a replacement initiative item or approving the same text again does not resolve duplicate-effect risk.

## Follow-up review

The review records the affected mandate and article revision, decisions made under uncertainty, actual control scope, and remaining obligations. It compares the incident with the original assumptions and assigns owners for correction, evidence lookup, and knowledge-base repair.

If the original effect remains unknown, a named responder retains the case. The initiative can remain paused while the investigation continues. A later evidence assessment links to the earlier one and explains what changed.

Any proposal to resume uses reviewed scope and current authority. The incident's learning can inform a new policy decision; it does not modify the policy automatically.
