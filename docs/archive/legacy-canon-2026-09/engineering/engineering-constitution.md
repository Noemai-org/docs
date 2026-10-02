> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Engineering Constitution

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/engineering-constitution.md

⸻

1. Definition

The Engineering Constitution defines the non-negotiable engineering principles, boundaries, invariants, and implementation requirements governing the construction and operation of Noema.

It translates Noema’s architectural boundaries into engineering constraints.

The Engineering Constitution exists to ensure that implementation does not silently collapse distinctions established by the Noema architecture.

It governs:

* system boundaries
* component responsibilities
* data and state ownership
* deterministic control
* provenance
* versioning
* validation
* Trust integration
* Action Graph execution
* Action Contract enforcement
* external system interaction
* failure handling
* observability
* auditability
* security
* evolution and compatibility

It does not redefine the semantic ontology or architectural concepts.

Therefore:

Architecture defines the system structure and responsibility boundaries.
Engineering defines how those boundaries are implemented and preserved.

⸻

2. Constitutional Principle

Noema must be engineered so that its implementation cannot silently turn probabilistic interpretation into authoritative execution.

The fundamental engineering boundary is:

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

Every implementation must preserve the semantic distinction between these stages.

No component may acquire authority merely because it happens to have technical access to another component.

⸻

3. Engineering Authority

The Engineering Constitution is subordinate to the canonical Noema architecture and ontology.

Engineering implementations must conform to:

1. canonical ontology
2. canonical architectural boundaries
3. Trust semantics
4. Action Contract semantics
5. execution semantics
6. this Engineering Constitution

Implementation convenience must not override a canonical boundary.

Where implementation pressure conflicts with an architectural invariant, the implementation must change.

The architecture must not be silently weakened to accommodate an implementation shortcut.

⸻

4. Separation of Concerns

Noema components must have explicit responsibilities.

At minimum, engineering must preserve separation between:

Interpretation
Intent
Validation
Trust
Action Graph
Action Contract
Execution
Outcome

A component may consume information from another component without becoming the owner of that component’s responsibility.

For example:

* the Intent Engine may consume Context
* Trust may consume Intent
* the Action Graph may consume Trust results
* Execution may consume Action Contracts
* Outcome may reference execution evidence

But:

Intent Engine ≠ Trust Engine
Trust ≠ Execution
Action Graph ≠ Authorization
Action Contract ≠ Capability
Execution ≠ Outcome
Noema ≠ External Business System

These distinctions are constitutional.

⸻

5. Authority Must Be Explicit

Technical access does not constitute semantic authority.

A service having the ability to call an external API does not mean it is authorized to perform the operation.

A model having access to a tool does not mean it is permitted to invoke the tool.

A component possessing data does not mean it owns that data.

Engineering implementations must therefore distinguish:

Access
Capability
Authorization
Authority
Execution

These are separate concepts.

⸻

6. No Implicit Authority

Noema must never derive authority from:

* model confidence
* component location
* API availability
* possession of credentials
* existence of a tool
* presence of an Action in a graph
* successful previous execution
* conversational continuation
* implementation-level defaults

Authority must be established through the applicable canonical mechanism.

⸻

7. Model Boundary

Models are probabilistic components.

They may assist Noema with:

* interpretation
* extraction
* candidate generation
* ambiguity detection
* clarification generation
* candidate Action Graph construction
* candidate Action selection
* explanation
* classification

Model output must not automatically become canonical system state.

The engineering boundary is:

Model Output
      ↓
Candidate Representation
      ↓
Deterministic Processing
      ↓
Canonical State

Never:

Model Output
      ↓
Authoritative State

without the applicable deterministic validation and control boundary.

⸻

8. No Direct Consequential Tool Execution

A model must not directly perform consequential Actions outside the canonical execution path.

The implementation must preserve:

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
Execution Consumer
  ↓
External System

A tool interface is an implementation mechanism.

It is not an authority mechanism.

⸻

9. Canonical State

Canonical Noema state must be represented using explicit schemas.

Engineering implementations must avoid treating:

* prompts
* model messages
* arbitrary JSON
* tool-call payloads
* logs
* natural-language descriptions

as substitutes for canonical state.

Canonical state must have:

* defined identity
* defined schema
* version semantics
* provenance where applicable
* lifecycle semantics
* validation rules

⸻

10. Strong Typing at Authority Boundaries

Where practical, authority-bearing objects should be strongly typed.

Examples include:

Intent
IntentVersion
ValidationResult
TrustEvaluation
ActionGraph
ActionNode
ActionContract
Capability
ExecutionRequest
ExecutionResult
Outcome
Evidence
Provenance

Unstructured model output must not cross an authority boundary without conversion into the appropriate canonical representation.

⸻

11. Identity

Canonical entities must have stable identities independent of their versions.

For example:

intent_id
intent_version

rather than treating the entire serialized object as its identity.

The same principle applies where applicable to:

* Action Graphs
* Action Nodes
* Action Contracts
* execution attempts
* outcomes
* evidence
* evaluations

Identity semantics must be deterministic and reconstructible.

⸻

12. Versioning

Material semantic changes must produce a new version or another explicitly reconstructible state transition.

Engineering systems must not silently overwrite historical canonical state when doing so would destroy the ability to reconstruct what was previously established.

Versioning must support:

* audit
* replay
* debugging
* revalidation
* Trust reconstruction
* execution reconstruction
* incident analysis

⸻

13. Immutability of Historical Decisions

Historical canonical decisions should be immutable.

Examples include:

* resolved Intent versions
* Trust evaluations
* executed Action Graph versions
* Action Contract versions
* execution records
* Outcome records

Corrections should be represented through explicit subsequent events or versions.

Historical state must not be rewritten merely to make current state appear cleaner.

⸻

14. Event and State Discipline

Noema may use event-driven or state-oriented implementation models.

Regardless of implementation style, material state transitions must have explicit causes.

A state must not change merely because:

* a model generated a different answer
* a prompt was reformulated
* a worker restarted
* a retry occurred without policy
* a timeout was interpreted as failure
* a component inferred a new state

State transitions must correspond to defined events, contract results, dependencies, or deterministic re-evaluation.

⸻

15. Provenance

Material canonical information must retain provenance sufficient to establish:

* where it came from
* when it was established
* which version established it
* which evidence supported it
* which rule or process produced it
* whether it originated from the Actor, model, context, external evidence, or deterministic processing

Provenance must distinguish:

ACTOR
MODEL
CONTEXT
EXTERNAL_EVIDENCE
DETERMINISTIC_RULE
DEFAULT
CLARIFICATION
SYSTEM

as applicable.

⸻

16. Provenance Is Not Chain-of-Thought

Noema must preserve decision provenance without requiring retention of private model reasoning.

The engineering objective is reconstructibility of canonical decisions, not storage of hidden reasoning traces.

It must be possible to establish:

What was established?
Why was it established?
What evidence supported it?
Which rule/version produced it?
What happened afterward?

without requiring private model chain-of-thought.

⸻

17. Determinism

Where Noema defines deterministic rules, those rules must be implemented deterministically.

Given the same relevant:

input
context
evidence
rules
versions
configuration

the resulting canonical decision should be reproducible where the architecture requires it.

Model variability must not silently alter deterministic semantics.

⸻

18. Configuration Is Part of System Semantics

Configuration that can materially affect:

* Intent resolution
* validation
* Trust
* graph construction
* Action selection
* execution
* retry
* compensation
* policy

must be versioned or otherwise reconstructible.

A production decision must not depend on an unrecorded configuration state.

⸻

19. Unknown Is a First-Class State

Engineering systems must distinguish:

KNOWN
UNKNOWN
MISSING
AMBIGUOUS
INVALID
FAILED

where the relevant domain requires those distinctions.

Unknown must never silently become:

FALSE

or:

TRUE

or:

FAILED

unless the applicable semantics explicitly define that conversion.

⸻

20. No Silent Defaults

Defaults must be explicit.

A default may be used only where:

1. the relevant semantics permit it
2. the default rule is defined
3. its scope is known
4. its provenance can be recorded
5. its application is deterministic

Convenience must never be used to conceal missing information.

⸻

21. Validation Boundary

Validation must be explicit and machine-readable.

Validation must establish whether a canonical object satisfies its applicable structural and semantic requirements.

Validation must not be replaced by:

* model confidence
* successful parsing
* schema shape alone
* API acceptance
* natural-language plausibility

A structurally valid object may still be semantically invalid.

⸻

22. Trust Boundary

Trust is an independent control boundary.

Engineering systems must not convert:

Resolved

into:

Trusted

automatically.

Likewise:

Graph exists

does not mean:

Execution authorized

Trust state must remain distinct from Intent, graph, and execution state.

⸻

23. Action Graph Boundary

The Action Graph must be explicit and inspectable.

It must represent the relevant:

* Actions
* dependencies
* conditions
* inputs
* outputs
* capabilities
* execution relationships
* failure semantics

An opaque model-generated sequence must not become the authoritative execution structure.

A model may propose a graph.

Deterministic processing must establish whether the graph is valid and executable.

⸻

24. No Hidden Actions

Engineering implementations must not silently perform consequential operations that are absent from the declared execution semantics.

If an operation is required, it must be:

1. represented explicitly as an Action, or
2. explicitly defined as part of an Action Contract’s execution semantics.

This prevents execution from diverging from the declared graph.

⸻

25. Action Contract Boundary

Every executable Action must resolve to an applicable Action Contract.

The Action Contract defines the executable interface and obligations associated with the Action.

Engineering must not infer contractual behavior from:

* Action names
* natural-language descriptions
* model-generated instructions
* undocumented provider behavior

The contract is the executable boundary.

⸻

26. Capability and Authorization

Engineering must preserve:

Capability ≠ Authorization

A capability establishes that an operation is available.

Authorization establishes whether the operation may be performed in the specific context.

The existence of:

card.replacement.create

does not establish that the Actor may invoke it.

⸻

27. External Systems Remain Authoritative

Noema must not silently become the system of record for business state owned by an external system.

Examples include:

* account status
* payment status
* card status
* inventory
* customer records
* delivery status

Noema may cache or reference such information where appropriate.

It must preserve the distinction between:

Noema's representation of a fact

and:

authoritative external business state

⸻

28. Execution-Time Authority

Pre-execution validation does not guarantee that external conditions remain valid.

Engineering systems must account for:

Time of Check
      ≠
Time of Use

Where required, Action Contracts or execution consumers must perform final authoritative checks.

A stale precondition must not be treated as current merely because it was previously validated.

⸻

29. Execution Is Not Success

An executable Action establishes permission and structure for execution.

It does not guarantee successful completion.

The system must distinguish:

AUTHORIZED / EXECUTABLE

from:

EXECUTED

and:

SUCCESSFUL

An external system may reject or fail an otherwise valid Action.

⸻

30. Outcome Is Distinct From Execution

Execution records what the consumer attempted or performed.

Outcome records what Noema establishes happened.

The engineering model must support outcomes such as:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN

as applicable.

⸻

31. Unknown Execution Results

Timeouts and transport failures must not automatically be interpreted as execution failure.

For example:

REQUEST_PAYMENT
      ↓
network timeout
      ↓
UNKNOWN

may be correct if the payment provider may have accepted the request.

Engineering must preserve uncertainty until authoritative state can establish the result.

⸻

32. Idempotency

Retryable Actions must have explicit idempotency semantics where appropriate.

An uncertain response must not cause duplicate consequential operations.

For example:

CREATE_PAYMENT

must not create multiple payments merely because the caller cannot determine whether the first request succeeded.

Idempotency belongs primarily to the Action Contract and execution architecture, but all orchestration components must respect it.

⸻

33. Retry Discipline

Retries must be explicit and bounded.

A retry policy should define, where applicable:

* retryable failures
* maximum attempts
* timeout
* backoff
* idempotency requirements
* termination condition
* escalation behavior

The system must never retry indefinitely because an operation has not produced a satisfactory result.

⸻

34. Compensation

Compensation must be explicit.

Engineering must not assume that:

Compensation = Rollback

External systems may not support transactional rollback.

Compensation may therefore produce a new business operation rather than restore the original state.

Compensation requirements must be represented in the applicable execution semantics.

⸻

35. Durable Execution

Long-running execution must be durable across:

* process termination
* worker failure
* network interruption
* deployment
* infrastructure restart
* temporary dependency failure

Execution state must not exist solely in ephemeral process memory when recovery is required.

The system must be able to reconstruct:

what was pending
what completed
what failed
what was unknown
what may be retried
what requires intervention

without relying on the memory of a particular worker.

⸻

36. No Duplicate Consequential Execution

A recovered worker must not blindly repeat an Action merely because the previous worker disappeared.

Before retrying a consequential Action, the execution system must respect:

* idempotency
* execution attempt state
* provider semantics
* contract requirements
* outcome uncertainty

Worker failure is not equivalent to Action failure.

⸻

37. Concurrency

Concurrent execution must be explicit.

Two Actions may execute concurrently only where:

* dependencies permit it
* contracts permit it
* resource constraints permit it
* atomicity permits it
* external system semantics permit it
* execution safety permits it

Visual independence in a graph is insufficient by itself.

⸻

38. Ordering

Required ordering must be represented explicitly.

Engineering implementations must not reorder Actions merely to improve performance when ordering semantics prohibit it.

Optimization is subordinate to:

* Intent semantics
* dependencies
* Trust
* Action Contracts
* policy
* authorization
* atomicity
* safety

⸻

39. Atomicity

Engineering must never infer atomicity merely because multiple Actions belong to the same Intent.

The system must explicitly establish whether a group is:

ATOMIC
INDEPENDENT
PARTIALLY_EXECUTABLE
COMPENSATABLE

as applicable.

⸻

40. Partial Execution

Partial execution must be explicit.

If an Intent does not permit partial execution, individually executable nodes must not be executed merely because they are technically available.

For example:

A = READY
B = BLOCKED
C = READY

does not authorize:

Execute A
Execute C

when the Intent requires all-or-nothing behavior.

⸻

41. Human Intervention

Human intervention must be represented explicitly where required.

For example:

ACTION
  ↓
HUMAN_REVIEW
  ↓
CONTINUE

must remain distinct from:

ACTION
  ↓
FAILED

Human review is a governance state, not an execution failure.

⸻

42. Approval

Approval is an explicit governance dependency.

An Action requiring approval must not execute before the applicable approval condition is satisfied.

Approval must not automatically remain valid after a material change to the Intent, graph, authorization, or relevant execution conditions.

Material changes require the applicable re-evaluation.

⸻

43. Confirmation

Actor confirmation must be represented explicitly where required.

Conversational continuation must not automatically be interpreted as confirmation.

A confirmation event must be attributable to the relevant Actor and Intent and must satisfy the applicable confirmation semantics.

⸻

44. Cancellation

Cancellation must be explicit.

Cancellation must be distinguishable from:

FAILED
BLOCKED
EXPIRED
REJECTED

If execution has already begun, cancellation semantics must respect the state of the relevant Actions and external systems.

Noema must not claim successful cancellation merely because a cancellation request was issued.

⸻

45. Temporal Semantics

Time-sensitive state must be explicit.

Engineering systems must account for:

* expiration
* deadlines
* timeouts
* validity windows
* scheduling
* delayed execution
* stale state
* temporal policy changes

A previously valid decision must not automatically remain valid indefinitely.

⸻

46. State Machines

Canonical lifecycle states should be represented as explicit state machines where appropriate.

State transitions must be:

* defined
* valid
* observable
* auditable
* attributable to an event or deterministic evaluation

Illegal state transitions must be rejected.

⸻

47. Trust State and Execution State

Trust state must not be reused as execution state.

For example:

Trust:
READY
Execution:
NOT_STARTED

is valid.

Later:

Trust:
READY
Execution:
FAILED

is also valid.

Execution failure does not retroactively imply that the Trust decision was incorrect.

⸻

48. Graph State and Execution State

Graph readiness and execution status must remain distinguishable.

A graph may be:

VALID

while execution is:

NOT_STARTED

or:

FAILED

The implementation must not collapse graph validity into execution outcome.

⸻

49. Re-Evaluation

Material changes must trigger the appropriate re-evaluation.

Examples include:

* Intent changes
* authorization changes
* policy changes
* capability changes
* Action Contract changes
* dependency changes
* external business-state changes
* relevant context changes
* expiration

Noema must not silently continue executing a stale representation.

⸻

50. Stale State

Engineering systems must identify when a representation depends on state that may no longer be current.

A stale object must not cross an authority boundary merely because it was once valid.

Where necessary, the system must:

Detect
   ↓
Invalidate
   ↓
Revalidate
   ↓
Re-evaluate
   ↓
Continue / Revise / Stop

⸻

51. Reconciliation

Where Noema and an external system may disagree about execution state, reconciliation must favor the authoritative external system for its domain.

Noema should preserve:

* previous local state
* external evidence
* reconciliation event
* resulting state
* provenance

A reconciliation must not erase the historical discrepancy.

⸻

52. Failure Handling

Failures must be classified rather than collapsed into generic errors.

Relevant classes may include:

VALIDATION_FAILURE
TRUST_BLOCK
DEPENDENCY_FAILURE
CONTRACT_FAILURE
AUTHORIZATION_FAILURE
EXTERNAL_SYSTEM_FAILURE
NETWORK_FAILURE
TIMEOUT
UNKNOWN_OUTCOME
POLICY_FAILURE
CONFIGURATION_FAILURE
INTERNAL_FAILURE

The exact taxonomy may evolve.

The engineering requirement is that failure semantics remain explicit enough to drive deterministic handling.

⸻

53. Error Handling

Errors crossing component boundaries should be structured.

Machine-readable error identity should accompany human-readable information where appropriate.

An error should preserve sufficient context to establish:

* component
* operation
* object identity
* relevant version
* failure class
* timestamp
* correlation identity
* retryability where applicable

⸻

54. No Error Masking

Engineering components must not convert meaningful uncertainty or failure into apparent success.

Examples prohibited:

timeout → SUCCESS
unknown → FALSE
missing → default
authorization failure → generic unavailable
contract rejection → completed

unless the governing semantics explicitly define that transformation.

⸻

55. Observability

Every consequential lifecycle stage must be observable.

At minimum, engineering should support inspection of:

* Intent identity/version
* validation result
* Trust evaluation
* graph identity/version
* Action identity
* Action Contract identity/version
* capability
* execution attempt
* state transition
* failure
* retry
* compensation
* human intervention
* outcome

Observability must not require access to hidden model reasoning.

⸻

56. Correlation

Related events across components must be correlatable.

A lifecycle should permit reconstruction across:

Intent
→ Validation
→ Trust
→ Graph
→ Contract
→ Execution
→ Outcome

Correlation identifiers must not replace canonical object identity.

They serve a different purpose:

Identity = what object is this?
Correlation = what lifecycle/process is this part of?

⸻

57. Auditability

Material system decisions must be auditable.

An auditor should be able to reconstruct:

1. what the Actor expressed
2. what Intent was established
3. which version was used
4. what validation established
5. what Trust evaluation established
6. which graph was selected
7. which contracts governed execution
8. what Actions executed
9. what failures occurred
10. what external outcomes were observed
11. what final Outcome was established

⸻

58. Audit Integrity

Audit records must not be mutable merely because current system state has changed.

Historical records must preserve the state and evidence relevant at the time of the decision or event.

Corrections should be additive and attributable.

⸻

59. Security Boundary

Security must be enforced independently of model behavior.

A compromised or manipulated model must not be able to obtain additional authority by:

* naming a privileged Action
* constructing a privileged graph
* requesting an unrestricted tool
* changing an Action parameter
* modifying a capability reference
* asserting authorization
* claiming prior approval

Security controls must operate outside the model’s authority.

⸻

60. Least Privilege

Components and execution consumers should receive only the capabilities required for their defined responsibilities.

No component should receive broad authority merely because future functionality might require it.

Least privilege applies to:

* services
* workers
* credentials
* tools
* Action Contracts
* external APIs
* data access

⸻

61. Credential Isolation

Credentials and secrets must not become part of ordinary semantic representations.

They must not be embedded in:

* Intent
* Action Graph
* model prompts
* model output
* audit records
* ordinary provenance
* user-visible explanations

Credential material belongs to the appropriate secure execution infrastructure.

⸻

62. Data Minimization

Components should consume only the information required for their responsibility.

The Intent Engine should not receive unrestricted business data merely because it might be useful for inference.

Execution consumers should not receive unrelated semantic context merely because it exists upstream.

Data access must follow explicit boundaries.

⸻

63. Model Input Security

Untrusted external content must not be treated as system authority merely because it appears inside model context.

External content may contain:

* instructions
* tool references
* policy-like language
* malicious directives
* fabricated authority claims

Engineering must preserve the distinction between:

Data

and:

Authority

⸻

64. Prompt Injection Resistance

Noema must not permit content encountered during execution or information retrieval to silently redefine:

* Intent
* Trust
* authorization
* Action Contract
* graph structure
* policy
* system instructions

Untrusted content may provide evidence.

It does not become authority merely by being retrieved.

⸻

65. External Evidence

External evidence used in semantic or execution decisions must preserve:

* source
* retrieval time
* relevant version or identifier
* evidence reference
* provenance

Where external evidence is authoritative for a business fact, Noema should reference rather than impersonate that authority.

⸻

66. API Boundaries

External integrations must be treated as explicit capability boundaries.

Each integration should define:

* supported operations
* inputs
* outputs
* authentication requirements
* authorization requirements
* failure semantics
* timeout behavior
* idempotency
* rate limits where relevant
* authoritative state
* version compatibility

⸻

67. Contract Evolution

Action Contracts and integration contracts evolve.

Engineering must not silently assume that a newer contract is semantically equivalent to an older one.

Contract changes that materially affect execution must be versioned and must participate in graph validation and re-evaluation.

⸻

68. Compatibility

Changes to canonical interfaces must consider:

* backward compatibility
* version compatibility
* persisted historical state
* replay
* long-running execution
* external consumers
* migration

A schema change is not merely a code change when persisted canonical state depends upon it.

⸻

69. Reproducibility

Noema must strive to reproduce historical decisions from the relevant recorded inputs and versions.

For a material decision, reconstruction may require:

Intent Version
Context Version
Evidence
Rule Versions
Policy Version
Trust Evaluation
Graph Version
Action Contract Version
Configuration Version

The exact set depends on the decision.

⸻

70. Replay

Replay must not accidentally cause consequential Actions to execute again.

Engineering systems must distinguish:

Replay for reconstruction

from:

Execution retry

A replay operation must default to non-consequential analysis unless explicitly authorized otherwise.

⸻

71. Deterministic Testing

Canonical semantic and governance logic should be tested using deterministic fixtures.

Tests should cover:

* valid states
* invalid states
* unknown states
* ambiguous states
* conflicting evidence
* stale state
* material changes
* authorization boundaries
* retries
* unknown outcomes
* partial execution
* compensation
* concurrency
* recovery

⸻

72. Property and Invariant Testing

Where practical, engineering should test invariants rather than only example cases.

Examples:

Unresolved Intent
→ cannot become Executable without resolution
Unauthorized Action
→ cannot cross execution boundary
Missing dependency
→ cannot become READY
Unknown mandatory condition
→ cannot become satisfied implicitly
Stale graph
→ cannot silently execute
Retry without idempotency
→ must not be treated as safe by default

⸻

73. Failure Injection

Durable execution systems should be tested under realistic failure conditions.

Examples include:

* worker termination
* process restart
* network timeout
* duplicate delivery
* delayed response
* external system rejection
* partial dependency failure
* database interruption
* deployment during execution

The objective is to establish that failure does not silently corrupt canonical state.

⸻

74. Concurrency Testing

Concurrent execution must be tested for:

* duplicate execution
* race conditions
* stale reads
* lost updates
* ordering violations
* incorrect dependency resolution
* inconsistent state transitions

Concurrency must be treated as a semantic concern where it affects execution correctness.

⸻

75. Database and Persistence Discipline

Persistent state must reflect canonical lifecycle semantics.

Transactions should protect state transitions where atomicity is required.

Persistence must not create false guarantees that do not exist across external systems.

A database transaction within Noema does not make an external API operation transactional.

⸻

76. Distributed Systems Principle

Noema must assume that distributed operations can experience:

* delay
* duplication
* reordering
* partial failure
* lost communication
* stale state
* uncertain outcomes

Engineering must not rely on an idealized synchronous execution model.

⸻

77. Exactly-Once Claims

Noema must not claim exactly-once execution merely because a local queue or database provides exactly-once-like processing semantics.

Exactly-once business effect depends on the external system and Action Contract.

Where external systems provide only at-least-once semantics, Noema must use appropriate idempotency and reconciliation mechanisms.

⸻

78. Queue and Worker Semantics

Queues must not be treated as authority boundaries.

A queued Action remains governed by:

* its Intent
* Trust decision
* Action Graph
* Action Contract
* authorization
* validity window
* execution conditions

Queue delivery does not itself authorize execution.

⸻

79. Long-Running Operations

Long-running operations must preserve their governing context.

A worker resuming an operation must establish that the:

* Intent remains applicable
* Trust requirements remain satisfied
* Action Contract remains valid
* capability remains available
* relevant authorization remains valid
* execution conditions remain satisfied

where the semantics require re-evaluation.

⸻

80. No Silent Replanning

Execution systems must not silently replace an Action Graph with a new strategy because an Action failed.

Replanning is a semantic event.

Where replanning is permitted, the system must:

Failure / Material Change
        ↓
Re-evaluation
        ↓
Candidate Revision
        ↓
Validation
        ↓
Trust / Contract Checks
        ↓
New Graph Version

A worker must not improvise a new plan.

⸻

81. Optimization

Engineering may optimize:

* latency
* throughput
* resource usage
* cost
* parallelism
* external calls

but optimization must not alter:

* Intent semantics
* authorization
* Trust
* policy
* Action Contract obligations
* atomicity
* safety
* required audit behavior

Optimization is subordinate to correctness.

⸻

82. Caching

Caching must preserve semantic validity.

A cached value must not be treated as authoritative beyond its defined validity semantics.

Where cached information can affect consequential execution, the system must establish whether:

* freshness is sufficient
* authoritative re-check is required
* expiration applies
* invalidation is required

⸻

83. Observability Must Not Become Authority

Logs, metrics, traces, dashboards, and monitoring systems describe system state.

They must not become sources of canonical authority merely because operators can modify them.

Operational tooling must not silently mutate Intent, Trust, or execution state outside defined control paths.

⸻

84. Administrative Operations

Administrative overrides, where the architecture permits them, must be:

* explicitly authorized
* attributable
* auditable
* scoped
* time-bounded where appropriate
* distinguishable from ordinary system behavior

An operator override must not be represented as if it were an ordinary deterministic system decision.

⸻

85. Human Override

Where human override is supported, the system must preserve:

original state
override event
actor
authority
reason
timestamp
resulting state

Override must not erase the original decision history.

⸻

86. Deployment Safety

Deployments must account for long-lived Noema state.

A deployment must not invalidate:

* persisted Intent versions
* active execution graphs
* Action Contracts
* pending executions
* event schemas
* audit records

without an explicit migration or compatibility strategy.

⸻

87. Schema Migration

Schema migrations must preserve historical meaning.

Where an old representation cannot be losslessly transformed into a new representation, the system must retain the original representation or an equivalent reconstructible form.

Migration must not rewrite history into a semantically different representation without recording the transformation.

⸻

88. Feature Flags

Feature flags that alter canonical behavior must be treated as semantic configuration.

Their values must be observable and reconstructible for decisions where they materially affect:

* resolution
* validation
* Trust
* graph construction
* execution
* outcome

⸻

89. Engineering Documentation

Every authority-bearing component must document:

* responsibility
* inputs
* outputs
* invariants
* state transitions
* failure semantics
* dependencies
* security boundaries
* external authorities
* versioning behavior

Documentation is part of engineering correctness when it defines architectural contracts.

⸻

90. Component Boundary Requirement

Every Noema component must have a clearly defined boundary.

A component specification should answer:

1. What does it own?
2. What does it consume?
3. What does it produce?
4. What authority does it possess?
5. What authority does it not possess?
6. What state does it own?
7. What external systems does it depend on?
8. What invariants must it preserve?

If these cannot be answered, the component boundary is insufficiently defined.

⸻

91. Dependency Discipline

Components should depend on explicit interfaces rather than implementation details.

A dependency must identify:

* purpose
* interface
* authority
* failure behavior
* version semantics

Circular dependencies that collapse architectural boundaries should be avoided.

⸻

92. No Hidden Cross-Layer Coupling

A component must not acquire another component’s responsibility through an incidental dependency.

Examples:

Execution Worker → directly mutates Intent
Model Adapter → directly changes Trust
Action Graph → directly grants authorization
Context Service → directly executes Actions

Such behavior violates architectural separation.

⸻

93. Canonical Interface Principle

Cross-component communication should use canonical representations wherever the architecture defines them.

For example:

Intent → Validation

should not require an undocumented model-specific representation.

Likewise:

Action Graph → Execution

must resolve through the defined Action Contract boundary.

⸻

94. No Stringly-Typed Authority

Critical authority-bearing fields must not rely solely on arbitrary strings where a canonical identifier or typed representation is required.

Examples include:

* Action identity
* capability identity
* contract identity
* policy identity
* state
* dependency type
* outcome
* failure class

Human-readable labels may accompany canonical identifiers.

They must not replace them.

⸻

95. State Transition Audit

Material state transitions should produce auditable records.

At minimum:

previous state
new state
event/cause
object identity
version
timestamp
actor/system source

where applicable.

⸻

96. Event Ordering

Engineering must not assume global ordering unless the underlying architecture explicitly provides it.

Where ordering matters, the relevant scope must be defined.

Examples:

* per Intent
* per execution
* per Action
* per external resource

Global ordering should not be simulated where it is unnecessary or unavailable.

⸻

97. Clock Discipline

Time-dependent decisions must use a defined time source.

Engineering must distinguish:

* event time
* processing time
* external system time
* expiration time
* scheduled execution time

A local worker clock must not silently override authoritative external timestamps where those timestamps govern business state.

⸻

98. Security and Audit Tradeoffs

Security controls must not destroy the provenance necessary to audit consequential decisions.

Likewise, audit requirements must not expose secrets or unnecessarily sensitive information.

Engineering must preserve:

Auditability
+
Data Minimization
+
Credential Isolation

simultaneously.

⸻

99. Privacy by Boundary

Sensitive data should remain within the smallest necessary architectural boundary.

Model access, logging, telemetry, and external integration must not automatically receive all upstream data.

Data propagation must have a defined purpose.

⸻

100. Noema Must Fail Closed at Authority Boundaries

When a required authority condition cannot be established, Noema must not assume permission.

Examples:

Authorization unknown
→ do not execute
Required approval unknown
→ do not execute
Mandatory condition unknown
→ do not execute
Action Contract unresolved
→ do not execute
Capability identity unresolved
→ do not execute

This does not mean every informational operation must fail closed.

The principle applies where the unresolved condition is required for consequential execution.

⸻

101. Engineering and Clarification

Engineering systems must preserve unresolved semantic state rather than forcing premature completion.

For example:

recipient = AMBIGUOUS

must remain representable.

The implementation must not require every Intent object to be artificially complete merely because downstream schemas prefer complete objects.

⸻

102. Engineering and Candidate State

Candidate representations must remain distinguishable from canonical representations.

Examples:

Candidate Intent
Canonical Intent
Candidate Action Graph
Executable Action Graph
Candidate Capability
Bound Capability
Proposed Action
Executable Action

Candidate state must never cross into authoritative execution merely through serialization or persistence.

⸻

103. Canonical Execution Boundary

The execution boundary is the point at which Noema permits a consequential Action to be performed.

Before crossing it, the implementation must establish the applicable:

* Intent state
* validation state
* Trust state
* Action Graph state
* Action Contract
* capability
* authorization
* execution conditions

The exact requirements depend on the Action Contract.

⸻

104. Consumer Authority

The execution consumer remains authoritative for execution-time conditions within its domain.

Therefore:

Noema:
Graph valid
Trust ready
Contract valid
Consumer:
Precondition no longer satisfied

may legitimately result in:

Execution rejected

The consumer’s rejection does not automatically imply that the preceding Intent or Trust decision was malformed.

⸻

105. External Side Effects

External side effects must be attributable to an explicit execution attempt.

A consequential side effect should be traceable to:

Intent
→ Graph
→ Action
→ Contract
→ Execution Attempt
→ External Operation

where the relevant integration supports such correlation.

⸻

106. Side-Effect Boundaries

Engineering must distinguish:

Read

from:

Write / Consequential Action

Read operations may support resolution or validation.

Write operations require the applicable execution controls.

A model must not transform an informational capability into a consequential capability through arbitrary parameter construction.

⸻

107. Outcome Verification

Where required, successful API acceptance must not automatically be treated as successful business outcome.

For example:

Request accepted

may differ from:

Business operation completed

Action Contracts should define whether postcondition verification is required.

⸻

108. No False Completion

Noema must not record an Action or Intent as complete merely because:

* a request was sent
* a worker stopped
* a queue accepted a message
* an API returned HTTP success
* a model stated that the task was complete

Completion must be established according to the relevant execution and postcondition semantics.

⸻

109. Engineering Change Discipline

Changes to foundational behavior must identify their effect on:

* ontology
* architecture
* state machines
* Action Contracts
* persistence
* audit
* execution
* compatibility

A code change that changes semantics is an architectural change even if its diff is small.

⸻

110. Backward Compatibility Must Not Preserve Incorrect Semantics

Compatibility is subordinate to canonical correctness.

If an older interface permits behavior that violates a new foundational invariant, compatibility mechanisms must not silently preserve that unsafe behavior.

Migration must be explicit.

⸻

111. Experimental Features

Experimental implementations must not silently become canonical behavior.

Experimental features should have explicit status and must be isolated from foundational semantics until adopted.

⸻

112. Implementation Freedom

The Engineering Constitution does not mandate a specific:

* programming language
* database
* queue
* workflow engine
* model provider
* cloud provider
* orchestration framework

unless another canonical specification explicitly does so.

Implementation choices remain open provided they preserve the constitutional invariants.

⸻

113. Technology Is Subordinate to Semantics

Noema must not reshape its semantic architecture merely to fit the abstractions of a selected technology.

Examples:

Database model ≠ canonical ontology
Workflow engine ≠ Action Graph
LLM agent loop ≠ Trust system
API gateway ≠ Authorization model
Queue ≠ execution authority
Prompt ≠ Intent
Tool call ≠ Action Contract

Technology implements Noema.

Technology does not define Noema’s authority model.

⸻

114. Engineering Review Requirement

Foundational changes should be reviewed against:

* architectural boundaries
* canonical invariants
* state transitions
* authority boundaries
* failure semantics
* provenance
* auditability
* security
* backward compatibility

A feature is not complete merely because its happy path works.

⸻

115. Operational Readiness

A consequential component should not be considered production-ready without defined behavior for:

* normal execution
* invalid input
* missing input
* unknown state
* dependency failure
* timeout
* duplicate request
* retry
* restart
* stale state
* external rejection
* partial execution
* recovery
* audit

⸻

116. Engineering Completeness

An implementation is incomplete if it defines only the success path.

For every consequential operation, engineering must define as applicable:

SUCCESS
FAILURE
UNKNOWN
RETRY
BLOCK
WAIT
CANCEL
TIMEOUT
RECOVERY
COMPENSATION

The applicable subset depends on the Action Contract.

⸻

117. Canonical Lifecycle

The engineering implementation must preserve the canonical lifecycle:

Expression
    ↓
Interpretation
    ↓
Intent Construction
    ↓
Intent Resolution
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
Postcondition Verification
    ↓
Outcome

The implementation may introduce internal stages.

It must not remove or silently merge authoritative boundaries.

⸻

118. Constitutional Invariants

Invariant 1

Model output is never automatically canonical authority.

Invariant 2

Intent state and Trust state are separate.

Invariant 3

Trust and Execution state are separate.

Invariant 4

Capability does not imply authorization.

Invariant 5

An Action Graph does not grant authorization.

Invariant 6

A candidate representation is not an executable representation.

Invariant 7

Every consequential Action must cross an explicit Action Contract boundary.

Invariant 8

Unknown must not silently become known.

Invariant 9

Ambiguity must not silently become a guess.

Invariant 10

Material semantic changes must be reconstructible.

Invariant 11

Historical canonical state must not be silently rewritten.

Invariant 12

External business systems remain authoritative for their business state.

Invariant 13

Pre-execution validation does not eliminate TOCTOU risk.

Invariant 14

Retries must respect idempotency and contract semantics.

Invariant 15

Worker failure does not automatically mean Action failure.

Invariant 16

Unknown execution outcomes must remain unknown until established.

Invariant 17

Partial execution must be explicit.

Invariant 18

Replanning must be explicit and governed.

Invariant 19

Optimization must not alter Intent semantics.

Invariant 20

No hidden consequential Actions may occur outside declared execution semantics.

Invariant 21

No component may acquire authority through implementation convenience.

Invariant 22

Material state transitions must be attributable.

Invariant 23

Security controls must remain independent of model behavior.

Invariant 24

A stale representation must not silently cross an authority boundary.

Invariant 25

Auditability must not depend on access to private model reasoning.

⸻

119. Engineering Review Questions

Every foundational implementation should be answerable through the following questions:

1. What canonical object does this component operate on?
2. What state does it own?
3. What state does it explicitly not own?
4. What authority does it possess?
5. What authority does it not possess?
6. What is the authoritative source for each external fact?
7. Can model output bypass deterministic validation?
8. Can an Action execute without an applicable Action Contract?
9. Can an unknown condition accidentally become satisfied?
10. Can a stale decision cross the execution boundary?
11. Can a retry produce duplicate side effects?
12. Can a worker restart cause duplicate execution?
13. Can partial execution be represented correctly?
14. Can an unknown external outcome be represented?
15. Can the decision be reconstructed later?
16. Can the historical state be audited?
17. Can a compromised component escalate authority?
18. Can the system distinguish failure from unknown?
19. Can the system distinguish candidate state from canonical state?
20. Does implementation convenience violate any architectural invariant?

If these questions cannot be answered, the implementation is not sufficiently specified.

⸻

120. Canonical Mental Model

The Engineering Constitution can be reduced to eight principles:

1. Canonical state must be explicit.
2. Authority must be explicit.
3. Boundaries must remain separate.
4. Uncertainty must remain visible.
5. Material state must be versioned and auditable.
6. Execution must be contract-governed and durable.
7. External systems remain authoritative for their domains.
8. Implementation must preserve architecture rather than redefine it.

Which produces:

Canonical State
      ↓
Explicit Authority
      ↓
Deterministic Control
      ↓
Contracted Execution
      ↓
Durable State
      ↓
Observable Outcome

⸻

121. Final Definition

The Engineering Constitution is Noema’s foundational set of engineering constraints governing how its semantic, governance, execution, and outcome architecture must be implemented.

Its purpose is not to prescribe a particular technology stack.

Its purpose is to make the architectural boundaries enforceable in software.

The central engineering principle is:

Noema must never allow implementation mechanisms, probabilistic model behavior, technical access, or operational convenience to silently become semantic or execution authority.

Therefore:

Models may propose.
Intent Engine establishes Intent.
Validation establishes validity.
Trust establishes execution eligibility.
Action Graph establishes execution structure.
Action Contracts establish executable obligations.
Execution performs permitted Actions.
External systems establish external business state.
Outcome records what Noema establishes actually happened.

And the engineering constitution requires that these boundaries remain explicit, durable, versioned, observable, auditable, and enforceable throughout the lifetime of the system.