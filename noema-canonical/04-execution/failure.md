Failure

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: 04-execution/failure.md

⸻

1. Definition

Failure is the canonical representation of an execution that cannot successfully produce its intended Outcome within the applicable execution semantics.

Failure is an execution fact, not an interpretation of Intent.

It answers:

Did the attempted Action fail to complete successfully?

Failure must be distinguished from:

REJECTED
CANCELLED
TIMED_OUT
UNKNOWN
COMPENSATED

because these states have materially different semantics.

⸻

2. Core Principle

Noema must represent failure explicitly without confusing failure with uncertainty.

The critical distinction is:

FAILURE
=
the system knows the Action did not succeed
UNKNOWN
=
the system does not know whether the Action succeeded

Therefore:

timeout ≠ failure
unknown ≠ failure
rejection ≠ failure

unless authoritative evidence establishes the appropriate classification.

⸻

3. Failure Belongs to Execution

Failure occurs at execution time.

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
Failure

The existence of a failure does not mean:

Intent was invalid
Action was invalid
Trust was incorrect

The Action may have been perfectly valid and authorized but still failed operationally.

⸻

4. Failure vs Invalid Intent

Consider:

Intent:
"Refund my payment."

Suppose the Intent resolves correctly to:

refund_payment

Trust approves it.

Execution then fails because the payment provider is unavailable.

The correct interpretation is:

Intent       = valid
Action       = valid
Trust        = valid
Execution    = failed

Failure therefore belongs to execution semantics.

⸻

5. Failure vs Trust Denial

If Trust determines:

DENIED

then execution should not occur.

Therefore:

Trust Denied
    ↓
No Execution

Whereas:

Trust Approved
    ↓
Execution
    ↓
Failure

represents an execution failure.

These must never be conflated.

⸻

6. Failure Taxonomy

Noema should distinguish failure classes according to their operational semantics.

A foundational taxonomy is:

VALIDATION_FAILURE
AUTHORIZATION_FAILURE
BUSINESS_FAILURE
DEPENDENCY_FAILURE
RESOURCE_FAILURE
NETWORK_FAILURE
TIMEOUT_FAILURE
CONFLICT_FAILURE
EXECUTION_FAILURE
INTERNAL_FAILURE

The taxonomy may evolve.

The important requirement is that failures remain machine-classifiable.

⸻

7. Validation Failure

The Action cannot be executed because required execution inputs are invalid.

Example:

refund_payment
payment_id = null

Result:

VALIDATION_FAILURE

This may occur at the consumer boundary even if Noema previously validated the Action Contract.

⸻

8. Authorization Failure

The execution consumer determines that the caller or contract is not authorized for the requested operation.

Example:

Action:
delete_customer
Consumer:
authorization scope missing

Result:

AUTHORIZATION_FAILURE

This should not normally occur if Noema’s Trust Engine and contract validation are correctly aligned, but the execution boundary must remain defensive.

⸻

9. Business Failure

The Action is structurally valid and authorized, but the current business state prevents execution.

Example:

refund_payment

where:

payment.status = REFUNDED

or:

payment.status = NOT_REFUNDABLE

Result:

BUSINESS_FAILURE

⸻

10. Dependency Failure

An external dependency required for execution fails.

Example:

Noema
  ↓
Payment Service
  ↓
Payment Provider
  ↓
UNAVAILABLE

Result:

DEPENDENCY_FAILURE

The Action itself may remain valid.

⸻

11. Resource Failure

The execution cannot proceed because a required resource is unavailable.

Examples:

database unavailable
connection pool exhausted
disk unavailable
queue unavailable
capacity exhausted

Result:

RESOURCE_FAILURE

⸻

12. Network Failure

Communication required to perform the Action fails.

Examples:

connection refused
DNS failure
connection reset
TLS failure

Network failure is often retryable, but not always.

The consumer must determine retryability.

⸻

13. Timeout Failure

A timeout means the execution did not complete within the expected time.

However:

A timeout alone does not establish that the Action failed.

Therefore the preferred semantic classification is:

TIMEOUT

which may transition to:

SUCCESS
FAILURE
UNKNOWN

after reconciliation.

⸻

14. Conflict Failure

The Action cannot be executed because the relevant business state changed concurrently.

Example:

update_order(order_123)

but:

order.version = 8

while the contract expected:

version = 7

Result:

CONFLICT_FAILURE

The consumer may return the current state for reconciliation.

⸻

15. Internal Failure

The consumer encounters an unexpected internal error.

Example:

panic
unexpected exception
corrupt internal state
unhandled implementation error

Result:

INTERNAL_FAILURE

The underlying details should be captured for diagnostics without exposing unnecessary internal information to the Intent layer.

⸻

16. Failure Structure

Conceptually:

Failure {
    failure_id
    execution_id
    category
    code
    message
    source
    retryable
    occurred_at
    evidence
}

This is a semantic model, not a final storage schema.

⸻

17. Failure Identity

Every material failure should have an identifiable relationship to the execution that produced it.

execution_id
      ↓
failure_id

Example:

execution:
exec_123
failure:
fail_456

Failure identity should not replace execution identity.

The execution remains the primary causal object.

⸻

18. Failure Code

A machine-readable failure code should identify the specific failure condition.

Examples:

INSUFFICIENT_FUNDS
PAYMENT_PROVIDER_UNAVAILABLE
RESOURCE_NOT_FOUND
CONTRACT_EXPIRED
VERSION_CONFLICT
DEPENDENCY_TIMEOUT
INVALID_PARAMETER

Codes should be stable enough for deterministic policy evaluation.

⸻

19. Failure Message

A human-readable message may provide context.

Example:

Payment provider rejected the refund because the transaction
has already been fully refunded.

The message is explanatory.

The failure code is authoritative for machine behavior.

⸻

20. Failure Source

Failure should identify where it originated.

Possible sources:

NOEMA
CONSUMER
BUSINESS_SYSTEM
EXTERNAL_PROVIDER
NETWORK
UNKNOWN

Example:

source:
PAYMENT_PROVIDER

This helps distinguish execution failures from orchestration failures.

⸻

21. Failure Evidence

A consequential failure should be supported by evidence.

Examples:

provider_error_code
provider_transaction_id
HTTP status
business-state snapshot
resource version
consumer receipt

Evidence should establish why the consumer classified the execution as failed.

⸻

22. Failure Certainty

Failure classification requires sufficient evidence.

The model should distinguish:

CONFIRMED_FAILURE

from:

POSSIBLE_FAILURE

However, POSSIBLE_FAILURE should generally map to:

UNKNOWN

rather than being represented as a true Failure.

This preserves Noema’s determinism principle.

⸻

23. Failure vs Unknown

Consider:

request sent
   ↓
connection lost

There are two possible realities:

provider executed request

or:

provider never received request

Without reconciliation:

UNKNOWN

not:

FAILURE

⸻

24. Failure State

A conceptual execution lifecycle is:

EXECUTING
    │
    ▼
FAILED

The failure record explains why.

The execution state and failure reason should remain separate concepts.

⸻

25. Failure Is Terminal Only When Appropriate

Some failures are recoverable.

Example:

NETWORK_FAILURE

may result in:

retry

Therefore:

FAILED
   ↓
RETRYING
   ↓
EXECUTING

The final execution outcome may eventually be:

SUCCESS

⸻

26. Retryable Failure

A failure may carry:

retryable = true

Example:

DEPENDENCY_UNAVAILABLE
retryable = true

But retryability must be bounded by:

max_attempts
time budget
Action semantics
idempotency
policy

⸻

27. Non-Retryable Failure

Example:

INSUFFICIENT_FUNDS

Repeatedly executing:

charge_payment

will not normally solve the problem.

Therefore:

retryable = false

The next step may instead be:

clarification
new Intent
compensation
human review

depending on the domain.

⸻

28. Failure and Retry Policy

Retry should be deterministic.

Example:

Failure:
NETWORK_FAILURE
Policy:
retry ≤ 3 times
with exponential backoff

The model should not decide:

"Let's try one more time."

based on intuition.

⸻

29. Failure and Compensation

Failure may produce a compensation decision, but it does not automatically produce compensation.

Example:

reserve_inventory → SUCCESS
charge_payment → FAILURE

The reservation may require compensation.

But:

send_email → FAILURE

may require no compensation.

The relationship is:

Failure
   ↓
Evaluate recovery
   ├── Retry
   ├── Compensate
   ├── Escalate
   └── Complete as failed

⸻

30. Partial Failure

Composite execution may produce partial failure.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE

The overall execution may therefore be:

PARTIALLY_FAILED

rather than simply:

FAILED

This distinction matters for compensation and Outcome evaluation.

⸻

31. Partial Failure Model

Conceptually:

Execution Group
├── Action A → SUCCESS
├── Action B → SUCCESS
└── Action C → FAILURE

The system should preserve each child execution’s state.

The parent execution should summarize rather than erase those facts.

⸻

32. Failure Propagation

A child Action failure may propagate to dependent Actions.

Example:

create_customer
      ↓
create_subscription
      ↓
send_email

If:

create_customer → FAILURE

then:

create_subscription
send_email

may become:

BLOCKED

rather than failed.

This is an important distinction.

⸻

33. Blocked vs Failed

FAILED
=
Action was attempted and did not succeed.
BLOCKED
=
Action was not attempted because a prerequisite was not satisfied.

Example:

create_customer → FAILURE
create_subscription → BLOCKED

The subscription Action did not fail because it never executed.

⸻

34. Failure Propagation Must Be Explicit

Noema should not infer arbitrary downstream failure.

Dependency relationships determine propagation.

A → B

means:

A failure may affect B

but the exact behavior must be defined by the execution graph.

⸻

35. Failure and Outcome

Failure is not necessarily the final Outcome.

Example:

Execution:
refund_payment
Result:
FAILURE
Recovery:
retry
Second execution:
SUCCESS

The final Outcome may be:

refund completed

The original failure remains part of execution history.

⸻

36. Failure History Is Immutable

A successful retry must not erase:

Attempt 1 → FAILURE

It should produce:

Attempt 1 → FAILURE
Attempt 2 → SUCCESS

This preserves:

auditability
debuggability
causal history
operational evidence

⸻

37. Failure and Auditability

For consequential Actions, the system should be able to answer:

What failed?
Why did it fail?
When did it fail?
Which Action was being executed?
Which Contract authorized it?
Which consumer attempted it?
Was it retried?
Was it compensated?
What ultimately happened?

Failure records provide part of that chain.

⸻

38. Failure and Determinism

The model must not convert probabilistic signals into authoritative failure states.

For example:

LLM:
"The payment probably failed."

is not sufficient evidence.

Instead:

Payment provider:
transaction status = DECLINED

supports:

CONFIRMED FAILURE

⸻

39. Failure and Evidence

Evidence hierarchy should prefer authoritative sources.

Conceptually:

authoritative business system
        ↓
execution consumer
        ↓
transport / infrastructure
        ↓
inference

Inference should never override authoritative execution evidence.

⸻

40. Failure and Business State

A failure should describe the execution condition, not unnecessarily duplicate the entire business state.

Example:

failure.code:
PAYMENT_ALREADY_REFUNDED

rather than storing an uncontrolled snapshot of every payment attribute.

Relevant evidence may be attached separately.

⸻

41. Failure and Policy Evaluation

Failure can trigger deterministic policies.

Example:

Failure:
PAYMENT_PROVIDER_UNAVAILABLE
Policy:
retry up to 3 times

Another:

Failure:
PAYMENT_ALREADY_REFUNDED
Policy:
mark desired Outcome satisfied

Another:

Failure:
REFUND_PROHIBITED
Policy:
human review

The failure itself does not determine the recovery action.

Policy does.

⸻

42. Failure and Clarification

Not every failure requires clarification.

However, a failure may reveal that the original Intent cannot be completed under current conditions.

Example:

Intent:
"Book the cheapest flight."
Execution:
FAILURE — no flight satisfies constraints.

Noema may transition into a clarification or reformulation state if the user must provide additional constraints.

This is different from a purely technical failure.

⸻

43. Failure and Intent State

The Intent lifecycle should distinguish:

EXECUTION_FAILED

from:

INTENT_INVALID

and:

INTENT_AMBIGUOUS

The failure of an Action does not retroactively make the Intent ambiguous.

⸻

44. Failure and User Communication

Failure messages exposed to users should be derived from structured failure information.

The user-facing explanation should communicate:

what could not be completed
why, when known
what can happen next

without exposing unnecessary internal implementation details.

⸻

45. Failure Classification

A useful canonical classification is:

┌───────────────────────┐
│      FAILURE          │
├───────────────────────┤
│ Validation            │
│ Authorization         │
│ Business              │
│ Dependency            │
│ Resource              │
│ Network               │
│ Conflict              │
│ Internal              │
└───────────────────────┘

Timeout and unknown conditions should be modeled separately when the execution state cannot establish failure.

⸻

46. Failure Transition Model

EXECUTING
    │
    ├──────────────→ SUCCESS
    │
    ├──────────────→ FAILURE
    │                   │
    │                   ├── RETRY
    │                   │
    │                   ├── COMPENSATE
    │                   │
    │                   ├── ESCALATE
    │                   │
    │                   └── TERMINATE
    │
    ├──────────────→ TIMEOUT
    │                   │
    │                   └── RECONCILE
    │
    └──────────────→ UNKNOWN
                        │
                        └── RECONCILE

⸻

47. Failure Recovery

A failure may lead to:

RETRY
COMPENSATION
ESCALATION
CLARIFICATION
TERMINATION

The choice must be determined by explicit execution semantics and policy.

⸻

48. Failure Does Not Imply User Error

A failure may be entirely infrastructural.

Example:

User Intent:
"Send ₦50,000."
Intent:
valid
Action:
valid
Trust:
approved
Execution:
payment provider unavailable
Failure:
DEPENDENCY_FAILURE

The user did nothing wrong.

Noema should not describe this as user error.

⸻

49. Failure Does Not Imply System Error

Similarly:

INSUFFICIENT_FUNDS

may be a legitimate business failure rather than an infrastructure problem.

The classification should preserve this distinction.

⸻

50. Failure and Consumer Contracts

Consumers should return structured failure information according to the Action Contract protocol.

For example:

{
  "status": "FAILED",
  "failure": {
    "code": "INSUFFICIENT_FUNDS",
    "category": "BUSINESS_FAILURE",
    "retryable": false
  }
}

The precise wire format is implementation-specific.

The semantic fields are canonical.

⸻

51. Failure and Compensation Lineage

When compensation follows failure:

Action
  ↓
Execution
  ↓
Failure
  ↓
Compensation Decision
  ↓
Compensation Execution

The compensation must reference the failure that triggered it.

This provides causal lineage:

compensation_id
    ↓
failure_id
    ↓
execution_id
    ↓
contract_id
    ↓
action_id

⸻

52. Failure and Observability

Failure should be observable through:

logs
metrics
traces
execution records
events
audit records

The implementation may vary.

The semantic requirement is that material failures are not silent.

⸻

53. Failure Metrics

Useful operational measurements include:

failure_rate
failure_rate_by_action
failure_rate_by_consumer
failure_rate_by_category
retry_rate
recovery_rate
compensation_rate
unknown_rate
mean_time_to_recovery

These are operational metrics, not canonical ontology entities.

⸻

54. Failure Security

Failure records may contain sensitive operational information.

Therefore:

provider credentials
secrets
tokens
private internal infrastructure details

must not be exposed merely because they exist in the underlying error.

Failure information should follow Noema’s broader evidence and authorization policies.

⸻

55. Failure Invariants

Invariant 1

Failure means the system has established that an attempted Action did not complete successfully.

Invariant 2

Failure must not be inferred from uncertainty alone.

Invariant 3

Unknown execution state must remain distinct from failure.

Invariant 4

Timeout must not automatically be classified as failure.

Invariant 5

Trust denial is not execution failure because execution should not occur.

Invariant 6

A blocked dependent Action is not a failed Action if it was never executed.

Invariant 7

Failure does not invalidate the original Intent by itself.

Invariant 8

Failure does not automatically imply retry.

Invariant 9

Failure does not automatically imply compensation.

Invariant 10

Retry attempts must preserve failure history.

Invariant 11

Failure classification should be machine-readable.

Invariant 12

Consequential failures should be supported by evidence.

Invariant 13

Recovery decisions must be deterministic where their consequences are material.

Invariant 14

A successful retry must not erase the original failure.

Invariant 15

Composite execution must preserve individual child failures.

Invariant 16

Failure records must maintain lineage to the execution that produced them.

⸻

56. Canonical Mental Model

The simplest model is:

              EXECUTION
                  │
          ┌───────┴────────┐
          │                │
       SUCCESS           FAILURE
                           │
                 ┌─────────┼─────────┐
                 │         │         │
               RETRY   COMPENSATE  ESCALATE
                 │         │         │
                 ▼         ▼         ▼
             EXECUTION   RECOVERY   REVIEW

But when certainty is unavailable:

EXECUTION
    │
    ▼
TIMEOUT / LOST RESPONSE
    │
    ▼
UNKNOWN
    │
    ▼
RECONCILIATION
    │
    ├── SUCCESS
    └── FAILURE

⸻

57. Final Definition

Failure is the explicit, evidence-backed state in which an attempted Action is established to have not successfully produced its intended execution result.

The core invariant is:

Noema must never turn uncertainty into failure. A failed Action is one whose unsuccessful execution is known; an Action whose result is unknown must remain unknown until authoritative evidence establishes what happened. Recovery—whether retry, compensation, escalation, or termination—is a separate deterministic decision.