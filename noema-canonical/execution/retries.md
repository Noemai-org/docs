Retries

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/retries.md

⸻

1. Definition

A retry is a new execution attempt of an Action whose previous attempt did not establish a definitive successful Outcome, performed under explicitly defined retry semantics and safety constraints.

A retry is not simply:

run the same thing again

It is:

re-evaluate
    ↓
determine whether retry is safe
    ↓
create a new execution attempt
    ↓
observe the result

⸻

2. Core Principle

Noema must never retry a consequential Action merely because the previous attempt failed, timed out, or became uncertain.

Before retrying, Noema must determine:

Is retry permitted?
Is retry safe?
Are preconditions still satisfied?
Could the previous attempt have succeeded?
Is the Action idempotent or otherwise protected?
Has the retry budget been exhausted?

⸻

3. Why Retries Exist

Distributed execution is inherently unreliable.

An Action can produce:

timeout
connection failure
provider error
process crash
network partition
rate limit
temporary unavailability
unknown execution state

A failure to receive a response does not necessarily mean the external Action did not occur.

Therefore Noema must distinguish:

execution failed

from:

execution result unknown

before considering retry.

⸻

4. Retry Is a New Attempt

Each retry is a distinct execution attempt.

Action A
 ├── Attempt 1
 ├── Attempt 2
 └── Attempt 3

The attempts should have distinct identities:

action_id
execution_id
attempt_id

This is important for:

auditability
idempotency
observability
reconciliation
provider correlation

⸻

5. Retry Does Not Reset Execution History

If:

Attempt 1 → TIMEOUT
Attempt 2 → SUCCESS

the execution history remains:

Attempt 1: TIMEOUT
Attempt 2: SUCCESS

Noema must preserve the complete attempt history.

It should not rewrite the first attempt as though it never occurred.

⸻

6. Retry vs Re-execution

These concepts should remain distinct.

Retry

The same semantic Action is attempted again because the previous attempt did not establish the required result.

Re-execution

A new execution of an Action that is intentionally invoked again, potentially because the user or workflow explicitly requested it.

Example:

User:
"Send the report again."

is not necessarily a retry.

⸻

7. Retry vs Compensation

A retry attempts to achieve the same intended effect.

Compensation attempts to mitigate or reverse an effect that has already occurred.

Retry:
charge payment again
Compensation:
refund a payment that was already charged

Confusing these can create severe side effects.

⸻

8. Retry vs Reconciliation

Reconciliation attempts to determine what actually happened.

Retry:
"Try it again."
Reconciliation:
"Find out whether it already happened."

For uncertain consequential Actions:

UNKNOWN
   ↓
RECONCILE
   ↓
Did postcondition occur?

Only if reconciliation establishes that the required effect did not occur should retry normally become a candidate.

⸻

9. Retry State Machine

Conceptually:

ATTEMPTED
   │
   ├── SUCCESS ───────────────► COMPLETE
   │
   ├── DEFINITIVE FAILURE ────► RETRY EVALUATION
   │
   └── UNKNOWN ────────────────► RECONCILIATION
                                      │
                              ┌───────┴───────┐
                              ▼               ▼
                           EFFECT          NO EFFECT
                          EXISTS              │
                              │              ▼
                              ▼          RETRY EVALUATION
                           COMPLETE

⸻

10. Retry Eligibility

A retry should be considered only when:

retry policy permits it
AND
retry budget remains
AND
Action remains valid
AND
required preconditions are satisfied
AND
authorization remains valid
AND
retry is safe
AND
no existing successful effect has been established

⸻

11. Preconditions Must Be Re-Evaluated

A retry is not exempt from preconditions.

Example:

Attempt 1:
balance = ₦100,000
withdraw ₦100,000
timeout

Before retry:

balance = ₦0

The original precondition:

balance >= ₦100,000

is no longer satisfied.

Therefore:

retry = BLOCKED

⸻

12. Authorization Must Be Re-Evaluated

Authorization may change between attempts.

Example:

Attempt 1:
authorization = APPROVED
Attempt 2:
authorization = REVOKED

The retry must not proceed simply because the first attempt was authorized.

⸻

13. Idempotency Is a Primary Retry Safety Mechanism

Retries are safest when the Action is idempotent.

Conceptually:

f(f(x)) = f(x)

For example:

set account.status = ACTIVE

Repeated execution produces the same final state.

Contrast:

charge ₦100,000

which is not inherently idempotent.

Retrying it can produce:

₦100,000
+
₦100,000

instead of one charge.

⸻

14. Idempotency Keys

For non-idempotent external operations, Noema may require an idempotency mechanism.

Example:

idempotency_key = intent_123/action_456

The provider can use the key to recognize duplicate attempts.

Conceptually:

Attempt 1:
charge(key=abc123)
Attempt 2:
charge(key=abc123)
Provider:
same logical operation

The exact mechanism belongs to the Action Contract and consumer/provider integration.

⸻

15. Idempotency Does Not Mean Retry Is Always Safe

Even an idempotent Action may have:

side effects
rate limits
external dependencies
time-sensitive conditions
authorization changes

Therefore:

idempotent
≠
automatically retryable

Idempotency is a safety property, not a retry permission.

⸻

16. Unknown Execution State

The most dangerous retry case is:

UNKNOWN

Example:

Noema
  ↓
POST /charge
  ↓
provider processes charge
  ↓
network connection fails
  ↓
Noema receives no response

Noema cannot conclude:

charge failed

The correct state is:

charge outcome = UNKNOWN

⸻

17. Unknown Must Trigger Reconciliation Before Retry

For consequential Actions:

UNKNOWN
   ↓
reconcile
   ↓
postcondition evaluation

If:

payment.status = SETTLED

then:

do not retry

If:

payment does not exist

and sufficient evidence establishes this:

retry may become eligible

⸻

18. Retry After Definitive Failure

A retry may be more straightforward when failure is definitive.

Example:

provider:
HTTP 503
operation not accepted

If the provider contract establishes that:

operation was not processed

then retry may be safe, subject to:

retry policy
preconditions
authorization
idempotency
budget

⸻

19. Error Classification

Retry decisions should depend on error class.

A useful conceptual classification is:

TRANSIENT
PERMANENT
UNKNOWN
CONFLICT
RATE_LIMITED
AUTHORIZATION
PRECONDITION

Examples:

Transient

503 Service Unavailable
connection reset
temporary dependency failure

Potentially retryable.

Permanent

invalid account
unsupported operation
malformed request

Normally not retryable.

Unknown

timeout after request transmission

Requires reconciliation.

Authorization

403 Forbidden

Normally not automatically retryable.

Precondition

insufficient balance

Normally requires state change or replanning, not blind retry.

⸻

20. Retryability Must Be Explicit

The executor should not infer:

"network error → retry"

solely from the transport error.

The Action Contract or retry policy should define what classes of failures are retryable.

Conceptually:

RetryPolicy {
    max_attempts
    retryable_failures
    backoff
    timeout
    jitter
}

⸻

21. Retry Budget

Retries must be bounded.

Example:

max_attempts = 3

Then:

Attempt 1
Attempt 2
Attempt 3
STOP

Noema must not retry indefinitely by default.

⸻

22. Retry Budget vs Execution Timeout

These are different controls.

Execution timeout

How long one attempt may execute.

max_execution_time = 30s

Retry budget

How many attempts may be made.

max_attempts = 3

Both may be required.

⸻

23. Time-Based Retry Budgets

A retry policy may also constrain total retry duration.

Example:

retry_window = 10 minutes

Even if:

max_attempts = 10

Noema must stop retrying after the retry window expires.

⸻

24. Exponential Backoff

Retries should generally not happen immediately when failures are transient.

A common strategy:

delay = base × 2^attempt

Example:

Attempt 1 → immediate
Attempt 2 → 1s
Attempt 3 → 2s
Attempt 4 → 4s

The exact values are policy-defined.

⸻

25. Jitter

Distributed systems may require randomized jitter to prevent synchronized retries.

Conceptually:

delay = exponential_backoff + jitter

However, jitter affects scheduling rather than semantic decision-making.

The decision to retry must remain deterministic under the same policy and state; the exact scheduling delay may be intentionally non-deterministic.

⸻

26. Retry Storms

Unbounded or synchronized retries can create:

service overload
queue saturation
cascading failures
rate-limit amplification

Therefore retry policy is also a system stability mechanism.

⸻

27. Retry and Rate Limits

A provider may respond:

429 Too Many Requests

Noema should respect provider-defined retry guidance such as:

Retry-After

where available.

Repeatedly retrying immediately can worsen the failure.

⸻

28. Retry and Dependency Failure

Suppose:

Noema
  ↓
Payment Service
  ↓
Bank

If the bank is unavailable:

retrying aggressively against Payment Service

may not help.

Retry policy should consider the actual failure domain.

⸻

29. Retry and Circuit Breaking

Repeated failures may justify temporarily preventing further attempts.

Conceptually:

healthy
  ↓
failures
  ↓
OPEN
  ↓
wait
  ↓
HALF_OPEN
  ↓
test

Circuit-breaking is an execution infrastructure concern but can influence retry eligibility.

⸻

30. Retry and Concurrency

Retries can overlap with previous attempts if the original execution is merely slow.

Example:

Attempt 1 still running
Attempt 2 starts

This can create duplicate execution.

Noema should therefore know whether the previous attempt is:

finished
failed
unknown
still executing

before starting another attempt.

⸻

31. No Concurrent Retries by Default

For consequential Actions:

Noema should not create concurrent retry attempts unless the Action Contract explicitly permits concurrent execution.

The default should be:

one active attempt per logical Action

⸻

32. Retry and Execution Leases

Long-running execution may use a lease:

attempt owns execution lease

A retry should not begin until:

lease expired
OR
attempt definitively terminated

This prevents two consumers from believing they independently own the same execution.

⸻

33. Retry and Consumer Crashes

Consider:

consumer receives Action
 ↓
executes external operation
 ↓
consumer crashes

Noema may not know whether the operation completed.

Therefore recovery should produce:

UNKNOWN

rather than:

FAILED

until sufficient evidence exists.

⸻

34. Retry and Postconditions

Postconditions are central to safe retry.

Attempt
   ↓
Observed Evidence
   ↓
Postcondition
   ↓
Satisfied?

If:

YES

then:

no retry

If:

NO

then:

evaluate retry policy

If:

UNKNOWN

then:

reconcile

⸻

35. Retry and Precondition/Postcondition Relationship

A useful execution loop is:

Evaluate Preconditions
        ↓
Execute
        ↓
Observe
        ↓
Evaluate Postconditions
        ↓
 ┌──────┼──────────┐
 ▼      ▼          ▼
PASS   FAIL      UNKNOWN
 │      │          │
 ▼      ▼          ▼
DONE  Retry?    Reconcile
          │
          ▼
   Re-evaluate
   Preconditions

⸻

36. Retry and Compensation

Suppose:

Step A → SUCCESS
Step B → SUCCESS
Step C → FAILURE

Retrying C may be correct if safe.

But if C partially executed:

Step C → UNKNOWN

the system should reconcile before either:

retry C

or:

compensate A/B

⸻

37. Retry and Partial Effects

An Action can fail after producing partial effects.

Example:

create_user

Provider creates the user but response is lost.

Noema sees:

UNKNOWN

Blind retry may create:

duplicate user

unless:

idempotency key

or:

postcondition reconciliation

prevents it.

⸻

38. Retry and Semantic Identity

Retries must preserve the identity of the logical Action.

logical_action_id = A123

Attempts:

attempt_1
attempt_2
attempt_3

This enables Noema to reason:

these attempts represent one intended Action

rather than three independent Actions.

⸻

39. Retry and User Intent

A retry must not change the underlying Intent.

Intent:
"Renew my card."

Attempt 1 and Attempt 2 remain attempts to realize:

the same resolved Intent

A retry must not silently introduce a new interpretation.

⸻

40. Retry and Planning

A retry normally does not require a new Plan if:

same Action
same Intent
same semantic objective

But a failed precondition or changed external state may invalidate the existing Plan.

Then:

retry

may become:

replan

⸻

41. Retry vs Replan

Retry

Same Action remains valid.

A → failure
A → retry

Replan

Current Action or Plan is no longer valid.

A → precondition failure
      ↓
new plan

Noema must not use retries to compensate for an invalid plan.

⸻

42. Retry and Human Intervention

Human intervention may be required when:

retry budget exhausted
authorization changed
risk increased
provider state ambiguous
postcondition cannot be established
policy requires approval

Example:

Attempt 1 → UNKNOWN
Reconciliation → UNKNOWN
Retry not safe
        ↓
Human Intervention

⸻

43. Retry and Risk

The higher the Action’s consequence, the stronger the retry safeguards should be.

A conceptual policy:

Low risk:
limited automatic retry
Medium risk:
retry with idempotency and bounded attempts
High risk:
reconciliation + explicit safety conditions
Critical:
human or policy-controlled retry

Risk semantics belong to the Trust model.

⸻

44. Retry and Authorization Expiry

Authorization may expire during retry.

Example:

Authorization:
valid until 12:00
Attempt 1:
11:59
Attempt 2:
12:01

The second attempt must not inherit the first attempt’s authorization blindly.

⸻

45. Retry and Policy Changes

Policies can change between attempts.

Example:

Attempt 1:
policy version 3
Attempt 2:
policy version 4

Noema must define whether the retry:

uses original policy snapshot

or:

must satisfy current policy

For consequential Actions, this should be explicit rather than inferred.

⸻

46. Retry and Contract Versioning

Likewise:

ActionContract v1

may differ from:

ActionContract v2

A retry should preserve the semantic contract under which the logical Action was created, unless the execution model explicitly permits migration.

⸻

47. Retry and Determinism

Retry decisions should be deterministic from:

Action
attempt history
current state
preconditions
authorization
policy
retry policy
risk
evidence

Given the same inputs, the decision should be reproducible:

RETRY
DO_NOT_RETRY
RECONCILE
INTERVENE
REPLAN

⸻

48. Retry and LLMs

LLMs should not independently decide:

"this probably failed, let's try again."

For consequential Actions, retry decisions should be derived from:

structured execution state
structured errors
postcondition evaluation
retry policy
risk policy

An LLM may assist with classification of unstructured provider messages, but the final retry decision should be deterministic.

⸻

49. Retry Observability

Every attempt should expose:

logical_action_id
execution_id
attempt_id
attempt_number
started_at
completed_at
failure_class
error
precondition_snapshot
postcondition_result
retry_decision
retry_policy
next_attempt_at

This allows operators to understand:

why did Noema retry?

⸻

50. Retry Auditability

A consequential retry should answer:

Why was it retried?
Which attempt preceded it?
What evidence established that retry was safe?
Which policy permitted it?
Were preconditions revalidated?
Was authorization revalidated?
Was idempotency protection present?

The execution record should make these questions answerable.

⸻

51. Retry Events

Conceptually useful events include:

ACTION_ATTEMPT_STARTED
ACTION_ATTEMPT_FAILED
ACTION_ATTEMPT_UNKNOWN
RETRY_EVALUATED
RETRY_APPROVED
RETRY_BLOCKED
RETRY_SCHEDULED
RECONCILIATION_STARTED
RECONCILIATION_COMPLETED
RETRY_BUDGET_EXHAUSTED

Exact event naming belongs to the broader execution event model.

⸻

52. Retry Policy

A Retry Policy may conceptually contain:

RetryPolicy {
    max_attempts
    max_elapsed_time
    retryable_failures
    backoff_strategy
    initial_delay
    max_delay
    jitter
    requires_idempotency
    reconcile_before_retry
}

Not every Action needs every field.

⸻

53. Retry Classification

A useful canonical classification:

RETRYABLE
NOT_RETRYABLE
RECONCILE_FIRST
REPLAN_REQUIRED
HUMAN_INTERVENTION_REQUIRED

These are decisions, not merely error codes.

⸻

54. Retry Decision Matrix

Situation	Default Decision
Definitive transient failure	Retry if policy permits
Definitive permanent failure	Do not retry
Precondition failure	Re-evaluate/replan
Authorization failure	Do not automatically retry
Unknown external outcome	Reconcile first
Postcondition satisfied	Do not retry
Postcondition not satisfied	Evaluate retry policy
Retry budget exhausted	Stop
Idempotency unavailable for unsafe Action	Block retry
Policy requires human approval	Intervene
Contract no longer valid	Replan
Previous attempt still running	Do not start concurrent retry

⸻

55. Retry Invariants

Invariant 1

A retry is a new attempt of the same logical Action.

Invariant 2

Every attempt must have a distinct execution identity.

Invariant 3

Retries must be bounded.

Invariant 4

Retries must not be triggered solely by uncertainty.

Invariant 5

Unknown execution state requires reconciliation before retry when duplicate effects are possible.

Invariant 6

Required preconditions must be re-evaluated before retry.

Invariant 7

Authorization must be revalidated when required by policy or contract.

Invariant 8

Retry safety must be established for non-idempotent Actions.

Invariant 9

A satisfied postcondition terminates the need for retry.

Invariant 10

Retries must not create concurrent executions of the same consequential Action unless explicitly permitted.

Invariant 11

Retry must not silently change the user’s Intent.

Invariant 12

Retry must not be used to compensate for an invalid Plan.

Invariant 13

Retry decisions must be deterministic given the same structured state and policies.

Invariant 14

Retry history must be immutable and auditable.

Invariant 15

Retry policy must distinguish transient failure from unknown outcome.

Invariant 16

Retry exhaustion must produce an explicit terminal state.

Invariant 17

Retry must respect Action risk and Trust requirements.

Invariant 18

A retry must not bypass authorization, policy, or precondition checks.

⸻

56. Canonical Mental Model

                     ACTION
                        │
                        ▼
                 PRECONDITIONS
                        │
                        ▼
                    EXECUTE
                        │
                        ▼
                    ATTEMPT
                        │
          ┌─────────────┼──────────────┐
          ▼             ▼              ▼
       SUCCESS        FAILURE        UNKNOWN
          │             │              │
          ▼             ▼              ▼
        DONE      RETRY EVALUATION   RECONCILE
                        │              │
                 ┌──────┼──────┐       │
                 ▼      ▼      ▼       ▼
              RETRY   STOP   REPLAN  EFFECT?
                 │               │      │
                 ▼               │  ┌───┴───┐
            NEW ATTEMPT           │  ▼       ▼
                 │               │ YES      NO
                 └───────────────┘  │        │
                                    ▼        ▼
                                   DONE   RETRY EVAL

⸻

57. Canonical Execution Loop

The complete Noema execution loop becomes:

Resolved Intent
      ↓
Plan
      ↓
Action Contract
      ↓
Precondition Evaluation
      ↓
Authorization / Trust Evaluation
      ↓
Execute Attempt
      ↓
Observe Evidence
      ↓
Postcondition Evaluation
      ↓
┌───────────┼────────────┐
▼           ▼            ▼
SUCCESS    FAILURE      UNKNOWN
│           │            │
▼           ▼            ▼
DONE    Retry Policy   Reconcile
            │            │
       ┌────┼────┐       │
       ▼    ▼    ▼       ▼
     RETRY STOP REPLAN  Outcome?
       │                 │
       ▼             ┌───┴───┐
   Revalidate        ▼       ▼
   Preconditions   SUCCESS  NO EFFECT
       │                    │
       ▼                    ▼
   New Attempt          Retry Eval

⸻

58. Final Definition

A retry is a bounded, policy-governed re-attempt of the same logical Action after a previous attempt failed to establish its required Outcome. Retries require fresh evaluation of relevant preconditions, authorization, execution state, and safety constraints. When the result of the previous attempt is unknown, Noema must reconcile before retrying whenever duplicate or consequential effects are possible.

The core invariant is:

Noema never retries because “something went wrong.” It retries only when the system can establish that another attempt is permitted, safe, still relevant to the same Intent, and capable of producing the required Outcome without creating an uncontrolled duplicate effect.