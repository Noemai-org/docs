> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Failure

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/failure.md

⸻

1. Definition

Failure is the canonical representation of an execution in which an attempted Action is established, through sufficient evidence, to have not successfully completed according to the applicable execution semantics.

Failure is an execution-domain fact.

Failure must be distinguished from:

* REJECTED
* CANCELLED
* EXPIRED
* TIMED_OUT
* UNKNOWN
* BLOCKED
* COMPENSATED

because these states have materially different semantics.

Failure does not describe whether an Intent was valid, whether Trust was correct, or whether the enterprise business state ultimately reflects the requested Outcome.

⸻

2. Core Principle

Noema must represent failure explicitly without confusing failure with uncertainty.

The critical distinction is:

FAILURE
=
the system has sufficient evidence that the attempted Action did not succeed
UNKNOWN
=
the system does not have sufficient evidence to establish whether the Action succeeded

Therefore:

timeout ≠ failure
unknown ≠ failure
rejection ≠ failure
blocked ≠ failure

unless authoritative evidence establishes the appropriate classification.

⸻

3. Failure Belongs to Execution

Failure occurs within execution semantics.

Source of Intent
      ↓
Intent
      ↓
Action
      ↓
Hard Schema Validation
      ↓
Resolution / State Reconciliation
      ↓
Deterministic Trust
      ↓
Action Contract
      ↓
Execution
      ↓
Failure

The existence of a failure does not mean:

* the Intent was invalid
* the Action was invalid
* Trust was incorrect
* the user necessarily made an error

An Action may be correctly interpreted, resolved, trusted, contracted, and dispatched while still failing during execution.

⸻

4. Failure vs Invalid Intent

Consider:

Intent:
"Refund my payment."

Suppose the Intent resolves correctly to:

refund_payment

The Intent is schema-valid, the target is resolved, applicable state is reconciled, and Trust permits execution.

Execution then fails because the payment provider is unavailable.

The correct interpretation is:

Intent       = valid
Action       = valid
Trust        = EXECUTE
Execution    = failed

Failure therefore belongs to execution semantics.

⸻

5. Failure vs Trust Denial

If Trust determines:

REJECT

then execution must not occur.

Therefore:

Trust
  ↓
REJECT
  ↓
No Execution

Whereas:

Trust
  ↓
EXECUTE
  ↓
Execution
  ↓
FAILURE

represents an execution failure.

CLARIFY and ESCALATE similarly do not represent execution failure when no consequential execution has occurred.

Trust outcomes are canonical:

EXECUTE
CLARIFY
ESCALATE
REJECT

They must not be replaced by execution failure classifications.

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
CONFLICT_FAILURE
EXECUTION_FAILURE
INTERNAL_FAILURE

A timeout may be recorded as an execution condition or failure-related event, but a timeout alone does not establish failure.

The taxonomy may evolve.

The important requirement is that established failures remain machine-classifiable.

⸻

7. Validation Failure

A validation failure occurs when an attempted execution cannot proceed because required execution inputs or execution-bound structures are invalid.

Example:

refund_payment
payment_id = null

Result:

VALIDATION_FAILURE

Validation may occur at multiple deterministic boundaries.

Hard schema validation and admission occur before canonical execution semantics are admitted. A later consumer-side validation failure may still occur because the enterprise system can impose execution-time constraints that were unavailable or changed after admission.

Such a failure does not permit the model to reinterpret or repair the Action automatically.

⸻

8. Authorization Failure

An execution consumer may determine that the supplied execution request is not technically authorized for the requested operation.

Example:

Action:
delete_customer
Consumer:
required authorization scope missing
Result:
AUTHORIZATION_FAILURE

This should not normally occur when Noema’s Trust evaluation, Action Contract, and enterprise authorization integration are correctly aligned, but the execution boundary must remain defensive.

Authorization failure must not be treated as evidence that the Intent itself was invalid.

Technical authorization, policy authorization, and business authorization remain distinct concepts.

⸻

9. Business Failure

A business failure occurs when the Action is structurally valid and execution is permitted to be attempted, but current enterprise business state prevents the requested operation from completing.

Example:

refund_payment
payment.status = REFUNDED

or:

payment.status = NOT_REFUNDABLE

Result:

BUSINESS_FAILURE

The relevant enterprise business state remains owned by the enterprise system of record.

The Failure record describes the execution condition rather than becoming a replacement source of business truth.

⸻

10. Dependency Failure

A dependency failure occurs when an external or downstream dependency required for execution cannot successfully support the operation.

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

The Action may remain valid and correctly authorized.

A dependency failure may be retryable, but retryability is determined by explicit execution semantics, idempotency, policy, and current state rather than model judgment.

⸻

11. Resource Failure

A resource failure occurs when required execution infrastructure or execution resources are unavailable or exhausted.

Examples:

database unavailable
connection pool exhausted
disk unavailable
queue unavailable
capacity exhausted

Result:

RESOURCE_FAILURE

Resource availability does not itself establish whether the underlying business Action occurred.

If execution uncertainty remains after resource failure, the execution may require reconciliation and remain UNKNOWN.

⸻

12. Network Failure

A network failure occurs when communication required to execute or observe an Action fails.

Examples:

connection refused
DNS failure
connection reset
TLS failure

Network failure is often retryable, but not always.

A lost response after a potentially successful request is not automatically a Failure. If the request may have reached the enterprise system, execution must be treated as UNKNOWN until authoritative evidence establishes what occurred.

⸻

13. Timeout

A timeout means that an expected execution response or completion condition was not observed within the applicable time boundary.

A timeout alone does not establish that the Action failed.

Therefore:

TIMEOUT
   ↓
RECONCILIATION
   ↓
SUCCESS
FAILURE
UNKNOWN

The timeout should be preserved as an execution condition and historical event even if later reconciliation establishes success or failure.

Timeout is therefore not a substitute for Outcome classification.

⸻

14. Conflict Failure

A conflict failure occurs when an Action cannot be completed because relevant enterprise state changed concurrently or no longer satisfies the execution preconditions.

Example:

update_order(order_123)
expected:
order.version = 7
actual:
order.version = 8

Result:

CONFLICT_FAILURE

The current authoritative state may be returned as evidence for State Reconciliation.

A conflict does not permit the system to silently modify the Action or retry against a newly observed state unless the applicable Action and policy explicitly permit that behavior.

⸻

15. Internal Failure

An internal failure occurs when the execution consumer or execution infrastructure encounters an unexpected internal condition.

Examples:

panic
unexpected exception
corrupt internal state
unhandled implementation error

Result:

INTERNAL_FAILURE

Diagnostic details should be retained according to security and observability policy without exposing unnecessary implementation details to the Intent layer or end user.

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
    evidence_refs
}

For consequential execution, the structure should also preserve sufficient lineage and semantic context to establish:

* the exact Action Instance
* the exact Action Contract version
* the exact Intent Object version
* the execution attempt
* the relevant actor and resolved target
* the applicable execution context
* the evidence supporting classification

This is a semantic model, not a final storage schema.

⸻

17. Failure Identity

Every material failure must have an identifiable relationship to the execution that produced it.

execution_id
      ↓
failure_id

Example:

execution:
exec_123
failure:
fail_456

Failure identity must not replace execution identity.

The execution remains the primary causal object, while a Failure identifies a material unsuccessful execution condition.

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

Codes should be stable enough to support deterministic policy evaluation, metrics, recovery logic, and audit.

A failure code must not silently change semantic meaning across versions.

⸻

19. Failure Message

A human-readable message may provide contextual explanation.

Example:

Payment provider rejected the refund because the transaction
has already been fully refunded.

The message is explanatory.

The structured failure category and code are the machine-relevant semantic fields.

User-facing explanations may be derived from these structured fields but must respect data boundaries and authorization requirements.

⸻

20. Failure Source

Failure should identify the component or authority from which the failure condition originated.

Possible sources include:

NOEMA
CONSUMER
BUSINESS_SYSTEM
EXTERNAL_PROVIDER
NETWORK
RESOURCE
UNKNOWN

Example:

source:
PAYMENT_PROVIDER

Source identifies origin.

It does not automatically establish authority for every claim associated with the failure.

Authority remains claim-specific.

⸻

21. Failure Evidence

A consequential Failure should be supported by evidence.

Examples:

provider_error_code
provider_transaction_id
HTTP status
business-state observation
resource version
consumer receipt
enterprise event
authoritative status response

Evidence must retain provenance and applicable temporal semantics.

Evidence is distinct from Fact Status.

For example:

Evidence:
provider status response
Fact Status:
VERIFIED

The evidence supports a fact; it is not itself the Fact Status.

⸻

22. Failure Certainty

Failure classification requires sufficient evidence.

Conceptually:

CONFIRMED_FAILURE

requires evidence sufficient to establish that the attempted Action did not succeed.

A signal such as:

POSSIBLE_FAILURE

should generally not be represented as an authoritative Failure.

If the available evidence cannot distinguish success from failure, the execution should remain:

UNKNOWN

This preserves Noema’s deterministic treatment of uncertainty.

⸻

23. Failure vs Unknown

Consider:

request sent
     ↓
connection lost

There are at least two possible realities:

provider executed request

or:

provider never received request

Without authoritative reconciliation:

UNKNOWN

not:

FAILURE

State Reconciliation should determine whether the enterprise system can establish the current execution/business state.

⸻

24. Failure State

A conceptual execution lifecycle is:

EXECUTING
    │
    ▼
FAILED

The Failure record explains why the execution entered a failed state.

Execution state and failure reason remain separate concepts.

Similarly:

TIMED_OUT
UNKNOWN
BLOCKED
CANCELLED

must not be treated as interchangeable Failure categories.

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
RECOVERY DECISION
   ↓
RETRY
   ↓
EXECUTING

The final Outcome may eventually be successful.

The original Failure remains permanently part of execution history.

⸻

26. Retryable Failure

A Failure may carry:

retryable = true

Example:

DEPENDENCY_UNAVAILABLE
retryable = true

But retryability must be bounded by:

max_attempts
time budget
Action semantics
idempotency
current enterprise state
policy
contract validity

A model must not independently determine that a Failure should be retried.

⸻

27. Non-Retryable Failure

Example:

INSUFFICIENT_FUNDS

Repeatedly executing:

charge_payment

will not normally resolve the condition.

Therefore:

retryable = false

The next step may instead be:

new Intent
clarification
escalation
compensation
termination

depending on the Action semantics and applicable policy.

⸻

28. Failure and Retry Policy

Retry must be deterministic where it has material consequences.

Example:

Failure:
NETWORK_FAILURE
Policy:
retry ≤ 3 times
with exponential backoff

The model must not decide:

"Let's try one more time."

based on intuition or confidence.

Retry must also respect idempotency and execution identity.

A retry must not create an unintended second business occurrence.

⸻

29. Failure and Compensation

Failure may produce a compensation evaluation, but it does not automatically produce compensation.

Example:

reserve_inventory → SUCCESS
charge_payment    → FAILURE

The reservation may require compensation.

But:

send_email → FAILURE

may require no compensation.

The relationship is:

Failure
   ↓
Evaluate Recovery
   ├── Retry
   ├── Compensate
   ├── Escalate
   └── Terminate

Compensation must itself use an explicit Action, Action Contract, Trust evaluation, execution, and verification path.

Noema must not infer an inverse Action merely because an Action failed.

⸻

30. Partial Failure

Composite execution may produce partial failure.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE

The execution group may therefore be classified as:

PARTIALLY_FAILED

rather than simply:

FAILED

The exact parent classification is determined by the composite execution semantics.

The distinction matters for recovery, compensation, verification, and Outcome evaluation.

⸻

31. Partial Failure Model

Conceptually:

Execution Group
├── Action A → SUCCESS
├── Action B → SUCCESS
└── Action C → FAILURE

Each child execution must retain its own:

* execution identity
* status
* attempts
* evidence
* failure, where applicable
* Outcome, where established

The parent execution summarizes child facts without erasing them.

⸻

32. Failure Propagation

A child Action Failure may affect dependent Actions.

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

A dependent Action that was never attempted has not itself failed.

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

Blocked is an execution-control state, not a Failure category.

⸻

34. Failure Propagation Must Be Explicit

Noema must not infer arbitrary downstream failure.

Dependency relationships determine propagation.

A → B

means that failure of A may affect B.

The exact behavior must be defined by the execution graph and applicable semantics.

Possible results include:

BLOCKED
CANCELLED
SKIPPED
COMPENSATION_REQUIRED

A downstream Action must not be reported as failed unless it was actually attempted and its unsuccessful execution was established.

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

The final Outcome may establish that the requested operation completed successfully.

The original Failure remains part of the execution history.

Outcome must not be retroactively rewritten into the Failure record.

⸻

36. Failure History Is Immutable

A successful retry must not erase:

Attempt 1 → FAILURE

It should produce:

Attempt 1 → FAILURE
Attempt 2 → SUCCESS

This preserves:

* auditability
* debuggability
* causal history
* operational evidence
* recovery history

Historical execution facts are not silently rewritten because a later attempt succeeded.

⸻

37. Failure and Auditability

For consequential Actions, the system should be able to answer:

* What failed?
* Why did it fail?
* When did it fail?
* Which Action was being executed?
* Which Action Contract version governed execution?
* Which Intent Object version initiated the operation?
* Which consumer attempted it?
* Which actor and target were resolved?
* What evidence established the failure?
* Was State Reconciliation performed?
* Was it retried?
* Was it compensated?
* What ultimately happened?

Failure records provide one part of this causal chain.

The complete audit trail should connect:

Intent version
   ↓
Trust Decision
   ↓
Action / Contract
   ↓
Execution attempt
   ↓
Failure
   ↓
Reconciliation / Recovery
   ↓
Subsequent execution
   ↓
Verification
   ↓
Outcome

⸻

38. Failure and Determinism

The model must not convert probabilistic signals into authoritative Failure states.

For example:

LLM:
"The payment probably failed."

is insufficient evidence.

Instead:

Payment provider:
transaction status = DECLINED

may support:

CONFIRMED FAILURE

provided the source is authoritative for the relevant claim and the observation has passed the applicable validation/admission and reconciliation requirements.

Model confidence is not Fact Status and cannot establish Failure by itself.

⸻

39. Failure and Evidence

Evidence should be evaluated according to provenance, authority, temporal validity, and semantic relevance.

Conceptually:

authoritative business system
        ↓
validated execution consumer observation
        ↓
transport / infrastructure evidence
        ↓
model inference

This is not a universal source hierarchy.

A source being closer to execution does not automatically make it authoritative for every claim.

Authority is claim-specific.

Inference must not override authoritative execution evidence.

⸻

40. Failure and Business State

A Failure should describe the execution condition without unnecessarily duplicating the enterprise’s entire business state.

Example:

failure.code:
PAYMENT_ALREADY_REFUNDED

rather than storing an uncontrolled snapshot of every payment attribute.

Relevant enterprise observations may be attached separately as evidence and reconciled state.

The enterprise system of record remains authoritative for the underlying business state.

⸻

41. Failure and Policy Evaluation

Failure can trigger deterministic recovery policies.

Example:

Failure:
PAYMENT_PROVIDER_UNAVAILABLE
Policy:
retry up to 3 times

Another:

Failure:
PAYMENT_ALREADY_REFUNDED
Policy:
reconcile the requested Outcome against current enterprise state

Another:

Failure:
REFUND_PROHIBITED
Policy:
escalate for human intervention

The Failure itself does not determine the recovery action.

Policy and execution semantics do.

⸻

42. Failure and Clarification

Not every Failure requires clarification.

However, a Failure may reveal that the original Intent cannot be completed under current conditions and that additional information is required.

Example:

Intent:
"Book the cheapest flight."
Execution:
FAILURE — no flight satisfies the applicable constraints.

Noema may require clarification or a new Intent if additional constraints are necessary.

This is different from a purely technical execution failure.

If the semantic goal itself materially changes, Noema must create a new Intent version rather than silently modifying the existing admitted Intent.

⸻

43. Failure and Intent State

The Intent lifecycle should distinguish:

EXECUTION_FAILED

from:

INTENT_INVALID
INTENT_AMBIGUOUS
CLARIFICATION_REQUIRED

The failure of an Action does not retroactively make the Intent ambiguous or invalid.

An admitted Intent remains historically immutable.

If recovery requires a materially different request, the system creates a new Intent version with explicit lineage.

⸻

44. Failure and User Communication

Failure messages exposed to users should be derived from structured failure information and verified execution facts.

The user-facing explanation should communicate:

* what could not be completed
* why, when known
* whether the result is actually known
* what can happen next

It must not expose unnecessary secrets, credentials, internal infrastructure details, protected data, or private model reasoning.

If execution remains UNKNOWN, the user must not be told that the Action definitely failed merely because a timeout or transport error occurred.

⸻

45. Failure Classification

A useful canonical classification is:

┌─────────────────────────┐
│        FAILURE          │
├─────────────────────────┤
│ Validation              │
│ Authorization           │
│ Business                │
│ Dependency              │
│ Resource                │
│ Network                 │
│ Conflict                │
│ Execution               │
│ Internal                │
└─────────────────────────┘

Timeout and Unknown conditions remain distinct when execution evidence cannot establish failure.

BLOCKED, CANCELLED, and REJECTED are execution/control outcomes rather than Failure categories.

⸻

46. Failure Transition Model

EXECUTING
    │
    ├──────────────→ COMPLETED
    │                   │
    │                   └── VERIFY
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
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                 SUCCESS             FAILURE

Reconciliation may establish that an apparently timed-out execution actually succeeded.

⸻

47. Failure Recovery

A Failure may lead to:

RETRY
COMPENSATION
ESCALATION
CLARIFICATION
TERMINATION

The choice must be determined by explicit execution semantics, Action Contract constraints, current reconciled state, idempotency, and applicable policy.

Where recovery itself is consequential, it must pass through the same deterministic trust and execution boundaries.

⸻

48. Failure Does Not Imply User Error

A Failure may be entirely infrastructural.

Example:

User Intent:
"Send ₦50,000."
Intent:
valid
Action:
valid
Trust:
EXECUTE
Execution:
payment provider unavailable
Failure:
DEPENDENCY_FAILURE

The user did nothing wrong.

Noema should not describe an infrastructural or provider failure as user error.

⸻

49. Failure Does Not Imply System Error

Similarly:

INSUFFICIENT_FUNDS

may be a legitimate business failure rather than an infrastructure problem.

The classification should preserve the distinction between:

business condition

and:

technical execution condition

This distinction matters for recovery, user communication, metrics, and policy.

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

Consumer output remains untrusted until it passes the applicable contract/schema validation and admission boundary.

A consumer response must not redefine the Action Contract or create new executable semantics.

⸻

51. Failure and Compensation Lineage

When compensation follows a Failure:

Action
  ↓
Execution
  ↓
Failure
  ↓
Compensation Evaluation
  ↓
Compensation Action
  ↓
Trust
  ↓
Compensation Contract
  ↓
Compensation Execution
  ↓
Verification
  ↓
Compensation Outcome

The compensation must reference the Failure and original execution that triggered the evaluation.

Conceptually:

compensation_id
      ↓
failure_id
      ↓
execution_id
      ↓
contract_id
      ↓
action_id
      ↓
intent_version

Compensation is a new execution lineage. It does not mutate the original Failure.

⸻

52. Failure and Observability

Material Failure should be observable through mechanisms appropriate to the implementation:

logs
metrics
traces
execution records
events
audit records
Operational Memory

The implementation may vary.

The semantic requirement is that material failures are not silent and remain causally attributable.

Operational Memory may retain structured failure history, but it is not a source of enterprise business authority.

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

Metrics must not collapse UNKNOWN into Failure merely to simplify reporting.

⸻

54. Failure Security

Failure records may contain sensitive operational information.

Therefore:

provider credentials
secrets
tokens
private internal infrastructure details
protected enterprise data

must not be exposed merely because they exist in the underlying error.

Failure information must follow Noema’s data boundaries, authorization, retention, and audit policies.

The model must not receive credentials or unrestricted internal failure payloads merely because it is generating a user-facing explanation.

⸻

55. Failure and State Reconciliation

State Reconciliation is a first-class recovery mechanism for execution uncertainty and state divergence.

A typical path is:

Execution
   ↓
Failure / Timeout / Unknown
   ↓
Observe authoritative enterprise state
   ↓
Hard Schema Validation / Admission
   ↓
State Reconciliation
   ↓
Reconciled Facts / Fact Status
   ↓
Trust / Preconditions / Recovery Evaluation

Reconciliation is particularly important when:

* the consumer reports conflicting information
* a timeout leaves operation state uncertain
* a network failure occurs after dispatch
* business state changed concurrently
* retry safety depends on current state
* compensation eligibility depends on what actually occurred

Reconciliation must not silently rewrite historical execution facts.

⸻

56. Failure, Fact Status, and Outcome

Failure, Evidence, Fact Status, Execution State, and Outcome are distinct.

For example:

Evidence:
provider response
Fact Status:
VERIFIED
Execution State:
FAILED
Outcome:
UNFULFILLED

or:

Evidence:
request timeout
Fact Status:
UNKNOWN
Execution State:
UNKNOWN
Outcome:
UNKNOWN

A Failure record cannot itself establish that an enterprise business state changed.

The enterprise system of record remains authoritative for the relevant business state.

Similarly, Trust EXECUTE does not mean that execution succeeded.

⸻

57. Failure and Versioned Lineage

Consequential Failure records should preserve the semantic versions relevant to the attempted execution.

At minimum, where applicable:

intent_version
action_version
action_contract_version
execution_version
trust_decision_version
policy_version
graph_version
capability_version
integration_version
system_version

These version dimensions must remain distinct.

A later contract, policy, integration, or graph version must not silently change the interpretation of a historical Failure.

⸻

58. Failure and Replay

Historical execution events and Failure records may be replayed for:

* audit
* diagnostics
* reconciliation
* recovery analysis
* testing

Replay must not create a new enterprise business occurrence by default.

A replayed Failure is historical evidence about a prior execution.

If current policy or state is reevaluated, that is a new evaluation with its own identity and provenance; the historical Failure remains unchanged.

⸻

59. Failure and Planner Boundaries

The planner may use established Failure information to select among permitted recovery paths.

It may not:

* invent a new Action
* invent a compensation operation
* create authority
* modify an Action Contract
* bypass Trust
* bypass State Reconciliation
* directly access enterprise systems
* convert uncertainty into Failure

Recovery options must come from the Enterprise Action Graph, Capability Registry, Action Model, Action Contract Registry, and applicable deterministic policy.

⸻

60. Failure and Structural Security

The Failure model operates inside Noema’s hard security boundary.

The following are untrusted inputs:

user input
model output
retrieved enterprise text
tool responses
consumer messages
external provider messages

They must not directly create executable consequences.

The model has no direct credentials or unrestricted enterprise access.

A structured Failure returned by a consumer is therefore subject to deterministic validation and admission before it can influence recovery, Trust, retry, compensation, or user-visible claims.

⸻

61. Failure Invariants

Invariant 1

Failure means the system has sufficient evidence that an attempted Action did not complete successfully.

Invariant 2

Failure must not be inferred from uncertainty alone.

Invariant 3

Unknown execution state must remain distinct from Failure.

Invariant 4

Timeout must not automatically be classified as Failure.

Invariant 5

Trust REJECT is not execution Failure because consequential execution should not occur.

Invariant 6

A BLOCKED dependent Action is not a failed Action if it was never executed.

Invariant 7

Failure does not invalidate the original Intent by itself.

Invariant 8

Failure does not automatically imply retry.

Invariant 9

Failure does not automatically imply compensation.

Invariant 10

Retry attempts must preserve prior Failure history.

Invariant 11

Failure classification must be machine-readable.

Invariant 12

Consequential Failures should be supported by sufficient evidence.

Invariant 13

Recovery decisions must be deterministic where their consequences are material.

Invariant 14

A successful retry must not erase the original Failure.

Invariant 15

Composite execution must preserve individual child failures.

Invariant 16

Failure records must maintain lineage to the execution that produced them.

Invariant 17

A consumer-reported Failure must pass the applicable validation and admission boundary before it is used as authoritative execution evidence.

Invariant 18

Failure evidence must remain distinct from Fact Status, Execution State, Outcome, and enterprise Business State.

Invariant 19

A timeout or transport error must enter reconciliation when execution may have occurred.

Invariant 20

Historical Failure records must not be silently rewritten by later successful execution or current-state reevaluation.

Invariant 21

Recovery must not invent Actions, capabilities, authority, or compensation semantics.

Invariant 22

The exact admitted Intent Object version must remain traceable through consequential execution and Failure.

Invariant 23

Resolved actor, Action, target, resource, and applicable scope must remain traceable for consequential Failure.

Invariant 24

Trust EXECUTE establishes permission to proceed under evaluated conditions; it does not establish execution success.

Invariant 25

Failure does not establish enterprise Business State unless authoritative enterprise evidence separately establishes that state.

Invariant 26

Replay of historical Failure must not create a new enterprise business occurrence by default.

Invariant 27

Operational Memory may retain Failure history but must not become the authority for enterprise Business State.

Invariant 28

The model must not independently classify probabilistic inference as authoritative Failure.

Invariant 29

Read-only execution can still produce consequential Failure when protected information or downstream effects are involved.

Invariant 30

Failure classification and recovery semantics must remain stable across contract versions unless an explicit semantic version change defines otherwise.

⸻

62. Canonical Mental Model

The simplest model is:

                    EXECUTION
                        │
              ┌─────────┴─────────┐
              │                   │
          SUCCESS              FAILURE
                                  │
                     ┌────────────┼────────────┐
                     │            │            │
                   RETRY      COMPENSATE    ESCALATE
                     │            │            │
                     ▼            ▼            ▼
                 EXECUTION     RECOVERY     REVIEW

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
HARD VALIDATION / ADMISSION
    │
    ▼
STATE RECONCILIATION
    │
    ├── SUCCESS
    │
    ├── FAILURE
    │
    └── UNKNOWN

The key rule is:

uncertainty → reconciliation
not
uncertainty → failure

⸻

63. Final Definition

Failure is the explicit, evidence-backed execution-domain state in which an attempted Action is established not to have successfully completed according to its applicable execution semantics.

Failure is distinct from Trust denial, cancellation, blocking, timeout, and unknown execution state.

A failed Action is one whose unsuccessful execution is known. An Action whose result cannot yet be established must remain UNKNOWN until sufficient authoritative evidence and State Reconciliation establish what happened.

Recovery—whether retry, compensation, escalation, clarification, or termination—is a separate deterministic decision governed by Action semantics, current reconciled state, idempotency, policy, and explicit execution constraints.

The core invariant is:

Noema must never turn uncertainty into Failure.

And the broader execution principle is:

Failure records what is known about an unsuccessful execution.
State Reconciliation establishes what can be known.
Outcome records the verified semantic result.
Enterprise systems remain authoritative for enterprise Business State.