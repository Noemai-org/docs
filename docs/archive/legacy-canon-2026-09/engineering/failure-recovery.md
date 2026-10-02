> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Failure Recovery

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/failure-recovery.md

⸻

1. Definition

Failure Recovery is Noema’s engineering specification for detecting, classifying, containing, recovering from, and recording failures that occur during Intent processing, Action Graph evaluation, Action Contract execution, and Outcome formation.

Failure Recovery defines how Noema behaves when an operation does not proceed according to its expected execution semantics.

It does not redefine:

* Intent semantics
* Trust semantics
* Action Graph semantics
* Action Contract authority
* external business-state authority

Instead, it provides the engineering mechanisms required to preserve those boundaries when execution encounters failure, uncertainty, interruption, or partial completion.

The canonical relationship is:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Action Graph
   ↓
Action Contract
   ↓
Execution
   ↓
Failure / Success / Unknown
   ↓
Recovery
   ↓
Outcome

The central principle is:

A failure must produce an explicit state transition, not an implicit continuation.

⸻

2. Purpose

Noema operates across distributed systems in which:

* external systems may fail
* network communication may fail
* processes may terminate
* execution may be interrupted
* dependencies may become unavailable
* business state may change
* an external operation may succeed even when its response is lost
* retries may produce duplicate effects
* Actions may partially complete
* recovery itself may fail

Failure Recovery exists to ensure that these conditions do not cause Noema to:

* silently assume success
* silently assume failure
* execute unauthorized Actions
* bypass Action Contracts
* mutate an Intent without explicit transition
* repeat non-idempotent Actions unsafely
* conceal partial execution
* lose execution history
* convert unknown outcomes into deterministic outcomes without evidence

⸻

3. Core Principle

Noema must distinguish:

SUCCESS
FAILED
UNKNOWN
BLOCKED
WAITING
CANCELLED

These states have different meanings.

In particular:

UNKNOWN ≠ FAILED
UNKNOWN ≠ SUCCESS

An uncertain external result must remain uncertain until authoritative evidence establishes the outcome or a defined recovery policy establishes a safe terminal interpretation.

⸻

4. Failure Is Not a Single State

Failure Recovery must distinguish at least:

1. Action failure
2. Dependency failure
3. Execution interruption
4. Infrastructure failure
5. Contract violation
6. Authorization failure
7. External business-state rejection
8. Timeout
9. Unknown execution outcome
10. Recovery failure
11. Graph invalidation
12. Trust invalidation
13. Human intervention requirement

These failures may have different recovery semantics.

A generic:

ERROR

is insufficient as the canonical execution state.

⸻

5. Failure Domains

Failures should be classified according to the layer in which they occur.

Conceptually:

Intent Layer
    ↓
Validation Layer
    ↓
Trust Layer
    ↓
Graph Layer
    ↓
Contract Layer
    ↓
Execution Layer
    ↓
External System

A failure in one layer must not automatically be interpreted as a failure in another.

For example:

Execution FAILED

does not imply:

Trust INVALID

Similarly:

External system unavailable

does not imply:

Intent invalid

⸻

6. Failure Classification

A failure should be represented with machine-readable semantics.

Conceptually:

Failure {
    failure_id
    category
    code
    severity
    action_id
    graph_id
    contract_id
    retryability
    recoverability
    certainty
    cause
    evidence
    timestamp
    provenance
}

The exact schema belongs to the relevant engineering and execution specifications.

⸻

7. Failure Categories

Canonical failure categories may include:

VALIDATION_FAILURE
TRUST_FAILURE
GRAPH_FAILURE
CONTRACT_FAILURE
AUTHORIZATION_FAILURE
PRECONDITION_FAILURE
DEPENDENCY_FAILURE
EXECUTION_FAILURE
TIMEOUT
NETWORK_FAILURE
RESOURCE_FAILURE
EXTERNAL_REJECTION
UNKNOWN_OUTCOME
CANCELLATION
EXPIRATION
RECOVERY_FAILURE

The taxonomy may evolve.

The important requirement is that materially different failure semantics remain distinguishable.

⸻

8. Failure Severity

Failure severity may be represented separately from failure type.

Possible levels include:

INFO
WARNING
ERROR
CRITICAL

Severity describes operational significance.

It does not determine whether an Action is retryable.

For example:

ERROR + RETRYABLE

and:

ERROR + NON_RETRYABLE

are both valid.

⸻

9. Retryability

Retryability must be explicit.

Conceptually:

RETRYABLE
NON_RETRYABLE
UNKNOWN

A failure must not be retried merely because the operation failed.

Retryability must be determined from:

* Action Contract
* failure class
* idempotency semantics
* external system behavior
* retry policy
* execution state

⸻

10. Recoverability

Recoverability is distinct from retryability.

An Action may be:

not retryable
but recoverable

For example:

Payment request
     ↓
Unknown outcome
     ↓
Query payment status
     ↓
Determine authoritative result

The original Action is not necessarily retried.

Instead, recovery establishes its outcome.

Therefore:

Retry ≠ Recovery

⸻

11. Failure State

An Action may transition through states such as:

NOT_READY
READY
EXECUTING
COMPLETED
FAILED
WAITING
BLOCKED
SKIPPED
UNKNOWN
CANCELLED

Failure Recovery must respect the canonical Action Graph state model.

It must not invent a new state merely because recovery is required.

Recovery may be represented through explicit events and transitions.

⸻

12. Failure State vs Trust State

Failure state must remain separate from Trust state.

Example:

Trust:
READY
Execution:
FAILED

is valid.

The execution failure does not automatically invalidate the prior Trust decision.

However, a material change may require Trust re-evaluation.

For example:

Execution failure
       ↓
Material condition changed
       ↓
Trust re-evaluation

⸻

13. Failure State vs Intent State

Failure must also remain distinct from Intent lifecycle.

For example:

Intent:
RESOLVED
Action:
FAILED

does not necessarily mean:

Intent:
INVALID

The Intent remains the semantic representation of what the Actor intended.

The execution result records what occurred while attempting to fulfill it.

⸻

14. Deterministic Failure Handling

Given:

Failure
+
Action Contract
+
Action Graph
+
Execution Policy
+
Current State

the recovery behavior should be deterministic where the governing rules are deterministic.

A model must not invent recovery behavior at execution time.

For example:

Action FAILED

must not cause an LLM to decide:

“I think we should retry.”

Retry semantics must already be established by the applicable engineering and contract rules.

⸻

15. Failure Event

Failures should be represented as explicit events.

Examples:

action.failed
action.timeout
action.unknown
action.blocked
action.retry_scheduled
action.retry_started
action.retry_exhausted
recovery.started
recovery.completed
recovery.failed
execution.interrupted
graph.invalidated
graph.revalidated

Events must be durable and auditable where they affect execution state.

⸻

16. Failure Event Provenance

A failure event should preserve sufficient provenance to reconstruct what happened.

Conceptually:

FailureEvent {
    event_id
    action_id
    graph_id
    execution_id
    failure_code
    previous_state
    resulting_state
    contract_version
    capability
    timestamp
    attempt
    evidence
    source
}

The system must not require hidden model reasoning to reconstruct execution history.

⸻

17. Failure Detection

Failure may be detected through:

* explicit external rejection
* Action Contract violation
* timeout
* connection failure
* process termination
* dependency failure
* invalid response
* failed postcondition
* authorization rejection
* resource exhaustion
* explicit cancellation
* recovery timeout
* authoritative external status

Failure detection must not depend solely on transport-level errors.

An HTTP success response, for example, does not by itself establish successful business execution.

⸻

18. Postcondition Failure

An Action may return a technically successful response while failing to establish its expected postcondition.

Example:

REQUEST_REPLACEMENT
       ↓
response = accepted
       ↓
expected postcondition:
replacement_request.status = CREATED
       ↓
verification:
status = UNKNOWN

The Action must not automatically be recorded as fully completed merely because the transport operation succeeded.

Postcondition semantics belong to the Action Contract and execution architecture.

⸻

19. Timeout

Timeout is not inherently equivalent to failure.

For example:

REQUEST_PAYMENT
       ↓
timeout

may mean:

request definitely failed

or:

request may have succeeded

Therefore timeout handling must classify the resulting certainty.

Possible outcomes:

FAILED
UNKNOWN

depending on available evidence.

⸻

20. Unknown Outcome

An unknown outcome occurs when Noema cannot establish whether an external operation completed.

Example:

CREATE_PAYMENT
      ↓
request sent
      ↓
network connection lost
      ↓
response unavailable

The correct state may be:

UNKNOWN

rather than:

FAILED

Noema must preserve the uncertainty.

⸻

21. Unknown Outcome Recovery

Unknown outcomes should use an explicit recovery strategy where supported.

Examples:

Query authoritative operation status

or:

Reconcile external state

or:

Request human intervention

The recovery strategy must be defined by the applicable Action Contract or execution policy.

⸻

22. Never Retry Unknown Effects Blindly

An unknown outcome must not automatically trigger a duplicate operation.

For example:

CREATE_PAYMENT
       ↓
UNKNOWN
       ↓
CREATE_PAYMENT again

may create two payments.

Instead:

CREATE_PAYMENT
       ↓
UNKNOWN
       ↓
QUERY_PAYMENT_STATUS
       ↓
AUTHORITATIVE RESULT

should be preferred when the external system supports such reconciliation.

⸻

23. Idempotency

Retry safety depends on idempotency semantics.

An Action Contract should define, where relevant:

* idempotency key
* idempotency scope
* deduplication semantics
* replay behavior
* duplicate detection
* uncertainty handling

Noema must not assume that repeating an Action is safe merely because the Action appears deterministic.

⸻

24. Retry Policy

Retry behavior should define:

max_attempts
backoff
retryable_failures
timeout
jitter
idempotency_requirements
termination_condition

Conceptually:

Action
  ↓
FAILED
  ↓
Retry policy?
  ├── NO → terminal failure
  └── YES
       ↓
attempt < maximum?
  ├── NO → retry exhausted
  └── YES
       ↓
retry

Retries must be bounded.

⸻

25. Retry Exhaustion

When retry limits are reached:

FAILED
   ↓
RETRY_EXHAUSTED

must not silently become:

SUCCESS

The graph must transition according to its defined failure policy.

Possible results include:

FAILED
BLOCKED
ESCALATED
WAITING
UNKNOWN

depending on the Action semantics.

⸻

26. Backoff

Retries should respect an explicit backoff strategy where appropriate.

Backoff may be required to:

* prevent load amplification
* respect provider limits
* allow transient faults to recover
* avoid synchronized retry storms

Backoff is an execution concern and must remain bounded by the applicable policy.

⸻

27. Retry Storm Prevention

Noema must avoid uncontrolled retry amplification.

Potential controls include:

* maximum attempts
* exponential backoff
* jitter
* concurrency limits
* circuit breaking
* provider rate limits
* graph-level retry budgets

Failure recovery must not transform a dependency outage into a larger distributed-system failure.

⸻

28. Dependency Failure

An Action may fail because a required dependency has failed.

Example:

A → B → C
A = COMPLETED
B = FAILED
C = BLOCKED

C must not execute unless the graph defines a valid recovery path that restores its prerequisites.

⸻

29. Failure Propagation

Failure propagation must follow explicit dependency semantics.

A failed node may cause downstream nodes to become:

BLOCKED
SKIPPED
WAITING

depending on graph policy.

Failure must not propagate indiscriminately to unrelated independent branches.

⸻

30. Independent Branches

Consider:

        ┌── B
A ──────┤
        └── C

If:

B = FAILED

C may remain executable if:

* C is independent of B
* partial execution is permitted
* the graph’s atomicity rules permit it
* Trust and Contract requirements remain satisfied

Graph topology alone does not determine whether partial execution is permitted.

⸻

31. Atomicity

Failure recovery must respect Intent and graph atomicity semantics.

If an Intent requires atomic treatment:

A
B
C

and:

B = FAILED

Noema must not continue with A or C merely because they remain individually executable.

The applicable atomicity policy governs whether execution may continue.

⸻

32. Partial Execution

Partial execution must be explicit.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The resulting execution must preserve all four states.

It must not be collapsed into:

FAILED

without retaining the underlying action-level history.

⸻

33. Compensation

Compensation may be required after partial execution.

Example:

A → B → C
C fails
Compensation:
B_compensate
A_compensate

Compensation must be explicitly defined.

Noema must not assume that every Action has a compensating operation.

⸻

34. Compensation Is Not Rollback

External systems may not support transactional rollback.

Therefore:

Compensation ≠ Rollback

A compensating Action may produce a new business operation that attempts to mitigate an earlier operation.

Its result must be recorded independently.

⸻

35. Compensation Failure

Compensation may itself fail.

Example:

A completed
B completed
C failed
   ↓
Compensate B
   ↓
FAILED

The system must preserve:

* original failure
* compensation attempt
* compensation result
* remaining unresolved state

Recovery failure must never overwrite the original execution history.

⸻

36. Recovery Is Its Own Execution

A recovery Action is an Action.

It must therefore be subject to:

* Action identity
* Action Contract
* capability requirements
* authorization
* Trust requirements
* execution state
* failure semantics
* provenance

Recovery must not become an authority bypass.

⸻

37. No Recovery Bypass

Noema must not implement:

Action failed
    ↓
Emergency tool call
    ↓
Execute arbitrary operation

Instead:

Failure
   ↓
Defined Recovery Policy
   ↓
Recovery Action
   ↓
Action Contract
   ↓
Execution

The recovery path remains inside the canonical execution boundary.

⸻

38. Recovery Planning

Recovery may require constructing a recovery graph.

Conceptually:

Original Graph
      ↓
Failure
      ↓
Recovery Evaluation
      ↓
Recovery Graph
      ↓
Validation
      ↓
Trust / Contract checks
      ↓
Recovery Execution

A recovery graph is not automatically trusted merely because the original graph was trusted.

⸻

39. Recovery and Trust

A recovery operation may introduce new execution consequences.

Therefore:

Original Trust

does not automatically authorize every possible recovery Action.

A recovery Action may require:

* new Trust evaluation
* additional authorization
* additional approval
* updated policy evaluation
* new Action Contract binding

depending on its semantics.

⸻

40. Recovery and Material Change

If recovery changes the intended execution semantics materially, the relevant graph or Intent state must be explicitly revised.

For example:

Original Intent:
Transfer ₦100,000 to Account A

must not silently become:

Transfer ₦100,000 to Account B

merely because Account A became unavailable.

That would be semantic mutation, not failure recovery.

⸻

41. Recovery vs Replanning

These concepts must remain distinct.

Recovery addresses failure within the execution of an established objective.

Replanning determines a new execution structure because circumstances changed.

For example:

Email provider unavailable

may result in:

Replan:
Use permitted SMS capability

if the Intent permits that alternative.

The change must be governed by explicit graph-selection semantics.

⸻

42. Recovery and Alternative Capabilities

An alternative capability may be used only when the Intent and applicable policies permit it.

Example:

Notify customer
Email unavailable
       ↓
SMS capability available

Noema must not automatically substitute SMS merely because email failed.

The selection criteria must be explicit.

⸻

43. Graph Invalidation

A failure may invalidate the current Action Graph.

Examples:

* capability revoked
* Action Contract changed materially
* required dependency disappears
* authorization changes
* policy changes
* external state changes materially

The graph must then undergo explicit revalidation.

⸻

44. Stale Graph

A graph may be valid at:

T1

and no longer valid at:

T2

Noema must not silently continue execution against materially stale assumptions.

Conceptually:

Graph
 ↓
Material Change
 ↓
Invalidation
 ↓
Revalidation
 ↓
Graph Revision

⸻

45. Process Interruption

Execution may be interrupted by:

* process termination
* machine failure
* deployment
* container restart
* worker loss
* network partition
* scheduler failure

The system must recover from interruption without assuming that an interrupted Action did or did not execute.

⸻

46. Durable Execution State

Execution state required for recovery must be durably persisted.

At minimum, the system should be able to reconstruct:

* Intent identity/version
* graph identity/version
* Action identity
* execution identity
* attempt number
* Action state
* dependency state
* contract version
* relevant failure
* timestamps
* recovery history
* outcome status

In-memory state must not be the sole source of truth for durable execution.

⸻

47. Checkpointing

Long-running executions should persist sufficient state to resume safely.

A checkpoint may contain:

execution_id
graph_version
completed_nodes
active_nodes
pending_nodes
failed_nodes
unknown_nodes
retry_state
recovery_state

Checkpoint semantics must prevent an execution from resuming with an inconsistent graph state.

⸻

48. Resume Semantics

After interruption:

Execution interrupted
       ↓
Recover durable state
       ↓
Determine last known state
       ↓
Reconcile uncertain Actions
       ↓
Resume according to graph

Noema must not simply restart the entire graph from the beginning unless the graph and Action Contracts explicitly permit that behavior.

⸻

49. Duplicate Execution Prevention

Recovery must guard against duplicate execution.

Example:

Worker A:
Action sent
Worker A:
process dies
Worker B:
does not know whether Action executed

Worker B must not blindly repeat a non-idempotent Action.

The execution architecture should use appropriate mechanisms such as:

* idempotency keys
* durable execution records
* leases
* fencing
* provider-side deduplication
* authoritative reconciliation

as applicable.

⸻

50. Lease and Ownership Semantics

Where execution workers claim Actions, ownership should be explicit.

A worker may hold an execution lease.

If the lease expires:

Worker A
   ↓
lease expired
   ↓
Worker B

Worker B must establish safe ownership before continuing.

Lease expiration does not itself prove that Worker A stopped executing.

⸻

51. Fencing

Where concurrent execution could create harmful duplicate effects, fencing mechanisms may be required.

The objective is:

Only the current execution owner may perform the permitted operation.

Fencing is an implementation concern, but it is necessary where stale workers could otherwise continue executing consequential Actions.

⸻

52. External State Reconciliation

When internal execution state and external business state disagree, the external authoritative system remains authoritative for its business domain.

Example:

Noema:
PAYMENT = UNKNOWN
Provider:
PAYMENT = COMPLETED

Noema should reconcile its execution record with the authoritative provider evidence.

It should not invent a contradictory business state.

⸻

53. Reconciliation

Reconciliation may be used to resolve:

* unknown outcomes
* interrupted executions
* duplicate detection
* external state changes
* stale execution records
* postcondition uncertainty

A reconciliation operation must preserve evidence of the authoritative source.

⸻

54. Recovery from Unknown State

An Action in:

UNKNOWN

should remain unknown until:

1. authoritative evidence resolves the outcome,
2. a defined recovery process establishes a terminal state,
3. or an explicitly governed human decision resolves the condition.

The system must not convert:

UNKNOWN → FAILED

merely to simplify state management.

⸻

55. Human Intervention

Some failures cannot be safely resolved automatically.

The graph may transition to:

WAITING_FOR_HUMAN

or an equivalent explicit intervention state.

Human intervention should be distinguishable from failure.

Example:

Payment outcome unknown
       ↓
Human review required

is different from:

Payment failed

⸻

56. Human Intervention Is Governed

Human intervention does not bypass the execution model.

A human decision should produce an explicit event containing:

* decision identity
* decision type
* relevant scope
* timestamp
* authority context
* resulting transition
* provenance

The exact approval and governance semantics belong to the applicable Trust and execution specifications.

⸻

57. Cancellation During Failure

An Actor may cancel an Intent while recovery is in progress.

Cancellation must be handled explicitly.

For example:

Action FAILED
      ↓
Recovery pending
      ↓
Actor cancels Intent

The system must determine, according to the applicable semantics, whether:

* recovery should stop
* already-started Actions must continue
* compensation is required
* external reconciliation is required

Cancellation does not automatically undo external effects.

⸻

58. Failure During Cancellation

Cancellation itself may fail.

Example:

Cancel request
     ↓
external system unavailable

The cancellation state must remain explicit.

Noema must distinguish:

cancellation requested

from:

cancellation completed

⸻

59. Failure During Approval

Approval-dependent execution may encounter failure before or after approval.

Approval does not guarantee successful execution.

For example:

Approval granted
      ↓
Execution
      ↓
FAILED

The approval remains evidence that the governance condition was satisfied at that point.

It does not establish execution success.

⸻

60. Failure After Partial Completion

When some Actions have completed and another fails, Noema must preserve the exact execution boundary.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The system must not report:

Nothing happened.

Nor should it report:

Everything succeeded.

The Outcome must reflect partial execution.

⸻

61. Outcome Formation

Failure Recovery contributes evidence to the final Outcome.

Conceptually:

Action States
+
Failure Events
+
Recovery Events
+
Postcondition Evidence
+
External Evidence
      ↓
Outcome

Outcome formation remains distinct from Trust.

⸻

62. Outcome States

Execution-level outcomes may include:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN
CANCELLED

The exact canonical vocabulary should remain aligned with the broader Noema Outcome specification.

⸻

63. Failure Does Not Rewrite History

If:

Action A = COMPLETED
Action B = FAILED

and recovery later succeeds:

Recovery B = COMPLETED

the history must retain both events.

The system should not rewrite:

B FAILED

into:

B COMPLETED

without preserving the failure event and recovery transition.

⸻

64. Recovery History

Recovery history should record:

original failure
       ↓
recovery strategy
       ↓
recovery attempt
       ↓
recovery result
       ↓
resulting execution state

This allows operators and auditors to reconstruct how the final state was reached.

⸻

65. Recovery Limits

Recovery must be bounded.

A recovery process should define, where relevant:

* maximum attempts
* maximum duration
* maximum escalation depth
* retry budget
* compensation limits
* reconciliation timeout
* human intervention threshold

Noema must not enter an uncontrolled recovery loop.

⸻

66. Recovery Loops

The Action Graph already prohibits unrestricted cycles unless iteration is explicitly bounded.

The same principle applies to recovery.

Invalid:

failure
 ↓
recover
 ↓
failure
 ↓
recover
 ↓
...

without a bounded termination policy.

Valid recovery requires explicit:

attempt limit
timeout
termination condition
failure behavior

⸻

67. Recovery Ordering

Recovery Actions must respect dependencies.

Example:

A
↓
B
↓
C

If B fails and compensation requires:

C_compensate

that compensation cannot be performed merely because it exists.

Its prerequisites and current external state must be established.

Recovery is itself dependency-aware.

⸻

68. Recovery Preconditions

A recovery Action may have preconditions.

Example:

REFUND_PAYMENT
Preconditions:
    payment.status = SETTLED
    refund_not_already_issued = true

If the preconditions are not satisfied, the recovery Action must not execute.

⸻

69. Recovery Postconditions

Recovery Actions may define expected postconditions.

Example:

COMPENSATE_TRANSFER
Expected:
    compensation.status = COMPLETED

Postconditions should be verified where required.

An accepted request is not automatically equivalent to a verified business outcome.

⸻

70. Recovery and Idempotency

Recovery Actions may themselves be retried.

Therefore they require the same discipline as primary Actions:

Recovery Action
      ↓
Action Contract
      ↓
Idempotency
      ↓
Retry Policy
      ↓
Execution

Recovery must not introduce a second-order duplication problem.

⸻

71. Failure Cascades

One infrastructure failure may affect multiple Actions.

For example:

Payment provider unavailable
A → Payment
B → Payment
C → Payment

Noema should avoid independently retrying every failed Action without regard to shared dependency state.

System-level controls may include:

* dependency health state
* circuit breakers
* rate limits
* bounded retry budgets
* dependency-aware scheduling

⸻

72. Circuit Breaking

Where repeated dependency failures make continued execution unsafe or wasteful, the execution layer may temporarily prevent new calls to that dependency.

A circuit breaker must not alter the semantic Intent.

It changes execution availability.

For example:

Capability:
payment.create
State:
temporarily unavailable

may cause Actions to become:

BLOCKED

or:

WAITING

according to policy.

⸻

73. Backpressure

Failure recovery must account for system capacity.

Repeated failures can increase queue depth through retries.

Therefore execution systems may need:

* bounded queues
* concurrency limits
* retry budgets
* admission controls
* rate limits

Operational resilience must not compromise semantic correctness.

⸻

74. Resource Exhaustion

Resource exhaustion may include:

* CPU
* memory
* storage
* connection pools
* worker capacity
* provider quotas

Resource exhaustion should be distinguished from business rejection.

For example:

NO_WORKER_CAPACITY

is not equivalent to:

ACCOUNT_NOT_ELIGIBLE

Different recovery policies may apply.

⸻

75. Contract Failure

An Action may fail because the Action Contract cannot be satisfied.

Examples:

* required input missing
* capability mismatch
* contract version incompatible
* required precondition absent
* unsupported operation
* invalid response schema

These failures should generally prevent blind retries unless the contract explicitly permits recovery.

⸻

76. Authorization Failure

Authorization failure must remain distinct from technical failure.

Example:

TRANSFER_FUNDS
     ↓
AUTHORIZATION_DENIED

must not be treated as:

NETWORK_FAILURE

Retrying an authorization denial does not establish authorization.

A material authorization change may require Trust re-evaluation.

⸻

77. Business-State Rejection

An external system may reject an Action because current business state does not permit it.

Example:

RENEW_CARD
     ↓
card.status = BLOCKED
     ↓
external rejection

This is different from infrastructure failure.

The consumer remains authoritative for its business state.

⸻

78. Permanent vs Transient Failure

Failures may be classified as:

TRANSIENT
PERMANENT
UNKNOWN

Examples:

Transient:

temporary network outage
rate limit
temporary provider unavailability

Permanent:

unsupported operation
authorization denied
invalid account

Unknown:

external response unavailable

The classification must come from explicit semantics rather than model judgment.

⸻

79. Failure Escalation

A failure may escalate when automatic recovery is exhausted.

Conceptually:

Failure
  ↓
Retry
  ↓
Retry exhausted
  ↓
Reconciliation
  ↓
Still unresolved
  ↓
Escalation

Escalation may result in:

WAITING
BLOCKED
HUMAN_INTERVENTION
UNKNOWN
FAILED

according to the applicable policy.

⸻

80. Failure Notifications

Operational notifications may be generated when failures meet defined thresholds.

Notifications must not be confused with execution recovery.

For example:

Action failed
   ↓
operator notified

does not mean:

Action recovered

Notification is observability.

Recovery is execution state transition.

⸻

81. Failure Observability

Noema should expose sufficient operational information to determine:

* what failed
* where it failed
* when it failed
* which Action was executing
* which graph version was active
* which contract version applied
* which attempt failed
* whether the outcome was known
* what recovery occurred
* what remains unresolved

Observability must not require access to private model reasoning.

⸻

82. Failure Correlation

Failures should be correlatable across:

intent_id
graph_id
execution_id
action_id
attempt_id
recovery_id
event_id

This allows an operator to reconstruct an execution without relying on textual logs alone.

⸻

83. Structured Error Codes

Failure codes should be machine-readable.

Examples:

ACTION_PRECONDITION_FAILED
ACTION_TIMEOUT
ACTION_UNKNOWN_OUTCOME
CAPABILITY_UNAVAILABLE
CONTRACT_INVALID
AUTHORIZATION_DENIED
EXTERNAL_REJECTION
DEPENDENCY_FAILED
RETRY_EXHAUSTED
RECOVERY_FAILED
POSTCONDITION_UNVERIFIED
EXECUTION_INTERRUPTED
GRAPH_INVALIDATED

Human-readable descriptions may accompany them.

Codes remain canonical.

⸻

84. Error Information

Failure records should expose sufficient information for remediation while avoiding unnecessary sensitive data.

Errors should not require dumping:

* credentials
* secrets
* authentication tokens
* private payloads
* unnecessary personal data

into operational logs.

⸻

85. Recovery and Security

Failure recovery must preserve security boundaries.

A failure must not cause:

normal authorization
      ↓
failure
      ↓
privileged fallback

Recovery paths must operate under the same authority model.

A degraded mode must not become an authority escalation mechanism.

⸻

86. Recovery and Secrets

Recovery mechanisms must not persist sensitive credentials merely to make retries easier.

Credentials should remain governed by the applicable secret-management and capability architecture.

Execution records should reference credential context without unnecessarily storing secret material.

⸻

87. Recovery and Model Behavior

Models may assist with:

* explaining a failure
* summarizing operational state
* proposing candidate recovery strategies
* generating human-readable diagnostics

They must not autonomously override deterministic recovery controls.

For consequential recovery:

Model Proposal
      ↓
Deterministic Validation
      ↓
Policy / Trust / Contract Checks
      ↓
Execution

The model remains a proposal source rather than the authority.

⸻

88. No Hidden Recovery

A model must not silently perform additional recovery operations.

For example:

Payment failed

must not cause an undeclared:

Refund
Retry
Alternative payment
Account modification

unless those operations are represented by the applicable Action Graph and governed by their contracts.

⸻

89. Recovery Provenance

Recovery should record why it occurred.

Provenance may include:

* original failure
* failure code
* recovery policy
* selected recovery Action
* Action Contract
* capability
* graph version
* policy version
* evidence
* execution result
* operator intervention

This provides an auditable recovery chain.

⸻

90. Recovery Versioning

Recovery behavior may depend on versioned:

* Action Contracts
* policies
* graph rules
* retry policies
* reconciliation rules
* capability definitions

The versions applicable to a recovery event should be preserved.

⸻

91. Material Policy Change During Recovery

If recovery remains pending while a material policy changes, Noema must determine whether the existing recovery path remains valid.

It must not silently continue using stale governance assumptions.

Conceptually:

Recovery pending
       ↓
Policy changes materially
       ↓
Re-evaluation
       ↓
Continue / revise / block

⸻

92. Failure and Durable State

Every state transition required for recovery must be durably recorded before the system relies on that transition for subsequent execution.

The system must avoid:

memory:
Action = COMPLETED
database:
Action = EXECUTING

when a crash could cause duplicate execution.

The exact transaction and persistence model belongs to the execution architecture.

⸻

93. Atomic State Transitions

Where execution state and scheduling state must change together, the persistence mechanism should provide the required atomicity.

For example:

Action:
FAILED
and
Retry:
SCHEDULED

must not leave the system in an ambiguous state where the retry is both unscheduled and considered scheduled.

⸻

94. Exactly-Once Semantics

Noema should not assume that distributed execution automatically provides exactly-once effects.

The architecture should distinguish:

exactly-once processing

from:

exactly-once external effect

The latter generally depends on the external system and Action Contract.

Where exactly-once effects cannot be guaranteed, Noema must use explicit idempotency and reconciliation mechanisms.

⸻

95. At-Least-Once Execution

Execution infrastructure may use at-least-once delivery or retry semantics.

If so, Action Contracts must define how duplicate delivery is handled.

For example:

event delivered twice

must not necessarily imply:

business operation executed twice

when idempotency semantics are correctly established.

⸻

96. At-Most-Once Execution

At-most-once processing may reduce duplicate execution but may increase the possibility of lost work.

Therefore the engineering choice must be explicit.

Noema must not claim a stronger execution guarantee than the underlying system can provide.

⸻

97. Failure Recovery Guarantees

Noema should state execution guarantees precisely.

For example:

Durable state recovery:
YES
Duplicate external effect prevention:
ONLY WHERE CONTRACT / PROVIDER SUPPORTS IT
Unknown outcome resolution:
ONLY WHERE AUTHORITATIVE RECONCILIATION EXISTS
Automatic compensation:
ONLY WHERE EXPLICITLY DEFINED

The system must not represent engineering aspirations as execution guarantees.

⸻

98. Recovery Testing

Failure Recovery must be tested against realistic failure modes.

Tests should include:

* worker crash
* process restart
* network timeout
* provider timeout
* provider rejection
* duplicate response
* lost response
* duplicate request
* dependency outage
* capability disappearance
* contract mismatch
* authorization change
* partial graph execution
* compensation failure
* retry exhaustion
* stale worker
* concurrent recovery
* unknown external state

⸻

99. Fault Injection

The engineering system should support controlled fault injection where appropriate.

Examples:

force timeout
drop response
terminate worker
delay dependency
return external rejection
corrupt intermediate state

The purpose is to verify that failure semantics are implemented rather than merely documented.

⸻

100. Recovery Invariants

Invariant 1

Failure must be represented explicitly.

Invariant 2

Unknown outcome must not silently become success or failure.

Invariant 3

Retryability must be explicit.

Invariant 4

Retries must be bounded.

Invariant 5

Retries must respect idempotency semantics.

Invariant 6

Recovery Actions remain subject to Action Contracts.

Invariant 7

Recovery must not bypass Trust or authorization.

Invariant 8

Partial execution must remain explicitly represented.

Invariant 9

Compensation is not equivalent to rollback.

Invariant 10

Recovery failure must not erase the original failure.

Invariant 11

External business systems remain authoritative for their business state.

Invariant 12

A stale graph must not silently continue across a material change.

Invariant 13

Interrupted execution must be recoverable from durable state.

Invariant 14

Unknown external effects must not be blindly repeated.

Invariant 15

Recovery loops must be bounded.

Invariant 16

Recovery must not mutate Intent semantics silently.

Invariant 17

Recovery history must be auditable.

Invariant 18

Execution failure does not automatically invalidate Trust.

Invariant 19

Model-generated recovery proposals are not execution authority.

Invariant 20

No recovery mechanism may become an authority-escalation mechanism.

⸻

101. Canonical Failure Recovery Flow

The canonical lifecycle is:

Action Execution
      ↓
Result
      │
      ├─────────────── SUCCESS
      │                  ↓
      │               Continue
      │
      ├─────────────── FAILURE
      │                  ↓
      │            Classify Failure
      │                  ↓
      │          Recovery Policy
      │             │         │
      │             │         └── No Recovery
      │             │                 ↓
      │             │              FAILED
      │             │
      │             └── Recovery Required
      │                     ↓
      │               Recovery Action
      │                     ↓
      │                Contract Checks
      │                     ↓
      │                  Execute
      │
      └─────────────── UNKNOWN
                         ↓
                  Reconciliation
                    │        │
                    │        └── Cannot Resolve
                    │                ↓
                    │             UNKNOWN
                    │
                    └── Authoritative Result
                              ↓
                         Continue / Failed

⸻

102. Canonical Recovery Lifecycle

The engineering lifecycle can be reduced to:

Detect
   ↓
Classify
   ↓
Persist
   ↓
Contain
   ↓
Determine Recoverability
   ↓
Retry / Reconcile / Compensate / Escalate
   ↓
Verify
   ↓
Resume / Block / Fail / Complete
   ↓
Record Outcome

Each transition must have explicit semantics.

⸻

103. Recovery Decision Model

For a failed Action, Noema should determine:

1. What failed?
2. Is the failure known or uncertain?
3. Did the external operation possibly occur?
4. Is retry permitted?
5. Is the Action idempotent or deduplicated?
6. Is reconciliation available?
7. Is compensation defined?
8. Does the graph permit continuation?
9. Does recovery require new authorization or Trust evaluation?
10. What terminal state is permitted if recovery cannot resolve the failure?

These questions should be answered through explicit system semantics rather than ad hoc model behavior.

⸻

104. Recovery and Action Graph

The Action Graph remains the canonical representation of execution relationships.

Failure changes node and dependency state.

For example:

A
↓
B
↓
C

If:

B = FAILED

then:

C = BLOCKED

unless the graph defines a recovery or alternative path.

Recovery does not bypass graph semantics.

⸻

105. Recovery and Durable Execution

Durable execution provides the engineering substrate for preserving execution state across interruptions.

Failure Recovery defines what the system does with that durable state.

Conceptually:

Action Graph
      ↓
Durable Execution
      ↓
Failure
      ↓
Durable Failure State
      ↓
Recovery
      ↓
Resumption / Terminal Outcome

The two concerns are related but distinct.

⸻

106. Recovery and Outcome

Outcome records what actually happened.

Failure Recovery provides the mechanisms necessary to establish that result.

Therefore:

Recovery
   ↓
Evidence
   ↓
Outcome

Outcome must not merely report what the system intended to happen.

It must represent what execution established.

⸻

107. Final Definition

Failure Recovery is Noema’s engineering discipline for handling execution failure, uncertainty, interruption, partial completion, retry, reconciliation, compensation, escalation, and recovery while preserving the semantic and authority boundaries of the Noema architecture.

Its central invariant is:

Noema must never convert execution uncertainty into certainty merely to continue processing.

The canonical model is:

Failure
   ↓
Explicit State
   ↓
Deterministic Recovery Policy
   ↓
Bounded Recovery
   ↓
Verification
   ↓
Explicit Outcome

And the fundamental boundary remains:

Intent defines what the Actor wants.
Trust determines whether execution may proceed.
Action Graph defines execution structure.
Action Contracts define executable obligations.
Execution performs permitted Actions.
Failure Recovery determines how execution responds when reality diverges from expectation.
Outcome records what was actually established.