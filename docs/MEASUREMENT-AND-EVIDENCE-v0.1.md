# Measurement and evidence v0.1

Status: draft guidance. [Documentation index](README.md) · [Review template](../templates/review-record.md)

## Claims at different levels

| Claim | Relevant evidence | What it does not establish by itself |
|---|---|---|
| An action occurred | Bound provider observation and engineering verification | Content quality, customer benefit, or enduring state |
| A reply met quality criteria | Defined evaluation against a stated sample and rubric | Every future reply will meet those criteria |
| Support outcomes improved | Comparable outcome observations with population and timeframe | The AI intervention caused the improvement |
| AI caused the improvement | An appropriate comparison design and analysis of competing explanations | Transfer to another population or operating condition |

Management should use operational evidence wherever relevant, while retaining the separate evidence needed for product and organizational claims. Contextual observations and user testimony can be useful evidence when their limits are explicit.

## Define metrics before interpreting them

A metric definition includes its owner, decision purpose, formula, units, denominator, population, collection source, observation window, baseline, target or trigger, missing-data rule, and limitations. Distinguish collection time from the period measured. Record method changes as new versions so historical results remain interpretable.

Do not invent a baseline from a model estimate. Do not treat missing observations as zero. A self-reported confidence score does not replace a measurement or evidence assessment.

## A balanced measurement set

| Dimension | Candidate measures |
|---|---|
| Value | Resolution quality, repeat contact, customer effort, time to useful outcome |
| Reliability | Verified effects, unresolved-operation age, recovery completion |
| Risk | Scope violations, material adverse effects, exceptions and their age |
| Economics | Total cost per eligible case, review effort, rework and recovery cost |
| Human experience | Review burden, reported workload, override reasons, affected people's feedback |
| Learning | Assumptions assessed, time to resolve uncertainty, decisions revised with evidence |

Select only measures that inform a real decision. Define countermeasures for incentives that could distort them: faster replies paired with resolution quality, for example. An override rate can signal either poor automation or effective supervision; investigate its meaning before using it as a target.

## Evidence handling

Each assessment identifies a claim, subject revision where relevant, evidence sources, observation window, assessment time, method, and limitations. Keep supporting and contradictory observations. A source's authority to report an effect differs from its accessibility to a particular viewer.

An agent may prepare a summary, but the system should retain references and enable verification of material claims. Missing, stale, restricted, or deleted sources remain explicit limitations. A management summary cannot expand access to the underlying information.

Outcome reports should distinguish observed change, the team's interpretation, and causal conclusions. Compare against the original criteria, disclose population shifts and missing data, and describe why the evidence supports the chosen management action.
