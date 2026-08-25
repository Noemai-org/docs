Idempotency

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: 04-execution/idempotency.md

⸻

1. Definition

Idempotency is the execution property that allows the same Action to be attempted multiple times without producing unintended additional effects beyond the semantics of the original Action.

Idempotency exists because distributed execution cannot reliably assume that a request is processed exactly once.

The canonical principle is:

Same semantic Action
+
Repeated execution attempts
=
No unintended duplicate effect

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

The consumer must be able to distinguish:

new Action

from:

duplicate execution attempt

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

Idempotency prevents this unintended duplication.

⸻

4. Idempotency Is Not Exactly-Once Delivery

These concepts must remain separate.

Exactly-once delivery:
message is delivered exactly once

versus:

Idempotent execution:
repeated delivery does not create unintended repeated effects

Noema should not depend on universal exactly-once delivery.

Instead:

At-least-once delivery
+
Idempotent execution
+
Reconciliation

is the preferred distributed execution model.

⸻

5. Idempotency Is Not Deduplication Alone

Deduplication asks:

“Have I seen this request before?”

Idempotency asks:

“If I see this request again, can I safely produce the same semantic result without creating an unintended additional effect?”

A deduplication table may be one implementation mechanism.

It is not the complete semantic guarantee.

⸻

6. Idempotency Belongs to Execution

Idempotency is primarily an execution concern.

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
Outcome

Intent resolution should not need to know how a payment provider handles retries.

The execution boundary must enforce the appropriate semantics.

⸻

7. Semantic Identity

The central question is:

What makes two execution attempts the same Action?

Noema should distinguish:

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

⸻

8. Action Identity vs Execution Identity

Conceptually:

Action Instance
      │
      ├── Execution Attempt 1
      ├── Execution Attempt 2
      └── Execution Attempt 3

The attempts are distinct execution events.

The Action Instance is the semantic operation being attempted.

⸻

9. Idempotency Key

An idempotency key identifies the semantic execution request.

Example:

idempotency_key:
idem_01JABC...

The key should be:

unique within its intended scope
stable across retries
bound to the intended Action

⸻

10. Idempotency Key Is Not a Random Request ID

A request ID may identify:

HTTP request #1

while the idempotency key identifies:

the semantic Action being requested

Therefore:

request_id_1 ≠ request_id_2

may still represent:

idempotency_key_X

and therefore the same Action.

⸻

11. Key Stability

If a retry generates a new idempotency key:

Attempt 1:
K1
Attempt 2:
K2

the consumer cannot know that both represent the same semantic Action.

Correct:

Attempt 1:
K1
Attempt 2:
K1

⸻

12. Key Scope

An idempotency key must have a defined scope.

Possible scopes:

tenant
consumer
Action type
resource
Action Contract
global

For example:

(tenant_id, action_type, idempotency_key)

may define uniqueness.

The scope must be explicit.

⸻

13. Key Collision

Two genuinely different Actions must not accidentally share an idempotency key within the same scope.

Example:

refund_payment(payment_123)

and:

refund_payment(payment_456)

must not be treated as the same operation.

Therefore the semantic Action parameters must be bound to the idempotency identity.

⸻

14. Parameter Binding

An idempotency record should associate the key with the canonical Action parameters.

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

the consumer should reject the request rather than silently reinterpret it.

⸻

15. Idempotency Record

Conceptually:

IdempotencyRecord {
    key
    action
    parameters_hash
    execution_id
    status
    outcome
    created_at
    expires_at
}

The exact storage representation is implementation-specific.

⸻

16. Idempotency Lifecycle

A typical lifecycle is:

NEW
 ↓
PROCESSING
 ↓
COMPLETED

Possible terminal states:

FAILED
UNKNOWN
EXPIRED

The exact state machine depends on execution semantics.

⸻

17. First Request

The first request creates the idempotency record:

K123
   ↓
not found
   ↓
create record
   ↓
execute

The consumer associates the Action with that key.

⸻

18. Duplicate Request While Processing

Suppose:

K123 → PROCESSING

and another request arrives:

K123

The consumer must not blindly execute again.

Possible deterministic behavior:

return PROCESSING

or:

wait for existing execution

or:

return current execution state

depending on the protocol.

⸻

19. Duplicate Request After Success

Suppose:

K123
    ↓
SUCCESS

A later request with:

K123

should normally return the existing result rather than execute the Action again.

Conceptually:

K123
 ↓
existing execution
 ↓
existing Outcome

⸻

20. Duplicate Request After Failure

This requires explicit semantics.

A failed Action may be:

retryable

or:

non-retryable

Therefore a consumer must know whether reuse of the same idempotency key means:

return original failure

or:

resume/retry the existing semantic Action

The semantics must not be ambiguous.

⸻

21. Retry Semantics

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

⸻

22. Idempotency and Unknown

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

The consumer should first attempt reconciliation.

K123
 ↓
UNKNOWN
 ↓
query authoritative provider
 ├── SUCCESS
 ├── FAILURE
 └── UNKNOWN

⸻

23. Idempotency and Reconciliation

The canonical relationship is:

Idempotency
      +
Reconciliation
      ↓
Safe retry semantics

Idempotency prevents duplicate effects.

Reconciliation establishes whether the original effect occurred.

They solve different problems.

⸻

24. Idempotency and Timeouts

A timeout must preserve the original idempotency key.

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

Otherwise the retry may create a second effect.

⸻

25. Idempotency and Action Contracts

An Action Contract should carry the necessary idempotency semantics for consequential Actions.

Conceptually:

ActionContract {
    contract_id
    action
    parameters
    idempotency {
        key
        scope
        semantics
    }
}

The precise contract schema belongs in action-contracts.md.

⸻

26. Idempotency Is Part of the Contract

For Actions where duplicate effects are dangerous, idempotency should not be an optional afterthought.

The contract should make clear:

whether idempotency is required
how identity is established
how long the key remains valid
what duplicate requests return

⸻

27. Idempotency Policy

Different Actions may have different semantics.

Example:

send_email

may tolerate duplicates poorly.

set_customer_status(active)

is naturally idempotent.

increment_balance(100)

is generally non-idempotent.

The execution model must not assume every Action is inherently idempotent.

⸻

28. Naturally Idempotent Actions

An Action is naturally idempotent when repeating it results in the same effective state.

Example:

set_user_status(user_123, ACTIVE)

Repeated execution:

ACTIVE → ACTIVE

does not create a new semantic effect.

⸻

29. Non-Idempotent Actions

Some Actions inherently produce additional effects when repeated.

Examples:

charge_payment
increment_counter
create_order
send_money
send_notification

For these Actions, explicit idempotency mechanisms are generally required.

⸻

30. Idempotency Transformation

A non-idempotent operation may sometimes be made safely repeatable through an idempotency key.

For example:

charge_payment

becomes effectively idempotent when:

charge_payment + K123

is treated as one semantic charge.

⸻

31. Idempotency and Create Operations

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

and repeated requests should resolve to:

invoice_1

⸻

32. Idempotency and State Mutation

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

This distinction belongs in the Action semantics.

⸻

33. Idempotency and External Providers

Noema may depend on providers with their own idempotency mechanisms.

Example:

Noema
  ↓
Payment Consumer
  ↓
Payment Provider

The consumer should propagate or translate idempotency semantics appropriately.

Noema should not assume that the external provider is automatically idempotent.

⸻

34. End-to-End Idempotency

True safety may require idempotency across the entire execution chain:

Noema
  ↓
Execution Consumer
  ↓
Provider
  ↓
Database

If only the outer layer is idempotent:

Noema → same request

but the provider creates duplicate effects, the system is not actually safe.

⸻

35. Idempotency Boundary

The strongest practical guarantee is:

same semantic Action
       ↓
same execution identity
       ↓
same downstream semantic identity
       ↓
same resulting effect

The boundary must extend far enough to protect the actual side effect.

⸻

36. Idempotency and Database Constraints

Database-level constraints can provide important enforcement.

Examples:

UNIQUE(idempotency_key)
UNIQUE(tenant_id, idempotency_key)

or a domain-specific uniqueness constraint.

These mechanisms are implementation details but may be necessary to make the semantic guarantee enforceable.

⸻

37. Atomic Claiming

Creating the idempotency record and claiming the right to execute must be atomic where possible.

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

atomic create/claim K123

followed by execution.

⸻

38. Concurrency

Concurrent requests with the same idempotency key must converge on one semantic execution.

Example:

Request A ──┐
            ├── K123 ──→ one execution
Request B ──┤
            │
Request C ──┘

They must not independently produce:

Execution A
Execution B
Execution C

unless the Action semantics explicitly permit that behavior.

⸻

39. Idempotency and Distributed Locks

Distributed locks may help implement idempotency.

However:

A lock is not itself an idempotency guarantee.

Locks can expire, be lost, or fail during network partitions.

The durable semantic record must remain authoritative.

⸻

40. Idempotency Record Retention

Idempotency records may require retention for a defined period.

Example:

created_at
expires_at

The retention period depends on:

Action semantics
business risk
provider behavior
retry window
audit requirements

A key should not expire while a legitimate retry may still create a duplicate effect.

⸻

41. Idempotency Key Expiration

After expiration:

K123

may no longer be recognized.

A new Action should then use a new semantic identity.

Expiration must therefore be chosen carefully.

⸻

42. Reuse After Expiration

Reusing an expired idempotency key for a materially new Action is dangerous.

The system should either:

reject reuse

or:

require a new Action identity

depending on contract semantics.

⸻

43. Idempotency and Compensation

Compensation Actions also require idempotency.

Example:

release_inventory(reservation_123)

must not release the same reservation twice in a way that causes unintended effects.

Therefore:

Original Action
    ↓
Failure
    ↓
Compensation Action
    ↓
Compensation Idempotency Key

The compensation has its own semantic identity.

⸻

44. Idempotency and Human Intervention

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

⸻

45. Human Intervention May Create a New Action

However, if the human chooses a materially different operation:

Original:
refund ₦50,000

Human decides:

refund ₦30,000

this is not merely a retry.

It is a new semantic Action and therefore requires:

new Action identity
new contract
new authorization semantics
new idempotency identity

⸻

46. Idempotency and Composite Actions

Composite workflows need identity at multiple levels.

Example:

Intent
 ↓
Workflow
 ├── create_customer
 ├── create_subscription
 └── send_email

Each consequential Action should have its own execution identity and idempotency semantics.

The workflow itself may also have a parent execution identity.

⸻

47. Idempotency and Parallelism

Parallel Actions must not accidentally share an idempotency key.

Bad:

send_email → K123
send_sms   → K123

Correct semantic identities:

send_email → K_EMAIL_123
send_sms   → K_SMS_123

unless the contract explicitly defines a shared semantic operation.

⸻

48. Idempotency and Event Delivery

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

⸻

49. Idempotency and Queue Delivery

Queues frequently provide at-least-once delivery.

Therefore:

message delivered
message processed
message acknowledged

are separate states.

A consumer must be able to safely receive the same message more than once.

⸻

50. Idempotency and Acknowledgement

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
existing execution found
    ↓
existing result returned

⸻

51. Idempotency and Exactly-Once Effects

Noema’s practical objective should not be:

exactly-once message processing

but:

exactly-once intended effect

where the Action semantics permit it.

This is achieved through:

stable semantic identity
+
durable execution state
+
idempotent consumer behavior
+
reconciliation

⸻

52. Idempotency Failure

Idempotency itself can fail.

Examples:

idempotency store unavailable
duplicate key race
key collision
record corruption
provider ignores idempotency key

These are execution failures and should be surfaced explicitly.

A system must not falsely claim idempotent protection when the mechanism was unavailable.

⸻

53. Idempotency and Unknown State

If the consumer cannot determine whether an idempotency record exists or whether the downstream effect occurred:

UNKNOWN

is preferable to executing blindly.

For consequential Actions:

uncertain idempotency state
        ↓
stop
        ↓
reconcile

⸻

54. Idempotency and Determinism

Idempotency decisions must be deterministic.

Given:

same key
same scope
same Action identity
same parameters

the system should deterministically resolve to:

existing execution

rather than probabilistically deciding whether to execute again.

⸻

55. Idempotency and Trust

Idempotency does not replace Trust.

A duplicate request must still be evaluated against the validity of its contract.

For example:

existing idempotency key
+
expired contract

does not automatically mean:

execute

The system must define whether returning the historical result is permitted while new execution is not.

⸻

56. Idempotency and Contract Expiration

Suppose:

K123

already produced:

SUCCESS

but the Action Contract has since expired.

A duplicate request may safely return the historical result because no new mutation occurs.

However, attempting a new execution after expiration should be rejected.

This distinction must be explicit.

⸻

57. Idempotency and Security

Idempotency keys may be sensitive because they can expose execution identity.

They should therefore:

not contain secrets
not contain credentials
not encode sensitive information unnecessarily
be protected from unauthorized reuse

A valid idempotency key alone should not constitute authorization.

⸻

58. Idempotency and Auditability

The execution record should allow reconstruction of:

which key was used
which Action it represented
which attempts occurred
which result was produced
which retries happened
which consumer handled them

This is essential for consequential workflows.

⸻

59. Idempotency Invariants

Invariant 1

The same semantic Action must retain the same idempotency identity across retries.

Invariant 2

Different semantic Actions must not accidentally share an idempotency identity within the same scope.

Invariant 3

Idempotency keys must be bound to the Action semantics and relevant parameters.

Invariant 4

A duplicate request must not create an unintended duplicate effect.

Invariant 5

Idempotency must remain effective across network retries and at-least-once delivery.

Invariant 6

Idempotency must distinguish execution attempts from semantic Action identity.

Invariant 7

Unknown execution state must not trigger an unprotected duplicate execution.

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

Idempotency does not eliminate the need for reconciliation.

Invariant 16

If idempotency state cannot be established for a consequential Action, the system must prefer uncertainty and reconciliation over blind execution.

⸻

60. Canonical Mental Model

                 ACTION INSTANCE
                       │
                       ▼
                IDEMPOTENCY KEY
                       │
              ┌────────┼────────┐
              │        │        │
          Attempt 1  Attempt 2  Attempt 3
              │        │        │
           FAILURE   TIMEOUT   SUCCESS
                       │
                       ▼
                 RECONCILIATION
                       │
                       ▼
                 SINGLE EFFECT

Or more simply:

             Same Action
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Retry     Retry     Retry
        │         │         │
        └─────────┼─────────┘
                  ▼
          Same semantic identity
                  │
                  ▼
       No unintended duplicate effect

⸻

61. Final Definition

Idempotency is the property that preserves the semantic identity of an Action across repeated execution attempts and prevents those attempts from producing unintended duplicate effects.

The core invariant is:

Noema assumes execution may be delivered more than once. A retry is therefore not a new Action by default: it is another attempt to realize the same semantic Action. Stable idempotency identity, durable execution state, downstream enforcement, and reconciliation together ensure that uncertainty and at-least-once delivery do not become duplicate consequential effects.