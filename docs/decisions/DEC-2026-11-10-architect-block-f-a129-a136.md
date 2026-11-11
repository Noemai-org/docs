# DEC-2026-11-10 · Architect Block F: rulings A129 to A136, and the Founder's decision on the G5 field gate (noema#349)

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 10 Nov 2026 (Block F), and by the Founder (the G5 field gate), relayed to the Repo Steward; recorded by the Repo Steward on 11 Nov 2026.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). **Incomplete: the texts of A129, A135 and A136 were not given to the Steward; §1 says so and records only what was given.** |
| **Date** | 10 November 2026 (decided); 11 November 2026 (recorded) |
| **Owner** | Principal Architect (A129 to A136); Founder (§3, the G5 field gate); Founder and Technical Co-Founder (the merge) |
| **Decides** | A130 to A134 as given; the Founder's G5 field-gate decision (§3). A129, A135 and A136: numbers reserved, text pending (§1). |
| **Closes** | The request on noema#434 (Voice closes it). |
| **Supersedes** | Per ruling, in §1. §3 supersedes PERD §45.4's and REQ-VOI-005's "at least 100 field sessions" **for the G5 field plan only**. |
| **Amends** | One sentence of `DEC-2026-11-10-architect-sync-2-a123-a126` (§4). No SoT, PERD or plan file is edited. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 10 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 10 November 2026 (decided); 11 November 2026 (recorded)
- Closes: the request on noema#434
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A130 to A134 as given; the G5 field-gate decision
- Decision: §1 and §3
- Rationale and evidence: Architect Block F of 10 Nov 2026 and the Founder's decision on noema#349, relayed by the Founder and by Voice on noema#434
- Affected requirement IDs / SoT sections: REQ-AGT-001, REQ-VOI-005; AGENT-14, AGENT-29; INV-12; SoT §0.4; PERD §45.4
- Migration notes: none
- Supersedes: see the Supersedes row above

---

## 1. The rulings (Block F)

| ID | Ruling (as given) | Supersedes |
|---|---|---|
| **A129** | **Text not supplied to the Steward when this record was written; it is now in `DEC-2026-11-11-architect-rulings-a129-a147`.** The only description received then: it narrows A14 for a main-red hotfix. The conditions of the narrowing (who may merge, which reviews, which checks) are not recorded here and **nobody may apply A129 until its text is committed**. | Pending its text. |
| **A130** | **A READY follows the PR's own diff, not its head.** A clean merge of `main`, or a comment-only or status-only commit, keeps every READY. Post the patch-id before and after. Nobody re-reads. | **Generalises D11** (DEC-2026-11-07-founder-decisions-block-d): D11 covered a clean merge of `main` for a Codex READY; A130 covers every READY and also comment-only and status-only commits, and requires the patch-id before and after. |
| **A131** | **Definition of done.** Before posting `READY FOR CODEX at <sha>`, the PR body carries and fills the table in §2. If any row is empty, the task is **not** done. After one `READY FOR CODEX` line, push only to fix a named finding. | **Adds** to the PR-description rules of AGENTS §11 and plan §13.1. Supersedes nothing. |
| **A132** | Any Draft you have not finished: complete it now. **The end-of-day open pull request count must be 10 or less.** | Nothing. It sits beside the plan §5 limit (at most 4 open PRs per driving founder), which is unchanged. |
| **A133** | No polling, no "nothing needs action" messages, no repeated status. If blocked on a named gate, end the turn. Report once, when done or when a human is needed. | Nothing. A process rule for agents. |
| **A134** | **Codex reviews only on one line:** `READY FOR CODEX at <sha>`. | **Narrows A29** (the same line, "the Founders run sweeps") and **bears on A121** (a Founder sweep or the Codex bot at the current head counts): see §5, a question for the Architect. |
| **A135** | **Text now in `DEC-2026-11-11-architect-rulings-a129-a147`.** | Per the record of 11 Nov. |
| **A136** | **Text now in `DEC-2026-11-11-architect-rulings-a129-a147`.** | Per the record of 11 Nov. |

## 2. The definition of done (A131), as given

| # | Row | What fills it |
|---|---|---|
| 1 | **Task card**: every acceptance criterion (done_when, PERD REQ, SoT IDs, rulings) | the test name and the CI link that proves it |
| 2 | **Authority** | you re-read the cited SoT sections, the INV list, AGENTS §5, and every ruling and decision record naming this task; you cite only COMMITTED records; a conflict means stop and raise it |
| 3 | **Classes reviewers found repeatedly, in YOUR diff** | (a) identity, actor and tenant are never caller-supplied (INV-12); (b) every input is bounded and validated (negative, zero, MaxInt, huge, Unicode case-folding) and fails closed on malformed or missing; (c) no swallowed error: every append, IO and DB error path has a test that FAILS when the error is ignored (mutate it and watch the test go red); (d) every SECURITY DEFINER function pins `search_path = pg_catalog, pg_temp` and schema-qualifies, and every new tenant table has RLS plus FORCE (A6); (e) no secret, hostname, oracle or held-out material in code, logs, fixtures, README or status files; (f) every claim in the PR body and README matches the code; (g) contracts follow AGENT-15, and migrations follow the A113 ascending order and have an upgrade-path test; (h) cross-PR interplay: merge current `main` locally, run the full suite, and list every open PR touching the same files |
| 4 | **Run everything you can locally** | read the CI check runs at the head yourself and paste the table |
| 5 | **Only then** | post one `READY FOR CODEX at <sha>`; after that, push only to fix a named finding |

## 3. The Founder's decision on the G5 field gate (noema#349), as relayed

Relayed by the Founder at the Architect sync of 10 Nov 2026 (afternoon) and restated by Voice on noema#434. **Owner: the Founder.**

- **240 field sessions**: 120 in Pidgin, and 30 each in en-NG, Yoruba, Hausa and Igbo.
- **Pooled gate:** correctness at least 90% **and** its lower 95% bound at least 80% (A96).
- **Per-locale floor:** each locale at least 80% (24 of 30), reported per locale.
- **Latency:** a latency claim passes only if the **upper** 95% bound of P95 is at or below the target (A126(b)). The 2.5 s target and the 50% Pidgin rule stay.

**What it supersedes:** PERD §45.4 and REQ-VOI-005's acceptance, "at least 100 field sessions", **for the G5 field plan only**, with the sample size replaced by the plan above. It supersedes nothing else. The text of PERD §45.4 and REQ-VOI-005 is not edited here: if the Founders want the PERD or the SoT text changed, that is a new version file (AGENTS §11).

## 4. Correction to an earlier record

`DEC-2026-11-10-architect-sync-2-a123-a126`, §2, the A126(b) bullet, said A126(b) "does not set the F5 field gate, the session plan or the per-locale floor: those stay the Founder's decision on noema#349". That was true when written. The Founder has since decided (§3), so the sentence is corrected in this pull request to point at §3. The ruling A126(b) itself is unchanged.

## 5. What the Steward did where the rulings are silent, and a question

- **A129, A135, A136.** The Steward did not invent text. The numbers are used; **next free is A137**. The Architect is asked to give the three texts; the Steward adds them in a follow-up pull request that changes only these rows.
- **A134 and A121.** A121 says a Codex review at the current head, from the Founder sweep or the Codex bot, counts, and an unresolved P1 from either blocks. A134 says Codex reviews only on the one line. The Steward reads them together as: Codex reviews are **triggered** by the line; a review that exists at the current diff still counts (A121, A130). The Architect is asked to confirm.
- **A131 and the templates.** The table is recorded here. Putting it into `docs/poc/execution/templates/pr-checklist.md` is a separate change; the Steward asks the Architect whether to do it now.
- **A130 and the patch-id.** "Post the patch-id before and after" means `git patch-id` of the PR's own diff against `main`. The Steward uses that reading.

## 6. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109 to A112 | REC-09, control-plane callers, one non-author Founder approval, DEBT-13 and SEC-15 | |
| DEC-2026-11-10-architect-sync-a113-a122 (merged) | A113 to A122 | |
| DEC-2026-11-10-architect-sync-2-a123-a126 (merged) | A123 to A126 | |
| DEC-2026-11-10-architect-sync-3-a127-a128 (docs#152, merged) | A127, A128 | |
| This record | A129 to A136 (A129, A135, A136 pending text) | **A137** |
