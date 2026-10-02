> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Workflow Model

Status: Foundational
Version: 0.2
Domain: Product
Canonical Path: product/workflow-model.md

⸻

1. Definition

A Workflow is Noema’s durable, stateful coordination model for transforming an executable Intent into a sequence or graph of validated Actions, decisions, waits, human interventions, verifications, and Outcomes.

The Workflow Model answers:

“How does Noema coordinate multiple executable steps over time while preserving Intent, authority, policy, enterprise boundaries, and execution truth?”

A Workflow is not merely a list of Actions.

It is a controlled execution structure that may contain:

* Intent
* Intent references
* Actions
* Preconditions
* Postconditions
* Decisions
* Policy evaluation
* Trust evaluation
* Evidence requirements
* Dependencies
* Sequential execution
* Parallel execution
* Branching
* Joins
* Wait states
* Events
* Human intervention
* Approvals
* Clarification
* Retries
* Idempotency
* Compensation
* Reconciliation
* Cancellation
* Timeouts
* Recovery
* Completion conditions
* Execution history

Conceptually:

Executable Intent
       │
       ▼
Workflow Plan
       │
       ▼
Validation
       │
       ▼
Workflow Instance
       │
       ├── Action
       ├── Decision
       ├── Wait
       ├── Human Intervention
       ├── Verification
       └── Compensation
               │
               ▼
            Outcome

⸻

2. Purpose

The purpose of the Workflow Model is to provide a durable semantic representation for multi-step enterprise execution.

Many enterprise outcomes cannot be achieved through a single Action.

For example:

Intent:
"Close my account."
Workflow:
Resolve Account
      ↓
Check Balance
      ↓
Check Pending Transactions
      ↓
Resolve Required Settlement
      ↓
Close Account
      ↓
Verify Closure

The Workflow defines how these Steps relate, what conditions permit progression, what happens when execution is uncertain, and when the overall Intent can be considered satisfied.

⸻

3. Core Architectural Principle

A Workflow is a coordination and execution construct.

It is not automatically the authoritative owner of the enterprise Business State being modified.

Enterprise Systems
       │
       ▼
Business State
       ▲
       │
   Integrations
       ▲
       │
    Actions
       ▲
       │
   Workflow
       ▲
       │
Executable Intent

Noema may be authoritative for:

* Intent state
* Workflow state
* Step state
* execution records
* trust decisions
* intervention state
* workflow outcomes

The enterprise remains authoritative for enterprise Business State unless an explicit architecture delegates otherwise.

Therefore:

Workflow State is not Enterprise Business State.

⸻

4. Workflow vs Action

An Action represents an executable operation.

A Workflow coordinates multiple operations and control decisions.

Example:

Action:
refund_payment

versus:

Workflow:
refund_and_close_account

which may contain:

resolve_payment
validate_refund
refund_payment
verify_refund
validate_closure
close_account
verify_closure

Therefore:

Workflow ≠ Action

A Workflow may contain one Action, but the existence of a Workflow does not eliminate the semantic identity of that Action.

⸻

5. Workflow vs Intent

An Intent represents the desired outcome of the initiating Principal.

A Workflow represents an executable strategy for accomplishing that Intent.

Intent
   ↓
Intent Resolution
   ↓
Executable Intent
   ↓
Workflow Planning
   ↓
Validated Workflow
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

The Workflow is therefore derived from the executable Intent and the capabilities, enterprise state, policies, and constraints relevant to execution.

⸻

6. Workflow Is Not Intent

Natural language must not be transformed directly into an executable Workflow merely because a model can produce a plausible sequence of Actions.

The correct relationship is:

Natural Language
       ↓
Interaction
       ↓
Intent
       ↓
Intent Resolution
       ↓
Executable Intent
       ↓
Workflow Planning
       ↓
Validation
       ↓
Execution

Not:

Natural Language
       ↓
Workflow
       ↓
Execution

Material ambiguity in the Intent must be resolved before consequential Workflow execution.

⸻

7. Executable Intent as Workflow Anchor

An Executable Intent defines what Noema has sufficient grounds to attempt.

The Workflow operationalizes that Intent.

Executable Intent
       │
       ▼
Workflow
       │
       ├── Step A
       ├── Step B
       └── Step C

Every consequential Workflow must preserve a reference to the Intent from which it was derived.

A Workflow must not silently expand, narrow, or redefine the Intent merely because an alternative execution path is convenient.

⸻

8. Workflow Identity

Every Workflow Instance must have a stable identity.

Conceptually:

WorkflowInstance {
    workflow_id
    intent_id
    definition_id
    definition_version
    state
    steps
    created_at
    updated_at
}

The identifier enables Noema to associate:

* Intent
* Workflow Definition
* Workflow Instance
* Steps
* Actions
* executions
* decisions
* evidence
* interventions
* retries
* compensation
* reconciliation
* outcomes
* audit history

⸻

9. Workflow Definition vs Workflow Instance

A Workflow Definition describes reusable execution semantics.

A Workflow Instance represents one concrete execution journey.

Workflow Definition
refund_and_close_account:v2
          │
          ├── Workflow Instance WF-1001
          ├── Workflow Instance WF-1002
          └── Workflow Instance WF-1003

The Definition describes possible behavior.

The Instance contains execution-specific state such as:

* Intent
* participants
* resources
* parameters
* resolved references
* policy context
* authorization context
* evidence
* decisions
* Step state
* execution results
* interventions
* timestamps
* Outcomes

Therefore:

Workflow Definition ≠ Workflow Instance

⸻

10. Workflow Definition

A Workflow Definition may specify:

* trigger conditions
* required Intent type
* Steps
* Action references
* dependencies
* transition conditions
* branching
* joins
* Preconditions
* Postconditions
* approval requirements
* human intervention requirements
* retry semantics
* timeout semantics
* compensation semantics
* reconciliation requirements
* completion criteria
* failure propagation
* cancellation behavior

A Definition describes permitted execution structure.

It does not establish that any particular execution occurred.

⸻

11. Workflow Instance

A Workflow Instance represents a concrete execution journey.

Example:

Workflow Definition:
refund_and_close_account:v2
Workflow Instance:
WF-8421
Intent:
INT-4421
Requester:
Principal P-123
Payment:
PAY-123
Account:
ACC-456

The Instance maintains the actual state of this particular execution.

⸻

12. Workflow Plan vs Workflow Instance

A Workflow Plan is a candidate execution strategy.

A Workflow Instance is the controlled execution state created after the relevant validation boundary.

Intent
  ↓
Planning
  ↓
Candidate Workflow Plan
  ↓
Capability Validation
  ↓
Policy Validation
  ↓
Authority / Trust Validation
  ↓
Workflow Instance
  ↓
Execution

A plan is not evidence of execution.

A model-generated plan must never be treated as proof that Actions occurred.

⸻

13. Workflow State

A Workflow may contain states such as:

CREATED
RESOLVING
PLANNING
VALIDATING
READY
RUNNING
WAITING
AWAITING_HUMAN
BLOCKED
COMPENSATING
RECONCILING
SUCCEEDED
PARTIALLY_COMPLETED
FAILED
CANCELLED
UNKNOWN

Exact states may vary by implementation.

State semantics must remain explicit.

Workflow state must represent established execution facts and control conditions rather than model confidence.

⸻

14. Workflow State Is Not Model Confidence

A model may estimate:

“The refund probably succeeded.”

That is not equivalent to:

Workflow Step:
SUCCEEDED

A Workflow transition must be based on established evidence and defined execution semantics.

Conceptually:

Model Interpretation
       ↓
Candidate Decision
       ↓
Noema Validation
       ↓
Execution / Evidence
       ↓
Deterministic State Transition

The model may propose.

The Workflow runtime establishes state.

⸻

15. Workflow as a State Machine

Workflow execution should be representable as a state-transition system.

Conceptually:

Current State
      +
Event / Execution Result
      +
Policy
      +
Evidence
      +
Preconditions
      ↓
Valid Transition
      ↓
New State

Invalid transitions must be rejected.

For example:

CANCELLED → RUNNING

should not occur unless an explicit semantic transition permits it.

Likewise:

UNKNOWN → SUCCEEDED

requires evidence establishing success.

⸻

16. Workflow Steps

A Workflow consists of explicit Steps.

A Step may represent:

* Action
* Decision
* Verification
* Wait
* Human Intervention
* Approval
* Clarification
* Compensation
* Reconciliation

Example:

Step 1 → Resolve Payment
Step 2 → Validate Refund
Step 3 → Refund Payment
Step 4 → Verify Refund
Step 5 → Close Account
Step 6 → Verify Closure

Each Step must have explicit semantics.

⸻

17. Step Identity

Every consequential Step should have a stable identity.

Conceptually:

Step {
    step_id
    workflow_id
    type
    state
    dependencies
    action_reference
}

This allows Noema to establish:

* which Step is executing
* which Step completed
* which Step failed
* which Step is blocked
* which Step requires intervention
* which Step is eligible to run

⸻

18. Step Dependencies

Steps may depend on other Steps.

Resolve Payment
      ↓
Refund Payment
      ↓
Verify Refund
      ↓
Close Account

A dependent Step must not execute until its required dependency conditions are satisfied.

Dependencies must be explicit rather than inferred solely from the order in which a model generated Steps.

⸻

19. Sequential Execution

A Workflow may execute sequentially:

A
↓
B
↓
C
↓
D

Sequential execution is appropriate where later Steps depend on earlier outcomes or state.

The sequence itself does not establish success. Each transition remains subject to its own execution semantics.

⸻

20. Parallel Execution

Independent Steps may execute concurrently.

          ┌── Check Subscription
          │
Intent ───┼── Check Balance
          │
          └── Check Pending Transactions

Parallelism is valid only when it does not violate:

* dependencies
* resource constraints
* authorization
* Policy
* data consistency
* enterprise concurrency semantics
* Action preconditions

Noema must not use parallelism merely because two Actions appear syntactically independent.

⸻

21. Join Semantics

Parallel branches may converge through a Join.

        ┌── A ──┐
Start ──┼── B ──┼── Join
        └── C ──┘

The Join defines the conditions required for continuation.

For example:

A = SUCCESS
B = SUCCESS
C = SUCCESS

may be required.

Alternatively, Policy may establish that C is non-critical.

Join semantics must be explicit.

⸻

22. Conditional Branching

A Workflow may branch according to deterministic conditions.

Check Balance
      │
      ├── balance = 0
      │       ↓
      │   Close Account
      │
      └── balance > 0
              ↓
          Settlement

Branch conditions that depend on enterprise Business State must be grounded in appropriate authoritative data.

A model may propose a branch.

The Workflow runtime must validate the branch condition against available evidence and Policy.

⸻

23. Workflow Decisions

A Workflow Decision determines which valid execution path should be followed.

A decision may depend on:

* resolved Intent
* Context
* Canonical Data
* Evidence
* Policy
* Action outcomes
* resource state
* previous Steps
* current authorization
* risk requirements

Consequential decisions should be explainable and reproducible from the relevant execution record.

⸻

24. Planning vs Decision vs Execution

These are distinct concepts.

Planning:

What execution strategy could satisfy the Intent?

Decision:

Which permitted path applies given current evidence and Policy?

Execution:

What Action was actually attempted and what happened?

Therefore:

Planning
   ↓
Candidate Plan
   ↓
Validation
   ↓
Decision
   ↓
Action
   ↓
Execution
   ↓
Outcome

Noema must not collapse these into a single model inference.

⸻

25. Workflow and Capability Discovery

Workflow planning must operate over capabilities that actually exist.

Conceptually:

Enterprise Capability / Action Registry
              ↓
          Available Actions
              ↓
          Workflow Planning
              ↓
        Capability Validation
              ↓
             Execute

A model must not invent an Action merely because it would be useful.

Every executable Step must resolve to an available and authorized capability.

⸻

26. Workflow and Action Contracts

Each executable Action should expose a machine-checkable contract containing, as applicable:

* Action identity
* input schema
* output schema
* target Resource type
* required authority
* Preconditions
* Postconditions
* side-effect semantics
* idempotency semantics
* reversibility
* timeout behavior
* error semantics
* required evidence
* data requirements
* Policy constraints

The Workflow should compose these contracts rather than reconstructing Action semantics from natural language.

⸻

27. Workflow and Bounded Autonomy

A Workflow provides a boundary within which autonomous planning and execution may operate.

Autonomy must remain constrained by:

* executable capabilities
* Action contracts
* resolved Intent
* authorization
* Policy
* Trust
* Preconditions
* resource scope
* risk
* execution state

The model must not acquire new authority merely by generating a new Workflow Step.

Therefore:

Planning capability does not imply execution authority.

⸻

28. Workflow and Trust

Trust may be evaluated multiple times during a Workflow.

Workflow
   ↓
Action A
   ↓
Trust Evaluation
   ↓
Execute
   ↓
Action B
   ↓
Trust Evaluation
   ↓
Execute

Trust should not automatically be treated as permanently valid for the entire Workflow.

A later Step may involve:

* a different Resource
* a different Principal
* greater risk
* changed Business State
* different scope
* stronger authorization requirements
* new Policy

and therefore require reevaluation.

⸻

29. Workflow and Authorization

Authorization must be evaluated in the context of the actual Action.

Conceptually:

Principal
   +
Action
   +
Resource
   +
Scope
   +
Policy
   +
Current Authority
   ↓
Authorization Decision

The existence of an authorized Workflow does not mean every Action inside that Workflow is automatically authorized.

Authorization must remain aligned with the specific consequential operation.

⸻

30. Workflow and Policy

Policy constrains the Workflow.

Policy may define:

* permitted Actions
* required approvals
* risk thresholds
* required authentication
* sequencing
* retry limits
* timeout behavior
* compensation
* data requirements
* human intervention
* separation of duties
* completion requirements
* cancellation rules
* expiration

Therefore:

Workflow
   ↓
Policy Evaluation
   ↓
Permitted Execution Path

Policy is a constraint on execution, not merely documentation for the model.

⸻

31. Workflow and Separation of Duties

Where Policy requires distinct participants, a Workflow must preserve the distinction.

Example:

Requester
    ↓
Intent
    ↓
Approver
    ↓
Execution

The Workflow must not silently satisfy an approval requirement by having the same Principal perform both roles when Policy requires separation.

⸻

32. Workflow and Preconditions

Consequential Actions may have Preconditions.

Example:

Action:
refund_payment
Preconditions:
payment.status = CAPTURED
refund.amount <= refundable_amount

The Workflow must establish required Preconditions before execution.

A previous observation may satisfy a Precondition only if its freshness and provenance remain valid under the relevant Action and Policy.

⸻

33. Workflow and Postconditions

An Action may have Postconditions.

Example:

Action:
refund_payment
Expected Postcondition:
payment.status = REFUNDED

Where authoritative verification is required, an API response alone does not necessarily establish the Postcondition.

The Workflow may therefore require:

Action
  ↓
Execution Outcome
  ↓
Authoritative Verification
  ↓
Postcondition Established

⸻

34. Workflow and Canonical Data

Workflow decisions may depend on enterprise Canonical Data.

Workflow
   ↓
Read Enterprise State
   ↓
Canonical Data
   ↓
Decision

Noema must preserve the authority boundary of the underlying System of Record.

Workflow Context must not silently become Canonical Data merely because it is stored by Noema.

⸻

35. Workflow and Context

Workflow execution may require Context such as:

* originating Principal
* acting Principal
* execution Principal
* Intent
* resolved Resources
* organizational scope
* tenant
* authorization context
* current enterprise state
* previous Step outcomes
* Policy
* relevant Evidence
* execution history

Context should be purpose-bound and Step-scoped where possible.

⸻

36. Workflow and Evidence

Evidence establishes facts relevant to Workflow decisions.

Example:

Evidence:
payment.status = CAPTURED
Source:
Payment System
Observed:
T1

Evidence should preserve sufficient provenance to establish:

* source
* observation time
* relevant Resource
* value
* retrieval method
* freshness where applicable

Evidence supports decisions.

Evidence is not automatically equivalent to Business State.

⸻

37. Workflow and Grounding

Where a Workflow depends on enterprise state, Noema should distinguish:

Claim
  ↓
Evidence
  ↓
Source Authority
  ↓
Grounded Fact

A model-generated statement such as:

“The account appears closed.”

must not be treated as equivalent to an authoritative enterprise observation:

Account System:
status = CLOSED
observed_at = T2

Grounding requirements depend on the consequence and Policy of the Step.

⸻

38. Workflow and Events

Events may drive Workflow transitions.

Example:

Payment Submitted
      ↓
Event
      ↓
Workflow
      ↓
Resume / Transition

An Event establishes that an event was received.

It does not necessarily establish the current canonical state of the Resource.

Where current state matters, Noema may need to query the authoritative System of Record.

⸻

39. Event Ordering and Deduplication

Event-driven Workflows must account for:

* duplicate events
* delayed events
* out-of-order events
* missing events
* replayed events

Workflow transitions must therefore be idempotent and based on explicit event semantics.

Receiving an event twice must not silently execute a consequential Action twice.

⸻

40. Event-Driven Workflow

A Workflow may wait for an external event.

Submit Payment
      ↓
WAITING
      ↓
payment.completed
      ↓
Verify Payment
      ↓
Resume

Waiting is a legitimate Workflow state.

The Workflow must not simulate completion because an expected event is likely to occur.

⸻

41. Workflow and Human Intervention

Human intervention is a first-class Workflow capability.

Examples:

* clarification
* approval
* manual review
* exception handling
* conflict resolution
* recovery decision
* authorization escalation

Conceptually:

Workflow
   ↓
Human Required
   ↓
AWAITING_HUMAN
   ↓
Human Decision
   ↓
Validation
   ↓
Workflow Resumes

The intervention must be attributable to the relevant Principal.

⸻

42. Workflow and Clarification

If material Intent ambiguity prevents safe execution:

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
Revalidation
   ↓
Workflow Resumes

Clarification must not be treated as permission to invent missing information.

A clarification response may modify the Intent and therefore may require renewed planning, authorization, and Trust evaluation.

⸻

43. Workflow and Approval

Some Steps require approval.

Action
   ↓
Approval Required
   ↓
Approver
   ↓
Approval
   ↓
Revalidation
   ↓
Execute

Approval should be bound to the relevant:

* Workflow
* Intent
* Action
* Resource
* parameters
* scope
* approving Principal
* Policy version

An approval does not replace authorization.

⸻

44. Workflow and Confirmation

Confirmation may satisfy a Policy requirement.

User:
"Confirm transfer of $20,000."
Confirmation
      ↓
Bound to Intent / Action
      ↓
Authorization
      ↓
Trust
      ↓
Execution

Confirmation is contextual.

A generic historical “yes” must not be reused for a different Action.

⸻

45. Workflow and Compensation

A Workflow may partially succeed.

Example:

A → SUCCESS
B → SUCCESS
C → FAILED

Policy may require compensation:

C FAILED
   ↓
Compensation
   ↓
Reverse / Correct A and/or B

Compensation is itself an Action and must therefore remain subject to:

* authorization
* Action contracts
* Preconditions
* Policy
* Trust
* enterprise state
* execution semantics

⸻

46. Workflow Is Not a Database Transaction

A Workflow may span:

* multiple systems
* long time periods
* asynchronous events
* human approvals
* irreversible operations

Therefore a Workflow is not generally equivalent to a distributed database transaction.

It may instead require:

* compensation
* reconciliation
* retries
* idempotency
* explicit intermediate states
* durable execution
* human intervention

⸻

47. Workflow and Irreversible Actions

Some Actions cannot be fully reversed.

Examples:

* sending an external message
* deleting a resource
* releasing funds
* submitting a regulatory filing

A Workflow must represent irreversibility explicitly.

The existence of a later corrective Action does not mean the original Action was reversible.

⸻

48. Workflow and Failure

A Step may fail without the entire Workflow failing.

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

Failure propagation must be defined by Workflow semantics and Policy.

⸻

49. Workflow and Unknown State

A Workflow may enter UNKNOWN when Noema cannot establish whether an external Action completed.

Example:

Request sent
    ↓
Connection lost
    ↓
Outcome UNKNOWN

Noema must not convert:

UNKNOWN → FAILED

or:

UNKNOWN → SUCCESS

without evidence.

Unknown is a meaningful execution state, not an error message to be hidden.

⸻

50. Workflow and Reconciliation

When external execution state is uncertain, reconciliation may query authoritative enterprise state.

Refund = UNKNOWN
      ↓
Query Payment System
      ↓
Payment System:
Refund = COMPLETED
      ↓
Step = SUCCEEDED

Reconciliation prevents duplicate execution caused by treating uncertainty as failure.

Reconciliation must itself have explicit semantics and evidence.

⸻

51. Workflow and Retry

Retry is permitted only when defined execution semantics allow it.

A retry may require:

* transient failure classification
* idempotency
* deduplication
* Policy permission
* retry limits
* current authorization
* current Preconditions

A timeout alone does not necessarily justify retrying a consequential Action.

⸻

52. Workflow and Idempotency

Consequential Actions should have explicit idempotency semantics where possible.

Example:

workflow_id = WF-123
step_id = refund_payment
idempotency_key = WF-123:refund_payment

If a network failure occurs, Noema should be able to determine whether another attempt could duplicate the enterprise operation.

Idempotency belongs to Action and integration semantics and must not be assumed merely because an Action is represented as a Workflow Step.

⸻

53. Workflow and Side Effects

A Workflow must distinguish between:

* planning
* observation
* validation
* execution
* side effects

A model generating:

refund_payment(...)

does not mean the refund occurred.

The enterprise side effect occurs only through the authorized execution boundary.

Candidate Action
      ↓
Validation
      ↓
Authorized Execution
      ↓
Enterprise Side Effect
      ↓
Observed Outcome

⸻

54. Workflow and Concurrency

Multiple Workflow Instances may act on the same Resource.

Workflow A
    ↓
Account 123
Workflow B
    ↓
Account 123

Noema must respect enterprise concurrency semantics.

A state observed by Workflow A must not automatically be assumed unchanged when Workflow A later executes another Step.

⸻

55. Workflow and State Changes

Enterprise state may change between Steps.

Step 1:
balance = $10,000
External Change
Step 2:
balance = $2,000

Consequential Preconditions must be revalidated where required.

Earlier Context does not automatically become current truth.

⸻

56. Workflow and Staleness

Workflow Context can become stale.

Freshness requirements should be determined by:

* Action
* Resource
* risk
* Policy
* enterprise semantics

For high-consequence Actions, Noema may require fresh observation immediately before execution.

⸻

57. Workflow and Optimistic Concurrency

A Workflow may use enterprise resource versions.

Example:

Account:
version = 42

Action expects:

version = 42

Enterprise system responds:

version = 43

The Workflow may need to:

* re-read
* revalidate
* re-plan
* request clarification
* obtain renewed approval
* abort

according to Policy.

⸻

58. Workflow and Resource Locking

Where enterprise systems provide locking, leases, reservations, or concurrency controls, Noema should use those mechanisms rather than treating local Workflow state as sufficient.

A Workflow record stating:

Account = available

does not itself lock that Account.

⸻

59. Workflow and Dynamic Planning

Some Workflows may be dynamically constructed.

Intent
   ↓
Available Capabilities
   ↓
Current Enterprise State
   ↓
Policy
   ↓
Candidate Workflow
   ↓
Validation
   ↓
Execution

Dynamic planning is permitted within defined autonomy boundaries.

Dynamic planning must not create:

* new authority
* nonexistent capabilities
* unauthorized resources
* unsupported Action parameters
* Policy exceptions

⸻

60. Workflow and Deterministic Replanning

A Workflow may become invalid because enterprise conditions change.

Original Plan
      ↓
Enterprise State Changes
      ↓
Plan Invalid
      ↓
Replanning
      ↓
Validation
      ↓
New Execution Path

Replanning must preserve the resolved Intent.

If the new plan materially changes the consequence of execution, renewed Trust, authorization, confirmation, or approval may be required.

⸻

61. Workflow Mutation

Workflow structure or execution state may change after execution begins.

Examples:

* external state changes
* Action failure
* Policy change
* human intervention
* external event
* resource unavailability

Material changes must be explicit and auditable.

Noema must preserve the prior execution history rather than silently rewriting it.

⸻

62. Workflow Versioning

Workflow Definitions must be versioned when execution semantics change.

Example:

refund_workflow:v1
refund_workflow:v2

An existing Workflow Instance must retain the Definition version relevant to its execution.

A new Definition must not retroactively reinterpret historical execution.

⸻

63. Policy Versioning

Policy may change during the lifecycle of a Workflow.

Where necessary, the execution record should preserve:

workflow_version
policy_version
authorization_context
trust_decision

This enables reconstruction of why a particular execution path was permitted at the relevant time.

⸻

64. Workflow and Authorization Revocation

Authorization may change after Intent creation.

Example:

Intent Created
      ↓
User Role Revoked
      ↓
Execution Attempted

Intent creation does not automatically grant permanent execution authority.

The Workflow must evaluate current authority according to Policy.

⸻

65. Workflow and Approval Expiry

Approvals and confirmations may expire.

Example:

Approval
   ↓
24-hour validity
   ↓
Expired
   ↓
Revalidation / New Approval

Noema must not reuse expired approval or confirmation merely because the same Workflow remains active.

⸻

66. Workflow and Long-Running Execution

A Workflow may run for:

* seconds
* minutes
* hours
* days

Long-running execution therefore requires durable state.

The Workflow must be resumable where required.

Session termination must not automatically terminate the execution journey.

⸻

67. Workflow and Resumption

A paused Workflow may resume when its blocking condition is satisfied.

WAITING_FOR_APPROVAL
        ↓
Approval Received
        ↓
Revalidation
        ↓
RESUMING
        ↓
Next Step

Resumption should revalidate any state, authority, evidence, or Preconditions that may have become stale.

⸻

68. Workflow and Cancellation

A User or authorized Principal may request cancellation.

Cancellation must be evaluated against:

* current Workflow state
* current Step state
* Action semantics
* Policy
* reversibility
* enterprise capabilities

Cancellation is not automatically rollback.

RUNNING
   ↓
Cancellation Request
   ↓
Policy Evaluation
   ↓
Cancel / Reject / Continue

An already completed irreversible Action cannot necessarily be cancelled.

⸻

69. Workflow and Timeout

Timeouts may apply to:

* individual Steps
* external responses
* human intervention
* Workflow execution

A timeout does not necessarily establish external failure.

Example:

API Timeout
    ↓
Outcome UNKNOWN
    ↓
Reconciliation

The timeout semantics must be defined by the relevant Action and Workflow contract.

⸻

70. Workflow and Compensation Boundaries

Compensation does not guarantee restoration of the exact prior enterprise state.

Example:

Charge
  ↓
Refund

does not necessarily mean the enterprise system is identical to its state before the charge.

Compensation must therefore be represented as a new authorized operation with its own outcome.

⸻

71. Workflow and Completion

A Workflow is complete only when its defined completion conditions are satisfied.

Completion may require:

Required Steps succeeded
+
Required Postconditions established
+
Required approvals completed
+
Required interventions completed
+
No unresolved blocking state

Therefore:

Last API call returned 200

does not necessarily imply:

Workflow = SUCCEEDED

⸻

72. Workflow Outcome

The Workflow Outcome describes the final established execution result.

Possible Outcomes include:

SUCCEEDED
FAILED
CANCELLED
PARTIALLY_COMPLETED
UNKNOWN

Outcome semantics must preserve the difference between:

* established facts
* incomplete execution
* uncertainty
* failure
* cancellation

⸻

73. Partial Completion

A Workflow may partially complete.

Example:

Refund:
SUCCESS
Account Closure:
FAILED

The Workflow must preserve the individual Step results.

It must not collapse meaningful partial execution into an oversimplified binary result.

⸻

74. Workflow and Enterprise Systems

A Workflow may cross multiple enterprise systems.

Example:

CRM
 ↓
Billing
 ↓
Payment
 ↓
Identity

Each Action must respect the authority boundary of the relevant System of Record.

The Workflow coordinates these systems without becoming the owner of their Business State.

⸻

75. Workflow and Enterprise Action Graph

The Enterprise Action Graph describes capabilities and relationships available to Noema.

Workflow planning may select from those capabilities.

Enterprise Action Graph
          ↓
       Planning
          ↓
        Workflow
          ↓
         Steps
          ↓
        Actions

The Workflow must not invent capabilities that do not exist in the enterprise environment.

⸻

76. Workflow and Integration

Actions execute through defined integrations.

Workflow
   ↓
Action
   ↓
Integration
   ↓
Enterprise System

The Workflow should reason primarily in terms of semantic Action contracts.

Transport details such as HTTP methods, SDK calls, queues, or vendor-specific protocols should remain encapsulated by the Integration Model.

⸻

77. Workflow and Data Minimization

Each Step should request only the data required for that Step.

For example:

refund_payment

may require:

payment_id
amount
currency
status

It should not automatically retrieve unrelated customer information.

Workflow composition must not become an excuse for unrestricted data aggregation.

⸻

78. Workflow and Security Boundaries

Every Step remains subject to relevant security controls.

A Workflow must not become a mechanism for:

* privilege escalation
* tenant crossing
* unauthorized delegation
* authorization bypass
* data leakage
* scope expansion
* identity substitution

Technical orchestration must preserve enterprise security boundaries.

⸻

79. Workflow and Tenant / Organizational Boundaries

Workflow execution must preserve:

* tenant
* organization
* business unit
* legal entity
* environment
* resource scope

boundaries.

A Workflow must not infer that because a Principal can access Resource A, the same Principal can access Resource B.

⸻

80. Workflow and User Roles

Multiple participants may occupy different roles within one Workflow.

Requester
    ↓
Intent
    ↓
Approver
    ↓
Operator
    ↓
Execution

Noema must preserve these distinctions.

The technical Execution Principal may be different from the originating User.

⸻

81. Workflow and Execution Principal

The principal initiating an Action may differ from the technical identity executing the enterprise API call.

Acting Principal:
Jane Doe
Execution Principal:
Noema Service Identity

The service identity’s technical ability to execute an API call does not establish that every User is authorized to use that capability.

The Workflow must preserve the originating Principal and relevant authorization context.

⸻

82. Workflow and Auditability

A consequential Workflow should produce an execution trail.

Intent Created
      ↓
Workflow Planned
      ↓
Workflow Validated
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
Verification
      ↓
Next Step

The record should allow Noema to establish:

* what was intended
* what was planned
* what was authorized
* what Action was attempted
* what evidence existed
* who participated
* what actually happened
* where execution stopped
* how recovery occurred

⸻

83. Workflow History

Workflow history should be append-oriented where possible.

Noema should preserve significant events such as:

* creation
* planning
* validation
* state transitions
* Step execution
* decisions
* evidence
* approvals
* confirmations
* human intervention
* retries
* compensation
* reconciliation
* cancellation
* final Outcome

Historical execution records must not be silently overwritten.

⸻

84. Workflow and Replayability

Where required for consequential operations, Noema should be able to reconstruct the execution path from durable records.

A reconstruction should preserve the relevant:

Intent
Workflow Version
Policy Version
Principal
Authorization Context
Actions
Inputs
Evidence
Events
State Transitions
Outcomes
Interventions

Replay must distinguish:

reconstructing what happened

from:

executing the Actions again.

Historical replay must never accidentally become live execution.

⸻

85. Workflow and Observability

Noema should be able to observe:

* current Workflow state
* current Step
* completed Steps
* failed Steps
* pending Steps
* blocked conditions
* required human intervention
* external dependencies
* retry count
* compensation state
* reconciliation state

Observability supports:

* operations
* debugging
* audit
* recovery
* user transparency

⸻

86. Workflow and User Experience

The User should experience the Workflow as progress toward an outcome rather than as internal infrastructure.

Example:

User:
"Close my account."
Noema:
Checking your account...
Noema:
There is a pending refund.
Noema:
The refund has completed.
Noema:
Your account has been closed.

The underlying Workflow may contain many Steps that do not need to be exposed individually.

⸻

87. Workflow Transparency

Noema should expose enough state to establish meaningful progress.

Examples:

* Resolving
* Waiting for approval
* Executing
* Waiting for external system
* Verifying
* Requires clarification
* Requires intervention
* Completed
* Failed

Transparency must not expose unnecessary implementation details or sensitive enterprise information.

⸻

88. Workflow and Notifications

A Workflow may generate notifications for significant transitions.

Examples:

* Approval Required
* Clarification Required
* Action Completed
* Human Intervention Required
* Workflow Failed
* Workflow Completed

Notifications must be derived from established Workflow state.

A notification must not claim an enterprise outcome that has not been established.

⸻

89. Workflow and Recovery

Recovery brings an interrupted or failed Workflow into a valid recoverable or terminal state.

Possible paths include:

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

Recovery behavior must be explicit.

⸻

90. Workflow and Intent Preservation

The Intent remains the semantic anchor of the Workflow.

Example:

Intent:
"Get my account closed."
Plan A:
Refund → Close
Plan B:
Settlement → Close
Plan C:
Manual Review → Close

The Workflow may change while preserving the same Intent.

Therefore:

Workflow is an execution strategy, not the Intent itself.

⸻

91. Workflow and Material Intent Change

If the User materially changes the Intent:

"Close my account."
becomes:
"Actually, keep it open."

the existing Workflow may no longer be valid.

Noema must not continue executing a Workflow that no longer corresponds to the active Intent.

Material Intent change may require:

* Workflow cancellation
* replanning
* renewed authorization
* renewed Trust
* renewed confirmation
* new approval

as applicable.

⸻

92. Workflow and Compound Intent

A compound Intent may result in one composite Workflow or multiple related Workflows.

Example:

Intent:
"Refund the payment and close my account."

Possible structure:

Composite Workflow
       │
       ├── Refund Workflow
       └── Account Closure Workflow

Relationships between the Workflows must be explicit.

⸻

93. Workflow Composition

Workflows may compose when one Workflow depends on another.

Workflow A
    ↓
Workflow B
    ↓
Workflow C

Composition must preserve:

* Intent relationships
* Principal relationships
* authorization
* resource boundaries
* Policy
* failure semantics
* compensation semantics
* auditability

A parent Workflow must not automatically inherit authority that a child Workflow does not possess.

⸻

94. Workflow Nesting

A Workflow may invoke a sub-workflow.

Example:

Account Closure
      │
      ├── Refund Workflow
      ├── Subscription Workflow
      └── Identity Workflow

Each sub-workflow may maintain independent execution state while remaining associated with the parent.

Parent-child relationships must be explicit and auditable.

⸻

95. Workflow Atomicity Boundaries

A Workflow must explicitly distinguish atomic operations from non-atomic coordination.

Example:

Payment System:
Atomic refund operation
Cross-System Workflow:
Non-atomic

Noema must not represent cross-system execution as atomic when the underlying systems cannot guarantee atomicity.

⸻

96. Workflow and Risk Escalation

Risk may increase as a Workflow progresses.

Example:

Step 1:
Read Account
Step 2:
Modify Account
Step 3:
Transfer Funds

Later Steps may require stronger controls.

Trust, authorization, confirmation, approval, and human intervention must therefore remain Step-sensitive.

⸻

97. Workflow and Human-in-the-Loop

Human participation is not an exceptional failure mode.

It is a first-class Workflow capability.

Workflow
   ↓
Human Required
   ↓
WAITING
   ↓
Human Decision
   ↓
Validation
   ↓
Resume

The Workflow must preserve:

* who intervened
* why intervention was required
* what decision was made
* what Intent or Action the decision applied to
* what happened afterward

⸻

98. Workflow and External Uncertainty

External uncertainty must remain explicit.

Examples:

Timeout
Connection Lost
Duplicate Event
Missing Callback

do not automatically imply:

FAILED

or:

SUCCEEDED

Noema must preserve uncertainty until sufficient evidence establishes the relevant state.

⸻

99. Workflow and Reconciliation Before Re-execution

When an Action may have produced a side effect but its outcome is unknown, reconciliation should generally precede another consequential attempt where duplicate execution is possible.

Action Attempt
      ↓
Outcome UNKNOWN
      ↓
Reconcile
      ↓
Determine Actual State
      │
      ├── Completed → Continue
      │
      ├── Not Completed → Retry if permitted
      │
      └── Still Unknown → Escalate / Wait

This prevents uncertainty from becoming duplicate execution.

⸻

100. Workflow and Deterministic Execution Boundaries

The model may assist with:

* candidate planning
* candidate branching
* candidate parameter selection
* interpretation
* replanning

The execution runtime must establish:

* valid capability
* valid Action contract
* current authorization
* required Policy
* Preconditions
* Trust
* execution
* state transitions

Therefore:

Model
   ↓
Candidate
   ↓
Validation Boundary
   ↓
Deterministic Execution Boundary
   ↓
Enterprise Side Effect

The model does not directly own Workflow state.

⸻

101. Workflow and Noema System of Record

Noema may be authoritative for:

Intent State
Workflow State
Step State
Execution Record
Trust Decision
Intervention State
Workflow Outcome

Enterprise Systems of Record remain authoritative for:

Account
Payment
Customer
Inventory
Subscription
Employee
Other Enterprise Business State

Therefore:

Noema System of Record
        │
        ├── Intent
        ├── Workflow
        ├── Trust
        ├── Execution
        └── Intervention
Enterprise Systems of Record
        │
        ├── Account
        ├── Payment
        ├── Customer
        └── Inventory

⸻

102. Workflow and Enterprise State Discrepancy

Noema Workflow State may temporarily disagree with enterprise Business State.

Example:

Noema:
refund Step = SUCCEEDED
Payment System:
refund.status = PENDING

The discrepancy must not be hidden.

Noema must preserve the distinction between:

* Action execution result
* enterprise state
* verification result
* Workflow state

and reconcile according to the applicable semantics.

⸻

103. Workflow and Outcome Truth

A User-facing message is not itself the source of truth for execution.

For example:

Assistant:
"Your refund is complete."

must be derived from established Workflow and enterprise evidence.

Conversely:

Assistant:
"Your refund failed."

must not be stated merely because a timeout occurred when external execution remains unknown.

⸻

104. Workflow and Minimum Necessary Execution Context

A Workflow should carry only the context necessary for its execution.

It should avoid becoming a generalized container for:

* unrelated User data
* unrelated enterprise records
* unnecessary credentials
* unrelated Business State
* unnecessary historical interactions

Context should be scoped according to purpose, Action, Resource, and Policy.

⸻

105. Workflow and Credentials

Workflow state must not become a credential store.

Authentication credentials, secrets, API keys, and privileged service credentials belong to the appropriate security and integration boundaries.

The Workflow may reference the execution identity or credential context required to perform an Action without exposing or duplicating secret material.

⸻

106. Workflow and Environment Boundaries

Where an enterprise environment contains multiple environments, such as:

Development
Staging
Production

the Workflow must preserve the target environment.

A Workflow generated for one environment must not silently execute against another.

Environment is therefore part of relevant execution context.

⸻

107. Workflow and Resource Identity

Resource references used by Workflow Steps must be resolved before consequential execution.

A model-generated reference such as:

"John's account"

is not sufficient if multiple enterprise resources match.

The Workflow must operate on an explicitly resolved Resource identity.

Natural Language Reference
        ↓
Candidate Resource
        ↓
Resolution
        ↓
Authoritative Resource Identity
        ↓
Workflow Step

⸻

108. Workflow and Resource Scope

A Workflow must preserve resource scope across Steps.

If an Action is authorized for:

Account A

that authorization does not automatically extend to:

Account B

Resource identity and scope must remain explicit throughout the execution journey.

⸻

109. Workflow and Delegation

Where execution occurs under delegated authority, the Workflow should preserve:

acting_principal
delegated_principal
delegation_scope
delegation_authority

where relevant.

Delegation must not be represented as identity substitution.

The Workflow must remain able to distinguish:

who acted
for whom they acted
under what authority
what Action occurred

⸻

110. Workflow and Separation Between Observation and Mutation

Observation and mutation are different Workflow operations.

For example:

Read Account

does not itself modify enterprise state.

Where possible, Workflows should make explicit which Steps:

* observe
* validate
* decide
* mutate
* verify

This distinction improves risk control and auditability.

⸻

111. Workflow and Dry Run / Preview

Where supported by the relevant Action contract, Noema may construct a non-executing Workflow preview.

A preview may establish:

* intended Steps
* required approvals
* expected resources
* Preconditions
* potential Actions
* potential side effects

A preview must not be represented as execution.

Preview
   ≠
Execution

⸻

112. Workflow and Execution Leases

Where an Action or Workflow requires exclusive execution for a period, lease semantics may be used.

A lease must have:

* owner
* scope
* start
* expiration
* renewal semantics

Expiration of a local lease must not be confused with cancellation of an enterprise operation unless the enterprise system explicitly guarantees that behavior.

⸻

113. Workflow and Recovery After Process Failure

A Noema process may terminate while a Workflow remains active.

Durable Workflow state must therefore allow recovery.

After process recovery, Noema must determine:

* current Workflow state
* current Step
* pending executions
* unknown executions
* outstanding human interventions
* current enterprise state where required

It must not blindly repeat an Action merely because local process state was lost.

⸻

114. Workflow and Execution Attempt

A Step may have multiple execution attempts.

Conceptually:

Step
 │
 ├── Attempt 1 → UNKNOWN
 ├── Reconciliation
 └── Attempt 2 → SUCCESS

The Workflow must preserve the individual attempts rather than overwriting Attempt 1 with Attempt 2.

This distinction is necessary for auditability and recovery.

⸻

115. Workflow and Attempt Identity

Each consequential execution attempt should be independently identifiable where necessary.

Conceptually:

workflow_id
step_id
attempt_id
idempotency_key

This allows Noema to distinguish:

* one Step
* multiple attempts
* duplicate requests
* retries
* reconciliations

without collapsing them into a single event.

⸻

116. Workflow and Policy Changes During Execution

A Policy may change while a Workflow is running.

Noema must define whether the applicable Policy is:

* evaluated dynamically
* pinned for the Workflow
* pinned for individual Actions
* otherwise versioned

The chosen semantics must be explicit.

Historical execution must preserve enough Policy context to reconstruct why an Action was permitted.

⸻

117. Workflow and Intent Expiration

Some Intents may become stale or expire.

For example:

Intent:
"Transfer this amount today."

If the relevant execution window expires, the Workflow must not assume the original Intent remains executable indefinitely.

Expiration behavior is governed by Intent and Policy semantics.

⸻

118. Workflow and Confirmation Staleness

Confirmation may become stale when material execution conditions change.

Example:

User confirms transfer
       ↓
Account state changes
       ↓
Precondition changes
       ↓
Confirmation no longer sufficient
       ↓
Revalidation / Reconfirmation

Confirmation belongs to the specific Intent and Action context.

It is not a permanent property of the User.

⸻

119. Workflow and Human Decision Binding

Human decisions must be bound to the relevant execution context.

A decision such as:

"Approve"

must identify, where relevant:

* Workflow
* Step
* Action
* Resource
* parameters
* Principal
* timestamp
* applicable Policy

A generic historical decision must not be reused outside its intended scope.

⸻

120. Workflow and Outcome Verification

An execution result and a verified enterprise Outcome are related but distinct.

Action Execution
      ↓
Execution Outcome
      ↓
Verification
      ↓
Established Enterprise Outcome

The Workflow may require verification before progressing.

This is particularly important for asynchronous, eventually consistent, or externally processed Actions.

⸻

121. Workflow and Eventual Consistency

Enterprise systems may expose state asynchronously.

For example:

Action submitted
      ↓
PENDING
      ↓
External processing
      ↓
COMPLETED

The Workflow must represent intermediate state explicitly.

It must not convert:

PENDING

into:

SUCCEEDED

without the required evidence.

⸻

122. Workflow and Failure Domains

Failure should be attributed to the appropriate domain.

Possible failure domains include:

* Intent resolution
* capability resolution
* authorization
* Policy
* Action validation
* integration
* enterprise system
* network
* human intervention
* verification
* reconciliation

The Workflow should preserve the distinction rather than reducing every failure to a generic error.

⸻

123. Workflow and User-Facing Failure Semantics

User-facing communication should reflect established Workflow state.

For example:

FAILED

may support:

“The account closure could not be completed.”

Where:

UNKNOWN

may require:

“I could not yet confirm whether the closure completed.”

The product must not manufacture certainty for conversational convenience.

⸻

124. Workflow and User Experience Abstraction

Internal Workflow complexity may be greater than what the User sees.

Internal:
Resolve
→ Validate
→ Authorize
→ Execute
→ Verify
→ Reconcile
→ Continue
User:
“Closing your account…”

Abstraction is acceptable provided the User-facing state remains truthful.

⸻

125. Workflow and Audit Attribution

Consequential execution should preserve attribution for:

requested_by
acting_principal
approved_by
confirmed_by
executed_by
intervened_by

These may represent different principals.

The Workflow must not collapse them into one generic “User” field.

⸻

126. Workflow and Non-Repudiation

For high-consequence operations, the Workflow may need sufficient evidence that a particular Principal performed a particular approval or confirmation.

This may include:

* authenticated identity
* timestamp
* Intent binding
* Action binding
* Resource binding
* authorization evidence
* confirmation evidence
* Policy context

Exact requirements depend on enterprise Policy and risk.

⸻

127. Workflow and No Silent Authority Expansion

A Workflow must never acquire authority merely through composition.

For example:

Workflow A
    ↓
calls Workflow B
    ↓
Workflow B accesses Resource X

does not establish that Workflow A is authorized to access Resource X.

Authorization remains applicable to the actual Action and Resource.

⸻

128. Workflow and No Silent Capability Expansion

Dynamic planning must not turn an unavailable capability into an executable one.

If the Action Graph contains:

read_account
close_account

but does not contain:

delete_customer

a model-generated Workflow containing delete_customer is invalid.

The Workflow runtime must reject capabilities that cannot be resolved to executable contracts.

⸻

129. Workflow and Semantic Integrity

A Workflow must preserve the semantic identity of:

* Intent
* Principal
* Resource
* Action
* Policy
* Trust
* Evidence
* Execution
* Outcome

It must not collapse these into a generic “task” object.

The value of the Workflow Model depends on maintaining these distinctions.

⸻

130. Workflow Invariants

Invariant 1

A Workflow coordinates execution; it is not an Action.

Invariant 2

A Workflow is derived from an Intent and must not replace the Intent.

Invariant 3

Every consequential Workflow must remain traceable to its initiating Intent.

Invariant 4

A Workflow Plan is not evidence of execution.

Invariant 5

A Workflow Definition and Workflow Instance are distinct concepts.

Invariant 6

Every consequential Step must have explicit semantics.

Invariant 7

Step dependencies must be satisfied before dependent execution.

Invariant 8

Workflow state must be based on established execution facts, not model confidence.

Invariant 9

The model may propose Workflow structure but must not independently establish runtime execution state.

Invariant 10

Every executable Step must resolve to an available Action or explicitly defined Workflow capability.

Invariant 11

Noema must not invent enterprise capabilities.

Invariant 12

Action execution must remain subject to the relevant Action contract.

Invariant 13

Trust may require independent evaluation at different Workflow Steps.

Invariant 14

Authorization must be evaluated in the relevant Principal, Action, Resource, Scope, and Policy context.

Invariant 15

Authorization for one Step does not automatically authorize another Step.

Invariant 16

Policy constrains Workflow execution.

Invariant 17

Consequential Actions must satisfy required Preconditions.

Invariant 18

Required Postconditions must be verified according to Action and Policy semantics.

Invariant 19

Workflow Context must not silently become authoritative enterprise Business State.

Invariant 20

Evidence must preserve sufficient provenance for consequential decisions.

Invariant 21

Model-generated claims are not authoritative enterprise state.

Invariant 22

Events may drive transitions but do not necessarily establish current canonical state.

Invariant 23

Duplicate, delayed, missing, or out-of-order events must not produce unintended duplicate execution.

Invariant 24

Human intervention must be represented explicitly when required.

Invariant 25

Approval and confirmation must remain bound to their relevant execution context.

Invariant 26

Confirmation does not replace authorization.

Invariant 27

A Workflow is not equivalent to a distributed database transaction.

Invariant 28

Partial completion must remain representable.

Invariant 29

UNKNOWN must not be silently converted into SUCCESS or FAILED.

Invariant 30

Retry must respect Action idempotency, Policy, authorization, and current Preconditions.

Invariant 31

An uncertain consequential Action should be reconciled before re-execution where duplicate side effects are possible.

Invariant 32

Enterprise state may change between Workflow Steps.

Invariant 33

Stale Context must not automatically satisfy current consequential Preconditions.

Invariant 34

Workflow Definitions must be versioned when execution semantics change.

Invariant 35

Historical execution must remain reconstructable under the relevant Workflow and Policy versions.

Invariant 36

Dynamic Workflow planning must be validated before execution.

Invariant 37

Planning, decision, and execution are distinct semantic stages.

Invariant 38

Workflow mutation must be explicit and auditable.

Invariant 39

Workflow changes must not silently redefine the underlying Intent.

Invariant 40

A material Intent change may invalidate the current Workflow.

Invariant 41

Workflow composition must preserve Intent, authorization, resource, Policy, failure, compensation, and audit boundaries.

Invariant 42

A child Workflow does not automatically inherit authority from its parent.

Invariant 43

Noema must not represent cross-system execution as atomic when underlying systems cannot guarantee atomicity.

Invariant 44

Compensation is not guaranteed to restore the exact previous Business State.

Invariant 45

Irreversible Actions require explicit risk and Policy treatment.

Invariant 46

Long-running Workflows must support durable state and resumability where required.

Invariant 47

Workflow resumption may require revalidation of stale Preconditions, authority, Evidence, and Policy.

Invariant 48

Workflow completion requires satisfaction of defined completion conditions.

Invariant 49

A successful API response does not necessarily establish Workflow success.

Invariant 50

Noema may be authoritative for Workflow and execution state without becoming authoritative for enterprise Business State.

Invariant 51

Workflow history must preserve consequential state transitions, execution attempts, decisions, evidence, and interventions.

Invariant 52

The technical Execution Principal may differ from the originating Principal and must remain attributable.

Invariant 53

Tenant, organizational, legal, environment, and Resource boundaries must remain intact across Workflow Steps.

Invariant 54

A Workflow must not become a mechanism for privilege escalation or authorization bypass.

Invariant 55

Workflow Steps should use the minimum data required for their purpose.

Invariant 56

Credentials and secrets must remain outside ordinary Workflow state.

Invariant 57

Resource identity must be resolved before consequential execution.

Invariant 58

Model-generated Resource candidates are not authoritative Resource identities.

Invariant 59

Delegation must remain explicit and auditable.

Invariant 60

Requester, confirmer, approver, operator, and intervenor roles must remain distinguishable.

Invariant 61

A Workflow must distinguish observation, decision, mutation, verification, and execution.

Invariant 62

A preview or dry run must not be represented as execution.

Invariant 63

Execution attempts must remain individually reconstructable where consequential.

Invariant 64

Process failure must not cause blind re-execution of potentially completed Actions.

Invariant 65

Approval and confirmation may expire or become stale.

Invariant 66

Policy changes during execution must have explicit semantics.

Invariant 67

Intent expiration must prevent stale Intent from being silently executed where applicable.

Invariant 68

Execution Outcomes and verified enterprise Outcomes must remain distinguishable.

Invariant 69

Eventually consistent enterprise state must be represented explicitly.

Invariant 70

Failure domains should remain distinguishable where necessary for recovery and audit.

Invariant 71

User-facing Workflow communication must reflect established state rather than conversational assumptions.

Invariant 72

A Workflow must not acquire new authority through composition or dynamic planning.

Invariant 73

A Workflow must not acquire new executable capabilities through model generation.

Invariant 74

Workflow execution must preserve semantic distinctions between Intent, Principal, Resource, Action, Policy, Trust, Evidence, Execution, and Outcome.

Invariant 75

When external state cannot be established, the Workflow must preserve uncertainty rather than manufacture certainty.

⸻

131. Conceptual Workflow Model

Conceptually:

Workflow {
    workflow_id
    intent_id
    definition_id
    definition_version
    state
    participants
    context
    steps
    dependencies
    policy_context
    authorization_context
    trust_context
    evidence
    events
    execution_attempts
    interventions
    created_at
    updated_at
}

This is a semantic model, not necessarily a literal database schema.

The Workflow Model does not own:

* enterprise identity
* enterprise authorization
* enterprise Business State
* credentials
* arbitrary enterprise resources

unless explicitly delegated by architecture.

⸻

132. Conceptual Step Model

Step {
    step_id
    workflow_id
    type
    state
    dependencies
    action_reference
    resource_reference
    parameters
    preconditions
    postconditions
    policy_requirements
    authorization_requirements
    trust_requirements
    evidence_requirements
    attempts
    created_at
    updated_at
}

The exact implementation may differ, but consequential execution semantics must remain explicit.

⸻

133. Conceptual Execution Attempt

ExecutionAttempt {
    attempt_id
    workflow_id
    step_id
    execution_principal
    acting_principal
    action_reference
    idempotency_key
    started_at
    completed_at
    request
    outcome
    evidence
    error
}

Execution attempts should preserve sufficient information to distinguish:

* attempted execution
* successful execution
* failed execution
* unknown execution
* retried execution
* reconciled execution

⸻

134. Fundamental Workflow Relationship

The complete semantic relationship is:

PRINCIPAL
    │
    ▼
  INTENT
    │
    ▼
INTENT RESOLUTION
    │
    ▼
EXECUTABLE INTENT
    │
    ▼
WORKFLOW PLANNING
    │
    ▼
CANDIDATE WORKFLOW
    │
    ▼
VALIDATION
    │
    ├──────────────┐
    ▼              ▼
CAPABILITY      POLICY /
VALIDATION      AUTHORITY
    │              │
    └──────┬───────┘
           ▼
        TRUST
           │
           ▼
       WORKFLOW
           │
           ├── Decision
           │
           ├── Human Intervention
           │
           ├── Wait
           │
           └── ACTION
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
            VERIFICATION
                 │
                 ▼
             NEXT STEP
                 │
        ┌────────┼─────────┐
        ▼        ▼         ▼
      Retry     Wait    Reconcile
        │        │         │
        └────────┴─────────┘
                 │
                 ▼
          WORKFLOW STATE
                 │
                 ▼
          COMPLETION CHECK
                 │
                 ▼
        VERIFIED OUTCOME

⸻

135. Final Definition

A Workflow is Noema’s durable coordination representation for carrying an executable Intent through validated planning, policy and authority constraints, Action execution, human intervention, waiting, verification, recovery, and final Outcome.

The fundamental execution journey is:

Intent
   ↓
Resolution
   ↓
Executable Intent
   ↓
Workflow Planning
   ↓
Validation
   ↓
Policy / Authorization / Trust
   ↓
Action
   ↓
Execution
   ↓
Evidence
   ↓
Verification
   ↓
Next Step
   │
   ├── Continue
   ├── Retry
   ├── Wait
   ├── Clarify
   ├── Approve
   ├── Escalate
   ├── Reconcile
   ├── Compensate
   └── Cancel
   ↓
Workflow Completion
   ↓
Verified Outcome

The architectural rule is:

Noema owns the coordination and execution journey represented by a Workflow, while enterprise systems remain authoritative for the Business State upon which that Workflow operates. Workflow planning may be dynamic and model-assisted, but consequential execution must remain bounded by executable capabilities, Action contracts, Intent, authorization, Policy, Trust, Preconditions, evidence, and explicit state transitions. Noema must preserve uncertainty when external state cannot be established, must never manufacture enterprise truth, and must never silently expand the authority or meaning of the Intent it was created to fulfill.