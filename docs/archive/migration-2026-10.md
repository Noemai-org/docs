# Documentation migration report: October 2026

> **Historical record, non-authoritative.** This report describes the migration of this repository to `NOEMA_SOURCE_OF_TRUTH.md` v1.1. It defines nothing. For current authority see [`../NOEMA_SOURCE_OF_TRUTH.md`](../NOEMA_SOURCE_OF_TRUTH.md).

| | |
|---|---|
| Date | 2 October 2026 |
| Branch | `claude/gracious-volta-c478x8` (not pushed, not merged) |
| Base commit | `9b701bc` |
| Authority applied | SoT v1.1, sha256 `6c1ea6839c041d7d0c1597d2581ccb7ec6e7169e0d51d24712ad341f06068868` |
| Method | Pass 1: audit and plan, approved by the founder. Pass 2: execution under the approved controls. No application code exists in, or was added to, the repository. |

## A. Final repository tree

The archived legacy tree's 174 files are collapsed below. Its layout is unchanged from the old `noema-canonical/`.

```
.
├── .gitignore                      (now ignores .DS_Store)
├── AGENTS.md                       agent operating instructions (new)
├── CLAUDE.md                       imports AGENTS.md (new)
├── README.md                       entry point (replaced)
└── docs/
    ├── NOEMA_SOURCE_OF_TRUTH.md    CANONICAL, v1.1, byte-identical (new)
    ├── README.md                   ownership map (new)
    ├── requirements-index.md       traceability index (new, derived)
    ├── open-decisions.md           AGENT-02 register (new)
    ├── engineering/
    │   ├── boundary-map.md         (new, derived)
    │   └── state-registry.md       (new, derived)
    ├── poc/
    │   └── README.md               POC brief + done checklist (new, derived)
    ├── decisions/
    │   └── README.md               decision-record process (new)
    └── archive/                    NON-AUTHORITATIVE
        ├── README.md               (new)
        ├── migration-2026-10.md    this report (new)
        ├── legacy-canon-2026-09/   former noema-canonical/ (174 .md, each bannered)
        │   ├── CANON.md, CHANGELOG.md, GLOSSARY.md, README.md
        │   └── ai/ architecture/ contracts/ data/ decisions/ engineering/ enterprise/
        │       execution/ graph/ integrations/ intent/ interfaces/ loops/ ontology/
        │       product/ reference-workflows/ strategy/ taxonomy/ thesis/ trust/
        └── source-drafts-2026-09/  4 pre-SoT PDFs
```

## B. File migration report

These are every file that existed before the migration (199 under `noema-canonical/`) plus the root files.

| Old file | Action | Destination | Reason |
|---|---|---|---|
| `README.md` | REPLACE | `README.md` | It held a second definition of Noema ("intent infrastructure layer") and the stale lifecycle. The new README defers to the SoT. |
| `.DS_Store` | REMOVE | n/a | Operating-system junk, tracked by mistake. |
| `.gitignore` (empty) | UPDATE | `.gitignore` | Now ignores `.DS_Store`. |

Each row of the table below carries: old file · purpose · status class (ACTIVE, HISTORICAL, SUPERSEDED, CONTRADICTORY, REDUNDANT or OBSOLETE) · SoT sections that now own the subject · destination · action · reason. Every archived file was moved with `git mv`, so `git log --follow` works.

| Old file | Purpose | Status class | SoT section(s) | Destination | Action | Reason |
|---|---|---|---|---|---|---|
| `noema-canonical/CANON.md` | Repository-level canon: definition, 31 invariants, lifecycle | CONTRADICTORY | §0.1–§13, §45, §55 | docs/archive/legacy-canon-2026-09/CANON.md | ARCHIVE | A competing definition of Noema and a competing invariant set (READY/WAITING/BLOCKED). SoT replaces it entirely. |
| `noema-canonical/CHANGELOG.md` | Changelog of legacy canon | HISTORICAL | App. D | docs/archive/legacy-canon-2026-09/CHANGELOG.md | ARCHIVE | Records the superseded model; history only. |
| `noema-canonical/GLOSSARY.md` | Quick glossary | CONTRADICTORY | App. A | docs/archive/legacy-canon-2026-09/GLOSSARY.md | ARCHIVE | Competing glossary (Trust=READY etc.). App. A is canonical. |
| `noema-canonical/POC/NOEMA POC Specification_1.pdf` | Pre-SoT source draft (PDF) | HISTORICAL / SUPERSEDED | App. D (v1.0, v1.1) | docs/archive/source-drafts-2026-09/NOEMA POC Specification_1.pdf | ARCHIVE | Superseded by SoT v1.0/1.1 (App. D names the Master Company Document and POC Specification as superseded). |
| `noema-canonical/POC/Noema Master Company Document FINAL.pdf` | Pre-SoT source draft (PDF) | HISTORICAL / SUPERSEDED | App. D (v1.0, v1.1) | docs/archive/source-drafts-2026-09/Noema Master Company Document FINAL.pdf | ARCHIVE | Superseded by SoT v1.0/1.1 (App. D names the Master Company Document and POC Specification as superseded). |
| `noema-canonical/POC/Noema_POC_Product_Engineering_Specification_2.pdf` | Pre-SoT source draft (PDF) | HISTORICAL / SUPERSEDED | App. D (v1.0, v1.1) | docs/archive/source-drafts-2026-09/Noema_POC_Product_Engineering_Specification_2.pdf | ARCHIVE | Superseded by SoT v1.0/1.1 (App. D names the Master Company Document and POC Specification as superseded). |
| `noema-canonical/POC/Noema_POC_Product_Engineering_Specification_3.pdf` | Pre-SoT source draft (PDF) | HISTORICAL / SUPERSEDED | App. D (v1.0, v1.1) | docs/archive/source-drafts-2026-09/Noema_POC_Product_Engineering_Specification_3.pdf | ARCHIVE | Superseded by SoT v1.0/1.1 (App. D names the Master Company Document and POC Specification as superseded). |
| `noema-canonical/README.md` | Repository index + definition + invariants | CONTRADICTORY | §0.1–0.6, §1, §51 | docs/archive/legacy-canon-2026-09/README.md | ARCHIVE | Second definition of Noema and stale index; replaced by docs/README.md. |
| `noema-canonical/ai/ai-harness.md` | Model abstraction, AI harness, intent generation, evaluation, AI safety | SUPERSEDED | §17, §20.2 B1/B6, §47, INV-01/02, AGENT-05 | docs/archive/legacy-canon-2026-09/ai/ai-harness.md | ARCHIVE | Model-agnostic interface, schema gate and benchmark gating are in SoT. Evaluation is the Noema Trusted Execution Benchmark (§20.2, §38). |
| `noema-canonical/ai/evaluation.md` | Model abstraction, AI harness, intent generation, evaluation, AI safety | SUPERSEDED | §17, §20.2 B1/B6, §47, INV-01/02, AGENT-05 | docs/archive/legacy-canon-2026-09/ai/evaluation.md | ARCHIVE | Model-agnostic interface, schema gate and benchmark gating are in SoT. Evaluation is the Noema Trusted Execution Benchmark (§20.2, §38). |
| `noema-canonical/ai/intent-generation.md` | Model abstraction, AI harness, intent generation, evaluation, AI safety | SUPERSEDED | §17, §20.2 B1/B6, §47, INV-01/02, AGENT-05 | docs/archive/legacy-canon-2026-09/ai/intent-generation.md | ARCHIVE | Model-agnostic interface, schema gate and benchmark gating are in SoT. Evaluation is the Noema Trusted Execution Benchmark (§20.2, §38). |
| `noema-canonical/ai/model-abstraction.md` | Model abstraction, AI harness, intent generation, evaluation, AI safety | SUPERSEDED | §17, §20.2 B1/B6, §47, INV-01/02, AGENT-05 | docs/archive/legacy-canon-2026-09/ai/model-abstraction.md | ARCHIVE | Model-agnostic interface, schema gate and benchmark gating are in SoT. Evaluation is the Noema Trusted Execution Benchmark (§20.2, §38). |
| `noema-canonical/ai/safety.md` | Model abstraction, AI harness, intent generation, evaluation, AI safety | SUPERSEDED | §17, §20.2 B1/B6, §47, INV-01/02, AGENT-05 | docs/archive/legacy-canon-2026-09/ai/safety.md | ARCHIVE | Model-agnostic interface, schema gate and benchmark gating are in SoT. Evaluation is the Noema Trusted Execution Benchmark (§20.2, §38). |
| `noema-canonical/architecture/action-graph.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/action-graph.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/context-engine.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/context-engine.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/durable-execution.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/durable-execution.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/execution-planner.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/execution-planner.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/execution-record.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/execution-record.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/intent-engine.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/intent-engine.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/operational-memory.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/operational-memory.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/outcome-engine.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/outcome-engine.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/overview.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/overview.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/architecture/trust-engine.md` | Component architecture: Intent/Context/Trust/Outcome Engines, Action Graph, Planner, Durable Execution, Record, Memory | CONTRADICTORY | §13, §14, §16, §17, §35, §43.9, §51 | docs/archive/legacy-canon-2026-09/architecture/trust-engine.md | ARCHIVE | Different component model (Intent Engine, Context Engine, Validation layer, Execution Contracts); Trust returns READY/WAITING/BLOCKED; overview.md mandates Temporal (contradicts §34.5, §35.1, OD-07). |
| `noema-canonical/contracts/action-contract.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/action-contract.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/context-contract.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/context-contract.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/event-contract.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/event-contract.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/execution-contract.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/execution-contract.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/intent-contract.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/intent-contract.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/overview.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/overview.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/trust-contract.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/trust-contract.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/contracts/versioning.md` | Intent/Context/Trust/Action/Execution/Event contracts + versioning | CONTRADICTORY | §43, PLAT-NFR-17, AGENT-15 | docs/archive/legacy-canon-2026-09/contracts/versioning.md | ARCHIVE | Contract set differs from §43.10 primitives; trust-contract uses EXECUTE/CLARIFY/ESCALATE/REJECT (four outcomes, not seven). Canonical schemas belong in /contracts JSON Schemas (code), not prose. |
| `noema-canonical/data/canonical-data.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/canonical-data.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/data/context.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/context.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/data/data-model.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/data-model.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/data/evidence.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/evidence.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/data/persistence.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/persistence.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/data/provenance.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/provenance.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/data/temporal-state.md` | Canonical data, context, evidence, provenance, persistence, temporal state | SUPERSEDED | §14 Evidence Layer, §35.3, §43.5-43.6, §50 | docs/archive/legacy-canon-2026-09/data/temporal-state.md | ARCHIVE | Evidence item and FactStatus now canonical (§43.5); Postgres-only persistence (§35.3). temporal-state.md holds a richer time model than SoT (read_at/effective_at only) -> OPEN/UNOWNED. |
| `noema-canonical/decisions/ADR-001-example.md` | ADR template/example | REDUNDANT | §0.4, §52 | docs/archive/legacy-canon-2026-09/decisions/ADR-001-example.md | ARCHIVE | Template content folded into new decision-log process; example itself archived. |
| `noema-canonical/decisions/ADRs/ADR-001-intent-as-first-class-object.md` | Architecture decision record | SUPERSEDED | §3.1, §13.2, §43.1 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-001-intent-as-first-class-object.md | ARCHIVE | Principle survives as Intent Object (proposal, signed, versioned). |
| `noema-canonical/decisions/ADRs/ADR-002-noema-owns-intent-state-not-business-state.md` | Architecture decision record | SUPERSEDED | §12 (execution-journey record), PLAT-NFR-06 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-002-noema-owns-intent-state-not-business-state.md | ARCHIVE | Reframed: Noema is system of record for the execution journey. |
| `noema-canonical/decisions/ADRs/ADR-003-probabilistic-deterministic-boundary.md` | Architecture decision record | SUPERSEDED | §3, §13, INV-01, INV-02 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-003-probabilistic-deterministic-boundary.md | ARCHIVE | Survives as INV-01/02 and the four-power separation. |
| `noema-canonical/decisions/ADRs/ADR-004-deterministic-trust-evaluation.md` | Architecture decision record | CONTRADICTED IN PART | §13.1, PLAT-NFR-01, INV-21 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-004-deterministic-trust-evaluation.md | ARCHIVE | Determinism survives; READY/WAITING/BLOCKED states replaced by seven outcomes. |
| `noema-canonical/decisions/ADRs/ADR-005-explicit-execution-contracts.md` | Architecture decision record | CONTRADICTED | §13.2, §43.2, §43.8 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-005-explicit-execution-contracts.md | ARCHIVE | Execution Contract replaced by Decision Grant + Capability Descriptor. |
| `noema-canonical/decisions/ADRs/ADR-006-capability-permission-separation.md` | Architecture decision record | SUPERSEDED | §55 #9, three authorisation layers §14 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-006-capability-permission-separation.md | ARCHIVE | Survives as principle 9 and three-layer authorisation. |
| `noema-canonical/decisions/ADRs/ADR-007-enterprise-systems-remain-authoritative.md` | Architecture decision record | SUPERSEDED | §12, §13.3, PLAT-NFR-06 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-007-enterprise-systems-remain-authoritative.md | ARCHIVE | Survives verbatim in spirit. |
| `noema-canonical/decisions/ADRs/ADR-008-clarification-over-guessing.md` | Architecture decision record | SUPERSEDED | §13.3, INV-06, POC-FR-04, OD-03 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-008-clarification-over-guessing.md | ARCHIVE | Survives as CLARIFY + INV-06. |
| `noema-canonical/decisions/ADRs/ADR-009-separate-validation-from-trust.md` | Architecture decision record | CONTRADICTED | §13.1 (schema gate), §43.1 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-009-separate-validation-from-trust.md | ARCHIVE | No separate Validation layer; schema gate at Understanding boundary, Trust checks schema+signature. |
| `noema-canonical/decisions/ADRs/ADR-010-trust-state-machine.md` | Architecture decision record | CONTRADICTED | §13.1, §14 Decision Maker, PLAT-FR-05 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-010-trust-state-machine.md | ARCHIVE | Replaced by seven-outcome decision + grant; trust no longer owns EXECUTING/COMPLETED. |
| `noema-canonical/decisions/ADRs/ADR-011-intent-state-separate-from-execution-state.md` | Architecture decision record | SUPERSEDED | §13, §43.3-43.4 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-011-intent-state-separate-from-execution-state.md | ARCHIVE | Survives (stronger) as four powers with separate objects. |
| `noema-canonical/decisions/ADRs/ADR-012-provenance-and-auditability.md` | Architecture decision record | SUPERSEDED | §13 Record, §43.6, INV-10/11 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-012-provenance-and-auditability.md | ARCHIVE | Replaced by hash-chained causal Record. |
| `noema-canonical/decisions/ADRs/ADR-013-bounded-autonomy.md` | Architecture decision record | SUPERSEDED | §41.1, §18.5, §38.4 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-013-bounded-autonomy.md | ARCHIVE | Replaced by earned-consequence steps and safety-autonomy curve. |
| `noema-canonical/decisions/ADRs/ADR-014-human-intervention-as-explicit-state.md` | Architecture decision record | SUPERSEDED | §13.1 (CLARIFY/CONFIRM/ESCALATE), PLAT-FR-15 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-014-human-intervention-as-explicit-state.md | ARCHIVE | Survives as Trust outcomes + maker-checker. |
| `noema-canonical/decisions/ADRs/ADR-015-fail-closed-on-unknown.md` | Architecture decision record | SUPERSEDED | BD-10, INV-07, INV-16, INV-19, PLAT-NFR-03 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-015-fail-closed-on-unknown.md | ARCHIVE | Survives as invariants. |
| `noema-canonical/decisions/ADRs/ADR-016-consumer-side-authoritative-validation.md` | Architecture decision record | SUPERSEDED | §43.3 REJECTED_BY_TARGET, INV-17 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-016-consumer-side-authoritative-validation.md | ARCHIVE | Survives as target rejection + revalidation. |
| `noema-canonical/decisions/ADRs/ADR-017-outcome-separate-from-trust.md` | Architecture decision record | SUPERSEDED | §13, INV-04, INV-15 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-017-outcome-separate-from-trust.md | ARCHIVE | Survives as Outcome power. |
| `noema-canonical/decisions/ADRs/ADR-018-canonical-repository-authority.md` | Architecture decision record | CONTRADICTED | §0.4, §0.2 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-018-canonical-repository-authority.md | ARCHIVE | Authority order replaced by §0.4; status tags by §0.2; CANON.md no longer the anchor. |
| `noema-canonical/decisions/ADRs/ADR-019-durable-execution-and-workflow-orchestration.md` | Architecture decision record | CONTRADICTED | §34.5, §35.1, §35.3, OD-07 | docs/archive/legacy-canon-2026-09/decisions/ADRs/ADR-019-durable-execution-and-workflow-orchestration.md | ARCHIVE | Proposed Temporal; SoT: Postgres durable state in POC, evaluate Temporal for Phase 3. |
| `noema-canonical/decisions/README.md` | ADR index/process | SUPERSEDED | §0.4, §46, §52 | docs/archive/legacy-canon-2026-09/decisions/README.md (replaced by docs/decisions/README.md) | ARCHIVE + REPLACE | New decision log aligned to BD/OD registers and §52. |
| `noema-canonical/engineering/architecture.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/architecture.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/components.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/components.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/constitution.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/constitution.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/engineering-constitution.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/engineering-constitution.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/failure-recovery.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/failure-recovery.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/idempotency.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/idempotency.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/observability.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/observability.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/reliability.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/reliability.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/runtime.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/runtime.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/scalability.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/scalability.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/security.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/security.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/system-boundaries.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/system-boundaries.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/engineering/testing.md` | Constitution(x2), architecture, components, runtime, reliability, idempotency, observability, scalability, security, boundaries, testing | CONTRADICTORY / REDUNDANT | §35.3, §44-52 | docs/archive/legacy-canon-2026-09/engineering/testing.md | ARCHIVE | Two overlapping "constitutions"; component names conflict with §14/§51; no requirement IDs; stack not stated. SoT Part IX is normative and supersedes. |
| `noema-canonical/enterprise/auditability.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/auditability.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/business-state.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/business-state.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/data-boundaries.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/data-boundaries.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/identity.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/identity.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/organizational-boundaries.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/organizational-boundaries.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/overview.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/overview.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/permissions.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/permissions.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/system-of-record.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/system-of-record.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/enterprise/systems.md` | Enterprise systems, system of record, business state, identity, permissions, audit, data/org boundaries | SUPERSEDED | §11, §12, PLAT-NFR-06, PLAT-FR-16, §47, §50 | docs/archive/legacy-canon-2026-09/enterprise/systems.md | ARCHIVE | Core principle (systems of record stay authoritative) survives in SoT. Examples are internal-employee/HR scenarios, contrary to BD-02 (embedded in customer-facing products). |
| `noema-canonical/execution/action-contracts.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/action-contracts.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/action-model.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/action-model.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/compensation.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/compensation.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/execution-model.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/execution-model.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/failure.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/failure.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/human-intervention.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/human-intervention.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/idempotency.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/idempotency.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/planning.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/planning.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/postconditions.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/postconditions.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/preconditions.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/preconditions.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/execution/retries.md` | Action model/contracts, planning, pre/postconditions, idempotency, retries, failure, compensation, human intervention | SUPERSEDED | §13.2, §14 Execution, §35.5, §43.3, §43.8-43.9, INV-03/07/08/15/17/18 | docs/archive/legacy-canon-2026-09/execution/retries.md | ARCHIVE | "Action Contract"/"Execution Contract" replaced by Capability Descriptor + Decision Grant + Execution Receipt; retries now only under a new grant (AGENT-08). |
| `noema-canonical/graph/capability-model.md` | Enterprise Action Graph, capability model, graph evolution | SUPERSEDED | §14 Execution, §43.8-43.9, INV-18 | docs/archive/legacy-canon-2026-09/graph/capability-model.md | ARCHIVE | Action Graph is data of registered capabilities + evidence reads with a deterministic Planner and plan_hash; old graph docs predate grant/plan binding. |
| `noema-canonical/graph/enterprise-graph.md` | Enterprise Action Graph, capability model, graph evolution | SUPERSEDED | §14 Execution, §43.8-43.9, INV-18 | docs/archive/legacy-canon-2026-09/graph/enterprise-graph.md | ARCHIVE | Action Graph is data of registered capabilities + evidence reads with a deterministic Planner and plan_hash; old graph docs predate grant/plan binding. |
| `noema-canonical/graph/graph-evolution.md` | Enterprise Action Graph, capability model, graph evolution | SUPERSEDED | §14 Execution, §43.8-43.9, INV-18 | docs/archive/legacy-canon-2026-09/graph/graph-evolution.md | ARCHIVE | Action Graph is data of registered capabilities + evidence reads with a deterministic Planner and plan_hash; old graph docs predate grant/plan binding. |
| `noema-canonical/graph/graph-model.md` | Enterprise Action Graph, capability model, graph evolution | SUPERSEDED | §14 Execution, §43.8-43.9, INV-18 | docs/archive/legacy-canon-2026-09/graph/graph-model.md | ARCHIVE | Action Graph is data of registered capabilities + evidence reads with a deterministic Planner and plan_hash; old graph docs predate grant/plan binding. |
| `noema-canonical/integrations/adapters.md` | Integration model, adapters, enterprise capabilities, SDK | SUPERSEDED | §14 utilities, §39, §51 /adapters, AGENT-24, POC-NFR-05 | docs/archive/legacy-canon-2026-09/integrations/adapters.md | ARCHIVE | SDK is a Phase 3 item (§41); POC adapters are synthetic_tushe only. Old docs describe a general SDK as if current. |
| `noema-canonical/integrations/enterprise-capabilities.md` | Integration model, adapters, enterprise capabilities, SDK | SUPERSEDED | §14 utilities, §39, §51 /adapters, AGENT-24, POC-NFR-05 | docs/archive/legacy-canon-2026-09/integrations/enterprise-capabilities.md | ARCHIVE | SDK is a Phase 3 item (§41); POC adapters are synthetic_tushe only. Old docs describe a general SDK as if current. |
| `noema-canonical/integrations/integration-model.md` | Integration model, adapters, enterprise capabilities, SDK | SUPERSEDED | §14 utilities, §39, §51 /adapters, AGENT-24, POC-NFR-05 | docs/archive/legacy-canon-2026-09/integrations/integration-model.md | ARCHIVE | SDK is a Phase 3 item (§41); POC adapters are synthetic_tushe only. Old docs describe a general SDK as if current. |
| `noema-canonical/integrations/sdk.md` | Integration model, adapters, enterprise capabilities, SDK | SUPERSEDED | §14 utilities, §39, §51 /adapters, AGENT-24, POC-NFR-05 | docs/archive/legacy-canon-2026-09/integrations/sdk.md | ARCHIVE | SDK is a Phase 3 item (§41); POC adapters are synthetic_tushe only. Old docs describe a general SDK as if current. |
| `noema-canonical/intent/clarification.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/clarification.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/confidence.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/confidence.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/executable-intent.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/executable-intent.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/intent-ambiguity.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/intent-ambiguity.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/intent-composition.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/intent-composition.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/intent-language.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/intent-language.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/intent-lifecycle.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/intent-lifecycle.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/intent-model.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/intent-model.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/intent/intent-resolution.md` | Intent model, lifecycle, resolution, ambiguity, clarification, confidence, composition | SUPERSEDED | §13.3, §14 Understanding, §43.1, POC-FR-02..04, POC-FR-13 | docs/archive/legacy-canon-2026-09/intent/intent-resolution.md | ARCHIVE | Intent Object now defined in §43.1 (pack nodes, abstract slots, ambiguity_flags, signed). Old lifecycle uses CLARIFICATION_REQUIRED and Validation stages. Intent composition/cancellation is not covered by SoT -> OPEN. |
| `noema-canonical/interfaces/action-api.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/action-api.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/context-api.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/context-api.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/event-model.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/event-model.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/execution-api.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/execution-api.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/integration-model.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/integration-model.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/intent-api.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/intent-api.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/overview.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/overview.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/interfaces/trust-api.md` | Intent/Action/Context/Trust/Execution APIs, event model, integration model | CONTRADICTORY | §39, §43.11, PLAT-FR-12, PLAT-FR-14, OD-15 | docs/archive/legacy-canon-2026-09/interfaces/trust-api.md | ARCHIVE | Defines five public APIs the SoT does not specify (undocumented-API risk). SoT POC integration surface is a single signed listener payload (§39); Mode 2 contract is OD-15, deferred to Phase 4. |
| `noema-canonical/loops/clarification-loop.md` | Clarification loop, execution loop, operational learning | SUPERSEDED | §13.2, §35.2, §14 Operational Memory, §34.5 | docs/archive/legacy-canon-2026-09/loops/clarification-loop.md | ARCHIVE | Loops are now the POC loop (§35.2) and recovery-through-Trust. "Learning from production data" is a POC non-goal (§34.5). |
| `noema-canonical/loops/execution-loop.md` | Clarification loop, execution loop, operational learning | SUPERSEDED | §13.2, §35.2, §14 Operational Memory, §34.5 | docs/archive/legacy-canon-2026-09/loops/execution-loop.md | ARCHIVE | Loops are now the POC loop (§35.2) and recovery-through-Trust. "Learning from production data" is a POC non-goal (§34.5). |
| `noema-canonical/loops/operational-learning.md` | Clarification loop, execution loop, operational learning | SUPERSEDED | §13.2, §35.2, §14 Operational Memory, §34.5 | docs/archive/legacy-canon-2026-09/loops/operational-learning.md | ARCHIVE | Loops are now the POC loop (§35.2) and recovery-through-Trust. "Learning from production data" is a POC non-goal (§34.5). |
| `noema-canonical/loops/overview.md` | Clarification loop, execution loop, operational learning | SUPERSEDED | §13.2, §35.2, §14 Operational Memory, §34.5 | docs/archive/legacy-canon-2026-09/loops/overview.md | ARCHIVE | Loops are now the POC loop (§35.2) and recovery-through-Trust. "Learning from production data" is a POC non-goal (§34.5). |
| `noema-canonical/ontology/action.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/action.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/actor.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/actor.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/capability.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/capability.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/concepts.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/concepts.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/constraint.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/constraint.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/context.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/context.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/entities.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/entities.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/glossary.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/glossary.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/intent.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/intent.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/outcome.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/outcome.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/overview.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/overview.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/policy.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/policy.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/relationships.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/relationships.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/resource.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/resource.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/ontology/state.md` | Abstract concept essays (Intent, Action, Actor, Capability, Policy, State...) | SUPERSEDED | §15.2, §43, App. A | docs/archive/legacy-canon-2026-09/ontology/state.md | ARCHIVE | Ontology is defined by SoT abstract types (§15.2), canonical objects (§43) and glossary (App. A). Old ontology uses Validation/Action Contract/READY vocabulary; a few files cite the superseded POC Spec PDF. |
| `noema-canonical/product/card-renewal.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/product/commercial-wedge.md` | Product, user, interaction, workflow, integration models, commercial wedge | CONTRADICTORY | §9, §11, §18, §19, §30-34 | docs/archive/legacy-canon-2026-09/product/commercial-wedge.md | ARCHIVE | Card-replacement commercial wedge; employee/HR examples (internal tool framing, contra BD-02); no Delegation Curve/experience rules. |
| `noema-canonical/product/enterprise-studio.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/product/first-wedge.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/product/integration-model.md` | Product, user, interaction, workflow, integration models, commercial wedge | CONTRADICTORY | §9, §11, §18, §19, §30-34 | docs/archive/legacy-canon-2026-09/product/integration-model.md | ARCHIVE | Card-replacement commercial wedge; employee/HR examples (internal tool framing, contra BD-02); no Delegation Curve/experience rules. |
| `noema-canonical/product/interaction-model.md` | Product, user, interaction, workflow, integration models, commercial wedge | CONTRADICTORY | §9, §11, §18, §19, §30-34 | docs/archive/legacy-canon-2026-09/product/interaction-model.md | ARCHIVE | Card-replacement commercial wedge; employee/HR examples (internal tool framing, contra BD-02); no Delegation Curve/experience rules. |
| `noema-canonical/product/product-model.md` | Product, user, interaction, workflow, integration models, commercial wedge | CONTRADICTORY | §9, §11, §18, §19, §30-34 | docs/archive/legacy-canon-2026-09/product/product-model.md | ARCHIVE | Card-replacement commercial wedge; employee/HR examples (internal tool framing, contra BD-02); no Delegation Curve/experience rules. |
| `noema-canonical/product/product-thesis.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/product/support-usecases.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/product/user-model.md` | Product, user, interaction, workflow, integration models, commercial wedge | CONTRADICTORY | §9, §11, §18, §19, §30-34 | docs/archive/legacy-canon-2026-09/product/user-model.md | ARCHIVE | Card-replacement commercial wedge; employee/HR examples (internal tool framing, contra BD-02); no Delegation Curve/experience rules. |
| `noema-canonical/product/workflow-model.md` | Product, user, interaction, workflow, integration models, commercial wedge | CONTRADICTORY | §9, §11, §18, §19, §30-34 | docs/archive/legacy-canon-2026-09/product/workflow-model.md | ARCHIVE | Card-replacement commercial wedge; employee/HR examples (internal tool framing, contra BD-02); no Delegation Curve/experience rules. |
| `noema-canonical/reference-workflows/card-renewal/README.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/actions.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/actors.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/context.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/execution.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/failure-modes.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/integrations.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/intents.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/metrics.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/ontology.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/problem.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/card-renewal/trust.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/reference-workflows/customer-account-inquiry/actions.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/actions.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/actors.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/actors.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/context.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/context.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/execution.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/execution.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/failure.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/failure.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/intent.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/intent.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/outcomes.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/outcomes.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/overview.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/overview.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/reference-workflows/customer-account-inquiry/trust.md` | Reference workflow: balance/statement/spending-summary inquiry as "initial commercial wedge" | CONTRADICTORY | §31-34, BD-03 | docs/archive/legacy-canon-2026-09/reference-workflows/customer-account-inquiry/trust.md | ARCHIVE | Declares a different first wedge (account inquiry) than BD-03 (transaction-exception resolution). Cites the superseded POC Spec PDF. |
| `noema-canonical/research/README.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/rfcs/RFC-001-intent-object.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/rfcs/RFC-002-trust-state-machine.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/rfcs/RFC-003-action-graph.md` | Empty placeholder (0 bytes) | OBSOLETE | - | (removed; in Git history) | REMOVE | No content; card-renewal / enterprise-studio / RFC / research placeholders are not canonical. Recoverable from git history. |
| `noema-canonical/strategy/expansion.md` | Wedge, market, positioning, expansion, roadmap | CONTRADICTORY | §19, §22-29, §30-32, §41-42 | docs/archive/legacy-canon-2026-09/strategy/expansion.md | ARCHIVE | Positions Noema as an "Intent Operating System"/"intent-centric control architecture for governed AI execution" (forbidden framing, §12, §25.4); card-replacement wedge; roadmap phases differ from §41 exit gates. |
| `noema-canonical/strategy/market.md` | Wedge, market, positioning, expansion, roadmap | CONTRADICTORY | §19, §22-29, §30-32, §41-42 | docs/archive/legacy-canon-2026-09/strategy/market.md | ARCHIVE | Positions Noema as an "Intent Operating System"/"intent-centric control architecture for governed AI execution" (forbidden framing, §12, §25.4); card-replacement wedge; roadmap phases differ from §41 exit gates. |
| `noema-canonical/strategy/positioning.md` | Wedge, market, positioning, expansion, roadmap | CONTRADICTORY | §19, §22-29, §30-32, §41-42 | docs/archive/legacy-canon-2026-09/strategy/positioning.md | ARCHIVE | Positions Noema as an "Intent Operating System"/"intent-centric control architecture for governed AI execution" (forbidden framing, §12, §25.4); card-replacement wedge; roadmap phases differ from §41 exit gates. |
| `noema-canonical/strategy/roadmap.md` | Wedge, market, positioning, expansion, roadmap | CONTRADICTORY | §19, §22-29, §30-32, §41-42 | docs/archive/legacy-canon-2026-09/strategy/roadmap.md | ARCHIVE | Positions Noema as an "Intent Operating System"/"intent-centric control architecture for governed AI execution" (forbidden framing, §12, §25.4); card-replacement wedge; roadmap phases differ from §41 exit gates. |
| `noema-canonical/strategy/wedge.md` | Wedge, market, positioning, expansion, roadmap | CONTRADICTORY | §19, §22-29, §30-32, §41-42 | docs/archive/legacy-canon-2026-09/strategy/wedge.md | ARCHIVE | Positions Noema as an "Intent Operating System"/"intent-centric control architecture for governed AI execution" (forbidden framing, §12, §25.4); card-replacement wedge; roadmap phases differ from §41 exit gates. |
| `noema-canonical/taxonomy/fintech/intents.md` | Intent/Trust/Outcome taxonomies + fintech instances | CONTRADICTORY | §15, BD-06, POC-FR-15, INV-14 | docs/archive/legacy-canon-2026-09/taxonomy/fintech/intents.md | ARCHIVE | Taxonomies written as classification essays, not abstract schemas loaded as data; fintech taxonomy covers transfers/refunds/cards (money movement) which the POC prohibits (BD-08, §34.2); uses READY/BLOCKED trust states. |
| `noema-canonical/taxonomy/fintech/outcomes.md` | Intent/Trust/Outcome taxonomies + fintech instances | CONTRADICTORY | §15, BD-06, POC-FR-15, INV-14 | docs/archive/legacy-canon-2026-09/taxonomy/fintech/outcomes.md | ARCHIVE | Taxonomies written as classification essays, not abstract schemas loaded as data; fintech taxonomy covers transfers/refunds/cards (money movement) which the POC prohibits (BD-08, §34.2); uses READY/BLOCKED trust states. |
| `noema-canonical/taxonomy/fintech/trust.md` | Intent/Trust/Outcome taxonomies + fintech instances | CONTRADICTORY | §15, BD-06, POC-FR-15, INV-14 | docs/archive/legacy-canon-2026-09/taxonomy/fintech/trust.md | ARCHIVE | Taxonomies written as classification essays, not abstract schemas loaded as data; fintech taxonomy covers transfers/refunds/cards (money movement) which the POC prohibits (BD-08, §34.2); uses READY/BLOCKED trust states. |
| `noema-canonical/taxonomy/intent-taxonomy.md` | Intent/Trust/Outcome taxonomies + fintech instances | CONTRADICTORY | §15, BD-06, POC-FR-15, INV-14 | docs/archive/legacy-canon-2026-09/taxonomy/intent-taxonomy.md | ARCHIVE | Taxonomies written as classification essays, not abstract schemas loaded as data; fintech taxonomy covers transfers/refunds/cards (money movement) which the POC prohibits (BD-08, §34.2); uses READY/BLOCKED trust states. |
| `noema-canonical/taxonomy/outcome-taxonomy.md` | Intent/Trust/Outcome taxonomies + fintech instances | CONTRADICTORY | §15, BD-06, POC-FR-15, INV-14 | docs/archive/legacy-canon-2026-09/taxonomy/outcome-taxonomy.md | ARCHIVE | Taxonomies written as classification essays, not abstract schemas loaded as data; fintech taxonomy covers transfers/refunds/cards (money movement) which the POC prohibits (BD-08, §34.2); uses READY/BLOCKED trust states. |
| `noema-canonical/taxonomy/trust-taxonomy.md` | Intent/Trust/Outcome taxonomies + fintech instances | CONTRADICTORY | §15, BD-06, POC-FR-15, INV-14 | docs/archive/legacy-canon-2026-09/taxonomy/trust-taxonomy.md | ARCHIVE | Taxonomies written as classification essays, not abstract schemas loaded as data; fintech taxonomy covers transfers/refunds/cards (money movement) which the POC prohibits (BD-08, §34.2); uses READY/BLOCKED trust states. |
| `noema-canonical/thesis/non-goals.md` | Company thesis, problem, vision, principles, non-goals (v0.1-0.2) | SUPERSEDED | §1-12, §55, §57 | docs/archive/legacy-canon-2026-09/thesis/non-goals.md | ARCHIVE | Defines Noema as an "intent infrastructure layer"/"semantic execution layer"; no four-power separation, POC fence, Modes, or packs. SoT Parts I-III, X, XI own this. Keeping it active would create a second definition of Noema. |
| `noema-canonical/thesis/principles.md` | Company thesis, problem, vision, principles, non-goals (v0.1-0.2) | SUPERSEDED | §1-12, §55, §57 | docs/archive/legacy-canon-2026-09/thesis/principles.md | ARCHIVE | Defines Noema as an "intent infrastructure layer"/"semantic execution layer"; no four-power separation, POC fence, Modes, or packs. SoT Parts I-III, X, XI own this. Keeping it active would create a second definition of Noema. |
| `noema-canonical/thesis/problem.md` | Company thesis, problem, vision, principles, non-goals (v0.1-0.2) | SUPERSEDED | §1-12, §55, §57 | docs/archive/legacy-canon-2026-09/thesis/problem.md | ARCHIVE | Defines Noema as an "intent infrastructure layer"/"semantic execution layer"; no four-power separation, POC fence, Modes, or packs. SoT Parts I-III, X, XI own this. Keeping it active would create a second definition of Noema. |
| `noema-canonical/thesis/thesis.md` | Company thesis, problem, vision, principles, non-goals (v0.1-0.2) | SUPERSEDED | §1-12, §55, §57 | docs/archive/legacy-canon-2026-09/thesis/thesis.md | ARCHIVE | Defines Noema as an "intent infrastructure layer"/"semantic execution layer"; no four-power separation, POC fence, Modes, or packs. SoT Parts I-III, X, XI own this. Keeping it active would create a second definition of Noema. |
| `noema-canonical/thesis/vision.md` | Company thesis, problem, vision, principles, non-goals (v0.1-0.2) | SUPERSEDED | §1-12, §55, §57 | docs/archive/legacy-canon-2026-09/thesis/vision.md | ARCHIVE | Defines Noema as an "intent infrastructure layer"/"semantic execution layer"; no four-power separation, POC fence, Modes, or packs. SoT Parts I-III, X, XI own this. Keeping it active would create a second definition of Noema. |
| `noema-canonical/thesis/why-noema.md` | Company thesis, problem, vision, principles, non-goals (v0.1-0.2) | SUPERSEDED | §1-12, §55, §57 | docs/archive/legacy-canon-2026-09/thesis/why-noema.md | ARCHIVE | Defines Noema as an "intent infrastructure layer"/"semantic execution layer"; no four-power separation, POC fence, Modes, or packs. SoT Parts I-III, X, XI own this. Keeping it active would create a second definition of Noema. |
| `noema-canonical/trust/ambiguity.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/ambiguity.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/authorization.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/authorization.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/determinism.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/determinism.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/evidence.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/evidence.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/policy-evaluation.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/policy-evaluation.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/risk.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/risk.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/trust-engine.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/trust-engine.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/trust-model.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/trust-model.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/trust-state-machine.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/trust-state-machine.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |
| `noema-canonical/trust/validation.md` | Trust model, engine, state machine, authorization, policy, risk, evidence, validation, ambiguity | CONTRADICTORY | §13.1-13.3, §14 Trust, §43.2, §45, §47 | docs/archive/legacy-canon-2026-09/trust/validation.md | ARCHIVE | Trust State Machine (UNRESOLVED/EVALUATING/WAITING/BLOCKED/READY/EXECUTING/COMPLETED) contradicts seven-outcome Decision Maker + Decision Grant; Trust state machine includes execution states (violates four-power separation). |

## C. New files created

| File | Purpose | SoT sections | Why it exists separately |
|---|---|---|---|
| `docs/NOEMA_SOURCE_OF_TRUTH.md` | The canonical document, unmodified | All | The founder-adopted authority must live in the repository. SoT §51 places it under `/docs`. |
| `README.md` (replaced) | Repository entry point | Front matter, §0.1, §1, §12 | Points readers to the SoT without restating it. |
| `AGENTS.md` | Operating instructions for coding and documentation agents | §0.3, §0.4, §44, §45 | Agents read root instruction files first. This one routes them to the SoT and adds documentation-handling rules for this repository. It adds no product or engineering rules. |
| `CLAUDE.md` | Imports `AGENTS.md` | n/a | Prevents a second, divergent instruction hierarchy. |
| `docs/README.md` | Map of which document owns which question; reading paths; change rules | Front matter (reader table), §0.4 | Navigation and ownership only. It does not define anything. |
| `docs/requirements-index.md` | All 170 SoT IDs, each with section, scope (POC / PLATFORM / ALL), POC mapping and verification | App. B, §0.5, §21, §37, §44–46 | AGENT-01 traceability. Summaries are verbatim SoT prefixes. |
| `docs/open-decisions.md` | Status register for OD-01 to OD-15, plus provisional NON-CANONICAL OD-P-01 to OD-P-12 | §46, AGENT-02 | AGENT-02 names this exact path. |
| `docs/engineering/boundary-map.md` | Per power: components, planned module, may / must-never, enforcing IDs, import rules | §13–17, §43, §45, §47, §51 | One navigable view for security and platform engineers. The architecture itself stays in the SoT. |
| `docs/engineering/state-registry.md` | Every state and status value, with its source section; example-only sets flagged | §0.2, §13.1, §14, §34.3, §35.5, §38.3, §43 | The SoT defines states across six sections; this is a single lookup that stops agents inventing values. |
| `docs/poc/README.md` | POC fence, scope pointers, explicit not-built list, order of work, claims discipline, §40.3 checklist | §30–40 | Product engineers need a working checklist; the definition stays in the SoT. |
| `docs/decisions/README.md` | Decision-record process and template | §0.4, §46, §52 | The founder and engineering decision logs (§0.4) need a home. Replaces the legacy ADR process. |
| `docs/archive/README.md` | Non-authoritative policy, legacy-to-SoT concept map, ADR supersession map, list of removed files | App. D | Keeps the history usable without letting it compete with the SoT. |
| `docs/archive/migration-2026-10.md` | This report | n/a | The record the founder requested. |

**Deliberately not created:**

- separate thesis, ontology, glossary, trust, execution, contracts, security, taxonomy or Intent Computing documents (the SoT owns each in one place, and copies would become competing definitions);
- JSON Schemas (§43 gives example shapes, not complete schemas);
- `/core`, `/contracts` and the other implementation directories (OD-P-01);
- RFC or research directories (nothing to put in them);
- replacements for the 21 empty placeholders.

## D. Files archived and removed

- **Archived, 178 files, all with `git mv`:**
  - 174 Markdown files to `docs/archive/legacy-canon-2026-09/` (each now opens with a NON-AUTHORITATIVE banner: 2 lines added per file, content otherwise unchanged);
  - 4 PDFs to `docs/archive/source-drafts-2026-09/`.

  Replacements: the SoT, plus the derived documents in §C.
- **Removed from the active tree, 22 files.** All are recoverable from Git history at `9b701bc`. None is recreated, because the SoT requires none of them.

| Removed | Reason | Replacement |
|---|---|---|
| `noema-canonical/reference-workflows/card-renewal/{README,actions,actors,context,execution,failure-modes,integrations,intents,metrics,ontology,problem,trust}.md` (12) | 0 bytes; the card-renewal wedge is not canonical (BD-03) | None. The POC wedge is defined in SoT §31–34. |
| `noema-canonical/product/{card-renewal,enterprise-studio,first-wedge,product-thesis,support-usecases}.md` (5) | 0 bytes | None. Studio is PLAT-FR-17 / Phase 3; the wedge is BD-03; the product thesis is SoT Part III. |
| `noema-canonical/research/README.md` (1) | 0 bytes | None. External evidence lives in SoT App. C under the rules in §0.6. |
| `noema-canonical/rfcs/RFC-00{1,2,3}-*.md` (3) | 0 bytes | None. Changes go through SoT revision, decision records or open decisions. |
| `.DS_Store` (1) | Operating-system junk | None; now ignored. |

## E. Contradiction resolution report

Format: old statement → canonical statement → affected files (all now archived) → resolution.

1. **Definition of Noema.**
   - Old: "intent infrastructure layer"; "deterministic intent-to-action boundary"; "general-purpose semantic execution layer"; "Intent Operating System"; "intent-centric control architecture for governed AI execution".
   - Canonical: trusted execution infrastructure for consequential action. It is not a control plane, agent framework or intent-conversion API (SoT §1, §12, §57).
   - Affected: `README.md`, `noema-canonical/README.md`, `CANON.md`, `thesis/*`, `strategy/{wedge,market,roadmap,positioning}.md`.
   - Resolution: archived. The only active definition is the SoT, and every active document points to §1/§12.
2. **Intent Computing.**
   - Old: not named. "Intent as a first-class computational primitive" was presented as the product thesis.
   - Canonical: Intent Computing is the paradigm; trusted execution infrastructure is the category and the company (§3.1).
   - Affected: `thesis/thesis.md`, ADR-001.
   - Resolution: archived. The SoT is the sole definition.
3. **Architecture and lifecycle.**
   - Old: Intent → Resolution → Validation → Trust → Contract → Execution → Outcome; Intent, Context and Outcome Engines; a separate AI Layer.
   - Canonical: four separate powers (Understanding → Trust → Execution → Outcome) plus an independent Record (§13, §14).
   - Affected: `architecture/*`, `engineering/{architecture,components,system-boundaries}.md`, `CANON.md`, `loops/*`, all taxonomy files.
   - Resolution: archived. Navigation aid: `docs/engineering/boundary-map.md`.
4. **Trust model.**
   - Old: a Trust State Machine (UNRESOLVED / EVALUATING / WAITING / BLOCKED / READY → EXECUTING → COMPLETED / FAILED), with "No direct WAITING → READY" rules.
   - Canonical: exactly one of seven outcomes (`ALLOW`, `CLARIFY`, `CONFIRM`, `WAIT`, `ESCALATE`, `REJECT`, `UNKNOWN`). A single-use Decision Grant only on `ALLOW`. Trust cannot execute (§13.1, §14, PLAT-FR-05, PLAT-FR-07).
   - Affected: `trust/*`, `architecture/trust-engine.md`, `CANON.md`, `GLOSSARY.md`, ADR-004, ADR-010, ADR-015, `taxonomy/{trust-taxonomy,fintech/trust}.md`.
   - Resolution: archived. Lookup: `docs/engineering/state-registry.md` §2.
5. **Trust contract outcomes.**
   - Old: EXECUTE / CLARIFY / ESCALATE / REJECT.
   - Canonical: the seven outcomes above.
   - Affected: `contracts/trust-contract.md`, `interfaces/trust-api.md`.
   - Resolution: archived.
6. **Validation layer.**
   - Old: a separate deterministic layer (VALID / INVALID / INCOMPLETE / UNKNOWN).
   - Canonical: a schema gate at the Understanding boundary; Trust checks schema and signature (§13.1, §43.1, INV-02).
   - Affected: `trust/validation.md`, ADR-009, ADR-016, `CANON.md`.
   - Resolution: archived.
7. **Canonical contract.**
   - Old: Action Contracts and Execution Contracts.
   - Canonical: Capability Descriptor, Decision Grant, Execution Receipt and Outcome Verdict, among the §43.10 primitives.
   - Affected: `contracts/*`, `execution/action-contracts.md`, ADR-005, `engineering/*`.
   - Resolution: archived. No schemas were invented (OD-P-01, OD-P-06, OD-P-08).
8. **Execution semantics.**
   - Old: retries governed by a contract retry budget, inside execution.
   - Canonical: a timeout or silence is `OUTCOME_UNKNOWN`; a write is retried only under a new grant after verification; recovery goes only through Trust (§13.2, §35.5, INV-07, INV-15, AGENT-08).
   - Affected: `execution/{retries,failure,idempotency}.md`, `engineering/{idempotency,failure-recovery}.md`, `contracts/execution-contract.md`.
   - Resolution: archived.
9. **Outcome semantics.**
   - Old: PENDING / COMPLETED / FAILED / PARTIALLY_COMPLETED / UNKNOWN / CANCELLED; execution records "Completed".
   - Canonical: Verdict `ACHIEVED` / `NOT_ACHIEVED` / `PARTIALLY_ACHIEVED` / `PENDING_EXTERNAL` / `UNKNOWN` / `COMPENSATED`. Execution never writes `SUCCEEDED` (§43.3–43.4, INV-04).
   - Affected: `architecture/{outcome-engine,execution-record}.md`, `taxonomy/{outcome-taxonomy,fintech/outcomes}.md`.
   - Resolution: archived.
10. **Durable execution.**
    - Old: "Noema should use Temporal" (architecture overview); Temporal "selected as the preferred implementation" (ADR-019, Proposed).
    - Canonical: no Temporal in the POC. Postgres is the only authoritative store; Temporal is evaluated for Phase 3 (§34.5, §35.1, §35.3, OD-07).
    - Affected: `architecture/{overview,execution-planner,durable-execution}.md`, ADR-019.
    - Resolution: archived. Stated in `docs/poc/README.md` and `docs/engineering/boundary-map.md`.
11. **First wedge.**
    - Old: card replacement (`strategy/wedge.md`, `product/commercial-wedge.md`, examples throughout); customer account inquiry, described as "Noema's initial commercial wedge" (`reference-workflows/customer-account-inquiry/*`).
    - Canonical: voice-fronted transaction-exception resolution in Nigerian fintech, "Where is my money?" (BD-03, §31–34).
    - Resolution: archived; empty card-renewal stubs removed. `docs/poc/README.md` names the canonical wedge and explicitly rejects the other two.
12. **Taxonomies.**
    - Old: classification essays; a fintech taxonomy including TRANSFER_FUNDS, refunds and card operations; READY/BLOCKED trust states.
    - Canonical: three abstract schemas loaded as data; the fintech pack holds only POC nodes; telecom, insurance and healthcare-admin conformance packs are skeletal; no money movement in the POC (§15, BD-06, BD-08, INV-14).
    - Affected: `taxonomy/*`.
    - Resolution: archived. No taxonomy content was written, because pack content is data to be authored with the build (§15.6).
13. **Public interfaces.**
    - Old: five public APIs (Intent, Action, Context, Trust, Execution) plus an event model, presented as the Noema interface layer.
    - Canonical: not specified. The SoT defines the canonical input contract (PLAT-FR-01), the reconstruction API (PLAT-FR-12), the POC listener payload (§39), and Mode 2 as OD-15 (Phase 4).
    - Affected: `interfaces/*`, `integrations/sdk.md`.
    - Resolution: archived. `docs/engineering/boundary-map.md` states this.
14. **Who Noema is for.**
    - Old: internal employee, HR and finance-team examples.
    - Canonical: embedded in enterprises' customer-facing products for their customers (BD-02, §11).
    - Affected: `product/{product-model,user-model,integration-model}.md`, `enterprise/*`.
    - Resolution: archived.
15. **Authority and governance.**
    - Old: Canon > Specification > Architecture > ADR > Research > Reference > Strategy (ADR-018, both READMEs); `CANON.md` as the anchor.
    - Canonical: SoT §0.4 order of authority; §0.2 status tags; the §46 open-decisions process.
    - Resolution: archived. Restated only by reference in `AGENTS.md` and `docs/README.md`.
16. **Roadmap.**
    - Old: phases "Semantic → Capability → Contract → Domain → Deployment → Ecosystem → Operational optimisation"; horizon "Intent Operating System".
    - Canonical: Phases 0–6 with evidence-based exit gates, the founder year map, and the industry, region and modality sequence (§41–42).
    - Affected: `strategy/{roadmap,expansion}.md`.
    - Resolution: archived.
17. **Operational Memory.**
    - Old: "historical intent and execution record", with a learning loop (`loops/operational-learning.md`).
    - Canonical: a structured record of operational reality, versioned and reversible, never a free-form instruction store. Learning from production data is a POC non-goal (§14, §34.5).
    - Resolution: archived.
18. **Invariant sets.**
    - Old: 31 unnumbered invariants (`CANON.md`, `noema-canonical/README.md`) plus per-ADR invariant lists.
    - Canonical: INV-01 to INV-22 (§45).
    - Resolution: archived. The index lists INV-01 to INV-22.
19. **Market and number claims.**
    - The audit found no stale TAM or market figures. Dollar amounts in legacy documents are illustrative policy-threshold examples only. No number was carried into active documentation (AGENT-18).

## F. Requirement traceability report

| Category | Result |
|---|---|
| **Preserved** | All 170 SoT IDs, spelled exactly as in the SoT: BD-01 to BD-15, PLAT-FR-01 to PLAT-FR-17, PLAT-NFR-01 to PLAT-NFR-21, PLAT-US-01 to PLAT-US-11, POC-FR-01 to POC-FR-17, POC-NFR-01 to POC-NFR-10, US-01 to US-16, INV-01 to INV-22, AGENT-01 to AGENT-26, OD-01 to OD-15. Also the families B1–B8, S0–S3 and AT-01 to AT-20 (range only). Every one appears in `requirements-index.md` (OD-xx in `open-decisions.md`). |
| **Migrated from legacy** | None. The legacy documents contained no requirement IDs. |
| **Consolidated** | None. No IDs were merged or renamed. |
| **Superseded** | Legacy unnumbered invariants (31 in `CANON.md`, plus ADR invariant lists) are superseded by INV-01 to INV-22 and the binding decisions. The legacy ADR-001 to ADR-019 are mapped in `archive/README.md`. |
| **Unresolved** | The `SEC-` and `PERF-` prefixes are named in §0.3 but no IDs exist (OD-P-07). AT-01 to AT-20 are defined in the absent Tushe specification (OD-P-03). POC-FR-17 has no platform mapping (OD-P-11). Unowned legacy concepts are listed in OD-P-12 and are not requirements. |
| **New IDs** | None canonical. The provisional OD-P-01 to OD-P-12 are NON-CANONICAL migration identifiers. |

## G. Open decisions

All are in [`../open-decisions.md`](../open-decisions.md).

- **Canonical:** OD-01 to OD-15. Unchanged; defaults apply.
- **Provisional, NON-CANONICAL:**

| ID | Subject | Needs founder input? |
|---|---|---|
| OD-P-01 | Repository layout: documentation-first or monorepo per §51 | Yes |
| OD-P-02 | Founder decision log and engineering decision log not in the repository | Yes |
| OD-P-03 | Tushe specification v1.0 absent (AT-01 to AT-20, scenario pack, lifecycle transitions); blocks Phase A exit | Yes, please add the document |
| OD-P-04 | Runbooks (kill switch, incident playbook) absent; needed before Phase 2 | Later |
| OD-P-05 | Founding Canon v4.0, POC Spec v2.0 and peer drafts not in the archive | Optional |
| OD-P-06 | Intent Object `status` values not enumerated | Yes, before the contracts v1 freeze |
| OD-P-07 | `SEC-` / `PERF-` prefixes named but undefined | Yes |
| OD-P-08 | Authority-layer result values and reason-code set not enumerated | Yes, before the contracts v1 freeze |
| OD-P-09 | Canonical risk-class set and core-vs-pack ownership | Yes |
| OD-P-10 | Look-alike names (`OUTCOME_UNKNOWN` / `EXECUTION_OUTCOME_UNKNOWN`; severity S0–S3 vs sensitivity S3/S4) | Optional renaming |
| OD-P-11 | POC-FR-17 has no platform mapping | Optional |
| OD-P-12 | Unowned legacy concepts (composite intents, cancellation and expiry, temporal model, contract-version lifecycle, event semantics, org hierarchy) | Decide case by case |

None of these was resolved by guessing. Where a "proposed default" is given, it is the smallest safe reading and is labelled as a proposal.

## H. Broken references

- **Active documentation:** none. Every Markdown link and every backtick file path in active documents resolves (see §J). References to the 21 removed placeholders are written as removal records, and the decision-record filename pattern is a naming template.
- **Archived documentation:** archived files keep their original plain-text cross-references (for example `trust/trust-model.md`). Because the tree moved as a whole, these still resolve relative to `docs/archive/legacy-canon-2026-09/`. The exceptions are references to the 21 removed placeholders (for example `reference-workflows/card-renewal/`), which now point at files that exist only in Git history. This is intentional; archived content was not edited beyond the banner.
- **External references with no file in the repository:** the Tushe specification (OD-P-03), the founder and engineering decision logs (OD-P-02), runbooks (OD-P-04), Founding Canon v4.0 and the peer drafts (OD-P-05).

## I. Semantic consistency audit

I reviewed every active document by reading it, not only with string search. Each answer below is single and authoritative:

| Question | Single authoritative answer | Active documents that only point to it |
|---|---|---|
| What Noema is / is not | SoT §1, §12, §57 | README, docs/README, AGENTS |
| Intent Computing | SoT §3.1 | docs/README |
| Canonical architecture | SoT §13–17 | boundary-map (derived) |
| POC definition | SoT Part VII | poc/README (derived) |
| POC vs platform boundary | SoT §30, BD-04 | poc/README, requirements-index (scope column) |
| First wedge | BD-03, SoT §31 | poc/README |
| Mode 1 / Mode 2 | SoT §16 | boundary-map, state-registry |
| Intent / Trust / Outcome Taxonomies | SoT §15 | boundary-map (packs row) |
| Canonical contracts | SoT §43 | boundary-map, state-registry |
| State semantics, trust outcomes, execution semantics, outcome semantics | SoT §13.1, §35.5, §43 | state-registry (derived lookup) |
| Requirement IDs | SoT (App. B) | requirements-index |
| Status tags | SoT §0.2 | state-registry §1 (copied table, attributed) |
| Coding-agent rules | SoT §44 | AGENTS.md (pointer list) |
| Open-decision process | SoT §46, AGENT-02 | open-decisions, decisions/README |

The checks performed:

- **Separation of powers.** No active document lets one power do another's job. The boundary map lists each power's prohibitions verbatim from §13.1 and §13.3.
- **No framing as fintech, Nigerian, voice or chatbot.** No active document describes Noema that way. Every Nigeria, fintech and voice mention sits inside an explicitly labelled POC context or a BD citation.
- **No future capability presented as current.** Mode 2, Studio, the SDK, monetary capabilities and Temporal all appear only as deferred or not built.
- **No status upgrades.** No HYPOTHESIS, TARGET or ILLUSTRATIVE item is restated as fact, achieved or planned. The 73% and 89% figures are explicitly marked [HYPOTHESIS].
- **Stale-term hits.** Every remaining hit in active documents is in a supersession, negation or contrast context (listed in §J, check 7). Examples: "Do not implement … READY / WAITING / BLOCKED" in AGENTS.md; "Not a POC requirement: … Temporal" in boundary-map.md; the OD-07 row in open-decisions.md, which quotes the SoT.
- **Two issues found and fixed during the review:**
  - The archive README described the two POC-spec PDFs as "two copies"; they are distinct files. Corrected.
  - The SoT's `/docs/open-decisions.md` absolute path is now resolved by the validator as `docs/open-decisions.md`.

## J. Validation results

Checks were run with a standard-library Python script kept outside the repository, because adding tooling would need an [OPEN] entry under AGENT-14. The output from the final run follows.

```
== 1. SoT byte identity
  upload 6c1ea6839c041d7d0c1597d2581ccb7ec6e7169e0d51d24712ad341f06068868 
  repo   6c1ea6839c041d7d0c1597d2581ccb7ec6e7169e0d51d24712ad341f06068868 
   IDENTICAL
== 2. Markdown links in active docs
  checked 72 links
== 3. Backtick path references in active docs
  checked 323 path refs (of which 197 distinct former noema-canonical/ paths verified against base commit 9b701bc)
== 4. Requirement IDs
  IDs used in derived docs: 172 | not in SoT: []
  SoT IDs missing from index/register: []
== 5. Section references (§) in derived docs exist in SoT
  bad: []
== 6. Duplicate headings within a file
== 7. Stale-term hits in active derived docs (for semantic review)
  AGENTS.md:19: [READY]
  AGENTS.md:19: [WAITING]
  AGENTS.md:19: [BLOCKED]
  AGENTS.md:19: [Action Contract]
  AGENTS.md:19: [Validation layer]
  AGENTS.md:19: [intent infrastructure]
  AGENTS.md:19: [Intent OS]
  AGENTS.md:19: [card-replacement]
  AGENTS.md:19: [Temporal]
  AGENTS.md:44: [Temporal]
  docs/archive/README.md:15: [noema-canonical]
  docs/archive/README.md:27: [intent infrastructure]
  docs/archive/README.md:27: [Intent Operating System]
  docs/archive/README.md:29: [Trust State Machine]
  docs/archive/README.md:29: [WAITING]
  docs/archive/README.md:29: [BLOCKED]
  docs/archive/README.md:29: [READY]
  docs/archive/README.md:30: [Validation layer]
  docs/archive/README.md:31: [Action Contract]
  docs/archive/README.md:31: [Execution Contract]
  docs/archive/README.md:33: [Temporal]
  docs/archive/README.md:33: [Temporal]
  docs/archive/README.md:34: [account inquiry]
  docs/archive/README.md:39: [Intent OS]
  docs/archive/README.md:50: [READY]
  docs/archive/README.md:50: [WAITING]
  docs/archive/README.md:50: [BLOCKED]
  docs/archive/README.md:55: [Validation layer]
  docs/archive/README.md:72: [card-renewal]
  docs/archive/README.md:72: [card-renewal]
  docs/archive/README.md:73: [card-renewal]
  docs/engineering/boundary-map.md:69: [Temporal]
  docs/engineering/boundary-map.md:69: [Temporal]
  docs/engineering/state-registry.md:43: [READY]
  docs/engineering/state-registry.md:43: [WAITING]
  docs/engineering/state-registry.md:43: [BLOCKED]
  docs/engineering/state-registry.md:43: [CLARIFICATION_REQUIRED]
  docs/open-decisions.md:39: [Temporal]
  docs/poc/README.md:17: [account inquiry]
  docs/poc/README.md:59: [Temporal]
  docs/poc/README.md:59: [Temporal]
  (plus 493 hits inside this report itself: the historical file table in §B and the contradiction list in §E)
== 8. Archive banner coverage
  files without banner: []
RESULT: failures = 0
```

How to read the output:

- Check 3 counts backtick path references. Intentional names (the removed placeholders and the decision-record filename template) are allow-listed.
- Check 7 is informational. It lists every stale-term occurrence in active documents so that each can be confirmed to be a negation or contrast, which it is (§I).
- Failures must be 0.

## K. Git diff summary

| Commit | Content |
|---|---|
| `4fd11cd` | Archive the legacy tree and pre-SoT PDFs (178 renames). Remove 21 empty placeholders and `.DS_Store`. Update `.gitignore`. |
| `bb13ce0` | Prepend the NON-AUTHORITATIVE banner to 174 archived Markdown files (+349 lines, 0 removed). |
| `8047171` | Add the SoT copy, AGENTS.md, CLAUDE.md, and the derived documents in `docs/`. Replace README.md. |
| (this commit) | Add this report. |

Totals from `9b701bc` to `8047171`:

- 213 files changed: 178 renamed, 22 deleted, 11 added, 2 modified (`README.md`, `.gitignore`).
- 4,197 insertions and 107 deletions.
  - 2,742 of the insertions are the verbatim SoT.
  - 349 are archive banners.
  - About 1,106 are new derived documentation and instructions.
  - The 107 deletions are the replaced root README and the old `.gitignore` state.
- No application code, infrastructure, CI/CD or deployment configuration was touched. None exists in the repository.
- Nothing was pushed or merged.

## L. Residual risks and items requiring founder approval

1. **Founder approval needed** for OD-P-01 (repository layout), OD-P-03 (add the Tushe specification; this blocks Phase A exit), OD-P-06 and OD-P-08 (enumerations needed before the contracts v1 freeze), OD-P-07 (SEC-/PERF- IDs) and OD-P-09 (risk classes). Each may need a SoT revision (v1.2).
2. **Drift risk in derived documents.**
   - `requirements-index.md`, `docs/engineering/state-registry.md` and `poc/README.md` copy short SoT text. A future SoT revision must be followed by regenerating or rechecking them.
   - Recommended: add the validator to CI once a tooling decision is recorded (AGENT-14).
3. **Archive misuse risk.** Search tools will still surface archived files. The per-file banner, the archive README and AGENTS.md all mark them as non-authoritative, but agents that ignore headers could still quote them. Deleting the archive later (it remains in Git history) is an option for the founders.
4. **Knowledge not in the SoT.** Some legacy reasoning (OD-P-12) is preserved only in the archive. If any of it matters for the POC, it must be raised through AGENT-02 rather than read from the archive.
5. **External-source gaps.** The SoT relies on documents that are not in the repository (OD-P-02 to OD-P-05). Until they are added, the §0.4 order of authority cannot be applied in full from this repository alone.
6. **Branch state.** All work is on `claude/gracious-volta-c478x8`, committed locally and not pushed. If the container is reclaimed before a push, the commits will be lost. Pushing requires your explicit instruction.
