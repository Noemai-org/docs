# POC execution plan

> **Status: Accepted** ([DEC-2026-10-11-poc-4week-plan](../../decisions/DEC-2026-10-11-poc-4week-plan.md), re-pointed by [DEC-2026-10-16](../../decisions/DEC-2026-10-16-execution-reset.md) E11). [`NOEMA_POC_4WEEK_PLAN_v1.4.md`](NOEMA_POC_4WEEK_PLAN_v1.4.md) (current until plan v1.5 merges; 13 Oct 2026, applying [DEC-2026-10-13](../../decisions/DEC-2026-10-13-code-monorepo.md), one code repository) is the dated execution plan for the POC build, **Mon 12 Oct to Fri 6 Nov 2026** (moving to Fri 13 Nov in v1.5). It ranks below the [SoT](../../NOEMA_SOURCE_OF_TRUTH.md) and the [PERD](../perd/README.md): if it disagrees with either, stop the affected task, keep the safe behaviour and follow the governing document (plan, "How to use this plan").
>
> Versions 1.1, [`NOEMA_POC_4WEEK_PLAN_v1.1.md`](NOEMA_POC_4WEEK_PLAN_v1.1.md), 1.2, [`NOEMA_POC_4WEEK_PLAN_v1.2.md`](NOEMA_POC_4WEEK_PLAN_v1.2.md), and 1.3, [`NOEMA_POC_4WEEK_PLAN_v1.3.md`](NOEMA_POC_4WEEK_PLAN_v1.3.md), are kept unchanged.

| File | What it is |
|---|---|
| [`tasks.csv`](tasks.csv) | All 209 tasks, generated from the plan for the board. Run `python3 tools/plan_index.py --write`; CI runs `--check`. Never edit by hand. |
| [`calendar.md`](calendar.md) | Fixed meetings, gates and deadlines (WAT). |
| [`daily/`](daily/README.md) · [`gates/`](gates/README.md) · [`release/`](release/README.md) | Daily notes, gate records and the release evidence bundle, written when they happen. |
| [`debt.md`](debt.md) · [`discovery-log.md`](discovery-log.md) | Debt register (REQ-OPS-004) and founder discovery log (GOV-09). |
| [`templates/`](templates/) | Daily note, gate record, change request, PR checklist, agent handoff, demo pre-flight. |
| [`task-cards/`](task-cards/README.md) | One task card per task, written before the task starts. |

## How a task is run

1. Pick a task from the board (imported from [`tasks.csv`](tasks.csv)).
2. Write its card with the [PERD task card](../perd/templates/task-card.md), copying the REQ acceptance criteria.
3. Write the failing tests first.
4. Open a PR that cites the task ID, the REQ IDs and the SoT IDs.
5. Close the task only against the task definition of done (plan §13.1; [`templates/pr-checklist.md`](templates/pr-checklist.md)).

**Status values:** `Backlog → Ready → In progress → In review → Verified → Done`, plus the `Blocked` flag, which always names its blocker, its owner and the date it must clear (plan, "How to use this plan").

## Daily rhythm, gates and notes

- The fixed meetings are in [`calendar.md`](calendar.md) (plan §5).
- The daily note goes in `daily/<YYYY-MM-DD>.md`, using [`templates/daily-note.md`](templates/daily-note.md).
- Gate outcomes go in `gates/G<n>.md`, using [`templates/gate-record.md`](templates/gate-record.md). The outcome is **PASS, FAIL or BLOCKED** only.

## How the plan changes

A change goes through a [change request](templates/change-request.md) (plan §19). One PR then carries all three of:

1. a new version file (`NOEMA_POC_4WEEK_PLAN_v1.2.md`; the old version is kept);
2. the regenerated `tasks.csv`;
3. a note in that day's daily note.

The plan never changes silently.

## Rules for coding agents

Follow plan §4.1 (task card, tests first, two reviews on P0 paths, CONFLICT block, handoff report via [`templates/agent-handoff.md`](templates/agent-handoff.md)) and §13.1. An agent's report is not acceptance. Agents never:

- edit `/contracts` without a version bump (AGENT-15);
- touch safety thresholds (REQ-AGT-005);
- add a dependency (AGENT-14);
- access the held-out repository or the oracle (REQ-AGT-004);
- weaken, skip or delete a test to make CI green;
- add a model call to Trust, Execution or Outcome, or give a model credentials, tools, SQL, shell or network reach;
- add a monetary action or any prohibited case or evidence mutation;
- map a timeout to failure, or collapse an unknown or contradictory state.
