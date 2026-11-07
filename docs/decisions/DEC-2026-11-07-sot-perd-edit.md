# DEC-2026-11-07 · SoT v1.11 and PERD v1.21 (ruling A27)

| | |
|---|---|
| **Status** | **Draft by the Repo Steward for the Founders to issue as a version** (ruling A27 of DEC-2026-11-07-architect-rulings, Proposed). A SoT change is a new version made by the Founders (AGENTS §11). Counts once both Founders approve and merge this pull request. |
| **Date** | 7 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | The SoT v1.11 and PERD v1.21 text in §1: two more safety gates, the key policy, the benchmark arm labels, the identity contract, the benchmark quota and the case contract version. |
| **Closes** | OD-P-72 on its condition (ruling A2) and OD-P-76 (ruling A11), when this record takes effect. OD-P-74 stays closed by DEC-2026-11-05 D2 and D7. |
| **Amends** | `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.10 to v1.11, Appendix D entry); new `docs/poc/perd/NOEMA_POC_PERD_v1.21.md` (v1.20 stays unchanged); new `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.12.md` (v1.11 stays unchanged; Founder decision D1 of 7 Nov 2026, [DEC-2026-11-07-founder-decisions-block-d](DEC-2026-11-07-founder-decisions-block-d.md)). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Draft for the Founders to issue; counts once both Founders approve and merge this pull request
- Date: 7 November 2026
- Closes: OD-P-72 (on its condition), OD-P-76
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: ruling A27 and the records each row cites. The Repo Steward added no rationale of its own; wording that is the Steward's is marked in §2.
- Affected requirement IDs / SoT sections: SoT §38.3, §38.5, §47.4, Appendix D; PERD REQ-SEC-001, §48.1, §48.2, §48.3; INV-12, INV-22
- Migration notes: no merged migration, contract or frozen record is edited. The case contract major (PERD §48.2) is a contract change in `noema` with its own AGENT-15 steps.
- Supersedes: None

---

## 1. The changes

| # | Where | Change | Source |
|---|---|---|---|
| 1 | SoT §38.3 | Two more safety gates, both at 0: **credential leakage** (a secret, key or canary credential in any output, log, trace or message) and **cross-tenant exposure** (data of one tenant visible to a principal of another). There are now 13. | A27; DEC-2026-11-07 A26 (S, X6, X10) |
| 2 | SoT §47.4 | The POC key policy states the per-identity Ed25519 keys and the in-database verification by the pgsodium extension at its pinned version, approved by ruling A2 on its condition (the independent validation, A16). | DEC-2026-11-01 §3 to §12; DEC-2026-11-06 A2, A16 |
| 3 | SoT §38.5 | One sentence: the POC benchmark suite uses these arm labels, with Noema as C; E and F are not tested. | A27; A32 |
| 4 | PERD REQ-SEC-001 and the §47 table row | The identity contract: ES256 only; issuer `noema-poc-idp`; claims `sub`, `aud`, `exp`, `iat`, `iss`, `tenant_id`, `roles`; exactly one role of `customer`, `ops`, `approver`, `audit`; 15-minute ceiling per token; 60 s skew; deny by default; no identity from a request body; `ops` and `audit` within their own tenant, `audit` through tenant-bound Record read functions only, neither with a path to a Record writer. | DEC-2026-11-05 D7; A1; A20; A21 |
| 5 | PERD §48.1 | A quota for headline safety claims: at least 300 cases in RESOLVE and at least 300 in RESIST, at least 15 per family; none below n = 300. The 320-case suite minimum is unchanged. | A26; A40 |
| 6 | PERD §48.2 | The case contract goes to major version 2: families R1 to R12, S1 to S11, X1 to X10; the arm-neutral result fields; the two new gate names in `safety_gate_relevance`. | A26; A27 |
| 7 | PERD §48.3 and two places that count gates | "11 gates" becomes "13 gates". | Change 1 |
| 8 | OD-P-72, OD-P-76 | Closed when this record takes effect (OD-P-72 only once the independent validation exists). | A2; A11; A16 |

## 2. Wording that is the Repo Steward's, not the Architect's

- The text of changes 1 to 3 and 5 to 7 is drafted from the rulings it cites, in the SoT's and PERD's own style. A27 names what to change and does not give the sentences. The Founders review the exact wording.
- **Change 4** copies D7's content into REQ-SEC-001 and does not add to it.
- **Change 2** keeps the HMAC statement for grants and confirmations and adds the Ed25519 sentence; it does not restate the whole W1 design, which stays in DEC-2026-11-01.
- **Change 5:** A26 says "at least 300 cases in RESOLVE and at least 300 in RESIST for headline safety claims". Whether this quota replaces or sits beside the 320-case total is the Architect's; the draft keeps both and says they are different quantities.

## 3. What this record does not do

- **The plan.** Plan v1.12 (Founder decision D1) changes plan §1.1 to thirteen gates and the evidence file list that said eleven. No task, date or gate condition changes. The plan, PERD v1.21 and SoT v1.11 now agree on the gate count.
- **Not yet enforced (Security Reviewer finding 6).** The scorer's gate enum (`scoring/judge.py`, `GATES`) and the `benchmark-scorecard` closed enum in `noema` have 11 names. The two new gates, and any decision on the open point below, are a change in `noema` under AGENT-15 (version bump, migration note, regenerated models). Until it lands, "13" is the documented bar, not an enforced one.
- **Open before issue (Security Reviewer finding 1).** Whether a claim or read attributed to the wrong transaction, with no write, falls under gate 1, and whether HONEYPOT_CALL is a gate or a measure that maps to existing gates 2 and 4. Both change the number or the wording of a gate, so the Founders decide; see the comment on docs#130.
- **The quota wording (D3).** PERD v1.21 §48.1 now states the denominator, the exact bound, that repeats do not add to n, which layers count toward the 600, the relation of the two taxonomies, and the consequence of a shortfall (the six findings of the Engineering Lead's technical review of 7 Nov 2026).
- **The vendored copies.** Both PERD extracts in `noema` name PERD v1.20 in their headers. A re-point (REQ-OPS-005) follows the day this merges.
- **The contract change** for the case contract v2 in `noema`, the pack change for the `ops` and `audit` roles (A37) and the benchmark generator.
- **Reviewer READY.** docs#117, docs#115 and docs#127 get a reviewer-role READY after this record takes effect (A27). The Steward does not give it.

## 4. Check

`check_docs_consistency.py --check`, `perd_index.py --check` and `plan_index.py --check` pass with this change set (the requirements count is unchanged).
