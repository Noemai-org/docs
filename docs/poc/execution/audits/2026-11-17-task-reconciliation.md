# Task reconciliation, 17 Nov 2026

Date: 2026-11-17 · Owner: Repo Steward · Task: GOV-30 (status assessment) · Source: `docs/poc/execution/tasks.csv` (275 rows, plan v1.21) against the merged and open pull requests of `Noemai-org/noema` (446) and `Noemai-org/docs` (160) read on 17 Nov 2026. This is a derived, non-normative record. It defines no requirement, gate or decision.

## 1. The counts

| Category | Tasks |
|---|---|
| Completed | 72 |
| In progress | 49 |
| In review | 2 |
| Ready | 14 |
| Blocked | 86 |
| Deferred | 7 |
| Stalled | 16 |
| Not started | 29 |
| **Total** | **275** |

The eight categories are mutually exclusive and add up to the 275 tasks in the register. A task sits in the first rule that fits, in the order of section 2. "Stale or unsupported" is a separate flag laid over the same tasks, not a ninth category: it covers **79** tasks (section 4).

Before this audit the board said: Backlog 127, In progress 64, Done 46, Unassessed 24, Ready 12, In review 2. After it, `current_status` says: Backlog 122, Done 72, In progress 65, Ready 14, In review 2. The board's four columns cannot express Blocked, Deferred or Stalled, so those three are carried in this record and in the `blocked` flag; they read as Backlog or In progress in `tasks.csv`.

## 2. Rules used

In this order, the first that fits:

1. **Completed**: every clause of the task's `Done when` is shown by merged code, tests or records on `main`. A status file is a claim, not evidence. The merge commit's check-run is listed in the evidence column of the CSV; where it was red or missing, the CSV says so.
2. **Deferred**: the plan dates it "After the build window" (6 tasks), or the plan §2 cut line already defers it (ARM-04, "arms E and F not tested").
3. **In review**: an open, non-draft pull request with no conflict and no change request, and the work is not yet met.
4. **In progress**: an open pull request that is a draft, conflicted or red, or merged work with activity in the last 7 days and a clause still missing.
5. **Stalled**: merged work that does not meet `Done when`, no open pull request that moves, and no activity for more than 7 days (before 10 Nov 2026), or the board said In progress and nothing supports it.
6. **Blocked**: no work yet, and a Needs task is not Completed, an external input (a Tushe delivery) has not arrived, or the verifier named a blocker.
7. **Ready**: every Needs task is Completed, nothing external is awaited, no work has started, and the planned date is today or earlier.
8. **Not started**: everything else with no evidence (for example the planned date is later than today).

The seven-day line is a working choice of this audit, not a plan rule. Say so if you want a different one.

## 3. What changed on the board

Updated the same day (17 Nov 2026) after the first draft: ENV-17 is Completed (noema#537, read after the audit; the Founders' message called it merged and the code on `main` supports it) and UND-14 is In progress, not Done: the compile route is not built or wired on `main` (`services/model/README.md`; noema#598 merged the compiler only), so the report that it merged is not supported.

- Completed: **72** against **46** Done before. The gap is work that merged without anyone moving the board; the CSV lists each task with the evidence.
- **6** tasks the board called Done are not supported (section 4).
- `Unassessed` is gone: all 24 of those tasks now have a category.
- `blocked` is `true` exactly where the CSV has a blocker, and `false` for Completed tasks and tasks with none.

## 4. Stale or unsupported board entries (79)

| Kind | Tasks |
|---|---|
| board In progress → Completed | 18 |
| board Backlog → Completed | 9 |
| board Unassessed → Not started | 9 |
| board Unassessed → Ready | 6 |
| board Done, not supported by merged evidence | 6 |
| board In progress → Blocked | 6 |
| board In progress → Not started | 6 |
| board Unassessed → Blocked | 5 |
| board Ready → Not started | 4 |
| board Unassessed → In progress | 3 |
| board Ready → Completed | 2 |
| board Ready → Blocked | 2 |
| board In review → In progress | 1 |
| board In review → Completed | 1 |
| board Unassessed → Completed | 1 |

Board Done but not supported by merged evidence:

- PRE-05 (V): Blocked. No committed order/delivery record
- GOV-01 (FND): Stalled. Register columns are ID/conflict/why/resolution/Status; no owner, due date or affected-task column seen, so "no unowned row" not shown
- GOV-03 (FND): Blocked. Access list not evidenced in a committed doc
- GOV-06 (FND, EL): Stalled. No OD-P entry carries the literal mark "in force (provisional)"; they are labelled NON-CANONICAL provisional with Open statuses
- CON-05 (C1+AG): Ready. No rule found for NUMERIC/REAL/MONEY SQL types in migrations, and none for a literal exponent multiplier on money; Go float rule covers fields/areas only.
- EDG-02 (EL): In progress. Only the handler is merged and tested against a fake Feed; no PostgreSQL Feed or mount when the reader DSN is configured, so serving a real conversation stream is not shown.

The full list, with the evidence for each, is the `stale_flag` column of the CSV.

## 5. Task IDs by category

**Completed (72):** PRE-01, GOV-19, PLT-01, GOV-20, CON-02, GOV-04, PLT-02, PLT-03, PLT-04, CON-01, BEN-01, BEN-02, SEC-01, CON-03, PLT-06, PLT-07, REC-01, STM-01, UND-02, BEN-03, VOI-02, PCK-01, EVD-01, EVD-03, UND-04, ENV-09, BEN-04, VOI-03, PCK-02, ENV-08, SEC-02, TRU-01, TRU-02, TRU-03, TRU-05, EXE-01, RES-01, OPS-08, OPS-09, GOV-29, EXE-02, EXE-03, OUT-01, RCV-01, REC-03, TST-01, OPS-07, EXE-04, TRU-09, SEC-04, OUT-02, BEN-10, PCK-03, TRU-13, PCK-04, REC-09, SEC-05, BEN-13, REC-04, BEN-14, BEN-15, TST-04, SEC-11, UND-12, BEN-30, VOI-18, SEC-14, SEC-12, REC-08, ENV-15, BEN-31, ENV-17

**In progress (49):** PLT-05, AGT-01, VOI-01, UND-01, UND-03, EDG-01, UND-05, ENV-05, ENV-06, TRU-04, GOV-30, ENV-14, EXP-01, BEN-05, SEC-03, VOI-04, TRU-06, VOI-05, TRU-07, TRU-08, EDG-02, CAP-01, VOI-06, UI-01, EXE-05, EXE-09, RCV-02, MEM-01, MEM-02, CON-07, UI-02, VOI-08, EXP-04, UI-03, SEC-08, SEC-09, BEN-16, UI-04, VOI-10, OPS-02, UND-13, VOI-17, EXE-08, TST-05, BEN-29, BEN-21, BEN-23, VOI-14, UND-14

**In review (2):** ENV-04, ENV-13

**Ready (14):** PRE-02, PRE-03, PRE-04, GOV-02, GOV-05, GOV-23, GOV-09, REC-02, PLT-08, CON-05, EVD-02, EVD-06, CON-06, REC-06

**Blocked (86):** PRE-05, GOV-03, ENV-01, ENV-02, ENV-11, EVD-04, EVD-05, UND-06, ENV-10, GOV-07, ENV-07, AMB-01, AMB-02, AMB-03, AMB-04, AMB-05, RES-03, RES-04, GOV-10, BEN-28, STM-03, REC-10, UND-15, VOI-07, TST-02, UND-08, PLN-03, RCV-04, GOV-11, OUT-04, RCV-03, EXP-02, EXP-03, OUT-05, API-01, EXP-05, VOI-09, SEC-07, OBS-01, OBS-02, BEN-17a, BEN-17b, SEC-10, PLN-02, OPS-01, VOI-11, OPS-03, BEN-19, UI-05, OBS-03, UND-09, UND-10, UND-11, RES-05, CAP-03, MEM-04, GOV-12, REC-07, SEC-13, TST-06, ARM-01, ARM-02, BEN-22, VOI-12, ARM-03, ARM-05, BIZ-02, UI-06, VOI-13, BEN-24, BEN-25, VOI-15, BIZ-03, REL-01, GOV-13, BEN-26, BEN-27, GOV-14, REL-02, DEM-01, GOV-15, GOV-16, DEM-02, DEM-03, GOV-17, GOV-18

**Deferred (7):** ARM-04, GOV-24, GOV-25, GOV-26, GOV-27, OPS-05, OPS-06

**Stalled (16):** CON-04, GOV-01, GOV-06, GOV-22, ENV-03, PLN-01, BEN-12, REC-05, SEC-06, VOI-16, BEN-18, EXP-06, PLT-09, GOV-28, EXE-07, BEN-20

**Not started (29):** ENV-12, GOV-08, INP-01, STM-02, BEN-06, RES-02, BEN-07, BEN-08, TRU-10, UND-16, EXE-06, TRU-11, TRU-12, BEN-09, BEN-11, UND-07, GOV-21, TRU-14, ENV-16, CAP-02, OUT-03, TST-03, DATA-01, DATA-02, OPS-04, PCK-05, MEM-03, SEC-15, BIZ-01

## 6. Files

- [`2026-11-17-task-reconciliation.csv`](2026-11-17-task-reconciliation.csv): one row per task with ID, owner, workstream, gate, planned date, board status before, category, new status, blocked flag, blocker, verdict, evidence, gap, last activity, open pull request state, stale flag and source reference (plan line and `tasks.csv`).
- `tasks.csv`: only `current_status` and `blocked` changed (the two fields the Steward writes; AGENTS §9). `python3 tools/plan_index.py --check` passes.

## 7. Limits of this audit

- Pull requests were matched to tasks by the task ID in the title or branch name. Six verification agents then read the code, tests and records on `main` against each task's `Done when`. Tasks with no matching PR and no `Done` mark were not read one by one: they are classed from their Needs and dates alone.
- Not checked: the private `benchmark-heldout` repository (INV-22; BEN-11 and GOV-03 are "no evidence"), the `brain` repository (GOV-22), the GitHub Environments API (403 through the proxy; PLT-01), and whether the human reviewer READY gates were given (REC-09, among others). A Completed task is therefore "merged and meeting `Done when`", not "accepted" in the sense of plan §4.1.
- Some Completed tasks merged with a red or missing check-run (noted per task in the CSV: for example noema#186, #194, #272, #177, #115). `main`'s head was green when checked. They stay Completed with that note; say if you want them held at Verified until a green run is linked.
- Judgement calls the verifiers flagged are in each row's `evidence` and `gap` text. Where a call is strict (for example GOV-06 and GOV-01), the reason is written there so the owner can answer it.
- Open pull requests were not re-read for CI beyond what the agents saw; their state is a snapshot of 17 Nov 2026.
