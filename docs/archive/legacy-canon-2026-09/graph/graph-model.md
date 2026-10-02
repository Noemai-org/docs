> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Graph Model

Status: Foundational
Version: 0.1
Domain: Graph
Canonical Path: graph/graph-model.md

⸻

1. Definition

The Noema Graph Model defines the structural model used to represent enterprise reality as a connected, scoped, versioned, temporal, authority-aware, and provenance-aware graph.

It specifies:

* what entities exist in the graph
* what relationships connect them
* what those relationships mean
* what information belongs on nodes and edges
* how scope and authority are represented
* how temporal validity is modeled
* how evidence and Fact Status are represented
* how graph state evolves
* how graph state supports intent-aware execution

The Graph Model is the structural foundation for the Enterprise Graph and its executable projections.

⸻

2. Purpose

The Graph Model exists to provide a canonical representation of the environment in which Noema interprets and executes Intent.

It allows Noema to reason about questions such as:

* Who is requesting an Action?
* Which organization does the Actor belong to?
* Which Resources exist?
* Which Systems own or manage those Resources?
* Which Capabilities exist?
* Which Permissions apply?
* Which Policies constrain execution?
* Which Actions are possible?
* Which Integrations can execute them?
* Which Evidence establishes a claim?
* Which Workflow or dependency applies?
* Which state is current?
* Which state was historically established?
* Which relationships remain unknown or conflicted?

⸻

3. Graph Model Principle

The graph is not merely a collection of entities.

Its meaning comes from the combination of:

Nodes
+
Relationships
+
Attributes
+
Scope
+
Authority
+
Temporal Validity
+
Provenance
+
Version
+
Fact Status

A node without meaningful relationships is often insufficient to establish executable enterprise structure.

A relationship without scope, authority, or temporal semantics may also be insufficient for consequential reasoning.

⸻

4. Graph as Enterprise Structure

The Graph Model represents enterprise structure rather than merely enterprise data.

It captures relationships between:

* Actors
* Organizations
* Identities
* Resources
* Systems
* Capabilities
* Actions
* Permissions
* Policies
* Workflows
* Events
* Evidence
* Contracts
* Integrations
* Environments
* Domains

This structure allows Noema to reason across otherwise disconnected enterprise systems.

⸻

5. Graph Does Not Replace Enterprise Systems

The Graph Model must never be interpreted as a replacement for enterprise Systems of Record.

Enterprise systems remain authoritative for business state such as:

* balances
* transactions
* account ownership
* inventory
* payment state
* contractual state
* customer records
* financial ledgers

The graph represents the relationships and execution-relevant structure around those systems.

A graph representation of a business fact does not transfer authority over that fact to Noema.

⸻

6. Graph Does Not Become Shadow Business State

Noema must not replicate business state merely because graph traversal would become easier.

A graph representation of a business fact is justified only when it serves a defined Noema purpose and preserves the authority of the underlying enterprise source.

Enterprise System
      │
      │ authoritative business state
      ▼
Business Truth
      │
      │ observed / represented
      ▼
Noema Graph
      │
      │ execution-relevant structure
      ▼
Enterprise Structure

Noema may maintain references, projections, observations, and execution-domain state without becoming a shadow System of Record.

⸻

7. Graph Node

A node represents a canonical entity relevant to Noema’s reasoning or execution model.

Examples include:

* Actor
* Organization
* Identity
* Resource
* System
* Capability
* Action
* Policy
* Permission
* Workflow
* Event
* Evidence
* Contract
* Integration
* Environment
* Domain

Every node type must have defined semantics.

A model-generated candidate entity is not canonical merely because it conforms to the node schema.

⸻

8. Node Identity

Every canonical node must have a stable identity within its defined scope.

A node identity must not depend solely on mutable display attributes.

For example:

customer_name = "John Doe"

is not a sufficient identity.

A stable enterprise identifier may be required:

customer_id = "cust_123"

Identity semantics are defined by the owning domain and authoritative source.

⸻

9. Node Attributes

Nodes may contain attributes required to describe their graph semantics.

Typical attributes include:

id
type
name
description
status
scope
source
authority
observed_at
effective_at
valid_from
valid_until
version
provenance
metadata
fact_status

Attributes must have defined semantics and must not become an uncontrolled metadata store.

⸻

10. Relationship

A relationship represents a semantically meaningful connection between two nodes.

Examples:

ACTOR ──BELONGS_TO──> ORGANIZATION
ACTOR ──HAS_IDENTITY──> IDENTITY
ORGANIZATION ──OWNS──> RESOURCE
SYSTEM ──PROVIDES──> CAPABILITY
CAPABILITY ──REQUIRES──> PERMISSION
CAPABILITY ──CONSTRAINED_BY──> POLICY
CAPABILITY ──BOUND_TO──> INTEGRATION
ACTION ──SATISFIES──> INTENT
EXECUTION ──USES──> ACTION

Relationships carry semantic meaning; they are not arbitrary graph edges.

⸻

11. Relationship Direction

Relationships should have explicit direction whenever direction affects semantics.

For example:

SYSTEM ──PROVIDES──> CAPABILITY

is preferable to an undirected connection because the direction establishes the semantic relationship.

Reverse traversal may still be supported by the graph engine, but canonical semantics remain directional.

⸻

12. Relationship Type

Every relationship must have a defined type.

Examples include:

BELONGS_TO
OWNS
HAS_IDENTITY
PROVIDES
REQUIRES
GRANTS
CONSTRAINS
DEPENDS_ON
IMPLEMENTS
BINDS_TO
TRIGGERS
PRECEDES
PRODUCES
OBSERVED_BY
SUPPORTED_BY
AUTHORIZES
EXECUTES

Relationship types form part of the graph ontology.

A relationship type must have stable semantics.

⸻

13. Relationship Semantics

A relationship must answer a specific semantic question.

For example:

SYSTEM ──PROVIDES──> CAPABILITY

means the system exposes or supports the capability.

It does not automatically mean:

Actor can execute Capability

That may additionally require:

Actor
→ Identity
→ Organization / Scope
→ Permission
→ Policy
→ Capability
→ Resource

Graph traversal must therefore preserve semantic distinctions.

⸻

14. Relationship Attributes

Relationships may carry attributes when the relationship itself has relevant state.

Examples:

* scope
* authority
* valid_from
* valid_until
* observed_at
* effective_at
* source
* provenance
* status
* version
* conditions
* fact_status

confidence may exist as interpretation metadata, but model confidence must not be treated as authority or Fact Status.

⸻

15. Relationship as First-Class Information

Some relationships are sufficiently important that they must be modeled as first-class objects rather than implicit connections.

For example:

Actor ──HAS_PERMISSION──> Capability

may require additional information such as:

* granted_by
* grant_time
* expiration
* scope
* conditions
* source
* authority
* validity

In such cases, the relationship itself carries enterprise meaning.

⸻

16. Graph Scope

Every graph claim exists within a defined scope.

Possible scopes include:

* tenant
* organization
* legal_entity
* business_domain
* environment
* resource
* system
* region
* jurisdiction
* time

A graph claim without sufficient scope may be ambiguous or unsafe.

⸻

17. Scope Is Part of Meaning

The statement:

User X can retrieve Account Y

is incomplete without knowing:

* which organization
* which environment
* which account
* which system
* which policy
* which time
* which authority

Scope therefore participates directly in graph semantics.

⸻

18. Authority

Authority identifies which source is authoritative for a particular graph claim.

Authority is claim-specific.

For example:

Banking Core
    → authoritative for account balance
IAM System
    → authoritative for user permission
Policy Repository
    → authoritative for policy definition
Noema
    → authoritative for execution-domain state it owns

No source is automatically authoritative for every fact it contains.

Graph membership itself does not create authority.

⸻

19. Source Versus Authority

A source and an authority are not necessarily the same concept.

A documentation repository may describe a capability without being authoritative for whether that capability is currently enabled.

A system may emit an event without being authoritative for a policy.

The Graph Model therefore distinguishes:

SOURCE
from
AUTHORITY

Source identifies origin.

Authority identifies which source is permitted to establish the relevant claim.

⸻

20. Provenance

Every material graph claim should have sufficient provenance to explain where it originated.

Provenance may identify:

* source system
* document
* API
* schema
* event
* configuration
* administrator
* integration
* discovery process
* reconciliation process
* admission process

Provenance allows graph state to remain explainable and historically reconstructable.

⸻

21. Evidence

Evidence supports graph claims.

A graph should distinguish between:

Claim
Evidence supporting claim
Authority of evidence
Validity of evidence
Fact Status of claim

Evidence may come from:

* APIs
* schemas
* documentation
* configuration
* events
* policies
* human confirmation
* State Reconciliation

Evidence does not automatically establish truth merely because it exists.

⸻

22. Hard Schema Validation and Admission

Graph information must pass the applicable hard schema validation and admission boundary before it becomes canonical graph state.

The canonical boundary is:

Candidate Entity / Relationship
          ↓
Hard Schema Validation
          ↓
Semantic Validation
          ↓
Authority / Provenance Validation
          ↓
Scope / Temporal Validation
          ↓
Admission
          ↓
Canonical Graph State

This boundary applies to information originating from:

* models
* users
* enterprise APIs
* events
* retrieved documentation
* configuration
* integrations
* discovery processes

Structural validity does not establish enterprise authority.

Persistence does not confer authority.

⸻

23. Fact Status

Fact Status describes the current epistemic status of a graph claim.

Canonical values are:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

* Evidence
* Context
* Graph State
* Business State
* Outcome
* model confidence

For example:

Evidence:
    Authoritative system reports capability enabled.
Fact Status:
    VERIFIED

If the authoritative source cannot currently be reached:

Current state:
    unavailable
Fact Status:
    UNKNOWN

Noema must not convert UNKNOWN into a presumed current fact.

⸻

24. Temporal Model

Graph state is temporal.

A fact may have:

* observed_at
* effective_at
* valid_from
* valid_until

These timestamps represent different concepts.

For example:

Permission changed at 09:00
Noema observed the change at 09:05
effective_at = 09:00
observed_at  = 09:05

These values must not be conflated.

Recency does not substitute for authority.

⸻

25. Historical State

The Graph Model must preserve historical meaning where historical graph state affects:

* auditability
* execution reconstruction
* policy evaluation
* incident analysis
* reconciliation
* dispute resolution
* recovery
* replay

A graph update must not erase the ability to understand what the graph represented previously.

⸻

26. Versioning

Graph state is versioned.

A graph version identifies a coherent structural and semantic state of the graph at a particular point in its evolution.

Conceptually:

Graph v41
   │
   ├── Capability A
   ├── Policy P1
   └── Integration I1
Graph v42
   │
   ├── Capability A
   ├── Policy P2
   └── Integration I1

The difference between versions must be reconstructable.

Graph version is distinct from:

* deployment version
* contract version
* policy version
* integration version
* system version
* capability version

⸻

27. Graph Snapshot

A graph snapshot represents the graph state that was valid or observable under a defined version and scope.

Snapshots may be used for:

* deterministic evaluation
* replay
* audit
* debugging
* execution reconstruction
* reconciliation
* recovery

Snapshots do not necessarily duplicate every underlying enterprise business record.

A snapshot is historical graph context, not a replacement for the enterprise System of Record.

⸻

28. Graph Mutation

Graph mutation changes canonical graph state.

Examples include:

ADD
UPDATE
REMOVE
DEPRECATE
RETIRE
SUPERSEDE
RESTORE
MERGE
SPLIT
SCOPE
UNSCOPE
CORRECT

Mutations must be:

* validated
* attributable
* authority-aware
* scope-aware
* temporally valid
* versioned where required

Graph Evolution defines the controlled process for these mutations.

⸻

29. Model Interaction With the Graph

A model may help discover or propose graph information.

It must not directly establish canonical graph truth.

The model may produce:

* Candidate Entity
* Candidate Relationship
* Candidate Capability
* Candidate Mapping
* Candidate Evidence Interpretation

The deterministic graph pipeline must then validate the proposal.

Model Proposal
      ↓
Hard Schema Validation
      ↓
Evidence
      ↓
Authority
      ↓
Scope
      ↓
Temporal Validation
      ↓
Admission
      ↓
Canonical Graph State

The model has no authority to mutate the canonical graph.

⸻

30. Graph Truth and Epistemic State

The graph should distinguish states such as:

PROPOSED
SUPPORTED
VERIFIED
CANONICAL
UNKNOWN
CONFLICTED
DEPRECATED
RETIRED

These states must not be treated as interchangeable.

In particular:

* PROPOSED does not mean established.
* SUPPORTED does not necessarily mean authoritative.
* VERIFIED describes Fact Status, not necessarily lifecycle.
* CANONICAL describes admission into the applicable graph scope.
* UNKNOWN preserves insufficient knowledge.
* CONFLICTED preserves unresolved disagreement.
* DEPRECATED and RETIRED describe lifecycle.

A proposed graph fact must never silently become canonical.

⸻

31. Unknown State

UNKNOWN is a legitimate graph state.

If available evidence is insufficient to establish whether a relationship or capability exists, the graph must preserve that uncertainty.

Capability ──?──> Integration

is preferable to inventing:

Capability ──EXECUTED_BY──> Integration

when the relationship cannot be established.

Unknown graph state may require reconciliation before it can participate in consequential execution.

⸻

32. Conflict State

The graph may encounter conflicting claims.

For example:

System A → Capability enabled
System B → Capability disabled

The graph must not resolve the conflict merely by counting sources.

Resolution depends on:

* authority
* scope
* freshness
* effective time
* claim type
* enterprise policy
* reconciliation semantics

If conflict cannot be deterministically resolved, CONFLICTED must remain explicit.

⸻

33. Canonicality

Canonicality is scoped.

A graph fact may be canonical for:

Tenant A
Environment Production
Resource X
Time T

without being canonical for:

Tenant B
Environment Staging
Resource Y
Time T

Canonicality must therefore always be interpreted within its defined:

* scope
* authority
* temporal validity
* graph version

Canonical does not mean eternally canonical.

⸻

34. Core Node Model

The conceptual node model is:

Node
├── Identity
├── Type
├── Attributes
├── Scope
├── Authority
├── Provenance
├── Temporal Validity
├── Fact Status / State
└── Version

Not every node requires every field, but every field that exists must have defined semantics.

⸻

35. Core Edge Model

The conceptual relationship model is:

Relationship
├── Source Node
├── Target Node
├── Type
├── Scope
├── Authority
├── Provenance
├── Temporal Validity
├── Conditions
├── Fact Status / State
└── Version

The edge must never carry semantics that contradict its relationship type.

⸻

36. Actor Model

An Actor represents an entity capable of expressing Intent or participating in an execution.

Actors may include:

* Human
* Service
* Agent
* System Process
* Organization Representative

Actor identity is distinct from:

* authentication
* credentials
* authorization
* delegation
* effective execution principal

An Agent acting on behalf of a human does not automatically become the human identity.

⸻

37. Organization Model

An Organization represents an enterprise organizational boundary relevant to authority, ownership, policy, permissions, or execution.

Organizations may contain:

* departments
* teams
* business units
* legal entities
* projects
* regions

Organizational relationships must preserve scope and temporal validity.

Membership does not automatically imply authorization.

⸻

38. Identity Model

Identity represents the relationship between an Actor and one or more enterprise-recognized identities.

Identity may be established through:

* identity provider
* directory
* authentication system
* enterprise account
* customer identifier
* service identity

Identity does not itself establish permission.

Authoritative identity resolution must be based on the applicable enterprise authority rather than model inference alone.

⸻

39. Resource Model

A Resource represents an enterprise object that can be referenced, queried, modified, or acted upon.

Examples include:

* Account
* Customer
* Statement
* Transaction
* Order
* Ticket
* Subscription
* Document

Business state belonging to the Resource remains authoritative in the appropriate enterprise System of Record.

A graph Resource reference is not itself the complete business state of that Resource.

⸻

40. System Model

A System represents an enterprise application, platform, service, datastore, or operational subsystem.

Examples:

* CRM
* Core Banking
* ERP
* IAM
* Ticketing System
* Payment Processor
* Data Warehouse

A System may provide capabilities without owning every fact related to those capabilities.

System authority is claim-specific.

⸻

41. Capability Model

A Capability represents a bounded enterprise ability exposed through a defined and governed mechanism.

Examples:

retrieve_account_balance
retrieve_statement
search_transactions
calculate_spending_summary
create_complaint

Capability is distinct from:

* Permission
* Intent
* Action
* Action Contract
* Execution
* Outcome

Capability existence does not imply that it is currently available, permitted, executable, or successful.

⸻

42. Action Model

An Action represents a concrete semantic operation selected from an established Capability.

Conceptually:

Intent
   ↓
Capability
   ↓
Action
   ↓
Action Contract
   ↓
Execution

An Action must remain bounded by the Capability, Action Model, and Action Contract from which it was derived.

The planner cannot invent an Action merely because a model believes an operation would be useful.

⸻

43. Permission Model

Permission represents enterprise authorization to perform a Capability or Action under defined conditions.

Permission does not create Capability.

Capability = possible
Permission = authorized

Both may be required before execution.

Permission itself does not establish Trust or execution success.

⸻

44. Policy Model

Policy represents rules that constrain what may be done, when, how, by whom, and under which conditions.

Policies may constrain:

* actors
* organizations
* capabilities
* actions
* resources
* environments
* risk levels
* approval requirements

Policy is distinct from Permission.

Technical authorization, policy authorization, and business authorization must not be collapsed into a single graph relationship.

⸻

45. Workflow Model

A Workflow represents an ordered or conditional set of enterprise operations.

A Workflow may establish:

* required steps
* dependencies
* ordering
* approval points
* branching
* recovery
* completion conditions

Workflow structure can constrain capability composition and Action planning.

Workflow structure does not itself grant authority.

⸻

46. Event Model

An Event represents an occurrence observed by Noema or an enterprise system.

Events may provide evidence of:

* state changes
* execution outcomes
* configuration changes
* permission changes
* workflow transitions
* external activity

An Event is evidence of an occurrence, not automatically the authoritative state itself.

Event occurrence does not automatically create authorization or an executable Action.

⸻

47. Evidence Model

Evidence represents information used to support a graph claim or execution decision.

Evidence should preserve:

* origin
* content reference
* authority
* observed time
* effective time
* scope
* validity
* integrity
* schema/admission status

Evidence remains evidence even when it is strong.

Fact Status separately describes the status of the claim supported by that evidence.

⸻

48. Contract Model

A Contract represents a formal boundary governing a semantic or executable interaction.

Examples include:

* Action Contract
* Execution Contract
* Context Contract
* Intent Contract
* Trust Contract
* Event Contract

Contracts provide explicit semantics where unconstrained graph traversal would be insufficient.

Graph relationships may reference contracts, but the Graph Model does not absorb the semantic responsibilities of those contracts.

⸻

49. Integration Model

An Integration represents the mechanism through which Noema connects a canonical Capability or Action to an enterprise System.

An Integration may provide:

* API mapping
* authentication
* request transformation
* response normalization
* error mapping
* idempotency
* timeout handling
* reconciliation

Integration is an execution boundary, not the definition of enterprise Capability itself.

Provider endpoint identity is not automatically Capability identity.

⸻

50. Environment Model

An Environment identifies the operational context in which a graph claim or Capability exists.

Examples:

* development
* staging
* production
* sandbox
* region
* tenant-specific deployment

A Capability existing in staging does not establish that it exists in production.

Environment is therefore part of graph scope whenever it affects semantics or executability.

⸻

51. Domain Model

A Domain represents a bounded enterprise or semantic area.

Examples:

* Accounts
* Payments
* Customer Support
* Identity
* Orders
* Billing
* Compliance

Domains help constrain graph traversal, authority, policies, and Capability interpretation.

⸻

52. Graph Traversal

Graph traversal is the process of following valid relationships to establish whether a path exists between relevant entities.

A valid traversal must respect:

* relationship semantics
* scope
* authority
* permissions
* policy
* temporal validity
* graph version
* environment
* Fact Status
* unresolved or conflicting state

Traversal must never treat mere connectivity as authorization.

⸻

53. Executability Path

A graph path can establish an executable route only when required constraints are satisfied.

Conceptually:

Actor
  ↓
Identity
  ↓
Organization / Scope
  ↓
Resource
  ↓
Capability
  ↓
Permission
  ↓
Policy
  ↓
Action
  ↓
Action Contract
  ↓
Integration
  ↓
Enterprise System

The actual path may vary by Workflow and domain.

Graph connectivity alone does not establish executability.

⸻

54. Graph-Constrained Action Selection

Action selection must be constrained by established graph reality.

The model may propose:

retrieve_balance

The graph and applicable enterprise sources must establish the relevant:

* Capability
* Resource
* Actor
* Scope
* Permission
* Policy
* System
* Integration
* Contract
* current state

Only then can the Action proceed through deterministic Trust and execution controls.

The planner cannot invent missing graph capabilities or authority.

⸻

55. Graph and Trust

The graph provides structural inputs required by the Trust Engine.

Trust may evaluate:

* Who is acting?
* What Action or Capability is requested?
* What Resource is involved?
* What Permissions apply?
* Which Policy governs the operation?
* Which Environment is targeted?
* What Evidence supports the claims?
* What Fact Status applies?
* What uncertainty remains?
* Which Capability and Action Contract are available?

The graph does not replace Trust.

It provides structured enterprise context against which Trust operates.

Canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Graph states such as UNKNOWN, UNAVAILABLE, or CONFLICTED are not additional Trust outcomes.

⸻

56. Graph and Intent

Intent expresses what the source of Intent wants to accomplish.

The graph provides the enterprise structure required to resolve whether that Intent maps to an executable operation.

Intent
   ↓
Graph Resolution
   ↓
Capability
   ↓
Action
   ↓
Trust
   ↓
Execution

The graph does not become the Intent itself.

A material change to the semantic interpretation of an admitted Intent creates a new Intent version rather than silently mutating the existing one.

⸻

57. Graph and Context

Context supplies information required to resolve graph references.

Examples:

* Which account?
* Which organization?
* Which environment?
* Which customer?
* Which transaction?
* Which timeframe?

Context may resolve otherwise ambiguous graph references.

Context is not automatically authoritative merely because it contains a graph reference.

⸻

58. Graph and State Reconciliation

State Reconciliation is a first-class mechanism for determining whether current enterprise observations support graph claims.

Conceptually:

Enterprise Systems / Sources
          ↓
Observations
          ↓
Hard Schema Validation / Admission
          ↓
State Reconciliation
          ↓
Reconciled Claims / Fact Status
          ↓
Graph Evaluation
          ↓
Graph Mutation if established

This is particularly important for:

* current Capability availability
* System ownership
* Resource relationships
* Permission state
* organizational membership
* integration status
* authoritative bindings

The graph must not treat stale or cached state as current merely because it is present.

⸻

59. Graph and Execution

Execution consumes graph-derived structure but does not redefine graph semantics.

Execution may reference:

* graph_version
* capability_id
* action_id
* integration_id
* policy_version
* contract_version
* resolved resource
* resolved actor
* scope

This allows execution to be reconstructed against the graph state used at decision time.

⸻

60. Graph and Outcome

Execution outcomes may generate new Evidence that changes graph knowledge.

For example:

Integration reports capability unavailable
        ↓
Evidence generated
        ↓
Graph capability state evaluated
        ↓
State Reconciliation initiated

Execution therefore contributes observations to graph evolution without automatically redefining canonical truth.

Outcome remains distinct from enterprise Business State.

⸻

61. Graph and Reconciliation

Reconciliation compares graph claims against authoritative enterprise sources.

It may detect:

* missing Capability
* stale Permission
* changed Policy
* removed Integration
* Resource mismatch
* unexpected configuration
* changed System ownership

Reconciliation is a mechanism for maintaining graph integrity.

It is not an excuse to silently overwrite historical graph state.

⸻

62. Graph and Recovery

Recovery depends on graph structure.

A failed or unknown execution may require determining:

* alternative Capability
* alternative Integration
* recovery Workflow
* required approval
* current Permission
* current Policy
* current Resource state

Recovery must use graph state applicable to the recovery decision rather than blindly replaying stale assumptions.

The planner must not invent an alternative capability or authority.

⸻

63. Graph and Determinism

The graph is a deterministic substrate after canonicalization and admission.

The model may produce probabilistic interpretations, but graph validation must determine whether proposed entities and relationships are established.

Probabilistic Proposal
        ↓
Deterministic Graph Validation
        ↓
Canonical / Unknown / Conflict

Given the same applicable canonical inputs, scope, graph version, and rules, graph semantics must be deterministic.

⸻

64. Graph Query Semantics

Graph queries must have explicit semantic intent.

Examples:

* Find capabilities available to Actor X.
* Find Systems providing Capability Y.
* Find Policies constraining Capability Y.
* Find Integrations capable of executing Action Z.
* Find authoritative source for Resource R.
* Find current organizational scope for Actor X.

Queries must distinguish between:

existence
availability
authorization
authority
executability
current state
historical state

These are different questions.

⸻

65. Graph Integrity

Graph integrity requires:

* valid node identity
* valid relationship types
* valid references
* scope consistency
* authority consistency
* temporal consistency
* version consistency
* provenance availability
* Fact Status consistency
* semantic consistency

An internally connected graph is not necessarily an accurate graph.

⸻

66. Referential Integrity

Every relationship must reference valid nodes or explicitly represent an unresolved external reference.

The graph must not contain silently broken references.

If an external entity cannot currently be resolved:

UNKNOWN_EXTERNAL_REFERENCE

may be preferable to fabricating a node.

An unresolved reference must not be treated as an established Resource, Actor, System, or Capability.

⸻

67. Semantic Integrity

Graph entities and relationships must preserve ontology distinctions.

For example:

Capability ≠ Permission
Permission ≠ Policy
Action ≠ Capability
Execution ≠ Action
Event ≠ State
Evidence ≠ Truth
Source ≠ Authority
Outcome ≠ Business State
Fact Status ≠ Evidence

Collapsing these distinctions creates unsafe execution semantics.

⸻

68. Security Boundary

Graph access must respect enterprise security boundaries.

Graph queries may expose sensitive structural information even when they do not expose business records.

Therefore access controls may be required for:

* node visibility
* relationship visibility
* attribute visibility
* graph traversal
* provenance
* policy information
* permission information
* system topology
* integration metadata

The model must not receive unrestricted graph access merely because graph data is structurally represented.

⸻

69. Privacy Boundary

The Graph Model should minimize unnecessary personal or sensitive data.

Where a graph relationship can be represented without copying underlying sensitive business data, Noema should prefer the reference rather than duplication.

Noema Graph
     │
     └── resource_ref ──> Enterprise System

rather than unnecessarily storing the full Resource record.

Graph history must not become an uncontrolled historical copy of enterprise databases.

⸻

70. Performance

The Graph Model must support efficient resolution of common execution paths.

Performance optimizations may include:

* indexes
* materialized projections
* cached relationships
* precomputed traversals
* partitioning
* graph snapshots

Optimization must not alter canonical semantics, authority, temporal validity, or Fact Status.

⸻

71. Caching

Cached graph information must retain:

* source
* authority
* scope
* observed_at
* effective_at
* version
* validity
* Fact Status

A cache entry must never be treated as permanently current merely because it exists.

When freshness is material to execution, current state must be reconciled against the applicable authoritative source.

⸻

72. Materialized Projections

The graph may expose specialized projections for particular workloads.

Examples:

* Capability Graph
* Permission Graph
* Enterprise Action Graph
* Workflow Graph
* Integration Graph

These projections are derived representations.

They must remain traceable to canonical graph semantics and must not silently acquire independent authority.

⸻

73. Enterprise Action Graph

The Enterprise Action Graph is an executable-oriented projection of the broader Enterprise Graph.

Conceptually:

Enterprise Graph
       │
       ├── organizational structure
       ├── systems
       ├── resources
       ├── policies
       ├── evidence
       └── capabilities
              │
              ▼
     Enterprise Action Graph
              │
              ├── capabilities
              ├── permissions
              ├── policies
              ├── dependencies
              ├── contracts
              ├── integrations
              └── execution paths

The Enterprise Action Graph does not replace the Enterprise Graph.

It is a bounded executable projection used by Trust, planning, and execution.

⸻

74. Graph Evolution Boundary

Changes to graph structure are governed by the Graph Evolution model.

The Graph Model defines what the graph means.

Graph Evolution defines how graph state changes over time.

Graph Model
    │
    │ defines structure and semantics
    ▼
Graph State
    │
    │ changes through governed
    ▼
Graph Evolution

Neither should silently redefine the other.

⸻

75. Graph as a Deterministic Substrate

Once graph facts have been canonicalized, downstream systems should be able to reason over them deterministically.

Given:

same graph version
+
same scope
+
same authority
+
same applicable policy state
+
same input

the graph query should produce the same semantic result.

Where inputs are UNKNOWN or CONFLICTED, the deterministic result must preserve that epistemic state rather than inventing certainty.

⸻

76. Graph Model Invariants

The following invariants are mandatory:

1. Every canonical node has a defined identity.
2. Every relationship has a defined semantic type.
3. Relationships must not imply semantics they do not explicitly represent.
4. Graph scope is part of graph meaning.
5. Authority is claim-specific.
6. Source and authority are distinct concepts.
7. Material claims must have sufficient provenance.
8. Temporal validity must be explicit where time affects meaning.
9. effective_at and observed_at must not be conflated.
10. Historical graph state must remain interpretable.
11. Graph versions must be reconstructable.
12. Graph mutations must be attributable.
13. Hard schema validation must precede canonical graph admission.
14. Persistence must not confer authority.
15. Model proposals are not canonical graph truth.
16. Model confidence is not enterprise authority or Fact Status.
17. Fact Status is distinct from Evidence, Context, Business State, Graph State, and Outcome.
18. Canonical Fact Status values are VERIFIED, UNVERIFIED, STALE, CONFLICTED, and UNKNOWN.
19. UNKNOWN is a valid graph state.
20. Conflicting claims must not be resolved by source count alone.
21. Canonicality is scoped and temporal.
22. Enterprise systems remain authoritative for their business state.
23. The graph must not become shadow business state.
24. Capability is distinct from Permission.
25. Permission is distinct from Policy.
26. Capability is distinct from Action.
27. Action is distinct from Execution.
28. Event is distinct from business state.
29. Evidence is distinct from Fact Status.
30. Source is distinct from Authority.
31. Outcome is distinct from enterprise Business State.
32. Graph connectivity does not imply authorization.
33. Graph connectivity does not imply executability.
34. Traversal must respect scope.
35. Traversal must respect temporal validity.
36. Traversal must respect applicable Policy.
37. Traversal must respect Permission.
38. Traversal must respect graph version.
39. Traversal must respect unresolved and conflicting state.
40. Environment must be respected when environment affects Capability availability.
41. External references must not be fabricated.
42. Graph projections must remain traceable to canonical semantics.
43. Caches must preserve graph validity metadata.
44. Optimizations must not alter graph semantics.
45. Graph changes must preserve prior execution interpretability.
46. Execution must reference the graph state used for material decisions.
47. Reconciliation must preserve evidence of discrepancies.
48. State Reconciliation must be used where current enterprise state is required to establish or validate a graph claim.
49. Graph mutation must be deterministic after validation and admission.
50. Canonical graph state must be explainable through provenance and applicable authority.
51. Graph semantics must remain stable across implementation changes unless explicitly versioned.
52. Noema must not silently redefine enterprise truth.
53. In-flight Executions must not silently switch graph semantics.
54. Pending Actions may require deterministic revalidation after material graph changes.
55. Historical replay must use historically applicable graph state.
56. Replay must not recreate enterprise side effects.
57. Material graph decisions must preserve the exact Intent version when they affect consequential execution.
58. Admitted Intent versions are immutable; material changes create a new Intent version with supersedes.
59. Resolved Actor, Action, Target, Resource, and scope must not be silently substituted because of graph evolution.
60. Planner behavior must remain bounded by the Enterprise Action Graph, Capability Registry, Action Model, and Action Contracts.
61. Graph membership must not grant permission, authorization, or Trust.
62. Trust outcomes remain exactly EXECUTE, CLARIFY, ESCALATE, and REJECT.
63. Trust EXECUTE must not be interpreted as execution success.
64. Graph Capability availability must not be interpreted as execution success.
65. Security-sensitive graph access and mutations must respect applicable authorization and data boundaries.
66. Operational Memory and graph journals are historical records, not enterprise business-state authority.
67. Read-only graph paths may still be consequential and require appropriate Trust and data-boundary controls.
68. Graph Evolution must preserve the distinction between what was known, what is known, and what is merely proposed or suspected.
69. Graph state must not silently convert UNKNOWN or CONFLICTED claims into established facts.
70. Noema must never turn model imagination into enterprise fact.

⸻

77. Conceptual Graph

The core Noema graph can be represented as:

                         ┌──────────────┐
                         │ Organization │
                         └──────┬───────┘
                                │
                              owns
                                │
                                ▼
                         ┌──────────────┐
                         │   Resource   │
                         └──────┬───────┘
                                │
                             exists in
                                │
                                ▼
                         ┌──────────────┐
                         │    System    │
                         └──────┬───────┘
                                │
                            provides
                                │
                                ▼
                         ┌──────────────┐
                         │  Capability  │
                         └──────┬───────┘
                         ┌──────┴──────┐
                      requires       constrained by
                         │               │
                         ▼               ▼
                  ┌────────────┐   ┌────────────┐
                  │ Permission │   │   Policy   │
                  └────────────┘   └────────────┘
                         │
Actor ──identity──> Identity
  │
  └───────────────> Organization
Capability
     │
     ├──bound to──────> Integration
     │
     ├──governed by───> Contract
     │
     └──participates──> Workflow

This structure is illustrative rather than exhaustive.

⸻

78. Graph as Execution Infrastructure

The Graph Model provides the structural substrate between interpretation and execution.

Source of Intent
    ↓
Intent
    ↓
Context / State Reconciliation
    ↓
Graph Resolution
    ↓
Capability
    ↓
Trust
    ↓
Action
    ↓
Action Contract
    ↓
Execution
    ↓
Enterprise System
    ↓
Verification
    ↓
Outcome
    ↓
Graph Evidence / Evolution

The graph therefore connects understanding of enterprise structure to safe execution without becoming the owner of enterprise business truth.

⸻

79. Implementation Independence

The Graph Model defines semantics independently of the underlying graph technology.

Noema may use:

* property graph
* RDF
* graph database
* relational projection
* hybrid graph storage

provided the implementation preserves the canonical semantics defined here.

The storage engine is an implementation detail.

⸻

80. Graph Portability

Graph semantics should remain portable across implementations.

A graph migration must preserve:

* identity
* relationship semantics
* scope
* authority
* provenance
* temporal validity
* version
* Fact Status
* lifecycle state

Changing storage technology must not silently change graph meaning.

⸻

81. Relationship to Canonical Data

The Graph Model defines how entities and relationships are structurally represented.

The Canonical Data model defines how canonical data is represented and governed.

They are complementary:

Canonical Data
      │
      ▼
Graph Nodes / Attributes
      │
      ▼
Graph Relationships
      │
      ▼
Enterprise Structure

Neither should silently absorb the responsibilities of the other.

Graph structure does not transfer authority over enterprise business data to Noema.

⸻

82. Relationship to Graph Evolution

The Graph Model defines the stable conceptual vocabulary of the graph.

Graph Evolution defines controlled change to graph state.

Graph Model
= What the graph means
Graph Evolution
= How graph state changes under governance

Both are required for a trustworthy graph substrate.

⸻

83. Relationship to Capability Model

The Capability Model defines what a Capability means and how Capabilities behave as executable enterprise abstractions.

The Graph Model defines how Capabilities participate in the broader enterprise structure.

Therefore:

Capability Model
        +
Graph Model
        ↓
Capability as Graph Node

This allows Capability discovery and execution planning to remain graph-constrained.

⸻

84. Relationship to Enterprise Graph

The Enterprise Graph is the canonical graph constructed according to this model.

The Graph Model defines its structural semantics.

Graph Model
     ↓
Enterprise Graph
     ↓
Enterprise Action Graph
     ↓
Trust / Planning
     ↓
Execution

The Enterprise Graph therefore cannot introduce relationship semantics that contradict the Graph Model.

⸻

85. Final Definition

The Noema Graph Model is the canonical structural model for representing enterprise reality as a connected, scoped, versioned, temporal, authority-aware, and provenance-aware graph.

It defines the entities, relationships, attributes, constraints, evidence, Fact Status, and semantic boundaries required for Noema to reason about:

* Actors
* Organizations
* Identities
* Resources
* Systems
* Capabilities
* Permissions
* Policies
* Workflows
* Integrations
* Contracts
* Evidence
* Execution structure

The Graph Model enables Noema to move from:

Source of Intent
      ↓
Admitted Intent
      ↓
Enterprise Context
      ↓
Graph Resolution
      ↓
Capability / Action
      ↓
Deterministic Trust
      ↓
Bounded Execution

while preserving a fundamental boundary:

Noema models enterprise reality. Enterprise systems remain authoritative for enterprise business truth.

The graph is therefore not a database of everything the enterprise knows.

It is the governed structural substrate through which Noema can represent what exists, how it is related, what is possible, what is permitted, what is authoritative, what is established, what is unknown, what is conflicted, and what can safely participate in execution.

Its central invariant is:

The graph may structure enterprise reality, but it must never manufacture enterprise truth.