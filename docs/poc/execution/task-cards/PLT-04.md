# Task card: PLT-04

Plan v1.4 task PLT-04. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-13](../../../decisions/DEC-2026-10-13-code-monorepo.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P0-004  PLT-04 · Docker Compose with the six networks of PERD §65.1 and the profiles `dev`, `ci`, `bench` and `demo`; `make up`, `make reset`, `make bench-smoke` targets
Priority: P0
Requirement IDs: REQ-OPS-001, REQ-NFR-004; SoT IDs: INV-29, INV-22; SoT §35.3
Rationale: INV-29, INV-22 [REQ-OPS-001]. SoT §35.3; one-click reproducibility [REQ-NFR-004]. Each service's image is built from that service's folder only (PERD v1.4 §65.1; DEC-2026-10-13 R2).
Modules touched (allowlist; paths the agent may create or change in `noema`): deploy/compose/; Makefile (the `up`, `reset` and `bench-smoke` targets only)   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: PERD v1.4 §65.1 topology in → a Compose project and Make targets out
Acceptance criteria:
  REQ-OPS-001:
  - The connection-test matrix SHALL pass in CI and before every release run.
  REQ-NFR-004:
  - A fresh-clone CI job SHALL reach a green smoke run.
  Task "Done when" (plan v1.4): `make up` starts Postgres, Temporal, empty services and the UI shell
Tests to write FIRST (AGENT-11): the connection-test matrix of REQ-OPS-001 (every forbidden route fails from inside each container); `make up` reaches a healthy state with Postgres, Temporal, the empty services and the UI shell. The fresh-clone smoke run of REQ-NFR-004 needs the benchmark runner and cases, which later tasks deliver (BEN-18, REL-02), so `make bench-smoke` here is a target that exists and runs the empty suite
Faults to exercise (AGENT-12): none (a Compose task; no enterprise fault applies)
Dependencies: PLT-01; REQ-OPS-001, REQ-NFR-004 (REQ-SEC-002 for REQ-OPS-001)
Out of scope: any product logic; any provider call; any Tushe call; the Dockerfiles and manifests (PLT-01); the CI workflows (PLT-02); the hostility proxy, `mock-case` and the webhook receiver service definitions (ENV-08, ENV-09, ENV-13)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent. Needs: PLT-01.
