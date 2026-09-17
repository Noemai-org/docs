Execution Model

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/execution-model.md

⸻

1. Definition

The Execution Model defines how Noema moves a trusted, contract-bound Action from an Action Contract to an actual execution attempt, how execution state is tracked, how uncertainty is handled, and how an Outcome is established through verification.

Execution is the point at which a permitted Action crosses the execution boundary into an Execution Consumer and potentially affects an external system.

The canonical boundary is:

Source of Intent
   ↓
Intent
   ↓
Action
   ↓
Trust
   ↓
Action Contract
   ↓
Execution
   ↓
Verification
   ↓
Outcome

⸻

2. Core Principle

Noema determines whether an Action may proceed and defines the execution boundary; the Execution Consumer performs the Action; the authoritative enterprise system establishes the resulting business state.

Noema determines:

what may happen
under what conditions
against which resolved target

The Execution Consumer determines:

how the Action is performed

The authoritative enterprise system determines:

what actually happened to enterprise Business State

Execution therefore does not make Noema the enterprise System of Record.

⸻

3. Execution Is Not Intent

An Intent expresses desired semantic meaning.

Example:

"Refund my payment."

Execution is the actual attempt to perform:

refund_payment(payment_123)

Therefore:

Intent ≠ Execution

An Intent may produce an Action and Action Contract without execution ever occurring.

⸻

4. Execution Is Not an Action

An Action describes a semantic operation:

refund_payment

An Execution represents an attempt to perform a specific Action Instance:

execution_123
    action = refund_payment
    payment = payment_123

Therefore:

Action ≠ Execution

The Action is reusable semantic definition; the Execution is a concrete occurrence.

⸻

5. Execution Is Not an Action Contract

The Action Contract defines the authorized and bounded execution boundary.

Execution represents what happened when that Contract was consumed.

Action Contract
    ↓
Execution Attempt
    ↓
Verification
    ↓
Outcome

A valid Action Contract does not guarantee successful execution.

⸻

6. Execution Is Not Outcome

Execution is the attempt.

Outcome is what execution and verification establish about the requested operation.

Example:

Execution:
Attempted to refund payment_123.
Outcome:
Refund transaction ref_456 was established.

Therefore:

Execution ≠ Outcome

An execution can exist with an UNKNOWN Outcome.

⸻

7. Execution Boundary

The canonical boundary is:

                         NOEMA
────────────────────────────────────────
Source of Intent
  ↓
Intent
  ↓
Resolution
  ↓
Hard Schema Validation / Admission
  ↓
State / Context Reconciliation
  ↓
Trust
  ↓
Action
  ↓
Action Contract
────────────────────────────────────────
                    ↓
             EXECUTION CONSUMER
                    ↓
             BUSINESS SYSTEMS
                    ↓
               VERIFICATION
────────────────────────────────────────
                    ↓
                   NOEMA

Once the Action Contract crosses the execution boundary, the consumer owns the execution mechanics.

The consumer does not acquire authority beyond the Contract.

⸻

8. Execution Consumer

An Execution Consumer is a system capable of consuming an Action Contract and attempting the corresponding Action.

Examples:

payment-service
crm-service
inventory-service
workflow-engine
database-service
notification-service

The consumer translates the canonical Action into an implementation-specific operation.

The implementation may differ across enterprises while the Action semantics remain stable.

⸻

9. Consumer Responsibilities

The consumer is responsible for:

* authenticating and validating the received Contract;
* checking Contract validity and applicability;
* validating its own integration requirements;
* binding to the specified enterprise resource;
* performing final business-state validation where required;
* enforcing consumer-side execution constraints;
* executing the Action;
* maintaining execution attempt state;
* reporting structured execution state;
* returning execution evidence;
* reporting what it can establish about the resulting Outcome.

The consumer must not expand the Contract’s scope or interpret it as permission for another Action.

⸻

10. Noema Responsibilities

Noema is responsible for:

* Intent resolution;
* Action determination;
* hard schema validation and admission;
* actor and target resolution;
* Context and State Reconciliation;
* Trust evaluation;
* policy evaluation;
* risk evaluation;
* Action Contract generation;
* execution coordination;
* execution lineage;
* verification coordination;
* Outcome interpretation;
* compensation coordination;
* audit and Operational Memory.

Noema does not become the business system merely because it coordinates execution.

⸻

11. Execution Identity

Every execution requires a unique identifier:

execution_id

Example:

execution_id:
exec_01J...

This allows Noema and consumers to distinguish:

Action Contract

from:

execution

and from:

individual execution attempts

Execution identity must remain stable enough to support idempotency, reconciliation, audit, and recovery.

⸻

12. Contract-to-Execution Relationship

One Action Contract may produce one or more execution attempts depending on its execution semantics.

For example:

contract_123
     ↓
execution_123
     ↓
attempt_1
     ↓
timeout
     ↓
reconciliation
     ↓
attempt_2
     ↓
success

Retries must preserve the semantic identity of the Action while maintaining distinct attempt identities.

Whether multiple attempts are represented under one execution record or as independently stored execution records is implementation-specific.

⸻

13. Execution Attempt

An Execution Attempt is one concrete attempt by a consumer to perform the Action described by an Action Contract.

Conceptually:

Execution {
    execution_id
    contract_id
    action_instance_id
    attempt
    consumer
    started_at
    completed_at
    status
    outcome
    evidence
    error
}

The exact persistence schema is implementation-specific.

The semantic distinction between execution and attempt must remain explicit.

⸻

14. Attempt vs Execution

For clarity:

Execution
    ├── Attempt 1
    ├── Attempt 2
    └── Attempt 3

An execution represents the logical execution activity, while an attempt represents one concrete delivery or performance attempt.

Alternatively, an implementation may model each attempt as an independently identifiable execution record.

The important requirement is that retries remain observable and causally linked.

⸻

15. Execution Lifecycle

A conceptual lifecycle is:

ISSUED
   ↓
DISPATCHED
   ↓
ACCEPTED
   ↓
EXECUTING
   ↓
COMPLETED

Branches may include:

REJECTED
FAILED
TIMED_OUT
CANCELLED
UNKNOWN

UNKNOWN is particularly important because absence of an observed result does not establish absence of an external effect.

⸻

16. ISSUED

The Action Contract exists and is ready for delivery to its intended consumer.

At this point:

Contract = valid
Execution = not yet attempted

The existence of an issued Contract does not imply that execution occurred.

⸻

17. DISPATCHED

Noema or an execution coordinator has transmitted the Contract to the intended consumer.

This does not establish:

* consumer receipt;
* consumer acceptance;
* execution start;
* business-state mutation.

Dispatch is a transport/execution-control event.

⸻

18. ACCEPTED

The consumer has acknowledged that it has accepted the Contract for processing.

This does not mean:

Action succeeded

It means:

Consumer accepted responsibility for processing

Acceptance is therefore distinct from execution success.

⸻

19. EXECUTING

The consumer is actively attempting the Action.

Example:

payment-service
    ↓
calling payment provider

The business-state effect remains unestablished until the consumer or an authoritative source provides sufficient evidence.

⸻

20. COMPLETED

The consumer has established that the execution attempt completed according to its execution semantics.

For consequential Actions, completion should be accompanied by sufficient evidence and verification requirements.

COMPLETED therefore describes execution lifecycle state; it does not by itself define the complete enterprise Outcome.

⸻

21. FAILED

The consumer established that the Action did not complete successfully according to the relevant execution semantics.

Example:

payment provider
    ↓
definitively rejected transaction

A failure may still leave external side effects in some systems. Where the effect is uncertain, the correct state is UNKNOWN until reconciled.

⸻

22. REJECTED

The consumer refuses to execute the Contract.

Possible reasons include:

* unsupported Action;
* invalid consumer-side parameters;
* consumer policy;
* resource unavailable;
* Contract invalid;
* Contract expired;
* integration incompatibility.

Consumer rejection differs from a business execution failure.

A consumer must not reject a Contract by silently substituting a different Action.

⸻

23. TIMED_OUT

The execution did not complete within the applicable execution window.

Important:

TIMEOUT ≠ confirmed failure

The external system may have committed the Action even though the consumer did not receive the result.

Therefore:

TIMEOUT
   ↓
determine whether state is established
   ├── established success
   ├── established failure
   └── UNKNOWN

Timeout handling is governed by the Action, Contract, consumer semantics, and reconciliation requirements.

⸻

24. UNKNOWN

UNKNOWN means:

Noema or the execution consumer cannot deterministically establish whether the Action occurred or what execution state was reached.

Example:

Request sent
    ↓
External system executes
    ↓
Network connection lost
    ↓
No response

The result is:

UNKNOWN

not:

FAILED

Unknown execution state is first-class and must not be collapsed into failure.

⸻

25. Unknown Execution State

Unknown execution state must trigger reconciliation where possible.

UNKNOWN
   ↓
State Reconciliation
   ↓
┌───────────┬───────────┬───────────┐
▼           ▼           ▼
SUCCESS    FAILURE     UNKNOWN

Only after reconciliation should the system determine the next recovery path.

If authoritative state remains unavailable or conflicting, the system may require intervention or escalation.

⸻

26. Execution State Is Not Trust State

The Trust Model determines whether an Action is permitted to proceed.

The Execution Model determines what happens after the permitted execution path is established.

For example:

Trust:
EXECUTE
Execution:
FAILED

The failure does not mean the Action was untrusted.

Likewise:

Trust:
REJECT
Execution:
none

No execution should occur.

Trust EXECUTE means permission to proceed under evaluated conditions; it does not mean execution succeeded.

⸻

27. Execution Preconditions

Execution should not begin unless the applicable execution prerequisites are established, including:

valid Action Contract
+
applicable Trust Decision
+
resolved actor
+
resolved Action
+
resolved exact target/resource
+
required execution context
+
consumer available

Where current enterprise state is material, the relevant preconditions must be evaluated against sufficiently current authoritative or reconciled state.

⸻

28. Final Business-State Validation

The execution consumer should validate relevant business state immediately before mutation where appropriate.

Example:

Noema:
"Refund payment_123."
Consumer:
"payment_123 is already refunded."

The consumer should not blindly execute against stale state.

This is especially important where another system or concurrent execution may have changed the resource after Trust evaluation.

⸻

29. State Freshness

Noema may have evaluated Trust using state observed earlier.

That state may change before execution.

Example:

10:00
Trust evaluation:
payment = CAPTURED
10:02
Execution:
payment = ALREADY_REFUNDED

The authoritative enterprise state must determine the actual business condition.

Freshness is claim-, action-, policy-, and execution-specific. A newer observation is not automatically more authoritative than an older authoritative source.

⸻

30. Execution Concurrency

Two contracts may attempt related Actions concurrently.

Example:

Contract A:
refund payment_123
Contract B:
refund payment_123

The enterprise system must protect the relevant business invariant.

Possible result:

A → SUCCESS
B → REJECTED / ALREADY_COMPLETED

Noema cannot rely solely on its own Intent or execution state to prevent every concurrent business mutation.

Enterprise atomic operations, resource versions, conditional writes, transactions, reservations, or equivalent mechanisms may be required.

⸻

31. Idempotency

Execution must support appropriate idempotency semantics for Actions where duplicate execution is dangerous.

Example:

contract_id = C123
execution_id = E123
idempotency_key = K456

If the consumer receives:

K456
K456
K456

it should not create three independent mutations where the Action semantics prohibit that.

Idempotency must be defined by the Action and execution contract rather than assumed universally.

⸻

32. Retry

Execution may be retried when the failure is transient and retry is permitted.

Example:

Attempt 1
    ↓
NETWORK_FAILURE
    ↓
Attempt 2
    ↓
SUCCESS

Retry policy should consider:

* Action idempotency;
* failure classification;
* execution limits;
* time constraints;
* current business state;
* Contract validity;
* consumer semantics.

An UNKNOWN execution must be reconciled before retry where the original effect may have occurred.

⸻

33. Retry Is Not Reauthorization by Default

A retry of the same execution should preserve the semantic identity of the original Action.

Example:

Contract C:
transfer ₦100,000

Retrying C means:

retry transfer ₦100,000

It does not mean:

create a new transfer Intent

However, if Contract validity, authorization, policy, state, or other consequential conditions have changed, deterministic revalidation or a new Trust Decision may be required.

A retry must never silently broaden or alter the Action.

⸻

34. Execution Expiration

Contracts may contain an execution expiration.

Example:

expires_at:
2026-08-25T15:00:00Z

A consumer receiving the Contract after expiration should reject it unless the Contract or applicable policy explicitly permits execution.

Expiration is distinct from business-state truth.

⸻

35. Cancellation

Some executions may be cancellable.

Example:

EXECUTING
    ↓
CANCEL_REQUESTED
    ↓
CANCELLED

Cancellation is not guaranteed.

If an external system has already committed the mutation:

CANCELLED

may no longer be possible.

The system must distinguish cancellation of execution activity from reversal or compensation of an already-committed business effect.

⸻

36. Cancellation vs Compensation

Cancellation attempts to prevent or stop execution where possible.

Compensation addresses an effect that has already occurred.

Cancellation:
stop before effect where possible
Compensation:
correct after effect

Example:

Pending payment
    ↓
cancel_payment

versus:

Payment completed
    ↓
refund_payment

These are distinct Actions with distinct authorization and execution semantics.

⸻

37. Execution Atomicity

Execution may be:

ATOMIC
NON_ATOMIC
UNKNOWN

depending on the consumer and Action.

Noema must not assume distributed atomicity merely because several Actions belong to one Intent.

Atomicity is scoped to the system and operation that actually provides it.

⸻

38. Composite Execution

A composite Intent may produce multiple Actions:

A
↓
B
↓
C

The Execution Model represents each Action execution independently.

For example:

Execution Graph
    A → SUCCESS
    B → SUCCESS
    C → FAILURE

This enables precise failure propagation, compensation evaluation, reconciliation, and Outcome assessment.

⸻

39. Execution Dependencies

Dependencies must be explicit.

Example:

create_customer
      ↓
create_subscription
      ↓
send_welcome_email

If:

create_customer → FAILURE

downstream Actions should not execute unless their dependency semantics explicitly permit it.

A Planner or execution engine must not infer arbitrary dependency relationships from natural-language descriptions.

⸻

40. Execution Graph

For composite execution:

             create_customer
                    │
                    ▼
             create_subscription
                    │
                    ▼
             send_notification

The graph defines:

* ordering;
* dependencies;
* parallelism;
* failure propagation;
* compensation relationships;
* applicable execution constraints.

The Enterprise Action Graph and execution graph are related but distinct. The Enterprise Action Graph describes available enterprise capabilities and relationships; the execution graph describes a particular execution plan.

⸻

41. Parallel Execution

Independent Actions may execute concurrently.

Example:

             ┌── send_email
Intent ──────┤
             └── send_push

If no dependency exists:

send_email
send_push

may execute in parallel.

Parallelism must be explicitly permitted by Action dependencies, resource constraints, policy, and execution semantics.

⸻

42. Execution Ordering

Where order matters:

A → B

must be represented as an explicit dependency or execution constraint.

Noema must not rely on incidental queue ordering, network timing, or implementation behavior.

⸻

43. Execution Result

The consumer should produce a structured result.

Conceptually:

ExecutionResult {
    execution_id
    attempt_id
    status
    outcome
    evidence
    error
    completed_at
}

The result must distinguish what the consumer knows from what it merely attempted.

⸻

44. Execution Evidence

Execution evidence may include:

* transaction identifier;
* provider reference;
* resource version;
* authoritative timestamp;
* affected resource;
* consumer receipt;
* enterprise operation identifier;
* reconciliation reference.

Evidence supports Outcome establishment but is not itself equivalent to Fact Status or Business State.

Evidence may be:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

through the separate Fact Status semantics applicable to the underlying claim.

⸻

45. Error Model

Execution errors should be structured.

Conceptually:

ExecutionError {
    code
    category
    message
    retryable
    source
}

Possible categories:

VALIDATION_ERROR
AUTHORIZATION_ERROR
BUSINESS_RULE_ERROR
RESOURCE_ERROR
DEPENDENCY_ERROR
NETWORK_ERROR
TIMEOUT
INTERNAL_ERROR
UNKNOWN

The canonical taxonomy should evolve as implementation experience accumulates.

An error classification must not be used to manufacture certainty about an external business effect that remains unknown.

⸻

46. Retryability

An error may indicate whether retry is appropriate where the consumer can determine this.

For example:

NETWORK_ERROR
retryable = true

versus:

INSUFFICIENT_FUNDS
retryable = false

Retryability is an execution concern governed by explicit Action and execution semantics.

It is not an LLM judgment.

⸻

47. Execution Outcome

The Execution Model distinguishes:

execution status

from:

Outcome

and from:

enterprise Business State

For example:

Execution status:
COMPLETED
Outcome:
refund_transaction_created

The corresponding enterprise business state remains authoritative in the relevant enterprise system.

⸻

48. Execution and Outcome

The relationship is:

Execution
    ↓
Verification
    ↓
Outcome

Outcome describes what the execution and available authoritative evidence establish about the requested operation.

An execution may complete without establishing the desired business Outcome.

⸻

49. Execution Does Not Invent Outcomes

A consumer should report only what it can establish.

Bad:

Execution succeeded,
therefore customer is satisfied.

Customer satisfaction is not automatically an execution fact.

Better:

payment_refund_transaction_created

The Outcome Model determines how this established result relates to the requested Intent Outcome.

⸻

50. Execution Provenance

Every execution should maintain provenance including:

execution_id
contract_id
intent_version
action_id
action_version
action_instance_id
actor_reference
target_reference
consumer
timestamps
attempts
trust_decision_id
outcome

Where applicable, provenance should also preserve:

policy_version
capability_version
graph_version
integration_version
contract_versions

This allows the causal path to be reconstructed.

⸻

51. Execution Trace

A canonical trace might look like:

Intent: int_123:v2
    ↓
Action: refund_payment:v3
    ↓
Trust Decision: trust_456
    ↓
Action Contract: contract_789:v2
    ↓
Execution: exec_001
    ↓
Consumer: payment-service
    ↓
Attempt: attempt_1
    ↓
Verification
    ↓
Outcome: refund_created

The exact versions are significant because historical execution must remain interpretable according to the semantics that governed it at the time.

⸻

52. Execution and Compensation

When execution produces a verified divergence requiring recovery:

Execution
    ↓
Verification
    ↓
Outcome / Divergence
    ↓
Compensation Evaluation
    ↓
Compensation Action
    ↓
Compensation Contract
    ↓
Compensation Execution
    ↓
Verification

The original execution remains immutable.

Compensation does not rewrite the original execution Outcome.

⸻

53. Execution and Human Intervention

Some executions may require human intervention.

Example:

Execution:
UNKNOWN
    ↓
reconciliation unavailable
    ↓
HUMAN_REVIEW

Human intervention must not silently mutate execution history.

The intervention should be represented as a distinct decision, Action, event, or execution-domain record with its own identity and provenance.

If the human materially changes the desired Intent, that change must create a new Intent version rather than mutating the original.

⸻

54. Execution Events

Execution may be represented through semantic events such as:

CONTRACT_DISPATCHED
CONTRACT_ACCEPTED
EXECUTION_STARTED
EXECUTION_PROGRESS
EXECUTION_COMPLETED
EXECUTION_FAILED
EXECUTION_RECONCILIATION_REQUIRED
EXECUTION_RECONCILED

Whether Noema uses event sourcing internally is an implementation decision.

The semantic execution events must remain observable and auditable where required.

⸻

55. Execution Progress

Long-running Actions may expose progress.

Example:

PROVISIONING
    25%
    50%
    75%
    100%

Progress is informational execution state.

It must not be confused with:

* successful completion;
* verified business Outcome;
* enterprise Business State.

⸻

56. Long-Running Execution

Some Actions cannot complete immediately.

Examples:

provision_infrastructure
process_refund
generate_report
ship_order
migrate_data

The Execution Model therefore supports:

ACCEPTED
    ↓
EXECUTING
    ↓
...time...
    ↓
COMPLETED

Long-running execution must respect Contract expiration, authorization validity, resource state, and any required revalidation semantics.

⸻

57. Asynchronous Execution

An Action Contract may be consumed asynchronously:

Noema
  ↓
Queue / Transport
  ↓
Consumer
  ↓
Execution
  ↓
Outcome / Verification
  ↓
Noema

The Action Contract remains the semantic authorization boundary regardless of transport.

Transport does not create new authority.

⸻

58. Synchronous Execution

Execution may also be synchronous:

Noema
  ↓
Consumer
  ↓
Business System
  ↓
Outcome
  ↓
Noema

The semantic model remains the same.

Only transport and timing differ.

⸻

59. Execution Isolation

An execution consumer should execute only within the scope defined by the Action Contract.

If the Contract authorizes:

update_customer(customer_123)

the consumer must not interpret that as permission to:

delete_customer(customer_123)

or:

update_customer(customer_456)

The consumer must not substitute resources, Actions, parameters, or authority outside the Contract.

⸻

60. Execution Security

Consumers should establish the required:

* Contract authenticity;
* Contract integrity;
* consumer identity;
* Contract validity;
* execution authority;
* parameter validity;
* resource binding.

The model must not possess execution credentials or direct enterprise access.

No free-form model output may reach the execution boundary as executable authority.

Execution must occur through explicit registered capabilities and Action Contracts.

⸻

61. Execution Exactly-Once Semantics

Noema should not assume exactly-once execution across distributed systems.

The practical model should prefer, where appropriate:

at-least-once delivery
+
idempotent execution
+
deduplication
+
reconciliation

Exactly-once behavior may exist within a particular system, but it must not be treated as a universal distributed invariant.

⸻

62. Execution Delivery Semantics

Execution infrastructure may support:

AT_MOST_ONCE
AT_LEAST_ONCE
EFFECTIVELY_ONCE

The selected delivery semantics must be explicit.

For consequential Actions, at-least-once delivery generally requires strong idempotency or deduplication guarantees.

Delivery semantics do not determine business Outcome semantics.

⸻

63. Execution Consistency

The Execution Model must distinguish:

Noema execution state
Consumer execution state
Enterprise Business State
External provider state

These may temporarily diverge.

Example:

Noema:
EXECUTING
Consumer:
COMPLETED
External provider:
COMPLETED

Noema must reconcile toward authoritative evidence rather than assuming that its local execution state is business truth.

⸻

64. Consumer and Business-State Authority

For a domain Action such as:

refund_payment

the relevant enterprise payment system or System of Record is generally authoritative for:

Was the refund actually created?

Noema should not infer this merely from:

execution request sent

or:

consumer acknowledged request

Authority is claim-specific and must be established through the appropriate enterprise source.

⸻

65. Execution Reconciliation

Reconciliation resolves uncertainty between execution records and authoritative business or execution state.

Example:

Execution:
UNKNOWN
Reconciliation:
payment provider says refund reference
transaction_refund_123 exists
Result:
refund execution established

State Reconciliation is a first-class capability rather than an incidental retry mechanism.

The reconciled claim should retain its source, authority, observation time, and Fact Status.

⸻

66. Execution Recovery

Recovery mechanisms may include:

retry
reconciliation
compensation
manual intervention
escalation

The correct mechanism depends on:

* execution state;
* Action semantics;
* current enterprise state;
* idempotency;
* policy;
* authorization;
* compensation definitions;
* time constraints.

Recovery must be deterministic where the consequences are material.

⸻

67. Execution and Determinism

The execution model must never use model intuition to decide whether an external mutation occurred.

Bad:

"The request probably succeeded."

Better:

SUCCESS

only when sufficient authoritative or appropriately reconciled evidence supports that conclusion.

Otherwise:

UNKNOWN

remains the correct state.

The model may assist with interpretation or candidate recovery planning, but it cannot establish execution truth.

⸻

68. Execution and Noema’s Trust Boundary

Trust answers:

May this Action execute?

Execution answers:

What happened when we attempted it?

Verification answers:

What can we establish about the resulting state?

Outcome answers:

What result has been established in relation to the requested operation?

These distinctions must remain explicit throughout the architecture.

⸻

69. Conceptual Execution Model

                       INTENT
                          │
                          ▼
                        ACTION
                          │
                          ▼
                   TRUST → EXECUTE
                          │
                          ▼
                   ACTION CONTRACT
                          │
                          ▼
                      DISPATCH
                          │
                          ▼
                      CONSUMER
                          │
                ┌─────────┴─────────┐
                ▼                   ▼
             REJECT              ACCEPT
                                    │
                                    ▼
                                EXECUTING
                                    │
                         ┌──────────┼──────────┐
                         ▼          ▼          ▼
                     SUCCESS     FAILURE     UNKNOWN
                         │          │          │
                         │          │          ▼
                         │          │     RECONCILIATION
                         │          │          │
                         │          └────┬─────┘
                         │               │
                         │          ┌────┴─────┐
                         │          ▼          ▼
                         │       SUCCESS    FAILURE /
                         │                    UNKNOWN
                         │
                         ▼
                    VERIFICATION
                         │
                         ▼
                      OUTCOME
                         │
                  ┌──────┴──────┐
                  ▼             ▼
             ACCEPTABLE     DIVERGENCE
                                │
                                ▼
                         COMPENSATION /
                            ESCALATION

⸻

70. Execution Invariants

Invariant 1

Execution occurs only against an explicit Action Contract.

Invariant 2

An Action Contract does not guarantee successful execution.

Invariant 3

Execution Consumers own execution mechanics.

Invariant 4

Enterprise authoritative systems establish enterprise Business State.

Invariant 5

UNKNOWN execution state must not be represented as confirmed failure.

Invariant 6

Timeout does not necessarily mean failure.

Invariant 7

Retries must preserve the semantic identity of the original Action unless a new Action is explicitly created.

Invariant 8

Consequential Actions must provide appropriate idempotency semantics.

Invariant 9

Execution attempts must remain observable and causally linked.

Invariant 10

Execution history must not be silently rewritten.

Invariant 11

Cancellation and compensation are distinct.

Invariant 12

Execution dependencies must be explicit.

Invariant 13

Parallel execution must occur only where Action dependencies and constraints permit it.

Invariant 14

Compensation requires its own execution semantics.

Invariant 15

Noema must not infer business success from dispatch or consumer acceptance alone.

Invariant 16

Consequential execution results must be supported by appropriate evidence and verification.

Invariant 17

State Reconciliation must be used when execution or relevant business state is materially uncertain.

Invariant 18

Fact Status is distinct from Evidence, Execution State, and Outcome.

Invariant 19

Trust EXECUTE means the Action is permitted to proceed; it does not mean execution succeeded.

Invariant 20

Outcome is distinct from enterprise Business State.

Invariant 21

The exact Intent version governing consequential execution must remain identifiable.

Invariant 22

An admitted Intent is immutable; material changes require a new Intent version.

Invariant 23

The resolved actor, Action, exact target/resource, scope, and Action Instance must be preserved for consequential execution.

Invariant 24

The Planner cannot invent Actions, capabilities, authority, or Contract semantics.

Invariant 25

Execution must remain bounded by the Enterprise Action Graph, Capability Registry, Action Registry, and Action Contract.

Invariant 26

Model output, retrieved information, and tool responses are untrusted inputs and cannot directly authorize execution.

Invariant 27

Execution consumers must not expand the authority or scope of an Action Contract.

Invariant 28

Unknown business or execution state must remain explicit rather than being resolved through probabilistic guessing.

Invariant 29

Replay of execution observations or events must not create a new business occurrence by default.

Invariant 30

Operational Memory may preserve execution history but is not authoritative enterprise Business State.

⸻

71. Canonical Mental Model

The Execution Model can be reduced to:

Action Contract
      │
      │ authorizes
      ▼
Execution
      │
      │ attempts
      ▼
Execution Consumer
      │
      ▼
Enterprise System
      │
      │ establishes / exposes
      ▼
Evidence
      │
      ▼
Verification / State Reconciliation
      │
      ▼
Outcome

With recovery:

Execution
    │
    ├── SUCCESS ────────────────→ Verification → Outcome
    │
    ├── RETRY ─────────────────→ Execution Attempt
    │
    ├── UNKNOWN ───────────────→ Reconciliation
    │
    ├── FAILURE ───────────────→ Compensation / Escalation
    │
    └── REJECTED ──────────────→ Execution Control State

The central rule is:

Trust determines permission.
Execution performs the Action.
Verification establishes what can be known.
Outcome records the established result.
Enterprise Systems of Record remain authoritative for Business State.

⸻

72. Final Definition

The Execution Model defines execution as the controlled attempt to perform a trusted, contract-bound Action through an Execution Consumer, with explicit lifecycle states, execution identity, retry and idempotency semantics, reconciliation of uncertainty, verification, authoritative Outcome establishment, and bounded recovery mechanisms.

Execution is deliberately separated from Intent, Action, Trust, Action Contract, Outcome, and enterprise Business State.

The core invariant is:

Noema does not confuse permission with execution, execution with success, or success with business truth. An Action Contract establishes what may be executed; the consumer attempts it; authoritative enterprise systems establish what happened; State Reconciliation resolves uncertainty where possible; verification establishes the relevant Outcome; and Noema records the resulting execution history without inventing certainty where none exists.