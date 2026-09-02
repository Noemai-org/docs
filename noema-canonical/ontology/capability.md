A Capability describes what a system is able to do. It does not mean that Noema is authorized to do it, nor that a particular Actor is permitted to invoke it.

Capability

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/capability.md

⸻

1. Definition

A Capability is a defined ability of a system, service, component, or execution environment to perform an operation.

A Capability answers:

What can this system do?

A Capability does not answer:

* Who may invoke it?
* Whether a particular Intent is trusted?
* Whether a particular Action should be performed?
* Whether execution will succeed?
* What business outcome will result?

Those concerns belong to other Noema concepts.

The fundamental relationship is:

Capability
    │
    │ enables
    ▼
Action
    │
    │ advances
    ▼
Intent

⸻

2. Capability Is Not Action

An Action represents an operation Noema intends to perform.

A Capability represents an ability available to perform that operation.

For example:

Action:
RequestCardRenewal
Capability:
banking.cards.renew

The distinction is:

Action
"What do we want to do?"
Capability
"What can this system do?"

An Action may require one or more Capabilities.

A Capability may support many different Actions depending on its interface and semantics.

⸻

3. Capability Is Not Authority

A system may possess a Capability without every Actor being authorized to invoke it.

For example:

Capability:
banking.accounts.transfer
Actor A:
Authorized
Actor B:
Not authorized

Both Actors may interact with the same system, but their Authority differs.

Therefore:

Capability establishes possibility; Authority establishes permission.

⸻

4. Capability Is Not Permission

Permission is a property of an authorization relationship.

Capability is a property of a system or execution environment.

System
  │
  └── has ───────► Capability
Actor
  │
  └── may have ──► Authority

Noema must evaluate both independently.

⸻

5. Capability Is Not Trust

The existence of a Capability does not make an Action trustworthy.

For example:

Capability:
banking.accounts.transfer
Intent:
"Transfer $10,000 to this account."

The system may technically support the operation.

That does not establish:

* that the Actor intended the transfer
* that the recipient is correct
* that the transfer is permitted
* that policy allows it
* that the requested amount is acceptable
* that Noema should execute it

Capability is therefore one input into trust and execution, not a substitute for them.

⸻

6. Capability Is Not Implementation

A Capability describes a system ability at the semantic level.

It should not be defined merely as:

POST /api/v1/cards/renew

That is an implementation interface.

The Capability is the semantic ability:

banking.cards.renew

The concrete API, RPC method, SDK call, function, or tool through which the Capability is exposed belongs to the integration and contract layers.

This distinction allows Noema to reason about capabilities independently of a specific implementation.

⸻

7. Capability Has an Owner

A Capability must have an identifiable source.

The source may be:

* an enterprise system
* a SaaS application
* a service
* a database-backed application
* an internal Noema component
* an external API
* a physical system exposed through software
* another execution environment

For example:

Owner:
Banking Platform
Capability:
banking.cards.renew

The owner is responsible for defining and maintaining the actual ability.

Noema may discover, register, consume, and orchestrate the Capability without becoming its owner.

⸻

8. Capability Has a Semantic Identity

A Capability should have a stable semantic identity independent of its transport mechanism.

For example:

banking.cards.renew
banking.cards.status.read
crm.customer.update
payments.transfer.create
notifications.email.send

The naming convention is not yet normative.

The important principle is:

A Capability must be addressable as a semantic operation rather than only as a transport-specific endpoint.

⸻

9. Capability Has an Interface

A Capability must expose enough information for Noema to understand how it may be invoked.

At a conceptual level:

Capability
├── identity
├── owner
├── description
├── inputs
├── outputs
├── target
├── preconditions
├── side effects
├── failure semantics
└── execution interface

The detailed executable representation belongs in 11-contracts/.

⸻

10. Capability Has Inputs

A Capability may require structured inputs.

For example:

Capability:
payments.transfer.create
Inputs:
- source_account
- destination_account
- amount
- currency

Inputs must have defined semantics.

Noema must not assume that arbitrary model-generated values are valid Capability inputs.

Input validation belongs at the boundary between Action and Capability execution.

⸻

11. Capability Has Outputs

A Capability may produce:

* data
* state changes
* identifiers
* events
* execution results
* errors
* status information

For example:

Capability:
banking.cards.status.read
Output:
CardStatus

Outputs should have defined semantics so that Noema can reason about the resulting state.

⸻

12. Capability Has Preconditions

A Capability may only be valid under particular conditions.

For example:

Capability:
banking.cards.renew
Preconditions:
- card exists
- card is eligible for renewal
- customer identity is verified

Capability-level Preconditions describe what must be true for the underlying system operation to be valid.

They may differ from Action-level Preconditions.

An Action may impose additional conditions based on the particular Intent.

⸻

13. Capability Has Side Effects

A Capability may be:

Read-only

It observes information without intentionally changing business state.

Examples:

GetCustomer
GetCardStatus
CheckEligibility

Mutating

It changes state.

Examples:

UpdateCustomer
RenewCard
CreatePayment
CancelSubscription

External-effecting

It causes effects beyond the system’s internal state.

Examples:

SendEmail
SendSMS
IssueRefund
CreateExternalPayment

The classification of side effects is important because it may affect Trust, authorization, risk, idempotency, and human approval.

⸻

14. Capability Has Risk Characteristics

Capabilities may have different risk profiles.

For example:

Low Risk:
Read customer profile
Medium Risk:
Update customer address
High Risk:
Transfer funds
Delete account
Issue refund

Risk is not itself the Capability.

It is a property that may influence the conditions under which the Capability may be invoked.

A Capability with significant side effects should generally have stronger execution controls than a read-only Capability.

⸻

15. Capability Has Authority Requirements

A Capability may define the type of authority required to invoke it.

For example:

Capability:
payments.refund.create
Required Authority:
payments.refund.initiate

The Capability defines the requirement.

The authorization system determines whether the current Actor satisfies that requirement.

Therefore:

Capability
     │
     └── requires ───► Authority
                         ▲
                         │
                       Actor

⸻

16. Capability May Be Composed

A complex Capability may internally depend on other Capabilities.

For example:

Capability:
card.renew
may internally require:
├── card.status.read
├── customer.verify
├── card.eligibility.check
└── card.replacement.create

However, the internal implementation of a Capability should not automatically expose all underlying operations as part of its public semantic contract.

Composition is an implementation and contract concern unless the underlying Capabilities are independently exposed.

⸻

17. Capability Discovery

Noema must have a way to determine what Capabilities are available.

Capability discovery may occur through:

* explicit registration
* configuration
* API schemas
* service metadata
* tool definitions
* capability registries
* integration manifests
* runtime discovery

The discovery mechanism is implementation-specific.

The canonical requirement is:

Noema must not assume a Capability exists merely because an Action would benefit from it.

Availability must be established.

⸻

18. Capability Registration

A Capability may be registered with Noema using a canonical representation.

Conceptually:

Capability Registration
identity
owner
description
inputs
outputs
target
preconditions
side effects
authority requirements
risk characteristics
execution interface
version
status

The registration model is defined outside the ontology.

This document defines what the Capability represents.

⸻

19. Capability Versioning

Capabilities may evolve.

A change may affect:

* inputs
* outputs
* semantics
* preconditions
* side effects
* authorization requirements
* execution behavior

A change that alters the meaning of a Capability must be treated as a semantic change, not merely a software deployment.

Therefore:

Capability identity and Capability implementation version must be distinguishable.

The versioning and compatibility rules belong in 11-contracts/versioning.md.

⸻

20. Capability Availability

A registered Capability is not necessarily available for execution at all times.

Possible states include:

REGISTERED
AVAILABLE
UNAVAILABLE
DEGRADED
DEPRECATED
REVOKED
UNKNOWN

Availability is runtime state.

Capability identity is semantic state.

Noema must distinguish between the two.

For example:

Capability exists
        +
Capability currently unavailable
        ↓
Action cannot currently execute

The existence of a Capability does not imply current availability.

⸻

21. Capability and Action Selection

When Noema resolves an Intent into an Action, it must determine whether an appropriate Capability exists.

Conceptually:

Intent
  ↓
Candidate Action
  ↓
Capability Discovery
  ↓
Available Capability?
  │
  ├── Yes → Continue
  │
  └── No  → Cannot execute

Noema should not invent a Capability to satisfy an Intent.

If no suitable Capability exists, Noema may:

* request clarification
* explain that the operation is unavailable
* propose an alternative
* escalate
* terminate the workflow

depending on the context and policy.

⸻

22. Capability and Trust

Capability is one of the inputs to Trust evaluation.

A conceptual Trust evaluation may include:

Resolved Intent
       +
Context
       +
Evidence
       +
Authority
       +
Capability
       +
Policy
       +
Constraints
       ↓
Trust Decision

A missing Capability may prevent execution.

A Capability does not guarantee Trust.

⸻

23. Capability and Bounded Autonomy

Capabilities define part of the boundary within which Noema can operate autonomously.

An autonomous system cannot safely operate beyond the Capabilities available to it.

Therefore:

Autonomy
   ⊆
Available Capabilities
   ∩
Granted Authority
   ∩
Applicable Policy
   ∩
Trusted Intent

This provides an important boundary against unrestricted agentic behavior.

Noema cannot autonomously perform an operation for which no explicit Capability exists.

⸻

24. Capability and External Systems

A Capability may be backed by an external system.

For example:

Noema
   │
   │ consumes
   ▼
Capability:
banking.cards.renew
   │
   │ backed by
   ▼
Banking API
   │
   ▼
Banking System

The external system remains responsible for executing the operation and maintaining authoritative business state.

Noema provides orchestration and intent-level coordination.

⸻

25. Capability and Business State

A Capability may read or mutate business state.

For example:

Capability:
crm.customer.update

The Capability may modify customer state.

However, the business system remains authoritative for that state.

Noema must distinguish:

Capability:
"What can be done?"
Business State:
"What is currently true?"

A Capability should not be treated as a source of truth simply because it can modify or retrieve that truth.

⸻

26. Capability and Agents

An AI Agent may discover or invoke Capabilities.

However, the Agent does not define the Capability merely by generating a tool call.

The canonical flow is:

Agent Proposal
      ↓
Noema
      ↓
Known Capability
      ↓
Validation
      ↓
Authority
      ↓
Action Contract
      ↓
Execution

An arbitrary model-generated tool definition is not automatically a trusted Noema Capability.

⸻

27. Capability Provenance

Noema should maintain provenance for the origin of a Capability.

Relevant provenance may include:

Capability Owner
Integration
Registration
Schema
Version
Discovery Source
Last Verification

This allows Noema to answer:

Where did this Capability come from, and why does Noema believe it exists?

⸻

28. Capability Failure

A Capability may fail independently of the Action that requested it.

For example:

Action:
RequestCardRenewal
Capability:
banking.cards.renew
Failure:
Banking API unavailable

The Action remains conceptually valid even though execution failed.

Therefore Noema must distinguish:

Invalid Action
       ≠
Valid Action + Capability Failure

This distinction is important for retry, recovery, diagnosis, and human intervention.

⸻

29. Capability and Outcomes

A Capability execution may produce one or more Outcomes.

For example:

Capability:
payments.transfer.create
Execution:
Successful
Observed Outcome:
Transfer created with transaction ID.

The Capability defines the operation.

The Outcome describes what happened.

Noema should not infer Outcome solely from the existence of the Capability invocation.

⸻

30. Capability Ontology

At the conceptual level:

Capability
├── identity
├── owner
├── semantic description
├── inputs
├── outputs
├── target
├── preconditions
├── authority requirements
├── side effects
├── risk characteristics
├── execution interface
├── availability
├── version
├── provenance
└── lifecycle state

This is an ontology-level representation.

It is intentionally not the final implementation schema.

The executable representation belongs in:

11-contracts/

⸻

31. Canonical Distinctions

Noema must preserve the following distinctions:

Capability
"What can this system do?"
Action
"What operation do we want to perform?"
Authority
"Who is permitted to cause it?"
Permission
"Does this Actor satisfy the applicable authorization rule?"
Contract
"Under what explicit terms can the operation execute?"
Availability
"Can the Capability currently be invoked?"
Execution
"What attempt was made?"
Outcome
"What actually happened?"

These concepts are related but must not be collapsed into a single abstraction.

⸻

32. Core Invariants

Invariant 1

A Capability represents an ability of a system or execution environment to perform an operation.

Invariant 2

Capability does not imply Authority.

Invariant 3

Capability does not imply Trust.

Invariant 4

Capability does not imply current Availability.

Invariant 5

A model-generated tool call does not automatically constitute a Noema Capability.

Invariant 6

Noema must not invent Capabilities to satisfy an Intent.

Invariant 7

An Action must map to an available Capability before execution can occur.

Invariant 8

Capability semantics must be distinguishable from its transport or implementation mechanism.

Invariant 9

Capabilities with side effects require explicit execution semantics.

Invariant 10

Capability ownership remains with the system that provides the underlying ability.

Invariant 11

Capability versions must be distinguishable when their semantics or execution behavior differ.

Invariant 12

Capability availability must be distinguishable from Capability existence.

Invariant 13

Capability failures must be distinguishable from invalid Actions.

Invariant 14

An Agent cannot acquire authority merely by discovering or invoking a Capability.

Invariant 15

Noema’s autonomous operating boundary cannot exceed the Capabilities explicitly available to it.

⸻

33. Relationship to Other Canonical Domains

This document defines the ontology of Capability.

Related definitions live in:

01-ontology/
├── actor.md
├── intent.md
├── action.md
├── context.md
├── policy.md
├── constraint.md
├── authority.md
├── outcome.md
└── state.md

Trust semantics involving Capabilities belong primarily in:

03-trust/

Capability execution semantics belong in:

04-execution/

Capability registration and executable schemas belong in:

11-contracts/

External system mappings belong in:

06-enterprise/

⸻

34. Canonical Summary

A Capability is an explicit, semantically defined ability of a system or execution environment to perform an operation. It establishes what can be done, but does not establish who may do it, whether it should be done, whether it is trusted, or what outcome will result.

The canonical relationship is:

ACTOR
  │
  │ may possess Authority
  ▼
AUTHORITY
  │
  │ permits
  ▼
ACTION
  │
  │ requires
  ▼
CAPABILITY
  │
  │ enables
  ▼
EXECUTION
  │
  │ produces
  ▼
OUTCOME

Capability is therefore one of the fundamental boundaries that prevents Noema’s probabilistic reasoning layer from becoming an unrestricted execution layer.co