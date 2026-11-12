# DEC-2026-11-12 · Architect ruling A176 (interim): pushes, merges of `main`, CI cancels and one action pin

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the ruling); Founder and Technical Co-Founder (the merge) |
| **Decides** | One interim ruling, A176 (§1), with five rules. |
| **Closes** | Nothing by itself. |
| **Supersedes** | Nothing committed. See §1 for how each rule relates to earlier rules. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: nothing by itself
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A176 (interim)
- Decision: §1
- Rationale and evidence: the Architect's message of 12 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: AGENT-14, AGENT-29; SoT §0.4
- Migration notes: none
- Supersedes: nothing committed

---

## 1. The ruling, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A176** (interim) | **The Steward commits these rules.** (1) Never merge `main` into a PR unless it conflicts or a stack needs it. (2) A failing-first draft gets one push for the red head. After that, no pushes until the fix is ready. (3) Never push to a branch with a run in progress. Let it finish, or cancel your own run first. (4) IL splits noema#482 now. The concurrency cancel goes in its own small PR first. Sharding follows only with measured numbers. (5) `actions/cache`: the Architect could not verify its SHA from there. IL names the tag and full SHA, and SR or the Steward checks it on GitHub's release page. The Steward approves it only after that. | Nothing committed. Rule (1) narrows the habit of merging `main` into a PR to keep a READY alive (A130 says a clean merge keeps it; it does not say to do one). Rule (5) applies AGENT-14 (a new dependency needs approval) to `actions/cache`. |

## 2. What the Steward did where the ruling is silent

- **The numbering.** The Architect's rulings from A171 to A175 have not been given to the Steward in text. This record does not use those numbers and does not guess them. **Next free after this record: A177**; the Steward adds A171 to A175 in a follow-up pull request when their texts arrive.
- **Rule (5) and who checks.** The Steward will not approve the `actions/cache` pin until IL names the tag and the full SHA and the SHA is checked on GitHub's release page (for the tag, the commit SHA of the tag in `actions/cache`). Nothing is approved here.
- **Rules (1) to (3) and the Steward's own branches.** The Steward follows them from this record's date: it merges `main` into a pull request only to clear a conflict, and it does not push to a branch while a run on it is in progress.
- **Interim.** The ruling is marked interim by the Architect. It stays until a later ruling replaces it.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A147 | |
| docs#157 (open) | A148 to A161 | |
| docs#158 (open) | A162 to A165 | |
| docs#159 (open) | A166 to A170 | |
| A171 to A175 | used by the Architect; texts not yet given to the Steward | |
| This record | A176 (interim) | **A177** |
