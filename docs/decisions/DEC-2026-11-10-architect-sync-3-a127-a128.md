# DEC-2026-11-10 · Architect sync of 10 Nov 2026 (afternoon): rulings A127 and A128

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 10 Nov 2026 (the afternoon Architect sync), relayed to the Repo Steward by the Founder; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 10 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Two rulings, A127 and A128 (§1). Each states what it supersedes. |
| **Closes** | Nothing by itself. |
| **Supersedes** | Nothing committed. Both rulings apply existing rules (A29, A14, A111) to specific cases; §1 says how. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 10 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 10 November 2026
- Closes: nothing by itself
- Owner: Principal Architect; Founder and Technical Co-Founder
- Decides: rulings A127 and A128
- Decision: §1
- Rationale and evidence: the afternoon Architect sync of 10 Nov 2026, relayed by the Founder
- Affected requirement IDs / SoT sections: REQ-AGT-001; AGENT-14, AGENT-29; SoT §0.4
- Migration notes: none
- Supersedes: nothing committed

---

## 1. The rulings

| ID | Ruling | Supersedes |
|---|---|---|
| **A127** | **The text fix on noema#168 goes in a follow-up pull request; noema#168's head stays unchanged.** | Nothing committed. It is a one-pull-request case of A29's fix matrix: the finding is answered by the follow-up, not by a new commit on noema#168, so the READYs given at noema#168's current head stand. |
| **A128** | **A pull request merges only after the reviewer-role READY at its current head. The Founder merges on the owner's `READY TO MERGE` line.** | Nothing committed. It states the order of the A14 and A111 gates: the reviewer-role READY at the current head comes first, then the owner's `READY TO MERGE` line, then one non-author Founder (A111). A111 left the other gates unchanged; this ruling fixes their order. |

## 2. What the Steward did where the rulings are silent

- **A127 and the follow-up.** The ruling names no task or owner for the follow-up. The Steward asks the owner of noema#168 (EL) to open it; it is not numbered or tracked here. The "text fix" is not described in the ruling and is not described here.
- **A128 and merges already made.** Several pull requests merged on 10 Nov, before this record. This record does not judge them. Where a merged pull request lacked a reviewer-role READY at its head, the Steward lists it for the Founders and does not reopen anything.
- **Numbering.** A113 to A122 are in docs#148 (merged 10 Nov) and A123 to A126 in docs#150 (merged 10 Nov). This record follows them; next free is **A129**. If either record changes a number, this one moves with it.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109, A110, A111, A112 | REC-09, control-plane callers, one non-author Founder approval, DEBT-13 and SEC-15 | |
| DEC-2026-11-10-architect-sync-a113-a122 (docs#148, merged) | A113 to A122 | |
| DEC-2026-11-10-architect-sync-2-a123-a126 (docs#150, merged) | A123 to A126 | |
| This record | A127, A128 | **A129** |
