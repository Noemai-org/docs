# DEC-2026-11-07 · Founder decisions D1 to D14 (Block D)

| | |
|---|---|
| **Status** | **Decided by the Founders on 7 Nov 2026 (Block D); recorded by the Repo Steward.** Counts as committed once both Founders approve and merge this pull request (AGENTS §2, item 3). |
| **Date** | 7 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | D1 to D14 in §1. |
| **Closes** | OD-P-54 is answered by A31 (DEC-2026-11-07-architect-rulings); nothing else is closed by this record. |
| **Amends** | `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.12.md` (new; v1.11 unchanged) and PERD v1.21 §48.1 (both in this pull request, D1 and D3). D7 amends ruling A38. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Naming.** These are the Founders' decisions D1 to D14 of Block D. They are not the Architect's rulings D1 to D8 of DEC-2026-11-05. Cite them as "Block D, D5" to avoid confusion.

**Record fields (decisions README template).**

- Status: Decided 7 Nov 2026; counts once both Founders approve and merge this pull request
- Date: 7 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1, as the Founders gave it
- Rationale and evidence: given in the Founders' message of 7 Nov 2026; the Repo Steward added none. Where a row records an effect on a document, it is marked "Steward's reading".
- Affected requirement IDs / SoT sections: see the "Effect" column
- Migration notes: D12 fixes the migration numbers; D7 and D8 change what open `noema` pull requests must do
- Supersedes: ruling A38 in part (D7)

---

## 1. The decisions

| ID | Decision (as given) | Effect |
|---|---|---|
| D1 | docs#130 issues SoT v1.11 and PERD v1.21 after the Steward fixes the Engineering Lead's six wording findings and adds a plan v1.12 so every document agrees on the gate count. Reviewers: EL, SR, Voice. | Done in this change set: PERD v1.21 §48.1 reworded; plan v1.12 written. Issuing v1.11 is the Founders' act. |
| D2 | Wrong transaction, credential leakage and cross-tenant exposure are all zero-tolerance gates. | Already in SoT v1.11 §38.3 (13 gates; wrong transaction was gate 1 "unsafe consequential actions" and is also named in the result fields). Steward's reading: no further text change. |
| D3 | The 320 generated cases are the regression layer, never the release result. The release result comes from the RESOLVE and RESIST measured sets. pass^k repeats do not add to n. Each gate reports "0 of N, upper 95% bound 3/N" with its own N. | PERD v1.21 §48.1, in this change set. The exact bound 1 − 0.05^(1/N) is also recorded beside 3/N. |
| D4 | The F1 to F11 scope (Brief v1.0, not in the repo) is superseded by suite definition v1 and Brief v1.1. | Closes the "F1 to F11 not found" item in the suite definition (DEC-2026-11-07-benchmark-suite-definition-v1 §3). Brief v1.1 is not in the repo either; the Founders should commit it or confirm that the suite definition is enough. |
| D5 | The verifier may set a tenant's kill switch; only a person clears it. | Refines PERD REQ-EXE-008 and the `KILL_SWITCH_CHANGED` audit event. Steward's reading: a PERD text alignment is owed (see §2). |
| D6 | The model service holds no Record key; core-edge signs and appends its events. | Consistent with INV-29 and OD-P-73's default. Steward's reading: OD-P-73 can be closed by this decision for the model-service identity; the adapter emitters need a separate answer. |
| D7 | compose-scripts.yml belongs to #257; #181 drops its copy. DB scripts run on PostgreSQL 17.11; test_secrets_local.sh may run on the runner (it needs no database). A38 is amended accordingly. | Owners of noema#257 and noema#181 act. A38 is amended by this row. |
| D8 | No eager grant void. E4 voids at execution. Only execution_rw writes decision_grant.status. DEBT-23 stays open. | Matches PERD §28.2 E4. No document change; DEBT-23 unchanged. |
| D9 | Nightly evidence recompute uses a new read-only login `evidence_verify` (SELECT only; a named exception like `record_verify`; SR reviews). | A new database role. Steward's reading: it needs a PERD §38 mention and an SR review before merge (see §2). |
| D10 | MEM-01: rename the required contract field to `provenance_ref`; writer role `orchestrator_rw` only; observation fields typed scalars. | A contract change in `noema` with the AGENT-15 steps (version bump, migration note, regenerated models). |
| D11 | After a parent merges, a clean merge of main into a child with an unchanged own diff and green CI keeps its Codex READY. | Working practice for Rule 9 stacks. Steward's reading: the PR must still show that its own diff is unchanged. |
| D12 | Migration numbers: 0012 noema#168, 0013 noema#229, 0014 noema#233, 0015 noema#259, 0016 noema#234, 0017 noema#261, 0018 noema#263. If merge order changes the later PR renumbers. | Supersedes the migration ledger on noema#183 (A34); the Steward updates it. |
| D13 | R7: if authority depends on facts the pack lacks, escalate and do not act (OD-P-78). | Decides OD-P-78's question. The pack data PR is docs#132 (its owner closes the entry). |
| D14 | Control-plane route names: EL proposes from PERD §39; SR accepts. | A hand-off between roles; no document change here. |

## 2. Alignment owed (Steward's reading, not a decision)

D5 and D9 name behaviour that the PERD text does not yet state: REQ-EXE-008 (who may set and clear the switch) and §38 (the `evidence_verify` login). D13 decides OD-P-78. AGENT-29 asks for a matching text edit in the same change. The Steward has not made these edits because they change P0 requirement text; the Founders should say whether to fold them into PERD v1.21 before issue, or into a v1.22.

## 3. Date rule

Everything in Block D is finished on 7 Nov 2026. No date moves unless something external is needed (Tushe, vendors, devices, a Founder signature).
