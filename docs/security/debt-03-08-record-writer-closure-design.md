# DEBT-03 and DEBT-08: closing the Record writers, and the test that starts REC-08

**Core Engineer 1 (Execution, Record, Recovery), 6 Nov 2026. Derived and non-normative: the [SoT](../NOEMA_SOURCE_OF_TRUTH.md), the PERD, [DEC-2026-11-01-receipt-and-record-signing](../decisions/DEC-2026-11-01-receipt-and-record-signing.md) (D-numbers below) and [`debt.md`](../poc/execution/debt.md) decide. Nothing here is a decision; every default it names stays [REC] or [OQ] until adopted.** SYNTHETIC data only. The closing task is REC-08 (REQ-AUD-006, C1, planned 1 Dec 2026, gate G3); this note exists so REC-08 starts with its closure test specified. Dates in `tasks.csv` rule; this note moves none.

## 1. What is built on `main` and what is still open

| Fact | Where it is read from |
|---|---|
| A Record write goes through `record_lock_head_t()` and `record_insert_t(...)`. The tenant comes from the calling login (`session_user` mapped in `tenant_login`), never from an argument (DEBT-04, closed on `main`). | `services/core/migrations/0004`, `0005`; `record/chain/chain.go` |
| `written_by` must be the emitter the login is bound to (a power's own emitter, or the one emitter a `record_emitter` login is bound to). A login of one power cannot write in another power's name through `record_insert_t`. | `record_insert_t`, `tenant_login.emitter` (DEBT-07 slice, noema#145) |
| Nothing in the database holds a key. The event's `hash` is computed by the caller; the function checks only that the event extends the head. So a holder of **one runtime credential** is limited to its own emitter and tenant, but **can still append any well-formed event as that emitter**, and a holder of `outcome_rw` can still call `outcome_record_verdict(...)` and write a verdict nobody reached. | DEBT-03, DEBT-08 text; `0007` |
| After REC-08 the database refuses an event whose Ed25519 signature does not verify under a registered, ACTIVE key of its `written_by` identity. | D1, D11, D12, REQ-AUD-006 |

Honest reading: DEBT-04 and DEBT-07 already narrowed the blast radius (tenant and emitter are bound to the login). DEBT-03 and DEBT-08 are closed only when **possession of a database credential no longer lets anyone make an event or verdict verify**. The key lives outside PostgreSQL (D3).

## 2. What REC-08 builds (from the decision record, not new)

1. `record-event.v4` with a required `sig` (D1 and §4.3 of the decision record); `hash` keeps its v3 meaning and `sig` is outside the hashed body. v3 is not edited.
2. `record_event.signed_jcs` and `sig_key_id`/`sig_value` columns; a `BEFORE INSERT` trigger, `ENABLE ALWAYS`, owned by `noema_migrator`, that rebuilds the message `noema/record-event/v1\n` + `JCS(event without hash and without sig)`, runs the D7/D8 consistency checks (tenant, `seq`, `prev_hash`, `written_by` against the row), calls `noema_sig.verify('record-event', …)` (already built for receipts in migration 0012) and raises `NS001` on false (D12).
3. Fail closed when verification is unavailable (D13): a Record append that fails fails its enclosing transaction (REQ-AUD-001, EC-E16).
4. Every writer signs with its own identity key (D2): `core-execution`, `core-outcome`, `core-trust`, `core-evidence`, `core-workflows`, `core-edge`, `core-record`, `admin`. An identity with no registered key cannot append. The eight runtime emitters of `record/chain/actors.json` (model service and the mocks) have no key under the OD-P-73 default (a proposal, not a decision), so the database refuses their events; that default must be adopted before DEBT-07 closes.
5. The chain verifier (REC-05) checks every signature and reports a revoked key's events.
6. `outcome_record_verdict` (DEBT-08): the verdict document is signed by `core-outcome` and verified by the same function (purpose `outcome-verdict`); the table `outcome_verdict` gets its trigger (D12). `outcome_rw` alone no longer suffices.

Dependencies already merged or in review: 0012 (`noema_sig.verify`, `signing_key`, rotation and revocation; noema#229), `refuseEnabledExtensionEventTrigger`, `internal/sigfixture` and `execution/signing/signingtest` (signing helpers for tests that must not import Execution's signer). Not built: any signer for a non-Execution identity, record-event v4, and the Record trigger.

## 3. The closure test, written before the code (failing first)

Run it **before** any REC-08 code, on the `main` of that day; it must fail by the forgery succeeding, with the run linked. SR owns writing it (debt.md DEBT-03 owners); C1 supplies the fixtures.

**Setup.** A migrated database; tenants `ten_a` and `ten_b`; one login per power for `ten_a`, mapped in `tenant_login`; SYNTHETIC keys for `core-execution` and `core-outcome` registered through `key_register`; the private halves held only by the test.

**Forgery matrix: every cell must be refused after REC-08 and must succeed today.** Each is attempted with the credential named, **and with no key**, and with the **wrong identity's key**:

| # | Credential and path | Forged object | After REC-08 |
|---|---|---|---|
| 1 | `execution_rw` login → `record_insert_t` | a well-formed event, `written_by = core-execution`, correct `prev_hash`, no `sig` | `NS001` |
| 2 | same, `sig` made with a key the database does not hold | same | `NS001` |
| 3 | same, `sig` made with `core-outcome`'s key | same | `NS001` (identity binding, D2/D11) |
| 4 | `outcome_rw` login → `outcome_record_verdict(...)` | an `ACHIEVED` verdict and its events that Outcome did not reach (DEBT-08) | refused; no verdict, request or event is kept |
| 5 | `outcome_rw` login → `record_insert_t` | an Outcome-emitter event without Outcome's key | `NS001` |
| 6 | any runtime login, direct `INSERT INTO record_event` (and `COPY`) | any row | privilege error (already true) and, if the privilege were granted, `NS001` (mutation check) |
| 7 | genuine signed event replayed at another `seq`, chain or tenant | a replay | refused (D7: the signature binds `tenant_id`, `seq`, `prev_hash`, `written_by`) |
| 8 | runtime login: `SET session_replication_role = replica`, `ALTER/DISABLE TRIGGER`, `CREATE OR REPLACE` of the verifying function | trigger bypass | refused, and the trigger is `ENABLE ALWAYS` |
| 9 | revoked key | an event signed before and after `compromised_since` | later ones refused; the verifier reports earlier ones as untrusted (REC-05) |
| 10 | extension dropped or library missing | a correctly signed event | refused, no row, nothing else of the transaction kept (D13) |
| 11 | rotation | two ACTIVE keys both insert; a RETIRED key is refused for inserts and still verifies in the verifier; a third ACTIVE key cannot be registered | as D3/D5 |

**Mutation check (decision-record test 14).** Remove each condition of the trigger in turn (purpose, identity, `seq`/`prev_hash` binding, tenant binding, `NS001` raise); each removal fails a named test.

**The closing evidence** for DEBT-03 and DEBT-08 is the green run of this matrix at the final head, SR's independent validation, and the list of paths checked (the A20 list; `docs/security/decision-tables-row-security-audit.md` in noema is the pattern). It is not a log line (AGENT-21).

## 4. Order of work for REC-08 (so the closure test is never the last thing written)

1. SR (or C1 for SR) commits the forgery matrix as a tests-only commit; the red run is linked in the PR.
2. Contract: `record-event.v4.json`, `reconstruction.v4`, codegen, INVENTORY, fixtures, golden vectors family `ed25519_signing_vectors` (AGENT-15 steps: version bump, migration note, regenerated models).
3. Migration: `signed_jcs` and signature columns on `record_event`, the trigger, the `record_insert_t` change to pass the signed bytes. Forward-only, after the numbers then taken (D3).
4. Signers: Execution first (it already signs receipts), then Outcome (C2, through its own signer port, never importing Execution's), then the other identities as they first write.
5. The chain verifier checks signatures; revoked-key report.
6. Closure run, SR validation, DEBT-03 and DEBT-08 rows updated by the owners (the agent does not close them).

## 5. Open points to take to the Engineering Lead (not decided here)

- **OD-P-73** (no key for the eight runtime emitters): must be adopted, or those events stay unwritable and DEBT-07's closure needs EDG-01 to carry them.
- **Existing rows.** Record chains exist only in tests and local Compose today, as for receipts. If a longer-lived chain existed, its v3 rows would have no `sig`; the trigger would apply to inserts only and the verifier must accept v3 rows below a recorded cut-over `seq`. The decision record is silent on a cut-over; ask.
- **Who signs `admin` events** (D2a) and where that key is held for the POC.
- **Per-insert cost.** Decision-record test 15 measures it against the PERD §47 budget; Record appends are on every consequential path.

## 6. What this note does not do

It adds no requirement, contract, threshold or state, changes no tier, and closes nothing. Closure belongs to the DEBT owners (EL accountable, C1 builds, C2 signs Outcome's events, SR validates; `debt.md`).
