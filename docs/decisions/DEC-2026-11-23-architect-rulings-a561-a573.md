# DEC-2026-11-23 · Architect rulings A561 to A573 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A561 to A573 (§1), every one Interim. |
| **Supersedes** | **A566 refines A560** (§1: floor division only for the final reported score; the margin and the floor are compared in exact scaled-integer arithmetic). **A567 settles** where the freeze allow-list lives (`trust_limits.json`, under A544) and opens a conflict with PERD REQ-RES-002 (register entry SOT-C-33). **A561 turns** the PERD's 10-minute default confirmation expiry into a ceiling. **A564** gives the Outcome verdict signer its own key directory. **A571** changes noema#905. **A572** files DEBT-57. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. A567's PERD change and the A555 and A566 PERD notes go through change requests (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A561 to A573
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-14, INV-20, INV-21, INV-29; AGENT-15, AGENT-16, AGENT-27; REQ-TRU-009, REQ-TRU-010, REQ-RES-002, REQ-AMB-003, REQ-AUD-004; PERD §22, §23; AGENTS §5, §8, §11
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A565 is one contract version bump by C1 after G1 (AGENT-15 steps). A567 keeps additive optional pack members at v1 with a migration note (precedent noema#879, noema#902). A572 adds no migration.

## 1. The rulings

Confirmed first: A554 to A560 are committed on `main` (docs#232, merged 13:13 UTC, 23 Nov 2026, in `DEC-2026-11-23-architect-rulings-a554-a560`).

### A561 (interim, confirmation TTL ceiling).

The ceiling is the PERD's 10 minutes (EL reads it so; C2 cites the section). It is a required member of `trust_limits.json`, owned by C2. C1 reads it through `trustlimits` and refuses a larger TTL in intake and in the Writer. #911 merges first and the ceiling follows as a small PR. C1 also narrows the Writer's SQLSTATE class-23 match to the specific constraint.

### A562 (interim, #903 and #733).

- A disposition id goes into a `RecordRequest` only when the continuation names an escalation-set step. It never goes onto a read or no-step decision. C1 fixes #903's pass-through, and #733's refusal stays.
- An early ESCALATE (before policy and evidence are evaluated) is still recorded, with its intent hash, the policy version in force and its reason codes, and an empty evidence set (the hash of the empty set). If the PERD forbids this, C1 raises a CONFLICT block instead of guessing.
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

## 2. What the Steward did, and where the rulings are silent

- **A561.** PERD REQ-TRU-009 says "Default expiry: 10 min [ADOPTED DEC-2026-10-17]". A561 makes 10 minutes the ceiling for the TTL; the value is the PERD's, and C2 cites the section when it adds the required `trust_limits.json` member. The Steward fills no value (AGENT-16). noema#911 merges first.
- **A562.** The hash of the empty evidence set is not stated in the ruling; C1 states which digest it is and where it is defined. Whether the PERD forbids recording an early ESCALATE is C1's to check, and a CONFLICT block is C1's if it does (AGENT-27); the Steward raises none.
- **A564.** IL adds the mounts, and SR reads the new key directory (a secrets path). Identity `core-outcome` is announced in `services/core/migrations/0013_receipt_signature.sql`; mode 0400 and owner 65532 come from A518 and A553, as in A554.
- **A565 and A570.** A565 is after G1, one contract version bump by C1 with the AGENT-15 steps; nothing changes now, and FE hears first. A570's wording rules apply to the UI PRs (FE's); the Steward changes no UI text.
- **A566 and the A555 change request.** A566 refines A560. The Steward added the A566 rule and the proposed PERD notes to `CR-2026-11-23-A555-perd-22-1-ranker-placement` (still a Draft; the PERD stays v1.28). The example in A566 shows why the rule matters: 9000.00 minus 5500.25 is 3499.75, below the 3500 margin, so the case is AMBIGUOUS; on floored scores it would read 9000 minus 5500, exactly 3500, and pass.
- **A567 and the conflicts register.** The Steward added **SOT-C-33** (Open) to `docs/poc/perd/conflicts-register.md` and drafted `CR-2026-11-23-A567-perd-res-002-freeze-allow-list` (Draft). PERD REQ-RES-002 puts `allowed_under_freeze: true` on the capability descriptors [ADOPTED DEC-2026-10-17]; A544 and A567 put the allow-list in `trust_limits.json`. Until the Founders adopt the change request, A567 governs, and the safer reading applies: a missing limits entry means nothing is allowed under freeze (A544).
- **A568 and A569 to A573.** A568 is Voice's (noema#824); A569 and A570 are FE's (noema#638, #609, #616); A571 is EL's (noema#905); A573 is FE's. The Steward changes no code or UI.
- **A572 and the debt register.** The Steward filed **DEBT-57** (the narrower provisioning login for tenants-provision and tenant-init; owner C2 with IL; due before the G2 review). A572 does not set a tier; the Architect sets it. The G1 record states plainly what is used.
- **Migration ledger on noema#183** is unchanged: 0037 stays reserved.
- **Task status (`tasks.csv`)** is unchanged here; it moves only on merged evidence.
- **Next free ruling: A574.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533`, `-a534-a540`, `-a542-a553`, `-a554-a560` | A530 to A533; A534 to A540; A541 noted, A542 to A553; A554 to A560 | |
| This record | A561 to A573 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank); A537 lane contents beyond lane 5 | **A574** |
