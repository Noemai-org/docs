# Task card: GOV-19

Plan v1.2 task GOV-19. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P0-019  GOV-19 · Founders approve, amend or reject DEC-2026-10-12 and SoT v1.4 (PR A)
Priority: P0
Requirement IDs: REQ-ENV-007; SoT §36, §40.1, §0.4; BD-07; AGENT-29
Rationale: Tushe's response of 7 Oct 2026 changes who provides the case domain, ground truth, time and some faults. SoT §36 is a [DECISION], so the change needs a committed decision record, the SoT edit and the regenerated register in one pull request (AGENT-29). Without it, G0 cannot be held and G1 has no write target (DEC-2026-10-12 §9).
Modules touched (allowlist): none in code. Noemai-org/docs pull request #10 (PR A; originally PR #10, merge commit 88f59f9) only
Contracts: none; bump required? N
Inputs/outputs: PR A (DEC-2026-10-12, SoT v1.4, register, Tushe correspondence) → merged, or amendments recorded
Acceptance criteria:
  REQ-ENV-007:
  - The report SHALL list every AT and TEN result with the run seed and Tushe version.
  Task "Done when" (plan v1.2): PR A merged, or amendments recorded
Tests to write FIRST (AGENT-11): none (decision task); docs-consistency, perd_index and plan_index checks green on PR A
Faults to exercise (AGENT-12): none
Dependencies: GOV-01; REQ-ENV-007
Out of scope: any code; any change to the DEC other than founder amendments; sending documents to Tushe
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: FND. Open item for the founders: PR A raises one CONFLICT block (SoT §35.6 rule 4 is also amended by D3; the DEC's "Amends" line names only §36).
