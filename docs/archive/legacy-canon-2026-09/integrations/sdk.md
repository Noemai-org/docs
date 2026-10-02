> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Integration SDK

Status: Foundational
Version: 0.1
Domain: Integrations
Canonical Path: integrations/sdk.md

⸻

1. Definition

The Integration SDK defines the developer-facing primitives, interfaces, lifecycle, and constraints for building integrations between Noema and external enterprise systems.

The SDK provides the implementation surface through which integration developers create adapters, provider bindings, capability implementations, event handlers, authentication mechanisms, error mappings, health checks, evidence acquisition, and reconciliation logic.

The SDK translates the conceptual Integration Model into a consistent engineering interface.

The SDK implements Noema’s canonical integration semantics. It does not redefine Intent, Trust, Action, Execution, Outcome, or enterprise business-state semantics.

⸻

2. Purpose

The SDK exists to make integrations:

* predictable
* capability-oriented
* contract-driven
* secure
* deterministic
* observable
* testable
* versioned
* replaceable
* reconcilable
* consistent across providers

The SDK should make the correct integration architecture the easiest architecture to implement.

⸻

3. Core Principle

The SDK is an implementation framework around Noema’s canonical integration semantics.

It must not redefine those semantics.

Canonical Noema Model
        │
        ▼
   Integration SDK
        │
        ├── Adapter
        ├── Binding
        ├── Authentication
        ├── Translation
        ├── Error Mapping
        ├── Events
        ├── Health
        ├── Evidence
        └── Reconciliation
        │
        ▼
Enterprise System / Provider

The SDK implements the integration boundary.

It does not own the Intent, Trust, or enterprise business-state models.

⸻

4. SDK Responsibilities

The SDK provides primitives for:

* defining integrations
* defining provider bindings
* implementing adapters
* declaring capabilities
* translating requests
* validating provider responses
* normalizing responses
* mapping errors
* handling events
* resolving credential references
* enforcing integration contracts
* reporting health
* acquiring evidence
* supporting State Reconciliation
* producing execution evidence
* instrumenting observability
* testing integrations
* managing lifecycle and versioning

The SDK may support both:

Evidence Acquisition
        │
        ▼
State Reconciliation

and:

Action Contract
        │
        ▼
Execution
        │
        ▼
Integration SDK

Not every SDK invocation is a consequential Action execution.

⸻

5. SDK Non-Responsibilities

The SDK must not provide mechanisms that allow integrations to independently:

* interpret human intent
* create canonical Intent Objects
* override Trust Engine decisions
* invent permissions
* mutate enterprise business truth
* bypass Action Contracts
* execute arbitrary model-generated operations
* expose credentials to models
* silently alter canonical capability semantics
* declare provider data authoritative without applicable enterprise authority
* convert uncertain observations into established facts
* establish an enterprise Outcome merely from provider transport success

These boundaries are architectural constraints.

⸻

6. Integration SDK Mental Model

An integration developer should conceptually implement:

Integration
    │
    ├── Provider
    ├── System
    ├── Environment
    ├── Scope
    ├── Capabilities
    ├── Bindings
    ├── Authentication
    ├── Events
    ├── Health
    ├── Evidence
    └── Reconciliation

The SDK supplies the primitives required to express these properties.

Current enterprise state remains subject to:

Enterprise Source
       │
       ▼
Observation
       │
       ▼
Hard Schema Validation / Admission
       │
       ▼
State Reconciliation
       │
       ▼
Reconciled Fact / Fact Status

The SDK supports this process but does not become the enterprise System of Record.

⸻

7. Canonical Integration Interface

Conceptually, an integration should expose:

Integration {
    identity()
    capabilities()
    validate()
    execute()
    normalize()
    mapError()
    events()
    health()
    evidence()
    reconcile()
}

This is a conceptual interface rather than a mandatory programming-language signature.

Concrete SDKs may adapt the interface to the host language.

execute() represents provider-facing execution where applicable.

evidence() and reconcile() represent non-executing integration functions that may be required to establish current state or verify an uncertain execution.

⸻

8. Integration Definition

An integration definition should declare:

* integration identity
* provider identity
* system identity
* environment
* supported capabilities
* adapter
* authentication requirements
* configuration schema
* scope
* version
* lifecycle metadata

The SDK should validate the definition before registration.

Unvalidated definitions are not canonical integration definitions.

⸻

9. Integration Identity

The SDK should require a stable integration identifier.

Conceptually:

integration_id
provider_id
system_id
environment
version

Identity must be deterministic and collision-resistant within the applicable Noema scope.

Integration identity does not establish authority over enterprise business state.

⸻

10. Provider Definition

The SDK should allow an integration to declare its provider.

A provider definition may include:

* provider identifier
* provider name
* system identifiers
* API surfaces
* protocol
* authentication mechanisms
* supported environments

Provider metadata must not become canonical business truth merely because it is declared by the SDK.

Provider identity establishes provenance and binding information, not business-state authority.

⸻

11. System Definition

The SDK must distinguish provider from system.

Provider
   │
   ├── System A
   ├── System B
   └── System C

An integration must bind to the specific system against which evidence acquisition, reconciliation, or execution occurs.

Where an enterprise identifies a System of Record for a claim, that authority must be represented explicitly rather than inferred from provider identity alone.

⸻

12. Environment Definition

The SDK should require explicit environment configuration.

Supported environments may include:

development
testing
staging
production

Environment must never be inferred from arbitrary runtime context when doing so could select the wrong enterprise system.

Environment selection is part of integration identity and execution scope.

⸻

13. Scope Definition

The SDK should allow integration scope to be declared explicitly.

Scope may include:

* tenant
* organization
* legal entity
* environment
* resource
* capability
* geographic boundary

An integration must not operate outside its declared scope.

Scope is a constraint, not an authorization decision.

⸻

14. Capability Declaration

The SDK should allow developers to declare canonical capabilities.

Example:

capability:
    id: retrieve_account_balance
    version: 1
    inputs:
        - account_id
    outputs:
        - balance
    authority:
        system_of_record: account_system

The declaration describes the semantic operation.

It must not merely expose the provider endpoint.

A capability declaration is canonical only after the applicable validation and registration process.

⸻

15. Capability Identity

Capability identity must be stable and semantic.

A capability identifier should describe what the enterprise can accomplish, not how a provider exposes it.

Prefer:

retrieve_account_balance

over:

GET_/v3/accounts/{id}/balance

The latter is an implementation detail.

Capability identity does not imply permission, authorization, availability, or Trust approval.

⸻

16. Capability Contract

Each SDK capability declaration should be associated with a contract defining:

* inputs
* outputs
* required context
* preconditions
* postconditions
* constraints
* authorization requirements
* error semantics
* idempotency semantics
* evidence requirements
* freshness requirements

The SDK should reject incomplete executable capability definitions where required contract information is missing.

The SDK must not weaken a canonical Action Contract merely because a provider cannot naturally represent one of its requirements.

⸻

17. Capability Binding

The SDK should allow a capability to be bound to a provider operation.

Canonical Capability
        │
        ▼
Capability Binding
        │
        ▼
Provider Operation

The binding should contain sufficient information for deterministic provider interaction.

A binding is implementation metadata. It does not redefine the semantic identity of the capability.

⸻

18. Provider Operation

A provider operation identifies the concrete operation used by the integration.

It may contain:

* endpoint
* operation name
* RPC method
* SQL statement reference
* SDK method
* queue destination
* event command
* provider-specific identifier

The provider operation is never itself the canonical capability.

Arbitrary provider operations must not become executable merely because the SDK can technically invoke them.

⸻

19. Adapter Interface

The SDK should provide a standard adapter interface.

Conceptually:

Adapter {
    validate()
    execute()
    normalizeResponse()
    mapError()
    health()
    evidence()
    reconcile()
}

The interface should be small enough to implement consistently and rich enough to preserve execution, evidence, and reconciliation semantics.

Adapters may support read-only evidence acquisition as well as side-effecting execution.

⸻

20. Request Context

Every consequential adapter execution should receive a structured execution context.

Conceptually:

ExecutionContext {
    execution_id
    intent_version
    action_id
    capability_id
    tenant_id
    organization_id
    environment
    resource_scope
    deadline
    idempotency_key
    authorization_context
    resolution_identity
}

Only fields necessary for the operation should be exposed.

The exact Intent version and resolved identity must be preserved for consequential execution.

The SDK must not receive raw model output as an authority source.

⸻

21. Intent Isolation

The SDK should not expose raw human intent to provider adapters unless explicitly required for an integration-specific, governed purpose.

Adapters should receive canonical execution data.

Source of Intent
    │
    ▼
Intent
    │
    ▼
Action
    │
    ▼
Capability
    │
    ▼
Action Contract
    │
    ▼
SDK Adapter

This prevents provider implementations from becoming intent interpreters.

The SDK does not resolve semantic ambiguity in human input.

⸻

22. Request Translation

The SDK should provide a standard translation boundary.

Canonical Request
      │
      ▼
translateRequest()
      │
      ▼
Provider Request

Translation may include:

* field mapping
* identifier transformation
* serialization
* parameter formatting
* protocol-specific metadata
* provider-specific options

Translation must preserve the semantics required by the canonical contract.

⸻

23. Response Normalization

The SDK should provide a standard normalization boundary.

Provider Response
      │
      ▼
normalizeResponse()
      │
      ▼
Canonical Response

Normalization must preserve material information required for:

* outcome classification
* evidence
* recovery
* reconciliation
* auditability

Normalization must not convert uncertainty into certainty.

⸻

24. Error Mapping

The SDK should provide explicit provider-to-canonical error mapping.

Conceptually:

Provider Error
      │
      ▼
mapError()
      │
      ▼
Canonical Error

Error mappings should be versioned and testable.

Provider error mapping must distinguish transport/technical conditions from business-state outcomes where possible.

⸻

25. Canonical Error Categories

The SDK should support canonical categories such as:

VALIDATION_ERROR
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
RATE_LIMITED
TIMEOUT
UNAVAILABLE
CONFLICT
DUPLICATE
PROVIDER_REJECTED
MALFORMED_RESPONSE
UNKNOWN_OUTCOME
INTEGRATION_ERROR

Provider-specific details may be preserved as metadata.

These are integration/execution error categories and must not be confused with Noema’s canonical Trust outcomes:

EXECUTE
CLARIFY
ESCALATE
REJECT

⸻

26. Unknown Outcome

The SDK must support explicit unknown execution outcomes.

For example:

execute()
   │
   └── timeout / transport loss
         │
         ▼
    UNKNOWN_OUTCOME

The SDK must not force every execution into success or failure.

An unknown execution state should normally trigger verification or State Reconciliation before retry, compensation, or final classification.

Unknown is an epistemic condition. It is not automatically a business failure.

⸻

27. Idempotency

The SDK should make idempotency explicit.

An adapter should receive an idempotency key where the capability supports one.

Execution
   │
   ▼
Idempotency Identity
   │
   ▼
Provider Request

The SDK must make it difficult to accidentally retry non-idempotent operations.

Provider idempotency guarantees must not be assumed unless established by the integration contract or provider semantics.

⸻

28. Retry Policy

The SDK may provide bounded technical retry primitives.

Retry configuration should specify:

* retryable errors
* maximum attempts
* backoff
* deadline
* idempotency requirements
* reconciliation requirements

Retries must not be used to hide unknown outcomes.

If the external operation may already have occurred, verification or State Reconciliation takes precedence over blind retry.

⸻

29. Deadline Propagation

Execution deadlines should propagate through the SDK.

Execution Deadline
       │
       ▼
SDK
       │
       ▼
Adapter
       │
       ▼
Provider

Adapters should not extend execution beyond the canonical deadline without explicit policy.

A deadline expiration is an execution condition and must not automatically establish business-state failure.

⸻

30. Authentication Interface

The SDK should provide an abstraction for authentication.

Conceptually:

AuthenticationProvider {
    authenticate()
    refresh()
    revoke()
}

Concrete implementations may support:

* OAuth
* API keys
* mTLS
* service accounts
* signed requests
* delegated credentials
* provider SDK authentication

Authentication establishes technical access. It does not itself establish business authorization or Trust approval.

⸻

31. Credential References

The SDK should operate on credential references rather than raw secrets wherever possible.

Credential Reference
       │
       ▼
Secure Credential Provider
       │
       ▼
Authentication
       │
       ▼
Provider

Secrets should remain isolated from model-visible data.

The model must not receive provider credentials merely because an integration requires them.

⸻

32. Credential Lifecycle

The SDK should support credential lifecycle operations such as:

* resolution
* refresh
* expiration detection
* rotation
* revocation
* failure handling

Credential lifecycle failures must remain distinguishable from provider business failures.

Credential state must not be exposed as ordinary execution context.

⸻

33. Authorization Context

The SDK may receive an authorization context representing authorization information established by the execution system.

It must not infer new permissions from:

* user language
* model output
* provider documentation
* capability existence
* endpoint availability

Technical authorization, policy authorization, and business authorization remain distinct concerns.

Provider authorization remains authoritative for provider-side access.

The SDK cannot grant enterprise permission merely by possessing credentials.

⸻

34. Configuration Schema

SDK integrations should declare configuration schemas.

Configuration may include:

* endpoints
* timeouts
* provider options
* event subscriptions
* feature flags
* rate limits
* pagination behavior
* reconciliation configuration
* capability bindings

Secrets should not be embedded directly in ordinary configuration objects.

⸻

35. Configuration Validation

The SDK should validate configuration before activation.

Validation should identify:

* missing required values
* invalid formats
* incompatible options
* unsupported environments
* invalid provider bindings
* unsafe configuration combinations
* invalid scopes
* incompatible capability contracts

Invalid configurations must not silently produce active integrations.

Configuration validation is part of the hard admission boundary for integration configuration.

⸻

36. Provider Constraints

The SDK should expose provider constraints as explicit configuration or capability metadata.

Examples:

rate_limit
max_page_size
max_concurrency
request_timeout
required_ordering
eventual_consistency
async_processing

Provider constraints that affect execution must be enforceable rather than merely documented.

⸻

37. Pagination Interface

The SDK should provide a consistent pagination abstraction.

Conceptually:

Page {
    items[]
    next_cursor
    has_more
}

Adapters must indicate whether a result is complete or partial.

The SDK must not silently collapse truncated provider results into complete results.

Partial data must retain semantics sufficient for downstream Context, Evidence, or State Reconciliation handling.

⸻

38. Freshness Metadata

SDK responses should preserve retrieval timing where relevant.

Conceptually:

Observation {
    value
    observed_at
    source
    authority
    freshness
}

Freshness must be interpreted relative to the claim, action, resource, and policy requiring it.

Recency alone does not establish authority.

⸻

39. Event Interface

The SDK should provide an event-handling interface.

Conceptually:

EventHandler {
    parse()
    normalize()
    verify()
    handle()
}

Events must retain provider provenance.

An event is an observation or message. It is not automatically canonical business state or an Outcome.

⸻

40. Event Verification

Incoming events should be verified where the provider supports verification mechanisms.

Verification may include:

* signatures
* certificates
* shared secrets
* trusted transport
* provider-issued identifiers

Unverified events must not automatically modify canonical state.

Successful authentication of an event does not automatically establish authority for every claim contained in the event.

⸻

41. Event Ordering

The SDK should preserve provider event ordering where ordering is semantically meaningful.

Where ordering cannot be guaranteed, events must carry sufficient metadata for deterministic handling or State Reconciliation.

Ordering must be scoped appropriately to the resource, stream, partition, aggregate, or provider semantics that define it.

⸻

42. Webhooks

The SDK may provide webhook primitives for providers that communicate through callbacks.

Webhook handlers should:

* authenticate requests
* verify signatures
* validate schemas
* normalize events
* preserve provider identifiers
* produce observable processing records

Webhook receipt must not automatically imply business-state truth.

Event absence must not automatically establish that an event did not occur.

⸻

43. Health Interface

The SDK should provide a standard health interface.

Conceptually:

Health {
    status
    checked_at
    latency
    reason
}

Health should distinguish:

* available
* degraded
* unavailable
* unknown

Health describes operational state, not capability existence, authorization, executability, or business outcome.

⸻

44. Capability Health

A provider may be partially healthy.

Therefore the SDK should support capability-level health where necessary.

Integration
   │
   ├── Capability A → healthy
   ├── Capability B → degraded
   └── Capability C → unavailable

A single integration health status must not conceal capability-specific failures when those differences matter.

Capability health is operational metadata and is not a Trust decision.

⸻

45. Reconciliation Interface

The SDK should provide a reconciliation interface for operations whose external state or outcome is uncertain.

Conceptually:

Reconciler {
    locate()
    verify()
    reconcile()
}

Reconciliation should use authoritative enterprise state whenever possible.

The SDK provides the mechanism for acquiring and normalizing observations. State Reconciliation determines the reconciled claim.

⸻

46. Reconciliation Scope

Reconciliation should be scoped to the specific execution and external resource.

It should avoid broad speculative queries.

Conceptually:

Execution
   │
   ├── Provider
   ├── Operation
   ├── External ID
   ├── Resource
   └── Time Window

This reduces the possibility of incorrectly associating unrelated external state with an execution.

A reconciliation result must preserve the identity and scope used to establish the association.

⸻

47. Evidence Interface

The SDK should provide mechanisms for producing execution and observation evidence.

Conceptually:

Evidence {
    source
    authority
    observed_at
    provider_reference
    scope
    data
}

Evidence must preserve provenance and authority.

Evidence is not automatically Fact Status.

A source may provide evidence that is UNVERIFIED, STALE, CONFLICTED, or UNKNOWN for a particular claim.

⸻

48. Provider References

Provider-generated identifiers should be preserved where they support:

* reconciliation
* auditability
* support investigation
* duplicate detection
* outcome verification

Examples include:

* request IDs
* transaction IDs
* operation IDs
* event IDs
* correlation IDs

Provider references are identifiers and provenance metadata. They do not independently establish business truth.

⸻

49. Observability Interface

The SDK should expose standardized instrumentation for:

* execution IDs
* Intent versions
* integration IDs
* capability IDs
* adapter versions
* provider requests
* latency
* retries
* errors
* provider correlation IDs
* reconciliation
* State Reconciliation results

Instrumentation must avoid exposing credentials or unnecessary sensitive payloads.

⸻

50. Logging

SDK logging should be structured.

Logs should include stable identifiers rather than relying on free-form textual descriptions.

Sensitive values must be redacted before logging.

The SDK should provide safe defaults for redaction.

Logs are operational evidence and must not silently become authoritative enterprise state.

⸻

51. Metrics

The SDK should support metrics such as:

* execution latency
* request count
* technical success rate
* technical failure rate
* unknown-outcome rate
* retry count
* provider error rate
* rate-limit events
* reconciliation rate
* health status

Metrics should distinguish technical integration behavior from business outcomes.

An HTTP success rate must not be represented as an enterprise business-success rate unless the relevant business semantics establish that relationship.

⸻

52. Tracing

The SDK should propagate trace context through provider requests where supported.

Tracing should establish:

Noema Execution
      │
      ▼
Integration
      │
      ▼
Adapter
      │
      ▼
Provider

Provider correlation identifiers should be linked to the Noema execution trace.

Tracing establishes causal observability, not business-state authority.

⸻

53. Testing SDK

The SDK should provide reusable testing primitives.

These may include:

* adapter test harnesses
* contract test fixtures
* mock providers
* error simulation
* timeout simulation
* event fixtures
* reconciliation fixtures
* schema validation
* credential tests
* State Reconciliation fixtures
* malformed-response tests

Testing primitives should validate integration semantics, not merely HTTP connectivity.

⸻

54. Contract Test Harness

The SDK should make it possible to verify:

Canonical Contract
       │
       ▼
Adapter
       │
       ▼
Provider Behavior

The test harness should detect mismatches in:

* request mapping
* response mapping
* error mapping
* idempotency
* timeout behavior
* postconditions
* event handling
* evidence preservation
* reconciliation behavior

Contract tests must test semantic preservation, not merely protocol compatibility.

⸻

55. Mock Provider

A mock provider should be able to simulate:

* successful responses
* validation failures
* authorization failures
* timeouts
* rate limiting
* malformed responses
* duplicate operations
* asynchronous completion
* provider outages
* stale responses
* conflicting observations
* delayed events
* missing events

This enables deterministic integration testing.

⸻

56. Deterministic Testing

Given the same:

* integration version
* adapter version
* capability contract
* execution context
* provider fixture
* relevant policy/configuration
* State Reconciliation inputs

the SDK test result should be deterministic.

External nondeterminism must be explicitly simulated rather than accidentally introduced.

⸻

57. SDK Registration

An integration package should register its capabilities and adapters with Noema through a controlled registration mechanism.

Conceptually:

SDK Package
    │
    ▼
Registration
    │
    ▼
Hard Validation / Admission
    │
    ▼
Registry
    │
    ▼
Activation

Registration must not automatically imply production authorization.

Registration is not Trust approval and does not grant enterprise permissions.

⸻

58. Registration Validation

Registration should validate:

* identity
* version
* capability declarations
* contracts
* provider bindings
* environment
* scope
* authentication configuration
* adapter implementation
* required handlers
* compatibility
* schema definitions
* lifecycle metadata

Invalid integrations must be rejected before activation.

Model-generated or externally discovered integration metadata must not bypass registration validation.

⸻

59. SDK Versioning

The SDK itself must be versioned independently from:

* integration version
* adapter version
* capability version
* provider API version
* contract versions

SDK Version
     ≠
Integration Version
     ≠
Capability Version
     ≠
Adapter Version
     ≠
Provider API Version

Compatibility must be explicit.

⸻

60. SDK Compatibility

SDK releases should define compatibility guarantees.

Breaking SDK changes should not silently invalidate active integrations.

Where required, multiple SDK versions may coexist during migration.

Compatibility does not permit an SDK release to silently alter the historical meaning of a canonical capability or contract.

⸻

61. Adapter Versioning

Adapters should be independently versioned.

An adapter change may involve:

* request translation
* response normalization
* authentication
* error mapping
* provider protocol
* operational behavior
* reconciliation behavior

A provider API change does not automatically imply a canonical capability change.

A semantic change to a capability or contract requires the appropriate canonical versioning process.

⸻

62. Integration Lifecycle Hooks

The SDK may provide lifecycle hooks such as:

onRegister()
onValidate()
onActivate()
onHealthChange()
onDisable()
onDeprecate()
onRetire()

Lifecycle hooks must remain bounded and observable.

They must not silently alter canonical execution semantics.

⸻

63. Activation

Activation should require successful validation.

Conceptually:

REGISTERED
     │
     ▼
VALIDATED
     │
     ▼
PROVISIONED / AUTHENTICATED
     │
     ▼
ACTIVE

Production authorization is an external governance condition and must not be implied merely by activation.

The SDK should prevent partially configured integrations from being activated.

⸻

64. Deactivation

The SDK should support controlled deactivation.

Deactivation should prevent new executions where appropriate while allowing the execution system to handle already-running executions according to policy.

Historical execution records must remain intact.

Deactivation must not mutate historical integration semantics.

⸻

65. Deprecation

Deprecation indicates that an integration or adapter should no longer be selected for new execution paths.

Deprecation must not erase historical definitions.

Existing executions must remain interpretable against the version that performed them.

⸻

66. Retirement

Retirement indicates that an integration is no longer executable.

Retirement must preserve:

* historical metadata
* versions
* execution evidence
* audit records
* provider references
* relevant reconciliation records

Retirement is not deletion of historical truth.

⸻

67. Security Defaults

The SDK should use secure defaults.

Examples include:

* TLS where applicable
* credential isolation
* request validation
* bounded timeouts
* safe logging
* least privilege
* tenant isolation
* secret redaction
* explicit environment selection
* explicit capability binding
* bounded resource consumption

Developers should have to explicitly opt into exceptional behavior.

Security controls must not depend on model compliance.

⸻

68. Data Sanitization

Provider responses should be sanitized before becoming broadly available to Noema components.

Sanitization may remove or restrict:

* credentials
* authentication material
* unnecessary personal data
* secrets
* provider-internal fields
* irrelevant payloads

The canonical response should contain only information required by the capability contract and execution journey.

Sanitization does not establish Fact Status or enterprise authority.

⸻

69. Input Validation

The SDK should validate canonical inputs before provider translation.

Validation may include:

* schema validation
* type validation
* required fields
* identifier formats
* bounds
* provider constraints
* capability-specific constraints
* scope constraints

Invalid input must fail deterministically before unnecessary provider calls.

The SDK must not use provider execution as a substitute for canonical input validation.

⸻

70. Output Validation

Provider responses should be validated before normalization is accepted.

Validation should detect:

* malformed payloads
* missing required fields
* invalid types
* unexpected schema changes
* inconsistent provider identifiers
* incompatible response versions

Malformed responses should not be silently normalized into valid-looking canonical data.

Schema validation establishes structural validity. It does not by itself establish business-state authority.

⸻

71. Protocol Abstraction

The SDK should abstract protocol mechanics behind common interfaces.

A developer should be able to implement:

RESTAdapter
GraphQLAdapter
GRPCAdapter
SOAPAdapter
SQLAdapter
MQAdapter
SDKAdapter

without changing the canonical capability model.

Protocol abstraction must not erase material differences in semantics such as delivery guarantees, transaction behavior, ordering, or idempotency.

⸻

72. Provider-Specific Extensions

The SDK may support provider-specific extensions.

Extensions must remain isolated from canonical semantics.

Canonical Capability
        │
        ▼
Standard SDK Interface
        │
        └── Provider Extension

Provider extensions must not become mandatory dependencies of the core Noema model.

Provider-specific behavior that affects canonical execution must be explicitly represented in the relevant binding, contract, or integration version.

⸻

73. Dependency Management

Integration packages should declare dependencies explicitly.

Dependencies may include:

* SDK version
* provider SDK
* protocol libraries
* cryptographic libraries
* serialization libraries

Dependency changes must be evaluated for security and compatibility impact.

Dependency changes must not silently alter canonical integration semantics.

⸻

74. Runtime Isolation

Integration execution should be isolated from unrelated integrations where practical.

A failure in one provider integration should not automatically compromise:

* another tenant
* another provider
* another integration
* the Noema control plane

Isolation may be implemented through processes, workers, containers, sandboxes, or equivalent mechanisms.

⸻

75. Resource Limits

The SDK should support bounded resource consumption.

Limits may apply to:

* execution time
* memory
* concurrency
* payload size
* retries
* pagination
* provider calls
* reconciliation scope

Unbounded integration behavior is incompatible with predictable execution.

⸻

76. Failure Containment

Integration failures must be contained within the integration boundary where possible.

An adapter failure should produce a canonical integration/execution condition rather than destabilizing the broader Intent or Trust system.

The SDK must not silently reinterpret an integration failure as a business Outcome.

⸻

77. SDK and Enterprise Graph

SDK definitions should provide enough metadata for registration in the Enterprise Graph.

The SDK may contribute:

Provider
System
Integration
Capability
Binding
Protocol
Environment
Scope
Version

The graph remains responsible for canonical structural representation and governance.

Graph registration does not by itself establish current enterprise business state.

⸻

78. SDK and Trust

The SDK provides technical execution facts, provider observations, and integration metadata.

It does not determine whether an Action should execute.

Trust Engine
     │
     │ deterministic decision
     ▼
Execution System
     │
     ▼
SDK
     │
     │ technical interaction
     ▼
Provider

The SDK must therefore expose sufficient metadata for Trust and Execution without becoming a Trust Engine itself.

Provider availability, credential validity, or endpoint accessibility may be inputs to Trust or execution eligibility, but they are not themselves Trust decisions.

⸻

79. SDK and Action Contracts

The SDK implements the provider-facing portion of an Action Contract.

It must respect:

* required inputs
* preconditions
* postconditions
* permissions
* constraints
* idempotency
* evidence requirements
* verification requirements

The SDK must never weaken the canonical contract to accommodate a provider.

Where a provider cannot satisfy the contract, the integration must expose that limitation rather than silently changing the contract.

⸻

80. SDK and Execution

The SDK operates within an execution lifecycle managed by Noema.

Admitted Intent
      │
      ▼
Resolved Action
      │
      ▼
Deterministic Trust
      │
      ▼
Action Contract
      │
      ▼
Execution Controller
      │
      ▼
SDK
      │
      ▼
Provider
      │
      ▼
Observation / Result
      │
      ▼
Verification / State Reconciliation
      │
      ▼
Outcome

The SDK contributes provider interaction state and evidence.

The execution layer owns canonical execution state.

Trust = EXECUTE does not mean that the provider operation succeeded.

⸻

81. SDK and Recovery

The SDK may expose provider-specific recovery primitives.

Examples:

* retry
* status lookup
* cancellation
* reconciliation
* continuation
* provider-specific recovery operation

Recovery decisions remain governed by the Execution Model, Action Contract, capability semantics, and applicable Trust conditions.

An SDK must not independently decide to compensate, retry indefinitely, or alter the original Intent.

⸻

82. SDK and Graph Evolution

Changes to SDK integration definitions may produce graph evolution events.

For example:

SDK Definition Change
        │
        ▼
Integration Change
        │
        ▼
Validation / Admission
        │
        ▼
Graph Evolution

The change must be validated before it changes canonical graph state.

Historical graph and integration versions must remain reconstructable.

⸻

83. SDK Package Structure

A conceptual integration package may look like:

integration/
├── manifest
├── capabilities/
│   ├── balance
│   ├── statements
│   └── transactions
├── adapter/
├── authentication/
├── events/
├── reconciliation/
├── errors/
├── tests/
└── README

The exact filesystem layout is implementation-specific.

The conceptual separation should remain.

⸻

84. Integration Manifest

An SDK integration manifest should declare enough metadata for deterministic registration.

Conceptually:

manifest {
    integration_id
    provider_id
    system_id
    environment
    version
    sdk_version
    capabilities[]
    protocols[]
    authentication[]
    scopes[]
}

The manifest should be machine-readable and validated before registration.

Manifest metadata is not automatically authoritative enterprise data.

⸻

85. Developer Experience

The SDK should make common integration operations concise.

A developer should not need to manually reimplement:

* correlation
* credential isolation
* retry accounting
* timeout propagation
* error normalization
* health reporting
* evidence structure
* tracing
* tenant scope checks
* schema validation
* reconciliation hooks

These should be standardized primitives.

⸻

86. Opinionated Defaults

The SDK should be intentionally opinionated about safety.

Defaults should favor:

* explicit scopes
* bounded execution
* secure authentication
* deterministic validation
* structured errors
* explicit idempotency
* safe retries
* evidence preservation
* observable execution
* tenant isolation
* verification before retry after uncertainty
* explicit environment selection

Flexibility should not come at the expense of execution correctness.

⸻

87. Escape Hatches

The SDK may expose low-level escape hatches for unusual provider behavior.

Such escape hatches must:

* be explicit
* be observable
* preserve canonical contracts
* preserve security controls
* preserve execution state
* require appropriate validation
* preserve auditability

An escape hatch must not become a general bypass around the Integration Model, Action Contracts, Trust, or execution controls.

⸻

88. No Arbitrary Execution

The SDK must not expose an interface such as:

execute(raw_model_output)

or:

execute(arbitrary_provider_operation)

Executable operations must resolve through:

Source of Intent
   ↓
Intent
   ↓
Action
   ↓
Capability
   ↓
Action Contract
   ↓
Trust
   ↓
Integration Binding
   ↓
SDK
   ↓
Provider

This is a fundamental security and determinism invariant.

The SDK may expose non-executing provider interaction for discovery, evidence acquisition, health, or reconciliation, but side-effecting operations must remain within the canonical execution path.

⸻

89. Canonical SDK Invariants

1. The SDK implements the Integration Model rather than redefining it.
2. The SDK must not interpret human intent.
3. The SDK must not make Trust decisions.
4. The SDK must not own enterprise business state.
5. Capabilities must be semantic rather than provider-endpoint identities.
6. Provider operations must remain implementation details.
7. Every executable provider operation must be associated with a validated capability binding.
8. Integration identity must be explicit.
9. Provider identity must be explicit.
10. System identity must be explicit.
11. Environment must be explicit.
12. Scope must be explicit.
13. Tenant boundaries must be enforced.
14. Credentials must remain isolated from model context.
15. Authentication must be explicit.
16. Authorization must never be inferred from capability existence.
17. Technical, policy, and business authorization must remain distinguishable.
18. Capability contracts must be explicit.
19. Canonical inputs must be schema-validated before provider execution.
20. Provider outputs must be schema-validated before normalization.
21. Response normalization must preserve material execution semantics.
22. Provider errors must map to canonical errors.
23. UNKNOWN_OUTCOME must be a supported result.
24. Timeouts must not automatically become business failures.
25. Retries must respect idempotency.
26. Retry behavior must be bounded.
27. Deadlines must propagate through the SDK.
28. Provider constraints must be represented when execution-relevant.
29. Pagination must preserve completeness semantics.
30. Freshness metadata must be preserved where relevant.
31. Provider events must retain provenance.
32. Unverified events must not silently modify canonical state.
33. Reconciliation must be available for uncertain outcomes.
34. State Reconciliation must remain distinct from raw integration retrieval.
35. Evidence must preserve provenance and authority.
36. Evidence must remain distinct from Fact Status.
37. Fact Status must not be inferred from model confidence.
38. Provider identifiers must be preserved where operationally relevant.
39. Logging must not expose secrets.
40. Observability must be standardized.
41. Sensitive payloads must be sanitized.
42. Integration registration must be validated through the hard admission boundary.
43. Activation must require successful validation.
44. Lifecycle transitions must be explicit.
45. Deprecation must preserve historical interpretability.
46. Retirement must preserve historical execution records.
47. SDK versioning must be independent from capability versioning.
48. Adapter versioning must be independent from provider API versioning.
49. Provider API changes must not automatically redefine capabilities.
50. Provider-specific extensions must not redefine canonical semantics.
51. Runtime failures must be contained where possible.
52. Resource consumption must be bounded.
53. Escape hatches must not bypass canonical contracts.
54. The SDK must not expose arbitrary provider execution.
55. Model-generated operations must never directly reach provider adapters.
56. SDK registration must not imply production authorization.
57. Failover must require semantic compatibility.
58. Multiple provider implementations must remain explicitly bound.
59. Integration health must remain distinct from capability existence.
60. Capability health may differ from integration health.
61. Cancellation must not imply provider cancellation without evidence.
62. Partial results must not be silently treated as complete.
63. Historical executions must remain interpretable against their integration versions.
64. SDK behavior must remain deterministic under equivalent execution conditions.
65. Integration changes must be observable.
66. Security controls must not depend solely on model compliance.
67. The SDK must preserve enterprise System-of-Record authority.
68. The SDK must not create shadow canonical business state.
69. The SDK must operate only within the validated Noema execution path for side-effecting operations.
70. Hard schema validation must precede admission of externally supplied integration data into canonical Noema processing.
71. Provider source identity must not be treated as authority for every claim.
72. Recency must not be treated as authority.
73. Current enterprise state must be established through appropriate State Reconciliation where required.
74. Unknown and conflicted observations must remain explicit.
75. The SDK must preserve the exact Intent version associated with consequential execution.
76. Resolved actor, action, target, resource, scope, and resolution identity must remain available where required for consequential execution.
77. EXECUTE from Trust must not be interpreted as provider success or business success.
78. Provider transport success must not automatically establish enterprise Outcome.
79. The SDK must not mutate an admitted Intent to accommodate provider behavior.
80. Historical integration semantics must remain reconstructable through explicit versioning and provenance.
81. Replay of provider events or observations must not create new business occurrences by default.
82. Operational Memory and integration logs must not become enterprise authority merely through persistence.
83. Read-only integration operations may still require Trust and governance when they expose consequential or protected information.
84. The SDK must not create authority from technical access.
85. The SDK must preserve causal links between Intent version, execution, provider interaction, observation, reconciliation, and Outcome.

⸻

90. Final Definition

The Integration SDK is the canonical developer-facing implementation layer through which Noema integrations are built, validated, registered, executed, observed, reconciled, tested, and evolved.

It provides standardized primitives for adapters, capability declarations, provider bindings, request translation, response validation and normalization, authentication, credential isolation, error mapping, event handling, health, evidence acquisition, State Reconciliation, observability, lifecycle management, and contract testing.

The SDK exists to make external enterprise systems executable through Noema without allowing provider-specific mechanics to redefine Noema’s canonical semantics.

Its fundamental side-effecting execution boundary is:

Source of Intent
      ↓
Canonical Intent
      ↓
Resolved Action
      ↓
Capability
      ↓
Action Contract
      ↓
Deterministic Trust Decision
      ↓
Integration Binding
      ↓
SDK Adapter
      ↓
Provider Operation
      ↓
Enterprise System
      ↓
Provider Observation / Event
      ↓
State Reconciliation / Verification
      ↓
Execution State
      ↓
Outcome

For non-executing integration interactions, the SDK may also provide:

Enterprise System / Provider
      ↓
Observation / Event
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Reconciled Fact / Fact Status
      ↓
Context / Trust / Verification

The Integration SDK therefore provides the controlled engineering surface between Noema’s deterministic execution model and the heterogeneous systems through which enterprise capabilities are realized.

Its boundary is not merely a protocol abstraction.

It is the implementation boundary that preserves the distinction between provider mechanics and Noema semantics, between technical access and authority, between observation and fact, between execution and outcome, and between uncertainty and established enterprise state.