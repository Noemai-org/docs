Preconditions

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: 04-execution/preconditions.md

⸻

1. Definition

A precondition is an explicit condition that must hold before an Action may safely and validly execute.

Preconditions answer:

“What must be true before we allow this Action to happen?”

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

A precondition is therefore an entry condition for execution, not a prediction about what will happen afterward.

⸻

2. Core Principle

Noema must not execute an Action merely because the Action is valid in the abstract. The conditions required for that specific execution must also hold at the execution boundary.

An Action may have been:

planned
authorized
contractually valid

and still be unsafe to execute because a required precondition is no longer true.

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

the Action should not execute merely because the original plan was valid.

The current state invalidates the precondition.

⸻

4. Preconditions Are Runtime Guards

Preconditions protect the boundary between:

planning

and:

execution

Conceptually:

Plan
  ↓
Action
  ↓
Precondition Evaluation
  ↓
┌───────────────┐
│               │
PASS           FAIL
│               │
▼               ▼
Execute       Stop

⸻

5. Preconditions vs Intent

Intent expresses:

What the user wants.

A precondition expresses:

What must be true for an Action to safely realize that Intent.

Example:

Intent:
"Renew my card."
Precondition:
customer account is active.

The precondition does not become part of the user’s Intent.

⸻

6. Preconditions vs Constraints

These concepts are related but distinct.

Constraint

A restriction on what may be done.

refund <= ₦10,000,000

Precondition

A condition that must currently hold before a particular Action executes.

refund.request.status = APPROVED

A Constraint may generate a required precondition.

But they are not synonymous.

⸻

7. Preconditions vs Authorization

Authorization answers:

“Is this Actor permitted to perform this Action?”

A precondition answers:

“Is the world currently in the state required for this Action?”

Both may be required.

Authorization = PASS
Preconditions = PASS
          ↓
       Execute

Either failing is sufficient to block execution.

⸻

8. Preconditions vs Policy

Policy defines rules governing permissible behavior.

A policy may establish a precondition.

Example:

Policy:
refunds above ₦1m require manager approval.

Resulting Action precondition:

manager_approval.status = APPROVED

Policy remains authoritative.

⸻

9. Preconditions vs Postconditions

The distinction is fundamental.

PRECONDITION
What must already be true
        ↓
      ACTION
        ↓
POSTCONDITION
What should become true

Example:

Precondition:
card.status = LOST
Action:
issue_replacement_card
Postcondition:
replacement_card.status = ACTIVE

⸻

10. Preconditions Must Be Explicit

A consequential Action should not depend on hidden assumptions.

Bad:

issue_refund()

with an executor silently assuming:

payment exists
payment is refundable
refund has not already occurred

Better:

Preconditions:
payment.exists
payment.refundable
refund.status = NOT_ISSUED

⸻

11. Preconditions Are Declarative

Where possible, preconditions should be represented as explicit predicates.

Conceptually:

Precondition:
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

⸻

13. Preconditions and Evidence

Evaluation requires evidence.

Precondition
     ↓
Evidence
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

⸻

14. Precondition Evaluation States

A precondition should not be limited to a binary model.

Conceptually:

SATISFIED
NOT_SATISFIED
UNKNOWN

This is important because:

UNKNOWN ≠ NOT_SATISFIED

If the system cannot establish whether a safety-critical condition holds, it should not assume that it does.

⸻

15. Unknown Preconditions

Suppose:

Precondition:
account.balance >= ₦100,000

but the account service is unavailable.

Noema cannot establish:

TRUE

The correct state is:

UNKNOWN

For consequential Actions:

UNKNOWN
   ↓
do not execute

unless the Action Contract explicitly defines safe behavior under uncertainty.

⸻

16. Preconditions as Safety Gates

For high-consequence Actions:

UNKNOWN

should generally behave as:

BLOCKED

rather than:

PROCEED

This follows Noema’s broader deterministic safety principle:

Absence of sufficient evidence is not evidence that the condition is satisfied.

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

Preconditions may therefore require freshness guarantees.

⸻

18. Time-Sensitive Preconditions

Some conditions are valid only within a time window.

Example:

approval.created_at < 15 minutes ago

or:

market.is_open = TRUE

The execution boundary must evaluate such conditions at the relevant time.

⸻

19. Preconditions and Race Conditions

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

A precondition check alone does not guarantee safety if the underlying state can change before execution.

⸻

20. Atomic Preconditions

Where necessary, the precondition and mutation should be enforced atomically.

For example:

UPDATE account
SET balance = balance - 100000
WHERE id = 123
AND balance >= 100000

The exact implementation is domain-specific.

The principle is:

When a precondition protects against a concurrent state change, the enforcement boundary must prevent a time-of-check/time-of-use race.

⸻

21. Preconditions and Concurrency

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

locking
transactions
optimistic concurrency
version checks
atomic operations

where appropriate.

⸻

22. Resource Preconditions

Many preconditions concern Resources.

Example:

Action:
delete_file(file_123)
Preconditions:
file_123.exists
actor_can_delete(file_123)

The Resource identity must be explicit.

⸻

23. State Preconditions

A precondition may require a specific Resource state.

Example:

Action:
capture_payment(payment_123)
Precondition:
payment_123.status = AUTHORIZED

If:

payment_123.status = CAPTURED

the Action must not be executed again unless the contract explicitly permits it.

⸻

24. Relationship Preconditions

An Action may require a relationship to exist.

Example:

Action:
remove_user_from_team

Precondition:

user_123 ∈ team_456

If the relationship does not exist, the Action may be invalid or already satisfied depending on its semantics.

That distinction should be explicit.

⸻

25. Capability Preconditions

Execution may require a Capability.

Example:

Action:
provision_server

Precondition:

provisioning capability available

If no compatible consumer exists:

NO_EXECUTABLE_PATH

rather than speculative execution.

⸻

26. Authorization Preconditions

Authorization itself may be modeled as an execution gate.

Example:

Precondition:
authorization.status = APPROVED

However, authorization remains conceptually distinct from ordinary resource-state preconditions.

The Trust subsystem is authoritative for authorization.

⸻

27. Human Approval Preconditions

Some Actions require explicit human approval.

Example:

Action:
issue_refund(₦20,000,000)
Precondition:
finance_manager_approval = APPROVED

The planner may identify this requirement.

The approval itself must be established before execution.

⸻

28. Evidence Preconditions

An Action may require evidence to exist.

Example:

Action:
approve_claim
Preconditions:
identity_verified
required_documents_verified
fraud_screening_completed

These conditions must be established through the Evidence and Trust systems.

⸻

29. Policy-Derived Preconditions

Policies may dynamically create preconditions.

Example:

Policy:
international_transfer > threshold
requires enhanced verification

The Action may therefore require:

enhanced_verification.status = COMPLETE

The executor should not bypass this requirement because the original plan did not include it.

⸻

30. Preconditions and Planning

Planning should identify known preconditions.

Example:

Plan:
verify_account
    ↓
issue_card

The dependency may arise because:

issue_card.precondition:
account_verified = TRUE

Planning can therefore use preconditions to establish Action ordering.

⸻

31. Preconditions and Dynamic State

Planning happens at one point in time.

Execution happens later.

Therefore:

Plan-time precondition

and:

Execution-time precondition

must be distinguished.

A plan can establish:

"this Action is potentially executable"

but the execution boundary must verify conditions that are required to hold at execution time.

⸻

32. Precondition Revalidation

For mutable or high-risk Resources:

Plan
 ↓
Precondition check
 ↓
wait
 ↓
Execution
 ↓
Precondition recheck
 ↓
Execute

The required degree of revalidation depends on the Action’s risk and state volatility.

⸻

33. Preconditions and Action Contracts

An Action Contract should be capable of expressing relevant preconditions.

Conceptually:

ActionContract {
    action
    inputs
    preconditions[]
    authorization
    idempotency
    postconditions[]
}

The contract defines the executable boundary.

⸻

34. Preconditions and Idempotency

Idempotent execution does not eliminate preconditions.

A retry may encounter different state.

Example:

First attempt:
precondition = PASS
execution = UNKNOWN

After reconciliation:

payment.status = SETTLED

A retry should not execute merely because the original precondition was satisfied.

Current state must be evaluated against the Action’s semantics.

⸻

35. Preconditions and Retries

A retry is a new execution attempt of the same semantic Action.

Therefore the system should determine:

Are the required preconditions still valid?

before retrying.

A previous successful precondition evaluation does not automatically remain valid.

⸻

36. Preconditions and Postconditions

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

This creates a dependency:

A.postcondition
        ↓
B.precondition

This is one of the core mechanisms by which execution plans become ordered.

⸻

37. Preconditions and State Transitions

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

The Action is therefore a controlled state transition.

⸻

38. Preconditions and State Machine Validity

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

invalid

or:

already satisfied

depending on the Action semantics.

This must not be inferred implicitly.

⸻

39. Preconditions and Natural Idempotency

An Action can be idempotent while still having preconditions.

Example:

Action:
set_status(ACTIVE)

Precondition:

resource.exists

Repeated execution may remain safe, but the Resource must still exist.

⸻

40. Preconditions and Composite Actions

A composite Action may have:

Action-level preconditions

and:

Step-level preconditions

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

⸻

41. Preconditions and Conditional Plans

A precondition can determine which path is valid.

Check eligibility
      │
 ┌────┴────┐
 │         │
TRUE      FALSE
 │         │
 ▼         ▼
Issue     Stop

The planner may encode the branch.

Execution evaluates the actual condition.

⸻

42. Preconditions and Failure

If a required precondition is false:

Precondition = NOT_SATISFIED

the Action should not execute.

This is not an execution failure.

It is an execution eligibility failure.

The distinction matters:

Precondition failure:
Action was not valid to execute.
Execution failure:
Action was valid and attempted, but did not complete successfully.

⸻

43. Preconditions and Intervention

A failed precondition may require human intervention.

Example:

refund_amount > approval_threshold

Precondition:

manager_approval = APPROVED

If not approved:

BLOCKED
   ↓
Human Intervention

The Action remains unexecuted.

⸻

44. Preconditions and Replanning

A failed precondition may invalidate the current plan.

Example:

Plan:
issue_card

Precondition:

customer.eligible = TRUE

Runtime evaluation:

customer.eligible = FALSE

Possible result:

Plan invalidated
   ↓
replan

The system must not blindly continue.

⸻

45. Preconditions and Clarification

A missing precondition may sometimes indicate missing Intent information.

Example:

Action:
book_flight
Required:
destination

If destination is absent from the resolved Intent:

clarification

may be required.

The planner should not invent the missing value.

⸻

46. Preconditions and Determinism

Precondition evaluation must be deterministic wherever the condition can be represented deterministically.

Given:

same state
same evidence
same policy version
same evaluation rules

the result should be:

same result

An LLM should not randomly decide that a safety-critical precondition “probably passes.”

⸻

47. LLM-Assisted Preconditions

An LLM may assist in extracting facts from unstructured evidence.

Example:

Document
 ↓
LLM extraction
 ↓
"approval appears present"

But the authoritative evaluation should still establish:

approval.status = VERIFIED

through the deterministic Trust/Evidence pipeline.

⸻

48. Preconditions and External State

External systems may change independently of Noema.

Therefore a precondition involving external state should be evaluated against an authoritative or sufficiently fresh source.

Example:

inventory.available >= 1

must reflect current inventory, not an old cached value where overselling is possible.

⸻

49. Preconditions and Transactions

When multiple preconditions protect a single atomic mutation, they may need to be evaluated within the same transaction.

Example:

balance >= amount
account.status = ACTIVE

followed by:

debit account

Checking these separately from the mutation can introduce race conditions.

⸻

50. Preconditions and Optimistic Concurrency

A Resource version can be used as a precondition.

Example:

resource.version = 17

Action:

update_resource

If the current version is:

18

the Action should fail its precondition rather than overwrite concurrent changes.

This provides an explicit concurrency boundary.

⸻

51. Preconditions and Atomicity

Where practical:

A precondition that protects the correctness of a state mutation should be enforced as close as possible to the mutation itself.

This minimizes:

time-of-check
→
time-of-use

gaps.

⸻

52. Precondition Composition

Multiple preconditions may be composed.

Example:

P1 AND P2 AND P3

where:

P1 = account active
P2 = user authorized
P3 = sufficient balance

All are required.

⸻

53. Alternative Preconditions

Some Actions may allow alternative valid conditions.

Example:

P1 OR P2

For example:

verified_identity
OR
trusted_existing_session

The equivalence must be explicitly defined.

Noema must not invent alternative paths.

⸻

54. Precondition Evaluation Order

Where evaluation itself has cost or side effects, the order may matter.

Example:

cheap local condition
       ↓
expensive external verification

However, evaluation order must never alter the semantic result.

Precondition checks should themselves ideally be side-effect free.

⸻

55. Preconditions Should Be Side-Effect Free

A precondition check should generally observe state rather than mutate it.

Bad:

check_balance()

which itself reserves or deducts money.

Better:

observe_balance()

followed by the actual mutation under the appropriate atomicity guarantees.

⸻

56. Preconditions and Observability

Every failed or unknown precondition should be observable.

The execution record should preserve:

precondition
evaluation result
evidence
evaluation time
reason

Example:

Precondition:
account.status = ACTIVE
Observed:
account.status = SUSPENDED
Result:
NOT_SATISFIED

⸻

57. Preconditions and Auditability

A consequential Action should be explainable in terms of the conditions that allowed it to execute.

For example:

Why was this Action executed?
Because:
account.status = ACTIVE
authorization = APPROVED
risk_level = ACCEPTABLE
resource.version = 17

The exact evidence should be traceable.

⸻

58. Preconditions and Security

Preconditions must not be client-controlled facts.

Bad:

request.preconditions = {
    account_verified: true
}

A caller cannot establish their own authorization or safety conditions merely by asserting them.

The system must obtain authoritative evidence.

⸻

59. Preconditions and Trust

Trust determines whether evidence is sufficient to accept a precondition.

Observed evidence
      ↓
Trust evaluation
      ↓
Precondition satisfaction

A claim may exist without being trusted.

Therefore:

claim exists
≠
precondition satisfied

⸻

60. Preconditions and Authorization

A useful execution gate is:

Intent valid
      AND
Plan valid
      AND
Authorization valid
      AND
Preconditions satisfied
      ↓
Action may execute

Failure of any required gate prevents execution.

⸻

61. Preconditions and Postcondition Chains

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

This creates a formal dependency graph.

⸻

62. Preconditions and Plan Validity

A plan may be structurally valid while being runtime-infeasible.

Example:

Plan:
issue_card

Structurally:

VALID

Runtime:

customer.eligibility = FALSE

Therefore:

Action blocked
Plan may require replanning

This is why plan validity and runtime execution eligibility must remain distinct.

⸻

63. Precondition Lifecycle

Conceptually:

DEFINED
   ↓
EVALUATING
   ↓
SATISFIED

or:

DEFINED
   ↓
EVALUATING
   ↓
NOT_SATISFIED

or:

DEFINED
   ↓
EVALUATING
   ↓
UNKNOWN

A previously satisfied precondition may later require re-evaluation.

⸻

64. Precondition Snapshot

For auditability, Noema may preserve the evaluated state:

precondition_snapshot {
    condition
    evidence
    evaluated_at
    result
}

This does not mean the snapshot remains true forever.

It records what was established at that time.

⸻

65. Precondition Expiration

Some preconditions may have a validity duration.

Example:

identity_verification valid for 10 minutes

After expiration:

previously satisfied

does not necessarily mean:

currently satisfied

The condition must be re-established.

⸻

66. Preconditions and Long-Running Actions

For long-running Actions, a precondition may be valid at start but cease to hold during execution.

Example:

Action:
provision infrastructure

Precondition:

account remains authorized

If authorization is revoked mid-execution, the execution model must define whether the Action:

continues
pauses
terminates
compensates

This belongs to execution lifecycle semantics, not merely the initial precondition check.

⸻

67. Start Preconditions vs Continuous Invariants

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

68. Preconditions and Side Effects

An Action must not produce consequential side effects before required preconditions have been satisfied.

Bad:

begin payment
 ↓
check authorization

Correct:

check authorization
 ↓
check preconditions
 ↓
execute payment

Where the external operation itself atomically validates the relevant conditions, that boundary may serve as the authoritative enforcement point.

⸻

69. Preconditions and Idempotent State

For naturally idempotent Actions:

set_status(ACTIVE)

the precondition may permit:

status = ACTIVE

depending on whether the Action means:

"make active"

rather than:

"transition from pending to active"

The semantic distinction must be explicit.

⸻

70. Preconditions and Action Semantics

Two Actions with similar names may have different preconditions.

activate_card

could mean:

requires:
card.status = ISSUED

while:

ensure_card_active

could mean:

requires:
card.exists

and succeed if already active.

Action semantics therefore determine precondition semantics.

⸻

71. Preconditions and Failure Classification

A useful distinction:

PRECONDITION_NOT_SATISFIED

means:

The Action cannot currently execute under its contract.

EXECUTION_FAILED

means:

The Action was eligible and attempted, but execution failed.

POSTCONDITION_NOT_SATISFIED

means:

Execution occurred, but the required effect was not established.

UNKNOWN

means:

The system cannot currently establish the relevant state.

These distinctions should remain canonical.

⸻

72. Preconditions and Recovery

Recovery depends on why the precondition failed.

Example:

balance insufficient

may require:

wait

while:

authorization revoked

may require:

human intervention

and:

resource deleted

may require:

replan

Noema should not apply a universal retry policy to precondition failures.

⸻

73. Preconditions and Safety

For high-risk Actions:

UNKNOWN

should normally result in:

BLOCK

For low-risk or read-only Actions, the contract may permit a different behavior.

The Action’s risk profile therefore influences how unknown preconditions are handled.

⸻

74. Preconditions and Read Actions

Not every Action requires strict mutation preconditions.

Example:

get_account_balance

may only require:

account exists
actor authorized to read

The precondition model should be proportionate to the Action’s consequences.

⸻

75. Preconditions and Write Actions

State-changing Actions generally require stronger preconditions.

Example:

delete_account

may require:

account exists
actor authorized
account has no blocking dependencies
retention policy permits deletion

⸻

76. Preconditions and External APIs

A provider API may have its own preconditions.

Example:

Provider:
capture payment only if payment.status = AUTHORIZED

Noema should model this requirement where it is relevant to safe execution.

Provider-side enforcement may ultimately be authoritative.

⸻

77. Preconditions and Consumer Responsibility

The consumer executing an Action must enforce the preconditions required by its Action Contract.

Noema should not assume:

"the consumer probably checked it."

The contract must define responsibility.

⸻

78. Preconditions and Noema Responsibility

Noema is responsible for establishing the semantic conditions that it owns.

The consumer is responsible for enforcing execution-local conditions it owns.

This suggests a layered model:

Noema:
intent / trust / policy / contract validity
Consumer:
execution-specific runtime invariants
Provider:
provider-specific execution constraints

These boundaries should be explicit.

⸻

79. Preconditions and Contract Boundaries

A precondition belongs at the layer that can actually enforce it.

For example:

Noema:
authorization approved
Consumer:
resource version = 17
Provider:
payment instrument valid

Duplicating conditions across layers may be useful for defense in depth, but ownership should remain clear.

⸻

80. Preconditions and Deterministic State

Preconditions should preferably reference canonical state rather than free-form natural language.

Bad:

customer appears to be eligible

Better:

customer.eligibility_status == ELIGIBLE

This makes execution behavior:

observable
testable
auditable
deterministic

⸻

81. Preconditions and Canonical Ontology

Preconditions should use the concepts defined by Noema’s Ontology.

For example:

Actor
Resource
State
Capability
Policy
Constraint
Relationship

rather than introducing ad hoc terminology for each execution integration.

⸻

82. Preconditions and Execution Contracts

The canonical execution chain becomes:

Executable Intent
       ↓
Action Plan
       ↓
Action Contract
       ↓
Preconditions
       ↓
Authorization
       ↓
Execution
       ↓
Postconditions
       ↓
Outcome

The ordering of authorization and precondition checks may vary by implementation, but both must be satisfied before consequential execution.

⸻

83. Preconditions Invariants

Invariant 1

An Action must not execute when a required precondition is not satisfied.

Invariant 2

UNKNOWN must not be treated as SATISFIED for consequential Actions.

Invariant 3

Preconditions must be explicit and evaluatable.

Invariant 4

Preconditions must be evaluated against sufficient evidence.

Invariant 5

Precondition evaluation must be deterministic where the underlying condition is deterministic.

Invariant 6

A precondition snapshot records what was established at a point in time; it does not guarantee that the condition remains true.

Invariant 7

Time-sensitive preconditions must respect their freshness or validity window.

Invariant 8

Preconditions must not be satisfied merely by caller assertion.

Invariant 9

Preconditions must not silently replace authorization or policy evaluation.

Invariant 10

Where race conditions are possible, preconditions protecting mutations must be enforced atomically or with appropriate concurrency control.

Invariant 11

A failed precondition is distinct from an execution failure.

Invariant 12

A failed precondition must not automatically trigger retry.

Invariant 13

A postcondition from one Action may establish a precondition for another Action.

Invariant 14

Retries must re-evaluate relevant runtime preconditions.

Invariant 15

A materially changed Action requires its own precondition evaluation.

Invariant 16

Precondition failures must be observable and auditable.

Invariant 17

Preconditions must be evaluated at the layer responsible for enforcing them.

Invariant 18

Noema must not invent missing precondition values from ambiguous Intent.

⸻

84. Canonical Mental Model

                     ACTION
                        │
                        ▼
              ┌─────────────────┐
              │ PRECONDITIONS   │
              └────────┬────────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
         SATISFIED   FALSE     UNKNOWN
             │         │         │
             ▼         ▼         ▼
       AUTHORIZATION  BLOCK     BLOCK /
             │                  RECONCILE
             ▼
          EXECUTE
             │
             ▼
       POSTCONDITIONS
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
     TRUE   FALSE UNKNOWN
       │      │      │
       ▼      ▼      ▼
    SUCCESS FAILURE RECONCILE /
                     INTERVENE

And across Actions:

Action A
   │
   └── Postcondition A
             │
             ▼
       Precondition B
             │
             ▼
          Action B

⸻

85. Final Definition

A precondition is an explicit, evaluable condition that must be established before an Action may execute. Preconditions protect the execution boundary from stale state, invalid assumptions, unauthorized conditions, and unsafe state transitions.

The core invariant is:

Noema does not execute an Action because the plan says it should. It executes only when the Action’s required authorization and runtime preconditions are satisfied at the appropriate execution boundary. If a required condition is false or cannot be established, Noema stops, reconciles, intervenes, or replans rather than guessing.