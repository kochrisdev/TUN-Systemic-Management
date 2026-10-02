# Local pilot: AI Initiative Review

Status: experimental implementation with focused local validation. [Documentation index](README.md) · [Validation report](PILOT-VALIDATION-2026-10-02.md) · [Schema profile](../schemas/README.md)

## Question

Can a team trace a review decision from an organizational outcome and bounded mandate through scoped evidence, while preserving unknown effects and current authority?

## Run the demonstration

Requires Python 3.11 or later; the named local validation used Python 3.13.4. From the repository root on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-pilot.txt
.\.venv\Scripts\python.exe -m reference.tsm_pilot.demo
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

On macOS or Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-pilot.txt
.venv/bin/python -m reference.tsm_pilot.demo
.venv/bin/python -m unittest discover -s tests -v
```

These commands install into a repository-local environment. No credentials, model API, network service, or provider configuration is needed to run the installed pilot.

The demo uses a fixed synthetic clock at `2026-10-02T12:00:00Z`. The runtime uses the current UTC clock unless a fixture clock is explicitly supplied. The demo's default temporary database is removed when the run ends. To retain it, use a new path:

```powershell
.\.venv\Scripts\python.exe -m reference.tsm_pilot.demo --db .pilot-data/first-run.sqlite3
```

The command refuses existing paths. Choose another filename for a new run. `.pilot-data/` is ignored by Git.

## Implemented workflow

The host creates an initiative with an embedded outcome and metric criteria, proposes a mandate with embedded delegation, and records a human-fixture decision about the exact mandate revision. Its agent fixture can reserve resources only within the currently active revision's actions, targets, interval, and limits. An SQLite transaction prevents concurrent reservations from spending the same headroom twice.

Revisions are immutable. Proposing a new mandate revision makes the mandate proposed and prevents fresh reservations against the old revision. Approval does not carry over. Paused or revoked mandates require a new reviewed revision to resume in this profile. Existing reservations remain recorded and continue to consume capacity.

Observation records distinguish outcome measurements from operation reports. Reviews inspect all current observations for the selected initiative and exact observation window, excluding explicitly superseded records while retaining their history. Stale or method/population-mismatched measurements cannot support a criterion. Conflicting measurements remain visible. An operation marked verified cannot satisfy an outcome criterion.

A review's proposed action is a recommendation. It does not activate, pause, expand, or retire a mandate. A fixture owner must separately record a supported decision. The implemented decision actions are approve, reject, pause, and revoke; portfolio retirement and budget increases are not implemented.

## Expected demo result

The fixture measures draft quality at 90% against a 95% threshold, so the review assessment is `contradicted`. An unknown-effect fixture remains explicit in the review limitations. The owner pauses the mandate; a fresh reservation is rejected. Reopening the database preserves the review and earlier reservation.

The demo reserves USD 350 of a USD 600 ceiling, leaving USD 250 of local reservation headroom. This is a separate synthetic scenario from the longer [Markdown support narrative](../examples/ai-support-initiative.md), which includes other commitments and costs.

## Identity and evidence boundaries

Callers select a fixed fixture identity: `owner-a`, `reviewer-a`, `viewer-a`, `agent-a`, or a separate scope's `owner-b` and `agent-b`. Owners manage their initiative and mandate decisions. Owners and reviewers can supply observations and create review recommendations. The delegate agent reserves resources. Viewers can read team-visible records. Reviewers-only evidence makes derived reviews and linked decisions reviewers-only.

This selection mechanism is not authentication. The Python process and database access are trusted. Source references are recorded, not authenticated or fetched. The program does not encrypt records, implement retention/deletion, or provide an independently tamper-proof audit log.

Reservations are accounting commitments, not provider execution grants or measured spending. Duplicate request identities return the original historical reservation only when all parameters match, even after a later pause; they never issue new authority. There is no settlement or capacity-release API in this increment.

## Remaining acceptance work

The [validation report](PILOT-VALIDATION-2026-10-02.md) maps actual local checks. Real identity, authenticated evidence, provider dispatch, lost-response reconciliation, cancellation acknowledgements, recovery, and Design components remain future integrations. The [incident narrative](../examples/incident-and-mandate-pause.md) still describes behavior beyond this local boundary. Complete [specification assessments](CONFORMANCE-MATRIX.md) remain unassessed.
