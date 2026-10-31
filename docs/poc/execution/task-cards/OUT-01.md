# Task card: OUT-01

Plan v1.9 task OUT-01 (week 1, Fri 23 Oct; late, on G1's critical path through BEN-05). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Repository: `noema` (the card lives in `docs`). Drafted 31 Oct 2026 by the Core Engineer 2 role agent for the owner to approve, amend or reject. **Status: DRAFT. Not approved. No code starts until a founder approves this card and answers the four questions in "Decisions needed before code".**

```
TASK-P7-001  OUT-01 · Outcome Verifier, verify-by-key scope: settle window; Outcome's own reads; verify by idempotency key; the predicate subset the slice needs; verdicts; RecoveryRequest in the same transaction
Priority: P0
Requirement IDs: REQ-VER-001, REQ-VER-002 (subset), REQ-VER-003, REQ-RCV-002; SoT IDs: INV-04, INV-07, INV-15, INV-19, INV-28, AGENT-12, AGENT-16, AGENT-21, POC-FR-09, POC-FR-10, PLAT-FR-10, US-06, US-16
Rationale: INV-04; AGENT-21; POC-FR-09. For OUTCOME_UNKNOWN, Outcome first queries the target by idempotency key; a retry decision is possible only after verification shows the effect is absent (POC-FR-10; US-06). [REQ-VER-001, REQ-RCV-002]
Modules touched (allowlist; paths in `noema`):
  services/core/outcome/verifier/
  services/core/outcome/predicate/
  services/core/outcome/watch/            (the Postgres row only; no Temporal code, which is OUT-03)
  services/core/outcome/README.md, services/core/outcome/doc.go
  services/core/outcome/e2e/              (new test package; see decision Q3)
  services/core/migrations/<next>_outcome_verdict.sql   (see decisions Q1 and Q2)
  services/core/migrations/README.md
  status/roles/core-engineer-2.md
  ← nothing else may change. contracts/ is read-only (no bump). execution/, trust/, evidence/, adapters/ are read-only.
Contracts: outcome-verdict.v1.json, outcome-definition.v1.json, execution-receipt.v1.json, enums.v1.json (Verdict), fault-plan.v1.json (fixture only); bump required? N
Inputs/outputs: an execution_receipt row (any state) plus the plan step's outcome definition from the loaded pack → one outcome verdict (outcome-verdict.v1) with its VERIFICATION_READ and VERDICT Record events; for every verdict other than ACHIEVED, one recovery_request with verdict_id, in the same transaction; for PENDING_EXTERNAL, one outcome_watch row with a deadline
Acceptance criteria:
  REQ-VER-001:
  - False-success verdicts SHALL be 0.
  - Verification accuracy against the oracle SHALL be 100% on the release suite.
  - Verdicts with `verified_at` − `dispatched_at` < settle window SHALL be 0.
  REQ-VER-002 (subset):
  - A predicate referencing an unknown field SHALL fail `packcheck`. Three-valued logic SHALL be property-tested (UNKNOWN propagates).
  REQ-VER-003:
  - Non-ACHIEVED verdicts without a RecoveryRequest SHALL be 0 (DB constraint).
  REQ-RCV-002:
  - In US-06, dispatches SHALL equal 1. Across the B4 suite, blind retries SHALL be 0.
  Task "Done when" (plan v1.9): US-06: verdict ACHIEVED with exactly 1 dispatch
  Founder-approved criteria (role prompt, Core Engineer 2, 30 Oct 2026), restated as tests:
  1. The verifier waits the settle window of the outcome definition on the injected clock, then reads the target itself. A receipt, an HTTP status, a workflow completion or Trust's evidence snapshot is never proof.
  2. US-06 (the target commits, the response is lost): Outcome finds the committed case by idempotency key and returns ACHIEVED, with exactly one dispatch and one logical case, and no second create.
  3. A timeout or a missing response stays OUTCOME_UNKNOWN until Outcome decides (INV-07).
  4. Invalid, missing, inconsistent or unverifiable evidence fails closed; Outcome never manufactures success.
  5. UNKNOWN and PENDING_EXTERNAL are handled correctly; PENDING_EXTERNAL has a durable watch and a deadline (INV-28).
  6. Every verdict is auditable from the Record.
  7. US-06 uses the existing fixture contracts/fixtures/valid/fault-plan/mock_case_commit_then_drop.json; the failure is never mocked (AGENT-12).
Tests to write FIRST (AGENT-11):
  - US-06 against the real mock-case binary and real PostgreSQL, fault from mock_case_commit_then_drop.json: verdict ACHIEVED; grant_spend count 1; mock-case truth shows one case and one create command for the key
  - US-16 (verified NOT_ACHIEVED): a complete, empty page for the key gives NOT_ACHIEVED plus one recovery_request with verdict_id
  - EC-E03 (200 PENDING, nothing created) and EC-E04: never ACHIEVED
  - settle window: no read and no verdict before dispatched_at + settle_window_seconds (property test on the injected clock)
  - read budget: 3 attempts at 1, 3 and 9 s of simulated time, then UNKNOWN plus one recovery_request (AGENT-16; the values are not changed)
  - fail closed: an incomplete page, a MALFORMED read, two cases for one key, a case whose tenant or key differs from the receipt, and a predicate that evaluates to UNKNOWN each give UNKNOWN, never ACHIEVED (INV-19: absence of evidence is not a negative fact)
  - DB constraint: inserting a non-ACHIEVED verdict without a recovery_request in the same transaction fails; a PENDING_EXTERNAL verdict without an outcome_watch fails
  - Record: VERIFICATION_READ per read attempt, VERDICT, RECOVERY_REQUESTED, WATCH_CREATED appended in the verdict's transaction; chain verifies; a failed append writes no verdict (EC-E16)
  - boundary: outcome/ imports nothing under trust/, evidence/ or execution/ internals (the verifier-independence lint, INV-04)
Faults to exercise (AGENT-12): fp_case_create_timeout_after_commit_v1 (mock_case_commit_then_drop.json); for the read path, mock-case FaultPlans HTTP_5XX, HTTP_429, DROP_RESPONSE, PAGINATE and INJECTION_PAYLOAD on find_cases. Never mocks.
Dependencies: EXE-02 (Done per docs#73 assessment); REQ-VER-002 (internal/predicate, merged); REQ-RCV-001 (Trust consumes the RecoveryRequest; not built, out of scope)
Out of scope:
  - receipt-signature verification in Outcome (SoT §13.1): added after the W1 Ed25519 key design is approved; see "Receipt signature slot" below
  - the Temporal outcome-watch workflow, its schedule and the fallback sweeper (OUT-03, C1)
  - the full predicate language and every pack outcome other than fin.outcome.exception.case_opened (OUT-02)
  - status_explained verification against ledger, switch and settlement (no adapter for them is built; hosted Tushe is paused)
  - Trust's evaluation of the RecoveryRequest (REQ-RCV-001), the inbound event inbox (OUT-04), callbacks (REQ-VER-005)
  - any change to execution/, trust/, contracts/, adapters/, a threshold, TTL, retry budget or settle window
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2 (a founder) with the Core Engineer 2 role agent. Needs: EXE-02. Gate: G1 (through BEN-05). G0 has not passed, so no result of this task counts as Phase B evidence until it does (plan §3, DEC-2026-10-16 E4).

## Decisions needed before code

Each of these touches a security boundary, a shared migration or a committed decision, so the role agent does not decide them (common charter §6).

| # | Question | Why it blocks | Options | Recommended |
|---|---|---|---|---|
| Q1 | **Privileges for `outcome_rw`.** Migration 0001 gives `outcome_rw` SELECT on the execution tables and INSERT on `outbox_event` only. OUT-01 needs: INSERT on new `outcome_verdict` and `outcome_watch` tables; INSERT on `recovery_request` with `verdict_id`; `recovery_request.grant_id` made nullable with a CHECK that exactly one of `grant_id` and `verdict_id` is set (REQ-VER-003, DEC-2026-10-18); a deferred constraint trigger so that a non-ACHIEVED verdict without its recovery_request cannot commit | Role privileges are a security boundary (charter §6.3). The `recovery_request` change alters a table that `execution_rw` writes today and that DEBT-01's closure work may also touch | (a) as listed, `outcome_rw` gets INSERT only, never UPDATE or DELETE, on its own tables; (b) a SECURITY DEFINER function `outcome_record_verdict(...)` is the only write path, as `record_insert` is for the Record; (c) do nothing: no verdict can be stored | **(b)**: one audited write path, no table-level INSERT for the role, the same pattern as `record_insert` |
| Q2 | **Migration number and order with the held DEBT-01 work.** `0002_grant_spent_void.sql` is on the held noema#94 and noema#90. An Outcome migration needs a number | Forward-only migrations are never renumbered after merge. Taking 0002 collides; taking 0003 before 0002 merges leaves a gap that the migrator may refuse | (a) OUT-01 takes 0003 and waits to merge until #94 merges or is closed; (b) OUT-01 takes 0002 and #94 renumbers to 0003 (C1's branch, held); (c) the Founders reserve numbers per task | **(a)**: no change to held work; C1 is told |
| Q3 | **Applying the US-06 FaultPlan from a test in the core tree.** Criterion 7 requires `mock_case_commit_then_drop.json`. The only way to apply it is `PUT /control/v1/fault-plan` on mock-case's bench listener with the bench credential. DEC-2026-10-26 D2 puts that client in `benchmark/runner/`, "never in the core"; `execution/e2e` has followed that rule and does not cover the dropped-response case for this reason | This is a committed founder decision. A test-only helper in `services/core/outcome/e2e/` would be a control-plane client in the core tree | (a) a test-only helper in a `_test.go` file of `services/core/outcome/e2e/`, never compiled into the binary, with a static test that no non-test file references `/control/` or `/truth/` (the decision record is amended to say so); (b) the US-06 run lives in `benchmark/runner/` and drives the core through the public API (blocked: the intake path and API-01 are not built); (c) the core test replays the adapter recording of `TIMEOUT_AFTER_COMMIT` (not live; does not prove one logical case from the truth endpoint) | **(a)**, recorded as an amendment to DEC-2026-10-26 before the code merges. (c) is not acceptable evidence for criterion 2 |
| Q4 | **The key that signs a verdict.** `outcome-verdict.v1.json` requires `sig` (HMAC-SHA-256 in the POC). No record names Outcome's signing key | Keys are a security boundary. Reusing the grant key or Execution's receipt key lets Outcome forge another power's artefact (BD-05) | (a) a new HMAC key `outcome-verdict-<n>` held only by Outcome, file-mounted like the others (PLT-05); (b) defer: store the verdict unsigned (violates the contract; not acceptable); (c) wait for the W1 Ed25519 design and sign verdicts with an Outcome Ed25519 key | **(a)** now, moved to Ed25519 with the W1 design |

## Design notes (for review; not decisions)

- **What the receipt is used for.** Only as a pointer: which idempotency key, tenant and grant, `dispatched_at`, and the plan step's outcome definition. It is never proof (INV-04). A verdict is the same whether the receipt says `ACKNOWLEDGED` or `OUTCOME_UNKNOWN`.
- **Verify by key, then the predicate.** Step 1 reads `FindCases{IdempotencyKey}` with Outcome's read-only adapter identity. Step 2 reads `FindCases{TransactionRef}` to a complete page, because the `case_opened` predicate counts cases for (subject, `created_by_intent`) and a key-scoped read cannot see a second case under another key. Only a complete page can support a negative or a count (INV-19); an incomplete page is UNKNOWN.
- **Receipt signature slot.** The verifier takes a `ReceiptAuthenticity` port that runs before any read. OUT-01 ships no implementation that holds a key: receipts are HMAC-signed today, and Outcome holding Execution's HMAC key could forge receipts (DEBT-01). When the W1 Ed25519 design is approved, an implementation with Execution's public key plugs into that port. A failed check gives `SECURITY_EVENT SIGNATURE_INVALID` and UNKNOWN, with no rework of the verifier. Until then the verdict records `receipt_signature: NOT_CHECKED` in its Record event, so the gap is visible in every reconstruction.
- **PENDING_EXTERNAL.** `case_opened` has no pending condition, so US-06 never produces it. OUT-01 writes the `outcome_watch` row with `deadline_at` and `next_check_at` in the verdict's transaction, enforced by the database; the workflow that drives it is OUT-03 (C1). The test for the watch row uses a predicate fixture, because no adapter yet produces a pending state.
