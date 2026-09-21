Durable Execution

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/durable-execution.md

⸻

1. Definition

Durable Execution is Noema’s architectural model for ensuring that an authorized execution process can survive interruption, failure, delay, retry, process termination, infrastructure failure, and other transient conditions without losing the authoritative state required to determine what has happened, what remains permitted, and what may happen next.

Durable Execution concerns the persistence and recovery of execution state.

It does not establish:

* what the Actor intends
* whether an Intent is semantically resolved
* whether an Intent is trusted
* what Actions should exist in an Action Graph
* what an Action Contract permits
* whether an external business operation ultimately succeeded

Those responsibilities belong to other architectural layers.

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
Durable Execution
   ↓
External Execution
   ↓
Outcome

Durable Execution ensures that the execution process remains recoverable, inspectable, and state-consistent across interruptions and failures.

⸻

2. Architectural Responsibility

Durable Execution is responsible for maintaining sufficient execution state to resume, reconcile, or terminate execution without relying on volatile process memory.

It is responsible for:

* persisting execution state
* persisting Action state
* recording execution transitions
* recording durable execution events
* recovering interrupted execution
* maintaining execution checkpoints where required
* coordinating retries according to Action Contract semantics
* preserving idempotency information
* distinguishing completed, failed, pending, and unknown execution states
* detecting interrupted execution
* supporting reconciliation with external systems
* preserving execution history
* preventing duplicate execution where durable state and contracts permit prevention
* making recovery deterministic where the architecture requires it

Durable Execution must not silently cross into:

* Intent resolution
* Trust determination
* authorization
* Action selection
* external business-state ownership

⸻

3. Why Durable Execution Exists

Execution cannot be treated as a single uninterrupted function call.

Consider:

Action A
   ↓
Action B
   ↓
Action C

The process executing Action B may:

* terminate
* lose network connectivity
* restart
* lose its host
* encounter a timeout
* receive an ambiguous external response
* lose volatile memory
* be unavailable for an extended period

The external system may nevertheless have completed the operation.

Therefore:

Process Failure
      ≠
Action Failure

and:

Process Restart
      ≠
Execution Restart From Zero

Durable Execution exists to preserve the execution state necessary to distinguish these cases.

⸻

4. Core Principle

Noema must not depend on volatile process state as the authoritative record of execution.

Conceptually:

Volatile Process
      ↓
Execution
      ↓
Durable State

not:

Volatile Process
      ↓
Execution State

If the process disappears, the execution state must remain recoverable.

The fundamental principle is:

Execution state required for recovery must survive the process that produced it.

⸻

5. Durable State vs Runtime State

Noema should distinguish:

Runtime state

from:

Durable execution state.

Runtime state may include:

* in-memory variables
* open connections
* temporary caches
* worker-local state
* transient execution context

Durable state may include:

* execution identity
* graph version
* Action identity
* Action state
* attempt count
* idempotency identity
* dependency state
* persisted outputs
* failure state
* unknown outcome state
* timestamps
* recovery markers
* external operation references

Runtime state may disappear.

Durable execution state must remain reconstructible.

⸻

6. Execution Identity

Every execution must have an explicit identity.

Conceptually:

Execution {
    execution_id
    intent_id
    intent_version
    graph_id
    graph_version
    state
    created_at
    updated_at
}

The exact schema belongs to the execution specification.

Execution identity must remain stable across process restarts.

A restarted worker must recover the same execution rather than silently creating a new execution representing the same work.

⸻

7. Action Execution Identity

Individual Action executions should also have explicit identities.

Conceptually:

ActionExecution {
    execution_id
    action_node_id
    action_execution_id
    contract_id
    contract_version
    state
    attempt
}

This allows Noema to distinguish:

Action

from:

Execution of Action

and:

Attempt to execute Action

These are separate concepts.

⸻

8. Execution State

Execution state should be explicit.

Conceptual Action execution states include:

NOT_STARTED
READY
EXECUTING
WAITING
COMPLETED
FAILED
BLOCKED
SKIPPED
UNKNOWN
CANCELLED

The exact state machine belongs to the execution specification.

These states must not be conflated with:

* Intent state
* Trust state
* graph validation state

For example:

Intent:
RESOLVED
Trust:
READY
Action:
UNKNOWN

is a valid state combination.

⸻

9. Durable State Transitions

Durable execution state must change through explicit execution events or defined state transitions.

Conceptually:

READY
  ↓
EXECUTING
  ↓
COMPLETED

or:

READY
  ↓
EXECUTING
  ↓
FAILED

or:

READY
  ↓
EXECUTING
  ↓
UNKNOWN

The transition must be durably recorded before it is treated as authoritative.

A process must not rely solely on an in-memory belief that a transition occurred.

⸻

10. Execution Event

A durable execution event represents a material execution transition or observation.

Conceptually:

ExecutionEvent {
    event_id
    execution_id
    action_execution_id
    event_type
    previous_state
    resulting_state
    timestamp
    attempt
    provenance
}

Illustrative events include:

execution.started
action.ready
action.started
action.completed
action.failed
action.waiting
action.unknown
action.retry_scheduled
execution.interrupted
execution.recovered
execution.completed
execution.failed

The exact protocol may evolve.

The important requirement is that material execution state remains reconstructible.

⸻

11. Event Ordering

Execution events must have an explicit ordering mechanism.

Possible mechanisms include:

* monotonically increasing sequence numbers
* durable event versions
* transactional state revisions
* another explicitly defined ordering mechanism

Wall-clock timestamps alone should not be treated as sufficient ordering authority.

For example:

event_sequence = 41
event_sequence = 42
event_sequence = 43

provides an explicit execution history.

⸻

12. Durable State and Atomicity

Where a state transition and its associated durable event must be treated as one logical operation, the architecture should provide an atomic persistence boundary.

For example:

Action completed
      +
Completion recorded

should not produce an ambiguous durable state where one exists without the other unless the architecture explicitly defines reconciliation semantics.

The implementation mechanism may vary.

The invariant is that recovery must be able to determine the authoritative execution state.

⸻

13. Recovery

Recovery is the process of reconstructing executable state after execution has been interrupted.

Conceptually:

Durable Execution State
        ↓
Recovery
        ↓
Reconstructed Execution
        ↓
Resume / Reconcile / Terminate

Recovery must not assume that the interrupted process completed its last operation.

It must determine the state from durable information and, where necessary, authoritative external evidence.

⸻

14. Process Failure

A process may fail after:

Action started

but before:

Action completed

For example:

Worker
   ↓
starts payment
   ↓
process crashes

The durable state may remain:

EXECUTING

The external payment system may have:

COMPLETED

or:

NOT_FOUND

or:

UNKNOWN

Therefore recovery must not automatically convert:

EXECUTING

into:

FAILED

⸻

15. Interrupted Execution

An interrupted execution is not necessarily a failed execution.

Conceptually:

EXECUTING
    ↓
Process interruption
    ↓
RECOVERY REQUIRED

Recovery may result in:

COMPLETED
FAILED
RETRYABLE
UNKNOWN
WAITING

depending on the available evidence and applicable Action Contract.

⸻

16. Durable Execution and Unknown Outcomes

Unknown outcomes are fundamental to durable execution.

Consider:

REQUEST_PAYMENT
      ↓
External request
      ↓
Network timeout

The response does not establish whether the payment occurred.

The correct durable state may therefore be:

UNKNOWN

not:

FAILED

and not:

COMPLETED

unless authoritative evidence establishes the result.

⸻

17. Unknown Must Remain Unknown

Noema must not convert an unknown execution result into success or failure merely to simplify recovery.

Therefore:

UNKNOWN
   ≠
FAILED

and:

UNKNOWN
   ≠
COMPLETED

An unknown state may require:

* reconciliation
* external lookup
* human intervention
* provider confirmation
* explicit recovery policy

⸻

18. Recovery and External Authority

External systems remain authoritative for their respective business state.

For example:

Noema:
payment execution = UNKNOWN
Payment Provider:
payment status = COMPLETED

The authoritative provider evidence may resolve the execution state.

Noema should record the evidence and transition its execution state accordingly.

Noema must not manufacture external business state from the absence of a response.

⸻

19. Reconciliation

Reconciliation is the process of resolving uncertain execution state against an authoritative external system.

Conceptually:

Action
  ↓
UNKNOWN
  ↓
Reconciliation
  ↓
External Authority
  ↓
Observed State
  ↓
Durable Execution State

For example:

UNKNOWN
   ↓
Query provider
   ↓
provider = COMPLETED
   ↓
COMPLETED

or:

UNKNOWN
   ↓
Query provider
   ↓
provider = NOT_FOUND
   ↓
Recovery policy

The exact recovery semantics depend on the Action Contract and external system.

⸻

20. Retry

Retries must be durable.

A retry must not depend on a worker remembering that an Action had previously failed.

Conceptually:

Action Attempt 1
      ↓
FAILED
      ↓
Retry permitted
      ↓
Action Attempt 2

The durable state should preserve:

* attempt count
* failure classification
* retry eligibility
* retry timing
* idempotency identity
* applicable contract version

⸻

21. Retry Is Not Re-Execution by Default

A retry does not automatically mean:

perform the external operation again.

The system must first determine whether the previous attempt’s outcome is known.

For example:

Attempt 1
   ↓
timeout
   ↓
Outcome UNKNOWN

Blindly performing Attempt 2 may create a duplicate external operation.

Therefore:

Retry

must respect the distinction between:

FAILED

and:

UNKNOWN

⸻

22. Idempotency

Idempotency is a central requirement for durable execution of consequential Actions.

An Action Contract may define an idempotency key or equivalent mechanism.

Conceptually:

Action
   ↓
Idempotency Key
   ↓
External Consumer

If an execution attempt is repeated after an uncertain result, the consumer may recognize that the operation has already been submitted.

The exact semantics belong to the Action Contract and consumer.

Durable Execution must preserve and reuse the relevant idempotency identity according to those semantics.

⸻

23. Idempotency Identity

Where required, the same logical Action execution should preserve the same idempotency identity across retries.

For example:

action_execution_id = AX-123
idempotency_key     = IK-456

Attempt 1:

IK-456 → external system

Attempt 2:

IK-456 → external system

must not silently become:

IK-789 → external system

if that would defeat the Action’s idempotency semantics.

⸻

24. Retry Boundaries

Retries must be bounded according to the applicable Action Contract and execution policy.

Relevant controls may include:

* maximum attempts
* timeout
* retryable failure classes
* backoff
* retry window
* idempotency requirements
* external provider semantics

A model must not invent retry behavior during recovery.

⸻

25. Durable Timers

Durable execution may require waiting.

Examples:

WAIT 30 minutes

or:

WAIT UNTIL APPROVAL

A wait must not depend on a worker remaining alive.

Instead:

Action
  ↓
WAITING
  ↓
Durable wake condition
  ↓
READY

The execution may therefore survive process termination while waiting.

⸻

26. Long-Running Execution

Some Actions or Action Graphs may take:

* seconds
* minutes
* hours
* days
* longer periods

Durable Execution must not require a continuously running process for the entire lifetime of the execution.

The durable execution state should be sufficient to resume processing when the required event or condition occurs.

⸻

27. Human Waiting

Human approval or confirmation may suspend execution.

Example:

CREATE_TRANSFER
      ↓
WAIT_FOR_APPROVAL
      ↓
APPROVED
      ↓
EXECUTE_TRANSFER

The waiting state must be durable.

The execution must survive:

* worker restart
* service deployment
* infrastructure failure
* extended waiting periods

Approval itself does not erase the need for downstream Trust and execution checks where those are required.

⸻

28. External Events

Execution may depend on an external event.

Examples:

* payment provider callback
* delivery status update
* human approval
* identity verification result
* external resource becoming available

The execution may enter:

WAITING

and later resume when the event is received.

External events must be associated with the correct execution identity and validated according to the applicable event semantics.

⸻

29. Duplicate Events

Distributed systems may deliver the same external event more than once.

Therefore event processing should be designed to tolerate duplicate delivery where the relevant protocol permits it.

Conceptually:

event_123
event_123

must not result in:

Action completed twice

The implementation may use:

* event identity
* deduplication
* sequence numbers
* idempotent state transitions
* transactional consumption

The exact mechanism belongs to the execution architecture.

⸻

30. Out-of-Order Events

External events may also arrive out of order.

For example:

delivery.completed

may arrive before:

delivery.dispatched

if the underlying integration does not guarantee ordering.

Noema must not blindly advance execution state based solely on event arrival order.

Applicable ordering and state-transition rules must determine whether the event is valid for the current execution state.

⸻

31. Execution Checkpoints

Durable execution may use explicit checkpoints.

A checkpoint represents a durable point from which execution can safely resume.

Conceptually:

A
↓
Checkpoint 1
↓
B
↓
Checkpoint 2
↓
C

The exact checkpoint model depends on implementation.

The architectural requirement is that recovery must be able to reconstruct enough state to continue without violating Action Graph and Action Contract semantics.

⸻

32. Checkpoint vs Outcome

A checkpoint does not mean that the external Action succeeded.

For example:

Checkpoint:
Action request submitted

does not necessarily mean:

External operation completed

Durable Execution must distinguish:

* execution progress
* request submission
* external acknowledgment
* verified outcome

These may be separate states.

⸻

33. Execution Journal

Noema may maintain a durable execution journal.

Conceptually:

Execution Journal
1. execution.created
2. action.ready
3. action.started
4. request.submitted
5. response.timeout
6. action.unknown
7. reconciliation.started
8. external.status=COMPLETED
9. action.completed

The journal supports:

* recovery
* auditability
* debugging
* reconciliation
* historical reconstruction

The exact persistence mechanism is implementation-specific.

⸻

34. Execution State Reconstruction

The authoritative execution state should be reconstructible from durable state.

Conceptually:

Durable Events / State
        ↓
State Reconstruction
        ↓
Current Execution State

A recovered worker should not depend on undocumented assumptions about what happened before the process terminated.

⸻

35. Recovery Is Not Replanning

Recovery must not silently become arbitrary replanning.

If execution is interrupted:

Action Graph v3
      ↓
Execution interrupted
      ↓
Recovery

does not mean:

Execution interrupted
      ↓
Generate a new plan

The existing graph remains authoritative unless the architecture explicitly determines that a material change requires:

* revalidation
* Trust re-evaluation
* graph revision
* new execution state

Recovery and replanning are distinct operations.

⸻

36. Recovery and Graph Version

Execution must retain the Action Graph version against which it was created.

Conceptually:

Intent Version: 7
Graph Version: 3
Execution: 14

Recovery must resume against the appropriate graph version.

A newer graph must not silently replace the graph governing an already-authorized execution.

⸻

37. Material Change During Execution

External conditions may materially change during execution.

Examples:

* capability revoked
* Action Contract changed
* authorization changed
* external resource state changed
* policy changed
* Intent changed

Such changes may require:

Pause
  ↓
Re-evaluation
  ↓
Trust / Contract / Graph decision
  ↓
Resume / Revise / Terminate

Durable execution must preserve the transition.

It must not silently continue under stale assumptions.

⸻

38. Execution Lease

Distributed execution may require a mechanism preventing multiple workers from simultaneously believing they own the same execution.

A lease or equivalent ownership mechanism may be used.

Conceptually:

Execution
    ↓
Worker A owns execution
    ↓
Worker A fails
    ↓
Lease expires
    ↓
Worker B recovers execution

The lease is an execution coordination mechanism.

It is not an authorization mechanism.

⸻

39. Lease Is Not Execution Authority

Possessing an execution lease does not mean the worker has permission to execute an Action.

The canonical authority chain remains:

Trust
  ↓
Action Graph
  ↓
Action Contract
  ↓
Execution

A lease merely establishes which execution worker may currently operate on durable execution state.

⸻

40. Concurrency Control

Durable execution must prevent conflicting concurrent state transitions where necessary.

For example:

Worker A:
Action READY → EXECUTING
Worker B:
Action READY → EXECUTING

must not result in two independent executions of the same non-idempotent Action unless explicitly permitted.

Possible mechanisms include:

* leases
* optimistic concurrency
* compare-and-swap semantics
* transactional state transitions
* durable locks where appropriate

The specific mechanism is implementation-dependent.

⸻

41. Exactly-Once Semantics

Noema should not assume that distributed execution can universally provide exactly-once external side effects.

The architecture should distinguish:

Exactly-once state transition

from:

Exactly-once external effect

An internal durable state transition may be made atomic.

An external system may still receive duplicate requests unless the external contract provides appropriate idempotency semantics.

Therefore:

Exactly-once execution semantics cannot be assumed merely because internal state is durable.

⸻

42. At-Least-Once Execution

Some execution architectures may use at-least-once delivery or retry.

In such systems:

Action
   ↓
Attempt
   ↓
Retry
   ↓
Possible duplicate request

Durable Execution must rely on the Action Contract and consumer semantics to prevent harmful duplication where required.

Idempotency is therefore not optional for every Action, but it is essential where duplicate execution can produce consequential effects.

⸻

43. At-Most-Once Execution

At-most-once execution may avoid duplicate requests by refusing to retry uncertain operations.

However, this may leave the outcome unknown.

For example:

Request submitted
      ↓
Timeout
      ↓
Do not retry
      ↓
UNKNOWN

Therefore:

Avoiding duplication

may trade off against:

certainty of completion

The applicable Action Contract and execution policy must establish the correct semantics.

⸻

44. Durable Execution and Compensation

If an Action Graph requires compensation after partial execution, durable execution must preserve the state necessary to determine which compensations are applicable.

Example:

A → COMPLETED
B → COMPLETED
C → FAILED

may produce:

Compensate B
Compensate A

if explicitly defined.

Compensation must not be inferred merely because execution failed.

⸻

45. Compensation Is Not Rollback

External operations may not support transactional rollback.

Therefore:

Compensation

does not necessarily mean:

Rollback

Durable Execution must preserve the actual history of:

* original Action
* external effect
* compensation Action
* compensation result

A failed compensation must remain visible.

⸻

46. Partial Execution

An execution may terminate in a partially completed state.

Example:

A → COMPLETED
B → COMPLETED
C → FAILED
D → NOT_STARTED

Durable Execution must preserve these individual states.

It must not compress them into:

FAILED

without retaining the underlying Action-level history.

⸻

47. Execution Outcome

The aggregate execution outcome may include:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN
CANCELLED

The exact state model belongs to the execution specification.

Aggregate outcome must remain distinct from individual Action state.

⸻

48. Execution Completion

An execution is complete only when the graph’s applicable completion conditions have been satisfied.

Completion may require:

* all mandatory Actions completed
* required postconditions verified
* required external outcomes observed
* no unresolved mandatory branches
* no outstanding compensation requirements
* no required human intervention

A final process return value alone does not establish completion.

⸻

49. Durable Completion

Completion itself must be durable.

Conceptually:

Last required Action
       ↓
Completion conditions satisfied
       ↓
Execution COMPLETED
       ↓
Durable completion record

A worker terminating immediately after determining completion must not leave the execution permanently ambiguous.

⸻

50. Cancellation During Execution

An execution may be cancelled.

Cancellation must be represented explicitly.

For example:

EXECUTING
    ↓
Cancellation requested
    ↓
CANCELLATION PROCESSING
    ↓
CANCELLED

Cancellation semantics depend on whether Actions have already produced external effects.

A cancellation request does not necessarily imply that external operations can be undone.

⸻

51. Cancellation vs Failure

Cancellation and failure must remain distinct.

CANCELLED

means the execution was terminated through an explicit cancellation semantic.

FAILED

means execution could not complete according to its applicable failure semantics.

These states may have different downstream consequences.

⸻

52. Execution Timeouts

Timeouts must be explicit.

A timeout may mean:

* the worker exceeded an execution limit
* the external system did not respond
* a waiting condition expired
* a reconciliation window elapsed

A timeout does not automatically mean that the external operation failed.

Therefore:

Timeout
   ↓
Evaluate semantics

not:

Timeout
   ↓
FAILED

⸻

53. Durable Waiting and Timeout

A durable wait should include enough information to recover the waiting state.

Conceptually:

WAITING {
    condition
    deadline
    wake_event
    timeout_policy
}

The exact representation is implementation-specific.

The important requirement is that a restarted worker can determine whether the wait is:

* still active
* satisfied
* expired
* unknown

⸻

54. Execution Recovery After Deployment

A deployment must not invalidate active durable executions merely because the worker implementation changed.

Where compatibility permits:

Old Worker
    ↓
Durable State
    ↓
New Worker
    ↓
Resume

The execution must retain the versioned semantics required to interpret its state.

Incompatible changes require explicit migration or termination semantics.

⸻

55. Execution Schema Versioning

Durable execution records should be versioned where schema evolution can affect recovery.

Conceptually:

execution_schema_version = 3

A newer execution engine must know how to interpret older durable records or explicitly migrate them.

Silent reinterpretation of historical state is not acceptable.

⸻

56. Action Contract Versioning

Execution must retain the Action Contract version relevant to each Action execution.

For example:

Action:
TRANSFER_FUNDS
Contract:
transfer.create
Version:
4

Recovery should not silently reinterpret an old execution using a materially different contract.

If the contract changes materially, explicit re-evaluation may be required.

⸻

57. Durable Execution and Trust

Durability does not preserve Trust indefinitely.

For example:

Trust:
READY
Execution:
WAITING

If the execution remains suspended long enough for relevant Trust conditions to change, the execution may require Trust re-evaluation before continuing.

Durable state preserves the execution.

It does not bypass Trust.

⸻

58. Durable Execution and Authorization

Authorization must not be inferred from durable execution state.

For example:

Action state = READY

does not mean:

Actor is currently authorized

If authorization is time-sensitive or materially changes during execution, the applicable Trust and Action Contract semantics must determine whether execution can continue.

⸻

59. Durable Execution and Business State

Durable execution state is not authoritative business state.

For example:

Noema:
payment Action = COMPLETED

does not by itself mean Noema owns:

payment.status = SETTLED

The external payment system remains authoritative for its business state.

Noema records execution observations and references to external evidence.

⸻

60. Durable Execution and TOCTOU

Time-of-check / time-of-use conditions apply to durable execution.

For example:

Trust Check
    ↓
Execution waits 2 hours
    ↓
External state changes
    ↓
Resume

The original Trust decision may no longer be sufficient.

Therefore consequential Actions may require final authoritative checks before execution.

Durable waiting must not create a mechanism for bypassing fresh execution-time conditions.

⸻

61. Recovery Policy

Recovery behavior should be explicit.

A recoverable Action may specify:

RECOVER
RETRY
RECONCILE
WAIT
ESCALATE
FAIL

The correct response depends on the Action Contract and execution state.

A model must not invent recovery semantics.

⸻

62. No Silent Re-Execution

A recovered worker must not blindly repeat an Action merely because its durable state is:

EXECUTING

The worker must first determine whether:

* the Action completed
* the Action failed
* the Action remains in progress
* the external outcome is unknown
* reconciliation is required
* retry is permitted

This is especially important for non-idempotent external operations.

⸻

63. Recovery Decision

Conceptually:

Durable State
      ↓
Determine Last Known State
      ↓
Evaluate Contract
      ↓
Evaluate External Evidence
      ↓
Recovery Decision
      ↓
Resume / Reconcile / Retry / Wait / Fail

Recovery is therefore a controlled execution decision, not a blind restart.

⸻

64. Execution Provenance

Durable execution should preserve provenance for material execution events.

Provenance may include:

* execution ID
* Action identity
* Action execution identity
* graph version
* contract version
* worker identity
* attempt number
* event identity
* external request identity
* external response reference
* timestamps
* recovery identity
* reconciliation evidence

This allows Noema to reconstruct what occurred without exposing private model reasoning.

⸻

65. Execution Observability

Noema should be able to inspect:

* current execution state
* Action states
* dependency states
* attempt counts
* retries
* waiting conditions
* timeouts
* external operation references
* unknown outcomes
* reconciliation
* compensation
* human intervention
* recovery events
* final outcome

Observability should reflect durable execution state rather than transient worker memory.

⸻

66. Execution Audit History

Material execution transitions should be auditable.

Example:

Execution v1
     ↓
Action A completed
     ↓
Action B started
     ↓
Worker failure
     ↓
Recovery
     ↓
Action B unknown
     ↓
Provider reconciliation
     ↓
Action B completed
     ↓
Action C executed

The history should remain reconstructible.

⸻

67. Durable Execution and the Action Graph

The Action Graph describes the structure of permitted execution.

Durable Execution records and manages the actual progression through that structure.

Therefore:

Action Graph
   ↓
What may happen structurally

while:

Durable Execution
   ↓
What execution has durably reached

The graph is not replaced by the execution journal.

The execution journal does not redefine the graph.

⸻

68. Durable Execution and Outcome

Outcome records what actually happened.

Durable Execution provides the evidence and state history necessary to derive or establish that outcome.

Therefore:

Action Graph
      ↓
Execution
      ↓
Durable Execution State
      ↓
Observed Outcome

An execution state of:

UNKNOWN

must be capable of producing an outcome that remains:

UNKNOWN

until sufficient evidence becomes available.

⸻

69. Execution Does Not Guarantee Success

Durable execution provides recoverability.

It does not guarantee:

SUCCESS

External systems may fail.

Networks may fail.

Business state may change.

Consumers may reject Actions.

An external operation may remain unknown.

Therefore:

Durable Execution
      ≠
Successful Execution

⸻

70. Long-Lived Execution

An Intent may result in execution that remains active for an extended period.

Durable Execution must support state persistence across:

* worker restarts
* infrastructure replacement
* service deployments
* temporary outages
* long human approval periods
* external system delays

Execution lifetime must therefore be independent of the lifetime of an individual worker process.

⸻

71. Execution Handoff

An execution may move between workers.

Conceptually:

Worker A
   ↓
Durable State
   ↓
Worker B

The execution identity and Action execution identity must remain stable across the handoff.

Worker identity is operational provenance, not execution identity.

⸻

72. Execution Isolation

Concurrent executions must remain isolated.

For example:

Execution E1
Action A
Execution E2
Action A

must not accidentally share:

* idempotency identity
* Action state
* external operation identity
* dependency state

unless explicitly defined by the relevant contract.

⸻

73. Execution Dependencies

Durable Execution must respect Action Graph dependencies.

If:

A → B

and A is:

UNKNOWN

B must not automatically execute merely because its worker is available.

The execution layer must evaluate the dependency according to the graph semantics.

⸻

74. Parallel Execution

When independent Actions are permitted to execute concurrently:

        ┌── B ──┐
A ──────┤       ├── D
        └── C ──┘

Durable Execution must preserve independent Action state.

If B completes and C remains unknown:

B = COMPLETED
C = UNKNOWN
D = NOT_READY

unless the graph explicitly defines another behavior.

Parallelism must not collapse dependency semantics.

⸻

75. Failure Propagation

Failure propagation must follow the Action Graph and Action Contract.

If:

A → B → C

and B fails:

B = FAILED

then C must not automatically execute unless an explicit recovery or alternative path permits it.

Durable Execution records the resulting state.

It does not invent recovery behavior.

⸻

76. Execution Re-Evaluation

Material conditions may require execution re-evaluation.

Examples:

* Action Contract changes
* capability disappears
* authorization changes
* policy changes
* external business state changes
* dependency becomes invalid
* execution remains suspended beyond a defined validity period

The durable execution state should make such re-evaluation explicit.

⸻

77. Execution Migration

Long-lived executions may outlive versions of the execution system.

If migration is required, it must be explicit.

Conceptually:

Execution v1
      ↓
Migration
      ↓
Execution v2

The migration must preserve the semantic meaning of the existing execution state.

A migration must not silently change the Actor’s Intent or authorized Action structure.

⸻

78. Execution Data Retention

Durable execution records should be retained according to the applicable retention requirements.

Retention must preserve whatever information is necessary for:

* recovery
* audit
* reconciliation
* outcome reconstruction
* dispute resolution
* compliance where applicable

The exact retention policy is outside this foundational document.

⸻

79. Sensitive Execution Data

Durability does not justify unrestricted persistence of sensitive information.

Execution records should retain the minimum information necessary to support:

* recovery
* provenance
* auditability
* reconciliation
* outcome determination

Sensitive values should be handled according to Noema’s applicable data-protection and security architecture.

⸻

80. Durable Execution Security Boundary

Durable state must not become an authority-escalation mechanism.

A worker recovering an execution must not gain permissions merely because the durable record contains:

Action = TRANSFER_FUNDS

The worker remains subject to:

* Trust
* authorization
* Action Contracts
* capability constraints
* execution-time conditions

Durability preserves state.

It does not create authority.

⸻

81. Model Interaction

An LLM may assist with:

* interpreting execution errors
* proposing recovery diagnostics
* explaining execution state
* suggesting candidate reconciliation procedures where explicitly permitted

It must not silently mutate authoritative durable execution state.

For consequential state transitions:

Model Proposal
      ↓
Deterministic Validation / Contract Rules
      ↓
Durable State Transition

The model is not the authority over execution state.

⸻

82. No Hidden Execution State

An execution must not depend on hidden state that is absent from the durable execution representation.

For example, if a worker internally remembers:

payment already submitted

but durable state contains no corresponding evidence, a restarted worker cannot safely rely on that memory.

Material execution facts must be durably represented or recoverable from authoritative external evidence.

⸻

83. No Hidden Side Effects

Durable execution must account for consequential side effects.

If an Action Contract causes:

TRANSFER_FUNDS

and also contractually requires:

AUDIT_RECORD
NOTIFICATION

those semantics must be represented by the Action Contract or explicit Action Graph nodes.

Durable Execution must not create unrecorded consequential operations.

⸻

84. Execution Boundary

The canonical execution boundary is:

Trust
   ↓
Action Graph
   ↓
Action Contract
   ↓
Execution Consumer
   ↓
External System

Durable Execution sits within the execution architecture:

Action Contract
      ↓
Durable Execution
      ↓
Consumer
      ↓
External System

Its role is to make the progression through execution durable and recoverable.

It does not replace the consumer or the external system.

⸻

85. Canonical Durable Execution Lifecycle

The conceptual lifecycle is:

Executable Action Graph
        ↓
Execution Created
        ↓
Action Ready
        ↓
Action Started
        ↓
External Operation
        │
        ├───────────────┐
        ▼               ▼
   Known Result     Unknown Result
        │               │
        ▼               ▼
   State Update     Reconciliation
        │               │
        └───────┬───────┘
                ▼
        Durable State
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
     Resume   Wait     Complete
        │
        ▼
     Outcome

At any point, execution may require:

WAIT
RETRY
RECONCILE
ESCALATE
COMPENSATE
BLOCK
FAIL
CANCEL

only where those transitions are explicitly defined.

⸻

86. Canonical Recovery Flow

The canonical recovery process is:

Process / Worker Failure
          ↓
Durable Execution State
          ↓
Recover Execution Identity
          ↓
Recover Graph + Contract Versions
          ↓
Recover Action State
          ↓
Determine Last Known State
          ↓
Evaluate External Evidence
          ↓
Apply Recovery Semantics
          ↓
Resume / Reconcile / Retry / Wait / Fail

Recovery must not silently create a new Intent, new graph, or new authority context.

⸻

87. Fundamental Recovery Principle

The most important durable execution distinction is:

What Noema knows
        ≠
What the external system did

For example:

Noema:
request submitted
Network:
connection lost
Provider:
operation may have completed

The resulting execution state may be:

UNKNOWN

until authoritative evidence resolves it.

Durable Execution exists partly to preserve this uncertainty rather than destroying it through an unjustified assumption.

⸻

88. Durable Execution Invariants

Invariant 1

Execution state required for recovery must survive process termination.

Invariant 2

Process failure must not automatically be interpreted as Action failure.

Invariant 3

Unknown external outcomes must remain explicitly unknown until resolved.

Invariant 4

Retries must respect Action Contract and idempotency semantics.

Invariant 5

A retry must not silently create a new logical Action execution.

Invariant 6

Durable execution state must remain associated with the correct Intent and Action Graph versions.

Invariant 7

Recovery must not silently become arbitrary replanning.

Invariant 8

Durable execution does not grant authorization.

Invariant 9

External systems remain authoritative for their business state.

Invariant 10

Execution state and Trust state are separate dimensions.

Invariant 11

Waiting must be durable when execution can outlive a worker process.

Invariant 12

Human approvals and external events required for execution must be durably associated with the correct execution.

Invariant 13

Material execution transitions must be reconstructible.

Invariant 14

Exactly-once external side effects must not be assumed without supporting contract semantics.

Invariant 15

Partial execution must remain observable at Action level.

Invariant 16

Compensation must be explicit and must not be treated as automatic rollback.

Invariant 17

A stale execution must not silently bypass renewed Trust, authorization, policy, or contract requirements.

Invariant 18

Durable state must not depend on hidden worker memory for material execution facts.

Invariant 19

Recovery must distinguish known failure from unknown external outcome.

Invariant 20

Durability preserves execution state; it does not establish semantic meaning, authorization, or business truth.

⸻

89. Canonical Mental Model

Durable Execution can be reduced to five questions:

1. What execution are we performing?
2. What has durably happened?
3. What remains unresolved or incomplete?
4. What does the applicable Action Contract permit us to do next?
5. What evidence is required before execution can safely continue or complete?

This produces:

Executable Graph
      ↓
Execution Identity
      ↓
Durable State
      ↓
External Effect
      ↓
Observed / Reconciled State
      ↓
Recovery or Continuation
      ↓
Outcome

⸻

90. Relationship to the Noema Architecture

The broader architecture becomes:

                         HUMAN
                           │
                           ▼
                        INTENT
                           │
                           ▼
                    INTERPRETATION
                           │
                           ▼
                       RESOLUTION
                           │
                           ▼
                      VALIDATION
                           │
                           ▼
                         TRUST
                           │
                           ▼
                     ACTION GRAPH
                           │
                    ┌──────┴──────┐
                    ▼             ▼
             ACTION CONTRACTS  DEPENDENCIES
                    │             │
                    └──────┬──────┘
                           ▼
                  DURABLE EXECUTION
                           │
                           ▼
                  EXECUTION CONSUMER
                           │
                           ▼
                  EXTERNAL SYSTEMS
                           │
                           ▼
                       OUTCOME

Each layer has a distinct responsibility.

⸻

91. The Fundamental Boundary

Durable Execution sits at the boundary between:

The execution process may be interrupted

and:

The execution state must remain recoverable.

Therefore:

Execution
   ↓
Durable State
   ↓
Recovery
   ↓
Continuation / Reconciliation
   ↓
Outcome

The fundamental invariant is:

Noema must never require the survival of a particular worker process in order to preserve the authoritative state of an execution.

⸻

92. Final Definition

Durable Execution is Noema’s architectural mechanism for preserving, recovering, and advancing execution state across process failure, interruption, waiting, retries, uncertain external outcomes, and long-running execution.

It ensures that:

* execution identity persists
* Action state persists
* execution transitions are reconstructible
* retries respect idempotency
* unknown outcomes remain unknown until resolved
* external state remains authoritative
* waiting survives worker termination
* recovery does not become arbitrary replanning
* partial execution remains explicit
* material execution history remains auditable

Its central invariant is:

Noema does not equate process execution with execution truth. It durably records what is known, preserves what is unknown, and recovers execution according to explicit Action Graph, Action Contract, Trust, and external-system semantics.

The architectural boundary is therefore:

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
External Execution
   ↓
Observed Outcome

Durable Execution preserves the state of what Noema is doing. It does not itself establish what Noema is authorized to do, what the Actor intended, or what an external system ultimately did.