# Worked example: an AI support initiative

**Fictional scenario.** All identities, dates, thresholds, costs, and observations below are illustrative. No experiment or software run is reported here.

[Documentation index](../docs/README.md) · [Initiative charter](../templates/initiative-charter.md)

## 1. Frame the outcome

Initiative `initiative-support-01`, revision `1`, aims to reduce staff handling time for routine support cases while maintaining response quality and resolution outcomes. The accountable owner is the Support Lead. The Operations Sponsor can approve the experiment's budget and scope.

Alternatives are continuing the current workflow, improving the knowledge base, or piloting assisted drafting. The initial decision selects a two-week drafting experiment for one support queue, from `2026-10-01T09:00:00Z` to `2026-10-15T09:00:00Z`.

The fictional baseline is 100 eligible cases from the preceding two weeks, with median staff handling time of 10 minutes and 10 reopened cases within seven days. The team records possible case-mix differences. Baseline quality under the new evaluation rubric is unknown and needs a comparable sample; no quality improvement claim is available yet.

The illustrative continuation criteria are median handling time at most 8 minutes, at least 95% of sampled drafts meeting the defined quality rubric, and a seven-day reopen rate no greater than 10%. These are this fictional team's criteria, not universal TUN targets.

## 2. Decide and delegate

Decision `decision-support-start-01` approves initiative revision `1` and mandate `mandate-support-01`, revision `1`. The agent may read assigned cases and approved knowledge-base articles and create drafts. It may not change customer account settings, grant refunds, or broaden its data access.

An assigned human reviewer must approve the exact reply and recipient before a separate host-controlled send action. The drafting agent has no independent send authority. The host rechecks permission and the proposal revision at dispatch.

The total pilot resource ceiling is USD 600, including the agreed valuation of reviewer effort. Further delegation is prohibited. The Support Lead can request a pause; the application owner operates and observes the actual control path. New drafting and sending must stop when the relevant authority expires, subject to the documented boundary for work already accepted by a provider.

The reviewer acknowledges the sampling commitment, the application owner owns runtime enforcement, and the data analyst owns the baseline and outcome measurements. A shared knowledge-base update is a dependency with its own owner.

## 3. Observe without collapsing claims

At the fictional interim review on `2026-10-08T09:00:00Z`, the record contains:

| Observation | Illustrative value | Interpretation limit |
|---|---|---|
| Eligible pilot cases | 80 | Case mix may differ from baseline |
| Median staff handling time | 7 minutes across the 80 cases | Association during the pilot; causal effect is not established |
| Drafts meeting the rubric before correction | 72 of 80, or 90% | Below the 95% criterion; final sent replies can still have been corrected |
| Seven-day reopen rate | Not yet available for the complete cohort | Cannot establish the resolution criterion |
| Provider send effects | 80 verified operation claims | Establish only the defined send effect, not customer understanding or resolution |
| Model and tool cost | USD 90 | Fictional observed cost for the window |
| Infrastructure cost | USD 20 | Fictional allocated cost for the window |
| Reviewer effort | 8 hours at USD 30/hour = USD 240 | Valuation is part of this pilot's accounting rule |
| Total observed cost | USD 350 | USD 90 + USD 20 + USD 240 |
| Outstanding commitments | USD 30 | Counted against the shared ceiling |
| Remaining headroom | USD 220 | USD 600 minus USD 350 minus USD 30; future work still needs current authority |

The report links each value to a hypothetical metric definition, observation window, and source record. Evidence references here are illustrative labels, not existing logs or receipts. The product outcome assessment remains insufficient: speed improved in the observed sample, draft quality missed the criterion, and resolution evidence is incomplete.

## 4. Review and adapt

Review `review-support-01` considers continuing unchanged, revising the knowledge base and sampling again, or retiring the experiment. The Support Lead recommends a pause in new drafting while the team investigates the recurring quality errors. The Operations Sponsor records the selected change and its resource implications in `decision-support-change-01`.

A proposed mandate revision `2` narrows the next experiment to a defined subset of cases after the knowledge-base changes are reviewed. Prior approval does not automatically activate revision `2`. The pause request, host acknowledgement, and evidence that new dispatch has stopped are recorded separately.

Follow-ups assign the knowledge-base owner to correct the observed gaps, the analyst to complete the seven-day measurements, and the application owner to account for any ongoing operations. A further review is set for `2026-10-15T09:00:00Z` or earlier if a material incident occurs. No extension beyond expiry is assumed.

## 5. Preserve the learning

A candidate learning says that handling-time improvement alone was insufficient to justify expansion. The observed draft errors suggest a knowledge-base gap, but the causal explanation remains a hypothesis until examined. The review records both the learning and the uncertainty.

The example demonstrates how to reason across outcome, mandate, authority, operations, and evidence. It does not demonstrate software conformance or real business improvement.
