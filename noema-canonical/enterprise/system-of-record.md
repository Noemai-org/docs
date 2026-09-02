System of Record

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/system-of-record.md

⸻

1. Definition

A System of Record (SoR) is the authoritative enterprise system responsible for maintaining the canonical state of a particular business domain, resource, or fact.

The System of Record concept establishes a critical boundary for Noema:

Noema may understand, orchestrate, observe, and act upon enterprise state without becoming the authoritative owner of that state.

For example:

CRM
→ customer record
Ledger
→ financial balance
HRIS
→ employee status
IAM
→ identity and permissions
Inventory system
→ inventory state

Noema integrates with these systems rather than replacing them.

⸻

2. Purpose

The purpose of this concept is to prevent Noema from becoming a shadow system of record.

Noema will inevitably maintain state about executions:

Intent
Trust Decision
Action
Execution
Outcome
Intervention

That state is different from the underlying business state:

Customer
Account
Balance
Employee
Invoice
Order
Inventory

The distinction must remain explicit.

⸻

3. Core Principle

The enterprise owns business truth; Noema owns execution truth.

This is one of the most important architectural boundaries in Noema.

ENTERPRISE
────────────────────────────
Business Truth
customer
account
balance
invoice
order
employee
inventory
NOEMA
────────────────────────────
Execution Truth
intent
resolution
trust
action
execution
outcome
intervention

⸻

4. Business Truth

Business Truth is the authoritative state of the enterprise domain.

Examples:

Account.balance = $10,000
Invoice.status = PAID
Employee.status = ACTIVE
Card.status = FROZEN
Order.status = SHIPPED

The authoritative value belongs to the designated enterprise System of Record.

Noema may cache or derive representations of these values, but those representations do not supersede the source.

⸻

5. Execution Truth

Noema owns facts about the execution journey it manages.

Examples:

Intent received at 10:42
Intent resolved at 10:43
Trust decision = EXECUTE
Action submitted
Execution timed out
Outcome = UNKNOWN
Human intervention requested

These are Noema-native facts.

The enterprise System of Record does not necessarily know this entire causal journey.

⸻

6. System of Record vs Noema State

Consider:

Intent:
"Refund my last payment."

Noema may record:

intent_id = 123
action = refund_payment
trust_decision = EXECUTE
execution_status = COMPLETED

The payment system remains authoritative for:

payment.status
refund.status
refund.amount
transaction_id

Noema’s record of:

execution_status = COMPLETED

does not replace the payment system’s record of the actual financial state.

⸻

7. One Fact, One Authority

Where possible, every consequential enterprise fact should have a clearly defined authoritative source.

For example:

Identity
→ Identity Provider
Employee Status
→ HRIS
Account Balance
→ Ledger
Payment Status
→ Payment System
Inventory
→ Inventory System

Noema should know where the truth lives.

⸻

8. Authority Is Domain-Specific

There is not necessarily one enterprise-wide System of Record.

Different domains may have different authorities.

             ENTERPRISE
   ┌──────────┬───────────┬──────────┐
   ▼          ▼           ▼          ▼
 Identity    Finance      HR       Inventory
   │           │           │          │
   ▼           ▼           ▼          ▼
  IAM        Ledger       HRIS      ERP

Noema integrates across them.

⸻

9. Source of Truth vs Source of Evidence

These terms must not be conflated.

System of Record

The authoritative owner of a particular fact.

Source of Evidence

A system that provides information useful for reasoning or verification.

For example:

CRM
→ customer information
Payment System
→ authoritative payment state

The CRM may provide evidence about the customer, but it may not be authoritative for the payment.

⸻

10. Enterprise APIs

An API is not automatically a System of Record.

An API is an interface to a system.

API
 ↓
Service
 ↓
Database / Business System

The underlying service or system may own the authoritative state.

Noema should therefore distinguish:

interface

from:

authority

⸻

11. Noema as an Execution System of Record

Noema may itself become a System of Record for certain execution-domain facts.

For example:

execution_id
intent_id
action_id
trust_decision
execution_state
intervention
execution_history

This is compatible with the enterprise boundary because these are facts about Noema’s orchestration.

Therefore:

Noema should not avoid becoming a System of Record entirely; it should become the System of Record for the execution journey it owns.

⸻

12. Execution Journey

The execution journey can be modeled as:

Intent
   ↓
Interpretation
   ↓
Resolution
   ↓
Context
   ↓
Trust
   ↓
Action
   ↓
Execution
   ↓
Outcome

Noema should preserve this history as a coherent causal record.

⸻

13. Business State Must Remain External

Suppose Noema executes:

freeze_card

The enterprise card system reports:

status = FROZEN

Noema may record:

Action = freeze_card
Outcome = SUCCESS

But the canonical card state remains:

Card System:
status = FROZEN

Noema should not maintain a competing:

Noema:
card.status = FROZEN

as an authoritative business record.

⸻

14. Cached Enterprise State

Noema may cache enterprise state for performance.

For example:

Customer:
id = 123
status = ACTIVE

But cached state is:

derived

not:

authoritative

The cache should have an explicit freshness model.

⸻

15. Stale State

Consider:

Noema cache:
account.balance = $5,000

Enterprise ledger:

account.balance = $2,000

The ledger wins.

Noema must never treat stale cached state as authoritative merely because it has a locally stored value.

⸻

16. Read-After-Write

After consequential execution, Noema may need to verify the resulting Business State against the System of Record.

Action
  ↓
Enterprise mutation
  ↓
Query System of Record
  ↓
Verify Postcondition
  ↓
Outcome

This is particularly important where execution responses are asynchronous or ambiguous.

⸻

17. Unknown Outcome

A critical case:

Noema
   ↓
POST /refund
   ↓
timeout

Noema cannot safely conclude:

refund failed

The request may have succeeded.

Instead:

Execution:
OUTCOME_UNKNOWN

Noema should reconcile against the System of Record.

⸻

18. Reconciliation

Reconciliation resolves differences between:

Noema Execution State

and:

Enterprise Business State

Example:

Noema:
refund request submitted
outcome unknown
        ↓ query
Payment System:
refund completed

Noema can then transition:

OUTCOME_UNKNOWN
        ↓
CONFIRMED_SUCCESS

The payment system remains authoritative for the refund itself.

⸻

19. System-of-Record Discovery

Noema may need to determine:

Which system owns this fact?

This may come from:

Enterprise configuration
Integration metadata
Action Contract
API documentation
Enterprise Action Graph
Human configuration

Noema should not infer authority purely from whichever system happens to return data first.

⸻

20. Provenance

Enterprise facts should retain provenance where consequential.

Conceptually:

Fact {
    value
    source
    observed_at
    version
    authority
}

Example:

balance = $5,000
source = Ledger
observed_at = 10:32:04
authority = authoritative

This allows Trust decisions to distinguish authoritative evidence from secondary information.

⸻

21. Authority Hierarchy

When multiple sources provide conflicting information, Noema needs an authority model.

Example:

Ledger
    ↑
authoritative
Analytics DB
    ↑
derived
Cache
    ↑
temporary

A conflict should not be resolved through model preference.

It should be resolved according to explicitly defined source authority.

⸻

22. Conflicting Systems

Suppose:

CRM:
customer.status = ACTIVE
Billing:
customer.status = SUSPENDED

Noema must not simply select:

ACTIVE

because it appears more frequently or semantically plausible.

The relevant domain authority must be established.

⸻

23. Authority Is Action-Dependent

The authoritative system may depend on the fact being evaluated.

Example:

Customer name
→ CRM
Payment status
→ Payment System
Account balance
→ Ledger

Noema’s Enterprise Action Graph should represent these relationships explicitly where useful.

⸻

24. System of Record and Context

Context should identify the source of important enterprise facts.

Context
├── customer
│    └── source = CRM
│
├── payment
│    └── source = Payment System
│
└── balance
     └── source = Ledger

This prevents Context from becoming an undifferentiated collection of potentially stale information.

⸻

25. System of Record and Trust

Trust should consider the authority of evidence.

For example:

Evidence:
account.balance = $5,000
Source:
Ledger
Authority:
authoritative

is stronger than:

Evidence:
account.balance = $5,000
Source:
cached analytics database

The distinction can materially affect high-risk execution.

⸻

26. System of Record and Preconditions

Preconditions should be evaluated against the appropriate authoritative state.

Example:

Precondition:
balance >= $1,000

For a financial Action, Noema should generally evaluate this against the authoritative financial source rather than an arbitrary cached representation.

⸻

27. System of Record and Postconditions

Postconditions may require verification against the System of Record.

Example:

Action:
cancel_subscription
Postcondition:
subscription.status = CANCELLED

Verification:

Subscription System
→ status = CANCELLED

Only then should Noema mark the business outcome as confirmed.

⸻

28. System of Record and Action Contracts

An Action Contract should identify the enterprise capability and, where relevant, the authoritative resource system.

Conceptually:

ActionContract {
    action
    target
    capability
    preconditions
    execution
    postconditions
    authority_source
}

This helps Noema understand where execution occurs and where outcome verification should happen.

⸻

29. System of Record and Integrations

Integrations should expose enough metadata to establish:

system identity
capability
resource ownership
authority
schema
version

For example:

Integration:
Payments API
System:
Payment Service
Authority:
payment state
Capabilities:
refund
capture
void

⸻

30. System of Record and Events

Events may originate from the authoritative system.

Example:

Payment System
      ↓
payment.refunded
      ↓
Noema

The event provides strong evidence that the System of Record changed.

Noema should preserve:

event source
event identity
event timestamp
event version

where required for reconciliation and audit.

⸻

31. Events Are Not Automatically Authority

An event may be delayed, duplicated, reordered, or lost.

Therefore:

event received

does not necessarily mean:

current state = event payload

For consequential verification, Noema may need to query the System of Record.

⸻

32. Eventual Consistency

Enterprise architectures frequently contain:

primary database
read replicas
event streams
caches
search indexes
analytics systems

These may temporarily disagree.

Noema must understand the consistency guarantees of the system it is interacting with.

⸻

33. Derived Systems

Derived systems include:

search indexes
data warehouses
analytics databases
materialized views
caches
event projections

These are useful for Context and discovery.

They should not be treated as authoritative unless the enterprise explicitly designates them as such.

⸻

34. Noema’s Own Database

Noema’s database may contain:

intent records
execution records
action records
trust decisions
audit records
integration metadata
reconciliation state

This database is authoritative for these Noema-owned concepts.

It is not automatically authoritative for:

accounts
payments
employees
customers
inventory

⸻

35. Shadow System of Record

A shadow System of Record occurs when Noema begins maintaining an independent authoritative representation of enterprise Business State.

For example:

Enterprise:
account.balance = $10,000
Noema:
account.balance = $10,000

Then Noema starts modifying its own copy:

Noema:
account.balance = $8,000

while the enterprise ledger says:

Enterprise:
account.balance = $7,500

At this point Noema has created conflicting business truth.

This should be avoided.

⸻

36. Why Shadow State Is Dangerous

Shadow Business State creates:

consistency problems
reconciliation complexity
stale data
authority conflicts
security exposure
duplicated business logic
operational complexity

It also moves Noema toward becoming another enterprise application rather than an execution infrastructure layer.

⸻

37. Reference vs Ownership

Noema should distinguish:

reference

from:

ownership

For example:

Noema:
customer_id = 123

is a reference.

It does not mean Noema owns:

Customer #123

The customer remains owned by the appropriate enterprise system.

⸻

38. Entity Identity

Enterprise Resources should normally be referenced using stable enterprise identifiers.

Example:

customer_id
account_id
invoice_id
payment_id

Noema should avoid inventing a second identity for the same enterprise resource unless there is a specific architectural need.

⸻

39. Tenant Boundaries

In multi-tenant environments:

Tenant A
   ↓
System of Record A
Tenant B
   ↓
System of Record B

Noema must maintain strict tenant boundaries.

A resource from one tenant must never become accessible merely because another tenant has a similar identifier.

⸻

40. Organizational Authority

A System of Record can also establish organizational facts.

For example:

HRIS
→ employee belongs to Finance
IAM
→ employee has role Finance Manager

Noema consumes these facts when evaluating enterprise authority.

It should not manufacture organizational authority from behavioral patterns.

⸻

41. Human Configuration

Some enterprise authority relationships may not exist in machine-readable systems.

For example:

"All refunds above $10,000 require CFO approval."

Noema may ingest such configuration into its enterprise model.

But the configuration itself must have:

owner
version
effective date
provenance

where appropriate.

⸻

42. System-of-Record Metadata

A useful abstraction is:

SystemOfRecord {
    system_id
    domain
    resource_types
    authoritative_facts
    capabilities
    consistency_model
    version
    provenance
}

This metadata allows Noema to reason about enterprise authority without owning the underlying data.

⸻

43. Authority Changes

Enterprise architecture evolves.

A business may migrate:

CRM A
    ↓
CRM B

or:

Ledger A
    ↓
Ledger B

Noema must support changes in System-of-Record designation without requiring the core intent model to change.

⸻

44. System-of-Record Versioning

Where authority changes over time, Noema may need to know:

before migration:
System A authoritative
after migration:
System B authoritative

This matters when reconstructing historical execution decisions.

⸻

45. Historical Authority

An old execution may have relied on:

System A

even though:

System B

is authoritative today.

Auditability therefore requires preserving enough provenance to understand which source was authoritative at the time of execution.

⸻

46. System of Record and Auditability

A good audit record can answer:

Which enterprise system supplied the relevant fact?
Was that system authoritative?
When was the fact observed?
What version or revision was used?
Did the authoritative state change before execution?
Was postcondition verification performed?

⸻

47. System of Record and Determinism

Deterministic Trust requires deterministic authority resolution.

Noema should not do:

System A says X
System B says Y
Model thinks X is probably right
→ execute

Instead:

Conflict detected
     ↓
Authority relationship evaluated
     ↓
Authoritative source identified
     ↓
State verified
     ↓
Trust decision

If authority cannot be established:

CLARIFY
ESCALATE
or REJECT

depending on policy.

⸻

48. System of Record and Failure

If the System of Record is unavailable:

GET /account/123
        ↓
timeout

Noema should not substitute arbitrary stale state for authoritative state when the Action requires current truth.

The resulting state may be:

AUTHORITY_UNAVAILABLE

which Trust and Policy can handle explicitly.

⸻

49. Fail-Closed for Consequential Operations

For high-risk Actions:

authoritative state unavailable

should generally prevent execution unless enterprise Policy explicitly allows an alternative.

This prevents Noema from crossing the enterprise boundary based on uncertain Business State.

⸻

50. System of Record and Offline Execution

Offline or delayed execution requires special care.

If:

Intent resolved at T1

but:

Action executes at T2

then the authoritative Business State may have changed.

The Action’s Preconditions may therefore need revalidation immediately before execution.

⸻

51. System of Record and Concurrency

Two Noema executions may target the same enterprise resource.

Example:

Execution A:
withdraw $5,000
Execution B:
withdraw $5,000

Both may observe:

balance = $10,000

If the enterprise System of Record supports transactional concurrency controls, Noema should rely on them rather than attempting to recreate ledger semantics locally.

⸻

52. System of Record and Idempotency

Idempotency belongs at the execution boundary.

Noema may maintain:

execution_id
idempotency_key

The enterprise System of Record or capability implementation should enforce the business semantics of duplicate operations where supported.

⸻

53. System of Record and Compensation

Compensation should mutate Business State through the authoritative enterprise capability.

Noema should not directly manipulate a shadow representation to simulate rollback.

Original Action
      ↓
Enterprise
      ↓
Compensation Action
      ↓
Enterprise

⸻

54. System of Record and Recovery

Recovery decisions belong to Noema’s execution layer.

Business-state mutations remain enterprise-owned.

Noema:
retry / compensate / reconcile / escalate
Enterprise:
apply actual state transition

⸻

55. System-of-Record Boundary

The boundary can be summarized as:

┌──────────────────────────────────────────┐
│              ENTERPRISE                 │
│                                          │
│      SYSTEMS OF RECORD                   │
│                                          │
│  Customer  Account  Ledger  HR  Orders  │
│       │       │       │      │      │   │
└───────┼───────┼───────┼──────┼──────┼───┘
        │       │       │      │      │
        └───────┴───────┼──────┴──────┘
                        │
                 Enterprise APIs
                        │
                        ▼
┌──────────────────────────────────────────┐
│                 NOEMA                    │
│                                          │
│ Intent → Trust → Action → Execution      │
│                       │                  │
│                       ▼                  │
│                    Outcome               │
│                                          │
│     Execution System of Record           │
└──────────────────────────────────────────┘

⸻

56. Canonical Invariants

Invariant 1

Every consequential enterprise fact should have a clearly understood authoritative source.

Invariant 2

Noema must not become a shadow System of Record for Business State.

Invariant 3

Noema may be the System of Record for the execution journey it owns.

Invariant 4

Enterprise Business State remains authoritative within the enterprise System of Record.

Invariant 5

Cached or derived enterprise data is not authoritative unless explicitly designated as such.

Invariant 6

Source of evidence and System of Record are distinct concepts.

Invariant 7

An API is an interface, not necessarily the System of Record.

Invariant 8

Authority is domain-specific and may differ across enterprise resources.

Invariant 9

Authority may be Action-dependent.

Invariant 10

Conflicting sources must be resolved through explicit authority semantics, not model preference.

Invariant 11

Authoritative state should be revalidated when freshness materially affects execution safety.

Invariant 12

Unknown execution outcomes must be reconciled against the appropriate System of Record where possible.

Invariant 13

Events are evidence of state transitions but do not necessarily establish current state.

Invariant 14

Noema must preserve provenance for consequential enterprise facts and execution decisions where required.

Invariant 15

Historical audit records must preserve enough information to identify the authoritative source at the time of execution.

Invariant 16

If authoritative state is unavailable, Noema must not silently substitute uncertain state for high-risk execution.

Invariant 17

Noema should use enterprise transaction and concurrency semantics rather than recreating Business State management locally.

Invariant 18

Compensation and recovery must mutate Business State through authorized enterprise capabilities.

Invariant 19

Enterprise resource identity should remain anchored to enterprise identifiers.

Invariant 20

The boundary between enterprise Business Truth and Noema Execution Truth must remain explicit.

⸻

57. Final Definition

A System of Record is the authoritative enterprise source for a defined category of Business State. Noema integrates with Systems of Record to obtain authoritative context, perform authorized Actions, and verify Outcomes, while maintaining its own authoritative record of the execution journey.

The architectural boundary is therefore:

ENTERPRISE
owns:
Business Truth
NOEMA
owns:
Execution Truth

Or more precisely:

Noema should know where enterprise truth lives, use that truth to make deterministic execution decisions, and never quietly become the place where that truth lives.