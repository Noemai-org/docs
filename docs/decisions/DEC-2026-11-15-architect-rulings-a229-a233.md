# DEC-2026-11-15 · Architect rulings A229 to A233 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 15 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 15 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Five rulings, A229 to A233 (§1). Each states what it supersedes. |
| **Closes** | The conditional complaint question between noema#594 and noema#588 (A229); the plan binding at the Trust write, noema#572 and noema#603 (A230); the separators of the Record guard, noema#600 (A231); the body limit (A232); the trust limits of noema#574 and the retry conflict of noema#603 (A233). |
| **Supersedes** | Per ruling, in §1. In short: **A229 supersedes A223**; **A232 amends A212** (16384 becomes 32768). |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 15 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A229 to A233
- Decision: §1
- Rationale and evidence: the Architect's message of 15 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-03, INV-05, INV-07, INV-17, INV-22; AGENT-16, AGENT-29; REQ-EXE-003, REQ-EXE-007, REQ-TRU-001, REQ-TRU-008, REQ-TRU-009, REQ-SEC-003, REQ-INP-002; SoT §0.4
- Migration notes: none by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A229** (interim) | **Complaint is always conditional (noema#594, noema#588).** `log_complaint_reference` is irreversible and regulatory, so the case client never has an unconditional path. IL changes noema#594 so the adapter always sends `If-None-Match: *`, and a 412 is typed as "complaint exists". The `IfNone` option disappears. noema#588 then needs no field and keeps its tests. SR's design wins, which supersedes A223. | **A223** (the merge order of noema#594 and noema#588 with an `IfNone` option; recorded in `DEC-2026-11-15-architect-rulings-a223-a228`). |
| **A230** (interim) | **noema#572, plan binding.** The writer refuses an ALLOW whose confirmation's plan hash differs from the plan T14 built. The confirmation spend is single-use in the same transaction (noema#603). C1 implements this at the T15 write. | Nothing committed. It binds the plan at the Trust write (**A205**, Trust plan). |
| **A231** (interim) | **noema#600, separators.**<br>• The Record guard uses the display mask's wide separator set.<br>• The one exemption is an `UPPER_SNAKE` reason-code token with at most 6 digits in total and at most 3 per group. That covers `CONFLICT_409_412` and keeps `X_4111_1111_1111_1111` refused.<br>• A184 covers every outward surface and the Record. The model-service redactor already conforms (noema#468). | Nothing committed. It adds one exemption to the guard (**A193** accepted seven) and fixes the separator set of the one definition of **A194**. |
| **A232** (interim) | `NOEMA_MAX_BODY_BYTES` is 32768. Voice is right that "characters" means code points, and a JSON-escaped astral character takes 12 bytes. 2000 × 12 is 24,000, plus the envelope, which fits in 32768. | **A212** (`NOEMA_MAX_BODY_BYTES` is 16384): amended to 32768. |
| **A233** (interim) | **noema#574 and noema#603.**<br>• For trust limits, zero is refused. The ambiguity floor is at least 7000 (it can only tighten). The at-risk ratio is between 1000 and 5000 basis points. Both are provisional until GOV-06.<br>• For noema#603: a retry that names a different confirmation than the stored decision is refused as a typed conflict. | Nothing committed. It bounds the provisional values of **A205** (Q1: the PERD values as pack data, provisional per GOV-06). |

## 2. What the Steward did where the rulings are silent

- **A229 supersedes A223, which is recorded in docs#182 (open when this record was written).** This record names A223 by text only. Whichever record merges first, both stand: A223 as given, then A229 superseding it. The Steward asks the Founders to merge docs#182 first so the committed history keeps the order the rulings were given.
- **A232 amends A212,** which docs#178 recorded and which is committed on `main`. The A209 to A213 record is not edited in place; this record carries the amendment. Anything that cites 16384 now cites 32768 (noema#577 carries the value as data).
- **A233's at-risk range** (1000 to 5000 basis points) contains the PERD value 25% (2500 basis points, `[REC]`, PERD v1.23 line 2126 and v1.24 line 2146), and the floor "at least 7000" is the PERD floor 0.70. Both stay provisional pack data until GOV-06 adopts them; this record adopts nothing.
- **The `/contracts` v1 tag.** The Architect asked the Steward to confirm its name: it is **`contracts-v1.0.0`** (PERD v1.24 milestone M1 "Contracts v1 frozen: tag `contracts-v1.0.0`; generated types"; ruling A12 of `DEC-2026-11-06-architect-rulings`: tagged after CON-04 and CON-06 are Done, and it means the frozen contract files at the G1 SHA, each schema keeping its own version). G0-N needs it. Tagging is a Founder action; the Steward does not tag. CON-06 was In progress at the last assessment.
- **The G1 target of 15 Nov** is the Founder's order and goes in its own pull request with its own record, not this one.
- **Next free ruling: A234.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A222 (merged); A223 to A228 in docs#182 (open) | |
| This record | A229 to A233 | **A234** |
