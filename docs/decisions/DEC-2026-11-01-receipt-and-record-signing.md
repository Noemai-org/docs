# DEC-2026-11-01-receipt-and-record-signing

- **Status:** **Proposed.** Nothing here is decided or adopted. The Founders decide; the Technical Co-Founder and the Founder confirm by approving the pull request that adds this record. W2's spike checks T1 to T6 passed in CI (58 of 58, 1 Nov 2026; §1), so under the Architect's condition the direction is pgsodium, not Option C. It remains subject to the Founders' approval of the dependency (AGENT-14, OD-P-72) and to W4. If the Founders refuse the dependency, §11 (Option C) applies instead. **Updated 1 Nov 2026** for the spike's findings: Alpine kept (D10), the pgsodium event trigger disabled at bootstrap (D10a), the T6 pass condition (D13).
- **Date:** 1 November 2026
- **Task:** GOV-28 (W1). Owners in tasks.csv: EL, FND. Prepared by the Engineering Lead role agent; the Founders own the decision.
- **Closes:** none. Proposes the design that DEBT-01 closure criterion (1) requires, and the PERD text that adopts it. It opens [OD-P-72](../open-decisions.md#od-p-72) (pgsodium, AGENT-14) and [OD-P-73](../open-decisions.md#od-p-73) (keys for `model-service` and the adapter emitters).
- **Owner:** Founder and Technical Co-Founder.
- **Authority order applied:** SoT v1.10 → decision records (DEC-2026-10-28-spent-grant-void, DEC-2026-10-29-receipt-signature-alert, DEC-2026-10-31-proof-depth-and-completeness D18 to D20) → PERD v1.19 → plan v1.10.

## 1. Inputs, and what each one fixes

| Input | What it fixes for this design |
|---|---|
| DEBT-01 ([`debt.md`](../poc/execution/debt.md)), Tier 0 | A caller with `execution_rw` can insert a well-formed forged receipt and void a `SPENT` grant once `noema#94` lands. Six closure criteria; `noema#94` and `noema#90` stay held until they are evidenced |
| DEC-2026-10-28-spent-grant-void D2 | The receipt, the void, the RecoveryRequest and the outbox are one transaction (the "28 Oct transaction rule"). Option B keeps it; Option C changes it (§11) |
| DEC-2026-10-29-receipt-signature-alert, DEBT-02, OD-P-71 | A human must be alerted on a failed receipt signature. Not met; not changed here |
| DEC-2026-10-31 D18, D20 | One signing design for receipts and Record events. "Tamper-evident", never "tamper-proof". Limit: it defeats a stolen database credential, not a compromised core process |
| PERD v1.19 REQ-AUD-006 | Each writing power signs each event with its own Ed25519 key over the RFC 8785 event including the previous hash; the database refuses an event that does not verify; trusted keys sit in a table owned by the migration role |
| W2 evaluation (SEC-12), `docs/security/w2-ed25519-extension-evaluation.md`, docs#78, **not yet merged** | Recommends pgsodium v3.1.11 (commit `a8b8a27`), conditional on spike checks T1 to T6; rejects `pg_ed25519`; `pg-crypto` not yet; Option C if none is viable. GOV-28's Needs is SEC-12, so this record cannot be approved before W2 is merged |
| W2 spike, §10 addendum of the evaluation; [run 41314576829](https://github.com/Noemai-org/noema/actions/runs/41314576829), carried by noema#106 (test infrastructure only, not on `main`) | 58 of 58 checks pass for T1 to T6 on `postgres:17.11-alpine` with libsodium 1.0.22 (SHA-256 and minisign signature checked) and pgsodium v3.1.11 (full commit id checked). No base change was needed. **Finding:** without `shared_preload_libraries`, pgsodium's event trigger `pgsodium_trg_mask_update` makes every DDL command fail; the fix is to disable it at bootstrap (D10a). Not shown by the spike: performance, extension upgrades, the real canonical bytes of this record |
| Architect, 1 Nov 2026 (relayed in the Engineering Lead session; counts once this record or another is committed) | (a) The PostgreSQL target is the major Compose runs today, **17.11**; a custom image may change the base image if pgsodium does not build on Alpine, and this record says so (§5.1). (b) **`execution_rw` must never be a member of the migration role**: a design requirement (§6). (c) The Record table's owner must be the migration role; confirm from migration `0001` what it is today and state any deviation (§6.1). (d) **One Ed25519 key per power that writes events, including Outcome's verdict signing, kept separate from Execution's** (§3, §8) |
| `noema` `main` at `34f6a8b` | Migration `0001`; `record/chain/actors.json` (17 emitters, 16 with scope `RUNTIME`); only `core-execution` appends events today (`execution/ledger/ledger.go:138`); `execution-receipt.v1` and `outcome-verdict.v1` carry `sig: {key_id, value}`; Compose runs `postgres:17.11-alpine` (digest-pinned), migrations as the superuser `postgres` |

## 2. What this design does, in one paragraph

Each core power that writes signs what it writes with its own Ed25519 private key, held outside PostgreSQL. The database holds only public keys, in a table that only the migration role can change. A trigger that the migration role owns verifies every receipt, Record event and Outcome verdict as it is inserted, through one verification function that calls pgsodium. An insert whose signature does not verify, or that cannot be verified at all, fails. The signed bytes bind the tenant, the grant, the attempt, the idempotency key and the state, so a genuine receipt cannot be replayed against another grant. A caller holding any runtime database credential but no private key can no longer insert a receipt, an event or a verdict that the database accepts. That closes DEBT-01's path. It does not protect against a compromised core process, which holds the private keys (§9).

## 3. Signing keys: one per writing identity

**D1. Scope.** Ed25519 signs three objects: execution receipts (`execution-receipt.v1`), Record events (record-event v4, §4.3) and Outcome verdicts (`outcome-verdict.v1`). Grants and confirmation requests stay HMAC-SHA-256 under REQ-SEC-005 until before Phase 2; this record does not change them.

**D2. One key pair per writing identity.** The key's identity is a `written_by` value of record-event v3 (PERD §32.1). A key signs only for its own identity, and the database checks that the key's identity matches what the object claims.

| Identity (`written_by`) | Signs | Notes |
|---|---|---|
| `core-execution` | Receipts; its Record events | Today's only writer of events |
| `core-outcome` | Outcome verdicts; its Record events | **Separate from `core-execution`**, so Outcome's verification of a receipt stays independent (SoT §13.1; §8) |
| `core-trust` | Its Record events | Grants stay HMAC (D1) |
| `core-evidence`, `core-workflows`, `core-edge`, `core-record` | Their Record events | Each gets a key when it first writes an event; until then it has no key and cannot append |
| `admin` (control plane) | `KEY_ROTATED`, `POLICY_PUBLISHED`, `PACK_LOADED`, `KILL_SWITCH_CHANGED`, `CONFIG_CHANGED` | The admin key is held by the operator tooling, not by the core's runtime |
| `model-service`, and the adapter emitters `mock-ledger`, `mock-switch`, `mock-destination`, `mock-customer`, `mock-policy`, `mock-case`, `mock-clock` | **Nothing in the POC** | **Open: [OD-P-73](../open-decisions.md#od-p-73).** No code appends as these today. Safe default: no key is registered, so the database refuses any event that claims them. The model service never holds a Record key or any core credential (INV-29) |
| `benchmark-runner` | Nothing | Already refused by the core (`BENCHMARK_ONLY` in `actors.json`) |

**D3. Custody.**
- Each private key is a separate file-mounted secret (PLT-05; OQ-09 decides the shared-environment secrets manager). It is read at start-up only by the package of the power that owns it, and never by another. An architecture-lint rule enforces this: `execution` cannot import Outcome's signer, and `outcome` cannot import Execution's.
- No private key enters PostgreSQL, a log, a trace, a fixture, a PR or the model service. The SEC-07 scanner covers logs.
- Signing uses Go's standard library `crypto/ed25519`. That is not a new dependency.
- Before Phase 2, keys move to a regional managed key service (REQ-SEC-005, SoT §47.4). This record does not move them.

**D4. Key ID and version.** `sig.key_id` is `<identity>.ed25519.<version>`, for example `core-execution.ed25519.3`, matching `^[a-z][a-z-]*\.ed25519\.[1-9][0-9]*$`. `sig.value` is the 64-byte signature as 128 lower-case hex characters. The key ID carries both the identity and the version, so a verifier never infers either. Sorting by key ID is not ordering: the database compares versions as integers.

**D5. Rotation and revocation.**
- A key is in one of three states: `ACTIVE`, `RETIRED` or `REVOKED`.
  - At most **two** keys per identity are `ACTIVE` (the rotation overlap of REQ-SEC-005). The signer always uses the newest active version.
  - **The database accepts an insert only under an `ACTIVE` key.** A `RETIRED` or `REVOKED` key is refused for new inserts.
- **Retirement** is routine. Objects signed while the key was active still verify for the chain verifier (REQ-AUD-005), because the key table keeps retired keys and the time they were retired.
- **Revocation** is for a key believed compromised. It records `compromised_since`. The chain verifier reports every object signed under a revoked key at or after `compromised_since` as untrusted for human review; it never silently accepts them.
- Only the migration role changes the key table, through three functions it owns: `key_register`, `key_retire` and `key_revoke`. No runtime role can execute them.
- Each change appends `KEY_ROTATED`, written by `admin`. The first keys are registered by the migration that creates the table, which writes no event; the first `KEY_ROTATED` follows the first rotation.

## 4. Canonical bytes: exactly what is signed

**D6. The message.** For each object type, the message is a fixed domain tag followed by the RFC 8785 (JCS) bytes of the document without `sig`. The JCS is the same implementation the Record already uses (`platform/crypto`, `tools/jcs_ref.py`; integers only).

| Object | Domain tag (UTF-8, ending in a line feed) | Document |
|---|---|---|
| Receipt | `noema/receipt/v1\n` | `execution-receipt.v1` without `sig` |
| Record event | `noema/record-event/v1\n` | The event without `hash` and without `sig`: exactly the body that `hash` covers, including `prev_hash` and `seq` |
| Outcome verdict | `noema/outcome-verdict/v1\n` | `outcome-verdict.v1` without `sig` |

The tag stops a signature over one type from verifying as another (cross-type confusion). The key's identity (D2) stops one power's signature from passing as another's.

**D7. What the signed receipt binds**, and how the database checks it at insert.
- **The fields.** The signed document carries `tenant_id`, `grant_id`, `attempt`, `idempotency_key`, `execution_state`, `receipt_id`, `transport_result`, `external_ack`, `correlation_id`, `logical_action` and `dispatched_at` (all required by `execution-receipt.v1`).
- **The database checks** that:
  1. every one of those fields equals the row's own column;
  2. the tenant, grant, attempt and idempotency key equal the `grant_spend` row that E8 recorded;
  3. the key's identity is `core-execution`.
- **The effect on replay.** A genuine receipt cannot be replayed against another grant, tenant, attempt, idempotency key or state: any changed field breaks the signature, and copying the bytes unchanged fails check 2. `UNIQUE (grant_id, attempt)` stops a second copy for the same attempt.
- **Verdicts** bind `tenant_id`, `verdict_id` and `receipt_id`. **Record events** bind `tenant_id`, `seq`, `prev_hash` and `written_by`, so a signed event cannot be moved to another position, chain or emitter.

**D8. The signed bytes are stored.** The database has no JCS implementation, so each signed table gains a `signed_jcs bytea` column holding the exact document bytes that were signed, without the tag. At insert, the trigger checks:
1. that the signature verifies over the domain tag followed by `signed_jcs`;
2. that `convert_from(signed_jcs, 'UTF8')::jsonb` equals the row's parsed document without `sig` (`json`, or `body` for events);
3. that the row's typed columns equal the document's fields.

The Go writers and verifiers (Controller, Outcome, chain verifier) also require that `signed_jcs` is exactly the JCS of the document. A document with duplicate member names is refused there, because `jsonb` would silently keep only the last one.

**D9. Contracts (AGENT-15).**
- `execution-receipt.v1` and `outcome-verdict.v1` keep their shape (`Sig` is `{key_id, value}`). Their migration note: the algorithm is now chosen by the key table, and `common.v1.json` `Sig`'s description changes from "HMAC-SHA-256 in the POC" to name both algorithms and the object each signs. That is a description change, and validation is unchanged. A v1 reader that verifies with HMAC refuses an Ed25519 value, which fails closed. No HMAC-signed receipt exists outside tests.
- **record-event v4** (`record-event.v4.json`, a new major) adds a required `sig`. `hash = SHA-256(prev_hash ‖ JCS(event without hash))` keeps its v3 meaning: `sig` is outside the hashed body, and both are computed over the same body. `reconstruction.v4` follows. v3 is not edited.

## 5. Database verification

**D10. The extension (conditional; [OD-P-72](../open-decisions.md#od-p-72), AGENT-14).**
- **Which build.** pgsodium **v3.1.11, commit `a8b8a2739bab1f7a07445b1c911e2bd1abf67784`**, built from source into Noema's own PostgreSQL **17.11** image. libsodium is a pinned version, and its tarball's checksum and signature are verified at build. The upstream Dockerfile is not reused (it verifies nothing).
- **Base image.** `postgres:17.11-alpine`, digest-pinned, as Compose runs today. **Kept** (Architect, 1 Nov 2026): the spike built libsodium 1.0.22 and pgsodium v3.1.11 on it and passed T1 to T6, so no base change is needed. libsodium is pinned by SHA-256 and its minisign signature is checked against the project's published key; pgsodium is pinned by full commit id, compared after checkout.
- **What is used.** Only `pgsodium.crypto_sign_verify_detached`. There is no `shared_preload_libraries` entry, no server key, and no Transparent Column Encryption. `EXECUTE` on every pgsodium function is revoked from `PUBLIC`.
- **Unused objects.** The roles, tables and event triggers that pgsodium installs are unused. W4 lists them, and T5 shows that none can be used by a runtime role.

**D10a. pgsodium's event trigger is disabled at bootstrap (W4 carries it).** Without `shared_preload_libraries`, the event trigger `pgsodium_trg_mask_update` reads `pgsodium.enable_event_trigger`, a setting that exists only when the library is preloaded, so every DDL command it fires on fails, including a forward-only migration's `ALTER TABLE` (spike finding). Preloading is not used, because it starts pgsodium's server-key management. So, once, as a superuser, in the same bootstrap step that runs `CREATE EXTENSION pgsodium` and before any Noema migration:
  1. `ALTER EVENT TRIGGER pgsodium_trg_mask_update DISABLE;` and the same for every other event trigger the extension installs (W4 lists them from `pg_event_trigger` after `CREATE EXTENSION`);
  2. `ALTER DATABASE <db> SET pgsodium.enable_event_trigger = 'off';`

  Transparent Column Encryption is not used, so nothing depends on these triggers.
- **Guard against re-enabling.** An extension upgrade (`ALTER EXTENSION pgsodium UPDATE`) or a re-install could re-create or re-enable an event trigger. So `db.Migrate` checks first, and refuses to run if any event trigger owned by the extension (`pg_depend` with `deptype = 'e'` on `pgsodium`) has `evtenabled` other than `'D'`. The core's start-up check does the same and refuses to start. Both fail closed, and a test covers each (§10, item 16). Upgrading the extension is a change under AGENT-14 that re-runs T1 to T6.

**D11. One verification function**, `noema_sig.verify(purpose text, claimed_identity text, key_id text, msg bytea, sig_hex text) RETURNS boolean`.
- **Properties.** Owned by the migration role, `SECURITY DEFINER`, `SET search_path = pg_catalog, pg_temp`, and every call schema-qualified.
- **It returns false** unless all of the following hold:
  - `sig_hex` matches `^[0-9a-f]{128}$`, so it decodes to exactly 64 bytes;
  - the key ID matches D4;
  - the key exists, is `ACTIVE`, and its identity equals `claimed_identity`;
  - the purpose (`receipt`, `record-event` or `outcome-verdict`) is one that identity may sign (D2);
  - the public key is exactly 32 bytes;
  - `pgsodium.crypto_sign_verify_detached(decode(sig_hex, 'hex'), msg, public_key)` is true.
- **It has no exception handler.** Any error from pgsodium or from a missing extension propagates and aborts the statement.

**D12. Triggers.**
- **Where.** A `BEFORE INSERT` trigger on each signed table: `execution_receipt` (W4), `record_event` (REC-08), and `outcome_verdict` when OUT-01 creates it. The trigger rebuilds the message from the domain tag and `signed_jcs`, runs the D7 and D8 checks, calls `noema_sig.verify`, and raises `SQLSTATE 'NS001'` ("signature not verified") on false.
- **Firing.** Each trigger is set `ENABLE ALWAYS`, so it fires even under `session_replication_role = replica`. A trigger fires on every insert path: `INSERT`, `INSERT … SELECT`, `COPY` and inserts from any function.
- **The `SECURITY_EVENT`.** When a core writer receives `NS001`, it appends `SECURITY_EVENT SIGNATURE_INVALID` in a transaction of its own, signed with its own key: the rule of DEC-2026-10-28 §7, extended to the database's refusal. A forger who holds only a database credential triggers no event. The insert fails, and the database log carries the refusal. Detecting such attempts is DEBT-02's alert path, not this record.

**D13. When verification is unavailable, inserts fail closed.** If the extension is missing, the library file is gone or the function errors, the insert raises and its transaction rolls back, so nothing is accepted unverified.
- **The core's reaction.** Every operation that needed the insert stops:
  - a receipt that cannot be written leaves the attempt `DISPATCHING`, and the sweeper takes it over as `OUTCOME_UNKNOWN`;
  - a Record append that fails makes its enclosing transaction fail (REQ-AUD-001, EC-E16).
- **Why there is no `SECURITY_EVENT` here.** The original T6 row of W2 §7 expects "a `SECURITY_EVENT` rather than silence". That cannot hold: when verification is unavailable, no Record append succeeds, including the `SECURITY_EVENT` itself. The signal is the error the core returns and its structured, redacted log line. A human alert for this case is part of DEBT-02 and OD-P-71 (a channel that does not depend on the database).
- **T6 pass condition (agreed wording, proposed to the Security Reviewer for docs#78):** with the extension dropped, or its library file missing, or the verification function raising, a correctly signed receipt or event is refused, no row is added, and no other write of that transaction is kept; the core returns the error and logs it (structured, redacted). No `SECURITY_EVENT` is expected, because no Record append can succeed while verification is unavailable; alerting a human is DEBT-02 (OD-P-71). The spike's own T6 already tests this ("a valid receipt is refused and no row is added").

## 6. Privileges

**D14. The migration role.** Migration `0001` creates no named migration role (see §6.1). W4 creates `noema_migrator`, `NOLOGIN`. The deployment's migration login is its only member; in Compose that is the superuser `postgres`, which runs `db.Migrate` today.
- **Design requirement (Architect, 1 Nov 2026):** `execution_rw`, and every other runtime role (`trust_rw`, `outcome_rw`, `evidence_rw`, `orchestrator_rw`, `record_append`), is **never** a member of `noema_migrator`, directly or through another role. A test pins this from `pg_auth_members`, recursively.
- **No privileged attributes.** No runtime role is `SUPERUSER`, `CREATEROLE`, `CREATEDB`, `REPLICATION` or `BYPASSRLS` (pinned).

**D15. What `noema_migrator` owns**, after W4 and REC-08:
- the tables `execution_receipt`, `record_event`, `record_chain_head`, `signing_key` (and `outcome_verdict` when it is created);
- the functions `noema_sig.verify`, the trigger functions, `receipt_insert`, `key_register`, `key_retire`, `key_revoke`;
- the triggers;
- the schema `noema_sig`.

**D16. What the runtime roles may do.**
- **`execution_rw`** loses `INSERT` on `execution_receipt`. It inserts only through `receipt_insert(...)`, a `SECURITY DEFINER` function owned by `noema_migrator` on which `execution_rw` has `EXECUTE`. The trigger still verifies every insert, whatever the path. Revoking the write and verifying the content are separate controls, each with its own test (W2 §3).
- **`record_append`** stays the definer of `record_lock_head` and `record_insert`. It gets `INSERT` on `record_event` and `SELECT`, `INSERT` and `UPDATE` on `record_chain_head`, as grants rather than ownership. It therefore cannot disable or replace the trigger.
- **No runtime role** gets any right to `ALTER`, `DROP`, `DISABLE TRIGGER`, `CREATE OR REPLACE` or `TRUNCATE` on these objects. Only an owner, a member of the owner role, or a superuser can do those, and §6.1 removes every runtime role from that set.
- **No runtime role** has `CREATE` on any schema. That stops `search_path` shadowing; PostgreSQL 15 and later already revoke `CREATE` on `public` from `PUBLIC`, and a test pins it.
- **`session_replication_role`** can be set only by a superuser.
- **The `signing_key` table:** `SELECT` for `trust_rw`, `execution_rw`, `outcome_rw` and `record_append` (public keys only, for their own verifiers); `INSERT`, `UPDATE`, `DELETE` and `TRUNCATE` for no runtime role. An immutability trigger allows only the status changes of D5, and only from the three key functions.

### 6.1 Deviation found in migration `0001` (Architect, question c)

Today `record_event` and `record_chain_head` are owned by **`record_append`**, not by a migration role (`0001`: `ALTER TABLE record_event OWNER TO record_append; ALTER TABLE record_chain_head OWNER TO record_append;`). Every other table is owned by whatever login ran the migration, which is the superuser `postgres` in Compose. The migrating login is also granted `record_append` (`GRANT record_append TO CURRENT_USER`). Effects today:
- `record_append` is a `NOLOGIN` role with no runtime member. `execution_rw` is not a member of it, so `execution_rw` cannot disable the Record table's triggers today.
- But **the owner of the Record table is the same role whose definer functions append to it.** A verification trigger on that table would be removable by any session that can act as `record_append`.
- No named migration role exists, so the requirement "owned by the migration role" cannot be checked.

W4 transfers both tables to `noema_migrator` (D15), grants `record_append` what D16 says, and adds the pins. It is a forward-only migration; `0001` is not edited.

## 7. What this design does not fix (stated plainly)

1. **Compromise of a private key, or of the core process.** The core is one deployable (PERD §41.1, DEC-2026-10-17: one service identity at the network level). Every power's private key is in one process's memory. An attacker inside that process can sign as any power. This design defeats a **stolen database credential**, not a compromised core process. Separating keys by process needs per-power deployables or a managed key service with per-power credentials (before Phase 2).
2. **The migration role and the superuser.** Anyone who can act as `noema_migrator` or as a superuser can change the key table, the function or the trigger, or write rows directly. External anchoring (REQ-AUD-007, REC-07) makes a rewrite of history detectable afterwards; nothing makes it impossible. The word stays **tamper-evident** (D20).
3. **Outcome still verifies independently.** A receipt the database accepted was signed by `core-execution`'s key. That proves who signed it, not that the write happened as the receipt says. Outcome reads the target by key and checks the receipt's signature with `core-execution`'s public key (SoT §13.1 "Checks" row; INV-04; OUT-01). The database check does not replace it.
4. **The alert.** A refused signature is recorded where it can be, but no human is told. DEBT-02 stays open.
5. **pgsodium itself.** An extension upgrade could re-create or re-enable its event trigger (D10a); the start-up and migration guards and test 16 catch it, but an upgrade is still a reviewed change that re-runs T1 to T6. Pinning, a verified build and the spike reduce but do not remove the risk of a large, intermittently maintained extension inside the database that holds the Record (W2 §3, §6).

## 8. Outcome's key and independence (Architect, item d)

- **Signing.** Outcome signs each verdict with `core-outcome`'s key (D2), over the domain-tagged JCS of the verdict (D6).
- **Verifying.** Outcome verifies a receipt with `core-execution`'s **public** key, read from `signing_key`. It never holds Execution's private key, and Execution never holds Outcome's.
- **Why it is separate.** If Outcome and Execution shared a key, the checker could forge what it checks (BD-05, AGENT-22). With separate keys, a stolen `execution_rw` credential cannot forge a verdict: that needs Outcome's key and `outcome_rw`, and the database verifies a verdict's signature under `core-outcome` only.
- **The limit of §7.1 applies.** In the POC the separation is enforced by key files, package boundaries (an architecture-lint rule) and database roles, not by separate processes.
- **What Core Engineer 2 needs for OUT-01:**
  - the verdict domain tag;
  - the key ID format;
  - the rule that `outcome_verdict` gets the same `signed_jcs` column and trigger;
  - the verify-only interface to `core-execution`'s public key;
  - the golden vectors of §10.

## 9. Migration plan for `noema#94` and `noema#90`

Neither pull request is touched by this record; C1 executes W3 and W4 under their tasks, and the Founders merge. **`noema#94` never merges before W4 is on `main`,** because #94 opens the `SPENT → VOID` path that DEBT-01 attacks.

| Step | Task, owner | What lands | Gate to the next step |
|---|---|---|---|
| 0 | SEC-12, SR | W2 merged (docs#78). Spike T1 to T6 already passed in CI (run 41314576829, noema#106, outside `main`) | W2 merged with the agreed T6 wording |
| 1 | GOV-28, Founders | This record approved, with the PERD v1.20 text of §12 in the same docs PR (AGENT-29), OD-P-72 decided | — |
| 2 | EXE-07 (W3), C1 | Go signer and verify-only interfaces in `platform/crypto`; key registry; key loading from file; the Controller signs receipts with Ed25519 (no database change yet); golden vectors | Signing and rotation tests green; no key material in logs or traces |
| 3 | EXE-08 (W4), C1 | Custom `postgres:17.11-alpine` image (D10); the bootstrap step of D10a (`CREATE EXTENSION`, event trigger disabled, setting off) and its migration and start-up guards; the next free migration number: `noema_migrator`, `noema_sig` schema, `signing_key`, `noema_sig.verify`, the receipt trigger, `signed_jcs` on `execution_receipt`, ownership transfer of §6.1, `receipt_insert`, the revocations of D16; `schema_test.go` pins; `docs/db_schema.md` regenerated | The §10 tests that W4 owns, green in CI at its final head |
| 4 | EXE-04, C1 | `noema#94`: merge `main` in (no rebase). Its migration is renumbered to the next free number, which is allowed only because it has never merged. Its guard keeps the confirmed-refusal conditions of REQ-EXE-004. Condition (g) changes from "64 lower-case hex (HMAC shape)" to "the receipt row exists": the receipt can only exist if the trigger verified it. Its shape tests become verification tests with fixtures signed by a synthetic test key | DEBT-01 criteria (1) to (6) evidenced by SR (SEC-13); EL closes DEBT-01 |
| 5 | EXE-04, C1 | `noema#90`: merge `main` in. `Controller.completeReceipt` verifies Ed25519 (public key) instead of HMAC, as defence in depth. The `SECURITY_EVENT` rule of DEC-2026-10-28 §7 is unchanged and now also covers `NS001` | CI green at the final head; the Founders merge #94, then #90 |
| 6 | REC-08, C1 | record-event v4; a `signed_jcs` and `sig` on `record_event`; the Record trigger; every writer signs; the chain verifier checks every signature | REQ-AUD-006 acceptance; G3 |
| 7 | OUT-01, C2 | `outcome_verdict` with `signed_jcs`, `sig` and the same trigger; Outcome verifies receipts | US-06 and the verdict tests |

**Nothing is migrated:** no receipt, event or verdict exists outside tests and throwaway databases (as checked for DEC-2026-10-28 §4; to be re-checked by W4).

## 10. Test plan (C1 writes and runs them failing first; SR validates independently, SEC-13)

| # | Test | Maps to | Owner |
|---|---|---|---|
| 1 | Build pgsodium and libsodium (pinned, checksum-verified) into the 17.11 image; `CREATE EXTENSION` with no preload | T1 | C1 (spike), SR |
| 2 | RFC 8032 §7.1 known-answer vectors verify through `noema_sig.verify`; each altered byte of signature, message and key fails | T2 | C1 |
| 3 | Malleability: `S + L`, non-canonical key, small-order key, small-order `R`, all-zero signature: all refused | T3 | C1 |
| 4 | The wrapper refuses: signatures of 63, 65 and 0 bytes and non-hex; NULLs; unknown, retired, revoked and wrong-identity key IDs; a purpose the identity may not sign; a domain tag of another type; a 64-hex HMAC value under an Ed25519 key ID, and the reverse (algorithm confusion) | T4 | C1 |
| 5 | Replay: a genuine receipt inserted for another grant, tenant, attempt, idempotency key or state; a genuine event at another `seq` or chain; a verdict for another receipt: all refused | T4, DEBT-01 (3) | C1 |
| 6 | `signed_jcs` that differs from the row's document or columns; a document with duplicate member names (Go side): refused | D8 | C1 |
| 7 | As `execution_rw`, every one refused:<br>• `INSERT` and `COPY` into `execution_receipt`;<br>• `INSERT`, `UPDATE`, `DELETE` and `TRUNCATE` on `signing_key`;<br>• `ALTER`, `DROP`, `DISABLE TRIGGER` and `CREATE OR REPLACE` on the trigger and the functions;<br>• `SET ROLE noema_migrator`;<br>• `SET session_replication_role = replica`;<br>• `CREATE FUNCTION` in any schema;<br>• calling `key_register`.<br>The same list as every other runtime role. Membership of `noema_migrator` pinned empty of runtime roles | T5, D14 to D16 | C1, SR |
| 8 | **The DEBT-01 closure test:** as `execution_rw`, a well-formed forged `REJECTED_STALE_VERSION` receipt for a `SPENT` grant, by `INSERT`, by `receipt_insert` and by every function it may execute, cannot be written and the grant cannot be voided. Written first against the held code of `noema#94`, where it must fail (the forgery succeeds), then green after W4 | DEBT-01 (2), (3) | SR (failing first), C1 |
| 9 | Verification unavailable: extension dropped; library file removed; function raising: a correctly signed receipt or event is refused, no row is added and no other write of its transaction is kept; the core returns the error and logs it; no `SECURITY_EVENT` is expected | T6 (the agreed condition, D13) | C1, SR |
| 10 | Rotation (REQ-SEC-005 for these keys): during the overlap, objects under the old and the new key both insert; after retirement, the old key is refused for inserts and still verifies in the chain verifier; a third active key cannot be registered; revocation marks later objects untrusted | DEBT-01 (4), SEC-09 | C1, SR |
| 11 | Golden vectors: a new family `ed25519_signing_vectors` in `contracts/fixtures/golden_vectors.json`, computed by a synthetic, public, test-only key and checked by Go, Python and the database; labelled synthetic (AGENT-25) | D6 | C1 |
| 12 | Outcome verifies a receipt with the public key only; an architecture-lint rule that `execution` and `outcome` cannot import each other's signer | D3, §8, DEBT-01 (5) | C2, C1 |
| 13 | REC-08: a forged event by `record_insert` with any runtime credential is refused; the chain verifier checks every signature and reports a revoked key's events | REQ-AUD-006 | C1 |
| 14 | Mutation check: remove each condition of `noema_sig.verify` and of the trigger in turn; each removal is caught by a test | All | SR |
| 15 | PERD §47 budget: the verification cost per insert, measured, not assumed | §47 | C1 |
| 16 | **Event trigger stays disabled.** After bootstrap, every event trigger owned by pgsodium has `evtenabled = 'D'`, and DDL by `noema_migrator` succeeds. Re-enable `pgsodium_trg_mask_update` (as a superuser, simulating an upgrade): `db.Migrate` refuses to run and the core refuses to start, each with a distinct error. Also run after `ALTER EXTENSION pgsodium UPDATE` whenever the pinned version changes | D10a, T1 | C1, SR |

## 11. Fallback: Option C (if W2's spike fails or the Founders refuse pgsodium)

**What it is.** The database verifies nothing. A `SPENT` grant becomes `VOID` only after an **Outcome verdict** confirms the refusal from Outcome's own read of the target.

**The change to the 28 Oct transaction rule, stated plainly.** DEC-2026-10-28 D2 puts the receipt, the void, the RecoveryRequest and the outbox in **one** transaction. Option C splits it into three steps:

1. **Transaction 1 (Execution):** the signed receipt `REJECTED_STALE_VERSION`, the `RECEIPT` event and the outbox event that starts verification. The grant **stays `SPENT`**. There is no RecoveryRequest yet.
2. **Outcome (asynchronous):**
   - It verifies the receipt's Ed25519 signature with `core-execution`'s public key (Ed25519 is still used for signing, D1 to D9; only the database check is dropped).
   - It reads the target by key and confirms that the target's version token is unchanged and that no effect exists.
   - It writes a verdict `NOT_ACHIEVED`, signed with `core-outcome`'s key, that references the receipt.
3. **Transaction 2 (Execution or Trust, as the Founders choose):** `SPENT → VOID`, `GRANT_VOIDED{REJECTED_STALE_VERSION}`, the RecoveryRequest and its outbox event. The `decision_grant_guard` permits the transition only if a verdict row, written by `outcome_rw`, references this grant's single confirmed receipt with `NOT_ACHIEVED`.

**What it buys.** Forging a void now needs **two** credentials, `execution_rw` and `outcome_rw`, or the core process. The confirmation comes from an independent read of the target, not from the receipt alone.

**What it costs:**
- recovery waits for Outcome's settle window and read (US-19 timing);
- it depends on OUT-01, which is not built;
- `REJECTED_STALE_VERSION` gets a period in which the grant is `SPENT` with a refusal receipt;
- a crash between the three steps leaves the case waiting, so the sweeper must resume it (crash-point matrix, REQ-TST-008);
- the Outcome verdict enum has no value that says "verified that nothing was applied", so the guard reads `NOT_ACHIEVED` plus the receipt link, and Outcome must write `NOT_ACHIEVED` only after its read shows the version unchanged.

**What it does not meet.** REQ-AUD-006's "the database refuses an event whose signature does not verify" cannot be met without a database verifier. Under Option C, Record writers are authenticated only by the chain verifier (Go, after the fact) and by anchoring (REQ-AUD-007). The Founders must either accept that as a stated limit, with REQ-AUD-006 amended (§12.9), or keep REQ-AUD-006 open and its G3 gate failing. **This is a weaker control and must be described that way.**

## 12. Exact PERD amendment text (for PERD v1.20, applied only after approval; v1.19 is not edited)

Each item gives the v1.19 text and the text that replaces it. Items 1 to 8 are Option B. Item 9 replaces items 1 and 7 if Option C is chosen.

**12.1 REQ-AUD-006, the "Expected behaviour", "Failure behaviour", "Security" and "Tests" lines.**

> before (Expected behaviour): One signing design covers receipts (DEBT-01, Option B) and Record events. Trusted public keys sit in a table owned by the migration role; no runtime role can change it.
>
> after: One Ed25519 signing design covers execution receipts, Record events and Outcome verdicts (DEC-2026-11-01-receipt-and-record-signing). Each writing identity of §32.1 has its own key pair; a key signs only for its own identity, and Outcome's key is separate from Execution's. The signed message is a fixed domain tag (`noema/receipt/v1\n`, `noema/record-event/v1\n`, `noema/outcome-verdict/v1\n`) followed by the RFC 8785 bytes of the document without `sig` (for an event, the body that `hash` covers, including `prev_hash` and `seq`). `sig.key_id` is `<identity>.ed25519.<version>`; `sig.value` is 128 lower-case hex characters. The signed bytes are stored beside the parsed document. Trusted public keys sit in the table `signing_key`, owned by the migration role `noema_migrator`; no runtime role can change it or is a member of `noema_migrator`. A `BEFORE INSERT` trigger owned by `noema_migrator`, set `ENABLE ALWAYS`, verifies every insert into `execution_receipt`, `record_event` and `outcome_verdict` through one `SECURITY DEFINER` function that uses pgsodium's `crypto_sign_verify_detached` [OD-P-72], and checks that the signed document equals the row and, for a receipt, the spend.
>
> before (Failure behaviour): Verification unavailable means the append fails closed and the operation stops.
>
> after: A signature that does not verify, or a verification that cannot run (extension missing, library missing, function error), makes the insert fail and its transaction roll back; nothing is accepted unverified. When verification cannot run, no Record append succeeds, so no `SECURITY_EVENT` can be written: the core returns the error, logs it, and the operation stops (REQ-AUD-001, EC-E16).
>
> before (Security): Private keys never enter PostgreSQL. Limit: a compromise of the core process itself exposes its keys; this control defeats a stolen database credential.
>
> after: Private keys never enter PostgreSQL, a log, a trace or the model service; each is a separate file-mounted secret read only by its own power's package. Two keys per identity may be active during rotation; retired keys still verify history; a revoked key's objects from its `compromised_since` time are reported as untrusted. Limits: a compromise of the core process exposes every power's keys, because the core is one deployable; anyone acting as `noema_migrator` or a superuser can change the keys, the function or the trigger, which external anchoring (REQ-AUD-007) detects afterwards. This control defeats a stolen database credential. The Record is tamper-evident, never tamper-proof.
>
> before (Tests): Failing-first forgery tests by INSERT and by every function; key rotation with two active keys.
>
> after: Failing-first forgery tests by INSERT, COPY and every function, for every runtime role; replay against another grant, tenant, attempt, idempotency key, state, sequence or chain; RFC 8032 and malleability vectors; verification unavailable; the privilege tests of DEC-2026-11-01-receipt-and-record-signing §10 item 7; key rotation with two active keys, retirement and revocation.

**12.2 REQ-SEC-005, Requirement, first bullet.**

> before: There is one HMAC key for grants and confirmation requests, held in the secrets manager.
>
> after: There is one HMAC key for grants and confirmation requests, held in the secrets manager. Execution receipts, Record events and Outcome verdicts are signed with per-identity Ed25519 keys under REQ-AUD-006; the same rotation rule applies to them.

And its acceptance criterion, appended:

> after (added): A rotation test SHALL show, for each Ed25519 identity, that objects under the old and the new key are accepted during the overlap and that the old key is refused for new objects after retirement.

**12.3 REQ-EXE-004, Expected behaviour, the sentence beginning "Two limits of this check".**

> before: … and the database does not verify the receipt's HMAC (the keys are not in the database), it relies on the signed document being inserted only by Execution.
>
> after: … and the receipt exists only if the database verified its Ed25519 signature under `core-execution`'s active key and its signed document equals the row and the spend (REQ-AUD-006); the guard's signature condition is that the receipt row exists.

**12.4 §32.1, after "The hash is computed as:".**

> after (added): Every event of schema major 4 carries `sig` (`key_id`, `value`): an Ed25519 signature by the key of its `written_by` identity over `noema/record-event/v1\n` followed by `JCS(event without hash and without sig)`. `sig` is not part of the hashed body. `record-event.v4.json`.

**12.5 §38.2, rows.**

> `execution_receipt`, before: `receipt_id`, `json`, `execution_state`, `raw_status`, `sig` | `decision_grant` | Insert | Immutable | Execution | Permanent
>
> after: `receipt_id`, `json`, `signed_jcs`, `execution_state`, `raw_status`, `sig` (Ed25519, REQ-AUD-006) | `decision_grant` | Insert, through `receipt_insert` only; a trigger owned by `noema_migrator` verifies every insert | Immutable | Execution (owner `noema_migrator`) | Permanent
>
> `record_event`, before: … | Insert | **INSERT-only role** | Every power | Permanent
>
> after: … plus `signed_jcs`, `sig` | Insert, through `record_insert` only; a trigger owned by `noema_migrator` verifies every insert | **INSERT-only role** | Every power (owner `noema_migrator`; `record_append` holds grants, not ownership) | Permanent
>
> added row: `signing_key` | REQ-AUD-006 | `key_id`, `identity`, `version`, `algorithm` (`ED25519`), `public_key` (32 bytes), `purposes`, `status` (`ACTIVE`, `RETIRED`, `REVOKED`), `activated_at`, `retired_at`, `compromised_since` | — | Insert and status change through `key_register`, `key_retire`, `key_revoke` only (owner `noema_migrator`) | Identity columns immutable; at most two `ACTIVE` per identity | Control plane | Permanent

**12.6 REQ-DATA-001, Security line, appended.**

> after (added): A separate `NOLOGIN` migration role, `noema_migrator`, owns the signed tables, the key table, the verification function and its triggers. No runtime role is a member of it, directly or through another role, and none is `SUPERUSER`, `CREATEROLE`, `CREATEDB`, `REPLICATION` or `BYPASSRLS` or has `CREATE` on any schema; a test pins each.

**12.7 §41.1, the "Holds" column.**

> `core-execution`, before: Grant verification key; Tushe write credential (non-monetary)
>
> after: Grant verification key; Ed25519 receipt and event signing key (`core-execution`); Tushe write credential (non-monetary)
>
> `core-outcome`, before: Tushe read credential
>
> after: Tushe read credential; Ed25519 verdict and event signing key (`core-outcome`), separate from Execution's; `core-execution`'s public key
>
> `core-trust`, before: Grant HMAC key (read from the secrets manager at start-up and kept in memory)
>
> after: Grant HMAC key (read from the secrets manager at start-up and kept in memory); Ed25519 event signing key (`core-trust`)
>
> `admin`, before: Policy publish; pack load; kill switch; key rotation
>
> after: Policy publish; pack load; kill switch; key rotation; Ed25519 event signing key (`admin`), held by the operator tooling

**12.8 §36.1, a row added after "HMAC-SHA-256 grants and confirmations".**

> after (added): | **Ed25519 receipts, events and verdicts; one key per writing identity; two during rotation; verified in PostgreSQL by pgsodium v3.1.11 (pinned commit, built into the `postgres:17.11-alpine` image; its event trigger disabled at bootstrap)** | A stolen database credential cannot forge a receipt, event or verdict | INV-03, INV-04, REQ-AUD-006 | Verification only in application code (Option C); `pg_ed25519` (accepts malleable signatures) | POC-essential [OD-P-72] | §47.4 |

**12.9 Option C only: replaces 12.1 and 12.3, and amends REQ-EXE-004 and REQ-AUD-006 as follows.**

> REQ-EXE-004, Expected behaviour, first sentence, after (Option C): When the target refuses the expected version (409 or 412), one database transaction writes the signed receipt `REJECTED_STALE_VERSION`, appends `RECEIPT` and enqueues the verification outbox event; the grant stays SPENT. The grant moves from SPENT to VOID, `GRANT_VOIDED{REJECTED_STALE_VERSION}` is appended and the RecoveryRequest is added, in a second transaction, only after Outcome has verified the receipt's signature and written a verdict `NOT_ACHIEVED` for it from its own read of the target, showing the version unchanged. This replaces the single transaction of DEC-2026-10-28 D2.
>
> REQ-AUD-006, Acceptance criteria, after (Option C): A caller holding any database credential but no signing key SHALL be unable to append an event that the chain verifier accepts; the chain verifier SHALL check every signature. The database does not verify signatures (no extension is approved); undetected rewriting is prevented only together with REQ-AUD-007.

## 13. SoT §52 questions

1. **Does it serve the POC, and not the platform?** Yes. It closes a Tier 0 defect (DEBT-01) counted by G3, and REQ-AUD-006, a P0 requirement of the POC.
2. **What is the simplest version that works?** The standard library signs. One extension function verifies, behind one wrapper with one trigger per signed table. There is no new service and no key service in the POC.
3. **Is it safe?** It is fail-closed on every path (§5, D13). It adds a dependency inside the database, which is stated as a risk (§7.5, OD-P-72).
4. **Can the Record prove it later?** Yes. Every event carries its signature, and the chain verifier checks it.
5. **Is it deterministic?** Yes. Ed25519 signatures are deterministic, and the signed bytes are JCS.

**Unsafe autonomy surface:** it **decreases**. A database credential alone can no longer create a receipt, an event or a verdict, so it can no longer void a grant.

## 14. Record fields (decisions README template)

- Status: Proposed (see the top of this record)
- Date: 1 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: §3 to §11 (D1 to D16, the migration plan, the test plan, the Option C fallback)
- Rationale and evidence: §1, §2, §6.1, §7; the W2 evaluation
- Affected requirement IDs / SoT sections: REQ-AUD-006, REQ-AUD-005, REQ-AUD-001, REQ-AUD-007, REQ-SEC-005, REQ-EXE-004, REQ-DATA-001, REQ-VER-001; INV-03, INV-04, INV-11, INV-29; BD-05; AGENT-14, AGENT-15, AGENT-22; SoT §13.1, §43.3, §43.6, §47.4; PERD §32.1, §36.1, §38.2, §41.1
- Migration notes: §9 (code and database), D9 (contracts), §12 (PERD v1.20)
- Supersedes: none. Amends DEC-2026-10-28 D2 only if Option C (§11) is chosen
