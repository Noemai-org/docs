Here is the actual updated file. I’ve kept the 69-section canonical structure, but tightened the definitions and removed places where the integration layer could accidentally become a second semantic/action authority.

Integration Model

Status: Foundational
Version: 0.2
Domain: Product
Canonical Path: product/integration-model.md

⸻

1. Definition

An Integration is the controlled boundary through which Noema connects to an external enterprise system in order to discover, retrieve, observe, and execute capabilities against enterprise-owned Business State.

The Integration Model answers:

“How does Noema safely interact with systems that own enterprise capabilities and Business State?”

Noema does not exist in isolation.

It operates across enterprise systems such as:

* Identity Systems
* Customer Systems
* Payment Systems
* HR Systems
* CRM Systems
* ERP Systems
* Communication Systems
* Internal APIs
* Databases
* Event Systems

The Integration Model defines how these systems become controlled execution surfaces within Noema without transferring ownership of their underlying Business State to Noema.

Conceptually:

Enterprise Systems
        │
        ▼
    Integrations
        │
        ▼
      Noema
        │
        ├── Intent
        ├── Context
        ├── Evidence
        ├── Trust
        ├── Action
        └── Execution

Noema coordinates execution.

Enterprise systems remain authoritative for their respective domains.

⸻

2. Purpose

The purpose of the Integration Model is to establish a consistent semantic and execution abstraction for interacting with heterogeneous enterprise systems.

Enterprise systems differ in:

* protocols
* APIs
* authentication
* data models
* schemas
* error semantics
* consistency guarantees
* event models
* availability
* versioning
* authorization models

Noema should not expose these implementation differences directly to Intent.

Instead:

Enterprise System
      ↓
Integration
      ↓
Capability
      ↓
Action Contract
      ↓
Trust
      ↓
Execution

The Integration Model therefore provides the boundary between:

Noema’s semantic execution model

and:

enterprise-specific implementation.

The boundary may hide implementation details, but must not hide the guarantees required for safe execution.

⸻

3. Integration Boundary

An Integration is the controlled boundary through which Noema interacts with an external system.

Conceptually:

Noema
  │
  ▼
Integration Boundary
  │
  ▼
Enterprise System

The boundary defines or exposes:

* available capabilities
* input requirements
* authentication
* authorization
* schemas
* transport
* errors
* state semantics
* consistency guarantees
* events
* observability
* provenance
* execution guarantees

Noema should interact through the defined Integration boundary rather than making assumptions about the underlying system.

⸻

4. Integration vs System

An Integration is not the enterprise system itself.

Enterprise System
       │
       ▼
   Integration
       │
       ▼
      Noema

The enterprise system owns the business domain.

The Integration provides controlled access to that domain.

For example:

Payment System
      ↓
Payment Integration
      ↓
     Noema

Noema does not become the Payment System merely because it can invoke its capabilities or observe its state.

⸻

5. Integration vs Capability

A System exposes capabilities.

An Integration exposes those capabilities to Noema through a controlled executable boundary.

For example:

Payment System
    │
    ├── get_payment
    ├── refund_payment
    └── cancel_payment
            │
            ▼
    Payment Integration
            │
            ▼
          Noema

The Integration translates between the enterprise system’s implementation and Noema’s semantic execution model.

A discovered endpoint is not automatically a trusted Capability.

⸻

6. Integration vs Action

An Action represents the semantic operation Noema intends to cause.

An Integration provides the mechanism through which that Action may be executed against a particular enterprise system.

Therefore:

Intent
  ↓
Action
  ↓
Integration
  ↓
Enterprise System

The Action answers:

What operation is Noema attempting to cause?

The Integration answers:

Through which enterprise boundary can that operation be executed?

The Integration must not independently redefine the semantic Action.

⸻

7. Integration vs Action Contract

An Action Contract defines the executable requirements of an Action.

The Integration implements or exposes the enterprise mechanism required to satisfy that contract.

Conceptually:

Action Contract
      ↓
Integration Capability
      ↓
Enterprise Operation

The Integration must provide sufficient guarantees for the Action Contract to remain meaningful.

Where the enterprise system cannot satisfy the required contract semantics, the Integration must not silently claim compatibility.

⸻

8. Integration as a Translation Boundary

Enterprise APIs commonly expose implementation-specific concepts.

For example:

POST /v3/customers/9281/cards/123/replacement

Noema should reason semantically about:

replace_card

The Integration translates:

Noema Action
    ↓
Integration Mapping
    ↓
Enterprise API Operation

This prevents enterprise-specific API details from leaking into the Intent model.

⸻

9. Integration Contract

Each executable Integration should expose a contract describing what Noema can rely upon.

Conceptually:

IntegrationContract {
    identity
    capabilities
    schemas
    authentication
    authorization
    preconditions
    postconditions
    consistency
    idempotency
    retry_semantics
    errors
    events
    provenance
    observability
    lifecycle
    version
}

The exact representation may vary.

The semantic guarantees must remain explicit.

⸻

10. Capability Discovery

Noema may discover potential capabilities from:

* API specifications
* API schemas
* documentation
* configuration
* workflow definitions
* event schemas
* enterprise metadata
* explicit human configuration

Conceptually:

Enterprise Sources
      ↓
Integration Knowledge
      ↓
Potential Capabilities
      ↓
Capability Validation
      ↓
Executable Capabilities
      ↓
Action Contracts

Capability discovery must not be confused with unrestricted autonomous invention of Actions.

Discovery produces candidates.

Validation establishes whether they are executable.

⸻

11. Capability Registration

Capabilities may be explicitly registered with Noema.

Example:

Capability:
refund_payment
System:
Payment Platform
Inputs:
payment_id
amount
reason
Preconditions:
payment.status = CAPTURABLE
Postcondition:
refund.status = CREATED

Registration creates an explicit executable boundary.

Registration alone does not bypass Trust, Authority, Policy, or Action Contract requirements.

⸻

12. Capability Identity

Capabilities should have stable semantic identities.

Examples:

refund_payment
replace_card
freeze_card
create_invoice
suspend_employee

The underlying enterprise endpoint may change.

The semantic Capability should remain stable where its meaning and execution guarantees remain compatible.

⸻

13. Integration Identity

Each Integration should have a stable identity.

Conceptually:

Integration {
    integration_id
    system_id
    version
    environment
    tenant_scope
}

This allows Noema to distinguish:

Production Payment System

from:

Staging Payment System

and:

Tenant A Payment System

from:

Tenant B Payment System

⸻

14. Environment Boundaries

Integrations must preserve environment boundaries.

For example:

Production
    ↓
Production Integration

and:

Staging
    ↓
Staging Integration

Noema must not accidentally execute a Production Action against a staging or development system, or vice versa.

Environment must therefore be explicit wherever it affects execution authority or semantics.

⸻

15. Tenant Boundaries

Integrations must preserve tenant boundaries.

For example:

Tenant A
   ↓
Integration A
   ↓
Enterprise System A

must not implicitly access:

Tenant B

Integration identity, credentials, authorization, and execution scope must preserve the applicable tenant boundary.

⸻

16. Authentication

An Integration must define how Noema authenticates to the target system.

Possible mechanisms include:

* API keys
* OAuth
* service accounts
* mTLS
* signed requests
* delegated credentials
* workload identity

Authentication establishes:

“Who is making the request to the external system?”

Authentication alone does not establish authorization.

⸻

17. Authorization

Integration authorization establishes whether the authenticated principal may perform the requested operation.

Conceptually:

Identity
   ↓
Authentication
   ↓
Authorization
   ↓
Capability

Noema must distinguish:

Who are we?

from:

What are we allowed to do?

Integration authorization does not replace Noema’s Authority model.

It is one layer of the overall authorization boundary.

⸻

18. Delegated Authorization

Some enterprise operations execute on behalf of a user.

Conceptually:

User
 ↓
Noema
 ↓
Delegated Authority
 ↓
Enterprise System

The Integration must preserve the distinction between:

* Noema’s identity
* initiating user’s identity
* delegated authority
* target enterprise resource

This is particularly important for consequential Actions.

⸻

19. Credential Isolation

Credentials must not become part of Intent or model-visible Context unnecessarily.

The semantic execution path is:

Intent
   ↓
Action
   ↓
Trust
   ↓
Integration
   ↓
Credential Resolution
   ↓
Enterprise System

Credentials remain within the appropriate secure execution boundary.

The model should not need access to credentials merely to determine an Action.

⸻

20. Input Mapping

The Integration maps Noema Action inputs to enterprise-specific inputs.

Example:

Noema:
customer_id = C123
Enterprise API:
customerId = "C123"

Mapping may include:

* field renaming
* type conversion
* identifier translation
* schema transformation
* formatting

Mapping must preserve semantic meaning.

An Integration must not silently change the meaning of an Action input.

⸻

21. Output Mapping

Enterprise responses must be translated back into Noema’s semantic model.

Example:

Enterprise API:
status = "replacement_requested"

may map to:

Action Outcome:
replacement_requested

Where the response represents enterprise state rather than merely an execution response, Noema must preserve that distinction.

Transport success is not automatically a Business Outcome.

⸻

22. Schema Management

Integrations must account for schema versions.

Example:

Payment API v1
Payment API v2
Payment API v3

Noema should know which schema and Capability version an Integration implements.

Schema changes must not silently alter the meaning of an Action Contract.

⸻

23. Integration Versioning

An Integration may be versioned independently from the enterprise system.

For example:

Payment Integration v1
Payment Integration v2

Versioning may represent:

* API changes
* semantic changes
* authentication changes
* capability changes
* mapping changes
* execution guarantees
* consistency guarantees

Noema should preserve compatibility where required.

⸻

24. Capability Versioning

Capabilities may also change over time.

For example:

refund_payment v1
refund_payment v2

A Capability version must represent meaningful semantic or execution-contract changes.

A version change must not silently modify an existing Action’s behavior.

⸻

25. Preconditions

Integrations may expose information required to evaluate Preconditions.

Example:

Action:
refund_payment
Precondition:
payment.status = CAPTURED

The Integration may retrieve the relevant authoritative enterprise State.

Conceptually:

Integration
    ↓
Enterprise State
    ↓
State Resolution
    ↓
Precondition Evaluation

The Integration provides access to State.

It does not decide whether the State satisfies the overall Trust requirement.

⸻

26. Postconditions

Integrations may expose the authoritative State required to verify Postconditions.

Example:

Action:
freeze_card
Expected State:
card.status = FROZEN

Noema may execute:

Integration
    ↓
freeze_card

and then verify:

Integration
    ↓
Authoritative Card State
    ↓
Postcondition

This connects the Integration Model directly to Noema’s canonical State model.

⸻

27. Read Operations

Not every Integration interaction causes state change.

Read operations may retrieve:

* identity
* resources
* State
* configuration
* policy
* capabilities
* historical information

Reads provide Context and Evidence for execution.

Conceptually:

Integration
    ↓
Read
    ↓
Enterprise State / Data
    ↓
Observation
    ↓
Evidence / Context

A read must not be represented as a mutation merely because it participates in an execution.

⸻

28. Write Operations

Write operations may change enterprise Business State.

Examples:

* create_payment
* refund_payment
* freeze_card
* close_account
* update_employee

Consequential writes require stronger execution guarantees than ordinary reads.

They should be governed by applicable:

* Authority
* authorization
* Policy
* Preconditions
* idempotency
* risk requirements
* Postconditions
* auditability

⸻

29. Idempotency

Integrations should expose idempotency semantics for consequential operations where the target system supports them.

Example:

refund_payment
idempotency_key = execution-123

If execution is retried:

Retry
   ↓
Same Idempotency Key
   ↓
Same Logical Operation

Noema must not assume that retrying an external write is safe without understanding the Integration’s semantics.

⸻

30. Retry Semantics

Integration failures must distinguish between:

SAFE_TO_RETRY
UNSAFE_TO_RETRY
UNKNOWN

Examples:

Network timeout
→ outcome unknown
Validation error
→ retry unlikely to help
Rate limit
→ retry may be appropriate
Duplicate request
→ depends on idempotency semantics

Retry behavior must be governed by the Action Contract and Integration guarantees.

⸻

31. Unknown Outcome

A timeout after a write does not necessarily mean that the Action failed.

Example:

Noema
   ↓
Enterprise System
   ↓
Action executed
   ↓
Response lost
   ↓
Noema

The correct state may be:

Outcome = UNKNOWN

Noema should reconcile against authoritative enterprise State where possible.

Unknown must remain distinct from failure.

⸻

32. Error Semantics

Integrations should normalize enterprise errors into meaningful execution states.

Examples:

INVALID_INPUT
UNAUTHORIZED
FORBIDDEN
NOT_FOUND
CONFLICT
RATE_LIMITED
UNAVAILABLE
TIMEOUT
UNKNOWN

The normalized error must preserve sufficient underlying information for diagnosis, Trust, Policy, and Execution decisions.

⸻

33. Error Classification

An error should indicate whether it is:

* deterministic
* transient
* authorization-related
* policy-related
* resource-related
* dependency-related
* consistency-related
* unknown

This classification may affect:

* retry
* clarification
* escalation
* compensation
* reconciliation
* final Outcome

⸻

34. Partial Execution

An Integration may execute part of a compound operation before failure occurs.

Example:

Action A
   ↓
Succeeded
Action B
   ↓
Failed

Noema must preserve the execution state of each operation.

It must not represent the entire compound Intent simply as:

FAILED

without preserving the partial execution history and resulting enterprise State.

⸻

35. Integration Events

Enterprise systems may emit events describing state changes.

Example:

Payment System
      ↓
payment.refunded
      ↓
Event Infrastructure
      ↓
Noema

Events can provide Evidence and help reconcile Execution State.

Events do not automatically replace authoritative State queries.

⸻

36. Eventual Consistency

An Integration may expose eventually consistent data.

For example:

Write
  ↓
System of Record
  ↓
Event
  ↓
Projection
  ↓
Read

The read may temporarily reflect an older State.

Noema must understand the consistency semantics before treating the result as sufficient Evidence for consequential execution.

⸻

37. Consistency Contract

An Integration should describe relevant consistency guarantees.

Examples:

* Strongly Consistent
* Eventually Consistent
* Read-After-Write
* Versioned
* Snapshot-Based

The required consistency level depends on the Action Contract and consequence of stale information.

⸻

38. Integration Availability

An Integration may be unavailable even when Noema itself is operational.

Example:

Noema
  ↓
Payment Integration
  ↓
Payment System
  ↓
Unavailable

Noema must represent this as an external dependency condition rather than automatically treating it as an Intent failure.

⸻

39. Integration Health

Integration health may include:

* availability
* latency
* error rate
* authentication status
* dependency status
* schema compatibility
* event delivery health

Health information may influence execution decisions where explicitly governed.

Health must not independently override Action-level Policy or Trust requirements.

⸻

40. Integration Observability

Integration execution should produce sufficient telemetry to diagnose failures.

Relevant information may include:

integration_id
capability
execution_id
request_id
correlation_id
timestamp
latency
result
error

Sensitive payloads and credentials must not be logged indiscriminately.

Observability must support reconstruction without violating data-minimization requirements.

⸻

41. Integration Provenance

Noema should preserve provenance concerning information obtained through Integrations.

For example:

Source:
Payment System
Observed:
payment.status = CAPTURED
Observed At:
T1
Version:
42

This supports:

* Evidence
* State Resolution
* Trust
* Auditability
* reconciliation
* historical reconstruction

⸻

42. Integration and Evidence

Integration observations can become Evidence.

Conceptually:

Enterprise System
      ↓
Integration
      ↓
Observation
      ↓
Evidence
      ↓
Trust

The Integration establishes how the information was obtained.

Evidence establishes how that information supports a decision.

The two concepts must remain distinct.

⸻

43. Integration and Context

Integration results may populate Context.

Example:

User Intent
    ↓
Integration
    ↓
Account Data
    ↓
Context

Context may contain both canonical and non-canonical information.

Noema must preserve the authority, timestamp, source, and provenance of underlying information where those characteristics matter.

Canonical enterprise State should remain independently addressable rather than being buried inside an opaque Context object.

⸻

44. Integration and Trust

Trust may depend on information retrieved through an Integration.

For example:

Integration
    ↓
Canonical Account State
    ↓
Evidence
    ↓
Trust Evaluation

The reliability, authority, freshness, and consistency characteristics of the Integration affect the Evidence available to the Trust Engine.

The Integration does not itself make the Trust decision.

⸻

45. Integration and Policy

Policies may determine whether an Integration can be used for a particular Action.

For example:

Action:
transfer_funds
Policy:
Only Production Payment Integration
may execute this Action.

An Integration is therefore not merely a technical transport mechanism.

It is part of the executable trust boundary.

⸻

46. Integration and Risk

Different Integrations may have different risk characteristics.

For example:

Read-only Integration
→ lower execution consequence
Financial Write Integration
→ higher execution consequence

Risk evaluation should account for:

* Capability
* Action
* Resource
* Authority
* Integration
* environment
* tenant
* potential State transition
* consequence

Risk does not replace Policy or Authority.

⸻

47. Integration and Human Intervention

An Integration failure may require human intervention.

Example:

Enterprise System
      ↓
Ambiguous Error
      ↓
Noema
      ↓
Human Intervention

Noema should preserve enough execution context for the human to understand:

* what Intent was resolved
* what Action was selected
* what Trust decision occurred
* what Integration was used
* what was attempted
* what was observed
* what remains unknown
* what next action is possible

⸻

48. Integration and Compensation

Compensation must execute through appropriate enterprise capabilities.

If:

Action A
→ Enterprise State Changed

and compensation is required:

Compensation
    ↓
Integration
    ↓
Enterprise Capability

Noema must not compensate by mutating an internal copy of enterprise Business State.

Compensation itself is an Action subject to its own Authority, Policy, Trust, Preconditions, and execution semantics.

⸻

49. Integration and System of Record

The Integration provides controlled access to a System of Record.

It does not replace that System of Record.

Conceptually:

System of Record
      ↓
Integration
      ↓
Noema

Enterprise authority remains with the appropriate enterprise system.

Noema may maintain execution and intent state without claiming ownership of the underlying business State.

⸻

50. Multiple Integrations

Noema may integrate multiple systems representing the same logical domain.

Example:

Customer
   │
   ├── CRM Integration
   ├── Billing Integration
   └── Support Integration

Each Integration may be authoritative for different facts.

Noema must not assume that one Integration is globally canonical.

Authority is fact- and domain-specific.

⸻

51. Integration Conflicts

Two Integrations may return conflicting information.

Example:

CRM:
customer.status = ACTIVE
Billing:
customer.status = SUSPENDED

Noema must determine:

* which system is authoritative for the relevant fact;
* whether the values describe different concepts;
* whether one value is stale;
* whether consistency guarantees differ;
* whether reconciliation is required.

Noema must preserve unresolved conflict rather than silently selecting a value through probabilistic preference.

⸻

52. Integration Discovery and EAG

Enterprise Action Graph construction may use Integration information.

Conceptually:

Enterprise APIs
Documentation
Schemas
Events
Policies
Workflows
Configuration
      ↓
Enterprise Action Graph
      ↓
Capabilities
      ↓
Actions

The Integration Model provides the executable connection between the Enterprise Action Graph and the underlying enterprise systems.

⸻

53. Integration and Enterprise Action Graph

An EAG node may represent:

Capability

while the Integration identifies:

How that Capability is executed

Therefore:

Enterprise Action Graph
       ↓
Capability
       ↓
Integration
       ↓
Enterprise System

This separates semantic capability from implementation.

⸻

54. Integration Abstraction

Noema should abstract implementation details without hiding execution semantics.

The Integration should hide:

* HTTP details
* serialization
* authentication mechanics
* endpoint paths
* transport-specific details

while preserving:

* Capability
* inputs
* outputs
* authorization
* Preconditions
* Postconditions
* consistency
* errors
* idempotency
* retry semantics
* execution guarantees
* provenance

The abstraction boundary must therefore be:

implementation-opaque but semantically explicit.

⸻

55. Integration Replacement

An Integration should ideally be replaceable without changing the semantic Intent model.

For example:

Payment Integration A
        ↓
refund_payment

may later become:

Payment Integration B
        ↓
refund_payment

provided the semantic Action Contract and required execution guarantees remain compatible.

This reduces unnecessary coupling between Noema and individual vendors or implementations.

⸻

56. Integration Migration

During system migration:

Legacy System
      ↓
Migration
      ↓
New System

Noema may temporarily operate multiple Integrations.

Authority, capability mappings, State semantics, and execution boundaries must be explicit during the transition.

Noema must not infer that the newer system is authoritative merely because it was introduced later.

⸻

57. Integration Security Boundary

The Integration boundary is a security boundary.

It must control:

* credentials
* identity
* authorization
* network access
* data access
* capability exposure
* tenant isolation
* environment isolation
* secret handling

An Integration should expose only the capabilities required by Noema.

⸻

58. Integration Data Minimization

An Integration should retrieve and transmit only the data required for the relevant operation.

For example:

refund_payment

may require:

payment_id
amount
reason

It should not require unrelated customer information.

The Integration must therefore preserve:

Least Privilege
+
Purpose Limitation
+
Data Minimization

⸻

59. Integration Lifecycle

Integrations have a lifecycle.

Conceptually:

Discovered
    ↓
Configured
    ↓
Validated
    ↓
Active
    ↓
Degraded
    ↓
Suspended
    ↓
Retired

Noema must not execute against an Integration whose lifecycle State does not permit execution.

Lifecycle State must be distinguished from the Business State owned by the external system.

⸻

60. Integration Validation

Before an Integration becomes executable, Noema should validate:

* authentication
* connectivity
* capability mappings
* schemas
* authorization
* environment
* tenant scope
* consistency semantics
* error mappings
* idempotency
* execution guarantees
* State observation semantics
* Postcondition verification

An Integration should not become trusted merely because configuration exists.

⸻

61. Integration Trust

Trust in an Integration is contextual.

A system may be trusted for:

Read Customer

without automatically being trusted for:

Modify Customer

Similarly:

Production Integration

may be trusted for one Capability but prohibited for another by Policy.

Trust must therefore be evaluated at the appropriate scope.

Integration trust is not a global boolean.

⸻

62. Integration Failure Isolation

An Integration failure must not corrupt Noema’s internal execution state.

Noema should preserve:

Intent
Trust Decision
Action
Execution Attempt
Integration Result
Outcome
State Observations

even when the external system fails.

This allows:

* recovery
* reconciliation
* compensation
* escalation
* human intervention

without rewriting execution history.

⸻

63. Integration and Determinism

Integrations are part of the deterministic execution boundary.

The model may determine that:

refund_payment

is the intended Action.

Trust determines whether execution is permitted.

The Integration determines how the permitted Action is invoked against the enterprise system.

Therefore:

Model
   ↓
Intent
   ↓
Resolution
   ↓
Trust
   ↓
Action Contract
   ↓
Integration
   ↓
Enterprise System

The Integration must not independently invent, reinterpret, or authorize Actions.

⸻

64. Integration and Intent

Intent should remain independent of vendor-specific APIs.

For example:

Intent:
"Refund my payment."

should resolve to:

Action:
refund_payment

rather than:

Stripe POST /v1/refunds

or:

Adyen POST /payments/{id}/refund

Vendor-specific execution belongs below the semantic Action boundary.

⸻

65. Integration and Outcome

The Integration provides the observations necessary to establish whether execution produced the intended enterprise result.

Conceptually:

Action
  ↓
Integration
  ↓
Enterprise System
  ↓
Execution Result
  ↓
Observation
  ↓
Outcome
  ↓
Resulting State

A transport-level success response does not necessarily imply successful Business State transition.

Outcome must be established according to the Action’s Postconditions and enterprise semantics.

This distinction is essential:

Transport Success
       ≠
Business Outcome Success
       ≠
Desired State Satisfied

⸻

66. Integration Model

Conceptually:

Integration {
    integration_id
    system_id
    environment
    tenant_scope
    version
    authentication
    authorization
    capabilities
    input_mapping
    output_mapping
    preconditions
    postconditions
    consistency
    idempotency
    retry_semantics
    error_mapping
    event_sources
    state_observation
    provenance
    observability
    lifecycle
}

This is a semantic model rather than a requirement for a literal database representation.

⸻

67. Integration Relationships

Integration
│
├── connects_to → System
├── exposes → Capability
├── implements → Action Contract
├── retrieves → Enterprise Data
├── observes → Enterprise State
├── produces → Evidence
├── provides → Context
├── invokes → Enterprise Action
├── emits → Events
├── verifies → Postcondition
└── participates_in → Execution

The Integration is therefore both:

an access boundary

and:

an execution boundary.

It is not the owner of the underlying Business State.

⸻

68. Integration Invariants

Invariant 1

An Integration is the controlled boundary between Noema and an external enterprise system.

Invariant 2

An Integration does not become the owner of the enterprise Business State it accesses.

Invariant 3

Intent must remain independent of vendor-specific implementation details.

Invariant 4

Semantic Actions must be separated from transport-specific execution mechanisms.

Invariant 5

Every executable Integration must have an explicit Capability contract.

Invariant 6

Authentication and authorization are distinct concerns.

Invariant 7

Integration authorization does not replace Noema Authority evaluation.

Invariant 8

Credentials must remain within the secure execution boundary.

Invariant 9

Tenant and environment boundaries must be explicit.

Invariant 10

An API endpoint does not automatically constitute an executable Capability.

Invariant 11

Schema and Capability changes must not silently change Action semantics.

Invariant 12

Consequential writes must respect the Integration’s idempotency and retry semantics.

Invariant 13

A timeout after a write must not automatically be interpreted as execution failure.

Invariant 14

Unknown external Outcomes must remain explicitly unknown until reconciled.

Invariant 15

Integration errors must preserve sufficient semantic information for Trust and Execution decisions.

Invariant 16

Events may provide Evidence of enterprise State changes but do not automatically replace authoritative State.

Invariant 17

Integration observations must retain sufficient provenance for consequential decisions.

Invariant 18

Integration access must follow least-privilege and data-minimization principles.

Invariant 19

An Integration must not bypass Noema’s Trust, Policy, Authority, or Action Contract boundaries.

Invariant 20

An Integration must not independently reinterpret or invent Actions.

Invariant 21

Integration failures must not corrupt Noema’s internal execution state.

Invariant 22

Compensation must operate through authorized enterprise capabilities.

Invariant 23

Multiple Integrations may coexist for different authority domains or implementations.

Invariant 24

Conflicting Integration results must be resolved through authority, consistency, State resolution, or explicit reconciliation—not probabilistic guessing.

Invariant 25

Integration trust is scoped to the relevant Capability, Action, resource, environment, tenant, and Policy.

Invariant 26

An Integration must not be executable when its lifecycle or validation State does not permit execution.

Invariant 27

Integration abstraction must hide implementation details without hiding execution semantics.

Invariant 28

An Integration should be replaceable without unnecessarily changing the semantic Intent model.

Invariant 29

Noema may coordinate enterprise execution through Integrations without becoming the enterprise System of Record.

Invariant 30

Enterprise State remains authoritative according to the applicable domain authority model.

Invariant 31

Observed State must remain distinguishable from authoritative State where the source does not establish authority.

Invariant 32

Stale or eventually consistent Integration data must not automatically be treated as current State.

Invariant 33

Integration observations must preserve sufficient temporal information to determine whether State is current for the relevant Action.

Invariant 34

An Integration must not convert an uncertain external Outcome into a definitive success or failure without sufficient evidence.

Invariant 35

Postcondition verification must use State and Evidence appropriate to the Action’s required consistency and authority.

Invariant 36

A successful transport response does not by itself establish successful Business State transition.

Invariant 37

Integration execution must preserve the distinction between Execution Result, Outcome, and resulting enterprise State.

Invariant 38

Integration capabilities must expose sufficient guarantees for Noema to evaluate the relevant Action Contract deterministically.

Invariant 39

Integration-specific failures must remain distinguishable from Intent resolution failures and Trust denials.

Invariant 40

The Integration boundary must not become an alternate path around Noema’s deterministic execution boundary.

⸻

69. Final Definition

The Integration Model defines the controlled boundary through which Noema discovers, accesses, observes, and executes enterprise capabilities while preserving enterprise ownership of Business State.

The fundamental relationship is:

Enterprise System
        │
        ▼
    Integration
        │
        ▼
    Capability
        │
        ▼
 Action Contract
        │
        ▼
      Trust
        │
        ▼
    Execution
        │
        ▼
Enterprise Operation
        │
        ▼
   Observation
        │
        ▼
     Outcome
        │
        ▼
Resulting Enterprise State

The architectural rule is:

Noema should abstract how enterprise capabilities are implemented without abstracting away the guarantees, authority, State semantics, provenance, and constraints required to execute them safely.

The deeper Noema boundary is therefore:

Human Intent
      ↓
Intent Resolution
      ↓
Context + Evidence
      ↓
Current State
      ↓
Policy + Constraint + Authority
      ↓
Trust
      ↓
Action Contract
      ↓
Integration
      ↓
Enterprise Execution
      ↓
Outcome
      ↓
State Verification
      ↓
Resulting State

And the ownership boundary remains:

                NOEMA
                  │
        Intent / Trust / Action
        Execution / Outcome
                  │
          Integration Boundary
                  │
                  ▼
       ENTERPRISE SYSTEMS
                  │
        Business State / SoR

Noema coordinates and governs execution against enterprise systems. It does not silently become the authority for the Business State those systems own.

That is the canonical Integration boundary.