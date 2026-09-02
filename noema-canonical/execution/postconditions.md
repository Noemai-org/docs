Postconditions

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/postconditions.md

⸻

1. Definition

A postcondition is a condition that must hold after an Action or execution step has completed for the system to consider the expected effect of that Action established.

Postconditions answer:

“What must be true after this Action for us to say that it succeeded?”

They are therefore the bridge between execution and Outcome.

Action
   ↓
Execution
   ↓
Observed State
   ↓
Postcondition Evaluation
   ↓
Outcome

⸻

2. Core Principle

Execution completion does not imply Action success.

An executor can report:

process exited successfully

while the intended business effect did not occur.

Noema therefore distinguishes:

execution completed

from:

postconditions satisfied

and from:

intended Outcome established

⸻

3. Why Postconditions Exist

Consider:

Action:
activate_card(card_123)

The external API returns:

HTTP 200

That establishes that the API request completed successfully.

It does not necessarily establish:

card_123.status = ACTIVE

A postcondition provides the semantic criterion for determining whether the intended effect actually occurred.

⸻

4. Execution vs Effect

The canonical distinction is:

Execution:
"Did the Action attempt complete?"
Effect:
"Did the intended state change occur?"

Postconditions primarily concern the second question.

Execution signal
      +
Postcondition evidence
      ↓
Semantic Outcome

⸻

5. Preconditions vs Postconditions

These concepts must remain distinct.

Precondition

What must be true before an Action can execute.

Example:

account.status = ACTIVE

Postcondition

What must be true after the Action executes.

Example:

card.status = ACTIVE

Therefore:

Precondition
    ↓
Action
    ↓
Postcondition

⸻

6. Postconditions Are Not Predictions

A planner may predict:

expected:
card.status = ACTIVE

This is not yet a fact.

The system must observe evidence after execution.

Expected:
card.status = ACTIVE
Observed:
card.status = ACTIVE
Therefore:
postcondition satisfied

⸻

7. Expected vs Observed

Noema should explicitly distinguish:

Expected Postcondition

from:

Observed State

Example:

Expected:
balance = ₦100,000
Observed:
balance = ₦100,000

The equality between expected and observed state establishes satisfaction.

⸻

8. Postcondition Evaluation

Conceptually:

evaluate(
    expected_postcondition,
    observed_state
)

produces:

SATISFIED
NOT_SATISFIED
UNKNOWN

UNKNOWN is important.

Noema must not convert missing evidence into success.

⸻

9. Unknown Is Not Failure

Suppose:

Action:
charge_customer

The provider times out.

Noema cannot determine whether the charge occurred.

The postcondition:

transaction.status = COMPLETED

cannot currently be established.

The correct result may be:

UNKNOWN

not:

FAILED

and certainly not:

SUCCESS

⸻

10. Postconditions and Evidence

Postconditions depend on Evidence.

Action
 ↓
Evidence
 ↓
Postcondition Evaluation
 ↓
Outcome

Evidence may come from:

database state
API response
event
provider confirmation
resource inspection
human confirmation

The evidence must be sufficient for the specific postcondition.

⸻

11. Evidence Quality

Not all evidence is equally authoritative.

For example:

Executor says:
"payment succeeded"

may be weaker than:

Payment provider:
transaction_123 = SETTLED

The canonical Evidence model in 03-trust/evidence.md should determine how evidence is evaluated.

⸻

12. Postconditions Are Domain-Semantic

A technical success signal is not necessarily a semantic postcondition.

Example:

HTTP 201

is a transport-level result.

The semantic postcondition might be:

user.account.status = ACTIVE

Noema should reason about the semantic condition, not merely the transport result.

⸻

13. Postcondition Types

Postconditions can describe different kinds of effects.

State

card.status = ACTIVE

Existence

invoice_123 exists

Non-existence

reservation_123 does not exist

Relationship

user_123 owns card_456

Value

balance = ₦100,000

Event

refund_settled event observed

External confirmation

provider confirms shipment

⸻

14. State Postconditions

A state postcondition specifies the expected state of a Resource.

Example:

Action:
suspend_account(account_123)
Postcondition:
account_123.status = SUSPENDED

⸻

15. Existence Postconditions

Some Actions create Resources.

Example:

Action:
create_invoice
Postcondition:
invoice_123 EXISTS

The existence itself may be insufficient if additional properties matter.

A stronger postcondition might be:

invoice_123 EXISTS
invoice_123.status = ISSUED
invoice_123.amount = ₦500,000

⸻

16. Non-Existence Postconditions

Deletion or cancellation may require proving absence.

Example:

Action:
delete_customer(customer_123)
Postcondition:
customer_123 does not exist

This is stronger than:

DELETE request returned 204

⸻

17. Relationship Postconditions

Some Actions modify relationships.

Example:

Action:
assign_user_to_team

Postcondition:

user_123 ∈ team_456.members

⸻

18. Quantitative Postconditions

Actions may produce measurable values.

Example:

Action:
transfer ₦100,000

Possible postconditions:

source.balance = previous_balance - ₦100,000
destination.balance = previous_balance + ₦100,000

Multiple postconditions may therefore be required to establish correctness.

⸻

19. Temporal Postconditions

Some effects must occur within a temporal boundary.

Example:

Action:
send_otp

Postcondition:

otp_delivery.confirmed within 30 seconds

Temporal semantics must be explicit where timing affects correctness.

⸻

20. Composite Postconditions

An Action may have multiple required conditions.

Example:

Action:
issue_card

Postconditions:

card exists
card.status = ACTIVE
card.owner = customer_123
card.type = REPLACEMENT

The Action should not be considered fully successful merely because one condition holds.

⸻

21. Conjunctive Postconditions

A composite postcondition may require:

P1 AND P2 AND P3

Example:

card.exists
AND
card.status = ACTIVE
AND
card.owner = customer_123

All must be satisfied.

⸻

22. Disjunctive Postconditions

Some Actions may permit alternative valid outcomes.

Example:

shipment.status = DELIVERED
OR
shipment.status = PICKUP_AVAILABLE

The contract must explicitly define whether these are equivalent successful Outcomes.

Noema must not infer equivalence.

⸻

23. Conditional Postconditions

A postcondition may depend on an Action branch.

Example:

if payment.method = CARD:
    card_transaction.status = SETTLED
if payment.method = BANK_TRANSFER:
    transfer.status = CONFIRMED

The applicable postcondition must be determined from the actual execution path.

⸻

24. Postcondition Scope

Postconditions may apply to:

single Action
plan step
composite Action
entire Plan
workflow

The scope must be explicit.

⸻

25. Action-Level Postconditions

Example:

Action:
create_customer
Postcondition:
customer exists

This establishes the immediate semantic effect.

⸻

26. Plan-Level Postconditions

A Plan may have a higher-level postcondition.

Example:

Plan:
renew_card
Final postcondition:
customer has an active replacement card

The plan-level condition may depend on several Action-level postconditions.

verify
   ↓
issue
   ↓
activate
   ↓
Final Postcondition

⸻

27. Postconditions and Outcomes

Postconditions provide evidence for determining Outcome.

Postconditions
       │
       ▼
Evaluation
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
TRUE  FALSE UNKNOWN
 │      │      │
 ▼      ▼      ▼
SUCCESS FAILURE UNCERTAIN

The exact Outcome semantics belong to outcome.md.

⸻

28. Postconditions Do Not Define the User’s Intent

Intent:

"Get me a replacement card."

Postcondition:

replacement_card.status = ACTIVE

The postcondition operationalizes the intended result.

It does not redefine the Intent.

⸻

29. Postconditions and Planning

Planning should define expected postconditions for Actions where necessary.

Example:

Plan:
issue_card
Expected:
card.status = ISSUED

Execution later determines whether this expectation was actually satisfied.

⸻

30. Postconditions and Action Contracts

An Action Contract may contain:

action
inputs
preconditions
authorization
idempotency
postconditions

Conceptually:

ActionContract {
    action
    inputs
    preconditions
    postconditions
}

The exact schema remains defined in action-contracts.md.

⸻

31. Postconditions and Idempotency

Postconditions are important for determining whether a retry is necessary.

Example:

Action:
activate_card

After a timeout:

Unknown execution

Noema checks:

card.status = ACTIVE

If true:

postcondition satisfied

No retry is necessary.

This is a key relationship:

Idempotency
+
Postcondition verification
+
Reconciliation

⸻

32. Postconditions and Reconciliation

When execution state is uncertain:

Execution:
UNKNOWN

Noema may evaluate postconditions against authoritative external state.

UNKNOWN
 ↓
observe Resource
 ↓
evaluate Postcondition
 ↓
SATISFIED / NOT SATISFIED / UNKNOWN

This can resolve uncertainty without blindly repeating the Action.

⸻

33. Postconditions and Compensation

If required postconditions cannot be satisfied:

Action
 ↓
partial effect
 ↓
postcondition failure

the execution system may need compensation.

Example:

create_order → SUCCESS
reserve_inventory → SUCCESS
charge_payment → FAILURE

The plan may then evaluate compensation Actions.

⸻

34. Postcondition Failure

A postcondition failure means:

The Action did not establish the required semantic effect.

It does not necessarily mean the Action had no effect.

Example:

Expected:
balance = ₦100,000
Observed:
balance = ₦80,000

The Action may have partially changed the state.

The execution record must preserve the observed state.

⸻

35. Partial Satisfaction

For composite postconditions:

P1 = TRUE
P2 = TRUE
P3 = FALSE

the result is not full success.

Possible semantic state:

PARTIALLY_SATISFIED

if supported by the Outcome model.

Otherwise:

NOT_SATISFIED

with evidence describing which conditions failed.

⸻

36. Postcondition Drift

A postcondition may be satisfied immediately and later become false because another system changes the Resource.

Example:

Action:
activate_card
Postcondition:
card.status = ACTIVE

At T1:

ACTIVE

At T2:

BLOCKED

The original Action may still have succeeded.

Therefore postcondition evaluation must have a defined observation time.

⸻

37. Temporal Truth

The canonical interpretation is:

Postcondition P
was satisfied
at observation time T

rather than:

P is permanently true

This distinction matters for mutable Resources.

⸻

38. Postcondition Observation Window

Some postconditions require a defined observation window.

Example:

Action:
send_email

Postcondition:

delivery.confirmed within 5 minutes

The system should not evaluate the condition indefinitely.

⸻

39. Eventual Postconditions

Some effects are asynchronous.

Example:

Action:
provision_server

The API may return:

provisioning_started

while the actual postcondition is:

server.status = READY

The system may therefore need:

polling
event subscription
callback
reconciliation

to establish the postcondition.

⸻

40. Synchronous vs Asynchronous Postconditions

Synchronous

Action
 ↓
response
 ↓
postcondition immediately observable

Asynchronous

Action
 ↓
accepted
 ↓
wait
 ↓
external state changes
 ↓
observe
 ↓
postcondition evaluated

The execution model must distinguish these cases.

⸻

41. Postcondition Evidence Must Be Authoritative

A postcondition should ideally be evaluated against the authoritative source of truth.

For example:

payment provider

rather than:

Noema's local cache

when the provider owns the payment state.

The authoritative source depends on the Resource.

⸻

42. Cached State

Cached state may be stale.

Therefore:

cache:
status = ACTIVE

does not necessarily establish:

authoritative state:
status = ACTIVE

unless freshness guarantees make the cache authoritative for that evaluation.

⸻

43. Postcondition Evaluation Must Be Deterministic

Given:

same postcondition
+
same relevant observed state
+
same evaluation rules

Noema should produce the same result.

P(state) → TRUE/FALSE/UNKNOWN

This evaluation must not depend on model improvisation.

⸻

44. LLMs and Postconditions

An LLM may assist with:

mapping unstructured evidence

but should not independently decide that a consequential postcondition is satisfied when deterministic evidence is available.

Preferred:

LLM:
extract relevant evidence
Deterministic evaluator:
evaluate postcondition

⸻

45. Postcondition Normalization

Different systems may express equivalent state differently.

Example:

"active"
"ACTIVE"
"enabled"

Noema should normalize these representations before evaluation where the ontology defines them as equivalent.

The equivalence must be canonical.

⸻

46. Postcondition Contradictions

Evidence may conflict.

Example:

Provider A:
ACTIVE
Provider B:
SUSPENDED

Noema must not arbitrarily select one.

The system should enter an evidence-resolution or uncertainty state according to Trust semantics.

⸻

47. Postcondition Staleness

Evidence may be too old to establish a current postcondition.

Example:

Last known state:
ACTIVE at 10:00
Current evaluation:
12:00

If the Resource can change between those times, the evidence may be insufficient.

The correct result may be:

UNKNOWN

⸻

48. Postcondition and Resource Ownership

The system must know which Resource the postcondition refers to.

Example:

balance = ₦100,000

is insufficient without identifying:

account_123.balance

Canonical postconditions should bind to specific Resources or Resource identities.

⸻

49. Postcondition and Concurrency

Concurrent Actions may affect the same Resource.

Example:

Action A:
set status ACTIVE
Action B:
set status BLOCKED

If both execute concurrently, postcondition evaluation must account for ordering and causality.

A postcondition should not be interpreted without its relevant execution context.

⸻

50. Postcondition and Causality

Noema should distinguish:

Action caused state S

from:

state S happened sometime after Action

For consequential workflows, establishing causality may require:

execution ID
event ID
transaction ID
provider reference
timestamp

⸻

51. Postcondition and Auditability

A successful postcondition evaluation should preserve:

postcondition definition
observation time
observed value
evidence source
evidence identity
evaluation result
evaluator/version

This allows the system to explain why an Outcome was established.

⸻

52. Postcondition Versioning

Postcondition semantics may evolve.

Therefore evaluations should be associated with the version of the contract or evaluation rule used.

Example:

postcondition_version = 2

Historical evaluations must remain interpretable.

⸻

53. Postcondition Failure Handling

When a required postcondition fails:

Action
 ↓
Postcondition FALSE

the system may:

retry
reconcile
replan
compensate
request human intervention
terminate

The correct path depends on the Action Contract, failure semantics, and Trust state.

⸻

54. Postcondition Evaluation Does Not Automatically Trigger Retry

A failed postcondition does not mean:

retry immediately

For example:

Action:
create_payment

Postcondition:

payment.status = SETTLED

If it is currently:

PROCESSING

the correct response may be to wait or reconcile rather than issue another payment.

⸻

55. Postconditions and Human Confirmation

Some domains may permit human confirmation as evidence.

Example:

Action:
physical_delivery

Postcondition:

recipient confirms receipt

Human evidence must still be evaluated according to the Trust and Evidence model.

Human confirmation should not automatically override stronger contradictory evidence.

⸻

56. Postcondition Hierarchy

Complex workflows can contain nested postconditions.

Action
   ↓
Action Postcondition
   ↓
Plan Postcondition
   ↓
Intent Outcome

Example:

activate_card
    ↓
card.status = ACTIVE
    ↓
replacement_card.available = TRUE
    ↓
user's card renewed

Each level should have distinct semantics.

⸻

57. Postcondition Invariants

Invariant 1

Execution completion does not imply postcondition satisfaction.

Invariant 2

A postcondition must be evaluated against evidence.

Invariant 3

Expected state must not be represented as observed state.

Invariant 4

Missing evidence must not be interpreted as success.

Invariant 5

UNKNOWN must remain distinct from FALSE.

Invariant 6

Postconditions must reference the relevant Resource or state explicitly.

Invariant 7

Composite postconditions must define whether all or only some conditions are required.

Invariant 8

Temporal postconditions must define their observation window where timing matters.

Invariant 9

Postcondition evaluation must use authoritative or sufficiently trustworthy evidence.

Invariant 10

Postcondition evaluation must be deterministic given the same inputs and evaluation rules.

Invariant 11

Postcondition satisfaction at one point in time does not imply permanent satisfaction.

Invariant 12

Postcondition failure does not automatically imply retry.

Invariant 13

An uncertain postcondition must not trigger an unprotected consequential retry.

Invariant 14

Postcondition evaluations must be auditable.

Invariant 15

Plan-level postconditions must not be inferred solely from planned Actions.

Invariant 16

Postconditions must not redefine or silently alter the underlying Intent.

⸻

58. Canonical Mental Model

                    ACTION
                      │
                      ▼
                  EXECUTION
                      │
                      ▼
                 OBSERVATION
                      │
                      ▼
                  EVIDENCE
                      │
                      ▼
             POSTCONDITION EVAL
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      SATISFIED    NOT SATISFIED  UNKNOWN
          │           │           │
          ▼           ▼           ▼
       SUCCESS     FAILURE     RECONCILE /
                                 WAIT /
                               INTERVENE

At the workflow level:

Intent
  ↓
Plan
  ↓
Action
  ↓
Execution
  ↓
Observed State
  ↓
Postconditions
  ↓
Evidence
  ↓
Outcome

⸻

59. Final Definition

A postcondition is an explicit, evaluable statement of the state or effect that must be established after an Action for its semantic success to be recognized. Postconditions are evaluated against evidence, not assumptions, and may resolve to satisfied, not satisfied, or unknown.

The core invariant is:

Noema never treats “the executor said it completed” as equivalent to “the intended effect occurred.” An Action becomes semantically successful only when its required postconditions are established by sufficient evidence.