# Task card: OUT-01

Plan v1.10 task OUT-01 (week 1, Fri 23 Oct; late, on G1's critical path through BEN-05). Governed by PERD v1.19 and [DEC-2026-10-31-proof-depth-and-completeness](../../../decisions/DEC-2026-10-31-proof-depth-and-completeness.md) (D11, D14 to D16, D18, D24 bear on this card); PERD §29 and §30.3 REQ-RCV-002 are unchanged from v1.18. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Repository: `noema` (the card lives in `docs`). Drafted 31 Oct 2026 by the Core Engineer 2 role agent; the four open questions were answered by the Principal System Architect on 1 Nov 2026 ("Decisions" below). **Status: DRAFT until the Founder approves and merges this card. No OUT-01 code is written before then.**

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
  services/core/outcome/e2e/              (new test package; the control and truth helper lives only in its _test.go files; decision Q3)
  services/core/migrations/0004_outcome_verdict.sql     (decisions Q1 and Q2; 0002 is reserved for noema#94, 0003 for Core Engineer 1's record_read)
  services/core/migrations/testdata/      (the upgrade-order test fixture only; decision Q2)
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
  - boundary: outcome/ imports nothing under trust/, evidence/ or execution/ internals (the verifier-independence lint, INV-04); the architecture lint passes
  - write path (Q1): outcome_record_verdict(...) is the only way to store a verdict, a watch or a verdict-sourced recovery_request; outcome_rw has EXECUTE on it and no table-level INSERT, UPDATE or DELETE on outcome_verdict, outcome_watch or recovery_request; every other role, including execution_rw and trust_rw, is refused EXECUTE (one test per role)
  - migrations (Q2): a fresh database applies 0001, 0004 and passes every Outcome test; an upgrade where 0004 is applied first and 0002 afterwards (the noema#94 file, pinned by SHA-256 in testdata) succeeds, and the 0002 and Outcome tests both pass on the result
  - test-only control client (Q3): no non-test file under services/ references a mock-case /control/ or /truth/ path, the bench credential, or any package under benchmark/ or the hostility proxy (a static test)
Faults to exercise (AGENT-12): fp_case_create_timeout_after_commit_v1 (mock_case_commit_then_drop.json; also crash point 4 of the D14 matrix, "after the target commits with the response lost", whose final state Outcome's verdict decides); for the read path, mock-case FaultPlans HTTP_5XX, HTTP_429, DROP_RESPONSE, PAGINATE and INJECTION_PAYLOAD on find_cases; once the hostility proxy carries them, the D15 corrupted-payload families (truncated body, invalid JSON, wrong Content-Type, empty body with a success status, extra or missing required field), each of which must give UNKNOWN, never ACHIEVED (REQ-ENV-005 as amended). Never mocks.
Dependencies: EXE-02 (Done per the docs#77 assessment); REQ-VER-002 (internal/predicate, merged); REQ-RCV-001 (Trust consumes the RecoveryRequest; not built, out of scope)
Out of scope:
  - verifying a compensation (REQ-RCV-005, D11): the verifier treats a compensation's receipt like any other receipt, and nothing in OUT-01 assumes a capability is forward-only; compensation-specific outcome definitions and the §30.2 compensation rows are later tasks
  - receipt-signature verification in Outcome (SoT §13.1) and Ed25519 signing of Outcome's Record events (REQ-AUD-006, REC-08): both follow the W1 design, task GOV-28 (due to the founders Wed 4 Nov); see "Receipt signature slot" below. The verdict signature itself is in scope (Q4)
  - the Temporal outcome-watch workflow, its schedule and the fallback sweeper (OUT-03, C1)
  - the full predicate language and every pack outcome other than fin.outcome.exception.case_opened (OUT-02)
  - status_explained verification against ledger, switch and settlement (no adapter for them is built; hosted Tushe is paused)
  - Trust's evaluation of the RecoveryRequest (REQ-RCV-001), the inbound event inbox (OUT-04), callbacks (REQ-VER-005)
  - any change to execution/, trust/, contracts/, adapters/, a threshold, TTL, retry budget or settle window
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
  Added by DEC-2026-10-31: the code passes golangci-lint with errcheck, contextcheck and no panic outside main and tests (D24, REQ-TST-010; written to pass before PLT-09 lands); the per-merge chaos subset passes once TST-02 carries it (D16, REQ-TST-009), because this PR touches Outcome
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2 (a founder) with the Core Engineer 2 role agent. Needs: EXE-02. Gate: G1 (through BEN-05). G0 has not passed, so no result of this task counts as Phase B evidence until it does (plan §3, DEC-2026-10-16 E4).

## Decisions (Principal System Architect, 1 Nov 2026)

Given in the session of 1 Nov 2026 and recorded here; they count once the Founder approves and merges this card (AGENTS.md §2 item 3). The options considered are in the history of docs#74.

| # | Question | Decision | What the card requires because of it |
|---|---|---|---|
| Q1 | Write privileges for `outcome_rw` | **One SECURITY DEFINER database function, `outcome_record_verdict(...)`, is the only write path.** EXECUTE is granted only to `outcome_rw`. It inserts the verdict, its `recovery_request` (with `verdict_id`; `grant_id` nullable, a CHECK that exactly one of them is set; REQ-VER-003, DEC-2026-10-18) and, for PENDING_EXTERNAL, its `outcome_watch`, in one transaction, and appends their Record events through `record_insert`. `outcome_rw` gets no table-level INSERT, UPDATE or DELETE on these tables | **Known gap, stated plainly:** until signed Record events land (REC-08, REQ-AUD-006, DEC-2026-10-31 D18), anyone holding the `outcome_rw` credential can call the function and write a verdict that Outcome did not reach. The function bounds what can be written (a well-formed verdict, its recovery request and its events, in order), not who wrote it. REC-08 closes this: the database will refuse an event whose signature does not verify against Outcome's trusted public key. The PR repeats this paragraph and links the debt register entry the Repo Steward files for it |
| Q2 | Migration number | **`0004`.** `0002` is reserved for noema#94 and `0003` for Core Engineer 1's `record_read`. OUT-01 does not wait for #94 to merge | `platform/db.Migrate` applies every file not yet applied, in name order, so a gap is allowed. The PR tests a fresh database, and an upgrade where `0002` is applied after `0004`. #94's `0002` replaces only `decision_grant_guard()` and touches nothing in `0004` (checked against #94's head `b576b32`) |
| Q3 | Applying the US-06 FaultPlan from a core test | **Approved: a test-only helper.** No non-test file imports benchmark or hostility-proxy code, and the architecture lint passes | The helper lives only in `_test.go` files of `services/core/outcome/e2e/`. The amendment to DEC-2026-10-26 is in this same PR, as Amendment 1 of that record |
| Q4 | The key that signs a verdict | **Outcome signs verdicts with its own Ed25519 key under GOV-28 (W1), separate from Execution's key.** The Engineering Lead is adding verdict signing to W1 | The verifier signs through a signer port. If W1 is approved by Wed 4 Nov, the port's implementation is the W1 Ed25519 signer. **Only if W1 slips past Wed 4 Nov:** an interim HMAC key held only by Outcome (PLT-05), a debt entry, and a report to the Principal System Architect that day |

## Design notes (for review; not decisions)

- **What the receipt is used for.** Only as a pointer: which idempotency key, tenant and grant, `dispatched_at`, and the plan step's outcome definition. It is never proof (INV-04). A verdict is the same whether the receipt says `ACKNOWLEDGED` or `OUTCOME_UNKNOWN`.
- **Verify by key, then the predicate.** Step 1 reads `FindCases{IdempotencyKey}` with Outcome's read-only adapter identity. Step 2 reads `FindCases{TransactionRef}` to a complete page, because the `case_opened` predicate counts cases for (subject, `created_by_intent`) and a key-scoped read cannot see a second case under another key. Only a complete page can support a negative or a count (INV-19); an incomplete page is UNKNOWN.
- **Receipt signature slot.** The verifier takes a `ReceiptAuthenticity` port that runs before any read. OUT-01 ships no implementation that holds a key: receipts are HMAC-signed today, and Outcome holding Execution's HMAC key could forge receipts (DEBT-01). When the GOV-28 (W1) Ed25519 design is approved, an implementation with Execution's public key plugs into that port. A failed check gives `SECURITY_EVENT SIGNATURE_INVALID` and UNKNOWN, with no rework of the verifier. Until then the gap is visible in every reconstruction: the verdict's Record event says the receipt signature was not checked, if the Record event contract allows such a field; if it does not, that is raised in the PR rather than added (AGENT-15).
- **Record-event signing slot (D18, REQ-AUD-006, REC-08).** Outcome appends its Record events (`VERIFICATION_READ`, `VERDICT`, `RECOVERY_REQUESTED`, `WATCH_CREATED`) only through `outcome_record_verdict(...)`, and the Go side builds them through one function that takes the signer port of Q4. When REC-08 adds per-event signatures, the trusted-key table and the database check, only that port's implementation and the function's signature check change.
- **PENDING_EXTERNAL.** `case_opened` has no pending condition, so US-06 never produces it. OUT-01 writes the `outcome_watch` row with `deadline_at` and `next_check_at` in the verdict's transaction, enforced by the database; the workflow that drives it is OUT-03 (C1). The test for the watch row uses a predicate fixture, because no adapter yet produces a pending state.
