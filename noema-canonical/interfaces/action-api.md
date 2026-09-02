Action API

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/action-api.md

⸻

1. Definition

The Action API is the interface through which an external consumer submits, observes, and manages executable Actions within Noema.

It defines the boundary between:

External System / Consumer
            ↓
        Action API
            ↓
          Noema
            ↓
     Execution System

The Action API is not the mechanism that determines what the user intended, and it is not the business system executing the Action.

It is the protocol through which executable work crosses the Noema boundary.

⸻

2. Purpose

The Action API exists to provide a stable, machine-readable interface for:

* submitting executable Actions
* referencing Action Contracts
* supplying execution context
* requesting execution
* observing execution state
* retrieving Outcomes
* handling failures
* supporting reconciliation
* interacting with human intervention where required

The API should expose Noema’s execution semantics without requiring consumers to understand Noema’s internal implementation.

⸻

3. Core Principle

The Action API exposes executable intent and execution state as explicit contracts, not as arbitrary commands.

A consumer should not need to know:

how Noema planned the Action
how Trust evaluated it internally
which executor processed it
which queue carried it
which worker executed it

It should interact with stable semantic interfaces.

⸻

4. Action API Boundary

The conceptual boundary is:

                 NOEMA
                   │
       ┌───────────┴───────────┐
       │                       │
    Intent                  Execution
       │                       │
       └───────────┬───────────┘
                   │
              Action API
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
   Enterprise   Agent       Consumer
    System      System       Service

The API therefore acts as an execution boundary, not merely an HTTP interface.

⸻

5. What the Action API Owns

The Action API owns the protocol semantics for:

Action submission
Action identity
Action status
Action lifecycle
Action observation
Action cancellation
Action retry requests where permitted
Outcome retrieval
Execution references

It does not own:

Enterprise account state
Enterprise balances
Enterprise permissions
Enterprise business records
Provider-specific business state

Those remain owned by the relevant systems.

⸻

6. Action Identity

Every Action submitted through the API should have a stable logical identity.

Conceptually:

action_id

Example:

act_01JXYZ...

This identity represents the logical Action, not a particular execution attempt.

⸻

7. Execution Identity

A logical Action may produce multiple execution attempts.

Therefore:

action_id
    │
    ├── execution_1
    │      ├── attempt_1
    │      └── attempt_2
    │
    └── execution_2

The API should distinguish:

Action
Execution
Attempt

rather than collapsing them into one identifier.

⸻

8. Action Submission

Conceptually:

POST /actions

A submission should contain enough information to establish the Action’s execution contract.

Example:

{
  "action": "issue_replacement_card",
  "actor": "customer_123",
  "inputs": {
    "card_id": "card_456"
  },
  "context": {
    "channel": "mobile"
  }
}

The exact transport and schema are implementation concerns.

The canonical model is semantic rather than tied to HTTP.

⸻

9. Action Submission Is Not Execution

Submitting an Action does not necessarily mean:

execute immediately

The API may return:

ACCEPTED

while Noema performs:

validation
authorization
precondition evaluation
planning
scheduling
execution

Therefore:

Action acceptance and Action execution are distinct states.

⸻

10. Action Acceptance

An Action may be accepted when:

request is syntactically valid
Action is recognized
contract can be resolved
required inputs are present

But acceptance does not guarantee:

authorization
execution eligibility
successful execution

⸻

11. Action Lifecycle

The API should expose the Action lifecycle defined by the Execution domain.

Conceptually:

SUBMITTED
    ↓
ACCEPTED
    ↓
VALIDATING
    ↓
AUTHORIZED
    ↓
READY
    ↓
EXECUTING
    ↓
COMPLETED

Alternative paths include:

CLARIFICATION_REQUIRED
BLOCKED
REJECTED
FAILED
UNKNOWN
RECONCILIATING
CANCELLED

The exact canonical state machine should remain aligned with 04-execution/execution-model.md.

⸻

12. Action Contract Reference

An Action should resolve against an Action Contract.

Conceptually:

{
  "action": "issue_replacement_card",
  "contract": {
    "name": "issue_replacement_card",
    "version": "1.2"
  }
}

The API should make contract identity observable.

This allows consumers to determine:

which semantic contract governed execution

⸻

13. Contract Versioning

Action Contracts should be versioned.

For example:

issue_replacement_card@1.0
issue_replacement_card@1.1
issue_replacement_card@2.0

A previously accepted Action should not silently change semantics because the underlying contract was updated.

⸻

14. Action Input

Action inputs describe the values required by the Action.

Example:

{
  "inputs": {
    "customer_id": "cus_123",
    "card_id": "card_456"
  }
}

Inputs are not the same as Intent.

Intent answers:

What does the user want?

Action inputs answer:

What concrete values does this executable Action require?

⸻

15. Context

Actions may carry execution context.

Examples:

channel
locale
request_source
session_reference
correlation_id
tenant
environment

Context provides execution-relevant information but should not be used to smuggle untrusted authorization claims into the Action.

⸻

16. Actor

The API should identify the Actor on whose behalf the Action is being executed.

Conceptually:

{
  "actor": {
    "type": "customer",
    "id": "cus_123"
  }
}

Actor identity must be established through trusted authentication and authorization mechanisms.

A caller-provided identifier alone is not proof of identity.

⸻

17. Resources

Actions may operate on Resources.

Example:

{
  "resource": {
    "type": "card",
    "id": "card_456"
  }
}

Resource references should be explicit where possible.

⸻

18. Idempotency

The Action API should support idempotent submission.

Example:

Idempotency-Key: 01JXYZ...

This protects against:

client timeout
network retry
duplicate submission
consumer crash

without creating multiple logical Actions unintentionally.

⸻

19. Idempotency Scope

The API must define what an idempotency key represents.

A useful semantic model is:

idempotency key
        ↓
logical Action submission

It should not automatically mean:

execution attempt

Multiple execution attempts may belong to one idempotent Action.

⸻

20. Duplicate Submission

Suppose the client sends:

POST /actions
Idempotency-Key: abc

and does not receive a response.

The client retries:

POST /actions
Idempotency-Key: abc

The API should recognize:

same logical submission

rather than creating another Action.

⸻

21. Correlation

Actions should support correlation identifiers.

Example:

correlation_id
request_id
trace_id

These allow consumers to connect:

user request
→ intent
→ action
→ execution
→ attempts
→ outcome

across distributed systems.

⸻

22. Action Status

Consumers need a stable way to inspect Action state.

Conceptually:

GET /actions/{action_id}

Response:

{
  "id": "act_123",
  "status": "EXECUTING"
}

The API should expose canonical states rather than arbitrary worker statuses.

⸻

23. Status Is Not Outcome

This distinction is important.

status = COMPLETED

describes the lifecycle state of the Action.

The:

Outcome

describes what was actually established by execution.

For example:

status:
COMPLETED
outcome:
replacement_card_id = card_789

⸻

24. Outcome Retrieval

The API should expose the resulting Outcome where appropriate.

Conceptually:

GET /actions/{action_id}/outcome

The Outcome should be grounded in observed evidence and postcondition evaluation.

It should not merely contain:

"the executor said it worked."

⸻

25. Evidence

Where appropriate, the API may expose references to the evidence supporting the Outcome.

For example:

{
  "outcome": {
    "status": "SUCCESS",
    "evidence": [
      {
        "source": "card_service",
        "reference": "evt_789"
      }
    ]
  }
}

The API should avoid leaking sensitive internal evidence unnecessarily.

⸻

26. Preconditions

The API may expose precondition status.

Example:

{
  "preconditions": [
    {
      "condition": "card.status == LOST",
      "status": "SATISFIED"
    }
  ]
}

This is valuable for observability and intervention.

However, consumers should not be able to arbitrarily mark preconditions as satisfied unless the relevant contract explicitly supports a trusted attestation mechanism.

⸻

27. Authorization

Authorization state may be observable.

Conceptually:

authorization:
    status = APPROVED

But the Action API must not allow a caller to self-authorize a consequential Action.

Authorization is determined by the Trust and policy layers.

⸻

28. Action Errors

Errors should be structured.

Example:

{
  "error": {
    "code": "PRECONDITION_NOT_SATISFIED",
    "message": "Card is not in a replaceable state."
  }
}

The error code should be machine-readable.

The human-readable message should be considered supplementary.

⸻

29. Error Categories

The API should distinguish at least:

INVALID_REQUEST
UNKNOWN_ACTION
CONTRACT_INVALID
PRECONDITION_NOT_SATISFIED
AUTHORIZATION_FAILED
POLICY_BLOCKED
EXECUTION_FAILED
EXECUTION_UNKNOWN
RECONCILIATION_REQUIRED
CANCELLED
RETRY_EXHAUSTED
HUMAN_INTERVENTION_REQUIRED

Exact codes belong to the canonical API specification.

⸻

30. Unknown Is a First-Class State

The API must never collapse:

UNKNOWN

into:

FAILED

Example:

POST payment
→ timeout

The API should represent:

execution_status = UNKNOWN

if the system cannot establish whether the payment occurred.

This is essential for safe retries.

⸻

31. Reconciliation

An Action may enter:

RECONCILIATING

when Noema needs to establish external reality.

Consumers should be able to observe this state.

Example:

POST /actions/{id}/reconcile

Whether reconciliation is consumer-triggered or system-triggered is an implementation decision.

⸻

32. Retry Interface

A retry may be exposed as an API operation where consumer-controlled retry is appropriate.

Conceptually:

POST /actions/{action_id}/retry

However:

The API must not interpret a retry request as permission to bypass Noema’s retry policy.

The request means:

"evaluate whether this Action may be retried."

not:

"execute this Action again regardless of safety."

⸻

33. Cancel Interface

Where cancellation is supported:

POST /actions/{action_id}/cancel

Cancellation is a request to transition the Action into a cancellable state.

It does not necessarily mean:

external execution has been reversed

If the Action already produced effects, compensation may be required.

⸻

34. Cancellation Semantics

An Action may be:

CANCELLED

before execution.

But after an irreversible external side effect:

CANCEL

may no longer be sufficient.

The API must distinguish:

prevent execution

from:

reverse execution

⸻

35. Human Intervention

Some Actions may enter:

HUMAN_INTERVENTION_REQUIRED

The API should allow consumers or authorized operators to observe the intervention requirement.

Example:

{
  "status": "HUMAN_INTERVENTION_REQUIRED",
  "reason": "Manager approval required."
}

Human intervention remains governed by Trust and policy.

⸻

36. Clarification

An Action may require clarification before it can become executable.

Example:

status = CLARIFICATION_REQUIRED

The API should expose the unresolved requirement.

Example:

{
  "clarification": {
    "field": "destination",
    "reason": "Multiple destinations were possible."
  }
}

Noema must not silently choose one.

⸻

37. Action API and Intent API

These should remain separate conceptual interfaces.

Intent API
    ↓
resolve what the user means
    ↓
Executable Intent
    ↓
Action API
    ↓
execute

The Action API should not become a second Intent parser.

⸻

38. Action API and Execution API

Likewise:

Action API

is the external semantic boundary.

The internal:

Execution API

may be an implementation mechanism used by workers, executors, or consumers.

Consumers should not need access to internal execution machinery.

⸻

39. Consumer Model

A consumer might receive:

Action:
issue_replacement_card

and execute it against its own domain system.

Conceptually:

Noema
  │
  │ Action Contract
  ▼
Consumer
  │
  ▼
Enterprise System

The consumer reports execution evidence and outcome back through the appropriate interface.

⸻

40. Action Delivery

The Action API may support:

pull
push
webhook
event stream
queue

The transport is not the canonical model.

The semantic contract remains:

Action
→ Consumer
→ Execution
→ Evidence
→ Outcome

⸻

41. Webhooks

For asynchronous consumers, Noema may notify external systems when Action state changes.

Example:

action.completed
action.failed
action.blocked
action.requires_intervention

Webhook delivery itself must be treated as an unreliable transport.

Consumers should use Action identity to retrieve authoritative state.

⸻

42. Eventual Consistency

Action status may propagate asynchronously.

Therefore:

webhook:
ACTION_COMPLETED

should not necessarily be treated as the complete source of truth.

The Action API’s canonical resource should remain authoritative.

⸻

43. Polling

Consumers may poll:

GET /actions/{action_id}

where event-driven delivery is unavailable.

Polling should not change Action semantics.

⸻

44. Long-Running Actions

The API must support Actions whose execution exceeds a normal request-response lifetime.

Instead of:

POST /actions

blocking until completion, the API may return:

202 Accepted

with:

action_id
status_url

Conceptually:

{
  "id": "act_123",
  "status": "ACCEPTED"
}

⸻

45. Synchronous Actions

Some low-risk or fast Actions may complete within the submission request.

The API may return:

200 OK

with the resulting Outcome.

However:

Synchronous transport must not imply synchronous semantics.

The underlying Action remains governed by the same execution model.

⸻

46. API Does Not Guarantee Immediate Execution

A consumer should not infer:

POST /actions succeeded

means:

business operation succeeded

It means the Action request was accepted according to the API’s semantics.

The response contract must make this distinction explicit.

⸻

47. Tenant Isolation

Enterprise Actions must remain scoped to their owning tenant or enterprise context.

Conceptually:

tenant
   ↓
Action
   ↓
Actor
   ↓
Resources

An Action from one tenant must never be able to reference another tenant’s resources through identifier guessing or manipulated input.

⸻

48. Authentication

The Action API requires authenticated callers.

Authentication establishes:

who is calling

It does not by itself establish:

who the Action is on behalf of

That distinction belongs to Actor and Authorization semantics.

⸻

49. Authorization

Authorization establishes:

whether the caller may perform the requested operation

and, where applicable:

whether the Actor represented by the Action is permitted to cause the Action.

These should not be conflated.

⸻

50. API Security Boundary

The API must treat all caller-provided values as untrusted until validated.

This includes:

actor
resource
authorization claims
context
inputs
callback URLs
metadata

Trust must be established through the appropriate system.

⸻

51. Action API and Enterprise Ownership

Noema should not become the system of record for enterprise business state merely because the Action API exposes references to that state.

For example:

Action:
refund_payment

Noema may record:

payment_id
execution history
authorization
evidence references
outcome

The enterprise/payment system remains authoritative for:

payment balance
ledger
refund accounting

⸻

52. Action API as System of Execution Record

Noema can be authoritative for:

what Action was requested
what contract governed it
what trust decisions occurred
what execution attempts occurred
what evidence was observed
what Outcome was established

This is different from owning the underlying business domain.

⸻

53. API Versioning

The Action API itself must be versioned independently from Action Contract versions.

For example:

API v1
Action Contract v3

These represent different compatibility boundaries.

⸻

54. Backward Compatibility

API evolution should preserve semantic compatibility where possible.

Changing:

field names
response structure
state semantics
error semantics

can break consumers even if the transport remains HTTP.

Therefore semantic versioning must include the meaning of the interface.

⸻

55. Action API and Schema Validation

Requests should be validated before entering execution.

Validation includes:

schema
required fields
types
Action identity
contract compatibility
tenant scope
input constraints

Validation failure should not create an executable Action.

⸻

56. Action API and Intent Validation

The API should not accept arbitrary natural-language text as though it were already executable.

For example:

{
  "action": "do whatever is necessary"
}

is not an executable Action.

It must first pass through Intent resolution.

⸻

57. Action API and Executable Intent

The ideal boundary is:

Natural Language
      ↓
Intent Model
      ↓
Intent Resolution
      ↓
Executable Intent
      ↓
Action API

The Action API operates on already-resolved semantics.

⸻

58. Action API and Trust Engine

The API should invoke or depend upon Trust evaluation before allowing consequential execution.

Conceptually:

Action submitted
      ↓
Validation
      ↓
Trust evaluation
      ↓
Authorization
      ↓
Preconditions
      ↓
Execution

The API should not independently reproduce Trust logic.

⸻

59. Action API and Policy

Policy determines whether an Action is permissible.

The API exposes the result:

ALLOWED
BLOCKED
REQUIRES_APPROVAL

rather than allowing consumers to override policy.

⸻

60. Action API and Action Contract

The Action Contract defines:

what the Action means
required inputs
preconditions
authorization requirements
execution semantics
idempotency requirements
postconditions
failure semantics

The Action API transports and exposes this contract.

⸻

61. Action API and Execution Attempt

A consumer may receive an execution request containing:

{
  "action_id": "act_123",
  "execution_id": "exe_456",
  "attempt_id": "att_789",
  "contract": "issue_replacement_card@1.2"
}

This allows the consumer to correlate its work with Noema’s execution record.

⸻

62. Action Acknowledgement

Consumers may need to acknowledge receipt.

Conceptually:

Action delivered
       ↓
ACK
       ↓
Consumer owns execution attempt

Acknowledgement should not mean:

Action succeeded

It only establishes delivery/ownership semantics.

⸻

63. Execution Result

The consumer should return a structured execution result.

Conceptually:

{
  "status": "SUCCESS",
  "evidence": [],
  "result": {}
}

The result must then be evaluated against the Action’s expected postconditions.

⸻

64. Consumer Claims vs Established Outcome

A consumer saying:

status = SUCCESS

is evidence.

It is not necessarily the final semantic Outcome.

Noema may need to validate:

postconditions
evidence
provider state

before establishing the canonical Outcome.

This distinction is central to Noema’s Trust architecture.

⸻

65. Action API and Evidence

A result may contain:

evidence references
provider event IDs
resource versions
timestamps
execution metadata

The API should preserve enough provenance to establish why the Action reached its final state.

⸻

66. Action API and Recovery

The API should expose enough state to allow consumers to recover after:

process crash
network failure
consumer restart
Noema restart
provider outage

Stable identifiers are therefore fundamental.

⸻

67. Action API and Exactly-Once Semantics

The API should not assume that distributed execution can provide universal exactly-once semantics.

Instead, it should rely on:

idempotency
deduplication
execution identity
reconciliation
atomicity

where necessary.

The canonical principle is:

Exactly-once effects are established through system design, not assumed from message delivery.

⸻

68. Action API and At-Least-Once Delivery

Action delivery may be at-least-once:

delivery 1
delivery 2
delivery 3

Consumers must therefore safely recognize:

same action_id
same execution_id
same attempt_id

and avoid unintended duplicate effects.

⸻

69. Action API and At-Most-Once Delivery

At-most-once delivery avoids duplicates at the cost of possible loss.

For consequential Actions, losing an Action can be unacceptable.

Therefore Noema should prefer explicit execution-state tracking over relying purely on transport semantics.

⸻

70. Action API Observability

The API should expose:

action_id
execution_id
attempt_id
status
timestamps
contract_version
failure classification
retry state
intervention state
outcome

Consumers should not need access to internal worker logs to understand the Action lifecycle.

⸻

71. Action API Audit Trail

The Action resource should support reconstruction of:

Intent
   ↓
Action
   ↓
Trust decision
   ↓
Preconditions
   ↓
Execution attempts
   ↓
Evidence
   ↓
Postconditions
   ↓
Outcome

This provides the execution audit trail.

⸻

72. Action API and Determinism

The API itself should be deterministic in its semantic interpretation.

For the same:

Action
contract
inputs
authorization
state
policy

the system should not randomly produce different execution decisions.

LLM inference may exist upstream, but the Action API must operate on resolved executable semantics.

⸻

73. Action API and Ambiguity

An ambiguous request should not reach the Action API as an executable Action.

Instead:

Ambiguous Intent
      ↓
Clarification
      ↓
Resolved Intent
      ↓
Executable Action

This preserves the boundary between probabilistic interpretation and deterministic execution.

⸻

74. Action API and Human Confirmation

Certain Actions may require explicit user confirmation.

Example:

Action:
transfer ₦5,000,000

Trust policy:

confirmation_required = TRUE

The API can expose:

AWAITING_CONFIRMATION

rather than executing.

⸻

75. Confirmation Is Not Authorization

User confirmation means:

the user explicitly confirmed the proposed Action

Authorization means:

the policy permits the Actor to perform it

Both may be required.

⸻

76. Action API and Risk

Risk evaluation can affect API-visible state.

For example:

LOW_RISK
MEDIUM_RISK
HIGH_RISK
CRITICAL

A high-risk Action may become:

REQUIRES_APPROVAL

rather than:

READY

The API exposes the resulting execution state, not an independent risk decision.

⸻

77. Action API and Multi-Step Execution

A single Action may produce multiple internal steps.

The API should distinguish:

logical Action

from:

execution plan

and:

internal steps

Consumers generally care about the logical Action unless the contract explicitly exposes step-level execution.

⸻

78. Action API and Composite Actions

For composite Actions:

renew_card
 ├── verify_eligibility
 ├── issue_card
 └── activate_card

the API may expose:

overall Action

while keeping individual steps internal.

If steps are exposed, they should have stable identities and explicit semantics.

⸻

79. API Resource Model

A conceptual Action resource:

{
  "id": "act_123",
  "type": "issue_replacement_card",
  "contract": {
    "name": "issue_replacement_card",
    "version": "1.2"
  },
  "actor": {
    "type": "customer",
    "id": "cus_123"
  },
  "status": "EXECUTING",
  "execution": {
    "id": "exe_456",
    "attempt": 1
  },
  "created_at": "...",
  "updated_at": "..."
}

This is illustrative rather than a finalized wire schema.

⸻

80. Canonical Operations

The Action API should conceptually support:

Create Action
Get Action
List Actions
Get Action Outcome
Get Action Execution
Request Retry
Request Cancellation
Request Reconciliation
Acknowledge Action
Submit Execution Result

Not every consumer needs every operation.

⸻

81. Read vs Command Operations

A useful distinction:

Query

GET /actions/{id}

Observes state.

Command

POST /actions/{id}/retry

Requests a state transition.

The API must make this distinction explicit.

⸻

82. Commands Are Requests, Not Overrides

Calling:

POST /actions/{id}/retry

does not mean:

retry unconditionally

It means:

evaluate whether retry is permitted

Likewise:

POST /actions/{id}/cancel

means:

evaluate whether cancellation is currently possible

⸻

83. API Error Semantics

HTTP or transport status codes should communicate protocol-level outcomes.

Domain-specific execution state should remain in the response body/resource.

For example:

HTTP 202
status = EXECUTING

is different from:

HTTP 400
status = INVALID_REQUEST

The exact HTTP mapping belongs to the implementation specification.

⸻

84. API Should Be Transport-Agnostic

Although the first implementation may use:

HTTP + JSON

the canonical Action API should describe semantic operations independently of transport.

The same contract could eventually support:

HTTP
gRPC
events
message queues
SDKs

without changing the meaning of an Action.

⸻

85. API as a Stable Integration Boundary

Enterprise integrations should depend on:

Action Contract
Action API
Event semantics
Outcome semantics

rather than:

Noema internals
worker implementation
database schema
queue implementation
LLM provider

This is critical for Noema’s architectural durability.

⸻

86. What the Action API Must Not Become

The Action API must not become:

A generic RPC proxy

POST /execute-anything

An LLM command endpoint

POST /do-what-user-meant

A business database

GET /customers
GET /balances

unless such access is explicitly part of an integration boundary.

A policy bypass

POST /actions/{id}/force

A hidden workflow engine

The API should expose workflow semantics without coupling consumers to internal orchestration.

⸻

87. Canonical Relationship to Other Domains

02-intent
    ↓
Executable Intent
    ↓
03-trust
    ↓
Authorization / Risk / Policy
    ↓
04-execution
    ↓
Action Contract / Preconditions / Execution
    ↓
05-interfaces
    ↓
Action API
    ↓
External Consumers

Interfaces are therefore the boundary, not the source of truth for the underlying semantics.

⸻

88. Invariants

Invariant 1

Every executable Action has a stable logical identity.

Invariant 2

Action identity is distinct from execution-attempt identity.

Invariant 3

Action submission does not imply successful execution.

Invariant 4

The Action API does not bypass Trust, Policy, Authorization, or Preconditions.

Invariant 5

Unknown execution state must remain distinguishable from definitive failure.

Invariant 6

Retry requests must be evaluated against retry policy.

Invariant 7

Action Contracts must be explicitly versioned.

Invariant 8

An Action must be traceable from submission through Outcome.

Invariant 9

Caller-provided claims must not be treated as authoritative evidence without validation.

Invariant 10

Action status and Outcome must remain conceptually distinct.

Invariant 11

The API must support asynchronous execution.

Invariant 12

Consumers must be able to recover Action state without relying solely on event delivery.

Invariant 13

The API must support idempotent submission for operations where duplicate creation is possible.

Invariant 14

The API must not require consumers to understand Noema’s internal execution implementation.

Invariant 15

Cancellation must not be represented as compensation.

Invariant 16

Retry must not be represented as a new logical Intent.

Invariant 17

Noema must not silently resolve ambiguity at the Action API boundary.

Invariant 18

The Action API must preserve enough provenance to reconstruct the execution journey.

⸻

89. Canonical Mental Model

                    USER / SYSTEM
                         │
                         ▼
                    INTENT
                         │
                         ▼
               EXECUTABLE INTENT
                         │
                         ▼
                 ┌───────────────┐
                 │   TRUST       │
                 │ policy/risk   │
                 │ authorization │
                 └───────┬───────┘
                         │
                         ▼
                 ACTION CONTRACT
                         │
                         ▼
                    ACTION API
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Consumer    Executor   Enterprise
              │          │          │
              └──────────┼──────────┘
                         ▼
                    EXECUTION
                         │
                         ▼
                      EVIDENCE
                         │
                         ▼
                  POSTCONDITIONS
                         │
                         ▼
                      OUTCOME

⸻

90. Final Definition

The Action API is Noema’s external execution boundary: a stable, transport-independent interface through which executable Actions are submitted, observed, controlled, and reconciled. It exposes Action identity, contract, lifecycle, execution state, and Outcome without transferring ownership of enterprise business state to Noema.

The core principle is:

The Action API is not a “do this” endpoint. It is a contract boundary through which Noema turns a trusted, executable Action into an observable execution journey—without allowing the interface itself to bypass intent resolution, Trust, policy, authorization, preconditions, or execution safety.