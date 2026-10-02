Noema Architecture Overview

Status: Foundational
Version: 0.2
Domain: Architecture
Canonical Path: architecture/overview.md

⸻

1. Definition

The Noema Architecture defines the system boundaries, components, durable workflows, state transitions, and relationships through which human intent is transformed into trusted, contract-governed execution and verified outcome.

Noema is an intent infrastructure layer.

Its architectural responsibility is to provide a controlled and durable path between:

Human Intent
     ↓
Meaning
     ↓
Context
     ↓
Validation
     ↓
Trust
     ↓
Action
     ↓
Execution
     ↓
Outcome

Noema does not replace the systems that own business state.

It coordinates intent across those systems while maintaining explicit control over:

* understanding
* context
* validation
* trust
* authority
* planning
* execution
* outcome
* provenance
* durable lifecycle state

The architecture therefore separates:

* probabilistic understanding from deterministic control
* Intent state from business state
* validation from Trust
* capability from permission
* planning from execution
* execution from outcome
* orchestration from business-state ownership

⸻

2. Architectural Objective

The architecture exists to make the intent-to-action boundary explicit, durable, observable, and recoverable.

The system must be able to establish:

1. what the Actor intends
2. what context is required to understand that Intent
3. whether the resulting Intent is valid
4. whether the Intent may proceed
5. what Action can satisfy the Intent
6. what capability can perform that Action
7. what contract governs execution
8. what execution occurred
9. what outcome resulted
10. what evidence and provenance support each transition
11. what happens if the process is interrupted
12. how the lifecycle resumes without losing authoritative state

The architecture must preserve the distinction between these concerns.

⸻

3. Core Architectural Boundary

The fundamental Noema boundary is:

                         NOEMA
┌─────────────────────────────────────────────────────┐
│                                                     │
│  Human Expression                                   │
│        ↓                                            │
│  Intent Engine                                      │
│        ↓                                            │
│  Context Engine                                     │
│        ↓                                            │
│  Validation                                         │
│        ↓                                            │
│  Trust Engine                                       │
│        ↓                                            │
│  Action Graph / Planning                            │
│        ↓                                            │
│  Execution Contract                                 │
│        ↓                                            │
│  Durable Execution / Orchestration                  │
│        ↓                                            │
│  Execution Consumer                                 │
│        ↓                                            │
│  Outcome Engine                                     │
│                                                     │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
              Existing Enterprise Systems

Noema owns the Intent-side lifecycle and the coordination necessary to safely cross the execution boundary.

External systems remain authoritative for the business state they own.

Durable workflow orchestration preserves Noema’s lifecycle across time, retries, failures, approvals, waiting periods, and external events. It does not become the authority for the business state being mutated.

⸻

4. Architectural Components

The canonical architecture consists of the following conceptual components:

* Intent Engine
* Context Engine
* Validation
* Trust Engine
* Action Graph
* Execution Planner
* Execution Contract
* Durable Execution / Workflow Orchestration
* Execution Record
* Outcome Engine
* Operational Memory
* AI Layer

These components are related but must not collapse into one undifferentiated agent.

Each component has a distinct architectural responsibility.

The architecture also requires a durable execution mechanism capable of maintaining long-running Noema workflows across:

* asynchronous operations
* retries
* failures
* waiting periods
* approvals
* human intervention
* external events
* process restarts
* execution timeouts
* compensation or recovery paths

⸻

5. Intent Engine

The Intent Engine transforms human expression into a canonical Intent representation.

Its responsibilities include:

* interpreting human expression
* constructing candidate Intent representations
* resolving semantic ambiguity
* incorporating permitted context
* requesting clarification when required
* maintaining Intent state
* producing a resolved Intent suitable for downstream validation

The Intent Engine may use probabilistic AI.

The resulting canonical Intent must remain structurally explicit and inspectable.

The Intent Engine does not determine execution authority.

That responsibility belongs to Trust.

⸻

6. Context Engine

The Context Engine acquires and organizes information required to understand, validate, and evaluate an Intent.

Context may include:

* Actor identity
* organizational context
* resource state
* relevant business state
* policies
* capabilities
* historical information
* temporal information
* external evidence

The Context Engine must distinguish between:

Context Available
Context Relevant
Context Authoritative
Context Fresh
Context Sufficient

Context is evidence for reasoning and evaluation.

Context does not automatically constitute permission.

External systems may remain authoritative for the facts that Context retrieves.

⸻

7. Validation

Validation establishes whether the canonical Intent is structurally complete, semantically applicable, and consistent with the rules and information required for its next lifecycle transition.

The conceptual flow is:

Resolved Intent
       ↓
Structural Validation
       ↓
Type Validation
       ↓
Reference Validation
       ↓
Domain Validation
       ↓
Constraint Validation
       ↓
Context Validation
       ↓
Temporal / Freshness Validation
       ↓
Validation Result

Validation produces structured results.

Conceptually:

VALID
INVALID
INCOMPLETE
UNKNOWN

Validation does not authorize an Intent.

Validation does not execute an Action.

Validation does not guarantee execution success.

Validation may be repeated whenever material conditions change.

⸻

8. Trust Engine

The Trust Engine determines whether a validated Intent has sufficient deterministic grounds to proceed toward execution.

Trust may evaluate:

* evidence
* authorization
* policy
* risk
* capability
* constraints
* context
* freshness
* approval
* confirmation
* execution eligibility

The Trust Engine is the principal control boundary between probabilistic understanding and executable action.

Conceptually:

Validated Intent
       ↓
Evidence
       +
Authorization
       +
Policy
       +
Risk Controls
       +
Capability
       +
Constraints
       +
Context
       ↓
Trust Decision

Trust must not be reduced to model confidence.

A Trust decision is a stateful, attributable decision based on explicit conditions and evidence.

⸻

9. Trust State

Trust is represented as an explicit lifecycle.

The canonical Trust states are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Execution state is represented separately.

For example:

NOT_STARTED
EXECUTING
COMPLETED
FAILED
UNKNOWN

The architectural distinction is important.

Trust establishes execution eligibility.

Execution establishes what actually happened.

Therefore:

READY ≠ COMPLETED
TRUST ≠ OUTCOME

Durable orchestration may persist and advance these states, but it does not redefine their semantics.

⸻

10. Action Graph

The Action Graph represents the capabilities and relationships through which an Intent can be satisfied.

It provides the structural representation of possible Actions and their dependencies.

Conceptually:

Intent
  ↓
Candidate Actions
  ↓
Action Dependencies
  ↓
Required Capabilities
  ↓
Executable Path

The Action Graph should make explicit:

* available Actions
* Action relationships
* dependencies
* prerequisites
* capabilities
* constraints
* sequencing requirements
* alternative execution paths where applicable

The Action Graph represents what can be done.

It does not independently establish what may be done.

Capability is not permission.

⸻

11. Execution Planner

The Execution Planner determines how a trusted Intent can be translated into an executable sequence of Actions.

Planning may involve:

* Action selection
* dependency resolution
* sequencing
* prerequisite satisfaction
* parallelization where permitted
* compensation requirements
* failure handling
* partial-execution semantics
* execution constraints

Planning must operate within the authority established by Trust.

The Planner cannot create authority that Trust has not established.

Conceptually:

Trusted Intent
      ↓
Action Graph
      ↓
Execution Planning
      ↓
Execution Plan
      ↓
Execution Contract

The Planner determines an executable strategy.

The durable workflow runtime is responsible for reliably carrying that strategy through its lifecycle.

Planning and orchestration therefore remain distinct concerns.

⸻

12. Durable Execution and Workflow Orchestration

Noema contains workflows that may outlive an individual request, process, model invocation, or application instance.

Examples include:

* waiting for clarification
* waiting for approval
* waiting for an external event
* retrying transient operations
* executing multi-step Actions
* coordinating multiple enterprise systems
* recovering from process interruption
* handling long-running execution
* maintaining execution state across failures
* performing compensation or recovery activities

These workflows require durable execution.

Noema should use Temporal as the workflow orchestration and durable execution substrate.

Temporal provides the runtime mechanism for maintaining workflow progress independently of the lifetime of an individual application process.

Architecturally:

Noema Semantic State
        │
        ▼
┌──────────────────────────┐
│ Durable Workflow         │
│ Orchestration             │
│                          │
│ Temporal                 │
└────────────┬─────────────┘
             │
       Activities / Calls
             │
     ┌───────┼────────┐
     ▼       ▼        ▼
  Context  Trust   Execution
  Systems  Systems Consumers

Temporal is an orchestration mechanism, not a semantic authority.

It does not determine:

* what an Intent means
* whether an Intent is valid
* whether an Actor is authorized
* whether Trust should be granted
* what business state is authoritative
* whether an Action is semantically appropriate

Those decisions remain within the corresponding Noema components and authoritative external systems.

12.1 Workflow vs Activity

Noema should distinguish durable workflow orchestration from external side effects.

Conceptually:

Workflow
   │
   ├── determine next lifecycle state
   ├── wait for events
   ├── wait for approval
   ├── schedule retry
   ├── coordinate activities
   └── maintain durable progress
          │
          ▼
      Activities
          │
          ├── context acquisition
          ├── validation calls
          ├── Trust evaluation
          ├── capability discovery
          ├── enterprise API calls
          └── outcome verification

The exact activity decomposition is an implementation concern.

The architectural principle is that external side effects must be explicitly controlled and attributable.

12.2 Temporal Is Not the Source of Truth

Temporal workflow state is operational orchestration state.

It must not be treated as the authoritative business record.

The distinction is:

Temporal
   ↓
Workflow execution state
Noema
   ↓
Intent / Trust / Execution / Outcome lifecycle state
Enterprise System
   ↓
Authoritative business state

These layers may reference one another without becoming interchangeable.

12.3 Durable Waiting

Waiting is a legitimate architectural state.

For example:

Trust
  ↓
WAITING_FOR_APPROVAL
  ↓
Durable Workflow Wait
  ↓
Approval Event
  ↓
Re-evaluation
  ↓
Continue / Block

Noema must not require a continuously running process merely to preserve a waiting state.

12.4 Retries

Retries must be governed by the semantics of the Action and contract.

A retry must not blindly repeat a consequential side effect.

Execution contracts should therefore define, where applicable:

* idempotency semantics
* retryability
* retry limits
* timeout behavior
* compensation behavior
* duplicate-detection requirements

Durable orchestration provides retry mechanisms; the Action Contract determines whether retrying is semantically safe.

12.5 Workflow Determinism

Workflow orchestration must preserve the distinction between:

* deterministic workflow state transitions
* external side effects
* probabilistic model calls

AI model calls and external system calls must not be treated as inherently deterministic workflow logic.

Where a workflow depends on external or nondeterministic information, the relevant result should be captured as an explicit event, activity result, evidence reference, or state transition.

⸻

13. Execution Contract

The Execution Contract is the explicit boundary between Noema’s decision process and the execution consumer.

A contract may establish:

* Action identity
* target
* inputs
* capability
* authorization requirements
* preconditions
* constraints
* expected effects
* postconditions
* failure semantics
* idempotency requirements
* retry semantics
* timeout semantics
* compensation semantics
* audit requirements

Conceptually:

Trusted Intent
      ↓
Execution Plan
      ↓
Execution Contract
      ↓
Consumer Acceptance
      ↓
Durable Execution
      ↓
Execution Consumer

Noema should execute contracts rather than arbitrary model-generated instructions.

⸻

14. Execution Record

The Execution Record provides the durable representation of what Noema instructed or attempted to execute.

It should provide enough information to reconstruct:

* which Intent produced the execution
* which Trust decision authorized it
* which Action was selected
* which contract governed it
* which consumer received it
* when execution occurred
* what execution state was reported
* what errors or failures occurred
* what retries occurred
* what outcome was observed

The Execution Record is part of Noema’s operational and audit boundary.

It is not necessarily the authoritative business record.

The target system remains authoritative for the business mutation it owns.

⸻

15. Outcome Engine

The Outcome Engine determines and records what happened after execution.

Its responsibilities include:

* receiving execution results
* evaluating postconditions
* reconciling expected and observed outcomes
* identifying partial execution
* identifying failures
* identifying unknown outcomes
* recording outcome evidence
* associating outcomes with the originating Intent

The fundamental relationship is:

Trust
  ↓
Execution Eligibility
  ↓
Execution
  ↓
Outcome

Trust does not determine outcome.

The external execution environment remains authoritative over actual business-state changes.

⸻

16. Operational Memory

Operational Memory preserves information required for Noema to maintain continuity across the Intent lifecycle.

It may contain:

* prior Intent state
* Trust history
* execution records
* outcome records
* relevant context
* provenance
* prior clarifications
* operational events
* references to external authoritative records

Operational Memory must not become an uncontrolled substitute for authoritative enterprise systems.

Where business state is owned externally, Noema should retain references and provenance rather than silently creating a competing source of truth.

Operational Memory and durable workflow state are related but not identical.

Workflow Runtime
        ↓
Durable orchestration state
Operational Memory
        ↓
Noema lifecycle / operational history
Enterprise Systems
        ↓
Authoritative business state

⸻

17. AI Layer

AI is a reasoning and interpretation capability within the architecture.

It may assist with:

* natural-language interpretation
* candidate Intent generation
* entity extraction
* semantic normalization
* context retrieval
* candidate Action selection
* clarification generation
* planning proposals
* anomaly identification
* evaluation and testing

AI does not become the authoritative source for:

* authorization
* policy enforcement
* deterministic validation
* Trust decisions
* business-state ownership
* execution authority

The architectural pattern is:

AI
 ↓
Proposal
 ↓
Deterministic Systems
 ↓
Established State
 ↓
Execution

The AI layer may propose.

Canonical Noema components establish.

The AI implementation remains model-agnostic.

⸻

18. End-to-End Architecture

The complete conceptual architecture is:

                         Human
                           │
                           ▼
                    Human Expression
                           │
                           ▼
                    ┌──────────────┐
                    │ Intent Engine│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │Context Engine│
                    └──────┬───────┘
                           │
                           ▼
                      Validation
                           │
                 ┌─────────┴─────────┐
                 │                   │
             INCOMPLETE           INVALID
                 │                   │
                 ▼                   ▼
          Clarification           Blocked
                 │
                 └─────────────┐
                               ▼
                         Trust Engine
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
              WAITING       BLOCKED        READY
                 │                           │
                 │                           ▼
                 │                      Action Graph
                 │                           │
                 │                           ▼
                 │                   Execution Planner
                 │                           │
                 │                           ▼
                 │                   Execution Contract
                 │                           │
                 │                           ▼
                 │                  Durable Workflow
                 │                  Orchestration
                 │                           │
                 │                           ▼
                 │                    Execution Consumer
                 │                           │
                 │                           ▼
                 │                    Execution Record
                 │                           │
                 │                           ▼
                 │                     Outcome Engine
                 │                           │
                 │                           ▼
                 └────────────────────── Outcome

This diagram represents the conceptual architecture rather than a mandatory implementation topology.

Components may be physically combined or distributed provided their semantic boundaries remain intact.

Durable orchestration may span multiple components and lifecycle transitions.

⸻

19. The Intent-to-Outcome Pipeline

The architecture can be reduced to the following canonical pipeline:

EXPRESS
   ↓
INTERPRET
   ↓
RESOLVE
   ↓
CONTEXTUALIZE
   ↓
VALIDATE
   ↓
TRUST
   ↓
SELECT
   ↓
PLAN
   ↓
CONTRACT
   ↓
ORCHESTRATE
   ↓
EXECUTE
   ↓
VERIFY
   ↓
OUTCOME

At multiple points the system may stop and transition into:

CLARIFY
WAIT
BLOCK
ESCALATE
FAIL

These are legitimate system behaviors.

The architecture must not optimize for apparent completion at the expense of correct state.

Durable workflow orchestration ensures that these states can persist across process boundaries and time.

⸻

20. Separation of Concerns

The architecture must preserve the following distinctions.

Intent vs Context

Intent represents what the Actor wants.

Context represents information relevant to understanding or evaluating that Intent.

Validation vs Trust

Validation establishes whether the Intent is valid.

Trust establishes whether the Intent may proceed.

Capability vs Permission

Capability establishes what a system can perform.

Permission establishes whether the Action may be performed for the Actor and circumstances.

Planning vs Execution

Planning determines how an Action can be performed.

Execution performs the Action.

Orchestration vs Execution

Orchestration coordinates workflow progression.

Execution performs the external side effect.

Execution vs Outcome

Execution records what was attempted or performed.

Outcome establishes what actually resulted.

Intent State vs Business State

Intent state belongs to Noema.

Business state remains owned by the authoritative external system.

These distinctions are architectural invariants.

⸻

21. State Ownership

Noema owns state concerning the Intent lifecycle.

Examples include:

* Intent State
* Validation State
* Trust State
* Planning State
* Execution State
* Outcome Association
* Provenance
* lifecycle events

The workflow runtime maintains durable workflow execution state required to carry the lifecycle through time.

External systems own their domain state.

Examples include:

* Account State
* Payment State
* Customer State
* Employee State
* Card State
* Inventory State

Noema may reference and act upon external state.

It should not silently redefine it.

⸻

22. External System Boundary

The execution architecture assumes that Noema operates across existing systems.

Conceptually:

                         Noema
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        Identity        Payments         CRM
          System          System        System
             │             │             │
             ▼             ▼             ▼
       Authoritative   Authoritative   Authoritative
       Identity State  Payment State   Customer State

Noema coordinates these systems through explicit interfaces.

The external system remains authoritative for the business operation it performs.

The workflow runtime does not change this authority model.

⸻

23. Authority Boundary

Authority flows through explicit mechanisms.

Actor
  ↓
Intent
  ↓
Validation
  ↓
Authorization
  ↓
Trust
  ↓
Action Contract
  ↓
Durable Execution
  ↓
Execution Consumer

No component may implicitly increase the authority established by the previous stage.

In particular:

AI inference
    ≠
authorization
Capability
    ≠
permission
Trust
    ≠
business ownership
Workflow orchestration
    ≠
business authority

⸻

24. Deterministic / Probabilistic Architecture

Noema intentionally combines probabilistic and deterministic systems.

The boundary is:

              PROBABILISTIC
────────────────────────────────
Interpretation
Candidate Intent
Semantic Inference
Retrieval
Planning Proposals
Clarification Generation
────────────────────────────────
              DETERMINISTIC
Validation
State
Authorization
Policy
Trust
Contracts
Execution Controls
Audit
────────────────────────────────
          DURABLE ORCHESTRATION
Workflow State
Waiting
Retries
Timers
Signals / Events
Lifecycle Coordination

Durable orchestration does not make a probabilistic decision deterministic.

It provides reliable execution of explicitly defined workflow semantics.

AI output cannot silently become authoritative merely because it was generated by a model.

⸻

25. Re-Evaluation

The architecture must support re-evaluation when material conditions change.

Examples include:

* Intent changes
* context changes
* authorization changes
* policy changes
* evidence expires
* capability becomes unavailable
* resource state changes
* risk changes
* time-sensitive conditions expire
* approval changes
* execution environment changes

Conceptually:

Current State
      ↓
Material Event
      ↓
Collect Current Conditions
      ↓
Validate / Evaluate
      ↓
New State

This prevents stale Trust and stale execution decisions from silently remaining valid.

Durable orchestration provides the mechanism for waiting for material events and resuming the lifecycle.

It does not eliminate the requirement to re-evaluate semantic or authorization conditions.

⸻

26. Execution Boundary

READY does not mean execution has occurred.

The canonical transition is:

READY
  ↓
Execution Contract
  ↓
Durable Orchestration
  ↓
Consumer Acceptance
  ↓
EXECUTING
  ↓
Outcome

The execution consumer remains an independent participant in the architecture.

The Trust Engine does not execute the Action.

The Planner does not execute the Action.

The AI does not execute the Action merely by generating an instruction.

The workflow runtime coordinates execution but does not become the business executor.

The execution boundary is explicit.

⸻

27. Failure Architecture

Failure must remain typed and observable.

Potential failure classes include:

* Intent Failure
* Context Failure
* Validation Failure
* Trust Block
* Authorization Failure
* Capability Failure
* Planning Failure
* Contract Rejection
* Workflow Failure
* Execution Failure
* Partial Execution
* Outcome Failure
* Unknown Outcome

The architecture must preserve these distinctions because recovery depends upon knowing where and why progression stopped.

Durable orchestration should distinguish retryable operational failures from deterministic business failures.

For example:

Transient network failure
        ↓
Retry may be appropriate
Authorization denied
        ↓
Retry does not create authority
Invalid Intent
        ↓
Clarification / correction required
Unknown execution outcome
        ↓
Reconciliation required

Retry behavior must therefore be governed by the semantics of the operation rather than applied indiscriminately.

⸻

28. Unknown State

Unknown information must not silently become a positive assertion.

Examples:

Authorization = UNKNOWN
Recipient = UNKNOWN
Resource State = UNKNOWN
Execution Outcome = UNKNOWN

Unknown may require:

* WAITING
* RE-EVALUATION
* HUMAN INTERVENTION
* BLOCKING
* RECONCILIATION

depending on the applicable semantics.

The architecture must not convert uncertainty into authority.

An unknown execution outcome is particularly significant.

Noema must not automatically interpret:

request timed out

as:

execution failed

when the external system may have performed the operation.

The system must support explicit reconciliation of unknown outcomes.

⸻

29. Human Intervention

Human intervention is an architectural control mechanism.

It may occur when:

* intent is ambiguous
* required evidence is unavailable
* approval is required
* authorization cannot be established
* risk exceeds permitted boundaries
* execution produces an unexpected result
* business rules require human judgment
* an outcome cannot be deterministically established

The architecture therefore supports:

System
  ↓
WAITING
  ↓
Human Input
  ↓
Re-Evaluation
  ↓
Continue / Block / Escalate

Human intervention should be represented explicitly rather than hidden inside conversational behavior.

A durable workflow may remain suspended while awaiting the required human decision.

⸻

30. Provenance

Every consequential architectural transition should be traceable.

Relevant provenance may include:

* Intent version
* Context references
* Evidence references
* Validation result
* Rule and policy versions
* Trust evaluation
* Authorization result
* selected Action
* Execution Contract
* workflow identifier
* execution consumer
* execution result
* outcome evidence
* timestamps
* retries
* human interventions
* material state transitions

The objective is reconstructibility.

Noema should be able to answer:

Why did this Intent reach this state?

and:

What happened after that decision?

without requiring access to hidden model reasoning.

⸻

31. Durable Workflow and Provenance

Workflow orchestration provides operational history, but workflow history should not be assumed to be the complete Noema provenance model.

Noema should retain canonical references to consequential decisions and state transitions.

Conceptually:

Workflow Runtime
       │
       ├── workflow execution history
       │
       ▼
Noema Provenance
       │
       ├── Intent
       ├── Validation
       ├── Trust
       ├── Contract
       ├── Execution
       └── Outcome
       │
       ▼
Authoritative Enterprise Evidence

This permits Noema to distinguish:

* how the workflow progressed
* why Noema made a consequential decision
* what the external system actually established

⸻

32. Temporal and Long-Running Intent Lifecycles

Some Intent lifecycles may extend beyond a single interaction.

For example:

User Request
     ↓
Intent Resolution
     ↓
Validation
     ↓
Trust
     ↓
Approval Required
     ↓
WAITING
     ↓
Approval Event
     ↓
Re-Evaluation
     ↓
Execution
     ↓
Outcome

The lifecycle may span:

* seconds
* minutes
* hours
* days
* potentially longer periods

The architecture therefore treats time as a first-class lifecycle dimension.

Durable workflow orchestration allows the Intent lifecycle to survive:

* process restarts
* service failures
* deployment changes
* temporary infrastructure failures
* long waiting periods

This does not change the semantic ownership of the lifecycle.

⸻

33. Architectural Invariants

The architecture is governed by the following invariants.

Invariant 1

Noema owns Intent state, not authoritative business state.

Invariant 2

Probabilistic model output does not constitute deterministic authority.

Invariant 3

Ambiguous Intent must not be silently guessed into certainty.

Invariant 4

Validation and Trust remain distinct.

Invariant 5

Capability and permission remain distinct.

Invariant 6

Trust must be evaluated through explicit conditions.

Invariant 7

READY does not imply execution success.

Invariant 8

Execution consumers remain authoritative for the business mutations they perform.

Invariant 9

Unknown mandatory conditions cannot produce execution readiness.

Invariant 10

Material changes may invalidate previous decisions.

Invariant 11

Execution must occur through explicit contracts.

Invariant 12

Execution outcomes must be represented separately from Trust decisions.

Invariant 13

Important state transitions must be observable and reconstructible.

Invariant 14

Human intervention is a valid architectural state.

Invariant 15

No component may silently acquire authority outside its defined boundary.

Invariant 16

Workflow orchestration must not become a substitute for business-state authority.

Invariant 17

Durable execution must preserve lifecycle state across process and infrastructure failure.

Invariant 18

Retries must respect Action and contract semantics.

Invariant 19

Unknown execution outcomes must not be converted into successful or failed outcomes without sufficient evidence.

Invariant 20

Workflow progression must not bypass Validation, Trust, or required contractual boundaries.

⸻

34. Architectural Mental Model

The architecture can be reduced to seven questions:

1. What does the Actor want?
           ↓
2. What does the Actor mean?
           ↓
3. What information establishes that meaning?
           ↓
4. Is the resulting Intent valid?
           ↓
5. May the Intent proceed?
           ↓
6. What explicit Action can satisfy it?
           ↓
7. What actually happened?

These correspond broadly to:

Intent
Resolution
Context
Validation
Trust
Execution
Outcome

Durable orchestration ensures that these transitions remain reliable across time.

Everything else exists to make those transitions reliable, bounded, and reconstructible.

⸻

35. Architectural Relationship to the Canon

The architecture implements the principles established by the Noema Canon.

The Canon establishes foundational boundaries.

Architecture establishes the components and relationships that realize those boundaries.

Specifications define precise behavior.

Implementations realize the specifications.

Therefore:

Canon
  ↓
Specification
  ↓
Architecture
  ↓
Implementation

Architecture must not silently redefine canonical principles.

If implementation requirements expose a contradiction in the architecture, the contradiction should be resolved explicitly through the appropriate specification or architectural decision process.

The selection of Temporal as a durable workflow substrate is an architectural implementation decision governed by the relevant ADR. It does not alter the semantic definition of Trust, Intent, Validation, Execution, or Outcome.

⸻

36. Architectural Extensibility

The architecture is intended to support additional:

* Intent types
* Actions
* capabilities
* enterprise systems
* policy systems
* authorization systems
* AI models
* execution consumers
* validation rules
* Trust predicates
* outcome mechanisms
* workflow types
* event sources

without changing the fundamental intent-to-action boundary.

New functionality should be introduced through explicit contracts and extensions to the relevant canonical abstractions.

It should not require collapsing previously distinct responsibilities.

⸻

37. Reference Architecture

The reference architecture is:

                    ┌─────────────────────┐
                    │       ACTOR         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   INTENT ENGINE     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   CONTEXT ENGINE    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     VALIDATION      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    TRUST ENGINE     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    ACTION GRAPH     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ EXECUTION PLANNER   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ EXECUTION CONTRACT  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ DURABLE WORKFLOW    │
                    │ ORCHESTRATION       │
                    │     (Temporal)      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ EXECUTION CONSUMER  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   OUTCOME ENGINE    │
                    └─────────────────────┘
       ┌──────────────────────────────────────────┐
       │         OPERATIONAL MEMORY              │
       │  State · Provenance · Records · Events  │
       └──────────────────────────────────────────┘
       ┌──────────────────────────────────────────┐
       │              AI LAYER                   │
       │ Interpretation · Retrieval · Proposals │
       └──────────────────────────────────────────┘

The AI Layer and Operational Memory are cross-cutting architectural capabilities rather than replacements for the core lifecycle components.

Durable workflow orchestration is an infrastructure capability supporting the lifecycle rather than a replacement for any semantic component.

⸻

38. Architectural Technology Boundary

The architecture deliberately distinguishes canonical semantics from implementation technology.

The following are architectural concepts:

* Intent
* Context
* Validation
* Trust
* Policy
* Capability
* Action
* Contract
* Execution
* Outcome
* Provenance
* Operational Memory

These concepts must remain stable even if their implementation technologies change.

Technology choices may include:

* AI model providers
* programming languages
* databases
* message brokers
* API protocols
* cloud infrastructure
* observability systems
* workflow runtimes

Such technologies implement architectural responsibilities; they do not redefine them.

Temporal is therefore an implementation of the durable workflow orchestration responsibility, not a canonical definition of what a Noema workflow means.

⸻

39. Final Definition

The Noema Architecture is the system structure that transforms human intent into validated, trusted, contract-governed, durably orchestrated execution and verified outcome while preserving explicit boundaries between probabilistic inference, deterministic control, execution authority, workflow coordination, and authoritative business state.

The central architectural principle is:

Noema does not give probabilistic systems the authority to become deterministic systems.
It uses probabilistic systems to understand intent and deterministic architecture to establish what may happen.

Durable execution adds a second critical principle:

Noema does not assume that an intent lifecycle completes within a single process or interaction.
Its consequential workflows must be able to wait, resume, retry, recover, and reconcile without losing the semantic boundaries or authority established by the architecture.

The resulting system is:

Human Intent
     ↓
Intent Understanding
     ↓
Context
     ↓
Validation
     ↓
Trust
     ↓
Action
     ↓
Contract
     ↓
Durable Orchestration
     ↓
Execution
     ↓
Outcome

with every consequential transition explicit, bounded, durable, observable, attributable, and re-evaluable.