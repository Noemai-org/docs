# DEC-2026-10-28 · A SPENT grant becomes VOID only for a confirmed REJECTED_STALE_VERSION refusal

| | |
|---|---|
| **Status** | Accepted in principle by the Founders on 28 October 2026 (Option 1 of the conflict recorded in `noema` pull request 90, with the conditions in §1; decisions given in a working session, so they count once this record is merged). The Technical Co-Founder confirms by approving the pull request that adds it |
| **Date** | 28 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Resolves a conflict inside the PERD that was not in [`conflicts-register.md`](../poc/perd/conflicts-register.md) |
| **Amends** | The PERD: a new version, [v1.18](../poc/perd/NOEMA_POC_PERD_v1.18.md) (§38.2, REQ-EXE-001, REQ-EXE-004). `services/core/migrations/` in `Noemai-org/noema`: one new forward-only migration. No SoT text changes |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted in principle by the Founders (see the table above)
- Date: 28 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-EXE-001, REQ-EXE-004, REQ-AUD-001; INV-03, INV-17, INV-27; US-19; EC-E11; SoT §43.3; PERD §27.1, §28.1, §38.2. No SoT change; the requirement count stays 154
- Migration notes: §4
- Amended: §6 (28 October 2026), after the merge
- Supersedes: none

---

## 1. The decisions

The Founders' instruction of 28 October 2026, recorded as given and as applied:

| | Decision |
|---|---|
| D1 | **Option 1.** The PERD §38.2 `decision_grant` lifecycle permits `SPENT → VOID`, only for a confirmed `REJECTED_STALE_VERSION` refusal. Every other transition out of `SPENT`, `VOID` and `EXPIRED` stays refused. The `decision_grant_guard` trigger is changed by a new forward-only migration, never bypassed |
| D2 | **One transaction.** The receipt, the invalidation of the grant, the RecoveryRequest and the outbox writes happen in one transaction. The Record events `RECEIPT` and `GRANT_VOIDED` are written in it. If any write fails, none is kept |
| D3 | **Audit continuity.** The `GRANT_SPENT` event stays on the Record. `GRANT_VOIDED` follows `RECEIPT`, and its payload names the change from `SPENT` to `VOID`, so the earlier state and the transition stay visible in the Record |
| D4 | **Regression evidence is a condition of merging.** The migration, this amendment, this record and the regression tests (the permitted transition, and every refused transition still refused) are reviewed before the `noema` pull request 90 merges |

## 2. Rationale and evidence

The conflict, quoted from the PERD v1.17 and the SoT (checked 28 October 2026):

> A. PERD REQ-EXE-004: "A version mismatch gives `REJECTED_STALE_VERSION`: the grant is void, the case returns to Trust, and there is no automatic retry." SoT §43.3: "`REJECTED_STALE_VERSION` voids the grant and returns the case to Trust." SoT US-19: "the conditional write is rejected (`REJECTED_STALE_VERSION`), no write is applied, the grant is void". PERD §28.1: "Grant | ISSUED, SPENT, VOID, EXPIRED".
>
> B. PERD §38.2, `decision_grant`: "ISSUED → SPENT, VOID or EXPIRED | Status only (via spend and void)". REQ-EXE-001 Audit: "`GRANT_SPENT` or `GRANT_VOIDED{reason}`". Migration 0001 enforces B with `decision_grant_guard` ("decision_grant: SPENT is final").

The refusal is made at E9, after E8 has spent the grant, so a refused grant is always `SPENT` first. A and B could not both hold. No line supported a grant that is both `SPENT` and `GRANT_VOIDED`. The Founders chose to keep A, change B, and keep the guard in force for everything else.

The exact §38.2 text this record changes (PERD v1.17, the `decision_grant` row, lifecycle column):

> before: `ISSUED → SPENT, VOID or EXPIRED`
>
> after (PERD v1.18): `ISSUED → SPENT, VOID or EXPIRED. SPENT → VOID only for a confirmed `REJECTED_STALE_VERSION` refusal (REQ-EXE-004); every other change of a grant that is SPENT, VOID or EXPIRED is refused`

The other two PERD lines changed are REQ-EXE-001's Audit line and REQ-EXE-004's Expected behaviour (before: "—"), Audit and Tests lines; PERD v1.18 lists them under "Changes in v1.18".

## 3. Agent decisions

1. **What "confirmed" means, and the mapping it rests on.** The instruction asks that the transition be permitted "when the receipt carries REJECTED_STALE_VERSION and the outcome check has confirmed that no write was applied", and then asks for the mapping of the real target's refusal to be verified. Verified on 28 October 2026:
   - *The target contract.* The POC's write target is `mock-case`, Noema's own case system. Tushe defines no case API: `tushe-spec-delta-v1.2.md` lists CON-01 and IDP-07 as "Not needed: Noema writes to its own case system", and the G0 worksheet answers AT-14 with "Noema covers". `mock-case`'s contract is PERD §34.4 ("Route with expected version: version mismatch returns a distinct error and applies nothing") and its OpenAPI document (`synthetic/mock_case/internal/api/openapi.json` in `noema`): the route answers `409` with the error name `VERSION_MISMATCH`, "nothing applied", with `current_version_token` in the details. Its `412 PRECONDITION_FAILED` is a different refusal, of a create that is conditional on absence.
   - *The mapping.* `409 VERSION_MISMATCH` → the adapter's class `VERSION_CONFLICT_409_412` (raw code `409:VERSION_MISMATCH`) → the receipt's typed field `transport_result` → execution state `REJECTED_STALE_VERSION` (PERD §27.1 E10). `412 PRECONDITION_FAILED` → `DUPLICATE_CREATE` → `REJECTED_BY_TARGET`, which never confirms. The class name's "409_412" is the wording of E10; the adapter gives the class to the one `409 VERSION_MISMATCH` only. The adapter's contract tests replay exchanges recorded from the real `mock-case`, and an end-to-end test against it stores the refusal as raw status `VERSION_CONFLICT_409_412:409:VERSION_MISMATCH` and signed `transport_result` `VERSION_CONFLICT_409_412`.
   - *What the first draft got wrong.* The first draft of the check read the unsigned `raw_status` column. The receipt contract has a typed, signed field for the transport result (`transport_result`, a string of the shape `^[A-Z][A-Z0-9_]*$`), and it has no typed reason code. The check now reads the signed document and cross-checks it against the row and the spend; `raw_status` is a diagnostic that must agree.
   - *The check.* PERD v1.18 defines a **confirmed refusal** as: the grant has exactly one receipt; it has the tenant, grant, attempt and idempotency key of the spend; its state is `REJECTED_STALE_VERSION`; its typed `transport_result` is `VERSION_CONFLICT_409_412`; it carries no external acknowledgement. A refused conditional write applies nothing (INV-27), so that is the evidence that no write was applied.
   - *Limits.* The receipt contract fixes the shape of `transport_result` but no value set, so the string is Noema's own constant. The database does not verify the receipt's HMAC; only Execution inserts receipts.
   - *Not an Outcome read.* The Outcome verifier is not built (plan task OUT-01) and its read is asynchronous (it runs from the outbox event that `Complete` writes), while D2 requires the void to be in the receipt's transaction. A gate on an Outcome verdict would make D2 impossible. Outcome's read still follows. **This is the one reading the Founders should confirm.** If they want the void to wait for an Outcome verdict, D2 changes: the receipt is written first and the void in a later transaction, with a recorded verdict as the precondition.
2. **Payload fields, not a new contract.** `payload` is not part of `record-event.v3.json`; its hash is. The `GRANT_VOIDED` payload therefore carries `from_status`, `to_status` and `receipt_id` without a contract change. The void reason and the event type are unchanged.
3. **The guard is replaced, not bypassed.** The migration uses `CREATE OR REPLACE FUNCTION decision_grant_guard()` and leaves the triggers as they are. Migration 0001 is not edited (forward-only).
4. **Pre-write voids are unchanged** (`ISSUED → VOID`), apart from the payload fields of decision 2.
5. **No conflicts-register entry.** The conflict was never listed there, so there is nothing to close in it.

## 4. Migration notes (AGENT-15)

- **Specification.** PERD v1.18 is a new file; v1.17 and earlier stay unchanged. The current-PERD pointers in [`docs/README.md`](../README.md) and [`poc/perd/README.md`](../poc/perd/README.md) move to v1.18.
- **Vendored copies.** The two PERD extracts in `noema` (`contracts/perd-32-2-event-types.md`, `services/core/orchestrator/perd-28-2-state-machine.md`) name the PERD file, and the other vendored copies name the docs commit, so they are re-pointed in the same session after this record merges (REQ-OPS-005). Their text does not change.
- **Code.** In `noema`: one forward-only migration (`decision_grant_guard` replaced); `ledger.Complete` makes the void in the receipt's transaction; the ledger tests assert `VOID` and every refused transition. No contract file changes. No existing row changes.
- **Nothing is migrated.** No grant exists outside tests and throwaway databases (checked 28 October 2026: the writer is not wired into `cmd/core`).

## 6. Amendment of 28 October 2026, after the merge of the pull request that added this record

PERD v1.18 is not edited in place. This amendment records three findings the Founders asked for; a PERD v1.19 is needed only if they want the text of REQ-EXE-004 to carry them.

**6.1 The "nothing applied" guarantee comes from `mock-case`'s OpenAPI document, not from a real target's contract.** §3 item 1 and PERD v1.18 REQ-EXE-004 take a confirmed refusal as the evidence that no write was applied, because "a refused conditional write applies nothing (INV-27)". For the POC that guarantee is `mock-case`'s: the route response `409` in `synthetic/mock_case/internal/api/openapi.json` ("VERSION_MISMATCH: a distinct error; nothing applied"), PERD §34.4 ("Route with expected version: version mismatch returns a distinct error and applies nothing") and `mock-case`'s own contract test. Tushe defines no case API for the POC (`tushe-spec-delta-v1.2.md`: CON-01 and IDP-07 "Not needed: Noema writes to its own case system"; the G0 worksheet, AT-14: "Noema covers"). **The guarantee must be re-verified against any real target before production use.** Nothing in the check can establish it for another target: the class `VERSION_CONFLICT_409_412` is whatever that target's adapter maps to it.

**6.2 The receipt's signature: nothing verified it before the receipt was written; the Founders decided to add two checks.** Checked on 28 October 2026 in `noema`, before the decision:
- `KeyRing.VerifyWith` was called in one place, `services/core/execution/controller/controller.go` (E1), and verified the grant's signature.
- The receipt was signed by `Controller.sign` and written by `ledger.Complete`, which stored the signature as it was. The recovery sweeper's receipts took the same path. No code verified a receipt's signature before or after the write.
- The SoT puts that check in Outcome (SoT §13.1, the "Checks" row of the constitution table: "Signature of the receipt"). Outcome is not built (plan task OUT-01). The PERD has no requirement that names it, and REQ-SEC-005 describes one HMAC key "for grants and confirmation requests".
- The database holds no key (PERD §41.1). The trigger of migration 0002 compared the signature member of the signed document with the row's signature columns: a consistency check, not a verification, and not even a check that the value was non-empty (an empty key and an empty value on both sides passed).

**Decision of the Founders, 28 October 2026 (options 2 and 3 of the four offered), implemented in `noema#94` and `noema#90`, not yet merged:**
- *The trigger.* The receipt's signature, in the signed document and in the row, must have a non-empty key and a value of 64 lower-case hex characters (the shape that `crypto.Verify` accepts for an HMAC-SHA-256). This is a shape check; the database cannot verify an HMAC.
- *The Controller.* `Controller.completeReceipt` verifies the receipt's HMAC with `KeyRing.VerifyWith`, over the canonical JSON of the document it signed, before `Ledger.Complete` writes the receipt, for the receipt of a dispatch (E11) and for the sweeper's receipt. A failed verification writes nothing: no receipt, no Record event, no RecoveryRequest, no outbox event, the grant is not voided; the attempt stays `DISPATCHING` and the sweeper takes it over as `OUTCOME_UNKNOWN`. A forged or empty signature is refused on both sides, and tests show it.
- *What remains.* Whoever can write as `execution_rw` without the Controller can still write a well-formed signature that verifies against nothing; the database cannot close that without a key. Outcome, when built, is a further checker (SoT §13.1). No security event is appended on a failed verification (the instruction was that a failure writes nothing); REQ-SEC-005 says verification failures "fail closed and raise an alert", so an alert on this path is a follow-up the Founders may ask for.

**6.3 Reconciling "the row's signature" with "the database does not verify the HMAC".** The first is condition (g) of the trigger: the signed document's signature member equals the row's signature columns and, after the decision in 6.2, has the shape of an HMAC-SHA-256. The second is the limit in §3 item 1. They do not conflict: (g) compares two copies of one string and checks its shape; the verification of the HMAC is the Controller's. Wording that read like a verification ("the document's signature is the row's signature") is reworded in the `noema` migration comment and README, and PERD v1.18's wording, which says only that the document is "checked against the spend" and that "the database does not verify the receipt's HMAC", stands.

## 7. Amendment of 29 October 2026: a failed receipt verification appends one SECURITY_EVENT SIGNATURE_INVALID

**Status of this section: proposed by the Technical Co-Founder's agent, in the direction the Founders approved on 29 October 2026 (given in a working session; it counts once this amendment is merged).** The pull request that adds it is for the Founders to merge.

**7.1 The conflict, named.** §6.2 records the Founders' decision of 28 October that a failed receipt verification "writes nothing: no receipt, no Record event, no RecoveryRequest, no outbox event", and says an alert on this path "is a follow-up the Founders may ask for". The clauses that call for an alert are:

| Source | Clause |
|---|---|
| PERD v1.18 REQ-SEC-005, Requirement | "Verification failures fail closed and raise an alert." |
| PERD v1.18 §32.2, Security row | `SECURITY_EVENT{kind: … SIGNATURE_INVALID …}` is an adopted event type and kind (DEC-2026-10-17) |
| PERD v1.18 §12.5, EC-X09 | "Forged Intent Object (bad or missing HMAC on the internal hop) or forged confirmation: Reject; security alert" |
| PERD v1.18 §42, TM-17 | "Forged internal object": detection "Signature failures"; record `SECURITY_EVENT`; test EC-X09. [`threat-to-test-map.md`](../security/threat-to-test-map.md) lists TM-17 as "Not started", with no REQ named |
| PERD v1.18 REQ-AUD-001 | Every power appends events about its own objects "in the same transaction as the object write wherever possible"; if an append fails, the enclosing transaction fails and the action does not happen |
| SoT §13.1 ("Checks" row), §47.4 | Names the receipt's signature as a check and sets the key policy. The SoT has no clause that requires an alert for a failed receipt signature (INV-11's alert is for a chain break) |

Authority order applied: SoT, then decision records, then the PERD. §6.2 is a decision record and outranks the PERD's REQ-SEC-005 wording, so the PERD cannot override it; the two cannot both hold as written, and this amendment is the smallest change that lets both stand. It changes one word of §6.2 ("no Record event" becomes "no Record event except the one below") and nothing else.

**7.2 The amendment.** §6.2's "writes nothing" is read as: a failed verification writes no receipt, no `RECEIPT` or `GRANT_VOIDED` event, no RecoveryRequest, no outbox event, and changes neither the grant nor the attempt. **It appends exactly one Record event, `SECURITY_EVENT` of kind `SIGNATURE_INVALID`, and nothing else.** The no-business-side-effects rule stands: the event is the only write.

**7.3 The rules, each with its test in `noema#90`:**

| | Rule | Test |
|---|---|---|
| Failure behaviour | The receipt is refused with `ErrReceiptSignature`; fail closed. The attempt stays `DISPATCHING`; the sweeper takes it over as `OUTCOME_UNKNOWN` with the honest key ring. The same holds for the sweeper's own receipt | `TestAFailedReceiptVerificationAppendsExactlyOneSecurityEventAndNothingElse` (controller, simulated; ledger, real PostgreSQL) |
| Write permission | No new privilege, role, table, column, contract field or metric. The event goes through `Ledger.Append`, which calls `record_lock_head` and `record_insert`, the two functions `execution_rw` already may execute (migration 0001). `execution_rw` gains no write on any table. There is no `ops_alert` row and no `OPS_ALERT_RAISED` (both stay unbuilt, PERD §32.2 and §38.2) | the existing role tests; the real-PostgreSQL test reads `written_by` and the event's object |
| Event contents | `event_type` `SECURITY_EVENT`, `kind` `SIGNATURE_INVALID`, `written_by` `core-execution`, `object_ref` the grant ID, the tenant and correlation of the grant. Payload: `cause` (`RECEIPT_SIGNATURE_NOT_VERIFIED`, or `RECEIPT_DOCUMENT_NOT_CANONICAL` if the document cannot be canonicalised), `receipt_id`, `attempt`. **Never** the signature, the key ID the receipt claims, the document or any text from the target (all untrusted) | the real-PostgreSQL test reads the payload and shows the forged value is nowhere in the Record |
| Transaction boundary | A transaction of its own, after the verification fails and with no other write open. There is no object write for it to share (REQ-AUD-001), and the receipt is never written | the Record holds `REVALIDATION_PASSED`, `GRANT_SPENT`, `DISPATCH_ATTEMPTED`, `SECURITY_EVENT`, in that order and no `RECEIPT` |
| Count | One event per failed verification. The dispatch path and the sweeper each verify once per receipt, and the sweeper stops at its first failure, so one sweep adds at most one event. A repeating key fault therefore adds one event per sweep until it is fixed | the sweeper case in the same tests (two events after one dispatch failure and one sweeper failure; none after an honest recovery) |
| If the event write fails | Nothing is written either. `Execute` and `Recover` return an error that is `ErrReceiptSignature` **and** carries the append failure (`errors.Is` holds for both); the grant stays `SPENT`, the attempt `DISPATCHING`, no receipt, no event, no RecoveryRequest, no outbox event; the Record chain still verifies. The event that failed is not invented later by the sweeper. The failure is surfaced to the caller; this is the same fail-closed rule as EC-E16 (nothing is done that the Record cannot hold) | `TestIfTheSecurityEventCannotBeAppendedNothingIsWrittenAndBothFailuresAreReturned` (controller, with a refusing ledger; ledger, with a real fault: a trigger planted with the admin role refuses a `SECURITY_EVENT` inside `record_insert`) |
| Honest receipts | A receipt that verifies appends no event | `TestAnHonestReceiptAppendsNoSecurityEvent` |

**7.4 What this does not do, stated plainly.**
- It is a Record entry, not a notification. Nothing reads `SECURITY_EVENT` and tells anyone; there is no `ops_alert` row, no `OPS_ALERT_RAISED` and no metric (none is built, and the Founders asked for none). REQ-SEC-005's "raise an alert" is met as far as TM-17 names it (`SECURITY_EVENT`) and no further. Operator notification stays open until the alert path (`ops_alert`, REQ-OPS) is built.
- On the dispatch path the Controller signs the receipt itself just before it verifies it, so a failure there means the key ring cannot verify what it signed (a key-ring or configuration fault, or a canonicalisation fault), not a forgery by an outsider. The event is the right record of it. It does not detect a forged receipt written by a caller with `execution_rw` that bypasses the Controller (see the debt entry for that risk).
- The SoT is unchanged. PERD v1.18 is not edited in place; a PERD v1.19 is needed only if the Founders want REQ-SEC-005 or EC-X09 to carry this reading.

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted in principle, with conditions | 28 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
