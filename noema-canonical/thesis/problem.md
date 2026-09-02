Problem

Status: Foundational
Version: 0.1
Domain: Thesis
Canonical Path: thesis/problem.md

⸻

1. The Problem

Software systems are increasingly capable of performing actions on behalf of humans.

APIs exist.
Business systems exist.
Automation exists.
AI models can understand natural language and invoke tools.

Yet there is still a fundamental gap between:

What a human means

and:

What a computer is allowed to do.

Today, that gap is typically bridged by application-specific code, rigid workflows, forms, prompts, tool definitions, and human interpretation.

These mechanisms work when intent is predictable.

They become fragile when intent is expressed dynamically, ambiguously, across multiple systems, and with consequential side effects.

Noema exists to address this gap.

⸻

2. The Core Problem

The core problem is not that computers cannot execute actions.

They execute actions extremely well.

The problem is that computers generally require intent to be translated into a sufficiently precise machine representation before execution.

Consider:

“Renew my company card.”

A human may consider this straightforward.

A computer needs to determine:

Who is "my"?
Which company?
Which card?
Is the card eligible for renewal?
What does "renew" mean in this system?
Which capability performs the renewal?
Does this Actor have authority?
What policies apply?
Are there constraints?
What is the current state?
What should happen if renewal requires approval?
How do we know the renewal actually succeeded?

The difficulty is therefore not merely execution.

It is semantic translation under uncertainty and authority constraints.

⸻

3. The Existing Abstraction Is Too Low-Level

Most software interfaces expose operations:

GET /customers/:id
POST /cards/:id/renew
DELETE /subscriptions/:id
POST /payments/:id/refund

These APIs describe how a system can be operated.

They do not necessarily describe:

What a human is trying to accomplish.

The distinction is:

API:
RenewCard(card_id)
Human:
"Make sure I have a valid company card when this one expires."

The second statement contains intent, context, temporal requirements, and potentially multiple valid execution paths.

Current systems generally force an application developer to manually bridge that semantic gap.

⸻

4. The AI Era Exposes the Problem

Large language models have significantly improved the ability of machines to interpret natural language.

A Model can infer that:

“Renew my company card.”

probably corresponds to something like:

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
* whether the Actor has authority
* whether the requested operation is permitted
* whether the current State allows it
* which Policy applies
* which Action should execute
* whether the resulting Outcome satisfies the Intent

This creates a new systems problem:

How do we turn probabilistic interpretation into deterministic, trustworthy execution?

⸻

5. Tool Calling Does Not Solve the Problem

Modern AI systems often address actionability through tool calling.

Conceptually:

User
 ↓
LLM
 ↓
Tool Selection
 ↓
Tool Call
 ↓
API

This solves one problem:

The Model can invoke software.

It does not solve the deeper problem:

Should this particular Action be executed given what the user actually intended and the surrounding constraints?

Tool descriptions do not constitute a canonical ontology.

A function schema does not establish authority.

A successful API response does not prove Intent satisfaction.

Model confidence does not establish Trust.

⸻

6. Prompts Are Not a Trust Boundary

A common approach is to encode rules into prompts:

You are an assistant.
Never delete accounts unless...
Only refund payments when...
Ask for clarification if...

This creates brittle, implicit semantics.

Critical business rules become dependent on:

* prompt construction
* Model behavior
* context windows
* instruction ordering
* Model version
* tool descriptions
* retrieval quality

This is unsuitable as the primary control plane for consequential execution.

The system needs explicit, machine-evaluable semantics outside the Model.

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

But a human may instead say:

“Take care of my expiring card.”

The system now needs to determine what “take care of” means in context.

This is fundamentally different from executing a predefined workflow.

⸻

8. Human Intent Is Richer Than Commands

Human requests frequently contain implicit information.

Consider:

“Get Sarah the same access John has.”

This contains multiple semantic dimensions:

Actor:
Current user
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
Whether current user may grant that access

A simple function call does not capture all of this.

The system needs a representation of the meaning behind the command.

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

Entity
Resource
Scope
Time
Authority
Policy
State
Parameters

A trustworthy system must treat ambiguity explicitly.

It cannot assume that the most probable interpretation is always acceptable.

⸻

10. Uncertainty Becomes Dangerous at the Execution Boundary

A mistaken answer in a conversational system may be inconvenient.

A mistaken Action can be consequential.

Examples:

Wrong account selected
Wrong customer deleted
Wrong payment refunded
Wrong employee granted access
Wrong deployment terminated
Wrong document published
Wrong funds transferred

The system therefore requires a different relationship with uncertainty.

For information retrieval:

uncertainty → lower confidence

For consequential execution:

uncertainty → clarification / denial / escalation

⸻

11. Permission Is Not Intent

Traditional authorization answers:

“Can this Actor perform this operation?”

Noema must also answer:

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
"Show me the customer's profile."

Alice may be authorized to delete the customer.

That does not make deletion the correct Action.

Therefore:

Authority ≠ Intent

Both must be established independently.

⸻

12. Capability Is Not Permission

Similarly:

Capability:
refund_payment

only establishes that an operation exists.

It does not establish:

Actor may perform it

or:

Policy permits it

or:

Current State allows it

The system needs to distinguish:

What can happen?

from:

What should happen?

and:

What may happen?

⸻

13. Successful Execution Does Not Prove Success of Intent

Suppose Noema executes:

RenewCard(card_123)

and receives:

HTTP 200 OK

That only establishes that the external system accepted the request.

It does not necessarily establish that:

Card is now active

or:

The requested renewal was actually completed

or:

The user's Intent has been satisfied.

Therefore:

Execution Success
        ≠
Intent Success

Outcome verification is part of the problem.

⸻

14. Systems Have Fragmented Semantics

Enterprise environments contain many systems:

CRM
ERP
HRIS
Payment Provider
Identity Provider
Ticketing System
Cloud Infrastructure
Databases
Internal Services

Each has its own:

* identifiers
* terminology
* APIs
* state models
* permissions
* business rules

A human sees:

"the customer"

while different systems may represent that customer as:

CRM Customer #392
Billing Account #8831
Support User #1049
Payment Customer cus_7...

The system therefore needs semantic resolution across boundaries.

⸻

15. Integration Complexity Is Not the Fundamental Problem

The problem is not simply:

“There are too many APIs.”

API integration tools already address much of that problem.

The deeper issue is:

Human Meaning
      ↓
?
      ↓
System-Specific Action

The missing layer is a canonical semantic representation of executable intent.

⸻

16. Business Logic Is Fragmented Across Applications

Today, intent interpretation is frequently distributed across:

frontend validation
backend services
API gateways
workflow engines
authorization middleware
prompt instructions
tool schemas
database constraints
human procedures

There is rarely a single canonical representation of:

What the Actor intends
What must be true
What is permitted
What Action should happen
What Outcome is expected

This makes systems difficult to reason about and difficult to compose.

⸻

17. The Missing Abstraction

The missing abstraction is not another API protocol.

It is a semantic layer between:

Human Intent

and:

Executable Action

That layer must be able to represent:

Actor
Intent
Entity
Resource
Capability
Context
State
Constraint
Policy
Authority
Action
Outcome

and establish the relationships between them.

⸻

18. The Desired Transformation

The system should transform:

Natural Language

into:

Canonical Intent

then:

Canonical Intent
        ↓
Resolution
        ↓
Validation
        ↓
Trust Decision
        ↓
Executable Action
        ↓
Outcome

The critical property is that the original natural-language request does not remain the implicit source of truth throughout execution.

⸻

19. The Problem in One Sentence

Software has powerful mechanisms for executing operations, and AI has become capable of interpreting human language, but there is no sufficiently general semantic and deterministic layer that reliably connects human intent to authorized, constrained, executable action.

⸻

20. The Problem Noema Specifically Addresses

Noema addresses the problem of trustworthy intent execution across heterogeneous software systems.

More precisely:

Given an Actor expressing an Intent in natural language or another human-facing interface, determine the canonical meaning of that Intent, resolve the relevant Resources and Context, establish applicable Capabilities, Policies, Constraints, and Authority, and produce an executable Action whose Outcome can be verified.

⸻

21. What Makes This a Systems Problem

This is not merely an AI problem.

It spans several layers:

                HUMAN
                  │
                  ▼
          Intent Expression
                  │
                  ▼
        Probabilistic Interpretation
                  │
                  ▼
          Semantic Resolution
                  │
                  ▼
          Canonical Representation
                  │
          ┌───────┼────────┐
          ▼       ▼        ▼
       Policy  Authority  State
          │       │        │
          └───────┼────────┘
                  ▼
           Deterministic Trust
                  │
                  ▼
               Action
                  │
                  ▼
             Execution
                  │
                  ▼
              Outcome

Each layer has different correctness requirements.

⸻

22. The Fundamental Tension

The problem can be expressed as a tension between two properties:

Human interaction wants flexibility.

Humans want to say:

“Take care of this for me.”

without specifying every implementation detail.

Software execution requires precision.

Software needs:

exact Actor
exact Resource
exact Capability
exact parameters
exact authority
exact constraints
exact Action

Noema exists in the space between those two requirements.

⸻

23. Why Existing Approaches Are Insufficient

Approach	What it solves	What remains unsolved
APIs	System execution	Human intent
Workflow engines	Predefined processes	Dynamic intent
RPA	UI automation	Semantic intent
Tool calling	Model → operation	Trust and meaning
Prompting	Model behavior	Deterministic enforcement
IAM	Permission	Intent correctness
Policy engines	Rule evaluation	Intent representation
RAG	Information retrieval	Action legitimacy
Knowledge graphs	Relationships	Executable intent
Agent frameworks	Autonomous behavior	Deterministic trust
Chat interfaces	Human interaction	Execution semantics

Noema is not intended to replace these technologies.

It provides the missing semantic boundary through which they can participate in trustworthy intent execution.

⸻

24. The First-Order Problem

The first-order problem is:

How can a machine reliably determine what a human intends to accomplish?

The second-order problem is:

How can that interpretation be converted into an Action without allowing probabilistic uncertainty to leak into consequential execution?

The third-order problem is:

How can the resulting Outcome be verified against the original Intent?

Noema must address all three.

⸻

25. The Problem Is Not “AI Cannot Understand Humans”

Modern Models can understand humans surprisingly well.

The problem is that understanding is not enough.

A Model can correctly infer:

“The user wants to renew their card.”

while Noema still needs to determine:

Which card?
Which Actor?
Is renewal available?
Is the Actor authorized?
What policy applies?
What constraints apply?
Which Action should execute?
What constitutes successful renewal?

The gap is therefore not merely language understanding.

It is operational semantics and trust.

⸻

26. The Problem Is Not Lack of Automation

Enterprises already automate enormous numbers of operations.

The problem is that automation is usually bound to:

predefined workflows
predefined triggers
predefined forms
predefined APIs
predefined rules

Noema targets the space where the desired operation is expressed dynamically through human Intent.

⸻

27. The Problem Is Not That Humans Need More Interfaces

Adding another UI does not solve the semantic problem.

Forms make humans translate Intent into system-specific fields.

Noema aims to reverse that relationship:

Traditional:
Human
 ↓
System-specific form
 ↓
Structured command
 ↓
Action

versus:

Noema:
Human
 ↓
Intent
 ↓
Canonical semantics
 ↓
Validated Action

⸻

28. The Fundamental Failure Mode

The failure Noema is designed to prevent is:

A system executes an Action that is technically valid but semantically wrong.

Examples:

Correct API call
Wrong customer
Correct permission
Wrong intent
Correct tool
Wrong resource
Correct workflow
Wrong context
Successful execution
Wrong outcome

These failures are particularly dangerous because the underlying software may report everything as successful.

⸻

29. The Desired Property

A trustworthy Noema execution should satisfy:

Action
⊆
Actor Authority
∩
Intent
∩
Capability
∩
Policy
∩
Constraints
∩
Current State
∩
Context

If the required intersection cannot be established, Noema should not silently proceed.

⸻

30. The Thesis

The thesis underlying Noema is:

Human intent should become a first-class computational object.

Once Intent becomes explicit, the system can reason about:

what was requested
who requested it
what it refers to
what is possible
what is permitted
what constraints apply
what Action should occur
what happened afterward

This creates a semantic execution layer between humans and software.

⸻

31. The Opportunity

The emergence of highly capable Models makes this layer newly practical.

Models can provide the probabilistic interface required to translate messy human language into candidate canonical Intent.

Noema can provide the deterministic substrate required to make that interpretation trustworthy.

Together:

Probabilistic Intelligence
          +
Canonical Semantics
          +
Deterministic Trust
          +
Executable Capabilities
          =
Trustworthy Intent Execution

That is the problem Noema exists to solve.