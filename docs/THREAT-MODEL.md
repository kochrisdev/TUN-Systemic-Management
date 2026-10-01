# Management threat model

Status: initial scenario analysis; controls and challenges are proposed. [Documentation index](README.md) · [Conformance matrix](CONFORMANCE-MATRIX.md)

## Assets and actors

Protect the integrity of decisions, authority, budgets, outcome claims, organizational memory, and private evidence. Relevant actors include authorized and unauthorized people, agents, source authors, providers, and services. Failure can arise through error, incentives, stale information, or deliberate manipulation.

## Failure scenarios

| Failure | Consequence | Proposed control and challenge | Requirement |
|---|---|---|---|
| A task count becomes a success claim | Investment continues without benefit | Require outcome criteria; challenge a completed initiative with poor user results | TSM-001, TSM-006 |
| An agent-authored recommendation becomes an approved decision | Accountability and decision rights disappear | Separate recommendation provenance from an authenticated decision; submit an unsigned recommendation | TSM-002 |
| A changed mandate reuses old approval | Unreviewed authority expansion | Bind decisions to revisions; change targets or spending limits after approval | TSM-003, TSM-004 |
| Child agents each reuse a parent budget | Aggregate overspend | Shared reservations and authority chain checks; race concurrent work | TSM-003, TSM-005 |
| A fluent report conceals missing or conflicting evidence | False confidence in performance | Preserve source and claim limits; remove or contradict an observation | TSM-006 |
| A repeated exception never expires | Temporary discretion becomes permanent | Expiry and explicit renewal; attempt use after expiry | TSM-009 |
| A stop acknowledgement becomes “all work stopped” | Accepted or unknown effects are overlooked | Separate control lifecycle and provider effects; lose a response during pause | TSM-008 |
| Private evidence leaks through summaries | Unauthorized disclosure | Enforce projection and source access; inspect a restricted viewer's output | TSM-010 |
| A retrospective silently changes policy | Unreviewed authority change | Learning proposes a new decision; submit generated policy edits | TSM-004, TSM-011 |
| Retired initiatives retain active authority | Unowned effects and costs continue | Close delegations and assign residual obligations; attempt new dispatch after retirement | TSM-011 |
| Planned checks are presented as validation | Unsupported adoption or safety claims | Require scoped assessment evidence; review a report with missing runs | TSM-012 |
| Approval load exceeds review capacity | People approve without meaningful scrutiny | Measure review burden; inspect rushed approvals and adjust mandate scope | TSM-005, TSM-007 |

This analysis does not replace the application's security threat model or domain-specific assessment. Additional scenarios should come from the actual workflow and its affected people.
