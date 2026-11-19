# Change request: CR-2026-11-18-A337-con08-parseintentref

- Change ID: CR-2026-11-18-A337-con08-parseintentref
- Requester: Principal Architect (ruling A337), relayed to the Repo Steward; C1 (the intent reference has two parsers' worth of readers and no shared one)
- REQ IDs affected: REQ-API-001 (contracts are generated, versioned and tested). One new plan task (below).
- Behaviour before: the intent reference `<intent_id>@<version>` (for example `int_X@1`, the form `IntentRef` takes in the orchestrator, noema#661) is parsed by each reader that needs it, and it is not the `<prefix>_<ULID>` shape of PERD §32.3. EL's read of noema#661 asked for one parser and one test shared with C1 before the Trust adapter relies on it. No task owns it.
- Behaviour after: **CON-08** exists (workstream CON; owner C1; REQ-API-001; Needs CON-03; date 2026-11-18, the day of CON-07, a Steward default): `ParseIntentRef` lives next to the generated type; the Trust adapter and the Record's typed-ID checks use it; the gate's supersedes link refuses `@007`, a version the contract cannot hold. It joins the G2 review row GOV-11 Needs, as the plan requires for tasks dated to a gate.
- The ruling gave the ID and the owner, not the requirement, the Need, the date or the done-when: those are the Steward's smallest defaults and C1 or the Architect may correct them in a later version.
- Safety and security impact: none of the Tier 0 gates, thresholds or TTLs change. One parser for a reference that carries identity into Trust removes a class of drift; a version the contract cannot hold is refused, not repaired.
- Tests added or changed: the owner's, failing first (AGENT-11). None here.
- Schedule and dependency impact: one task added (plan count 277 + 1 = 278). Whether CON-08 must land before the G1 run is the Architect's to say.
- SoT or PERD text changes: no.
- Decision owner: Principal Architect
- Decision record: DEC-2026-11-18-architect-rulings-a329-a340 (A337)
- Migration and rollback: none. Applied in plan v1.24 (after plan v1.23, docs#202); roll back by returning to plan v1.23.
