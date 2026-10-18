# Task card: PLT-02

Plan v1.5 task PLT-02 (re-baselined by DEC-2026-10-16 E3 to Mon 19 Oct). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-13](../../../decisions/DEC-2026-10-13-code-monorepo.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P0-002  PLT-02 · CI pipeline: build, unit tests, secret scan, dependency pinning check, SBOM, codegen diff, image file-list check (DEC R2), environment-reference check (DEC R3), PR trace-ID check (PERD REQ IDs plus SoT IDs)
Priority: P0
Requirement IDs: REQ-TST-005, REQ-SEC-007, REQ-AGT-001; SoT IDs: AGENT-14, AGENT-01. It also implements the CI checks in the acceptance criteria of REQ-SEC-002 (image file list) and REQ-SEC-005 (environment references), copied under PLT-01
Rationale: SoT §38 [REQ-TST-005]. SoT §47.2 (ASI04), SoT §50.4 [REQ-SEC-007]. AGENT-01; traceability (§59) [REQ-AGT-001]. One repository widens what a workflow can reach, so secrets are scoped to GitHub Environments per service and each image is checked for the other service's files (DEC-2026-10-13 R2, R3).
Modules touched (allowlist; paths the agent may create or change in `noema`): .github/workflows/; tools/ci/   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: the diff of a pull request, each service's built image, and each workflow file in → pass or fail checks out
Acceptance criteria:
  REQ-TST-005:
  - Branch protection SHALL require the merge checks.
  REQ-SEC-007:
  - CI SHALL fail on an unpinned dependency, a detected secret, or an unsigned pack.
  REQ-AGT-001:
  - A PR without IDs SHALL fail the `trace-ids` check.
  Task "Done when" (plan v1.5): a PR without IDs fails; a planted test secret fails; a planted cross-service file in an image fails CI; a workflow referencing another area's environment fails CI. Re-baselined by DEC-2026-10-16 E3
Tests to write FIRST (AGENT-11), each a planted-violation test (a "canary") that must fail CI before the check exists and pass once it does:
  - a pull request without REQ and SoT IDs (the `trace-ids` check);
  - a planted test secret;
  - a cross-service file placed in a service's image (the image file-list check, DEC R2);
  - a workflow that references another area's environment, for example a core workflow naming `model-ci` (the environment-reference check, DEC R3);
  - a secret defined at repository level (DEC R3).
Faults to exercise (AGENT-12): none (a CI task; no enterprise fault applies)
Dependencies: PLT-01; REQ-TST-005, REQ-SEC-007, REQ-AGT-001
Out of scope: any product logic; any provider call; any Tushe call; the lint rules (PLT-03); Compose (PLT-04); creating environments or secrets, or changing branch protection (the engineering lead applies those by hand, see PLT-01-settings-checklist.md)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent. Needs: PLT-01.
