Execution

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/execution.md

⸻

1. Definition

Execution is the controlled process through which Noema invokes an approved Action against an enterprise capability and determines the resulting Outcome.

Within the Customer Account Inquiry workflow, Execution begins only after:

Intent
   ↓
Resolution
   ↓
Context
   ↓
Trust
   ↓
Policy
   ↓
Action

has established that the Action is permitted to proceed.

Execution is therefore not model reasoning.

It is the transition from:

what the Customer wants

to:

what the enterprise system actually did

⸻

2. Purpose

The purpose of Execution is to provide a deterministic, observable, bounded, and auditable mechanism for carrying out Actions.

Execution must establish:

which Action ran
against which Resource
under which Principal
with which inputs
through which enterprise capability
with what result
and with what final Outcome

⸻

3. Core Principle

Noema must distinguish between:

intended execution

and:

actual execution

For example:

Model / Plan:
retrieve_statement

does not mean:

Statement Retrieved

The latter can only be established from execution evidence.

Therefore:

Action Selected
      ≠
Action Executed
      ≠
Action Succeeded

⸻

4. Execution Boundary

The execution boundary is the point at which Noema invokes an enterprise capability.

Intent
   ↓
Context
   ↓
Trust
   ↓
Policy
   ↓
Action
   │
   │ EXECUTION BOUNDARY
   ▼
Enterprise Capability
   ↓
Enterprise System

Before the boundary, Noema determines whether and what to execute.

After the boundary, Noema determines what actually happened.

⸻

5. Execution Preconditions

Execution must not begin until required Preconditions are satisfied.

For example:

get_account_balance
Preconditions:
    principal authenticated
    account resolved
    account within authorized scope
    Action permitted

Conceptually:

Action
  ↓
Preconditions
  ↓
Satisfied?
 ├── YES → Execute
 └── NO  → Block

Missing information is not equivalent to a satisfied Precondition.

⸻

6. Execution Authorization

Authorization must be established before execution.

Principal
    +
Action
    +
Resource
    +
Scope
    ↓
Authorization

For example:

Customer A
    ↓
get_account_balance
    ↓
Account A
    ↓
Authorized

Noema must not infer authorization simply because the Customer requested the Action.

⸻

7. Execution Request

Once the Action is approved, Noema constructs an execution request from the Action Contract and validated Context.

Conceptually:

ExecutionRequest {
    execution_id
    action_id
    action_version
    principal
    target
    inputs
    authorization
    idempotency_key
    correlation_id
}

The request should contain only the information required by the enterprise capability.

⸻

8. Execution Identity

Every execution should have a stable execution identifier.

Example:

execution_id = EXE-12345

This identifier allows Noema to correlate:

Action
Enterprise Request
Enterprise Response
Events
Retries
Evidence
Outcome
Audit Record

The execution identifier belongs to Noema’s execution domain.

⸻

9. Correlation

Noema should preserve correlation across system boundaries.

Noema
   ↓
execution_id
   ↓
Integration
   ↓
Enterprise API
   ↓
Enterprise System

Where supported, enterprise request identifiers should also be preserved.

This allows Noema to reconstruct what occurred across the execution boundary.

⸻

10. Action Invocation

The Action is invoked through an Integration.

Action
   ↓
Integration
   ↓
Enterprise API
   ↓
Enterprise System

The Integration translates the semantic Action into the enterprise-specific protocol.

For example:

get_account_balance
        ↓
GET /accounts/{id}/balance

The API implementation is not the Action itself.

⸻

11. Execution Does Not Depend on Model Continuation

Once execution begins, the LLM should not be responsible for maintaining execution correctness.

The execution system should control:

request construction
validation
timeouts
retries
idempotency
response handling
verification
state transitions
audit records

The model may interpret results where appropriate, but it should not redefine execution state.

⸻

12. Execution State

An Action execution has an explicit lifecycle.

Conceptually:

PLANNED
   ↓
READY
   ↓
EXECUTING
   ↓
SUCCEEDED

or:

EXECUTING
   ↓
FAILED

or:

EXECUTING
   ↓
UNKNOWN

Additional states may exist where required.

The state machine must be explicit.

⸻

13. Execution State vs Business State

These states must remain separate.

Noema:

execution.status = SUCCEEDED

does not necessarily mean:

enterprise.business_state = expected_state

For example:

create_complaint
    ↓
Noema received response
    ↓
execution.status = SUCCEEDED

The Support System remains authoritative for the actual Case state.

⸻

14. Read Execution

Most Actions in this reference workflow are read operations.

Example:

get_account_balance

Execution:

Action
   ↓
Ledger API
   ↓
Balance
   ↓
Evidence
   ↓
Outcome

The Action observes enterprise state without mutating it.

⸻

15. Statement Retrieval Execution

For:

retrieve_statement

the execution flow is:

Intent
   ↓
Statement Request
   ↓
Account + Period Resolution
   ↓
Trust
   ↓
Authorization
   ↓
retrieve_statement
   ↓
Statement System
   ↓
Statement Result
   ↓
Verification
   ↓
Outcome

The retrieved statement remains an enterprise resource.

⸻

16. Transaction Search Execution

For:

search_transactions

the execution request may contain:

account_id
date_range
merchant
amount
status
transaction_type

The enterprise Transaction System performs the search.

Noema records the execution and resulting evidence.

⸻

17. Spending Summary Execution

For:

get_spending_summary

execution may involve:

transaction data
       ↓
aggregation capability
       ↓
spending summary

The resulting summary must retain its semantic classification.

If it is calculated from underlying transactions:

summary = derived

It must not silently become canonical Business State.

⸻

18. Complaint Creation Execution

create_complaint is the primary state-changing Action in this reference workflow.

Execution:

Customer Intent
      ↓
Complaint Context
      ↓
Trust
      ↓
Authorization
      ↓
create_complaint
      ↓
Support System
      ↓
Case Created
      ↓
Verification
      ↓
Outcome

Noema records that it requested the creation.

The Support System remains authoritative for the Case.

⸻

19. Execution Inputs

Execution inputs must come from validated Action inputs.

For example:

search_transactions {
    account_id
    date_from
    date_to
}

Inputs should not be reconstructed from model memory after validation.

Once the Action is approved, the execution layer should use the validated representation.

⸻

20. Input Validation

Before invocation, inputs must satisfy the Action Contract.

For example:

date_from <= date_to
account_id is valid
required fields exist
types are correct
scope is valid

Invalid inputs must prevent execution.

Invalid Input
     ↓
Execution Blocked

⸻

21. Resource Validation

The target Resource must remain within the authorized scope.

For example:

principal = Customer A
account = Account A

is valid only if the Customer is authorized for that Account.

Resource resolution and resource authorization must therefore remain connected throughout execution.

⸻

22. Execution and Canonical Data

When an Action requires authoritative enterprise state, Execution should use the appropriate System of Record.

Example:

get_account_balance
        ↓
Ledger
        ↓
Canonical Balance

Noema should not silently substitute:

model estimate
stale projection
untrusted cache

when the Action’s Policy requires current canonical state.

⸻

23. Execution and Evidence

Execution produces Evidence.

For example:

Ledger Response
      ↓
Execution Evidence

Evidence should preserve:

source
execution_id
observed_at
resource
result
response metadata
version

where available.

⸻

24. Execution and Postconditions

After execution, required Postconditions must be evaluated.

Example:

create_complaint
      ↓
Support System
      ↓
case_id
      ↓
Postcondition:
case exists

The Postcondition determines whether the intended execution result has been established.

⸻

25. Execution Verification

Execution success should be based on evidence.

Possible verification levels include:

response received
resource returned
authoritative state verified
enterprise event observed

The required verification level depends on the Action and Policy.

⸻

26. Execution Success

An Action may be marked:

SUCCEEDED

when its contractually required execution and verification conditions have been satisfied.

A successful HTTP response alone does not universally establish successful business execution.

For example:

HTTP 200

may still contain:

business_status = rejected

Execution must therefore evaluate the semantic result.

⸻

27. Execution Failure

Execution may fail because of:

invalid input
authorization rejection
enterprise rejection
network failure
timeout
service unavailable
dependency failure
verification failure

Failure should be classified according to the Action Contract.

Failure
   ↓
Failure Policy
   ├── Retry
   ├── Escalate
   ├── Clarify
   ├── Recover
   └── Reject

⸻

28. Unknown Execution State

Noema must distinguish:

FAILED

from:

UNKNOWN

Example:

Noema
   ↓
create_complaint
   ↓
Support System
   ↓
request accepted
   ↓
network connection lost

Noema cannot safely conclude:

FAILED

because the Case may have been created.

The correct state may be:

UNKNOWN

followed by reconciliation or verification.

⸻

29. Execution Timeout

A timeout means Noema did not receive a result within the defined execution window.

It does not necessarily mean the enterprise Action did not execute.

Therefore:

Timeout
   ↓
UNKNOWN

may be more correct than:

Timeout
   ↓
FAILED

depending on Action semantics.

⸻

30. Execution Retry

Retries are governed by the Action Contract.

For example:

temporary network failure
        ↓
retry

while:

authorization denied
        ↓
do not retry

Retry decisions must be deterministic and Policy-driven.

⸻

31. Execution Idempotency

Idempotency protects against duplicate execution.

For:

create_complaint

a retry could create duplicate cases.

Therefore:

execution_id
      +
idempotency_key

should identify the logical operation where the enterprise capability supports idempotency.

Noema must not assume that network retries are harmless.

⸻

32. Execution Attempt

A single logical Action execution may have multiple attempts.

Execution
   ├── Attempt 1
   ├── Attempt 2
   └── Attempt 3

The logical execution remains the same.

Each attempt should be separately observable.

Conceptually:

execution_id
attempt_number
started_at
ended_at
result
failure

⸻

33. Execution Ordering

For compound Intents, Actions may have dependencies.

Example:

resolve_account
      ↓
search_transactions
      ↓
get_spending_summary

An Action must not execute before its required dependencies are satisfied.

Execution ordering should therefore be determined by the validated Plan.

⸻

34. Parallel Execution

Independent read Actions may be executed in parallel where Policy permits.

For example:

                ┌── get_account_balance
Intent ─────────┼── retrieve_statement
                └── search_transactions

Parallelism must not violate:

authorization
data boundaries
dependency ordering
rate limits
enterprise constraints

⸻

35. Execution Cancellation

An execution may be cancelled before completion when Policy permits.

Possible causes:

user cancellation
timeout policy
human intervention
upstream dependency failure
policy change

Cancellation semantics must distinguish:

not started
cancelled before invocation
invocation already sent
enterprise execution unknown

This distinction matters for state-changing Actions.

⸻

36. Execution Recovery

Recovery may be required when an Action ends in an uncertain state.

Example:

create_complaint
      ↓
UNKNOWN
      ↓
query Support System
      ↓
case found
      ↓
SUCCEEDED

or:

case not found
      ↓
Policy determines whether retry is safe

Recovery must not blindly repeat an Action whose prior execution may have succeeded.

⸻

37. Reconciliation

Reconciliation compares Noema’s Execution State with authoritative enterprise state.

Example:

Noema:
execution = UNKNOWN
Support System:
case_id = 84721
status = OPEN

Reconciliation establishes:

execution = SUCCEEDED

where the Action Contract permits that conclusion.

⸻

38. Execution and Human Intervention

Human intervention may be required when:

execution is UNKNOWN
enterprise systems conflict
authorization is unclear
Policy requires review
recovery is unsafe

Conceptually:

Execution
    ↓
Uncertainty
    ↓
Human Intervention
    ↓
Decision
    ↓
Resume / Recover / Reject

Human intervention is part of the execution lifecycle, not an informal exception.

⸻

39. Execution and Data Boundaries

The execution layer must enforce the Action’s data boundary.

Only required inputs should cross into an enterprise integration.

For example:

search_transactions
        ↓
account_id
date_range
filters

not the entire Context object.

This prevents accidental data propagation across system boundaries.

⸻

40. Execution and Temporal State

Execution should preserve the relevant temporal context.

For example:

"last month"

should already be resolved into:

date_from
date_to
timezone

before execution.

The enterprise integration should not independently reinterpret natural-language time expressions.

⸻

41. Execution and Environment

Execution must explicitly identify the target environment.

Example:

environment = production

must not accidentally resolve to:

environment = staging

Environment is part of the execution boundary.

⸻

42. Execution and Tenancy

Execution must preserve tenant scope.

execution
    ↓
tenant = A
    ↓
account = 123

must never silently become:

tenant = B
account = 123

even if the resource identifier is identical.

⸻

43. Execution and Organizational Boundaries

Where applicable, execution must preserve organizational scope.

For example:

tenant
    ↓
organization
    ↓
account

The enterprise authorization model determines whether the Principal may access the resource.

Noema must not collapse these boundaries.

⸻

44. Execution Audit Record

A consequential execution should produce an audit record containing sufficient information to reconstruct the execution.

Conceptually:

ExecutionRecord {
    execution_id
    action_id
    action_version
    principal
    target
    input_reference
    started_at
    completed_at
    attempts
    result
    outcome
    evidence_reference
    policy_reference
    trust_reference
    failure
}

The exact persistence model is implementation-specific.

⸻

45. Execution Provenance

Execution provenance should establish:

who initiated execution
what Action was executed
what version was used
what Resource was targeted
what inputs were supplied
what enterprise system was invoked
what response was received
what verification occurred

This supports auditability and debugging.

⸻

46. Execution Observability

Execution should expose operational signals such as:

latency
attempt count
failure rate
timeout rate
unknown outcomes
verification failures
enterprise dependency health

Observability should not alter the semantic execution state.

It provides visibility into it.

⸻

47. Execution and Customer Response

The Customer-facing response should be based on the verified Outcome.

For example:

Action
   ↓
Enterprise Result
   ↓
Verification
   ↓
Outcome
   ↓
Customer Response

Noema should not tell the Customer:

"Your complaint has been created."

until the execution state provides sufficient evidence for that claim.

⸻

48. Execution and Model Interpretation

The model may assist in converting an execution result into a natural-language response.

For example:

BalanceResult
      ↓
LLM
      ↓
Customer-facing explanation

But the model must not change:

execution.status
outcome
enterprise state
verification result

The model explains execution results; it does not define them.

⸻

49. Execution and Compound Intent

For compound Intent:

"Show me my balance and last month's spending."

Noema may execute:

get_account_balance
        +
get_spending_summary

Each Action should have its own:

execution state
inputs
evidence
outcome
verification

The overall Intent Outcome should be derived from the individual execution results.

⸻

50. Partial Execution

Compound execution may produce partial success.

Example:

get_account_balance
    → SUCCEEDED
get_spending_summary
    → FAILED

The overall execution must not be represented as fully successful.

Instead:

Partial Success

should remain explicit.

The response can then accurately communicate which portion succeeded.

⸻

51. Execution State Machine

The reference lifecycle can be represented as:

                ┌───────────────┐
                │    PLANNED    │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │     READY     │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   EXECUTING   │
                └───┬─────┬─────┘
                    │     │
             success│     │failure
                    │     │
                    ▼     ▼
              ┌────────┐ ┌────────┐
              │SUCCESS │ │ FAILED │
              └────────┘ └────────┘
                    │
                    │
             uncertain result
                    │
                    ▼
              ┌─────────┐
              │ UNKNOWN │
              └────┬────┘
                   │
                   ▼
             RECONCILIATION

Additional states may be introduced where required by the broader Execution Model.

⸻

52. Reference Execution Flows

Balance Inquiry

Customer
   ↓
Intent
   ↓
Resolve Account
   ↓
Trust
   ↓
Authorization
   ↓
get_account_balance
   ↓
Ledger
   ↓
Balance
   ↓
Verify
   ↓
Respond

Statement Retrieval

Customer
   ↓
Intent
   ↓
Resolve Account + Period
   ↓
Trust
   ↓
Authorization
   ↓
retrieve_statement
   ↓
Statement System
   ↓
Statement
   ↓
Verify
   ↓
Respond

Transaction Search

Customer
   ↓
Intent
   ↓
Resolve Account + Filters
   ↓
Trust
   ↓
Authorization
   ↓
search_transactions
   ↓
Transaction System
   ↓
Transactions
   ↓
Verify
   ↓
Respond

Spending Summary

Customer
   ↓
Intent
   ↓
Resolve Account + Period
   ↓
Trust
   ↓
Authorization
   ↓
get_spending_summary
   ↓
Transaction / Analytics Capability
   ↓
Summary
   ↓
Verify / Classify
   ↓
Respond

Complaint

Customer
   ↓
Intent
   ↓
Resolve Customer + Related Resource
   ↓
Trust
   ↓
Authorization
   ↓
create_complaint
   ↓
Support System
   ↓
Case
   ↓
Verify
   ↓
Respond

⸻

53. Execution Invariants

Invariant 1

An Action must not execute before required Preconditions are satisfied.

Invariant 2

Authorization must be established before execution.

Invariant 3

Execution must operate on validated Action inputs.

Invariant 4

Execution must target an explicitly resolved Resource and scope.

Invariant 5

Action selection, Action invocation, and Action success are distinct states.

Invariant 6

Noema must distinguish Execution State from enterprise Business State.

Invariant 7

Execution success must be based on sufficient execution evidence.

Invariant 8

A timeout must not automatically be interpreted as business failure.

Invariant 9

Unknown execution state must remain distinct from failure.

Invariant 10

Retries must follow explicit Action and Policy semantics.

Invariant 11

State-changing Actions must have explicit idempotency semantics.

Invariant 12

A retry must not blindly duplicate an Action whose prior execution may have succeeded.

Invariant 13

Postconditions must be evaluated according to the Action Contract.

Invariant 14

Consequential execution must retain sufficient provenance for audit and reconstruction.

Invariant 15

Only the minimum required Context should cross an Integration boundary.

Invariant 16

Execution must preserve tenant, organizational, resource, and environment boundaries.

Invariant 17

The model must not redefine execution state after the execution boundary.

Invariant 18

Model interpretation of an execution result must not alter the underlying Outcome.

Invariant 19

Enterprise Systems remain authoritative for Business State.

Invariant 20

Noema remains authoritative for its own Execution State.

Invariant 21

Unknown execution outcomes must have an explicit recovery or reconciliation path where applicable.

Invariant 22

Human intervention must be represented as an explicit execution state or transition rather than an informal exception.

Invariant 23

Compound executions must preserve the independent state and Outcome of each Action.

Invariant 24

Partial execution success must remain distinguishable from complete success.

Invariant 25

Customer-facing responses must reflect verified execution Outcomes rather than model expectations.

⸻

54. Final Definition

Execution is the controlled, deterministic process by which Noema invokes an approved Action against an enterprise capability, observes the resulting behavior, verifies the required Outcome, and records the execution journey.

The fundamental relationship is:

INTENT
   │
   ▼
CONTEXT
   │
   ▼
TRUST + POLICY
   │
   ▼
ACTION
   │
   ▼
PRECONDITIONS
   │
   ▼
AUTHORIZATION
   │
   ▼
EXECUTION
   │
   ▼
ENTERPRISE SYSTEM
   │
   ▼
EVIDENCE
   │
   ▼
POSTCONDITIONS
   │
   ▼
OUTCOME
   │
   ├── SUCCEEDED
   ├── FAILED
   ├── UNKNOWN
   └── PARTIAL

And the architectural rule is:

Noema must never confuse an intended Action with an executed Action, or an executed Action with a successful Outcome. Execution is established by what the enterprise system actually did and what Noema can verify—not by what the model expected to happen.