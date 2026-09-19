# Noema Architecture Overview
Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/overview.md
⸻
## 1. Definition
The Noema Architecture defines the system boundaries, components, flows, and relationships through which human intent is transformed into trusted, contract-governed execution and verified outcome.
Noema is an intent infrastructure layer.
Its architectural responsibility is to provide the controlled path between:
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
It coordinates intent across those systems while maintaining explicit control over understanding, trust, authority, execution, and provenance.
⸻
## 2. Architectural Objective
The architecture exists to make the intent-to-action boundary explicit.
The system must be able to establish:
1. what the Actor intends
2. what context is required to understand that intent
3. whether the resulting Intent is valid
4. whether the Intent may proceed
5. what Action should satisfy the Intent
6. what capability can perform that Action
7. what contract governs execution
8. what execution occurred
9. what outcome resulted
10. what evidence and provenance support each transition
The architecture must preserve the distinction between these concerns.
⸻
## 3. Core Architectural Boundary
The fundamental Noema boundary is:
```text
                    NOEMA
┌───────────────────────────────────────────────┐
│                                               │
│  Human Expression                             │
│        ↓                                      │
│  Intent Engine                                │
│        ↓                                      │
│  Context Engine                               │
│        ↓                                      │
│  Validation                                   │
│        ↓                                      │
│  Trust                                         │
│        ↓                                      │
│  Action Graph / Planning                      │
│        ↓                                      │
│  Execution Contract                           │
│        ↓                                      │
│  Execution                                    │
│        ↓                                      │
│  Outcome                                      │
│                                               │
└───────────────────────────────────────────────┘
                    │
                    ▼
        Existing Enterprise Systems

Noema owns the intent-side lifecycle and the coordination necessary to safely cross the execution boundary.

External systems remain authoritative for the business state they own.

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
* Execution Record
* Outcome Engine
* Operational Memory
* AI Layer

These components are related but must not collapse into one undifferentiated agent.

Each component has a distinct architectural responsibility.

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

⸻

9. Trust State

Trust is represented as an explicit lifecycle.

The canonical Trust states are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Execution outcome may be represented separately as:

EXECUTING
COMPLETED
FAILED

The architectural distinction is important.

Trust establishes execution eligibility.

Execution establishes what actually happened.

Therefore:

READY ≠ COMPLETED

and:

TRUST ≠ OUTCOME

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

⸻

12. Execution Contract

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
Execution

Noema should execute contracts rather than arbitrary model-generated instructions.

⸻

13. Execution Record

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
* what outcome was observed

The Execution Record is part of Noema’s operational and audit boundary.

It is not necessarily the authoritative business record.

The target system remains authoritative for the business mutation it owns.

⸻

14. Outcome Engine

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

15. Operational Memory

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

⸻

16. AI Layer

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

⸻

17. End-to-End Architecture

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

⸻

18. The Intent-to-Outcome Pipeline

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

⸻

19. Separation of Concerns

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

Execution vs Outcome

Execution records what was attempted or performed.

Outcome establishes what actually resulted.

Intent State vs Business State

Intent state belongs to Noema.

Business state remains owned by the authoritative external system.

These distinctions are architectural invariants.

⸻

20. State Ownership

Noema owns state concerning the Intent lifecycle.

Examples include:

Intent State
Trust State
Validation State
Planning State
Execution State
Outcome Association
Provenance

External systems own their domain state.

Examples include:

Account State
Payment State
Customer State
Employee State
Card State
Inventory State

Noema may reference and act upon external state.

It should not silently redefine it.

⸻

21. External System Boundary

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

⸻

22. Authority Boundary

Authority flows through explicit mechanisms.

Actor
  ↓
Intent
  ↓
Authorization
  ↓
Trust
  ↓
Action Contract
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

⸻

23. Deterministic / Probabilistic Architecture

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

This boundary does not mean AI cannot participate in downstream processes.

It means AI output cannot silently become authoritative merely because it was generated by a model.

⸻

24. Re-Evaluation

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

⸻

25. Execution Boundary

READY does not mean execution has occurred.

The canonical transition is:

READY
  ↓
Execution Contract
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

The execution boundary is explicit.

⸻

26. Failure Architecture

Failure must remain typed and observable.

Potential failure classes include:

Intent Failure
Context Failure
Validation Failure
Trust Block
Authorization Failure
Capability Failure
Planning Failure
Contract Rejection
Execution Failure
Partial Execution
Outcome Failure
Unknown Outcome

The architecture must preserve these distinctions because recovery depends upon knowing where and why progression stopped.

⸻

27. Unknown State

Unknown information must not silently become a positive assertion.

Examples:

Authorization = UNKNOWN
Recipient = UNKNOWN
Resource State = UNKNOWN
Execution Outcome = UNKNOWN

Unknown may require:

WAITING
RE-EVALUATION
HUMAN INTERVENTION
BLOCKING

depending on the applicable semantics.

The architecture must not convert uncertainty into authority.

⸻

28. Human Intervention

Human intervention is an architectural control mechanism.

It may occur when:

* intent is ambiguous
* required evidence is unavailable
* approval is required
* authorization cannot be established
* risk exceeds permitted boundaries
* execution produces an unexpected result
* business rules require human judgment

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

⸻

29. Provenance

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
* execution consumer
* execution result
* outcome evidence
* timestamps
* human interventions

The objective is reconstructibility.

Noema should be able to answer:

Why did this Intent reach this state?

and:

What happened after that decision?

without requiring access to hidden model reasoning.

⸻

30. Architectural Invariants

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

⸻

31. Architectural Mental Model

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

Everything else exists to make those transitions reliable.

⸻

32. Architectural Relationship to the Canon

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

⸻

33. Architectural Extensibility

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

without changing the fundamental intent-to-action boundary.

New functionality should be introduced through explicit contracts and extensions to the relevant canonical abstractions.

It should not require collapsing previously distinct responsibilities.

⸻

34. Reference Architecture

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

⸻

35. Final Definition

The Noema Architecture is the system structure that transforms human intent into validated, trusted, contract-governed execution and verified outcome while preserving explicit boundaries between probabilistic inference, deterministic control, execution authority, and authoritative business state.

The central architectural principle is:

Noema does not give probabilistic systems
the authority to become deterministic systems.
It uses probabilistic systems to understand intent
and deterministic architecture to establish
what may happen.

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
Execution
     ↓
Outcome

with every consequential transition explicit, bounded, observable, and attributable.