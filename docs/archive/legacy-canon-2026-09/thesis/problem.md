> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Problem

Status: Foundational
Version: 0.1
Domain: Thesis
Canonical Path: thesis/problem.md

⸻

1. The Problem

Software systems are increasingly capable of performing consequential actions on behalf of people, agents, and other systems.

APIs exist.
Business systems exist.
Automation exists.
AI Models can understand natural language and invoke tools.

Yet there remains a fundamental gap between:

What a source of intent means

and:

What a system is authorized and able to execute.

Today, that gap is typically bridged by application-specific code, rigid workflows, forms, prompts, tool definitions, policy logic, and human interpretation.

These mechanisms work well when intent is predictable and execution paths are known.

They become fragile when intent is expressed dynamically, ambiguously, across heterogeneous systems, and with consequential side effects.

Noema exists to address this gap.

⸻

2. The Core Problem

The core problem is not that computers cannot execute actions.

They execute actions extremely well.

The problem is that consequential execution requires intent to be translated into a sufficiently precise, validated, authorized, and contextually grounded machine representation before execution.

Consider:

“Renew my company card.”

A person may consider this straightforward.

A system needs to determine:

* Who is the Actor?
* Which company?
* Which card?
* What does “renew” mean in this enterprise context?
* Is the card eligible for renewal?
* Which Capability can satisfy the Intent?
* Which Action should be executed?
* Does the Actor have the required authority?
* What Policies apply?
* What Constraints apply?
* What is the current enterprise State?
* Is the required state sufficiently reconciled across systems?
* What should happen if clarification or approval is required?
* How will the resulting Outcome be verified?

The difficulty is therefore not merely execution.

It is semantic translation, resolution, governance, and verified execution under uncertainty.

⸻

3. The Existing Abstraction Is Too Low-Level

Most software interfaces expose operations:

GET /customers/:id
POST /cards/:id/renew
DELETE /subscriptions/:id
POST /payments/:id/refund

These APIs describe how a system can be operated.

They do not necessarily describe:

What a source of intent is trying to accomplish.

The distinction is:

API:
RenewCard(card_id)
Intent:
“Make sure I have a valid company card when this one expires.”

The second statement may contain intent, actor context, resource references, temporal requirements, constraints, and multiple valid execution paths.

Current systems generally force application developers to manually bridge this semantic gap.

⸻

4. The AI Era Exposes the Problem

Large language models have significantly improved the ability of machines to interpret natural language.

A Model may infer that:

“Renew my company card.”

corresponds to something like:

Intent:
RenewCard
Resource:
CompanyCard
Actor:
CurrentUser

But interpretation alone does not make the operation safe.

The Model may still be wrong about:

* which entity is being referenced
* which Resource is intended
* whether the Actor is correctly resolved
* whether the Actor has authority
* whether the requested operation is permitted
* whether the current State permits the operation
* which Policy applies
* which Capability can satisfy the Intent
* which Action should execute
* whether the resulting Outcome satisfies the original Intent

This creates a systems problem:

How do we turn probabilistic interpretation into deterministic, trustworthy execution?

⸻

5. Tool Calling Does Not Solve the Problem

Modern AI systems often address actionability through tool calling.

Conceptually:

Source of Intent
      ↓
Model
      ↓
Tool Selection
      ↓
Tool Call
      ↓
API

This solves one problem:

The Model can invoke software.

It does not solve the deeper problem:

Should this particular Action be executed given the resolved Intent, Actor, target, current State, authority, Policy, Constraints, and available evidence?

Tool descriptions do not constitute a canonical ontology.

A function schema does not establish authority.

A successful API response does not prove Intent satisfaction.

Model confidence does not establish Trust.

No free-form Model output should therefore be allowed to cross directly into consequential execution.

⸻

6. Prompts Are Not a Trust Boundary

A common approach is to encode rules into prompts:

You are an assistant.
Never delete accounts unless...
Only refund payments when...
Ask for clarification if...

This creates brittle, implicit semantics.

Critical execution constraints can become dependent on:

* prompt construction
* Model behavior
* context windows
* instruction ordering
* Model version
* tool descriptions
* retrieval quality

This is unsuitable as the primary control plane for consequential execution.

The system needs explicit, machine-evaluable semantics outside the Model, with a hard boundary between probabilistic interpretation and deterministic validation, Trust, and execution.

⸻

7. Existing Automation Assumes Known Intent

Traditional automation works well when the desired behavior is predefined.

For example:

WHEN invoice becomes overdue
    THEN send reminder

or:

WHEN card expires
    THEN issue replacement

The workflow is already known.

But a person or agent may instead express:

“Take care of my expiring card.”

The system now needs to determine what “take care of” means in context and whether a valid execution path exists.

This is fundamentally different from executing a predefined workflow.

⸻

8. Intent Is Richer Than Commands

Sources of intent frequently contain information that is not represented by a simple operation name and parameter list.

Consider:

“Get Sarah the same access John has.”

This contains multiple semantic dimensions:

Actor:
Current source of authority
Intent:
Grant access
Target:
Sarah
Reference:
John's existing access
Resource:
Access permissions
Context:
Relevant organization/system
Constraint:
Match John's access
Potential Policy:
Whether the Actor may grant that access

A simple function call does not capture all of this.

The system needs a representation of the meaning behind the request.

⸻

9. Ambiguity Is Normal

Natural language is inherently ambiguous.

Examples:

“Cancel the old subscription.”

“Send the report to the team.”

“Move the money to savings.”

“Delete the inactive users.”

“Give James access.”

Each request may require resolution of:

* Actor
* Entity
* Resource
* Scope
* Time
* Target
* Authority
* Policy
* State
* Parameters

A trustworthy system must treat material ambiguity explicitly.

It cannot assume that the most probable interpretation is always acceptable.

When ambiguity materially affects consequential execution, the correct outcome may be CLARIFY rather than inference.

⸻

10. Uncertainty Becomes Dangerous at the Execution Boundary

A mistaken answer in a conversational system may be inconvenient.

A mistaken Action can be consequential.

Examples include:

* wrong account selected
* wrong customer deleted
* wrong payment refunded
* wrong employee granted access
* wrong deployment terminated
* wrong document published
* wrong funds transferred

The system therefore requires a different relationship with uncertainty.

For information retrieval:

uncertainty → lower confidence

For consequential execution:

material uncertainty
        ↓
clarification / rejection / escalation

And when the execution state itself is uncertain:

uncertain execution
        ↓
verification / reconciliation
        ↓
retry only when safe

Timeout or lack of response must not automatically be interpreted as failure.

⸻

11. Intent and Authorization Are Distinct

Traditional authorization asks:

“Can this Actor perform this operation?”

Noema must also establish:

“Is this the operation the Actor actually intended?”

These are different questions.

For example:

Actor:
Alice
Capability:
DeleteCustomer
Authority:
Alice is allowed to delete customers.
Intent:
“Show me the customer's profile.”

Alice may be authorized to delete the customer.

That does not make deletion the correct Action.

Therefore:

Authority ≠ Intent

Both must be established independently.

Authorization must also be evaluated against a sufficiently resolved:

Actor
+
Action
+
Target / Resource
+
Context / Current State
+
Applicable Policy

Noema does not replace the enterprise as the authority source for business permissions or enterprise state. It provides the deterministic evaluation boundary through which those supplied authorities and governance conditions can be applied.

⸻

12. Capability Is Not Permission

Similarly:

Capability:
refund_payment

only establishes that an operation is possible through the connected enterprise environment.

It does not establish:

* that the Actor may perform it
* that the current request authorizes it
* that Policy permits it
* that the current State allows it
* that executing it is consistent with the resolved Intent

The system must distinguish:

What can happen?
        ↓
Capability
What is authorized?
        ↓
Authorization
What conditions govern it?
        ↓
Policy
What should happen?
        ↓
Intent + Action semantics

⸻

13. Successful Execution Does Not Prove Intent Satisfaction

Suppose Noema executes:

RenewCard(card_123)

and receives:

HTTP 200 OK

That establishes something about the external request.

It does not necessarily establish that:

* the renewal completed
* the card is now active
* the intended card was renewed
* the expected enterprise state was reached
* the original Intent was satisfied

Therefore:

Execution Success
        ≠
Intent Satisfaction

Outcome verification is part of the execution problem.

Completion requires sufficient evidence that the expected Outcome has actually been established.

⸻

14. Systems Have Fragmented Semantics

Enterprise environments contain many systems:

* CRM
* ERP
* HRIS
* Payment Provider
* Identity Provider
* Ticketing System
* Cloud Infrastructure
* Databases
* Internal Services

Each may have its own:

* identifiers
* terminology
* APIs
* state models
* permissions
* business rules

A person may see:

“the customer”

while different systems represent that customer as:

CRM Customer #392
Billing Account #8831
Support User #1049
Payment Customer cus_7...

The system therefore needs semantic resolution across boundaries.

It also needs to distinguish:

* source of information
* authority of information
* freshness
* temporal applicability
* contradictory observations

Retrieving a value from a system does not automatically make that value authoritative.

⸻

15. Integration Complexity Is Not the Fundamental Problem

The problem is not simply:

“There are too many APIs.”

API integration tools already address much of that problem.

The deeper issue is:

Intent
  ↓
?
  ↓
System-Specific Action

The missing layer is a canonical semantic representation of executable Intent and its relationship to Context, Capabilities, Authority, Policy, State, Action, Execution, Evidence, and Outcome.

Integration remains necessary, but it is not itself the fundamental abstraction Noema introduces.

⸻

16. Business Logic Is Fragmented Across Applications

Today, intent interpretation and execution governance may be distributed across:

* frontend validation
* backend services
* API gateways
* workflow engines
* authorization middleware
* prompt instructions
* tool schemas
* database constraints
* human procedures

There is rarely a single canonical representation connecting:

What was intended
        ↓
What was resolved
        ↓
What is possible
        ↓
What is authorized
        ↓
What conditions apply
        ↓
What Action should occur
        ↓
What was attempted
        ↓
What Outcome was established

This makes systems difficult to reason about, compose, audit, and recover.

⸻

17. The Missing Abstraction

The missing abstraction is not another API protocol.

It is a semantic and governance layer between:

Source of Intent

and:

Executable Action

That layer must be able to represent and relate:

* Actor
* Intent
* Entity
* Resource
* Context
* Capability
* Authorization
* Policy
* Constraint
* State
* Evidence
* Action
* Execution
* Outcome

It must also preserve uncertainty rather than forcing unresolved information into false certainty.

⸻

18. The Desired Transformation

The system should transform:

Source of Intent
        ↓
Intent Compilation
        ↓
Hard Schema Validation
        ↓
Context
        ↓
State Reconciliation
        ↓
Deterministic Trust
        ↓
Action Graph / Outcome Graph
        ↓
Planning
        ↓
Execution
        ↓
Verification / Recovery
        ↓
Outcome

Natural language is an interface to this process, not its canonical representation.

The original request must not remain the implicit source of truth throughout execution.

Once an Intent Object is admitted to Trust, it is typed, schema-validated, versioned, and immutable. Changes to intent create a new version rather than silently mutating the admitted object.

⸻

19. The Problem in One Sentence

Software has powerful mechanisms for executing operations, and AI has become capable of interpreting human language, but there is no sufficiently general semantic and deterministic layer that reliably connects a source of intent to resolved, authorized, constrained, executable action and a verifiable outcome across heterogeneous enterprise systems.

⸻

20. The Problem Noema Specifically Addresses

Noema addresses the problem of trustworthy intent execution across heterogeneous enterprise systems.

More precisely:

Given a source of intent from a person, AI agent, system, voice interface, text interface, chat interface, WhatsApp interaction, API, or other supported source, determine the canonical meaning of that Intent, resolve the relevant Actor, Entities, Resources, and Context, reconcile relevant State, establish applicable Capabilities, Policies, Constraints, and Authority, and produce a governed executable Action whose resulting Outcome can be verified and recovered when necessary.

Noema does not become the enterprise system of record for the underlying business domain.

Enterprise systems remain authoritative for business state, while Noema owns the semantic and execution state required to govern the transition from intent to outcome.

⸻

21. What Makes This a Systems Problem

This is not merely an AI problem.

It spans several layers:

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
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Authority    Policy     Constraints
          │          │          │
          └──────────┼──────────┘
                     ▼
             Action / Outcome
                  Graphs
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

Each layer has different correctness requirements.

The critical architectural boundary is:

PROBABILISTIC
understand / interpret / propose
              │
              │ HARD BOUNDARY
              ▼
DETERMINISTIC
validate / resolve / reconcile / govern /
plan / execute / verify / recover / audit

⸻

22. The Fundamental Tension

The problem can be expressed as a tension between two properties.

Human and agent-facing interaction wants flexibility.

A source of intent should be able to express:

“Take care of this for me.”

without specifying every implementation detail.

Software execution requires precision.

The execution system needs sufficiently resolved:

* Actor
* Intent
* Target
* Capability
* Action
* Authority
* Policy
* Constraints
* Context
* Current State

Noema exists in the space between those two requirements.

Its purpose is not to eliminate ambiguity by guessing.

Its purpose is to make ambiguity, uncertainty, authority, and execution state explicit and governable.

⸻

23. Why Existing Approaches Are Insufficient

Approach	What it solves	What remains unsolved
APIs	System execution	Intent semantics and governance
Workflow engines	Predefined processes	Dynamic intent and semantic resolution
RPA	UI automation	Canonical intent and trustworthy execution
Tool calling	Model → operation	Deterministic trust and intent correctness
Prompting	Model behavior	Deterministic enforcement
IAM	Permission	Intent correctness and execution semantics
Policy engines	Rule evaluation	Canonical intent and execution lifecycle
RAG	Information retrieval	Action legitimacy and authority
Knowledge graphs	Relationships	Governed executable intent
Agent frameworks	Agent behavior	Deterministic execution boundary
Chat interfaces	Human interaction	Execution semantics and verification

Noema is not intended to replace these technologies.

It provides a semantic and trust boundary through which they can participate in trustworthy intent execution.

⸻

24. The First-Order Problem

The first-order problem is:

How can a machine reliably determine what a source of intent means and resolve the relevant entities, resources, actor, and context?

The second-order problem is:

How can that interpretation be converted into an Action without allowing probabilistic uncertainty to leak into consequential execution?

The third-order problem is:

How can the resulting Outcome be verified against the original Intent and recovered safely when execution state is uncertain or partially failed?

Noema must address all three.

⸻

25. The Problem Is Not “AI Cannot Understand Humans”

Modern Models can understand humans surprisingly well.

The problem is that understanding is not enough.

A Model can correctly infer:

“The user wants to renew their card.”

while Noema still needs to determine:

* Which Actor?
* Which card?
* Which enterprise Resource?
* Is renewal available?
* Is the Actor authorized?
* What Policy applies?
* What Constraints apply?
* What is the current State?
* Which Capability can satisfy the Intent?
* Which Action should execute?
* What constitutes successful renewal?

The gap is therefore not merely language understanding.

It is operational semantics, governance, and verified execution.

⸻

26. The Problem Is Not Lack of Automation

Enterprises already automate enormous numbers of operations.

The problem is that automation is usually bound to:

* predefined workflows
* predefined triggers
* predefined forms
* predefined APIs
* predefined rules

Noema targets the space where the desired operation is expressed dynamically and must be resolved into a governed execution path.

This does not make predefined workflows obsolete. They can remain execution mechanisms within a Noema-governed path.

⸻

27. The Problem Is Not That People Need More Interfaces

Adding another UI does not solve the semantic problem.

Forms make people translate intent into system-specific fields.

Noema aims to reverse that relationship:

Traditional:
Source of Intent
      ↓
System-specific form
      ↓
Structured command
      ↓
Action

versus:

Noema:
Source of Intent
      ↓
Canonical Intent
      ↓
Resolution / Validation
      ↓
Governed Action

The interface may be voice, text, chat, WhatsApp, API, or another source. The canonical semantic representation remains the same.

⸻

28. The Fundamental Failure Mode

The failure Noema is designed to prevent is:

A system executes an Action that is technically valid but semantically, contextually, or authoritatively wrong.

Examples:

Correct API call
Wrong customer
Correct permission
Wrong Intent
Correct tool
Wrong Resource
Correct workflow
Wrong Context
Successful execution
Wrong or unverified Outcome

These failures are particularly dangerous because the underlying software may report everything as technically successful.

⸻

29. The Desired Property

A governed Noema execution should satisfy:

Action
⊆
Resolved Intent
∩
Resolved Actor Authority
∩
Available Capability
∩
Applicable Policy
∩
Applicable Constraints
∩
Current Reconciled State
∩
Relevant Context

This is not a literal set operation. It expresses the requirement that an Action must be justified simultaneously by the resolved semantic, authority, capability, governance, state, and contextual conditions.

If a required condition cannot be established with sufficient certainty, Noema must not silently proceed.

The canonical Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

Execution control may additionally require states such as waiting, confirmation, or unknown execution state, but these do not replace the canonical Trust outcomes.

⸻

30. The Thesis

The thesis underlying Noema is:

Intent should become a first-class computational object.

Once Intent becomes explicit and canonical, the system can reason about:

* what was requested
* who or what initiated it
* what it refers to
* what was resolved
* what is possible
* what is authorized
* what constraints apply
* what Action should occur
* what was attempted
* what evidence exists
* what Outcome was established

This creates a semantic and deterministic execution layer between sources of intent and enterprise software.

⸻

31. The Opportunity

The emergence of highly capable Models makes this layer newly practical.

Models can provide the probabilistic interpretation and candidate-generation capabilities required to translate messy source input into candidate canonical Intent.

Noema can provide the deterministic substrate required to validate, resolve, govern, execute, verify, and recover from that interpretation.

Together:

Probabilistic Intelligence
          +
Canonical Semantics
          +
Deterministic Trust
          +
Executable Capabilities
          +
Verification / Recovery
          =
Trustworthy Intent Execution

The commercial opportunity is to provide this capability as Trusted Enterprise Execution Infrastructure: an embedded execution boundary that enterprises can integrate into their own products so their users and customers can express intent and receive governed outcomes across existing enterprise systems.

That is the problem Noema exists to solve.