Constitution

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/constitution.md

⸻

1. Definition

The Noema Constitution is the foundational engineering specification that defines the non-negotiable architectural, semantic, execution, security, provenance, and governance principles by which Noema must be implemented.

The Constitution establishes constraints on the implementation of Noema’s architecture.

It does not define every implementation detail.

It defines the invariants that implementation details must preserve.

Therefore:

Architecture defines the system structure.
Components define the system parts.
The Constitution defines the engineering constraints those parts must obey.

The Constitution exists to prevent implementation choices from silently weakening Noema’s semantic and execution boundaries.

⸻

2. Purpose

Noema is intended to provide a controlled transition from human intent to consequential execution.

That transition must remain:

* explicit
* inspectable
* deterministic where determinism is required
* provenance-preserving
* authority-bounded
* contract-governed
* auditable
* resilient to failure
* resistant to ambiguity and unintended execution

The Constitution therefore establishes the engineering rules that preserve the distinction between:

Human Expression
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
Outcome

No implementation component may collapse these boundaries merely for convenience.

⸻

3. Constitutional Principle

The fundamental engineering principle of Noema is:

Probabilistic systems may propose. Deterministic system boundaries establish, authorize, and execute.

An AI model may:

* interpret
* infer
* classify
* extract
* propose
* plan
* generate candidates
* suggest alternatives

But model output does not become authoritative merely because it is plausible, coherent, or highly confident.

Authority must arise from the applicable Noema representation, validation, Trust decision, contract, policy, and execution boundary.

⸻

4. Authority Is Explicit

Noema must maintain explicit authority boundaries.

The following are distinct:

Interpretation
Intent
Validation
Trust
Capability
Authorization
Action Graph
Action Contract
Execution
Outcome

No component may acquire authority merely because it happens to participate in a previous stage.

In particular:

Intent ≠ Authorization
Capability ≠ Authorization
Action Graph ≠ Authorization
Model Confidence ≠ Truth
Model Output ≠ Authority
Validation ≠ Trust
Trust ≠ Execution
Execution ≠ Outcome Success

⸻

5. Human Intent Is the Semantic Origin

Noema exists to represent and safely fulfill an Actor’s objective.

The Actor remains the source of Intent.

Noema may interpret an Actor’s expression.

It must not silently replace the Actor’s objective with a system-generated objective.

Therefore:

Actor Expression
      ↓
Interpretation
      ↓
Intent Resolution

must preserve the semantic relationship to the Actor.

Any material semantic transformation must be explicit and reconstructible.

⸻

6. Intent Must Be Canonical

The canonical Intent representation is the authoritative semantic representation used by downstream Noema components.

Application-specific or model-specific representations may exist internally.

They must not silently replace the canonical Intent model.

The system must distinguish:

Candidate Intent
      ≠
Canonical Intent

A candidate interpretation remains a proposal until the Intent Engine establishes it as canonical.

⸻

7. Ambiguity Must Remain Ambiguity

Noema must never convert material semantic ambiguity into certainty merely because one interpretation appears more probable.

For example:

recipient = John

when multiple Johns satisfy the reference must remain unresolved unless the applicable evidence establishes which John is intended.

The valid transition is:

AMBIGUOUS
    ↓
CLARIFICATION / AUTHORITATIVE RESOLUTION
    ↓
RESOLVED

not:

AMBIGUOUS
    ↓
BEST GUESS
    ↓
EXECUTION

⸻

8. Unknown Must Not Become True

Unknown information must remain explicitly unknown.

Noema must distinguish:

KNOWN
UNKNOWN
MISSING
AMBIGUOUS
INVALID

These states must not be collapsed merely to permit execution to continue.

In particular:

UNKNOWN ≠ TRUE
UNKNOWN ≠ FALSE
UNKNOWN ≠ AUTHORIZED

Unknown mandatory conditions must not satisfy execution requirements.

⸻

9. Provenance Is a First-Class Engineering Requirement

Material semantic and execution-relevant information must retain provenance.

Noema should be able to establish:

* where a value originated
* which version established it
* which rule produced it
* which evidence supported it
* which Actor interaction established it
* which model proposed it
* which external system supplied it
* when it was established

Potential provenance sources include:

ACTOR
MODEL
CONTEXT
EXTERNAL_EVIDENCE
DETERMINISTIC_RULE
DEFAULT
CLARIFICATION
SYSTEM

Provenance explains origin.

It does not itself establish authority.

⸻

10. No Hidden Semantic Mutation

A component must not silently change a material semantic value merely to satisfy downstream requirements.

For example, an implementation must not transform:

Cancel my subscription

into:

Cancel subscription_123

unless the applicable resolution semantics establish that subscription_123 is the intended target.

Convenience is not a semantic authority.

⸻

11. No Hidden Execution

Consequential execution must be represented through explicit Noema execution structures.

A system must not silently perform additional consequential operations that are absent from the relevant Action Graph, Action Contract, or explicitly defined contract behavior.

If execution requires:

LOOKUP_ACCOUNT
CHECK_BALANCE
TRANSFER_FUNDS
SEND_NOTIFICATION

those operations must have an explicit architectural or contractual representation.

Noema must avoid hidden execution semantics.

⸻

12. Models Are Not Execution Authorities

An LLM or other probabilistic model must never become the final authority merely by producing an apparently valid plan or tool call.

The canonical boundary is:

Model
  ↓
Candidate
  ↓
Deterministic Validation
  ↓
Trust / Policy
  ↓
Action Contract
  ↓
Execution Consumer

A model may propose an Action Graph.

A model may not authorize its own graph.

A model may propose a tool invocation.

A model may not thereby acquire permission to execute it.

⸻

13. No Direct Consequential Tool Calls

A model must not bypass Noema’s control boundary by directly invoking consequential tools.

The canonical path is:

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
Consumer
  ↓
Execution

Tool invocation is an implementation mechanism.

It is not the authority model.

⸻

14. Validation Must Be Separate

Validation establishes whether a representation satisfies defined structural and semantic requirements.

Validation does not authorize execution.

Therefore:

VALID

must not be interpreted as:

AUTHORIZED

and:

VALID

must not be interpreted as:

SUCCESSFUL

Validation remains a distinct architectural stage.

⸻

15. Trust Must Be Separate

Trust establishes whether an Intent or Action is permitted to proceed under the applicable governance, authorization, policy, risk, and execution conditions.

Trust must not be conflated with:

* semantic resolution
* graph construction
* capability availability
* execution success

The system must preserve these distinctions.

⸻

16. Trust Does Not Guarantee Execution

A Trust decision establishes eligibility under the conditions evaluated.

It does not guarantee that external execution will succeed.

For example:

Trust = READY
Execution = FAILED

is a valid system state.

Execution failure does not automatically imply that the original Trust decision was invalid.

⸻

17. Trust Decisions Must Be Bound to Versions

Trust decisions must be associated with the semantic state to which they apply.

A material Intent change must not silently inherit a Trust decision made for an earlier Intent version.

Conceptually:

Intent v1
   ↓
Trust Evaluation 1
Intent v2
   ↓
new Validation
   ↓
new Trust Evaluation

The previous decision remains historical evidence for the previous state.

⸻

18. Action Graphs Must Be Explicit

The Action Graph is an explicit representation of:

* Actions
* dependencies
* conditions
* capabilities
* inputs
* outputs
* execution relationships
* failure semantics

An opaque model-generated sequence must not become the canonical execution structure merely because it appears coherent.

The graph must be inspectable.

⸻

19. Graph Structure Is Not Authorization

The presence of an Action in a graph does not authorize that Action.

For example:

TRANSFER_FUNDS

appearing in an Action Graph does not establish:

Actor authorized to transfer funds

Authorization remains within the applicable Trust and execution-control boundaries.

⸻

20. Dependencies Must Be Explicit

Dependencies must not be inferred merely from:

* visual ordering
* generated prose
* model assumptions
* implementation convenience

If Action B depends on Action A, the dependency must be represented explicitly.

Different dependency semantics must remain distinguishable where relevant, including:

DATA_DEPENDENCY
ORDER_DEPENDENCY
CONDITION_DEPENDENCY
AUTHORIZATION_DEPENDENCY
APPROVAL_DEPENDENCY
RESOURCE_DEPENDENCY

⸻

21. Conditional Execution Must Be Explicit

A conditional branch must contain an explicit condition.

For example:

CHECK_ELIGIBILITY
      ↓
eligible = true
      ↓
RENEW_CARD

The executor must not silently substitute its own condition.

Unknown conditions must not be treated as satisfied.

⸻

22. Parallelism Must Be Proven Safe

Actions may execute concurrently only when their dependencies and applicable contracts permit concurrent execution.

Structural independence does not automatically establish operational safety.

The execution layer must respect:

* resource constraints
* ordering requirements
* Action Contracts
* atomicity
* external system semantics
* concurrency controls

⸻

23. Ordering Must Be Preserved

Where an ordering dependency exists, execution must respect it.

An optimizer or planner must not reorder Actions merely because the reordered sequence appears operationally equivalent.

Ordering may be a semantic or safety requirement.

⸻

24. Candidate Graph ≠ Executable Graph

Noema must distinguish:

Candidate Action Graph

from:

Executable Action Graph

A candidate graph may contain:

* unresolved dependencies
* unresolved capabilities
* unvalidated conditions
* unresolved contracts
* policy conflicts

It must not cross the execution boundary until applicable requirements have been satisfied.

⸻

25. Action Contracts Are Mandatory Boundaries

Every executable Action must resolve to an applicable Action Contract.

The Action Contract defines the executable interface and obligations associated with the Action.

Conceptually:

Action Graph Node
      ↓
Action Contract
      ↓
Consumer
      ↓
Execution

An Action identity alone is insufficient to establish executable behavior.

⸻

26. Capability Is Not Authorization

Capability answers:

What operation is available?

Authorization answers:

May this Actor perform this operation under these conditions?

Therefore:

Capability ≠ Authorization

Discovering a capability must never grant permission to use it.

⸻

27. External Systems Remain Authoritative

Noema must not silently claim ownership of authoritative external business state.

For example:

Account.status
Payment.status
Card.status
Delivery.status

may remain authoritative in external systems.

Noema may:

* query the state
* reference the state
* record evidence about the state
* use the state in decision-making

but must not represent its own cached belief as authoritative merely because it exists internally.

⸻

28. External State Is Mutable

Business state may change between:

validation
trust
graph construction
contract binding
execution

Therefore, a previously valid graph may become invalid before execution.

The system must support execution-time validation where required.

⸻

29. TOCTOU Must Be Treated Explicitly

Time-of-check/time-of-use conditions are inherent to distributed execution.

The following implication is invalid:

Condition true at T1
        ↓
Condition guaranteed true at T2

Consequential Action Contracts may therefore require final authoritative checks at execution time.

Noema must not assume stale validation remains sufficient indefinitely.

⸻

30. No Stale Execution

A materially stale graph, contract, authorization state, or execution condition must not silently cross the execution boundary.

Material changes may require:

REVALIDATE
RETRUST
REPLAN
RECONTRACT
BLOCK
ESCALATE

as defined by the applicable semantics.

⸻

31. Graph Mutation During Execution Is Prohibited

Once execution begins, the executed graph must not be silently mutated.

If material conditions change:

Graph v1
   ↓
Material Change
   ↓
Re-evaluation
   ↓
Graph v2

The transition must be explicit and auditable.

⸻

32. Versioning Is Mandatory for Material State

Material changes to semantic or execution-relevant representations must be reconstructible.

Relevant versioned objects may include:

* Intent
* Action Graph
* Trust evaluation
* Action Contract
* policy
* resolution rules
* capability definitions

Versioning allows Noema to answer:

What exactly was evaluated and executed?

⸻

33. Determinism Where Required

Where a Noema rule is defined as deterministic, the result must be reproducible from the relevant inputs and versions.

Conceptually:

Input
+
Context
+
Evidence
+
Rules
+
Versions
=
Deterministic Result

Model variability must not silently alter a deterministic downstream result.

⸻

34. Model Variability Must Be Contained

Probabilistic variability is acceptable in proposal-generation stages.

It must be bounded before it becomes authoritative state.

For example:

LLM
 ↓
Candidate Intent
 ↓
Deterministic Resolution

is acceptable.

Whereas:

LLM
 ↓
Canonical Intent
 ↓
Execution

without the required semantic controls is not.

⸻

35. Confidence Is Not Truth

Model confidence may be retained as metadata.

It must not be treated as semantic establishment, authorization, or execution permission.

Therefore:

confidence = 0.99

does not imply:

resolved = true

nor:

authorized = true

⸻

36. Defaults Must Be Explicit

Defaults may be used only where defined semantics permit them.

A default must have:

* explicit rule
* defined scope
* deterministic basis
* provenance
* applicable authority

Defaults must not be used to conceal ambiguity.

⸻

37. Clarification Is a Valid System State

When required semantic information is missing or ambiguous, the system may enter:

WAITING_FOR_CLARIFICATION

Clarification must not be represented as:

FAILED

unless the applicable semantics define it as such.

The system should ask for the smallest missing information necessary to establish the Intent.

⸻

38. Human Approval Is Explicit

Where an Action requires human or organizational approval, approval must be represented as an explicit governance condition.

For example:

CREATE_TRANSFER
      ↓
WAIT_FOR_APPROVAL
      ↓
EXECUTE_TRANSFER

Approval is evidence of a required governance condition.

Approval does not automatically eliminate other Trust or execution requirements.

⸻

39. Actor Confirmation Is Explicit

Where explicit Actor confirmation is required, conversational continuation must not automatically be interpreted as confirmation unless the governing semantics explicitly define it.

For consequential operations:

ACTION
  ↓
WAIT_FOR_CONFIRMATION
  ↓
EXECUTE

should remain explicit where required.

⸻

40. Atomicity Must Be Explicit

Noema must not infer atomicity merely because multiple Actions belong to the same Intent.

A group of Actions must have explicit semantics defining whether it is:

ATOMIC
INDEPENDENT
PARTIALLY_EXECUTABLE
COMPENSATABLE

The system must respect the Actor’s Intent semantics regarding partial execution.

⸻

41. Partial Execution Must Be Explicit

If an Intent does not permit partial execution, individually executable Actions must not be executed simply because their local conditions are satisfied.

For example:

A = READY
B = BLOCKED
C = READY

does not automatically authorize:

Execute A
Execute C

if the Intent requires the whole operation to succeed as a unit.

⸻

42. Execution State Must Be Distinct

Execution state must remain separate from semantic and Trust state.

Example:

Intent:
RESOLVED
Trust:
READY
Execution:
NOT_STARTED

Later:

Intent:
RESOLVED
Trust:
READY
Execution:
EXECUTING

Finally:

Intent:
RESOLVED
Trust:
READY
Execution:
FAILED

These states describe different dimensions.

⸻

43. Unknown Execution Results Must Remain Unknown

A timeout or network failure does not necessarily mean an external Action failed.

For example:

REQUEST_PAYMENT
      ↓
NETWORK_TIMEOUT
      ↓
UNKNOWN

must not automatically become:

FAILED

when the external system may have processed the request.

Unknown outcomes require explicit handling.

⸻

44. Retries Must Be Bounded

Retries must be governed by explicit semantics.

A retry policy should define, where applicable:

* maximum attempts
* retryable failures
* timeout
* backoff
* idempotency requirements
* termination conditions

A model must not invent retry behavior during execution.

⸻

45. Idempotency Must Be Preserved

Retryable consequential Actions must respect their idempotency semantics.

For example:

CREATE_PAYMENT

must not create multiple payments merely because the first response was uncertain.

Idempotency belongs primarily to Action Contracts and execution architecture, but all planning and execution layers must respect it.

⸻

46. Compensation Is Not Rollback

Compensating Actions must be explicitly defined.

For example:

A → B → C
C fails
↓
Compensate B
↓
Compensate A

does not imply that the external system has been transactionally rolled back.

Noema must distinguish:

ROLLBACK

from:

COMPENSATION

External systems may not support true rollback.

⸻

47. Failure Semantics Must Be Explicit

Action failure must have defined semantics.

Possible policies include:

STOP
RETRY
COMPENSATE
SKIP
ESCALATE
CONTINUE

The system must not invent recovery behavior dynamically without an applicable rule or contract.

⸻

48. Execution Outcome Must Be Honest

Noema must not represent partial or uncertain execution as success.

Possible execution outcomes include:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN

The final Outcome must accurately reflect what is known to have happened.

⸻

49. Postconditions Must Be Verified Where Required

An Action returning successfully does not necessarily establish that the desired external state exists.

Where required, Noema should verify applicable postconditions through authoritative evidence.

For example:

REQUEST_REPLACEMENT
      ↓
response = accepted
      ↓
VERIFY_REQUEST_STATUS

The appropriate verification semantics belong to the Action Contract and execution architecture.

⸻

50. Completion Must Be Explicit

A graph must not be considered complete merely because one final Action returned successfully.

Completion may require:

* mandatory nodes completed
* required postconditions verified
* required external outcomes observed
* no unresolved mandatory branches
* no outstanding compensation
* required human intervention completed

Completion semantics must be explicit.

⸻

51. Re-Evaluation Is a First-Class Operation

Material changes may require re-evaluation.

Examples include:

* Intent changes
* authorization changes
* policy changes
* capability disappearance
* Action Contract changes
* resource changes
* dependency invalidation
* material external-state changes

The system must not silently continue from stale assumptions.

⸻

52. No Silent Replanning

Replanning may be necessary.

But a material change in execution structure must be represented explicitly.

For example:

Graph v1
   ↓
Capability unavailable
   ↓
Re-evaluation
   ↓
Graph v2

The system must retain the relationship between graph versions.

⸻

53. Optimization Is Subordinate to Semantics

Execution optimization may seek to improve:

* latency
* cost
* number of calls
* resource usage
* parallelism
* reliability

But optimization must never alter:

* Actor Intent
* Trust requirements
* authorization
* Action Contract obligations
* policy
* atomicity
* safety requirements

Therefore:

Optimization may change execution structure, but never semantic authority.

⸻

54. No Semantic Mutation Through Optimization

An optimizer must not remove, add, or alter a semantically required Action merely because doing so appears cheaper or faster.

For example:

Intent:
Send email + create audit record

must not become:

Send email

merely because the audit operation increases execution cost.

⸻

55. Security Boundaries Must Be Independent

No component must be able to escalate authority merely by modifying another representation.

For example:

Model → Action Graph

must not allow:

Action Graph → additional capability

without independent capability and authorization checks.

Security-sensitive decisions must remain independently enforceable.

⸻

56. Least Authority

Components should operate with only the capabilities necessary for their defined responsibilities.

In particular:

* Intent resolution should not require execution authority.
* Graph construction should not itself grant execution authority.
* Model inference should not require unrestricted external system access.
* Execution consumers should receive only the contracted operation and required inputs.

Noema should minimize authority propagation across architectural boundaries.

⸻

57. Consumer Is Authoritative at Execution Boundary

The execution consumer may reject an Action even when:

Graph = valid
Trust = ready
Contract = valid

if an execution-time business condition is no longer satisfied.

The consumer remains authoritative for execution-time conditions within its business domain.

⸻

58. Noema Does Not Own External Business Truth

Noema coordinates execution.

It does not become the authoritative owner of:

* banking balances
* card status
* customer records
* payment status
* shipment status
* enterprise records

unless a future specification explicitly establishes such authority.

External systems remain authoritative for their respective domains.

⸻

59. Auditability Without Private Reasoning

Noema must preserve sufficient provenance to reconstruct material system decisions.

This includes:

* input representations
* Intent versions
* resolution results
* evidence references
* rule versions
* Trust evaluations
* graph versions
* Action Contracts
* execution events
* outcome states
* material changes

This does not require storing private model chain-of-thought.

The objective is decision provenance, not hidden reasoning disclosure.

⸻

60. Event History Must Be Reconstructible

Material lifecycle transitions should be represented as explicit events or equivalent durable state transitions.

Examples include:

intent.created
intent.resolved
intent.updated
intent.superseded
intent.cancelled
graph.created
graph.validated
graph.invalidated
graph.revised
trust.evaluated
trust.changed
action.started
action.completed
action.failed
action.unknown
execution.completed
execution.failed
execution.partially_completed

The final state should be reconstructible from authoritative history.

⸻

61. State Transitions Must Have Causes

A state transition must occur because of a defined event, dependency transition, contract result, material condition change, or deterministic re-evaluation.

A state must not change merely because:

* a model became more confident
* a prompt was reformulated
* a model generated a different plan
* a retry occurred without a retry policy

⸻

62. Durable Execution

Consequential execution must survive process failure, worker failure, network failure, and restart without losing authoritative execution state.

The execution architecture must distinguish:

No record of execution

from:

Execution occurred but result is unknown

Durability must therefore preserve:

* execution identity
* Action identity
* attempt identity
* inputs
* contract version
* timestamps
* state transitions
* external correlation identifiers
* observed responses
* unknown states

⸻

63. Exactly-Once Must Not Be Assumed

Noema must not assume that distributed execution can universally guarantee exactly-once external effects.

Where external operations are retryable or uncertain, the architecture should rely on explicit mechanisms such as:

* idempotency keys
* deduplication
* external operation identifiers
* durable attempt records
* reconciliation
* execution-time verification

The exact guarantees belong to the relevant execution and Action Contract specifications.

⸻

64. Durable State Must Be Authoritative

Transient process memory must not be the sole source of truth for consequential execution state.

If a worker crashes after initiating an external operation, the durable execution record must allow the system to determine what is known and what remains unknown.

⸻

65. Recovery Must Preserve Semantics

Recovery must not silently reinterpret an Intent, Trust decision, or Action Graph.

On restart, the system should resume from durable authoritative state.

It must not reconstruct execution from an approximate model-generated narrative.

⸻

66. Idempotent Recovery

Recovery procedures must respect Action idempotency.

If execution state is uncertain, the recovery mechanism must not blindly repeat a consequential Action.

It must first apply the applicable Action Contract and uncertainty-resolution semantics.

⸻

67. Concurrency Must Be Controlled

Concurrent execution must respect:

* graph dependencies
* Action Contracts
* resource constraints
* external-system semantics
* idempotency
* atomicity
* authorization
* consistency requirements

Noema must not infer that concurrency is safe merely because Actions have no obvious data dependency.

⸻

68. Resource Ownership Must Be Explicit

When multiple Actions compete for a resource, the applicable ownership or coordination semantics must be explicit.

The system must not rely on accidental ordering produced by:

* worker scheduling
* network timing
* model output
* queue ordering unless queue ordering is contractually authoritative

⸻

69. Configuration Is Not Authority

Configuration values must not silently become authorization or semantic truth.

A configuration such as:

default_recipient = X

does not establish that X is the Actor’s intended recipient unless the relevant Intent semantics explicitly authorize that default.

Configuration must remain subject to the applicable architectural boundary.

⸻

70. Policy Must Be Explicit

Policies that materially affect Intent resolution, Trust, Action Graph construction, or execution must be represented in a versioned and inspectable form.

Policy effects must be attributable.

For example:

Transfer > threshold
      ↓
Approval required

The policy establishes the requirement.

The Action Graph represents the resulting dependency.

⸻

71. Policy Changes Are Material

A policy change that affects an already prepared or executable graph may require re-evaluation.

Noema must not assume that an old graph remains executable under materially changed policy.

⸻

72. Schema Evolution Must Preserve Meaning

Changes to canonical schemas must preserve semantic compatibility or provide an explicit migration path.

A schema migration must not silently reinterpret existing Intent, graph, Trust, or Outcome records.

Material schema changes must be versioned.

⸻

73. Backward Compatibility Must Be Explicit

When a newer component consumes an older representation, compatibility must be established explicitly.

The system must not infer semantic equivalence merely because fields can be mechanically mapped.

⸻

74. No Implicit Semantic Coercion

Type conversion must not silently alter meaning.

For example:

UNKNOWN → FALSE

or:

AMBIGUOUS → first candidate

is prohibited where the distinction is semantically material.

⸻

75. Structured Errors

Errors at architectural boundaries must be machine-readable.

Human-readable messages may accompany them.

Examples include:

AMBIGUOUS_REFERENCE
MISSING_REQUIRED_INPUT
INVALID_INTENT
INVALID_GRAPH
UNRESOLVED_DEPENDENCY
CAPABILITY_UNAVAILABLE
CONTRACT_INVALID
AUTHORIZATION_REQUIRED
APPROVAL_REQUIRED
CONFIRMATION_REQUIRED
PRECONDITION_FAILED
EXECUTION_UNKNOWN
POSTCONDITION_FAILED
STALE_GRAPH
POLICY_CHANGED

The exact taxonomy remains subject to the canonical specifications.

⸻

76. Errors Must Not Be Collapsed

Different failure causes must remain distinguishable where they imply different recovery behavior.

For example:

BLOCKED

is not necessarily:

FAILED

and:

UNKNOWN

is not necessarily:

FAILED

and:

WAITING_FOR_APPROVAL

is not:

FAILED

⸻

77. Cancellation Is Explicit

Cancellation must be represented as an explicit lifecycle event.

It must not be conflated with:

* failure
* blocking
* expiration
* rejection

Cancellation semantics must define what happens to already-started Actions.

⸻

78. Expiration Is Explicit

Temporal validity must be represented explicitly where required.

An Intent, Trust decision, graph, approval, or contract may have validity constraints.

Expiration must not silently be interpreted as success or failure.

⸻

79. Time Is Part of Execution Semantics

Where execution depends on time, Noema must preserve the relevant temporal information.

Examples include:

* validity windows
* deadlines
* scheduled Actions
* timeouts
* retry delays
* approval expiry
* external state freshness

Temporal semantics must be explicit rather than inferred from processing time alone.

⸻

80. External Evidence Must Be Traceable

When external evidence contributes to Intent resolution, validation, Trust, or execution, Noema must retain an appropriate evidence reference.

Noema should be able to distinguish:

fact obtained from authoritative source

from:

fact inferred by model

and:

fact supplied by Actor

⸻

81. Evidence Freshness Matters

Evidence may become stale.

Where freshness is material to a decision, the system must establish whether the evidence remains valid at the point where it is used.

Old evidence must not silently substitute for current authoritative state when the Action Contract requires current verification.

⸻

82. No Cross-Domain Authority Leakage

A component authoritative for one concern must not automatically become authoritative for another.

For example:

Context

may provide information for Intent resolution.

It does not thereby authorize execution.

Similarly:

Capability Registry

may establish capability availability.

It does not establish Actor authorization.

⸻

83. Component Responsibilities Must Remain Narrow

Each Noema component should have a clearly defined responsibility.

A component must not absorb another component’s authority merely because doing so simplifies implementation.

For example:

Intent Engine

must not become:

Intent + Trust + Execution

and:

Action Graph

must not become:

Graph + Authorization

Boundaries are architectural controls.

⸻

84. Interface Contracts Must Be Explicit

Components must communicate through explicit interfaces.

Interfaces should define:

* inputs
* outputs
* schemas
* versions
* errors
* state transitions
* authority assumptions
* provenance requirements
* timing semantics
* retry semantics

An informal natural-language understanding between components is insufficient for consequential execution.

⸻

85. Component Substitution Must Preserve Semantics

An implementation component may be replaced if the replacement preserves the applicable interface and semantic guarantees.

For example:

Model A

may be replaced by:

Model B

provided downstream semantic and authority guarantees remain intact.

Noema architecture must not make a particular model the implicit source of system truth.

⸻

86. Model Independence

Noema’s canonical semantics must not depend on a particular LLM provider, model family, prompt format, or inference API.

Models are replaceable implementation components.

The canonical representations must remain model-independent.

⸻

87. Provider Failure Must Not Corrupt Authority

Failure of an AI provider must not cause the system to manufacture semantic certainty or execution authority.

If interpretation cannot be completed:

UNRESOLVED
WAITING
DEGRADED

may be appropriate according to the applicable semantics.

The system must not fabricate missing information merely to maintain throughput.

⸻

88. Fail Closed for Authority

Where a mandatory authority condition cannot be established, Noema must not assume permission.

In general:

Unknown authorization
      ≠
Authorized

and:

Unknown mandatory condition
      ≠
Satisfied

The exact failure behavior depends on the applicable policy and contract.

⸻

89. Fail Safely for Uncertain Execution

Execution uncertainty must be represented rather than hidden.

For example:

External request
      ↓
timeout
      ↓
UNKNOWN

should trigger the appropriate reconciliation or verification process rather than an arbitrary assumption.

⸻

90. No Silent Data Loss

Material information required to reconstruct semantic or execution history must not be discarded merely because it is inconvenient to retain.

Retention requirements should be defined by the relevant governance and storage specifications.

⸻

91. Observability Is Not Authority

Logs, metrics, traces, dashboards, and monitoring systems may describe Noema state.

They must not become authoritative state merely because they are observable.

Operational telemetry and canonical state must remain distinguishable.

⸻

92. Logging Must Preserve Security Boundaries

Observability must not require exposing unnecessary sensitive information.

The system should record sufficient information for:

* debugging
* auditability
* provenance
* execution reconstruction

while respecting applicable data-protection and access-control requirements.

⸻

93. Secrets Must Not Become Semantic Data

Credentials, tokens, keys, and other secrets must not be incorporated into canonical Intent, Action Graph, or provenance representations unless explicitly required by a secure contract.

Where possible, representations should reference secure credentials indirectly rather than embedding secrets.

⸻

94. Authorization Must Be Revalidated Where Required

A prior authorization decision may become stale.

Where an Action Contract requires current authorization, execution must perform the appropriate revalidation.

A historical Trust decision must not automatically authorize a materially changed execution.

⸻

95. Approval Must Be Bound to the Approved Operation

An approval should be associated with the relevant:

* Intent
* version
* Action
* parameters
* scope
* time
* Actor or approver identity

An approval for one material operation must not silently authorize another.

⸻

96. Confirmation Must Be Bound to Meaning

Actor confirmation must apply to a defined semantic operation.

A generic conversational response must not be interpreted as confirmation of an unrelated or materially changed operation.

⸻

97. Reconfirmation May Be Required

If material execution parameters change after confirmation, the applicable semantics may require renewed confirmation.

For example:

Transfer ₦50,000

confirmed by the Actor does not automatically establish confirmation for:

Transfer ₦500,000

Material changes must remain explicit.

⸻

98. Execution Must Be Correlatable

Every consequential execution should have durable correlation identity sufficient to connect:

Actor
Intent
Intent Version
Trust Evaluation
Action Graph
Graph Version
Action
Action Contract
Execution Attempt
External Operation
Outcome

This enables reconstruction across distributed systems.

⸻

99. External Correlation Identifiers Must Be Preserved

Where an external system provides an operation identifier, Noema should retain it as execution evidence.

This is especially important for:

* uncertain outcomes
* retries
* reconciliation
* duplicate prevention
* postcondition verification

⸻

100. Reconciliation Is a First-Class Concern

Where execution may produce an uncertain external state, Noema must support reconciliation.

Conceptually:

Execution UNKNOWN
      ↓
Reconciliation
      ↓
External authoritative state
      ↓
Resolved Outcome

Reconciliation must not simply overwrite the unknown state with an assumption.

⸻

101. Execution History Must Be Append-Oriented

Material execution history should preserve what occurred rather than merely storing the latest mutable state.

A current state may be derived from authoritative events or equivalent durable records.

Historical execution evidence must remain reconstructible.

⸻

102. Deterministic State Machines

Where Noema defines a state machine, transitions must be explicitly specified.

Invalid transitions must be rejected.

For example:

CANCELLED
    ↓
EXECUTING

must not occur unless the applicable lifecycle explicitly defines such a transition.

⸻

103. State Machines Must Not Be Implicit

State semantics must not exist solely in application code without an authoritative specification.

The canonical state model should define:

* states
* transition events
* valid transitions
* terminal states
* invalid transitions
* recovery semantics

⸻

104. Durable Execution and State Machines Must Align

Execution recovery must preserve the Action and graph state machine.

A worker restart must not produce a new semantic interpretation merely because execution resumed in a different process.

⸻

105. Exactly-Once Semantics Must Be Scoped

Where a component claims exactly-once behavior, the scope must be explicit.

For example:

exactly-once event processing

does not necessarily mean:

exactly-once external financial effect

External effects require their own idempotency and reconciliation semantics.

⸻

106. At-Least-Once Must Be Safe

Where infrastructure provides at-least-once delivery, Noema must ensure that duplicate delivery does not produce unauthorized duplicate effects.

This may require:

* idempotency
* deduplication
* durable operation identity
* consumer-side safeguards

⸻

107. Queue Semantics Must Not Become Hidden Authority

A message queue may order or deliver events.

It does not thereby establish:

* semantic truth
* authorization
* business state
* Actor intent

Queue behavior remains an implementation mechanism subject to Noema’s canonical state model.

⸻

108. Distributed Systems Must Assume Failure

Noema must assume that:

* processes crash
* networks partition
* requests time out
* messages duplicate
* messages arrive late
* external systems reject requests
* external state changes
* workers restart
* capabilities disappear

Architecture must not depend on an idealized failure-free execution environment.

⸻

109. No Silent Retry of Consequential Operations

A consequential operation must not be retried solely because a response was missing or delayed unless the applicable semantics establish that retry is safe.

Unknown outcome requires uncertainty handling, not automatic repetition.

⸻

110. Execution Consumers Must Enforce Contracts

The consumer executing an Action must validate the applicable execution contract.

The consumer must not assume that upstream graph construction guarantees current execution validity.

⸻

111. Consumer Rejection Is a Valid Outcome

A consumer may reject an Action because:

* preconditions changed
* authorization expired
* resource unavailable
* policy changed
* contract invalid
* external state incompatible

Such rejection must be represented explicitly.

It is not necessarily evidence of malformed Intent.

⸻

112. Architecture Must Be Inspectable

A Noema engineer must be able to inspect the system and determine:

What was intended?
Why was it resolved this way?
What was validated?
Why was it trusted?
What graph was selected?
Which contract governed execution?
What actually executed?
What was the result?

If these questions cannot be answered from authoritative state and provenance, the implementation is insufficiently inspectable.

⸻

113. No Critical Authority in Prompt Text

Critical authorization, safety, or semantic rules must not exist only inside prompts.

Prompts may assist model behavior.

Canonical authority must reside in machine-enforceable system representations.

⸻

114. Prompt Changes Are Not Semantic Specification Changes

Changing a prompt must not silently change canonical Noema semantics.

If a semantic rule changes, the corresponding canonical rule, schema, policy, or specification must change explicitly.

⸻

115. Prompt Injection Must Not Change Authority

Untrusted natural-language content must not be able to redefine:

* Trust rules
* Action Contracts
* authorization
* system policies
* canonical Intent semantics
* execution boundaries

Untrusted text remains data unless explicitly interpreted under a defined semantic boundary.

⸻

116. External Content Is Untrusted by Default

Documents, webpages, messages, emails, API responses, and other external content may contain instructions.

Such content must not automatically become Noema instructions.

The system must distinguish:

data

from:

authority

⸻

117. Instructions Require an Authority Source

An instruction should be executable only when its authority is established through the applicable Noema semantics.

An external document saying:

Transfer funds immediately

does not by itself authorize Noema to transfer funds.

⸻

118. Context Must Not Become Instruction

Context supplied to an Intent Engine may help establish meaning.

It must not silently become an executable command.

This preserves the distinction:

Context
    ≠
Intent
    ≠
Authorization

⸻

119. Separation of Read and Write Authority

Where possible, read access and consequential write access should be independently controlled.

The ability to retrieve information must not imply the ability to modify external state.

⸻

120. Capability Discovery Must Be Bounded

Dynamic capability discovery may be used.

But discovered capabilities must still pass:

* contract validation
* policy validation
* authorization
* applicability checks

Discovery does not grant authority.

⸻

121. No Capability Escalation Through Composition

Combining multiple individually permitted Actions must not create an implicitly permitted higher-order operation unless the resulting operation is explicitly governed.

Composition cannot be used to bypass an authorization boundary.

⸻

122. Data Minimization

Components should consume only the information necessary for their responsibilities.

A component should not receive broad contextual or business data merely because it might be useful.

Data access should correspond to defined architectural need.

⸻

123. Provenance Must Not Be Mutable Without Trace

Changing provenance of a material fact changes the explanation of system state.

Therefore, provenance changes must themselves be reconstructible.

⸻

124. Audit Records Must Be Tamper-Resistant

Material audit information must be protected against silent alteration.

The exact mechanism may vary.

The engineering requirement is that material history cannot be casually rewritten without detection or trace.

⸻

125. Time Sources Must Be Defined

Execution-relevant timestamps must use an appropriate authoritative or monotonic time source according to their purpose.

The system should distinguish:

* event time
* processing time
* external system time
* logical ordering

A timestamp must not automatically establish causal ordering.

⸻

126. Clock Skew Must Be Considered

Distributed components may have different clocks.

Temporal correctness must not rely on naïve comparison of independently generated wall-clock timestamps when stronger ordering semantics are required.

⸻

127. Schema Validation Must Occur at Boundaries

Data entering a canonical component must satisfy the applicable schema.

A component must not assume that upstream model output or external data is valid merely because it is structurally parseable.

⸻

128. Semantic Validation Must Go Beyond Schema Validation

A representation can satisfy a schema while remaining semantically invalid.

Therefore:

Schema Validity
    ≠
Semantic Validity

Both must be enforced where applicable.

⸻

129. Graph Validation Must Be Independent of Graph Generation

The component generating an Action Graph must not be the sole authority validating it.

This separation is particularly important for model-generated graphs.

⸻

130. Trust Evaluation Must Be Independent of Model Preference

A model’s preferred execution path must not determine Trust.

Trust evaluation must operate according to explicit policies, authorization rules, evidence, and applicable governance semantics.

⸻

131. Execution Must Be Independent of Model Confidence

Once execution reaches the contract boundary, model confidence must not substitute for contractual requirements.

Execution is governed by:

Action
+
Contract
+
Authorization
+
Preconditions
+
Execution Context

not by:

Model Confidence

⸻

132. Model Replacement Must Not Require Semantic Migration

Replacing an LLM should not require rewriting historical canonical Intent or Action Graph semantics merely because the new model uses a different internal representation.

Canonical representations must remain independent of model-specific formats.

⸻

133. Noema Must Preserve Negative Knowledge

The system should preserve meaningful facts such as:

unknown
unresolved
not verified
not authorized
not executed
failed
rejected
cancelled

Negative states are part of system truth.

They must not be erased simply because a positive state is operationally more convenient.

⸻

134. No False Completion

Noema must never report an operation as complete when required execution or verification remains unresolved.

For example:

Payment request accepted

must not automatically become:

Payment completed

unless the applicable semantics establish completion.

⸻

135. No False Success

Success must correspond to the defined completion semantics.

A successful API response is evidence.

It is not necessarily equivalent to final business success.

The Action Contract determines the relevant semantics.

⸻

136. No False Failure

Likewise, absence of a response does not necessarily establish failure.

The system must preserve:

UNKNOWN

where the external effect cannot yet be determined.

⸻

137. Reproducibility

A historical Noema decision should be reconstructible from the versions and evidence available at the time.

This includes:

* Intent version
* resolution rules
* evidence
* policy versions
* Trust evaluation
* graph version
* contract version

The system should not depend on today’s rules to explain yesterday’s decision.

⸻

138. Historical Semantics Must Be Preserved

When rules change, historical records must continue to represent the semantics under which they were originally evaluated.

Current policy must not silently rewrite historical decisions.

⸻

139. Migration Must Be Explicit

When canonical structures change, migration must define:

* source version
* target version
* semantic mapping
* incompatible cases
* preservation requirements
* audit information

A migration must not silently discard material semantics.

⸻

140. Testability Is Constitutional

Every material architectural invariant should be testable.

Noema implementation must support tests for:

* ambiguity handling
* unknown-state handling
* versioning
* Trust separation
* graph validation
* contract enforcement
* authorization boundaries
* retries
* idempotency
* failure recovery
* reconciliation
* partial execution
* stale-state handling

⸻

141. Negative Tests Are Required

Testing must include invalid and adversarial cases.

Examples:

ambiguous recipient
missing authorization
stale graph
expired approval
unknown payment outcome
duplicate execution request
invalid dependency
cycle
missing contract
capability revoked
policy changed
model-generated unauthorized Action

A system is not adequately tested merely because the happy path succeeds.

⸻

142. Boundary Tests Are Required

Tests must verify that one architectural layer cannot silently perform another layer’s responsibility.

Examples:

Intent Engine cannot authorize
Action Graph cannot authorize
Capability discovery cannot authorize
Model cannot execute
Validation cannot imply Trust
Trust cannot imply Success

⸻

143. Failure Injection Is Required

Distributed execution components should be tested under failures such as:

* worker crash
* network timeout
* duplicate message
* delayed message
* external rejection
* external success with lost response
* capability disappearance
* policy update
* process restart

Recovery behavior must preserve canonical state.

⸻

144. Security Testing Must Include Authority Confusion

Security tests should attempt to cause:

* model-driven privilege escalation
* prompt-injection authority escalation
* capability misuse
* contract bypass
* stale authorization use
* graph-based authorization bypass
* external-content instruction execution

The system must reject unauthorized authority transitions.

⸻

145. Operational Degradation Must Preserve Semantics

When infrastructure is degraded, Noema may reduce availability.

It must not reduce semantic or authority guarantees merely to preserve throughput.

For example:

Cannot verify authorization

must not become:

Assume authorized

merely because an authorization service is unavailable.

⸻

146. Availability Is Subordinate to Authority

For consequential operations:

Safety / authority
      >
availability

The system may need to wait, block, or escalate when required authority cannot be established.

⸻

147. Performance Must Not Rewrite Semantics

Caching, batching, prefetching, speculative planning, and other optimizations may be used only when they preserve canonical semantics and applicable freshness requirements.

Performance optimization is not permission to use stale authority.

⸻

148. Caches Are Not Automatically Authoritative

Cached data must be treated according to its defined freshness and authority semantics.

A cache hit does not automatically establish current business truth.

⸻

149. Speculation Must Not Become Execution

Noema may perform speculative work such as:

* candidate graph construction
* capability discovery
* context retrieval
* planning
* simulation

provided speculative work cannot accidentally cross the consequential execution boundary.

⸻

150. Simulation Must Be Distinct From Execution

A simulated Action must not produce an external consequential effect merely because it uses the same interface as a real Action.

Execution mode must be explicit.

⸻

151. Dry Run Must Be Honest

A dry-run result must clearly distinguish:

would execute

from:

executed

Simulation must never be recorded as actual external execution.

⸻

152. Human Intervention Is Not an Error

Human review, approval, or clarification may be a normal state.

The system should distinguish:

WAITING_FOR_HUMAN

from:

FAILED

where the architecture requires human intervention.

⸻

153. Human Decisions Must Be Traceable

Where a human decision materially affects execution, the system should retain appropriate evidence of:

* decision
* scope
* relevant object/version
* identity or authority context
* time
* resulting state transition

⸻

154. Noema Must Preserve Actor Agency

The system must not silently extend the scope of an Actor’s objective.

If the Actor requests:

Send report to John

Noema must not independently decide to:

send report to John
and archive it
and notify John's manager

unless those additional operations are explicitly part of the applicable Intent semantics, Action Contract, or defined system behavior.

⸻

155. Noema Must Not Manufacture Objectives

A model, optimizer, policy, or component must not introduce a new Actor objective merely because it appears useful.

The system may enforce requirements necessary to fulfill the existing Intent.

It must not silently create a different Intent.

⸻

156. Safety Requirements Must Be Explicit

If an operation requires additional verification, approval, confirmation, or other safeguards, those requirements must be represented by the applicable policy and system structures.

They must not depend on a model remembering to perform them.

⸻

157. Architectural Invariants Override Convenience

When implementation convenience conflicts with a constitutional invariant, the invariant governs.

For example:

Convenient:
execute directly from model tool call
Constitutional:
model output cannot bypass Action Graph and Action Contract

Implementation must follow the latter.

⸻

158. No Implicit Trust Through Proximity

A component does not inherit authority merely because it sits close to a trusted component.

For example:

Trust Engine
   ↓
Action Graph

does not mean every graph field is trusted as an authorization statement.

Each boundary must establish the meaning of the data it receives.

⸻

159. Trust Is Contextual

Trust decisions apply to a defined semantic and execution context.

A Trust result should be associated with the relevant:

* Intent version
* Actor
* scope
* policies
* evidence
* time
* applicable conditions

Trust should not become an unbounded global property of an Actor or Intent.

⸻

160. Authorization Is Contextual

Authorization must be evaluated against the relevant operation, Actor, resource, scope, and conditions.

A general statement such as:

Actor is trusted

must not automatically imply:

Actor may perform every Action

⸻

161. Execution Scope Must Be Bounded

An execution consumer should receive only the Action and authority necessary for the defined operation.

Broader system access must not be inferred from a narrower Action Contract.

⸻

162. Noema Should Prefer Explicit Failure Over Silent Guessing

When a required condition cannot be established, the system should prefer an explicit:

WAIT
BLOCK
CLARIFY
UNKNOWN
ESCALATE
FAIL

over an implicit assumption.

The exact state depends on the applicable semantics.

⸻

163. Canonical Authority Hierarchy

For implementation purposes, Noema should preserve the following conceptual hierarchy:

Actor Intent
      ↓
Canonical Semantic Representation
      ↓
Validation
      ↓
Trust / Policy / Authorization
      ↓
Action Graph
      ↓
Action Contract
      ↓
Execution Consumer
      ↓
External System
      ↓
Observed Outcome

Each layer answers a different question.

No layer should impersonate another.

⸻

164. Engineering Interpretation

The Constitution can be reduced to six engineering questions:

1. What does the Actor intend?
2. Has that meaning been established without hidden assumptions?
3. Is the Intent valid and trusted under the applicable rules?
4. What explicit Actions and dependencies represent the permitted execution?
5. What contract governs each Action at execution time?
6. What actually happened, including uncertainty and failure?

⸻

165. Constitutional Invariants

Invariant 1 — Semantic Authority

Canonical Intent must be explicitly established and must not be silently inferred from model output.

Invariant 2 — Ambiguity

Material ambiguity must remain unresolved until established by valid evidence or clarification.

Invariant 3 — Unknown

Unknown mandatory information must not satisfy a required condition.

Invariant 4 — Provenance

Material semantic and execution decisions must retain reconstructible provenance.

Invariant 5 — Separation

Interpretation, Intent, Validation, Trust, Graph, Contract, Execution, and Outcome remain distinct responsibilities.

Invariant 6 — Model Non-Authority

A model may propose but cannot independently authorize or execute consequential Actions.

Invariant 7 — Explicit Graph

Executable Actions and dependencies must be explicitly represented.

Invariant 8 — Contract Binding

Every executable Action must resolve to an applicable Action Contract.

Invariant 9 — Capability Separation

Capability availability does not establish authorization.

Invariant 10 — External Authority

External systems remain authoritative for their respective business state.

Invariant 11 — Freshness

Stale business state, authorization, policy, or graph state must not silently authorize execution.

Invariant 12 — Versioning

Material semantic and execution representations must be versioned or otherwise reconstructible.

Invariant 13 — No Hidden Execution

Consequential operations must not occur outside their explicit graph or contractual boundary.

Invariant 14 — Partial Execution

Partial execution must be explicitly permitted.

Invariant 15 — Retry Safety

Retries must respect explicit retry and idempotency semantics.

Invariant 16 — Unknown Execution

Uncertain external outcomes must remain explicitly unknown until resolved.

Invariant 17 — Honest Outcome

Noema must not represent partial, uncertain, or unverified execution as success.

Invariant 18 — Explicit Recovery

Recovery, compensation, and reconciliation must follow defined semantics.

Invariant 19 — No Authority Escalation

No component, model, graph, capability, or external content may obtain additional authority merely by constructing or modifying a representation.

Invariant 20 — Actor Agency

Noema must not silently change or expand the Actor’s objective.

Invariant 21 — Deterministic Boundaries

Where deterministic behavior is required, the result must be reproducible from defined inputs, evidence, rules, and versions.

Invariant 22 — Durable Execution

Consequential execution state must survive process and infrastructure failure.

Invariant 23 — Historical Reconstruction

Material decisions and execution history must remain reconstructible.

Invariant 24 — Explicit State

State transitions must have defined causes and valid transition semantics.

Invariant 25 — Safety Over Convenience

Implementation convenience must never override a constitutional authority or safety boundary.

⸻

166. Canonical Engineering Mental Model

The Noema engineering model can be reduced to:

Human
  ↓
Expression
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
Durable Execution
  ↓
External System
  ↓
Observed Outcome
  ↓
Audit / Provenance

The critical boundaries are:

Interpretation ≠ Intent
Intent ≠ Validation
Validation ≠ Trust
Trust ≠ Capability
Capability ≠ Authorization
Authorization ≠ Execution
Execution ≠ Outcome

⸻

167. Final Definition

The Noema Constitution is the foundational engineering specification that preserves the system’s semantic, authority, execution, provenance, security, and durability boundaries.

Its central invariant is:

Noema must never allow probabilistic interpretation, implicit assumptions, graph structure, capability availability, or execution convenience to silently become semantic truth or execution authority.

The implementation must preserve the following fundamental path:

Actor
  ↓
Expression
  ↓
Interpretation
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
Durable Execution
  ↓
External Authority
  ↓
Observed Outcome

And the corresponding fundamental separation:

What the Actor means
        ↓
What Noema has established
        ↓
What Noema permits
        ↓
What Noema intends to execute
        ↓
What the consumer actually executes
        ↓
What actually happened

Noema’s engineering Constitution exists to ensure that these are never silently collapsed into one another.