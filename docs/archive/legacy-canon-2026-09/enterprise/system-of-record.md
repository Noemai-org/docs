> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

System of Record

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/system-of-record.md

⸻

1. Definition

A System of Record (SoR) is the authoritative enterprise system responsible for maintaining the canonical state of a particular business domain, resource, or claim within a defined scope.

The System of Record concept establishes a critical boundary for Noema:

Noema may understand, reconcile, orchestrate, observe, and act upon enterprise state without becoming the authoritative owner of that Business State.

Examples:

CRM
→ customer record
Ledger
→ financial balance
HRIS
→ employee status
IAM
→ identity and permissions
Inventory System
→ inventory state

Noema integrates with these systems rather than replacing them.

⸻

2. Purpose

The purpose of this concept is to prevent Noema from becoming a shadow System of Record for enterprise Business State.

Noema necessarily maintains state about its own execution domain:

Intent
Trust Decision
Action
Execution
Verification
Outcome
Intervention
Audit
Operational Memory

That state is distinct from the underlying enterprise Business State:

Customer
Account
Balance
Employee
Invoice
Order
Inventory
Payment

The distinction must remain explicit.

⸻

3. Core Principle

The enterprise owns authoritative Business State; Noema owns and canonically manages its execution-domain state.

Conceptually:

ENTERPRISE
────────────────────────────────
Business State / Business Truth
customer
account
balance
invoice
order
employee
inventory
payment
subscription
NOEMA
────────────────────────────────
Execution-Domain State
intent
resolution
trust
action
execution
verification
outcome record
intervention
audit
operational memory

Noema’s execution-domain Outcome records describe what Noema observed or established about an execution. They do not automatically become the authoritative enterprise Business State.

⸻

4. Business State

Business State is the authoritative state of an enterprise domain or resource.

Examples:

Account.balance = $10,000
Invoice.status = PAID
Employee.status = ACTIVE
Card.status = FROZEN
Order.status = SHIPPED
Payment.status = COMPLETED

The authoritative value belongs to the designated enterprise System of Record for the relevant claim.

Noema may cache, project, reconcile, or derive representations of these values, but those representations do not supersede the enterprise authority.

⸻

5. Execution-Domain State

Noema canonically manages facts about the execution journey it operates.

Examples:

Intent received at 10:42
Intent resolved at 10:43
Trust decision = EXECUTE
Action submitted
Execution timed out
Execution state = UNKNOWN
Verification completed
Human intervention requested

These are Noema execution-domain facts.

An enterprise System of Record does not necessarily know or own this complete causal journey.

⸻

6. System of Record vs Noema State

Consider:

Intent:
"Refund my last payment."

Noema may record:

intent_id = 123
intent_version = 2
action = refund_payment
trust_decision = EXECUTE
execution_status = COMPLETED

The payment system remains authoritative for:

payment.status
refund.status
refund.amount
transaction_id

Noema’s:

execution_status = COMPLETED

does not replace the payment system’s record of the actual financial state.

Execution completion and enterprise Business State are related but distinct.

⸻

7. One Fact, One Authority

Where possible, every consequential enterprise claim should have a clearly defined authoritative source.

Examples:

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

Noema should know where the relevant enterprise truth is authoritative.

This does not require one universal System of Record for the entire enterprise.

⸻

8. Authority Is Domain- and Claim-Specific

There is not necessarily one enterprise-wide System of Record.

Different domains, resources, and claims may have different authorities.

                 ENTERPRISE
        ┌──────────┼──────────┬──────────┐
        ▼          ▼          ▼          ▼
    Identity     Finance      HR      Inventory
        │          │          │          │
        ▼          ▼          ▼          ▼
       IAM       Ledger       HRIS       ERP

Authority may be scoped further by:

claim
resource
tenant
legal entity
organization
environment
time

Noema must preserve these boundaries when determining which source is authoritative for a consequential decision.

⸻

9. Source of Truth vs Source of Evidence

These concepts must not be conflated.

System of Record

The authoritative enterprise source for a defined claim or category of Business State.

Source of Evidence

A system that provides information useful for reasoning, discovery, reconciliation, or verification.

For example:

CRM
→ customer information
Payment System
→ authoritative payment state

The CRM may provide evidence about the customer while not being authoritative for the payment.

A source can therefore be useful evidence without being the System of Record for the claim under evaluation.

⸻

10. Enterprise APIs

An API is not automatically a System of Record.

An API is an interface through which Noema accesses an enterprise capability or system.

Conceptually:

API
 ↓
Service
 ↓
Business System
 ↓
Authoritative State

The underlying service or system may own the authoritative state.

Noema must therefore distinguish:

interface

from:

authority

An API response may be authoritative for a claim if the enterprise designates the underlying system as authoritative, but the interface itself does not establish authority.

⸻

11. Noema as an Execution System of Record

Noema may itself be the System of Record for certain execution-domain facts.

Examples:

execution_id
intent_id
action_id
trust_decision
execution_state
verification_state
intervention
execution_history

This is compatible with the enterprise boundary because these are facts about Noema’s execution domain.

Therefore:

Noema should not avoid becoming a System of Record entirely. It should become authoritative for the execution-domain state it owns while remaining non-authoritative for enterprise Business State it does not own.

⸻

12. Embedded Product Boundary

Noema is Trusted Enterprise Execution Infrastructure embedded into enterprise products and workflows.

Its relationship with Systems of Record therefore depends on the operating mode.

Mode 1: Noema Full-Stack Execution

Source of Intent
      ↓
Noema
      ↓
Intent
      ↓
Trust
      ↓
Action
      ↓
Enterprise System of Record
      ↓
Verification

Mode 2: Independent Trust / Execution Boundary

Human / Agent / Enterprise Orchestrator
                ↓
        Existing Intent / Action Flow
                ↓
              Noema
                ↓
       Trust / Execution Boundary
                ↓
        Enterprise Systems

In both modes, Noema does not become the authoritative owner of the enterprise Business State merely because it participates in execution.

⸻

13. Execution Journey

The execution journey can be modeled as:

Source of Intent
      ↓
Interpretation
      ↓
Candidate Intent
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolution
      ↓
Context / State Reconciliation
      ↓
Trust
      ↓
Action Graph / Planning
      ↓
Action Contract
      ↓
Execution
      ↓
Verification
      ↓
Outcome
      ↓
Audit / Operational Memory

Noema should preserve this history as a coherent causal record.

⸻

14. Business State Must Remain External

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

Noema should not maintain a competing authoritative:

Noema:
card.status = FROZEN

as Business State.

It may retain an observation or reference to that state as part of execution context, evidence, audit, or Operational Memory.

⸻

15. Cached Enterprise State

Noema may cache enterprise state for performance.

Example:

Customer:
id = 123
status = ACTIVE

A Noema cache is:

derived

not:

authoritative

unless the enterprise explicitly designates that cache or projection as authoritative for the relevant claim.

Cached representations should have an explicit freshness and provenance model.

⸻

16. Stale State

Consider:

Noema cache:
account.balance = $5,000
Enterprise Ledger:
account.balance = $2,000

The ledger is authoritative for the balance.

Noema must never treat stale cached state as authoritative merely because it has a locally stored value.

If freshness is insufficient for the intended Action, Noema must reconcile or obtain current authoritative state before proceeding.

⸻

17. Read-After-Write

After consequential execution, Noema may need to verify the resulting Business State against the relevant System of Record.

Conceptually:

Action
  ↓
Enterprise Mutation
  ↓
Query System of Record
  ↓
Verify Postcondition
  ↓
Noema Outcome

This is particularly important where execution responses are asynchronous, delayed, partial, or ambiguous.

⸻

18. Unknown Outcome

A critical case is:

Noema
   ↓
POST /refund
   ↓
timeout

Noema cannot safely conclude:

refund failed

The request may have succeeded.

The execution state may instead be:

UNKNOWN

Noema should reconcile against the appropriate System of Record before retrying or declaring a definitive business outcome.

⸻

19. Reconciliation

State Reconciliation is a first-class Noema platform capability.

It reconciles observations from enterprise systems into an explicit representation of the currently supported enterprise claims and their epistemic status.

Conceptually:

Enterprise Systems of Record
          ↓
Observations
          ↓
Hard Schema Validation / Admission
          ↓
State Reconciliation
          ↓
Reconciled Facts / Fact Status / Evidence
          ↓
Context
          ↓
Trust

For example:

Noema:
refund request submitted
execution outcome = UNKNOWN
        ↓ reconcile
Payment System:
refund completed
        ↓
Noema:
execution outcome = CONFIRMED_SUCCESS

The payment system remains authoritative for the refund itself.

Reconciliation does not transfer ownership of Business State to Noema.

⸻

20. Fact Status

Fact Status must remain distinct from Evidence, Context, Business State, Outcome, and model confidence.

Relevant values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Claim:
payment.status = COMPLETED
Source:
Payment System
Evidence:
payment status response
Fact Status:
VERIFIED

A cached response may instead produce:

Fact Status:
STALE

A conflict between authoritative sources may produce:

Fact Status:
CONFLICTED

Noema must not use model confidence as a substitute for Fact Status.

⸻

21. System-of-Record Discovery

Noema may need to determine:

“Which system is authoritative for this claim?”

This information may come from:

Enterprise configuration
Integration metadata
Action Contract
API documentation
Enterprise Action Graph
Human configuration
System metadata

Noema must not infer authority merely from whichever system happens to return data first.

Authority must be explicitly represented or established through enterprise-defined semantics.

⸻

22. Provenance

Consequential enterprise observations should retain provenance.

Conceptually:

Observation {
    claim
    value
    source
    authority
    observed_at
    effective_at
    version
    schema_version
    provenance
}

Example:

balance = $5,000
source = Ledger
authority = authoritative
observed_at = 10:32:04
version = 4812

This allows Noema to distinguish authoritative observations from secondary or stale information.

⸻

23. Authority Model

When multiple sources provide information about the same claim, Noema needs an explicit authority model.

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

A conflict must not be resolved through model preference, frequency, semantic plausibility, or recency alone.

It must be resolved according to explicitly defined authority semantics.

⸻

24. Conflicting Systems

Suppose:

CRM:
customer.status = ACTIVE
Billing:
customer.status = SUSPENDED

Noema must not simply select:

ACTIVE

because it appears more frequently or semantically plausible.

The relevant domain and claim authority must be established.

If authority cannot be established and the claim is consequential, the state should remain explicitly:

CONFLICTED

or:

UNKNOWN

as appropriate.

The model must not arbitrate enterprise truth.

⸻

25. Authority Is Action- and Claim-Dependent

The authoritative system may depend on the fact being evaluated.

Example:

Customer name
→ CRM
Payment status
→ Payment System
Account balance
→ Ledger

The same resource may therefore have different authoritative systems for different claims.

Noema’s Enterprise Action Graph and integration metadata should represent these relationships where useful.

⸻

26. System of Record and Context

Context should preserve the provenance and authority of important enterprise information.

Conceptually:

Context
├── customer
│    └── source = CRM
│
├── payment
│    └── source = Payment System
│
└── balance
     └── source = Ledger

Where applicable, Context should also retain:

authority
observed_at
effective_at
version
Fact Status

This prevents Context from becoming an undifferentiated collection of potentially stale information.

⸻

27. System of Record and Trust

Trust should consider the authority and epistemic status of relevant enterprise evidence.

For example:

Evidence:
account.balance = $5,000
Source:
Ledger
Authority:
authoritative
Fact Status:
VERIFIED

is materially different from:

Evidence:
account.balance = $5,000
Source:
cached analytics database
Authority:
derived
Fact Status:
STALE

The distinction may determine whether a consequential Action can proceed.

Trust does not itself establish enterprise authority. It evaluates the available evidence and enterprise-defined constraints deterministically.

⸻

28. System of Record and Preconditions

Preconditions should be evaluated against the appropriate current enterprise state.

Example:

Precondition:
balance >= $1,000

For a financial Action, Noema should generally evaluate this against the authoritative financial source or an explicitly authorized, sufficiently fresh representation of that source.

A stale cache must not silently satisfy a precondition requiring current truth.

⸻

29. System of Record and Postconditions

Postconditions may require verification against the System of Record.

Example:

Action:
cancel_subscription
Postcondition:
subscription.status = CANCELLED

Verification:

Subscription System
→ status = CANCELLED

Noema can then record a confirmed execution outcome.

The subscription system remains authoritative for the subscription’s Business State.

⸻

30. System of Record and Action Contracts

An Action Contract should identify the enterprise capability and, where relevant, the authoritative system or authority source involved in execution and verification.

Conceptually:

ActionContract {
    action
    target
    capability
    preconditions
    execution
    postconditions
    authority_source
    verification_source
}

This helps Noema understand:

where execution occurs
where relevant state lives
where preconditions are evaluated
where postconditions are verified

An Action Contract does not transfer enterprise ownership of Business State to Noema.

⸻

31. System of Record and Integrations

Integrations should expose enough metadata to establish:

system identity
capability
resource ownership
authority
schema
version
consistency model

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

Integration metadata describes how Noema interacts with enterprise systems. It does not itself create enterprise authority.

⸻

32. System of Record and Events

Events may originate from the authoritative system.

Example:

Payment System
      ↓
payment.refunded
      ↓
Noema

The event can provide evidence about a state transition.

Noema should preserve, where required:

event source
event identity
event timestamp
event version
schema version
correlation

The event’s source and authority must remain explicit.

⸻

33. Events Are Not Automatically Current State

An event may be delayed, duplicated, reordered, replayed, or absent.

Therefore:

event received

does not necessarily mean:

current state = event payload

For consequential verification, Noema may need to query and reconcile against the System of Record.

Event absence is also not proof that the corresponding business occurrence did not happen.

⸻

34. Eventual Consistency

Enterprise architectures frequently contain:

primary database
read replicas
event streams
caches
search indexes
analytics systems
materialized views

These may temporarily disagree.

Noema must understand the consistency guarantees and authority semantics of the system it is interacting with.

A derived or eventually consistent view must not silently be treated as current authoritative state.

⸻

35. Derived Systems

Derived systems include:

search indexes
data warehouses
analytics databases
materialized views
caches
event projections

These are useful for discovery, Context, investigation, and reconciliation.

They should not be treated as authoritative unless the enterprise explicitly designates them as authoritative for the relevant claim.

⸻

36. Noema’s Own Database

Noema’s database may contain:

intent records
execution records
action records
trust decisions
verification records
audit records
integration metadata
reconciliation state
operational memory

This database may be authoritative for Noema-owned execution-domain concepts.

It is not automatically authoritative for:

accounts
payments
employees
customers
inventory
orders
balances

Noema’s persistence does not confer enterprise authority.

⸻

37. Shadow System of Record

A shadow System of Record occurs when Noema begins maintaining an independent authoritative representation of enterprise Business State.

For example:

Enterprise:
account.balance = $10,000
Noema:
account.balance = $10,000

If Noema subsequently maintains and mutates its own authoritative copy:

Noema:
account.balance = $8,000
Enterprise Ledger:
account.balance = $7,500

Noema has created competing Business Truth.

This should be avoided.

⸻

38. Why Shadow State Is Dangerous

Shadow Business State creates:

consistency problems
reconciliation complexity
stale data
authority conflicts
security exposure
duplicated business logic
operational complexity

It also moves Noema toward becoming another enterprise application rather than Trusted Enterprise Execution Infrastructure.

⸻

39. Reference vs Ownership

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

40. Enterprise Resource Identity

Enterprise resources should normally be referenced using stable enterprise identifiers.

Examples:

customer_id
account_id
invoice_id
payment_id
order_id
subscription_id

Noema should avoid inventing a second authoritative identity for the same enterprise resource unless there is a specific architectural need.

Noema may maintain its own execution identifiers that reference enterprise resources.

⸻

41. Tenant Boundaries

In multi-tenant environments:

Tenant A
   ↓
System of Record A
Tenant B
   ↓
System of Record B

Noema must maintain strict tenant isolation.

A resource from one tenant must never become accessible merely because another tenant has a similar identifier.

Tenant scope must be preserved in:

Context
Identity
Permissions
Authority
Execution
Audit
Operational Memory

⸻

42. Organizational Authority

A System of Record can establish organizational facts.

For example:

HRIS
→ employee belongs to Finance
IAM
→ employee has Finance Manager role

Noema consumes these facts when evaluating enterprise authority.

It must not manufacture organizational authority from behavioral patterns, model inference, or historical execution alone.

⸻

43. Human Configuration

Some enterprise authority relationships may not exist in machine-readable systems.

Example:

"All refunds above $10,000 require CFO approval."

Noema may ingest such configuration into its enterprise model.

The configuration should have, where appropriate:

owner
source
version
effective date
scope
provenance

Human configuration is not automatically authoritative merely because it has been entered into Noema. Its authority must be established by the enterprise governance model.

⸻

44. Hard Schema Validation and Admission

Enterprise data entering Noema must cross an explicit validation and admission boundary before being treated as a structured Noema input.

Conceptually:

Enterprise API / Event / Tool Response
              ↓
       Hard Schema Validation
              ↓
            Admission
              ↓
      Context / Evidence / State

The following must not become authoritative merely because they can be parsed:

model-generated claims
user-provided claims
retrieved enterprise text
tool output
external messages
unvalidated API payloads

Persistence also does not establish authority.

Authority comes from the enterprise source and its defined semantics.

⸻

45. Authority and Knowledge State

Enterprise truth and Noema’s current knowledge of that truth are distinct.

For example:

Enterprise:
refund.status = COMPLETED

while:

Noema:
knowledge state = UNKNOWN

may occur when the authoritative observation has not yet been received or reconciled.

Conversely, Noema may retain a historical observation that is no longer current.

Noema must represent this epistemic distinction explicitly rather than pretending that lack of knowledge changes enterprise truth.

⸻

46. Authority and Freshness

Authority and freshness are separate dimensions.

A source may be authoritative but its locally cached observation may be stale.

A recently received observation may also come from a non-authoritative source.

Therefore:

recent ≠ authoritative
authoritative ≠ necessarily current

Noema must evaluate both dimensions when current state matters.

⸻

47. System-of-Record Versioning

Where authority or resource state changes over time, Noema may need to preserve relevant versions.

Examples:

business/resource version
source assertion version
event version
schema/transport version
contract version
policy version
integration mapping version
graph/capability version

These version dimensions are distinct.

Historical execution records should preserve the versions necessary to reconstruct what authority and state were relied upon at the time.

⸻

48. Authority Changes

Enterprise architecture evolves.

A business may migrate:

CRM A
    ↓
CRM B

or:

Ledger A
    ↓
Ledger B

Noema must support changes in System-of-Record designation without requiring the core Intent model to change.

The authority mapping itself is versioned enterprise configuration.

⸻

49. Historical Authority

An old execution may have relied on:

System A

even though:

System B

is authoritative today.

Auditability therefore requires preserving enough provenance to determine which source was authoritative for the relevant claim at the time of execution.

Current authority must not be retroactively substituted into historical execution records.

⸻

50. System of Record and Auditability

A consequential audit record should be able to answer:

Which enterprise system supplied the relevant observation?
Which claim did it support?
Was that system authoritative for the claim?
What was the observation time?
What was the effective time?
What version or revision applied?
What was the Fact Status?
Was State Reconciliation performed?
Which Intent version was evaluated?
Which Trust Decision was made?
Was the state revalidated before execution?
Was postcondition verification performed?

This forms part of Noema’s causal audit trail.

⸻

51. System of Record and Determinism

Deterministic Trust requires deterministic authority resolution.

Noema must not do:

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
State observed / reconciled
       ↓
Fact Status established
       ↓
Trust evaluated

If authority cannot be established for a consequential claim, Noema must not guess.

The applicable Trust result may be:

CLARIFY
ESCALATE
REJECT

depending on the circumstances and enterprise policy.

⸻

52. System of Record and Failure

If the System of Record is unavailable:

GET /account/123
        ↓
timeout

Noema should not silently substitute arbitrary stale state for authoritative state when the Action requires current truth.

The resulting knowledge condition may be:

UNKNOWN

or another explicit operational condition.

Trust and policy determine whether execution can proceed.

⸻

53. Fail-Closed for Consequential Operations

For high-risk Actions:

authoritative state unavailable

should generally prevent execution unless enterprise Policy explicitly permits an alternative source or execution strategy.

This prevents Noema from crossing the enterprise boundary based on uncertain Business State.

Fail-closed is a policy/risk decision, not a universal semantic rule that every unavailable source must produce the Trust outcome REJECT.

⸻

54. System of Record and Offline Execution

Offline or delayed execution requires special care.

If:

Intent resolved at T1

but:

Action executes at T2

the authoritative Business State may have changed.

Action Preconditions may therefore need revalidation immediately before execution.

The earlier observation remains historically valid for the time it was observed but may no longer be sufficient for current execution.

⸻

55. System of Record and Concurrency

Two Noema executions may target the same enterprise resource.

Example:

Execution A:
withdraw $5,000
Execution B:
withdraw $5,000
Both observe:
balance = $10,000

If the enterprise System of Record supports transactional concurrency controls, Noema should rely on those mechanisms rather than attempting to recreate ledger semantics locally.

Useful enterprise mechanisms include:

transactions
resource versions
ETags
conditional writes
reservations
leases
idempotency keys
atomic business operations

⸻

56. System of Record and Idempotency

Idempotency belongs at the execution boundary.

Noema may maintain:

execution_id
idempotency_key

The enterprise System of Record or capability implementation should enforce the business semantics of duplicate operations where supported.

Noema’s execution record does not replace enterprise idempotency semantics.

⸻

57. System of Record and Compensation

Compensation should mutate Business State through the authoritative enterprise capability.

Noema should not directly manipulate a shadow representation to simulate rollback.

Conceptually:

Original Action
      ↓
Enterprise System
      ↓
Compensation Action
      ↓
Enterprise System

The compensation itself requires appropriate authorization and an explicit Action Contract.

⸻

58. System of Record and Recovery

Recovery decisions belong to Noema’s execution layer.

Business-state mutations remain enterprise-owned.

Noema:
retry
reconcile
verify
compensate
escalate
Enterprise:
apply actual Business State transition

For an unknown execution:

Historical execution state
        ↓
External operation state
        ↓
Current authoritative observation
        ↓
State Reconciliation
        ↓
Revalidate Trust / Preconditions
        ↓
Continue / Clarify / Escalate / Reject

Noema must not guess the result of an ambiguous enterprise operation.

⸻

59. Replay and Historical State

Replay of enterprise observations or events is non-executing by default.

Replaying:

historical event
historical observation
historical execution record

must not silently create a new enterprise business occurrence.

Historical authority, observations, Trust decisions, and execution records remain historical.

A modern reevaluation against current state is a separate operation and must not mutate the historical record.

⸻

60. Operational Memory

Noema may retain structured operational history about:

cases
executions
failures
interventions
reconciliation
verification
recovery

This Operational Memory is not a System of Record for enterprise Business State.

It is also not generic AI memory.

Its purpose is to preserve execution-domain knowledge and history useful for future operation, analysis, audit, and improvement.

⸻

61. Read-Only Operations

System-of-Record access is not consequential only when it mutates data.

A read-only operation may expose:

financial information
identity attributes
privileged organizational information
security information
regulated data

Therefore read-only access may require Trust, authorization, data-boundary evaluation, and appropriate auditability.

read-only ≠ non-consequential

⸻

62. System-of-Record Boundary

The boundary can be summarized as:

┌──────────────────────────────────────────────┐
│                  ENTERPRISE                  │
│                                              │
│            SYSTEMS OF RECORD                 │
│                                              │
│ Customer  Account  Ledger  HR  Orders       │
│     │        │       │      │      │         │
└─────┼────────┼───────┼──────┼──────┼─────────┘
      │        │       │      │      │
      └────────┴───────┼──────┴──────┘
                       │
                Enterprise Interfaces
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                   NOEMA                      │
│                                              │
│ Source → Intent → Trust → Action → Execute  │
│                                │             │
│                                ▼             │
│                           Verification       │
│                                │             │
│                                ▼             │
│                             Outcome          │
│                                              │
│       Execution-Domain System of Record     │
└──────────────────────────────────────────────┘

Noema crosses the enterprise boundary to perform governed Actions, but it does not thereby acquire ownership of enterprise Business State.

⸻

63. Canonical Architecture

The canonical relationship between Systems of Record and Noema is:

Enterprise Systems of Record
          ↓
Enterprise Observations
          ↓
Hard Schema Validation / Admission
          ↓
State Reconciliation
          ↓
Reconciled Facts
          ↓
Fact Status / Evidence
          ↓
Context
          ↓
Deterministic Trust
          ↓
Enterprise Action Graph / Planner
          ↓
Action Contract
          ↓
Enterprise Execution
          ↓
System of Record
          ↓
Verification
          ↓
Noema Outcome
          ↓
Audit / Operational Memory

This preserves the fundamental separation:

Enterprise
→ authoritative Business State
Noema
→ authoritative execution-domain state

⸻

64. Canonical Invariants

Invariant 1

Every consequential enterprise claim should have a clearly understood authoritative source where the enterprise architecture permits one to be defined.

Invariant 2

Noema must not become a shadow System of Record for enterprise Business State.

Invariant 3

Noema may be the System of Record for the execution-domain state it owns.

Invariant 4

Enterprise Business State remains authoritative within the appropriate enterprise System of Record.

Invariant 5

Cached or derived enterprise data is not authoritative unless explicitly designated as such for the relevant claim.

Invariant 6

Source of evidence and System of Record are distinct concepts.

Invariant 7

An API is an interface, not necessarily a System of Record.

Invariant 8

Authority is domain-, claim-, resource-, scope-, and time-specific.

Invariant 9

Authority may be Action-dependent.

Invariant 10

Conflicting sources must be resolved through explicit authority semantics, not model preference.

Invariant 11

Recency does not establish authority.

Invariant 12

Authoritative state should be revalidated when freshness materially affects execution safety.

Invariant 13

Unknown execution outcomes must be reconciled against the appropriate System of Record where possible.

Invariant 14

Events are observations or evidence of enterprise occurrences and do not automatically establish current Business State.

Invariant 15

Event absence does not prove non-occurrence.

Invariant 16

Noema must preserve provenance for consequential enterprise observations and execution decisions where required.

Invariant 17

Historical audit records must preserve enough information to identify the relevant authority and versions at the time of execution.

Invariant 18

If authoritative state is unavailable, Noema must not silently substitute uncertain state for high-risk execution.

Invariant 19

Noema should use enterprise transaction and concurrency semantics rather than recreating Business State management locally.

Invariant 20

Compensation and recovery must mutate Business State through authorized enterprise capabilities.

Invariant 21

Enterprise resource identity should remain anchored to enterprise identifiers.

Invariant 22

The boundary between enterprise Business Truth and Noema execution-domain state must remain explicit.

Invariant 23

Enterprise data must cross the appropriate hard schema validation and admission boundary before being used as structured Noema input.

Invariant 24

Persistence of an observation or response in Noema does not make that observation authoritative.

Invariant 25

Fact Status is distinct from Evidence, Context, Business State, Outcome, and model confidence.

Invariant 26

State Reconciliation is a first-class platform capability and must not be reduced to incidental integration behavior.

Invariant 27

Noema must preserve VERIFIED, UNVERIFIED, STALE, CONFLICTED, and UNKNOWN conditions where applicable rather than collapsing them into a binary truth value.

Invariant 28

Enterprise truth and Noema knowledge state must remain distinguishable.

Invariant 29

Model-generated claims cannot establish enterprise authority.

Invariant 30

Consequential decisions must reference the exact Intent Object version being evaluated.

Invariant 31

An admitted Intent is immutable; a material semantic change creates a new Intent version rather than silently changing historical meaning.

Invariant 32

Consequential execution requires the relevant actor, Action, target resource, and scope to be resolved sufficiently for deterministic authorization and Trust evaluation.

Invariant 33

The Enterprise Action Graph may represent authority relationships, but graph representation alone does not establish enterprise authority.

Invariant 34

The Planner cannot invent capabilities, authority, permissions, or Action Contract semantics.

Invariant 35

A Trust outcome of EXECUTE does not mean that enterprise execution or Business State transition has succeeded.

Invariant 36

Outcome records in Noema do not replace authoritative enterprise Business State.

Invariant 37

Unknown execution state must be reconciled before retrying a potentially completed consequential operation.

Invariant 38

Replay of observations or events must not silently create new enterprise business occurrences.

Invariant 39

Historical authority and state must not be retroactively replaced with current authority or state.

Invariant 40

Operational Memory is not enterprise Business State and does not become a shadow System of Record.

Invariant 41

Tenant and organizational boundaries must be preserved when accessing or reconciling Systems of Record.

Invariant 42

Read-only access may still be consequential and may require authorization, Trust, and auditability.

Invariant 43

Noema must not use arbitrary stale or secondary data as authoritative state when current enterprise truth is required.

Invariant 44

Noema must rely on explicit enterprise authority semantics rather than model inference when determining which system owns a consequential claim.

Invariant 45

System-of-Record metadata describes enterprise authority and integration semantics; it does not transfer ownership of Business State to Noema.

⸻

65. Final Definition

A System of Record is the authoritative enterprise source for a defined category of Business State or claim within a defined scope and time.

Noema integrates with Systems of Record to obtain authoritative observations, reconcile enterprise state, evaluate Trust, perform authorized Actions, and verify execution Outcomes while maintaining its own authoritative record of the execution-domain journey.

The architectural boundary is therefore:

ENTERPRISE
owns authoritative Business State
NOEMA
owns authoritative execution-domain state

More precisely:

Noema should know where enterprise truth lives, establish which observations are authoritative for the claim being evaluated, reconcile current state when required, use that state within deterministic Trust and governed execution, and verify the resulting enterprise state without quietly becoming the place where that Business State lives.

The fundamental rule is:

Enterprise
→ owns Business Truth
Noema
→ manages the journey through Intent, Trust, Action, Execution,
  Verification, Outcome, Audit, and Operational Memory

Noema therefore remains infrastructure for trusted enterprise execution rather than another owner of enterprise Business State.