# Change request: CR-2026-11-08-REC-09-record-export

- Change ID: CR-2026-11-08-REC-09-record-export
- Requester: Core Engineer 1 (C1), through noema issue #354; drafted by the Repo Steward. **The Founders approved it; the plan row and `tasks.csv` row are added in plan v1.13 in the same change set.**
- Status: **Approved by the Founders on 8 Nov 2026 (ruling A109, DEC-2026-11-08-rec-09-record-export), with four conditions: a library function and not an HTTP route; Needs REC-03 and the audit_record shape of noema#249; the Security Reviewer's READY on what it exposes before the C1 PR leaves Draft; the decision record, plan v1.13, tasks.csv and the card in one change set.**
- REQ IDs affected: REQ-AUD-003 (reconstruction), REQ-BEN-001, REQ-BEN-009 (REV rule 6); INV-22 (nothing from the oracle or held-out set), INV-12 (identity from the session only). Plan tasks: a new task proposed as **REC-09**; it follows REC-03.
- Behaviour before: The Record can be reconstructed per correlation by REC-03. There is no neutral export of one correlation's Record for the comparison arms' `audit_record`, and no task row covers it. The ruling that C1 owns the export (with EL reviewing) is in `benchmark/environment-capabilities-v1.md` §11 (noema#248, "ruling of 8 Nov 2026"); the rulings of 8 Nov are recorded in docs#140 (IL's R7 is ruling A93).
- Behaviour after: A read-only adapter in `services/core/record/` (new package `record/export`) turns one correlation's Record into the neutral `audit_record` of `benchmark-arm-result.v1`: per step, seq, time, step name, actor, evidence ids, inputs digest, outputs digest, decision and outcome; plus a digest of the whole. It reads only through the existing tenant-bound `record_read` path; the tenant comes from the session (INV-12); a span whose chain does not verify is refused, not exported (as in REC-03).
- Safety and security impact: none to a Tier 0 gate. It is read-only, adds no migration, no contract change, no dependency and no role. It must show nothing from the oracle or the held-out set (INV-22). The export is arm-facing, so it needs the Security Reviewer's check on what it exposes.
- Tests added or changed: for a sample of cases a reviewer reconstructs the decisions from the export alone; the export digest is stable across two runs on the same Record; a chain that does not verify is refused; a cross-tenant call is refused. All failing first (AGENT-11).
- Schedule and dependency impact: **proposed task REC-09** · owner C1 · reviewer EL · Needs REC-03 and the contract `benchmark-arm-result.v1` (noema#249, still Draft) · Done when the two tests above pass. It blocks §11 of noema#248 and any Noema-arm run scored on `audit_record`. WIP: it counts as one open P0-path PR for C1 while open (AGENTS §3); that limit is the Founders'.
- SoT or PERD text changes: no.
- Decision owner: Founders (plan §19).
- Decision record: [DEC-2026-11-08-rec-09-record-export](../../../decisions/DEC-2026-11-08-rec-09-record-export.md).
- Migration and rollback: none; delete the package to roll back.

**What the Founders are asked:** approve the new task REC-09 as above, or say which existing task covers it. On approval I add it in a plan version file with the regenerated `tasks.csv` and the task card, in one change set.
