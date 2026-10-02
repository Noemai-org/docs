Execution Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/execution-contract.md

⸻

1. Definition

An Execution Contract is the explicit contract governing how an authorized Noema Action is executed, observed, transitioned, verified, recovered, and ultimately resolved.

An Execution Contract answers:

“Under what deterministic rules does Noema execute an Action, track its progress, handle uncertainty or failure, and establish the resulting Outcome?”

The Execution Contract sits between the Action Contract and the enterprise execution boundary.

Intent
   │
   ▼
Trust
   │
   ▼
Action Contract
   │
   ▼
Execution Contract
   │
   ▼
Enterprise Capability
   │
   ▼
Enterprise State

The Execution Contract governs the execution journey.

It does not define enterprise Business State itself.

⸻

2. Purpose

The purpose of the Execution Contract is to establish deterministic execution semantics.

It defines:

* execution identity
* Action binding
* authorization binding
* execution state
* state transitions
* attempts
* preconditions
* timeouts
* retries
* idempotency
* verification
* postconditions
* Events
* Evidence
* Outcomes
* failure handling
* recovery
* reconciliation
* compensation
* intervention
* deadlines
* concurrency
* auditability

This prevents execution behavior from being implicitly determined by model output, application-specific conventions, or transport behavior.

⸻

3. Core Principle

An Execution is a controlled state-transition process.

It is not simply:

Action → API Call → Response

Instead:

Action
   ↓
Execution
   ↓
Preconditions
   ↓
Attempt
   ↓
Enterprise Interaction
   ↓
Observation
   ↓
Verification / Reconciliation
   ↓
Postconditions
   ↓
Outcome

Every consequential transition must have explicit semantics.

⸻

4. Execution Identity

Every Execution must have a stable unique identifier.

Example:

execution_id:
exec_01J...

The identifier allows Noema to correlate:

* Intent
* Intent version
* Action
* Action Contract version
* Execution
* Attempts
* Events
* Evidence
* State Reconciliation
* Outcome
* Interventions

An Execution ID must remain stable throughout the Execution lifecycle.

⸻

5. Execution and Action

An Execution is an instance of an Action.

Action:
retrieve_account_balance
Execution:
exec_123

The Action Contract defines what the Action means.

The Execution Contract defines how a particular invocation of that Action proceeds.

Action Contract
      ↓
Action Semantics
Execution Contract
      ↓
Execution Semantics

The Execution Contract must not redefine the semantic meaning, allowed effects, or required inputs of the Action.

⸻

6. Execution and Intent

An Execution originates from an admitted and resolved Intent where the execution path is derived from Intent.

Conceptually:

Source of Intent
      ↓
Intent Object
      ↓
Resolution
      ↓
Trust
      ↓
Action
      ↓
Execution

The Execution must preserve the relationship to the originating Intent and its immutable version where required for auditability, reconstruction, and causal traceability.

If the Intent changes materially, the resulting execution semantics must not silently mutate. A new Intent version or new execution path must be created according to the relevant Contract rules.

⸻

7. Execution Admission

Execution is not admitted merely because a model proposed an Action.

Before consequential execution, Noema must establish at least:

Intent
   ↓
Hard Schema Validation
   ↓
Context
   ↓
State Reconciliation
   ↓
Trust
   ↓
Action Contract
   ↓
Execution Contract

The model may assist with interpretation and proposal.

It must not directly create execution authority, modify an Action Contract, invent a Capability, or bypass validation and Trust.

⸻

8. Execution Authorization

An Execution must not begin merely because an Action was identified.

The required Trust decision must authorize execution.

Intent
   ↓
Resolution
   ↓
Trust
   ├── REJECT
   ├── CLARIFY
   ├── ESCALATE
   └── EXECUTE
             ↓
         Execution

Execution therefore represents an authorized attempt to perform an Action, not merely a model-generated proposal.

Authorization must be bound to the resolved actor, Action, target Resource, applicable scope, relevant Policy, and execution conditions.

⸻

9. Execution State

Execution State describes where an Execution currently stands.

A canonical state model may include:

CREATED
AUTHORIZED
PRECONDITION_CHECK
READY
RUNNING
WAITING
VERIFYING
RECONCILING
RETRYING
SUCCEEDED
FAILED
UNKNOWN
CANCELLED
ESCALATED

Not every Action requires every state.

The permitted states and transitions must be defined by the Execution Contract.

Execution State is Noema execution-domain state. It is not enterprise Business State.

⸻

10. State Machine

Conceptually:

CREATED
   ↓
AUTHORIZED
   ↓
PRECONDITION_CHECK
   ↓
READY
   ↓
RUNNING
   ↓
VERIFYING
   ├── SUCCEEDED
   ├── FAILED
   └── UNKNOWN

Asynchronous execution may introduce:

RUNNING
   ↓
WAITING
   ↓
EVENT RECEIVED
   ↓
VERIFYING

Uncertain execution may introduce:

UNKNOWN
   ↓
RECONCILING
   ├── SUCCEEDED
   ├── FAILED
   └── ESCALATED

Retry may introduce:

FAILED
   ↓
RETRYING
   ↓
RUNNING

The state machine must not permit arbitrary transitions.

⸻

11. Deterministic State Transitions

Execution State transitions must be deterministic.

For example:

RUNNING → SUCCEEDED

should occur only when the Contract’s success and verification conditions have been satisfied.

The model must not decide:

“This response probably means success.”

Instead:

Observation
    ↓
Evidence / State Reconciliation
    ↓
Contract Rules
    ↓
State Transition

Consequential state transitions must be derived from defined semantics, not model confidence.

⸻

12. Terminal and Non-Terminal States

Terminal states represent an Execution for which no further execution transition is expected under the current lifecycle.

Typical terminal states include:

SUCCEEDED
FAILED
CANCELLED
ESCALATED

UNKNOWN requires special treatment.

UNKNOWN means the truth of the execution has not been established. It may persist while reconciliation is possible, or terminate through an explicit escalation or other Contract-defined resolution.

UNKNOWN must never be silently interpreted as success or failure.

⸻

13. UNKNOWN State

UNKNOWN is a first-class execution state.

Example:

Request sent
     ↓
Connection lost
     ↓
No response
     ↓
UNKNOWN

Noema must not infer:

UNKNOWN → FAILED

or:

UNKNOWN → SUCCEEDED

without sufficient Evidence or authoritative State Reconciliation.

Instead:

UNKNOWN
   ↓
Reconcile
   ├── SUCCEEDED
   ├── FAILED
   └── ESCALATE

UNKNOWN preserves epistemic uncertainty rather than manufacturing certainty.

⸻

14. Execution Attempt

An Execution may contain one or more Attempts.

Execution
   ├── Attempt 1
   ├── Attempt 2
   └── Attempt 3

An Attempt represents a concrete effort to invoke an enterprise Capability or perform a defined execution step.

Each Attempt should have its own identity and timestamps.

⸻

15. Attempt Identity

Conceptually:

attempt_id
execution_id
attempt_number
started_at
completed_at
request_identity
result
failure

Attempts must remain distinguishable from the overall Execution.

Execution ≠ Attempt

An Execution describes the overall lifecycle.

An Attempt describes one concrete effort.

⸻

16. Preconditions

Execution must validate required Preconditions before invoking the enterprise Capability.

Execution
   ↓
Preconditions
   ├── satisfied → continue
   └── unsatisfied → stop / re-evaluate

Preconditions should be evaluated against appropriate authoritative enterprise information and the relevant Context.

Examples:

* account exists
* customer identity is resolved
* target Resource is resolved
* Resource is eligible
* required technical authorization exists
* required Policy conditions are satisfied
* required enterprise state is current

⸻

17. Preconditions and Resolved Target

Consequential execution must have a resolved execution target.

A target such as:

“Tunde’s account”

is not sufficient where multiple Resources could match.

Before execution:

Actor
   ↓
Action
   ↓
Target Resource
   ↓
Scope

must be resolved to the degree required by the Action Contract.

Material target ambiguity must prevent execution and produce the appropriate CLARIFY, ESCALATE, or REJECT path rather than allowing execution against the most likely Resource.

⸻

18. Preconditions and Timing

A Precondition may be true when planning begins and false when execution begins.

Planning Time
     ↓
Precondition = TRUE
Execution Time
     ↓
Precondition = FALSE

Consequential Preconditions should therefore be evaluated at the appropriate point defined by the Execution Contract.

Planning-time validation does not automatically satisfy execution-time validation.

⸻

19. Preconditions and Freshness

Preconditions may require freshness guarantees.

Example:

account.balance >= $1,000

A stale value may be insufficient for a consequential Action.

The Execution Contract should identify when fresh authoritative data is required.

Freshness is claim- and action-specific. There is no universal freshness threshold applicable to every execution.

⸻

20. Execution Start

Execution begins only after the required admission conditions are satisfied:

Intent resolved
      ↓
Hard schema validation passed
      ↓
Actor / Action / Target resolved
      ↓
Required Context available
      ↓
State reconciled where required
      ↓
Trust decision permits execution
      ↓
Action Contract validated
      ↓
Preconditions satisfied
      ↓
Execution

Execution must not skip an earlier gate merely because a later component believes execution is safe.

⸻

21. Invocation

An Execution invokes an enterprise Capability through an Integration boundary.

Noema
  ↓
Action Contract
  ↓
Enterprise Capability
  ↓
Integration / Adapter
  ↓
Enterprise System

The Execution Contract should not depend on a specific transport unless transport behavior affects execution semantics.

Adapters translate canonical execution semantics into provider-specific protocols. They do not decide whether an Action should execute.

⸻

22. Request Identity

Consequential enterprise requests should carry sufficient identity to support:

* idempotency
* correlation
* audit
* reconciliation
* duplicate detection

Example:

execution_id
attempt_id
idempotency_key

The exact fields depend on the relevant Integration and enterprise guarantees.

⸻

23. Idempotency

Idempotency is critical when retrying consequential operations.

Example:

Execution
   ↓
Attempt 1
   ↓
Request sent
   ↓
Timeout

Noema cannot safely assume the enterprise system did not process the request.

A retry must therefore use an appropriate idempotency mechanism where supported, or perform reconciliation before repeating an operation whose duplicate effect would be unsafe.

Idempotency semantics belong to the Action, Capability, Integration, and Execution Contract as applicable. They must not be assumed universally.

⸻

24. Timeout

A timeout means Noema did not receive the expected response within the defined period.

It does not necessarily mean:

operation failed

Example:

Request
   ↓
Enterprise System
   ↓
Processing
   ↓
No response before timeout

The correct resulting state may be:

UNKNOWN

rather than:

FAILED

Timeout classification must preserve the possibility that the enterprise operation completed.

⸻

25. Retry

Retries are governed by explicit Policy and Contract rules.

A retry may depend on:

* failure class
* Action semantics
* idempotency
* attempt count
* backoff
* time budget
* enterprise guarantees
* current enterprise state
* verification results

Noema must not blindly retry every failure.

⸻

26. Retry Safety

A retry is safe only when the Contract establishes that repeating the operation cannot create an unintended duplicate effect.

For example:

retrieve_account_balance

may generally be safely retried.

A consequential mutation may require:

idempotency key
+
enterprise deduplication

or:

reconciliation
+
verification

before retry.

⸻

27. Retryable Failures

Failures may be classified as:

TRANSIENT
PERMANENT
UNKNOWN
POLICY_BLOCKED
VALIDATION_FAILURE
AUTHORIZATION_FAILURE

Only explicitly retryable conditions should automatically trigger another Attempt.

UNKNOWN should generally require verification or reconciliation before another consequential attempt.

⸻

28. Backoff

Retries should follow defined timing semantics.

Example:

Attempt 1
   ↓
wait
   ↓
Attempt 2
   ↓
wait longer
   ↓
Attempt 3

Backoff prevents Noema from amplifying enterprise instability.

Backoff does not by itself establish retry safety.

⸻

29. Retry Budget

Execution should have bounded retry behavior.

A Retry Budget may define:

* maximum attempts
* maximum elapsed time
* maximum retry delay
* maximum reconciliation window

Example:

max_attempts = 3
max_execution_time = 30s

Once the budget is exhausted, the Execution transitions according to deterministic Policy.

⸻

30. Failure Classification

Failures should be classified rather than treated as a single generic error.

Examples:

NETWORK_FAILURE
TIMEOUT
VALIDATION_FAILURE
AUTHENTICATION_FAILURE
AUTHORIZATION_FAILURE
NOT_FOUND
CONFLICT
RATE_LIMITED
DEPENDENCY_FAILURE
PROVIDER_REJECTION
UNKNOWN_OUTCOME

Classification determines recovery behavior.

A transport failure classification must not automatically imply a business failure classification.

⸻

31. Failure vs Unknown

These states must remain distinct.

FAILED means sufficient Evidence establishes that the Action did not succeed.

UNKNOWN means Noema cannot yet establish whether the Action succeeded.

Therefore:

No Response
      ≠
Confirmed Failure

This distinction is required for safe retry and recovery.

⸻

32. Postconditions

Postconditions establish whether the expected effect or result of an Action has actually been established.

Action
   ↓
Enterprise System
   ↓
Postcondition Verification

Example:

Expected:
complaint exists
Observed:
complaint_id = C-123

The Execution may transition to SUCCEEDED when the required verification conditions are satisfied.

⸻

33. Postcondition Verification

A successful transport response is not necessarily a successful business outcome.

HTTP 200
   ≠
Business Success

Where required, Noema must verify the relevant enterprise State, Event, or other authoritative Evidence.

Verification requirements are defined by the Action and Execution Contracts.

⸻

34. Outcome

Outcome describes what has been established about the Execution.

Examples may include:

SUCCEEDED
FAILED
UNKNOWN
CANCELLED
ESCALATED

Outcome is not simply the latest Execution State.

The Outcome must be derived from defined Evidence, verification rules, authoritative enterprise State where applicable, and Contract semantics.

It must not be generated from model interpretation alone.

⸻

35. Outcome vs Enterprise State

An Execution Outcome and enterprise Business State represent different domains.

Noema Execution Outcome
          ≠
Enterprise Business State

For example:

Outcome:
complaint_created
Enterprise State:
complaint.status = OPEN

Noema may establish an execution Outcome based on evidence that an enterprise state changed. It does not thereby become the owner of that enterprise state.

⸻

36. Outcome vs Response

A Response is a transport- or provider-level observation.

An Outcome is an execution-level conclusion.

Response
   ↓
Normalization
   ↓
Evidence
   ↓
Verification / Reconciliation
   ↓
Outcome

Therefore:

Response ≠ Outcome

The model must not collapse these layers.

⸻

37. Events

An Execution may consume or produce Events.

Example:

Action
   ↓
Execution
   ↓
Enterprise Event
   ↓
Evidence
   ↓
Verification

The Event Contract governs Event semantics.

The Execution Contract governs how a valid Event may affect Execution State.

An Event does not automatically establish current enterprise State or authorize another Action.

⸻

38. Asynchronous Execution

An Execution may remain active while waiting for an Event.

RUNNING
   ↓
WAITING
   ↓
Event
   ↓
VERIFYING
   ↓
SUCCEEDED

The Event must contain sufficient identity, correlation, scope, timing, and semantic guarantees to safely associate it with the Execution.

If the Event is insufficient to establish the required fact, Noema must reconcile against an authoritative source.

⸻

39. Execution Context

Execution may require Context containing:

* principal
* tenant
* organization
* Resource identifiers
* enterprise identifiers
* relevant canonical data
* permissions
* Policy
* previous observations
* deadlines
* environment
* execution-specific constraints

Only Context permitted and required by the relevant Contracts should be available to the Execution.

⸻

40. Execution Context Is Not Business State

Noema may maintain execution state such as:

execution.status
attempt.count
trust.decision
verification.status

These do not replace enterprise state such as:

account.status
transaction.status
customer.status

The enterprise remains authoritative for its Business State.

⸻

41. Enterprise State and State Reconciliation

State Reconciliation is a first-class execution mechanism.

Execution may require Noema to reconcile observations from:

* enterprise Systems of Record
* Events
* provider responses
* multiple enterprise systems
* prior execution attempts

Conceptually:

Observations
     ↓
State Reconciliation
     ↓
Current Enterprise State
     ↓
Verification
     ↓
Execution Decision / Outcome

Reconciliation does not create a shadow System of Record.

Its purpose is to establish the best supported current state required for safe execution and verification.

⸻

42. Execution and System of Record

The enterprise System of Record remains authoritative for enterprise Business State.

Noema may be authoritative for its execution-domain state, including:

execution.status
execution.outcome
attempt.history
trust.decision
verification.status

The enterprise may remain authoritative for:

account.status
payment.status
transaction.status

This boundary must remain explicit.

⸻

43. Execution and Trust

Trust determines whether execution is permitted.

Execution determines how an authorized Action proceeds.

Trust
  ↓
EXECUTE
  ↓
Execution

Execution must not reinterpret a rejected, clarification-required, or escalated Trust decision as authorization.

⸻

44. Trust During Execution

Trust conditions may need to be reevaluated if execution conditions materially change.

Examples:

* permissions changed
* Resource state changed
* risk increased
* required Context became stale
* Policy version changed
* target resolution changed
* execution deadline changed

The Execution Contract should define when re-evaluation is required.

A Trust decision must not be treated as permanently valid if the conditions on which it depended have materially changed.

⸻

45. Technical, Policy, and Business Authorization

Execution must preserve the distinction between different forms of authorization.

Technical authorization

Whether Noema or the Integration has the technical credential or permission required to invoke an operation.

Policy authorization

Whether Noema’s applicable Policy permits the execution.

Business authorization

Whether the enterprise’s business rules and current authoritative state permit the requested operation.

These are related but not interchangeable.

Technical Authorization
        +
Policy Authorization
        +
Business Authorization
        ↓
Execution Eligibility

Noema must not treat successful API authentication as proof that an Action is business-authorized.

⸻

46. Intervention

Some Executions require intervention.

Example:

Execution
   ↓
Ambiguous or unresolved enterprise state
   ↓
ESCALATED
   ↓
Authorized intervention
   ↓
Resume / Cancel / Reject

Intervention must be an explicit state transition.

It must not be represented as an implicit model decision.

Where an intervention changes the Intent, target, authority, or execution conditions materially, the resulting change must be captured explicitly rather than silently mutating the existing execution semantics.

⸻

47. Cancellation

An Execution may be cancellable.

Cancellation semantics must distinguish:

not yet started
currently running
already submitted
completed
unknown

A cancellation request does not necessarily mean the enterprise operation was successfully cancelled.

If cancellation itself is an enterprise operation, it must pass through an authorized Capability and its own Action/Execution semantics.

⸻

48. Compensation

Compensation is different from cancellation.

Cancellation attempts to prevent or stop an operation.

Compensation attempts to correct an already completed operation.

Action A
   ↓
Completed
   ↓
Compensation Action

Compensation must use authorized enterprise Capabilities.

Noema must not directly mutate enterprise Business State to compensate for an Action.

Compensation must not be assumed to restore the exact prior state unless the enterprise semantics explicitly guarantee that property.

⸻

49. Partial Execution

Compound workflows may partially execute.

Example:

Action A → SUCCEEDED
Action B → FAILED

The overall workflow must preserve the individual Execution outcomes.

Noema must not collapse:

partial success

into:

success

without explicit aggregation semantics.

⸻

50. Compound Execution

A compound Intent may create multiple Executions.

Intent
 ├── Action A
 │     └── Execution A
 │
 └── Action B
       └── Execution B

Each Execution retains its own:

* identity
* Intent version relationship
* state
* attempts
* Evidence
* Outcome

The parent Workflow or Task may aggregate these without destroying their individual semantics.

⸻

51. Dependency Between Executions

Execution B may depend on Execution A.

Execution A
    ↓
Outcome
    ↓
Precondition
    ↓
Execution B

Execution B must not start unless its dependency conditions are satisfied.

An Outcome may establish only the conditions explicitly supported by its Evidence. It must not be treated as broader proof than its Contract defines.

⸻

52. Execution Ordering

Execution ordering should be explicit where semantics require it.

A → B → C

does not mean:

A, B, C

may execute concurrently.

The Execution Contract should define dependency and ordering constraints.

⸻

53. Execution Deadlines and SLA Constraints

An Execution may have a deadline or service-level constraint.

Example:

deadline:
2026-09-01T20:00:00

Timing constraints may govern:

* execution start
* retries
* waiting
* reconciliation
* intervention
* completion

After a deadline is reached, the Execution transitions according to deterministic Policy.

A deadline does not by itself establish that an enterprise operation failed.

⸻

54. Execution Lease

Long-running Executions may require a lease or ownership mechanism.

This prevents multiple workers from simultaneously believing they own the same Execution.

Conceptually:

Execution
   ↓
Lease
   ↓
Worker

Lease expiry must produce deterministic recovery behavior.

A lease is an execution coordination mechanism. It does not change the semantic authority of the Execution or enterprise state.

⸻

55. Concurrency

The same Execution must not be processed concurrently in a way that creates conflicting state transitions or duplicate consequential effects.

Noema should enforce appropriate concurrency control.

Examples:

* optimistic locking
* execution version
* state transition guards
* leases
* idempotency

Concurrency control must apply to both execution-state mutation and consequential enterprise invocation where necessary.

⸻

56. Execution Version

An Execution may carry a version.

Example:

execution_version = 7

A state transition can require:

current_version = expected_version

This prevents stale workers from overwriting newer Execution State.

Execution versioning is distinct from:

* Intent version
* Action Contract version
* Execution Contract version
* Enterprise State version

The relevant versions must be retained when necessary to reconstruct execution semantics.

⸻

57. Recovery

If Noema crashes during execution:

RUNNING
   ↓
process failure

the system must reconstruct the Execution from durable state.

Recovery should determine:

* last known state
* active Attempt
* request identity
* known Events
* available Evidence
* relevant Context
* applicable Contract versions
* Trust decision
* retry eligibility
* reconciliation requirement

⸻

58. Recovery Must Not Guess

After a crash, Noema may not know whether the enterprise operation completed.

For example:

Request sent
   ↓
Noema crashes
   ↓
Restart

Noema must not assume:

FAILED

or:

SUCCEEDED

without sufficient Evidence.

It should preserve or enter:

UNKNOWN

and reconcile where necessary.

⸻

59. Reconciliation

Reconciliation determines the actual enterprise condition relevant to an uncertain execution.

UNKNOWN
   ↓
Query authoritative System of Record
   ↓
Observe Canonical State
   ↓
Verify Postcondition
   ↓
Resolve Execution State / Outcome

Reconciliation may require multiple observations when the enterprise state is distributed across systems.

Conflicting observations must remain explicit rather than being resolved through majority vote or model preference.

⸻

60. Execution Evidence

An Execution should retain Evidence relevant to its state transitions.

Examples:

* API response
* Event
* canonical Resource state
* permission result
* Precondition evaluation
* Postcondition evaluation
* State Reconciliation result
* human intervention
* provider acknowledgement

Each consequential transition should be explainable through its Evidence and the Contract rules that interpreted that Evidence.

Evidence is not identical to enterprise State or Outcome.

⸻

61. Fact Status

Execution may depend on facts whose status must be explicit.

A fact may be:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

Evidence
Context
Enterprise State
Execution State
Outcome

For example:

Evidence:
provider response received
Fact:
transaction completed
Fact Status:
UNVERIFIED

until authoritative State Reconciliation or another sufficient verification mechanism establishes the fact.

Execution must not treat Evidence presence alone as proof that every derived fact is verified.

⸻

62. Execution Provenance

Execution provenance should allow Noema to reconstruct:

what Source of Intent initiated the Intent
what Intent version was admitted
what Action was selected
which Action Contract version applied
which Trust decision authorized it
which actor and target were resolved
which Context was used
which enterprise state was reconciled
which Attempt occurred
which Capability was invoked
which Events were received
which Evidence was observed
which verification rules were applied
why the Outcome was established

This forms part of Noema’s causal audit trail.

⸻

63. Auditability

For consequential Executions, Noema should preserve:

* execution_id
* Intent ID and version
* Action ID and Contract version
* Execution Contract version
* Trust decision
* resolved actor and target
* relevant Context reference
* Preconditions
* Attempts
* request identities
* responses
* Events
* Evidence
* Fact Status where relevant
* State Reconciliation
* state transitions
* failures
* retries
* interventions
* postconditions
* Outcome
* timestamps

Auditability means reconstructing the causal basis of consequential execution.

It does not require exposing private model chain-of-thought.

⸻

64. Execution Observability

Operational telemetry may include:

* latency
* attempt count
* failure rate
* retry count
* queue delay
* verification latency
* reconciliation latency
* unknown rate
* escalation rate

Observability data should remain distinct from authoritative execution state.

Metrics ≠ Execution State

Telemetry may describe execution behavior without establishing business truth.

⸻

65. Execution Logging

Logs should support operational diagnosis without unnecessarily duplicating sensitive enterprise data.

The Contract should respect:

* data minimization
* privacy
* security classification
* retention Policy
* tenant isolation

Sensitive payloads should not automatically be written into logs.

Logs are not a substitute for structured causal audit records.

⸻

66. Execution and Data Boundaries

Execution should access only the data required to perform and verify the Action.

Example:

Account Inquiry

may require:

account_id
account.status
account.balance

It should not automatically access unrelated enterprise data.

Data access must be bounded by purpose, scope, Capability, Context Contract, Policy, and applicable enterprise authorization.

⸻

67. Credential Isolation

The model must not receive credentials required to execute enterprise Actions.

The execution boundary should be:

Model
   ↓
Intent / Proposal
   ↓
Noema Trust + Contracts
   ↓
Execution Controller
   ↓
Credentialed Integration
   ↓
Enterprise System

Credentials, connection secrets, signing material, and privileged provider access remain outside model control.

A model-generated request must never become an executable enterprise operation merely because it contains plausible parameters.

⸻

68. Execution and Permissions

Permission checks should occur against the appropriate authority.

A principal being authenticated does not imply:

authorized_for_action

Execution must respect:

principal
tenant
organization
resource
operation
policy
environment

Technical authorization, Policy authorization, and business authorization must not be conflated.

⸻

69. Execution and Organizational Boundaries

An Execution must preserve organizational boundaries.

Example:

Organization A
    ↓
Account A

must not accidentally operate on:

Organization B
    ↓
Account B

even if identifiers or names appear similar.

Resolved Resource identity and scope must therefore be part of consequential execution binding.

⸻

70. Execution and Environment

Executions must be bound to an environment.

Examples:

production
staging
development

A production Execution must never accidentally invoke a staging Capability.

Environment must therefore be part of the execution boundary where relevant.

⸻

71. Execution Contract Model

Conceptually:

ExecutionContract {
    execution_type
    allowed_states
    transitions
    preconditions
    postconditions
    timeout_policy
    retry_policy
    idempotency_policy
    verification_policy
    reconciliation_policy
    recovery_policy
    intervention_policy
    cancellation_policy
    compensation_policy
    deadline_policy
    concurrency_policy
    event_bindings
    audit_requirements
}

This is a semantic model, not necessarily a literal database schema.

⸻

72. Execution Model

Conceptually:

Execution {
    execution_id
    intent_id
    intent_version
    action_id
    action_contract_version
    execution_contract_version
    state
    version
    principal
    tenant
    organization
    target_resource
    environment
    created_at
    started_at
    completed_at
    deadline
    attempts
    precondition_results
    postcondition_results
    evidence
    reconciliation_results
    failures
    outcome
}

⸻

73. Execution Relationships

Execution
   │
   ├── instantiates → Action
   ├── originated_from → Intent
   ├── authorized_by → Trust Decision
   ├── binds_to → Resolved Actor / Target
   ├── uses → Context
   ├── evaluates → Preconditions
   ├── contains → Attempts
   ├── receives → Events
   ├── records → Evidence
   ├── reconciles → Enterprise State
   ├── verifies → Postconditions
   ├── produces → Outcome
   ├── may_require → Intervention
   └── may_require → Compensation

⸻

74. Execution Lifecycle

A canonical lifecycle may be:

CREATED
   ↓
AUTHORIZED
   ↓
PRECONDITION_CHECK
   ↓
READY
   ↓
RUNNING
   ↓
VERIFYING
   ├── SUCCEEDED
   ├── FAILED
   └── UNKNOWN

Additional paths may include:

RUNNING
   ↓
WAITING
   ↓
VERIFYING
RUNNING
   ↓
FAILED
   ↓
RETRYING
   ↓
RUNNING
UNKNOWN
   ↓
RECONCILING
   ↓
SUCCEEDED / FAILED / ESCALATED

All transitions remain Contract- and Policy-governed.

⸻

75. Execution Contract and Action Contract

The distinction is fundamental.

Action Contract

Defines:

* what the Action means
* what inputs it accepts
* what Capability it invokes or represents
* what effects are permitted
* what Preconditions and Postconditions are semantically relevant
* what verification requirements apply

Execution Contract

Defines:

* how the Action is performed
* how Attempts are managed
* how Execution State transitions occur
* how timeouts are handled
* how retries are governed
* how uncertainty is reconciled
* how Outcomes are established
* how recovery occurs

The Execution Contract must not redefine the meaning of the Action.

⸻

76. Execution Contract and Event Contract

The Event Contract defines Event semantics.

The Execution Contract defines how Events may affect an Execution.

Event Contract
      ↓
Event meaning
      ↓
Evidence / Reconciliation
      ↓
Execution Contract
      ↓
Execution transition

An Event does not bypass Execution rules.

Event receipt does not automatically establish an Outcome or authorize subsequent execution.

⸻

77. Execution Contract and Context Contract

The Context Contract defines what Context may be supplied to an Execution.

Context Contract
      ↓
Permitted Context
      ↓
Execution Contract
      ↓
Execution

Execution must not implicitly acquire arbitrary enterprise data.

Context availability does not automatically mean that every Context item is authoritative for a consequential claim.

Where required, the Execution Contract must rely on Fact Status, Evidence, and State Reconciliation to establish whether Context is sufficient for execution.

⸻

78. Execution Contract and Trust Contract

Trust determines whether execution is permitted.

Execution Contract determines how permitted execution proceeds.

Trust
   ↓
Authorization / EXECUTE
   ↓
Execution Contract
   ↓
Execution

A valid Execution Contract cannot override a Trust rejection.

If the conditions underlying the Trust decision materially change, execution must follow the defined re-evaluation rules rather than continuing under stale authority.

⸻

79. Execution Contract and Enterprise Business State

The Execution Contract governs Noema’s execution lifecycle.

The enterprise remains authoritative for Business State.

Execution State
     ≠
Business State

For example:

Noema:
execution = SUCCEEDED
Enterprise:
account.status = ACTIVE

These represent different domains of truth.

⸻

80. Execution Contract and Determinism

Execution is where Noema’s deterministic architecture becomes operational.

The probabilistic layer may help determine:

what the Source of Intent means

and may propose:

which Action may satisfy it

But after the hard validation and Trust boundary:

Contract
   +
Policy
   +
Evidence
   +
Fact Status
   +
State Reconciliation
   +
authoritative enterprise State

must determine the execution path.

The system must not rely on:

* model intuition
* model probability
* best guess

to transition consequential Execution State.

⸻

81. Execution Contract and Ambiguity

If required execution information remains ambiguous:

Execution
   ↓
Required actor / action / target / fact ambiguous
   ↓
CLARIFY / ESCALATE / REJECT

Noema must not proceed simply because the model has selected the most likely interpretation.

Ambiguity remains an execution constraint until deterministically resolved.

⸻

82. Execution Contract and Human Confirmation

Policy may require explicit confirmation before certain Executions.

Example:

Action identified
   ↓
Trust
   ↓
Confirmation required
   ↓
Authorized confirmation
   ↓
Execution

Confirmation is distinct from authorization.

Where confirmation is consequential, it must be recorded as Execution Evidence and bound to the relevant Intent, actor, Action, target, and execution conditions.

Confirmation must not be used to bypass Policy, authorization, or capability restrictions.

⸻

83. Execution Contract and Bounded Planning

A Planner may determine an execution sequence within the bounds established by Trust, Action Contracts, Capabilities, Policies, and execution constraints.

The Planner must not:

* create authority
* invent Capabilities
* create arbitrary Actions
* modify Action Contracts
* bypass Trust
* bypass schema validation
* bypass Preconditions
* expand target scope
* access arbitrary enterprise data
* redefine Outcomes

Trust
   ↓
Allowed Action / Capability Space
   ↓
Planner
   ↓
Execution Contract
   ↓
Execution

Planning is therefore bounded by the canonical execution model.

⸻

84. Execution Contract and Structural Safety

Execution safety must not depend on the model behaving correctly.

The architecture must structurally prevent:

Model
   ↓
Arbitrary Enterprise Operation

Instead:

Model
   ↓
Intent / Candidate Action
   ↓
Hard Schema Validation
   ↓
Trust
   ↓
Registered Capability
   ↓
Action Contract
   ↓
Execution Contract
   ↓
Credentialed Integration
   ↓
Enterprise System

Only explicitly registered and governed Capabilities may cross the execution boundary.

Prohibited Capabilities must be unavailable to the execution path rather than merely discouraged through prompting.

⸻

85. Execution Contract and Commercial Scope

The Execution Contract is independent of the commercial wedge.

For read-oriented operations:

* account inquiry
* statement retrieval
* transaction search
* spending summary
* complaint logging

the same execution principles apply:

authorize
   ↓
validate
   ↓
reconcile where required
   ↓
invoke
   ↓
observe
   ↓
verify
   ↓
record

The Contract therefore supports the Phase 1 POC without requiring Noema to begin with high-risk financial mutations.

Deep read-only investigation may still be consequential because it can expose protected information or establish facts on which later actions depend. Read-only therefore does not mean semantically shallow or risk-free.

⸻

86. Execution Contract Invariants

Invariant 1

Every consequential Execution must have a stable identity.

Invariant 2

Every Execution must be bound to a defined Action.

Invariant 3

Execution must only begin after the required Trust decision permits it.

Invariant 4

Consequential execution must follow the required hard validation and admission gates.

Invariant 5

Execution State transitions must be deterministic.

Invariant 6

Only defined state transitions are permitted.

Invariant 7

Preconditions must be evaluated before consequential invocation.

Invariant 8

Precondition validity must satisfy the freshness requirements of the Action.

Invariant 9

Consequential execution must bind to a sufficiently resolved actor, Action, target Resource, and scope.

Invariant 10

An Attempt is distinct from the overall Execution.

Invariant 11

Retries must be governed by explicit Policy and Contract rules.

Invariant 12

A retry must not create unintended duplicate effects.

Invariant 13

Timeout does not automatically mean failure.

Invariant 14

Unknown execution conditions must remain explicitly represented as UNKNOWN.

Invariant 15

Noema must not convert UNKNOWN into success or failure without sufficient Evidence or State Reconciliation.

Invariant 16

Successful transport responses do not automatically establish successful business outcomes.

Invariant 17

Consequential Postconditions must be verified according to the required verification Policy.

Invariant 18

Events may affect Execution State only according to defined Event and Execution Contract semantics.

Invariant 19

Event receipt does not automatically authorize subsequent execution.

Invariant 20

Execution State must remain distinct from enterprise Business State.

Invariant 21

Noema must not create shadow canonical Business State to simplify execution.

Invariant 22

Recovery after process failure must preserve uncertainty where enterprise outcome cannot be established.

Invariant 23

Reconciliation must be available where execution outcome can become uncertain.

Invariant 24

Fact Status must remain distinct from Evidence, Context, State, and Outcome.

Invariant 25

Compound Executions must preserve the individual state and Outcome of each Action.

Invariant 26

Partial success must not be silently represented as total success.

Invariant 27

Intervention must be represented as an explicit execution transition.

Invariant 28

Cancellation does not automatically establish that the enterprise operation was cancelled.

Invariant 29

Compensation must use authorized enterprise Capabilities.

Invariant 30

Execution must respect tenant, organizational, legal, permission, and environment boundaries.

Invariant 31

Execution must access only the data necessary for its defined purpose.

Invariant 32

Execution provenance must be sufficient to reconstruct consequential execution decisions.

Invariant 33

The model must not independently determine consequential Execution State transitions.

Invariant 34

Execution deadlines and retry budgets must be bounded where applicable.

Invariant 35

Concurrent workers must not create conflicting state transitions or unintended duplicate consequential effects for the same Execution.

Invariant 36

An Execution Contract must not redefine the semantic meaning of the Action it executes.

Invariant 37

Noema’s Execution State and Outcome are authoritative within Noema’s execution domain, while enterprise Business State remains authoritative within the enterprise domain.

Invariant 38

When execution truth cannot be established, Noema must preserve uncertainty rather than manufacture certainty.

Invariant 39

Technical authorization, Policy authorization, and business authorization must not be treated as interchangeable.

Invariant 40

A Planner must not create authority, invent Capabilities, modify Contracts, or bypass Trust and execution constraints.

Invariant 41

Model-generated proposals must not directly cross the enterprise execution boundary.

Invariant 42

Credentials and privileged enterprise access must remain outside model control.

Invariant 43

A material change to execution conditions must invalidate or trigger reevaluation of affected Trust, Preconditions, or execution decisions according to Contract rules.

Invariant 44

A deadline or timeout must not itself manufacture a business Outcome.

⸻

87. Final Definition

An Execution Contract is the authoritative specification governing the lifecycle of an authorized Noema Action from initiation through verified resolution.

It defines:

WHAT
is being executed
UNDER WHICH
Action Contract
FOR WHICH
resolved actor, target, and scope
WITH WHICH
authorization
AGAINST WHICH
Preconditions
THROUGH WHICH
enterprise Capability
WITH WHICH
Attempt and retry semantics
USING WHICH
verification and reconciliation rules
UNDER WHICH
failure, recovery, and compensation rules
UNTIL WHICH
Execution State and Outcome are established

The fundamental relationship is:

SOURCE OF INTENT
   │
   ▼
INTENT OBJECT
   │
   ▼
HARD SCHEMA VALIDATION
   │
   ▼
CONTEXT
   │
   ▼
STATE RECONCILIATION
   │
   ▼
TRUST
   │
   ▼
ACTION CONTRACT
   │
   ▼
EXECUTION CONTRACT
   │
   ▼
PRECONDITIONS
   │
   ▼
ATTEMPT
   │
   ▼
ENTERPRISE CAPABILITY
   │
   ├──────────────► EVENT
   │                 │
   │                 ▼
   │              EVIDENCE
   │                 │
   ▼                 │
OBSERVATION ◄────────┘
   │
   ▼
VERIFICATION / RECONCILIATION
   │
   ▼
POSTCONDITIONS
   │
   ▼
EXECUTION STATE / OUTCOME

And the architectural rule is:

Noema must treat Execution as a deterministic, Contract-governed state machine. The probabilistic layer may interpret Intent and propose Actions, but once execution crosses the admission and Trust boundary, every consequential transition must be governed by Contract, Policy, Evidence, Fact Status, State Reconciliation, and authoritative enterprise state—not by model intuition or probability.