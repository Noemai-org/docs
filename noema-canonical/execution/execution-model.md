Execution Model

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/execution-model.md

⸻

1. Definition

The Execution Model defines how Noema moves an authorized Action from an Action Contract to an actual execution attempt, how execution state is tracked, and how the resulting Outcome is established.

Execution is the point at which an abstract, trusted Action crosses into the external world.

The canonical boundary is:

Intent
   ↓
Action
   ↓
Trust
   ↓
Action Contract
   ↓
Execution
   ↓
Outcome

⸻

2. Core Principle

Noema authorizes and describes execution; the execution consumer performs it.

This distinction is fundamental.

Noema determines:

what may happen

The consumer determines:

how it happens

The authoritative business system determines:

what actually happened

⸻

3. Execution Is Not Intent

An Intent expresses desired meaning.

Example:

"Refund my payment."

Execution is the actual attempt to perform:

refund_payment(payment_123)

Therefore:

Intent ≠ Execution

⸻

4. Execution Is Not an Action

An Action describes an operation:

refund_payment

An Execution represents an attempt to perform a specific Action Instance:

execution_123
    action = refund_payment
    payment = payment_123

Therefore:

Action ≠ Execution

⸻

5. Execution Is Not an Action Contract

The Action Contract defines the authorized execution boundary.

Execution represents what happened when that contract was consumed.

Action Contract
    ↓
Execution Attempt
    ↓
Execution Outcome

A valid contract does not guarantee successful execution.

⸻

6. Execution Is Not Outcome

Execution is the attempt.

Outcome is the result.

Example:

Execution:
"Attempted to refund payment_123."
Outcome:
"Refund transaction ref_456 was created."

Therefore:

Execution ≠ Outcome

⸻

7. Execution Boundary

The canonical boundary is:

                 NOEMA
────────────────────────────────
Intent
  ↓
Resolution
  ↓
Validation
  ↓
Trust
  ↓
Action Contract
────────────────────────────────
                 ↓
          EXECUTION CONSUMER
                 ↓
          BUSINESS SYSTEM

Once the Action Contract crosses the execution boundary, the consumer owns the execution mechanics.

⸻

8. Execution Consumer

An Execution Consumer is a system capable of consuming an Action Contract and attempting the corresponding Action.

Examples:

payment-service
crm-service
inventory-service
workflow-engine
database-service
notification-service

The consumer translates the canonical Action into its implementation-specific operation.

⸻

9. Consumer Responsibilities

The consumer is responsible for:

authenticating the contract
validating contract structure
checking contract validity
binding to the appropriate business resource
performing final business-state validation
executing the Action
reporting execution state
reporting Outcome

⸻

10. Noema Responsibilities

Noema is responsible for:

Intent resolution
Action determination
Validation
Trust evaluation
Policy evaluation
Risk evaluation
Action Contract generation
execution coordination
execution lineage
Outcome interpretation
compensation coordination

Noema does not become the business system merely because it coordinates execution.

⸻

11. Execution Identity

Every execution requires a unique identifier:

execution_id

Example:

execution_id:
exec_01J...

This allows the system to distinguish:

Action Contract

from:

individual execution attempts

⸻

12. Contract-to-Execution Relationship

One Action Contract may produce one or more execution attempts depending on the execution semantics.

For example:

contract_123
     ↓
execution_attempt_1
     ↓
timeout
     ↓
execution_attempt_2
     ↓
success

However, retries must respect the Action’s idempotency semantics.

⸻

13. Execution Attempt

An Execution Attempt is one concrete attempt by a consumer to perform the Action described by an Action Contract.

Conceptually:

Execution {
    execution_id
    contract_id
    attempt
    consumer
    started_at
    completed_at
    status
    outcome
}

⸻

14. Attempt vs Execution

For clarity:

Execution
    └── Attempt 1
    └── Attempt 2
    └── Attempt 3

or, depending on the implementation:

Execution Attempt
    = independently identifiable execution record

The exact persistence model is implementation-specific.

The important requirement is that retries remain observable.

⸻

15. Execution Lifecycle

A conceptual lifecycle is:

ISSUED
   ↓
DISPATCHED
   ↓
ACCEPTED
   ↓
EXECUTING
   ↓
COMPLETED

Failure branches may include:

REJECTED
FAILED
TIMED_OUT
CANCELLED
UNKNOWN

⸻

16. ISSUED

The Action Contract exists and is ready for delivery to its intended consumer.

At this point:

Contract = valid
Execution = not yet started

⸻

17. DISPATCHED

Noema or an execution coordinator has transmitted the contract to the intended consumer.

This does not mean the consumer received it.

⸻

18. ACCEPTED

The consumer has acknowledged that it has accepted the contract for processing.

This does not mean:

Action succeeded

It means:

Consumer accepted responsibility for processing.

⸻

19. EXECUTING

The consumer is actively attempting the Action.

Example:

payment-service
    ↓
calling payment provider

⸻

20. COMPLETED

The consumer has established that the requested Action completed successfully.

The completion should be supported by an execution Outcome.

⸻

21. FAILED

The consumer established that the Action did not complete successfully.

Example:

payment provider rejected transaction

⸻

22. REJECTED

The consumer refuses to execute the contract.

Possible reasons:

unsupported Action
invalid parameters
consumer policy
resource unavailable
contract invalid
contract expired

This differs from business execution failure.

⸻

23. TIMED_OUT

The execution did not complete within the applicable execution window.

Important:

Timeout does not necessarily mean failure.

The Action may have completed externally even though the consumer did not receive the result.

Therefore:

TIMEOUT → UNKNOWN

may be more accurate than:

TIMEOUT → FAILURE

depending on the consumer’s ability to establish state.

⸻

24. UNKNOWN

UNKNOWN means:

The system cannot deterministically establish whether the Action occurred.

Example:

Request sent
    ↓
External system executes
    ↓
Network connection lost
    ↓
No response

The result is:

UNKNOWN

not:

FAILED

This distinction is critical for consequential Actions.

⸻

25. Unknown Execution State

Unknown execution state must trigger reconciliation where possible.

UNKNOWN
   ↓
Query authoritative system
   ↓
┌───────────┬───────────┐
▼           ▼           ▼
SUCCESS    FAILURE     UNKNOWN

Only after reconciliation should the system determine the next step.

⸻

26. Execution State Is Not Trust State

The Trust State Machine determines whether execution is permitted.

The Execution Model determines what happens after authorization.

For example:

Trust:
READY
Execution:
FAILED

The failure does not mean the Action was untrusted.

Likewise:

Trust:
BLOCKED
Execution:
none

No execution should exist.

⸻

27. Execution Preconditions

Execution should not begin unless:

valid Action Contract
+
authorized execution
+
consumer available

are established.

The consumer may additionally require authoritative business-state conditions.

⸻

28. Final Business-State Validation

The execution consumer should validate state immediately before mutation where appropriate.

Example:

Noema:
"Refund payment_123."
Consumer:
"payment_123 is already refunded."

The consumer should not blindly execute based on stale information.

⸻

29. State Freshness

Noema may have evaluated Trust using state observed earlier.

That state may have changed before execution.

Example:

10:00
Trust evaluation:
payment = CAPTURED
10:02
Execution:
payment = ALREADY_REFUNDED

The consumer’s authoritative state must win.

This is one reason Noema must not claim business-state ownership.

⸻

30. Execution Concurrency

Two contracts may attempt related Actions concurrently.

Example:

Contract A:
refund payment_123
Contract B:
refund payment_123

The consumer must protect the business invariant.

Possible outcomes:

A → SUCCESS
B → REJECTED / ALREADY_COMPLETED

Noema cannot rely solely on its own intent state to prevent all concurrent business mutations.

⸻

31. Idempotency

Execution must support idempotency for Actions where duplicate execution is dangerous.

Example:

contract_id = C123
idempotency_key = K456

If the consumer receives:

K456
K456
K456

it should not create three independent mutations.

⸻

32. Retry

Execution may be retried when the failure is transient.

Example:

Attempt 1
    ↓
NETWORK_FAILURE
    ↓
Attempt 2
    ↓
SUCCESS

Retry policy should consider:

Action idempotency
failure classification
execution limits
time constraints
business semantics

⸻

33. Retry Is Not Reauthorization by Default

A retry of the same execution should not silently become a new semantic Action.

Example:

Contract C:
transfer ₦100,000

Retrying C means:

retry transfer ₦100,000

not:

create a new transfer Intent

However, if the contract has expired or material parameters change, a new Trust evaluation may be required.

⸻

34. Execution Expiration

Contracts may contain an execution expiration.

Example:

expires_at:
2026-08-25T15:00:00Z

A consumer receiving the contract after expiration should reject it unless policy explicitly allows otherwise.

⸻

35. Cancellation

Some executions may be cancellable.

Example:

EXECUTING
    ↓
CANCEL_REQUESTED
    ↓
CANCELLED

But cancellation is not guaranteed.

If an external system has already committed the mutation:

CANCELLED

may not be possible.

⸻

36. Cancellation vs Compensation

Cancellation prevents or stops an execution where possible.

Compensation addresses an effect that has already occurred.

Cancellation:
stop before effect
Compensation:
correct after effect

Example:

Pending payment
    ↓
cancel_payment

versus:

Payment completed
    ↓
refund_payment

⸻

37. Execution Atomicity

Execution may be:

ATOMIC
NON_ATOMIC
UNKNOWN

depending on the consumer and Action.

Noema should not assume distributed atomicity.

⸻

38. Composite Execution

A composite Intent may produce multiple Actions:

A
↓
B
↓
C

The Execution Model must represent each Action execution independently.

For example:

Execution Graph
    A → SUCCESS
    B → SUCCESS
    C → FAILURE

This enables compensation and precise Outcome evaluation.

⸻

39. Execution Dependencies

Dependencies should be explicit.

Example:

create_customer
      ↓
create_subscription
      ↓
send_welcome_email

If:

create_customer → FAILURE

then downstream Actions should not execute unless their dependency semantics explicitly permit it.

⸻

40. Execution Graph

For composite execution:

             create_customer
                    │
                    ▼
             create_subscription
                    │
                    ▼
             send_notification

The graph defines:

ordering
dependencies
parallelism
failure propagation
compensation relationships

⸻

41. Parallel Execution

Independent Actions may execute concurrently.

Example:

             ┌── send_email
Intent ──────┤
             └── send_push

If there is no dependency:

send_email
send_push

may execute in parallel.

The execution model must make the independence explicit.

⸻

42. Execution Ordering

Where order matters:

A → B

must be represented as a dependency.

Noema should not rely on incidental queue ordering or implementation behavior.

⸻

43. Execution Result

The consumer should produce a structured result.

Conceptually:

ExecutionResult {
    execution_id
    status
    outcome
    evidence
    error
    completed_at
}

⸻

44. Execution Evidence

Execution evidence may include:

transaction_id
provider_reference
resource_version
timestamp
affected_resource
consumer_receipt

This evidence helps establish the actual Outcome.

⸻

45. Error Model

Execution errors should be structured.

Conceptually:

ExecutionError {
    code
    category
    message
    retryable
    source
}

Possible categories:

VALIDATION_ERROR
AUTHORIZATION_ERROR
BUSINESS_RULE_ERROR
RESOURCE_ERROR
DEPENDENCY_ERROR
NETWORK_ERROR
TIMEOUT
INTERNAL_ERROR
UNKNOWN

The canonical taxonomy should evolve as implementation experience accumulates.

⸻

46. Retryability

An error should indicate whether retry is appropriate where the consumer can determine this.

For example:

NETWORK_ERROR
retryable = true

versus:

INSUFFICIENT_FUNDS
retryable = false

Retryability is an execution concern, not an LLM judgment.

⸻

47. Execution Outcome

The Execution Model should distinguish:

execution status

from:

business outcome

For example:

Execution status:
COMPLETED
Business outcome:
payment_refunded

Or:

Execution status:
COMPLETED
Business outcome:
no_change_required

⸻

48. Execution and Outcome

The relationship is:

Execution
    ↓
produces
    ↓
Outcome

The Outcome describes the resulting business fact or state relevant to the Intent.

⸻

49. Execution Does Not Invent Outcomes

A consumer should report what it can establish.

Bad:

Execution succeeded,
therefore customer is satisfied.

Customer satisfaction is not an execution fact.

Better:

payment_refund_transaction_created

The Outcome Model determines how this relates to the desired Intent Outcome.

⸻

50. Execution Provenance

Every execution should maintain provenance:

execution_id
contract_id
intent_id
action_id
action_instance_id
consumer
timestamps
attempts
outcome

This allows the full causal path to be reconstructed.

⸻

51. Execution Trace

A canonical trace might look like:

Intent: int_123
    ↓
Action: refund_payment
    ↓
Trust Evaluation: trust_456
    ↓
Contract: contract_789
    ↓
Execution: exec_001
    ↓
Consumer: payment-service
    ↓
Attempt: 1
    ↓
Outcome: refund_created

This is the execution lineage.

⸻

52. Execution and Compensation

When execution produces an Outcome requiring recovery:

Execution
    ↓
Outcome
    ↓
Compensation Decision
    ↓
Compensation Action
    ↓
Compensation Contract
    ↓
Compensation Execution

The original execution remains immutable.

⸻

53. Execution and Human Intervention

Some executions may require human intervention.

Example:

Execution:
UNKNOWN
    ↓
reconciliation unavailable
    ↓
HUMAN_REVIEW

Human intervention must not silently mutate execution history.

The resulting decision should be recorded as a separate event or Action.

⸻

54. Execution Events

Execution may be represented as an event stream:

CONTRACT_DISPATCHED
CONTRACT_ACCEPTED
EXECUTION_STARTED
EXECUTION_PROGRESS
EXECUTION_COMPLETED
EXECUTION_FAILED
EXECUTION_RECONCILIATION_REQUIRED
EXECUTION_RECONCILED

Whether Noema uses event sourcing internally is an implementation decision.

The semantic events should remain observable.

⸻

55. Execution Progress

Long-running Actions may expose progress.

Example:

PROVISIONING
    25%
    50%
    75%
    100%

Progress is informational.

It must not be confused with successful completion.

⸻

56. Long-Running Execution

Some Actions cannot complete immediately.

Examples:

provision_infrastructure
process_refund
generate_report
ship_order
migrate_data

The Execution Model therefore supports:

ACCEPTED
    ↓
EXECUTING
    ↓
...time...
    ↓
COMPLETED

⸻

57. Asynchronous Execution

An Action Contract may be consumed asynchronously.

Noema
  ↓
Queue
  ↓
Consumer
  ↓
Execution
  ↓
Outcome

The Action Contract remains the authorization boundary regardless of transport.

⸻

58. Synchronous Execution

Execution may also be synchronous:

Noema
  ↓
Consumer
  ↓
Business System
  ↓
Outcome
  ↓
Noema

The semantic model remains the same.

Only the transport and timing differ.

⸻

59. Execution Isolation

An execution consumer should execute only within the scope defined by the Action Contract.

If the contract authorizes:

update_customer(customer_123)

the consumer must not interpret that as permission to:

delete_customer(customer_123)

or:

update_customer(customer_456)

⸻

60. Execution Security

Consumers should establish:

contract authenticity
contract integrity
consumer identity
contract validity
authorization context

before executing consequential Actions.

Security mechanisms are implementation-specific.

⸻

61. Execution Exactly-Once Semantics

Noema should not assume exactly-once execution across distributed systems.

The practical model should prefer:

at-least-once delivery
+
idempotent execution
+
reconciliation

where appropriate.

Exactly-once behavior may exist within a particular system, but it should not be treated as a universal distributed invariant.

⸻

62. Execution Delivery Semantics

Execution infrastructure may support:

AT_MOST_ONCE
AT_LEAST_ONCE
EFFECTIVELY_ONCE

The chosen semantics must be explicit.

For consequential Actions, at-least-once delivery generally requires strong idempotency or deduplication guarantees.

⸻

63. Execution Consistency

The Execution Model must distinguish:

Noema state
Consumer state
External system state

These may temporarily diverge.

Example:

Noema:
EXECUTING
Consumer:
completed
External provider:
completed

Noema must reconcile toward authoritative evidence.

⸻

64. Consumer as Business-State Authority

For a domain Action:

refund_payment

the payment system is generally authoritative for:

Was the refund actually created?

Noema should not infer this merely from:

execution request sent

⸻

65. Execution Reconciliation

Reconciliation resolves uncertainty between execution records and authoritative business state.

Example:

Execution:
UNKNOWN
Reconciliation:
payment provider says transaction_refund_123 exists
Result:
SUCCESS

This is essential for distributed execution.

⸻

66. Execution Recovery

Recovery mechanisms may include:

retry
reconciliation
compensation
manual intervention
escalation

The correct mechanism depends on the failure class and Action semantics.

⸻

67. Execution and Determinism

The execution model must never use model intuition to decide whether an external mutation occurred.

Bad:

"The request probably succeeded."

Better:

SUCCESS

only when authoritative evidence supports it.

Otherwise:

UNKNOWN

⸻

68. Execution and Noema’s Trust Boundary

Trust answers:

May this Action execute?

Execution answers:

What happened when we attempted it?

This distinction should remain immutable throughout the architecture.

⸻

69. Conceptual Execution Model

                 INTENT
                    │
                    ▼
                  ACTION
                    │
                    ▼
                 TRUST
                    │
                    ▼
             ACTION CONTRACT
                    │
                    ▼
                DISPATCH
                    │
                    ▼
               CONSUMER
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       REJECT              ACCEPT
                              │
                              ▼
                         EXECUTING
                              │
                   ┌──────────┼──────────┐
                   ▼          ▼          ▼
               SUCCESS     FAILURE     UNKNOWN
                   │          │          │
                   │          ▼          ▼
                   │      RETRY /     RECONCILE
                   │      COMPENSATE       │
                   │          │            │
                   └──────────┴────────────┘
                              │
                              ▼
                           OUTCOME

⸻

70. Execution Invariants

Invariant 1

Execution occurs only against an Action Contract.

Invariant 2

An Action Contract does not guarantee successful execution.

Invariant 3

Execution consumers own execution mechanics.

Invariant 4

Authoritative business systems establish actual business state.

Invariant 5

Unknown execution state must not be represented as confirmed failure.

Invariant 6

Timeout does not necessarily mean failure.

Invariant 7

Retries must preserve the semantic identity of the original Action unless a new Action is explicitly created.

Invariant 8

Consequential Actions must provide appropriate idempotency semantics.

Invariant 9

Execution attempts must remain observable.

Invariant 10

Execution history must not be silently rewritten.

Invariant 11

Cancellation and compensation are distinct.

Invariant 12

Execution dependencies must be explicit.

Invariant 13

Parallel execution must only occur where Action dependencies permit it.

Invariant 14

Compensation requires its own execution semantics.

Invariant 15

Noema must not infer business success from dispatch or acceptance alone.

Invariant 16

Execution results must be supported by evidence where the business state is consequential.

⸻

71. Canonical Mental Model

The Execution Model can be reduced to:

Action Contract
      │
      │ authorizes
      ▼
Execution
      │
      │ attempts
      ▼
Business System
      │
      │ establishes
      ▼
Outcome

With failure handling:

Execution
    │
    ├── SUCCESS ────────────────→ Outcome
    │
    ├── RETRY ─────────────────→ Execution
    │
    ├── UNKNOWN ───────────────→ Reconciliation
    │
    ├── FAILURE ───────────────→ Compensation / Escalation
    │
    └── REJECTED ──────────────→ Execution Failure

⸻

72. Final Definition

The Execution Model defines execution as the controlled attempt to perform an authorized Action through an Execution Consumer, with explicit lifecycle states, retry and reconciliation semantics, authoritative Outcome reporting, and bounded recovery mechanisms.

The core invariant is:

Noema does not confuse permission with execution, execution with success, or success with business truth. An Action Contract establishes what may be executed; the consumer attempts it; the authoritative system establishes what actually happened; and Noema records that Outcome without inventing certainty where none exists.