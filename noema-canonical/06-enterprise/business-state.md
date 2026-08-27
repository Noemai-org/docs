Business State

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/business-state.md

⸻

1. Definition

Business State is the authoritative state of the enterprise domain that Noema operates against, but does not own.

Business State describes the current condition of enterprise entities and resources:

Account
Balance
Customer
Card
Order
Invoice
Employee
Subscription
Transaction
Permission

Noema may read, reference, validate, and act upon Business State.

The enterprise remains the authoritative owner of that state.

⸻

2. Purpose

Business State establishes a critical architectural boundary:

Noema
    │
    │ reads / evaluates / requests changes
    ▼
Enterprise System
    │
    │ owns
    ▼
Business State

Noema is not a replacement for:

* databases
* ledgers
* CRMs
* ERPs
* payment systems
* identity systems
* inventory systems
* HR systems
* enterprise systems of record

⸻

3. Core Principle

Noema owns the execution journey; the enterprise owns the business state.

This is one of the most important boundaries in the Noema architecture.

Enterprise:
"What is true?"
Noema:
"What did the user intend, what Action was permitted,
what was executed, and what happened as a result?"

⸻

4. Business State vs Noema State

These must remain distinct.

Business State

account.balance = 5000
card.status = ACTIVE
employee.role = MANAGER
invoice.status = PAID

Noema State

intent.state = RESOLVED
action.state = READY
trust.state = DECIDED
trust.decision = EXECUTE
execution.state = COMPLETED

The former describes the enterprise.

The latter describes Noema’s execution process.

⸻

5. Enterprise System of Record

The enterprise system remains authoritative for its domain.

For example:

Banking System
    ↓
Account balance
Payment Processor
    ↓
Payment status
CRM
    ↓
Customer profile
Identity Provider
    ↓
User permissions

Noema consumes these sources rather than replacing them.

⸻

6. Noema as System of Record for Execution

Noema may become the system of record for:

Intent lifecycle
Clarification history
Action lifecycle
Trust decisions
Execution history
Intervention
Execution outcomes

Therefore:

Business State:
enterprise-owned
Execution State:
Noema-owned

⸻

7. Business State Is External to Noema

Business State should conceptually sit outside Noema.

                 NOEMA
┌───────────────────────────────────┐
│ Intent                            │
│ Action                            │
│ Trust                             │
│ Execution                         │
│ Audit                             │
└────────────────┬──────────────────┘
                 │
                 │ APIs / Events / Integrations
                 ▼
┌───────────────────────────────────┐
│       ENTERPRISE SYSTEMS          │
│                                   │
│ Accounts                          │
│ Customers                         │
│ Transactions                      │
│ Orders                            │
│ Permissions                       │
│ Ledgers                           │
└───────────────────────────────────┘

⸻

8. Business State Is Observed

Noema generally interacts with Business State through observation.

For example:

Context Request
       ↓
Enterprise API
       ↓
account.status = ACTIVE
account.balance = $5,000

Noema can then use those facts for:

* Intent resolution
* Trust evaluation
* Action planning
* Preconditions
* Execution
* Outcome verification

⸻

9. Observation Is Not Ownership

Noema storing:

account.balance = 5000

for evaluation purposes does not make Noema authoritative for the balance.

The distinction is:

Stored by Noema:
observed fact
Owned by enterprise:
authoritative fact

⸻

10. Business State Can Change

Business State is dynamic.

Example:

10:00
balance = $5,000
10:05
another transaction occurs
10:06
balance = $2,000

A previous Noema observation does not automatically remain valid.

⸻

11. State Freshness

Every Business State observation should be considered in terms of freshness.

Conceptually:

Business State
      ↓
Observed at T1
      ↓
Trust evaluation at T2
      ↓
Execution at T3

The system must determine whether the T1 observation remains valid at T2 or T3.

⸻

12. Stale State

Suppose:

Observed:
balance = $10,000

Then another transaction occurs:

Actual balance:
$3,000

If Noema still relies on the old observation to authorize:

transfer $8,000

the execution could be unsafe.

Therefore state freshness can become a Trust requirement.

⸻

13. Business State and Context

Business State is one of the primary sources of Context.

Business State
      ↓
Context
      ↓
Intent / Trust / Execution

Context provides the relevant subset of enterprise state needed for the current journey.

⸻

14. Context Is Not Business State

These are related but different.

Business State

The enterprise’s actual domain state.

Context

The relevant information gathered for Noema’s current operation.

Example:

Business State:
entire customer profile
Context:
customer.id
customer.status
customer.account_type

Noema does not need to replicate the entire enterprise domain to perform one Action.

⸻

15. Business State and Resources

Business resources have state.

Example:

Resource:
Account #123
State:
ACTIVE

or:

Resource:
Card #456
State:
BLOCKED

The resource model describes the enterprise object.

Business State describes its current condition.

⸻

16. Business State and Entity State

An Entity can possess multiple state dimensions.

For example:

Customer
├── identity
├── verification
├── account status
├── credit status
└── subscription status

Noema should avoid collapsing these into a single generic state when the enterprise domain distinguishes them.

⸻

17. Business State Transitions

Business State can transition because of:

human activity
Noema execution
external systems
scheduled processes
events
other applications

For example:

Card:
ACTIVE
  ↓
BLOCKED
  ↓
REPLACEMENT_REQUESTED
  ↓
ACTIVE

Noema may initiate one of these transitions without owning the state machine.

⸻

18. Noema Requests State Changes

The normal relationship is:

Noema
  ↓
Action
  ↓
Enterprise API
  ↓
Business State changes

For example:

Action:
freeze_card(card_123)
Enterprise:
card.status = FROZEN

Noema records the execution journey and observed result.

The enterprise remains authoritative for card.status.

⸻

19. No Direct State Mutation

Noema should not conceptually mutate enterprise state by directly manipulating another system’s database.

Bad:

Noema
  ↓
UPDATE enterprise_database

Preferred:

Noema
  ↓
Action
  ↓
Enterprise API / approved integration
  ↓
Business State

This preserves enterprise ownership and domain invariants.

⸻

20. Business State and Action Contracts

An Action Contract may depend on Business State.

Example:

Action:
withdraw_money
Precondition:
account.status = ACTIVE

Noema obtains the relevant state:

account.status → ACTIVE

Trust can then evaluate the precondition.

⸻

21. Business State and Preconditions

Business State frequently supplies precondition evidence.

Precondition:
account.balance >= amount
Observed:
balance = $10,000
Requested:
amount = $5,000
Result:
PRECONDITION_SATISFIED

The observation should be attributable to its source and time.

⸻

22. Business State and Policy

Policy can depend on Business State.

Example:

Policy:
Premium customers may transfer up to $50,000.
Business State:
customer.tier = PREMIUM

Trust combines these:

Business State
      +
Policy
      ↓
Trust Evaluation

⸻

23. Business State and Authorization

Authorization can also depend on Business State.

Example:

Business State:
employee.role = FINANCE_MANAGER

Authorization system:

FINANCE_MANAGER
    ↓
may approve invoices

Noema consumes the authorization result or authoritative role information.

⸻

24. Business State and Risk

Risk evaluation may depend on current state.

Example:

account.failed_attempts = 5

combined with:

new withdrawal request

may influence the risk evaluation.

Again, Noema does not become the authority for the underlying account state.

⸻

25. Business State and Outcome

After execution, Noema may verify the resulting Business State.

Example:

Action:
freeze_card(card_123)
Execution:
COMPLETED
Enterprise state:
card.status = FROZEN

The observed Business State provides evidence for the Outcome.

⸻

26. Execution Success vs Business State Change

These must remain distinct.

Execution:
COMPLETED

does not automatically imply:

Business State:
desired state achieved

The enterprise may accept a request asynchronously.

Therefore Noema may need to verify the resulting state.

⸻

27. Eventual Consistency

Enterprise systems may be eventually consistent.

Example:

Noema requests:
cancel_order
Enterprise:
request accepted
Immediately:
order.status = PROCESSING
Later:
order.status = CANCELLED

Noema must not assume that the first response necessarily represents the final Business State.

⸻

28. Business State and Events

Enterprise events may communicate Business State changes.

order.cancelled
      ↓
Noema
      ↓
Outcome verification

Events can therefore complement direct API queries.

⸻

29. Event vs State

An event says:

Something happened.

State says:

This is the current condition.

Example:

Event:
card.frozen
State:
card.status = FROZEN

Noema may consume both.

Neither should be treated as interchangeable.

⸻

30. State Authority

When multiple systems provide conflicting state, Noema must know which source is authoritative.

Example:

CRM:
customer.status = ACTIVE
Billing System:
customer.status = SUSPENDED

Noema cannot arbitrarily choose one.

The enterprise integration and domain configuration must define the authoritative source.

⸻

31. Source of Truth

For every important Business State attribute, there should be a definable authority.

Conceptually:

account.balance
    → Ledger
customer.identity
    → Identity Service
subscription.status
    → Billing System

Noema should consume this authority rather than inventing its own.

⸻

32. Conflicting State

If authoritative state cannot be established:

Source A:
ACTIVE
Source B:
SUSPENDED

Noema should not silently select the more convenient value for consequential execution.

Depending on Policy, the system may:

CLARIFY
ESCALATE
REJECT
HOLD

⸻

33. Business State and Determinism

Trust decisions should use explicitly identified Business State observations.

For example:

balance:
$5,000
observed_at:
12:03:11
source:
ledger

This makes the decision’s factual basis reconstructable.

⸻

34. Business State Snapshot

For high-risk operations, Noema may preserve a relevant state snapshot.

Example:

{
  "account_status": "ACTIVE",
  "available_balance": 5000,
  "observed_at": "..."
}

This snapshot is evidence of what Noema observed.

It does not replace the enterprise ledger.

⸻

35. Snapshot vs Live Query

Noema may use either:

snapshot

or:

live query

depending on the Action’s requirements.

High-risk operations may require a fresh query immediately before execution.

⸻

36. Business State and TOCTOU

Noema must account for time-of-check to time-of-use problems.

Example:

T1:
check balance
T2:
another transaction changes balance
T3:
execute transfer

A successful check at T1 does not guarantee the condition remains true at T3.

Possible mitigations include:

fresh validation
enterprise-side atomic enforcement
transactional APIs
conditional requests
idempotency
optimistic concurrency

The enterprise system should enforce authoritative invariants.

⸻

37. Enterprise Invariants

Business systems may enforce invariants such as:

balance cannot become negative
order cannot be cancelled after shipment
invoice cannot be paid twice
card cannot be simultaneously ACTIVE and BLOCKED

Noema should respect these invariants rather than attempting to recreate them independently.

⸻

38. Noema Must Not Become a Shadow Ledger

A dangerous architectural failure would be:

Enterprise Ledger
        +
Noema Ledger
        ↓
Two competing truths

Noema should not maintain a parallel authoritative copy of critical financial or business state merely for convenience.

⸻

39. Cached Business State

Caching may still be useful.

For example:

cached customer tier
cached capabilities
cached metadata

But cached values must be treated according to their freshness and authority requirements.

A cache is not automatically authoritative.

⸻

40. Business State and Permissions

Permissions are Business State or authorization-related state depending on the enterprise architecture.

Examples:

user.role
user.permissions
account.access_level

Noema should consume the enterprise’s authoritative authorization semantics.

It should not invent a parallel permission model that overrides the enterprise.

⸻

41. Business State and Capability

Capability answers:

Can this enterprise system perform this operation?

Business State answers:

What is the current condition of the relevant business object?

Example:

Capability:
refund_payment
Business State:
payment.status = SETTLED

Both may be required to execute a refund.

⸻

42. Business State and Resource Availability

Some resources are stateful.

Example:

Warehouse inventory:
SKU-123 = 4 units

An Action:

ship 3 units

depends on that state.

If the inventory changes before execution, Trust or the enterprise system must prevent an invalid operation.

⸻

43. Business State and Human Intent

Users often refer to Business State implicitly.

Example:

“Cancel my pending order.”

Noema must determine:

Which order?
Is it pending?
Can pending orders be cancelled?

These questions require Business State.

⸻

44. Business State and Intent Resolution

Business State may disambiguate Intent.

Example:

User:
"Cancel my order."
Enterprise state:
Order A — CANCELLED
Order B — SHIPPED
Order C — PENDING

Noema may infer that Order C is the relevant candidate.

However:

Business State may provide evidence for resolution, but consequential ambiguity must still be handled explicitly.

⸻

45. Business State and Historical Context

Current Business State is not always enough.

Some Actions depend on history.

Example:

number_of_refunds_in_last_30_days
previous_approvals
transaction_velocity
prior_failed_attempts

Noema may retrieve historical enterprise information as Context.

The underlying history remains enterprise-owned.

⸻

46. Business State and Temporal Context

Some state is valid only within a time period.

Examples:

promotion active until midnight
authorization expires at 18:00
account temporarily restricted

Trust must evaluate state relative to the relevant execution time.

⸻

47. Business State and Multi-System Domains

A single Action may span multiple enterprise systems.

Example:

Refund payment
    ↓
Payment processor
Update order
    ↓
Order system
Notify customer
    ↓
Messaging system

There may therefore be no single global Business State.

Noema must treat each enterprise system according to its domain authority.

⸻

48. Distributed Business State

Distributed state introduces challenges:

system A:
UPDATED
system B:
PENDING
system C:
FAILED

Noema should not manufacture a fictional unified state.

Instead, it should model the relevant observations and their sources.

⸻

49. Business State and Execution Saga

When an Action spans multiple enterprise systems, execution may produce intermediate Business State.

Step 1:
payment captured
Step 2:
order updated
Step 3:
inventory reserved

If Step 3 fails, Noema’s Compensation mechanisms may attempt corrective Actions.

The enterprise systems remain authoritative for each resulting state.

⸻

50. Business State and Compensation

Compensation does not mean restoring Noema’s state.

It means performing another Action intended to restore or mitigate enterprise state.

Example:

Capture payment
      ↓
Inventory reservation fails
      ↓
Compensating Action:
refund payment

Noema records this execution chain.

The payment provider remains authoritative for payment state.

⸻

51. Business State and Auditability

Auditability should record relevant observations of Business State without pretending to own them.

Example:

Trust evaluated at 14:02
Observed:
account.status = ACTIVE
source = Banking API
observed_at = 14:02:04

Later:

account.status = FROZEN

The historical observation remains part of the audit trail.

⸻

52. Historical State Must Not Be Rewritten

If the enterprise state changes:

14:00:
ACTIVE
14:10:
FROZEN

the audit record of the 14:00 observation must not become:

FROZEN

It must remain historically accurate.

⸻

53. Business State and Trust

Trust uses Business State as evidence.

Business State
       ↓
Evidence
       ↓
Trust Evaluation
       ↓
Decision

The Trust decision must identify important state observations used to reach it.

⸻

54. Business State and Action Eligibility

Business State can determine whether an Action is currently eligible.

Example:

Action:
cancel_order(order_123)
Business State:
order.status = SHIPPED

If policy says shipped orders cannot be cancelled:

Trust:
REJECT

⸻

55. Business State and Policy Versioning

A historical decision may depend on both:

Business State at T1
+
Policy version N

An auditor must be able to distinguish this from:

Business State at T2
+
Policy version N+1

⸻

56. Business State Access

Noema should access Business State through approved enterprise interfaces.

Preferred:

API
event stream
query interface
domain service
approved connector

Avoid:

direct database coupling
undocumented internal tables
bypassing domain APIs

unless explicitly supported by the enterprise architecture.

⸻

57. Business State Permissions

Noema’s ability to read Business State should itself be governed.

Noema
   ↓
Enterprise authorization
   ↓
Read permitted?

Noema should receive only the state required for the relevant operation.

⸻

58. Data Minimization

Noema should not ingest an entire enterprise database simply because it can.

The canonical principle is:

Retrieve the minimum Business State necessary to resolve, trust, execute, or verify the current Action.

⸻

59. Sensitive Business State

Business State may contain highly sensitive information.

Examples include:

financial information
identity information
employment information
customer information
internal operational data

Access, retention, storage, and exposure must follow enterprise policy.

⸻

60. Business State and Tenant Isolation

Business State must always remain tenant-scoped where applicable.

An Action belonging to:

Tenant A

must not accidentally retrieve or act upon:

Tenant B

This boundary should be enforced at the integration and Trust layers.

⸻

61. Business State and Idempotency

Business State can help determine whether an Action has already taken effect.

Example:

Action:
refund payment
Current state:
payment.status = REFUNDED

Noema may determine that another refund should not be issued.

However, enterprise-side idempotency remains preferable where available.

⸻

62. Business State and Concurrency

Multiple actors may change the same resource.

User A → update account
User B → freeze account
Agent C → close account

Noema must not assume exclusive ownership of the resource.

Enterprise systems should enforce concurrency and state-transition invariants.

⸻

63. Optimistic Concurrency

Where supported, Noema may provide:

version = 42

with an Action:

update_resource(expected_version=42)

The enterprise system can reject the operation if the state has changed.

This is preferable to Noema assuming that an old observation remains valid.

⸻

64. Business State and Preconditions at Execution

Preconditions may be checked:

during Trust

but some conditions should also be enforced:

at execution time

This is especially important when state can change between Trust and Execution.

⸻

65. Business State Authority Hierarchy

Where necessary, Noema should know:

Primary authoritative source
        ↓
Secondary source
        ↓
Cached observation
        ↓
Derived inference

Consequential decisions should prefer the highest-authority available source.

⸻

66. Derived Business State

Some state may be computed.

Example:

customer.is_high_value = true

derived from:

annual_spend > threshold

Noema should identify whether such values are:

authoritative enterprise attributes

or:

derived observations

The distinction matters for Trust.

⸻

67. Business State and Model Inference

An LLM may infer:

"John is probably the customer's manager."

That is not automatically Business State.

Inference should not be promoted into authoritative enterprise fact without an appropriate source or explicit confirmation.

⸻

68. Business State Must Be Grounded

For consequential execution:

Model inference
       ≠
Business State

Instead:

Enterprise source
       ↓
Business State
       ↓
Context / Evidence
       ↓
Trust

⸻

69. Business State and Noema’s Moat

Noema does not need to own the enterprise data to create value.

Its value lies in understanding how to:

discover relevant state
interpret it
evaluate it
combine it with policy
reason about freshness
use it to construct Actions
verify outcomes

This makes the execution journey the product rather than another database.

⸻

70. Canonical Relationship

                ENTERPRISE
┌─────────────────────────────────┐
│                                 │
│       BUSINESS STATE            │
│                                 │
│ accounts                        │
│ customers                       │
│ orders                          │
│ permissions                     │
│ transactions                    │
│ inventory                       │
│ subscriptions                   │
│                                 │
└───────────────┬─────────────────┘
                │
          authoritative
             state
                │
                ▼
              Noema
┌─────────────────────────────────┐
│                                 │
│ Context                         │
│ Intent Resolution               │
│ Trust                           │
│ Action                          │
│ Execution                       │
│ Audit                           │
│ Outcome                         │
│                                 │
└─────────────────────────────────┘

⸻

71. Canonical Flow

Enterprise Business State
          │
          ▼
       Context
          │
          ├───────────────┐
          ▼               ▼
   Intent Resolution    Trust
          │               │
          ▼               │
        Action ◄──────────┘
          │
          ▼
      Execution
          │
          ▼
Enterprise System
          │
          ▼
 Business State Change
          │
          ▼
 Outcome Verification

⸻

72. Canonical Invariants

Invariant 1

The enterprise remains authoritative for Business State.

Invariant 2

Noema owns the execution journey, not the underlying business state.

Invariant 3

Noema must not create a competing system of record for critical enterprise state.

Invariant 4

Business State observations must be attributable to an authoritative source where possible.

Invariant 5

State freshness must be considered whenever stale information could produce unsafe execution.

Invariant 6

Historical observations must remain historically accurate.

Invariant 7

Noema must not silently convert model inference into authoritative Business State.

Invariant 8

Conflicting authoritative state must not be resolved through arbitrary guessing.

Invariant 9

Enterprise invariants remain enforced by the enterprise system.

Invariant 10

Noema should interact with Business State through approved interfaces rather than bypassing domain ownership.

Invariant 11

Business State used for consequential Trust decisions must be sufficiently authoritative and fresh for the operation.

Invariant 12

Execution success does not imply that the desired Business State was achieved.

Invariant 13

Outcome verification may require observing Business State after execution.

Invariant 14

Business State access must respect authorization, tenant isolation, and data-minimization requirements.

Invariant 15

Cached Business State must not be treated as authoritative merely because it exists inside Noema.

Invariant 16

Distributed Business State must preserve source and domain authority rather than being collapsed into an artificial single truth.

Invariant 17

Noema must account for state changes between Trust evaluation and execution.

Invariant 18

Where possible, authoritative enterprise systems should enforce critical state invariants at execution time.

Invariant 19

Noema may record Business State observations as evidence without becoming the owner of that state.

Invariant 20

A Noema audit trail must distinguish observed Business State from Noema-owned execution state.

⸻

73. Final Definition

Business State is the authoritative condition of the enterprise’s entities, resources, and domain systems. Noema observes and uses Business State as context and evidence for Intent resolution, Trust, Action construction, execution, and Outcome verification, while leaving ownership and authority over that state with the enterprise systems that maintain it.

The architectural boundary is:

                    NOEMA
      ┌────────────────────────────┐
      │                            │
      │ Intent                     │
      │ Resolution                 │
      │ Context                    │
      │ Trust                      │
      │ Action                     │
      │ Execution                  │
      │ Audit                      │
      │ Outcome                    │
      │                            │
      └─────────────┬──────────────┘
                    │
              observes / acts
                    │
                    ▼
      ┌────────────────────────────┐
      │         ENTERPRISE         │
      │                            │
      │ Business State             │
      │ Systems of Record          │
      │ Domain Invariants          │
      │ Ledgers                    │
      │ Permissions                │
      │ Resources                  │
      │                            │
      └────────────────────────────┘

Noema should be the system of record for the journey, not the system of record for the world it operates on.