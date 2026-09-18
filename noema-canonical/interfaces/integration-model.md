Integration Model

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/integration-model.md

⸻

1. Definition

The Integration Model defines how Noema connects its canonical intent and execution model to external enterprise systems without allowing provider-specific interfaces to redefine Noema’s semantics.

An integration is the boundary between Noema and an external capability, system, service, or human-operated process.

Noema
  │
  │ Canonical Action
  ▼
Integration
  │
  │ Provider-specific translation
  ▼
Enterprise System

The integration layer translates between models. It should not become a second intent engine.

⸻

2. Purpose

The Integration Model defines:

* how external systems are represented
* how capabilities are discovered
* how Actions map to external operations
* how provider APIs are invoked
* how provider responses become evidence
* how external events enter Noema
* how provider failures are represented
* how credentials and authorization are handled
* how provider-specific semantics are isolated
* how integrations evolve without changing Noema’s canonical model

⸻

3. Core Principle

Noema owns the canonical semantic model; integrations own the translation to and from provider-specific systems.

For example:

Noema:
issue_replacement_card
        ↓
Integration:
CardServiceAdapter
        ↓
Provider:
POST /cards/replacement

The provider’s API should not become Noema’s ontology.

⸻

4. Integration Boundary

The conceptual boundary is:

┌───────────────────────────────┐
│             NOEMA             │
│                               │
│ Intent                        │
│ Action                        │
│ Trust                         │
│ Policy                        │
│ Execution                     │
│ Outcome                       │
└──────────────┬────────────────┘
               │
        Integration Boundary
               │
┌──────────────▼────────────────┐
│          INTEGRATION          │
│                               │
│ Adapter                       │
│ Mapping                       │
│ Authentication                │
│ Request Translation            │
│ Response Translation           │
│ Event Translation              │
└──────────────┬────────────────┘
               │
┌──────────────▼────────────────┐
│      ENTERPRISE SYSTEM        │
│                               │
│ API / Database / Provider     │
│ Event Bus / Workflow / Human  │
└───────────────────────────────┘

⸻

5. Integration Is Not an Action

An Integration describes how Noema reaches a system.

An Action describes what Noema intends to cause to happen.

Action:
issue_replacement_card
Integration:
bank_card_service
Operation:
POST /cards/replacement

Multiple integrations may implement the same Action.

⸻

6. One Action, Multiple Integrations

For example:

issue_replacement_card
        │
        ├── Visa Card Service
        ├── Mastercard Card Service
        └── Internal Card Platform

The canonical Action remains:

issue_replacement_card

Only its execution binding changes.

⸻

7. Integration Capability

An integration exposes one or more capabilities.

Integration
    │
    ├── Capability A
    ├── Capability B
    └── Capability C

A capability represents something the connected system can perform or provide.

This connects directly to the canonical ontology/capability.md.

⸻

8. Capability vs Provider Operation

These are not necessarily equivalent.

Provider:

POST /v2/cards/reissue

Noema:

issue_replacement_card

The provider endpoint is an implementation mechanism.

The Noema capability is semantic.

⸻

9. Integration Mapping

The integration layer maps:

Noema Action
      ↓
Integration Mapping
      ↓
Provider Operation

For example:

Action:
freeze_account
Provider:
PATCH /accounts/{id}
Provider payload:
{
  "status": "FROZEN"
}

The mapping translates canonical semantics into provider semantics.

⸻

10. Mapping Is Explicit

Mappings should be explicit and versioned.

Conceptually:

action: freeze_account
integration: banking-core
version: 1
operation: PATCH /accounts/{account_id}

The integration should not infer mappings dynamically during consequential execution unless explicitly permitted.

⸻

11. Integration Contract

Every integration should have a contract describing:

identity
version
capabilities
operations
authentication
inputs
outputs
errors
events
timeouts
retry semantics
idempotency
limits
dependencies

This gives Noema a deterministic integration boundary.

⸻

12. Integration Identity

Each integration should have a stable identity.

Example:

integration_id:
banking-core

Versioning should be explicit:

banking-core@v2

This allows execution history to identify exactly which integration semantics were used.

⸻

13. Integration Versioning

Integrations evolve.

banking-core@v1
banking-core@v2
banking-core@v3

A historical execution should remain interpretable even after the integration changes.

Therefore:

Execution history must reference the integration version used at execution time.

⸻

14. Adapter

An adapter is the executable boundary between Noema and a provider.

Canonical Action
       ↓
Adapter
       ↓
Provider API

The adapter may perform:

* serialization
* authentication
* request construction
* protocol translation
* response parsing
* error normalization
* event normalization

⸻

15. Adapter Responsibility

An adapter is responsible for translation, not policy.

It should not decide:

"Should Noema execute this Action?"

That decision belongs upstream to Trust and Policy.

⸻

16. Provider-Specific Semantics

Providers often have semantics that do not exist in Noema.

Example:

provider_status = PENDING_REVIEW

The adapter may map that to a canonical execution state or evidence type.

But it should not silently invent:

Noema Outcome = SUCCESS

without sufficient evidence.

⸻

17. Provider Response

Provider responses enter Noema as observations.

Provider Response
       ↓
Adapter
       ↓
Normalized Result / Evidence
       ↓
Noema

The provider does not directly mutate canonical state.

⸻

18. Evidence Translation

Example:

Provider:
{
  "transaction_id": "txn_123",
  "status": "completed"
}

Integration translates this into:

Evidence:
provider_confirmation
reference = txn_123
observed_status = completed

Noema can then evaluate whether this satisfies the Action’s postconditions.

⸻

19. External Events

Integrations may receive events from providers.

Provider
   ↓
Webhook / Event Bus
   ↓
Integration
   ↓
Canonical Event
   ↓
Noema

Provider events must be normalized before entering the canonical Event Model.

⸻

20. Event Translation

Example:

Provider:
card.replacement.completed

may become:

Noema:
resource.state_changed

with provider-specific information preserved as evidence or metadata.

⸻

21. Event Identity

External events should retain their original identity.

Example:

provider_event_id = evt_123

Noema should assign its own canonical event identity as well.

Noema Event:
evt_noema_456
External Event:
evt_provider_123

This supports deduplication and auditability.

⸻

22. Event Deduplication

Providers may deliver the same event more than once.

Therefore integrations should support:

external_event_id
source
timestamp
deduplication key

where available.

Duplicate delivery must not produce duplicate semantic effects.

⸻

23. External Systems Are Not Always APIs

An integration may connect to:

REST API
GraphQL API
gRPC service
database
message broker
event stream
SFTP
workflow engine
SaaS platform
CLI
human process

The Integration Model is transport-agnostic.

⸻

24. Human Integration

Some enterprise capabilities may require human interaction.

Noema
   ↓
Human Workflow
   ↓
Enterprise Operator
   ↓
Result / Evidence
   ↓
Noema

This remains an integration boundary even though no machine API exists.

⸻

25. Authentication

Integrations may require:

API keys
OAuth
mTLS
service accounts
signed requests
JWT
delegated credentials

Credential handling belongs to the integration/security infrastructure, not the canonical Action itself.

⸻

26. Authorization Context

An integration must distinguish:

Noema authorization

from:

Provider authentication/authorization

For example:

Noema:
User is authorized to freeze account.
Provider:
Noema's service credential may call freeze-account API.

Both conditions may need to hold.

⸻

27. Credential Isolation

Credentials should never become part of canonical intent.

Incorrect:

Action:
freeze_account
credential:
sk_live_...

Correct:

Action:
freeze_account
Integration:
banking-core
Credential:
managed externally

⸻

28. Secrets

Secrets must be referenced rather than embedded in:

Action
Intent
Execution Event
Audit Log
Evidence

The integration layer resolves credentials securely at execution time.

⸻

29. Tenant Isolation

An integration may be configured differently per enterprise tenant.

Tenant A
  ↓
banking-core → Provider Account A
Tenant B
  ↓
banking-core → Provider Account B

The canonical integration identity may remain the same while configuration differs.

⸻

30. Integration Configuration

Configuration may include:

endpoint
credential reference
tenant mapping
timeouts
rate limits
provider options
feature flags

Configuration should be separate from the semantic Action.

⸻

31. Environment Isolation

Integrations may exist across:

development
staging
production

An execution must never accidentally resolve a production integration from a non-production context.

Environment should therefore be explicit where relevant.

⸻

32. Integration Selection

When multiple integrations can satisfy a capability:

Capability
    │
    ├── Integration A
    ├── Integration B
    └── Integration C

selection should be deterministic according to:

policy
tenant configuration
capability compatibility
availability
risk
cost
routing rules

It should not be an arbitrary model choice during execution.

⸻

33. Integration Discovery

Noema may discover integrations from:

API schemas
OpenAPI
GraphQL schemas
gRPC definitions
documentation
event schemas
configuration
enterprise metadata
human configuration

Discovery provides information.

It does not automatically make every discovered operation executable.

⸻

34. Discovery vs Registration

Discovery:

"What does this system appear to expose?"

Registration:

"What has Noema explicitly accepted as an integration?"

These should remain separate.

⸻

35. Registration

A registered integration becomes part of Noema’s executable environment.

Registration should establish:

identity
version
capabilities
contracts
credentials
environment
ownership

⸻

36. Validation

Before registration or activation, Noema should validate:

schema compatibility
authentication
capability mappings
Action Contracts
event mappings
failure mappings
idempotency behavior
health

An integration that cannot satisfy required contracts should not be marked executable.

⸻

37. Integration Health

Integrations may expose health signals:

AVAILABLE
DEGRADED
UNAVAILABLE
UNKNOWN

Health is contextual.

A provider being unavailable does not necessarily mean every Action using that integration is permanently impossible.

⸻

38. Rate Limits

Providers may impose:

requests/second
requests/minute
concurrency limits
daily quotas

These constraints should be represented in the integration contract.

Execution planning and scheduling can then account for them.

⸻

39. Rate-Limit Failure

A provider response such as:

HTTP 429

should be normalized into an appropriate failure class.

For example:

TRANSIENT_FAILURE

with retry-after information preserved where available.

⸻

40. Provider Timeouts

Provider timeout behavior should be explicit.

Noema → Integration → Provider
                       ↓
                    timeout

The adapter must distinguish:

provider rejected request

from:

provider response unknown

This feeds directly into the Execution domain's UNKNOWN state.

⸻

41. Idempotency

Where provider APIs support idempotency:

Noema execution_id
      ↓
provider idempotency key

The integration should map the identities appropriately.

⸻

42. Provider Idempotency

Provider idempotency keys must be stable across retries of the same logical operation where the provider contract requires it.

Example:

Action:
charge_customer
Attempt 1:
provider_key = exe_123
Attempt 2:
provider_key = exe_123

This can prevent duplicate external effects.

The exact mapping depends on the provider’s semantics.

⸻

43. Integration Failure Normalization

Providers expose different error formats.

Provider A:

{"error":"insufficient_funds"}

Provider B:

{"code":"BAL_001"}

Noema should normalize these into canonical failure semantics:

PRECONDITION_FAILURE

while preserving the provider-specific error as evidence/metadata.

⸻

44. Do Not Destroy Provider Detail

Normalization must not discard useful information.

Canonical:

failure = TRANSIENT_FAILURE

should be able to retain:

provider_code
provider_message
provider_request_id
provider_status
raw_reference

subject to security and privacy constraints.

⸻

45. Provider State vs Noema State

A provider may have:

PENDING
PROCESSING
COMPLETED

while Noema has:

EXECUTING
UNKNOWN
OUTCOME_PENDING

These state systems must not be conflated.

The integration translates provider observations into Noema-relevant evidence.

⸻

46. External State Is Observed

Noema does not automatically own the provider’s business state.

For example:

Banking System:
account balance = $500

Noema may observe it.

Noema does not become the authoritative ledger.

This preserves the core Noema boundary:

Noema owns the execution journey, not enterprise business state.

⸻

47. Resource References

Integrations should return stable references to external resources.

Example:

resource_type = card
resource_id = card_123
provider = banking-core

Noema can use these references in subsequent Actions.

⸻

48. Resource Identity

Provider resource identity should remain distinguishable from Noema identity.

Noema resource reference:
res_123
Provider:
card_456

Mappings should be explicit.

⸻

49. Integration and Resource Model

The relationship is:

Noema Resource
      ↓
External Resource Reference
      ↓
Integration
      ↓
Provider Resource

This allows Noema to reason about external entities without claiming ownership of their underlying state.

⸻

50. Integration Composition

A single execution may involve multiple integrations.

Example:

Create Customer
      ↓
CRM Integration
      ↓
Payment Integration
      ↓
Notification Integration

Each integration remains independently identifiable.

⸻

51. Integration Failure in Composition

If:

CRM → SUCCESS
Payment → SUCCESS
Notification → FAILED

the overall execution must preserve the partial execution state.

Possible recovery:

retry notification

rather than repeating the successful payment.

This is one reason execution identity and step-level state matter.

⸻

52. Integration Dependencies

Integrations may depend on other integrations.

Example:

Identity Provider
      ↓
Payment Provider

Dependency relationships should be explicit when they affect execution.

⸻

53. Integration Lifecycle

A conceptual lifecycle:

DISCOVERED
    ↓
REGISTERED
    ↓
VALIDATED
    ↓
ACTIVE
    ↓
DEGRADED
    ↓
SUSPENDED
    ↓
DEPRECATED
    ↓
REMOVED

Historical executions must remain interpretable after an integration becomes deprecated.

⸻

54. Integration Deprecation

Deprecation must not invalidate historical execution records.

If:

banking-core@v1

is deprecated, historical executions must continue to reference:

banking-core@v1

rather than being rewritten to v2.

⸻

55. Integration Replacement

A new integration may replace an old one:

banking-core@v1
       ↓
banking-core@v2

But the replacement should be explicitly validated for semantic compatibility.

Identical endpoint shape does not imply identical Action semantics.

⸻

56. Semantic Compatibility

Two integrations are compatible only if they can satisfy the same relevant:

Capabilities
Action Contracts
Preconditions
Postconditions
Failure semantics
Idempotency requirements
Evidence requirements

⸻

57. Integration Observability

Every integration invocation should make available, where appropriate:

integration_id
integration_version
execution_id
attempt_id
provider_request_id
timestamps
latency
status
failure

This enables debugging without contaminating the canonical semantic model.

⸻

58. Correlation

Requests, events, and provider operations should be correlatable.

Conceptually:

intent_id
   ↓
action_id
   ↓
execution_id
   ↓
attempt_id
   ↓
provider_request_id
   ↓
provider_event_id

This chain is extremely valuable for audit and reconciliation.

⸻

59. Integration Security Boundary

The integration boundary is untrusted from Noema’s semantic perspective.

Provider responses must be treated as:

observations

not unquestioned truth.

They must pass through validation and evidence handling.

⸻

60. Provider Claims

A provider may claim:

status = completed

Noema should ask:

Does this evidence satisfy the Action's postconditions?

rather than blindly accepting the provider’s terminology.

⸻

61. Integration Trust

The trustworthiness of an integration can itself be modeled.

Potential dimensions include:

identity
authentication
schema integrity
provider reliability
evidence quality
execution guarantees

This can influence Trust and Risk decisions without making the integration itself the Trust Engine.

⸻

62. Integration Contracts and Action Contracts

These contracts operate at different layers.

Action Contract
"What must be true for this Action?"
Integration Contract
"How can this system perform or observe it?"

The Integration Contract must satisfy the Action Contract.

⸻

63. Example

Canonical Action:

refund_payment

Action Contract:

Precondition:
payment exists
Postcondition:
refunded_amount = requested_amount

Integration:

Stripe Adapter

Provider operation:

POST /refunds

Provider response:

refund_id = re_123
status = succeeded

Noema evaluates whether this evidence satisfies the canonical postcondition.

⸻

64. Multiple Provider Implementations

The same Action may be executed through:

Stripe
Adyen
Internal Payment Service

The Action Contract remains stable.

The integration binding varies.

This separation allows enterprise-specific infrastructure without fragmenting Noema’s semantic model.

⸻

65. Integration as Translation Layer

The fundamental transformation is:

Canonical Noema Model
        ↕
Integration Mapping
        ↕
Provider Model

This is the central purpose of the Integration Model.

⸻

66. What Integrations Must Not Do

An integration must not:

* reinterpret user intent
* bypass Trust
* override Policy
* manufacture authorization
* silently change an Action
* declare success without sufficient evidence
* hide provider uncertainty
* mutate canonical business state as if it were authoritative
* silently retry unsafe operations
* embed secrets in canonical objects

⸻

67. What Integrations May Do

An integration may:

* translate requests
* authenticate with providers
* invoke provider operations
* normalize provider responses
* normalize provider failures
* receive provider events
* expose provider capabilities
* provide external resource references
* supply evidence
* perform provider-specific protocol handling
* implement provider-specific idempotency

⸻

68. Integration Invariants

Invariant 1

An Integration is an implementation boundary, not an intent boundary.

Invariant 2

Canonical Actions remain provider-independent.

Invariant 3

Provider-specific operations must be explicitly mapped.

Invariant 4

Integration versions must be identifiable.

Invariant 5

Provider responses are observations and evidence, not automatic canonical truth.

Invariant 6

Provider uncertainty must not be converted into false certainty.

Invariant 7

Integration credentials must remain outside canonical semantic objects.

Invariant 8

External events must be deduplicatable.

Invariant 9

Provider failures must be normalized without destroying provider-specific detail.

Invariant 10

Provider resource identity must remain distinguishable from Noema identity.

Invariant 11

Integration selection must obey policy and execution constraints.

Invariant 12

Historical executions must remain interpretable after integration changes.

Invariant 13

Integration failure must not silently corrupt canonical execution state.

Invariant 14

Integration adapters must not bypass Trust or Authorization.

Invariant 15

Integration capabilities must not automatically become executable capabilities merely because they were discovered.

⸻

69. Canonical Mental Model

                         NOEMA
                           │
                   Canonical Action
                           │
                           ▼
                    Action Contract
                           │
                           ▼
                    Trust / Policy
                           │
                           ▼
                    Execution Model
                           │
                           ▼
                  ┌─────────────────┐
                  │   INTEGRATION   │
                  │                 │
                  │ Mapping         │
                  │ Adapter         │
                  │ Auth            │
                  │ Translation     │
                  │ Error Mapping   │
                  │ Event Mapping   │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           REST API     Event Bus     Human
              │            │            │
              └────────────┼────────────┘
                           ▼
                    Enterprise System
                           │
                           ▼
                      Observation
                           │
                           ▼
                        Evidence
                           │
                           ▼
                  Postcondition Check
                           │
                           ▼
                         Outcome

⸻

70. Relationship to the Noema Architecture

The Integration Model sits at the edge of the system:

thesis
    ↓
ontology
    ↓
intent
    ↓
trust
    ↓
execution
    ↓
interfaces
    ↓
Enterprise Systems

Within interfaces:

Intent API
Action API
Trust API
Context API
Event Model
Execution API
Integration Model

form the primary external boundaries.

⸻

71. Final Definition

The Integration Model defines the canonical boundary between Noema’s semantic execution system and external enterprise systems. It specifies how capabilities are exposed, Actions are mapped to provider operations, requests and responses are translated, external events are normalized, provider failures are represented, and external state becomes evidence without allowing provider-specific semantics to redefine Noema’s canonical model.

The most important architectural rule is:

Noema speaks in canonical Actions and Outcomes. Integrations speak in provider-specific operations and observations. The Integration Model is the translation layer between the two.