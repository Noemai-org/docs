# Task card: ENV-12

Plan v1.2 task ENV-12. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P2-012  ENV-12 · Acceptance worksheet agreed and signed with Tushe on the Tuesday call; definitions 1.1 to 1.3 recorded
Priority: P0
Requirement IDs: REQ-ENV-007; SoT §36, §40.1
Rationale: Thursday's joint session must be a demonstration, not a negotiation: each AT passes as written, under an amended condition both sides sign, or as an agreed exception with owner and date. DEC-2026-10-12, D7.
Modules touched (allowlist): docs/poc/tushe/acceptance/ (noema-org/docs)   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: G0-worksheet-2026-10-12-DRAFT.pdf → the signed worksheet, committed as a separate file
Acceptance criteria:
  REQ-ENV-007:
  - The report SHALL list every AT and TEN result with the run seed and Tushe version.
  Task "Done when" (plan v1.2): signed worksheet committed in `docs/poc/tushe/acceptance/`
Tests to write FIRST (AGENT-11): none (agreement task)
Faults to exercise (AGENT-12): none
Dependencies: ENV-01, GOV-19; REQ-ENV-007
Out of scope: editing the draft worksheet in place; adding internal strategy, benchmark details or held-out material to anything sent to Tushe
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owners: IL, EL.
