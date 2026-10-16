# Task card: GOV-20

Plan v1.3 task GOV-20. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md), Amendment 1. Open decision: [OD-P-43](../../../open-decisions.md#od-p-43) (PERD v1.3 OQ-15).

```
TASK-P0-020  GOV-20 · Decide where the public webhook receiver runs and how it is secured (PERD OQ-15); record the decision
Priority: P0
Requirement IDs: REQ-OPS-001, REQ-SEC-002; SoT IDs: INV-29, INV-22
Rationale: Tushe delivers webhooks only to public HTTPS endpoints; AT-06 needs the receiver on Fri 16 Oct. DEC-2026-10-12, Amendment 1 (D5).
Modules touched (allowlist): docs/decisions/ (the decision record); docs/open-decisions.md (closing OD-P-43, regenerated register) (Noemai-org/docs)   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: PERD v1.3 §67.2 OQ-15 and its minimum safe default → a committed decision record; OD-P-43 closed
Acceptance criteria:
  REQ-OPS-001:
  - The connection-test matrix SHALL pass in CI and before every release run.
  REQ-SEC-002:
  - Connection tests run from inside each container SHALL show that every forbidden route fails.
  Task "Done when" (plan v1.3): decision recorded; OD-P entry closed
Tests to write FIRST (AGENT-11): none (decision task); the decision names the connection tests ENV-13 must add for the public host
Faults to exercise (AGENT-12): none
Dependencies: PLT-04; REQ-OPS-001, REQ-SEC-002
Out of scope: building the receiver (ENV-13); exposing any Noema component other than the receiver and the proxy in front of it
Minimum safe default if not decided by Wed 14 Oct: one small public HTTPS host that runs only the receiver and the proxy in front of it; no other Noema component is exposed (PERD v1.3 OQ-15)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL. Needed by Wed 14 Oct (plan v1.3 §17).
