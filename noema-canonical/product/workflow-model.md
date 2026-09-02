Yes. workflow-model.md should sit above individual Actions and describe how multiple Intents, Actions, states, policies, and human interventions are coordinated over time. It should also stay consistent with the distinctions we established in the earlier canonical files.

Workflow Model

Status: Foundational
Version: 0.1
Domain: Product
Canonical Path: product/workflow-model.md

⸻

1. Definition

A Workflow is a structured, stateful sequence of Intent, Action, decision, and execution steps that collectively accomplish an enterprise outcome.

The Workflow Model answers:

“How does Noema coordinate multiple steps, decisions, and participants toward an intended outcome?”

A Workflow is not simply a list of Actions.

It may contain:

* Intent
* Actions
* Preconditions
* Postconditions
* Trust decisions
* Policy evaluation
* branching
* sequencing
* parallel execution
* retries
* compensation
* human intervention
* waiting states
* events
* failure handling
* completion conditions

Conceptually:

Intent
   │
   ▼
Workflow
   │
   ├── Action
   ├── Action
   ├── Decision
   ├── Human Intervention
   ├── Wait
   └── Action
          │
          ▼
       Outcome

⸻

2. Purpose

The purpose of the Workflow Model is to provide a semantic representation for multi-step execution.

Enterprise operations frequently require more than one Action.

For example:

"Close my account."

may require:

Check balance
      ↓
Check pending transactions
      ↓
Cancel eligible services
      ↓
Close account
      ↓
Verify closure

The Workflow Model describes how these steps relate and how Noema moves between them.

⸻

3. Core Principle

A Workflow coordinates execution.

It does not become the authoritative owner of the Business State being modified.

Therefore:

Enterprise Systems
       │
       ▼
Business State
       │
       ▲
       │
    Workflow
       │
       ▼
     Actions

Noema owns the execution journey.

The enterprise remains authoritative for enterprise Business State unless explicitly delegated otherwise.

⸻

4. Workflow vs Action

An Action represents an executable operation.

A Workflow represents the coordination of multiple operations and decisions.

For example:

Action:
refund_payment

versus:

Workflow:
refund_and_close_account

The Workflow may contain:

refund_payment
verify_refund
close_account
verify_closure

Therefore:

Workflow ≠ Action

⸻

5. Workflow vs Intent

Intent represents what the User or initiating Principal wants to accomplish.

Workflow represents how Noema coordinates execution toward that Intent.

Conceptually:

Intent
  ↓
Workflow Selection / Construction
  ↓
Execution

For example:

Intent:
"Refund my payment and close my account."
Workflow:
1. Resolve payment
2. Validate refund eligibility
3. Refund payment
4. Verify refund
5. Validate account closure
6. Close account
7. Verify closure

The Workflow is derived from the executable Intent and applicable enterprise capabilities and policies.

⸻

6. Workflow Is Not the Intent

A User may express:

"Get this done."

The underlying Intent may be refined through clarification.

The Workflow should not be constructed until Noema has sufficient understanding of the Intent and its required execution semantics.

Therefore:

Natural Language
      ↓
Intent
      ↓
Resolution
      ↓
Workflow

not:

Natural Language
      ↓
Workflow

⸻

7. Workflow and Executable Intent

An executable Intent defines what Noema is permitted and expected to accomplish.

A Workflow operationalizes that Intent.

Conceptually:

Executable Intent
        │
        ▼
   Workflow
        │
        ├── Action A
        ├── Action B
        └── Action C

Every consequential Workflow should remain traceable to the Intent that produced it.

⸻

8. Workflow Identity

A Workflow should have a stable identity within Noema.

Conceptually:

Workflow {
    workflow_id
    intent_id
    state
    steps
    created_at
    updated_at
}

The identifier allows Noema to track:

* lifecycle
* state transitions
* executions
* interventions
* failures
* retries
* compensation
* outcomes
* audit history

⸻

9. Workflow Instance vs Workflow Definition

A Workflow Definition describes a reusable execution structure.

A Workflow Instance represents one concrete execution journey.

Example:

Workflow Definition:
refund_and_close_account
Workflow Instance:
WF-12345

The definition may be reused.

The instance contains the actual:

* Intent
* Resources
* parameters
* decisions
* state
* evidence
* executions
* outcomes

Therefore:

Workflow Definition ≠ Workflow Instance

⸻

10. Workflow Definition

A Workflow Definition may specify:

trigger
steps
dependencies
conditions
transitions
failure policies
retry policies
compensation
approval requirements
completion criteria

It defines possible execution behavior.

It does not represent the actual result of a particular Workflow Instance.

⸻

11. Workflow Instance

A Workflow Instance represents an actual execution.

Example:

Workflow:
refund_and_close_account
Instance:
WF-8421
User:
Jane
Payment:
PAY-123
Account:
ACC-456

The instance maintains execution-specific state.

⸻

12. Workflow State

A Workflow may move through states such as:

CREATED
RESOLVING
READY
RUNNING
WAITING
BLOCKED
AWAITING_HUMAN
COMPENSATING
SUCCEEDED
FAILED
CANCELLED
UNKNOWN

The exact state machine is defined by Workflow semantics and execution policy.

State must reflect observed execution state, not model confidence.

⸻

13. Workflow State Is Deterministic

Workflow state transitions should be deterministic with respect to:

* current state
* event
* Action outcome
* Preconditions
* Postconditions
* Policy
* evidence

The model may propose a Workflow.

It must not arbitrarily determine its runtime state.

Conceptually:

Model
  ↓
Candidate Workflow
  ↓
Noema Validation
  ↓
Deterministic Workflow State

⸻

14. Workflow Steps

A Workflow consists of Steps.

A Step may represent:

Action
Decision
Wait
Human Intervention
Verification
Compensation

Example:

Step 1 → Resolve Payment
Step 2 → Refund Payment
Step 3 → Verify Refund
Step 4 → Close Account
Step 5 → Verify Closure

Each Step has explicit semantics.

⸻

15. Step Identity

Every consequential Step should have an identifiable identity.

Conceptually:

Step {
    step_id
    workflow_id
    type
    state
    dependencies
}

This enables Noema to reason about:

* which Step is executing
* which Step failed
* which Step requires intervention
* which Step has completed

⸻

16. Step Dependencies

Steps may depend on other Steps.

Example:

Resolve Payment
      ↓
Refund Payment
      ↓
Verify Refund
      ↓
Close Account

A dependent Step must not execute until its required dependencies satisfy their conditions.

⸻

17. Sequential Execution

The simplest Workflow executes sequentially.

A
↓
B
↓
C
↓
D

Example:

Validate
  ↓
Authorize
  ↓
Execute
  ↓
Verify

Sequential execution is appropriate where later Steps depend on the state produced by earlier Steps.

⸻

18. Parallel Execution

Independent Steps may execute concurrently.

Example:

        ┌── Check Subscription
        │
Intent ─┼── Check Balance
        │
        └── Check Pending Transactions

The Workflow may continue when the required parallel Steps have completed.

Parallelism must not violate:

* dependency constraints
* data consistency
* authorization
* Action preconditions
* enterprise concurrency semantics

⸻

19. Join

Parallel branches may converge.

        ┌── A ──┐
Start ──┼── B ──┼── Join
        └── C ──┘

The Join defines the conditions under which the Workflow may continue.

For example:

A = SUCCESS
B = SUCCESS
C = SUCCESS

may be required.

Alternatively, Policy may permit:

A = SUCCESS
B = SUCCESS
C = FAILED

if C is non-critical.

⸻

20. Conditional Branching

A Workflow may branch based on deterministic conditions.

Example:

Check Balance
      │
      ├── balance = 0
      │      ↓
      │   Close Account
      │
      └── balance > 0
             ↓
         Refund / Settlement

Branching conditions must be grounded in appropriate enterprise state.

The model may propose the branch.

Noema determines whether the branch is valid.

⸻

21. Workflow Decisions

A Workflow Decision determines which execution path is valid.

Decisions may depend on:

* Context
* Canonical Data
* Evidence
* Policy
* Action state
* previous Outcomes

A consequential decision should be explainable and reproducible.

⸻

22. Workflow and Trust

Trust may be evaluated at multiple points.

For example:

Workflow
   ↓
Action A
   ↓
Trust
   ↓
Action A executes
   ↓
Action B
   ↓
Trust
   ↓
Action B executes

Trust should not automatically be treated as permanently valid for the entire Workflow.

A later Action may introduce:

* higher risk
* different Resource
* different authority
* different Policy
* changed Business State

requiring a new evaluation.

⸻

23. Workflow and Policy

Policy constrains Workflow execution.

Policy may define:

* allowed Actions
* required approvals
* risk thresholds
* sequencing requirements
* retry limits
* timeout behavior
* compensation requirements
* data requirements
* human intervention
* completion criteria

Therefore:

Workflow
    ↓
Policy Evaluation
    ↓
Permitted Execution Path

⸻

24. Workflow and Preconditions

Every consequential Action within a Workflow may have Preconditions.

Example:

Refund Payment
Preconditions:
    payment.status = CAPTURED
    refund.amount <= refundable_amount

The Workflow must satisfy required Preconditions before executing the Action.

⸻

25. Workflow and Postconditions

After an Action completes, the Workflow may require Postcondition verification.

Example:

Action:
refund_payment
Expected:
payment.status = REFUNDED

The Workflow should not infer success solely from an API response if authoritative verification is required.

⸻

26. Workflow and Canonical Data

Workflow decisions may depend on Canonical Data.

Example:

Workflow
    ↓
Check Account State
    ↓
Canonical Data
    ↓
Decision

The Workflow must preserve enterprise authority boundaries.

Noema should not manufacture canonical Business State for workflow convenience.

⸻

27. Workflow and Context

Workflow execution may require Context such as:

* User identity
* Resource references
* organizational scope
* current enterprise state
* prior Step outcomes
* relevant Policy
* execution history

Context should be scoped to the Workflow and Step where possible.

⸻

28. Workflow and Evidence

Evidence supports Workflow decisions and execution state.

Example:

Evidence:
payment.status = CAPTURED
source = Payment System
observed_at = T1

The Workflow may use this Evidence to satisfy a Precondition.

Evidence should preserve provenance sufficient to explain consequential decisions.

⸻

29. Workflow and Events

Events may drive Workflow transitions.

Example:

Payment Submitted
      ↓
Event
      ↓
Workflow
      ↓
Next Step

An event may indicate that a state changed.

Where current authoritative state matters, Noema may still verify against the System of Record.

⸻

30. Event-Driven Workflow

A Workflow may pause while waiting for an external event.

Example:

Submit Payment
      ↓
WAITING
      ↓
payment.completed
      ↓
Resume Workflow

Waiting is a legitimate Workflow state.

The Workflow should not simulate completion merely because an expected event is likely to arrive.

⸻

31. Workflow and Human Intervention

Human intervention may become a Workflow Step.

Examples:

Clarification
Approval
Manual Review
Exception Handling
Conflict Resolution
Recovery Decision

Conceptually:

Workflow
   ↓
AWAITING_HUMAN
   ↓
Human Decision
   ↓
Workflow resumes

The intervention must be attributable to the relevant Principal.

⸻

32. Workflow and Clarification

If Intent ambiguity prevents safe execution:

Workflow
   ↓
Missing Required Information
   ↓
Clarification
   ↓
User Response
   ↓
Intent Resolution
   ↓
Workflow Resumes

The Workflow should not bypass unresolved material ambiguity merely to continue execution.

⸻

33. Workflow and Approval

Some Steps may require approval.

Action
   ↓
Approval Required
   ↓
Approver
   ↓
Approved
   ↓
Execute

Approval must be bound to:

* Workflow
* Intent
* Action
* Resource
* relevant parameters
* approving Principal

where required.

⸻

34. Workflow and Compensation

A multi-step Workflow may partially succeed.

Example:

A → SUCCESS
B → SUCCESS
C → FAILED

If the Workflow requires rollback or corrective action, compensation may be initiated.

A
↓
B
↓
C FAILED
↓
Compensation
↓
Recover / Reverse

Compensation operates against enterprise Business State through authorized capabilities.

⸻

35. Workflow Is Not a Database Transaction

A Workflow may span:

* multiple systems
* long time periods
* asynchronous events
* human approvals
* irreversible operations

Therefore it cannot generally be treated as one atomic database transaction.

Instead, it may use:

* compensation
* reconciliation
* retries
* idempotency
* explicit intermediate states
* human intervention

⸻

36. Workflow and Failure

A Step may fail without the entire Workflow necessarily failing.

Example:

Optional Notification
        ↓
FAILED
        ↓
Workflow continues

Whereas:

Account Closure
        ↓
FAILED
        ↓
Workflow FAILED

Failure propagation is determined by Workflow semantics and Policy.

⸻

37. Workflow and Unknown State

A Workflow may enter:

UNKNOWN

when Noema cannot establish whether an external Action completed.

Example:

Request sent
    ↓
Connection lost
    ↓
Outcome unknown

Noema must not assume:

UNKNOWN = FAILED

or:

UNKNOWN = SUCCESS

without evidence.

⸻

38. Workflow and Retry

Retry behavior belongs to the Workflow and Action execution semantics.

A retry may be permitted when:

* failure is transient
* Action is idempotent or safely deduplicated
* Policy permits retry
* retry limits have not been exceeded

A retry must not blindly repeat a consequential operation.

⸻

39. Workflow and Idempotency

Every consequential Action should have appropriate idempotency semantics.

For example:

Workflow Step:
refund_payment
idempotency_key:
WF-123:refund_payment

If a network failure occurs, Noema should be able to determine whether retrying could duplicate the operation.

⸻

40. Workflow and Concurrency

Multiple Workflow Instances may operate on the same Resource.

Example:

Workflow A
   ↓
Account 123
Workflow B
   ↓
Account 123

Noema must respect enterprise concurrency semantics.

It should not assume that a state observed at Workflow creation remains valid throughout execution.

⸻

41. Workflow and State Changes

Enterprise state may change between Steps.

Example:

Step 1:
balance = $10,000
External change
Step 2:
balance = $2,000

The Workflow must revalidate consequential Preconditions where required.

Earlier Context must not automatically be treated as current truth.

⸻

42. Workflow and Staleness

Workflow Context can become stale.

Therefore:

Observed State
      ↓
Time passes
      ↓
Potentially stale

Freshness requirements should be defined by:

* Action
* Resource
* Policy
* risk

⸻

43. Workflow and Dynamic Planning

Some Workflows may be constructed dynamically.

Example:

Intent
  ↓
Available Capabilities
  ↓
Enterprise State
  ↓
Policy
  ↓
Dynamic Workflow

The model may assist with candidate planning.

Noema must validate the resulting Workflow against executable capabilities, Policy, Preconditions, and Trust requirements.

⸻

44. Workflow Planning vs Workflow Execution

Planning determines:

“What should happen?”

Execution determines:

“What is happening or what happened?”

These are distinct.

Planning
   ↓
Workflow Plan
   ↓
Validation
   ↓
Execution

A plan is not evidence that execution occurred.

⸻

45. Workflow Mutation

A Workflow may need to change after execution begins.

Examples:

* new enterprise state
* Action failure
* Policy change
* human intervention
* external event
* resource becoming unavailable

Changes must be explicit and auditable.

Noema should preserve the prior execution history rather than silently rewriting it.

⸻

46. Workflow Versioning

Workflow Definitions should be versioned where behavior may change.

Example:

refund_workflow:v1
refund_workflow:v2

An existing Workflow Instance should retain the definition version under which it was created or executed.

Historical execution should not be reinterpreted solely because a newer definition exists.

⸻

47. Workflow and Policy Versioning

Policy may also change over time.

Therefore an execution record may need to preserve:

workflow_version
policy_version
authorization_context
trust_decision

where required for reconstruction.

⸻

48. Workflow and Auditability

A consequential Workflow should produce an execution trail.

Conceptually:

Workflow Created
      ↓
Step Started
      ↓
Evidence Collected
      ↓
Trust Evaluated
      ↓
Action Executed
      ↓
Outcome Observed
      ↓
Next Step

This allows Noema to explain:

* what happened
* why it happened
* who authorized it
* what evidence was used
* where execution stopped

⸻

49. Workflow and Recovery

Recovery is the process of bringing an interrupted or failed Workflow to a valid terminal or recoverable state.

Possible paths:

FAILED
  ↓
RETRY

or:

FAILED
  ↓
COMPENSATE

or:

FAILED
  ↓
HUMAN INTERVENTION

or:

UNKNOWN
  ↓
RECONCILIATION

Recovery behavior is explicit Workflow semantics.

⸻

50. Workflow and Reconciliation

When Noema cannot determine the state of an external operation, reconciliation may query authoritative enterprise state.

Example:

Workflow:
refund = UNKNOWN
Payment System:
refund = COMPLETED
Reconciliation
      ↓
Step = SUCCEEDED

This prevents duplicate execution caused by treating uncertainty as failure.

⸻

51. Workflow Completion

A Workflow is complete only when its completion conditions are satisfied.

Completion may require:

All required Steps succeeded
      +
Postconditions verified
      +
Required human decisions completed
      +
No unresolved blocking state

Therefore:

last Action returned 200

does not necessarily mean:

Workflow = SUCCEEDED

⸻

52. Workflow Outcome

The Workflow Outcome describes the final established result.

Possible outcomes include:

SUCCEEDED
FAILED
CANCELLED
PARTIALLY_COMPLETED
UNKNOWN

The exact Outcome semantics must distinguish execution facts from assumptions.

⸻

53. Partial Completion

A Workflow may produce a partially completed result.

Example:

Refund:
SUCCESS
Account Closure:
FAILED

The Workflow should preserve both results.

It must not collapse the state into a misleading binary:

SUCCESS

or:

FAILED

without representing the underlying execution reality.

⸻

54. Workflow Cancellation

A Workflow may be cancelled when Policy and current execution state permit cancellation.

Cancellation is not necessarily rollback.

For example:

Pending Workflow
    ↓
Cancelled

may simply prevent future Steps from executing.

Already completed enterprise Actions may require separate compensation.

⸻

55. Workflow Timeouts

A Workflow may define timeouts for:

* individual Steps
* external responses
* human intervention
* overall execution

A timeout does not automatically establish external failure.

For example:

API Timeout
    ↓
Outcome UNKNOWN

may require reconciliation before another attempt.

⸻

56. Workflow and External Systems

A Workflow may cross multiple enterprise systems.

Example:

CRM
 ↓
Billing
 ↓
Payment
 ↓
Identity

Each Action must respect the relevant System of Record and authority boundary.

The Workflow coordinates them without collapsing their ownership models.

⸻

57. Workflow and Enterprise Action Graph

The Enterprise Action Graph provides the capabilities and relationships available to Noema.

The Workflow selects and coordinates appropriate Actions from that graph.

Conceptually:

Enterprise Action Graph
          ↓
      Planning
          ↓
       Workflow
          ↓
       Actions

The Workflow must not invent capabilities that do not exist in the enterprise environment.

⸻

58. Workflow and Integration

Workflow Steps execute through defined integrations.

Example:

Workflow
   ↓
Action
   ↓
Integration
   ↓
Enterprise System

Integration details should remain encapsulated by the Integration Model.

The Workflow should reason semantically about Actions rather than depend unnecessarily on transport-specific implementation details.

⸻

59. Workflow and User Experience

The User should experience the Workflow as progress toward an outcome rather than as internal infrastructure.

For example:

User:
"Close my account."
Noema:
Checking your account...
Noema:
There is a pending refund.
Noema:
The refund is complete.
Noema:
Your account has been closed.

The underlying Workflow may contain many Steps.

The User experience need not expose every internal transition.

⸻

60. Workflow Transparency

Noema should expose enough Workflow state to establish meaningful progress.

Useful states include:

Resolving
Waiting for approval
Executing
Waiting for external system
Verifying
Requires clarification
Requires intervention
Completed
Failed

Transparency should not expose unnecessary internal implementation details or sensitive enterprise information.

⸻

61. Workflow and Notifications

A Workflow may produce notifications when significant transitions occur.

Examples:

Approval Required
Action Completed
Human Intervention Required
Workflow Failed
Workflow Completed

Notifications are interaction concerns.

They should reflect established Workflow state.

⸻

62. Workflow and Long-Running Processes

Some Workflows may execute for:

seconds
minutes
hours
days

A Workflow must therefore support durable state and resumability where required.

Noema cannot assume that the process remains in memory for the entire lifecycle.

⸻

63. Workflow Resumption

A paused Workflow may resume when its blocking condition is satisfied.

Example:

WAITING_FOR_APPROVAL
        ↓
Approval Received
        ↓
RESUMING
        ↓
Next Step

Resumption should revalidate any state that may have become stale.

⸻

64. Workflow and Expiration

A Workflow may have an expiration policy.

For example:

Approval valid for 24 hours

After expiration:

Workflow
    ↓
Approval Expired
    ↓
Re-evaluation / New Approval

Noema should not reuse expired authorization or confirmation without applicable Policy allowing it.

⸻

65. Workflow and Security

Workflow execution must preserve security boundaries across every Step.

A Workflow must not become a mechanism for:

* privilege escalation
* tenant crossing
* authorization bypass
* data leakage
* unauthorized delegation

Each consequential Step remains subject to relevant security and Trust requirements.

⸻

66. Workflow and Data Boundaries

Each Step should request only the data required for execution.

For example:

Step:
refund_payment

may require:

payment_id
amount
currency
status

It should not automatically retrieve unrelated customer information.

Workflow composition must not become an excuse for unrestricted data aggregation.

⸻

67. Workflow and Resource Locking

Some enterprise operations may require resource coordination.

For example:

Workflow A
   ↓
Account 123
Workflow B
   ↓
Account 123

The enterprise system may provide locking, versioning, or concurrency controls.

Noema should use those mechanisms where required rather than assuming local Workflow state is sufficient to prevent conflicts.

⸻

68. Workflow and Optimistic Concurrency

A Workflow may use resource versions.

Example:

Account:
version = 42

Action expects:

version = 42

Enterprise system responds:

version changed to 43

The Workflow may need to:

re-read
revalidate
re-plan
clarify
or abort

according to Policy.

⸻

69. Workflow and Deterministic Replanning

Replanning may be required when the original plan becomes invalid.

For example:

Original Plan
      ↓
Enterprise State Changes
      ↓
Plan Invalid
      ↓
Replanning

Replanning must not silently change the User’s Intent.

The new plan must still satisfy the resolved Intent and applicable Trust requirements.

⸻

70. Workflow and Intent Preservation

The Workflow may change.

The Intent should remain the semantic anchor.

Example:

Intent:
"Get my account closed."
Plan A:
Refund → Close
Plan B:
Settlement → Close
Plan C:
Manual Review → Close

Different execution paths may satisfy the same Intent.

The Workflow is therefore an execution strategy, not the Intent itself.

⸻

71. Workflow and Intent Change

If the User materially changes the Intent:

"Close my account."
becomes:
"Actually, keep it open."

the existing Workflow may need to stop or be replaced.

Noema must not continue executing a Workflow that no longer corresponds to the active Intent.

⸻

72. Workflow and Compound Intent

Compound Intent may naturally produce multiple coordinated Workflows or one composite Workflow.

Example:

Intent:
"Refund the payment and close my account."

Possible structure:

Composite Workflow
       │
       ├── Refund Workflow
       └── Account Closure Workflow

The relationship between them must be explicit.

⸻

73. Workflow Composition

Workflows may be composed when one Workflow depends on another.

Workflow A
    ↓
Workflow B
    ↓
Workflow C

Composition must preserve:

* Intent relationships
* authorization boundaries
* resource boundaries
* failure semantics
* compensation semantics
* auditability

⸻

74. Workflow Nesting

A Workflow may invoke a sub-workflow.

Example:

Account Closure
      │
      ├── Refund Workflow
      ├── Subscription Workflow
      └── Identity Workflow

Each sub-workflow may maintain its own execution state while remaining associated with the parent Workflow.

⸻

75. Workflow and Atomicity Boundaries

A Workflow must explicitly define where atomicity is and is not available.

For example:

Payment System:
atomic refund operation
Cross-System Workflow:
not atomic

Noema should not present cross-system execution as atomic when the underlying enterprise systems cannot guarantee atomicity.

⸻

76. Workflow and Compensation Boundaries

Compensation is not guaranteed to restore the exact prior state.

For example:

Charge
  ↓
Refund

may be compensatable.

But:

Send Email

may not be truly reversible.

The Workflow must represent these differences explicitly.

⸻

77. Workflow and Irreversible Actions

Some Actions are irreversible or only partially reversible.

Examples:

Delete Resource
Send External Message
Submit Regulatory Filing
Release Funds

Such Actions should carry appropriate risk and Policy requirements.

The Workflow must not assume compensation exists merely because an Action failed later.

⸻

78. Workflow and Risk Escalation

Risk may increase as a Workflow progresses.

Example:

Step 1:
read account
Step 2:
modify account
Step 3:
transfer funds

A later Step may require stronger Trust controls.

The Workflow must therefore permit Trust evaluation to vary by Step.

⸻

79. Workflow and Human-in-the-Loop

Human involvement is a first-class Workflow capability.

Workflow
   ↓
Human Required
   ↓
WAITING
   ↓
Human Decision
   ↓
Workflow Resumes

Human intervention should be represented as explicit state rather than hidden outside the Workflow.

⸻

80. Workflow Observability

Noema should be able to observe:

current Workflow state
current Step
completed Steps
failed Steps
pending Steps
blocking conditions
required interventions
external dependencies

Observability supports operations, debugging, audit, and recovery.

⸻

81. Workflow History

Workflow history should be append-oriented where possible.

Noema should preserve:

state transition
Step execution
decision
evidence
human intervention
retry
compensation
Outcome

Historical events should not be silently overwritten.

⸻

82. Workflow and Audit Trail

A consequential Workflow should allow reconstruction of:

Original Intent
      ↓
Workflow Plan
      ↓
Trust Decisions
      ↓
Actions
      ↓
Evidence
      ↓
Outcomes
      ↓
Interventions
      ↓
Final Result

This creates an auditable execution journey.

⸻

83. Workflow and Noema’s System of Record

Noema may be authoritative for:

Workflow State
Step State
Execution State
Trust Decision
Intervention State
Workflow Outcome

The enterprise remains authoritative for its own Business State.

Therefore:

Noema System of Record
        │
        ├── Workflow
        ├── Intent
        ├── Trust
        └── Execution

while:

Enterprise Systems of Record
        │
        ├── Account
        ├── Payment
        ├── Customer
        └── Inventory

remain separate.

⸻

84. Workflow and Enterprise State

The Workflow records what Noema knows about execution.

It does not automatically become the source of truth for the enterprise resource.

Example:

Noema:
refund Step = SUCCEEDED
Payment System:
refund.status = PENDING

The discrepancy must be reconciled according to the relevant semantics.

⸻

85. Workflow and Unknown External State

If an external system cannot establish the state of an Action:

Workflow
   ↓
UNKNOWN
   ↓
Reconciliation

The Workflow should preserve uncertainty rather than invent a terminal state.

⸻

86. Workflow Termination

A Workflow should terminate only through defined terminal states.

Examples:

SUCCEEDED
FAILED
CANCELLED

An:

UNKNOWN

state may remain non-terminal until reconciliation or explicit Policy determines otherwise.

⸻

87. Workflow Invariants

Invariant 1

A Workflow coordinates execution; it is not an Action.

Invariant 2

A Workflow is derived from an Intent rather than replacing the Intent.

Invariant 3

Every consequential Workflow must remain traceable to its initiating Intent.

Invariant 4

A Workflow must not invent enterprise capabilities that do not exist.

Invariant 5

Workflow state must be based on established execution facts, not model confidence.

Invariant 6

A Workflow Definition and Workflow Instance are distinct concepts.

Invariant 7

Workflow Steps must have explicit semantics.

Invariant 8

Step dependencies must be satisfied before dependent execution.

Invariant 9

Parallel execution must respect dependency, consistency, authorization, and Policy constraints.

Invariant 10

Conditional branches must be based on deterministic, appropriately grounded conditions.

Invariant 11

Trust may need to be evaluated independently for different Workflow Steps.

Invariant 12

Policy constrains Workflow execution.

Invariant 13

Consequential Actions must satisfy their required Preconditions.

Invariant 14

Required Postconditions must be verified according to Action and Policy semantics.

Invariant 15

Workflow Context must not silently become authoritative enterprise Business State.

Invariant 16

Events may drive Workflow transitions but do not necessarily establish current canonical state.

Invariant 17

Human intervention must be represented explicitly when required.

Invariant 18

Confirmation and approval must remain bound to the relevant Intent, Action, Resource, and scope.

Invariant 19

A Workflow is not equivalent to a distributed database transaction.

Invariant 20

Partial completion must remain representable.

Invariant 21

UNKNOWN must not be silently converted into SUCCESS or FAILED.

Invariant 22

Retries must respect idempotency and Policy.

Invariant 23

Workflow execution must tolerate enterprise state changing between Steps.

Invariant 24

Stale Context must not automatically satisfy current consequential Preconditions.

Invariant 25

Workflow Definitions should be versioned when execution semantics change.

Invariant 26

Historical execution must remain reconstructable under the relevant Workflow and Policy versions.

Invariant 27

A Workflow may be dynamically planned, but dynamic plans must be validated before execution.

Invariant 28

Planning and execution are separate states.

Invariant 29

Workflow changes must not silently change the underlying User Intent.

Invariant 30

A material Intent change may invalidate the current Workflow.

Invariant 31

Workflow composition must preserve authorization, resource, failure, compensation, and audit boundaries.

Invariant 32

Noema must not represent cross-system execution as atomic when the underlying systems cannot guarantee atomicity.

Invariant 33

Compensation is not guaranteed to restore the exact previous Business State.

Invariant 34

Irreversible Actions require appropriate risk and Policy treatment.

Invariant 35

Long-running Workflows must support durable state and resumability where required.

Invariant 36

Resuming a Workflow may require revalidation of stale Preconditions and authorization.

Invariant 37

Workflow completion requires satisfaction of defined completion conditions.

Invariant 38

The last successful API response does not necessarily establish Workflow success.

Invariant 39

Noema may be authoritative for Workflow and execution state without becoming authoritative for enterprise Business State.

Invariant 40

Workflow history must preserve consequential state transitions and execution evidence.

Invariant 41

The technical execution identity may differ from the originating User or Principal and must remain attributable.

Invariant 42

Tenant, organizational, legal, and environment boundaries must remain intact across Workflow Steps.

Invariant 43

A Workflow must not become a mechanism for privilege escalation or authorization bypass.

Invariant 44

Workflow execution should use the minimum data required by each Step.

Invariant 45

When external state cannot be established, the Workflow must preserve uncertainty rather than manufacture certainty.

⸻

88. Final Definition

A Workflow is Noema’s structured representation of a multi-step execution journey through which an executable Intent is transformed into coordinated Actions, decisions, human interventions, and verified Outcomes.

The fundamental relationship is:

USER / PRINCIPAL
       │
       ▼
     INTENT
       │
       ▼
 INTENT RESOLUTION
       │
       ▼
     WORKFLOW
       │
       ├───────────────┐
       ▼               ▼
    POLICY           TRUST
       │               │
       └───────┬───────┘
               ▼
            ACTION
               │
               ▼
          EXECUTION
               │
        ┌──────┴──────┐
        ▼             ▼
     OUTCOME       EVIDENCE
        │             │
        └──────┬──────┘
               ▼
          NEXT STEP
               │
               ▼
          WORKFLOW
               │
               ▼
       VERIFIED OUTCOME

A more complete execution journey is:

Intent
   ↓
Resolution
   ↓
Workflow Planning
   ↓
Validation
   ↓
Trust / Policy
   ↓
Action
   ↓
Execution
   ↓
Verification
   ↓
Next Step
   │
   ├── Retry
   ├── Wait
   ├── Clarify
   ├── Escalate
   ├── Compensate
   └── Continue
   ↓
Workflow Completion

The architectural rule is:

Noema owns the coordination and execution journey of a Workflow, while enterprise systems remain authoritative for the Business State that the Workflow acts upon. A Workflow may plan, coordinate, pause, retry, compensate, and recover, but it must never manufacture certainty about enterprise state or silently redefine the Intent it was created to fulfill.