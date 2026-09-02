Temporal State

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/temporal-state.md

⸻

1. Definition

Temporal State is Noema’s representation of how relevant facts, context, evidence, and enterprise state change over time.

Noema must distinguish between:

* what is true now
* what was observed then
* what was believed at the time
* what changed after an Action
* what was true when a decision was made

Temporal State exists because state is not timeless.

⸻

2. Purpose

An enterprise environment is continuously changing.

User
  ↓
Intent
  ↓
Context
  ↓
Trust Decision
  ↓
Action
  ↓
Outcome

The information available at each stage may differ.

For example:

10:00
Account balance = $20,000
10:02
Trust decision = EXECUTE
10:03
Another transaction reduces balance to $5,000
10:04
Transfer executes

Noema must preserve the distinction between the balance observed at 10:00 and the balance that exists at 10:04.

⸻

3. Core Principle

Noema must never confuse historical state with current state.

A historical observation may explain a historical decision without being sufficient to authorize a new Action.

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

which account
which system
which environment
when observed

⸻

5. Temporal State vs Current State

Current state answers:

What is true now?

Temporal State answers:

What was true, or observed to be true, at a particular point in time?

Both are necessary.

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

The external System of Record remains authoritative.

⸻

7. Temporal State and Provenance

Temporal State and Provenance are closely related.

Provenance answers:

Where did this information come from?

Temporal State answers:

When did this information apply or become known?

Together:

Claim
 ├── Provenance
 └── Temporal context

⸻

8. Two Important Times

Noema should distinguish at least:

event_time

and:

observation_time

An event may have happened at 10:00 but only become known to Noema at 10:03.

⸻

9. Observation Time

observed_at represents when the source state or fact was observed.

Example:

balance = $10,000
observed_at = 10:00

This does not imply that Noema received it at 10:00.

⸻

10. Receipt Time

received_at represents when Noema received the observation.

observed_at = 10:00
received_at = 10:02

The distinction matters in distributed systems.

⸻

11. Decision Time

A Trust decision has its own temporal position.

decision_at = 10:03

The Evidence used by the decision may have been observed earlier.

⸻

12. Execution Time

An Action may execute later:

executed_at = 10:04

Therefore:

observation
    ↓
decision
    ↓
execution

are separate temporal events.

⸻

13. Outcome Time

The Outcome may occur or become observable later still.

outcome_occurred_at = 10:05

or:

outcome_observed_at = 10:06

Again, these are not necessarily the same.

⸻

14. Temporal Chain

A complete Execution may therefore have:

10:00  Observation
10:01  Intent resolution
10:02  Trust evaluation
10:03  Decision
10:04  Action
10:05  External state change
10:06  Outcome observation

Noema should preserve this sequence.

⸻

15. Temporal State Is Not Event Sourcing

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

or combinations of these.

⸻

16. State Snapshots

A snapshot represents state as observed at a particular point.

Example:

Context Snapshot #42
identity = user/123
balance = $20,000
subscription = ACTIVE
policy_version = 7
captured_at = 10:00

The snapshot is historical.

It should not automatically be interpreted as current.

⸻

17. Context Snapshots

Context used for Trust evaluation should be associated with the time at which it was assembled.

Context
    ↓
captured_at
    ↓
Evidence versions

This allows Noema to reconstruct what information influenced the decision.

⸻

18. Temporal Context

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

Noema should preserve the temporal metadata of its components.

⸻

19. Context Consistency Window

For some Actions, Evidence gathered over a long period may be undesirable.

A policy may require:

all critical Evidence
observed within 60 seconds

This creates a temporal consistency requirement.

⸻

20. Temporal Coherence

A Trust decision should evaluate whether its Evidence is temporally coherent for the Action.

For example:

Identity:
5 minutes old
Account balance:
5 seconds old
Authorization:
2 hours old

The Action may require revalidation because the Evidence was assembled across incompatible time windows.

⸻

21. Freshness

Freshness describes how old an observation is relative to the point at which it is being used.

Conceptually:

freshness = current_time - observed_at

The acceptable threshold is policy-dependent.

⸻

22. Freshness Is Not Truth

An old observation is not necessarily false.

It may simply no longer be suitable for a particular decision.

Observed:
balance = $20,000

can remain historically true while being unsuitable for a transfer authorization five minutes later.

⸻

23. Evidence Expiration

Evidence may have a maximum usable age.

Example:

balance:
max_age = 30 seconds

After that:

Evidence status = STALE

The historical observation remains intact.

⸻

24. Temporal Validity

Some information has an explicit validity interval.

Policy A:
valid_from = Jan 1
valid_until = Jun 30

Noema should determine whether the policy was applicable at the relevant decision time.

⸻

25. Effective Time

Enterprise records may have:

effective_at

representing when a state becomes applicable.

This can differ from when the record was created.

⸻

26. Effective Time vs Observation Time

Example:

Employee promotion
effective_at = Jan 1
recorded_at = Jan 3

The promotion applies from Jan 1 even though Noema only learned about it on Jan 3.

These timestamps must not be conflated.

⸻

27. Valid Time and Transaction Time

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

28. Historical Truth

Suppose:

Account status:
ACTIVE

at 10:00.

At 10:10:

Account status:
SUSPENDED

A historical execution at 10:02 should retain:

status = ACTIVE

as the state observed at that time.

⸻

29. Current Truth

At 10:10, a new Action should consult current authoritative state.

The historical ACTIVE observation should not be reused merely because it was once valid.

⸻

30. Temporal State and Decision Reconstruction

A Trust decision should be reconstructable using the state and Evidence available at the decision time.

Conceptually:

Decision D1
    ↓
Context Snapshot C1
    ↓
Evidence E1...En
    ↓
Temporal State at D1

⸻

31. Temporal State and Determinism

Deterministic Trust evaluation requires deterministic temporal inputs.

If a policy says:

balance must be ≥ $10,000

Noema must know:

Which balance, observed when?

Otherwise the same decision may produce different results depending on when the system is replayed.

⸻

32. Temporal Determinism

Historical replay should use:

historical Evidence
historical Policy
historical Context
historical Action Contract

rather than silently querying current enterprise state.

⸻

33. Temporal State and Replay

For example:

2026-08-20
Trust Decision = EXECUTE

Replay should reconstruct:

what Noema knew on 2026-08-20

not:

what the enterprise system says today

⸻

34. Temporal State and Revalidation

Revalidation is intentionally different.

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

35. Historical Decision vs Current Decision

These should remain separate:

Historical:
EXECUTE
Current revalidation:
REJECT

The latter does not rewrite the former.

⸻

36. Temporal State and Long-Running Execution

Long-running Actions are especially sensitive to temporal state.

Example:

Intent accepted
      ↓
Approval obtained
      ↓
Execution delayed 2 hours

During those two hours:

permissions may change
account state may change
policy may change
resource may change

Noema must know which conditions require revalidation.

⸻

37. Temporal Preconditions

A Precondition may include a freshness requirement:

beneficiary_verified
observed within 5 minutes

or:

account_status
must be current

⸻

38. Temporal Postconditions

Postconditions are also time-bound.

Example:

payment.status = REFUNDED

at:

10:05

does not necessarily mean the payment will remain refunded forever.

The postcondition establishes what was verified at the relevant time.

⸻

39. Temporal State and Idempotency

Idempotency is inherently temporal.

Noema may need to determine:

Has this Action already been executed?

The answer depends on historical execution state.

⸻

40. Temporal State and Duplicate Execution

Example:

10:00
refund request submitted
10:01
network timeout
10:02
retry begins

Noema must inspect temporal execution history before issuing another external Action.

⸻

41. Temporal State and Unknown Outcomes

A timeout does not establish failure.

10:00
Action submitted
10:01
No response

The external system may have executed the Action.

Temporal state enables Noema to represent:

Outcome = UNKNOWN

until new Evidence arrives.

⸻

42. Temporal State and Reconciliation

Later:

10:05
Payment System:
REFUNDED

Noema can reconcile the unknown execution.

The historical sequence remains:

submitted
→ unknown
→ verified refunded

⸻

43. Temporal State and Event Ordering

Distributed systems may deliver events out of order.

Example:

Event B received
Event A received

while:

A occurred before B

Noema should preserve source event time and identifiers where possible.

⸻

44. Event Time

For an event:

event_time

represents when the event occurred according to the source.

⸻

45. Processing Time

processed_at

represents when Noema processed the event.

These may differ significantly.

⸻

46. Late Events

A late event may describe an earlier state transition.

Example:

10:00
event occurred
10:05
event received

Noema should not automatically interpret receipt order as domain-event order.

⸻

47. Event Versioning

Events may change schema over time.

Historical events should retain:

event_type
event_version

so their original semantics remain interpretable.

⸻

48. Temporal State and Eventual Consistency

Different enterprise systems may converge at different times.

Example:

Payment System:
REFUNDED
Reporting System:
PENDING

Both observations may be temporally valid from their respective perspectives.

Noema should preserve the temporal and source dimensions rather than flattening them into one value.

⸻

49. Temporal State and Source Authority

Temporal conflict resolution must consider:

source authority
event time
observation time
scope
version

A newer observation is not automatically more authoritative.

⸻

50. Temporal State and Conflicting Evidence

Example:

10:00 Identity System:
ACTIVE
10:01 CRM:
ACTIVE
10:02 Identity System:
SUSPENDED

The Trust Engine should evaluate the appropriate authoritative source at the relevant time.

⸻

51. Temporal State and Policy Versions

Policies are temporal entities.

Policy v1
effective: Jan 1 – Jun 30
Policy v2
effective: Jul 1 onward

A decision on June 30 must use the policy applicable at that time.

⸻

52. Temporal State and Action Contract Versions

Action Contracts may also evolve.

Contract v1
endpoint = /refund
Contract v2
endpoint = /payments/{id}/refund

Historical executions must preserve the contract version used.

⸻

53. Temporal State and Configuration

Configuration may change over time:

approval_threshold:
$10,000

then:

$5,000

Historical decisions must retain the configuration applicable at decision time.

⸻

54. Temporal State and Identity

Identity assertions are temporal.

A user may:

gain a role
lose a role
change organization
lose access

Therefore authorization should consider the identity and permission state applicable at the time of execution.

⸻

55. Temporal State and Permissions

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

56. Temporal State and Authorization

Authorization therefore may be modeled as:

Principal
+
Permission
+
Resource
+
Action
+
Time

rather than merely:

Principal
+
Permission

⸻

57. Temporal State and Organizational Boundaries

Organizational membership can change.

Employee
    Organization A

may become:

Employee
    Organization B

Temporal state determines which organizational boundary applied at a given time.

⸻

58. Temporal State and Business State

Noema observes business state but does not own it.

Examples:

order = SHIPPED
invoice = PAID
subscription = ACTIVE
account = SUSPENDED

These states should retain their temporal context.

⸻

59. State Transitions

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

60. State History

Where relevant, Noema should retain enough information to reconstruct meaningful state history.

Example:

10:00 PENDING
10:02 APPROVED
10:03 EXECUTING
10:05 COMPLETED

⸻

61. Temporal State and Noema State

Noema itself has state:

Intent State
Trust State
Execution State
Recovery State

These are distinct from enterprise business state.

Noema may own its own temporal state while only observing enterprise temporal state.

⸻

62. Intent State Over Time

An Intent may move through:

RECEIVED
   ↓
RESOLVING
   ↓
RESOLVED
   ↓
TRUSTED
   ↓
EXECUTING
   ↓
COMPLETED

The transitions form temporal history.

⸻

63. Trust State Over Time

Trust may evolve:

UNKNOWN
   ↓
EVALUATING
   ↓
TRUSTED
   ↓
INVALIDATED

A previously trusted state can become invalid when relevant temporal conditions change.

⸻

64. Execution State Over Time

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

65. Temporal State and Trust Invalidation

A Trust decision can become stale.

Example:

10:00
Trust = EXECUTE
10:10
authorization revoked

The original Trust decision remains historically valid.

But it may no longer authorize a new execution attempt.

⸻

66. Temporal Trust Validity

A Trust decision may therefore have:

issued_at
valid_until
invalidated_at

where applicable.

⸻

67. Temporal Trust Is Policy-Driven

Not every Trust decision needs an expiration.

The required temporal validity depends on:

risk
Action
Evidence
policy
execution duration

⸻

68. Temporal State and Risk

Risk can increase as Evidence ages.

For example:

balance observed:
10 seconds ago → low concern
balance observed:
1 hour ago → potentially unacceptable

Therefore temporal freshness can directly affect Trust.

⸻

69. Temporal Risk Windows

Policies may define:

high-risk transfer:
balance must be < 30 seconds old
low-risk read:
balance may be < 10 minutes old

⸻

70. Temporal State and Clarification

Temporal ambiguity can also require clarification.

Example:

“Use the balance from earlier.”

Earlier could mean:

10 minutes ago
today
last statement
previous transaction

Noema should not infer temporal meaning when it materially affects execution.

⸻

71. Temporal State and Intent Resolution

Temporal expressions such as:

last
previous
yesterday
recent
earlier
this month

must be resolved against explicit temporal context.

⸻

72. Temporal Intent

An Intent may include temporal constraints:

refund my last payment

becomes conceptually:

Action:
refund
Resource:
most recent eligible payment
Temporal criterion:
latest by defined ordering

The temporal criterion must be explicit enough for deterministic resolution.

⸻

73. Temporal Ordering

“Last payment” should not necessarily mean:

latest created_at

It could mean:

latest successful payment

depending on domain semantics.

Noema should rely on the relevant enterprise semantics rather than inventing an ordering.

⸻

74. Temporal State and Entity Resolution

Temporal state can affect entity identity.

For example:

customer/123

may have been active in 2025 but inactive in 2026.

The relevant identity depends on the Action’s temporal context.

⸻

75. Temporal State and Resource Lifecycle

Resources may have lifecycles:

CREATED
ACTIVE
SUSPENDED
DELETED

Noema should know whether a resource existed or was valid at the relevant point in time.

⸻

76. Temporal State and Deleted Resources

A resource deleted today may still be relevant to a historical Execution.

Deletion should not erase historical references required for audit.

⸻

77. Temporal State and Referential Integrity

Historical references should remain interpretable even when the current resource state changes.

For example:

Execution #123
resource = account/456

should remain understandable even if account/456 is later closed.

⸻

78. Temporal State and Data Retention

Retention policies must balance:

auditability
privacy
storage cost
legal requirements
operational requirements

Temporal history should not be retained indefinitely by default.

⸻

79. Temporal State and Data Minimization

Noema should retain temporal information necessary for:

* execution reconstruction
* audit
* recovery
* reconciliation
* policy enforcement

without indiscriminately copying every historical enterprise state.

⸻

80. Temporal State and Snapshots vs Events

There are two useful representations:

Snapshot:
state at time T

and:

Event:
change occurring at time T

Noema may use either or both.

⸻

81. Snapshot Advantages

Snapshots are useful for:

fast reconstruction
Trust evaluation
Context persistence
audit views

⸻

82. Event Advantages

Events are useful for:

causal history
state transitions
reconciliation
asynchronous workflows

⸻

83. Combined Temporal Model

A practical implementation may use:

Events
   +
Snapshots
   +
Provenance

to reconstruct temporal state efficiently.

⸻

84. Temporal State and Persistence

Persisted temporal state should distinguish:

current state
historical observations
execution state
decision history

These should not be collapsed into one mutable record when doing so would destroy auditability.

⸻

85. Mutable vs Immutable State

Operational state may be mutable:

execution.status = RUNNING

while historical transitions should remain reconstructable:

PLANNED → RUNNING

The implementation may use both a current projection and an immutable history.

⸻

86. Temporal State and Projections

A current-state projection can be derived from historical events.

Events
 ↓
Projection
 ↓
Current State

The projection is replaceable.

The historical record preserves lineage.

⸻

87. Temporal State and Materialized Views

Noema may materialize frequently accessed current state for performance.

But:

A materialized current view must not be mistaken for complete historical truth.

⸻

88. Temporal State and Cache

Caches introduce another temporal dimension.

A cached value should have:

observed_at
cached_at
expires_at
source

where relevant.

⸻

89. Temporal State and Cache Freshness

A cache may be valid for ordinary operations but unacceptable for high-risk execution.

The Trust Engine should apply policy rather than assuming:

cache hit = current truth

⸻

90. Temporal State and Stale-While-Revalidate

Noema may use stale information temporarily while obtaining fresh information.

But if an Action requires current state:

stale value

must not silently pass the execution gate.

⸻

91. Temporal State and External Latency

High latency increases the gap between:

observation

and:

execution

This can increase temporal risk.

⸻

92. Temporal State and TOCTOU

Noema must account for time-of-check vs time-of-use problems.

Example:

10:00
Check: account has sufficient funds
10:05
Execute transfer

The account may have changed between the check and execution.

For consequential Actions, revalidation or atomic enterprise-side guarantees may be required.

⸻

93. Temporal Preconditions and TOCTOU

A precondition evaluated earlier does not necessarily guarantee the same state at execution time.

Therefore policies may require:

check immediately before execution

or:

external transactional guarantee

⸻

94. Temporal State and Concurrency

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

95. Temporal State and Concurrency Guarantees

Noema should distinguish:

observed state

from:

atomic guarantee

A historical observation cannot provide an atomic guarantee by itself.

⸻

96. Temporal State and Enterprise Transactions

Where the enterprise system supports transactional preconditions, Noema should prefer those guarantees for consequential Actions.

For example:

transfer only if balance >= amount

may be enforced atomically by the enterprise system.

⸻

97. Temporal State and Action Contracts

Action Contracts should expose temporal semantics where relevant.

Examples:

idempotency window
authorization TTL
resource version
conditional update
ETag
optimistic concurrency token

⸻

98. Temporal State and Versions

Resource versions can provide strong temporal concurrency semantics.

Example:

resource_version = 42

Action:

update only if version = 42

If the resource has changed:

version = 43

the Action can fail safely rather than applying to stale state.

⸻

99. Temporal State and Optimistic Concurrency

Where supported, Noema should preserve concurrency tokens obtained with Evidence and provide them to Actions that require them.

⸻

100. Temporal State and ETags

HTTP-style ETags are one example:

If-Match: "abc123"

This converts temporal state into a conditional execution guarantee.

⸻

101. Temporal State and Preconditions

A strong Precondition may therefore be:

resource_version = 42

rather than merely:

resource.status = ACTIVE

The former protects against concurrent modification.

⸻

102. Temporal State and Postconditions

After execution, Noema should verify the resulting state at a defined temporal point.

⸻

103. Temporal State and Recovery

Recovery requires temporal awareness.

If Noema crashes:

Action submitted

it must determine:

what happened before the crash

without assuming that the absence of a local completion record means external failure.

⸻

104. Temporal Recovery

Recovery may therefore involve:

historical execution state
+
external operation state
+
current enterprise state

and reconciliation between them.

⸻

105. Temporal State and Compensation

Compensation depends on what happened before failure.

Example:

Step 1 succeeded
Step 2 failed

The compensation decision depends on the temporal execution history.

⸻

106. Temporal State and Workflow Ordering

Compound Intent requires temporal ordering when Actions depend on one another.

A
 ↓
B
 ↓
C

Noema must preserve which Action happened before which.

⸻

107. Temporal State and Causality

Timestamps alone may not establish causality.

Noema should use explicit relationships where available:

caused_by
depends_on
triggered_by
correlates_with

⸻

108. Temporal State and Correlation IDs

Correlation identifiers can connect temporal events:

request_id
execution_id
operation_id
event_id

This allows Noema to construct coherent execution timelines.

⸻

109. Temporal State and Event Causality

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

110. Temporal State and Ordering Guarantees

Where a source provides ordering guarantees:

sequence_number
offset
version

Noema should preserve them.

⸻

111. Temporal State and Distributed Systems

Noema operates across systems that may have:

* clock skew
* network delay
* retries
* duplicate events
* eventual consistency
* asynchronous processing

Temporal State must therefore be modeled explicitly rather than inferred from local wall-clock time alone.

⸻

112. Temporal State and Clock Skew

Timestamps from different systems may not be directly comparable.

Where temporal precision matters, Noema should prefer:

source sequence
logical version
causal identifier

when available.

⸻

113. Temporal State and Ordering Confidence

Noema should distinguish:

known ordering

from:

probable ordering

A model should not silently resolve temporal uncertainty for consequential execution.

⸻

114. Temporal Ambiguity

If the system cannot establish whether:

Event A

occurred before:

Event B

and that ordering affects execution, the appropriate result may be:

RECONCILE

or:

ESCALATE

rather than guess.

⸻

115. Temporal State and Deterministic Uncertainty

Unknown temporal ordering should become an explicit system state.

ORDER_UNKNOWN

is preferable to inventing:

A happened before B

without evidence.

⸻

116. Temporal State and Policy Evaluation

Policies can contain temporal constraints:

Action must occur within 10 minutes of approval.

Noema can evaluate:

execution_at - approval_at <= 10 minutes

deterministically.

⸻

117. Temporal Policy Examples

Policies may specify:

approval freshness
authentication freshness
balance freshness
resource version
session lifetime
authorization lifetime

⸻

118. Temporal State and Human Approval

Human approval may have a validity period.

approved_at = 10:00
expires_at = 11:00

An Action at 12:00 cannot automatically rely on the same approval.

⸻

119. Temporal State and Authentication

Authentication may also have a freshness requirement.

For example:

authenticated_at = 10:00

may be insufficient for a high-risk Action at 14:00.

The policy determines whether reauthentication is required.

⸻

120. Temporal State and Session State

Session state can change independently of business state.

Noema should preserve the relevant authentication and session context when it contributes to Trust.

⸻

121. Temporal State and Identity Revalidation

For high-risk Actions:

historical identity

may require:

current identity verification

before execution.

⸻

122. Temporal State and Policy Changes During Execution

Suppose:

10:00
Policy v5 permits Action
10:05
Policy v6 prohibits Action
10:10
Action executes

Noema must have an explicit policy governing whether the Action uses:

policy at authorization time

or:

policy at execution time

It must not be accidental.

⸻

123. Policy Effective Semantics

The applicable policy point should be defined by the execution contract or enterprise policy.

Possible anchors include:

Intent received
Trust decision
Action start
Action commit

⸻

124. Temporal State and Long-Lived Plans

A plan generated today may execute tomorrow.

The plan should therefore distinguish:

plan creation time

from:

execution time

and identify which elements require revalidation.

⸻

125. Temporal State and Plan Validity

A plan may have:

valid_until

or require dynamic re-evaluation of its assumptions.

⸻

126. Temporal State and Planning Assumptions

Every significant plan assumption should be considered time-sensitive.

Example:

Assumption:
subscription is ACTIVE

If the plan executes later, Noema may need to verify that assumption again.

⸻

127. Temporal State and Execution Preconditions

Planning can produce:

Precondition:
subscription.status = ACTIVE

Execution evaluates it at the appropriate time.

⸻

128. Temporal State and Dynamic Context

Some Context is static:

organization_id

Some is dynamic:

account_balance

Noema should not treat both as having identical temporal behavior.

⸻

129. Temporal State and Context Classification

Useful conceptual categories include:

Static
Slow-changing
Dynamic
Ephemeral
Event-derived
Historical

The required freshness depends on the category.

⸻

130. Temporal State and Data Model

A temporal observation may conceptually contain:

TemporalObservation {
    value
    valid_from
    valid_until
    observed_at
    received_at
    source
    version
}

The exact schema is implementation-dependent.

⸻

131. Temporal State and Current Projections

A current projection may be derived:

Historical Observations
        ↓
Temporal Resolution
        ↓
Current State

But the projection should remain traceable to the observations from which it was derived.

⸻

132. Temporal State and Provenance

A temporal observation should therefore conceptually have:

Observation
 ├── value
 ├── temporal metadata
 └── provenance

⸻

133. Temporal State and Evidence

Evidence should preserve enough temporal information to determine:

when was this true?
when was this observed?
when was this received?

where relevant.

⸻

134. Temporal State and Canonical Data

Canonical data may represent the latest authoritative state.

But Noema should not discard the temporal metadata necessary to understand:

when that state became known

or:

which version was used.

⸻

135. Temporal State and Data Lineage

Data lineage becomes:

Source
 ↓
Observation at T1
 ↓
Transformation
 ↓
Evidence at T2
 ↓
Decision at T3
 ↓
Action at T4
 ↓
Outcome at T5

This is temporal provenance.

⸻

136. Temporal State and Auditability

A useful audit record should answer:

What did Noema know at the moment it acted?

Not merely:

What does the system say now?

⸻

137. Temporal State and Explainability

When explaining a historical decision:

“The transfer was approved because the account had sufficient balance.”

the explanation should be grounded in:

balance observed = $20,000
observed_at = 10:00
decision_at = 10:01
policy = v7

rather than today’s balance.

⸻

138. Temporal State and Compliance

Many audit and compliance requirements are inherently temporal.

Questions include:

What policy was active?
Who was authorized?
What information was available?
When was approval given?
When did execution occur?

Temporal State supports these questions.

⸻

139. Temporal State and Historical Immutability

Historical observations that materially influenced decisions should not be silently rewritten.

Corrections should produce new observations.

⸻

140. Temporal Correction

If an enterprise later corrects a value:

10:00
balance reported = $20,000
10:30
source corrects record:
actual balance = $18,000

Noema should preserve the fact that $20,000 was what it observed at 10:00.

⸻

141. Temporal State and Retrospective Correction

A correction may affect future decisions but should not retroactively alter what Noema knew at the time.

⸻

142. Temporal State and Audit Integrity

This creates an important distinction:

Historical observation:
what was known
Corrected state:
what is now known about the past

Both may be retained when required.

⸻

143. Temporal State and Reprocessing

When historical data is reprocessed, the resulting interpretation should be identified as a new computation.

It should not overwrite the historical interpretation used during the original Execution.

⸻

144. Temporal State and Model Reprocessing

Likewise, a newer model may resolve historical Intent differently.

That does not change what the original model resolved at execution time.

⸻

145. Temporal State and Model Version

Where model output materially affects execution, provenance should identify:

model version
inference time

so historical interpretation remains reconstructable.

⸻

146. Temporal State and Historical Model Behavior

A historical execution should remain associated with the model version that produced the relevant inference.

⸻

147. Temporal State and Deterministic Replay

Replay should distinguish:

historical replay

from:

modern reevaluation

Historical replay uses historical inputs.

Modern reevaluation uses current rules and potentially current models.

They are different operations.

⸻

148. Temporal State and Evaluation

Noema can use historical executions to evaluate:

policy quality
model quality
intent resolution
trust decisions
execution reliability

without changing the original records.

⸻

149. Temporal State and Learning

Historical state can provide training or evaluation data.

However, learning must not mutate historical execution truth.

⸻

150. Temporal State and Causal Analysis

Temporal ordering can help determine:

what happened before failure
what changed before the Action
which event preceded the Outcome

This supports debugging and recovery.

⸻

151. Temporal State and Root Cause

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

152. Temporal State and Compensation

Compensation often depends on temporal facts:

Was Step A completed before Step B failed?

The answer comes from execution history.

⸻

153. Temporal State and Partial Execution

A compound Action may partially execute:

Step A: succeeded at 10:00
Step B: failed at 10:01
Step C: not started

Temporal state identifies exactly where execution stopped.

⸻

154. Temporal State and Human Intervention

Human intervention should be timestamped.

10:05
Operator approves retry

This approval becomes part of the temporal execution history.

⸻

155. Temporal State and Overrides

Overrides should create new temporal events rather than rewriting prior Trust decisions.

Trust:
REJECT at 10:00
Human override:
APPROVE at 10:05

Both remain visible.

⸻

156. Temporal State and Audit Trail

The audit trail should preserve state transitions:

10:00 RECEIVED
10:01 RESOLVED
10:02 TRUSTED
10:03 EXECUTING
10:04 UNKNOWN
10:06 RECONCILED
10:07 COMPLETED

⸻

157. Temporal State and State Machines

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

158. Temporal State and Invalid Transitions

Temporal history should preserve invalid or rejected transitions where they matter.

Example:

Attempt:
COMPLETED → RUNNING

may be rejected.

The rejection itself can be part of the execution history.

⸻

159. Temporal State and Monotonicity

Some states should progress monotonically.

For example:

COMPLETED

should not silently become:

RUNNING

unless the domain explicitly supports such transitions.

⸻

160. Temporal State and Reversible State

Other business states may legitimately reverse:

ACTIVE
 → SUSPENDED
 → ACTIVE

Temporal State must preserve each transition.

⸻

161. Temporal State and State Semantics

State names alone are insufficient.

A state should have defined semantics regarding:

entry
exit
validity
transition rules
temporal behavior

⸻

162. Temporal State and Outcome Semantics

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

⸻

163. Temporal State and Knowledge State

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

164. Knowledge State

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

165. Temporal Knowledge

Noema must preserve:

When did Noema become aware of this fact?

This is different from:

When did the fact become true?

⸻

166. Temporal State and Epistemic Boundaries

This distinction is fundamental to safe automation.

What happened
≠
What Noema knew
≠
What Noema inferred

Temporal State helps maintain all three distinctions.

⸻

167. Temporal State and Inference

A model may infer:

payment/123 is probably the last payment

at 10:00.

At 10:01, a new payment arrives.

The inference may become obsolete even though it was reasonable at 10:00.

⸻

168. Temporal Inference Validity

Inference should therefore be evaluated relative to the temporal state in which it was produced.

⸻

169. Temporal State and Clarification

If relevant state changes while Intent is being resolved:

Candidate A at 10:00
Candidate B created at 10:01

Noema may need to re-resolve rather than blindly execute the original candidate.

⸻

170. Temporal State and Execution Windows

An Intent may have a defined execution window:

valid_from
valid_until

This can prevent stale Intent from being executed indefinitely.

⸻

171. Temporal State and User Intent

User Intent itself may become stale.

Example:

“Transfer $5,000 from account A to B.”

If submitted yesterday, Noema should not assume the user still intends execution today unless the workflow semantics permit deferred execution.

⸻

172. Temporal Intent Validity

The Intent lifecycle should therefore define when an Intent remains executable and when it requires re-confirmation.

⸻

173. Temporal State and Expired Intent

An expired Intent should transition to an explicit state:

EXPIRED

rather than remaining ambiguously executable.

⸻

174. Temporal State and Long-Lived Authorization

A user may authorize an automation once for repeated Actions.

The authorization may have:

scope
effective_from
expires_at

Temporal State enables enforcement.

⸻

175. Temporal State and Recurring Execution

Recurring Intent creates repeated temporal executions.

Each execution should have its own:

Context
Trust evaluation
Evidence
Decision
Action
Outcome

rather than assuming that a previous execution remains permanently trusted.

⸻

176. Temporal State and Repeated Actions

A successful execution yesterday does not necessarily authorize today’s execution.

Current state and current policy may differ.

⸻

177. Temporal State and Scheduling

Scheduled execution introduces a gap:

Intent created
        ↓
scheduled time
        ↓
execution

Relevant assumptions may need revalidation at execution time.

⸻

178. Temporal State and Deferred Execution

The longer the delay, the more likely dynamic Evidence becomes stale.

Risk and policy should determine the required revalidation.

⸻

179. Temporal State and Policy TTL

Trust decisions may use explicit TTLs:

valid_for = 5 minutes

After expiry:

REVALIDATION_REQUIRED

⸻

180. Temporal State and Action TTL

Some external Actions may also have deadlines.

Example:

payment authorization expires in 15 minutes

Noema should preserve and enforce these temporal constraints where exposed by the integration.

⸻

181. Temporal State and External Deadlines

External deadlines should be represented as constraints rather than merely comments.

⸻

182. Temporal State and Temporal Constraints

A Temporal Constraint can conceptually express:

before
after
within
until
since
during

These can apply to:

Intent
Evidence
Policy
Authorization
Action
Outcome

⸻

183. Temporal Constraint Example

Approval must occur within 30 minutes before execution.

Conceptually:

0 <= execution_at - approval_at <= 30m

⸻

184. Temporal Constraint Example

Balance observation must be less than 60 seconds old.

Conceptually:

execution_at - balance.observed_at <= 60s

⸻

185. Temporal Constraint Example

Refund must occur before subscription cancellation.

This creates a temporal dependency:

refund_at < cancellation_at

⸻

186. Temporal State and Action Ordering

Temporal dependencies should be explicit in a plan.

Refund
   ↓
Cancel Subscription

rather than relying on incidental execution order.

⸻

187. Temporal State and Causal Dependencies

Where Action B requires the Outcome of Action A:

A completed
   ↓
B allowed

The temporal dependency becomes an execution precondition.

⸻

188. Temporal State and Parallel Actions

Independent Actions may execute concurrently.

Their temporal ordering may be undefined.

Noema should not fabricate an ordering where none exists.

⸻

189. Temporal State and Concurrency Semantics

A compound Intent may therefore specify:

sequential
parallel
ordered
unordered
conditional

execution semantics.

⸻

190. Temporal State and Race Conditions

When two Actions modify related resources concurrently, the enterprise integration must provide appropriate concurrency semantics.

Noema should not rely solely on timestamps to prevent races.

⸻

191. Temporal State and Version Checks

Resource versions can provide stronger guarantees:

version = 17

Action executes only if:

version still = 17

Otherwise:

REVALIDATE

⸻

192. Temporal State and Enterprise Atomicity

When possible, Noema should delegate atomic state guarantees to the System of Record.

Noema’s temporal model provides context and reasoning; it does not replace enterprise transaction semantics.

⸻

193. Temporal State and Source-of-Truth Boundaries

A historical snapshot in Noema is not a replacement for the enterprise System of Record.

It is a record of:

what Noema observed

at a particular time.

⸻

194. Temporal State and Data Ownership

Therefore:

Enterprise:
owns state
Noema:
owns execution history and temporal observations relevant to execution

⸻

195. Temporal State and Audit Ownership

Noema should own enough temporal execution history to explain:

what happened in Noema

while preserving references to:

what happened in enterprise systems.

⸻

196. Temporal State and Audit Completeness

An audit record should be temporally ordered enough to reconstruct the Execution journey.

⸻

197. Temporal State and Explainability

Explanations should use the temporal context relevant to the decision.

Avoid:

“The account had $20,000.”

Prefer:

“At the time the transfer was authorized, the account was observed with a balance of $20,000.”

The latter is temporally precise.

⸻

198. Temporal State and Trust Explanation

Likewise:

“The user was authorized.”

should be grounded as:

“The identity system reported the user had the required permission at the time the authorization check was performed.”

⸻

199. Temporal State and Outcome Explanation

For outcomes:

“The refund succeeded.”

should distinguish:

Action submitted

from:

Outcome later verified

⸻

200. Temporal State and Failure Explanation

A timeout should be explained as:

“No response was received within the configured timeout.”

not:

“The refund failed.”

unless authoritative evidence establishes failure.

⸻

201. Temporal State and Unknown State

Temporal uncertainty should produce explicit states:

UNKNOWN
STALE
EXPIRED
PENDING
REQUIRES_REVALIDATION

rather than silently converting uncertainty into a definitive state.

⸻

202. Temporal State and Trust Decisions

A Trust Engine may therefore evaluate:

Evidence present?
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

⸻

203. Temporal State and Deterministic Outcomes

The Trust Engine should produce deterministic outcomes such as:

EXECUTE
CLARIFY
ESCALATE
REJECT
REVALIDATE

based on temporal conditions and policy.

⸻

204. Temporal State and Revalidation

REVALIDATE is particularly important for temporal state.

It means:

The previous decision or Evidence may have been valid, but its temporal validity is no longer sufficient for the current execution.

⸻

205. Temporal State and Clarification

CLARIFY is appropriate when the temporal interpretation itself is ambiguous.

Example:

“Use the payment from last week.”

If multiple payments qualify and the temporal criterion does not resolve uniquely, Noema should clarify.

⸻

206. Temporal State and Escalation

ESCALATE may be appropriate when temporal conflict cannot be resolved automatically.

⸻

207. Temporal State and Rejection

REJECT is appropriate when a temporal constraint is definitively violated.

Example:

Approval expired

⸻

208. Temporal State and Execution

Before execution:

Temporal Preconditions
        ↓
Trust
        ↓
Action

must be satisfied.

⸻

209. Temporal State and Post-Execution

After execution:

Outcome Evidence
        ↓
Temporal verification
        ↓
Final state

must establish what happened.

⸻

210. Temporal State and Persistence Model

A conceptual persisted record may contain:

TemporalRecord {
    record_id
    subject
    state
    valid_from
    valid_until
    observed_at
    received_at
    recorded_at
    source
    version
}

The exact implementation remains open.

⸻

211. Temporal State and State History

Noema should preserve history where history materially affects:

trust
execution
recovery
reconciliation
audit

Not every transient value requires indefinite retention.

⸻

212. Temporal State and Retention Policy

Retention should be explicitly governed.

For example:

Execution history:
7 years
Operational cache:
15 minutes

The actual durations depend on enterprise policy and requirements.

⸻

213. Temporal State and Privacy

Temporal history may reveal sensitive behavioral information.

Examples:

when a user accessed a system
when money moved
when an employee changed role

Access and retention must therefore be controlled.

⸻

214. Temporal State and Data Minimization

Noema should retain temporal information proportional to its purpose.

⸻

215. Temporal State and Integrity

Historical state relevant to audit should be protected from silent modification.

⸻

216. Temporal State and Tamper Evidence

Where necessary, Noema may use:

hashes
signatures
immutable logs
version chains

to strengthen temporal history integrity.

⸻

217. Temporal State and Recovery Integrity

Recovery should never assume:

missing record = did not happen

External systems may have progressed independently.

⸻

218. Temporal State and External Truth

The System of Record remains the authoritative source for current business state.

Noema’s historical record describes its observed and execution history.

⸻

219. Temporal State and Reconciliation

When local and external state disagree:

Noema:
UNKNOWN
Enterprise:
SUCCEEDED

the enterprise observation can resolve the local uncertainty.

⸻

220. Temporal State and Eventual Reconciliation

Reconciliation should produce a new temporal observation rather than rewriting the old state.

⸻

221. Temporal State and Current Projection

The current projection should always be derivable from the latest applicable state according to source authority and temporal rules.

⸻

222. Temporal State and Historical Projection

Historical projections should be reconstructable at a specified time where required.

For example:

state_as_of(T)

⸻

223. Temporal Query Semantics

Useful conceptual queries include:

state_now(resource)
state_as_of(resource, T)
observed_at(record)
valid_during(record, interval)
changed_between(resource, T1, T2)

These semantics may guide implementation.

⸻

224. Temporal State and API Design

Interfaces may expose temporal metadata explicitly.

For example:

GET /resource

may return:

version
observed_at

where relevant.

⸻

225. Temporal State and Event API

Event interfaces should preserve:

event_id
event_time
received_at
sequence
version

where available.

⸻

226. Temporal State and Integration Model

Integrations should describe temporal guarantees where known:

real-time
eventually consistent
snapshot
cached
asynchronous
transactional

This informs Trust evaluation.

⸻

227. Temporal State and Enterprise Action Graph

The Enterprise Action Graph may represent temporal characteristics of Actions:

Action
 ├── preconditions
 ├── freshness requirements
 ├── concurrency semantics
 ├── idempotency window
 └── outcome timing

⸻

228. Temporal State and Action Contract

An Action Contract may specify:

requires_current_state
supports_version_check
supports_idempotency
returns_async_operation

These capabilities affect temporal execution safety.

⸻

229. Temporal State and Integration Capability

Noema should know whether an integration supports:

conditional writes
transactions
version checks
idempotency keys
event notifications
read-after-write consistency

where relevant.

⸻

230. Temporal State and Strong Guarantees

Strong enterprise guarantees can reduce temporal uncertainty.

For example:

atomic conditional update

is stronger than:

read state
→ wait
→ write state

Noema should prefer stronger guarantees where available.

⸻

231. Temporal State and Weak Guarantees

If an integration provides only eventually consistent reads, Noema should account for that uncertainty in Trust and Execution.

⸻

232. Temporal State and Risk

The weaker the temporal guarantee, the more important:

revalidation
conditional execution
human approval

may become.

⸻

233. Temporal State and High-Risk Actions

For high-risk Actions, Noema should prefer:

fresh authoritative Evidence
+
strong concurrency guarantees
+
explicit temporal constraints

⸻

234. Temporal State and Low-Risk Actions

Low-risk Actions may tolerate:

cached
slightly stale
secondary

Evidence when policy permits.

⸻

235. Temporal State and Policy

The Trust Engine should never invent freshness requirements.

They should originate from:

enterprise policy
Action contract
risk policy
integration guarantees

⸻

236. Temporal State and Risk-Adjusted Freshness

Conceptually:

Risk
 ↓
Freshness Requirement
 ↓
Temporal Validation
 ↓
Trust Decision

⸻

237. Temporal State and Evidence Quality

Evidence quality includes:

authority
provenance
freshness
scope
integrity
temporal validity

⸻

238. Temporal State and Evidence Conflict

If two observations disagree, Noema should consider:

source authority
observation time
valid time
version
scope

before resolving the conflict.

⸻

239. Temporal State and Temporal Authority

A later observation from a lower-authority source does not necessarily supersede an earlier observation from the authoritative source.

⸻

240. Temporal State and Historical Authority

The authoritative source may itself change over time.

For example:

System A authoritative until Jan 1
System B authoritative after Jan 1

The authority model itself can be temporal.

⸻

241. Temporal State and Source Migration

When systems migrate:

System A
   ↓
System B

Noema must preserve the source identity relevant to historical observations.

⸻

242. Temporal State and Semantic Drift

Meaning can change over time.

A field:

status = ACTIVE

may have different semantics after a schema change.

Version metadata helps preserve interpretation.

⸻

243. Temporal State and Schema Evolution

Historical records should retain enough version information to interpret them correctly.

⸻

244. Temporal State and Policy Evolution

Policies evolve.

Historical Trust decisions should remain tied to the policy version that governed them.

⸻

245. Temporal State and Contract Evolution

Action Contracts evolve.

Historical executions should remain tied to the contract used at execution time.

⸻

246. Temporal State and Model Evolution

Models evolve.

Historical model decisions should remain tied to the model version used.

⸻

247. Temporal State and Noema Evolution

Noema’s own semantic schemas evolve.

Historical records should preserve sufficient version metadata to remain interpretable.

⸻

248. Temporal State and Backward Compatibility

Temporal records should not depend on mutable semantics that make historical data impossible to interpret after upgrades.

⸻

249. Temporal State and Canonical Semantics

Canonical state definitions should remain version-aware when their meaning changes materially.

⸻

250. Temporal State and Temporal Ontology

Ontology concepts can themselves have temporal validity.

For example:

Capability
Policy
Relationship
State

may be introduced, changed, or deprecated over time.

⸻

251. Temporal State and Relationships

Relationships can change:

User → belongs_to → Organization A

then:

User → belongs_to → Organization B

Temporal state determines which relationship applied at a given time.

⸻

252. Temporal State and Permissions Graph

Permissions may also change:

User
 ↓
Role
 ↓
Permission

The relationship must be evaluated relative to the relevant time.

⸻

253. Temporal State and Entity Relationships

Similarly:

Customer
 ↓ owns
Account

may change over time.

Historical execution must preserve the relationship relevant at execution time.

⸻

254. Temporal State and Resource Ownership

Ownership changes should be temporally represented when ownership affects authorization.

⸻

255. Temporal State and Organizational Context

Enterprise context is dynamic.

organization
department
role
manager
location
cost center

may change over time.

Only context relevant to execution needs to be persisted, but when it is material, its temporal validity matters.

⸻

256. Temporal State and User Context

User Intent is interpreted within the context available at that time.

Later context should not silently rewrite historical interpretation.

⸻

257. Temporal State and Intent History

A complete Intent history may contain:

original input
clarifications
resolved interpretation
Trust evaluation
execution
outcome

each with temporal metadata.

⸻

258. Temporal State and Clarification History

Clarification changes Intent state.

Example:

10:00
"refund my last payment"
10:01
"the $500 payment"
10:02
resolved to payment/123

The temporal sequence matters for reconstruction.

⸻

259. Temporal State and User Corrections

If the user corrects themselves:

“No, not that payment. The other one.”

the new statement should become a new Intent event rather than rewriting the previous interpretation.

⸻

260. Temporal State and Human Intent Evolution

Intent can evolve during an interaction.

Noema should preserve the transition:

candidate intent
   ↓
clarification
   ↓
revised intent

⸻

261. Temporal State and Trust Re-evaluation

When Intent changes materially, Trust should be evaluated again.

⸻

262. Temporal State and Execution Replanning

If relevant state changes before execution:

plan created
   ↓
state changed

Noema may need to replan.

⸻

263. Temporal State and Dynamic Planning

Planning should therefore distinguish:

static plan components

from:

state-dependent assumptions

⸻

264. Temporal State and Plan Invalidation

A plan may become invalid when:

resource deleted
policy changed
authorization revoked
Evidence expires
Action Contract changes

The resulting state should be explicit:

PLAN_INVALIDATED

⸻

265. Temporal State and Execution Safety

Temporal State acts as one of the mechanisms preventing stale decisions from becoming unsafe executions.

⸻

266. Temporal State and Deterministic Execution

The principle is:

A decision is deterministic only relative to the state and Evidence against which it was evaluated.

If the relevant state changes, Noema must determine whether that invalidates the decision.

⸻

267. Temporal State and Trust Recalculation

Noema should not continuously recompute Trust merely because time passes.

Instead, Policies should define when temporal changes require reevaluation.

⸻

268. Temporal State and State Change Triggers

Possible triggers include:

Evidence expiration
Policy change
Authorization change
Resource version change
External event
Execution delay
Risk threshold

⸻

269. Temporal State and Event-Driven Revalidation

External events may invalidate an existing decision.

Example:

Trust:
EXECUTE
Event:
account.suspended
Result:
Trust invalidated

⸻

270. Temporal State and Reactive Trust

This enables Trust to respond to known state changes without turning the Trust Engine into a probabilistic continuous monitor.

⸻

271. Temporal State and Deterministic Invalidation

If a policy states:

account suspension invalidates transfers

then:

account.suspended

deterministically invalidates the relevant execution authority.

⸻

272. Temporal State and Execution Locks

Some enterprise systems provide temporary locks or reservations.

These may be modeled as temporal state:

reservation
valid_from
valid_until

⸻

273. Temporal State and Reservations

A reservation may prevent conflicting Actions during a defined interval.

Noema should respect the semantics provided by the enterprise system.

⸻

274. Temporal State and Leases

Leases are explicitly temporal:

lease_acquired
expires_at

Noema must not assume a lease remains valid beyond its expiration.

⸻

275. Temporal State and Distributed Locks

Distributed locks have temporal validity and failure semantics.

Noema should treat them as integration-specific guarantees, not generic truth.

⸻

276. Temporal State and Execution Windows

An Execution may have:

started_at
deadline
expires_at

These boundaries should be enforced according to policy and Action Contract.

⸻

277. Temporal State and SLA

Execution SLAs can also be temporal constraints:

Action must complete within 30 seconds.

This affects monitoring and outcome state but does not necessarily mean the external Action failed when the deadline is exceeded.

⸻

278. Temporal State and Timeout

Timeout means:

Noema stopped waiting.

It does not necessarily mean:

external operation stopped.

This distinction is critical.

⸻

279. Temporal State and Async Outcomes

An asynchronous operation may complete after Noema’s timeout.

Temporal state allows the later Outcome to reconcile the earlier unknown state.

⸻

280. Temporal State and Retry

Retries must consider temporal execution history.

Before retry:

Did the previous attempt possibly succeed?

If yes:

reconcile

before issuing a potentially duplicate Action.

⸻

281. Temporal State and Idempotency Windows

An external system may define:

idempotency_key valid for 24 hours

Noema must respect the temporal scope of that guarantee.

⸻

282. Temporal State and Compensation Windows

Some compensation operations may only be possible within a defined time period.

This should be modeled explicitly.

⸻

283. Temporal State and Recovery Windows

Recovery workflows may also have deadlines.

Example:

cancel operation within 5 minutes

⸻

284. Temporal State and Failure Classification

A failure may be:

immediate
delayed
unknown
expired
reconciled

Temporal history helps classify it correctly.

⸻

285. Temporal State and Retry Policy

Retry eligibility may depend on:

elapsed time
attempt count
external operation state
idempotency window

⸻

286. Temporal State and Backoff

Retry timing is itself part of execution history:

attempt 1 → 10:00
attempt 2 → 10:01
attempt 3 → 10:03

⸻

287. Temporal State and Audit

A complete retry history should remain reconstructable.

⸻

288. Temporal State and Human Intervention Timing

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

289. Temporal State and Approval Expiration

A stale human approval should not automatically remain valid.

⸻

290. Temporal State and Escalation

Escalation itself has temporal semantics:

escalated_at
response_deadline
resolved_at

⸻

291. Temporal State and SLA Escalation

If a human does not respond within the required window:

approval_pending

may transition to:

expired

rather than remaining indefinitely executable.

⸻

292. Temporal State and State Machine

Temporal behavior should therefore be represented explicitly in Noema state machines.

⸻

293. Temporal State and Data Contracts

Interfaces exposing temporal information should use consistent semantics for:

created_at
updated_at
observed_at
effective_at
valid_from
valid_until
event_time
received_at

Each field must have a defined meaning.

⸻

294. Timestamp Semantics

Noema should avoid generic timestamp fields whose meaning is ambiguous.

For example:

timestamp

is weaker than:

observed_at

or:

effective_at

⸻

295. Temporal Precision

Precision should match the domain.

Financial execution may require finer temporal resolution than ordinary metadata.

⸻

296. Time Zones

Temporal data should use explicit time-zone semantics.

Internally, normalized UTC timestamps are generally preferable for machine reasoning, while preserving original timezone context where the domain meaning depends on it.

⸻

297. Calendar Semantics

Human expressions such as:

tomorrow
next month
end of day
business day

require domain-specific calendar semantics.

Noema should not infer these arbitrarily.

⸻

298. Temporal Intent and Business Calendars

Enterprise workflows may define:

business day
working hours
holiday calendar
cutoff time

These can materially affect execution.

⸻

299. Temporal Policy and Business Calendars

A policy may say:

“Transfers submitted after 4 PM execute next business day.”

Noema must use the enterprise’s defined calendar rather than a generic assumption.

⸻

300. Temporal State and Recurrence

Recurring Intent requires explicit recurrence semantics:

daily
weekly
monthly
business-day

and a defined timezone/calendar where relevant.

⸻

301. Temporal State and Scheduling Ambiguity

If the user’s phrase:

“every Friday”

does not specify timezone and multiple organizational timezones matter, Noema may need clarification.

⸻

302. Temporal State and Timezone Boundaries

Execution scheduled for:

09:00 Africa/Lagos

is not necessarily:

09:00 UTC

Temporal semantics must be explicit.

⸻

303. Temporal State and Daylight Saving

Where applicable, timezone transitions can produce ambiguous or nonexistent local times.

The temporal model should rely on a proper timezone database rather than naive offsets.

⸻

304. Temporal State and Business Cutoffs

Cutoff times should be represented as explicit temporal constraints.

⸻

305. Temporal State and Expiration

Expiration should be explicit:

expires_at

rather than inferred from:

updated_at

⸻

306. Temporal State and Lifecycle

Every temporal object should have a defined lifecycle where relevant:

created
active
expired
superseded
revoked
archived

⸻

307. Temporal State and Supersession

A newer version may supersede an older version without invalidating its historical relevance.

Example:

Policy v6
superseded by v7

v6 remains the policy used by historical decisions.

⸻

308. Temporal State and Revocation

Revocation is different from supersession.

Authorization granted
   ↓
revoked

The historical authorization remains true before revocation but cannot be used after it.

⸻

309. Temporal State and Effective Revocation

The system should distinguish:

revoked_at

from:

effective_revocation_at

when the enterprise domain requires that distinction.

⸻

310. Temporal State and Retroactive Changes

Some enterprise systems may make retroactive corrections.

Noema should preserve both:

historical observation

and:

later correction

when necessary.

⸻

311. Temporal State and Audit Semantics

An audit trail should never silently rewrite history because the source later changed.

⸻

312. Temporal State and Data Correction

Corrections should be additive where possible:

Observation 1
Correction 2

rather than destructive replacement.

⸻

313. Temporal State and Historical Context

A historical Execution should retain the relevant Context snapshot or references sufficient to reconstruct it.

⸻

314. Temporal State and Context Mutation

Current Context should never mutate historical Context records.

⸻

315. Temporal State and Snapshot Identity

Snapshots should have stable identifiers:

context_snapshot_id

This lets Decisions reference exactly which Context was used.

⸻

316. Temporal State and Evidence Identity

Evidence should similarly have stable identifiers.

evidence_id

This prevents later updates from silently changing historical decisions.

⸻

317. Temporal State and Decision Identity

Trust decisions should be immutable historical facts:

decision_id
decision_at
result
inputs
policy_version

⸻

318. Temporal State and Action Identity

Executions and Action attempts should have stable IDs:

execution_id
attempt_id
external_operation_id

⸻

319. Temporal State and Outcome Identity

Outcomes should also be identifiable:

outcome_id
observed_at
source

⸻

320. Temporal State and Lineage

These IDs create a temporal lineage:

Intent
 ↓
Context Snapshot
 ↓
Evidence
 ↓
Trust Decision
 ↓
Execution
 ↓
Attempt
 ↓
External Operation
 ↓
Outcome

⸻

321. Temporal State and Audit Reconstruction

The entire timeline can then be reconstructed without depending on mutable current state.

⸻

322. Temporal State and Observability

Operational observability can use temporal state to expose:

latency
queue time
execution time
retry delay
reconciliation delay
human intervention time

⸻

323. Temporal State and Performance

Temporal metadata should support performance analysis without becoming part of business-state ownership.

⸻

324. Temporal State and Debugging

Engineers can ask:

What changed between decision and execution?

Temporal State provides the answer.

⸻

325. Temporal State and Incident Analysis

After an incident:

What was true?
What did Noema know?
What changed?
When did it change?
Why was the Action still allowed?

These are temporal questions.

⸻

326. Temporal State and Safety

Temporal correctness is therefore part of execution safety.

A decision can be semantically correct at T1 and unsafe at T2.

⸻

327. Temporal Safety Principle

Validity at decision time does not automatically imply validity at execution time.

Whether the decision remains executable must be determined by policy.

⸻

328. Temporal State and Trust Revalidation Principle

When temporal validity is material to an Action, Noema must explicitly determine whether the relevant Evidence remains valid before execution.

⸻

329. Temporal State and Historical Truth Principle

Noema must preserve what it knew at the time without rewriting history based on later information.

⸻

330. Temporal State and Current Truth Principle

Current enterprise state must be obtained from the authoritative System of Record when current state is required.

⸻

331. Temporal State and Uncertainty Principle

When temporal ordering, freshness, or validity cannot be established and materially affects execution, uncertainty must become an explicit Trust state rather than an implicit assumption.

⸻

332. Core Invariants

Invariant 1

Historical state must remain distinguishable from current state.

Invariant 2

Observation time must remain distinguishable from receipt time.

Invariant 3

Event time must remain distinguishable from processing time.

Invariant 4

Effective time must remain distinguishable from recording time.

Invariant 5

Historical Decisions must retain the temporal context under which they were made.

Invariant 6

Historical Evidence must not be silently replaced by newer Evidence.

Invariant 7

New Evidence must create a new temporal observation when it represents a new observation.

Invariant 8

Current state must be obtained from the appropriate authoritative System of Record when current state is required.

Invariant 9

Historical snapshots must not be treated as current truth merely because they are persisted by Noema.

Invariant 10

Evidence freshness requirements must be determined by policy, risk, and Action semantics.

Invariant 11

Expired Evidence may remain historically valid while being unusable for current execution.

Invariant 12

Expired authorization must not silently authorize new execution.

Invariant 13

Policy versions must remain associated with the decisions they governed.

Invariant 14

Action Contract versions must remain associated with the executions that used them.

Invariant 15

Model versions must remain associated with consequential model inferences where required for reconstruction.

Invariant 16

Temporal conflicts must not be silently resolved by recency alone.

Invariant 17

Source authority and temporal recency are separate dimensions.

Invariant 18

Unknown temporal ordering must remain explicitly unknown when it materially affects execution.

Invariant 19

Timeout must not be interpreted as external failure without supporting Evidence.

Invariant 20

Recovery must account for external Actions that may have occurred without a local completion record.

Invariant 21

Retries must consider temporal execution history and idempotency semantics.

Invariant 22

Long-running or deferred executions must revalidate temporal assumptions when required by policy.

Invariant 23

Historical Trust decisions must not be retroactively rewritten.

Invariant 24

Revalidation is a new evaluation, not a mutation of historical Trust.

Invariant 25

Historical corrections must not erase what Noema observed at the time.

Invariant 26

Temporal state must respect tenant, organizational, security, and data boundaries.

Invariant 27

Temporal history should be retained according to explicit retention requirements.

Invariant 28

Temporal metadata should use precise semantics rather than ambiguous generic timestamps.

Invariant 29

Temporal constraints that materially affect execution must be explicit.

Invariant 30

Noema must distinguish domain state from Noema’s knowledge state.

Invariant 31

Noema must distinguish what happened from what it knew happened.

Invariant 32

Noema must distinguish inference time from the temporal validity of the inferred fact.

Invariant 33

State transitions relevant to execution, recovery, reconciliation, or audit must remain reconstructable.

Invariant 34

A change in current state must not silently alter historical execution records.

Invariant 35

Temporal validity must be evaluated relative to the Action being performed.

Invariant 36

When temporal uncertainty materially affects execution, Noema must transition to an explicit safe state such as REVALIDATE, CLARIFY, ESCALATE, or REJECT.

⸻

333. Final Definition

Temporal State is Noema’s representation of state, observations, knowledge, and validity across time. It preserves the distinction between what was true, what was observed, what Noema knew, what was decided, what was executed, and what was later verified. Temporal State allows Noema to evaluate freshness, validity, ordering, expiration, concurrency, recovery, and revalidation without confusing historical information with current enterprise truth.

The canonical temporal chain is:

              DOMAIN STATE
                   │
                   ▼
              OBSERVATION
             at time T₁
                   │
                   ▼
              EVIDENCE
             known at T₂
                   │
                   ▼
           TRUST / DECISION
             at time T₃
                   │
                   ▼
              EXECUTION
             at time T₄
                   │
                   ▼
          EXTERNAL STATE CHANGE
             at time T₅
                   │
                   ▼
          OUTCOME OBSERVATION
             at time T₆

The key principle is:

Noema must know not only what is true, but what was true when, what it knew when, and whether that knowledge is still valid for the Action it is about to perform.