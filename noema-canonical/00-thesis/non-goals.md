Absolutely. 00-thesis/non-goals.md should be unusually explicit. For Noema, this file is important because the vision is broad enough that the project could easily drift into “AI agent platform,” “workflow engine,” “RPA,” “copilot,” or “universal enterprise operating system.”

The purpose of this document is to establish what Noema deliberately refuses to become.

Non-Goals

Status: Foundational
Version: 0.1
Domain: Thesis
Canonical Path: 00-thesis/non-goals.md

⸻

1. Purpose

This document defines what Noema is not intended to build, own, or become.

Noema’s vision is intentionally broad: a system for converting human intent into trustworthy, executable operations across software systems.

Without explicit boundaries, that vision can expand indefinitely.

These non-goals therefore act as architectural and product constraints.

A proposed feature, abstraction, or integration should be questioned against these boundaries before becoming part of Noema’s core.

⸻

2. Noema Is Not a General-Purpose AI Assistant

Noema is not intended to become another general-purpose conversational AI assistant.

It does not primarily exist to:

answer questions
generate prose
summarize documents
write poems
brainstorm ideas
chat socially
generate arbitrary content

Those capabilities may be useful at the interface layer, but they are not Noema’s core product.

Noema’s core concern is:

Turning human intent into trustworthy action.

⸻

3. Noema Is Not a Foundation Model

Noema does not intend to train or own a general-purpose foundation model.

The Model is an inference component within Noema.

The architecture must therefore remain model-agnostic.

Conceptually:

User
  ↓
Noema
  ↓
Model
  ↓
Candidate Interpretation
  ↓
Noema

The Model proposes.

Noema determines what can be trusted and executed.

⸻

4. Noema Is Not an AI Agent Framework

Noema is not primarily a framework for creating autonomous agents.

An agent framework generally focuses on concepts such as:

agents
tools
memory
planning
loops
reasoning
delegation
autonomy

Noema may use some of these mechanisms internally.

They are not the fundamental abstraction.

Noema’s fundamental abstraction is:

Intent

and the deterministic process by which that Intent becomes an authorized Action.

⸻

5. Noema Is Not an Autonomous Agent

Noema should not be defined by the principle:

“Let the AI figure out what to do.”

Instead:

Let the AI propose an interpretation, then let Noema establish what may actually be done.

The system must be capable of stopping.

Interpretation
     ↓
Insufficient certainty
     ↓
Clarification

rather than:

Insufficient certainty
     ↓
Best guess
     ↓
Execute

⸻

6. Noema Is Not an RPA Platform

Noema is not a traditional Robotic Process Automation system.

RPA generally automates predefined interaction sequences such as:

open application
click button
enter value
download file
copy value
paste value

Noema should operate at a higher semantic level.

Instead of:

Click → Fill → Submit

Noema represents:

Intent
→ Capability
→ Action
→ Resource
→ Policy
→ Authority
→ Outcome

The implementation may eventually drive UI automation where necessary, but UI automation is not the semantic foundation.

⸻

7. Noema Is Not a Workflow Engine

Noema is not intended to replace workflow engines such as systems built around:

DAGs
state machines
scheduled jobs
durable workflows
business process definitions

A workflow engine answers:

What sequence of predefined operations should execute?

Noema answers:

What does this human intend, and what executable operation is legitimately authorized by that intent?

Noema may invoke or integrate with workflow engines.

It should not absorb their responsibilities unnecessarily.

⸻

8. Noema Is Not a Business Process Database

Noema does not own the complete business state of every connected system.

This is a foundational boundary.

Noema owns:
Intent State
Trust State
Execution State
Semantic State

The connected business system owns:

Account State
Payment State
Order State
Customer State
Inventory State
Employee State

Therefore:

Noema owns intent state, not business state.

Noema may reference, resolve, validate, and act upon external business state.

It should not become the authoritative system of record for that state.

⸻

9. Noema Is Not an ERP

Noema does not intend to become a replacement for:

CRM
ERP
HRIS
Accounting systems
Payment systems
Inventory systems
Ticketing systems

Those systems own domain-specific business state.

Noema operates across them.

⸻

10. Noema Is Not a System of Record

Noema should not become the canonical source of truth for external domain entities merely because it interacts with them.

For example:

Bank
  owns → Account
CRM
  owns → Customer
Payment Provider
  owns → Payment
HRIS
  owns → Employee

Noema may maintain references, snapshots, observations, and provenance.

But it should not silently assume ownership of the underlying entity.

⸻

11. Noema Is Not an Integration Marketplace

Integrations are necessary infrastructure.

They are not the product thesis.

Noema should not become primarily:

"Connect 10,000 apps."

The number of connectors is not the core measure of Noema’s value.

The important abstraction is:

Intent
     ↓
Canonical Interpretation
     ↓
Executable Action
     ↓
Trust
     ↓
External System

⸻

12. Noema Is Not an API Gateway

Noema does not replace:

API Gateway
Service Mesh
Reverse Proxy
Load Balancer
Integration Gateway

Noema may sit above these systems.

It determines why and whether an operation should happen, rather than merely routing traffic.

⸻

13. Noema Is Not an Orchestration Platform by Default

Noema may orchestrate multiple Actions when required by an Intent.

However, orchestration itself is not the foundational abstraction.

For example:

Intent:
"Renew my company card."

may require:

Check eligibility
→ Create renewal
→ Update billing
→ Notify user

Noema may coordinate these operations.

But the canonical object remains the Intent and its resulting Outcome—not the orchestration graph itself.

⸻

14. Noema Is Not a Prompt Engineering Framework

Noema should not depend on increasingly elaborate prompts as its primary correctness mechanism.

This:

SYSTEM PROMPT
+
50 RULES
+
TOOL DESCRIPTIONS
+
EXAMPLES
=
HOPE

is not the Trust architecture.

Instead:

Natural Language
      ↓
Semantic Interpretation
      ↓
Canonical Ontology
      ↓
Deterministic Validation
      ↓
Trust
      ↓
Execution

Prompting may assist interpretation.

It must not substitute for canonical semantics and deterministic controls.

⸻

15. Noema Is Not a Tool-Calling Wrapper

Simply giving a Model tools does not constitute Noema.

This architecture:

User
 ↓
LLM
 ↓
Tool Call
 ↓
API

is insufficient.

Noema requires explicit semantics around:

Actor
Intent
Capability
Resource
Context
Constraint
Policy
Authority
Action
Outcome
State

The tool call is merely an execution mechanism.

⸻

16. Noema Is Not a Chat Interface

Chat is one possible interface.

It is not the product boundary.

Noema should eventually support intent originating from:

Chat
Voice
UI
API
Events
Forms
Applications
Agents
Automated systems

The canonical representation must remain interface-independent.

⸻

17. Noema Is Not UI Generation

Noema may eventually generate or manipulate interfaces.

That is not its foundational purpose.

The important distinction is:

UI
 ↓
Intent

rather than:

Intent
 ↓
UI

UI is one possible representation or interaction mechanism.

Intent is the canonical abstraction.

⸻

18. Noema Is Not a Design System

Noema does not define:

buttons
cards
colors
typography
layouts
navigation
component libraries

These belong to consuming applications.

Noema should expose semantic capabilities and executable operations, not prescribe visual design.

⸻

19. Noema Is Not a Knowledge Graph Product

Noema may require a semantic graph.

However, the graph is infrastructure for representing canonical meaning.

The product is not:

“A better enterprise knowledge graph.”

The graph exists to support:

intent understanding
entity resolution
relationship resolution
policy evaluation
capability discovery
action validation
trust decisions

⸻

20. Noema Is Not a Search Engine

Noema may need retrieval.

It may use:

vector search
keyword search
graph traversal
structured queries
semantic retrieval

But retrieval is not the end goal.

Search answers:

What information can I retrieve?

Noema answers:

What does the user intend, and what can legitimately happen because of it?

⸻

21. Noema Is Not RAG

Retrieval-Augmented Generation can be part of Noema’s implementation.

It is not the architecture itself.

RAG helps retrieve information.

Noema must establish:

what the information means
whether it is authoritative
whether it applies
whether it permits an Action
whether the resulting Action is safe

Therefore:

RAG ≠ Trust
RAG ≠ Intent
RAG ≠ Authorization
RAG ≠ Execution

⸻

22. Noema Is Not a Policy Engine Alone

Noema may contain or integrate with a policy engine.

But Policy is only one component of the decision.

A valid execution may depend on:

Intent
Actor
Resource
Capability
Context
State
Policy
Constraint
Authority
Evidence

Therefore Noema is not merely:

if policy then allow

⸻

23. Noema Is Not an Authorization System

Traditional authorization asks:

Is Actor X allowed to perform Operation Y?

Noema must answer a larger question:

Given what this Actor intended, the Resources involved, the current Context and State, the applicable Policies and Constraints, and the available Authority, is this specific Action legitimate to execute?

Noema may integrate with existing authorization systems.

It should not casually replace them.

⸻

24. Noema Is Not a Security Product

Security is a foundational requirement.

It is not sufficient to define the product.

Noema should not attempt to become a replacement for:

IAM
SIEM
EDR
DLP
WAF
Secrets Management
Security Operations

Security controls may constrain execution, but Noema’s core problem remains intent-to-action correctness.

⸻

25. Noema Is Not a Human Replacement

Noema is not designed around the assumption:

“Remove humans from every workflow.”

Its purpose is to make human intent executable with less friction while preserving appropriate human control.

For consequential ambiguity:

Noema asks.

For insufficient authority:

Noema stops.

For uncertain interpretation:

Noema clarifies.

For prohibited operations:

Noema refuses.

Autonomy is subordinate to correctness.

⸻

26. Noema Is Not “Do Whatever the User Says”

Natural-language instructions are not automatically executable commands.

For example:

“Delete the old customer accounts.”

Noema must resolve:

Which customers?
What qualifies as old?
Does the Actor have authority?
Which system owns the accounts?
Is deletion permitted?
Are there retention requirements?
What Resources are affected?
What Policy applies?

The Model’s interpretation is not sufficient.

⸻

27. Noema Is Not a Guessing Engine

When canonical information is insufficient, Noema should not fabricate certainty.

The preferred progression is:

Known
  ↓
Resolvable
  ↓
Ambiguous
  ↓
Clarify

not:

Unknown
  ↓
Guess
  ↓
Execute

This is a foundational Trust principle.

⸻

28. Noema Is Not Responsible for Every Business Rule

Business systems remain responsible for domain-specific invariants that belong to them.

For example:

Bank:
ledger correctness
Inventory system:
stock accounting
Payment provider:
payment settlement
HRIS:
employment records

Noema may consume these rules or evaluate relevant constraints.

It should not duplicate every domain’s complete business logic.

⸻

29. Noema Is Not a Distributed Transaction Manager

Noema may coordinate Actions across multiple systems.

It should not automatically assume responsibility for implementing global ACID semantics across arbitrary external systems.

Where transactional guarantees are unavailable, Noema must model:

partial success
failure
compensation
retry
reconciliation

rather than pretending distributed atomicity exists.

⸻

30. Noema Is Not an Event Bus

Noema may consume and emit events.

It is not intended to replace:

Kafka
NATS
RabbitMQ
SQS
Pulsar

Events are mechanisms for communicating State changes and execution information.

They are not the core semantic model.

⸻

31. Noema Is Not a Job Queue

Noema may execute asynchronous Actions.

It is not a replacement for a generic job queue.

A job queue answers:

When and how should this task execute?

Noema answers:

Why should this Action exist, what does it mean, and is it legitimate to execute?

⸻

32. Noema Is Not a Scheduler

Scheduling may be required for certain Intents.

Example:

“Remind me to renew this tomorrow.”

But scheduling is an execution concern.

It does not define Noema’s fundamental semantics.

⸻

33. Noema Is Not an Autonomous Planning System

Planning can be useful.

But Noema should not optimize for:

maximum autonomy
maximum task completion
minimum human intervention

at the expense of semantic correctness.

The system should prefer:

correct clarification

over:

incorrect completion

⸻

34. Noema Is Not a Replacement for Domain Expertise

Noema provides a semantic execution layer.

It does not magically understand every organization’s business.

Organizations must still define:

Entities
Capabilities
Policies
Constraints
Authorities
Resources
Actions
Outcomes

Noema provides the language and execution boundary for representing these concepts.

⸻

35. Noema Is Not a Universal Ontology of Everything

The canonical ontology should be intentionally minimal.

Noema does not need to model every concept in every domain.

It needs a stable set of primitives capable of representing executable human intent.

The ontology should expand only when a concept is necessary to express or validate meaningful execution semantics.

⸻

36. Noema Is Not a Business Logic Dumping Ground

Every new business rule should not automatically become a Noema primitive.

The canonical architecture should preserve separation between:

Noema semantics

and:

Domain semantics

Noema provides the language through which domain semantics become executable.

It does not absorb every domain implementation detail.

⸻

37. Noema Is Not a Replacement for Existing Systems

Noema should generally sit above and across existing systems rather than requiring organizations to replace them.

Conceptually:

                    Noema
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
         CRM         ERP         Payments
          │           │           │
          ▼           ▼           ▼
       Business    Business    Business
        State       State       State

Noema provides the semantic execution layer connecting intent to those systems.

⸻

38. Noema Is Not Another “AI Wrapper”

The product must not reduce to:

LLM
+
Prompt
+
Tools
+
Dashboard

If the core intellectual property can be removed and replaced by a generic tool-calling framework without materially changing the architecture, Noema has failed to establish its intended abstraction.

The differentiator must be the semantic and deterministic intent execution layer.

⸻

39. Noema Is Not Defined by Its Model

The underlying Model may change.

GPT
Claude
Gemini
Llama
Qwen
Future Model

Noema should remain conceptually intact.

The Model is replaceable infrastructure.

The canonical ontology, intent representation, trust boundary, and execution semantics are the durable architecture.

⸻

40. Noema Is Not Defined by Its Transport

Noema may eventually operate through:

REST
GraphQL
gRPC
MCP
Webhooks
Events
SDKs
UI
Voice

Transport is not the semantic layer.

A different transport must not require redefining Intent.

⸻

41. Noema Is Not Defined by Its Storage Technology

Noema may use:

PostgreSQL
Neo4j
Redis
Vector databases
Object storage
Search indexes

These are implementation choices.

The canonical model must remain independent of the persistence technology.

⸻

42. Noema Is Not “AI That Acts”

That phrase is too broad to be a sufficient definition.

The critical distinction is:

AI that acts

versus:

A system that determines whether an intended Action
is semantically valid, authorized, constrained, and trustworthy
before allowing execution.

The latter is the Noema thesis.

⸻

43. Architectural Test

When evaluating a proposed feature, ask:

Does this improve Noema’s ability to:

understand Intent?
resolve canonical meaning?
identify Actors?
identify Resources?
identify Capabilities?
evaluate Context?
apply Constraints?
apply Policy?
verify Authority?
determine Trust?
execute Actions?
verify Outcomes?

If not, it probably does not belong in Noema’s core.

⸻

44. Product Boundary

The simplest boundary is:

                 NOEMA
┌─────────────────────────────────────┐
│                                     │
│ Intent Understanding                │
│ Semantic Resolution                 │
│ Canonical Representation            │
│ Trust Evaluation                    │
│ Action Authorization                │
│ Execution Coordination              │
│ Outcome Verification                │
│                                     │
└─────────────────────────────────────┘
                 │
                 ▼
        External Systems

Noema owns the semantic boundary between human intent and executable action.

External systems continue to own their business domains.

⸻

45. Canonical Principle

Noema does not exist to replace every system that performs work. It exists to provide the semantic and trust boundary through which human intent becomes legitimate, executable action.

Therefore:

Noema does not own every system.
Noema does not own every workflow.
Noema does not own every policy.
Noema does not own every business rule.
Noema does not own every model.
Noema does not own every interface.
Noema owns the intent-to-action boundary.

That is the boundary the rest of the canonical documentation should preserve.