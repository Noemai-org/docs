# Open decisions

This is the register that SoT AGENT-02 points to (`/docs/open-decisions.md`). It tracks the **status** of open decisions. It does not define them.

- **Canonical open decisions (OD-01 to OD-16)** are defined in [`NOEMA_SOURCE_OF_TRUTH.md`](NOEMA_SOURCE_OF_TRUTH.md) §46. Their table below is generated from §46 by `python3 tools/check_docs_consistency.py --write` and must not be edited by hand. If the two differ, §46 wins.
- **Provisional migration items (OD-P-01 onwards)** were raised by the October 2026 documentation migration. They are **NON-CANONICAL**. They are not requirements and they do not authorise any work. Each one stays provisional until a founder decision adopts it into a future SoT revision (where it would get a canonical OD number) or closes it.

## How the process works

These rules come from SoT §0.4, §44 (AGENT-02) and §46.

1. If a task needs something the SoT does not specify, do not invent it. Follow AGENT-02:
   1. identify the missing decision;
   2. explain why it matters;
   3. propose the smallest safe default;
   4. state what evidence would invalidate that default;
   5. add an entry here marked [OPEN];
   6. do not expand scope until it is decided.
2. Each canonical open decision has a recommended default, and that default applies until the decision is made (§46).
3. Changing a [DECISION] or [CONVICTION] item needs a new version of the SoT (§46). Binding decisions BD-01 to BD-16 (§0.5) change only that way.
4. Every decision is recorded with its date, owner, rationale and evidence. A decision that is not written down does not exist (§0.4). Decision records go in [`decisions/`](decisions/README.md).
5. When an entry is decided, update its **Status** and **Record** columns and link the decision record. Do not delete the row.

Some questions must be answered with evidence and are **never silently resolved** (§46, last paragraph):
- the actual baseline case volume, cost, repeat contacts and resolution time at the first partner;
- whether the chosen speech providers meet latency and language-quality targets in real conditions;
- the commercial unit that best matches value (OD-01).

## Canonical open decisions (SoT §46)

<!-- BEGIN GENERATED: canonical-open-decisions (source: docs/NOEMA_SOURCE_OF_TRUTH.md §46). Do not edit by hand. Run: python3 tools/check_docs_consistency.py --write -->
| ID | Decision | Default or decision (SoT §46) | Decide by | Status | Record |
|---|---|---|---|---|---|
| OD-01 | Pricing model | First pilot: fixed fee with auditable success criteria agreed in writing in advance; verified outcomes counted internally from day one (verified success, verified safe refusal, verified escalation, unresolved or unknown); outcome-based pricing tested only once both sides can agree on what counted; never per seat | Before the first paid pilot | OPEN | — |
| OD-02 | Policy evaluation | Deterministic, versioned rules evaluated in our code; import/export for Cedar and OPA later | Phase B | OPEN | — |
| OD-03 | Ambiguity thresholds | 0.35 auto-resolve margin; escalate above 4 candidates; tune only with full benchmark runs | Phase C | OPEN | — |
| OD-04 | Speech providers | **DECIDED 9 Oct 2026 (DEC-2026-10-09; BD-16).** Aethex AI, Indigenius and N-ATLAS, all integrated behind the provider-neutral speech interface. Default per locale chosen by benchmark (key-slot accuracy, then latency, then cost); switchable by configuration. Each must pass the voice subset and the real-conditions gate (§37.5) before it serves a demo or pilot, and must clear vendor due diligence (data terms, continuity) before handling partner data. | Closed | Closed | [DEC-2026-10-06-vendor-benchmarks](decisions/DEC-2026-10-06-vendor-benchmarks.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-05 | Model providers for Understanding | **DECIDED 9 Oct 2026 (DEC-2026-10-09; BD-16).** GPT, Gemini and Claude, all integrated behind the provider-neutral interface. Default per task chosen by intent accuracy on the code-switched suite; switchable by configuration; automatic failover to another integrated provider. Each provider's enterprise data-retention terms are confirmed, and account data is masked before it is sent, before any partner data flows. | Closed | Closed | [DEC-2026-10-06-vendor-benchmarks](decisions/DEC-2026-10-06-vendor-benchmarks.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-06 | Record integrity | POC: hash chain only, no anchoring. Before Phase 2 production: periodic anchoring of chain heads. External notarisation deferred. | Before Phase 2 | OPEN | — |
| OD-07 | Durable execution engine | **DECIDED 9 Oct 2026 (DEC-2026-10-06-architecture-and-contracts, confirmed by DEC-2026-10-09).** Temporal from the POC onward, under the rules in §35.6 and INV-30. Postgres remains the only authoritative store. | Closed | Closed | [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-08 | Data retention | Minimal by default; raw audio discarded after transcription unless a dispute needs it and consent is recorded; retention per pack and region | Before the first design-partner data conversation | OPEN | — |
| OD-09 | Policy precedence when policy changes mid-case | **DECIDED in v1.2 (see INV-09, INV-26).** Any policy change voids outstanding grants and Trust re-evaluates under the version in force; a rule marked AT_ADMISSION in policy data keeps the version in force when the intent was admitted. Trust never infers "stricter". | Closed | Closed | [DEC-2026-10-02-sot-v1.2](decisions/DEC-2026-10-02-sot-v1.2.md) |
| OD-10 | Public benchmark scope | Publish taxonomy, schemas, fault model and scoring; keep partner data private | End of Phase 1 | OPEN | — |
| OD-11 | Implementation language and deployment shape | **DECIDED 9 Oct 2026 (DEC-2026-10-09).** Two deployables split at the model boundary: Python model service; Go core service (§35.6). | Closed | Closed | [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-12 | First design partner and customer channel | A Nigerian bank or large fintech with high "where is my money" volume and an executive owner of the KPI; channel through its own app overlay. Pick one exception subtype during discovery (§38.6). | Before the end of Phase 1 | OPEN | — |
| OD-13 | First production deployment model | Single-tenant SaaS in-region for the first partner; multi-tenant with strong isolation once tenant-isolation tests pass; customer VPC only where a buyer requires it | Before shadow mode | OPEN | — |
| OD-14 | Certifications the first buyers require, and when | SOC 2 Type I in Phase 2, Type II in Phase 3; confirm with the first US/EU prospects before committing spend | Before Phase 3 planning | OPEN | — |
| OD-15 | The exact Mode 2 contract | Request → decision → (grant) → execution → verdict, versioned, with delegation chain; defined only after Mode 1 has run in production | Phase 4 planning | OPEN | — |
| OD-16 | Custody of the held-out benchmark set | Held by the benchmark owner in a separate private repository with access restricted from the build team and its coding agents; release runs executed by the benchmark owner | Before Phase C | OPEN | — |
<!-- END GENERATED: canonical-open-decisions -->

## Provisional migration items (NON-CANONICAL)

Each entry follows the AGENT-02 structure. "Proposed default" is the smallest safe reading. It is a proposal, not a decision.

<a id="od-p-01"></a>
### OD-P-01: Repository layout (documentation-first vs. monorepo)

- **Status:** [CLOSED] · Multi-repo layout confirmed by [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md) (PR #4). The mapping of repositories to deployables is tracked in [OD-P-13](#od-p-13).
- **Missing decision:** SoT §51 describes a `/noema` monorepo with `/contracts`, `/core`, `/packs`, `/adapters`, `/providers`, `/voice`, `/ui`, `/benchmark`, `/tools/lint` and `/docs`. The SoT does not say whether *this* repository (`Noemai-org/docs`) is that monorepo or a separate documentation repository.
- **Why it matters:**
  - SoT §43 places the JSON Schemas in `/contracts`.
  - The core lint (§15.4) and the import linter (§51) operate on `/core`.
  - AGENT-02 names the path `/docs/open-decisions.md`.
- **Proposed default:** treat this repository as documentation-first.
  - Documentation lives under `docs/`, which satisfies the AGENT-02 path whichever topology is chosen.
  - Do not create `/contracts`, `/core` or any other implementation directory merely because §51 describes it. Each one is created only when a POC requirement needs it.
- **What would invalidate it:** a founder decision that this repository hosts the POC code, or the creation of a separate code repository.

<a id="od-p-02"></a>
### OD-P-02: Where the engineering decision log lives

- **Status:** [OPEN] · NON-CANONICAL · partly addressed by SoT v1.2 §0.4 (founder decisions are committed to the SoT or `docs/decisions/`)
- **Missing decision:** SoT §0.4 ranks "the engineering decision log" sixth (item 6) but does not say where it lives. Since SoT v1.2, §0.4 item 1 says a founder decision counts only once it is committed to the SoT or to `docs/decisions/`, so the founder decision log now has a defined home. The engineering decision log's location is still unstated.
- **Why it matters:** without a defined location, an engineer or agent cannot apply the full order of authority.
- **Proposed default:**
  - Use [`decisions/`](decisions/README.md) for the engineering decision log as well.
  - Until a committed founder decision is added there, the SoT is the highest authority available in this repository. The first record is [DEC-2026-10-02-sot-v1.2](decisions/DEC-2026-10-02-sot-v1.2.md).
  - Do not invent historical decisions.
- **What would invalidate it:** the founders keep the log elsewhere. In that case, link it from `decisions/README.md`.
- **Note (v1.3):** founder decisions now live in [`decisions/`](decisions/README.md), and AGENT-29 requires each decision record to land in the same pull request as the matching SoT edit and the regenerated register. Where the engineering decision log lives is still open.

<a id="od-p-03"></a>
### OD-P-03: The Tushe specification was referenced but absent

- **Status:** [CLOSED] by [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md) (PR #4); the specification was added in PR #3.
- **Update:** the issued v1.0 specification is now in the repository as a frozen record: [`poc/tushe/`](poc/tushe/README.md).
- **Missing decision:** SoT §36 and §0.4 (item 4) rely on *Noema × Tushe Synthetic Enterprise Environment: Technical Requirements & Acceptance Specification v1.0*, which is not in this repository. That document defines:
  - acceptance tests AT-01 to AT-20;
  - the twenty-scenario pack;
  - the documented transitions and invariants of the domain lifecycles.
- **Why it matters:**
  - Phase A cannot exit without AT-01 to AT-20 passing (§36, §40.1).
  - The SoT ranks the Tushe specification fourth in its order of authority.
- **Proposed default:**
  - Rely only on the summary in SoT §36 and the lifecycle lists in §35.5.
  - Do not write AT-xx definitions or scenario content from memory or inference.
  - Add the specification to the repository (for example under `docs/poc/`) once it is available.
- **What would invalidate it:** the specification is added, or the founders decide to keep it outside the repository and link to it.
- **Note:** requested changes to the specification (v1.0 → v1.1) are listed in [`poc/tushe/tushe-spec-delta-v1.1.md`](poc/tushe/tushe-spec-delta-v1.1.md).

<a id="od-p-04"></a>
### OD-P-04: Runbooks named by the SoT do not exist

- **Status:** [OPEN] · NON-CANONICAL · not needed until Phase 2
- **Missing decision:** SoT §51 says `/docs` holds runbooks. SoT §39 requires a tested kill switch, a rollback and disable path, and an incident playbook with a named owner before any customer-facing action. None of these documents exists.
- **Why it matters:** they are a precondition for shadow, assisted and governed production (§39, §40.3 "Added before any production use").
- **Proposed default:** none is written now. They are written and tested before Phase 2 production, with the real system they describe.
- **What would invalidate it:** a design partner requires them earlier.
- **Note:** empty scaffolds (headings and TODOs only, no steps) now exist in [`runbooks/`](runbooks/README.md), proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md). This entry stays [OPEN]: no runbook is written or tested.

<a id="od-p-05"></a>
### OD-P-05: Superseded source drafts are only partly present

- **Status:** [OPEN] · NON-CANONICAL · low priority
- **Missing decision:** SoT Appendix D says v1.0 superseded the following, and that v1.1 merged a review of three peer drafts:
  - "Founding Canon v4.0";
  - the "Master Company Document (Final)";
  - the "POC Specification v2.0".

  The repository holds four pre-SoT PDFs (now in [`archive/source-drafts-2026-09/`](archive/source-drafts-2026-09/)). It does not hold Founding Canon v4.0, a document labelled POC Specification v2.0, or clearly identified peer drafts.
- **Why it matters:** this is historical completeness only. The SoT already records every correction it made.
- **Proposed default:** no action. Add the missing drafts to the archive if the founders want a complete paper trail.
- **What would invalidate it:** nothing operational depends on this.

<a id="od-p-06"></a>
### OD-P-06: The Intent Object `status` values are not enumerated

- **Status:** [CLOSED] · Enums decided in [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md) (PR #4). The value list is normative; see [`engineering/state-registry.md`](engineering/state-registry.md) §6.
- **Missing decision:** the Intent Object example (§43.1) has `"status": "VALIDATED"`, but the SoT lists no other value and no lifecycle for this field. The SoT does define:
  - the versioning rules (`version`, `supersedes`, immutable once admitted to Trust);
  - clarification binding (POC-FR-13).
- **Why it matters:** a schema cannot be frozen with an open enum, and the contract freeze is a Phase A exit condition.
- **Proposed default:** do not define the enum in documentation. Settle it with the contract freeze and record it as a decision.
- **What would invalidate it:** a SoT revision that enumerates it.

<a id="od-p-07"></a>
### OD-P-07: `SEC-` and `PERF-` ID prefixes are named but undefined

- **Status:** [OPEN] · NON-CANONICAL
- **Missing decision:** SoT §0.3 lists `SEC-` and `PERF-` among the stable requirement ID prefixes. No ID with either prefix appears anywhere in the SoT, and Appendix B does not list them.
- **Why it matters:**
  - AGENT-01 requires every change to cite an ID.
  - Security work (§47) and performance work (§48) can currently be traced only to PLAT-NFR, POC-NFR, INV or AGENT IDs, or to section numbers.
- **Proposed default:**
  - Do not mint `SEC-` or `PERF-` IDs.
  - Trace security work to PLAT-NFR-14, PLAT-NFR-20, BD-11, INV-01 to INV-30 and AGENT-09/10/13, plus a §47 reference.
  - Trace performance work to PLAT-NFR-13, POC-NFR-09 and a §48 reference.
- **What would invalidate it:** a SoT revision that defines these ID families.

<a id="od-p-08"></a>
### OD-P-08: Value sets for authority-layer results and reason codes are not enumerated

- **Status:** [CLOSED] · Enums decided in [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md) (PR #4). The value lists are normative; see [`engineering/state-registry.md`](engineering/state-registry.md) §2.
- **Missing decision:** the SoT gives these values only as examples:
  - the Decision Record's `authority` layer results: `PASS`, `NOT_EVALUATED` (§43.2);
  - Trust reason codes: `AMBIGUOUS_COUNTERPARTY` (§43.2), `PROHIBITED_CAPABILITY` (US-10), `DECLINED_BY_APPROVER` (§43.2a, since v1.2).
- **Why it matters:** both are cross-boundary contract fields (PLAT-FR-05, POC-FR-06).
- **Proposed default:** treat these as examples only. Define the value sets with the contract freeze and record the decision.
- **What would invalidate it:** a SoT revision that enumerates them.

<a id="od-p-09"></a>
### OD-P-09: The canonical risk-class set and its ownership

- **Status:** [OPEN] · NON-CANONICAL
- **Missing decision:**
  - The SoT uses `R0` read/internal, `R1` append-only write, `R2` non-monetary write, `R3` regulatory write (since v1.2, for `LOG_COMPLAINT_REFERENCE`) and `PROHIBITED` in the POC registry (§34.3).
  - It also uses `R3` in an [ILLUSTRATIVE] telecom row (§15.4), for a refund capability.
  - Since v1.2, a capability's `risk_class` may never be lower than the risk implied by its consequence profile (§43.8), but the mapping from profile to class is not defined.
  - It says risk classes live in each vertical's Trust Taxonomy (§15.1, §15.5).
  - It requires `PROHIBITED` to be enforced structurally (§34.2, INV-05).

  No complete list of risk classes is defined, and the SoT does not say which classes are core semantics and which are pack data.
- **Why it matters:** INV-14 forbids vertical-specific terms in core. Prohibition must be a core guarantee, while other risk levels vary by domain.
- **Proposed default:** core recognises only the structural `PROHIBITED` semantics. All other risk classes are pack data, used only as written in the SoT for the POC.
- **What would invalidate it:** a SoT revision that defines a core risk ladder.

<a id="od-p-10"></a>
### OD-P-10: Similar names that must not be conflated

- **Status:** [OPEN] · NON-CANONICAL · terminology hygiene, not a contradiction
- **Missing decision:** two pairs of terms look alike but mean different things:
  - `OUTCOME_UNKNOWN` is an Execution Receipt `execution_state` (§43.3) and the classification for a lost case-write response (§35.5). `EXECUTION_OUTCOME_UNKNOWN` is a *transaction* lifecycle state in the synthetic environment and the classification for a ledger debit with a switch timeout (§35.5).
  - Severity classes `S0`–`S3` (§38.3) share a prefix with data-sensitivity labels such as `S3_financial_pii` and "data class S4" (§15.3, §15.4).
- **Why it matters:** an engineer or agent could conflate them.
- **Proposed default:** keep every name exactly as the SoT writes it, and always qualify a value by the object or field it belongs to. [`engineering/state-registry.md`](engineering/state-registry.md) does this.
- **What would invalidate it:** a SoT revision that renames either pair.

<a id="od-p-11"></a>
### OD-P-11: POC-FR-17 maps to no platform requirement

- **Status:** [OPEN] · NON-CANONICAL · low priority
- **Missing decision:** POC-FR-17 (the evidence panel) maps to "Demo evidence" rather than to a PLAT-FR ID (§37.1). It is not stated whether an evidence or reconstruction view is a platform requirement beyond PLAT-FR-12 (reconstruction API) and PLAT-US-05/06.
- **Proposed default:** treat POC-FR-17 as a POC-only requirement. Do not mint a PLAT ID.
- **What would invalidate it:** a SoT revision that adds one.

<a id="od-p-12"></a>
### OD-P-12: Legacy concepts with no owner in the SoT (OPEN / UNOWNED)

- **Status:** [OPEN] · NON-CANONICAL · **not requirements**
- **What these are:** the archived legacy documents describe concepts the SoT neither adopts nor rejects. They are recorded here so the knowledge is not lost. None of them may be implemented on the strength of the archive.

| Concept | Where the legacy reasoning lives (archive) | Nearest SoT anchor |
|---|---|---|
| Several intents in one utterance; composite intents | `archive/legacy-canon-2026-09/intent/intent-composition.md` | §43.1 has one `intent_node` per Intent Object |
| Intent cancellation and expiry | `archive/legacy-canon-2026-09/architecture/intent-engine.md` | `supersedes` (§43.1), abandon-and-resume (POC-FR-13, US-11) |
| A richer time model (event, observation, receipt, processing, decision, execution and outcome time) | `archive/legacy-canon-2026-09/data/temporal-state.md` | `read_at` and `effective_at` (§43.5); event and ingestion time (§35.5) |
| A lifecycle for contract versions (draft → retired) and compatibility classes | `archive/legacy-canon-2026-09/contracts/versioning.md` | PLAT-NFR-17, AGENT-15 |
| Event delivery, ordering and duplication semantics | `archive/legacy-canon-2026-09/contracts/event-contract.md` | outbox/inbox (§35.3), `EVENT_ORDER_UNCERTAIN` (§35.5) |
| Organisational and tenant hierarchy detail | `archive/legacy-canon-2026-09/enterprise/organizational-boundaries.md` | PLAT-FR-16 |

- **Proposed default:** do not build any of these. If a POC case needs one, raise a specific entry under AGENT-02.

<a id="od-p-13"></a>
### OD-P-13: Which repository hosts each deployable and `/contracts`

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-13-code-monorepo](decisions/DEC-2026-10-13-code-monorepo.md) R1 and R2 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-13 R1, R2):** All POC code lives in one repository, `noema`. The model service is `services/model/` and the core service is `services/core/`, two separate deployables with separate manifests, build contexts, images, credentials and networks. `/contracts` lives at `contracts/` in `noema`; generated Go and Python types are committed inside each service and checked by CI. `backend` and `intent-engine` are archived. SoT v1.5 §51 no longer carries the [OPEN] mapping note.
- **Missing decision:** DEC-2026-10-06-architecture-and-contracts names four repositories (`docs`, `brain`, `backend`, `intent-engine`), and DEC-2026-10-09 defines two deployables (the Python model service and the Go core service). No record says which repository hosts which deployable, which one hosts `/contracts`, or what `brain` contains. SoT v1.3 §51 marks this [OPEN].
- **Why it matters:** `/contracts` must live in exactly one repository, with the others consuming generated packages pinned by version (§51). The CI boundary checks in §51 run per repository.
- **Proposed default (inference, not a decision):** `intent-engine` hosts the model service; `backend` hosts the core service and `/contracts`. The role of `brain` is unknown.
- **What would invalidate it:** a decision record that maps the repositories differently.

**OD-P-14 to OD-P-41** mirror the open questions of [POC PERD v1.1](poc/perd/README.md) (current: see README) (§67.2, tagged [OQ]) and its [REC] defaults awaiting adoption (§67.3), proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md). Field text is quoted from the PERD; in quoted text, a bare "§" points to the PERD and "SoT §" to the SoT (PERD P.2). Like every OD-P entry, they authorise no work on their own.

<a id="od-p-14"></a>
### OD-P-14: Who is the benchmark owner? (OQ-01)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: Before P3
- **Question:** Who is the benchmark owner?
- **Why it matters:** OD-16; release runs; held-out set
- **Minimum safe default (meanwhile):** Founder-appointed person outside the build team
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Founders
- **Deadline:** Before P3
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-01. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-15"></a>
### OD-P-15: Who reviews arm competence? (OQ-02)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: Before P13
- **Question:** Who reviews arm competence?
- **Why it matters:** Fair comparison
- **Minimum safe default (meanwhile):** An external engineer under NDA
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Founders
- **Deadline:** Before P13
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-02. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-16"></a>
### OD-P-16: Does the Tushe case API support idempotency keys, query-by-key and version tokens? (OQ-03)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-12-tushe-environment-scope](decisions/DEC-2026-10-12-tushe-environment-scope.md) §8 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-12 §8):** Yes, because the case API is now ours (D1). The case capabilities keep the PERD §25.1 retry-safety class QUERYABLE_BY_KEY and concurrency CONDITIONAL_WRITE.
- **Question:** Does the Tushe case API support idempotency keys, query-by-key and version tokens?
- **Why it matters:** Retry safety; conditional writes
- **Minimum safe default (meanwhile):** Resolve in Phase A. Until proven, register the case capabilities with retry safety NONE (one dispatch at most, escalate on uncertainty) and concurrency NONE where INV-27 allows
- **What would change it:** Tushe API and the delta
- **Owner:** Integration lead
- **Deadline:** Phase A
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-03. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-17"></a>
### OD-P-17: Repository mapping (SoT §51 [OPEN]) (OQ-04)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-13-code-monorepo](decisions/DEC-2026-10-13-code-monorepo.md) R1 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-13 R1 to R8):** One code repository, `noema`, with the layout of DEC R1 and PERD §64.2. `docs` keeps governance; `benchmark-heldout` (private) holds the held-out set; `brain` keeps its non-build purpose; `backend` and `intent-engine` are archived after inspection.
- **Question:** Repository mapping (SoT §51 [OPEN])
- **Why it matters:** Phase B cannot start cleanly
- **Minimum safe default (meanwhile):** §64.1 recommendation
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Founders
- **Deadline:** Before Phase B
- **Note:** the same decision was tracked as [OD-P-13](#od-p-13); this entry only mirrors the PERD question and its §64.1 recommendation. Both are closed together.
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-04. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-18"></a>
### OD-P-18: Purpose of the `brain` repository (OQ-05)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-13-code-monorepo](decisions/DEC-2026-10-13-code-monorepo.md) R7 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-13 R7, confirmed by [DEC-2026-10-16](decisions/DEC-2026-10-16-execution-reset.md) E8):** `brain` holds founder documentation outside the build. It is not part of the build's chain of authority: nothing in it is a specification, a requirement or a decision for the POC unless first moved into `docs` through a decision record. Coding agents do not read or cite it for build work. Nothing about it is archived or changed. DEC-2026-10-16 E8 adds where build records live (gates, daily notes and sessions in `docs/poc/execution/`; Tushe observations and correspondence in `docs/poc/tushe/`; incidents and as-built notes in `noema/docs/`) and what `brain` never holds (specifications, build records, technology decisions).
- **Question:** Purpose of the `brain` repository
- **Why it matters:** Avoid misplaced code
- **Minimum safe default (meanwhile):** No POC code there
- **What would change it:** Founder intent
- **Owner:** Founders
- **Deadline:** Before Phase B
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-05. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-19"></a>
### OD-P-19: Quantity units in the Intent Object (major vs minor) (OQ-06)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: P1
- **Question:** Quantity units in the Intent Object (major vs minor)
- **Why it matters:** Money correctness
- **Minimum safe default (meanwhile):** Minor units plus a marker (contract minor version)
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Tech lead
- **Deadline:** P1
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-06. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-20"></a>
### OD-P-20: Which speech providers offer streaming TTS for all five locales? (OQ-07)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: Week 1
- **Question:** Which speech providers offer streaming TTS for all five locales?
- **Why it matters:** Voice answer path
- **Minimum safe default (meanwhile):** Text on screen where TTS is missing
- **What would change it:** Vendor documentation and tests
- **Owner:** Voice lead
- **Deadline:** Week 1
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-07. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-21"></a>
### OD-P-21: Field protocol owner, devices and SIMs (OQ-08)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: Week 3
- **Question:** Field protocol owner, devices and SIMs
- **Why it matters:** Voice gate
- **Minimum safe default (meanwhile):** §45.4 protocol
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Voice lead
- **Deadline:** Week 3
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-08. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-22"></a>
### OD-P-22: Secrets manager for shared environments (OQ-09)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: P0
- **Question:** Secrets manager for shared environments
- **Why it matters:** Key management
- **Minimum safe default (meanwhile):** File-mounted secrets locally only
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Tech lead
- **Deadline:** P0
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-09. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-23"></a>
### OD-P-23: CI access to Tushe (live or recorded) (OQ-10)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-12-tushe-environment-scope](decisions/DEC-2026-10-12-tushe-environment-scope.md) §8 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-12 §8):** Pull requests use recorded Tushe responses replayed through the proxy; the nightly and release runs use live Tushe in test mode.
- **Question:** CI access to Tushe (live or recorded)
- **Why it matters:** Merge gates
- **Minimum safe default (meanwhile):** Recorded Tushe responses for merges; live for nightly runs
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Integration lead
- **Deadline:** P2
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-10. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-24"></a>
### OD-P-24: How is an ESCALATE handoff without a case delivered to the partner? (The SoT listener has no handoff event) (OQ-11)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: Before the first partner demo
- **Question:** How is an ESCALATE handoff without a case delivered to the partner? (The SoT listener has no handoff event)
- **Why it matters:** Unresolved-target escalations
- **Minimum safe default (meanwhile):** Customer instruction plus the ops inspector only. Propose an `escalation.handoff` event as a contract addition after partner discovery
- **What would change it:** Partner requirements
- **Owner:** Product
- **Deadline:** Before the first partner demo
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-11. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-25"></a>
### OD-P-25: Tenant time zone and lexicon reviewers (native speakers for yo, ha, ig, pcm) (OQ-12)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: P5
- **Question:** Tenant time zone and lexicon reviewers (native speakers for yo, ha, ig, pcm)
- **Why it matters:** Time windows; numerals
- **Minimum safe default (meanwhile):** Africa/Lagos; reviewers to be contracted
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Founders
- **Deadline:** P5
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-12. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-26"></a>
### OD-P-26: Do the value lists in DEC-2026-10-06-architecture-and-contracts differ from this PERD's lists? (OQ-13)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: P1
- **Question:** Do the value lists in DEC-2026-10-06-architecture-and-contracts differ from this PERD's lists?
- **Why it matters:** Contract drift
- **Minimum safe default (meanwhile):** The DEC record governs. Agents must diff before P1
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Tech lead
- **Deadline:** P1
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-13. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-27"></a>
### OD-P-27: Legal validation of synthetic clocks before any external claim (OQ-14)

- **Status:** [OQ] [OPEN] · NON-CANONICAL · decide by: Before any external demo
- **Question:** Legal validation of synthetic clocks before any external claim
- **Why it matters:** Regulatory accuracy
- **Minimum safe default (meanwhile):** All clocks labelled SYNTHETIC
- **What would change it:** Counsel review
- **Owner:** Founders
- **Deadline:** Before any external demo
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-14. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-28"></a>
### OD-P-28: PERD [REC] defaults: Trust semantics

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for trust semantics. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** WAIT and UNKNOWN definitions (§23.1); disposition and action decision linkage plus a `disposition_decision_id` field; R0 reads without grants
- **Where they are specified:** [PERD](poc/perd/README.md) §23.1 (the seven outcomes; disposition and action decisions, REQ-TRU-010); §25.1 (R0 reads and grants). Conflicts SOT-C-03, SOT-C-04, SOT-C-05.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-29"></a>
### OD-P-29: PERD [REC] defaults: Investigation state

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for investigation state. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** The investigation state machine (§28.2)
- **Where they are specified:** [PERD](poc/perd/README.md) §28.2 (investigation state machine); §28.3 (REQ-STM-001, REQ-STM-002).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-30"></a>
### OD-P-30: PERD [REC] defaults: Resolution

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for resolution. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Ranking weights; 0.70 floor; 0.85 key-slot threshold; clarification 10 min; 2 rounds; dormancy 30 min; resume 72 h
- **Where they are specified:** [PERD](poc/perd/README.md) §22.1 (ambiguity lifecycle: REQ-AMB-003 ranking and floor, REQ-AMB-004 to REQ-AMB-006 clarification, rounds, dormancy and resume, REQ-AMB-007 key-slot threshold). Touches SoT OD-03.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-31"></a>
### OD-P-31: PERD [REC] defaults: Grants and confirmations

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for grants and confirmations. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Grant TTL 10 min; confirmation TTL 10 min
- **Where they are specified:** [PERD](poc/perd/README.md) §23.6 (REQ-TRU-008 Decision Grant issuance; REQ-TRU-009 confirmation contract).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-32"></a>
### OD-P-32: PERD [REC] defaults: Recovery

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for recovery. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Recovery budget of 2 dispatches; verification read schedule
- **Where they are specified:** [PERD](poc/perd/README.md) §30.2 (recovery decision table); §30.3 (REQ-RCV-003 recovery budget); §29.2 (REQ-VER-001 verification read retries).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-33"></a>
### OD-P-33: PERD [REC] defaults: Watches and callbacks

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for watches and callbacks. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Watch schedule; callback retry schedule
- **Where they are specified:** [PERD](poc/perd/README.md) §29.2 (REQ-VER-004 durable outcome watch; REQ-VER-005 `outcome.updated` callback).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-34"></a>
### OD-P-34: PERD [REC] defaults: Contracts and identifiers

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for contracts and identifiers. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** JCS canonicalisation; length-prefixed key encoding; `policy_scope` = `policy_id`; ID scheme; Record event additions
- **Where they are specified:** [PERD](poc/perd/README.md) §27.2 (idempotency key and `policy_scope`, SOT-C-13); §32.1 to §32.3 (Record event, event types, ID scheme).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-35"></a>
### OD-P-35: PERD [REC] defaults: Policy

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for policy. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Policy schema and precedence ladder
- **Where they are specified:** [PERD](poc/perd/README.md) §23.4 (policy as data, precedence).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-36"></a>
### OD-P-36: PERD [REC] defaults: Freeze

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for freeze. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Freeze allow-list
- **Where they are specified:** [PERD](poc/perd/README.md) §22.3 (REQ-RES-002 contradiction freeze). Conflict SOT-C-12.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-37"></a>
### OD-P-37: PERD [REC] defaults: Explanation

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for explanation. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Facts contract and claim validator
- **Where they are specified:** [PERD](poc/perd/README.md) §31.2 (facts contract); §31.3 (REQ-EXP-002 claim validator).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-38"></a>
### OD-P-38: PERD [REC] defaults: Fault injection

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for fault injection. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** FaultPlan contract
- **Where they are specified:** [PERD](poc/perd/README.md) §37.1 (FaultPlan contract and effect enum).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-39"></a>
### OD-P-39: PERD [REC] defaults: Benchmark

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for benchmark. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Case schema; evil provider; A0 diagnostic arm
- **Where they are specified:** [PERD](poc/perd/README.md) §48.2 (case contract); §49 (the evil provider); §50.1 (A0 diagnostic, SOT-C-18).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-40"></a>
### OD-P-40: PERD [REC] defaults: Infrastructure

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for infrastructure. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Temporal persistence database; per-power DB roles; network topology
- **Where they are specified:** [PERD](poc/perd/README.md) §36.1 (Temporal persistence, SOT-C-14); §41.1 (per-power DB roles, SOT-C-16); §65.1 (POC network topology).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-41"></a>
### OD-P-41: PERD [REC] defaults: Retention

- **Status:** [REC] [OPEN] · NON-CANONICAL · provisional default until accepted or replaced by a decision record
- **Missing decision:** whether to adopt the PERD [REC] defaults for retention. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Retention defaults
- **Where they are specified:** [PERD](poc/perd/README.md) §38.2 (retention column); §38.3 (retention and data-handling defaults). Real-data retention stays SoT OD-08.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-42"></a>
### OD-P-42: Schedule compression: Phase A in parallel with build week 1

- **Status:** [OPEN] · NON-CANONICAL · decide by: Mon 12 Oct 2026
- **Missing decision:** SoT §40.2 [TARGET] plans four weeks of build *after* Phase A exits. The [four-week plan](poc/execution/README.md) §3 runs Phase A in parallel with build week 1, with G0 due Thu 15 Oct (task GOV-04).
- **Why it matters:** Phase B results produced before G0 would rest on unproven Tushe semantics.
- **Minimum safe default:** gates outrank dates; no Phase B result counts before G0.
- **What would invalidate it:** a founder decision to keep Phase A before the four-week clock, or G0 failing so that week-1 results are unusable.
- **Owner:** Founders
- **Deadline:** Mon 12 Oct 2026
- **Source:** plan §3; proposed in [DEC-2026-10-11-poc-4week-plan](decisions/DEC-2026-10-11-poc-4week-plan.md).

<a id="od-p-43"></a>
### OD-P-43: Public webhook receiver hosting and security (OQ-15)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-execution-reset](decisions/DEC-2026-10-16-execution-reset.md) E6 (takes effect when that record is approved and merged). Closes plan task GOV-20
- **Answer (DEC-2026-10-16 E6):** The webhook relay (`synthetic/webhook_relay/` in `noema`, a test-environment component, E5) runs on one small public HTTPS host that runs nothing else. The Engineering lead picks the provider at setup and records it in the `local-setup` runbook. The relay verifies the Standard Webhooks signature and the five-minute tolerance, rejects and counts anything unverified, and stores each verified delivery unchanged, keyed by delivery ID. It holds only the webhook signing secret: no database, Tushe, grant or provider credential. The core pulls verified deliveries over an authenticated outbound connection to an allowlisted host, into its inbox, which deduplicates by delivery ID (REQ-API-008). Nothing on the internet can reach the core. In the benchmark profile the core's pull runs through the hostility proxy; the proxy never runs on the public host.
- **Question:** Where does the public webhook receiver run, and how is it secured?
- **Why it matters:** Tushe delivers webhooks only to public HTTPS endpoints; AT-06 needs it on Fri 16 Oct.
- **Minimum safe default (meanwhile):** One small public HTTPS host that runs only the receiver; no other Noema component is exposed. (The earlier wording, "and the proxy in front of it", is replaced by the E6 design above.)
- **What would change it:** — (none stated)
- **Owner:** Engineering lead
- **Deadline:** Wed 14 Oct 2026 (plan task GOV-20); decided 16 Oct 2026
- **Source:** [PERD v1.3](poc/perd/NOEMA_POC_PERD_v1.3.md) §67.2, OQ-15 (answered in [PERD v1.5](poc/perd/NOEMA_POC_PERD_v1.5.md)); [DEC-2026-10-12-tushe-environment-scope](decisions/DEC-2026-10-12-tushe-environment-scope.md), Amendment 1.

<a id="od-p-44"></a>
### OD-P-44: How `evidence_set_hash` is built

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-contract-and-pack-clarifications](decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) C1 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-16 contract-and-pack-clarifications C1):** Sort the `(evidence_id, payload_hash)` pairs by the UTF-8 bytes of `evidence_id`, join `LP(evidence_id) ‖ LP(payload_hash)` for each pair, and take SHA-256. `LP()` is the 4-byte big-endian length plus UTF-8 bytes of PERD §27.2. The whole input is rejected on an empty or duplicate `evidence_id` or a `payload_hash` that is not `sha256:` plus 64 lowercase hex characters. Trust never issues a grant over an empty evidence set. Four golden vectors and five negative fixtures are in PERD v1.6 §21.3.
- **Missing decision:** the construction of `evidence_set_hash` (PERD v1.5 §21.3 gave only "SHA-256 over the sorted list of `(evidence_id, payload_hash)`"), so that Go and Python implement the committed vectors the same way (task CON-04).
- **Why it matters:** the hash is bound into every grant (SoT §13.2, INV-17). Two implementations that differ by one byte reject each other's grants.
- **Minimum safe default (meanwhile):** the C1 construction, which reproduces both committed vectors.
- **What would change it:** a committed vector that the construction does not reproduce, or an implementation that cannot reproduce all four vectors in CI.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before CON-04 is done; decided 16 Oct 2026
- **Source:** [PERD v1.6](poc/perd/NOEMA_POC_PERD_v1.6.md) §21.3, REQ-CTX-004; [DEC-2026-10-16-contract-and-pack-clarifications](decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) C1.

<a id="od-p-45"></a>
### OD-P-45: Intent model of the fintech pack

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-contract-and-pack-clarifications](decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) C2 (takes effect when that record is approved and merged)
- **Answer (DEC-2026-10-16 contract-and-pack-clarifications C2):** The fintech pack has exactly two intent nodes, `fin.payments.exception.investigate` and `fin.meta.out_of_scope`. Question types and requested remedies are slots, never nodes. The ten upper-case classes of the ported pack are mapped (PERD v1.6 §20.4) and deleted; `SELECT_BENEFICIARY` is counterparty resolution inside the node. The conformance packs follow the same shapes within the SoT §15.4 cap.
- **Missing decision:** which intent model the pack uses: the ported pack's ten classes (two of which, `TRANSFER_FUNDS` as a write intent and `REQUEST_REFUND`, contradict the money boundary) or the two nodes of SoT §15.3 and PERD §20.4 (E12 review item 4).
- **Why it matters:** Trust, the compiler and the benchmark are built against the pack's shapes in week 1.
- **Minimum safe default (meanwhile):** the two-node model; the ported classes are not built against (task PCK-01 is in progress, DEC C3).
- **What would change it:** a change to SoT §15.3.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before PCK-01 and UND-05 start the rewrite; decided 16 Oct 2026
- **Source:** [PERD v1.6](poc/perd/NOEMA_POC_PERD_v1.6.md) §20.4, REQ-INT-005; [DEC-2026-10-16-contract-and-pack-clarifications](decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) C2, C3.
