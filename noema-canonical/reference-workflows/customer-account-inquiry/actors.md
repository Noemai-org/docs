Actors

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/actors.md

⸻

1. Definition

An Actor is a Principal, system, service, or human participant that performs, authorizes, provides, receives, or influences an operation within the Customer Account Inquiry workflow.

Actors are distinct from:

Intent
Action
Resource
System of Record
Role
Permission

An Actor participates in the workflow.

An Action describes what is performed.

A Permission determines what an Actor is authorized to do.

⸻

2. Purpose

The purpose of the Actor model is to establish:

who initiates the workflow
who is represented by the Intent
which systems provide information
which systems execute Actions
who authorizes access
who may intervene
who receives the Outcome

The Actor model also establishes clear boundaries between the Customer, Noema, enterprise systems, and human operators.

⸻

3. Actor Model

The reference workflow can be represented as:

Customer
    │
    ▼
  Noema
    │
    ├── Identity System
    ├── Account System
    ├── Transaction System
    ├── Statement System
    └── Support System
              │
              ▼
       Human Support Agent

Not every execution involves every Actor.

The participating Actors depend on the Intent and resulting Action.

⸻

4. Primary Actors

The primary Actors are:

Customer
Noema
Enterprise Systems

Supporting Actors include:

Identity System
Account / Ledger System
Transaction System
Statement System
Support System
Human Support Agent

These Actors have different responsibilities and authority boundaries.

⸻

5. Customer

The Customer is the Principal initiating the Intent.

Examples:

"What's my balance?"
"Show my statement."
"Find my transaction from yesterday."
"How much did I spend last month?"
"I don't recognize this transaction."

The Customer provides the initial natural-language request.

The Customer’s request does not by itself establish:

identity
authorization
resource
intent certainty
enterprise state

These must be established through the Noema workflow.

⸻

6. Principal

The Principal is the identity on whose behalf the workflow is being performed.

In the simplest case:

Customer = Principal

However, the two concepts are not inherently identical.

A workflow may involve:

Customer
    ↓
acting as
    ↓
Principal

or a Customer may act under an authorized delegation.

Noema must preserve the distinction between the person interacting with the system and the identity represented by the request.

⸻

7. Noema

Noema is the Intent-to-Execution system coordinating the workflow.

Noema is responsible for:

Intent interpretation
Intent resolution
Context assembly
Ambiguity handling
Trust evaluation
Policy evaluation
Authorization evaluation
Action selection
Execution coordination
Outcome verification
Execution state
Auditability

Noema does not own the enterprise Business State accessed through the workflow.

⸻

8. Noema’s Authority Boundary

Noema has authority over its own execution domain.

This includes:

Intent State
Trust State
Action State
Execution State
Intervention State
Outcome State

Noema does not thereby gain authority over:

Account State
Balance
Transaction State
Statement State
Customer Record
Support Case State

Those remain owned by the appropriate enterprise systems.

⸻

9. Enterprise Systems

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

Ledger
    → balance
Transaction System
    → transactions
Statement System
    → statements
Support System
    → complaints / cases

Noema must preserve these boundaries.

⸻

10. Identity System

The Identity System establishes or provides information about the Principal.

It may provide:

principal_id
customer_id
identity status
authentication status
identity attributes
account relationships

Noema may consume this information as Context.

The Identity System remains authoritative for the identity information within its defined domain.

⸻

11. Account System

The Account System provides account-related information.

Examples:

account_id
account status
account ownership
account relationships
account metadata

The Account System may also be the System of Record for specific account attributes.

The exact authority boundary must be explicitly defined by the enterprise.

⸻

12. Ledger

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
Ledger
    ↓
Canonical Balance
    ↓
Noema
    ↓
Customer

Noema does not create or redefine the balance.

⸻

13. Transaction System

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
search_transactions
   ↓
Transaction System
   ↓
Transaction Results

Noema validates that returned transactions satisfy the requested scope.

⸻

14. Statement System

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

Noema does not become the authoritative owner of the statement.

⸻

15. Support System

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

⸻

16. Human Support Agent

A Human Support Agent may participate when automated execution cannot safely continue.

Examples:

identity ambiguity
data conflict
unsupported complaint
policy exception
enterprise inconsistency

The Human Support Agent may:

review evidence
provide clarification
make an authorized decision
resolve an exception
continue a workflow

Human intervention must remain bounded by organizational authority and Policy.

⸻

17. Human Intervention Boundary

A Human Support Agent does not automatically gain unrestricted authority by entering the workflow.

Human actions remain subject to:

identity
role
permissions
organizational boundaries
policy
audit requirements

A human decision should be recorded as part of the execution journey.

⸻

18. Actor vs Role

An Actor is a participant.

A Role defines a set of responsibilities or permissions associated with an Actor.

For example:

Actor:
Support Agent A
Role:
Customer Support Agent
Permissions:
view customer account
create complaint
view transaction details

The Role does not itself become the Actor.

⸻

19. Actor vs Permission

Actors and Permissions must remain distinct.

For example:

Customer A
    │
    └── Permission:
        view Account A transactions

The Customer is the Actor.

The permission determines whether the requested Action is authorized.

Being an Actor does not imply unrestricted access.

⸻

20. Actor vs Resource

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

⸻

21. Actor vs Principal

The Actor is the participant in the workflow.

The Principal is the identity represented in the authorization decision.

Often:

Actor = Principal

But this cannot be assumed universally.

For delegated access:

Actor
    ↓
acts_for
    ↓
Principal

Noema must preserve this distinction when relevant.

⸻

22. Actor Identity

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

The model exists to establish accountability and authority.

⸻

23. Actor Types

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

The type of Actor affects how authority, authentication, authorization, and accountability are evaluated.

⸻

24. System Actors

Enterprise Systems are treated as Actors because they participate in execution.

A System Actor may:

provide data
execute an Action
return a result
emit an Event
confirm state
reject a request
report failure

System Actors must have defined integration contracts and authority boundaries.

⸻

25. Noema as an Orchestrating Actor

Noema is not merely another enterprise application.

Its role is to coordinate:

Intent
Context
Trust
Action
Execution
Outcome

It does not replace the authority of the enterprise systems involved.

Conceptually:

Customer
    ↓
Noema
    ├── requests data
    ├── evaluates Trust
    ├── invokes Actions
    └── verifies Outcomes
            ↓
    Enterprise Systems

⸻

26. Actor and Intent

The initiating Actor provides the source of the Intent.

Customer
    ↓
Natural Language
    ↓
Intent

The Intent should preserve the relationship to the initiating Principal.

For example:

Intent {
    principal = customer_123
    operation = transaction_search
}

This allows Noema to determine whose data is being requested.

⸻

27. Actor and Identity Resolution

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

⸻

28. Actor and Ambiguity

Actor ambiguity must remain explicit.

Example:

Two eligible customers:
John Smith
John Smith

or:

Customer
    ↓
Multiple organizational identities

Noema must not silently select an Actor when the ambiguity is consequential.

The workflow should transition to:

AMBIGUOUS
    ↓
CLARIFICATION

or another Policy-defined resolution path.

⸻

29. Actor and Authorization

Authorization evaluates whether an Actor or Principal may perform an Action against a Resource.

Conceptually:

Principal
    +
Action
    +
Resource
    +
Scope
    ↓
Authorization Decision

For example:

Customer A
    +
view_transactions
    +
Account A
    ↓
ALLOW

while:

Customer A
    +
view_transactions
    +
Account B
    ↓
DENY

where the enterprise Policy does not authorize access.

⸻

30. Actor and Organizational Boundaries

Actors may belong to different organizational scopes.

Examples:

Tenant
Organization
Business Unit
Legal Entity
Environment

An Actor’s authority must not cross these boundaries implicitly.

For example:

Customer A
    → Tenant A
Customer B
    → Tenant B

Shared identifiers do not imply shared authority.

⸻

31. Actor and Data Boundaries

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

Actor participation does not eliminate data minimization requirements.

⸻

32. Actor and Policy

Policies constrain what Actors may do.

Examples:

Customer
    → may retrieve own statements
Support Agent
    → may create complaints
Noema
    → may invoke approved enterprise Actions
Ledger
    → authoritative for balance

Policy defines these relationships.

Noema should not infer authority merely from an Actor’s existence.

⸻

33. Actor and Trust

Trust evaluates whether the workflow has sufficient grounds to proceed.

Actor-related Trust considerations may include:

identity confidence
authentication
authorization
delegation
organizational membership
resource ownership
policy
risk

Trust does not reduce to Actor identity alone.

Known Actor
    ≠
Authorized Action

⸻

34. Actor and Action

An Actor may initiate, authorize, invoke, or execute an Action.

For example:

Customer
    ↓ initiates
balance inquiry
Noema
    ↓ invokes
retrieve_balance
Ledger
    ↓ performs
balance retrieval

These are different relationships.

Noema should preserve them rather than treating every participant as the executor.

⸻

35. Actor and Action Ownership

The Actor initiating an Action does not necessarily own the Action’s underlying Resource.

For example:

Customer
    ↓ requests
retrieve_balance
    ↓ against
Account
    ↓ owned by / authoritative within
Enterprise

Noema must preserve enterprise ownership semantics.

⸻

36. Actor and Enterprise Authority

Enterprise Systems define authority over Business State.

For example:

Ledger
    → balance authority
Transaction System
    → transaction authority
Statement System
    → statement authority

Noema cannot override this authority merely because it orchestrates the workflow.

⸻

37. Actor and Evidence

Actor activity can generate Evidence.

Examples:

Customer
    → provided clarification
Identity System
    → authenticated Principal
Ledger
    → returned balance
Support Agent
    → approved exception

Evidence should preserve the Actor or System responsible for the observation or decision where relevant.

⸻

38. Actor and Provenance

Consequential interactions should preserve provenance.

Conceptually:

Provenance {
    actor
    action
    source
    timestamp
    authority
}

This allows Noema to answer:

Who provided this information?
Which system produced it?
Who authorized this decision?
Which Actor performed this Action?

⸻

39. Actor and Events

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

⸻

40. Actor and Human Clarification

A Customer may provide clarification:

Noema:
"Which account?"
Customer:
"My current account."

The Customer remains the originating Actor.

The clarification becomes additional information for Intent Resolution.

Noema must still validate the resulting Resource against enterprise identity and authorization data.

⸻

41. Actor and Complaint Logging

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

42. Actor and Read Operations

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
view
    ↓
own account data

does not imply:

Customer
    ↓
view
    ↓
any enterprise account

Read access remains scoped.

⸻

43. Actor and Future Financial Writes

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
policy approval

These requirements belong to future write workflows and should not be implicitly introduced into the Phase 1 reference workflow.

⸻

44. Actor Failure

Actors and systems may become unavailable.

Examples:

Identity System unavailable
Ledger unavailable
Transaction System unavailable
Statement System unavailable
Support System unavailable
Human Agent unavailable

Noema must not treat unavailable Actors as silently successful.

The workflow must transition according to the relevant failure and recovery Policy.

⸻

45. Actor Authentication

Authentication establishes that an Actor is who they claim to be.

Authentication is distinct from:

authorization
identity resolution
Trust

Conceptually:

Authentication
      ↓
Identity
      ↓
Authorization
      ↓
Trust

The exact sequence may vary by workflow, but the semantic distinctions must remain.

⸻

46. Actor Authorization

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

⸻

47. Actor Accountability

Consequential workflow events should be attributable.

Noema should be able to determine:

who initiated the Intent
which Principal was represented
which system provided the data
which system executed the Action
which human intervened
which Actor produced the Outcome

This supports auditability and incident investigation.

⸻

48. Actor Lifecycle

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

Actor lifecycle is distinct from Intent and Execution lifecycle.

⸻

49. Actor Model

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

50. Actor Relationships

The reference workflow contains relationships such as:

Customer
    ├── initiates → Intent
    ├── represents → Principal
    └── receives → Outcome
Noema
    ├── resolves → Intent
    ├── assembles → Context
    ├── evaluates → Trust
    ├── invokes → Action
    └── verifies → Outcome
Enterprise System
    ├── provides → Data
    ├── executes → Capability
    └── establishes → Business State
Human Support Agent
    ├── reviews → Execution
    ├── provides → Intervention
    └── resolves → Exception

⸻

51. Reference Actor Flow

The complete Actor interaction can be represented as:

                    CUSTOMER
                       │
                       │ Intent
                       ▼
                     NOEMA
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
      IDENTITY      ACCOUNT      TRANSACTION
       SYSTEM       SYSTEM         SYSTEM
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                    NOEMA
                       │
                       ├──────► STATEMENT SYSTEM
                       │
                       └──────► SUPPORT SYSTEM
                                      │
                                      ▼
                              HUMAN SUPPORT AGENT

The participating path depends on the requested operation.

⸻

52. Example: Balance Inquiry

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
Ledger
    ↓
Canonical Balance
    ↓
Noema
    ↓
Customer

Actors remain distinct from the data and Actions exchanged between them.

⸻

53. Example: Transaction Search

Customer
    ↓
"Find my transaction from yesterday."
    ↓
Noema
    ↓
Identity System
    ↓
Transaction System
    ↓
Transaction Results
    ↓
Noema
    ↓
Customer

If multiple accounts are eligible:

Transaction Search
        ↓
Ambiguity
        ↓
Customer Clarification

The workflow does not guess the intended account.

⸻

54. Example: Complaint Logging

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
create_complaint
    ↓
Support System
    ↓
Case Created
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

⸻

55. Actor Invariants

Invariant 1

Every consequential workflow participant must have an attributable identity appropriate to its Actor type.

Invariant 2

The Actor initiating an Intent must remain distinguishable from the Intent itself.

Invariant 3

Actor, Principal, Role, Permission, Resource, and Action are distinct concepts.

Invariant 4

An Actor’s participation does not imply unrestricted authorization.

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

⸻

56. Final Definition

Actors are the identifiable human, system, service, or organizational participants that initiate, authorize, provide, execute, review, or receive operations within the Customer Account Inquiry workflow.

The fundamental relationship is:

ACTOR
   │
   ▼
INTENT
   │
   ▼
NOEMA
   │
   ├── resolves
   ├── contextualizes
   ├── evaluates Trust
   └── invokes
          │
          ▼
   ENTERPRISE ACTOR
          │
          ▼
       RESULT
          │
          ▼
       NOEMA
          │
          ▼
       OUTCOME
          │
          ▼
        ACTOR

And the architectural rule is:

An Actor’s participation establishes who is involved in the workflow; it does not by itself establish what that Actor is authorized to access, what Action they may perform, or which Business State they control.