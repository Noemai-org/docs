Outcome

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/outcome.md

⸻

1. Definition

An Outcome is the observable result produced by an Action, Execution, or domain process, evaluated in relation to the Intent that initiated it.

Outcome answers:

What actually happened, and did it satisfy what was intended?

An Outcome is therefore distinct from:

* Intent
* Action
* Execution
* Execution Result
* System State

The fundamental relationship is:

Intent
   ↓
Action
   ↓
Execution
   ↓
Observed Outcome
   ↓
Outcome Evaluation
   ↓
Intent Satisfied / Unsatisfied

⸻

2. Outcome Is the End of the Semantic Loop

Noema should not treat execution as the end of the workflow.

The complete semantic lifecycle is:

Actor
  ↓
Intent
  ↓
Resolution
  ↓
Trust
  ↓
Action
  ↓
Execution
  ↓
Outcome
  ↓
Verification
  ↓
Intent Satisfaction

This distinction is foundational.

Noema does not merely determine what should happen. It must be capable of determining what actually happened.

⸻

3. Outcome Is Not Intent

Intent describes the desired objective.

Outcome describes the observed result.

Intent:
Transfer $500 to Alice.
Outcome:
$500 transferred to Alice.

The two may correspond, but they are not the same object.

Intent ≠ Outcome

⸻

4. Outcome Is Not Action

An Action describes an operation.

Action:
TransferFunds

An Outcome describes the result:

Outcome:
Transfer completed.
Transaction ID = tx_123

The same Action may produce different Outcomes.

TransferFunds
   ├── Success
   ├── InsufficientFunds
   ├── AuthorizationDenied
   ├── Timeout
   └── ExternalSystemFailure

⸻

5. Outcome Is Not Execution Result

A technical Execution Result describes what the invoked system returned.

Example:

HTTP 200
{
  "transaction_id": "tx_123"
}

That is not necessarily the complete business Outcome.

The business Outcome may require further verification:

Execution Result
      ↓
Transaction Created
      ↓
Funds Actually Moved
      ↓
Outcome Verified

Therefore:

Execution Result ≠ Outcome

⸻

6. Outcome Is Not System State

System State describes a condition.

Outcome describes what resulted from an Action or process.

Example:

State:
Card = active
Outcome:
Card renewal completed successfully.

The resulting State may be evidence for the Outcome, but they are not equivalent.

⸻

7. Outcome Structure

A canonical Outcome conceptually contains:

Outcome
├── id
├── action
├── intent
├── status
├── result
├── affected entities
├── state changes
├── evidence
├── provenance
├── timestamps
└── satisfaction

The actual serialization belongs to the schema layer.

⸻

8. Outcome Identity

Every material Outcome should have an identity.

Example:

outcome_123

This allows Noema to reference the Outcome independently of:

* the Intent
* the Action
* the Execution
* the external system

⸻

9. Outcome Status

An Outcome should have an explicit status.

A foundational status model is:

PENDING
SUCCEEDED
PARTIALLY_SUCCEEDED
FAILED
REJECTED
CANCELLED
UNKNOWN

Additional domain-specific statuses may exist.

The status vocabulary must remain extensible without changing the meaning of the core states.

⸻

10. SUCCEEDED

SUCCEEDED means the Action produced the expected operational result and the relevant Outcome has been sufficiently established.

Example:

Action:
RenewCard
Outcome:
Card renewed successfully.

⸻

11. PARTIALLY_SUCCEEDED

PARTIALLY_SUCCEEDED means some intended effects occurred while one or more intended effects did not.

Example:

Intent:
Onboard Employee
Outcomes:
✓ Employee created
✓ Email provisioned
✗ Permissions failed

The overall Outcome should not be represented as fully successful.

⸻

12. FAILED

FAILED means the intended Action did not successfully produce its expected operational result.

Examples:

Insufficient funds
External service unavailable
Validation failure
Execution timeout

⸻

13. REJECTED

REJECTED means the Action was explicitly prevented from proceeding.

Example:

Intent:
Refund $50,000
Outcome:
Rejected because Actor lacks required authority.

This differs from an execution failure because the Action may never have been attempted.

⸻

14. CANCELLED

CANCELLED means execution or an ongoing process was intentionally stopped.

Example:

Intent:
Generate report
Outcome:
Cancelled by Actor before completion.

⸻

15. UNKNOWN

UNKNOWN means Noema cannot establish the actual Outcome with sufficient confidence.

Example:

Action:
Transfer $5,000
Execution:
Timeout
Bank state:
Unknown

Noema must not convert this into:

FAILED

or:

SUCCEEDED

without evidence.

This is particularly important for distributed systems.

⸻

16. Pending Outcome

An Action may have been initiated without its final Outcome being available.

Action:
TransferFunds
Outcome:
PENDING

This may occur with:

* asynchronous processing
* eventual consistency
* external approval
* long-running jobs
* queued Actions

The Outcome can later transition to a terminal state.

⸻

17. Expected Outcome

An Expected Outcome describes what should happen if the Intent is successfully fulfilled.

Example:

Intent:
Renew Card
Expected Outcome:
Card status becomes active with a new expiry date.

Expected Outcome is part of the semantic contract.

⸻

18. Observed Outcome

An Observed Outcome describes what Noema or an authoritative source actually observes.

Example:

Observed Outcome:
Card status = active
expiry = 2030-08

The distinction is:

Expected Outcome
        ↓
     Compare
        ↑
Observed Outcome

⸻

19. Outcome Verification

Outcome Verification determines whether the observed result corresponds to the expected result.

Expected Outcome
       +
Observed Evidence
       ↓
Outcome Verification
       ↓
Satisfied / Unsatisfied / Unknown

Verification may be:

* immediate
* asynchronous
* event-driven
* polling-based
* source-confirmed

⸻

20. Intent Satisfaction

Intent satisfaction answers:

Did the Outcome actually fulfill the Actor’s Intent?

Example:

Intent:
Transfer $500 to Alice.
Observed Outcome:
$500 transferred to Alice.
Result:
SATISFIED

But:

Intent:
Transfer $500 to Alice.
Observed Outcome:
$500 transferred to Bob.
Result:
UNSATISFIED

Even though the underlying transfer Action succeeded technically.

⸻

21. Execution Success vs Intent Satisfaction

This is one of Noema’s critical distinctions.

Execution Success
        ≠
Intent Satisfaction

Example:

Action:
POST /transfer
HTTP Response:
200 OK

The execution succeeded technically.

But if the wrong account received the funds:

Intent:
UNSATISFIED

Therefore Noema should evaluate both:

Technical Success
        +
Semantic Satisfaction

⸻

22. Satisfaction Status

A foundational satisfaction vocabulary is:

SATISFIED
PARTIALLY_SATISFIED
UNSATISFIED
UNKNOWN

⸻

23. SATISFIED

The observed Outcome sufficiently fulfills the Intent.

Intent:
Renew Card
Outcome:
Card successfully renewed.
Satisfaction:
SATISFIED

⸻

24. PARTIALLY_SATISFIED

Only part of the Intent was fulfilled.

Example:

Intent:
Book flights for two people.
Outcome:
One passenger successfully booked.
Second booking failed.
Satisfaction:
PARTIALLY_SATISFIED

⸻

25. UNSATISFIED

The Outcome does not fulfill the Intent.

Example:

Intent:
Cancel subscription.
Outcome:
Subscription remains active.
Satisfaction:
UNSATISFIED

⸻

26. UNKNOWN Satisfaction

Noema cannot establish whether the Intent was satisfied.

Example:

Intent:
Transfer $5,000.
Execution:
Timeout.
Bank:
No confirmation available.
Satisfaction:
UNKNOWN

Noema must preserve the uncertainty.

⸻

27. Outcome Evidence

An Outcome should be supported by Evidence where material.

Example:

Outcome:
Payment refunded.
Evidence:
Payment provider transaction record.

Evidence may come from:

* external APIs
* databases
* events
* receipts
* signed responses
* system state
* human confirmation

⸻

28. Outcome Provenance

Outcome Provenance describes where the Outcome information came from.

Example:

Outcome:
Payment completed
Source:
Payment Provider
Observed At:
2026-08-23T09:32:00Z
Source Reference:
txn_123

Provenance is essential for auditability.

⸻

29. Outcome Timestamp

An Outcome may contain multiple relevant timestamps.

requested_at
started_at
completed_at
observed_at
verified_at

These timestamps must not be collapsed when their semantics differ.

⸻

30. Outcome Duration

Where relevant, Noema may record the duration between:

Action Started
        ↓
Action Completed

This supports:

* SLA evaluation
* latency analysis
* workflow monitoring
* operational diagnostics

Duration is metadata about the Outcome, not the Outcome itself.

⸻

31. State Changes

An Outcome may produce State changes.

Example:

Before:
Card.status = expired
Action:
RenewCard
After:
Card.status = active

The Outcome may include:

State Changes:
status: expired → active
expiry: 2026-08 → 2030-08

However:

State Change and Outcome must remain distinct concepts.

⸻

32. Affected Entities

An Outcome should identify the Entities affected by the Action where possible.

Example:

Outcome:
Payment refunded
Affected Entities:
Payment: payment_123
Customer: customer_456
Account: account_789

⸻

33. External Outcomes

External systems may produce outcomes that Noema consumes.

Example:

Noema
  ↓
Payment Provider
  ↓
Payment Outcome
  ↓
Noema

Noema should distinguish:

External System Outcome

from:

Noema's interpretation of that Outcome

⸻

34. Outcome Normalization

Different systems may express equivalent outcomes differently.

Example:

HTTP 200
status = "success"
Provider B:
status = "completed"
Provider C:
result = "OK"

Noema may normalize these into:

SUCCEEDED

while retaining the original source representation and provenance.

⸻

35. Outcome Conflicts

Multiple sources may disagree.

Example:

Payment Provider:
Payment = completed
Internal Database:
Payment = pending

Noema must not silently select one.

The conflict should be represented:

Outcome:
UNKNOWN
Evidence:
CONFLICTING

until the conflict can be resolved.

⸻

36. Outcome Freshness

An Outcome may become stale.

Example:

10:00
Account status = active
10:30
Account status = suspended

A previous Outcome remains historically valid but may no longer represent current State.

Therefore:

Historical Outcome
        ≠
Current State

⸻

37. Outcome Finality

Not every Outcome is immediately final.

Examples:

Payment:
PENDING
Transfer:
PROCESSING
Approval:
AWAITING_REVIEW

Noema must distinguish:

Interim Outcome

from:

Final Outcome

⸻

38. Outcome Lifecycle

A conceptual lifecycle is:

PENDING
   ↓
OBSERVED
   ↓
VERIFIED
   ↓
FINAL

Failure paths may include:

PENDING
   ↓
FAILED

or:

PENDING
   ↓
UNKNOWN

The exact lifecycle should be defined separately from the ontology.

⸻

39. Outcome Correlation

An Outcome must be traceable to the Action that produced it.

Intent
   │
   ▼
Action
   │
   └── action_id
          │
          ▼
       Execution
          │
          └── execution_id
                 │
                 ▼
              Outcome
                 │
                 └── outcome_id

This enables end-to-end traceability.

⸻

40. Outcome and Intent Correlation

The Outcome should also remain associated with the originating Intent.

Intent ID:
intent_123
Action ID:
action_456
Outcome ID:
outcome_789

This enables:

Intent
  ↓
Actions
  ↓
Outcomes

and allows Noema to determine whether the original objective was satisfied.

⸻

41. Multiple Outcomes

A single Intent may produce multiple Outcomes.

Example:

Intent:
Onboard Employee
Outcomes:
1. Employee created
2. Email account created
3. Permissions assigned
4. Welcome email sent

Noema may therefore evaluate:

Composite Intent Satisfaction

from multiple Outcomes.

⸻

42. Composite Outcome

Multiple Actions may collectively produce a Composite Outcome.

Intent
   ↓
Action A ──► Outcome A
   ↓
Action B ──► Outcome B
   ↓
Action C ──► Outcome C
              │
              ▼
       Composite Outcome

The Composite Outcome describes the aggregate result.

⸻

43. Partial Failure

Composite operations require explicit partial failure semantics.

Example:

Action A ✓
Action B ✓
Action C ✗
Action D not attempted

Overall:

Outcome:
PARTIALLY_SUCCEEDED

Noema must not represent this as full success.

⸻

44. Outcome Dependencies

Some Outcomes depend on previous Outcomes.

Example:

Create Account
      ↓
Outcome: Account Created
      ↓
Fund Account
      ↓
Outcome: Funding Completed

If the first Outcome fails, the second Action may never execute.

⸻

45. Outcome Compensation

A failed multi-step process may require compensating Actions.

Example:

Create Resource ✓
Charge Customer ✓
Provision Service ✗

A compensation Action may be:

Refund Customer

The compensation Outcome must remain separate from the original Outcome.

Original Outcome
      ↓
Failure
      ↓
Compensation Action
      ↓
Compensation Outcome

⸻

46. Outcome Does Not Rewrite History

Once an Outcome has been established, later state changes must not erase it.

Example:

10:00
Payment completed.
12:00
Payment reversed.

The historical Outcomes are:

Outcome A:
Payment completed.
Outcome B:
Payment reversed.

The system must preserve the temporal sequence.

⸻

47. Outcome Correction

If an Outcome was incorrectly recorded, the correction should create an explicit correction or superseding record rather than silently rewriting history.

Original Outcome
      ↓
Correction
      ↓
Corrected Interpretation

Auditability requires preserving lineage.

⸻

48. Outcome and Idempotency

Repeated execution attempts may produce duplicate or equivalent Outcomes.

Example:

Execution A:
Transfer $500
Execution B:
Retry after timeout

Both may refer to the same underlying transaction.

Noema should use correlation and idempotency semantics to avoid incorrectly interpreting retries as independent business Outcomes.

⸻

49. Outcome Uncertainty

Outcome uncertainty is expected in distributed systems.

Examples:

Network timeout
External service unavailable
Event not received
Eventual consistency
Conflicting sources
Unknown transaction state

Noema must represent:

UNKNOWN

where the actual Outcome cannot be established.

⸻

50. Unknown Is Not Failure

This distinction is mandatory.

FAILED

means there is evidence that the Action failed.

UNKNOWN

means Noema does not know whether it succeeded or failed.

Example:

Request → Payment Provider
       ↓
Network Timeout

Correct:

Outcome = UNKNOWN

Not:

Outcome = FAILED

unless authoritative evidence establishes failure.

⸻

51. Outcome Verification Sources

Outcome verification should prefer authoritative sources.

A conceptual hierarchy may be:

Authoritative System of Record
        ↓
Authoritative Event
        ↓
Verified External Response
        ↓
Trusted Observation
        ↓
Unverified Observation
        ↓
Model Inference

Model inference should not normally establish a consequential Outcome by itself.

⸻

52. Model-Generated Outcome

A Model may infer a likely Outcome:

"Looks like the payment probably succeeded."

This is not equivalent to an authoritative Outcome.

It should be represented as:

Model Inference:
payment likely succeeded

rather than:

Outcome:
SUCCEEDED

until established by sufficient evidence.

⸻

53. Human-Confirmed Outcome

In some workflows, a human may confirm an Outcome.

Example:

System:
Unable to verify shipment.
Human:
"The package was delivered."

This becomes Evidence with a particular provenance and trust level.

It should remain distinguishable from machine-observed evidence.

⸻

54. Outcome Authority

The source establishing an Outcome matters.

For example:

Payment State
→ Payment Provider
Employee Record
→ HR System
Account Balance
→ Banking System

Noema should identify the authoritative source where one exists.

⸻

55. Outcome Reconciliation

When multiple systems contain representations of the same Outcome, Noema may reconcile them.

Source A
   +
Source B
   +
Source C
      ↓
Reconciliation
      ↓
Canonical Outcome

Reconciliation must preserve the underlying evidence and provenance.

⸻

56. Outcome Semantics for External APIs

An API response must not automatically be interpreted as the business Outcome.

Example:

HTTP 202 Accepted

means:

Request accepted for processing.

It does not necessarily mean:

Business operation completed.

Therefore:

HTTP Response
      ≠
Business Outcome

unless the API contract explicitly establishes that equivalence.

⸻

57. Outcome Semantics for Asynchronous Systems

For asynchronous operations:

Action
  ↓
Accepted
  ↓
Processing
  ↓
Completed
  ↓
Verified

The initial response may only establish:

Execution Accepted

The final Outcome may arrive later through:

* webhook
* event
* polling
* callback
* system-of-record query

⸻

58. Outcome and Events

An event may be evidence of an Outcome.

Example:

Event:
card.renewed
Outcome:
Card renewal completed.

But:

Event ≠ Outcome

The event is an observable representation originating from a system.

Noema interprets it into canonical Outcome semantics.

⸻

59. Outcome and State Reconciliation

Sometimes the best evidence of an Outcome is the resulting State.

Example:

Before:
subscription.status = active
Action:
CancelSubscription
After:
subscription.status = cancelled

The State change supports the Outcome:

Outcome:
Subscription cancellation completed.

But State remains independently modeled.

⸻

60. Outcome Expiration

Some Outcomes have temporal validity.

Example:

Authorization granted for 30 minutes.

The Outcome may remain historically valid while no longer being operationally applicable.

Historical validity and current applicability are distinct.

⸻

61. Outcome Auditability

Material Outcomes should be auditable.

At minimum, the system should be able to establish:

What happened?
When did it happen?
Which Intent caused it?
Which Action produced it?
Which Execution attempted it?
Which Entity was affected?
What evidence supports it?
Where did the evidence originate?
Was the Outcome verified?

⸻

62. Outcome Provenance Chain

A canonical provenance chain is:

Actor
  ↓
Intent
  ↓
Trust Decision
  ↓
Action
  ↓
Execution
  ↓
External System
  ↓
Observation
  ↓
Evidence
  ↓
Outcome
  ↓
Satisfaction Evaluation

This allows Noema to reconstruct the complete semantic lifecycle.

⸻

63. Outcome Integrity

An Outcome should not be materially modified without preserving its history.

Where corrections are required:

Original Outcome
      ↓
Correction / Supersession
      ↓
Current Interpretation

The original record remains part of the audit trail.

⸻

64. Outcome and Trust

Trust determines whether Noema may allow an Action.

Outcome determines what happened after that decision.

Therefore:

Trust
  ↓
Authorization to act
Outcome
  ↓
Result of acting

Outcome does not retroactively establish that an Action was authorized.

⸻

65. Outcome and Failure Recovery

An Outcome may trigger recovery logic.

Example:

Outcome:
Payment Failed
Recovery:
Retry
Retry Outcome:
Payment Succeeded

Each is a distinct Outcome.

The overall Intent may ultimately become:

SATISFIED

despite an earlier failed execution.

⸻

66. Outcome and Retries

Retries must not automatically create multiple business Outcomes.

Execution Attempt 1
      ↓
Timeout
Execution Attempt 2
      ↓
Success

Potentially:

One business Outcome:
Transfer Completed

with:

Two execution attempts

The ontology must distinguish Execution Attempts from business Outcomes.

⸻

67. Outcome and Compensation

A compensation Action does not erase the original Outcome.

Example:

Charge Customer
      ↓
Outcome: Charged
Provision Service
      ↓
Outcome: Failed
Refund Customer
      ↓
Outcome: Refunded

The final business state may be corrected, but the historical Outcomes remain.

⸻

68. Outcome Classification

Outcomes may be classified along multiple dimensions.

Operational

SUCCESS
FAILURE
PENDING
UNKNOWN

Semantic

SATISFIED
PARTIAL
UNSATISFIED
UNKNOWN

These dimensions should not be collapsed.

For example:

Operational:
SUCCESS
Semantic:
UNSATISFIED

is possible.

Example:

Wrong account successfully received the transfer.

⸻

69. Dual Outcome Model

Noema should conceptually distinguish:

Operational Outcome

from:

Intent Satisfaction

For example:

┌────────────────────────────┐
│ Operational Outcome        │
│                            │
│ Action executed: SUCCESS   │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ Semantic Evaluation        │
│                            │
│ Intent satisfied: NO       │
└────────────────────────────┘

This distinction is one of the most important parts of the Outcome ontology.

⸻

70. Canonical Outcome Model

A conceptual representation:

Outcome
├── id
├── intent_id
├── action_id
├── execution_id
├── status
├── result
├── affected_entities
├── state_changes
├── evidence
├── provenance
├── timestamps
├── verification
└── satisfaction

Where:

status

describes operational result.

And:

satisfaction

describes whether the Intent was fulfilled.

⸻

71. Canonical Outcome Flow

                 INTENT
                    │
                    ▼
                 ACTION
                    │
                    ▼
                EXECUTION
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Execution Result     External State
          │                   │
          └─────────┬─────────┘
                    ▼
               EVIDENCE
                    │
                    ▼
             OBSERVED OUTCOME
                    │
                    ▼
            OUTCOME VERIFICATION
                    │
                    ▼
          INTENT SATISFACTION

⸻

72. Core Invariants

Invariant 1

An Outcome represents what actually happened.

Invariant 2

Outcome must remain distinct from Intent.

Invariant 3

Outcome must remain distinct from Action.

Invariant 4

Outcome must remain distinct from Execution.

Invariant 5

Execution success does not automatically imply Intent satisfaction.

Invariant 6

An HTTP success response does not automatically constitute a business Outcome.

Invariant 7

An unknown Outcome must not be represented as a failure without evidence.

Invariant 8

An unknown Outcome must not be represented as success without evidence.

Invariant 9

Expected Outcome and Observed Outcome must remain distinct.

Invariant 10

Outcome verification must use appropriate Evidence.

Invariant 11

Material Outcomes must have traceable Provenance.

Invariant 12

Historical Outcomes must not be silently overwritten by later State changes.

Invariant 13

Retries must remain distinguishable from independent business Outcomes.

Invariant 14

Compensating Actions must not erase the original Outcome.

Invariant 15

Partial success must remain explicitly represented.

Invariant 16

Conflicting Evidence must remain visible until reconciled.

Invariant 17

Model inference alone must not establish a consequential Outcome when authoritative verification is required.

Invariant 18

An Outcome must remain correlated with the Intent and Action that produced it.

Invariant 19

Outcome State and business Entity State must remain conceptually distinct.

Invariant 20

Outcome evaluation must ultimately determine whether the original Intent was satisfied, partially satisfied, unsatisfied, or remains unknown.

⸻

73. Relationship to the Noema Ontology

outcome.md completes the relationship established across the ontology:

Actor
  │
  │ expresses
  ▼
Intent
  │
  │ concerns
  ▼
Entity
  │
  │ interpreted through
  ▼
Context
  │
  │ constrained by
  ▼
Constraint / Policy
  │
  │ governed by
  ▼
Authority
  │
  │ evaluated by
  ▼
Trust
  │
  │ permits
  ▼
Action
  │
  │ requires
  ▼
Capability
  │
  │ performs
  ▼
Execution
  │
  │ produces
  ▼
Outcome
  │
  │ verified through
  ▼
Evidence
  │
  │ evaluated against
  ▼
Intent
  │
  ▼
Satisfaction

This gives Noema a closed semantic loop rather than a one-way agent/tool pipeline.

⸻

74. Canonical Principle

The central principle of this document is:

Noema must distinguish between what was requested, what was authorized, what was attempted, what technically happened, what actually happened in the domain, and whether the original Intent was satisfied.

Therefore:

Intent
   ≠
Action
   ≠
Execution
   ≠
Execution Result
   ≠
Outcome
   ≠
Intent Satisfaction

That separation is what allows Noema to remain deterministic and auditable even when the systems it orchestrates are probabilistic, asynchronous, distributed, or partially observable.