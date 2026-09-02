Compensation

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/compensation.md

⸻

1. Definition

Compensation defines how Noema represents and coordinates corrective Actions when an execution sequence produces a partial, failed, or otherwise unacceptable Outcome.

Compensation exists because execution is not always atomic.

An Action may succeed while a subsequent Action fails:

Action A → SUCCESS
Action B → FAILURE

The original state may now be partially changed.

Compensation provides a controlled mechanism for addressing that state.

⸻

2. Core Principle

Compensation is not rollback. It is an explicitly modeled corrective Action executed after an already-committed effect.

This distinction is fundamental.

A database transaction may provide:

BEGIN
  A
  B
COMMIT

with true rollback:

ROLLBACK

But distributed execution often looks like:

Service A → SUCCESS
      ↓
Service B → SUCCESS
      ↓
Service C → FAILURE

The earlier effects cannot necessarily be rolled back transactionally.

Noema therefore needs compensation semantics.

⸻

3. Why Compensation Exists

Consider:

Intent:
"Book the flight and hotel."

Execution:

reserve_flight      → SUCCESS
reserve_hotel       → FAILURE

The user’s desired Outcome has not been achieved.

Yet the flight reservation may already exist.

Compensation could produce:

cancel_flight       → SUCCESS

resulting in:

reserve_flight
      ↓
reserve_hotel
      ↓
FAILURE
      ↓
cancel_flight

⸻

4. Compensation Is Not Automatic Rollback

Noema must not assume:

failure → inverse operation

For example:

charge_card

does not necessarily imply:

refund_card

as a mechanically safe inverse.

A refund may:

* require authorization;
* have different business semantics;
* incur fees;
* be subject to policy;
* be impossible after a certain period;
* create a new financial transaction.

Therefore compensation must be explicitly modeled.

⸻

5. Compensation Is an Action

A compensation operation is itself an Action.

Example:

Original Action:
charge_payment
Compensation Action:
refund_payment

Therefore compensation participates in the same Noema execution model:

Action
  ↓
Trust
  ↓
Action Contract
  ↓
Execution
  ↓
Outcome

A compensation Action is not outside the ontology.

⸻

6. Compensation and Intent

The original Intent expresses the desired Outcome.

Compensation exists to address a divergence between:

Desired Outcome

and:

Actual Outcome

Conceptually:

Intent
  ↓
Expected Outcome
  ↓
Execution
  ↓
Actual Outcome
  ↓
Divergence
  ↓
Compensation

⸻

7. Compensation Trigger

Compensation may be considered when:

execution failure
partial completion
timeout
consumer rejection
external failure
inconsistent downstream state

occurs.

However:

A failure does not automatically imply that compensation is appropriate.

The system must determine whether a compensating Action is defined and justified.

⸻

8. Compensation Preconditions

A compensation Action may have explicit preconditions.

Example:

refund_payment

may require:

original_charge.exists
original_charge.status = CAPTURED
refund_not_already_completed

The authoritative execution system may evaluate these conditions.

⸻

9. Compensation Eligibility

A previously executed Action may have a compensation definition:

charge_payment
    compensatable = true
    compensation = refund_payment

Another Action may be:

send_email
    compensatable = false

because the email cannot meaningfully be unsent.

⸻

10. Compensatable Does Not Mean Reversible

These concepts must remain distinct.

Reversible

The original state can meaningfully be restored.

Compensatable

A subsequent Action can address the effect.

Example:

send_email

cannot be reversed.

But a follow-up:

send_correction_email

may compensate for its effect in a business sense.

Therefore:

reversal ≠ compensation

⸻

11. Compensation vs Undo

“Undo” is often a user-interface concept.

Compensation is an execution concept.

For example:

User:
Undo purchase.

may resolve to:

cancel_order

or:

refund_payment

depending on business semantics.

Noema should resolve the user’s Intent into the appropriate Action rather than assuming that “undo” means a generic inverse operation.

⸻

12. Compensation Relationship

The Action Model should allow a relationship such as:

Action A
   │
   │ may be compensated by
   ▼
Action B

Example:

reserve_hotel
      │
      └── compensated by → cancel_hotel_reservation

The relationship should be explicit.

⸻

13. Compensation Scope

A compensation Action should identify the specific execution effect it addresses.

Example:

compensation:
    action: cancel_hotel_reservation
    compensates: execution_123

This prevents a generic:

cancel_hotel_reservation

from being incorrectly interpreted as compensation for an unrelated reservation.

⸻

14. Compensation Lineage

Every compensation execution should maintain lineage to the original execution.

Conceptually:

Original Contract
       ↓
Original Execution
       ↓
Original Outcome
       ↓
Compensation Contract
       ↓
Compensation Execution
       ↓
Compensation Outcome

This creates an auditable causal chain.

⸻

15. Compensation Identity

A compensation operation should have its own identity.

For example:

original_execution_id:
exec_123
compensation_id:
comp_456

The compensation is a new execution event.

It must not overwrite the original execution record.

⸻

16. Compensation Requires Authorization

Compensation is not inherently authorized merely because the original Action was authorized.

This is critical.

For example:

Original:
charge ₦100,000

may have been authorized.

But:

Compensation:
refund ₦100,000

is a distinct Action.

It may require its own:

* authorization;
* policy evaluation;
* risk evaluation;
* evidence;
* Action Contract.

Therefore:

Authorization does not automatically transfer from an original Action to its compensation Action.

⸻

17. Compensation and Trust

A compensation Action passes through Trust according to its own semantics.

Conceptually:

Original Action
      ↓
Trust
      ↓
Execution
      ↓
Failure / Partial Outcome
      ↓
Compensation candidate
      ↓
Trust
      ↓
Compensation Contract
      ↓
Execution

Where the system has explicitly defined a trusted compensation mechanism, some authorization context may be inherited or pre-authorized.

But that inheritance must itself be a deterministic policy.

⸻

18. No Implicit Authorization Inheritance

Bad:

Original Action was allowed
        ↓
Compensation automatically allowed

Better:

Original Action was allowed
        ↓
Compensation relationship exists
        ↓
Compensation policy evaluated
        ↓
Compensation authorized

This preserves the Trust boundary.

⸻

19. Compensation Policy

Organizations may define policies such as:

If reservation succeeds but payment fails,
cancel the reservation automatically.

This can be represented as a deterministic compensation policy.

Conceptually:

Trigger:
payment.failure
Condition:
reservation.status = CONFIRMED
Compensation:
cancel_reservation

The policy should be explicit rather than inferred by a model.

⸻

20. Compensation and Determinism

Compensation is especially sensitive to Noema’s determinism principle.

The system must not reason:

"The reservation probably should be cancelled."

Instead:

Policy:
payment failure + confirmed reservation
→ cancel reservation

or:

No compensation rule applies.

If the correct compensation cannot be determined safely:

REQUIRES_REVIEW

is preferable to guessing.

⸻

21. Compensation Strategies

A compensation strategy may be:

AUTOMATIC
MANUAL
CONDITIONAL
NONE

Automatic

The system may issue the compensation Action automatically when deterministic conditions are satisfied.

Manual

A human must authorize or initiate compensation.

Conditional

Compensation occurs only if specified conditions are met.

None

No compensation exists or is appropriate.

⸻

22. Automatic Compensation

Example:

reserve_inventory → SUCCESS
charge_payment    → FAILURE

Policy:

If payment fails,
release_inventory.

Noema can deterministically create:

release_inventory

subject to the relevant Trust and execution requirements.

⸻

23. Manual Compensation

Some situations require human judgment.

Example:

Customer received duplicate shipment.

Possible corrective Actions:

refund
replacement
return request
account credit

If policy does not uniquely determine the appropriate response:

COMPENSATION_REQUIRES_REVIEW

Noema should not guess.

⸻

24. Conditional Compensation

Example:

charge_payment → SUCCESS
create_subscription → FAILURE

Policy:

If subscription creation failed
AND
payment is refundable
→ refund payment.

Otherwise:

Escalate.

⸻

25. Compensation Chains

Compensation itself may fail.

Example:

A → SUCCESS
B → FAILURE
↓
compensate A
↓
FAILURE

The system now has a compensation failure.

This must not be hidden.

⸻

26. Compensation Failure

A compensation failure should create an explicit state.

Conceptually:

COMPENSATION_FAILED

This indicates:

The system attempted a defined corrective Action, but the corrective Action itself did not complete successfully.

This may require:

retry
alternative compensation
manual intervention
escalation

⸻

27. Nested Compensation

A compensation Action may itself have a compensating Action.

This should be permitted only where the semantics are explicitly defined.

For example:

Original:
reserve_inventory
Compensation:
release_inventory
Compensation of compensation:
not defined

Generally:

Compensation chains should be bounded.

Unbounded compensation recursion is dangerous.

⸻

28. Compensation Depth

The execution model should support a bounded compensation depth.

Conceptually:

max_compensation_depth = N

If the system reaches the boundary:

COMPENSATION_LIMIT_REACHED

and requires deterministic escalation.

⸻

29. Compensation Ordering

When multiple Actions need compensation, ordering matters.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE

Potential compensation:

compensate B
      ↓
compensate A

This resembles a reverse dependency order.

However, the correct ordering is domain-specific and must be explicitly modeled.

⸻

30. Compensation Dependency Graph

A composite execution may be represented as:

A
↓
B
↓
C

If C fails:

C → FAILURE
B → compensation
A → compensation

The execution engine can use the dependency graph to determine eligible compensation Actions.

It must not blindly reverse every Action.

⸻

31. Compensation Is Not Guaranteed

A compensation strategy cannot guarantee restoration of the original state.

Example:

send_money

followed by:

refund_money

may not restore every external effect:

* fees;
* exchange-rate differences;
* notifications;
* downstream processing;
* timing effects.

Therefore the system should distinguish:

compensation attempted

from:

original state fully restored

⸻

32. Compensation Outcome

A compensation produces its own Outcome.

Example:

Compensation:
refund_payment
Outcome:
SUCCESS
Reference:
refund_tx_456

The original Outcome remains:

charge_payment:
SUCCESS

Both records remain true.

⸻

33. Desired Outcome vs Compensated Outcome

The original Intent may have:

Desired Outcome:
hotel + flight booked

Actual execution:

flight booked
hotel failed

Compensation:

flight cancelled

Final state:

flight not booked
hotel not booked

This may be an acceptable recovery state even though the original desired Outcome was not achieved.

Noema must preserve that distinction.

⸻

34. Compensation and Outcome

Outcome should therefore be modeled as:

Expected Outcome
       ↓
Execution Outcome
       ↓
Outcome Evaluation
       ↓
Compensation if required
       ↓
Compensation Outcome
       ↓
Final Outcome State

Compensation is part of recovery, not a rewriting of history.

⸻

35. Compensation and Idempotency

Compensation Actions should be idempotent where possible.

Example:

refund_payment(payment_123)

If the compensation request is delivered twice:

C1
C1

the system should not accidentally issue two refunds.

The consumer should use an appropriate idempotency key.

⸻

36. Compensation and Retry

Retry and compensation are different mechanisms.

Retry

Attempts the same Action again.

A → FAILURE
↓
retry A

Compensation

Executes a different corrective Action.

A → SUCCESS
↓
compensate A

Therefore:

retry ≠ compensation

⸻

37. When to Retry

Retry is appropriate when:

transient network failure
temporary service unavailability
rate limiting
recoverable infrastructure failure

provided the Action is safe to retry.

⸻

38. When to Compensate

Compensation is appropriate when:

an effect already occurred
AND
that effect should be corrected
AND
a valid corrective Action exists

Example:

charge succeeded
subscription creation failed
→ refund

⸻

39. Retry Before Compensation

A system may sometimes need to determine whether the original Action actually failed.

Example:

Request sent
↓
timeout
↓
unknown state

It would be dangerous to immediately compensate because:

the Action may actually have succeeded.

The execution system should reconcile the state first.

Therefore:

UNKNOWN
   ↓
reconcile
   ↓
SUCCESS / FAILURE
   ↓
possible compensation

⸻

40. Compensation and Unknown State

An unknown Outcome must not be treated as failure.

Example:

charge_payment
    ↓
timeout
    ↓
UNKNOWN

Noema should not immediately issue:

refund_payment

because the charge may have succeeded.

The system needs authoritative reconciliation.

⸻

41. Compensation and External Systems

Compensation becomes particularly important when Actions cross system boundaries.

Example:

Noema
 ↓
Payment Service
 ↓
Payment Provider

Noema cannot assume a distributed transaction across all three systems.

Compensation provides a higher-level recovery mechanism.

⸻

42. Consumer Responsibility

The execution consumer remains responsible for implementing the actual compensating Action.

Noema defines:

what compensation is authorized

The consumer determines:

how the compensation is performed

⸻

43. Noema Responsibility

Noema is responsible for:

identifying compensation requirements
evaluating applicable policies
resolving compensation Actions
applying Trust
issuing Action Contracts
maintaining lineage
tracking outcomes

The consumer is responsible for:

executing the compensating Action
validating authoritative business state
reporting the result

⸻

44. Compensation Contract

A compensation Action should result in its own Action Contract.

Conceptually:

Original Contract
      ↓
Original Execution
      ↓
Failure / Partial Outcome
      ↓
Compensation Decision
      ↓
Compensation Action
      ↓
Trust Evaluation
      ↓
Compensation Contract
      ↓
Consumer

This preserves the same execution boundary used everywhere else.

⸻

45. Compensation Contract Lineage

A compensation contract should reference:

original_contract_id
original_execution_id
compensation_id

This allows the execution graph to be reconstructed.

⸻

46. Compensation Record

Conceptually:

Compensation {
    compensation_id
    original_action
    original_execution
    trigger
    reason
    compensation_action
    strategy
    authorization
    contract_id
    status
    outcome
}

This is a conceptual model rather than the final storage schema.

⸻

47. Compensation Trigger Types

Possible triggers include:

ACTION_FAILURE
DEPENDENCY_FAILURE
TIMEOUT
PARTIAL_COMPLETION
POLICY_CONDITION
OUTCOME_MISMATCH
MANUAL_REQUEST

The canonical taxonomy should evolve as Noema’s execution model matures.

⸻

48. Compensation Reason

A compensation record should explain why it exists.

Example:

reason:
"Payment succeeded but subscription provisioning failed."

For deterministic systems, the machine-readable trigger should accompany the human-readable explanation.

⸻

49. Compensation vs Escalation

Not every failure should result in compensation.

Sometimes the correct response is:

ESCALATE

Example:

Payment succeeded.
Subscription creation failed.
Refund is prohibited by policy.

The system should not invent another recovery operation.

Instead:

COMPENSATION_UNAVAILABLE
        ↓
HUMAN_REVIEW

⸻

50. Compensation State Machine

A conceptual compensation lifecycle:

NOT_REQUIRED
     │
     ▼
REQUIRED
     │
     ▼
EVALUATING
     │
     ├───────────────┐
     ▼               ▼
AUTHORIZED       REQUIRES_REVIEW
     │
     ▼
CONTRACTED
     │
     ▼
EXECUTING
     │
   ┌─┴──────────┐
   ▼            ▼
SUCCESS       FAILED
                │
                ▼
             ESCALATED

This state machine is separate from the Trust State Machine and the Action Contract lifecycle.

⸻

51. Compensation State Semantics

NOT_REQUIRED

No corrective Action is necessary.

REQUIRED

A prior Outcome has created a compensatable divergence.

EVALUATING

The system is determining the appropriate compensation.

AUTHORIZED

The compensation Action has passed the required Trust checks.

REQUIRES_REVIEW

Deterministic compensation cannot safely be established.

CONTRACTED

A compensation Action Contract has been issued.

EXECUTING

The consumer is executing the compensation.

SUCCESS

The compensating Action completed successfully.

FAILED

The compensation attempt did not complete successfully.

ESCALATED

The system requires further intervention.

⸻

52. Compensation Invariants

Invariant 1

Compensation is an Action.

Invariant 2

Compensation is not automatic rollback.

Invariant 3

A failed Action does not automatically imply compensation.

Invariant 4

A compensation Action must be explicitly defined or deterministically derived from an explicit policy.

Invariant 5

Compensation must maintain lineage to the original execution.

Invariant 6

Compensation does not erase or mutate the original Outcome.

Invariant 7

Compensation requires its own authorization semantics.

Invariant 8

Compensation must not be based on probabilistic guessing when the consequences are material.

Invariant 9

Unknown execution state must not be treated as confirmed failure.

Invariant 10

Retry and compensation are distinct mechanisms.

Invariant 11

Compensation Actions should be idempotent where possible.

Invariant 12

Compensation failure must remain observable and auditable.

Invariant 13

Compensation recursion must be bounded.

Invariant 14

Noema must distinguish “compensation attempted” from “original state restored.”

Invariant 15

The execution consumer remains authoritative for the actual business-state change.

⸻

53. Canonical Mental Model

The simplest model is:

             ACTION
                │
                ▼
            EXECUTION
                │
        ┌───────┴────────┐
        ▼                ▼
     SUCCESS          FAILURE
        │                │
        │                ▼
        │          Is there an
        │          explicit/
        │          deterministic
        │          compensation?
        │                │
        │          ┌─────┴─────┐
        │          ▼           ▼
        │         YES          NO
        │          │           │
        │          ▼           ▼
        │      COMPENSATE    ESCALATE
        │          │
        │          ▼
        │       OUTCOME
        │
        └──────────┬───────────
                   ▼
              FINAL OUTCOME

⸻

54. Final Definition

Compensation is Noema’s explicit recovery mechanism for execution effects that cannot simply be rolled back. It models corrective Actions, their authorization, contracts, execution, lineage, and Outcomes without rewriting the history of the original execution.

The core invariant is:

When execution produces an unacceptable partial or failed Outcome, Noema does not guess how to undo the world. It determines whether an explicit, authorized compensating Action exists; if one does, it executes that Action through the same Trust and Contract boundaries as any other Action. If one does not, Noema escalates rather than inventing a recovery.