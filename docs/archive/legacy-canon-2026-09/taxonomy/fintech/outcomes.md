Outcomes

Status: Foundational
Version: 0.1
Domain: Taxonomy / Fintech
Canonical Path: taxonomy/fintech/outcomes.md

⸻

1. Definition

A Fintech Outcome is a canonical representation of the externally observable result produced by the fulfillment, non-fulfillment, or termination of a financial Intent.

An Outcome describes what happened.

It does not describe:

* what the Actor intended
* whether the Intent was trusted
* how the Action Graph was constructed
* which execution strategy was used
* whether an individual Action was authorized
* why a particular business decision was made

The canonical distinction is:

Intent
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Execution
  ↓
Fintech Outcome

Therefore:

Intent = what the Actor wants
Outcome = what actually happened

An Outcome must not be inferred merely because an Action was attempted.

⸻

2. Purpose

The Fintech Outcome taxonomy provides a canonical vocabulary for representing results across financial domains.

It allows Noema to distinguish outcomes such as:

* successfully completed financial operations
* rejected operations
* blocked operations
* partially completed operations
* pending operations
* cancelled operations
* expired operations
* failed operations
* unknown outcomes
* outcomes requiring reconciliation

The taxonomy exists so that financially consequential results are represented explicitly rather than collapsed into generic success or failure.

⸻

3. Outcome Boundary

The Outcome taxonomy sits downstream of execution.

Intent
   ↓
Trust
   ↓
Action Graph
   ↓
Action Contracts
   ↓
Execution
   ↓
External Financial Systems
   ↓
Observed Result
   ↓
Fintech Outcome

The Outcome layer records the result known to Noema.

It does not become the authoritative owner of external financial state.

For example:

Payment Provider
    ↓
payment = SETTLED
    ↓
Noema Outcome
    ↓
PAYMENT_SETTLED

The payment provider remains authoritative for the payment state.

⸻

4. Outcome vs Intent

An Intent expresses the desired objective.

An Outcome expresses the resulting state of fulfillment.

Example:

Intent:
Transfer ₦100,000 to Account B.
Outcome:
TRANSFER_SETTLED

These are separate semantic objects.

A successful Intent fulfillment does not rewrite the original Intent.

Likewise:

Intent:
Transfer ₦100,000.
Outcome:
TRANSFER_FAILED

does not mean that the Actor intended failure.

⸻

5. Outcome vs Execution State

Execution state describes what happened operationally to Actions.

Outcome describes the resulting fulfillment state of the relevant Intent or financial operation.

For example:

Action:
CREATE_TRANSFER
Execution:
COMPLETED
External State:
TRANSFER_PENDING
Outcome:
TRANSFER_PENDING

Therefore:

Action completed
        ≠
Financial operation completed

Execution success may only establish that an instruction was successfully submitted.

The resulting financial state may remain pending or unknown.

⸻

6. Outcome vs Trust

Trust establishes whether execution may proceed.

Outcome establishes what happened after or during execution.

Therefore:

Trust:
READY
Outcome:
TRANSFER_FAILED

is valid.

Similarly:

Trust:
BLOCKED
Outcome:
NOT_EXECUTED

may be valid.

A negative Outcome must not be interpreted as evidence that the original Trust decision was incorrect.

⸻

7. Outcome Authority

Noema must distinguish between:

1. an observed execution result
2. an authoritative external business state
3. a derived Noema Outcome

For example:

Payment Provider
    ↓
authoritative state = SETTLED
Noema
    ↓
observed evidence = settlement confirmed
Outcome
    ↓
PAYMENT_SETTLED

Noema should retain the evidence supporting the Outcome.

It should not claim ownership of financial state maintained by external systems.

⸻

8. Core Outcome Properties

A Fintech Outcome should be capable of representing:

Outcome {
    id
    intent_id
    operation
    status
    subject
    external_reference
    evidence
    provenance
    observed_at
    effective_at
    source
    version
}

The exact schema belongs to the canonical Outcome model.

⸻

9. Outcome Identity

Each Outcome should have an explicit identity.

Conceptually:

outcome_id

should distinguish one recorded Outcome from another.

An Outcome may also reference:

intent_id
action_id
execution_id
external_operation_id

where applicable.

These identifiers must not be conflated.

⸻

10. Outcome Status

The taxonomy should support distinct outcome states.

Core statuses include:

COMPLETED
PARTIALLY_COMPLETED
PENDING
FAILED
REJECTED
BLOCKED
CANCELLED
EXPIRED
UNKNOWN
NOT_EXECUTED

Additional domain-specific statuses may be introduced where necessary.

Status meanings must remain explicit.

⸻

11. COMPLETED

COMPLETED indicates that the relevant financial operation has reached its defined successful completion condition.

Example:

Intent:
Transfer funds.
Outcome:
TRANSFER_COMPLETED

Completion should be based on the applicable completion semantics.

A successfully submitted request is not necessarily a completed financial operation.

⸻

12. PARTIALLY_COMPLETED

PARTIALLY_COMPLETED indicates that some required components of the financial Intent were completed while others were not.

Example:

Intent:
Transfer balance and close account.
Outcome:
BALANCE_TRANSFER_COMPLETED
ACCOUNT_CLOSURE_FAILED

The aggregate Outcome may therefore be:

PARTIALLY_COMPLETED

Partial completion must remain explicit.

It must not be silently represented as success.

⸻

13. PENDING

PENDING indicates that the operation has been initiated or accepted but its final financial state has not yet been established.

Example:

TRANSFER_SUBMITTED
        ↓
TRANSFER_PENDING

Pending does not mean failed.

Pending does not mean completed.

Pending may require later observation or reconciliation.

⸻

14. FAILED

FAILED indicates that the relevant operation did not successfully complete according to the applicable execution semantics.

Example:

CREATE_TRANSFER
      ↓
provider_error
      ↓
TRANSFER_FAILED

Failure should be accompanied by structured failure information where available.

⸻

15. REJECTED

REJECTED indicates that an authoritative system or applicable decision mechanism explicitly declined the operation.

Example:

TRANSFER_REQUEST
      ↓
BANK
      ↓
REJECTED

Rejection should remain distinct from technical failure.

For example:

REJECTED

may mean the financial institution declined the transaction, whereas:

FAILED

may indicate that the operation could not complete because of a technical or execution failure.

⸻

16. BLOCKED

BLOCKED indicates that execution could not proceed because a required condition prevented continuation.

Examples include:

Required approval absent
Required authorization absent
Required capability unavailable
Required verification incomplete

A blocked operation is not necessarily failed.

It may become executable if the blocking condition is resolved.

⸻

17. CANCELLED

CANCELLED indicates that the relevant operation was explicitly terminated before its defined completion.

Cancellation may originate from:

* Actor action
* system policy
* expiration handling
* authorized administrative intervention
* external financial system

The source of cancellation should be retained.

⸻

18. EXPIRED

EXPIRED indicates that an operation or Intent could no longer proceed because its temporal validity ended.

Example:

Payment authorization
    ↓
valid_until = 18:00
    ↓
18:01
    ↓
EXPIRED

Expiration is distinct from failure and cancellation.

⸻

19. UNKNOWN

UNKNOWN indicates that Noema cannot establish the final state of the financial operation.

This is particularly important for financial Actions.

Example:

REQUEST_TRANSFER
      ↓
network timeout
      ↓
provider response unknown
      ↓
TRANSFER_UNKNOWN

Noema must not convert an uncertain external result into FAILED merely because the response was unavailable.

Likewise, it must not convert it into COMPLETED.

⸻

20. NOT_EXECUTED

NOT_EXECUTED indicates that the relevant financial operation did not cross the execution boundary.

Examples:

Trust = BLOCKED
Outcome = NOT_EXECUTED

or:

Intent cancelled before execution
Outcome = NOT_EXECUTED

This status distinguishes non-execution from execution failure.

⸻

21. Outcome Categories

Fintech Outcomes may be organized into several semantic categories.

Fulfillment Outcomes

COMPLETED
PARTIALLY_COMPLETED

Transitional Outcomes

PENDING
WAITING

Negative Execution Outcomes

FAILED
REJECTED
BLOCKED

Termination Outcomes

CANCELLED
EXPIRED
NOT_EXECUTED

Uncertainty Outcomes

UNKNOWN

The exact canonical enumeration should remain aligned with the broader Outcome taxonomy.

⸻

22. Payment Outcomes

Payment-related outcomes may include:

PAYMENT_CREATED
PAYMENT_SUBMITTED
PAYMENT_PENDING
PAYMENT_AUTHORIZED
PAYMENT_DECLINED
PAYMENT_FAILED
PAYMENT_SETTLED
PAYMENT_REVERSED
PAYMENT_CANCELLED
PAYMENT_UNKNOWN

These represent different stages and results.

They should not be collapsed into a single generic PAYMENT_SUCCESS state.

⸻

23. Transfer Outcomes

Transfer-related outcomes may include:

TRANSFER_CREATED
TRANSFER_SUBMITTED
TRANSFER_PENDING
TRANSFER_COMPLETED
TRANSFER_REJECTED
TRANSFER_FAILED
TRANSFER_CANCELLED
TRANSFER_REVERSED
TRANSFER_UNKNOWN

The exact available statuses depend on the authoritative financial system and applicable Action Contract.

⸻

24. Account Outcomes

Account-related operations may include:

ACCOUNT_CREATED
ACCOUNT_UPDATED
ACCOUNT_CLOSED
ACCOUNT_SUSPENDED
ACCOUNT_REACTIVATED
ACCOUNT_CLOSURE_PENDING
ACCOUNT_CLOSURE_FAILED
ACCOUNT_UPDATE_FAILED

The Outcome must represent the result established by the authoritative account system.

⸻

25. Card Outcomes

Card-related operations may include:

CARD_ISSUED
CARD_ACTIVATED
CARD_REPLACEMENT_REQUESTED
CARD_REPLACED
CARD_BLOCKED
CARD_UNBLOCKED
CARD_CANCELLED
CARD_EXPIRED
CARD_REPLACEMENT_FAILED

Where the external card system distinguishes additional states, those states may be represented through the applicable domain taxonomy.

⸻

26. Verification Outcomes

Financial verification operations may produce outcomes such as:

VERIFICATION_COMPLETED
VERIFICATION_FAILED
VERIFICATION_REJECTED
VERIFICATION_PENDING
VERIFICATION_EXPIRED
VERIFICATION_UNKNOWN

Verification completion does not itself imply authorization for a later financial Action.

⸻

27. Loan Outcomes

Loan-related operations may include:

APPLICATION_SUBMITTED
APPLICATION_PENDING
APPLICATION_APPROVED
APPLICATION_REJECTED
APPLICATION_WITHDRAWN
LOAN_DISBURSED
LOAN_DISBURSEMENT_FAILED
LOAN_REPAID

Approval is an Outcome of an applicable decision process.

It is not equivalent to execution authorization for every subsequent Action.

⸻

28. Investment Outcomes

Investment-related operations may include:

ORDER_CREATED
ORDER_SUBMITTED
ORDER_PENDING
ORDER_EXECUTED
ORDER_PARTIALLY_EXECUTED
ORDER_REJECTED
ORDER_CANCELLED
ORDER_EXPIRED
ORDER_UNKNOWN

For market-facing operations, execution and settlement may be separate outcomes.

Therefore:

ORDER_EXECUTED

does not necessarily mean:

SETTLEMENT_COMPLETED

⸻

29. Settlement Outcomes

Settlement should be represented independently where the financial domain requires it.

Examples:

SETTLEMENT_PENDING
SETTLEMENT_COMPLETED
SETTLEMENT_FAILED
SETTLEMENT_REVERSED
SETTLEMENT_UNKNOWN

Settlement status should originate from the authoritative settlement mechanism where applicable.

⸻

30. Reversal Outcomes

A financial operation may initially complete and later be reversed.

Example:

TRANSFER_COMPLETED
       ↓
REVERSAL
       ↓
TRANSFER_REVERSED

Reversal does not erase the historical fact that the earlier operation reached completion.

The Outcome history should preserve the transition.

⸻

31. Outcome Transitions

Fintech Outcomes may evolve over time.

Example:

PENDING
   ↓
COMPLETED

or:

PENDING
   ↓
FAILED

or:

PENDING
   ↓
UNKNOWN
   ↓
RECONCILED
   ↓
COMPLETED

Outcome transitions must be explicit and auditable.

⸻

32. Outcome History

Noema should preserve the history of material Outcome transitions.

Example:

Outcome Event 1:
TRANSFER_PENDING
Outcome Event 2:
TRANSFER_COMPLETED

The later Outcome must not silently overwrite the historical record.

This supports:

* auditability
* reconciliation
* incident investigation
* financial traceability
* operational debugging

⸻

33. External References

Financial Outcomes should retain authoritative external references where available.

Examples:

provider_transaction_id
bank_reference
payment_reference
settlement_reference
account_reference
card_reference

External references enable reconciliation with the system that owns the financial state.

⸻

34. Evidence

An Outcome should identify the evidence supporting its status where practical.

Evidence may include:

* provider response
* transaction confirmation
* settlement event
* webhook
* ledger record
* authoritative API response
* reconciliation result
* execution result

The evidence source should be retained as provenance.

⸻

35. Provenance

Outcome provenance should identify:

source
source_system
source_event
observed_at
effective_at
external_reference
execution_reference

This allows Noema to distinguish:

Observed

from:

Inferred

and:

Expected

from:

Confirmed

⸻

36. Expected vs Observed Outcome

An expected postcondition is not the same as an observed Outcome.

Example:

Expected:
payment.status = SETTLED

does not establish:

PAYMENT_SETTLED

until authoritative evidence confirms the state.

Therefore:

Expected Outcome
      ≠
Observed Outcome

⸻

37. Outcome Confirmation

Where an operation has consequential financial effects, Noema should distinguish between:

REQUEST_ACCEPTED

and:

FINANCIAL_EFFECT_CONFIRMED

For example:

TRANSFER_REQUEST_ACCEPTED

may only mean that the bank accepted the instruction.

The final transfer state may remain:

TRANSFER_PENDING

until settlement or completion is confirmed.

⸻

38. Unknown and Reconciliation

Unknown financial outcomes should enter an explicit reconciliation path where applicable.

Conceptually:

UNKNOWN
   ↓
RECONCILIATION
   ↓
AUTHORITATIVE RESULT
   ├── COMPLETED
   ├── FAILED
   ├── REJECTED
   └── NOT_FOUND / UNKNOWN

Noema must not resolve uncertainty through assumption.

⸻

39. Reconciliation

Reconciliation compares Noema’s recorded execution state with authoritative external financial state.

Example:

Noema:
TRANSFER_UNKNOWN
Bank:
transaction = COMPLETED
Reconciliation:
      ↓
TRANSFER_COMPLETED

Reconciliation should preserve the evidence supporting the correction.

⸻

40. Duplicate Outcomes

Repeated provider events may refer to the same financial operation.

Noema should use stable identifiers and idempotency semantics to prevent duplicate financial Outcomes from being interpreted as separate operations.

For example:

provider_event_123
provider_event_123
provider_event_123

should not become three independent financial completions.

⸻

41. Outcome Correlation

Outcomes should be correlatable across the execution lifecycle.

Conceptually:

intent_id
   ↓
graph_id
   ↓
action_id
   ↓
execution_id
   ↓
external_operation_id
   ↓
outcome_id

This permits reconstruction of the complete causal path.

⸻

42. Composite Financial Outcomes

A composite Intent may produce multiple Outcomes.

Example:

Intent:
Close account and transfer remaining balance.
Outcomes:
ACCOUNT_CLOSED
TRANSFER_COMPLETED

The aggregate result must preserve the individual component Outcomes.

Noema must not collapse materially different financial results into one undifferentiated status.

⸻

43. Aggregate Outcome

Where an Intent has multiple components, an aggregate Outcome may be derived from component Outcomes.

Example:

Component A = COMPLETED
Component B = FAILED
Aggregate:
PARTIALLY_COMPLETED

The aggregation rules must be deterministic.

They must not conceal component-level failure.

⸻

44. Atomic Financial Intent

If the Intent or Action Contract requires atomic execution, an aggregate Outcome must respect that semantic requirement.

For example:

A = COMPLETED
B = FAILED

must not be represented as:

COMPLETED

if the operation was required to succeed atomically.

The appropriate result may instead require:

FAILED

or:

UNKNOWN

depending on the actual financial state.

⸻

45. Outcome and Compensation

Compensation does not erase the original Outcome.

Example:

TRANSFER_COMPLETED
      ↓
DOWNSTREAM_FAILURE
      ↓
COMPENSATION_EXECUTED

The history should preserve:

Original:
TRANSFER_COMPLETED
Compensation:
TRANSFER_REVERSED

Compensation is a subsequent operation, not retroactive deletion of history.

⸻

46. Outcome and Failure Recovery

Failure recovery may change the eventual Outcome.

Example:

PAYMENT_FAILED
      ↓
RETRY
      ↓
PAYMENT_COMPLETED

The failure event remains part of execution history.

The final aggregate Outcome may be:

COMPLETED

provided the defined completion condition was ultimately satisfied.

⸻

47. Outcome and Idempotency

Idempotency must prevent retries from producing unintended duplicate financial operations.

Example:

CREATE_PAYMENT
      ↓
timeout
      ↓
retry

The system must determine whether the original payment was already created.

The resulting Outcome must be based on the authoritative financial state, not merely on the number of execution attempts.

⸻

48. Outcome and External State

External financial systems remain authoritative.

For example:

Noema:
PAYMENT_PENDING
Provider:
PAYMENT_SETTLED

Noema should reconcile its Outcome representation with the authoritative provider state.

Noema must not override external state simply because its local execution state differs.

⸻

49. Temporal Semantics

An Outcome may contain multiple relevant times:

requested_at
executed_at
observed_at
effective_at
settled_at
recorded_at

These timestamps should not be treated as interchangeable.

For financial operations, the distinction between when an operation occurred and when Noema learned that it occurred can be material.

⸻

50. Outcome Freshness

An Outcome may become stale as external financial state changes.

For example:

PAYMENT_PENDING

may cease to represent current state after settlement.

Noema should preserve the historical Outcome while establishing the latest known Outcome separately.

⸻

51. Current Outcome vs Outcome History

The system should distinguish:

Current Outcome

from:

Outcome History

Example:

History:
PENDING
   ↓
AUTHORIZED
   ↓
SETTLED
Current:
SETTLED

Historical states remain reconstructible.

⸻

52. Outcome Versioning

Material Outcome changes should be versioned or represented through immutable Outcome events.

Conceptually:

Outcome v1 = PENDING
Outcome v2 = SETTLED

The exact event-sourcing or versioning mechanism belongs to the broader architecture.

The semantic requirement is reconstructibility.

⸻

53. Outcome Errors

Outcome errors should use machine-readable codes.

Examples:

PROVIDER_REJECTED
INSUFFICIENT_FUNDS
ACCOUNT_BLOCKED
INVALID_DESTINATION
AUTHORIZATION_FAILED
TIMEOUT
NETWORK_FAILURE
SETTLEMENT_FAILURE
DUPLICATE_REQUEST
UNKNOWN_PROVIDER_STATE
RECONCILIATION_REQUIRED

The exact taxonomy may evolve by financial domain.

Human-readable explanations may accompany these codes.

⸻

54. Outcome Classification

An Outcome should distinguish at least:

STATUS
CAUSE
EVIDENCE
SOURCE
TEMPORAL_STATE

For example:

status = REJECTED
cause = INSUFFICIENT_FUNDS
source = BANK
evidence = provider_response_123

This is preferable to encoding all semantics in a single opaque string.

⸻

55. Outcome Does Not Explain Intent

The Outcome taxonomy must not redefine the Intent.

Example:

Intent:
Send ₦100,000 to John.
Outcome:
TRANSFER_REJECTED

The Outcome does not determine whether:

* John was the correct recipient
* the amount was what the Actor intended
* the Intent was properly resolved

Those questions belong to earlier lifecycle stages.

⸻

56. Outcome Does Not Grant Authority

A prior successful Outcome does not authorize a future operation.

Example:

TRANSFER_COMPLETED

does not imply:

Actor may perform another transfer.

Authorization remains governed by Trust and applicable Action Contracts.

⸻

57. Outcome Does Not Establish Trust

An Outcome must not be used as a substitute for Trust.

For example:

Previous transaction:
COMPLETED

does not imply:

Current transaction:
TRUSTED

Each consequential Intent must pass through the applicable Trust lifecycle.

⸻

58. Outcome and Policy

Policies may define how Outcomes are interpreted operationally.

For example:

TRANSFER_UNKNOWN
      ↓
RECONCILIATION_REQUIRED

A policy may determine that execution cannot continue until reconciliation resolves the uncertainty.

The policy governs downstream behavior.

The Outcome records the observed state.

⸻

59. Outcome and Human Intervention

Some Outcomes may require human intervention.

Example:

TRANSFER_UNKNOWN
      ↓
HUMAN_REVIEW_REQUIRED

Human review is not itself equivalent to a financial Outcome.

The eventual Outcome must still be established from authoritative evidence.

⸻

60. Outcome and Clarification

Clarification normally belongs to Intent resolution rather than financial execution.

Therefore:

Intent
  ↓
Clarification Required

is not normally a financial Outcome.

However, if clarification occurs after an operation has already entered an external financial process, the relevant financial Outcome must be represented separately.

⸻

61. Outcome and Cancellation

Cancellation must distinguish:

CANCEL_REQUESTED

from:

CANCEL_CONFIRMED

A cancellation request does not prove that the financial operation was cancelled.

Example:

PAYMENT_CANCEL_REQUESTED
      ↓
provider processing
      ↓
PAYMENT_CANCELLED

The confirmed Outcome should be based on authoritative evidence.

⸻

62. Outcome and Reversal

Reversal similarly requires authoritative confirmation.

REVERSAL_REQUESTED
      ↓
REVERSAL_PENDING
      ↓
REVERSAL_COMPLETED

The original transaction Outcome remains historically visible.

⸻

63. Outcome and Settlement

For financial operations where settlement is distinct from instruction execution:

Instruction
    ↓
Accepted
    ↓
Executed
    ↓
Settled

Noema should not collapse these stages unless the authoritative financial system defines them as one semantic state.

⸻

64. Outcome Determinism

Outcome classification should be deterministic from:

Execution Result
External Evidence
Action Contract
Outcome Rules
Authoritative State

The same relevant evidence and rule versions should produce the same canonical classification.

An LLM must not arbitrarily decide whether:

timeout = FAILED

when the external state is actually unknown.

⸻

65. Model-Generated Outcome Classification

Models may assist in interpreting unstructured provider messages.

For example:

Provider message
      ↓
LLM classification proposal
      ↓
Candidate Outcome
      ↓
Deterministic Outcome Validation
      ↓
Canonical Outcome

The model must not independently establish a financially consequential Outcome when authoritative structured evidence is available or required.

⸻

66. Outcome Provenance and Model Provenance

If a model assists with Outcome classification, Noema may retain:

generation_source
model_id
model_version
generation_timestamp

But model provenance does not establish financial authority.

The canonical authority remains the applicable external evidence, contract semantics, and deterministic classification rules.

⸻

67. Outcome Observability

Noema should make it possible to inspect:

* current Outcome
* Outcome history
* external reference
* source system
* evidence
* timestamps
* execution reference
* reconciliation status
* failure cause
* compensation
* retries
* human intervention

This supports financial operational visibility.

⸻

68. Outcome Auditability

A financially consequential Outcome should be reconstructible.

At minimum, Noema should be able to establish:

1. the originating Intent
2. the relevant Action Graph
3. the Action executed
4. the execution result
5. the external operation reference
6. the evidence received
7. the Outcome assigned
8. subsequent Outcome transitions
9. reconciliation activity
10. final known state

⸻

69. Outcome Security

Outcome records may contain financially sensitive information.

Therefore Outcome handling must preserve applicable:

* access controls
* data minimization
* confidentiality
* integrity
* auditability
* retention requirements

Outcome observability must not become unrestricted access to financial data.

⸻

70. Outcome Integrity

Outcome records must be protected against unauthorized mutation.

Historical financial Outcomes should be append-only or otherwise tamper-evident where required.

A later correction should create an explicit correction or subsequent Outcome event rather than silently rewriting history.

⸻

71. Outcome Retention

Retention requirements depend on:

* financial domain
* jurisdiction
* applicable regulation
* contractual obligations
* operational requirements

The taxonomy does not independently establish retention periods.

Those requirements belong to the applicable compliance and data-governance specifications.

⸻

72. Outcome Reconciliation Loop

A canonical reconciliation loop may be represented as:

Execution
    ↓
Observed Result
    ↓
Outcome
    ↓
External State Check
    ↓
Reconciliation
    ↓
Updated Outcome

This is particularly important for:

* payments
* transfers
* settlements
* reversals
* withdrawals
* deposits
* investment orders

where asynchronous external state changes are common.

⸻

73. Outcome Lifecycle

A conceptual lifecycle is:

NOT_EXECUTED
      ↓
SUBMITTED
      ↓
PENDING
      ↓
COMPLETED

Alternative paths may include:

PENDING
   ↓
FAILED

or:

PENDING
   ↓
REJECTED

or:

PENDING
   ↓
UNKNOWN
   ↓
RECONCILED
   ↓
COMPLETED

The permitted transitions must be defined by the relevant financial operation.

⸻

74. Invalid Outcome Transitions

The system must not permit arbitrary Outcome transitions.

For example:

COMPLETED
   ↓
PENDING

should not occur without explicit semantics explaining why a previously completed operation has entered a new state.

Similarly:

FAILED
   ↓
COMPLETED

should be represented as a subsequent execution attempt, reconciliation, or other explicitly defined transition rather than silently changing history.

⸻

75. Outcome Aggregation

Aggregate Outcomes must preserve component-level semantics.

Example:

Transfer:
COMPLETED
Notification:
FAILED

The financial transfer may still be:

TRANSFER_COMPLETED

while the overall composite Intent may be:

PARTIALLY_COMPLETED

Noema must avoid allowing an unrelated downstream failure to erase a confirmed financial result.

⸻

76. Outcome and Notifications

Notifications are generally operational Actions rather than financial state.

Therefore:

TRANSFER_COMPLETED
SEND_NOTIFICATION_FAILED

should remain distinct.

The failed notification does not imply that the transfer failed.

⸻

77. Outcome and Ledger State

Where a ledger or accounting system is authoritative, its state should be treated as the relevant source for ledger outcomes.

For example:

Ledger:
entry posted
Outcome:
LEDGER_ENTRY_POSTED

Noema should retain the ledger reference rather than treating its own internal state as the authoritative accounting record.

⸻

78. Outcome and Balance

A balance shown by Noema should not be treated as authoritative merely because an Outcome exists.

For example:

TRANSFER_COMPLETED

does not by itself establish the current account balance.

Current balance remains an external financial state maintained by the authoritative financial system.

⸻

79. Outcome and Financial Finality

Not every successful execution is financially final.

For example:

PAYMENT_AUTHORIZED

may later become:

PAYMENT_SETTLED

or:

PAYMENT_REVERSED

The taxonomy must preserve these distinctions.

⸻

80. Outcome Invariants

Invariant 1

An Outcome represents what happened, not what the Actor intended.

Invariant 2

Execution success does not automatically imply financial completion.

Invariant 3

Unknown external state must remain unknown until authoritative evidence establishes the result.

Invariant 4

Rejected, failed, blocked, cancelled, expired, and not-executed states must remain semantically distinct.

Invariant 5

Partial completion must not be represented as unconditional success.

Invariant 6

Outcome history must remain reconstructible.

Invariant 7

Noema must not claim ownership of external financial state.

Invariant 8

Authoritative external references should be retained where available.

Invariant 9

Expected postconditions must not be represented as confirmed Outcomes without appropriate evidence.

Invariant 10

Retries must not create duplicate financial Outcomes or duplicate financial operations.

Invariant 11

Compensation does not erase the original Outcome.

Invariant 12

Outcome classification must be deterministic where applicable rules and evidence are deterministic.

Invariant 13

Outcome status must not be used as a substitute for Trust.

Invariant 14

A prior Outcome does not authorize future financial operations.

Invariant 15

Financially consequential Outcome changes must be auditable.

Invariant 16

Reconciliation must not silently rewrite historical Outcome records.

⸻

81. Canonical Fintech Outcome Model

The conceptual model is:

                 FINTECH INTENT
                       │
                       ▼
                 ACTION GRAPH
                       │
                       ▼
                   EXECUTION
                       │
                       ▼
              EXTERNAL FINANCIAL SYSTEM
                       │
                       ▼
                OBSERVED EVIDENCE
                       │
                       ▼
                FINTECH OUTCOME
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        CURRENT STATE       OUTCOME HISTORY
             │                   │
             └─────────┬─────────┘
                       ▼
                 RECONCILIATION

The core semantic distinction is:

Intent
    =
desired financial objective
Execution
    =
operations performed
Outcome
    =
financial result established from execution and evidence

⸻

82. Canonical Outcome Questions

Every Fintech Outcome should answer, where applicable:

1. What financial operation produced this Outcome?
2. What happened?
3. What is the current status?
4. What evidence establishes that status?
5. Which system is authoritative for the underlying state?
6. When did the operation occur?
7. When did Noema observe the result?
8. Can the result still change?
9. Does reconciliation remain necessary?
10. What prior Outcomes led to the current state?

⸻

83. Relationship to the Fintech Intent Taxonomy

The Intent taxonomy describes the financial objectives that Actors may express.

The Outcome taxonomy describes the corresponding results.

Conceptually:

Intent
        ↓
Financial Objective
        ↓
Action Graph
        ↓
Execution
        ↓
Outcome

Examples:

TRANSFER_FUNDS
        ↓
TRANSFER_COMPLETED
PAY_BILL
        ↓
PAYMENT_SETTLED
REPLACE_CARD
        ↓
CARD_REPLACED
CLOSE_ACCOUNT
        ↓
ACCOUNT_CLOSED

The relationship is not necessarily one-to-one.

One Intent may produce:

* multiple Actions
* multiple intermediate Outcomes
* multiple component Outcomes
* one aggregate Outcome

⸻

84. Fintech Outcome Taxonomy Principle

The taxonomy should favor semantic precision over generic status labels.

For example, these states should not be collapsed:

REQUEST_ACCEPTED
PAYMENT_AUTHORIZED
PAYMENT_SETTLED
PAYMENT_REVERSED

Each represents a materially different financial condition.

Likewise:

FAILED
REJECTED
BLOCKED
UNKNOWN
CANCELLED

must remain distinguishable.

⸻

85. Final Definition

A Fintech Outcome is Noema’s canonical representation of the externally observable and appropriately evidenced result of a financial operation associated with an Intent.

Its central invariant is:

Noema must represent what actually happened in the financial operation without confusing execution success, expected state, Trust eligibility, or inferred state with confirmed financial outcome.

The canonical relationship is:

Financial Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contract
      ↓
Execution
      ↓
External Financial State
      ↓
Evidence
      ↓
Fintech Outcome
      ↓
Reconciliation
      ↓
Final Known Outcome

And the fundamental boundary remains:

Intent
=
what the Actor wants
Outcome
=
what Noema can establish happened