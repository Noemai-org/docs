# Task card: PLT-03

Plan v1.5 task PLT-03 (re-baselined by DEC-2026-10-16 E3 to Mon 19 Oct). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-13](../../../decisions/DEC-2026-10-13-code-monorepo.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P0-003  PLT-03 · `tools/lint`: core forbidden terms; import boundaries (trust, execution and outcome; explanation never imported); no wall-clock outside the clock package; no float money; no mock libraries in integration or benchmark packages; no benchmark branches; no provider SDK in core manifests; no DB driver or Temporal client in the model service; no file in `services/core/` references a path in `services/model/`, or the reverse
Priority: P0
Requirement IDs: REQ-NFR-005, REQ-TST-004, REQ-TST-006, REQ-DATA-002, REQ-SEC-002; SoT IDs: POC-NFR-10, INV-14, POC-FR-15, AGENT-12, OD-08, INV-29; SoT §51 boundary rules
Rationale: POC-NFR-10, INV-14, POC-FR-15 [REQ-NFR-005]. AGENT-12 [REQ-TST-004]. Validity of the proof [REQ-TST-006]. Correctness; EC-A07 depends on exact arithmetic [REQ-DATA-002]. INV-29, SoT §51 boundary rules [REQ-SEC-002]. Splitting repositories never stopped anyone adding a model SDK to the core's dependency file; these lints do, in any layout (DEC-2026-10-13 §2, R2).
Modules touched (allowlist; paths the agent may create or change in `noema`): tools/lint/   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: the source tree and each service's dependency manifest in → pass or fail per rule out
Acceptance criteria:
  REQ-NFR-005:
  - CI SHALL be green on the lint and on four-pack contract tests.
  REQ-TST-004:
  - A lint SHALL flag mock libraries imported in integration and benchmark packages.
  REQ-TST-006:
  - A lint SHALL find no references to the benchmark environment outside configuration.
  REQ-DATA-002:
  - The lint SHALL find no `float` or `double` money fields in core or contracts.
  - Property tests on conversion SHALL pass.
  REQ-SEC-002:
  - Connection tests run from inside each container SHALL show that every forbidden route fails.
  - Each service's container image SHALL contain only files from that service's folder and its generated contracts; a CI check SHALL list each image's files and fail otherwise.
  Task "Done when" (plan v1.5): each rule has a canary file that fails CI. Re-baselined by DEC-2026-10-16 E3
Tests to write FIRST (AGENT-11), each a planted-violation test (a "canary") that must fail before the rule exists and pass once it does:
  - a provider SDK added to `services/core/go.mod`;
  - a database driver for the core schemas, or a Temporal client, added to `services/model/pyproject.toml`;
  - a cross-service path: a file in `services/core/` referencing a path in `services/model/`, and the reverse;
  - one canary per remaining rule: a forbidden core term; an import between trust, execution and outcome internals; an import of explanation output; a wall-clock call outside the clock package; a `float` or `double` money field; a mock library in an integration or benchmark package; a reference to the benchmark environment outside configuration.
Faults to exercise (AGENT-12): none (a lint task; no enterprise fault applies)
Dependencies: PLT-01; REQ-NFR-005, REQ-TST-004, REQ-TST-006, REQ-DATA-002, REQ-SEC-002
Out of scope: any product logic; any provider call; any Tushe call; the CI workflows that run the lint (PLT-02); any dependency, linter or formatter not listed in PERD §36.1 without an [OPEN] entry and approval (AGENT-14)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent. Needs: PLT-01.
