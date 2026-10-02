> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

System Boundaries

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/system-boundaries.md

⸻

1. Definition

System Boundaries define the explicit architectural and engineering boundaries between Noema and the systems, components, authorities, capabilities, and external environments with which it interacts.

The purpose of System Boundaries is to establish:

* what Noema owns
* what Noema does not own
* where authority resides
* where state resides
* where validation occurs
* where execution occurs
* where responsibility transfers between components
* which assumptions may cross a boundary
* which assumptions must not cross a boundary
* how failures and uncertainty propagate across boundaries

The central principle is:

A boundary is a responsibility and authority boundary, not merely a software-module boundary.

Noema must not acquire authority merely because information or execution crosses one of its internal boundaries.

⸻

2. Core Principle

Noema is an orchestration, semantic, trust, and execution-governance system.

It is not automatically the authoritative owner of every domain object, business state, capability, identity, policy, or external transaction it coordinates.

Conceptually:

Actor
  ↓
Expression
  ↓
Interpretation
  ↓
Intent Engine
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Action Contract
  ↓
Execution Consumer
  ↓
External System
  ↓
Outcome

Each boundary has a defined responsibility.

No component may silently absorb the responsibility of another component merely because doing so is operationally convenient.

⸻

3. Boundary Invariants

The following invariants govern Noema system boundaries.

Invariant 1

A component may exercise only the authority explicitly assigned to it.

Invariant 2

Possession of information does not imply authority over that information.

Invariant 3

Access to a capability does not imply authorization to invoke it.

Invariant 4

Successful validation does not imply successful execution.

Invariant 5

A graph containing an Action does not authorize that Action.

Invariant 6

Noema does not become authoritative over external business state merely because it observes or caches that state.

Invariant 7

External systems remain authoritative for business state within their defined domains.

Invariant 8

Execution consumers remain responsible for enforcing execution-time conditions within their domain.

Invariant 9

Unknown information must remain unknown across boundaries unless an authoritative source establishes it.

Invariant 10

A boundary crossing must preserve sufficient provenance to reconstruct what information or authority was transferred.

⸻

4. Noema System Boundary

Noema’s system boundary encompasses the components necessary to transform an Actor’s expressed objective into governed execution and a recorded Outcome.

At a conceptual level:

                    NOEMA
┌─────────────────────────────────────────────┐
│                                             │
│ Interpretation                              │
│      ↓                                      │
│ Intent Engine                               │
│      ↓                                      │
│ Validation                                  │
│      ↓                                      │
│ Trust                                       │
│      ↓                                      │
│ Action Graph                                │
│      ↓                                      │
│ Action Contracts                            │
│      ↓                                      │
│ Execution Coordination                      │
│      ↓                                      │
│ Outcome / Observability / Audit             │
│                                             │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
              External Systems

The boundary does not mean Noema controls everything on either side.

It means the responsibility transfer is explicitly defined.

⸻

5. Internal vs External Responsibility

Noema components are responsible for Noema semantics and governance.

External systems are responsible for their own authoritative domain state and execution semantics.

For example:

Noema
  ├── Intent semantics
  ├── Trust decisions
  ├── Action Graph structure
  ├── Contract governance
  ├── Execution coordination
  └── Outcome recording
Banking System
  ├── Account state
  ├── Account balance
  ├── Transaction state
  └── Banking-domain execution

Noema may coordinate a banking Action.

It does not thereby become the authoritative banking ledger.

⸻

6. Authority vs Access

Access and authority are distinct.

A component may be able to read a resource without becoming authoritative over that resource.

For example:

Noema
   │
   │ read
   ▼
Customer Registry

does not imply:

Noema = Customer Registry

Similarly:

Noema
   │
   │ invoke
   ▼
Payment Capability

does not imply:

Noema = Payment Authority

The distinction must remain explicit.

⸻

7. Authority Domains

Every important state or decision should have an identifiable authority.

Examples include:

Domain	Authority
Actor expression	Actor / interaction record
Intent semantics	Noema Intent Engine
Intent validity	Validation subsystem
Execution eligibility	Trust subsystem
Action structure	Action Graph
Action permissions	Action Contract + Trust / authorization boundary
External account state	External account system
Payment transaction state	Payment provider / financial system
Identity record	Authoritative identity system
Delivery state	Delivery provider
Execution result	Execution consumer + external system evidence

The exact authority depends on the domain.

Noema must not create competing authoritative state without an explicit architectural reason.

⸻

8. Semantic Boundary

The boundary between human expression and canonical Intent is a semantic boundary.

Human Expression
      ↓
AI Interpretation
      ↓
Candidate Intent
      ↓
Intent Engine
      ↓
Canonical Intent

The model may propose meaning.

The Intent Engine establishes canonical Intent.

Therefore:

Model Output ≠ Canonical Intent

The semantic boundary must preserve the distinction between:

* what was expressed
* what was inferred
* what was resolved
* what was established

⸻

9. Intent Engine Boundary

The Intent Engine owns semantic construction and resolution.

It does not own:

* authorization
* Trust
* external business state
* execution
* provider-side transaction state

Its boundary is:

Expression
   ↓
Interpretation
   ↓
Intent Engine
   ↓
Canonical Intent

The resulting Intent then crosses into Validation.

⸻

10. Validation Boundary

Validation determines whether a canonical Intent satisfies applicable structural and semantic requirements.

Conceptually:

Canonical Intent
      ↓
Validation
      ↓
Validation Result

Validation does not establish authorization.

For example:

Validation:
amount is valid
recipient exists
required fields are present

does not establish:

Actor may transfer the amount.

That remains a Trust / authorization concern.

⸻

11. Trust Boundary

Trust establishes whether a validated Intent may proceed under Noema’s execution-governance requirements.

Conceptually:

Validated Intent
      ↓
Trust
      ↓
Execution Eligibility

Trust may incorporate:

* identity
* authorization
* policy
* risk
* approvals
* constraints
* contextual conditions
* required evidence

Trust does not execute the Action.

⸻

12. Trust Is Not Execution

The Trust boundary must remain separate from execution.

Trust = may proceed
Execution = what happened

A Trust decision of:

READY

does not mean:

SUCCESS

Similarly:

Execution = FAILED

does not necessarily mean:

Trust decision = INVALID

These are different architectural dimensions.

⸻

13. Action Graph Boundary

The Action Graph represents how a trusted Intent may be fulfilled.

It defines:

* Actions
* dependencies
* conditions
* execution relationships
* inputs
* outputs
* failure relationships
* capability bindings
* contract relationships

It does not independently establish authorization.

Therefore:

Trust
  ↓
Action Graph

does not mean the graph itself becomes an authority.

⸻

14. Action Contract Boundary

The Action Contract defines the executable interface and obligations associated with an Action.

Conceptually:

Action Graph Node
      ↓
Action Contract
      ↓
Execution Consumer

The contract establishes the terms under which an Action may be executed.

It may define:

* required inputs
* permitted outputs
* preconditions
* postconditions
* authorization requirements
* idempotency requirements
* retry semantics
* failure semantics
* execution obligations
* provider interaction requirements

⸻

15. Execution Boundary

The execution boundary is crossed when Noema causes an external or consequential operation to occur.

Before the boundary:

Intent
Validation
Trust
Graph
Contract

After the boundary:

External effect
External state transition
Provider response
Execution outcome

This boundary is consequential.

It must therefore be explicit, observable, and governed.

⸻

16. Execution Consumer Boundary

The execution consumer is responsible for carrying an Action Contract into an execution environment.

Conceptually:

Noema
  ↓
Action Contract
  ↓
Execution Consumer
  ↓
Provider / External System

The consumer may enforce execution-time conditions.

The consumer must not silently alter the semantic meaning of the Intent.

⸻

17. External System Boundary

External systems remain authoritative for their own business domains.

Examples include:

* banking systems
* payment processors
* CRM systems
* identity systems
* logistics systems
* communication providers
* enterprise databases
* document systems

Noema may coordinate these systems.

It does not automatically become the owner of their state.

⸻

18. External State Authority

If an external system owns a state variable, Noema should treat that system as authoritative.

For example:

Bank
    account.status = ACTIVE

Noema may cache:

observed_account_status = ACTIVE

but this is not equivalent to:

Noema owns account.status

The distinction becomes especially important when external state changes after observation.

⸻

19. State Observation Boundary

Observed external state should carry:

* source
* observation time
* resource identity
* relevant version or revision where available
* provenance
* freshness semantics
* uncertainty where applicable

Conceptually:

External Authority
       ↓
Observation
       ↓
Noema Context

An observation is not necessarily a permanent fact.

⸻

20. Time-of-Check / Time-of-Use Boundary

State can change between validation and execution.

Example:

T1:
Account = ACTIVE
T2:
Trust = READY
T3:
Account = SUSPENDED
T4:
Execute

Noema must therefore distinguish:

state observed during evaluation

from:

state established at execution time

Where the Action Contract requires it, the execution consumer must perform a final authoritative check.

⸻

21. Capability Boundary

A capability represents an available operation.

For example:

card.replacement.create

The capability boundary establishes:

Can this system expose this operation?

It does not establish:

May this Actor perform it?

Therefore:

Capability ≠ Authorization

Capability discovery must not become an authorization mechanism.

⸻

22. Capability Discovery Boundary

Noema may discover capabilities from external systems or registries.

Conceptually:

Intent
  ↓
Required Action
  ↓
Capability Discovery
  ↓
Candidate Capabilities

Discovered capabilities remain subject to:

* contract validation
* authorization
* policy
* trust
* execution constraints

Discovery does not grant permission.

⸻

23. Identity Boundary

Identity systems may remain authoritative for identity attributes.

Noema may consume:

actor_id
identity attributes
authentication evidence
authorization claims

but must distinguish:

identity evidence

from:

Noema Trust decision

Identity establishes identity-related facts.

Trust determines whether those facts satisfy the applicable execution requirements.

⸻

24. Policy Boundary

Policies may originate from:

* Noema governance
* organizational rules
* regulatory requirements
* Action Contracts
* external systems
* domain-specific policy engines

Policy determines constraints or requirements.

The Action Graph represents the operational consequence of those requirements.

For example:

Policy:
Transfers above threshold require approval.
Graph:
Create Transfer
      ↓
Request Approval
      ↓
Execute Transfer

Policy and graph must not be silently conflated.

⸻

25. Authorization Boundary

Authorization determines whether a principal may perform a consequential operation under the applicable authority model.

Authorization must remain distinct from:

* Intent
* capability
* graph structure
* model confidence
* execution success

The following is invalid:

Graph contains:
TRANSFER_FUNDS
therefore:
Actor authorized = true

The graph cannot grant authority by representation alone.

⸻

26. Approval Boundary

Human or organizational approval is a governance boundary.

For example:

Action
   ↓
Approval Required
   ↓
Approval
   ↓
Execution

Approval is evidence that a required governance condition was satisfied.

It does not necessarily establish every other execution condition.

Approval may need to be re-evaluated when material circumstances change.

⸻

27. Confirmation Boundary

Actor confirmation is distinct from generic conversational continuation.

Where confirmation is required:

Action
   ↓
Confirmation Required
   ↓
Explicit Confirmation
   ↓
Execution

Noema must not infer confirmation merely because the Actor continues the conversation.

The semantics of confirmation must be explicit.

⸻

28. Human Intervention Boundary

Human intervention is a legitimate execution state.

For example:

Action
   ↓
Human Review
   ↓
Continue

The system must distinguish:

HUMAN_REVIEW_REQUIRED

from:

FAILED

and:

BLOCKED

Human intervention may itself introduce a new material condition requiring revalidation.

⸻

29. Clarification Boundary

Clarification belongs primarily to Intent resolution.

When semantic information is insufficient:

Intent
   ↓
Ambiguity
   ↓
Clarification
   ↓
Resolved Intent

Clarification must not be used to bypass Trust.

Likewise, Trust must not be used to guess unresolved semantic meaning.

⸻

30. Context Boundary

The Context Engine may acquire and organize information used by Intent resolution and downstream evaluation.

The Intent Engine consumes context.

It does not automatically become the owner of all context.

Conceptually:

Context Sources
      ↓
Context Engine
      ↓
Context
      ↓
Intent Engine / Validation / Trust

Context must retain provenance and authority semantics.

⸻

31. Evidence Boundary

Evidence used by Noema must remain distinguishable from the conclusions derived from that evidence.

For example:

Evidence:
CRM says customer.status = ACTIVE
Conclusion:
Intent target resolves to customer_123

The evidence is not identical to the semantic or Trust decision derived from it.

This distinction supports:

* auditability
* re-evaluation
* disagreement detection
* source replacement
* historical reconstruction

⸻

32. Model Boundary

AI models are probabilistic components.

They may provide:

* interpretation
* candidate Intent
* candidate Actions
* candidate graph structures
* clarification suggestions
* classifications
* extraction
* summaries

They must not silently become authoritative over:

* canonical Intent
* Trust
* authorization
* Action permission
* external business state
* execution outcome

The model boundary therefore separates:

probabilistic proposal

from:

canonical system state

⸻

33. Model-Generated Action Boundary

A model may propose an Action Graph:

LLM
 ↓
Candidate Graph
 ↓
Deterministic Validation
 ↓
Trust / Contract Validation
 ↓
Executable Graph

The model cannot bypass those controls.

A model-generated graph remains a proposal until it satisfies the applicable deterministic requirements.

⸻

34. Tool Boundary

Tools are implementation mechanisms.

They are not authority mechanisms.

A model must not directly perform consequential tool calls merely because a tool is available.

The governed path remains:

Intent
 ↓
Trust
 ↓
Action Graph
 ↓
Action Contract
 ↓
Execution Consumer
 ↓
Tool / Provider

A tool being technically reachable does not mean it is semantically or operationally authorized.

⸻

35. Data Boundary

Data crossing a system boundary must have explicit semantics.

The receiving component must know, where relevant:

* what the value represents
* who supplied it
* where it originated
* when it was observed
* whether it is authoritative
* whether it is inferred
* whether it is stale
* whether it is complete
* whether it is unknown

Data should not cross boundaries as semantically opaque values when downstream decisions depend on their meaning.

⸻

36. Provenance Boundary

Material information crossing a boundary should preserve provenance.

Conceptually:

Value
 ├── source
 ├── timestamp
 ├── evidence reference
 ├── version
 └── derivation context

Provenance allows downstream components to determine whether information may legitimately be relied upon.

Loss of provenance must not silently convert an uncertain value into an authoritative one.

⸻

37. Version Boundary

Material semantic objects should carry version identity where required.

Examples:

Intent v7
Graph v3
Contract v12
Policy v8
Trust Evaluation v14

A downstream component must not silently treat a materially changed upstream object as the same object.

Version compatibility must be explicit where material.

⸻

38. Contract Boundary

Every significant cross-component interaction should have a defined contract.

A contract should specify, as applicable:

* inputs
* outputs
* preconditions
* postconditions
* errors
* states
* ownership
* authority
* version compatibility
* retry semantics
* timeout behavior
* idempotency semantics
* observability requirements

A shared data structure alone is not sufficient to define a boundary.

⸻

39. Failure Boundary

Failures must retain their domain meaning when crossing boundaries.

Examples:

Intent ambiguity

is not:

Execution failure
Authorization denied

is not:

Provider unavailable
Provider timeout

is not necessarily:

Transaction failed

Boundary contracts must preserve these distinctions.

⸻

40. Unknown Boundary

Unknown is a valid state across system boundaries.

For example:

Provider response:
UNKNOWN

must not automatically become:

FAILED

Similarly:

External state unavailable

must not become:

state = false

Noema must preserve uncertainty until an authoritative result resolves it.

⸻

41. Execution Outcome Boundary

Execution results cross back into Noema as evidence of what happened.

Conceptually:

Execution Consumer
      ↓
Provider
      ↓
Observed Result
      ↓
Noema Outcome

Noema records and interprets the execution result according to the applicable contract.

The external system remains authoritative over its own business state.

⸻

42. Outcome vs External State

An execution response is not necessarily equivalent to authoritative business state.

For example:

Provider response:
REQUEST_ACCEPTED

does not necessarily mean:

business operation = COMPLETED

The Action Contract may require subsequent verification.

Therefore:

Execution Response
        ≠
Final Business State

unless the contract explicitly establishes that equivalence.

⸻

43. Persistence Boundary

Noema persistence should preserve the state necessary to reconstruct its own decisions and lifecycle.

Persisted information may include:

* Intent versions
* resolution results
* provenance
* Trust evaluations
* Action Graph versions
* Action Contract references
* execution states
* event history
* outcomes
* failures
* retries
* compensation
* human interventions

Persistence does not transfer ownership of external business state to Noema.

⸻

44. Cache Boundary

Cached data must not be treated as authoritative merely because it is locally available.

A cache should preserve, where relevant:

* source
* observation time
* freshness
* version
* invalidation semantics

A stale cache must not silently satisfy a requirement for current authoritative state when the contract requires a fresh check.

⸻

45. Event Boundary

Events communicate state transitions or observations across components.

An event should have explicit semantics.

Examples:

intent.resolved
trust.ready
graph.validated
action.started
action.completed
action.failed
action.unknown
outcome.recorded

Events are records of defined occurrences.

They must not be treated as arbitrary commands unless the event contract explicitly defines command semantics.

⸻

46. Command Boundary

Commands request an operation.

For example:

ExecuteAction

is different from:

ActionExecuted

The first expresses a request.

The second records an observed event.

Conflating commands and events creates ambiguity around authority and state.

⸻

47. Message Boundary

Messages crossing asynchronous boundaries must preserve enough identity to correlate them with the relevant semantic and execution objects.

Where applicable, messages should include or reference:

* Intent identity
* Intent version
* Action identity
* Graph identity/version
* Contract identity/version
* execution identity
* correlation identity
* causation identity

This supports durable execution and reconstruction.

⸻

48. Transaction Boundary

Noema must not assume distributed atomicity merely because multiple systems participate in one Intent.

For example:

Noema
 ↓
System A
 ↓
System B

does not imply:

A + B = one atomic transaction

If transactional atomicity is unavailable, the architecture must use explicit:

* sequencing
* compensation
* reconciliation
* partial completion
* recovery
* outcome semantics

⸻

49. Compensation Boundary

Compensation crosses a semantic boundary because compensation is not equivalent to rollback.

For example:

Create Transfer
      ↓
Send Notification
      ↓
Notification fails

A compensation action might exist.

But:

compensation ≠ transactional rollback

The external systems determine what compensating operations are possible.

⸻

50. Idempotency Boundary

Retries may cause the same logical Action to cross a boundary more than once.

Therefore, consequential boundaries must define idempotency semantics.

Conceptually:

Logical Action
      ↓
Execution Attempt 1
      ↓
Unknown
      ↓
Execution Attempt 2

The second attempt must not unintentionally create a second business effect where the contract requires idempotent behavior.

Idempotency belongs primarily to the Action Contract and execution architecture.

⸻

51. Retry Boundary

Retries must not cross a boundary without defined retry semantics.

The retry policy should consider:

* failure class
* attempt count
* timeout
* backoff
* idempotency
* provider semantics
* resource state
* compensation requirements

A generic retry mechanism must not convert every failure into a retryable condition.

⸻

52. Security Boundary

Security boundaries define where trust, credentials, secrets, permissions, and privileged operations may cross.

Sensitive credentials should not be exposed to components that do not require them.

A model should not receive unrestricted credentials merely because a downstream tool requires them.

Conceptually:

Model
  ↓
Action Contract
  ↓
Execution Consumer
  ↓
Credential Boundary
  ↓
Provider

Credential possession must remain separate from semantic authority.

⸻

53. Secret Boundary

Secrets should remain within the smallest boundary capable of using them.

Noema should avoid exposing:

* API keys
* private credentials
* provider tokens
* signing keys
* privileged connection information

to components that do not require them.

Secret access should be explicit and auditable.

⸻

54. Tenant Boundary

Where Noema operates across multiple organizations or tenants, tenant isolation must be explicit.

A tenant boundary must prevent unintended access to:

* Intent data
* context
* credentials
* policies
* capabilities
* execution records
* outcomes
* observability data

Cross-tenant access must be explicitly authorized.

Tenant identity must not be inferred merely from conversational context.

⸻

55. Actor Boundary

An Actor is the principal whose objective is represented by an Intent.

Actor identity must remain stable across the Intent lifecycle unless explicitly changed.

A downstream component must not silently substitute:

requesting system

for:

Intent Actor

The distinction is particularly important when services act on behalf of humans or organizations.

⸻

56. Delegation Boundary

An Actor may delegate authority to another principal or system.

Delegation must be explicit.

For example:

Human Actor
   ↓
Delegated Agent
   ↓
Noema
   ↓
External System

The presence of a delegated agent does not automatically grant unrestricted authority.

Delegation must carry the applicable scope, constraints, and provenance.

⸻

57. Organizational Boundary

Noema may coordinate actions across organizational systems.

Organizational boundaries may affect:

* authority
* policy
* approval
* identity
* data access
* capability availability
* execution responsibility

Noema must not assume that a capability available within one organizational domain is automatically available within another.

⸻

58. Domain Boundary

Business domains should remain distinct.

For example:

Identity
Payments
CRM
Logistics
Notifications

may each maintain separate authoritative state.

Noema coordinates across these domains through explicit contracts.

It should not silently duplicate or redefine domain semantics merely to simplify orchestration.

⸻

59. API Boundary

External APIs are execution interfaces, not semantic authorities by default.

An API response should be interpreted according to its contract.

For example:

HTTP 200

does not universally mean:

business operation succeeded

The Action Contract must define the semantic meaning of the provider response.

⸻

60. Network Boundary

Network communication introduces:

* latency
* timeout
* duplication
* reordering
* disconnection
* partial failure
* unknown outcomes

Noema must not interpret network failure as business failure unless the contract establishes that conclusion.

Network boundaries therefore require explicit timeout and uncertainty semantics.

⸻

61. Temporal Boundary

Time affects the validity of information and authorization.

Examples:

Intent expires at T
Approval valid until T
Capability available from T1 to T2
Observed state valid for Δt

A value that was valid at one time may not remain valid later.

Temporal validity must therefore be explicit where material.

⸻

62. Trust Decision Boundary

A Trust decision belongs to a particular Intent version and relevant evaluation context.

Conceptually:

Intent v7
   ↓
Trust Evaluation 14
   ↓
READY

If the Intent becomes:

Intent v8

the previous Trust decision must not silently transfer when the change is material.

The relationship between the decision and the evaluated object must remain reconstructible.

⸻

63. Graph Execution Boundary

An Action Graph may exist before execution.

The graph must distinguish:

Candidate
Validated
Executable
Executing
Completed
Failed
Unknown

Crossing from planning into execution is therefore a material boundary.

Noema must not silently treat a candidate graph as executable.

⸻

64. Durable Execution Boundary

Long-running execution may cross process, machine, service, or time boundaries.

Durable execution must preserve sufficient state to resume without losing semantic context.

Conceptually:

Action
 ↓
Persist execution state
 ↓
Process interruption
 ↓
Recovery
 ↓
Resume according to contract

Recovery must not silently create a new Intent or Action identity.

The logical execution identity must survive infrastructure failure.

⸻

65. Recovery Boundary

Infrastructure recovery and business recovery are distinct.

For example:

Worker crashed

is an infrastructure failure.

Whereas:

Payment provider rejected transaction

is a business/execution failure.

The recovery mechanism must preserve the distinction.

Infrastructure recovery must not automatically retry non-retryable business failures.

⸻

66. Observability Boundary

Observability data should describe system behavior without becoming a hidden source of authority.

Metrics, logs, and traces may record:

* Intent IDs
* graph IDs
* Action IDs
* execution IDs
* durations
* failures
* retries
* state transitions
* dependency transitions

Observability must not be treated as the authoritative source of business state unless explicitly defined as such.

⸻

67. Audit Boundary

Audit records provide reconstructibility of material decisions and state transitions.

Audit data should distinguish:

what was requested
what was interpreted
what was resolved
what was authorized
what was executed
what was observed
what changed

Auditability does not require storing private model chain-of-thought.

It requires retaining sufficient decision provenance and state history.

⸻

68. Configuration Boundary

Configuration may affect system behavior but must not silently redefine semantic authority.

Material configuration should therefore be:

* versioned where necessary
* attributable
* observable
* deployable through controlled mechanisms

A configuration change that materially affects graph construction, Trust, or execution may require revalidation.

⸻

69. Policy Change Boundary

A policy change can invalidate previously prepared execution structures.

For example:

Graph v3
   ↓
Policy v8 → v9
   ↓
Material rule change
   ↓
Graph revalidation

Noema must not silently execute a stale graph where the governing policy has materially changed.

⸻

70. Contract Change Boundary

Action Contracts are versioned execution boundaries.

If:

Contract v4

changes materially to:

Contract v5

Noema must determine whether an existing graph remains valid.

A contract change must not silently alter the semantics of an already authorized execution.

Where required, the graph must be revalidated or regenerated.

⸻

71. Capability Revocation Boundary

A capability may disappear after graph construction.

Example:

Graph:
SEND_SMS
Capability:
sms.send
T1: available
T2: revoked
T3: execute

The execution path must detect the material capability change.

Noema must not silently treat historical availability as current permission.

⸻

72. External Dependency Boundary

Every external dependency introduces an explicit boundary.

A dependency may fail because of:

* timeout
* unavailability
* authorization rejection
* invalid input
* business rule rejection
* rate limiting
* network failure
* unknown state

The dependency contract must define which failures are:

* retryable
* terminal
* compensatable
* unknown
* requiring human intervention

⸻

73. Boundary Failure Semantics

A boundary should define failure behavior rather than relying on generic infrastructure defaults.

Conceptually:

Boundary Failure
      ↓
Classify
      ↓
RETRY / BLOCK / WAIT / COMPENSATE / FAIL / UNKNOWN

The classification must respect the semantic layer in which the failure occurred.

⸻

74. Boundary Crossings Must Be Explicit

A consequential operation should have a traceable boundary crossing.

Conceptually:

Action Contract
      ↓
Execution Request
      ↓
External System
      ↓
External Result

The system should be able to reconstruct:

* what crossed the boundary
* why it crossed
* under which Intent
* under which Trust decision
* under which Contract
* at what time
* with which execution identity
* what result returned

⸻

75. No Hidden Authority

No component may obtain authority merely through an indirect path.

For example:

LLM
 ↓
Tool
 ↓
Provider

must not bypass:

Intent
 ↓
Trust
 ↓
Action Graph
 ↓
Action Contract

Similarly:

Graph
 ↓
Capability

must not bypass authorization.

Authority must remain explicit at every consequential boundary.

⸻

76. No Hidden State Ownership

Noema must not silently become the authoritative owner of state merely because it stores a copy.

For example:

External System:
balance = ₦100,000
Noema cache:
balance = ₦100,000

does not establish:

Noema owns balance

The external system remains authoritative unless the architecture explicitly defines otherwise.

⸻

77. Boundary Reconciliation

When Noema and an external system disagree, the architecture must identify the authoritative source.

For example:

Noema:
payment = UNKNOWN
Provider:
payment = COMPLETED

The provider may be authoritative for payment state.

Noema should reconcile its representation rather than silently preserve the stale local state.

⸻

78. Boundary Consistency

Cross-boundary consistency should be defined rather than assumed.

Possible consistency models include:

* immediate consistency
* eventual consistency
* read-after-write consistency
* provider-confirmed consistency
* explicitly uncertain state

The correct model depends on the domain and contract.

Noema must not assume stronger consistency than the underlying systems provide.

⸻

79. Boundary Latency

A boundary may introduce latency.

Long-running operations should therefore support explicit:

* WAITING
* IN_PROGRESS
* UNKNOWN
* TIMEOUT
* COMPLETED

states.

Timeout must not automatically imply business failure where the external operation may still be processing.

⸻

80. Boundary Security Principle

Every boundary should follow least-authority principles.

A component should receive only:

* the data it requires
* the capabilities it requires
* the credentials it requires
* the authority it requires
* for the duration required

Noema should avoid creating broad internal privileges merely to simplify integration.

⸻

81. Boundary Observability Principle

Every material boundary should be observable.

At minimum, Noema should be able to establish:

source
destination
operation
identity
version
timestamp
result
failure
correlation

This supports debugging, auditing, reliability engineering, and incident reconstruction.

⸻

82. Boundary Version Compatibility

Components may evolve independently.

A boundary contract must therefore define compatibility expectations.

Conceptually:

Producer vN
      ↓
Contract
      ↓
Consumer vN / compatible version

A component must not assume compatibility merely because message delivery succeeds.

Semantic compatibility must be established.

⸻

83. Boundary Evolution

Boundaries should evolve without silently changing their authority semantics.

A new implementation may replace an old implementation while preserving:

* identity semantics
* contract semantics
* provenance semantics
* state semantics
* authorization semantics
* failure semantics

Architectural refactoring must not silently change what a component is authorized to do.

⸻

84. Boundary Testing

Boundary behavior must be tested independently of internal implementation.

Tests should include:

* valid inputs
* invalid inputs
* missing information
* unknown values
* stale state
* authorization failures
* capability revocation
* contract mismatch
* provider timeout
* duplicate requests
* partial failure
* external state changes
* recovery
* version mismatch

Boundary tests establish whether the responsibility transfer remains correct.

⸻

85. Boundary Failure Injection

Reliability testing should deliberately exercise boundary failures.

Examples:

Provider unavailable
Provider timeout
Provider returns unknown result
Capability disappears
Contract changes
External state changes
Network disconnects
Worker crashes
Duplicate execution request

The objective is to verify that uncertainty and failure remain correctly classified.

⸻

86. Boundary and Idempotency

Every consequential boundary should identify whether repeated delivery is safe.

Where repetition is unsafe, the contract must provide a mechanism such as:

* idempotency key
* execution identity
* provider transaction identity
* deduplication
* reconciliation

Noema must not assume at-most-once delivery unless the underlying boundary actually guarantees it.

⸻

87. Boundary and Ordering

Some boundaries require ordering guarantees.

For example:

Revoke Credential
      ↓
Issue Credential

The ordering requirement must be explicit.

Network or queue behavior must not silently reorder operations whose semantics require strict sequencing.

⸻

88. Boundary and Parallelism

Parallel boundary crossings are permissible only where their contracts allow independent execution.

The fact that two Actions are represented as separate graph branches does not automatically establish that the external operations are safe to perform concurrently.

Parallelism must respect:

* resource conflicts
* ordering
* atomicity
* provider limits
* policy
* Action Contracts

⸻

89. Boundary and Partial Execution

When multiple boundaries participate in one Intent, partial execution must remain explicit.

Example:

Payment → COMPLETED
Notification → FAILED
Audit → COMPLETED

Noema must not collapse these states into an undifferentiated:

FAILED

or:

SUCCESS

without applying the defined Intent and Outcome semantics.

⸻

90. Boundary and Unknown Execution

A boundary may produce an unknown result.

Example:

Request
  ↓
Provider
  ↓
Timeout

The system must distinguish:

request definitely failed

from:

request outcome unknown

This distinction is fundamental to safe retry and reconciliation.

⸻

91. Boundary and Durable State

When a boundary crossing is consequential, sufficient execution state should be durably recorded before recovery can depend upon it.

The durable record should allow Noema to determine:

* what was attempted
* whether it was acknowledged
* whether the result is known
* whether retry is permitted
* which contract governed the operation
* which execution identity was used

This prevents process failure from destroying execution semantics.

⸻

92. Boundary and Reconciliation

When execution becomes uncertain, reconciliation may be required.

Conceptually:

Execution Attempt
      ↓
Unknown
      ↓
Query Authoritative System
      ↓
Observed Business State
      ↓
Reconcile

Reconciliation must use the authoritative external source where one exists.

A local assumption must not substitute for authoritative evidence.

⸻

93. Boundary and Recovery

Recovery must respect the original semantic boundary.

If a worker crashes while executing:

CREATE_PAYMENT

recovery must resume the existing execution according to its contract.

It must not create a new Intent merely because the infrastructure process restarted.

Infrastructure identity and semantic identity are distinct.

⸻

94. Boundary and Replanning

A material external change may require graph revision.

For example:

Capability A unavailable
       ↓
Graph invalid
       ↓
Re-evaluation
       ↓
Alternative capability
       ↓
Graph v2

Replanning must not silently mutate the original Intent.

The revised graph must remain linked to the relevant Intent version and re-evaluation.

⸻

95. Boundary and Intent Mutation

A downstream system must not modify the Actor’s Intent merely to make execution possible.

For example:

Intent:
Send ₦100,000
Provider limit:
₦50,000

The provider limitation does not authorize Noema to transform the Intent into:

Send ₦50,000

A material semantic change requires explicit resolution with the Actor or applicable canonical semantics.

⸻

96. Boundary and Outcome

Outcome represents what Noema can establish about execution.

The Outcome should preserve the distinction between:

* requested operation
* execution attempt
* observed provider response
* verified external state
* final Noema outcome

Outcome must not claim certainty beyond the evidence available.

⸻

97. Canonical Boundary Flow

The canonical system relationship is:

                    ACTOR
                      │
                      ▼
              HUMAN EXPRESSION
                      │
                      ▼
                INTERPRETATION
                      │
                      ▼
                INTENT ENGINE
                      │
                      ▼
              CANONICAL INTENT
                      │
                      ▼
                 VALIDATION
                      │
                      ▼
                    TRUST
                      │
                      ▼
                ACTION GRAPH
                      │
                      ▼
              ACTION CONTRACT
                      │
                      ▼
            EXECUTION CONSUMER
                      │
                      ▼
              EXTERNAL SYSTEM
                      │
                      ▼
          EXTERNAL AUTHORITATIVE STATE
                      │
                      ▼
                 OBSERVATION
                      │
                      ▼
                   OUTCOME

Each transition represents a responsibility boundary.

⸻

98. Boundary Responsibility Matrix

Boundary	Upstream Responsibility	Downstream Responsibility
Expression → Interpretation	preserve Actor expression	propose interpretation
Interpretation → Intent Engine	provide candidate meaning	establish canonical Intent
Intent Engine → Validation	provide resolved semantic representation	verify validity
Validation → Trust	provide valid Intent	establish execution eligibility
Trust → Action Graph	provide governed execution context	represent execution structure
Graph → Contract	identify Action role	establish executable obligations
Contract → Consumer	provide executable interface	perform contracted operation
Consumer → External System	issue valid request	enforce domain execution
External System → Noema	provide authoritative result/state	record and interpret evidence
Execution → Outcome	report execution facts	establish execution outcome

⸻

99. Boundary Ownership Rules

Every boundary should answer five questions:

1. Who owns the state?
2. Who establishes authority?
3. Who validates the input?
4. Who performs the operation?
5. Who determines the authoritative outcome?

If these questions cannot be answered, the boundary is insufficiently defined.

⸻

100. Boundary Design Rules

A Noema boundary should be:

* explicit
* contract-driven
* observable
* versioned where material
* provenance-preserving
* failure-aware
* authority-aware
* idempotency-aware where consequential
* compatible with durable execution
* resistant to implicit privilege escalation

A boundary should not depend on undocumented assumptions.

⸻

101. Forbidden Boundary Shortcuts

The following architectural shortcuts are prohibited:

Shortcut 1

Model output → execution

Shortcut 2

Capability → authorization

Shortcut 3

Graph membership → authorization

Shortcut 4

Validation success → execution success

Shortcut 5

Timeout → definite failure

Shortcut 6

Cached state → authoritative state

Shortcut 7

Conversation continuation → confirmation

Shortcut 8

Model confidence → semantic resolution

Shortcut 9

Provider response → final business state without contract-defined verification

Shortcut 10

Infrastructure retry → unrestricted business retry

These shortcuts collapse distinct responsibilities and therefore violate system boundaries.

⸻

102. Architectural Boundary Test

For any proposed component or integration, Noema should be able to state:

This component owns:
    ...
This component does not own:
    ...
This component may establish:
    ...
This component may not establish:
    ...
This component consumes:
    ...
This component produces:
    ...
Its authoritative source is:
    ...
Its failure semantics are:
    ...
Its boundary contract is:
    ...

If these distinctions cannot be made, the component boundary requires further definition.

⸻

103. Fundamental Boundary Principle

Noema should separate:

Meaning

from:

Validity

and:

Authority

from:

Capability

and:

Planning

from:

Execution

and:

Execution Result

from:

Authoritative Business State

and:

Infrastructure Failure

from:

Business Failure

These distinctions are foundational to the architecture.

⸻

104. Canonical Mental Model

System boundaries can be reduced to six questions:

1. Who owns this state?
2. Who has authority to establish this fact or decision?
3. Which component is responsible for this operation?
4. What contract governs the boundary crossing?
5. What happens if the boundary fails or produces an unknown result?
6. Can the entire boundary crossing be reconstructed afterward?

If those questions have explicit answers, the boundary is architecturally defined.

⸻

105. Final Definition

System Boundaries define the explicit responsibility, authority, state-ownership, execution, data, security, and failure boundaries between Noema and the systems with which it interacts.

The central invariant is:

Noema must never obtain authority merely because information, capability, model output, graph structure, or execution access crosses a system boundary.

The canonical separation remains:

Expression
    ↓
Interpretation
    ↓
Intent
    ↓
Validation
    ↓
Trust
    ↓
Action Graph
    ↓
Action Contract
    ↓
Execution
    ↓
External Authority
    ↓
Outcome

Each layer has a distinct responsibility.

Each boundary must preserve the distinction between what is known, what is inferred, what is authorized, what is attempted, what is executed, and what is ultimately established.

The fundamental engineering rule is:

Noema may coordinate across boundaries, but it must not silently collapse them.