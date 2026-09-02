Contracts Overview

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/overview.md

⸻

1. Definition

Noema Contracts are the canonical schemas and behavioral agreements that define how semantic intent, context, trust, actions, execution, events, and outcomes move through the Noema system.

Contracts establish explicit boundaries between components that would otherwise rely on implicit assumptions.

They define not only what data looks like, but also what that data means, what may change it, what guarantees apply, and what responsibilities belong to each boundary.

⸻

2. Purpose

The Contracts domain exists to make Noema’s execution pipeline:

* explicit
* deterministic
* interoperable
* versionable
* auditable
* testable
* recoverable
* integration-independent

Contracts prevent individual services, models, integrations, or workflows from silently defining system semantics.

⸻

3. Core Question

The Contracts domain answers:

What must be true at each boundary for Noema to safely move from one state of the intent journey to another?

Contracts define the guarantees between those boundaries.

⸻

4. Contracts as System Boundaries

A contract is a boundary between two or more components.

Conceptually:

Component A
    │
    │ Contract
    ▼
Component B

The contract defines what Component B can expect from Component A and what Component A may expect in return.

⸻

5. Contracts Are More Than Schemas

A schema defines structure.

A Noema Contract defines:

structure
+ semantics
+ constraints
+ invariants
+ lifecycle
+ ownership
+ versioning
+ failure behavior

Therefore:

Contract ≠ JSON Schema
Contract ≠ API Payload
Contract ≠ Database Model

A schema may implement part of a contract, but it does not constitute the entire contract.

⸻

6. Contract Domains

The foundational Contracts domain contains:

contracts/
├── overview.md
├── intent-contract.md
├── context-contract.md
├── trust-contract.md
├── action-contract.md
├── execution-contract.md
└── event-contract.md

These contracts describe the principal semantic boundaries of Noema’s execution model.

⸻

7. Intent Contract

The Intent Contract defines what the user or initiating system is trying to accomplish.

Intent

It captures:

* semantic goal
* intent type
* subject
* target
* parameters
* constraints
* ambiguity
* resolution state
* provenance
* lifecycle

The Intent Contract does not authorize execution.

⸻

8. Context Contract

The Context Contract defines contextual information used to understand, resolve, evaluate, or execute an Intent.

Context

Context may include:

* identity
* tenant
* organization
* resource relationships
* temporal context
* permissions
* environment
* relevant enterprise data
* evidence references

Context enriches intent without silently redefining it.

⸻

9. Trust Contract

The Trust Contract defines the deterministic conditions and decision semantics governing whether a requested operation may proceed.

Its canonical outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

Trust does not reinterpret the user’s goal.

It evaluates whether the resolved intent and proposed action satisfy applicable policies, evidence requirements, permissions, risk constraints, and execution conditions.

⸻

10. Action Contract

The Action Contract defines an executable operation that can be derived from an Intent.

Intent
   ↓
Action

An Action should specify:

* action identity
* action type
* target
* parameters
* required context
* preconditions
* permissions
* idempotency semantics
* expected outcome
* integration requirements

The Action Contract is the bridge between semantic intent and executable behavior.

⸻

11. Execution Contract

The Execution Contract governs the lifecycle of an Action once execution begins.

Action
   ↓
Execution

It defines:

* execution identity
* lifecycle state
* attempts
* preconditions
* running state
* timeouts
* retries
* verification
* outcomes
* failures
* recovery
* intervention
* reconciliation

Execution is not equivalent to an API request.

⸻

12. Event Contract

The Event Contract defines the canonical representation of facts about state transitions and significant occurrences within Noema.

Event

Events communicate what happened.

They do not independently authorize what should happen next.

For example:

IntentResolved
TrustDecisionMade
ActionCreated
ExecutionStarted
ExecutionCompleted
ExecutionFailed

Events provide temporal and audit lineage across the system.

⸻

13. Contract Relationship

The primary relationship is:

                 Human
                   │
                   ▼
                Intent
                   │
                   ▼
                Context
                   │
                   ▼
                 Trust
                   │
             ┌─────┴─────┐
             │            │
          Clarify      Continue
                          │
                          ▼
                        Action
                          │
                          ▼
                      Execution
                          │
                          ▼
                        Event
                          │
                          ▼
                       Outcome

Each stage has a distinct contract.

⸻

14. Intent to Action Boundary

The Intent Contract represents the desired goal.

The Action Contract represents an executable operation.

Intent:
"Show my transactions from last month."
Action:
RetrieveTransactions(
    account_id,
    start_date,
    end_date
)

The mapping must be explicit.

An integration must not be allowed to infer the semantic meaning of an Intent on its own.

⸻

15. Action to Execution Boundary

An Action describes what should be executed.

An Execution represents the controlled attempt to perform it.

Action
   ↓
Execution Instance

One Action definition may produce multiple execution instances where retry, recovery, or repeated intent instances require it.

⸻

16. Events Across Contracts

Events connect lifecycle transitions across the contracts.

Conceptually:

Intent
  │
  ├── IntentReceived
  ├── IntentResolved
  │
  ▼
Trust
  │
  ├── TrustEvaluated
  │
  ▼
Action
  │
  ├── ActionCreated
  │
  ▼
Execution
  │
  ├── ExecutionStarted
  ├── ExecutionCompleted
  └── ExecutionFailed

Events provide evidence of transitions without becoming the authority for those transitions.

⸻

17. Contract Ownership

Each contract must have a clearly defined semantic owner.

Conceptually:

Intent Contract
→ Noema intent domain
Context Contract
→ Noema context domain
Trust Contract
→ Noema trust domain
Action Contract
→ Noema action domain
Execution Contract
→ Noema execution domain
Event Contract
→ Noema event domain

Ownership determines who may define, validate, and evolve the semantics of a contract.

⸻

18. Contract Authority

A contract does not automatically grant authority over the underlying data.

For example:

Execution Contract

may describe an execution against an account.

It does not make Noema authoritative for:

account balance
account ledger
transaction truth
account ownership

Enterprise systems remain authoritative for enterprise business state.

⸻

19. Noema Contract Authority

Noema may be authoritative for its own execution-domain state, including:

* intent lifecycle
* trust decisions
* action instances
* execution lifecycle
* intervention state
* execution evidence
* execution lineage
* contract versions

This authority does not extend into enterprise business truth merely because Noema references it.

⸻

20. Contract Boundaries

Contracts should establish explicit boundaries between:

semantic state
context
trust
executable intent
execution state
events
enterprise business state

Crossing a boundary must be deliberate.

A component should not modify another domain’s state simply because it has access to its representation.

⸻

21. Contract Invariants

A contract should define invariants that must remain true regardless of implementation.

For example:

Intent
→ must have identity
Action
→ must have explicit semantics
Execution
→ must have lifecycle state
Event
→ must have occurrence identity
Trust
→ must produce a defined decision

Invariants provide the stable foundation beneath evolving implementations.

⸻

22. Contract Validation

Contracts must be validated at their boundaries.

Validation should establish:

* structural validity
* semantic validity
* required fields
* supported versions
* scope
* lifecycle state
* permitted transitions
* invariant compliance

Validation failure must prevent invalid state from silently propagating downstream.

⸻

23. Structural Versus Semantic Validation

Structural validation asks:

Does this object have the required shape?

Semantic validation asks:

Does this object mean something valid within Noema?

For example:

{
  "action": "retrieve_transactions",
  "account_id": null
}

may be structurally valid JSON but semantically invalid if the account is required.

Both forms of validation are necessary.

⸻

24. Contract Versioning

Every foundational contract must be versioned.

Contract v1
Contract v2
Contract v3

Versioning protects:

* compatibility
* replay
* historical interpretation
* integration stability
* auditability
* migration

A breaking semantic change must not silently reinterpret historical contract instances.

⸻

25. Backward Compatibility

Contract evolution should distinguish:

additive change
compatible semantic change
breaking structural change
breaking semantic change

Compatibility must be evaluated at the semantic level, not merely by whether existing JSON can still be parsed.

⸻

26. Contract Immutability

Once a contract instance has influenced a consequential decision, its historical representation must remain reconstructable.

For example:

Intent v1
   ↓
Trust Decision
   ↓
Action

Later changes to the Intent Contract must not make the historical decision uninterpretable.

⸻

27. Contract Lineage

Contracts should preserve lineage across the intent journey.

Intent
   │
   ▼
Context
   │
   ▼
Trust Decision
   │
   ▼
Action
   │
   ▼
Execution
   │
   ▼
Event
   │
   ▼
Outcome

Each downstream object should be traceable to the upstream object that caused or informed its creation.

⸻

28. Contract Provenance

Contract instances should retain sufficient provenance to establish:

* who or what produced them
* when they were produced
* which version produced them
* what inputs informed them
* what context was used
* what prior state existed

Provenance is required for meaningful auditability and recovery.

⸻

29. Contracts and AI Models

AI models may participate in producing candidate Intent or Context representations.

They do not own the contracts.

The architecture is:

LLM
 ↓
Candidate Interpretation
 ↓
Contract Validation
 ↓
Deterministic Resolution
 ↓
Trust
 ↓
Action
 ↓
Execution

The model is therefore an input to the contract-governed system, not the governing authority.

⸻

30. Determinism

Noema’s contract layer is a primary mechanism for enforcing determinism after probabilistic interpretation.

The model may say:

"I think this means X."

The contract-governed system must determine:

Is X valid?
Is X sufficiently resolved?
Is X permitted?
What Action represents X?
Can X execute?
What happened?

These decisions cannot be delegated to model confidence alone.

⸻

31. Unknown State

Contracts must be capable of representing uncertainty.

Examples include:

UNKNOWN
UNRESOLVED
PENDING
CONFLICTED

Noema must not force uncertain information into a false binary such as:

SUCCESS / FAILURE

when the underlying truth is not established.

⸻

32. Failure Semantics

Every consequential contract boundary should define failure behavior.

Failure may arise from:

* invalid input
* missing context
* ambiguity
* permission failure
* trust rejection
* unavailable integration
* timeout
* provider error
* business-state conflict
* verification failure

Failures must preserve the boundary at which they occurred.

⸻

33. Unknown Is Not Failure

A timeout does not necessarily mean an operation failed.

For example:

Request sent
    ↓
Provider timeout
    ↓
Outcome UNKNOWN

The Execution Contract must preserve this distinction.

The Contracts domain must not force uncertain external state into an incorrect failure state.

⸻

34. Contracts and Recovery

Contracts provide the state and lineage necessary for recovery.

Recovery may require:

retry
reconciliation
clarification
compensation
human intervention
cancellation

Recovery must operate against explicit contract state rather than reconstructing intent from logs or model output.

⸻

35. Contracts and Enterprise Systems

Enterprise systems remain the authority for enterprise business state.

The contract architecture therefore separates:

Noema Contract State
        from
Enterprise Business State

For example:

Execution:
SUCCEEDED
Enterprise:
authoritative business state

The latter must still be verified through the enterprise boundary where required.

⸻

36. Contracts and Integrations

Integrations translate canonical Noema Actions into provider-specific operations.

Conceptually:

Canonical Action
      ↓
Integration Adapter
      ↓
Provider Operation

Provider-specific request formats must not redefine canonical Noema semantics.

The integration layer is an implementation boundary, not the semantic authority.

⸻

37. Contracts and Data

Contracts reference data.

They do not automatically own the underlying data.

For example:

Context Contract
    ↓
references customer/account data
Enterprise System
    ↓
owns authoritative customer/account state

This distinction prevents Noema from becoming an accidental shadow system of record.

⸻

38. Contracts and Evidence

Evidence may support contract decisions.

For example:

Evidence
    ↓
Context
    ↓
Trust
    ↓
Action

Evidence must retain its authority, freshness, provenance, scope, and validity.

A contract should not treat the mere existence of evidence as proof that the evidence is authoritative.

⸻

39. Contracts and Permissions

Permissions are contract-relevant constraints.

A valid Intent may still result in:

REJECT

if the requesting identity lacks permission.

Permissions must be evaluated according to enterprise authority and applicable Noema policy.

⸻

40. Contracts and Organizational Boundaries

Contracts must respect:

* tenant boundaries
* organization boundaries
* legal-entity boundaries
* environment boundaries
* resource ownership
* identity boundaries

A contract instance must never silently cross an authority boundary.

⸻

41. Contracts and Temporal State

Contract instances exist at specific points in time.

Therefore contracts should retain relevant:

created_at
updated_at
effective_at
expires_at
version

where applicable.

Historical contract interpretation must use the correct temporal context.

⸻

42. Contracts and Auditability

Contracts make the Noema execution journey reconstructable.

An audit trail should be able to answer:

What was requested?
What was understood?
What context was used?
What trust decision occurred?
What Action was selected?
What Execution occurred?
What happened externally?
What outcome was established?

This requires contract lineage across the entire journey.

⸻

43. Contracts and Observability

Operational telemetry should reference contract identities.

Useful identifiers include:

intent_id
context_id
trust_decision_id
action_id
execution_id
event_id
contract_version

These identifiers allow operational events to be correlated with semantic state.

⸻

44. Contract Serialization

Contracts may be serialized as:

* JSON
* protocol buffers
* database records
* event payloads
* API representations

Serialization is an implementation detail.

The canonical semantics remain defined by the contract itself.

⸻

45. Contract Transport

Contracts may cross:

* process boundaries
* service boundaries
* network boundaries
* integration boundaries
* asynchronous event boundaries

Transport must preserve the semantic guarantees of the contract.

Serialization or transport must not silently alter meaning.

⸻

46. Contract Security

Contract instances may contain sensitive information.

Contracts must therefore support:

* authentication
* authorization
* tenant isolation
* data minimization
* encryption
* access control
* retention
* auditability

Security requirements apply to both contract definitions and contract instances.

⸻

47. Contract Ownership Versus Data Ownership

Contract ownership answers:

Who defines the semantics of this object?

Data ownership answers:

Who is authoritative for the underlying fact?

These are not necessarily the same.

For example:

Noema
→ owns Execution Contract semantics
Bank
→ owns account balance truth

This distinction is foundational.

⸻

48. Contract Composition

Contracts may reference or compose other contracts.

For example:

Execution Contract
├── Action Contract
├── Context Contract
└── Trust Decision

Composition must preserve the boundaries and invariants of each constituent contract.

One contract must not silently absorb another domain’s authority.

⸻

49. Contract Dependency Direction

The preferred dependency direction is:

Intent
  ↓
Context
  ↓
Trust
  ↓
Action
  ↓
Execution
  ↓
Events / Outcome

Dependencies should flow toward downstream execution semantics rather than creating circular semantic ownership.

⸻

50. Contract Independence

Each contract should be independently understandable.

A developer should be able to determine:

* what the contract represents
* who owns it
* what fields matter
* what states exist
* what transitions are permitted
* what invariants apply
* what other contracts it references

without reverse-engineering implementation code.

⸻

51. Contract Testing

Contracts should be testable independently of implementation.

Testing should include:

* schema validation
* semantic validation
* state-transition validation
* invariant testing
* compatibility testing
* serialization testing
* integration contract testing
* failure-path testing

Contract tests should protect semantics, not merely object shape.

⸻

52. Contract Migration

When a contract changes, migration must account for:

existing instances
active executions
historical events
integrations
stored state
replay
audit requirements

A new contract version must not invalidate the ability to understand historical execution journeys.

⸻

53. Contract Registry

Noema should maintain a canonical registry of supported contracts and versions.

Conceptually:

Contract Registry
├── Intent Contract
├── Context Contract
├── Trust Contract
├── Action Contract
├── Execution Contract
└── Event Contract

The registry should establish which versions are active, deprecated, or retired.

⸻

54. Canonical Contract Lifecycle

A contract definition follows:

DEFINE
  ↓
VALIDATE
  ↓
VERSION
  ↓
PUBLISH
  ↓
IMPLEMENT
  ↓
TEST
  ↓
OBSERVE
  ↓
EVOLVE
  ↓
DEPRECATE
  ↓
RETIRE

Contract evolution must preserve historical interpretability.

⸻

55. Reference Architecture

The Contracts domain can be represented as:

                         HUMAN
                           │
                           ▼
                    ┌─────────────┐
                    │    Intent   │
                    │   Contract  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Context   │
                    │   Contract  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Trust    │
                    │   Contract  │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │             │
                 CLARIFY       CONTINUE
                                  │
                                  ▼
                         ┌─────────────┐
                         │   Action    │
                         │   Contract  │
                         └──────┬──────┘
                                │
                                ▼
                         ┌─────────────┐
                         │  Execution  │
                         │   Contract  │
                         └──────┬──────┘
                                │
                                ▼
                         ┌─────────────┐
                         │    Event    │
                         │   Contract  │
                         └──────┬──────┘
                                │
                                ▼
                         ENTERPRISE SYSTEM
                                │
                                ▼
                              OUTCOME

⸻

56. Contracts as the Deterministic Spine

The Contracts domain forms a deterministic spine through Noema.

Human Language
      │
      ▼
Probabilistic Interpretation
      │
      ▼
┌─────────────────────────────────────┐
│          CONTRACT BOUNDARIES        │
│                                     │
│ Intent → Context → Trust → Action   │
│                    ↓                │
│                Execution            │
│                    ↓                │
│                  Events             │
└─────────────────────────────────────┘
      │
      ▼
Enterprise Execution

The contract layer constrains what may happen after interpretation.

⸻

57. Contract Boundaries and Determinism

The model may generate candidate interpretations.

The contract system determines whether those interpretations are:

* valid
* complete
* sufficiently resolved
* properly scoped
* trusted
* executable
* observable
* recoverable

Therefore:

Probabilistic interpretation must terminate at deterministic contract boundaries before consequential execution.

⸻

58. Commercial Scope

The initial commercial wedge does not require the full complexity of financial state-changing operations.

Phase 1 can operate on read and support workflows such as:

ACCOUNT_BALANCE_INQUIRY
STATEMENT_RETRIEVAL
TRANSACTION_SEARCH
SPENDING_SUMMARY
COMPLAINT_LOGGING

These workflows still require the complete semantic chain:

Intent
→ Context
→ Trust
→ Action
→ Execution
→ Outcome

The contract architecture therefore remains useful even when the initial Actions are primarily read-oriented.

⸻

59. Contract Design Principles

Noema Contracts should follow these principles:

1. Explicitness — semantic meaning must be explicit.
2. Separation — domains must retain distinct ownership.
3. Traceability — consequential decisions must be reconstructable.
4. Determinism — downstream state transitions must not depend on probabilistic guessing.
5. Versionability — contracts must evolve without destroying historical meaning.
6. Authority awareness — contracts must respect the authoritative system for each fact.
7. Failure transparency — uncertainty must not be disguised as failure or success.
8. Integration independence — provider APIs must not define canonical Noema semantics.
9. Security — contracts must respect data and organizational boundaries.
10. Recoverability — contract state must contain enough information to recover safely.

⸻

60. Contracts Do Not Replace Domain Logic

Contracts define boundaries and guarantees.

They do not replace:

* trust policy
* intent resolution
* workflow logic
* execution engines
* integration adapters
* enterprise business logic

Instead, contracts make the interaction between those systems explicit.

⸻

61. Contracts Do Not Replace Enterprise Systems

Noema’s Contracts domain does not attempt to model the enterprise’s entire business system.

The separation is:

Noema
→ intent and execution journey
Enterprise
→ business truth and business state

Contracts provide the interfaces between those worlds.

⸻

62. Contracts and System of Record

A contract may establish Noema as authoritative for a particular Noema-owned state without making Noema authoritative for external business state.

For example:

Noema:
Execution = SUCCEEDED
Enterprise:
Account state = authoritative external truth

Both statements can coexist without conflict.

⸻

63. Contracts and the Execution Journey

The complete journey can be represented as:

Human Request
      ↓
Intent Contract
      ↓
Context Contract
      ↓
Trust Contract
      ↓
Action Contract
      ↓
Execution Contract
      ↓
Event Contract
      ↓
Enterprise System
      ↓
Verified Outcome

This is the canonical contract path through Noema.

⸻

64. Contract Invariants

Invariant 1

Every foundational Noema contract has an explicit semantic purpose.

Invariant 2

Every contract has a defined owner.

Invariant 3

Every contract has a version.

Invariant 4

Contract semantics are distinct from serialization format.

Invariant 5

Contract validation includes semantic validity, not only structural validity.

Invariant 6

Historical contract instances must remain interpretable.

Invariant 7

Contract boundaries must preserve domain ownership.

Invariant 8

Intent does not authorize execution.

Invariant 9

Context does not redefine intent.

Invariant 10

Trust determines whether an authorized path may proceed.

Invariant 11

Action defines executable behavior.

Invariant 12

Execution defines the lifecycle of an Action instance.

Invariant 13

Events describe occurrences and state transitions.

Invariant 14

Events do not independently authorize consequential operations.

Invariant 15

Every consequential execution retains lineage to its originating Intent.

Invariant 16

Contract instances preserve sufficient provenance for auditability.

Invariant 17

Unknown and unresolved states must remain representable.

Invariant 18

Timeout does not automatically imply execution failure.

Invariant 19

Contract failures preserve the boundary at which failure occurred.

Invariant 20

Recovery operates against explicit contract state.

Invariant 21

Noema contract authority does not override enterprise authority over business state.

Invariant 22

Integrations must not redefine canonical Noema semantics.

Invariant 23

Contract changes must not silently reinterpret historical state.

Invariant 24

Contract instances must respect tenant, organizational, identity, resource, and environment boundaries.

Invariant 25

Contract data must respect applicable security, privacy, and retention requirements.

Invariant 26

AI-generated interpretations must pass through contract-governed validation before consequential execution.

Invariant 27

Model confidence does not independently authorize execution.

Invariant 28

Noema must not silently convert material ambiguity into certainty.

Invariant 29

Contract composition must preserve the ownership and invariants of constituent contracts.

Invariant 30

Noema’s contract layer must remain independent of provider-specific implementation details.

⸻

65. Final Definition

The Contracts domain is the canonical set of semantic and behavioral boundaries that govern how Noema transforms human intent into trusted, observable, executable, and recoverable operations.

Its foundational contracts are:

Intent
Context
Trust
Action
Execution
Event

Together they establish the deterministic structure of the Noema execution journey:

Human Intent
    ↓
Intent Contract
    ↓
Context Contract
    ↓
Trust Contract
    ↓
Action Contract
    ↓
Execution Contract
    ↓
Event Contract
    ↓
Verified Outcome

Contracts do not own enterprise business truth.

They define the rules by which Noema interacts with that truth while preserving semantic ownership, authority boundaries, provenance, determinism, versioning, auditability, and recovery.

The governing principle is:

Contracts make every consequential boundary explicit, so Noema never has to rely on implicit semantics, hidden state, or probabilistic judgment where deterministic system behavior is required.