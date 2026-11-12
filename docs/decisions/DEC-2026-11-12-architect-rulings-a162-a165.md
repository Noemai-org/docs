# DEC-2026-11-12 · Architect rulings A162 to A165

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). **A162 also needs the Founder's approval of the harness re-freeze record** (`DEC-2026-11-12-harness-masking-refreeze`, D10 frozen values). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Four rulings, A162 to A165 (§1). Each states what it supersedes. |
| **Closes** | The questions behind noema#462 (A165) and noema#472 (A164), and EL's finding on the harness masking floor (A162). |
| **Supersedes** | Per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. The rulings of A148 to A161 are in `DEC-2026-11-12-architect-rulings-a148-a160` (docs#157, open when this was written). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 12 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: the questions behind noema#462 and noema#472
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A162 to A165
- Decision: §1
- Rationale and evidence: the Architect's message of 12 Nov 2026 relayed by the Founder; EL's finding on the harness masking floor
- Affected requirement IDs / SoT sections: REQ-SEC-001, REQ-SEC-004, REQ-AGT-001, PERD §44.2 and the explanation criteria; INV-12, INV-29; AGENT-13, AGENT-15, AGENT-29; SoT §0.4
- Migration notes: A165 adds migration 0024; A164 adds none
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A162** | **Model-service masking floor.** EL found the harness still masks at 8 (frozen in `benchmark/decisions/harness-*.json`, hashed in a decision record). The PERD wins: prompts are an outward surface, so the floor is 4. The two harness configs are re-frozen without the key, and the harness reads the shared `masking-limits.v1`. Tightening masking is safer, and no arm has run yet. A new decision record carries it. Founder approval needed (D10 frozen values). | **The value `account_run_min_digits: 8` frozen in `benchmark/decisions/harness-gpt-6-luna.json` and `harness-gpt-6.1-terra.json` and hashed in `benchmark/decisions/2026-10-27-model-selection.md`.** The new record `DEC-2026-11-12-harness-masking-refreeze` carries the re-freeze. |
| **A163** | **Identity shapes.** Widen the Intent Object's `asserted_by` pattern to allow hyphens (a contract bump, AGENT-15), so `noema-poc-idp` fits. The synthetic IdP mints `sub` as `usr_<ULID>` and the verifier requires that shape. G1 principals are `usr_…`. | **The current `asserted_by` pattern of the Intent Object contract** (it does not allow a hyphen). The contract bump is the owner's, with the AGENT-15 steps. |
| **A164** | **noema#472 (budget in the database).** No new void reason or event kind now. The refused grant stays `ISSUED` and the caller gets `BudgetSpent`. C1 records the refusal with an existing event if a fitting reason code exists, otherwise a DEBT entry. Under A141 noema#472 does not wait for 0022. | Nothing. |
| **A165** | **noema#462.** Migration 0015's `policy_version_key` is executable by PUBLIC. EL fixes it with a forward migration (0024): revoke from PUBLIC, grant only to the roles that need it, failing-first with EL's own existing test. This clears noema#268's red `core`. | Nothing. A forward migration; 0015 is not edited (AGENTS §7). |

## 2. What the Steward did where the rulings are silent

- **A162 and the new record.** The Steward wrote the decision record the ruling asks for in the docs repository: `DEC-2026-11-12-harness-masking-refreeze`. It names what changes and what it supersedes, and **needs the Founder's approval**. The re-freeze itself (the two config files and the new SHA-256 hashes in a `benchmark/decisions/` record) is the Benchmark Owner's work in `noema`; the Steward computes no hash and edits no benchmark file.
- **A162 against A154.** A154 already puts the maximum unmasked digit run at 4 on every outward surface, including model prompts. A162 applies it to the harness. They do not conflict.
- **A164 and A165 and numbers.** The migration number 0024 is A165's. 0022 stays unresolved between noema#410 and the admitted-intent store (record `DEC-2026-11-12-architect-rulings-a148-a160`, §2); this record does not decide it.
- **`tasks.csv`.** No change is made: the message says "UND-05 and EXE-05 notes per Architect" but gives no text, and the CSV has no note column. The session note records what is already decided for both (UND-05: the USD 5 hard stop and the key names, DEC-2026-11-11-architect-rulings-a129-a147 §3; EXE-05: the allowlist of A157). The Steward asks the Architect for the notes.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A147 | |
| DEC-2026-11-12-architect-rulings-a148-a160 (docs#157, open) | A148 to A161 | |
| This record | A162 to A165 | **A166** |
