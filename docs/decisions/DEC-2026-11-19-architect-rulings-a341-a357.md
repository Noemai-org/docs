# DEC-2026-11-19 · Architect rulings A341 to A357 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 19 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 19 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Seventeen rulings, A341 to A357 (§1). |
| **Closes** | The confirmation-lane conflicts (A341), the Writes, Ownership and Policies and Clocks questions (A342, A344, A345), noema#743's clauses (A343), the escalation set (A346), the error-text sweep (A347), the 40001 lock (A348), the regression-link rule (A349), the small adapter rulings (A350), SSE (A351), docs#206 and docs#209 (A352), noema#716 (A353), stack readiness (A354), BO's package (A355), the bench settings (A356) and process (A357). |
| **Supersedes** | **A346 corrects A335.** **A348 amends A339.** **A352 settles** the open option of `DEC-2026-11-18-architect-rulings-a329-a340` §2 (docs#206: option (b)). Otherwise per ruling, in §1. |
| **Amends** | The PERD, as a Proposed draft (v1.26, §2); the debt register (DEBT-52, DEBT-53); the migration ledger on noema#183 (0033); the G0-N checklist. Nothing in the SoT or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 19 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A341 to A357
- Decision: §1
- Rationale and evidence: the Architect's message of 19 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-12, INV-19, INV-25, INV-26; AGENT-13, AGENT-15, AGENT-16, AGENT-27, AGENT-29; REQ-TRU-002, REQ-TRU-005, REQ-TRU-009, REQ-CTX-007, REQ-EXE-008; PERD §23.1, §23.3, §28.2; SoT §43.2a
- Migration notes: migration 0033 (C2, `admitted_intent.logical_resolution_epoch`); `may_write` is a pack-schema minor; `message-request.v1` is additive (AGENT-15)
- Supersedes: see the Supersedes row above

## 1. The rulings, as given

### A341 (interim): Confirmation lane conflicts (EL and C1).

- **Who opens the request:** `Status` is a pure read. It returns `NewRequest` when none is open, and the Recorder persists it in the same transaction as the CONFIRM decision (record first, EC-E16). noema#757 is right and #750 conforms to it. #757 merges first.
- **Who records `CONFIRMATION_RECEIVED`:** one owner, the store (noema#756), so the Record event and the row are one unit. The route does not append it.
- **One answer per request:** enforced by the database, `UNIQUE (tenant_id, request_id)`. The first answer wins and a later one gets 409.
- **Route checks:** the `cfr_` pattern on `request_id`. A customer may answer only a SELF request where the session principal is the requester. Anyone else needs the approver role.
- **T13 safeguards:** it refuses a Given whose fresh evidence-set hash or policy version is empty (UNKNOWN). When more than one policy version took part, the binding's policy version is `ps:` plus hex of SHA-256 over the sorted versions joined by newline.
- **Pending request id:** the intake result carries it so the route can offer the card. noema#755 carries it.
- noema#755: rebase on #757, keeping only the Declined to REJECT mapping.

*Supersedes or changes:* Applies **A329** (the Confirmations adapter is EL's) and **INV-25**, **INV-12**. Migration 0032 is the store (§2).

### A342 (interim): Writes.NeedsWrite.

Add a required boolean `may_write` to every intent node, and a packcheck rule that checks it against the graphs. `fin.payments.exception.investigate` is true, because it can end in ESCALATE. EL adds the field, loader and packcheck rule (a pack-schema minor). C1's adapter reads it. `Writes.Enabled` is the tenant kill-switch read, built by C1.

*Supersedes or changes:* Applies **A329** (Writes is C1's) and **A319** (the kill-switch read). A pack-schema minor change (AGENT-15) with a migration note, EL's.

### A343 (interim): noema#743's clauses.

All three are confirmed. `option_id` requires `clarification_id`. A message carries `text` or `option_id`: they are never both. `clarification_id` with `text` is allowed. The route requires `text` on a first message.

*Supersedes or changes:* Applies **A336** (`message-request.v1`). noema#743 is CON-08's contract pull request.

### A344 (interim): Ownership (C2).

Ownership is a principal-scoped read through the same enterprise read port the Candidates adapter uses, looking the target up only within that customer's scope. Not-owned and absent both return false, and T8's response is identical for both. Nothing is inferred from any Tushe response. It is built against the stand-in client now.

*Supersedes or changes:* Follows **A329** (the assignment of Ownership moves to C2 here: A329 listed it with C1) — see §2. Applies **INV-19**.

### A345 (interim): Policies and Clocks facts (S1 to S4, Q1 to Q8).

**S1:**

- `subject_resource` comes from `AdmittedIntent.TargetRef`.
- `subject_resource.status` is the slot status, mapped by identical name, and any other value is an error.
- `logical_resolution_epoch` is a new column on `admitted_intent` (migration 0033, C2, because A151 gave C2 the store). It is 1 at creation. The increment path is later debt.
- The case rows come from the sealed evidence snapshot. EL adds the case system to the profile's `evidence_required`, and C2 adds the case mapping. Absence is never "no case" (INV-19).
- A fact produced by an earlier plan step (`case_id`) is a pack-declared `produced_by` marker. At T11 the FactSource supplies a typed placeholder reference, `planned:<node>`. Execution revalidates with the real id at E4, because the graph's edge puts case creation first.

**S2:** `admitted_at` is the evaluated version's `created_at`.

**S3:** clock anchors come from the sealed snapshot's `complaint_ref` item, and absence is NOT_STARTED. In G1 no complaint exists, so the clock is NOT_STARTED.

**S4:** the at-risk fraction is `NOEMA_TRUST_AT_RISK_BPS=2500` (PERD §27 line 2126, A233 bounds 1000 to 5000). Empty routes are accepted for G1 (A225 handles breach). A pack `routes` field is debt before G2.

**Q1 to Q8 confirmed as built:**

- `published_at` is the effective time, and the intake clock and DB clock are one clock in the bench.
- Every matched rule is recorded.
- Intent-node rules are refused at pack load.
- All supported pack versions load into one book.
- One policy per book.
- Loud error on same-second publications.
- No publication means REJECT `NO_PERMITTING_RULE`.
- `ReevaluateAt` is the reading plus `wait_seconds`.
- Seed: the bench tenants need a published `fin.pol@3.1`, or every query rejects. C1 provides the publish command and IL runs it at init.

*Supersedes or changes:* Registers **migration 0033** on the ledger (noema#183). Opens the pack-routes debt (DEBT-53). Applies **A233**, **A225**, **A151**, **A226**.

### A346 (interim): Correction to A335.

The escalation set is g2's three writes, passed by the composition root as a graph id. `log_complaint_reference` belongs to g3, with a SELF confirmation and `case_id != null`. It follows G1 and uses the confirmation path now being built. Disposition linkage means each disposition authorises exactly its own graph's writes.

*Supersedes or changes:* **Corrects A335**, which put all three write capabilities (including `log_complaint_reference`) in the escalation set. `log_complaint_reference` is g3's, after G1.

### A347 (interim): Fixed-text errors.

Every new adapter and library (noema#738, #747, `KEY_ROTATED`, #748) uses a fixed public error text, with the cause kept for `errors.Is` and `errors.As`. No tenant id or driver text appears in it. C1 sweeps them.

*Supersedes or changes:* Applies **AGENT-13**.

### A348 (interim): A339 deviation accepted.

C1 uses a session-level advisory lock taken before `BEGIN`. A transaction-level lock inside a SERIALIZABLE transaction would take its snapshot before waiting, and that is the stale-snapshot failure. The conditions are: always release on the same connection, with the wait bounded by the context deadline, and a test proving release after panic and cancellation.

*Supersedes or changes:* Amends **A339** (the lock is session-level, before `BEGIN`).

### A349 (interim): regression-link.

Defects below the public API use a `Regression case:` line naming a changed test file (A156). No BEN case is needed. noema#748 and #737 are settled.

*Supersedes or changes:* Applies **A156** and the check of MEM-02 (noema#673).

### A350 (interim): Small adapter rulings.

- noema#741: add explicit checks for direction and currency (two lines, so there is no further debate). Take the bounds from the contract's own constants, and a test asserts they equal the schema.
- noema#739 and #740: C2 files the shared-reader follow-up (DEBT-52).
- noema#751: the PlanGraphs adapter takes params only from the intent's slots and pack data, and SR reads it before wiring.
- noema#752: refuse a context with no deadline, and test the `ErrCommit` to UNKNOWN mapping.

*Supersedes or changes:* Opens DEBT-52.

### A351 (interim): SSE is off the G1 path.

noema#726 continues after G1. The harness polls `GET /v1/investigations/{id}` and the audit route.

*Supersedes or changes:* Applies **A318**/**A296** (SSE) by moving it after G1.

### A352 (interim): Change requests.

docs#206 takes option (b): no new arrow, and the runner re-evaluates so Trust decides ESCALATE. docs#209 is approved: the SoT wins on `DECLINED_BY_APPROVER`. The Steward drafts one PERD version covering both, plus TRU-08's lazy void, EVD-06's order (strip, cap, detect), and §23.3.

*Supersedes or changes:* **Settles** the question left open in `DEC-2026-11-18-architect-rulings-a329-a340` §2 (option (b)). Applies **A338**. Drafted as PERD v1.26 (§2).

### A353 (interim): noema#716.

Include the `init.sh` change for tenant creation (a protected path, and the Founder's approval of the pull request covers it).

*Supersedes or changes:* Applies **A319** (tenant creation becomes an init-time step) and AGENTS §11 (protected paths).

### A354 (interim): Stack readiness (IL).

- Rename the mode to `stack-check`.
- The expected `RECORD_ACCESSED` count is derived from the run's own request log, not a constant.
- Pin the planted canary in the command.

*Supersedes or changes:* Renames the `mode=smoke` of **A323**.

### A355 (interim): BO's package.

Rows 5, 8 and 9 are computed from the run's artifacts (the check-runs JSON, the leak-scan output, the probe results), not attested.

*Supersedes or changes:* Applies **A322**.

### A356 (interim): Compose bench settings (IL).

These are values with no code defaults:

| Setting | Value |
|---|---|
| `NOEMA_STORE_TIMEOUT_MS` | 1000 |
| `NOEMA_SEAL_TIMEOUT_MS` | 1000 |
| `NOEMA_COMPILE_TIMEOUT_MS` | 3000 |
| `NOEMA_READ_TIMEOUT_MS` | 2000 |
| `NOEMA_TRUST_DB_TIMEOUT_MS` | 1000 |
| `NOEMA_TRUST_RECONCILE_TIMEOUT_MS` | 1000 |
| `NOEMA_GRANT_KEY_MAX_ACTIVE` | 2 |
| `NOEMA_DB_SERIALIZATION_ATTEMPTS` | 3 |
| `NOEMA_OUTBOX_INTERVAL_MS` | 1000 |
| `NOEMA_TRUST_AT_RISK_BPS` | 2500 |
| `NOEMA_GRANT_KEY_DIR`, `NOEMA_PACK_DIR`, `NOEMA_TRUST_DSN_DIR` | paths |

IL also adds the per-tenant Trust login secrets for `NOEMA_TRUST_DSN_DIR`.

*Supersedes or changes:* Collects the settings of **A319**, **A320**, **A330**, **A345**. Applies **AGENT-16** (no defaults in code) and INV-29 (the secrets are file-mounted).

### A357 (interim): Process.

One `regression-link` note per pull request. Agents stop re-posting the same status, and a stopped agent stays stopped.

*Supersedes or changes:* Applies **A340**.

## 2. What the Steward did, and where the rulings are silent

- **A335 corrected (A346).** A335 is recorded in `DEC-2026-11-18-architect-rulings-a329-a340` (§1, merged in docs#207). That record is not edited; this one says A346 corrects it. The corrected reading: the escalation set is graph g2's three writes, passed as a graph id; `log_complaint_reference` belongs to g3 (a SELF confirmation and `case_id != null`), after G1.
- **One PERD version (A352): PERD v1.26, Proposed,** by CR-2026-11-19-A352-perd-v1.26. It is v1.25 (which carries v1.24's Intron change and the D8 lazy void of A312) plus: **§23.3** (a) the T13 row may end in REJECT `DECLINED_BY_APPROVER` on a declined confirmation (docs#209; the SoT §43.2a already says so: the SoT wins) and (b) the reason-code table gains the three codes A254 adopted, with the steps that produce them (`TARGET_FROZEN` at T10; `CLOCK_BREACHED_UNROUTED` and `DISPATCH_BUDGET_EXHAUSTED` at T12, as the code has them); **REQ-CTX-007** (EVD-06's order: strip control characters, then cap, then detect; the call site is the Evidence layer after the payload read; the detector's patterns are pack data, A292). **docs#206 under option (b) changes no PERD text** (no new §28.2 arrow). TRU-08's lazy void is carried from v1.25 unchanged. v1.26 takes effect only with the SoT version that restates INV-26 (SOT-C-32) and the one that adopts A179, as v1.25 does; its §23.3 and REQ-CTX-007 changes need no SoT edit, so the Architect may split them out if he wants them sooner.
- **A344 moves Ownership to C2.** A329 listed Ownership with C1; A344 says "Ownership (C2)". The Steward records both as given. C2 builds it; C1 and C2 confirm the assignment on their pull requests (A332: the authors decide).
- **DEBT-52 and DEBT-53 are filed** (§3). The `logical_resolution_epoch` increment path (A345 S1, "later debt") is not filed: no owner or due point is given. C2 names it when the path is built.
- **Migration 0033 is registered** on the ledger (noema#183, a comment posted by the Steward): `admitted_intent.logical_resolution_epoch`, C2, A345 S1. The same comment lists 0030 (noema#716), 0032 (the confirmation store, noema#756) and the migrations on `main`.
- **G0-N checklist refreshed** from merged work (`docs/poc/execution/sessions/2026-11-17-1000-G0-N-checklist.md`); still **not yet passed**.
- **A353** (the `init.sh` change in noema#716): the ruling says the Founder's approval of the pull request covers it; the Steward does not approve. The protected-path rule needs that approval on the final head.
- **Next free ruling: A358.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| This record | A341 to A357 | **A358** |
