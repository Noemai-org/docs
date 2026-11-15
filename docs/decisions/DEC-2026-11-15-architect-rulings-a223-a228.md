# DEC-2026-11-15 · Architect rulings A223 to A228 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 15 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 15 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Six rulings, A223 to A228 (§1). Each states what it supersedes. |
| **Closes** | The conflict between noema#588 and noema#594 (A223); the review questions on noema#576 (A224); the T10 to T12 questions of the Trust assembly (A225); C1's carried notes on noema#567 and #571 (A226); the bench certificate keys of noema#568 (A227); C2's and EL's small questions on noema#596, voice confidence and noema#591 (A228). |
| **Supersedes** | Per ruling, in §1. In short: A224 and A225 refine **A216** and **A218**; A228 repeats **A220** for noema#591 without change. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 15 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A223 to A228
- Decision: §1
- Rationale and evidence: the Architect's message of 15 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-03, INV-07, INV-08, INV-19, INV-22; AGENT-14, AGENT-16, AGENT-29; REQ-EXE-003, REQ-EXE-007, REQ-STM-001, REQ-TRU-001, REQ-SEC-003; SoT §0.4
- Migration notes: none by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A223** (interim) | **noema#588 versus noema#594.** #594 (the adapter's `IfNone` option) merges first, after an independent read by EL or C2. Then #588 merges `main` and sets `IfNone: true` for the complaint capability, with a test that removing it fails. Codex and C1 were looking at different bases. | Nothing committed. It orders the work of **A185** (conditional complaint create) and the EXE-09 follow-up. |
| **A224** (interim) | **noema#576.** `COMPENSATED` stops the run exactly as `UNKNOWN` does (A68: no retry). EL fixes the runner and the test. When a key's dispatches reach 2, Trust itself decides `ESCALATE` through the existing arrows. The runner's refusal is only the backstop. | Nothing committed. It refines **A216** (the write-path rules of noema#576) and applies **A68**. |
| **A225** (interim) | **T10 to T12.**<br>• Reads continue on a frozen target. Only writes are refused, as a typed refusal, not an internal error.<br>• If the pack's routing omits a breached clock, T12 escalates by itself.<br>• A Partial classification is unsettled and fails closed. | Nothing committed. It refines **A218** (the T10 split): a Partial classification is unsettled and fails closed. |
| **A226** (interim) | **Notes carried by C1.** In the next push to each PR:<br>• Compare the intent's correlation ID with the request's (noema#567).<br>• Verify that T9's snapshot belongs to this intent and refuse a negative evidence age (noema#571). | Nothing committed. |
| **A227** (interim) | **noema#568.** Bench certificate keys at mode 644 in a 711 directory are accepted. The CA key is deleted and the keys are throwaway. A debt entry records the production secrets plan. | Nothing committed. It is a bench-only exception to the file-mode care of the secrets practice (AGENTS §10); the production plan is the debt entry. |
| **A228** (interim) | **Small answers.**<br>• noema#596: the Reconciler takes a `PayloadReader` port. EL implements it over the Trust pool in `cmd/core`. `layer.Item` already carries `payload_ref`.<br>• Voice confidence for the low-ASR rule is the minimum over tokens in basis points, with a missing token counted as 0. Voice stays refused in G1.<br>• A220 (for noema#591): a foreign-tenant token gets 401 `SESSION_INVALID` and a wrong-role session gets 404. The seed, cost and latency integer fields are exempt by type under A154. | Nothing. The third bullet **repeats A220** (recorded in `DEC-2026-11-14-architect-rulings-a214-a222`) word for word in substance. The voice rule is consistent with **A191** (a missing confidence counts as low). |

## 2. What the Steward did where the rulings are silent

- **A226 names noema#567 and noema#571, which have merged.** Both were merged before this record was written (read on GitHub on 15 Nov). The notes cannot go "in the next push to each PR". **They go into C1's next Trust pull request** (noema#572, or a follow-up if C1 prefers); the Steward asks C1 on noema#572 to carry them and the Architect to correct this reading.
- **A227 asks for a debt entry.** It is a docs change to `debt.md`, which the open pull request docs#180 (DEBT-36) also edits; per AGENT-29 and to avoid a stacked conflict it goes in its own small pull request after docs#180 merges. Proposed: DEBT-37, bench certificate keys (mode 644 in a 711 directory, throwaway, CA key deleted), owner IL, removal condition the production secrets plan (OQ-09, PLT-05), expiry before any non-bench profile (a Steward default).
- **A223 and the independent read.** The independent read of noema#594 by C2 is on the pull request at `94a697ad` (read on GitHub on 15 Nov). Whether that satisfies A223 is for the Founders and the Architect; the Steward records only that it exists.
- **A228 repeats A220.** No conflict; the Steward records the repetition so the two records agree.
- **The reader assignments (§5 of A213, §6 of A222) are still not given to the Steward.** The Architect is asked again to post them on noema#183.
- **Next free ruling: A229.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A208 (merged); A209 to A213 in docs#178 and A214 to A222 in docs#181 (open) | |
| This record | A223 to A228 | **A229** |
