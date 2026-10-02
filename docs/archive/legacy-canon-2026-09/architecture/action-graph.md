Action Graph

Status: Foundational
Version: 0.2
Domain: Architecture
Canonical Path: architecture/action-graph.md

⸻

1. Definition

The Action Graph is Noema’s explicit, inspectable representation of the executable Actions, dependencies, conditions, capabilities, contracts, and execution relationships required to fulfill an Intent.

The Action Graph represents how an Intent may be fulfilled.

It does not determine:

* what the Actor means — Intent Resolution
* whether the Intent is structurally valid — Validation
* whether the Intent is eligible to proceed — Trust
* what authority exists — Authorization
* how an Action is executed — Execution Consumer
* what actually happened — Outcome

The architectural separation is:

Intent
  ↓
Resolution
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

The Action Graph is therefore the structural bridge between execution eligibility and execution.

⸻

2. Core Principle

Noema must not reduce consequential execution to an opaque sequence of model-generated tool calls.

Execution structure must be explicit, inspectable, versioned, and governed by deterministic constraints.

Conceptually:

Trusted Intent
      ↓
Action Graph
      ↓
Action Contracts
      ↓
Execution Consumer
      ↓
External Systems
      ↓
Outcome

The graph makes execution dependencies, conditions, capabilities, and permitted relationships explicit.

A model may propose graph structure.

A model does not thereby establish that the graph is valid or executable.

⸻

3. Why the Action Graph Exists

Many Intents cannot be fulfilled through a single Action.

For example:

Intent:
"Renew my card and send it to my current address."
Possible execution structure:
Resolve Account
      ↓
Verify Card Eligibility
      ↓
Verify Delivery Address
      ↓
Request Card Renewal
      ↓
Confirm Renewal
      ↓
Initiate Delivery
      ↓
Verify Outcome

Some Actions may be sequential.

Others may be independent and potentially parallel.

Some may depend on outputs from previous Actions.

Some may require approval, confirmation, authorization, or other conditions.

The Action Graph provides the explicit representation of these relationships.

⸻

4. Action Graph vs Intent

An Intent is not an Action Graph.

The Intent represents the Actor’s objective.

The Action Graph represents a possible operational realization of that objective.

For example:

Intent:
Replace my expired card.

may produce:

Check Card Status
        ↓
Check Replacement Eligibility
        ↓
Create Replacement Request
        ↓
Verify Request Accepted

The graph may change while the Intent remains unchanged.

Therefore:

Intent ≠ Action Graph

The graph is derived from the Intent, applicable Context, available capabilities, Action definitions, policies, and execution requirements.

⸻

5. Action Graph vs Execution Plan

The Action Graph is the canonical structural representation of execution relationships.

An execution plan may contain additional strategy for traversing that structure.

For example:

Action Graph:
A → B
A → C
B → D
C → D

may yield an execution strategy:

Execute A
Parallel:
    B
    C
Then:
    D

The distinction is:

Action Graph
    =
structural dependencies and permitted relationships
Execution Plan
    =
concrete execution strategy

A model-generated plan must not become authoritative merely because it appears coherent.

⸻

6. Action Graph vs Workflow

A workflow generally represents a reusable operational process.

An Action Graph represents the execution structure relevant to a particular Intent.

For example:

Workflow:
Card Renewal Process

may produce different Action Graphs depending on:

* the Actor
* the resource
* the requested operation
* applicable policy
* available capabilities
* current Context
* execution constraints

Therefore:

Workflow = reusable process
Action Graph = Intent-specific execution structure

The precise relationship between reusable workflows and Action Graphs may be defined by a separate architecture specification.

⸻

7. Graph Model

Conceptually:

                    Intent
                      │
                      ▼
                 Action Graph
                      │
             ┌────────┼────────┐
             ▼        ▼        ▼
          Action A  Action B  Action C
             │        │        │
             └────┬───┴────┬───┘
                  ▼        ▼
                Action D
                   │
                   ▼
                Outcome

An Action Graph consists primarily of:

* Action nodes
* dependencies
* conditions
* inputs
* outputs
* capability bindings
* contract bindings
* execution relationships
* preconditions
* postconditions
* failure semantics
* atomicity semantics
* provenance
* version information

⸻

8. Action Graph Node

An Action Graph node represents an Action that may be evaluated for execution.

Conceptually:

ActionNode {
    id
    action
    inputs
    outputs
    capability
    contract
    preconditions
    postconditions
    dependencies
    constraints
    state
    provenance
}

The exact schema is implementation-defined and must remain consistent with the Action and Action Contract specifications.

⸻

9. Action Identity

Every executable Action must have an explicit canonical identity.

Examples:

CARD_STATUS_CHECK
CARD_REPLACEMENT_REQUEST
DELIVERY_ADDRESS_LOOKUP
CARD_DELIVERY_REQUEST

Action identity must not depend on natural-language descriptions generated by a model.

Human-readable descriptions may accompany canonical Action identities.

They do not replace them.

⸻

10. Action Inputs

An Action may require explicit typed inputs.

For example:

CARD_REPLACEMENT_REQUEST
Inputs:
    account_id
    card_id
    replacement_reason
    delivery_address

Inputs may originate from:

* the Intent
* trusted Context
* outputs of prior Actions
* explicit Actor-provided information
* explicitly permitted defaults
* authoritative external evidence

Inputs must not be invented merely to make a graph executable.

⸻

11. Action Outputs

Actions may produce outputs consumed by downstream Actions.

Example:

VERIFY_CARD
    ↓
card_eligibility
    ↓
REQUEST_REPLACEMENT

Outputs should be explicitly represented and typed where the relevant Action Contract supports typed values.

A downstream Action must not treat an output as established merely because the preceding node was executed; the output semantics and execution result must satisfy the applicable contract.

⸻

12. Dependencies

A dependency explicitly establishes a relationship between an Action and another Action or condition.

For example:

A
↓
B

means that B depends on A according to the dependency semantics represented by the graph.

A dependency must not be inferred merely from visual ordering.

It must be explicitly represented.

⸻

13. Dependency Types

The canonical model may support distinct dependency relationships, including:

DATA_DEPENDENCY
ORDER_DEPENDENCY
CONDITION_DEPENDENCY
AUTHORIZATION_DEPENDENCY
APPROVAL_DEPENDENCY
CONFIRMATION_DEPENDENCY
RESOURCE_DEPENDENCY

The exact taxonomy may evolve.

Different dependency semantics must not be silently conflated.

⸻

14. Data Dependency

A data dependency exists when an Action requires output from another Action.

Example:

LOOKUP_CUSTOMER
      │
      │ customer_id
      ▼
FETCH_CUSTOMER_ACCOUNT

The downstream Action cannot construct its required input until the upstream Action produces the required output.

⸻

15. Ordering Dependency

An ordering dependency establishes required sequencing even when the downstream Action does not consume the upstream Action’s output.

Example:

REVOKE_OLD_TOKEN
      ↓
ISSUE_NEW_TOKEN

The second Action must not execute before the first when the governing Action Contracts require that ordering.

⸻

16. Condition Dependency

An Action may depend on a condition established by another Action.

Example:

CHECK_ELIGIBILITY
       ↓
eligible = true
       ↓
RENEW_CARD

If:

eligible = false

the downstream Action must not execute unless the graph explicitly defines an alternative path.

The condition is part of the graph semantics.

⸻

17. Parallel Actions

Independent Actions may execute concurrently when the relevant graph, Action Contracts, resource constraints, and execution semantics permit it.

Example:

             ┌── CHECK_ACCOUNT ──┐
             │                   │
VERIFY_USER ─┤                   ├── COMPLETE_REQUEST
             │                   │
             └── CHECK_CARD ────┘

The graph represents:

VERIFY_USER → CHECK_ACCOUNT
VERIFY_USER → CHECK_CARD
CHECK_ACCOUNT → COMPLETE_REQUEST
CHECK_CARD    → COMPLETE_REQUEST

Parallelism must not be inferred solely from apparent independence.

The execution layer must establish that concurrent execution is safe and contractually permitted.

⸻

18. Sequential Actions

Actions requiring strict ordering must be explicitly represented.

Example:

A
↓
B
↓
C

Therefore:

B depends on A
C depends on B

A planner or executor must not reorder these Actions unless the governing semantics explicitly permit it.

⸻

19. Branching

An Action Graph may contain conditional branches.

Example:

CHECK_ELIGIBILITY
       │
   ┌───┴────┐
   │        │
eligible  ineligible
   │        │
   ▼        ▼
RENEW      STOP

The branch condition must be explicit.

A model must not silently select a branch based on an unstated assumption.

⸻

20. Convergence

Multiple branches may converge on a later Action.

Example:

          ┌── PATH A ──┐
START ────┤            ├── COMPLETE
          └── PATH B ──┘

The convergence condition must specify what must be satisfied before the downstream Action may execute.

⸻

21. Graph Acyclicity

The default Action Graph must be a directed acyclic graph.

For example:

A → B → C

is valid.

An unrestricted cycle such as:

A → B → C
↑       ↓
└───────┘

must not be permitted.

Cycles are permitted only where the architecture explicitly defines a bounded iterative construct.

This prevents uncontrolled execution loops.

⸻

22. Iteration

Some business processes legitimately require repetition.

For example:

Poll Delivery Status
       ↓
   Is Delivered?
    ↙       ↘
  No         Yes
  ↓           ↓
 Wait       Complete
  ↓
Poll Again

This must not be represented as an unrestricted graph cycle.

Instead, iteration should be represented through an explicit bounded construct defining, where applicable:

* iteration condition
* maximum attempts
* timeout
* delay
* termination condition
* retry policy
* failure behavior

⸻

23. Graph Preconditions

An Action may define preconditions.

Example:

RENEW_CARD
Preconditions:
    card.status = ELIGIBLE
    actor.authorized = true
    delivery.address_verified = true

An Action whose mandatory preconditions are not satisfied must not execute.

Preconditions may be evaluated by Trust, the execution consumer, or both, according to the applicable Action Contract.

The graph must not treat the existence of a precondition as evidence that the precondition is satisfied.

⸻

24. Graph Postconditions

Actions may define expected postconditions.

Example:

REQUEST_REPLACEMENT
Expected postcondition:
    replacement_request.status = CREATED

Postconditions support verification of execution effects.

They do not make Noema the authoritative owner of external business state.

Where an external system is authoritative, postcondition verification must rely on authoritative external observations.

⸻

25. Action Contract Boundary

Each executable Action must resolve to an applicable Action Contract before execution.

Conceptually:

Action Graph Node
       ↓
Action Contract
       ↓
Execution Consumer
       ↓
Execution

The Action Graph determines the structural role of an Action.

The Action Contract defines its executable interface, obligations, constraints, and consumer-facing semantics.

⸻

26. Capability Binding

An Action must bind to an appropriate capability.

Example:

Action:
CARD_REPLACEMENT_REQUEST
Capability:
card.replacement.create

Capability establishes that a mechanism for performing the Action exists.

It does not establish permission.

Therefore:

Capability ≠ Authorization

⸻

27. Authorization Within the Graph

An Action may have authorization dependencies.

Example:

TRANSFER_FUNDS
Authorization:
Actor may transfer from source account

The graph may represent an authorization dependency:

Authorization Check
        ↓
Transfer Action

The graph does not replace the Trust Engine or the authoritative authorization system.

Authorization remains part of the execution-eligibility boundary.

⸻

28. Approval Dependencies

Some Actions require human or organizational approval.

Example:

CREATE_TRANSFER
       ↓
WAIT_FOR_APPROVAL
       ↓
EXECUTE_TRANSFER

Approval may be represented as an explicit dependency.

Approval is structured evidence of a governance condition.

Receipt of approval must not bypass Trust re-evaluation or other mandatory conditions.

⸻

29. Confirmation Dependencies

An Action may require explicit Actor confirmation.

Example:

DELETE_ACCOUNT
       ↓
WAIT_FOR_CONFIRMATION
       ↓
EXECUTE_DELETE

Confirmation must be represented explicitly where required.

Conversational continuation must not be interpreted as confirmation unless the applicable semantics explicitly establish that behavior.

⸻

30. Graph and Trust

The Action Graph does not bypass Trust.

The canonical relationship is:

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

Graph construction may begin before Trust is complete for analysis or candidate planning.

However, no Action may cross the execution boundary without satisfying applicable Trust requirements.

⸻

31. Candidate Graph Before Trust

Noema may construct a candidate Action Graph while an Intent is still being evaluated.

For example:

Intent
  ↓
Candidate Action Graph
  ↓
Trust Evaluation

The candidate graph is not therefore executable.

The architecture must preserve:

Candidate Graph ≠ Executable Graph

⸻

32. Graph Authorization

An Action Graph must never itself be interpreted as authorization.

For example:

Graph contains:
TRANSFER_FUNDS

does not establish:

Actor is authorized to transfer funds.

The graph represents a possible execution structure.

Trust and Action Contracts establish whether the individual Actions may actually execute.

⸻

33. Graph Validity

An Action Graph must itself satisfy structural requirements before execution.

Graph validation may establish:

* required nodes exist
* node identities are valid
* dependencies reference valid nodes
* dependency semantics are coherent
* required inputs are available or have defined sources
* cycles are prohibited or explicitly bounded
* conditions are well formed
* Action Contracts are resolvable
* capability references are valid
* graph versioning is valid
* atomicity semantics are defined where required
* failure semantics are defined where required

⸻

34. Graph Validation Result

Conceptually:

ActionGraphValidationResult {
    status
    errors
    warnings
    unresolved_dependencies
}

Possible statuses include:

VALID
INVALID
INCOMPLETE
UNKNOWN

Unknown must remain distinguishable from valid.

An unresolved mandatory condition must not silently become satisfied.

⸻

35. Graph Immutability During Execution

Once execution begins, the graph governing that execution must not be silently mutated.

If the Intent or material execution conditions change, Noema must represent the change explicitly.

Conceptually:

Graph Version 1
      ↓
Material Change
      ↓
Re-evaluation
      ↓
Graph Version 2

The relationship between graph versions must remain auditable.

⸻

36. Graph Versioning

An Action Graph should have an explicit version or evaluation identity.

Conceptually:

Intent Version: 7
Graph Version: 3
Trust Evaluation: 14

This allows Noema to reconstruct which graph was evaluated and authorized for execution.

A graph version must not silently inherit execution authority from a materially different graph.

⸻

37. Graph Provenance

The Action Graph should record why each significant Action and dependency exists.

Provenance may include:

* source Intent
* Intent version
* Context references
* Action identity
* capability source
* applicable policy
* dependency source
* evidence references
* graph generation or evaluation ID
* graph version
* creation timestamp
* relevant rule versions

This supports auditability without requiring exposure of private model reasoning.

⸻

38. Model-Generated Graphs

LLMs may propose Action Graphs.

The canonical architecture is:

LLM
 ↓
Candidate Action Graph
 ↓
Deterministic Graph Validation
 ↓
Trust / Contract Validation
 ↓
Executable Action Graph

A model-generated graph remains a proposal until it satisfies the applicable deterministic requirements.

Model output must not silently become graph authority.

⸻

39. No Hidden Actions

An executable graph must not contain implicit consequential Actions that are absent from the graph or from an explicitly defined Action Contract.

For example, if the graph contains:

TRANSFER_FUNDS

but execution silently performs:

LOOKUP_ACCOUNT
CHECK_BALANCE
CREATE_AUDIT_RECORD
SEND_NOTIFICATION

those operations must either be:

* explicit graph nodes
* contractually required behavior of the Action Contract
* or otherwise explicitly defined execution behavior

Noema must avoid hidden execution semantics.

⸻

40. No Arbitrary Model Tool Calls

A model must not bypass the Action Graph by directly issuing arbitrary consequential tool calls.

The canonical path remains:

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
Execution

Tool invocation is an implementation mechanism.

It is not an authority model.

⸻

41. Action Graph and Existing Systems

The Action Graph does not replace enterprise systems.

It coordinates Actions against available capabilities.

Example:

Noema Action Graph
       │
       ├── CRM capability
       ├── Identity capability
       ├── Payment capability
       └── Notification capability

External systems remain authoritative for their respective business domains.

⸻

42. Action Graph and Business State

The graph may depend on external business state.

For example:

Account.status = ACTIVE

may be required before an Action executes.

Noema may acquire this state from the authoritative system.

It must not silently claim ownership of that state.

⸻

43. External State Can Change

An Action Graph may become unsuitable for execution between construction and execution.

Example:

T1:
Account = ACTIVE
T2:
Account = SUSPENDED
T3:
Execute Action

The execution consumer may reject the Action.

This does not necessarily mean the original graph was structurally invalid.

It demonstrates that external business state is dynamic.

⸻

44. Time-of-Check / Time-of-Use

The graph must account for TOCTOU conditions.

Conceptually:

Validate
   ↓
Trust
   ↓
Contract
   ↓
Execute

does not imply:

Conditions at Validate
=
Conditions at Execute

Consequential Action Contracts may therefore require final authoritative checks at execution time.

⸻

45. Failure Propagation

Failure in one node may affect downstream nodes.

Example:

A
↓
B
↓
C

If:

B = FAILED

then C must not automatically execute unless the graph explicitly defines a valid recovery or alternate path.

⸻

46. Failure Policies

An Action Graph may explicitly define failure behavior such as:

STOP
RETRY
COMPENSATE
SKIP
ESCALATE
CONTINUE

These semantics must be explicit.

A model must not invent recovery behavior during execution.

⸻

47. Retry

Retries must be bounded and contractually defined.

Conceptually:

Action
  ↓
FAILED
  ↓
Retry permitted?
  ├── No → FAILED
  └── Yes
       ↓
     Retry

Retry semantics should account for:

* maximum attempts
* timeout
* idempotency
* retryable failure classes
* backoff
* external system semantics

An arbitrary increase in retries must not become an implicit execution strategy.

⸻

48. Idempotency

Actions that may be retried should define appropriate idempotency semantics.

For example:

CREATE_PAYMENT

must not accidentally create multiple payments merely because Noema retries after an uncertain response.

Idempotency belongs primarily to the Action Contract and execution architecture, but the Action Graph must respect those semantics.

⸻

49. Compensation

Some multi-Action executions may require compensating Actions.

Example:

A → B → C
C fails
Compensation:
B_compensate
A_compensate

Compensation must not be assumed to be equivalent to rollback.

External systems may not support transactional rollback.

Compensation semantics must therefore be explicit.

⸻

50. Partial Execution

A graph may partially execute.

Example:

A → COMPLETED
B → COMPLETED
C → FAILED
D → NOT_STARTED

The resulting execution record must distinguish:

* completed Actions
* failed Actions
* pending Actions
* skipped Actions
* unknown Actions

Partial execution must not be silently represented as overall success.

⸻

51. Unknown Execution Outcome

An Action may produce an unknown execution result.

Example:

REQUEST_PAYMENT
      ↓
Network Timeout
      ↓
Result = UNKNOWN

Noema must not assume:

FAILED

when the external system may have successfully processed the request.

The graph and Action Contract must support explicit unknown execution outcomes where required.

⸻

52. Completion Conditions

Graph completion must be explicitly defined.

A graph is not necessarily complete merely because the final node returned a successful response.

Completion may require:

* all mandatory nodes completed
* required postconditions verified
* required external outcomes observed
* no unresolved mandatory branches
* no outstanding compensation requirements

The precise completion semantics belong to the execution specification.

⸻

53. Graph Outcome

The Action Graph may participate in an execution-level outcome model such as:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN

These outcomes must remain distinct from Trust state.

For example:

Trust State:
READY
Execution State:
FAILED

is valid.

⸻

54. Composite Actions

An Action Graph may contain Actions that themselves represent composite operations.

For example:

RENEW_CARD

may internally invoke multiple provider operations.

Whether those internal operations are represented as graph nodes depends on the Action Contract boundary.

The abstraction boundary must remain explicit.

⸻

55. Atomicity

The graph must distinguish whether a group of Actions is:

* atomic
* independently executable
* partially executable
* compensatable

Noema must not infer atomicity merely because Actions belong to the same Intent.

⸻

56. Composite Intent

A composite Intent may produce multiple related Action Graph components.

Example:

Intent:
"Close the account, transfer the remaining balance,
and notify me."

Possible graph:

Close Account
Transfer Balance
Send Notification

The graph must encode whether these Actions are:

* sequential
* parallel
* conditionally dependent
* atomic
* independently executable

The Intent semantics and applicable execution rules determine whether partial execution is permissible.

⸻

57. Partial Execution Must Be Explicit

If an Intent does not permit partial execution:

A = READY
B = BLOCKED
C = READY

must not result in:

Execute A
Execute C

merely because those nodes are individually executable.

The graph must respect the declared atomicity and partial-execution semantics.

⸻

58. Graph State

Each node may have an execution state.

Conceptually:

NOT_READY
READY
EXECUTING
COMPLETED
FAILED
SKIPPED
BLOCKED
WAITING
UNKNOWN

The graph may also have an aggregate execution state.

Graph state must remain distinct from Trust state and external business outcome.

⸻

59. Trust State vs Graph State

These states must not be conflated.

For example:

Trust:
READY
Graph:
READY
Execution:
NOT_STARTED

Later:

Trust:
READY
Graph:
EXECUTING
Execution:
EXECUTING

Finally:

Trust:
READY
Execution:
FAILED

Trust establishes eligibility.

Graph state represents execution structure and progression.

Execution state represents what occurred operationally.

⸻

60. Graph Re-Evaluation

Material changes may require graph re-evaluation.

Examples include:

* capability disappears
* Action Contract changes
* required resource becomes unavailable
* policy changes
* Intent changes
* authorization changes
* dependency becomes invalid
* external state changes materially
* execution constraints change

Conceptually:

Action Graph
     ↓
Material Change
     ↓
Graph Revalidation
     ↓
Trust Re-evaluation
     ↓
Graph Revision if required

Noema must not silently continue execution using a graph whose material assumptions are no longer valid.

⸻

61. Graph Invalidation

A graph should be considered invalid for continued execution when a material dependency no longer holds.

Example:

Graph:
Transfer → Notify
Transfer capability revoked

The graph may require revision before execution continues.

Graph invalidation is distinct from execution failure.

⸻

62. Graph and Policy

Policies may affect graph construction.

Example:

Transfer > ₦10M
        ↓
Approval Required

The resulting graph may contain:

Create Transfer
      ↓
Request Approval
      ↓
Execute Transfer

Policy establishes the governance requirement.

The graph represents the resulting operational dependency.

⸻

63. Graph and Risk

Risk controls may add conditions or prohibit execution.

Example:

High-Risk Transfer
        ↓
Additional Verification
        ↓
Approval
        ↓
Transfer

Risk policy may therefore alter the graph.

The graph does not itself become the source of risk authority.

⸻

64. Graph and Human Intervention

Human intervention can be represented as an explicit dependency.

Example:

ACTION
  ↓
HUMAN_REVIEW
  ↓
CONTINUE

The graph should distinguish:

HUMAN_REVIEW_REQUIRED

from:

ACTION_FAILED

Human intervention is a legitimate execution state where the applicable policy requires it.

⸻

65. Graph and Clarification

Clarification normally occurs before an executable graph is finalized when required semantic information is missing.

Example:

Intent:
"Send the report to John."
Multiple Johns identified
        ↓
Clarification
        ↓
Resolved Intent
        ↓
Action Graph

Noema must not construct an executable graph by arbitrarily selecting a recipient.

⸻

66. Candidate vs Executable Graph

The architecture must preserve:

Candidate Action Graph
        ↓
Graph Validation
        ↓
Trust Evaluation
        ↓
Contract Validation
        ↓
Executable Action Graph

A candidate graph may contain unresolved dependencies.

An executable graph must satisfy the requirements necessary to cross the execution boundary.

⸻

67. Graph Determinism

For a given set of:

* Intent
* Context
* Evidence
* capabilities
* policies
* Action definitions
* Action Contracts
* graph rules
* relevant versions

the canonical graph construction should be deterministic where deterministic construction is required.

If multiple valid execution strategies exist, Noema may represent alternative candidate graphs or select among them using explicitly defined criteria.

Selection must not silently become arbitrary model behavior.

⸻

68. Graph Selection

Multiple graphs may fulfill the same Intent.

Example:

Intent:
Notify customer.

Possible capabilities:

Email
SMS
Push Notification

Selection may depend on:

* Actor preference
* available capability
* policy
* cost constraints
* delivery requirements
* Context
* explicit Intent constraints

Selection criteria must be explicit.

⸻

69. Graph Optimization

Graph optimization may seek to improve:

* execution latency
* external calls
* resource consumption
* reliability
* cost
* parallelism

Optimization must not violate:

* Intent semantics
* Trust requirements
* Action Contracts
* policies
* authorization
* constraints
* atomicity
* safety boundaries

Optimization is subordinate to correctness and authority.

⸻

70. No Semantic Mutation Through Optimization

Graph optimization must not change the Actor’s Intent.

For example:

Intent:
Send an email and create an audit record.

An optimizer cannot remove the audit record merely because doing so reduces execution cost.

Graph optimization changes execution structure.

It must not change Intent semantics.

⸻

71. Graph Observability

Noema should be able to inspect:

* graph version
* node states
* dependency states
* selected capabilities
* Action Contracts
* execution timestamps
* failures
* retries
* compensation
* human interventions
* graph revisions
* final execution outcome

This provides operational observability without requiring exposure of private model reasoning.

⸻

72. Graph Audit History

Significant graph changes must be auditable.

Example:

Graph v1
    ↓
Capability unavailable
    ↓
Graph invalidated
    ↓
Graph v2
    ↓
Alternative capability selected

The history should preserve the cause and basis of the graph change.

⸻

73. Graph Provenance and Model Provenance

If an LLM proposed a graph, Noema may record:

generation_source = model
model_id
model_version
generation_timestamp

This identifies the graph’s origin.

It does not establish graph authority.

Canonical authority remains with:

Deterministic Validation
+
Trust
+
Action Contracts
+
Execution Constraints

⸻

74. Security Boundary

The Action Graph must not become an authority-escalation mechanism.

A malicious or compromised model must not obtain additional capabilities merely by constructing a graph that references them.

Capability and authorization must remain independently verified.

Graph structure cannot grant:

* permission
* scope
* credentials
* elevated authority
* access to restricted resources

⸻

75. Capability Discovery

Noema may discover available capabilities dynamically.

Conceptually:

Intent
   ↓
Required Action
   ↓
Capability Discovery
   ↓
Candidate Capabilities
   ↓
Capability Selection
   ↓
Action Graph

Discovered capabilities must still satisfy applicable:

* capability requirements
* Action Contracts
* authorization
* policy
* Trust conditions
* execution constraints

⸻

76. Consumer Validation

The execution consumer may reject an Action after graph validation.

Example:

Noema:
Graph valid
Trust ready
Contract valid
Consumer:
Precondition no longer satisfied

The execution consumer remains authoritative over execution-time business conditions within its domain.

⸻

77. Graph Does Not Guarantee Success

An executable graph establishes an execution structure that has satisfied the applicable prerequisites.

It does not guarantee:

Execution = SUCCESS

External systems may fail.

Resources may change.

Networks may fail.

Business state may change.

Therefore:

Executable Graph ≠ Successful Outcome

⸻

78. Canonical Action Graph Lifecycle

The conceptual lifecycle is:

Resolved Intent
       ↓
Candidate Actions
       ↓
Candidate Action Graph
       ↓
Graph Validation
       ↓
Trust Evaluation
       ↓
Capability Binding
       ↓
Action Contract Binding
       ↓
Executable Action Graph
       ↓
Execution
       ↓
Postcondition Verification
       ↓
Outcome

At appropriate stages, Noema may need to:

CLARIFY
WAIT
BLOCK
REPLAN
ESCALATE
FAIL

These transitions must be governed by explicit semantics.

⸻

79. State Transition Principle

An Action Graph state may change only because of:

* a defined event
* a dependency transition
* a contract result
* a material condition change
* deterministic re-evaluation
* an explicitly defined execution transition

It must not change merely because:

* a model became more confident
* a prompt was reformulated
* a model generated a different plan
* a retry occurred without an applicable retry policy

⸻

80. Action Graph Invariants

Invariant 1

The Action Graph represents execution structure, not Intent meaning.

Invariant 2

The Action Graph does not grant authorization.

Invariant 3

Every executable Action must resolve to an explicit capability and applicable Action Contract.

Invariant 4

Dependencies must be explicit.

Invariant 5

Conditional branches must have explicit conditions.

Invariant 6

Unknown mandatory conditions must not be treated as satisfied.

Invariant 7

A candidate graph is not automatically executable.

Invariant 8

Graph optimization must not alter Intent semantics.

Invariant 9

Partial execution must be explicitly permitted.

Invariant 10

Retries must respect defined retry and idempotency semantics.

Invariant 11

External business systems remain authoritative for their business state.

Invariant 12

Material graph changes must be auditable.

Invariant 13

A stale graph must not silently cross the execution boundary.

Invariant 14

Execution failure does not by itself imply that the preceding Trust decision was invalid.

Invariant 15

Graph structure must never be used to bypass Trust, authorization, policy, or Action Contract requirements.

Invariant 16

Hidden consequential Actions must not exist outside the graph or an explicitly defined Action Contract boundary.

Invariant 17

Unknown execution outcomes must remain distinct from confirmed failure.

Invariant 18

Graph versions must remain tied to the Intent and execution conditions against which they were established.

Invariant 19

Material graph changes require explicit revision or re-evaluation.

Invariant 20

A model-generated graph remains non-authoritative until it satisfies the deterministic requirements governing executable graphs.

⸻

81. Canonical Mental Model

The Action Graph can be reduced to five questions:

1. What Actions are required to fulfill the Intent?
2. What does each Action depend on?
3. Which capabilities and Action Contracts can perform those Actions?
4. Under what conditions may each Action execute?
5. What happens if an Action succeeds, fails, or produces an unknown result?

The resulting abstraction is:

Intent
  ↓
Actions
  ↓
Dependencies
  ↓
Conditions
  ↓
Capabilities
  ↓
Contracts
  ↓
Execution
  ↓
Outcome

⸻

82. Relationship to the Noema Architecture

The Action Graph fits into the broader architecture as follows:

                    HUMAN
                      │
                      ▼
                   INTENT
                      │
                      ▼
               INTERPRETATION
                      │
                      ▼
                 RESOLUTION
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
             ┌────────┴────────┐
             ▼                 ▼
       ACTION CONTRACTS     DEPENDENCIES
             │                 │
             └────────┬────────┘
                      ▼
                  EXECUTION
                      │
                      ▼
                   OUTCOME

Each layer has a distinct architectural responsibility.

The Action Graph does not absorb the responsibilities of Intent, Validation, Trust, Action Contracts, Execution, or Outcome.

⸻

83. The Fundamental Boundary

The Action Graph is the structural bridge between:

May this Intent proceed?

and:

How will the permitted Actions actually be performed?

Therefore:

Trust
  ↓
Execution Eligibility
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

The graph must never become a substitute for Trust.

Likewise, Trust must not be treated as an execution plan.

⸻

84. Final Definition

The Action Graph is Noema’s explicit, inspectable representation of the Actions, dependencies, conditions, capabilities, contracts, and execution relationships required to fulfill a trusted Intent.

Its central invariant is:

Noema does not execute an opaque model-generated plan. It executes explicit Actions governed by explicit dependencies, capabilities, contracts, authorization, policies, constraints, and execution conditions.

The model may propose.

The architecture validates.

Trust establishes eligibility.

The Action Graph establishes executable structure.

The Action Contract establishes the executable interface and obligations.

The execution consumer performs the Action.

The external system remains authoritative for its business state and outcome.