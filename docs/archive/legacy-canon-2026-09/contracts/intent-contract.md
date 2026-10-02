> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/intent-contract.md

⸻

1. Definition

An Intent Contract is the canonical contract that defines the structure, meaning, constraints, provenance, resolution state, and lifecycle of an Intent recognized and managed by Noema.

An Intent represents a desired goal expressed by a Source of Intent without prematurely defining how that goal will be executed.

A Source of Intent may be:

* a human
* an application
* an agent
* an enterprise system
* a workflow
* an API
* another authorized computational process

The Intent Contract is the semantic boundary between an interpreted request and the deterministic systems that contextualize, resolve, evaluate, authorize, plan, and execute that request.

⸻

2. Purpose

The Intent Contract exists to make Intent:

* structured
* explicit
* inspectable
* versionable
* attributable
* resolvable
* traceable
* interface-independent
* integration-independent
* execution-independent

Its purpose is to prevent language interpretation, application conventions, or model output from becoming implicit and untraceable execution authority.

⸻

3. Core Question

The Intent Contract answers:

What is the Source of Intent trying to accomplish?

It does not by itself answer:

* which enterprise system should be called
* whether the request is permitted
* whether the request satisfies Trust requirements
* which Capability should execute
* whether execution succeeded
* what the enterprise Business State currently is
* what the final Outcome of execution is

Those concerns belong to other Noema contracts and domains.

⸻

4. Intent Is Not an Action

An Intent expresses a desired goal.

An Action expresses an executable operation.

For example:

Intent:
"Show me my recent transactions."
Action:
RetrieveTransactions(account_id, date_range)

The Intent Contract describes the first.

The Action Contract describes the second.

The transformation between them must be explicit and auditable.

⸻

5. Intent Is Not Execution

Intent describes the requested goal.

Execution describes what Noema actually attempted or performed.

Therefore:

Intent ≠ Execution

An Intent may exist without execution.

An Execution may fail without invalidating the semantic existence of the original Intent.

An Intent may require clarification, rejection, or escalation before any Execution is created.

⸻

6. Intent Is Not Business State

Intent is not enterprise truth.

For example:

Intent:
"How much money do I have?"
Business State:
Current account balance

The Intent Contract represents the request for the information.

The enterprise System of Record remains authoritative for the balance itself.

⸻

7. Intent Is Not Context

Intent describes the requested goal.

Context provides information necessary to understand, resolve, evaluate, or execute that goal.

For example:

Intent:
"Show my transactions."
Context:
customer identity
account
date range
organization
permissions
channel
locale
time

Context may resolve an incomplete Intent, but it must not silently redefine the requested objective.

⸻

8. Intent Is Not Trust

Intent describes what the Source of Intent wants.

Trust determines whether Noema may safely proceed with the resolved Intent under applicable authority, Policy, evidence, and enterprise conditions.

Therefore:

Intent → Trust Evaluation

not:

Intent = Trust

A valid Intent may still produce:

EXECUTE
CLARIFY
ESCALATE
REJECT

Trust is evaluated against a sufficiently resolved Intent; the Intent Contract itself does not grant execution authority.

⸻

9. Intent Is Not Natural Language

Natural language is one possible input representation.

Intent is the structured semantic representation derived from an input or received directly from another authorized Source of Intent.

Conceptually:

Source of Intent
      ↓
Input Representation
      ↓
Interpretation
      ↓
Intent

The original input should remain attributable to the resulting Intent where available.

Noema must not assume that every Intent originated as natural language.

⸻

10. Source of Intent

Every Intent must identify its Source of Intent.

Possible sources include:

* user utterance
* structured user input
* application request
* agent request
* API request
* enterprise event
* workflow continuation
* system-generated request
* authorized operator input
* another Noema component operating within defined authority

The Source of Intent must remain distinguishable from the interpreted Intent.

A source identifies where a request originated. It does not by itself establish authority to execute it.

⸻

11. Intent Identity

Every persisted Intent must have a stable unique identifier.

intent_id

The identifier represents the identity of the Intent instance throughout its lifecycle.

It must not be replaced merely because the Intent is clarified, enriched, resolved, replanned, or executed.

⸻

12. Intent Version

An Intent must support immutable semantic versioning.

Conceptually:

intent_id
version

A material semantic change creates a new Intent version.

For example:

Intent v1:
"Show my transactions."
        ↓ clarification
Intent v2:
"Show my transactions from August."

The previous version remains historically recoverable.

An Intent version that has entered a consequential downstream decision must not be silently mutated.

⸻

13. Intent Type

An Intent should have a canonical type.

Examples:

ACCOUNT_BALANCE_INQUIRY
STATEMENT_RETRIEVAL
TRANSACTION_SEARCH
SPENDING_SUMMARY
COMPLAINT_LOGGING

Intent types provide a stable semantic vocabulary independent of natural-language phrasing.

The canonical type must not be invented dynamically by a model and treated as authoritative without validation against the Intent taxonomy.

⸻

14. Intent Schema

An Intent must be structurally representable and schema-validatable.

Conceptually:

Intent
├── identity
├── version
├── type
├── source
├── original_input
├── actor
├── subject
├── target
├── parameters
├── constraints
├── scope
├── requested_outcome
├── resolution_state
├── ambiguity
├── provenance
├── context_references
├── status
└── timestamps

The exact implementation may evolve, but the semantic structure must remain explicit.

A structurally invalid Intent must not cross the hard admission boundary into Trust or Execution.

⸻

15. Hard Schema Validation

Before an Intent becomes eligible for Trust evaluation or executable planning, it must pass hard schema validation.

Validation must establish that the Intent:

* conforms to the supported Intent Contract version
* contains required structural fields
* uses recognized semantic types
* represents parameters according to schema
* represents scope correctly
* represents ambiguity explicitly
* preserves provenance
* does not contain structurally invalid values

The model may propose an Intent representation.

It cannot bypass schema validation.

Model / Source
      ↓
Candidate Intent
      ↓
Hard Schema Validation
      ↓
Admitted Intent

⸻

16. Intent Actor

Where relevant, the Intent should identify the Actor whose goal is being represented.

Actor resolution may involve:

* authenticated principal
* customer
* delegated principal
* organization
* service identity
* authorized system

Actor identification is distinct from Intent interpretation.

A semantically clear Intent may remain unresolved because the Actor is unknown or ambiguous.

⸻

17. Intent Subject

The Intent Contract should identify the subject of the request where applicable.

Examples:

* customer
* account
* statement
* transaction
* complaint
* card
* payment

Subject identification must not be inferred beyond available evidence when doing so could change the requested meaning.

⸻

18. Intent Target

The Intent Contract may identify the target Resource or domain object involved in the request.

For example:

Intent:
Retrieve transactions
Target:
Account

The target may initially be unresolved.

An unresolved target is not permission to guess.

For consequential execution, the target must be resolved to the degree required by the Action Contract and applicable Trust rules.

⸻

19. Resolved Target Binding

A target reference and a resolved execution target are not necessarily equivalent.

For example:

"my account"

may initially represent a semantic target category while multiple enterprise accounts exist.

Before consequential execution, Noema must establish the specific Resource required by the Action.

Conceptually:

Actor
   ↓
Intent
   ↓
Target Reference
   ↓
Resolution
   ↓
Specific Resource

Material target ambiguity must remain explicit until resolved.

⸻

20. Intent Parameters

Intent parameters represent values required to express the Source of Intent’s goal.

For example:

{
  "date_range": {
    "from": "2026-08-01",
    "to": "2026-08-31"
  }
}

Parameters should distinguish:

* explicitly provided values
* context-derived values
* resolved values
* unresolved values
* conflicting values
* inferred values

The distinction must remain recoverable.

⸻

21. Explicit Versus Inferred Parameters

Noema must distinguish between what the Source of Intent explicitly stated and what the system inferred.

For example:

Source:
"Show my transactions from last month."
Explicit:
transaction retrieval
Resolved:
date range = previous calendar month

The resolved value may be deterministic given temporal Context, but it must not be represented as though it was explicitly provided.

Inference must remain attributable.

⸻

22. Missing Parameters

An Intent may be incomplete.

For example:

"Show my transactions."

may not identify:

* which account
* which date range
* which transaction scope

Missing information does not automatically invalidate the Intent.

It may instead create a resolution requirement.

⸻

23. Ambiguity

Ambiguity exists when multiple materially different interpretations remain possible.

Example:

"Show my account."

If the Source of Intent has multiple accounts and the target cannot be deterministically resolved, the Intent remains ambiguous.

Noema must not select one merely because it appears statistically likely.

⸻

24. Ambiguity Is State

Ambiguity is not merely a model confidence score.

It is an explicit condition of Intent resolution.

Conceptually:

Intent
  ↓
Ambiguity Evaluation
  ↓
Resolved
OR
Clarification Required

If ambiguity affects consequential behavior, it must become deterministic workflow state.

⸻

25. Model Confidence

The model may provide a confidence signal about its interpretation.

That signal may be useful metadata about a probabilistic interpretation.

It is not authorization, validation, or proof of semantic correctness.

Model Interpretation
        ↓
Candidate Intent
        ↓
Validation / Resolution
        ↓
Trust / Execution Decision

A high confidence score does not override:

* unresolved identity
* unresolved target
* enterprise Policy
* authority
* Context requirements
* Contract constraints
* conflicting evidence

⸻

26. Intent Resolution

Intent Resolution transforms an interpreted or received Intent into a sufficiently specified semantic representation.

Resolution may use:

* Context
* identity
* canonical enterprise data
* Evidence
* user clarification
* organizational rules
* temporal Context
* enterprise relationships
* prior Intent versions

Resolution must remain traceable.

Resolution is not execution authorization.

⸻

27. Resolution Does Not Mean Execution

Successfully resolving an Intent does not authorize an Action.

The lifecycle is:

Intent
  ↓
Resolution
  ↓
Context
  ↓
State Reconciliation
  ↓
Trust
  ↓
Action
  ↓
Execution

Each boundary has its own Contract.

⸻

28. Intent Constraints

An Intent may contain constraints that define boundaries around the requested goal.

Examples:

* date range
* Resource scope
* amount range
* channel
* organization
* urgency
* requested format
* deadline
* temporal scope

Constraints must remain semantically distinct from implementation details.

A constraint must not be silently relaxed merely because an Action or Capability cannot satisfy it.

⸻

29. Requested Outcome

The Intent Contract should capture the outcome the Source of Intent is seeking.

For example:

Requested Outcome:
"Understand my spending for August."

This may later map to one or more executable Actions.

The requested outcome must not be replaced by the implementation plan.

⸻

30. Intent and Outcome

Requested Outcome and execution Outcome are distinct.

The Intent represents what the Source of Intent wants.

The execution Outcome represents what Noema establishes happened.

Therefore:

Requested Outcome
        ≠
Execution Outcome

An Action may succeed while the requested semantic goal remains incomplete.

⸻

31. One Intent May Produce Multiple Actions

A single Intent may require multiple Actions.

For example:

Intent:
"Give me a summary of my August spending."
Actions:
1. Retrieve transactions
2. Aggregate transactions
3. Produce spending summary

The Intent remains the semantic parent.

The Actions remain executable units.

The mapping must preserve lineage and must not expand the requested scope without explicit semantics.

⸻

32. Multiple Intents May Exist in One Input

A single input may express multiple distinct goals.

For example:

"Show my balance and tell me my biggest expense last month."

may produce:

Intent A:
ACCOUNT_BALANCE_INQUIRY
Intent B:
SPENDING_SUMMARY

Noema must preserve the distinction between separate Intents when their resolution, Trust, or execution requirements differ.

⸻

33. Intent Composition

Some Intents may be composed of related sub-Intents.

Conceptually:

Parent Intent
├── Sub-intent A
├── Sub-intent B
└── Sub-intent C

Composition must preserve identity and lineage.

A compound Intent must not obscure individual semantic goals that require separate Trust or execution treatment.

⸻

34. Intent Status

An Intent should have an explicit lifecycle status.

Conceptual states include:

RECEIVED
VALIDATING
INTERPRETING
RESOLVING
CLARIFICATION_REQUIRED
RESOLVED
TRUST_PENDING
AUTHORIZED
PLANNED
EXECUTING
VERIFYING
COMPLETED
FAILED
REJECTED
ESCALATED
CANCELLED

The exact state machine may evolve.

The principle does not:

Intent state must be explicit rather than inferred from incidental events.

Intent status must not be confused with Execution State or enterprise Business State.

⸻

35. Clarification

Clarification is a deterministic state transition used when required Intent information cannot be safely resolved.

Intent
  ↓
Ambiguous
  ↓
CLARIFICATION_REQUIRED
  ↓
Clarification
  ↓
New Intent Version
  ↓
Resolution

Clarification must preserve:

* the original Intent version
* the reason clarification was required
* the clarification source
* the resulting Intent version

Clarification must not silently overwrite history.

⸻

36. Intent Immutability

Once an Intent version has been admitted for consequential downstream processing, its semantic meaning must be immutable.

Operational metadata may change, but the admitted semantic representation must not be silently rewritten.

A material change creates a new version linked through:

supersedes

or an equivalent explicit version relationship.

This ensures that a later execution cannot retroactively change the Intent that authorized its lineage.

⸻

37. Intent Versioning

Material semantic changes should produce a new Intent version.

Versioning protects:

* auditability
* reproducibility
* debugging
* Trust evaluation
* execution lineage
* recovery
* causal reconstruction

An executed Action must be traceable to the exact Intent representation from which it was derived.

⸻

38. Intent Provenance

Every Intent should retain provenance describing how it was produced.

Provenance may include:

* Source of Intent
* original input
* interpreter or model
* model version where applicable
* timestamp
* conversation or request identifier
* resolution events
* Context references
* Evidence references
* clarifications
* Intent version

Provenance must allow Noema to reconstruct the semantic journey of the Intent.

⸻

39. Original Source Representation

The original Source representation should be preserved where appropriate.

For example:

Input:
"How much did I spend last month?"
Intent:
SPENDING_SUMMARY
period = previous_calendar_month

The normalized Intent should not erase the original expression or source representation.

For non-language Sources, the original structured request or source event should remain attributable in the same manner.

⸻

40. Intent Normalization

Different source representations may resolve to the same canonical Intent.

For example:

"How much do I have?"
"What's my balance?"
"Check my balance."

may all resolve to:

ACCOUNT_BALANCE_INQUIRY

Normalization creates semantic consistency without requiring identical source representations.

⸻

41. Intent Equivalence

Two Intents are equivalent only when their semantic meaning and relevant constraints are equivalent.

Lexical similarity is insufficient.

For example:

"Show my transactions."

and:

"Show my transactions from January."

are not equivalent if the first leaves the period unspecified.

Equivalence must be evaluated semantically, not by textual similarity.

⸻

42. Intent Scope

Every Intent must operate within a defined scope where relevant.

Scope may include:

* tenant
* organization
* Actor
* customer
* account
* Resource
* environment
* channel
* time period

Scope prevents an otherwise valid Intent from being applied to the wrong authority boundary.

⸻

43. Intent and Identity

An Intent may depend on resolving the identity of the Actor and/or target Resource.

Identity resolution is separate from Intent interpretation.

For example:

"Show my balance."

may be semantically clear while the requesting customer’s identity remains unresolved.

Semantic clarity does not compensate for identity ambiguity.

⸻

44. Intent and Context

Context enriches Intent.

Conceptually:

Intent
+
Context
=
Resolved Intent

But Context must not silently alter the Source of Intent’s requested objective.

Context can fill a missing value only when the applicable resolution rules permit doing so.

Where Context contains uncertain or conflicting information, its status must remain explicit.

⸻

45. Intent and Evidence

Evidence may support the resolution of an Intent.

Examples:

* customer profile
* account metadata
* previous conversation
* enterprise records
* explicit clarification
* validated event

Evidence should be attributable and evaluated according to its authority, freshness, scope, and validity.

Evidence does not automatically become part of the Intent itself.

⸻

46. Intent and Fact Status

Facts used to resolve an Intent may have explicit Fact Status.

Possible statuses include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

Intent
Evidence
Context
Enterprise State
Execution State
Outcome

For example:

Evidence:
account metadata retrieved
Fact:
account belongs to Actor X
Fact Status:
VERIFIED

if the evidence is authoritative and current enough for that claim.

A model confidence score must not be treated as Fact Status.

⸻

47. Intent and Canonical Data

Canonical enterprise data may resolve Intent parameters.

For example:

Intent:
"Show my account balance."
Canonical data:
customer → account relationship

Noema may use that relationship to resolve the target account.

The balance itself remains enterprise Business State.

Noema must not create shadow business state merely to simplify Intent resolution.

⸻

48. Intent and State Reconciliation

Where Intent resolution depends on distributed, stale, conflicting, or uncertain enterprise information, Noema may require State Reconciliation.

Conceptually:

Intent
   ↓
Required Fact
   ↓
Observations
   ↓
State Reconciliation
   ↓
Resolved Context / Fact Status
   ↓
Intent Resolution

Reconciliation establishes the state required to safely resolve or execute the Intent.

It does not make Noema the System of Record.

⸻

49. Intent and Permissions

An Intent may request something the Actor is not permitted to access.

Therefore:

Valid Intent
      ≠
Permitted Intent

Permission and authorization are evaluated after Intent understanding and within the applicable Trust and enterprise authority boundaries.

Intent validity must never be used as a substitute for authorization.

⸻

50. Intent and Trust Boundary

The Intent Contract provides input to the Trust Engine.

Trust evaluates whether the resolved Intent may proceed.

Conceptually:

Intent Contract
      ↓
Context / State Reconciliation
      ↓
Trust Evaluation
      ↓
EXECUTE / CLARIFY / ESCALATE / REJECT

The Intent Contract itself must not encode the final Trust decision.

Trust must operate on a sufficiently resolved Actor, Action, target, scope, Context, Policy, and relevant enterprise conditions.

⸻

51. Intent and Action Contract

The Action Contract defines the executable operation selected to fulfill an Intent.

Conceptually:

Intent
   ↓
Action Selection
   ↓
Action Contract

The mapping must be explicit and auditable.

Noema must be able to establish why an Action was selected for an Intent.

A model may propose an Action, but it must not create an unregistered Action or Capability.

⸻

52. Intent and Execution Contract

The Execution Contract governs the execution of an Action produced from an Intent.

The relationship is:

Intent
  ↓
Action
  ↓
Execution

Execution must retain lineage back to the originating Intent and exact Intent version.

⸻

53. Intent and Event Contract

Events may communicate lifecycle facts relevant to an Intent.

Examples:

IntentReceived
IntentResolved
IntentClarificationRequested
IntentClarified
IntentRejected
IntentEscalated
IntentCompleted

Events describe occurrences.

They do not independently authorize consequential Actions.

An Event may provide Evidence for Intent state, but Event receipt does not automatically establish the underlying enterprise Business State.

⸻

54. Intent Lineage

Intent lineage connects the semantic journey:

Source of Intent
    ↓
Input
    ↓
Intent
    ↓
Intent Version
    ↓
Resolution
    ↓
Action
    ↓
Execution
    ↓
Outcome

Every consequential Execution should be traceable to its originating Intent and exact semantic version.

⸻

55. Intent Outcome

The outcome of an Intent represents whether the requested semantic goal was fulfilled.

An Action succeeding does not necessarily mean the Intent succeeded.

For example:

Action:
Retrieve transactions
Transport:
SUCCESS
Requested Intent:
Spending summary
Intent Outcome:
INSUFFICIENT_DATA

Intent completion must therefore be evaluated at the semantic goal level.

⸻

56. Partial Fulfillment

An Intent may be partially fulfilled.

For example:

Intent:
"Show my balance and summarize my recent spending."
Balance:
SUCCESS
Spending summary:
FAILED

Noema must represent the partial result rather than collapsing the entire Intent into an undifferentiated success or failure.

⸻

57. Unknown Intent State

Intent resolution may sometimes remain uncertain because required information cannot be established.

Noema must preserve UNKNOWN where appropriate rather than manufacturing certainty.

Examples:

UNKNOWN_ACTOR
UNKNOWN_TARGET
UNKNOWN_SCOPE
UNKNOWN_PARAMETER
UNKNOWN_FACT

Unknown is a valid system state, not an implementation error.

⸻

58. Intent Failure

Intent failure must distinguish between different causes.

Examples:

INVALID_INPUT
AMBIGUOUS_INTENT
UNRESOLVED_IDENTITY
MISSING_CONTEXT
INSUFFICIENT_AUTHORIZATION
TRUST_REJECTION
ACTION_UNAVAILABLE
EXECUTION_FAILURE
BUSINESS_OUTCOME_FAILURE

Failure classification should preserve the semantic boundary at which failure occurred.

A failed Action does not necessarily mean the Intent itself was invalid.

⸻

59. Intent Cancellation

An Intent may be cancelled before completion.

Cancellation should preserve:

* Intent identity
* Intent version
* current state
* cancellation source
* cancellation reason
* timestamp
* related Actions and Executions
* resulting Outcome

Cancellation must not erase historical Intent state.

A cancellation request must not be confused with successful cancellation of downstream enterprise execution.

⸻

60. Escalation and Intervention

An Intent may require escalation or intervention.

Examples:

* ambiguous identity
* unresolved target
* policy exception
* insufficient Evidence
* high-risk request
* enterprise-specific escalation
* unresolved enterprise state

Escalation must preserve the original Intent and its resolution history.

Intervention is an explicit system state and event, not a silent model correction.

⸻

61. Determinism After Interpretation

Interpretation of source input may be probabilistic.

The lifecycle after admission must become increasingly deterministic.

Source Input
      ↓
Probabilistic Interpretation
      ↓
Hard Schema Validation
      ↓
Deterministic Resolution
      ↓
State Reconciliation where required
      ↓
Deterministic Trust
      ↓
Bounded Action Selection
      ↓
Deterministic Execution

The Intent Contract is therefore a critical transition boundary between probabilistic interpretation and deterministic system behavior.

⸻

62. No Silent Guessing

Noema must not silently choose between materially different Intent interpretations.

For example:

"Show my account."

If two accounts are materially plausible and the distinction affects the requested behavior, Noema must clarify.

It must not execute against the account with the highest model probability merely because that probability is high.

⸻

63. Intent History

Intent history should be append-preserving.

When an Intent changes:

Intent v1
    ↓
Resolution event
    ↓
Clarification
    ↓
Intent v2

The system should retain sufficient history to reconstruct the transition.

Current operational state may be represented separately, but historical semantic meaning must remain recoverable.

⸻

64. Intent Persistence

Persisted Intent state should support:

* lifecycle tracking
* lineage
* auditing
* recovery
* replay
* debugging
* analytics
* outcome analysis

Persistence must not turn Noema into the authoritative store for enterprise Business State.

Noema persists the Intent and execution journey, not the enterprise’s underlying business truth.

⸻

65. Intent Security

Intent data may contain sensitive business or customer information.

Intent persistence and transmission must respect:

* tenant isolation
* authorization
* data minimization
* access control
* retention Policies
* audit requirements
* applicable privacy boundaries

The Intent Contract must not become a mechanism for bypassing enterprise security controls.

⸻

66. Intent Idempotency

Repeated delivery of the same input must not unintentionally create duplicate consequential work.

Intent identity and deduplication semantics should distinguish:

same input
same Intent
same Action
same Execution

These are not automatically equivalent.

An identical user request may represent a new Intent instance.

Intent-level deduplication must not be confused with execution-level idempotency.

⸻

67. Intent Replay

An Intent may be replayed for diagnostic or recovery purposes where Policy permits.

Replay must preserve the distinction between:

historical interpretation

and:

new execution attempt

Replay must never implicitly create duplicate consequential execution.

Historical Intent versions must remain unchanged during replay.

⸻

68. Intent and Recovery

When downstream execution fails or becomes uncertain, the original Intent remains the semantic source of the requested goal.

Recovery should determine whether the Intent:

* can continue
* requires another Action
* requires reconciliation
* requires clarification
* must be escalated
* has failed
* has been fulfilled

Recovery must not rewrite the original Intent merely to make an execution path appear successful.

⸻

69. Intent and Reconciliation

Where execution produces an uncertain result, Noema may reconcile against authoritative enterprise state.

For example:

Intent
  ↓
Action
  ↓
Execution
  ↓
UNKNOWN
  ↓
Enterprise State Reconciliation
  ↓
Outcome Determination

Reconciliation resolves execution uncertainty.

It does not redefine the Source of Intent’s original goal.

⸻

70. Intent and Temporal Semantics

Intent may contain temporal meaning.

Examples:

* today
* yesterday
* last month
* recent
* this week
* from January to March

Temporal expressions must be resolved using explicit temporal Context.

Relative time must not be interpreted inconsistently across execution boundaries.

The resolved temporal interpretation must be attributable to the relevant time, timezone, locale, and Intent version.

⸻

71. Intent and Localization

Intent interpretation may depend on:

* locale
* timezone
* language
* regional conventions
* date formats
* currency representation

These should be represented as Context or resolution inputs rather than silently embedded assumptions.

Localization must not alter canonical Intent semantics.

⸻

72. Intent and Enterprise Boundaries

Intent may cross organizational or system boundaries.

Noema must preserve the boundary between:

Source of Intent
      ↓
Noema Interpretation and Resolution
      ↓
Enterprise Authority

The Intent Contract cannot grant authority that the enterprise does not provide.

An Intent may request an operation across multiple enterprise systems, but each resulting Action and Capability remains subject to its own authority and execution constraints.

⸻

73. Intent Contract Validation

An Intent must be validated before becoming eligible for downstream processing.

Validation should determine whether:

* Intent type is recognized
* required semantic structure exists
* schema is valid
* scope is structurally valid
* parameters are structurally valid
* ambiguity is represented
* provenance exists
* version is supported
* lifecycle state is valid
* unsupported or prohibited semantics are rejected

Validation does not itself authorize execution.

⸻

74. Intent Contract Versioning

The Intent Contract itself must be versioned.

Changes to the contract schema must distinguish:

* backward-compatible structural changes
* semantic changes
* breaking changes

Historical Intents must remain interpretable according to the Contract version under which they were created.

A Contract version change must not silently alter the historical meaning of an existing Intent.

⸻

75. Intent Contract and Integrations

Integrations must not receive raw natural-language input as their authoritative execution instruction.

Instead:

Intent
  ↓
Action Contract
  ↓
Execution Contract
  ↓
Integration

Integrations operate on explicit executable contracts.

This prevents provider-specific behavior from becoming the semantic definition of the Source of Intent.

⸻

76. Intent Contract and AI Models

AI models may produce candidate Intent interpretations.

The model must not directly mutate enterprise state.

Model output must enter Noema through the Intent admission boundary and subsequent deterministic controls.

Conceptually:

Model
    ↓
Candidate Intent
    ↓
Hard Schema Validation
    ↓
Intent Resolution
    ↓
Trust
    ↓
Action

The model is an interpreter and proposal mechanism, not the execution authority.

A model cannot:

* create authority
* invent a Capability
* bypass schema validation
* bypass Trust
* silently resolve material ambiguity
* modify an admitted Intent version
* directly invoke an enterprise system

⸻

77. Intent Observability

Noema should make the Intent lifecycle observable.

Useful telemetry includes:

intent_id
intent_type
resolution_duration
clarification_count
trust_result
action_count
execution_count
final_outcome
failure_reason
escalation_reason

Observability should describe the Intent journey without exposing unnecessary sensitive data.

Operational telemetry must remain distinct from canonical Intent state.

⸻

78. Intent Auditability

A consequential Intent should be causally auditable.

An audit record should make it possible to establish:

* what the Source of Intent expressed
* what Noema interpreted
* which Intent version was admitted
* what Context was used
* what ambiguity existed
* what was clarified
* which facts were relied upon
* what State Reconciliation occurred
* what Trust decision occurred
* what Action was selected
* what Execution occurred
* what Outcome resulted

The audit trail must distinguish Source-provided information from system-generated interpretations and enterprise-derived facts.

Auditability does not require exposing private model chain-of-thought.

⸻

79. Intent Metrics

Intent-level metrics may include:

* interpretation accuracy
* clarification rate
* resolution latency
* Trust rejection rate
* escalation rate
* Action conversion rate
* execution completion rate
* Intent completion rate
* partial fulfillment rate
* failure rate
* unknown rate

These metrics should measure the complete Intent journey rather than only model performance.

⸻

80. Intent Quality

A high-quality Intent is:

* semantically explicit
* structurally valid
* sufficiently resolved
* attributable
* scoped
* versioned
* traceable
* compatible with downstream Contracts
* free from unresolved consequential ambiguity

Model confidence alone is not a measure of Intent quality.

⸻

81. Intent Completion

An Intent is complete only when its requested semantic outcome has been determined.

Possible terminal outcomes include:

FULFILLED
PARTIALLY_FULFILLED
FAILED
REJECTED
ESCALATED
CANCELLED

An execution SUCCEEDED state is not sufficient by itself to declare Intent completion.

The semantic relationship between the requested outcome and established execution outcomes must be evaluated.

⸻

82. Reference Intent Model

Conceptually:

┌──────────────────────────────────────────────┐
│                    Intent                    │
├──────────────────────────────────────────────┤
│ intent_id                                    │
│ version                                      │
│ contract_version                             │
│ type                                         │
│ source                                       │
│ original_input                               │
│ actor                                        │
│ subject                                      │
│ target                                       │
│ parameters                                   │
│ constraints                                  │
│ requested_outcome                            │
│ scope                                        │
│ ambiguity                                    │
│ resolution_state                             │
│ context_references                           │
│ provenance                                   │
│ status                                       │
│ timestamps                                   │
└──────────────────────────────────────────────┘
                    │
                    ▼
          Context / Evidence
                    │
                    ▼
          State Reconciliation
                    │
                    ▼
             Trust Evaluation
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Clarify   Escalate   Continue
                              │
                              ▼
                           Action
                              │
                              ▼
                          Execution
                              │
                              ▼
                           Outcome

⸻

83. Intent Relationships

The canonical semantic relationships are:

Source of Intent
      │
      ▼
    Intent
      │
      ├── has → Intent Type
      ├── has → Actor
      ├── has → Target
      ├── has → Parameters
      ├── has → Constraints
      ├── has → Requested Outcome
      ├── has → Scope
      ├── has → Provenance
      ├── resolved_by → Context / Evidence
      ├── constrained_by → Policy
      ├── reconciled_against → Enterprise State
      ├── evaluated_by → Trust
      ├── maps_to → Action
      ├── produces → Execution
      └── seeks → Outcome

These relationships must remain semantically distinct.

In particular:

Intent
≠
Action
≠
Execution
≠
Enterprise State
≠
Outcome

⸻

84. Canonical Intent Lifecycle

The canonical lifecycle is:

SOURCE
  ↓
INTERPRET
  ↓
CREATE INTENT
  ↓
HARD SCHEMA VALIDATION
  ↓
RESOLVE
  ↓
CLARIFY IF REQUIRED
  ↓
CONTEXTUALIZE
  ↓
STATE RECONCILE IF REQUIRED
  ↓
TRUST EVALUATE
  ↓
MAP TO ACTION
  ↓
EXECUTE
  ↓
OBSERVE
  ↓
VERIFY
  ↓
COMPLETE

Not every Intent reaches execution.

An Intent may terminate earlier through:

* clarification
* rejection
* escalation
* cancellation
* unsupported intent
* resolution failure

The lifecycle must preserve the exact point and reason at which termination occurred.

⸻

85. Phase 1 Intent Examples

The initial commercial scope may prioritize common support and information-retrieval Intents such as:

ACCOUNT_BALANCE_INQUIRY
STATEMENT_RETRIEVAL
TRANSACTION_SEARCH
SPENDING_SUMMARY
COMPLAINT_LOGGING

These represent read-oriented and support-oriented workflows.

Phase 1 does not require Noema to move money or perform financial state-changing operations.

The Intent Contract itself remains domain-agnostic; these examples represent the initial fintech specialization.

⸻

86. Intent Contract Invariants

Invariant 1

Every persisted Intent has a stable identity.

Invariant 2

Every Intent has an explicit semantic type.

Invariant 3

Every admitted Intent conforms to the applicable Intent Contract schema.

Invariant 4

Intent interpretation must remain distinguishable from the original Source representation.

Invariant 5

Intent is not an Action.

Invariant 6

Intent is not an Execution.

Invariant 7

Intent is not enterprise Business State.

Invariant 8

Intent does not itself authorize execution.

Invariant 9

Material ambiguity must be represented explicitly.

Invariant 10

Noema must not silently guess when unresolved ambiguity materially affects behavior.

Invariant 11

Model confidence must not independently authorize execution.

Invariant 12

Explicit Source-provided values must remain distinguishable from inferred or resolved values.

Invariant 13

Intent resolution must be traceable.

Invariant 14

Material Intent revisions must preserve historical lineage through immutable versions.

Invariant 15

Context may enrich an Intent but must not silently redefine its requested goal.

Invariant 16

Evidence may support Intent resolution but does not automatically become Intent.

Invariant 17

Fact Status must remain distinct from Evidence, Context, Intent, State, and Outcome.

Invariant 18

Identity resolution is distinct from Intent interpretation.

Invariant 19

Target resolution must be sufficiently specific for consequential execution.

Invariant 20

Permissions are distinct from Intent validity.

Invariant 21

Trust decisions are distinct from Intent interpretation.

Invariant 22

Actions must be explicitly derived from resolved Intents.

Invariant 23

Executions must retain lineage to their originating Intent and Intent version.

Invariant 24

Events may describe Intent lifecycle changes but do not independently authorize Actions.

Invariant 25

Intent Outcomes must be evaluated against the requested semantic outcome.

Invariant 26

Successful transport or Action execution does not automatically mean successful Intent completion.

Invariant 27

Partial fulfillment must remain representable.

Invariant 28

Unknown is a valid state when required truth cannot be established.

Invariant 29

Intent failure must preserve the semantic boundary at which failure occurred.

Invariant 30

Intent cancellation must preserve historical state.

Invariant 31

Clarification and intervention must remain attributable.

Invariant 32

Intent persistence must not create a shadow System of Record for enterprise Business State.

Invariant 33

Intent scope must respect tenant, organization, Resource, environment, and other applicable authority boundaries.

Invariant 34

Intent data must respect enterprise security and privacy boundaries.

Invariant 35

Intent versions must remain interpretable according to their applicable Contract version.

Invariant 36

Replay must not implicitly duplicate consequential execution.

Invariant 37

Recovery must not rewrite the original Source of Intent merely to conceal downstream failure.

Invariant 38

Reconciliation may resolve execution or enterprise-state uncertainty but must not redefine the originating Intent.

Invariant 39

The Intent Contract must remain independent of provider-specific integration details.

Invariant 40

Natural-language interpretation may be probabilistic, but consequential state transitions after Intent admission must be deterministic.

Invariant 41

Noema owns the lifecycle and state of the Intent within its execution domain.

Invariant 42

Enterprise systems remain authoritative for enterprise Business State.

Invariant 43

A valid Intent is not necessarily an authorized Intent.

Invariant 44

A model-generated Intent representation must not bypass hard schema validation.

Invariant 45

A model must not create authority, invent Capabilities, or directly invoke enterprise systems through an Intent.

Invariant 46

Material changes to an admitted Intent must create a new semantic version rather than silently mutating the existing version.

Invariant 47

Intent resolution must preserve uncertainty when required facts cannot be established.

Invariant 48

The Intent Contract must not encode or imply a final Trust decision.

Invariant 49

The Intent Contract must preserve the distinction between the requested goal and the implementation selected to fulfill it.

Invariant 50

An Intent is complete only when its requested semantic outcome has been determined.

⸻

87. Final Definition

The Intent Contract is Noema’s canonical representation of what a Source of Intent is trying to accomplish.

It transforms an interpreted or received request into a structured, schema-valid, attributable, scoped, versioned, and traceable semantic object that can be resolved, reconciled, evaluated for Trust, mapped to executable Actions, and followed through execution to Outcome.

The Intent Contract deliberately separates:

what the Source of Intent wants
        from
what Context and enterprise state establish
        from
whether Trust permits proceeding
        from
how Noema executes it
        from
what the enterprise system considers true
        from
what Outcome Noema can establish

Its governing rule is:

Intent defines the desired goal; it does not authorize, execute, or redefine enterprise truth.

Noema may use probabilistic models to interpret source input, but once an interpretation enters the Intent Contract, structural validity, ambiguity, resolution, Context, State Reconciliation, Trust, Action selection, execution, and Outcome must be governed through explicit deterministic boundaries.

The Intent Contract is therefore the canonical semantic anchor connecting a Source of Intent to trusted enterprise execution without allowing interpretation to become implicit authority.