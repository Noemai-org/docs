Glossary

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/glossary.md

⸻

1. Purpose

The Noema Glossary defines the canonical meaning of terms used throughout the Noema architecture, documentation, specifications, APIs, and engineering discussions.

Its purpose is to prevent semantic drift.

If a term has a defined meaning in the Canon, Noema documentation must use that meaning consistently.

The Glossary is not intended to explain every concept in depth.

Detailed semantics belong in the relevant canonical ontology documents.

⸻

2. Normative Language

The following terms are used according to their normal specification meaning:

Term	Meaning
MUST	Absolute requirement
MUST NOT	Absolute prohibition
SHOULD	Recommended unless a justified exception exists
SHOULD NOT	Generally prohibited unless justified
MAY	Optional
CAN	Describes capability, not permission

⸻

3. Core Noema Vocabulary

Action

A concrete operation that can be performed by a system, Actor, or Capability.

Examples:

CreateAccount
RenewCard
CancelSubscription
TransferFunds

See: action.md

⸻

Actor

An Entity capable of expressing an Intent or initiating an Action.

Examples:

Customer
Employee
Administrator
Service
Agent

See: actor.md

⸻

Authority

The recognized permission or organizational basis allowing an Actor to perform an Action or access an Entity.

Authority answers:

Is this Actor permitted to do this?

Authority is distinct from Capability.

⸻

Capability

A defined ability to perform a class of Actions.

Examples:

card.renew
account.read
payment.refund

Capability answers:

What can this system or integration do?

See: capability.md

⸻

Candidate

A possible interpretation, Entity, Action, Capability, or other semantic result produced during resolution.

A Candidate is not necessarily the final canonical selection.

Candidate
   ≠
Resolved Value

⸻

Clarification

A deterministic request for additional information required to resolve a material ambiguity or missing requirement.

Example:

User:
"Cancel my subscription."
Noema:
"You have both Pro and Enterprise subscriptions. Which one
would you like to cancel?"

Clarification is preferable to unsupported guessing when material ambiguity exists.

⸻

Concept

An abstract semantic type or category used to describe Entities or domain meaning.

Example:

Concept:
Card
Entities:
card_123
card_456

See: concepts.md

⸻

Constraint

A condition, boundary, or restriction that limits what may be valid, permitted, or executable.

Examples:

Refund <= original payment amount
Transfer requires sufficient balance
Approval required above $50,000

See: constraint.md

⸻

Context

The relevant information, circumstances, relationships, and state surrounding an Intent, Action, or decision.

Context answers:

What matters about the situation?

See: context.md

⸻

Decision

A resolved determination made by Noema concerning interpretation, validation, trust, Action selection, or execution.

Examples:

Intent resolved
Entity resolved
Action permitted
Clarification required
Execution denied

A Decision is not synonymous with model output.

⸻

Entity

A distinct, identifiable thing within a domain.

Examples:

Customer
Account
Card
Payment
Invoice
Subscription

See: entities.md

⸻

Evidence

Information that supports or contradicts a proposition, decision, Entity resolution, or Context fact.

Evidence answers:

What supports this conclusion?

Evidence is distinct from Context and Authority.

⸻

Execution

The actual invocation or performance of an Action against an external or internal system.

Action Definition
      ↓
Execution
      ↓
Observed Outcome

Execution is distinct from planning or intent interpretation.

⸻

Intent

The desired objective or outcome expressed or implied by an Actor.

Example:

"Renew my expired card."

Possible canonical representation:

Intent
├── Actor
├── Objective
├── Target
├── Constraints
└── Context

Intent is not Action.

⸻

Intent Resolution

The process of transforming an expressed request into a canonical, structured Intent representation.

Natural Language
      ↓
Candidate Interpretations
      ↓
Context / Evidence
      ↓
Resolved Intent

⸻

Outcome

The observable result of an attempted or completed Action.

Examples:

Card renewed
Payment refunded
Transfer rejected
Account created

Outcome describes what happened.

It is not what the Actor intended to happen.

⸻

Policy

A rule or organizational/business requirement governing behavior, eligibility, or decision-making.

Example:

Cards may be renewed up to 30 days before expiry.

A Policy may produce or imply Constraints.

Policy and Constraint are related but distinct.

⸻

Provenance

Information describing where a fact, Entity, decision input, or other information originated.

Examples:

Source:
Banking API
Observed At:
2026-08-23T12:05:00+01:00

Provenance answers:

Where did this information come from?

⸻

Resource

An Entity that is relevant as an object of an Action.

Example:

Entity:
Card
Action:
Renew Card
Role:
Resource

Resource is therefore often a contextual role played by an Entity.

⸻

Resolution

The process of determining the canonical interpretation of an ambiguous or non-canonical input.

Resolution may apply to:

Intent
Entity
Action
Capability
Reference
Context

⸻

State

The condition of an Entity, Resource, system, or process at a particular point in time.

Examples:

Card = expired
Account = active
Payment = pending
API = unavailable

State is temporal and may change.

⸻

Trust

The determination that an Intent, Action, Entity resolution, Context, or execution satisfies the required conditions for proceeding.

Trust is a Noema-controlled decision boundary.

Model Output
      ↓
Noema Validation
      ↓
Trust Decision
      ↓
Execute / Clarify / Deny / Escalate

Trust is not equivalent to model confidence.

⸻

4. Intent Vocabulary

Objective

The desired result represented by an Intent.

Example:

Intent:
"Renew my card."
Objective:
Renew Card

⸻

Target

The Entity or Entities that an Intent or Action concerns.

Example:

Intent:
"Renew my card."
Target:
card_123

⸻

Intent Parameter

A structured value required to fully specify an Intent.

Examples:

destination = London
amount = $500
date = 2026-09-12

⸻

Intent State

The lifecycle state of an Intent within Noema.

Possible states may include:

RECEIVED
INTERPRETING
AMBIGUOUS
RESOLVED
VALIDATING
TRUSTED
EXECUTING
COMPLETED
FAILED
CANCELLED

The exact lifecycle should be defined by the Intent State specification rather than this glossary.

⸻

5. Entity Vocabulary

Entity Type

The Concept defining the type of an Entity.

Entity Type:
Card
Entity:
card_123

⸻

Entity Identifier

A value used to identify an Entity.

An Entity may possess multiple identifiers across systems.

⸻

Entity Reference

A natural-language or structured reference to an Entity.

Examples:

"my card"
"the primary account"
"account 123"
"the subscription we discussed"

⸻

Entity Resolution

The process of determining which canonical Entity a reference refers to.

⸻

Canonical Entity

The Entity selected as the authoritative semantic representation for a resolved reference.

⸻

6. Action Vocabulary

Action Type

A canonical category of Action.

Examples:

Create
Read
Update
Delete
Transfer
Approve
Cancel
Renew

⸻

Action Instance

A specific execution of an Action against a specific target and Context.

Action Type:
RenewCard
Action Instance:
renew card_123 for customer_456

⸻

Action Contract

The explicit definition of what an Action requires and what it guarantees.

An Action Contract may specify:

Inputs
Targets
Preconditions
Constraints
Authorization
Side Effects
Expected Outcome
Failure Conditions

⸻

Side Effect

A material change caused by an Action beyond simply returning information.

Examples:

Sending an email
Charging a card
Changing account state
Creating a record

⸻

7. Capability Vocabulary

Capability Definition

A declaration of an available ability.

Example:

Capability:
card.renew

⸻

Capability Provider

The system, service, integration, or component that provides a Capability.

⸻

Capability Contract

The formal interface describing how a Capability can be invoked and what it guarantees.

⸻

Capability Availability

Whether a Capability is currently available for invocation.

AVAILABLE
UNAVAILABLE
DEGRADED
UNKNOWN

Capability availability is contextual and temporal.

⸻

8. Context Vocabulary

Context Fact

An individual piece of information contributing to effective Context.

Example:

customer.subscription.status = active

⸻

Effective Context

The Context that Noema has determined to be sufficiently relevant and valid for a particular decision.

⸻

Context Snapshot

A representation of relevant Context at a particular point in time.

⸻

Context Requirement

A piece of Context required to make a particular decision.

Example:

Action:
RefundPayment
Context Requirements:
- payment exists
- payment is refundable
- Actor is authorized

⸻

Context Conflict

A condition in which multiple Context facts materially contradict one another.

⸻

9. Trust Vocabulary

Trust Decision

A deterministic decision concerning whether Noema may proceed with a proposed Intent, Action, or execution.

Possible outcomes:

TRUSTED
REJECTED
CLARIFICATION_REQUIRED
ESCALATION_REQUIRED

⸻

Trust Boundary

The point at which Noema transitions from interpreting or proposing behavior to authorizing consequential behavior.

The Trust Boundary is one of Noema’s most important architectural boundaries.

⸻

Model Confidence

A probabilistic estimate produced by a model concerning its own output.

Model Confidence:

≠ Trust
≠ Authority
≠ Truth

A high model confidence score does not automatically authorize execution.

⸻

Deterministic Validation

Validation performed according to explicit rules, contracts, policies, constraints, authority, or authoritative system state rather than model probability.

⸻

10. Authority Vocabulary

Authorization

The determination that an Actor is permitted to perform a particular Action against a particular Entity under specific Context.

Actor
+
Action
+
Target
+
Context
      ↓
Authorization

⸻

Authority Source

The system, policy, role, organizational structure, or other source establishing Authority.

⸻

Scope of Authority

The set of Entities, Actions, resources, or conditions over which an Actor’s Authority applies.

⸻

11. Evidence Vocabulary

Evidence Source

The source from which Evidence originates.

Examples:

Banking API
CRM
Database
User statement
Signed document
Identity provider

⸻

Evidence Status

The semantic status of Evidence.

Possible statuses:

CONFIRMED
UNCONFIRMED
CONFLICTING
STALE
INVALID

The canonical statuses should be defined separately if the Trust system formalizes them.

⸻

12. Provenance Vocabulary

Source

The system, Actor, document, service, or other origin from which information was obtained.

⸻

Observation

A fact recorded from a source at a particular point in time.

Observation:
balance = $500
Source:
Banking API
Observed At:
12:05

⸻

Lineage

The trace connecting information to its source and subsequent semantic use.

Source
  ↓
Observation
  ↓
Context
  ↓
Decision
  ↓
Action
  ↓
Outcome

⸻

13. Execution Vocabulary

Execution Request

A request to perform an Action after it has passed the required validation and Trust checks.

⸻

Execution Attempt

A concrete attempt to invoke an Action.

An Action may have multiple Execution Attempts.

⸻

Execution Result

The immediate technical result returned by an execution.

Example:

HTTP 200
transaction_id = tx_123

Execution Result is not necessarily equivalent to the final business Outcome.

⸻

Execution Failure

A condition in which an Action cannot be successfully executed.

Examples:

Timeout
Unavailable Capability
Authorization Failure
Validation Failure
External System Error

⸻

14. Outcome Vocabulary

Expected Outcome

The result an Intent or Action is intended to produce.

⸻

Observed Outcome

The result actually observed after execution.

These must remain distinct.

Expected Outcome
        ≠
Observed Outcome

⸻

Outcome Verification

The process of determining whether the observed result satisfies the expected Outcome.

⸻

15. Business Vocabulary

Business State

The current state of a business Entity or process maintained by the authoritative business system.

Noema may consume Business State but does not necessarily own it.

⸻

System of Record

The authoritative system responsible for maintaining a particular category of business information.

Example:

Banking System → account balance
CRM → customer profile
Billing System → subscription status

⸻

Business Rule

A rule describing domain-specific behavior or eligibility.

Business Rules may be expressed through Policies and Constraints.

⸻

16. Semantic Vocabulary

Canonical

The representation designated by Noema as the authoritative semantic representation of a concept.

⸻

Semantic Contract

An explicit definition of the meaning, structure, requirements, and guarantees associated with a Noema concept.

⸻

Ontology

The formal vocabulary and relationships used to represent the domain of Noema.

The ontology defines what things mean.

⸻

Taxonomy

A hierarchical classification of concepts.

Example:

Action
├── Financial Action
│   ├── Transfer
│   └── Refund
└── Account Action
    ├── Create
    └── Cancel

Ontology is broader than taxonomy.

⸻

Schema

A structural representation of data.

A Schema describes how information is represented.

Ontology describes what that information means.

Ontology
   ↓
Meaning
Schema
   ↓
Representation

⸻

17. Model Vocabulary

Model

A probabilistic system used to interpret, classify, generate, or transform information.

⸻

Model Output

Information produced by a Model.

Model Output is not automatically canonical Noema state.

⸻

Model Proposal

A candidate interpretation, Entity resolution, Action, or other semantic result proposed by a Model for Noema to evaluate.

⸻

Model Inference

A conclusion generated by a Model that is not directly established by authoritative evidence.

Model Inference must remain distinguishable from confirmed information.

⸻

18. Deterministic Vocabulary

Deterministic

A behavior whose result is governed by explicit inputs and defined rules such that the same relevant inputs produce the same decision.

⸻

Probabilistic

A behavior whose result is influenced by uncertainty, probability, or model inference.

Noema may use probabilistic components internally.

However:

Probabilistic generation does not automatically constitute deterministic authorization.

⸻

Deterministic State

A Noema state in which the information necessary to make the relevant decision is sufficiently established.

⸻

Uncertainty

A condition in which Noema cannot establish a required fact, interpretation, Entity, or decision with sufficient certainty.

Uncertainty must be represented explicitly when material.

⸻

19. Clarification Vocabulary

Clarification State

A deterministic Noema state in which additional information is required before proceeding.

⸻

Clarification Requirement

The specific missing or ambiguous information that must be resolved.

Example:

Missing:
Target Account

⸻

Clarification Question

The user-facing request designed to resolve a Clarification Requirement.

⸻

20. Integration Vocabulary

Integration

A connection between Noema and an external system or service.

⸻

Connector

The implementation responsible for communicating with an external system.

⸻

External System

A system outside Noema that provides data, capabilities, or execution.

⸻

Adapter

A component that translates between Noema’s canonical semantic representation and an external system’s representation.

⸻

21. Lifecycle Vocabulary

Received

An Intent or request has entered Noema but has not yet been resolved.

⸻

Resolved

The relevant semantic interpretation has been established sufficiently for the next stage.

⸻

Validated

Required structural, semantic, contextual, and contractual checks have passed.

⸻

Trusted

Noema has determined that the relevant operation may proceed across the Trust Boundary.

⸻

Executing

An Action is currently being performed.

⸻

Completed

Execution produced an accepted successful Outcome.

⸻

Failed

Execution or validation produced an unsuccessful result.

⸻

Rejected

Noema explicitly determined that the request or proposed Action must not proceed.

⸻

Escalated

The request has been transferred to a human or higher-authority process because Noema cannot safely resolve or execute it autonomously.

⸻

22. Canonical Term Relationships

The core vocabulary can be summarized as:

Actor
  │
  │ expresses
  ▼
Intent
  │
  ├── concerns ─────► Entity
  │
  ├── interpreted using ─► Context
  │
  └── constrained by ────► Constraint
                                │
                                ▼
                           Policy / Authority
                                │
                                ▼
                           Trust Decision
                                │
                                ▼
                              Action
                                │
                                ▼
                           Execution
                                │
                                ▼
                             Outcome

Capabilities provide the executable abilities:

Action
   │
   └── requires ───► Capability
                          │
                          └── provided by ───► External System

⸻

23. Terms That Must Not Be Used Interchangeably

The following distinctions are normative.

Intent vs Action

Intent = desired objective
Action = operation performed to achieve it

Entity vs Resource

Entity = identifiable thing
Resource = Entity in an actionable role

Actor vs Entity

Entity = identifiable thing
Actor = Entity capable of participating as an initiator

Capability vs Authority

Capability = ability exists
Authority = permission exists

Context vs State

Context = relevant surrounding information
State = condition at a point in time

Context vs Evidence

Context = information relevant to a decision
Evidence = information supporting or contradicting a proposition

Policy vs Constraint

Policy = governing rule
Constraint = boundary imposed on a decision/action

Model Confidence vs Trust

Model Confidence = model's probabilistic assessment
Trust = Noema's deterministic decision

Expected Outcome vs Observed Outcome

Expected = what should happen
Observed = what actually happened

Identifier vs Identity

Identifier = reference value
Identity = semantic continuity of the Entity

Model Output vs Canonical State

Model Output = proposal
Canonical State = validated Noema representation

⸻

24. Deprecated / Avoided Terminology

Noema documentation SHOULD avoid ambiguous terms when a canonical term exists.

“AI decides”

Prefer:

Model proposes
Noema resolves
Noema validates
Noema decides

The Model should not be described as the final authority over Trust or execution.

⸻

“The AI knows”

Prefer:

Noema has authoritative Context
A source reports
The Model inferred
The system observed

“Knows” is too ambiguous for canonical technical documentation.

⸻

“The AI executes”

Prefer:

Noema authorizes execution
Capability executes the Action
External system performs the operation

⸻

“Intent = command”

Avoid this equivalence.

An Intent expresses an objective.

A command may represent an executable instruction.

⸻

“Tool = Capability”

Avoid treating these as universally synonymous.

A tool may be an implementation mechanism.

Capability is the semantic ability exposed to Noema.

⸻

“Context = memory”

Avoid this equivalence.

Memory may provide information that becomes Context.

Memory itself is not necessarily Context.

⸻

25. Canonical Naming Principles

Noema terminology should follow these principles:

1. Semantic precision

Terms should describe what something means, not merely how it is implemented.

2. Stable abstraction

Ontology terms should remain valid even if the underlying implementation changes.

3. Explicit boundaries

Closely related concepts should remain distinguishable.

4. No overloaded terminology

A single canonical term should not represent multiple materially different concepts.

5. Implementation neutrality

Ontology terms should not unnecessarily encode infrastructure choices.

For example:

Capability

is canonical.

REST endpoint

is an implementation detail.

⸻

26. Canonical Vocabulary Hierarchy

The primary Noema vocabulary can be organized as:

ONTOLOGY
│
├── Concepts
│
├── Entities
│
├── Actors
│
├── Resources
│
├── Actions
│
├── Capabilities
│
├── Intents
│
├── Context
│
├── Constraints
│
├── Policies
│
├── Authority
│
├── Evidence
│
├── State
│
├── Provenance
│
└── Outcomes

The operational relationship is:

Actor
  ↓
Intent
  ↓
Context
  ↓
Entity Resolution
  ↓
Constraints + Authority + Policy
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

⸻

27. Canonical Principles

The Glossary establishes the following vocabulary principles:

1. Intent describes what is wanted.
2. Action describes what is done.
3. Entity describes what the Intent or Action concerns.
4. Actor describes who or what participates as an initiator.
5. Capability describes what can be done.
6. Authority describes what may be done.
7. Context describes what is relevant about the situation.
8. Constraint describes what limits the decision or Action.
9. Policy describes governing rules.
10. Evidence describes what supports or contradicts a proposition.
11. State describes a condition at a point in time.
12. Provenance describes where information came from.
13. Trust describes whether Noema permits progression across a decision boundary.
14. Execution describes an attempted or actual operation.
15. Outcome describes what actually resulted.
16. Model Output is a proposal, not automatically canonical truth.
17. Unknown information must remain unknown until established.
18. Ambiguity must remain explicit until resolved.

⸻

28. Canonical Summary

The Noema vocabulary exists to enforce one fundamental discipline:

Noema must distinguish what the user wants, what the system can do, what it is allowed to do, what information establishes the situation, what thing is being acted upon, what actually happened, and who or what is responsible for each part.

The canonical semantic chain is:

ACTOR
  │
  │ expresses
  ▼
INTENT
  │
  ├──────────────► ENTITY
  │
  ├──────────────► CONTEXT
  │
  └──────────────► CONSTRAINTS
                         │
                         ▼
                    AUTHORITY
                         │
                         ▼
                       TRUST
                         │
                         ▼
                       ACTION
                         │
                         ▼
                    CAPABILITY
                         │
                         ▼
                     EXECUTION
                         │
                         ▼
                      OUTCOME

And the central Noema distinction remains:

MODEL
  │
  │ proposes
  ▼
NOEMA
  │
  ├── resolves
  ├── validates
  ├── establishes context
  ├── checks constraints
  ├── evaluates authority
  └── makes trust decision
              │
              ▼
          EXECUTION

This Glossary should be treated as the vocabulary authority for the rest of the Canon. If a later document needs to introduce a new foundational term, it should either define it here or explicitly reference the document that owns its canonical definition.