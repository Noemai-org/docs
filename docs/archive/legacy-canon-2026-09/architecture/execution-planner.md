> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Execution Planner

Status: Foundational
Version: 0.3
Domain: Architecture
Canonical Path: architecture/execution-planner.md

⸻

1. Definition

The Execution Planner is the Noema architectural component responsible for transforming a trusted, resolved Intent into an explicit, inspectable Execution Plan composed of Actions, dependencies, ordering constraints, execution requirements, and applicable Execution Contracts.

The Execution Planner answers:

Given a trusted Intent, what must be executed, in what order, using which capabilities and contracts?

It does not answer:

May this Intent execute?

That is the responsibility of Trust.

It does not answer:

What does the Actor mean?

That is the responsibility of Intent Interpretation and Resolution.

It does not establish authorization.

That is the responsibility of Trust and the applicable authoritative authorization mechanisms.

It does not execute Actions.

Execution is performed through explicit Execution Contracts, durable orchestration where required, and execution consumers.

The Planner therefore occupies the architectural boundary between Trust and durable execution orchestration.

⸻

2. Position in Noema

The canonical relationship is:

Human Expression
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
Plan Validation
       ↓
Execution Contract
       ↓
Durable Workflow
       ↓
Execution Consumer
       ↓
Authoritative Business System
       ↓
Outcome Verification
       ↓
Outcome

The Planner establishes the intended execution structure.

The durable execution layer preserves and coordinates that structure across failures, delays, retries, restarts, external events, and long-running execution.

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
Execution Contracts
      ↓
Durable Execution
      ↓
Execution Consumers

A model may propose a plan.

The canonical Planner and deterministic validation establish the executable plan.

The resulting execution path must therefore be inspectable before consequential execution begins.

⸻

4. Planning vs Trust

Trust and planning are distinct architectural concerns.

Trust asks:

May this Intent proceed toward execution?

Planning asks:

What execution path can fulfill this Intent?

For example:

Intent:
Replace expired card

Trust may establish:

Intent = trusted
Authorization = satisfied
Policy = satisfied
Required capability = available

The Planner may then produce:

1. Verify card eligibility
2. Create replacement request
3. Notify customer

The fact that Trust has established execution eligibility does not cause Trust to become the planning mechanism.

Likewise, the Planner must not independently establish that an Actor is authorized.

⸻

5. Planning vs Execution

The Planner creates an Execution Plan.

It does not execute the plan.

The conceptual boundary is:

Execution Planner
        ↓
Execution Plan
        ↓
Durable Workflow
        ↓
Activities / Execution Consumers
        ↓
Business Systems

Creating a plan must not itself cause consequential business-side effects.

The Planner therefore remains free of hidden execution behavior.

⸻

6. Planning vs Durable Workflow

Noema must distinguish an Execution Plan from a durable workflow instance.

The Execution Plan describes:

What should happen.

The durable workflow describes:

How execution of that plan is maintained and coordinated over time.

Therefore:

Execution Plan
      ≠
Durable Workflow

The Plan is a Noema semantic artifact.

The Workflow is a runtime orchestration mechanism implementing or coordinating that artifact.

A workflow must therefore remain attributable to the Plan and Contracts from which it was established.

⸻

7. Durable Execution

Noema execution may span:

* seconds
* minutes
* hours
* days
* weeks
* external approvals
* asynchronous enterprise operations
* delayed business events

Execution therefore cannot depend on a single in-memory process remaining alive.

The architecture requires durable execution semantics for long-running or failure-sensitive execution.

A durable workflow orchestration system may provide:

* durable workflow state
* recovery
* retries
* timers
* signals
* asynchronous waiting
* continuation
* activity scheduling
* execution history

These capabilities support Noema execution architecture but do not replace Noema’s semantic boundaries.

⸻

8. Temporal’s Architectural Role

Temporal is the reference implementation technology for durable workflow orchestration.

Its architectural responsibility is operational execution durability.

Conceptually:

Noema Semantic Layer
────────────────────────
Intent
Trust
Plan
Contract
Policy
Outcome Semantics
Provenance
        │
        ▼
Temporal
────────────────────────
Workflow State
Timers
Retries
Signals
Durability
Recovery
Activity Scheduling
        │
        ▼
Execution Consumers

Temporal must not become the authoritative source of:

* Intent
* authorization
* Trust
* policy
* capability
* business state
* business ownership
* Noema outcome semantics

Temporal provides durable mechanics.

Noema retains semantic authority.

⸻

9. Planning Inputs

A planning operation may consume:

* resolved Intent
* validated Intent
* Trust decision
* Actor
* Context
* constraints
* available capabilities
* Action definitions
* Execution Contracts
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

10. Planning Preconditions

An Intent should not enter execution planning unless the conditions required by the architecture have been satisfied.

At minimum:

Intent is resolved
AND
Intent is valid
AND
Intent is trusted for planning
AND
required capabilities are known

If these conditions are not satisfied, the Planner must not manufacture an executable plan.

The lifecycle may instead transition to an appropriate state such as:

WAITING
BLOCKED
HUMAN_INTERVENTION_REQUIRED
RE-EVALUATING

Unknown mandatory conditions must not be treated as satisfied.

⸻

11. Execution Plan

An Execution Plan is a structured representation of the work required to fulfill a trusted Intent.

Conceptually:

ExecutionPlan {
    plan_id
    plan_version
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
    temporal_requirements
    provenance
}

The exact schema is defined by the relevant Noema specifications.

The critical architectural requirement is:

The plan must be explicit and inspectable before it crosses the execution boundary.

⸻

12. Actions

A plan consists of explicit Actions.

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

An Action must not be represented solely as free-form model instructions.

If an operation is consequential to execution, that operation must have an explicit Action representation.

⸻

13. Action Graph

An Execution Plan may be represented as an Action Graph.

An Action Graph represents:

* Actions
* dependencies
* ordering
* prerequisites
* data flow
* conditional relationships
* completion requirements

For example:

A: Verify Customer
        ↓
B: Create Replacement
        ↓
C: Notify Customer

The Action Graph represents execution structure.

The Execution Planner constructs or selects the applicable graph.

The Action Graph remains a reusable architectural abstraction and is not merely internal Planner logic.

⸻

14. Sequential Execution

Where strict ordering is required:

Verify eligibility
        ↓
Create replacement
        ↓
Notify customer

the Planner must preserve the dependency.

If:

B depends on A

then:

A → B

is a planning constraint.

The Planner must not reorder consequential Actions merely because another ordering appears operationally convenient.

⸻

15. Parallel Execution

Independent Actions may be represented as parallel branches where permitted.

For example:

             ┌── Notify customer
             │
Verify ──────┤
             │
             └── Record audit event

Parallelism must be supported by the applicable:

* Action semantics
* Contracts
* resource constraints
* business rules
* execution requirements

The Planner must establish that ordering is not semantically required and that relevant side effects do not conflict.

Parallelism must not be inferred solely for performance.

⸻

16. Conditional Execution

Plans may contain explicit conditional branches.

For example:

Verify account
      │
      ├── eligible → continue
      │
      └── ineligible → stop

Consequential branching must be represented explicitly.

Conditions must have defined semantics.

The Planner must not hide consequential branching inside model reasoning or undocumented workflow behavior.

⸻

17. Planning Must Preserve Intent Semantics

The Planner decomposes an Intent.

It must not silently reinterpret the Intent.

For example:

Intent:
Replace my expired card

may produce:

Verify eligibility
Create replacement
Notify customer

It must not silently become:

Close account

unless that behavior is explicitly established by authoritative Intent semantics, policy, or an applicable Action Contract.

Planning is decomposition, not reinterpretation.

⸻

18. Planning and Constraints

Constraints attached to an Intent must propagate into the Execution Plan where applicable.

Example:

Constraint:
Do not contact customer by phone

must prevent the Planner from producing:

Action:
Call customer

unless an authoritative subsequent lifecycle transition changes the applicable constraint.

The Planner must preserve applicable constraints rather than treating them as advisory text.

⸻

19. Planning and Capabilities

Every executable Action should map to an explicit Capability.

The relationship is:

Intent
  ↓
Action
  ↓
Capability
  ↓
Execution Contract
  ↓
Execution Consumer

Capability establishes what a system can perform.

It does not establish permission to perform that operation.

The Planner must not create executable Actions for capabilities that have not been established as available for the intended execution path.

⸻

20. Planning and Permission

Capability discovery must not be used as a substitute for authorization.

For example:

Capability:
DELETE_ACCOUNT

does not imply:

Actor:
authorized to delete account

Authorization remains governed by Trust and the applicable authoritative authorization mechanisms.

The Planner may reference authorization requirements established elsewhere, but it must not manufacture authorization.

⸻

21. Planning and Execution Contracts

Each executable Action should resolve to an explicit Execution Contract.

Conceptually:

Action
  ↓
Execution Contract
  ├── Inputs
  ├── Preconditions
  ├── Authorization Requirements
  ├── Constraints
  ├── Expected Effects
  ├── Postconditions
  ├── Failure Semantics
  └── Idempotency

The Planner assembles the execution path.

The Contract defines the explicit conditions under which an Action may execute.

The Plan references applicable Contracts; it does not replace them.

⸻

22. Preconditions

Actions may have preconditions such as:

* Account exists
* Card is expired
* Customer is eligible
* Capability is available
* Required approval exists

Where a precondition depends on mutable authoritative business state, the Plan should identify whether that condition must be checked again immediately before execution.

A planning-time observation must not automatically be treated as an execution-time guarantee.

⸻

23. Postconditions

Plans should identify expected outcomes where they can be defined.

Example:

Action:
Create replacement card
Expected postcondition:
Replacement request exists

The Planner defines the expected condition.

Execution and outcome verification determine whether that condition actually occurred.

⸻

24. Planning and Business State

The Planner does not own authoritative business state.

The relationship is:

Observed Business State
        ↓
Planning Input
        ↓
Execution
        ↓
Authoritative Business Outcome

The enterprise system remains authoritative for the business mutation and state that it owns.

A Plan is not a substitute for authoritative business state.

⸻

25. Planning and Context

Context may influence planning.

Examples include:

* Actor identity
* organizational role
* resource state
* available capabilities
* temporal constraints
* policy requirements
* system availability
* prior execution state

Context does not itself establish authority.

Context helps determine the applicable execution path within authority already established elsewhere.

⸻

26. Planning and Freshness

Planning inputs can become stale.

For example:

T1  Account = ACTIVE
T2  Plan generated
T3  Account becomes BLOCKED
T4  Execution begins

The Plan must identify conditions requiring final authoritative validation.

A Plan is not a guarantee that the world remains unchanged.

⸻

27. Planning and TOCTOU

Noema must account for time-of-check/time-of-use conditions.

The lifecycle may be:

Validation
   ↓
Trust
   ↓
Planning
   ↓
Durable Workflow
   ↓
Execution

Business state may change between each stage.

Therefore, execution consumers remain responsible for authoritative final checks where required.

Planning-time validation does not eliminate execution-time validation requirements.

⸻

28. Planning Determinism

Given equivalent:

* Intent
* Context
* Trust decision
* Capabilities
* Action definitions
* Contracts
* planning rules
* relevant versions

the Planner should produce the same canonical Execution Plan, subject to explicitly defined infrastructure variation.

Consequential planning decisions must not depend on arbitrary model variation.

Where model-assisted planning is used, model output must be canonicalized and subjected to deterministic validation before it becomes executable planning state.

⸻

29. LLMs and Planning

LLMs may assist with:

* decomposition
* candidate Action selection
* dependency discovery
* plan proposal
* alternative plan generation

They must not become the final authority for executable planning.

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

The model proposes.

The architecture establishes.

⸻

30. Plan Validation

An Execution Plan must be validated before entering executable workflow state.

Validation may establish:

* every Action exists
* every Action maps to a Capability
* required inputs exist
* dependencies are valid
* prohibited cycles do not exist
* ordering constraints are satisfiable
* Contracts exist
* constraints are preserved
* required preconditions are represented
* completion conditions exist
* temporal requirements are represented
* execution boundaries are respected

An invalid Plan must not enter executable workflow state.

⸻

31. Cycles

A Plan may contain dependencies.

For ordinary sequential execution, dependencies should normally form an acyclic graph.

For example:

A → B → C

is valid.

A dependency structure such as:

A → B
B → C
C → A

must not be silently treated as executable.

If the execution model explicitly supports cycles, their semantics must be established by that model.

Otherwise, a prohibited cycle is a Plan validation failure.

⸻

32. Plan Completeness

A Plan is complete when the semantics required for execution are represented.

Conceptually:

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

A durable workflow must not compensate for an incomplete Plan.

Workflow durability preserves execution; it does not supply missing semantic planning information.

⸻

33. Durable Workflow Creation

Once the Execution Plan has passed validation, Noema may establish a durable workflow instance.

Conceptually:

Execution Plan
      ↓
Plan Validation
      ↓
Workflow Definition
      ↓
Workflow Instance
      ↓
Activities

The workflow instance must reference the canonical Plan and relevant versions.

Creating a workflow instance does not create business authority.

⸻

34. Workflow Identity

A durable workflow should be traceable to the Noema execution lifecycle.

Conceptually:

intent_id
plan_id
plan_version
execution_id
workflow_id
contract_id

These identifiers allow correlation across:

Intent
   ↓
Trust
   ↓
Plan
   ↓
Workflow
   ↓
Activity
   ↓
Execution Record
   ↓
Outcome

⸻

35. Workflow vs Execution Plan

The distinction is:

Plan:
"What should happen?"
Workflow:
"Maintain and coordinate execution of that plan."
Activity:
"Perform an individual external operation."

The Plan is semantic.

The Workflow is durable orchestration.

The Activity is an execution mechanism.

These concepts must not be conflated.

⸻

36. Activities and Execution Consumers

External side effects should occur through explicit execution boundaries.

Conceptually:

Workflow
    ↓
Activity
    ↓
Execution Contract
    ↓
Execution Consumer
    ↓
Enterprise System

Activities must not become uncontrolled mechanisms for arbitrary model-generated actions.

An Activity should execute only the Actions represented by the applicable Plan and Contract.

⸻

37. Workflow Determinism

Where Temporal is used, workflow orchestration logic must satisfy Temporal’s deterministic workflow execution requirements.

Consequential external side effects, nondeterministic operations, and external I/O must not be hidden inside deterministic workflow logic.

Conceptually:

Workflow
    │
    ├── deterministic orchestration
    ├── timers
    ├── state transitions
    └── activity scheduling
             │
             ▼
         Activities
             │
             └── external I/O / side effects

Temporal’s workflow model governs durable orchestration behavior.

Noema’s Planner remains responsible for semantic planning.

⸻

38. Retries and Idempotency

Durable execution may require retries.

Retries must preserve Action Contract semantics.

For example:

Create replacement card

must not create multiple replacement requests merely because an Activity is retried.

Retry behavior must therefore be governed by:

* idempotency
* Execution Contracts
* consumer semantics
* failure classification

Retries are an execution concern.

They must not become a mechanism for bypassing Trust or Contract requirements.

⸻

39. Timeouts

Actions may have explicit timeout requirements.

Examples include:

* Activity timeout
* Workflow timeout
* approval deadline
* business validity deadline

These are distinct concepts.

A Temporal timeout does not automatically mean that a Noema Intent has semantically failed.

The resulting Noema state must be established according to the applicable failure and outcome semantics.

⸻

40. Long-Running Execution

Noema must support execution that spans long periods.

For example:

Request replacement
      ↓
Wait for production
      ↓
Wait for shipment
      ↓
Confirm delivery

Durable workflow orchestration may maintain execution state while:

* waiting for external events
* waiting for human approval
* waiting for time
* waiting for enterprise systems
* retrying transient failures

Long-running execution must preserve relevant:

* state
* provenance
* dependencies
* deadlines
* retry semantics
* revalidation requirements
* Trust expiration semantics

⸻

41. Signals and External Events

Long-running execution may depend on external events.

Conceptually:

Workflow
   ↓
WAITING
   ↓
External Event
   ↓
Workflow Resumes
   ↓
Re-evaluation
   ↓
Continue / Block / Escalate

An external event must not automatically be treated as sufficient authority merely because it resumes a workflow.

The event must be interpreted according to Noema’s state and Trust semantics.

⸻

42. Human Intervention

Human intervention may be represented as an explicit durable waiting state.

For example:

Workflow
    ↓
WAITING_FOR_HUMAN
    ↓
Human Decision
    ↓
Re-evaluation
    ↓
Continue / Block / Cancel

A workflow waiting for approval must not be interpreted as already authorized execution.

Human approval remains a governance transition whose semantics are established by the relevant Trust and execution architecture.

⸻

43. Trust During Durable Execution

Trust does not automatically remain valid for the lifetime of a workflow.

A long-running workflow may encounter:

* authorization changes
* policy changes
* expired evidence
* capability changes
* resource changes
* Intent changes
* risk changes

Therefore:

READY
  ↓
Planning
  ↓
Durable Execution
  ↓
Material Change
  ↓
Re-evaluate Trust
  ↓
Continue / Block / Cancel

Durability must not become a mechanism for bypassing newly applicable Trust requirements.

A durable workflow preserves execution state.

It does not preserve expired authority.

⸻

44. Replanning

Material changes may invalidate a Plan.

The canonical response is:

Existing Plan
      ↓
Material Change
      ↓
Invalidate
      ↓
Re-evaluate
      ↓
Re-plan
      ↓
New Plan

Material changes may include:

* Intent changes
* Trust changes
* authorization changes
* policy changes
* capability changes
* resource-state changes
* Contract changes
* material constraint changes
* stale required evidence

Noema must not silently continue executing an obsolete Plan.

⸻

45. Plan Immutability and Versioning

Once a Plan has entered execution, material modifications should produce a new Plan version.

Conceptually:

Plan V1
   ↓
Material Change
   ↓
Plan V2

Historical Plan V1 must remain reconstructible.

The workflow must remain attributable to the Plan version under which its execution was initiated.

A material change must not silently mutate execution history.

⸻

46. Workflow Resumption

A durable workflow may resume after:

* process failure
* infrastructure restart
* worker restart
* temporary service unavailability
* long waiting periods

Resumption must not imply that all semantic conditions remain valid.

Before consequential continuation, Noema may need to re-evaluate:

* Trust
* authorization
* policy
* capability
* resource state
* Contract validity
* temporal constraints
* relevant Intent constraints

Durability preserves execution state.

It does not preserve expired authority or stale business assumptions.

⸻

47. Compensation

Some Plans require compensating Actions when later Actions fail.

For example:

Reserve resource
      ↓
Create transaction
      ↓
Notify system

If a later Action fails, a compensation Action may be required.

Compensation must be explicit.

Noema must not assume that enterprise operations are transactionally reversible.

⸻

48. Partial Execution

A multi-Action Plan may partially execute.

For example:

A → COMPLETED
B → COMPLETED
C → FAILED

The Plan remains the description of intended execution.

The Execution Record and Outcome Engine establish what actually happened.

Partial execution must therefore be represented explicitly.

⸻

49. Atomicity

Composite Intents may have different atomicity semantics.

Some may require:

A + B + C
=
all succeed

Others may permit:

A succeeds
B fails
C continues

The Planner must preserve the semantics established by the Intent and applicable Contracts.

Durable orchestration does not automatically make a distributed operation atomic.

Noema must not infer partial-execution permission from implementation convenience.

⸻

50. Concurrent Intents

Multiple Intents may target the same resources.

For example:

Intent A → Account X
Intent B → Account X

The Planner must not assume global independence.

Concurrency semantics belong to the applicable:

* Execution Contracts
* resource controls
* authoritative systems
* explicit serialization requirements

Where serialization is semantically required, the Plan must preserve that requirement.

⸻

51. Resource Dependencies

Actions may depend on resources.

Conceptually:

Action A
   ↓
Resource R

A resource dependency may involve:

* ownership
* availability
* reservation
* concurrency
* state
* capacity

Material resource dependencies should be represented explicitly where required for correct execution.

⸻

52. Temporal Planning

Actions may contain temporal requirements.

Examples:

Execute before 17:00
Wait 24 hours
Do not execute before approval
Execute only while authorization is valid

Temporal requirements must be explicit.

A durable workflow may implement timers and waiting, but semantic validity of the temporal condition remains a Noema concern.

⸻

53. Plan Expiration

A Plan may contain:

valid_until

After expiration, the existence of the Plan alone does not permit execution.

The appropriate response may include:

* Trust re-evaluation
* Plan revalidation
* new Plan generation
* Contract regeneration

as required by the applicable architecture.

⸻

54. Workflow Cancellation

A workflow may be cancelled because:

* Actor cancels the Intent
* Intent changes
* Trust is revoked
* authorization is revoked
* policy changes
* resource becomes unavailable
* Plan becomes invalid

Cancellation must be represented explicitly.

A previously accepted workflow is not necessarily required to reach business completion.

⸻

55. Failure Semantics

Failures must remain typed.

Potential classes include:

* Intent failure
* Context failure
* Validation failure
* Trust block
* Authorization failure
* Capability failure
* Planning failure
* Contract rejection
* Workflow failure
* Activity failure
* Timeout
* Partial execution
* Outcome failure
* Unknown outcome

Durable orchestration failure mechanisms must map into Noema’s semantic failure model rather than replacing it.

⸻

56. Unknown Execution State

Execution may produce an unknown result.

For example:

Activity request sent
        ↓
Connection lost
        ↓
Result unknown

The system must not automatically conclude:

FAILED

or:

COMPLETED

without appropriate evidence.

The result may remain:

UNKNOWN

and require reconciliation with the authoritative enterprise system.

⸻

57. Consumer-Side Final Validation

Execution consumers may perform final authoritative checks.

The boundary is:

Noema Plan
      ↓
Execution Consumer
      ↓
Final Authoritative Checks
      ↓
Execute / Reject

This is expected because business state may change between planning and execution.

Consumer-side validation is complementary to earlier Intent validation, Trust evaluation, and Plan validation.

Consumer rejection does not necessarily mean that the Plan was structurally invalid when created.

It may mean that authoritative execution conditions changed.

⸻

58. Execution Outcome

The Planner does not determine execution outcome.

The canonical relationship is:

Intent
  ↓
Trust
  ↓
Plan
  ↓
Durable Workflow
  ↓
Execution
  ↓
Outcome

Possible outcomes include:

COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN

The Outcome Engine determines the semantic outcome from execution evidence and authoritative state.

⸻

59. Plan Provenance

A Plan should preserve provenance including:

* Intent identifier
* Intent version
* Trust evaluation identifier
* Context references
* Capability identifiers
* Action definitions
* Contract versions
* planning-rule versions
* Planner version
* timestamp
* workflow identifier where applicable

This permits reconstruction of the planning conditions and execution path associated with a particular Plan.

⸻

60. Workflow Provenance

Where durable workflow orchestration is used, provenance should correlate:

Intent
   ↓
Trust Decision
   ↓
Plan
   ↓
Contract
   ↓
Workflow
   ↓
Activity
   ↓
Execution Record
   ↓
External Operation
   ↓
Outcome

Temporal workflow history may provide execution evidence.

Noema’s provenance model remains the canonical semantic audit structure.

⸻

61. Plan Inspection

Before execution, authorized components should be able to inspect:

* Actions
* ordering
* targets
* capabilities
* Contracts
* dependencies
* constraints
* preconditions
* failure semantics
* completion conditions
* temporal requirements

The Plan must not require hidden model state to understand its intended execution.

⸻

62. Plan Explainability

Plan explainability means being able to account for the structural basis of the Plan.

For example:

Intent:
Replace expired card
Plan:
1. Verify card eligibility
2. Request replacement
3. Notify customer

The explanation is structural:

Each Action satisfies an explicit requirement
of the trusted Intent.

This does not require exposing private model reasoning.

The canonical requirement is inspectable planning structure and decision provenance.

⸻

63. No Hidden Actions

Consequential Actions must not be hidden inside:

* prompts
* model instructions
* natural-language descriptions
* implicit tool calls
* undocumented workflow branches
* undocumented Activity behavior

If an operation matters to execution, it must be represented explicitly as an Action.

⸻

64. No Hidden Authority

The Planner must not create authority.

For example:

Planner:
"User probably intends this."

does not establish:

Authorization:
GRANTED

Likewise:

Temporal Workflow exists

does not establish:

Execution:
AUTHORIZED

Durable orchestration preserves execution state.

It does not grant permission.

⸻

65. Plan Selection

Where multiple Plans are possible, selection should be governed by explicit criteria such as:

* Intent constraints
* policy
* capability requirements
* Contract compatibility
* resource availability
* temporal requirements
* cost constraints
* reliability requirements

The selection criteria and their precedence must be explicit.

No implicit model preference should become an execution authority.

⸻

66. Alternative Execution Paths

An Intent may have multiple valid execution paths.

For example:

Intent:
Notify customer

may permit:

Email
SMS
Push Notification

where the applicable Intent semantics, policy, capabilities, and Contracts permit those alternatives.

The Planner may represent alternative paths.

Selection must be governed by explicit architectural criteria.

The Planner must not select an alternative merely because an LLM considers it preferable.

⸻

67. Planner Failure

The Planner may fail to produce a valid Plan.

Examples include:

* no suitable capability
* incompatible Contracts
* unresolved dependency
* impossible ordering
* missing input
* unsatisfied planning constraint
* invalid Action definition

Planner failure must not be converted into an executable Plan merely to continue the lifecycle.

The resulting state may be:

WAITING
BLOCKED
HUMAN_INTERVENTION_REQUIRED

depending on the underlying cause.

⸻

68. No Guessing in Planning

The Planner must not invent missing execution semantics.

Example:

Intent:
Send the report to John.

If the recipient remains unresolved, the Planner must not select:

John_2

merely because that recipient appears probable.

Planning begins only from sufficiently established Intent semantics.

Unknown mandatory information must remain unresolved.

⸻

69. Plan Serialization

Execution Plans must be representable in canonical machine-readable form.

The representation should preserve:

* Action identity
* dependencies
* ordering
* parameters
* Contracts
* conditions
* constraints
* versions
* provenance

The serialization technology remains an implementation concern unless separately standardized.

⸻

70. Planning Auditability

Material planning events should be auditable.

Examples include:

plan.created
plan.validated
plan.invalidated
plan.replanned
plan.accepted
plan.rejected
plan.expired
plan.cancelled

Where durable workflows are involved, corresponding workflow events should be correlated with these semantic events.

⸻

71. Plan and Workflow Versioning

Noema must distinguish semantic Plan versions from workflow implementation versions.

Conceptually:

Intent Version
       ↓
Plan Version
       ↓
Contract Version
       ↓
Workflow Implementation Version
       ↓
Execution

These versions must not be conflated.

A workflow implementation may evolve while historical execution remains attributable to the Plan, Contracts, and workflow implementation under which it ran.

⸻

72. Workflow and Business State

Workflow state is not business state.

For example:

Workflow:
ReplacementRequested = true

does not necessarily establish:

Banking System:
CardReplacement = CREATED

The latter remains authoritative to the banking system.

Workflow state represents orchestration state.

Enterprise state represents business state.

⸻

73. Reconciliation

Where execution produces an uncertain result, the workflow may enter a reconciliation state.

Conceptually:

Execution
    ↓
Result Unknown
    ↓
Reconciliation
    ↓
Authoritative System
    ↓
Confirmed Outcome

Reconciliation must not create an outcome from absence of evidence.

⸻

74. Planning State

The Planner may maintain conceptual states:

NOT_PLANNED
PLANNING
PLAN_READY
PLAN_INVALID
PLAN_EXPIRED
REPLANNING
CANCELLED

These are planning states.

They must not be confused with:

* Trust State
* Workflow State
* Execution State
* Outcome State

Each lifecycle has its own semantic responsibility.

⸻

75. Trust, Planning, and Durable Execution

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
             Plan Validation
                   │
                   ▼
          Execution Contract
                   │
                   ▼
           Durable Workflow
                   │
                   ▼
              Execution
                   │
                   ▼
                Outcome

Each stage has a distinct responsibility.

No stage should silently absorb the authority of another.

⸻

76. Recommended Architecture

The reference architecture is:

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
                    Trusted Intent
                         │
                         ▼
                 ┌───────────────┐
                 │    Execution  │
                 │    Planner    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │  Action Graph │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Plan Validation│
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Contracts   │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Durable     │
                 │   Workflow    │
                 │ / Temporal    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Activities  │
                 │ / Consumers   │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Authoritative │
                 │ Business      │
                 │ System        │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │    Outcome    │
                 └───────────────┘

Temporal is therefore positioned as durable execution infrastructure rather than as another semantic authority in the Noema decision chain.

⸻

77. Canonical Planning Flow

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
Attach Execution Contracts
      │
      ▼
Validate Plan
      │
      ▼
Execution Plan
      │
      ▼
Establish Durable Workflow
      │
      ▼
Consumer Acceptance
      │
      ▼
Execution
      │
      ▼
Outcome Verification

The durable workflow is established only after the semantic Plan has passed the applicable validation boundary.

⸻

78. Planning Invariants

Invariant 1

The Planner does not determine whether an Intent is trusted.

Invariant 2

The Planner does not execute Actions.

Invariant 3

Every consequential Action must be explicit.

Invariant 4

Every executable Action must map to an explicit Capability and applicable Contract.

Invariant 5

Planning must preserve Intent semantics.

Invariant 6

Planning must preserve applicable constraints.

Invariant 7

Planning must not manufacture authorization.

Invariant 8

Unknown mandatory planning conditions must not be treated as satisfied.

Invariant 9

Material changes may invalidate an existing Plan.

Invariant 10

A Plan does not guarantee execution success.

Invariant 11

Execution consumers remain authoritative for final business-state checks.

Invariant 12

Material Plans must be versioned and traceable.

Invariant 13

The Planner must not silently invent missing Intent information.

Invariant 14

Partial execution must be explicitly permitted.

Invariant 15

Plan changes must be explicit and reconstructible.

Invariant 16

Durable workflow state does not constitute Trust or authorization.

Invariant 17

Durable execution must not bypass renewed Trust evaluation when material conditions change.

Invariant 18

Workflow orchestration must remain distinct from authoritative business-state ownership.

Invariant 19

External side effects must occur through explicit execution boundaries.

Invariant 20

An execution workflow must remain attributable to the Plan, Contracts, and Trust decision under which it was initiated.

⸻

79. Relationship to Trust State

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
WORKFLOW_STARTED
    ↓
EXECUTING

However, planning and durable execution do not freeze Trust.

If a material Trust condition changes:

READY
  ↓
material change
  ↓
EVALUATING

the associated Plan or Workflow may become invalid.

The Planner must therefore respect the Trust State Machine defined by the Trust architecture.

⸻

80. Relationship to Validation

Validation occurs at multiple architectural boundaries.

The lifecycle is:

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
Contract Validation
  ↓
Durable Execution

These validations apply to different objects and must not be conflated.

Intent validation establishes that the Intent satisfies the requirements for Trust evaluation.

Plan validation establishes that the resulting execution structure satisfies the requirements for execution.

Contract validation establishes that the applicable Action may cross the execution boundary under explicit conditions.

⸻

81. Relationship to Outcome Verification

The Planner defines expected execution structure and completion conditions where possible.

It does not determine whether those conditions actually occurred.

Therefore:

Planner:
"What should happen?"
Execution:
"What operation was attempted or performed?"
Outcome Engine:
"What actually resulted?"

These questions must remain separate.

⸻

82. Final Definition

The Execution Planner is Noema’s deterministic planning layer for transforming a trusted, resolved Intent into an explicit, inspectable, dependency-aware Execution Plan composed of defined Actions, capabilities, constraints, and Execution Contracts.

The Plan may subsequently be realized through a durable workflow orchestration system such as Temporal.

The central architectural principle is:

Noema does not execute what the model merely proposes. A trusted Intent must be transformed into an explicit Execution Plan whose Actions, dependencies, constraints, and Contracts can be validated before crossing the execution boundary. Durable workflow orchestration preserves and coordinates that execution over time; it does not create authority.

The resulting relationship is:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Execution Plan
   ↓
Plan Validation
   ↓
Execution Contract
   ↓
Durable Workflow
   ↓
Execution Consumer
   ↓
Authoritative Business System
   ↓
Outcome Verification
   ↓
Outcome

This preserves the architectural separation:

NOEMA
determines
WHAT MAY HAPPEN
       │
       ▼
EXECUTION PLAN
determines
WHAT SHOULD HAPPEN
       │
       ▼
DURABLE ORCHESTRATION
ensures
EXECUTION CAN CONTINUE RELIABLY
       │
       ▼
EXECUTION CONSUMER
determines
WHAT OPERATION WAS ATTEMPTED OR PERFORMED
       │
       ▼
AUTHORITATIVE BUSINESS SYSTEM
determines
WHAT ACTUALLY OCCURRED IN THE BUSINESS DOMAIN
       │
       ▼
OUTCOME ENGINE
determines
WHAT RESULTED

The Planner therefore establishes the explicit semantic execution structure, while durable orchestration preserves that structure over time and execution consumers remain responsible for crossing the actual business-system execution boundary.