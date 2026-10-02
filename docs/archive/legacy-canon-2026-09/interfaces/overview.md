> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Overview

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/overview.md

⸻

1. Definition

The Interfaces layer defines the boundaries through which Noema receives intent, accesses context, represents events, creates and observes execution, and connects to external enterprise systems.

The Interfaces layer is not the semantic core of Noema.

It is the boundary around the semantic core.

                    ┌─────────────────────────┐
                    │        EXTERNAL          │
                    │ Users / Agents / Systems │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       05-INTERFACES      │
                    │                         │
                    │ Intent API              │
                    │ Action API              │
                    │ Context API             │
                    │ Trust API               │
                    │ Execution API           │
                    │ Event Model             │
                    │ Integration Model       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      NOEMA CORE         │
                    │                         │
                    │ Ontology                │
                    │ Intent                  │
                    │ Trust                   │
                    │ Execution               │
                    └─────────────────────────┘

⸻

2. Purpose

The Interfaces layer exists to make Noema’s canonical model usable by:

* applications
* enterprise systems
* AI agents
* human-facing interfaces
* developers
* workflow systems
* event infrastructure
* external service providers

It defines how systems communicate with Noema, without allowing those external systems to redefine Noema’s semantics.

⸻

3. Core Principle

Interfaces expose Noema’s canonical model; they do not define it.

The canonical semantics live in:

ontology
intent
trust
execution

The Interfaces layer exposes those semantics through stable boundaries.

Canonical Model
      ↓
Interfaces
      ↓
External Consumers

Not:

External API
      ↓
changes canonical semantics

⸻

4. Why an Interfaces Layer Exists

Noema interacts with fundamentally different kinds of systems.

A user expresses intent.

An application submits structured requests.

An enterprise system provides context.

A provider emits an event.

An execution system performs an Action.

A third-party API provides a capability.

These interactions require different interfaces.

The Interfaces layer gives each interaction an explicit boundary.

⸻

5. Interface Structure

The current structure is:

interfaces/
│
├── overview.md
├── intent-api.md
├── action-api.md
├── trust-api.md
├── context-api.md
├── execution-api.md
├── event-model.md
└── integration-model.md

Each file represents a distinct boundary.

⸻

6. Interface Domains

Interface	Primary Responsibility
intent-api.md	Receive and manage Intent from any source
action-api.md	Represent and expose executable Actions
trust-api.md	Expose the deterministic Trust evaluation boundary
context-api.md	Provide contextual information to Intent and Execution
event-model.md	Represent observable state changes and occurrences
execution-api.md	Coordinate and observe execution
integration-model.md	Connect Noema to external enterprise systems
overview.md	Define the relationship and boundaries across all interfaces

⸻

7. Intent API

The Intent API is the entry point for desired outcomes. It accepts intent from human, agent, system, or application sources and converts probabilistic or structured inputs into canonical Intent objects.

User / Agent / System
     │
     ▼
 Intent API
     │
     ▼
   Intent

It handles:

* intent submission from any source
* interpretation and schema validation
* resolution of ambiguous or underspecified intent
* clarification lifecycle
* executable intent production
* intent versioning and immutability
* intent lifecycle state

It does not authorize or execute the resulting Action.

The probabilistic-to-canonical translation is an internal implementation detail. The interface contract operates on canonical Intent objects.

⸻

8. Context API

The Context API provides information required to understand and evaluate an Intent or Action.

                ┌──────────────┐
                │  Context API │
                └───────┬──────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
      Actor          Resource         History

Context can include:

* actors
* resources
* relationships
* current state
* historical information
* environmental information
* enterprise information

The Context API provides context.

It does not itself determine whether an Action is trusted or authorized.

⸻

9. Action API

The Action API represents executable operations.

Executable Intent
       │
       ▼
   Action API
       │
       ▼
     Action

An Action is concrete enough to be evaluated by Trust and subsequently executed.

Example:

Intent:
"Replace my card."
        ↓
Action:
issue_replacement_card(card_123)

The Action API does not interpret raw natural language.

⸻

10. Execution API

The Execution API manages the execution journey of Actions.

Action
  │
  ▼
Execution API
  │
  ├── start
  ├── observe
  ├── retry
  ├── intervene
  └── complete

It exposes execution state and lifecycle without redefining the Action itself.

⸻

11. Event Model

The Event Model represents facts about things that happened or were observed.

Something happens
       ↓
     Event
       ↓
      Noema

Events may originate internally or externally.

Examples:

intent.resolved
action.created
execution.started
execution.failed
resource.updated
provider.confirmed

Events are not commands.

⸻

12. Event vs Command

This distinction is fundamental.

Command:
"Execute this Action."
Event:
"This happened."

The Interfaces layer must preserve this distinction.

⸻

13. Integration Model

The Integration Model connects Noema to enterprise systems.

Noema
  │
  ▼
Integration
  │
  ▼
Enterprise System

It handles:

* provider adapters
* capability mappings
* request translation
* response translation
* authentication
* provider events
* failure normalization
* external resource references

Integrations must not redefine Noema’s canonical semantics.

⸻

14. The Complete Interface Graph

The interfaces form a connected system:

                         USER / AGENT / SYSTEM
                              │
                              ▼
                        ┌───────────┐
                        │ Intent API│
                        └─────┬─────┘
                              │
                              ▼
                           Intent
                              │
                              ▼
                      Executable Intent
                              │
                              ▼
                        ┌───────────┐
                        │ Action API│
                        └─────┬─────┘
                              │
                              ▼
                            Action
                              │
                              ▼
                        ┌───────────┐
                        │ Trust API │
                        └─────┬─────┘
                              │
                    EXECUTE / CLARIFY / ESCALATE / REJECT
                              │ (EXECUTE)
                              ▼
                      ┌────────────────┐
                      │ Execution API  │
                      └───────┬────────┘
                              │
                              ▼
                       Integration Model
                              │
                              ▼
                     Enterprise System

Alongside this flow:

Context API ────────────────► Intent / Trust / Execution
Event Model ◄───────────────► All lifecycle boundaries

⸻

15. Interfaces Are Not the Core

The distinction between the layers is important.

interfaces

does not define:

What is an Intent?
What is an Action?
What constitutes Trust?
What is an Outcome?

Those definitions belong to the canonical domains.

Instead, Interfaces define:

How those concepts cross system boundaries.

⸻

16. Canonical Model vs Interface Contract

For example:

Ontology:
What is an Action?
Action Model:
How is an Action structured?
Action API:
How does an external system interact with an Action?

These are related but distinct.

⸻

17. Interface Stability

Interfaces should be more stable than implementation details.

An enterprise application should not need to understand:

which LLM was used
which embedding model was used
which internal resolver ran
which database stored the Intent

It should interact with canonical Noema concepts.

⸻

18. Internal Implementation Is Hidden

The interface boundary intentionally hides internal mechanisms.

External Consumer
       │
       ▼
Canonical Interface
       │
       ▼
┌───────────────────────────────┐
│ Internal Noema Implementation │
│                               │
│ Models                        │
│ Resolver                      │
│ Trust Engine                  │
│ Planner                       │
│ Execution Engine              │
└───────────────────────────────┘

Implementation can evolve without changing the semantic contract.

⸻

19. Interface Contracts

Every interface should explicitly define:

identity
inputs
outputs
states
errors
events
authorization
versioning
idempotency
timeouts

The exact requirements vary by interface.

⸻

20. State Is Explicit

Interfaces should expose canonical state rather than forcing consumers to infer it.

For example:

{
  "state": "CLARIFICATION_REQUIRED"
}

is preferable to requiring a consumer to infer state from:

{
  "clarification": null,
  "action": null,
  "execution": null
}

⸻

21. Interfaces Must Preserve Determinism

The underlying model may be probabilistic.

The interfaces must expose deterministic system states.

For example:

Model:
candidate = John Smith
confidence = 0.92
Trust / Resolution:
AMBIGUOUS
API:
state = CLARIFICATION_REQUIRED

The interface must not expose probabilistic interpretation as if it were a definitive execution decision.

⸻

22. Interface Boundaries and Trust

Interfaces must not become Trust bypasses.

For example, a caller must not be able to submit:

{
  "action": "transfer_money",
  "approved": true
}

and cause Noema to accept approved as authoritative.

Authorization and policy evaluation remain under the Trust domain.

⸻

23. Interface Boundaries and Execution

Likewise, receiving an Action through an API does not necessarily mean it can execute.

Action received
      ↓
Validation
      ↓
Trust
      ↓
Policy
      ↓
Execution

The interface is not the authority that determines whether the Action may execute.

⸻

24. API Commands

Commands crossing an interface represent requests.

Examples:

submit_intent
clarify_intent
cancel_intent
create_action
start_execution
retry_execution

Commands must be validated against the canonical state machine.

⸻

25. Events

Events crossing an interface represent facts.

Examples:

intent.resolved
execution.started
execution.completed
execution.failed

An event should not masquerade as a command.

⸻

26. External Events

External systems may produce events:

Bank
 ↓
"card_replacement.completed"
 ↓
Integration
 ↓
Canonical Event
 ↓
Noema

The Integration Model translates provider-specific events into canonical events or evidence.

⸻

27. Interface Versioning

Interfaces must support evolution without breaking consumers.

Conceptually:

Intent API v1
Intent API v2

However, versioning should not be used to create competing semantic definitions.

For example:

v1: Intent means X
v2: Intent means something completely different

would represent semantic fragmentation rather than healthy API evolution.

⸻

28. Backward Compatibility

Where possible:

Existing consumer
       ↓
Stable canonical contract
       ↓
New Noema implementation

The internal system should evolve behind the interface.

⸻

29. Idempotency

Interfaces that cause state transitions or external effects should support idempotency where appropriate.

For example:

POST /intents
Idempotency-Key: abc123

repeated requests should not unexpectedly create duplicate logical objects.

Execution APIs require particularly strong idempotency guarantees.

⸻

30. Correlation

Interfaces should support correlation across the complete journey.

intent_id
   ↓
action_id
   ↓
execution_id
   ↓
integration_id
   ↓
provider_request_id
   ↓
event_id

This allows an enterprise to trace:

what the user requested → what Noema understood → what it attempted → what happened externally.

⸻

31. Auditability

Interface interactions should produce sufficient information to reconstruct consequential decisions.

This includes:

who
what
when
through which interface
with which object
under which version
with which resulting state

Sensitive data should be handled according to security and privacy requirements.

⸻

32. Error Model

Interfaces should expose canonical errors where possible.

Examples:

INVALID_REQUEST
INVALID_STATE_TRANSITION
AMBIGUOUS_INTENT
CLARIFICATION_REQUIRED
UNAUTHORIZED
FORBIDDEN
UNSUPPORTED_CAPABILITY
CONFLICT
NOT_FOUND
EXECUTION_UNAVAILABLE

Provider-specific errors should remain available where useful but should not become the canonical error taxonomy.

⸻

33. Interface Errors vs Execution Failures

These are different.

API Error:
invalid request

means the interface request itself was invalid.

Whereas:

Execution Failure:
provider unavailable

means the request was valid but execution encountered a problem.

These must not be conflated.

⸻

34. Interface Security

Every interface must establish appropriate:

authentication
authorization
tenant isolation
input validation
data access controls
auditability

Security policy belongs to the broader Trust and enterprise security model.

⸻

35. Multi-Tenant Boundary

Noema interfaces should preserve tenant isolation.

Tenant A
   ↓
Noema
Tenant B
   ↓
Noema

Objects, context, executions, integrations, and events must not cross tenant boundaries unless explicitly authorized.

⸻

36. Human and Machine Consumers

The Interfaces layer should not assume that every consumer is human.

Consumers may include:

Human UI
AI Agent
Enterprise Backend
Workflow Engine
Mobile Application
CLI
Integration Service
Another Noema Instance

The canonical semantics remain the same.

⸻

37. Natural Language Is Not the Interface Contract

Natural language may be one input mechanism.

It should not define the canonical API schema.

Natural Language
       ↓
Intent API
       ↓
Canonical Intent

This allows Noema to support structured clients without forcing them through conversational interpretation.

The conversion from probabilistic natural-language input to a canonical Intent object is an internal concern of the Intent API. External consumers interact with canonical Intent state, not with intermediate model outputs.

⸻

38. Structured Clients

An enterprise application may submit:

{
  "goal": "replace_card",
  "target": {
    "type": "card",
    "id": "card_123"
  }
}

This can enter the same Intent model as:

"Please replace my card."

The input mechanism differs.

The canonical Intent does not.

⸻

39. Interfaces as Translation Boundaries

The Interfaces layer contains two broad classes of translation.

Inbound

External representation
        ↓
Canonical Noema representation

Outbound

Canonical Noema representation
        ↓
External representation

The translation must preserve semantics.

⸻

40. Lossless Where Necessary

For consequential operations, interface translation should preserve sufficient information to reconstruct:

original request
canonical interpretation
decision
execution
outcome

Information should not be discarded merely because a downstream API does not need it.

⸻

41. Noema Should Not Become an API Gateway

The Integration Model may connect many enterprise APIs.

But Noema is not fundamentally:

API Gateway

Its purpose is semantic orchestration around intent, trust, action, and execution.

The integration layer exists to serve that model.

⸻

42. Noema Should Not Become a Generic Workflow API

Likewise, Noema is not merely:

workflow engine

A workflow describes predetermined process logic.

Noema additionally handles:

human intent
ambiguity
context
trust
policy
dynamic action selection
execution uncertainty

⸻

43. Interface Composition

Interfaces may participate in a single lifecycle:

Intent API
    ↓
Context API (during resolution)
    ↓
Action API
    ↓
Trust API
    ↓
Execution API
    ↓
Integration Model
    ↓
Event Model

The interfaces therefore form a system rather than independent APIs.

⸻

44. Canonical Lifecycle Through Interfaces

                 USER / AGENT / SYSTEM
                      │
                      ▼
                ┌────────────┐
                │ Intent API │
                └─────┬──────┘
                      │
                      ▼
                   INTENT
                      │
              ┌───────┴───────┐
              │               │
              ▼               ▼
         Context API      Clarification
              │               │
              └───────┬───────┘
                      ▼
               RESOLVED INTENT
                      │
                      ▼
              EXECUTABLE INTENT
                      │
                      ▼
                ACTION API
                      │
                      ▼
                 TRUST API
                      │
              EXECUTE / CLARIFY
              ESCALATE / REJECT
                      │ (EXECUTE)
                      ▼
               EXECUTION API
                      │
                      ▼
              INTEGRATION MODEL
                      │
                      ▼
             ENTERPRISE SYSTEM
                      │
                      ▼
                EVENT MODEL
                      │
                      ▼
                  OUTCOME

⸻

45. Interface Ownership

Concern	Primary Owner
Intent semantics	Intent domain
Intent submission and lifecycle	Intent API
Context semantics (Grounding)	Ontology / Context domain
Context retrieval	Context API
Action semantics	Ontology / Action domain
Action representation	Action API
Trust evaluation	Trust API
Authorization	Trust
Policy evaluation	Trust
Execution semantics	Execution domain
Execution interaction	Execution API
External provider mapping	Integration Model
Event semantics	Event Model
External event translation	Integration Model

This prevents responsibility from leaking across boundaries.

⸻

46. Interface Invariants

Invariant 1

Interfaces expose canonical Noema semantics; they do not redefine them.

Invariant 2

Intent, Action, Trust, and Execution remain separate concepts across interfaces.

Invariant 3

No interface may bypass Trust to produce an executable side effect.

Invariant 4

Probabilistic model output must not be exposed as deterministic authorization.

Invariant 5

State transitions must obey canonical state machines.

Invariant 6

Commands and Events must remain distinguishable.

Invariant 7

External provider semantics must remain isolated behind integrations.

Invariant 8

Provider-specific failures must not become the canonical Noema failure model.

Invariant 9

Interfaces must preserve sufficient provenance for consequential decisions.

Invariant 10

Interface consumers should not need to know Noema’s internal implementation.

Invariant 11

Canonical objects must have stable identities across their lifecycle.

Invariant 12

Interfaces must support appropriate idempotency for consequential operations.

Invariant 13

Tenant and authorization boundaries must be enforced independently of client claims.

Invariant 14

Natural-language input and structured input must converge on the same canonical semantic model where they represent the same intent.

Invariant 15

Historical interface interactions must remain auditable.

⸻

47. The Boundary Principle

The entire Interfaces layer can be reduced to one principle:

External Systems
       │
       │  Interface
       ▼
Canonical Noema Semantics
       │
       │  Interface
       ▼
External Systems

The interface is a boundary of translation and enforcement, not a place where semantics become ambiguous.

⸻

48. Canonical Mental Model

                         NOEMA
┌────────────────────────────────────────────────────────────┐
│                                                            │
│                     CANONICAL CORE                         │
│                                                            │
│   Ontology → Intent → Trust → Execution → Outcome          │
│                                                            │
└──────────────────────────┬─────────────────────────────────┘
                           │
                           │
                    05 — INTERFACES
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Intent API         Context API        Action API
        │                  │                  │
        ├──────────────────┼──────────────────┤
        │                  │                  │
        ▼                  ▼                  ▼
   Trust API       Execution API     Event Model
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                  Integration Model
                           │
                           ▼
                  Enterprise Systems

⸻

49. What the Interfaces Layer Gives Noema

Without this layer, Noema has internal semantics but weak system boundaries.

With it, Noema becomes consumable as infrastructure.

It allows:

Application / Agent / Enterprise System
     ↓
Intent API
     ↓
Noema
     ↓
Enterprise Systems

without requiring every application to independently implement:

intent resolution
ambiguity handling
trust evaluation
action modeling
execution state
integration translation

That is a major part of Noema’s infrastructure proposition.

⸻

50. Final Definition

The Interfaces layer is the boundary through which Noema’s canonical semantic system communicates with humans, agents, applications, enterprise systems, and external providers. It exposes Intent, Context, Action, Trust, Execution, Event, and Integration semantics while preserving the separation between probabilistic interpretation, deterministic trust evaluation, authorization, execution, and external system behavior.

The central architectural rule is:

Interfaces translate between the outside world and Noema’s canonical model; they must never become a backdoor around that model.

And the complete boundary can be summarized as:

             EXTERNAL WORLD
                    │
                    ▼
              ┌───────────┐
              │ Interfaces│
              └─────┬─────┘
                    │
                    ▼
         ┌─────────────────────┐
         │    NOEMA CANON      │
         │                     │
         │ Intent              │
         │ Context             │
         │ Trust               │
         │ Action              │
         │ Execution           │
         │ Outcome             │
         └──────────┬──────────┘
                    │
                    ▼
             ENTERPRISE WORLD

The Interfaces layer is therefore the membrane of Noema: it lets intent, evidence, commands, events, and execution cross the boundary without allowing the semantics of either side to silently corrupt the other.

⸻

51. Deployment Modes

Noema interfaces support two architectural deployment modes.

Mode 1 — Full Stack

Noema operates the complete semantic pipeline from intent ingestion through execution. All canonical interfaces are active.

Intent API
    ↓
Intent → Resolution → Executable Intent
    ↓
Trust API
    ↓
Execution API
    ↓
Integration Model
    ↓
Enterprise Systems

Mode 2 — Independent Trust and Execution Boundary

An external agent or orchestrator manages user interaction and intent resolution. Noema serves as an independent trust and execution layer that evaluates proposed Actions before they reach enterprise systems.

External Agent / Orchestrator
    ↓
Action API  (submits resolved, executable Actions)
    ↓
Trust API
    ↓
Execution API
    ↓
Enterprise Systems

In Mode 2, the external system is responsible for intent resolution. Noema remains the authoritative Trust and Execution boundary. The Trust API and Action API are the critical entry points.

The interface layer must support both modes without assuming that Noema always owns the conversational or agent layer. No interface may silently bypass Trust merely because intent resolution occurred outside Noema.
