# DEC-2026-11-08 · New task REC-09, the Noema record export (ruling A109)

| | |
|---|---|
| **Status** | **Decided by the Founders on 8 Nov 2026; recorded by the Repo Steward.** Counts once both Founders approve and merge this pull request (AGENTS §2, item 3). |
| **Date** | 8 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | Adds task REC-09 to the plan on the conditions in §1. |
| **Closes** | The change request [CR-2026-11-08-REC-09-record-export](../poc/execution/change-requests/CR-2026-11-08-REC-09-record-export.md) (its Status becomes Approved). |
| **Supersedes** | **Nothing.** Ruling A93 (the record export goes to C1 as owner, with EL reviewing) stands; this record adds the task row and the conditions. |
| **Amends** | New plan version `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.13.md` (v1.12 and v1.11 stay unchanged), the regenerated `tasks.csv`, and the card `task-cards/REC-09.md`. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 8 Nov 2026; counts once both Founders approve and merge
- Date: 8 November 2026
- Closes: CR-2026-11-08-REC-09-record-export
- Owner: Founder and Technical Co-Founder
- Decision: ruling A109 in §1
- Rationale and evidence: the Founders' message of 8 Nov 2026 on docs#142; the Repo Steward added none
- Affected requirement IDs / SoT sections: REQ-AUD-003, REQ-BEN-001, REQ-BEN-009; INV-12, INV-22
- Migration notes: none; delete the package to roll back
- Supersedes: nothing

---

## 1. The ruling

| ID | Ruling |
|---|---|
| **A109** | The Founders approve the new task **REC-09**, the Noema record export (owner C1, reviewer EL), on four conditions: **(1)** the export is a **library function called by the Noema arm runner, not an HTTP route**; if a route is ever wanted it first gets a row in the control-plane matrix (docs#134). **(2)** It Needs REC-03 and the `audit_record` shape in `benchmark-arm-result.v1` (noema#249). **(3)** The Security Reviewer gives reviewer-role READY on what the export exposes (nothing from the oracle or the held-out set, INV-22; neutral fields only) before the C1 pull request leaves Draft. **(4)** In the same change set (AGENT-29): this decision record, the plan version file adding REC-09, the regenerated `tasks.csv` and the task card (owner C1, reviewer EL). |

## 2. What the Steward chose where the ruling is silent

- **Date.** The ruling gave none. REC-09 is placed in the Wednesday 18 November group of plan v1.13; the date moves only by change request (plan §19). C1 may start earlier on the failing tests, because REC-03 is dated Monday 9 November.
- **Priority.** P1 on the card (the export adds no P0 path); the Security Reviewer's READY and two human reviews still apply.
- **The `audit_record` dependency** is not a task; the card says it must be merged or its shape agreed before the PR leaves Draft.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| This record | A109 | **A110** |
| DEC-2026-11-08-perd-39-4-control-plane-callers (docs#141) | A110 | **A111** |
