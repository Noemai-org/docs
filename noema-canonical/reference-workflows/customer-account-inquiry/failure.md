Failure

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/failure.md

⸻

1. Definition

Failure is the explicit representation of an execution that did not satisfy the conditions required for successful completion.

Within the Customer Account Inquiry workflow, Failure answers:

“What prevented the requested Action from completing successfully?”

Failure is an execution state and diagnostic classification. It is not an assumption that something went wrong merely because Noema did not immediately receive a response.

The distinction is fundamental:

Action
   ↓
Execution
   ↓
Result
   │
   ├── Success
   ├── Failure
   ├── Unknown
   └── Partial

⸻

2. Purpose

The purpose of Failure handling is to ensure that Noema:

detects failure
classifies failure
preserves evidence
determines recoverability
applies Policy
communicates accurately

Failure must lead to a deterministic next state.

It must never result in the model simply deciding what “probably happened.”

⸻

3. Core Principle

Failure must be distinguished from uncertainty.

For example:

Enterprise API
     ↓
HTTP 400
     ↓
known rejection
     ↓
FAILED

is different from:

Enterprise API
     ↓
connection lost
     ↓
execution outcome unknown
     ↓
UNKNOWN

Therefore:

No response ≠ Failure

and:

Failure ≠ Unknown

⸻

4. Failure Boundary

Failure belongs to the Execution domain.

Intent
   ↓
Context
   ↓
Trust
   ↓
Action
   ↓
Execution
   ↓
Failure

Failure should not be introduced merely because:

the model is uncertain

Model uncertainty belongs to Trust and Intent resolution.

Execution Failure describes what happened during Action execution.

⸻

5. Failure Categories

Failures in this workflow may include:

validation failure
authorization failure
resource failure
enterprise rejection
integration failure
network failure
timeout
dependency failure
verification failure
policy failure

Each category should have explicit semantics.

⸻

6. Validation Failure

A Validation Failure occurs when the Action request does not satisfy its Action Contract.

Example:

search_transactions
date_from > date_to

Result:

VALIDATION_FAILED

The Action should not be sent to the enterprise system.

Invalid Request
     ↓
Execution Blocked

⸻

7. Missing Context Failure

An Action may fail to become executable because required Context is unavailable.

Example:

Intent:
"Show me my balance."
Required:
account_id
Available:
customer_id only

Noema must not invent an account.

The correct transition may be:

Missing Context
      ↓
Clarification

rather than:

Missing Context
      ↓
Failure

Whether this is represented as a workflow failure or blocked execution depends on the broader state model.

⸻

8. Authorization Failure

Authorization Failure occurs when the Principal is not permitted to perform the Action against the target Resource.

Example:

Principal
    ↓
Account B
    ↓
Authorization Denied

Result:

AUTHORIZATION_FAILED

Noema must not retry authorization failures unless Policy explicitly indicates that authorization state may change and retry is appropriate.

⸻

9. Resource Failure

A requested Resource may not exist or may no longer be accessible.

Example:

account_id = 123
      ↓
Account Not Found

Possible result:

RESOURCE_NOT_FOUND

Noema should not substitute another account merely because it appears similar.

If multiple candidate Resources exist:

Ambiguous Resource
      ↓
Clarification

⸻

10. Enterprise Rejection

An enterprise system may receive a valid request but reject the Action according to its own Business Rules.

Example:

Noema
   ↓
retrieve_statement
   ↓
Statement System
   ↓
Request Rejected

The enterprise response is authoritative for the rejection.

Noema should preserve the returned reason where permitted.

⸻

11. Network Failure

A network failure occurs when Noema cannot successfully communicate with the enterprise capability.

Examples:

connection refused
connection reset
DNS failure
transport error

Network failure does not necessarily establish that the enterprise Action did not execute.

Therefore the resulting state may be:

NETWORK_FAILURE

with the execution Outcome potentially:

UNKNOWN

depending on when the failure occurred.

⸻

12. Timeout

A timeout occurs when the enterprise system does not respond within the configured execution window.

Example:

create_complaint
      ↓
request sent
      ↓
timeout

Noema cannot automatically conclude:

complaint was not created

The correct execution state may be:

UNKNOWN

followed by verification or reconciliation.

⸻

13. Dependency Failure

An Action may depend on another enterprise capability.

Example:

get_spending_summary
       ↓
Transaction System
       ↓
Aggregation Service
       ↓
Unavailable

The resulting failure should identify the dependency that prevented execution.

DEPENDENCY_FAILURE

This allows Policy to determine whether retry or escalation is appropriate.

⸻

14. Verification Failure

Execution may appear successful but fail its required Postcondition.

Example:

create_complaint
      ↓
HTTP 200
      ↓
Expected case_id absent
      ↓
Verification Failure

Result:

VERIFICATION_FAILED

This must not automatically be reported to the Customer as success.

⸻

15. Semantic Failure

A transport-level success does not guarantee semantic success.

Example:

HTTP 200
{
    status: "REJECTED"
}

The enterprise capability responded successfully, but the requested Business Action did not succeed.

Noema must classify the semantic result correctly.

Transport Success
      ≠
Business Success

⸻

16. Policy Failure

Execution may be blocked by Noema Policy even when the enterprise capability is available.

Example:

Action
   ↓
Policy
   ↓
Not permitted

Possible result:

POLICY_BLOCKED

No enterprise invocation should occur if Policy blocks execution before the execution boundary.

⸻

17. Failure vs Trust Failure

Trust Failure occurs before or during the decision to execute.

Execution Failure occurs after an Action has entered execution or after execution was attempted.

Example:

Ambiguous account
      ↓
Trust cannot establish sufficient confidence
      ↓
CLARIFY

This is not an Execution Failure.

By contrast:

Account resolved
      ↓
Action approved
      ↓
Enterprise API rejects request
      ↓
EXECUTION FAILURE

These states must remain distinct.

⸻

18. Failure vs Clarification

Clarification is appropriate when additional information from the Principal is required.

Example:

"Show me my account."

Multiple accounts:

Account A
Account B

Result:

AMBIGUOUS
   ↓
CLARIFY

Noema should not represent this as an enterprise execution failure.

⸻

19. Failure vs Escalation

Escalation is appropriate when the system cannot safely resolve a failure automatically.

Example:

Enterprise systems disagree
        ↓
Authority cannot be established
        ↓
ESCALATE

Escalation is therefore a Policy-driven response to a condition, not itself a failure category.

⸻

20. Failure Classification

A Failure should contain sufficient information to determine what happened.

Conceptually:

Failure {
    code
    category
    message
    execution_id
    action_id
    attempt
    source
    retryable
    recoverable
    occurred_at
    evidence
}

The exact schema is implementation-specific.

⸻

21. Failure Codes

Failure codes should be stable and machine-readable.

Examples:

VALIDATION_FAILED
AUTHORIZATION_FAILED
RESOURCE_NOT_FOUND
RESOURCE_UNAVAILABLE
ENTERPRISE_REJECTED
NETWORK_FAILURE
TIMEOUT
DEPENDENCY_FAILURE
VERIFICATION_FAILED
POLICY_BLOCKED

Human-readable messages may accompany these codes.

⸻

22. Retryability

A Failure should have explicit retry semantics.

Example:

TIMEOUT
    ↓
potentially retryable

while:

AUTHORIZATION_FAILED
    ↓
normally not retryable

Retryability must be determined by Action and Policy, not by the model.

⸻

23. Retry Safety

A Failure may be technically retryable but operationally unsafe to retry.

Example:

create_complaint
      ↓
timeout

The enterprise system may already have created the complaint.

Therefore:

retryable

must not automatically mean:

safe to repeat

Idempotency and reconciliation must be considered.

⸻

24. Failure Recovery

Recovery should follow a deterministic path.

Failure
   ↓
Classify
   ↓
Policy
   ├── Retry
   ├── Reconcile
   ├── Clarify
   ├── Escalate
   └── Reject

The model should not select the recovery path based solely on intuition.

⸻

25. Recovery After Read Failure

For a read Action:

get_account_balance
      ↓
TIMEOUT

Noema may:

retry

if Policy permits.

If the enterprise system remains unavailable:

retry exhausted
      ↓
ESCALATE / INFORM

Noema must not fabricate a balance.

⸻

26. Recovery After Statement Failure

For:

retrieve_statement

a temporary infrastructure failure may be retryable.

A permanent rejection may not be.

Example:

Service Unavailable
      ↓
Retry

versus:

Statement Not Available
      ↓
Do Not Retry
      ↓
Inform Customer

The distinction must be based on the enterprise result and Policy.

⸻

27. Recovery After Transaction Search Failure

For:

search_transactions

Noema may retry transient failures.

If the Transaction System returns a definitive error:

Invalid Date Range

Noema should correct or clarify the input rather than repeatedly retrying the same invalid request.

⸻

28. Recovery After Spending Summary Failure

A spending summary may depend on transaction data.

If the underlying Transaction System is unavailable:

get_spending_summary
        ↓
Dependency Failure

Noema may retry according to dependency Policy.

It must not replace the unavailable authoritative source with an unsupported estimate merely to produce an answer.

⸻

29. Recovery After Complaint Creation Failure

Complaint creation requires special handling because it changes enterprise state.

Example:

create_complaint
      ↓
timeout

Noema must consider:

Was the request accepted?
Does the enterprise system support idempotency?
Can the Case be queried?
Can the operation be reconciled?

Only after these questions are resolved should Noema determine whether another attempt is safe.

⸻

30. Unknown Outcome

Unknown is not a failure classification.

It is an execution outcome indicating that Noema cannot establish whether the Action succeeded or failed.

Execution
   ↓
Unknown
   ↓
Reconciliation

For state-changing Actions, Unknown should be treated conservatively.

⸻

31. Partial Failure

Compound Intents may result in partial failure.

Example:

get_account_balance
    → SUCCEEDED
search_transactions
    → FAILED

The overall workflow should preserve both outcomes.

It must not collapse them into:

FAILED

without retaining the successful Action.

⸻

32. Failure Propagation

A failed dependency may prevent downstream Actions.

Example:

resolve_account
      ↓
FAILED
      ↓
search_transactions
      ↓
BLOCKED

The downstream Action was not necessarily itself executed.

Therefore:

BLOCKED

must remain distinguishable from:

FAILED

⸻

33. Failure Cascades

Noema should prevent one failure from being incorrectly interpreted as multiple independent failures.

Example:

Transaction System unavailable
        ↓
search_transactions FAILED
        ↓
get_spending_summary BLOCKED

The root cause is the dependency failure.

Audit records should preserve the causal relationship.

⸻

34. Failure Evidence

Every consequential Failure should retain relevant Evidence.

Examples:

HTTP status
enterprise error code
response body reference
timeout information
request identifier
dependency identifier
timestamp
attempt number

Sensitive information should be subject to the applicable Data Boundaries.

⸻

35. Failure Provenance

Noema should be able to answer:

What failed?
Where did it fail?
When did it fail?
Which Action was being executed?
Which attempt failed?
What evidence established the failure?

Conceptually:

Failure
   ↓
Evidence
   ↓
Source
   ↓
Timestamp

⸻

36. Failure Auditability

Failure records should support reconstruction of the execution journey.

Example:

execution_id = EXE-123
action = retrieve_statement
attempt = 2
source = Statement System
failure = TIMEOUT
occurred_at = ...
retryable = true

This should allow operators to reconstruct the sequence without relying on model memory.

⸻

37. Customer-Facing Failure

Customer-facing responses should reflect the verified execution state.

For example, if the balance service is unavailable:

The balance could not be retrieved right now.

is appropriate.

Noema should not respond:

Your balance is ₦500,000.

using stale or fabricated information simply because the requested Action failed.

⸻

38. Failure Communication

Failure communication should distinguish among:

known failure
temporary unavailability
unknown outcome
authorization denial
missing information

These have different implications for the Customer.

For example:

Account not found

is materially different from:

The account service is temporarily unavailable.

⸻

39. Failure and Model Explanation

The model may convert structured Failure information into a natural-language explanation.

However:

Failure Classification
        ↓
Execution System
        ↓
Model Explanation

not:

Model
   ↓
invent Failure Classification

The model can explain the failure.

It should not manufacture one.

⸻

40. Failure and Human Intervention

Human intervention may be required when:

execution remains UNKNOWN
enterprise systems conflict
recovery is unsafe
Policy requires review
repeated retries fail

Conceptually:

Failure / Unknown
       ↓
Policy
       ↓
Human Intervention
       ↓
Resume / Recover / Reject

⸻

41. Failure and Compensation

For the Customer Account Inquiry workflow, most Actions are read operations and therefore generally require no compensation.

For state-changing Actions such as:

create_complaint

compensation is generally not equivalent to simply retrying.

If a complaint was successfully created but Noema failed to record the result, reconciliation should occur before any further state-changing Action.

⸻

42. Failure and Idempotency

Idempotency is particularly important for failures occurring after an enterprise request may have been accepted.

Example:

create_complaint
      ↓
request sent
      ↓
timeout

Before retrying:

check idempotency

or:

reconcile enterprise state

where supported.

This prevents duplicate Cases.

⸻

43. Failure and Postconditions

A Postcondition Failure occurs when execution completed but the expected state cannot be established.

Example:

create_complaint
      ↓
Enterprise Response
      ↓
Expected Case unavailable
      ↓
Postcondition failed

Noema must not mark the Action as successfully completed merely because the transport request succeeded.

⸻

44. Failure and Canonical Data

When failure relates to enterprise Business State, the authoritative enterprise system should determine the state.

For example:

Noema:
UNKNOWN
Support System:
case_id = 123
status = OPEN

Noema may reconcile the execution to:

SUCCEEDED

based on the canonical enterprise state.

⸻

45. Failure and Data Boundaries

Failure records must not become a mechanism for copying sensitive enterprise data into Noema.

Error responses should be minimized and classified.

For example:

enterprise_error_code

may be sufficient instead of retaining an entire response containing unrelated customer information.

⸻

46. Failure and Environment

Failures must preserve the environment in which they occurred.

environment = production

must remain distinct from:

environment = staging

A staging failure must never affect the state of a production execution.

⸻

47. Failure and Tenant Scope

Failure records must preserve tenant scope.

tenant = A
execution = EXE-123

must not be confused with:

tenant = B
execution = EXE-123

Execution identifiers should therefore be interpreted within their appropriate authority boundary.

⸻

48. Failure State Model

Conceptually:

EXECUTING
    │
    ├── known failure ──────→ FAILED
    │
    ├── uncertain result ───→ UNKNOWN
    │
    └── success ────────────→ SUCCEEDED

A known Failure may then enter:

FAILED
   ↓
Policy
   ├── RETRY
   ├── RECOVER
   ├── ESCALATE
   └── REJECT

⸻

49. Failure Lifecycle

Action
   ↓
Execution Attempt
   ↓
Failure Detected
   ↓
Failure Classified
   ↓
Evidence Recorded
   ↓
Policy Evaluated
   ↓
Recovery Decision
   ├── Retry
   ├── Reconcile
   ├── Clarify
   ├── Escalate
   └── Reject

The lifecycle must remain deterministic.

⸻

50. Failure Model

Conceptually:

Failure {
    execution_id
    action_id
    action_version
    category
    code
    attempt
    source
    dependency
    occurred_at
    retryable
    recoverable
    message_reference
    evidence_reference
    resulting_state
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

51. Failure Relationships

Failure
   │
   ├── belongs_to → Execution
   ├── caused_by → Dependency
   ├── supported_by → Evidence
   ├── classified_by → Policy
   ├── may_trigger → Retry
   ├── may_trigger → Reconciliation
   ├── may_trigger → Human Intervention
   └── results_in → Execution State

⸻

52. Failure Invariants

Invariant 1

Failure must represent a known unsuccessful execution condition.

Invariant 2

Failure must remain distinct from Unknown execution state.

Invariant 3

Failure must remain distinct from Trust failure.

Invariant 4

Failure must remain distinct from Clarification.

Invariant 5

A missing Context requirement must not be satisfied through guessing.

Invariant 6

Validation failures must prevent invalid Actions from being executed.

Invariant 7

Authorization failures must not be bypassed through retries or alternative Resources.

Invariant 8

A Resource failure must not cause Noema to substitute another Resource without explicit resolution.

Invariant 9

Transport success does not necessarily establish Business Success.

Invariant 10

Verification failure must prevent an Action from being represented as successfully completed.

Invariant 11

Timeouts must not automatically be interpreted as business failure.

Invariant 12

Retryability must be determined by Action semantics and Policy.

Invariant 13

Retryable does not necessarily mean safe to repeat.

Invariant 14

State-changing Actions must consider idempotency and reconciliation before retry.

Invariant 15

Failure must preserve sufficient Evidence to establish what occurred.

Invariant 16

Failure records must preserve relevant execution, tenant, organizational, and environment scope.

Invariant 17

Failure information must respect enterprise Data Boundaries.

Invariant 18

Downstream Actions blocked by an upstream failure must remain distinguishable from Actions that actually failed.

Invariant 19

Failure cascades must preserve causal relationships.

Invariant 20

Compound execution must preserve individual Action failures independently.

Invariant 21

Customer-facing responses must reflect verified execution state.

Invariant 22

The model may explain Failure but must not independently define Failure classification.

Invariant 23

Recovery must follow explicit Policy rather than probabilistic model judgment.

Invariant 24

Unknown outcomes must have an explicit reconciliation or intervention path where applicable.

Invariant 25

Noema must never manufacture success merely because the requested result is unavailable.

⸻

53. Final Definition

Failure is the explicit, evidence-backed representation of a known unsuccessful execution condition within Noema.

For the Customer Account Inquiry workflow:

ACTION
   │
   ▼
EXECUTION
   │
   ▼
RESULT
   │
   ├── SUCCESS
   │
   ├── FAILURE
   │      │
   │      ├── Validate
   │      ├── Classify
   │      ├── Record Evidence
   │      └── Apply Policy
   │
   ├── UNKNOWN
   │      ↓
   │   Reconcile
   │
   └── PARTIAL
          ↓
       Continue / Recover

And the architectural rule is:

Noema must never treat uncertainty as failure, and must never treat failure as permission to guess. A failure must be classified from execution evidence, governed by Policy, and resolved through an explicit recovery, reconciliation, escalation, clarification, or rejection path.