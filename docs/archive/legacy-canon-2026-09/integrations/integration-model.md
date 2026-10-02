> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Integration Model

Status: Foundational
Version: 0.1
Domain: Integrations
Canonical Path: integrations/integration-model.md

⸻

1. Definition

The Integration Model defines how Noema represents, governs, validates, and operates boundaries between its canonical execution model and external enterprise systems.

An Integration is a governed boundary through which Noema may:

* discover and validate enterprise capabilities
* bind canonical capabilities to concrete implementations
* acquire enterprise observations and evidence
* execute validated operations
* receive provider events
* support State Reconciliation
* preserve provenance and execution evidence
* manage provider-specific authentication and protocol semantics
* detect and govern integration drift

An Integration may therefore support both knowledge acquisition and consequential execution.

The distinction is important:

Evidence / State Acquisition
        ↓
Integration
        ↓
Provider Observation
        ↓
Schema Validation / Admission
        ↓
State Reconciliation

and:

Admitted Intent
        ↓
Resolution
        ↓
Deterministic Trust
        ↓
Action Contract
        ↓
Execution
        ↓
Integration
        ↓
Enterprise System

The Integration Model defines the structural and semantic rules governing both boundaries.

⸻

2. Purpose

The Integration Model exists to ensure that integrations remain:

* explicit
* governed
* versioned
* observable
* replaceable
* capability-oriented
* authority-preserving
* deterministic after probabilistic interpretation
* isolated from model reasoning
* bounded by contracts
* compatible with State Reconciliation
* consistent across enterprise providers

An integration must allow Noema to interact with an enterprise environment without making provider implementation details part of Noema’s canonical intent semantics.

⸻

3. Core Principle

Noema integrates with enterprise capabilities, systems, and evidence surfaces rather than treating APIs as the primary semantic abstraction.

An API is an implementation surface.

A capability is the semantic operation Noema needs to understand.

A system is the enterprise component that owns or exposes resources, capabilities, and potentially authoritative business state.

Therefore:

Enterprise System
       │
       ▼
Provider API / Protocol
       │
       ▼
Integration Adapter
       │
       ▼
Capability Binding
       │
       ▼
Canonical Capability
       │
       ▼
Action Contract
       │
       ▼
Execution

For state acquisition:

Enterprise System / Event / Provider
       │
       ▼
Integration Adapter
       │
       ▼
Validated Observation
       │
       ▼
State Reconciliation
       │
       ▼
Fact Status / Evidence / Context

The integration layer translates between these representations without changing their canonical meaning or creating enterprise authority.

⸻

4. Integration Boundary

The integration boundary separates Noema’s canonical execution domain from external enterprise systems.

┌───────────────────────────────────────────────┐
│                    Noema                      │
│                                               │
│ Intent → Context → Trust → Action Contract   │
│                    │                          │
└────────────────────┼──────────────────────────┘
                     │
              Integration Boundary
                     │
┌────────────────────┼──────────────────────────┐
│                    ▼                          │
│             Integration Layer                 │
│                                               │
│ Adapter → Binding → Translation → Provider    │
│                    │                          │
└────────────────────┼──────────────────────────┘
                     │
                     ▼
            Enterprise System

The boundary must be explicit rather than implicit.

Noema must not allow a model, arbitrary application code, or unregistered provider operation to cross this boundary directly.

⸻

5. Integration Is Not Intent

An integration must not interpret human or agent intent as canonical Noema Intent.

Intent interpretation belongs to the Intent and Context layers.

Source of Intent
       │
       ▼
Candidate Interpretation
       │
       ▼
Hard Schema Validation / Admission
       │
       ▼
Admitted Intent
       │
       ▼
Resolution
       │
       ▼
Trust
       │
       ▼
Action Contract
       │
       ▼
Integration

An integration may provide evidence used during interpretation or resolution, but retrieved provider data must not silently become canonical Intent.

An integration must never become a secondary intent interpreter.

⸻

6. Integration Is Not Trust

Integrations do not determine whether a consequential operation should be permitted.

Trust evaluation belongs to the deterministic Trust boundary.

An adapter may enforce technical requirements and report provider conditions, but it must not independently decide that an otherwise rejected or escalated Action should execute.

Trust
  │
  ├── EXECUTE ───────► Integration
  ├── CLARIFY
  ├── ESCALATE
  └── REJECT

EXECUTE means the applicable Trust conditions permit the Action to proceed.

It does not mean the enterprise operation will succeed.

⸻

7. Integration Is Not Business State

An integration does not own the business state of the external system.

For example, if an integration retrieves an account balance:

Enterprise System
     │
     │ authoritative business state
     ▼
Integration
     │
     │ normalized observation
     ▼
Noema
     │
     ▼
State Reconciliation

Noema may record the observation and execution evidence.

It must not silently become the authoritative owner of the balance.

Enterprise systems remain authoritative for their designated business facts.

⸻

8. Integration and System of Record

Every integration path should identify the enterprise system responsible for relevant business truth where that authority is known.

Conceptually:

Capability
    │
    ├── provider
    ├── system
    ├── resource
    └── system_of_record

The system of record is authority for a defined claim or domain, not necessarily every piece of data emitted by the system.

An integration may retrieve, mutate, or observe business state, but the authoritative source remains the designated enterprise authority.

⸻

9. Integration Components

The Integration Model consists of related concepts:

Integration
├── Adapter
├── Provider Binding
├── Capability Binding
├── Protocol
├── Authentication
├── Credentials
├── Configuration
├── Contract
├── Request Translation
├── Response Normalization
├── Error Mapping
├── Event Handling
├── Reconciliation
├── Health State
├── Version
└── Lifecycle State

These concepts must remain distinguishable.

⸻

10. Integration

An Integration represents a governed connection between Noema and an external enterprise environment.

An integration identifies:

* external provider
* target enterprise system
* environment
* tenant or organizational scope
* supported protocols
* supported capabilities
* adapter implementation
* authentication mechanism
* configuration
* lifecycle state
* semantic and implementation versions
* operational health
* applicable bindings

An integration is therefore broader than an adapter.

⸻

11. Adapter

An Adapter implements the technical translation between Noema’s canonical operations or observation requests and an external provider’s interface.

Canonical Operation / Observation Request
        │
        ▼
      Adapter
        │
        ▼
Provider Operation / Observation Surface

The adapter is responsible for protocol and provider mechanics.

It is not responsible for deciding what the user meant, what the enterprise business state means, or whether a consequential Action should execute.

⸻

12. Provider

A Provider is the external organization, platform, application, or service exposing capabilities or information through an integration surface.

Examples may include:

* banking platforms
* CRM systems
* ERP systems
* identity providers
* payment processors
* internal enterprise services

Provider identity must be explicit.

⸻

13. Provider System

A provider may expose multiple systems or environments.

Therefore:

Provider
   │
   ├── System A
   ├── System B
   └── System C

An integration must identify the specific system against which operations or observations are performed.

Provider identity alone is insufficient to establish authority or execution eligibility.

⸻

14. Provider Binding

A Provider Binding connects a canonical capability to a provider-specific implementation.

Canonical Capability
        │
        ▼
Provider Binding
        │
        ▼
Provider Operation

The binding defines how the semantic capability is realized by a specific enterprise system.

A binding must not redefine the canonical capability’s semantics.

⸻

15. Capability Binding

A capability binding must specify at minimum:

* canonical capability
* capability version
* provider
* system
* adapter
* provider operation
* protocol
* integration version
* environment
* scope
* operational constraints
* validity

The binding is an implementation relationship, not a replacement for the capability definition.

⸻

16. One Capability, Multiple Providers

A canonical capability may have multiple provider implementations.

                 ┌── Provider A
                 │
Capability ──────┼── Provider B
                 │
                 └── Provider C

The semantic capability may remain stable while implementations vary.

Multiple implementations do not automatically imply semantic equivalence or automatic failover.

⸻

17. One Provider, Multiple Capabilities

A provider may expose many capabilities.

Provider
   │
   ├── retrieve_account_balance
   ├── retrieve_statement
   ├── search_transactions
   └── create_complaint

The integration model must represent these capabilities independently.

A provider connection must not be treated as one monolithic capability.

⸻

18. Protocol Independence

Integrations must abstract over provider protocols.

Supported protocols may include:

* REST
* GraphQL
* gRPC
* SOAP
* SQL
* RPC
* message queues
* event streams
* provider SDKs

The protocol is an implementation characteristic, not the canonical capability identity.

Direct database access is permitted only when explicitly represented as a governed enterprise capability and Action Contract. An adapter must not use arbitrary SQL as an unbounded execution mechanism.

⸻

19. API Independence

Noema must not define enterprise capabilities purely in terms of API endpoints.

For example:

GET /accounts/{id}/balance

is not itself the canonical capability.

The canonical capability may be:

retrieve_account_balance

The endpoint is one provider-specific realization of that capability.

⸻

20. Request Translation

The integration layer translates canonical execution requests into provider-specific requests.

Canonical Request
      │
      ▼
Schema / Contract Validation
      │
      ▼
Translation
      │
      ▼
Provider Request

Translation may include:

* field mapping
* identifier mapping
* parameter transformation
* serialization
* protocol-specific metadata
* pagination parameters
* authentication headers
* provider-specific formatting

Translation must preserve canonical semantics.

⸻

21. Response Normalization

Provider responses must be translated into canonical Noema representations without discarding material information.

Provider Response
       │
       ▼
Schema Validation / Admission
       │
       ▼
Adapter
       │
       ▼
Canonical Observation / Execution Result

Normalization must preserve information required for:

* execution state
* evidence
* error interpretation
* reconciliation
* auditability
* recovery
* provenance

A normalized response is not automatically an authoritative fact or business outcome.

⸻

22. Hard Schema Validation and Admission

External integration data must cross a hard validation boundary before it becomes eligible for canonical use.

Potential inputs include:

* provider responses
* provider events
* API schemas
* discovery metadata
* configuration
* adapter metadata
* provider errors
* model-generated mappings
* model-generated capability candidates

The general boundary is:

External / Model-Derived Input
          │
          ▼
Hard Schema Validation
          │
          ▼
Semantic / Scope / Provenance Validation
          │
          ▼
Canonical Admission

Successful schema validation establishes structural validity.

It does not, by itself, establish enterprise authority or current business truth.

Persistence also does not establish authority.

⸻

23. Lossless Execution Semantics

Where information affects execution correctness, recovery, reconciliation, or auditability, integration translation must be semantically lossless.

Provider-specific details may be abstracted away.

Material facts may not be discarded.

For example:

Provider:
"Request accepted, processing asynchronously"

must not become:

Noema:
"Execution succeeded"

The asynchronous uncertainty must remain represented.

⸻

24. Error Mapping

Provider errors must be translated into canonical execution semantics.

Provider Error
      │
      ▼
Error Mapping
      │
      ▼
Canonical Failure / Uncertainty

Error mapping must distinguish at least:

* validation failure
* authentication failure
* authorization failure
* rate limiting
* timeout
* unavailable system
* provider rejection
* conflict
* duplicate request
* unknown outcome
* malformed response
* integration failure

Unknown must remain distinct from established failure.

⸻

25. Unknown Outcome

A timeout or missing provider response does not automatically establish that execution failed.

The integration model must support:

UNKNOWN

when the external system’s final state cannot be established.

The correct path may be:

Provider Interaction
       ↓
Timeout / Missing Response
       ↓
UNKNOWN
       ↓
State Reconciliation
       ↓
Current Authoritative Observation
       ↓
Resolved Execution / Outcome State

Noema must not convert communication uncertainty into business failure without sufficient evidence.

⸻

26. Idempotency

Integrations must explicitly represent idempotency semantics where applicable.

Action Instance
      │
      ▼
Execution Identity / Idempotency Key
      │
      ▼
Provider Operation

The idempotency identity must be tied to the semantic Action and its execution scope rather than treated as an arbitrary string.

An integration must not blindly retry a non-idempotent operation merely because a response was not received.

The idempotency contract and provider guarantees must be explicit.

⸻

27. Technical Retries

Integrations may perform bounded technical retries when explicitly permitted.

Retries must be:

* policy-bounded
* observable
* deterministic under equivalent inputs
* compatible with idempotency
* compatible with provider semantics
* bounded by deadlines and attempt limits

Technical retry is not a Trust decision.

An adapter must never use retries to conceal uncertainty.

After an UNKNOWN condition, reconciliation should establish whether a retry is safe before a new attempt is dispatched.

⸻

28. Authentication

Authentication is an integration concern.

The integration model must represent:

* authentication mechanism
* credential reference
* credential scope
* credential lifecycle
* authentication status
* required provider identity

Authentication material must remain outside model-generated context.

Authentication establishes a technical relationship with a provider. It does not by itself establish Noema Trust or business authorization.

⸻

29. Credentials

Credentials must be referenced rather than exposed as ordinary execution data.

Action
   │
   ▼
Integration
   │
   ▼
Credential Reference
   │
   ▼
Secure Credential Store

Models must never receive raw secrets merely because an integration requires them.

Credentials must not be stored in:

* Intent Objects
* capability definitions
* Action Contracts
* graph metadata
* ordinary model context
* general logs
* Operational Memory

except through controlled secret references where explicitly required.

⸻

30. Authorization

Provider authorization and Noema Trust are related but distinct.

Technical Authorization
        │
        ▼
Noema Trust / Policy Evaluation
        │
        ▼
Action Contract
        │
        ▼
Provider Authorization
        │
        ▼
Enterprise Operation

Technical authorization, policy authorization, and business authorization must not be conflated.

A Noema Trust decision does not grant permissions that the enterprise system has not granted.

Conversely, successful provider authentication does not establish that a requested Action satisfies Noema’s Trust conditions.

⸻

31. Tenant Isolation

Integrations must preserve tenant and organizational boundaries.

An integration instance must explicitly identify its applicable scope.

Integration
   │
   ├── Tenant
   ├── Organization
   ├── Environment
   └── System

Credentials, capabilities, permissions, evidence, and execution contexts must not cross tenant boundaries implicitly.

⸻

32. Environment Isolation

Enterprise systems commonly expose multiple environments:

* development
* testing
* staging
* production

The integration model must represent environment explicitly.

A production capability must never be selected merely because a development binding exists.

Environment is part of execution meaning and scope.

⸻

33. Scope

Integration scope may include:

* tenant
* organization
* legal entity
* system
* resource
* environment
* geographic boundary
* capability
* time period

Scope is part of integration meaning.

A technically valid integration outside the applicable scope is not a valid execution path.

⸻

34. Configuration

Integration configuration may include:

* endpoint information
* protocol configuration
* timeouts
* rate limits
* feature flags
* provider-specific options
* pagination behavior
* event subscriptions
* environment settings

Configuration must be versioned where changes can affect execution semantics, security, authority, capability availability, or reconciliation behavior.

⸻

35. Capability Discovery

Integrations may discover capabilities from:

* API specifications
* schemas
* documentation
* provider metadata
* workflow definitions
* administrative configuration
* observed enterprise behavior
* human configuration

Discovery produces candidates.

Discovery alone does not establish canonical capability truth or executable authority.

⸻

36. Capability Validation

Discovered capabilities must be validated before becoming canonical and executable.

Validation may establish:

* existence
* semantic meaning
* inputs
* outputs
* constraints
* permissions
* provider binding
* authority basis
* environment
* scope
* operational behavior
* contract compatibility

Only validated capabilities may participate in canonical execution.

Capability validation does not grant enterprise permission.

⸻

37. Model-Assisted Discovery

Models may assist integration discovery.

For example, a model may infer:

Possible Capability:
retrieve_account_balance

from provider documentation.

The model’s inference is a proposal.

Model
  ↓
Candidate Capability
  ↓
Hard Schema Validation
  ↓
Deterministic Semantic Validation
  ↓
Enterprise Evidence / Authority
  ↓
Canonical Registration

A model must never directly create executable capability authority.

⸻

38. Integration Registry

Noema should maintain a governed registry of integration definitions.

The registry should be able to answer:

* which integrations exist
* which systems they connect to
* which capabilities they provide
* which adapters implement them
* which environments they target
* which versions are active
* what their operational status is
* what their scope is
* what evidence and provenance support their registration

The registry is not a replacement for enterprise business systems.

⸻

39. Integration Identity

Every integration must have a stable identity.

Conceptually:

integration_id
provider_id
system_id
environment
tenant_scope
version

Identity must remain stable across ordinary implementation or configuration changes unless the integration’s semantic identity itself changes.

⸻

40. Versioning

Integration versions must be distinct from other semantic and implementation versions.

Capability Version
        ≠
Integration Version
        ≠
Adapter Version
        ≠
Provider API Version
        ≠
Contract Version
        ≠
Policy Version
        ≠
Graph Version

A provider API can change without changing the semantic capability.

An adapter can change without changing the provider binding’s semantic meaning.

Historical execution must retain the versions required to reconstruct the integration path used at the time.

⸻

41. Lifecycle

Integrations have an explicit lifecycle.

DISCOVERED
    │
    ▼
REGISTERED
    │
    ▼
VALIDATED
    │
    ▼
ACTIVE
    │
    ├── DEGRADED
    │
    ├── DISABLED
    │
    ▼
DEPRECATED
    │
    ▼
RETIRED

Lifecycle transitions must be governed and observable.

A lifecycle transition must not silently rewrite historical execution semantics.

⸻

42. Health

Integration health describes operational availability and technical condition.

Health does not determine whether a capability exists.

These are distinct:

Capability Exists
        ≠
Integration Available

Health may include separate dimensions for:

* adapter process health
* provider connectivity
* credential validity
* configuration validity
* capability availability
* event ingestion health
* reconciliation health

⸻

43. Availability

Availability describes whether an integration path can currently communicate with its provider or perform its supported technical operation.

Potential states include:

* AVAILABLE
* DEGRADED
* UNAVAILABLE
* UNKNOWN

Availability may affect planning and execution without changing the underlying capability definition.

Availability is not:

* permission
* Trust
* business authorization
* business success
* enterprise business state

⸻

44. Capability Eligibility

A capability may exist but be ineligible for a particular execution.

Eligibility may depend on:

* tenant
* actor
* resolved target
* permissions
* policy
* resource
* environment
* integration health
* temporal constraints
* required context
* provider state
* capability constraints

Capability existence alone is insufficient for execution.

⸻

45. Integration Selection

When multiple integrations can realize the same capability, selection must be governed.

Selection may consider:

* scope
* authority
* environment
* capability compatibility
* permissions
* provider status
* version compatibility
* policy
* operational health
* execution constraints
* idempotency guarantees
* freshness requirements

The model may propose a candidate.

Final selection must be deterministic under established canonical rules.

The integration layer must not allow model preference to override policy, scope, authority, or capability compatibility.

⸻

46. Failover

Multiple provider bindings do not automatically imply failover.

Failover must preserve:

* canonical capability semantics
* Action identity
* actor and target
* authorization
* authority
* tenant scope
* resource identity
* idempotency
* consistency requirements
* policy
* environment semantics
* outcome semantics

A different provider must not be substituted merely because it is available.

An alternative binding must be explicitly registered or otherwise governed by canonical integration configuration.

⸻

47. Semantic Equivalence

Two provider operations may implement the same canonical capability only if their semantics are sufficiently equivalent.

Provider A Operation ─┐
                      ├── Canonical Capability
Provider B Operation ─┘

Equivalence may require matching:

* inputs
* outputs
* resource semantics
* authority
* freshness
* preconditions
* postconditions
* failure semantics
* security constraints
* idempotency
* consistency behavior

Equivalent naming or similar API structure is insufficient.

⸻

48. Integration Contracts

Every consequential executable integration path must be governed by applicable contracts defining:

* expected inputs
* expected outputs
* preconditions
* postconditions
* errors
* timeout semantics
* idempotency
* authorization requirements
* evidence requirements
* version compatibility
* provider constraints

The Action Contract remains the canonical executable boundary.

The integration must not invent or weaken contract semantics at runtime.

⸻

49. Preconditions

Provider-specific preconditions may supplement canonical capability and Action Contract preconditions.

For example:

Canonical:
account identifier required
Provider:
account identifier + branch code required

The integration may enforce the provider-specific requirement.

It must not weaken canonical preconditions.

Where a provider precondition depends on current enterprise state, the relevant state may need State Reconciliation before the operation can be considered executable.

⸻

50. Postconditions

Provider responses must be evaluated against expected postconditions.

For read operations, this may mean establishing that:

* requested resource was identified
* requested data was retrieved
* response corresponds to requested scope
* freshness requirements were satisfied
* result completeness is known

For write operations, provider acknowledgement alone may not establish the final business postcondition.

Final business state may require verification against the enterprise system of record.

⸻

51. Events

Integrations may receive provider events representing:

* state changes
* asynchronous completion
* failures
* notifications
* reconciliation signals
* workflow transitions

Events must be normalized into Noema’s canonical Event model while preserving provider provenance.

A provider event is an observation or evidence source; it is not automatically a business-state transition.

⸻

52. Event Authority

A provider event does not automatically become canonical business truth.

Its authority depends on:

* source
* system of record
* event semantics
* scope
* temporal validity
* provenance
* reconciliation requirements

Therefore:

Provider Reported Event
        ≠
Canonical Business State

unless the event and its source are authoritative for the relevant claim.

Event absence is also not proof that an event or business operation did not occur.

⸻

53. Reconciliation

Integration is a major mechanism for State Reconciliation, but the adapter itself does not establish reconciled enterprise truth.

The canonical pattern is:

Enterprise System of Record
        │
        ▼
Provider Observation
        │
        ▼
Hard Schema Validation / Admission
        │
        ▼
State Reconciliation
        │
        ▼
Reconciled Facts / Fact Status / Evidence
        │
        ▼
Context / Trust / Verification

Reconciliation is particularly important after:

* timeouts
* connection failures
* asynchronous operations
* duplicate-request ambiguity
* provider outages
* partial responses
* conflicting observations
* stale cached state
* event ordering problems

The integration supplies observations and reconciliation access. It does not independently declare the final business truth.

⸻

54. Fact Status

Integration observations must remain distinct from Fact Status.

Canonical Fact Status values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

An adapter response is evidence or an observation.

It may support a Fact Status after validation and reconciliation, but the raw response must not itself be treated as a Fact Status.

Model confidence must never substitute for Fact Status.

⸻

55. Evidence

Integration responses may produce evidence supporting:

* execution outcomes
* business observations
* capability validation
* provider state
* reconciliation
* audit records

Evidence must preserve:

* source
* authority
* provenance
* observed time
* effective time where available
* validity
* scope
* version
* relevant provider identifiers

Evidence is not automatically equivalent to truth.

Source identity does not by itself establish authority.

⸻

56. Observability

Every integration execution should be observable through stable correlation identifiers.

Observability should support:

* request tracing
* provider correlation IDs
* execution IDs
* latency
* retries
* failures
* response classification
* adapter version
* integration version
* provider operation
* reconciliation activity
* provider request IDs

Observability must not require exposing credentials or unnecessary sensitive business data.

⸻

57. Auditability

Integration activity must produce sufficient records to reconstruct what occurred.

For consequential operations, Noema should be able to establish:

Source of Intent
       ↓
Intent Version
       ↓
Resolved Actor / Action / Target
       ↓
Trust Decision
       ↓
Action Contract
       ↓
Capability / Integration Binding
       ↓
Adapter / Provider
       ↓
Execution Attempt
       ↓
Provider Observation
       ↓
State Reconciliation / Verification
       ↓
Outcome

The exact semantic and implementation versions relevant to each stage must be retained.

For non-executing evidence acquisition, the audit chain may begin at the observation request rather than an Intent.

⸻

58. Data Minimization

Integrations should transmit only the information required for the operation.

Provider responses should not automatically become model context.

Sensitive fields must be filtered according to:

* purpose
* permissions
* policy
* tenant scope
* data classification
* actor scope

Integration boundaries are therefore also data-control boundaries.

⸻

59. Sensitive Data

Credentials, authentication material, secrets, tokens, and unnecessary sensitive business data must remain outside ordinary model reasoning paths.

The integration layer must enforce the separation between:

Execution Secret
      ≠
Model Context

No model should receive raw provider credentials merely because it can propose or inspect an integration.

⸻

60. Provider Constraints

Integrations must explicitly represent provider constraints such as:

* rate limits
* request size limits
* pagination
* concurrency limits
* maintenance windows
* required ordering
* supported fields
* eventual consistency
* asynchronous processing
* provider-specific idempotency requirements

Provider constraints become executable constraints when they affect the canonical action path.

⸻

61. Rate Limiting

Rate limits are operational constraints, not intent semantics.

An integration may queue, delay, or reject operations when provider limits require it.

Such behavior must remain observable.

A rate limit must not be represented as a business rejection unless enterprise semantics explicitly define it that way.

⸻

62. Timeouts

Timeout behavior must preserve uncertainty.

Request
  │
  ▼
Provider
  │
  ├── Response ───────► Known Provider Observation
  │
  └── Timeout ────────► Outcome May Be UNKNOWN

A timeout is an execution condition.

It is not automatically:

* business failure
* provider rejection
* successful completion

Where the provider operation may have committed despite the timeout, State Reconciliation is required before retry or compensation.

⸻

63. Cancellation

Cancellation must be explicitly modeled where provider protocols support it.

Noema cancellation does not necessarily imply that the provider operation has stopped.

Therefore:

Noema Cancelled
        ≠
Provider Operation Cancelled

The distinction must be preserved until externally verified.

Committed external effects remain part of execution history even when cancellation occurs later.

⸻

64. Concurrency

Integrations must respect provider and capability concurrency requirements.

Where operations have ordering dependencies, the integration must preserve required ordering.

Parallel execution must never be introduced merely as an optimization when doing so can alter semantics.

Concurrency controls are implementation/execution constraints, not permission or Trust decisions.

⸻

65. Pagination

Provider pagination must be normalized into canonical retrieval semantics.

The integration should distinguish:

* complete result
* partial result
* paginated result
* continuation available
* continuation exhausted
* provider truncation

A truncated provider response must not be silently presented as a complete enterprise result.

⸻

66. Freshness

Integration results may have freshness requirements.

A response must carry sufficient temporal information to determine whether it satisfies the applicable claim or capability freshness requirements.

Retrieved / Observed At
        │
        ▼
Freshness Evaluation
        │
        ├── Sufficient
        └── Insufficient

Freshness is claim-specific.

Recency does not establish authority.

⸻

67. Caching

Caching is an implementation optimization subject to canonical freshness and authority requirements.

Noema must distinguish:

Cached Observation
        ≠
Current Enterprise State

A cached value may be used only when its freshness, authority, scope, and purpose satisfy the applicable contract.

⸻

68. Drift

Integration drift occurs when provider implementation or observed behavior changes relative to Noema’s known integration model.

Examples include:

* changed API schemas
* removed endpoints
* changed response semantics
* changed authentication
* changed error codes
* changed permissions
* changed capability behavior
* changed idempotency semantics
* changed event semantics

Drift must be detected and governed.

⸻

69. Drift Detection

Drift detection may use:

* schema comparison
* contract testing
* provider metadata
* failed executions
* response anomalies
* documentation changes
* reconciliation
* administrative signals
* event anomalies

Detected drift must not silently alter canonical capability semantics.

Material drift may require disabling an integration binding until deterministic validation establishes compatibility.

⸻

70. Integration Evolution

Integration changes must be represented as governed evolution events.

A change may affect:

* adapter version
* provider binding
* protocol
* authentication
* configuration
* capability availability
* operational constraints
* event semantics
* reconciliation behavior

Historical executions must remain interpretable against the integration versions used at the time.

⸻

71. Breaking Changes

Breaking integration changes include changes that invalidate existing execution assumptions.

Examples:

* incompatible provider schema
* removed operation
* changed authentication requirements
* incompatible response semantics
* changed idempotency behavior
* changed authorization semantics
* changed event meaning
* changed resource identity semantics

Breaking changes require explicit validation before affected execution paths are reactivated.

⸻

72. Backward Compatibility

Where possible, integrations should support backward-compatible evolution.

Multiple versions may coexist:

Capability v1
   │
   ├── Adapter v1
   └── Provider API v1
Capability v1
   │
   └── Adapter v2
          │
          └── Provider API v2

Provider evolution does not automatically require semantic capability evolution.

Compatibility must be established semantically rather than inferred from technical compatibility alone.

⸻

73. Integration Replacement

An integration may be replaced without changing the canonical capability when semantic compatibility is preserved.

Capability
    │
    ├── Old Binding ──► Provider A
    │
    └── New Binding ──► Provider B

Replacement must preserve required:

* capability semantics
* authority
* scope
* resource semantics
* contract guarantees
* security properties
* idempotency guarantees
* outcome semantics

Historical executions retain their original binding references.

⸻

74. Integration Failure

Integration failure is distinct from business failure.

Integration Failure
       │
       ├── Provider unavailable
       ├── Network failure
       ├── Authentication failure
       ├── Adapter failure
       └── Protocol failure

The canonical execution state must preserve this distinction.

A provider communication failure may result in UNKNOWN rather than FAILED when the external business state cannot be established.

⸻

75. Recovery

Recovery must be governed by the applicable capability, Action Contract, execution policy, and current reconciled state.

Possible recovery actions include:

* retry
* wait
* reconcile
* use an approved equivalent binding
* request human intervention
* terminate as failed
* preserve unknown state

Recovery must never rely on an unverified assumption about external business state.

A retry after UNKNOWN requires appropriate reconciliation and idempotency analysis.

⸻

76. Integration and Enterprise Graph

Integrations are represented in the Enterprise Graph.

Conceptually:

Enterprise System
        │
        ▼
   Integration
        │
        ▼
      Adapter
        │
        ▼
 Capability Binding
        │
        ▼
   Capability

The graph provides structural context required to determine whether an integration path exists and how it relates to enterprise systems and capabilities.

Graph connectivity does not itself establish authorization, current business truth, or Trust.

⸻

77. Integration and Enterprise Action Graph

The Enterprise Action Graph represents the executable-oriented projection of enterprise reality.

Integrations provide the bridge between graph-defined capabilities and concrete provider operations.

EAG Capability
      │
      ▼
Action Contract
      │
      ▼
Integration Binding
      │
      ▼
Adapter
      │
      ▼
Enterprise System

The integration participates in the executable graph without becoming the graph or replacing Trust.

⸻

78. Integration and Action

An Action represents a concrete semantic operation selected for execution.

The integration realizes the Action through its validated capability binding.

Intent
  ↓
Action
  ↓
Capability
  ↓
Integration Binding
  ↓
Provider Operation

The integration must not create arbitrary Actions independently.

The exact intent_version, resolved actor, resolved Action, exact target/resource, scope, and resolution identity must remain associated with consequential execution.

⸻

79. Integration and Trust Engine

The Trust Engine establishes whether a resolved Action may proceed.

The integration provides technical facts and availability information that may be relevant to that decision, but does not make the Trust decision.

Trust Decision
      │
      ▼
Integration Eligibility
      │
      ▼
Provider Execution

Technical availability, provider authorization, and business authorization remain distinct from Trust.

⸻

80. Integration and Execution

The execution layer owns the lifecycle of an execution.

The integration performs the provider-facing operation within that lifecycle.

Execution
   │
   ▼
Integration
   │
   ▼
Provider
   │
   ▼
Observation / Event
   │
   ▼
Verification / Reconciliation
   │
   ▼
Outcome

Integration state must not replace execution state.

⸻

81. Integration and Outcome

The integration produces observations about what happened externally.

The execution and verification layers determine the canonical execution and outcome semantics from those observations and applicable contracts.

The enterprise system remains authoritative for resulting business state.

This distinction allows Noema to preserve:

* provider response
* normalized response
* evidence
* uncertainty
* execution status
* reconciliation state
* business outcome observations

without conflating them.

Trust EXECUTE is not a success outcome.

⸻

82. Integration State Model

An integration may be represented conceptually as:

Integration {
    id
    provider
    system
    environment
    scope
    adapter
    capabilities[]
    bindings[]
    authentication
    configuration
    version
    health
    lifecycle
    provenance
}

This is a conceptual model rather than an implementation schema.

⸻

83. Integration Execution Model

A canonical integration execution can be represented as:

Admitted Intent
      │
      ▼
Resolution
      │
      ▼
Deterministic Trust
      │
      ▼
Capability / Integration Selection
      │
      ▼
Action Contract Validation
      │
      ▼
Credential Resolution
      │
      ▼
Request Translation
      │
      ▼
Provider Execution
      │
      ▼
Response / Error / Timeout / Event
      │
      ▼
Schema Validation / Normalization
      │
      ▼
Execution State + Evidence
      │
      ▼
Verification / State Reconciliation
      │
      ▼
Outcome

For evidence acquisition:

Evidence Request
      │
      ▼
Integration
      │
      ▼
Provider Observation
      │
      ▼
Schema Validation / Admission
      │
      ▼
State Reconciliation
      │
      ▼
Fact Status / Evidence / Context

Every transition must have defined semantics.

⸻

84. Determinism

After probabilistic intent interpretation, integration behavior must be deterministic under the same applicable canonical inputs.

These may include:

* canonical Action
* exact Intent version
* resolved actor and target
* graph version
* capability version
* integration version
* adapter version
* provider binding
* policy
* permission state
* execution context
* provider state
* relevant contract versions

The integration layer must not introduce uncontrolled model-based decisions.

Provider nondeterminism may still exist in the external environment; Noema must represent that uncertainty rather than conceal it.

⸻

85. Model Boundary

Models may assist with:

* capability discovery
* provider documentation interpretation
* schema interpretation
* mapping proposals
* anomaly investigation
* evidence summarization

Models must not directly control:

* credential selection
* authorization bypass
* provider selection without governance
* contract mutation
* Trust decisions
* arbitrary provider operations
* canonical business-state classification
* Action Contract execution
* direct database or network access

The model proposes.

The deterministic integration system validates and executes within registered boundaries.

⸻

86. Integration Security

Integration security must include:

* credential isolation
* tenant isolation
* least privilege
* secret rotation
* secure transport
* authorization enforcement
* request validation
* response validation and sanitization
* sensitive-data controls
* auditability
* provider trust configuration
* environment isolation
* capability-bound execution

Security controls must be enforced independently of model behavior.

No model output should be capable of directly creating a provider request outside a validated capability and Action Contract path.

⸻

87. Testing

Integrations must be testable independently and contractually.

Testing should include:

* adapter unit tests
* provider contract tests
* schema compatibility tests
* authentication tests
* authorization tests
* error mapping tests
* timeout tests
* idempotency tests
* reconciliation tests
* event tests
* pagination tests
* freshness tests
* tenant-isolation tests
* scope tests
* drift tests
* negative-path tests

A successful mock response is insufficient evidence that an integration is production-valid.

⸻

88. Contract Testing

Contract tests should verify that provider behavior continues to satisfy assumptions encoded by the integration and Action Contracts.

Contract failures must prevent unsafe integration activation where the failure affects execution correctness, security, authority, reconciliation, or outcome interpretation.

Contract testing must distinguish:

* transport compatibility
* schema compatibility
* semantic capability compatibility
* execution compatibility

These are not interchangeable.

⸻

89. Integration Registration

An integration should become executable only after required registration, schema validation, semantic validation, scope validation, security validation, and capability binding validation.

Conceptually:

Discovered
   │
   ▼
Registered
   │
   ▼
Validated
   │
   ▼
Governed
   │
   ▼
Active

Registration is not itself a Trust decision or business authorization.

Registration establishes that Noema may use the integration within its declared scope and governance conditions.

⸻

90. Integration Observability Model

Integration observability should provide a complete operational chain:

Execution ID
    │
    ├── Intent Version
    ├── Action
    ├── Capability
    ├── Integration
    ├── Adapter Version
    ├── Provider Operation
    ├── Request ID
    ├── Provider Correlation ID
    ├── Response
    ├── Error
    ├── Retry History
    ├── Observation
    └── Reconciliation

This allows failures and uncertain states to be investigated without reconstructing execution from ambiguous logs.

⸻

91. Version and Provenance Dimensions

Integration records must preserve distinct version and temporal dimensions where relevant.

These may include:

* Intent Object version
* Action version
* Capability version
* Action Contract version
* Trust Contract version
* Policy version
* Graph version
* Capability Registry version
* Integration version
* Adapter version
* provider API/schema version
* system version
* resource/business-state version
* integration mapping version

Temporal fields may include:

* occurred_at
* effective_at
* observed_at
* received_at
* recorded_at
* decision_at
* execution_at
* completed_at

These dimensions must not be collapsed into one generic version or timestamp.

⸻

92. Replay

Provider events, observations, and integration records may be replayed for:

* investigation
* reconciliation
* audit
* testing
* historical reconstruction

Replay must be non-executing by default.

Replaying an event or provider observation must not create a new business occurrence or execute a new Action unless an explicit, separately authorized execution is initiated.

Historical decisions remain historical. Current reevaluation is a distinct operation.

⸻

93. Operational Memory

Operational Memory may retain:

* integration interactions
* provider observations
* execution attempts
* failures
* reconciliation history
* drift events
* adapter versions
* provider identifiers
* recovery history

Operational Memory is not:

* enterprise business-state authority
* a permission source
* a Trust authority
* a replacement for a system of record
* generic model memory

Historical records may support future reasoning, but they do not become authoritative merely because they are stored in Noema.

⸻

94. Read Operations

Integration reads are not automatically consequence-free.

A read operation may expose:

* protected customer data
* financial information
* identity attributes
* privileged configuration
* security-sensitive system information
* organizational relationships

Therefore read operations may still require:

* resolved identity
* scope validation
* permission evaluation
* policy evaluation
* Trust
* auditability
* data minimization

Read-only does not mean ungoverned.

⸻

95. Write Operations

Write integrations create or modify enterprise state or cause externally visible side effects.

They require stronger guarantees around:

* authorization
* policy
* confirmation where required
* idempotency
* auditability
* reconciliation
* verification
* recovery

Capability or integration registration alone does not authorize execution.

For the Noema Phase 1 fintech POC, permitted writes remain limited to governed non-monetary operations such as complaint, escalation, or case-state updates. Money movement is outside the POC execution boundary.

⸻

96. Integration and State Reconciliation

Integration paths must expose sufficient capabilities for Noema to reconcile state when direct execution evidence is incomplete.

A reconciliation path should identify:

* authoritative system
* resource
* claim being reconciled
* observation method
* scope
* temporal validity
* relevant resource version
* evidence returned
* limitations
* reconciliation result

The adapter supplies access to the observation surface.

State Reconciliation determines the reconciled state.

⸻

97. Integration and Canonicality

Canonicality must be scoped.

A capability, binding, observation, or configuration record may be canonical for a defined:

* tenant
* organization
* system
* domain
* resource type
* claim
* environment
* temporal scope

A provider response is not authoritative merely because it comes from an integration.

Likewise:

Most Recent
      ≠
Most Authoritative

Authority is claim-specific.

⸻

98. Causal Audit Boundary

For consequential operations, the integration layer must preserve causal linkage between:

Source of Intent
      ↓
Hard Schema Validation / Admission
      ↓
Intent Version
      ↓
Resolved Actor / Action / Target
      ↓
State Reconciliation / Context
      ↓
Trust Decision
      ↓
Capability / Integration Binding
      ↓
Action Contract
      ↓
Execution Attempt
      ↓
Provider Observation
      ↓
Verification / State Reconciliation
      ↓
Outcome

This provides causal traceability without requiring disclosure of private model chain-of-thought.

⸻

99. Canonical Integration Invariants

The following invariants are mandatory:

1. Integrations are explicit boundaries between Noema and external enterprise environments.
2. Integrations do not interpret canonical Intent.
3. Integrations do not make Trust decisions.
4. Integrations do not own enterprise business state.
5. Enterprise systems remain authoritative for their designated business facts.
6. Capabilities are semantic abstractions above provider APIs.
7. Provider APIs are implementation surfaces, not canonical capability identities.
8. Every executable capability must have a validated provider binding.
9. Provider bindings must identify their applicable scope.
10. Environment must be explicit.
11. Tenant boundaries must never be implicit.
12. Integration credentials must remain outside ordinary model context.
13. Authorization must never be inferred from capability existence.
14. Capability existence must remain distinct from capability availability.
15. Availability must remain distinct from authorization and Trust.
16. Provider errors must map into canonical execution semantics.
17. Unknown outcomes must remain distinguishable from established failures.
18. Timeouts must not automatically imply business failure.
19. Retries must respect idempotency semantics.
20. Integrations must not silently retry unsafe operations.
21. Response normalization must preserve material uncertainty.
22. Material execution evidence must not be discarded during translation.
23. Provider events must retain provenance.
24. Provider observations must not automatically become canonical business truth.
25. Integration versions must remain distinct from capability versions.
26. Adapter versions must remain distinct from provider API versions.
27. Provider API changes must not automatically change capability semantics.
28. Integration selection must be governed.
29. Failover must require semantic compatibility.
30. Provider substitution must respect authority and scope.
31. Model-generated integration mappings are proposals, not canonical truth.
32. Canonical integration state must be deterministically validated.
33. Integration lifecycle transitions must be explicit.
34. Integration drift must be detectable.
35. Breaking changes must not silently activate.
36. Historical executions must remain interpretable.
37. Integration cancellation must not imply provider cancellation without evidence.
38. Partial provider results must not be presented as complete without qualification.
39. Cached results must respect freshness requirements.
40. Integration configuration that affects execution semantics must be versioned.
41. Reconciliation must be available where external outcome cannot be established.
42. Integration failure must remain distinct from business failure.
43. Integration state must not replace execution state.
44. Integration adapters must not bypass Action Contracts.
45. Integration adapters must not invent permissions.
46. Integration adapters must not mutate canonical capability semantics.
47. Integration security controls must not depend solely on model compliance.
48. Provider-specific mechanics must remain isolated from canonical Intent semantics.
49. Integration activity must be observable and auditable.
50. Integration boundaries must preserve enterprise authority.
51. The same canonical capability may have multiple provider implementations.
52. Multiple provider implementations must not imply automatic failover.
53. Semantic equivalence must be established before substituting implementations.
54. Integration execution must remain within the validated execution graph.
55. No provider response may be treated as stronger evidence than its authority permits.
56. Unknown must remain a first-class integration condition.
57. Integration evolution must preserve historical meaning.
58. Integration changes must be governed by evidence and validation.
59. The integration layer may translate semantics but must not redefine them.
60. Noema must execute only through integrations whose capability, scope, contract, authorization, and operational state are sufficiently established.
61. External provider data must cross the applicable hard schema validation/admission boundary before canonical use.
62. Persistence of integration data does not establish authority.
63. Fact Status must remain distinct from Evidence.
64. Fact Status must not be derived from model confidence alone.
65. State Reconciliation is distinct from adapter translation.
66. State Reconciliation must be used where current enterprise state cannot otherwise be established with sufficient authority and freshness.
67. Source identity must not be conflated with authority.
68. Recency must not be treated as authority.
69. Exact Intent Object version must be preserved for consequential integration operations.
70. Admitted Intent versions are immutable; material changes require a new version with explicit lineage.
71. Resolved actor, Action, exact target/resource, and scope must be preserved for consequential operations.
72. Trust outcomes remain exactly EXECUTE, CLARIFY, ESCALATE, and REJECT.
73. Integration availability and lifecycle states are not Trust outcomes.
74. Trust EXECUTE does not establish execution success.
75. Provider acknowledgement does not automatically establish business Outcome.
76. Outcome does not replace enterprise Business State.
77. Technical authorization, policy authorization, and business authorization remain distinct.
78. Capability registration does not grant permission.
79. Adapter invocation must occur through registered capability and contract boundaries for consequential execution.
80. Models must not receive integration credentials or obtain direct provider execution access.
81. Arbitrary HTTP, SQL, or provider operations are not capabilities merely because an adapter can technically invoke them.
82. Idempotency identity must be tied to the semantic Action and execution scope.
83. UNKNOWN execution state must not trigger blind retry.
84. Retry after UNKNOWN requires appropriate reconciliation and idempotency analysis.
85. Alternative integration bindings must preserve semantic capability and Action requirements.
86. Provider events and observations are not automatically business-state transitions.
87. Event absence must not be treated as proof of non-occurrence.
88. Partial results must retain their completeness status.
89. Freshness requirements are claim- and operation-specific.
90. Read operations may be consequential and require Trust.
91. Write operations require stronger execution, verification, and recovery controls.
92. Replay is non-executing by default.
93. Operational Memory is historical execution knowledge, not enterprise authority.
94. Version dimensions must remain distinguishable across integration, adapter, provider, capability, contract, policy, graph, and system semantics.
95. Integration configuration changes affecting semantics must be versioned and auditable.
96. Historical integration paths must remain reconstructable.
97. Security boundaries must be enforced independently of model compliance.
98. The integration layer must not silently weaken canonical constraints during provider translation.
99. Provider-specific mechanics must never redefine canonical enterprise capability semantics.
100. Integration selection, failover, and substitution must be deterministic under established governance rules.
101. Integration registration is a governance boundary, not authorization by itself.
102. Canonical graph connectivity does not itself establish current business truth or permission.
103. Noema must not maintain a shadow system of record for enterprise business state through integration projections.
104. Integration observations may support Fact Status only after applicable validation and reconciliation.
105. Consequential integration activity must preserve causal provenance from Intent through Trust, Contract, Execution, Observation, Reconciliation, and Outcome.

⸻

100. Final Definition

The Integration Model is Noema’s canonical model for representing and governing the boundary between canonical enterprise capabilities and their concrete external implementations and observation surfaces.

It defines how Noema discovers, validates, binds, authenticates, invokes, observes, normalizes, reconciles, versions, monitors, and evolves integrations while preserving:

* capability semantics
* enterprise authority
* execution determinism
* security
* provenance
* scope
* freshness
* uncertainty
* auditability
* historical reconstructability

An integration is therefore not merely a connector or API client.

It is a governed boundary through which Noema may acquire enterprise observations and evidence or invoke a validated consequential operation.

The integration layer translates canonical semantics into concrete provider protocols and translates provider observations back into structured evidence and execution state.

It does not interpret canonical Intent, grant authority, make Trust decisions, or become the source of enterprise business truth.

The canonical architecture is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolve Actor / Action / Target
      ↓
Context / State Reconciliation
      ↓
Deterministic Trust
      ↓
Enterprise Action Graph / Capability Selection
      ↓
Plan
      ↓
Action Contract
      ↓
Execution Controller
      ↓
Integration
      ↓
Enterprise System / Provider
      ↓
Observation / Event
      ↓
State Reconciliation / Verification
      ↓
Outcome

For evidence acquisition, integrations may participate earlier as controlled observation surfaces:

Enterprise System / Provider
      ↓
Integration
      ↓
Observation
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Fact Status / Evidence / Context

The core invariant is:

Integration translates and connects. It does not decide, authorize, or redefine. Enterprise systems remain authoritative for enterprise business truth.