> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Enterprise Capabilities

Status: Foundational
Version: 0.1
Domain: Integrations
Canonical Path: integrations/enterprise-capabilities.md

⸻

1. Definition

An Enterprise Capability is a canonical, scoped, versioned representation of an operation that an enterprise environment can perform through one or more connected systems, integrations, or workflows.

A capability describes what the enterprise can accomplish, independent of the particular API, provider, protocol, or implementation used to accomplish it.

Conceptually:

Enterprise Reality
       ↓
Enterprise Capability
       ↓
Provider / System Binding
       ↓
Integration Adapter
       ↓
Executable Operation

A capability represents enterprise ability. It does not itself establish authorization, Trust, execution, or business-state truth.

⸻

2. Purpose

Enterprise Capabilities provide the semantic bridge between enterprise reality and executable Noema actions.

They allow Noema to reason about:

* what an enterprise can do
* which systems can perform it
* which resources are involved
* what inputs are required
* what outputs are produced
* what permissions may be required
* what policies constrain it
* what contracts govern execution
* which integrations implement it
* what conditions must hold
* what failure semantics apply
* what recovery characteristics exist
* what evidence establishes the capability
* within which scope and environment it is available

⸻

3. Capability Principle

A capability represents ability, not authorization.

Capability  = What can be done
Permission  = Who may do it
Policy      = Under what rules it may be done
Action      = What operation is instantiated for a request
Execution   = What was actually attempted
Outcome     = What the execution and verification established

These concepts must remain distinct.

Capability registration does not grant permission.

Capability availability does not imply executability.

Capability execution does not establish business-state truth.

⸻

4. Capability as an Enterprise Abstraction

Enterprise APIs expose implementation mechanisms.

Capabilities expose enterprise meaning.

For example:

Provider API:
GET /accounts/{id}/balance
Canonical Capability:
retrieve_account_balance

The endpoint is an implementation detail.

The capability is the semantic abstraction Noema reasons about.

⸻

5. Capability Independence

A capability should not be defined by:

* an HTTP method
* an API endpoint
* a provider name
* an SDK method
* a database query
* a message topic
* a GraphQL operation
* a transport protocol

Those may implement the capability but do not define its semantic identity.

⸻

6. Capability Identity

Every enterprise capability must have a stable identity.

Conceptually:

capability_id

The identity should remain stable across compatible implementation changes unless the semantic meaning of the capability changes.

For example:

retrieve_account_balance

may move from Provider A to Provider B without becoming a different capability if its canonical semantics remain compatible.

⸻

7. Capability Name

Capability names should describe enterprise semantics rather than implementation details.

Preferred:

retrieve_account_balance
search_transactions
retrieve_statement
create_complaint

Avoid:

call_get_balance_api
execute_graphql_query
invoke_provider_x_balance_endpoint

Names must describe what is accomplished, not how it is implemented.

⸻

8. Capability Description

Every capability must have a precise semantic description.

A capability description should establish, where applicable:

* purpose
* supported operation
* required inputs
* output semantics
* affected resources
* preconditions
* postconditions
* constraints
* authorization requirements
* supported environments
* availability semantics
* failure semantics
* recovery characteristics
* implementation bindings

Ambiguous capability descriptions must not become executable authority.

⸻

9. Capability Scope

Capabilities exist within a defined enterprise scope.

Scope may include:

* tenant
* organization
* legal entity
* business domain
* system
* environment
* region
* resource type
* resource instance

A capability available to one tenant does not automatically exist for another tenant.

Scope is part of capability meaning, not merely deployment metadata.

⸻

10. Capability Lifecycle

Capabilities have a controlled lifecycle:

DISCOVERED
    ↓
PROPOSED
    ↓
VALIDATING
    ↓
REGISTERED
    ↓
ACTIVE
    ↓
DEPRECATED
    ↓
RETIRED

Lifecycle state determines whether a capability may participate in discovery, planning, or execution.

Lifecycle state does not itself establish authorization.

⸻

11. Discovery

Capabilities may be discovered from:

* enterprise APIs
* API schemas
* provider documentation
* integration metadata
* workflows
* configuration
* enterprise administrators
* existing systems
* validated operational observations

Discovery creates a candidate.

It does not automatically create canonical capability truth or executable authority.

⸻

12. Capability Proposal

A discovered capability may initially exist as a proposal.

Conceptually:

Discovery
   ↓
Capability Proposal
   ↓
Evidence
   ↓
Hard Schema Validation / Admission
   ↓
Semantic Validation
   ↓
Canonical Capability

The proposal must remain distinguishable from an established capability.

⸻

13. Model-Generated Capabilities

A model may identify potential capabilities from documentation, schemas, workflows, or other enterprise information.

Model output is only a proposal.

Model
  ↓
Candidate Capability
  ↓
Hard Schema Validation / Admission
  ↓
Evidence / Provenance / Authority Evaluation
  ↓
Deterministic Registration
  ↓
Canonical Capability

A model must never directly create executable capability authority.

Model confidence is not capability authority, Fact Status, or proof that an enterprise operation exists.

⸻

14. Hard Schema Validation and Admission

Capability definitions and bindings must cross a deterministic schema validation and admission boundary before they can participate as canonical execution metadata.

Admission should validate, as applicable:

* capability structure
* semantic fields
* identity
* scope
* lifecycle state
* version
* binding structure
* implementation reference
* required constraints
* provenance
* source metadata
* compatibility metadata

Unvalidated provider documentation, schemas, configuration, model output, or discovered metadata must not be treated as canonical capability semantics.

Persistence does not establish authority.

⸻

15. Capability Validation

Validation determines whether a proposed capability corresponds to a real, bounded, and governable enterprise operation.

Validation may consider:

* enterprise source
* API schema
* documentation
* configuration
* provider behavior
* integration tests
* workflow evidence
* administrator confirmation
* capability verification

Validation must establish semantic meaning, not merely technical connectivity.

A successful connection to an endpoint does not establish that the endpoint implements the claimed capability.

⸻

16. Capability Authority

A capability should have an identifiable authoritative basis for the claims made about it.

Possible authorities include:

* enterprise system
* enterprise API
* configuration registry
* approved workflow definition
* integration administrator
* governed capability registry

Authority is claim-specific.

A source that is authoritative for one property is not automatically authoritative for every capability property.

⸻

17. Capability Evidence

Capability evidence establishes why Noema believes a capability exists or has particular semantics.

Evidence may include:

* API definition
* OpenAPI schema
* GraphQL schema
* provider documentation
* successful capability verification
* workflow definition
* configuration
* enterprise confirmation
* integration test results

Evidence must retain provenance, scope, temporal validity, and source information.

Evidence is not itself business-state truth.

⸻

18. Capability Fact Status

Fact Status is distinct from Evidence, Context, Business State, and Outcome.

Where a capability-related claim is evaluated, its Fact Status may be:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example, an old API schema may be evidence that a capability previously existed while the current capability status is STALE.

A model’s confidence score must not be converted into Fact Status.

Capability lifecycle status and Fact Status are separate dimensions.

⸻

19. Capability Provenance

Capability provenance should identify:

source
source_type
observed_at
effective_at
scope
authority
version
validation_method

This allows Noema to answer:

Why does Noema believe this capability exists, and within what scope?

⸻

20. Capability Version

Capabilities are versioned when their semantic contract changes.

For example:

retrieve_statement v1
retrieve_statement v2

A version change may result from changes to:

* required inputs
* output semantics
* supported resources
* preconditions
* postconditions
* constraints
* failure semantics
* security requirements
* idempotency semantics

A provider API version change alone does not necessarily require a capability version change.

⸻

21. Capability Version Versus Implementation Version

Capability semantics and implementation versions are separate.

A provider may move from API v1 to API v2 while preserving the same capability semantics.

Conversely, a capability may require a new semantic version while using the same underlying provider API.

Historical executions must retain the exact capability version used by the execution.

⸻

22. Capability Versus Provider API

The relationship is:

Enterprise Capability
        │
        ├── implemented by ──> Provider API A
        │
        ├── implemented by ──> Provider API B
        │
        └── implemented by ──> Internal System

Multiple technical implementations may satisfy the same semantic capability.

Semantic compatibility must be established before implementations are treated as interchangeable.

⸻

23. Capability Versus Adapter

The distinction is:

Capability
= What can be accomplished
Adapter
= How Noema communicates with a particular implementation

A capability may have multiple adapters.

An adapter may implement multiple capabilities.

The relationship must be explicitly registered.

⸻

24. Capability Binding

A capability binding connects a canonical capability to an implementation.

Conceptually:

Capability
    │
    │ binding
    ▼
Integration
    │
    ▼
Adapter
    │
    ▼
Provider Operation

The binding must preserve:

* capability identity
* capability version
* adapter identity
* adapter version
* system
* environment
* scope
* provider operation
* status
* validity

⸻

25. Multiple Implementations

An enterprise may expose the same capability through multiple systems.

For example:

retrieve_customer_profile
        │
        ├── CRM Adapter
        ├── Customer Data Platform Adapter
        └── Internal Customer Service Adapter

These implementations are not automatically interchangeable.

Semantic compatibility must be established for the relevant:

* inputs
* outputs
* resource semantics
* authority
* freshness
* preconditions
* postconditions
* failure semantics
* security constraints

⸻

26. Capability Equivalence

Two operations are equivalent only when they satisfy the same canonical capability semantics within the relevant scope.

Matching API names or similar responses are insufficient evidence of equivalence.

Equivalence may require matching:

* input semantics
* output semantics
* resource semantics
* freshness guarantees
* authority
* preconditions
* postconditions
* failure semantics
* security constraints
* tenant scope
* temporal semantics

⸻

27. Capability Inputs

Every capability must define its required inputs.

Inputs may include:

* resource identifier
* actor context
* time range
* filters
* pagination
* query parameters
* execution context
* correlation information

Input definitions must specify type, semantics, requiredness, scope, and constraints.

A capability must not rely on unspecified implicit inputs for consequential execution.

⸻

28. Capability Outputs

Every capability should define its expected output semantics.

Outputs may include:

* resource
* collection
* status
* summary
* reference
* evidence
* provider metadata

Output semantics must distinguish between:

successful result
empty result
partial result
unknown result
failure

A provider response must not be treated as a canonical Outcome merely because it has a successful transport status.

⸻

29. Resource Requirements

Capabilities should identify which resource types they operate on.

For example:

retrieve_account_balance
    ↓
Account

and:

search_transactions
    ↓
Account
    ↓
Transaction

Resource references must remain scoped and resolvable.

For consequential operations, the final target Resource must be explicitly resolved before execution.

⸻

30. Preconditions

A capability may require preconditions before execution.

Examples:

* actor identified
* resource resolved
* required permission exists
* required context resolved
* current state satisfies required condition
* system available
* integration active
* policy conditions satisfied

Preconditions must be explicit.

A capability definition does not itself establish that its preconditions are currently satisfied.

⸻

31. Postconditions

A capability may define postconditions describing what should be established after execution.

For read operations:

requested information retrieved

For side-effecting operations:

enterprise operation accepted
resource updated
case created

Postconditions are expected semantic conditions.

They are not actual Outcome or Business State.

Verification and the authoritative enterprise system establish what actually happened.

⸻

32. Capability Constraints

Capabilities may have constraints such as:

* resource scope
* maximum query range
* supported currencies
* supported regions
* required fields
* rate limits
* operating hours
* environment
* tenant configuration
* data-access restrictions

Constraints are part of capability semantics where they determine whether the capability can support a particular operation.

⸻

33. Permission Requirements

A capability may require one or more permissions.

Conceptually:

Actor
  ↓
Identity
  ↓
Permission
  ↓
Capability

The capability states what permission may be required.

The enterprise authorization system determines whether the resolved actor actually possesses the required permission.

A capability does not create, grant, or infer permission.

⸻

34. Authorization Distinctions

Capability requirements must remain distinct from authorization decisions.

Noema may encounter:

Technical Authorization
Policy Authorization
Business Authorization

Technical authorization concerns whether a system or integration may technically invoke an operation.

Policy authorization concerns whether applicable policy permits the operation.

Business authorization concerns whether the enterprise’s business rules permit the operation for the relevant actor, resource, and state.

A capability may declare requirements for these boundaries but must not collapse them into capability existence.

⸻

35. Policy Requirements

Policies may constrain capability execution.

For example:

Capability
     ↓
Policy
     ↓
Approval Required

Capability existence does not override policy.

Policy evaluation remains a Trust concern rather than a capability-definition shortcut.

⸻

36. Context Requirements

A capability may require context to become executable.

Examples:

which account?
which customer?
which organization?
which environment?
which date range?

An unresolved required context means the capability cannot yet form a complete executable path.

Noema must not guess materially consequential context.

⸻

37. Capability Availability

Capability existence and capability availability are distinct.

Capability exists
        ≠
Capability is currently available

Availability may depend on:

* provider health
* integration status
* credentials
* environment
* configuration
* feature flags
* system maintenance
* provider restrictions

Availability is an operational property and may itself be UNKNOWN.

⸻

38. Capability Existence, Availability, Eligibility, and Executability

These concepts must remain separate.

Existence
= Does the enterprise define or possess this ability?
Availability
= Is an implementation currently available?
Eligibility
= Can this capability participate in this particular request?
Executability
= Is there a currently valid path through Trust, Action Contract,
  integration, and runtime conditions?

A capability may exist while being unavailable.

It may be available while ineligible for a particular actor or resource.

It may be eligible while still requiring final runtime validation.

⸻

39. Capability Eligibility

Eligibility determines whether a capability can participate in a particular execution path.

It may depend on:

* resolved actor
* identity
* resolved resource
* scope
* permission
* policy
* context
* environment
* availability
* current state
* capability constraints

Eligibility does not itself constitute a Trust decision.

⸻

40. Capability Selection

Capability selection maps a resolved Intent and execution requirement to one or more enterprise capabilities.

Conceptually:

Admitted Intent
      ↓
Intent / Context Resolution
      ↓
Candidate Capabilities
      ↓
Graph / Registry Constraints
      ↓
Semantic Validation
      ↓
Eligible Capability Set
      ↓
Trust / Planning Constraints
      ↓
Selected Executable Path

The model may propose candidates, but canonical capability selection must be constrained by registered enterprise capabilities, authoritative context, applicable policies, permissions, scope, and current state.

⸻

41. Capability Selection and Trust

Capability selection and Trust are related but distinct.

Trust does not create capabilities.

Capability discovery does not grant Trust.

A capability can be selected as part of a candidate execution path, after which deterministic Trust evaluates whether the specific resolved action may proceed.

The canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Capability states such as UNAVAILABLE, UNKNOWN, DEPRECATED, or WAITING_FOR_CAPABILITY are not Trust outcomes.

⸻

42. Ambiguous Capability Selection

If multiple capabilities remain materially indistinguishable and the distinction affects execution, Noema must not guess.

For example:

retrieve_customer_profile
retrieve_customer_account_profile

If available context does not establish which semantic operation is required:

CLARIFY

may be required.

Ambiguity is execution-relevant state.

⸻

43. Capability Composition

Capabilities may be composed into workflows when their contracts and dependencies permit composition.

For example:

resolve_customer
      ↓
retrieve_account
      ↓
retrieve_transactions
      ↓
calculate_spending_summary

Composition must preserve each capability’s:

* scope
* constraints
* authorization requirements
* preconditions
* postconditions
* failure semantics
* idempotency semantics

⸻

44. Capability Dependencies

A capability may depend on other capabilities.

Examples:

search_transactions
      ↓
requires account resolution

or:

create_complaint
      ↓
requires customer identification

Dependencies must be explicit where they affect executability.

Hidden dependencies must not be introduced by model inference or adapter implementation.

⸻

45. Capability Decomposition

A high-level capability may be decomposed into lower-level capabilities.

For example:

retrieve_spending_summary
        │
        ├── resolve_account
        ├── retrieve_transactions
        └── calculate_summary

Decomposition must not create unsupported enterprise operations.

Each child capability must independently exist or be explicitly defined as part of a governed composite capability.

⸻

46. Capability Composition Versus Implementation

Composition is a semantic relationship.

Implementation is a technical relationship.

For example:

Capability A
     +
Capability B
     ↓
Workflow / Composite Capability

is different from:

Capability A
     ↓
Adapter
     ↓
Provider API

These relationships must remain explicit.

⸻

47. Capability Failure Semantics

Every executable capability should define expected failure classes where possible.

Examples:

INVALID_INPUT
UNAUTHORIZED
FORBIDDEN
RESOURCE_NOT_FOUND
CONFLICT
RATE_LIMITED
PROVIDER_UNAVAILABLE
TIMEOUT
UNKNOWN

These are capability/execution semantics, not automatically Trust outcomes.

A capability may define how particular failures can be recovered, retried, reconciled, or escalated.

⸻

48. Unknown Outcome

A capability execution may produce an unknown execution state.

For example:

request sent
     ↓
provider timeout
     ↓
result cannot be established
     ↓
UNKNOWN

Noema must not force:

UNKNOWN → FAILED

without sufficient evidence.

Unknown execution state should normally trigger verification or State Reconciliation before retry or compensation.

⸻

49. State Reconciliation

Capability-related state that depends on current enterprise reality may require State Reconciliation.

A canonical path is:

Enterprise System / Provider
        ↓
Observation
        ↓
Hard Schema Validation / Admission
        ↓
State Reconciliation
        ↓
Reconciled Fact
        ↓
Fact Status
        ↓
Context / Trust / Planning

The adapter may acquire observations.

The capability may describe how those observations are obtained.

Neither the adapter nor capability definition becomes the authority for enterprise business state merely because it retrieved the data.

⸻

50. Fact Status and Capability State

Capability state must not be used as a substitute for Fact Status.

For example:

Capability Status:
ACTIVE
Fact Status:
UNKNOWN

is valid.

The capability may be active while the current availability or state of a particular enterprise resource remains unknown.

Likewise:

Capability Status:
ACTIVE
Fact Status:
STALE

may mean that the capability exists but the particular observation available to Noema is outdated.

⸻

51. Capability Reconciliation

Reconciliation verifies that registered capability metadata still corresponds to enterprise reality.

It may compare:

Registered Capability
        vs
Current API / Schema / Configuration / Provider Behavior

Discrepancies must be recorded rather than silently rewriting canonical semantics.

Capability reconciliation concerns capability meaning and availability.

Business-state reconciliation remains governed by the enterprise state reconciliation model.

⸻

52. Capability Freshness

Capability metadata may become stale.

For example:

API previously supported operation X
        ↓
Provider removes operation X
        ↓
Registered capability metadata becomes stale

Freshness metadata should accompany capability evidence and availability information.

Freshness does not establish authority.

Recency is not authority.

⸻

53. Capability Drift

Capability drift occurs when the real enterprise operation diverges from registered capability semantics.

Examples:

* provider changes output meaning
* required input changes
* operation becomes restricted
* resource semantics change
* capability becomes unavailable
* workflow behavior changes
* security requirements change

Drift must trigger validation, reconciliation, or graph/capability evolution as appropriate.

⸻

54. Idempotency Semantics

Side-effecting capabilities must define whether repeated execution is safe.

Possible semantics:

IDEMPOTENT
NON_IDEMPOTENT
CONDITIONALLY_IDEMPOTENT
UNKNOWN

Noema must not assume idempotency from an HTTP method, provider convention, or model inference.

Idempotency must be bound to the Action Instance and execution semantics where required.

⸻

55. Read Capability Semantics

Read capabilities generally do not intentionally change enterprise business state.

Phase 1 examples include:

retrieve_account_balance
retrieve_statement
search_transactions
calculate_spending_summary

Even read operations require appropriate:

* identity
* resource scope
* permission
* policy
* context
* data-access controls

Read-only does not mean non-consequential.

A read operation may expose protected financial, identity, operational, or organizational information and therefore require deterministic Trust.

⸻

56. Write Capability Semantics

Write capabilities change enterprise state or cause externally visible side effects.

They require stronger guarantees around:

* authorization
* policy
* confirmation where required
* idempotency
* auditability
* reconciliation
* verification
* recovery

Capability registration alone does not authorize execution.

For the Noema Phase 1 transaction-exception POC, write capabilities are deliberately restricted to non-monetary operations such as complaint creation, escalation, routing, or case-state updates.

⸻

57. Confirmation

A capability may declare that a particular Action requires confirmation.

Confirmation is a control requirement, not a capability permission and not a Trust outcome.

A capability cannot treat the presence of a confirmation signal as sufficient authorization.

The exact actor, Intent version, Action, target, scope, and applicable policy must remain bound to the confirmation.

⸻

58. Capability Security

Capability metadata can itself be sensitive.

It may reveal:

* available enterprise systems
* privileged operations
* internal workflows
* security boundaries
* administrative functions
* sensitive resources
* provider topology

Access to capability metadata should therefore respect enterprise security and data boundaries.

⸻

59. Capability Visibility

Not every capability must be visible to every actor or integration context.

Visibility may depend on:

* tenant
* organization
* role
* environment
* domain
* security policy
* data-access scope

A capability can exist without being exposed as an eligible option to a particular actor.

Visibility does not equal permission.

⸻

60. Capability and Enterprise Graph

Enterprise capabilities are first-class nodes in the Enterprise Graph.

Conceptually:

System
   │
   └── PROVIDES ──> Capability
                         │
                         ├── REQUIRES ──> Permission
                         ├── CONSTRAINED_BY ──> Policy
                         ├── IMPLEMENTED_BY ──> Adapter
                         └── PARTICIPATES_IN ──> Workflow

The graph provides relationships required for capability resolution and bounded planning.

Graph connectivity does not itself establish authorization or business-state authority.

⸻

61. Capability and Enterprise Action Graph

The Enterprise Action Graph provides an executable-oriented projection of enterprise capabilities.

Conceptually:

Enterprise Capability
        ↓
Capability Binding
        ↓
Action / Action Contract
        ↓
Integration
        ↓
Execution Path

The EAG provides bounded relationships among:

* actors
* permissions
* policies
* capabilities
* actions
* resources
* systems
* integrations
* contracts

The EAG is not an independent source of enterprise business-state truth.

⸻

62. Capability and Intent

Intent describes what the source of intent wants to accomplish.

Capability describes what the enterprise can accomplish.

Intent
  = Requested semantic goal
Capability
  = Available enterprise ability

Intent resolution therefore includes determining whether available enterprise capabilities can support the resolved request.

A capability must not be invented merely because an Intent appears to require one.

⸻

63. Capability and Action

A capability is not itself an Action.

Capability
    ↓
Action

The capability defines the bounded enterprise ability.

The Action represents the concrete semantic operation instantiated for a particular Intent.

An Action must bind the relevant actor, target, resource, parameters, and scope before consequential execution.

⸻

64. Capability and Trust

Trust evaluates whether a specific capability-derived Action may proceed under current conditions.

Trust may consider:

* resolved actor
* identity
* permission
* policy
* resource
* context
* risk
* evidence
* current reconciled state
* environment
* capability constraints

Capability existence is necessary for an executable path but is not sufficient for execution.

Trust outcomes remain exactly:

EXECUTE
CLARIFY
ESCALATE
REJECT

EXECUTE means the evaluated path is permitted to proceed. It does not mean that the capability execution will succeed.

⸻

65. Capability and Contract

The capability defines semantic ability.

The Action Contract defines the precise executable boundary.

Capability
     ↓
Action
     ↓
Action Contract
     ↓
Executable Operation

The Action Contract must constrain execution so that the operation cannot exceed the registered capability semantics.

No free-form model output may bypass this boundary.

⸻

66. Capability and Adapter

The adapter implements the technical boundary between a capability and an external system.

Capability
     ↓
Binding
     ↓
Adapter
     ↓
Provider

The adapter must preserve capability semantics during translation.

Provider-specific behavior must not silently redefine the canonical capability.

⸻

67. Capability and Business State

Capabilities may read or change business state, but they do not own that state.

For example:

retrieve_account_balance
        ↓
Banking System
        ↓
Account Balance

The capability describes the operation.

The banking system or designated enterprise System of Record remains authoritative for the balance.

Capability ≠ Business State Authority

⸻

68. Capability and System of Record

The system implementing a capability may also be the System of Record for the resulting business state.

For example:

Capability
    ↓
Banking System
    ↓
Account Balance

The capability describes the operation.

The enterprise System of Record remains authoritative for the resulting business state.

Noema may retain observations, evidence, reconciliation results, and execution history without becoming a shadow System of Record.

⸻

69. Capability Metadata Model

A canonical capability may be represented conceptually as:

Capability
├── identity
├── name
├── description
├── version
├── domain
├── scope
├── status
├── inputs
├── outputs
├── resources
├── preconditions
├── postconditions
├── constraints
├── permissions
├── policies
├── dependencies
├── failure_semantics
├── idempotency_semantics
├── availability
├── evidence
├── fact_status
├── provenance
├── authority
└── bindings

Not every capability requires every field.

Every execution-relevant property must nevertheless be explicit or explicitly inherited from a governed contract or referenced canonical object.

⸻

70. Capability Binding Model

A binding may be represented as:

Capability Binding
├── capability_id
├── capability_version
├── adapter_id
├── adapter_version
├── system_id
├── provider
├── operation
├── environment
├── tenant_scope
├── resource_scope
├── status
└── validity

This keeps semantic capability identity separate from technical implementation.

⸻

71. Capability Resolution Pipeline

Capability resolution should follow:

Admitted Intent
      ↓
Intent / Context Resolution
      ↓
Candidate Capability Discovery
      ↓
Graph / Capability Registry Lookup
      ↓
Scope Validation
      ↓
Capability Schema / Semantic Validation
      ↓
Capability Eligibility
      ↓
Trust / Planning Constraints
      ↓
Executable Capability Path

State-dependent eligibility may require State Reconciliation before final selection.

Only governed capabilities may proceed toward Action planning.

⸻

72. Capability Selection and Determinism

After model interpretation and hard schema validation, capability selection must be deterministic given the same canonical inputs.

Conceptually:

same admitted intent version
+
same resolved actor / target / scope
+
same reconciled context
+
same graph version
+
same capability registry version
+
same applicable policies
+
same authorization inputs
+
same environment

should produce the same eligible capability set.

Determinism must not be achieved by hiding unresolved ambiguity or selecting based on model preference.

⸻

73. Capability Registry

Noema should maintain a governed Capability Registry containing canonical capability definitions and their bindings.

The registry should support:

* lookup
* versioning
* scope
* lifecycle state
* provenance
* authority
* validation
* deprecation
* supersession
* reconciliation
* compatibility

The registry must not become an uncontrolled dump of discovered API endpoints.

The registry is a canonical execution discovery surface, not an enterprise business-state System of Record.

⸻

74. Capability Registration

A capability should become executable only after registration establishes, as applicable:

* semantic definition
* scope
* authoritative basis
* evidence
* version
* implementation binding
* contract compatibility
* lifecycle state
* security requirements
* operational constraints

Registration is a governance boundary.

Registration does not grant runtime permission to an actor.

⸻

75. Capability Health

Capability health should distinguish:

semantic existence
implementation availability
provider availability
credential validity
configuration validity
execution eligibility
execution success

A temporary provider outage does not mean the capability no longer exists.

Credential validity does not establish capability semantic validity.

Execution success does not establish that future executions will succeed.

⸻

76. Capability Monitoring

Capability monitoring may track:

* execution success rate
* latency
* provider errors
* schema changes
* availability
* drift
* reconciliation failures
* contract violations
* deprecation signals

Monitoring data should inform validation and evolution without automatically rewriting canonical capability semantics.

Observed monitoring data is evidence until admitted and interpreted under the applicable authority model.

⸻

77. Capability Observability

Every consequential capability execution should be traceable to, as applicable:

capability_id
capability_version
intent_version
action_id
execution_id
adapter_id
adapter_version
system_id
provider_request_id
graph_version
contract_version
trust_decision_id

This allows the execution path to be reconstructed.

Non-executing capability discovery and read operations may require different levels of lineage according to their consequence and data sensitivity.

⸻

78. Capability Failure Boundary

Capability failure must remain distinguishable from failures elsewhere.

Intent / Resolution Failure
Trust Decision
Capability Resolution Failure
Contract Validation Failure
Adapter Failure
Provider Failure
Business Operation Failure
Unknown Execution State

These states require different recovery behavior.

A provider timeout must not automatically be represented as a capability semantic failure.

⸻

79. Capability Recovery

Recovery may involve:

* retry
* State Reconciliation
* alternative implementation
* alternative capability
* human intervention
* clarification
* escalation
* compensation where applicable

Recovery must respect the original Intent version, Action semantics, capability constraints, permissions, policies, contracts, idempotency requirements, and enterprise state.

The planner cannot invent a recovery capability.

⸻

80. Alternative Capability

An alternative capability may be considered only when its semantics are sufficiently compatible with the original intended operation or requested outcome.

For example:

Capability A unavailable
        ↓
Candidate Capability B
        ↓
Semantic Compatibility
        ↓
Scope / Policy / Authorization Validation
        ↓
Trust Re-evaluation

Noema must not substitute an arbitrary operation merely because it appears similar.

A materially different capability requires a new semantic decision and, where the requested operation changes, a new Intent version.

⸻

81. Capability Changes During Execution

If capability semantics change while an execution is in progress, the execution must not silently switch to the new semantics.

The execution should retain references to:

intent_version
capability_version
graph_version
contract_version
adapter_version

Any required revalidation or replanning must be explicit.

Historical execution meaning must remain reconstructable.

⸻

82. Capability Evolution

Capability evolution occurs when the semantic enterprise operation changes.

Examples:

* input semantics change
* output semantics change
* resource scope changes
* preconditions change
* postconditions change
* failure semantics change
* security requirements change
* idempotency semantics change

Such changes may require a new capability version.

Implementation changes that preserve semantics may instead be represented through binding or adapter version changes.

⸻

83. Intent Version Lineage

Consequential capability resolution and execution must preserve the exact Intent Object version that produced the operation.

An admitted Intent is immutable once admitted to Trust.

If clarification or another material change alters the requested semantic operation:

Intent v1
   ↓
supersedes
   ↓
Intent v2

Capability resolution for v2 must not silently rewrite the historical capability resolution for v1.

⸻

84. Resolved Identity and Target

For consequential capability use, Noema must preserve:

* resolved actor
* principal or delegated identity where applicable
* action
* exact target Resource
* scope
* resolution identity
* relevant resolution version
* Intent version

Capability existence cannot compensate for unresolved identity or target ambiguity.

An unresolved consequential target must not be guessed.

⸻

85. Planner Boundary

The planner may select and compose only capabilities represented by governed enterprise structures.

Planning is bounded by:

Enterprise Action Graph
        +
Capability Registry
        +
Action Model
        +
Action Contracts
        +
Enterprise Constraints

The planner must not:

* invent capabilities
* invent permissions
* invent authority
* create arbitrary resources
* bypass Trust
* modify canonical capability semantics
* create unregistered provider operations
* use arbitrary HTTP or SQL as an implicit capability

A model may propose a plan or capability candidate, but deterministic validation establishes whether the proposed path is admissible.

⸻

86. Security Boundary

Capability metadata and bindings must participate in Noema’s structural security boundary.

The model, user input, retrieved enterprise text, provider responses, and tool output are untrusted inputs.

The model must have no direct access to:

* enterprise credentials
* provider secrets
* unrestricted enterprise databases
* arbitrary provider endpoints
* unrestricted capability registry writes

Execution must occur through registered capabilities, Action Contracts, and approved integrations.

Secret references may be carried by controlled infrastructure but must not become part of ordinary capability semantics or model-visible context without explicit authorization.

⸻

87. Causal Audit

For consequential capability execution, Noema should preserve a causal chain such as:

Source of Intent
      ↓
Hard Schema Validation / Admission
      ↓
Intent Version
      ↓
Resolution
      ↓
Context / State Reconciliation
      ↓
Capability Resolution
      ↓
Trust Decision
      ↓
Action
      ↓
Action Contract
      ↓
Execution Attempt
      ↓
Adapter / Provider Observation
      ↓
State Reconciliation / Verification
      ↓
Outcome

Capability provenance should explain why a capability was considered available and applicable.

Auditability does not require exposing private model chain-of-thought.

⸻

88. Version Dimensions

Capability history may involve several independent version dimensions:

Intent Version
Capability Version
Action Version
Action Contract Version
Trust Contract Version
Policy Version
EAG / Graph Version
Capability Registry Version
Adapter Version
Integration Mapping Version
System Version
Provider API / Schema Version
Resource / Business-State Version
Event / Transport Schema Version

These versions must not be conflated.

Historical execution reconstruction must preserve the versions relevant to the execution.

⸻

89. Replay Semantics

Capability discovery records, provider observations, and capability-related events may be replayed for:

* analysis
* reconciliation
* testing
* audit
* reconstruction

Replay must not create a new business operation by default.

A replayed observation must not silently become a new capability execution.

Execution replay, where supported, requires explicit semantics and must preserve idempotency and safety boundaries.

⸻

90. Operational Memory

Operational Memory may retain structured history concerning:

* capability discovery
* capability validation
* capability drift
* capability selection
* capability execution
* failures
* reconciliation
* recovery
* provider behavior

Operational Memory is historical execution knowledge.

It is not:

* enterprise business-state authority
* permission authority
* capability authority merely because it contains historical records
* generic model memory

Historical records may support future decisions but must be evaluated against current authoritative state.

⸻

91. Capability and Business-State Authority

Enterprise systems remain authoritative for enterprise business state.

Noema may maintain canonical execution-domain representations concerning:

* Intent
* capability resolution
* Trust
* Action
* execution
* reconciliation
* Outcome
* audit
* operational history

These representations do not replace enterprise Systems of Record.

A capability response can be evidence about business state without becoming business-state authority.

⸻

92. Read-Only Consequence

Capability classification as read-only does not eliminate Trust requirements.

For example:

retrieve_customer_profile

may be technically read-only while exposing protected identity information.

Therefore:

Read-only
    ≠
Non-consequential

Data sensitivity, actor scope, permission, policy, and purpose remain relevant.

⸻

93. Capability Lifecycle and Historical Reconstructability

Deprecation and retirement must preserve historical meaning.

A retired capability must not receive new executions unless an explicit policy permits exceptional use.

Historical executions retain references to their original capability version and binding.

Historical Execution
       ↓
Retired Capability Version
       ↓
Historical Binding
       ↓
Historical Evidence

Retirement is not deletion.

⸻

94. Capability Deprecation

A capability may be deprecated when:

* a provider operation is being retired
* a superior capability supersedes it
* enterprise policy changes
* its semantics are no longer preferred
* its implementation becomes unsafe
* its constraints make it unsuitable for new execution

Deprecated capabilities should not normally be selected for new executions.

Deprecation must not alter the semantics of historical executions.

⸻

95. Capability Retirement

Retirement means the capability is no longer eligible for new execution.

Historical references remain valid for:

* audit
* reconstruction
* analysis
* historical reconciliation
* incident investigation

Retirement must not silently redirect historical execution records to a replacement capability.

⸻

96. Capability Supersession

A capability may be superseded by another capability.

Conceptually:

Capability v1
      ↓
SUPERSEDED_BY
      ↓
Capability v2

Supersession is a semantic relationship.

It does not imply equivalence.

Historical executions continue referencing the original capability version.

⸻

97. Capability Drift and Graph Evolution

Capability drift may require changes to the Enterprise Graph or Enterprise Action Graph.

Such changes must preserve:

* provenance
* scope
* authority
* temporal validity
* historical graph versions
* capability versions
* binding versions

A graph update must not silently rewrite historical capability meaning.

⸻

98. Capability and State Reconciliation During Recovery

When capability execution produces an unknown state, recovery must follow a reconciliation-first pattern where appropriate:

Execution Unknown
       ↓
Provider / Enterprise Observation
       ↓
Hard Schema Validation / Admission
       ↓
State Reconciliation
       ↓
Fact Status
       ↓
Trust / Preconditions Re-evaluated
       ↓
Retry / Continue / Compensate / Escalate

A timeout is not automatically a capability failure.

A retry is not automatically safe merely because the capability is marked idempotent; the current state and execution identity remain relevant.

⸻

99. Canonical Capability Execution Model

The canonical path is:

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
EAG / Capability Selection
      ↓
Plan
      ↓
Action Contract
      ↓
Execution Controller
      ↓
Integration Adapter
      ↓
Enterprise System / Provider
      ↓
Observation / Event
      ↓
State Reconciliation / Verification
      ↓
Outcome

Capability resolution may occur before final Trust evaluation to identify candidate executable paths, but no capability candidate becomes executable merely through discovery or selection.

⸻

100. Capability as a Bounded Execution Primitive

An Enterprise Capability is an enterprise-level semantic primitive.

It provides the bounded answer to:

What can this enterprise environment actually accomplish?

It does not answer:

May this actor perform it now?

That question belongs to authorization and deterministic Trust.

It does not answer:

Did it actually happen?

That question belongs to execution, verification, Outcome, and authoritative enterprise state.

⸻

101. Capability Execution Boundary

A capability may support two broad classes of Noema operations.

Evidence Acquisition

Capability
      ↓
Adapter
      ↓
Enterprise System
      ↓
Observation
      ↓
State Reconciliation

This path may be used to obtain information needed for Context, Reconciliation, or Trust.

Consequential Execution

Admitted Intent
      ↓
Resolved Action
      ↓
Trust
      ↓
Capability
      ↓
Action Contract
      ↓
Adapter
      ↓
Enterprise System
      ↓
Verification
      ↓
Outcome

The two paths must not be conflated.

An adapter invocation does not automatically mean an Action was executed.

⸻

102. Capability Invariants

The following invariants are mandatory:

1. A capability represents bounded enterprise ability.
2. Capability is distinct from permission.
3. Capability is distinct from policy.
4. Capability is distinct from authorization.
5. Capability is distinct from Trust.
6. Capability is distinct from Intent.
7. Capability is distinct from Action.
8. Capability is distinct from Action Contract.
9. Capability is distinct from execution.
10. Capability is distinct from Outcome.
11. Capability is distinct from adapter.
12. Capability is distinct from provider API.
13. Capability is not defined by a provider endpoint.
14. Capability identity is stable across compatible implementation changes.
15. Capability scope is explicit.
16. Capability semantics are explicit.
17. Capability inputs are explicit.
18. Capability outputs are explicit.
19. Capability resources are explicit.
20. Preconditions are explicit where required.
21. Postconditions are explicit where meaningful.
22. Constraints are explicit.
23. Required permissions are explicit where applicable.
24. Applicable policies are explicit where applicable.
25. Capability dependencies are explicit where execution depends on them.
26. Capability evidence is attributable.
27. Capability provenance is preserved.
28. Capability authority is identifiable for relevant claims.
29. Model-generated capabilities are proposals, not canonical capability truth.
30. Discovery does not automatically establish executable authority.
31. Capability definitions cross a hard schema validation/admission boundary before canonical execution use.
32. Persistence does not establish capability authority.
33. Capability Fact Status is distinct from Evidence.
34. Capability Fact Status is distinct from lifecycle status.
35. Fact Status may be VERIFIED, UNVERIFIED, STALE, CONFLICTED, or UNKNOWN.
36. Model confidence cannot establish capability authority or Fact Status.
37. State Reconciliation is used where current enterprise state or capability availability requires reconciliation.
38. Source and authority remain distinct.
39. Recency and authority remain distinct.
40. Canonicality is scoped.
41. Capability versions are explicit.
42. Capability lifecycle is explicit.
43. Deprecated capabilities are not silently selected for new executions.
44. Retired capabilities cannot receive new executions under normal operation.
45. Historical capability versions remain reconstructable.
46. Capability bindings are explicit.
47. Adapter identity is distinct from capability identity.
48. Provider implementation is distinct from capability semantics.
49. Multiple implementations do not imply semantic equivalence.
50. Capability existence is distinct from availability.
51. Availability is distinct from eligibility.
52. Eligibility is distinct from executability.
53. Eligibility respects scope.
54. Eligibility respects authorization requirements.
55. Eligibility respects policy requirements.
56. Eligibility respects environment.
57. Capability selection is deterministic after canonical inputs are established.
58. Ambiguous capability selection must not be resolved by guessing.
59. Capability composition preserves individual capability constraints.
60. Capability decomposition does not invent unsupported enterprise operations.
61. Capability failures are semantically classified.
62. Timeout does not automatically establish capability failure.
63. Unknown execution state is preserved explicitly.
64. Unknown execution state is reconciled before blind retry or compensation.
65. Side-effecting capabilities define idempotency semantics.
66. Idempotency does not replace Trust or verification.
67. Capability drift is detectable.
68. Capability reconciliation is supported.
69. Capability changes do not silently alter in-flight execution semantics.
70. Exact Intent version is preserved for consequential capability execution.
71. Admitted Intent is immutable once admitted to Trust.
72. Material Intent changes create a new Intent version.
73. Resolved actor and exact target are preserved for consequential execution.
74. Capability selection cannot create authority.
75. The planner cannot invent capabilities, permissions, resources, or provider operations.
76. Planner behavior is bounded by the EAG, Capability Registry, Action Model, and Action Contracts.
77. Capability registration is a governance boundary.
78. Capability registration does not grant runtime permission.
79. Capability does not create authorization.
80. Trust outcomes remain exactly EXECUTE, CLARIFY, ESCALATE, and REJECT.
81. Capability operational states are not Trust outcomes.
82. Trust EXECUTE does not imply execution success.
83. Capability success does not by itself establish enterprise business-state truth.
84. Enterprise Systems of Record remain authoritative for enterprise business state.
85. Capability metadata respects enterprise security boundaries.
86. Model output cannot directly invoke a capability.
87. The model has no direct capability credentials or unrestricted provider access.
88. Arbitrary HTTP, SQL, or provider operations are not implicit capabilities.
89. Capability execution occurs through governed Action Contracts and integrations.
90. Read-only capabilities may still be consequential.
91. Sensitive capability visibility is governed.
92. Replay of capability observations is non-executing by default.
93. Operational Memory is historical and non-authoritative.
94. Capability substitution requires semantic compatibility.
95. Capability evolution preserves historical meaning.
96. Capability version, graph version, contract version, adapter version, and provider version are distinct dimensions.
97. Capability execution is observable.
98. Consequential capability execution is auditable.
99. Provider responses and events remain evidence until appropriately validated and interpreted.
100. Capability semantics cannot be redefined by adapter implementation details.

⸻

103. Conceptual Enterprise Capability Graph

                         ┌──────────────┐
                         │    Actor     │
                         └──────┬───────┘
                                │
                              has
                                │
                                ▼
                         ┌──────────────┐
                         │  Permission  │
                         └──────┬───────┘
                                │
                             permits
                                │
                                ▼
┌──────────┐             ┌──────────────┐             ┌───────────┐
│  Intent  │────────────>│  Capability  │────────────>│  System   │
└──────────┘             └──────┬───────┘             └─────┬─────┘
                                │                            │
                         constrained by                 provides
                                │                            │
                                ▼                            ▼
                         ┌──────────────┐             ┌───────────┐
                         │    Policy    │             │  Adapter  │
                         └──────────────┘             └─────┬─────┘
                                                           │
                                                        invokes
                                                           │
                                                           ▼
                                                   ┌──────────────┐
                                                   │ Provider Op  │
                                                   └──────────────┘

The graph illustrates semantic relationships rather than a required storage schema.

Connectivity does not itself establish permission, Trust, or business-state authority.

⸻

104. Capability Execution Model

The complete consequential capability path is:

Source of Intent
      ↓
Intent Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Context / State Resolution
      ↓
Candidate Capability Resolution
      ↓
Deterministic Trust
      ↓
Capability / Action Selection
      ↓
Action Contract
      ↓
Integration Adapter
      ↓
Enterprise System
      ↓
Verification / State Reconciliation
      ↓
Outcome

For evidence acquisition:

Capability
      ↓
Integration Adapter
      ↓
Enterprise System
      ↓
Observation
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Fact Status

The capability is the semantic bridge between what the source of intent requests and what the enterprise environment can actually accomplish.

⸻

105. Final Definition

An Enterprise Capability is a canonical, scoped, versioned, governed, evidence-backed representation of an enterprise ability that can be implemented through one or more systems, integrations, adapters, or workflows.

It defines, as applicable:

what can be done
+
what inputs are required
+
what outputs are produced
+
what resources are involved
+
what conditions apply
+
what permissions are required
+
what policies constrain it
+
what constraints apply
+
how it may be implemented
+
what evidence establishes its existence
+
within what scope and version it is valid

without conflating those semantics with:

permission
authorization
policy
intent
action
action contract
execution
adapter
provider API
business state
outcome

Enterprise Capabilities are therefore bounded semantic execution primitives of Noema’s integration layer.

They allow Noema to reason in terms of enterprise ability rather than provider mechanics while preserving the fundamental architecture:

Capability
    = what the enterprise can do
Trust
    = whether a specific resolved operation may proceed
Action Contract
    = the precise executable boundary
Adapter
    = how the operation is technically invoked
Execution
    = what was attempted
Verification / State Reconciliation
    = what can be established about what happened
Outcome
    = Noema's execution-domain result
Enterprise System of Record
    = authoritative business state

The core invariant is:

A capability describes what the enterprise can do; it never, by itself, grants authority, creates executable permission, establishes business truth, or guarantees successful execution.