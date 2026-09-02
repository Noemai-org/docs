Concepts

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/concepts.md

⸻

1. Purpose

This document defines the major concepts that constitute the Noema ontology and establishes the relationships between them.

It is an ontology map, not the detailed specification of every concept.

The individual ontology documents are authoritative for the detailed semantics of each concept.

The purpose of this document is to answer:

What are the fundamental things that exist in the Noema model, and how do they relate to one another?

⸻

2. The Noema Ontology

At its highest level, Noema models the transition from human intent to trusted execution.

Actor
  │
  │ expresses
  ▼
Intent
  │
  │ requires
  ▼
Context
  │
  │ informs
  ▼
Intent Resolution
  │
  ▼
Trust
  │
  │ authorizes transition toward
  ▼
Action
  │
  │ requires
  ▼
Capability
  │
  │ enables
  ▼
Execution
  │
  ▼
Outcome

This lifecycle exists within additional concepts including:

Authority
Policy
Constraint
Evidence
State
Provenance
Resource
System

These concepts constrain, explain, or contextualize the primary lifecycle.

⸻

3. Conceptual Layers

The Noema ontology can be understood through five conceptual layers.

Layer 1 — Participants

Who or what participates?

Actor
Identity
Organization
System

⸻

Layer 2 — Intent

What is someone trying to accomplish?

Intent
Objective
Context
Constraint

⸻

Layer 3 — Trust

Why is Noema justified in proceeding?

Evidence
Policy
Authority
Trust
Confidence

⸻

Layer 4 — Execution

What can actually be done?

Action
Capability
Contract
Execution

⸻

Layer 5 — Result

What happened?

Outcome
State
Business State
Provenance

The boundaries between these layers are intentional.

⸻

4. Foundational Concepts

The following concepts form the primary vocabulary of Noema.

⸻

4.1 Actor

An Actor is an entity that participates in the intent-to-action lifecycle.

An Actor may be:

* a human
* an organization
* a system
* an automated agent
* a delegated representative

Actor answers:

Who or what is participating?

Canonical definition:

01-ontology/actor.md

⸻

4.2 Intent

An Intent represents an Actor’s desired objective or state of affairs.

Intent answers:

What does the Actor want to accomplish?

Intent is the central object of Noema.

Human language may express Intent, but the natural-language expression is not itself the canonical executable representation.

Canonical definition:

01-ontology/intent.md

⸻

4.3 Context

Context is the information relevant to interpreting, validating, trusting, or executing an Intent.

Context may include:

* Actor information
* business state
* system state
* temporal information
* organizational context
* previous interactions
* policies
* capabilities
* external evidence

Context answers:

What information is necessary to understand this Intent correctly?

Canonical definition:

01-ontology/context.md

⸻

4.4 Action

An Action is a bounded operation that can advance an Intent.

Action answers:

What operation can be performed to advance the Intent?

Canonical definition:

01-ontology/action.md

⸻

4.5 Capability

A Capability is an explicit ability of a system or execution environment to perform an operation.

Capability answers:

What can this system do?

Canonical definition:

01-ontology/capability.md

⸻

4.6 Outcome

An Outcome represents what actually happened as a consequence of an Action or execution attempt.

Outcome answers:

What happened?

Outcome must be distinguished from the intended result.

Canonical definition:

01-ontology/outcome.md

⸻

5. Supporting Concepts

The following concepts support the primary lifecycle.

⸻

5.1 Identity

Identity represents the recognized identity of an entity.

Identity answers:

Who is this entity?

Identity is not equivalent to Actor, Authority, or Permission.

Authentication may establish Identity.

Identity may then participate as an Actor within a Noema interaction.

⸻

5.2 Authority

Authority represents the ability of an Actor to legitimately cause an Action under defined conditions.

Authority answers:

What is this Actor permitted to cause?

Authority is contextual.

It may depend on:

* identity
* role
* organization
* delegation
* policy
* target
* action
* time
* risk

Authority is not Capability.

⸻

5.3 Policy

A Policy is a rule or set of rules that constrains what may occur under defined conditions.

Policy answers:

What rules govern this Intent or Action?

Policies may originate from:

* enterprise organizations
* regulatory requirements
* system owners
* security controls
* product rules
* Noema configuration

Policies may influence Trust, Authority, Action selection, and Execution.

⸻

5.4 Constraint

A Constraint is a condition that limits the permissible interpretation, planning, or execution of an Intent or Action.

Constraint answers:

What must remain true or what must not be violated?

Examples:

Amount <= $10,000
Departure >= 09:00
Only use approved vendors
Do not contact the customer by SMS

Constraints may originate from an Actor, Intent, Policy, or system.

⸻

5.5 Evidence

Evidence is information used to support or challenge a proposition relevant to Intent resolution, Trust, or Execution.

Evidence answers:

What supports this conclusion?

Examples include:

* verified identity
* system records
* policy documents
* API responses
* explicit user statements
* authorization records
* external data
* execution results

Evidence should have provenance.

⸻

5.6 Trust

Trust represents Noema’s deterministic determination that sufficient grounds exist to permit a particular transition from understood Intent toward Action or Execution.

Trust answers:

Has Noema established sufficient grounds to proceed?

Trust is not model confidence.

Trust is not permission.

Trust is not capability.

Trust is a deterministic decision derived from explicit inputs, evidence, policies, authority, constraints, and other applicable conditions.

⸻

5.7 Confidence

Confidence represents the degree of certainty associated with a probabilistic interpretation or inference.

Confidence answers:

How strongly does the model believe this interpretation?

Confidence may contribute evidence to Noema’s reasoning.

It does not itself grant Trust or Authority.

⸻

5.8 Resource

A Resource is an entity that an Action may operate on, inspect, create, modify, or otherwise affect.

Examples:

Customer
Account
Card
Subscription
Invoice
Document
Payment
Employee

Resources often belong to external systems of record.

⸻

5.9 System

A System is a software or technological environment that stores state, provides capabilities, or executes operations.

Examples:

CRM
Banking Platform
Payment Processor
Identity Provider
ERP
Notification Service
Database

A System may provide Capabilities without becoming part of Noema itself.

⸻

5.10 State

State represents the condition of an entity, Intent, Action, Execution, or workflow at a particular point in time.

State answers:

What condition is this entity currently in?

Noema must distinguish between:

Intent State
Action State
Execution State
Noema State
Business State

Noema owns relevant Intent and execution state.

External systems remain authoritative for their business state.

⸻

5.11 Provenance

Provenance describes where information, decisions, Actions, or Outcomes came from.

Provenance answers:

Where did this information or decision originate?

Provenance may include:

* source system
* Actor
* timestamp
* policy version
* evidence source
* capability version
* execution identifier
* workflow transition

Provenance enables auditability without requiring exposure of private model reasoning.

⸻

6. Derived Concepts

Some Noema concepts are not independent entities but arise from relationships between foundational concepts.

⸻

6.1 Delegation

Delegation is a relationship in which one Actor permits another Actor to act on its behalf.

Principal
   │
   │ delegates
   ▼
Delegate

Delegation affects Authority.

⸻

6.2 Role

A Role describes how an Actor participates in an Intent, Action, or workflow.

Examples:

Initiator
Principal
Delegate
Beneficiary
Approver
Executor
Observer

Role does not define Actor identity.

⸻

6.3 Authorization

Authorization is the evaluation of whether an Actor has sufficient Authority to perform a particular Action under particular conditions.

Conceptually:

Actor
+
Action
+
Target
+
Context
+
Policy
=
Authorization Decision

Authorization is therefore a relationship and decision, not simply an attribute of an Actor.

⸻

6.4 Execution

Execution is the actual attempt to perform an Action.

Action
   ↓
Execution Attempt
   ↓
Observed Result

An Action can exist without being executed.

⸻

6.5 Contract

A Contract defines the explicit conditions and semantics under which an Action or Capability may be executed.

A Contract may define:

* inputs
* outputs
* preconditions
* postconditions
* authorization requirements
* side effects
* failure semantics
* idempotency
* versioning

Contracts translate ontology into executable guarantees.

⸻

7. Primary Relationships

The most important relationships in the Noema ontology are:

Actor
  │
  ├── expresses ─────────────► Intent
  │
  ├── possesses ─────────────► Authority
  │
  ├── performs ──────────────► Action
  │
  └── receives ──────────────► Outcome
Intent
  │
  ├── has ───────────────────► Context
  │
  ├── contains ──────────────► Constraint
  │
  └── motivates ─────────────► Action
Action
  │
  ├── operates on ───────────► Resource
  │
  ├── requires ──────────────► Capability
  │
  ├── requires ──────────────► Authority
  │
  ├── governed by ───────────► Policy
  │
  └── produces ──────────────► Outcome
Capability
  │
  ├── belongs to ────────────► System
  │
  └── enables ───────────────► Action
Trust
  │
  ├── considers ─────────────► Evidence
  ├── considers ─────────────► Policy
  ├── considers ─────────────► Authority
  ├── considers ─────────────► Capability
  └── permits ───────────────► Execution

⸻

8. The Central Noema Relationship Graph

The core ontology can therefore be represented as:

                           ┌─────────────┐
                           │   Actor     │
                           └──────┬──────┘
                                  │
                              expresses
                                  │
                                  ▼
                           ┌─────────────┐
                           │   Intent    │
                           └──────┬──────┘
                                  │
                         contextualized by
                                  │
                                  ▼
                           ┌─────────────┐
                           │   Context   │
                           └──────┬──────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │ Intent Resolution │
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │      Trust       │
                        └────────┬─────────┘
                                 │
                         trusted transition
                                 │
                                 ▼
                           ┌─────────────┐
                           │   Action    │
                           └──────┬──────┘
                                  │
                             requires
                                  │
                                  ▼
                         ┌────────────────┐
                         │  Capability    │
                         └───────┬────────┘
                                 │
                              enables
                                 │
                                 ▼
                         ┌────────────────┐
                         │   Execution    │
                         └───────┬────────┘
                                 │
                              produces
                                 │
                                 ▼
                         ┌────────────────┐
                         │    Outcome     │
                         └────────────────┘

Cross-cutting concepts:

Policy ───────────────► Trust / Authority / Action
Constraint ───────────► Intent / Action / Execution
Evidence ─────────────► Resolution / Trust / Verification
Authority ────────────► Action / Execution
Provenance ───────────► All material decisions and transitions
State ────────────────► Intent / Action / Execution / Outcome
Resource ─────────────► Action / Capability / Outcome
System ───────────────► Capability / Business State

⸻

9. The Intent-to-Action Boundary

The most important conceptual boundary in Noema is:

                UNDERSTANDING
                     │
                     ▼
                  Intent
                     │
                     │
═════════════════════╪═════════════════════
                     │
                  Trust
                     │
═════════════════════╪═════════════════════
                     │
                     ▼
                 Action
                     │
                EXECUTION

The first side is dominated by interpretation and probabilistic reasoning.

The second side requires deterministic controls.

Trust is the boundary.

This boundary is foundational to Noema’s architecture.

⸻

10. The Authority Boundary

A second important boundary is:

Capability
    │
    │ "can the system do this?"
    ▼
    X
    │
    │ "may this Actor cause this?"
    ▼
Authority

Capability and Authority must never be collapsed.

The existence of a Capability means an operation is technically possible.

Authority determines whether a particular Actor may cause that operation under the applicable conditions.

⸻

11. The Business-State Boundary

A third important boundary is:

                 NOEMA
        ┌─────────────────────┐
        │                     │
        │ Intent State        │
        │ Trust State         │
        │ Action State        │
        │ Execution State     │
        │                     │
        └──────────┬──────────┘
                   │
                   │ acts through
                   ▼
        ┌─────────────────────┐
        │ External Systems    │
        │                     │
        │ Business State      │
        │                     │
        └─────────────────────┘

Noema coordinates with business systems but does not become the authoritative owner of their business state.

⸻

12. Canonical Concept Categories

For clarity, Noema concepts can be categorized as follows.

Entities

Actor
Intent
Action
Capability
Resource
System

Contextual Concepts

Context
Constraint
Policy
Evidence

Authority Concepts

Identity
Authority
Role
Delegation
Authorization

Execution Concepts

Contract
Execution
State
Outcome

Epistemic Concepts

Confidence
Trust
Evidence
Provenance

Some concepts intentionally appear in multiple categories because their relationships cross conceptual boundaries.

⸻

13. Concepts That Must Not Be Collapsed

The following distinctions are canonical:

Actor       ≠ Identity
Actor       ≠ Authority
Actor       ≠ User
Intent      ≠ Action
Action      ≠ Execution
Action      ≠ Outcome
Capability  ≠ Authority
Capability  ≠ Permission
Capability  ≠ Trust
Confidence  ≠ Trust
Trust       ≠ Authorization
Policy      ≠ Constraint
Evidence    ≠ Confidence
Business State ≠ Intent State

These distinctions are not merely terminological.

They represent different responsibilities and failure modes in the Noema architecture.

⸻

14. Ontological Invariants

Invariant 1

Intent is the central object of the Noema model.

Invariant 2

An Actor participates in an Intent but is not the Intent itself.

Invariant 3

An Action is an operation that can advance an Intent.

Invariant 4

A Capability establishes what a system can do.

Invariant 5

Authority establishes what an Actor may cause.

Invariant 6

Trust establishes whether Noema has sufficient grounds to proceed.

Invariant 7

Confidence does not establish Trust.

Invariant 8

Execution represents an attempt to perform an Action.

Invariant 9

Outcome represents what actually happened.

Invariant 10

Business State remains owned by the relevant system of record.

Invariant 11

Material relationships and decisions must have sufficient provenance.

Invariant 12

Ambiguity must be representable as explicit state.

Invariant 13

Noema must preserve conceptual distinctions even when implementation layers combine them internally.

⸻

15. Ontology Dependency Order

The ontology should be developed in dependency order.

Actor
  │
  ├─────────────┐
  ▼             ▼
Identity       Intent
                 │
                 ▼
              Context
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
   Constraint            Policy
       │                   │
       └─────────┬─────────┘
                 ▼
               Trust
                 │
        ┌────────┴────────┐
        ▼                 ▼
      Action          Authority
        │
        ▼
   Capability
        │
        ▼
    Execution
        │
        ▼
     Outcome

This ordering is conceptual rather than a strict implementation dependency.

⸻

16. Relationship to Individual Ontology Documents

This document provides the ontology map.

Detailed definitions belong in:

01-ontology/
├── actor.md
├── action.md
├── capability.md
├── intent.md
├── context.md
├── state.md
├── outcome.md
├── policy.md
├── constraint.md
├── authority.md
├── resource.md
├── identity.md
└── relationships.md

When a detailed ontology document conflicts with this document, the conflict must be resolved explicitly rather than allowing terminology to diverge silently.

⸻

17. Ontology and Implementation

The ontology is independent of implementation.

For example, the ontology may define:

Capability:
payments.transfer.create

without requiring a specific:

* HTTP endpoint
* GraphQL mutation
* gRPC method
* SDK
* database
* programming language
* AI model
* infrastructure provider

Implementation details belong in the architecture and contract layers.

The ontology defines meaning.

The contracts define executable semantics.

The architecture defines implementation.

⸻

18. Ontology and Research

Research may introduce new concepts or challenge existing ones.

However, a concept does not become canonical merely because it appears in:

* a paper
* an agent framework
* an AI model
* an external architecture
* an industry standard
* an experiment

A proposed concept should be evaluated for:

1. semantic necessity
2. relationship to existing concepts
3. architectural consequences
4. operational usefulness
5. compatibility with Noema’s invariants

Only then should it become part of the canonical ontology.

⸻

19. The Minimal Noema Vocabulary

If Noema were reduced to its smallest meaningful vocabulary, the following concepts would remain:

Actor
Intent
Trust
Action
Capability
Execution
Outcome

Everything else exists to provide sufficient context, authority, evidence, constraint, or explanation around these concepts.

The minimal lifecycle is therefore:

ACTOR
   ↓
INTENT
   ↓
TRUST
   ↓
ACTION
   ↓
CAPABILITY
   ↓
EXECUTION
   ↓
OUTCOME

⸻

20. Canonical Summary

The Noema ontology models the entities, relationships, and states required to transform human Intent into trusted, bounded, executable Actions while preserving the distinction between participation, authority, capability, execution, and business outcome.

At the highest level:

Actor
  ↓
Intent
  ↓
Context
  ↓
Trust
  ↓
Action
  ↓
Capability
  ↓
Execution
  ↓
Outcome

With:

Identity
Authority
Policy
Constraint
Evidence
Resource
State
Provenance

providing the context and constraints around that lifecycle.

The ontology exists to give Noema a stable language for intent and execution independent of any particular model, interface, enterprise application, or implementation technology.