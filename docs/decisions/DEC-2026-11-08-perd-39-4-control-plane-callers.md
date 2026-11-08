# DEC-2026-11-08 · PERD §39.4: the reconstruction and record-verify routes stay audit-only (ruling A110, option A)

| | |
|---|---|
| **Status** | **Decided by the Founders on 8 Nov 2026 (option A); recorded by the Repo Steward.** Counts once both Founders approve and merge this pull request (AGENTS §2, item 3). |
| **Date** | 8 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | `GET /v1/reconstructions/{correlation_id}` and `GET /v1/record/verify?tenant_id=` (rows 10 and 11 of the SEC-04 matrix, docs#134) stay callable by `audit` only, as PERD §39.4 says. |
| **Closes** | The withdrawn widening in OD-P-79 finding 3 (docs#133): it is not adopted. |
| **Amends** | **Nothing.** No PERD v1.22 file. The matrix (docs#134) is unchanged. |
| **Supersedes** | Nothing. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 8 Nov 2026 (option A); counts once both Founders approve and merge
- Date: 8 November 2026
- Closes: the widening of OD-P-79 finding 3 (not adopted)
- Owner: Founder and Technical Co-Founder
- Decision: ruling A110, option A
- Rationale and evidence: the Founders' message of 8 Nov 2026 on docs#141, §1
- Affected requirement IDs / SoT sections: PERD §39.4; ruling A20 (DEC-2026-11-06); REQ-SEC-001; INV-12
- Migration notes: none
- Supersedes: nothing

---

## 1. The ruling

| ID | Ruling |
|---|---|
| **A110** | The Founders choose **option A: stay audit-only.** Reasons given: neither route exists yet; widening later is cheap and narrowing later is not; and options B and C widen `ops` toward the Record against ruling A20. The record is Decided, option A. There is **no PERD v1.22 file** and the matrix (docs#134) is **unchanged**. OD-P-79 is updated to say that rows 10 and 11 stay audit-only (the status line of OD-P-79 is in docs#133, its owner's pull request; this record is what it cites). |

## 2. What it means in practice

- PERD §39.4 stands as written for these two routes: `reconstructions` and `record/verify` are `audit`; `ops` has no path to them.
- The SEC-04 matrix tests rows 10 and 11 as audit-only (the `ops` cells stay refused with the not-found shape).
- Any later widening needs a new decision record that names the class and the tenant rule, and the matrix cells change in the same change set.

## 3. The options that were not chosen

- **B:** widen `record/verify` only to `ops` (own tenant).
- **C:** widen both routes to `ops` (own tenant), which gives `ops` case content.
Neither is built and neither needs undoing.

## 4. The Steward's ledger

A110 follows A109 (DEC-2026-11-08-rec-09-record-export, docs#142). Next free after both: **A111**.
