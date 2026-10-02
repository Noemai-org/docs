> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Execution Record

Status: Foundational
Version: 0.2
Domain: Architecture
Canonical Path: architecture/execution-record.md

⸻

1. Definition

The Execution Record is the canonical Noema record of an execution attempt and its observed execution lifecycle after an Intent crosses the execution boundary.

It records:

* what Intent and Action gave rise to the execution,
* which Trust decision established execution eligibility,
* which Execution Contract governed the attempt,
* which Capability and Execution Consumer were involved,
* what execution events occurred,
* what the consumer reported,
* what evidence supports those reports, and
* what execution state resulted.

The Execution Record preserves the distinction between:

Intent
   ↓
Trust
   ↓
Execution Authorization
   ↓
Execution
   ↓
Observed Result
   ↓
Outcome Verification
   ↓
Outcome

The Execution Record does not:

* define Intent meaning,
* establish Trust,
* create authorization,
* execute Actions,
* own authoritative business state, or
* independently determine business outcome.

Its responsibility is to provide the canonical, attributable record of what occurred at the execution layer.

⸻

2. Purpose

The Execution Record provides a durable and auditable representation of execution.

It allows Noema to reconstruct:

* which Intent produced the execution,
* which Intent version was involved,
* which Action was executed,
* which Execution Contract governed it,
* which Trust evaluation established execution eligibility,
* which Capability was invoked,
* which Execution Consumer accepted or performed the operation,
* when execution was requested, accepted, started, and completed,
* what execution events occurred,
* what result the consumer reported,
* what failures occurred,
* whether the result was complete, partial, failed, or unknown, and
* what evidence supports the recorded result.

The record must be sufficient to reconstruct the execution lifecycle without requiring access to hidden model reasoning.

⸻

3. Position in Noema

The canonical relationship is:

Intent
   ↓
Validation
   ↓
Trust Evaluation
   ↓
Execution Planning
   ↓
Plan Validation
   ↓
Execution Contract
   ↓
Durable Workflow
   ↓
Execution Consumer
   ↓
Execution Record
   ↓
Outcome Verification
   ↓
Outcome

The Execution Record therefore belongs to the execution layer.

It does not replace:

* Intent,
* Trust,
* Execution Plan,
* Execution Contract,
* Workflow state, or
* authoritative business-system state.

⸻

4. Execution Record vs Intent

An Intent represents what the Actor wants to accomplish.

An Execution Record represents an execution attempt resulting from an approved execution path for that Intent.

Therefore:

Intent
"What does the Actor want?"
Execution Record
"What execution attempt occurred because of that Intent?"

One Intent may produce:

* no Execution Record,
* one Execution Record, or
* multiple Execution Records.

A composite Intent may produce multiple component executions.

The relationship between the Intent and those executions must remain explicit.

⸻

5. Execution Record vs Execution Plan

The Execution Plan defines the intended execution structure.

The Execution Record records what happened when that structure was executed.

Therefore:

Execution Plan
      ↓
Defines intended execution
      ↓
Execution
      ↓
Execution Record
      ↓
Records observed execution

The Execution Record must reference the applicable Plan and Plan version where the Plan is part of the execution lifecycle.

It must not reconstruct the historical Plan from current definitions.

⸻

6. Execution Record vs Execution Contract

The Execution Contract establishes the execution boundary and defines the terms under which an Action may be performed.

The Execution Record records the execution attempt governed by that Contract.

Therefore:

Execution Contract
      ↓
Defines execution boundary
      ↓
Execution Consumer
      ↓
Execution Record
      ↓
Records observed execution

The Execution Record must reference the governing Contract and Contract version.

It must not silently become a substitute for the Contract.

⸻

7. Execution Record vs Business State

The Execution Record is not authoritative business state.

For example:

Execution Record:
payment request accepted
Payment System:
payment status = pending

The Execution Record may accurately record that the consumer accepted the request while the Payment System remains authoritative for the payment’s business state.

Therefore:

Execution history ≠ Business truth

The authoritative enterprise system remains the source of truth for the business state it owns.

⸻

8. Core Principle

The Execution Record must distinguish between:

What Noema authorized for execution

and:

What the execution system actually reported

Execution occurs across system boundaries and therefore cannot be assumed to produce a successful or authoritative business outcome merely because execution was authorized.

Consequently:

READY ≠ EXECUTED
EXECUTED ≠ SUCCESS
SUCCESS REPORT ≠ NECESSARILY VERIFIED BUSINESS OUTCOME

⸻

9. Canonical Execution Record

Conceptually:

ExecutionRecord {
    execution_id
    intent_id
    intent_version
    plan_id
    plan_version
    action_id
    action_version
    execution_contract_id
    execution_contract_version
    trust_evaluation_id
    trust_evaluation_version
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
    idempotency_key
    parent_execution_id
    retry_of
    attempt_number
    result
    failure
    evidence
    provenance
}

The exact schema is defined by the relevant data model.

The architectural requirement is that the record preserve sufficient identity, versioning, and provenance to reconstruct the execution lifecycle.

⸻

10. Execution Identity

Every execution attempt must have a unique:

execution_id

The identifier represents the Noema execution attempt.

It must remain distinct from:

intent_id
action_id
plan_id
execution_contract_id
workflow_id
business_transaction_id
consumer_transaction_id

These identifiers refer to different objects or systems.

⸻

11. Intent Reference

The Execution Record must reference the Intent that produced the execution.

At minimum:

intent_id
intent_version

The historical Intent version must remain reconstructible.

A later modification to the Intent must not rewrite historical execution.

⸻

12. Plan Reference

Where execution was produced from an Execution Plan, the record should preserve:

plan_id
plan_version

This establishes:

Intent
   ↓
Plan
   ↓
Execution

The historical Plan version must remain reconstructible.

⸻

13. Action Reference

The Execution Record must identify the Action being executed.

Conceptually:

action_id
action_version

The Action must be represented through the canonical Action model rather than reconstructed from free-form model output.

⸻

14. Execution Contract Reference

The record must identify the governing Execution Contract:

execution_contract_id
execution_contract_version

This establishes the execution boundary under which the attempt occurred.

⸻

15. Trust Evaluation Reference

The Execution Record must identify the Trust evaluation that established execution eligibility.

Conceptually:

trust_evaluation_id
trust_evaluation_version

The record should not reduce this provenance to:

trusted = true

without preserving which Trust decision established that state.

The Execution Record records the authorization provenance; it does not independently establish authorization.

⸻

16. Capability Reference

The record should identify the Capability through which the Action was executed.

Conceptually:

capability_id
capability_version

This preserves the distinction:

Action
"What operation does the plan require?"
Capability
"What system capability performs it?"

Capability does not itself establish permission.

⸻

17. Consumer Identity

The Execution Consumer must be identifiable.

Conceptually:

consumer_id

The consumer may be:

* a payment service,
* CRM,
* banking system,
* enterprise API,
* internal execution service,
* workflow activity, or
* another authorized execution system.

The record should identify the system responsible for accepting, performing, and/or reporting the execution according to the applicable contract.

⸻

18. Execution State

Execution state represents the observed lifecycle of an execution attempt.

A conceptual state model is:

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

and, where explicitly permitted:

STARTED
    ↓
PARTIALLY_COMPLETED

The exact state machine may be specified separately.

Execution State must remain distinct from Trust State, Plan State, Workflow State, and Outcome State.

⸻

19. Accepted

ACCEPTED means the Execution Consumer has accepted the execution request or applicable Execution Contract according to the consumer’s semantics.

It does not mean that execution has completed.

Therefore:

ACCEPTED ≠ COMPLETED

⸻

20. Started

STARTED means that execution has actually begun according to the applicable execution semantics.

This distinction is important because a consumer may accept an execution request without immediately beginning the underlying operation.

⸻

21. Completed

COMPLETED means the Execution Consumer has reported successful completion according to the execution contract.

The record should retain the evidence supporting that report.

Completion of execution does not automatically establish authoritative business state.

Where required, business-state verification occurs through the Outcome or verification layer.

⸻

22. Failed

FAILED means that failure of the execution has been established according to the applicable execution semantics.

Failure should be structured.

Examples include:

CONSUMER_REJECTED
TIMEOUT
DEPENDENCY_FAILURE
PRECONDITION_FAILED
VALIDATION_FAILED
AUTHORIZATION_REJECTED
EXECUTION_ERROR

The taxonomy should remain extensible.

⸻

23. Partially Completed

Composite execution may produce component-level results.

For example:

Action A → COMPLETED
Action B → FAILED
Action C → COMPLETED

Where partial execution is permitted by the applicable Intent, Plan, and Contract, the Execution Record must preserve the component-level results.

It must not collapse them into a misleading binary result.

⸻

24. Unknown

An execution may produce a result whose final state cannot be established.

For example:

Request sent
    ↓
Consumer timeout
    ↓
No definitive response

Noema cannot safely infer either:

FAILED

or:

COMPLETED

without sufficient evidence.

The execution may therefore enter:

UNKNOWN

This is especially important for non-idempotent operations.

⸻

25. Unknown Is Not Failure

The distinction is fundamental:

FAILED

means failure has been established.

UNKNOWN

means the final execution state has not been established.

An UNKNOWN execution may require:

* reconciliation,
* authoritative status lookup,
* human intervention,
* retry analysis, or
* consumer-side recovery.

Unknown must never be silently converted into failure or success.

⸻

26. Execution Timestamps

The record should preserve observed execution timestamps, including where applicable:

requested_at
accepted_at
started_at
completed_at
rejected_at

Timestamps must represent observed lifecycle events rather than inferred events.

Not every execution will contain every timestamp.

⸻

27. Input References

Execution inputs must be traceable to the applicable Execution Contract and Action.

The record may contain or reference the canonical inputs.

Sensitive information should be referenced, protected, redacted, or otherwise minimized where possible.

The principle is:

Auditability must not require uncontrolled duplication of sensitive data.

⸻

28. Target References

Where applicable, the execution target should be identifiable.

Examples:

customer_123
account_456
ticket_789
payment_321

References should use canonical identifiers appropriate to the target system.

Noema must not invent authoritative business identifiers.

⸻

29. Result

The Execution Record may contain a structured execution result.

Conceptually:

result {
    status
    output_reference
    consumer_reference
    observed_at
}

The result describes what the Execution Consumer reported.

It does not automatically become authoritative business state.

⸻

30. Failure Information

Failures should be represented structurally rather than only as free-form text.

Conceptually:

failure {
    code
    category
    message
    retryable
    source
}

The machine-readable failure code should be canonical.

Human-readable messages may provide diagnostic context.

⸻

31. Execution Evidence

Execution results may be supported by evidence such as:

* consumer responses,
* external transaction references,
* API acknowledgements,
* enterprise events,
* status queries,
* reconciliation results, or
* other authoritative observations.

The Execution Record should reference relevant evidence sufficient to establish what was observed.

The evidence may remain owned by the external system.

⸻

32. Provenance

Every Execution Record must preserve provenance sufficient to reconstruct how execution occurred.

Relevant provenance includes:

* Intent and Intent version,
* Execution Plan and Plan version,
* Trust evaluation,
* Action and Action version,
* Execution Contract and Contract version,
* Capability and Capability version,
* Execution Consumer,
* workflow identity where applicable,
* execution events,
* timestamps,
* external references,
* result evidence, and
* relevant execution implementation versions.

The record must not depend on hidden model reasoning to establish execution provenance.

⸻

33. Execution Event History

An Execution Record may be represented through an append-only event history.

For example:

T0 execution.requested
T1 execution.accepted
T2 execution.started
T3 execution.completed

or:

T0 execution.requested
T1 execution.accepted
T2 execution.failed

The event history provides a reconstructible execution timeline.

⸻

34. Immutability

Historical execution facts must not be silently rewritten.

For example:

execution.started

must not later be rewritten to:

execution.accepted

without preserving the historical event.

Corrections must be represented through explicit events, amendments, or other auditable mechanisms.

⸻

35. Idempotency

Consequential execution must explicitly address idempotency.

Where applicable, the Execution Record should preserve:

idempotency_key

This allows Noema and execution consumers to distinguish a repeated request from a genuinely new execution.

Idempotency semantics belong to the Action, Contract, and Consumer boundary and must not be inferred solely from the existence of an Execution Record.

⸻

36. Retries

A failed or unknown execution may result in a retry.

Retries must not erase the original execution attempt.

For example:

Execution E1
    ↓
UNKNOWN
    ↓
Retry
    ↓
Execution E2

The relationship should remain explicit.

Possible relationships include:

parent_execution_id
retry_of
attempt_number

The exact representation is an implementation concern.

⸻

37. Execution Record and Trust

Trust answers:

May this Intent proceed toward execution?

The Execution Record answers:

What happened when execution was attempted?

Therefore:

Trust
   ↓
Execution eligibility
Execution Record
   ↓
Observed execution history

A failed execution does not, by itself, establish that the preceding Trust decision was incorrect.

⸻

38. Consumer-Side Validation

An Execution Consumer may perform final authoritative checks.

For example:

Noema:
Intent valid
Trust satisfied
Contract valid
Consumer:
Account no longer eligible

The consumer may reject the operation.

The Execution Record must preserve the rejection without rewriting the earlier validation or Trust history.

This preserves temporal causality between Noema’s decision and the later execution environment.

⸻

39. Execution Boundary

An Execution Record corresponds to an explicit crossing of the execution boundary.

Conceptually:

PLAN_READY
    ↓
CONTRACT_ACCEPTED
    ↓
EXECUTION
    ↓
Execution Record

The exact point at which the record is created may vary by implementation.

The transition itself must remain explicit and attributable.

⸻

40. No Execution Without an Execution Contract

Consequential execution must not originate from arbitrary model output.

The canonical path is:

Intent
   ↓
Trust
   ↓
Execution Plan
   ↓
Action
   ↓
Execution Contract
   ↓
Execution Consumer
   ↓
Execution Record

The Execution Record must identify the governing Contract.

⸻

41. External Transaction References

An external system may provide its own transaction identifier.

For example:

consumer_transaction_id
business_transaction_id

These identifiers should be retained where relevant.

They must remain distinct from:

execution_id

because Noema owns the execution record while the external system owns its business transaction.

⸻

42. Outcome Verification

Execution completion and business outcome verification are distinct concepts.

For example:

Execution:
API returned success
Verification:
Authoritative customer record reflects the requested change

For consequential Actions, Noema may require postcondition verification.

The Execution Record should therefore preserve the distinction between:

Observed execution result

and:

Verified business outcome

⸻

43. Execution Record and Outcome

The canonical relationship is:

Execution
   ↓
Observed Result
   ↓
Verification
   ↓
Outcome

The Execution Record captures execution and its observed results.

The Outcome model represents what ultimately resulted according to the applicable evidence and verification semantics.

Neither should silently replace the authoritative business system.

⸻

44. Composite Execution

A composite Intent may produce multiple Execution Records.

For example:

Intent I1
   │
   ├── Action A → Execution E1
   ├── Action B → Execution E2
   └── Action C → Execution E3

The parent-child relationship must remain explicit.

This permits Noema to reconstruct:

* aggregate execution state, and
* component-level execution state.

⸻

45. Atomicity

Atomicity must be explicitly defined by the Action and Execution Contract.

Noema must not infer atomicity merely because multiple operations appear related.

If an Action is atomic, the Execution Record must reflect its atomic execution semantics.

If it is not atomic, component-level execution results may be recorded independently.

⸻

46. Human Intervention

An execution may require human intervention because of:

* unknown execution state,
* external-system disagreement,
* reconciliation requirements,
* unexpected business state, or
* explicit policy requirements.

For example:

EXECUTING
    ↓
UNKNOWN
    ↓
HUMAN_INTERVENTION_REQUIRED

The intervention event must remain observable and attributable.

⸻

47. Auditability

Execution Records are a core component of Noema’s audit architecture.

An audit trail should be capable of establishing:

Actor
  ↓
Intent
  ↓
Resolved Intent
  ↓
Validation
  ↓
Trust Decision
  ↓
Execution Plan
  ↓
Action
  ↓
Execution Contract
  ↓
Execution Consumer
  ↓
Execution Events
  ↓
Observed Result
  ↓
Verification
  ↓
Outcome

The Execution Record is the canonical execution-layer link in this chain.

⸻

48. Security and Sensitive Data

Execution Records may contain sensitive information.

Implementations should therefore minimize unnecessary duplication of:

* credentials,
* authentication material,
* secrets,
* financial information,
* personal data, and
* protected business information.

References, hashes, protected storage, or redaction should be used where sufficient.

Security and data-governance requirements belong to the applicable security architecture and governance specifications.

⸻

49. Retention

Execution Records require explicit retention semantics.

Retention may depend upon:

* regulatory requirements,
* audit requirements,
* business requirements,
* data sensitivity,
* contractual requirements, and
* operational requirements.

Retention policy must preserve the provenance necessary to reconstruct consequential execution for the applicable retention period.

Exact retention periods are implementation and policy concerns.

⸻

50. Versioning

Execution Records must preserve the versions of objects that materially governed execution.

Where applicable:

intent_version
plan_version
action_version
execution_contract_version
capability_version
trust_evaluation_version
workflow_implementation_version

Historical execution must remain reconstructible even as Noema evolves.

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

Historical reconstruction must not depend on the current versions of mutable definitions.

⸻

52. Execution Record Lifecycle

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

and where explicitly permitted:

STARTED
    ↓
PARTIALLY_COMPLETED

The final state model may be more granular.

⸻

53. State Transition Principles

Execution state transitions must be:

* explicit,
* attributable,
* timestamped,
* based on observed execution events,
* auditable, and
* reconstructible.

A model interpretation must not silently overwrite an authoritative consumer event.

⸻

54. Execution Record and Durable Workflow

Where durable workflow orchestration is used:

Execution Plan
      ↓
Durable Workflow
      ↓
Activity
      ↓
Execution Consumer
      ↓
Execution Record

The Workflow provides durable orchestration.

The Execution Record provides the canonical semantic record of the execution attempt.

Workflow history and Execution Records may correlate, but they are not identical artifacts.

A workflow history does not replace the Noema Execution Record.

⸻

55. Unknown Execution and Reconciliation

When execution produces an unknown result:

Execution
    ↓
UNKNOWN
    ↓
Reconciliation
    ↓
Authoritative System
    ↓
Confirmed Result

Reconciliation must obtain sufficient evidence before changing the semantic execution or outcome state.

Absence of a response is not itself evidence of failure.

⸻

56. Execution Record Does Not Create Authority

The existence of an Execution Record does not establish that execution was authorized.

Likewise:

Execution Record exists

does not imply:

Trust = GRANTED

and:

Execution Record = COMPLETED

does not imply:

Business State = VERIFIED

Authority originates from the appropriate Trust and authorization mechanisms.

Business truth originates from the authoritative business system.

⸻

57. Canonical Example

Intent:
Transfer ₦500,000 to customer_123
Validation:
VALID
Trust:
READY
Plan:
P-123
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
Payment provider reports transaction completed
Execution State:
COMPLETED

The Execution Record connects the execution to the governing Intent, Plan, Trust decision, Action, Contract, Capability, and Consumer.

It does not become the authoritative source of payment-system state.

⸻

58. Failure Example

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

The failure records the execution result.

It does not rewrite the historical fact that the Intent was valid and trusted when execution began.

⸻

59. Unknown Outcome Example

Intent:
Transfer ₦5,000,000
Trust:
READY
Execution:
E-777
Consumer:
Banking Service
Request:
ACCEPTED
Response:
TIMEOUT
Execution State:
UNKNOWN

Noema must not infer:

FAILED

unless the authoritative system establishes failure.

A reconciliation process may therefore be required.

⸻

60. Execution Record Invariants

Invariant 1

Every Execution Record represents a specific execution attempt or explicitly defined execution lifecycle.

Invariant 2

Every consequential execution must be traceable to an Intent.

Invariant 3

Every consequential execution must be traceable to an applicable Execution Contract.

Invariant 4

Execution Records do not replace authoritative business state.

Invariant 5

Execution State is distinct from Trust State.

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

Partial execution must be explicit where permitted.

Invariant 12

Consumer-side validation may reject execution after Noema has established Trust.

Invariant 13

Execution success does not automatically establish authoritative business truth.

Invariant 14

Sensitive execution data must not be duplicated unnecessarily.

Invariant 15

Execution must remain attributable to the Plan, Contract, and Trust decision under which it was initiated.

Invariant 16

An Execution Record must not itself create authority.

Invariant 17

External transaction identifiers must remain distinct from Noema execution identifiers.

Invariant 18

Historical execution facts must not be silently rewritten.

⸻

61. Canonical Relationship

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
                 │ Execution    │
                 │    Plan      │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Contract   │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Consumer   │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │  Execution   │
                 │    Record    │
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

This preserves the Noema boundary between:

understanding
Trust
planning
execution
business truth

⸻

62. Canonical Mental Model

The Execution Record can be reduced to five questions:

1. What Intent caused this execution?
2. What Plan, Action, and Contract governed it?
3. Which Capability and Consumer performed or accepted it?
4. What happened during execution?
5. What evidence supports the observed result?

These questions define the minimum conceptual responsibility of the Execution Record.

⸻

63. Final Definition

The Execution Record is Noema’s structured, durable, and auditable representation of an execution attempt and its observed execution lifecycle.

It links execution to the governing:

* Intent,
* Intent version,
* Execution Plan,
* Action,
* Trust evaluation,
* Capability,
* Execution Contract,
* Execution Consumer,
* execution events, and
* evidence.

It records what was attempted and what execution reported.

It does not establish Intent meaning, create Trust, grant authority, or replace authoritative business state.

The central invariant is:

Noema records the authorized execution path and the observed execution history; it does not confuse execution history with authoritative business truth.

The canonical relationship is therefore:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Execution Plan
   ↓
Execution Contract
   ↓
Durable Workflow
   ↓
Execution Consumer
   ↓
Execution Record
   ↓
Outcome Verification
   ↓
Outcome

This establishes the Execution Record as the historical and auditable execution artifact between execution and outcome, without allowing it to become a substitute for Trust, Contracts, Workflow state, or authoritative enterprise state.