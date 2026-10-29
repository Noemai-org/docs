# DEC-2026-10-29 · Database-side Ed25519 verification for execution receipts

| Field | Value |
|---|---|
| **Status** | Founder-selected direction; implementation and security acceptance pending |
| **Date** | 29 October 2026 |
| **Owner** | EL — design and implementation; SR — independent security validation |
| **Closes** | DEBT-01 only after all six closure criteria and evidence are accepted |
| **Amends** | PERD v1.19 proposal; no SoT text change |
| **Authority order applied** | SoT → decision records → PERD → plan |

## 1. Decision

Proceed with **Option B: PostgreSQL verifies Ed25519 signatures on execution receipts before a receipt row can be inserted**. The signature's private key remains outside PostgreSQL and outside the database writer's reach. PostgreSQL receives only the trusted public verification keys.

The existing HMAC scheme for decision grants and confirmation requests remains unchanged. Receipt signing is a separate purpose and key lifecycle.

This records the Founder-selected direction. It does **not** assert that the implementation is built, deployed, or tested, and does not close DEBT-01.

## 2. Security boundary

The 29 October PostgreSQL test established that `execution_rw` can insert a forged but well-shaped `REJECTED_STALE_VERSION` receipt for a spent grant with no receipt and then void the grant. The database currently checks signature shape and row consistency, not cryptographic validity.

The target state is:

1. Execution signs the canonical receipt payload with Ed25519 using a private key held outside PostgreSQL.
2. The database verifies the signature using a trusted public key selected by a closed, allowlisted key ID.
3. The exact bytes that were signed are persisted, and the database independently verifies that the JSON stored in the receipt matches those signed bytes. No re-serialization ambiguity is permitted.
4. The receipt INSERT trigger rejects unknown keys, malformed payloads, mismatched signed payload/JSON/columns, invalid signatures, and any cryptographic verification error. Fail closed.
5. The role `execution_rw` cannot add or alter public keys, disable the verifier, replace its function, or bypass the trigger. Key registry writes and migration privileges are unavailable to runtime roles.
6. The `SPENT → VOID` transition remains possible only for a confirmed stale-version refusal with a valid, database-verified receipt. No other transition is relaxed.

## 3. Cryptographic implementation and deployment requirements

Use a maintained PostgreSQL cryptographic extension that exposes Ed25519 verification, with **pgsodium as the initial candidate**. Before implementation is accepted, EL must pin the exact extension release and source/image digests, confirm its PostgreSQL 17 compatibility, verify the exact SQL function signature and argument order from that release, review licence and maintenance status, and run the extension's own signature test vectors. Do not use an unpinned `latest` tag or assume an API from a different release.

The PostgreSQL image must be reproducibly built with the extension installed. Production/local and CI/test databases must use that same pinned image; the existing test helper's system-installed PostgreSQL path must not silently run without the extension. Startup/migration must fail if the required extension or verifier function is absent.

The public-key registry must support controlled rotation: active and explicitly overlap-approved keys can verify receipts; unknown keys fail; retired keys are rejected after the defined overlap window. Public-key registry changes are admin/migration-only and audited. The database must never contain receipt signing private keys.

The signature input format, byte encoding, key-ID rules, canonical JSON rules, and public-key encoding must be specified in the code contract and covered by fixed cross-language test vectors before the migration is approved.

## 4. Required failing-first evidence

- Direct INSERT as `execution_rw` with a well-formed forged signature fails and leaves no receipt.
- A forged stale-version receipt cannot change a spent grant to VOID, whether attempted by direct INSERT or any exposed function.
- A valid signed receipt succeeds; one-byte payload mutation, altered JSON, altered row columns, wrong tenant/grant/attempt/idempotency key, unknown key ID, malformed key/signature, and invalid signature all fail closed.
- The database verifies the exact stored signed bytes and checks the stored JSON equals the parsed signed payload.
- The role-permission matrix proves `execution_rw` cannot write the public-key registry, replace verifier functions, disable triggers, or acquire migration/admin privileges.
- Rotation test proves old/new key overlap, signing with the newest key, and rejection after retirement.
- Existing grant lifecycle regression tests continue to prove only the confirmed `SPENT → VOID` transition is permitted.
- Outcome independently verifies receipt signatures and reconstructs its verdict from its own authoritative reads (SoT §13.1; OUT-01).
- CI evidence is linked from the final PR head. Local test claims alone do not close the risk.

## 5. Ownership and dates

- **EL:** deliver the reviewed design, exact extension/version/image pin, PERD amendment and implementation PR by **Wednesday, 4 November 2026**.
- **SR:** independently review the threat boundary, key lifecycle, failing-first tests and all six DEBT-01 closure criteria; deliver evidence for **G3 review, Friday, 6 November 2026**.
- The Founder must explicitly record whether the observed invalid-grant-void behavior touches any Tier 0 gate or invariant (REQ-OPS-004). Do not mark this assessment as passed by inference.

## 6. Relationship to DEBT-01

DEBT-01 remains open until all six criteria in [the debt register](../poc/execution/debt.md) are evidenced. The decision to pursue Option B is not closure evidence. The database bypass is not considered fixed by Controller-side verification alone, by signature-shape checks, or by an Outcome-only check.

## 7. Rollback and migration discipline

Use forward-only migrations. Do not edit an already-merged migration. Do not merge the current EXE-04 or grant-void migration PRs as a substitute for this work. The receipt-verification migration must be reviewed together with its tests, database image, deployment configuration, PERD update, and this record. If the extension cannot be built and tested reproducibly, stop and return to the Founder with the exact blocker rather than weakening the database verification requirement.
