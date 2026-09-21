Reliability

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/reliability.md

⸻

1. Definition

Reliability is Noema’s engineering discipline for ensuring that Intent processing, Trust evaluation, Action Graph construction, Action Contract execution, and Outcome recording behave predictably under failure, interruption, delay, duplication, partial completion, external-system instability, and changing conditions.

Reliability does not mean that execution always succeeds.

Reliability means that Noema preserves its architectural guarantees when execution does not proceed normally.

The central reliability objective is:

Noema must fail explicitly, recover deliberately, preserve state and provenance, and never convert uncertainty or partial execution into false success.

The canonical relationship is:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Action Graph
   ↓
Action Contracts
   ↓
Execution
   ↓
Outcome

Reliability applies across the entire lifecycle.

⸻

2. Core Principle

Noema must be designed on the assumption that failure is normal.

Failures may occur because of:

* process termination
* machine failure
* network interruption
* provider failure
* timeout
* duplicate delivery
* delayed response
* unavailable capability
* stale external state
* contract violation
* authorization change
* policy change
* dependency failure
* partial execution
* unknown execution outcome
* infrastructure degradation
* human intervention

The engineering system must therefore preserve correctness without assuming uninterrupted execution.

The principle is:

Failure is an expected system condition.
Undefined failure behavior is an architectural defect.

⸻

3. Reliability vs Availability

Reliability and availability are related but distinct.

Availability concerns whether a system is accessible and able to respond.

Reliability concerns whether the system behaves correctly over time, including when components fail.

A system may be:

Available
but unreliable

if it produces incorrect outcomes.

Likewise:

Temporarily unavailable
but reliable

if it preserves state and resumes correctly after recovery.

Noema prioritizes preservation of semantic, trust, execution, and outcome correctness over superficial availability.

⸻

4. Reliability Boundary

Reliability spans the architectural boundaries:

Actor
  ↓
Intent Engine
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Action Contract
  ↓
Execution Consumer
  ↓
External System
  ↓
Outcome

Each boundary introduces possible failure.

Noema must distinguish:

Noema failure
External system failure
Network failure
Unknown outcome
Semantic failure
Trust failure
Contract failure
Execution failure

These must not be collapsed into a generic FAILED state when doing so would destroy meaningful information.

⸻

5. Reliability Invariants

Noema reliability is governed by the following invariants.

Invariant 1

A failure must not silently become success.

Invariant 2

An unknown execution result must not silently become failure or success.

Invariant 3

Retries must respect Action Contract semantics.

Invariant 4

Retries must not create unintended duplicate consequential Actions.

Invariant 5

Partial execution must remain explicitly represented.

Invariant 6

Recovery must preserve provenance and execution history.

Invariant 7

A process restart must not require reconstructing execution state from memory.

Invariant 8

External systems remain authoritative for their business state.

Invariant 9

Recovery must not bypass Trust, authorization, policy, or Action Contract requirements.

Invariant 10

A stale Action Graph must not silently resume execution after a material change.

Invariant 11

Every consequential execution must have an identifiable execution identity.

Invariant 12

Reliability mechanisms must not alter Intent semantics.

Invariant 13

A system must not claim completion until the applicable completion conditions are satisfied.

Invariant 14

Recovery behavior must be deterministic where the applicable semantics require determinism.

Invariant 15

Noema must preserve enough durable state to reconstruct what happened.

⸻

6. Reliability Model

The reliability model can be represented as:

Detect
  ↓
Persist
  ↓
Classify
  ↓
Contain
  ↓
Recover
  ↓
Verify
  ↓
Record Outcome

Reliability is therefore not merely retry logic.

It includes:

* state durability
* failure classification
* idempotency
* timeout handling
* retry policy
* compensation
* reconciliation
* recovery
* observability
* invariant enforcement
* outcome verification

⸻

7. Durable State

Any state required to resume or reconstruct execution must be durable.

Noema must not rely on:

* process memory
* temporary variables
* model context
* ephemeral worker state
* undocumented execution history

as the authoritative source of execution state.

At minimum, durable execution state should permit reconstruction of:

* Intent identity
* Intent version
* Trust state
* Action Graph version
* Action identity
* Action Contract identity/version
* execution identity
* node state
* dependency state
* attempt count
* retry state
* external references
* outcome state
* failure information
* timestamps
* provenance

⸻

8. Restart Safety

A process may terminate at any point.

Examples:

before execution
during execution
after request submission
before response receipt
after response receipt
before outcome persistence
after outcome persistence

The system must therefore define recovery semantics for each relevant boundary.

A restart must not cause Noema to assume:

nothing happened

merely because the local process no longer remembers what happened.

⸻

9. Execution Identity

Every consequential Action execution should have an explicit execution identity.

Conceptually:

execution_id

This identity distinguishes:

Action

from:

Attempt to execute Action

For example:

Action:
CREATE_PAYMENT
Execution:
exec_123
Attempt 1
Attempt 2
Attempt 3

The Action remains the semantic operation.

The execution identity tracks its operational lifecycle.

⸻

10. Attempt Identity

Where external systems support idempotency or request correlation, each execution attempt should have an explicit attempt identity.

Conceptually:

execution_id
    ↓
attempt_id
    ↓
external_request_id

This supports:

* duplicate detection
* reconciliation
* provider correlation
* incident investigation
* retry analysis

The exact identity model belongs to the execution and idempotency specifications.

⸻

11. Failure Classification

Failures should be classified according to their semantics.

Possible classes include:

VALIDATION_FAILURE
TRUST_FAILURE
DEPENDENCY_FAILURE
CAPABILITY_FAILURE
CONTRACT_FAILURE
AUTHORIZATION_FAILURE
TIMEOUT
NETWORK_FAILURE
PROVIDER_FAILURE
RATE_LIMIT
RESOURCE_UNAVAILABLE
CONFLICT
STALE_STATE
UNKNOWN_OUTCOME
INTERNAL_FAILURE
HUMAN_INTERVENTION

The taxonomy may evolve.

The important requirement is that recovery behavior must depend on failure semantics rather than merely on the presence of an error.

⸻

12. Retryable vs Non-Retryable Failure

A failure must not automatically imply retry.

Conceptually:

Failure
   ↓
Classify
   ↓
Retryable?
 ┌─┴─┐
Yes No
 │   │
Retry Stop/Recover

Retryability may depend on:

* failure class
* Action Contract
* idempotency
* provider semantics
* attempt count
* timeout
* resource state
* policy
* graph semantics

A generic retry loop is insufficient for consequential Actions.

⸻

13. Retry Boundaries

Retries must be bounded.

A retry policy may define:

maximum_attempts
maximum_elapsed_time
backoff
retryable_failures
termination_conditions

Noema must avoid unrestricted retries.

An indefinitely retrying Action can become:

* an execution loop
* a resource drain
* a duplicate-operation source
* an availability problem
* a violation of Actor expectations

⸻

14. Backoff

Where retries are permitted, backoff may reduce pressure on unstable external systems.

Possible strategies include:

fixed delay
exponential backoff
bounded exponential backoff
provider-directed retry delay

The exact strategy belongs to the applicable execution policy and Action Contract.

Backoff must not alter semantic execution state.

⸻

15. Idempotency

Idempotency is a core reliability property for consequential Actions.

A retry after an uncertain response must not unintentionally perform the same consequential operation multiple times.

For example:

CREATE_PAYMENT
      ↓
request submitted
      ↓
network timeout
      ↓
result unknown

Noema must not simply issue:

CREATE_PAYMENT

again without considering whether the original request may have succeeded.

Idempotency requirements are defined more specifically in engineering/idempotency.md.

⸻

16. Unknown Outcomes

Unknown outcome is a first-class reliability condition.

Example:

Noema → Provider
          ↓
       request
          ↓
      network loss
          ↓
      no response

The correct state may be:

UNKNOWN

rather than:

FAILED

The system may need to:

* reconcile with the provider
* query authoritative state
* await provider confirmation
* escalate
* require human review
* terminate with an explicitly unknown outcome

The key invariant is:

No response ≠ operation failed

⸻

17. Timeout Semantics

A timeout indicates that a response was not received within the permitted period.

It does not necessarily indicate that the external Action was not performed.

Therefore:

TIMEOUT

must be distinguished from:

DEFINITIVE_FAILURE

and:

UNKNOWN_OUTCOME

depending on the external system semantics.

Timeout handling must be defined at the Action Contract and execution layers.

⸻

18. Failure Propagation

Failures propagate through graph dependencies according to explicit semantics.

Example:

A
↓
B
↓
C

If:

B = FAILED

then:

C

must not execute unless the Action Graph explicitly defines a valid path allowing it.

Failure propagation must respect:

* dependency type
* branch conditions
* recovery policy
* compensation semantics
* partial-execution rules

⸻

19. Failure Isolation

Independent Actions should not necessarily fail merely because another unrelated Action failed.

Example:

       ┌── A ──┐
START ─┤       ├── D
       └── B ──┘

If A fails while B remains independently executable, the graph semantics determine whether B may continue.

Reliability must preserve the explicit dependency structure rather than applying a global failure rule.

⸻

20. Partial Execution

Noema must support partial execution explicitly.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The system must preserve the distinction between:

* completed
* failed
* blocked
* skipped
* waiting
* unknown
* not started

Partial execution must not be represented as:

SUCCESS

unless the defined completion conditions explicitly permit that result.

⸻

21. Recovery

Recovery is the process of returning an interrupted or failed execution to a defined state.

Possible recovery outcomes include:

RESUME
RETRY
WAIT
RECONCILE
COMPENSATE
ESCALATE
BLOCK
CANCEL
FAIL

Recovery behavior must be determined by explicit semantics.

A model must not invent recovery behavior at runtime for consequential Actions.

⸻

22. Resume

Resume is appropriate when durable state establishes that execution can safely continue.

Example:

A = COMPLETED
B = EXECUTING
process terminated

After restart:

load durable state
      ↓
determine B state
      ↓
reconcile if necessary
      ↓
resume according to contract

Noema must not blindly restart B merely because B was previously marked EXECUTING.

The external system may already have received the request.

⸻

23. Reconciliation

Reconciliation determines external reality when local execution state is insufficient.

Example:

Local state:
UNKNOWN
Authoritative provider:
payment = CREATED

Noema can reconcile its local execution state with the authoritative business system.

The external system remains authoritative for its domain.

Reconciliation is therefore a critical reliability mechanism for distributed execution.

⸻

24. Recovery Must Preserve Authority Boundaries

Recovery must not become a mechanism for bypassing governance.

For example:

Trust = BLOCKED

must not become:

Recovery → Execute anyway

Similarly:

Contract = INVALID

must not become:

Recovery → use previous contract

Recovery restores valid execution state.

It does not create authority.

⸻

25. Recovery After Material Change

Execution conditions may change while an Action is waiting.

Examples:

* capability revoked
* authorization changed
* policy changed
* Action Contract changed
* Intent changed
* external resource changed
* required dependency disappeared

The execution must be re-evaluated according to the applicable lifecycle.

Conceptually:

Interrupted Execution
        ↓
Material Change
        ↓
Revalidation
        ↓
Trust Re-evaluation
        ↓
Resume / Revise / Block

⸻

26. Stale Execution State

Persisted state can become stale.

For example:

Action = READY

does not guarantee that the Action remains executable after a long delay.

Before consequential execution, the applicable Action Contract may require final checks.

Reliability therefore includes freshness controls.

⸻

27. Heartbeats and Leases

Long-running execution may require explicit liveness mechanisms.

Possible mechanisms include:

heartbeat
lease
visibility timeout
execution ownership
worker registration

A lease may establish that a worker currently owns execution responsibility.

Lease expiration must not automatically imply that the Action failed.

The system may need reconciliation before another worker resumes the Action.

⸻

28. Worker Failure

If a worker terminates while executing an Action:

Worker A
   ↓
Action X
   ↓
Worker terminates

Noema must determine whether:

* the Action never started
* the Action may have started
* the Action completed
* the outcome is unknown

The recovery decision must be based on durable state and authoritative evidence.

⸻

29. Duplicate Workers

Distributed execution may result in multiple workers attempting the same Action.

Reliability mechanisms must prevent unintended duplicate consequential execution through mechanisms such as:

* execution ownership
* leases
* idempotency keys
* compare-and-set state transitions
* durable locks where appropriate
* provider-side deduplication

The exact mechanism depends on the Action Contract and infrastructure.

⸻

30. Concurrency

Independent graph nodes may execute concurrently when permitted.

Reliability must preserve:

* dependency correctness
* resource constraints
* ordering requirements
* idempotency
* atomicity
* external-system limits

Parallelism must therefore be explicit and controlled.

⸻

31. Concurrency Conflicts

Two Actions may attempt to modify related external state.

Example:

Action A → Account
Action B → Account

If their effects conflict, the graph or Action Contracts must define the permitted relationship.

Noema must not assume that concurrent execution is safe merely because two nodes have no direct data dependency.

⸻

32. Resource Exhaustion

Reliability includes protection against resource exhaustion.

Relevant resources may include:

* workers
* memory
* CPU
* connection pools
* queues
* provider quotas
* database capacity
* external API limits

A reliability mechanism must not convert an external failure into uncontrolled internal resource consumption.

Examples include:

bounded queues
bounded retries
timeouts
concurrency limits
rate limits
backpressure

⸻

33. Backpressure

When downstream capacity is constrained, upstream work may need to slow or stop.

Conceptually:

Producer
   ↓
Queue
   ↓
Consumer capacity exhausted
   ↓
Backpressure

Backpressure prevents transient overload from becoming systemic failure.

Backpressure may result in:

WAITING
DEFERRED
BLOCKED

rather than failure.

⸻

34. Dependency Failure

An Action may depend on an unavailable capability or service.

Example:

Action Graph
     ↓
Payment Capability
     ↓
Unavailable

The system must distinguish:

temporarily unavailable
permanently unavailable
unknown availability

Recovery behavior should depend on the classification.

⸻

35. External Provider Failure

External systems may fail independently of Noema.

Examples:

* HTTP 5xx
* service unavailable
* provider timeout
* provider maintenance
* malformed response
* provider rejection
* rate limit

Noema must preserve the provider response and classify it according to the Action Contract.

External failure does not necessarily imply a Noema architectural failure.

⸻

36. Provider Rejection

A provider may explicitly reject an Action.

Example:

Noema:
Action permitted
Provider:
Action rejected because account is suspended

This is an execution-time business-state result.

The provider remains authoritative for the relevant external state.

Noema must record the rejection rather than attempting to override it.

⸻

37. Contract Failure

An Action Contract may become invalid or fail its obligations.

Examples:

* required field missing
* unsupported operation
* schema mismatch
* contract version mismatch
* precondition failure
* response violates contract

Contract failures must prevent unsafe execution or downstream interpretation.

⸻

38. Schema and Protocol Failure

External responses may not conform to expected schemas.

Noema must not silently interpret malformed data as valid Action output.

Conceptually:

Response
   ↓
Contract validation
   ↓
Invalid

The resulting state may be:

CONTRACT_FAILURE

or another explicitly defined failure class.

⸻

39. Poisoned Work

A repeatedly failing Action can become a persistent source of failure.

Example:

Retry
 ↓
Failure
 ↓
Retry
 ↓
Failure
 ↓
Retry

Noema must use bounded retries and terminal failure states to prevent a poisoned Action from continuously consuming resources.

Such Actions may require:

ESCALATION
HUMAN_REVIEW
MANUAL_RECONCILIATION

⸻

40. Dead-Letter Handling

Where asynchronous execution is used, unrecoverable messages or execution records may require dead-letter handling.

A dead-letter state must preserve:

* original execution identity
* Action identity
* graph identity
* failure classification
* attempts
* timestamps
* relevant provider references
* recovery history

Dead-lettering must not mean deletion.

It means:

automated processing terminated

with state retained for investigation or controlled recovery.

⸻

41. Cancellation

An execution may be cancelled.

Cancellation must distinguish:

not started
running
already submitted externally
completed
unknown

If an external Action has already been submitted, local cancellation does not necessarily cancel the external operation.

The resulting state must reflect actual execution semantics.

⸻

42. Compensation

When an already completed Action cannot simply be undone, a compensating Action may be required.

Example:

A → B → C
       ↓
       C fails
Compensation:
B_compensate
A_compensate

Compensation must not be assumed equivalent to rollback.

External systems may not provide transactional rollback.

Compensation therefore requires explicit semantics and observability.

⸻

43. Compensation Failure

Compensation itself may fail.

Example:

Original Action
      ↓
Completed
      ↓
Failure elsewhere
      ↓
Compensation
      ↓
FAILED

Noema must preserve the resulting state.

It must not report that the original operation was rolled back merely because compensation was attempted.

Possible outcomes include:

COMPENSATION_REQUIRED
COMPENSATION_IN_PROGRESS
COMPENSATION_FAILED
PARTIALLY_COMPENSATED

The exact taxonomy belongs to the execution model.

⸻

44. Recovery Must Be Auditable

Every material recovery decision should be recorded.

Examples:

retry initiated
execution resumed
execution reconciled
graph invalidated
compensation started
compensation failed
human review requested
execution cancelled

The history should permit reconstruction of:

what happened
why recovery occurred
what state existed
what action was taken
what happened afterward

⸻

45. Reliability and Observability

Reliability depends on observability.

Noema should expose operational information sufficient to identify:

* failure location
* failure class
* Action identity
* execution identity
* attempt count
* dependency state
* graph version
* contract version
* provider response
* retry history
* recovery state
* latency
* final outcome

Observability should expose operational state without requiring access to private model reasoning.

Detailed observability semantics belong to engineering/observability.md.

⸻

46. Reliability Metrics

Relevant reliability measurements may include:

* execution success rate
* definitive failure rate
* unknown outcome rate
* retry rate
* retry exhaustion rate
* recovery rate
* reconciliation rate
* compensation rate
* compensation failure rate
* execution latency
* dependency latency
* provider failure rate
* timeout rate
* queue delay
* recovery duration
* incident frequency

Metrics must preserve semantic distinctions.

For example:

UNKNOWN

must not be counted as:

FAILED

unless the reporting specification explicitly defines such aggregation.

⸻

47. Error Budgets

Operational reliability may use error budgets for infrastructure and execution services.

However, error-budget mechanisms must not override semantic correctness.

For example, exceeding an operational threshold does not justify:

* skipping Trust
* bypassing authorization
* suppressing verification
* declaring unknown outcomes successful
* executing stale graphs

Reliability targets remain subordinate to Noema’s architectural invariants.

⸻

48. Graceful Degradation

When a capability becomes unavailable, Noema may degrade gracefully where the Intent semantics permit it.

Example:

Preferred:
SMS
Alternative:
Email

An alternative must not be selected merely because it exists.

Selection must respect:

* Intent constraints
* Actor requirements
* policy
* capability semantics
* Action Contracts
* authorization
* delivery requirements

Degradation must not silently change what the Actor intended.

⸻

49. No Silent Semantic Degradation

Reliability must never become an excuse for semantic mutation.

For example:

Intent:
Send through SMS

must not silently become:

Send through email

merely because SMS is unavailable.

If substitution is permitted by the Intent or governing policy, it must be explicit.

Otherwise:

BLOCKED / UNAVAILABLE

may be the correct state.

⸻

50. Fail-Closed vs Fail-Open

Noema should explicitly determine whether a failure condition permits continued execution.

For consequential Actions, uncertainty about a required safety, authorization, or governance condition should generally remain unresolved rather than being treated as satisfied.

Conceptually:

Unknown authorization
        ↓
not authorized

is different from:

Unknown authorization
        ↓
authorization confirmed

The latter is impermissible without authoritative evidence.

The exact fail-closed semantics belong to the relevant Trust and Action Contract specifications.

⸻

51. Reliability and Trust

Reliability must not alter Trust semantics.

For example:

Trust = BLOCKED

must remain blocked regardless of:

* retry count
* worker availability
* execution urgency
* external pressure

Similarly:

Trust = READY

does not guarantee successful execution.

The distinction remains:

Trust → execution eligibility
Execution → operational result

⸻

52. Reliability and Action Graph

The Action Graph defines execution relationships.

Reliability mechanisms must preserve those relationships.

A recovery process must not:

* bypass dependencies
* execute blocked downstream nodes
* skip mandatory conditions
* invent branches
* remove required Actions
* reorder Actions contrary to their contracts

Recovery modifies execution state according to graph semantics.

It does not rewrite the Intent.

⸻

53. Reliability and Intent Versioning

If an Intent changes materially during an interrupted execution, the old execution state must not silently become execution state for the new Intent version.

Conceptually:

Intent v1
   ↓
Execution
   ↓
Intent materially changed
   ↓
Intent v2

The system must establish whether:

* the existing execution can continue
* the execution must stop
* compensation is required
* the graph must be rebuilt
* Trust must be re-evaluated

Previous authorization must not silently transfer across material semantic changes.

⸻

54. Reliability and Graph Versioning

Likewise, a changed Action Graph must remain distinguishable from its predecessor.

Example:

Graph v1
   ↓
failure / material change
   ↓
Graph v2

The execution history must preserve which graph version governed each Action.

This supports:

* audit
* reconciliation
* debugging
* incident analysis
* deterministic recovery

⸻

55. Reliability and Outcome

Outcome is the authoritative record of what Noema established happened during execution.

Reliability requires that Outcome distinguish:

SUCCESS
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
CANCELLED
UNKNOWN

The exact Outcome taxonomy belongs to the Outcome specification.

The reliability requirement is that outcome states remain semantically meaningful.

⸻

56. Completion Is an Assertion

Completion is not simply:

worker returned 200

or:

last Action returned success

Completion must satisfy the applicable graph and contract conditions.

For example:

all mandatory Actions completed
+
required postconditions satisfied
+
required external outcomes verified
+
no unresolved mandatory dependencies

Only then may the execution be represented as complete.

⸻

57. Exactly-Once Semantics

Noema should distinguish:

exactly-once processing

from:

exactly-once external effect

Distributed systems may not be able to guarantee exactly-once external effects solely through local execution semantics.

Therefore, Noema should rely on explicit mechanisms such as:

* idempotency keys
* provider-side deduplication
* durable execution state
* reconciliation
* transactional boundaries where available

Claims of exactly-once behavior must be tied to a defined boundary.

⸻

58. At-Least-Once Execution

Where execution is intentionally at-least-once, Action Contracts must define how repeated attempts are handled.

For example:

At-least-once delivery
        ↓
Idempotent Action
        ↓
Single intended external effect

Without appropriate idempotency semantics, at-least-once execution may create duplicate effects.

The reliability architecture must make this explicit.

⸻

59. Exactly-Once State Transitions

Within Noema’s own durable state, state transitions should use mechanisms that prevent conflicting concurrent updates.

Examples include:

compare-and-set
transactional update
version checks
optimistic concurrency
durable coordination

The specific implementation is an engineering concern.

The architectural requirement is that execution state cannot be silently corrupted by concurrent writers.

⸻

60. State Transition Safety

An execution state transition must be valid according to the state machine.

For example:

NOT_STARTED
   ↓
EXECUTING
   ↓
COMPLETED

is valid.

But:

COMPLETED
   ↓
NOT_STARTED

must not occur silently.

If a correction is required, it must be represented as an explicit event or state transition with provenance.

⸻

61. Recovery State Machine

A conceptual recovery lifecycle is:

RUNNING
   ↓
INTERRUPTED
   ↓
CLASSIFY
   ↓
┌──────────┬──────────┬───────────┐
↓          ↓          ↓
RESUME    RETRY    RECONCILE
↓          ↓          ↓
RUNNING   RUNNING   VERIFIED
                       │
                       ▼
                    RUNNING

Other outcomes may include:

BLOCKED
FAILED
COMPENSATION_REQUIRED
ESCALATED
UNKNOWN

The exact execution state machine should be defined separately.

⸻

62. Human Recovery

Some failures require human intervention.

Examples:

* unknown payment outcome
* irreconcilable provider state
* contract mismatch
* ambiguous business state
* failed compensation
* policy exception

Human intervention must be explicit.

For example:

UNKNOWN
   ↓
HUMAN_REVIEW_REQUIRED
   ↓
RECONCILED

Human intervention must not be represented as an ordinary Action failure.

⸻

63. Manual Intervention Must Preserve Provenance

A human recovery decision should preserve:

* actor or operator identity where applicable
* reason
* timestamp
* affected execution
* previous state
* resulting state
* evidence used
* applicable authorization

This prevents manual intervention from becoming an untraceable mutation of execution state.

⸻

64. Disaster Recovery

Noema infrastructure should support recovery from larger-scale failures.

Examples include:

* database failure
* regional infrastructure failure
* queue loss
* worker fleet failure
* provider outage
* storage failure

Disaster recovery must preserve the same architectural invariants as ordinary recovery.

Availability restoration is insufficient if it produces incorrect execution state.

⸻

65. Durable Recovery Point

The system should define the durable state from which execution can be reconstructed.

A recovery point should contain sufficient information to establish:

what Intent existed
what graph existed
what Actions were authorized
what Actions executed
what outcomes were known
what remained unresolved

Recovery must not depend on reconstructing history from transient logs alone.

⸻

66. Recovery Testing

Reliability must be tested through deliberate failure scenarios.

Examples include:

* worker termination during execution
* database restart
* queue duplication
* network timeout
* provider timeout
* provider success followed by response loss
* duplicate execution request
* capability disappearance
* contract version change
* authorization revocation
* graph invalidation
* compensation failure
* partial execution
* unknown external outcome

A system is not reliable merely because the normal execution path works.

⸻

67. Failure Injection

Where appropriate, engineering systems should deliberately inject failures to verify recovery behavior.

Examples:

kill worker
delay provider response
drop network response
duplicate message
reject request
expire lease
invalidate dependency
corrupt test response

The purpose is to establish that defined invariants survive failure.

⸻

68. Recovery Verification

Recovery tests should verify state rather than merely absence of errors.

For example:

Worker restarted

is not sufficient.

The test should establish:

No duplicate external effect
+
execution state preserved
+
graph dependencies preserved
+
outcome correctly recorded

Reliability testing therefore validates semantic correctness.

⸻

69. Incident Reconstruction

After a failure, Noema should be able to reconstruct:

1. the Intent
2. the Intent version
3. the Trust state
4. the Action Graph
5. the Action Contract
6. the execution identity
7. each attempt
8. external requests
9. responses received
10. failures
11. retries
12. recovery decisions
13. graph changes
14. final Outcome

This is an engineering requirement, not merely an observability convenience.

⸻

70. Reliability and Provenance

Reliability events should preserve provenance.

For example:

execution.retry_requested
    execution_id
    action_id
    attempt
    reason
    policy_version
    timestamp

This permits recovery behavior to be reconstructed without relying on hidden model state.

⸻

71. No Hidden Recovery

A model must not silently perform recovery actions outside the explicit execution system.

For example:

Action failed
   ↓
LLM decides to call another tool

is not an acceptable reliability mechanism for consequential execution.

Recovery must follow:

Action Graph
   ↓
Action Contract
   ↓
Execution Policy
   ↓
Recovery

Tool use remains an implementation mechanism, not an authority model.

⸻

72. Reliability and Model Failure

Models may:

* hallucinate Actions
* generate incorrect parameters
* misinterpret failures
* produce inconsistent plans
* propose unsafe recovery
* misunderstand external responses

Therefore, reliability mechanisms must not rely on model correctness as a safety guarantee.

Deterministic validation, contracts, durable state, and explicit recovery semantics remain authoritative.

⸻

73. Model Unavailability

Noema should distinguish model unavailability from Intent failure.

For example:

LLM unavailable

does not necessarily mean:

Intent invalid

The system may:

WAIT
RETRY
FALL BACK
REQUEST CLARIFICATION

depending on the lifecycle stage and available deterministic mechanisms.

⸻

74. Reliability and Clarification

If required semantic information is missing, reliability mechanisms must not substitute an arbitrary value merely to keep execution moving.

Example:

recipient = ambiguous

must remain:

CLARIFICATION_REQUIRED

rather than:

select probable recipient

Reliability preserves semantic correctness even when that means delaying execution.

⸻

75. Reliability and External State

External business state can change independently of Noema.

Example:

T1:
Account = ACTIVE
T2:
Noema prepares execution
T3:
Account = SUSPENDED
T4:
Action executes

The external system remains authoritative.

The Action Contract may reject execution.

Noema should record the resulting condition rather than treating the rejection as evidence that the external system is incorrect.

⸻

76. Time-of-Check / Time-of-Use

Reliability must account for TOCTOU conditions.

A condition verified at:

T1

may no longer hold at:

T2

when execution occurs.

Consequential Action Contracts may therefore require execution-time checks.

Reliability must preserve this distinction:

Previously verified

does not necessarily mean:

currently true

⸻

77. Recovery and Re-Validation

After sufficient interruption or material change, Noema may need to revalidate:

* Intent
* graph
* capability
* Action Contract
* authorization
* policy
* external state

Revalidation must be explicit.

A recovery mechanism must not blindly resume stale execution merely because the original execution was once valid.

⸻

78. Reliability and Versioning

Reliability-relevant artifacts should be versioned where changes can affect behavior.

Examples include:

* Intent versions
* graph versions
* Action Contract versions
* policy versions
* resolution-rule versions
* retry-policy versions
* recovery-policy versions

The execution record should preserve the versions relevant to the decision.

⸻

79. Reliability and Determinism

Where recovery behavior is governed by deterministic rules, the same relevant state and rule versions should produce the same recovery decision.

For example:

Failure:
TIMEOUT
Attempt:
2
Maximum:
3
Retry policy:
v4

should deterministically establish whether another retry is permitted.

Model variability must not silently alter deterministic recovery semantics.

⸻

80. Reliability Does Not Guarantee Success

Reliability is not a promise that every Action succeeds.

An external system may reject an Action.

A capability may disappear.

A network may fail.

A business condition may change.

A provider may return an unknown result.

A reliable Noema system represents these conditions correctly.

Therefore:

Reliable System
      ≠
Always Successful System

Instead:

Reliable System
=
Predictable behavior under success and failure

⸻

81. Reliability Does Not Mean Aggressive Recovery

The objective is not to maximize the number of Actions that eventually execute.

The objective is to preserve correctness.

Therefore, a reliable system may legitimately choose:

STOP
WAIT
BLOCK
ESCALATE
UNKNOWN

rather than:

RETRY UNTIL SOMETHING WORKS

The appropriate response is determined by the semantics of the Action and its governing contracts.

⸻

82. Reliability Architecture

The engineering model can be summarized as:

                 Durable State
                      │
                      ▼
Intent → Trust → Action Graph → Contract → Execution
                                  │
                                  ▼
                              External System
                                  │
                                  ▼
                               Outcome
                                  │
                                  ▼
                         Failure / Recovery
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
           Retry              Reconcile           Compensate
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  ▼
                              Verified State

Reliability surrounds execution rather than existing as a separate final step.

⸻

83. Reliability Checklist

Before an Action is considered operationally reliable, Noema should be able to answer:

1. What is the execution identity?
2. What happens if the worker terminates?
3. What happens if the request times out?
4. What happens if the external system performed the Action but Noema received no response?
5. Can the Action be retried safely?
6. What makes the Action idempotent?
7. What failures are retryable?
8. How many retries are permitted?
9. What happens after retry exhaustion?
10. How is external state reconciled?
11. What happens if authorization changes?
12. What happens if the Action Graph becomes stale?
13. What happens if compensation fails?
14. How is partial execution represented?
15. How is the final Outcome established?
16. Can the entire execution history be reconstructed?

If these questions cannot be answered, the Action is not sufficiently specified for reliable consequential execution.

⸻

84. Canonical Reliability Flow

The canonical lifecycle is:

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
Durable State
   ↓
Success
   │
   └── Failure
         ↓
      Classify
         ↓
   ┌─────┼──────────┬───────────┐
   ▼     ▼          ▼           ▼
 Retry  Resume   Reconcile  Compensate
   │     │          │           │
   └─────┴──────────┴───────────┘
                ↓
             Verify
                ↓
             Outcome

At any stage, the valid result may instead be:

WAIT
BLOCK
ESCALATE
CANCEL
UNKNOWN
FAIL

according to the applicable semantics.

⸻

85. Relationship to Failure Recovery

engineering/reliability.md defines the broader engineering principles governing predictable behavior under failure.

engineering/failure-recovery.md defines the more specific mechanisms and lifecycle for recovering from interrupted or failed execution.

The relationship is:

Reliability
    ↓
Failure Classification
    ↓
Failure Recovery

Reliability establishes the requirements.

Failure recovery implements the corresponding recovery behavior.

⸻

86. Relationship to Idempotency

Idempotency is a specific reliability mechanism for controlling duplicate execution effects.

The relationship is:

Reliability
     ↓
Safe Retry
     ↓
Idempotency

Idempotency does not itself provide complete reliability.

A system may be idempotent while still suffering from:

* stale state
* incorrect authorization
* dependency failures
* malformed contracts
* incomplete recovery
* unknown outcomes

Therefore:

Idempotency ⊂ Reliability

⸻

87. Relationship to Observability

Observability provides the evidence required to operate and investigate a reliable system.

The relationship is:

Reliability
     ↓
State + Events + Metrics
     ↓
Observability
     ↓
Detection + Diagnosis + Verification

Observability does not create reliability by itself.

It makes reliability behavior inspectable.

⸻

88. Relationship to Durable Execution

Durable execution provides the infrastructure semantics necessary to preserve execution state across process and infrastructure failures.

Conceptually:

Reliability Requirements
          ↓
Durable Execution
          ↓
Recoverable Execution State

Durable execution is therefore an implementation foundation for reliability, not a substitute for Action Contracts, Trust, or graph semantics.

⸻

89. Engineering Principle

Noema must treat every consequential Action as a distributed operation occurring across potentially unreliable boundaries.

Therefore:

Assume interruption.
Assume duplication.
Assume delay.
Assume stale state.
Assume partial failure.
Assume unknown outcome.

Then define what the system must do in each case.

This is preferable to designing only for the successful execution path and adding retries afterward.

⸻

90. Canonical Mental Model

Reliability can be reduced to five questions:

1. What state must survive failure?
2. What can safely be retried?
3. What must be reconciled rather than retried?
4. What happens when execution is only partially complete?
5. How does Noema establish and record what actually happened?

Which produces:

Durable State
      ↓
Failure Classification
      ↓
Controlled Recovery
      ↓
Verification
      ↓
Outcome

⸻

91. Final Definition

Reliability is Noema’s engineering discipline for preserving correctness, state, provenance, execution integrity, and explicit outcome semantics across failure, interruption, duplication, delay, partial execution, changing external conditions, and recovery.

Its central invariant is:

Noema must never rely on uninterrupted execution for correctness. Every consequential execution must have explicit failure, retry, recovery, reconciliation, and outcome semantics sufficient to preserve the distinction between what was intended, what was authorized, what was attempted, what actually happened, and what remains unknown.

The fundamental boundary remains:

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
Durable Execution
   ↓
Recovery / Reconciliation
   ↓
Verified Outcome

Reliability therefore does not mean that Noema always succeeds.

It means that when Noema succeeds, fails, waits, retries, recovers, compensates, or encounters an unknown result, the system preserves the truth of its state and never silently converts operational uncertainty into semantic certainty.