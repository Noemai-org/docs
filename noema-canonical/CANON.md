Noema Canon

Status: Foundational
Version: 0.1
Purpose: Define the principles, boundaries, terminology, and invariants that constitute Noema.

⸻

1. Purpose

Noema is an intent infrastructure layer for turning human intent into trusted, executable actions across existing software systems.

Noema exists between human intent and enterprise execution.

Its fundamental responsibility is not to replace enterprise systems, databases, or business applications. Its responsibility is to understand what a person intends to accomplish, establish whether that intent is sufficiently understood and authorized to act upon, and coordinate execution through explicit contracts and existing systems.

Noema therefore separates:

* understanding from trust
* intent state from business state
* probabilistic inference from deterministic authorization
* planning from execution
* capability from permission
* execution from ownership of business truth

⸻

2. The Core Thesis

Human intent should be expressible as a structured, verifiable, and executable object rather than remaining trapped inside an application-specific interface.

Traditional software requires humans to translate their goals into the vocabulary and interaction model of each application.

Noema reverses this relationship.

The human expresses what they want.

Noema resolves that intent into a canonical representation, gathers the context required to understand it, evaluates whether it can be trusted, and maps it onto executable capabilities exposed by the systems that can fulfill it.

The application remains responsible for its domain.

Noema becomes responsible for the intent-to-action boundary.

⸻

3. What Noema Owns

Noema owns intent state.

This includes, but is not limited to:

* the representation of expressed intent
* interpretation and resolution of intent
* ambiguity
* clarification state
* contextualization of intent
* constraints attached to intent
* intent confidence
* trust state
* action selection
* execution state
* provenance of decisions made by Noema
* the relationship between intent and executable actions

Noema does not own the authoritative business state of the systems it operates against.

For example, if a banking system is authoritative for a customer’s card status, Noema does not become the source of truth for that card.

Noema may observe, reason about, and act upon that state through defined interfaces.

Noema owns intent state, not business state.

This is a foundational architectural boundary.

⸻

4. The Noema Boundary

Noema sits between human intent and existing systems.

Human
  │
  │ expresses
  ▼
Intent
  │
  │ resolve
  ▼
Contextualized Intent
  │
  │ evaluate
  ▼
Trusted Intent
  │
  │ map
  ▼
Executable Action
  │
  │ execute
  ▼
Enterprise System
  │
  │ produces
  ▼
Business Outcome

Noema does not need to own the systems on either side of this boundary.

Its value comes from making the boundary between what a human means and what a system is permitted to do explicit, reliable, and executable.

⸻

5. The Probabilistic / Deterministic Boundary

AI models are inherently probabilistic.

Noema may use probabilistic models to:

* interpret natural language
* identify candidate intents
* extract entities
* infer relationships
* retrieve relevant context
* propose actions
* generate clarifying questions
* construct candidate execution plans

However:

Probabilistic inference must not be silently converted into deterministic authority.

The Trust Engine is the boundary between probabilistic understanding and executable action.

The model may propose.

Noema must establish.

The model may infer.

Noema must verify.

The model may be uncertain.

Noema must be able to stop.

⸻

6. Noema Must Not Guess

When Noema lacks sufficient information to establish what the user intends, it must not manufacture certainty.

Insufficient certainty must produce an explicit state.

That state is clarification.

                    ┌──────────────┐
                    │ User Intent  │
                    └──────┬───────┘
                           │
                           ▼
                    Intent Resolution
                           │
                  ┌────────┴────────┐
                  │                 │
             Sufficient         Insufficient
              certainty           certainty
                  │                 │
                  ▼                 ▼
               Trust           Clarification
                  │                 │
                  ▼                 │
             Execution ◄────────────┘

Clarification is not an error condition.

It is a valid and intentional Noema state.

When Noema cannot establish intent with sufficient certainty, the correct action is to ask—not to guess.

⸻

7. Intent Is a First-Class Object

An intent is not merely a string extracted from a conversation.

A Noema intent must eventually be representable as structured state.

Conceptually:

Intent
├── actor
├── objective
├── subject
├── context
├── constraints
├── desired outcome
├── required capabilities
├── confidence
├── provenance
└── state

The exact schema is defined elsewhere in the canonical ontology and intent specifications.

The important canonical principle is:

Human language is an input to intent resolution; it is not itself the executable representation of intent.

⸻

8. Intent Must Be Contextual

Intent cannot always be understood from the user’s words alone.

Noema may need:

* user identity
* organizational context
* permissions
* current business state
* previous interactions
* system state
* policies
* available capabilities
* temporal information
* relevant external evidence

Context must therefore be treated as a first-class part of intent resolution.

However, context must not be treated as unlimited permission to infer.

Context may resolve ambiguity, but context must not manufacture authority.

⸻

9. Trust Is Deterministic

Noema’s Trust Engine must be deterministic with respect to the same:

* intent
* context
* evidence
* policies
* capabilities
* authorization state
* constraints

Given the same inputs and policy version, trust evaluation should produce the same result.

The model may change its interpretation.

The Trust Engine must not arbitrarily change its decision because a model happened to produce a different probability distribution.

Trust therefore requires explicit evidence and rules.

A conceptual trust evaluation may consider:

Intent validity
        +
Context sufficiency
        +
Evidence validity
        +
Policy compliance
        +
Authorization
        +
Capability availability
        +
Constraint satisfaction
        +
Risk boundary
        ↓
Trust Decision

⸻

10. Trust Is Not the Same as Confidence

Model confidence and Noema trust are different concepts.

Confidence describes how strongly a probabilistic model believes an interpretation.

Trust describes whether Noema has sufficient deterministic grounds to permit the resulting action.

A model can have high confidence and Noema can still reject the action.

A model can have moderate confidence and Noema may request additional information before deciding.

Therefore:

Model confidence is evidence for reasoning; it is not authority for execution.

⸻

11. Actions Must Be Explicit

Noema must not treat arbitrary model-generated instructions as executable actions.

Execution must occur through defined capabilities and action contracts.

An executable action should establish, where applicable:

* action identity
* target
* inputs
* required capability
* authorization requirements
* preconditions
* constraints
* expected side effects
* postconditions
* failure semantics
* idempotency semantics
* audit requirements

Conceptually:

Trusted Intent
      │
      ▼
Action Selection
      │
      ▼
Action Contract
      │
      ├── Preconditions
      ├── Authorization
      ├── Constraints
      └── Capability
      │
      ▼
Execution
      │
      ▼
Postcondition Verification

Noema executes contracts, not model output.

⸻

12. Capability Is Not Permission

A system may expose an operation without Noema being permitted to invoke it for a particular actor or circumstance.

Therefore:

* Capability answers: “Can this system perform this action?”
* Permission answers: “Is this actor allowed to cause this action?”
* Trust answers: “Has Noema established sufficient grounds to permit this intent to become this action?”

These concepts must remain distinct.

⸻

13. Noema Does Not Own Business Truth

Enterprise systems remain authoritative for their respective domains.

Examples include:

* a payment processor owning payment state
* an identity provider owning identity state
* a CRM owning customer records
* an HR system owning employee records
* a banking system owning account state

Noema may coordinate across these systems, but it must not silently create a competing source of truth.

When Noema needs information, it should obtain that information through explicit interfaces and retain appropriate provenance.

When Noema changes business state, the authoritative system remains the system of record.

⸻

14. Every Action Has a Boundary

Noema must know what it is allowed to do.

Autonomy therefore exists within explicit boundaries.

Those boundaries may include:

* actor permissions
* organizational policies
* action contracts
* financial limits
* data-access boundaries
* risk thresholds
* approval requirements
* system capabilities
* temporal constraints
* human-in-the-loop requirements

Autonomy is bounded by contract, policy, capability, and authority.

Noema should never interpret “be autonomous” as permission to invent its own authority.

⸻

15. Human Intervention Is a First-Class State

Noema must be capable of stopping execution and requesting human intervention.

Human intervention is appropriate when:

* intent remains ambiguous
* required evidence is unavailable
* policy requires approval
* authorization cannot be established
* risk exceeds the configured boundary
* an action contract cannot guarantee the expected outcome
* execution produces an unexpected state
* business rules require human judgment

Human intervention is not necessarily failure.

It is one of the legitimate outcomes of bounded autonomy.

⸻

16. Execution Must Be Observable

Noema must be able to explain:

* what intent it resolved
* what context it used
* what evidence informed the decision
* what trust decision was made
* what action was selected
* which contract authorized execution
* which system was called
* what happened during execution
* what outcome was observed
* whether human intervention occurred

This does not imply exposing chain-of-thought or private model reasoning.

It means maintaining decision provenance and execution auditability.

Noema must be able to account for what it did without requiring access to hidden model reasoning.

⸻

17. Failure Is Part of the Model

Noema must treat failure as a first-class part of intent execution.

Failures may occur during:

* intent resolution
* context acquisition
* trust evaluation
* capability discovery
* authorization
* planning
* execution
* postcondition verification

Noema must distinguish between:

* failed understanding
* insufficient information
* denied authority
* unavailable capability
* rejected policy
* execution failure
* partial execution
* unknown outcome

A system that merely returns “failed” loses information necessary for safe recovery.

⸻

18. Noema Must Prefer Explicit State Over Implicit Behavior

Important system conditions must be represented as state rather than inferred from side effects or application behavior.

Examples include:

UNRESOLVED
CLARIFICATION_REQUIRED
RESOLVED
TRUST_PENDING
TRUSTED
REJECTED
READY
EXECUTING
SUCCEEDED
FAILED
PARTIALLY_COMPLETED
HUMAN_INTERVENTION_REQUIRED

The exact state machine is defined by the relevant canonical specifications.

The principle is:

If a condition materially affects what Noema may do next, that condition should be representable as explicit state.

⸻

19. Noema Is Not a Chatbot

A conversational interface may be one way humans interact with Noema.

It is not the definition of Noema.

Noema is concerned with:

intent → trust → action → outcome

rather than:

prompt → response

The interface may eventually be:

* chat
* voice
* API
* embedded UI
* workflow
* agent
* application
* automation

The canonical abstraction must remain independent of the presentation layer.

⸻

20. Noema Is Not an ERP, CRM, Database, or System of Record

Noema should not reproduce the functionality of every system it integrates with.

Its purpose is not to become another enterprise application.

Instead, Noema should make existing capabilities intent-addressable.

The enterprise owns domain capabilities.

Noema provides the layer that determines how human intent can safely invoke those capabilities.

⸻

21. Noema Is Not an Autonomous Agent Without Boundaries

Noema may use agents internally.

It may employ planning, reasoning, retrieval, tool use, and other agentic mechanisms.

But “agentic” does not define the authority model.

The canonical authority model remains:

Intent
  ↓
Understanding
  ↓
Trust
  ↓
Contract
  ↓
Execution

Agents operate inside these boundaries.

They do not define the boundaries.

⸻

22. Canonical Knowledge Has Authority

Not all information in the Noema repository is equally authoritative.

The repository distinguishes between:

Canon

Defines what Noema currently believes to be foundationally true.

Specification

Defines precise behavior, schemas, contracts, and semantics derived from the Canon.

Architecture

Defines how the current implementation realizes those specifications.

Decision Records

Explain why important decisions were made.

Research

Contains hypotheses, experiments, external findings, and ideas that may influence future decisions.

Reference Workflows

Demonstrate the canonical concepts in real-world scenarios.

Strategy

Defines commercial and organizational direction.

These categories must not be conflated.

⸻

23. The Canon Can Change, but Not Casually

The Canon is authoritative, but it is not immutable.

A foundational principle may change when:

* evidence invalidates it
* implementation reveals a fundamental contradiction
* a new requirement exposes a missing abstraction
* the commercial or technical model changes materially

Changes to the Canon must be deliberate.

A canonical change should normally include:

1. the principle being changed
2. the reason for the change
3. evidence supporting the change
4. affected specifications
5. affected contracts
6. affected implementations
7. migration implications
8. an ADR documenting the decision

The Canon should never silently drift.

⸻

24. Canonical Language Must Be Precise

Noema’s terminology is part of its architecture.

Words such as:

* intent
* context
* state
* trust
* confidence
* capability
* permission
* action
* execution
* outcome
* evidence
* policy
* constraint

must have precise definitions.

If two concepts are materially different, Noema must not use one term interchangeably with the other merely because they sound similar.

The canonical glossary is therefore normative.

⸻

25. The First Workflow Is a Proof, Not the Product

Noema’s first commercial workflow may focus on a narrow enterprise problem such as card renewal.

That workflow exists to prove the underlying system.

The workflow must therefore demonstrate that Noema can:

1. understand a real human objective
2. acquire the context necessary to resolve it
3. distinguish certainty from ambiguity
4. ask for clarification when necessary
5. deterministically evaluate trust
6. select an authorized capability
7. execute through a typed contract
8. interact with existing systems
9. verify the resulting outcome
10. maintain an auditable intent lifecycle

The workflow should constrain Noema enough to make the system measurable without defining the limits of the platform.

⸻

26. The Fundamental Noema Loop

The canonical lifecycle is:

EXPRESS
   ↓
RESOLVE
   ↓
CONTEXTUALIZE
   ↓
VALIDATE
   ↓
TRUST
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

At any point where Noema cannot safely proceed, the lifecycle may transition to:

CLARIFY
REJECT
ESCALATE

The system should never skip a required state merely to produce an apparently successful outcome.

⸻

27. The Core Invariants

The following are foundational Noema invariants.

Invariant 1 — Noema owns intent state, not business state.

Invariant 2 — Model confidence is not execution authority.

Invariant 3 — Noema must not guess when intent is materially ambiguous.

Invariant 4 — Trust evaluation must be deterministic.

Invariant 5 — Execution must occur through explicit capabilities and contracts.

Invariant 6 — Capability and permission are distinct.

Invariant 7 — Enterprise systems remain authoritative for their business domains.

Invariant 8 — Autonomy is bounded by explicit authority and policy.

Invariant 9 — Human intervention is a valid system state.

Invariant 10 — Material decisions must have provenance.

Invariant 11 — Important execution conditions must be represented as explicit state.

Invariant 12 — The conversational interface is not the Noema abstraction.

Invariant 13 — Noema must fail closed when it cannot establish sufficient grounds for execution.

Invariant 14 — Research may challenge the Canon but does not become Canon automatically.

Invariant 15 — Canonical concepts must have precise, stable definitions.

⸻

28. The Ultimate Abstraction

The simplest expression of Noema is:

Human Intent
     ↓
Meaning
     ↓
Trust
     ↓
Action
     ↓
Outcome

Everything else in Noema exists to make those transitions reliable.

The long-term objective is not merely to make AI better at understanding language.

It is to create a standard infrastructure for expressing, validating, and executing human intent across software systems without surrendering control, authority, or determinism to probabilistic models.

⸻

29. Canonical Test

Whenever a proposed feature, architecture decision, abstraction, or integration is introduced, the following questions should be answerable:

1. What intent does this represent?
2. What state does Noema own?
3. What business state remains owned by another system?
4. What evidence establishes the intent?
5. What makes the intent sufficiently understood?
6. What makes the intent trusted?
7. What authority permits the action?
8. What capability performs the action?
9. What contract governs execution?
10. What happens if the system is uncertain?
11. What happens if execution fails?
12. How is the outcome verified?
13. What provenance is retained?
14. What happens when a human must intervene?
15. Does this strengthen or violate the canonical boundaries of Noema?

If these questions cannot be answered, the proposal is not yet sufficiently defined to become part of the Noema system.

⸻

30. The Canon in One Sentence

Noema is the deterministic intent-to-action boundary that allows probabilistically understood human intent to become safely executable across existing systems through explicit context, trust, authority, capability, and action contracts.