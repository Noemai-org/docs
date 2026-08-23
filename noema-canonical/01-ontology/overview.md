Absolutely. overview.md should be the map of the ontology, not another deep definition of each concept. It should tell someone entering the repository what Noema’s canonical semantic model is, how the concepts relate, and where to look next.

Overview

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/overview.md

⸻

1. Purpose

The Noema Ontology defines the canonical concepts and relationships required to represent human intent as something that can be interpreted, validated, trusted, executed, and evaluated.

It establishes a shared vocabulary between:

* humans
* AI models
* Noema
* enterprise systems
* applications
* tools
* agents

The ontology exists to prevent critical semantic concepts from being conflated.

In particular:

Intent ≠ Action
Action ≠ Capability
Capability ≠ Authority
Authority ≠ Trust
Execution ≠ Outcome
Outcome ≠ Intent Satisfaction

These distinctions are foundational to Noema.

⸻

2. The Core Problem

Traditional AI application architectures often collapse the following sequence into one step:

User
  ↓
LLM
  ↓
Tool Call

This creates a dangerous semantic gap.

The system may understand:

“I want to cancel my subscription.”

and immediately produce:

cancel_subscription()

without formally establishing:

* which subscription
* which Actor
* whether the Actor has Authority
* whether the Intent is sufficiently resolved
* whether the Capability is appropriate
* whether Constraints apply
* whether execution is permitted
* whether the resulting Outcome actually satisfied the Intent

Noema introduces explicit semantic boundaries between these stages.

⸻

3. The Noema Semantic Model

The canonical model is:

Actor
   │
   │ expresses
   ▼
Intent
   │
   ├──────────────► Entity
   │
   ├──────────────► Context
   │
   ├──────────────► Constraint
   │
   └──────────────► Concepts
          │
          ▼
      Resolution
          │
          ▼
       Validation
          │
          ▼
        Trust
          │
          ▼
        Action
          │
          ▼
      Capability
          │
          ▼
      Execution
          │
          ▼
       Outcome
          │
          ▼
      Evidence
          │
          ▼
 Intent Satisfaction

This is the fundamental semantic flow through Noema.

⸻

4. Ontology Layers

The ontology can be understood as several conceptual layers.

┌─────────────────────────────────────┐
│             EXPRESSION              │
│ Human / Agent expression of intent  │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│              SEMANTICS              │
│ Actor · Intent · Entity · Context   │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│             GOVERNANCE              │
│ Constraint · Policy · Authority     │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│               TRUST                 │
│ Deterministic execution decision    │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│              EXECUTION              │
│ Action · Capability · Execution     │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│               RESULT                │
│ Outcome · Evidence · State         │
└─────────────────────────────────────┘

The layers are conceptual rather than necessarily physical software modules.

⸻

5. Foundational Concepts

The ontology contains a set of foundational concepts that should be treated as canonical.

Actor
Intent
Action
Capability
Entity
Context
Constraint
Concept
Outcome

Other concepts may build upon these.

⸻

6. Actor

An Actor is the entity that expresses or initiates an Intent.

An Actor may be:

Human
Organization
Service
Agent
System
Process

The Actor answers:

Who wants this?

See:

actor.md

⸻

7. Intent

An Intent represents the desired objective of an Actor.

It answers:

What does the Actor want to accomplish?

Example:

Actor:
Customer
Intent:
Renew Card
Target:
card_1234

Intent is the central semantic object in Noema.

See:

intent.md

⸻

8. Action

An Action is an operation that may be performed to fulfill an Intent.

Example:

Intent:
Renew Card
Action:
RenewCard(card_1234)

An Action is therefore downstream from Intent.

See:

action.md

⸻

9. Capability

A Capability describes an ability available to a system, service, tool, or Actor.

Example:

Capability:
card.renew

A Capability answers:

What can this system do?

It does not answer:

What should it do?

See:

capability.md

⸻

10. Entity

An Entity is a distinct object or subject that can be referenced, identified, observed, modified, or acted upon.

Examples:

Customer
Card
Account
Transaction
Subscription
Employee
Organization

Entities provide the targets and subjects of Intent and Action.

See:

entities.md

⸻

11. Context

Context represents information relevant to interpreting or evaluating an Intent.

Examples:

Conversation history
Current application state
Previous Actions
Actor's current session
Relevant Entities
Temporal information
Environmental information

Context answers:

What surrounding information is necessary to understand this Intent?

See:

context.md

⸻

12. Constraint

A Constraint limits the conditions under which an Intent may be fulfilled.

Examples:

amount <= $5,000
only during business hours
requires approval
direct flights only
must use existing account

Constraints answer:

What limits apply?

See:

constraint.md

⸻

13. Concept

A Concept is an abstract semantic category used to describe the domain.

Examples:

Payment
Subscription
Renewal
Approval
Transfer
Customer
Account

Concepts provide the semantic vocabulary from which more concrete Entities, Intents, Actions, and Capabilities can be defined.

See:

concepts.md

⸻

14. Outcome

An Outcome represents what actually happened as a consequence of an Action or process.

Example:

Action:
RenewCard(card_1234)
Outcome:
Card renewed successfully.

Outcome answers:

What actually happened?

See:

outcome.md

⸻

15. The Fundamental Distinctions

Noema’s ontology depends heavily on maintaining semantic boundaries.

Intent vs Action

Intent:
Renew my card.
Action:
RenewCard(card_1234)

Intent is the objective.

Action is an operation.

⸻

Action vs Capability

Action:
RenewCard(card_1234)
Capability:
card.renew

Action is a concrete operation.

Capability is an available ability.

⸻

Capability vs Authority

A system may have the Capability to perform an Action without having Authority to perform it in a particular context.

Capability:
refund.payment
Authority:
DENIED

⸻

Authority vs Trust

Authority is a governance fact.

Trust is Noema’s decision regarding whether the current Intent/Action can proceed under the applicable evidence, constraints, policies, and authority.

⸻

Execution vs Outcome

Execution:
Request sent successfully.
Outcome:
Payment actually completed.

The first describes an attempt.

The second describes what happened in the domain.

⸻

Outcome vs Intent Satisfaction

Outcome:
Transfer completed.
Intent:
Transfer $500 to Alice.
Actual:
$500 transferred to Bob.

Operationally:

SUCCESS

Semantically:

UNSATISFIED

This distinction is critical.

⸻

16. The Intent-to-Outcome Loop

The ontology can be reduced to one central loop:

        ┌───────────────────────┐
        │                       │
        ▼                       │
      Actor                     │
        │                       │
        ▼                       │
      Intent                    │
        │                       │
        ▼                       │
    Resolution                 │
        │                       │
        ▼                       │
      Trust                    │
        │                       │
        ▼                       │
      Action                   │
        │                       │
        ▼                       │
    Execution                  │
        │                       │
        ▼                       │
     Outcome                   │
        │                       │
        ▼                       │
  Satisfaction ────────────────┘

The loop closes when Noema determines whether the resulting Outcome satisfies the original Intent.

⸻

17. Expression → Intent

Humans rarely express Intent in canonical form.

For example:

“Can you sort out my card?”

Possible interpretations:

RenewCard
ReplaceCard
UnblockCard
CancelCard

Noema must resolve the expression into a sufficiently reliable Intent.

The Model may assist with this process.

The Model does not become the canonical authority.

⸻

18. Candidate Intent

Before an Intent is fully resolved, Noema may have one or more candidate interpretations.

Expression
     │
     ▼
┌───────────────┐
│ Candidate A   │
│ Candidate B   │
│ Candidate C   │
└───────┬───────┘
        ▼
Context + Evidence
        │
        ▼
Canonical Intent

If no candidate reaches the required confidence or evidence threshold:

Clarification Required

⸻

19. Deterministic Resolution Boundary

Noema’s Trust Engine should be deterministic.

The model may be probabilistic.

Therefore:

Model
  ↓
Probabilistic Interpretation
  ↓
Noema Semantic Representation
  ↓
Deterministic Validation
  ↓
Deterministic Trust Decision

Noema must not rely on probabilistic model confidence as a substitute for deterministic requirements.

⸻

20. Uncertainty Is a First-Class State

Noema must explicitly represent uncertainty.

Examples:

Unknown target
Missing parameter
Ambiguous Intent
Conflicting Context
Unverified Outcome
Unknown external state

The system must not transform:

Unknown

into:

Known

merely to continue execution.

⸻

21. Clarification as a Semantic State

When material ambiguity exists, clarification is not an error.

It is a legitimate state transition.

Intent
  ↓
Incomplete
  ↓
Clarification Required
  ↓
Actor Response
  ↓
Resolved Intent

The system should ask the smallest question necessary to remove the ambiguity.

⸻

22. Trust Boundary

The ontology establishes a boundary between:

Interpretation

and:

Consequential Execution

Conceptually:

        INTERPRETATION
              │
              ▼
        Candidate Intent
              │
              ▼
       Canonical Intent
              │
              ▼
          Validation
              │
              ▼
        ─────────────
         TRUST BOUNDARY
        ─────────────
              │
              ▼
            Action
              │
              ▼
          Execution

Crossing this boundary requires satisfying Noema’s deterministic conditions.

⸻

23. Intent Is the Unit of Meaning

Noema should treat Intent as the semantic unit connecting human interaction to execution.

Human
  ↓
Intent
  ↓
Action

This means integrations should not primarily be modeled as:

User → Tool

but:

Actor → Intent → Capability → Action

with governance and trust between them.

⸻

24. Capability Matching

After an Intent has been resolved, Noema may determine which Capabilities can satisfy it.

Intent
   ↓
Required Capability
   ↓
Available Capabilities
   ↓
Candidate Action

Example:

Intent:
Renew Card
Required Capability:
card.renew
Available:
bank.card.renew

Capability matching does not itself authorize execution.

⸻

25. Authority

Authority determines whether an Actor may perform a particular operation under a particular scope.

Example:

Actor:
Employee
Intent:
Approve payment of $100,000
Authority:
Maximum approval = $50,000

The Intent may be perfectly understood.

The Action may be technically possible.

The Actor may still lack sufficient Authority.

⸻

26. Constraints and Policies

Constraints and Policies shape the conditions under which Intent may be fulfilled.

Intent
   │
   ├── Actor constraints
   ├── Domain constraints
   ├── Policy constraints
   └── System constraints

Noema should make these restrictions explicit rather than embedding them invisibly inside prompts or tools.

⸻

27. Action Planning

An Intent may require one or more Actions.

Intent
   ↓
Action Plan
   ├── Action A
   ├── Action B
   └── Action C

The Action Plan is implementation-oriented.

The Intent remains the semantic objective.

Different Action Plans may fulfill the same Intent.

⸻

28. Outcome Verification

Noema should verify consequential Outcomes rather than assuming them.

Action
  ↓
Execution
  ↓
External System
  ↓
Evidence
  ↓
Outcome
  ↓
Verification

This is especially important for:

* asynchronous systems
* distributed systems
* external APIs
* eventual consistency
* financial operations
* irreversible Actions

⸻

29. Provenance

Every material semantic decision should be traceable to its source.

Conceptually:

Expression
   ↓
Interpretation
   ↓
Intent
   ↓
Context / Evidence
   ↓
Trust Decision
   ↓
Action
   ↓
Outcome

Provenance allows Noema to answer:

Why did the system believe this was the user’s Intent?

and:

Why did the system allow this Action?

and:

How does the system know this Outcome occurred?

⸻

30. Temporal Semantics

Intent, Action, and Outcome exist across time.

Noema should distinguish:

requested_at
resolved_at
authorized_at
started_at
completed_at
observed_at
verified_at

Temporal semantics are important for:

* scheduled Actions
* recurring Intents
* deadlines
* expiration
* stale Context
* State transitions
* Outcome verification

⸻

31. Historical Truth vs Current Truth

The ontology must distinguish what happened historically from what is true now.

Example:

10:00
Card = active
11:00
Card = suspended

The fact that the card was active at 10:00 remains historically true.

Therefore:

Historical Outcome
        ≠
Current State

Noema should preserve temporal history rather than rewriting it.

⸻

32. Composite Intents

An Intent may contain multiple objectives.

Example:

“Cancel my old plan and upgrade me to Pro.”

Canonical representation:

Composite Intent
├── Cancel Subscription
└── Upgrade Subscription

Dependencies between those objectives must be explicit.

⸻

33. Derived Intents

Agents may derive new Intents from an existing Intent.

Principal Intent
       ↓
Agent Reasoning
       ↓
Derived Intent

Example:

Principal Intent:
Keep inventory above 100 units.
Derived Intent:
Order 50 units.

The derived Intent must retain its relationship to the originating Intent and Actor.

⸻

34. Delegation

An Actor may delegate authority to another Actor.

Principal
   │
   │ delegates
   ▼
Agent
   │
   ▼
Intent

Delegation does not imply unlimited Authority.

The delegated scope must remain explicit.

⸻

35. Ontology as a Contract

The ontology is not merely documentation.

It is intended to become the semantic contract shared by:

Noema Runtime
Noema Trust Engine
SDKs
Connectors
Agent Interfaces
Application Integrations
Documentation
Schemas
Tests
Observability

Changes to foundational concepts therefore have architectural consequences.

⸻

36. Canonical Vocabulary

The following terms have specific meanings within Noema.

Term	Canonical Meaning
Actor	Entity expressing or initiating an Intent
Intent	Desired objective of an Actor
Action	Operation performed to fulfill an Intent
Capability	Ability available to perform an operation
Entity	Identifiable object or subject in the domain
Context	Information relevant to interpretation/evaluation
Constraint	Condition limiting fulfillment
Concept	Abstract semantic category
Authority	Permission/scope to perform an operation
Policy	Rule governing behavior
Trust	Determination that an Intent/Action may proceed
Execution	Attempt to perform an Action
Evidence	Information supporting a semantic claim
Outcome	Observable result of an Action/process
State	Condition of an Entity or system
Provenance	Origin and lineage of information
Satisfaction	Degree to which Outcome fulfills Intent

⸻

37. Ontology Directory

The ontology currently contains:

01-ontology/
│
├── overview.md
│
├── concepts.md
├── glossary.md
│
├── actor.md
├── intent.md
├── action.md
├── capability.md
│
├── entities.md
├── context.md
├── constraint.md
│
└── outcome.md

Additional documents may be introduced as the ontology matures.

Potential future foundational concepts include:

authority.md
policy.md
evidence.md
execution.md
state.md
provenance.md
resource.md
event.md
satisfaction.md

These should only become canonical documents when their semantics are sufficiently stable.

⸻

38. Relationship Map

The primary ontology relationships can be summarized as:

Actor
  │
  └── expresses ─────────► Intent
                              │
                              ├── targets ──────► Entity
                              │
                              ├── interpreted by ► Context
                              │
                              └── constrained by ► Constraint
Intent
  │
  └── fulfilled through ──► Action
                              │
                              └── enabled by ───► Capability
                                                       │
                                                       ▼
                                                   Execution
                                                       │
                                                       ▼
                                                    Outcome
                                                       │
                                                       ├── supported by ──► Evidence
                                                       │
                                                       └── evaluated as ──► Satisfaction

Governance surrounds the execution path:

                Policy
                  │
                  ▼
Constraint ──► Authority ──► Trust
                              │
                              ▼
                            Action

⸻

39. The Noema Principle

The ontology is built around one central principle:

Human intent should become a canonical semantic object before consequential execution is permitted.

This creates the architectural boundary:

Natural Language
       ↓
Interpretation
       ↓
Canonical Intent
       ↓
Deterministic Trust
       ↓
Action
       ↓
Outcome

⸻

40. Canonical Invariants

The ontology MUST preserve the following invariants:

1. Intent is distinct from its natural-language expression.
2. Intent is distinct from Action.
3. Action is distinct from Capability.
4. Capability does not imply Authority.
5. Authority does not automatically imply Trust.
6. Model interpretation does not automatically establish canonical Intent.
7. Material ambiguity must not be silently resolved.
8. Unknown information must remain explicitly unknown.
9. Intent must be sufficiently resolved before consequential Action.
10. Trust must be evaluated before consequential execution.
11. Execution success does not imply business success.
12. Outcome must be distinguished from Execution Result.
13. Outcome must be verified where verification is required.
14. Outcome must be evaluated against the original Intent.
15. Historical Outcomes must not be erased by later State changes.
16. Material semantic decisions must retain provenance.
17. Derived and delegated Intents must retain their lineage.
18. Material Intent changes require appropriate revalidation.
19. Constraints and Policies must not be hidden inside model prompts or tool implementations.
20. The ontology defines semantics; implementation details belong elsewhere.

⸻

41. What This Ontology Is Not

The ontology does not define:

* API endpoints
* database schemas
* SDK implementation
* prompt templates
* model architecture
* UI components
* connector implementation
* infrastructure
* application-specific business logic

Those belong in their respective repository domains.

The ontology defines the meaning and relationships that those systems must implement consistently.

⸻

42. Canonical Mental Model

The simplest way to understand Noema’s ontology is:

WHO?
  Actor
   │
   ▼
WANTS WHAT?
  Intent
   │
   ▼
ABOUT WHAT?
  Entity
   │
   ▼
UNDER WHAT CONDITIONS?
  Context + Constraints + Policy
   │
   ▼
IS IT ALLOWED?
  Authority + Trust
   │
   ▼
WHAT CAN DO IT?
  Capability
   │
   ▼
WHAT SHOULD BE DONE?
  Action
   │
   ▼
WHAT HAPPENED?
  Execution + Outcome
   │
   ▼
DID IT ACHIEVE THE GOAL?
  Satisfaction

This is the semantic backbone of Noema.

⸻

43. Final Canonical Statement

Noema’s ontology provides a canonical language for representing who wants what, what that intent refers to, what constraints and authority govern it, what actions may fulfill it, what capabilities enable those actions, what actually happened, and whether the resulting outcome satisfied the original intent.

The ontology therefore transforms the conventional:

LLM → Tool Call

model into:

Actor
  ↓
Intent
  ↓
Context + Entities + Constraints
  ↓
Resolution
  ↓
Authority + Trust
  ↓
Action
  ↓
Capability
  ↓
Execution
  ↓
Evidence
  ↓
Outcome
  ↓
Intent Satisfaction

That chain is the core semantic contract of Noema.