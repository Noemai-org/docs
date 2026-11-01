# W2: PostgreSQL Ed25519 verification extensions, evaluation (SEC-12)

Date: 2026-10-31
Task: SEC-12 (owner SR; human owner: a founder). Requirement: REQ-AUD-006. Feeds: GOV-28 (W1), EXE-08 (W4), REC-08, SEC-13.
Status: **Recommendation for founder approval under AGENT-14. Nothing is adopted.** This is a docs-only evaluation: nothing was installed, built or run, and no file in `noema` was touched.
Non-normative: it decides nothing. The SoT, the PERD and the decision records govern.

## 1. Question and method

Which PostgreSQL extension, if any, can verify an Ed25519 signature inside the database, so that a caller holding `execution_rw` (or any other database credential) cannot insert a forged receipt or Record event? Needed for DEBT-01 Option B and for REQ-AUD-006 (receipts and Record events share one design, DEC-2026-10-31-proof-depth-and-completeness D18).

Method: candidates found by web search on 31 Oct 2026; every fact below was then read from the project's own repository (cloned or fetched raw) at the commit named. Facts I could not read from a primary source are marked **NOT VERIFIED**. Nothing was executed: "it works" is not claimed for any candidate, and a build-and-test spike is listed as a follow-up in section 7.

Candidates found: `pgsodium`, `pg_ed25519`, `pg-crypto` (RustedBytes), `pgjwt`. PostgreSQL's own `pgcrypto` has no Ed25519 function that I found (**NOT VERIFIED** beyond a search; the `pgcrypto` documentation should be checked if anyone doubts this). An untrusted procedural language (PL/Python and similar) is not an extension that verifies; it would put a language runtime and a Python crypto library inside the database, and is not evaluated further.

## 2. Summary table

| | pgsodium | pg_ed25519 | pg-crypto (RustedBytes) | pgjwt |
|---|---|---|---|---|
| Pinned version | v3.1.11, commit `a8b8a2739bab1f7a07445b1c911e2bd1abf67784` | 0.2, commit `203944dbd3444257490eb30d2f6363e391a23a6b` | 0.1.0, commit `a07210ac1f98e5a722843c7389afdd0cd26ebe3c` | 0.1.3 (not pinned further) |
| Licence | ISC-style permissive (LICENSE, "Copyright (c) 2020 Michel Pelletier and Contributors") | MIT | MIT | MIT (Cargo.toml) |
| Last release / commit | tag v3.1.11, 10 Jun 2026 (before it, v3.1.9 on 10 Nov 2023) | 1 Aug 2019 | one tag v0.1.0; repo started 31 Aug 2026 | last commit 30 May 2026 |
| Maintainers | 3 committers in history; one wrote 243 commits | 1 | 1 | 1 |
| Crypto underneath | libsodium (CI builds 1.0.22) | vendored copy of the 2015 `orlp/ed25519` reference code | `dryoc` (pure Rust) | pgrx Rust, JWT-specific |
| Rejects non-canonical `S` | yes (via libsodium) | **partly** (see 4.2) | NOT VERIFIED | not evaluated |
| Rejects small-order keys and `R` | yes (via libsodium) | **no** | NOT VERIFIED | not evaluated |
| PostgreSQL 16 / 17 | README: 14+; CI builds from source for any `version` | README: 9.4+ (2019; never built against 16 or 17 by the project) | pgrx features pg14 to pg18 | targets 18, 13 to 17 by flag |
| Fit | usable | reject | not yet | wrong shape (JWT) |

## 3. Candidate: pgsodium (recommended, conditional)

Sources: <https://github.com/michelp/pgsodium>, `src/sign.c`, `pgsodium.control`, `latest-changes.md`, `Dockerfile`, git history.

**Function.** `pgsodium.crypto_sign_verify_detached(sig bytea, message bytea, key bytea) returns boolean` (`src/sign.c`). It raises an error on a NULL argument or a public key whose length is not 32 bytes, and returns `crypto_sign_verify_detached(...) == 0`. It does not check the signature length itself; libsodium reads 64 bytes from `sig`. **A wrapper must reject any signature that is not exactly 64 bytes before calling it.** I did not confirm what libsodium does with a shorter `bytea`; the wrapper makes the question moot.

**Cryptography.** libsodium's `_crypto_sign_ed25519_verify_detached` (`jedisct1/libsodium`, `src/libsodium/crypto_sign/ed25519/ref10/open.c`, master) in its default build (not `ED25519_COMPAT`):
- rejects a non-canonical `S` (`sc25519_is_canonical`), so a signature cannot be malleated by adding the group order;
- rejects a non-canonical public key (`ge25519_is_canonical`);
- rejects a small-order public key and a small-order `R`;
- ends with a small-order check on the verification equation's result rather than a plain byte compare.

I did not verify constant-time behaviour. For verification, the inputs are public (signature, message, public key), so constant time is not a confidentiality requirement here; the property that matters is rejecting malleable and non-canonical encodings, which the code above does. Whether the libsodium version that a given distribution installs has these checks must be pinned and tested (section 7, test T3); the pgsodium README requires libsodium 1.0.18 or later, and the project's CI builds 1.0.22.

**Maintenance.** Active, with a gap. v3.1.9 (10 Nov 2023), then v3.1.10 and v3.1.11 (10 Jun 2026) after commits on 6 and 7 Oct 2025 that include "Fix sql injection vulnerability in pgsodium.mask_role (#115)" and "Fix/security audit improvements (#119)". So there was a roughly two-year release gap in which the project carried a SQL-injection defect in a function we would not use. Open issues: 28 (titles not read; **NOT VERIFIED** whether any is a security issue). Supabase's documentation says Supabase does not recommend new use of pgsodium and expects a deprecation cycle; that statement is about Supabase's platform and its Transparent Column Encryption and Server Key Management features, which we would not use. Upstream carries no deprecation or archive notice at the commit above. This is a real project risk and is in the risk list (section 6).

**Supply chain.** Source on GitHub; the upstream `Dockerfile` downloads PostgreSQL and libsodium tarballs with `curl` and **no checksum or signature check**, so we must not reuse that Dockerfile. Release tags are not shown to be signed (**NOT VERIFIED**; no signature material was found in the repository). A tag since June 2026 triggers an automatic GitHub Release. Distribution for us would be a build from the pinned commit inside our own image (section 5); a PGDG or Debian package of pgsodium for PostgreSQL 16 or 17 was **NOT VERIFIED** (the PGDG index was not reachable from this session).

**PostgreSQL version.** README: "As of version 3.0.0 pgsodium requires PostgreSQL 14+." **Our Compose file runs `postgres:17.11-alpine` (digest-pinned), not PostgreSQL 16** (`noema/deploy/compose/docker-compose.yml:58`). The task text and the question asked about 16. The compatibility that matters is 17 on Alpine (musl). Neither the PostgreSQL 17 nor the Alpine build was tested (**NOT VERIFIED**). This must be resolved with the Engineering Lead (section 6, item 1).

**Footprint.** The extension installs much more than we need: roles (`pgsodium_keyiduser`, `pgsodium_keymaker`, `pgsodium_keyholder`), the key tables, event triggers, and Transparent Column Encryption. `pgsodium.control` has no `trusted` or `superuser` line, so `CREATE EXTENSION` needs a superuser. Server-managed keys are optional and it can run without `shared_preload_libraries` (README), which is the mode we want: no server key, no preload, verify function only. The cost is a large surface of unused SQL objects in the database that holds the Record.

**When unavailable or failing to load.** (a) Image built without the extension: `CREATE EXTENSION` fails and the migration fails; nothing is half-applied if the migration is transactional. (b) Extension missing at run time (wrong image, dropped extension): a trigger or function that calls it raises an error and the `INSERT` fails. That is fail-closed and is the behaviour we want, and the test for it is T6 (section 7). (c) Bad input: a NULL argument or a wrong-length public key raises an error, also fail-closed. The fail-open risk is in the wrapper, not the extension: a wrapper that catches the error and treats it as "not verified, accept for later review" would fail open. The wrapper must not contain an exception block that swallows these errors.

**Trust model.** The extension does not stop us building the required arrangement; it also does not provide it. We would have to build, in migrations run by a migration role that `execution_rw` is not a member of:
1. a trusted-key table (`key_id`, `power`, `public_key bytea`, `valid_from`, `valid_to`, `revoked_at`), owned by the migration role, with `INSERT`, `UPDATE`, `DELETE` and `TRUNCATE` granted to no runtime role and an immutability trigger as in the existing contract tables;
2. a verifier function owned by the migration role, `SECURITY DEFINER`, with `SET search_path = pg_catalog, pg_temp` and a schema-qualified call to `pgsodium.crypto_sign_verify_detached`, that checks length, looks the key up by `key_id` and the `written_by` identity, checks it is active at the event time, and fails on any doubt;
3. a `BEFORE INSERT` trigger on `execution_receipt` and on the Record table calling it, owned by the migration role, which `execution_rw` cannot `ALTER`, `DROP` or disable (`ALTER TABLE ... DISABLE TRIGGER` needs table ownership, so the table owner must be the migration role as well);
4. `execution_rw` has `EXECUTE` on neither the trigger function nor `pgsodium` objects beyond what the trigger needs (the trigger runs the definer's rights).

The residual path is any role that can become the migration role or a superuser. That is outside what an extension can address and must be stated in the W1 design. A control that restricts writes (revoking `INSERT`) is **not** the same as a control that authenticates a receipt; W4 needs both, and each needs its own test.

## 4. Other candidates

### 4.1 pg-crypto (RustedBytes), not yet
Source: <https://github.com/RustedBytes/pg-crypto> at `a07210a`. Exposes `ed25519_verify(data, signature, public_key) returns boolean` (`src/modern.rs`), built on `dryoc` 1.0 with pgrx `=0.19.2`, `superuser = false` in the control file, `relocatable = true`. Reasons not to choose it now: one author, first commit 31 Aug 2026, version 0.1.0, no history of use. The function builds the message by concatenating signature and data and calling `dryoc`'s signed-message verification; whether `dryoc` rejects non-canonical `S` and small-order points is **NOT VERIFIED** (I did not read `dryoc`). Revisit only if pgsodium is refused and after reading `dryoc`'s verifier.

### 4.2 pg_ed25519, rejected
Source: <https://gitlab.com/dwagin/pg_ed25519> at `203944d`. MIT, version 0.2, one maintainer, last commit 1 Aug 2019 (15 commits, one tag, no later activity). It vendors the 2015 `orlp/ed25519` code (`src/ed25519/verify.c`). Its verifier:
- checks only `signature[63] & 224`, which rejects `S` at or above 2^253 but accepts `S` in the range from the group order up to 2^253: **malleable signatures verify**;
- does not check that the public key is canonical, nor reject small-order keys or small-order `R`;
- needs no further analysis to disqualify it for authenticating receipts that a later verifier must treat as unique.

Also unmaintained for seven years and never built by its author against PostgreSQL 16 or 17. The SQL file and control file could not be fetched (GitLab rate limit), so its NULL handling is **NOT VERIFIED**; it is moot given the above.

### 4.3 pgjwt, not a fit
Source: <https://github.com/vishvish/pgjwt>. A JWT library; verifying a JWT means parsing and trusting a header and encoding that we do not want in a canonical-bytes design (JCS over the event, REQ-AUD-006). I did not inspect its Ed25519 path. Excluded on fit.

## 5. Recommendation

**Recommend pgsodium v3.1.11, pinned by commit and built into our own PostgreSQL image, using only `crypto_sign_verify_detached` behind a migration-owned wrapper, conditional on the six checks in section 7 passing in a spike before GOV-28 is approved.** It is the only candidate whose verifier I could read and that rejects the encodings we care about (non-canonical `S`, non-canonical and small-order keys, small-order `R`), and it has activity in 2026.

It is a weak recommendation: the surface is large, the maintenance history has a two-year gap, a vendor warns about it, the upstream Dockerfile does not verify its downloads, and the PostgreSQL major in Compose is not the one the task assumed. If the spike or the founders reject it, the answer is **"none viable"**, which triggers Option C.

**Option C (the fallback).** The void waits for an Outcome verdict (DEBT-01 text). Under Option C the database does not verify signatures, so REQ-AUD-006's "the database refuses an event that does not verify" cannot be met by it. The founders should decide whether Option C closes DEBT-01 for receipts only and leaves Record-writer authentication to the verifier plus anchoring (REQ-AUD-007), and record that as a limit. I am not recommending Option C unless the spike fails; it is the safer choice if the founders will not take a new dependency, but it is a weaker control and must be described that way.

## 6. Escalation (charter section 6 format)

**Decision required (AGENT-14: new dependency; also item 3 and item 6 of section 6: a security boundary and a new dependency).** Adopt pgsodium for in-database Ed25519 verification, or fall back to Option C.

**Problem.** DEBT-01 stays open until a receipt reaches `execution_receipt` only through a verifier that holds a public key and cannot sign (closure criterion 2). A database-side verifier needs an extension; the only candidate I can recommend is a large, intermittently released extension that this evaluation has not run.

**Options.**

| | A. Adopt pgsodium v3.1.11 (recommended, conditional on the spike) | B. Adopt `pg-crypto` | C. Option C, no extension |
|---|---|---|---|
| Effort | Medium: custom image with a verified build, wrapper, key table, trigger, tests | Medium plus reading `dryoc` | Low to medium |
| Risk | Large unused surface; maintenance gap; unverified on PostgreSQL 17 and Alpine | Single author, three months old; canonical checks unread | Weaker: no in-database authentication; REQ-AUD-006 not met as written |
| Impact | Receipts and Record events share one verifier (D18) | Same | Receipts handled by the verdict path; Record writers rely on anchoring |
| Maintenance | We own a pinned build and its updates | Same, with a less-proven project | Least |

**Recommendation.** A, conditional. Approve a time-boxed spike (one day, owner C1 with SR reviewing, outside `noema` `main`) that runs checks T1 to T6 below. If any of T1, T2, T3, T4 or T6 fails, treat the answer as "none viable" and choose C.

**Question for the founders.** (1) May we add pgsodium, built from a pinned commit into a custom PostgreSQL image, as an [OPEN] AGENT-14 entry? (2) Is the Compose database PostgreSQL 17.11 on Alpine intended (the task text said 16)? If you want 16 or Debian, say so now, because it changes the build.

**What I need from the Engineering Lead before Wed 4 Nov (GOV-28):** the intended PostgreSQL major and base image; whether `execution_rw` can ever be a member of the migration role; and the Record table's owner.

**Risks to register if A is approved** (for `debt.md` or the open-decisions register; I have not edited either): upstream maintenance gap; Supabase deprecation signal; large unused extension surface; custom image build and its supply-chain controls; an unreadable default-privilege change on upgrade.

## 7. Spike checks to run before adoption (failing-first where a test is possible)

| ID | Check | Pass means |
|---|---|---|
| T1 | Build pgsodium v3.1.11 and libsodium (pinned version, checksum verified) into the image on the Compose base, then `CREATE EXTENSION pgsodium` as a superuser | Extension loads on the chosen PostgreSQL major, with no `shared_preload_libraries` entry |
| T2 | Known-answer vectors: RFC 8032 section 7.1 vectors verify | True for valid; false for each altered byte of signature, message and key |
| T3 | Malleability vectors: signature with `S + L`; non-canonical public key; small-order key; small-order `R`; all-zero signature | Each returns false (or raises), through the wrapper |
| T4 | Wrapper: signature of 63, 65 and 0 bytes; NULL signature, message and key; unknown, revoked, not-yet-valid and expired `key_id`; replay of a valid receipt for another grant, tenant, attempt or state | Every case is refused, with no exception block that converts an error into acceptance |
| T5 | Privilege: as `execution_rw`, try to `INSERT`/`UPDATE`/`DELETE`/`TRUNCATE` the key table, `ALTER` or `DROP` the trigger or function, `DISABLE TRIGGER`, `SET ROLE` to the migration role, `CREATE FUNCTION` that shadows the verifier through `search_path` | All refused. The forged receipt of DEBT-01 is refused, by `INSERT` and by any function |
| T6 | Extension unavailable: start the database with the extension absent, and with the library file missing | Inserts fail closed; nothing is accepted unverified; the failure is a `SECURITY_EVENT` rather than silence (links to DEBT-02) |

T1 to T6 are inputs to SEC-13. I will write them as failing-first tests when C1's EXE-07/EXE-08 branch exists, and keep the W2 spike separate from `noema#94` and `noema#90`.

## 8. Not covered, and why

- **Key custody** (where the private key lives, rotation, revocation procedure): W1/GOV-28 and SEC-09. The extension holds only public keys.
- **Signing inside a compromised core process:** an Ed25519 key in the core's memory is exposed by a compromise of that process. D18 states this limit; authentication defeats a stolen database credential, not a compromised core.
- **Record events and anchoring:** verification of events (REC-08) uses the same function. The chain-head anchor store is SEC-14, evaluated separately.
- **Performance** against the PERD §47 budget was not measured. Verification runs once per insert on the receipt and Record paths; a measurement belongs in the spike.

## 9. Sources read (31 Oct 2026)

- pgsodium: <https://github.com/michelp/pgsodium>, tag v3.1.11, commit `a8b8a27`; files `src/sign.c`, `pgsodium.control`, `Dockerfile`, `META.json`, `README.md`, `extension/`.
- libsodium: <https://github.com/jedisct1/libsodium>, `src/libsodium/crypto_sign/ed25519/ref10/open.c` (master on 31 Oct 2026; the exact commit was not recorded, so pin one when T3 is written).
- pg_ed25519: <https://gitlab.com/dwagin/pg_ed25519>, commit `203944d`; `src/ed25519/verify.c`, `src/pg_ed25519.c`, `Makefile`, `README.md`.
- pg-crypto: <https://github.com/RustedBytes/pg-crypto>, commit `a07210a`; `src/modern.rs`, `pg_crypto.control`, `Cargo.toml`, `docs/API.md`.
- pgjwt: <https://github.com/vishvish/pgjwt>, README and Cargo.toml only.
- Supabase statement on pgsodium: <https://supabase.com/docs/guides/database/extensions/pgsodium>.
- Compose database image: `noema/deploy/compose/docker-compose.yml` at `34f6a8b`.
- Authority: `docs/poc/execution/debt.md` (DEBT-01), DEC-2026-10-31-proof-depth-and-completeness (D18), plan v1.10 tasks SEC-12, GOV-28, EXE-08, SEC-13, REC-08.

## 10. Addendum, 2026-11-01: what the spike found

Architect decisions of 1 Nov 2026: pgsodium is approved on condition that checks T1 to T6 all pass in CI; if any fails the answer is Option C. The spike runs in `noema` under `deploy/spike/pgsodium/` (workflow `pgsodium-spike`), as test infrastructure only. The target is **PostgreSQL 17.11 on Alpine**, the major Compose runs today (the "16" in the task text was an error). **No base change was needed:** libsodium 1.0.22 and pgsodium v3.1.11 build on `postgres:17.11-alpine` from pinned sources (libsodium by SHA-256, with its minisign signature checked against the project's published key; pgsodium by full commit id, compared after checkout).

**Correction to section 3 and section 5.** The evaluation said pgsodium runs without `shared_preload_libraries` and that this is the mode we want. That is true for calling the function and false for DDL. The first CI run failed in setup with `unrecognized configuration parameter "pgsodium.enable_event_trigger"`: the event trigger `pgsodium_trg_mask_update` calls `current_setting('pgsodium.enable_event_trigger')` with no default, and `src/pgsodium.c` defines that setting only when the library is preloaded. So with the extension installed and no preload, **every DDL command that fires the trigger fails, including the `ALTER TABLE` of a forward-only migration.** Preloading is not a way out: it runs a root-key script at server start (server key management, which we do not want). The spike's answer is to disable the event trigger (`ALTER EVENT TRIGGER pgsodium_trg_mask_update DISABLE`, superuser, once, at bootstrap) and set `pgsodium.enable_event_trigger = 'off'` at database level; we do not use Transparent Column Encryption. A check (T1) proves DDL by the migration role works afterwards. This adds one bootstrap step that W4 must carry and a risk to register: an extension upgrade could re-enable the trigger. The check is green in CI (below).

**Two harness expectations were wrong, not pgsodium** (corrected in `6953266`): the `BEFORE INSERT` trigger runs before the `NOT NULL` check, so a NULL signature is refused by the wrapper with a different message; and a `GRANT` by a non-owner only warns and grants nothing, so that check now asserts the privilege itself. Neither correction weakens a check.

**Result.** 58 of 58 checks pass at head `4206c77`: [run 41314576829](https://github.com/Noemai-org/noema/actions/runs/41314576829), carried by [noema#106](https://github.com/Noemai-org/noema/pull/106). T1 (loads on 17.11 Alpine with no preload, DDL works), T2 (RFC 8032 vectors and altered inputs), T3 (`S + L`, small-order and non-canonical keys, small-order `R`, all-zero signature: all refused, called directly and through the wrapper), T4 (wrapper and trigger: lengths, NULLs, replay across grant, tenant, attempt and state, revoked, not-yet-valid, expired and unknown keys, signed by another key, forged well-formed), T5 (authentication and restriction tested separately, including `pg_temp` shadowing and a superuser in `session_replication_role = replica`) and T6 (library missing, extension dropped: a valid receipt is refused and no row is added) all pass. By the Architect's condition the answer is therefore **pgsodium, not Option C**, subject to W4 and to founder approval under AGENT-14.

**What this does not show.** It is a spike on synthetic data in a throwaway container: nothing here is in `main`, and nothing is adopted. T6 shows the insert fails closed, not that anyone is alerted (DEBT-02, W4). Performance, extension upgrades, and the real canonical bytes (GOV-28) are untested. The spike is test infrastructure and must not be read as DEBT-01 evidence; the closure evidence is SEC-13's, after W4. The `S + L` vector also shows why `pg_ed25519` was rejected only on code reading: I did not run it.
