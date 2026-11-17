# DEC-2026-11-17 · Architect rulings A296 to A305 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 17 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 17 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Ten rulings, A296 to A305 (§1). |
| **Closes** | EL's Temporal TLS, PLT-09 and SSE questions (A296), C1's EXE-06, TRU-08, TRU-10 and RCV-02 questions (A297), the UI-05 numbers, noema#677, #682 and #696 (A298), the outbox (A299), the BEN-12 table (A300), noema#640's gitleaks lines (A301), the red-evidence wait (A302), the Tier 2 read (A303), the three audits and the AGENTS.md wording set (A304) and the tamper signal (A305). Closes the audit issues noema#605, #607 and #637. |
| **Supersedes** | **A302** replaces the wait of **A175**/**A176**; **A303** relaxes **A143** Tier 2; **A304** withdraws the AGENTS.md re-point offered in the A287 to A295 record. Per ruling, in §1. |
| **Amends** | The plan: the TRU-08 row is corrected in plan v1.22 (CR-2026-11-17-D8-tru08-row). Nothing in the SoT or the PERD. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 17 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A296 to A305
- Decision: §1
- Rationale and evidence: the Architect's message of 17 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-03, INV-30; AGENT-11, AGENT-14, AGENT-16, AGENT-29; REQ-TRU-005, REQ-RCV-002, REQ-EXE-006, REQ-VER-005, REQ-UI-001; PERD §23.1, §28.2 (E4); SoT §0.4
- Migration notes: none for contracts. Plan v1.22 carries the corrected TRU-08 row; `tasks.csv` regenerated
- Supersedes: see the Supersedes row above

## 1. The rulings, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A296** (interim) | **EL.** Temporal TLS: IL adds Temporal TLS to the Compose bench profile, and EL's "refuse plain" test follows it. PLT-09 is an approved tool. It is in the plan row and PERD v1.19 (golangci-lint, mypy, Ruff). EL opens it with versions pinned by hash, and SR reads it because it touches `.github`. SSE: start the rewrite now against a Feed interface. It does not wait on 0029. | Nothing committed. Settles AGENT-14 for PLT-09's tools (they are in the plan row and the PERD). |
| **A297** (interim) | **C1.** EXE-06: build the Trust refusal and the PUS-06 test now. The listener is a separate task. TRU-08: Block D, D8 (lazy void at execution, E4) stands over the plan row. Add the end-to-end two-version test. The Steward corrects the row by change request. TRU-10: PERD §23.1 (adopted) defines it. An action decision is the per-write-step decision. An ESCALATE disposition authorises only the escalation plan's write steps (create case, record evidence, route). The set comes from the pack's escalation plan. RCV-02: A216 stands. When the budget is spent the runner goes to HANDED_TO_TEAM with the Record-derived hand-off. No new "evidence packet" is invented. Build it after noema#572. | TRU-08 row corrected in plan v1.22 by CR-2026-11-17-D8-tru08-row. A216 confirmed. The "listener" has no task row: see §2. |
| **A298** (interim) | **FE.** UI-05 shows the numbers exactly as scorecard-view gives them. No rounding and no derived values. C1 adds the generated scorecard-view TS parser (noema#677) and fixes the invalid conditional fixtures in noema#682, because a misleading verified badge is a defect. noema#696: the Architect approves in principle react, react-dom and esbuild, pinned exactly, in `ui/` only. The Founder approves by comment. | Applies the contract of **A250**/**A267** (`scorecard-view.v1`). The dependency approval is the Founder's to post (AGENT-14); this record does not stand in for it. |
| **A299** (interim) | **Outbox (C2).** PLT-08 splits: 08a is the outbox, and 08b is the HMAC callback (REQ-VER-005), done later. No retry cap in this pull request (a cap is a policy number, AGENT-16). Failing events retry every pass, which is the safe direction. A poison-event alert is DEBT-45 (owner C2), due before G3. Migration 0031 stands. Tier 1. | Opens DEBT-45. The plan split is not registered here: see §2. |
| **A300** (interim) | **BO.** The BEN-12 G2 table has one row per user story plus a by-family rollup, built from case-level judgements and the manifest as a pure function. A290 is recorded in docs#200, which is waiting for Codex and a Founder's approval. | Nothing committed. |
| **A301** (interim) | **Voice.** The two `.gitleaksignore` lines for noema#640 are approved, each with a reason: synthetic test strings in earlier commits. | An exception to AGENTS §10 (no secret in the repository): approved line by line, with the reason in the file. |
| **A302** (interim) | **Red evidence.** Concurrency cancel is on, so the full red run is cancelled as soon as the agent pushes. The red proof is the failing job (the shard or static job) of the new tests, read the moment that job completes. After that the agent pushes green at once, with no need to wait for the rest of the red run. AGENT-11 stays. | **Replaces** the wait of **A175**/**A176** (a full red run read before the fix is pushed). A176's other rules (one push per fix round, merge main only for a conflict) are unchanged. |
| **A303** (interim) | **Reads.** The independent read for Tier 2 can be one line from any named reader, posted proactively. Fixed findings follow A287. The reader checks only the fix. | Relaxes the independent read of **A143** Tier 2; follows **A287**. |
| **A304** (interim) | **Steward.** The A288 edge reading is confirmed: `.github` workflows that spend money or hold secrets keep SR. The audits noema#605, #607 and #637 are closed as accepted one-time exceptions. The AGENTS.md wording set is skipped for now, because the decision record outranks it. | Confirms the Steward's reading in the A287 to A295 record (§2). Closes three audits. Withdraws the AGENTS.md re-point set offered there. |
| **A305** (interim) | **DEBT.** C2's hash-mismatch tamper signal is DEBT-44, owner C2 with SR, due before G3. | Opens DEBT-44 (noema#663: a stored payload that no longer matches its hash becomes UNKNOWN silently). |

## 2. What the Steward did where the rulings are silent

- **TRU-08 (A297).** Corrected in plan v1.22, in this pull request, by CR-2026-11-17-D8-tru08-row (v1.22 is not yet on `main`, so it is edited rather than versioned again). The corrected row follows D8 only: no eager void, void at execution (E4) with `POLICY_SUPERSEDED`, only `execution_rw` writes `decision_grant.status`, AT_ADMISSION rules keep their admission version, the two-version test added. **A difference the Steward is not resolving:** the PERD's policy-publication text still says publication "marks every unspent grant governed by an earlier version of that policy VOID". D8 says no document change; the CR asks the Architect whether PERD v1.25 rewords it.
- **PLT-08 split (A299): not registered.** The ruling says "08a" and "08b". The plan row PLT-08 names owner C1 while the ruling heads the outbox "(C2)", and the PR trace check (`tools/ci/check_pr_trace.py`) reads a fixed list of prefixes followed by two digits and a word boundary, which does not accept `PLT-08a`. The Steward needs the owner of each half and an answer on the ID form (for example PLT-08 stays the outbox and a new ID is the callback) before changing the plan. Until then PLT-08 is the outbox.
- **EXE-06's listener (A297).** "The listener is a separate task." No plan row names it. The Steward does not invent one; the Architect or C1 names it and its Needs.
- **DEBT-44 and DEBT-45** are in the debt register in this pull request (A305, A299), owner C2 for both, due before G3, Tier 2 proposed.
- **The AGENTS.md wording set is skipped (A304).** `AGENTS.md` §11 and plan §4 still describe Tier 1 and Tier 2 only; the A287, A288 and A303 changes apply from the decision records, which outrank `AGENTS.md`.
- **Audit issues noema#605, #607 and #637** were closed on 17 Nov with this disposition. The cause stands: the branch rule on noema `main` still reads 0 required approving reviews with approval of the most recent push off (read 17 Nov). Changing it is a Founder's setting (docs#38).
- **`tasks.csv` refresh from merges.** Six pull requests merged since the last refresh (noema#629, #622, #641, #642, #587, #660). Checked against the done-when text: PLT-02, SEC-11, BEN-30 and OPS-07 are already Done; #660 is STM-04's task card, not the task; PLT-05 ("no secret in the repository; scan clean") is not met by #622 alone. No status changes.
- **Next free ruling: A306.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A295 (A278 to A295 in docs#197 and docs#200) | |
| This record | A296 to A305 | **A306** |
