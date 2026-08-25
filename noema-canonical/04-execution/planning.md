Planning

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: 04-execution/planning.md

⸻

1. Definition

Planning is the process of determining a valid sequence of executable Actions required to move from an accepted Intent toward its intended Outcome, subject to the constraints, policies, capabilities, dependencies, and execution semantics known to Noema.

Planning answers:

What Actions must happen, and in what order, for this Intent to be executed safely?

Planning does not itself execute Actions.

Intent
   ↓
Resolution
   ↓
Planning
   ↓
Action Plan
   ↓
Trust / Policy
   ↓
Action Contracts
   ↓
Execution
   ↓
Outcome

⸻

2. Core Principle

Planning determines what should be executed; execution determines what actually happened.

This distinction is fundamental.

Plan ≠ Execution

A valid plan is not evidence that any Action has occurred.

⸻

3. Why Planning Exists

A resolved Intent may require more than one Action.

For example:

Intent:
"Renew my company card."
Plan:
1. Verify account
2. Verify card eligibility
3. Generate replacement card
4. Update delivery address
5. Notify account owner

Noema needs a formal representation of this sequence before execution can safely begin.

⸻

4. Planning Is Downstream of Intent

Planning must not determine what the user intended.

The canonical sequence is:

User Input
    ↓
Intent
    ↓
Intent Resolution
    ↓
Executable Intent
    ↓
Planning

The planner operates on an already-resolved Intent.

If the Intent remains materially ambiguous:

Intent
   ↓
AMBIGUOUS
   ↓
Clarification

not:

AMBIGUOUS
   ↓
Planner guesses

⸻

5. Planning Is Not Intent Resolution

Intent resolution answers:

“What does the user want?”

Planning answers:

“What executable Actions can realize that Intent?”

These must remain separate.

Intent Resolution
    = semantic problem
Planning
    = operational problem

⸻

6. Planning Is Not Trust

Planning determines a candidate execution strategy.

Trust determines whether that strategy is permitted.

Planning
   ↓
Candidate Action Plan
   ↓
Trust Evaluation
   ↓
Authorized / Denied / Intervention

The planner must not grant itself authorization.

⸻

7. Planning Is Not Policy Evaluation

A planner may consider policies as constraints.

It must not become the authoritative policy evaluator.

For example:

Planner:
"Refund requires manager approval."

may be useful as planning context.

But the canonical decision remains:

Policy Engine:
MANAGER_APPROVAL_REQUIRED

⸻

8. Planning Is Not Execution

A plan may contain:

Action A
Action B
Action C

but this does not mean:

A = executed
B = executed
C = executed

The execution state exists separately.

⸻

9. Plan Identity

Every executable plan should have a stable identity.

Conceptually:

plan_id
intent_id
version
created_at
status

This allows the system to distinguish:

Plan P1

from:

Plan P2

generated after a material change.

⸻

10. Plan Version

Plans may evolve.

Example:

Plan v1
  ↓
Action A
Action B
Action C

A new constraint is discovered:

Plan v2
  ↓
Action A
Action D
Action C

The system must preserve the distinction between versions.

A plan should not be silently mutated after execution has begun.

⸻

11. Plan Immutability

Once a plan has entered execution, its historical representation should be immutable.

If the strategy changes:

Plan v1
   ↓
superseded
   ↓
Plan v2

rather than:

Plan v1
   ↓
silently modified

This preserves auditability and causal lineage.

⸻

12. Action Plan

Conceptually:

ActionPlan {
    plan_id
    intent_id
    actions[]
    dependencies
    constraints
    assumptions
    expected_outcome
}

The exact schema belongs to implementation.

The semantic model is canonical.

⸻

13. Plan as a Directed Graph

A plan is better understood as a dependency graph than merely a list.

             Verify Account
                  │
                  ▼
          Verify Eligibility
             │          │
             ▼          ▼
       Create Card   Update Address
             │          │
             └────┬─────┘
                  ▼
               Notify

This allows:

sequential execution
parallel execution
conditional execution
dependency enforcement

⸻

14. Sequential Actions

Some Actions must occur in order.

Example:

verify_identity
      ↓
create_account
      ↓
issue_card

The planner must represent these dependencies explicitly.

⸻

15. Parallel Actions

Some Actions are independent.

Example:

              ┌→ update_profile
Intent ────────┤
              └→ send_notification

If neither depends on the other, they may execute concurrently.

The plan must make that independence explicit.

⸻

16. Conditional Actions

Some Actions depend on runtime state.

Example:

verify_card
     ↓
 ┌───┴────┐
 │        │
valid    invalid
 │        │
 ▼        ▼
renew    terminate

The plan must define the condition governing the branch.

The planner must not assume the branch outcome in advance.

⸻

17. Plan Dependencies

An Action may depend on:

another Action
resource state
evidence
policy result
external state
human decision

Example:

create_card
    depends_on:
        card_eligibility = TRUE

⸻

18. Dependency Semantics

Dependencies should be explicit.

For example:

Action B
requires:
    Action A = SUCCESS

is materially different from:

Action B
requires:
    Action A = COMPLETED

because COMPLETED may include non-success terminal states depending on execution semantics.

⸻

19. Preconditions

An Action may have preconditions.

Example:

issue_card
requires:
    customer_verified = true
    account_status = ACTIVE

The planner should represent these requirements.

The execution system must verify them at the appropriate boundary.

⸻

20. Postconditions

An Action may produce expected state transitions.

Example:

issue_card
expected:
    card.status = ACTIVE

These are expected effects, not guarantees.

The actual Outcome must be established through execution evidence.

⸻

21. Plan Assumptions

Planning often relies on assumptions.

Example:

Assumption:
customer has a valid delivery address

Assumptions must not silently become facts.

If an assumption becomes invalid:

Plan
   ↓
invalidated
   ↓
re-plan / clarify / intervene

⸻

22. Planning and Context

Plans may depend on Context.

Example:

Intent:
"Book the cheapest available flight."
Context:
departure city
destination
travel date
passenger count

The plan must reference the relevant Context without confusing contextual information with Intent itself.

⸻

23. Planning and Resources

Actions operate on Resources.

A plan should identify relevant resource dependencies.

Example:

Action:
update_card
Resource:
card_123

This supports:

authorization
concurrency control
dependency analysis
execution tracking

⸻

24. Planning and Capabilities

A plan may only contain Actions that available consumers can perform.

Conceptually:

Intent
   ↓
Required capability
   ↓
Available capability
   ↓
Candidate Action

If the required Capability does not exist:

NO_EXECUTABLE_PLAN

rather than:

invented Action

⸻

25. Planning and Action Contracts

The planner produces candidate Actions.

Execution requires valid Action Contracts.

Plan
 ↓
Action
 ↓
Contract
 ↓
Execution

Planning should therefore preserve enough information to construct or validate the required contract.

⸻

26. Planning and Trust

Trust may evaluate:

the entire plan

or:

individual Actions

or both.

For high-consequence workflows:

Plan
 ↓
Action A → authorized
Action B → requires approval
Action C → authorized

The plan therefore does not imply uniform authorization.

⸻

27. Plan Feasibility

Before execution, Noema should determine whether the plan is executable.

A plan may be infeasible because:

required capability unavailable
required resource unavailable
policy prohibits Action
authorization unavailable
dependency impossible
required human authority unavailable
contract cannot be constructed

The correct state is:

PLAN_INFEASIBLE

not speculative execution.

⸻

28. Planning Failure

Planning can fail before execution begins.

Examples:

NO_CAPABILITY
UNSATISFIABLE_CONSTRAINT
MISSING_RESOURCE
POLICY_BLOCKED
AMBIGUOUS_DEPENDENCY
INVALID_ACTION_SEQUENCE

Planning failure is distinct from execution failure.

Planning failure:
nothing executed
Execution failure:
an Action was attempted

⸻

29. Planning and Constraints

Constraints restrict the set of valid plans.

Examples:

must happen before
must not happen after
requires approval
maximum cost
deadline
resource availability
regulatory restriction

The planner must produce a plan satisfying the applicable constraints.

⸻

30. Planning and Policy Constraints

Policy may impose planning constraints.

Example:

Policy:
refunds above ₦10m require approval

Possible plan:

calculate_refund
      ↓
request_manager_approval
      ↓
issue_refund

The planner incorporates the policy-defined requirement.

The Policy Engine remains authoritative.

⸻

31. Planning and Risk

Risk can affect the execution path.

Example:

Risk:
HIGH
Plan:
prepare_action
      ↓
human_review
      ↓
execute

The planner may represent the review step where policy requires it.

It cannot independently waive the risk requirement.

⸻

32. Planning and Human Intervention

Human intervention can be a planned control boundary.

Example:

Action A
   ↓
Human Approval
   ↓
Action B

This does not mean the planner predicts that a human will approve.

It means:

approval is a required prerequisite

The actual decision occurs at runtime.

⸻

33. Planning and Clarification

A plan cannot safely resolve missing Intent information.

Example:

Intent:
"Send the report."
Missing:
Which report?
Which recipient?

Correct:

Clarification

not:

Plan:
guess report
guess recipient

⸻

34. Planning and Ambiguity

Material ambiguity prevents executable planning.

Ambiguous Intent
      ↓
No executable plan
      ↓
Clarification

The planner may generate multiple candidate plans internally, but only a sufficiently resolved Intent should reach execution authorization.

⸻

35. Plan Determinism

For the same:

resolved Intent
relevant Context
available Capabilities
applicable Policies
known Constraints

the planner should produce a deterministic or reproducibly constrained plan where the domain requires it.

The LLM must not silently generate different consequential plans from identical authoritative inputs.

⸻

36. LLM-Assisted Planning

The model may be useful for proposing candidate plans.

For example:

LLM
 ↓
Candidate Plan
 ↓
Deterministic validation
 ↓
Accepted / rejected

The model does not become the source of execution authority.

⸻

37. Planner Output Validation

A generated plan must be validated against:

Ontology
Capabilities
Actions
Constraints
Policies
Authorization requirements
Action Contracts

Invalid plans must be rejected before execution.

⸻

38. Planning and Deterministic Validation

The canonical pipeline is:

Model proposes
      ↓
Noema validates
      ↓
Plan accepted

not:

Model proposes
      ↓
execute immediately

⸻

39. Plan Completeness

A plan should be considered complete only when the system can determine:

required Actions
dependencies
conditions
required capabilities
relevant constraints
expected terminal conditions

Incomplete plans should not enter autonomous execution.

⸻

40. Plan Minimality

Noema should avoid unnecessary Actions.

If:

Action A

achieves the required Outcome, the planner should not introduce:

Action B
Action C
Action D

without a semantic reason.

Unnecessary Actions increase:

risk
latency
cost
failure surface
authorization burden

⸻

41. Plan Optimality

Noema does not necessarily need to find the globally optimal plan.

The primary requirement is:

valid
safe
authorized
executable

Optimization is secondary.

A slightly slower valid plan is preferable to a faster unsafe one.

⸻

42. Plan Cost

Where relevant, plans may include cost estimates:

execution cost
financial cost
latency
resource consumption
risk

These may be used to choose between valid plans.

They do not override hard constraints.

⸻

43. Plan Deadline

Some Intentions have temporal constraints.

Example:

"Renew this before Friday."

The plan may therefore have:

deadline

Actions that cannot complete within the required temporal boundary may render the plan infeasible.

⸻

44. Plan Cancellation

A plan may be cancelled because:

Intent withdrawn
constraint violated
authorization revoked
resource unavailable
deadline passed
policy changed

Cancellation should terminate or invalidate pending Actions according to their execution semantics.

⸻

45. Plan Replanning

Replanning is required when the current plan is no longer valid.

Example:

Plan v1
   ↓
provider unavailable
   ↓
replan
   ↓
Plan v2

Replanning must preserve the history of the original plan.

⸻

46. Replanning Is Not Retrying

Retry:

same Action
same semantic identity
new execution attempt

Replanning:

new execution strategy
possibly different Actions
possibly different dependencies

Therefore:

Retry ≠ Replan

⸻

47. Replanning After Partial Execution

A plan may partially execute:

Action A → SUCCESS
Action B → SUCCESS
Action C → FAILURE

A new plan must account for the effects already produced.

It must not blindly repeat:

Action A
Action B

if doing so would duplicate effects.

⸻

48. Plan Lineage

Every plan should maintain lineage to:

Intent
parent plan
superseded plan
Actions
execution records
Outcome

Example:

Intent I1
   ↓
Plan P1
   ↓
Execution E1
   ↓
Failure
   ↓
Plan P2
   ↓
Execution E2
   ↓
Outcome O1

⸻

49. Plan and Outcome

A plan defines expected outcomes.

Execution produces observed outcomes.

Plan:
expected = card.status ACTIVE
Execution:
observed = card.status ACTIVE

The system can then establish:

Outcome:
SUCCESS

If the observed state differs:

Outcome:
FAILURE / PARTIAL / UNKNOWN

depending on the domain semantics.

⸻

50. Plan and Partial Completion

A multi-Action plan may produce partial completion.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE

The overall workflow must not simply be classified as:

nothing happened

The execution history must preserve each Action’s state.

⸻

51. Plan Compensation

If partial execution leaves inconsistent state, the plan may define compensation.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE
Compensation:
undo B
undo A

Compensation is itself an executable process and must follow the rules in compensation.md.

⸻

52. Plan State

A conceptual plan lifecycle:

DRAFT
  ↓
VALIDATING
  ↓
VALID
  ↓
READY
  ↓
EXECUTING
  ↓
COMPLETED

Possible alternate states:

INFEASIBLE
BLOCKED
CANCELLED
SUPERSEDED
FAILED

The exact state machine should remain aligned with execution-model.md.

⸻

53. DRAFT

A candidate plan exists but has not passed validation.

⸻

54. VALIDATING

The plan is being checked against:

Actions
Capabilities
Constraints
Policies
Contracts
dependencies

⸻

55. VALID

The plan satisfies the known structural and semantic requirements.

It is not necessarily authorized for execution yet.

⸻

56. READY

The plan has passed the required trust and authorization gates and can enter execution.

⸻

57. EXECUTING

One or more Actions from the plan are actively executing.

⸻

58. COMPLETED

All required Actions have reached their required terminal conditions and the intended Outcome has been established.

⸻

59. SUPERSEDED

A newer plan has replaced the plan.

The old plan remains part of history.

⸻

60. Plan Validation Invariants

Invariant 1

Planning occurs only after Intent has reached sufficient resolution for execution.

Invariant 2

Planning must never resolve material user ambiguity by guessing.

Invariant 3

A plan is not an execution.

Invariant 4

A plan is not authorization.

Invariant 5

A plan cannot contain Actions for which the required Capability does not exist.

Invariant 6

Action dependencies must be explicit.

Invariant 7

Conditional branches must have explicit conditions.

Invariant 8

Assumptions must not be represented as established facts.

Invariant 9

A plan must satisfy applicable hard Constraints.

Invariant 10

Policy remains authoritative over planning.

Invariant 11

Trust remains authoritative over authorization.

Invariant 12

Plans entering execution must have stable identity.

Invariant 13

Plans must not be silently mutated after execution begins.

Invariant 14

Replanning must preserve the lineage of previous plans and executions.

Invariant 15

A replanned workflow must account for Actions already executed.

Invariant 16

A plan must never claim an Outcome merely because its Actions were planned.

Invariant 17

A valid plan must still be evaluated against runtime state where required.

Invariant 18

The system must prefer a safe feasible plan over an optimized but unsafe plan.

⸻

61. Canonical Mental Model

                     INTENT
                       │
                       ▼
               INTENT RESOLUTION
                       │
                       ▼
                EXECUTABLE INTENT
                       │
                       ▼
                    PLAN
                       │
             ┌─────────┴─────────┐
             │                   │
          VALIDATE            INFEASIBLE
             │
             ▼
         TRUST / POLICY
             │
      ┌──────┴──────┐
      │             │
   AUTHORIZED    INTERVENTION
      │             │
      └──────┬──────┘
             ▼
          CONTRACTS
             │
             ▼
         EXECUTION
             │
             ▼
           OUTCOME

And for adaptation:

                PLAN v1
                   │
                   ▼
               EXECUTION
                   │
          ┌────────┼────────┐
          │        │        │
       SUCCESS   FAILURE  UNKNOWN
                             │
                             ▼
                       RECONCILIATION
                             │
                   ┌─────────┴─────────┐
                   │                   │
                RESOLVE              REPLAN
                                       │
                                       ▼
                                    PLAN v2

⸻

62. Final Definition

Planning is the controlled construction of an executable Action strategy from a resolved Intent. A plan defines the Actions, dependencies, conditions, constraints, and required control boundaries necessary to pursue an Outcome, but it does not itself authorize or execute those Actions.

The core invariant is:

Noema plans before it acts, but never confuses a plan with reality. Planning determines a valid strategy; Trust and Policy determine whether that strategy may proceed; Action Contracts define the executable boundary; Execution records what actually happened; and Outcomes are established from evidence rather than inferred from the plan.