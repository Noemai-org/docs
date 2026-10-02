> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Engine

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/intent-engine.md

⸻

1. Definition

The Intent Engine is Noema’s architectural component responsible for transforming an Actor’s expressed objective into a canonical, sufficiently resolved Intent that can proceed through Validation, Trust, and, ultimately, execution.

The Intent Engine establishes what the Actor intends to accomplish.

It does not:

* authorize execution
* establish Trust
* execute Actions
* own authoritative external business state
* determine how an Intent is operationally fulfilled

Its responsibility is to construct, resolve, version, and maintain canonical Intent.

The canonical relationship is:

Human Expression
      ↓
Interpretation
      ↓
Candidate Intent
      ↓
Intent Engine
      ↓
Canonical Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contracts
      ↓
Execution
      ↓
Outcome

⸻

2. Architectural Responsibility

The Intent Engine owns the semantic lifecycle between an Actor’s expression and a sufficiently resolved Intent.

It is responsible for:

* constructing Intent representations
* resolving semantic references
* identifying ambiguity
* identifying missing semantic information
* incorporating permitted context
* applying deterministic resolution rules
* requesting clarification
* maintaining Intent state
* maintaining Intent versions
* preserving semantic provenance
* identifying semantic requirements
* determining when an Intent is sufficiently resolved for Validation

The Intent Engine must not silently cross into:

* Validation authority
* Trust authority
* authorization
* execution planning authority
* execution
* external business-state ownership

These remain separate architectural responsibilities.

⸻

3. The Intent Boundary

The Intent Engine is the boundary between probabilistic interpretation and canonical semantic state.

                 Actor
                   │
                   ▼
           Human Expression
                   │
                   ▼
             Interpretation
                   │
                   ▼
          Candidate Intent
                   │
                   ▼
          ┌─────────────────┐
          │  Intent Engine  │
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
   Clarification       Canonical Intent
                              │
                              ▼
                         Validation
                              │
                              ▼
                            Trust

A model may propose an interpretation.

The Intent Engine establishes whether that interpretation can become canonical Intent.

Therefore:

Model Output
    ↓
Candidate Interpretation
    ↓
Intent Engine
    ↓
Canonical Intent

not:

Model Output
    ↓
Canonical Intent

⸻

4. Core Principle

Noema must preserve the distinction between:

What the Actor expressed

and:

What Noema has established the Actor intends.

Natural-language expression is evidence for semantic interpretation.

It is not itself the canonical Intent representation.

Likewise, a plausible model interpretation is not automatically an established Intent.

Therefore:

Plausible Interpretation
        ≠
Canonical Intent

The Intent Engine exists to establish that boundary.

⸻

5. Intent Engine Is Not the AI Model

The Intent Engine must not be equivalent to an LLM or other probabilistic model.

A model may:

* interpret language
* extract entities
* identify candidate objectives
* identify possible references
* propose parameters
* identify potential contextual relationships
* propose clarification questions
* construct candidate Intent objects

The Intent Engine determines whether those outputs satisfy the requirements for canonical Intent.

Therefore:

AI Model
   ↓
Candidate Interpretation
   ↓
Intent Engine
   ↓
Canonical Intent

The model is an input to the semantic process.

It is not the authority over Intent state.

⸻

6. Intent Engine Inputs

The Intent Engine may consume:

* Actor expression
* conversation context
* an existing Intent
* Actor identity
* authorized contextual information
* relevant business context
* domain vocabulary
* semantic rules
* deterministic defaults
* prior clarification responses
* permitted external evidence
* model-generated candidate interpretations

Every material input should retain provenance.

The Intent Engine must distinguish, where applicable:

ACTOR
MODEL
CONTEXT
EXTERNAL_EVIDENCE
DETERMINISTIC_RULE
DEFAULT
CLARIFICATION

These sources must not be silently conflated.

⸻

7. Intent Engine Outputs

The Intent Engine may produce:

* canonical Intent
* updated Intent version
* partially resolved Intent
* unresolved Intent
* semantic requirements
* ambiguity records
* clarification requirements
* clarification requests
* resolution provenance
* Intent state transitions
* candidate interpretations where canonical resolution is not yet possible

A resolved Intent becomes eligible for Validation.

It does not automatically become trusted.

Intent Engine
      ↓
Resolved Intent
      ↓
Validation
      ↓
Trust

⸻

8. Canonical Intent Construction

The Intent Engine constructs Intent using Noema’s canonical Intent ontology.

Conceptually:

Intent {
    id
    version
    actor
    objective
    action
    subject
    parameters
    context
    constraints
    desired_outcome
    required_capabilities
    provenance
    state
}

The exact Intent schema belongs to the canonical Intent specification.

The Intent Engine must not create competing application-specific semantic representations where the canonical ontology already defines the relevant concept.

⸻

9. Intent Resolution

Intent resolution establishes the semantic meaning of an Actor expression.

For example:

"Send ₦50,000 to John."

may establish:

objective = transfer_funds
amount = ₦50,000
recipient = John

However, if multiple persons named John are possible:

recipient = AMBIGUOUS

The Intent Engine must not arbitrarily select one.

Instead:

Intent
   ↓
Ambiguity Detected
   ↓
Clarification Required

⸻

10. Resolution Is Not Guessing

The Intent Engine may use contextual evidence to resolve meaning where that evidence establishes the interpretation.

It must not treat probability alone as semantic authority.

For example:

John A
John B
John C

If authoritative context establishes that the Actor selected John B, the Intent may resolve to John B.

If the system merely estimates that John B is the most likely interpretation, the Intent remains unresolved.

The governing principle is:

Plausibility ≠ Semantic Establishment

⸻

11. Clarification as a First-Class Operation

Clarification is a first-class Intent Engine operation.

When required semantic information cannot be established, the Engine should produce a structured clarification requirement.

Example:

Intent:
    action = TRANSFER
    amount = ₦50,000
    recipient = AMBIGUOUS
Requirement:
    recipient identity must be established

The Intent may enter:

WAITING_FOR_CLARIFICATION

The clarification request should target the unresolved semantic requirement.

⸻

12. Targeted Clarification

Clarification should establish the smallest missing semantic condition necessary to continue.

Instead of:

Please provide more information.

the Engine should identify the actual ambiguity:

Which John do you mean: John A or John B?

The Intent Engine should not request information that has already been established.

⸻

13. Contextual Resolution

Context may establish Intent information.

Relevant context may include:

* current conversation
* active resource
* Actor-selected entity
* prior explicit reference
* organizational context
* temporal context
* authoritative system state
* previously resolved Intent information

Context must be applied according to explicit resolution rules.

Context is not unlimited permission to infer.

Therefore:

Context
   ↓
may establish meaning

but not:

Context
   ↓
may establish authority

Authorization remains a Trust concern.

⸻

14. Intent State

The Intent Engine maintains semantic Intent state.

Conceptual states include:

CREATED
RESOLVING
UNRESOLVED
CLARIFICATION_REQUIRED
RESOLVED
SUPERSEDED
CANCELLED
EXPIRED

The exact lifecycle belongs to the Intent specification.

Intent state must not be substituted with Trust state.

For example:

Intent State:
RESOLVED
Trust State:
WAITING_FOR_APPROVAL

These are valid simultaneous states because they represent different dimensions.

⸻

15. Intent State vs Trust State

This distinction is foundational.

Intent state answers:

What is the semantic lifecycle of the Intent?

Trust state answers:

What is the current execution eligibility of the Intent?

Therefore:

Intent
 ├── Intent State
 └── Trust State

An Intent may therefore be:

RESOLVED
+
WAITING_FOR_APPROVAL

or:

RESOLVED
+
READY

The Intent Engine owns semantic Intent state.

The Trust subsystem owns Trust state.

⸻

16. Intent Versioning

An Intent must be versioned whenever its canonical semantic representation materially changes.

Example:

Intent v1
recipient = John
      ↓
clarification
      ↓
Intent v2
recipient = customer_123

The previous representation must remain reconstructible.

Intent versioning supports:

* provenance
* auditability
* revalidation
* Trust re-evaluation
* debugging
* reproducibility
* historical reconstruction

A material semantic change must never silently overwrite historical Intent state.

⸻

17. Material Intent Changes

Material changes may include:

* Actor changes
* objective changes
* Action changes
* target changes
* resource changes
* amount changes
* destination changes
* constraints changes
* desired outcome changes
* execution-relevant parameter changes
* material contextual assumption changes

A material change must trigger the appropriate downstream Validation and Trust re-evaluation.

Intent v1
   ↓
Material Change
   ↓
Intent v2
   ↓
Validation
   ↓
Trust Evaluation

A previous Trust decision must not silently transfer to a materially changed Intent.

⸻

18. Non-Material Updates

Not every update requires a new semantic Intent version.

Examples may include:

* internal processing metadata
* evaluation identifiers
* observability metadata
* non-semantic timestamps

The implementation should distinguish semantic changes from operational metadata.

The relevant criterion is whether the change can materially affect:

* Intent meaning
* semantic validity
* execution eligibility

⸻

19. Intent Provenance

The Intent Engine must preserve provenance for material semantic claims.

Conceptually:

Field:
    recipient
Value:
    customer_123
Source:
    ACTOR_CLARIFICATION
Evidence:
    clarification_event_456
Timestamp:
    ...

Possible provenance sources include:

ACTOR
MODEL
CONTEXT
EXTERNAL_EVIDENCE
DETERMINISTIC_RULE
DEFAULT
CLARIFICATION

Provenance allows Noema to distinguish established information from inferred information.

⸻

20. Candidate Intent

Noema must distinguish:

Candidate Intent

from:

Canonical Intent

A Candidate Intent represents a possible semantic interpretation.

A Canonical Intent represents an interpretation established by the Intent Engine.

This prevents probabilistic model output from silently becoming authoritative system state.

⸻

21. Multiple Candidate Interpretations

An expression may legitimately produce multiple candidates.

Example:

"Cancel the subscription."

Possible targets:

Subscription A
Subscription B
Subscription C

The Intent Engine should preserve this ambiguity until it can be resolved through:

* explicit Actor clarification
* authoritative context
* deterministic semantic rules
* authoritative evidence

It must not collapse candidates arbitrarily.

⸻

22. Deterministic Resolution Rules

Where semantic resolution depends on deterministic rules, those rules should be explicit and versioned.

Conceptually:

Resolve(
    CandidateIntent,
    Context,
    Evidence,
    ResolutionRules
)
→ ResolutionResult

Given the same relevant inputs and rule versions, deterministic resolution should be reproducible.

Model variability must not silently alter a deterministic resolution outcome.

⸻

23. Defaults

Defaults may be used only where Intent semantics explicitly permit them.

For example:

currency = account.default_currency

may be valid if the account’s authoritative currency is defined as the canonical source.

But:

recipient = most_recent_contact

must not be silently assumed merely because it appears likely.

Every semantic default should have:

* an explicit rule
* defined scope
* provenance
* deterministic basis

Defaults must never become a mechanism for hiding ambiguity.

⸻

24. Semantic Completeness

An Intent is semantically complete when the information necessary to establish its intended meaning has been resolved.

Semantic completeness does not establish:

* structural validity
* authorization
* Trust
* capability availability
* execution readiness
* execution success

Therefore:

Semantically Complete
        ≠
Valid
        ≠
Trusted
        ≠
Executed
        ≠
Successful

⸻

25. Intent Requirements

The Intent Engine may identify machine-readable semantic requirements.

Example:

Intent:
    action = TRANSFER
    amount = ₦50,000
    recipient = ?
Requirement:
    recipient identity required

Conceptually:

Requirement {
    code
    field
    description
    source
    blocking
    resolvable
}

The exact schema belongs to the canonical Intent ontology.

⸻

26. Intent Engine vs Validation

The Intent Engine establishes semantic Intent.

Validation determines whether the resulting Intent satisfies structural and applicability requirements.

Therefore:

Intent Engine
      ↓
Canonical Intent
      ↓
Validation

For example:

Intent Engine:
recipient = customer_123
Validation:
customer_123 exists

The Intent Engine should not become a duplicate Validation Engine.

⸻

27. Intent Engine vs Trust

The Intent Engine does not determine whether an Intent may execute.

After semantic resolution:

Resolved Intent
      ↓
Validation
      ↓
Trust

Trust may establish states such as:

WAITING
BLOCKED
READY

The Intent Engine must not convert:

RESOLVED

into:

TRUSTED

⸻

28. Intent Engine and Context Engine

The Intent Engine consumes context.

The Context Engine is responsible for acquiring, organizing, and maintaining contextual information.

Therefore:

Context Engine
      ↓
Context
      ↓
Intent Engine
      ↓
Resolved Intent

The Intent Engine should not become the authoritative owner of all contextual data.

It should reference contextual information according to explicit provenance and dependency rules.

⸻

29. Intent Engine and Action Graph

The Intent Engine establishes the Actor’s semantic objective.

The Action Graph establishes an explicit operational structure for fulfilling that objective.

Therefore:

Intent
   ↓
Action Graph
   ↓
Actions
   ↓
Action Contracts
   ↓
Execution

The Intent Engine may identify the semantic Action or objective that an Action Graph must ultimately satisfy.

It does not determine the complete execution structure.

That responsibility belongs to the Action Graph and associated planning architecture.

⸻

30. Intent Engine and Execution Planning

The architectural distinction is:

Intent Engine
"What does the Actor intend?"

versus:

Action Graph / Planner
"How can that Intent be fulfilled?"

The Intent Engine must not prematurely collapse semantic meaning into a specific execution sequence.

For example:

Intent:
Renew my card.

does not itself establish:

Check eligibility
→ Verify address
→ Request renewal
→ Confirm renewal
→ Initiate delivery

Those are execution-structure concerns.

⸻

31. Intent and Objective

The Intent Engine must preserve the distinction between:

* objective
* Action
* execution strategy

An Actor may express:

“I need my card renewed.”

The objective may be:

renew_card

The eventual Action Graph may contain:

CHECK_ELIGIBILITY
VERIFY_ADDRESS
REQUEST_REPLACEMENT
CONFIRM_REQUEST

The Intent Engine establishes the objective.

It does not need to encode the eventual execution sequence into the Intent itself.

⸻

32. Intent and Action

An Intent may contain an explicit Action where the Actor’s expression is operationally specific.

Example:

"Cancel subscription 123."

may establish:

objective = cancel_subscription
target = subscription_123

The eventual execution structure may still contain multiple Actions.

Therefore:

Intent
   ↓
Objective
   ↓
Action Graph
   ↓
Actions

The semantic objective remains distinct from its operational realization.

⸻

33. Composite Intents

A single Actor expression may contain multiple objectives.

Example:

“Cancel my old subscription and move the balance to my new account.”

The Intent Engine may represent this as a composite Intent or related Intent components, according to the canonical Intent model.

The representation must preserve:

* component identity
* dependencies
* ordering requirements
* shared constraints
* atomicity requirements
* provenance

The Intent Engine must not infer permission for partial execution merely because the components can be separated.

⸻

34. Intent Relationships

Intent relationships should be explicit where they materially affect lifecycle or provenance.

Examples include:

SUPERSEDES
DERIVED_FROM
DEPENDS_ON
CHILD_OF
COMPOSED_OF
CLARIFIES
REPLACES

These relationships allow Noema to reconstruct how semantic state evolved.

⸻

35. Conversational Continuity

Conversation may provide information required to resolve an existing Intent.

Example:

Actor:
"Send ₦50,000 to John."
Noema:
"Which John?"
Actor:
"John from Finance."

The second response should resolve the existing Intent rather than silently creating an unrelated semantic object.

Conceptually:

Expression 1
    ↓
Intent v1
    ↓
Clarification
    ↓
Expression 2
    ↓
Intent v2

The relationship must remain auditable.

⸻

36. Intent Supersession

An Actor may materially change the objective.

Example:

"Transfer ₦50,000."
        ↓
"Actually, make it ₦75,000."

The Intent Engine must represent the material change explicitly.

The previous version becomes superseded rather than silently rewritten.

Downstream Validation and Trust associated with the previous version must not automatically apply to the new version.

⸻

37. Cancellation

An Actor may cancel an Intent before execution.

Cancellation should be represented as an explicit lifecycle event:

RESOLVED
   ↓
intent.cancelled
   ↓
CANCELLED

Cancellation must remain distinct from:

BLOCKED
FAILED

because these states have different causes and lifecycle meanings.

⸻

38. Intent Expiration

Some Intents may have temporal validity.

Example:

valid_until = 18:00

After expiration, the Intent may require re-resolution, revalidation, or another explicitly defined lifecycle transition.

The Intent Engine must not assume that a previously resolved Intent remains semantically applicable indefinitely.

⸻

39. External Evidence

The Intent Engine may consume external evidence when required to establish meaning.

Example:

Actor:
"Renew my card ending in 1234."
Card Registry:
card_1234 belongs to Actor

The evidence may establish the target resource.

The external system remains authoritative for the underlying business fact.

Noema should retain:

* evidence reference
* provenance
* relevant evaluation identity
* applicable timestamp

⸻

40. Unknown Information

The Intent Engine must distinguish:

KNOWN
UNKNOWN
AMBIGUOUS
MISSING

These states are not interchangeable.

For example:

recipient = UNKNOWN

does not mean:

recipient = DENIED

and does not mean:

recipient = MOST_LIKELY_CANDIDATE

If required semantic information is unknown or ambiguous, the Intent must not become resolved merely to permit downstream processing.

⸻

41. No Silent Semantic Mutation

The Intent Engine must not modify the Actor’s objective merely to satisfy downstream requirements.

For example:

Actor:

"Cancel my subscription."

must not silently become:

cancel subscription_123

unless canonical resolution rules and available evidence establish that subscription_123 is the intended target.

Semantic convenience is not sufficient justification for mutation.

⸻

42. Intent Resolution Determinism

Where deterministic rules govern resolution, the result should be reproducible from:

Intent Input
+
Context
+
Evidence
+
Resolution Rules
+
Rule Versions

Model variability may exist upstream.

The canonical resolution process must preserve explicit provenance for any model-derived information that enters the Intent.

⸻

43. Model Confidence

Model confidence may be retained as metadata where useful.

However:

confidence ≠ resolution

A model may report:

recipient confidence = 0.99

while the Intent remains unresolved because multiple recipients satisfy the candidate interpretation.

Confidence can inform processing.

It cannot independently establish canonical semantic truth.

⸻

44. Intent Engine Errors

Intent Engine errors should be structured and machine-readable.

Examples include:

AMBIGUOUS_REFERENCE
MISSING_REQUIRED_MEANING
UNSUPPORTED_INTENT
INVALID_INTENT_STRUCTURE
CONTEXT_INSUFFICIENT
REFERENCE_UNRESOLVED
CONFLICTING_CONTEXT
RESOLUTION_RULE_FAILURE

Human-readable explanations may accompany these codes.

Machine-readable error identity remains canonical.

⸻

45. Resolution Result

Conceptually:

IntentResolutionResult {
    status
    intent
    requirements
    ambiguities
    evidence
    provenance
    rule_versions
}

Possible statuses include:

RESOLVED
UNRESOLVED
CLARIFICATION_REQUIRED
INVALID
UNKNOWN

The exact result schema must remain aligned with the canonical Intent ontology and Validation model.

⸻

46. Intent Engine Events

Conceptual events include:

intent.created
intent.interpreted
intent.resolution_started
intent.resolved
intent.ambiguous
intent.clarification_required
intent.clarification_received
intent.updated
intent.superseded
intent.cancelled
intent.expired

These are architectural event concepts rather than a final event protocol.

Material events must preserve relevant provenance.

⸻

47. Re-Resolution

Re-resolution may be required when material semantic dependencies change.

Examples include:

* Actor provides clarification
* referenced resource changes
* contextual reference becomes unavailable
* external evidence changes
* Intent is materially amended
* a resolution rule changes where that rule is semantically material

Re-resolution must produce an explicit new resolution result.

A previous resolution must not silently remain authoritative when its semantic dependencies have materially changed.

⸻

48. Intent Dependency Graph

Intent resolution may depend on external semantic facts.

Conceptually:

Intent
  │
  ├── Actor
  ├── Resource
  ├── Context
  ├── Evidence
  └── Resolution Rules

These dependencies should be identifiable where they can affect semantic validity.

This allows Noema to determine when selective re-resolution is required rather than rebuilding every Intent after every contextual event.

⸻

49. Partial Intent Resolution

The Intent Engine may maintain a partially resolved Intent when useful.

Example:

action    = TRANSFER
amount    = ₦50,000
recipient = UNKNOWN
currency  = NGN

The unresolved portion should remain explicit.

Partial semantic state is preferable to silently inventing the missing information.

⸻

50. Intent Engine Contract

Conceptually:

ResolveIntent(
    Expression,
    Context,
    Evidence,
    ExistingIntent,
    ResolutionRules
)
→ IntentResolutionResult

The result should be:

* structured
* explicit about uncertainty
* versioned
* traceable
* inspectable
* deterministic where deterministic rules apply

The operation establishes semantic state.

It does not grant execution authority.

⸻

51. Intent Engine Auditability

The Intent Engine should make it possible to reconstruct:

1. the original Actor expression
2. the candidate interpretation
3. relevant context
4. evidence used for resolution
5. clarification requirements
6. clarification responses
7. applicable resolution rules
8. Intent versions
9. Intent state transitions
10. the resulting canonical Intent

This does not require retaining private model chain-of-thought.

It requires retaining semantic provenance and state necessary to reconstruct the canonical decision.

⸻

52. Intent Engine and Safety

Semantic uncertainty must not become execution authority.

Therefore:

AMBIGUOUS
    ↓
CLARIFICATION / UNRESOLVED

not:

AMBIGUOUS
    ↓
BEST GUESS
    ↓
EXECUTION

Likewise:

UNKNOWN
    ↓
UNKNOWN

not:

UNKNOWN
    ↓
ASSUMED TRUE

The Trust subsystem subsequently applies execution-governance controls.

⸻

53. Failure Modes

The Intent Engine should distinguish semantic failure modes.

Semantic ambiguity

The Actor’s meaning has multiple plausible interpretations.

→ CLARIFICATION_REQUIRED

Missing information

A required semantic field has not been established.

→ UNRESOLVED

Conflicting context

Available evidence supports incompatible interpretations.

→ UNRESOLVED / CLARIFICATION_REQUIRED

Unsupported objective

No canonical Intent representation can express the requested objective.

→ UNSUPPORTED

External information unavailable

Required evidence cannot currently be obtained.

→ UNKNOWN / NOT_RESOLVED

These states must not collapse into an undifferentiated generic failure.

⸻

54. Intent Engine and Validation Boundary

The architectural boundary is:

Intent Engine
    │
    │ establishes semantic meaning
    ▼
Canonical Intent
    │
    │ establishes structural/applicability validity
    ▼
Validation
    │
    │ establishes execution eligibility
    ▼
Trust

The Intent Engine must not absorb Validation or Trust responsibilities merely because some checks are necessary to resolve meaning.

Where a fact is needed for semantic resolution, the Intent Engine may consume that fact.

Whether the resulting Intent is valid or trusted remains downstream.

⸻

55. Intent Engine and Action Graph Boundary

The distinction between Intent and Action Graph must remain explicit.

Intent:
"What does the Actor want?"
Action Graph:
"What explicit Actions and dependencies can fulfill it?"

For example:

Intent:
Replace my expired card.

may produce an Action Graph containing:

CHECK_CARD_STATUS
        ↓
CHECK_REPLACEMENT_ELIGIBILITY
        ↓
CREATE_REPLACEMENT_REQUEST
        ↓
VERIFY_REQUEST_ACCEPTED

The Intent Engine establishes the objective.

The Action Graph establishes the operational structure.

⸻

56. Intent Engine and Execution Boundary

The Intent Engine does not execute Actions.

The canonical downstream path is:

Resolved Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contract
      ↓
Consumer
      ↓
Execution
      ↓
Outcome

Resolving an Intent therefore never constitutes permission to execute.

⸻

57. Intent Expiration and Material Context

A previously resolved Intent may become semantically stale when material contextual dependencies change.

Examples:

* referenced resource is no longer identifiable
* contextual reference changes
* required semantic evidence becomes invalid
* Actor materially changes the request
* temporal validity expires

The appropriate response is explicit re-resolution or lifecycle transition.

Noema must not silently preserve stale semantic assumptions.

⸻

58. Intent History

Intent history must remain reconstructible.

For a stable Intent identity:

intent_id = stable identity
version   = semantic revision

Noema should be able to reconstruct:

Intent v1
   ↓
Clarification
   ↓
Intent v2
   ↓
Material amendment
   ↓
Intent v3

This history provides the semantic basis for downstream Validation and Trust decisions.

⸻

59. Canonical Intent Engine Flow

The canonical lifecycle is:

                    Actor Expression
                           │
                           ▼
                    Interpretation
                           │
                           ▼
                    Candidate Intent
                           │
                           ▼
                  Intent Construction
                           │
                           ▼
                  Context Integration
                           │
                           ▼
                 Semantic Resolution
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
             Unresolved          Resolved
                  │                 │
                  ▼                 ▼
          Clarification         Validation
                  │                 │
                  └───────┐         ▼
                          │       Trust
                          │         │
                          └─────────┘

The cycle continues until:

* semantic requirements are established
* the Intent is resolved
* the Intent is cancelled
* the Intent expires
* the objective is unsupported
* or another explicitly defined terminal state is reached.

⸻

60. Intent Engine State Transition Principle

Intent state may change only because of an explicitly defined semantic event, dependency transition, clarification, evidence change, or deterministic re-evaluation.

It must not change merely because:

* a model became more confident
* a different model generated a different interpretation
* a prompt was reformulated
* a model produced a different candidate
* a downstream executor requires additional information

Semantic state must be established through the defined Intent Engine lifecycle.

⸻

61. Architectural Invariants

Invariant 1

The Intent Engine owns semantic Intent construction and resolution, not external business state.

Invariant 2

Model output is not automatically canonical Intent.

Invariant 3

The Intent Engine must not guess materially ambiguous meaning.

Invariant 4

Unknown semantic information must not be silently converted into known information.

Invariant 5

Clarification is a first-class Intent lifecycle operation.

Invariant 6

Intent state and Trust state are separate dimensions.

Invariant 7

A resolved Intent is not necessarily valid for execution.

Invariant 8

A resolved Intent is not necessarily trusted.

Invariant 9

Material Intent changes require a new semantic version or an equivalent reconstructible representation.

Invariant 10

Material semantic provenance must be retained.

Invariant 11

Deterministic resolution rules must be explicit and versionable.

Invariant 12

Context may establish meaning but does not establish execution authority.

Invariant 13

The Intent Engine does not authorize Actions.

Invariant 14

The Intent Engine does not execute Actions.

Invariant 15

External systems remain authoritative for external business facts.

Invariant 16

A previous Trust decision must not silently transfer to a materially changed Intent.

Invariant 17

Semantic ambiguity must remain explicit until resolved.

Invariant 18

Intent history must be reconstructible.

Invariant 19

Defaults must not conceal unresolved semantic ambiguity.

Invariant 20

Model confidence cannot independently establish canonical semantic resolution.

Invariant 21

The Intent Engine must not collapse semantic resolution into an execution plan.

Invariant 22

Canonical Intent establishes semantic meaning; Validation, Trust, Action Graph, Contracts, and Execution establish subsequent lifecycle responsibilities.

⸻

62. Canonical Mental Model

The Intent Engine can be reduced to four questions:

1. What did the Actor express?
2. What could that expression mean?
3. Which meaning has actually been established?
4. Is the resulting Intent sufficiently resolved to enter Validation?

This produces:

Actor Expression
       ↓
Interpretation
       ↓
Candidate Intent
       ↓
Semantic Resolution
       ↓
Canonical Intent
       ↓
Validation
       ↓
Trust
       ↓
Action Graph
       ↓
Action Contracts
       ↓
Execution
       ↓
Outcome

⸻

63. Final Definition

The Intent Engine is Noema’s semantic control layer for constructing, resolving, versioning, and maintaining canonical Intent between Actor expression and deterministic downstream Validation and Trust evaluation.

Its central invariant is:

Noema may use probabilistic models to propose what an Actor means, but the Intent Engine must preserve the distinction between a proposed interpretation and a canonically established Intent.

The Intent Engine establishes what the Actor intends.

Validation establishes whether that Intent is structurally and semantically valid.

Trust establishes whether that Intent may proceed.

The Action Graph establishes how the trusted objective may be operationally fulfilled.

Action Contracts establish the executable interfaces, obligations, and constraints governing individual Actions.

Execution establishes what is actually performed.

Outcome records what actually happened.

The boundaries therefore remain explicit:

Interpretation
      ↓
Intent Engine
      ↓
Canonical Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contracts
      ↓
Execution
      ↓
Outcome

Canonical boundary:

The Intent Engine determines what the Actor intends.
It does not determine whether the Actor is authorized,
how the Intent must be executed, or what actually happened.