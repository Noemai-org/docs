# Task card: ENV-12

Plan v1.3 task ENV-12 (moved from Tue 13 Oct to Fri 16 Oct by DEC-2026-10-12 Amendment 1). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P2-012  ENV-12 · Walk through, agree and sign the acceptance worksheet with Tushe at the 18:00 joint session (worksheet section 7)
Priority: P0
Requirement IDs: REQ-ENV-007; SoT §36, §40.1
Rationale: the joint session on Fri 16 Oct, 18:00–20:30 WAT, combines walkthrough, sign-off and the tests; the worksheet is signed first, so the tests that follow (ENV-07) are a demonstration, not a negotiation: each AT passes as written, under an amended condition both sides sign, or as an agreed exception with owner and date. DEC-2026-10-12, D7 and Amendment 1.
Modules touched (allowlist): docs/poc/tushe/acceptance/ (Noemai-org/docs)   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: G0-worksheet-2026-10-13-SENT.md and .pdf → the signed worksheet, committed as G0-worksheet-2026-10-16-SIGNED.md and .pdf
Acceptance criteria:
  REQ-ENV-007:
  - The report SHALL list every AT and TEN result with the run seed and Tushe version.
  Task "Done when" (plan v1.3): signed worksheet committed in `docs/poc/tushe/acceptance/`
Tests to write FIRST (AGENT-11): none (agreement task)
Faults to exercise (AGENT-12): none
Dependencies: ENV-01, GOV-19; REQ-ENV-007
Out of scope: editing the sent worksheet in place; adding internal strategy, benchmark details or held-out material to anything sent to Tushe
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owners: IL, EL. Day: Fri 16 Oct, 18:00 (plan v1.3).
