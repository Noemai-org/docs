Capability Model

Status: Foundational
Version: 0.1
Domain: Graph
Canonical Path: graph/capability-model.md

⸻

1. Definition

A Capability is a bounded, versioned, and governed description of what an enterprise-connected system or system boundary is able to accomplish through a defined operation.

A Capability represents ability, not:

* Intent;
* Permission;
* Authorization;
* Trust;
* Action;
* Execution;
* Outcome;
* enterprise Business State.

In Noema, Capabilities are first-class nodes in the Enterprise Action Graph (EAG). They connect enterprise reality to the set of Actions Noema can safely construct and execute through explicit Action Contracts and integrations.

⸻

2. Purpose

The Capability Model exists to:

* represent executable enterprise abilities;
* make available operations discoverable;
* constrain action planning to known capabilities;
* connect resolved Intent to executable operations;
* express capability requirements and dependencies;
* provide the basis for Action construction and validation;
* support deterministic Trust evaluation;
* preserve the boundary between capability and authorization;
* support capability-aware integration discovery;
* make enterprise execution surfaces structurally understandable;
* preserve provenance, versioning, and lifecycle;
* prevent model-generated operations from becoming executable by implication.

⸻

3. Core Principle

Noema must never treat arbitrary model output as an executable Capability.

A Capability must exist as a known, validated, governed graph object before it can support an executable Action.

The conceptual boundary is:

Probabilistic
──────────────────────────────
Intent interpretation
Candidate capability generation
Semantic matching proposals
──────────────────────────────
Hard Schema Validation / Admission
──────────────────────────────
Deterministic
Capability Graph
Action Model
Action Contracts
Trust
Execution
──────────────────────────────
Enterprise Systems

The model may propose what capability might satisfy an Intent.

The canonical graph determines whether that Capability exists and is applicable.

⸻

4. Capability Is Ability

A Capability answers:

What can this enterprise environment do?

Examples:

retrieve_account_balance
retrieve_statement
search_transactions
calculate_spending_summary
create_complaint
update_customer_profile
initiate_payment

A Capability describes an available enterprise ability.

It does not answer whether a particular actor is allowed to exercise that ability.

⸻

5. Capability Is Not Permission

A Capability describes what is possible.

A Permission describes what a particular principal is authorized to do.

Capability
    = the enterprise can perform X
Permission
    = this principal may perform X

Both may be required before an Action can execute.

Conceptually:

Capability
    +
Authorization
    +
Trust
    +
Valid Action
    +
Action Contract
    =
Potentially Executable Operation

Capability availability never creates permission.

⸻

6. Capability Is Not Intent

Intent describes the semantic goal originating from a Source of Intent.

Capability describes an enterprise ability that may help satisfy that goal.

For example:

Intent:
"Show me my transactions from last month."
Capability:
search_transactions

Intent is source- and actor-centered.

Capability is enterprise-execution-centered.

One Intent may require one or more Capabilities.

⸻

7. Capability Is Not an Action

A Capability represents an available ability.

An Action is a concrete semantic operation selected and instantiated for a particular Intent, target, resource, parameters, and context.

Capability
    ↓
Action
    ↓
Action Instance
    ↓
Execution

For example:

Capability:
search_transactions
Action:
search_transactions(
    customer_id = C123,
    start_date = 2026-08-01,
    end_date = 2026-08-31
)

The Capability does not itself identify the concrete target or parameter values.

⸻

8. Capability Is Not an Action Contract

The Capability answers:

What enterprise ability exists?

The Action Contract answers:

Under what formal contract may this Action be invoked and executed?

The Action answers:

What specific semantic operation are we performing?

Capability
"What is possible?"
Action
"What operation are we performing?"
Action Contract
"What formally governs its execution?"

A Capability without a valid Action Contract and executable binding is not sufficient to produce an executable Action.

⸻

9. Capability Is Not Trust

Capability establishes ability.

Trust establishes whether a particular resolved Action may proceed under applicable conditions.

Capability:
Can this operation exist?
Trust:
May this resolved operation proceed now?

A system may have a Capability while a particular Action is rejected, clarified, escalated, or otherwise prevented by Trust.

Canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Capability state must not be confused with these outcomes.

⸻

10. Capability Is Not Execution

Capability describes potential.

Execution describes an actual attempt to exercise that ability.

Capability
    ↓
Action
    ↓
Action Contract
    ↓
Execution

The existence of a Capability does not establish that an Action was executed or succeeded.

⸻

11. Capability Is Not Business State

A Capability does not represent the current state of an enterprise resource.

For example:

Capability:
retrieve_account_balance
Enterprise Business State:
account.balance = ₦1,250,000

The Capability describes the operation that can retrieve the business fact.

The enterprise System of Record remains authoritative for the business fact.

⸻

12. Capability as a Graph Node

Capabilities are first-class nodes in the Enterprise Action Graph.

A simplified graph may contain:

Source of Intent
      ↓
Intent
      │
      ├── requires → Capability
      │                  │
      │                  └── enables → Action
      │
      └── constrained by → Context
                              │
                              └── evaluated by → Trust

The graph represents relationships between semantic intent, enterprise ability, resources, systems, policies, capabilities, and execution surfaces.

⸻

13. Capability Identity

Every canonical Capability must have a stable identity.

Conceptually:

capability_id
capability_version

The identity should remain stable across ordinary implementation changes when the semantic ability remains unchanged.

The identity must not depend solely on a provider-specific API endpoint.

For example:

GET /v1/accounts/{id}/transactions
GET /api/customers/{id}/transactions
POST /transaction/search

may implement the same canonical semantic Capability.

⸻

14. Capability Semantics

A Capability must describe its semantic purpose independently of transport.

The model should capture, as applicable:

* what the Capability accomplishes;
* what resource types it operates on;
* what inputs it requires;
* what outputs it produces;
* what constraints apply;
* what preconditions apply;
* what postconditions are expected;
* what contracts govern invocation;
* what systems can provide it;
* what dependencies it has;
* what evidence it may produce;
* what failure characteristics are known;
* what recovery characteristics are known.

Transport details belong to integrations and execution bindings rather than the core semantic identity of the Capability.

⸻

15. Capability Structure

A canonical Capability may conceptually contain:

Capability
├── identity
├── semantic_definition
├── domain
├── resource_types
├── inputs
├── outputs
├── constraints
├── preconditions
├── postconditions
├── required_permissions
├── required_context
├── required_evidence
├── action_contracts
├── provider_bindings
├── dependencies
├── failure_characteristics
├── recovery_characteristics
├── provenance
├── authority
├── version
└── lifecycle_state

Not every implementation must expose every field.

The semantic distinctions must nevertheless remain explicit.

⸻

16. Capability Inputs

A Capability defines the information required to exercise an ability.

Examples:

search_transactions
    customer_id
    start_date
    end_date
retrieve_statement
    customer_id
    statement_period

Inputs may come from:

* resolved Intent;
* Context;
* enterprise data;
* identity;
* session state;
* explicit source input;
* previously established execution state.

Noema must not fabricate required inputs.

An unresolved required input may prevent Action construction or require CLARIFY.

⸻

17. Capability Outputs

A Capability defines the semantic class of result it can produce.

For example:

search_transactions
    → TransactionCollection
retrieve_statement
    → Statement

The semantic output is distinct from the provider’s raw response.

Integration layers may transform provider-specific responses into canonical representations after appropriate validation and admission.

⸻

18. Capability Preconditions

A Capability may require conditions before it can be exercised.

Examples:

* actor identity must be resolved;
* target resource must be identified;
* required context must exist;
* compatible integration must be available;
* required permission must be established;
* required contract version must be supported;
* resource state must satisfy defined conditions.

Capability preconditions constrain applicability.

They do not independently grant authorization.

The precise semantics of Action-level runtime preconditions belong to the Action Contract and execution model.

⸻

19. Capability Postconditions

A Capability may define expected conditions after successful execution.

For example:

retrieve_statement
    → statement is returned

For state-changing operations, postconditions may describe expected enterprise state changes.

Postconditions are expectations to be verified, not guarantees.

Actual enterprise business state remains enterprise-owned and must be established through appropriate authoritative evidence.

⸻

20. Capability Dependencies

Capabilities may depend on other capabilities.

For example:

resolve_customer
       ↓
resolve_account
       ↓
retrieve_balance

A dependency means the dependent Capability requires the prerequisite ability or resulting information/state.

Dependencies must be explicit.

Noema must not invent dependency chains dynamically merely because a model believes they are plausible.

⸻

21. Capability Composition

Multiple Capabilities may be composed to satisfy one Intent.

Example:

Intent:
"How much did I spend on food last month?"
Capabilities:
retrieve_transactions
        ↓
classify_transactions
        ↓
aggregate_spending

The resulting operation may contain multiple Actions and Executions.

Composition must remain explicit in the Action Graph and Plan.

⸻

22. Capability Granularity

Capabilities should be neither so broad that their semantics become ambiguous nor so narrow that the graph becomes operationally meaningless.

Prefer:

search_transactions

over:

do_customer_stuff

But avoid unnecessarily binding semantic identity to implementation details such as:

call_postgres_transaction_query_v17

Capability granularity should follow meaningful enterprise operations.

⸻

23. Capability Boundaries

A Capability should have a clear semantic boundary.

It should answer:

1. What can be done?
2. What resource does it operate on?
3. What inputs are required?
4. What result does it produce?
5. Under what conditions can it apply?
6. What contract governs invocation?
7. Which enterprise system or systems provide it?

If these cannot be answered sufficiently, the Capability is insufficiently bounded.

⸻

24. Capability and Resources

Capabilities operate on defined resource types.

Examples:

retrieve_balance
    operates_on → Account
search_transactions
    operates_on → Transaction
retrieve_statement
    operates_on → Statement
create_complaint
    operates_on → Complaint

Resource identity and enterprise Business State remain owned by the relevant enterprise authority.

A Capability does not itself identify a particular Resource instance.

⸻

25. Capability and Context

Context supplies information required to determine whether and how a Capability applies.

Examples include:

* actor identity;
* customer identity;
* account identity;
* organization;
* jurisdiction;
* time;
* environment;
* session state;
* relevant enterprise facts.

Context is not inherently authoritative merely because it is present.

Relevant information must satisfy the applicable validation, provenance, authority, freshness, and Fact Status requirements before being used for consequential decisions.

⸻

26. Capability and Identity

Capabilities may require identity context.

For example:

retrieve_account_balance
    requires:
        resolved_actor
        resolved_customer
        resolved_account

Identity resolution and Capability availability are separate concerns.

A Capability can exist even when the current actor has not yet been resolved sufficiently to invoke it.

⸻

27. Capability and Permission

A Capability may declare required permission classes.

For example:

Capability:
retrieve_account_balance
Required Permission:
account.read

The Capability declares the requirement.

The enterprise authorization system remains authoritative for whether the resolved principal possesses that authority.

Capability metadata must never be interpreted as proof that the permission exists.

⸻

28. Capability and Trust Evaluation

Trust evaluates the proposed use of a Capability in a specific context.

Conceptually:

Resolved Intent
      +
Resolved Actor / Target
      +
Context
      +
Evidence
      +
Capability
      +
Action
      +
Policy
      ↓
Deterministic Trust Evaluation
      ↓
EXECUTE | CLARIFY | ESCALATE | REJECT

Capability availability alone can never produce EXECUTE.

⸻

29. Capability Discovery

Noema may discover candidate capabilities from multiple enterprise sources, including:

* APIs;
* API schemas;
* documentation;
* workflow definitions;
* event schemas;
* policies;
* configuration;
* integration metadata;
* human-provided definitions.

Discovery produces candidate knowledge.

It does not automatically create a canonical executable Capability.

⸻

30. Capability Registration

A Capability must be registered before it becomes available to deterministic Action planning.

Registration should establish:

* stable identity;
* semantic definition;
* version;
* ownership;
* source;
* applicable authority;
* lifecycle state;
* contracts;
* provider bindings;
* constraints;
* provenance.

Unregistered capabilities must not silently enter the executable graph.

⸻

31. Hard Schema Validation and Admission

Capability definitions and externally discovered Capability representations must pass the applicable hard schema validation and admission boundary before becoming canonical graph objects.

The flow is:

Discovery / Model Proposal / External Source
                ↓
       Hard Schema Validation
                ↓
             Admission
                ↓
      Canonical Capability
                ↓
       Capability Validation
                ↓
       Graph Registration

A syntactically plausible model-generated Capability is not canonical merely because it matches a schema.

Semantic validity, provenance, authority, implementation, and lifecycle must also be established.

⸻

32. Capability Authority

Capability definitions may originate from multiple sources.

Noema must distinguish:

Capability Source
    ≠
Capability Authority

For example:

* documentation may describe an operation;
* an API schema may expose an operation;
* an integration may demonstrate connectivity;
* a system owner may establish operational authority.

Authority is claim-specific.

A source that proves an endpoint exists does not necessarily establish every semantic claim about that endpoint.

⸻

33. Capability Provenance

Every canonical Capability should retain provenance describing how it was established.

Provenance may include:

* source system;
* source document;
* API schema;
* integration;
* administrator;
* discovery process;
* transformation;
* version;
* timestamp.

Provenance allows Noema to determine why a Capability is recognized and which sources support its definition.

⸻

34. Capability Evidence

Evidence may support claims about a Capability.

Examples:

API schema
    → supports claim that an operation is exposed
Documentation
    → supports intended semantic behavior
Integration configuration
    → supports an executable binding
Runtime observation
    → supports current operational availability

These are distinct claims.

Evidence must not be collapsed into Capability authority without explicit semantics.

⸻

35. Fact Status and Capability Knowledge

Fact Status is distinct from Evidence and Capability identity.

A useful canonical set is:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Evidence:
provider responded successfully five minutes ago
Fact Status:
VERIFIED for the claim that the provider was reachable
at the relevant observation time

Fact Status is claim-, scope-, authority-, and time-specific.

Model confidence is not Fact Status.

⸻

36. Capability Freshness

Capabilities can become stale.

An API may be deprecated.

A workflow may change.

An integration may be disabled.

A provider may stop supporting an operation.

Therefore Capability applicability must account for freshness and lifecycle.

A stale Capability must not automatically be treated as currently executable.

⸻

37. Capability Lifecycle

A Capability should have an explicit lifecycle.

A conceptual lifecycle is:

DISCOVERED
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

Lifecycle transitions must be deterministic and auditable.

A retired Capability must remain interpretable for historical Actions that referenced its earlier version.

⸻

38. Capability Availability

Availability describes whether a Capability can currently be exercised through a valid implementation in a particular context.

Availability may depend on:

* active integration;
* supported contract version;
* environment;
* provider status;
* organizational scope;
* required dependencies;
* enterprise configuration.

Availability is contextual and temporal.

Capability existence does not guarantee current availability.

⸻

39. Capability Availability vs Business State

Capability availability must not be confused with enterprise Business State.

For example:

retrieve_balance = AVAILABLE

does not mean:

account.balance = known

Likewise:

retrieve_balance = UNAVAILABLE

does not establish anything about the actual account balance.

⸻

40. Capability Implementation

A canonical Capability may have multiple implementations.

For example:

retrieve_statement
    ├── Provider A
    ├── Provider B
    └── Provider C

The Capability remains the semantic abstraction.

Integration bindings determine how it is exercised against a particular enterprise system.

⸻

41. Capability Binding

A Capability Binding connects a canonical Capability to an executable integration surface.

Capability
    ↓
Binding
    ↓
Provider Operation
    ↓
Action Contract
    ↓
Execution

The binding may specify:

* provider;
* operation;
* protocol;
* authentication requirements;
* mapping;
* contract version;
* timeout behavior;
* idempotency behavior;
* error mapping;
* system version.

Binding metadata must not redefine the Capability’s semantic identity unless the semantic ability itself has changed.

⸻

42. Capability and Integration

Integration is the mechanism through which a Capability is exercised against an external system.

The integration translates between:

Noema Canonical Action
        ↕
Provider-Specific Operation

Integration logic must preserve the semantic boundary between the Capability and provider implementation.

Noema must not assume that an arbitrary reachable endpoint constitutes a valid Capability.

⸻

43. Capability and Events

Capabilities may produce or depend upon Events.

For example:

create_complaint
       ↓
ComplaintCreated

Events provide observations about enterprise or execution activity.

An Event does not itself constitute a Capability.

Observing an Event does not authorize Noema to perform a corresponding Action.

⸻

44. Capability and Policies

Policies constrain how Capabilities may be used.

For example:

Capability:
retrieve_statement
Policy:
Statements older than seven years cannot be retrieved.

The Capability remains an enterprise ability.

The policy determines whether a particular use is permitted.

Policy does not redefine the Capability merely because it restricts its use.

⸻

45. Capability and Constraints

Constraints may limit applicability.

Constraints can include:

* resource type;
* time period;
* organization;
* jurisdiction;
* environment;
* actor type;
* transaction state;
* data availability;
* provider limitations;
* regulatory boundaries.

Constraints should be represented explicitly rather than hidden inside natural-language descriptions.

⸻

46. Capability and Ambiguity

A Capability does not resolve ambiguity in an Intent.

For example:

Intent:
"Show me my account."
Available Capabilities:
retrieve_account_balance
retrieve_statement
retrieve_transactions

The existence of several Capabilities does not justify arbitrary selection.

If the ambiguity materially changes the requested operation, Noema must resolve it through the appropriate Intent clarification path.

⸻

47. Capability Selection

Capability selection is graph-constrained.

A model may propose candidate Capabilities during interpretation.

Noema must validate candidates against:

* registered Capability definitions;
* semantic compatibility;
* required context;
* resource types;
* contracts;
* authorization requirements;
* policies;
* Trust constraints;
* current availability.

Unknown capabilities cannot become valid merely because a model generated a plausible name.

⸻

48. Capability Matching

Intent-to-Capability matching should consider semantic compatibility.

Conceptually:

Intent Requirements
        ↓
Capability Candidates
        ↓
Semantic Validation
        ↓
Context / Resource Validation
        ↓
Contract Validation
        ↓
Trust Evaluation

Similarity alone is insufficient.

A semantically similar Capability may still be invalid because its resource, scope, permissions, contract, or constraints do not match.

⸻

49. Capability Conflicts

Multiple Capabilities may appear to satisfy the same Intent.

Noema must not silently choose between materially different Capabilities when the choice affects:

* meaning;
* target;
* authority;
* risk;
* outcome;
* data exposure;
* execution behavior.

Resolution may require:

* deterministic precedence;
* clarification;
* escalation.

The mechanism must be explicit.

⸻

50. Capability Supersession

A Capability may be superseded by another Capability.

For example:

retrieve_customer_profile_v1
        ↓ superseded by
retrieve_customer_profile_v2

Supersession must preserve historical interpretation.

Existing Actions and Executions referencing the original Capability must remain interpretable.

⸻

51. Capability Versioning

Capability semantics may evolve.

A new Capability version is required when semantic meaning or executable requirements change materially.

Implementation changes that preserve semantic meaning do not necessarily require a new Capability version.

Capability versioning is distinct from:

* API versioning;
* integration versioning;
* Action Contract versioning;
* model versioning;
* deployment versioning.

⸻

52. Capability Compatibility

Capability versions may be:

NON-BREAKING
CONDITIONALLY COMPATIBLE
BREAKING

Compatibility must be determined semantically.

A provider API can change while the canonical Capability remains compatible.

Conversely, a small provider change may require a Capability version change if the enterprise semantics change.

⸻

53. Capability and Action Graph Construction

Capabilities are fundamental building blocks of the Enterprise Action Graph.

A graph may represent:

Intent
  │
  ├── requires → Capability
  │                  │
  │                  ├── requires → Context
  │                  ├── governed_by → Policy
  │                  ├── requires → Permission
  │                  └── enables → Action
  │
  └── resolved_with → Evidence

The graph allows Noema to reason about executable enterprise reality rather than merely generate text.

⸻

54. Capability Graph Relationships

Canonical relationships may include:

Capability
├── requires → Capability
├── operates_on → Resource
├── requires → Context
├── requires → Permission
├── governed_by → Policy
├── implemented_by → Integration
├── bound_to → Provider Operation
├── produces → Event
├── supported_by → Evidence
├── constrained_by → Constraint
├── enables → Action
├── supersedes → Capability
└── depends_on → Capability

Relationships must have defined semantics.

They must not be created merely because two entities appear related in source material.

⸻

55. Capability and Action Planning

Action planning operates over known Capabilities.

Resolved Intent
      ↓
Required Capability Set
      ↓
Capability Graph
      ↓
Action Selection
      ↓
Plan

The Plan must reference actual registered Capabilities.

A Plan must not contain operations that exist only in model-generated reasoning.

⸻

56. Capability Sets

A single Intent may require a set of Capabilities.

For example:

Intent:
"Summarize my spending last month."
Required Capabilities:
    retrieve_transactions
    classify_transactions
    aggregate_spending

A Capability Set represents the abilities collectively required to satisfy a particular Intent.

Capability Sets may become reusable graph patterns.

⸻

57. Capability Paths

A graph may contain multiple paths from an Intent to an intended result.

For example:

Intent
  ↓
retrieve_transactions
  ↓
aggregate_spending
  ↓
SpendingSummary

or:

Intent
  ↓
retrieve_existing_spending_summary
  ↓
SpendingSummary

Path selection must consider explicit constraints including:

* semantic correctness;
* current state;
* Trust;
* policy;
* authorization;
* capability availability;
* cost;
* latency;
* risk.

The shortest path is not inherently the correct path.

⸻

58. Capability Failure Characteristics

A Capability may describe known failure characteristics where meaningful.

Examples:

IDENTITY_REQUIRED
PERMISSION_DENIED
RESOURCE_NOT_FOUND
VALIDATION_FAILED
PROVIDER_UNAVAILABLE
TIMEOUT
RATE_LIMITED
UNKNOWN_OUTCOME

Failure characteristics describe known behavior.

They do not establish that a particular execution failed.

Actual execution failure remains an execution-domain fact established through execution evidence.

⸻

59. Capability Recovery Characteristics

Capabilities may define recovery characteristics.

Examples:

* retryable;
* non-retryable;
* idempotent;
* conditionally idempotent;
* requires reconciliation;
* requires human intervention;
* supports compensation.

Recovery characteristics influence execution planning and control.

They do not themselves execute recovery.

⸻

60. Capability Safety Classification

Capabilities should be classified according to the consequences of exercising them.

Examples:

Read:
retrieve_balance
Sensitive read:
retrieve_customer_profile
State-changing:
update_customer_profile
Financial:
initiate_payment

Capability classification informs Trust and execution requirements.

It does not itself authorize an Action.

⸻

61. Read Capabilities

Read capabilities remain governed capabilities.

Examples:

* retrieve account balance;
* retrieve statement;
* search transactions;
* retrieve customer profile.

Read operations may still:

* expose protected data;
* cross organizational boundaries;
* invoke sensitive enterprise systems;
* consume significant resources;
* produce operational effects.

Therefore read-only does not mean governance-free.

⸻

62. Phase 1 Capability Scope

Noema’s initial commercial wedge may favor read-oriented and non-monetary capabilities with clear enterprise semantics.

Examples:

retrieve_account_balance
retrieve_statement
search_transactions
calculate_spending_summary
create_complaint

These support customer-account investigation without requiring Noema to move money.

The executable Capability surface should remain deliberately constrained to registered graph objects.

⸻

63. Capability Discovery from Enterprise Documentation

Enterprise documentation may describe capabilities without explicitly naming them as such.

For example:

"Customers can view transactions for the previous 90 days."

This may support discovery of:

search_transactions

However, documentation alone does not necessarily establish that the Capability is currently executable.

The graph must distinguish:

described capability
implemented capability
registered capability
available capability
authorized use

⸻

64. Capability Extraction

AI models may assist in extracting candidate Capabilities from enterprise sources.

For example:

Candidate Capability:
retrieve_customer_statement

The candidate must then pass deterministic validation for:

* semantic definition;
* source evidence;
* authority;
* implementation;
* resource types;
* contract;
* scope;
* lifecycle;
* integration binding;
* provenance.

Model-generated candidates are proposals, not canonical truth.

⸻

65. Capability Canonicalization

Multiple sources may describe the same underlying ability.

For example:

"View transactions"
"Transaction history"
"Get account transactions"
"Retrieve transaction records"

These may represent one canonical Capability:

search_transactions

Canonicalization should consolidate equivalent semantics while preserving source provenance.

⸻

66. Capability Duplication

The graph should avoid duplicate Capabilities representing the same semantic ability unless they differ in a meaningful dimension.

Meaningful differences may include:

* resource;
* scope;
* authority;
* security boundary;
* business semantics;
* execution behavior;
* required contract;
* jurisdiction.

Provider endpoint differences alone should not automatically create separate canonical Capabilities.

⸻

67. Capability Decomposition

A Capability should be decomposed when it combines independent enterprise abilities.

Avoid:

manage_customer_account

when the underlying semantics are:

retrieve_customer_profile
update_customer_profile
search_transactions
retrieve_statement
create_complaint

Decomposition makes permissions, Trust, execution, and auditability more precise.

⸻

68. Capability Aggregation

Conversely, multiple low-level operations may be represented by a higher-level Capability when the enterprise semantics are genuinely unified.

For example:

generate_spending_summary

may internally require:

retrieve_transactions
+
classify_transactions
+
aggregate_transactions

The graph may represent the higher-level Capability as composed semantics with explicit dependencies.

⸻

69. Capability Ownership

Every Capability should have an identifiable owner or owning domain.

Ownership may determine:

* who defines semantics;
* who approves changes;
* who controls lifecycle;
* who provides evidence;
* who resolves semantic conflicts;
* who manages integrations.

Capability ownership does not transfer ownership of enterprise Business State to Noema.

⸻

70. Capability Scope

Capabilities may be scoped by:

* tenant;
* organization;
* legal entity;
* environment;
* domain;
* resource type;
* provider;
* jurisdiction;
* time.

The same semantic Capability may therefore have different availability or constraints across enterprise contexts.

Canonicality is always scoped to its defined semantic, authority, source, tenant, and temporal boundaries.

⸻

71. Capability Environment

A Capability may be available in one environment but unavailable in another.

For example:

Production:
retrieve_statement → ACTIVE
Sandbox:
retrieve_statement → ACTIVE
Development:
retrieve_statement → UNAVAILABLE

Environment is generally an applicability dimension rather than part of the semantic Capability identity.

⸻

72. Capability State and Unknown

Noema must support uncertainty around current Capability availability.

If Noema cannot establish whether a Capability is currently available, it must not silently assume availability.

For example:

AVAILABLE
UNAVAILABLE
UNKNOWN

must remain distinguishable.

The appropriate downstream response depends on the cause and may involve clarification, escalation, replanning, or another deterministic control path.

UNKNOWN must not be silently converted to UNAVAILABLE or AVAILABLE.

⸻

73. Capability and State Reconciliation

Capability availability and implementation state may require reconciliation across enterprise systems.

For example:

Enterprise Systems
      ↓
Observations
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Reconciled Capability Availability
      ↓
Planning / Trust / Execution

State Reconciliation is particularly important when capability availability depends on:

* multiple systems;
* eventually consistent configuration;
* integration health;
* deployment state;
* provider state;
* contract support.

Reconciliation establishes current knowledge; it does not transfer authority from the enterprise.

⸻

74. Capability and Determinism

Capability reasoning must ultimately terminate in deterministic graph state.

The model may propose:

search_transactions

The graph determines whether that Capability:

* exists;
* is schema-valid;
* is registered;
* is semantically applicable;
* is within scope;
* has required dependencies;
* has a valid binding;
* is currently available.

The model does not create authority by generating a Capability name.

⸻

75. Capability Graph as an Executability Boundary

The Capability Graph acts as a structural boundary between language understanding and execution planning.

Probabilistic
────────────────────────────
Human Language
LLM Interpretation
Candidate Capabilities
Semantic Proposals
────────────────────────────
Hard Schema Validation / Admission
────────────────────────────
Deterministic
Capability Graph
Action Model
Contracts
Permissions
Policies
Trust
Execution
────────────────────────────
Enterprise Systems

Only validated and admitted Capabilities may cross into the executable portion of Noema.

⸻

76. Capability and Historical Execution

Historical Actions and Executions must retain references to the Capability version that governed them.

A Capability cannot be reinterpreted retrospectively merely because its current definition changed.

Historical references support:

* auditability;
* replay;
* incident investigation;
* recovery;
* reconciliation;
* compliance.

Historical execution remains tied to the semantic Capability that actually governed it.

⸻

77. Capability Observability

Noema should observe capability-level metrics such as:

* discovery rate;
* validation rate;
* registration rate;
* activation rate;
* invocation rate;
* failure rate;
* unknown-outcome rate;
* latency;
* provider availability;
* deprecation rate;
* selection conflicts;
* binding failures.

These metrics help identify weaknesses in the Enterprise Action Graph.

They are operational observations, not business-state authority.

⸻

78. Capability Graph Evolution

The Capability Graph evolves as enterprise systems evolve.

Evolution may include:

new Capability
Capability modification
Capability version
Capability supersession
Capability deprecation
Capability retirement
new provider binding
provider removal
dependency change
policy change
availability change

Graph evolution must preserve historical meaning.

A graph update must not silently rewrite the meaning of historical Actions or Executions.

⸻

79. Capability Security Boundary

Capability definitions may contain sensitive operational information.

Noema should control exposure of:

* provider details;
* internal endpoints;
* authorization requirements;
* implementation metadata;
* operational constraints;
* security-sensitive integration details.

Capability discovery does not imply unrestricted disclosure of implementation information.

The model should receive only the Capability information required for its authorized task.

⸻

80. Capability Registry

Noema should maintain a canonical registry of recognized Capabilities.

Conceptually:

Capability Registry
├── Identity
├── Semantic Definition
├── Versions
├── Lifecycle
├── Ownership
├── Provenance
├── Authority
├── Contracts
├── Policies
├── Dependencies
├── Provider Bindings
├── Scope
└── Availability

The Registry provides the canonical lookup surface for capability-aware planning.

Registry membership is necessary for executable use but does not itself grant authorization.

⸻

81. Capability Validation

Before a Capability can support an executable Action, Noema should validate:

1. Does the Capability exist?
2. Is its definition schema-valid?
3. Has it passed admission?
4. Is its version supported?
5. Is its lifecycle active?
6. Is its semantic definition sufficient?
7. Does the current Intent require it?
8. Does the Context satisfy its requirements?
9. Does the resolved resource match its supported resource type?
10. Are required permissions established through the appropriate authority?
11. Are required contracts available?
12. Is an executable binding available?
13. Are applicable policies and constraints satisfied?
14. Is relevant evidence sufficient and appropriately authoritative?
15. Is current availability established?
16. Can Trust evaluate the proposed use deterministically?

Failure of a required validation must produce an explicit deterministic state.

⸻

82. Capability and Planner Boundaries

The Planner may select among registered Capabilities and construct a bounded plan.

It must not:

* invent Capabilities;
* invent Actions;
* invent permissions;
* create authority;
* modify Action Contract semantics;
* bypass Trust;
* bypass State Reconciliation;
* directly access enterprise systems;
* create arbitrary HTTP or SQL operations as capabilities.

The Planner operates over the Enterprise Action Graph and registered execution surfaces.

⸻

83. Capability and Action Contracts

A Capability may reference one or more Action Contracts capable of expressing its executable use.

The relationship is:

Capability
    ↓
Action
    ↓
Action Contract
    ↓
Integration Binding
    ↓
Execution Consumer
    ↓
Enterprise System

The Capability describes the enterprise ability.

The Action Contract defines the formal execution boundary.

The exact Action Contract schema belongs to the Action Contract model.

⸻

84. Capability and State Reconciliation

A Capability may depend on current enterprise state even when the Capability itself is static.

For example:

Capability:
retrieve_account_balance
Current question:
Can account A be queried now?

The Capability may be active while the specific resource is:

* unavailable;
* restricted;
* deleted;
* in an incompatible state;
* unknown.

Capability existence therefore does not establish Action-level eligibility.

State Reconciliation supplies current enterprise-state knowledge where required.

⸻

85. Capability and Fact Status

Capability claims may require Fact Status.

For example:

Claim:
Provider supports Capability X
Evidence:
validated provider configuration
Fact Status:
VERIFIED

Another claim may be:

Claim:
Capability X is currently available
Fact Status:
UNKNOWN

These are separate claims with potentially different statuses.

A single Capability object must not imply that every associated claim is equally verified.

⸻

86. Capability and Outcome

Capability availability does not establish Outcome.

For example:

Capability:
create_complaint = ACTIVE

does not mean:

Complaint = CREATED

Only an actual Action execution followed by appropriate verification can establish the execution Outcome.

The enterprise system remains authoritative for the resulting Business State.

⸻

87. Capability and Unknown Execution

A Capability may explicitly identify that exercising it can produce UNKNOWN execution state.

For example:

initiate_external_operation
    recovery:
        requires_reconciliation

If execution becomes UNKNOWN, Noema must reconcile before retrying or taking another consequential Action where duplicate effects are possible.

Capability metadata informs this behavior.

It does not replace the execution and reconciliation models.

⸻

88. Capability and Read-Only Consequence

A read Capability may still be consequential.

For example:

retrieve_sensitive_customer_data

may have no business-state write but may expose protected information.

Therefore:

read-only
≠
no Trust required

Capability classification must account for data sensitivity and consequence, not only whether the operation writes business state.

⸻

89. Capability and Replay

Capability discovery, graph evolution, and historical execution records may be replayed for analysis.

Replay is non-executing by default.

Replaying a Capability graph must not automatically:

* invoke a provider;
* create an Action;
* execute an Action;
* change enterprise state.

A new execution requires an explicitly governed path.

⸻

90. Capability and Operational Memory

Operational Memory may retain:

* Capability discovery history;
* validation results;
* graph changes;
* binding failures;
* availability observations;
* historical selection;
* execution references.

Operational Memory is historical execution knowledge.

It is not:

* enterprise Business State;
* permission authority;
* current Capability authority by itself;
* a replacement for State Reconciliation;
* generic model memory.

⸻

91. Capability Version Dimensions

Capability semantic versioning must remain distinct from other version dimensions.

Relevant versions may include:

* Capability semantic version;
* Action version;
* Action Contract version;
* Trust Contract version;
* policy version;
* EAG version;
* Capability Registry version;
* integration mapping version;
* system version;
* provider version;
* resource/business-state version;
* transport/schema version;
* model version.

Historical execution should preserve the versions relevant to the actual decision and execution path.

⸻

92. Capability Causal Audit

A consequential Capability-driven execution should be traceable through a causal chain such as:

Source of Intent
      ↓
Intent Version
      ↓
Resolved Actor / Action / Target
      ↓
Capability Selection
      ↓
Capability Version
      ↓
Capability Provenance / Authority
      ↓
Context / State Reconciliation
      ↓
Trust Decision
      ↓
Action Contract
      ↓
Execution
      ↓
Verification
      ↓
Outcome

The audit explains which Capability made the execution path possible and which evidence established its applicability.

It does not require exposing private model chain-of-thought.

⸻

93. Capability Lifecycle and Historical Meaning

Capability lifecycle changes must preserve historical interpretation.

If:

Capability v1 → DEPRECATED
Capability v2 → ACTIVE

historical executions under v1 remain associated with v1.

Deprecation means that new executions may no longer select the Capability under applicable rules.

It does not erase or reinterpret historical use.

⸻

94. Capability Invariants

The Capability Model establishes the following invariants:

1. A Capability represents enterprise ability, not Intent.
2. A Capability is not a Permission.
3. A Capability is not authorization.
4. A Capability is not a Trust Decision.
5. A Capability is not an Action.
6. A Capability is not an Action Contract.
7. A Capability is not an Execution.
8. A Capability is not an Outcome.
9. A Capability is not enterprise Business State.
10. Every canonical Capability must have a stable identity.
11. Capability identity must be distinguishable from provider endpoint identity.
12. Capability semantics must remain implementation-independent.
13. Model-generated Capabilities are candidates, not canonical truth.
14. Capability definitions must pass applicable hard schema validation and admission.
15. Only registered Capabilities may support executable Action planning.
16. Capability selection must be graph-constrained.
17. Capability authority must be explicit and claim-specific.
18. Capability provenance must be preserved.
19. Capability availability must be distinguishable from Capability existence.
20. Capability availability must be scoped by relevant environment, tenant, organization, provider, time, and other applicability dimensions.
21. Capability uncertainty must remain distinguishable from unavailability.
22. Fact Status must remain distinct from Evidence, Context, Capability identity, and Outcome.
23. Model confidence must not become Capability authority or Fact Status.
24. Required Capability inputs must not be fabricated.
25. Required context must not be invented.
26. Capability availability does not imply Permission.
27. Capability availability does not imply Trust authorization.
28. Capability availability does not imply execution success.
29. Capability availability does not imply enterprise Business State.
30. Trust must independently evaluate proposed consequential use.
31. Canonical Trust outcomes remain EXECUTE, CLARIFY, ESCALATE, and REJECT.
32. Capability-specific states must not be represented as additional Trust outcomes.
33. Capability dependencies must be explicit.
34. Capability composition must remain observable.
35. Capability conflicts must not be resolved through silent guessing.
36. Provider endpoint differences must not automatically create separate canonical Capabilities.
37. Multiple provider implementations may realize one canonical Capability.
38. Capability failure characteristics must not be confused with actual Execution Failure.
39. Capability recovery characteristics must not themselves perform recovery.
40. Capability lifecycle must be explicit.
41. Capability versioning must preserve historical meaning.
42. Historical Actions must preserve the Capability version that governed them.
43. State Reconciliation must be used where current capability applicability or enterprise state cannot otherwise be established reliably.
44. Capability-related historical snapshots are not automatically current truth.
45. Planner cannot invent Capabilities, Actions, permissions, authority, or execution paths.
46. Planner cannot bypass Trust, Action Contracts, or State Reconciliation.
47. Capability registration does not grant authorization.
48. Capability discovery does not imply executable availability.
49. Replay of Capability knowledge must not create external side effects by default.
50. Operational Memory is historical knowledge, not enterprise authority.
51. Read-only Capabilities may still be consequential and require governance.
52. Enterprise systems remain authoritative for enterprise Business State.
53. A Capability must not become executable solely because an LLM generated a plausible description of it.
54. The canonical graph must preserve enough provenance, version, scope, and authority information to explain why a Capability was available to a particular execution path.

⸻

95. Relationship to the Noema Model

The Capability Model occupies the graph layer between enterprise execution reality and Action planning:

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
Enterprise Action Graph
      ↓
Capability Selection
      ↓
Plan
      ↓
Action Contract
      ↓
Execution
      ↓
Verification / Reconciliation
      ↓
Outcome

The Capability Graph constrains the transition from:

what the actor wants

to:

what the enterprise environment can actually support

without allowing the model to invent executable reality.

⸻

96. Final Definition

A Capability in Noema is a canonical, bounded, versioned, and governed representation of an enterprise ability that can be connected to executable operations through validated Action Contracts and integration bindings.

Capabilities are first-class nodes in the Enterprise Action Graph.

They provide the structural bridge between resolved Intent and executable Action while preserving the distinction between:

* ability and permission;
* ability and authorization;
* ability and Trust;
* ability and Action;
* ability and execution;
* ability and Outcome;
* ability and enterprise Business State.

A Capability becomes part of the executable graph only after appropriate schema validation, admission, semantic validation, provenance, authority, lifecycle, scope, and implementation requirements have been satisfied.

The model may assist in discovering or proposing Capabilities.

It cannot create a Capability by assertion.

Noema executes only through Capabilities the enterprise graph can establish as real, bounded, governed, and connected to an explicit execution path.