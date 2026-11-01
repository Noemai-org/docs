# Change request: CR-2026-11-01-GOV-30 · Re-baselined gate dates (proposal)

- **Change ID:** CR-2026-11-01-GOV-30
- **Requester:** Engineering Lead (role agent, for the EL role of plan §4), under DEC-2026-10-31-proof-depth-and-completeness D32 and plan task GOV-30. **This is a proposal.** It sets no date: the Founders record dates in the gate records (D32; plan §3.1 gate rules). Started on the Architect's instruction of 1 Nov 2026, from docs#77's counts, before docs#77 merged. **docs#77 merged on 1 Nov 2026 (`90bba64`); the counts on `main` are unchanged** (25 Done, 3 In review, 48 In progress, 18 Ready, 152 Backlog, 15 Unassessed), so nothing below changes. D32's two working days from OPS-09 end on Tue 3 Nov 2026.
- **Date:** Sunday 1 November 2026 (WAT).
- **REQ IDs affected:** none changed. Plan v1.10 §3 (calendar), §3.1 (gate dates), §11 (code freeze), §14 (demo), §16 (SR-03, SR-24, SR-25); tasks GOV-07, GOV-12, GOV-13, GOV-16, ENV-14, REL-01, DEM-02 and every dated row; gate records G0-N to G7.
- **SoT IDs:** SoT §40.2 (gates never move, dates do), §38.5 (no comparison arm before G3); DEC-2026-10-16 E3, E4.

## 1. Behaviour before

The plan v1.10 dates are:

| Gate | Date |
|---|---|
| G0-N | Thu 22 Oct 17:00 |
| G0-T | Date never confirmed by Tushe |
| G1 | Evidence Fri 23 Oct; review Mon 26 Oct 10:00 |
| G2 | Fri 30 Oct 16:00 |
| G3 | Fri 6 Nov 16:00 |
| G4, G5 | Wed 11 Nov |
| G6 | Thu 12 Nov 18:00 |
| Demo (G7 dry run 09:00) | Fri 13 Nov 14:00 |
| Code freeze | Wed 11 Nov 12:00 |

G0-N, G0-T, G1 and G2 have not been held. DEC-2026-10-31 added 35 tasks (now 261).

## 2. Evidence used

**Source.** The evidence is docs#77 (OPS-09, the Repo Steward's evidence-based assessment) at head `0c5897d` (1 Nov 2026, 13:55 UTC). Its counts are 25 Done, 3 In review, 48 In progress, 18 Ready, 152 Backlog and 15 Unassessed: 261 tasks, the counts the Architect gave. Not Done: **230 tasks**, leaving out the 6 `AFTER` rows.

**What each gate needs.** For each gate I took the tasks that deliver it and every task they need, transitively, through the `needs` column:
- G1: BEN-05, REC-03, OUT-01, EXE-02, TST-01 and the rows marked G1.
- G2: the "Delivered by" tasks of its 15 stories (plan Appendix D) and the rows marked G2.
- G3: week-3 rows, rows marked G3, and the tasks of US-04, US-09, US-12, US-16 and US-17.

Each gate's count below leaves out tasks already counted for an earlier gate.

**Units.** A task that is Backlog, Ready or Unassessed counts 1 unit. One that is In progress or In review counts ½.

| Gate | New tasks not Done | Of which In progress or In review | Blocked (docs#77) | Units |
|---|---|---|---|---|
| G1 (incl. G0-N) | 23 | 12 | ENV-01, ENV-03, ENV-05 (Tushe-dependent work paused by the Founder, 25 Oct) | 17 |
| G2 | 34 | 16 | EXE-04 (held for DEBT-01) | 26 |
| G3 | 78 | 11 | — | 72.5 |
| G4 to G7 and the rest | 95 | — | ENV-04, ENV-07, ENV-10, ENV-11, ENV-12 (Tushe), GOV-22 | 95 (an upper bound: not every row gates G4 to G7) |

**Throughput, measured.**
- 25 tasks are Done. 5 of them are week-0 governance rows, so about **20 build tasks were finished in the 10 working days from Mon 19 to Fri 30 Oct: 2 a day**. That is the base rate.
- The higher rate, **3 a day**, assumes the seven role agents started on 31 Oct raise output by half. That is an assumption, not a measurement. G1 is where it is tested (§5).
- Calendar: working days, Monday to Friday. Saturdays stay recovery-only (plan §3). Fri 25 Dec, Mon 28 Dec (Boxing Day observed) and Fri 1 Jan are excluded.

| Rate | G1 evidence ready | G2 ready | G3 ready | G4 to G7 ready |
|---|---|---|---|---|
| 2 tasks a day (measured) | Thu 12 Nov | Tue 1 Dec | Tue 26 Jan 2027 | Fri 2 Apr 2027 |
| 3 tasks a day (assumed) | Mon 9 Nov | Fri 20 Nov | Tue 29 Dec | Fri 12 Feb 2027 |

**What the method does not capture:**
- It ignores the critical-path length, which is short for G1: BEN-05 needs OUT-01 and REC-03.
- It treats every task as the same size.
- It cannot see the unassessed external rows (PRE-03 and the like).

It is a planning estimate, not a forecast with a confidence interval, and must not be quoted as a number outside the team (AGENT-18).

## 3. Behaviour after (proposed dates, for the Founders to record)

| Gate | Proposed date (WAT) | Condition that holds it |
|---|---|---|
| **G0-N** | **Fri 6 Nov 17:00** | **Founder decision needed (§4, item 1).** ENV-14 needs ENV-05 (the remaining adapters), which is blocked by the 25 Oct pause. If the pause stays, G0-N is **BLOCKED**: G1 evidence is recorded but does not count (E4), and the G1 review (GOV-07, which needs ENV-14) cannot be held |
| **G0-T** | **No date proposed** | Tushe confirms it (SR-24). G1 and later evidence counts only once G0-T passes |
| **G1** | Evidence **Wed 11 Nov**; review **Thu 12 Nov 10:00** | Between the two rates. Needs CON-03, EXE-01, PLN-01, TRU-05, REC-03, OUT-01 and BEN-05, all not Done. The cut-line trigger of plan §2 (items 4 and 5) already fired, because G1 had not passed by 26 Oct; the Founders apply it at this review |
| **G2** | **Fri 27 Nov 16:00** | Between 20 Nov and 1 Dec. US-19 needs EXE-04, which is held until DEBT-01 closes (GOV-28 → EXE-07 → EXE-08 → SEC-13). If DEBT-01 is not closed, US-19 fails and so does G2 |
| **G3** | **Fri 15 Jan 2027 16:00** (provisional) | Between 29 Dec and 26 Jan, after the two holiday weeks. **Re-checked at the G2 review** against the throughput measured from G1 to G2. No comparison arm starts before G3 passes (SoT §38.5) |
| **G4, G5** | **Wed 3 Feb 2027** (provisional) | About three weeks after G3: the week-4 rows (32) plus the remaining re-baseline rows. G5 also needs the field sessions (VOI), which can run before G3 |
| **G6** | **Thu 4 Feb 2027 18:00** (provisional) | — |
| **Demo, G7 dry run** | **Fri 5 Feb 2027 14:00** (dry run 09:00) (provisional) | Confirmed or moved at the G3 review |
| **Code freeze** | **Wed 3 Feb 2027 12:00** (provisional) | It moves with G4 and G5 (plan §11), never earlier than G3 + 2 weeks |

**One alternative the Founders may prefer:** fix only G0-N, G1 and G2 now, and leave G3 onwards undated until the G1 review measures throughput again. That keeps provisional dates out of anything external. Both are within plan §3.1: the gates are unchanged and only the dates move.

## 4. Decisions needed from the Founders (plan §17, D32)

1. **The Tushe pause of 25 Oct and G0-N.**
   - *Options:* (a) lift it for ENV-05, built against recorded responses and the hostility proxy (REQ-ENV-005), so that G0-N can be held on Fri 6 Nov; (b) keep it, record G0-N as BLOCKED, and accept that no G1 or G2 evidence counts.
   - *Recommendation:* (a). It is the only way any result counts before G0-T.
   - *Question:* lift the pause for ENV-05 from Mon 2 Nov?
2. **Scope under D32.** At the measured rate, the DEC-2026-10-31 additions (35 rows: authenticated writers, anchoring, the crash-point matrix, the chaos subset, the Context Fabric, compensation, and others) put G3 at the end of January. The cut line cannot remove them where they are P0 (never cut). Moving any of them out of the POC needs a new decision record.
   - *Question:* keep all of D32's scope and accept the January G3, or name what moves out?
3. **The demo date.**
   - *Options:* (a) record the provisional 5 Feb 2027 now; (b) record no demo date until the G3 review.
   - *Recommendation:* (b) for anything external; (a) only as an internal planning date.
   - *Question:* which?
4. **Re-measurement.** I propose that the G1 review measures throughput again from the Done count between Mon 2 Nov and the review, and that this proposal is redone with that rate.
   - *Question:* agreed?

## 5. Safety and security impact

None on any gate's conditions. No gate is weakened, merged or relabelled. Dates move, gates do not (SoT §40.2). DEBT-01 stays a G3 Tier 0 item, and US-19 cannot pass at G2 until it is closed. The proposal adds no work and removes none.

## 6. Tests added or changed

None.

## 7. Schedule and dependency impact

Every dated row of plan v1.10 moves with its gate. The critical items, by gate:
- **G0-N:** ENV-05 (blocked) and ENV-14.
- **G1:** CON-03 → EXE-01 → PLN-01; REC-01 → TRU-05, REC-03; OUT-01 → BEN-05 → GOV-07.
- **G2:** TRU-02, TRU-04, TRU-07, TRU-08; AMB-02, AMB-03; EXE-04 (after DEBT-01).
- **G3:** REC-07, REC-08, the crash-point matrix (REQ-TST-008), the chaos matrix (SEC-10) and BEN-16.

## 8. SoT or PERD text changes

None in this request. If the Founders record new dates, plan v1.11 is a new version file with its decision record. The gate records are updated in the same PR (plan §19, AGENT-29). The PERD is unchanged.

## 9. Decision owner and record

- **Decision owner:** the Founders (D32; GOV-30 owners "FND, EL").
- **Decision record:** none yet. It is written when the Founders decide, with plan v1.11.

## 10. Migration and rollback

- **Applying it:** the Founders write the chosen dates into each gate record (`docs/poc/execution/gates/`) and plan v1.11.
- **Rollback:** a later change request with new dates. Old dates are never edited in place; each version stays.
- **How it is redone:** from the then-current `tasks.csv`, with the method of §2.
