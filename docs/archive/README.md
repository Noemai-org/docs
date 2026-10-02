# Archive (NON-AUTHORITATIVE)

> **Nothing in this directory is authoritative.** It is kept so that the reasoning behind earlier work is not lost.
>
> - Do not implement, cite or quote from it as current guidance.
> - Do not quote numbers from it (AGENT-18).
> - The only authority is [`../NOEMA_SOURCE_OF_TRUTH.md`](../NOEMA_SOURCE_OF_TRUTH.md) (the SoT), then the order of authority in SoT §0.4.
>
> Every archived Markdown file carries a banner saying this.

## Contents

| Path | What it is | Why it is archived |
|---|---|---|
| [`legacy-canon-2026-09/`](legacy-canon-2026-09/) | The former `noema-canonical/` tree: 174 Markdown documents (CANON, glossary, thesis, ontology, architecture, trust, intent, execution, contracts, interfaces, data, graph, integrations, loops, ai, engineering, enterprise, taxonomy, strategy, product, reference workflow, ADR-001 to ADR-019). Written September 2026, versions 0.1–0.3. | It predates SoT v1.0/v1.1 and is built on a different model of Noema. It contradicts the SoT on the definition of Noema, the architecture, the Trust model, contracts, the first wedge and the taxonomies (see below). |
| [`source-drafts-2026-09/`](source-drafts-2026-09/) | Four PDFs dated 3–8 September 2026: two variants of the *Noema POC — Product + Engineering Specification* (files `_2` and `_3`; `_2` is labelled v1.0, 3 Sep 2026), *NOEMA POC Specification* v1.0 ("Complete Synthesis"), and *Noema Master Company Document FINAL* | Drafts that the SoT superseded (SoT Appendix D). |
| [`migration-2026-10.md`](migration-2026-10.md) | The report of the October 2026 documentation migration | A historical record of what moved, why, and what is still open. |

Git history is preserved: everything was moved with `git mv`. Use `git log --follow <path>` to see each file's earlier history.

## How the legacy model differs from the SoT

The table below is a summary. The full contradiction report is in [`migration-2026-10.md`](migration-2026-10.md) §E.

| Legacy concept (archive) | Current canonical position (SoT) |
|---|---|
| Noema as an "intent infrastructure layer", "deterministic intent-to-action boundary", "Intent Operating System" or "intent-centric control architecture" | Trusted execution infrastructure for consequential action (§1, §12, §57). Intent Computing is the paradigm, not the product (§3.1). |
| Lifecycle Intent → Resolution → Validation → Trust → Contract → Execution → Outcome, with Intent, Context and Outcome *Engines* | Four separate powers, Understanding → Trust → Execution → Outcome, plus an independent Record (§13, §14) |
| Trust State Machine: UNRESOLVED / EVALUATING / WAITING / BLOCKED / READY / EXECUTING / COMPLETED / FAILED | Decision Maker returns one of `ALLOW`, `CLARIFY`, `CONFIRM`, `WAIT`, `ESCALATE`, `REJECT`, `UNKNOWN`. Grants only on `ALLOW`. Trust never executes (§13.1, §14). |
| A separate deterministic Validation layer (VALID / INVALID / INCOMPLETE / UNKNOWN) | A schema gate at the Understanding boundary. Trust checks the schema and signature of the Intent Object (§13.1, INV-02). |
| Action Contracts and Execution Contracts | Capability Descriptor (§43.8), Decision Grant (§43.2) and Execution Receipt (§43.3) |
| Outcome states PENDING / COMPLETED / FAILED / PARTIALLY_COMPLETED / UNKNOWN / CANCELLED | Outcome Verdict `ACHIEVED` / `NOT_ACHIEVED` / `PARTIALLY_ACHIEVED` / `PENDING_EXTERNAL` / `UNKNOWN` / `COMPENSATED` (§43.4) |
| Temporal adopted as the durable-execution substrate | Postgres-backed durable state in the POC; Temporal evaluated for Phase 3 (§34.5, §35.3, OD-07) |
| Card replacement, or customer account inquiry, as the first wedge | Voice-fronted transaction-exception resolution in Nigerian fintech, "Where is my money?" (BD-03, §31) |
| Taxonomies as classification essays; a fintech taxonomy covering transfers, refunds and cards | Three abstract schemas loaded as data, plus conformance packs. The fintech pack holds only POC nodes. No money movement in the POC (§15, BD-06, BD-08). |
| Five public APIs (Intent, Action, Context, Trust, Execution) | Not specified by the SoT; see [`../engineering/boundary-map.md`](../engineering/boundary-map.md#scope-reminders) |
| Internal employee and HR examples | Embedded in enterprises' customer-facing products (BD-02, §11) |
| Authority hierarchy Canon > Specification > Architecture > ADR > … (ADR-018) | Order of authority in SoT §0.4; status tags in §0.2 |
| Roadmap phases "Semantic coverage → … → Operational optimisation" ending in an "Intent OS" | Phases 0–6 with evidence-based exit gates (§41) |

Ideas the archive holds that the SoT neither adopts nor rejects are listed as unowned items in [OD-P-12](../open-decisions.md#od-p-12). They are not requirements.

## Legacy ADR supersession map

| Legacy ADR | Disposition | Where the surviving idea lives in the SoT |
|---|---|---|
| ADR-001 Intent as a first-class object | Superseded | §3.1, §13.2, §43.1 (Intent Object as a signed proposal) |
| ADR-002 Noema owns intent state, not business state | Superseded (reframed) | §12: Noema is the system of record for the *execution journey*. PLAT-NFR-06. |
| ADR-003 Probabilistic/deterministic boundary | Superseded | §3, §13, INV-01, INV-02 |
| ADR-004 Deterministic trust evaluation | Contradicted in part | Determinism survives (PLAT-NFR-01, INV-21). The READY/WAITING/BLOCKED states do not. |
| ADR-005 Explicit execution contracts | Contradicted | §13.2, §43.2, §43.8 |
| ADR-006 Capability/permission separation | Superseded | §55 principle 9; the three authorisation layers (§14) |
| ADR-007 Enterprise systems remain authoritative | Superseded | §12, §13.3, PLAT-NFR-06 |
| ADR-008 Clarification over guessing | Superseded | §13.3, INV-06, POC-FR-04, OD-03 |
| ADR-009 Separate Validation from Trust | Contradicted | No Validation layer; a schema gate instead (§13.1, §43.1) |
| ADR-010 Trust state machine | Contradicted | Seven-outcome Decision Maker plus Decision Grant (§13.1, §14, PLAT-FR-05) |
| ADR-011 Intent state separate from execution state | Superseded (strengthened) | Four powers with separate signed objects (§13, §43) |
| ADR-012 Provenance and auditability | Superseded | Hash-chained causal Record (§13, §43.6, INV-10, INV-11) |
| ADR-013 Bounded autonomy | Superseded | Earning consequence (§41.1), Delegation Curve (§18.5), safety–autonomy curve (§38.4) |
| ADR-014 Human intervention as explicit state | Superseded | `CLARIFY` / `CONFIRM` / `ESCALATE` Trust outcomes; maker-checker (PLAT-FR-15) |
| ADR-015 Fail closed on unknown | Superseded | BD-10, INV-07, INV-16, INV-19, PLAT-NFR-03 |
| ADR-016 Consumer-side authoritative validation | Superseded | `REJECTED_BY_TARGET` (§43.3); revalidation before every write (INV-17) |
| ADR-017 Outcome separate from trust | Superseded | The Outcome power (§13), INV-04, INV-15 |
| ADR-018 Canonical repository authority | Contradicted | §0.4 order of authority; §0.2 status tags; [`../README.md`](../README.md) |
| ADR-019 Durable execution and workflow orchestration (status was *Proposed*) | Contradicted | §34.5, §35.1, §35.3, OD-07 |
| `decisions/ADR-001-example.md` (template) | Redundant | The record format is now in [`../decisions/README.md`](../decisions/README.md) |

## Removed, not archived

Twenty-one zero-byte placeholder files were removed rather than archived, because they held no content. All of them remain in Git history.

- **12 card-renewal reference-workflow stubs:** `reference-workflows/card-renewal/*`.
- **5 product stubs:** `product/card-renewal.md`, `enterprise-studio.md`, `first-wedge.md`, `product-thesis.md`, `support-usecases.md`.
- **1 research stub:** `research/README.md`.
- **3 RFC stubs:** `rfcs/RFC-001..003`.

They are not recreated, because the SoT requires none of them. The tracked `.DS_Store` file was also removed.
