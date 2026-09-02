Resource

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/resource.md

⸻

1. Definition

A Resource is an Entity, asset, capability-bearing object, information object, service, or finite capacity that can be accessed, consumed, allocated, modified, transferred, reserved, or otherwise acted upon by an Intent or Action.

A Resource answers:

What thing, asset, information, service, or capacity is available to be used or affected?

Examples include:

Account
Payment Card
Customer Record
Database Connection
Cloud Storage
Compute Capacity
Inventory
Money
API Quota
Employee Time
Document
Subscription
Vehicle
Physical Asset

⸻

2. Resource Is a Semantic Role

Not every Entity is inherently a Resource.

An Entity becomes relevant as a Resource when it participates in an operational relationship involving use, allocation, access, consumption, modification, or transfer.

For example:

Customer

is an Entity.

But:

Customer Record

may be a Resource when an Action accesses or modifies that record.

Therefore:

Resource ⊂ Entity

is a useful conceptual model, but Resource should not necessarily be implemented as a subclass in every storage model.

⸻

3. Resource vs Entity

This distinction is foundational.

Entity

A distinguishable thing that exists in Noema’s domain.

Resource

A thing that can be operationally used, accessed, consumed, allocated, modified, or otherwise acted upon.

Example:

Entity:
Customer #123
Resource:
Customer's account balance

Another:

Entity:
Warehouse
Resource:
Warehouse inventory

Another:

Entity:
Cloud Platform
Resource:
Available compute capacity

⸻

4. Resource vs Capability

A Capability represents:

What can be done.

A Resource represents:

What can be acted upon or used.

Example:

Capability:
transfer_funds
Resource:
Account #123

The Capability enables the Action.

The Resource is what the Action operates on.

Capability
     │
     ▼
Action ──────► Resource

⸻

5. Resource vs Context

Context describes the circumstances surrounding an Intent or Action.

Resource is something that may be acted upon within that Context.

Example:

Context:
Authenticated customer session
Resource:
Customer account

The session is Context.

The account is the Resource.

⸻

6. Resource vs Constraint

A Constraint limits how a Resource may be used.

Example:

Resource:
Account balance
Constraint:
Withdrawal <= available balance

Another:

Resource:
API quota
Constraint:
Maximum 1,000 requests per hour

⸻

7. Resource vs Policy

A Policy governs how a Resource may be used.

Resource:
Customer data
Policy:
Customer data may only be exported for legitimate business purposes.

Policy defines the governing rule.

Resource is what the rule governs.

⸻

8. Resource vs Authority

Authority determines whether an Actor is permitted to perform operations involving a Resource.

Example:

Actor:
Finance Manager
Authority:
May approve payments for Account A
Resource:
Account A

Authority can therefore be scoped to Resources.

⸻

9. Resource Lifecycle

Resources may have a lifecycle.

A generic lifecycle is:

DEFINED
   ↓
AVAILABLE
   ↓
ALLOCATED
   ↓
IN_USE
   ↓
RELEASED
   ↓
RETIRED

Not every Resource requires every state.

A financial account, for example, may instead use:

PENDING
ACTIVE
SUSPENDED
CLOSED

Resource lifecycle semantics belong to the Resource’s domain.

⸻

10. Resource Identity

A Resource should have a stable identity where it is individually addressable.

Example:

resource:
account:123

or:

resource:
document:invoice:456

Resource identity should be distinct from display names.

⸻

11. Resource Types

Foundational Resource categories include:

Physical Resource
Financial Resource
Information Resource
Digital Resource
Compute Resource
Network Resource
Human Resource
Time Resource
Capacity Resource
Service Resource
Credential Resource
Access Resource

These categories are extensible.

⸻

12. Physical Resources

Physical objects that can be used, allocated, transferred, or operated.

Examples:

Vehicle
Warehouse
Machine
Device
Inventory Item
Office Space
Equipment

Example:

Intent:
Book delivery vehicle.
Resource:
Vehicle #42.

⸻

13. Financial Resources

Resources representing monetary value or financial capacity.

Examples:

Cash
Account Balance
Credit
Payment Limit
Budget
Wallet
Funds

Example:

Intent:
Transfer $5,000.
Resource:
Account balance.

⸻

14. Information Resources

Information that can be accessed, modified, exported, retained, or deleted.

Examples:

Customer Record
Medical Record
Financial Record
Document
Report
Database Record
Transaction History

Information Resources require especially strong Policy and Authority semantics.

⸻

15. Digital Resources

Software-defined objects that can be operated on.

Examples:

File
Repository
API Key
Cloud Object
Database
Container
Deployment
DNS Record

⸻

16. Compute Resources

Computational capacity that can be allocated or consumed.

Examples:

CPU
Memory
GPU
VM
Container
Worker
Compute Instance

Example:

Intent:
Run ML training job.
Resource:
GPU capacity.

⸻

17. Network Resources

Resources representing connectivity or network capacity.

Examples:

Bandwidth
IP Address
Network
Port
VPN
Connection

⸻

18. Human Resources

Humans may be modeled as Entities that participate as Resources when their time, attention, or labor is being allocated.

Example:

Entity:
Engineer
Resource:
Engineer availability

This distinction prevents treating a person as merely an operational asset.

⸻

19. Time as a Resource

Time can be modeled as a Resource where it is explicitly allocated or consumed.

Example:

Resource:
30-minute appointment slot
Intent:
Book appointment
Action:
ReserveSlot

The Resource is the available time allocation, not simply the timestamp.

⸻

20. Capacity as a Resource

Capacity is a particularly important Resource type.

Examples:

API quota
Storage capacity
Inventory capacity
Credit limit
CPU capacity
Queue capacity
Appointment capacity

Capacity Resources are often consumable.

⸻

21. Consumable Resources

A consumable Resource decreases when used.

Examples:

Inventory
Money
API quota
Storage
Credit
Fuel
Compute credits

Conceptually:

Resource
   ↓
Consumption
   ↓
Reduced availability

⸻

22. Non-Consumable Resources

Some Resources can be used without being permanently depleted.

Examples:

Vehicle
Machine
Employee
Database
API service
Physical room

Use may temporarily change availability without destroying the Resource.

⸻

23. Allocatable Resources

An allocatable Resource can be reserved or assigned.

Examples:

Meeting Room
GPU
Employee Time
Vehicle
Inventory
IP Address

Example:

Intent:
Reserve meeting room.
Resource:
Room A.

⸻

24. Exclusive Resources

Some Resources cannot be simultaneously allocated to multiple consumers.

Example:

Resource:
Operating Room #3

Constraint:

Only one active allocation at a time.

The exclusivity itself may be represented as a Constraint.

⸻

25. Shared Resources

Some Resources may support multiple simultaneous consumers.

Examples:

Network
Database
API
Cloud Storage

The Resource may have capacity constraints rather than exclusive ownership.

⸻

26. Resource Availability

Resource availability is contextual and temporal.

Conceptually:

Resource
   +
Context
   +
Time
   ↓
Availability

Example:

Vehicle #42
Available:
09:00–12:00
Unavailable:
12:00–15:00

Availability should not be assumed merely because a Resource exists.

⸻

27. Resource State

A Resource may have state relevant to whether it can be acted upon.

Example:

Account:
ACTIVE
Card:
BLOCKED
Vehicle:
MAINTENANCE
API:
RATE_LIMITED

Resource state can become a Constraint on Actions.

⸻

28. Resource Ownership

A Resource may have an ownership relationship.

Actor ──owns──► Resource

Example:

Customer
  └── owns ──► Account #123

Ownership is not synonymous with Authority.

An owner may not necessarily have unlimited operational authority.

⸻

29. Resource Custody

Custody is distinct from ownership.

Actor ──has_custody_of──► Resource

Example:

Bank
  └── has_custody_of ──► Customer Funds

The Bank may have custody without owning the underlying funds.

⸻

30. Resource Access

An Actor may have access to a Resource.

Actor ──has_access_to──► Resource

Access does not automatically imply permission to perform every operation on that Resource.

Example:

Actor:
Support Agent
Access:
Customer Account
Authority:
Can view account
Authority:
Cannot delete account

⸻

31. Resource Allocation

A Resource may be allocated to an Actor, Intent, or Action.

Resource ──allocated_to──► Actor

or:

Resource ──allocated_to──► Intent

Example:

GPU #4
  └── allocated_to ──► MLTrainingIntent

⸻

32. Resource Reservation

A Resource may be reserved before actual use.

Intent
  └── reserves ──► Resource

Example:

Intent:
Book flight
  └── reserves ──► Seat 14A

Reservation does not necessarily mean consumption.

⸻

33. Resource Consumption

An Action may consume a Resource.

Action ──consumes──► Resource

Example:

TransferFunds
  └── consumes ──► Account Balance

Another:

SendMessage
  └── consumes ──► API Quota

⸻

34. Resource Modification

An Action may modify a Resource.

Action ──modifies──► Resource

Example:

UpdateCustomer
  └── modifies ──► Customer Record

⸻

35. Resource Creation

An Action may create a Resource.

Action ──creates──► Resource

Example:

CreateAccount
  └── creates ──► Account

The newly created Resource becomes part of the canonical domain state.

⸻

36. Resource Destruction

An Action may destroy or permanently remove a Resource.

Action ──destroys──► Resource

Example:

DeleteFile
  └── destroys ──► File

Destructive operations should generally have stronger Policy, Authority, and Trust requirements.

⸻

37. Resource Transfer

A Resource may move between Actors, Accounts, Locations, or other owners/custodians.

Action ──transfers──► Resource

Example:

TransferFunds
  └── transfers ──► Money

The transfer relationship should preserve:

source
destination
quantity
time
authority

where applicable.

⸻

38. Resource Transformation

An Action may transform one Resource into another state or Resource.

Action
   └── transforms ──► Resource

Example:

ConvertCurrency
   └── transforms ──► USD → NGN

Transformation does not necessarily imply destruction.

⸻

39. Resource Dependencies

Resources may depend on other Resources.

Resource ──depends_on──► Resource

Example:

Application
  └── depends_on ──► Database

Another:

API Service
  └── depends_on ──► Network

⸻

40. Resource Composition

A Resource may contain or be composed of other Resources.

Resource ──contains──► Resource

Example:

Warehouse
  └── contains ──► Inventory Item

Another:

Cloud Account
  └── contains ──► Compute Instance

⸻

41. Resource Hierarchy

Resources may have parent-child relationships.

Resource ──part_of──► Resource

Example:

GPU
  └── part_of ──► Compute Instance

This is different from simple ownership.

⸻

42. Resource Scope

A Resource may have a scope.

Possible scopes:

Actor
Organization
Department
Project
Environment
Region
Account
Tenant
System

Example:

Resource:
API Quota
Scope:
Organization = Acme

⸻

43. Resource Governance

Resources may be governed by Policies.

Resource ──governed_by──► Policy

Example:

CustomerData
  └── governed_by ──► DataExportPolicy

This is complementary to:

Action ──governed_by──► Policy

A Policy can govern both the Resource and the operation performed against it.

⸻

44. Resource Constraints

Resources may have Constraints.

Resource ──constrained_by──► Constraint

Example:

Account
  └── constrained_by ──► DailyWithdrawalLimit

This represents an inherent or externally imposed limit on Resource use.

⸻

45. Resource Authority

Authority may be scoped to a Resource.

Authority ──scoped_to──► Resource

Example:

AccountManagerAuthority
  └── scoped_to ──► Account #123

This allows Noema to distinguish:

Can approve refunds

from:

Can approve refunds for this account.

⸻

46. Resource Capability

Capabilities may operate on particular Resource types.

Capability ──operates_on──► Resource

Example:

Capability:
delete.customer
  └── operates_on ──► Customer Record

The Capability describes the operation.

The Resource describes the target.

⸻

47. Resource and Intent

An Intent may target or concern a Resource.

Intent ──targets──► Resource

Example:

Intent:
Delete my account
  └── targets ──► Account #123

targets should be used when the Resource is the direct object of the requested operation.

concerns is broader.

⸻

48. Resource and Action

An Action may:

access
read
write
modify
create
destroy
consume
allocate
reserve
release
transfer
transform

a Resource.

These relationships should be explicit where the distinction matters.

⸻

49. Resource Access Semantics

Access should not be treated as a binary concept.

Possible access modes include:

READ
WRITE
EXECUTE
ADMINISTER
ALLOCATE
TRANSFER
DELETE

Example:

Actor:
Support Agent
Resource:
Customer Record
Access:
READ
Authority:
May read
Authority:
May not delete

⸻

50. Resource Quantity

Some Resources are quantifiable.

Examples:

Money
Inventory
Storage
Bandwidth
CPU
Fuel
Credit

A quantity should have:

value
unit

Example:

500
USD

or:

20
GB

⸻

51. Resource Availability vs Quantity

These are distinct.

Resource Quantity:
100 units
Available Quantity:
40 units

The remainder may already be:

* allocated
* reserved
* consumed
* unavailable

Noema should not equate total quantity with available quantity.

⸻

52. Resource Reservation

Reservations create a temporal claim over a Resource.

Reservation
├── resource
├── claimant
├── quantity
├── valid_from
└── valid_until

Example:

Room A
Reserved:
10:00–11:00

The Resource remains in existence.

Its availability changes.

⸻

53. Resource Allocation vs Reservation

These concepts should remain distinct.

Reservation

A future or conditional claim on a Resource.

Allocation

The Resource has been assigned for use.

Example:

Reservation
    ↓
Approval
    ↓
Allocation
    ↓
Use

Not every domain requires all stages.

⸻

54. Resource Consumption vs Destruction

Consumption does not necessarily destroy a Resource.

Example:

Consume:
$100 from $1,000 balance

The Account still exists.

Destruction:

Delete Account

removes or retires the Resource itself.

⸻

55. Resource State Transitions

Actions may cause Resource state transitions.

Example:

Account
ACTIVE
  │
  │ SuspendAccount
  ▼
SUSPENDED

Another:

Card
ACTIVE
  │
  │ ReplaceCard
  ▼
REPLACED

State transitions should be represented as Outcomes rather than hidden side effects.

⸻

56. Resource and Outcome

Outcomes describe what happened to Resources.

Outcome ──affects──► Resource

Example:

Outcome:
PaymentCompleted
  └── affects ──► Account Balance

This relationship closes the loop between execution and domain state.

⸻

57. Resource Provenance

Resources may have provenance.

Example:

Resource:
Customer Account
Provenance:
Created by AccountCreationAction

This can establish lineage.

Action
  ↓
creates
  ↓
Resource

⸻

58. Resource Lineage

Resources may have historical lineage.

Resource B
  └── derived_from ──► Resource A

Example:

ReplacementCard
  └── derived_from ──► OriginalCard

This is important for auditability.

⸻

59. Resource Versioning

Information and digital Resources may be versioned.

Example:

Document v1
Document v2
Document v3

The Resource identity and Resource version should be distinguishable.

Historical Actions should reference the version they actually affected where necessary.

⸻

60. Resource Availability and Trust

A Resource’s availability can become a Trust input.

Example:

Intent:
Book Room A
Resource:
Room A
Availability:
UNAVAILABLE

Trust should not permit the Action simply because:

Capability:
book.room

exists.

Capability establishes possibility.

Resource state establishes whether the target can currently support the Action.

⸻

61. Resource Conflict

Two Intents may compete for the same Resource.

Example:

Intent A:
Reserve GPU #1
Intent B:
Reserve GPU #1

Noema must identify the Resource conflict.

Resolution may depend on:

* Policy
* Priority
* Reservation time
* Authority
* Actor
* Business rules

The Model must not arbitrarily choose.

⸻

62. Resource Locking

Some execution systems may temporarily lock Resources.

Conceptually:

Resource
   ↓
Lock
   ↓
Action Execution
   ↓
Release

Locking is an execution mechanism, not an ontology requirement.

The ontology should represent the semantic effects of allocation or reservation rather than implementation-specific locking primitives.

⸻

63. Resource Contention

Resource contention occurs when multiple Intents require the same constrained Resource.

Intent A ──► Resource X
Intent B ──► Resource X
Intent C ──► Resource X

Noema may need deterministic arbitration.

This belongs at the intersection of:

Resource
+
Constraint
+
Policy
+
Priority
+
Trust

⸻

64. Resource Priority

Some Resources may have priority rules governing allocation.

Example:

Emergency request
    >
Normal request

Priority is not an inherent property of every Resource.

Where it matters, it should be represented explicitly in Context, Policy, or the relevant Intent/Allocation model.

⸻

65. Resource as a Target

A Resource becomes operationally relevant when an Intent or Action targets it.

Intent
  ↓
targets
  ↓
Resource

This is one of the most important relationships in executable intent.

Without a resolvable target, Noema may know what the Actor wants but not what the request applies to.

⸻

66. Resource Resolution

The Model may help identify a candidate Resource from natural language.

Example:

“Transfer $500 from my savings account.”

Model interpretation:

candidate resource:
Savings Account

Noema must then resolve this against authoritative Entity/Resource data.

Natural Language
      ↓
Candidate Resource
      ↓
Resource Resolution
      ↓
Canonical Resource

The Model’s candidate must not automatically become the authoritative Resource.

⸻

67. Ambiguous Resource Resolution

Example:

“Transfer money from my account.”

If the Actor has:

Savings Account
Current Account
Dollar Account

Noema must not guess.

The system enters a clarification state.

Resource Resolution
      ↓
Multiple valid candidates
      ↓
Ambiguity
      ↓
Clarification

This is directly aligned with Noema’s deterministic Trust boundary.

⸻

68. Resource Identity and Ambiguity

Natural-language references may be ambiguous:

"my card"
"my account"
"the server"
"that document"
"the Lagos office"

Noema should resolve these to canonical Resource identities using Context and authoritative evidence.

If confidence is insufficient:

UNKNOWN

rather than an invented identity.

⸻

69. Resource Ownership Does Not Imply Unlimited Authority

This is a critical invariant.

Owner
   ≠
Unlimited Actor Authority

Example:

Customer owns Account.
Policy:
Account cannot be closed while legal proceedings are active.

Ownership establishes a relationship.

Policy and Authority determine what operations may occur.

⸻

70. Resource Access Does Not Imply Modification Authority

Likewise:

READ access
   ≠
WRITE authority

Example:

Support Agent
  └── can read ──► Customer Record
Support Agent
  └── cannot modify ──► Customer Record

⸻

71. Resource Security Boundary

Resources can represent security boundaries.

Examples:

Database
Account
API Key
Customer Record
Cloud Environment
Repository

Actions against these Resources should be evaluated using:

Actor
+
Authority
+
Policy
+
Context
+
Evidence

⸻

72. Resource and Multi-Tenancy

In a multi-tenant system, Resource scope may include a Tenant.

Resource
  └── scoped_to ──► Tenant

Noema must prevent an Actor’s authority in one Tenant from implicitly extending to another.

⸻

73. Resource and Ownership Transfer

Ownership itself can change.

Example:

Account
Owner A
   │
   │ TransferOwnership
   ▼
Owner B

The transfer should produce an Outcome establishing the new ownership state.

Historical ownership remains part of the domain history.

⸻

74. Resource Deletion

Deleting a Resource does not necessarily mean erasing every historical reference to it.

Example:

Account #123
   ↓
Deleted

Historical records may still reference:

Account #123

for:

* audit
* financial reconciliation
* legal obligations
* Outcome history

Therefore:

Resource deletion
≠
historical relationship deletion

⸻

75. Resource and Auditability

For consequential Resources, Noema should preserve:

Who accessed it?
Why?
Under which Intent?
Which Action?
Under which Authority?
Which Policy?
What happened?

This is one of the major reasons Resources belong explicitly in the ontology.

⸻

76. Resource Model

Conceptually:

Resource
├── id
├── type
├── state
├── owner
├── custodian
├── scope
├── quantity
├── availability
├── lifecycle
├── provenance
└── version

Not every Resource requires every field.

⸻

77. Resource Relationship Model

The foundational Resource graph:

                 Actor
                   │
              owns/accesses
                   │
                   ▼
                Resource
             /     |      \
            /      |       \
     governed_by  constrained_by  depends_on
          │          │              │
          ▼          ▼              ▼
       Policy    Constraint      Resource
          │
          ▼
       Authority
          │
          ▼
      Capability
          │
          ▼
        Action
          │
     ┌────┴────┐
     ▼         ▼
 consumes   modifies
     │         │
     └────┬────┘
          ▼
       Resource

⸻

78. Resource in the Noema Execution Model

The broader flow becomes:

Actor
  │
  ▼
Intent
  │
  ├──────────────► Resource
  │                  │
  │                  ├── Policy
  │                  ├── Constraint
  │                  ├── Authority
  │                  └── Availability
  │
  ▼
Trust
  │
  ▼
Action
  │
  ├── consumes ──► Resource
  ├── modifies ───► Resource
  ├── creates ────► Resource
  ├── destroys ───► Resource
  └── transfers ──► Resource
  │
  ▼
Outcome
  │
  └── affects ────► Resource

⸻

79. Canonical Resource Invariants

The following should be foundational:

1. A Resource is something that can be operationally acted upon, used, allocated, accessed, consumed, modified, transferred, or governed.
2. Resource is distinct from Capability.
3. Resource is distinct from Policy.
4. Resource is distinct from Constraint.
5. Resource is distinct from Context.
6. A Resource is generally an Entity occupying an operational role.
7. Capability describes what can be done; Resource describes what can be acted upon.
8. Existence of a Resource does not imply availability.
9. Availability is contextual and potentially temporal.
10. Ownership does not imply unlimited Authority.
11. Access does not imply modification Authority.
12. Resource identity must be resolved against authoritative data where consequential.
13. Ambiguous Resource references must not be silently resolved by guessing.
14. Resource state can constrain Action execution.
15. Resource consumption is distinct from Resource destruction.
16. Resource reservation is distinct from Resource allocation.
17. Resource creation and destruction should be represented through Actions and Outcomes.
18. Historical Resource relationships must remain auditable.
19. Resource governance must be explicit through Policy and Authority relationships.
20. Consequential Resource operations must pass through Noema’s Trust boundary.

⸻

80. Canonical Principle

A Resource is the operational object or capacity against which an Intent or Action has consequence.

The critical distinction is:

Intent
  = What is wanted
Action
  = What is done
Capability
  = What can be done
Resource
  = What is acted upon
Constraint
  = What limits the operation
Policy
  = What governs the operation
Authority
  = Who is permitted to perform it
Context
  = The circumstances in which it occurs
Trust
  = Whether Noema permits the operation
Outcome
  = What actually happened

That gives us a much cleaner semantic chain:

Actor
   │
   ▼
Intent ──────────────► Resource
   │                       │
   ├── Policy ─────────────┤
   ├── Constraint ─────────┤
   ├── Context ────────────┤
   └── Authority ──────────┘
               │
               ▼
             Trust
               │
               ▼
             Action
               │
               ▼
           Execution
               │
               ▼
            Outcome
               │
               ▼
            Resource

This is particularly important for the broader Noema idea: intent cannot become executable merely because the model understood the user’s words. It has to resolve the actual Resource those words refer to, establish the relationships around that Resource, and then cross the deterministic Trust boundary.