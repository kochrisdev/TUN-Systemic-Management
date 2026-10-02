# Local pilot validation — 2 October 2026

[Documentation index](README.md) · [Pilot guide](PILOT.md) · [Conformance matrix](CONFORMANCE-MATRIX.md)

## Scope and source

The tested implementation is [commit 44bcbcc](https://github.com/kochrisdev/TUN-Systemic-Management/commit/44bcbcc1d1cc9390ab386d76728d2a7208807c15). It contains the experimental schema, SQLite host, fixture scenario, and tests. This report and accompanying documentation updates are subsequent changes; they do not extend the implementation's tested behavior.

Validation was performed by the repository's AI development assistant in the local task environment. This is development verification, not independent review, prospective-user acceptance, organizational adoption, or complete specification conformance.

Environment: Windows 11 build 26200, Python 3.13.4, SQLite 3.49.1, and the exact versions in [requirements-pilot.txt](../requirements-pilot.txt), installed in a repository-local virtual environment. The runtime minimum is Python 3.11 because of the pinned dependency graph; other Python versions were not validated in this local run.

## Observed results

| Check | Actual result |
|---|---|
| `python -m unittest discover -s tests -v` | 30 tests passed; includes one fixture-manifest test with nine cases |
| `python -m reference.tsm_pilot.demo` | Completed; quality assessment contradicted, unknown-effect fixture preserved, mandate paused, fresh reservation blocked, reopen verified |
| `python -m pip check` | No broken requirements found |
| Documentation and whitespace checks | Run for the accompanying documentation update; check file links and requirement references, not runtime conformance |

The demo produced eight durable records before temporary cleanup. It reserved 35,000 of 60,000 USD cents and reported 25,000 cents remaining. No external effect or provider readback occurred. Its fixture clock was `2026-10-02T12:00:00Z`; that value is scenario data, not the time of this validation.

## Scenario coverage

| Evidence | Named tests or demonstration | Boundary |
|---|---|---|
| Revision and decision binding | `test_stale_approval_and_reservation_after_revision_are_blocked`, `test_repeated_approval_does_not_create_another_decision` | Local mandate and fixture owner only |
| Eligibility and scope | Tests for unapproved authority, expiry/future start, pause, revocation, wrong action/target | Blocks new local reservations; no provider dispatch |
| Shared resources | `test_concurrent_reservations_cannot_double_spend`, shared-ceiling and revision carry-over tests | SQLite reservation accounting; no spend settlement |
| Duplicate protection | `test_idempotent_reservations_require_exact_parameters` and pause replay test | Historical reservation replay only |
| Evidence meaning | Missing, operational-only, stale, conflicting, method/population mismatch, and correction tests | Synthetic supplied observations; provenance not authenticated |
| Scope and visibility | Role/scope tests, restricted review/decision propagation, cross-initiative evidence rejection | Caller-selected fixture identities, trusted local process |
| Persistence | Reopen/history test and demo | Reopening a committed database, not a crash during a transaction or power-loss test |
| Invalid inputs | Profile mutation cases, timestamps, duplicate keys, non-finite numbers, invalid budgets and database versions | Structural and selected semantic checks |

The initial test run exposed an unclosed SQLite connection in test setup on Windows. The test now explicitly closes those connections; the final 30-test run passed. This was a test-resource issue, not a claimed provider recovery exercise.

## Remaining gaps

No real identity, authenticated evidence ingestion, external provider, Design adapter, retention/deletion behavior, settlement/release mechanism, policy exception lifecycle, retirement workflow, or organizational usefulness assessment was tested. Lost-response and intervention evidence in the demo is synthetic. Real cancellation and reconciliation are not implemented. The automated Linux workflow is defined in this source; this local report does not claim a hosted CI result.

The broader specification requirements remain unassessed. These tests support only their named local behaviors.
