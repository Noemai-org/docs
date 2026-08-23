Yes. intent.md is probably the central ontology document in Noema. It should establish what an Intent actually is, while carefully keeping Intent separate from language, Action, Capability, and model output.

I’d make this one more foundational than the others because the rest of the system ultimately hangs off the Intent.

Intent

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/intent.md

⸻

1. Definition

An Intent is a structured representation of an Actor’s desired objective, including the target, relevant parameters, constraints, and Context necessary to determine what the Actor is trying to accomplish.

Intent answers:

What does the Actor want to accomplish?

An Intent represents a desired outcome, not an implementation.

Example:

Actor:
Customer
Intent:
Renew Card
Target:
card_1234

The Actor may express this as:

“Please renew my card.”

The natural-language expression is not itself the canonical Intent.

⸻

2. Intent Is the Core Semantic Object

Noema exists to transform ambiguous human interaction into a representation that can be evaluated deterministically.

Conceptually:

Human Expression
      │
      ▼
Interpretation
      │
      ▼
Candidate Intent
      │
      ▼
Context + Evidence
      │
      ▼
Canonical Intent
      │
      ▼
Trust Evaluation
      │
      ▼
Action

The Intent is therefore the principal semantic boundary between:

what the Actor means

and:

what the system may actually do

⸻

3. Intent Is Not Natural Language

Natural language is an expression of Intent.

It may be:

* incomplete
* ambiguous
* contextual
* colloquial
* indirect
* contradictory
* underspecified

For example:

“Can you sort out my card?”

Possible Intent candidates:

RenewCard
ReplaceCard
UnblockCard
CancelCard

The sentence itself does not establish which Intent is correct.

Noema must resolve this using Context, Evidence, and other available information.

⸻

4. Intent Is Not Model Output

A Model may propose an Intent representation.

That proposal is not automatically canonical.

User Expression
      │
      ▼
Model
      │
      ▼
Intent Proposal
      │
      ▼
Noema Validation
      │
      ▼
Canonical Intent

The Model is therefore an Intent interpreter, not the final authority over Intent state.

⸻

5. Intent Is Not Action

This distinction is fundamental.

Intent:
Renew my card.
Action:
RenewCard(card_1234)

The Intent expresses the objective.

The Action is the operation selected to achieve that objective.

One Intent may map to:

one Action

or:

multiple Actions

depending on the domain.

⸻

6. Intent Is Not Capability

Capability represents what a system can do.

Intent represents what the Actor wants.

Intent:
Renew my card.
Capability:
card.renew

A Capability may satisfy an Intent, but the existence of a Capability does not establish that it should be used.

⸻

7. Intent Is Not Authority

An Actor can express an Intent without being authorized to fulfill it.

Actor:
Employee
Intent:
Delete customer account.
Authority:
Insufficient

The Intent remains valid as an expression of what the Actor wants.

The Trust system determines whether the requested operation may proceed.

⸻

8. Intent Is Not Constraint

Constraints limit an Intent or its execution.

Intent:
Transfer $10,000.
Constraint:
Transfers above $5,000 require approval.

The Constraint does not become part of the objective.

It constrains how the objective may be fulfilled.

⸻

9. Intent Is Not Outcome

Intent describes what the Actor wants.

Outcome describes what actually happened.

Intent:
Refund payment.
Outcome:
Refund rejected because payment already settled.

Therefore:

Intent ≠ Outcome

An Intent may remain valid even when execution fails.

⸻

10. Intent Structure

A canonical Intent conceptually contains:

Intent
├── Actor
├── Objective
├── Target
├── Parameters
├── Constraints
├── Context
├── Priority
└── Temporal Requirements

Not every Intent requires every field.

The canonical structure is semantic rather than a fixed storage schema.

⸻

11. Actor

Every Intent has an initiating Actor.

Example:

Actor:
customer_123
Intent:
RenewCard

The Actor may be:

* human
* organization
* service
* autonomous agent
* system process

The Actor is distinct from the Intent.

⸻

12. Objective

The Objective describes the desired result.

Example:

Objective:
Renew Card

The Objective should describe the semantic goal rather than the implementation mechanism.

Prefer:

Renew Card

over:

POST /cards/123/renew

The latter is an Action or implementation detail.

⸻

13. Target

The Target identifies the Entity or Entities to which the Intent applies.

Example:

Intent:
Renew Card
Target:
card_1234

Target resolution may require Context.

If the target cannot be determined sufficiently:

Intent:
"Renew my card."
Available Cards:
3
Result:
Clarification Required

Noema must not silently select one.

⸻

14. Parameters

Parameters provide information required to fully specify the objective.

Example:

Intent:
BookFlight
Parameters:
origin = Lagos
destination = London
date = 2026-09-12
passengers = 1

Parameters may be:

* explicit
* inferred
* retrieved
* defaulted
* unresolved

Their epistemic status must remain distinguishable.

⸻

15. Explicit Parameters

A parameter explicitly supplied by the Actor.

User:
"Book me a flight to London on September 12."
Parameters:
destination = London
date = September 12

These generally have stronger evidentiary status than model inference, although explicit user input may still be ambiguous.

⸻

16. Inferred Parameters

A parameter inferred from Context or language.

Example:

User:
"Book me the cheapest flight."
Possible inference:
currency = user's default currency

Inference must remain distinguishable from explicit input.

Material inferred parameters may require confirmation.

⸻

17. Default Parameters

A parameter supplied by an explicit domain or system default.

Example:

User:
"Show my transactions."
Default:
sort = newest_first

Defaults must come from defined semantics rather than arbitrary model behavior.

⸻

18. Unresolved Parameters

A parameter required to complete an Intent but not yet established.

Example:

Intent:
TransferMoney
Missing:
destination_account

The Intent may therefore exist in a partially resolved state.

Intent
   ↓
Incomplete
   ↓
Clarification Required

⸻

19. Constraints

An Intent may contain or reference Constraints.

Example:

Intent:
BookFlight
Constraint:
Budget <= $800

Constraints do not necessarily originate from the Actor.

They may originate from:

* policy
* authority
* system requirements
* business rules
* explicit user requirements

⸻

20. Context

Intent interpretation depends on Context.

Example:

User:
"Renew it."
Context:
Current conversation concerns card_1234.

The Context allows the reference “it” to be resolved.

Context may also determine:

* target
* parameters
* applicable policies
* authority
* available capabilities
* constraints

See context.md.

⸻

21. Temporal Requirements

Some Intents contain temporal requirements.

Examples:

"Send this tomorrow."
"Cancel my subscription at the end of the month."
"Transfer $500 every Friday."

Temporal semantics may include:

start time
deadline
scheduled time
recurrence
duration
expiration

Time must be resolved explicitly when material.

⸻

22. Priority

An Intent may contain a priority when the Actor explicitly communicates one or the domain defines one.

Examples:

urgent
high
normal
low

Priority must not automatically override Constraints, Authority, or Trust.

For example:

User:
"This is urgent, transfer the money now."
Constraint:
Transfer requires approval.

Urgency does not eliminate the Constraint.

⸻

23. Intent References

Actors frequently express Intent indirectly.

Examples:

“Can you take care of this?”

“Fix my account.”

“I need that cancelled.”

“Make it work again.”

These expressions may contain an Intent but require Context to resolve:

Reference
   +
Context
   ↓
Candidate Intent

⸻

24. Intent Ambiguity

An Intent is ambiguous when multiple materially different interpretations remain possible.

Example:

User:
"Cancel my account."
Possible targets:
Account A
Account B
Account C

Or:

User:
"Fix my card."
Possible objectives:
Renew
Replace
Unblock

If the ambiguity can change the resulting Action or Outcome, Noema must not silently choose.

⸻

25. Intent Completeness

An Intent is complete when all information required for the relevant downstream decision has been sufficiently established.

Completeness is contextual.

For example:

"Show my account."

may be complete if the Actor has exactly one account.

But:

"Transfer money."

is incomplete if the destination and amount are required.

Therefore:

Intent completeness is determined by the requirements of the intended operation, not by the grammatical completeness of the sentence.

⸻

26. Intent Resolution

Intent Resolution transforms a raw expression into a canonical representation.

Expression
    │
    ▼
Candidate Interpretations
    │
    ├── Context
    ├── Entity Resolution
    ├── Constraints
    └── Evidence
          │
          ▼
    Resolved Intent

Resolution must establish enough semantic information for deterministic downstream evaluation.

⸻

27. Intent Resolution Is Not Execution

Noema may successfully resolve an Intent without executing anything.

User:
"Cancel my subscription."
Result:
Intent resolved.
No execution yet.

This distinction allows Noema to evaluate:

* authority
* policy
* constraints
* capability
* trust

before consequential behavior occurs.

⸻

28. Intent Lifecycle

An Intent may progress through states such as:

RECEIVED
   ↓
INTERPRETING
   ↓
PARTIALLY_RESOLVED
   ↓
CLARIFICATION_REQUIRED
   ↓
RESOLVED
   ↓
VALIDATED
   ↓
TRUSTED
   ↓
EXECUTING
   ↓
COMPLETED

Alternative terminal states may include:

REJECTED
FAILED
CANCELLED
ESCALATED

The exact state machine belongs in the Intent lifecycle specification.

⸻

29. Intent State vs Intent

Intent and Intent State are distinct.

Intent:
Renew card_1234
State:
RESOLVED

The Intent represents the semantic object.

The State describes where that Intent currently is in Noema’s lifecycle.

⸻

30. Intent Revision

An Intent may change as new information becomes available.

Example:

Initial:
"Book me a flight to London."
Later:
"Actually, make it Manchester."

This may represent:

Intent Revision

rather than a completely unrelated Intent.

Noema should preserve the relationship between revisions where auditability matters.

⸻

31. Intent Supersession

A newer Intent may supersede an earlier one.

Example:

Intent A:
Transfer $500.
Intent B:
Actually, transfer $700 instead.

Intent B may supersede Intent A.

The system should not execute both merely because both were previously resolved.

⸻

32. Intent Cancellation

An Actor may explicitly cancel an Intent.

Intent:
Send payment.
Actor:
"Never mind, cancel that."

Noema must distinguish:

Intent Cancellation

from:

Action Cancellation

An Intent may be cancelled before any Action occurs.

⸻

33. Compound Intents

An Actor may express multiple objectives in one interaction.

Example:

“Cancel my old subscription and move me to the Pro plan.”

This may resolve into:

Intent A:
Cancel Subscription
Intent B:
Create / Upgrade Subscription

These may have dependencies.

Intent A
   ↓
Outcome
   ↓
Intent B

The exact decomposition belongs in the Intent Resolution specification.

⸻

34. Dependent Intents

One Intent may depend on another.

Example:

Intent A:
Create Account
Intent B:
Fund Account

Intent B cannot execute successfully until Intent A produces the required Entity and state.

⸻

35. Intent Composition

Multiple Intent components may form a larger objective.

Example:

"Move me from Basic to Pro and cancel my old billing plan."

Canonical representation may contain:

Composite Intent
├── Upgrade Subscription
└── Cancel Billing Plan

Composition must preserve dependencies and ordering where material.

⸻

36. Intent Decomposition

A single high-level Intent may require multiple Actions.

Example:

Intent:
"Onboard this employee."
Actions:
1. Create employee record
2. Create email account
3. Assign permissions
4. Send welcome email

The Actor expressed one objective.

Noema may derive multiple Actions to fulfill it.

Intent
   ↓
Action Plan
   ├── Action 1
   ├── Action 2
   ├── Action 3
   └── Action 4

Action planning must remain subordinate to the Intent.

⸻

37. Intent vs Action Plan

An Intent describes what should be achieved.

An Action Plan describes how the system proposes to achieve it.

Intent:
Onboard employee.
Action Plan:
Create employee
→ provision email
→ assign permissions
→ notify employee

The Action Plan may change without changing the underlying Intent.

⸻

38. Intent and Capability Matching

Once an Intent is resolved, Noema may determine which Capabilities could satisfy it.

Intent
   ↓
Required Ability
   ↓
Capability Matching
   ↓
Candidate Capabilities

Example:

Intent:
Renew Card
Capabilities:
bank.card.renew
thirdparty.card.replace

Capability selection must consider Context, Constraints, Authority, and Trust.

⸻

39. Intent and Authority

Intent does not imply permission.

Actor:
Employee
Intent:
Approve $100,000 payment.
Authority:
Maximum approval = $50,000

The Intent remains semantically valid.

Trust evaluation rejects or escalates execution.

⸻

40. Intent and Policy

Policies may constrain how an Intent can be fulfilled.

Intent:
Refund customer.
Policy:
Refunds above $10,000 require manager approval.

The Policy does not alter the Actor’s desired objective.

It changes the conditions under which the Intent may be fulfilled.

⸻

41. Intent and Constraints

Constraints may originate directly from the Intent.

Example:

“Book me the cheapest direct flight under $800.”

Canonical Intent:

Objective:
Book Flight
Constraints:
direct = true
price <= $800

The constraints become part of the semantic representation because they affect fulfillment.

⸻

42. Intent and Entity Resolution

An Intent may reference an Entity indirectly.

"Renew my main card."

Noema must resolve:

"main card"
      ↓
Candidate Entities
      ↓
Context
      ↓
Resolved Entity

Entity resolution is therefore often a prerequisite for complete Intent resolution.

⸻

43. Intent and Context Resolution

Context can disambiguate the Intent.

Example:

Previous:
"Let's talk about my Pro subscription."
Current:
"Cancel it."

Context:

Current subject = Pro subscription

Intent:

CancelSubscription
Target = Pro subscription

Context must remain traceable as the basis for resolution.

⸻

44. Intent and Evidence

Evidence can support Intent interpretation.

Example:

User:
"My card is expired. Renew it."
Evidence:
Banking System confirms expiry.

The Evidence strengthens the interpretation.

However:

Evidence supports Intent resolution; it does not itself constitute Intent.

⸻

45. Intent and Trust

Intent is one of the principal inputs to Trust evaluation.

Conceptually:

Intent
   +
Context
   +
Entity
   +
Constraints
   +
Authority
   +
Evidence
   +
Capability
        │
        ▼
    Trust Decision

A resolved Intent is therefore not automatically trusted.

⸻

46. Intent and Execution

Only after the relevant Trust conditions are satisfied should Noema authorize execution.

Intent
  ↓
Resolve
  ↓
Validate
  ↓
Trust
  ↓
Action
  ↓
Execute

The distinction is fundamental:

An Intent expresses what should happen; execution determines whether anything actually happens.

⸻

47. Intent and Outcome

The Outcome must be compared against the original Intent.

Example:

Intent:
Transfer $500.
Observed Outcome:
Transfer $500 completed.

Success.

But:

Intent:
Transfer $500.
Observed Outcome:
Transfer $450 completed.

The system must not treat this as equivalent merely because an Action executed successfully.

Outcome verification must evaluate whether the observed result satisfies the Intent.

⸻

48. Intent Satisfaction

An Intent is satisfied when the resulting Outcome fulfills the semantic objective.

Conceptually:

Intent
   +
Observed Outcome
      │
      ▼
Satisfaction Evaluation
      │
   ┌──┴──┐
   ▼     ▼
Satisfied Unsatisfied

Technical execution success does not necessarily imply Intent satisfaction.

⸻

49. Intent Failure

An Intent may fail at multiple layers.

Interpretation Failure

No sufficiently reliable Intent can be resolved.

Validation Failure

Required conditions are not satisfied.

Trust Failure

Noema refuses to authorize execution.

Execution Failure

The Action cannot be successfully performed.

Outcome Failure

Execution succeeds technically but does not satisfy the Intent.

These must remain distinguishable.

⸻

50. Intent Uncertainty

Noema should represent uncertainty explicitly.

Examples:

Unknown target
Ambiguous objective
Missing parameter
Conflicting Context
Insufficient authority information
Uncertain capability

Noema must not silently convert uncertainty into certainty merely to continue execution.

⸻

51. Intent Clarification

Clarification is required when unresolved information is material.

Example:

User:
"Transfer $500."
Missing:
Destination account.

Noema should ask:

"Which account should I transfer the $500 to?"

rather than inventing a destination.

⸻

52. Minimal Clarification

Clarification should request the minimum information necessary to resolve the Intent.

Bad:

Please provide your full account details, address,
identity information, and transaction history.

Better:

Which account should receive the $500?

The objective is to minimize friction while preserving deterministic resolution.

⸻

53. Intent Normalization

Normalization converts semantically equivalent expressions into a canonical representation.

Examples:

"Cancel my subscription."
"Please cancel my plan."
"Get me off this subscription."

may normalize to:

Objective:
Cancel Subscription

Normalization must preserve materially meaningful differences.

⸻

54. Intent Equivalence

Two expressions may represent equivalent Intent even when their wording differs.

"Cancel my plan."
"Terminate my subscription."

Potentially equivalent:

CancelSubscription

But:

"Pause my subscription."

is materially different.

Semantic equivalence must therefore be determined by the ontology, not surface wording alone.

⸻

55. Intent Specificity

Intent representations may exist at different levels of specificity.

Example:

High-level:
Manage my account.
More specific:
Update my account.
Canonical:
UpdateAccountEmail

Noema should resolve to the level of specificity required for deterministic execution.

A vague Intent may be valid without being executable.

⸻

56. Intent Granularity

Noema should avoid both:

Overly broad Intent

and:

Implementation-level Intent

For example:

"Fix my banking situation."

is too broad to execute.

But:

POST /v1/accounts/123/cards/456/renew

is not an Intent.

The appropriate semantic level is:

RenewCard
Target = card_456

⸻

57. Intent Canonical Form

A conceptual canonical Intent representation:

Intent
├── id
├── actor
├── objective
├── target
├── parameters
├── constraints
├── context
├── temporal_requirements
├── priority
├── provenance
└── state

The actual serialization belongs to the schema and implementation specifications.

⸻

58. Intent Resolution Pipeline

The canonical resolution pipeline is:

User Expression
      │
      ▼
Language Interpretation
      │
      ▼
Candidate Intent(s)
      │
      ▼
Entity Resolution
      │
      ▼
Context Assembly
      │
      ▼
Parameter Resolution
      │
      ▼
Constraint Identification
      │
      ▼
Completeness Check
      │
      ▼
Canonical Intent

If a material ambiguity remains:

                 ┌──► Clarification
                 │
Candidate Intent ┤
                 │
                 └──► Canonical Intent

⸻

59. Intent Validation

Before an Intent becomes eligible for Trust evaluation, Noema should validate:

* Actor
* Objective
* Target
* required parameters
* relevant Context
* applicable Constraints
* temporal requirements
* Entity resolution
* semantic consistency

Validation must be deterministic where the relevant information permits it.

⸻

60. Intent Trust Boundary

A resolved Intent may still be untrusted.

Candidate Intent
      ↓
Canonical Intent
      ↓
Validation
      ↓
Trust Evaluation
      ↓
Trusted Intent

The Trusted Intent is the semantic representation that Noema is willing to use as the basis for consequential Action.

⸻

61. Trusted Intent

A Trusted Intent is an Intent that has satisfied the applicable Noema requirements for proceeding toward Action.

Trust may depend on:

Intent validity
Entity resolution
Context sufficiency
Authority
Constraints
Policy
Capability
Evidence
Risk

Trust is therefore contextual.

⸻

62. Intent Immutability After Trust

Once an Intent crosses a consequential Trust Boundary, material modifications should not silently mutate the trusted Intent.

If the Actor changes:

amount
target
destination
scope

Noema should generally produce a new or revised Intent requiring appropriate revalidation.

Trusted Intent A
      │
      │ material change
      ▼
Intent Revision B
      │
      ▼
Revalidation

⸻

63. Intent Identity

An Intent should have its own identity independent of the natural-language expression that produced it.

For example:

Intent ID:
intent_123

The same conversational interaction may produce multiple Intent objects.

⸻

64. Intent Provenance

Intent provenance should capture how the Intent was established.

Conceptually:

Intent
├── originating expression
├── Actor
├── Context used
├── Entity resolution
├── Model proposal
├── validation
└── resolution timestamp

This supports auditability without requiring preservation of hidden model chain-of-thought.

⸻

65. Intent Versioning

An Intent may have revisions.

intent_123
   │
   ├── v1: Transfer $500
   │
   ├── v2: Transfer $700
   │
   └── v3: Transfer $700 to Account B

Material revisions should preserve lineage.

⸻

66. Intent Cancellation and Supersession

An Intent may be:

CANCELLED
SUPERSEDED
EXPIRED
COMPLETED
FAILED

These states must be distinguished.

For example:

SUPERSEDED

means another Intent replaced it.

CANCELLED

means the Intent was explicitly withdrawn.

⸻

67. Recurring Intents

Some Intent expressions represent recurring objectives.

Example:

“Transfer $500 to my savings account every Friday.”

Canonical representation may include:

Objective:
Transfer Money
Parameters:
amount = $500
destination = savings_account
Temporal Requirement:
recurrence = weekly
day = Friday

Recurring Intent semantics require additional lifecycle rules.

⸻

68. Conditional Intents

Some Intents depend on conditions.

Example:

“If my balance drops below $1,000, transfer $500.”

Canonical representation:

Trigger:
balance < $1,000
Objective:
Transfer $500

The condition must remain distinguishable from the objective.

⸻

69. Delegated Intents

An Actor may express an Intent on behalf of another Actor.

Actor:
Assistant
Principal:
Customer
Intent:
Book flight

The delegation relationship must be explicit.

The fact that an Agent issued the request does not automatically establish that it has Authority.

⸻

70. Agentic Intent

An AI Agent may generate an Intent autonomously based on a prior objective.

Example:

Principal Intent:
"Keep my inventory above 100 units."
Agent-derived Intent:
"Order 50 units from Supplier A."

The derived Intent must remain distinguishable from the Principal’s original Intent.

Principal Intent
      ↓
Agent Reasoning
      ↓
Derived Intent

Derived Intent must be evaluated under the applicable Authority and Trust rules.

⸻

71. Intent Delegation Boundary

An Agent acting on behalf of an Actor does not inherit unlimited authority.

Principal
   │
   └── delegates ──► Agent
                         │
                         └── Intent

The delegation must define its applicable scope.

⸻

72. Intent and Noema’s Core Philosophy

Noema is not fundamentally a system for converting text into tool calls.

The semantic pipeline is:

Human Intent
      ↓
Canonical Intent
      ↓
Deterministic Evaluation
      ↓
Authorized Action

The Action is downstream.

The Intent is the durable semantic object.

⸻

73. Core Invariants

Invariant 1

An Intent represents an Actor’s desired objective.

Invariant 2

Natural language is an expression of Intent, not necessarily the canonical Intent itself.

Invariant 3

Model output is a proposal and must not automatically become canonical Intent.

Invariant 4

Intent and Action are distinct concepts.

Invariant 5

Intent and Capability are distinct concepts.

Invariant 6

Intent does not imply Authority.

Invariant 7

Intent does not imply Trust.

Invariant 8

Intent does not imply execution.

Invariant 9

Intent does not imply Outcome.

Invariant 10

A material Intent ambiguity must not be silently resolved through unsupported guessing.

Invariant 11

A material unresolved parameter must prevent the Intent from becoming execution-ready.

Invariant 12

Entity resolution must be sufficiently established before a material target is acted upon.

Invariant 13

Context used to resolve an Intent must remain distinguishable from the Intent itself.

Invariant 14

Constraints affecting fulfillment must remain explicitly represented.

Invariant 15

A material Intent modification after Trust requires appropriate revalidation.

Invariant 16

Expected Outcome and observed Outcome must remain distinct.

Invariant 17

Technical execution success does not automatically mean Intent satisfaction.

Invariant 18

Noema must prefer explicit clarification over unsupported assumptions when material uncertainty remains.

Invariant 19

Derived or delegated Intents must remain distinguishable from the originating Actor’s Intent.

Invariant 20

Intent provenance must be sufficient to reconstruct how the canonical Intent was established.

⸻

74. Relationship to Other Ontology Documents

intent.md sits at the center of the ontology:

01-ontology/
│
├── concepts.md
├── entities.md
├── actor.md
├── intent.md
├── action.md
├── capability.md
├── context.md
├── constraint.md
├── policy.md
├── authority.md
├── resource.md
├── state.md
├── evidence.md
├── provenance.md
└── outcome.md

The major semantic relationships are:

Actor
   │
   │ expresses
   ▼
Intent
   │
   ├── targets ──────► Entity
   │
   ├── interpreted by ► Context
   │
   ├── constrained by ► Constraint
   │
   └── governed by ──► Policy
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
                       Outcome

⸻

75. Canonical Summary

An Intent is a structured representation of an Actor’s desired objective, including the target, parameters, constraints, and relevant Context necessary to determine what the Actor wants to accomplish.

The canonical Noema flow is:

               HUMAN EXPRESSION
                      │
                      ▼
              MODEL INTERPRETATION
                      │
                      ▼
               CANDIDATE INTENT
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Context     Entities    Parameters
          │           │           │
          └───────────┼───────────┘
                      ▼
               INTENT RESOLUTION
                      │
                      ▼
              CANONICAL INTENT
                      │
                      ▼
                 VALIDATION
                      │
                      ▼
                TRUST DECISION
                      │
                      ▼
                    ACTION
                      │
                      ▼
                 EXECUTION
                      │
                      ▼
                   OUTCOME

And the most important Noema principle is:

The model may interpret what the Actor probably means; Noema must establish what the Actor means before allowing consequential behavior to proceed.