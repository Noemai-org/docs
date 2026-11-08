# DEC-2026-11-08 · PERD §39.4: callers of the reconstruction and record-verify routes (DRAFT amendment)

| | |
|---|---|
| **Status** | **Draft prepared by the Repo Steward. Not a decision, not in force.** It becomes a decision only when both Founders approve and merge it with one of the options chosen in §3. Prepared on the instruction recorded in the SEC-04 matrix (docs#134, open question 2): rows 10 and 11 stay audit-only until the PERD is amended, and the Steward prepares the amendment. |
| **Date** | 8 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | Whether `GET /v1/reconstructions/{correlation_id}` and `GET /v1/record/verify?tenant_id=` (matrix rows 10 and 11) may be called by a class other than `audit`, and from when. |
| **Closes** | The part of OD-P-79 that EL withdrew on 7 Nov (docs#133, finding 3), if option B or C is chosen. |
| **Amends** | If approved: a new PERD version file (v1.22, the PERD is never edited in place) changing the two rows of §39.4 below. Nothing is edited by this draft. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Draft, not in force; counts only once both Founders approve and merge it with an option chosen
- Date: 8 November 2026
- Closes: the withdrawn widening in OD-P-79 finding 3 (if B or C)
- Owner: Founder and Technical Co-Founder
- Decision: one of options A, B, C in §3
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: PERD §39.4, REQ-SEC-001, REQ-SEC-006 (tenant), REQ-AUD-*; ruling A20 (DEC-2026-11-06); INV-12
- Migration notes: a PERD v1.22 file and the regenerated PERD index; the matrix (docs#134) flips the `ops` cells of rows 10 and 11 in the same change
- Supersedes: nothing

---

## 1. What is in force today

PERD §39.4 (v1.21, in docs#130): `GET /v1/reconstructions/{correlation_id}` and `GET /v1/record/verify?tenant_id=` are callable by `audit` only. OD-P-79 (docs#133) keeps them audit-only: EL's wider "ops and audit" was withdrawn after the Security Reviewer's finding 3 (it widens `ops` toward the Record, against the spirit of ruling A20). The matrix (docs#134) tests rows 10 and 11 as audit-only. The credential classes C-ADMIN and C-VERIFY are ruled (A54) but no control-plane route or listener is built (TRU-08 slice 2).

## 2. Evidence for the amendment

- A20: `audit` reads only through tenant-bound Record read functions; `ops` acts within its own tenant and has no path to a Record writer (D7 items 7, 10, 11).
- `record/verify` returns chain verification status (a verdict and counts), not case content; `reconstructions` returns the causal chain of one correlation (case content).
- C-VERIFY is a set-only, kill-switch-only service credential (A54, OD-P-79); the verification job reads the Record through a database login (`record_verify`), not through HTTP.
- Neither route exists yet; the choice costs nothing to change before the control plane is built.

## 3. The options (the Founders choose one; nothing else is changed)

**Option A: stay audit-only.** No amendment. The matrix keeps its PERD reading. Simplest and the safest; the cost is that `ops` cannot see a chain-verification result through this API (they see alerts via `GET /v1/ops/alerts`).

**Option B (Steward's recommendation): widen `record/verify` only.** Replace the row with `GET /v1/record/verify?tenant_id=` · **ops, audit (own tenant)** · Chain verification status. For both classes `tenant_id` must equal the token's tenant, otherwise the not-found shape (INV-12, D7 item 7). `reconstructions` stays `audit`. Reason: the verification status carries no case content, so it does not widen `ops` toward the Record's contents (A20), while `ops` is the class that acts on an alert about a failed chain. It takes effect only when the conditions in §4 hold.

**Option C: widen both rows to `ops, audit (own tenant)`.** This is EL's withdrawn proposal. It gives `ops` the causal reconstruction of a correlation, which is case content; the Security Reviewer said this goes against A20's spirit. It needs a Founders' reason recorded here.

Replacement text for the two rows if B is chosen (C would also change the first row):

| Endpoint | Role | Purpose |
|---|---|---|
| `GET /v1/reconstructions/{correlation_id}` | audit | US-12 reconstruction |
| `GET /v1/record/verify?tenant_id=` | ops, audit (own tenant) | Chain verification status; `tenant_id` must equal the token's tenant |

## 4. Conditions before it takes effect

1. C-ADMIN and C-VERIFY exist: the separate control-plane listener and the service identity are built (TRU-08 slice 2; OQ-09 key per identity).
2. The SEC-04 matrix test (docs#134) passes with the `ops` cells of the chosen rows flipped to allowed, including the cross-tenant cell (`ops-other` gets the not-found shape) and the "handler never runs on a refusal" check.
3. A new PERD version file (v1.22) carries the changed rows, with the regenerated PERD index and an Appendix entry; this record is cited by it.
4. The Security Reviewer gives reviewer-role READY on the matrix and the amendment.

## 5. What the Founders are asked

Choose A, B or C. My recommendation is **B**, for the reasons in §2. If you choose B or C, say so in the WAITING issue and I will turn this draft into the decision record and prepare the v1.22 file in the same change set (AGENT-29), to be taken only when §4 holds.
