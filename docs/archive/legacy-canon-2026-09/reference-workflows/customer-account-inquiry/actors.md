> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

# Actors

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/actors.md

⸻

## 1. Definition

An Actor is a Principal, system, service, or human participant that performs, authorizes, provides, receives, reviews, or influences an operation within the Customer Account Inquiry workflow.

Actors are distinct from:

Intent
Action
Resource
System of Record
Role
Permission
Authority
Principal

An Actor participates in the workflow.

An Action describes what is performed.

A Permission describes what an Actor or Principal may be allowed to do.

Authority establishes the organizational or system boundary within which that permission is meaningful.

A Principal is the identity represented in an authorization decision.

⸻

## 2. Purpose

The purpose of the Actor model is to establish:

who initiates the workflow
who is represented by the Intent
which Principal is represented by the request
which systems provide information
which systems execute capabilities
who authorizes access
who may intervene
who receives the Outcome
which Actor is accountable for each consequential operation

The Actor model establishes explicit boundaries between:

Customer
Principal
Noema
Enterprise Systems
Human Operators
Resources
Authority
Permissions

Actor participation does not itself establish authorization.

⸻

## 3. Actor Model

The reference workflow can be represented as:

Customer
    │
    ▼
  Noema
    │
    ├── Identity System
    ├── Account System
    ├── Ledger
    ├── Transaction System
    ├── Statement System
    └── Support System
              │
              ▼
       Human Support Agent

Not every execution involves every Actor.

The participating Actors depend on the resolved Intent, Action, Resource, Policy, and execution path.

⸻

## 4. Primary Actors

The primary Actors are:

Customer
Noema
Enterprise Systems

Supporting Actors include:

Identity System
Account System
Ledger
Transaction System
Statement System
Support System
Human Support Agent

These Actors have different responsibilities, authority boundaries, and execution relationships.

⸻

## 5. Customer

The Customer is the human Actor initiating the Intent.

Examples:

"What's my balance?"
"Show my statement."
"Find my transaction from yesterday."
"How much did I spend last month?"
"I don't recognize this transaction."

The Customer provides the initial natural-language request.

The Customer's request does not by itself establish:

identity
authentication
authorization
resource
Intent certainty
enterprise state
ownership

These must be established through the Noema workflow and authoritative enterprise systems.

⸻

## 6. Principal

The Principal is the identity represented by the workflow for purposes of authorization and accountability.

In the simplest case:

Customer = Actor
Customer = Principal

However, these concepts are not inherently identical.

A workflow may involve:

Actor
    ↓
acts_for
    ↓
Principal

Examples include:

delegated access
authorized representatives
service-mediated requests
organizational identities

Noema must preserve the distinction between:

who is interacting with Noema

and:

whose authority, identity, or entitlement is represented by the request.

⸻

## 7. Actor vs Principal

An Actor is a participant in the workflow.

A Principal is the identity represented in an authorization decision.

Often:

Actor = Principal

But this must not be assumed.

For delegated access:

Actor A
    ↓ acts_for
Principal B
    ↓
Authorization

The authorization decision must bind to the correct Principal and Resource.

Actor identity alone does not establish permission.

⸻

## 8. Noema

Noema is the Intent-to-Execution system coordinating the workflow.

Noema is responsible for:

Intent interpretation
Intent resolution
Context assembly
ambiguity handling
Trust evaluation
Policy evaluation
authorization coordination
Action selection
execution coordination
Outcome verification
execution state
intervention state
auditability
provenance

Noema does not own the enterprise Business State accessed through the workflow.

Noema owns the state of its own execution.

⸻

## 9. Noema's Authority Boundary

Noema has authority over its own execution domain.

This includes:

Intent State
Trust State
Action State
Execution State
Intervention State
Outcome State
Provenance of its execution journey

Noema does not thereby gain authority over:

Account State
Balance
Transaction State
Statement State
Customer Record
Support Case State

Those remain authoritative within the appropriate enterprise systems.

The enterprise remains authoritative for Business State.

Noema remains authoritative for the execution state it owns.

⸻

## 10. Enterprise Systems

Enterprise Systems are Actors that provide authoritative data or capabilities required by the workflow.

Examples include:

Identity System
Account System
Ledger
Transaction System
Statement System
Support System

Each system has a defined authority boundary.

For example:

Identity System
    → identity authority

Account System
    → account relationship / account metadata authority

Ledger
    → financial balance / ledger-state authority

Transaction System
    → transaction authority

Statement System
    → statement authority

Support System
    → complaint / case authority

Noema must preserve these boundaries.

An enterprise system returning data does not automatically establish authority over every fact or interpretation associated with that data.

⸻

## 11. Identity System

The Identity System establishes or provides information about the Principal.

It may provide:

principal_id
customer_id
identity status
authentication status
identity attributes
account relationships
delegation relationships

Noema may consume this information as Context and Evidence.

The Identity System remains authoritative for identity information within its defined domain.

Authentication must remain distinct from authorization and Trust.

⸻

## 12. Account System

The Account System provides account-related information.

Examples:

account_id
account status
account ownership
account relationships
account metadata

The Account System may be the System of Record for specific account attributes.

The exact authority boundary must be explicitly defined by the enterprise.

Noema must not infer account ownership solely from a natural-language reference.

⸻

## 13. Ledger

The Ledger is authoritative for financial state where the enterprise defines it as the System of Record.

Examples:

account balance
ledger entries
financial state

For a balance inquiry:

Customer
    ↓
Noema
    ↓
Identity / Authorization
    ↓
Ledger
    ↓
Canonical Balance
    ↓
Noema
    ↓
Customer

Noema does not create, calculate, redefine, or substitute an inferred balance for canonical ledger state.

⸻

## 14. Transaction System

The Transaction System provides transaction information within its authority boundary.

Examples:

transaction_id
amount
currency
merchant
timestamp
transaction status
account relationship

For transaction search:

Intent
   ↓
Action
   ↓
Transaction System
   ↓
Transaction Results
   ↓
Verification

Noema validates that returned transactions satisfy the requested Resource and scope.

A transaction returned by the system must not be treated as evidence that the requesting Principal is authorized to access it unless authorization has independently established that relationship.

⸻

## 15. Statement System

The Statement System provides statements or statement-related resources.

Examples:

statement_id
account_id
statement period
statement document
statement status

For statement retrieval:

Intent
   ↓
retrieve_statement
   ↓
Statement System
   ↓
Statement
   ↓
Verification

Noema does not become the authoritative owner of the statement.

⸻

## 16. Support System

The Support System manages customer complaints and support cases.

Examples:

case_id
customer_id
transaction_id
case type
case status
case history

For complaint logging:

Customer
    ↓
Intent
    ↓
Noema
    ↓
create_complaint
    ↓
Support System
    ↓
Case

The Support System remains authoritative for the resulting support case.

Noema records the execution journey and resulting Outcome but does not become the System of Record for the case.

⸻

## 17. Human Support Agent

A Human Support Agent may participate when automated execution cannot safely continue.

Examples:

identity ambiguity
authorization ambiguity
data conflict
unsupported request
policy exception
enterprise inconsistency
unknown execution state

The Human Support Agent may:

review evidence
provide clarification
make an authorized decision
resolve an exception
continue a workflow
escalate a case

Human intervention must remain bounded by:

identity
role
permission
organizational authority
Policy
audit requirements

⸻

## 18. Human Intervention Boundary

A Human Support Agent does not automatically gain unrestricted authority by entering the workflow.

Human actions remain subject to:

identity
authentication
role
permissions
organizational boundaries
tenant boundaries
Policy
audit requirements

A human decision should be recorded as part of the execution journey.

Human intervention is itself an attributable workflow event.

⸻

## 19. Actor vs Role

An Actor is a participant.

A Role defines a set of responsibilities or permissions associated with an Actor.

Example:

Actor:
Support Agent A

Role:
Customer Support Agent

Permissions:
view authorized customer account
create complaint
view authorized transaction details

The Role does not itself become the Actor.

⸻

## 20. Actor vs Permission

Actors and Permissions must remain distinct.

Example:

Customer A
    │
    └── Permission:
        view Account A transactions

The Customer is the Actor.

The Permission determines whether the requested Action may be authorized.

Being an Actor does not imply unrestricted access.

⸻

## 21. Actor vs Resource

An Actor performs or requests operations against Resources.

Example:

Customer
    │
    └── requests
            ↓
         Account

Another example:

Customer
    │
    └── requests
            ↓
       Transaction

The Resource remains distinct from the Actor.

Authorization must bind the relevant Actor / Principal to the specific resolved Resource.

⸻

## 22. Actor Identity

Every consequential Actor interaction should be attributable to an identity appropriate to the workflow.

Conceptually:

Actor {
    actor_id
    actor_type
    principal_id
    organization_id
    tenant_id
    role
}

Not every field is required for every Actor.

The semantic purpose is:

accountability
authority resolution
authorization
auditability
provenance

⸻

## 23. Actor Types

The reference workflow may contain several Actor types:

HUMAN
    Customer
    Support Agent

SYSTEM
    Identity System
    Account System
    Ledger
    Transaction System
    Statement System
    Support System

ORCHESTRATOR
    Noema

The Actor type affects how:

authentication
authorization
authority
accountability
provenance

are evaluated.

⸻

## 24. System Actors

Enterprise Systems are treated as Actors because they participate in execution.

A System Actor may:

provide data
execute a capability
return a result
emit an Event
confirm state
reject a request
report failure

System Actors must have defined:

integration contracts
authority boundaries
identity
capability boundaries
provenance

A System Actor's participation does not give it authority outside its defined domain.

⸻

## 25. Noema as an Orchestrating Actor

Noema is not merely another enterprise application.

Its role is to coordinate:

Intent
Context
Evidence
Trust
Policy
Authorization
Action
Execution
Outcome
Verification

Conceptually:

Customer
    ↓
Noema
    ├── resolves Intent
    ├── assembles Context
    ├── evaluates Trust
    ├── evaluates Policy
    ├── invokes Actions
    └── verifies Outcomes
            ↓
    Enterprise Systems

Noema does not replace enterprise authority.

⸻

## 26. Actor and Intent

The initiating Actor provides the source of the Intent.

Customer
    ↓
Natural Language
    ↓
Intent

The Intent should preserve the relationship to the initiating Principal.

Example:

Intent {
    principal = customer_123
    operation = transaction_search
}

The Principal reference must subsequently be bound to the authorized Resource.

⸻

## 27. Actor and Identity Resolution

Natural language may identify an Actor indirectly.

Example:

"Show my transactions."

Noema must establish what:

"my"

refers to.

This may require:

authenticated identity
principal mapping
account relationships
organizational context
enterprise identity data

Identity resolution must be sufficiently grounded for the requested Action.

Identity resolution must not silently become authorization.

⸻

## 28. Actor and Ambiguity

Actor ambiguity must remain explicit.

Examples:

Two eligible customers:
John Smith
John Smith

or:

Customer
    ↓
Multiple organizational identities

or:

Principal
    ↓
Multiple eligible accounts

Noema must not silently select an Actor or Principal when the ambiguity is consequential.

The workflow should transition to:

AMBIGUOUS
    ↓
CLARIFY

or another Policy-defined resolution path.

Consequential probabilistic guessing is not an acceptable Actor-resolution mechanism.

⸻

## 29. Actor and Authorization

Authorization evaluates whether a Principal may perform a specific Action against a specific Resource within a specific Scope.

Conceptually:

Principal
    +
Action
    +
Resource
    +
Scope
    +
Policy
    ↓
Authorization Decision

Authorization must attach to the fully resolved business Resource.

For example:

Customer A
    +
search_transactions
    +
Account A
    ↓
ALLOW

while:

Customer A
    +
search_transactions
    +
Account B
    ↓
DENY

where Policy does not authorize access.

Technical capability access does not establish business authorization.

⸻

## 30. Target-Bound Authorization

Authorization must be bound to the resolved target.

The following is insufficient:

Customer A
    ↓
authorized to call search_transactions

The workflow must establish:

Customer A
    +
search_transactions
    +
Account A
    +
scope
    ↓
authorized

A technically authorized capability invoked against the wrong Resource is not an authorized operation.

This protects against confused-deputy failures.

The Action must therefore carry the resolved Resource and authorization context into the execution boundary.

⸻

## 31. Authorization Layers

Authorization may involve distinct layers.

### Technical Authorization

Can this Principal invoke the capability?

Example:

Customer A
    → may invoke transaction search

### Policy Authorization

Does the requested parameterization satisfy applicable Policy?

Example:

Customer A
    → may access authorized transaction history
    → within permitted scope

### Business Authorization

Given the fully resolved Principal, Action, Resource, Context, and current Business State, is this specific operation permitted?

This layer binds authorization to the actual enterprise situation.

The layers must not be collapsed into a single assumption that:

"the user is authenticated, therefore the action is authorized."

⸻

## 32. Actor and Organizational Boundaries

Actors may belong to different organizational scopes.

Examples:

Tenant
Organization
Business Unit
Legal Entity
Environment

An Actor's authority must not cross these boundaries implicitly.

For example:

Customer A
    → Tenant A

Customer B
    → Tenant B

Shared identifiers do not imply shared authority.

Cross-tenant or cross-account access must be explicitly authorized.

⸻

## 33. Actor and Data Boundaries

Actors should receive only the data necessary for their authorized purpose.

For example:

Customer
    ↓
requested transaction
    ↓
relevant transaction details

does not imply access to:

unrelated transactions
other customers
internal enterprise metadata
unrelated account information
credentials
secrets

Actor participation does not eliminate data minimization requirements.

⸻

## 34. Actor and Policy

Policies constrain what Actors may do.

Examples:

Customer
    → may retrieve authorized statements

Customer
    → may search authorized transactions

Support Agent
    → may create complaints within assigned authority

Noema
    → may invoke approved Actions

Ledger
    → authoritative for balance

Policy defines these relationships.

Noema should not infer authority merely from Actor existence, authentication, or natural-language request.

⸻

## 35. Actor and Trust

Trust evaluates whether the workflow has sufficient grounds to proceed.

Actor-related Trust considerations may include:

identity confidence
authentication
authorization
delegation
organizational membership
resource ownership
Policy
risk
freshness of evidence

Trust does not reduce to Actor identity alone.

Known Actor
    ≠
Authorized Action

Authenticated Actor
    ≠
Authorized Resource

Authorized Capability
    ≠
Authorized Business Outcome

⸻

## 36. Actor and Action

An Actor may:

initiate
authorize
invoke
execute
review
verify

an Action.

For example:

Customer
    ↓ initiates
balance inquiry

Noema
    ↓ invokes
get_account_balance

Ledger
    ↓ provides
canonical balance

These are different relationships.

Noema must preserve them rather than treating every participant as the executor.

⸻

## 37. Actor and Action Ownership

The Actor initiating an Action does not necessarily own the Action's underlying Resource.

For example:

Customer
    ↓ requests
get_account_balance
    ↓ against
Account
    ↓ authoritative within
Ledger / Enterprise

Noema must preserve enterprise ownership and authority semantics.

⸻

## 38. Actor and Enterprise Authority

Enterprise Systems define authority over Business State.

For example:

Identity System
    → identity authority

Account System
    → account relationship authority

Ledger
    → balance authority

Transaction System
    → transaction authority

Statement System
    → statement authority

Support System
    → case authority

Noema cannot override this authority merely because it orchestrates the workflow.

⸻

## 39. Actor and Evidence

Actor activity can generate Evidence.

Examples:

Customer
    → provided clarification

Identity System
    → authenticated Principal

Ledger
    → returned balance

Support Agent
    → approved authorized intervention

Evidence should preserve the Actor or System responsible for the observation or decision where relevant.

Evidence must not automatically be treated as authoritative merely because an Actor produced it.

Authority remains domain-specific.

⸻

## 40. Actor and Provenance

Consequential interactions should preserve provenance.

Conceptually:

Provenance {
    actor
    principal
    action
    resource
    source
    authority
    timestamp
}

This allows Noema to answer:

Who initiated this Intent?
Which Principal was represented?
Which Actor provided this information?
Which system produced the result?
Who authorized this decision?
Which system executed the capability?
Who intervened?
Which Actor or System produced the resulting evidence?

⸻

## 41. Actor and Events

Actors may produce or consume Events.

Examples:

Ledger
    ↓
balance.changed

Support System
    ↓
case.created

Noema
    ↓
execution.completed

Events should identify their producer where required.

Noema should not treat an Event producer as automatically authoritative for every fact contained in the Event.

Events are Evidence or Context unless their authority is explicitly established.

⸻

## 42. Actor and Human Clarification

A Customer may provide clarification:

Noema:
"Which account?"

Customer:
"My current account."

The Customer remains the originating Actor.

The clarification becomes additional Context for Intent Resolution.

Noema must still validate the resulting Resource against:

enterprise identity
account relationships
authorization
Policy

Customer clarification does not by itself establish canonical Resource ownership.

⸻

## 43. Actor and Complaint Logging

Complaint Logging introduces a second enterprise-side Actor:

Customer
    ↓
Noema
    ↓
Support System

A Human Support Agent may subsequently become involved:

Support System
    ↓
Human Support Agent

The transition from automated workflow to human support must be explicit and auditable.

⸻

## 44. Actor and Read Operations

The Phase 1 operations are:

balance inquiry
statement retrieval
transaction search
spending summary
complaint logging

Each requires an appropriate Actor relationship.

For example:

Customer
    ↓
requests
    ↓
authorized account data

does not imply:

Customer
    ↓
access
    ↓
any enterprise account

Read access remains scoped.

Read-only does not mean authorization-free.

⸻

## 45. Actor and Future Financial Writes

Future financial write operations introduce stronger Actor requirements.

For example:

Customer
    ↓
transfer money

may require:

strong identity
authorization
transaction limits
risk evaluation
confirmation
fresh state
Policy approval
idempotency
postcondition verification

These requirements belong to future write workflows and should not be implicitly introduced into the Phase 1 reference workflow.

⸻

## 46. Actor Failure

Actors and systems may become unavailable.

Examples:

Identity System unavailable
Ledger unavailable
Transaction System unavailable
Statement System unavailable
Support System unavailable
Human Agent unavailable

Noema must not treat unavailable Actors as silently successful.

The workflow must transition according to the relevant Failure and Recovery Policy.

Where required information prevents a safe decision:

UNKNOWN
or
ESCALATE

must remain distinguishable from successful execution.

⸻

## 47. Actor Authentication

Authentication establishes that an Actor is who they claim to be.

Authentication is distinct from:

identity resolution
authorization
Trust

Conceptually:

Authentication
      ↓
Identity
      ↓
Authority
      ↓
Authorization
      ↓
Trust / Policy
      ↓
Action

The exact operational sequence may vary by workflow, but the semantic distinctions must remain.

⸻

## 48. Actor Authorization

Authorization determines what an authenticated Actor or Principal is allowed to do.

For example:

Authenticated Customer
        ≠
Authorized to access every account

Authorization must be evaluated against:

Actor / Principal
Action
Resource
Scope
Policy
Authority

Authorization must be target-bound where the Action operates on a consequential Resource.

⸻

## 49. Actor Accountability

Consequential workflow events should be attributable.

Noema should be able to determine:

who initiated the Intent
which Principal was represented
which Actor authorized the operation
which system provided the data
which system executed the capability
which human intervened
which Actor produced the Evidence
which system established the Business State
which Outcome resulted

This supports:

auditability
incident investigation
replay analysis
policy analysis
accountability

⸻

## 50. Actor Lifecycle

Actors may enter and leave a workflow.

Conceptually:

AVAILABLE
    ↓
PARTICIPATING
    ↓
ACTIONING
    ↓
COMPLETED

or:

PARTICIPATING
    ↓
UNAVAILABLE
    ↓
RECOVERY / ESCALATION

Actor lifecycle is distinct from:

Intent lifecycle
Action lifecycle
Execution lifecycle
Outcome lifecycle

⸻

## 51. Actor Model

Conceptually:

Actor {
    actor_id
    actor_type
    principal
    organization
    tenant
    role
    authority_scope
}

This is a semantic model rather than a requirement for a literal database representation.

⸻

## 52. Actor Relationships

The reference workflow contains relationships such as:

Customer
    ├── initiates → Intent
    ├── represents → Principal
    └── receives → Outcome

Noema
    ├── resolves → Intent
    ├── assembles → Context
    ├── evaluates → Trust
    ├── evaluates → Policy
    ├── coordinates → Authorization
    ├── invokes → Action
    └── verifies → Outcome

Enterprise System
    ├── provides → Data
    ├── executes → Capability
    ├── establishes → Business State
    └── produces → Evidence / Events

Human Support Agent
    ├── reviews → Execution
    ├── provides → Intervention
    └── resolves → Exception

⸻

## 53. Reference Actor Flow

The complete Actor interaction can be represented as:

                    CUSTOMER
                       │
                       │ Intent
                       ▼
                     NOEMA
                       │
              Identity / Principal
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
      IDENTITY      ACCOUNT      TRANSACTION
       SYSTEM       SYSTEM         SYSTEM
          │            │            │
          └────────────┼────────────┘
                       │
                 Trust / Policy
                       │
                 Authorization
                       │
                       ▼
                    ACTION
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       LEDGER      STATEMENT     SUPPORT
                    SYSTEM       SYSTEM
          │            │            │
          └────────────┼────────────┘
                       │
                    RESULT
                       │
                       ▼
                     NOEMA
                       │
                 Verification
                       │
                       ▼
                    OUTCOME
                       │
                       ▼
                    CUSTOMER

If automation cannot safely continue:

                     NOEMA
                       │
                    ESCALATE
                       │
                       ▼
              HUMAN SUPPORT AGENT
                       │
                  INTERVENTION
                       │
                       ▼
                     NOEMA

The participating path depends on the resolved Intent and Policy.

⸻

## 54. Example: Balance Inquiry

Customer
    ↓
"What's my balance?"
    ↓
Noema
    ↓
Identity System
    ↓
Principal
    ↓
Account Resolution
    ↓
Authorization
    ↓
get_account_balance
    ↓
Ledger
    ↓
Canonical Balance
    ↓
Verification
    ↓
Noema
    ↓
Customer

Actors remain distinct from the data and Actions exchanged between them.

⸻

## 55. Example: Transaction Search

Customer
    ↓
"Find my transaction from yesterday."
    ↓
Noema
    ↓
Identity System
    ↓
Principal
    ↓
Account / Resource Resolution
    ↓
Trust / Policy
    ↓
Authorization
    ↓
search_transactions
    ↓
Transaction System
    ↓
Transaction Results
    ↓
Noema
    ↓
Verification
    ↓
Customer

If multiple consequential Resources remain eligible:

Transaction Search
        ↓
Ambiguity
        ↓
CLARIFY

The workflow does not guess the intended Resource.

If the Principal is not authorized for the candidate Resource:

Authorization
        ↓
REJECT

The workflow must not expose protected information merely to assist clarification.

⸻

## 56. Example: Complaint Logging

Customer
    ↓
"I don't recognize this transaction."
    ↓
Noema
    ↓
Identity / Transaction Context
    ↓
Trust
    ↓
Authorization
    ↓
create_complaint
    ↓
Support System
    ↓
Case Created
    ↓
Verification
    ↓
Customer

If human review is required:

Support System
    ↓
Human Support Agent
    ↓
Review / Intervention
    ↓
Updated Workflow State
    ↓
Noema

The Support System remains authoritative for the Case.

⸻

## 57. Actor and the Execution Boundary

Actors participate before, at, and after the execution boundary.

Before execution:

Customer
    ↓
Intent
    ↓
Noema
    ↓
Identity
    ↓
Context
    ↓
Trust
    ↓
Policy
    ↓
Authorization
    ↓
Action

At execution:

Action
    ↓
Enterprise Capability

After execution:

Enterprise Result
    ↓
Evidence
    ↓
Verification
    ↓
Outcome
    ↓
Customer / Human Agent

The model must not be treated as the authority that determines the final consequential operation after the Action has been established.

⸻

## 58. Actor and Fail-Closed Behavior

When an Actor or required enterprise system is unavailable, ambiguous, unauthorized, or unable to establish required state, Noema must not silently proceed.

The workflow must transition according to Policy:

REJECT
CLARIFY
ESCALATE
UNKNOWN

The absence of an error is not sufficient evidence of successful execution.

⸻

## 59. Actor Invariants

Invariant 1

Every consequential workflow participant must have an attributable identity appropriate to its Actor type.

Invariant 2

The Actor initiating an Intent must remain distinguishable from the Intent itself.

Invariant 3

Actor, Principal, Role, Permission, Resource, Authority, and Action are distinct concepts.

Invariant 4

An Actor's participation does not imply unrestricted authorization.

Invariant 5

Noema must not infer authorization merely from authenticated identity.

Invariant 6

Enterprise Systems remain authoritative for the Business State within their defined domains.

Invariant 7

Noema does not become the owner of enterprise Business State merely because it invokes an enterprise capability.

Invariant 8

System Actors must have explicit authority and integration boundaries.

Invariant 9

Human intervention must remain bounded by identity, role, permission, Policy, and organizational authority.

Invariant 10

Actor ambiguity must not be resolved through consequential probabilistic guessing.

Invariant 11

Actor identity must be sufficiently grounded for the risk level of the Action.

Invariant 12

Actor relationships must respect tenant, organizational, legal, and environment boundaries.

Invariant 13

Actor access must respect enterprise data boundaries and least-privilege requirements.

Invariant 14

Consequential Actor activity must be auditable.

Invariant 15

Actor provenance should be preserved where it affects Trust, authorization, execution, or auditability.

Invariant 16

An enterprise system returning data does not automatically establish authority over every fact it returns.

Invariant 17

Noema must preserve the distinction between who requested an Action and which system executed it.

Invariant 18

Customer clarification may provide additional Context but does not automatically establish canonical enterprise identity or Resource ownership.

Invariant 19

Read-only operations remain subject to Actor identity and authorization requirements.

Invariant 20

Future financial write operations require stronger Actor and Trust guarantees and must be defined separately from the Phase 1 reference workflow.

Invariant 21

Authorization must bind to the fully resolved Resource where the Action operates on a consequential Resource.

Invariant 22

Technical authorization to invoke a capability does not establish business authorization for a specific Resource or Outcome.

Invariant 23

Actor identity, Principal identity, authentication, authorization, Trust, and Policy must remain semantically distinguishable.

Invariant 24

Noema must not expose protected Resource information merely because Resource resolution is ambiguous or authorization has failed.

Invariant 25

Human intervention must itself be attributable and auditable.

Invariant 26

Enterprise Actor authority must remain bounded by the system's defined domain.

Invariant 27

Actor provenance must be preserved sufficiently to reconstruct consequential decisions and execution.

Invariant 28

Unavailable or uncertain Actors must not be treated as silently successful.

Invariant 29

Customer clarification does not override canonical enterprise identity, authorization, or Resource ownership.

Invariant 30

Actor participation does not transfer Business State authority from the enterprise System of Record to Noema.

Invariant 31

An Action must not execute against a Resource for which the represented Principal has not been authorized.

Invariant 32

Cross-account and cross-tenant access must never arise through implicit Actor resolution.

⸻

## 60. Final Definition

Actors are the identifiable human, system, service, or organizational participants that initiate, authorize, provide, execute, review, verify, or receive operations within the Customer Account Inquiry workflow.

The fundamental relationship is:

ACTOR
   │
   ▼
INTENT
   │
   ▼
PRINCIPAL
   │
   ▼
NOEMA
   │
   ├── resolves
   ├── contextualizes
   ├── evaluates Trust
   ├── evaluates Policy
   ├── coordinates Authorization
   └── invokes
          │
          ▼
       ACTION
          │
          ▼
   ENTERPRISE ACTOR
          │
          ▼
     BUSINESS STATE
          │
          ▼
       RESULT
          │
          ▼
       EVIDENCE
          │
          ▼
       VERIFICATION
          │
          ▼
       OUTCOME
          │
          ▼
        ACTOR

And the architectural rule is:

An Actor's participation establishes who is involved in the workflow; it does not by itself establish what that Actor is authorized to access, what Action they may perform, which Resource they may act against, or which Business State they control.

Authorization must bind the represented Principal, approved Action, resolved Resource, Scope, and applicable Policy.

Enterprise Systems remain authoritative for the Business State within their domains.

Noema remains authoritative for the execution state it owns and for the causal record of how the workflow reached its Outcome.