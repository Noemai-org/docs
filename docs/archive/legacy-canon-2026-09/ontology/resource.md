Resource

Status: Foundational
Version: 0.2
Domain: Ontology
Canonical Path: ontology/resource.md

⸻

1. Definition

A Resource is an Entity, asset, information object, service, or finite capacity that can be accessed, used, allocated, reserved, consumed, modified, transferred, created, destroyed, or otherwise acted upon by an Intent or Action.

A Resource answers:

What thing, asset, information, service, or capacity is available to be acted upon?

Examples include:

* Account
* Payment Card
* Customer Record
* Document
* Database
* Cloud Storage
* Compute Capacity
* Inventory
* Money
* API Quota
* Employee Time
* Subscription
* Vehicle
* Physical Asset

A Resource is therefore an operational role in the ontology, not merely a category of things.

⸻

2. Resource as a Semantic Role

Not every Entity is inherently a Resource.

An Entity becomes relevant as a Resource when it participates in an operational relationship involving access, use, allocation, reservation, consumption, modification, transfer, or another consequential operation.

For example:

Entity:
Customer

may become operationally relevant as:

Resource:
Customer Record

when an Action reads or modifies that record.

Conceptually:

Resource ⊂ Entity

may be useful, but Resource should not be assumed to require inheritance or subclassing in an implementation.

The distinction is semantic:

Entity
  = a distinguishable thing in the domain
Resource
  = an Entity or operational object/capacity against which an operation has consequence

⸻

3. Resource and Entity

Entity establishes what exists or is distinguishable in the domain.

Resource establishes what can be operationally acted upon, used, allocated, consumed, accessed, modified, or governed.

Example:

Entity:
Warehouse
Resource:
Inventory held by the Warehouse

Another:

Entity:
Cloud Platform
Resource:
Available compute capacity

The same Entity may participate in different semantic roles depending on the relationship in which it is involved.

⸻

4. Resource and Intent

An Intent expresses what an Actor wants to accomplish.

A Resource identifies what the Intent concerns or targets operationally.

Intent ──targets──► Resource

Example:

Intent:
Delete my account
        │
        ▼
Account #123

targets should be used when the Resource is the direct operational object of the requested operation.

concerns is broader and may apply when the relationship does not establish the Resource as the direct target.

The distinction is:

Intent
  = desired objective
Resource
  = operational object or capacity relevant to that objective

⸻

5. Resource and Action

An Action describes what Noema proposes or performs in order to fulfill an Intent.

A Resource describes what that Action operates upon.

An Action may:

* access a Resource
* read a Resource
* write a Resource
* modify a Resource
* create a Resource
* destroy a Resource
* consume a Resource
* allocate a Resource
* reserve a Resource
* release a Resource
* transfer a Resource
* transform a Resource

The relevant relationship should be represented explicitly where the distinction matters.

⸻

6. Resource and Capability

A Capability describes what can be done.

A Resource describes what can be acted upon.

Capability
     │
     ▼
  Action ──────► Resource

Example:

Capability:
transfer_funds
Resource:
Account #123

The existence of a Capability does not establish that a particular Resource can currently be operated upon.

Therefore:

Capability ≠ Resource

and:

Capability
  = operational possibility
Resource
  = operational object or capacity

⸻

7. Resource and Context

Context describes the circumstances within which an Intent or Action is interpreted or evaluated.

A Resource is an object or capacity relevant within that Context.

Example:

Context:
Authenticated customer session
Resource:
Customer Account

Context does not become a Resource merely because it references one.

⸻

8. Resource and Constraint

A Constraint limits how a Resource may be used or operated upon.

Example:

Resource:
Account Balance
Constraint:
Withdrawal <= available balance

Another:

Resource:
API Quota
Constraint:
Maximum 1,000 requests per hour

A Constraint may apply directly to a Resource, an Intent, an Action, or a combination of these.

⸻

9. Resource and Policy

A Policy establishes governing rules relevant to a Resource or operations involving that Resource.

Example:

Resource:
Customer Data
Policy:
Customer data may only be exported under specified conditions.

A Policy may therefore govern:

Resource
Action
Intent

These are distinct relationships and should not be collapsed.

⸻

10. Resource and Authority

Authority may be scoped to a Resource.

For example:

Authority
  └── scoped_to ──► Account #123

This establishes the resource scope relevant to an Authority.

Resource ownership, access, and Authority are distinct concepts.

Ownership ≠ Access ≠ Authority

An Actor may own a Resource without possessing unlimited Authority over every operation involving it.

⸻

11. Resource Categories

Foundational Resource categories include:

* Physical Resource
* Financial Resource
* Information Resource
* Digital Resource
* Compute Resource
* Network Resource
* Human Resource
* Time Resource
* Capacity Resource
* Service Resource
* Credential Resource
* Access Resource

These categories are extensible.

They describe useful semantic classes and do not require a fixed implementation hierarchy.

⸻

12. Physical Resources

Physical objects that can be used, allocated, transferred, reserved, modified, or operated upon.

Examples:

* Vehicle
* Warehouse
* Machine
* Device
* Inventory Item
* Office Space
* Equipment

Example:

Intent:
Book delivery vehicle
Resource:
Vehicle #42

⸻

13. Financial Resources

Resources representing monetary value or financial capacity.

Examples:

* Cash
* Account Balance
* Credit
* Payment Limit
* Budget
* Wallet
* Funds

Example:

Intent:
Transfer $5,000
Resource:
Account balance

⸻

14. Information Resources

Information that can be accessed, read, modified, exported, retained, or deleted.

Examples:

* Customer Record
* Medical Record
* Financial Record
* Document
* Report
* Database Record
* Transaction History

Information Resources may require particularly strong Policy, Authority, Context, and Evidence relationships.

⸻

15. Digital Resources

Software-defined objects that can be operated upon.

Examples:

* File
* Repository
* API Key
* Cloud Object
* Database
* Container
* Deployment
* DNS Record

⸻

16. Compute Resources

Computational resources or capacity that can be allocated or consumed.

Examples:

* CPU
* Memory
* GPU
* VM
* Container
* Worker
* Compute Instance

Example:

Intent:
Run ML training job
Resource:
GPU capacity

⸻

17. Network Resources

Resources representing connectivity, network infrastructure, or network capacity.

Examples:

* Bandwidth
* IP Address
* Network
* Port
* VPN
* Connection

⸻

18. Human Resources

A human is an Entity.

The person’s time, availability, attention, or labor may participate as a Resource when it is explicitly allocated or consumed.

Example:

Entity:
Engineer
Resource:
Engineer availability

This distinction prevents treating a person as merely an operational asset.

⸻

19. Time Resources

Time can be modeled as a Resource when a specific interval or allocation is operationally relevant.

Example:

Resource:
30-minute appointment slot
Intent:
Book appointment
Action:
ReserveSlot

The Resource is the available time allocation, not merely the timestamp at which an event occurs.

⸻

20. Capacity Resources

Capacity is an important Resource form.

Examples:

* API quota
* Storage capacity
* Inventory capacity
* Credit limit
* CPU capacity
* Queue capacity
* Appointment capacity

Capacity Resources may be consumable, allocatable, reservable, or shared.

⸻

21. Consumable Resources

A consumable Resource decreases in available quantity when consumed.

Examples:

* Inventory
* Money
* API quota
* Storage
* Credit
* Fuel
* Compute credits

Conceptually:

Resource
   │
   ▼
Consumption
   │
   ▼
Reduced availability

Consumption does not necessarily destroy the Resource itself.

⸻

22. Non-Consumable Resources

A Resource may be used without being permanently depleted.

Examples:

* Vehicle
* Machine
* Employee availability
* Database
* API service
* Physical room

Use may temporarily alter availability without destroying the Resource.

⸻

23. Allocatable Resources

An allocatable Resource can be reserved, assigned, or allocated for use.

Examples:

* Meeting Room
* GPU
* Employee Time
* Vehicle
* Inventory
* IP Address

Example:

Intent:
Reserve meeting room
Resource:
Room A

⸻

24. Exclusive and Shared Resources

Some Resources are exclusive:

Operating Room #3

and cannot support multiple incompatible allocations simultaneously.

Others are shared:

Database
Network
API
Cloud Storage

and may support multiple simultaneous consumers subject to capacity and other Constraints.

Exclusivity and sharing are semantic properties relevant to Resource availability and allocation; they should not be assumed for every Resource.

⸻

25. Resource Availability

Resource availability is contextual and potentially temporal.

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

The existence of a Resource does not imply that it is currently available.

Availability may depend on:

* current state
* allocation
* reservation
* quantity
* capacity
* time
* Context
* Policy
* other Resource dependencies

⸻

26. Resource State

A Resource may have state relevant to whether an operation can occur.

Examples:

Account:
ACTIVE
Card:
BLOCKED
Vehicle:
MAINTENANCE
API:
RATE_LIMITED

Resource state may therefore become an input to Constraint evaluation and Trust evaluation.

Resource state is not itself an Action or Outcome.

⸻

27. Resource Identity

An individually addressable Resource should have a stable canonical identity.

Examples:

account:123
document:invoice:456

Resource identity should be distinct from:

* display name
* natural-language reference
* temporary model-generated identifier

Where an operation is consequential, a candidate Resource identified from natural language must be resolved against authoritative Resource or Entity data.

⸻

28. Resource Ownership

A Resource may participate in an ownership relationship.

Actor ──owns──► Resource

Example:

Customer
  └── owns ──► Account #123

Ownership does not imply unlimited operational Authority.

Ownership is a domain relationship; the permissions associated with ownership depend on the relevant Policy, Authority, Context, and Constraints.

⸻

29. Resource Custody

Custody is distinct from ownership.

Actor ──has_custody_of──► Resource

Example:

Bank
  └── has_custody_of ──► Customer Funds

Custody does not establish ownership of the underlying Resource.

⸻

30. Resource Access

An Actor may have access to a Resource.

Actor ──has_access_to──► Resource

Access may be differentiated by mode, including:

* READ
* WRITE
* EXECUTE
* ADMINISTER
* ALLOCATE
* TRANSFER
* DELETE

Access does not automatically establish Authority for every operation.

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

31. Resource Allocation

A Resource may be allocated to an Actor, Intent, Action, or other appropriate allocation target.

Conceptually:

Resource ──allocated_to──► Actor

or:

Resource ──allocated_to──► Intent

Example:

GPU #4
  └── allocated_to ──► MLTrainingIntent

Allocation represents an assignment for use.

⸻

32. Resource Reservation

A reservation establishes a temporal or conditional claim over a Resource.

Conceptually:

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

A reservation does not necessarily constitute consumption or active use.

⸻

33. Allocation vs Reservation

These concepts remain distinct.

Reservation

A future or conditional claim over a Resource.

Allocation

The Resource has been assigned for use.

A domain may model a progression such as:

Reservation
     ↓
Approval
     ↓
Allocation
     ↓
Use

but not every Resource requires every stage.

⸻

34. Resource Consumption

An Action may consume a Resource.

Action ──consumes──► Resource

Examples:

TransferFunds
  └── consumes ──► Account Balance
SendMessage
  └── consumes ──► API Quota

Consumption should preserve the relevant quantity and unit where the Resource is quantifiable.

⸻

35. Resource Modification

An Action may modify a Resource.

Action ──modifies──► Resource

Example:

UpdateCustomer
  └── modifies ──► Customer Record

The resulting state change should be represented through the relevant Outcome rather than treated as an unobservable side effect.

⸻

36. Resource Creation

An Action may create a Resource.

Action ──creates──► Resource

Example:

CreateAccount
  └── creates ──► Account

The newly created Resource becomes part of canonical domain state once creation is established by the resulting Outcome and authoritative state.

⸻

37. Resource Destruction

An Action may destroy, delete, or permanently retire a Resource.

Action ──destroys──► Resource

Example:

DeleteFile
  └── destroys ──► File

Destructive operations may require stronger Policy, Authority, Constraint, Evidence, and Trust evaluation.

Destruction of a Resource does not imply destruction of its historical references.

⸻

38. Resource Transfer

An Action may transfer a Resource or a quantity of a Resource between parties, accounts, locations, or other destinations.

Action ──transfers──► Resource

Where applicable, the transfer semantics should preserve:

* source
* destination
* quantity
* unit
* time
* relevant Authority
* relevant provenance

Example:

TransferFunds
  └── transfers ──► Money

⸻

39. Resource Transformation

An Action may transform a Resource into another Resource or state.

Action ──transforms──► Resource

Example:

ConvertCurrency
  └── transforms ──► USD → NGN

Transformation does not necessarily imply destruction of the original Resource.

⸻

40. Resource Dependencies

Resources may depend on other Resources.

Resource ──depends_on──► Resource

Examples:

Application
  └── depends_on ──► Database
API Service
  └── depends_on ──► Network

Dependencies may become relevant to availability and execution resolution.

⸻

41. Resource Composition

A Resource may contain or be composed of other Resources.

Resource ──contains──► Resource

Examples:

Warehouse
  └── contains ──► Inventory Item
Cloud Account
  └── contains ──► Compute Instance

Containment is distinct from ownership and dependency.

⸻

42. Resource Hierarchy

Resources may participate in structural relationships.

Resource ──part_of──► Resource

Example:

GPU
  └── part_of ──► Compute Instance

part_of expresses structural composition rather than ownership.

⸻

43. Resource Scope

A Resource may have an explicit operational scope.

Possible scopes include:

* Actor
* Organization
* Department
* Project
* Environment
* Region
* Account
* Tenant
* System

Example:

Resource:
API Quota
Scope:
Organization = Acme

Scope must not be inferred merely from naming.

⸻

44. Resource Governance

A Resource may be governed by one or more Policies.

Resource ──governed_by──► Policy

Example:

CustomerData
  └── governed_by ──► DataExportPolicy

This is complementary to an Action being governed by Policy.

A Policy may govern:

the Resource
the Intent
the Action

depending on its semantic scope.

⸻

45. Resource Constraints

A Resource may participate in Constraint relationships.

Resource ──constrained_by──► Constraint

Example:

Account
  └── constrained_by ──► DailyWithdrawalLimit

A Constraint may represent an inherent, configured, contextual, or policy-derived limitation.

⸻

46. Resource Authority Scope

Authority may be scoped to a Resource.

Authority ──scoped_to──► Resource

Example:

AccountManagerAuthority
  └── scoped_to ──► Account #123

This allows Noema to distinguish between:

Authority:
May approve refunds

and:

Authority:
May approve refunds for Account #123

The semantics of Authority itself belong to the Authority ontology. Resource defines the resource-scoping relationship.

⸻

47. Resource Capability Scope

A Capability may specify the Resource on which it operates.

Capability ──operates_on──► Resource

Example:

Capability:
delete.customer
  └── operates_on ──► Customer Record

The distinction is:

Capability
  = what operation is possible
Resource
  = what the operation operates upon

⸻

48. Resource and Outcome

An Outcome may affect a Resource.

Outcome ──affects──► Resource

Example:

Outcome:
PaymentCompleted
  └── affects ──► Account Balance

This relationship connects execution results to canonical domain state.

Resource state changes should not be hidden from the semantic model when they are consequential.

⸻

49. Resource Provenance

A Resource may have provenance establishing where it came from or how it entered the canonical domain.

Example:

Resource:
Customer Account
Provenance:
Created by AccountCreationAction

A creation relationship may therefore establish lineage:

Action
  │
  └── creates ──► Resource

Provenance may identify the authoritative source, creating Action, observation, or other origin information relevant to the Resource.

⸻

50. Resource Lineage

A Resource may have historical lineage.

Resource B
  └── derived_from ──► Resource A

Example:

ReplacementCard
  └── derived_from ──► OriginalCard

Lineage is important for auditability and historical reconstruction.

⸻

51. Resource Versioning

Information and digital Resources may be versioned.

Example:

Document v1
Document v2
Document v3

Resource identity and Resource version should remain distinguishable.

Where necessary, historical Actions should identify the Resource version actually affected.

⸻

52. Resource Quantity

Some Resources are quantifiable.

Examples:

* Money
* Inventory
* Storage
* Bandwidth
* CPU
* Fuel
* Credit

A quantity consists conceptually of:

value
unit

Examples:

500 USD
20 GB

Quantity semantics must not be confused with availability.

⸻

53. Quantity vs Availability

Total Resource quantity and currently available quantity are distinct.

Example:

Resource Quantity:
100 units
Available Quantity:
40 units

The remaining quantity may be:

* allocated
* reserved
* consumed
* unavailable
* otherwise constrained

Therefore:

total quantity ≠ available quantity

⸻

54. Resource Availability as a Trust Input

Resource availability may be relevant to Trust evaluation.

Example:

Intent:
Book Room A
Resource:
Room A
Availability:
UNAVAILABLE

The existence of a Capability:

book.room

does not establish that the requested operation can currently succeed.

Conceptually:

Capability
  = possibility of performing an operation
Resource state / availability
  = whether the target can currently support it

⸻

55. Resource Conflict

Multiple Intents may compete for the same Resource.

Example:

Intent A ──► Resource X
Intent B ──► Resource X
Intent C ──► Resource X

Noema must represent the conflict rather than silently selecting a winner.

Resolution may depend on relevant:

* Policy
* Constraint
* Context
* Authority
* priority
* reservation
* allocation state

The Resource ontology establishes the conflict as a semantic condition; arbitration semantics belong to the applicable governance and resolution mechanisms.

⸻

56. Resource Contention

Resource contention occurs when multiple requests require the same constrained Resource.

Example:

Intent A ──► GPU #1
Intent B ──► GPU #1

Contention may arise from:

* exclusive allocation
* limited capacity
* conflicting reservations
* competing claims
* insufficient quantity

Noema must make the relevant Resource state and competing relationships explicit before consequential execution.

⸻

57. Resource Priority

Priority is not inherently a property of every Resource.

Where allocation or contention requires priority, it should be represented explicitly through the applicable Context, Policy, Intent, Constraint, or allocation model.

Example:

Emergency request
    >
Normal request

The Resource itself does not acquire a universal priority merely because it participates in such a rule.

⸻

58. Resource Resolution

Natural language may identify a candidate Resource.

Example:

"Transfer $500 from my savings account."

The Model may produce:

Candidate Resource:
Savings Account

Noema must then resolve that candidate against canonical Resource or Entity data.

The semantic flow is:

Natural Language
      ↓
Candidate Resource
      ↓
Resource Resolution
      ↓
Canonical Resource

A model-generated candidate must not automatically become an authoritative Resource.

⸻

59. Ambiguous Resource Resolution

Natural-language Resource references may be ambiguous.

Examples:

"my card"
"my account"
"the server"
"that document"
"the Lagos office"

If multiple canonical Resources satisfy the reference:

Resource Resolution
      ↓
Multiple candidates
      ↓
Ambiguity
      ↓
Clarification

Noema must not silently select an arbitrary Resource.

Where a consequential Resource cannot be resolved sufficiently:

UNKNOWN

is preferable to an invented identity.

⸻

60. Resource Resolution and Trust

Resource resolution is part of the semantic grounding required before consequential execution.

A Capability may establish that an operation is possible.

It does not establish:

* which Resource is intended
* that the Resource exists
* that the Resource is available
* that the Actor may operate upon it
* that Policy permits the operation
* that Constraints are satisfied

Therefore:

Intent
   ↓
Resource Resolution
   ↓
Relationship Resolution
   ↓
Trust Evaluation
   ↓
Action

The Model may assist with candidate identification, but authoritative Resource resolution must remain grounded in canonical data.

⸻

61. Resource Ownership Does Not Imply Unlimited Authority

This is a foundational invariant.

Owner
  ≠
Unlimited Authority

Example:

Customer
  └── owns ──► Account

does not establish that the Customer can perform every possible operation against that Account.

For example:

Policy:
Account cannot be closed while legal proceedings are active.

Ownership establishes a relationship.

Policy, Authority, Constraint, Context, Evidence, and Trust determine whether a particular operation may proceed.

⸻

62. Resource Access Does Not Imply Modification Authority

Likewise:

READ access
  ≠
WRITE authority

Example:

Support Agent
  └── has_access_to ──► Customer Record
Access:
READ

does not establish:

Authority:
MODIFY

Operations must be evaluated according to their actual semantic scope.

⸻

63. Resource Security Boundary

Resources may represent important security and governance boundaries.

Examples:

* Database
* Account
* API Key
* Customer Record
* Cloud Environment
* Repository

Consequential operations involving such Resources may require resolution of:

Actor
+
Intent
+
Resource
+
Authority
+
Policy
+
Constraint
+
Context
+
Evidence

before Trust permits execution.

⸻

64. Resource and Multi-Tenancy

A Resource may be scoped to a Tenant.

Resource ──scoped_to──► Tenant

An Actor’s authority over a Resource in one Tenant must not implicitly extend to a Resource in another Tenant.

Tenant scope is therefore relevant to Resource identity, resolution, access, Authority, and Trust evaluation.

⸻

65. Resource Ownership Transfer

Ownership of a Resource may change.

Example:

Account
   │
   ├── Owner A
   │
   ▼
TransferOwnership
   │
   ▼
Owner B

The resulting ownership state should be represented through the appropriate Outcome and canonical relationship.

Historical ownership must remain reconstructable.

⸻

66. Resource Deletion and History

Deleting or retiring a Resource does not necessarily remove historical references to it.

Example:

Account #123
    ↓
Deleted

Historical records may continue to reference:

Account #123

for:

* audit
* reconciliation
* legal obligations
* Outcome history
* provenance
* historical relationships

Therefore:

Resource deletion
  ≠
historical relationship deletion

⸻

67. Resource Auditability

For consequential Resources, Noema should be able to establish, where applicable:

Who accessed it?
Why?
Under which Intent?
Which Action?
Under which Authority?
Under which Policy?
Under which Context?
What happened?
What Evidence supports the result?

Resource relationships therefore participate directly in Noema’s auditability model.

⸻

68. Resource Lifecycle

Resources may participate in lifecycle states.

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

Another domain may use:

PENDING
   ↓
ACTIVE
   ↓
SUSPENDED
   ↓
CLOSED

Lifecycle semantics belong to the Resource’s domain.

Noema should not impose one universal Resource lifecycle where the domain does not require it.

⸻

69. Resource State Transitions

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

The semantic effect of such a transition should be represented through an Outcome.

The Action is what was performed.

The Outcome establishes what resulted.

The Resource records the resulting canonical state where applicable.

⸻

70. Resource Locking

Execution systems may temporarily lock Resources.

Conceptually:

Resource
   ↓
Lock
   ↓
Action Execution
   ↓
Release

Locking is an execution mechanism, not a foundational ontology requirement.

The ontology should represent the semantic effects of allocation, reservation, availability, or state rather than requiring a particular locking implementation.

⸻

71. Resource Model

Conceptually, a Resource may expose properties such as:

Resource
├── id
├── type
├── state
├── scope
├── quantity
├── availability
├── lifecycle
├── provenance
└── version

Not every Resource requires every property.

Properties should exist where they have semantic meaning for the Resource.

Ownership, custody, access, allocation, governance, Authority, and other relationships should remain relationships rather than being collapsed indiscriminately into Resource attributes.

⸻

72. Resource Relationship Model

The foundational Resource relationships include:

Actor ──owns──► Resource
Actor ──has_custody_of──► Resource
Actor ──has_access_to──► Resource
Intent ──targets──► Resource
Resource ──allocated_to──► Actor / Intent / Action
Intent ──reserves──► Resource
Action ──consumes──► Resource
Action ──modifies──► Resource
Action ──creates──► Resource
Action ──destroys──► Resource
Action ──transfers──► Resource
Action ──transforms──► Resource
Outcome ──affects──► Resource
Resource ──depends_on──► Resource
Resource ──contains──► Resource
Resource ──part_of──► Resource
Resource ──derived_from──► Resource
Resource ──governed_by──► Policy
Resource ──constrained_by──► Constraint
Authority ──scoped_to──► Resource
Capability ──operates_on──► Resource
Resource ──scoped_to──► Scope

The canonical relationship vocabulary and general relationship semantics are defined by ontology/relationships.md.

This document defines the meaning of Resource within those relationships.

⸻

73. Resource in the Noema Execution Model

The Resource participates in the broader semantic flow:

Actor
  │
  ▼
Intent
  │
  ├──────────────► Resource
  │                  │
  │                  ├── Policy
  │                  ├── Constraint
  │                  ├── Authority Scope
  │                  ├── State
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
  ├── transfers ──► Resource
  └── transforms ─► Resource
  │
  ▼
Execution
  │
  ▼
Outcome
  │
  └── affects ────► Resource

The Resource is therefore part of the semantic grounding required between understanding an Intent and permitting an Action.

⸻

74. Minimal Resource Resolution

For a consequential Intent involving a Resource, Noema should be able to resolve, where applicable:

Actor
   ↓
Intent
   ↓
Target Resource
   ↓
Resource Identity
   ↓
Resource State
   ↓
Resource Availability
   ↓
Relevant Constraints
   ↓
Relevant Policies
   ↓
Relevant Authority Scope
   ↓
Candidate Action

Only after the relevant Resource relationships are sufficiently resolved should the system cross the deterministic Trust boundary.

⸻

75. Resource Conflict Resolution

Where multiple requests contend for a Resource, Noema should preserve the relevant facts rather than collapsing them into an arbitrary decision.

For example:

Intent A ──reserves──► GPU #1
Intent B ──reserves──► GPU #1

The resulting state may require consideration of:

Resource
+
Availability
+
Reservation
+
Constraint
+
Policy
+
Context
+
Authority

The Resource ontology establishes what is being contested.

The applicable governance and resolution mechanisms determine how the conflict is handled.

⸻

76. Canonical Resource Invariants

The following are foundational:

1. A Resource is an operational object, asset, information object, service, or capacity against which an Intent or Action may have consequence.
2. Resource is semantically distinct from Entity, even where a Resource is an Entity occupying an operational role.
3. Resource is distinct from Capability.
4. Resource is distinct from Policy.
5. Resource is distinct from Constraint.
6. Resource is distinct from Context.
7. Capability describes what can be done; Resource describes what can be acted upon.
8. The existence of a Resource does not imply its availability.
9. Resource availability may be contextual and temporal.
10. Resource state may constrain an Action.
11. Ownership does not imply unlimited Authority.
12. Access does not imply modification Authority.
13. Resource identity must be resolved against authoritative data where consequential.
14. Ambiguous Resource references must not be silently resolved by guessing.
15. Resource quantity is distinct from Resource availability.
16. Resource reservation is distinct from Resource allocation.
17. Resource consumption is distinct from Resource destruction.
18. Resource creation and destruction should be represented through Actions and resulting Outcomes.
19. Resource governance should be explicit through relevant Policy relationships.
20. Resource Authority scope should be explicit where applicable.
21. Resource state and availability are relevant inputs to consequential execution.
22. Resource conflicts must not be silently resolved by arbitrary selection.
23. Historical Resource relationships must remain auditable.
24. Resource deletion does not require deletion of historical references.
25. Model-generated Resource candidates are not automatically authoritative Resources.
26. A Resource relationship that materially affects Trust should have sufficient supporting Evidence and provenance.
27. Resource semantics must remain independent of storage or execution implementation.
28. Consequential operations against Resources must cross Noema’s Trust boundary.

⸻

77. Canonical Resource Chain

The Resource-centered execution chain is:

Actor
   │
   ▼
Intent ──────────────► Resource
   │                       │
   ├── Context ────────────┤
   ├── Policy ─────────────┤
   ├── Constraint ─────────┤
   └── Authority Scope ────┘
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

The Resource is not merely a target identifier attached to an Action.

It is part of the semantic state required to determine whether an Intent can be grounded into a consequential operation.

⸻

78. Canonical Principle

A Resource is the operational object, asset, information object, service, or capacity against which an Intent or Action has consequence.

The foundational distinction is:

Intent
  = what is wanted
Action
  = what is done
Capability
  = what can be done
Resource
  = what is acted upon or used
Constraint
  = what limits the operation
Policy
  = what governs the operation
Authority
  = the scope under which an operation may be performed
Context
  = the circumstances in which the operation is interpreted
Trust
  = whether the operation is permitted to cross the execution boundary
Execution
  = the attempt to perform the Action
Outcome
  = what resulted

Therefore:

Meaning
   ↓
Intent
   ↓
Resource Resolution
   ↓
Relationship Resolution
   ↓
Trust
   ↓
Action
   ↓
Execution
   ↓
Outcome
   ↓
Resource State

The critical Noema invariant is:

An Intent cannot become executable merely because the Model understood what the Actor said. The intended Resource must be resolved to a canonical referent, the relevant Resource relationships must be established, and the resulting operation must satisfy the conditions required to cross the Trust boundary.