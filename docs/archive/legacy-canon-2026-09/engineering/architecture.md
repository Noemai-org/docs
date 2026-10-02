> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Architecture

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/architecture.md

⸻

1. Definition

Noema Engineering Architecture defines the implementation architecture through which Noema’s canonical semantic, validation, Trust, Action Graph, contract, execution, and Outcome models are realized as a reliable software system.

The Engineering Architecture is not a second ontology.

It translates Noema’s canonical architectural boundaries into implementable system components, interfaces, state transitions, persistence requirements, execution boundaries, observability mechanisms, and operational guarantees.

Its responsibility is therefore to answer:

How must Noema be engineered so that its canonical semantic and execution boundaries remain true at runtime?

The engineering architecture must preserve the distinction between:

* human expression
* interpretation
* Intent
* validation
* Trust
* Action Graph
* Action Contract
* execution
* external business state
* Outcome

The implementation must not collapse these boundaries merely because doing so is operationally convenient.

The canonical conceptual flow is:

Human Expression
      ↓
Interpretation
      ↓
Intent Engine
      ↓
Canonical Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contracts
      ↓
Execution
      ↓
Outcome

Engineering components implement this lifecycle.

They do not redefine it.

⸻

2. Architectural Objective

The primary engineering objective is to make Noema:

* deterministic where determinism is required
* explicit where authority is required
* durable across failures
* auditable across state transitions
* reproducible where decisions must be reconstructed
* safe against stale state
* resistant to hidden execution
* compatible with asynchronous and long-running execution
* explicit about uncertainty
* resilient to external-system failure
* observable without requiring model chain-of-thought
* capable of recovering execution without duplicating consequential Actions
* evolvable without silently changing historical semantics

The engineering architecture must therefore treat Noema as a stateful control system, not merely as a request/response application.

⸻

3. Core Engineering Principle

Noema must not depend on the continued availability, consistency, or memory of a single process to preserve semantic or execution state.

A process may fail.

A worker may restart.

A network may fail.

A model may become unavailable.

A consumer may become unavailable.

An external system may respond ambiguously.

A deployment may interrupt execution.

The canonical Noema state must nevertheless remain reconstructible.

Therefore:

Process Memory ≠ Canonical State

and:

Model Context ≠ System State

and:

Worker Availability ≠ Execution Continuity

Durable system state must exist independently of ephemeral compute.

⸻

4. Engineering Boundary

The Engineering Architecture sits beneath Noema’s conceptual architecture.

Conceptually:

                    NOEMA SEMANTIC ARCHITECTURE
Human
  ↓
Expression
  ↓
Intent Engine
  ↓
Intent
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Action Contracts
  ↓
Execution
  ↓
Outcome
                    ENGINEERING REALIZATION
                ┌─────────────────────────┐
                │       API / Input       │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │    Intent Engine        │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Validation / Trust      │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Action Graph Runtime    │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Contract / Capability   │
                │ Resolution              │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Durable Execution       │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Execution Consumers      │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Outcome / Evidence      │
                └─────────────────────────┘

Each implementation component must have a defined architectural responsibility.

⸻

5. Engineering Components

The engineering system should be decomposed into explicit components corresponding to Noema’s canonical boundaries.

Conceptually:

Input / API Layer
      ↓
Interpretation Layer
      ↓
Intent Engine
      ↓
Validation Engine
      ↓
Trust Engine
      ↓
Action Graph Engine
      ↓
Contract Resolver
      ↓
Durable Execution Engine
      ↓
Execution Consumers
      ↓
Outcome Recorder

Cross-cutting infrastructure supports these components:

                ┌──────────────────────────┐
                │     Event / State Log     │
                └──────────────────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
 Persistence          Observability       Audit / Provenance
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ↓
                    All Noema Components

These components may be implemented as separate services, modules, libraries, or processes.

The conceptual boundary is more important than the deployment topology.

⸻

6. Logical Architecture vs Deployment Architecture

Noema must distinguish logical architectural boundaries from physical deployment boundaries.

For example:

Intent Engine
Validation
Trust

may initially execute inside one process.

That does not mean they are one architectural responsibility.

Likewise:

Action Graph
Durable Execution
Consumer

may eventually be distributed across multiple services.

The engineering architecture therefore defines logical ownership and contracts first.

Physical decomposition may evolve independently.

⸻

7. State as a First-Class Engineering Concern

Noema is fundamentally stateful.

Important state includes:

* Intent state
* Intent versions
* validation results
* Trust state
* Trust evaluations
* Action Graph versions
* Action node states
* Action Contract bindings
* execution attempts
* external execution references
* approvals
* confirmations
* retries
* compensation state
* Outcome state
* provenance
* audit history

These states must not be represented solely through transient process variables.

A restart must not erase the semantic or execution state of the system.

⸻

8. Canonical State vs Derived State

Noema must distinguish canonical state from derived operational state.

Canonical state includes information necessary to establish what Noema has semantically or operationally established.

Examples:

Intent version
Trust decision
Action Graph version
Action Contract identity
Execution attempt
Outcome

Derived state may include:

queue depth
worker heartbeat
cache contents
materialized dashboards
temporary scheduling metadata

Derived state may be rebuilt.

Canonical state must remain durable and reconstructible.

⸻

9. Event History and State

Noema may use an event-oriented architecture to preserve material transitions.

Conceptually:

IntentCreated
      ↓
IntentResolved
      ↓
TrustEvaluated
      ↓
GraphCreated
      ↓
ActionReady
      ↓
ActionStarted
      ↓
ActionCompleted
      ↓
OutcomeRecorded

The exact persistence model may be event-sourced, state-based with immutable audit events, or hybrid.

The architectural requirement is:

Material semantic and execution transitions must remain reconstructible.

An implementation must not make historical state dependent on mutable records that silently overwrite the events that produced them.

⸻

10. Versioned State

Noema must version material semantic artifacts.

At minimum, engineering state should be capable of distinguishing:

Intent ID
Intent Version
Trust Evaluation ID
Trust Evaluation Version
Action Graph ID
Action Graph Version
Action Contract Version
Execution ID
Execution Attempt

This allows the system to answer:

Which exact semantic and governance state authorized this execution?

⸻

11. Immutable Historical Records

Historical records associated with material decisions should be append-oriented.

For example:

Intent v1
Intent v2
Intent v3

rather than:

Intent
  ↓
mutated repeatedly

The latter makes reconstruction dependent on undocumented database mutation history.

Noema should preserve the semantic history necessary for audit and replay.

Operational metadata may be mutable where appropriate.

Material semantic decisions should not be silently overwritten.

⸻

12. Identities

Engineering identifiers must distinguish stable identity from version identity.

Conceptually:

intent_id
intent_version
graph_id
graph_version
execution_id
attempt_id
action_id
action_instance_id

A stable identity answers:

Which logical object is this?

A version or instance identity answers:

Which particular representation or execution of that object is this?

This distinction is essential for retries, revisions, and auditability.

⸻

13. Correlation

Every material lifecycle operation should be correlatable across components.

A Noema execution may produce:

request_id
intent_id
intent_version
trust_evaluation_id
graph_id
graph_version
action_instance_id
execution_id
attempt_id
contract_id
outcome_id

The engineering system should allow these identifiers to be correlated without relying on natural-language descriptions.

⸻

14. Intent Engine Implementation Boundary

The Intent Engine is responsible for semantic construction and resolution.

Engineering components implementing it may include:

* interpretation adapter
* candidate Intent builder
* context resolver
* reference resolver
* clarification manager
* deterministic resolution engine
* Intent version store
* provenance recorder

The implementation must preserve:

Model Output
      ↓
Candidate Intent
      ↓
Intent Engine
      ↓
Canonical Intent

and must not implement:

Model Output
      ↓
Execution

⸻

15. Model Integration

Models are external or replaceable computational components from the perspective of Noema’s canonical state.

A model invocation should therefore be treated as an input-producing operation rather than an authority boundary.

The system may record:

model provider
model identifier
model version
request metadata
generation timestamp
candidate output

where appropriate.

Model output may contribute to:

* interpretation
* candidate Intent construction
* clarification generation
* candidate graph generation
* semantic extraction

It does not independently establish:

* authorization
* Trust
* capability
* Action Contract permission
* execution authority

⸻

16. Model Failure

The engineering architecture must treat model failure as an ordinary system condition.

Possible conditions include:

MODEL_UNAVAILABLE
MODEL_TIMEOUT
MODEL_INVALID_OUTPUT
MODEL_SCHEMA_FAILURE
MODEL_RATE_LIMITED
MODEL_OUTPUT_AMBIGUOUS
MODEL_OUTPUT_UNSUPPORTED

Noema must not convert model failure into fabricated semantic certainty.

For example:

Model unavailable
      ↓
UNRESOLVED / WAITING

not:

Model unavailable
      ↓
best guess
      ↓
execution

⸻

17. Structured Interfaces

Components should communicate through structured representations rather than informal natural-language conventions.

Examples include:

Intent
IntentResolutionResult
ValidationResult
TrustEvaluation
ActionGraph
ActionGraphValidationResult
ActionContract
ExecutionRequest
ExecutionResult
Outcome

Schemas should be versioned.

Unknown fields should not silently change semantic meaning.

Breaking schema changes must be explicitly managed.

⸻

18. Validation Boundary

Validation must remain separate from Intent construction.

The engineering flow is:

Canonical Intent
      ↓
Validation Engine
      ↓
Validation Result

Validation may establish:

* schema validity
* required fields
* reference validity
* semantic constraints
* domain applicability
* structural requirements

Validation does not establish execution authorization.

⸻

19. Trust Boundary

The Trust Engine consumes validated semantic state and relevant governance information.

Conceptually:

Validated Intent
      ↓
Trust Evaluation
      ↓
Trust State

Trust state must be persisted independently of execution state.

For example:

Trust = READY
Execution = FAILED

is a legitimate system state.

An execution failure does not retroactively mean that the Trust evaluation was invalid.

⸻

20. Action Graph Boundary

The Action Graph Engine constructs or evaluates explicit execution structure.

It must represent:

* Action nodes
* dependencies
* conditions
* inputs
* outputs
* capabilities
* contracts
* failure semantics
* execution relationships
* provenance

The graph must remain inspectable.

A model-generated graph is a candidate until it passes the applicable deterministic validation and governance requirements.

⸻

21. Action Graph Runtime

The Action Graph Runtime is responsible for evaluating which Action nodes are currently eligible to progress.

Conceptually:

Graph
  ↓
Dependency Evaluation
  ↓
Condition Evaluation
  ↓
Action Eligibility
  ↓
Ready Actions

The runtime must not invent graph semantics.

If a node is blocked because a required dependency is unknown, the runtime must preserve that state.

⸻

22. Action Contract Resolution

Every executable Action must resolve to an applicable Action Contract.

Conceptually:

Action Node
    ↓
Capability
    ↓
Action Contract
    ↓
Execution Interface

The engineering system must verify that:

* the Action exists
* the capability exists
* the contract is resolvable
* required inputs are available
* contract constraints are satisfied
* execution conditions remain valid

A graph node without a resolvable execution contract is not executable.

⸻

23. Capability Registry

Noema should maintain a machine-readable representation of available capabilities.

A capability record may include:

capability_id
version
provider
operation
input_schema
output_schema
contract_reference
availability
constraints
authorization_requirements

Capability discovery must not itself grant authorization.

Therefore:

Capability Discovery
        ≠
Authorization

⸻

24. External System Boundary

External systems remain authoritative for their own business domains.

Examples:

Banking System → account state
CRM → customer state
Identity Provider → identity state
Payment Provider → payment state
Shipping System → delivery state

Noema may:

* request state
* consume state
* verify state
* reference state
* record evidence about state

Noema must not silently claim ownership of external business truth.

⸻

25. Execution Boundary

Execution is the point at which Noema crosses from representing and governing an Action to causing an external effect.

This boundary must therefore be explicit.

Conceptually:

Action Graph
      ↓
Action Contract
      ↓
Execution Request
      ↓
Execution Consumer
      ↓
External Effect

No arbitrary model call, internal helper, or undocumented side effect should bypass this boundary for consequential Actions.

⸻

26. Durable Execution

Noema must support execution that survives process and infrastructure failure.

An execution may last:

* milliseconds
* seconds
* minutes
* hours
* days

depending on the Action.

The execution state must therefore not depend on a worker remaining alive for the entire duration.

Conceptually:

Execution
   ↓
Persisted State
   ↓
Worker
   ↓
Failure
   ↓
Recovery
   ↓
Worker
   ↓
Continue

The execution identity remains stable across worker replacement.

⸻

27. Execution as a State Machine

Execution should be represented through explicit states.

For example:

NOT_STARTED
READY
DISPATCHED
EXECUTING
WAITING
COMPLETED
FAILED
RETRYING
BLOCKED
UNKNOWN
COMPENSATING
COMPENSATED

The exact state taxonomy belongs to the execution specification.

The engineering implementation must ensure that state transitions occur through defined events or deterministic evaluation.

⸻

28. No In-Memory Execution Authority

A worker must never be the sole source of truth for whether an Action executed.

For example, this is insufficient:

worker memory:
    payment_sent = true

Instead:

Execution Record
    ↓
Attempt Record
    ↓
Consumer Response
    ↓
Outcome Evidence

must provide durable evidence.

Worker memory may be an optimization.

It must not be authoritative state.

⸻

29. At-Least-Once Delivery

Distributed execution commonly requires retryable delivery.

Therefore the engineering architecture must assume that an execution request may be delivered more than once.

Conceptually:

Dispatch
   ↓
timeout
   ↓
retry
   ↓
same Action

This makes idempotency a first-class engineering requirement.

Noema must not assume that:

one dispatch = one external effect

⸻

30. Idempotency Boundary

Idempotency should be enforced at the Action Contract and execution boundary where appropriate.

A consequential Action should have a stable idempotency identity such as:

execution_id
+
action_instance_id

or another contract-defined idempotency key.

A retry must be distinguishable from a new semantic Action.

The consumer should be able to determine whether the request has already been processed where the external system supports such semantics.

⸻

31. Unknown External Results

The engineering system must explicitly support ambiguous external outcomes.

Example:

Request sent
    ↓
network timeout
    ↓
response unknown

The system must not automatically record:

FAILED

if the external system may have completed the Action.

The correct state may be:

UNKNOWN

followed by:

RECONCILIATION

or another contract-defined recovery process.

⸻

32. Reconciliation

When external execution produces an uncertain result, Noema may need to reconcile against the authoritative external system.

Conceptually:

Action
  ↓
UNKNOWN
  ↓
Reconcile
  ├── Confirmed Completed
  ├── Confirmed Failed
  └── Remains Unknown

Reconciliation must be explicit.

It must not fabricate certainty.

⸻

33. Retry Engineering

Retries must be driven by explicit policy.

A retry decision may consider:

* failure class
* attempt count
* timeout
* idempotency
* contract semantics
* external provider behavior
* backoff
* maximum execution duration

The runtime must not retry every failure indiscriminately.

For example:

Permanent Authorization Failure
    ↓
FAILED

should not become:

RETRY
RETRY
RETRY

merely because a generic worker policy exists.

⸻

34. Durable Timers

Long-running execution may require waiting.

Examples:

WAIT_FOR_APPROVAL
WAIT_FOR_CONFIRMATION
WAIT_FOR_DELIVERY
WAIT_UNTIL_TIME
RETRY_AFTER_BACKOFF

These waits must be represented durably.

A process should be able to terminate while the Action remains:

WAITING

and later resume without losing state.

⸻

35. Human Interaction

Human approval and confirmation must be represented as durable state.

For example:

ACTION
  ↓
WAITING_FOR_APPROVAL
  ↓
APPROVAL_RECEIVED
  ↓
RE-EVALUATE
  ↓
EXECUTE

A UI session must not be the authoritative source of approval state.

The approval event must be durable and associated with the relevant Intent, graph, and Action instance.

⸻

36. Re-Evaluation Before Consequential Execution

A previously valid Action may become invalid before execution.

Therefore, before consequential execution, the engineering system may need to re-evaluate:

* Trust
* authorization
* capability availability
* Action Contract validity
* external business conditions
* graph freshness
* approvals
* confirmations
* temporal constraints

Conceptually:

Previously Valid
      ↓
Execution Boundary
      ↓
Final Evaluation
      ↓
Execute

This addresses time-of-check/time-of-use conditions.

⸻

37. Stale Execution State

Noema must detect stale state.

Examples:

Intent v1
Graph v1
Trust evaluation v1

while the current state is:

Intent v2
Graph v2

The execution runtime must not silently execute Graph v1 merely because a worker still holds a valid reference to it.

Version identity must be checked at appropriate boundaries.

⸻

38. Optimistic Concurrency

Where multiple workers may attempt to advance the same execution state, the persistence layer should provide concurrency control.

Possible mechanisms include:

* version numbers
* compare-and-swap
* transactional updates
* leases
* locks where justified
* unique constraints
* conditional writes

The exact mechanism may vary.

The invariant is:

Concurrent workers must not silently produce contradictory execution state.

⸻

39. Worker Leases

If execution workers claim pending Actions, the claim must be durable and recoverable.

Conceptually:

READY
  ↓
Worker A claims
  ↓
LEASED
  ↓
Worker A fails
  ↓
Lease expires
  ↓
Action becomes eligible again

The recovery mechanism must not confuse worker disappearance with Action failure.

⸻

40. Exactly-Once Semantics

Noema should not assume that distributed systems can provide exactly-once external effects merely through internal message processing.

The engineering distinction is:

Exactly-once state transition

versus:

Exactly-once external effect

These are not equivalent.

External exactly-once behavior depends on the capabilities and contract semantics of the target system.

Where exactly-once external effect cannot be guaranteed, Noema must use explicit idempotency and reconciliation semantics.

⸻

41. Transactional Boundaries

Noema should use transactions where they establish meaningful atomic state transitions.

For example:

Persist Action Attempt
+
Persist Dispatch Event

may require coordinated persistence.

However, a database transaction cannot automatically make an external API call transactional.

Therefore:

Database Transaction
    ≠
External System Transaction

Cross-system atomicity must never be assumed without explicit support.

⸻

42. Outbox Pattern

Where appropriate, Noema may use an outbox-style mechanism to ensure that durable state changes and subsequent message publication are coordinated.

Conceptually:

Transaction
 ├── Update Execution State
 └── Write Outbox Event
          ↓
      Dispatcher
          ↓
      Message / Queue

This prevents a state transition from being committed while the corresponding dispatch event is silently lost.

The specific persistence mechanism may differ.

The architectural requirement is durable coordination between state and dispatch.

⸻

43. Queue and Messaging Semantics

Messaging infrastructure should expose explicit delivery semantics.

Noema should account for:

* duplicate messages
* delayed messages
* reordered messages where possible
* lost messages
* poison messages
* consumer failure
* redelivery
* dead-letter handling

Messages should carry stable identities and relevant version information.

Message arrival must not itself imply semantic validity.

⸻

44. Event Ordering

Not all events require global ordering.

Noema should establish ordering requirements explicitly.

For example:

Intent v1
Intent v2

must preserve semantic version ordering.

But unrelated executions may progress independently.

The architecture should avoid imposing global serialization where local ordering is sufficient.

⸻

45. Graph Parallelism

The Action Graph may expose independent Actions that can execute concurrently.

Engineering runtime must nevertheless evaluate:

* dependency semantics
* resource conflicts
* contract restrictions
* atomicity
* shared external state
* concurrency limits
* idempotency
* ordering constraints

Therefore:

Graph independence
    ≠
automatic safe parallel execution

Parallelism is an execution decision constrained by graph and contract semantics.

⸻

46. Resource Coordination

Actions may compete for resources.

Examples:

Account Lock
Inventory
API Rate Limit
Exclusive Resource
Shared Record

The engineering architecture may require resource coordination mechanisms.

A graph must not assume that two logically independent Actions are physically independent.

⸻

47. Compensation

When an execution consists of multiple external effects, failure recovery may require compensation.

Conceptually:

A
↓
B
↓
C fails
Compensation:
B_compensate
↓
A_compensate

Compensation is an explicit Action governed by its own contract.

It is not an implicit database rollback.

⸻

48. Partial Completion

Engineering state must preserve partial execution.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The system must not compress this into:

FAILED

without retaining the underlying node states.

The final Outcome must preserve the distinction between:

* completed
* failed
* skipped
* blocked
* pending
* unknown
* compensated

where relevant.

⸻

49. Outcome Recording

Outcome is the durable record of what Noema established about execution.

It should distinguish:

Requested
Authorized
Dispatched
Observed
Verified
Completed
Failed
Unknown

where the relevant semantics apply.

Outcome must not be inferred solely from the absence of an error in a worker process.

⸻

50. Postcondition Verification

Successful consumer responses may not always establish that the desired business state exists.

Where contracts require verification:

Execute
  ↓
External Response
  ↓
Postcondition Verification
  ↓
Outcome

The authoritative external system remains the source of truth for its business state.

Noema records the evidence and verification result.

⸻

51. Failure Classification

Engineering failures should be structured.

Examples:

VALIDATION_FAILURE
TRUST_FAILURE
CONTRACT_FAILURE
AUTHORIZATION_FAILURE
DEPENDENCY_FAILURE
TIMEOUT
NETWORK_FAILURE
PROVIDER_FAILURE
CONFLICT
STALE_STATE
UNKNOWN_RESULT
PERMANENT_FAILURE
TRANSIENT_FAILURE

The classification must support deterministic downstream behavior.

Human-readable messages may accompany canonical machine-readable codes.

⸻

52. Error Handling

Noema should avoid generic error handling that collapses materially different conditions.

For example:

Authorization denied

is not equivalent to:

External provider unavailable

and neither is equivalent to:

External outcome unknown

Each condition may require different execution semantics.

⸻

53. Recovery

Recovery must be explicit.

A failed component may:

RETRY
RECONCILE
COMPENSATE
WAIT
ESCALATE
BLOCK
FAIL

The correct behavior derives from the Action Contract, graph semantics, and execution policy.

Recovery must not be invented dynamically by a model during execution.

⸻

54. Replanning

Replanning may become necessary when the existing graph can no longer fulfill the Intent.

Examples:

* capability unavailable
* contract changed
* dependency invalid
* external resource unavailable
* policy changed
* material business state changed

The engineering sequence should be:

Detect Material Change
      ↓
Invalidate / Revalidate
      ↓
Trust Re-evaluation where required
      ↓
Graph Revision
      ↓
Contract Rebinding
      ↓
Execution

Replanning must not silently mutate the existing graph history.

⸻

55. Graph and Execution Versioning

An execution must identify the graph against which it operates.

Conceptually:

execution_id
intent_id = I-123
intent_version = 4
graph_id = G-456
graph_version = 2

If the graph changes:

G-456 v2
      ↓
material change
      ↓
G-456 v3

the relationship must remain auditable.

An execution must not silently switch graph versions.

⸻

56. Deployment Independence

Deployment of Noema components must not implicitly terminate semantic or execution state.

For example:

Deploy new worker version

must not mean:

Cancel all executions

unless explicitly defined.

Long-running executions must survive ordinary application lifecycle events.

⸻

57. Schema Evolution

Noema schemas will evolve.

Engineering systems must therefore support versioned schemas for:

* Intent
* provenance
* validation
* Trust
* Action Graph
* Action Contract
* execution
* Outcome
* events

Historical records must remain interpretable.

A new software version must not make prior canonical records unreconstructible without an explicit migration strategy.

⸻

58. Backward Compatibility

When possible, new component versions should preserve compatibility with existing persisted state.

Where incompatible semantics are introduced:

Old Schema
    ↓
Explicit Migration
    ↓
New Schema

must be preferred over implicit reinterpretation.

A historical Intent must not acquire a different meaning merely because the current application version changed.

⸻

59. Deterministic Replay

Noema should support replay or reconstruction of material lifecycle decisions where the required inputs and versions are available.

For example:

Intent
+
Context
+
Evidence
+
Rules
+
Versions
      ↓
Resolution Result

and:

Graph
+
Contract
+
Execution Events
      ↓
Execution State

Replay must distinguish between:

* reconstructing historical state
* actually executing external Actions

Replaying an execution history must never accidentally re-execute consequential Actions.

⸻

60. Simulation

Noema may support dry-run or simulation modes.

A simulation may evaluate:

Intent
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Contracts

without causing external effects.

Simulation must be explicitly distinguished from execution.

For example:

SIMULATION

must not be interpreted as:

EXECUTION

by a consumer.

⸻

61. Testing Architecture

Noema engineering must test architectural invariants, not merely individual functions.

Testing should include:

Unit Testing

Individual semantic and execution components.

Contract Testing

Compatibility between Noema and execution consumers.

Integration Testing

Interactions with external capabilities.

Failure Testing

Timeouts, retries, duplicates, crashes, stale state, and unknown outcomes.

State-Machine Testing

Valid and invalid lifecycle transitions.

Recovery Testing

Worker failure and process restart.

Replay Testing

Historical reconstruction.

Concurrency Testing

Competing workers and simultaneous transitions.

Property / Invariant Testing

Architectural rules that must always hold.

⸻

62. Crash Recovery Testing

A core engineering requirement is the ability to recover from failure at arbitrary execution points.

Examples:

before dispatch
during dispatch
after dispatch but before response
after response but before persistence
after persistence but before acknowledgement
during retry
during compensation
during human waiting

Each state must have defined recovery semantics.

⸻

63. Testing Unknown Outcomes

Unknown external results must be explicitly tested.

Example:

Request sent
↓
Connection lost
↓
Response unknown

Expected behavior should verify that Noema does not incorrectly classify the Action as failed or completed without evidence.

⸻

64. Security Architecture

Security must preserve Noema’s authority boundaries.

The engineering system must enforce:

* authenticated Actor identity
* authorization boundaries
* capability restrictions
* Action Contract restrictions
* tenant isolation where applicable
* secret isolation
* credential protection
* auditability
* least privilege
* execution-boundary controls

A model must not be able to escalate privileges through semantic output.

⸻

65. Secret Handling

Secrets must not become ordinary Intent or graph data.

Examples:

* API credentials
* access tokens
* private keys
* passwords
* session secrets

should be handled through dedicated secret-management mechanisms.

Action Contracts may reference credentials or credential scopes without exposing secret material in canonical semantic records.

⸻

66. Tenant and Actor Isolation

Where Noema operates across multiple Actors or organizational tenants, all persisted and executable state must retain the relevant ownership boundary.

Cross-tenant references must not be resolved merely because an identifier happens to exist.

The engineering layer must enforce isolation independently of model behavior.

⸻

67. Auditability

The engineering architecture must allow reconstruction of material events.

At minimum, the system should be able to establish:

1. what the Actor expressed
2. what Intent was constructed
3. how it was resolved
4. what evidence was used
5. which validation occurred
6. what Trust evaluation occurred
7. which graph version was selected
8. which contracts were bound
9. which Actions executed
10. what external responses were received
11. what retries occurred
12. what human approvals occurred
13. what final Outcome was established

This does not require recording private model chain-of-thought.

It requires recording material system provenance.

⸻

68. Provenance Architecture

Provenance should be represented structurally.

A provenance record may identify:

source_type
source_id
source_version
timestamp
actor
component
rule_version
evidence_reference

Provenance should be attached to material claims and transitions rather than stored only in free-form logs.

⸻

69. Observability

Operational observability should cover:

* Intent lifecycle
* resolution latency
* clarification rate
* validation failures
* Trust transitions
* graph construction
* graph invalidation
* Action readiness
* execution latency
* retry counts
* unknown outcomes
* consumer failures
* compensation
* human intervention
* Outcome completion

Observability should distinguish system health from semantic state.

⸻

70. Logging

Logs should support debugging without becoming the canonical state store.

Logs may contain:

request identifiers
component
event
timestamp
correlation identifiers
failure code
execution metadata

Logs should not be treated as the authoritative record of whether an Action executed.

That information belongs in durable execution state and Outcome records.

⸻

71. Metrics

Metrics should be derived from canonical state where possible.

Useful measures include:

intent_resolution_latency
clarification_rate
validation_failure_rate
trust_block_rate
graph_generation_latency
execution_latency
retry_rate
unknown_outcome_rate
consumer_failure_rate
reconciliation_rate
compensation_rate

Metrics are operational views.

They do not replace canonical state.

⸻

72. Tracing

Distributed tracing may connect:

Expression
  ↓
Intent
  ↓
Validation
  ↓
Trust
  ↓
Graph
  ↓
Action
  ↓
Consumer

Tracing provides operational visibility.

It must not be confused with semantic provenance.

A trace shows execution relationships.

Provenance establishes why a semantic or governance state existed.

Both may be required.

⸻

73. Control Plane and Execution Plane

Noema can be usefully understood as having two related planes.

Control Plane

Responsible for:

* Intent
* validation
* Trust
* Action Graph
* contracts
* policy
* execution eligibility
* state transitions

Execution Plane

Responsible for:

* dispatch
* consumer invocation
* external effects
* retries
* reconciliation
* postcondition verification
* execution outcomes

Conceptually:

                 CONTROL PLANE
Intent → Validation → Trust → Graph → Contract
                                      │
                                      ▼
                              EXECUTION ELIGIBILITY
                                      │
                                      ▼
                 EXECUTION PLANE
                         Dispatch → Consumer
                                      ↓
                              External Effect
                                      ↓
                                  Outcome

The execution plane must not bypass the control plane.

⸻

74. Authority Boundary

The fundamental engineering boundary is:

Representation
      ↓
Governance
      ↓
Execution

The system must prevent lower layers from granting authority to themselves.

For example:

Action Graph

cannot grant authorization merely because it contains:

TRANSFER_FUNDS

Likewise:

Capability Registry

cannot grant authorization merely because:

transfer.create

exists.

Authorization remains independently established.

⸻

75. No Hidden Execution

No consequential external operation may occur outside the declared execution architecture without an explicit architectural basis.

If an Action causes:

database mutation
external API call
financial transfer
message delivery
account modification

the operation must be attributable to:

Intent
→ Graph
→ Action
→ Contract
→ Execution

or to an explicitly defined contractual internal operation.

This is necessary for auditability and control.

⸻

76. Contractual Internal Operations

An Action Contract may define internal operations required to perform an Action.

For example:

CREATE_TRANSFER

may require internal:

credential acquisition
request signing
provider request construction
response normalization

These operations need not necessarily become separate Action Graph nodes.

However, the contract boundary must make them explicit.

No contract may conceal an unrelated consequential operation.

⸻

77. Configuration vs Canonical Semantics

Engineering configuration must not silently redefine canonical semantic behavior.

Configuration may determine:

* infrastructure endpoints
* worker concurrency
* timeouts
* operational limits
* feature availability

But semantic changes such as:

what constitutes approval
what makes an Intent resolved
what Actions are required
what constitutes completion

should be governed through explicit versioned semantics or policies.

Operational configuration and semantic policy must remain distinguishable.

⸻

78. Policy Versioning

Where policy affects:

* Trust
* graph construction
* approval requirements
* execution conditions
* retries
* limits

the applicable policy version should be recorded.

For example:

Trust Evaluation:
policy_version = 17

This allows historical decisions to be reconstructed under the rules that actually applied at the time.

⸻

79. Time

Time is a first-class engineering input.

Material timestamps may include:

created_at
resolved_at
validated_at
trusted_at
graph_created_at
contract_bound_at
execution_started_at
execution_completed_at
outcome_recorded_at

Where temporal rules affect semantics, the relevant clock and timestamp semantics must be explicit.

Distributed components must not assume that local wall-clock timestamps are perfectly synchronized.

⸻

80. Temporal Validity

Noema must support temporal validity for:

* Intent
* Trust decisions
* approvals
* confirmations
* capabilities
* contracts
* credentials
* external evidence

An artifact valid at T1 may not remain valid at T2.

The engineering runtime must therefore respect explicit validity intervals where defined.

⸻

81. Backpressure

Execution infrastructure must prevent uncontrolled accumulation of work.

Backpressure may arise from:

* provider limits
* worker limits
* database capacity
* queue capacity
* concurrency restrictions
* Action Contract limits

The system may transition Actions into:

WAITING
BLOCKED
DEFERRED

rather than overwhelming external systems.

⸻

82. Rate Limits

External capability constraints should be represented where relevant.

For example:

Capability:
payment.create
Constraint:
100 requests/minute

The execution layer must enforce operational constraints without changing semantic Intent.

Rate limiting affects when an Action executes, not what the Actor intended.

⸻

83. Backoff and Scheduling

Retries and delayed execution should use durable scheduling.

A scheduled retry should be represented as state:

RETRY_WAITING
next_attempt_at = ...

rather than depending solely on a worker sleep.

Worker restart must not lose the schedule.

⸻

84. Cancellation

Cancellation must be represented explicitly.

Possible states include:

CANCEL_REQUESTED
CANCELLING
CANCELLED

Cancellation semantics depend on whether an external Action has already begun.

An already-issued external operation may not be cancellable.

Therefore:

Cancellation Requested

does not necessarily mean:

External Effect Reversed

The Outcome must reflect what actually occurred.

⸻

85. Shutdown Semantics

Graceful shutdown must preserve durable execution state.

A worker shutting down should:

* stop claiming new work where appropriate
* persist current state
* release or allow recovery of leases
* preserve in-flight attempt identity
* avoid falsely marking Actions as failed
* allow another worker to recover

The process lifecycle must not become an execution lifecycle.

⸻

86. Disaster Recovery

Noema must preserve sufficient durable state to recover from infrastructure loss.

Recovery objectives should be defined for:

* canonical semantic state
* Trust state
* graph state
* execution state
* provenance
* audit history
* Outcome records

Backups must be tested through actual restoration procedures.

A backup that cannot reconstruct Noema state is not sufficient merely because the files exist.

⸻

87. Data Retention

Retention policies must distinguish:

* canonical semantic records
* audit records
* operational logs
* metrics
* sensitive credentials
* temporary execution artifacts

Deletion or archival must not destroy information required for legally, operationally, or architecturally required reconstruction unless the governing retention policy explicitly permits it.

⸻

88. Privacy

Engineering persistence should minimize unnecessary sensitive data.

The system should store:

* what is necessary for semantic reconstruction
* what is necessary for execution
* what is necessary for auditability
* what is necessary for security

Sensitive information should not be duplicated across logs, events, traces, and model prompts without necessity.

⸻

89. External Evidence Storage

Evidence references should be durable enough to establish what source supported a semantic or execution decision.

Where Noema cannot permanently store the external content, it should retain an appropriate reference or evidence identifier where available.

The system must distinguish:

Evidence existed

from:

Evidence is currently retrievable

Historical reconstruction must account for evidence availability.

⸻

90. Dependency Management

Engineering dependencies should be explicit.

Noema should distinguish:

semantic dependency
execution dependency
infrastructure dependency
external capability dependency
resource dependency

Failure of one category must not automatically be interpreted as failure of another.

For example:

Database unavailable

is not semantically equivalent to:

Intent invalid

⸻

91. Availability

Noema should degrade explicitly when dependencies are unavailable.

Examples:

Context unavailable
    ↓
Intent may remain unresolved
Capability unavailable
    ↓
Graph may become blocked or require revision
Consumer unavailable
    ↓
Execution waits or fails according to contract

The system must preserve uncertainty instead of fabricating successful state.

⸻

92. Graceful Degradation

Graceful degradation must never cross semantic safety boundaries.

It may be acceptable to:

WAIT
DEFER
CLARIFY
BLOCK
ESCALATE

It is not acceptable to:

guess
assume authorization
invent missing parameters
execute an unvalidated Action

Reliability must not be achieved by weakening authority controls.

⸻

93. Engineering Invariants

Invariant 1

Canonical semantic state must not depend solely on process memory.

Invariant 2

Model output must not directly become execution authority.

Invariant 3

Intent, Validation, Trust, Action Graph, Contract, Execution, and Outcome remain distinct architectural responsibilities.

Invariant 4

Material semantic state must be versioned or otherwise reconstructible.

Invariant 5

Execution state must survive worker and process failure.

Invariant 6

Retries must not silently create duplicate consequential effects.

Invariant 7

Unknown external results must remain unknown until evidence establishes their outcome.

Invariant 8

External business systems remain authoritative for their business state.

Invariant 9

A stale graph must not silently execute.

Invariant 10

Action execution must resolve to an explicit Action Contract.

Invariant 11

Capability availability does not itself grant authorization.

Invariant 12

Workers are execution agents, not canonical state authorities.

Invariant 13

Logs are not a substitute for durable execution state.

Invariant 14

Replay must never accidentally re-execute consequential Actions.

Invariant 15

Human approval and confirmation must be durable system state.

Invariant 16

Schema evolution must not silently change the meaning of historical canonical state.

Invariant 17

Recovery behavior must be governed by explicit execution semantics.

Invariant 18

No hidden consequential Action may bypass the execution boundary.

Invariant 19

Operational optimization must not alter Intent semantics.

Invariant 20

Failure of an external system must not be silently converted into semantic success.

Invariant 21

Concurrent workers must not produce contradictory canonical execution state.

Invariant 22

Material state transitions must be auditable.

Invariant 23

Durable execution must preserve execution identity across worker replacement.

Invariant 24

No engineering convenience may collapse an authority boundary defined by the Noema architecture.

⸻

94. Canonical Engineering Lifecycle

The engineering lifecycle can be reduced to:

                    ACTOR
                      ↓
                Human Expression
                      ↓
                 Interpretation
                      ↓
                Intent Engine
                      ↓
               Canonical Intent
                      ↓
                  Validation
                      ↓
                    Trust
                      ↓
                Action Graph
                      ↓
              Action Contracts
                      ↓
             Durable Execution
                      ↓
             Execution Consumer
                      ↓
              External Systems
                      ↓
            Postcondition Check
                      ↓
                   Outcome

At every stage, the system must preserve:

Identity
Version
State
Provenance
Authorization Boundary
Failure Semantics

⸻

95. Canonical Recovery Lifecycle

When infrastructure or external execution fails:

Execution
   ↓
Failure / Interruption
   ↓
Durable State
   ↓
Recovery Evaluation
   ↓
┌──────────┬──────────┬──────────┬──────────┐
↓          ↓          ↓          ↓
Retry    Reconcile  Compensate  Escalate
   │          │          │          │
   └──────────┴──────────┴──────────┘
                     ↓
                  Outcome

Recovery must operate from durable state rather than worker memory.

⸻

96. Canonical Engineering Mental Model

The Engineering Architecture can be reduced to six questions:

1. Where is the canonical state stored?
2. Which component owns each state transition?
3. How does execution survive process and infrastructure failure?
4. How are consequential external effects made idempotent or reconciled?
5. How can every material decision and execution be reconstructed?
6. How does the system prevent implementation convenience from bypassing Noema’s authority boundaries?

These questions produce the engineering model:

Canonical State
      ↓
Explicit State Transitions
      ↓
Durable Execution
      ↓
Contracted External Effects
      ↓
Reconciliation
      ↓
Auditable Outcome

⸻

97. Relationship to Existing Noema Architecture

The Engineering Architecture implements, but does not replace, the foundational architecture.

The relationship is:

Intent Engine
    ↓
Canonical Intent
    ↓
Validation
    ↓
Trust
    ↓
Action Graph
    ↓
Action Contracts
    ↓
Durable Execution
    ↓
Outcome

The engineering layer supplies the mechanisms required to make these boundaries operationally real:

Persistence
Versioning
Concurrency Control
Messaging
Scheduling
Workers
Recovery
Idempotency
Reconciliation
Observability
Audit
Security
Schema Evolution

These mechanisms are subordinate to the canonical architectural semantics.

⸻

98. Fundamental Engineering Boundary

The fundamental engineering boundary is:

Noema must be able to stop, restart, recover, inspect,
and continue without losing the distinction between:
what the Actor intended,
what Noema established,
what Noema authorized,
what Noema attempted,
what the external system actually did,
and what Noema ultimately knows.

This distinction must survive:

* process failure
* worker failure
* deployment
* network failure
* provider failure
* model failure
* retries
* concurrency
* delayed execution
* human intervention
* graph revision
* schema evolution

⸻

99. Final Definition

The Engineering Architecture is the implementation architecture through which Noema preserves its canonical semantic and authority boundaries across persistent state, distributed execution, external effects, failures, recovery, and system evolution.

Its central invariant is:

Noema must not rely on ephemeral processes, probabilistic model behavior, or implicit execution semantics to maintain canonical state or execution authority. Canonical Intent, Validation, Trust, Action Graph, Action Contracts, Execution, and Outcome must remain explicit, durable, versioned, and reconstructible, while consequential external effects are governed through durable execution and explicit recovery semantics.

The engineering architecture therefore establishes the implementation foundation for:

Expression
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
Durable Execution
      ↓
External Effect
      ↓
Outcome

with the fundamental engineering property:

Explicit semantics
        +
Durable state
        +
Explicit authority
        +
Recoverable execution
        +
Auditable outcomes
        =
Reliable Noema