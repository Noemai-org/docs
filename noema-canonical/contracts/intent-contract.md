Intent Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/intent-contract.md

⸻

1. Definition

An Intent Contract is the canonical contract that defines the structure, meaning, constraints, and lifecycle of an intent recognized and managed by Noema.

It establishes what a user is trying to accomplish without prematurely defining how that goal will be executed.

An Intent Contract is the boundary between human intent and the deterministic systems that resolve, contextualize, authorize, plan, and execute that intent.

⸻

2. Purpose

The Intent Contract exists to make intent:

* structured
* explicit
* inspectable
* versionable
* resolvable
* traceable
* independent of a particular integration
* independent of a particular execution mechanism

Its purpose is to prevent natural-language interpretation from becoming an implicit and untraceable execution decision.

⸻

3. Core Question

The Intent Contract answers:

What is the user trying to accomplish?

It does not by itself answer:

* which enterprise system should be called
* whether the action is permitted
* whether the request is sufficiently trusted
* which API operation should execute
* whether execution succeeded
* what the enterprise business state currently is

Those concerns belong to other Noema contracts and domains.

⸻

4. Intent Is Not an Action

An Intent expresses a desired outcome.

An Action expresses an executable operation.

For example:

Intent:
"Show me my recent transactions."
Action:
RetrieveTransactions(account_id, date_range)

The Intent Contract describes the first.

The Action Contract describes the second.

The transformation between them must be explicit.

⸻

5. Intent Is Not Execution

Intent describes what should happen from the user’s perspective.

Execution describes what Noema actually attempted or performed.

Therefore:

Intent ≠ Execution

An intent may exist without execution.

An execution may fail without invalidating the original intent.

An intent may require clarification before any execution is created.

⸻

6. Intent Is Not Business State

Intent is not enterprise truth.

For example:

Intent:
"How much money do I have?"
Business State:
Current account balance

The Intent Contract represents the request for the information.

The enterprise system remains authoritative for the balance itself.

⸻

7. Intent Is Not Context

Intent describes the requested goal.

Context provides information necessary to understand, evaluate, or execute that goal.

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
session

Context may resolve an incomplete intent, but it must not silently redefine it.

⸻

8. Intent Is Not Trust

Intent describes what the user wants.

Trust determines whether Noema may safely proceed with that intent under applicable policy and evidence.

Therefore:

Intent → Trust Evaluation

not:

Intent = Trust

A valid intent may still be rejected, escalated, or clarified.

⸻

9. Intent Is Not Natural Language

Natural language is an input representation.

Intent is the structured semantic representation derived from that input.

Human Language
      ↓
Interpretation
      ↓
Intent

The original user expression should remain attributable to the resulting intent.

⸻

10. Intent Source

Every Intent should have a source.

Possible sources include:

* user utterance
* structured user input
* application event
* API request
* workflow continuation
* system-generated request
* human operator input

The source must be distinguishable from the interpreted intent.

⸻

11. Intent Identity

Every persisted Intent must have a stable unique identifier.

intent_id

The identifier represents the identity of the intent instance throughout its lifecycle.

It must not be replaced merely because the intent is clarified, enriched, replanned, or executed.

⸻

12. Intent Type

An Intent should have a canonical type.

Examples:

ACCOUNT_BALANCE_INQUIRY
STATEMENT_RETRIEVAL
TRANSACTION_SEARCH
SPENDING_SUMMARY
COMPLAINT_LOGGING

Intent types provide a stable semantic vocabulary independent of natural-language phrasing.

⸻

13. Intent Schema

An Intent should be structurally representable.

Conceptually:

Intent
├── identity
├── type
├── source
├── subject
├── target
├── parameters
├── constraints
├── requested_outcome
├── confidence
├── ambiguity
├── context_reference
├── status
├── timestamps
└── provenance

The exact implementation may evolve, but the semantic structure must remain explicit.

⸻

14. Intent Subject

The Intent Contract should identify the subject of the request where applicable.

Examples:

customer
account
statement
transaction
complaint

Subject identification must not be inferred beyond available evidence when doing so could change the requested meaning.

⸻

15. Intent Target

The Intent Contract may identify the target resource or domain object involved in the request.

For example:

Intent:
Retrieve transactions
Target:
Account

The target may initially be unresolved.

An unresolved target is not permission to guess.

⸻

16. Intent Parameters

Intent parameters represent values required to express the user’s goal.

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

⸻

17. Explicit Versus Inferred Parameters

Noema must distinguish between what the user explicitly stated and what the system inferred.

For example:

User:
"Show my transactions from last month."
Explicit:
transaction retrieval
Inferred:
date range = previous calendar month

Inference must remain attributable and must not be presented as explicit user input.

⸻

18. Missing Parameters

An Intent may be incomplete.

For example:

"Show my transactions."

may not identify:

* which account
* which date range
* which transaction scope

Missing information does not automatically invalidate the intent.

It may instead create a resolution requirement.

⸻

19. Ambiguity

Ambiguity exists when multiple materially different interpretations remain possible.

Example:

"Show my account."

If the user has multiple accounts and the target cannot be deterministically resolved, the intent remains ambiguous.

Noema must not select one merely because it appears statistically likely.

⸻

20. Ambiguity Is State

Ambiguity is not merely a model confidence score.

It is an explicit condition of the Intent lifecycle.

Conceptually:

Intent
  ↓
Ambiguity Evaluation
  ↓
Resolved OR Clarification Required

If ambiguity affects consequential behavior, it must become deterministic workflow state.

⸻

21. Model Confidence

The model may provide a confidence signal about its interpretation.

That signal is useful evidence.

It is not authorization to execute.

Model confidence
        ↓
Interpretation evidence
        ↓
Deterministic resolution
        ↓
Trust / execution decision

A high confidence score does not override enterprise policy or unresolved identity.

⸻

22. Intent Resolution

Intent Resolution transforms an interpreted intent into a sufficiently specified semantic representation.

Resolution may use:

* conversation history
* enterprise context
* identity
* canonical data
* evidence
* user clarification
* organizational rules
* temporal context

Resolution must remain traceable.

⸻

23. Resolution Does Not Mean Execution

Successfully resolving an Intent does not authorize an Action.

The lifecycle is:

Intent
  ↓
Resolution
  ↓
Context
  ↓
Trust
  ↓
Action
  ↓
Execution

Each boundary has its own contract.

⸻

24. Intent Constraints

An Intent may contain constraints that define boundaries around the requested outcome.

Examples:

date range
resource scope
amount range
channel
organization
urgency
requested format

Constraints must remain semantically distinct from implementation details.

⸻

25. Requested Outcome

The Intent Contract should capture the outcome the user is seeking.

For example:

Requested outcome:
"Understand my spending for August."

This may later map to one or more executable Actions.

The requested outcome should not be replaced by the implementation plan.

⸻

26. One Intent May Produce Multiple Actions

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

⸻

27. Multiple Intents May Exist in One User Message

A single user message may express multiple distinct goals.

For example:

"Show my balance and tell me my biggest expense last month."

may produce:

Intent A:
ACCOUNT_BALANCE_INQUIRY
Intent B:
SPENDING_SUMMARY

Noema must preserve the distinction between separate intents when their resolution or execution requirements differ.

⸻

28. Intent Composition

Some intents may be composed of related sub-intents.

Conceptually:

Parent Intent
├── Sub-intent A
├── Sub-intent B
└── Sub-intent C

Composition must preserve identity and lineage.

A compound intent must not obscure the individual semantic goals that require separate trust or execution treatment.

⸻

29. Intent Status

An Intent should have an explicit lifecycle status.

Conceptual states include:

RECEIVED
INTERPRETING
RESOLVING
CLARIFICATION_REQUIRED
RESOLVED
TRUST_PENDING
AUTHORIZED
PLANNED
EXECUTING
COMPLETED
FAILED
REJECTED
ESCALATED
CANCELLED

The exact state machine may evolve.

The principle does not:

Intent state must be explicit rather than inferred from incidental events.

⸻

30. Clarification

Clarification is a deterministic state transition used when required intent information cannot be safely resolved.

Intent
  ↓
Ambiguous
  ↓
CLARIFICATION_REQUIRED
  ↓
User clarification
  ↓
Intent updated
  ↓
Resolution

Clarification must preserve the original intent and the reason clarification was required.

⸻

31. Intent Mutation

An Intent may be refined during its lifecycle.

However, material changes must be traceable.

For example:

Intent v1:
"Show my transactions."
Intent v2:
"Show my transactions from August."

The system should be able to establish how and why the second representation was derived.

⸻

32. Intent Versioning

Material semantic changes should produce a new intent version or equivalent immutable revision.

Versioning protects:

* auditability
* reproducibility
* debugging
* trust evaluation
* execution lineage

An executed Action must be traceable to the intent representation that produced it.

⸻

33. Intent Provenance

Every Intent should retain provenance describing how it was produced.

Provenance may include:

source
original input
interpreter/model
model version
timestamp
conversation/session
resolution events
context references
human clarifications
intent version

Provenance must allow Noema to reconstruct the semantic journey of the intent.

⸻

34. Original User Expression

The original user expression should be preserved where appropriate.

For example:

Raw input:
"How much did I spend last month?"

may produce:

Intent:
SPENDING_SUMMARY
period = previous_calendar_month

The normalized intent should not erase the original expression.

⸻

35. Intent Normalization

Different natural-language expressions may resolve to the same canonical intent.

For example:

"How much do I have?"
"What's my balance?"
"Check my balance."

may all resolve to:

ACCOUNT_BALANCE_INQUIRY

Normalization creates semantic consistency without requiring identical language.

⸻

36. Intent Equivalence

Two intents are equivalent only when their semantic meaning and relevant constraints are equivalent.

Lexical similarity is insufficient.

For example:

"Show my transactions."

and:

"Show my transactions from January."

are not equivalent if the first leaves the period unspecified.

⸻

37. Intent Scope

Every Intent must operate within a defined scope where relevant.

Scope may include:

* tenant
* organization
* customer
* account
* resource
* environment
* channel
* time period

Scope prevents an otherwise valid intent from being applied to the wrong authority boundary.

⸻

38. Intent and Identity

An Intent may depend on resolving the identity of the requester and/or target resource.

Identity resolution is separate from intent interpretation.

For example:

"Show my balance."

may be semantically clear while the requesting customer’s identity remains unresolved.

Semantic clarity does not compensate for identity ambiguity.

⸻

39. Intent and Context

Context enriches Intent.

Conceptually:

Intent
+
Context
=
Resolved Intent

But context must not silently alter the user’s requested objective.

Context can fill a missing value only when the applicable resolution policy permits doing so.

⸻

40. Intent and Evidence

Evidence may support the resolution of an Intent.

Examples:

customer profile
account metadata
previous conversation
enterprise records
explicit user clarification

Evidence should be attributable and evaluated according to its authority and validity.

Evidence does not automatically become part of the Intent itself.

⸻

41. Intent and Canonical Data

Canonical enterprise data may resolve intent parameters.

For example:

Intent:
"Show my account balance."
Canonical data:
customer → account relationship

Noema may use that data to resolve the target account.

The balance itself remains enterprise business state.

⸻

42. Intent and Permissions

An Intent may request something the user is not permitted to access.

Therefore:

Valid Intent
      ≠
Permitted Intent

Permissions are evaluated after intent understanding and within the applicable trust and enterprise policy boundaries.

⸻

43. Intent and Trust Boundary

The Intent Contract provides input to the Trust Engine.

Trust evaluates whether the resolved intent may proceed.

Conceptually:

Intent Contract
      ↓
Context Contract
      ↓
Trust evaluation
      ↓
EXECUTE / CLARIFY / ESCALATE / REJECT

The Intent Contract itself must not encode the final trust decision.

⸻

44. Intent and Action Contract

The Action Contract defines the executable operation selected to fulfill an Intent.

Conceptually:

Intent
   ↓
Action selection
   ↓
Action Contract

The mapping must be explicit and auditable.

Noema must be able to explain why an Action was selected for an Intent.

⸻

45. Intent and Execution Contract

The Execution Contract governs the execution of an Action produced from an Intent.

The relationship is:

Intent
  ↓
Action
  ↓
Execution

Execution must retain lineage back to the originating Intent.

⸻

46. Intent and Event Contract

Events communicate lifecycle facts about an Intent.

Examples:

IntentReceived
IntentResolved
IntentClarificationRequested
IntentClarified
IntentRejected
IntentEscalated
IntentCompleted

Events describe what occurred.

They do not independently authorize consequential actions.

⸻

47. Intent Lineage

Intent lineage connects the entire execution journey:

User Input
    ↓
Intent
    ↓
Resolved Intent
    ↓
Action
    ↓
Execution
    ↓
Outcome

Every consequential execution should be traceable to its originating intent.

⸻

48. Intent Outcome

The outcome of an Intent represents whether the user’s requested goal was fulfilled.

An Action succeeding does not necessarily mean the Intent succeeded.

For example:

Action:
Retrieve transactions
Transport:
SUCCESS
Intent:
Spending summary requested
Outcome:
INSUFFICIENT_DATA

Intent outcome must be evaluated at the semantic goal level.

⸻

49. Partial Fulfillment

An Intent may be partially fulfilled.

For example:

Intent:
"Show my balance and summarize my recent spending."
Balance:
SUCCESS
Spending summary:
FAILED

Noema must represent the partial outcome rather than collapsing the entire intent into an undifferentiated success or failure.

⸻

50. Unknown Intent State

Intent resolution may sometimes remain uncertain because required information cannot be established.

Noema must preserve UNKNOWN where appropriate rather than manufacturing certainty.

For example:

UNKNOWN TARGET
UNKNOWN SCOPE
UNKNOWN IDENTITY
UNKNOWN PARAMETER

Unknown is a valid system state, not an implementation error.

⸻

51. Intent Failure

Intent failure must distinguish between different causes.

Examples:

INVALID_INPUT
AMBIGUOUS_INTENT
UNRESOLVED_IDENTITY
MISSING_CONTEXT
INSUFFICIENT_PERMISSION
TRUST_REJECTION
ACTION_UNAVAILABLE
EXECUTION_FAILURE
BUSINESS_OUTCOME_FAILURE

Failure classification should preserve the semantic boundary at which failure occurred.

⸻

52. Intent Cancellation

An Intent may be cancelled before completion.

Cancellation should preserve:

* intent identity
* current state
* cancellation source
* cancellation reason
* timestamp
* related actions/executions
* resulting outcome

Cancellation must not erase historical intent state.

⸻

53. Human Intervention

An Intent may require human intervention.

Examples:

ambiguous identity
policy exception
insufficient evidence
high-risk request
enterprise-specific escalation

Escalation must preserve the original intent and its resolution history.

Human intervention is not a silent model correction.

⸻

54. Determinism After Interpretation

The interpretation of natural language may be probabilistic.

The lifecycle after interpretation must become increasingly deterministic.

Natural Language
      ↓
Probabilistic Interpretation
      ↓
Deterministic Resolution
      ↓
Deterministic Trust
      ↓
Deterministic Action Selection
      ↓
Deterministic Execution

The Intent Contract is therefore a critical transition boundary between probabilistic interpretation and deterministic system behavior.

⸻

55. No Silent Guessing

Noema must not silently choose between materially different intent interpretations.

For example:

"Show my account."

If two accounts are equally plausible and the distinction matters, Noema must clarify.

It must not execute against the account with the highest model probability merely because that probability is high.

⸻

56. Intent Immutability and History

Intent history should be append-preserving.

When an intent changes:

Intent v1
    ↓
Resolution event
    ↓
Clarification
    ↓
Intent v2

The system should retain sufficient history to reconstruct the transition.

Current state may be mutable operationally, but historical meaning must remain recoverable.

⸻

57. Intent Persistence

Persisted Intent state should support:

* lifecycle tracking
* lineage
* auditing
* recovery
* replay
* debugging
* analytics
* outcome analysis

Persistence must not turn Noema into the authoritative store for enterprise business state.

Noema persists the intent and execution journey, not the enterprise’s underlying business truth.

⸻

58. Intent Security

Intent data may contain sensitive business or customer information.

Intent persistence and transmission must respect:

* tenant isolation
* authorization
* data minimization
* access control
* retention policies
* audit requirements
* applicable privacy boundaries

The Intent Contract must not become a mechanism for bypassing enterprise security controls.

⸻

59. Intent Idempotency

Repeated delivery of the same intent input must not unintentionally create duplicate consequential work.

Intent identity and deduplication semantics should distinguish:

same input
same intent
same action
same execution

These are not automatically equivalent.

An identical user request may represent a new intent instance.

⸻

60. Intent Replay

An Intent may be replayed for diagnostic or recovery purposes where policy permits.

Replay must preserve the distinction between:

historical interpretation
new execution attempt

Replay must never implicitly create duplicate consequential execution.

⸻

61. Intent and Recovery

When downstream execution fails or becomes uncertain, the original Intent remains the semantic source of the requested goal.

Recovery should determine whether the intent:

* can continue
* requires another action
* requires reconciliation
* requires clarification
* must be escalated
* has failed

Recovery must not rewrite the original user intent merely to make an execution path appear successful.

⸻

62. Intent and Reconciliation

Where execution produces an uncertain outcome, Noema may reconcile against authoritative enterprise state.

For example:

Intent
  ↓
Action
  ↓
Execution
  ↓
UNKNOWN
  ↓
Enterprise state reconciliation
  ↓
Outcome determination

Reconciliation resolves execution uncertainty.

It does not redefine the user’s original intent.

⸻

63. Intent and Temporal Semantics

Intent may contain temporal meaning.

Examples:

today
yesterday
last month
recent
this week
from January to March

Temporal expressions must be resolved using explicit temporal context.

Relative time must not be interpreted inconsistently across execution boundaries.

⸻

64. Intent and Localization

Intent interpretation may depend on:

* locale
* timezone
* language
* regional conventions
* date formats
* currency representation

These should be represented as context or resolution inputs rather than silently embedded assumptions.

⸻

65. Intent and Enterprise Boundaries

Intent may cross organizational or system boundaries.

Noema must preserve the boundary between:

User intent
      ↓
Noema interpretation
      ↓
Enterprise authority

The Intent Contract cannot grant authority that the enterprise system does not provide.

⸻

66. Intent Contract Validation

An Intent should be validated before it becomes eligible for downstream processing.

Validation should determine whether:

* intent type is recognized
* required semantic structure exists
* scope is valid
* parameters are structurally valid
* ambiguity is represented
* provenance exists
* lifecycle state is valid
* version is supported

Validation does not itself authorize execution.

⸻

67. Intent Contract Versioning

The Intent Contract itself must be versioned.

Changes to the contract schema must distinguish:

backward-compatible changes
breaking semantic changes

Historical intents must remain interpretable according to the contract version under which they were created.

⸻

68. Intent Contract and Integrations

Integrations must not receive raw natural-language intent as their authoritative execution instruction.

Instead:

Intent
  ↓
Action Contract
  ↓
Integration

Integrations operate on explicit executable contracts.

This prevents provider-specific behavior from becoming the semantic definition of user intent.

⸻

69. Intent Contract and AI Models

AI models may produce candidate intent interpretations.

The model should not directly mutate enterprise state.

A model output should enter Noema through the Intent Contract and subsequent deterministic controls.

LLM Output
    ↓
Intent Validation
    ↓
Intent Resolution
    ↓
Trust
    ↓
Action

The model is an interpreter, not the execution authority.

⸻

70. Intent Observability

Noema should make the intent lifecycle observable.

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

Observability should describe the intent journey without exposing unnecessary sensitive data.

⸻

71. Intent Auditability

A consequential Intent should be auditable.

An audit record should make it possible to establish:

what the user asked
what Noema interpreted
what context was used
what ambiguity existed
what was clarified
what trust decision occurred
what Action was selected
what Execution occurred
what outcome resulted

The audit trail must distinguish user-provided facts from system-generated interpretations.

⸻

72. Intent Metrics

Intent-level metrics may include:

* interpretation accuracy
* clarification rate
* resolution latency
* trust rejection rate
* escalation rate
* action conversion rate
* execution completion rate
* intent completion rate
* partial fulfillment rate
* failure rate

These metrics should measure the complete intent journey rather than only model performance.

⸻

73. Intent Quality

A high-quality Intent is:

* semantically explicit
* sufficiently resolved
* attributable
* scoped
* versioned
* traceable
* compatible with downstream contracts
* free from unresolved consequential ambiguity

Model confidence alone is not a measure of intent quality.

⸻

74. Intent Completion

An Intent is complete only when its requested semantic outcome has been determined.

Possible terminal outcomes include:

FULFILLED
PARTIALLY_FULFILLED
FAILED
REJECTED
ESCALATED
CANCELLED

A successful API response is not sufficient to declare Intent completion.

⸻

75. Reference Intent Model

Conceptually:

┌──────────────────────────────────────────┐
│                  Intent                  │
├──────────────────────────────────────────┤
│ intent_id                                │
│ version                                  │
│ type                                     │
│ source                                   │
│ original_input                           │
│ subject                                  │
│ target                                   │
│ parameters                               │
│ constraints                              │
│ requested_outcome                        │
│ scope                                    │
│ ambiguity                                │
│ resolution_state                         │
│ context_reference                        │
│ provenance                               │
│ status                                   │
│ timestamps                               │
└──────────────────────────────────────────┘
                    │
                    ▼
             Context / Evidence
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

76. Canonical Intent Lifecycle

The canonical lifecycle is:

INPUT
  ↓
INTERPRET
  ↓
CREATE INTENT
  ↓
RESOLVE
  ↓
CLARIFY IF REQUIRED
  ↓
CONTEXTUALIZE
  ↓
TRUST EVALUATE
  ↓
MAP TO ACTION
  ↓
EXECUTE
  ↓
OBSERVE
  ↓
VERIFY OUTCOME
  ↓
COMPLETE

Not every intent reaches execution.

An intent may terminate earlier through clarification, rejection, escalation, cancellation, or failure.

⸻

77. Phase 1 Intent Examples

The initial commercial scope should prioritize common support and information-retrieval intents such as:

ACCOUNT_BALANCE_INQUIRY
STATEMENT_RETRIEVAL
TRANSACTION_SEARCH
SPENDING_SUMMARY
COMPLAINT_LOGGING

These represent read-oriented and support-oriented workflows.

Phase 1 does not require Noema to move money or perform financial state-changing operations.

⸻

78. Intent Contract Invariants

Invariant 1

Every persisted Intent has a stable identity.

Invariant 2

Every Intent has an explicit semantic type.

Invariant 3

Intent interpretation must remain distinguishable from the original natural-language input.

Invariant 4

Intent is not an Action.

Invariant 5

Intent is not an Execution.

Invariant 6

Intent is not enterprise business state.

Invariant 7

Intent does not itself authorize execution.

Invariant 8

Material ambiguity must be represented explicitly.

Invariant 9

Noema must not silently guess when unresolved ambiguity materially affects behavior.

Invariant 10

Model confidence must not independently authorize execution.

Invariant 11

Explicit user-provided values must remain distinguishable from inferred values.

Invariant 12

Intent resolution must be traceable.

Invariant 13

Intent revisions must preserve historical lineage.

Invariant 14

Context may enrich an Intent but must not silently redefine its requested goal.

Invariant 15

Evidence may support intent resolution but does not automatically become Intent.

Invariant 16

Identity resolution is distinct from intent interpretation.

Invariant 17

Permissions are distinct from intent validity.

Invariant 18

Trust decisions are distinct from intent interpretation.

Invariant 19

Actions must be explicitly derived from resolved intents.

Invariant 20

Executions must retain lineage to their originating intent.

Invariant 21

Events describe Intent lifecycle changes but do not independently authorize actions.

Invariant 22

Intent outcomes must be evaluated against the requested semantic outcome.

Invariant 23

Successful transport does not automatically mean successful Intent completion.

Invariant 24

Partial fulfillment must remain representable.

Invariant 25

Unknown is a valid state when the required truth cannot be established.

Invariant 26

Intent failure must preserve the boundary at which failure occurred.

Invariant 27

Intent cancellation must preserve historical state.

Invariant 28

Human clarification and intervention must remain attributable.

Invariant 29

Intent persistence must not create a shadow system of record for enterprise business state.

Invariant 30

Intent scope must respect tenant, organization, resource, environment, and other applicable authority boundaries.

Invariant 31

Intent data must respect enterprise security and privacy boundaries.

Invariant 32

Intent versions must remain interpretable over their supported lifecycle.

Invariant 33

Replay must not implicitly duplicate consequential execution.

Invariant 34

Recovery must not rewrite the original user goal merely to conceal downstream failure.

Invariant 35

Reconciliation may resolve execution uncertainty but must not redefine the originating Intent.

Invariant 36

The Intent Contract must remain independent of provider-specific integration details.

Invariant 37

Natural-language interpretation may be probabilistic, but consequential state transitions after interpretation must be deterministic.

Invariant 38

Noema owns the lifecycle and state of the Intent within its execution domain.

Invariant 39

Enterprise systems remain authoritative for enterprise business state.

Invariant 40

An Intent is complete only when its requested outcome has been semantically resolved.

⸻

79. Final Definition

The Intent Contract is Noema’s canonical representation of what a human or authorized system is trying to accomplish.

It transforms an interpreted request into a structured, attributable, scoped, versioned, and traceable semantic object that can be resolved, evaluated for trust, mapped to executable Actions, and followed through execution to outcome.

The Intent Contract deliberately separates:

what the user wants
        from
how Noema executes it
        from
what the enterprise system considers true

Its governing rule is:

Intent defines the desired goal; it does not authorize, execute, or redefine enterprise truth.

Noema may use probabilistic models to interpret language, but once an interpretation enters the Intent Contract, ambiguity, context, trust, action selection, execution, and outcome must be governed through explicit deterministic boundaries.

The Intent Contract is therefore the canonical semantic anchor connecting human intent to trusted execution without allowing interpretation to become implicit authority.