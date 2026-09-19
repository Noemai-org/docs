Intent Engine

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/intent-engine.md

⸻

1. Definition

The Intent Engine is the architectural component responsible for transforming interpreted human intent into a canonical, resolved, validated Intent representation that can proceed through Noema’s Trust and execution lifecycle.

The Intent Engine is responsible for establishing what the Actor intends to accomplish.

It does not authorize execution.

It does not execute Actions.

It does not own authoritative business state.

Its responsibility is:

Understand, construct, resolve, and maintain canonical Intent.

The canonical relationship is:

Human Expression
      ↓
AI Interpretation
      ↓
Intent Candidate
      ↓
Intent Engine
      ↓
Canonical Intent
      ↓
Validation
      ↓
Trust
      ↓
Execution

⸻

2. Architectural Responsibility

The Intent Engine owns the semantic lifecycle between an Actor’s expression and a sufficiently resolved Intent.

It is responsible for:

* constructing Intent representations
* resolving semantic ambiguity
* identifying required information
* incorporating permitted context
* maintaining Intent state
* requesting clarification
* applying deterministic semantic rules
* preserving provenance
* producing Intent versions
* determining when an Intent is sufficiently resolved for Validation

The Intent Engine must not silently cross into:

* authorization
* Trust evaluation
* execution
* business-state ownership

These remain separate architectural responsibilities.

⸻

3. Intent Engine Boundary

The Intent Engine sits between probabilistic interpretation and deterministic downstream control.

                 Actor
                   │
                   ▼
             Human Expression
                   │
                   ▼
            AI Interpretation
                   │
                   ▼
          ┌──────────────────┐
          │   Intent Engine  │
          └────────┬─────────┘
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
                              │
                              ▼
                           Action

The Intent Engine therefore acts as a semantic boundary.

The AI may propose interpretations.

The Intent Engine establishes the canonical Intent representation.

⸻

4. Intent Engine vs AI Model

The Intent Engine must not be equivalent to an LLM or other model.

An AI model may:

* interpret language
* extract entities
* infer candidate objectives
* identify possible references
* propose missing context
* generate clarification questions
* construct candidate Intent objects

The Intent Engine determines whether those outputs can become canonical Intent.

Therefore:

Model Output
     ↓
Candidate Interpretation
     ↓
Intent Engine
     ↓
Canonical Intent

Not:

Model Output
     ↓
Canonical Intent

The model is an input to the Intent Engine.

It is not the authority over Intent state.

⸻

5. Core Principle

The Intent Engine must preserve the distinction between:

What the Actor said

and:

What Noema has established the Actor intends

Natural language is evidence for Intent interpretation.

The canonical Intent is the structured representation established after interpretation and resolution.

Therefore:

Noema must never confuse a plausible interpretation with an established Intent.

⸻

6. Intent Engine Inputs

The Intent Engine may consume:

* Actor expression
* conversation context
* previously established Intent
* Actor identity
* authorized contextual information
* relevant business context
* available capabilities
* domain vocabulary
* semantic rules
* deterministic defaults
* prior clarification responses
* external evidence permitted for Intent resolution
* model-generated candidate interpretations

Inputs must retain provenance.

The Intent Engine must be able to distinguish:

Actor-provided information
Model-inferred information
System-provided context
External evidence
Deterministic defaults

These sources must not be silently conflated.

⸻

7. Intent Engine Outputs

The Intent Engine may produce:

* canonical Intent
* updated Intent version
* unresolved Intent
* clarification requirement
* clarification request
* semantic requirements
* resolution provenance
* Intent state transition
* candidate interpretations where resolution is not yet possible

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

8. Intent Construction

The Intent Engine constructs Intent from available semantic information.

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

The exact Intent schema is defined by the canonical Intent ontology.

The Intent Engine must use that canonical representation rather than creating application-specific semantic representations.

⸻

9. Intent Resolution

Intent resolution establishes the semantic meaning of an expression.

Example:

"Send ₦50,000 to John."

The Intent Engine may establish:

objective = transfer_funds
amount = ₦50,000
recipient = John

But if multiple people named John exist:

recipient = ambiguous

The Intent Engine must not select one merely because it appears likely.

Instead:

Intent
   ↓
Ambiguity detected
   ↓
Clarification required

⸻

10. Resolution Is Not Guessing

The Intent Engine may use contextual evidence to resolve ambiguity when the evidence establishes a canonical interpretation.

It must not use probability alone as authority.

For example:

John A
John B
John C

If the Actor explicitly identifies John B through an authoritative contextual reference, the Intent may resolve to John B.

If the system merely estimates that John B is probably intended, the Intent remains unresolved.

The principle is:

Plausibility is not semantic establishment.

⸻

11. Clarification

Clarification is a first-class Intent Engine operation.

When required semantic information cannot be established, the Intent Engine should generate a structured clarification requirement.

Example:

Intent:
    action = transfer
    recipient = ambiguous
    amount = ₦50,000
Requirement:
    recipient identity must be established

The resulting state may be:

WAITING_FOR_CLARIFICATION

The clarification request should identify the missing semantic information without unnecessarily exposing internal implementation details.

⸻

12. Clarification Must Be Targeted

Clarification should resolve the smallest missing semantic condition necessary to continue.

Instead of:

“Please provide more information.”

Prefer a request that establishes the unresolved field.

For example:

“Which John do you mean: John A or John B?”

The Intent Engine should avoid asking for information that is already established.

⸻

13. Contextual Resolution

Context may resolve Intent information.

Relevant context may include:

* current conversation
* active resource
* Actor-selected entity
* prior explicit reference
* organizational context
* temporal context
* authoritative system state
* previously resolved Intent information

Context must be used according to explicit resolution rules.

Context is not unlimited permission to infer.

Therefore:

Context
   ↓
may resolve meaning

but not:

Context
   ↓
may manufacture authority

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

The exact lifecycle is defined by the Intent specification.

The Intent Engine should not use Trust states as substitutes for Intent states.

For example:

Intent State:
RESOLVED
Trust State:
WAITING_FOR_APPROVAL

These represent different dimensions.

⸻

15. Intent State vs Trust State

The distinction is foundational.

Intent state answers:

What is the semantic lifecycle of the Intent?

Trust state answers:

What is the current execution eligibility of the Intent?

Therefore:

Intent
 ├── Intent State
 └── Trust State

An Intent can be:

RESOLVED
+
WAITING_FOR_APPROVAL

or:

RESOLVED
+
READY

The Intent Engine owns the former.

The Trust subsystem owns the latter.

⸻

16. Intent Versioning

An Intent should be versioned whenever its canonical semantic representation materially changes.

Example:

Intent v1
recipient = John
       ↓ clarification
Intent v2
recipient = John_123

The previous representation must remain reconstructible.

Intent versioning supports:

* provenance
* auditability
* revalidation
* Trust re-evaluation
* debugging
* reproducibility
* historical reconstruction

A material semantic change must not silently overwrite history.

⸻

17. Material Intent Changes

Material changes may include:

* Action changes
* Actor changes
* target changes
* resource changes
* amount changes
* destination changes
* constraints changes
* desired outcome changes
* execution-relevant parameters changing
* contextual assumptions changing materially

A material change should trigger the appropriate downstream revalidation and Trust evaluation.

Conceptually:

Intent v1
   ↓
material change
   ↓
Intent v2
   ↓
Validation
   ↓
Trust Evaluation

⸻

18. Non-Material Updates

Not every event necessarily creates a new semantic Intent version.

Examples may include:

* internal processing metadata
* evaluation identifiers
* observability metadata
* non-semantic timestamps

The implementation should distinguish semantic changes from operational metadata.

The canonical criterion is whether the change can materially affect the meaning or execution eligibility of the Intent.

⸻

19. Intent Provenance

The Intent Engine must preserve provenance for semantic claims.

For relevant fields, provenance should identify where the information originated.

Conceptually:

Field:
recipient
Value:
customer_123
Source:
Actor clarification
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

20. Model-Assisted Intent Generation

Models may generate candidate Intent structures.

For example:

Natural Language
      ↓
LLM
      ↓
Candidate Intent

The candidate is then processed by the Intent Engine.

The Engine must establish:

* schema conformity
* required semantic fields
* reference resolution
* ambiguity
* permitted defaults
* contextual consistency
* provenance

The model must not directly establish canonical execution semantics.

⸻

21. Candidate vs Canonical Intent

Noema should distinguish:

Candidate Intent

from:

Canonical Intent

A candidate represents a possible interpretation.

A canonical Intent represents the interpretation established by Noema’s semantic process.

This distinction prevents probabilistic model output from silently becoming system state.

⸻

22. Multiple Candidate Interpretations

An expression may legitimately produce multiple candidates.

Example:

"Cancel the subscription."

Possible interpretations:

Subscription A
Subscription B
Subscription C

The Intent Engine should preserve ambiguity until it can be resolved through:

* explicit Actor clarification
* authoritative context
* deterministic semantic rules
* authoritative evidence

It should not collapse candidates arbitrarily.

⸻

23. Deterministic Resolution Rules

Where semantic resolution depends on deterministic rules, those rules should be explicit and versioned.

Conceptually:

Resolve(
    Candidate Intent,
    Context,
    Evidence,
    Resolution Rules
)
→ Resolution Result

Given the same relevant inputs and rule versions, resolution should be reproducible.

Model-generated variability must not silently alter deterministic resolution outcomes.

⸻

24. Defaults

Defaults may be used only where the Intent semantics explicitly permit them.

Example:

currency = account.default_currency

may be legitimate if the account’s authoritative currency is the canonical source.

But:

recipient = most_recent_contact

must not be silently assumed merely because it is statistically likely.

Every default should have:

* an explicit rule
* a defined scope
* a provenance marker
* a deterministic basis

⸻

25. Semantic Completeness

An Intent is semantically complete when all information required to establish its intended meaning has been resolved.

Semantic completeness does not mean:

* authorization is complete
* Trust is established
* execution capability is available
* execution will succeed

Therefore:

Semantically Complete
        ≠
Trusted
        ≠
Executed
        ≠
Successful

⸻

26. Intent Requirements

The Intent Engine may identify semantic requirements.

Example:

Intent:
    action = transfer
    amount = ₦50,000
    recipient = ?
Requirement:
    recipient identity required

Requirements should be machine-readable.

Conceptually:

Requirement {
    code
    field
    description
    source
    blocking
    resolvable
}

The exact schema remains subject to the canonical ontology.

⸻

27. Intent Engine and Validation

The Intent Engine establishes semantic Intent.

Validation verifies that the resulting Intent satisfies structural and applicability requirements.

Therefore:

Intent Engine
    ↓
Canonical Intent
    ↓
Validation

The Intent Engine should not duplicate the Validation Engine.

For example:

Intent Engine:
recipient = customer_123
Validation:
customer_123 exists

The distinction should remain explicit.

⸻

28. Intent Engine and Trust

The Intent Engine does not determine whether an Intent may execute.

After the Intent becomes sufficiently resolved:

Resolved Intent
      ↓
Validation
      ↓
Trust

Trust may determine:

WAITING
BLOCKED
READY

The Intent Engine must not convert:

resolved

into:

trusted

⸻

29. Intent Engine and Context Engine

The Intent Engine consumes context.

The Context Engine is responsible for acquiring, organizing, and maintaining contextual information.

Therefore:

Context Engine
       │
       ▼
Context
       │
       ▼
Intent Engine
       │
       ▼
Resolved Intent

The Intent Engine should not become the authoritative owner of all contextual data.

It should reference context according to explicit provenance and dependency rules.

⸻

30. Intent Engine and Action Graph

The Intent Engine may identify the objective and semantic Action required to satisfy an Intent.

The Action Graph represents available relationships between:

* Actions
* capabilities
* resources
* dependencies
* preconditions
* outputs
* execution relationships

The Intent Engine may therefore produce an Intent whose Action semantics can later be mapped through the Action Graph.

Conceptually:

Intent
  ↓
Action
  ↓
Action Graph
  ↓
Executable Capability

The Intent Engine does not itself execute the graph.

⸻

31. Intent Engine and Execution Planner

The Intent Engine establishes what the Actor intends.

The Execution Planner determines how that Intent can be fulfilled through available Actions and dependencies.

Therefore:

Intent Engine
"What does the Actor want?"
        ↓
Execution Planner
"How can that objective be fulfilled?"

The distinction prevents planning concerns from contaminating semantic resolution.

⸻

32. Intent Engine and Execution Contract

The Intent Engine does not create final execution authority merely by resolving Intent.

The later lifecycle is:

Resolved Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Selection
      ↓
Execution Contract
      ↓
Execution Consumer

An Execution Contract is therefore downstream of the Intent Engine.

⸻

33. Intent Identity

Each Intent should have a stable identity independent of its versions.

Conceptually:

intent_id = stable identity
version = semantic revision

This allows Noema to distinguish:

the same evolving Intent

from:

a different Intent

The exact identity semantics are defined in the Intent ontology.

⸻

34. Actor Ownership

An Intent must retain its Actor relationship.

The Actor identifies the principal whose objective is being represented.

The Intent Engine must not silently change the Actor because another system or model produces a different interpretation.

Any change to Actor identity is a material semantic event and should be explicitly represented.

⸻

35. Intent and Objective

The Intent Engine should preserve the distinction between:

Objective

and:

Action

An Actor may express:

“I need my card renewed.”

The objective is the desired outcome.

The specific operational Actions required to accomplish it may involve:

* checking eligibility
* selecting a renewal path
* requesting replacement
* updating records
* notifying the Actor

The Intent Engine should capture the objective without prematurely collapsing it into an implementation-specific execution sequence.

⸻

36. Intent and Action

An Intent may identify an explicit Action where the Actor’s request is operationally specific.

Example:

"Cancel subscription 123."

The Intent may represent:

objective = cancel_subscription
target = subscription_123

The eventual execution plan may contain multiple underlying Actions.

Therefore:

Intent
   ↓
Objective
   ↓
Plan
   ↓
Actions

The Intent Engine establishes the semantic objective.

⸻

37. Composite Intents

A single Actor expression may contain multiple objectives.

Example:

“Cancel my old subscription and move the balance to my new account.”

The Intent Engine may represent this as a composite Intent or a set of related Intent components, depending on the canonical Intent model.

The architecture must preserve:

* component identity
* dependencies
* ordering requirements
* shared constraints
* atomicity requirements
* provenance

The Intent Engine must not infer permission for partial execution merely because components can be separated.

⸻

38. Intent Relationships

Intents may have relationships such as:

SUPERSEDES
DERIVED_FROM
DEPENDS_ON
CHILD_OF
COMPOSED_OF
CLARIFIES
REPLACES

These relationships should be explicit where they materially affect lifecycle or provenance.

⸻

39. Conversational Continuity

Conversation may provide information needed to resolve an Intent.

Example:

Actor:

“Send ₦50,000 to John.”

Noema:

“Which John?”

Actor:

“John from Finance.”

The second response should update the existing Intent rather than creating an unrelated semantic object.

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

40. Intent Supersession

An Actor may change their objective.

Example:

"Transfer ₦50,000."

followed by:

"Actually, make it ₦75,000."

The Intent Engine should represent the material change explicitly.

The previous Intent version becomes superseded rather than silently rewritten.

Downstream Validation and Trust decisions associated with the previous version must not automatically apply to the new version.

⸻

41. Cancellation

An Actor may cancel an Intent before execution.

Cancellation should be represented as an explicit lifecycle event.

For example:

RESOLVED
   ↓
intent.cancelled
   ↓
CANCELLED

Cancellation must not be confused with:

BLOCKED
FAILED

These represent different causes and lifecycle meanings.

⸻

42. Intent Expiration

Some Intents may have temporal validity.

Example:

Intent valid until:
18:00

After expiration, the Intent may require re-resolution or become invalid for further processing.

Expiration should be explicit and deterministic.

The Intent Engine should not assume that a previously resolved Intent remains semantically applicable forever.

⸻

43. External Evidence

The Intent Engine may use external evidence where that evidence is necessary to resolve meaning.

For example:

Actor:
"Renew my card ending in 1234."
Card Registry:
card_1234 belongs to Actor

The evidence may establish the target resource.

The external system remains authoritative for the underlying business fact.

Noema retains the evidence reference and provenance.

⸻

44. Unknown Information

The Intent Engine must distinguish:

KNOWN
UNKNOWN
AMBIGUOUS
MISSING

These are not interchangeable.

For example:

recipient = unknown

does not mean:

recipient = denied

and does not mean:

recipient = most likely candidate

Unknown semantic information that is necessary to establish Intent should prevent the Intent from becoming resolved.

⸻

45. No Silent Semantic Mutation

The Intent Engine must not silently modify the Actor’s objective merely to satisfy downstream requirements.

For example:

Actor:

“Cancel my subscription.”

The Engine must not silently transform this into:

cancel subscription_123

unless the canonical resolution rules and available evidence establish that subscription_123 is the intended target.

Semantic convenience is not sufficient justification for mutation.

⸻

46. Intent Engine Determinism

Where deterministic rules govern resolution, the result should be reproducible from:

Intent input
+
Context
+
Evidence
+
Resolution rules
+
Rule versions

Model variability may exist upstream.

The canonical resolution process must preserve explicit provenance for any model-derived information that enters the Intent.

⸻

47. Intent Resolution Confidence

Model confidence may be retained as metadata where useful.

However:

confidence ≠ resolution

A model may report:

recipient confidence = 0.99

while the Intent remains unresolved because multiple recipients satisfy the candidate interpretation.

Confidence can inform processing.

It cannot independently establish canonical semantic truth.

⸻

48. Intent Engine Errors

Errors should be structured.

Examples:

AMBIGUOUS_REFERENCE
MISSING_REQUIRED_MEANING
UNSUPPORTED_INTENT
INVALID_INTENT_STRUCTURE
CONTEXT_INSUFFICIENT
REFERENCE_UNRESOLVED
CONFLICTING_CONTEXT
RESOLUTION_RULE_FAILURE

Human-readable explanations may accompany these codes.

Machine-readable codes remain canonical.

⸻

49. Intent Resolution Result

Conceptually:

ResolutionResult {
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

The exact result schema should remain aligned with the canonical Intent ontology and Validation model.

⸻

50. Intent Engine Event Model

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

These are illustrative architectural events rather than a final protocol.

Each material event should preserve provenance.

⸻

51. Intent Engine Re-Resolution

Re-resolution may be required when material semantic context changes.

Examples:

* Actor provides clarification
* referenced resource changes
* contextual reference becomes unavailable
* external evidence changes
* Intent is materially amended

Re-resolution must produce a new deterministic result.

A previous resolution must not be silently assumed to remain valid when its semantic dependencies have materially changed.

⸻

52. Intent Dependency Graph

Intent resolution may depend on external facts.

Conceptually:

Intent
  │
  ├── Actor
  ├── Resource
  ├── Context
  ├── Evidence
  └── Resolution Rules

Dependencies should be identifiable where they can affect semantic validity.

This enables selective re-resolution rather than rebuilding every Intent after every contextual event.

⸻

53. Intent Engine Auditability

The Intent Engine should make it possible to reconstruct:

1. the original Actor expression
2. the candidate interpretation
3. relevant context
4. evidence used for resolution
5. clarification requests
6. clarification responses
7. resolution rules
8. Intent versions
9. state transitions
10. the final canonical Intent

This does not require retaining private model chain-of-thought.

It requires retaining decision provenance and semantic state.

⸻

54. Intent Engine and Safety

Safety mechanisms must prevent semantic uncertainty from becoming execution authority.

The Intent Engine should therefore enforce:

Ambiguous
    ↓
Clarification / unresolved

not:

Ambiguous
    ↓
Best guess
    ↓
Execution

Similarly:

Unknown
    ↓
Unknown

not:

Unknown
    ↓
Assumed true

The Trust subsystem subsequently applies execution-governance controls.

⸻

55. Intent Engine Failure Modes

The Intent Engine should explicitly distinguish:

Semantic ambiguity

The Actor’s meaning is not sufficiently established.

→ CLARIFICATION_REQUIRED

Missing information

A required semantic field has not been provided.

→ UNRESOLVED

Conflicting context

Available evidence supports incompatible interpretations.

→ UNRESOLVED / CLARIFICATION_REQUIRED

Unsupported objective

No canonical Intent representation can express the requested objective.

→ UNSUPPORTED

External information unavailable

Required contextual evidence cannot currently be obtained.

→ UNKNOWN / NOT RESOLVED

These states should not collapse into a generic failure.

⸻

56. Intent Engine and Partial Information

The Intent Engine may maintain partially resolved Intent when useful.

Example:

action = TRANSFER
amount = ₦50,000
recipient = UNKNOWN
currency = NGN

This is preferable to discarding the entire semantic representation.

The unresolved portion should be explicitly represented.

⸻

57. Intent Engine and Deterministic Defaults

A deterministic default may resolve a field only when:

1. the Intent semantics permit the default
2. the default rule is explicit
3. the source is authoritative or otherwise defined
4. the result is deterministic
5. provenance is retained

Defaults must never be used as a mechanism for hiding ambiguity.

⸻

58. Intent Engine Contract

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
* deterministic where rules apply
* versioned
* traceable
* inspectable
* explicit about uncertainty

⸻

59. Canonical Intent Engine Flow

                 Actor Expression
                        │
                        ▼
                AI Interpretation
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
                 ┌──────┴──────┐
                 │             │
                 ▼             ▼
             Unresolved      Resolved
                 │             │
                 ▼             ▼
          Clarification     Validation
                 │             │
                 └──────┐      ▼
                        │     Trust
                        │      │
                        └──────┘

The loop continues until the semantic requirements necessary for the next lifecycle stage are established or the Intent is explicitly terminated.

⸻

60. Architectural Invariants

Invariant 1

The Intent Engine owns semantic Intent construction and resolution, not business state.

Invariant 2

Model output is not automatically canonical Intent.

Invariant 3

The Intent Engine must not guess materially ambiguous meaning.

Invariant 4

Unknown semantic information must not be silently converted into known information.

Invariant 5

Clarification is a valid Intent lifecycle state.

Invariant 6

Intent state and Trust state are separate dimensions.

Invariant 7

A resolved Intent is not necessarily valid for execution.

Invariant 8

A resolved Intent is not necessarily trusted.

Invariant 9

Material Intent changes require a new semantic version or equivalent reconstructible representation.

Invariant 10

Intent provenance must be retained for material semantic decisions.

Invariant 11

Deterministic resolution rules must be versionable.

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

⸻

61. Canonical Mental Model

The Intent Engine can be reduced to four questions:

1. What did the Actor express?
          ↓
2. What could that expression mean?
          ↓
3. Which meaning has been established?
          ↓
4. Is the resulting Intent sufficiently resolved for Validation?

Which produces:

Expression
    ↓
Interpretation
    ↓
Candidate Intent
    ↓
Resolution
    ↓
Canonical Intent
    ↓
Validation

⸻

62. Final Definition

The Intent Engine is Noema’s semantic control layer for constructing, resolving, versioning, and maintaining canonical Intent between human expression and deterministic downstream validation and Trust evaluation.

Its central invariant is:

Noema may use probabilistic models to propose what an Actor means, but the Intent Engine must preserve the distinction between a proposed interpretation and a canonically established Intent.

The Intent Engine establishes what the Actor intends.

Validation establishes whether that Intent is structurally and semantically valid.

Trust establishes whether that Intent may proceed.

Execution establishes what is actually performed.

The boundaries remain explicit:

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
Execution
      ↓
Outcome