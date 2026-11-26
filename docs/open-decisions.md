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
| OD-01 | Pricing model | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Fixed-fee, time-bounded pilot on one exception subtype, with success criteria, eligible-case definition, denominator, exclusions, data source and dispute process agreed in writing before signature; never per seat. Four outcome buckets counted from day one (verified success, verified safe refusal, verified escalation, unresolved or unknown). A correct refusal or escalation is a paid outcome priced below a verified success; a wrong action earns nothing. Outcome-linked pricing is tested only after both sides agree what counted; the Founder sets each pilot price from delivery cost. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-02 | Policy evaluation | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Deterministic, versioned policy-as-data evaluated only in the Go core; no Cedar or OPA in the POC; no policy logic in the model service; missing, malformed or conflicting policy never yields ALLOW. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-03 | Ambiguity thresholds | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** 0.35 auto-resolve margin; escalate above 4 candidates; both are pack data (intent-node `disambiguation`, §15.3), versioned and recorded in the Decision Record, and separate from the PERD resolution values; no score authorises an action. Changes need a full benchmark run and human approval. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-04 | Speech providers | **DECIDED 9 Oct 2026 (DEC-2026-10-09; BD-16).** Aethex AI, Indigenius and N-ATLAS, all integrated behind the provider-neutral speech interface. Default per locale chosen by benchmark (key-slot accuracy, then latency, then cost); switchable by configuration. Each must pass the voice subset and the real-conditions gate (§37.5) before it serves a demo or pilot, and must clear vendor due diligence (data terms, continuity) before handling partner data. | Closed | Closed | [DEC-2026-10-06-vendor-benchmarks](decisions/DEC-2026-10-06-vendor-benchmarks.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-05 | Model providers for Understanding | **DECIDED 9 Oct 2026 (DEC-2026-10-09; BD-16).** GPT, Gemini and Claude, all integrated behind the provider-neutral interface. Default per task chosen by intent accuracy on the code-switched suite; switchable by configuration; automatic failover to another integrated provider. Each provider's enterprise data-retention terms are confirmed, and account data is masked before it is sent, before any partner data flows. | Closed | Closed | [DEC-2026-10-06-vendor-benchmarks](decisions/DEC-2026-10-06-vendor-benchmarks.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-06 | Record integrity | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** POC: append-only, hash-chained Record in Postgres with canonical serialisation, a chain verifier in CI and the nightly job, and restricted write roles; described as tamper-evident within the POC threat model, never as immutable. **Amended 31 Oct 2026 (DEC-2026-10-31-proof-depth-and-completeness D18–D20):** in the POC, every event is signed by its writing power's key and verified on append, and chain heads are anchored on a schedule and at every run boundary to a separately controlled write-once store; the wording stays tamper-evident (never tamper-proof or immutable). | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-07 | Durable execution engine | **DECIDED 9 Oct 2026 (DEC-2026-10-06-architecture-and-contracts, confirmed by DEC-2026-10-09).** Temporal from the POC onward, under the rules in §35.6 and INV-30. Postgres remains the only authoritative store. | Closed | Closed | [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-08 | Data retention | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Minimal by default; raw audio discarded after transcription unless a documented dispute needs it (consent, purpose, expiry, restricted access recorded); identifiers masked before any model-provider call; synthetic data only until a partner-specific schedule exists. No universal retention period is set. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-09 | Policy precedence when policy changes mid-case | **DECIDED in v1.2 (see INV-09, INV-26).** Any policy change voids outstanding grants and Trust re-evaluates under the version in force; a rule marked AT_ADMISSION in policy data keeps the version in force when the intent was admitted. Trust never infers "stricter". | Closed | Closed | [DEC-2026-10-02-sot-v1.2](decisions/DEC-2026-10-02-sot-v1.2.md) |
| OD-10 | Public benchmark scope | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Publish taxonomy, case schema, fault model, scoring method, evaluation protocol and aggregate results including failures and safety-gate results, with counts, versions, confidence bounds and limitations. Never the held-out set, oracle labels, partner data, secrets or abusable exploit detail; a synthetic result is never presented as production performance; REV checks for leakage and reproducibility first. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-11 | Implementation language and deployment shape | **DECIDED 9 Oct 2026 (DEC-2026-10-09).** Two deployables split at the model boundary: Python model service; Go core service (§35.6). | Closed | Closed | [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md), [DEC-2026-10-09-deployment-temporal-providers](decisions/DEC-2026-10-09-deployment-temporal-providers.md) |
| OD-12 | First design partner and customer channel | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** One Nigerian bank or large fintech via an overlay in its own app or support channel, with a named executive KPI owner, measurable exception volume, authoritative evidence, a technical integration owner, agreement to baseline, shadow mode and stop conditions, and willingness to review failures. Exactly one exception subtype from discovery evidence; if none qualifies, discovery continues. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-13 | First production deployment model | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Single-tenant SaaS in a partner-approved region with separate credentials, database, keys, network boundary and operator access; no multi-tenant production until isolation, cross-tenant negative tests, backup/restore and independent review pass; customer VPC only when a qualified buyer requires and sponsors it. Two deployables, unchanged. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-14 | Certifications the first buyers require, and when | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Keep the §50.3 roadmap: SOC 2 Type I in Phase 2, Type II in Phase 3, ISO/IEC 27001 and 42001 in Phase 4; build the controls now; never claim a certification before the report exists. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-15 | The exact Mode 2 contract | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** Not defined or implemented in the POC; only the concept is frozen (request → decision → optional grant → execution → verdict, with the delegation chain); Noema re-evaluates at its own boundary and never trusts an upstream ALLOW; the exact contract is derived from Mode 1 production evidence. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
| OD-16 | Custody of the held-out benchmark set | **DECIDED 17 Oct 2026 (DEC-2026-10-17-open-decisions-closure).** The held-out set lives in `Noemai-org/benchmark-heldout`; the Founder is custodian and runs release evaluations; the Technical Co-Founder and every coding agent have no access; release runs use a frozen commit and pinned configuration and produce a signed bundle; every published benchmark report states the custody arrangement, and REV reviews leakage controls before any public claim. | Closed | Closed | [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) |
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

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** `docs/decisions/` holds founder and engineering decisions alike; technology decisions never live in `brain` (execution reset E8); a record that changes the SoT lands with the SoT edit and the regenerated register (AGENT-29).
- **Missing decision:** SoT §0.4 ranks "the engineering decision log" sixth (item 6) but does not say where it lives. Since SoT v1.2, §0.4 item 1 says a founder decision counts only once it is committed to the SoT or to `docs/decisions/`, so the founder decision log now has a defined home. The engineering decision log's location is still unstated.
- **Why it matters:** without a defined location, an engineer or agent cannot apply the full order of authority.
- **Proposed default:**
  - Use [`decisions/`](decisions/README.md) for the engineering decision log as well.
  - Until a committed founder decision is added there, the SoT is the highest authority available in this repository. The first record is [DEC-2026-10-02-sot-v1.2](decisions/DEC-2026-10-02-sot-v1.2.md).
  - Do not invent historical decisions.
- **What would invalidate it:** the founders keep the log elsewhere. In that case, link it from `decisions/README.md`.
- **Note (v1.3):** founder decisions now live in [`decisions/`](decisions/README.md), and AGENT-29 requires each decision record to land in the same pull request as the matching SoT edit and the regenerated register. The engineering decision log lives in `decisions/` as well (DEC-2026-10-17, OD-P-02).

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

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** No fictional runbooks. Before any customer-facing action, each of kill switch, rollback, incident response, unknown-outcome reconciliation, credential rotation, backup/restore including Record integrity, provider outage and data deletion is written against the real system and exercised, with an owner and a last-tested date; scaffolds do not satisfy the gate (task OPS-06).
- **Missing decision:** SoT §51 says `/docs` holds runbooks. SoT §39 requires a tested kill switch, a rollback and disable path, and an incident playbook with a named owner before any customer-facing action. None of these documents exists.
- **Why it matters:** they are a precondition for shadow, assisted and governed production (§39, §40.3 "Added before any production use").
- **Proposed default:** none is written now. They are written and tested before Phase 2 production, with the real system they describe.
- **What would invalidate it:** a design partner requires them earlier.
- **Note:** empty scaffolds (headings and TODOs only, no steps) now exist in [`runbooks/`](runbooks/README.md), proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md). No runbook is written or tested yet; the gate and its owner are in [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (task OPS-06).

<a id="od-p-05"></a>
### OD-P-05: Superseded source drafts are only partly present

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** No action; nothing is reconstructed. Originals are archived only if found, labelled non-authoritative.
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

- **Status:** [CLOSED] · Enums decided in [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md) (PR #4); one value removed and the lifecycle written by [DEC-2026-10-16-money-and-value-lists](decisions/DEC-2026-10-16-money-and-value-lists.md) §2.1. The value list is normative; see [`engineering/state-registry.md`](engineering/state-registry.md) §6.
- **Missing decision:** the Intent Object example (§43.1) has `"status": "VALIDATED"`, but the SoT lists no other value and no lifecycle for this field. The SoT does define:
  - the versioning rules (`version`, `supersedes`, immutable once admitted to Trust);
  - clarification binding (POC-FR-13).
- **Why it matters:** a schema cannot be frozen with an open enum, and the contract freeze is a Phase A exit condition.
- **Proposed default:** do not define the enum in documentation. Settle it with the contract freeze and record it as a decision.
- **What would invalidate it:** a SoT revision that enumerates it.

<a id="od-p-07"></a>
### OD-P-07: `SEC-` and `PERF-` ID prefixes are named but undefined

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** Not minted. Trace to PLAT-NFR, POC-NFR, INV, BD and AGENT IDs plus SoT §47 and §48.
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

- **Status:** [CLOSED] · Enums decided in [DEC-2026-10-06-architecture-and-contracts](decisions/DEC-2026-10-06-architecture-and-contracts.md) (PR #4); one value removed and the reason codes completed by [DEC-2026-10-16-money-and-value-lists](decisions/DEC-2026-10-16-money-and-value-lists.md) §2.2 and §2.3. The value lists are normative; see [`engineering/state-registry.md`](engineering/state-registry.md) §2.
- **Missing decision:** the SoT gives these values only as examples:
  - the Decision Record's `authority` layer results: `PASS`, `NOT_EVALUATED` (§43.2);
  - Trust reason codes: `AMBIGUOUS_COUNTERPARTY` (§43.2), `PROHIBITED_CAPABILITY` (US-10), `DECLINED_BY_APPROVER` (§43.2a, since v1.2).
- **Why it matters:** both are cross-boundary contract fields (PLAT-FR-05, POC-FR-06).
- **Proposed default:** treat these as examples only. Define the value sets with the contract freeze and record the decision.
- **What would invalidate it:** a SoT revision that enumerates them.

<a id="od-p-09"></a>
### OD-P-09: The canonical risk-class set and its ownership

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** `PROHIBITED` is core and structural; R0 to R3 are fintech pack data exactly as SoT §34.3; declared risk is never below the consequence profile (`packcheck` enforces it); an unknown risk label fails pack validation.
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

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** Names unchanged. Distinct enum types per field in `/contracts`, with negative contract tests proving they cannot be cross-assigned (task CON-06).
- **Missing decision:** two pairs of terms look alike but mean different things:
  - `OUTCOME_UNKNOWN` is an Execution Receipt `execution_state` (§43.3) and the classification for a lost case-write response (§35.5). `EXECUTION_OUTCOME_UNKNOWN` is a *transaction* lifecycle state in the synthetic environment and the classification for a ledger debit with a switch timeout (§35.5).
  - Severity classes `S0`–`S3` (§38.3) share a prefix with data-sensitivity labels such as `S3_financial_pii` and "data class S4" (§15.3, §15.4).
- **Why it matters:** an engineer or agent could conflate them.
- **Proposed default:** keep every name exactly as the SoT writes it, and always qualify a value by the object or field it belongs to. [`engineering/state-registry.md`](engineering/state-registry.md) does this.
- **What would invalidate it:** a SoT revision that renames either pair.

<a id="od-p-11"></a>
### OD-P-11: POC-FR-17 maps to no platform requirement

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** POC-only; no PLAT ID.
- **Missing decision:** POC-FR-17 (the evidence panel) maps to "Demo evidence" rather than to a PLAT-FR ID (§37.1). It is not stated whether an evidence or reconstruction view is a platform requirement beyond PLAT-FR-12 (reconstruction API) and PLAT-US-05/06.
- **Proposed default:** treat POC-FR-17 as a POC-only requirement. Do not mint a PLAT ID.
- **What would invalidate it:** a SoT revision that adds one.

<a id="od-p-12"></a>
### OD-P-12: Legacy concepts with no owner in the SoT (OPEN / UNOWNED)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** None adopted. A real failing case raises a specific AGENT-02 entry.
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

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-execution-reset](decisions/DEC-2026-10-16-execution-reset.md) E2 and [DEC-2026-10-16-contract-and-pack-clarifications](decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) C8 (point 1); confirmed as closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) (nothing is re-decided).
- **Answer:** The Founder is the benchmark owner and does not drive the C1 or C2 build areas; the Technical Co-Founder and every coding agent never read the held-out set.
- **Question:** Who is the benchmark owner?
- **Why it matters:** OD-16; release runs; held-out set
- **Minimum safe default (meanwhile):** Founder-appointed person outside the build team
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Founders
- **Deadline:** Before P3
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-01. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-15"></a>
### OD-P-15: Who reviews arm competence? (OQ-02)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-contract-and-pack-clarifications](decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) C8 (point 2) and plan task GOV-21; confirmed as closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) (nothing is re-decided).
- **Answer:** Two external people, ARM (arm builder) and REV (independent arm reviewer), under NDA, confirmed by GOV-11 on Fri 30 Oct.
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

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-money-and-value-lists](decisions/DEC-2026-10-16-money-and-value-lists.md) M1 to M10 (takes effect when that record is approved and merged). Closes OQ-06 and SOT-C-11.
- **Answer (DEC-2026-10-16-money-and-value-lists M1 to M10):** Every currency amount is an integer count of the currency's minor unit (NGN 20,000.00 is `2000000`), with an ISO 4217 currency in its own field and the exponent from one versioned table, `contracts/currencies.json`. There is no marker: in `/contracts` v1 every amount is in minor units. Bounds are 0 to 9,007,199,254,740,991 (2⁵³ − 1), the JCS ceiling; no floating point at any layer; conversion only at the edges, by deterministic code, never by a model; addition, subtraction and comparison only, within one currency. SoT §43.1 is corrected in SoT v1.7. Tests are the M10 table (CON-01 fixtures and CON-04 vectors).
- **Question:** Quantity units in the Intent Object (major vs minor)
- **Why it matters:** Money correctness
- **Minimum safe default (meanwhile):** Minor units plus a marker (contract minor version)
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Tech lead
- **Deadline:** P1
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-06. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-20"></a>
### OD-P-20: Which speech providers offer streaming TTS for all five locales? (OQ-07)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** Provider-neutral per-locale routing; where streaming TTS is missing or fails its gate, the verified answer is shown as text. Demo TTS is English and Pidgin only (clarifications C8 cut item 1); Yoruba, Hausa and Igbo are still measured; no locale is claimed until it passes.
- **Question:** Which speech providers offer streaming TTS for all five locales?
- **Why it matters:** Voice answer path
- **Minimum safe default (meanwhile):** Text on screen where TTS is missing
- **What would change it:** Vendor documentation and tests
- **Owner:** Voice lead
- **Deadline:** Week 1
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-07. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-21"></a>
### OD-P-21: Field protocol owner, devices and SIMs (OQ-08)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD §45.4 is the gate as written (Tecno Spark on Airtel 3G with 4G disabled, genuine Lagos noise, at least 100 sessions with at least 50% Pidgin, P95 ≤ 2.5 s from end of speech to admitted Intent Object, consent-recorded sessions); the Voice Lead owns it; extra devices and networks are non-gating diagnostics.
- **Question:** Field protocol owner, devices and SIMs
- **Why it matters:** Voice gate
- **Minimum safe default (meanwhile):** §45.4 protocol
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Voice lead
- **Deadline:** Week 3
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-08. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-22"></a>
### OD-P-22: Secrets manager for shared environments (OQ-09)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** Local: file-mounted secrets outside git. CI: GitHub Environments (`core-ci`, `model-ci`, `bench`) with OIDC where supported. Hosted: the managed secret store of the host recorded in the `local-setup` runbook. Credentials are separated per deployable and environment; grant and confirmation HMAC keys live only in the core; the model service holds no core-database, Temporal, adapter or grant credentials; no secret in source, images, logs, prompts, traces, Record payloads or agent context.
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

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** A durable Noema-owned handoff record (reason, urgency, evidence references, target queue if known, correlation ID) shown in the ops inspector; the customer is told that no case reference exists yet and someone must act; nothing claims a person accepted it without an acknowledgement. No external `escalation.handoff` event in the POC; it is added only after partner discovery specifies the receiver, acknowledgement and retry semantics.
- **Question:** How is an ESCALATE handoff without a case delivered to the partner? (The SoT listener has no handoff event)
- **Why it matters:** Unresolved-target escalations
- **Minimum safe default (meanwhile):** Customer instruction plus the ops inspector only. Propose an `escalation.handoff` event as a contract addition after partner discovery
- **What would change it:** Partner requirements
- **Owner:** Product
- **Deadline:** Before the first partner demo
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-11. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-25"></a>
### OD-P-25: Tenant time zone and lexicon reviewers (native speakers for yo, ha, ig, pcm) (OQ-12)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** Store UTC instants plus an IANA time zone; the tenant default is `Africa/Lagos` and configurable; the zone is never inferred from language or phone number. Native reviewers for yo, ha, ig and pcm are contracted before labels freeze and adjudicate disagreements; machine translation is not evidence.
- **Question:** Tenant time zone and lexicon reviewers (native speakers for yo, ha, ig, pcm)
- **Why it matters:** Time windows; numerals
- **Minimum safe default (meanwhile):** Africa/Lagos; reviewers to be contracted
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Founders
- **Deadline:** P5
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-12. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-26"></a>
### OD-P-26: Do the value lists in DEC-2026-10-06-architecture-and-contracts differ from this PERD's lists? (OQ-13)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-money-and-value-lists](decisions/DEC-2026-10-16-money-and-value-lists.md) §2 (takes effect when that record is approved and merged). Closes OQ-13 and SOT-C-26.
- **Answer (DEC-2026-10-16-money-and-value-lists §2):** The diff is the record's reconciliation. Intent Object `status` is `EXTRACTED`, `VALIDATED`, `REJECTED_AT_GATE` (`SUPERSEDED` removed; the PERD's `INADMISSIBLE` renamed). Authority results are `PASS`, `FAIL`, `NOT_EVALUATED` (`OVERRIDDEN` removed). Trust reason codes are two tiers: a closed core enum with producers, and pack codes in the `<vertical>.reason.<name>` namespace. `docs/engineering/state-registry.md` is the single normative home of the core lists, and CON-01 adds a CI check that fails on any difference between it and `/contracts`.
- **Question:** Do the value lists in DEC-2026-10-06-architecture-and-contracts differ from this PERD's lists?
- **Why it matters:** Contract drift
- **Minimum safe default (meanwhile):** The DEC record governs. Agents must diff before P1
- **What would change it:** — (none stated in PERD §67.2)
- **Owner:** Tech lead
- **Deadline:** P1
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-13. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-27"></a>
### OD-P-27: Legal validation of synthetic clocks before any external claim (OQ-14)

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** Every synthetic time, deadline and clock is labelled `SYNTHETIC` in UI, logs, exports and demo narration; no regulatory or legal claim without counsel review of the exact wording.
- **Question:** Legal validation of synthetic clocks before any external claim
- **Why it matters:** Regulatory accuracy
- **Minimum safe default (meanwhile):** All clocks labelled SYNTHETIC
- **What would change it:** Counsel review
- **Owner:** Founders
- **Deadline:** Before any external demo
- **Source:** [PERD](poc/perd/README.md) §67.2, OQ-14. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-28"></a>
### OD-P-28: PERD [REC] defaults: Trust semantics

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD §23.1 adopted as written: the seven outcomes with WAIT and UNKNOWN defined, linked disposition and action decisions with `disposition_decision_id`, and R0 reads without grants (principal-scoped, allow-listed and recorded). Closes SOT-C-03, 04, 05.
- **Missing decision:** whether to adopt the PERD [REC] defaults for trust semantics. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** WAIT and UNKNOWN definitions (§23.1); disposition and action decision linkage plus a `disposition_decision_id` field; R0 reads without grants
- **Where they are specified:** [PERD](poc/perd/README.md) §23.1 (the seven outcomes; disposition and action decisions, REQ-TRU-010); §25.1 (R0 reads and grants). Conflicts SOT-C-03, SOT-C-04, SOT-C-05.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-29"></a>
### OD-P-29: PERD [REC] defaults: Investigation state

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD §28.2 adopted exactly as written, as a projection changed only by named, guarded commands, kept separate from transaction state, execution state, verdict, case lifecycle and Temporal status.
- **Missing decision:** whether to adopt the PERD [REC] defaults for investigation state. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** The investigation state machine (§28.2)
- **Where they are specified:** [PERD](poc/perd/README.md) §28.2 (investigation state machine); §28.3 (REQ-STM-001, REQ-STM-002).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-30"></a>
### OD-P-30: PERD [REC] defaults: Resolution

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD values adopted: ranking weights, 0.70 floor, 0.85 key-slot threshold, 10-minute clarification, 2 rounds, 30-minute dormancy, 72-hour resume; independent of OD-03.
- **Missing decision:** whether to adopt the PERD [REC] defaults for resolution. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Ranking weights; 0.70 floor; 0.85 key-slot threshold; clarification 10 min; 2 rounds; dormancy 30 min; resume 72 h
- **Where they are specified:** [PERD](poc/perd/README.md) §22.1 (ambiguity lifecycle: REQ-AMB-003 ranking and floor, REQ-AMB-004 to REQ-AMB-006 clarification, rounds, dormancy and resume, REQ-AMB-007 key-slot threshold). Touches SoT OD-03.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-31"></a>
### OD-P-31: PERD [REC] defaults: Grants and confirmations

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** 10-minute TTL for grants and confirmations, single-use, exactly bound, with revalidation before dispatch; a confirmation is never a grant; any change voids it.
- **Missing decision:** whether to adopt the PERD [REC] defaults for grants and confirmations. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Grant TTL 10 min; confirmation TTL 10 min
- **Where they are specified:** [PERD](poc/perd/README.md) §23.6 (REQ-TRU-008 Decision Grant issuance; REQ-TRU-009 confirmation contract).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-32"></a>
### OD-P-32: PERD [REC] defaults: Recovery

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** A budget of 2 dispatches (a ceiling, not an obligation); verify before any retry; retry safety NONE means one dispatch at most; verification reads use 3 attempts at 1, 3 and 9 s of simulated time.
- **Missing decision:** whether to adopt the PERD [REC] defaults for recovery. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Recovery budget of 2 dispatches; verification read schedule
- **Where they are specified:** [PERD](poc/perd/README.md) §30.2 (recovery decision table); §30.3 (REQ-RCV-003 recovery budget); §29.2 (REQ-VER-001 verification read retries).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-33"></a>
### OD-P-33: PERD [REC] defaults: Watches and callbacks

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD schedules as written: watches at 5, 15 and 30 min, then every 60 min, plus named events, until the deadline (then UNKNOWN and a RecoveryRequest); callbacks at least once from the outbox, exponential from 1 s doubling, capped at 10 min, at most 12 attempts, then a metric and an ops alert.
- **Missing decision:** whether to adopt the PERD [REC] defaults for watches and callbacks. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Watch schedule; callback retry schedule
- **Where they are specified:** [PERD](poc/perd/README.md) §29.2 (REQ-VER-004 durable outcome watch; REQ-VER-005 `outcome.updated` callback).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-34"></a>
### OD-P-34: PERD [REC] defaults: Contracts and identifiers

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** JCS; LP key encoding; `policy_scope` = `policy_id`; the PERD ID scheme and Record events; `evidence_set_hash` is the LP construction of DEC-2026-10-16 clarifications C1 (the JCS-array proposal is rejected). Closes SOT-C-13.
- **Missing decision:** whether to adopt the PERD [REC] defaults for contracts and identifiers. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** JCS canonicalisation; length-prefixed key encoding; `policy_scope` = `policy_id`; ID scheme; Record event additions
- **Where they are specified:** [PERD](poc/perd/README.md) §27.2 (idempotency key and `policy_scope`, SOT-C-13); §32.1 to §32.3 (Record event, event types, ID scheme).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-35"></a>
### OD-P-35: PERD [REC] defaults: Policy

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** The PERD §23.4 schema and ladder as written: SAFETY > PROHIBITION > TENANT_SECURITY > REGULATORY > WORKFLOW > DEFAULT across classes; REJECT > ESCALATE > CONFIRM > WAIT > PERMIT within the winning class; no matching PERMIT gives `NO_PERMITTING_RULE`.
- **Missing decision:** whether to adopt the PERD [REC] defaults for policy. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Policy schema and precedence ladder
- **Where they are specified:** [PERD](poc/perd/README.md) §23.4 (policy as data, precedence).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-36"></a>
### OD-P-36: PERD [REC] defaults: Freeze

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** The PERD allow-list exactly (escalation case, evidence record, routing, held as pack data) and nothing else; a model can never release a freeze; INV-20 names the allow-list (SoT v1.8). Closes SOT-C-12.
- **Missing decision:** whether to adopt the PERD [REC] defaults for freeze. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Freeze allow-list
- **Where they are specified:** [PERD](poc/perd/README.md) §22.3 (REQ-RES-002 contradiction freeze). Conflict SOT-C-12.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-37"></a>
### OD-P-37: PERD [REC] defaults: Explanation

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** The PERD facts contract and claim validator; on validation failure, a deterministic fallback from verified facts.
- **Missing decision:** whether to adopt the PERD [REC] defaults for explanation. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Facts contract and claim validator
- **Where they are specified:** [PERD](poc/perd/README.md) §31.2 (facts contract); §31.3 (REQ-EXP-002 claim validator).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-38"></a>
### OD-P-38: PERD [REC] defaults: Fault injection

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD §37.1 FaultPlan and effect enum, amended by DEC-2026-10-12: `source` ∈ TUSHE, PROXY, MOCK_CASE; the `clock` block drives only Noema's simulated clock and `mock-case`, never Tushe; deterministic release runs (probabilities 0 or 1), with seeded stress runs separate.
- **Missing decision:** whether to adopt the PERD [REC] defaults for fault injection. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** FaultPlan contract
- **Where they are specified:** [PERD](poc/perd/README.md) §37.1 (FaultPlan contract and effect enum).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-39"></a>
### OD-P-39: PERD [REC] defaults: Benchmark

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** The PERD case schema, the evil provider (test-only, no credentials) and A0 as a diagnostic that never appears in a comparative claim; Tier 0 results reported separately. Closes SOT-C-18.
- **Missing decision:** whether to adopt the PERD [REC] defaults for benchmark. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Case schema; evil provider; A0 diagnostic arm
- **Where they are specified:** [PERD](poc/perd/README.md) §48.2 (case contract); §49 (the evil provider); §50.1 (A0 diagnostic, SOT-C-18).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-40"></a>
### OD-P-40: PERD [REC] defaults: Infrastructure

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD §36.1, §41.1 and §65.1 adopted: a separate `temporal` database that Noema code never reads; per-power Postgres roles with one core process identity in the POC (SoT §47.1 reworded); the PERD topology as amended by execution reset E6. Closes SOT-C-14 and SOT-C-16.
- **Missing decision:** whether to adopt the PERD [REC] defaults for infrastructure. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Temporal persistence database; per-power DB roles; network topology
- **Where they are specified:** [PERD](poc/perd/README.md) §36.1 (Temporal persistence, SOT-C-14); §41.1 (per-power DB roles, SOT-C-16); §65.1 (POC network topology).
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-41"></a>
### OD-P-41: PERD [REC] defaults: Retention

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) §3 (takes effect when that record is approved and merged).
- **Answer (DEC-2026-10-17 §3):** PERD §38.2 retention defaults for synthetic data (the record's §38.3 cite is corrected); partner data follows OD-08; deletion covers derived artefacts and is recorded without keeping the deleted data.
- **Missing decision:** whether to adopt the PERD [REC] defaults for retention. PERD §67.3 proposes adopting all §67.3 groups through one decision record, with any matching SoT edit and the regenerated register (AGENT-29).
- **Defaults (PERD §67.3, quoted):** Retention defaults
- **Where they are specified:** [PERD](poc/perd/README.md) §38.2 (retention column); §38.3 (retention and data-handling defaults). Real-data retention stays SoT OD-08.
- **What would invalidate them:** not stated in PERD §67.3. A decision record that accepts or replaces them. Thresholds, TTLs, budgets and provider defaults change only with a linked full benchmark run and human approval (AGENT-16, REQ-AGT-005).
- **Source:** [PERD](poc/perd/README.md) §67.3. Proposed with [DEC-2026-10-11-poc-perd-v1.1](decisions/DEC-2026-10-11-poc-perd-v1.1.md).

<a id="od-p-42"></a>
### OD-P-42: Schedule compression: Phase A in parallel with build week 1

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-10-16-execution-reset](decisions/DEC-2026-10-16-execution-reset.md) E3 and E4; confirmed as closed by [DEC-2026-10-17-open-decisions-closure](decisions/DEC-2026-10-17-open-decisions-closure.md) (nothing is re-decided).
- **Answer:** The build runs Mon 19 Oct to Fri 13 Nov; G0 is split into G0-T and G0-N, and G1 may run before G0-T but counts only once G0 passes; gates outrank dates.
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

<a id="od-p-46"></a>
### OD-P-46: Value types in the Action Graph node

- **Status:** [DECIDED] · NON-CANONICAL · the stated default is accepted by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** the types of `on_unknown`, `on_failure`, `recovery_ref` and `escalation_ref` (PERD §24 lists the fields with no value)
- **Why it matters:** the Planner and packcheck cannot check a graph without them
- **Minimum safe default (meanwhile):** `on_*` are the PERD §30.1 recovery types (RETRY_READ, VERIFY_BY_IDEMPOTENCY_KEY, RETRY_UNDER_NEW_GRANT, ESCALATE); `recovery_ref` is one of the capability's own `recovery[]`; `escalation_ref` is CASE or HANDOFF (PERD §30.2)
- **What would change it:** the PERD or SoT giving the types
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the Planner task (PLN-01)
- **Source:** [noema#26](https://github.com/Noemai-org/noema/pull/26); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §24, REQ-AG-001
<a id="od-p-47"></a>
### OD-P-47: Evidence-descriptor vocabulary for predicate type-checking

- **Status:** [DECIDED] · NON-CANONICAL · the stated default is accepted by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** the typed fields of each evidence entity and the typed predicate variables a pack declares (SoT §43.7 requires the type-check, and names no vocabulary)
- **Why it matters:** pack load cannot reject an unknown field without it
- **Minimum safe default (meanwhile):** `evidence_descriptors` and `predicate_variables` in the pack, with the grammar and shared corpus in `contracts/predicates/`
- **What would change it:** a vocabulary in the SoT or the Tushe worksheet
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before PCK-02 is accepted
- **Source:** [noema#26](https://github.com/Noemai-org/noema/pull/26), [noema#27](https://github.com/Noemai-org/noema/pull/27); SoT §43.7, REQ-VER-002
<a id="od-p-48"></a>
### OD-P-48: Per-kind fields of memory observations

- **Status:** [DECIDED] · NON-CANONICAL · the stated default is accepted by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** the fields of each of the six `memory_observation` kinds (PERD §33 gives the envelope and says each kind has its own schema)
- **Why it matters:** free text is forbidden, so each kind needs typed fields before anything is written
- **Minimum safe default (meanwhile):** `observation` holds typed scalars only (codes, IDs, integers, booleans)
- **What would change it:** each kind's owner supplying its field list
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the first observation is written (REC-xx)
- **Source:** [noema#26](https://github.com/Noemai-org/noema/pull/26); PERD §33, REQ-MEM-001
<a id="od-p-49"></a>
### OD-P-49: Missing SoT §15.1 minimum properties

- **Status:** [DECIDED] · NON-CANONICAL · the stated default is accepted by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** five minimum properties have no schema field: urgency; compiler model and prompt version on the Intent Object; fraud and risk signals; consent; acceptable uncertainty
- **Why it matters:** SoT §15.1 says a vertical may add fields but never remove these, so the abstract schemas must carry them
- **Minimum safe default (meanwhile):** none is carried; the POC pack needs none of them, and the table in `contracts/schemas/README.md` lists each as a gap
- **What would change it:** a decision on each, then a contract change (AGENT-15)
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the second vertical
- **Source:** [noema#26](https://github.com/Noemai-org/noema/pull/26); SoT §15.1
<a id="od-p-50"></a>
### OD-P-50: Payload schemas of the outbound events `case.created` and `confirmation.recorded`

- **Status:** [DECIDED] · NON-CANONICAL · the stated default is accepted by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** the payloads of two of the three signed events (only `outcome.updated` has a schema)
- **Why it matters:** REQ-API-001 says every object in §39.2 to §39.7 is a schema
- **Minimum safe default (meanwhile):** the integration contract names the events only
- **What would change it:** the field lists in PERD §39.7 turned into schemas
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the partner listener task (API-xx)
- **Source:** [noema#26](https://github.com/Noemai-org/noema/pull/26); PERD §39.7, REQ-API-006
<a id="od-p-51"></a>
### OD-P-51: Benchmark cases per capability, and template coverage

- **Status:** [DECIDED] · NON-CANONICAL · the stated default is accepted by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** packcheck cannot check that every capability has benchmark cases (AGENT-06) or that every template ID resolves, because there is no benchmark case set and no template container in the pack schema
- **Why it matters:** two PCK-02 checks cannot run
- **Minimum safe default (meanwhile):** both checks are listed as not run
- **What would change it:** the case set (T4) and a template container in the pack schema
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before PCK-02 is accepted
- **Source:** [noema#26](https://github.com/Noemai-org/noema/pull/26); AGENT-06, REQ-CAP-001
<a id="od-p-52"></a>
### OD-P-52: Reconciliation rule for REJECTED_CONFIRMED

- **Status:** [DECIDED] · NON-CANONICAL · EL proposed and SR concurred under Founder decision E4 of 7 Nov 2026: the situation is classified INSUFFICIENT_EVIDENCE with disposition UNKNOWN or ESCALATE; no rule yields REJECTED_CONFIRMED until the worksheet gives the values ([DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** a rule in rule set v1 that produces REJECTED_CONFIRMED. Not debited, and the authoritative source confirms rejection. Needs the ledger and switch values that mean "not debited" and "rejected", from the Tushe worksheet (INV-19: absence is never negative).
- **Why it matters:** the outcome definition `status_explained` names three of these classifications, but no rule yields them
- **Minimum safe default (meanwhile):** the situation falls to INSUFFICIENT_EVIDENCE (PERD REQ-RES-001: never a default success); a test in noema#27 asserts the fallback and that no rule produces it
- **What would change it:** the founders adding the rule and the Tushe field semantics
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before G0-T is signed
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §22.3, REQ-RES-001
<a id="od-p-53"></a>
### OD-P-53: Reconciliation rule for DEBIT_POSTED_CREDIT_UNCONFIRMED

- **Status:** [DECIDED] · NON-CANONICAL · EL proposed and SR concurred under Founder decision E4 of 7 Nov 2026: a non-terminal state (WAIT with a deadline, then ESCALATE); never a success; UNKNOWN without the worksheet switch value ([DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** a rule in rule set v1 that produces DEBIT_POSTED_CREDIT_UNCONFIRMED. Debit KNOWN, credit UNKNOWN or UNAVAILABLE, switch non-terminal. Needs the switch value that means non-terminal.
- **Why it matters:** the outcome definition `status_explained` names three of these classifications, but no rule yields them
- **Minimum safe default (meanwhile):** the situation falls to INSUFFICIENT_EVIDENCE (PERD REQ-RES-001: never a default success); a test in noema#27 asserts the fallback and that no rule produces it
- **What would change it:** the founders adding the rule and the Tushe field semantics
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before G0-T is signed
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §22.3, REQ-RES-001
<a id="od-p-54"></a>
### OD-P-54: Reconciliation rule for REVERSAL_PENDING

- **Status:** [DECIDED] · NON-CANONICAL · closed by ruling A31 of DEC-2026-11-07-architect-rulings (REVERSAL_PENDING is non-terminal), confirmed by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once both records merge.
- **Missing decision:** a rule in rule set v1 that produces REVERSAL_PENDING. Reversal initiated, not yet posted. Needs the rule and the reversal values that mean initiated.
- **Why it matters:** the outcome definition `status_explained` names three of these classifications, but no rule yields them
- **Minimum safe default (meanwhile):** the situation falls to INSUFFICIENT_EVIDENCE (PERD REQ-RES-001: never a default success); a test in noema#27 asserts the fallback and that no rule produces it
- **What would change it:** the founders adding the rule and the Tushe field semantics
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before G0-T is signed
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §22.3, REQ-RES-001
<a id="od-p-55"></a>
### OD-P-55: Reconciliation rule for PARTIAL

- **Status:** [DECIDED] · NON-CANONICAL · EL proposed, SR amended and EL confirmed under Founder decision E4 of 7 Nov 2026: the pack models one debit leg per transaction and no multi-leg facts, so anything not established as a single leg is UNKNOWN and escalates; no PARTIAL rule is built until a pack entity models legs ([DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** a rule in rule set v1 that produces PARTIAL. A multi-leg transaction with a missing leg. Needs the multi-leg facts, which no pack entity models yet.
- **Why it matters:** the outcome definition `status_explained` names three of these classifications, but no rule yields them
- **Minimum safe default (meanwhile):** the situation falls to INSUFFICIENT_EVIDENCE (PERD REQ-RES-001: never a default success); a test in noema#27 asserts the fallback and that no rule produces it
- **What would change it:** the founders adding the rule and the Tushe field semantics
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before G0-T is signed
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §22.3, REQ-RES-001
<a id="od-p-56"></a>
### OD-P-56: Reconciliation rule for EVENT_ORDER_UNCERTAIN

- **Status:** [DECIDED] · NON-CANONICAL · EL proposed and SR concurred under Founder decision E4 of 7 Nov 2026: the case is held as uncertain and escalates; Noema never picks an order ([DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** a rule in rule set v1 that produces EVENT_ORDER_UNCERTAIN. Ordering cannot be established. Needs the ordering facts and the rule that detects them.
- **Why it matters:** the outcome definition `status_explained` names three of these classifications, but no rule yields them
- **Minimum safe default (meanwhile):** the situation falls to INSUFFICIENT_EVIDENCE (PERD REQ-RES-001: never a default success); a test in noema#27 asserts the fallback and that no rule produces it
- **What would change it:** the founders adding the rule and the Tushe field semantics
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before G0-T is signed
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §22.3, REQ-RES-001
<a id="od-p-57"></a>
### OD-P-57: `allowed_under_freeze` on the capability descriptor

- **Status:** [DECIDED] · NON-CANONICAL · `allowed_under_freeze` is not allowed under freeze: the default is false and a capability is refused while frozen (Founders, Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** the descriptor field REQ-RES-002 says declares which capabilities are allowed under a contradiction freeze (CREATE_ESCALATION_CASE, RECORD_INVESTIGATION_EVIDENCE, ROUTE_TO_INTERNAL_OWNER)
- **Why it matters:** the freeze gate in `trust/reconcile` needs the list from pack data, and the schema has no such field
- **Minimum safe default (meanwhile):** the gate takes the list as an argument
- **What would change it:** a contract change adding the field (AGENT-15) once noema#26 has merged
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the grant constructor (TRU-08)
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); PERD REQ-RES-002
<a id="od-p-58"></a>
### OD-P-58: Reconciliation rule set v1 differs from the PERD text in three places

- **Status:** [DECIDED] · NON-CANONICAL · EL proposed and SR concurred under Founder decision E4 of 7 Nov 2026: the three deviations and the certainty tiers (definitive 2, indefinite 1) are accepted ([DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** whether rule set v1 may differ from PERD §22.3 where the PERD's own properties need it: R1 also requires no pending settlement, no pending reversal and no unavailable required source; R3 does not fire when the reversal conflicts with another fact; two KNOWN rows of a single-valued fact with different states are a contradiction. The certainty tiers are also set (definitive 2, indefinite 1)
- **Why it matters:** without these, a pending settlement past its window or a lost required source gave SUCCESS_CONFIRMED, which breaks "no pending state is collapsed into a terminal one" and "losing a source never raises certainty" (REQ-RES-001)
- **Minimum safe default (meanwhile):** the safer reading as built in noema#27, proposed for adoption in [DEC-2026-10-20-reconciliation-ruleset-v1](decisions/DEC-2026-10-20-reconciliation-ruleset-v1.md) (Proposed)
- **What would change it:** the founders amending PERD §22.3 or choosing the literal R1
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before G0-T
- **Source:** [noema#27](https://github.com/Noemai-org/noema/pull/27); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §22.3, REQ-RES-001
<a id="od-p-59"></a>
### OD-P-59: Free-text and speech answer binding

- **Status:** [DECIDED] · NON-CANONICAL · a free-text or speech answer binds only through a confirmed slot (Founders, Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** how REQ-AMB-005's deterministic label matching and model-assisted mapping to an option ID are split between the model service and Trust (noema#28 binds only clicks and negations)
- **Why it matters:** the answer path for voice and free text is not built
- **Minimum safe default (meanwhile):** only option IDs and negations are bound
- **What would change it:** a decision on the split, then T6.3 and T5
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the voice track
- **Source:** [noema#28](https://github.com/Noemai-org/noema/pull/28); PERD REQ-AMB-005
<a id="od-p-60"></a>
### OD-P-60: The state EXPLAINING_BLOCKED has no definition and no exit

- **Status:** [DECIDED] · NON-CANONICAL · decided by the Founders on 7 Nov 2026 (Block E, E4): the state exits to ESCALATING, an escalation case routed to OPS. Written into PERD v1.21 §28.2 in docs#130; it counts once that pull request is merged.
- **Missing decision:** what EXPLAINING_BLOCKED is and where it goes. PERD §28.2 lists "→ EXPLAINING_BLOCKED → fallback" as an exit of EXPLAINING, but gives the state no entry, no exit, no customer text and no audit trail, and "fallback" names no state.
- **Why it matters:** a blocked explanation (REQ-EXP-002: a claim not bound to a fact) must end in a safe, defined state, and the transition table (REQ-STM-001) cannot be complete without one.
- **Minimum safe default (meanwhile):** `transitions.yaml` has the row EXPLAINING → EXPLAINING_BLOCKED and no row leaving it, so an investigation that reaches it stays there and the safe fallback text is shown (REQ-EXP-002 failure behaviour).
- **What would change it:** a definition in the PERD of the state and its exit.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the explanation task (EXP-xx)
- **Source:** [noema#30](https://github.com/Noemai-org/noema/pull/30); [PERD v1.10](poc/perd/NOEMA_POC_PERD_v1.10.md) §28.2, REQ-STM-001, REQ-EXP-002.
<a id="od-p-61"></a>
### OD-P-61: PyYAML as a pinned CI dependency (AGENT-14)

- **Status:** [CLOSED] · NON-CANONICAL · withdrawn 20 Oct 2026: noema#29 went back to the standard-library secret-name check, so no dependency is added. The parser version stays in the history of noema#29 (commit `803e027`) for when an oracle credential is issued, and the request is raised again then.
- **Missing decision:** approval to add PyYAML 6.0.2, pinned and hashed in `tools/ci/requirements.lock`, to the CI safeguards job. It lets `check_secret_refs.py` parse workflow files and tell jobs apart, so the bench-only rule for `TUSHE_ORACLE_*` and `TUSHE_FIXTURE_*` can be enforced per job.
- **Why it matters:** `tools/ci` is standard-library only. A line scanner cannot know which job a secret reference sits in, and a hand-written YAML reader would be a security control that nobody has reviewed. The pinned parser runs on the CI runner only; it is in no service image.
- **Minimum safe default (meanwhile):** the dependency is added in noema#29 on the founders' written instruction to parse the YAML, and stays provisional until approved here. Rejecting it means replacing the parser with a strict, fail-closed reader of the workflow subset the repository uses.
- **What would change it:** the founders preferring a hand-written parser, or PyYAML failing the dependency review.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before noema#29 merges
- **Source:** [noema#29](https://github.com/Noemai-org/noema/pull/29); AGENT-14, REQ-SEC-007.
<a id="od-p-62"></a>
### OD-P-62: The network `tushe_egress` is for the hostility proxy and the webhook relay

- **Status:** [CLOSED] · NON-CANONICAL · decided 21 October 2026 by [DEC-2026-10-21-egress-layout-fault-reading](decisions/DEC-2026-10-21-egress-layout-fault-reading.md) D1: `tushe_egress` carries both the hostility proxy and the webhook relay; PERD §65.1 says so from v1.13 ("relay only" is removed).
- **Missing decision:** which services are members of `tushe_egress`.
- **Source:** the Founder's instructions of 21 October 2026; noema#48, noema#51; PERD §65.1, REQ-ENV-005.
<a id="od-p-63"></a>
### OD-P-63: IMPOSSIBLE_STATE is produced by the hostility proxy

- **Status:** [CLOSED] · NON-CANONICAL · decided 21 October 2026 by [DEC-2026-10-21-egress-layout-fault-reading](decisions/DEC-2026-10-21-egress-layout-fault-reading.md) D3: the proxy produces IMPOSSIBLE_STATE. The Founder asked to keep the committed text unless REQ-ENV-005 said otherwise; REQ-ENV-005 and DEC-2026-10-12 D4 say the proxy, and PERD §37.1's "fault controller only" line contradicted them, so v1.13 corrects the table.
- **Missing decision:** who owns IMPOSSIBLE_STATE.
- **Source:** the Founder's instructions of 21 October 2026; PERD REQ-ENV-005, §37.1, §37.2 (EC-S20); DEC-2026-10-12 D4.
<a id="od-p-64"></a>
### OD-P-64: REQ-ENV-004 needs a worked example

- **Status:** [CLOSED] · NON-CANONICAL · decided 21 October 2026 by [DEC-2026-10-21-egress-layout-fault-reading](decisions/DEC-2026-10-21-egress-layout-fault-reading.md) D4: the example is the §37.1 plan, a `mock-case` fault inside a `TUSHE` plan, which is the reading the fault-plan schema took. It is written into REQ-ENV-004 in PERD v1.13.
- **Missing decision:** the content of the REQ-ENV-004 example.
- **Source:** the Founder's instructions of 21 October 2026; Session B's description in noema#44; PERD REQ-ENV-004, §37.1.
<a id="od-p-65"></a>
### OD-P-65: The core's pull client for the webhook relay does not exist

- **Status:** [OPEN] · NON-CANONICAL · **DEFERRED** by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); not blocking.
- **Missing decision:** which task builds the core's outbound pull from the webhook relay (REQ-API-008) and with what credential handling. The relay (noema#48) and the matrix row exist; no core client does, and the proxy forwards relay pulls in the benchmark profile.
- **Why it matters:** until it exists, deliveries stored by the relay are never read.
- **Minimum safe default (meanwhile):** none; nothing pulls.
- **What would change it:** a task card for the pull client.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the event-delivery cases run
- **Source:** noema#48; PERD REQ-API-008, REQ-ENV-005.
<a id="od-p-66"></a>
### OD-P-66: `.env.example` has no entries for the relay and the proxy

- **Status:** [OPEN] · NON-CANONICAL · **DEFERRED** by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); not blocking.
- **Missing decision:** the secret and configuration names the relay (noema#48) and the hostility proxy (noema#51) need in `.env.example`, including the pull token the relay derives and the proxy's bench credential and number-map key. Both read their secrets from mounted files today, so the CI check that every workflow secret is listed has nothing to catch yet.
- **Why it matters:** a name that is not listed will not be found by the secret-name check when a workflow starts to use it.
- **Minimum safe default (meanwhile):** file-mounted secrets only; no names invented here.
- **What would change it:** the two services naming their variables in a pull request that adds them to `.env.example`.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before either service gets a workflow secret
- **Source:** noema#48, noema#51; AGENT-14, REQ-SEC-007.
<a id="od-p-67"></a>
### OD-P-67: Whether Tushe supplies the webhook signing secret

- **Status:** [CLOSED] · NON-CANONICAL · closed by [DEC-2026-11-16-tushe-addendum-od-p-67](decisions/DEC-2026-11-16-tushe-addendum-od-p-67.md) §2 (takes effect when that record is approved and merged): Tushe's addendum of 15 Nov 2026 (section 6) says the webhook endpoint and its signing-secret rotation are self-serve for Noema; ruling A240 has the Founder register and rotate it, with the value in the bench Environment only. Asked of Tushe by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)).
- **Missing decision:** whether Tushe gives Noema the signing secret for its webhooks, or Noema generates it and gives it to Tushe. The relay generates one into a named volume and says the secret Tushe was given can be written there instead (noema#48).
- **Why it matters:** the secret decides who can forge a delivery, and the vendor register (docs/vendors/README.md) has to name its owner.
- **Minimum safe default (meanwhile):** the relay-generated secret, synthetic, local only.
- **What would change it:** Tushe's written answer in `docs/poc/tushe/responses/`.
- **Owner:** Founder
- **Deadline:** before the first Tushe webhook is received
- **Source:** noema#48; DEC-2026-10-16 E6; PERD REQ-API-008.
<a id="od-p-68"></a>
### OD-P-68: Automating vendored-copy drift (proposal, not built)

- **Status:** [OPEN] · NON-CANONICAL · **DEFERRED** by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); not blocking.
- **Missing decision:** how a docs change that touches vendored text becomes a matching `noema` re-point pull request without a person having to notice. Today `noema` keeps five copies (`AGENTS.md`, `CLAUDE.md`, `contracts/state-registry.md`, the PERD §32.2 and §28.2 extracts) and a daily workflow (`docs-drift`) turns red when they differ from docs `main`. Each time, a person runs `tools/vendor/repoint_docs.py` and opens a pull request (noema#39, noema#55, noema#56). No PERD requirement governs this drift (PERD §64.2 says only that `AGENTS.md` and `CLAUDE.md` are copied from docs and state the commit; §64.1 covers `/contracts` only).
- **Why it matters:** the guard goes red after almost every docs merge, a red check that is expected stops being noticed, and the copies are read by CI (the state-machine test and the event-type drift check).
- **Proposal (smallest, no new access):** extend the existing `docs-drift` workflow in `noema`. It already has read access to docs through `DOCS_READ_TOKEN`. When `repoint_docs.py --check --ignore-commit` finds drift, the same job runs `repoint_docs.py` on a fresh branch `chore/repoint-docs-<docs sha7>` off `main`, commits only the files the script owns, and opens one pull request titled "GOV-22: re-point vendored docs copies to docs <sha7>", using `noema`'s own `GITHUB_TOKEN` (`contents: write`, `pull-requests: write`). It never pushes to `main`, never merges, and never edits a branch it did not create; if docs moves again it opens a new branch and closes the superseded pull request with a comment. Its pull request needs the same review as any other (one approval from the founder who did not open it; the bot is not a founder). The text of the docs files is data: the job runs only `noema`'s own script. The schedule is the cron it has today; a docs-side trigger would need write access from docs to `noema`, which is a new credential and is not proposed.
- **What the Founders must decide:** (1) turn on "Allow GitHub Actions to create and approve pull requests" for `noema` (a repository setting; approval stays off); (2) accept that a pull request opened with `GITHUB_TOKEN` does not start the other workflows, so its checks have to be started by a person pushing a commit or closing and reopening it (the alternative is a token or GitHub App, which is credential issuance and is not proposed); (3) whether a PERD requirement should say that vendored copies are checked against docs `main` daily and re-pointed by pull request (none exists today, and none is invented here). **Answer to (3):** REQ-OPS-005 (PERD v1.15, DEC-2026-10-23) now requires a matching re-point in the same change set and a drift check that fails when a copy differs; the automation proposed here stays open.
- **Tests it would need before it is built:** the existing `tools/vendor` tests; a workflow test that drift opens exactly one branch and one pull request and that no drift opens none; a canary that the job refuses to run on a fork or with a write token on any path other than the PR step; `check_pins` for any new action.
- **Minimum safe default (meanwhile):** the manual procedure of noema#56 (re-point, run `repoint_docs.py --check --ignore-commit`, require exit 0 immediately before merge).
- **What would change it:** the Founders preferring a docs-side trigger (and issuing the credential for it), or preferring to keep drift manual.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** none; before the next PERD version that adds a vendored section
- **Source:** noema#39, noema#55, noema#56; `.github/workflows/docs-drift.yml`; PERD §64.1, §64.2.
<a id="od-p-69"></a>
### OD-P-69: The format of `counterparty_display` in the candidate response (PROPOSAL)

- **Status:** [OPEN] · NON-CANONICAL · **DEFERRED** by the Founders (Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); not blocking.
- **Missing decision:** what `counterparty_display` carries. PERD REQ-CTX-006 says "counterparty_display (masked)" and "No unmasked names". The recipient matcher (REQ-AMB-003, D5) is deterministic code in the model service that matches name tokens, aliases, transliterations, phonetic keys and initials. Session D reports that if core masks with asterisks, matching has nothing to work on (noema#43, `docs/sessions/2026-10-21-1211-T5-T6.3.md`). The contract (`candidates-response.v1.json`, noema#42) today only forbids a run of five or more digits.
- **Why it matters:** the Recipient feature carries a weight of 0.25 in the ranking; with no readable token it scores 0 for every candidate, so identification depends on amount and time alone and more cases clarify or escalate.
- **Options:**
  - **A (proposed).** Core returns the principal's own beneficiary name, readable, in this principal-scoped internal response only. These are names the principal already knows (their own beneficiaries), and the response never leaves core and the model service. Conditions that make this safe: (1) the model service never puts `counterparty_display` in a prompt, a log or a trace (the harness masks before any provider call, and the redactor covers it); (2) every customer-facing string built from it (clarification options, explanations) is masked by the D4 label rules; (3) the shape lint and the contract keep every other field masked (account numbers to the last four). This amends the PERD's "no unmasked names" for this one internal API, so it needs a new PERD version.
  - **B.** Core returns precomputed match keys beside a masked display name (for example case-folded and transliteration-folded tokens, and initials). The matcher then matches keys only. It cannot use the nickname and variant lexicons or phonetic keys unless core carries the same lexicons, which duplicates the matcher data in core and breaks "never hard-coded".
  - **C.** Keep asterisk masking and accept that the Recipient feature scores 0.
- **Minimum safe default (meanwhile):** the contract as merged (masked display, no run of five digits); the matcher scores the Recipient feature 0 on a masked token.
- **What would change it:** the Founders choosing A or B, with a PERD amendment for A.
- **Owner:** Founder and Technical Co-Founder
- **Deadline:** before the first resolution benchmark run
- **Source:** noema#42, noema#43; PERD REQ-CTX-006, REQ-AMB-003, REQ-CTX-007; SoT §43 masking rules.
<a id="od-p-70"></a>
### OD-P-70: Certificates and the pack mount in the Compose setup (DEFAULT, WAITING FOR THE FOUNDER'S "YES")

- **Status:** [DECIDED] · NON-CANONICAL · the default is adopted: an internal certificate authority created by the Compose setup (Founders, Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** where the mTLS certificates between the two services come from in the local Compose setup (PERD §36.1, §65.1; INV-29), and how the pack directory reaches the core.
- **Why it matters:** the services need certificates to start with mTLS, and a pack must reach the core as data that nothing can change at run time (SoT §51: packs are data).
- **Default (smallest safe):** (1) an internal certificate authority that the Compose setup creates itself on first start; it issues the service certificates, and no certificate or key is committed; (2) synthetic data only; the authority and its certificates are labelled synthetic and are valid for the local setup only; (3) the pack directory is mounted into the core read-only.
- **What would change it:** a partner or Founder requiring an external authority or a managed secret store (OQ-09), or a need for the core to write to the pack directory (none is known).
- **Not covered:** issuing or storing any real credential. That stays with the Founder.
- **Owner:** Founder
- **Deadline:** before the first Compose profile that starts both services with mTLS
- **Source:** PERD §36.1, §65.1; INV-29; SoT §51; DEC-2026-10-21 compose-topology.

<a id="od-p-71"></a>
### OD-P-71: Who is alerted, and how, when a receipt signature fails (PLACEHOLDERS; DEFERRED to pre-production)

- **Status:** [OPEN] · **DEFERRED to pre-production** (Founders' decision, 29 Oct 2026) · NON-CANONICAL · no default is proposed for the recipient or the channel; nothing is built from this entry. **Development phase: no alert email and no recipient; a failed receipt signature is logged and flagged (the `SECURITY_EVENT` is recorded and DEBT-02 stays open).** The requirement for a human alert stays in place and is not met
- **Missing decision:** (a) the designated recipient (a role title) and the delivery channel of the operational alert; (b) the separate operator channel that does not depend on the database, used when the `SECURITY_EVENT` cannot be written or an alert cannot be delivered; (c) what happens if the operator channel itself fails; (d) how often a repeating fault may alert; (e) whether the alert reuses `ops_alert` and `OPS_ALERT_RAISED` (PERD §38.2, §32.2) or is a separate path; (f) how the core reaches an outbound operator channel (INV-29, PERD §65.1).
- **Why it matters:** the Founders require that a human is alerted when a receipt signature fails (29 Oct 2026). Without a recipient and a channel the requirement cannot be met, and a `SECURITY_EVENT` record or a log line is not an alert.
- **Default (smallest safe):** none proposed. Session A does not invent a recipient or a channel (AGENT-02). Until it is decided, the failure is fail-closed and recorded, and DEBT-02 stays open.
- **What would change it:** a Founder decision; a channel that needs a new dependency or egress (AGENT-14).
- **Not covered:** implementing the alert path.
- **Owner:** Founder (the choice); EL (Engineering Leader: the PERD text); SR (Security Reviewer: the rule and its fixture)
- **Deadline:** before production (deferred to pre-production; no development-phase date)
- **Source:** [DEC-2026-10-29-receipt-signature-alert](decisions/DEC-2026-10-29-receipt-signature-alert.md); PERD REQ-SEC-005, §44.1; DEBT-02.

### OD-P-72: Adopt pgsodium for in-database Ed25519 verification (AGENT-14; PROPOSED, conditional on the W2 spike)

- **Status:** [OPEN] · NON-CANONICAL · proposed by GOV-28 (W1). Approved by [DEC-2026-11-06-architect-rulings](decisions/DEC-2026-11-06-architect-rulings.md) A2, conditional on the independent validation of the 66 of 66 spike by Core Engineer 2 (A16); it closes when C2's result is posted on docs#117 and the record is merged. Nothing is built from this entry before then.
- **Missing decision:** whether pgsodium v3.1.11 (commit `a8b8a2739bab1f7a07445b1c911e2bd1abf67784`), built from source into Noema's own PostgreSQL 17.11 image with a checksum-verified libsodium, may be added as a dependency, using only `crypto_sign_verify_detached` behind a migration-owned wrapper.
- **Why it matters:** DEBT-01 (Tier 0) and REQ-AUD-006 need the database to refuse a receipt or Record event whose Ed25519 signature does not verify; PostgreSQL has no Ed25519 verifier of its own.
- **Default (smallest safe):** do not adopt until the Founders approve. The W2 spike passed T1 to T6 in CI on `postgres:17.11-alpine` (58 of 58, 1 Nov 2026), with one bootstrap step: pgsodium's event trigger is disabled and guarded against re-enabling (DEC-2026-11-01-receipt-and-record-signing D10a). If the Founders refuse, Option C applies (§11 of that record).
- **What would change it:** a failed check on a later run; a security issue in pgsodium or libsodium; an upstream deprecation; an extension upgrade that re-enables its event trigger; a PostgreSQL major that pgsodium does not support.
- **Not covered:** key custody (DEC-2026-11-01 §3); the write-once anchor store (SEC-14).
- **Owner:** Founders (the approval); SR (the evaluation and the spike, which SR built); C2 (the independent validation of the spike, A16); C1 (the image, EXE-08); EL (the design).
- **Deadline:** with GOV-28, Wed 4 Nov 2026.
- **Source:** [DEC-2026-11-01-receipt-and-record-signing](decisions/DEC-2026-11-01-receipt-and-record-signing.md) §5; the W2 evaluation (SEC-12, docs#78, not yet merged) and its spike (run 41314576829, noema#106); DEBT-01; PERD REQ-AUD-006.

### OD-P-73: Record keys for `model-service` and the adapter emitters (PROPOSAL)

- **Status:** [DECIDED] · NON-CANONICAL · the default is adopted, with the Founder decision D6 (Block D): the model service holds no Record key and core-edge signs and appends the events for it ([DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** record-event v3 lists `model-service` and seven adapter identities (`mock-ledger`, `mock-switch`, `mock-destination`, `mock-customer`, `mock-policy`, `mock-case`, `mock-clock`) as `RUNTIME` emitters (`services/core/record/chain/actors.json`). REQ-AUD-006 makes each emitter sign with its own key. The model service cannot hold a core credential (INV-29) and does not append to the Record itself, and the adapters run inside the core, so for each of them it is undecided who holds the key, or whether the core appends such events under its own identity instead.
- **Why it matters:** a key held by the core for another identity would let the core sign as that identity, which defeats the point of per-emitter keys.
- **Default (smallest safe):** register no key for these eight identities in the POC. The database then refuses any event that claims them (fail closed). No code appends as them today (checked 1 Nov 2026: only `core-execution` appends).
- **What would change it:** a slice that needs an event attributed to the model service or an adapter; a decision on the Mode 2 signed-proposal design (DEC-2026-10-31 D29).
- **Not covered:** the model service's own outputs, which cross the schema gate as untrusted data (INV-02).
- **Owner:** EL (the proposal); Founders (the decision).
- **Deadline:** before the first event attributed to one of these identities.
- **Source:** [DEC-2026-11-01-receipt-and-record-signing](decisions/DEC-2026-11-01-receipt-and-record-signing.md) §3 D2; PERD §32.1, REQ-AUD-006; INV-29.

### OD-P-74: Claim names and roles of the synthetic IdP's session token (built in noema#156)

- **Status:** [CLOSED] · adopted as canonical by [DEC-2026-11-05-architect-rulings](decisions/DEC-2026-11-05-architect-rulings.md) D2 (takes effect when that record is approved and merged). The NON-CANONICAL label is removed.
- **Answer (DEC-2026-11-05 D7, ruling A1 of 6 Nov 2026, which supersedes D2's claim and role lists):** the identity contract is D7's, not the default below. Issuer `noema-poc-idp`, exact match; claims `sub`, `aud`, `exp`, `iat`, `iss`, `tenant_id`, `roles`; `roles` holds exactly one of `customer`, `ops`, `approver`, `audit`; ES256 only; 15 minute ceiling; deny by default; and the Security Reviewer's nine gaps as requirements. The default below is kept as the history of what noema#156 first built: it has no `iss`, a list of roles and `operator` instead of `ops`, and implementers follow D7.
- **Missing decision:** which claims a session token carries and what they are called, and which roles exist. PERD REQ-SEC-001 says the synthetic IdP issues ES256 JWTs "for synthetic customers, operators and approvers, with roles" and that the core validates "signature, expiry, audience and tenant", and that `sub` is the only principal source. No document names the tenant claim, the roles claim, their values, or the issuer and key identification.
- **Why it matters:** the claim mapping decides which signed data becomes the principal, the tenant and the authority (INV-12). The synthetic IdP, the core's verifier and the benchmark's session provider must agree on it.
- **Default (smallest safe):** the claims `sub` (the principal), `aud` (one string, the core's audience), `exp` and `iat` (required, integer seconds; the token's lifetime, `exp - iat`, may not exceed a configured maximum, PERD REQ-API-004 [REC] 15 minutes), `tenant_id` (must be one of the tenants the deployment serves) and `roles` (a non-empty list of `customer`, `operator` or `approver`; any other value rejects the token); a JWT header `alg` of `ES256` only and a `kid` that names a configured P-256 public key. Every failure is one rejection. Built in `services/core/edge/session` (noema#156).
- **What would change it:** the enterprise IdP contract or the benchmark's IdP naming them differently; a need for more roles (for example audit or ops, REQ-API-004 route roles); a second tenant claim for operators who span tenants.
- **Not covered:** per-session rate limits, `request_id` deduplication, the 5-minute freshness for sensitive operations, route-level role checks (EDG-01's later slices); key rotation of the IdP.
- **Owner:** EL (the default and the verifier); IL (the synthetic IdP); Architect (the decision).
- **Deadline:** before the synthetic IdP issuer (EDG-01 slice 2) is merged.
- **Source:** PERD REQ-SEC-001, REQ-API-004, REQ-API-002; INV-12; `services/core/edge/session` and `status/EDG-01.md` in `noema`.

### OD-P-75: Status of a well-formed value from a corroborating-only source (DEFAULT, EVD-01)

- **Status:** [DECIDED] · NON-CANONICAL · UNKNOWN: a well-formed value from a corroborating-only source is UNKNOWN (Founders, Block E, E4, 7 Nov 2026; [DEC-2026-11-07-founder-decisions-block-e](decisions/DEC-2026-11-07-founder-decisions-block-e.md)); counts once that record merges.
- **Missing decision:** the FactStatus of a well-formed value, within its freshness limit, read from a source whose authority for the fact is CORROBORATING (not AUTHORITATIVE). PERD v1.20 §21.1 says KNOWN needs an authoritative source and does not say what a corroborating one gives.
- **Why it matters:** KNOWN is the status Trust and Outcome act on (INV-10, INV-19); giving it to a corroborating source would let a weaker source authorise an action.
- **Default (smallest safe):** UNKNOWN. Corroboration never confers KNOWN on its own; a later reconciliation rule (RES tasks) may raise it to INFERRED. Built in `AssignStatus` (noema#160).
- **What would change it:** a fixture or a design-partner source whose only available source is corroborating; a reconciliation rule that defines INFERRED from corroborating items.
- **Not covered:** the `AUTHORITATIVE_NEGATIVE` exception (task EVD-01 slice 1b, gated on a contract change request); INFERRED, AMBIGUOUS and CONTRADICTORY.
- **Owner:** EL (the default); Architect (the decision).
- **Deadline:** before EVD-01 slice 2 is merged.
- **Source:** PERD v1.20 §21.1, REQ-CTX-002; INV-10, INV-19; [`task-cards/EVD-01.md`](poc/execution/task-cards/EVD-01.md) D1.

### OD-P-76: Caddy as the webhook relay's TLS terminator (AGENT-14)

- **Status:** [DECIDED] · ruled by [DEC-2026-11-06-architect-rulings](decisions/DEC-2026-11-06-architect-rulings.md) A11: the relay's TLS terminator is Caddy (HTTP-01, ports 80 and 443, no DNS plugin). That record is merged, so Caddy is approved (housekeeping, 9 Nov 2026). The entry exists because AGENT-14 asks for an [OPEN] entry before a new component.
- **Answer (A11):** Caddy terminates TLS for the relay, with HTTP-01 on ports 80 and 443 and no DNS plugin.
- **Missing decision:** which component terminates TLS for the webhook relay (ENV-13), and how it gets its certificate.
- **Why it matters:** it is a new component on the path of inbound events; the relay's public address and certificates must stay out of the repository (AGENTS §10).
- **Default (smallest safe):** none was proposed; the Architect ruled.
- **What would change it:** a hosting choice that cannot answer HTTP-01 on port 80, or a need for a wildcard certificate (which needs a DNS plugin).
- **Not covered:** the Compose and relay changes (their own pull requests); the relay's hostname, which lives only in a GitHub Environment variable.
- **Owner:** IL (ENV-13); Architect (the decision).
- **Deadline:** before the relay is deployed.
- **Source:** DEC-2026-11-06 A11; ENV-13; AGENT-14.
### OD-P-77: Operations Model parameters for the benchmark IMPACT layer (AWAITING THE FOUNDER'S VALUES)

- **Status:** [OPEN] · NON-CANONICAL · no value has been chosen. Named by [DEC-2026-11-07-benchmark-suite-definition-v1](decisions/DEC-2026-11-07-benchmark-suite-definition-v1.md) (ruling A26, Proposed).
- **Missing decision:** the values of the published Operations Model that turns RESOLVE and RESIST results into the modelled IMPACT figures: human minutes per escalation type, the loaded cost per human minute, the SLA thresholds and the arrival rate. The model is identical for all arms, with M0 as the manual baseline, and every IMPACT figure is labelled "modelled" and reported across a sensitivity range.
- **Why it matters:** IMPACT figures (resolution time, human investigation minutes, human touches, escalation rate, first-contact resolution, SLA exposure, cost per exception, backlog, customer effort) are not computable without these values, and an invented value would turn a modelled figure into a claim (AGENT-18; SoT §0.6; SoT §38.6: partner variables are supplied by the partner, never invented).
- **Default (smallest safe):** none. No IMPACT figure is computed or reported until the Founder supplies the values, each with its source. RESOLVE and RESIST are reported without it.
- **What would change it:** a design partner who supplies measured values (SoT §38.6); a sensitivity range wide enough that no single value matters.
- **Not covered:** the choice of the sensitivity range; the REV sampling rule; the arms' configuration.
- **Owner:** Founder (the values and their sources); Benchmark Owner (the published model document).
- **Deadline:** before IMPACT is computed, and in any case published before the hidden run whose results feed it (A26 rule: pre-registered before any hidden case runs).
- **Source:** DEC-2026-11-07 (A26), "IMPACT"; SoT §38.5, §38.6.

### OD-P-79: Control-plane route names and credential classes (PROPOSAL, Founder decision D14)

- **Status:** [OPEN] · NON-CANONICAL · proposal by EL from PERD §39.4; the Security Reviewer accepted the route names and the `:set` / `:clear` split (7 Nov 2026) and asked for the credential classes below; the Architect rules on them. The credential classes are ruled in A54 (DEC-2026-11-08-rulings-a41-onward, with docs#140). Rows 10 and 11 of the matrix (`GET /v1/reconstructions/{correlation_id}` and `GET /v1/record/verify?tenant_id=`) stay audit-only (ruling A110, docs#141); the widening in finding 3 is not adopted. Not authority for building until accepted and committed.
- **Missing decision:** (1) the exact route names of the control plane, and (2) the credential classes that call them. PERD §39.4 lists the routes, but with one route for the kill switch, `POST /v1/admin/tenants/{id}/kill-switch` with `{enabled: bool, reason}`. Founder decision D5 says the verifier may set a tenant's kill switch and only a person clears it; one route with an `enabled` field cannot carry that difference.
- **Credential classes (answer to the Security Reviewer's finding 1).** The session roles stay as ruling A1 has them: `customer`, `ops`, `approver`, `audit` (a fifth session role would reopen A1 and D7). The control plane is a **separate listener and credential**, as §39.1 already says ("a separate admin credential, MFA-protected in shared environments"). Two classes:
  - **C-ADMIN**: the control-plane administrator credential, held by a person (MFA in shared environments). In a non-shared development environment there is no MFA, so C-ADMIN is one credential there and must not be read as MFA-protected.
  - **C-VERIFY**: a service credential for the verification identity, mTLS with a service identity (REQ-SEC-002), held by the verification job. It is **not** a person and **not** a session role.

  Until both classes exist, a person-only `:clear` is a sentence, not a control. What enforces D5 today is the database rule on `record_verify` (noema#190 has the failing-first test), and **no control-plane route is built** (this is the reason, not only that this entry is pending).
- **Routes (changes to §39.4 are marked):**

  | Route | Credential class | Effect |
  |---|---|---|
  | `POST /v1/admin/tenants/{tenant_id}/kill-switch:set` body `{reason}` **(replaces the single kill-switch route)** | C-ADMIN or C-VERIFY (C-VERIFY may call `:set` for any tenant, by design: the verifier is cross-tenant; the matrix tests that it can call nothing else) | switch on; `KILL_SWITCH_CHANGED` with the caller as actor; idempotent |
  | `POST /v1/admin/tenants/{tenant_id}/kill-switch:clear` body `{reason}` **(replaces the single kill-switch route)** | C-ADMIN only | switch off; C-VERIFY gets 403 `PERMISSION_DENIED`; `KILL_SWITCH_CHANGED` with the person as actor, and a `SECURITY_EVENT` in the same transaction (A71, docs#140); **its kind is not in the PERD §32.2 list yet: adding it (proposed name `KILL_SWITCH_CLEARED`) is a versioned PERD change plus a `record-event` contract change under AGENT-15, to be ruled and done before any route writes it** |
  | `GET /v1/admin/tenants/{tenant_id}/kill-switch` **(new route)** | C-ADMIN only | the state, the last change and who made it; ops and audit see the effect through `GET /v1/ops/alerts` |

  Every other route of §39.4 stands as written, **with the callers of §39.4 unchanged**: `GET /v1/reconstructions/{correlation_id}` and `GET /v1/record/verify?tenant_id=` are audit; the panel and the alerts are ops and audit or ops as §39.4 says. `POST /v1/admin/policies/{policy_id}/versions` and `.../versions/{v}/publish` (the segment form: ruling A183 amends D14's `{v}:publish`, [DEC-2026-11-13-d14-route-spelling](decisions/DEC-2026-11-13-d14-route-spelling.md)), `POST /v1/admin/packs:load` and `PUT /v1/admin/tenants/{id}/callback` take C-ADMIN. For publication, a version that is not higher than the active one (the same, or a downgrade) answers 409; the catalogue then needs a code for it (`POLICY_VERSION_NOT_NEWER`), which is a change to `errors.v1.json` under AGENT-15, not made here.
- **Two notes for SEC-04 (Security Reviewer's finding 4):**
  - **Key rotation has no route.** Public keys are registered by the migrator at deploy (`key_register`, an operator step, DEC-2026-11-01 D3a); the callback route rotates a callback secret only. A test of the absence is meaningful: no route matches rotate or key, and the runtime roles cannot execute `key_register`, `key_retire` or `key_revoke`.
  - **`GET /v1/record/verify?tenant_id=`** takes a tenant in the query. For `ops` and `audit` it must equal the token's tenant or the call is refused with the not-found shape (INV-12, D7 item 7).
- **Why it matters:** D5 is a safety property of who can undo a stop. If the route and the credential class cannot express it, the check moves into code that reads a body field.
- **Default (smallest safe):** the routes and the two credential classes above. Until accepted and built, no control-plane route exists (TRU-08 slice 1 builds none). The not-found shape is returned to a caller who may not know a route; `403 PERMISSION_DENIED` only for C-VERIFY on `:clear`; `POST /v1/benchmark/runs` is not served by the runtime core in any runtime profile.
- **What would change it:** the Architect defining the credential classes differently (for example a second human credential for `:set`), or a finding that C-VERIFY and C-ADMIN cannot be told apart at the listener in the POC.
- **Not covered:** authentication of the admin credential (OQ-09); the route that reads policy versions (needed once the control plane is built).
- **Owner:** EL (the proposal); SR (accepts, SEC-04); Architect (the credential-class ruling); Founders (D5, D14).
- **Deadline:** before the control plane is built (TRU-08 slice 2).
- **Source:** PERD v1.20 §39.1, §39.4; Founder decisions D5, D7, D14; DEC-2026-11-01 D3a; ruling A1, A20; REQ-SEC-001, REQ-SEC-002.
### OD-P-78: Pack data and evidence for delegate, joint-account and approver-threshold authority (R7), and what R8 repeats (DEFAULT, PCK)

- **Status:** [OPEN] · NON-CANONICAL · default in use. Founder decision D13 (7 Nov 2026) confirms the default ("if authority depends on facts the pack lacks, escalate and do not act"); the entry closes when D13 is committed to a decision record.
- **Missing decision:** the benchmark suite (A26, family R7) needs cases for a delegate acting for an owner, a joint account, and an approver whose authority depends on an amount threshold. The pack can say who may act on a resource only with what the contracts define: `authority.principal_must_own` (slot names), `authority.roles_allowed` (the four roles of ruling A1) and `approvals` (role names). It has no evidence entity for an account holder, a joint holder or a delegation, and no source that serves one (DEBT-12: account state has no source), and no threshold on an approver. A rule over such facts cannot be type-checked against evidence that does not exist, so the pack side cannot honestly be written yet.
- **Why it matters:** building these as pack data without a source would give the cases something to run that no component can answer; Trust would either guess or fail open on a fact it cannot read (INV-10).
- **Default (smallest safe):** in the POC, authority that depends on a delegation, a joint holder or an approver amount threshold is not decided autonomously: the request is ESCALATE with a reason that says which fact is missing. That reason is for the case and the operator only. The customer-facing message keeps the not-found shape for a non-owner (as in the X3 cases) and never reveals that a joint holder, a delegate or an approver threshold exists on someone else's account, so the R7 cases and the explanation templates cannot leak it (Security Reviewer, 7 Nov 2026). The cases for R7 then test that Noema escalates and does not act, and that the owner-only case (`principal_must_own`) still works. R8 (the same decision on five repeats) is not pack data: it is the determinism property of TRU-09 (replay, 10⁴ replays, 0 mismatches), and the benchmark checks it by running a case five times.
- **What would change it:** a design partner or the Tushe environment supplying an account-holder, delegation and mandate-limit source; a ruling that the evidence descriptors gain those entities (a contract change under AGENT-15, with an evidence source and a stand-in served by ENV-04).
- **Not covered:** money movement of any size (prohibited, BD-08); approver amount thresholds on a write the POC does not have.
- **Owner:** EL (the default); Architect (the decision); BO (the cases).
- **Deadline:** before BO fixes the R7 cases for the first visible set.
- **Source:** ruling A26 (benchmark suite v1, R7 and R8); PERD v1.20 §15, §23.4; REQ-TRU-009 (determinism, TRU-09); DEBT-12.

### OD-P-80: AGENT-14 entry, the arm-facing tool facade (APPROVED by the Architect, relayed by IL)

- **Status:** [DECIDED] · NON-CANONICAL · approved under AGENT-14 by the Architect (R1 as relayed by the Integration Lead, noema#363; ruling A87 in [DEC-2026-11-08-rulings-a41-onward](decisions/DEC-2026-11-08-rulings-a41-onward.md)); counts once that record merges and the Founders confirm A87.
- **Missing decision:** approval to add a tool facade that exposes the stand-in enterprise's tools to the comparison arms.
- **Why it matters:** AGENT-14 (no new dependency, service or tool without an approved entry); a facade is a new service on the benchmark path.
- **Default (smallest safe):** Go standard library only; `ci` and `bench` profiles only; no money-moving tool; no provider credentials; REST first and MCP second.
- **What would change it:** a need for a non-standard-library dependency, a profile other than `ci` and `bench`, or any tool that moves money.
- **Not covered:** the facade's design (IL's PRs noema#189, #252, #256, #361).
- **Owner:** IL (the build); Architect (the approval).
- **Deadline:** before the facade is merged.
- **Source:** noema#363; AGENT-14.

### OD-P-81: What a pack tool's input schema may contain (DECIDED with the Integration Lead, noema#362)

- **Status:** [DECIDED] · NON-CANONICAL · proposed by EL (pack owner) under AGENT-02 on noema#362; the Integration Lead (facade owner) answered yes on 10 Nov 2026, as the Architect sync of 10 Nov asked. Built in noema#417.
- **Missing decision:** which fields a published tool schema (`packs/schemas/fin/*.v1.json`, the capabilities' `input_schema`) holds. The stand-in's request bodies mix fields a caller supplies with fields Noema fills from the session or from Trust and Execution.
- **Why it matters:** the comparison arms are offered the same tools as Noema. An arm must never be asked for an identity (INV-12) or for a value Trust or Execution derives, or the tool surface itself becomes a way to forge one.
- **Default (smallest safe):** only the fields a caller supplies, with `additionalProperties: false`. Never the tenant, the principal, the epoch, `created_by_intent`, version tokens, idempotency keys or payload hashes. Reads take only lookup keys (transaction, account, time window). No schema exists for a prohibited capability (BD-08, REQ-CAP-002).
- **What would change it:** a facade or arm that cannot work without a derived field passed through by the caller; then the field is added by a pack change with its reason.
- **Not covered:** the field list of each tool (in noema#417; `lookup_transaction_history` is the least-sourced one).
- **Owner:** EL (pack data); IL (the facade).
- **Deadline:** before the facade's schema conformance test is enabled.
- **Source:** noema#362, noema#417; INV-12; AGENT-02.

### OD-P-82: Per-tenant reader pools for the SSE events route (DEFAULT, EL; ruling A170)

- **Status:** [OPEN] · NON-CANONICAL · default in use (ruling A170, [DEC-2026-11-12-architect-rulings-a166-a170](decisions/DEC-2026-11-12-architect-rulings-a166-a170.md); counts once that record is merged).
- **Missing decision:** how the SSE events route (`GET /v1/conversations/{conversation_ref}/events`, PERD §39.2) reads the Record and the investigation state per tenant.
- **Why it matters:** tenant isolation is enforced in the database (REQ-SEC-004); a shared reader credential would let the route read across tenants.
- **Default (smallest safe, ruling A170):** a file-mounted, read-only DSN per tenant. The route stays unmounted until it is configured.
- **What would change it:** (1) a decision to serve the Record and the investigation state from a pooled reader that is not per-tenant, which would need row-level security to carry the isolation alone (today the tenant is bound by the login, DEBT-04 option A); (2) the platform configuration (OPS-01) defining the secret layout for per-tenant logins differently from one read-only DSN file per tenant (noema#181 already mounts per-tenant secrets for the emitters); (3) the Record export (REC-09) replacing a live read for the events route. Evidence that would invalidate the default: a tenant whose reader login cannot read its own chain, or a login that can read another tenant's. (Stated by EL on docs#159.)
- **Not covered:** the route's event contents (PERD §39.2). The same reader pools serve the reconstruction route (`GET /v1/reconstructions/{correlation_id}`, noema#486), so this entry covers both routes.
- **Owner:** EL (files and builds); Architect (the decision).
- **Deadline:** before the SSE events route or the reconstruction route is mounted in a deployed profile (both stay unmounted until the DSN files are set).
- **Source:** ruling A170; PERD §39.2; REQ-API-001; REQ-SEC-004.

### OD-P-83: The link format of a fix PR's regression case (MEM-02; CLOSED; the workflow wiring merged in noema#673)

- **Status:** [CLOSED] · NON-CANONICAL · the format was accepted as ruling A156 (12 Nov 2026), committed in `docs/decisions/DEC-2026-11-12-architect-rulings-a148-a160.md` (docs#157, merged). It was held [OPEN] for one reason: the workflow wiring. **noema#673 (MEM-02, "wire the regression-link check into CI (labels, live description, ruling A156)") merged on 18 Nov 2026**, and `.github/workflows/regression-link.yml` on `main` sets `REGRESSION_ALLOW_TEST_FILE=1`, so the A156 alternative is on. Closed by the Steward at the Benchmark Owner's request (19 Nov 2026), as the entry said it would be. Proposed by the Benchmark Owner under AGENT-02 on noema#452; the number OD-P-83 is the Steward's allocation under ruling A171.
- **Missing decision:** the format of the regression link that REQ-MEM-002 requires on a fix PR. The requirement says a fix links the regression case it adds; it fixes no format.
- **Why it matters:** the check that enforces the link (`tools/ci/check_regression_link.py`, noema#452) needs a rule it can test, and the Definition of Done (AGENTS.md section 8: regression case committed before the fix merges) needs a place a reviewer can find the case.
- **Default (smallest safe):** a fix PR carries one line `Regression case: <ref>` in its body, outside any code block or quote. A fix PR is one **labelled `fix`** (the acceptance criterion of REQ-MEM-002, PERD v1.22 section on REQ-MEM-002: "CI SHALL block a PR labelled `fix` without a linked new case ID"); a head branch `fix/...` or a title that says fix also counts, as a supplement that never replaces the label. `<ref>` is a benchmark case ID (`BEN-<CATEGORY>-<4 digits>`), which is what REQ-MEM-002 requires ("a named, permanent benchmark case", "a linked new case ID"). "none", "n/a", "TBD" and empty are refused. The check follows CommonMark for fenced code.
- **The alternative (ruling A156, committed in docs#157):** a test file that the PR itself changes (`test_*.py`, `*_test.py`, `*_test.go`, `*.test.ts[x]`, optionally `::name`). The check accepts it only when `REGRESSION_ALLOW_TEST_FILE=1`, which the workflow wiring PR sets; it is off by default, so no PR passes on a test file alone until that PR turns the alternative on as A156 provides.
- **What would change it:** a regression-case registry (a directory of permanent cases) that the check should resolve IDs against instead of the shape alone (the check sees an ID's shape, not whether the case is new or permanent; the reviewer reads that); or a requirement to prove the order of the commits (the PR's file list cannot show that the test came before the fix; the reviewer reads the commits).
- **Not covered:** wiring the check into a workflow, including passing the PR's labels (`PR_LABELS`) and enabling the A156 alternative (a separate PR after noema#452 merges, as ruling A156 says; `.github` needs a Founder's approval, AGENTS.md section 11); the order of commits; whether a case ID is new.
- **Owner:** Benchmark Owner (the entry and the check); Architect (the decision, A156); Founder (the workflow wiring).
- **Deadline:** before the workflow wiring PR.
- **Source:** ruling A156; noema#452; REQ-MEM-002, REQ-BEN-006; AGENT-02, AGENT-11, AGENT-23.

<a id="od-p-84"></a>
### OD-P-84: UI-01 frontend dependencies (AGENT-14; DECIDED by the Founder, 13 Nov 2026)

- **Status:** [CLOSED] · NON-CANONICAL · decided 13 November 2026 by [DEC-2026-11-13-ui-01-frontend-dependencies](decisions/DEC-2026-11-13-ui-01-frontend-dependencies.md) D1 to D6 (takes effect when that record is approved and merged).
- **Missing decision:** Approve the exact UI-01 runtime and test dependencies and versions under AGENT-14.
- **Why it matters:** The fixed stack calls for React and Playwright, but the UI manifest currently contains only TypeScript. UI-01 needs a React runtime, TypeScript declarations and browser tests; pinning avoids floating versions.
- **Decision:** `react` 19.3.1, `react-dom` 19.3.1, `@types/react` 19.3.0, `@types/react-dom` 19.3.0 and `@playwright/test` 1.64.1, exact-pinned, with the existing TypeScript 5.9.3. No other direct dependency. The record sets three conditions: exact pins and a committed lockfile, an `npm audit` result in the UI-01 pull request, and a stated way for CI to obtain the Playwright browsers.
- **What would invalidate it:** a Founder decision for different versions or tools, a security or compatibility issue, or evidence that a listed package is unnecessary.
- **Owner:** Founder decided; Steward records the decision.
- **Source:** UI-01, REQ-UI-001, AGENT-14; noema#502; proposed in docs#161.

### OD-P-85: Resume of a stranded run (DEFAULT, EL; ruling A168)

- **Status:** [OPEN] · NON-CANONICAL · default in use (ruling A168 and A172, [DEC-2026-11-12-architect-rulings-a166-a170](decisions/DEC-2026-11-12-architect-rulings-a166-a170.md) and [DEC-2026-11-12-architect-rulings-a171-a175](decisions/DEC-2026-11-12-architect-rulings-a171-a175.md); count once those records are merged). Filed by the Steward from EL's answer on noema#477, posted on docs#159.
- **Missing decision:** what happens to an input that is recorded but not processed. PERD 28.2 has no failure state or arrow for it, and re-running `Trust.Decide` would record a second decision.
- **Why it matters:** a stranded run that is retried must not record a second decision for the same input (INV-03 spirit: no action without a single, recorded decision; the Record is the proof, AGENT-21).
- **Default (smallest safe):** resume from the last recorded state, never close the run. The retry goes through `Start` (noema#490), as A168 rules. Resume itself waits for the `Trust.Decide` follow-up PR. **Ruling A186 (13 Nov) replaces A172's index specification:** `Decide` is a pure function of its inputs; the lookup key is the full deterministic tuple of tenant, `intent_id`, `intent_hash`, context snapshot and policy version; the same inputs return the stored decision and append nothing; a re-evaluation with new evidence has a new key, so WAIT and CLARIFY re-decisions stay legal. EL maps the key onto the real columns and stops and asks if it cannot be formed from existing columns. Migration 0027 stays reserved ([DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md), interim).
- **What would change it:** C1's check that `Trust.Decide` returns the existing decision for the same input and appends nothing; or a ruling that adds a failure state to PERD 28.2 (a PERD change, by a new version file).
- **Not covered:** the state machine itself (PERD 28.2); the follow-up PR's design.
- **Owner:** EL (the build); Architect (the decision); C1 (the check).
- **Deadline:** before the persistence slice is wired into the runner.
- **Source:** rulings A168, A172 and A186; noema#466, noema#477, noema#490; PERD 28.2.

### OD-P-86: The Intent Object's signature in the POC (OPEN, check against the SoT; ruling A177)

- **Status:** [OPEN] · NON-CANONICAL · filed by the Steward on the Architect's instruction (ruling A177, noema#484).
- **Missing decision:** whether the POC may leave the Intent Object's own `sig` field as an unsigned marker and treat the Record's signature on `INTENT_ADMITTED` (made by the REC-08 emitter signer) as the signature that counts. SoT §7 says the Intent Object is "signed by Understanding" and lists "schema and signature of the Intent Object" among Trust's checks. The model service never signs (INV-29), and no signing domain for Understanding exists.
- **Why it matters:** if the SoT reading stands, Trust has a check it cannot perform in the POC. If A177 stands, the SoT sentence and the build differ, and a reader of the SoT could expect a signature that is not there. AGENT-02 forbids inventing a signing domain.
- **Ruling A189 (13 Nov, interim):** Trust checks that the recomputed `intent_hash` equals the hash in the signed `INTENT_ADMITTED` event, read through the admission reader (tenant, principal and correlation bound). This differs from SoT §7 ("signed by Understanding"), so A177 stays interim. **The SoT edit goes into v1.13 as its own pull request, after the Intron change in v1.12.** Until then this entry stays open and G1 evidence says "signatures verified: no". (A189 calls this conflict "OD-P-85"; in the register it is OD-P-86, and OD-P-85 is the stranded-run resume.) [DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md).
- **Default (smallest safe):** A177 as ruled. The core computes `intent_hash` over canonical JSON. The Record signs `INTENT_ADMITTED`. The Intent Object's `sig` stays the unsigned marker. No new signing domain. The model-side gate stays on v1 until the v2 contract is live.
- **What would change it:** a ruling that Understanding signs (that needs a signing domain, a key outside the model service's reach, and a contract change under AGENT-15); or a SoT edit that moves the signature check from the Intent Object to the Record.
- **Not covered:** the v2 contract's shape; the content of noema#484 and #489.
- **Owner:** Architect (the decision); Founders (a SoT edit, if one is needed); EL and C1 (the build).
- **Deadline:** before the v2 intent contract goes live.
- **Source:** ruling A177 in [DEC-2026-11-12-architect-interim-a177-a178](decisions/DEC-2026-11-12-architect-interim-a177-a178.md); SoT §7, AGENT-02, INV-29.

### OD-P-87: The SoT edit for BD-16 and OD-04 when Intron becomes the sole speech provider (OPEN; ruling A179)

- **Status:** [OPEN] · NON-CANONICAL · filed by the Steward on the Architect's instruction (ruling A179, [DEC-2026-11-13-voice-provider-intron](decisions/DEC-2026-11-13-voice-provider-intron.md); counts once that record is merged).
- **Missing decision:** the Founders' authoring or approval of the SoT edit that A179 needs: BD-16 (SoT lines 101 and 729), §35.3 (1511), §37 "Provider runs" (1816), OD-04 (2381) and the §51 `/providers` layout (2575), with an Appendix D entry. The ruling names "SoT v1.7"; the SoT on `main` is v1.11 and Appendix D already lists v1.7, so the next version is v1.12 and the number needs confirming.
- **Why it matters:** the SoT outranks every record. BD-16 says "speech integrates at least Aethex AI, Indigenius and N-ATLAS"; A179 integrates only Intron. Until the SoT changes, the SoT text stands and no one builds against A179 (AGENT-20, AGENT-27).
- **Default (smallest safe):** the draft in [DEC-2026-11-13-voice-provider-intron-sot-draft](decisions/DEC-2026-11-13-voice-provider-intron-sot-draft.md), which edits nothing. The Steward does not edit the SoT. BD-16 is not reinterpreted.
- **What would change it:** the Founders reword the draft, or decide the SoT stays and A179 is withdrawn.
- **Not covered:** a second speech provider (OD-P-88); data terms (OD-P-89).
- **Owner:** Founders (the SoT edit); Architect (the ruling).
- **Deadline:** before any task that builds against A179 starts (VOI-01, VOI-04, VOI-10, BEN-23, UND-13 and PRE-04 as changed by CR-2026-11-13-A179-intron-voice-provider).
- **Source:** ruling A179; SoT BD-16, OD-04, §35.3, §37, §51; AGENTS §11 (the SoT is not edited in place).

### OD-P-88: Whether to add a second speech provider at pilot readiness (ADOPTED as written; ruling A179)

- **Status:** [DEFAULT] · NON-CANONICAL · **adopted as written** on the Architect's instruction of 13 Nov 2026 ([DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md), §2); filed by the Steward on the Architect's instruction (ruling A179). The default below is the rule in force **from the SoT edit that adopts A179 (v1.12)**; until then the committed SoT stands and only synthetic audio goes to any speech provider.
- **Missing decision:** whether the POC adds a second speech provider, decided by the Founder at pilot readiness.
- **Why it matters:** one provider is a single point of failure for voice; A179 accepts that for the POC because a failure degrades safely to text and replacing Intron needs no change to Trust, Execution, Outcome or the Record.
- **Default (smallest safe):** no second provider in the POC.
- **What would change it:** the POC evidence A179 names: the G5 voice gate result, the field report (VOI-14), the latency lab report (VOI-16), Intron's answer on capacity, the data-terms outcome (GOV-25) and the failure drills. The gate thresholds already in the pack and the plan decide; agents set none.
- **Not covered:** which provider a second one would be.
- **Owner:** Founder (the decision); Voice Engineer and Benchmark Owner (the evidence).
- **Deadline:** pilot readiness.
- **Source:** ruling A179; G5; VOI-14, VOI-16, GOV-25.

### OD-P-89: Intron's written data terms (CLOSED; decided by the Founder, 19 Nov 2026; replaces the rule of ruling A180)

- **Status:** [CLOSED] · NON-CANONICAL · **decided** by the Founder on 19 Nov 2026 ([DEC-2026-11-19-founder-intron-data-terms-a377-a379](decisions/DEC-2026-11-19-founder-intron-data-terms-a377-a379.md), A377 to A379; takes effect when that record is approved and merged). It replaces A180's "written terms before real audio", which this entry had adopted ([DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md), §2).
- **Missing decision (as raised):** the Founder's commit of Intron's data terms: retention, zero data retention, no training, sub-processors, hosting region, deletion timeline and incident notice.
- **Decision:** Intron's email of 18 Nov 2026 is accepted as the data terms for the POC (A377). A DPA is no longer a precondition for any work, including real-speaker audio; the DPA follows the commercial agreement (A377, A378). Counsel is not needed and blocks nothing (A378). Consent forms are no longer required for recordings of people outside the team; the Integrator account's retention is zero days (A379). The Founder holds Intron to its commitments in writing (A377).
- **What stays:** REQ-VOI-004 (raw audio never in the repository or CI artifacts, only in the bench Environment's private store, deleted per the plan); synthetic audio stays labelled; masking before any provider call (AGENTS §10).
- **Not covered:** any claim of regulatory compliance (SoT §50.2, AGENTS §10): the certifications below are Intron's own statements. The terms of any other provider (OD-P-88).
- **Owner:** Founder (decided); Steward records.
- **Source:** A377 to A379; the Founder's instruction of 19 Nov 2026; PERD R-18; VOI-05; GOV-25.
- **Intron's statements (its email of 13 Nov 2026, noted on the Founder's direction of 16 Nov, A241; its email of 18 Nov 2026 as A377 states it; they are Intron's statements, accepted by the Founder as the POC data terms, not verified by Noema):**
  - Retention is set by the customer (zero, a day, a week, and so on); new accounts start at zero retention; zero data retention by default, configurable upward (A377).
  - Intron states it does not use customer audio or transcripts to train its models (A377: no training on customer data).
  - Processing runs on AWS in Ireland (EU) (the 13 Nov email).
  - Intron states it is SOC 2 Type I, ISO 27001 and NDPR certified (A377).
  - A Data Processing Agreement is signed together with the commercial agreement (A377: "alongside a commercial agreement").

### OD-P-90: Intron's rate limits and capacity (ADOPTED as written; rulings A179 and A182)

- **Status:** [DEFAULT] · NON-CANONICAL · **adopted as written** on the Architect's instruction of 13 Nov 2026 ([DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md), §2); filed by the Steward on the Architect's instruction (rulings A179 and A182). The default below is the rule in force **from the SoT edit that adopts A179 (v1.12)**; until then the committed SoT stands and only synthetic audio goes to any speech provider.
- **Missing decision:** which rate limits and what capacity bind the voice subset run (BEN-23), the field work and a pilot, and whether Intron's answer on capacity is enough for the pilot.
- **Why it matters:** A182 requires BEN-23 to pace for the documented rate limits. The rulings give no figure; the Steward invents none (AGENT-18).
- **Default (smallest safe):** pace every run to Intron's documented limits; report the measured results as they come; the adapter splits TTS input into Intron's documented 10 to 100 character chunks (A181).
- **What would change it:** Intron's written answer on capacity; the latency lab report (VOI-16); a failure drill that shows the limits bind earlier than documented.
- **Not covered:** G5 thresholds, which do not change (A182).
- **Owner:** Voice Engineer (the adapter and pacing); Benchmark Owner (BEN-23); Founder (the capacity decision).
- **Deadline:** before the first gate run on Intron.
- **Source:** rulings A179, A181, A182; BEN-23; VOI-16.
- **Vendor statements (Intron's email of 13 Nov 2026; unverified until the DPA is signed and, where it says so, until measured; recorded on the Founder's direction of 16 Nov, A241; they are notes, not decisions, and set no threshold):**
  - An Integrator account can be set up at once, with 60 free test minutes to split between speech-to-text and text-to-speech; billing is prepaid credit (card through Stripe or Paystack, or invoice).
  - List rates per audio hour: speech-to-text English (including Nigerian English) 1.00 USD; speech-to-text local languages (including Pidgin and code-mixed speech) 1.25 USD; text-to-speech English 1.25 USD; text-to-speech local languages 1.50 USD. A volume tier applies at 10,000 to 50,000 hours a month, with custom pricing. (External figures, recorded as Intron's statement only; AGENT-18.)
  - The standard plan includes 3 concurrent sessions; Intron says it can raise this once it knows peak concurrency, operating days and hours and monthly volumes, and that rate limits are set in the same step.
  - New real-time streaming endpoints are said to go live "in the next few weeks", built for voice bots and supporting 8 kHz telephony audio; Intron prefers to give measured P95 figures on them under the customer's load. Intron's engineering later gave: intermediate (partial) transcripts usually about 1.7 seconds, P95 of 3 seconds; final transcript P95 of 8 seconds from the end of audio, measured on a 5-minute stream; both to be confirmed on the customer's own audio and expected load during evaluation.
  - Intron states that Nigerian English, Nigerian Pidgin and speech mixed with Pidgin, Yoruba, Igbo or Hausa are supported (language codes in its documentation).
  - Intron asks for the use case, the split between streaming and batch and between English and local languages, peak concurrent sessions and operating hours, the latency target, any text-to-speech volume, and a call with its engineering and product team. That reply is the Founder's or the Voice Engineer's; it sets no threshold.
  - **Class (A241):** the concurrency and the streaming endpoints do not block engineering on synthetic audio. They may block the live gate run or production until measured or raised; classified then, not now. **The only latency target is VOI-16 (end of speech to first spoken word on the clean path, under 1.8 s, by stage; A241):** Intron's quoted figures above are its statements, not targets, and are not compared to VOI-16 until they are measured on the streaming endpoints.

### OD-P-91: Per-token confidence from Intron's speech-to-text (ADOPTED as written; ruling A181)

- **Status:** [DEFAULT] · NON-CANONICAL · **adopted as written** on the Architect's instruction of 13 Nov 2026 ([DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md), §2); filed by the Steward on the Architect's instruction (ruling A181). The default below is the rule in force **from the SoT edit that adopts A179 (v1.12)**; until then the committed SoT stands and only synthetic audio goes to any speech provider.
- **Missing decision:** whether Intron's speech-to-text returns a confidence for each token, so that the key-slot rule of the PERD (a key slot below the configured confidence forces CLARIFY) can use it; and what the value for "insufficient confidence" is.
- **Why it matters:** spoken amounts, account identifiers and transaction references are never trusted (A181). If a confidence is not returned, the rule has no input.
- **Default (smallest safe):** a missing confidence counts as low. Partial transcripts never set a slot. "Insufficient confidence" is Founder or pack data; no agent sets it. A spoken "yes" is never a confirmation; only the signed card submit is.
- **What would change it:** Intron's documentation or the qualification run (UND-13) showing which confidences it returns; the Founder or the pack setting the value.
- **Not covered:** the existing thresholds in the pack and the plan, which do not change.
- **Owner:** Voice Engineer (what Intron returns); Founder or pack data (the value).
- **Deadline:** before the first gate run on Intron.
- **Source:** ruling A181; REQ-VOI-003; INV-02; UND-13.

- **Source:** rulings A177 and A189; A177 in [DEC-2026-11-12-architect-interim-a177-a178](decisions/DEC-2026-11-12-architect-interim-a177-a178.md); SoT §7, AGENT-02, INV-29.
- **Vendor statements (Intron's email of 13 Nov 2026; unverified until the DPA is signed and, where it says so, until measured; recorded on the Founder's direction of 16 Nov, A241; they are notes, not decisions, and set no threshold):**
  - **The email does not answer this question.** It says nothing about a confidence for each token; the entry stays open on that point (Intron's documentation or the qualification run, UND-13).
  - **Class (A241):** if no per-token confidence is returned, the default already stands (a missing confidence counts as low); that blocks no engineering work.

### OD-P-92: A recorded-replay Understanding provider for the G1 run (APPROVED by the Founder in session, 13 Nov 2026; AGENT-14; ruling A188)

- **Status:** [DECIDED] · NON-CANONICAL · filed by the Steward on the Architect's instruction (ruling A188, [DEC-2026-11-13-architect-rulings-a183-a192](decisions/DEC-2026-11-13-architect-rulings-a183-a192.md), interim). **The Founder approved it in session on 13 Nov 2026 (AGENT-14: a new component needs an approved entry).** The approval is recorded here by the Repo Steward as the Founder stated it; it counts as committed once a Founder who did not author this pull request merges it (A111; AGENTS §2, item 3). The approval is for exactly the default below: bench and test profiles only, refused in the demo profile, recordings from a real live compile run as synthetic fixtures with provenance, evidence labelled "Understanding: recorded replay of live output".
- **Decision:** approved. The question was: approval to add a recorded-replay Understanding provider under `providers/` in the model service, for the G1 run.
- **Why it matters:** G1 requires two runs of US-01 and US-06 with identical Trust decisions. Live model output differs between runs, so a live provider cannot give identical decisions. Replay can.
- **Default (smallest safe, ruling A188):** the provider is selected by configuration in the bench and test profiles only and is **refused in the demo profile**. Its recordings come from a real live compile run and are stored as synthetic fixtures with provenance. The G1 evidence is labelled "Understanding: recorded replay of live output". Nothing in Trust, Execution or the Outcome verdict changes; the model output still crosses the schema gate (INV-02).
- **What would change it:** the Founder declines (G1 would then run on live output and "identical decisions" could not be shown); or the Founder asks for the live compile run to be part of G1, which needs its own cost approval (UND-05).
- **Not covered:** Understanding qualification (UND-13), live provider runs (UND-05), any use of replay in the demo or a pilot (refused).
- **Owner:** Founder (the approval); C2 (the provider); EL (the G1 path and the label).
- **Deadline:** before the G1 evidence run.
- **Source:** ruling A188; AGENT-14; plan §3.1 (G1); PERD REQ-INT-002.

### OD-P-93: A TypeScript codegen target for the UI's contract types (OPEN; AGENT-14; for the Founders' approval)

- **Status:** [OPEN] · NON-CANONICAL · filed by the Steward on the Architect's instruction (noema#523, [DEC-2026-11-13-architect-rulings-a193-a198](decisions/DEC-2026-11-13-architect-rulings-a193-a198.md)). **The Steward files it; the Founders approve it.** The approach was chosen in a session, which is not authoritative until committed (AGENTS §2, item 3).
- **Missing decision:** approval of a third generator target, TypeScript, in the in-repository generator `tools/codegen`, so that the UI has types and runtime parsers for the contracts it reads (generated into `ui/src/contract_types/`).
- **Why it matters:** the UI shows only what the core sent and never an unmasked number (PERD §40.4), so every response and event is parsed before it is shown. The fixed stack gives codegen to Go and Pydantic only, and hand-written types per language are forbidden (PERD §36.1). A new generator target is a new tool (AGENT-14).
- **Default (smallest safe):** the target in noema#523: Python standard library only, no new dependency, scoped by `tools/codegen/ts.json` (a contract the UI does not read does not reach the bundle), output never edited by hand, `generate.py --check` failing on a difference. Owners agree: C1 for `tools/codegen`, the frontend engineer for `ui/`.
- **What would change it:** a decision to use a schema-to-TypeScript tool from outside (a new dependency), or to keep UI types hand-written (against PERD §36.1); or a finding that the parsers need the conditional rules of the schemas (the Security Reviewer's note on noema#523).
- **Not covered:** the UI's API client; the conditional rules (`if`, `then`, `not`), which stay with the JSON Schema validator.
- **Owner:** Founders (the approval); EL (the PR); C1 and the frontend engineer (the owners of the paths).
- **Deadline:** before noema#523 merges.
- **Source:** noema#523; AGENT-14, AGENT-15; PERD §36.1, §40.4; ruling A187.

### OD-P-94: An accessibility scan tool for the UI tests: axe (CLOSED; approved by ruling A252)

- **Status:** [CLOSED] · NON-CANONICAL · **approved** by ruling A252 (the text of A238; `DEC-2026-11-16-architect-rulings-a242-a252`, docs#192, open; no link until it merges): `@axe-core/playwright` **4.14.0** with `axe-core` **~4.14.0**, pinned with a lockfile, **local scan only**, a **test-only** dependency under **MPL-2.0** (file-level terms, unmodified). Filed by the Steward from noema#610; the registry facts below were read on 16 Nov 2026.
- **Missing decision:** approval of an accessibility scanner in the UI test manifest, so that UI-01 and UI-04 can run a WCAG scan (PERD §40.1, WCAG 2.2 AA) against the local synthetic UI. The approved UI package list ([DEC-2026-11-13-ui-01-frontend-dependencies](decisions/DEC-2026-11-13-ui-01-frontend-dependencies.md)) has `react`, `react-dom`, their `@types` and `@playwright/test`, and no axe.
- **Why it matters:** no new dependency without an [OPEN] entry and approval (AGENT-14); a test dependency still runs in CI and needs a pinned, reviewed supply chain.
- **Default (smallest safe), the Frontend Engineer's proposal:** `@axe-core/playwright` **4.14.0**, an exact pin with the lockfile committed (the rule of D2 of the UI dependency record), used only in tests against the local synthetic UI, no separate server and no third-party runtime script. **Facts read from the npm registry on 16 Nov 2026:** version 4.14.0 is the `latest` tag, published 15 Oct 2026 (more than two weeks old); its only dependency is `axe-core` `~4.14.0` (so `axe-core` also needs an exact pin); peer dependency `playwright-core` `>= 1.0.0` (compatible with the approved Playwright 1.64.1); licence **MPL-2.0**, where the packages already approved are MIT; the registry listing was not checked for install scripts.
- **What would change it:** a security or compatibility finding on `@axe-core/playwright` or `axe-core`; a preinstalled equivalent in the approved Playwright image; or a Founder objection to the MPL-2.0 licence (a test-only dependency that is not shipped in the UI bundle; to be confirmed).
- **Not covered:** any other accessibility tool; running the scan against anything but the synthetic UI.
- **Owner:** Founders or the Architect (the approval); the Frontend Engineer (UI-01, UI-04); the Security Reviewer (the supply-chain read).
- **Deadline:** before UI-01 or UI-04 adds the package.
- **Source:** noema#610; ruling A238; AGENT-14; PERD §40.1; DEC-2026-11-13-ui-01-frontend-dependencies.



### OD-P-95: A YAML parser for the CI safeguards: PyYAML (CLOSED; approved by the Founder, 17 and 18 Nov 2026)

- **Status:** [CLOSED] · NON-CANONICAL · **approved** by the Founder in comments on noema#667 ("approved: PyYAML, hash-pinned, safe_load, safeguards job only", 17 Nov 2026 14:50 UTC and again 18 Nov 2026 10:07 UTC), on the Architect's ruling A283 and A294. Filed by the Steward on the Security Reviewer's request ([DEC-2026-11-18-od-p-95-96-yaml-parser-and-ui-browser-build](decisions/DEC-2026-11-18-od-p-95-96-yaml-parser-and-ui-browser-build.md)). AGENT-14.
- **Missing decision:** approval of one YAML parser as a pinned, hash-locked dependency of `tools/ci`, so that the workflow checks read the parsed document and not its lines.
- **Why it matters:** two safeguards (no persisted checkout credential, noema#622; workflow permissions, noema#629) were line scanners, and Codex found a bypass in each, one valid spelling after another. A parser removes the class. No YAML parser was a `tools/ci` dependency (read by the Security Reviewer on noema#667): `tools/ci` is standard library only; `gopkg.in/yaml.v3` is an indirect Go requirement only.
- **Approved (the smallest safe default, as the Founder wrote it):** PyYAML; **hash-pinned** (an exact version with its hashes in a `tools/ci/requirements.lock`); **`yaml.safe_load` only** (never `load`); installed in the **`safeguards` job only**, with no other use. The two checks then walk the parsed `jobs` and `steps` with the same tests and canaries, and the line scanners are deleted in the same change.
- **Version:** not named by the approval. The Security Reviewer chooses it in the pull request and commits its hashes; it must be a release older than two weeks. **Facts the Steward read from PyPI on 18 Nov 2026:** the latest release is 6.0.3, uploaded 25 Sep 2025; licence MIT.
- **What would change it:** a security finding on the chosen release; a parser that is already available without a new dependency; a failure of `safe_load` on a real workflow file.
- **Not covered:** any other use of PyYAML or any other parser; installing it outside the `safeguards` job.
- **Owner:** Security Reviewer (the pull request and the pin); Founders (the approval, given).
- **Deadline:** before noema#622 and noema#629 are replaced by parser-based checks.
- **Source:** noema#667, noema#622, noema#629; rulings A283 and A294; AGENT-14.

### OD-P-96: A local browser build for interactive React: esbuild (CLOSED; approved by the Founder, 17 and 18 Nov 2026)

- **Status:** [CLOSED] · NON-CANONICAL · **approved** by the Founder in comments on noema#696 ("approved: react, react-dom, esbuild, pinned exactly, ui only", 17 Nov 2026 and 18 Nov 2026 10:07 UTC), on the Architect's approval in principle (A298). Filed by the Steward on the Frontend Engineer's request (noema#696; "the Steward assigns the decision number"). AGENT-14.
- **Missing decision:** how the UI's interactive React reaches a browser without an external script. The approved React 19 packages ship CommonJS entry points; the existing build emits ES modules and does not bundle them, so a browser cannot run them. The approved UI package list ([DEC-2026-11-13-ui-01-frontend-dependencies](decisions/DEC-2026-11-13-ui-01-frontend-dependencies.md), D5) approves no bundler.
- **Approved:** `react`, `react-dom` (already approved, D1 of that record) and **`esbuild`**, **pinned exactly**, in `ui/` only, as a **dev dependency** that bundles the existing React and TypeScript entry point locally. No runtime CDN, no hand-written module loader, no new service, state library or UI framework.
- **Version:** the Frontend Engineer proposes **0.28.2** (noema#696). **Facts the Steward read from the npm registry on 18 Nov 2026:** 0.28.2 is the `latest` tag, published 8 Aug 2026 (more than two weeks old); licence MIT; no runtime dependencies; 26 optional platform-binary packages; its `postinstall` script is `node install.js`. The approval does not name the version, so the Founders or the Architect confirm 0.28.2 on noema#696 if they want it fixed here; otherwise the Frontend Engineer pins the version that passes the checks below, and the pull request names it.
- **Conditions (from noema#696, kept):** a committed lockfile; `npm audit` evidence on it (a high or critical finding returns the package to the Founders, D3 of the UI record); the install works under the existing `npm ci --ignore-scripts` policy, with the platform binary verified (esbuild's `postinstall` does not run under `--ignore-scripts`, so the install path is shown, not assumed); security and compatibility review (the Security Reviewer).
- **What would change it:** a security or compatibility finding on `esbuild`; an already-approved browser delivery method the Architect points to; a failure under `--ignore-scripts`.
- **Not covered:** any other bundler, dev server, plugin or loader; esbuild outside `ui/`; a runtime use.
- **Owner:** Frontend Engineer (the pull request, noema#699); Security Reviewer (the supply-chain read); Founders (the approval, given).
- **Deadline:** before noema#699 adds the package.
- **Source:** noema#696, noema#699; ruling A298; AGENT-14; REQ-UI-001, POC-FR-11; DEC-2026-11-13-ui-01-frontend-dependencies.


### OD-P-97: OpenTelemetry in both services (CLOSED; approved by ruling A320)

- **Status:** [CLOSED] · NON-CANONICAL · **approved** by ruling A320 ("REC-02: OpenTelemetry is approved (PERD §36.1)"; [DEC-2026-11-18-architect-rulings-a317-a328](decisions/DEC-2026-11-18-architect-rulings-a317-a328.md)). AGENT-14.
- **Missing decision:** approval of the OpenTelemetry packages REC-02 needs (the correlation chain in headers, `traceparent`, logs and spans in both services).
- **Why it matters:** no new dependency without an entry and approval (AGENT-14); PERD §36.1 names "OpenTelemetry, Prometheus-style metrics, JSON logs with redaction" in the fixed stack, so the stack is not in question, only the exact packages.
- **Approved:** OpenTelemetry for tracing and correlation in the core and the model service, as PERD §36.1 names it. The exact packages and versions are named by REC-02's pull request, pinned with the lockfile, and read by the Security Reviewer.
- **Not covered:** any vendor-specific agent or exporter (PERD §36.1 rejects vendor agents); any other telemetry library.
- **Owner:** C2 (REC-02); Security Reviewer (the supply-chain read).
- **Source:** ruling A320; PERD §36.1; REQ-AUD-004, REQ-OBS-002, REQ-SEC-003.

### OD-P-98: `pgregory.net/rapid` adopted (CLOSED; adopted, A320)

- **Status:** [CLOSED] · NON-CANONICAL · **adopted** by ruling A320 ("`rapid` is already in `go.mod` and in use, so the Steward records it as adopted"). The dependency itself was approved earlier by [DEC-2026-11-03-rapid-test-dependency](decisions/DEC-2026-11-03-rapid-test-dependency.md) (a test-only dependency of the core, Block E E6). AGENT-14.
- **Missing decision:** none outstanding: PERD §36.1 lists the Go property-testing library as [REC] and the approval was recorded on 3 and 7 Nov 2026.
- **Recorded:** `rapid` is the adopted Go property-testing library. The next PERD version drops its [REC] label.
- **Not covered:** any other property-testing library.
- **Owner:** Engineering lead.
- **Source:** ruling A320; DEC-2026-11-03-rapid-test-dependency; PERD §36.1.

### OD-P-99: golangci-lint for the Go gate (CLOSED; approved by ruling A318)

- **Status:** [CLOSED] · NON-CANONICAL · **approved** by ruling A318 ("PLT-09 stays approved (A296): golangci-lint 2.5.0 pinned, gating after the 12 baseline findings are fixed"). AGENT-14.
- **Missing decision:** approval of golangci-lint as a lint tool (AGENTS §5: linters not in PERD §36.1 need approval). PLT-09 names golangci-lint, mypy and Ruff in the plan row and PERD v1.19.
- **Approved:** golangci-lint **2.5.0**, pinned (by hash, A296), as the Go gate of PLT-09. It gates only after the 12 baseline findings are fixed; until then it reports. Reading `.github` changes is the Security Reviewer's (A296).
- **Not covered:** any other linter or formatter; mypy and Ruff are PLT-09's other tools under the plan row and PERD v1.19 and keep their own pins.
- **Owner:** EL (PLT-09); Security Reviewer (`.github`).
- **Source:** rulings A296 and A318; PLT-09; PERD v1.19.

### OD-P-100: Build provenance in the Record: once per process, not once per event (OPEN, deferred; trigger below)

- **Status:** [OPEN] · NON-CANONICAL · deferred until its trigger. Opened by Core Engineer 1 under ruling A488 (relayed by the Founder in session, interim, not yet committed; AGENTS §2.3); **reshaped on 21 Nov 2026 by the Founder's direction in session after merging noema#850 (not yet committed either: a decision record is the Steward's)**. AGENT-02.
- **Decided in session, not yet recorded (Founder, 21 Nov 2026):** noema#850 shipped option (a): no commit SHA on the POLICY_PUBLISHED event. It closes the real INV-12 hole, a caller asserting who published. A474 is to be amended and recorded: the commit-SHA line is dropped, replaced by "omit; the document hash ties the publication to the policy text".
- **Missing decision (the open part):** whether and how the Record states which build produced a run. Direction given: record it **once per process**, as a single process-start Record event carrying the build revision (marked `unavailable` or dirty when that is true) and the image digest, covering the core, `policypublish` and grant issuance; **not** as a member of each event. That needs **one typed guard shape in one place** (the payload guard, A184, refuses a bare 40-hex revision whenever it holds a run of more than four digits: checked on origin/main on 21 Nov 2026, `3f9a1c22b7d4e5f60812a3b4c5d6e7f801234567` is refused with "a run of 9 digits"; about 82% of random revisions hold such a run). A replay or a reconstruction could then say which build produced a run.
- **Why it matters (later, not now):** INV-21 replay and the G1/G2 evidence may need to name the build. **Today there is no consumer**, which is why the card is deferred.
- **Trigger to open the card:** when INV-21 replay, or the G1 or G2 evidence, needs build provenance. Until then nothing is built and no event, guard shape or payload member is added.
- **Proposed smallest safe default (when the trigger fires; for the Architect):** (1) a guard shape for a git revision at one path of the process-start event only (the whole string is 40 lower-case hex digits), with the same exemption style as the receipt paths of A231 and a test that the same string at any other path is still refused; (2) one process-start event, written once per process start by each process that issues or publishes (core, `policypublish`, grant issuance), carrying `build_revision` (`debug.ReadBuildInfo` `vcs.revision`; the literal `unavailable` when the information is absent; the literal `dirty` or `unavailable` when `vcs.modified` is true; no fallback to a flag, an environment variable or a file) and the image digest, with the build-info reader behind a small injected function so tests can supply values (test binaries carry no VCS data); (3) tests first: the value comes from the build information; absent gives `unavailable`; modified is marked; a flag or an environment variable named like a commit SHA changes nothing; the same string elsewhere is still refused; (4) a README line that the event names the binary, not the operator, and that the publisher stays the authenticated database role.
- **Evidence that would invalidate the default:** a guard shape that cannot be limited to one path without admitting a nine-digit identifier elsewhere; a build pipeline that never embeds VCS data or an image digest (the event would always say `unavailable`, and the decision would be to drop it); a consumer that needs the revision per event (it would then be per event, with the guard shape of (1)).
- **Owner:** Architect (the guard, the event and the contract); Core Engineer 1 (the writers); Security Reviewer (the guard change); Infrastructure Lead (the image digest).
- **Source:** ruling A488; A474 ([DEC-2026-11-20-architect-rulings-a469-a485](decisions/DEC-2026-11-20-architect-rulings-a469-a485.md)); noema#850 (merged, option (a)); `services/core/record/payloadguard/guard.go`; the Security Reviewer's recommendation on noema#850 (build information only, name `build_revision`); the Founder's direction of 21 Nov 2026.

### OD-P-101: The compile gate's threshold: 9000 basis points, interim (OPEN, Founder to confirm)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from ruling A603 (interim, in `DEC-2026-11-23-architect-rulings-a602-a605`; counts when that record merges). AGENT-16: an agent never sets a threshold.
- **Missing decision:** the threshold of the compile service's stage-1 gate ("Does the customer explicitly ask for something to be done for them?"): the confidence at or above which the gate answers yes and stage 2 picks a capability. A false assertion is the harmful error, so doubt abstains.
- **Interim value (the Architect's, labelled a Founder decision to confirm):** **9000 basis points**, held in pack data, never a code constant.
- **Why it matters:** a threshold set too low lets a false assertion through; too high makes the service miss explicit requests (the safe error, but a cost). The golden compile runs and the offline set (A604) are the evidence; no golden is edited (A533).
- **Proposed smallest safe default:** keep 9000 basis points until the Founders confirm or change it, after run 8 (and run 9 only if its readable evidence shows a threshold problem; A605).
- **Evidence that would invalidate the default:** the per-golden option, the top five probabilities including abstain and the threshold applied, printed by the job log (A602); run 8's variance over three repeats; the offline set of 24 to 30 synthetic phrasings (A604).
- **Owner:** the Founders (the value); Core Engineer 2 (the pack data and the gate); Benchmark Owner (the offline set).
- **Source:** rulings A602, A603, A604, A605; AGENT-16; INV-22.

### OD-P-102: `capability-descriptor.v2`: compensation per capability (OPEN, provisional; contract change for both Founders)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from ruling A631 (interim, in `DEC-2026-11-24-architect-rulings-a624-a643`; counts when that record merges). AGENT-15 applies.
- **Missing decision:** the contract `capability-descriptor` has no per-capability compensation member. The PERD packcheck rules need one. The Architect rules that **the PERD vocabulary wins**: a new `capability-descriptor.v2` with compensation as the enum `NONE_REQUIRED`, `INVERSE_CAPABILITY`, `ESCALATE_ONLY`, and an `inverse_mapping` (a capability id plus a parameter map) **required when `INVERSE_CAPABILITY`**. It adds only what the PERD packcheck rules need.
- **What stays open until both Founders approve the contract change:** the exact members and their JSON Schema; the packcheck rules (C1 owns them); the version bump, the migration note and the regenerated models (AGENT-15). PCK-05 stays separate (A627).
- **Why it matters:** a capability that has no declared compensation cannot be checked by packcheck for a missing inverse, and a pack could ship a write with no recovery definition (plan §13.1: no new capability without its registry entry, policy, verification predicate and recovery definition).
- **Proposed smallest safe default:** exactly the Architect's ruling and nothing more: the three enum values and `inverse_mapping` required for `INVERSE_CAPABILITY`; packcheck refuses a descriptor that omits the member.
- **Evidence that would invalidate the default:** a POC capability whose compensation the three values cannot express; an `inverse_mapping` that needs more than a capability id and a parameter map for the four POC capabilities.
- **Owner:** Core Engineer 1 (the contract and the packcheck rules); both Founders (approval); EL for PCK-05 (separate).
- **Source:** ruling A631; plan task CAP-02; PERD packcheck rules; AGENT-15.

### OD-P-103: `priority_routing` values for the SLA phases (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from ruling A644 (interim, in `DEC-2026-11-24-architect-rulings-a644-a656`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** The PERD and the plan give no more than the phrase "priority routing data" (plan row TRU-06). The Architect's smallest safe design: a pack member `priority_routing` maps each SLA phase to `{priority, owner_queue}`; `priority` is one of `HIGH`, `NORMAL`, `LOW`; **the values are SYNTHETIC, EL writes them**; C1's evaluator reads the member; a phase with no entry gets `NORMAL`. What is open is the values themselves (which phase gets which priority and which queue).
- **Why it matters:** A wrong priority sends a case to the wrong queue or delays an urgent one; it never allows a write (routing is not authority).
- **Proposed smallest safe default:** Exactly the Architect's design and nothing more; EL writes SYNTHETIC values; an absent phase is `NORMAL`.
- **Evidence that would invalidate the default:** A phase the SLA evaluator produces that the member cannot express; an `owner_queue` that does not exist in the pack's queues.
- **Owner:** EL (the values, as SYNTHETIC pack data); Core Engineer 1 (the evaluator); the Founders (any non-SYNTHETIC value).
- **Source:** ruling A644 (and A640: one owner per member); plan task TRU-06; AGENT-16.


### OD-P-104: The tenant-wide rate limit for TRU-11 is not built in the POC (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from ruling A648 (interim, in `DEC-2026-11-24-architect-rulings-a644-a656`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** TRU-11 counts the principal's decisions for a capability over the last hour on the database clock (A630, A648: every capability in the authorized set is checked; a voided grant still counts toward the hour). **A tenant-wide limit is not built in the POC.** What is open is whether and when one is wanted.
- **Why it matters:** Without a tenant-wide limit, many principals of one tenant can each stay under the per-principal limit while the tenant as a whole sends many writes.
- **Proposed smallest safe default:** No tenant-wide limit in the POC; the per-principal count only (A648). Wiring the Rates adapter happens after the G1 run.
- **Evidence that would invalidate the default:** A G1 or G2 case that needs a tenant-wide cap; a partner requirement for one.
- **Owner:** Architect (the decision); Core Engineer 1 (TRU-11).
- **Source:** rulings A630 and A648; plan task TRU-11.


### OD-P-105: The outcome pack-mapping field and a `Pending` member in the outcome-definition contract (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from ruling A651 (interim, in `DEC-2026-11-24-architect-rulings-a644-a656`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** For G1 the caller supplies the Outcome request's bindings; EL's composition fills them by exact name match between predicate variable and plan parameter, and refuses on a missing match; `Pending` stays nil (A651). What is open, after G1: a **pack mapping field** that carries the bindings in pack data, and a **`Pending` member** in the outcome-definition contract.
- **Why it matters:** Without them the bindings live in code at the composition root, and a pending outcome cannot be expressed in the outcome definition.
- **Proposed smallest safe default:** Nothing built before G1; exactly A651's exact-name match with refusal on a missing match; `Pending` stays nil.
- **Evidence that would invalidate the default:** A G1 case with a pending outcome that the nil `Pending` cannot represent; a binding that exact-name matching cannot resolve.
- **Owner:** Core Engineer 2 (the Outcome request builder, #950); EL (the composition); the Founders (a contract change, AGENT-15).
- **Source:** ruling A651; ruling A620 (slice 3 is C2's); AGENT-15.


### OD-P-106: The REGRESSION_LINK observation writer (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from ruling A652 (interim, in `DEC-2026-11-24-architect-rulings-a644-a656`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** The regression-link check (MEM-02, merged) fails a fix PR without a link; the Architect says a **`REGRESSION_LINK` observation writer** is open for after G1 (a writer that records the link as an observation). What exactly it records, and where, is not decided.
- **Why it matters:** Without it the link is checked in CI but not recorded as evidence a reviewer or the G3 gate can read later.
- **Proposed smallest safe default:** Nothing built before G1; the CI check stays as merged.
- **Evidence that would invalidate the default:** A G3 or release-evidence requirement that the CI check alone cannot meet.
- **Owner:** Benchmark Owner; EL.
- **Source:** ruling A652; plan task MEM-02 (Done); REQ-MEM-002.

### OD-P-107: The convergence window of each compared fact pair (named OD-RES05-1) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from the rulings A657 to A667 (interim, in `DEC-2026-11-25-architect-rulings-a657-a667`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** The window inside which two compared facts may still converge (RES-05, noema#949). A659 rules: no new number; the windows come from A641 (the smaller freshness limit of the pair), declared as `convergence_window_seconds` in rule set version 2. Whether the Founders accept those windows as the POC's is not recorded.
- **Why it matters:** Inside the window the Reconciler waits, with no write and no verdict; outside it escalates. A wrong window waits too long or escalates too early.
- **Proposed smallest safe default:** No window, so ESCALATE (fail closed). With A659, the window is the smaller freshness limit of the pair, checked equal by packcheck.
- **Evidence that would invalidate the default:** Settlement and reversal lag observed in the benchmark world that the freshness limits do not cover.
- **Owner:** Founders; C1 (rule set v2); EL (PCK-05).
- **Source:** rulings A641, A659; `status/RES-05.md` (feat/RES-05-convergence-windows); REQ-RES-005; AGENT-16.

### OD-P-108: Pack limit values that the SoT and the PERD do not state (named OD-A544) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from the rulings A657 to A667 (interim, in `DEC-2026-11-25-architect-rulings-a657-a667`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A544: `limits/trust_limits.json` and its values are C2's; a value the PERD and the SoT do not state is an [OPEN] entry. Which values those are is listed by the owner of each limit, not by the Steward.
- **Why it matters:** A pack value nobody may invent (AGENT-16) blocks any code that needs it, and a guessed one is an unsafe default.
- **Proposed smallest safe default:** Nothing allowed under freeze; no route means UNKNOWN (A544).
- **Evidence that would invalidate the default:** A value stated in the SoT or the PERD, or a Founder decision that sets it.
- **Owner:** C2 (the pack's values); Founders.
- **Source:** ruling A544 (`DEC-2026-11-23-architect-rulings-a542-a553`); AGENT-02, AGENT-16.

### OD-P-109: A per-source freshness override (named OD-EVD02-1) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from the rulings A657 to A667 (interim, in `DEC-2026-11-25-architect-rulings-a657-a667`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** PERD §21.2 names `per_source_override?` in the effective limit and `PROFILE_OVERRIDE` in `limit_set_by`, but neither the trust profile nor any pack member or contract carries an override. Where it lives, and who sets its values, is not decided.
- **Why it matters:** `freshness.Limits.Override` is an input nothing supplies, so it is zero.
- **Proposed smallest safe default:** No override.
- **Evidence that would invalidate the default:** A requirement to age one source out faster or slower than the profile's `max_evidence_age_seconds`.
- **Owner:** Founders (a pack member on the trust profile, additive, AGENT-15).
- **Source:** `status/EVD-02.md` (OD-EVD02-1); PERD §21.2; AGENT-16.

### OD-P-110: The read budget of REQ-CTX-003 (named OD-EVD02-2) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from the rulings A657 to A667 (interim, in `DEC-2026-11-25-architect-rulings-a657-a667`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** REQ-CTX-003 says "within the read budget" and no number is stated in the documents; `Session` takes the refresh timeout as a required argument.
- **Why it matters:** Without a stated budget every caller picks its own timeout, so a read can wait past what the journey allows.
- **Proposed smallest safe default:** The caller must pass a timeout; no default is set.
- **Evidence that would invalidate the default:** A budget in the SoT, the PERD or a Founder decision.
- **Owner:** Architect.
- **Source:** `status/EVD-02.md` (OD-EVD02-2); REQ-CTX-003; AGENT-16.

### OD-P-111: The clock-skew tolerance when ordering events (EVENT_ORDER) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from the rulings A657 to A667 (interim, in `DEC-2026-11-25-architect-rulings-a657-a667`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** Rules A641, A659 and the Reconciler's EVENT_ORDER_UNCERTAIN (OD-P-56) need to know how far apart two event times may be before their order is uncertain. The ruling names an `EVENT_ORDER skew` open entry without text; the Steward wrote this entry from OD-P-56 and the safe-default rule, and the Architect confirms or corrects it.
- **Why it matters:** A tolerance that is too wide hides a real reordering; one that is too narrow escalates cases the data would order.
- **Proposed smallest safe default:** Zero tolerance: any case where the order cannot be shown from the facts is EVENT_ORDER_UNCERTAIN, so ESCALATE.
- **Evidence that would invalidate the default:** Observed skew between the stand-in's and Tushe's event times in the benchmark world.
- **Owner:** Founders; C1.
- **Source:** OD-P-56; REQ-CTX-008 ("clock skew: recorded"); AGENT-16. Wording the Steward's.

### OD-P-112: The EVD-05 retry budget (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward from the rulings A657 to A667 (interim, in `DEC-2026-11-25-architect-rulings-a657-a667`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** REQ-CTX-008 gives a bounded exponential backoff of 100 ms, 300 ms and 900 ms for a 429 without `Retry-After`, labelled [REC], and "honour `Retry-After` within the read budget" with no stated budget (see OD-P-110). Whether the [REC] backoff is adopted for the POC is not recorded. The ruling names this open entry without text; the Steward wrote it from REQ-CTX-008, and the Architect confirms or corrects it.
- **Why it matters:** A retry budget is a safety limit (AGENT-16): too many retries hammer the enterprise, none turn every 429 into UNKNOWN.
- **Proposed smallest safe default:** No retry: a read that fails is UNKNOWN. The [REC] backoff stays [REC] until a decision adopts it.
- **Evidence that would invalidate the default:** A fixture or run showing that UNKNOWN on a 429 breaks a journey the pack allows.
- **Owner:** Founders; C2 (EVD-05).
- **Source:** REQ-CTX-008; plan task EVD-05; AGENT-16. Wording the Steward's.

### OD-P-113: The `reversal_posted` event's shape, and the reversal pair of the convergence matrix (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A673 to A684 (interim, in `DEC-2026-11-25-architect-rulings-a673-a684`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** Tushe has not stated the shape of the inbound `reversal_posted` event (A674, A659), so the window of the reversal pair of PCK-05's convergence matrix cannot be tied to its source. **A691 keeps the pair in the active rule list** with `convergence_window_seconds` = 0 (no window, an immediate ESCALATE; see OD-P-118). The remaining unknown is the `reversal_posted` event shape and, once Tushe states it, the freshness-based window (the smaller of its sources' freshness limits). The question is item 9 of `docs/poc/tushe/questions-2026-11-25-env05.md`, to be sent by the Founder with the OpenAPI request. The rule text, as the pack's rule set v1 carries it: the contradiction `reversal_conflict` (a reversal in state POSTED against a debit in state NOT_POSTED, unless noted) and rule R3 (REVERSED_CONFIRMED when a reversal is KNOWN, POSTED and `original_debit_linked`, with no `reversal_conflict` contradiction); EL attaches the exact pair to the pull request.
- **Why it matters:** Without the shape no window can be tied to the reversal source, and a guessed shape would be an invented one (AGENTS §14).
- **Update (A691, replaces A674's removal; interim, `DEC-2026-11-25-architect-rulings-a690-a700`):** the pair is **kept** in the active rule list and the set-730 corpus test is not weakened. Its `convergence_window_seconds` is declared as **0** (no window, so an immediate ESCALATE): the safest value, packcheck passes, no number is invented. When Tushe states the `reversal_posted` shape, the window becomes the smaller of its sources' freshness limits.
- **Proposed smallest safe default:** Per A691: the pair stays in the active rule list with a window of 0, so a case that depends on a reversal escalates at once and never waits. The other three computable pairs carry 300 s each (A641, A674).
- **Evidence that would invalidate the default:** Tushe's written answer giving the `reversal_posted` shape (and where the original-debit link comes from).
- **Owner:** Founders (the Tushe answer); EL (PCK-05).
- **Source:** rulings A659, A674; `docs/poc/tushe/questions-2026-11-25-env05.md` item 9; REQ-RES-005; AGENT-16.

### OD-P-114: A decline message template keyed by reason code (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A673 to A684 (interim, in `DEC-2026-11-25-architect-rulings-a673-a684`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A680: the decline is a fixed generic message with no internal code. Whether a pack template keyed by reason code replaces it is not decided; it is open after G1.
- **Why it matters:** A generic message is safe but gives the customer no plain reason; a reason-keyed text risks leaking an internal code or a rule.
- **Proposed smallest safe default:** The fixed generic message; no reason text, no code, no template.
- **Evidence that would invalidate the default:** A journey where the generic message makes the customer unable to act, shown after G1.
- **Owner:** Architect; FE (copy).
- **Source:** ruling A680; REQ-INP-004 (INP-01); AGENT-09.

### OD-P-115: Interim execute and rollback timeouts (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A673 to A684 (interim, in `DEC-2026-11-25-architect-rulings-a673-a684`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A681: `NOEMA_EXECUTION_EXECUTE_TIMEOUT_MS` and `NOEMA_EXECUTION_ROLLBACK_TIMEOUT_MS` stay required with no code default (fail closed). Interim values go in the bench compose only: execute 10000, rollback 5000. The Founders must confirm or change them.
- **Why it matters:** A timeout is a safety limit (AGENT-16); too short turns a slow write into OUTCOME_UNKNOWN, too long holds the case.
- **Proposed smallest safe default:** Execute 10000 ms and rollback 5000 ms in the bench compose only; nothing in code; a missing setting fails the start.
- **Evidence that would invalidate the default:** A measured execute or rollback time from the Tushe or stand-in runs that exceeds or far undercuts these.
- **Owner:** Founders; C1.
- **Source:** ruling A681; AGENT-16; REQ-EXE-003.

### OD-P-116: The `SLA_EVALUATED` payload schema (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A673 to A684 (interim, in `DEC-2026-11-25-architect-rulings-a673-a684`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A681 approves the `SLA_EVALUATED` payload schema as an additive contract file, with a migration note and regenerated models, in one small pull request for both Founders in the pass with #969. **A694 confirms the payload's members and the two conditional rules as written in #984.** What remains open is the contract file itself, its migration note and regenerated models (AGENT-15), and both Founders' approval.
- **Why it matters:** A Record event with no schema cannot be asserted in tests or read by the reconstruction (AGENT-15).
- **Update (A694, interim, `DEC-2026-11-25-architect-rulings-a690-a700`):** the `SLA_EVALUATED` members and the two conditional rules in #984 are **confirmed**; the entry stays Open until the contract file merges with both Founders' approval (A681).
- **Proposed smallest safe default:** No `SLA_EVALUATED` event is written until the contract file merges.
- **Evidence that would invalidate the default:** The members the clocks and the explanation need that the first draft lacks.
- **Owner:** C1; both Founders (approval).
- **Source:** ruling A681; AGENT-15; PERD §32.2.

### OD-P-117: `golang.org/x/text` and a manifest kind for the matcher data file (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A690 to A700 (interim, in `DEC-2026-11-25-architect-rulings-a690-a700`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A695 approves `golang.org/x/text` for the Go recipient matcher (C2, #960) and one manifest kind for the matcher data file. A new dependency needs an entry and approval (AGENT-14); the ruling says both Founders approve at the #960 merge. The module is not yet in PERD §36.1's list, and the manifest kind's name and shape are C2's to state in the pull request.
- **Why it matters:** A matcher built without a vetted text library would hand-roll Unicode handling for names; a new manifest kind is a pack-contract change (AGENT-15).
- **Proposed smallest safe default:** The matcher uses only the approved module and the one manifest kind; nothing else is added; the matcher data file is pack data, never code (SoT §51).
- **Evidence that would invalidate the default:** A need for a second module or a second manifest kind, or a finding that the module cannot do the matching A675 and A676 require.
- **Owner:** C2; both Founders (approval at the #960 merge).
- **Source:** ruling A695; AGENT-14, AGENT-15; PERD §36.1; noema#960.

### OD-P-118: The reversal pair's `convergence_window_seconds` of 0 (A691) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A690 to A700 (interim, in `DEC-2026-11-25-architect-rulings-a690-a700`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A691 keeps the reversal pair and declares its `convergence_window_seconds` as 0, meaning no window and an immediate ESCALATE, until Tushe states the `reversal_posted` shape; then the window becomes the smaller of its sources' freshness limits. Whether the Founders accept 0 for the POC is not recorded; it is the Architect's interim ruling.
- **Why it matters:** A window of 0 is the fail-closed value; a larger one would be an invented number (AGENT-16).
- **Update (A708, interim, `DEC-2026-11-26-architect-rulings-a704-a720`):** the schema and the loader allow a window of 0 (C1's small contracts PR, both Founders; see OD-P-124). The reversal pair stays at 0; EL reworks #988 after that PR.
- **Proposed smallest safe default:** 0 seconds: no window, immediate ESCALATE, for the reversal pair only.
- **Evidence that would invalidate the default:** Tushe's written shape for `reversal_posted` (see OD-P-113), after which the smaller freshness limit applies.
- **Owner:** Founders (with the Tushe answer); EL (#988).
- **Source:** ruling A691; OD-P-113; REQ-RES-005; AGENT-16.

### OD-P-119: The `step_params` member of the signed execution receipt (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A690 to A700 (interim, in `DEC-2026-11-25-architect-rulings-a690-a700`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A692 (slice 4, option (b)): add `step_params` to the signed execution receipt as an additive member in the receipt contract. It holds only the params named by the outcome definition's PLAN_PARAM bindings. It is a contract change (AGENT-15) with a migration note and both Founders; C1 owns it because Execution produces the receipt. The member's exact shape is C1's to state in the pull request.
- **Why it matters:** The outcome reader (lane 5 slice 4) cannot read the plan's params from what Execution wrote without it; a wider member would put params the outcome does not need into a signed receipt.
- **Proposed smallest safe default:** No `step_params` until the contract change merges; EL builds the slice 4 reader after that lands, and reads only what Execution wrote.
- **Evidence that would invalidate the default:** A needed param that no PLAN_PARAM binding names.
- **Owner:** C1; both Founders (approval).
- **Source:** ruling A692; AGENT-15; REQ-VER-001, REQ-VER-002; PERD §32.

### OD-P-120: The injection screen's five limits (bench values) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A704 sets the five Limits as settings with no code default: max patterns 64, max pattern length 1024 characters, max document size 65536 bytes, max nesting depth 8, field cap 256 characters. The values go in the bench compose only. Whether the Founders adopt them for any other profile is not recorded; EL maps them to the real field names and the `NOEMA_INJECTION_*` settings.
- **Why it matters:** They bound what the advisory screen reads (AGENT-16); too high a bound costs time, too low refuses real packs.
- **Proposed smallest safe default:** The bench values above, in the bench compose only; a missing setting fails the start.
- **Evidence that would invalidate the default:** A real pack's pattern data or an evidence document that exceeds a bound, seen in a run.
- **Owner:** Founders; EL; IL (compose).
- **Source:** ruling A704, A714; REQ-CTX-007; AGENT-16.

### OD-P-121: The planner text bound `NOEMA_PLAN_TEXT_MAX_BYTES` (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A705: required with no default; the bench compose sets 256. Whether 256 is adopted beyond the bench is not recorded.
- **Why it matters:** It bounds the plan text the Planner accepts (AGENT-16).
- **Proposed smallest safe default:** 256 bytes in the bench compose only; absent fails the start.
- **Evidence that would invalidate the default:** A plan text that legitimately exceeds 256 bytes in a G1 journey.
- **Owner:** Founders; EL; IL.
- **Source:** ruling A705, A714; AGENT-16.

### OD-P-122: The maximum push-to-talk recording of 30 seconds (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A715: the maximum push-to-talk recording is 30 s as a UI setting, and Voice enforces the same limit host-side. A715 marks it OPEN for the Founders: whether 30 s is the POC's value is theirs to confirm.
- **Why it matters:** A recording limit bounds audio stored and sent to the speech provider (AGENT-16; no raw audio retained beyond the plan).
- **Proposed smallest safe default:** 30 seconds, enforced in the UI and host-side by Voice.
- **Evidence that would invalidate the default:** A journey or an utterance in the recordings that needs longer.
- **Owner:** Founders; FE; Voice.
- **Source:** ruling A715; AGENT-16.

### OD-P-123: The version token and the complete marker of the portread payload (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A706 (A665): `version_token` is the maximum entry version, as a string; `complete` means the read answered and was not unavailable. The allowlist is extended to `evidence/portread`, in its own PR. Whether the Founders adopt this meaning for the contract is not recorded.
- **Why it matters:** The token and the marker decide whether a facts read is whole and current; a wrong meaning would let a partial read count as complete.
- **Proposed smallest safe default:** The meaning above; a read that did not answer is never `complete`.
- **Evidence that would invalidate the default:** A read path where the maximum entry version does not identify the state read.
- **Owner:** Architect; EL.
- **Source:** ruling A706, A665; INV-21.

### OD-P-124: A convergence window of 0 allowed by the pack schema and the loader (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A708: the schema and the loader allow a window of 0 (C1, a small contracts PR for both Founders). The reversal pair stays at 0 (A691); the four single-valued windows use the smaller freshness limit of their sources (300 s for credit and switch). OD-P-118 (the reversal pair's 0) is updated in place.
- **Why it matters:** A window of 0 means no window and an immediate ESCALATE; the schema change widens what a pack may declare (AGENT-15).
- **Proposed smallest safe default:** 0 only for the reversal pair; every other window the smaller freshness limit of its sources.
- **Evidence that would invalidate the default:** A pack that declares 0 for a pair other than the reversal pair.
- **Owner:** C1 (contracts PR); both Founders; EL (#988 rework).
- **Source:** rulings A691, A708; REQ-RES-005; AGENT-15, AGENT-16.

### OD-P-125: INP-01 design 8 (slot inheritance) rejected (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A712 rejects design 8: N+1 is compiled alone, and missing slots are asked through SLOT clarification (on `main` since #926). The other safer defaults of the INP-01 note stand; #684 merges after EL's re-read. Whether the Founders confirm the rejection is not recorded.
- **Why it matters:** Slot inheritance would carry earlier slot values into a new version; asking again is the safer reading.
- **Proposed smallest safe default:** Design 8 rejected; N+1 compiled alone; missing slots asked.
- **Evidence that would invalidate the default:** A journey where asking again makes the customer unable to continue.
- **Owner:** Founders; C2 (INP-01); EL.
- **Source:** ruling A712; REQ-INP-004, REQ-INT-004.

### OD-P-126: The REQ-INT-004 rewording (PERD v1.30, Proposed) (OPEN, provisional)

- **Status:** [OPEN] · NON-CANONICAL · opened by the Repo Steward at the Architect's instruction from the rulings A704 to A720 (interim, in `DEC-2026-11-26-architect-rulings-a704-a720`; counts when that record merges). AGENT-02 structure.
- **Missing decision:** A680 and A712 ask for a rewording of REQ-INT-004 like A312's: version N+1 voids nothing at admit time and a stale grant is refused at its next use (step E3). It is drafted as PERD v1.30 (Proposed; merged in `main`, with `CR-2026-11-25-A680-perd-v1.30-int-004-lazy-void`). Whether the Founders accept the version is not recorded (A688: approve if it restates A404 and D8 and changes no behaviour).
- **Why it matters:** Until accepted, the PERD text and the code disagree on when a grant is voided.
- **Proposed smallest safe default:** The v1.30 wording; the rulings govern until the Founders accept the version.
- **Evidence that would invalidate the default:** A reading of A404 or D8 that the wording does not match.
- **Owner:** Founders; Architect.
- **Source:** rulings A680, A688, A712; D8; PERD v1.30.
