# DEC-2026-11-23 · Architect rulings A561 to A576 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A561 to A576 (§1), every one Interim. |
| **Supersedes** | **A574 replaces the second bullet of A562** (no empty-evidence-set hash; truthful absence instead) and changes `decision-record.v2` (§1, A574). **A566 refines A560** (§1: floor division only for the final reported score; the margin and the floor are compared in exact scaled-integer arithmetic). **A567 settles** where the freeze allow-list lives (`trust_limits.json`, under A544) and opens a conflict with PERD REQ-RES-002 (register entry SOT-C-33). **A561 turns** the PERD's 10-minute default confirmation expiry into a ceiling. **A564** gives the Outcome verdict signer its own key directory. **A571** changes noema#905. **A572** files DEBT-57. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. A567's PERD change and the A555 and A566 PERD notes go through change requests (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A561 to A576
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-14, INV-20, INV-21, INV-29; AGENT-15, AGENT-16, AGENT-27; REQ-TRU-009, REQ-TRU-010, REQ-RES-002, REQ-AMB-003, REQ-AUD-004; PERD §22, §23; `decision-record.v2`; AGENTS §5, §8, §11
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A565 is one contract version bump by C1 after G1 (AGENT-15 steps). A567 keeps additive optional pack members at v1 with a migration note (precedent noema#879, noema#902). A574 adds one contract change and one database migration (C1's own small PR, the next free number on noema#183, 0038; both Founders for the contract; an independent migration read, A463). A572 adds no other migration.

## 1. The rulings

Confirmed first: A554 to A560 are committed on `main` (docs#232, merged 13:13 UTC, 23 Nov 2026, in `DEC-2026-11-23-architect-rulings-a554-a560`).

### A561 (interim, confirmation TTL ceiling).

The ceiling is the PERD's 10 minutes (EL reads it so; C2 cites the section). It is a required member of `trust_limits.json`, owned by C2. C1 reads it through `trustlimits` and refuses a larger TTL in intake and in the Writer. #911 merges first and the ceiling follows as a small PR. C1 also narrows the Writer's SQLSTATE class-23 match to the specific constraint.

### A562 (interim, #903 and #733).

- A disposition id goes into a `RecordRequest` only when the continuation names an escalation-set step. It never goes onto a read or no-step decision. C1 fixes #903's pass-through, and #733's refusal stays.
- An early ESCALATE (before policy and evidence are evaluated) is still recorded, with its intent hash, the policy version in force and its reason codes, and an empty evidence set (the hash of the empty set). If the PERD forbids this, C1 raises a CONFLICT block instead of guessing. **[This second bullet is withdrawn and replaced by A574 below: no empty-evidence-set hash; truthful absence instead. The text above is kept as the Architect gave it, for the audit trail.]**
- A replay test that breaks once #733 lands is updated in the same change.

### A563 (interim).

A missing time window makes Trust ask the customer when (CLARIFY) before any candidates read. The candidates read never runs on an empty window (A535).

### A564 (interim, Outcome signer keys).

The Outcome verdict signer gets its own key directory: `NOEMA_OUTCOME_KEY_DIR` with `NOEMA_OUTCOME_KEY_MAX_ACTIVE`, identity `core-outcome` (announced in migration 0013), files 0400, owner 65532. Execution and Outcome keys stay apart.

### A565 (interim, scorecard basis points, after G1).

BO's list is the scope: `Rate.rate`, `wilson95`, `rule_of_three_upper`, `exact_upper95` and the mean turns. Upper bounds round up, lower bounds round down, and the rate rounds to the nearest. Mean turns become integer milli-turns. One version bump, by C1, after G1, and FE hears first.

### A566 (interim, ranker, #918; refines A560).

Floor division applies only to the final reported score. The margin and the floor are compared in exact scaled-integer arithmetic on the unrounded sums, never on floored scores. A vector with a fractional score at the margin is required (top 9000.00 against 5500.25 must be AMBIGUOUS).

### A567 (interim, #910).

The freeze allow-list stays in `trust_limits.json` under A544. The conflict with REQ-RES-002, which puts it on the capability descriptors, goes into the conflicts register, and the Steward drafts the change request. The consumer fails closed when the limits entry is missing, owned by EL. Additive optional pack members stay v1 with a migration note (precedent #879, #902).

### A568 (interim, #824).

Every second of audio sent and received counts against the budget: STT audio sent and TTS audio generated. A read failure must not discard the report; it writes incrementally. Both are fixed before any live run.

### A569 (interim, #638 audience).

The reconstruction route is audit-only. UI-03's reconstruction view serves audit sessions only. Ops use their own panel route, which has no UI work until that route exists (after G1). The UI never implies ops can read reconstructions.

### A570 (interim, "Verified").

In customer screens (#609, #616) the word "Verified" is never used; outcomes use plain words (done, not yet confirmed). In the audit panel (#638), "Record verified" appears once, only from the backend's chain verdict, never per ACHIEVED item. A524's generic message applies to the panel only.

### A571 (interim, #905 and #900).

A partial pack-settings set is a named `/readyz` gap, as in #900 (A469, A486). An invalid value is fatal. #905 changes.

### A572 (interim, tenant-init).

Tenant-init uses the superuser DSN and the migration login stays out (A527, A536). The private-copy approach is accepted. The narrower provisioning login for tenants-provision and tenant-init is debt, owner C2 with IL, due before the G2 review. The G1 record states plainly what is used.

### A573 (interim).

FE's UI fixes may move to a Claude Code session if its environment cannot reach GitHub. Dependent UI PRs merge main in, never rebase (AGENTS §11).

### A574 (interim, corrects A562's second bullet).

FE is right, and so is the contract text. The Architect's "record an early ESCALATE with an empty evidence set" would claim an evidence evaluation that never happened. That is a synthetic claim, so it is withdrawn.

- **The fix is truthful absence.** `decision-record.v2` currently requires `evidence_snapshot_id`, `policy_version` and `evidence_freshness` for every outcome. The decision-basis rules allow an early non-ALLOW outcome to carry only the pack version and the evaluation time. So for REJECT, CLARIFY, WAIT, ESCALATE and UNKNOWN those three members become nullable. ALLOW and CONFIRM keep them required and non-null.
- **Mechanics.** C1 does it as its own small PR: a conditional schema rule, a migration relaxing NOT NULL with a CHECK on outcome (preserving the immutability triggers), a migration note and regenerated models. It is a `/contracts` change, so both Founders, and a migration needs an independent read (A463). The migration number is the next free one on #183.
- **Order for #903.** #903 merges now with the post-accept recording fix. An early-gate ESCALATE ends in UNKNOWN with a typed reason, which is safe and truthful. The contract PR follows immediately. C1 confirms none of the five G1 cases can end in an early ESCALATE. If any can, the contract PR moves ahead of the run.

### A575 (interim, #910).

`anchor_entities[].field` must be a declared Timestamp field in the descriptor. C2 adds that validation, with negative tests for a missing field and a non-timestamp field, and merges main to clear the conflict.

### A576 (interim, #616).

FE's safe retry is approved. After an ambiguous failure the original answer stays locked, the screen says it cannot confirm whether the answer was recorded, and retry sends only that same answer with the same request id. The opposite answer is never offered. The server's first-answer-wins rule (A341) stays the authority.

## 2. What the Steward did, and where the rulings are silent

- **A561 and the Writer's source for the ceiling (EL).** The ceiling reaches the Writer as an injected value from `trustlimits`, not as a database read inside the transaction, so the Writer's dependency direction stays as it is. EL moves the A519 tests (noema#909, which use a SYNTHETIC far-future expiry) to a value within 10 minutes when the ceiling lands.
- **A561.** PERD REQ-TRU-009 says "Default expiry: 10 min [ADOPTED DEC-2026-10-17]". A561 makes 10 minutes the ceiling for the TTL; the value is the PERD's, and C2 cites the section when it adds the required `trust_limits.json` member. The Steward fills no value (AGENT-16). noema#911 merges first.
- **A562 and A574.** A574 withdraws the second bullet of A562: nothing is recorded as an empty evidence set, and no empty-set hash exists. The reviewers' concern on docs#233 (Codex and EL: an empty-set hash could be mistaken for a sealed snapshot of nothing, and ALLOW or CONFIRM with an empty basis must stay refused) is met by A574's own terms, as the Steward reads them: the three members are **nullable** for REJECT, CLARIFY, WAIT, ESCALATE and UNKNOWN, so an early outcome claims no evaluation, and ALLOW and CONFIRM keep them required and non-null, so they cannot carry a missing basis. Grants come only from ALLOW (INV-25), as before. The ruling names a "typed reason" for an early-gate ESCALATE that ends in UNKNOWN (§1, A574, order for #903); C1 states the reason code in its PR, and the Steward invents none. The tests the reviewers asked for (a T7 and a T9 early ESCALATE through the real adapter and Writer; ALLOW and CONFIRM refused without the three members) are C1's and EL's.
- **A574: "nullable" is not "omitted" (Codex's second pass; open for the Architect).** The ruling says "nullable" and a migration that "relax[es] NOT NULL". In JSON Schema and database terms, a **nullable** member is present with the value `null`; an **optional** member may be left out; these are different contracts, and in a canonical, hashed record they are different bytes. The record does not leave "absent (null)" as the specification (an earlier line of this record used that phrase; it is withdrawn). **The Steward's reading, not a ruling:** the three keys stay *required* in `decision-record.v2` and hold JSON `null` for the five outcomes, which matches the database column that becomes nullable; ALLOW and CONFIRM require them present and non-null; no outcome may omit a key. **The Architect confirms or corrects this**, and C1 then aligns the schema rule, the DB CHECK, the generated models and the tests to that one contract.
- **A574 and the migration ledger.** The Steward reserved **0038** on noema#183 for A574's migration (0037 stays reserved for DEBT-54; no open pull request claims 0037 to 0049). The author is C1, so the independent migration read comes from EL or C2, and SR reads as SR (A463). The contract change needs both Founders (AGENT-15). C1 confirms that none of the five G1 cases can end in an early ESCALATE; if one can, the contract PR moves ahead of the G1 run. Until that PR merges, #903's early-gate ESCALATE ends in UNKNOWN with a typed reason.
- **A575 and A576.** A575 is C2's (noema#910: the validation, the negative tests, merging `main`); A576 is FE's (noema#616). The Steward changes no code or UI. A576 leaves A341 (first answer wins) as the authority.
- **A564.** IL adds the mounts, and SR reads the new key directory (a secrets path). Identity `core-outcome` is announced in `services/core/migrations/0013_receipt_signature.sql`; mode 0400 and owner 65532 come from A518 and A553, as in A554.
- **A565 and A570.** A565 is after G1, one contract version bump by C1 with the AGENT-15 steps; nothing changes now, and FE hears first. A570's wording rules apply to the UI PRs (FE's); the Steward changes no UI text.
- **A566 and the A555 change request.** A566 refines A560. The Steward added the A566 rule and the proposed PERD notes to `CR-2026-11-23-A555-perd-22-1-ranker-placement` (still a Draft; the PERD stays v1.28). The example in A566 shows why the rule matters: 9000.00 minus 5500.25 is 3499.75, below the 3500 margin, so the case is AMBIGUOUS; on floored scores it would read 9000 minus 5500, exactly 3500, and pass.
- **A567 and the conflicts register.** The Steward added **SOT-C-33** (Open) to `docs/poc/perd/conflicts-register.md` and drafted `CR-2026-11-23-A567-perd-res-002-freeze-allow-list` (Draft). PERD REQ-RES-002 puts `allowed_under_freeze: true` on the capability descriptors [ADOPTED DEC-2026-10-17]; A544 (Interim, already committed in docs#231) and A567 (Interim, in this record) put the allow-list in `trust_limits.json`. **Authority, stated conditionally (Codex's point):** A567 is not binding until this record is approved and merged by a non-author Founder (A111; AGENTS §2, item 3). Until then the committed PERD v1.28 REQ-RES-002 stands, A544 is the committed Interim ruling, and the conflict is recorded, not resolved. Once this record merges, A567 is the latest recorded decision (SoT §0.4) and governs until a new PERD version exists. Whichever applies, the safer reading is the same: a missing limits entry allows nothing under a freeze (A544).
- **A567 and the duplicate authority (EL and Codex).** The single source is real only when the descriptor's `allowed_under_freeze` is removed as an authority, or kept as non-authoritative with a pack loader that fails closed on any mismatch with the limits entry (EL recommends removal). It also needs a rule that a pack of manifest version 3 or later must list the limits files: EL found that noema#910's pin is opt-in (deleting the four manifest entries leaves the loader and packcheck green). Both are in the change request as conditions; the Architect decides the first.
- **A568 and A569 to A573.** A568 is Voice's (noema#824); A569 and A570 are FE's (noema#638, #609, #616); A571 is EL's (noema#905); A573 is FE's. The Steward changes no code or UI.
- **A572 and the debt register.** The Steward filed **DEBT-57** (the narrower provisioning login for tenants-provision and tenant-init; owner C2 with IL; due before the G2 review). A572 does not set a tier; the Architect sets it. EL recommends Tier 2 (a secrets path with the widest login, though the DSN never reaches argv, the environment or a log), with the due point as written and the G1 record naming the DSN used; that is a recommendation, not a ruling. The G1 record states plainly what is used.
- **Migration ledger on noema#183:** 0037 stays reserved for DEBT-54; **0038 is reserved for A574** (above). Next free: 0039.
- **Task status (`tasks.csv`)** is unchanged here; it moves only on merged evidence.
- **Next free ruling: A577.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533`, `-a534-a540`, `-a542-a553`, `-a554-a560` | A530 to A533; A534 to A540; A541 noted, A542 to A553; A554 to A560 | |
| This record | A561 to A576 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank); A537 lane contents beyond lane 5; the typed reason code of A574's early-gate UNKNOWN (C1 states it) | **A577** |
