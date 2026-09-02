Intent Language

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-language.md

⸻

1. Definition

Intent Language is the canonical semantic language Noema uses to represent what an Actor means to accomplish, independently of the natural-language expression used to communicate it and independently of the implementation used to execute it.

Natural language is the input.

Intent Language is the semantic representation.

Actions are the execution.

The fundamental transformation is:

Natural Language
      ↓
Intent Language
      ↓
Executable Intent
      ↓
Action
      ↓
Outcome

Intent Language therefore forms the semantic boundary between human expression and system execution.

⸻

2. Why Intent Language Exists

Humans communicate through language that is:

ambiguous
contextual
implicit
variable
incomplete
probabilistic

Systems execute through structures that are:

typed
explicit
bounded
validated
deterministic

Noema requires an intermediate representation capable of preserving the meaning of the Actor without requiring downstream systems to repeatedly interpret natural language.

Without such a representation:

User
 ↓
Model
 ↓
API call

The Model effectively becomes the execution planner.

Noema instead establishes:

User
 ↓
Model
 ↓
Intent Language
 ↓
Noema Resolution
 ↓
Trust
 ↓
Action

⸻

3. Intent Language Is Not a Programming Language

Intent Language should not be confused with a general-purpose programming language.

It does not primarily describe:

loops
variables
memory
control flow
algorithms
data structures

It describes:

who wants what
from which Resource
under which Constraints
in which Context
for which Outcome
through which Capability

Its semantic unit is Intent, not computation.

⸻

4. Intent Language Is Not Natural Language

Natural language:

“Can you sort out my card? It’s the one I used yesterday.”

Intent Language might represent:

Intent:
ResolveCardIssue
Actor:
CurrentUser
Resource:
CardUsedYesterday
Context:
Issue = unspecified
Outcome:
Card issue resolved

The exact wording disappears.

The semantic commitments remain.

Therefore:

Intent Language is meaning-preserving, not wording-preserving.

⸻

5. Intent Language Is Not an API Contract

An API contract might specify:

POST /cards/{id}/replacement

with:

card_id
reason
shipping_address

That is an execution interface.

Intent Language instead represents:

ReplaceCard(Card)

The Capability that can satisfy the Intent may later map that Intent to one or more APIs.

Therefore:

Intent Language
        ≠
API Schema

⸻

6. Intent Language Is Not a Workflow DSL

A workflow DSL typically describes:

Step A
  ↓
Step B
  ↓
Step C

Intent Language describes the semantic objective.

For example:

“Transfer my balance and close the account.”

Intent Language expresses:

TransferBalance
CloseAccount

with:

TransferBalance PRECEDES CloseAccount

It does not prescribe:

HTTP request A
wait 2 seconds
HTTP request B
retry 3 times

Those belong to execution.

⸻

7. The Core Semantic Vocabulary

Intent Language is built from the concepts defined in Noema’s ontology.

At minimum:

Actor
Intent
Action
Capability
Resource
Entity
Context
Constraint
Policy
State
Outcome
Relationship

These concepts should have stable meanings across the system.

⸻

8. The Core Intent Form

Conceptually:

Intent =
    Actor
    + Objective
    + Resources
    + Context
    + Constraints
    + Expected Outcome

A more expressive representation is:

Intent {
    actor
    objective
    resources
    context
    constraints
    expected_outcome
}

This is a semantic model, not necessarily the final wire format.

⸻

9. Actor

The Actor identifies who intends the Outcome.

Example:

Actor:
User#123

Intent Language must preserve Actor identity because:

authority
ownership
permissions
preferences
policy

may depend on the Actor.

An Intent without a resolvable Actor may not be executable where Actor identity is material.

⸻

10. Objective

The Objective describes what the Actor wants to accomplish.

Examples:

RenewCard
CancelSubscription
TransferFunds
CreateProject
UpdateAddress

The Objective should represent the semantic goal rather than the implementation mechanism.

For example:

Objective:
RenewCard

rather than:

Objective:
POST /cards/123/renew

⸻

11. Resources

Resources identify the objects affected by the Intent.

Example:

Intent:
RenewCard
Resource:
Card#123

Resources may be:

explicit
contextually inferred
retrieved
created by another Intent

but the final executable representation should resolve material Resources explicitly.

⸻

12. Context

Context provides information necessary to interpret an Intent.

Example:

Intent:
"Add Sarah."
Context:
CurrentProject = Noema

The Intent Language representation may therefore become:

AddMember(
    project = Noema,
    member = Sarah
)

Context should not be confused with Intent itself.

Context provides semantic grounding.

⸻

13. Constraints

Constraints restrict how the Intent may be satisfied.

Example:

“Book the cheapest nonstop flight.”

Intent:

BookFlight

Constraints:

nonstop = true
optimize = price

Constraints are part of meaning when the Actor explicitly or contextually establishes them.

⸻

14. Policy

Policy defines system-level or organizational rules governing whether an Intent may be satisfied.

Example:

Intent:
RefundPayment
Policy:
Refunds above $10,000 require approval.

The policy is not necessarily part of what the Actor wants.

Therefore:

Intent Language
        ↓
Trust / Policy Evaluation

Policy constrains execution without changing the Actor’s underlying objective.

⸻

15. Expected Outcome

The Outcome describes the state the Actor expects to exist after successful satisfaction of the Intent.

Example:

Intent:
RenewCard
Expected Outcome:
Card is renewed and usable.

This is important because an Intent should not be defined purely as an Action.

Two different Actions may produce the same Outcome.

⸻

16. Intent Is Goal-Oriented

Intent Language is fundamentally goal-oriented.

Compare:

"Call POST /renew."

with:

"Make my expired card usable again."

The second describes an Intent.

The system may satisfy it through:

replacement
renewal
reactivation

depending on domain rules and available Capabilities.

Therefore:

Intent Language describes desired semantic states, not merely requested operations.

⸻

17. Intent and Action

The distinction must remain strict.

Intent:
Renew my card.
Action:
Create replacement card.
Outcome:
Actor has a valid renewed card.

An Intent may result in:

one Action

or:

multiple Actions

The number of Actions does not determine the number of Intents.

⸻

18. Intent and Capability

A Capability represents what a system is capable of doing.

An Intent represents what the Actor wants.

For example:

Intent:
NotifyCustomer
Available Capabilities:
SendEmail
SendSMS
SendPushNotification

Noema may resolve an appropriate Capability based on:

Context
Constraints
Policy
Actor preference
available Resources

The Intent should remain independent of the Capability implementation.

⸻

19. Intent Language Must Be Capability-Agnostic

The canonical representation should avoid prematurely binding an Intent to an implementation.

For example:

Intent:
NotifyCustomer

is preferable to:

Intent:
SendCustomerEmail

when the Actor only requested notification.

This allows the same Intent to be satisfied by:

Email
SMS
Push

where permitted.

⸻

20. Intent Language and Domain Ontology

Intent Language should use canonical domain concepts rather than arbitrary Model-generated terminology.

For example, if the ontology defines:

Subscription
CancelSubscription
Customer

the Intent Language should reference those canonical concepts.

It should not randomly alternate between:

CancelSubscription
TerminateSubscription
EndPlan
StopMembership

unless those represent genuinely distinct concepts.

This provides semantic consistency.

⸻

21. Canonical Vocabulary

Intent Language should maintain a controlled vocabulary for:

Actions
Entities
Resources
Capabilities
Constraints
States
Outcomes
Relationships

This is one of the primary purposes of the canonical repository.

Natural-language expressions can vary infinitely.

Canonical semantic concepts should not.

⸻

22. Synonyms

Different expressions may map to the same Intent.

Example:

"Cancel my subscription."
"Stop my subscription."
"I don't want this subscription anymore."
"End my subscription."

may map to:

Intent:
CancelSubscription

Intent Language therefore normalizes linguistic variation into canonical meaning.

⸻

23. Polysemy

The same word may represent different semantic concepts depending on Context.

Example:

“Close the account.”

Could mean:

CloseBankAccount
CloseCustomerAccount
CloseInvestmentAccount

Intent Language must therefore be grounded in:

Context
Entity
Resource
Domain

rather than keyword matching.

⸻

24. Intent Language and Ambiguity

Intent Language does not eliminate ambiguity.

Instead, it gives Noema a structured place to represent it.

For example:

Intent:
CancelSubscription
Resource:
?

Candidates:

Subscription#123
Subscription#456

The Intent remains semantically incomplete or ambiguous until resolution.

Therefore:

Natural Language Ambiguity
        ↓
Intent Language
        ↓
Explicit unresolved field
        ↓
Clarification

This is preferable to silently guessing.

⸻

25. Intent Language and Confidence

Confidence is evidence about the validity of a semantic interpretation.

It should not become part of the meaning itself.

For example:

Intent:
RenewCard(Card#123)
Confidence:
0.93

The 0.93 is metadata about the resolution process.

It does not mean:

RenewCard with 93% certainty

as a semantic operation.

⸻

26. Intent Language and Executability

Intent Language can represent an Intent before it is executable.

Example:

Intent:
RenewCard
Actor:
Resolved
Resource:
Ambiguous
Outcome:
Resolved

This is a valid semantic representation but not yet an Executable Intent.

After clarification:

Resource:
Card#123

the Intent may become executable subject to Trust and Policy.

⸻

27. Intent Language and Clarification

Clarification should operate on semantic gaps.

Example:

Intent:
TransferFunds
Source:
Resolved
Destination:
AMBIGUOUS
Amount:
$500

Noema should ask:

“Which account should receive the $500?”

rather than asking the Actor to restate the entire request.

Intent Language therefore enables targeted clarification.

⸻

28. Intent Language and Composition

Intent Language must support Composite Intents.

Example:

CompositeIntent
├── TransferBalance
└── CloseAccount

Relationship:

TransferBalance
    PRECEDES
CloseAccount

This allows complex natural-language requests to be represented without collapsing them into an opaque command.

⸻

29. Intent Language and Context Continuity

Consider:

“Create a project called Noema.”

followed by:

“Add Sarah to it.”

Intent Language can preserve:

Intent A:
CreateProject(Noema)
Intent B:
AddMember(
    project = Noema,
    member = Sarah
)

The phrase “it” disappears.

Its semantic reference remains.

⸻

30. Intent Language and Temporal Continuity

Intent Language must support Intent lifecycle over time.

An Intent may transition through:

Expressed
↓
Interpreted
↓
Ambiguous
↓
Clarifying
↓
Resolved
↓
Executable
↓
Authorized
↓
Executing
↓
Completed

The semantic identity of the Intent should survive these transitions.

⸻

31. Intent Language and State

State describes the current condition of an Intent, Resource, or Outcome.

Example:

Intent State:
RESOLVED
Card State:
EXPIRED

The distinction matters.

An Intent Language representation should not confuse:

what the Actor wants

with:

what is currently true

⸻

32. Intent Language and Constraints

Constraints should be explicit.

Example:

“Transfer $500 to savings, but don’t use my emergency account.”

Intent:
TransferFunds
Amount:
$500
Destination:
SavingsAccount
Constraint:
Source != EmergencyAccount

This preserves an important semantic restriction that could otherwise be lost during execution planning.

⸻

33. Positive and Negative Intent

Intent Language should support both:

desired conditions

and:

prohibited conditions

Example:

“Book the cheapest flight, but not one with a layover.”

Objective:
BookFlight
Constraint:
Optimize(price)
Constraint:
Stops = 0

Negative constraints are still part of the Intent’s semantic specification.

⸻

34. Preferences vs Constraints

Not every Actor statement has equal semantic force.

Example:

“I’d prefer an afternoon flight.”

This may represent a Preference.

Whereas:

“I cannot travel before 2 PM.”

is a Constraint.

Intent Language should preserve this distinction.

Conceptually:

Preference:
preferred_departure >= 14:00
Constraint:
departure >= 14:00

The former can potentially be relaxed.

The latter cannot without changing the Intent.

⸻

35. Intent Language and Priority

Composite Intents may contain different priorities.

Example:

“Get me the cheapest flight, but if that’s unavailable, prioritize nonstop.”

Intent Language may represent:

Primary Objective:
minimize price
Secondary Preference:
nonstop

Priority must not be inferred casually where it materially affects execution.

⸻

36. Intent Language and Alternatives

Intent Language should support alternative goals where the Actor explicitly permits alternatives.

Example:

“Either renew the card or issue a replacement.”

AlternativeIntent
├── RenewCard
└── ReplaceCard

The alternatives must not be interpreted as:

RenewCard AND ReplaceCard

⸻

37. Intent Language and Conditional Intent

Conditional expressions should retain their condition.

Example:

“If the payment fails, retry it.”

Condition:
Payment.Failed
Intent:
RetryPayment

The condition is part of the semantic composition.

⸻

38. Intent Language and Negation

Negation must be represented explicitly.

Example:

“Don’t send the invoice to John.”

This is not simply:

SendInvoice

with missing data.

It may represent:

Constraint:
Recipient != John

or, depending on context:

ProhibitedIntent:
SendInvoice(to = John)

The distinction must be determined by the surrounding Intent.

⸻

39. Intent Language and Quantification

Natural language can specify quantity or scope.

Examples:

“Delete all inactive projects.”

Action:
DeleteProject
Scope:
all
Filter:
State = Inactive

“Delete this project.”

Scope:
single Resource

Quantification is therefore part of semantic intent.

⸻

40. Intent Language and Scope

Scope should be explicit where relevant.

Examples:

Resource scope:
single entity
Collection scope:
all matching entities
Organizational scope:
entire workspace

This prevents dangerous expansion of an Actor’s request.

For example:

“Delete this user.”

must not become:

Delete all users

because a downstream system interpreted the request too broadly.

⸻

41. Intent Language and Defaults

Defaults may be used only where they are canonical and safe.

Example:

User:
"Create a project."

If the system defines a default project visibility:

Visibility:
Private

that may be applied without clarification.

But a material parameter should not be silently defaulted simply because the Model has a plausible value.

⸻

42. Intent Language and Inference

Noema may infer semantic information from evidence.

For example:

“Renew the card I used yesterday.”

If transaction history identifies one card:

Resource:
Card#123

the inference may be valid.

But inferred information should remain distinguishable from explicitly expressed information where provenance matters.

Conceptually:

Value:
Card#123
Source:
TransactionHistory

⸻

43. Provenance

Every materially inferred component should ideally have provenance.

Example:

Resource:
Card#123
Provenance:
"card I used yesterday"
→ Transaction#789
→ Card#123

This supports:

auditability
debugging
clarification
trust

and allows Noema to explain why it interpreted an expression a certain way.

⸻

44. Intent Language and Grounding

An Intent is grounded when its references resolve to canonical concepts or actual domain objects.

Ungrounded:

"Renew that thing."

Grounded:

RenewCard(Card#123)

Grounding is therefore a key transition between:

linguistic representation

and:

executable semantic representation

⸻

45. Intent Language and Domain Independence

The language should define universal semantic primitives without forcing every domain into the same vocabulary.

For example:

Actor
Resource
Constraint
Outcome

are broadly applicable.

But:

Card
Subscription
Invoice
Shipment

are domain concepts.

Noema should support domain-specific ontologies while maintaining a common semantic foundation.

⸻

46. Intent Language and Domain Extensions

A domain can extend the canonical language.

Example:

Core:
Actor
Intent
Resource
Constraint
Outcome
Payments domain:
Payment
Refund
Settlement
Chargeback

The domain vocabulary must remain compatible with the canonical ontology.

⸻

47. Intent Language Should Be Typed

Semantic concepts should be typed wherever possible.

Instead of:

resource = "123"

prefer conceptually:

resource = Card#123

This allows Noema to distinguish:

Card#123
Customer#123
Invoice#123

even when identifiers happen to be identical.

Typing reduces semantic collisions.

⸻

48. Intent Language and Relationships

Relationships between concepts should be explicit.

Example:

Actor:
Alice
owns
Card#123

Then:

Intent:
RenewCard(Card#123)

Relationships provide grounding and support resolution.

⸻

49. Intent Language and Canonical Serialization

Noema will eventually need a machine-readable representation of Intent Language.

The exact serialization format may be:

JSON
YAML
Protocol Buffers
DSL

or another format.

However:

Serialization is an implementation decision; semantic meaning is canonical.

The repository should define the semantics before committing to a transport format.

⸻

50. Example Canonical Representation

A conceptual representation might look like:

Intent {
    actor: User#123,
    objective: RenewCard,
    resources: [
        Card#456
    ],
    context: {
        reason: Expired
    },
    constraints: [
        preserve_billing_relationships
    ],
    expected_outcome: {
        card_state: Active
    }
}

This is an example of the language, not a final API schema.

⸻

51. Example: Simple Intent

Human:

“Cancel my subscription.”

Canonical meaning:

Intent
├── Actor: CurrentUser
├── Objective: CancelSubscription
├── Resource: CurrentSubscription
└── Outcome: SubscriptionCancelled

⸻

52. Example: Ambiguous Intent

Human:

“Cancel my subscription.”

Context:

Subscription#1
Subscription#2

Canonical state:

Intent
├── Actor: CurrentUser
├── Objective: CancelSubscription
├── Resource:
│   ├── Subscription#1
│   └── Subscription#2
│
└── State: Ambiguous

Clarification is required.

⸻

53. Example: Composite Intent

Human:

“Refund the payment and email the customer.”

CompositeIntent
├── RefundPayment
│   ├── Resource: Payment#123
│   └── Outcome: PaymentRefunded
│
└── NotifyCustomer
    ├── Resource: Customer#456
    └── Outcome: CustomerNotified

Relationship:

RefundPayment
    PRECEDES
NotifyCustomer

if the Actor’s wording or domain semantics require notification only after refund completion.

⸻

54. Example: Conditional Intent

Human:

“If the payment fails, retry it.”

CompositeIntent
Condition:
Payment.Failed
Intent:
RetryPayment
Relationship:
CONDITIONAL_ON

⸻

55. Example: Contextual Intent

Previous:

“Create a project called Noema.”

Current:

“Add Sarah to it.”

Intent:
AddMember
Actor:
CurrentUser
Resource:
Project#Noema
Entity:
Sarah
Context:
Project#Noema ← previous Intent

⸻

56. Example: Constraint-Rich Intent

Human:

“Book me the cheapest nonstop flight to London next Friday, leaving after 2 PM.”

Intent:
BookFlight
Destination:
London
Date:
NextFriday
Constraints:
    stops = 0
    departure >= 14:00
Preference:
    minimize_price

The natural-language sentence has been transformed into explicit semantic structure.

⸻

57. Example: Outcome-Oriented Intent

Human:

“Make sure I can access my account again.”

Possible semantic representation:

Intent:
RestoreAccountAccess
ExpectedOutcome:
AccountAccessible

The system may later determine whether the appropriate Action is:

UnlockAccount
ResetPassword
RestoreAccount

The Intent remains independent of that implementation decision.

⸻

58. Canonical Intent Lifecycle

Intent Language should support the complete semantic lifecycle:

EXPRESSED
    ↓
INTERPRETED
    ↓
GROUNDED
    ↓
RESOLVED
    ↓
EXECUTABLE

with possible branches:

INTERPRETED
    ↓
AMBIGUOUS
    ↓
CLARIFICATION
    ↓
RESOLVED

and:

RESOLVED
    ↓
CONTRADICTED

if later authoritative information invalidates the interpretation.

⸻

59. Intent Language and Noema’s Trust Boundary

Intent Language establishes what the Actor is asking.

Trust determines whether Noema should permit the corresponding execution.

Therefore:

Intent Language
      ↓
"What does the Actor mean?"
      ↓
Trust
      ↓
"May this Intent be executed?"

These questions must not be conflated.

⸻

60. Canonical Principles

1. Intent Language represents meaning, not wording.

2. Intent Language is independent of implementation.

3. Intent is distinct from Action.

4. Intent is distinct from Capability.

5. Intent is goal-oriented.

6. Material semantic references should be explicitly grounded.

7. Ambiguity must remain representable.

8. Confidence is metadata, not semantic meaning.

9. Constraints and Preferences must remain distinguishable.

10. Policy constrains Intent execution but does not redefine Actor intent.

11. Composite Intents must preserve constituent Intent identity.

12. Semantic relationships must be explicit.

13. Intent Language should be typed.

14. Domain-specific concepts may extend the canonical vocabulary.

15. Serialization is implementation; semantics are canonical.

⸻

61. What Intent Language Protects Against

Intent Language protects Noema from:

Natural-language drift
Model-dependent execution
Repeated interpretation
Ambiguous API mapping
Loss of constraints
Loss of Context
Loss of Actor identity
Loss of desired Outcomes
Hidden assumptions
Implementation coupling

Most importantly, it prevents the system from treating:

"What the human said"

and:

"What the system should execute"

as the same representation.

⸻

62. What Intent Language Does Not Do

Intent Language does not:

authorize execution
execute Actions
select infrastructure
replace Policy
replace Capabilities
guarantee correctness
eliminate ambiguity
define business state

It provides the canonical semantic representation upon which those systems operate.

⸻

63. The Core Architectural Boundary

Noema’s semantic architecture can therefore be expressed as:

┌───────────────────────────────┐
│       Human Expression        │
│                               │
│ "Renew my expired card."      │
└───────────────┬───────────────┘
                │
                ▼
        Interpretation
                │
                ▼
┌───────────────────────────────┐
│        Intent Language        │
│                               │
│ Actor                         │
│ Objective                     │
│ Resource                      │
│ Context                       │
│ Constraints                   │
│ Expected Outcome              │
└───────────────┬───────────────┘
                │
                ▼
        Resolution / Grounding
                │
                ▼
┌───────────────────────────────┐
│       Executable Intent       │
└───────────────┬───────────────┘
                │
                ▼
             Trust
                │
                ▼
┌───────────────────────────────┐
│            Action             │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│           Outcome             │
└───────────────────────────────┘

⸻

64. Final Definition

Intent Language is Noema’s canonical semantic language for representing an Actor’s intended objective, its relevant Resources, Context, Constraints, relationships, and expected Outcome independently of natural-language wording and execution implementation.

The shortest canonical formulation is:

Natural language expresses intent. Intent Language makes that intent explicit, typed, grounded, and executable without turning meaning into implementation.