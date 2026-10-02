> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Thesis

Status: Foundational
Version: 0.1
Domain: Thesis
Canonical Path: thesis/thesis.md

⸻

1. The Thesis

Intent should be a first-class computational object.

Software has historically required people to translate what they want into the language of software:

Person
  ↓
Form
  ↓
API parameters
  ↓
Workflow
  ↓
Action

Noema proposes a different model:

Source of Intent
  ↓
Canonical Intent
  ↓
Resolution
  ↓
Trust Decision
  ↓
Action
  ↓
Verified Outcome

The fundamental premise is that Intent, rather than the API call, workflow, prompt, or UI, is the correct semantic abstraction for representing what a source of intent wants a computer system to accomplish.

A source of intent may be a person, AI agent, system, or supported interface. The semantic model remains the same.

⸻

2. The Central Claim

Noema’s central claim is:

A general-purpose semantic execution layer can sit between sources of intent and existing enterprise software systems, transforming Intent into trustworthy, authorized, constrained, executable Actions whose Outcomes can be verified without requiring the source of intent to understand the implementation details of those systems.

This layer should not replace the systems that already perform business operations.

It should make those systems semantically executable through Intent while preserving their role as authoritative systems of record for business state.

⸻

3. The Missing Layer

The modern software stack contains powerful layers:

┌─────────────────────────────┐
│ Human / Agent Interfaces    │
├─────────────────────────────┤
│ AI / Language Models        │
├─────────────────────────────┤
│ Applications                │
├─────────────────────────────┤
│ APIs / Services             │
├─────────────────────────────┤
│ Databases / Infrastructure  │
└─────────────────────────────┘

What is missing is a general layer that answers:

What does the source of intent mean, what can satisfy that meaning, and under what conditions may it become an executable operation?

Noema occupies that semantic execution boundary:

┌─────────────────────────────┐
│ Source of Intent             │
├─────────────────────────────┤
│           NOEMA              │
│                             │
│ Intent                      │
│ Resolution                   │
│ Context                      │
│ State Reconciliation         │
│ Trust                       │
│ Policy                      │
│ Authority                   │
│ Constraints                 │
│ Action Graph                │
│ Planning                    │
│ Execution                   │
│ Verification / Recovery     │
│ Outcome                     │
│ Causal Audit / Memory       │
├─────────────────────────────┤
│ Existing Enterprise Systems │
└─────────────────────────────┘

⸻

4. Intent as a Computational Primitive

Traditional software primitives include:

* Data
* Event
* Request
* Command
* Function
* Transaction
* Resource

Noema treats another abstraction as fundamental:

Intent

An Intent represents a desired objective or outcome from the perspective of an Actor.

For example:

“Renew my company card.”

is not merely a string.

It can become a canonical Intent Object containing concepts such as:

Intent
├── Actor
├── Objective
├── Resource
├── Context
├── Constraints
└── Desired Outcome

The exact representation is typed and schema-validated.

Once admitted into the Trust path, the Intent Object is immutable. A change to the Intent creates a new version rather than silently mutating the admitted representation.

This makes Intent something software can reason about independently of the language, interface, transport, or Model used to produce it.

⸻

5. Intent Is Not a Prompt

A prompt is an instruction or input to a Model.

An Intent is a canonical semantic object representing desired behavior.

This distinction is fundamental.

Prompt:
“Renew my card and don't ask me unnecessary questions.”
Intent:
RenewCard
Actor:
CurrentUser
Resource:
Card#123
Desired Outcome:
Card renewed

The prompt is an interface and Model-input artifact.

The Intent is part of the canonical system model.

⸻

6. Intent Is Not an Action

Intent describes what should be accomplished.

Action describes what the system will execute.

For example:

Intent:
“Make sure my card is renewed before it expires.”
Possible Action:
RenewCard(Card#123)

Another execution path might satisfy the same Intent through:

ReplaceCard(Card#123)
or:
ScheduleRenewal(Card#123, expiration_date)

Therefore:

Intent
  ≠
Action

Intent determines the semantic objective.

The execution layer determines the appropriate Action or Action plan capable of satisfying that objective.

⸻

7. The Intent-to-Action Boundary

Noema’s fundamental responsibility is the boundary between:

Meaning

and:

Machine Execution

The canonical platform flow is:

             SOURCE OF INTENT
       Human / Agent / System / Interface
                     │
                     ▼
            Intent Compilation
                     │
                     ▼
          Hard Schema Validation
                     │
                     ▼
                 Context
                     │
                     ▼
            State Reconciliation
                     │
                     ▼
        Deterministic Trust Boundary
                     │
                     ▼
       Enterprise Action / Outcome Graph
                     │
                     ▼
                  Planning
                     │
                     ▼
                 Execution
                     │
                     ▼
          Verification / Recovery
                     │
                     ▼
                  Outcome
                     │
                     ▼
             Causal Audit / Memory

The critical architectural boundary is:

PROBABILISTIC
understand / interpret / propose / generate candidates
                     │
                     │ HARD BOUNDARY
                     ▼
DETERMINISTIC
validate / resolve / reconcile / govern /
plan / execute / verify / recover / audit

The Model proposes.

Noema decides.

⸻

8. Probabilistic at the Edge, Deterministic at the Boundary

Noema does not reject probabilistic AI.

It places probabilistic reasoning in the appropriate part of the system.

Models may assist with:

* language interpretation
* intent classification
* entity resolution
* semantic matching
* retrieval
* candidate generation
* planning

But consequential execution requires deterministic controls.

Therefore:

Probabilistic Model
        ↓
Candidate Interpretation
        ↓
Canonical Noema Representation
        ↓
Hard Schema Validation
        ↓
Deterministic Resolution / Reconciliation
        ↓
Deterministic Trust Decision
        ↓
Execution

Probabilistic output is untrusted input until it passes the canonical admission and validation boundary.

No Model output should directly authorize consequential execution.

⸻

9. Trust Is the Core Control Plane

The central purpose of Noema’s Trust Engine is not to determine whether the Model is intelligent.

It determines whether an Action is sufficiently justified to execute.

Conceptually:

Trust =
f(
  Intent,
  Actor,
  Target,
  Capability,
  Authority,
  Policy,
  Constraint,
  Context,
  State,
  Evidence
)

The canonical Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

Trust is therefore a decision boundary, not a Model confidence score.

Enterprise systems remain the sources of authority for their own business permissions, policies, and business state. Noema evaluates the resolved execution path against the applicable governance conditions rather than replacing enterprise authorization systems.

⸻

10. Model Confidence Is Not Trust

A Model may say:

“I am 98% confident the user means Card #123.”

That does not establish:

Card #123
=
Intended Resource

Likewise:

Model confidence = 0.98

does not establish:

Actor authority = valid
Policy = satisfied
Constraint = satisfied
Current State = compatible
Action = safe

Therefore:

Model Confidence
       ≠
Noema Trust

This distinction is fundamental to the architecture.

⸻

11. Uncertainty Must Become a System State

Noema must represent uncertainty explicitly rather than forcing unresolved information into false certainty.

At the fact level, information may have statuses such as:

KNOWN
INFERRED
AMBIGUOUS
UNAVAILABLE
STALE
CONTRADICTORY
UNKNOWN
UNAUTHORIZED

At the execution level, an Action may reach an uncertain state where the system cannot yet establish whether the external operation occurred.

The unacceptable transition is:

UNKNOWN
   ↓
GUESS
   ↓
EXECUTE

Unknown execution state requires verification or reconciliation before a retry or subsequent consequential Action is considered.

⸻

12. Clarification Is Part of Execution

Traditional systems often treat clarification as a failure of the interface.

Noema treats clarification as a valid governed outcome.

For example:

“Transfer money to my savings account.”

If the Actor has three savings accounts, Noema should not select one arbitrarily.

It should produce:

CLARIFY

and ask which account is intended.

The system has not failed.

It has correctly determined that the required execution path cannot yet be established deterministically.

⸻

13. Authorization Is Necessary but Insufficient

A conventional authorization system asks:

Can Actor X perform Action Y?

Noema must additionally establish:

Is Action Y actually consistent with the resolved Intent?

Trustworthy execution therefore requires the relationship between:

Intent correctness
+
Actor / target resolution
+
Authority correctness
+
Policy correctness
+
State correctness
+
Constraint correctness

Authorization is one component of Trust, not its definition.

Noema must distinguish at least:

* Technical authorization: whether the connected system permits the operation.
* Policy authorization: whether applicable governance rules permit the operation.
* Business authorization: whether the enterprise’s business rules establish that the Actor may cause the requested operation.

These may depend on different authoritative sources.

⸻

14. The Canonical Ontology Is the Semantic Foundation

Noema requires a small, stable ontology for expressing executable Intent.

The foundational vocabulary includes:

Actor
Intent
Entity
Resource
Capability
Action
Execution
Outcome
State
Context
Constraint
Policy
Authority
Evidence
Relationship

These concepts provide the semantic vocabulary through which domains can describe and govern executable operations.

The ontology should remain:

* small
* explicit
* composable
* domain-agnostic
* machine-readable
* stable across implementation technologies

⸻

15. Domain Semantics Extend the Ontology

Noema does not need to encode every concept in every industry into its universal core.

Instead:

Universal Noema Primitives
             +
      Domain Semantics
             ↓
      Executable Intent

For example, a payments domain may define:

Payment
Refund
Settlement
Merchant
Cardholder

while a deployment domain may define:

Deployment
Environment
Release
Rollback
Service

Both domains can use the same foundational semantics:

Actor
Intent
Resource
Capability
Policy
Constraint
Action
Outcome

Domain intelligence belongs in domain configuration, enterprise-specific graph data, and adapters rather than being hard-coded into the universal execution engine.

⸻

16. Noema Does Not Own Business State

Noema operates across enterprise systems without becoming the authoritative owner of their business domains.

For example:

CRM
  → Customer state
Payment system
  → Payment state
ERP
  → Order state
HRIS
  → Employee state

Noema maintains the semantic and execution state necessary to reason about and govern execution, including:

Intent State
Trust State
Execution State
Outcome State
Evidence / Provenance
Operational History

Noema does not become another ERP, CRM, or universal business database.

Where multiple enterprise systems contribute observations, Noema performs state reconciliation for the purpose of determining the execution-relevant state without replacing the authoritative business system.

⸻

17. Noema Is a Semantic Execution Layer

Noema should be understood as a Trusted Enterprise Execution Infrastructure layer rather than as:

* an AI assistant
* an agent framework
* an RPA system
* a workflow engine
* an API gateway
* a policy engine
* a knowledge graph product
* a chatbot

Those technologies may participate in a Noema deployment.

None defines the thesis.

The thesis is:

Intent
  ↓
Meaning
  ↓
Trust
  ↓
Action
  ↓
Verified Outcome

⸻

18. Existing Systems Become Capabilities

Noema does not require the world to be rebuilt.

Existing enterprise software already contains enormous execution capability.

Noema’s job is to make that capability semantically addressable and governable.

Conceptually:

Existing System
      │
      ▼
   Adapter
      │
      ▼
Canonical Capability
      │
      ▼
    Noema
      ▲
      │
    Intent

For example:

Payment Provider
  → refund_payment
CRM
  → update_customer
Cloud Platform
  → deploy_service
Source Control
  → merge_pull_request

Noema reasons about canonical Capabilities rather than exposing arbitrary raw APIs directly to a Model.

A Capability describes what can be done.

It does not by itself establish that an Action is authorized or appropriate.

⸻

19. Integrations Should Be Adapters

External systems should map into Noema’s canonical semantic model.

External System
      │
      ▼
    Adapter
      │
      ▼
Canonical Capability
      │
      ▼
    Noema

Adapters translate between Noema’s canonical execution semantics and provider-specific protocols, identifiers, authentication mechanisms, errors, and operational behavior.

They are execution boundaries, not decision-makers.

This allows the underlying integration to change without changing the meaning of the Intent.

⸻

20. Action Is the Execution Contract

Once Noema determines that an Intent can safely proceed, the resulting Action should be explicit and contract-bound.

Conceptually:

Action
├── Actor
├── Capability
├── Target / Resource
├── Parameters
├── Preconditions
├── Constraints
├── Authority Context
└── Expected Outcome

The Action is not free-form Model output.

It is a typed representation that must satisfy the applicable Action Contract and Capability constraints.

The external system should not receive an ambiguous natural-language instruction.

It should receive an explicitly resolved and governed Action.

⸻

21. Planning Does Not Create Authority

Some Intents require multiple Actions or alternative execution paths.

A Planner may therefore determine a suitable sequence or composition of Actions.

However:

Planning
  ≠
Authority

The Planner cannot:

* create a Capability
* create permission
* override Policy
* bypass Trust
* bypass Action Contracts
* invent enterprise state
* convert uncertainty into authorization

Planning operates within the capabilities, policies, constraints, authority, and execution semantics already established by Noema.

⸻

22. Outcome Completes the Loop

Execution is not the end of the lifecycle.

Noema must determine whether the Action produced the expected Outcome.

Intent
  ↓
Action
  ↓
Execution Attempt
  ↓
Observed Evidence
  ↓
Verified Outcome
  ↓
State Reconciliation
  ↓
Intent Satisfaction

An external acknowledgement is evidence about execution, not automatically proof of business completion.

Verification is therefore part of the execution lifecycle.

⸻

23. Execution Requires Idempotency and Recovery

A consequential Action may be attempted more than once because of retries, timeouts, process failures, or infrastructure failures.

Noema must distinguish:

Action
Execution
Execution Attempt
Idempotency Key

These are related but distinct concepts.

If execution state is unknown, Noema should verify or reconcile the external state before retrying whenever the operation could produce a duplicate side effect.

Partial failure, compensation, reconciliation, and recovery must be explicit rather than assumed to behave like a distributed ACID transaction.

⸻

24. The Closed-Loop Model

The complete Noema model is therefore:

┌────────────────────┐
│ Source of Intent   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Canonical Intent   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Resolution         │
│ + Context          │
│ + State Reconcile  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Deterministic      │
│ Trust              │
│                    │
│ Authority          │
│ Policy             │
│ Constraints        │
│ Capability         │
│ Evidence           │
└─────────┬──────────┘
          │
     ┌────┴────┐
     ▼         ▼
 EXECUTE   CLARIFY /
           ESCALATE /
           REJECT
     │
     ▼
┌────────────────────┐
│ Action / Plan      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Execution          │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Verification /     │
│ Recovery           │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Verified Outcome   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Causal Audit /     │
│ Operational Memory │
└────────────────────┘

This is the core Noema execution model.

⸻

25. Safety Is Structural

Trustworthy execution cannot depend solely on Model behavior or Model confidence.

Noema must structurally constrain what can reach execution.

Therefore:

* Model output is untrusted.
* User-provided input is untrusted.
* Retrieved enterprise text is untrusted.
* Tool responses are untrusted until evaluated according to their authority and provenance.
* The Model has no direct enterprise credentials.
* Free-form Model output cannot directly invoke arbitrary enterprise operations.
* Capabilities must be explicitly registered and bounded.
* Arbitrary HTTP, SQL, or equivalent operations are not capabilities merely because a Model can describe them.
* Explicitly prohibited capabilities must be unavailable or hard-denied.
* Executors must revalidate relevant execution conditions at the execution boundary.

Safety therefore comes from architecture and enforceable contracts, not from asking a Model to behave correctly.

⸻

26. Auditability Is Causal Traceability

Noema must be able to reconstruct why a consequential Action occurred.

A causal audit should establish, as applicable:

Who initiated
      ↓
What they intended
      ↓
What was ambiguous
      ↓
How it was resolved
      ↓
What authority applied
      ↓
What Policy applied
      ↓
What enterprise State was observed
      ↓
What Evidence supported the decision
      ↓
What Action was selected
      ↓
What was attempted
      ↓
What downstream result occurred
      ↓
What final State was verified

Auditability does not require exposing private Model chain-of-thought.

The requirement is reproducible causal traceability of the governed execution decision.

⸻

27. Operational Memory Is Part of the System

Noema requires structured operational history describing cases, executions, failures, interventions, evidence, outcomes, and recovery.

This is Operational Memory.

It is not equivalent to:

* a generic Model memory
* a vector database
* a conversation history
* a retrieval index

Operational Memory exists to preserve the history required to understand, operate, audit, and improve consequential execution.

⸻

28. The Generality Thesis

Noema’s long-term thesis is not tied to one workflow.

The same primitives should be capable of expressing:

“Renew my card.”
“Give Sarah the same access John has.”
“Refund the duplicate payment.”
“Deploy the latest release to staging.”
“Book the earliest available flight.”
“Close the inactive account.”
“Move the remaining budget to Project B.”

The domain changes.

The underlying semantic structure remains:

Intent
→ Context
→ Capability
→ Authority
→ Policy
→ Action
→ Execution
→ Outcome

⸻

29. The Commercial Wedge

The broad thesis does not imply that Noema must begin broadly.

The first implementation should target a consequential workflow where the semantic gap, fragmented enterprise state, and execution risk are sufficiently significant to demonstrate the value of the system.

The initial proof should demonstrate:

Source of Intent
      ↓
Ambiguous / multi-step request
      ↓
Canonical Intent
      ↓
Resolution
      ↓
Trust Evaluation
      ↓
Multiple enterprise capabilities
      ↓
Execution
      ↓
Verified Outcome

The initial use case proves the primitive.

It does not define the entire company category.

⸻

30. The Smallest Proof

The smallest convincing proof of Noema is not:

“An AI can call an API.”

That is already commonplace.

The smallest proof is:

A source of intent can express a meaningful operational objective without knowing the underlying system APIs, and Noema can deterministically resolve that objective into a governed Action, execute it through existing enterprise capabilities, and verify the resulting Outcome.

When that transition cannot be safely established, Noema must clarify, escalate, or reject rather than guess.

⸻

31. The Architectural Consequence

If the thesis is correct, Noema’s architecture should be organized around semantic and execution primitives rather than integrations.

The center of the system should be:

Intent

around which the system resolves:

Actor
Context
Entity
Resource
Capability
Policy
Constraint
Authority
State
Evidence

and produces:

Action
Execution
Outcome

Integrations sit at the edge.

The ontology and trust semantics sit at the center.

The enterprise remains authoritative for business state.

⸻

32. The Economic Consequence

If Noema works, organizations do not need to redesign every existing application around AI.

Instead, they can expose existing business capabilities through a common semantic execution boundary.

Conceptually:

             Noema
          ↙    ↓    ↘
        CRM   ERP   Payments

with Intent providing the common semantic entry point.

The value is therefore not merely automation.

It is reducing the semantic and governance cost of connecting sources of intent to heterogeneous enterprise execution systems while preserving enterprise systems as the authoritative owners of business state.

⸻

33. The Embedded Product Model

Noema is intended to operate as an embedded enterprise product, not merely as an internal enterprise-operations tool.

An enterprise integrates Noema into its own product or service so that its users or customers can express intent and receive governed outcomes across the enterprise’s existing systems.

This creates two supported operating modes:

Mode 1: Full-Stack Noema
Source of Intent
      ↓
Noema
      ↓
Enterprise Systems

and:

Mode 2: Independent Trust Boundary
Source of Intent
      ↓
Enterprise Agent / Orchestrator
      ↓
Noema Trust + Execution Boundary
      ↓
Enterprise Systems

Mode 2 allows an enterprise to retain its existing interaction or orchestration layer while using Noema as an independent boundary before consequential execution.

The underlying semantic and trust model remains the same.

⸻

34. The Boundary of the Thesis

Noema does not claim that every request can or should become autonomous execution.

It claims that Intent can be represented explicitly enough to make the transition from source expression to software execution a principled, inspectable, and deterministic process.

When the system cannot establish that transition safely, the correct behavior is:

CLARIFY
ESCALATE
REJECT

or, where required by the execution lifecycle, wait for evidence, approval, or reconciliation.

The incorrect behavior is:

GUESS

⸻

35. Final Thesis Statement

Noema is Trusted Enterprise Execution Infrastructure in which Intent becomes a first-class computational object, probabilistic AI is used to interpret and propose candidate meanings, canonical semantics resolve those meanings, deterministic Trust mechanisms determine whether they may become Actions, enterprise systems provide the underlying execution capabilities and remain authoritative for business state, and verified Outcomes close the loop back to the original Intent.

In its shortest form:

Source of Intent
      ↓
Canonical Intent
      ↓
Resolution
      ↓
Deterministic Trust
      ↓
Executable Action
      ↓
Verified Outcome

Noema’s thesis is that this Intent-to-Action boundary should become a fundamental layer of enterprise software.