Planning

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/planning.md

⸻

1. Definition

Planning is the process of determining a valid sequence or dependency graph of executable Actions required to move from an admitted and sufficiently resolved Intent toward its intended Outcome, subject to the constraints, policies, capabilities, dependencies, current state, and execution semantics known to Noema.

Planning answers:

What Actions can realize this Intent, and in what order or dependency structure can they be executed safely?

Planning does not itself execute Actions.

Source of Intent
    ↓
Intent Interpretation
    ↓
Hard Schema Validation / Admission
    ↓
Intent Resolution
    ↓
State / Context Reconciliation
    ↓
Planning
    ↓
Candidate Action Plan
    ↓
Deterministic Trust
    ↓
Action Contracts
    ↓
Execution
    ↓
Verification / Reconciliation
    ↓
Outcome

⸻

2. Core Principle

Planning determines a candidate execution strategy; execution determines what actually happened.

This distinction is fundamental.

Plan
≠
Execution
≠
Outcome

A valid plan is not evidence that any Action has occurred.

A completed plan is not established merely because every planned step was dispatched. Required execution states, verification, and Outcome semantics must still be satisfied.

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

Noema needs a formal representation of this dependency structure before execution can safely begin.

Planning therefore converts a resolved semantic goal into a bounded operational strategy.

⸻

4. Planning Is Downstream of Intent

Planning must not determine what the source of intent meant.

The canonical sequence is:

Source of Intent
    ↓
Candidate Interpretation
    ↓
Hard Schema Validation / Admission
    ↓
Admitted Intent
    ↓
Resolution
    ↓
Planning

If the Intent remains materially ambiguous:

Intent
   ↓
material ambiguity
   ↓
CLARIFY

not:

material ambiguity
   ↓
planner guesses

The planner operates only on the semantic information admitted for planning.

⸻

5. Planning Is Not Intent Resolution

Intent resolution answers:

What does the source of Intent mean?

Planning answers:

What executable Actions can realize that meaning?

These must remain separate.

Intent Resolution
    =
semantic problem
Planning
    =
operational problem

Planning may expose that no executable strategy exists, but it must not repair material ambiguity by inventing user intent.

⸻

6. Planning Is Not Trust

Planning determines a candidate execution strategy.

Trust determines whether the resolved execution path is permitted to proceed.

Planning
   ↓
Candidate Action Plan
   ↓
Trust Evaluation
   ↓
EXECUTE / CLARIFY / ESCALATE / REJECT

The planner must not grant itself authorization.

The canonical Trust outcomes are exactly:

EXECUTE
CLARIFY
ESCALATE
REJECT

Other states such as READY, BLOCKED, WAITING_FOR_APPROVAL, or REQUIRES_REVALIDATION are execution or control states, not additional Trust outcomes.

⸻

7. Planning Is Not Policy Evaluation

A planner may consume policy constraints.

It must not become the authoritative policy evaluator.

For example:

Planner:
"Refund requires manager approval."

may be planning context.

The authoritative decision remains with the applicable policy and Trust evaluation:

Policy / Trust:
MANAGER_APPROVAL_REQUIRED

Policy semantics must not be invented by the planner or model.

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

Execution state exists separately.

Each Action Instance must establish its own execution state and evidence.

⸻

9. Plan Identity

Every executable plan should have a stable identity.

Conceptually:

plan_id
intent_id
intent_version
plan_version
created_at
status

This allows the system to distinguish:

Plan P1

from:

Plan P2

generated after a material change in state, constraints, policy, capability, or execution conditions.

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

A plan must not be silently mutated after it has become part of consequential execution history.

⸻

11. Plan Immutability

Once a plan has entered consequential execution, its historical representation should be immutable.

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

A new plan does not rewrite the history of Actions already attempted.

⸻

12. Action Plan

Conceptually:

ActionPlan {
    plan_id
    intent_id
    intent_version
    plan_version
    actions[]
    dependencies
    conditions
    constraints
    assumptions
    required_capabilities
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

* sequential execution
* parallel execution
* conditional execution
* dependency enforcement
* explicit failure propagation
* bounded replanning

The graph describes intended execution structure, not actual execution state.

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

An ordering relationship must not be inferred merely from the order in which Actions happen to appear in a generated list.

⸻

15. Parallel Actions

Some Actions are independent.

Example:

              ┌→ update_profile
Intent ───────┤
              └→ send_notification

If neither depends on the other and their concurrent execution is permitted, they may execute concurrently.

The plan must make that independence explicit.

Parallelism must not violate resource, authorization, policy, concurrency, or idempotency constraints.

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

Runtime conditions must be evaluated against appropriate current evidence and reconciled state where required.

⸻

17. Plan Dependencies

An Action may depend on:

* another Action
* resource state
* evidence
* Fact Status
* policy result
* capability availability
* external state
* human decision
* time constraint
* verification result

Example:

create_card
    depends_on:
        card_eligibility = VERIFIED

A dependency may refer to a required fact or state condition without itself becoming the authoritative source of that fact.

⸻

18. Dependency Semantics

Dependencies must be explicit.

For example:

Action B
requires:
    Action A = SUCCESS

is materially different from:

Action B
requires:
    Action A = COMPLETED

because COMPLETED may include terminal execution conditions that do not establish the required successful semantic effect.

Dependencies must reference the execution semantics appropriate to the Action.

⸻

19. Preconditions

An Action may have preconditions.

Example:

issue_card
requires:
    customer_verified = true
    account_status = ACTIVE

The planner should represent these requirements.

The execution system must verify them at the appropriate execution boundary using current applicable evidence and state.

A plan’s representation of a precondition is not itself proof that the precondition holds.

⸻

20. Postconditions

An Action may produce expected state transitions.

Example:

issue_card
expected:
    card.status = ACTIVE

These are expected effects, not guarantees.

The actual Outcome must be established through execution evidence and verification against the appropriate authoritative enterprise state.

⸻

21. Plan Assumptions

Planning often relies on assumptions.

Example:

Assumption:
customer has a valid delivery address

Assumptions must not silently become facts.

If an assumption cannot be established:

Plan
   ↓
assumption invalid / unknown
   ↓
reconcile / re-plan / clarify / intervene

The correct transition depends on the applicable semantics.

Model confidence must not convert an assumption into a verified fact.

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

The plan must reference the relevant Context without confusing Context with Intent.

Context must retain its provenance, scope, freshness, and applicable authority semantics.

Where current enterprise state matters, State Reconciliation must establish the relevant reconciled observations before consequential planning or execution.

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

* authorization
* concurrency control
* dependency analysis
* execution tracking
* idempotency
* auditability

The exact target Resource must be resolved before consequential execution.

The planner must not guess a resource merely because several resources appear plausible.

⸻

24. Planning and Capabilities

A plan may only contain Actions for which an applicable Capability exists.

Conceptually:

Intent
   ↓
Required Capability
   ↓
Capability Registry
   ↓
Candidate Action

If the required Capability does not exist:

NO_EXECUTABLE_PLAN

rather than:

invented Action

Capability availability is a bounded input to planning.

The planner cannot create capabilities or authority.

⸻

25. Planning and Enterprise Action Graph

The Enterprise Action Graph provides the bounded enterprise knowledge from which planning may select executable paths.

It may represent relationships among:

* Systems
* Resources
* Capabilities
* Actions
* Policies
* Events
* organizational boundaries
* authority relationships
* dependencies
* integrations

The planner may traverse the graph to construct a candidate strategy.

It must not infer that a graph relationship alone grants permission to execute.

⸻

26. Planning and Action Contracts

The planner produces candidate Actions.

Execution requires valid Action Contracts.

Plan
 ↓
Action
 ↓
Action Contract
 ↓
Execution

Planning should therefore preserve enough information to construct or validate the required Contract.

The planner cannot invent, weaken, or modify Action Contract semantics to make an otherwise infeasible plan executable.

⸻

27. Planning and Trust

Trust may evaluate:

* the overall plan
* individual Actions
* both

For a high-consequence workflow:

Plan
 ↓
Action A → EXECUTE
Action B → ESCALATE
Action C → EXECUTE

The plan therefore does not imply uniform authorization.

A Trust decision must reference the exact Intent version and applicable semantic versions of the Action, Contract, policy, graph, capability, and relevant decision context.

⸻

28. Planning and Authorization

Authorization must remain distinct from planning.

The planner may identify authorization requirements, but it does not create technical, policy, or business authorization.

For example:

Planner:
"Action B requires manager authority."

does not mean:

Manager authority exists.

That fact must be established from the applicable enterprise authority source and evaluated deterministically.

⸻

29. Plan Feasibility

Before execution, Noema should determine whether the plan is executable.

A plan may be infeasible because:

* required capability unavailable
* required resource unavailable
* policy prohibits an Action
* authorization cannot be established
* dependency is impossible
* required human authority is unavailable
* required Action Contract cannot be constructed
* required enterprise state is unknown or conflicted
* required idempotency protection is unavailable
* temporal constraints cannot be satisfied

The correct state is:

PLAN_INFEASIBLE

rather than speculative execution.

⸻

30. Planning Failure

Planning can fail before execution begins.

Examples:

NO_CAPABILITY
UNSATISFIABLE_CONSTRAINT
MISSING_RESOURCE
POLICY_BLOCKED
AMBIGUOUS_DEPENDENCY
INVALID_ACTION_SEQUENCE
UNKNOWN_REQUIRED_STATE
CONTRACT_UNAVAILABLE

Planning failure is distinct from execution failure.

Planning failure:
no consequential Action has been attempted
Execution failure:
an Action was attempted and failed according to execution semantics

The distinction is important for audit, recovery, and metrics.

⸻

31. Planning and Constraints

Constraints restrict the set of valid plans.

Examples:

* must happen before
* must not happen after
* requires approval
* maximum cost
* deadline
* resource availability
* regulatory restriction
* organizational boundary
* tenant boundary
* concurrency restriction
* data-access restriction

The planner must produce a plan satisfying applicable hard constraints.

A model-generated plan cannot override a hard constraint.

⸻

32. Planning and Policy Constraints

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

The applicable Policy and Trust evaluation remain authoritative.

A policy requirement is not satisfied merely because the planner inserted an approval step. The actual approval and authority must be established at runtime.

⸻

33. Planning and Risk

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

It cannot independently waive, downgrade, or reinterpret the applicable risk requirement.

Risk is an input to deterministic governance, not a planner-generated authorization.

⸻

34. Planning and Human Intervention

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

The actual decision occurs at runtime through the Human Intervention mechanism.

The human decision remains subject to authority validation and current state.

⸻

35. Planning and Clarification

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

Clarification creates or updates the semantic Intent rather than allowing the planner to invent missing intent parameters.

⸻

36. Planning and Ambiguity

Material ambiguity prevents consequential executable planning.

Ambiguous Intent
      ↓
No executable plan
      ↓
CLARIFY
      ↓
new Intent version
      ↓
re-plan

The planner may generate candidate strategies for analysis, but no candidate plan may become executable merely because the model selected one.

Only a sufficiently resolved and admitted Intent can enter the consequential planning and Trust path.

⸻

37. Plan Determinism

For the same:

* resolved Intent version
* relevant Context
* reconciled state
* available Capabilities
* applicable Policies
* known Constraints
* Action definitions
* applicable semantic versions

the planner should produce a deterministic or reproducibly constrained plan where the domain requires it.

The LLM must not silently generate materially different consequential plans from identical authoritative inputs without an explicit reason such as a changed model/version or non-deterministic optimization strategy that is itself governed.

For consequential execution, plan provenance must preserve which inputs and versions produced the plan.

⸻

38. LLM-Assisted Planning

The model may be useful for proposing candidate plans.

For example:

LLM
 ↓
Candidate Plan
 ↓
Hard Schema Validation
 ↓
Deterministic Plan Validation
 ↓
Accepted / Rejected

The model does not become the source of execution authority.

Model-generated Actions, dependencies, constraints, resource bindings, or assumptions remain untrusted until validated against canonical Noema semantics.

⸻

39. Planner Output Validation

A generated plan must be validated against:

* Ontology
* Intent version
* resolved actor
* resolved target and Resources
* Capabilities
* Actions
* Enterprise Action Graph
* Constraints
* Policies
* authorization requirements
* Action Contracts
* idempotency requirements
* temporal requirements
* organizational and data boundaries

Invalid plans must be rejected before consequential execution.

The plan itself must pass a hard schema and semantic admission boundary before being treated as a canonical executable plan.

⸻

40. Planning and Deterministic Validation

The canonical pipeline is:

Model proposes
      ↓
Hard Schema Validation
      ↓
Semantic / Graph / Constraint Validation
      ↓
State / Context Reconciliation where required
      ↓
Trust Evaluation
      ↓
Plan Accepted / Rejected / Escalated / Clarified

not:

Model proposes
      ↓
execute immediately

Probabilistic planning is therefore separated from deterministic execution governance.

⸻

41. Plan Completeness

A plan should be considered complete only when the system can determine:

* required Actions
* exact or deterministically resolvable targets
* dependencies
* conditions
* required capabilities
* relevant constraints
* required authorization boundaries
* idempotency requirements
* expected terminal conditions
* required verification paths
* compensation or recovery requirements where applicable

Incomplete plans should not enter autonomous consequential execution.

⸻

42. Plan Minimality

Noema should avoid unnecessary Actions.

If:

Action A

achieves the required semantic goal, the planner should not introduce:

Action B
Action C
Action D

without a semantic reason.

Unnecessary Actions increase:

* risk
* latency
* cost
* failure surface
* authorization burden
* data exposure
* reconciliation burden

Minimality is therefore a safety and execution-quality property, not merely an optimization preference.

⸻

43. Plan Optimality

Noema does not necessarily need to find the globally optimal plan.

The primary requirement is:

valid
safe
permitted
executable
verifiable

Optimization is secondary.

A slightly slower valid plan is preferable to a faster plan that violates a hard safety, policy, authorization, or execution constraint.

⸻

44. Plan Cost

Where relevant, plans may include cost estimates:

* execution cost
* financial cost
* latency
* resource consumption
* risk
* operational burden

These may be used to choose between valid plans.

They do not override hard constraints, Trust decisions, authorization requirements, or enterprise policies.

Cost estimates are planning metadata, not guarantees.

⸻

45. Plan Deadline

Some Intents have temporal constraints.

Example:

"Renew this before Friday."

The plan may therefore have:

deadline

Actions that cannot complete within the required temporal boundary may render the plan infeasible.

Temporal feasibility must use the applicable clock, validity interval, current state, and execution duration assumptions. Time passing may invalidate a previously valid plan.

⸻

46. Plan Cancellation

A plan may be cancelled because:

* Intent withdrawn
* constraint violated
* authorization revoked
* resource unavailable
* deadline passed
* policy changed
* required capability removed
* execution environment invalidated

Cancellation should terminate or invalidate pending Actions according to their execution semantics.

Cancellation does not necessarily reverse Actions that have already executed.

Those effects remain part of execution history and may require compensation or reconciliation.

⸻

47. Plan Replanning

Replanning is required when the current plan is no longer valid.

Example:

Plan v1
   ↓
provider unavailable
   ↓
reconciliation / feasibility evaluation
   ↓
replan
   ↓
Plan v2

Replanning must preserve the history of the original plan.

The new plan must be based on the current applicable Intent version, reconciled state, capabilities, policies, and constraints.

⸻

48. Replanning Is Not Retrying

Retry:

same Action
same semantic identity
new execution attempt

Replanning:

new execution strategy
possibly different Actions
possibly different dependencies

Therefore:

Retry
≠
Replan

A retry preserves semantic Action identity.

A replan may introduce new Action Instances and therefore new Action and idempotency identities.

⸻

49. Replanning After Partial Execution

A plan may partially execute:

Action A → SUCCESS
Action B → SUCCESS
Action C → FAILURE

A new plan must account for the effects already produced.

It must not blindly repeat:

Action A
Action B

if doing so would duplicate effects.

Before replanning consequential work, Noema may need State Reconciliation to establish the current enterprise state and determine which Actions remain necessary.

The planner must also preserve the execution and Outcome history of the original plan.

⸻

50. Plan Lineage

Every plan should maintain lineage to:

* Intent
* exact Intent version
* parent plan where applicable
* superseded plan
* Actions
* Action Contracts
* Trust Decisions
* execution records
* reconciliation records
* Outcome

Example:

Intent I1 v3
   ↓
Plan P1 v1
   ↓
Execution E1
   ↓
Failure / UNKNOWN
   ↓
State Reconciliation
   ↓
Plan P2 v1
   ↓
Execution E2
   ↓
Outcome O1

Plan lineage must preserve historical meaning rather than overwrite previous strategy.

⸻

51. Plan and Outcome

A plan defines expected terminal conditions.

Execution produces observed execution state and evidence.

For example:

Plan:
expected = card.status ACTIVE
Execution:
observed = card.status ACTIVE

The system can then establish the applicable Outcome according to the Outcome model.

If the observed state differs:

Outcome:
FAILURE / PARTIAL / UNKNOWN

may apply depending on domain semantics and available evidence.

The planner must never establish Outcome merely because the plan predicted it.

⸻

52. Plan and Partial Completion

A multi-Action plan may produce partial completion.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE

The workflow must not simply be classified as:

nothing happened

The execution history must preserve each Action Instance’s state, evidence, Outcome, and relationship to the parent plan.

The overall Outcome must follow the applicable outcome semantics rather than a planner-defined shortcut.

⸻

53. Plan Compensation

If partial execution leaves inconsistent or otherwise unacceptable state, the plan may require compensation.

Example:

A → SUCCESS
B → SUCCESS
C → FAILURE
Compensation:
undo B
undo A

Compensation is itself an executable process and must follow the rules in execution/compensation.md.

The planner cannot assume that every failed plan has a valid inverse operation.

Compensation must be explicit, bounded, authorized, contractually defined, and subject to current state and Trust requirements.

⸻

54. Plan State

A conceptual plan lifecycle is:

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
VERIFYING
  ↓
COMPLETED

Possible alternate states include:

INFEASIBLE
BLOCKED
CANCELLED
SUPERSEDED
FAILED
REQUIRES_RECONCILIATION

These are plan or execution control states, not additional Trust outcomes.

The exact state machine must remain aligned with execution/execution-model.md.

⸻

55. DRAFT

A candidate plan exists but has not passed required schema, semantic, graph, constraint, or capability validation.

A Draft plan is not executable.

⸻

56. VALIDATING

The plan is being checked against:

* Intent and exact Intent version
* Actions
* Capabilities
* Enterprise Action Graph
* Constraints
* Policies
* dependencies
* resources
* authorization requirements
* Action Contracts
* idempotency requirements
* temporal constraints
* verification requirements

Validation does not itself establish Trust authorization.

⸻

57. VALID

The plan satisfies the known structural and semantic planning requirements.

It is not necessarily authorized for execution yet.

A plan may be structurally valid while still requiring Trust evaluation, human approval, current-state validation, or other runtime controls.

⸻

58. READY

The plan has passed the required planning and Trust gates and can enter execution, subject to any execution-time revalidation required by its contracts and state conditions.

READY is a plan/execution control state, not a Trust outcome.

⸻

59. EXECUTING

One or more Actions from the plan are actively executing.

Individual Action and Execution records remain authoritative for the actual execution state.

A plan marked EXECUTING does not imply that every Action in the plan has executed successfully.

⸻

60. VERIFYING

Required execution results are being verified against applicable evidence and enterprise state.

Where the result is uncertain, State Reconciliation is performed before the system determines whether to retry, compensate, replan, escalate, or otherwise recover.

⸻

61. COMPLETED

A plan is completed only when all required Actions have reached their required terminal conditions and the applicable intended Outcome has been established according to the Outcome model.

Completion is therefore not equivalent to:

all Actions dispatched

or:

all Actions returned without transport errors

Verification and Outcome semantics remain authoritative.

⸻

62. SUPERSEDED

A newer plan has replaced the plan for future execution.

The old plan remains part of history.

Supersession does not erase:

* previous Actions
* execution attempts
* Trust Decisions
* failures
* UNKNOWN states
* Outcomes
* reconciliation records

⸻

63. Plan Invalidation

A plan may become invalid when a material planning input changes.

Examples:

* Intent version changes
* resolved target changes
* enterprise state changes
* relevant Fact Status changes
* capability becomes unavailable
* policy changes
* authorization changes
* resource becomes unavailable
* contract expires
* temporal deadline changes
* required organizational boundary changes

The system must not silently continue executing a plan whose validity depends on inputs that have materially changed.

The appropriate response may be revalidation, replanning, clarification, escalation, rejection, or cancellation according to deterministic policy.

⸻

64. Planning and State Reconciliation

Planning may depend on current enterprise state.

Examples include:

current account status
current card status
current inventory
current authorization
current resource ownership
current provider availability

Noema must distinguish:

planned assumption

from:

reconciled enterprise observation

When current state is required and available observations conflict, are stale, or are unknown, the planner must not silently select the most convenient value.

State Reconciliation may be required before:

* plan admission
* plan feasibility evaluation
* Action selection
* Trust evaluation
* execution
* retry
* compensation
* replanning

⸻

65. Planning and Fact Status

Planning inputs may reference facts with explicit Fact Status:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

Evidence
Context
Business State
Plan State
Outcome
Model Confidence

A planner must not treat:

model_confidence = high

as equivalent to:

Fact Status = VERIFIED

Planning may use non-verified information for candidate generation, but consequential execution requires the applicable deterministic evidence and state conditions.

⸻

66. Planning and Security

The planner operates inside Noema’s structural security boundary.

The following are untrusted:

user input
model output
retrieved enterprise text
external tool output
external provider responses
event payloads

They must not directly grant:

* authority
* capabilities
* permissions
* resource access
* credentials
* execution rights
* idempotency exemptions

The model has no credentials or direct enterprise execution access.

No free-form model output may directly reach the execution boundary.

⸻

67. Planning and Read-Only Actions

Planning must not assume that read-only Actions are consequence-free.

A read-only Action may:

* expose protected information
* perform deep cross-system investigation
* consume scarce resources
* trigger external workflows
* create records
* create operational side effects
* establish information required for consequential decisions

Therefore:

read-only
≠
non-consequential

Planning must apply the same bounded capability, authorization, Trust, and data-boundary semantics where required.

⸻

68. Planning and Operational Memory

Operational Memory may retain:

* plan history
* plan versions
* candidate strategies
* selected plans
* replanning reasons
* execution relationships
* failures
* reconciliation results
* recovery decisions

Operational Memory is not a source of enterprise Business State.

Historical planning records may explain why a plan was selected without becoming authoritative evidence that the plan’s assumptions remain true.

⸻

69. Planning Invariants

Invariant 1

Planning occurs only after Intent has reached sufficient semantic resolution for the intended level of execution.

Invariant 2

Planning must never resolve material source-of-Intent ambiguity by guessing.

Invariant 3

A plan is not an execution.

Invariant 4

A plan is not authorization.

Invariant 5

A plan cannot contain an Action for which the required Capability does not exist.

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

Plans entering consequential execution must have stable identity and version.

Invariant 13

Plans must not be silently mutated after consequential execution begins.

Invariant 14

Replanning must preserve the lineage of previous plans and executions.

Invariant 15

A replanned workflow must account for Actions already executed and their established or uncertain effects.

Invariant 16

A plan must never claim an Outcome merely because its Actions were planned.

Invariant 17

A valid plan must still be evaluated against runtime state where required.

Invariant 18

The system must prefer a safe feasible plan over an optimized but unsafe plan.

Invariant 19

The planner must not invent capabilities, permissions, authority, Actions, or Action Contract semantics.

Invariant 20

Material changes to Intent create a new Intent version and require appropriate plan lineage rather than silent plan mutation.

Invariant 21

A plan must not treat model confidence as authoritative Fact Status.

Invariant 22

Current-state-dependent planning must use appropriate State Reconciliation rather than silently relying on stale or conflicting observations.

Invariant 23

Trust outcomes remain exactly EXECUTE, CLARIFY, ESCALATE, and REJECT.

Invariant 24

Plan states such as READY, BLOCKED, INFEASIBLE, and REQUIRES_RECONCILIATION must not be represented as additional Trust outcomes.

Invariant 25

A plan must preserve the exact Intent version, relevant semantic contract versions, and decision context required for causal auditability.

Invariant 26

A plan must not execute through arbitrary model-generated operations outside the Enterprise Action Graph, Capability Registry, Action Registry, and Action Contract boundaries.

Invariant 27

Plan replay must not create new enterprise business occurrences by default.

Invariant 28

Historical plans must remain interpretable according to the semantic versions under which they were created.

Invariant 29

A plan must not silently continue after a material invalidating change to Intent, state, capability, policy, authorization, contract, or resource conditions.

Invariant 30

Planning must preserve the distinction between expected state transitions and established enterprise Business State.

⸻

70. Canonical Mental Model

                         SOURCE OF INTENT
                                │
                                ▼
                       CANDIDATE INTERPRETATION
                                │
                                ▼
                    HARD SCHEMA VALIDATION / ADMISSION
                                │
                                ▼
                         ADMITTED INTENT
                                │
                                ▼
                         INTENT RESOLUTION
                                │
                                ▼
                   CONTEXT / STATE RECONCILIATION
                                │
                                ▼
                             PLAN
                                │
                     ┌──────────┴──────────┐
                     │                     │
                 VALIDATE              INFEASIBLE
                     │
                     ▼
               TRUST / POLICY
                     │
          ┌──────────┼──────────┐
          │          │          │
       EXECUTE    ESCALATE   CLARIFY / REJECT
          │
          ▼
       CONTRACTS
          │
          ▼
       EXECUTION
          │
          ▼
   VERIFY / RECONCILE
          │
          ▼
        OUTCOME

And for adaptation:

                     PLAN v1
                        │
                        ▼
                    EXECUTION
                        │
             ┌──────────┼──────────┐
             │          │          │
          SUCCESS     FAILURE    UNKNOWN
                                   │
                                   ▼
                          STATE RECONCILIATION
                                   │
                         ┌─────────┴─────────┐
                         │                   │
                      RESOLVE              REPLAN
                                             │
                                             ▼
                                          PLAN v2

⸻

71. Final Definition

Planning is the controlled construction of an executable Action strategy from an admitted and sufficiently resolved Intent.

A plan defines the Actions, dependencies, conditions, constraints, resources, capabilities, and required control boundaries necessary to pursue an intended Outcome. It does not itself grant authority, execute Actions, establish enterprise state, or establish Outcome.

The core invariant is:

Noema plans before it acts,
but never confuses a plan with reality.
Planning determines a bounded strategy.
Trust determines whether the strategy may proceed.
Action Contracts define the executable boundary.
Execution records what actually happened.
Verification and State Reconciliation establish what can be known.
Outcome semantics classify what was established.

Planning therefore remains a bounded execution capability between semantic Intent resolution and consequential execution, with probabilistic candidate generation permitted only before deterministic validation, Trust, and Action Contract enforcement.