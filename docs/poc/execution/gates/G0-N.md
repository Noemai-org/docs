# Gate record: G0-N Phase A exit, Noema half

<!-- Template: ../templates/gate-record.md. Fill only at the gate meeting, from evidence on the screen (plan §3.1). Never pre-fill. Internal: TEN details stay out of the Tushe folder (DEC-2026-10-16 E4; AGENTS.md §4). -->

- Gate: G0-N, Phase A exit, Noema half (DEC-2026-10-16 E4). G0 passes when G0-N and G0-T both pass; G1 may run before G0-T and counts only once G0 passes.
- Date and time (WAT): scheduled Thu 22 Oct 2026, 17:00 (DEC-2026-10-16 E3; plan task ENV-14). Held on: _not yet held_
- Deciders: Engineering lead, integration lead, benchmark owner (the roles are held by the Founder and the Technical Co-Founder, DEC-2026-10-16 E2)
- Must be true (checklist): see below
- Evidence links: _none yet_
- Outcome: `PASS | FAIL | BLOCKED` — **pending**
- If it failed, what happens next: _not applicable yet_
- Regression cases added: _none yet_
- Signatures: _none yet_

## Must be true (all of it, plan §3.1)

- [ ] TEN-01 to TEN-08 pass (table below)
- [ ] `/contracts` v1 tagged
- [ ] ≥ 50 fixtures reproducible
- [ ] Isolation tests pass, including runtime refusal on Tushe `/partner/...` routes and on the `mock-case` truth endpoint

Evidence to show: the Noema-side TEN results with the run seed; the contracts tag; the fixture run log twice with identical output; the isolation test log.

If it fails: Phase B work continues on adapters and core logic. The Noema-covered exceptions AT-04, AT-05, AT-07 and AT-14 not shown internally before the G1 review (Mon 26 Oct, 10:00) block G1.

## TEN-01 to TEN-08 (PERD §34.5 [REC])

Noema's own checks against Tushe, run by the integration lead. They are internal: not in the worksheet and never sent to Tushe. Wording is copied from PERD v1.5 §34.5.

| ID | Check |
|---|---|
| TEN-01 | No runtime container can reach the oracle (network and credential) |
| TEN-02 | A replayed scenario gives identical Trust decisions and verdicts |
| TEN-03 | Every case read returns a version token, and a stale expected version is rejected with no change |
| TEN-04 | A case committed with its response dropped is found by idempotency key |
| TEN-05 | Tushe time is controlled per object; Noema's simulated clock applies only in tests and replays, and advances together with Temporal test time |
| TEN-06 | Every integration-hostility fault (429, pagination, schema drift, near-timeout, skew) can be produced on demand |
| TEN-07 | Every evidence response carries the provenance fields of §21.1 |
| TEN-08 | The Noema integration credential cannot perform any prohibited operation in Tushe |

| ID | Result | Run seed | Evidence link |
|---|---|---|---|
| TEN-01 to TEN-08 | pending | — | — |

## Internal notes (Noema only; do not share)

Internal targets for showing the Noema-covered tests (DEC-2026-10-12, Amendment 1, with the dates moved by DEC-2026-10-16 E3):

- AT-04, AT-05, AT-07 and AT-14: before the G1 review (Mon 26 Oct, 10:00);
- AT-17: within two working days of Tushe delivering R2.

Tushe hears only "once complete".
