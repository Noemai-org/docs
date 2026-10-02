> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Model

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-model.md

⸻

1. Definition

The Intent Model is Noema’s canonical structural model for representing an Actor’s intended objective as a typed, contextual, constrained, versioned, and resolvable semantic object.

The Intent Model defines what an Intent contains and how its semantic components relate.

It does not define:

* how natural language is interpreted — see intent-language.md
* how ambiguity is identified — see intent-ambiguity.md
* how ambiguity is resolved — see intent-ambiguity.md
* how clarification occurs — see clarification.md
* how confidence is evaluated — see confidence.md
* how an Intent progresses through time — see intent-lifecycle.md
* how execution is planned or performed — see the Action, Capability, Execution, and Action Contract specifications

The Intent Model is the structural foundation connecting these systems.

⸻

2. The Core Idea

Noema must not represent an Intent only as:

"Renew my card"

or as an implementation-level operation such as:

RenewCard(Card#123)

That representation may omit information required for resolution, Trust evaluation, execution, and Outcome verification.

The canonical semantic object is closer to:

Intent
├── Identity
├── Version
├── Source
├── Actor
├── Objective
├── Resources
├── Entities
├── Parameters
├── Scope
├── Context
├── Constraints
├── Preferences
├── Expected Outcome
├── Relationships
├── Provenance
└── Lifecycle Reference

The exact implementation and serialization may evolve.

The semantic structure and its invariants must remain stable.

⸻

3. Intent as a First-Class Semantic Object

An Intent is a first-class object in Noema.

Conceptually:

Intent {
    identity
    version
    source
    actor
    objective
    resources
    entities
    parameters
    scope
    context
    constraints
    preferences
    expected_outcome
    relationships
    provenance
    lifecycle_reference
}

An Intent is not merely a message, prompt, API call, or execution command.

Its semantic identity persists across resolution, clarification, Trust evaluation, execution, verification, and Outcome establishment.

Historical admitted versions are immutable.

A material semantic change produces a new Intent version rather than silently mutating the historical object.

⸻

4. Intent Identity and Intent Version Are Distinct

Noema must distinguish:

Intent Identity

from:

Intent Version

Conceptually:

Intent#123:v1
Intent#123:v2
Intent#123:v3

The Intent identity correlates the semantic object across its lifecycle.

The version identifies a specific immutable semantic representation.

A material clarification, modification, or other semantic change creates a new version with an explicit relationship such as:

v2.supersedes = v1

No historical Intent version is silently rewritten.

This preserves causal auditability and prevents semantic drift.

⸻

5. Source of Intent

Every Intent has a Source of Intent.

The Source identifies where the expression or event giving rise to the Intent originated.

Examples include:

Human
Agent
System
Workflow
API/Application
Enterprise Event

Source and Actor are distinct.

For example:

Source:
Customer-facing application
Actor:
User#123

or:

Source:
Enterprise workflow
Actor:
Organization#456

An originating event or system does not automatically establish authorization to perform an Action.

Source establishes provenance and origin, not authority.

⸻

6. Actor

Every Intent must identify an Actor where the Intent semantics require one, or use an explicitly defined system-level origin where the ontology permits it.

The Actor answers:

Who intends the Outcome?

Examples include:

User#123
Organization#456
System#789
Agent#321
AuthorizedDelegate#555

Actor identity may affect:

* authority
* permissions
* applicable policy
* available Resources
* contextual defaults
* execution scope

Actor resolution and authority are separate concerns.

No inference may manufacture identity or authority that has not been established by an authoritative source.

⸻

7. Objective

The Objective represents the central semantic goal of the Intent.

Examples include:

RenewCard
CancelSubscription
TransferFunds
CreateProject
UpdateAddress
NotifyCustomer

Where a corresponding canonical concept exists, the Objective should reference that canonical concept.

It should not be an arbitrary model-generated phrase treated as authoritative merely because it is syntactically valid.

The Objective describes what the Actor wants accomplished.

It does not specify the implementation strategy.

⸻

8. Objective vs Natural-Language Expression

Natural language is an expression of meaning.

The Intent Model represents the resulting semantic structure.

For example:

Expression:
"Can you get my account working again?"

may produce a candidate representation:

Objective:
RestoreAccountAccess

The original expression remains available through provenance.

The canonical semantic object should preserve the material semantic commitments established by the expression and available evidence without fabricating unsupported meaning.

⸻

9. Intent Is Not an Action

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

The Intent can remain semantically stable even when the execution strategy changes.

An Intent may reference an Action candidate or eventually produce one or more Actions, but an Intent is not itself an Action.

⸻

10. Intent Is Not a Capability

A Capability represents a bounded operation the system is able to perform.

An Intent represents the Actor’s desired objective.

For example:

Intent:
RestoreAccountAccess
Possible Capabilities:
├── VerifyIdentity
├── ResetPassword
└── InvalidateSessions

Capability availability does not establish:

* permission
* authorization
* policy compliance
* current applicability
* Trust
* execution success

The Intent Model therefore remains capability-agnostic.

⸻

11. Intent Is Not an Outcome

An Intent describes the desired objective.

An Expected Outcome describes the condition that would constitute satisfaction of that objective.

An Actual Outcome describes what verification establishes after execution.

Therefore:

Intent
   ↓
Expected Outcome
   ↓
Execution
   ↓
Observed Evidence
   ↓
Actual Outcome

Intent and Outcome must not be collapsed into one object or state.

⸻

12. Intent Is Not Business State

Noema owns Intent semantics and Intent lifecycle information.

The relevant enterprise system remains the source of truth for Business State.

Example:

Intent:
RenewCard(Card#123)
Intent lifecycle:
EXECUTABLE
Enterprise Business State:
Card#123 = EXPIRED

Later:

Intent lifecycle:
OUTCOME_PENDING
Enterprise Business State:
Card#123 = ACTIVE

Noema uses authoritative enterprise state and verification evidence to establish whether the Expected Outcome has been achieved.

Noema does not become the source of truth for the Card’s domain state merely by representing or observing it.

⸻

13. Resources

Resources identify domain objects materially affected by, referenced by, or required to satisfy an Intent.

Examples include:

Card#123
Account#456
Payment#789
Project#321
Invoice#555

Resources may have semantic roles such as:

primary
source
destination
subject
related
collection

The exact roles depend on the Intent type.

Material Resources must be resolved and grounded before an Intent can become Executable.

⸻

14. Resource Roles

A Resource is not merely an identifier.

Its role within an Intent must be explicit where role affects semantics.

For example:

TransferFunds
├── source      = Account#1
├── destination = Account#2
└── amount      = 500 USD

Swapping the source and destination changes the meaning materially.

Resource role is therefore part of the semantic representation and must not be inferred downstream from implementation conventions.

⸻

15. Entity References

An Intent may reference Entities that are not themselves the primary Resource.

Example:

"Send the invoice to Sarah."

Conceptually:

Resource:
Invoice#123
Entity:
Sarah#456

An Entity may represent:

* participant
* recipient
* owner
* destination
* reference
* organization
* related semantic object

The distinction between Resource and Entity is semantic rather than merely technical.

⸻

16. Parameters

Parameters contain typed values required to express the semantics of an Intent.

Examples include:

amount = 500 USD
quantity = 3
deadline = 2026-08-30T17:00
duration = 30 days

Parameters must retain semantic type information.

A parameter is not merely an arbitrary string extracted from language.

Parameter requirements are determined by the canonical Intent type and applicable domain semantics.

⸻

17. Scope

Scope determines the extent of an Intent.

Examples include:

single resource
specific collection
all matching resources
specific organizational scope
specific geographic scope

Scope must be explicit when it materially affects meaning.

For example:

"Delete this project."

is materially different from:

"Delete all inactive projects."

Scope must never be expanded through an implicit assumption merely because a broader operation is technically available.

⸻

18. Context

Context contains information relevant to interpreting or resolving an Intent.

Examples include:

* conversation context
* session context
* temporal context
* domain context
* Actor context
* environment context
* system context
* validated enterprise observations

Example:

Conversation:
"Create a project called Noema."
Follow-up:
"Add Sarah to it."

The second Intent may use conversational Context to resolve:

project = Noema

Context can help establish semantic references, but Context is not inherently authoritative.

Its scope, freshness, authority, and Fact Status must be assessed where material.

⸻

19. Context Is Not Intent

Context helps determine what an Intent means.

It is not necessarily part of what the Actor explicitly requested.

Example:

Context:
CurrentWorkspace = Engineering
Intent:
CreateProject("Noema")

The workspace may ground the Intent without becoming its Objective or being treated as an explicit Actor constraint.

Context should not silently introduce material requirements that the Actor did not express or that authoritative evidence does not establish.

⸻

20. Constraints

Constraints define semantic boundaries that the resulting execution must respect.

Example:

"Transfer $500 to savings, but don't use my emergency account."

Conceptually:

Objective:
TransferFunds
Parameters:
amount = 500 USD
Resources:
destination = Savings
Constraint:
source != EmergencyAccount

Constraints are part of the Intent’s semantic commitments.

They must survive resolution, planning, and execution.

No planner or Action selection mechanism may silently discard them.

⸻

21. Preferences

Preferences express desirable properties that may be relaxed under defined conditions.

Example:

"I'd prefer the cheapest flight."
Preference:
MinimizePrice

Compare:

"The flight must cost less than $500."
Constraint:
Price <= 500 USD

Preferences can influence planning or selection where the system is permitted to optimize.

They cannot override:

* hard constraints
* policy
* authority
* Trust conditions
* explicit prohibitions

⸻

22. Constraints vs Preferences

The distinction is semantic:

Constraint
    =
condition that must be satisfied
Preference
    =
desirable property to optimize or preserve where possible

The system must not convert a Preference into a mandatory Constraint without justification.

Likewise, it must not weaken an explicit Constraint into a Preference.

Where an Intent type supports priority among preferences, that priority must be explicitly represented or deterministically established.

⸻

23. Expected Outcome

The Expected Outcome describes the condition the Actor expects after successful satisfaction of the Intent.

Example:

Intent:
RenewCard
Expected Outcome:
Card#123.state = ACTIVE

The Expected Outcome provides a semantic target for verification.

It does not assert that the condition is already true.

It does not guarantee that execution will succeed.

⸻

24. Expected Outcome vs Actual Outcome

Noema must distinguish:

Expected Outcome

from:

Actual Outcome

Example:

Expected:
Card#123.state = ACTIVE
Observed:
Card#123.state = ACTIVE

The Actual Outcome is established from appropriate verification evidence.

A Trust decision of EXECUTE does not establish an Outcome.

Execution must occur, and verification must establish what actually happened.

⸻

25. Provenance

Significant Intent components should carry provenance where practical.

Example:

Resource:
Card#123
Provenance:
Expression:
"the card I used yesterday"
Evidence:
Transaction#789

Provenance allows Noema to answer questions such as:

Why was this Resource selected?
Which evidence supported this interpretation?
Which Intent version introduced this value?
What changed during clarification?

Provenance supports causal auditability.

It is not a substitute for authoritative state or authorization.

⸻

26. Explicit vs Inferred Values

The Intent Model should distinguish information that was:

explicitly expressed

from information that was:

inferred, grounded, or resolved from Context and evidence

Example:

"Renew my card."

Explicit:

Objective = RenewCard

Potentially resolved:

Resource = Card#123

if authoritative enterprise state establishes that only one eligible card satisfies the reference.

The distinction is important for clarification, Trust, provenance, and auditability.

An inferred value is not authoritative merely because a model inferred it confidently.

⸻

27. Evidence, Fact Status, and Confidence

Evidence, Fact Status, and Confidence are distinct.

Evidence answers:

What supports this claim?

Fact Status describes the epistemic status of the relevant claim.

Canonical Fact Status values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Confidence answers:

How strongly does a particular interpretation or claim appear supported?

Confidence is not authorization, Trust, or Fact Status.

A model may have high confidence in a candidate interpretation while the underlying claim remains UNVERIFIED or CONFLICTED.

⸻

28. Intent State

Intent lifecycle information is associated with the Intent but is governed by intent-lifecycle.md.

The Intent Model must not redefine lifecycle semantics.

For example:

Intent:
RenewCard(Card#123)
Lifecycle:
EXECUTABLE

The lifecycle may subsequently progress through Trust evaluation, execution, verification, and Outcome establishment.

Trust decisions and execution states must not be collapsed into the semantic structure of the Intent itself.

⸻

29. Semantic Resolution

An Intent is semantically resolved when the information necessary to establish its material meaning has been determined sufficiently for downstream deterministic evaluation.

Resolution may require:

* Resource grounding
* Entity resolution
* Context resolution
* State Reconciliation
* constraint resolution
* temporal resolution
* scope resolution
* reference resolution
* deterministic domain rules

Resolution is not the same as execution.

Resolution is also not the same as authorization.

⸻

30. Material Ambiguity

The Intent Model must be capable of representing unresolved alternatives without forcing an arbitrary choice.

Example:

Intent:
RenewCard
Resource Candidates:
├── Card#456
└── Card#789

If the distinction is materially relevant, the Intent remains unresolved with respect to that semantic dimension.

intent-ambiguity.md determines when such a distinction constitutes material ambiguity and when clarification is required.

The model must not collapse multiple materially valid interpretations merely to produce a single executable object.

⸻

31. Required vs Unknown vs Not Applicable

The model must distinguish:

known
unknown
not applicable
ambiguous

Example:

destination:
UNKNOWN

is different from:

destination:
NOT_APPLICABLE

and different from:

destination:
AMBIGUOUS

These states have different semantic consequences.

Missing information must not be silently converted into irrelevance.

⸻

32. Semantic Completeness

An Intent is semantically complete when all information required to establish its material meaning is available.

This does not mean every possible field must be populated.

For example:

CreateProject("Noema")

may not require:

description
logo
billing_plan

if those fields are optional for the relevant Intent type.

Semantic completeness is therefore determined by the canonical Intent schema and applicable domain semantics, not by a universal requirement that every field be populated.

⸻

33. Defaults

Defaults may resolve non-material omissions when they are:

* explicitly defined
* deterministic
* domain-valid
* within scope
* policy-compatible
* non-material to the Actor’s objective

Defaults must not:

* invent material intent
* expand scope
* manufacture authority
* select among materially ambiguous alternatives
* override explicit constraints

A default that changes the semantic meaning of the Intent is not a valid silent default.

⸻

34. Temporal Semantics

An Intent may contain temporal semantics such as:

Date:
2026-08-28
Deadline:
2026-08-30T17:00
Before:
17:00
Recurring:
Every Monday

Temporal information belongs in the semantic representation when it affects:

* the desired Outcome
* execution constraints
* scope
* validity
* ordering
* conditions

Temporal interpretation must be explicit enough for deterministic downstream evaluation where material.

⸻

35. Location Semantics

Where relevant, an Intent may contain geographic or logical location.

Example:

"Find me a hotel near the conference venue."

Conceptually:

Objective:
FindHotel
Context:
ConferenceVenue = X
Constraint:
Distance <= 2 km

Location references must be grounded where they materially affect execution or Outcome.

A location inferred from Context remains subject to the same evidence and resolution requirements as other material references.

⸻

36. Numeric and Scalar Values

Values must retain semantic types.

Instead of:

amount = "500"

the semantic representation should preserve:

amount:
    value = 500
    currency = USD

Likewise, the model may need typed representations for:

* duration
* distance
* percentage
* quantity
* timestamp
* rate
* count

Units and domains must not be discarded where they materially affect meaning.

⸻

37. Optionality

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

The Intent Model therefore defines a common structural foundation rather than requiring one universal field set for every Intent.

⸻

38. Conditional Semantics

An Intent may contain explicit conditional semantics.

Example:

"If the payment fails, retry it."

Conceptually:

Condition:
Payment.Failed
Intent:
RetryPayment

The condition must remain explicit.

The model or planner must not invent conditional relationships that materially alter the Actor’s intent.

Conditions are semantic relationships, not workflow implementation instructions.

⸻

39. Alternative Semantics

An Actor may explicitly allow alternatives.

Example:

"Either renew my card or replace it."

Conceptually:

Alternative:
├── RenewCard
└── ReplaceCard

The alternatives represent mutually acceptable semantic paths for satisfying the stated objective.

Alternatives do not imply that all alternatives should execute.

Selection among alternatives must respect:

* Intent semantics
* Constraints
* Policy
* Authority
* Trust
* available capabilities
* current state

⸻

40. Negation and Prohibition

Negative requirements must be represented explicitly when they materially constrain execution.

Example:

"Don't use my emergency account."

Conceptually:

Constraint:
source != EmergencyAccount

Negation should not be represented merely through absent data.

The specific representation of prohibitions depends on the canonical constraint and ontology model.

A negative constraint is not an instruction to bypass the prohibited condition through another interpretation.

⸻

41. Quantification

The model must support scope and quantity.

Example:

"Delete all inactive projects."

Conceptually:

Objective:
DeleteProject
Scope:
ALL
Filter:
State = INACTIVE

Compare:

"Delete this project."

Conceptually:

Scope:
SINGLE
Resource:
Project#123

Quantification must be explicit where it materially affects the set of Resources affected.

Noema must not infer broad quantification from a singular expression.

⸻

42. Relationships

Intent components may have explicit semantic relationships.

Examples include:

PRECEDES
DEPENDS_ON
CONDITIONAL_ON
ALTERNATIVE_TO

A relationship is meaningful only where its semantics are defined by the relevant ontology or Intent type.

Natural-language ordering words such as “then” are evidence for a relationship, not by themselves proof of an execution workflow.

Semantic relationships must not be confused with the Enterprise Action Graph.

The Intent Model represents semantic relationships.

The Planner maps resolved semantic requirements into bounded Actions and the Enterprise Action Graph.

⸻

43. Composite Intents

An Intent may contain or reference multiple constituent Intents.

Example:

"Transfer my remaining balance and close the account."

Conceptually:

Composite Intent#123
├── Intent#124:v1 TransferBalance
└── Intent#125:v1 CloseAccount

Each constituent Intent retains its own identity and version.

Composition does not merge the children into an indistinguishable execution command.

The semantic relationships between the constituents are represented explicitly.

⸻

44. Composite Intent Structure

Conceptually:

CompositeIntent {
    identity
    version
    source
    actor
    intents[]
    relationships[]
    shared_context[]
    constraints[]
    expected_outcome
    provenance
}

A Composite Intent is a semantic composition.

It is not an execution workflow.

For example:

TransferBalance
    PRECEDES
CloseAccount

expresses a semantic dependency that the Planner may later translate into an execution sequence.

The exact execution sequence remains an execution concern.

⸻

45. Partial Resolution of Composite Intents

Constituent Intents may resolve independently where the composition semantics permit it.

For example:

Child A:
RESOLVED
Child B:
CLARIFICATION_REQUIRED

This does not automatically make the entire Composite Intent executable or ineligible for any partial progress.

Whether a child may proceed independently depends on the explicit semantic dependencies and constraints of the composition.

Trust and execution conditions remain applicable to each child.

Authority and Trust are not inherited from the parent merely because the child belongs to the same composition.

⸻

46. Capability Binding

An Intent may be associated with candidate Capabilities capable of satisfying its semantic objective.

Example:

Intent:
NotifyCustomer
Candidate Capabilities:
├── SendEmail
├── SendSMS
└── SendPush

The Intent should not become semantically coupled to one Capability merely because that implementation is currently preferred.

Capability selection belongs to bounded planning and execution.

Capability existence does not establish:

permission
authorization
applicability
availability
Trust
success

⸻

47. Action Planning

The Intent Model does not prescribe the exact Actions required to satisfy an Intent.

Example:

Intent:
RestoreAccountAccess
Possible execution:
VerifyIdentity
    ↓
ResetPassword
    ↓
InvalidateSessions
    ↓
VerifyAccess

The Planner selects or constructs a bounded execution path using the Enterprise Action Graph, Capability Registry, Action Contracts, current state, and Trust constraints.

The Intent defines the semantic objective and requirements that the plan must satisfy.

⸻

48. Intent and Execution Plan

These are separate objects.

Conceptually:

Intent
   ↓
Executable Intent
   ↓
Trust
   ↓
Execution Plan
   ↓
Actions

An Execution Plan may change without changing the Actor’s semantic Intent.

Likewise, different valid plans may satisfy the same Intent.

The plan must remain within the capabilities, contracts, policies, authority, and Trust conditions established by Noema.

⸻

49. Executable Intent

Executable Intent is a specific resolved state of an Intent, not a different semantic category of desire.

An Intent becomes Executable when its material semantic requirements have been sufficiently established to support deterministic Trust evaluation and potential Action execution.

This generally requires:

* material meaning resolved
* material Resources grounded
* required parameters resolved
* scope established
* relevant Context established
* relevant State reconciled
* constraints explicit and evaluable
* required relationships resolved
* no material ambiguity remaining

Executable Intent does not mean:

authorized

and does not mean:

successful

Trust subsequently determines whether the Executable Intent may proceed.

⸻

50. Trust Relationship

The Trust Engine evaluates the resolved semantic object against the conditions required for safe and governed execution.

Conceptually:

Resolved Intent
      ↓
Executable Intent
      ↓
Trust Evaluation
      ↓
┌───────────┬───────────┬───────────┬──────────┐
│ EXECUTE   │ CLARIFY   │ ESCALATE  │ REJECT   │
└───────────┴───────────┴───────────┴──────────┘

Trust evaluates the Intent against relevant:

* current state
* policy
* authority
* constraints
* capability and Action applicability
* Action Contracts
* security conditions
* other deterministic governance requirements

Trust does not rewrite the Actor’s objective merely to obtain an executable path.

EXECUTE means the resolved path satisfies the applicable Trust conditions to proceed.

It does not mean execution has succeeded.

⸻

51. Authority Is Not an Intent Field That Can Be Inferred Freely

The Intent Model may represent the Actor and the semantic requirements relevant to authority.

It must not treat authority as an arbitrary Actor-provided value.

Authority depends on the relevant:

Actor
Action
Resource
Scope
Current State
Policy
Authorization source

Technical authorization, policy authorization, and business authorization are distinct concepts.

The Intent Model expresses what is intended.

Trust determines whether the resolved execution path may proceed under the applicable authority and governance conditions.

⸻

52. Intent State vs Trust Decision vs Execution State vs Outcome

Noema must not collapse these concepts into one status field.

They answer different questions:

Intent Lifecycle:
Where is the Intent in its semantic/control lifecycle?
Trust Decision:
May the resolved path proceed under current governance conditions?
Execution State:
What is happening with the Actions and execution attempts?
Outcome:
What condition did verification establish?

For example:

Intent:
EXECUTABLE
Trust:
EXECUTE
Execution:
IN_PROGRESS
Outcome:
PENDING

These states are compatible and describe different dimensions.

The canonical lifecycle and execution specifications define their respective semantics.

⸻

53. Cancellation, Expiration, and Supersession

Cancellation, expiration, and supersession must not be treated as semantic rewrites of a historical Intent.

An admitted Intent version remains immutable.

A cancellation or material modification may be represented through:

* explicit control state
* a new Intent version
* a new control Intent
* an explicit supersession relationship

depending on the applicable lifecycle semantics.

Cancellation is not equivalent to Trust REJECT.

Expiration is not equivalent to execution failure.

Supersession does not erase historical versions.

⸻

54. Intent Model and State Reconciliation

State Reconciliation is relevant to the Intent Model wherever external state is necessary to establish semantic meaning or determine whether a reference is still valid.

For example:

"Renew the card I used yesterday."

may require reconciliation across:

Transaction History
Card Records
Customer Records
Eligibility State

State Reconciliation may resolve the reference without asking the Actor.

It may also reveal:

multiple candidates
stale evidence
conflicting records
missing state

The resulting semantic status must preserve those distinctions rather than forcing a single value.

⸻

55. Intent Model and Intent Language

intent-language.md answers:

How does Noema represent semantic meaning?

intent-model.md answers:

What structural components constitute an Intent?

The distinction is:

Intent Language
    =
canonical semantic representation language/model
Intent Model
    =
canonical structural composition of an Intent

Intent Language can represent unresolved, resolved, and composite semantic structures.

Executable Intent is a resolved lifecycle state produced when the semantic requirements are sufficiently established.

⸻

56. Intent Model and Intent Ambiguity

intent-ambiguity.md determines when the Intent structure contains materially unresolved alternatives.

For example:

Resource Candidates:
├── Card#456
└── Card#789

The Intent Model provides a structure capable of representing the alternatives.

The Ambiguity specification determines:

* whether the alternatives are materially distinct
* whether available evidence resolves them
* whether clarification is required

The Intent Model must therefore support ambiguity without encoding an arbitrary resolution.

⸻

57. Intent Model and Clarification

Clarification operates on semantic gaps in the Intent.

For example:

Intent:
RenewCard
Resource:
AMBIGUOUS
├── Card#456
└── Card#789

A clarification request may ask the Actor to identify the intended card.

If the response materially changes the Intent semantics, it creates a new admitted Intent version.

The original version remains immutable.

A clarification response does not itself establish:

* authority
* business truth
* policy compliance
* Trust
* execution success

The response must re-enter validation and resolution.

⸻

58. Intent Model and Confidence

confidence.md determines how Noema represents epistemic support for interpretation.

The Intent Model provides the semantic object being interpreted and resolved.

Therefore:

Intent
   +
Evidence
   +
Fact Status
   +
Confidence

must remain conceptually distinct.

High confidence cannot override:

* material ambiguity
* conflicting authoritative state
* constraints
* policy
* authority
* Trust requirements

Confidence supports reasoning about evidence quality.

It does not determine permission.

⸻

59. Intent Model and Lifecycle

intent-lifecycle.md determines how an Intent version progresses through:

receipt
interpretation
validation
admission
resolution
clarification
executability
Trust evaluation
execution
verification
Outcome

The Intent Model defines the structural object that moves through that lifecycle.

Lifecycle state must not be used as a substitute for:

* Business State
* Trust Decision
* Execution State
* Actual Outcome

Historical versions remain auditable.

⸻

60. Intent Model and Determinism

Noema’s deterministic boundary depends on the Intent Model being explicit enough to support deterministic evaluation.

The probabilistic interpretation layer may generate:

candidate semantic representation

Noema must then establish through hard validation, resolution, evidence, and State Reconciliation:

whether the representation is admissible
whether its material meaning is resolved
whether required Resources are grounded
whether required constraints are evaluable
whether it can become Executable Intent

No probabilistic interpretation may directly invoke a consequential Action.

The architectural boundary is:

Expression
    ↓
Candidate Semantic Representation
    ↓
Hard Schema Validation / Admission
    ↓
Canonical Intent
    ↓
Resolution + State Reconciliation
    ↓
Executable Intent
    ↓
Trust
    ↓
Bounded Action
    ↓
Execution
    ↓
Verification
    ↓
Outcome

⸻

61. Canonical Conceptual Schema

A useful conceptual representation is:

Intent {
    identity: IntentID
    version: Version
    source: Source
    actor: Actor
    objective: Concept
    resources: [
        Resource
    ]
    entities: [
        Entity
    ]
    parameters: [
        TypedParameter
    ]
    scope: Scope
    context: ContextReferences
    constraints: [
        Constraint
    ]
    preferences: [
        Preference
    ]
    expected_outcome: ExpectedOutcome
    relationships: [
        Relationship
    ]
    provenance: Provenance
    lifecycle_reference: IntentLifecycleReference
}

This is a conceptual semantic model.

It is not a commitment to a specific programming language, database schema, API representation, or serialization format.

The model may be extended by domain-specific Intent types without changing the universal semantic principles.

⸻

62. Minimal Intent

The smallest meaningful Intent contains enough information to establish:

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

Additional fields become required according to the Intent type and domain semantics.

A minimal Intent is not necessarily Executable Intent.

It may require further resolution before deterministic Trust evaluation is possible.

⸻

63. Fully Resolved Intent

A fully resolved Intent might look conceptually like:

Intent {
    identity:
        Intent#123
    version:
        v2
    source:
        CustomerApplication
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
        Card#789.state = ACTIVE
    provenance:
        resource_resolution =
            Transaction#555
    lifecycle:
        EXECUTABLE
}

This representation is sufficiently explicit for deterministic Trust evaluation, subject to current state, policy, authority, contracts, and other applicable conditions.

It does not itself constitute a Trust decision.

⸻

64. Example: “Renew My Card”

Natural language:

"Please renew my card."

Initial canonical representation may contain:

Intent {
    actor:
        User#123
    objective:
        RenewCard
    resources:
        Card = UNKNOWN
}

If authoritative state establishes one eligible card:

Intent {
    actor:
        User#123
    objective:
        RenewCard
    resources:
        Card = Card#456
}

If multiple materially valid cards remain:

Intent {
    actor:
        User#123
    objective:
        RenewCard
    resources:
        CardCandidates:
            Card#456
            Card#789
    resolution:
        material_ambiguity = true
}

The Intent Model preserves the unresolved alternatives.

intent-ambiguity.md and clarification.md determine whether and how the ambiguity is resolved.

⸻

65. Example: “Renew the Card I Used Yesterday”

Conceptually:

Intent {
    actor:
        User#123
    objective:
        RenewCard
    resources:
        Card = Card#456
    context:
        usage_reference =
            yesterday
    provenance:
        Card#456
            ← Transaction#789
            ← "used yesterday"
    expected_outcome:
        Card#456.state = ACTIVE
}

The linguistic reference has become a grounded semantic reference through evidence and resolution.

If multiple cards satisfy the reference, the Resource remains ambiguous rather than being selected arbitrarily.

⸻

66. Example: “Transfer $500 to Savings”

Conceptually:

Intent {
    actor:
        User#123
    objective:
        TransferFunds
    resources:
        source =
            Checking#1
        destination =
            Savings#2
    parameters:
        amount =
            500 USD
}

Additional constraints, scope, authority requirements, and Expected Outcome semantics may be required by the domain.

If the source account is materially ambiguous:

resolution:
    source = AMBIGUOUS

The Intent is not Executable until the ambiguity is resolved or otherwise deterministically eliminated.

For consequential financial actions, current state and applicable authority and policy conditions must also be evaluated by Trust.

⸻

67. Example: Composite Intent

Natural language:

"Refund the payment and email me the receipt."

Conceptually:

CompositeIntent {
    actor:
        User#123
    intents: [
        Intent {
            objective:
                RefundPayment
            resources:
                Payment#456
        },
        Intent {
            objective:
                SendReceipt
            resources:
                Payment#456
        }
    ]
    relationship:
        RefundPayment
            PRECEDES
        SendReceipt
}

The relationship expresses semantic dependency.

The Planner determines the bounded Action sequence required to satisfy the composition.

Each constituent remains subject to its own resolution, Trust, Action Contract, execution, and verification requirements.

⸻

68. Intent Model and Canonical Ontology

The Intent Model depends on canonical ontology definitions established elsewhere in the repository.

Relevant primitives may include:

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

The Intent Model composes these primitives.

It should not silently redefine their canonical meanings.

Domain-specific extensions may add concepts and structures where the universal ontology permits them.

⸻

69. Semantic Representation vs Wire Schema

The Intent Model is a semantic model.

Its conceptual structure does not require a particular:

* JSON schema
* database schema
* API format
* programming language
* message protocol
* serialization format

A concrete implementation may introduce transport-specific representations.

Those representations must preserve the material semantics and invariants of the canonical Intent Model.

⸻

70. Versioning and Semantic Stability

The Intent Model must support evolution without silently changing historical meaning.

Changes to the model or Intent type must be versioned where they can alter semantic interpretation.

An Intent version identifies the exact semantic representation used at a point in the lifecycle.

Historical versions must remain interpretable using the relevant ontology, Intent-type, policy, and contract versions.

Canonical does not mean immutable forever at the schema level.

It means semantic changes are explicit, versioned, and auditable.

⸻

71. Intent Model Invariants

Invariant 1

Every Intent has an Intent Identity and a specific immutable Version once admitted.

Invariant 2

Every Intent has a Source of Intent and an Actor where the Intent semantics require one or an explicitly defined system-level origin.

Invariant 3

Every admitted Intent uses canonical semantic concepts appropriate to its Intent type and domain.

Invariant 4

Material Resources must be grounded before an Intent becomes Executable.

Invariant 5

Material ambiguity must be representable and must not be resolved through unsupported guessing.

Invariant 6

Constraints must survive resolution, planning, and execution.

Invariant 7

Preferences must not silently become hard Constraints.

Invariant 8

Expected Outcomes must remain distinct from Actions and Capabilities.

Invariant 9

Intent lifecycle state must remain distinct from Business State, Trust Decision, Execution State, and Actual Outcome.

Invariant 10

Evidence, Fact Status, and Confidence must remain conceptually distinct.

Invariant 11

Authority must not be manufactured through Intent interpretation or user-provided assertions alone.

Invariant 12

An Intent version must remain semantically stable throughout its lifecycle.

Invariant 13

Material semantic changes must create a new Intent version rather than mutate historical meaning.

Invariant 14

Execution implementation must remain replaceable without changing the Intent’s semantic identity.

Invariant 15

A Trust decision of EXECUTE must not be treated as proof of execution success or Outcome completion.

⸻

72. What the Intent Model Protects Against

Without a canonical model, different parts of Noema may interpret the same request differently.

The Intent Model protects against:

* semantic drift
* implicit assumptions
* lost constraints
* lost context
* untyped references
* scope expansion
* implementation coupling
* ambiguous execution
* unsupported authority assumptions
* unverifiable completion
* model-dependent state

It gives downstream subsystems a shared semantic object without requiring those subsystems to share implementation details.

⸻

73. Architectural Role

The Intent Model sits at the semantic center of Noema:

                    Source of Intent
                           │
                           ▼
                Candidate Interpretation
                           │
                           ▼
              Hard Schema Validation / Admission
                           │
                           ▼
                  ┌──────────────────┐
                  │   INTENT MODEL   │
                  │                  │
                  │ Identity         │
                  │ Version          │
                  │ Source           │
                  │ Actor            │
                  │ Objective        │
                  │ Resources        │
                  │ Entities         │
                  │ Parameters       │
                  │ Scope            │
                  │ Context          │
                  │ Constraints      │
                  │ Preferences      │
                  │ Expected Outcome │
                  │ Relationships    │
                  │ Provenance       │
                  └────────┬─────────┘
                           │
                    Resolution +
                  State Reconciliation
                           │
                           ▼
                  Executable Intent
                           │
                           ▼
                         Trust
                           │
                  ┌────────┼────────┐
                  ▼        ▼        ▼
               Action   Clarify  Escalate/Reject
                  │
                  ▼
               Execution
                  │
                  ▼
              Verification
                  │
                  ▼
                Outcome

The Intent Model is therefore the semantic contract connecting interpretation and resolution to Trust, execution, and Outcome verification.

It does not itself authorize, execute, or verify.

⸻

74. Final Definition

The Intent Model is Noema’s canonical structural representation of an Actor’s intended objective, including the Resources, Entities, Parameters, Scope, Context, Constraints, Preferences, Expected Outcome, semantic relationships, provenance, identity, and version required to resolve, govern, execute, and verify that Intent.

The shortest canonical formulation is:

An Intent is a first-class, typed, versioned semantic object that captures who wants what, what it concerns, under which conditions and scope, toward which Expected Outcome, and with what provenance, without coupling that meaning to how the system eventually executes it.