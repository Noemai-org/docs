> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Failure

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/failure.md

⸻

1. Definition

Failure is the explicit, evidence-backed representation of a known unsuccessful execution condition.

Within the Customer Account Inquiry workflow, Failure answers:

What prevented the requested Action from completing successfully?

Failure is an execution-domain state and diagnostic classification. It is not an assumption that something went wrong merely because Noema did not immediately receive a response.

The fundamental distinction is:

Action
   ↓
Execution Attempt
   ↓
Result
   │
   ├── SUCCEEDED
   ├── FAILED
   ├── UNKNOWN
   └── PARTIAL

Failure must therefore be grounded in execution evidence.

Noema must never infer failure merely from:

* lack of response
* model uncertainty
* stale Context
* ambiguous Intent
* an unexpected but unresolved enterprise state
* a timeout whose business consequence is unknown

⸻

2. Purpose

The purpose of Failure handling is to ensure that Noema:

* detects failure
* distinguishes failure from uncertainty
* classifies the failure
* preserves the evidence establishing it
* determines whether recovery is possible
* determines whether retry is safe
* applies the governing Policy
* preserves causal relationships
* prevents unsafe duplicate execution
* communicates the verified state accurately

Failure must always lead to a defined next state.

The model must never simply decide what “probably happened.”

⸻

3. Core Principle

Failure must remain distinct from uncertainty.

For example:

Enterprise API
     ↓
HTTP 400
     ↓
Known rejection
     ↓
FAILED

is materially different from:

Enterprise API
     ↓
Request may have been accepted
     ↓
Connection lost
     ↓
Outcome cannot be established
     ↓
UNKNOWN

Therefore:

No response ≠ Failure
Failure ≠ Unknown
Timeout ≠ automatically Failed
Retryable ≠ automatically Safe to Retry

The objective is not to eliminate uncertainty.

The objective is to represent uncertainty honestly and resolve it safely.

⸻

4. Failure Boundary

Failure belongs to the Execution domain.

The conceptual boundary is:

Intent
   ↓
Context
   ↓
Trust
   ↓
Policy
   ↓
Action
   ↓
Execution
   ↓
Result

Before execution:

model uncertainty
intent ambiguity
missing Context
insufficient Trust
authorization uncertainty

belong to the decision path.

After an Action is admitted to execution:

validation failure
authorization rejection
enterprise rejection
transport failure
timeout
dependency failure
verification failure

belong to execution and recovery semantics.

This distinction prevents Noema from treating an unresolved Intent as though an enterprise Action had failed.

⸻

5. Failure Categories

The reference workflow recognizes the following failure and blocking conditions:

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

Additional domain-specific classifications may be introduced where required.

The classification must be machine-readable and stable.

⸻

6. Validation Failure

A Validation Failure occurs when the Action request does not satisfy its Action Contract.

Example:

search_transactions
date_from > date_to
        ↓
VALIDATION_FAILED

The enterprise capability must not be invoked.

Invalid Action Input
       ↓
Validation Gate
       ↓
Execution Blocked

Examples include:

* required parameter missing
* invalid type
* malformed identifier
* invalid date interval
* invalid enum value
* parameter outside permitted range
* resource scope inconsistent with the Action Contract

Validation failure occurs before the execution boundary.

⸻

7. Missing Context

An Action may fail to become executable because required Context is unavailable.

Example:

Intent:
"Show me my balance."
Available:
customer_id
Required:
account_id
        ↓
Missing Context

Noema must not invent the missing account.

The appropriate transition may be:

Missing Context
      ↓
Clarification

or:

Missing Context
      ↓
Blocked

depending on the Action, Policy, and broader state model.

Missing Context is not automatically an enterprise execution failure.

⸻

8. Authorization Failure

Authorization Failure occurs when the Principal is not permitted to perform the Action against the resolved Resource and scope.

Example:

Principal A
     ↓
Account B
     ↓
Authorization Denied
     ↓
AUTHORIZATION_FAILED

Noema must not bypass the denial by:

* selecting another Resource
* changing the Principal
* weakening the scope
* retrying indefinitely
* asking the model to reinterpret authorization

Authorization decisions belong to the authorization and Policy layers.

A denied Action must not be executed merely because the Customer requested it.

⸻

9. Resource Failure

A requested Resource may not exist or may no longer be accessible.

Example:

account_id = 123
       ↓
Account Not Found
       ↓
RESOURCE_NOT_FOUND

Noema must not substitute another Resource because it appears similar.

If multiple candidate Resources exist:

Multiple Candidates
       ↓
AMBIGUOUS
       ↓
CLARIFY

Resource resolution and authorization must remain bound to the same execution scope.

⸻

10. Enterprise Rejection

An enterprise system may receive a structurally valid Action and reject it according to its own Business Rules.

Example:

Noema
   ↓
retrieve_statement
   ↓
Statement System
   ↓
Request Rejected

The enterprise system is authoritative for the returned Business-State rejection.

Noema should preserve the relevant enterprise error classification and reason where permitted by Data Boundaries.

This is different from a transport failure.

The enterprise system responded and established that the requested operation was not accepted.

⸻

11. Network Failure

A Network Failure occurs when Noema cannot successfully communicate with the enterprise capability.

Examples:

* connection refused
* connection reset
* DNS failure
* transport error
* connection interruption

A network failure does not necessarily establish that the enterprise Action did not execute.

Therefore:

NETWORK_FAILURE
       ↓
What is known about request acceptance?
       │
       ├── definitely not sent → FAILED / NOT_EXECUTED
       │
       └── may have been accepted → UNKNOWN

The resulting execution state depends on the point at which communication failed.

⸻

12. Timeout

A timeout occurs when Noema does not receive a result within the configured execution window.

A timeout is an observation about communication.

It is not automatically an observation about Business State.

For example:

create_complaint
      ↓
request sent
      ↓
timeout

Noema cannot conclude:

complaint was not created

unless additional evidence establishes that fact.

The appropriate state may be:

EXECUTION_OUTCOME_UNKNOWN

followed by a fresh verification read.

The POC specifically treats EXECUTION_OUTCOME_UNKNOWN as a load-bearing execution state rather than a disguised failure. NOEMA POC Specification_1.pdf

⸻

13. Unknown Execution Outcome

Unknown is not a Failure classification.

It is an execution state indicating:

Noema cannot currently establish whether the Action succeeded or failed.

Example:

create_complaint
      ↓
request sent
      ↓
connection lost
      ↓
UNKNOWN

The correct next step is not:

UNKNOWN
   ↓
blind retry

It is:

UNKNOWN
   ↓
fresh verification read
   ↓
authoritative state
   ├── found → SUCCEEDED
   ├── definitively absent → recovery decision
   └── still unresolved → ESCALATE / remain UNKNOWN

The POC explicitly requires that a timeout never silently become “failed” or “retry it”; an EXECUTION_OUTCOME_UNKNOWN state must be resolved through fresh state verification before another execution attempt. NOEMA POC Specification PDF.pdf

⸻

14. Dependency Failure

An Action may depend on one or more enterprise capabilities.

Example:

get_spending_summary
       ↓
Transaction System
       ↓
Aggregation Capability
       ↓
Unavailable

Result:

DEPENDENCY_FAILURE

The failure record must identify the dependency that prevented successful completion.

This allows Policy to determine whether to:

* retry
* wait
* recover
* escalate
* inform the Customer

A downstream Action blocked by a dependency failure must not be incorrectly recorded as though it independently executed and failed.

⸻

15. Verification Failure

Execution may appear successful while the required Postcondition cannot be established.

Example:

create_complaint
      ↓
HTTP 200
      ↓
expected case_id absent
      ↓
VERIFICATION_FAILED

The transport response alone is insufficient.

The Action must not be represented to the Customer as successfully completed unless the required verification condition is satisfied.

Verification is therefore part of execution semantics, not merely an observability feature.

The POC explicitly treats Verification as a core component because an HTTP response is not equivalent to a verified business outcome. NOEMA POC Specification_1.pdf

⸻

16. Semantic Failure

Transport-level success does not guarantee Business Success.

Example:

HTTP 200
{
    "status": "REJECTED"
}

The enterprise capability responded successfully at the transport layer.

The requested Business Action did not.

Therefore:

Transport Success
       ≠
Business Success

Noema must classify the semantic result according to the Action Contract and enterprise response semantics.

⸻

17. Policy Block

Execution may be blocked by Noema Policy even when:

* the enterprise capability is available
* the request is syntactically valid
* the Principal is authenticated
* the Resource exists

Example:

Action
   ↓
Policy Evaluation
   ↓
Not Permitted
   ↓
POLICY_BLOCKED

No enterprise invocation occurs when Policy blocks the Action before the execution boundary.

Policy failure must not be represented as an enterprise failure.

The POC requires deterministic, versioned Policy evaluation and records the Policy version governing the Trust Decision. NOEMA POC Specification MD.md

⸻

18. Failure vs Trust Failure

Trust Failure occurs while determining whether the proposed Action should be permitted.

Execution Failure occurs when an Action has entered execution or an execution attempt has been made and a known unsuccessful condition is established.

Example:

Ambiguous account
      ↓
Trust insufficient
      ↓
CLARIFY

This is not Execution Failure.

By contrast:

Account resolved
      ↓
Trust = ALLOW
      ↓
Action executed
      ↓
Enterprise rejects request
      ↓
FAILED

These states must remain semantically distinct.

⸻

19. Failure vs Clarification

Clarification is appropriate when additional information from the Principal is required to resolve material ambiguity.

Example:

"Show me my account."
Account A
Account B
        ↓
AMBIGUOUS
        ↓
CLARIFY

No enterprise execution failure occurred.

The system simply lacks sufficient information to safely determine the intended Resource.

Noema must never convert ambiguity into a guessed Resource merely to avoid a clarification.

⸻

20. Failure vs Escalation

Escalation is a Policy-driven response to a condition.

It is not itself a Failure category.

Example:

Enterprise systems disagree
        ↓
Authority cannot safely be established
        ↓
ESCALATE

Similarly:

Repeated recovery failure
        ↓
Policy threshold reached
        ↓
ESCALATE

The underlying condition may be:

* failure
* contradiction
* unknown state
* authorization issue
* insufficient evidence

while the resulting workflow action is:

ESCALATE

⸻

21. Failure Classification

A Failure should contain sufficient structured information to establish what happened.

Conceptually:

Failure {
    execution_id
    action_id
    action_version
    execution_attempt_id
    category
    code
    source
    dependency
    occurred_at
    retryable
    recoverable
    safe_to_retry
    message_reference
    evidence_reference
    resulting_state
}

The exact persistence schema is implementation-specific.

The semantic distinction between:

retryable
recoverable
safe_to_retry

should remain explicit.

These are not interchangeable properties.

⸻

22. Failure Codes

Failure codes should be stable and machine-readable.

Reference codes include:

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

Execution outcome states include:

SUCCEEDED
FAILED
UNKNOWN
PARTIAL

The implementation may extend the vocabulary, but equivalent concepts must not be represented inconsistently across Actions.

⸻

23. Retryability

A Failure may have explicit retry semantics.

For example:

temporary service unavailable
        ↓
potentially retryable

while:

authorization denied
        ↓
normally not retryable

Retryability must be defined by the Action Contract and Policy.

The model must not determine retryability through intuition.

Each registered capability should have explicit:

* retry semantics
* recovery semantics
* verification strategy
* risk classification

The POC’s Capability Registry explicitly requires these properties for each capability. NOEMA POC Specification MD.md

⸻

24. Retry Safety

A Failure can be retryable without being safe to repeat blindly.

Example:

create_complaint
      ↓
request sent
      ↓
timeout

The enterprise system may already have created the Case.

Therefore:

retryable
    ≠
safe to repeat

Before retrying a potentially state-changing Action, Noema must consider:

* whether the request may already have been accepted
* idempotency support
* current enterprise state
* verification
* reconciliation
* retry budget
* Action risk
* Policy

⸻

25. Verification-Before-Retry

For an uncertain state, retry must be gated by a fresh verification read.

Conceptually:

UNKNOWN
   ↓
Fresh Verification Read
   ↓
Current Enterprise State
   │
   ├── Action succeeded → SUCCEEDED
   │
   ├── Action did not occur → retry if permitted
   │
   └── state unresolved → ESCALATE / remain UNKNOWN

The POC’s execution-safety mechanism explicitly requires a client-generated idempotency key to exist before the call, distinct execution-attempt IDs, bounded retry budgets, and fresh verification before another attempt. NOEMA POC Specification PDF.pdf

This is a core safety rule.

⸻

26. Idempotency and Duplicate Prevention

State-changing Actions require explicit idempotency semantics.

For example:

Logical Action
      ↓
idempotency_key
      ↓
execution_attempt_1

If the attempt times out:

execution_attempt_1
      ↓
UNKNOWN
      ↓
verification
      ↓
retry only if safe

A second attempt must not silently create a second logical operation.

The idempotency key should be generated and persisted before the enterprise call where the capability supports it.

Duplicate user submissions and duplicate enterprise callbacks should be deduplicated against the appropriate idempotency identity.

⸻

27. Execution Attempt vs Logical Execution

A logical Action execution may contain multiple attempts.

execution_id
   │
   ├── execution_attempt_id = A1
   ├── execution_attempt_id = A2
   └── execution_attempt_id = A3

The logical execution remains the same.

Each attempt should retain:

execution_attempt_id
attempt_number
started_at
ended_at
request_reference
result
failure

This distinction is required for:

* retry analysis
* duplicate prevention
* audit
* reconciliation
* operational debugging

An execution_attempt_id must not be confused with the broader intent_id. The POC explicitly requires unique execution-attempt identity. NOEMA POC Specification PDF.pdf

⸻

28. Recovery

Recovery follows a deterministic path.

Failure / Unknown
       ↓
Classify
       ↓
Policy
       ├── Retry
       ├── Verify
       ├── Reconcile
       ├── Wait
       ├── Clarify
       ├── Escalate
       └── Reject

The model may explain the recovery state.

It must not independently select an unsafe recovery path.

The recovery mechanism must be encoded in the Action/Capability semantics and Policy.

⸻

29. Recovery After Read Failure

For a read Action:

get_account_balance
      ↓
TIMEOUT

Noema may retry if:

* the failure is transient
* the Action is retryable
* Policy permits the retry
* the retry does not violate execution constraints

If the authoritative source remains unavailable:

retry exhausted
      ↓
INFORM / ESCALATE

Noema must not fabricate or silently substitute an unsupported balance.

⸻

30. Recovery After Statement Failure

For:

retrieve_statement

a temporary infrastructure failure may be retryable.

Example:

Service Unavailable
      ↓
Retry

while:

Statement Not Available
      ↓
No Retry
      ↓
Inform Customer / Escalate

The distinction must come from the enterprise result and governing Policy.

⸻

31. Recovery After Transaction Search Failure

For:

search_transactions

transient infrastructure failures may be retryable.

But a definitive input error should not be retried indefinitely.

Example:

Invalid Date Range
      ↓
VALIDATION_FAILED
      ↓
Correct / Clarify

rather than:

Invalid Date Range
      ↓
Retry
      ↓
Invalid Date Range
      ↓
Retry

⸻

32. Recovery After Spending Summary Failure

A spending summary may depend upon transaction data or an aggregation capability.

Example:

get_spending_summary
       ↓
Transaction System unavailable
       ↓
DEPENDENCY_FAILURE

Noema may retry according to the dependency’s defined semantics.

It must not replace unavailable authoritative transaction information with an unsupported estimate simply to produce an answer.

If the summary is derived, the provenance of the underlying data must remain available for verification.

⸻

33. Recovery After Complaint Creation Failure

Complaint creation is a state-changing Action and therefore requires stronger recovery semantics.

Example:

create_complaint
      ↓
timeout

Before another write attempt, Noema must determine:

Was the request accepted?
       ↓
Can the Case be queried?
       ↓
Does the enterprise support idempotency?
       ↓
Can the operation be reconciled?

The safe sequence is:

TIMEOUT
   ↓
UNKNOWN
   ↓
QUERY SOURCE OF TRUTH
   ↓
Case found
   ↓
SUCCEEDED

If the Case cannot be found:

Case not found
   ↓
Determine whether retry is safe
   ↓
Retry only if Policy + Action semantics permit

The POC recovery playbook specifically requires re-querying the downstream system after a timeout following ticket submission rather than submitting a second ticket blindly. NOEMA POC Specification PDF.pdf

⸻

34. Reconciliation

Reconciliation resolves uncertain execution by comparing Noema’s execution record with authoritative enterprise state.

Example:

Noema:
execution = UNKNOWN
Support System:
case_id = 84721
status = OPEN

If the Action Contract permits that evidence to establish completion:

UNKNOWN
   ↓
RECONCILIATION
   ↓
SUCCEEDED

Reconciliation must use the appropriate System of Record.

It must not resolve conflicting systems by model preference.

⸻

35. Contradictory Enterprise State

A particularly important failure condition occurs when enterprise systems disagree.

For example:

Ledger:
transaction successful
Switch:
transaction failed

Noema must not:

* average the values
* choose the more optimistic result
* choose whichever response arrived last
* ask the model to decide
* silently collapse the contradiction

Instead:

Conflicting authoritative evidence
       ↓
CONTRADICTORY
       ↓
ESCALATE

The POC explicitly requires contradictory ledger/switch state to be classified as CONTRADICTORY and escalated rather than resolved through a default preference rule. NOEMA POC Specification_1.pdf

⸻

36. State Reconstruction and Failure

A Customer may describe a transaction as “failed” when the actual enterprise state is different.

Possible reconstructed states include:

DEBIT_CONFIRMED
CREDIT_MISSING
SETTLEMENT_PENDING
REVERSAL_PENDING
REVERSED
DUPLICATE
PARTIAL
PROVIDER_UNAVAILABLE
RECEIVING_INSTITUTION_UNAVAILABLE
STALE
CONTRADICTORY
EXECUTION_OUTCOME_UNKNOWN

Therefore:

Customer says "failed"
        ↓
Intent / Context
        ↓
State Reconstruction
        ↓
Actual enterprise state

The Customer’s description is evidence about the request, not automatically the canonical transaction state.

The POC explicitly requires state reconstruction rather than treating a user’s description of a failed transaction as the final state. NOEMA POC Specification_1.pdf

⸻

37. Stale State Is Not Automatically Failure

A stale enterprise read is not necessarily a failed Action.

Example:

Switch status
      ↓
observed_at = 10 minutes ago
      ↓
freshness SLA = 5 minutes
      ↓
STALE

The correct interpretation is:

STALE
   ↓
fresh read required

not:

STALE
   ↓
FAILED

Staleness is a property of evidence freshness.

It must remain distinct from:

* failure
* contradiction
* unknown
* successful execution

The POC requires stale state to be explicitly tagged rather than silently treated as current. NOEMA POC Specification_1.pdf

⸻

38. Failure Propagation

A failed upstream dependency may prevent downstream Actions from executing.

Example:

resolve_account
      ↓
FAILED
      ↓
search_transactions
      ↓
BLOCKED

The downstream Action was not necessarily executed.

Therefore:

BLOCKED ≠ FAILED

The execution record must preserve the distinction.

⸻

39. Failure Cascades

Noema should prevent one root failure from being represented as multiple unrelated failures.

Example:

Transaction System unavailable
        ↓
search_transactions
        ↓
FAILED
        ↓
get_spending_summary
        ↓
BLOCKED

The root cause is the dependency failure.

The audit trail should preserve:

root cause
   ↓
affected Action
   ↓
blocked dependent Action

This permits accurate operational diagnosis.

⸻

40. Partial Failure

Compound Intents may produce partial success.

Example:

get_account_balance
    → SUCCEEDED
search_transactions
    → FAILED

The overall workflow must preserve both results.

It must not collapse the entire execution into:

FAILED

without retaining the successful Action.

Conceptually:

Compound Intent
      ↓
Action A → SUCCEEDED
Action B → FAILED
      ↓
PARTIAL

The Customer-facing response should accurately represent the portions that were established and the portions that were not.

⸻

41. Failure Evidence

Every consequential Failure should retain the evidence necessary to establish what occurred.

Possible evidence includes:

HTTP status
enterprise error code
response classification
request identifier
execution_attempt_id
timestamp
dependency identifier
timeout metadata
verification result
enterprise response reference

Sensitive enterprise payloads should not automatically be retained in full.

The principle is:

minimum necessary data
+
maximum necessary traceability

The POC explicitly adopts minimum necessary data and maximum necessary traceability while keeping enterprise systems as the systems of record. NOEMA POC Specification PDF.pdf

⸻

42. Failure Provenance

Noema should be able to answer:

* What failed?
* Which Action was executing?
* Which attempt failed?
* Where did the failure occur?
* When did it occur?
* What evidence established the failure?
* Which enterprise dependency was involved?
* Which Policy governed recovery?
* Was retry attempted?
* Why was retry permitted or prohibited?

Conceptually:

Failure
   ↓
Evidence
   ↓
Source
   ↓
Timestamp
   ↓
Execution Attempt
   ↓
Policy
   ↓
Recovery Decision

“The model said so” is never sufficient provenance for a Trust or execution decision. NOEMA POC Specification PDF.pdf

⸻

43. Failure Auditability

Failure records must support reconstruction of the execution journey without relying on model memory.

Example:

execution_id = EXE-123
action = retrieve_statement
execution_attempt_id = ATT-002
source = Statement System
failure = TIMEOUT
occurred_at = ...
retryable = true
safe_to_retry = false
recovery = VERIFY

An operator should be able to reconstruct:

what happened
→
what Noema knew
→
what evidence existed
→
what Policy applied
→
what recovery occurred
→
what ultimately became true

The POC’s audit requirement is explicitly causal rather than equivalent to ordinary agent/tool logging. NOEMA POC Specification PDF.pdf

⸻

44. Failure and Operational Memory

Failure records should contribute to structured Operational Memory where appropriate.

The purpose is not to create a general-purpose AI memory system.

The useful historical record is:

what happened
what was known
why the decision was made
what was authorized
what happened after execution

The POC specifies structured records of cases, evidence, decisions, and outcomes rather than a general vector-memory system. NOEMA POC Specification PDF.pdf

⸻

45. Failure and Human Intervention

Human intervention may be required when:

* execution remains UNKNOWN
* authoritative systems contradict one another
* recovery is unsafe
* repeated retries fail
* authorization cannot be established
* Policy requires review
* required evidence cannot be obtained
* an Action’s consequences cannot be safely determined

Conceptually:

Failure / Unknown / Contradiction
          ↓
Policy
          ↓
Human Intervention
          ↓
Resume / Reconcile / Recover / Reject

Human intervention must be represented explicitly in the execution lifecycle.

It is not an informal exception outside the system.

⸻

46. Failure and Compensation

Most Actions in the Customer Account Inquiry workflow are read-oriented and therefore do not require compensation.

For state-changing Actions such as:

create_complaint

compensation must not be confused with retry.

Example:

Complaint creation
      ↓
UNKNOWN
      ↓
Reconciliation
      ↓
Case exists

The correct action is to reconcile the existing Case, not create another one.

Compensation semantics are Action-specific and should only be introduced where the enterprise capability defines them.

⸻

47. Failure and Data Boundaries

Failure handling must not become a mechanism for copying sensitive enterprise data into Noema.

For example, an enterprise error response may contain:

* unrelated customer information
* internal diagnostics
* credentials
* operational metadata
* data belonging to another Resource

Noema should retain only what is required to establish and audit the Failure.

For example:

enterprise_error_code
request_id
timestamp

may be sufficient.

The full response need not automatically become part of Context or Audit.

⸻

48. Failure and Environment

Failures must preserve the environment in which they occurred.

Example:

environment = production
execution = EXE-123

must remain distinct from:

environment = staging
execution = EXE-123

A staging failure must never affect a production execution.

Environment is part of the execution boundary.

⸻

49. Failure and Tenant Scope

Failure records must preserve tenant scope.

Example:

tenant = A
execution = EXE-123

must not be confused with:

tenant = B
execution = EXE-123

Execution identifiers must therefore be interpreted within the appropriate authority and tenancy boundary.

⸻

50. Failure and Organizational Scope

Where an enterprise contains multiple organizational or legal boundaries, Failure records must preserve relevant scope.

Examples:

tenant
organization
business_unit
legal_entity
environment

A failure in one organizational boundary must not silently alter the execution state of another.

⸻

51. Failure and Policy Unavailability

If Policy is required to determine whether an Action may proceed or recover and the Policy service is unavailable, Noema must not fail open.

The safe conceptual behavior is:

Policy unavailable
       ↓
Cannot establish required authorization/policy decision
       ↓
FAIL CLOSED
       ↓
ESCALATE / UNKNOWN

The POC specifically requires Policy-service unavailability during evaluation to fail closed rather than produce ALLOW. NOEMA POC Specification PDF.pdf

⸻

52. Failure and Model/Intent Engine Unavailability

If the Intent Engine or model provider is unavailable, Noema must not silently downgrade the trust path to an ungoverned heuristic.

The POC recovery behavior is:

Intent Engine unavailable
       ↓
UNKNOWN
       ↓
Honest response
       ↓
Retry path

The system must not bypass the Trust Engine merely because the model provider is unavailable. NOEMA POC Specification PDF.pdf

⸻

53. Failure and Session Resume

If a Customer abandons a workflow and later resumes it, Noema must not blindly continue from a stale Context snapshot.

Conceptually:

Previous Intent Object
       ↓
Resume
       ↓
Last valid Intent Object version
       ↓
Re-verify current state freshness
       ↓
Continue / Clarify / Reconcile

The POC explicitly requires resumption from the last valid Intent Object version with state freshness re-verified before continuation. NOEMA POC Specification PDF.pdf

⸻

54. Failure and Immutable Intent Versions

Once an Intent Object has been admitted to the Trust Engine, it must not be silently mutated.

If the Customer changes the request after a failure:

Intent v1
   ↓
Execution
   ↓
Failure
   ↓
Customer amendment
   ↓
Intent v2
   ↓
supersedes v1

The amendment must be an explicit, auditable transition.

This prevents a later user statement from silently rewriting the Intent under which a previous Action was authorized.

The POC specifies immutable Intent Object versions with explicit supersedes relationships. NOEMA POC Specification_1.pdf

⸻

55. Failure State Model

The core execution relationship is:

EXECUTING
    │
    ├── known unsuccessful condition ──→ FAILED
    │
    ├── uncertain result ─────────────→ UNKNOWN
    │
    └── verified success ─────────────→ SUCCEEDED

A known Failure may then enter:

FAILED
   ↓
Policy
   ├── RETRY
   ├── RECOVER
   ├── RECONCILE
   ├── ESCALATE
   └── REJECT

An uncertain result follows:

UNKNOWN
   ↓
Fresh Verification
   ↓
Reconciliation

The state machine must not permit a direct transition:

UNKNOWN
   ↓
SUCCEEDED

without sufficient verification evidence.

The POC transaction state model similarly prohibits a terminal-success interpretation of timeout without an intervening verification step. NOEMA POC Specification_1.pdf

⸻

56. Failure Lifecycle

The reference lifecycle is:

Action
   ↓
Execution Attempt
   ↓
Result
   ↓
Failure / Unknown Detected
   ↓
Classify
   ↓
Record Evidence
   ↓
Evaluate Policy
   ↓
Recovery Decision
   ├── Verify
   ├── Reconcile
   ├── Retry
   ├── Wait
   ├── Clarify
   ├── Escalate
   └── Reject
   ↓
Updated Execution State
   ↓
Verified Outcome

Every transition should be deterministic and auditable.

⸻

57. Failure Model

Conceptually:

Failure {
    execution_id
    action_id
    action_version
    execution_attempt_id
    category
    code
    source
    dependency
    occurred_at
    retryable
    recoverable
    safe_to_retry
    message_reference
    evidence_reference
    policy_reference
    resulting_state
    tenant
    organization
    environment
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

58. Failure Relationships

Failure
   │
   ├── belongs_to → Execution
   │
   ├── belongs_to → Execution Attempt
   │
   ├── caused_by → Dependency
   │
   ├── supported_by → Evidence
   │
   ├── governed_by → Policy
   │
   ├── may_trigger → Verification
   │
   ├── may_trigger → Reconciliation
   │
   ├── may_trigger → Retry
   │
   ├── may_trigger → Human Intervention
   │
   └── results_in → Execution State

The relationships preserve causal structure.

⸻

59. Reference Recovery Playbook

The Customer Account Inquiry workflow must explicitly cover at least the following failure scenarios.

Downstream timeout after state-changing submission

Submission
   ↓
Timeout
   ↓
UNKNOWN
   ↓
Re-query source of truth
   ↓
Case found?

Never submit a second state-changing request blindly. NOEMA POC Specification PDF.pdf

Missing webhook confirmation

Webhook missing
      ↓
Do not assume failure
      ↓
Poll source of truth
      ↓
Verify current state

The POC specifically requires direct polling of the source of truth on a bounded backoff schedule. NOEMA POC Specification PDF.pdf

Policy service unavailable

Policy unavailable
      ↓
FAIL CLOSED
      ↓
ESCALATE

Never fail open to ALLOW. NOEMA POC Specification PDF.pdf

Model provider unavailable

Model unavailable
      ↓
UNKNOWN
      ↓
Honest retry path

Do not bypass the Trust Engine with a lower-rigor heuristic. NOEMA POC Specification PDF.pdf

Contradictory enterprise state

Ledger ≠ Switch
      ↓
CONTRADICTORY
      ↓
ESCALATE

Never average or choose the more optimistic source. NOEMA POC Specification_1.pdf

Session resumed after abandonment

Resume
   ↓
Last valid Intent Object version
   ↓
Re-verify freshness
   ↓
Continue

Do not trust a stale Context snapshot merely because it was previously valid. NOEMA POC Specification PDF.pdf

⸻

60. Failure Invariants

Invariant 1

Failure must represent a known unsuccessful execution condition.

Invariant 2

Failure must remain distinct from Unknown execution state.

Invariant 3

Failure must remain distinct from Trust failure.

Invariant 4

Failure must remain distinct from Clarification.

Invariant 5

Missing Context must never be satisfied through guessing.

Invariant 6

Validation failures must prevent invalid Actions from executing.

Invariant 7

Authorization failures must not be bypassed through retries or alternative Resources.

Invariant 8

Resource failure must not cause silent Resource substitution.

Invariant 9

Transport success does not necessarily establish Business Success.

Invariant 10

Verification failure must prevent an Action from being represented as successfully completed.

Invariant 11

Timeout must not automatically be interpreted as Business Failure.

Invariant 12

Unknown execution outcome must remain distinct from Failure.

Invariant 13

An Unknown outcome must be resolved through fresh verification before a potentially consequential retry.

Invariant 14

Retryability must be determined by Action semantics and Policy.

Invariant 15

Retryable does not necessarily mean safe to repeat.

Invariant 16

State-changing Actions must consider idempotency and reconciliation before retry.

Invariant 17

Idempotency identity must be established before execution where supported.

Invariant 18

Each execution attempt must remain distinguishable from the logical Action execution.

Invariant 19

Failure must preserve sufficient Evidence to establish what occurred.

Invariant 20

Failure records must preserve execution, tenant, organizational, and environment scope.

Invariant 21

Failure information must respect enterprise Data Boundaries.

Invariant 22

Downstream Actions blocked by an upstream failure must remain distinguishable from Actions that actually executed and failed.

Invariant 23

Failure cascades must preserve causal relationships.

Invariant 24

Compound execution must preserve individual Action failures independently.

Invariant 25

Partial execution success must remain distinguishable from complete success.

Invariant 26

Contradictory authoritative enterprise state must not be resolved through model preference.

Invariant 27

Stale enterprise state must not silently be treated as current.

Invariant 28

Policy unavailability must not cause consequential execution to fail open.

Invariant 29

Model or Intent Engine unavailability must not bypass the Trust Engine.

Invariant 30

Human intervention must be represented explicitly in the execution lifecycle.

Invariant 31

The model may explain Failure but must not independently define Failure classification.

Invariant 32

Recovery must follow explicit Action and Policy semantics rather than probabilistic model judgment.

Invariant 33

Unknown outcomes must have an explicit verification, reconciliation, or intervention path where applicable.

Invariant 34

Customer-facing responses must reflect verified execution state.

Invariant 35

Noema must never manufacture success because the requested result is unavailable.

Invariant 36

Noema must never manufacture Failure merely because execution evidence is incomplete.

Invariant 37

A later user statement must not silently rewrite the Intent Object version under which an earlier Action was evaluated.

Invariant 38

Failure handling must preserve the distinction between enterprise Business State and Noema Execution State.

Invariant 39

Every consequential Failure must remain reconstructable from structured execution and evidence records rather than model memory.

Invariant 40

The system must fail safely rather than dangerously when required evidence, policy, state, or verification is unavailable.

⸻

61. Final Definition

Failure is the explicit, evidence-backed representation of a known unsuccessful execution condition within Noema.

For the Customer Account Inquiry workflow:

ACTION
   │
   ▼
EXECUTION
   │
   ▼
EXECUTION ATTEMPT
   │
   ▼
RESULT
   │
   ├── SUCCEEDED
   │
   ├── FAILED
   │      │
   │      ├── Detect
   │      ├── Classify
   │      ├── Preserve Evidence
   │      ├── Apply Policy
   │      └── Recover / Escalate / Reject
   │
   ├── UNKNOWN
   │      │
   │      ├── Fresh Verification
   │      └── Reconcile
   │
   └── PARTIAL
          │
          ├── Preserve individual Action states
          └── Continue / Recover / Escalate

And the architectural rule is:

Noema must never treat uncertainty as failure, and must never treat failure as permission to guess. A Failure must be established from execution evidence, classified deterministically, governed by Action semantics and Policy, and resolved through an explicit verification, reconciliation, recovery, escalation, clarification, or rejection path.

The deeper rule is:

NO RESPONSE
     ≠
FAILURE
TIMEOUT
     ≠
FAILED
RETRYABLE
     ≠
SAFE TO RETRY
TRANSPORT SUCCESS
     ≠
BUSINESS SUCCESS
UNKNOWN
     ≠
FAILED
MODEL EXPECTATION
     ≠
EXECUTION EVIDENCE

Noema’s failure model therefore exists not merely to report what went wrong, but to prevent the system from converting incomplete knowledge into an unsafe conclusion or a duplicate consequential Action.

The system must be able to say, with machine-verifiable provenance:

This failed.
Here is why.
Here is the evidence.
Here is what was known.
Here is what remains unknown.
Here is whether retry is permitted.
Here is whether retry is safe.
Here is what was verified.
Here is what Policy requires next.

That is the boundary between failure handling and simply asking an agent to “handle errors gracefully.”