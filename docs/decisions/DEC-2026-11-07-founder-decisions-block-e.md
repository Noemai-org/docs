# DEC-2026-11-07 · Founder decisions E1 to E7 (Block E)

| | |
|---|---|
| **Status** | **Decided by the Founders on 7 Nov 2026 (Block E, added to Block D); recorded by the Repo Steward.** Counts once both Founders approve and merge this pull request (AGENTS §2, item 3). |
| **Date** | 7 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | E1 to E7 in §1, and the open-decision answers of E4 in §2. |
| **Closes** | See §2. OD-P-60 is recorded in docs#130 (PERD §28.2). OD-P-72, OD-P-74 and OD-P-76 close with docs#117 and docs#123, not here. |
| **Amends** | `docs/open-decisions.md` (status lines only). No SoT or PERD text. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 7 Nov 2026; counts once both Founders approve and merge this pull request
- Date: 7 November 2026
- Closes: OD-P-46 to OD-P-51, OD-P-54, OD-P-57, OD-P-59, OD-P-70, OD-P-73, OD-P-75 (decided); OD-P-65, 66, 68, 69 deferred; OD-P-67 handed to Tushe
- Owner: Founder and Technical Co-Founder
- Decision: the tables in §1 and §2, as the Founders gave them
- Rationale and evidence: given in the Founders' message of 7 Nov 2026; the Repo Steward added none
- Affected requirement IDs / SoT sections: none changed
- Migration notes: none
- Supersedes: none. Continues DEC-2026-11-07-founder-decisions-block-d (Block D, on docs#130 until it merges; no link until then).

---

## 1. Rules and assignments

| ID | Decision (as given) |
|---|---|
| E1 | The role that opened a PR is the only one that pushes to it; the `tasks.csv` owner only breaks ties. Others comment. |
| E2 | Reviewer table: SR reviews noema #156 #163 #168 #181 #195 #196 #197 #198 #214 #229 #231 #233 #234 #236 #237 #239 #241 #243 #250 #253 #257 #259 #261 #263 #264. EL: noema #172 #174 #176 #194 #202 #210 #211 #215 #217 #224 #225; docs #108 #111 #114 #115 #117 #118 #120 #122 #123 #127. C2: noema #187 #188 #192 #193 #200 #201 #208 #213 #218 #219 #220 #228 #230. C1: noema #105 #164 #190 #191 #222 #226 #246 #251. Voice: noema #104 #117 #124 #148 #170 #180 #199 #205 #206 #207 #209 #221 #232 #235 #240 #242 #244 #248 #249 #252 #254 #255 #256 #258 #260 #262; docs #99 #113 #119 #121 #124 #125 #126 #128 #129 #130 #131 #132. Each posts READY or numbered findings at the current head within the hour; a role that wrote the PR skips it and tells the Steward. |
| E3 | The audit confuses noema#117 (benchmark runner) with docs#117 (rulings). noema#229 and noema#263 wait for docs#117. The Steward corrects the audit and every "do not merge before" line to say docs#117 or noema#117 in full. |
| E5 | The quota bound is 1 − 0.05^(1/n), one-sided 95%. docs#128 §9: paired design, exact McNemar with Newcombe's interval, 100 stratified decisions for the audit sample, primary comparison C against the best of A, B and D, one primary family per case (other tags are analysis-only and never add to n). |
| E6 | The Steward opens one docs PR flipping "Proposed" to "Decided" on the four merged records. |
| E7 | Unowned PRs: docs#132 to EL; docs#119 and noema#257 to C1; noema#256 to IL; noema#240 to BO; noema#254 duplicates noema#253 (A37): whoever opened noema#254 closes it after confirming noema#253 covers everything. |
| RelayRoute | A temporary `RelayRoute/` folder in `noema` (noema#269) for role-to-role requests; deleted when development is done; independent of every other folder. |

## 2. Open-decision rulings (E4)

| OD-P | Ruling | Register |
|---|---|---|
| 46, 47 to 51 | Accept the stated defaults. | Decided |
| 52, 53, 55, 56, 58 | EL proposes the safer fail-closed reading, SR concurs, the Steward records it today. EL's proposals: comment on docs#129 (issuecomment-6709557558). SR's concurrence: comment on docs#129 (issuecomment-6709854766). **52** no rule yields REJECTED_CONFIRMED until the Tushe worksheet gives the "not debited" and "rejected" values; a missing or unreadable value is never REJECTED_CONFIRMED (INV-19). The *classification* is INSUFFICIENT_EVIDENCE and the *disposition* is UNKNOWN or ESCALATE (SR's wording point). **53** debit KNOWN with credit UNKNOWN or UNAVAILABLE and a non-terminal switch is a non-terminal state (WAIT or ESCALATE), never a success; without the worksheet's switch value the case is UNKNOWN. A WAIT has a deadline after which the case escalates (A31's rule for REVERSAL_PENDING), and no customer text describes the case as failed or succeeded while it is non-terminal (SR's added clause). **55 (amended by SR; EL to confirm)** the POC's synthetic ledger models single-leg transactions only and they are treated as single-leg; no PARTIAL rule is built; a case whose evidence names more than one leg, or a leg count that does not match, is UNKNOWN and escalates. **56** Noema never picks an order by arrival or by a single source's timestamp; a tie, a missing time or sources that disagree hold the case as uncertain and escalate (INV-21, INV-10). **58** accept the three deviations and the certainty tiers (definitive 2, indefinite 1) as written, because each withholds certainty and none grants it (REQ-RES-001); the tiers are numbers decided here and become a safety threshold that agents do not change (REQ-AGT-005). | **52, 53, 56, 58: EL proposed, SR concurred; Decided in the register. 55: SR amended EL's line; the register entry stays [OPEN] until EL confirms the amendment.** |
| 54 | Closed by A31. | Decided |
| 57 | Not allowed under freeze. | Decided |
| 59 | Bind only through a confirmed slot. | Decided |
| 60 | Exit to OPS escalation. | Written into PERD §28.2 in docs#130 |
| 65, 66, 68, 69 | Deferred. | Deferred |
| 67 | Ask Tushe. | Open until Tushe answers |
| 70 | Internal CA. | Decided |
| 71 | Deferred. | Already deferred |
| 72 | Closed. | Closes with docs#117 (A2, A16) |
| 73 | Default: the edge signs for the model service. | Decided (with D6) |
| 74, 76 | Close with docs#123 and docs#117. | Close there |
| 75 | UNKNOWN. | Decided |
| 78 | Default. | Not in the register on `main` yet (docs#132 adds it) |

## 3. Notes by the Steward

- E1 and E7 change who pushes: the Steward pushes only to the PRs it opened (docs#115, 117, 120, 123, 126, 127, 129, 130, and noema#269).
- This record does not mark the Block D record or the Architect's records Decided; E6 does that for the four already merged ones.
