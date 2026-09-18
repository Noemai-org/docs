Execution API

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/execution-api.md

⸻

1. Definition

The Execution API is the interface through which Noema exposes, coordinates, and observes the execution of an executable Action across execution boundaries.

It defines how an executable Action moves from:

READY
  ↓
EXECUTION
  ↓
EVIDENCE
  ↓
POSTCONDITIONS
  ↓
OUTCOME

The Execution API is concerned with execution mechanics and execution state, not with determining what the user intended.

⸻

2. Purpose

The Execution API provides a stable interface for:

* starting execution
* delivering Actions to executors
* acknowledging execution ownership
* tracking execution attempts
* reporting execution results
* reporting failures
* requesting retries
* handling timeouts
* entering reconciliation
* observing execution state
* recording execution evidence
* completing execution
* coordinating compensation where required

⸻

3. Core Principle

The Execution API coordinates execution without becoming the authority for Intent, enterprise business state, or policy.

The API operates on an already-resolved Action.

Intent
   ↓
Executable Intent
   ↓
Trust
   ↓
Action
   ↓
Execution API
   ↓
Executor

The Execution API should not need to determine:

"What did the user mean?"

That has already been resolved upstream.

⸻

4. Execution Boundary

The conceptual boundary is:

                 NOEMA
                   │
             Action Contract
                   │
                   ▼
             Execution API
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       Executor  Worker   Consumer
          │        │        │
          └────────┼────────┘
                   ▼
             Enterprise System

The Execution API provides the coordination boundary between Noema’s execution state and the systems that perform the actual work.

⸻

5. Execution Is Not Intent

This distinction is fundamental.

Intent:
"Replace my lost card."
Action:
issue_replacement_card(card_123)
Execution:
invoke card service to issue replacement card.

The Execution API operates at the third layer.

⸻

6. Execution Is Not Planning

Planning determines:

what sequence of operations should occur

Execution determines:

perform the selected operation

Therefore:

Planning
   ↓
Execution Plan
   ↓
Execution API

The Execution API should not independently invent an execution plan unless explicitly delegated that responsibility by the relevant contract.

⸻

7. Execution Is Not Trust

Trust determines:

may this Action execute?

Execution determines:

how is the Action with a Trust outcome of EXECUTE carried out?

Therefore:

Trust
  ↓
EXECUTE decision
  ↓
Action READY
  ↓
Execution API

The Execution API must not become a policy bypass.

An Action that has not received a Trust outcome of EXECUTE must not enter execution.

⸻

8. Execution Identity

Every execution should have a stable identity.

Conceptually:

execution_id

Example:

exe_01JXYZ...

The execution identity represents a particular execution lifecycle associated with an Action.

⸻

9. Action Identity vs Execution Identity

These are distinct.

action_id
    │
    ├── execution_id_1
    │
    └── execution_id_2

An Action may have more than one execution lifecycle where the execution model permits it.

⸻

10. Attempt Identity

An execution may contain multiple attempts.

Action
  ↓
Execution
  ├── Attempt 1
  ├── Attempt 2
  └── Attempt 3

Each attempt should have a stable identity:

attempt_id

This allows Noema to distinguish:

same Action
same Execution
different attempt

⸻

11. Why Attempt Identity Matters

Suppose an executor times out:

attempt_1 → UNKNOWN

Noema may later perform:

attempt_2 → reconciliation

Without attempt identity, the execution history becomes ambiguous.

⸻

12. Execution Lifecycle

The canonical lifecycle should align with execution/execution-model.md.

Conceptually:

READY
  ↓
DISPATCHING
  ↓
DISPATCHED
  ↓
ACKNOWLEDGED
  ↓
EXECUTING
  ↓
SUCCEEDED

Alternative paths include:

FAILED
UNKNOWN
TIMED_OUT
RETRYING
BLOCKED
CANCELLED
RECONCILING
COMPENSATING
HUMAN_INTERVENTION_REQUIRED

The exact state machine remains defined by the Execution domain.

⸻

13. Starting Execution

Conceptually:

POST /executions

creates or begins an execution for an Action that has received a Trust outcome of EXECUTE.

Example:

{
  "action_id": "act_123",
  "contract": "issue_replacement_card@1.2"
}

The exact transport schema is implementation-specific.

⸻

14. Execution Creation vs Execution Start

These may be separate semantic operations.

Execution Created
      ↓
Execution Ready
      ↓
Execution Started

This distinction allows scheduling, queuing, and delayed execution.

⸻

15. Dispatch

Noema may dispatch an execution to an executor.

Noema
  ↓
Execution API
  ↓
Executor

The executor receives the execution contract and required context.

⸻

16. Execution Envelope

A conceptual execution envelope:

{
  "execution_id": "exe_123",
  "attempt_id": "att_001",
  "action_id": "act_456",
  "contract": {
    "name": "issue_replacement_card",
    "version": "1.2"
  },
  "inputs": {},
  "context": {},
  "deadline": "..."
}

This is illustrative rather than the finalized wire schema.

⸻

17. Contract Authority

The Action Contract remains authoritative for execution semantics.

The Execution API must not allow an executor to modify:

required inputs
preconditions
authorization requirements
postconditions
retry semantics
compensation semantics

unless the contract explicitly permits such variation.

⸻

18. Executor

An Executor is the system responsible for performing the actual operation.

For example:

Noema
   ↓
Executor
   ↓
Payment Provider

The executor may be:

internal service
enterprise API
external provider
worker
integration adapter
human operator

depending on the Action Contract.

⸻

19. Execution Adapter

Noema may use adapters to translate canonical Actions into provider-specific operations.

Canonical Action
       ↓
Execution Adapter
       ↓
Provider API

The adapter should preserve the Action’s semantic contract.

⸻

20. Executor Ownership

The Execution API should make execution ownership explicit.

After dispatch:

Noema
   ↓
Executor

the executor may acknowledge:

execution accepted

This means:

"I have accepted responsibility for this attempt."

It does not mean:

"The Action succeeded."

⸻

21. Acknowledgement

Conceptually:

POST /executions/{id}/acknowledge

The acknowledgement establishes delivery/ownership.

It should not establish an Outcome.

⸻

22. Execution Start

Once the executor begins actual work:

execution.started

should be recorded.

This distinguishes:

dispatched

from:

actually executing

which is important for timeout and recovery semantics.

⸻

23. Execution Result

An executor eventually reports a result.

Conceptually:

POST /executions/{id}/result

Example:

{
  "status": "SUCCEEDED",
  "result": {
    "card_id": "card_789"
  },
  "evidence": []
}

The result is an execution report.

It is not automatically the final Outcome.

⸻

24. Execution Result vs Outcome

This distinction is critical.

Executor:
"Card created."
        ↓
Execution Result
        ↓
Noema evaluates:
postconditions
evidence
contract
context
        ↓
Outcome established

The executor’s statement is an observation from an execution participant.

Noema establishes the canonical Outcome according to its Trust and Execution semantics.

⸻

25. Evidence

Execution results may include evidence.

Examples:

provider response
provider event ID
resource version
transaction reference
execution timestamp
resource state

Evidence should be attributable to the source that produced it.

⸻

26. Execution Evidence

Conceptually:

{
  "evidence": [
    {
      "type": "provider_confirmation",
      "source": "card-service",
      "reference": "evt_789"
    }
  ]
}

Noema can then evaluate whether the evidence satisfies the Action’s postconditions.

⸻

27. Failure

Executors must be able to report structured failures.

Example:

{
  "status": "FAILED",
  "failure": {
    "code": "PROVIDER_UNAVAILABLE",
    "class": "TRANSIENT"
  }
}

Failure classification is important because it determines recovery behavior.

⸻

28. Failure Classes

A canonical classification may include:

VALIDATION_FAILURE
AUTHORIZATION_FAILURE
PRECONDITION_FAILURE
TRANSIENT_FAILURE
PERMANENT_FAILURE
TIMEOUT
UNKNOWN
CONFLICT
PROVIDER_FAILURE
INTERNAL_FAILURE

The exact taxonomy should remain aligned with execution/failure.md.

⸻

29. Failure Does Not Always Mean Retry

A failed execution should not automatically retry.

The retry decision depends on:

failure class
retry policy
attempt count
idempotency
risk
current context
contract

The Execution API exposes and coordinates this decision; it does not blindly perform it.

⸻

30. Retry

Conceptually:

POST /executions/{id}/retry

may request another attempt.

But:

A retry request is subject to the Action Contract, Trust policy, retry policy, and current execution state.

It is not an unconditional command to repeat an external side effect.

⸻

31. Retry and Attempt Identity

A retry creates a new attempt:

execution_123
 ├── attempt_1
 └── attempt_2

It should not overwrite the history of attempt 1.

⸻

32. Retry and Context

A retry may require fresh context.

For example:

Attempt 1:
authorization = valid
Attempt 2:
authorization = revoked

The second attempt cannot blindly inherit the first attempt’s authorization context.

⸻

33. Retry and Preconditions

Before retrying, relevant preconditions may need to be re-evaluated.

Example:

attempt_1
   ↓
failed
   ↓
context changed
   ↓
preconditions re-evaluated
   ↓
attempt_2

This prevents retries from executing against obsolete assumptions.

⸻

34. Idempotency

Execution APIs must distinguish:

logical Action idempotency

from:

execution attempt identity

A retry should not accidentally create a new logical Action.

⸻

35. Exactly-Once Effects

The Execution API should not promise universal exactly-once execution.

Instead, safe execution relies on:

idempotency
deduplication
provider guarantees
execution identity
reconciliation
compensation

where applicable.

⸻

36. Unknown Execution

A timeout or connection failure can produce:

UNKNOWN

rather than:

FAILED

Example:

Noema → Provider
          ↓
       operation
          ↓
      connection lost

Noema cannot know whether the provider executed the operation.

The correct state may therefore be:

UNKNOWN

⸻

37. Unknown Is Not Failure

This is a core execution invariant.

FAILED

means:

Noema has sufficient evidence that the operation failed.
UNKNOWN

means:

Noema cannot establish whether the operation occurred.

The recovery strategies are different.

⸻

38. Reconciliation

Unknown execution may trigger reconciliation.

UNKNOWN
   ↓
RECONCILING
   ↓
query authoritative provider
   ↓
observe state
   ↓
establish result

The Execution API should support this lifecycle.

⸻

39. Reconciliation Interface

Conceptually:

POST /executions/{id}/reconcile

The operation means:

"Attempt to establish the actual external state."

It does not mean:

"Run the original Action again."

⸻

40. Cancellation

An execution may be cancellable before or during execution.

Conceptually:

POST /executions/{id}/cancel

But cancellation is only possible where the execution contract permits it.

⸻

41. Cancellation vs Compensation

These are different.

Cancellation:

prevent execution from continuing

Compensation:

reverse or offset an effect that already occurred

Example:

payment initiated
     ↓
cannot cancel
     ↓
compensation/refund

The Execution API must preserve this distinction.

⸻

42. Compensation

Some Actions have compensating operations.

Example:

create_resource
      ↓
compensate:
delete_resource

The compensating Action must itself obey:

Trust
Policy
Authorization
Preconditions
Execution

Compensation is not a magical rollback.

⸻

43. Human Intervention

Some execution failures cannot safely be resolved automatically.

Example:

provider state uncertain

may result in:

HUMAN_INTERVENTION_REQUIRED

The API should expose:

reason
required decision
affected Action
execution state
evidence

where appropriate.

⸻

44. Human Intervention Is a State

Human intervention should not be represented merely as:

error = true

It is a legitimate execution state.

EXECUTING
   ↓
INTERVENTION_REQUIRED
   ↓
APPROVED / REJECTED / RESOLVED

⸻

45. Execution Deadlines

Executions may have deadlines.

Example:

deadline = 2026-08-27T17:00:00Z

The Execution API should expose deadline state where relevant.

Deadline expiration must not automatically imply external failure.

⸻

46. Timeout

A timeout means:

Noema or executor stopped waiting within the defined time boundary.

It does not necessarily establish:

operation did not happen

Therefore timeout may transition to:

UNKNOWN

depending on the Action Contract.

⸻

47. Execution Lease

For distributed workers, execution ownership may use a lease.

Conceptually:

Executor A
   ↓
owns execution for 30 seconds

If the lease expires:

Noema
   ↓
determine whether another executor may continue

This prevents multiple workers from unknowingly executing the same attempt.

⸻

48. Execution Heartbeat

Long-running executions may provide heartbeats:

execution.heartbeat

Heartbeats indicate:

executor is alive

They do not necessarily indicate:

business operation succeeded

⸻

49. Heartbeat Timeout

Missing heartbeats may indicate:

executor failure
network partition
process crash

but should not automatically prove that the external Action failed.

Again:

executor unavailable
≠
business operation failed

⸻

50. Concurrency

The Execution API must prevent conflicting attempts where the Action Contract requires exclusive execution.

For example:

Action A
 ├── attempt 1
 └── attempt 2

may be unsafe if both can reach the provider.

Execution coordination should therefore support:

locks
leases
version checks
idempotency keys
provider request IDs

where necessary.

⸻

51. Execution Locking

Where required:

Action
   ↓
exclusive execution lease
   ↓
Attempt

Only the current owner may execute the attempt.

⸻

52. Execution Fencing

Fencing prevents an expired worker from continuing to operate after another worker has taken ownership.

Conceptually:

Worker A → lease 1
lease expires
Worker B → lease 2
Worker A tries operation
        ↓
rejected by fencing

This is particularly important for long-running distributed execution.

⸻

53. Execution Ordering

For dependent Actions:

A
 ↓
B
 ↓
C

the Execution API should preserve the ordering constraints established by the execution plan.

It should not execute B before A’s required postconditions are satisfied.

⸻

54. Parallel Execution

Where an execution plan permits:

        ┌── B ──┐
A ──────┤       ├── D
        └── C ──┘

the Execution API may coordinate parallel execution.

Parallelism must remain bounded by:

dependencies
resource constraints
policy
risk
provider limits

⸻

55. Execution Dependencies

An execution may depend on:

precondition
previous Action
previous execution
external state
human approval
provider response

These dependencies must be explicit.

⸻

56. Execution State Observation

Consumers should be able to query:

GET /executions/{execution_id}

and observe:

status
attempt
timestamps
executor
failure
evidence
reconciliation state
outcome reference

⸻

57. Execution History

The API should preserve execution history rather than exposing only the latest status.

Example:

execution_123
attempt_1
  STARTED
  TIMEOUT
  UNKNOWN
attempt_2
  STARTED
  SUCCEEDED

This history is important for audit and diagnosis.

⸻

58. Execution Timeline

A conceptual timeline:

10:00 Action ready
10:00 Execution created
10:01 Dispatched
10:01 Acknowledged
10:02 Started
10:05 Timeout
10:05 Unknown
10:07 Reconciliation started
10:08 Provider state observed
10:08 Outcome established

The API should make this reconstructable.

⸻

59. Execution Events

Execution state changes should emit Events through the Event Model.

Examples:

execution.created
execution.dispatched
execution.acknowledged
execution.started
execution.failed
execution.unknown
execution.retrying
execution.reconciling
execution.completed

The Execution API and Event Model therefore complement one another.

⸻

60. Execution API vs Event Model

The distinction is:

Execution API
    ↓
query / coordinate execution

while:

Event Model
    ↓
publish / consume execution occurrences

One is an execution interface.

The other is an observation model.

⸻

61. Execution API vs Action API

The Action API represents the external lifecycle of the logical Action.

The Execution API represents the execution lifecycle underneath it.

Action API
    ↓
Action
    │
    └── Execution API
             ↓
          Execution
             ↓
          Attempts

⸻

62. Execution API vs Context API

The Context API supplies contextual information.

The Execution API consumes the context required for execution.

Context API
    ↓
Context
    ↓
Execution API

Context should not be embedded indiscriminately into every execution request.

⸻

63. Execution API and Trust

Before execution begins, Trust may establish:

authorized = true
policy = allowed
risk = acceptable
preconditions = satisfied

The Execution API relies on those decisions.

However, if execution conditions materially change, the execution may require re-evaluation.

⸻

64. Trust Re-Evaluation

For long-running Actions, Noema may need to re-evaluate:

authorization
policy
risk
context
preconditions

before a consequential execution step.

This prevents a stale authorization decision from remaining valid indefinitely.

⸻

65. Execution API and Policy

Policy may constrain:

who executes
when execution may occur
which provider may be used
maximum attempts
maximum duration
approval requirements
compensation requirements

The Execution API must enforce or delegate these constraints rather than bypass them.

⸻

66. Execution API and Risk

Risk may determine execution strategy.

For example:

low risk
→ automatic execution
high risk
→ approval required

The Execution API should represent the resulting execution state.

It should not independently redefine risk policy.

⸻

67. Execution API and Postconditions

After execution, Noema evaluates the expected postconditions.

Execution Result
      ↓
Evidence
      ↓
Postcondition Evaluation
      ↓
Outcome

The Execution API must preserve the information required for that evaluation.

⸻

68. Execution API and Outcome

An execution can finish without an Outcome being immediately established.

For example:

execution completed
      ↓
provider event pending
      ↓
Outcome pending

Therefore:

Execution completion
≠
Outcome establishment

where the Action Contract requires additional evidence.

⸻

69. Execution API and Recovery

The Execution API must support recovery after:

worker crash
Noema crash
provider outage
network partition
message duplication
message loss
process restart

Stable identities and durable execution state are therefore foundational.

⸻

70. Recovery After Worker Crash

Example:

attempt_1
   ↓
worker crashes
   ↓
lease expires
   ↓
Noema evaluates state
   ↓
resume / retry / reconcile

The system should not simply assume the attempt failed.

⸻

71. Recovery After Noema Crash

After restart:

Action
Execution
Attempt
Context
Events

must remain recoverable from durable state.

Noema should not rely on in-memory worker state to establish execution truth.

⸻

72. Recovery After Provider Failure

If a provider becomes unavailable:

execution
   ↓
provider unavailable

the API may transition to:

RETRYING

or:

UNKNOWN

depending on what can be established.

⸻

73. Execution API and Distributed Systems

The API assumes distributed execution characteristics:

latency
partial failure
duplicate delivery
network partitions
out-of-order events
process crashes
stale state

It must therefore be designed around explicit state and evidence rather than optimistic assumptions.

⸻

74. Execution API and Exactly-Once Illusion

The API must not claim:

"this operation will execute exactly once."

unless the underlying system can actually guarantee the relevant property.

Instead, Noema should distinguish:

delivery semantics
execution semantics
effect semantics

These are separate.

⸻

75. Delivery vs Execution vs Effect

For example:

Delivered once
   ≠
Executed once
   ≠
Effect occurred once

The Action Contract must define the relevant safety requirements.

⸻

76. Execution Result Integrity

Execution results must be attributable to the executor and execution attempt that produced them.

A result should not be accepted if:

execution_id mismatch
attempt_id mismatch
contract mismatch
tenant mismatch
expired lease

where those checks are required.

⸻

77. Stale Result Protection

Suppose:

attempt_1

loses its lease.

Then:

attempt_2

begins.

If attempt 1 later reports:

SUCCESS

Noema must not blindly overwrite attempt 2’s state.

Execution identity and fencing prevent stale workers from corrupting the execution record.

⸻

78. Execution API and Multi-Tenancy

Every execution must remain scoped to its tenant.

A consumer must not be able to:

read another tenant's execution
modify another tenant's execution
submit results for another tenant

⸻

79. Execution API Security

The API should authenticate:

caller
executor
consumer

and authorize operations according to role and contract.

Different actors may have different permissions:

submit
execute
observe
cancel
retry
reconcile
approve

⸻

80. Execution API Auditability

The API should make it possible to reconstruct:

who started execution
which Action was executed
which contract governed it
which executor handled it
which attempts occurred
which evidence was returned
which failures occurred
which policies affected recovery
how the final Outcome was established

⸻

81. Execution API and Audit Trail

A canonical execution trail:

Action
  ↓
Execution Created
  ↓
Dispatched
  ↓
Acknowledged
  ↓
Started
  ↓
Attempt Result
  ↓
Evidence
  ↓
Postcondition Evaluation
  ↓
Outcome

with branches for:

failure
retry
unknown
reconciliation
compensation
human intervention

⸻

82. Execution API Resource Model

A conceptual Execution resource:

{
  "id": "exe_123",
  "action_id": "act_456",
  "status": "EXECUTING",
  "contract": {
    "name": "issue_replacement_card",
    "version": "1.2"
  },
  "attempt": {
    "id": "att_001",
    "number": 1
  },
  "executor": {
    "type": "service",
    "id": "card-executor"
  },
  "started_at": "..."
}

Again, this is a conceptual model rather than a finalized wire schema.

⸻

83. Canonical Operations

The Execution API may conceptually support:

Create Execution
Get Execution
List Executions
Start Execution
Acknowledge Execution
Report Execution Result
Report Failure
Retry Execution
Cancel Execution
Reconcile Execution
Submit Evidence
Get Execution History

Not every operation needs to be publicly exposed.

⸻

84. Commands Are Requests

Operations such as:

retry
cancel
reconcile

should be interpreted as requests subject to execution policy.

They do not override:

Trust
Authorization
Policy
Preconditions
Idempotency
Risk

⸻

85. Synchronous Execution

Some executions may complete within the API request.

Conceptually:

POST /executions
      ↓
execute
      ↓
result

This is acceptable for short-running operations.

But synchronous transport must not alter the underlying execution semantics.

⸻

86. Asynchronous Execution

Long-running executions should be asynchronous.

POST /executions
      ↓
202 Accepted
      ↓
execution_id
      ↓
GET /executions/{id}

or through event delivery.

⸻

87. Streaming Execution

For long-running operations, the API may eventually support execution streams.

For example:

execution.started
execution.progressed
execution.waiting
execution.completed

Progress events should not be confused with successful completion.

⸻

88. Progress

Progress may be exposed where useful:

{
  "progress": {
    "completed_steps": 3,
    "total_steps": 5
  }
}

Progress is informational unless the Action Contract gives it semantic meaning.

⸻

89. Execution Plan Visibility

Consumers may or may not see the internal execution plan.

The default should be:

logical Action
+
observable execution state

rather than exposing internal orchestration details unnecessarily.

⸻

90. Internal Execution Steps

Where a plan contains:

step_1
step_2
step_3

the Execution API may expose them if the integration contract requires step-level visibility.

Otherwise they remain implementation details.

⸻

91. Execution API and Compensation

If execution partially succeeds:

step_1 → SUCCESS
step_2 → SUCCESS
step_3 → FAILED

the API should expose the resulting execution state.

Recovery may then involve:

retry
continue
compensate
human intervention

according to the execution contract.

⸻

92. Partial Success

An execution should not necessarily be reduced to:

SUCCESS

or:

FAILED

when intermediate effects matter.

A richer execution state may be required:

PARTIALLY_COMPLETED

followed by:

COMPENSATING

or:

HUMAN_INTERVENTION_REQUIRED

⸻

93. Irreversible Effects

The Execution API must distinguish reversible from irreversible operations.

For irreversible Actions:

cancel
retry

require greater caution.

The API should defer to the Action Contract and Trust Engine.

⸻

94. External Side Effects

The Execution API exists specifically at the boundary where Noema may cause external side effects.

Examples:

send payment
create account
issue card
delete resource
send message
provision infrastructure

Therefore execution safety is a first-class concern.

⸻

95. Side-Effect Safety

Before allowing execution, Noema should establish:

Action identity
Contract
Authorization
Preconditions
Context
Idempotency
Execution ownership

The Execution API coordinates these requirements rather than bypassing them.

⸻

96. Execution API and Context Refresh

Before a consequential attempt, the executor may require fresh context.

For example:

current balance
current authorization
resource version
provider availability

The Execution API may request or trigger context refresh according to contract.

⸻

97. Execution API and Event Model

A typical lifecycle:

Execution API
      ↓
execution.started
      ↓
Executor
      ↓
execution.result
      ↓
Evidence
      ↓
Postcondition evaluation
      ↓
execution.completed
      ↓
outcome.established

Events provide the observable history around API operations.

⸻

98. Execution API and Context API

The relationship is:

Context API
      ↓
current execution context
      ↓
Execution API
      ↓
executor

Context may be refreshed between attempts.

⸻

99. Execution API and Action API

The relationship is:

Action API
    ↓
logical Action
    ↓
Execution API
    ↓
execution
    ↓
attempts

Action-level consumers should not need to manage execution attempts directly unless their integration requires it.

⸻

100. Execution API and Trust Engine

The Trust Engine remains the authority for:

authorization
risk
policy
ambiguity
determinism

The Execution API remains the authority for:

execution coordination
execution state
attempt lifecycle
execution recovery

These responsibilities should not collapse into one layer.

⸻

101. Execution API Invariants

Invariant 1

An Execution always belongs to a logical Action.

Invariant 2

Action identity and Execution identity are distinct.

Invariant 3

Execution identity and Attempt identity are distinct.

Invariant 4

An executor cannot redefine the meaning of the Action Contract.

Invariant 5

Execution cannot bypass Trust or Policy.

Invariant 6

Execution results are not automatically Outcomes.

Invariant 7

Unknown execution state must remain distinct from confirmed failure.

Invariant 8

Retries create distinguishable execution attempts.

Invariant 9

Retries must be evaluated against current context and policy.

Invariant 10

Stale execution attempts must not overwrite newer execution state.

Invariant 11

Execution cancellation is distinct from compensation.

Invariant 12

Timeout does not necessarily imply external failure.

Invariant 13

Execution must support recovery from distributed-system failures.

Invariant 14

Execution state must be durably reconstructable.

Invariant 15

Execution results must be attributable to the relevant executor and attempt.

Invariant 16

Execution must respect tenant boundaries.

Invariant 17

Execution history must remain auditable.

Invariant 18

Exactly-once effects must not be assumed merely from API or transport semantics.

Invariant 19

Reconciliation must be available where execution state can become uncertain.

Invariant 20

The Execution API must not silently convert uncertainty into success or failure.

⸻

102. Canonical Mental Model

                       ACTION
                         │
                         ▼
                ┌─────────────────┐
                │  TRUST / POLICY │
                └────────┬────────┘
                         │
                         ▼
                       READY
                         │
                         ▼
                 EXECUTION API
                         │
                  ┌──────┴──────┐
                  ▼             ▼
              Executor       Context
                  │             │
                  ▼             │
              Attempt           │
                  │             │
          ┌───────┼─────────────┘
          ▼       ▼
       Result   Failure
          │       │
          └───┬───┘
              ▼
           Evidence
              │
              ▼
       Postcondition Check
              │
       ┌──────┴──────┐
       ▼             ▼
    Outcome       Reconcile

⸻

103. Final Definition

The Execution API is Noema’s execution coordination boundary. It provides the interfaces through which authorized Actions are dispatched, executed, observed, retried, reconciled, cancelled, or compensated while preserving explicit execution identity, attempt history, evidence, uncertainty, and recovery semantics.

The core principle is:

The Execution API does not decide what should happen; it safely coordinates what has already been determined to be executable.

And critically:

Execution completion is not synonymous with Outcome establishment. Noema must retain the distinction between an executor’s result, observed evidence, verified postconditions, and the final Outcome.