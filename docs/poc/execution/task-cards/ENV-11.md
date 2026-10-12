# Task card: ENV-11

Plan v1.2 task ENV-11. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P2-011  ENV-11 · Tushe adapter mapping to PERD §34.4 payloads (ledger, payout `status`, `settlementStatus`, `arrivalStatus`, switch via status query and transition log); status query registered as an R0 read with its cooldown
Priority: P0
Requirement IDs: REQ-ENV-001, REQ-EXE-007, REQ-CAP-001; SoT IDs: POC-NFR-05, AGENT-24, INV-27, AGENT-06
Rationale: Noema's adapters must turn Tushe's objects into the PERD §34.4 payloads; DEC-2026-10-12 section 7 gives the mapping (ledger → double-entry ledger; transaction → payout `status`; settlement → `settlementStatus`; destination → `arrivalStatus`; switch → status query plus transition-log entries).
Modules touched (allowlist): services/core/adapters/synthetic_tushe/; packs/fintech/capabilities/ and packs/fintech/evidence_sources/ (status query descriptor)   ← nothing else may change
Contracts: `fin.ledger_entry`, `fin.switch_record`, `fin.destination_status` (PERD §34.4); bump required? N
Inputs/outputs: Tushe ledger, payout, settlement, arrival and status-query responses → PERD §34.4 normalised payloads; versioned mapping table
Acceptance criteria:
  REQ-ENV-001:
  - Replacing an adapter with a stub implementing the same interface SHALL require no changes to Understanding, Trust, Execution or Outcome.
  REQ-EXE-007:
  - The adapter contract tests SHALL cover every documented and every observed status.
  REQ-CAP-001:
  - `packcheck` SHALL reject each of 8 crafted invalid descriptors.
  Task "Done when" (plan v1.2): mapping table versioned; contract tests against live Tushe pass
Tests to write FIRST (AGENT-11): adapter contract tests per mapped object against live Tushe and recordings; status-query cooldown handling
Faults to exercise (AGENT-12): Tushe test account values (source TUSHE) for each payout outcome; status query returning `unreachable` and `cooling_down`
Dependencies: ENV-01; REQ-ENV-001, REQ-EXE-007, REQ-CAP-001
Out of scope: case, complaint and evidence adapters (ENV-08); registering the status query as an R0 read before Tushe confirms in writing that it cannot move money or change balances (request R6)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: IL.
