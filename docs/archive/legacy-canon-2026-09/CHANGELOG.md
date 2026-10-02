> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

CHANGELOG.md

# Noema Changelog
This file records significant changes to the Noema Canonical Repository.
The changelog tracks changes to canonical concepts, specifications, architecture, contracts, and other repository-level artifacts that materially affect the definition or implementation of Noema.
It is not intended to record every editorial correction or implementation commit.
---
## [Unreleased]
### Foundational Canonical Baseline
The Noema Canonical Repository is being established as a structured source of truth for the Noema system.
The current foundational model establishes:
- Noema as an intent infrastructure layer between human intent and existing software systems.
- Intent as a first-class canonical semantic object.
- A separation between:
  - interpretation
  - resolution
  - validation
  - trust
  - planning
  - contract formation
  - execution
  - outcome
- A deterministic Trust boundary between probabilistic model inference and executable action.
- Explicit separation of capability, authorization, policy, constraints, evidence, and trust.
- Enterprise systems remaining authoritative for their respective business domains.
- Explicit execution contracts as the boundary through which trusted Intent becomes executable.
- Human clarification and intervention as legitimate lifecycle states.
- Explicit state and provenance as foundational requirements.
- Fail-closed behavior when sufficient grounds for execution cannot be established.
### Trust Model Refinement
The Trust domain has been formalized around three distinct concepts:
1. **Trust Model** — defines what Trust means.
2. **Trust Engine** — defines how Trust is evaluated.
3. **Trust State Machine** — defines how Trust evolves over time.
The Trust State Machine establishes the canonical lifecycle:
```text
UNRESOLVED
    ↓
EVALUATING
    ↓
WAITING / BLOCKED / READY
    ↓
EXECUTING
    ↓
COMPLETED / FAILED

The model establishes that:

* Trust is a lifecycle rather than a one-time boolean decision.
* WAITING and BLOCKED are semantically distinct.
* WAITING represents an incomplete but potentially recoverable Trust condition.
* BLOCKED represents a condition that currently prohibits execution.
* READY represents execution eligibility, not successful execution.
* READY may be invalidated by material changes in authorization, policy, evidence, risk, capability, context, constraints, or other Trust dependencies.
* WAITING → READY should not occur directly; the Intent must return through EVALUATING.
* BLOCKED → READY should not occur directly; the Intent must return through EVALUATING.
* READY → EXECUTING requires an explicit execution boundary and consumer acceptance of the Execution Contract.
* Trust transitions must be deterministic and event-driven.
* Probabilistic model confidence must never directly determine Trust state.
* Trust history and transition provenance must be reconstructible.

Validation Layer

Validation has been established as a distinct canonical layer between Intent Resolution and Trust Evaluation.

The canonical lifecycle is:

User Expression
       ↓
Intent Interpretation
       ↓
Intent Resolution
       ↓
Validation
       ↓
Trust Evaluation
       ↓
Execution Eligibility
       ↓
Execution
       ↓
Outcome

Validation establishes whether a resolved Intent is structurally complete, semantically applicable, and consistent with the rules and information required for its next lifecycle transition.

The Validation model establishes:

* Validation is deterministic.
* Validation operates on canonical Intent semantics.
* Validation is distinct from Intent Resolution.
* Validation is distinct from Trust.
* Validation is distinct from authorization.
* Validation does not execute Actions.
* Validation must not silently modify Intent semantics.
* Missing information must remain distinguishable from invalid information.
* Unknown information must not be treated as valid.
* Validation results should be structured and inspectable.
* Validation rules should be versionable.
* Validation results should retain provenance.
* Validation may require re-evaluation when relevant Intent, context, resource, policy, evidence, capability, or temporal conditions change.
* External execution systems may perform additional authoritative validation.

The canonical conceptual result taxonomy is:

VALID
INVALID
INCOMPLETE
UNKNOWN

with the corresponding relationship to Trust:

INCOMPLETE → WAITING
INVALID    → BLOCKED
UNKNOWN    → WAITING / NOT READY
VALID      → TRUST EVALUATION

Canonical Separation of Lifecycles

The repository now distinguishes the following related but non-identical lifecycles:

Intent Lifecycle
Trust Lifecycle
Execution Lifecycle
Outcome

Trust and execution are therefore not required to be represented as a single state enum.

The canonical conceptual separation is:

                 Intent
                   │
          ┌────────┴────────┐
          ▼                 ▼
    Trust State       Execution State
          │                 │
     UNRESOLVED             │
     EVALUATING             │
     WAITING                │
     BLOCKED                │
     READY             EXECUTING
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                COMPLETED       FAILED

This separation prevents Trust from being conflated with execution outcome.

Determinism and Re-Evaluation

The foundational model now explicitly requires deterministic evaluation based on explicit inputs and rules.

For a given:

Intent
Context
Evidence
Rules
Policy Versions
Relevant Conditions

the resulting Validation and Trust decisions must be reproducible.

Material changes must trigger appropriate revalidation or Trust re-evaluation rather than allowing stale decisions to remain authoritative.

Examples of material events include:

* intent.updated
* intent.resolved
* evidence.added
* evidence.expired
* authorization.granted
* authorization.revoked
* approval.granted
* approval.expired
* policy.changed
* risk.changed
* capability.available
* capability.unavailable
* constraint.changed
* context.changed
* trust.expired

Dependency-aware re-evaluation is recognized as the preferred conceptual approach so that changes affect only the Intents whose relevant conditions depend upon them.

Provenance and Auditability

Validation and Trust decisions are required to be reconstructible.

Conceptually, significant Trust transitions record:

* previous state
* triggering event
* new state
* timestamp
* Intent version
* evaluation identifier
* relevant evidence
* reason

Validation results similarly identify:

* rule
* rule version
* input
* evidence
* timestamp
* result

This establishes provenance as a first-class property of consequential Noema decisions.

⸻

Versioning Policy

Noema uses semantic version identifiers for canonical artifacts.

A canonical artifact version should be incremented when its meaning or normative behavior changes.

Major

A major version indicates a breaking change to a canonical concept, contract, schema, lifecycle, or invariant.

Examples include:

* removing a foundational state
* changing the meaning of a canonical concept
* changing a normative contract incompatibly
* invalidating an established invariant

Minor

A minor version indicates a backward-compatible addition or meaningful expansion.

Examples include:

* adding a new canonical state subtype
* adding a new validation category
* adding a new supported event
* extending a taxonomy without changing existing meanings

Patch

A patch version indicates a non-semantic correction.

Examples include:

* editorial corrections
* clarification of wording without changing meaning
* formatting corrections
* typographical fixes

⸻

Changelog Principles

The changelog follows these principles:

1. Canonical changes must be explicit.
2. Foundational semantic changes must not be hidden inside implementation commits.
3. Breaking changes must identify their affected concepts and artifacts.
4. Changes to Canon should be traceable to the specifications and architecture they affect.
5. Historical entries should describe what changed, not silently rewrite history.
6. Research, proposals, and experiments should not be represented as canonical changes until adopted.
7. Editorial-only changes should not be overstated as architectural changes.

⸻

Future Entries

Future entries should identify, where applicable:

* version
* date
* affected domain
* changed canonical concepts
* added specifications
* changed contracts
* changed invariants
* migration implications
* related ADRs
* implementation impact

The changelog should remain a historical record of how the Noema Canonical Repository evolves.