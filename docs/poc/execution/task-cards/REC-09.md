# Task card: REC-09

Plan v1.13 task REC-09 (added by ruling A109 of [DEC-2026-11-08-rec-09-record-export](../../../decisions/DEC-2026-11-08-rec-09-record-export.md); dated Wed 18 Nov by the Repo Steward, because the Founders approved the task and gave no date). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Owner C1, reviewer EL. Written by the Repo Steward on 8 Nov 2026 from the change request and the Founders' conditions; the owner reviews it before work starts.

```
REC-09 · Noema record export: a library function that turns one correlation's Record into the neutral audit_record
Priority: P1 (the Founders approved it as a condition of the Noema arm being scored; REQ-AUD-003 is P0, the export adds no P0 path)
Requirement IDs: REQ-AUD-003, REQ-BEN-001, REQ-BEN-009 (REV rule 6); SoT IDs: INV-22 (nothing from the oracle or held-out set), INV-12 (identity from the session only)
Rationale: the comparison arms are scored on a neutral audit_record; the Noema arm's must come from its own Record, read-only and tenant-bound.
Form (Founders' condition 1): a LIBRARY FUNCTION called by the Noema arm runner. It is NOT an HTTP route. If a route is ever wanted it first gets a row in the control-plane matrix (docs#134).
Modules touched (allowlist): services/core/record/export/** (new package, including its `cmd/` CLI), status/REC-09.md
  ← nothing else may change. No migration, no contract change, no new dependency, no new role.
Contracts: none changed; it writes the audit_record shape of `benchmark-arm-result.v1` (noema#249, still a Draft). Bump required? N
Inputs/outputs: signature `Export(ctx, db, correlationID)`, with NO tenant argument. Out: the neutral audit_record: per step seq, time, step name, actor, evidence ids, inputs digest, outputs digest, decision, outcome; plus a digest of the whole. A span whose chain does not verify is refused, not exported (as in REC-03). The span is cut at a verified chain head, so an export taken while the head moves is still a consistent span.
Neutral mapping (Security Reviewer finding 1, INV-22): the export uses a CLOSED table from Record event type to the neutral step names of the arm view (noema#260, noema#248). A Record event type not in the table is refused, never exported as is. Never exported: `correlation_id`, `object_ref`, `written_by`, `prev_hash`, `hash`, `signature`, rule or policy ids, pack capability ids, or any fixture-derived id. `actor` is a role class only (`system`, `model`, `principal`, `operator`), never an emitter login, a `sub` or a tenant id. `evidence_ids` must resolve to tool calls in the same result.
Whole-export digest (finding 4): SHA-256 over the JCS (RFC 8785) of `entries`, preceded by the domain label `noema/audit-export/v1` and a 0x00 byte (the pattern of ruling A53), computed over the neutral fields only, so it cannot be confused with any Record or grant hash and does not depend on the chain hash scheme.
Reads: only through the existing tenant-bound read functions (A20), as `chain.ReadChain` does; the tenant is the database login's (`session_user`), never an argument (INV-12, DEBT-04). The Noema arm runner uses an existing per-tenant audit read login, NEVER `record_verify`, which reads every tenant's chain. `Export` refuses a nil or superuser connection.
Call path (finding 3): the arm runner is Python and `Export` is Go, so the card fixes the path. Default: a small CLI under `services/core/record/export/cmd/**` (inside the allowlist glob) run inside the arm container, opening the Record read-only with the per-tenant login, with no listening socket and no HTTP. Anything else (a listener, a binary elsewhere) is a new surface: C1 adds its path to the allowlist and tells the Security Reviewer before the PR leaves Draft; an HTTP route also breaks condition 1.
Acceptance criteria (the plan row's Done when):
  - for a sample of cases a reviewer reconstructs the decisions from the export alone;
  - the export digest is stable across two runs on the same Record;
  - a chain that does not verify is refused;
  - a call for another tenant is refused with the same not-found shape as a correlation id that exists nowhere (no existence oracle, REQ-API-002).
Tests to write FIRST (AGENT-11): the four above, each seen failing; plus an INV-22 canary test: seed the Record with oracle-shaped canary strings (a real case id, an `expected` marker, a held-out path) and assert none appears in the export bytes; a test that a login for tenant A asking for tenant B's correlation id gets the not-found shape; a test that `Export` refuses a nil or superuser connection; a test that every `evidence_ids` entry resolves to a tool call in the same result.
Faults to exercise (AGENT-12): a Record with a broken chain; a Record with a gap; a cross-tenant call; a span whose events include a type outside the closed table (refused); an export taken while the chain head moves (cut at a verified head).
Record events to assert: none written (read-only); the read itself goes through `record_read`.
Dependencies: REC-03 (Needs); the audit_record shape in noema#249 (not a task; must be merged or its shape agreed before the PR leaves Draft).
Review (Founders' condition 3): the Security Reviewer gives reviewer-role READY on what the export exposes (nothing from the oracle or held-out set; neutral fields only) BEFORE the C1 PR leaves Draft. EL reviews. P0-path rules for a Record package apply: two human reviews.
Out of scope: any HTTP route; any migration, contract change, dependency or role; export of anything other than the neutral fields.
Definition of done: tests green; boundary/lint green; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C1. Reviewer: EL (and the Security Reviewer, condition 3). Needs: REC-03. Dated Wed 18 Nov (plan v1.13).
