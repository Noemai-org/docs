# DEC-2026-11-12 · Architect rulings A171 to A175

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Five rulings, A171 to A175 (§1). Each states what it supersedes. |
| **Closes** | The open question on noema#410 and 0022 (A171, asked in `DEC-2026-11-12-architect-rulings-a166-a170`, §2). |
| **Supersedes** | Per ruling, in §1. In short: A171 corrects A167; A172 supersedes the owner assignment in noema#495. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 12 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: the 0022 question (A171)
- Owner: Principal Architect; Technical Co-Founder
- Decides: A171 to A175
- Decision: §1
- Rationale and evidence: the Architect's message of 12 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-12, INV-29; AGENT-02, AGENT-15, AGENT-29; SoT §0.4; REQ-API-001
- Migration notes: A171 reserves 0022; the migration table on noema#183 (C1) governs every number; no migration is added by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A171** | C1's migration ledger on noema#183 governs migration numbers. noema#410 is closed without merge, so A167's statement that #410 "holds" 0022 is corrected: **0022 stays reserved for C2's evidence-set binding; no other PR uses it.** The Steward allocates OD-P numbers: docs#159 keeps OD-P-82 (reader pools); the next two entries (BO's link-format entry, FE's frontend-dependency entry) take OD-P-83 and OD-P-84 in the order they open. | The words in **A167** that say noema#410 holds 0022. Nothing else in A167. |
| **A172** | noema#237 merges as is after its independent role read. The `Trust.Decide` lookup on `(tenant_id, intent_id, intent_hash)` and its unique index are a separate Tier 1 follow-up PR by the author of #237 (EL), failing test first; C1 reviews. Resume of a stranded run waits for it; `Start` (noema#490) is the retry path meanwhile. | **The owner assignment in noema#495.** It also fixes the order for the resume that **A168** ("EL builds resume after that") leaves open: resume waits for this follow-up. |
| **A173** | Fractional values never appear in any hashed member of the Intent Object. Confidence is carried as integer BasisPoints (0 to 10000) via a contract bump (AGENT-15): `intent-slot.v2` and `intent-object.v3`, opened after noema#480 merges. C2 writes schema, fixtures and gate; C1 writes contract tests. Canonical-input is not hashed or signed in anything built so far, so Ratio can stay there. | Nothing committed. It names the contract bump that **A166** item (2) asks for. |
| **A174** | UI checks run on Node 22 (`ui/.nvmrc`). A pass on another Node version is not evidence. | Nothing. |
| **A175** | After a NOT READY the author fixes all findings in one push and posts READY FOR CODEX at the new head once; Codex re-reads that head once. A NOT READY that rests on an authority not yet committed is resolved when the authority is committed; the reviewer then re-reads. | Nothing. It refines the one-push and one-read rules of **A134** and **A176**; it does not change who may merge (A111, A143). |

## 2. What the Steward did where the rulings are silent

- **A171 and the OD-P numbers.** OD-P-82 stays with docs#159. The Steward allocates OD-P-83 to BO's link-format entry and OD-P-84 to FE's frontend-dependency entry, in the order they open. The Steward files neither entry; their owners do. **OD-P-85** is the resume-of-a-stranded-run entry that EL asked the Steward to file on docs#159 (it refines A168 and A172). **OD-P-86** in docs#163 (the intent signature, A177) follows it. If BO or FE has not opened an entry by the time these merge, 83 and 84 stay reserved.
- **OD-P-82 completed.** EL stated the missing fields on docs#159 (what would change it, the deadline, and that the same reader pools serve the reconstruction route of noema#486). The Steward copied them into the entry as EL wrote them.
- **A171 and the board.** The Steward does not repeat any PR's migration number on noema#183 or in a record; it points to C1's table.
- **A172 and noema#495.** The Steward takes the owner assignment in noema#495 as superseded and says so on that issue when the ruling counts. The task row for the `Trust.Decide` lookup follow-up is not created here (no task ID was given); EL's PR carries its own task ID.
- **A173 and A166.** A166 item (2) told C2 to replace a loosened canonical JSON rule with integer basis points through a contract bump. A173 names the contracts (`intent-slot.v2`, `intent-object.v3`), the order (after noema#480 merges) and the owners. No contract file changes in this record (AGENT-15 steps are the PRs').
- **A174.** `ui/.nvmrc` is in `noema`; the Steward changes no file there. CI evidence from another Node version is not evidence on a UI check.
- **A175 and A176.** A176 (docs#162) says a failing-first draft gets one push for its red head. A175 covers the NOT READY case. The Steward follows both on its own PRs.
- **Numbering.** A176 is in docs#162 and A177 and A178 in docs#163, both open. This record follows A170; next free after A178 is **A179**.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A161 | |
| docs#158 (open) | A162 to A165 | |
| DEC-2026-11-12-architect-rulings-a166-a170 (docs#159, open) | A166 to A170 | |
| This record | A171 to A175 | |
| docs#162 (open) | A176 (interim) | |
| docs#163 (open) | A177, A178 (interim) | **A179** |
