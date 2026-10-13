# Task card: PLT-01

Plan v1.4 task PLT-01. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-13](../../../decisions/DEC-2026-10-13-code-monorepo.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P0-001  PLT-01 · Create the `noema` skeleton per DEC-2026-10-13 R1 and PERD v1.4 §64.2. It includes: per-service manifests (`services/core/go.mod`, `services/model/pyproject.toml`, `ui/package.json`); one Dockerfile per service with its own build context; path-filtered workflows; CODEOWNERS per R4; copies of AGENTS.md and CLAUDE.md that state the `docs` commit they came from; module READMEs; a Makefile
Priority: P0
Requirement IDs: REQ-AGT-002, REQ-AGT-005, REQ-SEC-002, REQ-SEC-005; SoT IDs: AGENT-03, AGENT-19, AGENT-16, AGENT-28, INV-29; SoT §47.4, §51
Rationale: Prevents gold-plating and drift (AGENT-03, AGENT-19) [REQ-AGT-002]. INV-29, SoT §51 boundary rules [REQ-SEC-002]. SoT §47.4 [REQ-SEC-005]. All POC code lives in one repository, `noema`; the two services stay physically separate, secrets are scoped by environment and code ownership is by path (DEC-2026-10-13 R1 to R4).
Modules touched (allowlist; paths the agent may create in `noema`): AGENTS.md; CLAUDE.md; .github/CODEOWNERS; .github/workflows/ (the path-filtered skeleton only; PLT-02 fills the checks); Makefile; contracts/ (README only); services/core/ (go.mod, Dockerfile, empty module folders with READMEs per PERD v1.4 §64.2); services/model/ (pyproject.toml, Dockerfile, empty module folders with READMEs per PERD v1.4 §64.2); packs/ (READMEs only); tools/lint/, tools/packcheck/, tools/codegen/ (READMEs only); ui/ (package.json, README); benchmark/ (READMEs only; never the held-out set); synthetic/mock_case/ (README only); deploy/compose/ (README only; PLT-04 fills it); docs/ (README only)   ← nothing else may change
Contracts: none; bump required? N
Inputs/outputs: DEC-2026-10-13 R1 tree and PERD v1.4 §64.2 in → an empty `noema` repository skeleton out; copies of AGENTS.md and CLAUDE.md from the `docs` repository, each stating the `docs` commit it was copied from
Acceptance criteria:
  REQ-AGT-002:
  - None stated in PERD v1.4 (Acceptance criteria: —). Requirement, verbatim: "A task card (§61.4) lists the modules the agent may touch. CI compares the diff paths against the card and fails on changes outside the allowlist, unless a reviewer approves an amendment."
  REQ-AGT-005:
  - A CODEOWNERS rule SHALL apply to the configuration paths.
  REQ-SEC-002:
  - Connection tests run from inside each container SHALL show that every forbidden route fails.
  - Each service's container image SHALL contain only files from that service's folder and its generated contracts; a CI check SHALL list each image's files and fail otherwise.
  REQ-SEC-005:
  - A rotation test SHALL verify grants issued under the old and the new key during overlap, then reject the old key after retirement.
  - CI secrets SHALL exist only in per-service GitHub Environments (`core-ci`, `model-ci`, `bench`), never at repository level; a CI check SHALL fail any workflow that references another area's environment.
  (the rotation test is proved by the other tasks that deliver REQ-SEC-005 (PLT-05, TRU-05, SEC-09); the second criterion is proved here and checked in CI by PLT-02)
  Task "Done when" (plan v1.4): `make build` builds each service independently; each image's file list contains only its own service; CODEOWNERS active; GitHub Environments `core-ci`, `model-ci` and `bench` exist with no repository-level secret (set by EL)
Tests to write FIRST (AGENT-11): a build of `services/core/` alone and of `services/model/` alone, each from its own folder as the Docker build context (`make build` builds each service independently); a CODEOWNERS parse test covering the DEC R4 paths; a check that AGENTS.md and CLAUDE.md in `noema` state the `docs` commit they came from. The canary checks for secrets, environments and images are PLT-02; for manifests and cross-service paths, PLT-03
Faults to exercise (AGENT-12): none (a skeleton task; no enterprise fault applies)
Dependencies: GOV-02; REQ-AGT-002, REQ-AGT-005, REQ-SEC-002, REQ-SEC-005 (REQ-OPS-003 for REQ-AGT-005)
Out of scope: any product logic; any provider call; any Tushe call; the CI checks (PLT-02); the lint rules (PLT-03); Compose and the `make up` targets (PLT-04); creating the repository or changing any repository setting (see "Settings the engineering lead applies by hand" below)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

**Settings the engineering lead applies by hand.** The agent never changes repository settings. It prepares, and keeps current, the checklist in [`PLT-01-settings-checklist.md`](PLT-01-settings-checklist.md). In summary:

- GitHub Environments `core-ci`, `model-ci` and `bench`;
- required reviewers on `bench` (the benchmark owner);
- branch protection on `main` (required checks, required CODEOWNER review, no force-push);
- no repository-level secrets.

Owner: EL, with a coding agent. Needs: GOV-02 (DEC-2026-10-13 merged; `noema` exists).
