# Noema Canonical Repository

Status: Foundational
Version: 0.2
Canonical Path: README.md

⸻

## 1. What This Repository Is

This is the canonical documentation and specification repository for Noema.

It defines what Noema is, what it owns, what it does not own, how it works, what it refuses to do, and why every architectural decision was made.

Everything here is authoritative until explicitly superseded by a newer version of the same document with a recorded reason for the change.

⸻

## 2. The Noema Thesis in One Sentence

> Noema is the deterministic intent-to-action boundary that transforms probabilistically understood human Intent into validated, trusted, and contractually executable Actions across existing systems while preserving explicit authority, contextual governance, provenance, and ownership of business truth.

⸻

## 3. The Core Claim

Software has historically required people to translate what they want into the language of software: forms, API calls, workflows, menus.

Noema reverses this relationship.

The Actor expresses what they want. Noema resolves that expression into a canonical Intent, acquires the context and evidence required to evaluate it, validates its structure and applicability, evaluates whether its Trust requirements are satisfied, and maps the trusted Intent onto executable Capabilities exposed by systems that can fulfil it.

The enterprise application remains authoritative for its domain.

Noema becomes responsible for the intent-to-action boundary.

⸻

## 4. What Noema Owns

Noema owns Intent state and the state associated with its intent-to-action lifecycle. This includes:

- expressed Intent representation
- Intent interpretation and resolution
- ambiguity and clarification state
- contextualized Intent and constraints
- Intent provenance
- Validation state
- Trust requirements and Trust state
- Trust evaluation history
- execution eligibility determination
- Action selection
- Execution Contract state
- execution coordination state
- provenance of decisions made by Noema
- the relationship between Intent and executable Actions

**Noema does not own the authoritative business state of the systems it operates against.**

> Noema owns Intent state, not business state.

This is a foundational architectural boundary.

⸻

## 5. The Canonical Lifecycle

```
EXPRESS
   ↓
INTERPRET
   ↓
RESOLVE
   ↓
CONTEXTUALIZE
   ↓
VALIDATE
   ↓
EVALUATE TRUST
   ↓
PLAN / SELECT ACTION
   ↓
CONTRACT
   ↓
EXECUTE
   ↓
VERIFY
   ↓
OUTCOME
```

At any point where Noema cannot safely proceed, the lifecycle transitions to:

```
CLARIFY  →  (return to resolution)
WAIT     →  (await required condition)
BLOCK    →  (prohibited by policy or authority)
ESCALATE →  (human intervention required)
```

The system must not skip a required state to produce an apparently successful outcome.

⸻

## 6. The Probabilistic / Deterministic Boundary

This boundary is the most important architectural invariant in the system.

```
PROBABILISTIC ZONE
──────────────────────────────────────
Language understanding
Candidate intent interpretation
Entity resolution candidates
Semantic retrieval
Candidate plan generation
──────────────────────────────────────
         HARD SCHEMA BOUNDARY
──────────────────────────────────────
DETERMINISTIC ZONE
Validation
Resolution
Trust evaluation
Execution eligibility
Action Contracts
Execution
Outcome verification
Provenance
```

The Model proposes. Noema decides.

Model confidence is not execution authority. A high-confidence model interpretation may still result in Trust = BLOCKED, WAITING, or CLARIFICATION_REQUIRED. Confidence and Trust are separate concepts.

⸻

## 7. Core Architectural Invariants

| # | Invariant |
|---|-----------|
| 1 | Noema owns Intent state, not authoritative business state. |
| 2 | Human language is input to Intent resolution, not the executable representation of Intent. |
| 3 | Model confidence is not execution authority. |
| 4 | Noema must not guess when Intent semantics are materially ambiguous. |
| 5 | Resolution, Validation, Trust, and Execution are distinct semantic layers. |
| 6 | Validation is deterministic. |
| 7 | Unknown information must not be treated as established information. |
| 8 | Trust evaluation is deterministic with respect to its governing inputs and versions. |
| 9 | Unknown mandatory Trust conditions cannot produce READY. |
| 10 | Authorization does not imply Trust. |
| 11 | Policy satisfaction does not imply Trust. |
| 12 | Capability availability does not imply Trust. |
| 13 | Risk acceptance does not imply Trust. |
| 14 | Validation does not authorize or execute Actions. |
| 15 | Execution occurs only through explicit Capabilities and Contracts. |
| 16 | Capability and permission are distinct. |
| 17 | Autonomy is bounded by explicit authority, Policy, Capability, and Contract. |
| 18 | WAITING and BLOCKED are semantically distinct states. |
| 19 | Material changes to Trust inputs require re-evaluation. |
| 20 | Material Intent changes require a new or re-established Trust evaluation. |
| 21 | Trust decisions must be traceable to their inputs, requirements, rules, and Evidence. |
| 22 | READY does not guarantee execution success. |
| 23 | Execution outcomes do not retroactively establish that a Trust decision was valid. |
| 24 | Enterprise systems remain authoritative for their business domains. |
| 25 | Human intervention is a valid lifecycle state. |
| 26 | Important execution conditions must be represented as explicit state. |
| 27 | The conversational interface is not the Noema abstraction. |
| 28 | Noema must fail closed for consequential execution when mandatory conditions cannot be established. |
| 29 | Fail-closed uncertainty may result in WAITING rather than permanent denial where the condition is recoverable. |
| 30 | Research may challenge the Canon but does not become Canon automatically. |
| 31 | Canonical concepts must have precise, stable definitions. |

⸻

## 8. Key Distinctions

These pairs are not interchangeable. Conflating them violates the architecture.

| These are NOT the same | Why it matters |
|---|---|
| Intent ≠ Action | Intent describes what the Actor wants. Action describes what the system executes. |
| Resolution ≠ Validation | Resolution determines meaning. Validation determines correctness. |
| Validation ≠ Trust | A valid Intent may remain blocked by policy or authority. |
| Trust ≠ Authorization | Authorization is one dimension of Trust, not a substitute for it. |
| Trust ≠ Confidence | Model confidence is probabilistic. Trust is a deterministic decision boundary. |
| Capability ≠ Permission | A system can possess a Capability without the Actor having authority to invoke it. |
| Execution ≠ Outcome | Execution is the attempt. Outcome is the verified result after postcondition evaluation. |
| Business State ≠ Intent State | Enterprise systems own business state. Noema owns Intent and execution state. |
| WAITING ≠ BLOCKED | WAITING = not yet. BLOCKED = prohibited. |
| READY ≠ SUCCESS | Trust READY means eligible to execute. It does not guarantee success. |
| Approval ≠ Authorization | Authorization establishes Actor authority. Approval satisfies an explicit approval requirement. |
| Confirmation ≠ Approval | Confirmation is the Actor confirming the Action. Approval is a separate authority requirement. |

⸻

## 9. Architecture Components

| Component | Responsibility |
|---|---|
| Intent Engine | Transforms human expression into a canonical, resolved Intent. May use AI. Does not determine execution authority. |
| Context Engine | Acquires and scopes the information required to interpret, validate, and evaluate an Intent. Does not own enterprise business state. |
| Validation | Deterministically evaluates whether the resolved Intent is structurally complete and valid for its next lifecycle transition. |
| Trust Engine | Evaluates whether all conditions (authorization, policy, risk, capability, constraints, evidence) have been satisfied for execution eligibility. Returns READY, WAITING, BLOCKED, or CLARIFICATION_REQUIRED. |
| Action Graph | Represents the available enterprise capabilities and their dependencies as a traversable graph. |
| Execution Planner | Determines what sequence or composition of Actions can satisfy a trusted Intent. Does not create authority. |
| Execution Contract | The explicit, typed contract governing what an Action may do, require, and guarantee. |
| Durable Execution | Maintains Noema's execution lifecycle across time, retries, failures, approvals, and external events. |
| Execution Record | The immutable record of all execution attempts, their outcomes, and their evidence. |
| Outcome Engine | Determines whether the observed result of execution satisfies the expected postconditions. Establishes the canonical Outcome. |
| Operational Memory | The historical intent and execution record for auditability and reconciliation. Does not assert business truth. |
| AI Layer | Probabilistic components for interpretation, classification, entity resolution, and retrieval. Operates upstream of the deterministic Trust boundary. |

⸻

## 10. Repository Structure

### Foundational

| Path | Purpose |
|---|---|
| `CANON.md` | The canonical principles, invariants, and foundational distinctions. Authoritative. |
| `GLOSSARY.md` | Quick-reference glossary of canonical terms. |
| `CHANGELOG.md` | Record of significant changes to the canonical documentation. |

### Thesis

| Path | Purpose |
|---|---|
| `thesis/thesis.md` | The full Noema thesis: problem, claim, and implied architecture. |
| `thesis/principles.md` | Design principles governing Noema's architecture and evolution. |
| `thesis/vision.md` | Long-term vision and direction. |
| `thesis/problem.md` | The problem Noema addresses. |
| `thesis/non-goals.md` | What Noema explicitly does not do. |
| `thesis/why-noema.md` | Why a new layer is needed. |

### Ontology

| Path | Purpose |
|---|---|
| `ontology/overview.md` | Overview of the Noema ontological vocabulary. |
| `ontology/glossary.md` | Full canonical glossary with detailed definitions. |
| `ontology/concepts.md` | Abstract semantic concepts. |
| `ontology/entities.md` | Entity semantics and types. |
| `ontology/intent.md` | Intent as a canonical object. |
| `ontology/action.md` | Action semantics. |
| `ontology/actor.md` | Actor semantics. |
| `ontology/capability.md` | Capability: what the system can do, distinct from what it is permitted to do. |
| `ontology/context.md` | Context semantics and governance. |
| `ontology/constraint.md` | Constraint: explicit boundaries on permissible behaviour. |
| `ontology/policy.md` | Policy: governing rules for eligibility and permissibility. |
| `ontology/resource.md` | Resource: Entities as objects of Actions. |
| `ontology/state.md` | State: conditions of Entities and systems. |
| `ontology/outcome.md` | Outcome: verified results of executed Actions. |
| `ontology/relationships.md` | How ontological concepts relate to each other. |

### Architecture

| Path | Purpose |
|---|---|
| `architecture/overview.md` | Canonical system architecture and component responsibilities. |
| `architecture/intent-engine.md` | Intent Engine design and lifecycle. |
| `architecture/context-engine.md` | Context Engine design. |
| `architecture/trust-engine.md` | Trust Engine: the deterministic evaluation boundary. |
| `architecture/action-graph.md` | The Enterprise Action Graph. |
| `architecture/execution-planner.md` | Execution Planning. |
| `architecture/execution-record.md` | Execution Record. |
| `architecture/outcome-engine.md` | Outcome Engine: postcondition verification. |
| `architecture/operational-memory.md` | Operational Memory. |
| `architecture/durable-execution.md` | Durable Execution: long-running, recoverable orchestration. |

### Trust

| Path | Purpose |
|---|---|
| `trust/trust-model.md` | The canonical Trust model. |
| `trust/trust-engine.md` | Trust Engine internals. |
| `trust/trust-state-machine.md` | The Trust State Machine. |
| `trust/determinism.md` | Determinism in Trust. |
| `trust/authorization.md` | Authorization as a Trust dimension. |
| `trust/evidence.md` | Evidence and its role in Trust. |
| `trust/policy-evaluation.md` | Policy evaluation within Trust. |
| `trust/risk.md` | Risk: consequence profiles and controls. |
| `trust/validation.md` | Validation as the deterministic pre-Trust layer. |
| `trust/ambiguity.md` | How ambiguity is handled without guessing. |

### Intent

| Path | Purpose |
|---|---|
| `intent/intent-model.md` | The Intent object: schema, lifecycle, and semantics. |
| `intent/intent-lifecycle.md` | How an Intent moves from expression to completion. |
| `intent/intent-resolution.md` | The resolution process. |
| `intent/intent-language.md` | How natural language is interpreted without being the execution primitive. |
| `intent/intent-ambiguity.md` | Ambiguity detection and handling. |
| `intent/intent-composition.md` | Composite and multi-step Intents. |
| `intent/clarification.md` | Clarification as a first-class governed lifecycle state. |
| `intent/confidence.md` | What confidence means and what it does not authorize. |
| `intent/executable-intent.md` | The transition from resolved to executable Intent. |

### Execution

| Path | Purpose |
|---|---|
| `execution/execution-model.md` | The Execution model: states, transitions, and semantics. |
| `execution/action-model.md` | Action structure within the execution layer. |
| `execution/action-contracts.md` | Action Contracts: the explicit boundary for what may be executed. |
| `execution/planning.md` | Planning: Actions that satisfy a trusted Intent. |
| `execution/preconditions.md` | Preconditions for execution. |
| `execution/postconditions.md` | Postconditions for Outcome verification. |
| `execution/idempotency.md` | Idempotency: preventing duplicate side effects. |
| `execution/retries.md` | Retry semantics. |
| `execution/failure.md` | Failure classification and recovery. |
| `execution/compensation.md` | Compensating Actions. |
| `execution/human-intervention.md` | Human intervention as an explicit execution state. |

### Contracts

| Path | Purpose |
|---|---|
| `contracts/overview.md` | The Contracts layer. |
| `contracts/action-contract.md` | Action Contract specification. |
| `contracts/intent-contract.md` | Intent Contract. |
| `contracts/trust-contract.md` | Trust Contract. |
| `contracts/execution-contract.md` | Execution Contract. |
| `contracts/context-contract.md` | Context Contract. |
| `contracts/event-contract.md` | Event Contract. |
| `contracts/versioning.md` | Contract versioning semantics. |

### Interfaces

| Path | Purpose |
|---|---|
| `interfaces/overview.md` | The canonical external interface layer. |
| `interfaces/intent-api.md` | Intent API. |
| `interfaces/action-api.md` | Action API. |
| `interfaces/trust-api.md` | Trust API. |
| `interfaces/context-api.md` | Context API. |
| `interfaces/execution-api.md` | Execution API. |
| `interfaces/event-model.md` | Canonical Event Model. |
| `interfaces/integration-model.md` | Integration Model. |

### Data

| Path | Purpose |
|---|---|
| `data/data-model.md` | The Noema canonical data model. |
| `data/canonical-data.md` | What canonical data Noema maintains. |
| `data/evidence.md` | Evidence data: structure, provenance, and lifecycle. |
| `data/context.md` | Context data: scoping, freshness, and trust. |
| `data/provenance.md` | Provenance tracking across consequential transitions. |
| `data/persistence.md` | How Noema state is persisted. |
| `data/temporal-state.md` | Temporal semantics. |

### Graph

| Path | Purpose |
|---|---|
| `graph/graph-model.md` | The Enterprise Action Graph: nodes, edges, and traversal. |
| `graph/enterprise-graph.md` | Enterprise capabilities in the graph. |
| `graph/capability-model.md` | Capability representation and discovery. |
| `graph/graph-evolution.md` | How the graph evolves. |

### Integrations

| Path | Purpose |
|---|---|
| `integrations/integration-model.md` | The full integration model. |
| `integrations/adapters.md` | Adapter design. |
| `integrations/enterprise-capabilities.md` | How enterprise capabilities are exposed. |
| `integrations/sdk.md` | SDK for building integrations. |

### Loops

| Path | Purpose |
|---|---|
| `loops/overview.md` | The canonical operational loops of Noema. |
| `loops/clarification-loop.md` | The clarification loop. |
| `loops/execution-loop.md` | The execution loop. |
| `loops/operational-learning.md` | How operational history informs future behaviour. |

### AI

| Path | Purpose |
|---|---|
| `ai/model-abstraction.md` | How AI models are abstracted and kept replaceable. |
| `ai/ai-harness.md` | The AI Harness: how models are governed. |
| `ai/intent-generation.md` | How models participate in Intent interpretation. |
| `ai/evaluation.md` | How AI outputs are evaluated before entering canonical state. |
| `ai/safety.md` | AI safety: the probabilistic/deterministic boundary. |

### Engineering

| Path | Purpose |
|---|---|
| `engineering/constitution.md` | The engineering constitution. |
| `engineering/engineering-constitution.md` | Engineering-level implementation rules. |
| `engineering/architecture.md` | Engineering architecture. |
| `engineering/components.md` | Component design. |
| `engineering/runtime.md` | Runtime requirements. |
| `engineering/reliability.md` | Reliability design. |
| `engineering/failure-recovery.md` | Failure recovery patterns. |
| `engineering/idempotency.md` | Idempotency implementation. |
| `engineering/observability.md` | Observability requirements. |
| `engineering/scalability.md` | Scalability design. |
| `engineering/security.md` | Security boundaries. |
| `engineering/system-boundaries.md` | System boundary enforcement. |
| `engineering/testing.md` | Testing requirements and philosophy. |

### Enterprise

| Path | Purpose |
|---|---|
| `enterprise/overview.md` | How Noema relates to enterprise systems. |
| `enterprise/systems.md` | Enterprise system types. |
| `enterprise/system-of-record.md` | Systems of record and why Noema defers to them. |
| `enterprise/business-state.md` | Business state and why Noema does not own it. |
| `enterprise/identity.md` | Enterprise identity in Trust. |
| `enterprise/permissions.md` | Enterprise permission systems. |
| `enterprise/auditability.md` | Auditability requirements. |
| `enterprise/data-boundaries.md` | Data boundaries between Noema and enterprise systems. |
| `enterprise/organizational-boundaries.md` | Organizational and multi-tenant boundaries. |

### Taxonomy

| Path | Purpose |
|---|---|
| `taxonomy/intent-taxonomy.md` | Classification of Intent types. |
| `taxonomy/outcome-taxonomy.md` | Classification of Outcome types. |
| `taxonomy/trust-taxonomy.md` | Classification of Trust conditions. |
| `taxonomy/fintech/intents.md` | Fintech-specific Intent taxonomy. |
| `taxonomy/fintech/outcomes.md` | Fintech-specific Outcome taxonomy. |
| `taxonomy/fintech/trust.md` | Fintech-specific Trust classification. |

### Strategy

| Path | Purpose |
|---|---|
| `strategy/wedge.md` | The commercial wedge: first market entry point. |
| `strategy/market.md` | Market analysis. |
| `strategy/positioning.md` | Positioning relative to adjacent technologies. |
| `strategy/expansion.md` | Expansion path beyond the initial wedge. |
| `strategy/roadmap.md` | Product and capability roadmap. |

### Product

| Path | Purpose |
|---|---|
| `product/product-model.md` | The Noema product model. |
| `product/user-model.md` | User model: who interacts with Noema. |
| `product/interaction-model.md` | How users and systems interact with Noema. |
| `product/workflow-model.md` | Workflow model. |
| `product/integration-model.md` | Product-level integration model. |
| `product/commercial-wedge.md` | Commercial wedge product definition. |

### Decisions

| Path | Purpose |
|---|---|
| `decisions/README.md` | How ADRs are structured and used. |
| `decisions/ADR-001-example.md` | Example ADR. |
| `decisions/ADRs/` | All Architecture Decision Records. |

### Reference Workflows and Research

| Path | Purpose |
|---|---|
| `reference-workflows/` | Canonical concepts demonstrated end-to-end in real scenarios. |
| `research/` | Hypotheses, experiments, rejected ideas. May challenge Canon; does not become Canon automatically. |
| `rfcs/` | Proposals for significant canonical or architectural changes. |

⸻

## 11. How to Navigate This Repository

| Goal | Start here |
|---|---|
| Understand Noema's purpose and thesis | `thesis/thesis.md`, then `CANON.md` |
| Learn canonical vocabulary | `GLOSSARY.md`, then `ontology/glossary.md` |
| Understand the architecture | `architecture/overview.md` |
| Understand the Trust model | `trust/trust-model.md` and `trust/trust-state-machine.md` |
| Understand execution | `execution/execution-model.md` and `execution/action-contracts.md` |
| Design an integration | `integrations/integration-model.md` and `integrations/adapters.md` |
| Find architectural decisions | `decisions/README.md` and `decisions/ADRs/` |
| See the system in a real workflow | `reference-workflows/card-renewal/` |

⸻

## 12. Authority Hierarchy

| Level | Documents | Meaning |
|---|---|---|
| Canon | `CANON.md`, `thesis/`, foundational `ontology/` | Foundational truth. Requires deliberate change process with ADR. |
| Specification | `interfaces/`, `contracts/`, `execution/`, `trust/`, `intent/` | Precise behaviour derived from Canon. |
| Architecture | `architecture/`, `engineering/`, `data/`, `graph/` | How specifications are realized. |
| Decision Records | `decisions/ADRs/` | Why decisions were made. |
| Research | `research/` | Challenges Canon; does not become Canon automatically. |
| Reference Workflows | `reference-workflows/` | Canonical concepts in real scenarios. |
| Strategy | `strategy/`, `product/` | Commercial and organizational direction. |

⸻

## 13. The Canonical Test

Before any feature, decision, or implementation is adopted, these questions must be answerable:

1. What Intent does this represent?
2. What semantic state does Noema own?
3. What business state remains owned by another system?
4. What establishes the meaning of the Intent?
5. What makes the Intent sufficiently resolved?
6. What makes the Intent structurally and semantically valid?
7. What Evidence establishes the relevant conditions?
8. What authority permits the Action?
9. What Policies govern it?
10. What Risk controls apply?
11. What Capability performs it?
12. What Constraints must hold?
13. What makes the Intent trusted?
14. What Contract governs execution?
15. What happens if information is unknown?
16. What happens if the Intent is ambiguous?
17. What happens if Trust requirements are incomplete?
18. What happens if a previously READY Intent becomes invalid?
19. What happens if execution fails?
20. What happens if execution produces an unknown outcome?
21. How is the Outcome verified?
22. What provenance is retained?
23. What happens when a human must intervene?
24. Which system remains authoritative for business truth?
25. Does the proposal strengthen or violate the canonical boundaries of Noema?

⸻

## 14. What Noema Is Not

- **An AI assistant** — AI models participate inside Noema. They do not define it.
- **An agent framework** — Agents operate within Noema's authority model. They do not define it.
- **An RPA system** — Noema operates through semantic contracts, not brittle screen automation.
- **A workflow engine** — Durable orchestration is one component, not the abstraction.
- **An API gateway** — Noema expresses canonical semantic Intent, not arbitrary API routing.
- **A policy engine** — Policy evaluation is one dimension of Trust.
- **A chatbot** — A conversational interface may interact with Noema. It is not what Noema is.
- **An ERP, CRM, or system of record** — Noema does not own business state.
- **An unbounded autonomous agent** — Noema operates within explicit authority, policy, capability, and contract boundaries at all times.
