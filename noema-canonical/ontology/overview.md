Overview

Status: Foundational
Version: 0.2
Domain: Ontology
Canonical Path: ontology/overview.md

⸻

1. Purpose

The Noema Ontology defines the canonical semantic concepts and relationships required to represent an Actor’s Intent, determine the conditions under which it may be fulfilled, translate it into permitted Actions, observe what occurred, and evaluate whether the resulting Outcome satisfied the original Intent.

The ontology establishes a shared semantic vocabulary across:

* humans
* AI models
* Noema Runtime
* Trust Engine
* applications
* enterprise systems
* agents
* tools
* connectors
* SDKs

Its primary purpose is to prevent concepts with different semantic meanings from being collapsed into one another.

The foundational distinctions are:

Intent        ≠ Action
Action        ≠ Capability
Capability    ≠ Authority
Authority     ≠ Trust
Action        ≠ Execution
Execution     ≠ Execution Result
Execution     ≠ Outcome
Outcome       ≠ State
Outcome       ≠ Satisfaction

These distinctions form the semantic foundation of Noema.

⸻

2. The Problem Noema Solves

Conventional AI application architectures often collapse a consequential workflow into:

User
  ↓
LLM
  ↓
Tool Call

This creates a semantic gap between what an Actor expressed and what a system actually does.

For example:

"Cancel my subscription."

may be transformed directly into:

cancel_subscription()

without establishing:

* which Actor expressed the request
* which subscription is being referenced
* what the Actor actually intends
* whether the Intent is sufficiently resolved
* which Entities are involved
* which Context is relevant
* which Constraints apply
* whether the Actor has Authority
* whether the Action is permitted
* which Capability enables the Action
* what Execution occurred
* what Outcome actually occurred
* what Evidence establishes that Outcome
* whether the Outcome satisfied the original Intent

Noema introduces explicit semantic boundaries between these concepts.

⸻

3. The Noema Semantic Model

The canonical semantic flow is:

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
  └──────────────► Constraint
          │
          ▼
      Resolution
          │
          ▼
      Validation
          │
          ▼
       Authority
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
 Execution Result / External Observation
          │
          ▼
       Evidence
          │
          ▼
       Outcome
          │
          ▼
    Satisfaction

This represents the core semantic lifecycle:

Expression
    ↓
Intent
    ↓
Resolution
    ↓
Validation
    ↓
Governance
    ↓
Trust
    ↓
Action
    ↓
Execution
    ↓
Observation / Evidence
    ↓
Outcome
    ↓
Intent Satisfaction

The ontology defines the meaning of these concepts and their relationships. It does not prescribe a particular implementation architecture.

⸻

4. Ontology Layers

The ontology may be understood through several conceptual layers:

┌──────────────────────────────────────┐
│              EXPRESSION              │
│  Human / Agent expression            │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│               SEMANTICS              │
│  Actor · Intent · Entity · Context   │
│  Concept                             │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│              GOVERNANCE              │
│  Constraint · Policy · Authority    │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│                TRUST                 │
│  Determination to permit progression │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│               ACTION                 │
│  Operation selected to fulfill Intent│
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│             EXECUTION                │
│  Attempt to perform an Action        │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│          OBSERVATION / RESULT        │
│  Execution Result · Evidence         │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│               OUTCOME                │
│  What actually occurred              │
└───────────────────┬──────────────────┘
                    ▼
┌──────────────────────────────────────┐
│             SATISFACTION             │
│  Relationship of Outcome to Intent   │
└──────────────────────────────────────┘

These are conceptual layers, not necessarily physical software modules.

⸻

5. Foundational Concepts

The foundational ontology consists of:

Actor
Intent
Action
Capability
Entity
Context
Constraint
Concept
Authority
Policy
Trust
Execution
Evidence
Outcome
State
Provenance
Satisfaction

Not every concept necessarily requires an independent canonical document at the same stage of ontology development.

A concept should become a canonical ontology object when its semantics are sufficiently stable and its distinction is architecturally meaningful.

⸻

6. Actor

An Actor is an entity that expresses, owns, initiates, or is otherwise responsible for an Intent within a Noema interaction.

An Actor may be:

* Human
* Organization
* Service
* Agent
* System
* Process

Actor answers:

Who is expressing or initiating this Intent?

See:

actor.md

⸻

7. Intent

An Intent is the canonical semantic representation of an Actor’s desired objective.

It represents what the Actor wants to accomplish independently of the particular Action ultimately used to accomplish it.

Example:

Actor:
Customer
Intent:
Renew Card
Entity:
card_1234

Intent answers:

What does the Actor want to accomplish?

Intent is the central semantic object connecting expression to consequential execution.

See:

intent.md

⸻

8. Action

An Action is a concrete operation that may be performed in pursuit of an Intent.

Example:

Intent:
Renew Card
Action:
RenewCard(card_1234)

An Action is therefore downstream from Intent.

The same Intent may be fulfilled through different Actions or Action Plans.

See:

action.md

⸻

9. Capability

A Capability represents an ability available to an Actor, system, service, tool, or other execution resource.

Example:

Capability:
card.renew

Capability answers:

What can be done?

It does not answer:

What should be done?

Capability availability does not establish Authority or Trust.

See:

capability.md

⸻

10. Entity

An Entity is a distinct object or subject that can be identified, referenced, observed, modified, or acted upon.

Examples:

* Customer
* Card
* Account
* Transaction
* Subscription
* Employee
* Organization

Entities provide the subjects and targets to which Intents and Actions refer.

See:

entities.md

⸻

11. Context

Context is information relevant to the interpretation, resolution, validation, execution, or evaluation of an Intent.

Examples include:

* conversation history
* application state
* Actor session
* relevant Entities
* previous Actions
* temporal information
* environmental information

Context answers:

What surrounding information is relevant to understanding or evaluating this Intent?

See:

context.md

⸻

12. Constraint

A Constraint specifies a condition that limits how an Intent may be fulfilled.

Examples:

amount <= $5,000
only during business hours
requires approval
direct flights only

Constraints answer:

What limits apply?

Constraints must remain semantically explicit rather than being hidden inside model prompts, tool implementations, or application-specific execution logic.

See:

constraint.md

⸻

13. Concept

A Concept is an abstract semantic category used to describe a domain.

Examples:

* Payment
* Subscription
* Renewal
* Approval
* Transfer
* Customer
* Account

Concepts provide vocabulary from which concrete Entities, Intents, Actions, and Capabilities may be described.

See:

concepts.md

⸻

14. Authority

Authority represents the scope within which an Actor is permitted to perform an operation or cause an effect.

For example:

Actor:
Employee
Requested Action:
Approve Payment
Authority:
Maximum approval = $50,000

An Intent may be perfectly understood and an Action may be technically possible while the Actor nevertheless lacks sufficient Authority.

Authority therefore remains distinct from Capability.

⸻

15. Policy

A Policy is a rule or governing specification that determines conditions under which behavior or execution is permitted, required, prohibited, or constrained.

Policies may establish or contribute to:

* Authority requirements
* execution restrictions
* approval requirements
* operational constraints
* governance conditions

Policy is distinct from the individual Constraint it produces or applies.

⸻

16. Trust

Trust represents Noema’s determination regarding whether a resolved Intent or proposed Action may proceed under the applicable semantic, governance, evidentiary, and policy conditions.

Conceptually:

Intent
   ↓
Resolution
   ↓
Validation
   ↓
Authority + Policy + Constraints + Evidence
   ↓
Trust
   ↓
Action

Trust is therefore distinct from Authority.

Authority is a governance fact or relationship.

Trust is Noema’s resulting determination within the execution lifecycle.

⸻

17. Execution

An Execution represents an attempt to perform an Action.

Execution describes the operational process through which an Action is invoked.

It must remain distinct from the business Outcome.

For example:

Action:
TransferFunds
Execution:
Request submitted successfully
Outcome:
Funds actually transferred

An Execution may succeed technically while the intended business effect remains unknown, fails, or does not satisfy the Intent.

⸻

18. Execution Result

An Execution Result represents information returned or produced by the execution mechanism.

For example:

HTTP 200
{
  "transaction_id": "tx_123"
}

An Execution Result does not automatically establish the business Outcome.

For example:

HTTP 202 Accepted

may establish that processing was accepted without establishing that the requested operation completed.

Therefore:

Execution Result ≠ Outcome

unless the relevant system contract explicitly establishes the equivalence.

⸻

19. Evidence

Evidence is information that supports a semantic claim or determination.

Evidence may originate from:

* external APIs
* databases
* system-of-record queries
* events
* signed responses
* receipts
* state observations
* human confirmation
* other trusted observations

Evidence provides the basis through which Noema can establish or verify an Outcome.

Model inference may contribute to interpretation but should not, by itself, establish a consequential Outcome where authoritative verification is required.

⸻

20. Outcome

An Outcome represents the observable result produced by an Action, Execution, or domain process.

Outcome answers:

What actually happened?

Outcome remains distinct from:

Intent
Action
Execution
Execution Result
State
Satisfaction

The core relationship is:

Intent
   ↓
Action
   ↓
Execution
   ↓
Observation / Evidence
   ↓
Outcome
   ↓
Satisfaction

See:

outcome.md

⸻

21. State

State represents a condition of an Entity or system at a particular point in time.

Example:

Card.status = active

A State may provide Evidence for an Outcome, but it is not itself the Outcome.

For example:

Action:
RenewCard
State Change:
expired → active
Outcome:
Card renewal completed

State therefore remains independently modeled.

⸻

22. Provenance

Provenance represents the origin, lineage, and supporting source information associated with a semantic claim, decision, or observation.

Provenance allows Noema to establish:

* where an Intent interpretation came from
* what Evidence supported a Trust decision
* where an Outcome observation originated
* which system or Actor supplied the information
* how a semantic record was derived or transformed

Material semantic decisions should retain sufficient provenance for reconstruction and audit.

⸻

23. Satisfaction

Satisfaction represents the degree to which an observed Outcome fulfills the originating Intent.

The foundational vocabulary is:

SATISFIED
PARTIALLY_SATISFIED
UNSATISFIED
UNKNOWN

Satisfaction must remain distinct from operational Outcome status.

For example:

Operational Outcome:
SUCCEEDED
Intent Satisfaction:
UNSATISFIED

This is possible when an Action executes successfully but produces the wrong business result.

⸻

24. Fundamental Distinctions

The ontology depends on preserving the following semantic boundaries.

Intent vs Action

Intent:
Renew my card.
Action:
RenewCard(card_1234)

Intent is the desired objective.

Action is an operation used to pursue that objective.

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

A system may possess the Capability to perform an operation without the Actor having Authority to cause that operation in a particular context.

Capability:
refund.payment
Authority:
DENIED

⸻

Authority vs Trust

Authority describes a governance relationship or permission scope.

Trust represents Noema’s determination regarding whether the current semantic request may proceed under the applicable conditions.

⸻

Execution vs Outcome

Execution:
Request submitted.
Outcome:
Payment completed.

Execution describes an attempt.

Outcome describes what occurred in the domain.

⸻

Execution Result vs Outcome

Execution Result:
HTTP 200
Outcome:
Funds transferred.

A technical response does not automatically establish a business result.

⸻

Outcome vs Satisfaction

Intent:
Transfer $500 to Alice.
Outcome:
$500 transferred to Bob.
Operational status:
SUCCEEDED
Satisfaction:
UNSATISFIED

Technical success and semantic fulfillment are separate evaluations.

⸻

25. Intent as the Semantic Unit

Noema treats Intent as the semantic unit connecting human or agent interaction to consequential execution.

The basic transformation is:

Expression
    ↓
Intent
    ↓
Action

Therefore the primary integration model is not:

User → Tool

but:

Actor
  ↓
Intent
  ↓
Governance + Trust
  ↓
Action
  ↓
Capability
  ↓
Execution
  ↓
Outcome

This distinction prevents an implementation mechanism from becoming a substitute for semantic meaning.

⸻

26. Expression and Intent

Natural-language expressions are not necessarily canonical Intents.

For example:

"Can you sort out my card?"

could correspond to several possible objectives:

RenewCard
ReplaceCard
UnblockCard
CancelCard

Noema must resolve the expression into a sufficiently reliable Intent before consequential execution.

A model may assist with interpretation.

The model does not become the canonical authority for the resulting Intent.

⸻

27. Candidate Intents

Before an Intent is resolved, Noema may maintain multiple candidate interpretations.

Expression
     │
     ▼
Candidate Intent A
Candidate Intent B
Candidate Intent C
     │
     ▼
Context + Evidence + Constraints
     │
     ▼
Resolved Intent

If material ambiguity remains:

Clarification Required

The system should seek the minimum additional information required to resolve the ambiguity.

⸻

28. Deterministic Resolution Boundary

Model interpretation may be probabilistic.

Noema’s consequential semantic decisions must be governed by explicit deterministic conditions.

Conceptually:

Model
  ↓
Probabilistic Interpretation
  ↓
Semantic Representation
  ↓
Deterministic Resolution / Validation
  ↓
Deterministic Trust Decision
  ↓
Consequential Action

Model confidence is therefore not a substitute for Noema’s semantic requirements.

⸻

29. Uncertainty

Uncertainty is a first-class semantic condition.

Examples include:

* unknown target
* missing parameter
* ambiguous Intent
* conflicting Context
* unknown Authority
* unverified Outcome
* unknown external state
* conflicting Evidence

Noema must not silently transform:

UNKNOWN

into:

KNOWN

merely to permit execution or simplify system behavior.

⸻

30. Clarification

Clarification is a semantic state rather than necessarily an error.

The lifecycle may be:

Intent
  ↓
Incomplete / Ambiguous
  ↓
Clarification Required
  ↓
Actor Response
  ↓
Resolved Intent

Clarification should address material uncertainty rather than unnecessarily collecting information.

⸻

31. Trust Boundary

The ontology establishes a conceptual boundary between interpretation and consequential execution.

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
             ─────────────
              TRUST BOUNDARY
             ─────────────
                   │
                   ▼
                 Action
                   │
                   ▼
               Execution

Crossing the Trust Boundary requires the applicable semantic and governance conditions to be satisfied.

⸻

32. Capability Matching

Once an Intent has been resolved, Noema may determine which Capabilities can support it.

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
Available Capability:
bank.card.renew

Capability matching identifies what may be possible.

It does not itself establish Authority or Trust.

⸻

33. Action Planning

One Intent may require multiple Actions.

Intent
   ↓
Action Plan
   ├── Action A
   ├── Action B
   └── Action C

The Action Plan is operational.

The Intent remains the semantic objective.

Different Action Plans may therefore fulfill the same Intent.

⸻

34. Composite Intents

An Intent may contain multiple objectives.

Example:

"Cancel my old plan and upgrade me to Pro."

may be represented as:

Composite Intent
├── Cancel Subscription
└── Upgrade Subscription

Dependencies and ordering between the component objectives must remain explicit.

⸻

35. Derived Intents

An Actor or agent may derive an Intent from another Intent.

Principal Intent
      ↓
Reasoning / Planning
      ↓
Derived Intent

Example:

Principal Intent:
Keep inventory above 100 units.
Derived Intent:
Order 50 units.

A Derived Intent must retain its relationship to its originating Intent and Actor.

⸻

36. Delegation

An Actor may delegate authority to another Actor.

Principal
   │
   │ delegates
   ▼
Delegate / Agent
   │
   ▼
Intent

Delegation does not imply unrestricted Authority.

Delegated scope, conditions, and limitations must remain explicit.

⸻

37. Outcome Verification

Noema should verify consequential Outcomes rather than assuming that execution succeeded.

Action
  ↓
Execution
  ↓
External System
  ↓
Observation
  ↓
Evidence
  ↓
Outcome
  ↓
Verification
  ↓
Satisfaction

Verification may be:

* immediate
* asynchronous
* event-driven
* polling-based
* source-confirmed

This distinction is particularly important for distributed systems, asynchronous APIs, financial operations, and irreversible Actions.

⸻

38. Operational Success vs Semantic Satisfaction

Noema must preserve two separate dimensions:

Operational Outcome
        +
Intent Satisfaction

For example:

Action:
POST /transfer
Execution:
HTTP 200
Operational Outcome:
SUCCEEDED
Observed Domain Result:
Funds transferred to Bob
Original Intent:
Transfer $500 to Alice
Satisfaction:
UNSATISFIED

Consequently:

Execution Success
      ≠
Business Success
      ≠
Intent Satisfaction

These distinctions must not be collapsed.

⸻

39. Historical Truth and Current State

Noema must distinguish historical events and Outcomes from current State.

Example:

10:00
Card = active
11:00
Card = suspended

The later State does not invalidate the historical fact that the Card was active at 10:00.

Therefore:

Historical Outcome
        ≠
Current State

Historical semantic records must not be silently rewritten by subsequent State changes.

⸻

40. Temporal Semantics

Semantic objects exist across time.

Noema should preserve distinct timestamps where their meanings differ, including:

requested_at
resolved_at
authorized_at
started_at
completed_at
observed_at
verified_at

Temporal semantics are relevant to:

* scheduled Actions
* recurring Intents
* deadlines
* expiration
* stale Context
* State transitions
* asynchronous Outcomes
* verification

A timestamp should not be reused merely because multiple lifecycle events happen to occur close together.

⸻

41. Provenance and Auditability

Material semantic decisions must be reconstructable.

Conceptually:

Expression
   ↓
Interpretation
   ↓
Intent
   ↓
Context / Evidence
   ↓
Authority / Policy
   ↓
Trust Decision
   ↓
Action
   ↓
Execution
   ↓
Evidence
   ↓
Outcome
   ↓
Satisfaction

Provenance allows Noema to answer:

Why was this interpreted as the Actor’s Intent?

Why was this Action permitted?

Which Capability enabled it?

What Execution occurred?

How does Noema know the Outcome occurred?

Why was the Intent considered satisfied or unsatisfied?

⸻

42. External Systems

Noema may orchestrate Actions against external systems.

The external system may produce:

* responses
* events
* state changes
* receipts
* transaction records
* other observations

Noema must distinguish the external system’s representation from its canonical semantic interpretation.

For example:

External System
      ↓
Provider Result
      ↓
Evidence
      ↓
Noema Outcome

The external response is not automatically the canonical Outcome.

⸻

43. Asynchronous Execution

For asynchronous systems:

Action
  ↓
Accepted
  ↓
Processing
  ↓
Completed
  ↓
Verified

An initial response may establish only:

Execution Accepted

The final Outcome may require:

* webhook
* event
* callback
* polling
* system-of-record query
* other authoritative observation

Therefore Noema must support Outcomes whose final status is not immediately known.

⸻

44. Outcome Uncertainty

Distributed systems can make the final Outcome temporarily or permanently uncertain.

Examples:

Network timeout
External service unavailable
Event not received
Eventual consistency
Conflicting sources
Unknown transaction state

Noema must preserve:

UNKNOWN

when the evidence does not establish success or failure.

In particular:

Timeout
   ≠
FAILED

A timeout may mean that Noema cannot determine whether the operation succeeded.

⸻

45. Model Inference

A model may produce an interpretation such as:

"Payment probably succeeded."

This is not equivalent to:

Outcome = SUCCEEDED

where authoritative verification is required.

Model inference may therefore be represented as evidence or an inference with appropriate provenance, confidence, and status, while the canonical Outcome remains unresolved until sufficient Evidence exists.

⸻

46. Multiple Outcomes

A single Intent may produce multiple Outcomes.

Example:

Intent:
Onboard Employee
Outcomes:
1. Employee created
2. Email account created
3. Permissions assigned
4. Welcome email sent

Noema may evaluate these Outcomes collectively when determining Composite Intent Satisfaction.

⸻

47. Partial Success

Composite operations require explicit partial-success semantics.

Example:

Action A ✓
Action B ✓
Action C ✗
Action D not attempted

The resulting operational evaluation may be:

PARTIALLY_SUCCEEDED

The ontology must not collapse partial completion into full success.

Likewise, operational partial success and semantic partial satisfaction remain separate dimensions.

⸻

48. Dependencies and Compensation

Outcomes may depend upon previous Outcomes.

Create Account
      ↓
Account Created
      ↓
Fund Account
      ↓
Funding Completed

If an earlier Action fails, later Actions may not execute.

A multi-step process may also require compensation:

Create Resource
      ↓
Outcome: Created
Charge Customer
      ↓
Outcome: Charged
Provision Service
      ↓
Outcome: Failed
Refund Customer
      ↓
Outcome: Refunded

The compensation Outcome does not erase the original Outcomes.

⸻

49. Retries and Idempotency

Execution Attempts and business Outcomes must remain distinct.

Example:

Execution Attempt 1
      ↓
Timeout
Execution Attempt 2
      ↓
Success

These may correspond to one underlying business Outcome:

Transfer Completed

Noema must use correlation and idempotency semantics where available to avoid incorrectly treating retries as independent business Outcomes.

⸻

50. Outcome Correction

Historical Outcomes must not be silently rewritten.

If an Outcome was incorrectly recorded:

Original Outcome
      ↓
Correction / Supersession
      ↓
Current Interpretation

The original record remains part of the semantic lineage.

This preserves auditability and historical reconstruction.

⸻

51. Ontology as a Contract

The ontology is not merely documentation.

It is the semantic contract shared across:

* Noema Runtime
* Trust Engine
* SDKs
* connectors
* agent interfaces
* application integrations
* schemas
* tests
* observability
* documentation

Changes to foundational concepts therefore have architectural consequences.

The ontology defines meaning and relationships.

Implementation domains define how those meanings are represented and executed.

⸻

52. Canonical Vocabulary

Term	Canonical Meaning
Actor	Entity that expresses or initiates an Intent
Intent	Desired objective of an Actor
Action	Operation performed to fulfill an Intent
Capability	Ability available to perform an operation
Entity	Identifiable object or subject in the domain
Context	Information relevant to interpretation or evaluation
Constraint	Condition limiting fulfillment
Concept	Abstract semantic category
Authority	Permission or scope governing an Actor’s ability to cause an operation or effect
Policy	Rule governing behavior or execution
Trust	Noema’s determination that an Intent or Action may proceed
Execution	Attempt to perform an Action
Execution Result	Result or response produced by the execution mechanism
Evidence	Information supporting a semantic claim or determination
Outcome	Observable result of an Action or process
State	Condition of an Entity or system at a point in time
Provenance	Origin and lineage of information or semantic determination
Satisfaction	Degree to which an Outcome fulfills an Intent

⸻

53. Relationship Model

The primary ontology relationships can be summarized as:

Actor
  │
  └── expresses ─────────► Intent
                              │
                              ├── concerns ───────► Entity
                              │
                              ├── interpreted with ► Context
                              │
                              └── constrained by ──► Constraint
                                                        │
                                                        ▼
                                                     Policy
                                                        │
                                                        ▼
                                                    Authority
                                                        │
                                                        ▼
                                                     Trust
                                                        │
                                                        ▼
                                                     Action
                                                        │
                                                        ├── enabled by ──► Capability
                                                        │
                                                        ▼
                                                     Execution
                                                        │
                                                        ├── produces ────► Execution Result
                                                        │
                                                        ▼
                                                     Evidence
                                                        │
                                                        ▼
                                                     Outcome
                                                        │
                                                        └── evaluated as ► Satisfaction

State and Provenance cross these relationships without replacing the concepts they describe.

⸻

54. The Intent-to-Outcome Loop

The central semantic loop is:

        ┌────────────────────────────┐
        │                            │
        ▼                            │
      Actor                          │
        │                            │
        ▼                            │
      Intent                         │
        │                            │
        ▼                            │
    Resolution                       │
        │                            │
        ▼                            │
      Trust                          │
        │                            │
        ▼                            │
      Action                         │
        │                            │
        ▼                            │
    Execution                        │
        │                            │
        ▼                            │
     Outcome                         │
        │                            │
        ▼                            │
   Satisfaction ─────────────────────┘

The loop closes when Noema evaluates the resulting Outcome against the originating Intent.

This is what distinguishes a semantic execution system from a system that merely issues tool calls.

⸻

55. Canonical Mental Model

The ontology can be understood through the following questions:

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
IN WHAT CONTEXT?
  Context
   │
   ▼
UNDER WHAT LIMITS?
  Constraints + Policy
   │
   ▼
WHO MAY CAUSE IT?
  Authority
   │
   ▼
MAY IT PROCEED?
  Trust
   │
   ▼
WHAT CAN PERFORM IT?
  Capability
   │
   ▼
WHAT SHOULD BE DONE?
  Action
   │
   ▼
WHAT WAS ATTEMPTED?
  Execution
   │
   ▼
WHAT WAS OBSERVED?
  Evidence
   │
   ▼
WHAT ACTUALLY HAPPENED?
  Outcome
   │
   ▼
DID IT ACHIEVE THE OBJECTIVE?
  Satisfaction

This is the semantic backbone of Noema.

⸻

56. Canonical Invariants

The ontology MUST preserve the following invariants:

1. Intent is distinct from its natural-language expression.
2. Intent is distinct from Action.
3. Action is distinct from Capability.
4. Capability does not imply Authority.
5. Authority is distinct from Trust.
6. Model interpretation does not automatically establish canonical Intent.
7. Material ambiguity must not be silently resolved.
8. Unknown information must remain explicitly unknown.
9. Intent must be sufficiently resolved before consequential Action.
10. Applicable governance conditions must be evaluated before consequential execution.
11. Trust must be established before consequential execution.
12. Execution is distinct from Outcome.
13. Execution Result is distinct from Outcome.
14. Execution success does not imply business success.
15. Execution success does not imply Intent Satisfaction.
16. Outcome must be distinguished from current Entity or system State.
17. Outcome must be verified where verification is required.
18. Outcome must be evaluated against the originating Intent.
19. Historical Outcomes must not be silently overwritten by later State.
20. Material semantic decisions must retain appropriate Provenance.
21. Derived Intents must retain their lineage.
22. Delegated Intents must retain delegation lineage and scope.
23. Material Intent changes require appropriate revalidation.
24. Constraints and Policies must not be hidden inside model prompts or tool implementations.
25. Model inference alone must not establish a consequential Outcome where authoritative verification is required.
26. Unknown Outcome must not be converted into failure without evidence.
27. Unknown Outcome must not be converted into success without evidence.
28. Conflicting Evidence must remain represented until appropriately reconciled.
29. Retries must remain distinguishable from independent business Outcomes.
30. Compensating Actions must not erase original Outcomes.
31. Partial completion must remain explicitly representable.
32. The ontology defines semantic meaning; implementation details belong to other repository domains.

⸻

57. What This Ontology Is Not

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

Those belong to their respective repository domains.

The ontology defines the canonical semantics and relationships that those systems must implement consistently.

⸻

58. Ontology Directory

The ontology currently contains:

ontology/
│
├── overview.md
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

These should become canonical documents only when their semantics are sufficiently stable and their separation is justified by the ontology.

⸻

59. The Noema Principle

The ontology is built around one central principle:

Human Intent must become a canonical semantic object before consequential execution is permitted.

This establishes the architectural boundary:

Natural Language
       ↓
Interpretation
       ↓
Canonical Intent
       ↓
Resolution + Validation
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

The purpose of this boundary is not merely to structure execution.

It preserves the distinction between:

what was expressed
what was intended
what was permitted
what was selected
what was attempted
what technically occurred
what actually occurred in the domain
what evidence establishes it
and whether the original objective was satisfied

⸻

60. Final Canonical Statement

Noema’s ontology provides a canonical semantic language for representing:

* who wants something
* what they want
* what the Intent concerns
* what Context is relevant
* what Constraints and Policies apply
* what Authority governs the request
* whether the request may proceed
* what Action can fulfill it
* what Capability enables that Action
* what Execution occurred
* what Evidence establishes the result
* what Outcome actually occurred
* and whether that Outcome satisfied the originating Intent

The ontology therefore transforms the conventional:

LLM
  ↓
Tool Call

into:

Actor
  ↓
Intent
  ↓
Context + Entity + Constraints
  ↓
Resolution
  ↓
Validation
  ↓
Authority + Policy
  ↓
Trust
  ↓
Action
  ↓
Capability
  ↓
Execution
  ↓
Execution Result + Observation
  ↓
Evidence
  ↓
Outcome
  ↓
Intent Satisfaction

The resulting model gives Noema a closed semantic loop rather than a one-way agent/tool pipeline.

The core invariant is:

Intent
  ≠
Action
  ≠
Capability
  ≠
Authority
  ≠
Trust
  ≠
Execution
  ≠
Execution Result
  ≠
Outcome
  ≠
State
  ≠
Satisfaction

That separation is the semantic foundation on which Noema can make consequential AI behavior interpretable, governable, deterministic at the trust boundary, observable, and auditable.