# Change request: CR-2026-11-17-A282-worker-task-row

- Change ID: CR-2026-11-17-A282-worker-task-row
- Requester: Principal Architect (ruling A282), relayed to the Repo Steward; EL (noema#660 proposes the ID WRK-01, which the trace check refuses, AGENTS §14)
- REQ IDs affected: REQ-EXE-005, REQ-EXE-006, REQ-RCV-002, REQ-OPS-003. One new plan task (below).
- Behaviour before: the core's Temporal worker (the process that registers the `EscalateCase` workflow and its activities so the graph runs for real) has no plan task. EL's card, `status/WRK-01.md` in noema#660, cites a prefix the trace check does not accept.
- Behaviour after: one row exists. **STM-04** (the STM family's next free ID, A282; owner **EL**; REQ-EXE-006, REQ-RCV-002, REQ-EXE-005, REQ-OPS-003; Needs STM-01 and EXE-06; date 2026-11-18, the day section that holds EXE-06, a Steward default) carries the worker as the card describes it: the D8 retry options, an unknown outcome stops with no retry, no wall-clock read or I/O in workflow code, mutual TLS, and the card's three faults (timeout and 5xx on the create write, a mid-workflow worker restart, Temporal unavailable at start). It joins the G2 review row GOV-11 Needs, as the plan requires for tasks dated to a gate. EL's noema#660 cites STM-04 in place of WRK-01.
- The ruling gave the family, not the date, Needs or done-when: those are the Steward's smallest defaults and EL, C1 or the Architect may correct them in a later version. Whether the worker must land before the G1 run, and so needs an earlier date, is the Architect's to say; the Founder's G1 target is not changed.
- Safety and security impact: none of the Tier 0 gates, thresholds or TTLs change.
- Tests added or changed: the owner's, failing first (AGENT-11). None here.
- Schedule and dependency impact: one task added (plan count 275 + 1 = 276).
- SoT or PERD text changes: no.
- Decision owner: Principal Architect
- Decision record: DEC-2026-11-17-architect-rulings-a278-a286 (A282)
- Migration and rollback: none. Applied in plan v1.22 (written after plan v1.21); roll back by returning to plan v1.21.
