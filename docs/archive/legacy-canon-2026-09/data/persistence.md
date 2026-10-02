> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Persistence

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/persistence.md

⸻

1. Definition

Persistence defines what Noema retains, why it retains it, how persisted information relates to enterprise state, and the guarantees required to reconstruct, audit, recover, reconcile, and safely operate an Intent execution.

Persistence answers:

“What must survive beyond the current runtime, and what guarantees must Noema provide about that information?”

Persistence is therefore not simply a database concern.

It is an execution, trust, recovery, reconciliation, and auditability concern.

Persistence gives Noema durable memory of its own execution domain without transferring ownership of enterprise Business State to Noema.

⸻

2. Purpose

Noema operates across potentially long-running and failure-prone workflows.

A process may:

receive Intent
      ↓
resolve Intent
      ↓
reconcile relevant state
      ↓
evaluate Trust
      ↓
execute Action
      ↓
lose network connectivity
      ↓
restart
      ↓
recover Execution
      ↓
reconcile current state
      ↓
verify Outcome

If relevant state existed only in process memory, Noema could lose the information required to safely continue.

Persistence provides continuity across:

* process restarts
* infrastructure failures
* retries
* asynchronous execution
* human intervention
* long-running workflows
* reconciliation
* auditing
* recovery
* deterministic reconstruction

⸻

3. Core Principle

Persist what Noema must remember to remain deterministic, recoverable, reconcilable, and accountable.

Noema should not persist everything simply because it can.

The persistence boundary should be driven by:

* operational requirements
* execution semantics
* trust requirements
* recovery requirements
* reconciliation requirements
* audit requirements
* enterprise retention requirements
* data minimization requirements

⸻

4. Persistence Is Not Business-State Ownership

A fundamental Noema boundary is:

Noema Persistence
        ≠
Enterprise System of Record

Noema may persist:

* Intent
* Intent versions
* Trust decisions
* Execution records
* Action metadata
* Evidence references
* Context snapshots
* Reconciliation records
* recovery state
* audit information
* intervention state
* operational history

while the enterprise remains authoritative for:

* accounts
* balances
* payments
* orders
* employees
* inventory
* business transactions
* other enterprise Business State

Persistence does not transfer authority merely because Noema stores a representation of information.

⸻

5. Persistence Model

Conceptually:

Enterprise Systems of Record
        │
        │ authoritative state
        ▼
Validated Integration / Observation
        │
        ▼
State Reconciliation
        │
        ▼
Noema Runtime
        │
        ▼
Noema Persistence

Noema Persistence records what Noema needs to operate, recover, reconcile, and explain its execution.

It does not become a shadow database for the enterprise.

⸻

6. Semantic Persistence Boundary

Persistence must preserve distinctions between:

Noema execution state
Enterprise Business State
Evidence
Fact Status
Context
Historical observation
Canonical Data Reference
Audit Record
Cache

These may be physically stored in the same infrastructure while remaining semantically different.

A database table does not determine semantic ownership.

⸻

7. What Noema Should Persist

The persistence layer should generally retain information required to reconstruct consequential execution.

This may include:

* Intent
* Intent lifecycle
* Intent versions
* resolved actor/action/target references
* Context snapshots
* Evidence references
* Fact Status
* State Reconciliation results
* Trust evaluations
* Trust state transitions
* policy references
* Action selections
* Action Contract versions
* Execution records
* Execution attempts
* idempotency information
* external operation identifiers
* failure information
* recovery state
* human intervention
* compensation state
* Outcome observations
* audit records
* causal relationships

The exact retention policy is implementation- and enterprise-dependent.

⸻

8. What Noema Should Generally Not Persist

Noema should avoid unnecessarily duplicating enterprise Business State.

For example, if the enterprise Ledger is authoritative for:

Account.balance

Noema generally should not maintain its own independently authoritative:

Account.balance

Instead, it may persist a scoped observation such as:

Claim:
Ledger reported balance = $10,000
Source:
Ledger
Observed:
2026-08-25T10:42:00Z

The persisted observation records what Noema observed.

It does not become a second System of Record.

⸻

9. Persistence Categories

A useful conceptual division is:

* Operational State
* Historical Record
* Evidence
* Fact
* Execution State
* Reconciliation Record
* Audit Record
* Reference
* Cache

These categories should not be conflated.

⸻

10. Operational State

Operational State represents information required for Noema to continue active work.

Examples:

Execution = RUNNING
retry_count = 2
waiting_for = PAYMENT_CONFIRMATION
next_action = VERIFY_REFUND

Operational State may be mutable.

It describes the current durable state of Noema’s own execution domain.

⸻

11. Historical Record

Historical Records preserve what happened.

Examples:

Intent received
Intent resolved
Trust evaluated
Action attempted
Policy evaluated
Human approved
Execution completed

Historical records should generally be append-oriented or otherwise protected against silent mutation.

⸻

12. Evidence Persistence

Noema may persist Evidence required to reconstruct why a decision was made.

For example:

Evidence:
Payment API reported status = SUCCEEDED

The persisted record should preserve sufficient provenance to determine:

* what was observed
* where it came from
* when it was observed
* under what scope it was observed
* what claim it supported
* which source or reference produced it

Evidence supports claims.

Evidence is not automatically truth.

⸻

13. Fact Status Persistence

Fact Status should be persisted where it materially affects Trust, execution, reconciliation, recovery, or audit.

Canonical Fact Status values are:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

Evidence
Context
State
Outcome
Canonical Data

A persisted fact may therefore look conceptually like:

Claim:
payment.status = SUCCEEDED
Fact Status:
VERIFIED
Evidence:
evidence_42
Observed At:
10:42

The status describes the evaluated state of the claim.

It does not turn every representation of that claim into enterprise truth.

⸻

14. Model Confidence Is Not Fact Status

Model confidence must not be persisted or interpreted as authoritative fact status.

For example:

model_confidence = 0.97

does not mean:

Fact Status = VERIFIED

Model confidence is interpretation metadata.

Fact Status is a semantic evaluation of a claim based on evidence, authority, freshness, reconciliation, and applicable rules.

⸻

15. Hard Schema Validation Before Persistence

External information must not become canonical Noema data merely because it was received.

Enterprise payloads, events, tool responses, and other external inputs are untrusted until they pass the applicable validation and admission boundary.

Conceptually:

External Input
      ↓
Schema Validation
      ↓
Semantic Validation / Classification
      ↓
Admission
      ↓
Persistence

Malformed or non-admitted data must not be persisted as authoritative canonical data.

Raw input may be retained for debugging or audit where explicitly permitted, but its status must remain distinguishable from admitted semantic data.

⸻

16. Persistence of Untrusted Inputs

Persistence may retain untrusted input when required for:

* debugging
* security investigation
* audit
* evaluation
* forensic analysis

However, retention does not upgrade its authority.

A persisted model response, user message, tool response, or external payload remains untrusted unless it has passed the appropriate semantic boundaries.

⸻

17. Execution Persistence

Every consequential Action should have a durable Execution identity.

Conceptually:

Execution {
    execution_id
    intent_id
    intent_version
    action
    target
    state
    attempts
    outcome
}

This allows Noema to recover an Execution after process failure.

The physical representation is implementation-dependent.

⸻

18. Intent Persistence

Intent may need to survive beyond the original request.

Example:

Intent
   ↓
Needs clarification
   ↓
User responds 4 hours later

The relevant Intent state must remain available.

The persisted Intent must preserve its semantic version.

⸻

19. Intent Version Persistence

Once an Intent is admitted to Trust, it is immutable.

A material change creates a new Intent version.

Example:

Intent v1
"Refund my last payment."
        ↓ clarification
Intent v2
"Refund payment #123."

Persistence must preserve:

v1
superseded_by → v2

Noema must not silently mutate the meaning of historical Intent.

⸻

20. Intent Lifecycle Persistence

Noema should persist meaningful Intent transitions.

Example:

RECEIVED
   ↓
INTERPRETING
   ↓
VALIDATING
   ↓
ADMITTED
   ↓
RESOLVING
   ↓
RESOLVED
   ↓
TRUST_PENDING
   ↓
READY_FOR_ACTION
   ↓
EXECUTING
   ↓
VERIFYING
   ↓
COMPLETED

The exact lifecycle is defined by the Intent Contract.

Persistence records its occurrence and history.

Intent lifecycle state must not be conflated with Trust outcomes or enterprise Business State.

⸻

21. Context Persistence

Context may need to be persisted when it is necessary to explain or resume an Execution.

However, Noema must distinguish:

Context Snapshot

from:

Enterprise Current State

A Context Snapshot describes what Noema had available at a particular point.

It does not automatically remain current.

⸻

22. Context Snapshot

Conceptually:

ContextSnapshot {
    snapshot_id
    execution_id
    captured_at
    identity
    relevant_resources
    relevant_state
    evidence_refs
    fact_status_refs
    policy_refs
    graph_version
}

This allows Noema to reconstruct the decision environment.

A snapshot is historical runtime context, not a shadow System of Record.

⸻

23. Snapshot vs Live State

This distinction is fundamental.

Snapshot:

Account.status = ACTIVE
observed_at = 10:30

Live Enterprise State:

Account.status = SUSPENDED
observed_at = 10:45

Both can be valid.

The first describes what Noema observed at 10:30.

The second describes the later enterprise observation.

Persistence must preserve temporal semantics rather than collapsing them into one mutable value.

⸻

24. Canonical Data References

Persistence may retain references to Canonical Data owned by an authoritative enterprise source.

Conceptually:

CanonicalDataReference {
    claim
    subject
    attribute
    value
    source_system
    authority_scope
    observed_at
    effective_at
    source_version
    freshness
    provenance
}

Canonicality is scoped.

A source may be authoritative for one claim within one domain and not authoritative for another.

⸻

25. Source, Authority, Freshness, and Authorization

Persistence must not collapse these dimensions.

They answer different questions:

Source:
Where did the information come from?
Authority:
Is this source authoritative for this claim within this scope?
Freshness:
How current is the observation?
Authorization:
Is this information or operation permitted to be accessed or used here?
Availability:
Can the information currently be obtained?

A source being available does not make it authoritative.

A source being authoritative does not mean the data is fresh.

A persisted reference does not grant authorization to access the underlying resource.

⸻

26. State Reconciliation Persistence

State Reconciliation is a first-class persistence concern.

Noema may receive observations from multiple enterprise systems:

Switch
Ledger
Payment Processor
Customer System
Operational System

Those observations may disagree, arrive out of order, or become stale.

Persistence should retain sufficient information to reconstruct the reconciliation process.

Conceptually:

StateReconciliation {
    subject
    observations[]
    authority_rules
    freshness_requirements
    result
    fact_status
    conflicts[]
    reconciled_at
}

⸻

27. Reconciliation Is Not Canonicality Creation

State Reconciliation does not invent authority.

It evaluates observations according to explicit:

* authority rules
* source scope
* temporal semantics
* freshness requirements
* conflict rules
* reconciliation policy

The result may be:

VERIFIED
CONFLICTED
UNKNOWN
STALE

where applicable.

Reconciliation selects an explicit interpretation of available observations.

It does not manufacture enterprise truth.

⸻

28. Persistence and Reconciliation

Reconciliation compares persisted observations and Noema expectations with current enterprise observations.

Example:

Persisted:
Execution = EXPECTED_SUCCESS
Enterprise:
Payment = SUCCEEDED
Result:
reconciled

Or:

Persisted:
Execution = EXPECTED_SUCCESS
Enterprise:
Payment = FAILED
Result:
discrepancy

The discrepancy must remain explicit until resolved.

⸻

29. Persistence and Unknown State

Unknown is first-class.

Persistence must be able to represent uncertainty for:

* values
* identity
* resources
* facts
* state
* reconciliation
* execution
* outcomes

NULL is not sufficient to express these semantics.

For example:

Outcome = UNKNOWN

must not be silently represented as:

Outcome = FAILED

or:

Outcome = SUCCESS

⸻

30. Unknown Execution Outcomes

One of the most important persistence requirements is preserving uncertainty.

Example:

Action submitted
      ↓
network timeout
      ↓
Outcome = UNKNOWN

Noema must persist:

UNKNOWN

unless the failure or success is subsequently established.

A timeout is an execution condition.

It is not automatically an Outcome.

⸻

31. Trust Persistence

Trust decisions should be persisted when they affect consequential execution.

For example:

Trust Decision:
EXECUTE

should be associated with:

* exact Intent version
* resolved actor
* resolved Action
* resolved target
* relevant Evidence
* Fact Status
* applicable Policy version
* Action Contract version
* graph/capability version where applicable
* decision timestamp
* decision validity
* decision context

⸻

32. Trust EXECUTE Is Not Success

Persistence must preserve the distinction:

Trust = EXECUTE

means:

The resolved execution path satisfied the applicable Trust conditions and may proceed.

It does not mean:

Action succeeded

Success is established through execution and verification.

Historical records must preserve these semantics.

⸻

33. Trust Decision Is Not Enterprise Policy

Noema may persist:

Trust Decision = EXECUTE

but that does not make Noema the owner of:

Enterprise Policy

The enterprise remains authoritative for its business policy semantics unless explicitly delegated otherwise.

Noema deterministically evaluates the applicable policy and trust conditions.

⸻

34. Policy Persistence

Noema may persist:

* policy identifier
* policy version
* policy evaluation result
* relevant policy inputs
* policy provenance

rather than necessarily storing the complete enterprise policy.

Where the policy itself is managed by Noema, persistence must retain the relevant version and lifecycle.

⸻

35. Action Persistence

Noema should persist enough information to determine which Action was selected.

Example:

Action:
refund_payment
Resource:
Payment #123
Action Contract:
refund_payment.v3

Action identity should remain stable enough for audit and recovery.

An Action refers to an explicitly registered capability, Action Contract, or Enterprise Action Graph operation.

It is not an arbitrary function generated by a model.

⸻

36. Planner Bounds

Persistence may record planner decisions, but persistence must not imply planner authority.

The Planner may select among:

* Enterprise Action Graph capabilities
* registered capabilities
* Action Contracts
* permitted execution paths

It may not:

* invent capabilities
* invent authority
* modify Action Contracts
* bypass Trust
* bypass schema validation
* directly execute arbitrary operations

Historical planner output must therefore remain subordinate to the deterministic execution boundary.

⸻

37. Action Contract Version

Execution records should preserve the Action Contract version used.

Example:

Action:
refund_payment
Contract:
v3

If the contract later changes to:

v4

historical executions must not silently appear to have used v4.

⸻

38. Execution Attempt Persistence

Each actual attempt should be distinguishable.

Execution #100
 ├── Attempt #1
 ├── Attempt #2
 └── Attempt #3

Each attempt may have:

* started_at
* completed_at
* request identity
* response reference
* failure
* timeout
* external operation ID
* retry decision
* verification status

⸻

39. Idempotency Persistence

Idempotency information must survive process restarts when the underlying Action requires it.

Conceptually:

Idempotency Key
      ↓
Execution
      ↓
Action

This prevents a restarted worker from interpreting an existing execution as new work.

Idempotency semantics belong to the Action and Execution contracts, not to persistence alone.

⸻

40. Persistence and Retries

Retries require durable knowledge of previous attempts.

Example:

Attempt 1
   ↓
timeout
   ↓
restart
   ↓
Attempt history recovered
   ↓
reconcile
   ↓
determine whether retry is safe

Without persistence and reconciliation, Noema may accidentally duplicate an Action.

⸻

41. Recovery

Persistence allows Noema to reconstruct an interrupted Execution.

Process
   ↓
crash
   ↓
Persistence
   ↓
recover Execution
   ↓
inspect state
   ↓
reconcile
   ↓
revalidate
   ↓
continue / retry / clarify / escalate

Recovery must not simply resume blindly from the last instruction.

⸻

42. Recovery Requires Revalidation

Persisted state is historical information.

It may no longer reflect current enterprise state.

Therefore:

Persisted Context
      ↓
Recovery
      ↓
State Reconciliation
      ↓
Current Context
      ↓
Trust Re-evaluation
      ↓
Permitted continuation

This is particularly important for Actions involving mutable resources.

⸻

43. Persistence and Determinism

Persistence contributes to deterministic behavior by preserving the inputs and decisions required to reconstruct execution.

Without persistence:

same Intent
+
unknown previous state
=
potentially different execution

With sufficient persistence:

Intent
+
historical state
+
Evidence
+
Fact Status
+
Policy version
+
Action Contract version
+
Execution history
=
recoverable decision

⸻

44. Persistence Does Not Guarantee Determinism

Persistence alone is insufficient.

Noema also requires:

* explicit state
* explicit policies
* explicit contracts
* explicit transitions
* explicit evidence
* deterministic reconciliation rules
* explicit authority
* explicit versioning

Persistence records those semantics.

It does not create them.

⸻

45. Event vs State Persistence

Noema should distinguish:

Event:
payment.refunded occurred

from:

State:
payment.status = REFUNDED

An event may be persisted as part of history.

Current enterprise state remains owned by the authoritative system.

A persisted event is not automatically a current canonical state assertion.

⸻

46. Events as Observations

Enterprise events are observations or occurrences.

They may contribute to State Reconciliation.

For example:

PaymentRefunded event
        ↓
observation
        ↓
State Reconciliation
        ↓
payment.status = REFUNDED
Fact Status = VERIFIED

The event itself does not automatically establish the final state.

Out-of-order events, missing events, duplicate events, and eventual consistency must remain representable.

⸻

47. Append-Oriented History

Consequential transitions should preferably produce append-oriented records.

For example:

Intent received
Intent resolved
Context captured
Evidence collected
Trust evaluated
Action selected
Attempt started
Attempt timed out
Reconciliation performed
Retry evaluated
Attempt completed
Outcome verified

This provides a durable execution history.

⸻

48. Event Sourcing Is Not Required

Noema may use event sourcing internally, but the semantic model does not require it.

The principle is:

Noema must preserve sufficient history to reconstruct consequential decisions, state transitions, reconciliation, and execution.

The underlying persistence technology is an implementation choice.

⸻

49. Transactional Boundaries

Persistence operations should have clear transactional semantics.

For example, when recording:

Execution → RUNNING

Noema must avoid states where:

Action dispatched

but:

Execution record does not exist

unless the architecture explicitly models and recovers that uncertainty.

⸻

50. Persistence and Action Dispatch

A critical distributed-systems problem is:

persist state
      +
dispatch Action

These may occur across different systems.

Noema must explicitly model the possibility that:

persistence succeeded
dispatch failed

or:

dispatch succeeded
persistence failed

The latter is especially dangerous because the external effect may exist without a corresponding local record.

Reconciliation and external operation identifiers are therefore essential.

⸻

51. Persistence and the Execution Boundary

Conceptually:

Intent
   ↓
Trust
   ↓
Persist Execution Identity
   ↓
Dispatch Action
   ↓
Observe / Reconcile
   ↓
Persist Outcome

The exact ordering depends on the execution architecture and delivery guarantees.

The semantic requirement is that Noema must explicitly model uncertainty around the dispatch boundary.

⸻

52. At-Least-Once Reality

Distributed execution commonly results in at-least-once delivery.

Therefore Noema must assume:

Action may be delivered more than once

unless stronger guarantees are explicitly established.

Idempotency and durable Execution identity are therefore fundamental.

⸻

53. Exactly-Once Claims

Noema should not casually claim exactly-once execution.

A system may provide:

exactly-once logical effect

through:

* idempotency
* deduplication
* transactional boundaries
* reconciliation

without literally guaranteeing exactly-once message delivery.

The distinction matters.

⸻

54. Persistence and Human Intervention

Human intervention may occur long after an Execution enters a blocked state.

Therefore the system may need to persist:

* reason for intervention
* relevant Evidence
* Fact Status
* current Noema state
* requested decision
* operator decision
* actor identity
* timestamp
* associated Intent and Execution versions

⸻

55. Persistence and Compensation

Compensation may depend on historical Execution state.

Example:

Action A:
charge payment → succeeded
Action B:
create subscription → failed

To determine whether compensation is required, Noema needs durable knowledge of Action A’s outcome.

Compensation itself must execute through authorized enterprise capabilities.

Noema should not compensate by mutating a local shadow copy of enterprise state.

⸻

56. Persistence and Auditability

Persistence is one of the foundations of auditability.

Noema should be able to answer:

* What did the source of intent provide?
* What did Noema understand?
* Which Intent version was admitted?
* What resources were identified?
* Which actor and target were resolved?
* What evidence was available?
* What was the Fact Status of relevant claims?
* Which enterprise source was authoritative?
* What state was reconciled?
* What policy applied?
* What Trust decision was made?
* Which Action Contract was selected?
* What attempts occurred?
* What changed?
* What was verified?
* What was the final Outcome?

⸻

57. Persistence and Explainability

The explanation of a consequential decision should be reconstructible from persisted records.

Conceptually:

Intent
  ↓
Resolution
  ↓
Evidence
  ↓
Fact Status
  ↓
State Reconciliation
  ↓
Policy
  ↓
Trust Decision
  ↓
Action
  ↓
Execution
  ↓
Verification
  ↓
Outcome

This is causal traceability.

It does not require exposing private model chain-of-thought.

⸻

58. Persistence and Provenance

Persisted records should preserve references to the origin of important information.

For example:

Evidence #42
source = Payment System
observed_at = 10:42
source_version = 781
claim = payment.status = SUCCEEDED

This is more valuable than simply storing:

payment_status = succeeded

without provenance.

⸻

59. Persistence and Causal Audit

Where meaningful, Noema should preserve relationships such as:

Clarification caused by Ambiguity
Reconciliation caused by Conflicting Observations
Trust Re-evaluation caused by State Change
Retry caused by Recoverable Failure
Compensation caused by Partial Outcome
Escalation caused by Unresolved Unknown

This creates causal execution history rather than merely chronological logs.

⸻

60. Persistence and Versioning

Important Noema artifacts should be versionable where changes could affect execution semantics.

Examples:

* Intent version
* Context schema/version
* Trust Contract version
* Action Contract version
* Execution Contract version
* Policy version
* integration mapping version
* Enterprise Action Graph version
* capability registry version
* relevant data/source version

Historical executions must retain the versions relevant to their decisions.

⸻

61. Data Versioning vs Contract Versioning

Data versioning must not be confused with Contract Versioning.

For example:

Source Version:
Ledger snapshot 781
Observed At:
10:42
Effective At:
10:40

is different from:

Action Contract:
refund_payment.v3

Data versioning describes information or source state.

Contract versioning describes semantic contract behavior.

Both may need to be preserved.

⸻

62. Persistence and Schema Evolution

Noema’s persistence model will evolve.

Historical records should remain interpretable after schema changes.

Therefore Noema should consider:

* persistence schema version
* semantic object version
* contract version
* migration strategy
* backward compatibility
* historical interpretation

A schema migration must not silently alter historical semantic meaning.

⸻

63. Persistence and Migration

Migration must preserve semantic meaning.

For example:

Historical:
FAILED

must not become:

UNKNOWN

simply because a new schema uses different state definitions.

If semantic meaning genuinely changes, the migration must explicitly represent that change rather than silently rewriting history.

⸻

64. Persistence and Integration

Integration responses should not necessarily be persisted wholesale.

Noema should retain the information required to establish:

* claim
* provenance
* authority
* Fact Status
* reconciliation result
* decision
* execution
* audit

while minimizing unnecessary duplication.

⸻

65. Persistence and Data Minimization

Persistence should follow:

Store the minimum information required to preserve Noema’s operational, safety, recovery, reconciliation, and accountability guarantees.

This reduces:

* storage cost
* privacy exposure
* security surface
* data duplication
* retention burden

⸻

66. Persistence and Sensitive Enterprise Data

Persisting Evidence may expose sensitive enterprise information.

Therefore persistence must respect:

* authorization
* classification
* encryption
* retention
* tenant isolation
* organizational boundaries
* legal boundaries
* data residency

Noema’s need to explain a decision does not override enterprise data controls.

⸻

67. Tenant Isolation

Persisted Noema data must preserve tenant boundaries.

Tenant A
 └── Intent
     └── Execution
         └── Evidence
Tenant B
 └── Intent
     └── Execution
         └── Evidence

Cross-tenant access must be explicitly authorized.

Tenant identity should be part of the semantic scope of persisted records where applicable.

⸻

68. Organizational Isolation

The same principle applies within an enterprise.

Noema must respect:

* organization
* business unit
* environment
* legal entity
* regional boundary
* data domain

when persistence contains data derived from those boundaries.

⸻

69. Persistence and Access Control

Persistence itself must not become an authorization bypass.

A user authorized to execute:

refund_payment

does not necessarily have access to:

* all historical Evidence
* all tenant data
* all Execution records
* all Context snapshots

Access to persisted information must be separately governed.

Technical, policy, and business authorization remain distinct.

⸻

70. Persistence and Deletion

Deletion requirements may conflict with audit requirements.

Noema should distinguish:

business deletion

from:

audit retention

and apply explicit retention policies.

Where records cannot be deleted due to legal or audit requirements, access must still be appropriately controlled.

⸻

71. Retention

Retention should be defined according to:

* record type
* enterprise policy
* legal requirements
* operational requirements
* audit requirements
* data classification
* Action risk

Not all Noema data requires the same retention period.

⸻

72. Expiration

Temporary operational data may have shorter lifetimes.

Examples:

* temporary Context
* ephemeral cache
* short-lived authorization evidence
* transient integration response

Expiration must not accidentally remove information required to reconstruct a consequential decision.

⸻

73. Cache vs Persistence

A cache is not a durable source of truth.

Cache:
optimization
Persistence:
durable operational/history requirement

If an Execution depends on a value surviving a restart, that value should not exist only in cache.

A cache must never silently become the only representation of a consequential execution fact.

⸻

74. Persistence and Current State

Persisted Noema state can represent:

what Noema currently believes about its own Execution

It should not be interpreted as:

current enterprise Business State

without appropriate State Reconciliation.

⸻

75. Persistence and Recovery State Machine

A recoverable Execution may conceptually move through:

RUNNING
   ↓
INTERRUPTED
   ↓
RECOVERING
   ↓
RECONCILING
   ↓
REVALIDATING
   ↓
RESUMING

or:

RECOVERING
   ↓
ESCALATED

Persistence makes these states durable.

⸻

76. Persistence and Concurrency

Multiple workers may interact with the same Execution.

Persistence must support mechanisms such as:

* optimistic concurrency
* compare-and-swap
* leases
* version checks
* locking

The specific mechanism is implementation-dependent.

The semantic requirement is:

Concurrent workers must not corrupt Execution state or produce conflicting transitions.

⸻

77. Persistence and State Transitions

State transitions should be validated.

For example:

PENDING → RUNNING

may be valid.

But:

COMPLETED → RUNNING

should generally require an explicit recovery or compensation semantic rather than occurring accidentally.

⸻

78. Persistence and Idempotent State Transitions

Repeated requests to record the same transition should not corrupt state.

Example:

mark execution completed

called twice should not create contradictory outcomes.

Persistence semantics must therefore support idempotent state updates where required.

⸻

79. Persistence and Ordering

Execution history may depend on event ordering.

Noema should preserve sufficient ordering information such as:

* sequence number
* logical version
* timestamp
* causal relationship

Timestamps alone may not establish ordering in distributed systems.

⸻

80. Persistence and Observability

Operational observability systems may contain:

* logs
* metrics
* traces

These are useful but should not be assumed to constitute the canonical Noema execution history.

Noema’s durable execution records should remain available independently of ephemeral observability infrastructure.

⸻

81. Persistence and Logs

Logs answer:

“What did the runtime print?”

Execution persistence answers:

“What happened to this Intent and Action?”

Logs may support investigation.

They should not be the only source of execution history.

⸻

82. Persistence and Traces

Distributed traces provide valuable diagnostic information.

However:

trace ≠ Execution Record

A trace may expire or be sampled.

A consequential Execution Record should have stronger durability guarantees.

⸻

83. Persistence and Events

Events may notify Noema of enterprise changes.

Persisting relevant events can support:

* reconciliation
* state reconstruction
* audit
* recovery

But Noema must retain the distinction between:

event occurrence

and:

current resource state

⸻

84. Persistence and External Systems

External systems may have their own retention and consistency guarantees.

Noema should not assume that a previously observed resource can always be queried later.

Consequential Evidence may therefore need to preserve sufficient information to explain what Noema observed, subject to enterprise data-retention constraints.

⸻

85. Persistence and Large Payloads

Noema should avoid storing large raw payloads by default when a smaller semantic representation is sufficient.

For example, instead of retaining an entire:

10 MB JSON document

Noema may retain:

relevant claim
source
request identifier
response metadata
relevant fields
hash/reference

when sufficient for audit and recovery.

⸻

86. Persistence and Integrity

Persisted records should be protected against unauthorized modification.

For consequential history, useful mechanisms may include:

* immutable records
* append-only storage
* cryptographic hashes
* signed records
* versioning
* tamper-evident chains

The exact mechanism depends on deployment requirements.

⸻

87. Persistence and Audit Integrity

An audit trail is useful only if its integrity can be trusted.

Noema should distinguish:

historical record

from:

current mutable operational state

Audit records should have stronger immutability guarantees where required.

⸻

88. Persistence and Disaster Recovery

Persistence infrastructure should define recovery objectives appropriate to the role of the data.

Important concepts include:

* RPO
* RTO
* replication
* backup
* restore
* durability

Noema should not claim stronger recovery guarantees than its persistence architecture provides.

⸻

89. Persistence Failure

Persistence itself can fail.

Example:

Action ready to execute
      ↓
Persistence unavailable

Noema must define whether execution may proceed.

For consequential Actions, inability to persist required state may itself be a reason to:

* block
* retry
* degrade safely
* escalate

rather than execute without required accountability and recovery guarantees.

⸻

90. Persistence Before Consequential Execution

A core safety principle is:

Noema should not perform an Action requiring durable execution state when that state cannot be durably recorded.

The exact boundary depends on the Action Contract, execution architecture, and risk requirements.

⸻

91. Persistence After Execution

Noema must also handle:

Action succeeded
      ↓
Outcome persistence failed

This creates an uncertain observation state.

The system should recover through:

* reconciliation
* idempotency
* external query
* execution lookup
* external operation identity

rather than assuming the Action failed.

⸻

92. Persistence and Logical Exactly-Once Effects

Noema can combine:

durable Execution identity
+
idempotency
+
reconciliation

to achieve reliable logical execution even when infrastructure provides only at-least-once delivery.

This is not a claim of exactly-once message delivery.

⸻

93. Persistence and Action Recovery

After restart:

Execution:
RUNNING
Last known:
Attempt 1 = UNKNOWN

Noema should not simply execute Attempt 2.

It should determine:

* Did Attempt 1 execute?
* Did the enterprise commit the Action?
* Is the Action idempotent?
* Is the external operation identifiable?
* Is reconciliation required?
* Has the applicable Trust decision remained valid?

Persistence provides the historical inputs for this reasoning.

⸻

94. Persistence and Compensation Recovery

Similarly:

Execution:
PARTIAL

may require recovering:

* completed Actions
* failed Actions
* available compensation Actions
* current enterprise state
* applicable Action Contract versions
* relevant Trust decisions

before compensation can safely proceed.

⸻

95. Persistence and Human Approval

If an Execution waits for approval:

WAITING_FOR_APPROVAL

that state must survive:

* process restart
* worker replacement
* network failure
* deployment

Approval Evidence should remain associated with the relevant Intent, Action, and Execution.

⸻

96. Persistence and Clarification

Likewise:

Intent:
CLARIFICATION_REQUIRED
waiting_for:
user clarification

must survive beyond the original request.

A clarification response must be associated with the correct Intent version and context.

⸻

97. Persistence and Context Versioning

Context can change.

For example:

Context v1
payment.status = SUCCEEDED

followed by:

Context v2
payment.status = REFUNDED

Noema should be able to distinguish these snapshots.

A newer Context version does not erase the historical observation represented by the earlier snapshot.

⸻

98. Persistence and Evidence Versioning

Evidence can be superseded.

Example:

Evidence v1:
status = PENDING
Evidence v2:
status = SUCCEEDED

The history should remain reconstructible.

Supersession does not mean the earlier observation never occurred.

⸻

99. Persistence and Policy Versioning

A Trust decision should identify which Policy version was evaluated.

Example:

Policy:
refund-policy
Version:
12

This prevents historical decisions from becoming ambiguous after policy changes.

⸻

100. Persistence and Integration Versioning

The same principle applies to integration mappings.

If:

Payment API mapping v2

interpreted:

"completed" → SUCCEEDED

historical executions should retain the mapping version used when that interpretation mattered.

⸻

101. Persistence and Schema Versioning

Persistent objects should carry enough schema information to remain interpretable.

Example:

Execution Schema = 4
Action Contract = refund.v3
Policy = refund-policy.v12
Integration Mapping = payment-api.v2

This provides semantic stability across system evolution.

⸻

102. Persistence and Data Lineage

Persisted records should preserve relationships between:

Intent
Evidence
Fact
Reconciliation
Trust Decision
Action
Execution
Outcome

This forms the Noema execution lineage.

⸻

103. Persistence and the Execution Record

The Execution Record is the central durable object for consequential execution.

Conceptually:

Execution Record
 ├── execution_id
 ├── intent_id
 ├── intent_version
 ├── actor_ref
 ├── action
 ├── target_ref
 ├── context_snapshot
 ├── evidence_refs
 ├── fact_status_refs
 ├── reconciliation_refs
 ├── trust_decision
 ├── attempts
 ├── state
 ├── outcome
 ├── external_operation_ids
 ├── timestamps
 └── versions

The physical implementation may differ.

⸻

104. Persistence and the Audit Record

The Audit Record answers:

“What happened, when, why, and based on what information?”

It should reference rather than duplicate large amounts of data wherever possible.

Audit records should preserve causal relationships and semantic versions.

⸻

105. Persistence and References

Noema should prefer stable references when the underlying enterprise data remains externally authoritative.

Example:

payment_id = 123
source = Payment System
tenant = tenant_42

rather than maintaining a shadow copy of the entire Payment record.

⸻

106. Persistence and Referential Integrity

References to enterprise resources should preserve enough identity to avoid ambiguity.

A bare:

123

may be insufficient.

A more useful semantic reference may include:

resource_type
resource_id
system
tenant
organization
environment
scope

⸻

107. Persistence and Resource Deletion

If an enterprise Resource is later deleted, historical Noema records should still be able to indicate what Resource the Execution originally targeted.

Therefore references used for audit should not depend entirely on the continued existence of the live enterprise record.

⸻

108. Persistence and Identity Resolution

Persistence must distinguish:

identity resolution

from:

canonicalization

A resolved identifier indicates which resource or actor a semantic reference refers to.

Canonicalization establishes which representation is authoritative within an explicit scope.

Neither may be inferred merely from a model’s confidence.

⸻

109. Persistence and Privacy

Persistence must minimize unnecessary replication of sensitive information.

Where possible:

reference
+
provenance
+
minimal necessary value

should be preferred over complete enterprise record duplication.

⸻

110. Persistence and Encryption

Depending on enterprise requirements, persisted data may require:

* encryption at rest
* encryption in transit
* key management
* field-level protection
* secret isolation

Secrets should not be persisted merely because they appeared in an integration payload.

⸻

111. Persistence and Secrets

Credentials, tokens, API keys, and other secrets should not become ordinary Execution data.

Persistence must explicitly distinguish:

execution metadata

from:

credentials

Secret material belongs in an appropriate secret-management system.

The model must never receive credentials merely because persistence contains execution information.

⸻

112. Persistence and Audit Redaction

Auditability does not require storing every raw value.

Sensitive fields may require:

* redaction
* tokenization
* hashing
* masking
* reference

while preserving enough information to reconstruct the decision.

⸻

113. Persistence and Searchability

Noema’s persisted records should be queryable by stable identifiers such as:

* intent_id
* intent_version
* execution_id
* resource_id
* principal_id
* idempotency_key
* correlation_id
* external_operation_id

This supports operational recovery and audit investigation.

⸻

114. Correlation

Related records should share a correlation identity.

Intent
   │
   └── correlation_id
          │
          ├── Trust
          ├── Action
          ├── Execution
          ├── Reconciliation
          └── Outcome

This allows distributed components to reconstruct a single execution journey.

⸻

115. Persistence and Observability Correlation

Where possible, Noema should connect:

execution_id
correlation_id
trace_id
request_id
external_operation_id

This creates a bridge between semantic execution records and infrastructure diagnostics.

Observability identifiers do not replace semantic execution identity.

⸻

116. Persistence and External Operation IDs

External systems may assign their own operation identifiers.

Example:

Noema:
execution_id = exec_123
Payment System:
operation_id = payop_987

The relationship should be persisted.

This is particularly important for reconciliation.

⸻

117. Persistence and Reconciliation Identity

A recovery process should be able to search the enterprise system using durable identifiers such as:

* idempotency key
* external operation ID
* resource ID
* transaction ID

Persistence should preserve these identifiers where available.

⸻

118. Persistence and Recovery Semantics

Recovery should be defined as:

Reconstructing the last known Noema Execution state, determining what remains uncertain, reconciling the relevant enterprise state, revalidating applicable conditions, and selecting the next permitted deterministic transition.

Not:

“Continue executing from wherever the process stopped.”

⸻

119. Persistence and State Reconstruction

A recovered Execution should be reconstructable from durable information:

Intent
+
Intent version
+
Context
+
Evidence
+
Fact Status
+
Reconciliation results
+
Trust decision
+
Action
+
Attempts
+
External identifiers
+
Current Execution state

⸻

120. Persistence and Stale State

Persisted state can become stale.

Therefore the persistence layer should make temporal semantics visible.

Example:

last_known_status = ACTIVE
observed_at = 09:00

is preferable to:

status = ACTIVE

without temporal context.

⸻

121. Persistence and Revalidation Windows

Some Actions may define maximum acceptable evidence age.

Example:

balance evidence:
max_age = 30 seconds

On recovery:

evidence age > 30 seconds

may require revalidation before execution.

Freshness requirements are claim- and action-specific.

⸻

122. Persistence and Durable Decisions

A Trust Decision should not be treated as permanently valid merely because it was once persisted.

For mutable or high-risk Actions:

old Trust Decision
      ↓
current Context changed
      ↓
State Reconciliation
      ↓
re-evaluate Trust

Persistence preserves the historical decision.

It does not freeze enterprise reality.

⸻

123. Persistence and Policy Changes

If policy changes while an Execution is waiting:

Execution:
WAITING_FOR_APPROVAL
Policy v12:
allowed
Policy v13:
approval requirements changed

Noema must have explicit semantics determining whether the Execution uses:

policy snapshot

or:

current policy

This must never be accidental.

The historical decision must remain unchanged even if a current-policy re-evaluation produces a different result.

⸻

124. Persistence and Long-Running Intent

Long-running Intent may require periodic revalidation.

Intent
 ↓
Trust
 ↓
Waiting
 ↓
Hours pass
 ↓
Resume
 ↓
Reconcile
 ↓
Revalidate
 ↓
Continue / Re-evaluate

Persistence makes the pause safe.

⸻

125. Persistence and Workflow State

Noema’s workflow state should describe execution semantics rather than duplicating enterprise workflow systems.

Noema may know:

WAITING_FOR_APPROVAL

without owning the enterprise’s:

approval workflow database

unless explicitly integrated as an enterprise capability.

⸻

126. Persistence and System of Record

Noema should remain explicit about which system owns each fact.

Noema:
Execution status
Payment System:
Payment status
Ledger:
Balance
Identity Provider:
Identity

Persistence should preserve these ownership relationships.

⸻

127. Persistence and Canonical Data

Persisted references to Canonical Data should identify, where required:

* source
* authority scope
* observation time
* effective time
* resource
* version
* provenance
* freshness

This preserves the distinction between:

canonical enterprise fact

and:

Noema's observation/reference to that fact

⸻

128. Persistence and Evidence Retention

Evidence retention should correspond to how long the evidence is necessary to explain or reconstruct a decision.

High-consequence Actions may require stronger retention than low-risk informational interactions.

Retention requirements should be explicit rather than assumed.

⸻

129. Persistence and Risk

Persistence requirements may increase with Action risk.

For example:

Low risk:
read-only query
High risk:
transfer funds

The second may require stronger:

* audit
* immutability
* evidence retention
* versioning
* reconciliation
* recovery guarantees

Read-only does not mean non-consequential.

A read operation involving protected enterprise data may itself require durable authorization and audit information.

⸻

130. Persistence and Risk-Adaptive Durability

Noema may define durability requirements based on Action class.

Conceptually:

Risk
 ↓
Required durability
 ↓
Evidence retention
 ↓
Audit requirements
 ↓
Recovery guarantees

The exact policy belongs to enterprise configuration and applicable Noema policy.

⸻

131. Persistence and Informational Requests

Not every user interaction requires a durable Execution Record.

For a purely informational query:

“What’s my account balance?”

Noema may only need ephemeral runtime Context, depending on enterprise requirements.

For:

“Transfer $10,000.”

durable Execution state is substantially more important.

The persistence requirement is determined by semantic consequence, not merely by whether the request is technically read or write.

⸻

132. Persistence and Ephemeral State

Ephemeral state is acceptable when losing it does not create an unsafe or unauditable condition.

Examples:

* temporary model output
* intermediate parsing artifacts
* cache entries
* short-lived UI state

The boundary must be explicit.

⸻

133. Persistence and Model Outputs

Raw LLM outputs should not automatically become durable canonical records.

Noema may persist model output when necessary for:

* debugging
* audit
* evaluation
* reproducibility

subject to data-retention requirements.

More importantly, Noema should persist the semantic result that affected execution, not blindly retain every intermediate token or generation.

Model output remains untrusted and must not become authoritative merely because it is persisted.

⸻

134. Persistence and Deterministic Replay

Replay can be useful for debugging and auditing.

A replayable Execution may require:

* Intent
* Intent version
* Context snapshot
* Evidence
* Fact Status
* reconciliation inputs/results
* Policy version
* Action Contract version
* Trust configuration
* integration semantics
* relevant graph/capability versions

Replay should distinguish:

historical reconstruction

from:

re-executing the Action

The latter must never occur accidentally during replay.

⸻

135. Persistence and Safe Replay

Replay must be non-executing by default.

Reconstructing:

"what would Noema have decided?"

must not dispatch:

refund_payment()

unless an explicit execution path is invoked and separately authorized.

⸻

136. Persistence and Testing

Persisted execution histories can become test fixtures.

Example:

Intent
+
Evidence
+
Fact Status
+
Policy
+
Action
+
Outcome

can be replayed against a new Trust implementation to detect behavioral changes.

This supports regression testing of Noema’s deterministic layer.

⸻

137. Persistence and Versioned Semantics

Historical records should be interpretable under the semantic versions that produced them.

For example:

Intent Model v4
Trust Model v7
Action Contract v3
Policy v12
Integration Mapping v2

This supports reliable audit and regression analysis.

⸻

138. Persistence and Migration Safety

When semantics change, Noema should avoid silently rewriting historical execution meaning.

Historical:

EXECUTE

must remain historically:

EXECUTE

even if current policy would now produce:

CLARIFY

The distinction between historical and current evaluation must remain explicit.

⸻

139. Persistence and Current Evaluation

Noema may re-evaluate historical executions for analysis.

That produces a new evaluation:

Historical Decision:
EXECUTE
Current Policy Re-evaluation:
CLARIFY

The new result must not overwrite the original historical decision.

⸻

140. Persistence and Audit Trail

A complete audit trail may look like:

Intent received
      ↓
Intent version admitted
      ↓
Intent resolved
      ↓
Context captured
      ↓
Evidence collected
      ↓
State reconciled
      ↓
Fact Status established
      ↓
Policy evaluated
      ↓
Trust = EXECUTE
      ↓
Action dispatched
      ↓
Attempt #1
      ↓
Timeout
      ↓
Outcome = UNKNOWN
      ↓
Reconciliation
      ↓
Evidence = SUCCEEDED
      ↓
Outcome = SUCCESS

Persistence makes this chain durable.

⸻

141. Persistence and Recovery Example

Consider:

“Refund my last payment.”

Noema resolves:

Payment #123

Then:

Trust = EXECUTE

and dispatches:

refund_payment(#123)

The network connection fails.

Noema records:

Attempt #1 = UNKNOWN

The worker crashes.

After restart:

recover Execution
        ↓
lookup idempotency key
        ↓
query Payment System
        ↓
State Reconciliation
        ↓
Payment = REFUNDED
        ↓
record Evidence
        ↓
Fact Status = VERIFIED
        ↓
Outcome = SUCCESS

No duplicate refund is issued.

⸻

142. Persistence and Failure Modes

Persistence architecture must account for:

* database unavailable
* partial write
* duplicate write
* lost acknowledgment
* network partition
* worker crash
* storage corruption
* replication lag
* schema mismatch
* stale reads
* concurrent updates

The execution model must explicitly define the resulting Noema state.

⸻

143. Persistence and Partial Writes

If part of an Execution Record is written successfully while another part fails, Noema must not assume the record is complete.

Use of:

* transactions
* write-ahead logs
* versioning
* reconciliation

may be appropriate depending on implementation.

Incomplete records must be detectable.

⸻

144. Persistence and Duplicate Writes

Retries at the persistence layer can produce duplicate records.

Consequential records should therefore have stable identifiers and idempotent write semantics where necessary.

Duplicate persistence events must not create contradictory execution history.

⸻

145. Persistence and Corruption

If persisted Execution state becomes inconsistent:

Execution = COMPLETED
Attempt = RUNNING

Noema should not silently choose one.

It should enter a defined recovery or reconciliation path.

⸻

146. Persistence and Availability

Durability and availability can conflict.

Noema should define which operations may proceed when persistence is degraded.

For high-risk Actions:

persistence unavailable
        ↓
do not execute

may be appropriate.

For low-risk interactions:

persistence unavailable
        ↓
serve request without durable history

may be acceptable.

This must be policy-driven.

⸻

147. Persistence and Enterprise Requirements

Enterprise deployments may impose:

* data residency
* retention periods
* legal hold
* audit requirements
* encryption standards
* access controls
* tenant isolation
* regional storage
* organizational boundaries

Noema persistence must be configurable to satisfy these requirements.

⸻

148. Persistence and Data Residency

Where enterprise policy requires regional storage, Noema should ensure persisted data remains within the permitted boundary.

This is especially relevant for:

* Evidence
* Context
* Audit records
* Identity information
* Execution metadata

⸻

149. Persistence and Data Classification

Persisted information may have classifications such as:

PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED

Classification should influence:

* storage
* access
* retention
* encryption
* replication

⸻

150. Persistence and Access Logging

Access to sensitive persisted records may itself require auditability.

For example:

Operator viewed Evidence for Execution #123

may need to become an audit event depending on enterprise requirements.

⸻

151. Persistence and System Boundaries

Noema may interact with multiple persistence systems:

Operational Store
Audit Store
Event Store
Cache
Secret Store
Enterprise Systems

These stores should have explicit ownership and semantics.

A physical database may contain multiple logical persistence domains, but those domains must remain semantically distinct.

⸻

152. Persistence Is a Semantic Boundary

The persistence layer should preserve the distinction between:

current operational state
historical observation
enterprise reference
Evidence
Fact Status
reconciliation result
audit record

A single database table does not eliminate these semantic distinctions.

⸻

153. Recommended Conceptual Storage Model

A logical persistence model may contain:

Intent
IntentVersion
ContextSnapshot
Evidence
Fact
FactStatus
StateObservation
StateReconciliation
TrustEvaluation
PolicyReference
ActionReference
Execution
ExecutionAttempt
Outcome
Failure
Intervention
AuditRecord

This is a conceptual model, not a mandatory relational schema.

⸻

154. Core Relationships

Intent
  │
  ├── has_versions → IntentVersion
  │
  └── creates → Execution
Execution
  ├── uses → ContextSnapshot
  ├── references → Evidence
  ├── references → Fact
  ├── references → StateReconciliation
  ├── evaluates → TrustEvaluation
  ├── invokes → Action
  ├── contains → ExecutionAttempt
  ├── produces → Outcome
  └── may_create → Intervention
Observation
  └── evaluated_by → StateReconciliation
StateReconciliation
  └── produces → Fact / State
Evidence
  └── supports → Claim

⸻

155. Persistence and the Noema Architecture

The persistence layer sits beneath the semantic execution lifecycle:

                    Source of Intent
                          │
                          ▼
                    Intent Engine
                          │
                          ▼
                  Hard Schema Gate
                          │
                          ▼
                  Context / Evidence
                          │
                          ▼
                 State Reconciliation
                          │
                          ▼
                   Deterministic Trust
                          │
                          ▼
              Action Graph / Planner
                          │
                          ▼
                      Execution
                          │
                          ▼
                    Verification
                          │
                          ▼
                       Outcome
                          │
                          ▼
                     Persistence

Persistence records the journey rather than replacing the systems involved in the journey.

Persistence also preserves the historical information necessary to repeat reconciliation and recover execution safely.

⸻

156. Persistence and the Noema Ownership Boundary

Noema may own canonical state in its own execution domain.

Examples include:

* Intent
* Intent version lineage
* Trust Decision
* Execution state
* Execution attempt history
* Outcome state
* intervention/case state
* reconciliation record
* operational execution history

Noema does not thereby own canonical enterprise Business State.

Examples of enterprise-owned state include:

* account balance
* payment ledger state
* inventory quantity
* employee status
* customer account status
* transaction settlement state

The distinction must remain explicit in persistence.

⸻

157. No Shadow Canonical Business State

Noema must not create a shadow canonical representation of enterprise Business State merely because that state is useful for execution.

If Noema stores:

payment.status = SUCCEEDED

it must be possible to determine whether that represents:

* an enterprise-owned authoritative value
* a persisted observation
* Evidence
* a Context snapshot
* a reconciled Fact
* a historical execution expectation

The representation alone must never imply ownership.

⸻

158. Persistence and Read-Only Consequences

Read-only operations can still be consequential.

For example:

Retrieve protected financial records

may expose sensitive enterprise data even though it does not mutate enterprise state.

Persistence may therefore need to retain:

* authorization evidence
* Trust decisions
* access records
* data-scope information
* relevant audit information

Data being read does not make the operation semantically consequence-free.

⸻

159. Persistence and Security Boundary

Persistence must respect the Noema security boundary.

The following remain untrusted:

* model output
* user-provided text
* retrieved enterprise text
* tool responses
* external payloads

The model must not have:

* enterprise credentials
* unrestricted database access
* unrestricted HTTP access
* direct execution authority

No free-form model output may become executable merely because it was persisted.

⸻

160. Persistence and Causal Reconstruction

A consequential execution should ideally support reconstruction of:

Claim
   ↓
Source / Authority
   ↓
Observation
   ↓
Fact Status
   ↓
State Reconciliation
   ↓
Trust Decision
   ↓
Action
   ↓
Execution Attempt
   ↓
Verification
   ↓
Outcome

This chain is the durable semantic lineage of execution.

⸻

161. Core Invariants

Invariant 1

Noema must persist information required to remain recoverable, deterministic, reconcilable, and auditable.

Invariant 2

Persistence does not transfer ownership of enterprise Business State to Noema.

Invariant 3

Noema must not silently become a shadow System of Record for enterprise data.

Invariant 4

Consequential Executions must have durable identities.

Invariant 5

Execution history must survive process-level failures when the Action requires recovery guarantees.

Invariant 6

Intent state requiring future interaction must survive beyond the original request.

Invariant 7

Admitted Intent versions must remain semantically immutable.

Invariant 8

Material Intent changes must create new versions rather than silently mutate historical Intent.

Invariant 9

Persisted Context is historical context, not automatically current enterprise state.

Invariant 10

Persisted Trust Decisions are historical decisions and do not automatically remain valid forever.

Invariant 11

Evidence required to reconstruct consequential decisions should be durably referenced or retained.

Invariant 12

Fact Status must remain distinct from Evidence, Context, State, Outcome, and Canonical Data.

Invariant 13

Model confidence must never be treated as authoritative Fact Status.

Invariant 14

External data must pass the applicable schema validation and admission boundary before being treated as admitted semantic data.

Invariant 15

Historical records must preserve relevant Policy, Action Contract, Intent, integration, graph, capability, and semantic versions.

Invariant 16

Execution attempts must be distinguishable.

Invariant 17

Idempotency information must survive whenever required to prevent duplicate logical execution.

Invariant 18

Unknown execution outcomes must remain explicitly represented.

Invariant 19

Persistence must not convert an uncertain outcome into success or failure without sufficient evidence.

Invariant 20

Recovery must reconcile and revalidate mutable enterprise state before continuing consequential execution.

Invariant 21

Historical records must not be silently rewritten to reflect current policy or current enterprise state.

Invariant 22

Replay must not accidentally execute Actions.

Invariant 23

Persisted references to enterprise Resources must retain sufficient identity and scope to remain meaningful.

Invariant 24

Persistence must preserve tenant, organizational, legal, and environmental boundaries.

Invariant 25

Persistence must not bypass enterprise authorization.

Invariant 26

Secrets must not be treated as ordinary execution data.

Invariant 27

Persistence should minimize unnecessary duplication of enterprise data.

Invariant 28

Retention must be appropriate to the semantic and operational purpose of the data.

Invariant 29

Consequential audit records should have stronger integrity guarantees than ordinary mutable operational state where required.

Invariant 30

Persistence failures must produce explicit system states rather than silent loss of execution history.

Invariant 31

Noema should not execute high-consequence Actions when required durable execution state cannot be safely recorded.

Invariant 32

Persistence must support reconciliation when execution state and enterprise state diverge.

Invariant 33

Concurrent updates to Execution state must not produce invalid or contradictory transitions.

Invariant 34

Historical execution records must remain interpretable across schema evolution.

Invariant 35

Source, authority, freshness, availability, and authorization must remain distinct dimensions.

Invariant 36

State Reconciliation must not invent authority or canonicality.

Invariant 37

Persisted enterprise observations must remain distinguishable from enterprise-owned canonical state.

Invariant 38

Trust EXECUTE must never be persisted or interpreted as proof that an Action succeeded.

Invariant 39

Planner persistence must not imply planner authority to invent capabilities, authority, or execution semantics.

Invariant 40

No persisted model output may bypass deterministic validation, Trust, authorization, or Action Contract boundaries.

Invariant 41

Persistence must preserve sufficient causal relationships to reconstruct why consequential transitions occurred.

Invariant 42

Noema-owned execution-domain state may be canonical within Noema without becoming canonical enterprise Business State.

Invariant 43

Persisted state must retain sufficient temporal information to distinguish historical observations from current enterprise state.

Invariant 44

A persisted record must not become authoritative merely because it is stored durably.

Invariant 45

Persistence must preserve enough information to answer:

What happened?
What was known?
What was authoritative?
What was reconciled?
What was trusted?
What was executed?
What was verified?
What ultimately occurred?

⸻

162. Final Definition

Persistence is the durable memory of Noema’s execution system.

It preserves the Intent versions, evidence, Fact Status, observations, reconciliation results, Trust decisions, state transitions, Actions, attempts, and Outcomes necessary for recovery, auditability, reconciliation, and deterministic continuation without becoming the System of Record for enterprise Business State.

The fundamental architecture is:

                  ENTERPRISE
                      │
              Authoritative State
                      │
                      ▼
          Validated Integration / Events
                      │
                      ▼
             State Reconciliation
                      │
                      ▼
                   NOEMA
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Intent       Trust      Execution
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Persistence
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
     History       Recovery       Audit
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                Reconciliation
                      │
                      ▼
                  ENTERPRISE

The key principle is:

Persistence gives Noema memory, not ownership.

It remembers what Noema knew, what it observed, what it reconciled, what it decided, and what it did so that execution can survive failure and remain accountable while enterprise systems remain authoritative for enterprise Business State.