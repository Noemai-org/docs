Execution Loop

Status: Foundational
Version: 0.1
Domain: Loops
Canonical Path: loops/execution-loop.md

⸻

1. Definition

The Execution Loop is Noema’s controlled runtime lifecycle for advancing an executable Action Graph through Action evaluation, contract enforcement, execution, outcome observation, failure handling, and completion.

The Execution Loop is responsible for determining what executable work is currently eligible to advance, invoking the applicable execution mechanism, observing the result, and transitioning execution state according to explicit semantics.

It does not:

* establish what the Actor intends
* resolve semantic ambiguity
* establish Trust
* grant authorization
* define business-state ownership
* invent Actions
* invent recovery behavior
* treat model output as execution authority

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
Execution Loop
  ↓
External Systems
  ↓
Observed Outcome

The Execution Loop therefore sits at the boundary between explicit executable structure and actual runtime effects.

⸻

2. Core Principle

Noema must not treat execution as a single opaque function call.

Execution is a stateful lifecycle in which:

1. an executable Action becomes eligible
2. its dependencies are evaluated
3. its contract is resolved
4. execution-time conditions are checked
5. the Action is dispatched
6. the external result is observed
7. the Action state is transitioned
8. downstream dependencies are evaluated
9. failures, retries, compensation, waiting, or escalation are handled explicitly
10. completion is established

Conceptually:

Executable Graph
      ↓
Eligibility
      ↓
Contract
      ↓
Execution
      ↓
Observation
      ↓
State Transition
      ↓
Graph Advancement

The loop must be explicit and inspectable.

⸻

3. Execution Loop Boundary

The Execution Loop begins only after the relevant execution prerequisites have been satisfied.

Resolved Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Contract Binding
      ↓
┌──────────────────────┐
│   Execution Loop     │
└──────────┬───────────┘
           ↓
       Execution
           ↓
        Outcome

The loop must not become an implicit replacement for upstream lifecycle stages.

In particular:

Execution Loop ≠ Trust Engine
Execution Loop ≠ Intent Engine
Execution Loop ≠ Action Graph Builder
Execution Loop ≠ Policy Engine
Execution Loop ≠ Business System

⸻

4. Executable Graph Requirement

The Execution Loop operates on an Executable Action Graph, not merely a candidate graph.

A candidate graph may contain:

* unresolved dependencies
* unresolved capabilities
* unresolved contracts
* unresolved conditions
* incomplete inputs

Such a graph must not cross the execution boundary.

The required distinction is:

Candidate Graph
      ↓
Graph Validation
      ↓
Trust
      ↓
Contract Binding
      ↓
Executable Graph
      ↓
Execution Loop

⸻

5. Execution Unit

The primary unit of execution is an Action Graph node bound to an applicable Action Contract.

Conceptually:

ExecutionUnit {
    graph_id
    graph_version
    node_id
    action
    contract
    capability
    inputs
    preconditions
    execution_state
    attempt
    idempotency_key
    provenance
}

The exact schema belongs to the relevant architecture and contract specifications.

The Execution Loop must preserve the identity of the graph, node, Action, Contract, and execution attempt.

⸻

6. Execution Eligibility

An Action may enter execution only when its execution prerequisites are satisfied.

These may include:

* graph validity
* dependency satisfaction
* required inputs
* preconditions
* Trust requirements
* authorization requirements
* capability availability
* Action Contract validity
* resource availability
* approval requirements
* confirmation requirements
* temporal constraints
* atomicity constraints

Conceptually:

Action
  ↓
Dependencies satisfied?
  ↓
Inputs available?
  ↓
Contract valid?
  ↓
Execution conditions satisfied?
  ↓
READY

If a required condition is unknown, the Action must not be treated as ready merely because execution is desirable.

⸻

7. Dependency Evaluation

The Execution Loop evaluates dependencies before dispatch.

For example:

A → B

requires the loop to establish that the dependency represented by A has been satisfied according to the applicable graph semantics before B becomes executable.

Visual ordering alone is insufficient.

Dependencies must be evaluated from the explicit graph representation.

⸻

8. Action Readiness

An Action may transition to READY only when its required execution conditions are satisfied.

Conceptually:

NOT_READY
    ↓
dependencies satisfied
    ↓
preconditions satisfied
    ↓
READY

READY does not mean that execution has occurred.

It means the Action is eligible for dispatch under the currently established execution conditions.

⸻

9. Execution Dispatch

Once an Action is ready, the Execution Loop dispatches it through the applicable execution mechanism.

Conceptually:

READY
  ↓
DISPATCH
  ↓
EXECUTING

The dispatch mechanism may involve:

* API invocation
* message publication
* queue delivery
* service invocation
* workflow execution
* provider integration
* another explicitly defined execution mechanism

The mechanism is subordinate to the Action Contract.

⸻

10. Contract Enforcement

The Action Contract defines the executable interface and obligations associated with an Action.

The Execution Loop must enforce the applicable contract rather than independently inventing execution semantics.

The contract may define:

* required inputs
* permitted outputs
* preconditions
* authorization requirements
* idempotency
* timeout
* retryability
* failure classes
* side-effect semantics
* compensation
* confirmation requirements
* execution constraints

Conceptually:

Action Graph Node
      ↓
Action Contract
      ↓
Execution Consumer

⸻

11. Consumer Boundary

The execution consumer remains authoritative for execution-time conditions within its domain.

For example:

Noema:
Graph valid
Trust ready
Contract valid
Consumer:
Account no longer eligible

The consumer may reject execution.

The Execution Loop must record that result rather than treating the rejection as evidence that the graph could simply be ignored.

⸻

12. Execution-Time Revalidation

Conditions established earlier may change before execution.

Therefore, consequential Actions may require final execution-time checks.

Conceptually:

Validation
   ↓
Trust
   ↓
Graph
   ↓
Contract
   ↓
Execution-Time Check
   ↓
Execute

The Execution Loop must not assume that:

Condition at planning time
=
Condition at execution time

This is especially important for dynamic external business state.

⸻

13. Time-of-Check / Time-of-Use

The Execution Loop must account for TOCTOU conditions.

For example:

T1: Account = ACTIVE
T2: Graph validated
T3: Account = SUSPENDED
T4: Execute

The execution consumer may reject the Action.

This must be represented as an execution-time condition failure rather than silently treated as a successful execution.

⸻

14. Execution State

Execution state must remain distinct from Trust state and Intent state.

Conceptual Action states include:

NOT_READY
READY
EXECUTING
COMPLETED
FAILED
SKIPPED
BLOCKED
WAITING
UNKNOWN

Additional runtime states may exist where required.

The Execution Loop owns runtime transitions associated with actual execution.

⸻

15. State Transition Principle

Execution state may change only through defined runtime events and deterministic evaluation.

Examples include:

READY
  ↓
execution.started
  ↓
EXECUTING

and:

EXECUTING
  ↓
execution.completed
  ↓
COMPLETED

or:

EXECUTING
  ↓
execution.failed
  ↓
FAILED

The loop must not mutate state merely because a model proposes a different result.

⸻

16. Execution Attempt

Each execution attempt should be identifiable.

Conceptually:

Action:
PAYMENT_CREATE
Attempt 1:
FAILED — timeout
Attempt 2:
UNKNOWN — provider response unavailable

Attempt identity supports:

* retry accounting
* idempotency
* observability
* failure analysis
* auditability
* reconstruction

An attempt must not be confused with the Action itself.

⸻

17. Idempotency

The Execution Loop must respect Action Contract idempotency semantics.

Where an Action can produce consequential side effects, retries must not unintentionally duplicate those effects.

Conceptually:

Action
  ↓
Execution Attempt
  ↓
Uncertain Result
  ↓
Retry permitted?
  ↓
Same idempotent operation

The loop must not create a new semantic operation merely because a prior execution attempt produced an uncertain response.

⸻

18. Unknown Outcomes

Execution may produce an unknown outcome.

Example:

CREATE_PAYMENT
      ↓
network timeout
      ↓
provider state unknown

The Execution Loop must not automatically convert this into:

FAILED

if the external system may have performed the operation.

The state may instead become:

UNKNOWN

and require:

* status reconciliation
* authoritative lookup
* human intervention
* explicit recovery
* bounded retry where contractually safe

⸻

19. Success

An execution response does not automatically establish complete success.

The loop may need to establish:

* operation accepted
* operation completed
* expected postcondition observed
* required external state confirmed
* downstream conditions satisfied

Therefore:

Execution Response = SUCCESS

does not necessarily imply:

Intent Outcome = COMPLETED

⸻

20. Postcondition Verification

Where required by the Action Contract, the Execution Loop should verify expected postconditions.

Example:

REQUEST_REPLACEMENT
       ↓
provider response = accepted
       ↓
verify:
replacement_request.status = CREATED

The external system remains authoritative for the underlying business state.

Noema records the verification result.

⸻

21. Downstream Advancement

After an Action completes, the loop evaluates dependent nodes.

Example:

A
↓
B
↓
C

After:

A = COMPLETED

the loop evaluates whether B is now eligible.

Completion of one node must not cause downstream execution unless the explicit graph dependencies and conditions permit it.

⸻

22. Parallel Execution

Independent Actions may execute concurrently when parallelism is permitted.

Example:

        ┌── B ──┐
A ──────┤       ├── D
        └── C ──┘

The loop may execute:

B
C

in parallel if:

* their dependencies are satisfied
* their contracts permit concurrency
* resource constraints permit concurrency
* atomicity requirements permit concurrency
* shared-resource conflicts are absent or explicitly controlled

Parallelism is an execution optimization, not an assumption derived from graph appearance alone.

⸻

23. Sequential Execution

Where the graph establishes strict ordering:

A → B → C

the loop must preserve that ordering.

It must not reorder Actions merely because a different order appears faster.

Reordering is permissible only when the graph semantics and applicable contracts explicitly permit it.

⸻

24. Branch Evaluation

Conditional branches must be evaluated from explicit graph conditions.

Example:

CHECK_ELIGIBILITY
        ↓
    ┌───┴────┐
    ↓        ↓
 eligible  ineligible
    ↓        ↓
 RENEW      STOP

The Execution Loop must not select a branch using an unstated model assumption.

The condition must be represented and evaluated explicitly.

⸻

25. Branch Failure

If a branch condition cannot be established, the dependent branch must not be treated as satisfied.

For example:

eligible = UNKNOWN

does not mean:

eligible = TRUE

The resulting Action may become:

WAITING
BLOCKED
UNKNOWN

depending on the applicable semantics.

⸻

26. Convergence

When branches converge, the Execution Loop must establish the explicit convergence condition.

Example:

        ┌── B ──┐
A ──────┤       ├── D
        └── C ──┘

If D requires both B and C, then:

B = COMPLETED
C = COMPLETED
      ↓
D = READY

If one mandatory branch fails:

B = COMPLETED
C = FAILED

then D must not automatically execute.

⸻

27. Waiting

Execution may legitimately enter a waiting state.

Examples include:

* human approval
* Actor confirmation
* external asynchronous operation
* scheduled execution time
* resource availability
* provider callback
* reconciliation
* bounded retry delay

Waiting is not equivalent to failure.

Conceptually:

READY
  ↓
WAITING
  ↓
condition satisfied
  ↓
READY

⸻

28. Human Approval

Where approval is required:

ACTION
  ↓
WAIT_FOR_APPROVAL
  ↓
APPROVED
  ↓
EXECUTE

The Execution Loop must treat approval as an explicit event.

Approval does not eliminate the requirement to re-evaluate execution-time conditions.

⸻

29. Actor Confirmation

Where explicit Actor confirmation is required:

ACTION
  ↓
WAIT_FOR_CONFIRMATION
  ↓
CONFIRMED
  ↓
EXECUTE

The Execution Loop must not infer confirmation merely from:

* continued conversation
* silence
* a model confidence score
* an unrelated Actor response

Confirmation semantics must be explicitly defined.

⸻

30. Asynchronous Execution

An Action may not complete within the dispatch request.

Example:

SUBMIT_TRANSFER
      ↓
ACCEPTED
      ↓
WAITING_FOR_EXTERNAL_RESULT
      ↓
provider callback
      ↓
COMPLETED

The Execution Loop must support asynchronous completion where the Action Contract requires it.

Submission and completion must remain distinct states.

⸻

31. External Events

External systems may produce events required to advance execution.

Examples:

payment.completed
delivery.shipped
approval.granted
identity.verified
provider.callback.received

External events must be authenticated, correlated, and associated with the correct execution context according to the relevant system boundary.

The loop must not treat an arbitrary external message as proof of completion.

⸻

32. Event Correlation

Execution events should be correlated to:

* Intent
* Intent version
* graph
* graph version
* Action node
* execution attempt
* contract
* external operation

This permits reliable reconstruction of execution history.

⸻

33. Failure Handling

A failed Action must transition according to explicit failure semantics.

Possible outcomes include:

RETRY
COMPENSATE
BLOCK
SKIP
ESCALATE
FAIL_GRAPH
WAIT

The Execution Loop must not invent recovery behavior.

Failure semantics come from the graph, Action Contract, and applicable execution policies.

⸻

34. Retry

A retry is permitted only when the relevant semantics allow it.

The loop should consider:

* retryable failure class
* maximum attempts
* backoff
* timeout
* idempotency
* external system behavior
* graph atomicity
* resource constraints

Conceptually:

FAILED
  ↓
Retry permitted?
 ┌──────┴──────┐
 No            Yes
 ↓              ↓
FAILED        WAIT
                ↓
              RETRY

⸻

35. Bounded Retry

Retries must be bounded.

The Execution Loop must not permit an Action to retry indefinitely unless an explicit bounded execution construct defines otherwise.

A retry policy should establish:

maximum_attempts
timeout
backoff
retryable_failures
termination_behavior

When the bound is exhausted, the Action transitions according to the defined failure semantics.

⸻

36. Compensation

Compensation may be required after partial execution.

Example:

A → B → C

If:

A = COMPLETED
B = COMPLETED
C = FAILED

the graph may specify:

B_COMPENSATE
      ↓
A_COMPENSATE

Compensation is not assumed to be equivalent to rollback.

The external system may not support transactional reversal.

⸻

37. Compensation Execution

Compensating Actions must themselves be explicit.

They require:

* identity
* contract
* capability
* inputs
* dependencies
* execution semantics
* failure semantics
* observability

The loop must not invent a compensating Action because an earlier Action failed.

⸻

38. Partial Execution

Execution may terminate with only part of the graph completed.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The loop must preserve the individual node states.

It must not collapse the result into:

SUCCESS

nor necessarily into a generic:

FAILED

without preserving the partial execution state.

⸻

39. Graph-Level Outcome

The Execution Loop may produce aggregate execution states such as:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN

The exact aggregate state is determined by the applicable execution semantics.

Graph-level state must remain distinct from:

Trust State
Intent State
Individual Action State

⸻

40. Completion

The loop must explicitly determine when execution is complete.

Completion may require:

* all mandatory Actions completed
* required branches resolved
* required postconditions verified
* no mandatory Action remains pending
* no unresolved mandatory outcome exists
* required compensation completed
* required external outcomes observed

Therefore:

last dispatched Action returned successfully

does not necessarily mean:

graph completed

⸻

41. Graph Completion vs Intent Completion

Execution completion and Intent completion are related but distinct.

For example:

Graph:
COMPLETED

may establish that the requested operational work completed.

But the resulting Intent Outcome must still record what actually happened.

Conversely, an Intent may permit an operational graph to complete while an external postcondition remains unknown.

The relationship must be defined by the applicable Intent and execution semantics.

⸻

42. Execution Outcome

The loop produces execution evidence that contributes to the final Outcome.

An Outcome may include:

status
completed_actions
failed_actions
skipped_actions
pending_actions
unknown_actions
external_results
postcondition_results
errors
timestamps
provenance

The canonical Outcome model belongs to the relevant outcome specification.

⸻

43. Unknown Is a First-Class Result

The Execution Loop must preserve uncertainty.

Examples:

provider response unknown
external callback missing
postcondition cannot be verified
execution state cannot be reconciled

These conditions must not be silently transformed into:

FAILED

or:

COMPLETED

unless authoritative evidence establishes the corresponding state.

⸻

44. Reconciliation

Unknown execution states may require reconciliation.

Conceptually:

UNKNOWN
   ↓
Authoritative Status Query
   ↓
┌──────────────┬──────────────┐
↓              ↓              ↓
COMPLETED     FAILED        UNKNOWN

The reconciliation mechanism must be defined by the applicable Action Contract or execution architecture.

⸻

45. Stale Execution

An executable graph may become stale after construction.

Examples:

* capability revoked
* contract changed
* authorization changed
* policy changed
* resource changed
* external business state changed materially
* Intent changed

The Execution Loop must not silently execute a graph whose execution authority or material prerequisites have become invalid.

The appropriate response may be:

BLOCK
REVALIDATE
REPLAN
ESCALATE
FAIL

according to explicit semantics.

⸻

46. Material Change During Execution

A material change during execution may require the loop to pause or terminate advancement.

Conceptually:

Executing Graph v1
      ↓
Material Change
      ↓
Pause
      ↓
Revalidation
      ↓
Trust Re-evaluation
      ↓
Graph Revision

The loop must preserve the relationship between the old and new graph versions.

⸻

47. No Silent Graph Mutation

The Execution Loop must not rewrite the Action Graph in place merely because execution encountered difficulty.

If the graph changes materially:

Graph v1
   ↓
revision
   ↓
Graph v2

the transition must be explicit and auditable.

⸻

48. Replanning

Replanning may be required when the existing graph can no longer fulfill the Intent under current conditions.

For example:

Graph v1
  ↓
Capability unavailable
  ↓
Replanning
  ↓
Candidate Graph v2
  ↓
Validation
  ↓
Trust / Contract Evaluation
  ↓
Executable Graph v2

Replanning is not an excuse to bypass Trust or contract validation.

⸻

49. Execution Loop and Trust

Trust establishes whether execution may proceed.

The Execution Loop establishes how executable work advances.

Therefore:

Trust = execution eligibility
Execution Loop = runtime advancement

A failed Action does not necessarily mean the original Trust decision was invalid.

Example:

Trust = READY
Execution = FAILED

is a valid system state.

⸻

50. Trust Re-evaluation

A material change may require Trust re-evaluation during execution.

Examples:

* authorization revoked
* policy changed
* Intent changed
* approval expired
* execution window expired
* material context changed

The loop must honor the resulting Trust state.

It must not continue execution merely because an earlier Trust decision was READY.

⸻

51. Authorization

The Execution Loop does not grant authorization.

Authorization may be represented as:

Authorization Check
       ↓
Action

or as part of the Action Contract.

The loop verifies that applicable authorization requirements are satisfied.

It does not invent them.

⸻

52. Capability Binding

Every executable Action must resolve to an appropriate capability.

Conceptually:

Action
  ↓
Capability
  ↓
Contract
  ↓
Consumer

The Execution Loop must not execute an Action through an arbitrary capability merely because that capability appears technically capable of performing it.

Capability selection remains governed by the Action Graph and applicable contracts.

⸻

53. Resource Constraints

Execution may be constrained by:

* concurrency limits
* rate limits
* quotas
* locks
* capacity
* budgets
* external provider limits
* dependency resources

The loop must respect explicit resource constraints.

Resource unavailability may produce:

WAITING
BLOCKED
RETRY

depending on the applicable semantics.

⸻

54. Concurrency Control

Where Actions execute concurrently, the loop must ensure that concurrency does not violate:

* graph dependencies
* Action Contracts
* resource constraints
* atomicity
* ordering requirements
* external system semantics

The Execution Loop must prefer correctness over maximal parallelism.

⸻

55. Scheduling

The loop may schedule Actions for execution based on:

* readiness
* dependencies
* temporal constraints
* resource availability
* priority
* retry delays
* external events

Scheduling determines when an eligible Action is dispatched.

It does not determine whether the Actor is authorized to perform the Action.

⸻

56. Priority

Where multiple Actions are ready, an execution scheduler may select among them according to explicit scheduling policy.

Priority must not violate:

* dependency semantics
* ordering
* atomicity
* Action Contracts
* Trust
* authorization
* Intent constraints

Priority is an execution concern, not a semantic authority.

⸻

57. Execution Isolation

An Action execution should be attributable to its graph and execution context.

Execution isolation should prevent:

* one Intent from accidentally consuming another Intent’s state
* one graph version from mutating another
* one execution attempt from being mistaken for another
* unrelated external events from advancing an Action

Correlation and identity are therefore execution controls, not merely observability metadata.

⸻

58. Execution Context

The Execution Loop may maintain a runtime execution context containing:

execution_id
intent_id
intent_version
graph_id
graph_version
node_id
action
contract_id
capability_id
attempt
idempotency_key
timestamps
state

The exact schema remains subject to the canonical runtime model.

⸻

59. Context Must Not Become Authority

Execution context may contain information necessary to perform an Action.

It must not silently become a source of authorization.

For example:

execution_context.actor = user_123

does not itself establish:

user_123 is authorized

Authorization remains governed by the applicable Trust and contract mechanisms.

⸻

60. External Side Effects

The Execution Loop is the point at which Noema crosses into external side effects.

Therefore the boundary must be explicit:

Planning
    ↓
Contract
    ↓
Execution Boundary
    ↓
External Side Effect

Before crossing this boundary, required execution conditions must be satisfied.

After crossing it, the loop must record what was attempted and what was observed.

⸻

61. Side-Effect Accounting

For consequential Actions, the loop should preserve enough information to establish:

* what Action was attempted
* which contract governed it
* which capability was invoked
* when it was invoked
* which execution attempt occurred
* which idempotency identity was used
* what response was observed
* whether the external state is known

This is necessary for recovery and auditability.

⸻

62. Execution Events

Conceptual runtime events include:

execution.started
action.ready
action.dispatched
action.accepted
action.completed
action.failed
action.waiting
action.blocked
action.retry_scheduled
action.retry_started
action.unknown
action.reconciled
action.compensation_started
action.compensation_completed
graph.completed
graph.failed
graph.blocked
graph.waiting

These are architectural event concepts rather than a final protocol.

Each event should preserve appropriate provenance and correlation.

⸻

63. Event Ordering

Execution events should preserve the ordering necessary to reconstruct state transitions.

For example:

action.ready
    ↓
action.dispatched
    ↓
action.completed

must not be represented as:

action.completed
    ↓
action.dispatched

The runtime should use durable event or state mechanisms sufficient to preserve execution correctness.

⸻

64. Durable Execution

The Execution Loop must be compatible with durable execution semantics.

A runtime failure must not cause Noema to lose the authoritative execution state.

For example:

Action A
  ↓
COMPLETED
  ↓
runtime crash

After recovery, the system must be able to establish that:

A = COMPLETED

rather than blindly executing A again.

Durability is therefore foundational to safe execution.

⸻

65. Crash Recovery

If the runtime crashes during execution, recovery must reconstruct the latest authoritative execution state.

Conceptually:

Execution State
      ↓
Runtime Failure
      ↓
Recovery
      ↓
State Reconstruction
      ↓
Resume / Reconcile / Halt

The system must not assume that an interrupted process implies that the external Action did not occur.

⸻

66. Recovery After Uncertain Dispatch

The most important recovery boundary occurs when the runtime cannot establish whether an external Action was executed.

Example:

dispatch request sent
      ↓
runtime/network failure
      ↓
response unavailable

The state becomes:

UNKNOWN

unless authoritative evidence establishes otherwise.

The recovery mechanism must then use the Action Contract’s reconciliation and idempotency semantics.

⸻

67. Exactly-Once Semantics

The Execution Loop must not assume that distributed execution can guarantee exactly-once side effects merely because a local runtime operation is executed once.

Instead, Noema should explicitly distinguish:

* execution attempt
* delivery semantics
* provider processing
* external side effect
* observed result

Where possible, idempotency and reconciliation should provide effective exactly-once business behavior.

⸻

68. At-Least-Once Execution

Some execution mechanisms may provide at-least-once delivery.

The loop must therefore tolerate duplicate delivery where the Action Contract permits safe deduplication.

Conceptually:

Dispatch
  ↓
possible duplicate delivery
  ↓
provider idempotency
  ↓
single semantic operation

The Action Contract must define the required semantics.

⸻

69. At-Most-Once Execution

Where an Action cannot safely be retried, the contract may impose at-most-once behavior.

If execution state becomes uncertain, the loop may require reconciliation rather than immediate retry.

The loop must not prefer retry merely because retry improves apparent availability.

⸻

70. Failure Classification

Execution failures should be classified where possible.

Examples:

VALIDATION_FAILURE
AUTHORIZATION_FAILURE
PRECONDITION_FAILURE
TRANSIENT_FAILURE
PERMANENT_FAILURE
TIMEOUT
RATE_LIMITED
RESOURCE_UNAVAILABLE
CONTRACT_FAILURE
EXTERNAL_SYSTEM_FAILURE
UNKNOWN_OUTCOME

Failure classes inform recovery behavior.

They must not be inferred arbitrarily when the evidence is insufficient.

⸻

71. Permanent Failure

A permanent failure is one for which the applicable semantics establish that retry cannot succeed under the current execution context.

The loop should transition according to the defined failure policy.

For example:

PERMANENT_FAILURE
      ↓
FAILED

or:

PERMANENT_FAILURE
      ↓
COMPENSATE

depending on the graph and contract.

⸻

72. Transient Failure

A transient failure may permit retry.

Examples:

* temporary network failure
* provider rate limiting
* temporary resource exhaustion

The loop must still obey bounded retry semantics.

Transient does not mean infinitely retryable.

⸻

73. Timeout

A timeout does not necessarily mean failure.

The loop must distinguish:

operation failed before completion

from:

operation may have completed but response was not observed

Where ambiguity exists, the Action may transition to:

UNKNOWN

rather than FAILED.

⸻

74. Cancellation

Execution cancellation must be explicit.

Cancellation may occur because:

* Actor cancels the Intent
* Intent expires
* Trust is revoked
* policy requires termination
* operator terminates execution
* system safety condition requires termination

Cancellation must not be confused with failure.

⸻

75. Cancellation After Dispatch

Cancellation cannot necessarily undo an external Action that has already been dispatched.

For example:

Action dispatched
      ↓
Actor cancellation

may require:

* allow completion
* attempt compensation
* issue cancellation to provider
* reconcile external state

The applicable Action Contract determines what is possible.

⸻

76. Execution Expiration

Execution may be constrained by an execution window.

Example:

Execute before:
18:00

After expiration, the loop must not silently continue.

The appropriate behavior may be:

BLOCK
REVALIDATE
REQUIRE_CONFIRMATION
FAIL

according to the applicable semantics.

⸻

77. Resource Locking

Where external or internal resources require locking, lock semantics must be explicit.

The loop must distinguish:

resource unavailable

from:

Action failed

when the resource may become available later.

Lock acquisition and release must be observable and bounded.

⸻

78. Long-Running Actions

Some Actions may remain active for extended periods.

The loop must support durable waiting rather than requiring a continuously running process.

Conceptually:

START_ACTION
     ↓
WAITING
     ↓
external event
     ↓
RESUME

The execution state must survive process restarts.

⸻

79. Backpressure

The runtime may experience more executable work than available capacity.

The Execution Loop should apply explicit backpressure rather than allowing unbounded resource consumption.

Backpressure may result in:

WAITING
QUEUED
DEFERRED

without implying that the Action itself failed.

⸻

80. Rate Limits

External rate limits must be respected.

If a provider returns a rate-limit condition:

RATE_LIMITED
      ↓
WAIT
      ↓
RETRY

where retry is contractually permitted.

The loop must preserve retry bounds.

⸻

81. Security Boundary

The Execution Loop must not become a mechanism for privilege escalation.

A model-generated or externally supplied graph must not be able to cause execution merely by containing an Action identifier.

Before dispatch, the loop must enforce the applicable:

* Trust state
* authorization
* capability
* Action Contract
* policy
* execution conditions

⸻

82. No Arbitrary Tool Calls

The Execution Loop must not permit arbitrary model-generated tool calls to bypass the executable graph.

The canonical path remains:

Intent
  ↓
Trust
  ↓
Action Graph
  ↓
Action Contract
  ↓
Execution Loop
  ↓
Consumer

A tool invocation is an execution mechanism, not an authority model.

⸻

83. Model Role During Execution

A model may assist with:

* interpreting external responses
* proposing recovery options
* generating explanations
* identifying possible anomalies

But the model must not silently determine:

* whether an Action is authorized
* whether a dependency is satisfied
* whether a required condition is true
* whether an unknown result should be treated as success
* whether a retry is permitted
* whether a graph should be mutated

Those decisions must be governed by explicit system semantics.

⸻

84. Execution Observability

The loop must provide sufficient observability to reconstruct execution.

At minimum, relevant telemetry should permit inspection of:

* execution identity
* graph version
* node identity
* Action identity
* Contract identity
* capability
* attempt
* state transitions
* timestamps
* latency
* failures
* retries
* external responses
* reconciliation
* compensation
* final outcome

Observability must support operational diagnosis without requiring private model reasoning.

⸻

85. Auditability

Consequential execution must be auditable.

The audit record should establish:

1. what was executed
2. under which Intent version
3. under which graph version
4. under which Action Contract
5. through which capability
6. with which execution identity
7. at what time
8. what was attempted
9. what was observed
10. what state transition resulted

⸻

86. Execution Provenance

Execution provenance should connect runtime events to upstream authority.

Conceptually:

Actor
 ↓
Intent
 ↓
Intent Version
 ↓
Trust Evaluation
 ↓
Graph Version
 ↓
Action Node
 ↓
Contract
 ↓
Execution Attempt
 ↓
External Operation
 ↓
Outcome

This chain enables reconstruction of why a consequential Action was executed.

⸻

87. No Hidden Execution

All consequential execution must be attributable to an explicit Action.

If an Action Contract requires internal operations, those operations must be contractually defined.

The runtime must not silently introduce additional consequential operations outside the declared execution semantics.

⸻

88. Execution and Business State

The Execution Loop may read or modify external business state through authorized capabilities.

It does not become the owner of that state.

For example:

CRM
   ↓
customer.status

remains authoritative for the customer status.

Noema records the state observed during execution and the evidence supporting it.

⸻

89. External System Failure

External system failure must remain distinguishable from Noema execution failure.

For example:

Noema runtime = healthy
Provider = unavailable

is different from:

Provider = healthy
Noema runtime = failed

This distinction is important for recovery and operational diagnosis.

⸻

90. Execution Isolation and Tenant Boundaries

Where multiple Actors, organizations, or execution domains share infrastructure, execution state must remain isolated according to the applicable security model.

An execution context must not permit cross-context access to:

* Intent state
* Action inputs
* credentials
* external resources
* execution results
* audit records

Isolation is a runtime correctness and security requirement.

⸻

91. Secret Handling

The Execution Loop must not treat credentials or secrets as ordinary execution data.

Secrets should be supplied through the appropriate secure mechanism.

They should not be:

* embedded in graph definitions
* exposed in logs
* copied into model prompts
* included unnecessarily in outcomes
* persisted as ordinary Action inputs

⸻

92. Execution Limits

The loop should support explicit limits such as:

* maximum execution duration
* maximum graph depth
* maximum Action attempts
* maximum concurrency
* maximum compensation attempts
* maximum external calls
* maximum waiting period

Limits prevent uncontrolled execution behavior.

⸻

93. Infinite Execution Prevention

The Execution Loop must not permit unbounded runtime loops.

Iteration must be represented through explicit bounded constructs defining:

* iteration condition
* maximum attempts
* timeout
* delay
* termination condition
* failure behavior

This aligns execution with the Action Graph requirement that unrestricted cycles are not permitted.

⸻

94. Execution Loop and Durable Scheduling

Scheduled work must be durable.

If an Action is waiting until a future time:

WAITING
   ↓
scheduled wake-up
   ↓
READY

the schedule must survive process failure.

The runtime must not depend on an in-memory timer as the authoritative source of execution state.

⸻

95. Execution Loop and Recovery

Recovery is part of execution semantics rather than an exceptional afterthought.

The loop must support:

Execute
  ↓
Failure / Crash / Unknown
  ↓
Recover
  ↓
Reconcile
  ↓
Resume / Retry / Compensate / Halt

Recovery behavior must remain bounded and explicit.

⸻

96. Execution Loop and Failure-Recovery Architecture

The Execution Loop consumes the failure and recovery semantics established by the engineering architecture.

The distinction is:

Failure-Recovery Architecture
    ↓
defines recovery semantics
Execution Loop
    ↓
applies those semantics at runtime

The loop must not independently redefine the canonical failure model.

⸻

97. Execution Loop and Idempotency Architecture

The Execution Loop consumes idempotency semantics defined by the Action Contract and engineering architecture.

Conceptually:

Action
  ↓
Idempotency Identity
  ↓
Execution Attempt
  ↓
External Effect

The loop must preserve idempotency identity across retries and recovery where required.

⸻

98. Execution Loop and Observability

Observability is part of execution correctness for consequential operations.

A runtime that performs an Action but cannot establish:

* what was executed
* whether it completed
* which attempt occurred
* what external response was observed

cannot reliably recover from failure.

Therefore execution state and execution observability must remain tightly coupled.

⸻

99. Execution Loop and Scalability

Scaling the Execution Loop horizontally must preserve execution correctness.

Multiple runtime workers must not independently execute the same non-idempotent Action merely because they observe the same READY state.

The architecture must provide appropriate:

* ownership
* leasing
* locking
* deduplication
* idempotency
* durable state transitions

according to the runtime design.

⸻

100. Worker Ownership

Where multiple workers process the same graph, an Action should have an explicit execution ownership mechanism.

Conceptually:

READY
  ↓
worker claims Action
  ↓
LEASED
  ↓
EXECUTING

If the worker fails, recovery must determine whether:

* the Action never started
* the Action completed
* the Action is still executing
* the external result is unknown

The system must not blindly assume any one outcome.

⸻

101. Lease Expiration

Where execution ownership uses leases, lease expiration must not automatically imply that the external Action did not occur.

For example:

Worker A
  ↓
dispatches payment
  ↓
worker crashes
  ↓
lease expires
  ↓
Worker B

Worker B must reconcile the previous attempt before creating a new consequential operation where required.

⸻

102. Exactly-Once State Transition

The runtime should ensure that state transitions themselves are durable and protected against conflicting workers.

For example:

READY → EXECUTING

should not permit two workers to independently claim the same Action unless the execution semantics explicitly support that behavior.

State-transition atomicity is a runtime requirement.

⸻

103. Graph Advancement Loop

Conceptually, the core loop is:

while graph is not terminal:
    evaluate executable nodes
    for each eligible node:
        verify contract and execution conditions
        claim execution ownership
        dispatch Action
        observe result
        transition node state
        apply failure/retry/recovery semantics
        evaluate newly eligible dependencies
    reconcile waiting or unknown nodes
    evaluate graph completion

This is a conceptual model rather than a prescribed implementation.

The implementation may be event-driven, queue-based, actor-based, workflow-based, or otherwise structured.

The semantics remain invariant.

⸻

104. Event-Driven Execution

The Execution Loop need not be implemented as a continuously polling loop.

It may be event-driven:

Action Completed
      ↓
Dependency Event
      ↓
Dependent Action Becomes Eligible
      ↓
Dispatch

The term “loop” describes the lifecycle semantics, not necessarily a particular programming construct.

⸻

105. Polling

Polling may be appropriate when external systems do not provide callbacks.

Polling must remain:

* bounded
* contractually defined
* rate-limited
* observable
* terminable

For example:

POLL_STATUS
    ↓
delivered?
 ┌──┴──┐
No    Yes
↓      ↓
wait  complete
↓
poll again

The iteration must have explicit termination semantics.

⸻

106. Callback Execution

Where external systems provide callbacks, the callback may advance the loop.

The callback must be:

* authenticated
* correlated
* validated
* idempotently processed

A callback must not be accepted solely because it contains a familiar Action identifier.

⸻

107. Execution Reconciliation

Reconciliation is required whenever local runtime state and external business state may diverge.

Examples:

Local = UNKNOWN
External = COMPLETED

or:

Local = EXECUTING
External = FAILED

The authoritative external source should determine the business outcome where appropriate.

Noema updates its execution state based on verified evidence.

⸻

108. Recovery Precedence

When recovering an uncertain Action, the runtime should prefer authoritative evidence over assumptions.

Conceptually:

Authoritative external state
          ↓
Reconciliation
          ↓
Execution state

not:

Runtime assumption
      ↓
External business state

⸻

109. Execution Termination

The Execution Loop must terminate when:

* the graph reaches a terminal completion state
* a terminal failure state is established
* execution is explicitly cancelled
* execution expires
* an unrecoverable safety condition occurs
* the applicable policy requires termination

Termination must be recorded as an explicit state transition.

⸻

110. No Silent Success

The Execution Loop must never report success merely because:

* all dispatch calls returned
* no exception occurred
* the model believes execution succeeded
* a worker terminated normally
* the graph reached a superficially terminal node

Success must be established according to the applicable graph, contract, and outcome semantics.

⸻

111. No Silent Failure

Likewise, the loop must not report failure merely because:

* a response was delayed
* a worker crashed
* an external callback is missing
* a result is temporarily unknown

where reconciliation may establish successful external execution.

Unknown must remain unknown until evidence resolves it.

⸻

112. Determinism

Given the same:

* executable graph
* graph version
* Action Contracts
* execution policies
* observed events
* external results

the state-transition logic should be deterministic wherever the architecture requires deterministic behavior.

Runtime scheduling may vary without changing the semantic result when Actions are independently executable.

⸻

113. Execution History

The Execution Loop must preserve sufficient history to reconstruct:

what became ready
what was dispatched
what was executed
what failed
what was retried
what remained unknown
what was compensated
what was reconciled
what ultimately completed

Execution history is part of the system’s durable operational record.

⸻

114. Execution State Reconstruction

The runtime should be capable of reconstructing current execution state from authoritative durable state.

A process restart must not create a new execution reality.

Conceptually:

Durable Execution Record
          ↓
Runtime Recovery
          ↓
Current Execution State

⸻

115. Execution Loop Invariants

Invariant 1

The Execution Loop executes only Actions represented by an executable Action Graph.

Invariant 2

The Execution Loop does not grant Trust or authorization.

Invariant 3

Every executable Action must resolve to an applicable Action Contract.

Invariant 4

Dependencies must be evaluated explicitly.

Invariant 5

Unknown conditions must not be treated as satisfied.

Invariant 6

Unknown execution outcomes must remain unknown until resolved by authoritative evidence or explicit terminal semantics.

Invariant 7

Retries must respect idempotency and bounded retry semantics.

Invariant 8

Compensation must be explicit.

Invariant 9

Execution state must remain distinct from Trust state and Intent state.

Invariant 10

External business systems remain authoritative for their business state.

Invariant 11

The runtime must preserve durable execution state across process failure.

Invariant 12

A worker failure must not automatically imply that an external Action failed.

Invariant 13

A stale or materially invalid execution context must not silently cross the execution boundary.

Invariant 14

Parallel execution must not violate dependencies, contracts, atomicity, or resource constraints.

Invariant 15

No model may bypass the Action Graph through arbitrary consequential tool calls.

Invariant 16

No execution result may be represented as success without satisfying the applicable completion semantics.

Invariant 17

Material execution-state transitions must be observable and auditable.

Invariant 18

Execution must terminate according to explicit terminal conditions.

⸻

116. Canonical Execution Loop Flow

The canonical lifecycle is:

Executable Action Graph
          ↓
Evaluate Dependencies
          ↓
Evaluate Preconditions
          ↓
Resolve Execution Eligibility
          ↓
READY
          ↓
Claim / Schedule
          ↓
Dispatch
          ↓
EXECUTING
          ↓
Observe Result
     ┌────┼─────────────┐
     ↓    ↓             ↓
COMPLETED FAILED      UNKNOWN
     │    │             │
     │    ├── Retry     ├── Reconcile
     │    ├── Compensate ├── Wait
     │    ├── Escalate   └── Resolve
     │    └── Fail
     │
     ▼
Evaluate Dependents
          ↓
Graph Completion
          ↓
Outcome

At any stage the loop may explicitly:

WAIT
BLOCK
RETRY
RECONCILE
COMPENSATE
ESCALATE
REPLAN
CANCEL
FAIL

according to the governing semantics.

⸻

117. Relationship to the Noema Architecture

The Execution Loop fits into the broader architecture as follows:

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
                           ▼
                   ACTION CONTRACTS
                           │
                           ▼
                  EXECUTION LOOP
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          CAPABILITY    SCHEDULER    RUNTIME
              │            │            │
              └────────────┼────────────┘
                           ▼
                    EXTERNAL SYSTEM
                           │
                           ▼
                     OBSERVED RESULT
                           │
                           ▼
                        OUTCOME

Each layer retains a distinct responsibility.

⸻

118. Fundamental Runtime Boundary

The Execution Loop is the boundary between:

“This Action is permitted and structurally executable.”

and:

“This Action was actually attempted and this is what was observed.”

Therefore:

Trust
  ↓
Execution Eligibility
  ↓
Action Graph
  ↓
Action Contract
  ↓
Execution Loop
  ↓
External Effect
  ↓
Observed Outcome

The Execution Loop must preserve this boundary.

⸻

119. Canonical Mental Model

The Execution Loop can be reduced to five questions:

1. What Action is currently eligible to execute?
2. What dependencies and execution conditions must be satisfied?
3. What Contract governs the execution?
4. What actually happened when the Action was attempted?
5. What state transition follows from that result?

Which produces:

Eligibility
    ↓
Contract
    ↓
Dispatch
    ↓
Observation
    ↓
State Transition
    ↓
Graph Advancement
    ↓
Outcome

⸻

120. Final Definition

The Execution Loop is Noema’s durable runtime control layer for advancing an executable Action Graph through explicit eligibility evaluation, Action Contract enforcement, dispatch, observation, state transition, dependency advancement, failure recovery, reconciliation, and completion.

Its central invariant is:

Noema does not equate planning with execution. An Action becomes executable only through explicit graph, Trust, authorization, capability, and contract requirements; once dispatched, its actual runtime result must be durably observed and represented without silently converting uncertainty into success or failure.

The boundary remains explicit:

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
Execution Loop
   ↓
External System
   ↓
Observed Outcome
   ↓
Outcome