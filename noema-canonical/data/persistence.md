Persistence

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/persistence.md

⸻

1. Definition

Persistence defines what Noema retains, why it retains it, how persisted information relates to enterprise state, and the guarantees required to reconstruct, audit, recover, and operate an Intent execution safely.

Persistence answers:

“What must survive beyond the current runtime, and what guarantees must Noema provide about that information?”

Persistence is therefore not simply a database concern.

It is an execution, trust, and auditability concern.

⸻

2. Purpose

Noema operates across potentially long-running and failure-prone workflows.

A process may:

receive Intent
      ↓
resolve Intent
      ↓
evaluate Trust
      ↓
execute Action
      ↓
lose network connectivity
      ↓
restart
      ↓
recover execution
      ↓
verify Outcome

If the relevant state existed only in process memory, Noema could lose the information required to safely continue.

Persistence provides continuity across:

* process restarts
* infrastructure failures
* retries
* asynchronous execution
* human intervention
* long-running workflows
* reconciliation
* auditing

⸻

3. Core Principle

Persist what Noema must remember to remain deterministic, recoverable, and accountable.

Noema should not persist everything simply because it can.

The persistence boundary should be driven by operational and semantic requirements.

⸻

4. Persistence Is Not Business-State Ownership

A fundamental Noema boundary is:

Noema Persistence
        ≠
Enterprise System of Record

Noema may persist:

Intent
Trust decisions
Execution records
Action metadata
Evidence references
Audit information
Recovery state

while the enterprise remains authoritative for:

accounts
balances
payments
orders
employees
inventory
business transactions

⸻

5. Persistence Model

Conceptually:

Enterprise Systems
        │
        │ authoritative state
        ▼
   Integration Layer
        │
        ▼
     Noema Runtime
        │
        ▼
   Noema Persistence

Noema Persistence records what Noema needs to operate and explain its execution.

It does not become a shadow database for the enterprise.

⸻

6. What Noema Should Persist

The persistence layer should generally retain information required to reconstruct consequential execution.

This may include:

Intent
Intent lifecycle
Resolved Intent
Context snapshots
Trust evaluations
Trust state transitions
Evidence references
Policy decisions
Action selections
Execution records
Execution attempts
Idempotency information
Failure information
Recovery state
Human intervention
Compensation state
Outcome observations
Audit records

The exact retention policy is implementation- and enterprise-dependent.

⸻

7. What Noema Should Generally Not Persist

Noema should avoid unnecessarily duplicating enterprise Business State.

For example, if the enterprise Ledger is authoritative for:

Account.balance

Noema generally should not maintain its own independently authoritative:

Account.balance

Instead, it may persist:

Evidence:
Ledger reported balance = $10,000
observed_at = ...

when required for execution or audit.

⸻

8. Persistence Categories

A useful conceptual division is:

Operational State
Historical Record
Evidence
Execution State
Audit Record
Reference
Cache

These categories should not be conflated.

⸻

9. Operational State

Operational State represents information required for Noema to continue active work.

Examples:

Execution = RUNNING
retry_count = 2
waiting_for = PAYMENT_CONFIRMATION
next_action = VERIFY_REFUND

Operational State may be mutable.

⸻

10. Historical Record

Historical Records preserve what happened.

Examples:

Intent received
Trust evaluated
Action attempted
Policy evaluated
Human approved
Execution completed

Historical records should generally be append-oriented or otherwise protected against silent mutation.

⸻

11. Evidence Persistence

Noema may persist Evidence required to reconstruct why a decision was made.

For example:

Evidence:
Payment API reported status = SUCCEEDED

The record should preserve sufficient provenance to determine:

what was observed
where it came from
when it was observed
what claim it supported

⸻

12. Execution Persistence

Every consequential Action should have a durable Execution identity.

Conceptually:

Execution {
    execution_id
    intent_id
    action
    state
    attempts
    outcome
}

This allows Noema to recover an Execution after process failure.

⸻

13. Intent Persistence

Intent may need to survive beyond the original request.

Example:

Intent
   ↓
Needs clarification
   ↓
User responds 4 hours later

The Intent state must remain available.

⸻

14. Intent Lifecycle Persistence

Noema should persist meaningful Intent transitions.

Example:

RECEIVED
   ↓
UNDERSTOOD
   ↓
RESOLVING
   ↓
RESOLVED
   ↓
TRUST_EVALUATING
   ↓
EXECUTING

The exact state machine is defined elsewhere.

Persistence records its occurrence and history.

⸻

15. Context Persistence

Context may need to be persisted when it is necessary to explain or resume an Execution.

However, Noema should distinguish:

Context Snapshot

from:

Enterprise Current State

A Context Snapshot describes what Noema knew at a particular point.

It does not automatically remain current.

⸻

16. Context Snapshot

Conceptually:

ContextSnapshot {
    snapshot_id
    execution_id
    captured_at
    identity
    relevant_resources
    relevant_state
    evidence_refs
    policy_refs
}

This allows Noema to reconstruct the decision environment.

⸻

17. Snapshot vs Live State

This distinction is fundamental.

Snapshot:
Account.status = ACTIVE
observed at 10:30
Live Enterprise State:
Account.status = SUSPENDED
observed at 10:45

Both can be valid.

The first describes what Noema knew at 10:30.

The second describes current enterprise state.

⸻

18. Trust Persistence

Trust decisions should be persisted when they affect consequential execution.

For example:

Trust Decision:
EXECUTE

should be associated with:

Intent
Evidence
Policy
Risk
Authorization
timestamp

This enables later reconstruction.

⸻

19. Trust Decision Is Not Enterprise Policy

Noema may persist:

Trust Decision = EXECUTE

but that does not make Noema the owner of:

Enterprise Policy

The enterprise remains authoritative for its policies unless explicitly delegated otherwise.

⸻

20. Policy Persistence

Noema may persist:

policy identifier
policy version
policy evaluation result
policy inputs

rather than necessarily storing the complete enterprise policy.

Where the policy itself is managed by Noema, the persistence model must retain the relevant version and lifecycle.

⸻

21. Action Persistence

Noema should persist enough information to determine which Action was selected.

Example:

Action:
refund_payment
Resource:
Payment #123
Action Contract:
refund_payment.v3

The Action identity should remain stable enough for audit and recovery.

⸻

22. Action Contract Version

Execution records should preserve the Action Contract version used.

Example:

Action:
refund_payment
Contract:
v3

If the contract later changes to:

v4

historical executions should not silently appear to have used v4.

⸻

23. Execution Attempt Persistence

Each actual attempt should be distinguishable.

Execution #100
 ├── Attempt #1
 ├── Attempt #2
 └── Attempt #3

Each attempt may have:

started_at
completed_at
request identity
response
failure
timeout
retry decision

⸻

24. Idempotency Persistence

Idempotency information must survive process restarts when the underlying Action requires it.

Conceptually:

Idempotency Key
      ↓
Execution
      ↓
Action

This prevents a restarted worker from interpreting an existing execution as new work.

⸻

25. Persistence and Retries

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
determine whether retry is safe

Without persistence, Noema may accidentally duplicate an Action.

⸻

26. Persistence and Unknown Outcomes

One of the most important persistence requirements is preserving uncertainty.

Example:

Action submitted
      ↓
network timeout
      ↓
Outcome = UNKNOWN

Noema must persist:

UNKNOWN

rather than:

FAILED

unless the failure is actually established.

⸻

27. Recovery

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
revalidate
   ↓
continue / retry / clarify / escalate

Recovery must not simply resume blindly from the last instruction.

⸻

28. Recovery Requires Revalidation

Persisted state is historical information.

It may no longer reflect current enterprise state.

Therefore:

Persisted Context
      ↓
Recovery
      ↓
Revalidation
      ↓
Current Context
      ↓
Trust Re-evaluation

This is particularly important for Actions involving mutable resources.

⸻

29. Persistence and Determinism

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
evidence
+
policy version
+
execution history
=
recoverable decision

⸻

30. Persistence Does Not Guarantee Determinism

Persistence alone is insufficient.

Noema also requires:

explicit state
explicit policies
explicit contracts
explicit transitions
explicit evidence

Persistence records those semantics; it does not create them.

⸻

31. Event vs State Persistence

Noema should distinguish:

Event:
payment.refunded occurred

from:

State:
payment.status = REFUNDED

An event may be persisted as part of the history.

The current enterprise state remains owned by the authoritative system.

⸻

32. Append-Oriented History

Consequential transitions should preferably produce append-oriented records.

For example:

Intent received
Intent resolved
Trust evaluated
Action selected
Attempt started
Attempt failed
Retry scheduled
Attempt completed
Outcome verified

This provides a durable execution history.

⸻

33. Event Sourcing Is Not Required

Noema may use event sourcing internally, but the semantic model does not require it.

The principle is:

Noema must preserve sufficient history to reconstruct consequential decisions and execution.

The underlying persistence technology is an implementation choice.

⸻

34. Transactional Boundaries

Persistence operations should have clear transactional semantics.

For example, when recording:

Execution → RUNNING

Noema must avoid states where:

Action dispatched

but:

Execution record does not exist

unless the system explicitly handles that uncertainty.

⸻

35. Persistence and Action Dispatch

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

The latter is especially dangerous.

⸻

36. Persistence and the Execution Boundary

Noema should define a durable boundary around Action dispatch.

Conceptually:

Intent
   ↓
Trust
   ↓
Persist Execution
   ↓
Dispatch Action
   ↓
Observe Result
   ↓
Persist Outcome

The exact ordering depends on the execution architecture and delivery guarantees.

⸻

37. At-Least-Once Reality

Distributed execution commonly results in at-least-once delivery.

Therefore Noema must assume:

Action may be delivered more than once

unless stronger guarantees are explicitly established.

Idempotency and durable Execution identity are therefore fundamental.

⸻

38. Exactly-Once Claims

Noema should not casually claim exactly-once execution.

A system may provide:

exactly-once logical effect

through:

idempotency
deduplication
transactional boundaries

without literally guaranteeing exactly-once message delivery.

The distinction matters.

⸻

39. Persistence and Human Intervention

Human intervention may occur long after an Execution enters a blocked state.

Therefore the system must persist:

reason for intervention
relevant Evidence
current state
requested decision
operator decision
timestamp

⸻

40. Persistence and Compensation

Compensation may depend on historical Execution state.

Example:

Action A:
charge payment → succeeded
Action B:
create subscription → failed

To determine whether compensation is required, Noema needs durable knowledge of Action A’s outcome.

⸻

41. Persistence and Auditability

Persistence is one of the foundations of auditability.

Noema should be able to answer:

What did the user ask?
What did Noema understand?
What resources were identified?
What evidence was available?
What policy applied?
What Trust decision was made?
What Action was selected?
What attempts occurred?
What changed?
What was the final outcome?

⸻

42. Persistence and Explainability

The explanation of a consequential decision should be reconstructible from persisted records.

Intent
  ↓
Evidence
  ↓
Policy
  ↓
Trust Decision
  ↓
Action
  ↓
Execution
  ↓
Outcome

If these relationships disappear after execution, Noema cannot reliably explain its behavior.

⸻

43. Persistence and Provenance

Persisted records should preserve references to the origin of important information.

For example:

Evidence #42
source = Payment System
observed_at = 10:42
version = 781

This is more valuable than simply storing:

payment_status = succeeded

⸻

44. Persistence and Versioning

Important Noema artifacts should be versionable where changes could affect execution semantics.

Examples:

Action Contract
Policy
Intent schema
Integration mapping
Trust configuration

Historical executions must retain the versions relevant to their decisions.

⸻

45. Persistence and Schema Evolution

Noema’s persistence model will evolve.

Historical records should remain interpretable after schema changes.

Therefore Noema should consider:

schema version
contract version
migration strategy
backward compatibility

for durable records.

⸻

46. Persistence and Integration

Integration responses should not necessarily be persisted wholesale.

Noema should retain the information required to establish:

claim
provenance
decision
execution
audit

while minimizing unnecessary duplication.

⸻

47. Persistence and Data Minimization

Persistence should follow:

Store the minimum information required to preserve Noema’s operational and accountability guarantees.

This reduces:

storage cost
privacy exposure
security surface
data duplication
retention burden

⸻

48. Persistence and Sensitive Enterprise Data

Persisting Evidence may expose sensitive enterprise information.

Therefore persistence must respect:

authorization
classification
encryption
retention
tenant isolation
organizational boundaries

Noema’s need to explain a decision does not override enterprise data controls.

⸻

49. Tenant Isolation

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

⸻

50. Organizational Isolation

The same principle applies within an enterprise.

Noema must respect:

organization
business unit
environment
legal entity

when persistence contains data derived from those boundaries.

⸻

51. Persistence and Access Control

Persistence itself must not become an authorization bypass.

A user authorized to execute:

refund_payment

does not necessarily have access to:

all historical Evidence
all tenant data
all Execution records

Access to persisted information must be separately governed.

⸻

52. Persistence and Deletion

Deletion requirements may conflict with audit requirements.

Noema should distinguish:

business deletion

from:

audit retention

and apply explicit retention policies.

Where records cannot be deleted due to legal or audit requirements, access must still be appropriately controlled.

⸻

53. Retention

Retention should be defined according to:

record type
enterprise policy
legal requirements
operational requirements
audit requirements
data classification

Not all Noema data requires the same retention period.

⸻

54. Expiration

Temporary operational data may have shorter lifetimes.

Examples:

temporary Context
ephemeral cache
short-lived authorization evidence
transient integration response

Expiration should not accidentally remove information required to reconstruct a consequential decision.

⸻

55. Cache vs Persistence

A cache is not a durable source of truth.

Cache:
optimization
Persistence:
durable operational/history requirement

If an Execution depends on a value surviving a restart, that value should not exist only in cache.

⸻

56. Persistence and Current State

Persisted Noema state can represent:

what Noema currently believes about its own Execution

It should not be interpreted as:

current enterprise Business State

without revalidation.

⸻

57. Persistence and Reconciliation

Reconciliation compares persisted Noema expectations with current enterprise observations.

Persisted:
Execution = EXPECTED_SUCCESS
Enterprise:
Payment = SUCCEEDED
Result:
reconciled

or:

Persisted:
Execution = EXPECTED_SUCCESS
Enterprise:
Payment = FAILED
Result:
discrepancy

⸻

58. Persistence and Recovery State Machine

A recoverable Execution may conceptually move through:

RUNNING
   ↓
INTERRUPTED
   ↓
RECOVERING
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

59. Persistence and Concurrency

Multiple workers may interact with the same Execution.

Persistence must support mechanisms such as:

optimistic concurrency
compare-and-swap
leases
version checks
locking

The specific mechanism is implementation-dependent.

The semantic requirement is:

Concurrent workers must not corrupt Execution state or produce conflicting transitions.

⸻

60. Persistence and State Transitions

State transitions should be validated.

For example:

PENDING → RUNNING

may be valid.

But:

COMPLETED → RUNNING

should generally require an explicit recovery or compensation semantic rather than occurring accidentally.

⸻

61. Persistence and Idempotent State Transitions

Repeated requests to record the same transition should not corrupt state.

Example:

mark execution completed

called twice should not create contradictory outcomes.

Persistence semantics must therefore support idempotent state updates where required.

⸻

62. Persistence and Ordering

Execution history may depend on event ordering.

Noema should preserve sufficient ordering information such as:

sequence number
logical version
timestamp
causal relationship

Timestamps alone may not establish ordering in distributed systems.

⸻

63. Persistence and Causality

Where meaningful, Noema should preserve relationships such as:

Retry caused by Failure
Compensation caused by Partial Outcome
Clarification caused by Ambiguity
Revalidation caused by Recovery

This allows execution history to be understood causally rather than merely chronologically.

⸻

64. Persistence and Observability

Operational observability systems may contain:

logs
metrics
traces

These are useful but should not be assumed to constitute the canonical Noema execution history.

Noema’s durable execution records should remain available independently of ephemeral observability infrastructure.

⸻

65. Persistence and Logs

Logs answer:

“What did the runtime print?”

Execution persistence answers:

“What happened to this Intent and Action?”

Logs may support investigation.

They should not be the only source of execution truth.

⸻

66. Persistence and Traces

Distributed traces provide valuable diagnostic information.

However:

trace ≠ Execution record

A trace may expire or be sampled.

A consequential Execution record should have stronger durability guarantees.

⸻

67. Persistence and Events

Events may notify Noema of enterprise changes.

Persisting relevant events can support:

reconciliation
state reconstruction
audit
recovery

But Noema must retain the distinction between:

event occurrence

and:

current resource state

⸻

68. Persistence and External Systems

External systems may have their own retention and consistency guarantees.

Noema should not assume that a previously observed resource can always be queried later.

Consequential Evidence may therefore need to preserve sufficient information to explain what Noema observed.

⸻

69. Persistence and Large Payloads

Noema should avoid storing large raw payloads by default when a smaller semantic representation is sufficient.

For example, instead of retaining an entire API response:

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

70. Persistence and Integrity

Persisted records should be protected against unauthorized modification.

For consequential history, useful mechanisms may include:

immutable records
append-only storage
cryptographic hashes
signed records
versioning
tamper-evident chains

The exact mechanism depends on deployment requirements.

⸻

71. Persistence and Audit Integrity

An audit trail is useful only if its integrity can be trusted.

Noema should be able to distinguish:

historical record

from:

current mutable operational state

Audit records should have stronger immutability guarantees where required.

⸻

72. Persistence and Disaster Recovery

Persistence infrastructure should define recovery objectives appropriate to the role of the data.

Important concepts include:

RPO
RTO
replication
backup
restore
durability

Noema should not claim stronger recovery guarantees than its persistence architecture provides.

⸻

73. Persistence Failure

Persistence itself can fail.

Example:

Action ready to execute
      ↓
Persistence unavailable

Noema must define whether execution may proceed.

For consequential Actions, inability to persist required state may itself be a reason to:

block
retry
degrade safely
escalate

rather than execute without accountability.

⸻

74. Persistence Before Consequential Execution

A core safety principle is:

Noema should not perform an Action requiring durable execution state when that state cannot be durably recorded.

The exact boundary depends on the Action Contract.

⸻

75. Persistence After Execution

Noema must also handle:

Action succeeded
      ↓
Outcome persistence failed

This creates an uncertain observation state.

The system should recover through:

reconciliation
idempotency
external query
execution lookup

rather than assuming the Action failed.

⸻

76. Persistence and Exactly-Once Logical Effects

Noema can combine:

durable Execution identity
+
idempotency
+
reconciliation

to achieve reliable logical execution even when infrastructure provides only at-least-once delivery.

⸻

77. Persistence and Action Recovery

After restart:

Execution:
RUNNING
Last known:
Attempt 1 = TIMEOUT

Noema should not simply execute Attempt 2.

It should determine:

Did Attempt 1 execute?
Did the enterprise commit the Action?
Is the Action idempotent?
Is reconciliation required?

Persistence provides the historical inputs for this reasoning.

⸻

78. Persistence and Compensation Recovery

Similarly:

Execution:
PARTIAL

may require recovering:

completed Actions
failed Actions
available compensation Actions
current enterprise state

before compensation can safely proceed.

⸻

79. Persistence and Human Approval

If an Execution waits for approval:

WAITING_FOR_APPROVAL

that state must survive:

process restart
worker replacement
network failure
deployment

Approval Evidence should also remain associated with the relevant Action.

⸻

80. Persistence and Clarification

Likewise:

Intent:
AMBIGUOUS
waiting_for:
user clarification

must survive beyond the original request.

A clarification response must be associated with the correct Intent version and context.

⸻

81. Persistence and Intent Versioning

Intent may evolve.

Intent v1
"Refund my last payment."
Clarification
Intent v2
"Refund payment #123."

Persistence should preserve the relationship between versions.

⸻

82. Persistence and Context Versioning

Context can also change.

Context v1
payment.status = SUCCEEDED
Context v2
payment.status = REFUNDED

Noema should be able to distinguish these snapshots.

⸻

83. Persistence and Evidence Versioning

Evidence can be superseded.

Evidence v1:
status = PENDING
Evidence v2:
status = SUCCEEDED

The history should remain reconstructible.

⸻

84. Persistence and Policy Versioning

A Trust decision should identify which Policy version was evaluated.

Policy:
refund-policy
version:
12

This prevents historical decisions from becoming ambiguous after policy changes.

⸻

85. Persistence and Integration Versioning

The same principle applies to integration mappings.

If:

Payment API mapping v2

interpreted:

"completed" → SUCCEEDED

historical executions should retain the mapping version used when that interpretation mattered.

⸻

86. Persistence and Schema Versioning

Persistent objects should carry enough schema information to remain interpretable.

Example:

Execution schema = 4
Action Contract = refund.v3
Policy = refund-policy.v12

This provides semantic stability across system evolution.

⸻

87. Persistence and Migration

Migration must preserve semantic meaning.

A schema migration should not silently change historical meaning.

For example:

FAILED

must not become:

UNKNOWN

simply because a new schema uses different state definitions.

⸻

88. Persistence and Data Lineage

Persisted records should preserve relationships between:

Intent
Evidence
Decision
Action
Execution
Outcome

This forms the Noema execution lineage.

⸻

89. Persistence and the Execution Record

The Execution Record is the central durable object.

Conceptually:

Execution Record
 ├── execution_id
 ├── intent_id
 ├── action
 ├── resource_refs
 ├── context_snapshot
 ├── trust_decision
 ├── evidence_refs
 ├── attempts
 ├── state
 ├── outcome
 ├── timestamps
 └── versions

The physical implementation may differ.

⸻

90. Persistence and the Audit Record

The Audit Record answers:

What happened, when, why, and based on what information?

It should reference rather than duplicate large amounts of data wherever possible.

⸻

91. Persistence and References

Noema should prefer stable references when the underlying enterprise data remains externally authoritative.

Example:

payment_id = 123
source = Payment System

rather than maintaining a shadow copy of the entire Payment record.

⸻

92. Persistence and Referential Integrity

References to enterprise resources should preserve enough identity to avoid ambiguity.

A bare:

123

may be insufficient.

A more useful semantic reference may include:

resource_type
resource_id
system
tenant
scope

⸻

93. Persistence and Resource Deletion

If an enterprise Resource is later deleted, historical Noema records should still be able to indicate what Resource the Execution originally targeted.

Therefore references used for audit should not depend entirely on the continued existence of the live enterprise record.

⸻

94. Persistence and Privacy

Persistence must minimize unnecessary replication of sensitive information.

Where possible:

reference
+
provenance
+
minimal necessary value

should be preferred over complete enterprise record duplication.

⸻

95. Persistence and Encryption

Depending on enterprise requirements, persisted data may require:

encryption at rest
encryption in transit
key management
field-level protection
secret isolation

Secrets should not be persisted merely because they appeared in an integration payload.

⸻

96. Persistence and Secrets

Credentials, tokens, API keys, and other secrets should not become ordinary Execution data.

Persistence must explicitly distinguish:

execution metadata

from:

credentials

Secret material belongs in an appropriate secret-management system.

⸻

97. Persistence and Audit Redaction

Auditability does not require storing every raw value.

Sensitive fields may require:

redaction
tokenization
hashing
masking
reference

while preserving enough information to reconstruct the decision.

⸻

98. Persistence and Searchability

Noema’s persisted records should be queryable by stable identifiers such as:

intent_id
execution_id
resource_id
principal_id
idempotency_key
correlation_id

This supports operational recovery and audit investigation.

⸻

99. Correlation

Related records should share a correlation identity.

Intent
   │
   └── correlation_id
          │
          ├── Trust
          ├── Action
          ├── Execution
          └── Outcome

This allows distributed components to reconstruct a single execution journey.

⸻

100. Persistence and Observability Correlation

Where possible, Noema should connect:

execution_id
correlation_id
trace_id
request_id
external operation ID

This creates a bridge between semantic execution records and infrastructure diagnostics.

⸻

101. Persistence and External Operation IDs

External systems may assign their own operation identifiers.

Example:

Noema:
execution_id = exec_123
Payment System:
operation_id = payop_987

The relationship should be persisted.

This is particularly important for reconciliation.

⸻

102. Persistence and Reconciliation Identity

A recovery process should be able to search the enterprise system using durable identifiers such as:

idempotency key
external operation ID
resource ID
transaction ID

Persistence should preserve these identifiers where available.

⸻

103. Persistence and Recovery Semantics

Recovery should be defined as:

Reconstructing the last known Noema Execution state, determining what remains uncertain, revalidating the relevant enterprise state, and selecting the next permitted deterministic transition.

Not:

“Continue executing from wherever the process stopped.”

⸻

104. Persistence and State Reconstruction

A recovered Execution should be reconstructable from durable information:

Intent
+
Intent version
+
Context
+
Evidence
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

105. Persistence and Stale State

Persisted state can become stale.

Therefore the persistence layer should make temporal semantics visible.

Example:

last_known_status = ACTIVE
observed_at = 09:00

This is preferable to:

status = ACTIVE

without temporal context.

⸻

106. Persistence and Revalidation Windows

Some Actions may define maximum acceptable evidence age.

Example:

balance evidence:
max_age = 30 seconds

On recovery:

evidence age > 30 seconds

may require revalidation before execution.

⸻

107. Persistence and Durable Decisions

A Trust Decision should not be treated as permanently valid merely because it was once persisted.

For mutable or high-risk Actions:

old Trust Decision
      ↓
current Context changed
      ↓
re-evaluate

Persistence preserves the historical decision; it does not freeze reality.

⸻

108. Persistence and Policy Changes

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

⸻

109. Persistence and Long-Running Intent

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
Revalidate
 ↓
Continue / Re-evaluate

Persistence makes the pause safe.

⸻

110. Persistence and Workflow State

Noema’s workflow state should describe execution semantics rather than duplicating enterprise workflow systems.

Noema may know:

WAITING_FOR_APPROVAL

without owning the enterprise’s:

approval workflow database

unless explicitly integrated as an enterprise capability.

⸻

111. Persistence and System of Record

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

112. Persistence and Canonical Data

Persisted references to Canonical Data should identify:

source
authority
observation time
resource
version

where needed.

This preserves the distinction between:

canonical enterprise fact

and:

Noema's observation of that fact

⸻

113. Persistence and Evidence Retention

Evidence retention should correspond to how long the evidence is necessary to explain or reconstruct a decision.

High-consequence Actions may require stronger retention than low-risk informational interactions.

⸻

114. Persistence and Risk

Persistence requirements may increase with Action risk.

For example:

Low risk:
read-only query
High risk:
transfer funds

The second may require stronger:

audit
immutability
evidence retention
versioning
reconciliation

⸻

115. Persistence and Risk-Adaptive Durability

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

The exact policy belongs to the enterprise configuration.

⸻

116. Persistence and Informational Requests

Not every user interaction requires a durable Execution record.

For a purely informational query:

“What’s my account balance?”

Noema may only need ephemeral runtime Context, depending on enterprise requirements.

For:

“Transfer $10,000.”

durable Execution state is substantially more important.

⸻

117. Persistence and Ephemeral State

Ephemeral state is acceptable when losing it does not create an unsafe or unauditable condition.

Examples:

temporary model output
intermediate parsing artifacts
cache entries
short-lived UI state

The boundary must be explicit.

⸻

118. Persistence and Model Outputs

Raw LLM outputs should not automatically become durable canonical records.

Noema should persist model output when necessary for:

debugging
audit
evaluation
reproducibility

subject to data-retention requirements.

More importantly, Noema should persist the semantic result that affected execution, not blindly retain every intermediate token or generation.

⸻

119. Persistence and Deterministic Replay

Replay can be useful for debugging and auditing.

A replayable Execution may require:

Intent
Context snapshot
Evidence
Policy version
Action Contract version
Trust configuration
integration semantics

Replay should distinguish:

historical reconstruction

from:

re-executing the Action

The latter must never occur accidentally during replay.

⸻

120. Persistence and Safe Replay

Replay must be non-executing by default.

Reconstructing:

"what would Noema have decided?"

must not dispatch:

refund_payment()

unless an explicit execution path is invoked.

⸻

121. Persistence and Testing

Persisted execution histories can become test fixtures.

Example:

Intent
+
Evidence
+
Policy
+
Action
+
Outcome

can be replayed against a new Trust implementation to detect behavioral changes.

This supports regression testing of Noema’s deterministic layer.

⸻

122. Persistence and Versioned Semantics

Historical records should be interpretable under the semantic versions that produced them.

For example:

Intent Model v4
Trust Model v7
Action Contract v3
Policy v12

This supports reliable audit and regression analysis.

⸻

123. Persistence and Migration Safety

When semantics change, Noema should avoid silently rewriting historical execution meaning.

Historical:

EXECUTE

should remain historically:

EXECUTE

even if current policy would now produce:

CLARIFY

The distinction between historical and current evaluation must remain explicit.

⸻

124. Persistence and Current Evaluation

Noema may re-evaluate historical executions for analysis.

That produces a new evaluation:

Historical Decision:
EXECUTE
Current Policy Re-evaluation:
CLARIFY

The new result must not overwrite the original historical decision.

⸻

125. Persistence and Audit Trail

A complete audit trail may look like:

Intent received
      ↓
Intent resolved
      ↓
Context captured
      ↓
Evidence collected
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

126. Persistence and Recovery Example

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
Payment = REFUNDED
        ↓
record Evidence
        ↓
Outcome = SUCCESS

No duplicate refund is issued.

⸻

127. Persistence and Failure Modes

Persistence architecture must account for:

database unavailable
partial write
duplicate write
lost acknowledgment
network partition
worker crash
storage corruption
replication lag
schema mismatch

The execution model must explicitly define the resulting Noema state.

⸻

128. Persistence and Partial Writes

If part of an Execution record is written successfully while another part fails, Noema must not assume the record is complete.

Use of:

transactions
write-ahead logs
versioning
reconciliation

may be appropriate depending on implementation.

⸻

129. Persistence and Duplicate Writes

Retries at the persistence layer can produce duplicate records.

Consequential records should therefore have stable identifiers and idempotent write semantics where necessary.

⸻

130. Persistence and Corruption

If persisted Execution state becomes inconsistent:

Execution = COMPLETED
Attempt = RUNNING

Noema should not silently choose one.

It should enter a defined recovery or reconciliation path.

⸻

131. Persistence and Availability

Durability and availability can conflict.

Noema should define which operations may proceed when persistence is degraded.

For high-risk Actions:

persistence unavailable
        ↓
do not execute

may be appropriate.

For low-risk read-only interactions:

persistence unavailable
        ↓
serve request without durable history

may be acceptable.

This must be policy-driven.

⸻

132. Persistence and Enterprise Requirements

Enterprise deployments may impose:

data residency
retention periods
legal hold
audit requirements
encryption standards
access controls
tenant isolation
regional storage

Noema persistence must be configurable to satisfy these requirements.

⸻

133. Persistence and Data Residency

Where enterprise policy requires regional storage, Noema should ensure persisted data remains within the permitted boundary.

This is especially relevant for:

Evidence
Context
Audit records
Identity information
Execution metadata

⸻

134. Persistence and Data Classification

Persisted information may have classifications such as:

PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED

Classification should influence:

storage
access
retention
encryption
replication

⸻

135. Persistence and Access Logging

Access to sensitive persisted records may itself require auditability.

For example:

Operator viewed Evidence for Execution #123

may need to become an audit event depending on enterprise requirements.

⸻

136. Persistence and System Boundaries

Noema may interact with multiple persistence systems:

Operational Store
Audit Store
Event Store
Cache
Secret Store
Enterprise Systems

These stores should have explicit ownership and semantics.

⸻

137. Persistence Is a Semantic Boundary

The persistence layer should preserve the distinction between:

current operational state
historical observation
enterprise reference
evidence
audit record

A single database table does not eliminate these semantic distinctions.

⸻

138. Recommended Conceptual Storage Model

A logical persistence model may contain:

Intent
IntentVersion
ContextSnapshot
Evidence
TrustEvaluation
PolicyReference
Action
Execution
ExecutionAttempt
Outcome
Failure
Intervention
AuditRecord

This is a conceptual model, not a mandatory relational schema.

⸻

139. Core Relationships

Intent
  │
  ├── has_versions → IntentVersion
  │
  └── creates → Execution
Execution
  ├── uses → ContextSnapshot
  ├── references → Evidence
  ├── evaluates → TrustEvaluation
  ├── invokes → Action
  ├── contains → ExecutionAttempt
  ├── produces → Outcome
  └── may_create → Intervention

⸻

140. Persistence and the Noema Architecture

The persistence layer sits beneath the semantic execution lifecycle:

                Intent
                  │
                  ▼
             Intent Model
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
               Action
                  │
                  ▼
             Execution
                  │
                  ▼
              Outcome
                  │
                  ▼
             Persistence

Persistence records the journey rather than replacing the systems involved in the journey.

⸻

141. Core Invariants

Invariant 1

Noema must persist information required to remain recoverable, deterministic, and auditable.

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

Persisted Context is historical context, not automatically current enterprise state.

Invariant 8

Persisted Trust Decisions are historical decisions and do not automatically remain valid forever.

Invariant 9

Evidence required to reconstruct consequential decisions should be durably referenced or retained.

Invariant 10

Historical records must preserve relevant Policy, Action Contract, and semantic versions.

Invariant 11

Execution attempts must be distinguishable.

Invariant 12

Idempotency information must survive whenever required to prevent duplicate logical execution.

Invariant 13

Unknown execution outcomes must remain explicitly represented.

Invariant 14

Persistence must not convert an uncertain outcome into success or failure without sufficient evidence.

Invariant 15

Recovery must revalidate mutable enterprise state before continuing consequential execution.

Invariant 16

Historical records must not be silently rewritten to reflect current policy or current enterprise state.

Invariant 17

Replay must not accidentally execute Actions.

Invariant 18

Persisted references to enterprise Resources must retain sufficient identity and scope to remain meaningful.

Invariant 19

Persistence must preserve tenant and organizational boundaries.

Invariant 20

Persistence must not bypass enterprise authorization.

Invariant 21

Secrets must not be treated as ordinary execution data.

Invariant 22

Persistence should minimize unnecessary duplication of enterprise data.

Invariant 23

Retention must be appropriate to the semantic and operational purpose of the data.

Invariant 24

Consequential audit records should have stronger integrity guarantees than ordinary mutable operational state where required.

Invariant 25

Persistence failures must produce explicit system states rather than silent loss of execution history.

Invariant 26

Noema should not execute high-consequence Actions when required durable execution state cannot be safely recorded.

Invariant 27

Persistence must support reconciliation when execution state and enterprise state diverge.

Invariant 28

Concurrent updates to Execution state must not produce invalid or contradictory transitions.

Invariant 29

Historical execution records must remain interpretable across schema evolution.

Invariant 30

Noema should persist enough information to answer:

What happened, what was known, what was trusted, what was executed, and what ultimately occurred?

⸻

142. Final Definition

Persistence is the durable memory of Noema’s execution system: it preserves the Intent, evidence, decisions, state transitions, Actions, attempts, and outcomes necessary for recovery, auditability, reconciliation, and deterministic continuation without becoming the System of Record for enterprise Business State.

The fundamental architecture is:

              ENTERPRISE
                  │
          Authoritative State
                  │
                  ▼
             Integration
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
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      History   Recovery   Audit
        │         │         │
        └─────────┼─────────┘
                  ▼
            Reconciliation
                  │
                  ▼
              ENTERPRISE

The key principle is:

Persistence gives Noema memory, not ownership. It remembers what Noema knew, decided, and did so that execution can survive failure and remain accountable—while enterprise systems remain authoritative for enterprise state.