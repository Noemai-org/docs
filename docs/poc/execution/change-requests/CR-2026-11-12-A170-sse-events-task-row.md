# Change request: CR-2026-11-12-A170-sse-events-task-row

- Change ID: CR-2026-11-12-A170-sse-events-task-row
- Requester: Principal Architect (ruling A170, 12 Nov 2026), relayed to the Repo Steward
- REQ IDs affected: REQ-API-001 (PERD §39.2: `GET /v1/conversations/{conversation_ref}/events`, server-sent events). New plan task (below).
- Behaviour before: no plan task builds the SSE events route; EL's G1 path note lists it as a node with no task row.
- Behaviour after: a task row exists. EL builds the SSE events under REQ-API-001 now, with no waiting for the row (A170). The route stays unmounted until the per-tenant reader pools are configured (OD-P-82).
- **Proposed row (the Steward's smallest defaults; the ruling gives none of these fields, EL or the Architect may correct them):** ID `EDG-02`; workstream PLT (as EDG-01); owner EL; REQ-API-001; Needs EDG-01; date 2026-11-18 (the G2 window); done_when "The events route serves the stream of PERD §39.2 for a conversation (`progress`, `clarification`, `confirmation`, `answer`, `error`), masked, tests pass, and the route is unmounted until the per-tenant reader DSN is configured".
- Safety and security impact: the route reads only; identity and tenant come from the session (INV-12); the per-tenant reader pools use a file-mounted read-only DSN (A170); output is masked (A154). None of the Tier 0 gates is touched.
- Tests added or changed: EL's, failing first (AGENT-11). None here.
- Schedule and dependency impact: one task added (266). No gate, requirement or other date changes.
- SoT or PERD text changes: no.
- Decision owner: Principal Architect
- Decision record: [DEC-2026-11-12-architect-rulings-a166-a170](../../../decisions/DEC-2026-11-12-architect-rulings-a166-a170.md), A170
- Migration and rollback: none. Applied in plan v1.18 (the row was added after docs#157 and docs#159 merged); roll back by returning to the previous plan version.
