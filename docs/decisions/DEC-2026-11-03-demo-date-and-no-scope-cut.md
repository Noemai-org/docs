# DEC-2026-11-03-demo-date-and-no-scope-cut

- **Status:** Decided by the Founder on 3 November 2026, in standing orders given in a working session. **It counts only once this record is merged** (AGENTS.md §2.3, SoT §0.4); the Technical Co-Founder confirms by approving the pull request that adds it. Until it merges, agents follow the committed documents it supersedes.
- **Date:** 3 November 2026
- **Task:** GOV-30 (re-baseline). Prepared by the Engineering Lead role agent; the Founders own the decision.
- **Closes:** none. Decides the change request `CR-2026-11-01-GOV-30-rebaseline` (docs#83, closed unmerged as superseded by this record).
- **Owner:** Founder and Technical Co-Founder.
- **Authority order applied:** SoT v1.10 → this record and earlier decision records → PERD v1.19 → plan v1.10. On a date, a working day or the cut line, this record wins over plan v1.10 and over DEC-2026-10-16 (SoT §0.4: the latest recorded founder decision).

## 1. Decisions

| # | Decision |
|---|---|
| D1 | **The demo is Saturday 12 December 2026, 14:00 WAT, and the date is fixed.** The G7 dry run is at 09:00 that day |
| D2 | **Monday to Saturday are work days.** Plan v1.10 §3 ("Saturdays are not planned work") no longer applies |
| D3 | **No scope is cut.** Every requirement and task in PERD v1.19, plan v1.10 and DEC-2026-10-31 is executed. The plan §2 cut line is not applied, and nothing is deferred to after the demo |
| D4 | **Gate dates are "no later than" dates, and the team beats them.** A task starts the moment its prerequisites are on `main`; nobody waits for a date, a meeting or a review window. The calendar is in §2 |
| D5 | **The gate-failure protocol.** If a gate fails on its date: (1) record **FAIL** in `docs/poc/execution/gates/` with the strongest evidence (check-run links, run IDs, failing cases), the root cause, and a resolution plan with owner, steps and date; (2) execute the plan until the gate passes; (3) a failed gate is never relabelled, softened or abandoned, and it never reduces scope; (4) provide the reports it needs. The rerun is a new run with its own ID (plan §3.1 gate rules stay) |

## 2. The gate calendar (WAT; "target" is the aim, "latest" is the commitment)

| Gate or event | Target | Latest |
|---|---|---|
| G0-N | Wed 4 Nov | Fri 6 Nov 17:00 |
| G0-T | — | Set by Tushe; unchanged (DEC-2026-10-16 E3, E4) |
| G1 | Mon 9 Nov | Evidence Wed 11 Nov; review Thu 12 Nov 10:00 |
| G2 | Wed 18 Nov | Fri 20 Nov 16:00 |
| G3 | Tue 1 Dec | Fri 4 Dec 16:00 |
| G4 and G5 | Mon 7 Dec | Wed 9 Dec |
| Code freeze | — | Wed 9 Dec 12:00 |
| G6 | Wed 9 Dec | Thu 10 Dec 18:00 |
| Recovery day | — | Fri 11 Dec |
| G7 dry run | — | Sat 12 Dec 09:00 |
| Demo | — | Sat 12 Dec 14:00 |

**Gate conditions are unchanged** (plan §3.1). Only dates move, never gates (SoT §40.2). G0 passes only when G0-N and G0-T both pass (E4), and no comparison arm starts before G3 passes (SoT §38.5).

## 3. What this supersedes, and what it does not

| Superseded | By |
|---|---|
| Plan v1.10 §3 calendar and §3.1 gate dates; the dates in the gate records G0-N to G7 | §2 (the gate records are updated in this pull request) |
| Plan §3 "Saturdays are not planned work" | D2 |
| Plan §11 code freeze "Wed 11 Nov 12:00 WAT" and §14 demo date | §2 |
| Plan §2 cut line, and DEC-2026-10-16-contract-and-pack-clarifications C8 items 1 to 3 ("cut now") | D3. The rows C8 changed return to their earlier scope: **VOI-04** (TTS for all five locales, not English and Pidgin only), **UI-01 to UI-06** (beyond the PERD §40 minimum) and **ARM-04** (arms E and F built and run, not written up as "not tested") |

**Not changed:** every invariant, Tier 0 gate and binding decision; the "never cut" list; the AGENTS.md rules (agents never approve or merge; a Needs task must be Done before its dependant starts; the allowlist; the stop conditions). D4's "start the moment prerequisites are on `main`" is the same Needs rule without waiting for a date.

**Not recorded here:** the Founder's working rules of the same orders (decide inside your task, APPROVE NOW on a ready PR, the report format, no idling) are working practice, not scheduling; they are not part of this record.

## 4. Handover and open items

- **Plan v1.11** (a new version file, never an edit in place) carries §2 and D2 to D3 into the plan text, with the `tasks.csv` rows named in §3 regenerated. **Handed to the Repo Steward.** Until it merges, this record wins on every difference.
- **Required pace (evidence for the Founders, not a change to the orders).** From `tasks.csv` on `main` (261 tasks, 25 Done), counting 1 for each task not Done and ½ for In progress or In review, along each gate's prerequisites: G1 needs 17, G2 43 and G3 115.5 cumulative, and everything 210.5, against **work days from Tue 3 Nov to the latest dates of 8, 16, 28 and 32.** That is about 2.1, 2.7, 4.1 and 6.6 units a day at the latest dates, against a measured **about 2 build tasks a working day** (19 to 30 Oct). G1's latest date is at today's pace; G2 needs about 1.4 times it, G3 about 2 times, the whole scope about 3 times. The seven role agents started on 31 Oct may raise the pace; that is not yet measured. The method treats all tasks as the same size and ignores critical paths. The Engineering Lead reports the measured pace at every gate.
- **Open: the Tushe pause of 25 Oct (DEC-2026-10-25).** G0-N's latest date needs ENV-14, which needs ENV-05, which that pause blocks. D3 implies lifting it, but it is a recorded founder decision, so lifting it needs an explicit founder word.
- **Open: G4 has three work days** between G3's latest (Fri 4 Dec) and G4's latest (Wed 9 Dec) for arms A, B and D to be built, reviewed, run and reported; the arm *builds* and the voice field sessions start before G3 where they do not depend on it.
- **Open: G0-T has no date.** The demo date is fixed, so a late G0-T makes every result after G0-N provisional (E4); the Founders escalate to Tushe's lead (SR-24).

## 5. Record fields (decisions README template)

- Status: see the top of this record
- Date: 3 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: §1 and §2
- Rationale and evidence: the Founder's orders; §4
- Affected requirement IDs / SoT sections: none changed; SoT §40.2 applied; plan v1.10 §2, §3, §3.1, §11, §14; DEC-2026-10-16 E3 and C8; gate records G0-N to G7
- Migration notes: §3 and §4 (plan v1.11 by the Repo Steward)
- Supersedes: the dates, the Saturday rule and the cut line named in §3
