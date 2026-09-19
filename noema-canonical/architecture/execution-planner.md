Execution Planner

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/execution-planner.md

⸻

1. Definition

The Execution Planner is the Noema architectural component responsible for transforming a trusted, resolved Intent into an explicit execution plan composed of actions, dependencies, ordering constraints, and required execution contracts.

The Execution Planner answers:

Given a trusted Intent, what must be executed, in what order, using which capabilities and contracts?

It does not answer:

May this Intent execute?

That is the responsibility of Trust.

It does not answer:

What does the user mean?

That is the responsibility of Intent Interpretation and Resolution.

It does not perform the resulting Actions.

That is the responsibility of the Execution layer and its consumers.

The Planner therefore sits between Trust and Execution.

⸻

2. Position in Noema

The canonical relationship is:

User Expression
       ↓
Intent Interpretation
       ↓
Intent Resolution
       ↓
Validation
       ↓
Trust Evaluation
       ↓
Trusted Intent
       ↓
Execution Planning
       ↓
Action Graph
       ↓
Execution Contracts
       ↓
Execution
       ↓
Outcome

The planner operates only on an Intent that has satisfied the requirements necessary for planning.

Planning must not be treated as authorization.

⸻

3. Core Principle

Noema must not allow execution to emerge implicitly from model reasoning.

The execution path must be explicit.

Therefore:

Trusted Intent
      ↓
Execution Plan
      ↓
Explicit Actions
      ↓
Dependencies
      ↓
Contracts
      ↓
Execution

The planner converts an abstract trusted objective into a representation that an execution consumer can inspect, validate, accept, and execute.

⸻

4. Planning vs Trust

Trust and planning are distinct.

Trust asks:

May this Intent proceed toward execution?

Planning asks:

What execution sequence can fulfill this Intent?

For example:

Intent:
Replace expired card

Trust may establish:

Intent = trusted
Authorization = satisfied
Policy = satisfied
Capability = available

The planner may then produce:

1. Verify card status
2. Create replacement request
3. Notify customer

Trust does not become planning merely because the Trust Engine knows which capabilities are available.

⸻

5. Planning vs Execution

The Planner creates an execution plan.

It does not execute the plan.

Conceptually:

Execution Planner
        │
        ▼
Execution Plan
        │
        ▼
Execution Consumer
        │
        ▼
Business System

The Planner must therefore remain free of hidden business-system side effects.

Creating a plan must not itself mutate the target system.

⸻

6. Planning Inputs

A planning operation may consume:

* resolved Intent
* validated Intent
* Trust decision
* Actor
* Context
* Constraints
* Available capabilities
* Action definitions
* Action contracts
* dependency information
* execution policies
* resource requirements
* temporal requirements
* relevant evidence
* execution boundaries

Conceptually:

Plan(
    Intent,
    Trust,
    Context,
    Capabilities,
    Contracts,
    Constraints
)
→ ExecutionPlan

The exact implementation contract remains architecture-dependent.

⸻

7. Planning Preconditions

An Intent should not enter execution planning unless the conditions required by the architecture have been satisfied.

At minimum, the Planner should be able to establish:

Intent is resolved
        AND
Intent is valid
        AND
Intent is trusted for planning
        AND
required capabilities are known

If these conditions are not satisfied, the Planner should not manufacture a plan that implies execution authority.

The appropriate lifecycle transition may instead be:

WAITING
BLOCKED
RE-EVALUATING

depending on the underlying condition.

⸻

8. Execution Plan

An Execution Plan is a structured representation of the work required to fulfill a trusted Intent.

Conceptually:

ExecutionPlan {
    intent
    actions
    dependencies
    ordering
    contracts
    preconditions
    postconditions
    constraints
    failure_semantics
    completion_conditions
    provenance
}

The exact schema is defined by the relevant architecture and execution specifications.

The important principle is:

An execution plan must be explicit enough that its intended execution behavior can be inspected before execution begins.

⸻

9. Actions

A plan consists of explicit Actions.

An Action should identify the operation that must be performed without relying on free-form model instructions.

Conceptually:

Action {
    action_id
    capability
    target
    inputs
    preconditions
    postconditions
    contract
}

The Action representation must remain compatible with the canonical Action and Capability definitions.

⸻

10. Action Graph

Execution plans may be represented as an Action Graph.

An Action Graph represents:

* Actions
* dependencies
* ordering
* prerequisites
* data flow
* conditional relationships
* completion requirements

Example:

A: Verify Customer
        │
        ▼
B: Create Replacement
        │
        ▼
C: Notify Customer

The graph makes execution dependencies explicit.

The Action Graph is defined separately in:

architecture/action-graph.md

⸻

11. Sequential Execution

Some plans require strict ordering.

Example:

Verify eligibility
        ↓
Create replacement
        ↓
Notify customer

The Planner must preserve such dependencies.

It must not reorder Actions merely because another ordering appears operationally convenient.

If:

B depends on A

then:

A → B

is a planning constraint.

⸻

12. Parallel Execution

Some Actions may be independent.

Example:

        ┌── Notify customer
        │
Verify ─┤
        │
        └── Record audit event

If the semantics permit independent execution, the Planner may represent the Actions as parallel branches.

However, parallelism must not be inferred merely for performance.

The Planner must establish that:

* Actions are independent
* their side effects do not conflict
* ordering is not semantically required
* the Intent permits such execution
* the relevant contracts permit parallel execution

⸻

13. Conditional Execution

A plan may contain conditional branches.

Example:

Verify account
      │
      ├── eligible → continue
      │
      └── ineligible → stop

Conditions must be explicit.

The Planner must not hide consequential branching inside model reasoning.

Conceptually:

Condition
    ↓
Branch
 ┌──┴──┐
 A     B

Each branch should have defined semantics.

⸻

14. Planning Must Preserve Intent Semantics

The Planner must not alter the objective of the Intent.

For example:

Intent:
Replace my expired card.

The Planner may decompose this into required Actions.

It must not silently transform the objective into:

Close account

or:

Issue a different product

unless such behavior is explicitly defined by the Intent semantics, policy, or Action contract.

Planning is decomposition, not reinterpretation.

⸻

15. Planning and Constraints

Constraints attached to the Intent must propagate into the execution plan where relevant.

Example:

Intent Constraint:
Do not contact customer by phone.

The Planner must not produce:

Action:
Call customer

unless the constraint has been explicitly superseded through an authoritative lifecycle event.

Planning must preserve applicable constraints.

⸻

16. Planning and Capabilities

Every executable Action should map to an explicit capability.

Conceptually:

Intent
  ↓
Action
  ↓
Capability
  ↓
Execution Contract
  ↓
Consumer

The Planner must not create executable Actions for capabilities that have not been established as available for the intended execution path.

Capability answers:

Can a system perform this operation?

It does not by itself establish:

Is this operation permitted?

That distinction remains governed by Trust.

⸻

17. Planning and Permission

The Planner must not use capability discovery as a substitute for authorization.

For example:

Capability:
DELETE_ACCOUNT

does not mean:

Actor:
authorized to delete account

The execution plan may reference authorization requirements, but the Planner must not independently manufacture authorization.

⸻

18. Planning and Action Contracts

Each executable Action should resolve to an explicit Action Contract.

Conceptually:

Action
  ↓
Contract
  ├── Inputs
  ├── Preconditions
  ├── Authorization
  ├── Constraints
  ├── Side Effects
  ├── Postconditions
  ├── Failure Semantics
  └── Idempotency

The Planner assembles the execution path.

The contract defines the terms under which the Action may execute.

⸻

19. Preconditions

A planned Action may require preconditions.

Examples:

Account exists
Card is expired
Customer is eligible
Replacement capability available

The Planner should preserve these conditions in the plan.

Where a precondition must be checked at execution time because business state may change, the plan should identify that requirement rather than assuming the earlier evaluation remains authoritative.

⸻

20. Postconditions

A plan should identify expected outcomes where they can be defined.

Example:

Action:
Create replacement card
Expected postcondition:
Replacement request exists

Postconditions provide the basis for outcome verification.

The Planner does not itself establish that the postcondition occurred.

The execution and verification layers do.

⸻

21. Planning and Business State

The Planner does not own authoritative business state.

It may reference business state required to construct a plan.

For example:

Card:
expired

may influence the plan.

But the banking system remains authoritative for the actual card state.

Therefore:

Observed business state
        ↓
Planning input
        ↓
Execution
        ↓
Authoritative business outcome

Noema must not treat the plan as the source of truth for business state.

⸻

22. Planning and Context

Context may influence planning.

Examples:

* Actor identity
* organizational role
* resource state
* available capabilities
* temporal constraints
* policy requirements
* system availability
* prior execution state

However, contextual information must not silently create authority.

Context helps determine the execution path.

Trust establishes whether the Intent may proceed.

⸻

23. Planning and Freshness

Planning may depend on information that can become stale.

Example:

T1:
Account status = ACTIVE
T2:
Plan generated
T3:
Account status changes
T4:
Execution begins

The Planner must not assume that every planning input remains authoritative indefinitely.

Where freshness is material, the plan should specify that the relevant condition must be rechecked before execution.

⸻

24. Planning and TOCTOU

Execution planning may occur before actual execution.

Therefore Noema can encounter time-of-check/time-of-use conditions.

Conceptually:

Validation
   ↓
Trust
   ↓
Planning
   ↓
Execution

Business state may change between each stage.

The Planner must therefore preserve final authoritative checks required by execution consumers.

A plan is not a guarantee that the world remains unchanged.

⸻

25. Planning Determinism

Given the same:

* Intent
* Context
* Trust decision
* Capabilities
* Action definitions
* Contracts
* Planning rules
* relevant versions

the Planner should produce the same execution plan, subject to explicitly defined nondeterministic infrastructure concerns.

Planning must not depend on arbitrary model variation for consequential decisions.

Where an LLM participates in planning, its output must be converted into a canonical plan representation and subjected to deterministic validation.

⸻

26. LLMs and Planning

LLMs may assist with:

* decomposition
* candidate Action selection
* dependency discovery
* plan proposal
* alternative plan generation

They should not be the final authority for executable planning.

The architectural pattern is:

Trusted Intent
      ↓
LLM / Planner Proposal
      ↓
Canonical Plan Representation
      ↓
Deterministic Plan Validation
      ↓
Execution Plan
      ↓
Execution Contract

The model may propose.

The architecture must establish.

⸻

27. Plan Validation

An Execution Plan should itself be validated before execution.

Validation may establish:

* every Action is defined
* every Action maps to a capability
* required inputs exist
* dependencies are valid
* graph contains no prohibited cycles
* ordering constraints are satisfiable
* contracts exist
* constraints are preserved
* required preconditions are represented
* completion conditions are represented
* execution boundaries are respected

A plan that cannot satisfy these requirements must not cross the execution boundary.

⸻

28. Cycles

A plan may contain dependencies.

For ordinary sequential execution, dependencies should normally form an acyclic graph.

Example:

A → B → C

is valid.

Where:

A → B
B → C
C → A

exists, the Planner must explicitly determine whether the execution model supports such a cycle.

A cyclic dependency must never be silently treated as executable.

⸻

29. Idempotency

The Planner should preserve idempotency requirements defined by Action Contracts.

For consequential Actions, retry behavior must be explicit.

Example:

Create replacement card

must not accidentally create multiple replacement requests merely because an execution consumer retries after an uncertain response.

Idempotency is therefore a contract concern that the Planner must preserve.

⸻

30. Failure Semantics

A plan must account for failure.

Possible outcomes include:

* Action failure
* timeout
* unavailable dependency
* rejected contract
* partial completion
* unknown execution result
* downstream system failure

The Planner should preserve the defined failure semantics of individual Actions.

It must not assume:

Plan generated
      =
Plan will succeed

⸻

31. Partial Failure

A multi-Action plan may partially execute.

Example:

A → COMPLETED
B → COMPLETED
C → FAILED

The Planner should therefore distinguish:

Plan validity

from:

Execution outcome

The plan remains a description of intended execution.

The Execution layer determines what actually happened.

⸻

32. Compensation

Some Actions may require compensation if a later Action fails.

Example:

Reserve resource
       ↓
Create transaction
       ↓
Notify system

If a later step fails, the system may require a compensating Action.

Compensation must be explicitly represented.

Noema must not assume that every failed Action can simply be rolled back.

⸻

33. Atomicity

Some composite Intents may require atomic execution.

Others may explicitly permit partial execution.

The Planner must preserve the semantics of the Intent and Action Contracts.

For example:

A
B
C

may require:

all succeed

or may permit:

A succeeds
B fails
C continues

Noema must not infer partial-execution permission merely because the graph permits it.

⸻

34. Human Intervention in Planning

Planning may identify conditions requiring human involvement.

Examples:

Approval required
Manual review required
Ambiguous branch
Unrecoverable execution condition

The Planner may therefore produce a plan containing an explicit human-intervention requirement.

Example:

Action:
Transfer funds
Requirement:
Human approval before execution

The presence of a human step does not constitute execution failure.

It is a valid bounded-autonomy mechanism.

⸻

35. Planning and Approval

If Trust determines:

WAITING_FOR_APPROVAL

the Planner should not create an execution plan that implies immediate execution unless the architecture explicitly permits pre-planning before approval.

The distinction is:

Plan may be prepared

versus:

Plan may be executed

These must not be conflated.

⸻

36. Plan Versioning

Execution plans may need version identifiers.

A plan should conceptually identify:

plan_id
plan_version
intent_id
intent_version
planning_rules_version
contract_versions
timestamp

This allows Noema to reconstruct which plan governed a particular execution attempt.

⸻

37. Planning Provenance

A plan should be traceable to its inputs.

At minimum, provenance may include:

* Intent identifier
* Intent version
* Trust evaluation identifier
* Context version
* capability identifiers
* Action definitions
* contract versions
* planning rule versions
* planner identity/version
* timestamp

This supports auditability and debugging.

⸻

38. Plan Immutability

Once an Execution Plan has been accepted for execution, material changes should produce a new plan version rather than silently mutating the existing plan.

Conceptually:

Plan V1
   ↓
material change
   ↓
Plan V2

This preserves execution history.

⸻

39. Trust Invalidation During Planning

A previously trusted Intent may become untrusted while planning is occurring.

Example:

READY
  ↓
Planning
  ↓
Authorization revoked

The existing plan must not automatically retain execution eligibility.

Trust must be re-evaluated according to the relevant Trust State Machine rules.

Planning does not freeze Trust indefinitely.

⸻

40. Plan Invalidation

A plan may become invalid if:

* Intent changes
* Trust expires
* authorization changes
* policy changes
* capability disappears
* relevant resource state changes
* contract changes
* material constraints change
* required evidence becomes stale

The plan should then be invalidated or re-planned according to the applicable architecture.

⸻

41. Replanning

Replanning should be triggered by material changes to planning inputs.

Conceptually:

Existing Plan
      ↓
Material Change
      ↓
Invalidate
      ↓
Re-evaluate Trust if required
      ↓
Re-plan
      ↓
New Execution Plan

Noema should not silently execute an obsolete plan.

⸻

42. Plan Execution Boundary

The execution boundary is crossed only when the execution consumer accepts the applicable Execution Contract.

The canonical sequence is:

Trusted Intent
      ↓
Execution Planning
      ↓
Plan Validation
      ↓
Execution Contract
      ↓
Consumer Acceptance
      ↓
Execution

Planning alone does not authorize execution.

⸻

43. Plan vs Contract

These concepts should remain distinct.

The Plan answers:

What sequence of Actions should fulfill the Intent?

The Contract answers:

Under what explicit conditions may this Action be executed?

Therefore:

Execution Plan
      ↓
Action
      ↓
Action Contract

A plan references contracts.

It does not replace them.

⸻

44. Plan vs Workflow

A workflow may represent a broader business process.

An Execution Plan is specifically concerned with the Actions required to fulfill a particular Intent.

Noema should avoid assuming that every enterprise workflow is an Execution Plan.

A workflow may contain:

* human processes
* organizational stages
* business procedures
* long-running state
* external approvals

An Execution Plan is the canonical representation of the execution path for an Intent.

⸻

45. Long-Running Plans

Some execution plans may span significant periods.

For example:

Request replacement
      ↓
Wait for production
      ↓
Wait for shipment
      ↓
Confirm delivery

The Planner must therefore support plans whose Actions do not complete within a single execution session.

Long-running execution must preserve:

* state
* provenance
* dependencies
* deadlines
* retries
* revalidation requirements
* Trust expiration semantics

⸻

46. Plan Resumption

A paused or interrupted plan may resume only when its continuation conditions remain valid.

Before resumption, Noema may need to re-evaluate:

* Trust
* authorization
* policy
* capability
* resource state
* relevant constraints
* execution preconditions

Resumption must not imply that the original conditions remain valid indefinitely.

⸻

47. Concurrent Intents

Multiple Intents may target the same business resources.

The Planner must not assume that independent Intent plans are globally independent merely because they are independently valid.

Example:

Intent A → modify Account X
Intent B → modify Account X

Concurrency semantics belong to the relevant execution contracts and authoritative systems.

Where conflicts are known, the plan should preserve the necessary serialization or locking requirements.

⸻

48. Resource Dependencies

Actions may depend on resources.

Conceptually:

Action A
   ↓
Resource R

A resource dependency may include:

* ownership
* availability
* reservation
* concurrency
* state
* capacity

The Planner should represent material resource dependencies explicitly where required.

⸻

49. Temporal Planning

Some Actions have temporal requirements.

Examples:

Execute before 17:00
Wait 24 hours
Do not execute before approval becomes active

Temporal constraints must be represented explicitly.

The Planner must not assume that a plan remains executable after a time boundary expires.

⸻

50. Planning and Risk

Risk may affect whether an Action can be planned or executed.

However, the Planner should not replace the Trust Engine’s risk evaluation.

The separation is:

Trust:
Is execution permitted?
Planner:
What execution path fulfills the trusted Intent?

Risk-related requirements established by Trust must be preserved by the plan.

⸻

51. Alternative Plans

There may be multiple valid ways to fulfill an Intent.

Example:

Intent:
Notify customer

Possible capabilities:

Email
SMS
Push notification

If policy and Intent semantics permit alternatives, the Planner may represent alternative execution paths.

Selection rules must be explicit.

The Planner must not select an alternative merely because an LLM considers it preferable.

⸻

52. Plan Selection

Where multiple plans exist, selection should be governed by explicit criteria such as:

* Intent constraints
* policy
* capability requirements
* contract compatibility
* resource availability
* temporal requirements
* cost constraints
* reliability requirements

The criteria and their precedence must be defined by the relevant architecture.

No implicit optimization objective should be assumed.

⸻

53. Plan Completeness

A plan should be considered complete only when all required execution semantics are represented.

Conceptually:

Plan Complete
    =
Actions defined
AND
Dependencies defined
AND
Contracts defined
AND
Inputs defined
AND
Required conditions represented
AND
Failure semantics represented
AND
Completion conditions represented

The exact completeness predicate remains implementation-specific.

⸻

54. Plan Serialization

Execution Plans should be representable in a canonical machine-readable form.

The serialized form should preserve:

* Action identity
* ordering
* dependencies
* parameters
* contracts
* conditions
* constraints
* versions
* provenance

The canonical serialization format is an implementation concern unless separately standardized.

⸻

55. Plan Inspection

Before execution, authorized components should be able to inspect the plan.

Inspection should allow determination of:

* what Actions will occur
* in what order
* against which targets
* using which capabilities
* under which contracts
* with which dependencies
* with which constraints
* what happens on failure

The plan should not require hidden model state to understand its intended execution.

⸻

56. Plan Explainability

Plan explainability means being able to account for the structural basis of the plan.

For example:

Intent:
Replace expired card
Plan:
1. Verify card eligibility
2. Request replacement
3. Notify customer
Reason:
Each Action satisfies an explicit requirement of the trusted Intent.

This does not require exposing private model reasoning.

The canonical requirement is structural and decision provenance.

⸻

57. Planning Auditability

Material planning events should be auditable.

Examples:

plan.created
plan.validated
plan.invalidated
plan.replanned
plan.accepted
plan.rejected
plan.expired

Each event should preserve sufficient provenance to reconstruct the planning lifecycle.

⸻

58. Planner Failure

The Planner may fail to produce a valid execution plan.

Examples:

* no suitable capability
* incompatible contracts
* unresolved dependency
* impossible ordering
* missing required input
* unsatisfied planning constraint
* invalid Action definition

Planner failure must not be converted into an executable plan merely to continue the lifecycle.

The resulting state may be:

WAITING
BLOCKED
HUMAN_INTERVENTION_REQUIRED

depending on the cause.

⸻

59. No Guessing in Planning

The Planner must not invent missing execution semantics.

Example:

Intent:
Send the report to John.

If the recipient remains unresolved, the Planner must not choose:

John_2

because it is statistically likely.

Planning begins only from sufficiently established Intent semantics.

⸻

60. No Hidden Actions

A plan must explicitly represent consequential Actions.

The Planner must not hide an Action inside:

* prompt text
* model instructions
* natural-language descriptions
* implicit tool calls
* undocumented side effects

If an Action matters to execution, it should be represented as an Action.

⸻

61. No Hidden Authority

The Planner must not create authority that does not exist elsewhere.

For example:

Planner:
"User probably intends this."

does not establish:

Authorization:
granted

The Planner operates within the authority established by Trust and the relevant execution contracts.

⸻

62. Consumer-Side Final Validation

The execution consumer may perform additional final checks.

This is expected because business state may change after planning.

Conceptually:

Noema Plan
      ↓
Consumer
      ↓
Final authoritative checks
      ↓
Execute / Reject

Consumer rejection does not necessarily mean that the plan was structurally invalid when created.

It means execution conditions changed or the consumer identified a condition authoritative to its domain.

⸻

63. Execution Outcome

The Planner does not determine execution outcome.

The relationship is:

Intent
  ↓
Trust
  ↓
Plan
  ↓
Execution
  ↓
Outcome

Possible outcomes include:

COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN

The exact outcome model belongs to the execution architecture.

⸻

64. Composite Intents

Composite Intents may produce composite plans.

Example:

Intent:
Close account and notify all administrators.

Potential plan:

A: Verify closure eligibility
        ↓
B: Close account
        ↓
C: Notify administrators

The Planner must preserve dependencies and the semantics of the composite Intent.

If the Intent requires atomic behavior, the plan must represent the relevant atomicity or compensation semantics.

⸻

65. Partial Execution Semantics

If partial execution is permitted:

A → COMPLETED
B → FAILED
C → WAITING

may be valid.

If partial execution is not permitted, the plan must enforce the appropriate execution semantics.

Noema must not infer partial execution permission from implementation convenience.

⸻

66. Human Approval as a Planning Node

Where approval is required, the plan may explicitly contain a human approval requirement.

Example:

Verify transfer
       ↓
Request approval
       ↓
Execute transfer

The approval node does not itself perform the business Action.

It represents a required governance transition.

⸻

67. Plan Cancellation

A plan may become unnecessary or invalid before execution.

Examples:

* Actor cancels the Intent
* Intent changes
* authorization revoked
* policy changes
* resource no longer exists

Cancellation should be represented explicitly.

The Planner must not assume that an accepted plan must eventually execute.

⸻

68. Plan Expiration

A plan may contain an execution validity period.

Example:

valid_until = 10:30

After expiration, execution must not proceed solely because the plan previously existed.

The plan may require:

Trust re-evaluation
Plan regeneration
Contract regeneration

as appropriate.

⸻

69. Planning State

The Planner itself may maintain explicit lifecycle states.

A conceptual taxonomy is:

NOT_PLANNED
PLANNING
PLAN_READY
PLAN_INVALID
PLAN_EXPIRED
REPLANNING
CANCELLED

These are architectural planning states and must not be confused with Trust or Execution states.

⸻

70. Trust, Planning, and Execution State

The architectural separation is:

                 Intent
                   │
          ┌────────┼─────────┐
          ▼        ▼         ▼
      Validation  Trust    Context
                   │
                   ▼
                Planning
                   │
                   ▼
              Execution
                   │
                   ▼
                Outcome

Each layer has a distinct responsibility.

⸻

71. Recommended Architecture

A clean architecture is:

                 ┌───────────────┐
                 │     Intent    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │  Validation   │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │     Trust     │
                 └───────┬───────┘
                         │
                     Trusted
                      Intent
                         │
                         ▼
                 ┌───────────────┐
                 │ Execution     │
                 │   Planner     │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Action Graph  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Contracts   │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Consumer    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Outcome     │
                 └───────────────┘

⸻

72. Canonical Planning Flow

The canonical flow is:

Trusted Intent
      │
      ▼
Identify required capabilities
      │
      ▼
Select candidate Actions
      │
      ▼
Resolve dependencies
      │
      ▼
Construct Action Graph
      │
      ▼
Attach Action Contracts
      │
      ▼
Validate Plan
      │
      ▼
Execution Plan
      │
      ▼
Consumer Acceptance
      │
      ▼
Execution

⸻

73. Planning Invariants

Invariant 1

The Planner does not determine whether an Intent is trusted.

Invariant 2

The Planner does not execute Actions.

Invariant 3

Every consequential Action must be explicit.

Invariant 4

Every executable Action must map to an explicit capability and applicable contract.

Invariant 5

Planning must preserve Intent semantics.

Invariant 6

Planning must preserve applicable constraints.

Invariant 7

Planning must not manufacture authorization.

Invariant 8

Unknown mandatory planning conditions must not be treated as satisfied.

Invariant 9

Material changes may invalidate an existing plan.

Invariant 10

A plan does not guarantee execution success.

Invariant 11

Execution consumers remain authoritative for final business-state checks.

Invariant 12

Material plans must be versioned and traceable.

Invariant 13

The Planner must not silently invent missing Intent information.

Invariant 14

Partial execution must be explicitly permitted.

Invariant 15

Plan changes must be explicit and reconstructible.

⸻

74. Relationship to the Trust State Machine

The Planner operates primarily after Trust has established execution eligibility.

Conceptually:

EVALUATING
    ↓
READY
    ↓
PLANNING
    ↓
PLAN_READY
    ↓
CONTRACT_ACCEPTED
    ↓
EXECUTING

However, planning does not freeze Trust.

If a material Trust condition changes:

READY
  ↓
material change
  ↓
EVALUATING

the associated plan may become invalid.

The Planner must respect the Trust State Machine defined in:

trust/trust-state-machine.md

⸻

75. Relationship to Validation

Validation occurs at multiple architectural boundaries.

The Intent is validated before Trust.

The resulting Execution Plan must also be validated before execution.

Therefore:

Intent
  ↓
Intent Validation
  ↓
Trust
  ↓
Planning
  ↓
Plan Validation
  ↓
Execution

These validations serve different objects and must not be conflated.

⸻

76. Relationship to Context Engine

The Context Engine supplies relevant context used during planning.

For example:

Context:
Card is expired
Customer is eligible
Replacement capability available

The Planner uses those facts to construct the execution path.

The Context Engine does not itself create an execution plan.

⸻

77. Relationship to Action Graph

The Action Graph provides the structural representation of execution dependencies.

The Planner constructs or selects the graph.

Therefore:

Execution Planner
       ↓
Action Graph

The Action Graph should remain a reusable architectural abstraction rather than being embedded inside planner-specific logic.

⸻

78. Relationship to Execution Contracts

The Planner maps Actions onto executable contracts.

Conceptually:

Action
  ↓
Contract Selection
  ↓
Contract Validation
  ↓
Execution

The contract remains the explicit execution boundary.

⸻

79. Relationship to Outcome Verification

The Planner defines expected completion conditions where possible.

The Outcome/Verification layer determines whether those conditions actually occurred.

Therefore:

Planner:
"What should happen?"
Execution:
"What did the system do?"
Verification:
"Did the expected result occur?"

These questions must remain separate.

⸻

80. Final Definition

The Execution Planner is Noema’s deterministic planning layer for transforming a trusted Intent into an explicit, inspectable, dependency-aware execution plan composed of defined Actions, capabilities, and execution contracts.

The central invariant is:

Noema does not execute what the model merely proposes. A trusted Intent must be transformed into an explicit execution plan whose Actions, dependencies, constraints, and contracts can be validated before crossing the execution boundary.