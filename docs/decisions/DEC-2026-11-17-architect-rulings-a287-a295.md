# DEC-2026-11-17 · Architect rulings A287 to A295 (interim, effective now)

| | |
|---|---|
| **Status** | **Interim, effective now.** Decided by the Principal Architect, relayed to the Repo Steward on 17 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). A290 and A291 carry the Founder's own decisions as the Architect relayed them. |
| **Date** | 17 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Nine rulings, A287 to A295 (§1). They remove review steps that slow the queue without adding safety (the Architect's words). |
| **Closes** | The settle rule for findings (A287), the third tier (A288), the noema#457 owner and the push-to-a-stuck-PR rule (A289), the X5 cost (A290), PRE-03 (A291), the injection detector's home (A292), PCK-05 (A293), noema#629 (A294) and the Codex lanes (A295). |
| **Supersedes** | Narrows **A178** (A287), adds a tier to **A143** (A288), replaces BO's USD 11 (A290), refines **A269** (A295). Per ruling, in §1. |
| **Amends** | Nothing in the SoT or the PERD. The review text in `AGENTS.md` §11 and plan §4 is not edited here (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim, effective now; counts on merge by a non-author Founder (A111)
- Date: 17 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A287 to A295
- Decision: §1
- Rationale and evidence: the Architect's message of 17 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, AGENT-09, AGENT-14, AGENT-16, AGENT-29; REQ-CTX-007; SoT §0.4
- Migration notes: none for contracts. A291 changes `tasks.csv` (PRE-03 Done, ENV-01 Ready)
- Supersedes: see the Supersedes row above

## 1. The rulings, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A287** (interim) | **Settle rule.** When a finding is verified as real, fixed, and the fix has a test that failed first plus CI green, the pull request is settled. Nobody re-reads the whole head. The reviewer who raised it checks only the fix lines. Often the agent's own proof (the red-then-green test) is enough. A P2 outside the changed lines becomes a tracked follow-up, not a blocker. P1s and anything that weakens an invariant still block. A P2 that needs a deliberate evasion of a hygiene guard (not a runtime boundary) is also a tracked follow-up. On a merged guard, the next hole found becomes the next small pull request. | Narrows **A178** (a reviewer READY at the same head does not close an inline P1): a settled finding no longer needs a re-read of the head. P1s and invariants are unchanged. |
| **A288** (interim) | **Tier 3.** Docs-only, status, task-card, test-only and tooling pull requests that touch no runtime path need Codex, CI and one Founder approval. No SR and no independent read. | Adds a third tier to **A143**. Tier 1 and Tier 2 stay as written (§2 says how the Steward reads the edge). |
| **A289** (interim) | **Ownership.** C1 takes over the noema#457 fix, because the shared digit definition is C1's anyway. Any agent may push a verified fix to a stuck pull request when its owner is mid-task. The push is one commit with a comment naming the finding. | Allows a push to another role's branch under that rule; **AGENTS §11** (no rewrite of published history, no force-push) is unchanged. |
| **A290** (interim) | **X5 cost.** The ceiling is USD 5 (the Founder's decision), the same as the compile run, with gpt-6-luna. BO's USD 11 is withdrawn. | Replaces BO's USD 11 proposal. Does not change the compile run's cap. |
| **A291** (interim) | **PRE-03 is Done.** The Founder's session with Tushe was the kickoff. The Steward marks it with the Founder's statement and the addendum as evidence. IL's ENV-01, 03, 05, 06 and 16 chain starts now. | Reads PRE-03's done-when ("both invites accepted by Tushe") as met by the kickoff session. ENV-01 loses its only Need. |
| **A292** (interim) | **Injection detector (REQ-CTX-007).** It lives in the core, in the evidence layer, because the core writes the Record. Its patterns are pack data in `packs/fintech/context/injection_patterns.v1.json`. It is advisory only: it raises a security event in the Record and never decides anything (INV-01, AGENT-09). | Nothing committed. Fixes the home of REQ-CTX-007's detector and its data file. |
| **A293** (interim) | **PCK-05.** It is a week-7 task and off the G1 path. EL does not pick the values (AGENT-16). Skip it for now. | Nothing committed. PCK-05 stays Backlog. |
| **A294** (interim) | **noema#629.** Its three remaining P2s are deliberate YAML evasions of a hygiene guard under CODEOWNERS review. They are tracked under noema#667 (the parser). The parser is the real fix. The Founder adds the approval of PyYAML on issue #667 (the comment "approved: PyYAML, hash-pinned, safe_load, safeguards job only"). #629 merges now. | Applies **A287** and **A283** to #629. The PyYAML approval is the Founder's to post (AGENT-14); this record does not stand in for it. |
| **A295** (interim) | **Throughput.** Codex is the single-lane bottleneck, with 22+ pull requests per sweep. Start a second Codex session. One takes `.github`, tools, docs, benchmark and voice. The other takes core Go and the model service. Read order matters: Codex reads unread pull requests first, ahead of re-reads of settled ones. | Refines **A269** (Codex reads only changed heads). |

## 2. What the Steward did where the rulings are silent

- **A287 and A288 take effect from this record**, because the Architect said "effective now". `AGENTS.md` §11 ("Reviews") and plan §4 still describe Tier 1 and Tier 2 only. The Steward does not edit them in this pull request: `AGENTS.md` is vendored into noema, and a change on docs `main` turns noema's `drift` check red until the copy is re-pointed (it did on 16 and 17 Nov). The wording change and its noema re-point are one change set, opened when the Founders say. Meanwhile this record outranks `AGENTS.md` (SoT → decision records → PERD → plan; AGENTS §2, item 9).
- **A288 on the edge.** "Tooling that touches no runtime path" includes `tools/` and test-only changes. A `.github/workflows` change that can spend money or hold a secret (for example `bench-live-compile.yml`) is read as runtime-adjacent and keeps SR until the Architect says otherwise.
- **A291.** PRE-03 is marked Done in `tasks.csv` in this pull request, with the Founder's session and the Tushe addendum of 15 Nov (`docs/poc/tushe/responses/2026-11-15-tushe-addendum-to-reply-of-10-nov.pdf`, docs#188) as the evidence. The done-when text says "both invites accepted"; A291 reads the kickoff session as meeting it. ENV-01 loses its only Need (PRE-03) and moves to Ready. ENV-03, ENV-05, ENV-06 and ENV-16 stay blocked on the chain, in order.
- **A294.** The Steward does not post the Founder's PyYAML approval on noema#667 and does not merge #629. The comment is for a Founder to post.
- **Audit issues noema#605, #607 and #637** are not closed here: the Founders' dispositions were not in the message (see the pull request).
- **Next free ruling: A296.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A286 (A278 to A286 in docs#197) | |
| This record | A287 to A295 | **A296** |
