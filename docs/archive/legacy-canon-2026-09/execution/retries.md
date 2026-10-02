> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Retries

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/retries.md

⸻

1. Definition

A retry is a new execution attempt of the same logical Action after a previous attempt failed to establish the required Outcome, performed under explicit retry semantics and safety constraints.

A retry is not simply:

run the same thing again

It is:

evaluate current conditions
        ↓
determine whether retry is permitted and safe
        ↓
create a new execution attempt
        ↓
observe and verify the result

A retry preserves the semantic identity of the logical Action. It does not create a new Intent merely because another attempt is required.

⸻

2. Core Principle

Noema must never retry a consequential Action merely because the previous attempt failed, timed out, or became uncertain.

Before retrying, Noema must determine:

* whether retry is permitted;
* whether retry is safe;
* whether the Action remains valid;
* whether required preconditions remain satisfied;
* whether the previous attempt may already have produced the intended effect;
* whether authorization remains valid;
* whether required idempotency protection exists;
* whether the retry budget remains;
* whether the current Plan and Action Contract remain applicable.

⸻

3. Retry in the Noema Architecture

Retry is an execution control mechanism downstream of Intent, Trust, planning, Action Contracts, and execution.

The canonical relationship is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolution
      ↓
Context / State Reconciliation
      ↓
Deterministic Trust
      ↓
EAG / Planner
      ↓
Action Contract
      ↓
Final Runtime Validation
      ↓
Execution Attempt
      ↓
Verification / State Reconciliation
      ↓
Retry Evaluation
      ↓
New Execution Attempt

Retry does not bypass any upstream safety boundary.

⸻

4. Hard Schema Validation and Admission

Retry-related definitions, policies, decisions, and execution records must themselves pass the applicable hard schema validation and admission boundary before they become canonical execution inputs.

External retry information is untrusted until validated.

This includes:

* provider responses;
* consumer responses;
* retry-after metadata;
* failure classifications;
* execution state reports;
* event payloads;
* model-generated classifications;
* user-provided claims.

Persistence alone does not make retry information authoritative.

⸻

5. Why Retries Exist

Distributed execution is inherently unreliable.

An Action may encounter:

* timeout;
* connection failure;
* provider error;
* process crash;
* network partition;
* rate limit;
* temporary unavailability;
* dependency failure;
* unknown execution state.

Failure to receive a response does not necessarily mean the external Action did not occur.

Therefore Noema must distinguish:

execution failed

from:

execution result unknown

before considering retry.

⸻

6. Retry Is a New Attempt

Every retry is a distinct execution attempt.

Logical Action A
 ├── Attempt 1
 ├── Attempt 2
 └── Attempt 3

Attempts should have distinct identities such as:

action_instance_id
execution_id
attempt_id
attempt_number

The exact identity model is defined by the broader execution model and contracts.

Distinct attempt identity is necessary for:

* auditability;
* idempotency;
* observability;
* reconciliation;
* provider correlation;
* recovery.

⸻

7. Retry Does Not Reset Execution History

If:

Attempt 1 → TIMEOUT
Attempt 2 → SUCCESS

the historical execution record remains:

Attempt 1: TIMEOUT
Attempt 2: SUCCESS

Noema must not rewrite Attempt 1 as though it never occurred.

The retry establishes a new attempt, not a correction of historical execution history.

⸻

8. Retry vs Re-execution

These concepts remain distinct.

Retry

The same semantic Action is attempted again because the previous attempt did not establish the required result.

Re-execution

A new execution of an Action is intentionally requested, potentially because the user or workflow explicitly requested the operation again.

For example:

User:
"Send the report again."

is not necessarily a retry.

The resulting Intent and Action semantics determine whether the request is a new logical Action or a retry of an existing one.

⸻

9. Retry vs Compensation

A retry attempts to achieve the same intended effect.

Compensation attempts to mitigate or reverse an effect that has already occurred.

Retry:
attempt the same intended operation again
Compensation:
perform a separate corrective Action

For example:

charge payment
        ↓
retry if confirmed not to have occurred
refund payment
        ↓
compensation after a charge has occurred

Noema must not use compensation semantics to justify a retry or vice versa.

⸻

10. Retry vs Reconciliation

Reconciliation attempts to determine what actually happened.

Retry:
"Try it again."
Reconciliation:
"Determine whether it already happened."

For uncertain consequential Actions:

UNKNOWN
   ↓
STATE RECONCILIATION
   ↓
postcondition / business-state evaluation

Only when sufficient authoritative evidence establishes that the required effect did not occur should retry normally become a candidate.

⸻

11. State Reconciliation Is First-Class

State Reconciliation is a platform capability, not merely an implementation detail of retry.

The relevant flow is:

Enterprise System of Record
        ↓
Observation
        ↓
Hard Schema Validation / Admission
        ↓
State Reconciliation
        ↓
Reconciled Facts / Fact Status / Evidence
        ↓
Retry Evaluation

This is particularly important when:

* execution is UNKNOWN;
* responses are delayed;
* systems are eventually consistent;
* multiple systems disagree;
* an attempt may have committed before communication failed;
* provider state cannot be established from the original response.

⸻

12. Fact Status

Fact Status is distinct from:

* Evidence;
* Execution Status;
* Context;
* Outcome.

A useful canonical set is:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Evidence:
provider response received at 12:01
Fact Status:
VERIFIED for claim X

Evidence is what was observed or supplied.

Fact Status describes the current epistemic status of the relevant claim after appropriate validation and reconciliation.

Model confidence is not Fact Status.

⸻

13. Unknown Is First-Class

UNKNOWN means that Noema cannot currently establish the relevant execution or business-state fact.

It does not mean:

FAILED

and it does not mean:

SUCCEEDED

An unknown state must not be converted into either outcome merely to make retry logic easier.

⸻

14. Unknown Execution State

Consider:

Noema
  ↓
POST /charge
  ↓
Provider processes charge
  ↓
Network connection fails
  ↓
No response

Noema cannot conclude:

charge failed

The correct execution state may be:

UNKNOWN

The next step is reconciliation.

⸻

15. Unknown Must Trigger Reconciliation Before Retry

For consequential Actions:

UNKNOWN
   ↓
RECONCILE
   ↓
determine current state

If reconciliation establishes:

payment.status = SETTLED

then:

do not retry

If sufficient authoritative evidence establishes:

required effect did not occur

then retry may become eligible.

If reconciliation remains:

UNKNOWN

Noema must not guess.

The Action may instead require continued reconciliation, escalation, or another policy-defined control path.

⸻

16. Hard Validation of External Execution Information

Provider and consumer execution responses must not be treated as authoritative merely because they report:

failed
success
not found
already processed
retryable

They must first pass the applicable validation and admission rules.

Semantic authority remains claim-specific.

A source can provide evidence without being authoritative for every claim.

⸻

17. Retry Eligibility

A retry should be considered only when the applicable conditions establish that:

retry policy permits it
AND
retry budget remains
AND
Action remains valid
AND
required preconditions are satisfied
AND
required authorization remains valid
AND
retry is safe
AND
no successful effect has been established
AND
no conflicting active attempt owns execution

Additional Action-specific conditions may apply.

⸻

18. Preconditions Must Be Re-Evaluated

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

Therefore the retry must not proceed merely because the first attempt was uncertain.

The current Action Contract and relevant state determine whether the next step is blocking, replanning, clarification, escalation, or another control path.

⸻

19. Authorization Must Be Re-Evaluated

Authorization can change between attempts.

Example:

Attempt 1:
authorization = valid
Attempt 2:
authorization = revoked

The second attempt must not inherit the first attempt’s authorization blindly.

Technical authorization, policy authorization, and business authorization remain distinct.

A retry key or previous Trust decision does not grant authority.

⸻

20. Trust Outcomes Remain Canonical

Retry evaluation must not create additional Trust outcomes.

The canonical Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

Retry-specific states such as:

RETRYABLE
RECONCILE_FIRST
BLOCKED
REQUIRES_REVALIDATION
WAITING
RETRY_SCHEDULED
BUDGET_EXHAUSTED

are execution or control semantics.

EXECUTE means that the applicable Trust conditions permit proceeding. It does not mean that the retry will succeed.

⸻

21. Trust EXECUTE Does Not Mean Success

A Trust decision of:

EXECUTE

means the resolved Action satisfies the applicable Trust conditions and is permitted to proceed.

It does not establish:

execution success

and it does not establish:

enterprise business-state change

Execution and verification establish what happened.

⸻

22. Idempotency Is a Primary Retry Safety Mechanism

Retries are safest when the Action is idempotent.

Conceptually:

f(f(x)) = f(x)

For example:

set account.status = ACTIVE

Repeated execution can produce the same resulting state.

Contrast:

charge ₦100,000

which is not inherently idempotent.

Blindly repeating it can produce:

₦100,000
+
₦100,000

instead of one intended charge.

⸻

23. Idempotency Keys

For operations that require protection against duplicate effects, the Action Contract may define an idempotency mechanism.

Conceptually:

idempotency_key = logical_action_id

The provider may use that key to recognize repeated attempts of the same logical operation.

For example:

Attempt 1:
charge(key=abc123)
Attempt 2:
charge(key=abc123)

The provider may recognize both attempts as belonging to the same logical operation.

The exact mechanism belongs to the Action Contract and consumer/provider integration.

⸻

24. Idempotency Does Not Mean Retry Is Always Safe

Even an idempotent Action may have:

* side effects;
* rate limits;
* external dependencies;
* time-sensitive conditions;
* authorization changes;
* resource contention;
* policy constraints.

Therefore:

idempotent
≠
automatically retryable

Idempotency is a safety property, not retry permission.

⸻

25. Retry and Idempotency Identity

The idempotency identity should be linked to the logical Action rather than generated independently for every attempt.

Conceptually:

Intent Version
      ↓
Action Instance
      ↓
Idempotency Identity
      ↓
Attempt 1
Attempt 2
Attempt 3

Creating a new idempotency identity for every retry can defeat the protection against duplicate effects.

Materially changing the semantic Action creates a new logical Action and therefore requires a new semantic identity.

⸻

26. Retry and Intent Identity

A retry normally preserves the exact admitted intent_version.

For example:

Intent v7
   ↓
Action A
   ↓
Attempt 1
   ↓
Attempt 2

Both attempts remain associated with Intent v7.

The admitted Intent is immutable.

A material change to the requested goal or meaning creates a new Intent version with explicit lineage rather than silently modifying the original.

⸻

27. Resolved Identity Must Be Preserved

For consequential Actions, retry lineage must preserve the resolved:

* actor;
* principal;
* Action;
* exact target;
* resource;
* scope;
* resolution identity;
* relevant delegation/effective identity.

A retry must not silently change the target or actor.

If those semantics change, the system is no longer merely retrying the same logical Action.

⸻

28. Retry After Definitive Failure

A retry may be more straightforward when failure is definitive.

Example:

Provider:
503 Service Unavailable
Contract establishes:
operation was not accepted

Retry may become eligible, subject to:

* retry policy;
* current preconditions;
* current authorization;
* idempotency requirements;
* budget;
* Action risk;
* current Plan validity.

A transport error alone does not establish that the operation was not accepted.

⸻

29. Error Classification

Retry decisions should depend on structured error classification.

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
consumer crash after dispatch

Requires reconciliation where duplicate effects are possible.

Authorization

403 Forbidden

Normally not automatically retryable.

Precondition

insufficient balance
resource already inactive

Normally requires state change, clarification, or replanning rather than blind retry.

⸻

30. Retryability Must Be Explicit

The executor should not infer:

network error → retry

solely from a transport error.

The Action Contract or applicable Retry Policy should define retryable conditions.

Conceptually:

RetryPolicy {
    max_attempts
    max_elapsed_time
    retryable_failures
    backoff
    timeout
    jitter
    requires_idempotency
    reconcile_before_retry
}

The actual schema belongs to the contract and policy definitions.

⸻

31. Retry Classification

A useful execution-level classification is:

RETRYABLE
NOT_RETRYABLE
RECONCILE_FIRST
REPLAN_REQUIRED
HUMAN_INTERVENTION_REQUIRED

These are retry-control decisions, not Trust outcomes.

⸻

32. Retry Budget

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

33. Retry Budget vs Execution Timeout

These are different controls.

Execution timeout

How long one attempt may execute.

max_attempt_duration = 30s

Retry budget

How many attempts may be made.

max_attempts = 3

Both may apply simultaneously.

⸻

34. Time-Based Retry Budgets

A Retry Policy may also constrain total retry duration.

Example:

retry_window = 10 minutes

Even if:

max_attempts = 10

Noema must stop retrying after the retry window expires.

Expiration is a control condition and must not be interpreted as evidence that the Action succeeded or failed.

⸻

35. Exponential Backoff

Retries commonly use backoff for transient failures.

Conceptually:

delay = base × 2^attempt

For example:

Attempt 1 → immediate
Attempt 2 → 1s
Attempt 3 → 2s
Attempt 4 → 4s

Exact values are policy-defined.

Backoff changes scheduling, not the semantic decision of whether retry is permitted.

⸻

36. Jitter

Distributed systems may require randomized jitter to prevent synchronized retries.

Conceptually:

delay = exponential_backoff + jitter

Jitter may make the exact scheduling time non-deterministic.

The underlying retry decision should remain determined by structured policy and state.

⸻

37. Retry Storms

Unbounded or synchronized retries can cause:

* service overload;
* queue saturation;
* cascading failures;
* rate-limit amplification;
* dependency exhaustion.

Retry policy is therefore both an execution-safety mechanism and a system-stability mechanism.

⸻

38. Retry and Rate Limits

A provider may return:

429 Too Many Requests

Noema should respect provider-defined retry guidance such as:

Retry-After

when that information is validated and applicable.

Repeatedly retrying immediately can amplify the failure.

⸻

39. Retry and Dependency Failure

Suppose:

Noema
  ↓
Payment Service
  ↓
Bank

If the bank is unavailable, repeatedly retrying the Payment Service may not improve the situation.

Retry policy should account for the actual failure domain and dependency state where available.

⸻

40. Retry and Circuit Breaking

Repeated failures may justify temporarily preventing further attempts.

Conceptually:

HEALTHY
   ↓
FAILURES
   ↓
OPEN
   ↓
WAIT
   ↓
HALF_OPEN
   ↓
TEST

Circuit breaking is execution infrastructure.

It can influence whether a retry may be scheduled, but it does not itself establish business Outcome.

⸻

41. Retry and Concurrency

Retries can overlap with previous attempts if the original attempt is merely slow.

Example:

Attempt 1 still executing
Attempt 2 starts

This can create duplicate execution.

Before starting another attempt, Noema should establish whether the previous attempt is:

* completed;
* definitively failed;
* unknown;
* still executing;
* owned by another execution consumer.

⸻

42. No Concurrent Retries by Default

For consequential Actions:

one active attempt per logical Action

should be the default unless the Action Contract explicitly permits concurrent execution.

Concurrent attempts require explicit semantics because they may create duplicate or conflicting effects.

⸻

43. Retry and Execution Leases

Long-running execution may use an execution lease.

Conceptually:

attempt owns execution lease

A retry should not begin until the previous ownership is:

definitively terminated

or:

lease has safely expired

according to the execution model.

A distributed lock is only a mechanism; it is not itself proof that duplicate effects are impossible.

⸻

44. Retry and Consumer Crashes

Consider:

consumer receives Action
        ↓
executes external operation
        ↓
consumer crashes

Noema may not know whether the external operation completed.

The appropriate state may therefore be:

UNKNOWN

rather than:

FAILED

until sufficient evidence establishes the result.

⸻

45. Retry and Postconditions

Postconditions are central to safe retry.

Attempt
   ↓
Observed Evidence
   ↓
State Reconciliation
   ↓
Postcondition Evaluation
   ↓
Result

If:

YES

then no retry is required.

If:

NO

retry may be evaluated.

If:

UNKNOWN

reconciliation remains necessary.

A previous Action’s postcondition does not become permanently true merely because it was once observed.

⸻

46. Retry and Precondition/Postcondition Relationship

A useful execution loop is:

Evaluate Runtime Preconditions
        ↓
Execute
        ↓
Observe
        ↓
Verify / Reconcile
        ↓
Evaluate Required Postconditions
        ↓
 ┌──────────┼──────────┐
 ▼          ▼          ▼
PASS       FAIL      UNKNOWN
 │          │          │
 ▼          ▼          ▼
DONE   Retry Eval   Reconcile
             │
             ▼
       Revalidate

The exact verification and reconciliation path is Action-specific.

⸻

47. Retry and Partial Effects

An Action can fail after producing partial effects.

Example:

create_user
Provider creates user
but response is lost

Noema sees:

UNKNOWN

Blind retry may create a duplicate user.

Idempotency protection or State Reconciliation should establish whether the intended effect already exists before another attempt.

⸻

48. Retry and Composite Actions

For composite Actions, retry semantics must preserve parent and child identities.

Conceptually:

Plan P
 ├── Action A
 ├── Action B
 └── Action C
      ├── Attempt 1
      └── Attempt 2

A retry of C is not automatically a retry of A or B.

Previously committed child effects must be considered before retrying subsequent work.

Replanning and compensation remain distinct mechanisms.

⸻

49. Retry and Compensation After Partial Execution

Suppose:

Step A → SUCCESS
Step B → SUCCESS
Step C → UNKNOWN

Noema must reconcile Step C before deciding whether to:

* retry C;
* compensate prior effects;
* escalate;
* replan.

Compensation must not be used merely because execution is uncertain.

⸻

50. Retry and Semantic Identity

Retries preserve the identity of the logical Action.

Conceptually:

logical_action_id = A123
attempt_1
attempt_2
attempt_3

This allows Noema to distinguish:

three attempts of one intended Action

from:

three independent Actions

⸻

51. Retry and Planning

A retry normally does not require a new Plan if:

* the same semantic Action remains valid;
* the same Intent remains applicable;
* the same objective remains valid;
* required conditions remain satisfied.

However, changed external state can invalidate the existing Plan.

For example:

Attempt fails
    ↓
precondition changes
    ↓
existing Plan no longer valid
    ↓
REPLAN

Retry must not be used to compensate for an invalid Plan.

⸻

52. Retry vs Replan

Retry

Same Action remains valid.
A → failure
A → retry

Replan

Current Action or Plan is no longer valid.
A → changed state
      ↓
new Plan

A replan may contain different Actions.

It must account for all effects already produced by previous execution attempts.

⸻

53. Plan Validity vs Runtime Eligibility

A Plan being structurally valid does not guarantee that a retry is currently executable.

For example:

Plan = VALID

while:

authorization = revoked

or:

precondition = NOT_SATISFIED

or:

resource state = UNKNOWN

The runtime eligibility decision must use current applicable state and controls.

⸻

54. Retry and Human Intervention

Human intervention may be required when:

* retry budget is exhausted;
* authorization changed;
* risk increased;
* provider state remains ambiguous;
* postcondition cannot be established;
* policy requires approval;
* recovery options are exhausted.

Example:

Attempt 1 → UNKNOWN
      ↓
Reconciliation → UNKNOWN
      ↓
Retry not safely established
      ↓
ESCALATE
      ↓
Human Intervention

Human intervention does not rewrite the previous execution history.

⸻

55. Retry and Risk

The required retry safeguards depend on the Action’s consequence and applicable Trust policy.

A policy may require:

Low risk:
limited automatic retry
Medium risk:
bounded retry + idempotency
High risk:
reconciliation + stronger runtime conditions
Critical:
explicit policy or human-controlled transition

These are illustrative policy structures, not universal risk thresholds.

Risk informs Trust and execution policy; risk itself does not authorize retry.

⸻

56. Retry and Authorization Expiry

Authorization may expire between attempts.

Example:

Authorization:
valid until 12:00
Attempt 1:
11:59
Attempt 2:
12:01

Attempt 2 must not inherit the first attempt’s authorization blindly.

The applicable authorization and policy semantics determine whether a new Trust evaluation is required.

⸻

57. Retry and Policy Changes

Policies can change between attempts.

Example:

Attempt 1:
Policy v3
Attempt 2:
Policy v4

Noema must define whether the retry:

* remains governed by the original policy snapshot;
* must satisfy current policy;
* requires explicit revalidation.

For consequential Actions, this behavior must be explicit rather than inferred.

⸻

58. Retry and Contract Versioning

Likewise:

Action Contract v1

may differ semantically from:

Action Contract v2

A retry normally preserves the semantic contract associated with the logical Action unless the execution model explicitly permits migration.

Published contract meaning must not silently change underneath historical attempts.

⸻

59. Version Lineage

Retry records may need to preserve relevant versions including:

* intent_version;
* Action version;
* Action Contract version;
* Trust Contract version;
* Trust Decision version;
* policy version;
* EAG version;
* Capability Registry version;
* integration mapping version;
* system/provider version;
* resource/business-state version;
* retry policy version.

Transport or schema versions are separate from semantic contract versions.

Historical records remain immutable.

⸻

60. Retry and Determinism

The semantic retry decision should be deterministic from the applicable structured inputs, including:

* logical Action identity;
* attempt history;
* current reconciled state;
* preconditions;
* authorization;
* policy;
* Retry Policy;
* risk;
* evidence;
* idempotency state;
* active execution state.

Conceptually:

RETRY
DO_NOT_RETRY
RECONCILE
INTERVENE
REPLAN

The exact scheduling delay may include intentional non-determinism such as jitter.

⸻

61. Retry and LLMs

An LLM must not independently decide:

"this probably failed, let's try again."

For consequential Actions, retry decisions should derive from:

* structured execution state;
* validated errors;
* State Reconciliation;
* postcondition evaluation;
* Retry Policy;
* preconditions;
* authorization;
* Trust requirements;
* idempotency state.

An LLM may assist in classifying unstructured provider messages, but the resulting information remains non-authoritative until validated and deterministically admitted.

The LLM cannot directly trigger consequential execution.

⸻

62. Retry Observability

Every attempt should expose structured information such as:

logical_action_id
execution_id
attempt_id
attempt_number
intent_version
started_at
completed_at
failure_class
error
precondition_snapshot
postcondition_result
reconciliation_reference
retry_decision
retry_policy_version
next_attempt_at

This allows operators to answer:

Why did Noema retry?

⸻

63. Retry Auditability

A consequential retry should make it possible to determine:

* why it was retried;
* which attempt preceded it;
* what evidence established retry eligibility;
* whether State Reconciliation occurred;
* which preconditions were evaluated;
* which authorization was evaluated;
* which policy permitted retry;
* which Action Contract governed it;
* what idempotency protection existed;
* whether the previous attempt could have succeeded;
* what changed between attempts.

This is part of Noema’s causal audit model.

⸻

64. Causal Retry Audit

A consequential retry should preserve a lineage similar to:

Source of Intent
      ↓
Intent Version
      ↓
Resolved Actor / Action / Target
      ↓
Trust Decision
      ↓
Plan
      ↓
Action Contract
      ↓
Execution
      ↓
Attempt 1
      ↓
Evidence
      ↓
State Reconciliation
      ↓
Retry Evaluation
      ↓
Attempt 2
      ↓
Verification / Reconciliation
      ↓
Outcome

The audit should explain the transition without exposing private model chain-of-thought.

⸻

65. Retry Events

Conceptually useful execution events include:

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

Exact event naming belongs to the broader Event Model.

Event occurrence does not itself establish business-state truth.

⸻

66. Retry Policy

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

Not every Action requires every field.

The policy must remain subordinate to:

* Action semantics;
* Action Contract;
* Trust;
* authorization;
* current state;
* system/provider constraints.

⸻

67. Retry Policy Does Not Grant Authority

A Retry Policy can say:

retry at most 3 times

It cannot independently grant permission to execute the Action.

Authorization and Trust remain separate.

Likewise:

idempotency_key
retry_budget
backoff

do not constitute authority.

⸻

68. Retry and Capability Availability

A retry requires an available execution path.

If the required Capability or consumer is unavailable, Noema must not invent an alternative operation merely to continue retrying.

The planner is bounded by:

Enterprise Action Graph
Capability Registry
Action Model
Action Contracts

Noema may replan when the original execution path is no longer available, subject to Trust and Intent semantics.

⸻

69. Retry and Security

Retry infrastructure must preserve the structural security boundary.

The following are untrusted inputs until appropriately validated:

* user input;
* model output;
* retrieved enterprise text;
* tool responses;
* provider responses;
* consumer reports;
* external events.

The model must not have direct credentials or arbitrary enterprise access.

No free-form model output may directly create or authorize a retry execution.

The executor must operate through explicit capabilities and Action Contracts.

⸻

70. Retry and Read-Only Actions

Idempotency is most critical for side-effecting Actions, but retry safety also applies to read-only operations.

Repeated read operations can still be consequential when they:

* access protected data;
* trigger rate limits;
* consume expensive resources;
* invoke external systems;
* produce audit or operational effects.

Therefore read-only does not mean retry policy can be ignored.

⸻

71. Retry and Operational Memory

Operational Memory may retain:

* previous attempts;
* retry decisions;
* failure patterns;
* reconciliation results;
* intervention history.

Operational Memory is historical execution knowledge.

It is not:

* enterprise business-state authority;
* authorization authority;
* permission;
* a replacement for State Reconciliation;
* generic model memory.

Historical retry records must not be treated as current truth without appropriate revalidation.

⸻

72. Replay

Replay of retry history is non-executing by default.

Replay may reconstruct:

what happened
why retry was selected
what evidence existed
which policy applied

It must not silently create a new external side effect.

A replay that intentionally creates a new execution is a new explicitly governed operation, not historical replay.

⸻

73. Retry and Time

Retry decisions are time-sensitive.

Relevant temporal values may include:

* attempt start time;
* attempt completion time;
* policy effective time;
* authorization validity;
* resource version time;
* evidence observation time;
* retry-window deadline;
* contract expiry;
* provider retry guidance.

Recency alone does not establish authority.

A newer observation from a non-authoritative source cannot automatically override an older authoritative observation.

⸻

74. Retry and Concurrency Control

A retry must account for concurrent state changes.

Where appropriate, safe execution may require:

* transactions;
* atomic conditional mutations;
* resource versions;
* ETags;
* compare-and-set;
* leases;
* reservations;
* provider idempotency keys.

The exact mechanism belongs to the relevant Action Contract and integration.

⸻

75. Retry and Expiration

A retry may become invalid when:

* the Intent expires;
* the Action Contract expires;
* authorization expires;
* policy validity ends;
* the retry window closes;
* the resource is no longer eligible;
* the Plan becomes stale;
* a provider operation is no longer valid.

Expiration is not itself proof that an external Action failed or succeeded.

⸻

76. Retry and Cancellation

Cancellation is distinct from retry.

A cancelled logical Action must not automatically become retryable.

If cancellation occurs after an external operation has already committed, the resulting business state must still be reconciled.

Cancellation does not erase historical attempts.

⸻

77. Retry and Human Decisions

A human may authorize a predefined retry transition where policy permits it.

The human decision must itself be validated against:

* human identity;
* required authority;
* Intent version;
* Action;
* target;
* current state;
* applicable policy.

A human approval does not itself establish execution success.

It also does not silently mutate the admitted Intent.

⸻

78. Retry Lifecycle

A conceptual retry lifecycle is:

ATTEMPT COMPLETED
      ↓
RETRY EVALUATING
      ↓
 ┌───────────────┬────────────────┬──────────────────┐
 ▼               ▼                ▼
RETRYABLE     RECONCILE       NOT RETRYABLE
 │               │                │
 ▼               ▼                ▼
SCHEDULE      STATE RESULT       STOP
 │               │
 ▼          ┌────┴────┐
NEW ATTEMPT ▼         ▼
          EFFECT     NO EFFECT
          EXISTS        │
             │          ▼
             ▼      RETRY EVALUATION
           STOP

Other control states may include:

WAITING
BLOCKED
REQUIRES_REVALIDATION
REPLAN_REQUIRED
HUMAN_INTERVENTION_REQUIRED
BUDGET_EXHAUSTED

These are execution-control states, not Trust outcomes.

⸻

79. Retry Decision Matrix

Situation	Default execution interpretation
Definitive transient failure	Retry if policy and safety conditions permit
Definitive permanent failure	Do not retry
Precondition failure	Re-evaluate and potentially replan
Authorization failure	Do not automatically retry
Unknown external outcome	Reconcile first
Postcondition satisfied	Do not retry
Postcondition not satisfied	Evaluate retry policy
Retry budget exhausted	Stop
Idempotency unavailable for unsafe Action	Block retry or require another governed path
Policy requires human approval	Escalate to intervention
Contract no longer valid	Replan or stop
Previous attempt still running	Do not start concurrent retry by default
Required Capability unavailable	Replan or escalate; do not invent a capability
Reconciliation remains UNKNOWN	Do not blind retry

⸻

80. Retry Does Not Establish Outcome

A retry is an attempt to establish the required result.

It does not itself establish:

SUCCESS

After every retry, Noema must still observe and verify the result.

The final Outcome is determined from execution evidence, verification, and appropriate enterprise state authority.

Outcome is distinct from enterprise Business State.

⸻

81. Retry and Outcome Classification

The execution layer should distinguish:

ATTEMPT STATUS

from:

OUTCOME

and from:

ENTERPRISE BUSINESS STATE

For example:

Attempt 1:
UNKNOWN
Attempt 2:
COMPLETED
Verification:
postcondition established
Outcome:
SUCCESS

The enterprise system remains authoritative for the corresponding business-state fact.

⸻

82. Retry Decision Is Not Outcome

The following are decisions or control states:

RETRY
DO_NOT_RETRY
RECONCILE
REPLAN
ESCALATE

They must not be presented as Outcomes.

Likewise:

RETRYABLE
REQUIRES_REVALIDATION
BUDGET_EXHAUSTED

are not Trust outcomes.

⸻

83. Retry and Precondition Snapshots

A retry evaluation should preserve the relevant precondition and state snapshot.

The snapshot records what was known at that point.

It is historical.

It does not become current enterprise truth merely because it was used to authorize an attempt.

A later retry requires current evaluation of volatile conditions.

⸻

84. Retry Invariants

Invariant 1

A retry is a new execution attempt of the same logical Action.

Invariant 2

Every execution attempt must have a distinct attempt identity.

Invariant 3

Retry lineage must preserve the exact admitted Intent version.

Invariant 4

Retries must preserve the semantic identity of the logical Action unless a new Action is explicitly created.

Invariant 5

Retries must be bounded.

Invariant 6

Retries must not be triggered solely by uncertainty.

Invariant 7

Unknown execution state requires reconciliation before retry when duplicate or consequential effects are possible.

Invariant 8

Relevant preconditions must be re-evaluated before retry.

Invariant 9

Authorization must be revalidated when required by policy, contract, or changed authority state.

Invariant 10

Retry safety must be established for non-idempotent Actions.

Invariant 11

Idempotency does not itself grant retry permission.

Invariant 12

A satisfied postcondition terminates the need for retry.

Invariant 13

Retries must not create concurrent executions of the same consequential Action unless explicitly permitted.

Invariant 14

A retry must not silently change the actor, target, resource, scope, or semantic Action.

Invariant 15

A retry must not silently change the user’s Intent.

Invariant 16

Retry must not be used to compensate for an invalid Plan.

Invariant 17

Replanning and retry are distinct execution controls.

Invariant 18

Retry decisions must respect current applicable Trust, policy, authorization, and preconditions.

Invariant 19

Trust EXECUTE does not establish execution success.

Invariant 20

Retry history must remain immutable and auditable.

Invariant 21

Retry policy must distinguish definitive failure from unknown execution state.

Invariant 22

Provider or consumer claims must not become authoritative merely because they report retryability.

Invariant 23

Hard schema validation and admission must precede canonical use of external execution information.

Invariant 24

State Reconciliation must be available as a first-class path for uncertain execution state.

Invariant 25

Fact Status must remain distinct from Evidence, Execution Status, Context, and Outcome.

Invariant 26

Timeout alone must not be treated as proof of failure.

Invariant 27

Idempotency identities must protect the logical Action rather than create independent semantics for each retry attempt.

Invariant 28

A retry must not bypass Action Contracts or the Capability Registry.

Invariant 29

A retry must not invent capabilities, permissions, authority, or recovery Actions.

Invariant 30

The model must not directly authorize or trigger consequential retries.

Invariant 31

Replay must not create external side effects by default.

Invariant 32

Operational Memory must not be treated as enterprise business-state authority.

Invariant 33

Historical precondition, authorization, and reconciliation snapshots must not be treated as current truth without revalidation.

Invariant 34

Retry decisions must account for concurrency and active execution ownership.

Invariant 35

Retry expiration and budget exhaustion must produce explicit control states.

Invariant 36

Compensation must remain distinct from retry.

Invariant 37

A retry does not establish an Outcome.

Invariant 38

Enterprise systems remain authoritative for the corresponding enterprise Business State.

Invariant 39

Read-only Actions may still require retry controls when their execution is consequential.

Invariant 40

The causal record of every consequential retry must preserve the Intent, Action, Trust, Contract, evidence, reconciliation, attempts, and resulting Outcome.

⸻

85. Canonical Mental Model

                    LOGICAL ACTION
                          │
                          ▼
                 RUNTIME PRECONDITIONS
                          │
                          ▼
                 TRUST / AUTHORIZATION
                          │
                          ▼
                  ACTION CONTRACT
                          │
                          ▼
                   EXECUTE ATTEMPT
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          SUCCESS       FAILURE      UNKNOWN
             │            │            │
             ▼            ▼            ▼
            DONE     RETRY EVAL    RECONCILE
                          │            │
                   ┌──────┼──────┐     │
                   ▼      ▼      ▼     ▼
                 RETRY   STOP   REPLAN EFFECT?
                   │               │    │
                   ▼               │ ┌──┴──┐
              NEW ATTEMPT          │ ▼     ▼
                   │               │YES    NO
                   └───────────────┘ │      │
                                     ▼      ▼
                                    DONE  RETRY EVAL

⸻

86. Canonical Execution Loop

The complete retry-aware execution loop is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolve Actor / Action / Target
      ↓
Context / State Reconciliation
      ↓
Deterministic Trust
      ↓
EAG / Planner
      ↓
Action Contract
      ↓
Final Runtime Preconditions
      ↓
Execute Attempt
      ↓
Observe Evidence
      ↓
Verify / State Reconciliation
      ↓
Postcondition Evaluation
      ↓
 ┌────────────┼─────────────┐
 ▼            ▼             ▼
SUCCESS      FAILURE       UNKNOWN
 │            │             │
 ▼            ▼             ▼
DONE     Retry Evaluation  Reconcile
              │             │
        ┌─────┼─────┐       │
        ▼     ▼     ▼       ▼
      RETRY  STOP REPLAN  Effect?
        │                    │
        ▼                ┌───┴───┐
Revalidate Runtime       ▼       ▼
Preconditions          YES      NO
        │               │        │
        ▼               ▼        ▼
 New Attempt           DONE   Retry Eval

⸻

87. Canonical Retry Principle

The retry loop is not:

failure → retry

It is:

attempt
  ↓
observe
  ↓
verify / reconcile
  ↓
determine current state
  ↓
evaluate retry eligibility
  ↓
revalidate
  ↓
retry only if safe and permitted

This distinction is fundamental to safe distributed execution.

⸻

88. Final Definition

A retry is a bounded, policy-governed new execution attempt of the same logical Action after a previous attempt failed to establish the required Outcome.

A retry preserves the exact semantic identity of the logical Action and its admitted Intent version while creating a distinct execution attempt. Before retrying, Noema must evaluate current preconditions, authorization, Trust requirements, Action Contract validity, execution ownership, retry policy, idempotency protection, and relevant enterprise state.

When the result of a previous attempt is unknown, Noema must use State Reconciliation before retrying whenever duplicate or consequential effects are possible.

The core invariant is:

Noema never retries because "something went wrong."
It retries only when the system can establish that another
attempt is permitted, safe, still relevant to the same logical
Action and Intent, and capable of proceeding without creating
an uncontrolled duplicate or violating current enterprise
constraints.

A retry is therefore an execution control decision, not a guess, not a new Intent, not compensation, and not evidence of success.