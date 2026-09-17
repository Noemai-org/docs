Intent Language

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-language.md

⸻

1. Definition

Intent Language is the canonical semantic language Noema uses to represent what an Actor means to accomplish, independently of the natural-language expression used to communicate it and independently of the implementation used to satisfy it.

Natural language is an input representation.

Intent Language is the canonical semantic representation.

Actions are execution representations.

The fundamental transformation is:

Natural Language
      ↓
Interpretation
      ↓
Intent Language
      ↓
Resolution / Grounding
      ↓
Executable Intent
      ↓
Trust
      ↓
Action
      ↓
Verification
      ↓
Outcome

Intent Language therefore forms the semantic boundary between Actor expression and deterministic system execution.

⸻

2. Why Intent Language Exists

Actors communicate through language that may be:

* ambiguous
* contextual
* implicit
* variable
* incomplete
* probabilistic

Enterprise systems execute through structures that must be:

* typed
* explicit
* bounded
* validated
* deterministically evaluable

Noema requires an intermediate semantic representation that preserves the meaning of the Actor without requiring downstream systems to repeatedly interpret natural language.

Without such a representation:

Actor
  ↓
Model
  ↓
API Call

the interpretation layer effectively becomes part of the execution path.

Noema instead establishes:

Actor Expression
      ↓
Interpretation
      ↓
Intent Language
      ↓
Resolution
      ↓
Executable Intent
      ↓
Trust
      ↓
Bounded Action
      ↓
Execution

The purpose of Intent Language is therefore to preserve semantic intent across the boundary between interpretation and execution.

⸻

3. Intent Language Is Not a Programming Language

Intent Language should not be confused with a general-purpose programming language.

It does not primarily describe:

* loops
* variables
* memory
* algorithms
* data structures
* implementation control flow

It describes semantic commitments such as:

* who intends the Outcome
* what objective is intended
* which Resources are relevant
* which Context grounds the expression
* which Constraints apply
* which Preferences apply
* which relationships exist
* which Outcome is expected

Its semantic unit is Intent, not computation.

⸻

4. Intent Language Is Not Natural Language

Natural language expresses meaning through words, references, context, implication, and linguistic structure.

For example:

"Can you sort out my card? It's the one I used yesterday."

Intent Language may represent:

Intent:
    ResolveCardIssue
Actor:
    CurrentUser
Resource:
    unresolved
    candidates ← transaction history
Context:
    temporal_reference = yesterday
Objective:
    resolve card issue
Expected Outcome:
    card issue resolved

The exact wording may disappear.

The semantic commitments must not.

Therefore:

Intent Language is meaning-preserving,
not wording-preserving.

⸻

5. Intent Language Is Not an API Contract

An API contract may specify:

POST /cards/{id}/replacement

with parameters such as:

card_id
reason
shipping_address

That is an execution interface.

Intent Language instead represents the semantic objective:

Objective:
    ReplaceCard
Resource:
    Card#123

The Capability that satisfies the Intent may later map this representation to one or more APIs or enterprise operations.

Therefore:

Intent Language
        ≠
API Schema

⸻

6. Intent Language Is Not a Workflow DSL

A workflow DSL typically describes execution sequence:

Step A
  ↓
Step B
  ↓
Step C

Intent Language describes semantic objectives and relationships.

For example:

"Transfer my balance and close the account."

may produce:

Intent A:
    TransferBalance
Intent B:
    CloseAccount
Relationship:
    TransferBalance PRECEDES CloseAccount

The semantic relationship is represented.

Intent Language does not prescribe:

HTTP request A
wait 2 seconds
HTTP request B
retry 3 times

Those are execution concerns.

Composition may establish dependencies, ordering, conditions, or alternatives, but the Planner determines the bounded implementation sequence within the available Enterprise Action Graph, Capability Registry, Action Registry, and Action Contracts.

⸻

7. The Core Semantic Vocabulary

Intent Language is built from concepts defined by Noema’s ontology.

At minimum:

Actor
Intent
Objective
Action
Capability
Resource
Entity
Context
Constraint
Preference
Policy
State
Outcome
Relationship

These concepts must have stable meanings across Noema.

Not every Intent requires every field.

The required semantic structure depends on the domain, action, consequence, and resolution requirements.

⸻

8. The Core Intent Form

Conceptually:

Intent =
    Actor
    + Objective
    + Resources
    + Context
    + Constraints
    + Preferences
    + Relationships
    + Expected Outcome

A more expressive conceptual representation is:

Intent {
    actor
    objective
    resources
    context
    constraints
    preferences
    relationships
    expected_outcome
}

This is a semantic model, not necessarily the final wire format.

Fields may remain unresolved during interpretation and resolution.

Materially unresolved fields prevent the Intent from becoming Executable Intent.

⸻

9. Actor

The Actor identifies who intends the Outcome.

Example:

Actor:
    User#123

Intent Language must preserve Actor identity because:

* authority
* ownership
* permissions
* preferences
* policy applicability
* scope

may depend on the Actor.

An Intent whose Actor is materially unresolved cannot become Executable Intent merely because the remaining fields are clear.

Actor resolution does not itself establish authorization.

Technical authorization, policy authorization, and business authorization remain distinct Trust concerns.

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

The latter is an execution representation.

⸻

11. Resources

Resources identify the objects affected by or relevant to an Intent.

Example:

Intent:
    RenewCard
Resource:
    Card#123

Resources may be:

* explicitly referenced
* resolved through Context
* resolved through State Reconciliation
* produced by another Intent
* established through authoritative enterprise relationships

But material Resources must be resolved before the Intent becomes Executable Intent.

An identifier alone is not sufficient when its type, scope, existence, ownership, or current state is material.

⸻

12. Context

Context provides information necessary to interpret or ground an Intent.

Example:

Intent:
    "Add Sarah."
Context:
    CurrentProject = Noema

The semantic representation may therefore become:

AddMember(
    project = Noema,
    member = Sarah
)

Context should not be confused with Intent itself.

Context provides semantic grounding.

Context is not automatically authoritative. Its authority, scope, freshness, and Fact Status must be evaluated where they materially affect resolution or Trust.

State Reconciliation may transform contextual observations into sufficiently established facts for deterministic use.

⸻

13. Constraints

Constraints restrict how the Intent may be satisfied.

Example:

"Book the cheapest nonstop flight."

may produce:

Intent:
    BookFlight
Constraints:
    nonstop = true
Preference:
    minimize_price

Constraints are part of the semantic specification when established by the Actor or otherwise validly incorporated into the Intent.

Constraints must survive resolution and execution planning.

They cannot be silently dropped because a selected Capability does not conveniently support them.

⸻

14. Policy

Policy defines system, enterprise, organizational, or regulatory conditions governing whether an Intent may be satisfied.

Example:

Intent:
    RefundPayment
Policy:
    Refunds above $10,000 require approval.

Policy is not necessarily part of what the Actor wants.

Therefore:

Intent Language
      ↓
Resolution
      ↓
Trust / Policy Evaluation

Policy constrains whether and under what conditions an Intent may proceed without redefining the Actor’s underlying objective.

Policy may restrict or eliminate execution paths.

Policy must not invent an Actor’s Intent.

⸻

15. Expected Outcome

Expected Outcome describes the state or condition the Actor expects to exist if the Intent is successfully satisfied.

Example:

Intent:
    RenewCard
Expected Outcome:
    Card is renewed and usable

This is important because an Intent should not be defined purely as an Action.

Different Actions may satisfy the same semantic Intent.

For example:

Intent:
    RestoreAccountAccess
Possible Actions:
    UnlockAccount
    ResetPassword
    RestoreAccount
Expected Outcome:
    AccountAccessible

Outcome semantics therefore remain distinct from implementation mechanics.

⸻

16. Intent Is Goal-Oriented

Intent Language is fundamentally goal-oriented.

Compare:

"Call POST /renew."

with:

"Make my expired card usable again."

The second expresses an objective.

The system may satisfy it through:

* renewal
* replacement
* reactivation

depending on domain semantics, current State, Policy, available Capabilities, and Trust conditions.

Therefore:

Intent Language describes semantic objectives,
not merely requested operations.

⸻

17. Intent and Action

The distinction must remain strict.

Intent:
    Renew my card.
Action:
    Create replacement card.
Expected Outcome:
    Actor has a valid usable card.

An Intent may result in:

one Action

or:

multiple Actions

The number of Actions does not determine the number of Intents.

Conversely, an Action must not be treated as proof that the original Intent was satisfied.

Verification establishes actual Outcome.

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

* Context
* Constraints
* Policy
* Actor preferences
* available Resources
* current Capability availability

The Intent remains independent of the Capability implementation.

Capability existence does not imply:

* permission
* authorization
* current availability
* suitability
* Trust
* success

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

The same semantic Intent may potentially be satisfied through:

Email
SMS
Push

where permitted.

Capability selection belongs downstream of semantic resolution and within bounded execution architecture.

⸻

20. Intent Language and Domain Ontology

Intent Language should use canonical domain concepts rather than arbitrary Model-generated terminology.

For example, if the ontology defines:

Subscription
CancelSubscription
Customer

Intent Language should reference those canonical concepts.

It should not randomly alternate between:

CancelSubscription
TerminateSubscription
EndPlan
StopMembership

unless those represent genuinely distinct concepts.

This provides semantic consistency across interpretation, resolution, Trust, execution, audit, and Operational Memory.

⸻

21. Canonical Vocabulary

Intent Language should maintain a controlled vocabulary for concepts such as:

* Objectives
* Actions
* Entities
* Resources
* Capabilities
* Constraints
* Preferences
* States
* Outcomes
* Relationships

Natural-language expressions can vary indefinitely.

Canonical semantic concepts should not vary without an explicit ontology or vocabulary change.

Canonical vocabulary does not mean every domain uses identical nouns. Domain extensions remain possible within the common semantic foundation.

⸻

22. Synonyms

Different expressions may map to the same semantic Intent.

Example:

"Cancel my subscription."
"Stop my subscription."
"I don't want this subscription anymore."
"End my subscription."

may map to:

Intent:
    CancelSubscription

Intent Language therefore normalizes linguistic variation into canonical semantic concepts.

The normalization must preserve material distinctions where they exist.

Synonyms are not assumed to be equivalent merely because they appear linguistically similar.

⸻

23. Polysemy

The same word may represent different semantic concepts depending on Context.

Example:

"Close the account."

could refer to:

CloseBankAccount
CloseCustomerAccount
CloseInvestmentAccount

Intent Language must therefore be grounded in:

* Context
* Entity
* Resource
* Domain
* Actor
* relevant State

rather than keyword matching.

Where multiple materially valid interpretations remain, the ambiguity must remain explicit until resolved.

⸻

24. Intent Language and Ambiguity

Intent Language does not eliminate ambiguity.

It gives Noema a structured representation in which ambiguity can remain explicit.

For example:

Intent:
    CancelSubscription
Resource:
    unresolved
Candidates:
    Subscription#123
    Subscription#456

The semantic representation is valid as an unresolved Intent, but it is not Executable Intent if the Resource is material.

Therefore:

Natural Language Ambiguity
          ↓
Intent Language
          ↓
Explicit unresolved semantic field
          ↓
Resolution / Clarification

Noema must not silently select one materially valid interpretation merely because it appears more probable.

⸻

25. Intent Language and Confidence

Confidence is evidence about the strength of an interpretation or claim.

It is not itself semantic meaning.

For example:

Intent:
    RenewCard(Card#123)
Confidence:
    0.93

The 0.93 is metadata about the interpretation process.

It does not mean:

RenewCard with 93% semantic meaning

Model confidence is non-authoritative interpretation metadata.

It does not establish:

* Fact Status
* authority
* authorization
* Trust
* Outcome
* semantic resolution

Confidence may support resolution, but deterministic evidence and State Reconciliation establish canonical semantic facts where required.

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
Expected Outcome:
    Resolved

This is a valid semantic representation but not yet Executable Intent.

After resolution:

Resource:
    Card#123

the Intent may become Executable Intent if all other material semantic requirements are satisfied.

Executable Intent does not mean authorized or successful.

Trust must still determine whether the resolved Intent may proceed.

⸻

27. Intent Language and Clarification

Clarification should operate on semantic gaps.

Example:

Intent:
    TransferFunds
Source:
    Resolved
Destination:
    Ambiguous
Amount:
    $500

Noema should ask the smallest question necessary to resolve the material ambiguity:

Which account should receive the $500?

rather than asking the Actor to restate the entire request.

Intent Language therefore enables targeted semantic clarification.

Clarification does not grant authority, establish business truth, or itself constitute execution approval.

A material clarification that changes the semantic meaning of an admitted Intent creates a new Intent version with supersedes; admitted Intent versions remain immutable.

⸻

28. Intent Language and Composition

Intent Language must support Composite Intents and explicit semantic relationships between constituent Intents.

Example:

Composite Intent
├── TransferBalance
└── CloseAccount
Relationship:
    TransferBalance PRECEDES CloseAccount

Composition may express:

* dependency
* precedence
* condition
* alternative
* shared constraint
* shared Context
* outcome dependency
* resource dependency

Composition is semantic structure, not execution workflow.

A composite may contain children that are independently resolved or executable.

Parent-level semantics do not automatically authorize constituent Intents.

⸻

29. Intent Language and Context Continuity

Consider:

"Create a project called Noema."

followed by:

"Add Sarah to it."

Intent Language can preserve the semantic reference:

Intent A:
    CreateProject(Noema)
Intent B:
    AddMember(
        project = Noema,
        member = Sarah
    )

The word it disappears.

Its resolved semantic reference remains.

The reference should be grounded through the relevant prior Intent, Context, or authoritative Resource relationship rather than through uncontrolled conversational memory.

⸻

30. Intent Language and Temporal Continuity

Intent Language must support Intent identity across its lifecycle.

A conceptual lifecycle is:

RECEIVED
    ↓
INTERPRETING
    ↓
VALIDATING
    ↓
ADMITTED
    ↓
RESOLVING
    ↓
RESOLVED
    ↓
EXECUTABLE
    ↓
TRUST_PENDING
    ↓
ACTION
    ↓
EXECUTION
    ↓
VERIFICATION
    ↓
OUTCOME

Possible semantic control states include:

CLARIFICATION_REQUIRED
EXPIRED
CANCELLED
SUPERSEDED

These are not Trust outcomes.

The canonical Intent version remains immutable once admitted. Material semantic changes create a new version.

⸻

31. Intent Language and State

State describes the current condition of an Intent, Resource, execution, or Outcome.

Example:

Intent State:
    RESOLVED
Resource State:
    EXPIRED

The distinction matters.

Intent Language must not confuse:

what the Actor wants

with:

what is currently true

Likewise, an Expected Outcome must not be confused with the Actual Outcome established by verification.

Enterprise business state remains owned by the relevant enterprise systems of record.

⸻

32. Intent Language and Constraints

Constraints should be explicit.

Example:

"Transfer $500 to savings, but don't use my emergency account."

may produce:

Intent:
    TransferFunds
Amount:
    $500
Destination:
    SavingsAccount
Constraint:
    Source != EmergencyAccount

The constraint is part of the semantic specification.

It must remain available to Trust and execution planning and must not be silently relaxed.

⸻

33. Positive and Negative Intent

Intent Language should support both:

* desired conditions
* prohibited conditions

Example:

"Book the cheapest flight, but not one with a layover."

may produce:

Objective:
    BookFlight
Preference:
    minimize_price
Constraint:
    Stops = 0

Negative constraints are still part of the semantic specification.

Where the Actor explicitly prohibits an action or condition, that prohibition must remain explicit rather than being represented as missing information.

⸻

34. Preferences vs Constraints

Not every Actor statement has equal semantic force.

Example:

"I'd prefer an afternoon flight."

may represent a Preference.

Whereas:

"I cannot travel before 2 PM."

represents a Constraint.

Conceptually:

Preference:
    preferred_departure >= 14:00
Constraint:
    departure >= 14:00

A Preference may potentially be relaxed according to the defined semantic model.

A Constraint cannot be relaxed without changing the Intent or otherwise obtaining valid authority to modify it.

Noema must not infer this distinction casually where it materially affects execution.

⸻

35. Intent Language and Priority

Composite Intents may contain explicit priorities.

Example:

"Get me the cheapest flight, but if that's unavailable, prioritize nonstop."

may represent:

Primary Objective:
    minimize price
Secondary Preference:
    nonstop

Priority must not be inferred casually where it materially affects the meaning of the request.

Where priority changes the set of acceptable Outcomes or execution choices, it must be explicitly represented or deterministically resolved.

⸻

36. Intent Language and Alternatives

Intent Language should support alternative goals where the Actor explicitly permits alternatives.

Example:

"Either renew the card or issue a replacement."

may produce:

Alternative
├── RenewCard
└── ReplaceCard

The alternatives must not be interpreted as:

RenewCard AND ReplaceCard

Alternative selection is a semantic decision constrained by the defined conditions, Resources, Policy, and available Capabilities.

The Planner may select among resolved alternatives but may not invent additional alternatives.

⸻

37. Intent Language and Conditional Intent

Conditional expressions should retain their condition.

Example:

"If the payment fails, retry it."

may produce:

Condition:
    Payment.Failed
Intent:
    RetryPayment
Relationship:
    CONDITIONAL_ON

The condition is part of the semantic composition.

Conditions must be deterministically evaluable from defined State, Outcome, evidence, or other explicitly identified inputs.

The Planner must not invent conditions during execution.

⸻

38. Intent Language and Negation

Negation must be represented explicitly.

Example:

"Don't send the invoice to John."

Depending on the surrounding Intent, this may represent:

Constraint:
    Recipient != John

or:

Prohibition:
    SendInvoice(to = John)

The distinction must be resolved from the semantic structure and Context.

Negation must not be silently discarded during normalization.

⸻

39. Intent Language and Quantification

Natural language can specify quantity or scope.

Example:

"Delete all inactive projects."

may produce:

Objective:
    DeleteProject
Scope:
    all matching Resources
Filter:
    State = Inactive

Whereas:

"Delete this project."

may produce:

Scope:
    single Resource

Quantification is therefore part of semantic Intent where it affects the Resource set or Outcome.

⸻

40. Intent Language and Scope

Scope should be explicit where relevant.

Examples include:

single Resource
collection of Resources
all matching Resources
workspace scope
organizational scope

Scope prevents dangerous expansion of the Actor’s request.

For example:

"Delete this user."

must not become:

Delete all users

because a downstream system interpreted the request too broadly.

Material scope must be resolved before Executable Intent.

⸻

41. Intent Language and Defaults

Defaults may be used only where they are canonical and semantically safe.

Example:

"Create a project."

If the system defines a valid default:

Visibility:
    Private

that default may be applied if the parameter is non-material, deterministic, in scope, and compatible with Policy.

A material parameter must not be silently defaulted merely because the Model has a plausible value.

Defaults must not become hidden intent.

⸻

42. Intent Language and Inference

Noema may infer semantic information from valid evidence.

For example:

"Renew the card I used yesterday."

If authoritative transaction history identifies one card, resolution may establish:

Resource:
    Card#123

The inference should remain distinguishable from explicit Actor expression where provenance matters.

Conceptually:

Value:
    Card#123
Source:
    TransactionHistory

Inference does not mean guesswork.

Where evidence does not uniquely establish a material interpretation, the ambiguity remains unresolved.

⸻

43. Provenance

Every materially inferred or resolved component should have provenance where required for auditability and Trust.

Example:

Resource:
    Card#123
Provenance:
    "card I used yesterday"
        ↓
    Transaction#789
        ↓
    Card#123

Provenance supports:

* auditability
* debugging
* clarification
* deterministic resolution
* Trust evaluation
* causal explanation

Provenance does not itself establish authority.

The source of a fact, its Fact Status, scope, freshness, and authority must be evaluated independently.

⸻

44. Intent Language and Grounding

An Intent is grounded when its semantic references resolve to canonical concepts, valid Resources, or authoritative domain relationships as required.

Ungrounded:

"Renew that thing."

Grounded:

RenewCard(Card#123)

Grounding is therefore a key transition between linguistic interpretation and executable semantic representation.

Grounding does not by itself make an Intent Executable Intent.

All material semantic requirements must still be resolved and deterministically evaluable.

⸻

45. Intent Language and Domain Independence

Intent Language should define universal semantic primitives without forcing every domain into the same vocabulary.

For example:

Actor
Resource
Constraint
Outcome
Relationship

are broadly applicable.

Domain concepts may include:

Card
Subscription
Invoice
Shipment
Payment

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
Payments:
    Payment
    Refund
    Settlement
    Chargeback

Domain vocabulary must remain compatible with the canonical ontology.

A domain extension must not silently redefine a core semantic primitive.

⸻

47. Intent Language Should Be Typed

Semantic concepts should be typed wherever possible.

Instead of:

resource = "123"

prefer:

resource = Card#123

This allows Noema to distinguish:

Card#123
Customer#123
Invoice#123

even when identifiers happen to be identical.

Typing reduces semantic collisions and supports deterministic resolution.

⸻

48. Intent Language and Relationships

Relationships between concepts should be explicit where they materially affect interpretation or resolution.

Example:

Actor:
    Alice
Relationship:
    Alice OWNS Card#123

Then:

Intent:
    RenewCard(Card#123)

Relationships provide semantic grounding and support deterministic resolution.

Relationship existence does not itself establish that a requested Action is authorized.

⸻

49. Intent Language and Canonical Serialization

Noema will require a machine-readable representation of Intent Language.

The exact serialization format may be:

JSON
YAML
Protocol Buffers
DSL

or another format.

However:

Serialization = implementation decision
Semantics = canonical

The repository should define semantic meaning before committing to a transport or serialization format.

A wire schema must not become the definition of Intent semantics.

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

This is an example of Intent Language, not a final API schema.

The representation may contain unresolved fields before resolution.

⸻

51. Example: Simple Intent

Human:

"Cancel my subscription."

Canonical semantic representation:

Intent
├── Actor: CurrentUser
├── Objective: CancelSubscription
├── Resource: CurrentSubscription
└── Expected Outcome: SubscriptionCancelled

Whether CurrentSubscription resolves to one actual Resource must be established through Context and State Reconciliation where necessary.

⸻

52. Example: Ambiguous Intent

Human:

"Cancel my subscription."

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
└── Resolution:
    Material ambiguity

Clarification is required if the Resource distinction is material.

Noema must not select one candidate solely because it has higher model confidence.

⸻

53. Example: Composite Intent

Human:

"Refund the payment and email the customer."

Possible semantic composition:

Composite Intent
├── Intent A:
│   ├── Objective: RefundPayment
│   ├── Resource: Payment#123
│   └── Expected Outcome: PaymentRefunded
│
└── Intent B:
    ├── Objective: NotifyCustomer
    ├── Resource: Customer#456
    └── Expected Outcome: CustomerNotified
Relationship:
    RefundPayment PRECEDES NotifyCustomer

The precedence relationship should be represented only when established by the Actor’s semantics or valid domain semantics.

Composition does not itself prescribe the API or execution sequence.

⸻

54. Example: Conditional Intent

Human:

"If the payment fails, retry it."

Semantic composition:

Condition:
    Payment.Failed
Intent:
    RetryPayment
Relationship:
    CONDITIONAL_ON

The condition must be evaluated from the defined Payment state or verified Outcome.

The Planner does not infer a new condition merely because it would be operationally convenient.

⸻

55. Example: Contextual Intent

Previous:

"Create a project called Noema."

Current:

"Add Sarah to it."

Semantic representation:

Intent:
    AddMember
Actor:
    CurrentUser
Resource:
    Project#Noema
Entity:
    Sarah
Context:
    Project#Noema ← resolved conversational reference

The reference to it is normalized into a typed semantic reference.

The reference must be validated against current Context and Resource state before execution.

⸻

56. Example: Constraint-Rich Intent

Human:

"Book me the cheapest nonstop flight to London next Friday, leaving after 2 PM."

Intent Language may represent:

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

The natural-language sentence has been transformed into explicit semantic structure while preserving the distinction between hard Constraints and Preferences.

⸻

57. Example: Outcome-Oriented Intent

Human:

"Make sure I can access my account again."

Possible semantic representation:

Intent:
    RestoreAccountAccess
Expected Outcome:
    AccountAccessible

The system may later determine whether an appropriate bounded Action is:

UnlockAccount
ResetPassword
RestoreAccount

The Intent remains independent of that implementation decision.

The selected Action remains subject to Trust, Action Contract, execution, and verification.

⸻

58. Canonical Intent Lifecycle

Intent Language should support the semantic lifecycle:

EXPRESSED
    ↓
INTERPRETED
    ↓
GROUNDED
    ↓
RESOLVING
    ↓
RESOLVED
    ↓
EXECUTABLE

with possible branches:

INTERPRETED
    ↓
MATERIAL AMBIGUITY
    ↓
CLARIFICATION_REQUIRED
    ↓
NEW INTENT VERSION
    ↓
RESOLVING
    ↓
RESOLVED

and:

RESOLVED
    ↓
CONFLICTING / INVALIDATED EVIDENCE
    ↓
RE-RESOLUTION OR NEW VERSION

Control states such as cancellation and expiry are separate from semantic meaning and Trust outcomes.

An admitted Intent version is immutable.

⸻

59. Intent Language and Noema’s Trust Boundary

Intent Language establishes what the Actor is asking.

Resolution establishes what the Intent means in canonical, grounded form.

Executable Intent establishes that the material semantic requirements are sufficiently resolved for deterministic Trust evaluation.

Trust determines whether the resolved Intent may proceed.

Therefore:

Intent Language
      ↓
"What does the Actor mean?"
      ↓
Resolution
      ↓
"What is the canonical meaning?"
      ↓
Executable Intent
      ↓
Trust
      ↓
"May this resolved Intent proceed?"

These questions must not be conflated.

Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

EXECUTE does not mean execution succeeded.

Actual success or failure is established through Execution and Verification.

⸻

60. Intent Language and State Reconciliation

Intent Language may contain references whose resolution depends on multiple enterprise systems.

For example:

"Find the payment that disappeared yesterday."

Resolving the semantic reference may require reconciliation across:

Customer
    ↓
Payment
    ↓
Switch
    ↓
Ledger
    ↓
Settlement

State Reconciliation is therefore relevant to Intent Language whenever semantic grounding depends on distributed enterprise state.

Noema must distinguish:

semantic expression
    ≠
enterprise observation
    ≠
reconciled fact
    ≠
business outcome

Fact Status remains distinct from Intent semantics.

Canonical values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

⸻

61. Intent Language and Versioning

Intent Language must preserve semantic identity across time.

An admitted Intent has an identity and version.

Conceptually:

Intent:
    ID = I-123
    Version = 1

If clarification materially changes its semantic content:

Intent:
    ID = I-123
    Version = 2
    supersedes = I-123:v1

Historical versions remain immutable.

This prevents later clarification, state changes, or interpretation updates from silently rewriting what the Actor previously expressed.

A Composite Intent must similarly reference exact constituent Intent versions and must create a new composite version when its material semantic structure changes.

⸻

62. Intent Language and Auditability

Intent Language provides the semantic object necessary for causal audit.

The audit record should be able to connect:

Actor Expression
      ↓
Intent Version
      ↓
Interpretation
      ↓
Resolution
      ↓
Evidence / Provenance
      ↓
Executable Intent
      ↓
Trust Decision
      ↓
Action
      ↓
Execution
      ↓
Verification
      ↓
Outcome

This does not require exposing private Model chain-of-thought.

Auditability requires causal traceability of material decisions and state transitions.

⸻

63. Canonical Semantic Architecture

Noema’s semantic architecture can therefore be expressed as:

┌─────────────────────────────────┐
│         Actor Expression        │
│                                 │
│ "Renew my expired card."        │
└────────────────┬────────────────┘
                 │
                 ▼
          Interpretation
                 │
                 ▼
┌─────────────────────────────────┐
│          Intent Language        │
│                                 │
│ Actor                           │
│ Objective                       │
│ Resources                       │
│ Context                         │
│ Constraints                     │
│ Preferences                     │
│ Relationships                   │
│ Expected Outcome                │
└────────────────┬────────────────┘
                 │
                 ▼
      Grounding / Resolution
                 │
                 ├── Context
                 ├── Evidence
                 ├── State Reconciliation
                 └── Clarification
                 │
                 ▼
┌─────────────────────────────────┐
│         Executable Intent       │
└────────────────┬────────────────┘
                 │
                 ▼
               Trust
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
     EXECUTE  CLARIFY  ESCALATE
                 │
                 └── REJECT
                 │
                 ▼
              Action
                 │
                 ▼
             Execution
                 │
                 ▼
           Verification
                 │
                 ▼
              Outcome

The critical boundary remains:

Probabilistic
interpretation / candidate generation
                │
                │
        HARD SEMANTIC BOUNDARY
                │
                ▼
Deterministic
resolution / Trust / execution

Intent Language is the canonical semantic representation at this boundary. It does not itself constitute the deterministic execution decision.

⸻

64. Canonical Principles

1. Intent Language represents meaning, not wording.
2. Intent Language is independent of execution implementation.
3. Intent is distinct from Action.
4. Intent is distinct from Capability.
5. Intent is goal-oriented.
6. Material semantic references must be grounded before execution.
7. Ambiguity must remain representable.
8. Confidence is metadata, not semantic meaning.
9. Constraints and Preferences must remain distinguishable.
10. Policy constrains execution but does not redefine Actor intent.
11. Composite Intents must preserve constituent Intent identity and version.
12. Semantic relationships must be explicit where materially relevant.
13. Intent Language should be typed.
14. Domain-specific concepts may extend the canonical vocabulary.
15. Serialization is an implementation decision; semantic meaning is canonical.
16. Defaults must not silently create material intent.
17. Inference must remain distinguishable from explicit expression where provenance matters.
18. State and Outcome must not be confused with Intent.
19. State Reconciliation may support grounding but does not redefine the Actor’s objective.
20. Executable Intent is distinct from authorization and execution success.
21. Admitted Intent versions are immutable.
22. Material clarification or semantic modification creates a new Intent version.
23. Intent Language must preserve constraints, scope, alternatives, conditions, and prohibitions.
24. Intent Language must not bypass Trust.

⸻

65. What Intent Language Protects Against

Intent Language protects Noema from:

* natural-language drift
* Model-dependent execution
* repeated interpretation
* ambiguous API mapping
* loss of Constraints
* loss of Preferences
* loss of Context
* loss of Actor identity
* loss of desired Outcomes
* hidden assumptions
* implementation coupling
* uncontrolled semantic expansion
* silent reinterpretation across time

Most importantly, it prevents Noema from treating:

"What the Actor said"

and:

"What the system should execute"

as the same representation.

Intent Language preserves the semantic intermediate representation between those two concerns.

⸻

66. What Intent Language Does Not Do

Intent Language does not:

* authorize execution
* execute Actions
* select infrastructure
* replace Policy
* replace Capabilities
* guarantee correctness
* eliminate ambiguity
* establish business truth
* guarantee Outcome
* replace State Reconciliation
* replace Trust
* replace Action Contracts
* replace Execution Contracts

It provides the canonical semantic representation upon which those systems operate.

⸻

67. Final Definition

Intent Language is Noema’s canonical semantic language for representing an Actor’s intended objective, relevant Resources, Context, Constraints, Preferences, relationships, and expected Outcome independently of natural-language wording and execution implementation.

It provides the semantic representation through which Noema can preserve meaning, resolve ambiguity, ground references, maintain constraints, compose related Intents, and produce Executable Intent without directly converting natural-language interpretation into consequential execution.

The shortest canonical formulation is:

Natural language expresses intent.
Intent Language makes that intent
explicit, typed, grounded, and stable
across the boundary between interpretation
and execution.
Executable Intent establishes semantic readiness.
Trust determines whether execution may proceed.