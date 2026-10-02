> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Idempotency

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/idempotency.md

⸻

1. Definition

Idempotency is the execution property that allows the same semantic Action to be attempted multiple times without producing unintended additional effects beyond the semantics of the original Action.

Idempotency exists because distributed execution cannot reliably assume that a request is processed exactly once.

The canonical principle is:

Same semantic Action
+
Repeated execution attempts
=
No unintended duplicate effect

Idempotency protects the boundary between repeated delivery and consequential effect. It does not establish whether the original effect actually occurred. That requires execution evidence and, where necessary, State Reconciliation.

⸻

2. Core Principle

Noema must assume that consequential Actions may be delivered or attempted more than once.

Therefore:

delivery
≠
execution
≠
effect

A network retry can cause the same Action Contract to reach a consumer multiple times.

The consumer must distinguish:

new semantic Action

from:

another execution attempt for an existing semantic Action

The distinction must be deterministic and based on explicit execution identity rather than model interpretation.

⸻

3. Why Idempotency Exists

Consider:

Noema
  ↓
Payment Service
  ↓
Payment Provider

Noema sends:

charge ₦100,000

The provider processes the charge successfully.

But the response is lost:

Provider → SUCCESS
Provider → X
Payment Service → timeout

Noema cannot safely assume the charge failed.

A naive retry may produce:

₦100,000 charge
+
₦100,000 charge
=
₦200,000 charged

Idempotency prevents the retry from becoming an unintended second semantic charge.

However, idempotency alone does not establish whether the first charge occurred. If execution state is unknown, reconciliation remains required.

⸻

4. Idempotency Is Not Exactly-Once Delivery

These concepts must remain separate.

Exactly-once delivery means:

message is delivered exactly once

Idempotent execution means:

repeated delivery does not create unintended repeated effects

Noema should not depend on universal exactly-once delivery.

The preferred distributed execution model is:

At-least-once delivery
+
Idempotent execution
+
Durable execution state
+
Reconciliation

Exactly-once delivery is a transport property.

Idempotency is a semantic execution property.

⸻

5. Idempotency Is Not Deduplication Alone

Deduplication asks:

Have I seen this request before?

Idempotency asks:

If I see this semantic Action again, can I safely process the repeated attempt without creating an unintended additional effect?

A deduplication table may be one implementation mechanism.

It is not the complete semantic guarantee.

A system can detect duplicate messages while still producing duplicate downstream effects if the duplicate protection does not extend to the actual side effect.

⸻

6. Idempotency Belongs to Execution

Idempotency is primarily an execution concern.

The broader execution model is:

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
Idempotency
   ↓
Verification / Reconciliation
   ↓
Outcome

Intent resolution should not need to know how a payment provider handles retries.

The execution boundary must enforce the appropriate idempotency semantics.

Idempotency does not replace Trust, Action Contracts, execution validation, or verification.

⸻

7. Semantic Identity

The central question is:

What makes two execution attempts the same semantic Action?

Noema must distinguish:

Action identity

from:

Execution attempt identity

Example:

Action:
refund_payment(payment_123)
Execution:
attempt_1
Execution:
attempt_2

Both attempts may belong to the same semantic Action.

The execution attempts are distinct events. The Action Instance remains the semantic operation being attempted.

⸻

8. Action Identity vs Execution Identity

Conceptually:

Action Instance
      │
      ├── Execution Attempt 1
      ├── Execution Attempt 2
      └── Execution Attempt 3

The attempts have distinct execution identities.

They share the semantic identity of the Action Instance when they represent retries of the same Action.

Therefore:

Action identity
≠
execution attempt identity

and:

same Action
→
multiple attempts may exist

⸻

9. Intent Version and Semantic Identity

For consequential execution, semantic identity must remain linked to the exact immutable Intent Object version from which the Action was derived.

Conceptually:

Intent v7
   ↓
Action Instance A123
   ↓
Idempotency Identity K123
   ↓
Execution Attempt 1
Execution Attempt 2

If a material change occurs to the Intent, that change creates a new Intent version rather than silently changing the existing semantic Action.

A new semantic Action may therefore require a new idempotency identity.

Historical execution attempts must continue to reference the original Intent version.

⸻

10. Idempotency Key

An idempotency key identifies the semantic execution request within a defined scope.

Example:

idempotency_key:
idem_01JABC...

The key should be:

* unique within its intended scope
* stable across retries
* bound to the intended Action
* resistant to accidental collision
* non-secret
* traceable to the corresponding execution identity

The exact key format is implementation-specific.

⸻

11. Idempotency Key Is Not a Random Request ID

A request ID may identify:

HTTP request #1

while the idempotency key identifies:

the semantic Action being requested

Therefore:

request_id_1 ≠ request_id_2

may still represent:

idempotency_key_X

and therefore the same semantic Action.

Request correlation and semantic idempotency must remain separate concepts.

⸻

12. Key Stability

If a retry generates a new idempotency key:

Attempt 1:
K1
Attempt 2:
K2

the consumer cannot necessarily determine that both attempts represent the same semantic Action.

Correct retry semantics:

Attempt 1:
K1
Attempt 2:
K1

The key remains stable while execution attempt identity changes.

⸻

13. Key Scope

An idempotency key must have a defined scope.

Possible scopes include:

* tenant
* consumer
* Action type
* resource
* Action Contract
* integration
* workflow
* environment
* global

For example:

(tenant_id, action_type, idempotency_key)

may define uniqueness.

The scope must be explicit and must be compatible with the authority and isolation boundaries of the Action.

⸻

14. Key Collision

Two genuinely different Actions must not accidentally share an idempotency key within the same scope.

Example:

refund_payment(payment_123)

and:

refund_payment(payment_456)

must not be treated as the same operation.

Therefore the semantic Action identity and all parameters relevant to its effect must be bound to the idempotency identity.

⸻

15. Parameter Binding

An idempotency record should associate the key with canonical Action parameters.

Conceptually:

idempotency_key = K123
action = refund_payment
parameters = {
    payment_id: payment_123,
    amount: 100000
}

If the same key arrives with materially different parameters:

K123
payment_id = payment_456

the consumer should reject the request or otherwise deterministically refuse reuse according to the Action Contract.

It must not silently reinterpret the existing idempotency identity as a different Action.

⸻

16. Idempotency Record

Conceptually:

IdempotencyRecord {
    key
    scope
    action_identity
    action_version
    intent_version
    parameters_hash
    execution_id
    status
    outcome_reference
    created_at
    expires_at
}

The exact storage representation is implementation-specific.

The record must preserve sufficient identity to determine whether a subsequent request represents the same semantic Action.

⸻

17. Idempotency Lifecycle

A typical lifecycle is:

NEW
 ↓
PROCESSING
 ↓
COMPLETED

Possible terminal or control states include:

FAILED
UNKNOWN
EXPIRED

The exact lifecycle depends on the execution semantics.

Importantly, UNKNOWN means the system cannot establish the actual execution result. It must not be silently converted into success or failure merely because the idempotency record exists.

⸻

18. First Request

The first request creates or atomically claims the idempotency record:

K123
   ↓
not found
   ↓
atomic create / claim
   ↓
execute

The consumer associates the semantic Action with that identity before allowing consequential execution to proceed.

⸻

19. Duplicate Request While Processing

Suppose:

K123 → PROCESSING

and another request arrives:

K123

The consumer must not blindly execute again.

Possible deterministic behavior includes:

return PROCESSING

or:

wait for existing execution

or:

return current execution state

depending on the protocol.

The duplicate request must converge on the existing semantic execution rather than create an unintended independent execution.

⸻

20. Duplicate Request After Success

Suppose:

K123
    ↓
SUCCESS

A later request with:

K123

should normally return or reference the existing result rather than execute the Action again.

Conceptually:

K123
 ↓
existing execution
 ↓
existing verified result

Returning a historical result is not a new execution and therefore may not require the same current execution authorization, provided the protocol permits historical result retrieval.

⸻

21. Duplicate Request After Failure

This requires explicit semantics.

A failed Action may be:

retryable

or:

non-retryable

Therefore a consumer must define whether reuse of the same idempotency identity means:

return original failure

or:

attempt another execution attempt for the same semantic Action

The semantics must not be ambiguous.

A retry does not automatically create a new Action.

⸻

22. Retry Semantics

A retry should normally preserve semantic identity:

Action Instance:
A123
Attempt:
1 → FAILURE
Attempt:
2 → SUCCESS

The idempotency key remains:

K123

while execution attempts remain distinct.

Therefore:

same semantic Action
≠
same execution attempt

⸻

23. Idempotency and Unknown

This is one of the most important cases.

Suppose:

K123
    ↓
PROCESSING
    ↓
external provider executes
    ↓
response lost
    ↓
UNKNOWN

A retry must not create a new semantic Action.

The consumer should first attempt reconciliation:

K123
 ↓
UNKNOWN
 ↓
query authoritative provider
 ├── SUCCESS
 ├── FAILURE
 └── UNKNOWN

Only after the execution state is established or the applicable recovery policy is evaluated should another consequential attempt proceed.

⸻

24. Idempotency and State Reconciliation

The canonical relationship is:

Idempotency
      +
State Reconciliation
      ↓
Safe retry semantics

Idempotency prevents repeated attempts from becoming unintended duplicate effects.

State Reconciliation establishes the current authoritative state when execution history or external effects are uncertain.

They solve different problems.

Idempotency answers:

Is this the same semantic Action?

State Reconciliation answers:

What actually happened, according to authoritative or sufficiently authoritative observations?

⸻

25. Idempotency and Timeouts

A timeout must preserve the original idempotency identity.

Bad:

Attempt 1:
K123
TIMEOUT
Retry:
K456

Correct:

Attempt 1:
K123
TIMEOUT
Retry:
K123

A timeout does not establish that the Action failed.

If the downstream effect is uncertain, the execution enters an unknown/reconciliation path.

⸻

26. Idempotency and Action Contracts

An Action Contract should carry the necessary idempotency semantics for consequential Actions.

Conceptually:

ActionContract {
    contract_id
    action
    parameters
    idempotency {
        required
        key
        scope
        semantics
        retention
    }
}

The precise contract schema belongs in execution/action-contracts.md.

The Action Contract must not permit idempotency semantics to be invented or modified by a model during execution.

⸻

27. Idempotency Is Part of the Contract

For Actions where duplicate effects are dangerous, idempotency should not be an optional afterthought.

The contract should make clear:

* whether idempotency is required
* how semantic identity is established
* the key scope
* how long the identity remains valid
* how duplicate requests are handled
* how unknown execution is reconciled
* whether the downstream consumer or provider must enforce the same identity

⸻

28. Idempotency Policy

Different Actions may have different semantics.

Example:

send_email

may tolerate duplicates poorly.

set_customer_status(active)

is naturally idempotent.

increment_balance(100)

is generally non-idempotent.

The execution model must not assume every Action is inherently idempotent.

Idempotency requirements are Action-specific and must be explicit.

⸻

29. Naturally Idempotent Actions

An Action is naturally idempotent when repeating it produces the same effective semantic state without introducing an additional intended effect.

Example:

set_user_status(user_123, ACTIVE)

Repeated execution:

ACTIVE → ACTIVE

does not create a new semantic state transition.

Natural idempotency does not eliminate the need for authorization, concurrency control, verification, or auditability.

⸻

30. Non-Idempotent Actions

Some Actions inherently produce additional effects when repeated.

Examples:

charge_payment
increment_counter
create_order
send_money
send_notification

For these Actions, explicit idempotency mechanisms are generally required when repeated delivery or retry is possible.

⸻

31. Idempotency Transformation

A non-idempotent operation may sometimes be made safely repeatable through an explicit semantic identity.

For example:

charge_payment

can become effectively idempotent when:

charge_payment + K123

is defined as one semantic charge.

The key does not change the underlying business semantics. It provides an identity by which repeated attempts can be recognized as attempts to realize the same operation.

⸻

32. Idempotency and Create Operations

Create operations require particular care.

Example:

create_invoice

A retry should not produce:

invoice_1
invoice_2

when the original request actually succeeded.

Instead:

K123
 ↓
invoice_1

and repeated requests should resolve to the existing semantic creation result where the contract permits.

The created resource identity should be retained as part of the execution result.

⸻

33. Idempotency and State Mutation

For mutations such as:

update_customer

the consumer should define whether the operation is:

set-based

or:

incremental

Example:

set_balance(100)

may be idempotent.

Whereas:

increase_balance(100)

is not.

This distinction belongs in the Action semantics rather than being inferred from the transport mechanism.

⸻

34. Idempotency and External Providers

Noema may depend on providers with their own idempotency mechanisms.

Example:

Noema
  ↓
Execution Consumer
  ↓
Payment Provider

The consumer should propagate or deterministically translate idempotency semantics where possible.

Noema must not assume that an external provider is automatically idempotent merely because the Noema-facing consumer is idempotent.

⸻

35. End-to-End Idempotency

True protection against duplicate effects may require idempotency across the entire execution chain:

Noema
  ↓
Execution Consumer
  ↓
Provider
  ↓
Database

If only the outer layer is idempotent:

Noema → same request

but the provider creates duplicate effects, the system is not actually protected.

The idempotency boundary must extend far enough to protect the actual consequential side effect.

⸻

36. Idempotency Boundary

The strongest practical guarantee is:

same semantic Action
       ↓
same execution identity
       ↓
same downstream semantic identity
       ↓
same protected side effect

The exact boundary depends on the enterprise execution architecture.

Noema should explicitly model where idempotency responsibility terminates and where downstream responsibility begins.

⸻

37. Idempotency and Database Constraints

Database-level constraints can provide important enforcement.

Examples:

UNIQUE(idempotency_key)

or:

UNIQUE(tenant_id, idempotency_key)

or a domain-specific uniqueness constraint.

These mechanisms are implementation details but may be necessary to make the semantic guarantee enforceable.

A database constraint is an enforcement mechanism, not the definition of idempotency.

⸻

38. Atomic Claiming

Creating the idempotency record and claiming the right to execute should be atomic where possible.

Bad:

check K123
    ↓
not found
check K123
    ↓
not found
create K123
create K123

This race can produce duplicate execution.

Preferred:

atomic create / claim K123
        ↓
only one execution owner

Other concurrent requests converge on the existing semantic execution.

⸻

39. Concurrency

Concurrent requests with the same idempotency key must converge on one semantic execution unless the Action Contract explicitly defines another behavior.

Example:

Request A ──┐
            ├── K123 ──→ one semantic execution
Request B ──┤
            │
Request C ──┘

They must not independently produce:

Execution A
Execution B
Execution C

unless those are explicitly defined as distinct semantic operations.

⸻

40. Idempotency and Distributed Locks

Distributed locks may help implement idempotency.

However:

lock
≠
idempotency

Locks can expire, be lost, or fail during network partitions.

The durable semantic idempotency record and authoritative execution state must remain the basis for determining whether an Action has already been claimed or executed.

⸻

41. Idempotency Record Retention

Idempotency records may require retention for a defined period.

Example:

created_at
expires_at

The retention period depends on:

* Action semantics
* business risk
* provider behavior
* retry window
* execution duration
* audit requirements
* reconciliation requirements

A key should not expire while a legitimate retry could still create a duplicate effect.

⸻

42. Idempotency Key Expiration

After expiration:

K123

may no longer be recognized as an active idempotency identity.

A new semantic Action should then use a new identity.

Expiration must therefore be chosen with awareness of downstream effect visibility and reconciliation windows.

⸻

43. Reuse After Expiration

Reusing an expired idempotency key for a materially new Action is dangerous.

The system should either:

reject reuse

or:

require a new Action identity

depending on contract semantics.

An expired key must not become an accidental alias for a different semantic operation.

⸻

44. Idempotency and Compensation

Compensation Actions also require idempotency.

Example:

release_inventory(reservation_123)

must not release the same reservation twice in a way that causes unintended effects.

Therefore:

Original Action
    ↓
Failure / Divergence
    ↓
Compensation Action
    ↓
Compensation Idempotency Identity

The compensation Action has its own semantic identity and execution lineage.

Original and compensation identities must not be conflated.

⸻

45. Idempotency and Human Intervention

Human-approved retries must preserve the original Action identity where the retry represents the same semantic operation.

Example:

Attempt 1:
K123 → UNKNOWN
Human:
APPROVE_RETRY
Attempt 2:
K123

The human decision does not automatically create:

K456

The retry remains an attempt to realize the same Action.

The human approval itself is a separately auditable decision and does not mutate the original Intent version.

⸻

46. Human Intervention May Create a New Action

If the human chooses a materially different operation:

Original:
refund ₦50,000

Human decides:

refund ₦30,000

this is not merely a retry.

It is a new semantic Action and therefore requires:

* new Action identity
* new Action Instance
* new Action Contract where applicable
* new authorization evaluation
* new idempotency identity
* corresponding audit lineage

A human decision cannot silently transform the semantics of an existing admitted Intent or Action.

⸻

47. Idempotency and Composite Actions

Composite workflows need identity at multiple levels.

Example:

Intent
 ↓
Workflow
 ├── create_customer
 ├── create_subscription
 └── send_email

Each consequential Action should have its own execution identity and idempotency semantics.

The workflow may also have a parent execution identity.

The parent identity must not be assumed to be sufficient for child-level side-effect protection.

⸻

48. Idempotency and Parallelism

Parallel Actions must not accidentally share an idempotency key.

Bad:

send_email → K123
send_sms   → K123

Correct semantic identities:

send_email → K_EMAIL_123
send_sms   → K_SMS_123

unless the contract explicitly defines both as one shared semantic operation.

⸻

49. Idempotency and Event Delivery

If execution is driven by events:

Event
  ↓
Consumer

the same event may be delivered multiple times.

The consumer should use:

event identity
+
Action identity
+
idempotency semantics

to prevent unintended repeated effects.

An event identity does not automatically become an Action identity.

Event occurrence also does not itself authorize execution.

⸻

50. Idempotency and Queue Delivery

Queues frequently provide at-least-once delivery.

Therefore:

message delivered
message processed
message acknowledged

are separate states.

A consumer must be able to safely receive the same message more than once.

The acknowledgement state must not be treated as proof that the consequential effect occurred unless the execution architecture explicitly establishes that relationship.

⸻

51. Idempotency and Acknowledgement

The following failure is possible:

execute Action
    ↓
SUCCESS
    ↓
acknowledgement lost

The queue then redelivers the message.

Without idempotency:

Action executes twice

With idempotency:

second delivery
    ↓
existing semantic execution found
    ↓
existing result or execution state returned

If the first execution result itself is uncertain, the consumer must reconcile rather than assume either success or failure.

⸻

52. Idempotency and Exactly-Once Effects

Noema’s practical objective should not be universal exactly-once message processing.

The objective is:

exactly-once intended effect

where the Action semantics and downstream systems make that property achievable.

This requires:

stable semantic identity
+
durable execution state
+
idempotent consumer behavior
+
downstream protection where required
+
reconciliation

Noema must not claim exactly-once effects where the downstream architecture cannot support the guarantee.

⸻

53. Idempotency Failure

Idempotency protection itself can fail.

Examples:

idempotency store unavailable
duplicate key race
key collision
record corruption
provider ignores idempotency key
downstream identity lost

These are execution conditions or failures that must be surfaced explicitly.

A system must not falsely claim idempotent protection when the mechanism was unavailable or could not be enforced.

For consequential Actions, inability to establish required idempotency protection may require preventing execution and entering an explicit recovery or escalation path.

⸻

54. Idempotency and Unknown State

If the consumer cannot determine whether an idempotency record exists or whether the downstream effect occurred:

UNKNOWN

is preferable to executing blindly.

For consequential Actions:

uncertain idempotency state
        ↓
stop
        ↓
State Reconciliation
        ↓
deterministic recovery decision

Unknown is not permission to retry.

⸻

55. Idempotency and Determinism

Idempotency decisions must be deterministic.

Given:

same key
same scope
same Action identity
same relevant parameters
same applicable execution semantics

the system should deterministically resolve to the existing semantic execution or to the contract-defined behavior.

It must not probabilistically decide whether to execute again.

Model confidence must never determine idempotency.

⸻

56. Idempotency and Trust

Idempotency does not replace Trust.

A duplicate request must still be evaluated according to the applicable contract and execution semantics.

For example:

existing idempotency key
+
expired contract

does not automatically mean:

execute

The system must distinguish between:

returning an existing historical result

and:

initiating new consequential execution

A historical result may be retrievable under one set of rules while a new execution attempt requires current Trust and contract validity.

⸻

57. Idempotency and Contract Expiration

Suppose:

K123

already produced:

SUCCESS

but the Action Contract has since expired.

A duplicate request may safely return or reference the historical result because no new mutation occurs, provided the retrieval is authorized.

Attempting a new execution after contract expiration must not be permitted merely because the idempotency key exists.

The distinction between historical result retrieval and new execution must remain explicit.

⸻

58. Idempotency and Security

Idempotency keys may expose execution identity and must therefore be protected appropriately.

They should:

* not contain secrets
* not contain credentials
* not encode sensitive information unnecessarily
* not be treated as authorization credentials
* be protected from unauthorized reuse
* be scoped to the intended tenant and execution boundary where applicable

A valid idempotency key alone must never constitute authorization.

The model must not receive credentials or direct access to the idempotency store merely to reason about duplicate execution.

⸻

59. Idempotency and Auditability

The execution record should allow reconstruction of:

* which idempotency identity was used
* which semantic Action it represented
* which Intent version it derived from
* which execution attempts occurred
* which consumer handled each attempt
* which retries occurred
* which reconciliation operations occurred
* which result or Outcome was established
* which contract and execution semantics applied

The audit chain should preserve causal lineage rather than merely recording the final status.

Conceptually:

Intent Version
      ↓
Action Instance
      ↓
Idempotency Identity
      ↓
Execution Attempt(s)
      ↓
Evidence / Reconciliation
      ↓
Outcome

⸻

60. Relationship to Fact Status, Evidence, and Outcome

Idempotency state must not be confused with enterprise truth.

For example:

idempotency record = COMPLETED

does not by itself establish:

enterprise business state = SUCCESS

The execution record may establish that an attempt completed according to consumer semantics, while the authoritative enterprise system may still be required to establish the resulting business state.

Similarly:

idempotency record = UNKNOWN

is an execution-domain condition. It does not itself establish that the enterprise fact is UNKNOWN.

Fact Status remains a separate classification:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

State Reconciliation may establish the relevant enterprise fact.

⸻

61. Idempotency and Planner Boundaries

The planner may select a bounded execution strategy involving idempotent Actions, but it must not invent idempotency semantics.

Planner behavior remains constrained by:

Enterprise Action Graph
+
Capability Registry
+
Action Registry
+
Action Contracts
+
Trust Decision

The planner cannot:

* invent an idempotency key scope
* declare a non-idempotent Action idempotent
* bypass required idempotency protection
* create a new capability
* bypass State Reconciliation
* reinterpret an UNKNOWN execution as safe to retry

Idempotency semantics are part of the registered execution model.

⸻

62. Structural Security Boundary

The idempotency boundary is part of Noema’s structural safety model.

The following are untrusted:

user input
model output
retrieved enterprise text
external tool output
external provider responses
event payloads

They must not directly define executable idempotency semantics.

The execution system must validate and admit structured inputs before using them to establish consequential execution identity.

The model has no authority to:

disable idempotency
change key scope
reuse another tenant's key
declare unknown execution successful

No free-form model output may directly reach the execution boundary.

⸻

63. Idempotency and Read-Only Actions

Idempotency is not limited to writes.

Read-only Actions may also require stable execution identity where they:

* create external side effects
* consume scarce resources
* initiate expensive provider operations
* create cases or records
* trigger downstream workflows
* expose protected information
* produce externally visible events

Therefore:

read-only
≠
non-consequential

Whether idempotency is required depends on the actual semantic effect of the Action.

⸻

64. Idempotency and Replay

Replay must be distinguished from retry.

A retry attempts to continue or repeat the same semantic Action under its original execution semantics.

A replay may instead reproduce historical observations or execution events for analysis, recovery, testing, or audit.

Replay must not create a new enterprise business occurrence by default.

Historical idempotency records and execution history must remain immutable.

⸻

65. Idempotency and Operational Memory

Operational Memory may retain structured idempotency and execution history, including:

* semantic Action identity
* idempotency identity
* execution attempts
* duplicate deliveries
* reconciliation events
* outcomes
* recovery decisions

Operational Memory is not enterprise business authority.

It records execution history and operational knowledge. It must not become a shadow source of truth for the enterprise system.

⸻

66. Versioning

Idempotency semantics must preserve the relevant semantic versions for consequential execution.

Relevant versions may include:

intent_version
action_version
action_contract_version
trust_contract_version
policy_version
graph_version
capability_version
integration_version
system_version

Transport or implementation changes must not silently change the semantic identity of a historical Action.

If an Action’s semantic meaning materially changes, it is a new semantic Action and must not reuse the old identity merely because the transport request looks similar.

⸻

67. Idempotency Invariants

Invariant 1

The same semantic Action must retain the same idempotency identity across retries.

Invariant 2

Different semantic Actions must not accidentally share an idempotency identity within the same scope.

Invariant 3

Idempotency identity must be bound to the Action semantics and all parameters material to its effect.

Invariant 4

A duplicate request must not create an unintended duplicate effect.

Invariant 5

Idempotency must remain effective across network retries and at-least-once delivery where the execution architecture claims such protection.

Invariant 6

Idempotency must distinguish semantic Action identity from execution attempt identity.

Invariant 7

Unknown execution state must not trigger unprotected duplicate execution.

Invariant 8

Retries must preserve the original Action identity unless the semantic Action changes.

Invariant 9

A materially changed Action requires a new semantic identity.

Invariant 10

Compensation Actions require their own idempotency semantics.

Invariant 11

Idempotency mechanisms must be concurrency-safe.

Invariant 12

Idempotency records must not silently expire while duplicate execution remains possible.

Invariant 13

An idempotency key is not an authorization credential.

Invariant 14

Idempotency does not imply exactly-once delivery.

Invariant 15

Idempotency does not eliminate the need for State Reconciliation.

Invariant 16

If required idempotency state cannot be established for a consequential Action, the system must prefer uncertainty and reconciliation over blind execution.

Invariant 17

The exact Intent Object version associated with a consequential Action must remain immutable across its execution attempts.

Invariant 18

Idempotency state must not be treated as authoritative enterprise Business State.

Invariant 19

Idempotency semantics must be deterministic and must not depend on model confidence.

Invariant 20

A downstream system must not be assumed idempotent merely because an upstream Noema boundary is idempotent.

Invariant 21

Historical execution and idempotency records must not be silently rewritten to reflect later retries or reconciliation.

Invariant 22

A materially different Action requires new authorization and idempotency semantics rather than reuse of the original identity.

Invariant 23

The planner must not invent, weaken, or bypass required idempotency semantics.

Invariant 24

Idempotency failure must not be represented as successful protection when the required mechanism could not be enforced.

Invariant 25

Idempotency identity must respect tenant, organizational, resource, and execution isolation boundaries where applicable.

⸻

68. Canonical Mental Model

                         INTENT VERSION
                              │
                              ▼
                       ACTION INSTANCE
                              │
                              ▼
                    IDEMPOTENCY IDENTITY
                              │
                 ┌────────────┼────────────┐
                 │            │            │
             Attempt 1    Attempt 2    Attempt 3
                 │            │            │
              FAILURE       UNKNOWN      SUCCESS
                              │
                              ▼
                     STATE RECONCILIATION
                              │
                    ┌─────────┴─────────┐
                    │                   │
                 VERIFIED            UNKNOWN
                    │                   │
                    ▼                   ▼
              ESTABLISHED          RECOVER /
               EXECUTION           ESCALATE
                    │
                    ▼
                  OUTCOME

Or more simply:

             Same Semantic Action
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Retry       Retry       Retry
          │           │           │
          └───────────┼───────────┘
                      ▼
             Same semantic identity
                      │
                      ▼
          No unintended duplicate effect
                      │
                      ▼
        Reconciliation when uncertain

⸻

69. Canonical Execution Relationship

The canonical relationship is:

Source of Intent
      ↓
Intent Object
      ↓
Hard Schema Validation / Admission
      ↓
Intent Version
      ↓
Action Instance
      ↓
Deterministic Trust
      ↓
Action Contract
      ↓
Idempotency Identity
      ↓
Execution Attempt
      ↓
Verification / State Reconciliation
      ↓
Outcome

The critical distinction is:

Intent Version
    ≠
Action Identity
    ≠
Idempotency Identity
    ≠
Execution Attempt Identity
    ≠
Outcome

These identities are related but must not be collapsed into one identifier.

⸻

70. Final Definition

Idempotency is the execution property that preserves the semantic identity of an Action across repeated execution attempts and prevents those attempts from producing unintended duplicate effects.

The core invariant is:

Noema assumes execution may be delivered more than once.
A retry is therefore not a new Action by default.
It is another attempt to realize the same semantic Action.

Stable semantic identity, durable idempotency state, atomic claiming, downstream enforcement, bounded execution semantics, and State Reconciliation together ensure that at-least-once delivery and execution uncertainty do not become duplicate consequential effects.

Idempotency does not establish authorization, enterprise truth, or successful Outcome.

It establishes the semantic boundary that makes repeated execution safe where the Action and downstream systems support that guarantee.