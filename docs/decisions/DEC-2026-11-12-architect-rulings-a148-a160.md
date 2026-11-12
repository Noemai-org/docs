# DEC-2026-11-12 · Architect rulings A148 to A160 (the answers to noema#441, #443, #445, #454, #456, #458, #459 and #461)

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Thirteen rulings, A148 to A160 (§1). Each states what it supersedes. |
| **Closes** | The questions on noema#441, #443, #445, #454, #456, #458, #459 and #461 (each asker closes its own issue). |
| **Supersedes** | Per ruling, in §1. In short: A153 replaces the unassigned "RCV-02 spend check" ledger note; A159 changes plan rows GOV-08 and GOV-10; A160 corrects `AGENTS.md` §11 and PERD §71.2. |
| **Amends** | New PERD version `docs/poc/perd/NOEMA_POC_PERD_v1.23.md` (A160, §71.2 only; v1.22 unchanged); new plan version `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.17.md` (A159) with the change request [CR-2026-11-12-A159-gov-decisions](../poc/execution/change-requests/CR-2026-11-12-A159-gov-decisions.md); `AGENTS.md` §11 (A160). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 12 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: CR-2026-11-12-A159-gov-decisions; the questions on noema#441, #443, #445, #454, #456, #458, #459, #461
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A148 to A160
- Decision: §1
- Rationale and evidence: the Architect's answers of 12 Nov 2026 relayed by the Founder; the issues named above
- Affected requirement IDs / SoT sections: REQ-SEC-001, REQ-SEC-004, REQ-INT-003, REQ-EXP-003, REQ-BEN-003, REQ-AGT-004, REQ-AGT-001; INV-12; AGENT-13, AGENT-15, AGENT-29; SoT §0.4
- Migration notes: A151 (0022) and A153 (0023) assign migration numbers; see §2 for a clash with an earlier assignment
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A148** | noema#443's four defaults are accepted: a read is final when the ledger, switch and destination reads all return KNOWN status; no settlement item in the slice; scope strings and payload shape as written in noema#443. | Nothing. |
| **A149** | **Session fields.** C1 adds three fields to the edge principal in noema#450's follow-up: `principal_type` mapped from the single role (customer, ops→operator, audit→auditor, approver); `asserted_by` = the verified issuer; `authn_ref` = a hash of the token's kid, sub and iat (never the token). **Creation event:** `INPUT_RECEIVED` is the investigation's creation event, appended first (Record first). | Nothing. |
| **A150** | `Components.Edge` in `compose.go` becomes an `http.Handler`. The role list is per route inside `edge.Load`. The ops→operator and audit→auditor mapping is accepted. | Nothing. |
| **A151** | **Admitted-intent store.** C2 builds it: one table with a migration (number 0022), RLS plus FORCE (A136), writer `orchestrator_rw` (D10 pattern). EL reviews. | Nothing. See §2 on the number 0022. |
| **A152** | Benchmark principals use the A1 roles only (customer, ops, approver, audit). Codex found on merged noema#198 that the benchmark's session provider still uses viewer and ops_agent, so those sessions cannot be issued. BO fixes now, failing-first. | Nothing. |
| **A153** | RCV-02 enforcement lives in the database (budget key: tenant, correlation, capability, target, counting `DISPATCH_ATTEMPTED`). C1 owns it, migration 0023. | **The ledger note on noema#183 that "RCV-02 spend check (A5)" is unassigned.** |
| **A154** | **Redaction:** mask digit runs of 8 or more to their last four. One constant is shared by the core and the model service. **Correlation ID:** the edge generates it. A client-supplied value must match `<prefix>_<ULID>` or is replaced. EL fixes (noema#458). | Nothing. It sets the number the AGENT-13 rule ("mask to the last four digits") leaves open. |
| **A155** | **EXP-01:** the `{fact:<kind>}` slot syntax in pack templates is approved, including `{fact:account}`. A `FactsSource` interface with a fake for tests. EL builds the real facts source in the orchestrator (STM-01). The pack edit needs one Founder approval. | Nothing. |
| **A156** | MEM-02's link format (`Regression case: <case ID or test file>`) is accepted as the default. BO drafts the open-decision entry. The workflow wiring is a separate PR after noema#452 merges. | Nothing. |
| **A157** | **EXE-05:** C1's allowlist extends to `services/core/adapters/**`. Capability descriptors in `packs/fintech/capabilities/**` need one Founder approval. Outcome predicates for evidence and complaints belong to OUT-02 (C2). | The EXE-05 task card's allowlist where it is narrower. The card file is not edited here. |
| **A158** | Go-side pattern validation at the core boundaries is C2's, extending the UND-04 gate. | Nothing. |
| **A159** | **GOV decisions.** GOV-03 done (Benchmark Owner Osemwota Osagie Anthony; access list = him and the Founder only). PRE-05 done. GOV-08 loses reviewer contracting but keeps the OQ-12 Africa/Lagos time-zone confirmation. GOV-10 uses the field contributors. Plan v1.17 by change request. | **Plan v1.16 rows GOV-08 (reviewer contracting) and GOV-10 (reviewers), and the OQ-12 sentence "reviewers contracted before labels freeze" (DEC-2026-10-17, OD-P-25) in so far as it requires contracted reviewers.** |
| **A160** | `AGENTS.md` §11 and PERD §71.2 are corrected from "two human reviews" to A143, with the noema re-point. | **The "two human reviews" sentence of `AGENTS.md` §11 and the "Code review" row of PERD §71.2**, both already superseded in effect by A143. |

## 2. What the Steward did where the rulings are silent, and what needs the Architect

- **A151 against an earlier number (needs the Architect).** The ledger has given **0022** to noema#410 (the evidence-set binding, A119) since 10 Nov (noema#416). A151 also names 0022 for the admitted-intent store. Both cannot take 0022. The Steward changes no assignment and asks the Architect which keeps 0022 and which takes the next free number after 0023.
- **A159 and statuses.** `tasks.csv` status fields stay as they are. A159 says GOV-03 and PRE-05 are done, but the plan requires a linked piece of evidence for Done (AGENTS §9). The Steward sets the status when the owners link the evidence (the access list for GOV-03, the delivery for PRE-05). The change request edits only the GOV-08 and GOV-10 rows.
- **A159 and the person named.** The name in A159 is recorded as given, for the GOV-03 row's evidence.
- **A160.** `AGENTS.md` §11's "Reviews" line now states the A143 gates; PERD v1.23 changes only the §71.2 "Code review" row. The `noema` copy of `AGENTS.md` and `CLAUDE.md` is re-pointed after this merges (REQ-OPS-005).
- **A156 and A149.** The open-decision entry for MEM-02 is BO's. The Steward adds no entry.
- **Closing.** Each asker closes its own issue once this merges.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109 to A128 and Block F | the earlier records (merged) | |
| DEC-2026-11-11-architect-rulings-a129-a147 (merged) | A129, A135 to A147 | |
| This record | A148 to A160 | **A161** |
