# DEC-2026-11-07 · Architect's rulings A27 to A40

| | |
|---|---|
| **Status** | Proposed for the Founders. The Architect gave these rulings in a work order of 7 November 2026 (Block C) and they are recorded here as given. An instruction given in a session is not authoritative until committed (AGENTS §2, item 3). They count once both Founders approve and merge this pull request. |
| **Date** | 7 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | The rulings in §1. |
| **Amends** | None by this record. A27 asks for SoT and PERD edits; those are a separate pull request that the Founders issue as a version (AGENTS §11). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; counts once both Founders approve and merge this pull request
- Date: 7 November 2026
- Decides: the rulings in §1
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: the Architect's work order of 7 November 2026 (relayed to the Repo Steward). This record adds no rationale the Architect did not give.
- Affected requirement IDs / SoT sections: per row
- Migration notes: per row; no merged migration or frozen record is edited
- Supersedes: None. A32 amends the Proposed A26 record (docs#127) before it merges.

The work order has no A33.

---

## 1. The rulings

| ID | Ruling | Tasks and sources it touches |
|---|---|---|
| A27 | **The Repo Steward drafts one SoT/PERD edit pull request.** It closes OD-P-72 (A2), A11 and D7 (A1); adds credential leakage and cross-tenant exposure as safety gates; aligns the SoT arm labels; amends the PERD §48.1 quota; and carries the case-contract major version. The Founders issue the version. docs#117, docs#115 and docs#127 then get a reviewer-role READY. | SoT §38.3, §38.5, §46, Appendix D; PERD §48.1, §48.2; OD-P-72, OD-P-76; DEC-2026-11-06 A2, A11; DEC-2026-11-05 D7; AGENTS §11 |
| A28 | **docs#112 is closed in favour of docs#123.** | docs#112; docs#123; A23 |
| A29 | **One fix matrix per pull request** (finding, commit, regression test, final-head checks), then one line `READY FOR CODEX at <sha>`. The author does not trigger Codex; the Founders run sweeps. Stacked pull requests get design review only until the parent merges, and a final review after `main` is merged in. Docs-only and data-only pull requests need CI plus a reviewer-role READY from a role that did not write them. | AGENTS §11; A14 |
| A30 | **TST-05 is option B:** a Go test with a real SIGKILL and no new CI job. There is one kill-point list, shared with RESOLVE/RESIST S9. | TST-05; noema#147; DEC-2026-11-07 A26 (S9) |
| A31 | **`REVERSAL_PENDING` is non-terminal.** It is never SUCCEEDED, FAILED or REVERSED. A decision on it is wait or escalate. | REQ-OUT-*; INV-07; AGENT-21 |
| A32 | **Suite scope (amends the A26 record).** R6 and R12 mean "correct handling the pack allows"; tools, policy and limits come from the pack. The arms use the SoT labels. There are 40 visible cases, chosen by a recorded seed. The Brief is issued at G3 evidence acceptance. | DEC-2026-11-07 A26; SoT §38.5; INV-22 |
| A34 | **Migration numbers are allocated in merge order on the noema#183 ledger.** The second pull request to merge merges `main` in and renumbers. | DEC-2026-11-05 D3; noema#183 |
| A35 | **DEBT-16 is docs#119 (unrun shell tests) and DEBT-17 is docs#121.** Everything else takes the next free number. TRU-08 is registered as debt. | debt register; REQ-OPS-004; AGENTS §7 |
| A36 | **noema#212 is closed (ported to noema#199).** noema#246 is an adjudication list. | noema#199, #212, #246 |
| A37 | **`ops_agent` becomes `ops`, and `viewer` becomes `audit` (read-only), in the pack.** | DEC-2026-11-06 A15; DEC-2026-11-05 D7 |
| A38 | **The script job for `test_init.sh` and `test_secrets_local.sh` runs against PostgreSQL 17.11.** | DEBT-16 (docs#119); PLT-06 |
| A39 | **One owner per pull request,** from the `tasks.csv` owner column. Only the owner pushes; others comment. | AGENTS §11; tasks.csv |
| A40 | **Reconstruction is reported as "consistent, not authenticated"** until slice B and REC-08. There is no headline safety claim below n = 300. There is one shared kill-point list. | REC-03, REC-08; DEBT-03; DEC-2026-11-07 A26 |

## 2. Notes for the people who act on these rulings

- **A27.** The Repo Steward drafts; the Founders issue the version. The draft is a pull request that bumps the SoT (Appendix D entry), adds a PERD version file and a decision record, and regenerates the derived files. Where the work order does not give the text of a change, the draft says so and does not invent it (AGENT-02).
- **A28.** The Repo Steward does not close pull requests (charter §3). The Founders close docs#112 unmerged; docs#123 is the merge target (A23 execution note).
- **A29.** From now on the Repo Steward posts the fix matrix and the single line on each pull request it owns, and does not request Codex. A reviewer-role READY from a role that did not write the pull request is still needed on a docs-only pull request.
- **A31.** `REVERSAL_PENDING` needs a pack and contract entry; the outcome states are owned by Core Engineer 1 and Core Engineer 2.
- **A34.** The ledger lives in the body of noema#183. A migration number is taken at merge, not at branch time.
- **A35.** The debt register is the Repo Steward's to keep. TRU-08 is filed as DEBT-18 (Founder decision of 7 Nov 2026, Block E: Voice's barge-in debt is DEBT-24 in docs#118, so DEBT-18 is free for TRU-08; DEBT-12 and DEBT-13 are mine, in docs#123 and docs#117; DEBT-14 and DEBT-15 are the Voice Engineer's in docs#118, with barge-in as DEBT-24; DEBT-16 is docs#119 and DEBT-17 is docs#121; DEBT-20 to DEBT-23 are the Engineering Lead's in docs#131), Tier 1 proposed, with the wording flagged for its owner to correct.
- **A39.** The `tasks.csv` owner column names the owner of a task. The Repo Steward reads it as the owner of the pull request that carries the task.
- **A40.** The wording "consistent, not authenticated" is used by every report of reconstruction until the two named items land.
