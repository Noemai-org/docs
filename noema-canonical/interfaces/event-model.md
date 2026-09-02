Event Model

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/event-model.md

⸻

1. Definition

The Event Model defines how Noema represents, produces, consumes, and propagates observable changes in Intent, Trust, Execution, and Outcome state across system boundaries.

Events are the mechanism through which Noema communicates that something has happened or a meaningful state transition has been observed.

An Event is therefore different from a command.

Command:
"Do this."
Event:
"This happened."

The distinction is foundational to Noema.

⸻

2. Purpose

The Event Model provides a canonical semantic model for:

* Action lifecycle changes
* Intent state changes
* Trust decisions
* Execution attempts
* Evidence observations
* Outcomes
* Failures
* Human intervention
* Clarification
* Reconciliation
* Policy changes where relevant
* External system events consumed by Noema

It allows Noema and external systems to remain loosely coupled while preserving an auditable execution journey.

⸻

3. Core Principle

An Event records an observation about something that happened; it does not instruct another system to make that thing happen.

Therefore:

Event ≠ Command
Event ≠ Request
Event ≠ Intent
Event ≠ Action
Event ≠ Outcome

An Event may provide evidence for an Outcome, but it is not automatically an Outcome itself.

⸻

4. Event as a First-Class Concept

Conceptually:

Event
 ├── Identity
 ├── Type
 ├── Subject
 ├── Source
 ├── Timestamp
 ├── Data
 ├── Provenance
 └── Correlation

An Event describes an occurrence within a system or at a system boundary.

⸻

5. Event vs State

An Event describes a transition or occurrence.

State describes the current condition.

Example:

Event:
CARD_STATUS_CHANGED
old = LOST
new = REPLACEMENT_PENDING

Current state:

card.status = REPLACEMENT_PENDING

The Event tells us what happened.

The State tells us what is true now, subject to the authority and freshness of the source.

⸻

6. Event vs Outcome

An Event can provide evidence for an Outcome.

For example:

Event:
CARD_CREATED

may support:

Outcome:
replacement card successfully created

But:

Event received

does not automatically mean:

Outcome established

Noema must evaluate whether the Event satisfies the relevant postconditions and evidence requirements.

⸻

7. Event vs Action

An Action represents intended executable work.

An Event represents an occurrence.

Action:
issue_replacement_card
Event:
replacement_card_created

The relationship is:

Action
  ↓
Execution
  ↓
Event(s)
  ↓
Evidence
  ↓
Outcome

⸻

8. Event Identity

Every Event should have a globally unique identifier.

Conceptually:

event_id

Example:

evt_01JXYZ...

Event identity must remain stable across delivery attempts.

⸻

9. Event Type

Every Event has a semantic type.

Examples:

action.submitted
action.accepted
action.started
action.completed
action.failed
execution.started
execution.succeeded
execution.failed
trust.approved
trust.blocked
clarification.requested
clarification.resolved
outcome.established
outcome.rejected

Event types should describe what happened, not what another system should do.

⸻

10. Event Naming

Event names should generally use past-tense or occurrence-oriented semantics.

Good:

card.created
payment.completed
authorization.revoked
action.failed

Bad:

create.card
execute.payment
authorize.action
retry.payment

The latter describe commands.

⸻

11. Event Subject

Every Event should identify the entity or object the Event concerns.

Conceptually:

{
  "subject": {
    "type": "action",
    "id": "act_123"
  }
}

The subject allows consumers to understand:

what does this Event refer to?

⸻

12. Event Source

Every Event should identify where it originated.

Example:

{
  "source": {
    "type": "system",
    "id": "card-service"
  }
}

Source identity is important for provenance and Trust evaluation.

⸻

13. Source vs Subject

These are distinct.

Source:
card-service
Subject:
card_123

The source tells us:

who produced the Event

The subject tells us:

what the Event is about

⸻

14. Event Timestamp

Events should contain the relevant time information.

At minimum:

occurred_at

Where useful, Noema should distinguish:

occurred_at
observed_at
published_at
received_at

These timestamps answer different questions.

⸻

15. Occurred At

occurred_at describes when the underlying event happened according to the source.

Example:

card_created
occurred_at = 10:42:12

⸻

16. Observed At

observed_at describes when Noema or another system observed the event.

Example:

occurred_at = 10:42:12
observed_at = 10:42:15

This distinction matters for distributed systems.

⸻

17. Published At

published_at describes when the Event was emitted onto an event transport.

It does not necessarily equal when the underlying business occurrence happened.

⸻

18. Received At

received_at describes when a consumer received the Event.

These timestamps allow Noema to reason about:

latency
freshness
ordering
staleness
causality

⸻

19. Event Data

Event data contains the semantic payload describing the occurrence.

Example:

{
  "type": "card.created",
  "data": {
    "card_id": "card_123",
    "card_type": "replacement"
  }
}

Event data should contain enough information to understand the occurrence without embedding unrelated system state.

⸻

20. Event Metadata

Metadata may include:

tenant
correlation_id
causation_id
trace_id
schema_version
producer
environment

Metadata supports distributed tracing, provenance, and lifecycle reconstruction.

⸻

21. Correlation ID

Events should support correlation.

Example:

correlation_id = act_123

This allows consumers to reconstruct:

Intent
→ Action
→ Execution
→ Event
→ Outcome

⸻

22. Causation ID

Where possible, an Event should identify the event or operation that caused it.

Example:

Event A
  ↓
Event B

Event B may contain:

causation_id = event_A

This provides causal lineage.

⸻

23. Event Causality

A causal chain may look like:

Intent resolved
      ↓
Action submitted
      ↓
Execution started
      ↓
Card provider called
      ↓
Card created
      ↓
Outcome established

Each occurrence can carry enough metadata to reconstruct the chain.

⸻

24. Event Ordering

Distributed systems cannot generally guarantee global ordering.

Therefore consumers must not assume:

received order == occurrence order

unless the relevant contract explicitly guarantees ordering.

⸻

25. Ordering Scope

Where ordering matters, it should be defined within an explicit scope.

For example:

ordering key = action_id

may guarantee:

Action A event 1
Action A event 2
Action A event 3

without requiring:

Action B event

to be globally ordered relative to Action A.

⸻

26. Event Sequence

An Event stream may include a sequence number.

Example:

sequence = 17

Sequence numbers can help consumers detect:

missing events
duplicates
reordering
gaps

⸻

27. Event Delivery Semantics

Noema should not assume event delivery is exactly once.

A practical model is:

at-least-once delivery
+
idempotent consumers
+
stable event identity

Consumers must therefore tolerate duplicate delivery.

⸻

28. Duplicate Events

The same Event may be delivered multiple times:

evt_123
evt_123
evt_123

These remain one logical Event.

Consumers should deduplicate using the Event identity.

⸻

29. Event Immutability

Once published, an Event should be immutable.

If a correction is required, publish a new Event.

Bad:

modify evt_123

Preferred:

evt_123
  ↓
evt_124 correction

This preserves historical integrity.

⸻

30. Event Corrections

A correction Event may reference the Event it supersedes.

Conceptually:

{
  "type": "resource.state_corrected",
  "causation_id": "evt_123"
}

The original Event remains part of the historical record.

⸻

31. Events and Auditability

The Event Model contributes to Noema’s execution audit trail.

Event
  ↓
Causal history
  ↓
Execution history
  ↓
Evidence
  ↓
Outcome

The event stream should therefore preserve enough provenance to explain how a decision or Outcome came to exist.

⸻

32. Internal vs External Events

Noema may have:

internal events
external events

Internal Events concern Noema’s own lifecycle.

External Events originate from enterprise systems or providers.

Example:

Internal:
action.execution_started
External:
payment.provider.confirmed

Both can participate in execution reasoning.

⸻

33. External Events

External systems may publish Events into Noema.

Example:

payment.completed
account.suspended
card.blocked
employee.terminated

Noema may use these Events as contextual observations or evidence.

⸻

34. External Events Are Not Automatically Trusted

An Event from an external system is still subject to validation.

Noema should evaluate:

source identity
signature
schema
timestamp
tenant
resource
sequence
provenance

before treating it as trusted evidence.

⸻

35. Event Authentication

Where appropriate, Event producers should authenticate their messages.

Possible mechanisms include:

mTLS
signed events
OAuth
API credentials
private network identity

The exact mechanism is implementation-specific.

The semantic requirement is:

Noema must be able to establish who produced an Event when producer identity matters to Trust.

⸻

36. Event Schema

Events should use explicit schemas.

Conceptually:

event_type
schema_version
payload

Example:

card.created@1

Schema evolution must preserve consumer compatibility.

⸻

37. Event Versioning

Event schemas should be independently versioned.

For example:

card.created@1
card.created@2

This is distinct from:

Action Contract v2
API v2

Each represents a different compatibility boundary.

⸻

38. Backward Compatibility

Event consumers may process Events long after they were produced.

Therefore schema changes should be handled conservatively.

Prefer:

additive changes
optional fields
explicit versions

over silently changing the meaning of existing fields.

⸻

39. Event Envelope

A canonical Event envelope may resemble:

{
  "id": "evt_123",
  "type": "card.created",
  "version": 1,
  "source": {
    "type": "system",
    "id": "card-service"
  },
  "subject": {
    "type": "card",
    "id": "card_456"
  },
  "occurred_at": "2026-08-27T10:00:00Z",
  "observed_at": "2026-08-27T10:00:02Z",
  "correlation_id": "act_789",
  "causation_id": "evt_122",
  "data": {}
}

This is a conceptual model, not the final wire schema.

⸻

40. Event and Context

Events can become Context observations.

External Event
      ↓
Validation
      ↓
Observation
      ↓
Context

For example:

ACCOUNT_SUSPENDED

may update contextual knowledge:

account.status = SUSPENDED

subject to source authority and freshness.

⸻

41. Event and Evidence

An Event can serve as evidence.

Event:
card.created
       ↓
Evidence:
provider reports card creation
       ↓
Postcondition:
replacement card exists
       ↓
Outcome:
Action succeeded

The Trust Engine determines whether the Event is sufficient evidence.

⸻

42. Event and Trust

The Trust Engine may evaluate:

event source
event integrity
event freshness
event sequence
event schema
event subject
event causality

before relying on the Event.

⸻

43. Event and Determinism

Events should provide deterministic observations.

The LLM may interpret an Event’s meaning upstream, but Trust decisions should operate on explicit event semantics.

For example:

event.type = card.created

is deterministic.

A model’s interpretation:

"this probably means the card was created"

is not sufficient for a high-trust execution decision.

⸻

44. Event and Intent

Intent may generate lifecycle Events.

Example:

intent.created
intent.clarification_requested
intent.clarified
intent.resolved
intent.rejected

These Events allow the Intent lifecycle to be observed externally.

⸻

45. Event and Action

Actions may produce lifecycle Events:

action.submitted
action.accepted
action.blocked
action.started
action.retrying
action.completed
action.failed
action.cancelled

These form the observable Action lifecycle.

⸻

46. Event and Execution

Execution attempts may produce:

execution.started
execution.succeeded
execution.failed
execution.timed_out
execution.unknown
execution.reconciled

These Events allow the execution journey to be reconstructed.

⸻

47. Event and Outcome

Outcome Events should be emitted only when the corresponding Outcome has been established.

Example:

outcome.established

should mean:

Noema has established the Outcome according to the relevant contract.

It should not merely mean:

consumer returned success.

⸻

48. Event and Failure

Failures should be represented explicitly.

Example:

execution.failed

may contain:

{
  "failure": {
    "class": "TRANSIENT",
    "code": "PROVIDER_TIMEOUT"
  }
}

This allows policy-driven retry and recovery.

⸻

49. Event and Unknown State

An Event may establish that execution entered an uncertain state.

Example:

execution.unknown

This is important because:

UNKNOWN ≠ FAILED

A timeout does not necessarily prove that an external operation failed.

⸻

50. Event and Reconciliation

Reconciliation may generate Events:

execution.reconciliation_started
execution.reconciled

The resulting evidence can establish:

SUCCESS
FAILED
UNKNOWN

or another canonical state.

⸻

51. Event and Human Intervention

Human intervention can be represented through Events:

intervention.requested
intervention.approved
intervention.rejected
intervention.completed

These Events should identify:

actor
authority
timestamp
Action
reason

where required.

⸻

52. Event and Clarification

Clarification can likewise be represented:

clarification.requested
clarification.received
clarification.resolved

The clarification Event should be associated with the Intent or Action requiring clarification.

⸻

53. Event and Policy

Policy changes may be represented by Events.

Example:

policy.updated
policy.activated
policy.deactivated

However, consumers must understand whether the Event describes:

policy metadata

or:

a policy decision

These are different concepts.

⸻

54. Event vs Policy Decision

Event:
policy.updated
Decision:
Action allowed

A policy update Event does not itself mean an Action is allowed.

The Trust Engine must evaluate the Action against the applicable policy.

⸻

55. Event Consumption

Consumers may subscribe to relevant Event types.

Conceptually:

Noema Event Stream
        │
        ├── Consumer A
        ├── Consumer B
        └── Consumer C

Each consumer is responsible for processing Events according to its own integration contract.

⸻

56. Event Subscription

Subscriptions should support filtering by relevant dimensions such as:

tenant
event type
subject type
subject ID
Action
environment

Broad unrestricted subscriptions should not be the default.

⸻

57. Event Delivery

Delivery mechanisms may include:

webhooks
message queues
event streams
pub/sub
SDK callbacks

The canonical Event Model should remain independent of transport.

⸻

58. Event Acknowledgement

Consumers may acknowledge receipt.

An acknowledgement means:

Event received

It does not mean:

Event accepted as true

nor:

business state changed

⸻

59. Event Processing Failure

If a consumer cannot process an Event, the delivery mechanism should support recovery through:

retry
dead-letter handling
replay
manual intervention

The Event itself should remain immutable.

⸻

60. Event Replay

Events should be replayable where the infrastructure and retention policy permit.

Replay allows consumers to reconstruct state after:

deployment
consumer crash
schema migration
bug fix
new consumer creation

Replay must preserve original Event identity.

⸻

61. Replay Is Not Re-Execution

This distinction is critical.

Replay Event

means:

process historical observation again

It does not mean:

execute the original Action again

An Event replay must never accidentally trigger a consequential Action as though the original command had been issued again.

⸻

62. Event Retention

Retention policies should be explicit.

Events may need longer retention when they support:

audit
compliance
reconciliation
execution history
causal reconstruction

Retention should also respect privacy and enterprise policy.

⸻

63. Event Ordering and Trust

If event ordering is security- or execution-critical, Noema must verify ordering using reliable mechanisms.

It should not infer:

latest received Event = latest truth

solely from network arrival order.

⸻

64. Event Freshness

An Event may become stale.

Example:

account.status = ACTIVE

from six hours ago may be insufficient for a high-risk transaction.

Freshness requirements belong to the relevant Action Contract or Policy.

⸻

65. Event Source Failure

If a trusted source stops producing Events:

provider unavailable

Noema must distinguish:

no new information

from:

nothing changed

Silence is not automatically evidence of stability.

⸻

66. Event Loss

If Noema detects an Event sequence gap:

sequence 41
sequence 42
sequence 44

it should not silently assume:

43 did not matter

Depending on the contract, Noema may:

request replay
pause processing
mark context stale
reconcile

⸻

67. Event Duplication

Duplicate Events must not create duplicate logical state transitions.

For example:

card.created
card.created

must not result in:

two cards

Consumers should use Event identity and domain-level idempotency.

⸻

68. Event Transactionality

Producing an Event should be coordinated carefully with the state change it represents.

A system must avoid:

database committed
but Event lost

or:

Event published
but database rolled back

where such inconsistency would violate the Event’s semantic contract.

The implementation may use patterns such as an outbox, but the canonical requirement is consistency between the claimed occurrence and the source state.

⸻

69. Event Atomicity

For critical domain Events:

State transition
+
Event publication

should have well-defined atomicity or recovery semantics.

Noema should never assume transport guarantees provide transactional coupling automatically.

⸻

70. Event and Idempotency

Event consumers should be idempotent.

A consumer should be safe when:

evt_123

is delivered more than once.

This is separate from Action idempotency.

Action idempotency
≠
Event consumption idempotency

⸻

71. Event and Action Idempotency

An Event may report that an idempotent Action completed.

Replaying the Event must not create a second Action.

The Event is an observation, not a new execution request.

⸻

72. Event Security

Events should be protected against:

spoofing
tampering
replay attacks
cross-tenant leakage
unauthorized subscription
payload injection

Security controls are implementation-specific but must preserve the semantic integrity of Events.

⸻

73. Event Payload Minimization

Events should contain only information necessary for their purpose.

Avoid:

entire customer profile
entire account record
entire enterprise database object

when a reference is sufficient.

Prefer:

{
  "customer_id": "cus_123"
}

where consumers can retrieve authorized details when necessary.

⸻

74. Event and Privacy

Event streams can become long-lived historical records.

Therefore event design must consider:

PII
sensitive attributes
retention
redaction
access control
tenant isolation

Immutable event history does not remove privacy obligations.

⸻

75. Event Redaction

Where legally or operationally necessary, the architecture may support controlled redaction.

However, redaction should not silently rewrite the historical meaning of an Event.

Where possible:

original Event
+
redaction metadata

should preserve audit semantics.

⸻

76. Event and Enterprise Action Graph

Events are one of the major inputs into Noema’s Enterprise Action Graph.

Enterprise APIs
Documentation
Policies
Workflows
Events
Human Configuration
        ↓
Enterprise Action Graph

Events provide the graph with evidence about how the enterprise actually behaves.

⸻

77. Event and Learning

Noema may use historical Events to improve:

Intent resolution
ambiguity handling
planning
failure prediction
routing
recovery

But learned patterns must not override deterministic Trust and Policy requirements.

Historical frequency is not authorization.

⸻

78. Event and Model Inference

An LLM may use historical Events to infer likely context.

For example:

Previous recipient:
John Smith

But the Event history should remain evidence.

It should not automatically become:

the current recipient

when ambiguity remains material.

⸻

79. Event and Deterministic State

Events can drive deterministic state machines.

Example:

ACTION_ACCEPTED
      ↓
Action State = ACCEPTED
EXECUTION_STARTED
      ↓
Action State = EXECUTING
EXECUTION_FAILED
      ↓
Action State = FAILED

State transitions should be defined by the relevant state machine, not improvised by consumers.

⸻

80. Event State Transition Validity

Not every Event is valid in every state.

For example:

COMPLETED
   ↓
EXECUTION_STARTED

may be invalid.

Noema should validate Event/state compatibility where it controls the state machine.

⸻

81. Event Reconciliation

If Events conflict with observed authoritative state:

Event:
account ACTIVE
Provider:
account BLOCKED

Noema should enter an appropriate reconciliation or conflict state rather than blindly trusting either value.

⸻

82. Event Authority

Events should carry or imply an authority level based on their source.

For example:

authoritative provider event

may carry more weight than:

client-generated event

But authority is ultimately determined by the relevant integration and policy.

⸻

83. Event Schema Registry

A production Noema implementation may maintain a registry of:

event types
schemas
versions
producers
consumers
compatibility rules

This ensures that Events remain discoverable and governed.

⸻

84. Event Contract

Each externally consumed Event should have an Event Contract defining:

event type
schema
producer
subject
semantics
ordering
delivery
replay
retention
security
versioning

This should become part of Noema’s broader integration contract model.

⸻

85. Event API Boundary

The Event Model may be exposed through:

Event API
Event Stream
Webhook Interface
Message Broker
SDK

These are delivery mechanisms.

The canonical semantic object remains:

Event

⸻

86. Event vs Event API

The Event Model defines:

what an Event means

An Event API defines:

how consumers obtain Events

These should remain separate.

⸻

87. Canonical Event Lifecycle

Occurrence
    ↓
Event Created
    ↓
Event Validated
    ↓
Event Published
    ↓
Event Delivered
    ↓
Event Observed
    ↓
Evidence / Context
    ↓
State Transition / Outcome

Not every Event necessarily passes through every stage.

⸻

88. Canonical Noema Flow

                  INTENT
                    │
                    ▼
             EXECUTABLE INTENT
                    │
                    ▼
                  ACTION
                    │
                    ▼
                EXECUTION
                    │
             ┌──────┴──────┐
             ▼             ▼
        INTERNAL        EXTERNAL
          EVENTS          EVENTS
             │             │
             └──────┬──────┘
                    ▼
                EVIDENCE
                    │
                    ▼
             POSTCONDITIONS
                    │
                    ▼
                 OUTCOME
                    │
                    ▼
               EVENT STREAM

⸻

89. Example: Card Replacement

A complete lifecycle might generate:

intent.resolved
        ↓
action.submitted
        ↓
action.accepted
        ↓
execution.started
        ↓
card.replacement_requested
        ↓
card.created
        ↓
execution.succeeded
        ↓
outcome.established
        ↓
action.completed

The Events form an observable history of the execution journey.

⸻

90. Example: Unknown Execution

action.submitted
      ↓
execution.started
      ↓
provider.timeout
      ↓
execution.unknown
      ↓
reconciliation.started
      ↓
provider.state.observed
      ↓
execution.reconciled
      ↓
outcome.established

This illustrates why the Event Model must support uncertainty and reconciliation rather than only success/failure.

⸻

91. Example: Human Approval

action.submitted
      ↓
trust.evaluated
      ↓
approval.required
      ↓
intervention.requested
      ↓
intervention.approved
      ↓
execution.started
      ↓
execution.completed

The approval Event does not itself execute the Action.

⸻

92. Example: Clarification

intent.created
      ↓
intent.ambiguous
      ↓
clarification.requested
      ↓
clarification.received
      ↓
intent.resolved
      ↓
action.created

The clarification Event changes the Intent lifecycle; it does not directly execute an Action.

⸻

93. Event Model Invariants

Invariant 1

An Event describes an occurrence, not a command.

Invariant 2

Events are immutable after publication.

Invariant 3

Every Event has stable identity.

Invariant 4

Every Event has a semantic type.

Invariant 5

Every Event has an identifiable source.

Invariant 6

Every Event has an identifiable subject where applicable.

Invariant 7

Event delivery may be duplicated.

Invariant 8

Consumers must be able to deduplicate Events.

Invariant 9

Event arrival order must not be assumed to equal occurrence order unless explicitly guaranteed.

Invariant 10

External Events are not automatically trusted evidence.

Invariant 11

An Event is not automatically an Outcome.

Invariant 12

An Event replay must never unintentionally re-execute a consequential Action.

Invariant 13

Event schema versions must be explicit.

Invariant 14

Event provenance must be preserved where it affects Trust.

Invariant 15

Event freshness must be evaluated where the Event affects consequential decisions.

Invariant 16

Event conflicts must not be resolved through arbitrary source preference.

Invariant 17

Silence is not automatically evidence that nothing changed.

Invariant 18

Event identity is distinct from Action identity and Execution identity.

Invariant 19

Event consumption idempotency is distinct from Action idempotency.

Invariant 20

Events must preserve sufficient causal information to reconstruct relevant execution history.

⸻

94. Canonical Mental Model

                         OCCURRENCE
                              │
                              ▼
                         ┌─────────┐
                         │  EVENT  │
                         └────┬────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
           Context          Evidence        State
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                        TRUST ENGINE
                              │
                              ▼
                           OUTCOME
                              │
                              ▼
                       EVENT / HISTORY

⸻

95. Final Definition

The Event Model is Noema’s canonical representation of observable occurrences across Intent, Trust, Execution, and enterprise systems. Events provide immutable, attributable, versioned, and causally traceable observations that can update Context, provide Evidence, drive deterministic state transitions, and contribute to establishing Outcomes.

The core principle is:

Events tell Noema what happened; they do not tell Noema what to do.

And critically:

An Event is evidence of an occurrence, not automatically proof of an Outcome. Its authority, freshness, provenance, and semantic relationship to the relevant Action must be evaluated before it can participate in a consequential Trust or Execution decision.