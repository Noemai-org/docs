# DEC-2026-11-13 · Amendment to Founder decision D14: the publish route uses the segment form (ruling A183)

| | |
|---|---|
| **Status** | **Interim.** Ruled by the Principal Architect on 13 Nov 2026 (A183), with the agreement of the Security Reviewer and C1 and the decision of the Engineering Lead (noema#505); recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111). |
| **Date** | 13 November 2026 |
| **Owner** | Principal Architect; Founders (D14) |
| **Decides** | The spelling of one control-plane route (§1). |
| **Closes** | The spelling question on noema#505 (item 2). |
| **Supersedes** | In Founder decision D14 (Block D, `DEC-2026-11-07-founder-decisions-block-d`) as carried by OD-P-79: the route `POST /v1/admin/policies/{policy_id}/versions/{v}:publish`. |
| **Amends** | OD-P-79 (docs#133); the control-plane authorization matrix row 5 (`docs/security/control-plane-authz-matrix.md`). PERD §39.4 carries the old spelling and changes in the next PERD version (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 13 November 2026
- Closes: the spelling question on noema#505
- Owner: Principal Architect; Founders
- Decides: the segment form for the publish route
- Decision: §1
- Rationale and evidence: noema#505 (the Security Reviewer's need, C1's recommendation, the Security Reviewer's agreement, EL's decision); ruling A183
- Affected requirement IDs / SoT sections: REQ-SEC-006 (control plane), INV-26; PERD §39.1, §39.4; Founder decisions D5, D14; SEC-04, ADV-14
- Migration notes: none. No control-plane route is built yet; the admin listener's route table is written against the segment form in its own task
- Supersedes: see the Supersedes row above

---

## 1. The amendment

The policy-publication route is spelled **`POST /v1/admin/policies/{policy_id}/versions/{v}/publish`** (a whole-segment wildcard), not `.../versions/{v}:publish`.

**Why.** Go's `http.ServeMux` (Go 1.22) accepts a wildcard only as a whole path segment, so `{v}:publish` cannot be registered. The two options on noema#505 were (a) the segment form and (b) a dedicated matcher on the admin listener. (a) needs no new dependency, changes no cell of the control-plane matrix, and does not put code that decides who may publish a policy into a custom matcher. The Security Reviewer and C1 recommended (a); the Engineering Lead decided (a); the Architect ruled (a) (A183).

**What does not change.** The credential class (C-ADMIN only), the 401 for defective tokens, the not-found shape for every refused class, the INV-26 transaction and the 409 `POLICY_VERSION_NOT_NEWER` behaviour of OD-P-79 stand. The other routes keep their spelling: `.../kill-switch:set`, `.../kill-switch:clear` and `packs:load` end in a literal segment and register as written.

## 2. What the Steward changed and what waits

- **Changed in this pull request:** the publish route line in OD-P-79 and row 5 of the control-plane authorization matrix.
- **Waits:** PERD §39.4 (line `POST /v1/admin/policies/{policy_id}/versions/{v}:publish`) is part of the PERD and is never edited in place. It changes in the next PERD version after PERD v1.24 (proposed in docs#168), by a new version file. Until then the matrix and this record carry the amendment, and the code follows A183.
