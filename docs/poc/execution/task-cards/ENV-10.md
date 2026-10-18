# Task card: ENV-10

Plan v1.5 task ENV-10. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P2-010  ENV-10 · Event-feed poller on Tushe `GET /v1/events` by sequence cursor, persisting into the inbox table (OUT-04 adds deduplication and late-evidence handling in week 3)
Priority: P0
Requirement IDs: REQ-API-008, REQ-ENV-001; SoT IDs: POC-NFR-05, AGENT-24; SoT §35.5
Rationale: Tushe treats the feed as the source of truth and webhooks as pointers; Tushe will not deliver to private addresses; polling makes event faults deterministic on Noema's own read path. DEC-2026-10-12, D5.
Modules touched (allowlist; all paths in the `noema` repository, DEC-2026-10-13) [REC, pending engineering-lead approval]: services/core/adapters/synthetic_tushe/events/ (the poller); its tests; the inbox migration, only if PLT-06 has not created the inbox table   ← nothing else may change
Contracts: inbound event (PERD §39.6); bump required? N
Inputs/outputs: Tushe `GET /v1/events` pages by sequence cursor → inbox rows; persisted cursor
Acceptance criteria:
  REQ-API-008:
  - A replayed event SHALL create no second inbox row and change no state; a forged event SHALL be rejected.
  REQ-ENV-001:
  - Replacing an adapter with a stub implementing the same interface SHALL require no changes to Understanding, Trust, Execution or Outcome.
  Task "Done when" (plan v1.5): no event lost or doubled across a restart; feed faults from ENV-09 observed
Tests to write FIRST (AGENT-11): restart test (no event lost or doubled); EC-S16, EC-S17, EC-X17; feed faults from ENV-09 observed
Faults to exercise (AGENT-12): proxy feed faults (source PROXY): event lost, delayed, reordered, malformed or stale; Tushe replay with the same delivery ID (source TUSHE)
Dependencies: PLT-01, ENV-03, ENV-09, R1 batch 1 received (Tushe credentials, due Thu 15 Oct; dated no earlier than the first working day after receipt); REQ-API-008, REQ-ENV-001
Out of scope: deduplication and late-evidence handling (OUT-04, week 3); webhooks
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2, with a coding agent.
