Principles

Status: Foundational
Version: 0.1
Domain: Thesis
Canonical Path: thesis/principles.md

⸻

1. Purpose

This document defines the principles that govern the design, architecture, and evolution of Noema.

These are not implementation preferences.

They are the invariants behind the system.

When architectural decisions conflict, these principles should be used to determine which direction is consistent with the Noema thesis.

⸻

2. Intent Is the Primary Abstraction

Noema is fundamentally an Intent system.

The central question is not:

What tool should the Model call?

It is:

What does the Actor intend to accomplish?

The system therefore begins with:

Actor
  ↓
Intent

rather than:

Actor
  ↓
Tool Call

Tools and Actions are implementation mechanisms downstream of Intent.

⸻

3. Intent Must Be Separated From Execution

An Intent is not an Action.

Intent:
"Renew my card."
Action:
RenewCard(...)

The same Intent may be fulfilled through different Actions depending on:

* Capability
* Resource
* Context
* Policy
* Constraint
* Authority
* State

Therefore:

Intent describes desired meaning; Action describes executable behavior.

⸻

4. The Model May Interpret, but Noema Must Decide

The Model is probabilistic.

Noema’s execution boundary must be deterministic wherever correctness requires determinism.

Model
  ↓
Candidate Interpretation
  ↓
Noema
  ↓
Validation
  ↓
Trust Decision
  ↓
Action

The Model should never be treated as the final authority merely because it produced a confident answer.

⸻

5. Uncertainty Must Resolve to Clarification

When Noema cannot establish the required meaning with sufficient certainty, it must not silently guess.

Uncertain
   ↓
Clarify

not:

Uncertain
   ↓
Best Guess
   ↓
Execute

This principle applies to:

* Actor identity
* Intent
* Resource
* Entity
* Capability
* Authority
* Policy applicability
* State
* Action parameters

⸻

6. Noema Owns Intent State, Not Business State

Noema should maintain the state required to understand and execute Intent.

It should not become the authoritative owner of external business state.

Noema:
Intent State
Trust State
Execution State
Outcome State

External systems:

CRM:
Customer State
Bank:
Account State
ERP:
Order State
HRIS:
Employee State

Noema may observe and act upon these states.

It does not automatically own them.

⸻

7. Canonical Meaning Must Be Explicit

Important concepts must have canonical representations.

Natural language:

"my card"

must eventually resolve to something like:

Resource:
Card#123

Likewise:

"renew it"

must resolve to:

Intent:
RenewCard
Target:
Card#123

Noema should not depend on implicit meaning buried inside prompts.

⸻

8. Ontology Before Automation

Noema should establish what a concept means before optimizing how it is executed.

The foundational vocabulary includes:

Actor
Intent
Entity
Resource
Capability
Action
Outcome
State
Context
Constraint
Policy
Authority
Relationship

Automation built on ambiguous semantics produces fragile systems.

⸻

9. Semantics Before Syntax

Noema should care more about:

what an operation means

than:

how the operation is represented.

For example:

REST
GraphQL
gRPC
MCP
SDK
CLI

may all represent the same semantic Action.

The canonical model should remain transport-independent.

⸻

10. Actions Must Have Explicit Semantics

An Action should not merely be:

function call

It should describe a meaningful operation against canonical domain objects.

Conceptually:

Action
├── capability
├── actor
├── resource
├── parameters
├── preconditions
├── constraints
├── authority
└── expected outcome

⸻

11. Capability Describes Possibility

A Capability answers:

What can this system or Actor do?

It does not mean:

What should be done right now?

For example:

Capability:
refund_payment

does not imply:

Intent:
Refund this payment

Capability establishes possibility.

Intent establishes desired behavior.

⸻

12. Authority Is Separate From Capability

The existence of a Capability does not imply that an Actor is authorized to use it.

Capability:
delete_customer

is different from:

Authority:
SupportAgent may delete Customer

Therefore:

Capability ≠ Authority

Noema must preserve this distinction.

⸻

13. Policy Is Separate From Authority

Authority determines whether an Actor has permission.

Policy determines the governing rules under which an operation may occur.

Authority:
Manager may approve refunds.
Policy:
Refunds above $10,000 require Finance approval.

Both may be necessary before execution.

⸻

14. Constraints Are First-Class

Constraints should not be hidden inside arbitrary application code or prompts when they materially affect execution.

Examples:

Transfer <= available balance
Refund <= original payment
Booking must occur before departure
Only one allocation at a time

Constraints should be inspectable and evaluable.

⸻

15. State Is a Trust Input

Noema must reason about what is currently true before executing an Action.

Intent
+
Current State
+
Policy
+
Constraint
+
Authority
+
Context

Example:

Intent:
Close account
Current State:
Account already closed

The correct behavior may be to recognize that the desired State is already satisfied rather than execute another operation.

⸻

16. Unknown Is Not False

Noema must distinguish:

TRUE
FALSE
UNKNOWN

This is critical.

If Noema cannot establish that:

Actor is authorized

that does not mean:

Actor is unauthorized

It means:

Authorization status is unknown.

The appropriate behavior may be to obtain additional evidence or ask for clarification.

⸻

17. Absence of Evidence Is Not Evidence of Permission

Noema should never reason:

No restriction found
→ therefore permitted

Instead:

Required authority?
Required policy?
Required evidence?
Required state?

must be explicitly satisfied where the operation requires them.

⸻

18. Trust Must Be Deterministic

The Trust Engine should produce a deterministic decision from canonical inputs.

Conceptually:

Trust(
    Intent,
    Actor,
    Resource,
    Capability,
    Authority,
    Policy,
    Constraint,
    Context,
    State,
    Evidence
)

should produce a defined decision such as:

PERMIT
DENY
CLARIFY
REQUIRE_APPROVAL
REQUIRE_EVIDENCE

The Model should not directly control this decision.

⸻

19. Trust Is Not Model Confidence

A Model may return:

confidence = 0.97

That does not mean:

trust = 0.97

Model confidence describes the Model’s confidence in its interpretation.

Trust describes whether Noema permits the resulting Action.

These are fundamentally different dimensions.

⸻

20. Evidence Must Be Distinguishable From Inference

Noema should distinguish:

Observed fact
Retrieved fact
User assertion
Model inference
System-derived fact

Example:

Account Status:
ACTIVE
Source:
Bank API

is different from:

Account Status:
ACTIVE
Source:
Model inferred from conversation

Consequential decisions should prefer authoritative evidence.

⸻

21. Resolution Must Precede Execution

Before an Action executes, Noema should resolve the semantic objects required to execute it.

At minimum:

Actor
Intent
Resource
Capability
Parameters
Context
Authority
Policy
Constraints

The general flow is:

Interpret
   ↓
Resolve
   ↓
Validate
   ↓
Trust
   ↓
Execute

⸻

22. No Hidden Semantic State

Critical meaning must not exist only inside:

* prompts
* Model context
* undocumented code
* tool descriptions
* application-specific conventions

If a concept affects whether an Action is permitted, its semantics should be representable in the canonical system.

⸻

23. The Canonical Representation Is the Contract

Once an Intent has been resolved into canonical form, downstream systems should operate on that representation rather than repeatedly reinterpreting the original natural language.

Natural Language
       ↓
Canonical Intent
       ↓
Action
       ↓
Execution

This prevents semantic drift across the execution pipeline.

⸻

24. Natural Language Is an Interface, Not the Canon

Users speak natural language.

Noema should not store natural language as the ultimate representation of intent.

Natural language is:

input

Canonical Intent is:

meaning

Action is:

execution

⸻

25. The Same Intent Should Be Interface-Independent

An Intent should be representable regardless of whether it originated from:

Chat
Voice
API
UI
Event
Agent
Application

For example:

"Renew my card."

and:

POST /cards/123/renew

may represent related operations, but Noema’s canonical semantics should not depend on either interface.

⸻

26. Explicit Beats Implicit

If an important relationship matters to execution, represent it explicitly.

Prefer:

Actor
  └── has_authority_for ──► Capability

over:

some hidden application convention

Prefer:

Action
  └── targets ──► Resource

over:

target inferred from arbitrary arguments

⸻

27. Determinism at the Boundary, Probabilism at the Edge

Noema should allow probabilistic systems where they create value:

language understanding
entity matching
intent classification
retrieval
candidate generation
planning

But deterministic boundaries should surround consequential execution:

          Probabilistic
              Model
                ↓
        Candidate Meaning
                ↓
       ┌────────────────┐
       │ Deterministic  │
       │ Noema Boundary │
       └────────────────┘
                ↓
             Action

This is a central architectural principle.

⸻

28. Clarification Is a First-Class Outcome

Clarification is not an error condition.

It is a legitimate system state.

Intent
  ↓
Insufficient information
  ↓
CLARIFICATION REQUIRED

A good Noema system should sometimes ask a question rather than perform an operation.

⸻

29. Refusal Is a Valid System Behavior

Noema must be able to say:

DENIED

without treating this as system failure.

If:

Policy prohibits Action

then refusal is correct behavior.

Likewise if:

Authority is insufficient

execution should stop.

⸻

30. Human Approval Is a First-Class Control

Some Actions should require human approval.

Intent
 ↓
Trust
 ↓
Approval Required
 ↓
Human Decision
 ↓
Execution

Noema should not equate autonomy with quality.

For high-impact operations, human intervention may be the correct system behavior.

⸻

31. Least Privilege

Noema should execute the minimum authority and capability necessary to satisfy an Intent.

If an Intent requires:

read_customer

Noema should not automatically request:

admin_customer

Likewise, an Action should operate against the smallest appropriate Resource scope.

⸻

32. Minimum Sufficient Action

Noema should prefer the smallest Action that fully satisfies the Intent.

Example:

Intent:
Change email address.

Do not execute:

Update entire customer profile.

if:

UpdateEmail

is sufficient.

This reduces:

* blast radius
* unintended mutations
* authorization complexity
* failure modes

⸻

33. Minimum Sufficient Information

Noema should request only the information necessary to resolve and execute an Intent.

Bad:

“Please provide all your account details.”

Better:

“Which of your two accounts should I use?”

The goal is not maximum information.

It is sufficient information for deterministic execution.

⸻

34. Side Effects Must Be Explicit

An Action should make its meaningful side effects discoverable.

For example:

Action:
CancelSubscription
Effects:
Subscription → CANCELLED
Future billing → stopped
Access → retained until end of period

Noema should not execute consequential side effects that are invisible in the canonical Action semantics.

⸻

35. Read and Write Must Be Distinct

Noema should distinguish:

READ

from:

MUTATE

and:

DESTRUCTIVE

operations.

The Trust requirements for:

GetCustomer

should not automatically be equivalent to:

DeleteCustomer

⸻

36. Destructive Actions Require Stronger Semantics

Actions that:

delete
transfer
publish
approve
cancel
revoke
deploy
send
charge

may produce irreversible or consequential effects.

They should generally require stronger validation than informational Actions.

⸻

37. Reversibility Matters

Noema should understand whether an Action is:

reversible
partially reversible
irreversible

Example:

UpdateProfile

may be reversible.

DeletePermanentData

may not be.

Irreversibility should influence Trust requirements.

⸻

38. Idempotency Matters

If an Intent has already been satisfied, Noema should avoid unnecessary duplicate execution.

Example:

Intent:
Activate card.
Current State:
ACTIVE.

The system should recognize that executing another activation may be unnecessary or invalid.

⸻

39. Execution Success Is Not Intent Success

This distinction is foundational.

Action:
HTTP 200

does not necessarily mean:

Intent:
Satisfied

Noema must evaluate the resulting Outcome and State.

Action Success
      ≠
Intent Satisfaction

⸻

40. Outcomes Must Be Verifiable

Where practical, Noema should verify that the expected Outcome actually occurred.

Expected:
Account → ACTIVE
Observed:
Account → ACTIVE

Then:

Intent:
SATISFIED

If the observed State differs:

Intent:
NOT SATISFIED

⸻

41. External Systems Remain Authoritative for Their Domain State

When Noema modifies an external Resource, the external system should remain the authority over its resulting domain state unless explicitly designed otherwise.

For example:

Payment Provider

remains authoritative for:

Payment = SETTLED

Noema should not declare:

Payment = SETTLED

simply because its Action returned successfully.

⸻

42. Provenance Is Part of Meaning

For consequential facts, Noema should know:

What is the fact?
Where did it come from?
When was it observed?
How was it derived?
Is the source authoritative?

A fact without provenance may be insufficient for Trust.

⸻

43. Temporal Semantics Matter

Intent is interpreted relative to time.

Consider:

“Book the room tomorrow.”

The system must understand:

Actor
Resource
Date
Time
Timezone
Availability

Likewise, Policies and States may change over time.

Noema must not treat temporal information as incidental metadata.

⸻

44. Scope Must Be Explicit

An operation may be scoped to:

Actor
Tenant
Organization
Project
Account
Environment
Region
Resource

Noema must not silently broaden scope.

Example:

“Delete my test deployments.”

must not become:

Delete all deployments.

⸻

45. No Silent Escalation

Noema must not escalate an Intent into a more powerful Action merely because it is technically easier.

Requested:
Read
Executed:
Read + Modify

is unacceptable unless the additional operation is explicitly authorized and semantically required.

⸻

46. No Silent Expansion of Intent

Similarly:

“Renew my card.”

must not automatically imply:

change address
change billing plan
increase credit limit
order additional cards

unless those effects are explicitly part of the canonical Action or required by domain semantics.

⸻

47. Semantic Equivalence Matters

Different natural-language expressions may map to the same Intent.

"Renew my card."
"Get me a new card when this one expires."
"Replace my expiring card."

may resolve to equivalent or related canonical Intents.

The canonical representation should capture semantic meaning rather than surface wording.

⸻

48. Semantic Differences Must Be Preserved

Conversely, similar language may represent materially different Intents.

"Cancel my subscription."
"Pause my subscription."
"Stop charging me."
"Delete my subscription."

These must not be collapsed merely because they sound similar.

Semantic distinctions matter when they produce different Actions or Outcomes.

⸻

49. Domain Semantics Must Be Composable

Noema should allow domains to define their own:

Entities
Resources
Capabilities
Policies
Constraints
States
Actions
Outcomes

while still using the same foundational ontology.

The goal is:

Universal primitives
+
Domain-specific semantics
=
Executable domain intent

⸻

50. Canonical Primitives Should Remain Small

Noema should resist continuously adding primitives.

A new primitive should exist only when the existing ontology cannot accurately represent the concept.

The objective is:

Minimum ontology, maximum expressive power.

⸻

51. Core Semantics Should Be Domain-Agnostic

The foundational meaning of:

Intent
Actor
Action
Resource
Capability
Policy
Constraint
Authority
Outcome
State
Context

should not depend on banking, healthcare, logistics, HR, or another particular industry.

Domains extend the primitives.

They should not redefine them casually.

⸻

52. Domain Logic Should Remain Domain-Owned

Noema should not become the ultimate owner of every domain rule.

For example:

Bank:
ledger semantics
Airline:
seat inventory semantics
Hospital:
clinical workflow semantics
ERP:
procurement semantics

Noema provides the common semantic execution layer.

⸻

53. Auditability Is a Design Requirement

For consequential Actions, Noema should be able to reconstruct:

Who intended it?
What did they intend?
What Resource was targeted?
What interpretation was produced?
What evidence supported it?
What Policy applied?
What Authority existed?
What Action was executed?
What happened?
What State changed?

Auditability should not be bolted on after execution.

⸻

54. Explainability Means Traceability

Noema does not need to expose private Model reasoning.

Instead, it should be able to explain the decision trace:

Intent:
Renew Card
Resource:
Card #123
Capability:
renew_card
Authority:
Cardholder
Policy:
Card renewal permitted
Constraint:
Card must be eligible
Trust:
PERMIT
Action:
RenewCard
Outcome:
Renewal accepted

This is operational explainability.

⸻

55. Failure Must Be Explicit

Noema should represent failure as a first-class condition.

Examples:

INTERPRETATION_FAILED
RESOLUTION_FAILED
AUTHORITY_FAILED
POLICY_FAILED
CONSTRAINT_FAILED
EXECUTION_FAILED
OUTCOME_VERIFICATION_FAILED

A generic:

"Something went wrong."

is insufficient for a system whose purpose is trustworthy execution.

⸻

56. Partial Failure Must Be Representable

Multi-step Intent execution may partially succeed.

Noema must not collapse:

Step A succeeded
Step B failed

into:

Action failed

without preserving the actual execution state.

⸻

57. Compensation Must Not Be Assumed

If an Action fails after partial execution, Noema must not assume that simply running an inverse Action will restore the original State.

Compensation is domain-specific.

The system should represent the need for compensation or reconciliation explicitly.

⸻

58. Noema Should Prefer Bounded Autonomy

Autonomy should be bounded by:

Authority
Policy
Constraint
Context
State
Risk
Reversibility

The objective is not:

maximum autonomy

but:

maximum useful autonomy within a defined trust boundary

⸻

59. Escalation Is Better Than Guessing

When Noema cannot safely complete an Intent:

Clarify

or:

Request Approval

or:

Request Evidence

or:

Escalate

is preferable to silently inventing missing information.

⸻

60. The System Must Be Able to Stop

A trustworthy execution system requires a valid terminal state of:

STOP

Noema must be comfortable not executing.

The ability to say:

“I cannot safely determine this.”

is a feature, not a failure.

⸻

61. Integration Should Follow Semantics

Noema should not design its ontology around the quirks of an individual integration.

Bad:

Stripe has X field
therefore Noema defines X

Better:

Noema defines:
Payment
Stripe adapter maps:
Stripe PaymentIntent → Payment

The canonical model comes first.

⸻

62. Adapters Translate; They Do Not Redefine

External systems should be connected through adapters that map:

External Semantics
       ↕
Noema Canonical Semantics

An integration should not redefine the meaning of canonical primitives.

⸻

63. Implementation Should Be Replaceable

The architecture should allow replacement of:

Model
Database
Vector Store
Graph Store
Queue
Transport
Integration
Execution Runtime

without changing the fundamental Noema thesis.

⸻

64. Optimize for Correctness Before Autonomy

The order of priorities should be:

Correctness
   ↓
Safety
   ↓
Determinism
   ↓
Auditability
   ↓
Reliability
   ↓
Autonomy
   ↓
Optimization

Autonomy that produces incorrect Actions is negative value.

⸻

65. Optimize for Semantic Compression

Noema’s value should increase as complex human intent can be represented by a small, stable set of canonical primitives.

For example:

Human Language
       ↓
Complex Intent
       ↓
Canonical Representation
       ↓
Executable Action

The canonical representation should be simpler and more precise than the original conversational expression.

⸻

66. The Canonical Model Must Outlive the Model

Models will change.

Prompt techniques will change.

Integration protocols will change.

Infrastructure will change.

The canonical semantic model should remain comparatively stable.

Model        → replaceable
Prompt       → replaceable
Transport    → replaceable
Integration  → replaceable
Ontology     → durable
Intent Model → durable
Trust Model  → durable

⸻

67. The Ultimate Principle

All other principles should ultimately serve one idea:

Noema exists to make human intent executable without making uncertainty, authority, policy, or state invisible.

The complete conceptual pipeline is:

                 HUMAN
                   │
                   ▼
                INTENT
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Context            Actor
          │                 │
          └────────┬────────┘
                   ▼
            Canonical Meaning
                   │
          ┌────────┼─────────┐
          ▼        ▼         ▼
       Resource Capability Authority
          │        │         │
          └────────┼─────────┘
                   ▼
              Policy
                   │
              Constraint
                   │
                State
                   │
                   ▼
                 TRUST
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       PERMIT    CLARIFY    DENY
          │
          ▼
        ACTION
          │
          ▼
      EXECUTION
          │
          ▼
       OUTCOME
          │
          ▼
    RESULTING STATE
          │
          ▼
  INTENT SATISFIED?

And the governing rule is:

Interpret probabilistically. Resolve canonically. Decide deterministically. Execute explicitly. Verify the outcome.