# Status and roadmap

Updated: 2 October 2026. [Documentation index](README.md) · [Scope](SCOPE.md)

## Current state

| Area | State |
|---|---|
| Concept, manifesto, management loop | Written as proposals |
| Twelve behavioral requirements | Draft-specified; all unassessed |
| Record semantics and lifecycle guidance | General model proposed; six-record experimental schema profile implemented |
| Decision, delegation, portfolio, measurement, review guidance | Written as draft guidance |
| Adoption templates | Available as Markdown |
| Support initiative and incident narratives | Written; fictional, not executed as full workflows |
| Local initiative-review fixture | Implemented; focused schema and runtime tests plus restart demonstration passed locally |
| Design and Engineering mappings | Documented against pinned source revisions; no adapter |
| Threat scenarios and assessment procedures | Complete requirements unassessed; selected local tests provide partial evidence |
| Local records, decisions, budget reservations, evidence review | Implemented with SQLite and fixture roles; see the named validation report |
| Production runtime, dashboard, SDK, autonomous management agent | Not implemented |
| Organizational adoption and decision-quality evidence | Not established |

## Next increments

The [2 October local validation report](PILOT-VALIDATION-2026-10-02.md) identifies the tested source and limitations. Prospective-user review remains open even though the technical prototype has progressed.

| Milestone | Work | Exit evidence |
|---|---|---|
| 1. Review the management contract | Walk through both scenarios with prospective users; resolve record and authority ambiguities | Named feedback, decisions, and consistent revised documents |
| 2. Define a narrow schema profile | Initial six-record profile and valid/invalid fixtures implemented; generalization and migration remain open | Initial local structural and semantic checks passed; compatibility is limited to the experimental profile |
| 3. Implement the local review pilot | Durable records, fixture roles, reservations, evidence assessments, and review history implemented | Local tests and restart demo passed; real identity and full lifecycle coverage remain open |
| 4. Connect one engineering operation | Preserve mandate links and verified, partial, and unresolved effects | Adapter results against pinned host and provider revisions |
| 5. Present the human review | Use appropriate Design components and management-specific views | Observed comprehension, accessibility review, and control-path results |
| 6. Run one named organizational adoption | Use actual owners and a bounded workflow; measure effort and decision usefulness | Operator feedback, outcome limitations, and scoped assessment |
| 7. Generalize from demonstrated reuse | Refine portfolio support, packaging, and additional providers | Evidence that the shared model fits another workflow |

Each increment should produce a usable result and evidence for its claims. A larger platform, hosted site, or package can follow demonstrated adoption needs.

## Reporting progress

Update artifact state only when the artifact exists or the named check has run. Preserve original evidence and its environment. Do not turn planned procedures or fictional scenarios into passed tests when adding implementation.
