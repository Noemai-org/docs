Intent Model

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-model.md

⸻

1. Definition

The Intent Model is Noema’s canonical structural model for representing an Actor’s intended Outcome as a typed, contextual, constrained, and resolvable semantic object.

The Intent Model defines what an Intent contains.

It does not define:

* how natural language is interpreted — see intent-language.md
* how ambiguity is resolved — see intent-ambiguity.md
* how clarification occurs — see clarification.md
* how confidence is evaluated — see confidence.md
* how an Intent progresses through time — see intent-lifecycle.md
* how execution is performed — see the Action and Capability ontology

The Intent Model is the structural foundation connecting these systems.

⸻

2. The Core Idea

Noema must not represent an Intent as:

"Renew my card"

or merely as:

RenewCard(Card#123)

That representation loses information that may be necessary for Trust, clarification, execution, and Outcome verification.

The canonical model is closer to:

Intent
├── Identity
├── Actor
├── Objective
├── Resources
├── Context
├── Constraints
├── Preferences
├── Expected Outcome
├── Relationships
├── Provenance
└── Lifecycle State

The exact implementation may evolve.

The semantic structure must remain stable.

⸻

3. Intent as a Semantic Object

An Intent is a first-class object in Noema.

Conceptually:

Intent {
    identity
    actor
    objective
    resources
    context
    constraints
    preferences
    outcome
    relationships
    provenance
    state
}

This means an Intent can be:

created
updated
clarified
resolved
authorized
executed
observed
completed
rejected
cancelled

without losing its identity.

⸻

4. Intent Is Not an Action

This distinction is foundational.

An Intent represents:

what the Actor wants accomplished

An Action represents:

what the system does to produce that result

Example:

Intent:
Make my expired card usable again.
Possible Actions:
├── VerifyCard
├── RenewCard
└── ReplaceCard

The Intent remains stable even if the Action strategy changes.

⸻

5. Intent Is Not an Outcome

An Intent describes the Actor’s desired objective.

An Outcome describes the resulting condition.

Example:

Intent:
RenewCard
Expected Outcome:
Card is active and usable

Therefore:

Intent → seeks Outcome

rather than:

Intent = Outcome

⸻

6. Intent Is Not Business State

Noema owns Intent State.

The domain system owns Business State.

Example:

Intent:
RenewCard(Card#123)
Intent State:
EXECUTING
Card State:
EXPIRED

Later:

Intent State:
COMPLETED
Card State:
ACTIVE

Noema observes the Card State to determine whether the expected Outcome has been achieved.

⸻

7. Intent Identity

Every Intent must have a stable identity.

Conceptually:

IntentID

Example:

Intent#7f31

Identity allows Noema to correlate:

conversation
clarifications
state transitions
Actions
authorization decisions
execution attempts
Outcomes
audit events

with the same semantic Intent.

⸻

8. Intent Version

An Intent may change over time.

Therefore the model should distinguish:

Intent Identity

from:

Intent Version

Example:

Intent#123:v1
Intent#123:v2
Intent#123:v3

If the Actor says:

“Actually, make that tomorrow.”

the Intent may become:

Intent#123:v2

rather than silently mutating historical state.

⸻

9. Actor

Every Intent has an Actor.

Intent
└── Actor

The Actor answers:

Who intends this Outcome?

Example:

Actor:
User#123

The Actor may be:

human
organization
system
agent
authorized delegate

depending on the domain.

Actor identity may influence:

authority
permissions
preferences
Policy
available Resources

⸻

10. Objective

The Objective represents the central semantic goal.

Examples:

RenewCard
CancelSubscription
TransferFunds
CreateProject
UpdateAddress
NotifyCustomer

The Objective should come from the canonical ontology wherever a corresponding concept exists.

It should not be an arbitrary Model-generated phrase.

⸻

11. Objective vs Natural-Language Expression

Consider:

“Can you get my account working again?”

The expression is linguistic.

The Objective might resolve to:

RestoreAccountAccess

The original wording should remain available through provenance, but the canonical Intent should use the semantic concept.

⸻

12. Resources

Resources identify the domain objects affected by the Intent.

Example:

Intent:
RenewCard
Resource:
Card#123

Resources may include:

primary resource
source resource
destination resource
related resources
collection resources

The exact roles depend on the Intent.

⸻

13. Entity References

An Intent may reference Entities that are not themselves the primary Resource.

Example:

“Send the invoice to Sarah.”

Resource:
Invoice#123
Entity:
Sarah#456

The distinction matters because:

Resource

is an object being operated upon, while:

Entity

may be a participant, reference, destination, owner, recipient, or other semantic object.

⸻

14. Context

Context contains information required to interpret the Intent correctly.

Example:

Conversation:
"Create a project called Noema."
Follow-up:
"Add Sarah to it."

The second Intent can resolve:

project = Noema

through conversational Context.

Context may include:

conversation context
session context
environment context
temporal context
domain context
Actor context
system context

⸻

15. Context Is Not Intent

Context helps determine what an Intent means.

It is not necessarily part of what the Actor explicitly requested.

Example:

Context:
CurrentWorkspace = Engineering
Intent:
CreateProject("Noema")

The workspace grounds the Intent but is not necessarily the Objective.

⸻

16. Constraints

Constraints define boundaries the resulting execution must respect.

Example:

“Transfer $500 to savings, but don’t use my emergency account.”

Intent:
TransferFunds
Amount:
$500
Destination:
Savings
Constraint:
Source != EmergencyAccount

Constraints are semantically significant.

They must not be discarded during planning.

⸻

17. Preferences

Preferences express desirable properties that may be relaxed under defined conditions.

Example:

“I’d prefer the cheapest flight.”

Preference:
MinimizePrice

Compare:

“The flight must cost less than $500.”

Constraint:
Price <= $500

Noema must preserve this distinction.

⸻

18. Constraints vs Preferences

A useful conceptual hierarchy is:

Hard Constraint
    ↓
Must be satisfied
Soft Constraint / Preference
    ↓
Should be satisfied where possible

The system must not convert a Preference into a mandatory Constraint without justification.

Likewise, it must not weaken an explicit Constraint into a Preference.

⸻

19. Expected Outcome

The Expected Outcome describes what the Actor expects to be true after successful satisfaction.

Example:

Intent:
RenewCard
Expected Outcome:
Card.State = Active

The Outcome provides the semantic completion criterion.

⸻

20. Outcome Verification

Noema should distinguish:

Expected Outcome

from:

Observed Outcome

Example:

Expected:
Card.State = Active
Observed:
Card.State = Active

Only after appropriate verification should the Intent become:

COMPLETED

⸻

21. Provenance

Every significant component of an Intent should have provenance where practical.

Example:

Resource:
Card#123
Provenance:
Actor expression:
"the card I used yesterday"
Evidence:
Transaction#789

Provenance allows Noema to answer:

Why does Noema believe this is what the Actor meant?

⸻

22. Explicit vs Inferred Values

The Intent Model should distinguish between information:

explicitly provided

and information:

inferred from Context or evidence

Example:

“Renew my card.”

Explicit:

Objective = RenewCard

Potentially inferred:

Resource = Card#123

if the Actor has only one eligible card.

This distinction becomes important for Trust and clarification.

⸻

23. Confidence Is Metadata

Confidence should not redefine the Intent.

Conceptually:

Intent:
RenewCard(Card#123)
Confidence:
0.96

The confidence value describes the interpretation process.

It is not itself a semantic component of:

RenewCard(Card#123)

See confidence.md.

⸻

24. Intent State

The Intent Model includes lifecycle state as metadata about the Intent.

Example:

Intent:
RenewCard(Card#123)
State:
RESOLVED

State is defined by intent-lifecycle.md.

The model should reference the lifecycle rather than redefine it.

⸻

25. Relationships

Intent components may have semantic relationships.

Example:

TransferFunds
    PRECEDES
CloseAccount

or:

NotifyCustomer
    DEPENDS_ON
RefundPayment

Relationships become especially important for Composite Intents.

⸻

26. Composite Intents

An Intent may contain multiple constituent Intents.

Example:

“Transfer my remaining balance and close the account.”

Intent#123
├── TransferBalance
└── CloseAccount

The parent is a Composite Intent.

Each child retains its own semantic identity.

⸻

27. Composite Intent Structure

Conceptually:

CompositeIntent {
    identity
    actor
    intents[]
    relationships[]
    constraints[]
    expected_outcome
}

Example:

CompositeIntent:
CloseAccount
Children:
├── TransferBalance
└── CloseAccount
Relationship:
TransferBalance PRECEDES CloseAccount

⸻

28. Conditional Intents

An Intent may be conditional.

Example:

“If the payment fails, retry it.”

Conceptually:

ConditionalIntent {
    condition:
        Payment.Failed
    intent:
        RetryPayment
}

The condition must remain explicit.

⸻

29. Alternative Intents

An Actor may explicitly allow alternatives.

Example:

“Either renew my card or replace it.”

AlternativeIntent
├── RenewCard
└── ReplaceCard

The alternatives represent mutually acceptable ways of satisfying the Actor’s objective.

Noema must not automatically execute both.

⸻

30. Negated Intent and Prohibition

The Intent Model must support negative semantic constraints.

Example:

“Don’t use my emergency account.”

Constraint:
Source != EmergencyAccount

Negation should not be represented merely as absent data.

It must be explicit where it materially constrains execution.

⸻

31. Quantification

The model must support scope and quantity.

Example:

“Delete all inactive projects.”

Objective:
DeleteProject
Scope:
All
Filter:
State = Inactive

Compare:

“Delete this project.”

Scope:
Single
Resource:
Project#123

This distinction is critical for preventing unintended scope expansion.

⸻

32. Temporal Semantics

An Intent may contain temporal information.

Examples:

Date:
2026-08-28
Deadline:
2026-08-30
Before:
17:00
Recurring:
Every Monday

Temporal information belongs in the Intent where it affects the Actor’s desired Outcome or execution constraints.

⸻

33. Location Semantics

Where relevant, Intent may contain geographic or logical location.

Example:

“Find me a hotel near the conference venue.”

Objective:
FindHotel
Context:
ConferenceVenue = X
Constraint:
Distance <= 2km

Location should be represented semantically rather than retained only as raw language.

⸻

34. Numeric and Scalar Values

Values should be typed.

Instead of:

amount = "500"

the semantic model should distinguish:

amount:
    value = 500
    currency = USD

Similarly:

duration
distance
percentage
quantity
timestamp

should retain their semantic types.

⸻

35. Optionality

Not every field is required for every Intent.

For example:

RenewCard

may require:

Actor
Objective
Resource

while:

NotifyCustomer

may require:

Actor
Objective
Recipient
Message

The required structure is determined by the canonical Intent type and its domain definition.

⸻

36. Required vs Unknown

The model must distinguish:

known

from:

unknown

and:

not applicable

Example:

destination:
UNKNOWN

is different from:

destination:
NOT_APPLICABLE

This prevents missing information from being silently interpreted as irrelevant information.

⸻

37. Null Is Not Ambiguity

An absent field does not necessarily mean ambiguity.

For example:

flight_number:
NOT_APPLICABLE

is different from:

flight_number:
UNKNOWN

and different again from:

flight_number:
AMBIGUOUS

The Intent Model should preserve these semantic distinctions.

⸻

38. Semantic Completeness

An Intent is semantically complete when all information necessary to determine its meaning is available.

This does not necessarily mean every possible field is populated.

For example:

Intent:
CreateProject("Noema")

may not require:

description
logo
billing_plan

if those are optional.

Semantic completeness is therefore determined by the Intent’s schema and domain semantics.

⸻

39. Executability

An Intent becomes executable when:

meaning is resolved
+
required Resources are grounded
+
required Constraints are known
+
appropriate Capability exists
+
execution prerequisites are satisfied

But:

Executable ≠ Authorized

Authorization remains a separate Trust decision.

⸻

40. Capability Binding

An Intent may be associated with one or more Capabilities capable of satisfying it.

Example:

Intent:
NotifyCustomer
Candidate Capabilities:
├── SendEmail
├── SendSMS
└── SendPush

The Intent should not become tightly coupled to a specific Capability merely because one implementation is currently preferred.

⸻

41. Action Planning

The Intent Model does not prescribe the exact Actions required.

Example:

Intent:
RestoreAccountAccess

Potential execution:

VerifyIdentity
    ↓
ResetPassword
    ↓
InvalidateSessions
    ↓
VerifyAccess

The Action sequence is an execution concern.

The Intent Model defines the semantic objective that the sequence must satisfy.

⸻

42. Intent and Execution Plan

These are separate objects.

Intent
   ↓
Execution Plan
   ↓
Actions

The Execution Plan may change without changing the Actor’s Intent.

This separation is essential for implementation flexibility.

⸻

43. Canonical Conceptual Schema

A useful conceptual representation is:

Intent {
    id: IntentID
    version: Version
    actor: Actor
    objective: Concept
    resources: [
        Resource
    ]
    entities: [
        Entity
    ]
    context: Context
    constraints: [
        Constraint
    ]
    preferences: [
        Preference
    ]
    expected_outcome: Outcome
    relationships: [
        Relationship
    ]
    provenance: Provenance
    state: IntentState
}

This is conceptual, not a commitment to a specific serialization format.

⸻

44. Minimal Intent

The smallest meaningful Intent should contain enough information to answer:

Who wants what?

Conceptually:

Intent {
    actor
    objective
}

Example:

Actor:
User#123
Objective:
CreateProject

Additional fields are added as required by the specific Intent.

⸻

45. Fully Grounded Intent

A fully grounded Intent might look conceptually like:

Intent {
    id: Intent#123
    actor:
        User#456
    objective:
        RenewCard
    resources:
        Card#789
    context:
        reason = Expired
    constraints:
        preserve_billing_relationship = true
    expected_outcome:
        Card#789.state = Active
    provenance:
        resource_resolution = Transaction#555
    state:
        RESOLVED
}

This is sufficiently explicit for downstream Trust and execution processing.

⸻

46. Example: “Renew My Card”

Natural language:

“Please renew my card.”

Initial representation:

Intent {
    actor: User#123
    objective: RenewCard
    resource: UNKNOWN
}

If the user has one eligible card:

Intent {
    actor: User#123
    objective: RenewCard
    resource: Card#456
}

If the user has multiple eligible cards:

Intent {
    actor: User#123
    objective: RenewCard
    resource:
        Card#456
        Card#789
    state:
        AMBIGUOUS
}

The model therefore directly supports Noema’s clarification architecture.

⸻

47. Example: “Renew the Card I Used Yesterday”

Intent {
    actor:
        User#123
    objective:
        RenewCard
    resource:
        Card#456
    context:
        usage_reference:
            yesterday
    provenance:
        Card#456
            ← Transaction#789
            ← "used yesterday"
    expected_outcome:
        Card#456.state = Active
}

The linguistic reference has become a grounded semantic reference.

⸻

48. Example: “Transfer $500 to Savings”

Intent {
    actor:
        User#123
    objective:
        TransferFunds
    resources:
        source = Checking#1
        destination = Savings#2
    constraints:
        amount = 500 USD
    expected_outcome:
        Savings#2.balance += 500 USD
}

If the source account is ambiguous:

state = AMBIGUOUS

⸻

49. Example: Composite Intent

“Refund the payment and email me the receipt.”

CompositeIntent {
    actor:
        User#123
    intents: [
        Intent {
            objective:
                RefundPayment
            resource:
                Payment#456
        },
        Intent {
            objective:
                SendReceipt
            resource:
                Payment#456
        }
    ]
    relationship:
        RefundPayment
            PRECEDES
        SendReceipt
}

⸻

50. Intent Model and Canonical Ontology

The Intent Model depends on the ontology defined elsewhere in the repository.

For example:

Actor
Capability
Concept
Constraint
Context
Entity
Outcome
Policy
Relationship
Resource
State

should have canonical definitions.

The Intent Model composes those primitives.

It should not redefine them.

⸻

51. Intent Model and Intent Language

intent-language.md answers:

How does Noema represent meaning?

intent-model.md answers:

What structural components constitute an Intent?

The distinction is:

Intent Language
    = semantic language
Intent Model
    = semantic structure

⸻

52. Intent Model and Intent Ambiguity

intent-ambiguity.md determines when the structure contains materially unresolved alternatives.

For example:

resource:
{
    candidate_a,
    candidate_b
}

The Intent Model allows the representation.

The Ambiguity specification determines:

whether the difference is material

and:

whether clarification is required

⸻

53. Intent Model and Confidence

confidence.md determines how Noema represents evidence about interpretation quality.

The Intent Model provides the object being evaluated.

Therefore:

Intent
   +
Evidence
   +
Confidence

must remain conceptually distinct.

⸻

54. Intent Model and Lifecycle

intent-lifecycle.md determines how the Intent transitions between states.

The Intent Model contains or references the current state.

Therefore:

Intent Model
    ↓
Intent State
    ↓
Lifecycle Rules

⸻

55. Intent Model and Trust

The Trust Engine consumes the resolved Intent.

Conceptually:

Intent Model
      ↓
Resolved Intent
      ↓
Trust Evaluation
      ↓
Authorized / Rejected

Trust should not modify the Actor’s original objective merely to make execution easier.

⸻

56. Intent Model and Determinism

Noema’s deterministic boundary depends on the Intent Model being explicit enough to support deterministic decisions.

The Model may generate:

candidate Intent

Noema should determine:

whether it is sufficiently complete
whether it is ambiguous
whether it satisfies semantic requirements
whether it can proceed

This is one of the primary reasons the Intent Model must be canonical.

⸻

57. Intent Model Invariants

Invariant 1

Every Intent has an Actor or an explicitly defined system-level origin.

Invariant 2

Every Intent has a canonical Objective.

Invariant 3

Material Resources must be grounded before execution.

Invariant 4

Material ambiguity must be representable.

Invariant 5

Constraints must not be silently discarded.

Invariant 6

Preferences must not silently become hard Constraints.

Invariant 7

Expected Outcomes must remain distinct from Actions.

Invariant 8

Intent State must remain distinct from Business State.

Invariant 9

Intent identity must survive lifecycle transitions.

Invariant 10

Execution implementation must remain replaceable without changing the Intent’s semantic identity.

⸻

58. What the Intent Model Protects Against

Without a canonical model, different parts of Noema may interpret the same request differently.

The Intent Model protects against:

semantic drift
implicit assumptions
lost constraints
lost context
untyped references
implementation coupling
ambiguous execution
unverifiable completion
model-dependent state

It gives every downstream subsystem the same semantic object to operate on.

⸻

59. The Architectural Role

The Intent Model sits at the center of Noema’s architecture:

                 Human Expression
                        │
                        ▼
               Interpretation
                        │
                        ▼
              ┌─────────────────┐
              │   INTENT MODEL   │
              │                 │
              │ Actor           │
              │ Objective       │
              │ Resources       │
              │ Context         │
              │ Constraints     │
              │ Outcome         │
              │ Provenance      │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Resolution          Trust
              │                 │
              └────────┬────────┘
                       ▼
                   Execution
                       │
                       ▼
                    Outcome

The Intent Model is therefore the semantic contract connecting interpretation to execution.

⸻

60. Final Definition

The Intent Model is Noema’s canonical structural representation of an Actor’s intended objective, including the Resources, Entities, Context, Constraints, Preferences, expected Outcome, relationships, provenance, and lifecycle state required to resolve, govern, execute, and verify that Intent.

The shortest canonical formulation is:

An Intent is a first-class, typed semantic object that captures who wants what, what it concerns, under which conditions, toward which Outcome, and with what evidence—without coupling that meaning to how the system eventually executes it.