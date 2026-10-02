Glossary

Status: Foundational
Version: 0.2
Domain: Ontology
Canonical Path: ontology/glossary.md

⸻

1. Purpose

The Noema Glossary defines the canonical meaning of terms used throughout the Noema architecture, documentation, specifications, contracts, APIs, and engineering discussions.

Its primary purpose is to prevent semantic drift across the Canon.

If a term has a defined meaning in the Canon, Noema documentation MUST use that meaning consistently unless a document explicitly establishes a narrower, domain-specific usage.

The Glossary provides the canonical vocabulary and cross-concept distinctions.

It is not intended to replace the detailed semantic definition of an ontology concept.

Detailed semantics belong in the relevant canonical ontology documents.

For example:

* intent.md defines Intent semantics.
* entities.md defines Entity semantics.
* context.md defines Context semantics.
* constraint.md defines Constraint semantics.
* action.md defines Action semantics.
* capability.md defines Capability semantics.

The Glossary establishes the shared vocabulary through which those documents relate to one another.

⸻

2. Normative Language

The following terms are used according to their specification meaning.

Term	Meaning
MUST	Absolute requirement
MUST NOT	Absolute prohibition
SHOULD	Recommended unless a justified exception exists
SHOULD NOT	Generally prohibited unless justified
MAY	Optional
CAN	Describes capability or possibility, not permission

In particular:

CAN does not mean MAY.

A system can possess a Capability without possessing Authority to exercise it in a particular circumstance.

⸻

3. Core Noema Vocabulary

Action

An Action is a concrete operation that can be performed against a target or set of targets within a Noema execution journey.

Examples:

CreateAccount
RenewCard
CancelSubscription
TransferFunds
RetrieveStatement
RefundPayment

An Action describes what is done, rather than what an Actor wants to accomplish.

See: action.md

⸻

Actor

An Actor is an Entity capable of expressing an Intent, initiating an Action, or participating in an execution according to the applicable semantics.

Examples:

Customer
Employee
Administrator
Service
Agent
Organization

Conceptually:

Actor ⊂ Entity

Not every Entity is an Actor.

See: actor.md

⸻

Authority

Authority is the recognized basis by which an Actor is permitted to perform an Action, access or affect a Resource, or make a decision within a defined scope.

Authority answers:

Who or what is permitted to cause this Action or make this decision?

Authority may arise from:

* role
* organizational position
* delegated authority
* policy
* ownership
* explicit authorization
* system-defined authority

Authority is distinct from Capability.

An Actor may possess Authority without the relevant Capability being available.

A system may possess a Capability without the Actor possessing Authority to invoke it.

See: authority.md

⸻

Capability

A Capability is a defined ability to perform a class of Actions.

Examples:

account.read
card.renew
payment.refund
payment.transfer.create

Capability answers:

What can this system, service, or integration do?

Capability does not answer whether the Action is permitted in the current situation.

See: capability.md

⸻

Candidate

A Candidate is a possible interpretation, Entity, Action, Capability, reference, or other semantic result produced during a resolution process.

A Candidate is not necessarily canonical.

Candidate
   ≠
Resolved Value

Candidates may be generated probabilistically.

Material resolution requires the applicable validation, evidence, authority, constraints, and deterministic rules.

⸻

Clarification

A Clarification is a deterministic request for additional information required to resolve a material ambiguity, missing requirement, or insufficiently specified Constraint or Context.

Example:

User:
"Cancel my subscription."
Noema:
"You have both Pro and Enterprise subscriptions.
Which one would you like to cancel?"

Clarification is the appropriate mechanism when Noema cannot safely establish a required semantic value.

Clarification is preferable to unsupported guessing when the ambiguity is material to the decision or execution.

⸻

Concept

A Concept is an abstract semantic type or category used to define domain meaning.

Example:

Concept:
Card
Entities:
card_123
card_456

Concepts define categories.

Entities represent identifiable instances of those categories.

See: concepts.md

⸻

Constraint

A Constraint is a condition, boundary, or restriction that limits the set of permissible interpretations, Actions, Resources, or Executions associated with an Intent.

Examples:

amount <= $10,000
approval required above $50,000
only use approved vendors
do not send external notifications

Constraint answers:

What must, must not, or may not be violated?

A Constraint is distinct from:

* Intent
* Preference
* Policy
* Authority
* Capability
* Condition
* Permission

A Policy may impose or generate a Constraint, but the Policy and resulting Constraint remain distinct concepts.

See: constraint.md

⸻

Context

Context is the bounded, relevant, authority-aware information available to Noema for interpreting Intent, resolving ambiguity, evaluating Trust, planning Actions, executing against enterprise systems, and verifying Outcomes.

Context answers:

What information is relevant to this decision or execution at this point in time?

Context is not synonymous with:

* Enterprise State
* Business State
* Canonical Data
* Evidence
* Intent
* Conversation History
* Model Input
* Noema State

Context should be purpose-bound and contain the information necessary for the current decision rather than everything available about the Principal or Resource.

See: context.md

⸻

Decision

A Decision is an explicit determination made within Noema concerning interpretation, resolution, validation, authority, Trust, Action selection, clarification, escalation, rejection, or execution progression.

Examples:

Intent resolved
Entity resolved
Constraint satisfied
Authorization established
Clarification required
Execution rejected

A Decision is not synonymous with Model Output.

A Model may propose information used by a Decision.

Noema establishes the Decision through the applicable deterministic rules, evidence, policy, authority, constraints, and Trust model.

⸻

Entity

An Entity is a distinct, identifiable thing that can be represented, referenced, related, observed, or acted upon within a Noema domain.

Examples:

Customer
Account
Card
Payment
Invoice
Subscription
Organization
Document

An Entity may:

* participate in an Intent
* serve as a Resource
* possess State
* have Attributes
* relate to other Entities
* be targeted by an Action
* appear in an Outcome

See: entities.md

⸻

Evidence

Evidence is information that supports or contradicts a proposition, decision, Entity resolution, Context fact, or other material semantic claim.

Evidence answers:

What supports or contradicts this conclusion?

Evidence is distinct from Context.

Context is information available for reasoning or execution.

Evidence describes the support or contradiction associated with a proposition or decision.

Evidence is also distinct from Authority.

A source may be authoritative without every observation from that source automatically being sufficient Evidence for every decision.

See: evidence.md where defined.

⸻

Execution

Execution is the actual invocation or performance of an Action against an internal or external system.

Conceptually:

Action Definition
      ↓
Execution Request
      ↓
Execution Attempt
      ↓
Observed Result
      ↓
Outcome

Execution is distinct from:

* Intent interpretation
* planning
* Action definition
* authorization
* Trust
* Outcome verification

Execution describes what was actually attempted or performed.

See: execution domain specifications.

⸻

Intent

An Intent is the desired objective or outcome expressed or implied by an Actor.

Example:

"Renew my expired card."

Possible canonical representation:

Intent
├── Actor
├── Objective
├── Target
├── Constraints
└── Context

Intent describes what the Actor wants to accomplish.

Intent is not an Action.

See: intent.md

⸻

Intent Resolution

Intent Resolution is the process of transforming an expressed request into a canonical, structured Intent representation.

Conceptually:

Natural Language
      ↓
Candidate Interpretations
      ↓
Context + Evidence
      ↓
Resolution
      ↓
Canonical Intent

Intent Resolution may involve:

* objective identification
* Entity resolution
* parameter extraction
* Constraint extraction
* ambiguity detection
* Context retrieval
* evidence evaluation

A model may propose interpretations during this process, but model output is not automatically canonical Intent.

⸻

Outcome

An Outcome is the observable result of an attempted or completed Action.

Examples:

Card renewed
Payment refunded
Transfer rejected
Account created
Statement retrieved

Outcome describes:

What actually resulted?

It is distinct from:

* Intent
* Expected Outcome
* Execution Result

An Outcome may indicate success, failure, partial completion, rejection, or other observed result according to the applicable domain semantics.

See: outcome.md

⸻

Policy

A Policy is a governing rule or organizational, regulatory, business, or system requirement that establishes permissible behavior, eligibility, obligations, restrictions, or decision requirements.

Example:

Employees may only book economy-class flights.

A Policy may generate or impose one or more Constraints.

Policy
   │
   └── imposes
          ↓
      Constraint

Policy and Constraint remain distinct.

A Policy describes the governing rule.

A Constraint represents an applicable boundary within a particular decision or execution.

See: policy.md

⸻

Provenance

Provenance is information describing the origin, derivation, observation, transformation, or lineage of a fact, Entity, decision input, or other information.

Examples:

Source:
Banking API
Observed At:
2026-08-23T12:05:00+01:00
Version:
482

Provenance answers:

Where did this information come from, when was it observed, and how did it become part of the current semantic representation?

Provenance is particularly important for consequential Context, Evidence, Entity Resolution, Decisions, and Outcomes.

⸻

Resource

A Resource is an Entity occupying a role as an object of an Action.

Example:

Entity:
Card
Action:
Renew Card
Role:
Resource

Resource is therefore a contextual role rather than necessarily a separate ontological category.

Conceptually:

Resource ⊂ Entity

where the Entity is relevant as something that an Action may inspect, create, modify, or otherwise affect.

See: resource.md

⸻

Resolution

Resolution is the process of determining a canonical interpretation for an ambiguous, incomplete, non-canonical, or natural-language input.

Resolution may apply to:

* Intent
* Entity
* Action
* Capability
* Reference
* Context
* parameters
* other semantic values

Resolution should remain distinct from validation.

Resolution determines what the input means.

Validation determines whether the resolved representation satisfies the applicable requirements.

⸻

State

State is the condition of an Entity, Resource, system, workflow, or process at a particular point in time.

Examples:

Card = expired
Account = active
Payment = pending
API = unavailable
Execution = awaiting_verification

State is temporal and may change.

State is distinct from the Entity whose condition it describes.

See: state.md

⸻

Trust

Trust is Noema’s explicit determination that a proposed interpretation, Entity resolution, Action, or execution satisfies the conditions required for progression across the applicable decision boundary.

Trust answers:

May Noema permit this operation to proceed under the applicable evidence, authority, policy, constraints, Context, and risk conditions?

Conceptually:

Model / External Inputs
        ↓
Noema Resolution
        ↓
Validation
        ↓
Trust Decision
        ↓
Execute / Clarify / Reject / Escalate

Trust is not:

* Model Confidence
* Capability
* Authority
* Evidence
* permission in isolation
* successful execution

Trust is a Noema-controlled decision boundary.

See: 03-trust/

⸻

4. Intent Vocabulary

Objective

The Objective is the desired result represented by an Intent.

Example:

Intent:
"Renew my card."
Objective:
Renew Card

Objective describes what the Actor seeks to accomplish.

It is not itself the executable Action.

⸻

Target

A Target is the Entity or Entities that an Intent or Action concerns.

Example:

Intent:
"Renew my card."
Target:
card_123

Target resolution may depend on Context, Evidence, Relationships, Constraints, and Authority.

⸻

Intent Parameter

An Intent Parameter is a structured value required to sufficiently specify an Intent.

Examples:

destination = London
amount = $500
date = 2026-09-12
currency = USD

A missing material Intent Parameter may produce a Clarification Requirement.

⸻

Intent State

Intent State is the lifecycle state of an Intent within Noema.

Possible conceptual states include:

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

The exact lifecycle semantics belong to the Intent State specification.

⸻

5. Entity Vocabulary

Entity Type

An Entity Type is the Concept defining the type of an Entity.

Example:

Entity Type:
Card
Entity:
card_123

The Entity Type describes what kind of Entity the instance represents.

⸻

Entity Identifier

An Entity Identifier is a value used to reference or distinguish an Entity.

An Entity may have multiple identifiers across systems.

Card
├── Noema ID
├── Banking ID
├── CRM ID
└── External Reference

Identifier is not synonymous with Entity Identity.

⸻

Entity Reference

An Entity Reference is a natural-language or structured reference that points to an Entity.

Examples:

"my card"
"the primary account"
"account 123"
"the subscription we discussed"
"it"
"this account"

An Entity Reference may require resolution.

⸻

Entity Resolution

Entity Resolution is the process of determining which canonical Entity a reference refers to.

Conceptually:

Reference
   ↓
Candidate Entities
   ↓
Context + Evidence + Relationships
   ↓
Resolution
   ↓
Canonical Entity

Material Entity Resolution must not silently rely on probability when deterministic resolution is required.

⸻

Canonical Entity

A Canonical Entity is the Entity designated as the canonical semantic representation of a resolved reference within the applicable Noema context.

Canonicalization does not necessarily mean that Noema owns the underlying enterprise Business State.

⸻

6. Action Vocabulary

Action Type

An Action Type is a canonical category or definition of an operation.

Examples:

Create
Read
Update
Delete
Transfer
Approve
Cancel
Renew

An Action Type describes the semantic operation.

⸻

Action Instance

An Action Instance is a specific proposed or executable Action associated with particular Targets, parameters, Context, and execution requirements.

Example:

Action Type:
RenewCard
Action Instance:
Renew card_123 for customer_456

⸻

Action Contract

An Action Contract is the explicit definition of what an Action requires, permits, guarantees, and may cause.

An Action Contract may specify:

* Inputs
* Targets
* Preconditions
* Constraints
* Authority requirements
* Capability requirements
* Side Effects
* Expected Outcome
* Failure Conditions
* Postconditions
* verification requirements

Action Contracts belong primarily to the Contracts domain, while the ontology defines the semantic concept of Action.

See: 11-contracts/

⸻

Side Effect

A Side Effect is a material change or externally observable consequence caused by an Action beyond merely returning information.

Examples:

Sending an email
Charging a card
Changing account state
Creating a record
Issuing a notification

Side Effects are relevant to Action Contracts, Trust, Constraints, and Outcome verification.

⸻

7. Capability Vocabulary

Capability Definition

A Capability Definition is a declaration of an available semantic ability.

Example:

Capability:
card.renew

⸻

Capability Provider

A Capability Provider is the system, service, integration, component, or other execution mechanism that provides a Capability.

The provider is not necessarily the same thing as the Capability.

⸻

Capability Contract

A Capability Contract is the formal interface describing how a Capability can be invoked and what it requires and guarantees.

A Capability Contract may establish:

* supported inputs
* supported Actions
* preconditions
* constraints
* execution semantics
* failure semantics
* output semantics

⸻

Capability Availability

Capability Availability describes whether a Capability is currently available for invocation.

Possible states include:

AVAILABLE
UNAVAILABLE
DEGRADED
UNKNOWN

Availability is contextual and temporal.

Capability Availability does not imply Authority.

⸻

8. Context Vocabulary

Context Fact

A Context Fact is an individual piece of information contributing to effective Context.

Example:

customer.subscription.status = active

A consequential Context Fact may preserve:

subject
attribute
value
source
authority
observed_at
effective_at
expires_at
version
provenance

⸻

Effective Context

Effective Context is the Context that Noema has determined to be sufficiently relevant, scoped, current, and valid for a particular decision or Action.

Effective Context is Action-specific.

Context that is valid for one operation may be insufficient or inappropriate for another.

⸻

Context Snapshot

A Context Snapshot is a representation of relevant Context at a particular point in time.

Snapshots support:

* auditability
* reconstruction
* debugging
* decision explanation
* historical analysis

A Context Snapshot does not become current enterprise truth merely because Noema stores it.

⸻

Context Requirement

A Context Requirement is a piece or category of Context required to make a particular decision or execute a particular Action.

Example:

Action:
RefundPayment
Context Requirements:
- payment exists
- payment status is known
- Actor is authorized
- refund amount is established

⸻

Context Conflict

A Context Conflict exists when multiple Context Facts materially contradict one another.

Example:

Ledger:
balance = $10,000
Cache:
balance = $8,000

Context Conflict must be resolved according to the applicable authority and consistency model rather than model confidence or majority selection.

⸻

Context Completeness

Context Completeness is the condition in which the Context contains the information necessary for the current decision or Action.

Completeness is Action-specific.

Context complete for Action A
        ≠
Context complete for Action B

⸻

Context Freshness

Context Freshness describes whether Context is sufficiently current for the requirements of the relevant decision or Action.

Freshness is distinct from authority.

Information may be authoritative but stale.

⸻

9. Constraint Vocabulary

Constraint Satisfaction

Constraint Satisfaction describes whether an applicable Constraint has been met.

Possible conceptual states include:

SATISFIED
VIOLATED
UNKNOWN
NOT_APPLICABLE
CONFLICTING

In particular:

UNKNOWN ≠ SATISFIED

⸻

Effective Constraint Set

The Effective Constraint Set is the collection of all applicable Constraints that must be satisfied for a particular Action or Execution.

Conceptually:

Intent Constraints
        +
Actor Constraints
        +
Policy Constraints
        +
Authority Constraints
        +
System Constraints
        +
Capability Constraints
        +
Execution Constraints
        ↓
Effective Constraint Set

Not every category exists in every interaction.

Applicability must be established explicitly.

⸻

Constraint Relaxation

Constraint Relaxation is an explicit modification that broadens or otherwise changes an applicable Constraint.

Example:

Original:
budget <= $500
Relaxed:
budget <= $600

Relaxation must preserve the original Constraint, the modified Constraint, the Actor, Authority, reason, timestamp, and applicable policy where material.

A Model must not silently relax a material Constraint.

⸻

Constraint Override

A Constraint Override is an explicit authorization to bypass, suspend, or modify an applicable Constraint.

An Override requires an appropriate:

* Actor
* Authority
* Constraint
* Scope
* Reason
* Validity

Override semantics belong to the applicable Trust, Authority, and Policy specifications.

⸻

10. Trust Vocabulary

Trust Decision

A Trust Decision is a deterministic determination concerning whether Noema may permit a proposed Intent, Entity resolution, Action, or Execution to proceed.

Possible outcomes include:

TRUSTED
REJECTED
CLARIFICATION_REQUIRED
ESCALATION_REQUIRED

Additional states may be defined by the Trust specification.

⸻

Trust Boundary

The Trust Boundary is the architectural decision boundary at which Noema transitions from interpretation, proposal, or planning into permitted consequential behavior.

Conceptually:

Model Proposal
      ↓
Resolution
      ↓
Validation
      ↓
Trust Boundary
      ↓
Execution

The Trust Boundary is distinct from the model itself.

⸻

Model Confidence

Model Confidence is a probabilistic estimate associated with a Model’s output or inference.

Model Confidence
        ≠
Trust
Model Confidence
        ≠
Authority
Model Confidence
        ≠
Truth

A high Model Confidence value does not by itself authorize execution or establish canonical state.

⸻

Deterministic Validation

Deterministic Validation is validation performed according to explicit rules, Contracts, Policies, Constraints, Authority requirements, or authoritative system state.

Deterministic Validation is distinct from probabilistic model confidence.

⸻

11. Authority Vocabulary

Authorization

Authorization is the determination that an Actor is permitted to perform a particular Action against a particular Entity or Resource under specified Context.

Conceptually:

Actor
+
Action
+
Target
+
Scope
+
Context
      ↓
Authorization

Authorization is not equivalent to Capability.

⸻

Authority Source

An Authority Source is the system, Policy, role, organizational structure, delegation, ownership relationship, or other recognized basis establishing Authority.

⸻

Scope of Authority

Scope of Authority is the set of Actions, Entities, Resources, organizations, environments, conditions, or other boundaries within which Authority applies.

Authority without scope is insufficient to establish unrestricted permission.

⸻

Delegated Authority

Delegated Authority is Authority exercised by one Actor on behalf of another Actor or Principal under explicitly defined scope and constraints.

Delegation does not automatically transfer all Authority of the delegating Actor.

⸻

12. Evidence Vocabulary

Evidence Source

An Evidence Source is the source from which Evidence originates.

Examples:

Banking API
CRM
Database
User statement
Signed document
Identity provider
System of Record

⸻

Evidence Status

Evidence Status describes the semantic condition of Evidence.

Possible conceptual statuses include:

CONFIRMED
UNCONFIRMED
CONFLICTING
STALE
INVALID
UNKNOWN

The exact normative status set belongs to the Evidence and Trust specifications.

⸻

Observation

An Observation is information recorded from a source at a particular point in time.

Example:

Observation:
balance = $500
Source:
Banking API
Observed At:
12:05

An Observation is not necessarily equivalent to current Business State.

⸻

13. Provenance Vocabulary

Source

A Source is the system, Actor, document, service, database, integration, or other origin from which information was obtained.

⸻

Observation Time

Observation Time is the time at which a fact or value was observed from its source.

Observation Time is distinct from:

* Effective Time
* Execution Time
* Recording Time

⸻

Effective Time

Effective Time is the time at which a fact, Policy, State, or other semantic value is considered applicable in its domain.

⸻

Lineage

Lineage is the trace connecting information to its source, transformations, semantic use, and resulting decisions or Outcomes.

Conceptually:

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

Lineage is a form of provenance.

⸻

14. Execution Vocabulary

Execution Request

An Execution Request is a request to perform an Action after the required semantic, contractual, authority, Constraint, and Trust requirements have been satisfied.

⸻

Execution Attempt

An Execution Attempt is a concrete attempt to invoke or perform an Action.

One Action may have multiple Execution Attempts.

Action
  ├── Attempt 1
  ├── Attempt 2
  └── Attempt 3

Each Attempt should remain distinguishable for audit and recovery.

⸻

Execution Result

An Execution Result is the immediate technical result returned by an Execution Attempt.

Example:

HTTP 200
transaction_id = tx_123

Execution Result is not necessarily equivalent to final business Outcome.

A successful technical response may still require Outcome verification.

⸻

Execution Failure

An Execution Failure is a condition in which an Action cannot be successfully completed or its result cannot be established according to the applicable execution semantics.

Examples:

Timeout
Unavailable Capability
Authorization Failure
Validation Failure
External System Error
Unknown Result

An Execution Failure is distinct from a Constraint Violation.

⸻

15. Outcome Vocabulary

Expected Outcome

An Expected Outcome is the result an Intent or Action is intended or contractually expected to produce.

Example:

Intent:
"Renew my card."
Expected Outcome:
Card status becomes renewed/active according to domain semantics.

⸻

Observed Outcome

An Observed Outcome is the result actually observed after an Execution Attempt or subsequent verification.

Expected Outcome
        ≠
Observed Outcome

The two must remain distinct.

⸻

Outcome Verification

Outcome Verification is the process of determining whether the Observed Outcome satisfies the Expected Outcome and applicable Postconditions.

Conceptually:

Execution
   ↓
Observed Result
   ↓
Fresh Context / Evidence
   ↓
Outcome Verification
   ↓
Outcome

⸻

16. Business Vocabulary

Business State

Business State is the current state of a business Entity, Resource, or process maintained by the authoritative enterprise system for that domain.

Examples:

Account.balance
Payment.status
Card.status
Subscription.status
Inventory.quantity

Noema may consume Business State through Context.

Noema does not become the owner of Business State merely by representing it.

⸻

System of Record

A System of Record is the authoritative system responsible for maintaining a particular category of enterprise Business State or canonical business information.

Examples:

Banking System → account balance
CRM → customer profile
Billing System → subscription status

Authority may be property-specific.

One System of Record need not be authoritative for every attribute of an Entity.

⸻

Business Rule

A Business Rule is a domain-specific rule describing business behavior, eligibility, conditions, obligations, or permissible operations.

Business Rules may be expressed through:

* Policy
* Constraint
* Action Contract
* enterprise system rules

The implementation of a Business Rule does not determine its ontology-level meaning.

⸻

17. Semantic Vocabulary

Canonical

Canonical describes the representation designated by Noema as the authoritative semantic representation for a particular concept within the applicable scope.

Canonical does not necessarily mean:

* source-of-record ownership
* enterprise authority
* physical persistence
* immutability

For example, Noema may maintain a canonical Intent representation while an enterprise system remains authoritative for the underlying Business State.

⸻

Semantic Contract

A Semantic Contract is an explicit definition of the meaning, structure, requirements, boundaries, or guarantees associated with a Noema concept.

Semantic Contracts establish stable meaning independently of implementation details.

⸻

Ontology

An Ontology is the formal vocabulary of concepts, Entities, relationships, distinctions, properties, and semantic rules used to represent the Noema domain.

The ontology defines:

What things mean and how they relate.

⸻

Taxonomy

A Taxonomy is a hierarchical classification of Concepts or other semantic categories.

Example:

Action
├── Financial Action
│   ├── Transfer
│   └── Refund
└── Account Action
    ├── Create
    └── Cancel

Ontology is broader than Taxonomy.

A taxonomy describes classification.

An ontology also describes relationships, properties, boundaries, and semantics.

⸻

Schema

A Schema is a structural representation of information.

A Schema describes:

How information is represented.

Ontology describes:

What that information means.

Therefore:

Ontology
   ↓
Meaning
Schema
   ↓
Representation

An implementation Schema must not redefine canonical ontology semantics without an explicit semantic change.

⸻

18. Model Vocabulary

Model

A Model is a probabilistic computational system used to interpret, classify, generate, infer, retrieve, transform, or otherwise process information.

The Model is a component within Noema.

It is not the canonical authority for Trust or enterprise Business State.

⸻

Model Output

Model Output is information produced by a Model.

Model Output may include:

* interpretation
* Entity candidates
* Action candidates
* extracted Constraints
* classifications
* proposed parameters
* summaries
* inferences

Model Output is not automatically canonical Noema state.

⸻

Model Proposal

A Model Proposal is a candidate semantic interpretation or operation proposed by a Model for Noema to evaluate.

Examples:

Proposed Intent
Proposed Entity
Proposed Action
Proposed Constraint
Proposed Parameter

A Model Proposal becomes canonical only through the applicable resolution and validation process.

⸻

Model Inference

A Model Inference is a conclusion generated by a Model that is not directly established by authoritative Evidence.

Model Inference must remain distinguishable from:

* observed fact
* canonical state
* authoritative Context
* Evidence
* validated resolution

⸻

19. Deterministic Vocabulary

Deterministic

Deterministic describes behavior whose result is governed by defined inputs and explicit rules such that equivalent relevant inputs produce the same semantic decision.

Determinism applies to the governing decision logic, not necessarily to every upstream Model component.

⸻

Probabilistic

Probabilistic describes behavior whose result is influenced by uncertainty, probability, statistical inference, or Model behavior.

Noema may use probabilistic components for:

* interpretation
* candidate generation
* extraction
* classification
* retrieval
* ranking

Probabilistic generation does not automatically constitute deterministic authorization.

⸻

Deterministic State

A Deterministic State is a Noema state in which the information necessary for the relevant decision has been sufficiently established according to the applicable rules.

⸻

Uncertainty

Uncertainty is a condition in which Noema cannot establish a required fact, interpretation, Entity, Context value, or decision with sufficient certainty for the relevant operation.

Material Uncertainty must be represented explicitly.

UNKNOWN

must not silently become:

PROBABLY TRUE

when the distinction affects consequential execution.

⸻

20. Clarification Vocabulary

Clarification State

A Clarification State is a deterministic Noema state in which additional information is required before the execution journey can safely progress.

⸻

Clarification Requirement

A Clarification Requirement is the specific missing, ambiguous, conflicting, or insufficiently specified information that must be resolved.

Example:

Missing:
Target Account

⸻

Clarification Question

A Clarification Question is the user-facing request designed to resolve a Clarification Requirement.

The question should request the minimum information necessary to establish the missing semantic value.

⸻

21. Integration Vocabulary

Integration

An Integration is a connection between Noema and an external or internal system through which data, capabilities, events, or execution may be accessed.

⸻

Connector

A Connector is an implementation component responsible for communicating with an external system.

The Connector is an implementation mechanism.

It is not itself the canonical semantic definition of the Capability or Entity.

⸻

External System

An External System is a system outside the relevant Noema execution boundary that provides data, capabilities, events, or execution.

Examples may include:

* Banking Systems
* CRM systems
* payment processors
* identity providers
* enterprise databases

⸻

Adapter

An Adapter is a component that translates between Noema’s canonical semantic representation and an external system’s representation.

Conceptually:

Noema Canonical Representation
             ↓
          Adapter
             ↓
External Representation

Adapters should preserve semantic meaning rather than silently redefining it.

⸻

22. Lifecycle Vocabulary

Received

Received means that an Intent or request has entered Noema but has not yet completed semantic resolution.

⸻

Resolved

Resolved means that the relevant semantic interpretation has been established sufficiently for the next required stage.

Resolution does not automatically mean Trust.

⸻

Validated

Validated means that the relevant structural, semantic, contextual, contractual, Constraint, and other required checks have passed according to the applicable specification.

Validation does not automatically mean execution.

⸻

Trusted

Trusted means that Noema has determined that the relevant operation may proceed across the applicable Trust Boundary.

Trusted does not mean that execution has succeeded.

⸻

Executing

Executing means that an Action is currently undergoing an Execution Attempt.

⸻

Completed

Completed means that the execution journey has reached an accepted terminal successful state according to the applicable Outcome and verification semantics.

⸻

Failed

Failed means that validation, execution, verification, or another required stage produced an unsuccessful terminal result.

⸻

Rejected

Rejected means that Noema explicitly determined that a request, interpretation, Action, or Execution must not proceed.

⸻

Escalated

Escalated means that the execution journey has been transferred to a human or higher-authority process because the relevant issue cannot or should not be resolved autonomously.

⸻

23. Canonical Term Relationships

The core vocabulary can be summarized as:

Actor
  │
  │ expresses
  ▼
Intent
  │
  ├── concerns ─────────► Entity
  │                         │
  │                         └── may serve as Resource
  │
  ├── interpreted using ─► Context
  │
  └── constrained by ────► Constraints
                              │
                              ├── may derive from Policy
                              ├── may arise from Authority
                              └── may arise from Capability/System
                                      │
                                      ▼
                               Trust Decision
                                      │
                                      ├── Clarify
                                      ├── Escalate
                                      ├── Reject
                                      └── Proceed
                                             │
                                             ▼
                                           Action
                                             │
                                             ├── requires ─► Capability
                                             │
                                             ▼
                                         Execution
                                             │
                                             ▼
                                          Outcome

The broader semantic chain is:

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
                 AUTHORITY / POLICY
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

⸻

24. Terms That Must Not Be Used Interchangeably

The following distinctions are normative.

Intent vs Action

Intent = desired objective
Action = operation performed to achieve or attempt the objective

An Intent may be satisfied through different possible Actions.

⸻

Entity vs Resource

Entity = identifiable thing
Resource = Entity occupying an actionable role

An Entity is not permanently a Resource.

⸻

Actor vs Entity

Entity = identifiable thing
Actor = Entity participating as an initiator or participant according to applicable semantics

Not every Entity is an Actor.

⸻

Capability vs Authority

Capability = ability exists
Authority = permission exists

A system may be capable of performing an Action without being authorized to perform it in a particular context.

⸻

Context vs State

Context = bounded relevant information
State = condition at a point in time

State may be represented within Context, but Context is broader than State.

⸻

Context vs Evidence

Context = information available for a decision or execution
Evidence = information supporting or contradicting a proposition or decision

A Context Fact may have Evidence supporting it.

⸻

Policy vs Constraint

Policy = governing rule
Constraint = applicable boundary imposed on a decision, Action, Resource, or Execution

A Policy may generate a Constraint.

⸻

Constraint vs Preference

Constraint = binding boundary
Preference = desirable characteristic

A Preference must not silently become a Constraint.

A Soft Constraint, where supported, must retain explicit semantics and must not become an excuse for silent relaxation.

⸻

Authority vs Constraint

Authority = who or what may act
Constraint = what boundaries apply

Authority does not automatically remove Constraints.

⸻

Capability vs Constraint

Capability = what can be done
Constraint = what limits what may be done

Capability does not override Constraint.

⸻

Model Confidence vs Trust

Model Confidence = probabilistic assessment
Trust = Noema decision boundary

Confidence does not establish Trust.

⸻

Expected Outcome vs Observed Outcome

Expected Outcome = what should result
Observed Outcome = what actually resulted

They must remain separately represented.

⸻

Identifier vs Identity

Identifier = reference value
Identity = semantic continuity of the Entity

One Entity may possess multiple identifiers.

⸻

Model Output vs Canonical State

Model Output = proposal or inference
Canonical State = validated Noema representation

Model Output does not automatically become canonical.

⸻

Execution Result vs Outcome

Execution Result = immediate technical result
Outcome = semantically relevant observed result

A technical success does not necessarily establish business success.

⸻

Entity Resolution vs Authorization

Entity Resolution = which Entity is being referenced?
Authorization = may this Actor access or affect it?

A resolved Entity is not necessarily authorized.

⸻

Entity Existence vs Entity Accessibility

Entity Existence = the Entity exists within the relevant domain
Entity Accessibility = the current Actor/System may access it

Knowing an identifier does not establish access.

⸻

Constraint Satisfaction vs Constraint Existence

Constraint Existence = a Constraint applies
Constraint Satisfaction = the Constraint is satisfied

The existence of a Constraint does not imply satisfaction.

⸻

Unknown vs Satisfied

UNKNOWN ≠ SATISFIED

Noema must not treat inability to establish compliance as compliance when the Constraint is material.

⸻

25. Deprecated / Avoided Terminology

Noema documentation SHOULD avoid ambiguous terminology when a canonical term exists.

“AI decides”

Prefer:

Model proposes
Noema resolves
Noema validates
Noema decides

The Model should not be described as the final authority over Trust or consequential execution.

⸻

“The AI knows”

Prefer:

Noema has authoritative Context
A source reports
The system observed
The Model inferred
Evidence establishes

“Knows” is too ambiguous for canonical technical documentation.

⸻

“The AI executes”

Prefer:

Noema authorizes execution
Capability provides the ability
Execution invokes the Action
External system performs the operation

⸻

“Intent = command”

Avoid this equivalence.

An Intent expresses an objective.

A command may represent an executable instruction.

⸻

“Tool = Capability”

Avoid treating these as universally synonymous.

A Tool may be an implementation mechanism.

Capability is the semantic ability exposed to Noema.

⸻

“Context = memory”

Avoid this equivalence.

Memory may provide information that becomes Context.

Memory itself is not necessarily Context.

⸻

“Confidence = certainty”

Avoid this equivalence.

A probabilistic Model Confidence value does not establish canonical truth or Trust.

⸻

“Successful API call = successful business operation”

Avoid this equivalence.

A technical Execution Result may require subsequent verification before a successful business Outcome can be established.

⸻

26. Canonical Naming Principles

Noema terminology should follow these principles.

1. Semantic precision

Terms should describe what something means, not merely how it is implemented.

2. Stable abstraction

Ontology terms should remain valid even when the underlying implementation changes.

3. Explicit boundaries

Closely related concepts must remain distinguishable where the distinction affects interpretation, authorization, Trust, or execution.

4. No overloaded terminology

A single canonical term should not represent multiple materially different concepts.

5. Implementation neutrality

Ontology terms should not unnecessarily encode infrastructure choices.

For example:

Capability

is canonical.

REST endpoint

is an implementation mechanism.

6. Authority preservation

Terms describing information must preserve the distinction between:

* source
* authority
* observation
* Context
* Evidence
* canonical representation

7. Lifecycle precision

Lifecycle terms must not be used as substitutes for semantic properties.

For example:

Trusted ≠ Completed
Validated ≠ Trusted
Executing ≠ Successful

⸻

27. Canonical Vocabulary Hierarchy

The primary Noema vocabulary can be organized as:

ONTOLOGY
│
├── Concepts
│
├── Entities
│   ├── Actors
│   └── Resources
│
├── Intents
│
├── Actions
│
├── Capabilities
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

This should not be interpreted as a strict inheritance hierarchy.

In particular:

Actor
Resource

are contextual roles that an Entity may occupy.

The operational relationship is:

Actor
  ↓
Intent
  ↓
Intent Resolution
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

28. Canonical Principles

The Glossary establishes the following vocabulary principles.

1. Intent describes what is wanted.
2. Objective describes the desired result of an Intent.
3. Action describes what is done.
4. Entity describes the identifiable thing involved.
5. Actor describes an Entity participating as an initiator or applicable participant.
6. Resource describes an Entity occupying an actionable role.
7. Capability describes what can be done.
8. Authority describes who or what may cause an Action or access an Entity within scope.
9. Context describes the bounded information relevant to the situation.
10. Constraint describes what limits the permissible solution or execution space.
11. Policy describes governing rules.
12. Evidence describes what supports or contradicts a proposition or decision.
13. State describes a condition at a point in time.
14. Provenance describes where information came from and how it was derived or used.
15. Trust describes Noema’s determination to permit progression across a decision boundary.
16. Execution describes an attempted or actual operation.
17. Execution Result describes the immediate technical result.
18. Outcome describes the semantically relevant observed result.
19. Expected Outcome and Observed Outcome must remain distinct.
20. Model Output is a proposal or inference, not automatically canonical truth.
21. Model Confidence is not Trust.
22. Capability is not Authority.
23. Entity Resolution is not Authorization.
24. Context is not automatically canonical enterprise state.
25. Policy and the Constraints derived from Policy remain distinct.
26. Unknown information must remain unknown until established.
27. Ambiguity must remain explicit until resolved.
28. Constraint conflicts must remain explicit until resolved according to applicable authority and policy.
29. Material Constraint relaxation or override must be explicit.
30. Material Entity resolution must be sufficiently established before consequential execution.
31. Context completeness and freshness are Action-specific.
32. Historical Context must remain distinguishable from current Context.
33. Execution success must not be inferred solely from a technical response when business verification is required.
34. Canonical representation does not automatically imply enterprise ownership or System-of-Record authority.
35. Noema must preserve semantic boundaries even when implementation mechanisms differ.

⸻

29. Canonical Semantic Chain

The core Noema execution model can be represented as:

USER / ACTOR
      │
      │ expresses
      ▼
    INTENT
      │
      ├───────────────► OBJECTIVE
      │
      ├───────────────► ENTITY / TARGET
      │
      ├───────────────► CONSTRAINTS
      │
      └───────────────► CONTEXT
                             │
                             ▼
                     RESOLUTION / VALIDATION
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
            EVIDENCE     AUTHORITY     POLICY
                │            │            │
                └────────────┼────────────┘
                             ▼
                        CONSTRAINTS
                             │
                             ▼
                           TRUST
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          CLARIFY         ESCALATE        REJECT
                                             │
                                             │
                                      if permitted
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
                                   EXECUTION RESULT
                                             │
                                             ▼
                                    FRESH CONTEXT
                                             │
                                             ▼
                                  OUTCOME VERIFICATION
                                             │
                                             ▼
                                          OUTCOME

This chain establishes the fundamental semantic separation between:

what is wanted
       ↓
what it concerns
       ↓
what information establishes the situation
       ↓
what limits the solution
       ↓
who is permitted
       ↓
whether Noema permits progression
       ↓
what operation is performed
       ↓
what capability performs it
       ↓
what actually happened

⸻

30. Canonical Vocabulary Authority

The Glossary is the cross-Canon vocabulary authority.

The detailed ontology documents remain the semantic authorities for their respective concepts.

Therefore:

Glossary
   │
   ├── establishes canonical terminology
   │
   └── references detailed semantic definitions
             │
             ├── intent.md
             ├── entities.md
             ├── actor.md
             ├── action.md
             ├── capability.md
             ├── context.md
             ├── constraint.md
             ├── policy.md
             ├── authority.md
             ├── state.md
             ├── outcome.md
             └── provenance.md

If a detailed ontology document introduces a term that materially changes the meaning of an existing canonical term, the conflict must be resolved explicitly rather than allowing both meanings to coexist silently.

If a later document introduces a new foundational term, it should:

1. define the term in its owning canonical document;
2. establish its relationship to existing concepts;
3. add the term to this Glossary where it is cross-Canon vocabulary;
4. preserve existing distinctions unless an explicit Canon change supersedes them.

⸻

31. Canonical Summary

The Noema Glossary exists to enforce one fundamental semantic discipline:

Noema must distinguish what the Actor wants, what that Intent concerns, what information establishes the situation, what constraints bound the permissible solution, who or what has Authority, what Capability exists, whether Noema permits progression, what Action is performed, what Execution actually occurred, and what Outcome resulted.

The canonical semantic chain is:

ACTOR
  │
  │ expresses
  ▼
INTENT
  │
  ├──────────────► OBJECTIVE
  │
  ├──────────────► ENTITY / TARGET
  │
  ├──────────────► CONTEXT
  │
  └──────────────► CONSTRAINTS
                         │
                         ├──────► POLICY
                         │
                         └──────► AUTHORITY
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

The Model participates primarily by proposing and interpreting:

MODEL
  │
  │ proposes
  ▼
NOEMA
  │
  ├── resolves
  ├── grounds
  ├── establishes Context
  ├── resolves Entities
  ├── validates
  ├── evaluates Constraints
  ├── evaluates Authority
  ├── evaluates Trust
  └── controls progression
              │
              ▼
          EXECUTION

The Model is therefore a semantic and probabilistic component within Noema, not the final authority over canonical state, Authority, Trust, or consequential execution.

The central Noema vocabulary distinction is:

WHAT IS WANTED
      ↓
INTENT
WHAT IT CONCERNS
      ↓
ENTITY / TARGET
WHAT MATTERS ABOUT THE SITUATION
      ↓
CONTEXT
WHAT LIMITS WHAT MAY BE DONE
      ↓
CONSTRAINT
WHAT GOVERNS THE RULE
      ↓
POLICY
WHO MAY ACT
      ↓
AUTHORITY
WHAT CAN BE DONE
      ↓
CAPABILITY
WHETHER NOEMA MAY PROCEED
      ↓
TRUST
WHAT IS DONE
      ↓
ACTION / EXECUTION
WHAT ACTUALLY RESULTED
      ↓
OUTCOME

And the foundational rule of the Glossary is:

Noema must preserve semantic distinctions that affect interpretation, authority, constraints, Trust, execution, or auditability.

The Glossary should therefore be treated as the shared vocabulary authority for the rest of the Canon, while the corresponding ontology documents remain the authoritative sources for the detailed semantics of each foundational concept.