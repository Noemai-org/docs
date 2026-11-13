# Change request: CR-2026-11-12-A159-gov-decisions

- Change ID: CR-2026-11-12-A159-gov-decisions
- Requester: Principal Architect (ruling A159, 12 Nov 2026), relayed to the Repo Steward
- REQ IDs affected: REQ-INT-003 (GOV-08, GOV-10), REQ-EXP-003 (GOV-10), REQ-BEN-003 and REQ-AGT-004 (GOV-03), REQ-VOI-005 (PRE-05). Plan tasks GOV-03, PRE-05, GOV-08, GOV-10.
- Behaviour before: GOV-08 contracts native-speaker reviewers for yo, ha, ig and pcm and confirms the Africa/Lagos time zone (OQ-12); GOV-10 is reviewed by "reviewers".
- Behaviour after: GOV-08 only confirms the Africa/Lagos time zone (OQ-12); GOV-10 is reviewed by the field contributors. GOV-03 and PRE-05 are decided as done: the benchmark owner is named (Osemwota Osagie Anthony), the access list to the private benchmark-heldout repository is him and the Founder only, and the field-session devices are ordered. Their status fields change when the evidence is linked (AGENTS §9).
- Safety and security impact: none on the Tier 0 gates or the invariants. GOV-03's access list (no builder or agent identity) is the INV-22 control; the change request does not alter it.
- Tests added or changed: none. GOV-10 keeps "every change has a golden test".
- Schedule and dependency impact: GOV-08's done_when no longer waits on reviewer contracting; GOV-10's Needs (GOV-08, UND-06) are unchanged. No gate or date moves. The task count stays 265.
- SoT or PERD text changes: no. OQ-12's text in the PERD ("reviewers contracted before labels freeze", DEC-2026-10-17) is superseded in effect by A159; the PERD text is not edited here.
- Decision owner: Principal Architect
- Decision record: [DEC-2026-11-12-architect-rulings-a148-a160](../../../decisions/DEC-2026-11-12-architect-rulings-a148-a160.md), A159
- Migration and rollback: apply by merging plan v1.17; roll back by returning to plan v1.16 (v1.16 is unchanged).
