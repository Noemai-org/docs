# Architecture map

> **Derived, non-normative** (DEC-2026-10-31-proof-depth-and-completeness D1). This map exists so that the names used in conversation lead straight to the canonical component, the governing text, the code and the work. It defines nothing. If it disagrees with the SoT or the PERD, they win and this file is wrong. The **Status** column is filled only from evidence by the Repo Steward (task OPS-09) and kept current as work merges; `Unassessed` means nobody has checked yet, not that nothing exists.

Governing versions: SoT v1.10, PERD v1.19, plan v1.10.

## How to read it

| Column | Meaning |
|---|---|
| Term in use | The name people use in discussion |
| Canonical name | The SoT name used in code, contracts and documents (PERD §18.2) |
| Governing text | Where the behaviour is defined |
| Code path | Where it lives in `noema` (PERD §64.2) |
| Tasks | `tasks.csv` IDs that build or prove it |
| Owner role | The role title that owns those tasks; the role agent executes under it |
| Status | From OPS-09 only, with an evidence link |

## Understanding (model service)

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Input / voice adapter | Input Gateway; voice pipeline | SoT §14; PERD §19.3, §35; REQ-INP-*, REQ-VOI-* | `services/model/noema_model/understanding/gateway/`, `voice/` | UND-01, UND-02, VOI-01 to VOI-18 | C2, V | Unassessed |
| Intent engine | Intent Compiler (+ deterministic lexicon) | SoT §14, §43.1; PERD §20; REQ-INT-* | `understanding/compiler/`, `packs/fintech/lexicons/` | UND-03, UND-05, UND-06, UND-08 | C2 | Unassessed |
| Context engine (session, history, prior cases) | **Context Fabric** | SoT §14, §35.1 (v1.10); REQ-CTX-009, REQ-CTX-010 | `understanding/pipeline/` with core reads through the Evidence Layer | UND-09, UND-10, INP-01 | C2 | Unassessed |
| Context engine (entity part) / disambiguation | **Entity Resolution**; ambiguity lifecycle; clarification | SoT §14; PERD §22.1; REQ-AMB-001 to 007; INV-06 | `understanding/resolution/`, `services/core/evidence/candidates_api/`, `packs/fintech/templates/` | AMB-*, UND-11 | C2 (gate in Trust: EL) | Unassessed |
| Model boundary / schema gate | Schema gate in both services | PERD §19.2; REQ-INT-002; INV-02 | `understanding/pipeline/`, core intake | UND-04 | C2, C1 | Unassessed |
| Model providers | Provider adapters; model harness | SoT §17; PERD §36; REQ-INT-006 | `providers/llm/`, `harness/` | UND-03, UND-12, UND-13 | C2 | Unassessed |
| Explanation | Explanation Engine (not a power) | SoT §14; PERD §31; REQ-EXP-* | `services/model/noema_model/explanation/` | EXP-*, EXP-06 | C2 | Unassessed |

## Trust (core service)

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Context engine (evidence part) | **Evidence Layer** (utility) | SoT §14, §43.5; PERD §21; REQ-CTX-001 to 008 | `services/core/evidence/{layer,freshness,candidates_api}/` | EVD-*, ENV-10 | C2 | Unassessed |
| State reconstruction; contradictory and fragmented state | **State Reconciliation** (decision-time); sealed context snapshot | SoT §14; PERD §21.3, §22.3; REQ-RES-001 to 005; INV-19, INV-20, INV-23 | `services/core/trust/reconcile/`, `packs/fintech/recon_rules/` | RES-01 to RES-05, PCK-05 | C2 (rules data: EL) | Unassessed |
| Trust engine | Authority Engine, Policy Engine, Risk and Clock Evaluation, Decision Maker | SoT §14; PERD §23; REQ-TRU-001 to 012 | `services/core/trust/{authority,policy,clocks,decide}/` | TRU-01 to TRU-12 | EL | Unassessed |
| Authorisation, permissions, confused deputy | Three-layer, target-bound authority | REQ-TRU-003; SoT §25.5 (positioning) | `services/core/trust/authority/` | TRU-04 | EL | Unassessed |
| Confirmations | Confirmation contract | SoT §43.2a; REQ-TRU-009; INV-25 | `services/core/trust/confirm/` | TRU-07 | EL | Unassessed |
| Grants (the trust envelope) | Decision Grant | SoT §43.2; REQ-TRU-008; INV-03 | `services/core/trust/grants/` | TRU-05, TRU-08 | EL | Unassessed |
| Identity and authentication | Synthetic IdP; session authentication; identity from the session only | REQ-SEC-001, REQ-INP-002; INV-12 | `services/core/edge/` | EDG-01 | C1 | Unassessed |

## Execution (core service)

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Action Graph | **Enterprise Action Graph** (pack data, never an API catalogue) | SoT §14, §43.9; PERD §24; REQ-AG-001 to 003 | `packs/fintech/graph/` (data), `tools/packcheck/` | PCK-01, PCK-02, PCK-04 | EL | Unassessed |
| Planner | Deterministic Planner | PERD §26; REQ-PLN-*, REQ-AG-003 | `services/core/execution/planner/` | PLN-01 to PLN-03 | C1 | Unassessed |
| Capability catalogue | Capability Registry (pack data plus core loader) | SoT §34.3, §43.8; PERD §25; REQ-CAP-001 to 005 | `services/core/execution/registry/`, `packs/fintech/capabilities/` | EXE-01, CAP-01 to CAP-03 | C1 | Unassessed |
| No duplicate effects under timeouts | Execution Controller: idempotency key before the call, single-transaction spend, OUTCOME_UNKNOWN | SoT §35.5; PERD §27; REQ-EXE-*; INV-07, INV-08, INV-24 | `services/core/execution/controller/` | EXE-02 to EXE-08, TST-05 | C1 | Unassessed |
| Recovery and compensation | Closure and Recovery Trigger; recovery decisions; recovery playbook; declared compensation | PERD §30; REQ-RCV-001 to 005; REQ-CAP-004 | `services/core/execution/recovery/` | RCV-01 to RCV-04, CAP-02 | C1 | Unassessed |
| Durable runner | Temporal workers | SoT §35.6; INV-30 | `services/core/workflows/` | OUT-03, OUT-05 | C1 | Unassessed |

## Outcome (core service)

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Independent verification | Outcome Verifier; Outcome Watch | SoT §13.1, §14; PERD §29; REQ-VER-*; INV-04, INV-28 | `services/core/outcome/{verifier,predicate,watch,callbacks}/` | OUT-01 to OUT-05 | C2 (Temporal parts: C1) | Unassessed |
| Honest unknown | OUTCOME_UNKNOWN, UNKNOWN verdicts and decisions | BD-10; INV-07, INV-13, INV-19 | across Execution, Outcome, Explanation | covered by US-06, US-16, US-17 | — | Unassessed |

## Record (independent)

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Audit, provenance, "Prove", regulator-grade evidence | Causal Record; reconstruction API; authenticated writers; external anchoring | SoT §14, §43.6, OD-06; PERD §32; REQ-AUD-001 to 007; INV-10, INV-11 | `services/core/record/{chain,reconstruct,verify}/` | REC-01 to REC-08, SEC-13, SEC-14 | C1 | Unassessed |
| Operational memory | Operational Memory (minimal; labelled pairs; escalation resolutions) | SoT §14, §35.1; PERD §33; REQ-MEM-001 to 004 | `services/core/record/memory/` | MEM-01 to MEM-04 | C1 | Unassessed |

## Packs, taxonomies and the human loop

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Intent, Trust and Outcome taxonomies | The three taxonomies in each Vertical Pack | SoT §15; BD-06 | `packs/fintech/{intents,trust,outcomes}/`; conformance packs `packs/{telecom,insurance,healthcare_admin}/` | PCK-01 to PCK-03 | EL | Unassessed |
| Human-in-the-loop escalation | Escalation into the enterprise's case system with the operator evidence packet; approvals by confirmation | DEC-2026-10-31 D2; REQ-EXP-004; SoT §43.2a | `ROUTE_TO_INTERNAL_OWNER`, `RECORD_INVESTIGATION_EVIDENCE` | EXP-05, EXP-06 | C2 | Unassessed |
| The bank's case system (in the POC) | `mock-case`, a test-environment component (not a Noema console) | REQ-ENV-008 | `synthetic/mock_case/` | ENV-08 | IL | Unassessed |
| Demo evidence panel | Ops and audit inspector (POC-FR-17) | PERD §40.2 | `ui/inspector/` | UI-* | FE | Unassessed |
| Operations console | Studio and maker-checker approvals | PLAT-FR-15, PLAT-FR-17 | post-POC | — | — | Not in the POC |

## Proof and testing

| Term in use | Canonical name | Governing text | Code path | Tasks | Owner role | Status |
|---|---|---|---|---|---|---|
| Scorecard (four tiers) | Tier 0 safety gates; Tier 1 terminal handling with diagnostics (incl. pass^k, disambiguation); Tier 2 autonomy curve; Tier 3 economics and latency | SoT §38; PERD §48.3; REQ-BEN-009 | `benchmark/scoring/` | BEN-*, BEN-30 | B | Unassessed |
| Chaotic enterprise simulation | Hostility proxy fault families; `mock-case` faults; chaos matrix; crash-point matrix | REQ-ENV-005; REQ-TST-008, REQ-TST-009; SEC-10 | `benchmark/hostility_proxy/`, `synthetic/mock_case/` | ENV-09, ENV-15, TST-05, TST-06, SEC-10 | IL, SR, B | Unassessed |
| Integration suite | US-01 to US-22, full suite, evil provider, chaos | PERD §45, §48, §49 | `benchmark/` | BEN-12, BEN-16, BEN-29, SEC-06 | B | Unassessed |
| Comparison arms | Arms A, B, D (and A0) | SoT §38.5; PERD §50 | `benchmark/arms/` | ARM-*, BEN-24 | ARM, REV (external people) | Unassessed |
