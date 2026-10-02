> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Decisions

Status: Foundational
Version: 0.1
Domain: Governance / Architecture
Canonical Path: decisions/README.md

⸻

1. Purpose

The decisions directory contains the formal record of significant architectural and foundational decisions made during the development of Noema.

Its primary purpose is to preserve decision provenance:

* what decision was made
* why it was made
* what alternatives were considered
* what consequences were accepted
* which canonical boundaries or specifications are affected
* whether a decision remains current or has been superseded

The directory exists so that Noema’s architecture can evolve without losing the reasoning behind its foundational choices.

⸻

2. Directory Structure

The canonical structure is:

decisions/
├── README.md
└── ADRs/
    ├── ADR-001-example.md
    ├── ADR-002-*.md
    ├── ADR-003-probabilistic-deterministic-boundary.md
    ├── ADR-004-deterministic-trust-evaluation.md
    ├── ADR-005-explicit-execution-contracts.md
    ├── ADR-006-capability-permission-separation.md
    ├── ADR-007-enterprise-systems-remain-authoritative.md
    ├── ADR-008-clarification-over-guessing.md
    ├── ADR-009-*.md
    ├── ADR-010-trust-state-machine.md
    ├── ADR-011-intent-state-separate-from-execution-state.md
    ├── ADR-012-provenance-and-auditability.md
    ├── ADR-013-bounded-autonomy.md
    ├── ADR-014-human-intervention-as-explicit-state.md
    ├── ADR-015-fail-closed-on-unknown.md
    ├── ADR-016-consumer-side-authoritative-validation.md
    ├── ADR-017-outcome-separate-from-trust.md
    └── ADR-018-canonical-repository-authority.md

The ADR directory is the canonical location for Architecture Decision Records.

⸻

3. What Belongs Here

A decision belongs in an ADR when it materially affects the architecture or foundational semantics of Noema.

Examples include decisions concerning:

* the probabilistic/deterministic boundary
* Trust evaluation
* Trust state transitions
* execution contracts
* capability and permission
* authority over business state
* clarification and ambiguity
* Intent and execution state
* provenance and auditability
* bounded autonomy
* human intervention
* fail-closed behavior
* consumer-side validation
* separation of Trust and Outcome
* canonical repository authority

These decisions establish boundaries that affect multiple parts of the Noema system.

⸻

4. What Does Not Belong Here

Not every engineering decision requires an ADR.

The following generally belong elsewhere:

Canon

Foundational principles that define what Noema is.

Specifications

Precise definitions, schemas, protocols, state semantics, and behavioral requirements.

Architecture

Descriptions of how the current system realizes the specifications.

Research

Experiments, hypotheses, external findings, and ideas that have not become accepted architectural decisions.

Implementation

Routine code-level decisions that do not materially change Noema’s architecture.

The distinction is:

Canon
    ↓
What Noema fundamentally is
Specification
    ↓
What Noema must mean or do
Architecture
    ↓
How Noema realizes it
ADR
    ↓
Why a significant architectural decision was made
Research
    ↓
What may inform future decisions

⸻

5. ADR Authority

An ADR records a decision; it does not automatically become the highest-level authority in the repository.

The current normative hierarchy remains governed by the canonical repository structure.

In particular:

Current Canon
      ↓
Current Specifications
      ↓
Current Architecture

ADRs provide the historical reasoning behind significant decisions.

If a later accepted decision supersedes an earlier ADR, the earlier ADR remains part of the historical record.

It should not be silently rewritten to reflect the newer decision.

⸻

6. ADR Lifecycle

An ADR may move through statuses such as:

PROPOSED
    ↓
ACCEPTED
    ↓
SUPERSEDED

Other statuses may include:

REJECTED
DEPRECATED

The status must make the current position of the decision explicit.

A superseded ADR remains valuable because it explains what Noema previously decided and why.

⸻

7. Creating a New ADR

A new ADR should be created when a proposed change materially affects an established architectural boundary or foundational behavior.

Before creating one, determine:

1. What decision is actually being made?
2. Why does it matter architecturally?
3. What existing Canon or specification does it affect?
4. What alternatives exist?
5. What are the consequences?
6. Does an existing ADR already address the same decision?
7. Does the decision supersede an existing ADR?
8. What implementation or migration consequences follow?

The ADR should record the decision rather than merely documenting implementation activity.

⸻

8. ADR Naming

ADR filenames use the following form:

ADR-NNN-short-descriptive-name.md

For example:

ADR-010-trust-state-machine.md

The numeric identifier is sequential.

The descriptive name should identify the decision itself rather than the implementation that happens to realize it.

⸻

9. ADR Content

A Noema ADR should normally contain:

Title
Status
Date
Decision Type
Domain
Canonical Path
Context
Decision
Alternatives Considered
Consequences
Architectural Implications
Relationship to Canon
Related Documents
Follow-Up Requirements
Final Decision / Principle

The exact structure may evolve as the ADR system matures.

The important requirement is that a reader should be able to reconstruct the decision without relying on undocumented context.

⸻

10. Decision Provenance

Each significant decision should be traceable.

An ADR should identify, where applicable:

* the problem that motivated the decision
* the architectural constraints
* alternatives considered
* the selected approach
* consequences
* affected canonical documents
* related ADRs
* subsequent decisions that supersede it

This provides a historical chain:

Problem
   ↓
Analysis
   ↓
Decision
   ↓
Implementation
   ↓
Consequences
   ↓
Future Decision

⸻

11. Superseding an ADR

When a decision changes, the previous ADR should remain intact.

A new ADR should record the new decision and explicitly identify the previous decision as superseded.

Conceptually:

ADR-XXX
   │
   │ superseded by
   ▼
ADR-YYY

The new decision should explain the reason for the change.

This prevents architectural history from being rewritten after the fact.

⸻

12. Relationship to the Noema Canon

The ADR collection currently documents decisions supporting several central Noema boundaries:

Human Intent
      ↓
Interpretation
      ↓
Resolution
      ↓
Validation
      ↓
Trust
      ↓
Execution Contract
      ↓
Execution
      ↓
Outcome

The ADRs establish important constraints around these transitions.

Examples include:

* probabilistic interpretation must not become deterministic authority
* Trust evaluation must be deterministic
* execution must use explicit contracts
* capability does not equal permission
* enterprise systems remain authoritative for business state
* ambiguity must lead to clarification rather than guessing
* Trust state must be explicit
* Intent state must remain distinct from execution state
* decisions must have provenance
* autonomy must remain bounded
* human intervention must be explicit
* unknown mandatory conditions must fail closed
* execution consumers may perform authoritative final validation
* execution outcome is distinct from Trust
* the canonical repository has explicit authority boundaries

⸻

13. Current ADR Collection

The current ADR collection is intended to establish the foundational architectural decision history of Noema.

ADR-001

ADR-001-example.md

Establishes the purpose, structure, authority, and lifecycle of Noema Architecture Decision Records.

ADR-003

ADR-003-probabilistic-deterministic-boundary.md

Defines the architectural boundary between probabilistic AI inference and deterministic Noema authority.

ADR-004

ADR-004-deterministic-trust-evaluation.md

Defines deterministic Trust evaluation as the mechanism for establishing execution eligibility.

ADR-005

ADR-005-explicit-execution-contracts.md

Establishes explicit execution contracts as the boundary between trusted Intent and execution.

ADR-006

ADR-006-capability-permission-separation.md

Separates system capability from actor permission and Trust.

ADR-007

ADR-007-enterprise-systems-remain-authoritative.md

Establishes that existing enterprise systems remain authoritative for their respective business domains.

ADR-008

ADR-008-clarification-over-guessing.md

Establishes clarification as the correct response when Noema cannot reliably establish material Intent semantics.

ADR-010

ADR-010-trust-state-machine.md

Defines the Trust lifecycle and its deterministic state transitions.

ADR-011

ADR-011-intent-state-separate-from-execution-state.md

Separates semantic Intent lifecycle from execution lifecycle.

ADR-012

ADR-012-provenance-and-auditability.md

Establishes provenance and auditability as requirements for consequential Noema decisions and execution.

ADR-013

ADR-013-bounded-autonomy.md

Defines autonomy as operating within explicit authority, policy, capability, and contractual boundaries.

ADR-014

ADR-014-human-intervention-as-explicit-state.md

Establishes human intervention as an explicit system state rather than an implicit failure mode.

ADR-015

ADR-015-fail-closed-on-unknown.md

Establishes fail-closed behavior when mandatory conditions cannot be established.

ADR-016

ADR-016-consumer-side-authoritative-validation.md

Establishes that execution consumers may perform final authoritative validation against current business state.

ADR-017

ADR-017-outcome-separate-from-trust.md

Separates Trust and execution eligibility from the actual outcome of execution.

ADR-018

ADR-018-canonical-repository-authority.md

Defines the authority relationship among Canon, specifications, architecture, ADRs, research, and other repository artifacts.

⸻

14. Gaps and Reserved Identifiers

ADR numbering is sequential, but not every identifier necessarily represents a currently populated ADR.

For example:

ADR-002
ADR-009

may represent decisions that have not yet been populated or whose intended scope has not yet been finalized.

Reserved identifiers should not be assigned new meanings casually.

Before creating a new ADR, inspect the existing sequence and determine whether the identifier has already been conceptually assigned.

⸻

15. ADRs Are Not the Implementation

An ADR does not prescribe every implementation detail.

For example:

ADR
 ↓
establishes:
"Trust must be deterministic."
Specification
 ↓
defines:
what deterministic Trust means.
Architecture
 ↓
defines:
how the Trust Engine implements it.
Code
 ↓
implements:
the architecture.

This separation prevents ADRs from becoming implementation manuals.

⸻

16. ADR Review

A proposed ADR should be reviewed for consistency with:

* the Noema Canon
* existing specifications
* existing ADRs
* architectural boundaries
* terminology
* Trust semantics
* Intent semantics
* execution semantics

Particular care should be taken when a proposed decision changes an existing foundational invariant.

Such changes should normally identify the affected ADRs and canonical documents explicitly.

⸻

17. Core Invariants

The decisions directory follows these principles:

1. Significant architectural decisions must be explicit.
2. Decision rationale must be preserved.
3. Historical decisions must remain reconstructible.
4. ADRs must not silently override the current Canon.
5. Superseded decisions must remain historically visible.
6. Related decisions must be cross-referenced.
7. ADR identifiers must remain stable.
8. Architectural terminology must remain consistent with the Canon.
9. A decision should be recorded at the level of abstraction at which it materially affects Noema.
10. Architectural history must not depend on undocumented conversations or individual memory.

⸻

18. Final Principle

The decisions directory exists to preserve the reasoning behind Noema’s architecture.

The governing principle is:

Noema should not only preserve what the system decided; it should preserve why significant architectural decisions were made, what alternatives were considered, and how those decisions relate to the current Canon.