# Change request: CR-2026-11-14-A211-api-contracts-task-row

- Change ID: CR-2026-11-14-A211-api-contracts-task-row
- Requester: Principal Architect (rulings A207 and A211), relayed to the Repo Steward; EL (noema#521 says it has no task row, AGENTS §14)
- REQ IDs affected: REQ-API-001, REQ-API-002, REQ-API-007. One new plan task (below).
- Behaviour before: noema#521 (public API response and SSE payload contracts) has no task that owns it; AGENTS §14 says no ID covers the work.
- Behaviour after: one row exists. **CON-07** (workstream CON; owners **EL, C1** (C1 is the contract co-owner); REQ-API-001, REQ-API-002, REQ-API-007; Needs CON-03; date 2026-11-18, a Steward default) carries the six-value public stage, the customer answer, the overlay card and the SSE event, one not-found shape, `case_ref_masked` with at most four digits, the `errors` bump (AGENT-15), Go-side enforcement through `record/payloadguard` on outbound edge responses (A194, A211) and the bound on `option_id`. It joins the G2 review row GOV-11 Needs, as the plan requires for tasks dated to a gate.
- The rulings gave the content, not the ID, date or done-when: those are the Steward's smallest defaults and EL, C1 or the Architect may correct them in a later version.
- Safety and security impact: none of the Tier 0 gates, thresholds or TTLs change. The Go-side guard on outbound edge responses is safety-positive (A211).
- Tests added or changed: the owners', failing first (AGENT-11). None here.
- Schedule and dependency impact: one task added (plan count 274 + 1 = 275). The date is a G2-window default (2026-11-18, the day the plan section "Wednesday 18 November · G2" holds). Whether CON-07 must land before the G1 run, and so needs an earlier date, is the Architect's to say (asked on docs#179); the Founder's G1 target is not changed.
- SoT or PERD text changes: no.
- Decision owner: Principal Architect
- Decision records: DEC-2026-11-14-architect-rulings-a199-a208 (A207) and DEC-2026-11-14-architect-rulings-a209-a213 (A211)
- Migration and rollback: none. Applied in plan v1.21 (written after plan v1.20, docs#177, merged); roll back by returning to plan v1.20.
