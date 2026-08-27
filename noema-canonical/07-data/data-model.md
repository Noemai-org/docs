Data Model

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: 07-data/data-model.md

⸻

1. Definition

The Noema Data Model defines the semantic structure, relationships, provenance, authority, and lifecycle of information used to resolve Intent, evaluate Trust, and execute Actions.

The Data Model answers:

“What kinds of data does Noema operate on, how are they related, and what does each piece of data mean?”

It is not simply a database schema.

The Data Model is the semantic contract underlying Noema’s data layer.

⸻

2. Purpose

Noema operates across enterprise systems that each have their own:

* schemas
* identifiers
* APIs
* databases
* event models
* terminology
* state representations

Noema requires a common semantic model without requiring every enterprise system to adopt Noema’s internal storage model.

Enterprise Systems
       │
       ▼
Integration Layer
       │
       ▼
Noema Data Model
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
Intent Trust Execution

⸻

3. Core Principle

Noema’s Data Model represents meaning, not ownership.

Noema may represent:

Customer
Account
Payment
Employee
Order
Policy
Capability
Action

without becoming the System of Record for those entities.

The model provides a semantic representation that allows Noema to reason across heterogeneous enterprise systems.

⸻

4. Semantic Model vs Physical Schema

The Data Model should not be confused with a database schema.

Semantic Model
     ↓
defines meaning
Physical Schema
     ↓
defines storage

For example, Noema may define:

Payment.status

while one enterprise exposes:

payment_status

and another:

state

The Integration layer maps the enterprise representation into the semantic model.

⸻

5. Data Model Layers

The Noema Data Model can be understood as several related layers:

┌──────────────────────────────┐
│        Intent Data           │
├──────────────────────────────┤
│        Trust Data            │
├──────────────────────────────┤
│       Execution Data         │
├──────────────────────────────┤
│      Enterprise Data        │
├──────────────────────────────┤
│      Provenance Data         │
└──────────────────────────────┘

These layers should remain semantically distinguishable.

⸻

6. Core Data Categories

Noema operates on several fundamental categories.

Entity
Resource
State
Context
Evidence
Constraint
Policy
Action
Outcome
Identity
Relationship

These categories form the foundation of the Noema semantic model.

⸻

7. Entity

An Entity represents a distinct enterprise subject.

Examples:

Customer
Employee
Organization
Account
Vendor

An Entity has identity and relationships with other entities.

Entity
 ├── identity
 ├── attributes
 └── relationships

⸻

8. Resource

A Resource represents something that can be acted upon.

Examples:

Payment
Order
Account
Invoice
Subscription
Card

A Resource may be associated with an Entity.

Customer
   │
   └── owns → Account

⸻

9. Identity

Identity establishes what an Entity or Resource refers to.

Conceptually:

Identity {
    type
    identifier
    namespace
    source
    scope
}

Identity is critical because natural-language Intent frequently refers to Resources indirectly.

⸻

10. Attribute

An Attribute describes a property of an Entity or Resource.

Examples:

Account.balance
Payment.amount
Payment.currency
Order.status
Employee.department

Attributes may have:

value
type
source
authority
timestamp
version

⸻

11. State

State describes the condition of a Resource or Noema object at a particular point in time.

Examples:

Payment = SUCCEEDED
Account = ACTIVE
Execution = RUNNING
Intent = RESOLVED

State should be modeled explicitly rather than inferred from arbitrary fields whenever state semantics are consequential.

⸻

12. State Ownership

State belongs to an authority domain.

Enterprise:
Account.status
Noema:
Execution.status

Noema should not silently replace enterprise state with a local approximation.

⸻

13. Relationship

Relationships connect entities, resources, actions, systems, and other semantic objects.

Examples:

Customer ──owns──> Account
Account ──has──> Payment
Action ──operates_on──> Resource
Policy ──governs──> Action
System ──owns──> Capability

Relationships are first-class semantic information.

⸻

14. Context

Context is the bounded information relevant to a particular Intent or Execution.

Context
 ├── identity
 ├── entities
 ├── resources
 ├── states
 ├── policies
 ├── evidence
 └── system information

Context provides runtime grounding for the rest of the model.

⸻

15. Evidence

Evidence represents information supporting a proposition or decision.

Conceptually:

Evidence {
    subject
    claim
    source
    observed_at
    authority
    confidence
    provenance
}

Evidence is not synonymous with truth.

Its strength depends on its source and authority.

⸻

16. Canonical Data

Canonical Data represents authoritative enterprise facts within a defined scope.

Canonical Data
      │
      ├── source
      ├── authority
      ├── scope
      ├── value
      └── temporal metadata

The Data Model must preserve the distinction between:

canonical
derived
inferred
cached
observed
historical
unknown

⸻

17. Constraint

A Constraint limits what may be valid or executable.

Examples:

refund.amount <= 5000
account.status = ACTIVE
transfer.currency = USD

Constraints may originate from:

Policy
System Capability
Business Rule
Resource State
Enterprise Configuration

⸻

18. Policy

Policy determines what is permitted, required, prohibited, or conditionally allowed.

Examples:

refunds above $5,000 require approval
employees cannot modify their own payroll
transfers above $50,000 require MFA

Policy is data within the semantic model but has normative authority.

⸻

19. Action

An Action represents an executable operation.

Examples:

refund_payment
freeze_card
create_user
transfer_funds
cancel_order

Actions operate against Resources through enterprise Capabilities.

Action
   ↓
Capability
   ↓
Enterprise System
   ↓
Resource

⸻

20. Intent

Intent represents the desired outcome or objective of a Principal.

Example:

"Refund my last payment."

may resolve to:

Intent {
    objective = REFUND
    resource = Payment:123
}

Intent is not itself an Action.

⸻

21. Intent vs Action

Intent:
"What the user wants."
Action:
"What the system can execute."

Example:

Intent:
"Get me a refund."
Action:
refund_payment(payment_id)

The Data Model preserves this distinction.

⸻

22. Outcome

Outcome represents what resulted from an attempted Action.

Examples:

SUCCESS
FAILED
PARTIAL
REQUIRES_INTERVENTION
UNKNOWN

Outcome should be grounded in observed execution results rather than inferred solely from Action submission.

⸻

23. Execution

Execution represents a concrete attempt to perform an Action.

Conceptually:

Execution {
    execution_id
    action
    context
    state
    attempts
    outcome
    timestamps
}

Execution connects Intent to real-world system activity.

⸻

24. Execution Data vs Enterprise Data

Noema must distinguish:

Enterprise Data

from:

Noema Execution Data

For example:

Enterprise:
payment.status = REFUNDED
Noema:
execution.status = COMPLETED

The two values are related but describe different domains.

⸻

25. Provenance

Every consequential data item should have sufficient provenance.

Conceptually:

Provenance {
    source
    authority
    observed_at
    effective_at
    version
    transformation
}

This allows Noema to determine:

Where did this information come from?

⸻

26. Source

Source identifies where data originated.

Examples:

CRM
Ledger
Payment API
HRIS
Event Bus
User
Noema

Source and authority are distinct.

A source may provide information without being authoritative for that particular fact.

⸻

27. Authority

Authority determines whether a source is authoritative for a particular fact.

Source:
Analytics DB
Authority for:
reporting metrics
Authority for:
account.balance
NO

The Data Model must not equate source presence with authority.

⸻

28. Scope

Data must have an understood scope.

Possible dimensions include:

tenant
organization
legal entity
environment
system
resource
attribute
time

Scope prevents accidental cross-boundary interpretation.

⸻

29. Temporal Data

Data may have multiple relevant timestamps:

observed_at
effective_at
created_at
updated_at
expires_at

These timestamps answer different questions.

For example:

effective_at
→ when the fact became true
observed_at
→ when Noema learned it

⸻

30. Version

Data may be versioned.

Account
version = 42

Version information supports:

optimistic concurrency
revalidation
reconciliation
auditability

⸻

31. Freshness

Freshness describes how current a data observation is relative to the requirement of an Action.

Freshness is not identical to authority.

canonical + stale

is possible.

Likewise:

fresh + non-canonical

is possible.

⸻

32. Uncertainty

The Data Model must represent uncertainty explicitly.

Possible states include:

KNOWN
UNKNOWN
AMBIGUOUS
CONFLICTED
STALE
UNAVAILABLE

Noema should not collapse these into a generic null.

⸻

33. Derived Data

Derived information should retain its derivation semantics.

Example:

customer_risk_score

may be calculated from:

transaction_history
payment_history
account_age

The resulting value should not be mistaken for canonical enterprise data unless the enterprise explicitly defines it as such.

⸻

34. Inferred Data

Inference represents a conclusion generated from available information.

Example:

likely_account = 123

Inference should be distinguishable from verified identity:

canonical_account = 123

This distinction is particularly important during Intent Resolution.

⸻

35. User-Provided Data

User-provided information is an important input to the Data Model.

User:
"Use account 123."

This creates an input fact.

It does not automatically establish:

account 123 exists
user owns account 123
user is authorized to operate account 123

Those facts require appropriate verification.

⸻

36. Data Classification

A useful semantic classification is:

CANONICAL
OBSERVED
DERIVED
INFERRED
USER_PROVIDED
HISTORICAL
UNKNOWN

Classification should be preserved where it affects Trust or execution.

⸻

37. Data Dependencies

Data objects may depend on other objects.

Example:

Risk Score
   ↓ depends_on
Transaction History
   ↓ sourced_from
Ledger

Dependency relationships support:

provenance
recomputation
invalidity detection
auditability

⸻

38. Data Lineage

Lineage represents how a value was produced.

Canonical Data
      ↓
Transformation
      ↓
Derived Data
      ↓
Context
      ↓
Evidence
      ↓
Decision

For consequential Actions, Noema should be able to trace this path where feasible.

⸻

39. Data Relationships

The core semantic relationships include:

Entity ──has──> Attribute
Entity ──has──> Resource
Resource ──has──> State
Resource ──related_to──> Resource
Intent ──refers_to──> Resource
Intent ──resolves_to──> Action
Action ──operates_on──> Resource
Action ──requires──> Context
Action ──requires──> Preconditions
Action ──produces──> Outcome
Policy ──governs──> Action
Evidence ──supports──> Claim
Data ──sourced_from──> System

⸻

40. The Noema Data Graph

These relationships form a semantic graph:

                  Policy
                    │
                  governs
                    ▼
Intent ────────> Action
  │                │
refers_to       operates_on
  │                │
  ▼                ▼
Resource ──────> State
  │
  │
  ▼
Canonical Data
  │
  ▼
Evidence
  │
  ▼
Trust
  │
  ▼
Execution
  │
  ▼
Outcome

This is not necessarily a requirement that Noema use a graph database.

It is a description of the semantic relationships.

⸻

41. Data Model and Enterprise Action Graph

The Enterprise Action Graph describes what an enterprise can do.

The Data Model describes the information required to understand and execute those operations.

Enterprise Action Graph
        +
Noema Data Model
        ↓
Runtime Execution Context

⸻

42. Data Model and Integration

Integration translates enterprise-specific representations into Noema’s semantic model.

Example:

Enterprise A:
{
    payment_status: "completed"
}
Enterprise B:
{
    state: "succeeded"
}

Both may map to:

Payment.status = SUCCEEDED

The Integration layer handles translation.

The Data Model defines the meaning of Payment.status.

⸻

43. Data Model and APIs

APIs expose enterprise data and capabilities.

The Data Model determines how returned information is semantically represented.

API Response
     ↓
Integration Mapping
     ↓
Data Model
     ↓
Context

⸻

44. Data Model and Events

Events represent changes or occurrences.

payment.refunded

may update or invalidate Context concerning:

Payment.status

The event model should map cleanly into the Data Model without conflating events with persistent state.

⸻

45. Data Model and State

State is a first-class concept because Noema frequently asks:

“What is true about this Resource now?”

For example:

Account.status = ACTIVE

is semantically different from:

Account.status_changed_at = ...

State should therefore not be reduced to arbitrary event history.

⸻

46. Data Model and Policy

Policy may depend on data.

Example:

if transfer.amount > 50000
then approval_required

The Data Model must represent the relationship between:

Policy
Amount
Action
Principal
Approval Requirement

⸻

47. Data Model and Preconditions

Preconditions consume Data Model values.

Precondition:
account.status == ACTIVE

The referenced state must resolve to an authoritative or appropriately trusted value.

⸻

48. Data Model and Postconditions

Postconditions also reference Data Model values.

Postcondition:
payment.status == REFUNDED

The resulting state should be verified through the appropriate source.

⸻

49. Data Model and Trust

Trust evaluates relationships among:

data
authority
identity
policy
risk
evidence
state

The Data Model provides the semantic substrate on which Trust operates.

⸻

50. Data Model and Determinism

Deterministic execution requires explicit semantics.

For example:

balance = 10000

must mean:

which account?
which currency?
which system?
which timestamp?
which tenant?

The Data Model should provide the structure necessary to answer these questions.

⸻

51. Data Model and Ambiguity

Ambiguity exists when the Data Model cannot uniquely resolve a reference.

Example:

"my account"

may map to:

Account A
Account B
Account C

Noema should preserve this ambiguity until resolved.

⸻

52. Data Model and Identity Resolution

Identity resolution maps natural-language references to canonical entities.

"John's account"
      ↓
Candidate Accounts
      ↓
Identity Resolution
      ↓
Canonical Account

The Data Model provides the identifiers and relationships needed to perform that resolution.

⸻

53. Data Model and Compound Intent

Compound Intent may produce multiple Actions operating across multiple Resource types.

Example:

"Cancel my order, refund the payment, and close the account."

maps to:

Order
  ↓
cancel_order
Payment
  ↓
refund_payment
Account
  ↓
close_account

The Data Model provides the relationships connecting these Resources.

⸻

54. Data Model and Ownership

Ownership is represented explicitly.

Example:

Customer
   │
 owns
   ▼
Account

Ownership should not be inferred solely from:

email
name
phone number
conversation history

when authoritative relationships exist.

⸻

55. Data Model and Permissions

Permission data determines whether a Principal can perform an Action against a Resource.

Principal
    │
 authorized_for
    ▼
Action
    │
 operates_on
    ▼
Resource

Permission is not inferred simply from Resource visibility.

⸻

56. Data Model and Organizational Boundaries

The Data Model must preserve organizational relationships and boundaries.

Organization
    │
    ├── Business Unit
    ├── Team
    └── Principal

These relationships can affect:

authorization
policy
resource visibility
Action availability

⸻

57. Data Model and Data Boundaries

Data access must respect:

tenant
organization
legal entity
environment
classification
purpose
permission

The Data Model does not grant access merely by representing a piece of data.

⸻

58. Data Model and Auditability

The Data Model should support reconstructing:

what was known
what was believed
what was authoritative
what Action was selected
what Policy applied
what Execution occurred
what Outcome resulted

This is essential for enterprise-grade automation.

⸻

59. Immutable Observations

Where appropriate, observations used for consequential decisions should be immutable.

Instead of:

balance = $10,000

being overwritten with:

balance = $8,000

Noema may preserve:

Observation 1:
balance = $10,000
Observation 2:
balance = $8,000

This improves auditability and temporal reasoning.

⸻

60. Data Model and Long-Running Execution

Data may change during execution.

Therefore an Execution may need to retain:

initial Context
current Context
revalidated Context
observed changes

This allows Noema to determine whether Preconditions remain valid.

⸻

61. Data Model and Reconciliation

Reconciliation compares Noema’s expected state with observed enterprise state.

Expected:
payment.status = REFUNDED
Observed:
payment.status = SUCCEEDED

The Data Model provides the common semantic representation required to detect this discrepancy.

⸻

62. Data Model and Failure

Failures should be represented semantically rather than as arbitrary strings.

Conceptually:

Failure {
    type
    source
    phase
    retryable
    recoverable
    details
}

This allows Execution logic to reason consistently about failures.

⸻

63. Data Model and Unknown Outcomes

An Action may succeed at the enterprise boundary while Noema fails to observe the result.

Example:

Request sent
     ↓
Timeout
     ↓
Result UNKNOWN

The Data Model must support:

Outcome = UNKNOWN

rather than incorrectly recording:

Outcome = FAILED

⸻

64. Data Model and Idempotency

Execution records should connect Actions with their idempotency identity.

Action
   │
   └── idempotency_key
             ↓
        Execution

This allows Noema to distinguish:

new execution

from:

retry of existing execution

⸻

65. Data Model and Compensation

Compensation requires knowledge of:

prior Action
prior state
current state
available capabilities

The Data Model therefore provides the semantic information required to determine whether compensation is possible.

⸻

66. Data Model and Human Intervention

When Noema cannot safely continue, intervention records should reference the relevant semantic objects:

Intent
Action
Resource
Context
Policy
Evidence
Failure
Execution

This gives the human operator enough context to make an informed decision.

⸻

67. Data Model and Noema Ownership Boundary

Noema should own semantic and execution data necessary to operate its Trust and Execution systems.

The enterprise should remain authoritative for enterprise Business State.

Noema owns:
Intent lifecycle
Trust decisions
Execution records
Action semantics
Evidence records
Enterprise owns:
Accounts
Balances
Payments
Orders
Employees
Business transactions

The exact boundary is enterprise-specific.

⸻

68. Canonical Data Model

The foundational object relationship is:

Enterprise System
       │
       ▼
Canonical Data
       │
       ▼
Data Model
       │
       ▼
Context
       │
       ▼
Evidence
       │
       ▼
Trust
       │
       ▼
Execution

The Data Model provides the semantic bridge between enterprise truth and Noema execution.

⸻

69. Conceptual Core Schema

A simplified conceptual model:

Principal
   │
   ▼
Intent
   │
   ├──────────► Context
   │               │
   │               ▼
   │            Evidence
   │               │
   ▼               ▼
Resource ─────► Trust
   │               │
   ▼               ▼
State          Decision
                   │
                   ▼
                 Action
                   │
                   ▼
               Execution
                   │
                   ▼
                Outcome

⸻

70. Core Invariants

Invariant 1

The Data Model is semantic, not merely a storage schema.

Invariant 2

Noema’s semantic representation does not transfer ownership of enterprise data.

Invariant 3

Enterprise-specific schemas must be mapped into the Noema semantic model through explicit integration semantics.

Invariant 4

Entities, Resources, State, Context, Evidence, Policy, Actions, and Outcomes are distinct semantic concepts.

Invariant 5

Intent and Action must remain distinct.

Invariant 6

Enterprise Business State and Noema Execution State must remain distinct.

Invariant 7

Canonical Data must remain distinguishable from derived, inferred, cached, and user-provided data.

Invariant 8

Data used for consequential execution should retain sufficient provenance.

Invariant 9

Authority and source are distinct concepts.

Invariant 10

Freshness and authority are distinct concepts.

Invariant 11

Unknown, ambiguous, stale, unavailable, and conflicted states must remain semantically distinguishable where consequential.

Invariant 12

Identity must include sufficient scope to prevent accidental cross-entity resolution.

Invariant 13

Relationships are first-class semantic information.

Invariant 14

Temporal information must be preserved when it affects interpretation or execution.

Invariant 15

Version information should be preserved when required for concurrency, validation, or auditability.

Invariant 16

User-provided information must not automatically become canonical enterprise data.

Invariant 17

Model inference must not automatically become canonical enterprise data.

Invariant 18

Events must remain distinguishable from persistent state.

Invariant 19

Context must remain distinguishable from Business State.

Invariant 20

Policy constrains data-driven execution; data does not override Policy.

Invariant 21

Representation of data does not grant authorization to access or use it.

Invariant 22

Data access must respect enterprise organizational and tenant boundaries.

Invariant 23

Noema should not create shadow canonical representations of enterprise Business State.

Invariant 24

Execution data must be sufficient to connect Intent, Context, Action, Execution, and Outcome.

Invariant 25

Unknown execution outcomes must not be incorrectly converted into failure or success.

Invariant 26

Data required for consequential execution must be revalidated when freshness requirements demand it.

Invariant 27

Historical observations required for auditability must not be silently overwritten.

Invariant 28

Derived data should preserve its dependency and derivation semantics where consequential.

Invariant 29

The Data Model must support deterministic reasoning without requiring the underlying model to be deterministic.

Invariant 30

The Data Model must preserve enough structure to distinguish what is known, what is authoritative, what is inferred, what is uncertain, and what changed.

⸻

71. Final Definition

The Noema Data Model is the semantic foundation through which Noema represents enterprise entities, resources, state, context, evidence, policies, actions, executions, and outcomes while preserving authority, provenance, temporal semantics, uncertainty, and enterprise ownership boundaries.

Its fundamental role is:

ENTERPRISE TRUTH
      │
      ▼
SEMANTIC DATA MODEL
      │
      ▼
RUNTIME CONTEXT
      │
      ▼
TRUST
      │
      ▼
EXECUTION
      │
      ▼
OBSERVED OUTCOME
      │
      ▼
ENTERPRISE TRUTH

The central rule is:

Noema’s Data Model should make enterprise information understandable and executable without making Noema the owner of that information.