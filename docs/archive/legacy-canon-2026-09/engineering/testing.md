> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Testing

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/testing.md

⸻

1. Definition

Testing is Noema’s engineering discipline for establishing, preserving, and continuously verifying the correctness of system behavior across its semantic, trust, execution, durability, security, and operational boundaries.

Testing exists to verify that Noema behaves according to its canonical specifications and invariants under:

* valid inputs
* invalid inputs
* ambiguous inputs
* incomplete information
* changing external state
* failures
* retries
* duplicate delivery
* timeouts
* partial execution
* unknown outcomes
* concurrency
* recovery
* adversarial conditions
* version changes

Testing must verify not merely that individual components function, but that the architectural boundaries between components remain intact.

The central principle is:

Noema must test its invariants and contracts, not merely its implementation.

⸻

2. Purpose

Testing provides evidence that:

* canonical Intent semantics are preserved
* validation remains deterministic where required
* Trust boundaries cannot be bypassed
* Action Graphs remain structurally valid
* Action Contracts are respected
* execution semantics remain correct
* retries do not create unintended effects
* recovery preserves durable state
* unknown outcomes remain unknown until resolved
* external business state is not falsely claimed as Noema state
* security boundaries remain enforced
* observability remains sufficient for reconstruction
* material state transitions remain auditable
* changes do not silently violate architectural invariants

Testing is therefore part of the engineering control system.

⸻

3. Testing Boundary

Testing does not replace:

* Validation
* Trust
* authorization
* Action Contracts
* runtime safeguards
* external system controls

Instead, testing verifies that these mechanisms behave according to their specifications.

Conceptually:

Architecture
     ↓
Specifications
     ↓
Invariants
     ↓
Implementation
     ↓
Tests
     ↓
Evidence

A passing test does not create permission.

A test demonstrates that an implementation satisfies a defined requirement under a defined condition.

⸻

4. Core Principle

Noema must not define correctness solely as:

function returned expected value

Correctness may include:

semantic correctness
+
state correctness
+
authorization correctness
+
contract correctness
+
failure correctness
+
durability correctness
+
security correctness
+
observability correctness

An implementation that produces the expected output while violating an architectural boundary is not correct.

⸻

5. Testable Invariants

Every foundational architectural invariant should be translated into testable engineering behavior where practical.

Examples:

Ambiguous Intent
      ↓
Clarification / unresolved

must not become:

Ambiguous Intent
      ↓
Best guess
      ↓
Execution

Similarly:

Candidate Action Graph
      ↓
Validation
      ↓
Trust
      ↓
Contract
      ↓
Execution

must not become:

Model
 ↓
Arbitrary Tool Call

Testing should therefore verify architectural boundaries as executable properties.

⸻

6. Testing Layers

Noema should use multiple complementary testing layers.

Conceptually:

Unit Tests
    ↓
Component Tests
    ↓
Contract Tests
    ↓
Integration Tests
    ↓
System Tests
    ↓
End-to-End Tests
    ↓
Failure / Recovery Tests
    ↓
Security Tests
    ↓
Production Verification

Each layer answers different questions.

No single test layer is sufficient.

⸻

7. Unit Testing

Unit tests verify isolated deterministic behavior.

Suitable targets include:

* Intent resolution rules
* schema validation
* state-transition functions
* dependency evaluation
* retry calculations
* idempotency-key generation
* graph validation
* policy evaluation
* error classification
* serialization
* version comparison
* invariant enforcement

Unit tests should be:

* deterministic
* fast
* isolated
* repeatable

Unit tests should not be used as evidence that distributed execution is correct.

⸻

8. Component Testing

Component tests verify behavior at architectural component boundaries.

Examples include:

Intent Engine
Validation Engine
Trust Engine
Action Graph Engine
Execution Runtime
Durability Layer
Observability Layer
Policy Engine

Component tests should verify both:

* component behavior
* component boundary contracts

For example, an Intent Engine test should establish that a materially ambiguous reference remains unresolved rather than merely verifying that a parser extracted a string.

⸻

9. Contract Testing

Contract tests verify that independently implemented components agree on their interfaces and obligations.

Important contracts include:

* Intent schema
* Validation results
* Trust state transitions
* Action Graph schema
* Action Contract schema
* execution requests
* execution outcomes
* error classifications
* event schemas
* persistence interfaces
* capability interfaces

A contract test should establish that:

Producer
   ↓
Contract
   ↓
Consumer

remains compatible.

Contract changes should be explicit and versioned where required.

⸻

10. Intent Engine Testing

Intent Engine tests should verify:

* candidate versus canonical Intent distinction
* semantic resolution
* ambiguity detection
* clarification requirements
* contextual resolution
* deterministic defaults
* provenance
* Intent versioning
* supersession
* cancellation
* expiration
* partial information
* unknown information
* conflicting context
* unsupported objectives

Example:

"Send ₦50,000 to John."

with multiple valid Johns should produce an unresolved or clarification-required result rather than an arbitrary recipient.

⸻

11. Validation Testing

Validation tests should verify:

* structural validity
* semantic validity
* required-field enforcement
* type correctness
* reference validity
* constraint enforcement
* unknown-state handling
* deterministic validation results

The test suite must distinguish:

VALID
INVALID
INCOMPLETE
UNKNOWN

where those states are part of the applicable specification.

Unknown must not silently become valid.

⸻

12. Trust Testing

Trust tests should verify that execution eligibility is determined according to the Trust specification.

Tests should cover:

* authorization
* policy
* risk controls
* approvals
* confirmations
* trust state transitions
* material Intent changes
* stale trust decisions
* revocation
* re-evaluation
* blocked execution
* waiting states

A critical invariant is:

Intent State ≠ Trust State

Tests must prevent one state machine from silently substituting for the other.

⸻

13. Action Graph Testing

Action Graph tests should verify:

* node identity
* dependency validity
* dependency types
* branch conditions
* convergence
* parallelism
* ordering
* graph acyclicity
* bounded iteration
* preconditions
* postconditions
* capability binding
* contract binding
* graph versioning
* provenance
* graph invalidation
* graph re-evaluation

A graph that appears visually correct but contains an invalid dependency must fail structural validation.

⸻

14. Candidate Graph Testing

Tests must preserve the distinction:

Candidate Graph
      ≠
Executable Graph

A model-generated graph should remain non-executable until it satisfies the required validation, Trust, capability, and Action Contract conditions.

Tests should specifically attempt to bypass those stages.

⸻

15. Execution Testing

Execution tests should verify:

* Action Contract compliance
* precondition enforcement
* input validation
* output handling
* execution state transitions
* failure classification
* retries
* idempotency
* timeout behavior
* unknown outcomes
* compensation
* partial execution
* completion semantics

Execution tests must not assume that an accepted request guarantees successful external execution.

⸻

16. Durable Execution Testing

Durable execution must be tested under interruption.

Representative scenarios include:

Action started
     ↓
process crashes
Action completes externally
     ↓
Noema crashes before recording result
Noema records intent to execute
     ↓
worker terminates
workflow resumes

The system should demonstrate that recovery does not silently:

* duplicate irreversible effects
* lose durable state
* skip required actions
* bypass Trust
* bypass Action Contracts
* fabricate completion

⸻

17. Failure Injection

Failure should be deliberately introduced during testing.

Examples include:

* process termination
* network timeout
* connection reset
* dependency failure
* provider rejection
* database failure
* queue failure
* delayed response
* duplicate response
* malformed response
* unavailable capability
* expired authorization
* changed external state

Failure injection should verify the defined recovery semantics rather than merely demonstrate that the system can fail.

⸻

18. Retry Testing

Retry behavior must be explicitly tested.

Tests should verify:

* maximum attempts
* retryable versus non-retryable errors
* backoff
* timeout
* idempotency
* duplicate delivery
* retry exhaustion
* state after exhaustion

Example:

REQUEST_PAYMENT
      ↓
timeout
      ↓
retry

must not result in two payments merely because the first response was unknown.

⸻

19. Idempotency Testing

Every retryable consequential operation should have appropriate idempotency tests.

Test scenarios should include:

same request
same idempotency key
multiple deliveries

Expected behavior must be explicitly defined.

Tests should verify that:

duplicate delivery
      ≠
duplicate business effect

where the Action Contract requires idempotent behavior.

⸻

20. Unknown Outcome Testing

Unknown execution outcomes require dedicated tests.

Example:

REQUEST_PAYMENT
      ↓
network timeout
      ↓
UNKNOWN

The system must not automatically convert:

UNKNOWN → FAILED

when the external system may have accepted the Action.

Tests should verify subsequent reconciliation behavior.

⸻

21. Partial Execution Testing

Tests must cover partially completed graphs.

Example:

A = COMPLETED
B = COMPLETED
C = FAILED
D = NOT_STARTED

The resulting graph and Intent outcome must preserve those distinctions.

Tests must prevent:

partial execution
      ↓
overall success

unless the applicable semantics explicitly define that result.

⸻

22. Compensation Testing

Compensation behavior should be tested independently from rollback assumptions.

Tests should establish:

* whether compensation is required
* which compensating Actions are permitted
* compensation ordering
* compensation failure
* incomplete compensation
* external non-transactionality
* final outcome semantics

The test suite must not assume:

compensation = rollback

unless the relevant system contract explicitly guarantees that equivalence.

⸻

23. Concurrency Testing

Concurrent execution should be tested for:

* race conditions
* duplicate execution
* conflicting state transitions
* lost updates
* stale reads
* ordering violations
* locking failures
* concurrent retries
* parallel graph branches

Tests should verify that permitted parallelism does not create unauthorized or inconsistent effects.

⸻

24. State-Machine Testing

Noema contains multiple state dimensions.

Tests should verify transitions independently.

Examples:

Intent State
Trust State
Graph State
Execution State
Outcome State

A test must not treat:

READY

as globally meaningful without identifying which state machine it belongs to.

Illegal state transitions should be rejected.

⸻

25. Property-Based Testing

Property-based testing should be used where invariants can be expressed generically.

Examples:

Intent resolution

For any materially ambiguous required field:

resolution != RESOLVED

unless an explicit resolution rule establishes the field.

Graph validation

For any executable graph:

all dependencies reference valid nodes

Idempotency

For an idempotent Action:

repeated equivalent execution
→
single business effect

State transitions

For any state machine:

invalid transition
→
rejected

Property-based tests can expose combinations that example-based tests do not anticipate.

⸻

26. Model Testing

Models are probabilistic components and require specialized testing.

Tests should measure:

* interpretation accuracy
* schema adherence
* ambiguity recognition
* hallucinated entities
* unsupported assumptions
* unsafe tool-selection behavior
* prompt sensitivity
* adversarial inputs
* regression across model versions

Model output must always be evaluated against deterministic downstream controls.

A model passing an interpretation benchmark does not make its output authoritative.

⸻

27. Model Boundary Testing

Tests should deliberately provide model outputs that are:

* syntactically valid but semantically wrong
* plausible but ambiguous
* incomplete
* overconfident
* malicious
* contradictory
* unauthorized
* structurally malformed

The system should demonstrate that these outputs cannot bypass canonical controls.

⸻

28. Prompt and Context Robustness

Where models participate in Intent interpretation or planning, tests should vary:

* wording
* ordering
* irrelevant context
* conflicting context
* adversarial instructions
* injected tool instructions
* malformed context
* repeated requests
* contradictory user statements

The objective is not to force deterministic model output.

The objective is to verify that model variability cannot violate deterministic architectural boundaries.

⸻

29. Security Testing

Security testing should verify:

* authentication
* authorization
* capability isolation
* tenant isolation
* secret handling
* input validation
* injection resistance
* privilege boundaries
* audit integrity
* replay protection
* event integrity
* credential handling
* tool-access boundaries

Security tests should include adversarial attempts to construct unauthorized Action Graphs or Action Contracts.

⸻

30. Authorization Bypass Testing

A critical test category is:

Model proposes privileged Action
        ↓
Action Graph
        ↓
Trust / Authorization

The test must establish that the graph cannot grant authorization merely by containing a privileged Action.

Similarly:

Capability exists

must not imply:

Actor authorized

⸻

31. Tool-Call Boundary Testing

Tests should verify that consequential tool calls cannot bypass the canonical execution path.

For example:

LLM
 ↓
arbitrary tool call

should not become an alternative authority path to:

Intent
 ↓
Trust
 ↓
Action Graph
 ↓
Action Contract
 ↓
Consumer
 ↓
Execution

This should be tested explicitly.

⸻

32. External-System Testing

Integration tests should verify behavior against external system contracts.

Tests should cover:

* success
* rejection
* timeout
* malformed response
* delayed response
* duplicate response
* unavailable service
* changed business state
* stale data
* rate limits

External systems remain authoritative for their business domains.

Tests must therefore avoid treating mocked Noema state as equivalent to authoritative external state.

⸻

33. Contract Mocks and Simulators

Mocks and simulators are useful for deterministic tests.

However, they can conceal integration failures.

Therefore:

Mock Tests
+
Contract Tests
+
Integration Tests

should be used together where appropriate.

Mocks must represent the relevant external contract rather than merely returning whatever response makes the test pass.

⸻

34. Time Testing

Time-dependent behavior requires controlled time.

Tests should cover:

* expiration
* timeout
* retry delay
* backoff
* scheduled execution
* deadline enforcement
* stale authorization
* temporal Intent constraints
* clock skew

Tests should avoid depending on uncontrolled wall-clock timing wherever deterministic time injection is possible.

⸻

35. Event Testing

Noema’s event-driven behavior should be tested for:

* event schema correctness
* ordering where required
* duplicate delivery
* missing events
* delayed events
* replay
* consumer idempotency
* unknown events
* version compatibility

Event processing should remain correct under at-least-once delivery where that is the runtime model.

⸻

36. Persistence Testing

Persistence tests should verify:

* atomic state transitions
* durability
* versioning
* optimistic concurrency where applicable
* recovery
* consistency
* duplicate writes
* transaction boundaries
* migration behavior

A successful in-memory test does not establish durable correctness.

⸻

37. Crash Consistency Testing

Crash consistency should be tested at critical boundaries.

Examples:

before persistence
during persistence
after persistence
before external execution
during external execution
after external execution
before outcome recording

Tests should establish what state Noema can recover after interruption at each boundary.

⸻

38. Recovery Testing

Recovery tests should verify:

Failure
  ↓
Detection
  ↓
Recovery
  ↓
Reconciliation
  ↓
Stable State

The recovered state must preserve the relevant invariants.

Recovery must not be treated as merely restarting a process.

⸻

39. Observability Testing

Observability itself must be tested.

Tests should verify that important operations produce sufficient:

* events
* metrics
* logs
* traces
* correlation identifiers
* execution identifiers
* Intent identifiers
* graph versions
* Action identifiers
* outcome information

Observability must support reconstruction without exposing prohibited secrets or private model reasoning.

⸻

40. Audit Testing

Tests should establish that material changes are auditable.

Examples:

Intent v1
    ↓
Intent v2
Graph v1
    ↓
Graph v2
Trust READY
    ↓
Trust REVOKED

The resulting audit history must preserve the causal transition.

⸻

41. Regression Testing

Every discovered production defect should result in an appropriate regression test where practical.

The regression test should reproduce:

previous failure
      ↓
expected corrected behavior

This prevents recurrence when the implementation changes.

Regression suites should be organized around failure classes and invariants rather than only individual bugs.

⸻

42. Compatibility Testing

Noema components and persisted representations may evolve independently.

Compatibility testing should cover:

* schema versions
* event versions
* Action Contract versions
* Intent versions
* graph versions
* persistence formats
* API versions
* model versions

A version change must not silently invalidate existing durable state.

⸻

43. Migration Testing

Schema and state migrations should be tested against:

* representative historical data
* incomplete records
* old versions
* malformed records
* large datasets
* interrupted migrations
* rollback or recovery procedures where supported

Migration correctness includes preservation of semantic meaning.

⸻

44. Load Testing

Load testing should establish system behavior under expected and elevated workloads.

Metrics may include:

* throughput
* latency
* queue depth
* resource consumption
* error rate
* retry rate
* saturation
* persistence latency
* recovery time

Load testing should not validate correctness by performance alone.

A fast incorrect system remains incorrect.

⸻

45. Stress Testing

Stress testing should intentionally exceed normal operating conditions.

Examples:

* high concurrency
* dependency saturation
* event bursts
* repeated retries
* large Action Graphs
* large Intent volumes
* slow external systems
* partial infrastructure failure

The objective is to identify degradation behavior and boundary failures.

⸻

46. Scalability Testing

Scalability tests should establish whether system behavior remains within defined engineering limits as:

* Intent volume increases
* graph complexity increases
* concurrent executions increase
* external dependencies increase
* event volume increases
* tenants increase

Tests should distinguish:

capacity limitation

from:

correctness failure

Both require explicit handling.

⸻

47. Chaos Testing

Where appropriate, controlled chaos testing may introduce:

* process failures
* dependency failures
* network partitions
* delayed responses
* resource exhaustion
* queue disruption
* storage failures

Chaos experiments must have defined hypotheses and expected safety properties.

Chaos is not valuable merely because it produces failures.

It is valuable when it verifies recovery invariants.

⸻

48. End-to-End Testing

End-to-end tests should exercise the canonical lifecycle.

Example:

Actor Expression
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
Action Contract
      ↓
Execution
      ↓
Outcome

End-to-end tests should cover both successful and unsuccessful lifecycle paths.

⸻

49. Negative Testing

Negative tests are first-class.

Examples:

* malformed Intent
* ambiguous Intent
* missing required information
* invalid graph
* missing capability
* missing contract
* unauthorized Action
* expired authorization
* invalid dependency
* stale graph
* failed external system
* duplicate request
* unknown execution result
* invalid state transition

The expected result should be explicit.

Noema should not merely test that valid requests work.

⸻

50. Boundary Testing

Architectural boundaries should receive dedicated tests.

Important boundaries include:

Interpretation → Intent
Intent → Validation
Validation → Trust
Trust → Action Graph
Action Graph → Contract
Contract → Execution
Execution → Outcome
Noema → External System

For every boundary, tests should establish:

* what may cross
* what may not cross
* what validation is required
* what provenance is preserved
* what failures occur when requirements are not satisfied

⸻

51. No Silent Bypass Testing

Tests should deliberately attempt to bypass each control.

Examples:

unresolved Intent → execution
candidate graph → execution
missing Trust → execution
missing Contract → execution
missing capability → execution
unauthorized capability → execution
stale graph → execution
unknown condition → satisfied

Each bypass attempt should be rejected or transitioned into the explicitly defined non-executable state.

⸻

52. Determinism Testing

Where the architecture requires deterministic behavior, tests should verify reproducibility.

Given:

same Intent
+
same Context
+
same Evidence
+
same Rules
+
same Versions

the canonical result should remain equivalent.

Deterministic components should not produce materially different results because of irrelevant execution variation.

⸻

53. Non-Deterministic Component Isolation

Some model behavior is inherently probabilistic.

Testing should therefore focus on isolating that variability behind deterministic boundaries.

Conceptually:

Probabilistic Model
       ↓
Candidate
       ↓
Deterministic Validation / Resolution
       ↓
Canonical State

Tests should establish that downstream state does not depend on uncontrolled model variability where deterministic semantics are required.

⸻

54. Test Data Provenance

Test data should preserve enough provenance to establish what a test is actually verifying.

Where relevant, test fixtures should identify:

* source
* version
* expected semantic state
* external-system assumptions
* policy version
* Action Contract version
* Intent version
* graph version

Fixtures must not encode undocumented assumptions as if they were canonical behavior.

⸻

55. Test Isolation

Tests should be isolated where isolation is necessary to establish deterministic behavior.

Shared mutable test state can create false positives and false negatives.

Tests involving durable execution or distributed behavior may intentionally share infrastructure, but the shared state and expected interactions must be explicit.

⸻

56. Test Repeatability

A test that passes once and fails intermittently without explanation is not sufficient evidence of correctness.

Tests should be:

* repeatable
* deterministic where possible
* independently diagnosable
* explicit about environmental dependencies

Flaky tests must be treated as engineering defects rather than normalized background noise.

⸻

57. Test Environment Parity

Testing environments should approximate production-relevant behavior where practical.

Important differences may include:

* persistence
* network behavior
* concurrency
* authentication
* external dependencies
* event delivery
* time
* failure modes

A component that works only in a simplified test environment does not establish production correctness.

⸻

58. Test Pyramid

Noema should maintain an appropriate distribution of tests.

Conceptually:

             E2E
            /   \
       System / Integration
          /         \
     Contract / Component
        /             \
              Unit

Lower-level tests provide fast feedback.

Higher-level tests verify cross-boundary behavior.

Neither should replace the other.

⸻

59. Test Coverage

Coverage should be evaluated across multiple dimensions.

Traditional code coverage may include:

* line coverage
* branch coverage
* function coverage

Noema additionally requires semantic and behavioral coverage such as:

* state transitions
* failure classes
* dependency types
* authorization paths
* Trust states
* graph states
* recovery paths
* unknown outcomes
* retry paths
* security boundaries

High code coverage does not imply architectural coverage.

⸻

60. State Transition Coverage

Every defined state transition should have tests for:

* valid transition
* invalid transition
* boundary conditions
* concurrent transition where relevant
* recovery from interruption
* persistence of the resulting state

For example:

WAITING_FOR_CLARIFICATION
        ↓
CLARIFICATION_RECEIVED

should be tested independently from:

WAITING_FOR_CLARIFICATION
        ↓
CANCELLED

if both transitions are permitted.

⸻

61. Failure Matrix

Engineering should maintain a failure matrix mapping failures to expected behavior.

Conceptually:

Failure	Expected behavior
Ambiguous Intent	Clarify / unresolved
Missing semantic field	Unresolved
Invalid graph	Block
Unauthorized Action	Reject / block
Contract unavailable	Block / re-evaluate
Retryable execution failure	Retry according to contract
Non-retryable failure	Fail
Unknown external outcome	Unknown / reconcile
Capability unavailable	Re-evaluate / replan
Process crash	Recover
Partial execution	Preserve partial state
Compensation failure	Explicit failure / escalation

The exact behavior must follow the applicable specification.

⸻

62. Test Oracles

Every test requires a defined oracle.

An oracle establishes what constitutes correct behavior.

Possible oracles include:

* canonical specification
* schema
* invariant
* state machine
* Action Contract
* external system contract
* policy
* deterministic rule
* expected event sequence

A model-generated output should not be its own authority for correctness.

⸻

63. Testing Model-Generated Artifacts

Where models generate:

* Intent candidates
* Action Graphs
* clarification requests
* execution strategies

tests should distinguish:

generation quality

from:

canonical correctness

The model may be evaluated for usefulness.

The deterministic system remains responsible for deciding whether generated artifacts are admissible.

⸻

64. Security Regression

Security failures require regression tests.

For example:

unauthorized Action
      ↓
execution attempt

must remain rejected after subsequent changes.

Security regression suites should cover previously discovered:

* privilege bypasses
* injection paths
* isolation failures
* replay vulnerabilities
* secret exposure
* authorization errors

⸻

65. Performance Regression

Performance-sensitive behavior should have regression thresholds where justified.

Examples:

* Intent resolution latency
* graph validation latency
* persistence latency
* execution scheduling latency
* event-processing latency
* recovery latency

Performance regression must not be fixed by weakening correctness or safety requirements.

⸻

66. Production Verification

Testing does not end at deployment.

Production verification may include:

* health checks
* invariant monitoring
* synthetic transactions
* canary execution
* event validation
* error-rate monitoring
* latency monitoring
* reconciliation checks

Production verification must remain within the applicable authorization and safety boundaries.

⸻

67. Reconciliation Testing

Where Noema interacts with authoritative external systems, reconciliation should be tested.

Example:

Noema:
Action UNKNOWN
External System:
Action COMPLETED

The reconciliation process must correctly transition Noema’s representation without fabricating historical execution facts.

⸻

68. Disaster Recovery Testing

Disaster recovery tests should verify:

* durable state restoration
* event recovery
* execution recovery
* idempotency preservation
* graph reconstruction
* Intent reconstruction
* audit reconstruction
* external reconciliation

A successful infrastructure restore is insufficient if semantic or execution state cannot be reconstructed.

⸻

69. Test of Historical Reconstruction

Noema should be able to reconstruct material historical state from durable records.

Tests should verify that it is possible to determine:

What Intent existed?
Which version?
Which graph?
Which Trust decision?
Which Action Contracts?
Which Actions executed?
What failed?
What remained unknown?
What was the final outcome?

Historical reconstruction is an engineering requirement, not merely an observability convenience.

⸻

70. Test Governance

Tests should be treated as governed engineering artifacts.

Important properties include:

* ownership
* version control
* reproducibility
* traceability
* maintenance
* failure investigation
* review

Foundational invariants should not depend solely on undocumented test behavior.

The specification remains authoritative.

Tests provide executable evidence of conformance.

⸻

71. Specification-to-Test Traceability

Foundational specifications should map to relevant tests.

Conceptually:

Specification
      ↓
Invariant
      ↓
Test Case
      ↓
Evidence

This makes it possible to determine whether an architectural change has corresponding engineering verification.

⸻

72. Test Naming

Tests should communicate the invariant or behavior being verified.

Prefer:

rejects_execution_when_trust_is_not_ready

over:

test_case_17

Names should make failures diagnostically useful.

⸻

73. Test Failure Semantics

A failing test should distinguish:

* implementation defect
* specification mismatch
* test defect
* environment failure
* external dependency failure
* nondeterministic infrastructure behavior

A test suite must not hide infrastructure failures by automatically treating them as product behavior.

⸻

74. Tests Must Not Encode Accidental Behavior

Tests should verify specified behavior rather than incidental implementation details.

For example, a test should not require a particular internal function call merely because the current implementation happens to use it unless that call is itself part of the contract.

This allows implementation evolution without weakening architectural guarantees.

⸻

75. Test-Driven Architectural Enforcement

Where a foundational invariant is sufficiently stable, it should have an executable test that would fail if the invariant were violated.

Examples:

unknown ≠ valid
candidate graph ≠ executable graph
capability ≠ authorization
trust ≠ execution success
partial execution ≠ automatic success
unknown outcome ≠ failure

These distinctions should be mechanically protected wherever feasible.

⸻

76. Testing and Change Management

Material architectural changes should trigger corresponding test review.

Changes affecting:

* Intent semantics
* Trust
* Action Graphs
* Action Contracts
* execution
* durability
* idempotency
* security
* state machines
* external interfaces

should include an explicit assessment of affected tests.

A change is incomplete when its behavioral verification has not been updated appropriately.

⸻

77. Testing and Versioning

Tests should be version-aware where semantics evolve.

For example:

Intent schema v1

and:

Intent schema v2

may legitimately have different validation requirements.

Tests should therefore identify the applicable version rather than assuming that historical behavior remains identical.

⸻

78. Testing and Backward Compatibility

Backward compatibility tests should establish that supported historical representations continue to behave according to their compatibility guarantees.

Compatibility must not silently preserve behavior that violates newly established security or authority boundaries.

Where incompatible change is intentional, the migration and transition behavior must itself be tested.

⸻

79. Testing and Replanning

If a material condition causes graph re-evaluation:

Graph v1
   ↓
material change
   ↓
revalidation
   ↓
Graph v2

tests should verify:

* Graph v1 is preserved
* the material change is recorded
* revalidation occurs
* required Trust evaluation occurs
* Graph v2 is explicitly established
* stale Graph v1 does not silently execute

⸻

80. Testing and Human Intervention

Human review and approval paths require tests.

Examples:

Action
  ↓
HUMAN_REVIEW_REQUIRED

Tests should verify that:

* the Action does not execute prematurely
* approval is represented explicitly
* rejection is represented explicitly
* approval does not bypass other required controls
* material changes after approval trigger appropriate re-evaluation

⸻

81. Testing and Clarification

Clarification paths should be tested as complete lifecycle transitions.

Example:

Intent
  ↓
Ambiguous
  ↓
Clarification Required
  ↓
Actor Response
  ↓
Intent v2
  ↓
Validation

Tests should establish that the clarification response updates the correct Intent lineage rather than creating an unrelated or silently mutated semantic object.

⸻

82. Testing and External State

Tests must recognize that external business state can change independently of Noema.

Example:

T1: Account ACTIVE
T2: Graph constructed
T3: Account SUSPENDED
T4: Execute

The test should verify that execution-time authority remains with the relevant external system and Action Contract.

A failed execution does not necessarily demonstrate that the earlier graph was malformed.

⸻

83. Testing and TOCTOU

Tests should explicitly exercise time-of-check/time-of-use conditions.

Example:

Check eligibility
      ↓
External state changes
      ↓
Execute

The expected behavior must follow the Action Contract and execution-time authority.

Tests should prevent stale validation results from being treated as permanent execution authority.

⸻

84. Testing and Atomicity

Tests should verify the declared atomicity semantics of composite execution.

Where Actions are independently executable:

A succeeds
B fails

must preserve the defined partial state.

Where execution is explicitly atomic or requires coordinated handling, tests must verify the corresponding behavior.

Atomicity must never be inferred merely from grouping.

⸻

85. Testing and Outcome Semantics

Tests should distinguish:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN

where those outcomes are defined.

An execution test should not collapse all non-success responses into:

FAILED

when the architecture defines a more precise outcome.

⸻

86. Test Completeness

Testing is sufficiently comprehensive when it provides evidence across:

* normal execution
* invalid execution
* ambiguous semantics
* authorization boundaries
* dependency relationships
* state transitions
* failure modes
* retries
* idempotency
* unknown outcomes
* recovery
* security
* concurrency
* persistence
* external integration
* observability
* historical reconstruction

No finite test suite proves that software has no defects.

The purpose is to establish meaningful evidence against the defined failure and correctness model.

⸻

87. Canonical Testing Flow

The canonical testing lifecycle is:

Specification
      ↓
Invariant / Contract
      ↓
Test Design
      ↓
Fixture / Environment
      ↓
Execution
      ↓
Observed Behavior
      ↓
Oracle Comparison
      ↓
Evidence
      ↓
Regression Protection

When a test fails:

Failure
   ↓
Classification
   ↓
Investigation
   ↓
Correction
   ↓
Regression Test

where appropriate.

⸻

88. Testing Invariants

Invariant 1

Tests must verify defined specifications and invariants rather than merely implementation details.

Invariant 2

A passing test does not create authorization.

Invariant 3

Model output must not be treated as authoritative merely because a test accepts it.

Invariant 4

Unknown states must remain distinct from failure, success, and validity where the specification requires that distinction.

Invariant 5

Tests must cover architectural boundaries, not only individual components.

Invariant 6

Retries must be tested together with idempotency semantics.

Invariant 7

Failure recovery must be tested under interruption and partial execution.

Invariant 8

Material state transitions must be testable and reconstructible.

Invariant 9

Security boundaries must have explicit negative tests.

Invariant 10

Candidate Intent and canonical Intent must remain distinguishable.

Invariant 11

Candidate Action Graph and executable Action Graph must remain distinguishable.

Invariant 12

Trust state must remain distinct from execution outcome.

Invariant 13

External business state must remain authoritative where defined by the architecture.

Invariant 14

Test coverage must include failure and recovery paths, not only successful paths.

Invariant 15

Foundational architectural invariants should be mechanically enforced by tests wherever feasible.

Invariant 16

Tests must not silently encode unspecified behavior as canonical behavior.

Invariant 17

Material architectural changes require corresponding test review.

Invariant 18

A test suite must not conceal correctness failures by conflating infrastructure failure with product behavior.

⸻

89. Canonical Mental Model

Testing in Noema can be reduced to five questions:

1. What behavior is specified?
2. What invariant or contract must hold?
3. What conditions could violate it?
4. Can the violation be reproduced and detected?
5. Does the system recover while preserving the invariant?

This produces:

Specification
      ↓
Invariant
      ↓
Test
      ↓
Failure / Success Evidence
      ↓
Regression Protection

⸻

90. Final Definition

Testing is Noema’s engineering discipline for providing executable evidence that the implementation conforms to its canonical specifications, contracts, state machines, security boundaries, durability requirements, and architectural invariants across normal, adversarial, failure, recovery, and evolving conditions.

Its central invariant is:

Noema does not consider a behavior correct merely because it works on the successful path. Correctness requires that the system preserve its semantic, authority, execution, durability, security, and recovery invariants across the conditions under which the system is expected to operate.

The engineering boundary remains:

Specification
      ↓
Invariant
      ↓
Implementation
      ↓
Testing
      ↓
Evidence
      ↓
Operational Verification

Testing therefore does not define what Noema is permitted to do.

It establishes whether the implementation actually behaves according to what Noema has defined.