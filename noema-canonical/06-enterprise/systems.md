Systems

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/systems.md

⸻

1. Definition

A System is a bounded enterprise software or infrastructure component that owns, exposes, transforms, or consumes business capabilities and state.

Systems are the operational machinery through which an enterprise represents its business and performs work.

Examples include:

CRM
ERP
Ledger
Payment Platform
Identity Provider
HRIS
Inventory System
Ticketing System
Communication Platform
Data Warehouse
Document Store

Noema does not treat all systems equally.

A system may be:

authoritative
transactional
derived
analytical
integrational
event-producing
event-consuming

The distinction matters because Noema must know which system is authoritative for which facts and capabilities.

⸻

2. Purpose

The Systems concept provides Noema with a canonical way to represent the enterprise technology environment.

Noema needs to understand:

What systems exist?
What does each system own?
What capabilities does each expose?
What resources does each manage?
What data does it contain?
What events does it emit?
What policies constrain it?
Which system is authoritative for a given fact?
How can Noema interact with it?

Without this model, the Enterprise Action Graph becomes merely a collection of disconnected APIs.

⸻

3. Core Principle

A system is not defined merely by its API. It is defined by the capabilities, resources, state, authority, and boundaries it participates in.

For example:

Payment API

is an interface.

The underlying:

Payment System

may own:

payments
refunds
captures
payment status

Noema should model both the system and its interfaces.

⸻

4. System vs Integration

These are distinct concepts.

System

The enterprise component that owns or participates in business operations.

Integration

The mechanism through which Noema interacts with that system.

System
   │
   ├── REST API
   ├── GraphQL API
   ├── Events
   ├── Webhooks
   └── SDK

Therefore:

System ≠ Integration

A single system may have many integrations.

⸻

5. System vs System of Record

A system may exist without being authoritative for a particular domain.

For example:

Analytics Database

is a system.

It may contain:

customer data
payment data
order data

but not be authoritative for any of them.

Therefore:

System
    ↓
may be
    ↓
System of Record

but:

System ≠ System of Record

⸻

6. System Categories

Systems may be classified according to their role.

Transactional
Authoritative
Derived
Analytical
Operational
Identity
Policy
Integration
Event
Observability

A system may belong to multiple categories.

For example:

Ledger
→ transactional
→ authoritative
→ event-producing

⸻

7. Transactional Systems

Transactional systems perform business operations and maintain mutable Business State.

Examples:

Banking Core
Payment System
Order Management
Inventory System

These systems are often directly involved in Noema execution.

⸻

8. Authoritative Systems

An authoritative system is the designated System of Record for a particular domain or fact.

Examples:

Ledger
→ account balance
HRIS
→ employment status
IAM
→ identity and access
CRM
→ customer relationship record

Authority is defined per domain rather than assumed globally.

⸻

9. Derived Systems

Derived systems transform information from other systems.

Examples:

Search Index
Cache
Materialized View
Event Projection
Data Warehouse
Analytics Database

They may be valuable Context sources but generally should not override the authoritative source.

⸻

10. Analytical Systems

Analytical systems optimize for:

reporting
aggregation
historical analysis
forecasting
business intelligence

They may contain highly useful enterprise information while remaining unsuitable for authoritative transactional decisions.

Example:

Data Warehouse:
revenue = $10.4M

does not necessarily mean it should be used as the authority for:

"Can this payment be refunded right now?"

⸻

11. Identity Systems

Identity systems manage:

users
service principals
groups
roles
credentials
authentication
authorization relationships

Examples:

Identity Provider
Directory
IAM platform

Noema consumes identity information from these systems.

⸻

12. Policy Systems

Some enterprises maintain policy separately from the systems that execute business operations.

Examples:

Authorization Policy Engine
Risk Engine
Compliance Platform
Approval System

These systems may provide decisions or constraints used by Noema’s Trust Engine.

⸻

13. Event Systems

Event systems transport or persist enterprise events.

Examples:

Event Bus
Message Broker
Streaming Platform
Webhook Infrastructure

Events can provide evidence about enterprise state transitions.

They do not automatically become authoritative Business State.

⸻

14. System Identity

Every integrated system should have a stable identity within Noema.

Conceptually:

System {
    system_id
    name
    type
    owner
    domain
    environment
    version
}

Example:

system_id:
payments.production
domain:
payments
environment:
production

⸻

15. System Ownership

A system should have an identifiable enterprise owner where possible.

Ownership may belong to:

team
department
business unit
legal entity
external provider

Ownership matters for:

support
governance
authorization
incident response
schema changes
policy

⸻

16. System Boundary

A system should have an explicit boundary.

┌──────────────────────────────┐
│        Payment System        │
│                              │
│  Payment State               │
│  Refunds                     │
│  Captures                    │
│  Payment Events              │
│                              │
│  REST API                    │
│  Event Stream                │
└──────────────────────────────┘

Noema interacts through the exposed boundary rather than reaching directly into internal implementation details.

⸻

17. System Resources

A system manages or exposes Resources.

For example:

Payment System
    ├── Payment
    ├── Refund
    ├── Capture
    └── Payment Method

The relationship is:

System
   ↓ manages
Resource

⸻

18. System Capabilities

Systems expose Capabilities.

Example:

Payment System
    ├── create_payment
    ├── capture_payment
    ├── refund_payment
    └── void_payment

The relationship is:

System
   ↓ exposes
Capability

A Capability describes what the system can do.

⸻

19. System Actions

Noema’s Actions invoke enterprise Capabilities.

Intent
   ↓
Action
   ↓
Capability
   ↓
System

Example:

Action:
refund_payment
Capability:
refund_payment
System:
Payment System

⸻

20. System State

A system may own or expose Business State.

Example:

Payment System
      ↓
Payment #123
      ↓
status = SUCCEEDED

Noema may observe this state.

The system remains authoritative where designated.

⸻

21. System Events

Systems may emit events describing state changes.

Example:

Payment System
      ↓
payment.refunded
      ↓
Event Infrastructure
      ↓
Noema

Events can update Context or trigger execution-related transitions.

⸻

22. System Dependencies

Systems rarely operate independently.

Example:

Order System
     │
     ├── Payment System
     ├── Inventory System
     └── Shipping System

Noema should understand relevant dependencies when planning compound Actions.

⸻

23. System Graph

Systems form part of the Enterprise Action Graph.

System
  │
  ├── owns → Resource
  │
  ├── exposes → Capability
  │
  ├── emits → Event
  │
  ├── consumes → Event
  │
  ├── depends_on → System
  │
  ├── governed_by → Policy
  │
  └── authoritative_for → Fact

This graph allows Noema to reason about enterprise execution paths.

⸻

24. System Relationships

Important relationships include:

owns
manages
exposes
depends_on
integrates_with
emits
consumes
authoritative_for
derived_from
governed_by

These relationships should remain explicit rather than inferred from arbitrary API behavior.

⸻

25. System Authority

Authority should be represented at the level of facts or resources.

Example:

Ledger
→ authoritative_for
→ Account Balance

while:

Analytics Warehouse
→ derived_from
→ Ledger

This allows Noema to distinguish authority from accessibility.

⸻

26. Multiple Systems and One Resource

An enterprise may represent the same logical Resource across multiple systems.

Example:

Customer
   │
   ├── CRM
   ├── Billing
   └── Support

These representations may not be equally authoritative.

Noema should maintain the relationship between:

logical resource

and:

system-specific representation

where necessary.

⸻

27. System Identity vs Resource Identity

A Resource may have different identifiers across systems.

Example:

CRM:
customer_id = C123
Billing:
customer_id = 847291
Support:
customer_id = USER-991

Noema may need an identity mapping.

However, this mapping should not cause Noema to become the owner of customer identity.

⸻

28. System Environment

A system may exist in multiple environments:

development
staging
production

These should be represented distinctly.

payments.dev
payments.staging
payments.production

An Action targeting production must not accidentally resolve to staging.

⸻

29. System Version

Systems evolve.

A system representation may therefore include:

API version
schema version
capability version
deployment version

This is particularly important for Action Contracts.

⸻

30. System Capability Versioning

A Capability may change over time.

Example:

refund_payment:v1
refund_payment:v2

The differences may include:

parameters
authorization
side effects
postconditions
error semantics
idempotency

Noema should treat material capability changes as contract changes.

⸻

31. System Availability

A system may be:

healthy
degraded
unavailable
maintenance
unknown

Availability may influence execution planning.

However:

system_available

does not mean:

Action_safe

Availability is only one execution consideration.

⸻

32. System Health vs Business State

These concepts are distinct.

Payment System:
HEALTHY
Payment:
DECLINED

The system is functioning correctly while the business operation is unsuccessful.

Conversely:

Payment System:
DEGRADED
Payment:
SUCCEEDED

The business state may still be valid.

⸻

33. System Failure

Systems can fail independently of Noema.

Examples:

timeout
5xx
connection failure
rate limiting
partial response
provider outage
schema incompatibility

Noema should classify the failure without automatically assuming the business operation failed.

⸻

34. Unknown Outcome

A particularly important case:

Noema
  ↓
System
  ↓
request
  ↓
timeout

The system may have executed the Action despite the timeout.

Therefore:

Transport Failure
≠
Business Failure

Noema may need to reconcile against the System of Record.

⸻

35. System Consistency Model

Systems may provide different consistency guarantees:

strong consistency
eventual consistency
read-after-write consistency
session consistency

Noema should understand the relevant guarantees when verifying Preconditions and Postconditions.

⸻

36. System Transactions

A system may support:

atomic transactions
conditional writes
optimistic locking
pessimistic locking
idempotency

Noema should use these capabilities where available rather than recreating transactional semantics externally.

⸻

37. Cross-System Execution

Many enterprise Actions span multiple systems.

Example:

"Refund the payment and close the account."
        ↓
Payment System
→ refund
        ↓
Account System
→ close account

Noema must recognize that these are separate execution boundaries.

There may be no distributed transaction spanning them.

⸻

38. System Dependencies and Planning

Planning must account for system dependencies.

Example:

close_account
     requires
refund_outstanding_balance

Therefore:

Refund
   ↓
verify outcome
   ↓
Close Account

The system graph can provide information necessary to construct this execution order.

⸻

39. System Dependency Failure

If:

Payment System

is unavailable, Noema may be unable to safely execute:

close_account

if the account closure requires the payment state to be verified.

Planning should therefore consider dependency availability.

⸻

40. System as a Trust Input

System metadata can influence Trust.

Relevant attributes include:

system identity
authority
environment
availability
version
capability
data provenance

For example:

Production Ledger

is stronger evidence for account balance than:

Analytics Replica

⸻

41. System as Evidence Source

A system response should carry provenance where consequential.

Conceptually:

Evidence {
    system
    capability
    resource
    value
    observed_at
    version
}

This lets Trust distinguish:

authoritative enterprise evidence

from:

model inference

⸻

42. System and Context

Systems contribute to Enterprise Context.

Example:

Context
├── Customer
│   └── source = CRM
│
├── Payment
│   └── source = Payment System
│
└── Balance
    └── source = Ledger

Context should preserve the system origin of consequential information.

⸻

43. System and Data Boundaries

Not every system should expose all of its data to Noema.

A system integration should define:

accessible resources
accessible fields
permitted operations
retention rules
redaction rules

This supports least-privilege access.

⸻

44. System and Permissions

System access does not automatically equal business authorization.

For example:

Noema credential:
can call POST /refund

does not necessarily mean:

principal:
is authorized to refund this payment

Technical access and business authorization must remain distinct.

⸻

45. System Credentials

Noema may use:

service credentials
OAuth tokens
API keys
mTLS identities
delegated credentials

These establish technical access to the system.

They should not obscure the effective business principal responsible for the Action.

⸻

46. System and Delegation

An enterprise may allow:

Human
 ↓
Noema
 ↓
System Credential

The system sees the technical credential, while Noema’s audit model preserves the originating principal and delegation context.

⸻

47. System and Auditability

Every consequential system interaction should be attributable where practical.

An audit record may include:

execution_id
system_id
integration_id
capability
principal
resource
request_id
timestamp
result

This establishes the connection between Noema execution and enterprise system behavior.

⸻

48. System and Observability

Systems should expose operational signals where appropriate:

latency
availability
error rate
request identifiers
provider status

These signals can improve execution reliability without becoming Business State themselves.

⸻

49. System and Action Contracts

Action Contracts should bind Actions to concrete system capabilities.

Example:

Action Contract
Action:
refund_payment
System:
payments.production
Capability:
refund_payment:v2
Input:
payment_id
amount
currency
Preconditions:
payment.status = SUCCEEDED
Postcondition:
refund.status = COMPLETED

This transforms an abstract Action into a bounded enterprise operation.

⸻

50. System and API Drift

If the system changes its interface:

v1:
refund(payment_id, amount)
v2:
refund(payment_id, amount, currency)

Noema should detect the contract mismatch.

It should not allow a model to improvise the missing parameter.

⸻

51. System and Policy Drift

A system’s policy requirements may change.

Example:

Previously:
refunds < $1,000

becomes:

refunds < $500

Noema must treat this as a meaningful authorization or policy change rather than assuming previous execution behavior remains valid.

⸻

52. System and Schema Drift

Schema changes can affect:

resource identity
resource state
capability inputs
capability outputs
postconditions

Schema validation therefore forms part of the enterprise integration boundary.

⸻

53. System Registration

A system integrated with Noema should have an explicit registration or discovery representation.

Conceptually:

System Registration
├── identity
├── owner
├── environment
├── capabilities
├── resources
├── integrations
├── authority
├── events
└── policies

This metadata can feed the Enterprise Action Graph.

⸻

54. System Discovery

Systems may be discovered from:

API specifications
service registries
documentation
configuration
event schemas
human configuration
integration metadata

Discovery does not imply authorization.

A discovered system is not automatically trusted for execution.

⸻

55. System Trust

Noema should distinguish:

system exists

from:

system is trusted for this operation

Trust may depend on:

identity
authentication
authorization
provenance
environment
capability
policy
risk

⸻

56. External Systems

Some systems are outside the enterprise.

Examples:

Payment Provider
Shipping Provider
Email Provider
Identity Provider

Noema should explicitly model their external status.

Enterprise
   │
   ├── Internal System
   │
   └── External Provider

This matters for authority and failure semantics.

⸻

57. External Provider vs Enterprise System of Record

An external provider may process an operation while the enterprise remains authoritative for its own Business State.

Example:

Payment Provider
→ processes payment
Enterprise Ledger
→ records financial state

The provider response is important evidence but does not automatically become the enterprise’s canonical ledger state.

⸻

58. System Boundaries and Legal Entities

Systems may serve multiple legal entities.

Example:

ERP
├── Nigeria Ltd.
├── UK Ltd.
└── US Inc.

Noema must preserve organizational and legal-entity boundaries when resolving Resources and Permissions.

⸻

59. System Isolation

Noema must prevent accidental cross-system or cross-tenant execution.

For example:

Tenant A
→ Payment System A
Tenant B
→ Payment System B

A resource identifier alone must not be sufficient to cross the boundary.

⸻

60. System Lifecycle

Systems have lifecycle states:

planned
active
degraded
deprecated
retired

Noema should not execute against:

deprecated

or:

retired

systems unless explicitly supported by enterprise policy.

⸻

61. System Migration

When an enterprise migrates:

System A
    ↓
System B

Noema must understand:

old authority
new authority
migration period
routing
resource mapping
capability differences

This prevents execution against the wrong system during transitions.

⸻

62. System Replacement

Replacing a system should not require redefining enterprise Intent semantics.

For example:

Intent:
"Refund the payment."

should remain stable while:

Payment System A

becomes:

Payment System B

Only the enterprise capability/integration layer should need substantial change.

This is an important abstraction boundary.

⸻

63. System Abstraction

Noema should reason primarily in terms of:

Intent
Action
Capability
Resource
Policy

rather than:

HTTP endpoint
database table
vendor SDK

The system and integration layers translate those concepts into implementation-specific operations.

⸻

64. System as an Enterprise Primitive

The Systems model provides the infrastructure beneath the Enterprise Action Graph:

Enterprise
    │
    ├── Systems
    │     ├── Resources
    │     ├── Capabilities
    │     ├── Events
    │     └── Authority
    │
    └── Policies
           │
           ▼
        Noema
           │
           ├── Intent
           ├── Trust
           ├── Action
           └── Execution

⸻

65. Canonical System Model

System {
    system_id
    name
    type
    owner
    domain
    environment
    version
    resources[]
    capabilities[]
    integrations[]
    events[]
    authoritative_for[]
    dependencies[]
    consistency_model
    lifecycle_state
}

Not every implementation must expose every field. The model defines the semantic concepts, not necessarily a literal database schema.

⸻

66. Canonical Relationships

System
 ├── owns → Resource
 ├── manages → Resource
 ├── exposes → Capability
 ├── accessed_by → Integration
 ├── emits → Event
 ├── consumes → Event
 ├── depends_on → System
 ├── authoritative_for → Fact
 ├── derived_from → System
 ├── governed_by → Policy
 └── belongs_to → Organization

⸻

67. Canonical Invariants

Invariant 1

A System is distinct from an Integration.

Invariant 2

A System is distinct from a System of Record.

Invariant 3

A System may own or manage Resources.

Invariant 4

A System may expose Capabilities.

Invariant 5

System authority must be explicit rather than inferred from accessibility.

Invariant 6

A system’s API does not automatically establish business authorization.

Invariant 7

Technical system credentials must not obscure the originating business principal.

Invariant 8

System environments must be explicitly distinguished.

Invariant 9

System versions must be considered when they affect Action Contracts or execution semantics.

Invariant 10

Derived systems must not silently override authoritative systems.

Invariant 11

System events are evidence of state transitions and do not automatically establish current Business State.

Invariant 12

Transport failure must not automatically be interpreted as business-operation failure.

Invariant 13

Unknown execution outcomes should be reconciled against the appropriate System of Record.

Invariant 14

Cross-system execution must not assume distributed atomicity unless explicitly guaranteed.

Invariant 15

System dependencies may affect Action planning and execution.

Invariant 16

System discovery does not imply system trust or authorization.

Invariant 17

System lifecycle state must be respected by execution.

Invariant 18

System migrations must preserve authority and resource identity semantics.

Invariant 19

Noema should abstract enterprise capabilities from vendor-specific implementation details.

Invariant 20

Replacing an enterprise system should not require changing the semantic definition of the Intent it serves.

Invariant 21

System provenance should be preserved for consequential Context and Evidence.

Invariant 22

Noema must not bypass system boundaries by directly manipulating underlying enterprise storage.

Invariant 23

External providers and internal enterprise systems must remain distinguishable.

Invariant 24

System boundaries must respect tenant, organizational, legal, and data boundaries.

Invariant 25

Noema must never infer enterprise authority solely from model output.

⸻

68. Final Definition

A System is a bounded enterprise component that owns, manages, exposes, transforms, or transports business capabilities and state. Noema models systems as part of the Enterprise Action Graph so it can determine where Resources live, which Capabilities are available, where authoritative state resides, and how Actions can safely cross enterprise boundaries.

The essential abstraction is:

                  ENTERPRISE
                       │
                    Systems
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Resources     Capabilities     Events
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                    Noema
                       │
                Intent → Trust
                       │
                    Action
                       │
                       ▼
                  Integration
                       │
                       ▼
                    System
                       │
                       ▼
               Business State

And the key architectural rule remains:

Noema should understand the enterprise’s systems deeply enough to execute safely, but abstract them deeply enough that Noema’s Intent and Action semantics do not become coupled to any particular vendor, API, database, or implementation.