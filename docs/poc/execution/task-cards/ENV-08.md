# Task card: ENV-08

Plan v1.2 task ENV-08. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P2-008  ENV-08 · Build `mock-case` per REQ-ENV-008, with its fault hooks and truth endpoint, plus the core's case adapter to it (started Tue 13 Oct)
Priority: P0
Requirement IDs: REQ-ENV-008, REQ-ENV-001, REQ-ENV-004, REQ-TST-003; SoT IDs: US-05, US-06, US-19, POC-NFR-05, POC-NFR-08, AGENT-24; SoT §36
Rationale: Tushe does not provide a case domain (Tushe response, 7 Oct 2026); every POC write targets a case system (PERD §25.1). DEC-2026-10-12, D1.
Modules touched (allowlist; all paths in the `noema` repository, DEC-2026-10-13): synthetic/mock_case/ ([REC] path, PERD v1.2 §64.2, pending engineering-lead approval and GOV-02); services/core/adapters/synthetic_tushe/ (the case client only); benchmark/fault_plans/ (mock-case fault plans, authored and owned by the benchmark owner)   ← nothing else may change
Contracts: case, complaint and evidence payloads `fin.case`, `fin.complaint_ref`, `fin.evidence_attachment` (PERD §34.4); bump required? TODO(EL): confirm against /contracts v1 (CON-01)
Inputs/outputs: case commands from the core's case adapter → case, complaint and evidence records with version tokens; fault plans from the benchmark runner
Acceptance criteria:
  REQ-ENV-008:
  - The contract tests SHALL pass for every row of §34.4 that it serves.
  - Commit-then-drop SHALL be reproducible from a fault plan and seed.
  - Its truth endpoint SHALL refuse every runtime identity.
  - It SHALL be built and maintained by someone who does not build services/core, and its fault plans SHALL be owned by the benchmark owner.
  REQ-ENV-001:
  - Replacing an adapter with a stub implementing the same interface SHALL require no changes to Understanding, Trust, Execution or Outcome.
  REQ-ENV-004:
  - Running the same case with the same seed twice SHALL produce identical fault traces and identical authoritative outcomes.
  REQ-TST-003:
  - A contract change without a version bump SHALL fail CI.
  Task "Done when" (plan v1.2): contract tests pass; commit-then-drop reproduces from a fault plan; truth endpoint refuses runtime identities; case adapter contract tests green
Tests to write FIRST (AGENT-11): contract tests for every §34.4 case, complaint and evidence row; US-05, US-06, US-19; EC-E01, EC-E02, EC-E05, EC-E06, EC-E11, EC-E12, EC-E13, EC-E14, EC-K01; truth-endpoint refusal for each runtime identity
Faults to exercise (AGENT-12): FaultPlans with source MOCK_CASE (to be authored by the benchmark owner): commit then drop the response; 5xx; 429 with Retry-After; reject a stale version; paginate results
Dependencies: PLT-01, ENV-03, CON-03; REQ-ENV-004, REQ-ENV-002, REQ-NFR-006
Out of scope: any dispute lifecycle; any monetary operation; any change under services/core other than the case client; Tushe adapters (ENV-05, ENV-11)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

**Builder.** The builder must not be C1 or C2 (REQ-ENV-008; plan SR-19). Owner: IL, with a coding agent. The benchmark owner owns the fault plans and the truth endpoint.
