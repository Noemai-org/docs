> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Idempotency

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/idempotency.md

⸻

1. Definition

Idempotency is the engineering property that permits an Action execution attempt to be repeated without producing unintended additional effects beyond those permitted by the Action Contract.

Idempotency is required because durable execution operates in an environment where execution outcomes may be uncertain.

An execution consumer may:

* successfully perform an external operation but fail to return the response
* time out while the external operation continues
* crash after sending a request
* retry after an ambiguous response
* receive duplicate delivery of an execution request
* recover and replay durable execution state
* process a message more than once
* encounter a network failure between Noema and an external system

Therefore:

A retry is not evidence that the previous execution did not occur.

The canonical concern is:

Execution Attempt
       ↓
External Effect
       ↓
Outcome Unknown
       ↓
Retry
       ↓
Potential Duplicate Effect

Idempotency provides the engineering mechanism for preventing an uncertain execution state from becoming an unintended duplicate external effect.

⸻

2. Core Principle

Noema must treat retries and duplicate delivery as normal properties of durable execution.

The fundamental invariant is:

A consequential Action must not produce unintended duplicate effects merely because its execution was retried, replayed, or delivered more than once.

Conceptually:

Action
  ↓
Execution Attempt 1
  ↓
Outcome Unknown
  ↓
Retry
  ↓
Execution Attempt 2

must not automatically mean:

External Effect × 2

Instead, the execution architecture must establish whether the second attempt:

* is a continuation of the first
* can safely be replayed
* can be deduplicated
* can be reconciled
* requires authoritative status lookup
* must be blocked because the outcome remains uncertain

⸻

3. Idempotency Is Not Exactly-Once Execution

Noema must distinguish:

Idempotent execution

from:

Exactly-once execution.

Exactly-once execution is a stronger property and cannot generally be assumed across arbitrary external systems.

A system may provide:

At-least-once delivery
+
Idempotency

without providing physically exactly-once message delivery.

The engineering objective is therefore not to assume that execution occurs exactly once.

The objective is to ensure that repeated execution attempts do not create unintended repeated effects.

Therefore:

Exactly-once delivery
        ≠
Idempotent effect

and:

At-least-once execution
        +
Idempotent Action semantics
        =
Safe retry behavior

where the external system and Action Contract support the required semantics.

⸻

4. Relationship to Durable Execution

Durable execution assumes that execution state may survive process failure and that execution may resume after interruption.

For example:

Action
  ↓
Persist intent to execute
  ↓
Send external request
  ↓
Process crashes

After recovery, Noema may know:

request persisted = YES
response persisted = NO

It therefore cannot safely conclude:

external effect = NOT PERFORMED

The correct state may be:

external outcome = UNKNOWN

Idempotency allows recovery to continue without blindly duplicating the external operation.

⸻

5. Idempotency and Unknown Outcomes

Unknown execution outcome is a first-class execution condition.

For example:

CREATE_PAYMENT
      ↓
request sent
      ↓
network timeout
      ↓
OUTCOME_UNKNOWN

Noema must not automatically translate:

UNKNOWN

into:

FAILED

and must not automatically retry:

UNKNOWN

as though no external request had occurred.

The correct recovery behavior depends on the Action Contract.

Possible strategies include:

UNKNOWN
   ↓
Query authoritative status
   ↓
Already completed → reconcile
Not completed → retry
Still unknown → remain UNKNOWN / escalate

or:

UNKNOWN
   ↓
Retry with same idempotency key

where the external capability supports idempotent request semantics.

⸻

6. Idempotency Boundary

Idempotency belongs primarily to the boundary between Noema execution and the external capability.

Conceptually:

Action Graph
      ↓
Action Contract
      ↓
Execution Consumer
      ↓
Idempotency Boundary
      ↓
External Capability
      ↓
External Business State

The Action Graph identifies the Action.

The Action Contract establishes the Action’s executable semantics.

The execution consumer performs the Action.

The external system remains authoritative for its business state.

Noema must not claim that an operation is idempotent merely because the graph contains the Action.

⸻

7. Action Contract Responsibility

The Action Contract should define idempotency requirements for consequential Actions where appropriate.

An Action Contract may specify:

* whether the Action is idempotent
* how idempotency is established
* the idempotency key
* key scope
* key lifetime
* duplicate-request behavior
* retry semantics
* status-reconciliation requirements
* whether the external capability guarantees deduplication
* whether an unknown result requires reconciliation
* whether replay is safe

Conceptually:

Action Contract
{
    action
    inputs
    outputs
    authorization
    preconditions
    idempotency
    retry_policy
    timeout
    failure_semantics
}

The exact schema belongs to the Action Contract specification.

⸻

8. Idempotency Key

An idempotency key is a stable identifier associated with a logical Action execution such that repeated attempts belonging to the same logical execution can be recognized as duplicates.

Conceptually:

Action Execution
    ↓
idempotency_key
    ↓
Attempt 1
Attempt 2
Attempt 3

All attempts represent the same logical execution when they carry the same applicable idempotency identity.

The key must not change merely because the Action is retried.

Therefore:

Retry ≠ New Action

and normally:

Retry Attempt 1
Retry Attempt 2
Retry Attempt 3
        │
        └── same logical execution identity

⸻

9. Idempotency Key vs Action Identity

An Action identity identifies the type of Action.

For example:

CREATE_PAYMENT

An idempotency key identifies a particular logical execution of that Action.

For example:

Action:
    CREATE_PAYMENT
Execution:
    payment_creation_for_intent_123
Idempotency Key:
    exec_456

Therefore:

Action Identity
    ≠
Execution Identity
    ≠
Idempotency Key

The exact identity relationships must be defined by the execution architecture.

⸻

10. Idempotency Key Stability

An idempotency key must remain stable across retries of the same logical execution.

Incorrect:

Attempt 1 → key A
Attempt 2 → key B
Attempt 3 → key C

This may cause an external provider to interpret each attempt as a distinct operation.

Correct, where supported:

Attempt 1 ─┐
Attempt 2 ─┼── key A
Attempt 3 ─┘

The key therefore represents the logical execution rather than the transport attempt.

⸻

11. Attempt Identity

An execution attempt may additionally have its own identity.

For example:

Logical Execution:
    exec_123
Attempts:
    attempt_1
    attempt_2
    attempt_3

This distinction allows Noema to preserve:

* logical execution identity
* attempt identity
* attempt timestamps
* retry count
* transport information
* individual responses
* failure information

Conceptually:

Execution
 ├── Attempt 1
 ├── Attempt 2
 └── Attempt 3

All attempts remain associated with the same logical Action execution.

⸻

12. Idempotency Scope

An idempotency key is meaningful only within a defined scope.

Possible scopes include:

* Action
* capability
* provider
* tenant
* Actor
* Intent
* execution
* resource
* global system

The scope must be explicit.

For example:

key = abc123
scope = payment.create

does not necessarily imply:

key = abc123
scope = account.delete

The same identifier may have different meanings in different scopes.

⸻

13. Idempotency Key Generation

Idempotency keys should be generated according to deterministic execution semantics where appropriate.

A key may be derived from:

* logical execution identity
* Action identity
* Intent identity
* graph node identity
* execution version
* explicitly defined contract fields

The derivation must be defined by the relevant contract.

Noema must avoid deriving keys from mutable or incidental transport metadata when the logical execution must remain stable.

For example:

request timestamp
network connection ID
process ID

should not automatically become the logical idempotency identity.

⸻

14. Idempotency and Intent Versions

A materially changed Intent represents a different semantic state.

For example:

Intent v1
amount = ₦50,000
Intent v2
amount = ₦75,000

The execution identity for v1 must not silently become the execution identity for v2.

Therefore:

Intent v1
    ↓
Execution A
    ↓
Idempotency Key A

and:

Intent v2
    ↓
Execution B
    ↓
Idempotency Key B

where the semantic change establishes a new execution.

A retry of v1 must retain v1’s execution identity.

⸻

15. Idempotency and Action Graph Versions

A graph revision may affect execution identity.

For example:

Graph v1
    ↓
Action A

later becomes:

Graph v2
    ↓
Action B

Noema must not automatically treat B as a retry of A.

The execution architecture must establish whether the revised graph represents:

* continuation
* replacement
* compensation
* a new Action
* a new execution

Idempotency must follow the logical execution semantics rather than merely the existence of a similar node.

⸻

16. Duplicate Delivery

Execution infrastructure may deliver the same logical execution more than once.

Example:

Queue
 ├── message(exec_123)
 └── message(exec_123)

The consumer must not assume:

message count = execution count

Instead:

logical execution identity
        ↓
deduplication / idempotency
        ↓
external effect

Duplicate delivery must therefore be safe under the Action’s contract.

⸻

17. Crash Recovery

A process may crash at any point.

Consider:

1. Load Action
2. Mark execution active
3. Send external request
4. Receive external response
5. Persist result

A crash may occur between any of these operations.

For example:

External request succeeds
        ↓
Process crashes
        ↓
Result not persisted

After recovery, Noema may observe:

local result = UNKNOWN
external effect = possibly completed

Recovery must use idempotency and/or reconciliation rather than assuming the external effect did not occur.

⸻

18. The Critical Failure Window

The most important idempotency boundary is:

External Effect
      ↓
Response
      ↓
Durable Local Record

A failure between these stages creates an uncertain outcome.

Conceptually:

Noema ───── request ─────> External System
                          │
                          ▼
                     Effect occurs
                          │
                    response lost
                          X
Noema <──── no response ──┘

The absence of a response does not prove the absence of an effect.

This is why idempotency must be designed around logical execution identity rather than response receipt.

⸻

19. Idempotency Record

Where required, Noema may maintain a durable idempotency record.

Conceptually:

IdempotencyRecord {
    key
    scope
    action
    execution_id
    status
    request_fingerprint
    result_reference
    created_at
    updated_at
    expiration
}

The exact schema is implementation-specific.

The record should permit the execution system to distinguish:

* first execution
* duplicate execution
* completed execution
* execution still in progress
* failed execution
* unknown execution
* conflicting reuse of a key

⸻

20. Request Fingerprint

An idempotency key should not automatically permit arbitrary reuse with different semantic inputs.

For example:

key = abc123
Attempt 1:
amount = ₦50,000
Attempt 2:
amount = ₦75,000

This may represent a semantic conflict.

The idempotency layer should therefore be able to associate the key with an appropriate request fingerprint or equivalent execution identity.

If a key is reused with materially different inputs, the system should produce an explicit conflict rather than silently treating the request as the original execution.

Conceptually:

same key
+
different semantic request
=
IDEMPOTENCY_CONFLICT

⸻

21. Idempotency Conflict

A conflict occurs when the same idempotency identity is presented with incompatible execution semantics.

Possible result:

IDEMPOTENCY_CONFLICT

The system must not:

* overwrite the original request
* execute the second request as though it were the first
* silently merge the requests

The conflict should be surfaced for deterministic handling.

⸻

22. Duplicate Request Semantics

When a duplicate request is detected, the system may:

Return original result

or:

Return current execution state

or:

Reconcile external status

or:

Reject duplicate

The appropriate behavior depends on the Action Contract and external capability.

Duplicate handling must therefore be explicit.

⸻

23. Idempotency Does Not Mean Suppressing All Repetition

Some Actions are legitimately repeatable.

For example:

READ_ACCOUNT

may be safely executed repeatedly without requiring an idempotency key.

Other Actions may intentionally create separate effects.

For example:

SEND_NOTIFICATION

may legitimately send multiple notifications if the Intent or contract defines each send as a distinct operation.

Therefore:

Idempotency is not a universal requirement to suppress repetition.

It is a requirement to preserve the intended semantics of repeated execution attempts.

⸻

24. Naturally Idempotent Actions

Some Actions are naturally idempotent.

For example:

SET_ACCOUNT_STATUS
    status = ACTIVE

Repeated application may produce the same resulting state:

ACTIVE → ACTIVE
ACTIVE → ACTIVE

However, natural idempotence must not be assumed merely from the Action name.

The external system’s semantics must establish whether repeated requests are safe.

⸻

25. Non-Idempotent Actions

Some Actions are inherently non-idempotent.

Examples may include:

CREATE_PAYMENT
CHARGE_CARD
SEND_MONEY
CREATE_RESOURCE
SEND_NOTIFICATION

depending on the external system.

For these Actions, retries require explicit protection through mechanisms such as:

* idempotency keys
* provider-side deduplication
* authoritative status lookup
* transactional semantics
* reconciliation
* compensation where appropriate

A non-idempotent Action must not be blindly retried.

⸻

26. Idempotency Is Not the Same as Atomicity

Idempotency and atomicity address different concerns.

Idempotency:

Can the same logical operation be safely attempted more than once?

Atomicity:

Does a group of operations behave as one indivisible unit?

For example:

A → B → C

may be idempotent at the individual Action level while the overall sequence is not atomic.

Therefore:

Idempotent ≠ Atomic

and:

Atomic ≠ Idempotent

Both properties must be defined independently.

⸻

27. Idempotency Is Not Compensation

Compensation addresses the consequences of an already-performed effect.

For example:

Create Transfer
      ↓
Create Account Record
      ↓
Failure
      ↓
Compensating Action

Idempotency prevents unintended duplicate effects during repeated execution.

Compensation attempts to address effects that have already occurred.

Therefore:

Idempotency
    =
safe repetition
Compensation
    =
explicit recovery from completed effects

They are complementary mechanisms.

⸻

28. Idempotency and Retry

Retry is safe only when the Action Contract establishes that retry is safe.

Conceptually:

FAILED
  ↓
Retry permitted?
  ├── NO → FAILED
  └── YES
        ↓
Idempotency semantics satisfied?
  ├── NO → BLOCK / RECONCILE
  └── YES
        ↓
Retry

A retry policy must therefore be coupled to idempotency semantics.

The presence of a network failure does not by itself justify a retry.

⸻

29. Retryable vs Non-Retryable Failures

The Action Contract should distinguish failure classes.

Examples:

RETRYABLE
NON_RETRYABLE
UNKNOWN

An unknown outcome is particularly important because:

UNKNOWN ≠ FAILED

A retry after UNKNOWN requires stronger reasoning than a retry after a confirmed pre-execution failure.

⸻

30. Pre-Execution Failure

If the execution consumer can establish that the external request was never sent, retry may be straightforward.

Example:

Action READY
      ↓
Consumer unavailable
      ↓
Request NOT_SENT

The execution may safely retry because no external effect was initiated.

The system must nevertheless rely on evidence sufficient to establish:

request not sent

rather than assuming it.

⸻

31. Post-Request Unknown

If the external request may have been sent:

Action
  ↓
Request transmitted
  ↓
Timeout
  ↓
UNKNOWN

the execution system must not treat the Action as a clean failure.

Possible handling:

UNKNOWN
   ↓
Provider status query

or:

UNKNOWN
   ↓
Retry with same idempotency key

where supported.

⸻

32. Provider-Side Idempotency

The strongest form of protection for many consequential external operations is provider-side idempotency.

Conceptually:

Noema
  │
  │ idempotency_key = K
  ▼
Provider
  │
  ├── first request → perform operation
  │
  └── duplicate K   → return prior result

The provider therefore becomes the authority for deduplicating the external operation.

Noema should prefer such mechanisms where available and contractually supported.

⸻

33. Consumer-Side Idempotency

Where the external provider does not provide idempotency, the execution consumer may maintain a durable deduplication mechanism.

Conceptually:

Execution Consumer
       ↓
Durable Idempotency Store
       ↓
External Capability

However, consumer-side deduplication alone does not necessarily protect against all failure windows.

For example:

Consumer records "sent"
      ↓
External request
      ↓
Consumer crashes

or:

External request succeeds
      ↓
Consumer crashes before durable record

Therefore the exact consistency guarantees must be explicit.

⸻

34. Idempotency and External Authority

Noema’s local idempotency record does not automatically establish external business state.

For example:

Noema:
execution = COMPLETED

does not necessarily prove:

Provider:
payment = settled

The authoritative external system remains authoritative for its domain state.

Idempotency protects execution semantics.

It does not replace external reconciliation.

⸻

35. Reconciliation

Reconciliation is the process of determining the authoritative external outcome after an uncertain execution.

Conceptually:

Action
  ↓
UNKNOWN
  ↓
Query external system
  ↓
┌───────────────┬───────────────┐
│               │               │
FOUND           NOT FOUND       UNKNOWN
│               │               │
▼               ▼               ▼
Completed       Retry           Escalate /
                if safe         remain unknown

Reconciliation should be defined by the Action Contract where required.

⸻

36. Idempotency and Read-After-Write

A reconciliation query may itself observe stale or eventually consistent state.

Therefore:

Write
 ↓
Immediate Read

does not necessarily establish:

Write did not occur

The external capability’s consistency model must be considered.

Noema must not interpret temporary absence of an effect as definitive evidence unless the external system’s semantics support that conclusion.

⸻

37. Idempotency TTL

Some external providers retain idempotency keys only for a limited period.

Therefore the Action Contract may need to define:

idempotency_key_lifetime

If a retry occurs after the provider’s deduplication window has expired, the same key may no longer protect against duplication.

Noema must therefore not assume indefinite provider-side idempotency.

⸻

38. Expired Idempotency Keys

If an idempotency key has expired at the relevant external system, Noema may need to:

* reconcile external state
* create a new execution identity only after establishing safety
* block execution
* request human intervention
* use another provider-defined recovery mechanism

The system must not simply resend a consequential operation because the original key is no longer effective.

⸻

39. Idempotency and Concurrency

Two workers may attempt the same logical execution concurrently.

Example:

Worker A ──┐
           ├── exec_123
Worker B ──┘

The system must prevent both workers from producing duplicate external effects when the Action is intended to execute once logically.

Possible mechanisms include:

* durable execution ownership
* compare-and-set state transitions
* distributed locks where appropriate
* provider-side idempotency
* durable deduplication
* fencing tokens
* transactional coordination

The exact mechanism belongs to the execution architecture.

⸻

40. Locking Is Not Idempotency

A lock may prevent concurrent execution while it is held.

It does not solve crash recovery after the lock disappears.

For example:

Worker A acquires lock
      ↓
External request succeeds
      ↓
Worker A crashes
      ↓
Lock expires
      ↓
Worker B retries

Without idempotency or reconciliation, Worker B may duplicate the external effect.

Therefore:

Locking ≠ Idempotency

Locks may complement idempotency but must not substitute for it.

⸻

41. Fencing and Stale Workers

Long-running or partitioned workers may continue operating after losing execution ownership.

Where necessary, execution architecture may use fencing mechanisms so that stale workers cannot continue performing effects.

Conceptually:

Worker A
token = 7
Worker B
token = 8

The external execution boundary may reject operations carrying an obsolete token where the capability supports such semantics.

Fencing is an execution-safety mechanism distinct from idempotency.

⸻

42. Idempotency and Durable State Transitions

Noema’s local execution state should itself be durable.

For example:

READY
 ↓
EXECUTING
 ↓
UNKNOWN

must survive process failure.

Recovery can then reconstruct the logical execution identity and apply the appropriate idempotency or reconciliation procedure.

A process-local retry counter is insufficient for durable execution.

⸻

43. Idempotency and Event Replay

Event-driven systems may replay events.

For example:

event_123
event_124
event_123

Consumers must distinguish:

event replay

from:

new business operation

Where processing an event produces consequential external effects, the consumer must use appropriate event identity and idempotency semantics.

Event replay must not silently produce duplicate business effects.

⸻

44. Idempotent Event Consumption

A consumer may record processed event identity:

event_id
consumer_id
processing_status
result

However, the same critical failure window remains:

External Effect
      ↓
record processed event

If the external effect occurs and the processed-event record is lost, replay can still duplicate the effect.

Therefore event-consumer deduplication must be combined with appropriate external idempotency or transactional mechanisms where necessary.

⸻

45. Idempotency and Message Delivery

Message delivery semantics may be:

at-most-once
at-least-once
effectively-once

Noema should not infer business-level idempotency from transport-level delivery guarantees.

For example:

at-most-once delivery

does not guarantee successful execution.

And:

at-least-once delivery

does not imply duplicate business effects if the consumer and external capability are correctly idempotent.

The relevant property is the resulting business effect.

⸻

46. Idempotency and Side Effects

An Action may produce multiple side effects.

For example:

CREATE_ACCOUNT
   ├── account record
   ├── audit record
   └── notification

The idempotency semantics must account for the Action Contract boundary.

If these are separate graph Actions:

CREATE_ACCOUNT
CREATE_AUDIT_RECORD
SEND_NOTIFICATION

each may have its own execution identity.

If they are internal effects of one composite Action, the Action Contract must define their semantics.

Noema must not assume that one idempotency key automatically makes all underlying effects safe.

⸻

47. Hidden Side Effects

The prohibition against hidden Actions applies to idempotency as well.

If an Action Contract causes:

TRANSFER_FUNDS

and silently triggers:

SEND_NOTIFICATION

then duplicate transfer and duplicate notification semantics must both be defined.

Hidden side effects make idempotency analysis incomplete.

Therefore:

Consequential side effects must belong to an explicit Action Contract boundary or explicit Action Graph representation.

⸻

48. Idempotency and Composite Actions

A composite Action may contain multiple provider operations.

For example:

RENEW_CARD
    ├── deactivate old card
    ├── create replacement
    └── initiate delivery

The composite Action must define whether:

* the entire operation has one idempotency identity
* individual internal operations have independent identities
* the composite is resumable
* partial completion is possible
* compensation is available

The abstraction boundary must be explicit.

⸻

49. Idempotency and Partial Execution

Partial execution requires careful identity management.

Example:

A → COMPLETED
B → COMPLETED
C → UNKNOWN
D → NOT_STARTED

Recovery must not restart A and B merely because the graph is being resumed.

Instead:

A → already completed
B → already completed
C → reconcile/retry according to contract
D → execute only when dependencies permit

Each logical Action execution must therefore retain durable identity.

⸻

50. Idempotency and Compensation

Suppose:

A → B → C

C fails after A and B have completed.

A compensating graph may be:

C failed
  ↓
Compensate B
  ↓
Compensate A

The compensating Actions themselves require execution identities and idempotency semantics.

A compensation retry must not create multiple compensating effects.

Therefore:

Original Action
        +
Compensating Action

both require explicit execution semantics.

⸻

51. Idempotency and Human Intervention

Human intervention may occur after an uncertain operation.

For example:

Payment
  ↓
UNKNOWN
  ↓
Human Review
  ↓
Provider confirms payment completed

The human decision must not create a new payment operation merely because the original execution was uncertain.

The recovery path should reconcile the existing logical execution.

⸻

52. Idempotency and Approval

Approval does not create a new execution identity by itself.

For example:

CREATE_TRANSFER
      ↓
WAIT_FOR_APPROVAL
      ↓
APPROVED
      ↓
EXECUTE_TRANSFER

If the execution after approval is retried, it must retain the logical execution identity associated with the approved Action.

Approval is a governance condition.

It is not a substitute for idempotency.

⸻

53. Idempotency and Trust

Idempotency does not establish Trust.

For example:

Idempotency Key = valid

does not mean:

Actor = authorized

The execution path remains:

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

Idempotency operates within the execution layer.

It cannot bypass:

* Trust
* authorization
* policy
* approval
* Action Contract requirements

⸻

54. Idempotency and Stale Authorization

A retry must not automatically inherit execution authority if the governing Trust or authorization conditions have materially changed.

For example:

Trust = READY
      ↓
Action request
      ↓
UNKNOWN
      ↓
authorization revoked
      ↓
retry

The execution architecture must apply the applicable re-evaluation rules.

Idempotency establishes whether the retry is the same logical operation.

It does not establish that the operation remains authorized.

⸻

55. Idempotency and Action Graph Re-Evaluation

If a graph is materially revised, the execution architecture must distinguish:

retry existing Action

from:

execute revised Action

A graph revision must not accidentally reuse an idempotency identity belonging to semantically different execution.

Conversely, a retry of an unchanged Action must not accidentally receive a new identity.

⸻

56. Idempotency and Replanning

Replanning may occur after:

* capability failure
* external state change
* timeout
* policy change
* resource unavailability
* execution failure

Replanning does not automatically mean that previously attempted Actions can be forgotten.

The new graph must account for already completed or uncertain effects.

For example:

Graph v1
A → B → C
A completed
B unknown
Graph v2
A → D → C

Graph v2 must not simply execute A again.

The execution history remains part of the recovery context.

⸻

57. Idempotency and External State

External business state remains authoritative.

For example:

Noema:
payment execution UNKNOWN
Provider:
payment = COMPLETED

The provider state can resolve the uncertainty.

Conversely:

Noema:
execution record = COMPLETED
Provider:
payment = NOT_FOUND

may indicate reconciliation inconsistency requiring investigation.

The local execution record must not automatically override authoritative external state.

⸻

58. Idempotency and Time

Idempotency semantics may be time-bound.

Relevant temporal properties may include:

* key lifetime
* retry window
* provider deduplication window
* execution deadline
* Intent expiration
* authorization expiration
* Action Contract validity

Therefore:

same logical operation

does not necessarily mean:

safe to execute forever

Time-based constraints remain applicable.

⸻

59. Idempotency and Expiration

An expired Action must not become executable merely because its idempotency key remains available.

For example:

Intent expires
      ↓
Execution retry

The retry must first satisfy the applicable lifecycle requirements.

Idempotency preserves execution identity.

It does not override expiration.

⸻

60. Idempotency and Cancellation

Cancellation must be distinguished from idempotent retry.

For example:

Action executing
      ↓
Actor cancels Intent

If the external operation has already been submitted, cancellation does not necessarily mean:

external operation = cancelled

The execution architecture must determine whether:

* cancellation can prevent execution
* cancellation requires provider cancellation
* compensation is required
* outcome remains unknown

A cancelled logical Intent must not cause ambiguous duplicate behavior during recovery.

⸻

61. Idempotency and Timeout

Timeout is a transport/execution observation, not necessarily an external business outcome.

For example:

Request
  ↓
30 second timeout
  ↓
UNKNOWN

The provider may still process the operation.

Therefore:

timeout ≠ failure

and:

timeout ≠ safe retry

The Action Contract must define timeout and retry semantics.

⸻

62. Idempotency and Network Partitions

Network partitions create a fundamental uncertainty:

Noema ─────X───── Provider

Noema may not know whether the provider received or processed the request.

The correct model is:

Outcome = UNKNOWN

until sufficient evidence establishes the external state.

Idempotency and reconciliation exist specifically to handle this class of failure.

⸻

63. Idempotency and Provider Errors

Provider errors must be classified carefully.

A response such as:

HTTP 500

does not necessarily establish:

operation not performed

The provider may have completed the operation before returning the error.

Therefore retryability must be based on the Action Contract and provider semantics rather than transport status alone.

⸻

64. Idempotency and Client Errors

A deterministic validation rejection may establish that no operation occurred.

For example:

INVALID_ACCOUNT

may be non-retryable.

However, Noema must rely on provider semantics rather than assuming that every error class guarantees absence of effect.

The distinction should be represented explicitly in the Action Contract.

⸻

65. Idempotency State

An idempotency-aware execution may expose states such as:

UNSEEN
IN_PROGRESS
COMPLETED
FAILED
UNKNOWN
CONFLICT
EXPIRED

The exact state model belongs to the execution architecture.

These states describe execution identity and deduplication semantics.

They must not be confused with:

* Intent State
* Trust State
* Graph State
* Outcome State

⸻

66. Idempotency State vs Execution State

The dimensions may be represented separately.

For example:

Execution:
    state = UNKNOWN
Idempotency:
    key = exec_123
    status = IN_PROGRESS

or:

Execution:
    state = COMPLETED
Idempotency:
    status = COMPLETED

The exact implementation may combine these where appropriate, but their semantic meanings must remain clear.

⸻

67. Durable Idempotency Records

Idempotency state must be durable when it is required to survive:

* process restart
* worker replacement
* failover
* deployment
* replay
* recovery

An in-memory deduplication cache is insufficient for consequential execution unless the external system itself provides the authoritative idempotency guarantee.

⸻

68. Idempotency Record Retention

Retention must be long enough to cover the relevant duplicate and retry window.

Retention policy may depend on:

* provider key lifetime
* Action risk
* execution duration
* reconciliation period
* audit requirements
* legal or regulatory requirements
* business semantics

The exact retention policy is domain-specific.

A record should not be discarded while it is still required to prevent unsafe duplicate execution.

⸻

69. Idempotency Store Failure

The idempotency store itself may fail.

Noema must define whether an Action can execute when idempotency state cannot be established.

For consequential non-idempotent Actions, the safe behavior may be:

Idempotency state unavailable
        ↓
BLOCK

rather than:

Idempotency state unavailable
        ↓
execute anyway

The correct behavior depends on the Action Contract.

⸻

70. Idempotency Must Not Be Best Effort for Consequential Actions

For Actions whose duplicate execution could create material harm, idempotency cannot be merely an optional optimization.

Examples may include:

* financial transfers
* irreversible deletion
* resource creation with external cost
* credential issuance
* account state changes
* legally significant submissions

Where duplicate effects are materially consequential, the execution path must establish the required idempotency or reconciliation guarantees before execution.

⸻

71. Idempotency and Irreversible Actions

Irreversible Actions require particular care.

For example:

DELETE_ACCOUNT

may appear naturally idempotent if deleting an already-deleted account has no additional effect.

But the surrounding side effects may not be idempotent.

For example:

DELETE_ACCOUNT
    ↓
SEND_CONFIRMATION

Repeated execution could generate multiple notifications.

The entire Action Contract boundary must therefore be evaluated.

⸻

72. Idempotency and Resource Creation

Creation operations frequently require idempotency.

For example:

CREATE_ORDER

must not produce:

ORDER A
ORDER B

because a client retried after a timeout.

Where possible, the logical execution identity should be passed to the provider so that repeated attempts refer to the same creation request.

⸻

73. Idempotency and State Mutation

State mutation can be idempotent when expressed as a target state rather than an incremental operation.

For example:

SET_STATUS(ACTIVE)

may be naturally idempotent.

Whereas:

INCREMENT_BALANCE(100)

is generally not idempotent because repeating it changes state again.

The Action Contract should distinguish these semantics.

⸻

74. Idempotency and Incremental Operations

Incremental operations require special handling.

Examples:

INCREMENT_BALANCE
ADD_CREDIT
APPEND_RECORD
INCREASE_LIMIT

Repeated execution may produce repeated effects.

Such Actions generally require:

* unique operation identity
* provider-side deduplication
* transactional semantics
* reconciliation
* or another explicit mechanism

They must not be treated as naturally idempotent.

⸻

75. Idempotency and Notifications

Notifications require explicit semantic definition.

For some Intents:

SEND_NOTIFICATION

may be expected exactly once.

For others:

SEND_REMINDER

may legitimately repeat.

Therefore the relevant question is not:

Is SEND_NOTIFICATION idempotent?

but:

What constitutes the logical notification effect for this Action Contract?

The contract must define the intended semantics.

⸻

76. Idempotency and External APIs

When Noema invokes an external API, the integration should document:

* provider idempotency support
* idempotency-key format
* scope
* retention period
* duplicate response behavior
* conflict behavior
* timeout semantics
* reconciliation API
* eventual consistency
* retry guidance

These become part of the integration’s execution contract.

⸻

77. Capability-Level Idempotency

A capability may expose idempotency semantics.

For example:

payment.create
    supports idempotency = true

Another capability may expose:

payment.cancel
    supports idempotency = false

Capability discovery should therefore expose sufficient metadata for safe Action binding where applicable.

However:

Capability supports idempotency

does not itself establish that the Actor is authorized to invoke it.

⸻

78. Capability Contract Compatibility

An Action should not bind to a capability whose idempotency semantics are incompatible with the Action Contract.

For example:

Action Contract:
    retry may occur after UNKNOWN
Capability:
    no duplicate protection
    no reconciliation API

This combination may be unsafe.

The Action should therefore be:

UNAVAILABLE

or:

BLOCKED

unless another explicit recovery mechanism exists.

⸻

79. Idempotency and Graph Construction

Idempotency requirements may influence Action Graph construction.

For example:

CREATE_PAYMENT

may require:

GENERATE_EXECUTION_ID
      ↓
CREATE_PAYMENT

or may require:

CREATE_PAYMENT
      ↓
RECONCILE_PAYMENT

depending on the capability.

The graph should explicitly represent consequential recovery Actions where they belong at the graph level.

Idempotency itself remains an execution property and should not be confused with graph dependency semantics.

⸻

80. Idempotency and Execution Planning

The Execution Planner should account for Action idempotency characteristics.

It should not optimize execution by transforming:

single logical Action

into:

multiple independent external operations

unless the resulting semantics remain equivalent.

Likewise, parallel execution must not create duplicate logical execution identities.

⸻

81. Idempotency and Parallel Execution

If two graph paths independently converge on the same consequential Action, the planner must establish whether they represent:

one logical execution

or:

two distinct executions

For example:

A ──┐
    ├── CREATE_RESOURCE
B ──┘

must not result in two creation operations merely because two workers reach the same Action concurrently.

The graph and execution identity must make the intended semantics explicit.

⸻

82. Idempotency and Convergent Graphs

Convergence does not itself establish duplicate identity.

For example:

A ──┐
    ├── C
B ──┘

means C has multiple dependencies.

It does not mean:

execute C once per dependency

The graph semantics should establish one logical C execution unless explicitly defined otherwise.

This distinction is important for idempotency.

⸻

83. Idempotency and Iteration

Bounded iteration creates repeated attempts that may or may not represent the same logical Action.

For example:

POLL_STATUS
   ↓
WAIT
   ↓
POLL_STATUS

Each poll may be a distinct read operation.

By contrast:

CREATE_PAYMENT
   ↓
retry
   ↓
CREATE_PAYMENT

should normally represent one logical payment creation execution.

Iteration semantics must therefore distinguish:

repeated observation

from:

repeated consequential effect

⸻

84. Idempotency and Polling

Polling operations are generally read-oriented and may not require the same idempotency protections as state-changing Actions.

However, polling may itself have:

* rate limits
* provider costs
* quotas
* side effects

Therefore the relevant capability semantics still apply.

The execution system should not assume that all reads are free or consequence-free.

⸻

85. Idempotency and Long-Running Actions

A long-running Action may remain:

EXECUTING

for an extended period.

A timeout at the orchestration layer does not necessarily mean the external operation stopped.

Therefore recovery should preserve:

logical execution identity

and use provider status mechanisms where available.

Noema must not create a second long-running operation merely because the local process stopped waiting.

⸻

86. Idempotency and Asynchronous Providers

Some providers accept an operation and return:

accepted
operation_id = X

The actual effect occurs later.

The logical identity becomes:

Noema execution
      ↓
provider operation X
      ↓
asynchronous completion

The Action Contract should define whether retries:

* resubmit the operation
* query operation X
* use the original idempotency key
* resume monitoring

The provider operation identity may become part of the durable execution record.

⸻

87. Provider Operation Identity

An external provider may return its own operation identifier.

For example:

provider_operation_id = p_123

Noema should retain this identifier where it is necessary for reconciliation.

The identities are distinct:

Noema execution_id
Provider operation_id
Attempt_id
Idempotency_key

Each has a different semantic purpose.

⸻

88. Identity Mapping

Where external systems provide operation identities, Noema should maintain an explicit mapping.

Conceptually:

Noema Execution
    exec_123
        │
        ├── idempotency_key = K
        │
        ├── attempt = 4
        │
        └── provider_operation = P_456

This allows recovery to locate the authoritative external operation without creating another one.

⸻

89. Idempotency and Reconciliation Records

Reconciliation results should be durable.

For example:

UNKNOWN
   ↓
Provider lookup
   ↓
FOUND: COMPLETED

The result should become part of the execution history.

The system should not repeatedly perform reconciliation without respecting the applicable consistency and retry semantics.

⸻

90. Idempotency and Auditability

The execution history should make it possible to reconstruct:

1. logical execution identity
2. idempotency key
3. Action identity
4. Action Contract version
5. attempts
6. request fingerprints
7. external operation identities
8. responses
9. failures
10. unknown states
11. retries
12. reconciliation
13. final outcome

This permits operators to determine whether an apparent duplicate was:

* a legitimate retry
* duplicate delivery
* a graph error
* a provider duplicate
* an execution race
* a compensation
* a distinct intended Action

⸻

91. Idempotency and Observability

Operational observability should expose appropriate identifiers.

For example:

intent_id
intent_version
graph_version
action_id
execution_id
attempt_id
idempotency_key
provider_operation_id

These identifiers allow operators to trace execution without relying on natural-language descriptions.

Sensitive values should not be exposed unnecessarily.

⸻

92. Idempotency and Privacy

Idempotency keys should not contain unnecessary sensitive business information.

For example, a key should not ordinarily encode:

account number
card number
personal address
payment amount

in a directly reversible or human-readable form merely for convenience.

Identifiers should be opaque where possible.

Request fingerprints should likewise follow applicable security and privacy requirements.

⸻

93. Idempotency and Security

Idempotency mechanisms themselves can become security boundaries.

An attacker who obtains a valid idempotency key must not automatically gain authorization to execute the underlying Action.

Therefore:

Idempotency Key
    ≠
Authorization Credential

Keys should not be treated as bearer authorization tokens.

Authorization remains independently evaluated.

⸻

94. Key Reuse Attacks

The system should prevent unauthorized or accidental reuse of idempotency identities.

A key associated with:

Actor A
Action X

must not automatically be accepted for:

Actor B
Action X

unless the contract explicitly defines such scope.

Key scope and request fingerprinting should prevent semantic identity collisions.

⸻

95. Idempotency and Multi-Tenancy

In a multi-tenant system, idempotency scope must account for tenant boundaries where appropriate.

For example:

tenant_A / key_123

and:

tenant_B / key_123

may represent independent logical executions.

A global deduplication mechanism must not accidentally cause cross-tenant interference.

⸻

96. Idempotency and Actor Identity

Where the Action semantics are Actor-specific, the execution identity must preserve the Actor relationship.

For example:

Actor A
    ↓
Transfer
    ↓
Execution X

must not be confused with:

Actor B
    ↓
Transfer
    ↓
Execution X

unless the identity model explicitly establishes that equivalence.

Idempotency does not erase Actor semantics.

⸻

97. Idempotency and Authorization Changes

A duplicate request may arrive after authorization changes.

The system must distinguish:

same execution identity

from:

currently authorized to continue

The Action Contract and Trust architecture determine whether a retry can continue or requires re-evaluation.

Idempotency preserves identity.

It does not preserve obsolete authorization.

⸻

98. Idempotency and Policy Changes

Policy may change while an Action is waiting for execution.

For example:

Action created
   ↓
policy changes
   ↓
retry

The retry must follow the applicable policy and re-evaluation semantics.

The existence of an idempotency key does not exempt the execution from current governance requirements.

⸻

99. Idempotency and Contract Versioning

Action Contracts should be versioned where material execution semantics change.

For example:

Contract v1
    retry after UNKNOWN = prohibited
Contract v2
    retry after UNKNOWN = provider reconciliation

A recovery operation must know which contract semantics govern the existing execution.

A new contract must not silently reinterpret historical execution state without an explicit migration or re-evaluation mechanism.

⸻

100. Historical Reproducibility

The execution record should retain sufficient information to reconstruct which idempotency semantics applied at execution time.

This may include:

* Action Contract version
* provider capability version
* idempotency policy version
* retry policy version
* graph version
* Intent version
* execution timestamp

This prevents current configuration from rewriting the meaning of historical execution.

⸻

101. Idempotency and Model Behavior

An LLM must not determine idempotency semantics at execution time through unconstrained reasoning.

For example, a model must not decide:

"That payment probably failed, so retry."

The execution decision must be governed by:

Action Contract
+
execution state
+
idempotency semantics
+
authoritative external evidence
+
defined recovery policy

Models may assist in proposing or interpreting information.

They must not become the authority for consequential retry behavior.

⸻

102. No Model-Generated Idempotency Bypass

A model must not be able to:

* generate a new idempotency key to force a retry
* alter an existing idempotency identity
* suppress an idempotency conflict
* reinterpret UNKNOWN as FAILED
* bypass reconciliation
* execute a duplicate consequential Action directly

The execution layer must enforce these constraints independently of model behavior.

⸻

103. Deterministic Recovery

Given:

Execution State
Action Contract
Idempotency State
External Evidence
Retry Policy

the recovery decision should be deterministic where the governing rules require determinism.

For example:

UNKNOWN
+
provider supports lookup
+
lookup = COMPLETED

must resolve according to the defined recovery semantics rather than model discretion.

⸻

104. Idempotency Failure Modes

The engineering architecture should distinguish at least:

Duplicate Request

The same logical execution is submitted more than once.

→ Deduplicate or return existing execution state.

Key Conflict

The same key is used with materially different request semantics.

→ IDEMPOTENCY_CONFLICT

Unknown Outcome

The request may have been processed but no authoritative result is available.

→ UNKNOWN / reconciliation.

Key Expired

The provider no longer guarantees deduplication for the key.

→ Reconcile or block.

Idempotency Store Unavailable

Required local deduplication state cannot be established.

→ Apply Action Contract policy; potentially block.

Provider Does Not Support Idempotency

External capability cannot safely deduplicate repeated consequential requests.

→ Require reconciliation or another explicit safety mechanism.

Concurrent Execution

Multiple workers attempt the same logical execution.

→ Coordinate using durable execution ownership and/or provider idempotency.

⸻

105. Idempotency Error Model

Conceptual machine-readable errors include:

IDEMPOTENCY_CONFLICT
IDEMPOTENCY_KEY_EXPIRED
IDEMPOTENCY_STATE_UNAVAILABLE
DUPLICATE_EXECUTION
RECONCILIATION_REQUIRED
RECONCILIATION_UNAVAILABLE
NON_IDEMPOTENT_RETRY
UNKNOWN_EXTERNAL_OUTCOME
EXECUTION_OWNERSHIP_CONFLICT

Human-readable descriptions may accompany these codes.

Machine-readable semantics remain canonical.

⸻

106. Idempotency Result

Conceptually:

IdempotencyResult {
    status
    key
    scope
    execution_id
    existing_result
    conflict
    retry_allowed
    reconciliation_required
}

Possible statuses may include:

NEW
DUPLICATE
IN_PROGRESS
COMPLETED
FAILED
UNKNOWN
CONFLICT
EXPIRED
BLOCKED

The exact schema remains subject to the execution architecture.

⸻

107. Canonical Idempotent Execution Flow

A consequential Action may follow:

Action Ready
      ↓
Resolve Execution Identity
      ↓
Resolve Idempotency Semantics
      ↓
Check Existing Execution
      ↓
┌───────────────┬────────────────┐
│               │                │
NEW           EXISTING          CONFLICT
│               │                │
▼               ▼                ▼
Execute       Reconcile /      Block
              return state
│
▼
External Effect
│
├── Success ────────────────► Persist Result
│
├── Confirmed Failure ──────► Persist Failure
│
└── Unknown ────────────────► Reconcile / Retry

The precise transitions depend on the Action Contract.

⸻

108. Recovery Flow After Crash

Conceptually:

Process Crash
      ↓
Recover Durable Execution
      ↓
Load Execution Identity
      ↓
Load Idempotency State
      ↓
Determine Last Known State
      ↓
┌──────────────────────────────┐
│                              │
COMPLETED                   UNKNOWN
│                              │
▼                              ▼
Resume downstream         Reconcile / retry
only                     according to contract

The recovery system must not restart the entire graph blindly.

⸻

109. Recovery Flow After Duplicate Delivery

Message Received
      ↓
Resolve execution identity
      ↓
Existing execution?
   ┌──────┴──────┐
   No            Yes
   │              │
   ▼              ▼
Start          Inspect state
execution         │
                  ▼
             Continue /
             return state /
             deduplicate

Duplicate delivery must not create a new logical execution unless the semantics explicitly define it as a new Action.

⸻

110. Recovery Flow After Unknown Outcome

UNKNOWN
   ↓
Is provider reconciliation available?
   │
 ┌─┴───────────────┐
 No                Yes
 │                  │
 ▼                  ▼
Is safe retry      Query provider
defined?              │
 │                 ┌──┼──┐
No                │  │  │
 │                │  │  │
▼               DONE NOT_FOUND UNKNOWN
BLOCK              │     │      │
                   ▼     ▼      ▼
                COMPLETE RETRY  WAIT/
                         if safe ESCALATE

The exact state transitions are contract-specific.

⸻

111. Idempotency and Completion

A logical execution should be considered complete only when the applicable Action Contract establishes completion.

For example:

Provider accepted request

may not equal:

Action completed

if the operation is asynchronous.

The idempotency layer must therefore preserve the distinction between:

* request accepted
* execution in progress
* effect completed
* outcome unknown

⸻

112. Idempotency and Outcome

The final Outcome must accurately reflect the execution history.

For example:

Execution:
    UNKNOWN

must not become:

Outcome:
    SUCCESS

merely because a retry was attempted.

Likewise:

Execution:
    COMPLETED

must not become:

FAILED

because a duplicate attempt returned an error after the original execution had already completed.

The logical execution result remains authoritative according to the defined semantics.

⸻

113. Duplicate After Completion

Suppose:

Attempt 1
    ↓
COMPLETED

and then:

Attempt 2
    ↓
same idempotency key

The second attempt should not create another effect.

Possible response:

return existing result

or:

return COMPLETED

according to the provider and consumer contract.

The second attempt is a duplicate, not a new logical Action.

⸻

114. Duplicate While In Progress

If:

Execution = IN_PROGRESS

and another worker receives the same execution identity, it should not automatically execute the Action again.

Possible behavior:

wait
observe
resume
return current state

depending on the execution architecture.

Concurrent ownership must be explicit.

⸻

115. Duplicate After Failure

A confirmed failure may permit retry if:

* the failure is retryable
* no external effect occurred, or
* the external capability provides safe idempotency
* the Action Contract permits retry

A failure must not automatically create a new execution identity.

Retrying the same logical Action should preserve the execution identity when appropriate.

⸻

116. Confirmed No-Effect Failure

If the provider establishes:

request rejected before execution

then a retry may be safe without reconciliation.

However, the evidence supporting:

no effect occurred

must be sufficient for the Action Contract.

Transport failure alone may not establish this.

⸻

117. Idempotency and Side-Effect Ordering

When an Action contains multiple effects, their ordering can affect recovery.

For example:

Create resource
      ↓
Send notification

If resource creation succeeds and notification fails, retrying the entire composite operation may duplicate the resource.

The graph or Action Contract must therefore define whether recovery resumes at:

Send notification

rather than:

Create resource

This is a major reason to preserve durable per-Action execution state.

⸻

118. Idempotency and Action Granularity

Action granularity affects recoverability.

An overly broad Action:

PROCESS_CUSTOMER_REQUEST

may conceal multiple external effects.

A more explicit graph may expose:

CREATE_ACCOUNT
UPDATE_PROFILE
SEND_NOTIFICATION

This allows each consequential effect to have explicit identity and recovery semantics.

However, decomposition must respect the actual Action Contract boundaries.

⸻

119. Idempotency and Atomic External APIs

If a provider offers an atomic operation with built-in idempotency, Noema may preserve that operation as a single Action.

For example:

CREATE_TRANSFER

may be one provider operation with:

idempotency_key

The graph does not need to expose provider-internal implementation steps merely to satisfy idempotency.

The contract boundary must remain explicit.

⸻

120. Idempotency and Non-Atomic Providers

If a provider requires multiple calls to achieve one logical Action:

create resource
update resource
confirm resource

the integration must define recovery semantics for each call.

Noema must not claim that the composite operation is idempotent merely because the overall Action has one identifier.

The internal provider operations may require their own identities.

⸻

121. Idempotency and Exactly-Once Intent

An Actor’s Intent may semantically require one effect.

For example:

"Pay this invoice once."

This semantic requirement should be represented in the relevant Intent and Action semantics.

The engineering implementation may achieve it through:

* provider idempotency
* unique business identifiers
* transactional constraints
* reconciliation
* durable execution

The system must not equate the semantic requirement with an assumption that exactly-once transport exists.

⸻

122. Business Uniqueness vs Idempotency

Business systems may enforce uniqueness independently.

For example:

invoice_id = INV-123

may permit only one payment.

This can provide a business-level deduplication mechanism.

However:

business uniqueness

and:

execution idempotency

remain distinct concepts.

Noema should use authoritative business uniqueness where available but must preserve explicit execution identity.

⸻

123. Idempotency and Natural Business Keys

A business key may serve as an idempotency identity if the Action Contract explicitly defines it that way.

For example:

invoice_id

could identify one logical payment.

But the system must establish:

* uniqueness
* scope
* lifecycle
* reuse rules
* conflict semantics

It must not assume that every business identifier is automatically safe as an idempotency key.

⸻

124. Idempotency and Request Fingerprinting

Where a provider supports idempotency keys, Noema should preserve enough information to detect semantic mismatch.

For example:

key = K
amount = 50,000
recipient = A

followed by:

key = K
amount = 75,000
recipient = A

must not silently produce ambiguous behavior.

The second request should be rejected as a conflict or handled according to provider-defined semantics.

⸻

125. Idempotency and Serialization

The representation used to generate a request fingerprint must be canonical where applicable.

Semantically equivalent requests should not accidentally produce different identities merely because of irrelevant serialization differences.

For example:

{"amount":50000,"currency":"NGN"}

and:

{"currency":"NGN","amount":50000}

may be semantically equivalent even though their textual ordering differs.

Canonicalization rules belong to the implementation and contract.

⸻

126. Idempotency and Schema Evolution

Changes to Action input schemas may affect request fingerprints.

A contract version should therefore establish how idempotency identity behaves across schema evolution.

A historical execution must not become a different logical operation merely because the serialization schema changed.

⸻

127. Idempotency and Versioned Contracts

Conceptually:

Execution
    ↓
Action Contract v3
    ↓
Idempotency semantics v2

must remain reconstructible after later versions are deployed.

Current configuration must not retroactively redefine historical execution.

⸻

128. Idempotency Testing

Engineering tests should include failure injection at the critical execution boundaries.

At minimum:

Before request
After request transmission
After provider effect
Before response receipt
After response receipt
Before local persistence
After local persistence
During recovery
During duplicate delivery
During concurrent execution

The objective is to establish that duplicate effects cannot occur under supported guarantees.

⸻

129. Idempotency Test Cases

Representative tests include:

Retry After Timeout

request sent
response lost
retry

Expected:

one external effect

where the contract guarantees idempotency.

Duplicate Message

same execution message × 2

Expected:

one logical execution

Concurrent Workers

worker A + worker B
same execution

Expected:

one external effect

where the architecture guarantees it.

Key Conflict

same key
different request

Expected:

IDEMPOTENCY_CONFLICT

Provider Reconciliation

UNKNOWN
provider = COMPLETED

Expected:

reconciled completion

Provider Reconciliation Not Found

UNKNOWN
provider = NOT_FOUND

Expected behavior according to the Action Contract, potentially retry.

⸻

130. Failure Injection

Idempotency cannot be validated only through successful-path tests.

The engineering test suite should intentionally introduce:

* process crashes
* network timeouts
* dropped responses
* duplicate messages
* delayed responses
* provider errors
* worker races
* storage failures
* provider reconciliation delays
* expired idempotency keys

The system should demonstrate safe behavior under these conditions.

⸻

131. Property-Based Idempotency Testing

Where appropriate, engineering tests may assert the invariant:

Repeated execution attempts
        ↓
same logical execution
        ↓
no unintended additional effect

across generated failure sequences.

The exact property depends on the Action Contract.

Idempotency should therefore be tested as a behavioral invariant rather than only as an implementation detail.

⸻

132. Idempotency Metrics

Operational metrics may include:

* duplicate execution attempts
* idempotency conflicts
* retries
* unknown outcomes
* reconciliation attempts
* reconciliation successes
* reconciliation failures
* provider idempotency failures
* expired idempotency keys
* concurrent execution conflicts
* blocked non-idempotent retries

These metrics help identify systemic execution reliability problems.

⸻

133. Idempotency Alerts

Alerts may be appropriate for:

* repeated unknown outcomes
* high idempotency conflict rates
* provider deduplication failures
* reconciliation failures
* idempotency store outages
* excessive retries
* expired keys during active recovery
* concurrent execution races
* evidence of duplicate external effects

Alerting thresholds should be domain-specific.

⸻

134. Operational Investigation

When a suspected duplicate effect occurs, operators should be able to trace:

Intent
  ↓
Intent Version
  ↓
Graph Version
  ↓
Action
  ↓
Execution
  ↓
Idempotency Key
  ↓
Attempts
  ↓
Provider Operation
  ↓
External Outcome

This trace should not depend on model-generated natural-language explanations.

Structured execution identity is canonical.

⸻

135. Idempotency and Audit History

The audit history should preserve material events such as:

execution.created
execution.started
execution.attempted
execution.unknown
execution.retried
execution.reconciled
execution.completed
execution.failed
idempotency.conflict
idempotency.duplicate_detected

These events are illustrative and may be formalized separately.

The important requirement is reconstructibility.

⸻

136. Idempotency and No Hidden Retry

A retry must be observable as an explicit execution event.

Noema must not silently repeat a consequential external Action without recording:

* why the retry occurred
* which execution identity was reused
* which retry policy permitted it
* which idempotency mechanism protected it

This supports operational and forensic analysis.

⸻

137. Idempotency and No Hidden Compensation

Likewise, compensating execution must be explicit.

A system must not silently issue a compensating external operation merely because an Action failed unless the applicable recovery semantics explicitly require it.

Compensation has its own execution identity and idempotency requirements.

⸻

138. Idempotency and Execution Authority

Idempotency protects the execution boundary.

It does not grant execution authority.

The canonical sequence remains:

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
Idempotency / Recovery Controls
  ↓
External Capability
  ↓
Outcome

The precise ordering of internal execution checks may differ, but the authority boundaries must remain intact.

⸻

139. Idempotency and the Action Graph Invariants

The Action Graph requires that:

* Actions be explicit
* dependencies be explicit
* failure behavior be explicit
* retries be contractually defined
* unknown outcomes remain unknown
* partial execution remain explicit

Idempotency operationalizes these principles at execution time.

It therefore supports, but does not replace, the Action Graph.

⸻

140. Idempotency and Durable Execution Invariants

Durable execution assumes:

* execution state survives process failure
* work may resume after interruption
* retries are expected
* external effects may outlive local processes
* outcomes may be uncertain

Idempotency is therefore a foundational execution property rather than an optional optimization.

⸻

141. Idempotency and Failure Recovery

Failure recovery must preserve logical execution identity.

For example:

Failure
  ↓
Recovery
  ↓
Same logical Action
  ↓
Same idempotency semantics

Recovery must not accidentally transform:

retry

into:

new consequential Action

unless the architecture explicitly defines the operation as a new Action.

⸻

142. Idempotency and State Machine Discipline

Execution state transitions must be explicit.

For example:

READY
  ↓
EXECUTING
  ↓
UNKNOWN
  ↓
RECONCILING
  ↓
COMPLETED

A model or operator must not arbitrarily transition:

UNKNOWN → COMPLETED

without the evidence required by the governing contract.

Likewise:

UNKNOWN → RETRY

requires a defined recovery rule.

⸻

143. Idempotency and Unknown as a First-Class State

The distinction is foundational:

FAILED

means the applicable semantics establish failure.

UNKNOWN

means the system cannot yet establish the external outcome.

This distinction prevents unsafe retries and false failure reporting.

⸻

144. Idempotency and Execution Outcome

The final Outcome should represent what actually happened, not merely what the local process attempted.

For example:

Attempt 1 = UNKNOWN
Attempt 2 = duplicate
Provider = COMPLETED

The logical Outcome is:

COMPLETED

not:

PARTIALLY_COMPLETED

merely because multiple attempts existed.

⸻

145. Idempotency and Evidence

Evidence used to establish execution state should be retained where necessary.

Evidence may include:

* provider response
* provider operation status
* reconciliation result
* durable execution record
* idempotency response
* external transaction identifier

Evidence provenance supports reconstruction of why an execution was considered complete or unresolved.

⸻

146. Idempotency and External Evidence Authority

Not all evidence has equal authority.

For example:

local timeout

does not establish:

provider operation failed

whereas:

provider status = FAILED

may establish it.

The execution architecture should distinguish observations from authoritative external state.

⸻

147. Idempotency and Provider Semantics

Provider documentation and integration contracts must be treated as authoritative for provider-specific idempotency behavior.

Noema must not assume that:

same key

always means:

same result

unless the provider contract establishes that behavior.

Provider-specific semantics must be encoded in the integration contract.

⸻

148. Idempotency and Capability Replacement

A capability may be replaced during an execution lifecycle.

For example:

Provider A
   ↓
unavailable
   ↓
Provider B

Noema must not blindly reuse the same idempotency key against Provider B if the key’s scope is provider-specific.

The execution identity and provider idempotency identity may need to remain distinct.

The recovery policy must explicitly determine whether the operation can safely move to another capability.

⸻

149. Cross-Provider Idempotency

When an Action can move between providers, the system should distinguish:

logical Action execution

from:

provider-specific idempotency identity

For example:

Logical Execution = E1
Provider A:
    key = A:E1
Provider B:
    key = B:E1

Whether such migration is safe depends on authoritative reconciliation and business semantics.

Noema must not assume that two providers share an idempotency namespace.

⸻

150. Idempotency and Graph Replanning Across Providers

If a provider fails after possibly performing an operation, switching providers may create a duplicate effect.

For example:

Provider A
    ↓
UNKNOWN
Provider B
    ↓
execute

is unsafe unless Noema can establish that Provider A did not perform the operation or the business domain guarantees uniqueness.

Therefore:

UNKNOWN Provider A
        ↓
Provider B

requires explicit reconciliation or another defined safety mechanism.

⸻

151. Idempotency and Resource Ownership

Idempotency records and execution records must have clear ownership.

The engineering architecture should define which component owns:

* logical execution identity
* idempotency state
* provider operation identity
* reconciliation state
* retry state

No component should independently create conflicting execution identities for the same logical Action.

⸻

152. Idempotency and Component Boundaries

A typical boundary may be:

Execution Orchestrator
        ↓
Action Contract
        ↓
Execution Adapter
        ↓
Idempotency Adapter
        ↓
Provider

The exact component structure belongs to engineering/components.md.

The important requirement is that idempotency semantics remain explicit at the boundary where external effects occur.

⸻

153. Idempotency and Persistence

Durable persistence should preserve the minimum information necessary to resume safely.

At minimum, where applicable:

execution_id
action_id
idempotency_key
attempts
current_state
contract_version
provider_operation_id
last_known_external_state
retry_count
timestamps

The exact persistence schema is implementation-specific.

⸻

154. Idempotency and Transaction Boundaries

Local database transactions may establish atomicity among local records.

They do not automatically establish atomicity with an external provider.

For example:

BEGIN TRANSACTION
record execution
COMMIT
external request

does not mean the external request is transactional with the local database.

Similarly:

external effect

cannot necessarily be rolled back by a local database transaction.

The architecture must explicitly address the local/external transaction boundary.

⸻

155. Transactional Outbox Relationship

Where applicable, an outbox pattern may help guarantee that a durable execution instruction is not lost between local state mutation and message publication.

However:

transactional outbox

does not itself guarantee external idempotency.

The downstream consumer must still safely handle duplicate delivery and external effects.

Therefore:

Outbox
+
Idempotent Consumer

may be required together.

⸻

156. Idempotency and Inbox Processing

An inbox or processed-message mechanism may record incoming execution requests.

This can prevent repeated processing of identical messages.

However, as with other local deduplication mechanisms, it does not automatically eliminate the external effect failure window.

For consequential operations:

Inbox deduplication
+
External idempotency / reconciliation

may both be required.

⸻

157. Idempotency and Exactly-Once Illusions

Noema must avoid architectural claims such as:

“The worker executes each Action exactly once.”

unless that property can actually be established across the relevant execution boundary.

A more precise model is:

Execution may be attempted multiple times.
Logical execution identity remains stable.
External effects are protected by defined idempotency/reconciliation semantics.

This accurately represents distributed-system failure behavior.

⸻

158. Idempotency and Operational Truth

The engineering system should distinguish:

attempt count

from:

effect count

For example:

attempts = 3
external_effects = 1

is a valid and expected outcome for a retry after uncertain response.

The existence of multiple attempts is not evidence of multiple business effects.

⸻

159. Idempotency and Audit Truth

The audit record should preserve both:

what Noema attempted

and:

what the external system established happened

This distinction is essential for forensic accuracy.

For example:

Attempt 1: request sent
Attempt 1: response unknown
Attempt 2: duplicate detected
Provider: completed

provides a more accurate history than:

Payment succeeded.

alone.

⸻

160. Idempotency and Observability Without Chain-of-Thought

Noema does not require private model reasoning to establish why an Action was retried.

It requires structured operational provenance:

retry_policy = PROVIDER_IDEMPOTENT
retry_reason = TIMEOUT
attempt = 2
idempotency_key = K
contract_version = 3

This is sufficient for execution auditability without exposing hidden model reasoning.

⸻

161. Canonical Idempotency Invariants

Invariant 1

A retry of the same logical Action must preserve its execution identity.

Invariant 2

A consequential Action must not be retried blindly after an unknown outcome.

Invariant 3

UNKNOWN must not silently become FAILED.

Invariant 4

UNKNOWN must not silently become COMPLETED.

Invariant 5

Idempotency does not grant authorization.

Invariant 6

An idempotency key is not itself an authorization credential.

Invariant 7

The same idempotency identity must not silently accept materially different request semantics.

Invariant 8

Duplicate delivery must not automatically create a new consequential execution.

Invariant 9

Idempotency state required for safe execution must be durable.

Invariant 10

Local idempotency state does not replace authoritative external business state.

Invariant 11

Provider-specific idempotency semantics must be explicit.

Invariant 12

Idempotency does not imply atomicity.

Invariant 13

Idempotency does not imply exactly-once transport.

Invariant 14

Compensating Actions require their own execution and idempotency semantics.

Invariant 15

A material Intent change must not silently reuse the execution identity of the previous semantic Intent.

Invariant 16

A material Action Contract change must not silently reinterpret historical execution.

Invariant 17

A stale worker must not be able to create an unintended duplicate effect.

Invariant 18

A graph retry must not restart already completed consequential Actions without applying their execution identities.

Invariant 19

Model-generated reasoning must not override deterministic retry and idempotency policy.

Invariant 20

Idempotency mechanisms must preserve the distinction between logical execution and individual attempts.

⸻

162. Canonical Mental Model

Idempotency can be reduced to six questions:

1. What logical Action is being executed?
2. What identifies that logical execution?
3. Has this execution already been attempted or completed?
4. What is known about the external effect?
5. Can the Action safely be retried or must it be reconciled?
6. What evidence establishes the final outcome?

Which produces:

Logical Action
      ↓
Execution Identity
      ↓
Idempotency Identity
      ↓
Execution Attempt
      ↓
External Effect
      ↓
Known / Unknown Outcome
      ↓
Retry / Reconcile / Complete

⸻

163. Relationship to Failure Recovery

The relationship between idempotency and failure recovery is:

Failure
   ↓
Determine execution state
   ↓
Determine external-effect uncertainty
   ↓
Apply idempotency semantics
   ↓
Retry / Reconcile / Compensate / Block
   ↓
Persist resulting state

Failure recovery determines what must happen after failure.

Idempotency determines whether repeating the logical Action is safe.

The two concerns are distinct but inseparable for consequential execution.

⸻

164. Relationship to Durable Execution

The relationship is:

Durable Execution
        ↓
Execution survives interruption
        ↓
Execution may resume
        ↓
Retries may occur
        ↓
External outcome may be uncertain
        ↓
Idempotency protects repeated execution

Durability without idempotency can result in duplicate external effects.

Idempotency without durable execution can lose the identity required to perform safe recovery.

Both therefore form part of Noema’s execution reliability model.

⸻

165. Relationship to Action Graph

The Action Graph establishes:

which Actions exist

and:

how Actions depend on one another

Idempotency establishes:

how repeated execution of those Actions behaves

Therefore:

Action Graph
    ↓
Action identity
    ↓
Action Contract
    ↓
Execution identity
    ↓
Idempotency
    ↓
External effect

The Action Graph must not itself be treated as an idempotency mechanism.

⸻

166. Relationship to Action Contracts

The Action Contract is the primary boundary for defining:

* whether an Action is idempotent
* how retries work
* what constitutes a duplicate
* how unknown outcomes are resolved
* what external identifiers are returned
* whether reconciliation is possible
* what failure classes permit retry

Therefore:

Idempotency semantics must be explicit at the Action Contract boundary.

⸻

167. Relationship to Outcome

Outcome records what actually happened.

Idempotency exists to make that outcome reliable despite repeated execution attempts and uncertain transport.

Therefore:

Idempotency
      ↓
Reliable execution semantics
      ↓
Outcome

Idempotency does not itself determine whether an Action succeeded.

It determines how the system safely establishes that result.

⸻

168. Canonical Execution Principle

Noema should treat every consequential external Action as potentially subject to:

duplicate delivery
retry
replay
timeout
process failure
network partition
unknown response
concurrent execution
recovery

The Action must therefore have explicit semantics for these conditions.

The engineering principle is:

Assume execution may be repeated; design the external effect so repetition is either safe, deduplicated, or explicitly prevented.

⸻

169. Final Definition

Idempotency is Noema’s engineering property for preserving the intended semantics of a logical Action when execution is retried, replayed, duplicated, recovered, or otherwise attempted more than once.

Its central invariant is:

Noema must never rely on the assumption that a consequential Action is executed only once. It must preserve logical execution identity and use explicit idempotency, reconciliation, transactional, or compensating mechanisms so that repeated execution attempts cannot produce unintended duplicate effects.

The fundamental distinction is:

Logical Execution
        ≠
Execution Attempt
        ≠
External Effect
        ≠
Execution Outcome

A robust Noema execution path therefore remains:

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
Execution Identity
   ↓
Idempotency / Recovery Semantics
   ↓
Execution Attempt
   ↓
External Capability
   ↓
Reconciliation where required
   ↓
Outcome

And the governing rule is:

Retry does not mean new Action.
Unknown does not mean failed.
Timeout does not mean no effect.
Duplicate delivery does not mean duplicate business operation.
Idempotency does not mean authorization.
Idempotency does not mean exactly-once transport.
Idempotency means that the system preserves the intended
logical effect despite the realities of distributed execution.