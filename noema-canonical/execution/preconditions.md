Preconditions

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/preconditions.md

⸻

1. Definition

A precondition is an explicit, evaluable condition that must be established before an Action may safely and validly execute.

Preconditions answer:

“What must be established before this Action may execute?”

The canonical relationship is:

Preconditions
      ↓
Action
      ↓
Execution
      ↓
Postconditions
      ↓
Outcome

A precondition is therefore an execution-entry condition, not a prediction about what will happen afterward.

⸻

2. Core Principle

Noema must not execute an Action merely because the Action is valid in the abstract.

The conditions required for that specific execution must also hold at the appropriate execution boundary.

An Action may have been:

* planned;
* structurally valid;
* associated with a valid Action Contract;
* permitted by a prior Trust decision;

and still be unsafe or invalid to execute because a required runtime condition is no longer satisfied.

Therefore:

Action Validity
      ≠
Current Execution Eligibility

⸻

3. Why Preconditions Exist

Consider:

Action:
issue_replacement_card(customer_123)

The Action may require:

customer.status = ACTIVE
card.status = LOST
replacement_eligibility = TRUE

If the card has already been replaced:

card.status = REPLACED

the Action should not execute merely because the original Plan was valid.

Current state invalidates the relevant precondition.

⸻

4. Preconditions Are Runtime Guards

Preconditions protect the boundary between planning and execution.

Plan
  ↓
Action
  ↓
Precondition Evaluation
  ↓
┌───────────────┐
│               │
PASS           FAIL / UNKNOWN
│               │
▼               ▼
Continue       Stop / Reconcile

A precondition check is therefore part of execution eligibility.

It is not merely documentation attached to an Action.

⸻

5. Preconditions vs Intent

Intent expresses:

What the source of Intent wants to accomplish.

A precondition expresses:

What must be established for a particular Action to safely realize that Intent.

Example:

Intent:
"Renew my card."
Precondition:
customer account is active.

The precondition does not become part of the user’s Intent.

It belongs to the Action and its execution semantics.

⸻

6. Preconditions vs Constraints

These concepts are related but distinct.

Constraint

A restriction on what may be done.

refund <= ₦10,000,000

Precondition

A condition that must currently hold before a particular Action executes.

refund.request.status = APPROVED

A Constraint may establish or require a precondition.

They are not synonymous.

⸻

7. Preconditions vs Authorization

Authorization answers:

“Is this Actor permitted to perform this Action?”

A precondition answers:

“Is the relevant state currently suitable for this Action?”

Both may be required.

Authorization = PASS
Preconditions = SATISFIED
          ↓
       Execute

Failure of either required gate prevents consequential execution.

Authorization remains distinct from resource-state and execution preconditions.

⸻

8. Preconditions vs Policy

Policy defines rules governing permissible behavior.

A policy may establish a required precondition.

Example:

Policy:
refunds above ₦1m require manager approval.

Resulting precondition:

manager_approval.status = APPROVED

Policy remains authoritative.

The Planner or executor must not silently remove a policy-derived precondition.

⸻

9. Preconditions vs Postconditions

The distinction is fundamental.

PRECONDITION
What must already be established
        ↓
      ACTION
        ↓
POSTCONDITION
What should be established afterward

Example:

Precondition:
card.status = LOST
Action:
issue_replacement_card
Postcondition:
replacement_card.status = ACTIVE

A precondition protects entry into execution.

A postcondition verifies the expected effect afterward.

⸻

10. Preconditions Must Be Explicit

A consequential Action should not depend on hidden assumptions.

Bad:

issue_refund()

with the executor silently assuming:

payment exists
payment is refundable
refund has not already occurred

Better:

Preconditions:
payment.exists
payment.refundable
refund.status = NOT_ISSUED

Hidden assumptions are not deterministic execution conditions.

⸻

11. Preconditions Are Declarative

Where possible, preconditions should be represented as explicit predicates.

Conceptually:

account.status == ACTIVE

rather than:

"the account should probably be active"

The latter is not a deterministic execution condition.

⸻

12. Preconditions Must Be Evaluatable

A precondition should have a defined evaluation mechanism.

For example:

account.status == ACTIVE

can be evaluated against authoritative account state.

A vague condition such as:

customer seems eligible

is not sufficiently precise for consequential execution.

Where a condition cannot be deterministically evaluated, the system must preserve that uncertainty rather than manufacture a Boolean result.

⸻

13. Preconditions and Evidence

Evaluation requires evidence or an applicable authoritative state observation.

Precondition
     ↓
Evidence / Observation
     ↓
Evaluation

Example:

Precondition:
account.status = ACTIVE
Evidence:
Account Service
account_123.status = ACTIVE
Result:
SATISFIED

Evidence must be relevant to the exact claim being evaluated.

⸻

14. Precondition Evaluation States

A precondition should not be limited to a binary model.

Conceptually:

SATISFIED
NOT_SATISFIED
UNKNOWN

This is important because:

UNKNOWN ≠ NOT_SATISFIED

If Noema cannot establish whether a safety-critical condition holds, it must not assume that the condition is satisfied.

⸻

15. Unknown Preconditions

Suppose:

Precondition:
account.balance >= ₦100,000

but the authoritative account service is unavailable.

Noema cannot establish:

TRUE

The correct evaluation is:

UNKNOWN

For consequential Actions:

UNKNOWN
   ↓
do not execute

unless the Action Contract explicitly defines a safe execution semantics under that uncertainty.

Any such behavior must be explicit and deterministic.

⸻

16. Preconditions as Safety Gates

For high-consequence Actions, an unknown required precondition should generally behave as blocked.

UNKNOWN
   ↓
BLOCK

This follows the deterministic safety principle:

Absence of sufficient evidence is not evidence that the condition is satisfied.

BLOCKED, REQUIRES_REVALIDATION, or similar values are execution/control states, not additional Trust outcomes.

⸻

17. Preconditions and Freshness

A previously verified precondition may become stale.

Example:

10:00
account.status = ACTIVE

At:

10:05
account.status = SUSPENDED

A cached ACTIVE result cannot necessarily authorize execution at 10:05.

Preconditions may therefore require explicit freshness guarantees.

Freshness is claim-specific and Action-specific.

⸻

18. Time-Sensitive Preconditions

Some conditions are valid only within a time window.

Example:

approval.created_at < 15 minutes ago

or:

market.is_open = TRUE

The execution boundary must evaluate such conditions at the relevant time.

The applicable temporal semantics must be explicit.

⸻

19. Preconditions and Fact Status

Precondition evaluation must remain distinct from Fact Status.

Fact Status describes the status of a particular claim:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

It does not itself mean:

precondition = SATISFIED

For example:

Fact Status:
VERIFIED
Observed:
account.status = SUSPENDED
Precondition:
account.status = ACTIVE
Result:
NOT_SATISFIED

A verified fact can establish that a precondition is false.

Likewise, an UNKNOWN fact may result in an UNKNOWN precondition.

Fact Status is not Evidence, Precondition Result, Execution Status, or Outcome.

⸻

20. Hard Schema Validation and Admission

External system responses, events, provider messages, retrieved enterprise data, and model-generated candidate information are not canonical execution inputs merely because they contain expected fields.

Before information can be used as structured evidence for a consequential precondition, it must pass the relevant schema validation and admission boundary.

External / Model Input
        ↓
Hard Schema Validation
        ↓
Admission / Semantic Validation
        ↓
Evidence / Observation
        ↓
State Reconciliation where required
        ↓
Precondition Evaluation

Persistence does not confer authority.

The model cannot bypass this boundary.

⸻

21. Preconditions and State Reconciliation

Current enterprise state may be distributed across systems, eventually consistent, stale, or contradictory.

State Reconciliation is therefore a first-class mechanism for establishing the state required by a precondition.

Enterprise Systems
      ↓
Observations
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Reconciled Claims / Fact Status
      ↓
Precondition Evaluation

Noema must not treat a cached, inferred, or partially observed state as current authoritative state merely because it is available.

⸻

22. Preconditions and Race Conditions

A major execution problem is:

check precondition
      ↓
precondition passes
      ↓
state changes
      ↓
execute Action

Example:

Check:
balance >= ₦100,000
Balance changes:
balance = ₦20,000
Charge:
₦100,000

A precondition observation alone does not guarantee safety if the underlying state can change before the mutation.

⸻

23. Atomic Preconditions

Where necessary, the precondition and mutation should be enforced atomically.

For example:

UPDATE account
SET balance = balance - 100000
WHERE id = 123
AND balance >= 100000

The exact implementation is domain-specific.

The principle is:

When a precondition protects against a concurrent state change, the enforcement boundary must prevent a time-of-check/time-of-use race.

The authoritative enterprise system or execution consumer may provide the atomic enforcement boundary.

⸻

24. Preconditions and Concurrency

Two executions may independently satisfy the same precondition.

Example:

Action A:
withdraw ₦100,000
Action B:
withdraw ₦100,000

Both observe:

balance >= ₦100,000

Without concurrency control, both may execute.

Therefore preconditions must be considered alongside:

* transactions;
* optimistic concurrency;
* resource versions;
* conditional writes;
* locking where appropriate;
* reservations or leases where appropriate;
* atomic enterprise operations.

⸻

25. Resource Preconditions

Many preconditions concern Resources.

Example:

Action:
delete_file(file_123)
Preconditions:
file_123.exists
actor_can_delete(file_123)

The Resource identity must be explicit.

A generic condition such as:

file.exists

is insufficient where multiple Resources could satisfy it.

⸻

26. State Preconditions

A precondition may require a specific Resource state.

Example:

Action:
capture_payment(payment_123)
Precondition:
payment_123.status = AUTHORIZED

If:

payment_123.status = CAPTURED

the Action must not be executed again unless its semantics explicitly permit an already-captured state.

⸻

27. Relationship Preconditions

An Action may require a relationship to exist.

Example:

Action:
remove_user_from_team

Precondition:

user_123 ∈ team_456.members

If the relationship does not exist, the Action may be invalid or already satisfied depending on the Action semantics.

That distinction must be explicit.

⸻

28. Capability Preconditions

Execution may require a registered Capability.

Example:

Action:
provision_server

Required capability:

server_provisioning

If no compatible Capability and Action Contract path exists:

NO_EXECUTABLE_PATH

rather than speculative execution.

Capability availability does not itself grant authority.

⸻

29. Authorization Preconditions

Authorization may be represented as an execution gate, but authorization and ordinary state preconditions remain distinct.

Example:

authorization = APPROVED

must be evaluated through the applicable authorization and Trust semantics.

Noema distinguishes:

* technical authorization;
* policy authorization;
* business authorization.

An authorization result is not merely another arbitrary Resource-state predicate.

⸻

30. Human Approval Preconditions

Some Actions require explicit human approval.

Example:

Action:
issue_refund(₦20,000,000)
Required:
finance_manager_approval = APPROVED

The Planner may identify this requirement.

The approval must be established through the defined human-intervention and authority mechanisms before execution.

A human identity alone does not establish authorization.

⸻

31. Evidence Preconditions

An Action may require specific evidence to exist.

Example:

Action:
approve_claim
Preconditions:
identity_verified
required_documents_verified
fraud_screening_completed

These conditions must be established through the applicable Evidence, State Reconciliation, and Trust mechanisms.

The existence of a document or model assertion does not automatically establish verification.

⸻

32. Policy-Derived Preconditions

Policies may dynamically establish required execution conditions.

Example:

Policy:
international_transfer > threshold
requires enhanced verification

The Action may therefore require:

enhanced_verification.status = COMPLETE

The executor must not bypass this requirement because the original Plan did not explicitly include it.

Policy-derived requirements must remain traceable to the applicable policy version.

⸻

33. Preconditions and Planning

Planning should identify known preconditions and use them to establish dependencies.

Example:

Plan:
verify_account
    ↓
issue_card

The dependency may arise because:

issue_card.precondition:
account_verified = TRUE

Planning may use preconditions to construct Action ordering.

Planning does not establish that the preconditions are currently satisfied.

⸻

34. Preconditions and Dynamic State

Planning happens at one point in time.

Execution may happen later.

Therefore:

Plan-time assessment
        ≠
Execution-time satisfaction

A Plan can establish:

“This Action is potentially executable under the inputs and assumptions known at planning time.”

The execution boundary must still verify conditions that are required to hold when execution occurs.

⸻

35. Precondition Revalidation

For mutable or high-risk Resources:

Plan
 ↓
Precondition assessment
 ↓
wait
 ↓
Execution
 ↓
Precondition revalidation
 ↓
Execute

The required degree of revalidation depends on:

* Action risk;
* state volatility;
* time elapsed;
* freshness requirements;
* concurrency model;
* policy;
* Action Contract semantics.

A previous successful evaluation does not automatically remain valid.

⸻

36. Preconditions and Action Contracts

An Action Contract should be capable of expressing relevant preconditions.

Conceptually:

ActionContract {
    action
    inputs
    preconditions[]
    authorization
    idempotency
    postconditions[]
    verification
}

The Action Contract defines the executable semantic boundary.

The exact schema remains defined in contracts/action-contract.md.

⸻

37. Preconditions and Idempotency

Idempotent execution does not eliminate preconditions.

A retry may encounter different state.

Example:

First attempt:
precondition = SATISFIED
execution = UNKNOWN

After reconciliation:

payment.status = SETTLED

A retry should not execute merely because the original precondition was satisfied.

Current state and current Action semantics must be evaluated.

⸻

38. Preconditions and Retries

A retry is a new execution attempt of the same semantic Action.

Therefore the system should determine:

Are the required runtime preconditions still satisfied?

before retrying.

A previous successful precondition evaluation does not automatically remain valid.

If the Action has materially changed, it is a new semantic Action and requires its own evaluation and execution identity.

⸻

39. Preconditions and Postconditions

A postcondition from one Action may become a precondition for another.

Example:

Action A:
verify_identity
Postcondition:
identity.status = VERIFIED

Then:

Action B:
open_account
Precondition:
identity.status = VERIFIED

This creates:

A.postcondition
       ↓
B.precondition

This relationship is one of the mechanisms through which execution Plans establish ordering.

⸻

40. Preconditions and State Transitions

An Action can be modeled as:

State S
   │
   │ preconditions satisfied
   ▼
Action
   │
   ▼
State S'
   │
   │ postconditions evaluated
   ▼
Outcome

The Action is therefore a controlled transition attempt.

The resulting enterprise Business State remains owned by the relevant enterprise authority.

⸻

41. Preconditions and State Machine Validity

For a Resource state machine:

PENDING
   ↓
ACTIVE
   ↓
SUSPENDED

an Action such as:

activate_resource

may have:

precondition:
state = PENDING

If the Resource is already:

ACTIVE

the Action may be:

* invalid;
* already satisfied;
* a no-op;

depending on the explicit Action semantics.

This must not be inferred implicitly.

⸻

42. Preconditions and Natural Idempotency

An Action can be idempotent while still having preconditions.

Example:

Action:
set_status(ACTIVE)
Precondition:
resource.exists

Repeated execution may remain safe, but the Resource must still exist.

Whether an already-active Resource satisfies the Action must be determined by the Action semantics.

⸻

43. Preconditions and Composite Actions

A composite Action may have:

* Action-level preconditions;
* step-level preconditions;
* branch-specific preconditions.

Example:

Renew Card
 ├── verify eligibility
 ├── issue replacement
 └── activate replacement

issue replacement may require:

eligibility = TRUE

while activate replacement may require:

replacement exists
replacement.status = ISSUED

The dependencies must be explicit.

⸻

44. Preconditions and Conditional Plans

A precondition can determine which execution path is valid.

Check eligibility
      │
 ┌────┴────┐
 │         │
TRUE      FALSE
 │         │
 ▼         ▼
Issue     Stop

The Plan may encode the branch.

Execution evaluates the actual condition from admitted evidence and current state.

A model must not predict the branch and treat the prediction as established state.

⸻

45. Preconditions and Failure

If a required precondition is false:

Precondition = NOT_SATISFIED

the Action should not execute.

This is not an execution failure.

The distinction is:

Precondition not satisfied
    →
Action was not eligible to execute
Execution failure
    →
Action was eligible and was attempted,
but execution failed

This distinction is important for recovery, audit, and metrics.

⸻

46. Preconditions and Intervention

A failed precondition may require human intervention.

Example:

refund_amount > approval_threshold
Required:
manager_approval = APPROVED

If approval is absent:

BLOCKED
   ↓
Human Intervention

The Action remains unexecuted unless the applicable intervention process establishes an allowed transition.

Human intervention does not automatically override the precondition.

⸻

47. Preconditions and Replanning

A failed precondition may invalidate the current Plan.

Example:

Plan:
issue_card
Precondition:
customer.eligible = TRUE

Runtime evaluation:

customer.eligible = FALSE

Possible result:

Action blocked
   ↓
Plan invalidated or re-evaluated
   ↓
Replan where permitted

The system must not blindly continue.

Replanning must account for the current reconciled state and any effects already produced.

⸻

48. Preconditions and Clarification

A missing precondition may sometimes indicate missing Intent information.

Example:

Action:
book_flight
Required:
destination

If destination is absent from the resolved Intent:

CLARIFY

may be required.

The Planner must not invent the missing value.

Clarification is an Intent-resolution mechanism, not a substitute for missing enterprise state.

⸻

49. Preconditions and Determinism

Precondition evaluation must be deterministic wherever the condition can be represented and evaluated deterministically.

Given:

same state
same evidence
same policy version
same evaluation rules
same relevant context

the result should be the same.

An LLM must not randomly decide that a safety-critical precondition “probably passes.”

⸻

50. LLM-Assisted Preconditions

An LLM may assist with extracting candidate facts from unstructured evidence.

Example:

Document
 ↓
LLM extraction
 ↓
"approval appears present"

This is candidate interpretation.

The authoritative execution condition must still be established through the deterministic admission, evidence, reconciliation, and Trust pipeline.

Candidate Interpretation
        ↓
Hard Schema Validation / Admission
        ↓
Evidence / Reconciliation
        ↓
Deterministic Evaluation

Model confidence is not Fact Status and is not sufficient authority for a consequential precondition.

⸻

51. Preconditions and External State

External systems may change independently of Noema.

Therefore a precondition involving external state should be evaluated against an authoritative or sufficiently fresh source.

Example:

inventory.available >= 1

must reflect current inventory where overselling is possible.

A stale cache must not silently satisfy the condition.

⸻

52. Preconditions and Transactions

When multiple preconditions protect a single atomic mutation, they may need to be enforced within the same transaction or equivalent atomic boundary.

Example:

balance >= amount
account.status = ACTIVE

followed by:

debit account

Checking these separately from the mutation can introduce race conditions.

The enterprise system or consumer may therefore need to enforce the conditions together with the mutation.

⸻

53. Preconditions and Optimistic Concurrency

A Resource version can be used as a precondition.

Example:

resource.version = 17

Action:

update_resource

If the current version is:

18

the Action should not overwrite the concurrent change.

Instead, the precondition fails or requires revalidation according to the Action Contract.

This provides an explicit concurrency boundary.

⸻

54. Preconditions and Atomicity

Where practical:

A precondition that protects the correctness of a state mutation should be enforced as close as possible to the mutation itself.

This minimizes:

time-of-check
      ↓
time-of-use

gaps.

Noema must distinguish an observational precondition check from an atomic enforcement guarantee.

⸻

55. Precondition Composition

Multiple preconditions may be composed.

Example:

P1 AND P2 AND P3

where:

P1 = account active
P2 = actor authorized
P3 = sufficient balance

All required predicates must be satisfied.

The composition semantics must be explicit.

⸻

56. Alternative Preconditions

Some Actions may allow alternative valid conditions.

Example:

P1 OR P2

For example:

verified_identity
OR
trusted_existing_session

The Action Contract or applicable policy must explicitly define the equivalence.

Noema must not invent alternative paths.

⸻

57. Precondition Evaluation Order

Where evaluation itself has cost or operational impact, the order may matter.

Example:

cheap local condition
       ↓
expensive external verification

However, evaluation order must not alter the semantic result.

Precondition evaluation should generally be observational and side-effect free.

⸻

58. Preconditions Should Be Side-Effect Free

A precondition check should generally observe state rather than mutate it.

Bad:

check_balance()

which itself reserves or deducts money.

Better:

observe_balance()

followed by the actual mutation under the appropriate atomicity guarantees.

If a resource reservation is itself required, it should be modeled as an explicit registered Action or capability with its own Trust, Contract, execution, idempotency, and postcondition semantics.

⸻

59. Preconditions and Observability

Every failed or unknown precondition should be observable.

The execution record should preserve:

precondition
evaluation result
evidence
Fact Status
evaluation time
reason

Example:

Precondition:
account.status = ACTIVE
Observed:
account.status = SUSPENDED
Result:
NOT_SATISFIED

This should be traceable to the relevant Resource and observation.

⸻

60. Preconditions and Auditability

A consequential Action should be explainable in terms of the conditions that allowed it to execute.

For example:

Why was this Action executed?
account.status = ACTIVE
authorization = APPROVED
resource.version = 17
required_policy_conditions = SATISFIED

The exact evidence, versions, and evaluation context should be traceable.

Auditability does not require exposing private model chain-of-thought.

⸻

61. Preconditions and Security

Preconditions must not be client-controlled facts.

Bad:

request.preconditions = {
    account_verified: true
}

A caller cannot establish their own authorization or safety conditions merely by asserting them.

The system must obtain the required evidence through approved enterprise interfaces and deterministic admission and evaluation boundaries.

⸻

62. Preconditions and Trust

Trust determines whether the resolved Action path may proceed under applicable authority, policy, evidence, and constraints.

Precondition evaluation is one input to that execution boundary.

Therefore:

claim exists
     ≠
claim is authoritative
     ≠
precondition satisfied
     ≠
Trust EXECUTE

A precondition may be satisfied only after the relevant evidence/state has passed the applicable validation, reconciliation, authority, and policy checks.

Trust remains distinct from the precondition predicate itself.

⸻

63. Preconditions and Authorization

A useful consequential execution gate is:

Admitted Intent
      AND
Resolved Action / Target
      AND
Applicable Trust Conditions
      AND
Required Authorization
      AND
Required Preconditions
      ↓
Action Contract
      ↓
Execute

The exact evaluation order may vary by implementation.

The semantic requirement does not:

Every required authorization and precondition must be satisfied at the appropriate execution boundary before consequential execution.

Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Values such as BLOCKED, REQUIRES_REVALIDATION, and WAITING_FOR_STATE are execution/control states, not Trust outcomes.

⸻

64. Preconditions and Postcondition Chains

Execution workflows can form chains:

A.postcondition
       ↓
B.precondition
B.postcondition
       ↓
C.precondition

Example:

verify_identity
       ↓
identity VERIFIED
       ↓
open_account
       ↓
account OPEN
       ↓
issue_card

Each dependency must be established from actual execution evidence or reconciled state.

The planner must not treat a planned predecessor as proof that its postcondition will occur.

⸻

65. Preconditions and Plan Validity

A Plan may be structurally valid while being runtime-infeasible.

Example:

Plan:
issue_card
Structural status:
VALID
Runtime:
customer.eligibility = FALSE

Therefore:

Action blocked
Plan may require re-evaluation or replanning

Plan validity and runtime execution eligibility remain distinct.

⸻

66. Preconditions and the Planner Boundary

The Planner may:

* identify known preconditions;
* construct dependencies from preconditions;
* select registered Actions whose preconditions can potentially be satisfied;
* propose verification or reconciliation steps.

The Planner may not:

* invent precondition values;
* declare unknown state satisfied;
* invent capabilities;
* invent authority;
* modify Action Contract semantics;
* bypass Trust;
* bypass State Reconciliation;
* treat model inference as authoritative state.

Planning is bounded by the:

Enterprise Action Graph
Capability Registry
Action Registry / Action Model
Action Contracts
Policies
Enterprise constraints
Reconciled state

⸻

67. Preconditions and the Execution Boundary

The execution boundary must distinguish:

Plan-time feasibility
        ↓
Action Contract validity
        ↓
Runtime precondition evaluation
        ↓
Authorization / Trust requirements
        ↓
Execution

A Plan cannot guarantee that a mutable condition remains satisfied until execution.

Where the Action Contract delegates a condition to a consumer or provider, that enforcement responsibility must be explicit.

⸻

68. Preconditions and Consumer Responsibility

The consumer executing an Action must enforce the preconditions assigned to it by the Action Contract.

Noema must not assume:

“The consumer probably checked it.”

The Contract must define responsibility.

A consumer-side enforcement result may itself require validation or authoritative observation before Noema treats it as evidence of the required condition.

⸻

69. Preconditions and Noema Responsibility

Noema is responsible for establishing the semantic conditions that it owns.

The consumer is responsible for execution-local conditions it owns.

The provider may enforce provider-specific constraints.

Conceptually:

Noema:
Intent / Trust / Policy / Contract validity
Consumer:
execution-local runtime invariants
Provider:
provider-specific execution constraints

These boundaries should be explicit.

⸻

70. Preconditions and Contract Boundaries

A precondition belongs at the layer that can actually enforce it.

For example:

Noema:
authorization requirement satisfied
Consumer:
resource.version = 17
Provider:
payment instrument valid

Conditions may be duplicated for defense in depth, but ownership and enforcement responsibility must remain clear.

⸻

71. Preconditions and Long-Running Actions

For long-running Actions, a precondition may be valid at start but cease to hold during execution.

Example:

Action:
provision infrastructure
Start precondition:
account remains authorized

If authorization is revoked during execution, the Execution Model must define whether the Action:

* continues;
* pauses;
* terminates;
* requires intervention;
* requires compensation.

This is not solved by the initial precondition check alone.

⸻

72. Start Preconditions vs Continuous Invariants

This distinction is useful.

Start precondition

Must be true before execution begins.

account.status = ACTIVE

Continuous invariant

Must remain true throughout execution.

authorization remains valid

Not every precondition must be continuously enforced.

The Action Contract should define the distinction where necessary.

⸻

73. Preconditions and Side Effects

An Action must not produce consequential side effects before required preconditions have been satisfied.

Bad:

begin payment
 ↓
check authorization

Correct:

check authorization
 ↓
check required preconditions
 ↓
execute payment

Where the external operation atomically validates the relevant conditions, that boundary may serve as the authoritative enforcement point.

⸻

74. Preconditions and Idempotent State

For naturally idempotent Actions:

set_status(ACTIVE)

the precondition may permit:

status = ACTIVE

depending on whether the Action means:

“Make active”

rather than:

“Transition from PENDING to ACTIVE.”

The semantic distinction must be explicit in the Action Model and Action Contract.

⸻

75. Preconditions and Action Semantics

Two Actions with similar names may have different preconditions.

For example:

activate_card

could mean:

requires:
card.status = ISSUED

while:

ensure_card_active

could mean:

requires:
card.exists

and succeed if the card is already active.

Action semantics determine precondition semantics.

Noema must not infer equivalence from names.

⸻

76. Preconditions and Failure Classification

A useful distinction is:

PRECONDITION_NOT_SATISFIED

means:

The Action cannot currently execute under its Contract.

EXECUTION_FAILED

means:

The Action was eligible and attempted, but execution failed.

POSTCONDITION_NOT_SATISFIED

means:

Execution occurred, but the required effect was not established.

UNKNOWN

means:

The system cannot currently establish the relevant state or execution result.

These states must remain semantically distinct.
⸻
## 77. Preconditions and Recovery
Recovery depends on why the precondition failed.
Example:
```text
balance insufficient

may require:

WAIT

while:

authorization revoked

may require:

ESCALATE

and:

resource deleted

may require:

REPLAN

No universal retry policy should be applied to precondition failures.

⸻

78. Preconditions and Safety

For high-risk Actions:

UNKNOWN

should normally result in:

BLOCK

or:

REQUIRES_REVALIDATION

For low-risk or read-only Actions, the Contract may permit a different behavior.

The Action’s consequence and risk profile therefore influence how unknown preconditions are handled.

⸻

79. Preconditions and Read Actions

Not every Action requires mutation-level preconditions.

Example:

get_account_balance

may require:

account exists
actor authorized to read

The precondition model should remain proportionate to the Action’s consequences.

Read-only does not mean non-consequential. Access to protected information may itself require Trust and strict preconditions.

⸻

80. Preconditions and Write Actions

State-changing Actions generally require stronger preconditions.

Example:

delete_account

may require:

account exists
actor authorized
account has no blocking dependencies
retention policy permits deletion

The exact requirements are domain-specific and must be explicit.

⸻

81. Preconditions and External APIs

A provider API may have its own preconditions.

Example:

Provider:
capture payment only if payment.status = AUTHORIZED

Noema should model this requirement where it is relevant to safe execution.

Provider-side enforcement may ultimately be authoritative for the provider-owned state.

The provider response remains subject to the applicable validation and evidence semantics.

⸻

82. Preconditions and Reconciliation After Uncertainty

If execution or precondition state becomes uncertain:

UNKNOWN

Noema should reconcile the relevant state before taking a consequential next step where possible.

UNKNOWN
   ↓
Observe authoritative systems
   ↓
Hard Schema Validation / Admission
   ↓
State Reconciliation
   ↓
Re-evaluate Preconditions
   ↓
Continue / Replan / Escalate / Reject

Noema must not resolve uncertainty by guessing.

⸻

83. Preconditions and Intent Versioning

Consequential precondition evaluations must retain the exact immutable Intent Object version associated with the Action.

Intent v1
   ↓
Resolved Action
   ↓
Precondition Evaluation
   ↓
Execution

If the semantic request materially changes:

Intent v1
   ↓
supersedes
Intent v2

the new Intent version must be evaluated independently.

A precondition evaluation from Intent v1 must not silently become evidence for Intent v2.

⸻

84. Preconditions and Audit Versioning

A consequential precondition evaluation should preserve the relevant semantic versions, including where applicable:

Intent Version
Action Version
Action Contract Version
Trust Decision Version
Policy Version
EAG / Capability Version
Integration Version
System / Provider Version
Resource Version
Precondition / Evaluation Rule Version

This allows historical execution eligibility to remain interpretable even as current configuration evolves.

⸻

85. Preconditions and Replay

Replay of precondition evaluation is non-executing by default.

Replay must not:

* create a new Action execution;
* recreate business side effects;
* silently alter historical precondition results;
* treat current state as if it were the historical state.

A historical evaluation remains associated with its original evidence, observations, state snapshot, versions, and evaluation context.

A modern reevaluation is a distinct operation.

⸻

86. Preconditions and Operational Memory

Precondition evaluations may contribute to Operational Memory.

Operational Memory may retain:

* recurring precondition failures;
* historical evaluations;
* reconciliation history;
* execution context;
* recovery patterns.

Operational Memory is not:

* enterprise Business State;
* authoritative current Resource state;
* a replacement for Evidence;
* a replacement for State Reconciliation;
* generic model memory.

Historical satisfaction does not establish current satisfaction.

⸻

87. Canonical Precondition Flow

The canonical flow is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolve Actor / Action / Target / Resource
      ↓
Context / State Reconciliation
      ↓
Trust Constraints / Decision
      ↓
Action Graph / Planning
      ↓
Action Contract
      ↓
Runtime Preconditions
      ↓
Authorization / Required Trust Conditions
      ↓
Execution
      ↓
Postconditions
      ↓
Verification / Reconciliation
      ↓
Outcome

For a mutable or consequential Action:

Plan-time Assessment
      ↓
Runtime Revalidation
      ↓
Preconditions Satisfied
      ↓
Atomic / Controlled Execution Boundary
      ↓
Postcondition Verification

The exact ordering of Trust and individual precondition checks may vary by implementation, but no consequential Action may execute without satisfying its required semantic gates.

⸻

88. Causal Audit Chain

A consequential execution should preserve the relationship:

Source of Intent
      ↓
Intent Version
      ↓
Resolution
      ↓
Reconciled State / Evidence
      ↓
Trust Decision
      ↓
Action / Action Instance
      ↓
Action Contract
      ↓
Precondition Evaluation
      ↓
Execution Attempt
      ↓
Observation / Verification
      ↓
Postcondition Evaluation
      ↓
Outcome

This provides causal traceability for why an Action was considered eligible and what subsequently happened.

⸻

89. Preconditions Invariants

Invariant 1

An Action must not execute when a required precondition is not satisfied.

Invariant 2

UNKNOWN must not be treated as SATISFIED for consequential Actions unless the Action Contract explicitly defines a safe deterministic behavior under that uncertainty.

Invariant 3

Preconditions must be explicit and evaluable.

Invariant 4

Preconditions must be evaluated against sufficient evidence, observation, or reconciled state.

Invariant 5

Precondition evaluation must be deterministic where the underlying condition is deterministic.

Invariant 6

Fact Status must remain distinct from Precondition Result, Evidence, Execution Status, and Outcome.

Invariant 7

A precondition snapshot records what was established at a point in time; it does not guarantee that the condition remains true.

Invariant 8

Time-sensitive preconditions must respect their freshness or validity window.

Invariant 9

Preconditions must not be satisfied merely by caller assertion.

Invariant 10

External or model-generated information must pass the relevant schema validation and admission boundary before becoming eligible canonical input to consequential precondition evaluation.

Invariant 11

State Reconciliation must be used where distributed, stale, conflicting, or uncertain enterprise state prevents sufficiently authoritative evaluation.

Invariant 12

Preconditions must not silently replace authorization or policy evaluation.

Invariant 13

Authorization and preconditions are distinct execution gates.

Invariant 14

Where race conditions are possible, preconditions protecting mutations must be enforced atomically or with appropriate concurrency control.

Invariant 15

A failed precondition is distinct from an execution failure.

Invariant 16

A failed precondition must not automatically trigger retry.

Invariant 17

Retries must re-evaluate relevant runtime preconditions.

Invariant 18

A postcondition from one Action may establish a precondition for another Action.

Invariant 19

A materially changed Action requires its own precondition evaluation.

Invariant 20

Precondition failures and unknown evaluations must be observable and auditable.

Invariant 21

Preconditions must be evaluated and enforced at the layer responsible for them.

Invariant 22

Noema must not invent missing precondition values from ambiguous Intent or model inference.

Invariant 23

The Planner may identify and compose preconditions but cannot declare them satisfied or invent the authority required to satisfy them.

Invariant 24

A Plan’s structural validity does not guarantee runtime precondition satisfaction.

Invariant 25

Trust EXECUTE does not guarantee that runtime preconditions will remain satisfied until execution.

Invariant 26

A precondition evaluation must preserve the exact Intent version associated with the consequential Action.

Invariant 27

Resolved Actor, Action, Target, Resource, scope, and resolution identity must remain traceable through consequential precondition evaluation.

Invariant 28

A cache or historical observation must not satisfy a current precondition without sufficient authority and freshness.

Invariant 29

Conflicting evidence must not be resolved through arbitrary source selection.

Invariant 30

A precondition check must not be treated as an atomic mutation guarantee unless the relevant enforcement boundary actually provides that guarantee.

Invariant 31

Precondition semantics must be versioned where their meaning can change.

Invariant 32

Historical precondition evaluations must remain interpretable under the semantic versions used when they were established.

Invariant 33

Replay must not recreate execution side effects or silently alter historical precondition evaluations.

Invariant 34

Operational Memory may preserve precondition history but must not become authoritative enterprise state.

Invariant 35

Read-only Actions may have consequential preconditions when their information access or downstream effects are consequential.

Invariant 36

Noema must not convert uncertainty about a required precondition into a satisfied condition merely to continue execution.

⸻

90. Canonical Mental Model

                         ACTION
                            │
                            ▼
                   PRECONDITION SET
                            │
                            ▼
              HARD VALIDATION / ADMISSION
                            │
                            ▼
                  STATE RECONCILIATION
                            │
                            ▼
                 PRECONDITION EVALUATION
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         SATISFIED      NOT SATISFIED   UNKNOWN
              │             │             │
              ▼             ▼             ▼
       TRUST / AUTH      BLOCK /        BLOCK /
       CONDITIONS       REPLAN         RECONCILE
              │
              ▼
          EXECUTION
              │
              ▼
       POSTCONDITIONS
              │
        ┌─────┼─────┐
        ▼     ▼     ▼
    SATISFIED FALSE UNKNOWN
        │      │      │
        ▼      ▼      ▼
      OUTCOME RECOVERY RECONCILE /
                       INTERVENE

Across Actions:

Action A
   │
   └── Postcondition A
             │
             ▼
       Precondition B
             │
             ▼
          Action B

The critical distinction is:

Planned
   ≠
Structurally Valid
   ≠
Currently Eligible
   ≠
Authorized
   ≠
Executed
   ≠
Successfully Verified

⸻

91. Final Definition

A precondition is an explicit, versioned, evaluable condition that must be established before an Action may execute safely and validly.

Preconditions protect the execution boundary from stale state, invalid assumptions, missing authority, policy violations, concurrency races, and unsafe state transitions. They are evaluated against sufficient evidence and, where required, reconciled enterprise state, while remaining distinct from Intent, Constraints, Authorization, Trust, Execution Status, Postconditions, and Outcome.

The core invariant is:

Noema does not execute an Action because a Plan says it should. It executes only when the Action’s required semantic gates and runtime preconditions are satisfied at the appropriate execution boundary.

If a required condition is false or cannot be established, Noema stops, reconciles, revalidates, intervenes, or replans according to explicit semantics rather than guessing.