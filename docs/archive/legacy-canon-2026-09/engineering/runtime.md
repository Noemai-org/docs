Runtime

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/runtime.md

⸻

1. Definition

The Noema Runtime is the engineering execution substrate responsible for carrying an authorized execution lifecycle from an executable Action Graph through Action Contract invocation, durable state transition, failure handling, recovery, and Outcome production.

The Runtime is responsible for operational execution.

It does not determine:

* what the Actor intends
* whether an Intent is semantically resolved
* whether an Intent is trusted
* what an Action is permitted to do
* whether an external business state is authoritative

Those responsibilities belong to the corresponding architectural layers.

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
Runtime
   ↓
Execution
   ↓
Outcome

The Runtime therefore implements the execution boundary established by Noema’s architecture.

⸻

2. Core Principle

Noema must not treat execution as an ephemeral function call.

Execution must be represented as a durable, observable, recoverable process whose state can survive:

* process termination
* machine failure
* worker failure
* network interruption
* deployment
* restart
* timeout
* partial completion
* uncertain external outcomes

The Runtime must preserve enough durable state to reconstruct what Noema knows about execution.

Therefore:

Execution
    ≠
Function Invocation

Execution is a lifecycle.

⸻

3. Runtime Responsibility

The Runtime is responsible for:

* loading executable Action Graph state
* scheduling eligible Actions
* enforcing dependency ordering
* invoking Action Contracts through their execution consumers
* persisting execution state
* coordinating retries
* handling timeouts
* recording execution attempts
* detecting uncertain outcomes
* coordinating recovery
* maintaining execution leases
* enforcing concurrency controls
* emitting execution events
* maintaining execution observability
* producing execution-level Outcomes
* preventing unauthorized execution paths
* preserving execution provenance

The Runtime does not redefine the semantic meaning of the Intent.

⸻

4. Runtime Boundary

The Runtime sits downstream of semantic, validation, trust, and graph construction concerns.

Conceptually:

                 CANONICAL INTENT
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
                 ┌──────────────┐
                 │   RUNTIME    │
                 └──────┬───────┘
                        │
                        ▼
                   EXECUTION
                        │
                        ▼
                    OUTCOME

The Runtime must not become a replacement for any upstream authority.

⸻

5. Runtime Is Not Trust

The Runtime must not determine whether an Intent is trusted.

A Runtime worker receiving:

Trust = READY

may execute according to the applicable execution authority.

A Runtime worker must not reinterpret:

Trust = BLOCKED

as:

Trust = READY

Similarly, the Runtime must not bypass an approval, authorization, policy, or other Trust requirement.

The Runtime enforces execution eligibility; it does not create it.

⸻

6. Runtime Is Not the Action Graph

The Action Graph represents:

* Actions
* dependencies
* conditions
* execution relationships
* graph state

The Runtime executes that structure.

Therefore:

Action Graph
    ↓
Runtime

not:

Runtime
    ↓
invent execution graph

The Runtime must not silently introduce consequential Actions absent from the executable graph or applicable Action Contract semantics.

⸻

7. Runtime Is Not the Action Contract

The Action Contract defines the executable interface and obligations of an Action.

The Runtime provides the machinery through which the contract is executed.

Conceptually:

Action Graph Node
       ↓
Action Contract
       ↓
Runtime Invocation
       ↓
Execution Consumer
       ↓
External Capability

The Runtime must respect the contract rather than reinterpret it.

⸻

8. Runtime Is Not Business-State Authority

External systems remain authoritative for their respective business domains.

For example:

Payment Provider
    → payment state
CRM
    → customer state
Identity Provider
    → identity state

The Runtime records execution observations.

It must not silently convert an execution observation into ownership of external business state.

⸻

9. Runtime Execution Unit

The fundamental Runtime execution unit is an Action execution attempt.

Conceptually:

ActionExecution {
    execution_id
    graph_id
    node_id
    action_id
    contract_id
    attempt
    state
    inputs
    started_at
    completed_at
    result
    error
    provenance
}

The exact schema belongs to the execution model.

The important requirement is that execution attempts are explicit and reconstructible.

⸻

10. Runtime Execution Lifecycle

A typical Action lifecycle is:

NOT_READY
    ↓
READY
    ↓
CLAIMED
    ↓
EXECUTING
    ↓
COMPLETED

Alternative terminal or intermediate states may include:

FAILED
BLOCKED
WAITING
RETRY_WAITING
UNKNOWN
CANCELLED
SKIPPED

State transitions must be governed by explicit Runtime semantics.

⸻

11. State Must Be Durable

Execution state that determines whether an Action may execute again must not exist only in process memory.

For example:

Action A
attempt = 2
state = EXECUTING

must remain recoverable if the worker terminates.

Durable state is necessary to prevent:

* duplicate execution
* lost execution
* inconsistent dependency evaluation
* unrecoverable workflows
* incorrect Outcome production

⸻

12. Runtime State Machine

Runtime state transitions should be explicit.

Conceptually:

READY
  ↓
CLAIMED
  ↓
EXECUTING
  ├──→ COMPLETED
  ├──→ FAILED
  ├──→ UNKNOWN
  ├──→ RETRY_WAITING
  └──→ BLOCKED

The Runtime must not transition state merely because a worker believes that a transition would be convenient.

Every transition must have a defined cause.

⸻

13. Durable Execution

Noema execution must be durable across Runtime process failure.

Durability requires persistence of sufficient execution state to reconstruct:

* graph identity
* graph version
* node state
* dependency state
* execution attempts
* retry state
* lease state
* relevant outputs
* errors
* unknown outcomes
* completion state

Durability does not require persisting arbitrary process memory.

It requires preserving canonical execution state.

⸻

14. Runtime Recovery

If a Runtime worker terminates while executing an Action, another Runtime worker must be able to determine the state of that execution.

Conceptually:

Worker A
   ↓
Action executing
   ↓
Worker failure
   ↓
Durable execution state
   ↓
Worker B
   ↓
Recovery

Recovery must not assume that process termination means the external Action failed.

The external outcome may be:

* successful
* failed
* unknown

This distinction is fundamental.

⸻

15. Execution Leases

The Runtime may use leases to coordinate ownership of execution work.

Conceptually:

Action
  ↓
Lease acquired by Worker A
  ↓
Execution

A lease must have:

* owner
* acquisition time
* expiration
* renewal semantics
* recovery semantics

Lease ownership is not execution ownership in the external system.

A worker losing a lease does not prove that the external Action stopped.

⸻

16. Lease Expiration

When a lease expires, another worker may become eligible to recover the execution.

However:

Lease expired
    ≠
External execution stopped

Therefore lease recovery must account for uncertain external state.

Where duplicate execution is dangerous, the Action Contract must provide appropriate idempotency or reconciliation semantics.

⸻

17. Concurrency Control

The Runtime must control concurrent execution where the graph or Action Contract requires serialization.

Examples:

Same node
    → one active execution
Same resource
    → serialized execution
Independent nodes
    → potentially parallel

Concurrency must be explicitly governed.

The Runtime must not assume that all independent graph nodes are safe to execute concurrently.

⸻

18. Parallel Execution

Where the Action Graph permits parallelism and the Action Contracts permit concurrent execution, the Runtime may execute independent Actions concurrently.

For example:

             ┌── B ──┐
A ───────────┤       ├── D
             └── C ──┘

The Runtime may execute B and C concurrently.

The Runtime must nevertheless preserve:

* dependency semantics
* resource constraints
* Action Contract constraints
* concurrency limits
* atomicity requirements

⸻

19. Sequential Execution

Where the graph establishes strict ordering:

A → B → C

the Runtime must not execute B before A satisfies the dependency semantics.

Likewise:

C

must not execute merely because the Runtime has observed that B was attempted.

The relevant dependency condition must be satisfied.

⸻

20. Dependency Evaluation

Before executing an Action, the Runtime must evaluate its dependencies.

Dependencies may require:

* completed upstream Actions
* specific outputs
* successful postconditions
* approval
* authorization
* external conditions
* explicit graph conditions

A dependency must not be satisfied merely because an upstream Action entered EXECUTING.

⸻

21. Conditions

Conditional graph branches must be evaluated explicitly.

Example:

CHECK_ELIGIBILITY
       ↓
eligible = true
       ↓
RENEW

The Runtime must use the defined condition semantics.

It must not invent a branch when the condition is:

UNKNOWN

Unknown must remain unknown unless an explicit recovery or resolution rule applies.

⸻

22. Input Materialization

Before invoking an Action Contract, the Runtime must materialize the Action’s required inputs.

Inputs may originate from:

* Intent
* trusted context
* upstream Action outputs
* authorized external evidence
* explicit defaults
* contract-defined values

The Runtime must not invent missing execution inputs.

If required input is unavailable, the Action must not execute merely to satisfy graph progress.

⸻

23. Input Integrity

The Runtime must preserve the relationship between an Action input and its source.

For example:

Input:
customer_id = customer_123
Source:
LOOKUP_CUSTOMER.output.customer_id

This supports:

* auditability
* reproducibility
* debugging
* security
* downstream verification

An input’s provenance should remain available where execution semantics require it.

⸻

24. Output Persistence

Action outputs required by downstream execution must be durably persisted.

Example:

VERIFY_ACCOUNT
      ↓
account_status = ACTIVE
      ↓
CREATE_TRANSFER

If the worker terminates after verification, the Runtime must not require the verification Action to be repeated merely because its output existed only in memory.

⸻

25. Output Integrity

The Runtime must distinguish:

output observed

from:

output assumed

Only an execution result established according to the Action Contract may become a canonical Action output.

Worker assumptions must not become graph state.

⸻

26. Execution Attempt Identity

Each attempt should have an explicit identity.

Conceptually:

execution_id = logical Action execution
attempt_id   = specific invocation attempt

For example:

execution_id = EX123
attempt 1 = ATT123-1
attempt 2 = ATT123-2

This allows retries and recovery to remain distinguishable.

⸻

27. Idempotency Boundary

Retry behavior must respect Action idempotency semantics.

The Runtime may retry an Action only when the applicable retry policy permits it.

The Runtime must not assume:

same request
=
safe duplicate request

For consequential operations, idempotency must be established through the Action Contract and execution architecture.

⸻

28. Unknown Outcomes

The Runtime must support explicit unknown execution outcomes.

Example:

REQUEST_PAYMENT
       ↓
network timeout
       ↓
UNKNOWN

The Runtime must not automatically convert this into:

FAILED

if the external system may have processed the request.

The correct recovery path may require:

* reconciliation
* status lookup
* idempotency-key reuse
* provider confirmation
* human intervention

⸻

29. Timeout Semantics

A Runtime timeout indicates that the Runtime has stopped waiting for a response.

It does not necessarily indicate that the external Action stopped.

Therefore:

Runtime timeout
    ≠
External cancellation

Timeout handling must define whether the Action becomes:

FAILED
UNKNOWN
RETRY_WAITING

or another explicitly defined state.

⸻

30. Cancellation

Cancellation must be explicit.

A Runtime cancellation request must distinguish:

cancel requested

from:

external execution cancelled

The external system may not support cancellation.

Therefore the resulting state may remain:

UNKNOWN

until the external outcome is established.

⸻

31. Retry Policy

Retries must be bounded and explicit.

A retry policy may define:

* maximum attempts
* retryable error classes
* backoff
* timeout
* jitter
* idempotency requirements
* reconciliation behavior
* terminal failure conditions

The Runtime must not implement arbitrary retry behavior merely because an Action failed.

⸻

32. Backoff

Retry delays should follow the applicable Action Contract and Runtime retry policy.

Conceptually:

Failure
  ↓
Retryable?
  ├── No → FAILED
  └── Yes
       ↓
    Backoff
       ↓
     Retry

Backoff is an execution mechanism.

It must not alter semantic Intent or graph meaning.

⸻

33. Failure Classification

The Runtime should distinguish failure classes.

Examples:

VALIDATION_FAILURE
AUTHORIZATION_FAILURE
CONTRACT_FAILURE
DEPENDENCY_FAILURE
TIMEOUT
NETWORK_FAILURE
RATE_LIMIT
EXTERNAL_BUSINESS_FAILURE
UNKNOWN_OUTCOME
WORKER_FAILURE
SYSTEM_FAILURE

Classification determines recovery semantics.

A transient infrastructure failure must not automatically be treated the same as a permanent business rejection.

⸻

34. Failure Propagation

If an Action fails, downstream Actions must respect the graph’s failure semantics.

Example:

A → B → C
B = FAILED

C must not execute unless an explicit recovery or alternate dependency path permits it.

Failure must therefore propagate according to graph semantics rather than generic Runtime behavior.

⸻

35. Compensation

The Runtime may execute compensating Actions where the graph and Action Contracts define them.

Compensation is not equivalent to rollback.

For example:

Create Payment
     ↓
Update Record
     ↓
Notification fails

A compensating Action may reverse or remediate a prior effect where supported.

The Runtime must not assume that every Action is reversible.

⸻

36. Partial Execution

The Runtime must explicitly represent partial execution.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The Runtime must not produce:

COMPLETED

merely because some Actions succeeded.

The graph Outcome must reflect the actual execution state.

⸻

37. Aggregate Execution State

The Runtime may maintain an aggregate graph execution state.

Possible states include:

NOT_STARTED
RUNNING
WAITING
BLOCKED
COMPLETED
FAILED
PARTIALLY_COMPLETED
CANCELLED
UNKNOWN

Aggregate state must be derived from the defined graph semantics.

It must not replace individual node state.

⸻

38. Execution Completion

A graph is complete only when its completion conditions are satisfied.

This may require:

* all mandatory Actions completed
* mandatory branches resolved
* required postconditions verified
* required external outcomes established
* compensation complete where required
* no unresolved mandatory dependencies

The Runtime must not treat the last attempted Action as automatically defining graph completion.

⸻

39. Postcondition Verification

Where an Action Contract requires postcondition verification, the Runtime must perform or coordinate that verification.

Example:

REQUEST_REPLACEMENT
       ↓
provider response
       ↓
VERIFY_REQUEST_STATUS
       ↓
COMPLETED

A successful invocation response may not itself establish that the desired external state exists.

⸻

40. External State Reconciliation

When execution produces an uncertain result, the Runtime may require reconciliation.

Example:

CREATE_PAYMENT
      ↓
timeout
      ↓
UNKNOWN
      ↓
LOOKUP_PAYMENT
      ↓
known result

Reconciliation must use an authoritative external source where available.

⸻

41. Runtime and TOCTOU

The Runtime must account for time-of-check/time-of-use conditions.

A condition established during graph construction may change before execution.

Therefore:

Graph Valid
     ↓
Time passes
     ↓
External state changes
     ↓
Execution attempt

The execution consumer may reject the Action.

This is an expected property of distributed execution.

⸻

42. Execution-Time Preconditions

Consequential Actions may require final execution-time preconditions.

Examples:

* account remains active
* authorization remains valid
* resource remains available
* transaction limit remains satisfied
* capability remains available

The Runtime must respect those checks.

It must not force execution because the graph was previously valid.

⸻

43. Stale Execution

An executable graph may become stale.

Material changes may include:

* Action Contract changes
* capability removal
* authorization changes
* policy changes
* Intent changes
* dependency invalidation
* external state changes

The Runtime must not silently continue execution when the architecture requires revalidation.

⸻

44. Graph Version Binding

Runtime execution must bind to a specific graph version.

Conceptually:

intent_id = I123
intent_version = 7
graph_id = G123
graph_version = 3

An Action execution must be traceable to the graph version from which it originated.

This prevents ambiguity when graphs are revised.

⸻

45. Contract Version Binding

Runtime execution should also identify the Action Contract version used.

Conceptually:

Action:
TRANSFER_FUNDS
Contract:
transfer.funds.v4

This supports:

* reproducibility
* audit
* recovery
* compatibility analysis
* debugging

A Runtime must not silently substitute a materially different contract during an existing execution.

⸻

46. Execution Context

An execution context may include:

ExecutionContext {
    intent_id
    intent_version
    graph_id
    graph_version
    node_id
    action_id
    contract_id
    actor
    authorization_reference
    correlation_id
    causation_id
}

The exact schema belongs to the execution model.

The purpose is to preserve execution lineage.

⸻

47. Correlation

Every Runtime execution should be correlatable to its originating lifecycle.

Conceptually:

Actor Expression
      ↓
Intent
      ↓
Trust Evaluation
      ↓
Graph
      ↓
Action
      ↓
Execution Attempt
      ↓
Outcome

Correlation identifiers should permit reconstruction of this chain without requiring private model reasoning.

⸻

48. Causation

Runtime events should preserve causation where applicable.

Example:

Action failed
      ↓
retry scheduled

The retry event should identify the failure event that caused it.

This supports deterministic reconstruction of Runtime history.

⸻

49. Runtime Event Model

Illustrative Runtime events include:

execution.started
action.ready
action.claimed
action.started
action.completed
action.failed
action.timed_out
action.unknown
action.retry_scheduled
action.retry_started
action.blocked
action.waiting
action.cancel_requested
action.cancelled
execution.recovered
execution.completed
execution.failed
execution.partially_completed
execution.unknown

These are architectural event concepts, not necessarily the final protocol.

⸻

50. Event Ordering

Events must preserve sufficient ordering information to reconstruct execution history.

Distributed systems may observe events out of order.

Therefore event consumers should not assume:

received_at
=
occurred_at

Where required, events should contain:

* event identity
* event time
* sequence or version information
* causation
* correlation
* execution identity

⸻

51. Event Durability

Execution events that are required for:

* recovery
* audit
* state reconstruction
* Outcome determination

must be durably recorded according to the Runtime’s persistence model.

Observability telemetry alone must not be the sole source of canonical execution state.

⸻

52. Runtime Persistence

Canonical Runtime state should be persisted in a durable state store.

The store must support the consistency guarantees required for:

* state transitions
* lease ownership
* attempt identity
* dependency evaluation
* recovery
* idempotency

The Runtime must not rely on best-effort telemetry for execution correctness.

⸻

53. State Transition Atomicity

Where required, state transitions and associated execution claims must be atomic.

For example:

READY
  ↓
CLAIMED by Worker A

must not allow Workers A and B to both believe they exclusively own the same execution.

The exact mechanism may vary:

* transactional storage
* compare-and-set
* leases
* consensus-backed coordination
* equivalent concurrency controls

The engineering requirement is correctness, not a specific implementation.

⸻

54. Worker Model

Workers are Runtime processes responsible for executing eligible Actions.

Workers should be:

* replaceable
* stateless with respect to canonical execution state
* recoverable
* horizontally scalable where appropriate
* constrained by execution contracts
* observable

A worker must not become the sole holder of canonical execution state.

⸻

55. Worker Failure

Worker termination must be treated as an infrastructure event, not automatically as Action failure.

Example:

Worker A
   ↓
Action invoked
   ↓
Worker crashes

The Runtime must determine whether the external outcome is:

COMPLETED
FAILED
UNKNOWN

before deciding the appropriate recovery path where the contract requires it.

⸻

56. Runtime Restart

A Runtime restart must not lose canonical execution state.

After restart, the Runtime must be able to recover:

* active executions
* waiting executions
* retry schedules
* leases
* dependency states
* completed outputs
* unknown outcomes

Recovery must be deterministic according to the persisted state and applicable policies.

⸻

57. Deployment

Deployment of a new Runtime version must not implicitly invalidate existing execution state.

The Runtime must support explicit compatibility semantics for:

* graph versions
* contract versions
* state schemas
* persisted events
* retry state
* recovery state

A deployment is not a reason to silently restart business execution.

⸻

58. Runtime Upgrades

Runtime changes must preserve the semantics of existing executions unless an explicit migration or compatibility rule exists.

If a change cannot safely interpret an existing execution state, that execution should be:

BLOCKED

or routed to an explicit migration/recovery path.

It must not be silently interpreted under incompatible semantics.

⸻

59. Queue Semantics

A Runtime may use queues to distribute executable Actions.

A queue is an execution mechanism.

It is not the canonical source of execution truth.

For example:

Durable Execution State
        ↓
Queue
        ↓
Worker

rather than:

Queue message
=
canonical execution state

Queue delivery may be:

* duplicated
* delayed
* reordered
* lost and reconstructed

The durable execution model must account for these properties.

⸻

60. At-Least-Once Delivery

The Runtime may operate under at-least-once message delivery.

Therefore:

message delivered twice

must not automatically produce:

Action executed twice

Execution identity and idempotency controls must protect consequential Actions.

⸻

61. Exactly-Once Semantics

The Runtime should not claim exactly-once external execution merely because internal message processing is deduplicated.

For external systems:

internal exactly-once
    ≠
external exactly-once

Exactly-once external effects require support from the external Action Contract and system semantics.

Where such guarantees cannot be established, Noema must represent the uncertainty explicitly.

⸻

62. Runtime Backpressure

The Runtime must support controlled admission of work.

Backpressure may be required when:

* workers are saturated
* downstream systems are rate-limited
* queues grow
* external providers degrade
* resource limits are reached

Backpressure should produce explicit waiting states rather than uncontrolled concurrency.

⸻

63. Resource Limits

Runtime execution may be constrained by:

* worker capacity
* concurrency limits
* provider quotas
* account limits
* memory
* CPU
* network capacity
* execution deadlines

Resource constraints must not be mistaken for semantic failure.

For example:

WAITING_FOR_CAPACITY

is different from:

ACTION_FAILED

⸻

64. Rate Limiting

The Runtime must respect applicable rate limits.

Rate limiting may operate at:

* global level
* tenant level
* Actor level
* capability level
* provider level
* Action level
* resource level

Rate limiting should be explicit and observable.

⸻

65. Execution Deadlines

Actions and executions may have deadlines.

The Runtime should distinguish:

deadline approaching

from:

deadline exceeded

When a deadline is exceeded, the resulting behavior must be explicitly defined.

It must not silently continue an execution that is no longer temporally valid.

⸻

66. Long-Running Actions

Some Actions may remain active for extended periods.

The Runtime must support long-running execution without requiring a worker process to remain continuously alive.

Conceptually:

START_ACTION
      ↓
WAITING
      ↓
EXTERNAL_EVENT
      ↓
RESUME

Durable state must represent the waiting condition.

⸻

67. Human Waiting States

An Action may wait for human intervention.

Example:

TRANSFER
   ↓
HUMAN_APPROVAL_REQUIRED
   ↓
WAITING
   ↓
APPROVAL_RECEIVED
   ↓
CONTINUE

The Runtime must distinguish waiting from failure.

Human approval does not automatically imply that all other execution conditions remain satisfied.

Relevant conditions may require re-evaluation.

⸻

68. External Events

External events may resume Runtime execution.

Examples:

* payment provider callback
* delivery confirmation
* approval event
* identity verification result
* resource availability notification

External events must be authenticated, correlated, and validated before affecting canonical Runtime state.

⸻

69. Untrusted Events

An external event must not mutate execution state merely because it contains a matching identifier.

The Runtime must verify:

* event authenticity
* expected source
* correlation
* execution identity
* event type
* state compatibility
* contract semantics

External input is evidence until validated according to the applicable protocol.

⸻

70. Runtime Security Boundary

The Runtime is an execution boundary.

It must prevent:

* unauthorized Action invocation
* contract bypass
* graph bypass
* capability escalation
* cross-tenant execution
* identity substitution
* untrusted state mutation
* arbitrary model tool calls

The Runtime must trust explicit execution authority, not arbitrary worker input.

⸻

71. Actor and Authorization Context

Runtime execution must retain the relevant Actor and authorization references.

A worker must not substitute its own identity for the Actor.

Conceptually:

Actor
  ↓
Authorization
  ↓
Action Contract
  ↓
Runtime
  ↓
Execution

Worker identity is infrastructure identity.

Actor identity is semantic and authorization context.

They must not be conflated.

⸻

72. Tenant Isolation

Where Noema operates across multiple organizational or security domains, Runtime state must preserve isolation boundaries.

Isolation must apply to:

* execution state
* inputs
* outputs
* credentials
* events
* queues
* logs
* metrics
* recovery operations

A worker processing one execution must not gain access to unrelated execution data.

⸻

73. Credential Handling

The Runtime should not persist sensitive credentials as ordinary execution state unless explicitly required and protected.

Credential acquisition should occur through the appropriate security boundary.

Execution records should retain references necessary for audit without unnecessarily exposing secret material.

⸻

74. Secret Redaction

Runtime logs and events must not expose secrets merely because those secrets were present in Action inputs or outputs.

Sensitive values may require:

* redaction
* tokenization
* reference substitution
* structured secret handling

Observability must remain useful without becoming a data-exfiltration mechanism.

⸻

75. Runtime Observability

The Runtime must expose sufficient operational information to determine:

* what is executing
* what is waiting
* what failed
* what retried
* what is unknown
* what is blocked
* which worker owns an execution
* which graph version is active
* which contract version is active
* how long execution has taken
* where execution is stalled

Observability must reflect canonical execution state.

⸻

76. Runtime Metrics

Useful Runtime metrics may include:

* Action execution latency
* queue latency
* retry rate
* failure rate
* unknown outcome rate
* recovery rate
* worker utilization
* lease expiration rate
* execution completion rate
* blocked execution count
* waiting execution count
* dependency blocking time
* external provider error rates

Metrics are operational evidence.

They do not replace execution state.

⸻

77. Runtime Logging

Logs should support operational diagnosis.

Relevant fields may include:

execution_id
attempt_id
graph_id
graph_version
node_id
action_id
contract_id
worker_id
event_id
correlation_id
causation_id
timestamp
state
error_class

Logs should avoid unnecessary sensitive payloads.

⸻

78. Runtime Tracing

Distributed execution may span:

Noema Runtime
    ↓
Execution Consumer
    ↓
Provider Adapter
    ↓
External System

Tracing should preserve causal relationships across these boundaries where supported.

Trace data should complement, not replace, canonical execution state.

⸻

79. Runtime Auditability

The Runtime must make it possible to reconstruct:

1. which graph was executed
2. which version was executed
3. which Actions were eligible
4. which Actions executed
5. which attempts occurred
6. which worker processed each attempt
7. what results were observed
8. what failures occurred
9. what retries occurred
10. what recovery occurred
11. what final Outcome was produced

This is execution provenance.

It does not require private model reasoning.

⸻

80. Runtime and Outcome

The Runtime produces execution evidence used to establish an Outcome.

Conceptually:

Action execution
      ↓
Execution observations
      ↓
Postcondition verification
      ↓
Execution Outcome

The Outcome should distinguish what Noema observed from what it merely expected.

⸻

81. Outcome Is Not Trust

A successful Trust evaluation does not imply successful execution.

Example:

Trust:
READY
Runtime:
FAILED

This is valid.

Likewise:

Trust:
READY
Runtime:
UNKNOWN

is valid.

Execution failure does not retroactively prove that the original Trust decision was incorrect.

⸻

82. Runtime Reconciliation

Recovery may require reconciliation between:

* durable Runtime state
* Action Contract state
* external business state
* provider events
* execution evidence

The Runtime should prefer authoritative evidence over local assumptions.

For example:

Local:
UNKNOWN
Provider:
COMPLETED
Result:
reconciled to COMPLETED

The reconciliation process must itself be auditable.

⸻

83. Runtime and Re-Planning

The Runtime must not silently become a planning engine.

If an Action cannot execute and a materially different execution structure is required:

Runtime failure
      ↓
Replanning required
      ↓
Action Graph revision
      ↓
Validation / Trust as required
      ↓
New execution

The Runtime may report the condition requiring replanning.

It must not invent a new consequential plan without the appropriate architectural process.

⸻

84. Runtime and Graph Mutation

The Runtime must not silently mutate an executing graph.

If material change occurs:

Graph v1
   ↓
Material change
   ↓
Execution transition
   ↓
Revalidation / re-evaluation
   ↓
Graph v2

The relationship between versions must remain explicit.

⸻

85. Runtime Determinism

Given the same:

* durable execution state
* Action Graph version
* Action Contract version
* Runtime rules
* external execution results

the Runtime’s state transition behavior should be deterministic wherever the architecture requires determinism.

Infrastructure nondeterminism must not silently become semantic nondeterminism.

⸻

86. Runtime State Reconstruction

A Runtime must be able to reconstruct current execution state from canonical durable state and defined event/state semantics.

Reconstruction should answer:

What is the current state?
Why is it in that state?
What event caused the transition?
What remains to execute?
What is waiting?
What is uncertain?

This capability is fundamental to recovery.

⸻

87. Runtime Garbage Collection

Completed execution state may eventually be subject to retention policies.

Retention must preserve whatever information is required for:

* audit
* compliance
* debugging
* reconciliation
* reproducibility
* Outcome reconstruction

Deletion must not occur merely because an execution is no longer active.

Retention is an explicit engineering concern.

⸻

88. Runtime Failure Domains

The Runtime should distinguish failures across domains:

Worker
Queue
Persistence
Network
Provider
Action
Contract
Authorization
Dependency
External Business State

This classification supports appropriate recovery behavior.

A persistence failure, for example, must not be treated as evidence that an external Action failed.

⸻

89. Runtime Availability

Runtime availability must be designed independently from execution correctness.

A temporary Runtime outage should result in:

execution waiting for recovery

rather than:

execution lost

Durability therefore takes precedence over superficial liveness.

⸻

90. Runtime Scalability

The Runtime may scale horizontally by distributing executable work among workers.

Scaling must preserve:

* execution identity
* dependency semantics
* concurrency constraints
* idempotency
* ordering
* tenant isolation
* durable state consistency

More workers must not change the semantic meaning of an execution.

⸻

91. Runtime Backward Compatibility

Runtime implementations must preserve compatibility with active execution state where required.

Changes to:

* state schema
* event schema
* retry semantics
* lease semantics
* Action invocation
* persistence representation

must be versioned or migrated where necessary.

Existing executions must not become unrecoverable because the Runtime changed.

⸻

92. Runtime Testing

The Runtime must be tested against failure, not merely successful execution.

Testing should include:

* worker crash
* process restart
* duplicate delivery
* delayed delivery
* lease expiration
* timeout
* provider failure
* unknown outcome
* retry
* duplicate retry
* persistence failure
* partial execution
* dependency failure
* cancellation
* recovery
* deployment during execution
* concurrent workers

The Runtime’s correctness is demonstrated by behavior under failure as well as success.

⸻

93. Fault Injection

Where practical, Runtime engineering should support deliberate fault injection.

Examples:

kill worker
delay provider response
drop callback
duplicate message
expire lease
fail persistence operation
return unknown outcome

Fault injection validates recovery semantics that ordinary happy-path tests cannot establish.

⸻

94. Runtime Safety Principle

When the Runtime cannot establish whether a consequential Action is safe to continue, it should prefer an explicit uncertain or blocked state over an invented success or failure state.

Conceptually:

Insufficient evidence
       ↓
UNKNOWN / BLOCKED

not:

Insufficient evidence
       ↓
ASSUME SUCCESS

and not:

Insufficient evidence
       ↓
ASSUME FAILURE

unless the applicable contract explicitly defines that interpretation.

⸻

95. Runtime Progress Principle

Durability must not become permanent stagnation.

The Runtime should make waiting and blocking states actionable through:

* retry scheduling
* external event handling
* reconciliation
* timeout handling
* escalation
* recovery
* re-evaluation

A durable state machine must preserve both safety and forward progress.

⸻

96. No Hidden Execution

Every consequential external effect must be attributable to an explicit execution path.

The Runtime must not permit:

Graph:
TRANSFER
Runtime secretly performs:
LOOKUP
TRANSFER
NOTIFY
AUDIT

unless those additional operations are explicitly defined by:

* graph nodes
* Action Contracts
* contractually required execution behavior

The execution boundary must remain inspectable.

⸻

97. No Arbitrary Tool Execution

The Runtime must not provide a mechanism through which a model can bypass the Action Graph and Action Contract layers.

The canonical path remains:

Intent
   ↓
Trust
   ↓
Action Graph
   ↓
Action Contract
   ↓
Runtime
   ↓
Execution Consumer
   ↓
External Capability

A tool invocation is an implementation mechanism.

It is not execution authority.

⸻

98. Runtime Architectural Invariants

Invariant 1

The Runtime executes authorized execution structures; it does not create authorization.

Invariant 2

The Runtime does not determine Intent meaning.

Invariant 3

The Runtime does not own authoritative external business state.

Invariant 4

Canonical execution state must be durable.

Invariant 5

Every consequential Action execution must be attributable to an explicit Action Graph and Action Contract.

Invariant 6

Runtime state transitions must have defined causes.

Invariant 7

Worker failure must not automatically be interpreted as external Action failure.

Invariant 8

Unknown external outcomes must remain explicitly unknown until reconciled or otherwise resolved.

Invariant 9

Retries must respect Action Contract and idempotency semantics.

Invariant 10

At-least-once delivery must not cause uncontrolled duplicate consequential effects.

Invariant 11

Lease expiration does not establish external execution cancellation.

Invariant 12

A Runtime timeout does not necessarily establish external failure.

Invariant 13

Dependency conditions must be satisfied before dependent Actions execute.

Invariant 14

The Runtime must not silently mutate the executable Action Graph.

Invariant 15

Material execution changes must remain auditable.

Invariant 16

Execution state must remain reconstructible after worker or Runtime failure.

Invariant 17

External systems remain authoritative for their business state.

Invariant 18

Execution failure does not imply Trust failure.

Invariant 19

Trust readiness does not imply execution success.

Invariant 20

Partial execution must remain explicitly represented.

Invariant 21

The Runtime must not invent missing inputs.

Invariant 22

The Runtime must not silently introduce hidden consequential Actions.

Invariant 23

Runtime observability must not replace canonical execution state.

Invariant 24

Runtime scaling must not alter execution semantics.

Invariant 25

A stale execution structure must not silently cross a required revalidation boundary.

⸻

99. Canonical Runtime Flow

The canonical Runtime lifecycle is:

Executable Action Graph
          ↓
Dependency Evaluation
          ↓
Action Eligibility
          ↓
Execution Claim
          ↓
Input Materialization
          ↓
Action Contract Invocation
          ↓
External Execution
          ↓
Execution Result
          │
     ┌────┼───────────┐
     │    │           │
     ▼    ▼           ▼
 COMPLETED FAILED    UNKNOWN
     │    │           │
     │    │           ▼
     │    │      Reconciliation
     │    │           │
     │    └──────┬────┘
     │           │
     ▼           ▼
Postcondition Verification
          ↓
Graph State Update
          ↓
Outcome

At any point the Runtime may enter:

WAITING
BLOCKED
RETRY_WAITING
CANCELLED
ESCALATED

when explicitly required by the applicable semantics.

⸻

100. Runtime Mental Model

The Runtime can be reduced to six questions:

1. What executable structure am I responsible for executing?
2. Which Action is eligible to execute now?
3. What Contract governs that execution?
4. What execution result was actually established?
5. What must happen when the result is failed, partial, or unknown?
6. Can the execution state be recovered and reconstructed after failure?

This produces:

Executable Graph
      ↓
Eligibility
      ↓
Contract Invocation
      ↓
Durable Execution
      ↓
Recovery / Reconciliation
      ↓
Outcome

⸻

101. Relationship to the Engineering Architecture

The Runtime is the operational substrate connecting Noema’s architectural execution model to concrete infrastructure.

                     INTENT
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
              ┌─────────────────┐
              │     RUNTIME     │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Workers      Persistence    Queues
          │            │            │
          └────────────┼────────────┘
                       ▼
               Execution Consumer
                       │
                       ▼
             External Capabilities
                       │
                       ▼
                    OUTCOME

Engineering concerns such as:

* durability
* idempotency
* failure recovery
* observability
* reliability
* concurrency
* persistence
* scheduling

exist to make this lifecycle operationally trustworthy.

⸻

102. Runtime and Durable Execution

Durable execution is not a separate alternative to the Runtime.

It is a fundamental property of the Runtime.

The Runtime must preserve execution state such that:

Runtime Process Failure
          ↓
Durable State Remains
          ↓
Recovery
          ↓
Execution Continues or Terminates Explicitly

The objective is not merely that the process survives.

The objective is that the execution lifecycle survives process failure.

⸻

103. Runtime and Idempotency

Idempotency protects the boundary between Runtime retry/recovery behavior and external side effects.

The relationship is:

Runtime
   ↓
Retry / Recovery
   ↓
Idempotent Action Contract
   ↓
External Effect

The Runtime must assume that recovery can produce repeated invocation attempts.

Action Contracts must therefore define the semantics necessary to make those attempts safe where required.

⸻

104. Runtime and Failure Recovery

Failure recovery is a Runtime responsibility, but recovery semantics originate from the applicable execution model.

The Runtime may:

RETRY
WAIT
RECONCILE
COMPENSATE
ESCALATE
BLOCK
FAIL

only where those transitions are explicitly permitted.

Recovery must never become improvisational planning.

⸻

105. Runtime and Observability

Observability must expose Runtime truth rather than manufacture it.

The Runtime should make visible:

Current State
     ↓
Transition History
     ↓
Execution Attempts
     ↓
Failures
     ↓
Retries
     ↓
Recovery
     ↓
Outcome

Operational telemetry should remain correlated with canonical execution state.

⸻

106. Runtime and Reliability

Reliability is not equivalent to:

never failing

A reliable Runtime is one that:

* preserves state
* detects failure
* distinguishes failure classes
* prevents unsafe duplication
* recovers where permitted
* represents uncertainty
* preserves provenance
* reaches explicit terminal states
* does not silently lose executions

Failure is expected.

Uncontrolled failure semantics are not.

⸻

107. Fundamental Runtime Boundary

The Runtime is the boundary between:

An Action that has been authorized and contracted for execution

and:

The concrete operational process that attempts to produce its external effect.

Therefore:

Trust
  ↓
Execution Eligibility
  ↓
Action Graph
  ↓
Action Contract
  ↓
Runtime
  ↓
External Execution
  ↓
Outcome

The Runtime must preserve every boundary above it.

It must not become a second Intent Engine, Trust Engine, Action Graph, or external business-state authority.

⸻

108. Final Definition

The Noema Runtime is the durable, observable, recoverable execution substrate responsible for executing authorized Action Graphs through explicit Action Contracts while preserving execution state, dependency semantics, retry and idempotency requirements, failure and recovery behavior, execution provenance, and Outcome integrity.

Its central invariant is:

Noema execution is a durable stateful process, not an ephemeral tool call. The Runtime executes explicit Actions under explicit Contracts and preserves enough canonical state to determine, recover, and audit what happened—even when workers, networks, providers, or external systems fail.

The final boundary is:

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
Runtime
    ↓
Execution
    ↓
Recovery / Reconciliation
    ↓
Outcome

And the fundamental Runtime principle is:

Authorized execution must remain:
    explicit
    durable
    recoverable
    observable
    idempotency-aware
    failure-aware
    contract-bound
    auditable

Noema must never confuse:

execution attempted

with:

execution completed

or:

execution completed

with:

external business outcome established

The Runtime exists to preserve those distinctions while carrying authorized execution safely from Action Graph to Outcome.