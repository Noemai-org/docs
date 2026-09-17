Compensation

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/compensation.md

⸻

1. Definition

Compensation defines how Noema represents, evaluates, authorizes, and coordinates corrective Actions when an execution sequence produces a partial, failed, or otherwise unacceptable Outcome.

Compensation exists because execution is not always atomic.

An Action may succeed while a subsequent Action fails:

Action A → SUCCESS
Action B → FAILURE

The original state may now be partially changed.

Compensation provides a controlled mechanism for addressing that divergence without rewriting the history of the original execution.

⸻

2. Core Principle

Compensation is not rollback.

It is an explicitly modeled corrective Action executed after an already-observed or reconciled effect.

A database transaction may provide:

BEGIN
  A
  B
COMMIT
ROLLBACK

with true transactional rollback.

Distributed execution often looks like:

Service A → SUCCESS
     ↓
Service B → SUCCESS
     ↓
Service C → FAILURE

The earlier effects may no longer be transactionally reversible.

Noema therefore models compensation as a separate, governed execution path.

⸻

3. Why Compensation Exists

Consider:

Intent:
"Book the flight and hotel."

Execution:

reserve_flight → SUCCESS
reserve_hotel  → FAILURE

The requested Outcome has not been achieved.

Yet the flight reservation may already exist.

If an explicit compensation relationship and applicable policy exist, compensation may produce:

cancel_flight → SUCCESS

The execution history remains:

reserve_flight
      ↓
reserve_hotel
      ↓
FAILURE
      ↓
cancel_flight

Compensation addresses the divergence. It does not erase the original events.

⸻

4. Compensation Is Not Automatic Rollback

Noema must not assume:

failure → inverse operation

For example:

charge_payment

does not necessarily imply:

refund_payment

as a mechanically safe inverse.

A refund may:

* require separate authorization;
* have different business semantics;
* incur fees;
* be subject to policy;
* be unavailable after a defined period;
* create a new financial transaction;
* require reconciliation before it can safely occur.

Compensation therefore requires explicit semantics.

⸻

5. Compensation Is an Action

A compensation operation is itself an Action.

Example:

Original Action:
charge_payment
Compensation Action:
refund_payment

The compensation Action participates in the same execution architecture:

Action
  ↓
Trust
  ↓
Action Contract
  ↓
Execution
  ↓
Verification
  ↓
Outcome

Compensation is not outside the Action or Execution models.

⸻

6. Compensation and Intent

The original Intent expresses a desired semantic goal.

Compensation exists when execution and verification establish a divergence between:

Requested / Expected Outcome

and:

Actual Observed Outcome

Conceptually:

Intent
  ↓
Expected Outcome
  ↓
Execution
  ↓
Verification
  ↓
Actual Outcome
  ↓
Divergence
  ↓
Compensation Evaluation

Compensation does not modify the original Intent.

If the user materially changes the desired goal, that is a new Intent version rather than a mutation of the original Intent.

⸻

7. Compensation Trigger

Compensation may be evaluated following:

* execution failure;
* partial completion;
* dependency failure;
* verified outcome mismatch;
* policy-defined recovery conditions;
* consumer rejection after an effect has occurred;
* reconciliation establishing an effect that requires correction;
* manual compensation request.

However:

failure ≠ compensation

A failure only creates a condition in which compensation may be considered.

The system must determine whether a valid compensating Action exists and whether executing it is justified.

⸻

8. Compensation and Unknown Execution State

An UNKNOWN execution state must not be treated as confirmed failure.

For example:

charge_payment
      ↓
request submitted
      ↓
timeout
      ↓
UNKNOWN

Noema must not immediately execute:

refund_payment

because the charge may have succeeded.

The execution system must first attempt authoritative reconciliation:

UNKNOWN
   ↓
State Reconciliation
   ↓
verified/reconciled execution state
   ↓
possible compensation evaluation

If reconciliation remains inconclusive, the system may require escalation or further intervention.

Timeout is an execution condition, not proof that compensation is required.

⸻

9. Compensation Preconditions

A compensation Action may have explicit preconditions.

Example:

refund_payment
original_charge.exists
original_charge.status = CAPTURED
refund_not_already_completed

These conditions may depend on current enterprise state.

Where current state is material, Noema must obtain and reconcile authoritative observations before determining whether the compensation Action can safely proceed.

⸻

10. Compensation Eligibility

An executed Action may have an explicit compensation definition.

Example:

charge_payment
    compensatable = true
    compensation = refund_payment

Another Action may be:

send_email
    compensatable = false

because no meaningful corrective Action has been defined.

Compensation eligibility is a semantic property of the Action and its applicable policies, not an inference produced from the Action name.

⸻

11. Compensatable Does Not Mean Reversible

These concepts remain distinct.

Reversible

The original effect can meaningfully be restored.

Compensatable

A subsequent Action can address the effect without necessarily restoring the exact prior state.

For example:

send_email

cannot be reversed.

A subsequent:

send_correction_email

may nevertheless compensate for the business effect.

Therefore:

reversal ≠ compensation

⸻

12. Compensation vs Undo

“Undo” is often a user-interface concept.

Compensation is an execution concept.

For example:

User:
"Undo purchase."

may resolve to:

cancel_order

or:

refund_payment

depending on the enterprise-defined semantics, current state, policy, and available capabilities.

Noema must resolve the request into an explicit Action rather than assuming that “undo” means a generic inverse operation.

⸻

13. Compensation Relationship

The Action Model may define an explicit relationship:

Action A
   │
   │ may be compensated by
   ▼
Action B

Example:

reserve_hotel
      │
      └── compensated by → cancel_hotel_reservation

The relationship must have defined semantics and must not be inferred merely because two Actions appear to be opposites.

⸻

14. Compensation Scope

A compensation Action must identify the specific execution effect it addresses.

Example:

compensation:
    action: cancel_hotel_reservation
    compensates: execution_123

This prevents a generic:

cancel_hotel_reservation

from being incorrectly interpreted as compensation for an unrelated reservation.

The compensation target must be resolved to the specific resource/effect within the relevant execution scope.

⸻

15. Compensation Lineage

Every compensation execution maintains lineage to the original execution.

Conceptually:

Original Intent Version
       ↓
Original Action Contract
       ↓
Original Execution
       ↓
Original Verification / Outcome
       ↓
Compensation Decision
       ↓
Compensation Action Contract
       ↓
Compensation Execution
       ↓
Compensation Verification / Outcome

This lineage forms part of the causal audit record.

⸻

16. Compensation Identity

A compensation operation has its own identity.

For example:

original_execution_id:
exec_123
compensation_id:
comp_456

The compensation is a new execution activity.

It must not overwrite or mutate the original execution record.

⸻

17. Compensation Requires Its Own Authorization Semantics

Compensation is not inherently authorized merely because the original Action was authorized.

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
* business conditions;
* evidence;
* Action Contract;
* execution constraints.

Therefore:

authorization(original Action)

does not automatically equal:

authorization(compensation Action)

⸻

18. Compensation and Trust

A compensation Action passes through the same deterministic Trust boundary as any other consequential Action.

Conceptually:

Original Action
      ↓
Trust
      ↓
Execution
      ↓
Failure / Partial / Verified Divergence
      ↓
Compensation Candidate
      ↓
Resolve Compensation Action
      ↓
State Reconciliation where required
      ↓
Trust
      ↓
Action Contract
      ↓
Execution
      ↓
Verification

Any inheritance of authorization or context must itself be explicitly defined by deterministic policy.

⸻

19. No Implicit Authorization Inheritance

Unsafe:

Original Action was allowed
        ↓
Compensation automatically allowed

Correct:

Original Action was permitted
        ↓
Compensation relationship exists
        ↓
Compensation conditions evaluated
        ↓
Required authority/policy evaluated
        ↓
Trust Decision
        ↓
Compensation Contract

Noema preserves the Trust boundary for the compensating Action.

⸻

20. Compensation Policy

Organizations may define deterministic policies such as:

If reservation succeeds
AND payment fails
AND reservation is still cancellable
→ cancel reservation

The policy explicitly defines:

* trigger;
* required evidence;
* state conditions;
* compensation Action;
* authorization requirements;
* applicable limits;
* escalation behavior.

The policy must be deterministic and versioned.

The model must not invent compensation policy.

⸻

21. Compensation and Determinism

Compensation is particularly sensitive to Noema’s determinism principle.

The system must not reason:

"The reservation probably should be cancelled."

Instead:

Policy:
payment failure
+
confirmed reservation
+
reservation cancellable
→
cancel_reservation

If no deterministic rule establishes the appropriate corrective Action:

ESCALATE

or an explicit compensation control state such as:

REQUIRES_REVIEW

may apply.

REQUIRES_REVIEW is not a Trust outcome.

If the situation reaches Trust, the canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

⸻

22. Compensation Strategies

A compensation strategy may be:

AUTOMATIC
MANUAL
CONDITIONAL
NONE

Automatic

The compensating Action may proceed automatically when deterministic conditions are satisfied and Trust returns EXECUTE.

Manual

Human intervention is required to initiate or authorize the compensating Action.

Conditional

Compensation occurs only when specified conditions are satisfied.

None

No compensating Action exists or compensation is not appropriate.

⸻

23. Automatic Compensation

Example:

reserve_inventory → SUCCESS
charge_payment    → FAILURE

Policy:

If payment failure is verified
AND inventory reservation remains active
→ release_inventory

Noema may resolve the compensation Action and evaluate it through Trust.

If permitted:

Trust → EXECUTE
      ↓
Action Contract
      ↓
release_inventory

Automatic does not mean ungoverned.

⸻

24. Manual Compensation

Some situations require human judgment.

Example:

Customer received duplicate shipment.

Possible corrective Actions:

refund
replacement
return_request
account_credit

If applicable policy does not uniquely determine the appropriate Action, Noema must not guess.

The execution state may become:

COMPENSATION_REQUIRES_REVIEW

with Trust/escalation semantics applied according to the applicable policy.

⸻

25. Conditional Compensation

Example:

charge_payment        → SUCCESS
create_subscription   → FAILURE

Policy:

If subscription creation failed
AND payment is refundable
AND refund is permitted
→ refund_payment

Otherwise:

ESCALATE

The conditions must be evaluated against current authoritative or reconciled enterprise state where required.

⸻

26. Compensation Chains

Compensation itself may fail.

Example:

A → SUCCESS
B → FAILURE
↓
compensate A
↓
FAILURE

The compensation failure must remain explicit.

It must not be represented as though the original Action simply never happened.

⸻

27. Compensation Failure

A compensation failure should create an explicit execution-domain state.

Conceptually:

COMPENSATION_FAILED

This means:

Noema attempted a defined corrective Action, but that corrective Action did not complete with a verified successful Outcome.

Depending on policy, the next step may be:

* retry;
* reconciliation;
* alternative compensation;
* human intervention;
* escalation.

A compensation failure is not automatically a business-state failure. Enterprise state remains authoritative.

⸻

28. Nested Compensation

A compensation Action may itself have a compensating Action.

This is permitted only where the relationship is explicitly defined.

For example:

Original:
reserve_inventory
Compensation:
release_inventory
Compensation of compensation:
not defined

Unbounded compensation recursion is dangerous.

Compensation depth must therefore be explicitly bounded.

⸻

29. Compensation Depth

The execution model may support:

max_compensation_depth = N

If the boundary is reached:

COMPENSATION_LIMIT_REACHED

The system must follow the applicable deterministic escalation policy.

The limit prevents compensation from becoming an uncontrolled recursive execution mechanism.

⸻

30. Compensation Ordering

When multiple Actions require compensation, ordering matters.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE

Potential recovery:

compensate B
      ↓
compensate A

This may resemble reverse dependency order.

However, reverse execution order is not universally correct.

The required ordering must be determined by the explicit dependency and compensation semantics of the execution graph.

⸻

31. Compensation Dependency Graph

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

The execution system can use the dependency graph to determine eligible compensation candidates.

It must not blindly reverse every Action.

Actions without defined compensation remain uncompensated and may require escalation or another deterministic recovery path.

⸻

32. Compensation Is Not Guaranteed

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
* timing effects;
* external side effects;
* regulatory records.

Therefore Noema must distinguish:

compensation attempted

from:

original state fully restored

The latter requires appropriate authoritative verification.

⸻

33. Compensation Outcome

A compensation produces its own execution Outcome.

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

Compensation does not rewrite the original Outcome.

⸻

34. Desired Outcome vs Compensated Outcome

The original Intent may have:

Desired Outcome:
hotel + flight booked

Execution:

flight booked
hotel failed

Compensation:

flight cancelled

Final observed situation:

flight not booked
hotel not booked

This may be an acceptable recovery state even though the original desired Outcome was not achieved.

Noema must preserve the distinction between:

* requested outcome;
* execution outcomes;
* compensation outcomes;
* final verified execution state;
* enterprise Business State.

⸻

35. Compensation and Outcome

Compensation therefore participates in outcome evaluation without rewriting history:

Expected Outcome
       ↓
Execution
       ↓
Verification
       ↓
Actual Outcome
       ↓
Divergence
       ↓
Compensation Evaluation
       ↓
Compensation Execution
       ↓
Compensation Verification
       ↓
Final Execution Assessment

The final execution assessment must not be confused with enterprise Business State.

Enterprise systems remain authoritative for their business domain.

⸻

36. Compensation and Idempotency

Compensation Actions should be idempotent where possible.

Example:

refund_payment(payment_123)

If the same compensation request is delivered twice, the consumer should not accidentally issue two refunds.

The compensation Action Contract should carry an appropriate execution identity/idempotency key, and the consumer should enforce the relevant idempotency semantics.

Compensation idempotency does not remove the need for reconciliation when execution becomes UNKNOWN.

⸻

37. Compensation and Retry

Retry and compensation are distinct mechanisms.

Retry

Attempts the same Action again:

A → FAILURE
↓
retry A

Compensation

Executes a different corrective Action:

A → SUCCESS
↓
compensate A

Therefore:

retry ≠ compensation

An UNKNOWN execution state must be reconciled before either retry or compensation when the original effect may already have occurred.

⸻

38. When to Retry

Retry may be appropriate when:

* transient network failure occurred;
* temporary service unavailability occurred;
* rate limiting occurred;
* recoverable infrastructure failure occurred;
* the Action’s retry semantics permit retry.

The execution system must first establish that retry is safe under the Action Contract, idempotency semantics, current state, and applicable policy.

A timeout must not automatically be classified as retryable failure.

⸻

39. When to Compensate

Compensation is appropriate when:

an effect has occurred
AND
the effect creates a defined divergence or unacceptable condition
AND
a valid corrective Action exists
AND
the corrective Action is permitted

Example:

charge succeeded
subscription creation failed
→ refund

provided the applicable policy and current state permit the refund.

⸻

40. Reconcile Before Compensation

A system may first need to determine whether the original Action actually failed.

Example:

Request sent
↓
timeout
↓
UNKNOWN

It would be dangerous to immediately compensate because the original Action may have succeeded.

The correct sequence is:

UNKNOWN
   ↓
State Reconciliation
   ↓
resolved/reconciled execution state
   ↓
possible compensation evaluation

This is especially important for externally committed effects.

⸻

41. Compensation and External Systems

Compensation is particularly important when Actions cross system boundaries.

Example:

Noema
  ↓
Payment Service
  ↓
Payment Provider

Noema cannot assume that these systems participate in a single distributed transaction.

Compensation provides a higher-level recovery mechanism across execution boundaries.

The exact business-state effect remains owned by the relevant enterprise system or System of Record.

⸻

42. Consumer Responsibility

The execution consumer remains responsible for implementing the actual compensating Action.

Noema defines and governs:

* the semantic Action;
* applicable constraints;
* authorization and policy conditions;
* Action Contract;
* lineage;
* verification requirements.

The consumer determines:

* how the compensating Action is physically performed;
* how its enterprise integration is implemented;
* what authoritative result is returned.

The consumer must not expand the Action Contract or perform an uncontracted operation.

⸻

43. Noema Responsibility

Noema is responsible for:

* identifying compensation requirements;
* evaluating applicable deterministic policies;
* resolving compensation Actions;
* reconciling relevant state;
* applying Trust;
* issuing Action Contracts;
* maintaining execution lineage;
* tracking compensation state;
* requesting verification;
* recording Outcomes;
* escalating when deterministic compensation is unavailable.

The consumer is responsible for:

* executing the compensating Action;
* respecting the Action Contract;
* validating or obtaining authoritative business-state results;
* reporting execution and verification information.

⸻

44. Compensation Contract

A compensation Action results in its own Action Contract.

Conceptually:

Original Intent Version
      ↓
Original Action
      ↓
Original Action Contract
      ↓
Original Execution
      ↓
Failure / Partial Outcome / Verified Divergence
      ↓
Compensation Evaluation
      ↓
Compensation Action
      ↓
State Reconciliation
      ↓
Trust Evaluation
      ↓
Compensation Action Contract
      ↓
Execution Consumer
      ↓
Verification

The compensation Contract uses the same execution boundary as every other consequential Action.

⸻

45. Compensation Contract Lineage

A compensation Contract should reference sufficient lineage to reconstruct causality, including:

original_intent_version
original_contract_id
original_execution_id
original_action_instance_id
compensation_id
compensation_action_version

Where applicable, it should also preserve:

trust_decision_id
policy_version
capability_version
graph_version

This allows the execution graph and decision context to be reconstructed.

⸻

46. Compensation Record

Conceptually:

Compensation {
    compensation_id
    original_intent_version
    original_action
    original_execution
    trigger
    reason
    compensation_action
    target_effect
    strategy
    authorization
    trust_decision
    contract_id
    status
    outcome
    verification
}

This is a conceptual model rather than the final storage schema.

The record must preserve lineage without becoming a replacement for the original execution record.

⸻

47. Compensation Trigger Types

Possible triggers include:

ACTION_FAILURE
DEPENDENCY_FAILURE
TIMEOUT
PARTIAL_COMPLETION
POLICY_CONDITION
OUTCOME_MISMATCH
RECONCILED_STATE
MANUAL_REQUEST

The canonical trigger taxonomy should evolve with the broader execution model.

A trigger identifies why compensation evaluation began. It does not itself establish that compensation is required.

⸻

48. Compensation Reason

A compensation record should explain why compensation was considered.

Example:

reason:
"Payment succeeded but subscription provisioning failed."

For deterministic systems, the machine-readable trigger should accompany a human-readable explanation.

The explanation is not a substitute for the underlying evidence, policy evaluation, or causal record.

⸻

49. Compensation vs Escalation

Not every divergence should result in compensation.

Sometimes the correct response is:

ESCALATE

Example:

Payment succeeded.
Subscription creation failed.
Refund is prohibited by policy.

Noema should not invent another recovery operation.

Instead:

COMPENSATION_UNAVAILABLE
        ↓
ESCALATE
        ↓
HUMAN / OPERATIONAL INTERVENTION

ESCALATE is a canonical Trust outcome where applicable. Operational states such as COMPENSATION_UNAVAILABLE or REQUIRES_REVIEW are execution-domain states and are not additional Trust outcomes.

⸻

50. Compensation State Machine

A conceptual compensation lifecycle is:

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
  ELIGIBLE       REQUIRES_REVIEW
     │
     ▼
TRUST_EVALUATION
     │
   ┌─┴───────────────┐
   ▼                 ▼
EXECUTE            ESCALATE / REJECT / CLARIFY
   │
   ▼
CONTRACTED
   │
   ▼
EXECUTING
   │
 ┌─┴──────────┐
 ▼            ▼
SUCCESS      UNKNOWN
              │
              ▼
          RECONCILIATING
              │
          ┌───┴────┐
          ▼        ▼
       SUCCESS   FAILED
                     │
                     ▼
                 ESCALATED

This state machine is separate from the Trust State Machine and Action Contract lifecycle.

EXECUTE in the Trust layer means the compensating Action is permitted to proceed. It does not mean the compensation succeeded.

⸻

51. Compensation State Semantics

NOT_REQUIRED

No compensating Action is currently required.

REQUIRED

A verified or appropriately established divergence has created a condition in which compensation must be evaluated.

EVALUATING

The system is determining whether a valid compensation Action and strategy exist.

REQUIRES_REVIEW

Deterministic compensation cannot safely be established without additional human or operational judgment.

TRUST_EVALUATION

The resolved compensation Action is being evaluated against applicable Trust conditions.

CONTRACTED

A compensation Action Contract has been issued.

EXECUTING

The consumer is executing the compensation.

RECONCILIATING

The compensation execution state is being reconciled because its outcome is unknown or otherwise requires authoritative state determination.

SUCCESS

The compensating Action has completed with a verified successful execution Outcome.

FAILED

The compensation attempt has not completed successfully and no successful compensating Outcome has been established.

ESCALATED

Further intervention is required.

These execution-domain states do not replace or modify the canonical Trust outcomes.

⸻

52. Compensation, Fact Status, and Evidence

Compensation decisions may depend on facts such as:

payment.status = CAPTURED
reservation.status = CONFIRMED
refund.status = NOT_COMPLETED

Noema must distinguish:

Evidence

from:

Fact Status

Fact Status may be:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Model confidence is not Fact Status.

A model may help identify candidate evidence or propose a compensation path, but it cannot establish authoritative business facts merely by expressing confidence.

Where required facts are UNKNOWN or CONFLICTED, compensation must not proceed by guessing.

⸻

53. Compensation and State Reconciliation

State Reconciliation is a first-class part of compensation evaluation.

The relevant flow is:

Enterprise Systems / Execution Consumer
              ↓
         Observations
              ↓
Hard Schema Validation / Admission
              ↓
       State Reconciliation
              ↓
     Reconciled Facts / Fact Status
              ↓
     Compensation Evaluation
              ↓
          Trust

Reconciliation is especially important when:

* the original execution is UNKNOWN;
* the external system is eventually consistent;
* multiple systems contain related state;
* a compensation target may already have changed;
* a previous compensation attempt may have succeeded;
* duplicate execution must be ruled out.

Compensation must operate on the best deterministically established state available, not on stale assumptions.

⸻

54. Compensation and Intent Versioning

Compensation must preserve the exact Intent version that produced the original execution.

An admitted Intent is immutable.

If a human or system changes the desired goal during recovery, that material change creates a new Intent version with explicit lineage:

Intent v1
   ↓
Execution
   ↓
Divergence
   ↓
Compensation

If the user instead requests a new goal:

Intent v1
   ↓
superseded by
   ↓
Intent v2

Compensation must not silently mutate the original Intent to make the recovery appear successful.

⸻

55. Compensation and Security

Compensation is a consequential execution path and therefore inherits Noema’s structural security requirements.

The model must not:

* receive or use execution credentials;
* directly call enterprise systems;
* invent compensation capabilities;
* modify Action Contracts;
* bypass Trust;
* transform arbitrary retrieved text into authority;
* infer authorization from confidence;
* create arbitrary HTTP, SQL, or other unregistered operations.

The compensation Action must resolve to an explicit Action, Capability, Action Contract, and permitted execution path.

⸻

56. Compensation and Planner Boundaries

Where the Planner participates in compensation selection, it remains bounded by:

Enterprise Action Graph
        +
Capability Registry
        +
Action Registry
        +
Action Contract Registry
        +
Trust constraints

The Planner may select among available, valid recovery paths.

It may not:

* invent a compensation Action;
* invent authority;
* create a new capability;
* modify an Action Contract;
* bypass Trust;
* expand compensation scope;
* decide that an unregistered operation is safe.

If no valid recovery path exists, the system must escalate or follow another explicit recovery policy.

⸻

57. Compensation and Causal Audit

Compensation must preserve a causal chain such as:

Intent Version
     ↓
Action
     ↓
Action Contract
     ↓
Execution Attempt
     ↓
Observation / Evidence
     ↓
State Reconciliation
     ↓
Fact Status
     ↓
Original Outcome
     ↓
Compensation Trigger
     ↓
Compensation Policy
     ↓
Compensation Action
     ↓
Trust Decision
     ↓
Compensation Contract
     ↓
Compensation Execution
     ↓
Verification
     ↓
Compensation Outcome

This provides causal auditability without requiring disclosure of private model chain-of-thought.

The explanation of why compensation occurred must be grounded in the evaluated conditions, evidence, policy, versions, and execution records.

⸻

58. Compensation and Operational Memory

Compensation history may be retained in Operational Memory as structured execution and recovery history.

Operational Memory may record:

* original execution;
* divergence;
* compensation decision;
* policy applied;
* compensation attempts;
* verification;
* intervention;
* final recovery state.

Operational Memory is not the enterprise source of truth for the business state being compensated.

Enterprise Systems of Record remain authoritative for enterprise Business State.

⸻

59. Compensation and Read-Only Operations

Compensation evaluation may involve read-only Actions that are nevertheless consequential.

For example:

read_payment_status
reconcile_reservation
inspect_refund_state

may expose protected financial or customer information or determine whether a consequential compensating Action is permitted.

Read-only therefore does not mean consequence-free.

Applicable data boundaries, authorization, Trust, and audit requirements still apply.

⸻

60. Compensation Invariants

Invariant 1

Compensation is an Action.

Invariant 2

Compensation is not automatic rollback.

Invariant 3

A failed Action does not automatically imply compensation.

Invariant 4

A compensation Action must be explicitly defined or deterministically established by an explicit policy.

Invariant 5

Compensation must maintain lineage to the original Intent version and execution.

Invariant 6

Compensation does not erase or mutate the original Outcome.

Invariant 7

Compensation has its own authorization semantics.

Invariant 8

Compensation must not be based on probabilistic guessing when the consequences are material.

Invariant 9

UNKNOWN execution state must not be treated as confirmed failure.

Invariant 10

State Reconciliation must be used where current external state is material to compensation safety.

Invariant 11

Retry and compensation are distinct mechanisms.

Invariant 12

Compensation Actions should be idempotent where possible.

Invariant 13

Compensation failure must remain observable and auditable.

Invariant 14

Compensation recursion must be bounded.

Invariant 15

Noema must distinguish compensation attempted from original state restored.

Invariant 16

Trust EXECUTE means the compensating Action is permitted to proceed; it does not mean the compensation succeeded.

Invariant 17

Compensation must execute through an explicit Action Contract.

Invariant 18

The Planner cannot invent compensation capabilities, authority, or executable semantics.

Invariant 19

Model confidence cannot establish compensation eligibility, authorization, or business-state truth.

Invariant 20

Enterprise Systems of Record remain authoritative for the business state affected by compensation.

Invariant 21

Compensation must not silently mutate an admitted Intent.

Invariant 22

A material change in the desired goal requires a new Intent version.

Invariant 23

Compensation state is distinct from Trust state and Action Contract lifecycle.

Invariant 24

Canonical Trust outcomes remain EXECUTE, CLARIFY, ESCALATE, and REJECT.

Invariant 25

Operational compensation states such as REQUIRES_REVIEW, COMPENSATION_FAILED, and COMPENSATION_LIMIT_REACHED are not additional Trust outcomes.

⸻

61. Canonical Mental Model

The canonical model is:

                    ACTION
                       │
                       ▼
                   EXECUTION
                       │
              ┌────────┴────────┐
              ▼                 ▼
           SUCCESS        FAILURE / PARTIAL
                                │
                                ▼
                         VERIFY / RECONCILE
                                │
                                ▼
                     Is a compensatable
                     divergence established?
                         │          │
                        NO         YES
                         │          │
                         ▼          ▼
                     ESCALATE   Resolve Compensation
                                    │
                                    ▼
                              State Reconciliation
                                    │
                                    ▼
                                Trust
                                    │
                     ┌──────────────┼──────────────┐
                     ▼              ▼              ▼
                  EXECUTE       CLARIFY/        REJECT/
                     │          ESCALATE          ...
                     ▼
             Action Contract
                     │
                     ▼
                EXECUTION
                     │
             ┌───────┴────────┐
             ▼                ▼
          SUCCESS          UNKNOWN
             │                │
             │                ▼
             │          RECONCILIATION
             │                │
             │                ▼
             │          SUCCESS / FAILED /
             │             ESCALATED
             │
             ▼
       Compensation Outcome

The central rule is:

Unknown → Reconcile
Failure / Verified Divergence → Evaluate Compensation
Explicit Compensation → Trust → Contract → Execute → Verify
No Safe Compensation → Escalate

⸻

62. Final Definition

Compensation is Noema’s explicit recovery mechanism for execution effects that cannot simply be rolled back.

It models corrective Actions, their eligibility, authorization, policy conditions, Action Contracts, execution, verification, lineage, and Outcomes without rewriting the history of the original execution.

Compensation is not an inverse-operation heuristic and is not implied by failure. When a consequential execution produces a verified divergence, Noema determines whether an explicit and permitted compensating Action exists. Where current enterprise state is material, that determination is grounded in State Reconciliation and Fact Status. The compensating Action then passes through the same deterministic Trust, Action Contract, execution, and verification boundaries as any other Action.

The core invariant is:

When execution produces an unacceptable partial or failed Outcome, Noema does not guess how to undo the world. It establishes whether an explicit, authorized compensating Action exists; if one does, it executes that Action through the same Trust and Contract boundaries as any other Action. If one does not, Noema escalates rather than inventing a recovery.

Compensation addresses execution divergence. It does not rewrite Intent, erase execution history, or become the source of truth for enterprise Business State.