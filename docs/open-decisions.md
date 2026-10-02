# Open decisions

This is the register that SoT AGENT-02 points to (`/docs/open-decisions.md`). It tracks the **status** of open decisions. It does not define them.

- **Canonical open decisions (OD-01 to OD-15)** are defined in [`NOEMA_SOURCE_OF_TRUTH.md`](NOEMA_SOURCE_OF_TRUTH.md) §46. Their text below is copied from §46 for convenience. If the two differ, §46 wins.
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
3. Changing a [DECISION] or [CONVICTION] item needs a new version of the SoT (§46). Binding decisions BD-01 to BD-15 (§0.5) change only that way.
4. Every decision is recorded with its date, owner, rationale and evidence. A decision that is not written down does not exist (§0.4). Decision records go in [`decisions/`](decisions/README.md).
5. When an entry is decided, update its **Status** and **Record** columns and link the decision record. Do not delete the row.

Some questions must be answered with evidence and are **never silently resolved** (§46, last paragraph):
- the actual baseline case volume, cost, repeat contacts and resolution time at the first partner;
- whether the chosen speech providers meet latency and language-quality targets in real conditions;
- the commercial unit that best matches value (OD-01).

## Canonical open decisions (SoT §46)

| ID | Decision | Recommended default (SoT) | Decide by | Status | Record |
|---|---|---|---|---|---|
| OD-01 | Pricing model | Platform fee + price per verified outcome by risk class; never per seat | Before the first paid pilot | [OPEN]: default applies | — |
| OD-02 | Policy evaluation | Deterministic, versioned rules evaluated in our code; import/export for Cedar and OPA later | Phase B | [OPEN]: default applies | — |
| OD-03 | Ambiguity thresholds | 0.35 auto-resolve margin; escalate above 4 candidates; tune only with full benchmark runs | Phase C | [OPEN]: default applies | — |
| OD-04 | Speech providers | Benchmark at least two (including an Intron- or N-ATLAS-based option) on the voice subset; choose on key-slot accuracy, then latency, then cost | Week 2 of the POC | [OPEN]: default applies | — |
| OD-05 | Model providers for Understanding | At least two benchmarked; choose on intent accuracy on the code-switched suite | Week 2 of the POC | [OPEN]: default applies | — |
| OD-06 | Record integrity | Hash chain with periodic anchoring of chain heads; external notarisation deferred | Before the first external demo | [OPEN]: default applies | — |
| OD-07 | Durable execution engine | Postgres-backed durable state for the POC; evaluate Temporal for Phase 3 | Phase 3 planning | [OPEN]: default applies | — |
| OD-08 | Data retention | Minimal by default; raw audio discarded after transcription unless a dispute needs it and consent is recorded; retention per pack and region | Before the first design-partner data conversation | [OPEN]: default applies | — |
| OD-09 | Policy precedence when policy changes mid-case | Admission-time policy governs, unless the new version is stricter, in which case the stricter applies; both recorded | Phase B | [OPEN]: default applies | — |
| OD-10 | Public benchmark scope | Publish taxonomy, schemas, fault model and scoring; keep partner data private | End of Phase 1 | [OPEN]: default applies | — |
| OD-11 | Implementation language | Python 3.13 + Django (chosen); TypeScript/Node 22 is the alternative two peer drafts recommended. Switch only if the build team is materially faster in it. The rules in §35.3 apply either way | Before Phase B | [OPEN]: default applies | — |
| OD-12 | First design partner and customer channel | A Nigerian bank or large fintech with high "where is my money" volume and an executive owner of the KPI; channel through its own app overlay | Before the end of Phase 1 | [OPEN]: default applies | — |
| OD-13 | First production deployment model | Single-tenant SaaS in-region for the first partner; multi-tenant with strong isolation once tenant-isolation tests pass; customer VPC only where a buyer requires it | Before shadow mode | [OPEN]: default applies | — |
| OD-14 | Certifications the first buyers require, and when | SOC 2 Type I in Phase 2, Type II in Phase 3; confirm with the first US/EU prospects before committing spend | Before Phase 3 planning | [OPEN]: default applies | — |
| OD-15 | The exact Mode 2 contract | Request → decision → (grant) → execution → verdict, versioned, with delegation chain; defined only after Mode 1 has run in production | Phase 4 planning | [OPEN]: default applies | — |

## Provisional migration items (NON-CANONICAL)

Each entry follows the AGENT-02 structure. "Proposed default" is the smallest safe reading. It is a proposal, not a decision.

<a id="od-p-01"></a>
### OD-P-01: Repository layout (documentation-first vs. monorepo)

- **Status:** [OPEN] · NON-CANONICAL · raised 2 Oct 2026
- **Missing decision:** SoT §51 describes a `/noema` monorepo with `/contracts`, `/core`, `/packs`, `/adapters`, `/providers`, `/voice`, `/ui`, `/benchmark`, `/tools/lint` and `/docs`. The SoT does not say whether *this* repository (`noema-org/docs`) is that monorepo or a separate documentation repository.
- **Why it matters:**
  - SoT §43 places the JSON Schemas in `/contracts`.
  - The core lint (§15.4) and the import linter (§51) operate on `/core`.
  - AGENT-02 names the path `/docs/open-decisions.md`.
- **Proposed default:** treat this repository as documentation-first.
  - Documentation lives under `docs/`, which satisfies the AGENT-02 path whichever topology is chosen.
  - Do not create `/contracts`, `/core` or any other implementation directory merely because §51 describes it. Each one is created only when a POC requirement needs it.
- **What would invalidate it:** a founder decision that this repository hosts the POC code, or the creation of a separate code repository.

<a id="od-p-02"></a>
### OD-P-02: Founder decision log and engineering decision log are not in the repository

- **Status:** [OPEN] · NON-CANONICAL
- **Missing decision:** SoT §0.4 ranks "the latest explicit, recorded founder decision" first (item 1) and "the engineering decision log" sixth (item 6). Neither log exists in this repository.
- **Why it matters:** without them, an engineer or agent cannot apply the full order of authority.
- **Proposed default:**
  - Use [`decisions/`](decisions/README.md) for both logs from now on.
  - Until a recorded founder decision is added there, the SoT is the highest authority available in this repository.
  - Do not invent historical decisions.
- **What would invalidate it:** the founders keep the log elsewhere. In that case, link it from `decisions/README.md`.

<a id="od-p-03"></a>
### OD-P-03: The Tushe specification is referenced but absent

- **Status:** [OPEN] · NON-CANONICAL · blocking for Phase A / Phase 0 exit
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

<a id="od-p-04"></a>
### OD-P-04: Runbooks named by the SoT do not exist

- **Status:** [OPEN] · NON-CANONICAL · not needed until Phase 2
- **Missing decision:** SoT §51 says `/docs` holds runbooks. SoT §39 requires a tested kill switch, a rollback and disable path, and an incident playbook with a named owner before any customer-facing action. None of these documents exists.
- **Why it matters:** they are a precondition for shadow, assisted and governed production (§39, §40.3 "Added before any production use").
- **Proposed default:** none is written now. They are written and tested before Phase 2 production, with the real system they describe.
- **What would invalidate it:** a design partner requires them earlier.

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

- **Status:** [OPEN] · NON-CANONICAL · decide before `/contracts` v1 is frozen (Phase A exit, §40.1)
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
  - Trace security work to PLAT-NFR-14, PLAT-NFR-20, BD-11, INV-01 to INV-22 and AGENT-09/10/13, plus a §47 reference.
  - Trace performance work to PLAT-NFR-13, POC-NFR-09 and a §48 reference.
- **What would invalidate it:** a SoT revision that defines these ID families.

<a id="od-p-08"></a>
### OD-P-08: Value sets for authority-layer results and reason codes are not enumerated

- **Status:** [OPEN] · NON-CANONICAL · decide before contracts v1 freeze
- **Missing decision:** the SoT gives these values only as examples:
  - the Decision Record's `authority` layer results: `PASS`, `NOT_EVALUATED` (§43.2);
  - Trust reason codes: `AMBIGUOUS_COUNTERPARTY` (§43.2), `PROHIBITED_CAPABILITY` (US-10).
- **Why it matters:** both are cross-boundary contract fields (PLAT-FR-05, POC-FR-06).
- **Proposed default:** treat these as examples only. Define the value sets with the contract freeze and record the decision.
- **What would invalidate it:** a SoT revision that enumerates them.

<a id="od-p-09"></a>
### OD-P-09: The canonical risk-class set and its ownership

- **Status:** [OPEN] · NON-CANONICAL
- **Missing decision:**
  - The SoT uses `R0` read/internal, `R1` append-only write, `R2` non-monetary write and `PROHIBITED` (§34.3).
  - It uses `R3` once, in an [ILLUSTRATIVE] telecom row (§15.4).
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
