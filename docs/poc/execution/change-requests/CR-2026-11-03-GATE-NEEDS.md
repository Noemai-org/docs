# Change request: missing Needs on the gate review rows (proposal)

- **Change ID:** CR-2026-11-03-GATE-NEEDS
- **Date:** 3 November 2026
- **Prepared by:** the Repo Steward, at the Architect's direction (work order of 3 Nov 2026, item 3). **A proposal for the Architect and the Founders. It changes no plan row and no `tasks.csv` row.** If approved, the Architect applies it in a plan version (plan §19) and I regenerate `tasks.csv`.
- **Status:** Proposed

## Problem

Plan v1.11 dates every task by the gate that needs it. The Needs rule (a task takes the earliest gate whose review row transitively needs it) works only for tasks on a gate row's Needs path. Today **158 of 261 tasks are on no gate's Needs path** (the tool's closure of ENV-14, GOV-07, BEN-05, GOV-11, GOV-12 and the G3-marked rows, GOV-13, GOV-16, DEM-02, DEM-03). They were dated by their old date mapped to the old gate window instead. So a gate can pass, by its review row's Needs, while tasks that belong to its window are not Done, and "tasks remaining per gate" cannot be computed from the Needs graph alone.

## Proposal

Add each such task to the **Needs** of the review row of the gate it is dated under in plan v1.11. A gate review row would then need everything dated to it, which is what "the gate passes" has always meant (plan §3.1 conditions are unchanged; this only makes the Needs column say it). Nothing else in any row changes.

| Gate (date in plan v1.11) | Review row | Needs today | Tasks to add | Add |
|---|---|---|---|---|
| G0-N | ENV-14 | CON-03, ENV-05, ENV-06, BEN-04, ENV-08, ENV-09, ENV-13, SEC-02 | 47 | GOV-01, GOV-04, GOV-05, GOV-06, GOV-22, GOV-23, PLT-02, PLT-03, PLT-05, AGT-01, ENV-02, VOI-01, GOV-09, SEC-01, PLT-07, REC-02, STM-01, PLT-08, UND-02, EDG-01, ENV-04, BEN-03, VOI-02, ENV-11, CON-05, EVD-01, EVD-02, EVD-03, EVD-04, EVD-05, EVD-06, UND-04, UND-05, UND-06, ENV-10, VOI-03, CON-06, TRU-01, TRU-02, TRU-03, TRU-04, RES-01, REC-06, OPS-08, OPS-09, GOV-29, GOV-30 |
| G1 | GOV-07 | BEN-05, ENV-14 | 4 | EXE-03, EXP-01, TST-01, OPS-07 |
| G2 | GOV-11 | BEN-12, GOV-21, R3 received | 38 | GOV-08, AMB-01, AMB-02, AMB-03, AMB-04, INP-01, STM-02, SEC-03, VOI-04, AMB-05, RES-02, RES-03, RES-04, TRU-06, EXE-04, VOI-05, TRU-07, TRU-08, TRU-09, SEC-04, CAP-01, GOV-10, VOI-06, UI-01, BEN-28, TRU-10, OUT-02, EXE-05, EXE-06, RCV-02, TRU-11, TRU-12, VOI-07, PCK-03, MEM-01, MEM-02, UND-07, UND-08 |
| G3 | GOV-12 | BEN-18, SEC-10, SEC-06 | 55 | OUT-03, OUT-04, RCV-03, EXP-02, EXP-03, UI-02, SEC-05, OUT-05, API-01, EXP-04, EXP-05, UI-03, REC-04, VOI-09, SEC-07, SEC-08, SEC-09, OBS-01, OBS-02, UI-04, VOI-10, TST-03, TST-04, PLN-02, DATA-01, DATA-02, OPS-01, OPS-02, VOI-16, OPS-03, SEC-11, BEN-19, UI-05, OBS-03, OPS-04, UND-09, UND-10, UND-11, UND-12, BEN-30, UND-13, PCK-04, PLN-03, PCK-05, RES-05, CAP-02, RCV-04, CAP-03, BEN-31, MEM-03, MEM-04, VOI-17, VOI-18, EXP-06, PLT-09 |
| G4/G5 | GOV-13 | BEN-24, VOI-14, REL-01 | 10 | BEN-21, BEN-22, BIZ-01, ARM-04, BEN-23, BIZ-02, UI-06, BEN-25, VOI-15, BIZ-03 |
| G6 | GOV-16 | BEN-27, GOV-14, REL-02 | 2 | DEM-01, GOV-15 |
| G7 | DEM-02 | GOV-16 | 2 | GOV-17, GOV-18 |

The 20 provisional rows of plan v1.11 (UND-09 to UND-13, BEN-30, BEN-31, PCK-04, PCK-05, PLN-03, RES-05, CAP-02, CAP-03, RCV-04, MEM-03, MEM-04, VOI-17, VOI-18, EXP-06, PLT-09) are in the G3 list above; if the Architect gives any an earlier gate, move it to that gate's list.

## Effects and risks

1. **Longer Needs cells.** GOV-12 would list about 55 more tasks; ENV-14 about 47. The tool accepts it (Needs may name any earlier-positioned task, and plan v1.11 orders every group topologically).
2. **A review row that needs a task does not wait for it to be dated earlier.** Under the standing orders a task starts when its own prerequisites are on `main`; the review row's new Needs only say the gate cannot pass before they are Done.
3. **Gate-order dependencies stay as they are.** For example no comparison arm starts before G3 passes (SoT §38.5): BEN-21 to BEN-25 and ARM-04 are added to GOV-13 (G4 and G5), and the existing arm rows already need G3 through GOV-12.
4. **Done rows.** Tasks that are already Done (for example PLT-02, REC-01's neighbours) are listed too; they cost nothing and make the closure complete.

## Options

| Option | Effort | Risk | Effect on the gate-readiness numbers |
|---|---|---|---|
| A. Apply the table above (recommended) | Small: one plan version and a regenerated CSV | Long Needs cells | Every task belongs to exactly one gate by the Needs graph; the table needs no date mapping |
| B. Add one aggregate row per gate that needs its tasks (for example "G2 scope complete") and make the review row need that row | Medium: 7 new rows | New IDs; more rows to maintain | Same as A, with shorter review rows |
| C. Leave as is | None | Gate passes on a thin Needs list; readiness depends on the old-date mapping | Counts stay approximate |

**Recommendation: A.** It uses the Needs column for what it is for and needs no new IDs.

**Question for the Architect:** A, B or C?
