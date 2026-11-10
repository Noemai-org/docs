# DEC-2026-11-10 · Architect sync of 10 Nov 2026 (after Codex sweep noema#423): rulings A123 to A126

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 10 Nov 2026 (the second Architect sync, after Codex sweep noema#423), relayed to the Repo Steward by the Founder; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 10 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Four rulings, A123 to A126 (§1). Each states what it supersedes. |
| **Closes** | Nothing by itself. It gives the authority the Codex findings on noema#272, noema#358 and noema#193 ask for (noema#423). |
| **Supersedes** | Per ruling, in §1: A124 replaces the "design review only" part of A29; A123 and A126 supersede nothing earlier that is committed; A125 supersedes nothing. |
| **Amends** | Nothing in the SoT, the PERD or the plan. The AGENTS.md §11 sentence on P0 reviews and plan §4 are applied as A123 states; a wording change to them is a separate change. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 10 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 10 November 2026
- Closes: nothing by itself
- Owner: Principal Architect; Founder and Technical Co-Founder
- Decides: rulings A123 to A126
- Decision: §1
- Rationale and evidence: the Architect sync of 10 Nov 2026 after Codex sweep noema#423, relayed by the Founder
- Affected requirement IDs / SoT sections: REQ-AGT-001; AGENT-14, AGENT-29; SoT §0.4
- Migration notes: none; A123 makes the migrations of the A113 chain P0
- Supersedes: see the Supersedes row above

---

## 1. The rulings

| ID | Ruling | Supersedes |
|---|---|---|
| **A123** | **The P0 second-review rule.** A P0 pull request needs two human reviews from two of EL, C1 and C2. **The author never counts.** The pair is EL plus C1 or C2, unless EL authored the pull request. **Migrations in the A113 chain are P0.** | Nothing committed. It states how "EL plus C1 or C2" (AGENTS §11; plan §4) applies when EL is the author and when the author is C1 or C2. |
| **A124** | **A stacked child may get a Codex READY on its own commit range**, with a commit-group map, and that READY **carries after the parent merges** (D11 of DEC-2026-11-07). | **The "design review only" part of A29** (stacked pull requests get design review only until the parent merges). The rest of A29 stands. |
| **A125** | **noema#156 merges only after noema#198 has every READY except the parent's, and noema#198 merges the same day.** | Nothing. |
| **A126** | **(a)** noema#193 may merge on DEBT-14, DEBT-15 and DEBT-24, with VOI-01 recorded as blocked on vendor documents. **(b)** Latency passes on the upper bound of its interval; correctness passes on the lower bound. **(c)** noema#272 cites Block D D10 (DEC-2026-11-07-founder-decisions-block-d); noema#358 cites A116 once docs#148 is merged. | Nothing committed. (a) is the one recorded exception to the AGENTS §3 rule that every Needs task is Done. |

## 2. What the Steward did where the rulings are silent

- **Numbering.** A113 to A122 are in docs#148 (open). This record is numbered after them; next free is **A127**. If docs#148 changes a number, this record moves with it.
- **A123 and the gate.** The ruling does not name which roles review when C1 or C2 is the author. The Steward reads "two of EL, C1, C2, author excluded" literally. The Steward asks EL to confirm on the pull request that adds the first P0 review under it.
- **A124 and what counts.** A commit-group map is a list of the child's own commits grouped by purpose, posted on the pull request. The Steward does not lower any A14 requirement: the Codex READY must be at the current head or carry by D11 (clean merge of `main`, own diff unchanged, CI green).
- **A126(b).** The ruling names no gate and no number. It does not set the F5 field gate, the session plan or the per-locale floor: those stay the Founder's decision on noema#349. The Steward changes no threshold.
- **A126(c).** noema#358 stays blocked on A116 until docs#148 merges; A116 is recorded there.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109, A110, A111, A112 | REC-09, control-plane callers, one non-author Founder approval, DEBT-13 and SEC-15 | |
| DEC-2026-11-10-architect-sync-a113-a122 (docs#148, open) | A113 to A122 | |
| This record | A123 to A126 | **A127** |
