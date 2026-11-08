# Task card: REC-09

Plan v1.13 task REC-09 (added by ruling A109 of [DEC-2026-11-08-rec-09-record-export](../../../decisions/DEC-2026-11-08-rec-09-record-export.md); dated Wed 18 Nov by the Repo Steward, because the Founders approved the task and gave no date). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Owner C1, reviewer EL. Written by the Repo Steward on 8 Nov 2026 from the change request and the Founders' conditions; the owner reviews it before work starts.

```
REC-09 · Noema record export: a library function that turns one correlation's Record into the neutral audit_record
Priority: P1 (the Founders approved it as a condition of the Noema arm being scored; REQ-AUD-003 is P0, the export adds no P0 path)
Requirement IDs: REQ-AUD-003, REQ-BEN-001, REQ-BEN-009 (REV rule 6); SoT IDs: INV-22 (nothing from the oracle or held-out set), INV-12 (identity from the session only)
Rationale: the comparison arms are scored on a neutral audit_record; the Noema arm's must come from its own Record, read-only and tenant-bound.
Form (Founders' condition 1): a LIBRARY FUNCTION called by the Noema arm runner. It is NOT an HTTP route. If a route is ever wanted it first gets a row in the control-plane matrix (docs#134).
Modules touched (allowlist): services/core/record/export/** (new package), status/REC-09.md
  ← nothing else may change. No migration, no contract change, no new dependency, no new role.
Contracts: none changed; it writes the audit_record shape of `benchmark-arm-result.v1` (noema#249, still a Draft). Bump required? N
Inputs/outputs: a correlation id and the session's tenant in → the neutral audit_record out: per step seq, time, step name, actor, evidence ids, inputs digest, outputs digest, decision, outcome; plus a digest of the whole. A span whose chain does not verify is refused, not exported (as in REC-03).
Reads: only through the existing tenant-bound `record_read` path; the tenant comes from the session (INV-12), never from an argument.
Acceptance criteria (the plan row's Done when):
  - for a sample of cases a reviewer reconstructs the decisions from the export alone;
  - the export digest is stable across two runs on the same Record;
  - a chain that does not verify is refused;
  - a call for another tenant is refused.
Tests to write FIRST (AGENT-11): the four above, each seen failing; plus a test that nothing from the oracle or the held-out set can appear in an export (INV-22).
Faults to exercise (AGENT-12): a Record with a broken chain; a Record with a gap; a cross-tenant call.
Record events to assert: none written (read-only); the read itself goes through `record_read`.
Dependencies: REC-03 (Needs); the audit_record shape in noema#249 (not a task; must be merged or its shape agreed before the PR leaves Draft).
Review (Founders' condition 3): the Security Reviewer gives reviewer-role READY on what the export exposes (nothing from the oracle or held-out set; neutral fields only) BEFORE the C1 PR leaves Draft. EL reviews. P0-path rules for a Record package apply: two human reviews.
Out of scope: any HTTP route; any migration, contract change, dependency or role; export of anything other than the neutral fields.
Definition of done: tests green; boundary/lint green; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C1. Reviewer: EL (and the Security Reviewer, condition 3). Needs: REC-03. Dated Wed 18 Nov (plan v1.13).
