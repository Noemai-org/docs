# DEC-2026-11-12 · Architect rulings A148 to A161 (the answers to noema#441, #443, #445, #454, #456, #458, #459 and #461)

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Fourteen rulings, A148 to A161 (§1). Each states what it supersedes. |
| **Closes** | The questions on noema#441, #443, #445, #454, #456, #458, #459 and #461 (each asker closes its own issue). |
| **Supersedes** | Per ruling, in §1. In short: A153 replaces the unassigned "RCV-02 spend check" ledger note; A159 changes plan rows GOV-08 and GOV-10; A160 corrects `AGENTS.md` §11 and PERD §71.2. |
| **Amends** | New PERD version `docs/poc/perd/NOEMA_POC_PERD_v1.23.md` (A160, §71.2 only; v1.22 unchanged); new plan version `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.17.md` (A159) with the change request [CR-2026-11-12-A159-gov-decisions](../poc/execution/change-requests/CR-2026-11-12-A159-gov-decisions.md); `AGENTS.md` §11 (A160). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 12 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: CR-2026-11-12-A159-gov-decisions; the questions on noema#441, #443, #445, #454, #456, #458, #459, #461
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A148 to A161
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
| **A154** | **Redaction.** One shared constant, the maximum unmasked digit run is 4, on every outward surface (logs, traces, API and error bodies, explanation text, served facts, model prompts, UI feed), per PERD explanation criterion 4 and the error-body criterion. The redactor masks any longer run to its last four, including full-width and Arabic-Indic digits. Exemptions are by type only: typed IDs, RFC 3339 timestamps, number-typed structured fields; list owned by SR with a test per entry; one Founder approval. Amounts in explanation text use thousands separators. The edge generates the correlation ID; a client value must match `<prefix>_<ULID>` or is replaced. EL fixes (noema#458). | **The earlier text of A154, "mask digit runs of 8 or more to their last four" (the first version of this record).** Nothing else. |
| **A155** | **EXP-01:** the `{fact:<kind>}` slot syntax in pack templates is approved, including `{fact:account}`. A `FactsSource` interface with a fake for tests. EL builds the real facts source in the orchestrator (STM-01). The pack edit needs one Founder approval. | Nothing. |
| **A156** | MEM-02's link format (`Regression case: <case ID or test file>`) is accepted as the default. BO drafts the open-decision entry. The workflow wiring is a separate PR after noema#452 merges. | Nothing. |
| **A157** | **EXE-05:** C1's allowlist extends to `services/core/adapters/**`. Capability descriptors in `packs/fintech/capabilities/**` need one Founder approval. Outcome predicates for evidence and complaints belong to OUT-02 (C2). | The EXE-05 task card's allowlist where it is narrower. The card file is not edited here. |
| **A158** | Go-side pattern validation at the core boundaries is C2's, extending the UND-04 gate. | Nothing. |
| **A159** | **GOV decisions.** GOV-03 done (Benchmark Owner Osemwota Osagie Anthony; access list = him and the Founder only). PRE-05 done. GOV-08 loses reviewer contracting but keeps the OQ-12 Africa/Lagos time-zone confirmation. GOV-10 uses the field contributors. Plan v1.17 by change request. | **Plan v1.16 rows GOV-08 (reviewer contracting) and GOV-10 (reviewers), and the OQ-12 sentence "reviewers contracted before labels freeze" (DEC-2026-10-17, OD-P-25) in so far as it requires contracted reviewers.** |
| **A160** | `AGENTS.md` §11 and PERD §71.2 are corrected from "two human reviews" to A143, with the noema re-point. | **The "two human reviews" sentence of `AGENTS.md` §11 and the "Code review" row of PERD §71.2**, both already superseded in effect by A143. |
| **A161** | **The input gateway (UND-02) writes `INPUT_RECEIVED` as `core-edge`**, with the tenant from the session and the payload channel, locale and `request_id` as the reconstruction projector reads them. **Record first:** if the append fails, the input is refused. The same `request_id` with the same body writes `INPUT_DEDUPLICATED` (no second `INPUT_RECEIVED`) and returns the original result. The same `request_id` with a different body returns 409 and writes `SECURITY_EVENT` kind `REQUEST_ID_REUSED`. **The orchestrator refuses a turn without a recorded `INPUT_RECEIVED` reference (fail closed).** The follow-up is EL's compose.go wiring PR. | Nothing. It completes **A149**'s creation-event line ("`INPUT_RECEIVED` is the investigation's creation event, appended first (Record first)") by saying who appends it and how a repeat is handled. |

## 2. What the Steward did where the rulings are silent, and what needs the Architect

- **A151 against an earlier number (needs the Architect).** The ledger has given **0022** to noema#410 (the evidence-set binding, A119) since 10 Nov (noema#416). A151 also names 0022 for the admitted-intent store. Both cannot take 0022. The Steward changes no assignment and asks the Architect which keeps 0022 and which takes the next free number after 0023.
- **A159 and statuses.** On the Architect's instruction of 12 Nov, `tasks.csv` sets GOV-03 and PRE-05 to Done (A159 decides them done; the evidence the plan asks for, the access list for GOV-03 and the delivery for PRE-05, is for the owners to link). The change request edits the GOV-08 and GOV-10 rows.
- **A159 and the person named.** The name in A159 is recorded as given, for the GOV-03 row's evidence.
- **A160.** `AGENTS.md` §11's "Reviews" line now states the A143 gates; PERD v1.23 changes only the §71.2 "Code review" row. The `noema` copy of `AGENTS.md` and `CLAUDE.md` is re-pointed after this merges (REQ-OPS-005).
- **A154 against the PERD (closed).** C1 asked in review whether A154 covers only the log redactor, because the PERD says "no unmasked digit runs longer than 4" in two acceptance criteria. The Architect replaced A154's text (§1): the maximum unmasked run is 4 on every outward surface, per those criteria. The earlier "8 or more" text is superseded.
- **A149, A150 and A161 against noema#447 (C1's report).** The orchestrator in noema#447 does not append `INPUT_RECEIVED` first. A161 settles it: the input gateway writes it, and the orchestrator refuses a turn without its reference. noema#447 stays as it is. The code changes (`Runner.RunRead`, the compose.go wiring PR, `status/STM-01.md`) are EL's and are not made by this record.
- **A156 and A149.** The open-decision entry for MEM-02 is BO's. The Steward adds no entry.
- **Closing.** Each asker closes its own issue once this merges.

## 3. A148 in detail: the four ENV-04 evidence defaults, as written on noema#443 and noema#441

noema#460 (C2) asked for the defaults to be in a committed record, because noema#443's reviewer gave a P1 at `89ee1cf`: the evidence-status rules were not decided in a committed record. The Architect's answer on noema#441, as C2 quoted it: "your task card is approved; the four defaults on #443 are accepted as proposed (final read = ledger/switch/destination all read with KNOWN status; no settlement item; scope strings as written; payload shape as written)". The ruling is A148 in §1. The text below is C2's statement of the four defaults; **if the Architect's text differs, the Architect's text governs** and the code follows it.

1. A read is determinate (KNOWN) only when it is final: the ledger has at least one entry and none pending; the switch is terminal and not UNKNOWN; the destination is a credit, not UNKNOWN or PENDING, with a terminal settlement (`REVERSAL_PENDING` is non-terminal, A31). Otherwise UNKNOWN.
2. There is no `fin.src.settlement` item: the destination answer is recorded under the destination source only.
3. `resource_scope` is `<resource kind from the pack>:<transaction ref>`; `principal_scope` is the session principal.
4. The payload is the normalised port answer, with sensitivity from the pack's source descriptor.

**Affected IDs:** REQ-CTX-001, REQ-CTX-002, REQ-ENV-001, REQ-AUD-001; INV-19, INV-23; A31. **Owner:** Principal Architect. **Date:** 12 November 2026.

**What would invalidate it** (C2's statement): a requirement that pending states count as determinate. Then default 1 changes, and the code and its tests change with it by a new ruling.

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109 to A128 and Block F | the earlier records (merged) | |
| DEC-2026-11-11-architect-rulings-a129-a147 (merged) | A129, A135 to A147 | |
| This record | A148 to A161 | **A162** |
