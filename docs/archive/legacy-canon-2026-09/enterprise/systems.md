> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Systems

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/systems.md

⸻

1. Definition

A System is a bounded enterprise software or infrastructure component that owns, exposes, transforms, stores, or consumes business capabilities, resources, events, or state.

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
policy-enforcing
identity-managing

The distinction matters because Noema must know which system is authoritative for which facts, resources, and capabilities.

A System is an enterprise primitive represented in the Enterprise Action Graph and connected to Resources, Capabilities, Policies, Events, Integrations, and authority relationships.

⸻

2. Purpose

The Systems concept provides Noema with a canonical way to represent the enterprise technology environment.

Noema needs to understand:

What systems exist?
What does each system own or manage?
What capabilities does each expose?
What resources does it manage?
What data does it contain or expose?
What events does it emit or consume?
What policies constrain it?
Which system is authoritative for a given fact or resource?
How can Noema interact with it?
What consistency and failure semantics does it provide?
What organizational, tenant, legal, and data boundaries apply?

Without this model, the Enterprise Action Graph becomes merely a collection of disconnected APIs.

The Systems model allows Noema to reason about enterprise execution without coupling Intent semantics to particular vendors, endpoints, databases, or implementation technologies.

⸻

3. Core Principle

A system is not defined merely by its API. It is defined by the capabilities, resources, state, authority, events, dependencies, and boundaries it participates in.

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

Noema should model both the System and the Integrations through which it is accessed.

Accessibility does not establish authority.

A system being callable by Noema does not mean that its returned data is authoritative or that a principal is authorized to perform every operation it exposes.

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

An integration is an access and translation boundary. It does not become the enterprise authority merely because it is the interface through which Noema receives information.

⸻

5. System vs System of Record

A system may exist without being authoritative for a particular domain or fact.

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

System of Record is a specific authority designation within the broader Systems model.

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

Classification describes system participation; it does not by itself establish authority for every fact or operation.

⸻

7. Transactional Systems

Transactional systems perform business operations and maintain mutable Business State.

Examples:

Banking Core
Payment System
Order Management
Inventory System

These systems are often directly involved in Noema execution.

Noema should use the transactional semantics provided by these systems where available rather than recreating Business State management locally.

⸻

8. Authoritative Systems

An authoritative system is the designated System of Record for a particular domain, resource, claim, or fact.

Examples:

Ledger
→ account balance

HRIS
→ employment status

IAM
→ identity and access relationships

CRM
→ customer relationship record

Authority is defined per domain and claim rather than assumed globally.

A system can therefore be authoritative for one fact while merely providing evidence for another.

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

A derived representation remains non-authoritative unless the enterprise explicitly designates it as authoritative for the relevant claim.

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

Analytical usefulness does not imply transactional authority.

⸻

11. Identity Systems

Identity systems manage or participate in:

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

Identity data must still pass through applicable schema validation and admission boundaries before becoming eligible for consequential Noema processing.

Identity authority remains enterprise-owned.

⸻

12. Policy Systems

Some enterprises maintain policy separately from the systems that execute business operations.

Examples:

Authorization Policy Engine
Risk Engine
Compliance Platform
Approval System

These systems may provide decisions or constraints used by Noema’s Trust Engine.

Noema should preserve the distinction between:

enterprise policy decision

and:

Noema Trust decision.

A policy system may provide authoritative policy evaluation without becoming the source of Noema’s overall Trust decision.

⸻

13. Event Systems

Event systems transport or persist enterprise events.

Examples:

Event Bus
Message Broker
Streaming Platform
Webhook Infrastructure

Events can provide observations or evidence about enterprise state transitions.

They do not automatically become authoritative Business State.

Event occurrence, event payload, reconciled state, and current Business State remain distinct concepts.

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

System identity must be sufficiently stable to support provenance, auditability, integration management, and historical reconstruction.

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
operational accountability

Ownership does not itself establish authority over every fact or capability exposed by the system.

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

The boundary includes technical access, data access, capability exposure, authorization requirements, and supported interaction semantics.

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

A Resource may have representations in multiple systems.

Managing a representation does not necessarily mean the system is authoritative for the logical resource.

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

Capability existence does not establish that every principal is authorized to invoke it.

⸻

19. System Actions

Noema’s Actions invoke enterprise Capabilities through explicit Action Contracts.

Intent
   ↓
Action
   ↓
Action Contract
   ↓
Capability
   ↓
Integration
   ↓
System

Example:

Action:
refund_payment
Capability:
refund_payment
System:
Payment System

The Action Contract defines the bounded semantic execution interface. A model must not invent an Action or derive executable semantics directly from an arbitrary System API.

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

A Noema observation of system state is not automatically equivalent to current enterprise truth. The observation must be evaluated according to authority, freshness, scope, and reconciliation requirements.

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

Events can provide observations, evidence, Context, or execution triggers.

An event must pass through the applicable validation and admission boundary before being used as structured Noema input.

An event trigger does not grant authority or bypass Trust.

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

Dependencies may affect:

preconditions
execution ordering
availability
verification
recovery
compensation
reconciliation

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
  ├── authoritative_for → Fact
  │
  └── accessed_by → Integration

The graph allows Noema to reason about enterprise execution paths.

Graph relationships are structured enterprise knowledge. They must not automatically be treated as authoritative Business State merely because they are represented in the graph.

⸻

24. System Relationships

Important relationships include:

owns
manages
exposes
depends_on
integrates_with
accessed_by
emits
consumes
authoritative_for
derived_from
governed_by
belongs_to

These relationships should remain explicit rather than inferred from arbitrary API behavior.

Where a relationship affects consequential execution, its provenance, scope, version, and effective period should be preserved where applicable.

⸻

25. System Authority

Authority should be represented at the level of facts, claims, resources, or defined domains.

Example:

Ledger
→ authoritative_for
→ Account Balance

while:

Analytics Warehouse
→ derived_from
→ Ledger

This allows Noema to distinguish authority from accessibility.

Authority should be scoped by the relevant claim, resource, tenant, organization, environment, and time where necessary.

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

Conflicting representations should be reconciled according to explicit authority semantics rather than model preference.

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

Mappings are integration knowledge and require provenance and appropriate validation. An inferred mapping must not silently become authoritative identity.

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

Environment is therefore part of execution scope and must be preserved through capability and integration resolution.

⸻

29. System Version

Systems evolve.

A system representation may therefore include:

API version
schema version
capability version
deployment version

This is particularly important for Action Contracts, Events, verification, and historical audit.

Transport or deployment version changes must not automatically be treated as semantic changes. Material semantic changes must be represented explicitly.

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
verification semantics

Noema should treat material capability changes as contract-relevant changes.

An execution should be bound to the applicable Action Contract and capability version rather than relying on whichever implementation happens to be current.

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

System health must therefore not be used as a proxy for Business State or Outcome.

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

Transport failure is an execution condition. It is not by itself a Business Outcome.

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

Noema may need to reconcile against the appropriate System of Record.

UNKNOWN is a first-class execution and epistemic state. Noema must not guess success or failure merely to complete a workflow.

⸻

35. System Consistency Model

Systems may provide different consistency guarantees:

strong consistency
eventual consistency
read-after-write consistency
session consistency

Noema should understand the relevant guarantees when verifying Preconditions and Postconditions.

Consistency semantics affect whether an observation is sufficient to establish a current claim or whether additional State Reconciliation is required.

⸻

36. System Transactions

A system may support:

atomic transactions
conditional writes
optimistic locking
pessimistic locking
idempotency
reservations
leases

Noema should use these capabilities where available rather than recreating transactional semantics externally.

Enterprise systems remain responsible for the correctness of their Business State transitions.

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

Compound execution must therefore preserve individual Action Contracts, authorization, execution identity, verification, and recovery semantics for each consequential Action.

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

The Planner remains bounded by the Enterprise Action Graph, Capability Registry, Action Contracts, Trust Decision, and current execution constraints. It cannot invent capabilities or authority from graph relationships.

⸻

39. System Dependency Failure

If:

Payment System

is unavailable, Noema may be unable to safely execute:

close_account

if the account closure requires the payment state to be verified.

Planning should therefore consider dependency availability, state freshness, and verification requirements.

Unavailable dependencies may produce UNKNOWN, CLARIFY, ESCALATE, or REJECT depending on the relevant execution and Trust semantics. Noema must not invent a successful path around a required unavailable dependency.

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
consistency model
integration status

For example:

Production Ledger

is stronger evidence for account balance than:

Analytics Replica

Trust evaluates these inputs together with resolved Intent, Context, Policy, Permissions, Preconditions, Risk, and other applicable constraints.

⸻

41. System as Evidence Source

A system response should carry provenance where consequential.

Conceptually:

Evidence {
    system
    integration
    capability
    resource
    value
    observed_at
    version
}

Evidence is not itself equivalent to Fact Status.

A system response may support a fact whose status is:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

depending on authority, reconciliation, freshness, consistency, and other applicable semantics.

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

However, Context is not automatically authoritative merely because it contains information originating from a System.

Context must retain sufficient provenance and authority metadata for downstream Trust and State Reconciliation.

⸻

43. System and Data Boundaries

Not every system should expose all of its data to Noema.

A system integration should define:

accessible resources
accessible fields
permitted operations
retention rules
redaction rules
tenant scope
organizational scope
data classification
purpose restrictions

This supports least-privilege access.

Data access is distinct from business authorization and from System-of-Record authority.

⸻

44. System and Permissions

System access does not automatically equal business authorization.

For example:

Noema credential:
can call POST /refund

does not necessarily mean:

principal:
is authorized to refund this payment

Technical access, business authorization, and Noema Trust remain distinct.

The effective business principal must remain attributable even when execution occurs through a Noema service credential.

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

Credentials are security material and must remain outside ordinary model context and untrusted model-generated data.

The model must not receive enterprise credentials or direct unrestricted access to enterprise systems.

⸻

46. System and Delegation

An enterprise may allow:

Human
 ↓
Noema
 ↓
System Credential

The system sees the technical credential, while Noema’s audit model preserves:

initiating principal
delegator
delegate
effective execution principal
delegation scope
authorization context

where applicable.

Delegation must not silently expand authority.

⸻

47. System and Auditability

Every consequential system interaction should be attributable where practical.

An audit record may include:

execution_id
intent_version
action_id
system_id
integration_id
capability
capability_version
principal
resource
request_id
timestamp
result

This establishes the connection between Noema execution and enterprise system behavior.

The audit record should preserve causal relationships without requiring exposure of private model chain-of-thought.

⸻

48. System and Observability

Systems should expose operational signals where appropriate:

latency
availability
error rate
request identifiers
provider status
consistency signals

These signals can improve execution reliability without becoming Business State themselves.

Operational telemetry must not be silently promoted to authoritative enterprise facts.

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

The Action Contract defines the executable semantic boundary; the System provides the underlying enterprise implementation.

⸻

50. System and API Drift

If the system changes its interface:

v1:
refund(payment_id, amount)
v2:
refund(payment_id, amount, currency)

Noema should detect the contract mismatch.

It should not allow a model to improvise the missing parameter.

Schema and contract validation must reject or quarantine incompatible operations before consequential execution.

⸻

51. System and Policy Drift

A system’s policy requirements may change.

Example:

Previously:

refunds < $1,000

becomes:

refunds < $500

Noema must treat this as a meaningful authorization or policy change rather than assuming previous execution behavior remains valid.

Previously valid Trust or execution decisions must not silently acquire new meaning because the current policy changed.

⸻

52. System and Schema Drift

Schema changes can affect:

resource identity
resource state
capability inputs
capability outputs
postconditions
event semantics

Schema validation therefore forms part of the enterprise integration boundary.

Unvalidated or incompatible system data must not become authoritative Noema Context, Evidence, or execution input merely because it was successfully retrieved.

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
├── policies
├── dependencies
└── lifecycle

This metadata can feed the Enterprise Action Graph.

Registration is descriptive and does not itself grant execution authority.

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

Discovered information must pass through applicable validation and admission processes before becoming canonical Noema enterprise knowledge.

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
integration integrity
current availability

System existence or registration cannot bypass deterministic Trust.

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

This matters for authority, data boundaries, credentials, failure semantics, contractual dependencies, and verification.

⸻

57. External Provider vs Enterprise System of Record

An external provider may process an operation while the enterprise remains authoritative for its own Business State.

Example:

Payment Provider
→ processes payment
Enterprise Ledger
→ records financial state

The provider response is important evidence but does not automatically become the enterprise’s canonical ledger state.

Where external provider state conflicts with enterprise state, the relevant authority relationship must be explicit.

⸻

58. System Boundaries and Legal Entities

Systems may serve multiple legal entities.

Example:

ERP
├── Nigeria Ltd.
├── UK Ltd.
└── US Inc.

Noema must preserve organizational and legal-entity boundaries when resolving Resources, Permissions, Capabilities, and Actions.

A system serving multiple entities does not imply that authority is shared across those entities.

⸻

59. System Isolation

Noema must prevent accidental cross-system or cross-tenant execution.

For example:

Tenant A
→ Payment System A
Tenant B
→ Payment System B

A resource identifier alone must not be sufficient to cross the boundary.

Resolution should preserve tenant, organization, environment, system, and resource identity where those dimensions are consequential.

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

systems unless explicitly supported by enterprise policy and the relevant integration/capability remains valid.

Lifecycle state is not itself a Trust outcome.

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
effective dates

This prevents execution against the wrong system during transitions.

Historical executions must remain interpretable according to the system and authority relationships that applied at the time.

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

Only the enterprise capability, Action Contract, integration, graph, and system layers should need substantial change where the semantic Action remains equivalent.

This is an important abstraction boundary.

⸻

63. System Abstraction

Noema should reason primarily in terms of:

Intent
Action
Capability
Resource
Policy
System
Integration

rather than:

HTTP endpoint
database table
vendor SDK

The System and Integration layers translate those concepts into implementation-specific operations.

The abstraction must be deep enough to preserve semantic independence while remaining precise enough to execute safely.

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

Systems are therefore not merely integration endpoints. They are part of Noema’s model of how enterprise capabilities, resources, authority, and state are organized.

⸻

65. Hard Schema Validation and System Data

System data entering Noema is not automatically trusted because it originated from an enterprise system.

The canonical boundary is:

Enterprise System
        ↓
Observation / Response / Event
        ↓
Hard Schema Validation / Admission
        ↓
Semantic Validation / Classification
        ↓
Context / Evidence / State Reconciliation
        ↓
Trust / Execution

Hard schema validation establishes structural admissibility.

It does not by itself establish:

authority
freshness
Fact Status
business truth
authorization

A successfully parsed response can still be stale, conflicted, unauthorized for the intended purpose, or otherwise insufficient.

⸻

66. State Reconciliation Across Systems

Enterprise state may be distributed across multiple systems.

Noema therefore treats State Reconciliation as a first-class platform capability rather than merely an integration concern.

Enterprise Systems
        ↓
Observations
        ↓
Hard Schema Validation / Admission
        ↓
State Reconciliation
        ↓
Reconciled Facts
        ↓
Fact Status / Evidence
        ↓
Context / Trust

Reconciliation may account for:

multiple sources
eventual consistency
event ordering
missing observations
resource versions
timestamps
source authority
conflicting claims
cross-system relationships

Noema must not resolve conflicting state through model preference.

⸻

67. Fact Status and System Observations

System observations contribute evidence toward enterprise claims.

Fact Status remains distinct from:

System
Evidence
Context
Business State
Outcome
Model confidence

Canonical Fact Status values are:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Ledger response
    ↓
Evidence
State Reconciliation
    ↓
balance = $5,000
Fact Status = VERIFIED

A system response may therefore be useful evidence without independently establishing a verified fact.

⸻

68. System Authority, Freshness, and Knowledge State

Three questions must remain distinct:

Who is authoritative?
How fresh is the observation?
What does Noema currently know?

A highly recent response from a non-authoritative system does not necessarily establish enterprise truth.

Conversely, an authoritative system may be temporarily unavailable, leaving Noema with:

Knowledge State = UNKNOWN

even though the enterprise itself has a definite Business State.

Recency does not equal authority.

⸻

69. Systems and Source of Intent

Systems may participate in the creation or transmission of Intent.

Possible Sources of Intent include:

human
agent
system
workflow
API/application
enterprise event
scheduled process
other explicitly supported enterprise source

A system-generated request must still pass through Noema’s Intent schema validation and Trust lifecycle.

An enterprise event occurring does not automatically mean that the event constitutes an authorized Intent.

The source of an Intent must remain attributable.

⸻

70. Systems and Intent Versioning

Consequential execution must preserve the exact Intent Object version under which the Action was evaluated.

An admitted Intent is immutable once admitted to Trust.

If resolution or clarification materially changes the Intent:

Intent v1
    ↓
clarification
    ↓
Intent v2
    └── supersedes → Intent v1

The System interaction, Trust Decision, Action Contract, execution, and verification records must reference the applicable Intent version.

System responses must not silently mutate the semantic Intent.

⸻

71. Systems and Bounded Planning

The Planner may use System information to construct an execution path, but System metadata alone does not grant permission to act.

Planning is bounded by:

Enterprise Action Graph
Capability Registry
Action Contracts
Trust Decision
resolved actor
resolved target
current enterprise state
applicable policy
execution constraints

The Planner must not:

invent capabilities
invent authority
create Action Contracts
expand permissions
bypass Trust
select arbitrary endpoints
turn arbitrary system APIs into executable capabilities

A System being discoverable does not make every operation executable.

⸻

72. Systems and State Reconciliation After Unknown Execution

When an execution interaction produces an ambiguous result:

Action
   ↓
System
   ↓
timeout
   ↓
Execution = UNKNOWN

Noema should not blindly retry.

The recovery path may be:

Historical Execution State
        ↓
External Operation State
        ↓
Current Authoritative Observation
        ↓
State Reconciliation
        ↓
Fact Status
        ↓
Revalidate Preconditions / Trust
        ↓
Continue / Clarify / Escalate / Reject

A reconciliation result establishes current knowledge. It does not rewrite the historical execution attempt.

⸻

73. Systems and Outcome

A System response is not automatically an Outcome.

For example:

HTTP 200

does not necessarily mean:

Business Outcome = SUCCESS

Similarly:

HTTP timeout

does not necessarily mean:

Business Outcome = FAILURE

Outcome must be established according to the Action Contract’s verification semantics and relevant authoritative enterprise state.

Noema’s Outcome record is an execution-domain record describing what Noema established about the Action. It does not replace enterprise Business State.

⸻

74. Systems and Replay

Replaying a System event, observation, or historical response must not automatically cause a new business execution.

By default:

Replay
→ reconstruction / analysis
→ non-executing

Historical System interactions should preserve their original identity, timestamp, version, provenance, and relationship to the original Intent and execution.

Modern reevaluation must be distinguishable from historical reconstruction.

⸻

75. Systems and Operational Memory

Noema may retain structured operational history about System interactions, including:

system failures
integration failures
latency
schema drift
capability changes
reconciliation outcomes
execution attempts
recovery patterns

This information belongs to Noema’s Operational Memory.

Operational Memory is not a replacement for the System of Record and must not become an alternative source of current enterprise Business State.

⸻

76. Mode 1 and Mode 2

Systems participate in both Noema operating modes.

Mode 1: Full-Stack Execution

Source of Intent
      ↓
Noema
      ↓
Trust
      ↓
Action
      ↓
Integration
      ↓
Enterprise System

Noema manages the complete execution journey.

Mode 2: Independent Trust Boundary

Human / Agent / Existing Orchestrator
              ↓
        Noema Trust Boundary
              ↓
       Action Contract
              ↓
       Enterprise System

In Mode 2, an existing enterprise agent or orchestrator may manage interaction and planning while Noema provides an independent deterministic trust and execution boundary.

The underlying enterprise Systems remain external authorities for their Business State in both modes.

⸻

77. Canonical System Model

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
    provenance
}

Not every implementation must expose every field.

The model defines semantic concepts, not necessarily a literal database schema.

Authority, capabilities, and relationships should be scoped and versioned where their meaning is consequential.

⸻

78. Canonical Relationships

System
 ├── owns → Resource
 ├── manages → Resource
 ├── exposes → Capability
 ├── accessed_by → Integration
 ├── emits → Event
 ├── consumes → Event
 ├── depends_on → System
 ├── authoritative_for → Fact / Claim / Resource
 ├── derived_from → System
 ├── governed_by → Policy
 └── belongs_to → Organization

These relationships form part of the Enterprise Action Graph.

They describe enterprise structure and execution possibilities but do not independently create authorization or Business State authority.

⸻

79. Canonical Invariants

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

System events are observations or evidence of state transitions and do not automatically establish current Business State.

Invariant 12

Transport failure must not automatically be interpreted as business-operation failure.

Invariant 13

Unknown execution outcomes should be reconciled against the appropriate System of Record where possible.

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

Invariant 26

System data must pass through applicable schema validation and admission boundaries before becoming canonical Noema input.

Invariant 27

Successful schema validation does not by itself establish authority, freshness, or Fact Status.

Invariant 28

State Reconciliation is a first-class capability for resolving relevant distributed enterprise state.

Invariant 29

Fact Status is distinct from Evidence, Context, System, Business State, Outcome, and model confidence.

Invariant 30

Canonical authority is scoped to the relevant fact, claim, resource, domain, tenant, organization, environment, and time where applicable.

Invariant 31

Accessibility does not imply authority.

Invariant 32

System registration does not imply execution authorization.

Invariant 33

A model must not convert arbitrary System APIs, documentation, or responses into executable capabilities.

Invariant 34

Planner decisions must remain bounded by the Enterprise Action Graph, Capability Registry, Action Contracts, Trust Decision, and resolved execution context.

Invariant 35

The model must not receive enterprise credentials or directly control enterprise Systems.

Invariant 36

A system response is not automatically an Outcome.

Invariant 37

Noema’s Outcome record does not replace authoritative enterprise Business State.

Invariant 38

Unknown state must remain explicit and must not be resolved through model preference or unsupported inference.

Invariant 39

Unknown execution results must be reconciled before blind retry of potentially consequential operations.

Invariant 40

Historical System interactions must remain distinguishable from current reevaluation and replay.

Invariant 41

Admitted Intent versions are immutable; consequential System interactions must reference the exact applicable Intent version.

Invariant 42

Resolved actor, target Resource, scope, Action, System, Integration, and Capability identity must be preserved for consequential execution.

Invariant 43

Technical authorization to access a System is distinct from business authorization to perform an Action.

Invariant 44

System relationships represented in the Enterprise Action Graph do not independently create authority.

Invariant 45

Noema must not maintain a shadow authoritative representation of enterprise Business State.

Invariant 46

Enterprise transaction, concurrency, and consistency semantics should be used rather than recreated in Noema.

Invariant 47

Read-only System interactions may still be consequential when they expose protected data or establish facts required for execution.

Invariant 48

System authority and freshness must be evaluated separately; recency does not establish authority.

Invariant 49

System-generated events or requests do not automatically constitute authorized Intent.

Invariant 50

Noema owns or canonically manages its execution-domain records, while enterprise Systems remain authoritative for enterprise Business State.

⸻

80. Final Definition

A System is a bounded enterprise component that owns, manages, exposes, transforms, stores, or transports business capabilities, resources, events, or state.

Noema models Systems as part of the Enterprise Action Graph so it can determine:

where Resources live,
which Capabilities are available,
where authoritative state resides,
which Integrations provide access,
what dependencies and constraints apply,
how enterprise state can be reconciled,
and how Actions can safely cross enterprise boundaries.

The canonical architecture is:

                  ENTERPRISE
                       │
                    Systems
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Resources     Capabilities     Events
        │              │              │
        └──────────────┼──────────────┘
                       │
                 System Authority
                       │
                       ▼
                    Noema
                       │
             Intent → Trust
                       │
                    Action
                       │
                 Action Contract
                       │
                       ▼
                  Integration
                       │
                       ▼
                    System
                       │
                       ▼
               Business State
                       │
                       ▼
            Verification / Reconciliation

The complete Noema execution boundary is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation / Admission
      ↓
Admitted Intent
      ↓
Context / State Reconciliation
      ↓
Deterministic Trust
      ↓
Enterprise Action Graph / Planner
      ↓
Action Contract
      ↓
Integration
      ↓
Enterprise System
      ↓
Verification
      ↓
Outcome / Audit / Operational Memory

And the essential architectural rule remains:

Noema should understand the enterprise’s Systems deeply enough to execute safely, while abstracting them deeply enough that Noema’s Intent and Action semantics do not become coupled to any particular vendor, API, database, or implementation.

Noema does not need to own enterprise Systems or Business State.

It needs to understand where enterprise truth and executable capability live, establish the relevant state through validation and reconciliation, evaluate deterministic Trust, invoke bounded capabilities, and verify what actually happened.

The enterprise owns its Business State.

Noema owns and canonically manages the execution-domain journey through which Intent becomes a governed, executed, and verified enterprise outcome.