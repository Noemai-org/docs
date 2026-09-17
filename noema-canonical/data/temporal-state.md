Temporal State

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/temporal-state.md

⸻

1. Definition

Temporal State is Noema’s representation of how relevant facts, observations, context, evidence, enterprise state, knowledge state, decisions, executions, and outcomes relate to time.

Noema must distinguish between:

* what is true now
* what was true at a particular time
* what was observed at a particular time
* when Noema received that observation
* what Noema knew at the time
* what Noema inferred at the time
* what was decided at the time
* what changed after an Action
* what was verified later

Temporal State exists because state is not timeless.

⸻

2. Purpose

An enterprise environment is continuously changing.

Source of Intent
      ↓
Validated / Admitted Intent
      ↓
Context + Observations
      ↓
State Reconciliation
      ↓
Fact Status / Evidence
      ↓
Deterministic Trust
      ↓
Action / Execution
      ↓
Verification
      ↓
Outcome
      ↓
Operational Memory / Audit

The information available at each stage may differ.

For example:

10:00
Account balance observed = $20,000
10:02
Trust Decision = EXECUTE
10:03
Another transaction reduces balance to $5,000
10:04
Transfer executes

Noema must preserve the distinction between the balance observed at 10:00 and the balance that exists at 10:04.

⸻

3. Core Principle

Noema must never confuse historical state with current state.

A historical observation may explain a historical decision without being sufficient to authorize a new Action.

Temporal validity is therefore always relative to:

* the claim
* the Action
* the resource
* the policy
* the authority
* the relevant time
* the required freshness

⸻

4. State Is Time-Bound

A state should be understood as:

State + Time + Scope

rather than simply:

State

For example:

account.status = ACTIVE
observed_at = 10:00

is incomplete without knowing:

* which account
* which system
* which environment
* which tenant or organization
* the source authority
* when the state was observed
* when the state was effective
* whether the observation remains usable for the intended Action

⸻

5. Temporal State vs Current State

Current state answers:

What is true now?

Temporal State answers:

What was true, observed, known, or applicable at a particular point in time?

Both are necessary.

Current state is required when a consequential Action depends on present enterprise truth.

Historical state is required when reconstructing a prior decision, execution, failure, or Outcome.

⸻

6. Enterprise State Ownership

Noema does not become the authoritative owner of enterprise state.

For example:

Banking System
    owns:
    account balance
Noema
    records:
    observed balance
    observation time
    provenance
    authority reference
    Fact Status

The external System of Record remains authoritative within its defined domain.

Noema may preserve observations and references to enterprise state without creating a shadow System of Record.

⸻

7. Temporal State and Provenance

Temporal State and Provenance are closely related.

Provenance answers:

Where did this information come from?

Temporal State answers:

When did this information apply, become observable, or become known?

Together:

Claim
 ├── Provenance
 └── Temporal context

Neither provenance nor temporal metadata alone establishes truth or authority.

⸻

8. Temporal Dimensions

Noema should distinguish, where applicable:

valid time
effective time
event time
observation time
receipt time
recording time
decision time
execution time
processing time
outcome occurrence time
outcome observation time
expiration time
invalidation time

These timestamps have different semantics and must not be collapsed into a generic timestamp.

⸻

9. Event Time

event_time represents when an event occurred according to its source.

For example:

event_time = 10:00

does not imply that Noema received or processed the event at 10:00.

⸻

10. Observation Time

observed_at represents when the source state or fact was observed.

Example:

balance = $10,000
observed_at = 10:00

This does not imply that Noema received it at 10:00.

⸻

11. Receipt Time

received_at represents when Noema received an observation or event.

Example:

observed_at = 10:00
received_at = 10:02

The distinction matters in distributed systems.

⸻

12. Processing Time

processed_at represents when Noema processed an event, observation, or message.

It is distinct from:

event_time
observed_at
received_at

Processing order must not automatically be treated as domain-event order.

⸻

13. Recording Time

recorded_at represents when Noema durably recorded the relevant record.

Recording time is a persistence property and does not establish when the underlying fact became true.

⸻

14. Effective Time

effective_at represents when a state, policy, relationship, permission, or configuration becomes applicable.

This may differ from when the source recorded the change.

⸻

15. Decision Time

A Trust Decision has its own temporal position.

decision_at = 10:03

The Evidence used by the decision may have been observed earlier.

A historical Trust Decision must preserve the relevant temporal context under which it was made.

⸻

16. Execution Time

An Action may execute later:

executed_at = 10:04

Therefore:

observation
    ↓
decision
    ↓
execution

are separate temporal events.

For asynchronous Actions, submission time and external completion time may be different again.

⸻

17. Outcome Time

An Outcome may occur or become observable later still.

For example:

outcome_occurred_at = 10:05
outcome_observed_at = 10:06

These are not necessarily the same.

Noema must distinguish the occurrence of an enterprise event from when Noema learned about it.

⸻

18. Temporal Chain

A complete Execution may therefore have:

10:00  Observation
10:01  Intent resolution
10:02  Trust evaluation
10:03  Trust Decision
10:04  Action submission
10:05  External state change
10:06  Outcome observation

Noema should preserve this sequence and the causal relationships between its records.

⸻

19. Temporal State Is Not Event Sourcing

Temporal State does not require Noema to implement full event sourcing.

The concept is semantic:

Relevant state and observations must remain interpretable in time.

The underlying implementation may use:

* event logs
* snapshots
* versioned records
* temporal tables
* immutable observations
* append-only records
* current projections
* combinations of these

⸻

20. State Snapshots

A snapshot represents state as observed or assembled at a particular point.

Example:

Context Snapshot #42
identity = user/123
balance = $20,000
subscription = ACTIVE
policy_version = 7
captured_at = 10:00

The snapshot is historical.

It must not automatically be interpreted as current enterprise state.

⸻

21. Context Snapshots

Context used for Trust evaluation should be associated with the time at which it was assembled.

Context
    ↓
captured_at
    ↓
Evidence versions
    ↓
State Reconciliation inputs/results

A Context Snapshot records the runtime view used by Noema.

It does not establish that every value within it was authoritative, current, or permitted for every possible purpose.

⸻

22. Snapshot vs Live State

A persisted snapshot is a historical runtime representation.

Live enterprise state is obtained from the applicable authoritative System of Record or approved source.

Therefore:

Persisted Snapshot ≠ Current Enterprise Truth

Persistence does not upgrade a historical observation into authority.

⸻

23. Temporal Context

Context may contain facts observed at different times.

Example:

identity:
10:00
balance:
10:01
policy:
09:00
payment:
10:02

Therefore a Context is not necessarily a single instant.

Noema should preserve the temporal metadata of components when it materially affects interpretation or execution safety.

⸻

24. Context Consistency Window

For some Actions, Evidence gathered over a long period may be undesirable.

A policy may require:

all critical Evidence
observed within 60 seconds

This creates a temporal consistency requirement.

The requirement belongs to policy, Action semantics, risk policy, or integration guarantees rather than being invented by the temporal subsystem.

⸻

25. Temporal Coherence

A Trust decision should evaluate whether its Evidence is temporally coherent for the Action.

For example:

Identity:
5 minutes old
Account balance:
5 seconds old
Authorization:
2 hours old

The Action may require revalidation because the Evidence was assembled across incompatible freshness windows.

⸻

26. Freshness

Freshness describes how old an observation is relative to the point at which it is being used.

Conceptually:

freshness_age = evaluation_time - observed_at

The acceptable threshold is policy-, Action-, risk-, and integration-dependent.

⸻

27. Freshness Is Not Truth

An old observation is not necessarily false.

It may simply no longer be suitable for a particular decision.

For example:

Observed:
balance = $20,000

can remain historically valid while being unsuitable for a transfer authorization five minutes later.

⸻

28. Fact Status and Temporal Validity

Fact Status is distinct from temporal metadata.

Noema may represent Fact Status as:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Temporal metadata helps determine Fact Status, but does not define it alone.

For example:

observed_at = 10:00
current time = 10:10

does not automatically mean STALE.

Whether the observation is stale depends on the claim, Action, policy, risk, and required freshness.

⸻

29. Evidence Expiration

Evidence may have a maximum usable age.

Example:

balance:
max_age = 30 seconds

After the applicable threshold:

Fact Status = STALE

The historical observation remains intact.

⸻

30. Temporal Validity

Some information has an explicit validity interval.

Example:

Policy A:
valid_from = Jan 1
valid_until = Jun 30

Noema should determine whether the policy was applicable at the relevant decision or execution time.

⸻

31. Valid Time and Transaction Time

Temporal systems commonly distinguish:

Valid Time

from:

Transaction Time

Valid Time asks:

When was this fact true in the domain?

Transaction Time asks:

When did the system record the fact?

Noema should preserve both where the distinction matters.

⸻

32. Effective Time vs Observation Time

Example:

Employee promotion
effective_at = Jan 1
recorded_at = Jan 3

The promotion applies from Jan 1 even though Noema only learned about it on Jan 3.

These timestamps must not be conflated.

⸻

33. Historical Truth

Suppose:

Account status:
ACTIVE

at 10:00.

At 10:10:

Account status:
SUSPENDED

A historical execution at 10:02 should retain:

status = ACTIVE

as the state observed or established for that historical decision, with its provenance and temporal scope.

⸻

34. Current Truth

At 10:10, a new Action should consult current authoritative state when current state is required.

The historical ACTIVE observation should not be reused merely because it was once valid.

⸻

35. Temporal State and State Reconciliation

State Reconciliation is a first-class Noema capability.

Temporal State provides the observations and historical records needed for reconciliation.

It does not perform reconciliation itself.

Conceptually:

Observation
     ↓
State Reconciliation
     ↓
Fact / Reconciled State

Conflicts, missing observations, eventual consistency, and unknown state must remain explicit.

⸻

36. Temporal State and Reconciliation History

Noema should preserve, where material:

* reconciliation identity
* observations considered
* source identities
* source versions
* temporal metadata
* reconciliation time
* resulting Fact Status
* conflicts identified
* resolution basis
* references to the resulting decision

A later reconciliation creates new knowledge; it does not rewrite the historical observation.

⸻

37. Temporal State and Decision Reconstruction

A Trust Decision should be reconstructable using the state and Evidence available at the decision time.

Conceptually:

Decision D1
    ↓
Context Snapshot C1
    ↓
Evidence E1...En
    ↓
State Reconciliation R1
    ↓
Temporal State at D1

The historical decision must not be reconstructed by silently substituting current enterprise state.

⸻

38. Temporal State and Determinism

Deterministic Trust evaluation requires deterministic temporal inputs.

If a policy says:

balance must be ≥ $10,000

Noema must know:

Which balance?
Observed when?
From which authority?
With what Fact Status?
Applicable to which Action?

Otherwise the same decision may produce different results depending on when it is replayed.

⸻

39. Temporal Determinism

Historical replay should use:

* historical Evidence
* historical Policy
* historical Context
* historical Action Contract
* historical Intent version
* relevant historical graph/capability versions
* historical reconciliation results
* historical model version where material

rather than silently querying current enterprise state.

⸻

40. Temporal State and Replay

For example:

2026-08-20
Trust Decision = EXECUTE

Historical replay should reconstruct:

what Noema knew and evaluated on 2026-08-20

not:

what the enterprise system says today.

⸻

41. Historical Replay vs Modern Re-Evaluation

These are different operations.

Historical replay

Reconstructs the original semantic computation using historical inputs and versions.

Modern re-evaluation

Runs current rules, current policies, current schemas, and potentially current models against historical or current data.

Modern re-evaluation must not overwrite the original historical interpretation.

⸻

42. Temporal State and Revalidation

Revalidation is intentionally different from historical replay.

It asks:

Does the Action remain valid under current state?

Therefore:

Historical Decision
      ↓
Current State
      ↓
Re-evaluation

This is a new evaluation.

⸻

43. Historical Decision vs Current Decision

These should remain separate:

Historical:
EXECUTE
Current revalidation:
REJECT

The latter does not rewrite the former.

⸻

44. Temporal State and Long-Running Execution

Long-running Actions are especially sensitive to temporal state.

Example:

Intent accepted
      ↓
Approval obtained
      ↓
Execution delayed 2 hours

During those two hours:

* permissions may change
* account state may change
* policy may change
* resource state may change
* Evidence may expire
* Action Contract semantics may change
* external operation windows may expire

Noema must know which conditions require revalidation.

⸻

45. Temporal Preconditions

A Precondition may include a freshness requirement:

beneficiary_verified
observed within 5 minutes

or:

account_status
must be current

The exact temporal requirement must be deterministic and contractually defined.

⸻

46. Temporal Postconditions

Postconditions are also time-bound.

Example:

payment.status = REFUNDED
verified_at = 10:05

does not necessarily mean the payment will remain refunded forever.

The postcondition establishes what was verified at the relevant time.

⸻

47. Temporal State and Idempotency

Idempotency is inherently temporal.

Noema may need to determine:

Has this Action already been executed?

The answer depends on historical execution state and the applicable idempotency semantics.

⸻

48. Temporal State and Duplicate Execution

Example:

10:00
refund request submitted
10:01
network timeout
10:02
retry begins

Noema must inspect temporal execution history before issuing another external Action.

If the previous attempt may have succeeded, reconciliation should occur before retry where required.

⸻

49. Temporal State and Unknown Outcomes

A timeout does not establish failure.

10:00
Action submitted
10:01
No response

The external system may have executed the Action.

Noema must be able to represent:

Outcome = UNKNOWN

until new Evidence establishes what occurred.

⸻

50. Temporal State and Reconciliation of Unknown

Later:

10:05
Payment System:
REFUNDED

Noema can reconcile the unknown execution.

The historical sequence remains:

submitted
→ unknown
→ reconciled
→ verified refunded

The later observation does not erase the earlier unknown state.

⸻

51. Temporal State and Event Ordering

Distributed systems may deliver events out of order.

Example:

Event B received
Event A received

while:

A occurred before B

Noema should preserve source event time and identifiers where possible.

Receipt order must not automatically become domain order.

⸻

52. Late Events

A late event may describe an earlier state transition.

Example:

10:00
event occurred
10:05
event received

Noema should not automatically interpret receipt order as domain-event order.

⸻

53. Event Versioning

Events may change schema over time.

Historical events should retain:

event_type
event_version

so their original semantics remain interpretable.

Transport/schema version and semantic contract version should remain distinguishable where necessary.

⸻

54. Temporal State and Eventual Consistency

Different enterprise systems may converge at different times.

Example:

Payment System:
REFUNDED
Reporting System:
PENDING

Both observations may be temporally valid from their respective perspectives.

Noema should preserve the temporal and source dimensions rather than flattening them into one value.

State Reconciliation determines whether a coherent current fact can be established.

⸻

55. Temporal State and Source Authority

Temporal conflict resolution must consider:

* source authority
* event time
* effective time
* observation time
* scope
* version
* Fact Status

A newer observation is not automatically more authoritative.

⸻

56. Temporal State and Conflicting Evidence

Example:

10:00 Identity System:
ACTIVE
10:01 CRM:
ACTIVE
10:02 Identity System:
SUSPENDED

The Trust Engine should evaluate the appropriate authoritative source and temporal applicability rather than simply selecting the latest value.

⸻

57. Temporal State and Policy Versions

Policies are temporal entities.

Policy v1
effective: Jan 1 – Jun 30
Policy v2
effective: Jul 1 onward

A decision on June 30 must use the policy applicable at that time.

Historical Trust Decisions must preserve the exact policy version that governed them.

⸻

58. Temporal State and Action Contract Versions

Action Contracts may also evolve.

Contract v1
endpoint = /refund
Contract v2
endpoint = /payments/{id}/refund

Historical executions must preserve the Action Contract version used.

A later Contract version must not silently reinterpret a historical execution.

⸻

59. Temporal State and Intent Versions

Intent Objects are immutable once admitted to Trust.

A material change creates a new Intent version:

Intent v1
     ↓
supersedes
     ↓
Intent v2

Clarification that materially changes the semantic request creates a new Intent version.

Historical Trust and Execution records must reference the exact Intent version used.

⸻

60. Temporal State and Configuration

Configuration may change over time.

Example:

approval_threshold:
$10,000

then:

approval_threshold:
$5,000

Historical decisions must retain the configuration or configuration version applicable at decision time.

⸻

61. Temporal State and Identity

Identity assertions are temporal.

A user may:

* gain a role
* lose a role
* change organization
* lose access
* change authorization scope

Therefore authorization should consider the identity and permission state applicable to the relevant time.

⸻

62. Temporal State and Permissions

Example:

10:00
user = finance-admin
10:05
role revoked
10:06
Action executes

A permission check performed at 10:00 may not necessarily remain sufficient at 10:06.

Whether revalidation is required is determined by policy and Action risk.

⸻

63. Temporal State and Authorization

Authorization may therefore be modeled as:

Principal
+
Permission
+
Resource
+
Action
+
Scope
+
Time

rather than merely:

Principal
+
Permission

Technical authorization, policy authorization, and business authorization remain distinct.

⸻

64. Temporal State and Organizational Boundaries

Organizational membership can change.

Employee
    Organization A

may become:

Employee
    Organization B

Temporal state determines which organizational boundary applied at a given time.

⸻

65. Temporal State and Business State

Noema observes enterprise business state but does not own it.

Examples:

order = SHIPPED
invoice = PAID
subscription = ACTIVE
account = SUSPENDED

These states should retain their temporal context when relevant to execution, reconciliation, recovery, or audit.

⸻

66. State Transitions

Business state is often better represented as transitions:

PENDING
   ↓
APPROVED
   ↓
EXECUTED
   ↓
COMPLETED

rather than only the latest value.

Historical transitions may matter for:

* audit
* recovery
* reconciliation
* compensation
* debugging

⸻

67. State History

Where relevant, Noema should retain enough information to reconstruct meaningful state history.

Example:

10:00 PENDING
10:02 APPROVED
10:03 EXECUTING
10:05 COMPLETED

This applies to Noema-owned execution state and, through observations/references, to relevant enterprise state.

⸻

68. Temporal State and Noema State

Noema itself has state:

* Intent State
* Trust Decision State
* Execution State
* Recovery State
* Case / Intervention State
* Outcome State

These are distinct from enterprise business state.

Noema may own its own temporal execution state while only observing enterprise temporal state.

⸻

69. Intent State Over Time

An Intent may move through:

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

Other explicit states may include:

CLARIFICATION_REQUIRED
PARTIALLY_FULFILLED
FAILED
CANCELLED
UNKNOWN
EXPIRED

Intent status is distinct from Trust outcome.

⸻

70. Trust State Over Time

Trust evaluation may move through:

EVALUATING
   ↓
DECIDED

with the resulting Trust outcome:

EXECUTE
CLARIFY
ESCALATE
REJECT

A previously valid Trust Decision may later become invalid for a new execution attempt because temporal conditions changed.

⸻

71. Execution State Over Time

Execution may move through:

PLANNED
   ↓
READY
   ↓
RUNNING
   ↓
SUCCEEDED

or:

RUNNING
   ↓
UNKNOWN
   ↓
RECONCILING
   ↓
SUCCEEDED

Temporal state preserves this journey.

⸻

72. Temporal State and Trust Invalidation

A Trust Decision can become stale.

Example:

10:00
Trust = EXECUTE
10:10
authorization revoked

The original Trust Decision remains a historical decision.

It may no longer authorize a new execution attempt.

⸻

73. Temporal Trust Validity

A Trust Decision may therefore have:

issued_at
valid_until
invalidated_at

where applicable.

Validity is scoped to the Intent version, Action, target, Evidence, policy, and execution conditions for which it was issued.

⸻

74. Temporal Trust Is Policy-Driven

Not every Trust Decision needs an expiration.

Required temporal validity depends on:

* risk
* Action
* Evidence
* policy
* execution duration
* integration guarantees
* authorization semantics

Noema must not invent a universal Trust TTL.

⸻

75. Temporal State and Risk

Risk can increase as Evidence ages.

For example:

balance observed:
10 seconds ago → acceptable
balance observed:
1 hour ago → potentially unacceptable

Therefore temporal freshness can directly affect Trust.

⸻

76. Temporal Risk Windows

Policies may define:

high-risk transfer:
balance must be < 30 seconds old
low-risk read:
balance may be < 10 minutes old

The actual requirements are enterprise- and Action-specific.

⸻

77. Temporal State and Clarification

Temporal ambiguity can require clarification.

Example:

“Use the balance from earlier.”

Earlier could mean:

* 10 minutes ago
* today
* last statement
* previous transaction

Noema should not infer temporal meaning when it materially affects execution.

⸻

78. Temporal State and Intent Resolution

Temporal expressions such as:

* last
* previous
* yesterday
* recent
* earlier
* this month

must be resolved against explicit temporal context.

If multiple interpretations remain materially different, the Intent remains ambiguous.

⸻

79. Temporal Intent

An Intent may include temporal constraints.

Example:

refund my last payment

becomes conceptually:

Action:
refund
Resource:
most recent eligible payment
Temporal criterion:
latest according to defined enterprise ordering

The temporal criterion must be explicit enough for deterministic resolution.

⸻

80. Temporal Ordering

“Last payment” should not necessarily mean:

latest created_at

It could mean:

latest successful payment

depending on domain semantics.

Noema should rely on the relevant enterprise semantics rather than inventing an ordering.

⸻

81. Temporal State and Entity Resolution

Temporal state can affect entity identity.

For example:

customer/123

may have been active in 2025 but inactive in 2026.

The relevant identity depends on the Action’s temporal context and enterprise semantics.

⸻

82. Temporal State and Resource Lifecycle

Resources may have lifecycles:

CREATED
   ↓
ACTIVE
   ↓
SUSPENDED
   ↓
DELETED

Noema should know whether a resource existed or was valid at the relevant point in time when that fact affects an execution or historical interpretation.

⸻

83. Temporal State and Deleted Resources

A resource deleted today may still be relevant to a historical Execution.

Deletion should not erase historical references required for audit.

⸻

84. Temporal State and Referential Integrity

Historical references should remain interpretable even when the current resource state changes.

For example:

Execution #123
resource = account/456

should remain understandable even if account/456 is later closed.

⸻

85. Temporal State and Data Retention

Retention policies must balance:

* auditability
* privacy
* storage cost
* legal requirements
* operational requirements

Temporal history should not be retained indefinitely by default.

⸻

86. Temporal State and Data Minimization

Noema should retain temporal information necessary for:

* execution reconstruction
* audit
* recovery
* reconciliation
* policy enforcement
* incident analysis

without indiscriminately copying every historical enterprise state.

⸻

87. Temporal State and Snapshots vs Events

There are two useful representations:

Snapshot:
state at time T

and:

Event:
change occurring at time T

Noema may use either or both.

⸻

88. Snapshot Advantages

Snapshots are useful for:

* fast reconstruction
* Trust evaluation
* Context persistence
* audit views
* recovery

A snapshot remains an observation or projection, not universal authority.

⸻

89. Event Advantages

Events are useful for:

* causal history
* state transitions
* reconciliation
* asynchronous workflows
* temporal ordering

An event is not automatically a fact merely because it was received.

⸻

90. Combined Temporal Model

A practical implementation may use:

Events
   +
Snapshots
   +
Observations
   +
Provenance
   +
Fact Status

to reconstruct temporal state efficiently.

⸻

91. Temporal State and Persistence

Persisted temporal state should distinguish:

* current Noema state
* historical observations
* execution state
* decision history
* reconciliation history
* Outcome history

These should not be collapsed into one mutable record when doing so would destroy auditability or historical meaning.

⸻

92. Mutable vs Immutable State

Operational state may be mutable:

execution.status = RUNNING

while historical transitions should remain reconstructable:

PLANNED → RUNNING

The implementation may use both a current projection and immutable history.

⸻

93. Temporal State and Projections

A current-state projection can be derived from historical observations or state transitions.

Historical Observations
        ↓
State Reconciliation
        ↓
Projection
        ↓
Current View

The projection is replaceable.

Historical records preserve lineage.

⸻

94. Temporal State and Materialized Views

Noema may materialize frequently accessed current state for performance.

But:

Materialized Current View ≠ Complete Historical Truth

A materialized view must remain traceable to the observations or records from which it was derived when traceability is required.

⸻

95. Temporal State and Cache

Caches introduce another temporal dimension.

A cached value should have, where relevant:

observed_at
cached_at
expires_at
source
version

A cache is not authoritative merely because it is recent.

⸻

96. Temporal State and Cache Freshness

A cache may be valid for ordinary operations but unacceptable for high-risk execution.

The Trust Engine should apply policy rather than assuming:

cache hit = current truth

⸻

97. Temporal State and Stale-While-Revalidate

Noema may use stale information temporarily while obtaining fresh information.

But if an Action requires current state:

stale value

must not silently pass the execution gate.

⸻

98. Temporal State and External Latency

High latency increases the gap between:

observation

and:

execution

This can increase temporal risk.

The appropriate response may be:

* revalidation
* conditional execution
* reconciliation
* escalation
* rejection

according to deterministic policy.

⸻

99. Temporal State and TOCTOU

Noema must account for time-of-check vs time-of-use problems.

Example:

10:00
Check: account has sufficient funds
10:05
Execute transfer

The account may have changed between the check and execution.

For consequential Actions, revalidation or atomic enterprise-side guarantees may be required.

⸻

100. Temporal Preconditions and TOCTOU

A precondition evaluated earlier does not necessarily guarantee the same state at execution time.

Therefore policies may require:

check immediately before execution

or:

external transactional guarantee

⸻

101. Temporal State and Concurrency

Multiple Noema executions may operate against changing enterprise state.

Example:

Execution A:
withdraw $8,000
Execution B:
withdraw $5,000

Both may independently observe:

balance = $10,000

Temporal state alone does not solve concurrency.

Enterprise systems may need transactional or concurrency controls.

⸻

102. Temporal State and Concurrency Guarantees

Noema should distinguish:

observed state

from:

atomic guarantee

A historical observation cannot provide an atomic guarantee by itself.

⸻

103. Temporal State and Enterprise Transactions

Where the enterprise system supports transactional preconditions, Noema should prefer those guarantees for consequential Actions.

For example:

transfer only if balance >= amount

may be enforced atomically by the enterprise system.

⸻

104. Temporal State and Action Contracts

Action Contracts should expose temporal semantics where relevant.

Examples:

* idempotency window
* authorization TTL
* resource version
* conditional update
* ETag
* optimistic concurrency token
* execution deadline
* asynchronous completion semantics

⸻

105. Temporal State and Resource Versions

Resource versions can provide strong temporal concurrency semantics.

Example:

resource_version = 42

Action:

update only if version = 42

If the resource has changed:

version = 43

the Action can fail safely or require revalidation rather than applying to stale state.

⸻

106. Temporal State and Optimistic Concurrency

Where supported, Noema should preserve concurrency tokens obtained with Evidence and provide them to Actions that require them.

The token is a constraint supplied by the enterprise integration, not a universal Noema guarantee.

⸻

107. Temporal State and ETags

HTTP-style ETags are one example:

If-Match: "abc123"

This converts an observation into a conditional execution requirement.

It is stronger than relying only on elapsed time.

⸻

108. Temporal State and Preconditions

A strong Precondition may therefore be:

resource_version = 42

rather than merely:

resource.status = ACTIVE

The former protects against certain concurrent modifications.

⸻

109. Temporal State and Postconditions

After execution, Noema should verify the resulting state at a defined temporal point.

Verification should establish what was observed and when, rather than assuming that dispatch itself proves success.

⸻

110. Temporal State and Recovery

Recovery requires temporal awareness.

If Noema crashes after:

Action submitted

it must determine:

what happened before the crash

without assuming that the absence of a local completion record means external failure.

⸻

111. Temporal Recovery

Recovery may therefore involve:

historical execution state
+
external operation state
+
current enterprise state
+
reconciliation

and a new deterministic evaluation of whether execution can continue.

⸻

112. Temporal State and Compensation

Compensation depends on what happened before failure.

Example:

Step 1 succeeded
Step 2 failed

The compensation decision depends on the temporal execution history and the enterprise state established by reconciliation.

⸻

113. Temporal State and Workflow Ordering

Compound Intent requires temporal ordering when Actions depend on one another.

A
 ↓
B
 ↓
C

Noema must preserve which Action happened before which and which dependencies were established.

⸻

114. Temporal State and Causality

Timestamps alone may not establish causality.

Noema should use explicit relationships where available:

caused_by
depends_on
triggered_by
correlates_with
supersedes

Temporal ordering and causality are related but distinct.

⸻

115. Temporal State and Correlation IDs

Correlation identifiers can connect temporal records:

request_id
intent_id
intent_version
execution_id
attempt_id
operation_id
event_id
decision_id
outcome_id

This allows Noema to construct coherent execution timelines.

⸻

116. Temporal State and Event Causality

For example:

Intent
  ↓
Execution
  ↓
External Request
  ↓
External Event
  ↓
Outcome

The relationships should remain explicit.

⸻

117. Temporal State and Ordering Guarantees

Where a source provides ordering guarantees:

* sequence number
* offset
* resource version
* causal identifier

Noema should preserve them.

⸻

118. Temporal State and Distributed Systems

Noema operates across systems that may have:

* clock skew
* network delay
* retries
* duplicate events
* eventual consistency
* asynchronous processing
* independent clocks

Temporal State must therefore be modeled explicitly rather than inferred from local wall-clock time alone.

⸻

119. Temporal State and Clock Skew

Timestamps from different systems may not be directly comparable.

Where temporal precision matters, Noema should prefer:

* source sequence
* logical version
* causal identifier
* enterprise transaction identifier

when available.

⸻

120. Temporal State and Ordering Confidence

Noema should distinguish:

known ordering

from:

unknown ordering

and, where useful for diagnostics:

probable ordering

A model should not silently resolve temporal uncertainty for consequential execution.

⸻

121. Temporal Ambiguity

If the system cannot establish whether:

Event A

occurred before:

Event B

and that ordering affects execution, the appropriate result may be:

REVALIDATION_REQUIRED

or:

ESCALATE

rather than guess.

⸻

122. Temporal State and Deterministic Uncertainty

Unknown temporal ordering should become an explicit system state.

Conceptually:

ORDER_UNKNOWN

is preferable to inventing:

A happened before B

without evidence.

This uncertainty may feed deterministic Trust and State Reconciliation.

⸻

123. Temporal State and Policy Evaluation

Policies can contain temporal constraints:

Action must occur within 10 minutes of approval.

Noema can evaluate:

execution_at - approval_at <= 10 minutes

deterministically.

⸻

124. Temporal Policy Examples

Policies may specify:

* approval freshness
* authentication freshness
* balance freshness
* resource version
* session lifetime
* authorization lifetime
* execution deadline
* compensation window
* idempotency window

⸻

125. Temporal State and Human Approval

Human approval may have a validity period.

approved_at = 10:00
expires_at = 11:00

An Action at 12:00 cannot automatically rely on the same approval.

Approval validity is distinct from Trust outcome and may be an execution precondition.

⸻

126. Temporal State and Authentication

Authentication may also have a freshness requirement.

For example:

authenticated_at = 10:00

may be insufficient for a high-risk Action at 14:00.

The applicable policy determines whether reauthentication is required.

⸻

127. Temporal State and Session State

Session state can change independently of business state.

Noema should preserve the relevant authentication and session context when it contributes to Trust.

Session state must not be treated as universal enterprise authorization.

⸻

128. Temporal State and Identity Revalidation

For high-risk Actions:

historical identity

may require:

current identity verification

before execution.

⸻

129. Temporal State and Policy Changes During Execution

Suppose:

10:00
Policy v5 permits Action
10:05
Policy v6 prohibits Action
10:10
Action executes

Noema must have an explicit policy governing whether the Action uses:

* policy at authorization time
* policy at execution time
* another defined policy anchor

It must not be accidental.

⸻

130. Policy Effective Semantics

The applicable policy point should be defined by the relevant contract or enterprise policy.

Possible anchors include:

* Intent admission
* Trust Decision
* Action start
* Action commit

Different policies may legitimately use different anchors.

⸻

131. Temporal State and Long-Lived Plans

A plan generated today may execute tomorrow.

The plan should therefore distinguish:

plan_creation_time

from:

execution_time

and identify which assumptions require revalidation.

⸻

132. Temporal State and Plan Validity

A plan may have:

valid_until

or require dynamic re-evaluation of its assumptions.

A planner cannot convert stale assumptions into current authority.

⸻

133. Temporal State and Planning Assumptions

Every significant plan assumption should be considered time-sensitive.

Example:

Assumption:
subscription is ACTIVE

If the plan executes later, Noema may need to verify that assumption again.

⸻

134. Temporal State and Execution Preconditions

Planning can produce:

Precondition:
subscription.status = ACTIVE

Execution evaluates it at the appropriate time.

Where the Action Contract supports conditional execution, the precondition should be enforced as close to the consequential operation as possible.

⸻

135. Temporal State and Dynamic Context

Some Context is static:

organization_id

Some is dynamic:

account_balance

Noema should not treat both as having identical temporal behavior.

⸻

136. Temporal State and Context Classification

Useful conceptual categories include:

* Static
* Slow-changing
* Dynamic
* Ephemeral
* Event-derived
* Historical

The required freshness depends on the category and the intended use.

⸻

137. Temporal State and Data Model

A temporal observation may conceptually contain:

TemporalObservation {
    value
    valid_from
    valid_until
    observed_at
    received_at
    recorded_at
    source
    authority
    scope
    version
    fact_status
}

The exact schema is implementation-dependent.

⸻

138. Temporal State and Current Projections

A current projection may be derived:

Historical Observations
        ↓
State Reconciliation
        ↓
Temporal Resolution
        ↓
Current State Projection

The projection should remain traceable to the observations from which it was derived.

⸻

139. Temporal State and Provenance

A temporal observation should therefore conceptually have:

Observation
 ├── value
 ├── temporal metadata
 ├── provenance
 ├── authority reference
 ├── scope
 └── Fact Status

These dimensions should remain separate.

⸻

140. Temporal State and Evidence

Evidence should preserve enough temporal information to determine, where relevant:

* when was this true?
* when was this observed?
* when was this received?
* when was this recorded?
* what version was applicable?
* what authority supplied it?

Evidence supports claims; Evidence is not automatically truth.

⸻

141. Temporal State and Canonical Data

Canonical Data may represent authoritative data within a defined scope.

But canonicality is not universal.

Noema should preserve enough temporal metadata to understand:

* when the value became applicable
* when it was observed
* which version was used
* which source supplied it
* what authority applied
* whether the value was authorized for the intended use

A value being labeled canonical does not make it universally current, accessible, or authoritative for every claim.

⸻

142. Temporal State and Data Lineage

Data lineage becomes:

Source
 ↓
Observation at T1
 ↓
Validation / Admission
 ↓
State Reconciliation
 ↓
Fact Status at T2
 ↓
Trust Decision at T3
 ↓
Action at T4
 ↓
Outcome at T5

This is temporal provenance.

⸻

143. Temporal State and Auditability

A useful audit record should answer:

What did Noema know at the moment it acted?

Not merely:

What does the enterprise system say now?

The audit should preserve the semantic inputs and references necessary to answer the first question without requiring private model chain-of-thought.

⸻

144. Temporal State and Explainability

When explaining a historical decision:

“The transfer was approved because the account had sufficient balance.”

the explanation should be grounded in:

balance observed = $20,000
observed_at = 10:00
decision_at = 10:01
policy = v7
Fact Status = VERIFIED

rather than today’s balance.

⸻

145. Temporal State and Trust Explanation

Likewise:

“The user was authorized.”

should be grounded as:

“The applicable identity system reported that the principal had the required permission for the resolved Action and target when the authorization check was performed.”

The explanation should reference the relevant authority, time, scope, and policy.

⸻

146. Temporal State and Outcome Explanation

For outcomes:

“The refund succeeded.”

should distinguish:

Action submitted

from:

Outcome later verified

A successful dispatch is not automatically a successful enterprise Outcome.

⸻

147. Temporal State and Failure Explanation

A timeout should be explained as:

“No response was received within the configured timeout.”

not:

“The refund failed.”

unless authoritative Evidence establishes failure.

⸻

148. Temporal State and Unknown State

Temporal uncertainty should produce explicit states such as:

UNKNOWN
STALE
EXPIRED
PENDING
REQUIRES_REVALIDATION
ORDER_UNKNOWN

rather than silently converting uncertainty into a definitive state.

⸻

149. Temporal State and Trust Decisions

A Trust evaluation may consider:

Evidence present?
        ↓
Schema valid?
        ↓
Fact Status acceptable?
        ↓
Fresh enough?
        ↓
Temporally applicable?
        ↓
Authoritative?
        ↓
Consistent?
        ↓
Policy satisfied?

These are deterministic evaluation conditions.

⸻

150. Temporal State and Trust Outcomes

The canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Temporal conditions may cause any of these outcomes.

REVALIDATE is not a fifth canonical Trust outcome.

It is an execution-control requirement or state indicating that previously sufficient information or authorization must be evaluated again.

⸻

151. Temporal State and Revalidation

Revalidation means:

The previous Evidence, decision, or assumption may have been valid, but its temporal validity is no longer sufficient for the current execution.

Revalidation must obtain and evaluate the applicable current state rather than mutate the historical decision.

⸻

152. Temporal State and Clarification

CLARIFY is appropriate when the temporal interpretation itself is ambiguous.

Example:

“Use the payment from last week.”

If multiple payments qualify and the temporal criterion does not resolve uniquely, Noema should clarify.

⸻

153. Temporal State and Escalation

ESCALATE may be appropriate when temporal conflict cannot be resolved automatically or when required authoritative information is unavailable.

⸻

154. Temporal State and Rejection

REJECT is appropriate when a temporal constraint is definitively violated.

Example:

Approval expired

The expired approval should not silently authorize execution.

⸻

155. Temporal State and Execution

Before execution:

Temporal Preconditions
        ↓
Current State / Reconciliation
        ↓
Trust Evaluation
        ↓
Action Contract Validation
        ↓
Execution

All required temporal conditions must be satisfied according to the applicable semantics.

⸻

156. Temporal State and Post-Execution

After execution:

Outcome Evidence
        ↓
Temporal Verification
        ↓
Reconciliation
        ↓
Outcome

must establish what happened and when it became known.

⸻

157. Temporal State and Persistence Model

A conceptual persisted record may contain:

TemporalRecord {
    record_id
    subject
    claim
    value
    valid_from
    valid_until
    observed_at
    received_at
    recorded_at
    source
    authority
    scope
    version
    fact_status
}

The exact implementation remains open.

⸻

158. Temporal State and State History

Noema should preserve history where history materially affects:

* Trust
* execution
* recovery
* reconciliation
* audit
* intervention
* causal analysis

Not every transient value requires indefinite retention.

⸻

159. Temporal State and Retention Policy

Retention should be explicitly governed.

For example:

Execution history:
7 years
Operational cache:
15 minutes

The actual durations depend on enterprise policy, legal requirements, data classification, and operational needs.

⸻

160. Temporal State and Privacy

Temporal history may reveal sensitive behavioral information.

Examples:

* when a user accessed a system
* when money moved
* when an employee changed role
* when a customer interacted with an enterprise

Access and retention must therefore be controlled.

⸻

161. Temporal State and Data Minimization

Noema should retain temporal information proportional to its purpose.

Where possible, Noema should retain:

* references
* identifiers
* relevant observations
* semantic Evidence
* provenance

rather than indiscriminately copying complete enterprise payloads.

⸻

162. Temporal State and Integrity

Historical state relevant to audit should be protected from silent modification.

Material corrections should be represented as new observations or correction records rather than destructive replacement.

⸻

163. Temporal State and Tamper Evidence

Where necessary, Noema may use:

* hashes
* signatures
* immutable logs
* version chains
* append-only records

to strengthen temporal history integrity.

Tamper evidence supports audit integrity; it does not establish business-state authority.

⸻

164. Temporal State and Recovery Integrity

Recovery should never assume:

missing record = did not happen

External systems may have progressed independently.

A missing local record may therefore produce:

UNKNOWN

until reconciliation establishes what happened.

⸻

165. Temporal State and External Truth

The System of Record remains the authoritative source for current business state within its defined domain.

Noema’s historical record describes:

* what Noema observed
* what Noema knew
* what Noema decided
* what Noema executed
* what Noema later verified

It does not replace enterprise business authority.

⸻

166. Temporal State and Reconciliation

When local and external state disagree:

Noema:
UNKNOWN
Enterprise:
SUCCEEDED

the authoritative enterprise observation can resolve the local uncertainty.

The historical UNKNOWN state remains part of the execution history.

⸻

167. Temporal State and Eventual Reconciliation

Reconciliation should produce a new temporal observation or reconciliation result rather than rewriting the old state.

Observation 1
    ↓
UNKNOWN
    ↓
Reconciliation
    ↓
Observation 2
    ↓
VERIFIED

⸻

168. Temporal State and Current Projection

The current projection should be derived according to:

* source authority
* temporal applicability
* scope
* version
* Fact Status
* reconciliation semantics

The latest record alone is not necessarily the correct current state.

⸻

169. Temporal State and Historical Projection

Historical projections should be reconstructable at a specified time where required.

For example:

state_as_of(resource, T)

The result must preserve the temporal and authority semantics used to derive it.

⸻

170. Temporal Query Semantics

Useful conceptual queries include:

state_now(resource)
state_as_of(resource, T)
observed_at(record)
valid_during(record, interval)
changed_between(resource, T1, T2)
knowledge_as_of(subject, T)

These semantics may guide implementation.

⸻

171. Temporal State and API Design

Interfaces may expose temporal metadata explicitly.

For example:

GET /resource
{
    "version": 42,
    "observed_at": "...",
    "effective_at": "..."
}

where relevant.

Interfaces should avoid ambiguous timestamp semantics.

⸻

172. Temporal State and Event API

Event interfaces should preserve, where available:

event_id
event_time
received_at
processed_at
sequence
version
source

These fields must have defined semantics.

⸻

173. Temporal State and Integration Model

Integrations should describe temporal guarantees where known:

* real-time
* eventually consistent
* snapshot
* cached
* asynchronous
* transactional
* conditionally consistent
* read-after-write consistent

These characteristics inform State Reconciliation and Trust evaluation.

⸻

174. Temporal State and Enterprise Action Graph

The Enterprise Action Graph may represent temporal characteristics of Actions:

Action
 ├── preconditions
 ├── freshness requirements
 ├── concurrency semantics
 ├── idempotency window
 ├── authorization lifetime
 ├── outcome timing
 └── verification requirements

These are Action semantics, not generic temporal defaults.

⸻

175. Temporal State and Action Contract

An Action Contract may specify:

requires_current_state
supports_version_check
supports_idempotency
returns_async_operation
supports_conditional_write
has_execution_deadline

These capabilities affect temporal execution safety.

⸻

176. Temporal State and Integration Capability

Noema should know whether an integration supports:

* conditional writes
* transactions
* version checks
* idempotency keys
* event notifications
* read-after-write consistency
* operation status lookup
* asynchronous completion

where relevant.

⸻

177. Temporal State and Strong Guarantees

Strong enterprise guarantees can reduce temporal uncertainty.

For example:

atomic conditional update

is stronger than:

read state
→ wait
→ write state

Noema should prefer stronger guarantees where available.

⸻

178. Temporal State and Weak Guarantees

If an integration provides only eventually consistent reads, Noema should account for that uncertainty in Trust and Execution.

It must not silently treat eventually consistent data as strongly current.

⸻

179. Temporal State and Risk

The weaker the temporal guarantee, the more important:

* revalidation
* conditional execution
* reconciliation
* human approval

may become.

The exact response is policy-driven.

⸻

180. Temporal State and High-Risk Actions

For high-risk Actions, Noema should prefer:

fresh authoritative Evidence
+
strong concurrency guarantees
+
explicit temporal constraints
+
verification

where the enterprise integration supports them.

⸻

181. Temporal State and Low-Risk Actions

Low-risk Actions may tolerate:

* cached
* slightly stale
* secondary-source

Evidence when policy permits.

Low-risk does not mean ungoverned.

⸻

182. Temporal State and Policy

The Trust Engine should never invent freshness requirements.

They should originate from:

* enterprise policy
* Action Contract
* risk policy
* integration guarantees
* explicit workflow semantics

⸻

183. Temporal State and Risk-Adjusted Freshness

Conceptually:

Risk
 ↓
Freshness Requirement
 ↓
Temporal Validation
 ↓
State Reconciliation
 ↓
Trust Decision

⸻

184. Temporal State and Evidence Quality

Evidence quality includes:

* authority
* provenance
* freshness
* scope
* integrity
* temporal validity
* Fact Status

Evidence quality is not equivalent to model confidence.

⸻

185. Temporal State and Evidence Conflict

If two observations disagree, Noema should consider:

* source authority
* observation time
* valid time
* version
* scope
* reconciliation semantics

before resolving the conflict.

⸻

186. Temporal State and Temporal Authority

A later observation from a lower-authority source does not necessarily supersede an earlier observation from the authoritative source.

Recency and authority are separate dimensions.

⸻

187. Temporal State and Historical Authority

The authoritative source may itself change over time.

For example:

System A authoritative until Jan 1
System B authoritative after Jan 1

The authority model itself can therefore be temporal.

⸻

188. Temporal State and Source Migration

When systems migrate:

System A
   ↓
System B

Noema must preserve the source identity relevant to historical observations and the authority model applicable to each period.

⸻

189. Temporal State and Semantic Drift

Meaning can change over time.

A field:

status = ACTIVE

may have different semantics after a schema or domain change.

Version metadata helps preserve interpretation.

⸻

190. Temporal State and Schema Evolution

Historical records should retain enough version information to interpret them correctly.

Transport/schema compatibility must not be confused with semantic compatibility.

⸻

191. Temporal State and Policy Evolution

Policies evolve.

Historical Trust Decisions should remain tied to the policy version that governed them.

⸻

192. Temporal State and Contract Evolution

Action Contracts evolve.

Historical executions should remain tied to the contract used at execution time.

⸻

193. Temporal State and Model Evolution

Models evolve.

Where model output materially affected execution, historical records should remain tied to:

model version
inference time
relevant input/reference

The model output remains non-authoritative unless admitted through Noema’s deterministic validation and governance boundaries.

⸻

194. Temporal State and Noema Evolution

Noema’s own semantic schemas evolve.

Historical records should preserve sufficient version metadata to remain interpretable.

A newer Noema implementation must not silently change the meaning of historical records.

⸻

195. Temporal State and Backward Compatibility

Temporal records should not depend on mutable semantics that make historical data impossible to interpret after upgrades.

Historical meaning must remain pinned to the relevant semantic versions.

⸻

196. Temporal State and Canonical Semantics

Canonical state definitions should remain version-aware when their meaning changes materially.

Canonicality must remain scoped to a defined claim, field, domain, authority, and temporal context.

⸻

197. Temporal State and Temporal Ontology

Ontology concepts can themselves have temporal validity.

For example:

* Capability
* Policy
* Relationship
* State
* Resource
* Constraint

may be introduced, changed, superseded, or deprecated over time.

⸻

198. Temporal State and Relationships

Relationships can change:

User → belongs_to → Organization A

then:

User → belongs_to → Organization B

Temporal state determines which relationship applied at a given time.

⸻

199. Temporal State and Permissions Graph

Permissions may also change:

User
 ↓
Role
 ↓
Permission

The relationship must be evaluated relative to the relevant time and authorization scope.

⸻

200. Temporal State and Entity Relationships

Similarly:

Customer
 ↓ owns
Account

may change over time.

Historical execution must preserve the relationship relevant at execution time.

⸻

201. Temporal State and Resource Ownership

Ownership changes should be temporally represented when ownership affects authorization, access, or Action semantics.

⸻

202. Temporal State and Organizational Context

Enterprise context is dynamic.

Examples:

* organization
* department
* role
* manager
* cost center

may change over time.

Only context relevant to execution needs to be persisted, but when it is material, its temporal validity matters.

⸻

203. Temporal State and User Context

User Intent is interpreted within the context available at that time.

Later context should not silently rewrite historical interpretation.

⸻

204. Temporal State and Intent History

A complete Intent history may contain:

original input
clarifications
resolved interpretation
Intent versions
Trust evaluation
execution
verification
outcome

each with temporal metadata.

⸻

205. Temporal State and Clarification History

Clarification may create a new Intent version.

Example:

10:00
"refund my last payment"
10:01
"the $500 payment"
10:02
resolved to payment/123

The temporal sequence matters for reconstruction.

⸻

206. Temporal State and User Corrections

If the user corrects themselves:

“No, not that payment. The other one.”

the new statement should become a new semantic Intent event/version rather than rewriting the previous interpretation.

⸻

207. Temporal State and Human Intent Evolution

Intent can evolve during an interaction.

Noema should preserve the transition:

candidate intent
   ↓
clarification
   ↓
revised intent

A material revision must not silently mutate the prior Intent version.

⸻

208. Temporal State and Trust Re-evaluation

When Intent changes materially, Trust should be evaluated again against the new Intent version.

⸻

209. Temporal State and Execution Replanning

If relevant state changes before execution:

plan created
   ↓
state changed

Noema may need to replan.

The prior plan remains historical.

⸻

210. Temporal State and Dynamic Planning

Planning should distinguish:

static plan components

from:

state-dependent assumptions

Only the latter necessarily require current-state revalidation.

⸻

211. Temporal State and Plan Invalidation

A plan may become invalid when:

* resource deleted
* policy changed
* authorization revoked
* Evidence expires
* Action Contract changes
* required capability changes
* relevant state changes

The resulting state should be explicit, for example:

PLAN_INVALIDATED

⸻

212. Temporal State and Execution Safety

Temporal State acts as one mechanism preventing stale decisions from becoming unsafe executions.

A decision that was valid at T1 is not automatically valid at T2.

⸻

213. Temporal State and Deterministic Execution

The principle is:

A decision is deterministic only relative to the state and Evidence against which it was evaluated.

If the relevant state changes, Noema must determine whether that invalidates or conditions the decision.

⸻

214. Temporal State and Trust Recalculation

Noema should not continuously recompute Trust merely because time passes.

Policies should define when temporal changes require reevaluation.

⸻

215. Temporal State and State Change Triggers

Possible triggers include:

* Evidence expiration
* Policy change
* Authorization change
* Resource version change
* External event
* Execution delay
* Risk threshold
* Explicit deadline
* Integration state change

⸻

216. Temporal State and Event-Driven Revalidation

External events may invalidate an existing execution decision.

Example:

Trust:
EXECUTE
Event:
account.suspended
Result:
execution authorization invalidated

The historical Trust Decision remains unchanged.

⸻

217. Temporal State and Reactive Trust

This enables Trust to respond to known state changes without turning the Trust Engine into a probabilistic continuous monitor.

Revalidation remains deterministic.

⸻

218. Temporal State and Deterministic Invalidation

If a policy states:

account suspension invalidates transfers

then:

account.suspended

deterministically invalidates the relevant execution authority or requires the defined revalidation path.

⸻

219. Temporal State and Execution Locks

Some enterprise systems provide temporary locks or reservations.

These may be modeled as temporal state:

reservation
valid_from
valid_until

Noema should respect the semantics provided by the enterprise system.

⸻

220. Temporal State and Reservations

A reservation may prevent conflicting Actions during a defined interval.

Noema should not infer reservation semantics that the enterprise system does not provide.

⸻

221. Temporal State and Leases

Leases are explicitly temporal:

lease_acquired
expires_at

Noema must not assume a lease remains valid beyond its expiration.

⸻

222. Temporal State and Distributed Locks

Distributed locks have temporal validity and failure semantics.

Noema should treat them as integration-specific guarantees, not generic truth.

⸻

223. Temporal State and Execution Windows

An Execution may have:

started_at
deadline
expires_at

These boundaries should be enforced according to policy and Action Contract.

⸻

224. Temporal State and SLA

Execution SLAs can also be temporal constraints:

Action should complete within 30 seconds.

This affects monitoring and Outcome classification but does not necessarily mean the external Action failed when the deadline is exceeded.

⸻

225. Temporal State and Timeout

Timeout means:

Noema stopped waiting.

It does not necessarily mean:

The external operation stopped.

This distinction is critical.

⸻

226. Temporal State and Async Outcomes

An asynchronous operation may complete after Noema’s timeout.

Temporal State allows the later Outcome to reconcile the earlier unknown state.

⸻

227. Temporal State and Retry

Retries must consider temporal execution history.

Before retry:

Did the previous attempt possibly succeed?

If yes:

reconcile

before issuing a potentially duplicate Action.

⸻

228. Temporal State and Idempotency Windows

An external system may define:

idempotency_key valid for 24 hours

Noema must respect the temporal scope of that guarantee.

After the guarantee expires, the same key may no longer provide the same protection.

⸻

229. Temporal State and Compensation Windows

Some compensation operations may only be possible within a defined time period.

This should be modeled explicitly in the Action Contract or enterprise workflow.

⸻

230. Temporal State and Recovery Windows

Recovery workflows may also have deadlines.

Example:

cancel operation within 5 minutes

If the deadline expires, the recovery path may require reconciliation or escalation.

⸻

231. Temporal State and Failure Classification

A failure may be:

* immediate
* delayed
* unknown
* expired
* reconciled

Temporal history helps classify it correctly.

⸻

232. Temporal State and Retry Policy

Retry eligibility may depend on:

* elapsed time
* attempt count
* external operation state
* idempotency window
* Action Contract
* reconciliation status

⸻

233. Temporal State and Backoff

Retry timing is itself part of execution history:

attempt 1 → 10:00
attempt 2 → 10:01
attempt 3 → 10:03

This history is relevant to recovery and audit.

⸻

234. Temporal State and Audit

A complete retry history should remain reconstructable.

It should distinguish:

attempt
submission
response
timeout
unknown
reconciliation
retry

where applicable.

⸻

235. Temporal State and Human Intervention Timing

Human intervention can alter execution timing:

Action blocked
   ↓
human review
   ↓
approved
   ↓
execution

Approval freshness may need evaluation.

⸻

236. Temporal State and Approval Expiration

A stale human approval should not automatically remain valid.

Approval validity is a temporal control requirement defined by policy.

⸻

237. Temporal State and Escalation

Escalation itself has temporal semantics:

escalated_at
response_deadline
resolved_at

These timestamps support operational state and audit.

⸻

238. Temporal State and SLA Escalation

If a human does not respond within the required window:

approval_pending

may transition to:

expired

rather than remaining indefinitely executable.

⸻

239. Temporal State and State Machine

Temporal behavior should therefore be represented explicitly in Noema state machines.

A transition should have:

from_state
to_state
transition_at
cause
actor
evidence

where applicable.

⸻

240. Temporal State and Invalid Transitions

Temporal history should preserve invalid or rejected transitions where they matter.

Example:

Attempt:
COMPLETED → RUNNING

may be rejected.

The rejection itself can be part of the execution history.

⸻

241. Temporal State and Monotonicity

Some states should progress monotonically.

For example:

COMPLETED

should not silently become:

RUNNING

unless the domain explicitly supports such transitions.

⸻

242. Temporal State and Reversible State

Other business states may legitimately reverse:

ACTIVE
 → SUSPENDED
 → ACTIVE

Temporal State must preserve each transition.

⸻

243. Temporal State and State Semantics

State names alone are insufficient.

A state should have defined semantics regarding:

* entry
* exit
* validity
* transition rules
* temporal behavior
* authority
* allowed transitions

⸻

244. Temporal State and Outcome Semantics

An Outcome can also evolve.

Example:

PENDING
 ↓
SUCCEEDED

or:

UNKNOWN
 ↓
FAILED

Noema should preserve the temporal evolution of Outcome knowledge.

Outcome history is distinct from enterprise business state.

⸻

245. Temporal State and Knowledge State

An important distinction is:

Domain State

versus:

Noema Knowledge State

For example:

Domain:
refund = SUCCEEDED
Noema:
UNKNOWN

until the authoritative observation arrives.

⸻

246. Knowledge State

Noema’s knowledge can move:

UNKNOWN
 ↓
OBSERVED
 ↓
VERIFIED

while enterprise state may independently move:

PENDING
 ↓
SUCCEEDED

These are different state machines.

⸻

247. Temporal Knowledge

Noema must preserve:

When did Noema become aware of this fact?

This is different from:

When did the fact become true?

The difference is fundamental in asynchronous and distributed systems.

⸻

248. Temporal State and Epistemic Boundaries

This distinction is fundamental to safe automation.

What happened
≠
What Noema knew
≠
What Noema inferred

Temporal State helps maintain all three distinctions.

⸻

249. Temporal State and Inference

A model may infer:

payment/123 is probably the last payment

at 10:00.

At 10:01, a new payment arrives.

The inference may become obsolete even though it was reasonable at 10:00.

Model confidence does not establish Fact Status.

⸻

250. Temporal Inference Validity

Inference should therefore be evaluated relative to the temporal state in which it was produced.

Where the inference affects consequential execution, it must pass through Noema’s deterministic resolution, validation, Trust, and capability boundaries.

⸻

251. Temporal State and Clarification During Resolution

If relevant state changes while Intent is being resolved:

Candidate A at 10:00
Candidate B created at 10:01

Noema may need to re-resolve rather than blindly execute the original candidate.

⸻

252. Temporal State and Execution Windows

An Intent may have a defined execution window:

valid_from
valid_until

This can prevent stale Intent from being executed indefinitely.

⸻

253. Temporal State and User Intent

User Intent itself may become stale.

Example:

“Transfer $5,000 from account A to B.”

If submitted yesterday, Noema should not assume the user still intends execution today unless the workflow semantics explicitly permit deferred execution.

⸻

254. Temporal Intent Validity

The Intent lifecycle should therefore define when an Intent remains executable and when it requires re-confirmation, revalidation, or expiration.

⸻

255. Temporal State and Expired Intent

An expired Intent should transition to an explicit state:

EXPIRED

rather than remaining ambiguously executable.

⸻

256. Temporal State and Long-Lived Authorization

A user may authorize an automation once for repeated Actions.

The authorization may have:

scope
effective_from
expires_at

Temporal State enables enforcement.

⸻

257. Temporal State and Recurring Execution

Recurring Intent creates repeated temporal executions.

Each execution should have its own:

* Context
* State Reconciliation
* Evidence
* Trust evaluation
* Decision
* Action
* Verification
* Outcome

A previous execution does not permanently authorize a future execution.

⸻

258. Temporal State and Repeated Actions

A successful execution yesterday does not necessarily authorize today’s execution.

Current state and current policy may differ.

⸻

259. Temporal State and Scheduling

Scheduled execution introduces a gap:

Intent created
        ↓
scheduled time
        ↓
execution

Relevant assumptions may need revalidation at execution time.

⸻

260. Temporal State and Deferred Execution

The longer the delay, the more likely dynamic Evidence becomes stale.

Risk and policy should determine the required revalidation.

⸻

261. Temporal State and Policy TTL

Trust decisions may use explicit TTLs:

valid_for = 5 minutes

After expiry:

REVALIDATION_REQUIRED

This is an execution-control condition, not a new Trust outcome.

⸻

262. Temporal State and Action TTL

Some external Actions may also have deadlines.

Example:

payment authorization expires in 15 minutes

Noema should preserve and enforce these temporal constraints where exposed by the integration.

⸻

263. Temporal State and External Deadlines

External deadlines should be represented as constraints rather than merely comments.

They should be machine-evaluable where they affect execution.

⸻

264. Temporal State and Temporal Constraints

A Temporal Constraint can conceptually express:

before
after
within
until
since
during

These can apply to:

* Intent
* Evidence
* Policy
* Authorization
* Action
* Outcome

⸻

265. Temporal Constraint Example

Approval must occur within 30 minutes before execution.

Conceptually:

0 <= execution_at - approval_at <= 30 minutes

⸻

266. Temporal Constraint Example

Balance observation must be less than 60 seconds old.

Conceptually:

execution_at - balance.observed_at <= 60 seconds

⸻

267. Temporal Constraint Example

Refund must occur before subscription cancellation.

This creates a temporal dependency:

refund_at < cancellation_at

⸻

268. Temporal State and Action Ordering

Temporal dependencies should be explicit in a plan.

Refund
   ↓
Cancel Subscription

rather than relying on incidental execution order.

⸻

269. Temporal State and Causal Dependencies

Where Action B requires the Outcome of Action A:

A completed
   ↓
B allowed

The temporal dependency becomes an execution precondition.

⸻

270. Temporal State and Parallel Actions

Independent Actions may execute concurrently.

Their temporal ordering may be undefined.

Noema should not fabricate an ordering where none exists.

⸻

271. Temporal State and Concurrency Semantics

A compound Intent may therefore specify:

* sequential
* parallel
* ordered
* unordered
* conditional

execution semantics.

⸻

272. Temporal State and Race Conditions

When two Actions modify related resources concurrently, the enterprise integration must provide appropriate concurrency semantics.

Noema should not rely solely on timestamps to prevent races.

⸻

273. Temporal State and Version Checks

Resource versions can provide stronger guarantees:

version = 17

Action executes only if:

version still = 17

Otherwise:

REVALIDATE

or another Action Contract-defined failure path.

⸻

274. Temporal State and Enterprise Atomicity

When possible, Noema should delegate atomic state guarantees to the System of Record.

Noema’s temporal model provides context and reasoning; it does not replace enterprise transaction semantics.

⸻

275. Temporal State and Source-of-Truth Boundaries

A historical snapshot in Noema is not a replacement for the enterprise System of Record.

It is a record of:

what Noema observed
at a particular time
from a particular source
under a particular authority context

⸻

276. Temporal State and Data Ownership

Therefore:

Enterprise:
owns enterprise business state
Noema:
owns Noema execution state,
decision history,
operational history,
and relevant temporal observations/references

Noema must not create shadow canonical business state merely because it stores observed values.

⸻

277. Temporal State and Audit Ownership

Noema should own enough temporal execution history to explain:

* what happened in Noema
* what Noema knew
* what Noema decided
* what Noema attempted
* what Noema verified

while preserving references to:

* what happened in enterprise systems

⸻

278. Temporal State and Audit Completeness

An audit record should be temporally ordered enough to reconstruct the Execution journey.

It should preserve causal relationships rather than depending only on timestamp sorting.

⸻

279. Temporal State and Explainability

Explanations should use the temporal context relevant to the decision.

Avoid:

“The account had $20,000.”

Prefer:

“At the time the transfer was authorized, the account was observed with a balance of $20,000.”

The latter is temporally precise.

⸻

280. Temporal State and Trust Explanation

A Trust explanation should identify the relevant:

* Intent version
* Action
* target
* Evidence
* Fact Status
* authority
* policy version
* temporal validity

without exposing private model chain-of-thought.

⸻

281. Temporal State and Outcome Explanation

Outcome explanations should distinguish:

Action dispatched

from:

Action acknowledged

from:

Outcome verified

These are temporally distinct states.

⸻

282. Temporal State and Failure Explanation

A failure explanation should identify:

* what failed
* when it failed
* what Evidence establishes the failure
* whether the external operation may have occurred
* whether reconciliation is required

A timeout alone is not sufficient to classify an external Action as failed.

⸻

283. Temporal State and Recovery

Recovery requires reconstruction of:

last known Noema execution state
+
external operation identity
+
current enterprise state
+
unknowns

before continuation.

The recovery path may require:

* reconciliation
* revalidation
* clarification
* escalation
* rejection
* compensation

according to deterministic rules.

⸻

284. Temporal State and Operational Memory

Temporal execution history may become Operational Memory.

Operational Memory contains structured information about:

* prior executions
* failures
* recovery
* interventions
* reconciliations
* outcomes
* recurring operational patterns

It is not:

* generic AI memory
* enterprise business-state authority
* unrestricted model context

⸻

285. Temporal State and Reprocessing

When historical data is reprocessed, the resulting interpretation should be identified as a new computation.

It should not overwrite the historical interpretation used during the original Execution.

⸻

286. Temporal State and Model Reprocessing

Likewise, a newer model may resolve historical Intent differently.

That does not change what the original model resolved at execution time.

The new interpretation is a new evaluation.

⸻

287. Temporal State and Model Version

Where model output materially affects execution, provenance should identify:

model version
inference time
relevant input/reference

Model confidence remains interpretation metadata rather than Fact Status.

⸻

288. Temporal State and Historical Model Behavior

A historical execution should remain associated with the model version that produced the relevant inference where that inference materially affected the execution.

⸻

289. Temporal State and Evaluation

Noema can use historical executions to evaluate:

* policy quality
* model quality
* intent resolution
* Trust decisions
* execution reliability
* reconciliation quality
* recovery quality

without changing the original records.

⸻

290. Temporal State and Learning

Historical state can provide training or evaluation data.

However, learning must not mutate historical execution truth.

Any derived dataset should remain identifiable as a derived artifact rather than becoming the original execution record.

⸻

291. Temporal State and Causal Analysis

Temporal ordering can help determine:

* what happened before failure
* what changed before the Action
* which event preceded the Outcome
* when Evidence became stale
* when authorization changed

This supports debugging and recovery.

⸻

292. Temporal State and Root Cause

A root-cause investigation may traverse:

Outcome
 ↓
Action
 ↓
Decision
 ↓
Evidence
 ↓
State at decision time
 ↓
Earlier state transition

Temporal State enables this reconstruction.

⸻

293. Temporal State and Compensation

Compensation often depends on temporal facts:

Was Step A completed before Step B failed?

The answer comes from execution history and, where necessary, reconciliation.

⸻

294. Temporal State and Partial Execution

A compound Action may partially execute:

Step A: succeeded at 10:00
Step B: failed at 10:01
Step C: not started

Temporal state identifies exactly where execution stopped.

⸻

295. Temporal State and Human Intervention

Human intervention should be timestamped.

10:05
Operator approves retry

This approval becomes part of the temporal execution history and may carry its own validity window.

⸻

296. Temporal State and Overrides

Overrides should create new temporal records rather than rewriting prior Trust Decisions.

Example:

Trust:
REJECT at 10:00
Human override:
APPROVE at 10:05

Both remain visible.

The override itself must be governed by explicit authority and policy.

⸻

297. Temporal State and Audit Trail

The audit trail should preserve state transitions:

10:00 RECEIVED
10:01 RESOLVED
10:02 TRUST DECISION = EXECUTE
10:03 EXECUTING
10:04 UNKNOWN
10:06 RECONCILED
10:07 COMPLETED

⸻

298. Temporal State and State Machines

Noema state machines should be temporally observable.

A transition should have:

from_state
to_state
transition_at
cause
actor
evidence

where applicable.

⸻

299. Temporal State and State Monotonicity

Some Noema states should progress monotonically unless an explicit transition permits otherwise.

Historical records should preserve both valid and rejected transitions where relevant.

⸻

300. Temporal State and Timestamp Semantics

Noema should avoid generic timestamp fields whose meaning is ambiguous.

For example:

timestamp

is weaker than:

observed_at
effective_at
received_at
decision_at
executed_at

Each temporal field must have a defined semantic meaning.

⸻

301. Temporal Precision

Precision should match the domain.

Financial execution may require finer temporal resolution than ordinary metadata.

Precision must be sufficient to distinguish events whose ordering affects safety.

⸻

302. Time Zones

Temporal data should use explicit time-zone semantics.

Internally, normalized UTC timestamps are generally preferable for machine reasoning, while preserving original timezone context where domain meaning depends on it.

⸻

303. Calendar Semantics

Human expressions such as:

* tomorrow
* next month
* end of day
* business day

require domain-specific calendar semantics.

Noema should not infer these arbitrarily.

⸻

304. Temporal Intent and Business Calendars

Enterprise workflows may define:

* business day
* working hours
* holiday calendar
* cutoff time

These can materially affect execution.

⸻

305. Temporal Policy and Business Calendars

A policy may say:

“Transfers submitted after 4 PM execute next business day.”

Noema must use the enterprise’s defined calendar rather than a generic assumption.

⸻

306. Temporal State and Recurrence

Recurring Intent requires explicit recurrence semantics:

* daily
* weekly
* monthly
* business-day

and a defined timezone/calendar where relevant.

⸻

307. Temporal State and Scheduling Ambiguity

If the user’s phrase:

“every Friday”

does not specify timezone and multiple organizational timezones matter, Noema may need clarification.

⸻

308. Temporal State and Timezone Boundaries

Execution scheduled for:

09:00 Africa/Lagos

is not necessarily:

09:00 UTC

Temporal semantics must be explicit.

⸻

309. Temporal State and Daylight Saving

Where applicable, timezone transitions can produce ambiguous or nonexistent local times.

The temporal model should rely on a proper timezone database rather than naive offsets.

⸻

310. Temporal State and Business Cutoffs

Cutoff times should be represented as explicit temporal constraints.

They should be evaluated using the applicable enterprise calendar and timezone.

⸻

311. Temporal State and Expiration

Expiration should be explicit:

expires_at

rather than inferred from:

updated_at

⸻

312. Temporal State and Lifecycle

Every temporal object should have a defined lifecycle where relevant:

created
active
expired
superseded
revoked
archived

Lifecycle state is distinct from temporal metadata.

⸻

313. Temporal State and Supersession

A newer version may supersede an older version without invalidating its historical relevance.

Example:

Policy v6
superseded by v7

v6 remains the policy used by historical decisions governed by v6.

⸻

314. Temporal State and Revocation

Revocation is different from supersession.

Authorization granted
   ↓
revoked

The historical authorization remains true before revocation but cannot be used after the effective revocation point.

⸻

315. Temporal State and Effective Revocation

The system should distinguish:

revoked_at

from:

effective_revocation_at

when the enterprise domain requires that distinction.

⸻

316. Temporal State and Retroactive Changes

Some enterprise systems may make retroactive corrections.

Noema should preserve both:

historical observation

and:

later correction

when necessary.

The correction must not silently rewrite the historical observation.

⸻

317. Temporal State and Audit Semantics

An audit trail should never silently rewrite history because the source later changed.

Historical knowledge and later correction are separate temporal facts.

⸻

318. Temporal State and Data Correction

Corrections should be additive where possible:

Observation 1
Correction 2

rather than destructive replacement.

⸻

319. Temporal State and Historical Context

A historical Execution should retain the relevant Context Snapshot or references sufficient to reconstruct it.

⸻

320. Temporal State and Context Mutation

Current Context should never mutate historical Context records.

A new Context Snapshot represents a new temporal view.

⸻

321. Temporal State and Snapshot Identity

Snapshots should have stable identifiers:

context_snapshot_id

This lets Decisions reference exactly which Context was used.

⸻

322. Temporal State and Evidence Identity

Evidence should similarly have stable identifiers:

evidence_id

This prevents later updates from silently changing historical decisions.

⸻

323. Temporal State and Decision Identity

Trust Decisions should be immutable historical records:

decision_id
intent_version
decision_at
result
inputs
policy_version
trust_contract_version

where applicable.

A later revalidation creates a new decision rather than mutating the old one.

⸻

324. Temporal State and Action Identity

Executions and Action attempts should have stable IDs:

execution_id
attempt_id
external_operation_id

These identities support idempotency, recovery, reconciliation, and audit.

⸻

325. Temporal State and Outcome Identity

Outcomes should also be identifiable:

outcome_id
observed_at
source

Outcome identity must distinguish Noema’s Outcome record from enterprise business state.

⸻

326. Temporal State and Lineage

These IDs create a temporal lineage:

Intent
 ↓
Context Snapshot
 ↓
Observation / Evidence
 ↓
State Reconciliation
 ↓
Trust Decision
 ↓
Execution
 ↓
Attempt
 ↓
External Operation
 ↓
Verification
 ↓
Outcome

⸻

327. Temporal State and Audit Reconstruction

The entire timeline can then be reconstructed without depending on mutable current state.

Historical reconstruction should use the versions and observations that were actually applicable at the relevant time.

⸻

328. Temporal State and Observability

Operational observability can use temporal state to expose:

* latency
* queue time
* execution time
* retry delay
* reconciliation delay
* human intervention time
* verification delay

⸻

329. Temporal State and Performance

Temporal metadata should support performance analysis without becoming part of business-state ownership.

⸻

330. Temporal State and Debugging

Engineers can ask:

What changed between decision and execution?

Temporal State provides the evidence required to answer the question.

⸻

331. Temporal State and Incident Analysis

After an incident:

What was true?
What did Noema know?
What did Noema infer?
What changed?
When did it change?
Which authority reported it?
Why was the Action still allowed?

These are temporal questions.

⸻

332. Temporal State and Safety

Temporal correctness is part of execution safety.

A decision can be semantically correct at T1 and unsafe at T2.

Whether it remains executable must be determined by explicit policy and current-state evaluation.

⸻

333. Temporal Safety Principle

Validity at decision time does not automatically imply validity at execution time.

Whether the decision remains executable must be determined by:

* Action semantics
* current state
* Evidence freshness
* authorization validity
* policy
* risk
* concurrency guarantees
* execution timing

⸻

334. Temporal State and Trust Revalidation Principle

When temporal validity is material to an Action, Noema must explicitly determine whether the relevant Evidence remains valid before execution.

Where required, Noema must obtain current authoritative state through State Reconciliation rather than treating historical observations as current truth.

⸻

335. Temporal State and Historical Truth Principle

Noema must preserve what it knew at the time without rewriting history based on later information.

A later correction creates new knowledge about the past; it does not erase the historical observation.

⸻

336. Temporal State and Current Truth Principle

Current enterprise state must be obtained from the authoritative System of Record or approved authoritative source when current state is required.

Noema’s persisted observations do not become current enterprise truth merely because they are newer than another Noema record.

⸻

337. Temporal State and Uncertainty Principle

When temporal ordering, freshness, authority, or validity cannot be established and materially affects execution, uncertainty must become an explicit system condition.

Noema must not resolve material temporal uncertainty through model confidence, recency alone, or inference.

⸻

338. Temporal State and Hard Admission

External payloads, events, tool responses, and model-generated information are untrusted until they pass the applicable validation and admission boundary.

Persistence does not make unvalidated information authoritative.

Unvalidated information may be retained as explicitly classified diagnostic or raw evidence where necessary, but it must not silently become authoritative input to Trust or Execution.

⸻

339. Temporal State and Fact Status

Temporal State must preserve Fact Status where relevant:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

* Evidence
* Context
* State
* Outcome
* Canonical Data
* model confidence

A model’s confidence score must never be used as a substitute for Fact Status.

⸻

340. Temporal State and Canonicality Scope

Canonicality is scoped.

A value may be canonical for:

* a specific field
* a specific claim
* a specific resource
* a specific enterprise domain
* a specific time interval
* a specific authority

without being universally canonical.

Therefore:

canonical ≠ universally current
canonical ≠ universally accessible
canonical ≠ universally authoritative

⸻

341. Temporal State and Source / Authority Separation

Noema must distinguish:

source
authority
freshness
availability
authorization

A source may provide information without being authoritative for the claim.

A recent observation may be available without being authorized for the intended use.

A historical source may be authoritative for historical reconstruction without being suitable for current execution.

⸻

342. Temporal State and Planner Boundaries

A persisted plan remains bounded by:

* Enterprise Action Graph
* Capability Registry
* Action Contract Registry
* Trust Decision
* resolved Intent
* applicable policy
* current execution conditions

Persistence of a plan does not grant authority.

The Planner cannot invent capabilities, create authority, modify Action Contract semantics, or bypass Trust because a plan has been persisted.

⸻

343. Temporal State and Model Output

Model output may be persisted for:

* debugging
* evaluation
* provenance
* reconstruction
* operational analysis

Persistence does not confer authority.

Model output remains untrusted interpretation or proposal data unless it passes the applicable deterministic validation and admission boundaries.

The model has no direct enterprise credentials or direct authority to mutate enterprise state.

⸻

344. Temporal State and Read-Only Operations

Read-only does not mean temporally or operationally insignificant.

A read-only operation may expose protected enterprise data or perform deep cross-system investigation.

Such operations may therefore require:

* Trust
* authorization
* temporal validation
* current-state reconciliation

according to policy.

⸻

345. Temporal State and Outcome Semantics

Noema must distinguish:

Trust Decision
EXECUTE

from:

Execution
submitted

from:

Outcome
verified

A persisted EXECUTE decision is a historical governance decision.

It is not proof of enterprise success.

⸻

346. Temporal State and Outcome vs Business State

Outcome is distinct from enterprise business state.

For example:

Noema Outcome:
REFUND_VERIFIED
Enterprise State:
payment.status = REFUNDED

Noema may reference the enterprise state that established the Outcome without becoming its owner.

⸻

347. Temporal State and No Shadow Business State

Noema must not create shadow canonical business state merely by storing enterprise observations.

Persisted business-state observations remain:

observations
+
provenance
+
temporal metadata
+
Fact Status

unless they belong to an explicitly Noema-owned execution-domain concept.

⸻

348. Temporal State and Noema-Owned Canonical State

Noema may own canonical state within its own execution domain, including:

* Intent versions
* Trust Decisions
* Execution state
* Execution attempts
* Noema Outcomes
* recovery state
* intervention/case state
* audit records
* reconciliation records

This is distinct from ownership of enterprise business state.

⸻

349. Temporal State and Historical Immutability

Historical observations that materially influenced decisions should not be silently rewritten.

Corrections should produce new observations.

Historical Intent versions, Trust Decisions, and execution records should remain immutable in semantic meaning.

⸻

350. Temporal State and Versioned Semantics

Temporal reconstruction may require preserving:

Intent version
Context version/snapshot
Evidence version
Trust Contract version
Trust Decision version
Action Contract version
Execution Contract version
Event version
Policy version
integration mapping version
EAG/capability version
model version

The relevant versions should be pinned to the historical record.

⸻

351. Temporal State and Reprocessing

Reprocessing historical data must create a distinguishable new computation.

It must not mutate:

* historical Intent interpretation
* historical Trust Decision
* historical Execution
* historical Outcome
* historical temporal observations

unless an explicit correction workflow defines otherwise.

⸻

352. Temporal State and Causal Audit

A causal audit should be able to traverse:

Claim
 ↓
Source / Authority
 ↓
Observation
 ↓
Validation / Admission
 ↓
State Reconciliation
 ↓
Fact Status
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

This provides causal traceability without requiring storage of private model chain-of-thought.

⸻

353. Temporal State and Historical Corrections

A correction should preserve both:

Historical Observation:
what Noema observed at T1
Later Correction:
what is now known about that historical state

This distinction is essential for audit integrity.

⸻

354. Temporal State and Reconciliation Identity

Each material reconciliation should have stable identity.

Conceptually:

reconciliation_id
subject
observations_considered
performed_at
result
fact_status
authority

This allows later decisions to reference the exact reconciliation result used.

⸻

355. Temporal State and Current-State Revalidation

Recovery and deferred execution should generally follow:

Historical Execution State
        ↓
Identify Unknowns
        ↓
Current Enterprise Observation
        ↓
State Reconciliation
        ↓
Fact Status
        ↓
Trust / Action Revalidation
        ↓
Continue / Clarify / Escalate / Reject

The recovery process must not simply resume from stale local state.

⸻

356. Temporal State and Persistence Failure

If required temporal or execution state cannot be durably recorded, high-consequence execution should normally block or escalate rather than proceed without accountability.

If persistence fails after external dispatch, the resulting uncertainty must be reconciled against the enterprise system.

⸻

357. Temporal State and Exactly-Once Semantics

Noema should not claim message-level exactly-once delivery where the underlying systems do not provide it.

The goal is:

exactly-once logical effect

where supported through:

* durable execution identity
* idempotency
* conditional execution
* reconciliation
* enterprise transaction guarantees

Temporal history is one of the mechanisms required to establish whether a logical effect already occurred.

⸻

358. Temporal State and Operational Memory

Operational Memory may retain structured temporal execution history for future operational use.

It must not become:

* a generic model memory
* an alternative System of Record
* an ungoverned source of authority

Historical operational patterns may inform future reasoning only through the applicable deterministic boundaries.

⸻

359. Conceptual Temporal Model

The canonical conceptual model is:

Enterprise System of Record
            │
            │ observations
            ▼
      Temporal Observation
            │
            ▼
      Validation / Admission
            │
            ▼
      State Reconciliation
            │
            ▼
       Fact Status
            │
            ▼
         Evidence
            │
            ▼
     Deterministic Trust
            │
            ▼
      Action / Execution
            │
            ▼
        Verification
            │
            ▼
         Outcome
            │
            ▼
 Operational Memory / Audit

The enterprise remains authoritative for enterprise business state.

Noema remains authoritative for its own execution-domain records and decisions.

⸻

360. Conceptual Temporal Record

A temporal record can be modeled conceptually as:

TemporalRecord {
    record_id
    subject
    claim
    value
    valid_from
    valid_until
    event_time
    effective_at
    observed_at
    received_at
    recorded_at
    source
    authority
    scope
    version
    fact_status
    provenance
    reconciliation_id
}

Not every record requires every field.

The exact schema is implementation-dependent.

⸻

361. Temporal State and Data Boundaries

Temporal records must respect:

* tenant boundaries
* organizational boundaries
* authorization boundaries
* data classification
* privacy requirements
* residency requirements
* retention requirements

Temporal history is not exempt from access control because it is historical.

⸻

362. Temporal State and Sensitive Data

Temporal metadata can itself be sensitive.

A timestamp indicating:

* money movement
* account access
* employee role change
* customer activity

may reveal sensitive behavioral information.

Noema should minimize and protect temporal data according to its classification.

⸻

363. Temporal State and Security

Historical temporal data must not bypass security controls.

A user authorized to access current state is not automatically authorized to access all historical state.

Access must be evaluated against the relevant resource, organization, tenant, temporal record, and policy.

⸻

364. Temporal State and Audit Integrity

Audit integrity requires that historical records remain attributable and tamper-evident where necessary.

The system should preserve:

* who or what produced the record
* when it was produced
* which source supplied it
* which version applied
* what temporal meaning the record has

⸻

365. Temporal State and Availability

Temporal history should remain available for recovery and audit according to its required durability class.

Not all temporal information requires the same durability.

Conceptually:

critical execution history
    → durable
operational cache
    → ephemeral
diagnostic telemetry
    → retention-dependent

⸻

366. Temporal State and Failure Modes

Important temporal failure modes include:

* clock skew
* stale Evidence
* missing observations
* delayed events
* out-of-order events
* duplicate events
* conflicting observations
* expired authorization
* expired Intent
* expired idempotency window
* unknown execution
* persistence failure
* lost correlation
* unavailable System of Record
* semantic version mismatch

These must remain explicit rather than being collapsed into generic failure.

⸻

367. Temporal State and Recovery State Machine

A temporal recovery path may conceptually be:

UNKNOWN
   ↓
RECONCILING
   ↓
VERIFIED

or:

UNKNOWN
   ↓
RECONCILING
   ↓
FAILED

or:

UNKNOWN
   ↓
RECONCILING
   ↓
ESCALATED

The transition depends on authoritative Evidence and deterministic policy.

⸻

368. Temporal State and Revalidation State

A stale decision may enter:

REVALIDATION_REQUIRED

This does not mean the historical decision was wrong.

It means the historical decision is insufficient to establish current execution authority.

⸻

369. Temporal State and Historical Immutability of Decisions

A historical Trust Decision:

decision_id = D1
result = EXECUTE
decision_at = T1

remains:

D1 = EXECUTE at T1

even if a later revalidation produces:

D2 = REJECT at T2

The two decisions represent different temporal evaluations.

⸻

370. Temporal State and Historical Immutability of Intent

An admitted Intent version remains semantically immutable.

If the user clarifies:

Intent v1
    ↓
supersedes
Intent v2

the original Intent remains part of history.

The new version becomes the basis for subsequent evaluation.

⸻

371. Temporal State and Historical Immutability of Evidence

Historical Evidence references should identify the exact observation used.

Later observations may supersede current applicability but must not silently mutate the historical Evidence record.

⸻

372. Temporal State and Temporal Authority

Authority itself may have temporal scope.

For example:

System A authoritative:
Jan 1 → Jun 30
System B authoritative:
Jul 1 → onward

Historical resolution must use the authority model applicable to the relevant period.

⸻

373. Temporal State and Temporal Scope

Every consequential temporal assertion should be understood within a scope that may include:

tenant
organization
environment
resource
claim
source
authority
time interval

Temporal validity without scope can be misleading.

⸻

374. Temporal State and Current Evaluation

Current evaluation should use current authoritative information when current state is required.

It should not simply load the most recently persisted Noema observation.

Conceptually:

Current Evaluation
       ↓
Current Enterprise Observation
       ↓
State Reconciliation
       ↓
Current Fact Status
       ↓
Trust Evaluation

⸻

375. Temporal State and Historical Evaluation

Historical evaluation should use the historical inputs and semantic versions that governed the original decision.

Conceptually:

Historical Decision
       ↓
Historical Intent Version
       ↓
Historical Context
       ↓
Historical Evidence
       ↓
Historical Policy
       ↓
Historical Contract
       ↓
Historical Evaluation

⸻

376. Temporal State and Modern Evaluation

Modern evaluation of historical data is a separate analytical operation.

It may use:

* current policies
* current models
* current ontology
* current contract semantics

but must be clearly marked as a new evaluation.

⸻

377. Temporal State and Safety Boundary

Temporal State is part of the deterministic boundary between:

probabilistic interpretation

and:

consequential execution

Temporal information supplied by models or external sources is not trusted merely because it contains timestamps.

It must be validated, scoped, and evaluated according to deterministic rules.

⸻

378. Temporal State and Canonical Execution Chain

The canonical temporal execution chain is:

Source of Intent
      ↓
Validated / Admitted Intent
      ↓
Context + Observations
      ↓
State Reconciliation
      ↓
Fact Status / Evidence
      ↓
Deterministic Trust
      ↓
Action / Execution
      ↓
Verification
      ↓
Outcome
      ↓
Operational Memory / Audit

Temporal metadata applies across every stage.

⸻

379. Temporal State and Temporal Knowledge Chain

Noema must preserve three distinct temporal perspectives:

Domain Time
    ↓
When something was true or occurred
Observation Time
    ↓
When Noema observed it
Knowledge Time
    ↓
When Noema became able to use it as known information

These may differ materially.

⸻

380. Temporal State and Execution Safety Boundary

Before consequential execution, Noema must be able to determine, where relevant:

Is the Intent still valid?
Is the target still the same?
Is the actor still authorized?
Is the Evidence fresh enough?
Is the state reconciled?
Is the policy still applicable?
Is the Action Contract still applicable?
Are concurrency conditions satisfied?
Is the Trust Decision still valid?

If not, the appropriate deterministic path is revalidation, clarification, escalation, or rejection according to policy.

⸻

381. Core Invariants

Invariant 1

Historical state must remain distinguishable from current state.

Invariant 2

Observation time must remain distinguishable from receipt time.

Invariant 3

Event time must remain distinguishable from processing time.

Invariant 4

Effective time must remain distinguishable from recording time.

Invariant 5

Decision time must remain distinguishable from execution time.

Invariant 6

Outcome occurrence time must remain distinguishable from outcome observation time.

Invariant 7

Historical Decisions must retain the temporal context under which they were made.

Invariant 8

Historical Evidence must not be silently replaced by newer Evidence.

Invariant 9

New Evidence must create a new temporal observation when it represents a new observation.

Invariant 10

Current state must be obtained from the appropriate authoritative System of Record when current state is required.

Invariant 11

Historical snapshots must not be treated as current truth merely because they are persisted by Noema.

Invariant 12

Evidence freshness requirements must be determined by policy, risk, Action semantics, and integration guarantees.

Invariant 13

Expired Evidence may remain historically valid while being unusable for current execution.

Invariant 14

Fact Status must remain distinct from Evidence, Context, State, Outcome, Canonical Data, and model confidence.

Invariant 15

Fact Status values must preserve explicit uncertainty and conflict where applicable.

Invariant 16

Expired authorization must not silently authorize new execution.

Invariant 17

Policy versions must remain associated with the decisions they governed.

Invariant 18

Action Contract versions must remain associated with the executions that used them.

Invariant 19

Intent versions used for consequential execution must remain identifiable and immutable in meaning.

Invariant 20

Model versions must remain associated with consequential model inferences where required for reconstruction.

Invariant 21

Temporal conflicts must not be silently resolved by recency alone.

Invariant 22

Source authority and temporal recency are separate dimensions.

Invariant 23

Source, authority, freshness, availability, and authorization must not be conflated.

Invariant 24

Unknown temporal ordering must remain explicitly unknown when it materially affects execution.

Invariant 25

Timeout must not be interpreted as external failure without supporting Evidence.

Invariant 26

Recovery must account for external Actions that may have occurred without a local completion record.

Invariant 27

Retries must consider temporal execution history and idempotency semantics.

Invariant 28

Long-running or deferred executions must revalidate temporal assumptions when required by policy.

Invariant 29

Historical Trust Decisions must not be retroactively rewritten.

Invariant 30

Revalidation is a new evaluation, not a mutation of historical Trust.

Invariant 31

Historical corrections must not erase what Noema observed at the time.

Invariant 32

Temporal state must respect tenant, organizational, security, and data boundaries.

Invariant 33

Temporal history should be retained according to explicit retention requirements.

Invariant 34

Temporal metadata should use precise semantics rather than ambiguous generic timestamps.

Invariant 35

Temporal constraints that materially affect execution must be explicit.

Invariant 36

Noema must distinguish domain state from Noema’s knowledge state.

Invariant 37

Noema must distinguish what happened from what it knew happened.

Invariant 38

Noema must distinguish inference time from the temporal validity of the inferred fact.

Invariant 39

State transitions relevant to execution, recovery, reconciliation, or audit must remain reconstructable.

Invariant 40

A change in current state must not silently alter historical execution records.

Invariant 41

Temporal validity must be evaluated relative to the Action being performed.

Invariant 42

When temporal uncertainty materially affects execution, Noema must transition to an explicit safe condition such as revalidation, clarification, escalation, or rejection.

Invariant 43

External payloads, events, tool responses, and model-generated information must not become authoritative merely because they are persisted.

Invariant 44

State Reconciliation must remain distinct from Temporal State; Temporal State supplies observations and history, while State Reconciliation determines the applicable reconciled state.

Invariant 45

A persisted observation must not become enterprise System-of-Record authority merely because Noema stores it.

Invariant 46

Trust EXECUTE must remain distinct from execution success and enterprise business-state change.

Invariant 47

Noema Outcome must remain distinct from enterprise business state.

Invariant 48

The Planner must not gain authority, capabilities, or execution rights merely because a plan is persisted.

Invariant 49

Historical replay must not dispatch consequential Actions by default.

Invariant 50

Historical replay must not silently substitute current enterprise state, current policy, current contract semantics, or current model behavior for historical inputs.

Invariant 51

Material Intent change must create a new Intent version rather than silently mutating the historical Intent.

Invariant 52

Temporal metadata must remain interpretable according to the semantic version applicable to the record.

Invariant 53

Historical observations, Decisions, and execution records must remain causally traceable through stable identifiers.

Invariant 54

When required durable temporal or execution state cannot be recorded, high-consequence execution should normally block or escalate rather than proceed without accountability.

Invariant 55

Post-dispatch persistence failure must be treated as uncertainty requiring reconciliation rather than assumed external failure.

Invariant 56

Exactly-once logical effects must not be claimed unless supported by appropriate idempotency, durable identity, conditional execution, transactional, or reconciliation guarantees.

Invariant 57

Operational Memory may preserve temporal execution history but must not become an alternative enterprise System of Record.

Invariant 58

Temporal correctness is part of execution safety.

⸻

382. Final Definition

Temporal State is Noema’s representation of state, observations, knowledge, validity, decisions, executions, and outcomes across time.

It preserves the distinction between:

* what was true
* what was observed
* what was received
* what was validated
* what was reconciled
* what Noema knew
* what Noema inferred
* what was decided
* what was executed
* what was later verified

Temporal State does not make Noema the owner of enterprise business state. Enterprise Systems of Record remain authoritative within their defined domains. Noema owns the temporal history and execution-domain state required to safely interpret, govern, execute, recover, reconcile, verify, and audit consequential Actions.

The canonical temporal chain is:

              ENTERPRISE STATE
                    │
                    │
                    ▼
              OBSERVATION
             at time T₁
                    │
                    ▼
        VALIDATION / ADMISSION
                    │
                    ▼
          STATE RECONCILIATION
                    │
                    ▼
        FACT STATUS / EVIDENCE
             known at T₂
                    │
                    ▼
       DETERMINISTIC TRUST
          decision at T₃
                    │
                    ▼
             EXECUTION
              at T₄
                    │
                    ▼
       EXTERNAL STATE CHANGE
              at T₅
                    │
                    ▼
            VERIFICATION
              at T₆
                    │
                    ▼
              OUTCOME
                    │
                    ▼
       OPERATIONAL MEMORY / AUDIT

The key principle is:

Noema must know not only what is true, but what was true when, what was observed when, what it knew when, which authority established it, whether that knowledge remains valid for the Action, and what actually happened after execution.