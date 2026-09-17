Business State

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/business-state.md

⸻

1. Definition

Business State is the authoritative state of the enterprise domain that Noema operates against, but does not own.

Business State describes the condition of enterprise entities and resources:

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
Inventory

Noema may read, reference, validate, reconcile, and act upon Business State.

The enterprise remains the authoritative owner of that state.

⸻

2. Purpose

Business State establishes a critical architectural boundary:

Noema
    │
    │ observes / evaluates / requests changes
    ▼
Enterprise Systems
    │
    │ own
    ▼
Business State

Noema is not a replacement for:

databases
ledgers
CRMs
ERPs
payment systems
identity systems
inventory systems
HR systems
enterprise systems of record

⸻

3. Core Principle

Noema owns the execution journey; the enterprise owns the business state.

This is one of the most important boundaries in the Noema architecture.

Enterprise:
"What is true in the business domain?"
Noema:
"What did the source of Intent request,
what did Noema determine,
what state did it observe,
what Action was permitted,
what was executed,
and what Outcome was established?"

⸻

4. Business State vs Noema State

These must remain distinct.

Business State

account.balance = 5000
card.status = ACTIVE
employee.role = MANAGER
invoice.status = PAID

Noema Execution-Domain State

intent.state = RESOLVED
trust.decision = EXECUTE
execution.state = COMPLETED
execution.attempt = 2
outcome.state = VERIFIED

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

Noema may become the system of record for its own execution domain, including:

Intent lifecycle
Intent versions
Clarification history
Trust decisions
Execution history
Execution attempts
Verification history
Intervention
Case state
Noema Outcomes
Audit history
Operational Memory

Therefore:

Business State:
enterprise-owned
Execution-Domain State:
Noema-owned

Noema ownership of execution-domain state does not extend into ownership of enterprise business state.

⸻

7. Business State Is External to Noema

Business State should conceptually sit outside Noema.

                 NOEMA
┌───────────────────────────────────┐
│ Intent                            │
│ Resolution                        │
│ Context                           │
│ State Reconciliation              │
│ Trust                             │
│ Action                            │
│ Execution                         │
│ Verification                      │
│ Audit                             │
│ Outcome                           │
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

Noema generally interacts with Business State through observations.

For example:

Context Request
       ↓
Enterprise API
       ↓
account.status = ACTIVE
account.balance = $5,000

Noema can then use those observations for:

Intent resolution
State Reconciliation
Trust evaluation
Action planning
Preconditions
Execution
Outcome verification

⸻

9. Observation Is Not Ownership

Noema storing:

account.balance = 5000

for evaluation purposes does not make Noema authoritative for the balance.

The distinction is:

Stored by Noema:
observed value
Owned by enterprise:
authoritative business fact

A Noema observation may be evidence without becoming the enterprise truth.

⸻

10. Observation Is Not Fact Status

An observation is what a source reported or what Noema received.

Fact Status is Noema’s deterministic classification of a claim after applicable validation and State Reconciliation.

Canonical Fact Status values are:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Therefore:

Observation:
ledger reports balance = $5,000
Fact Status:
VERIFIED

or:

Observations:
ledger reports $5,000
payment system reports $3,000
Fact Status:
CONFLICTED

Observation and Fact Status must remain distinct.

⸻

11. Business State and State Reconciliation

State Reconciliation is a first-class boundary between enterprise observations and the state Noema can safely rely upon.

The canonical relationship is:

Enterprise Observations
        ↓
State Reconciliation
        ↓
Reconciled Facts / State
        ↓
Fact Status
        ↓
Context / Trust / Execution

State Reconciliation considers applicable:

source authority
identity
temporal validity
freshness
consistency
resource version
scope
integration semantics

Temporal recency alone does not resolve authority or conflict.

⸻

12. Hard Admission Boundary

External information must not become canonical Noema input merely because it was received or persisted.

Potentially untrusted inputs include:

user input
model output
retrieved enterprise text
external events
tool responses
integration payloads
external API responses

The canonical boundary is:

External Input
      ↓
Hard Schema Validation / Admission
      ↓
Eligible Canonical Noema Input
      ↓
State Reconciliation where applicable

Persistence does not create authority.

Unvalidated data may be retained for explicitly classified diagnostic or evidentiary purposes, but it must remain classified as such.

⸻

13. Business State Can Change

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

14. State Freshness

Every Business State observation should be considered in terms of freshness.

Conceptually:

Business State
      ↓
Observed at T1
      ↓
State Reconciliation
      ↓
Trust evaluation at T2
      ↓
Execution at T3

The system must determine whether the observation remains valid for the relevant claim and operation at T2 or T3.

Freshness is claim-, action-, and policy-specific.

There is no universal freshness duration for Business State.

⸻

15. Stale State

Suppose:

Observed:
balance = $10,000

Then another transaction occurs:

Actual balance:
$3,000

If Noema still relies on the old observation to authorize:

transfer $8,000

the execution could be unsafe.

Therefore stale state may cause:

reconciliation
revalidation
clarification
escalation
rejection

depending on the applicable Trust conditions.

⸻

16. Business State and Context

Business State is one of the primary sources of Context.

Business State
      ↓
Observations
      ↓
Reconciliation
      ↓
Context
      ↓
Intent / Trust / Execution

Context provides the relevant information gathered for the current journey.

Context is not a replacement for Business State.

⸻

17. Context Is Not Business State

These are related but different.

Business State

The enterprise’s authoritative domain state.

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

18. Business State, Evidence, and Context

Business State observations may become evidence for Noema decisions.

The relationship is:

Enterprise Business State
        ↓
Observation
        ↓
Evidence
        ↓
State Reconciliation
        ↓
Fact Status
        ↓
Context / Trust

Evidence supports claims.

Fact Status classifies claims.

Context supplies information to a particular evaluation.

None of these concepts should be treated as synonymous with enterprise authority.

⸻

19. Business State and Resources

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

20. Business State and Entity State

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

21. Business State Transitions

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

22. Noema Requests State Changes

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

Noema records the execution journey and observes the resulting state.

The enterprise remains authoritative for card.status.

⸻

23. No Direct State Mutation

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

24. Business State and Action Contracts

An Action Contract may depend on Business State.

Example:

Action:
withdraw_money
Precondition:
account.status = ACTIVE

Noema obtains the relevant state:

account.status → ACTIVE

State Reconciliation establishes whether that observation can support the claim.

Trust can then evaluate the precondition.

⸻

25. Business State and Preconditions

Business State frequently supplies precondition evidence.

Precondition:
account.balance >= amount
Observed:
balance = $10,000
Requested:
amount = $5,000
Result:
PRECONDITION_SATISFIED

The observation should be attributable to its source, time, authority, and applicable resource version.

⸻

26. Business State and Policy

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

The policy remains the governing rule.

Business State supplies relevant facts.

⸻

27. Business State and Authorization

Authorization can also depend on Business State.

Example:

Business State:
employee.role = FINANCE_MANAGER
Authorization system:
FINANCE_MANAGER
    ↓
may approve invoices

Noema consumes the authoritative authorization result or role information.

It does not create enterprise permission semantics.

⸻

28. Business State and Risk

Risk evaluation may depend on current state.

Example:

account.failed_attempts = 5

combined with:

new withdrawal request

may influence risk evaluation.

Again, Noema does not become the authority for the underlying account state.

⸻

29. Business State and Outcome

After execution, Noema may verify the resulting Business State.

Example:

Action:
freeze_card(card_123)
Execution:
COMPLETED
Enterprise observation:
card.status = FROZEN
Outcome:
VERIFIED

The observed Business State provides evidence for the Outcome.

⸻

30. Execution Success vs Business State Change

These must remain distinct.

Execution:
COMPLETED

does not automatically imply:

Business State:
desired state achieved

The enterprise may accept a request asynchronously or partially.

Therefore Noema may need to verify the resulting state.

⸻

31. Eventual Consistency

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

32. Business State and Events

Enterprise events may communicate Business State changes.

order.cancelled
      ↓
Noema
      ↓
State Reconciliation / Verification
      ↓
Outcome

Events can complement direct API queries.

An event is an observation or signal about a state transition; it is not automatically the current state itself.

⸻

33. Event vs State

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

34. State Authority

When multiple systems provide conflicting state, Noema must know which source is authoritative for the relevant claim.

Example:

CRM:
customer.status = ACTIVE
Billing System:
customer.status = SUSPENDED

Noema cannot arbitrarily choose one.

The enterprise integration and domain configuration must define the authoritative source for the relevant claim.

⸻

35. Source of Truth

For every important Business State attribute, there should be a definable authority.

Conceptually:

account.balance
    → Ledger
customer.identity
    → Identity Service
subscription.status
    → Billing System

Noema should consume this authority rather than inventing its own.

“Source of truth” is therefore claim- and domain-specific, not necessarily a single enterprise-wide system.

⸻

36. Conflicting State

If authoritative state cannot be established:

Source A:
ACTIVE
Source B:
SUSPENDED

Noema should not silently select the more convenient value for consequential execution.

Depending on applicable Policy and Trust conditions, the system may:

CLARIFY
ESCALATE
REJECT

or place execution into an explicit operational state requiring reconciliation.

Conflict must remain visible.

⸻

37. Business State and Determinism

Trust decisions should use explicitly identified Business State observations and reconciliation results.

For example:

claim:
account.balance = $5,000
observed_at:
12:03:11
source:
ledger
authority:
primary
Fact Status:
VERIFIED

This makes the decision’s factual basis reconstructable.

⸻

38. Business State Snapshot

For high-risk operations, Noema may preserve a relevant state snapshot.

Example:

{
  "account_status": "ACTIVE",
  "available_balance": 5000,
  "observed_at": "..."
}

This snapshot is evidence of what Noema observed.

It does not replace the enterprise ledger or become current enterprise truth.

⸻

39. Snapshot vs Live Query

Noema may use either:

snapshot

or:

live query

depending on the Action’s requirements.

High-risk operations may require a fresh query immediately before execution or enterprise-side conditional enforcement.

⸻

40. Business State and TOCTOU

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
resource versions
reservations / leases where supported

The enterprise system should enforce authoritative invariants.

⸻

41. Enterprise Invariants

Business systems may enforce invariants such as:

balance cannot become negative
order cannot be cancelled after shipment
invoice cannot be paid twice
card cannot be simultaneously ACTIVE and BLOCKED

Noema should respect these invariants rather than attempting to become an independent authority over them.

Where possible, critical invariants should also be enforced by the enterprise at execution time.

⸻

42. Noema Must Not Become a Shadow Ledger

A dangerous architectural failure would be:

Enterprise Ledger
        +
Noema Ledger
        ↓
Two competing truths

Noema should not maintain a parallel authoritative copy of critical financial or business state merely for convenience.

It may maintain observations, evidence, cached data, or historical references required for execution and audit.

These remain distinct from enterprise authority.

⸻

43. Cached Business State

Caching may still be useful.

For example:

cached customer tier
cached capabilities
cached metadata
cached resource representation

But cached values must be treated according to their freshness and authority requirements.

A cache is not automatically authoritative.

⸻

44. Business State and Permissions

Permissions are enterprise authorization state or related enterprise domain state depending on the enterprise architecture.

Examples:

user.role
user.permissions
account.access_level

Noema should consume the enterprise’s authoritative authorization semantics.

It should not invent a parallel permission model that overrides the enterprise.

⸻

45. Business State and Capability

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

Capability availability is not itself Business State.

⸻

46. Business State and Resource Availability

Some resources are stateful.

Example:

Warehouse inventory:
SKU-123 = 4 units

An Action:

ship 3 units

depends on that state.

If the inventory changes before execution, Trust or the enterprise system must prevent an invalid operation.

⸻

47. Business State and Human Intent

Users often refer to Business State implicitly.

Example:

"Cancel my pending order."

Noema must determine:

Which order?
Is it pending?
Can pending orders be cancelled?

These questions require Business State observations and, where necessary, State Reconciliation.

⸻

48. Business State and Intent Resolution

Business State may disambiguate Intent.

Example:

User:
"Cancel my order."
Enterprise state:
Order A — CANCELLED
Order B — SHIPPED
Order C — PENDING

Noema may use this state as evidence for candidate resolution.

However, consequential ambiguity must still be handled explicitly.

Business State can support resolution; it does not authorize Noema to guess.

⸻

49. Business State and Historical Context

Current Business State is not always enough.

Some Actions depend on history.

Examples:

number_of_refunds_in_last_30_days
previous_approvals
transaction_velocity
prior_failed_attempts

Noema may retrieve historical enterprise information as Context.

The underlying history remains enterprise-owned.

⸻

50. Business State and Temporal Context

Some state is valid only within a time period.

Examples:

promotion active until midnight
authorization expires at 18:00
account temporarily restricted

Trust must evaluate state relative to the relevant claim, action, and execution time.

Temporal validity does not override authority.

⸻

51. Business State and Multi-System Domains

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

52. Distributed Business State

Distributed state introduces challenges:

system A:
UPDATED
system B:
PENDING
system C:
FAILED

Noema should not manufacture a fictional unified state.

Instead, it should model the relevant observations, authorities, scopes, and reconciliation results.

Where a unified business interpretation is required, it must be explicitly defined by enterprise domain semantics.

⸻

53. Business State and Execution Saga

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

54. Business State and Compensation

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

55. Business State and Auditability

Auditability should record relevant observations of Business State without pretending to own them.

Example:

Trust evaluated at 14:02
Observed:
account.status = ACTIVE
source:
Banking API
observed_at:
14:02:04
Fact Status:
VERIFIED

Later:

account.status = FROZEN

The historical observation remains part of the audit trail.

⸻

56. Historical State Must Not Be Rewritten

If the enterprise state changes:

14:00:
ACTIVE
14:10:
FROZEN

the audit record of the 14:00 observation must not become:

FROZEN

It must remain historically accurate.

Historical snapshots describe what was observed at the relevant time.

They do not establish current truth.

⸻

57. Business State and Trust

Trust uses Business State observations and reconciled facts as inputs.

Business State
       ↓
Observation
       ↓
State Reconciliation
       ↓
Fact Status
       ↓
Trust Evaluation
       ↓
Decision

The Trust decision must identify important state observations and reconciliation results used to reach it.

⸻

58. Business State and Action Eligibility

Business State can determine whether an Action is currently eligible.

Example:

Action:
cancel_order(order_123)
Business State:
order.status = SHIPPED

If policy says shipped orders cannot be cancelled:

Trust:
REJECT

The state observation supporting the decision must remain attributable.

⸻

59. Business State and Policy Versioning

A historical decision may depend on both:

Business State at T1
+
Policy version N

An auditor must be able to distinguish this from:

Business State at T2
+
Policy version N+1

Neither historical state nor historical policy should be silently replaced during reconstruction.

⸻

60. Business State Access

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

61. Business State Permissions

Noema’s ability to read Business State should itself be governed.

Noema
   ↓
Enterprise authorization
   ↓
Read permitted?

Noema should receive only the state required for the relevant operation.

Access to Business State can itself be consequential when it exposes protected information.

⸻

62. Data Minimization

Noema should not ingest an entire enterprise database simply because it can.

The canonical principle is:

Retrieve the minimum Business State necessary to resolve, reconcile, trust, execute, or verify the current Action.

⸻

63. Sensitive Business State

Business State may contain highly sensitive information.

Examples include:

financial information
identity information
employment information
customer information
internal operational data

Access, retention, storage, and exposure must follow enterprise policy.

⸻

64. Business State and Tenant Isolation

Business State must always remain tenant-scoped where applicable.

An Action belonging to:

Tenant A

must not accidentally retrieve or act upon:

Tenant B

This boundary should be enforced through integration, identity, scope, and Trust controls.

⸻

65. Business State and Idempotency

Business State can help determine whether an Action has already taken effect.

Example:

Action:
refund payment
Current state:
payment.status = REFUNDED

Noema may determine that another refund should not be issued.

However, enterprise-side idempotency remains preferable where available.

State observation alone must not be treated as a substitute for atomic idempotency guarantees.

⸻

66. Business State and Concurrency

Multiple actors may change the same resource.

User A → update account
User B → freeze account
Agent C → close account

Noema must not assume exclusive ownership of the resource.

Enterprise systems should enforce concurrency and state-transition invariants.

⸻

67. Optimistic Concurrency

Where supported, Noema may provide:

version = 42

with an Action:

update_resource(expected_version=42)

The enterprise system can reject the operation if the state has changed.

This is preferable to Noema assuming that an old observation remains valid.

⸻

68. Business State and Preconditions at Execution

Preconditions may be checked:

during Trust

but some conditions should also be enforced:

at execution time

This is especially important when state can change between Trust and Execution.

Noema should prefer enterprise-side atomic enforcement where supported.

⸻

69. Business State Authority Hierarchy

Where necessary, Noema should know:

Primary authoritative source
        ↓
Secondary source
        ↓
Cached observation
        ↓
Derived observation
        ↓
Model inference

This is not a universal hierarchy in which every primary source always dominates every other source.

Authority is claim-specific and defined by enterprise domain semantics.

Consequential decisions should use the appropriate authoritative source where available.

⸻

70. Derived Business State

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

71. Business State and Model Inference

An LLM may infer:

"John is probably the customer's manager."

That is not automatically Business State.

Inference should not be promoted into authoritative enterprise fact without an appropriate source, explicit enterprise rule, or required confirmation.

⸻

72. Business State Must Be Grounded

For consequential execution:

Model inference
       ≠
Business State

Instead:

Enterprise source
       ↓
Observation
       ↓
State Reconciliation
       ↓
Business Fact / Fact Status
       ↓
Context / Trust

The model may help identify what state needs to be retrieved.

It does not establish the enterprise state itself.

⸻

73. Business State and Knowledge State

Noema must distinguish enterprise domain truth from Noema’s knowledge of that truth.

For example:

Enterprise domain state:
refund = SUCCEEDED
Noema knowledge state:
UNKNOWN
Reason:
authoritative observation unavailable

Later:

Authoritative observation:
refund = SUCCEEDED
Fact Status:
VERIFIED

What is true in the enterprise and what Noema knew at a particular time are different temporal dimensions.

⸻

74. Business State and Temporal State

Business State is temporal.

A state claim must be interpreted relative to:

observed_at
effective_at
received_at
recorded_at
validity window
resource version

The exact temporal dimensions depend on the enterprise system.

Noema must not collapse observation time, enterprise effective time, and Noema recording time into one timestamp.

⸻

75. Business State and Unknown

Unknown is a legitimate state of Noema’s knowledge about Business State.

For example:

Enterprise state:
exists
Noema knowledge:
UNKNOWN

This does not mean:

enterprise state = UNKNOWN

It means Noema cannot currently establish the relevant enterprise state.

Unknown must not be silently converted into:

false
success
failure
safe
authorized

⸻

76. Business State and Capability

Business State does not determine the entire execution boundary.

A valid operation may require all of:

Business State
+
Capability
+
Action Contract
+
Authorization
+
Policy
+
Trust decision

No single dimension can substitute for the others.

⸻

77. Business State and the Enterprise Action Graph

The Enterprise Action Graph describes executable relationships among enterprise capabilities, resources, systems, and workflows.

Business State supplies current observations about those resources and systems.

Conceptually:

Enterprise Action Graph
        +
Business State
        ↓
Candidate executable path
        ↓
Trust
        ↓
Action

The graph does not become Business State.

Business State does not create new graph capabilities.

⸻

78. Business State and Planner Boundaries

The Planner may use Business State observations to select among permitted execution paths.

However, it cannot use Business State to:

invent capabilities
invent authority
modify Action Contracts
bypass Trust

Temporal persistence of a plan does not create permission to execute it.

⸻

79. Business State and Auditability

Auditability should establish:

what Business State was observed
which source provided it
when it was observed
what validation occurred
how it was reconciled
what Fact Status resulted
which Trust decision relied upon it

This allows an auditor to reconstruct what Noema knew without confusing that knowledge with current enterprise truth.

⸻

80. Business State and Operational Memory

Operational Memory may retain structured historical information about enterprise observations and execution cases.

It must not become:

a replacement for current enterprise state
a shadow ledger
an authorization source
a generic AI memory store

Historical operational knowledge may help future execution, but consequential current state should be re-established through appropriate enterprise observation and State Reconciliation.

⸻

81. Business State and Read-Only Operations

Read-only does not mean non-consequential.

Retrieving protected Business State may itself have material consequences.

For example:

customer financial information
employee records
account information
security-sensitive configuration

may require authorization and Trust even when Noema performs no enterprise write.

⸻

82. Business State and Security Boundary

Business State access must preserve the Noema security boundary.

The model must not receive unrestricted credentials or direct enterprise access.

Instead:

Model
   ↓
proposes information needed
   ↓
validated Intent / Context request
   ↓
registered capability
   ↓
enterprise integration
   ↓
Business State observation

Retrieved data remains subject to validation, scope, authorization, and classification.

⸻

83. Business State and Noema’s Moat

Noema does not need to own the enterprise data to create value.

Its value lies in understanding how to:

discover relevant state
resolve relevant resources
reconcile observations
interpret state in context
evaluate it against policy
reason about freshness
construct bounded Actions
execute through enterprise capabilities
verify outcomes
recover from uncertainty

This makes the trusted execution journey the product rather than another database.

⸻

84. Canonical Relationship

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
        Enterprise Observations
                │
                ▼
        Hard Schema Validation
                │
                ▼
       State Reconciliation
                │
          ┌─────┴─────┐
          ▼           ▼
       Evidence   Fact Status
          │           │
          └─────┬─────┘
                ▼
              Noema
┌─────────────────────────────────┐
│ Context                         │
│ Intent Resolution               │
│ Trust                           │
│ Action                          │
│ Execution                       │
│ Verification                   │
│ Audit                           │
│ Outcome                         │
└─────────────────────────────────┘

⸻

85. Canonical Flow

Enterprise Business State
          │
          ▼
     Observation
          │
          ▼
Hard Schema Validation / Admission
          │
          ▼
State Reconciliation
          │
          ├───────────────┐
          ▼               ▼
      Evidence        Fact Status
          │               │
          └───────┬───────┘
                  ▼
               Context
                  │
          ┌───────┴────────┐
          ▼                ▼
 Intent Resolution       Trust
          │                │
          └───────┬────────┘
                  ▼
                Action
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
              Verification
                  │
                  ▼
               Outcome
                  │
                  ▼
        Operational Memory

⸻

86. Canonical Boundary

The fundamental boundary is:

ENTERPRISE OWNS
────────────────────────────────
Business State
Systems of Record
Domain Invariants
Enterprise Authority
Enterprise Permissions
Enterprise Resources
Enterprise Business History
NOEMA OWNS
────────────────────────────────
Intent
Intent Versions
Resolution
Trust Decisions
Action State
Execution State
Verification History
Noema Outcomes
Intervention / Case State
Audit
Operational Memory

Noema may reference enterprise state throughout its execution journey without assuming ownership of it.

⸻

87. Canonical Invariants

Invariant 1

The enterprise remains authoritative for Business State.

Invariant 2

Noema owns the execution journey, not the underlying business state.

Invariant 3

Noema must not create a competing system of record for critical enterprise state.

Invariant 4

Business State observations must be attributable to an appropriate enterprise source where possible.

Invariant 5

External Business State inputs must pass the relevant hard schema validation and admission boundary before becoming eligible canonical Noema input.

Invariant 6

Persistence of unvalidated data must not make that data authoritative.

Invariant 7

State Reconciliation must be a first-class operation between enterprise observations and reconciled facts or state used by Noema.

Invariant 8

Fact Status must remain distinct from Evidence, Context, Business State, and Outcome.

Invariant 9

Canonicality must remain scoped to the relevant claim, domain, resource, authority, tenant, and temporal semantics.

Invariant 10

Source identity, authority, freshness, and authorization must remain distinct concepts.

Invariant 11

State freshness must be considered whenever stale information could produce unsafe execution.

Invariant 12

Historical observations must remain historically accurate.

Invariant 13

Noema must not silently convert model inference into authoritative Business State.

Invariant 14

Model confidence must never substitute for Business State, Fact Status, evidence authority, or authorization.

Invariant 15

Conflicting authoritative state must not be resolved through arbitrary guessing.

Invariant 16

Enterprise invariants remain enforced by the enterprise system.

Invariant 17

Noema should interact with Business State through approved interfaces rather than bypassing domain ownership.

Invariant 18

Business State used for consequential Trust decisions must be sufficiently authoritative and fresh for the operation.

Invariant 19

Execution success does not imply that the desired Business State was achieved.

Invariant 20

Outcome verification may require observing Business State after execution.

Invariant 21

Business State access must respect authorization, tenant isolation, scope, and data-minimization requirements.

Invariant 22

Cached Business State must not be treated as authoritative merely because it exists inside Noema.

Invariant 23

Distributed Business State must preserve source and domain authority rather than being collapsed into an artificial single truth.

Invariant 24

Noema must account for state changes between Trust evaluation and execution.

Invariant 25

Where possible, authoritative enterprise systems should enforce critical state invariants at execution time.

Invariant 26

Noema may record Business State observations as evidence without becoming the owner of that state.

Invariant 27

A Noema audit trail must distinguish observed Business State from Noema-owned execution state.

Invariant 28

Unknown must remain distinct from false, failure, success, authorization, or any other established Business State.

Invariant 29

Noema knowledge state must remain distinct from enterprise domain truth.

Invariant 30

Historical snapshots and Context snapshots must not become current enterprise truth merely because Noema stores them.

Invariant 31

Temporal recency alone must not establish authority.

Invariant 32

Business State used in consequential execution must preserve the relevant observation time, authority, scope, and resource version where applicable.

Invariant 33

Intent resolution may use Business State as evidence, but Business State must not be used to silently resolve consequential ambiguity without sufficient deterministic grounds.

Invariant 34

Business State does not create capabilities, permissions, or authority that are not otherwise established.

Invariant 35

Action selection remains bounded by the Enterprise Action Graph, Capability Registry, and registered Action Contracts.

Invariant 36

Planner persistence must not create authority or executable capability.

Invariant 37

Read-only access to protected Business State may itself be consequential and require Trust.

Invariant 38

Operational Memory must not become a substitute for current enterprise Business State.

Invariant 39

Recovery from uncertain execution must use appropriate verification and State Reconciliation before consequential retry where required.

Invariant 40

Noema must not directly mutate enterprise Business State outside approved enterprise capabilities and integrations.

Invariant 41

Compensation is an additional enterprise Action, not restoration of Noema’s internal state.

Invariant 42

Business State and Noema Outcomes must remain separate even when an Outcome is established from Business State verification.

Invariant 43

Historical Business State observations must not be rewritten to reflect later enterprise state.

Invariant 44

Noema must preserve enough temporal and provenance information to reconstruct the Business State it relied upon at a consequential decision point.

Invariant 45

Enterprise Business State remains the authority for the world Noema operates on; Noema remains the authority for the execution journey it owns.

⸻

88. Final Definition

Business State is the authoritative condition of the enterprise’s entities, resources, and domain systems. Noema observes and uses Business State as input to Intent resolution, State Reconciliation, Context, Trust, Action construction, execution, and Outcome verification, while leaving ownership and authority over that state with the enterprise systems that maintain it.

The architectural boundary is:

                    NOEMA
      ┌────────────────────────────┐
      │                            │
      │ Intent                     │
      │ Intent Resolution          │
      │ Context                    │
      │ State Reconciliation       │
      │ Trust                      │
      │ Action                     │
      │ Execution                  │
      │ Verification               │
      │ Audit                      │
      │ Outcome                    │
      │ Operational Memory         │
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

The enterprise remains authoritative for what is true in its business domain.

Noema remains authoritative for the execution-domain history of how it interpreted Intent, reconciled observations, evaluated Trust, selected bounded Actions, executed them, verified results, and established Outcomes.