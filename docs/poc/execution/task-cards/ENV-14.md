# Task card: ENV-14

Plan v1.5 task ENV-14 (the Noema half of G0, split from ENV-07 by DEC-2026-10-16 E4). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-16](../../../decisions/DEC-2026-10-16-execution-reset.md) E3 and E4.

```
TASK-P2-014  ENV-14 · G0-N, the Noema half of G0, Thu 22 Oct 17:00: TEN-01 to TEN-08 pass; `/contracts` v1 tagged; ≥ 50 fixtures reproducible; the isolation tests pass, including runtime refusal on Tushe `/partner/...` routes and on the `mock-case` truth endpoint. Internal: not in the worksheet and not sent to Tushe
Priority: P0
Requirement IDs: REQ-ENV-007, REQ-ENV-002; SoT §36, §40.1
Rationale: G0 has two halves and both must pass (DEC-2026-10-16 E4). The Tushe half (ENV-07, G0-T) waits for a date Tushe confirms; the Noema half does not, so G1 can run and its evidence can be recorded. It counts only once G0 passes.
Modules touched (allowlist): docs/poc/tushe/acceptance/ (the TEN report); tests   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: the TEN checks of PERD §34.5, the contracts tag, the fixture run log and the isolation test log in → a Noema-side report in docs/poc/tushe/acceptance/ (TEN results with run seed), kept apart from the worksheet results
Acceptance criteria:
  REQ-ENV-007:
  - The report SHALL list every AT and TEN result with the run seed and Tushe version.
  REQ-ENV-002:
  - Network connections from the core or model service to the `mock-case` truth endpoint, the proxy control API or the benchmark runner SHALL fail.
  - A call by any runtime identity to a Tushe `/partner/...` route or to the `mock-case` truth endpoint SHALL be refused.
  Task "Done when" (plan v1.5): Noema-side TEN report with run seed committed in `docs/poc/tushe/acceptance/`; contracts tag and fixture run log linked → G0-N
Tests to write FIRST (AGENT-11): TEN-01 to TEN-08 as written in PERD §34.5; the isolation matrix (SEC-02); two identical fixture runs
Faults to exercise (AGENT-12): the integration-hostility faults of TEN-06 (429, pagination, schema drift, near-timeout, skew)
Dependencies: CON-03, ENV-05, ENV-06, BEN-04, ENV-08, ENV-09, ENV-13, SEC-02; REQ-ENV-007, REQ-ENV-002
Out of scope: the AT tests and the signed worksheet (ENV-12, ENV-07); sending any TEN detail to Tushe (TEN checks are internal)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owners: IL, EL, B.
