# DEC-2026-11-03-demo-date-scope-and-working-rules

- **Status:** Decided by the Founder in standing orders of 3 November 2026, given in a working session. **They count only once this record is merged** (AGENTS.md §2.3, SoT §0.4); the Technical Co-Founder confirms by approving the pull request that adds it. Until it merges, agents follow the committed documents it supersedes. Items marked **CONFIRM** need an explicit founder word before work that depends on them.
- **Date:** 3 November 2026
- **Task:** GOV-30 (re-baseline). Prepared by the Engineering Lead role agent; the Founder owns the decision.
- **Closes:** none. Decides the outcome of the change request [CR-2026-11-01-GOV-30-rebaseline](../poc/execution/change-requests/CR-2026-11-01-GOV-30-rebaseline.md), whose proposed dates are superseded by the dates below.
- **Owner:** Founder and Technical Co-Founder.
- **Authority order applied:** SoT v1.10 → this record and earlier decision records → PERD v1.19 → plan v1.10. Where this record differs from plan v1.10 or from an earlier decision record on a date, a scope cut or a working day, **this record wins** (SoT §0.4: the latest recorded founder decision).

## 1. The decisions (the Founder's orders, as given)

| # | Decision |
|---|---|
| D1 | **Demo:** Saturday 12 December 2026, 14:00 WAT; the G7 dry run is at 09:00 that day. It does not move. **Monday to Saturday are work days** |
| D2 | **No scope is cut.** Every requirement and task in PERD v1.19, plan v1.10 and DEC-2026-10-31 is executed. The plan §2 cut line is not applied. Nothing is deferred to after the demo |
| D3 | **Gate dates are "no later than" dates, and the team beats them.** A task starts the moment its prerequisites are on `main`; nobody waits for a date, a meeting or a review window. The dates are in §2. Quality is not traded for speed |
| D4 | **A gate that fails on its date** is recorded FAIL in `docs/poc/execution/gates/` with the strongest evidence (check-run links, run IDs, failing cases), the root cause and a resolution plan (owner, steps, date). The plan is executed until the gate passes. A failed gate is never relabelled, softened or abandoned, and never reduces scope. Reports on it are provided |
| D5 | **No idling, no wasted tokens.** If the next step needs a decision, a review or a merge, state it and take the next task; "waiting for the founders" is never a status |
| D6 | **Decide inside your task** when the choice is reversible and consistent with the SoT, PERD and decision records, and record it in the PR body. Otherwise escalate in the charter format with a recommendation and keep working. The Architect answers the same day |
| D7 | **When checks are green at the final head and Codex has reviewed,** the author marks the PR Ready for review and puts at the top of the PR body: "APPROVE NOW: what it does, risk, recommendation", with the order in which PRs should be approved and merged. The Founders approve and merge |
| D8 | **Report format**, in this order: (a) done since the last report, with task, PR, head SHA and check-run links; (b) in progress, with what remains and ETA against target and latest; (c) decisions taken and where recorded; (d) questions, with problem, options, recommendation and consequence; (e) approvals needed, with each PR's APPROVE NOW line; (f) risks to a gate; (g) the next three tasks and when each starts. Claims count only with a check-run link at the final head; unknown is "unknown"; a failure is reported at once |

## 2. Dates (WAT; "target" is the aim, "latest" is the commitment)

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

**Gate conditions are unchanged** (plan §3.1). Only dates move, never gates (SoT §40.2). G0 still passes only when G0-N and G0-T both pass (E4). No comparison arm starts before G3 passes (SoT §38.5).

## 3. What this record supersedes (and what it does not)

| Superseded | By |
|---|---|
| Plan v1.10 §3 calendar and the gate dates in §3.1, and the dates of the gate records | §2 above |
| Plan §3 "Saturdays are not planned work" | D1: Saturday is a work day |
| Plan §11 code freeze "Wed 11 Nov 12:00 WAT" and §14 demo date | §2 above |
| Plan §2 cut line, and DEC-2026-10-16-contract-and-pack-clarifications C8 items 1 to 3 ("cut now") | D2. The rows C8 changed revert to their pre-C8 scope: **VOI-04** (TTS for all five locales, not English and Pidgin only), **UI-01 to UI-06** (beyond the PERD §40 minimum), **ARM-04** (arms E and F built and run, not written up as "not tested"). The Repo Steward lists the exact rows and regenerates `tasks.csv` |
| CR-2026-11-01-GOV-30-rebaseline §3 proposed dates | §2 above. The change request stays as the feasibility evidence (§4) |

**Not changed:** every invariant, Tier 0 gate, binding decision and the "never cut" list; AGENTS.md rules (agents never approve or merge; a Needs task must be Done before its dependant starts; the allowlist; the stop conditions). D3's "start the moment prerequisites are on `main`" is that same Needs rule, applied without waiting for a date.

## 4. Feasibility (evidence, not a change to the orders)

From docs#77's `tasks.csv` (261 tasks, 25 Done), by the method of the change request: units = 1 per task not Done, ½ for In progress or In review, counted along each gate's prerequisites.

| By | Units to finish (cumulative) | Work days from Tue 3 Nov (target / latest) | Units a day needed (target / latest) |
|---|---|---|---|
| G1 | 17 | 6 / 8 | 2.8 / 2.1 |
| G2 | 43 | 14 / 16 | 3.1 / 2.7 |
| G3 | 115.5 | 25 / 28 | 4.6 / 4.1 |
| Code freeze (all tasks, an upper bound) | 210.5 | 32 | 6.6 |

**Measured pace:** about 2 build tasks a working day (19 to 30 Oct). So G1's latest date is at today's pace, **G2 needs about 1.4 times it, G3 about 2 times, and the whole scope about 3 times.** The seven role agents started on 31 Oct may raise the pace; that is not yet measured. The method treats every task as the same size and ignores critical paths. **Unknown:** the real pace from here. The G1 review re-measures it (CR §4).

## 5. Open items

- **CONFIRM: lift the Tushe pause of 25 Oct (DEC-2026-10-25)** for all Tushe-dependent tasks (ENV-01, ENV-03, ENV-04, ENV-05, ENV-10 to ENV-12). D2 and D3 imply it, but the pause is a recorded founder decision. G0-N's latest date (Fri 6 Nov) cannot be met without it: ENV-14 needs ENV-05.
- **G4 has three work days** between G3's latest (Fri 4 Dec) and G4/G5's latest (Wed 9 Dec) to build, review and run arms A, B and D, and G5 needs the field sessions (≥100, ≥50% Pidgin). Both start earlier than G3 where they do not depend on it (voice and arm building); the comparison *runs* cannot.
- **G0-T has no date.** The demo date is fixed, so a late G0-T makes every result after G0-N provisional (E4). The Founders escalate to Tushe's lead (SR-24).
- **Plan v1.11** (a new version file, never an edit in place) carries §2 into the plan text; assigned to the Repo Steward with the `tasks.csv` regeneration. Until it exists, this record wins on every difference.

## 6. Record fields (decisions README template)

- Status: see the top of this record
- Date: 3 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: §1 and §2
- Rationale and evidence: the Founder's orders; §4
- Affected requirement IDs / SoT sections: none changed; SoT §40.2 applied; plan v1.10 §2, §3, §3.1, §11, §14; DEC-2026-10-16 E3 and C8; gate records G0-N to G7
- Migration notes: §3 (rows and records to update); plan v1.11 follows
- Supersedes: the dates, the Saturday rule and the cut line named in §3
