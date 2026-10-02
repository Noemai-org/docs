> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Outcome

Status: Foundational
Version: 0.2
Domain: Ontology
Canonical Path: ontology/outcome.md

⸻

1. Definition

An Outcome is the canonical semantic representation of what actually resulted from an Action, Execution, or domain process, as established through observation and Evidence.

Outcome answers:

What happened as a result of the Action, and what can Noema establish about that result?

Outcome is therefore distinct from:

* Intent
* Action
* Execution
* Execution Result
* Evidence
* Entity State
* Intent Satisfaction

The fundamental relationship is:

Intent
   ↓
Action
   ↓
Execution
   ↓
Observation / Evidence
   ↓
Outcome
   ↓
Outcome Evaluation
   ↓
Intent Satisfaction

The distinction is foundational:

Intent       = what was desired
Action       = what operation was selected
Execution    = what was attempted/performed
Exec Result  = what the execution mechanism returned
Outcome      = what actually resulted
Satisfaction = whether the Outcome fulfilled the Intent

⸻

2. Outcome and the Semantic Loop

Execution is not the end of a Noema workflow.

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
Observation
  ↓
Evidence
  ↓
Outcome
  ↓
Verification
  ↓
Intent Satisfaction

Noema must therefore distinguish between performing an operation and establishing what resulted from that operation.

This closes the semantic loop:

Desired
   ↓
Performed
   ↓
Observed
   ↓
Established
   ↓
Evaluated

⸻

3. Outcome Is Not Intent

Intent represents the Actor’s desired objective.

Outcome represents the resulting condition or effect established after an Action or process.

Example:

Intent:
Transfer $500 to Alice.
Outcome:
$500 was transferred to Alice.

The two may correspond, but they are different ontology objects.

Intent ≠ Outcome

⸻

4. Outcome Is Not Action

An Action represents an operation.

Example:

Action:
TransferFunds

An Outcome represents what resulted from that operation.

Examples:

Transfer completed.
Transfer rejected.
Transfer failed.
Transfer status unknown.

The same Action may therefore produce different Outcomes:

TransferFunds
   ├── SUCCEEDED
   ├── REJECTED
   ├── FAILED
   ├── UNKNOWN
   └── PENDING

⸻

5. Outcome Is Not Execution

An Execution represents an attempt to perform an Action.

Outcome represents what resulted from that attempt.

Action
   ↓
Execution
   ↓
Outcome

Multiple Execution attempts may contribute to one business Outcome.

Example:

Execution Attempt 1
      ↓
   Timeout
      ↓
Execution Attempt 2
      ↓
   Success
      ↓
Business Outcome:
Transfer Completed

Therefore:

Execution ≠ Outcome

⸻

6. Outcome Is Not Execution Result

An Execution Result represents what the execution mechanism returned.

Example:

HTTP 200
{
  "transaction_id": "tx_123"
}

This establishes that the invoked interface returned a particular response.

It does not necessarily establish the complete domain Outcome.

For example:

Execution Result
      ↓
Request Accepted
      ↓
Transaction Created
      ↓
Funds Actually Moved
      ↓
Outcome Verified

Therefore:

Execution Result ≠ Outcome

An execution result may constitute Evidence for an Outcome, but its semantic meaning must be determined from the relevant contract and Evidence.

⸻

7. Outcome Is Not Entity State

Entity State describes the condition of an Entity.

Outcome describes what resulted from an Action or process.

Example:

State:
Card.status = active
Outcome:
Card renewal completed.

A State change may provide Evidence for an Outcome, but State and Outcome remain distinct concepts.

State ≠ Outcome

⸻

8. Outcome Structure

Conceptually, an Outcome contains:

Outcome
├── id
├── intent
├── action
├── execution
├── status
├── result
├── affected_entities
├── state_changes
├── evidence
├── provenance
├── timestamps
├── verification
└── satisfaction

The canonical serialization of these properties belongs to the schema layer.

⸻

9. Outcome Identity

Every material Outcome should have an independent identity.

Example:

outcome_123

Outcome identity allows Noema to reference the Outcome independently of:

* the Intent
* the Action
* the Execution
* the Execution Result
* the external system
* the current Entity State

This is necessary for traceability, auditability, correlation, and historical preservation.

⸻

10. Outcome Status

Outcome status describes the operational state of the Outcome.

A foundational vocabulary is:

PENDING
SUCCEEDED
PARTIALLY_SUCCEEDED
FAILED
REJECTED
CANCELLED
UNKNOWN

The vocabulary may be extended by domain-specific schemas without changing the semantics of the foundational states.

Outcome status must not be conflated with Intent Satisfaction.

⸻

11. SUCCEEDED

SUCCEEDED means that the relevant operational result has been established as successfully occurring.

Example:

Action:
RenewCard
Outcome:
Card renewal completed successfully.
Status:
SUCCEEDED

SUCCEEDED does not, by itself, imply that the originating Intent was satisfied.

⸻

12. PARTIALLY_SUCCEEDED

PARTIALLY_SUCCEEDED means that some intended operational effects occurred while one or more expected effects did not.

Example:

Intent:
Onboard Employee
Outcomes:
✓ Employee created
✓ Email provisioned
✗ Permissions failed

The aggregate operational Outcome is:

PARTIALLY_SUCCEEDED

It must not be represented as full operational success.

⸻

13. FAILED

FAILED means that there is sufficient Evidence that the intended operation did not successfully produce its expected operational result.

Examples include:

* insufficient funds
* external service failure
* validation failure
* execution timeout where failure is established
* authoritative rejection after execution

A timeout alone does not necessarily establish FAILED.

Where the final domain result cannot be established, UNKNOWN may be correct.

⸻

14. REJECTED

REJECTED means that the Action was explicitly prevented from proceeding.

Example:

Intent:
Refund $50,000
Outcome:
Rejected because Actor lacks required authority.

Rejection is distinct from execution failure because the Action may never have been performed.

REJECTED ≠ FAILED

⸻

15. CANCELLED

CANCELLED means that an ongoing execution or process was intentionally stopped.

Example:

Intent:
Generate report
Outcome:
Cancelled by Actor before completion.

Cancellation should remain distinguishable from failure.

⸻

16. UNKNOWN

UNKNOWN means that Noema cannot establish the actual operational Outcome with sufficient Evidence.

Example:

Action:
Transfer $5,000
Execution:
Timeout
External State:
Unknown

The correct representation may be:

Outcome:
UNKNOWN

Noema must not convert uncertainty into either success or failure without sufficient Evidence.

⸻

17. Pending Outcome

An Action may have been initiated while its final Outcome remains unresolved.

Example:

Action:
TransferFunds
Outcome:
PENDING

This may occur because of:

* asynchronous processing
* eventual consistency
* external approval
* long-running operations
* queued execution
* delayed external events

A Pending Outcome may subsequently transition to a terminal Outcome.

⸻

18. Expected Outcome

An Expected Outcome describes the result that should occur if an Intent is successfully fulfilled.

Example:

Intent:
Renew Card
Expected Outcome:
Card status becomes active
with a new expiry date.

Expected Outcome forms part of the semantic contract against which an Observed Outcome may be evaluated.

Expected Outcome
       ↓
   Evaluation
       ↑
Observed Outcome

Expected Outcome must remain distinct from Observed Outcome.

⸻

19. Observed Outcome

An Observed Outcome describes what Noema has established from observations or Evidence.

Example:

Observed Outcome:
Card status = active
Expiry = 2030-08

Observation may originate from:

* an authoritative system
* an event
* an API response
* a database
* an external provider
* human confirmation
* another trusted source

Observation is not automatically equivalent to verification.

⸻

20. Outcome Verification

Outcome Verification determines whether sufficient Evidence establishes the claimed Outcome.

Conceptually:

Expected Outcome
       +
Observed Evidence
       ↓
Outcome Verification
       ↓
Verified / Unverified / Conflicting / Unknown

Verification may be:

* immediate
* asynchronous
* event-driven
* polling-based
* source-confirmed
* reconciliation-based

Verification semantics should remain distinct from Outcome status.

⸻

21. Intent Satisfaction

Intent Satisfaction determines whether the established Outcome fulfills the originating Intent.

Example:

Intent:
Transfer $500 to Alice.
Observed Outcome:
$500 transferred to Alice.
Satisfaction:
SATISFIED

But:

Intent:
Transfer $500 to Alice.
Observed Outcome:
$500 transferred to Bob.
Satisfaction:
UNSATISFIED

The underlying Action may have technically succeeded while the Intent remains unsatisfied.

⸻

22. Execution Success vs Intent Satisfaction

This distinction is foundational to Noema.

Execution Success
        ≠
Outcome Success
        ≠
Intent Satisfaction

Example:

Action:
POST /transfer
Execution Result:
HTTP 200 OK

This may establish technical execution success.

If the wrong account receives the funds:

Operational Outcome:
SUCCEEDED
Intent Satisfaction:
UNSATISFIED

Noema must therefore evaluate both the operational result and the semantic relationship between that result and the originating Intent.

⸻

23. Satisfaction Status

A foundational satisfaction vocabulary is:

SATISFIED
PARTIALLY_SATISFIED
UNSATISFIED
UNKNOWN

Satisfaction is a semantic evaluation of the Outcome against the Intent.

It is not an alternative Outcome status.

⸻

24. SATISFIED

SATISFIED means the established Outcome sufficiently fulfills the originating Intent.

Example:

Intent:
Renew Card
Outcome:
Card successfully renewed.
Satisfaction:
SATISFIED

⸻

25. PARTIALLY_SATISFIED

PARTIALLY_SATISFIED means that only part of the Intent was fulfilled.

Example:

Intent:
Book flights for two people.
Outcome:
Passenger A booked.
Passenger B not booked.
Satisfaction:
PARTIALLY_SATISFIED

⸻

26. UNSATISFIED

UNSATISFIED means that the established Outcome does not fulfill the originating Intent.

Example:

Intent:
Cancel subscription.
Outcome:
Subscription remains active.
Satisfaction:
UNSATISFIED

⸻

27. UNKNOWN Satisfaction

UNKNOWN means Noema cannot establish whether the Intent was satisfied.

Example:

Intent:
Transfer $5,000.
Execution:
Timeout.
External State:
No confirmation available.
Satisfaction:
UNKNOWN

Noema must preserve this uncertainty rather than converting it into a definitive semantic judgment.

⸻

28. Outcome Evidence

Material Outcomes should be supported by Evidence.

Example:

Outcome:
Payment refunded.
Evidence:
Payment provider transaction record.

Evidence may include:

* external API responses
* database records
* authoritative events
* receipts
* signed responses
* resulting Entity State
* human confirmation
* system observations

Evidence establishes the basis upon which an Outcome is represented or verified.

⸻

29. Outcome Provenance

Outcome Provenance identifies the origin of the information supporting an Outcome.

Example:

Outcome:
Payment completed.
Source:
Payment Provider
Observed At:
2026-08-23T09:32:00Z
Source Reference:
txn_123

Provenance is necessary for:

* auditability
* traceability
* reconciliation
* authority evaluation
* evidence inspection

⸻

30. Outcome Timestamps

An Outcome may contain multiple semantically distinct timestamps:

requested_at
started_at
completed_at
observed_at
verified_at

These timestamps must not be collapsed when their meanings differ.

For example:

completed_at ≠ observed_at ≠ verified_at

⸻

31. Outcome Duration

Where relevant, Noema may record duration between lifecycle events.

Example:

started_at
     ↓
completed_at

This supports:

* SLA evaluation
* latency analysis
* workflow monitoring
* operational diagnostics

Duration is metadata about the Outcome and must not be confused with the Outcome itself.

⸻

32. State Changes

An Outcome may result in Entity State changes.

Example:

Before:
Card.status = expired
Action:
RenewCard
After:
Card.status = active

The Outcome may record:

State Changes:
status: expired → active
expiry: 2026-08 → 2030-08

However:

State Change ≠ Outcome

The State Change may instead serve as Evidence supporting the Outcome.

⸻

33. Affected Entities

An Outcome should identify affected Entities where possible.

Example:

Outcome:
Payment refunded.
Affected Entities:
Payment: payment_123
Customer: customer_456
Account: account_789

Affected Entity references allow Noema to connect Outcomes to the domain objects whose state or relationships were affected.

⸻

34. External Outcomes

An external system may produce information representing an Outcome that Noema consumes.

Example:

Noema
  ↓
Payment Provider
  ↓
Provider Outcome
  ↓
Noema

Noema must distinguish:

External System Outcome

from:

Noema Canonical Outcome

The canonical Outcome may preserve the external representation as Evidence and Provenance.

⸻

35. Outcome Normalization

Different systems may represent equivalent operational results differently.

Example:

Provider A:
HTTP 200
status = "success"
Provider B:
status = "completed"
Provider C:
result = "OK"

Noema may normalize these into:

SUCCEEDED

while preserving:

* original source representation
* source identity
* provenance
* Evidence
* relevant external identifiers

Normalization must not destroy source semantics.

⸻

36. Outcome Conflicts

Multiple sources may provide conflicting information.

Example:

Payment Provider:
Payment = completed
Internal Database:
Payment = pending

Noema must not silently select one representation.

The conflict should remain represented in the Evidence and reconciliation layer.

Where the conflict prevents establishing the actual Outcome:

Outcome:
UNKNOWN
Evidence:
CONFLICTING

until the conflict is resolved.

⸻

37. Outcome Freshness

An Outcome is historical information and may become stale relative to current Entity State.

Example:

10:00
Account status = active
10:30
Account status = suspended

A prior Outcome remains historically valid if it accurately represented what happened at the earlier time.

Therefore:

Historical Outcome ≠ Current State

Current State must not retroactively rewrite historical Outcomes.

⸻

38. Outcome Finality

Not every Outcome is immediately final.

Examples:

Payment:
PENDING
Transfer:
PROCESSING
Approval:
AWAITING_REVIEW

Noema must distinguish interim observations from final established Outcomes.

Interim Outcome
       ↓
Final Outcome

Finality is distinct from the existence of an Outcome.

⸻

39. Outcome Lifecycle

A conceptual lifecycle is:

PENDING
   ↓
OBSERVED
   ↓
VERIFIED
   ↓
FINAL

Alternative paths may include:

PENDING
   ↓
FAILED

or:

PENDING
   ↓
UNKNOWN

The precise lifecycle mechanics belong to the execution and lifecycle specifications rather than the core ontology.

⸻

40. Outcome Correlation

An Outcome must be traceable to the Action and Execution associated with it.

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

This supports end-to-end traceability.

⸻

41. Outcome and Intent Correlation

An Outcome must remain associated with its originating Intent where applicable.

Example:

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
  ↓
Satisfaction

⸻

42. Multiple Outcomes

A single Intent may produce multiple Outcomes.

Example:

Intent:
Onboard Employee
Outcomes:
1. Employee created
2. Email account created
3. Permissions assigned
4. Welcome email sent

Noema may evaluate these collectively to determine Composite Intent Satisfaction.

⸻

43. Composite Outcome

Multiple Actions may collectively contribute to a Composite Outcome.

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

A Composite Outcome describes an aggregate operational result derived from multiple related Outcomes.

⸻

44. Partial Failure

Composite operations require explicit partial-failure semantics.

Example:

Action A ✓
Action B ✓
Action C ✗
Action D not attempted

The aggregate operational result may be:

PARTIALLY_SUCCEEDED

It must not be represented as full success.

⸻

45. Outcome Dependencies

Some Outcomes depend on preceding Outcomes.

Example:

Create Account
      ↓
Outcome:
Account Created
      ↓
Fund Account
      ↓
Outcome:
Funding Completed

If the first Outcome fails, the dependent Action may never execute.

Outcome dependency therefore provides important causal and workflow context without collapsing distinct Outcomes into one record.

⸻

46. Outcome Compensation

A failed multi-step process may trigger a compensating Action.

Example:

Create Resource
      ↓
Outcome: Created
Charge Customer
      ↓
Outcome: Charged
Provision Service
      ↓
Outcome: Failed
Refund Customer
      ↓
Outcome: Refunded

The compensation Outcome is distinct from the original Outcomes.

Original Outcome
      ↓
Failure
      ↓
Compensation Action
      ↓
Compensation Outcome

Compensation does not erase history.

⸻

47. Outcome Does Not Rewrite History

Once an Outcome has been established, later State changes must not erase it.

Example:

10:00
Outcome A:
Payment completed.
12:00
Outcome B:
Payment reversed.

Both Outcomes remain part of the historical record.

The later Outcome changes the current interpretation or state of the domain, but does not erase the earlier event.

⸻

48. Outcome Correction

If an Outcome was incorrectly recorded, correction must preserve its lineage.

Conceptually:

Original Outcome
      ↓
Correction / Supersession
      ↓
Corrected Interpretation

The original record remains auditable.

Noema must not silently mutate historical semantic facts in a manner that destroys provenance.

⸻

49. Outcome and Idempotency

Repeated execution attempts may produce duplicate or equivalent observations of the same underlying business Outcome.

Example:

Execution A:
Transfer $500
Execution B:
Retry after timeout

Both may refer to the same underlying transaction.

Noema must use correlation and idempotency semantics to distinguish:

Multiple Execution Attempts

from:

Multiple Business Outcomes

⸻

50. Outcome Uncertainty

Uncertainty is intrinsic to distributed and asynchronous systems.

Examples include:

* network timeout
* external service unavailability
* missing event
* eventual consistency
* conflicting sources
* unknown transaction state

Noema must represent unresolved uncertainty explicitly.

UNKNOWN

is therefore a semantic state, not an implementation error.

⸻

51. Unknown Is Not Failure

This distinction is mandatory.

FAILED

means there is sufficient Evidence that the Action failed.

UNKNOWN

means Noema cannot establish whether the Action succeeded or failed.

Example:

Request
   ↓
Payment Provider
   ↓
Network Timeout

Correct when no authoritative result exists:

Outcome = UNKNOWN

Not:

Outcome = FAILED

unless Evidence establishes failure.

⸻

52. Outcome Verification Sources

Outcome verification should consider source authority and Evidence quality.

A conceptual ordering is:

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

The ordering is a conceptual verification hierarchy, not a universal rule for every domain.

Where consequential Outcomes require authoritative verification, model inference alone should not establish the Outcome.

⸻

53. Model-Generated Outcome

A model may infer a likely result:

"Looks like the payment probably succeeded."

This is not equivalent to an established Outcome.

It should remain represented as a model inference or observation:

Model Inference:
payment likely succeeded

rather than:

Outcome:
SUCCEEDED

until sufficient Evidence establishes the Outcome.

⸻

54. Human-Confirmed Outcome

A human may provide Evidence establishing or contributing to an Outcome.

Example:

System:
Unable to verify shipment.
Human:
"The package was delivered."

The human statement becomes Evidence with identifiable provenance.

It must remain distinguishable from:

* system-generated Evidence
* authoritative system state
* external events
* model inference

⸻

55. Outcome Authority

The source establishing an Outcome matters.

Examples:

Payment State
→ Payment Provider
Employee Record
→ HR System
Account Balance
→ Banking System

Where an authoritative source exists, Noema should identify it as part of Outcome Provenance and Evidence.

⸻

56. Outcome Reconciliation

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

Reconciliation must preserve:

* underlying Evidence
* source identity
* provenance
* timestamps
* conflicts
* resolution basis

A canonical representation must not erase the source representations from which it was derived.

⸻

57. Outcome Semantics for External APIs

An API response must not automatically be interpreted as the business Outcome.

Example:

HTTP 202 Accepted

may mean:

Request accepted for processing.

It does not necessarily mean:

Business operation completed.

Therefore:

HTTP Response ≠ Business Outcome

unless the relevant API contract explicitly establishes that equivalence.

⸻

58. Outcome Semantics for Asynchronous Systems

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

The initial response may establish only:

Execution Accepted

The final Outcome may arrive later through:

* webhook
* event
* polling
* callback
* system-of-record query

Noema must not prematurely treat acceptance as completion.

⸻

59. Outcome and Events

An Event may provide Evidence of an Outcome.

Example:

Event:
card.renewed
Outcome:
Card renewal completed.

But:

Event ≠ Outcome

An Event is an observable representation emitted by a system.

Noema may interpret that Event as Evidence supporting a canonical Outcome.

⸻

60. Outcome and State Reconciliation

Resulting Entity State may provide Evidence for an Outcome.

Example:

Before:
subscription.status = active
Action:
CancelSubscription
After:
subscription.status = cancelled

This may support:

Outcome:
Subscription cancellation completed.

However:

State ≠ Outcome

The State remains independently modeled.

⸻

61. Outcome Expiration

Some Outcomes have temporal validity or applicability.

Example:

Authorization granted for 30 minutes.

The historical Outcome remains valid as a record of what occurred.

Its current operational applicability may later expire.

Therefore:

Historical Validity
        ≠
Current Applicability

⸻

62. Outcome Auditability

Material Outcomes should be auditable.

At minimum, Noema should be able to establish:

What happened?
When did it happen?
Which Intent was involved?
Which Action produced it?
Which Execution attempted it?
Which Entities were affected?
What Evidence supports it?
Where did the Evidence originate?
Was the Outcome verified?
What is its current satisfaction status?

⸻

63. Outcome Provenance Chain

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

This allows Noema to reconstruct the semantic lifecycle from desired objective through observed result.

⸻

64. Outcome Integrity

An Outcome must not be materially modified in a way that destroys its historical lineage.

Where correction is required:

Original Outcome
      ↓
Correction / Supersession
      ↓
Current Interpretation

The original record remains part of the audit trail.

⸻

65. Outcome and Trust

Trust determines whether Noema may permit an Action.

Outcome determines what resulted from that Action.

Therefore:

Trust
  ↓
Authorization / Permission to Act
Action
  ↓
Execution
  ↓
Outcome

Outcome does not retroactively establish that an Action was authorized.

Authorization and result are distinct semantic dimensions.

⸻

66. Outcome and Failure Recovery

An Outcome may trigger recovery logic.

Example:

Outcome:
Payment Failed
Recovery Action:
Retry Payment
Outcome:
Payment Succeeded

Each Outcome remains distinct.

The originating Intent may ultimately become:

SATISFIED

despite an earlier failed execution.

⸻

67. Outcome and Retries

Retries must not automatically create multiple business Outcomes.

Example:

Execution Attempt 1
      ↓
Timeout
Execution Attempt 2
      ↓
Success

Potentially:

One Business Outcome:
Transfer Completed
Execution Attempts:
2

The ontology must distinguish Execution Attempts from business Outcomes.

⸻

68. Outcome and Compensation

A compensating Action does not erase the original Outcome.

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

The final domain condition may be corrected, but the historical Outcomes remain independently represented.

⸻

69. Outcome Classification

Outcome semantics should be represented along separate dimensions.

Operational Status

SUCCEEDED
PARTIALLY_SUCCEEDED
FAILED
REJECTED
CANCELLED
PENDING
UNKNOWN

Intent Satisfaction

SATISFIED
PARTIALLY_SATISFIED
UNSATISFIED
UNKNOWN

These dimensions must not be collapsed.

For example:

Operational Status:
SUCCEEDED
Intent Satisfaction:
UNSATISFIED

is valid.

Example:

Intent:
Transfer $500 to Alice.
Outcome:
$500 successfully transferred to Bob.

The transfer operation succeeded, but the originating Intent was not satisfied.

⸻

70. Dual Evaluation Model

Noema should conceptually separate:

Operational Outcome

from:

Intent Satisfaction

Conceptually:

┌────────────────────────────┐
│ Operational Evaluation     │
│                            │
│ Action Result: SUCCEEDED   │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ Semantic Evaluation        │
│                            │
│ Intent Satisfaction:       │
│ UNSATISFIED                │
└────────────────────────────┘

This prevents technical execution success from being mistaken for semantic success.

⸻

71. Canonical Outcome Model

Conceptually:

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

describes the operational result.

And:

satisfaction

describes the semantic relationship between that result and the originating Intent.

These are independent dimensions.

⸻

72. Canonical Outcome Flow

                         INTENT
                            │
                            ▼
                         ACTION
                            │
                            ▼
                        EXECUTION
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          Execution Result       External State
                 │                     │
                 └──────────┬──────────┘
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
                  OPERATIONAL EVALUATION
                            │
                            ▼
                 INTENT SATISFACTION

The flow explicitly separates:

1. what was requested,
2. what Action was selected,
3. what was executed,
4. what the execution mechanism returned,
5. what was observed,
6. what Evidence supports,
7. what Outcome was established,
8. and whether the originating Intent was satisfied.

⸻

73. Core Invariants

Invariant 1

An Outcome represents an established result of an Action, Execution, or domain process.

Invariant 2

Outcome must remain distinct from Intent.

Invariant 3

Outcome must remain distinct from Action.

Invariant 4

Outcome must remain distinct from Execution.

Invariant 5

Outcome must remain distinct from Execution Result.

Invariant 6

Outcome must remain distinct from Entity State.

Invariant 7

Execution success does not automatically imply Intent Satisfaction.

Invariant 8

An HTTP success response does not automatically constitute a business Outcome.

Invariant 9

An unknown Outcome must not be represented as failure without sufficient Evidence.

Invariant 10

An unknown Outcome must not be represented as success without sufficient Evidence.

Invariant 11

Expected Outcome and Observed Outcome must remain distinct.

Invariant 12

Outcome verification must be grounded in appropriate Evidence.

Invariant 13

Material Outcomes must have traceable Provenance.

Invariant 14

Historical Outcomes must not be silently overwritten by later Entity State.

Invariant 15

Retries must remain distinguishable from independent business Outcomes.

Invariant 16

Compensating Actions must not erase original Outcomes.

Invariant 17

Partial operational success must remain explicitly represented.

Invariant 18

Conflicting Evidence must remain visible until reconciled.

Invariant 19

Model inference alone must not establish a consequential Outcome where authoritative verification is required.

Invariant 20

An Outcome should remain correlated with the relevant Intent, Action, and Execution.

Invariant 21

Outcome status and Intent Satisfaction must remain separate semantic dimensions.

Invariant 22

Outcome and Entity State must remain independently modeled even when State provides Evidence for an Outcome.

Invariant 23

Outcome correction must preserve historical lineage.

Invariant 24

Outcome finality must remain distinguishable from interim observation.

Invariant 25

Outcome evaluation must determine whether the originating Intent is satisfied, partially satisfied, unsatisfied, or remains unknown.

⸻

74. Relationship to the Noema Ontology

outcome.md completes the execution side of the Noema ontology:

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
  │ produces / enables observation of
  ▼
Outcome
  │
  │ supported by
  ▼
Evidence
  │
  │ verified through
  ▼
Verification
  │
  │ evaluated against
  ▼
Intent
  │
  ▼
Satisfaction

This gives Noema a closed semantic loop rather than a one-way agent/tool pipeline.

⸻

75. Canonical Principle

The central principle of the Outcome ontology is:

Noema must distinguish between what was requested, what was authorized, what was attempted, what technically occurred, what actually resulted in the domain, what Evidence establishes that result, and whether the original Intent was satisfied.

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

The resulting semantic loop is:

        DESIRED
           │
           ▼
         INTENT
           │
           ▼
         ACTION
           │
           ▼
       EXECUTION
           │
           ▼
       OBSERVATION
           │
           ▼
        EVIDENCE
           │
           ▼
        OUTCOME
           │
           ▼
      VERIFICATION
           │
           ▼
     SATISFACTION
           │
           └──────────────► INTENT

This separation allows Noema to preserve deterministic, auditable semantics across systems that are probabilistic, asynchronous, distributed, externally controlled, eventually consistent, or partially observable.