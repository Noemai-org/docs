# Task card: PCK-02

Plan v1.7 task PCK-02 (in progress under DEC C3; dated Wed 21 Oct, after PCK-01). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-16 contract-and-pack-clarifications](../../../decisions/DEC-2026-10-16-contract-and-pack-clarifications.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P1-002  PCK-02 · `packcheck validate`: schema, references, predicate type-checking, freshness fields, risk class vs consequence profile, no prohibited node in the graph, template coverage. Three checks are still missing: validation against the CON-01 pack schema, predicate type-checking and template coverage
Priority: P0
Requirement IDs: REQ-CAP-001, REQ-AG-001; SoT IDs: INV-27, AGENT-06, INV-18; SoT §15.3, §15.4, §34.3, §43.7
Rationale: AGENT-06; SoT §43.8. [REQ-CAP-001] SoT §43.9; INV-18. [REQ-AG-001]
Modules touched (allowlist; paths the agent may create or change in `noema`): tools/packcheck.py; packs/fixtures/bad_packs/   ← nothing else may change
Contracts: the pack schema from CON-01 (`contracts/`), read-only here; bump required? N
Inputs/outputs: a pack file in → PASS, or FAIL with the stated reasons and exit code 2
Acceptance criteria:
  REQ-CAP-001:
  - `packcheck` SHALL reject each of 8 crafted invalid descriptors.
  REQ-AG-001:
  - A pack containing a node with a PROHIBITED capability SHALL fail `packcheck` and CI.
  Task "Done when" (plan v1.7): Eight crafted bad packs all fail, and each of the three missing checks has a negative fixture that fails for the stated reason. Status: in progress (DEC-2026-10-16 contract-and-pack-clarifications C3). Delivered 15 Oct 2026 (commit ce8897e, ported by noema#1): references, risk class against consequence profile, prohibited graph nodes, cycles and write requirements. packcheck also enforces the namespace rules of DEC-2026-10-16 money-and-value-lists §2.4: it rejects a pack reason code outside its namespace and a pack code that reuses a core code
Tests to write FIRST (AGENT-11): the three negative fixtures first, each seen failing (passing validation) on the current `packcheck`: (1) a pack that breaks the CON-01 pack schema (a missing required field; an unknown field) must fail schema validation; (2) a pack whose predicate does not type-check (a comparison of mismatched types, an unknown field, an unknown capability ID, a missing `evaluation_time`; PERD §23.4) must fail predicate type-checking; (3) a pack that lacks a fallback template for an outcome × classification combination in any of the five locales must fail template coverage (REQ-EXP-002: template coverage SHALL be 100%). The eight existing bad packs keep failing with exit 2
Faults to exercise (AGENT-12): none (a pack-tooling task; no enterprise fault applies)
Dependencies: PCK-01; CON-01 (the pack schema); REQ: REQ-AG-001, REQ-CAP-001
Out of scope: any change to a pack's content (PCK-01); any new check beyond the three; any change to an existing check's meaning; a new dependency (AGENT-14)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent. Needs: PCK-01. Dated Wed 21 Oct. Status: in progress (DEC C3).

## The three missing checks (DEC-2026-10-16 contract-and-pack-clarifications C3)

| Check | What it must do | Negative fixture (must fail) |
|---|---|---|
| Validation against the CON-01 pack schema | Validate every pack file against the pack schema in `contracts/`, with the same code path locally and in CI (SoT §15.4, pack checker) | A pack with a missing required field, and one with an unknown field |
| Predicate type-checking | Type-check every success predicate and policy predicate (§43.7 expression language; PERD §23.4) | A predicate that compares mismatched types, names an unknown field or capability ID, or lacks `evaluation_time` |
| Template coverage | Require a fallback template for every outcome × classification combination in all five locales (REQ-EXP-002) | A pack that lacks one template in one locale |
| Reason-code namespaces (DEC-2026-10-16 money-and-value-lists §2.4) | Reject a pack reason code outside its `<vertical>.reason.<name>` namespace, and a pack code that reuses a core code | A pack with a reason code outside its namespace, and one that reuses a core code such as `NOT_AUTHORIZED` |
