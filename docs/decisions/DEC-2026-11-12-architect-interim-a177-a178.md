# DEC-2026-11-12 · Architect rulings A177 and A178 (interim): the intent signature, and inline P1 findings

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Two interim rulings, A177 and A178 (§1). |
| **Closes** | Nothing by itself. Opens OD-P-85 (§2). |
| **Supersedes** | Nothing committed. See §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: nothing by itself; opens OD-P-85
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A177 (interim), A178 (interim)
- Decision: §1
- Rationale and evidence: the Architect's message of 12 Nov 2026, relayed to the Steward (A177 answers C1's question on noema#484)
- Affected requirement IDs / SoT sections: AGENT-02, INV-22; SoT §7 (the Intent Object and its signature), §0.4
- Migration notes: none
- Supersedes: nothing committed

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A177** (interim) | **Intent signature (C1's question on noema#484).** The signature that counts is the Record's signature on `INTENT_ADMITTED`, made by the REC-08 emitter signer. The core computes `intent_hash` over canonical JSON. The Intent Object's own `sig` field stays the unsigned marker in the POC. No new signing domain is invented (AGENT-02). The Steward files an [OPEN] entry to check this against the SoT. The model service never signs. The model-side gate stays on v1 until the v2 contract is live. C2 fixes the #489 README and comments in one push. | Nothing committed. |
| **A178** (interim) | **Inline P1s.** A reviewer's "READY at the same head" does not resolve an open inline P1. Codex must say per thread whether it is resolved at the next head. INV-22 findings are never waived. | Nothing committed. It states how an open inline P1 is closed; it does not change who may merge (A111, A143). |

## 2. What the Steward did where the rulings are silent

- **The [OPEN] entry for A177 is OD-P-85.** The Steward read the SoT before writing it and found a difference to check, not a decision. SoT §7 describes the Intent Object as "signed by Understanding", and its Trust row lists "schema and signature of the Intent Object" among the checks. A177 keeps the Intent Object's `sig` as an unsigned marker and takes the Record's signature on `INTENT_ADMITTED` as the one that counts. The entry records that as the default and asks the Architect or the Founders to say whether this needs a SoT edit, a decision record that amends the SoT reading, or nothing. The Steward does not decide it.
- **The OD-P number.** docs#159 holds OD-P-82. The Steward understands BO and FE take the next two, so this record uses OD-P-85 and leaves 83 and 84 free. If BO or FE already hold 85, the Steward renumbers in one push.
- **Ruling numbers.** A171 to A175 are still not recorded; their texts have not been given. A176 is in docs#162 (open). Next free after this record: **A179**.
- **Who does what.** C2 fixes the noema#489 README and comments; the Steward does not touch noema#489. The Steward asks nothing of the model service.
- **A178 and the review comments.** The Steward will not count a reviewer's READY at an unchanged head as closing an inline P1. On a PR with an open inline P1 the Steward will say so on the board and wait for Codex's per-thread answer.
- **Interim.** Both rulings are marked interim by the Architect. They stay until a later ruling replaces them.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A161 | |
| docs#158 (open) | A162 to A165 | |
| docs#159 (open) | A166 to A170 | |
| A171 to A175 | used by the Architect; texts not yet given to the Steward | |
| docs#162 (open) | A176 (interim) | |
| This record | A177, A178 (interim) | **A179** |
