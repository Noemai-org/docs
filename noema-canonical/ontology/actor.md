Actor

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/actor.md

⸻

1. Definition

An Actor is an entity that can express Intent, possess or exercise Authority, or participate in the execution of an Action within the Noema system.

An Actor is the canonical representation of who or what is participating in an Intent or Action.

An Actor may be:

* a human
* an organization
* a service
* an automated agent
* another system
* a delegated representative acting on behalf of another Actor

Therefore:

An Actor is an entity capable of participating in the intent-to-action lifecycle.

⸻

2. Actor Is Not Identity

Identity establishes who an entity is.

Actor establishes who or what is participating in a Noema interaction.

These concepts are related but distinct.

For example:

Identity
    │
    ▼
Actor
    │
    ├── expresses Intent
    ├── receives Authority
    └── causes Actions

An identity may authenticate an entity, but authentication alone does not establish what that entity is permitted to do.

Therefore:

Identity establishes recognition; Actor establishes participation.

The identity model is defined separately from the ontology of Actor.

⸻

3. Actor Is Not Authority

An Actor may possess Authority, but Actor and Authority are not the same concept.

Actor
  │
  │ may possess
  ▼
Authority
  │
  │ permits
  ▼
Action

For example:

Actor:
Customer Support Agent
Authority:
May request replacement cards for customers.
Action:
RequestCardReplacement

Authority is contextual and policy-dependent.

An Actor’s existence never implies permission to perform every Action available to that Actor.

⸻

4. Actor Is Not Intent

An Actor expresses or causes an Intent.

The Intent represents the objective.

The Actor represents the participant.

Actor
   │
   │ expresses
   ▼
Intent

For example:

Actor:
Customer
Intent:
"Renew my expired card."

The Actor and Intent must therefore remain separate concepts.

⸻

5. Actor Is Not User

A human user is one possible type of Actor.

However, Noema must not define Actor as synonymous with User.

Consider:

Human User
    │
    └── Actor
Service
    │
    └── Actor
Automated Agent
    │
    └── Actor
Organization
    │
    └── Actor

This distinction allows Noema to support interactions that are not directly initiated by a human at the moment of execution.

⸻

6. Actor Types

At the ontology level, Noema recognizes several broad categories of Actor.

6.1 Human Actor

A human individual participating directly in the system.

Examples:

Customer
Employee
Administrator
Support Agent
Manager

⸻

6.2 Organizational Actor

An organization or organizational unit acting as a participant.

Examples:

Company
Department
Team
Business Unit

An organizational Actor may express or possess Authority without representing a single individual.

⸻

6.3 System Actor

A software system participating in an Intent or Action lifecycle.

Examples:

CRM
Payment Processor
Identity Provider
Banking System
Notification Service

A system Actor may execute or provide capabilities without being the originator of the underlying human Intent.

⸻

6.4 Agent Actor

An automated agent operating within explicitly defined authority.

An Agent Actor may:

* interpret Intent
* propose Actions
* execute permitted Actions
* monitor execution
* request clarification
* escalate to humans

However:

Agent status does not imply unrestricted authority.

An agent operates within the Authority and Capability boundaries granted to it.

⸻

6.5 Delegated Actor

A Delegated Actor acts on behalf of another Actor.

For example:

Principal:
Customer
Delegated Actor:
Customer Support Agent
Intent:
"Replace the customer's damaged card."

Delegation must preserve the distinction between:

* the Actor performing the operation
* the Actor on whose behalf it is performed
* the Authority that permits the delegation

⸻

7. Principal and Delegate

Where delegation exists, Noema should distinguish between:

Principal

The Actor whose interests, authority, or objective are being represented.

Delegate

The Actor performing an operation on behalf of the Principal.

Conceptually:

Principal
    │
    │ delegates
    ▼
Delegate
    │
    │ performs
    ▼
Action

For example:

Principal:
Customer
Delegate:
Support Agent
Action:
RequestCardReplacement

The existence of delegation must not cause Noema to treat the Delegate as the Principal.

⸻

8. Actor Relationships

An Actor may have relationships with other Actors.

Examples include:

Customer
   │
   │ employs / belongs to
   ▼
Organization
Manager
   │
   │ manages
   ▼
Employee
Agent
   │
   │ acts on behalf of
   ▼
Customer
Service
   │
   │ operates for
   ▼
Organization

Relationships may influence Context and Authority.

However, a relationship alone must not automatically grant permission.

⸻

9. Actor and Context

Actor identity is one component of Intent Context.

For example:

Intent:
"Cancel the subscription."
Actor:
Customer #123
Context:
- Customer owns subscription
- Subscription is active
- Cancellation policy applies
- Current date is within allowed cancellation period

Actor information may therefore affect:

* interpretation
* available capabilities
* applicable policies
* authorization
* risk
* execution

But Actor information must not be treated as unrestricted permission.

⸻

10. Actor and Intent

An Intent may have multiple Actor roles.

For example:

Intent:
"Renew my card."
Actors:
Initiator:
Customer
Beneficiary:
Customer
Executor:
Banking System
Approver:
Customer Support Manager

Therefore, “Actor” does not necessarily mean the entity that typed the original request.

Noema should be able to distinguish different participation roles where the workflow requires them.

⸻

11. Actor Roles

An Actor may occupy different roles within the lifecycle of an Intent or Action.

Possible roles include:

Initiator

The Actor that originates an Intent.

Principal

The Actor whose objective or authority is represented.

Delegate

An Actor acting on behalf of another Actor.

Beneficiary

The Actor intended to receive the benefit or result.

Approver

An Actor whose approval is required before execution.

Executor

The Actor or system that performs an Action.

Observer

An Actor permitted to observe relevant state without being authorized to modify it.

These roles describe participation, not Actor identity.

The same Actor may occupy multiple roles in a workflow.

⸻

12. Actor and Authority

Authority determines what an Actor may cause.

Conceptually:

Actor
  +
Context
  +
Policy
  +
Delegation
  ↓
Effective Authority

Effective Authority may depend on:

* actor identity
* actor type
* organizational membership
* role
* resource ownership
* delegation
* policy
* temporal conditions
* geographic or organizational boundaries
* risk level
* required approvals

Noema must evaluate Authority explicitly when it materially affects execution.

⸻

13. Authority Must Be Scoped

Authority should never be interpreted as an unrestricted capability.

An Actor may have authority to perform one Action but not another.

For example:

Actor:
Support Agent
May:
✓ View customer profile
✓ Request card replacement
May not:
✗ Transfer funds
✗ Delete customer account
✗ Modify account ownership

Authority should therefore be understood as scoped permission rather than a general property of an Actor.

⸻

14. Actor and Capability

Actor and Capability answer different questions.

Actor:
Who is participating?
Capability:
What can the system do?

An Actor may be authorized to invoke a Capability.

But the Capability itself belongs to the system or execution environment that exposes it.

Therefore:

Actor
   │
   │ authorized to invoke
   ▼
Capability
   │
   │ performs
   ▼
Action

Capability availability and Actor authority must remain independently evaluable.

⸻

15. Actor and Authentication

Authentication establishes that an entity has successfully presented credentials or another recognized proof of identity.

Authentication does not establish:

* intent
* authority
* capability
* trust
* policy compliance

Conceptually:

Authentication
      ↓
Identity Established
      ↓
Actor Identified
      ↓
Authority Evaluated
      ↓
Action May Be Considered

Noema must not treat successful authentication as automatic authorization.

⸻

16. Actor and Authorization

Authorization answers whether an Actor is permitted to cause a particular Action under particular conditions.

Therefore authorization must consider more than Actor identity.

A useful conceptual model is:

Authorization =
Actor
+
Action
+
Target
+
Context
+
Policy
+
Authority

The same Actor may be authorized to perform an Action against one target but not another.

Likewise, authorization may change based on context.

⸻

17. Actor and Delegation

Delegation allows one Actor to permit another Actor to act on its behalf.

A delegation relationship should establish:

* principal
* delegate
* delegated authority
* permitted Actions
* scope
* duration
* conditions
* revocation state

Conceptually:

Principal
   │
   │ grants
   ▼
Delegation
   │
   ├── scope
   ├── actions
   ├── conditions
   └── duration
   │
   ▼
Delegate

Delegation must be explicit when it materially affects authorization.

⸻

18. Actor and Agentic Systems

An AI Agent may be an Actor when it participates in the execution lifecycle.

However, an Agent Actor must not derive authority merely from its ability to reason or act.

For example:

Agent
   │
   ├── may interpret Intent
   ├── may propose Actions
   ├── may execute permitted Actions
   └── may request clarification

The Agent remains constrained by:

Authority
Capability
Policy
Action Contract
Trust Boundary

Intelligence does not create authority.

⸻

19. Actor and Noema

Noema itself may participate in a workflow, but the platform must distinguish between:

* Noema as infrastructure
* an automated component operating within Noema
* an external system
* the human or organization whose Intent is being executed

Noema must not attribute an external Actor’s Intent to itself merely because Noema orchestrates the resulting Action.

For example:

Customer
   │
   │ Intent
   ▼
Noema
   │
   │ orchestrates
   ▼
Banking System

Noema is the intermediary and execution coordinator.

It does not become the owner of the customer’s Intent.

⸻

20. Actor and Business State

Actors may be represented in business systems.

For example:

Customer
Employee
Account Owner
Administrator

The authoritative representation of those entities remains in the appropriate system of record.

Noema may maintain the information required for Intent resolution and execution, but should avoid creating an unnecessary competing source of truth.

⸻

21. Actor Lifecycle

An Actor may have lifecycle states depending on the domain.

At the Noema ontology level, relevant conditions may include:

IDENTIFIED
ACTIVE
SUSPENDED
REVOKED
DELEGATED
EXPIRED
UNKNOWN

These states are contextual.

An Actor’s lifecycle in a particular enterprise system may differ from its participation state within a Noema interaction.

Noema should not assume that an Actor’s global business status and Noema participation status are identical.

⸻

22. Actor Provenance

Noema should be able to establish where its knowledge of an Actor came from.

Relevant provenance may include:

Identity Provider
Enterprise Directory
Application Session
Delegation Record
Authorization System
User Input
External System

Actor information that materially affects execution should be traceable to an appropriate source.

⸻

23. Multiple Actors

An Intent may involve multiple Actors.

For example:

Intent:
"Approve the customer's card renewal."
Actors:
Customer
Support Agent
Manager
Banking System
Noema

Each Actor may have a different role.

Noema must preserve those distinctions rather than reducing the workflow to a single “user”.

⸻

24. Actor and Outcome

An Outcome may affect one or more Actors.

For example:

Action:
Renew Card
Executor:
Banking System
Principal:
Customer
Beneficiary:
Customer
Outcome:
Replacement card requested

The Actor that executes an Action is therefore not necessarily the Actor who benefits from the resulting Outcome.

⸻

25. Canonical Actor Model

At the conceptual level:

Actor
├── identity
├── type
├── roles
├── relationships
├── authority
├── delegations
├── organizational context
├── provenance
└── participation

Participation may include:

Actor
├── initiator
├── principal
├── delegate
├── beneficiary
├── approver
├── executor
└── observer

These are conceptual properties and relationships, not an implementation schema.

⸻

26. Canonical Distinctions

Noema must preserve the following distinctions:

Identity
"Who is this entity?"
Actor
"Who or what is participating?"
Role
"How is the Actor participating?"
Authority
"What is this Actor permitted to cause?"
Capability
"What can the system perform?"
Delegation
"Who is acting on whose behalf?"
Intent
"What does the Actor want to accomplish?"
Action
"What operation can advance that Intent?"
Outcome
"What actually happened?"

These concepts are related but must not be collapsed.

⸻

27. Core Invariants

Invariant 1

An Actor is a participant in the intent-to-action lifecycle, not merely a user account.

Invariant 2

Identity does not imply Authority.

Invariant 3

Actor does not imply Permission.

Invariant 4

Capability does not imply Authority.

Invariant 5

An Agent does not receive authority merely because it can reason or act.

Invariant 6

Delegation must preserve the distinction between Principal and Delegate.

Invariant 7

Actor roles describe participation and must not be confused with Actor identity.

Invariant 8

The same Actor may occupy multiple roles within an Intent or workflow.

Invariant 9

An Action may have multiple Actors associated with it.

Invariant 10

The Actor executing an Action is not necessarily the Actor whose Intent initiated it.

Invariant 11

Actor information that materially affects authorization or execution must have appropriate provenance.

Invariant 12

Noema must not become the authoritative owner of an Actor’s business identity merely because it orchestrates Actions involving that Actor.

Invariant 13

Authority must be evaluated in context when it materially affects execution.

Invariant 14

Intelligence does not create authority.

⸻

28. Relationship to Other Canonical Domains

This document defines the ontology of Actor.

Related definitions live in:

01-ontology/
├── intent.md
├── action.md
├── context.md
├── capability.md
├── policy.md
├── constraint.md
├── state.md
└── outcome.md

Identity and authentication semantics belong to the relevant enterprise and security specifications.

Authority and authorization semantics belong primarily in:

03-trust/
06-enterprise/

Delegation and execution semantics belong in:

04-execution/
11-contracts/

⸻

29. Canonical Summary

An Actor is an entity that participates in Noema’s intent-to-action lifecycle by expressing Intent, possessing or exercising Authority, receiving Outcomes, or performing Actions.

An Actor may be human, organizational, system-based, or agentic.

The Actor model exists to preserve the distinction between who participates, who is represented, who is authorized, who acts, and who benefits.

ACTOR
  │
  ├── expresses ────────► INTENT
  │
  ├── possesses ────────► AUTHORITY
  │
  ├── invokes ──────────► CAPABILITY
  │
  ├── performs ─────────► ACTION
  │
  └── receives ─────────► OUTCOME