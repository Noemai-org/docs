Execution Record

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/execution-record.md

⸻

1. Definition

An Execution Record is the canonical Noema record of an execution attempt after an Intent has crossed the execution boundary.

It records what Noema authorized for execution, what execution consumer accepted, what actually occurred, and what outcome was reported.

The Execution Record exists to preserve the distinction between:

* Intent
* Trust
* Execution authorization
* Execution
* Outcome

Therefore:

An Execution Record records execution history; it does not define Intent meaning or establish Trust by itself.

⸻

2. Purpose

The Execution Record provides a durable, auditable representation of an execution attempt.

It allows Noema to answer:

* Which Intent produced this execution?
* Which Intent version was executed?
* Which Execution Contract governed it?
* Which Trust decision authorized it?
* Which capability was invoked?
* Which execution consumer accepted it?
* When did execution begin?
* What happened during execution?
* What outcome was reported?
* Was execution successful, failed, partial, or unknown?
* What evidence supports the reported outcome?

The record should be sufficient to reconstruct the execution lifecycle without requiring hidden model reasoning.

⸻

3. Position in the Noema Lifecycle

The canonical relationship is:

Intent
   ↓
Validation
   ↓
Trust Evaluation
   ↓
Execution Eligibility
   ↓
Execution Contract
   ↓
Execution Consumer
   ↓
Execution Record
   ↓
Outcome

The Execution Record therefore belongs to the execution layer.

It does not replace:

* Intent state
* Trust state
* Execution Contract
* Business-system state

⸻

4. Execution Record vs Intent

An Intent describes what the Actor wants to accomplish.

An Execution Record describes an attempt to perform the Action selected for that Intent.

Therefore:

Intent
"What does the Actor want?"
Execution Record
"What execution attempt occurred because of that Intent?"

One Intent may produce:

* zero execution records
* one execution record
* multiple execution records

depending on the execution model.

For example, a composite Intent may result in several independently executed Actions.

⸻

5. Execution Record vs Execution Contract

The Execution Contract defines what may be executed.

The Execution Record records what was actually attempted.

Conceptually:

Execution Contract
        ↓
Defines permitted execution
        ↓
Execution
        ↓
Execution Record
        ↓
Records actual execution

The Execution Record should reference the governing Execution Contract rather than silently becoming the contract itself.

⸻

6. Execution Record vs Business State

The Execution Record is not the authoritative source of business truth.

For example:

Execution Record:
payment request accepted
Payment System:
payment status = pending

The execution record may report what the consumer observed or returned.

The external system remains authoritative for the underlying business state.

Therefore:

Execution history is not equivalent to business truth.

⸻

7. Core Principle

An Execution Record must distinguish between:

what Noema intended to execute

and:

what the external execution system actually reported.

This distinction is essential because execution occurs across system boundaries.

A trusted Intent can produce an execution attempt that:

* succeeds
* fails
* partially succeeds
* is rejected by the consumer
* times out
* produces an unknown outcome

Therefore:

READY ≠ EXECUTED
EXECUTED ≠ SUCCESS
SUCCESS REPORT ≠ NECESSARILY BUSINESS TRUTH

⸻

8. Canonical Execution Record

Conceptually:

ExecutionRecord {
    execution_id
    intent_id
    intent_version
    action_id
    action_version
    execution_contract_id
    execution_contract_version
    trust_evaluation_id
    capability_id
    capability_version
    consumer_id
    state
    requested_at
    accepted_at
    started_at
    completed_at
    input_reference
    target_reference
    result
    failure
    evidence
    provenance
}

The exact schema is defined elsewhere.

The canonical principle is that the record must preserve enough identity and provenance to connect execution back to the Intent and authorization chain.

⸻

9. Execution Identity

Every execution attempt must have a unique execution identifier.

Conceptually:

execution_id

The identifier provides stable reference to the execution attempt.

It must not be confused with:

intent_id
action_id
execution_contract_id
business_transaction_id

These identifiers represent different objects.

⸻

10. Intent Reference

The Execution Record should reference the Intent that caused the execution.

At minimum:

intent_id
intent_version

This preserves the exact semantic version against which the execution was authorized.

A later modification to the Intent must not silently rewrite the historical execution record.

⸻

11. Action Reference

The record should identify the Action that was executed.

Conceptually:

action_id
action_version

This establishes what executable operation the execution consumer received.

The Action should be defined through the canonical Action model rather than being reconstructed from free-form text.

⸻

12. Execution Contract Reference

The record should reference the Execution Contract governing the attempt.

Conceptually:

execution_contract_id
execution_contract_version

This allows Noema to establish:

Intent
   ↓
Trust
   ↓
Contract
   ↓
Execution

The historical contract version must remain reconstructible.

⸻

13. Trust Evaluation Reference

The Execution Record should identify the Trust evaluation that established execution eligibility.

Conceptually:

trust_evaluation_id

This establishes the authorization provenance of the execution attempt.

The record should not merely state:

trusted = true

without preserving which Trust decision established that condition.

⸻

14. Capability Reference

The Execution Record should identify the capability through which execution occurred.

Conceptually:

capability_id
capability_version

This distinguishes:

Action

from:

Capability

The Action describes what Noema intends to cause.

The Capability identifies the system operation through which that Action is performed.

⸻

15. Consumer Identity

The execution consumer should be identifiable.

Conceptually:

consumer_id

The consumer may be:

* a payment service
* CRM
* banking system
* workflow engine
* enterprise API
* internal execution service
* another authorized execution system

The record should identify the consumer responsible for accepting and reporting the execution.

⸻

16. Execution State

The Execution Record should have an explicit execution state.

A conceptual state model is:

ACCEPTED
   ↓
STARTED
   ↓
COMPLETED

with failure paths such as:

ACCEPTED
   ↓
REJECTED
STARTED
   ↓
FAILED
STARTED
   ↓
UNKNOWN

Partial execution may also require an explicit state.

For example:

PARTIALLY_COMPLETED

The exact execution state machine should remain separate from the Trust State Machine.

⸻

17. Accepted

ACCEPTED means the execution consumer has accepted the Execution Contract or execution request.

It does not mean that the Action has completed.

Therefore:

ACCEPTED ≠ COMPLETED

⸻

18. Started

STARTED means execution has actually begun.

This distinction is useful because an execution request may be accepted without the underlying operation having started.

For example:

Noema → Consumer
Consumer accepts request
        ↓
ACCEPTED
Consumer begins operation
        ↓
STARTED

⸻

19. Completed

COMPLETED means the execution consumer has reported successful completion according to its execution semantics.

The record should retain the evidence supporting that result.

However, where an external system is authoritative for business state, the completion report should not automatically be treated as a universal assertion of business truth.

⸻

20. Failed

FAILED means the execution consumer has reported that the execution did not successfully complete.

Failure should be structured.

Examples include:

CONSUMER_REJECTED
TIMEOUT
DEPENDENCY_FAILURE
PRECONDITION_FAILED
VALIDATION_FAILED
AUTHORIZATION_REJECTED
EXECUTION_ERROR

The exact taxonomy should remain extensible.

⸻

21. Partial Completion

Some Actions may produce partial results.

Example:

Composite Intent
    ├── Transfer A → COMPLETED
    ├── Transfer B → FAILED
    └── Transfer C → COMPLETED

The Execution Record must not collapse this into a misleading binary result.

Where partial execution is permitted by the Intent and contract, the execution record should preserve component-level outcomes.

⸻

22. Unknown Outcome

An execution may produce an outcome that Noema cannot establish.

Example:

Request sent
     ↓
Consumer timeout
     ↓
No response

Noema cannot safely conclude:

FAILED

because the external system may have completed the operation despite the missing response.

Therefore:

UNKNOWN

may be required.

This is especially important for non-idempotent Actions.

⸻

23. Unknown Is Not Failure

The distinction is:

FAILED

means failure has been established.

UNKNOWN

means the final outcome cannot be established.

These states must not be conflated.

An unknown execution may require:

* reconciliation
* status lookup
* human intervention
* retry analysis
* consumer-side recovery

⸻

24. Execution Timestamps

The record should preserve meaningful execution timestamps.

Conceptually:

requested_at
accepted_at
started_at
completed_at

Not every execution will contain every timestamp.

For example:

requested_at
accepted_at
rejected_at

may exist for a request that never started.

Timestamps should represent observed lifecycle events rather than inferred times.

⸻

25. Input Reference

Execution inputs should be traceable.

The Execution Record may contain or reference the canonical inputs supplied through the Execution Contract.

Where sensitive information is involved, the record should use appropriate references, redaction, or protected storage rather than unnecessarily duplicating sensitive payloads.

The principle is:

Auditability must not require uncontrolled duplication of sensitive data.

⸻

26. Target Reference

The execution target should be identifiable where applicable.

For example:

customer_123
account_456
ticket_789
payment_321

The reference should use the canonical identifier appropriate to the target system.

Noema should not invent authoritative business identifiers.

⸻

27. Result

The Execution Record may contain a structured execution result.

Conceptually:

result {
    status
    output_reference
    consumer_reference
    observed_at
}

The result should describe what the execution consumer reported.

It should not silently become an authoritative representation of external business state.

⸻

28. Failure Information

Failures should be structured rather than represented only as free-form text.

Conceptually:

failure {
    code
    category
    message
    retryable
    source
}

The human-readable message is useful for diagnostics.

The machine-readable failure code should be canonical.

⸻

29. Provenance

Every Execution Record should preserve provenance sufficient to reconstruct how the execution occurred.

Relevant provenance may include:

* Intent
* Intent version
* Validation result
* Trust evaluation
* Execution Contract
* Action
* Capability
* Consumer
* execution events
* result evidence
* timestamps
* relevant external references

The record should not require access to hidden model reasoning to establish execution provenance.

⸻

30. Execution Event History

An Execution Record may be backed by an event history.

Conceptually:

T0
execution.requested
T1
execution.accepted
T2
execution.started
T3
execution.completed

Or:

T0
execution.requested
T1
execution.accepted
T2
execution.failed

The event history provides a reconstructible execution timeline.

⸻

31. Immutability

Historical execution facts should be append-only or otherwise protected from silent modification.

For example:

execution.started

should not later be rewritten to:

execution.accepted

without preserving the original history.

Corrections should themselves be represented as explicit events or amendments.

⸻

32. Idempotency

Consequential execution requires explicit treatment of idempotency.

An Execution Record should be able to identify the relevant idempotency key where applicable.

Conceptually:

idempotency_key

This helps prevent accidental duplication when retries occur.

The Execution Record should distinguish:

new execution attempt

from:

retry of an existing execution

⸻

33. Retries

A failed or unknown execution may result in a retry.

Retries must not erase the original execution attempt.

Conceptually:

Execution E1
    ↓
UNKNOWN
    ↓
Retry
    ↓
Execution E2

The relationship should remain explicit.

For example:

parent_execution_id
retry_of
attempt_number

may be used.

The exact schema remains an implementation concern.

⸻

34. Execution Record and Trust

Trust establishes eligibility.

Execution records what happened after eligibility was established.

Therefore:

Trust
  ↓
"May this execute?"

while:

Execution Record
  ↓
"What happened when execution was attempted?"

A failed execution does not automatically prove that the preceding Trust decision was incorrect.

⸻

35. Execution Record and Validation

Validation establishes whether the Intent satisfies required structural and semantic conditions.

The Execution Record should therefore be able to trace back to the validated Intent.

However:

VALID
+
TRUST = READY

does not guarantee:

EXECUTION = SUCCESS

Execution occurs against changing external systems.

⸻

36. Execution Record and Consumer Validation

The execution consumer may perform additional validation.

Example:

Noema:
Intent valid
Trust ready
Execution Contract valid
Consumer:
account balance no longer sufficient

The consumer may reject the operation.

The Execution Record should record the rejection without rewriting Noema’s earlier validation history.

This preserves temporal causality.

⸻

37. Execution Boundary

The creation or activation of an Execution Record should correspond to an explicit execution boundary.

Conceptually:

READY
   ↓
Execution Contract accepted
   ↓
Execution Record created
   ↓
EXECUTING

The precise point at which an Execution Record is created may vary by implementation, but the transition must be explicit.

⸻

38. No Execution Without an Execution Contract

Noema should not create an authoritative execution attempt from arbitrary model output.

The canonical path is:

Intent
   ↓
Trust
   ↓
Action
   ↓
Execution Contract
   ↓
Execution Consumer
   ↓
Execution Record

The record should therefore identify the contract governing the execution.

⸻

39. Business Transaction References

An external system may provide its own transaction identifier.

For example:

consumer_transaction_id

This should be retained when available.

It must remain distinct from:

execution_id

because:

* Noema owns the execution record
* the external system owns the business transaction

⸻

40. External Evidence

Execution results may be supported by external evidence.

Examples:

Payment API response
CRM update confirmation
Banking transaction reference
Workflow completion event

The Execution Record should reference such evidence where necessary to establish what the consumer reported.

The evidence itself may remain owned by the external system.

⸻

41. Outcome Verification

Execution completion and outcome verification should remain conceptually distinct where necessary.

For example:

Execution:
API returned success
Verification:
Customer record reflects requested change

For consequential Actions, Noema may require postcondition verification.

The Execution Record should preserve the distinction between:

execution result

and:

verified business outcome

⸻

42. Execution Record and Outcome

The canonical chain is:

Execution
   ↓
Observed Result
   ↓
Verification
   ↓
Outcome

The Execution Record captures the execution and observed result.

The Outcome model may provide the higher-level representation of what ultimately happened.

The exact separation should remain explicit in the architecture.

⸻

43. Composite Execution

A composite Intent may produce multiple execution records.

Example:

Intent I1
   │
   ├── Action A → Execution E1
   ├── Action B → Execution E2
   └── Action C → Execution E3

The relationship between the parent Intent and component executions must be explicit.

This allows Noema to reconstruct both:

* aggregate execution state
* component-level execution state

⸻

44. Atomic Execution

If a composite Action is defined as atomic, the Execution Record should reflect the atomic execution semantics.

Noema must not infer atomicity merely because multiple operations appear related.

Atomicity must be established by the Action and Execution Contract.

⸻

45. Partial Execution

If partial execution is permitted:

A → COMPLETED
B → FAILED
C → COMPLETED

the Execution Record should preserve each component result.

If partial execution is not permitted, Noema must not silently continue executing independent components after an atomicity failure.

Execution semantics must follow the contract.

⸻

46. Human Intervention

An execution may require human intervention.

Examples:

* execution outcome unknown
* external system disagreement
* reconciliation required
* unexpected business state
* policy requires manual handling

The Execution Record should preserve the intervention event.

For example:

EXECUTING
   ↓
UNKNOWN
   ↓
HUMAN_INTERVENTION_REQUIRED

The exact state may belong to the execution or intervention model, but the relationship must remain observable.

⸻

47. Execution Record and Audit

Execution records are a core component of Noema’s auditability.

An audit trail should be able to establish:

Who initiated the Intent?
        ↓
What Intent was resolved?
        ↓
What was validated?
        ↓
What Trust decision was made?
        ↓
What Action was selected?
        ↓
What Contract authorized it?
        ↓
Which Consumer executed it?
        ↓
What happened?
        ↓
What outcome was observed?

The Execution Record is the execution-layer link in this chain.

⸻

48. Security and Sensitive Data

Execution records may contain sensitive information.

Therefore implementations should minimize unnecessary duplication of:

* credentials
* authentication material
* secrets
* financial data
* personal data
* protected business information

The Execution Record should retain references and hashes where sufficient rather than storing raw sensitive payloads unnecessarily.

Security requirements should be defined by the applicable security architecture and data-governance specifications.

⸻

49. Retention

Execution Records should have explicit retention semantics.

Retention may depend on:

* regulatory requirements
* audit requirements
* business requirements
* data sensitivity
* contractual requirements
* operational needs

Retention policy must not silently destroy the provenance required to reconstruct consequential execution.

The exact retention periods are implementation and policy concerns rather than part of this foundational definition.

⸻

50. Versioning

Execution Records should preserve the versions of the objects that materially governed execution.

At minimum, where applicable:

intent_version
action_version
execution_contract_version
capability_version
trust_evaluation_version

This allows historical execution to be reconstructed even as Noema evolves.

⸻

51. Deterministic Reconstruction

Given:

Execution Record
+
referenced versions
+
execution events
+
relevant evidence

Noema should be able to reconstruct the execution lifecycle.

Historical reconstruction must not depend on the current version of a mutable definition.

⸻

52. Execution Record Contract

Conceptually:

RecordExecution(
    Intent,
    ExecutionContract,
    Consumer,
    ExecutionEvents,
    Result
) → ExecutionRecord

The exact implementation may differ.

The canonical requirement is that execution records be structured, inspectable, and attributable.

⸻

53. Canonical Example

Intent:
Transfer ₦500,000 to customer_123
Validation:
VALID
Trust:
READY
Action:
TRANSFER_FUNDS
Execution Contract:
EC-123
Consumer:
Payment Service
Execution:
E-456
State:
STARTED
Consumer Result:
transaction_reference = TX-789
Verification:
payment provider reports transaction completed
Execution State:
COMPLETED

The record connects the execution back to the governing Intent and Contract without becoming the source of truth for the payment system.

⸻

54. Failure Example

Intent:
Send invoice to customer_123
Validation:
VALID
Trust:
READY
Execution Contract:
EC-321
Consumer:
Email Service
Execution:
E-654
State:
FAILED
Failure:
EMAIL_PROVIDER_UNAVAILABLE

The failure should not alter the historical fact that the Intent was valid and trusted at the time execution began.

⸻

55. Unknown Outcome Example

Intent:
Transfer ₦5,000,000
Trust:
READY
Execution:
E-777
Consumer:
Banking Service
Request:
accepted
Response:
timeout
Outcome:
UNKNOWN

Noema should not infer:

FAILED

unless the authoritative system establishes failure.

A reconciliation step may therefore be required.

⸻

56. Execution Record Lifecycle

A conceptual lifecycle is:

REQUESTED
    ↓
ACCEPTED
    ↓
STARTED
    ↓
COMPLETED

with alternative paths:

REQUESTED
    ↓
REJECTED
STARTED
    ↓
FAILED
STARTED
    ↓
UNKNOWN

and where permitted:

STARTED
    ↓
PARTIALLY_COMPLETED

The final implementation may use a more granular state model.

⸻

57. State Transition Principles

Execution state transitions must be:

* explicit
* attributable
* timestamped
* deterministic with respect to observed events
* auditable

A model’s interpretation of an execution response must not silently rewrite an authoritative consumer event.

⸻

58. Execution Record Invariants

Invariant 1

Every Execution Record represents a specific execution attempt or explicitly defined execution lifecycle.

Invariant 2

Every execution must be traceable to an Intent.

Invariant 3

Every consequential execution must be traceable to an Execution Contract.

Invariant 4

Execution Records do not replace authoritative business state.

Invariant 5

Execution state must remain distinct from Trust state.

Invariant 6

ACCEPTED does not imply COMPLETED.

Invariant 7

UNKNOWN must not be silently converted into FAILED or COMPLETED.

Invariant 8

Retries must not erase previous execution attempts.

Invariant 9

Historical execution records must remain reconstructible.

Invariant 10

Execution results must have provenance.

Invariant 11

Partial execution must be explicit.

Invariant 12

Noema must not infer permission for partial execution.

Invariant 13

Consumer-side validation may reject an execution after Noema has established Trust.

Invariant 14

Execution success does not automatically establish authoritative business truth.

Invariant 15

Sensitive execution data must not be duplicated unnecessarily.

⸻

59. Canonical Relationship

The complete execution relationship is:

                 ┌──────────────┐
                 │    Intent    │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Validation   │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │    Trust     │
                 └──────┬───────┘
                        │
                      READY
                        │
                        ▼
                 ┌──────────────┐
                 │Action/Contract│
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Consumer   │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │Execution     │
                 │   Record     │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Verification │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Outcome    │
                 └──────────────┘

This separation preserves the Noema boundary between understanding, Trust, execution, and business truth.

⸻

60. Canonical Mental Model

The Execution Record can be reduced to five questions:

1. What Intent caused this execution?
2. What Action and Contract governed it?
3. Which consumer performed or accepted it?
4. What actually happened during execution?
5. What evidence supports the reported result?

These questions define the minimum conceptual responsibility of the Execution Record.

⸻

61. Final Definition

An Execution Record is Noema’s structured, auditable representation of an execution attempt and its observed execution lifecycle, linked to the Intent, Trust decision, Action, Execution Contract, capability, consumer, and resulting evidence.

The core invariant is:

Noema records what was authorized and what execution reported; it does not confuse execution history with authoritative business truth.