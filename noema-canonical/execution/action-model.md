Action Model

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/action-model.md

⸻

1. Definition

The Action Model defines the canonical representation, semantics, lifecycle, and relationships of Actions within Noema.

An Action is the executable expression of an Intent’s desired change.

It answers:

What operation is intended to occur?

It does not by itself answer:

* Who may perform it?
* Whether it is currently permitted?
* How it is executed?
* What happened after execution?

Those concerns belong to Actor, Trust, Capability, Execution, and Outcome respectively.

⸻

2. Core Principle

An Action is a typed semantic operation, not a natural-language instruction and not an implementation-specific API call.

For example:

refund_payment

is an Action.

This:

"Please refund John's payment."

is an expression of Intent.

And this:

POST /payments/123/refund

is an implementation mechanism.

The Action Model sits between them.

⸻

3. Action in the Noema Model

The canonical relationship is:

Actor
  │
  │ expresses
  ▼
Intent
  │
  │ resolves to
  ▼
Action
  │
  │ requires
  ▼
Capability
  │
  │ governed by
  ▼
Trust
  │
  │ produces
  ▼
Action Contract
  │
  │ consumed by
  ▼
Execution System
  │
  │ produces
  ▼
Outcome

This relationship is foundational to Noema’s ontology.

⸻

4. Action vs Intent

An Intent represents desired meaning.

An Action represents the operation contained within that meaning.

Therefore:

Intent ≠ Action

Example:

Intent:
"Move ₦100,000 from my savings account to my current account."
Action:
transfer_money

The Intent carries:

Actor
Action
Resources
Parameters
Constraints
Context
Desired Outcome

The Action identifies the operation itself.

⸻

5. Action vs Capability

An Action describes what can be done conceptually.

A Capability describes what an execution system is able to do.

Example:

Action:
refund_payment
Capability:
payments.refund.v2

Therefore:

Action
   ↓
may be fulfilled by
   ↓
Capability

An Action can exist even when no currently available Capability can execute it.

⸻

6. Action vs Action Contract

An Action is semantic.

An Action Contract is executable and scoped.

Action:
refund_payment
Action Contract:
refund payment_123
amount = ₦50,000
currency = NGN
consumer = payment-service
expires_at = ...

The contract binds a general Action to a specific execution instance.

⸻

7. Action vs API Operation

An Action must not be defined in terms of an API endpoint.

Bad canonical model:

Action:
POST /v1/payments/{id}/refund

Better:

Action:
refund_payment

The consumer may implement that Action through:

HTTP
RPC
GraphQL
SQL
SDK
Queue
Workflow
CLI

Noema remains implementation-agnostic.

⸻

8. Action Identity

Every canonical Action should have a stable identifier.

Example:

action_id:
refund_payment

The identifier should be:

stable
machine-readable
unique within its namespace
implementation-independent

⸻

9. Action Name

A human-readable name may accompany the identifier.

Example:

action_id:
refund_payment
name:
Refund Payment

The identifier is canonical.

The display name is descriptive.

⸻

10. Action Description

Each Action should have a precise semantic description.

Example:

refund_payment
Description:
Return funds associated with an eligible payment
to the original payer according to applicable rules.

Descriptions should define semantics, not implementation details.

⸻

11. Action Inputs

Every Action should define its required inputs.

Example:

refund_payment {
    payment
    amount
    currency
    reason
}

Inputs should be typed.

⸻

12. Action Parameters

Parameters instantiate the Action.

For example:

Action:
refund_payment
Parameters:
payment = payment_123
amount = 50000
currency = NGN
reason = duplicate_charge

The Action definition specifies what parameters are possible or required.

The Intent supplies their values.

⸻

13. Required vs Optional Parameters

The Action Model should distinguish:

required
optional
conditional

Example:

refund_payment {
    payment       required
    amount        required
    currency      required
    reason        optional
    note          conditional
}

Conditional parameters may depend on other values.

⸻

14. Parameter Constraints

Parameters may have constraints.

Example:

amount:
    type = Money
    minimum = 0

Another:

currency:
    allowed = [NGN, USD, GBP]

These constraints contribute to Validation.

⸻

15. Action Preconditions

An Action may define semantic preconditions.

Example:

refund_payment
Precondition:
payment.status = CAPTURED

This does not necessarily mean Noema owns the payment state.

The execution consumer may be the authoritative source for the precondition.

Noema can represent the requirement without becoming the system of record.

⸻

16. Action Postconditions

Actions may define expected semantic postconditions.

Example:

refund_payment
Expected Outcome:
payment refund initiated

Postconditions should describe the intended business effect, not falsely assert that it occurred.

The actual result comes from the execution consumer.

⸻

17. Action Semantics

An Action should define:

What does this Action mean?
What resources does it operate on?
What parameters does it accept?
What conditions must hold?
What effect does it request?

It should not define:

Which HTTP endpoint to call?
Which database query to execute?
Which SDK method to invoke?

Those belong to the Capability / Consumer layer.

⸻

18. Action Resource Binding

Actions generally operate on one or more Resources.

Example:

Action:
update_customer
Resource:
customer_123

or:

Action:
transfer_money
Resources:
source_account
destination_account

The Action Model should specify which resource roles are required.

⸻

19. Resource Roles

For multi-resource Actions, resources should have semantic roles.

Example:

transfer_money {
    source_account
    destination_account
}

This is preferable to:

resources = [account_1, account_2]

because the meaning of each resource is explicit.

⸻

20. Action and Actor

Actions may have Actor requirements.

Example:

delete_customer

may require:

Actor:
customer_admin

However, the Action itself does not grant authorization.

It merely defines what the operation is and potentially what authority class is required.

Trust determines whether the actual Actor may perform it.

⸻

21. Action Scope

An Action should have a clearly defined semantic scope.

For example:

refund_payment

means refunding a specific payment.

It should not implicitly include:

close_account
send_email
delete_customer

unless those are explicitly modeled as part of a composite Action.

⸻

22. Atomic Actions

An Atomic Action represents one semantic operation.

Examples:

create_invoice
refund_payment
cancel_subscription
update_profile
approve_transaction

Atomic does not necessarily mean technically indivisible.

It means the Action has one primary semantic purpose.

⸻

23. Composite Actions

Some Intent expressions may resolve to multiple Actions.

Example:

"Refund the payment and notify the customer."

may resolve to:

refund_payment
send_notification

The Action Model should support composition without forcing unrelated operations into one Action definition.

⸻

24. Action Composition

A composite execution graph may look like:

refund_payment
      │
      ▼
send_notification

where the second Action depends on the first succeeding.

Alternatively:

refund_payment ─────┐
                    ├──→ complete
send_notification ──┘

where they are independent.

The dependency semantics must be explicit.

⸻

25. Action Dependencies

Actions may declare dependencies on other Actions.

Example:

notify_customer
requires:
refund_payment.success

This allows Noema to model execution ordering without embedding implementation logic.

⸻

26. Action Idempotency

An Action definition should indicate whether repeated execution is semantically safe.

For example:

get_customer

is generally naturally repeatable.

Whereas:

charge_card

is not inherently idempotent.

The Action Model should expose this semantic property.

⸻

27. Idempotency Semantics

Possible conceptual classifications:

SAFE_TO_REPEAT
IDEMPOTENCY_SUPPORTED
NOT_IDEMPOTENT
UNKNOWN

This informs Action Contract and consumer behavior.

It does not replace the consumer’s actual idempotency mechanism.

⸻

28. Reversibility

Actions may also have semantic reversibility.

Example:

create_invoice

may be reversible through:

cancel_invoice

But these are distinct Actions.

Noema should not assume:

Action A
+
failure
=
inverse Action A

unless explicitly modeled.

⸻

29. Destructive Actions

The Action Model should identify Actions with destructive or irreversible effects.

Examples:

delete_account
delete_data
terminate_service
close_account

These characteristics can contribute to Risk and Trust evaluation.

The Action itself does not decide whether execution is allowed.

⸻

30. Side Effects

Actions should declare meaningful side-effect characteristics.

For example:

send_notification

has an external side effect.

calculate_quote

may be read-only.

A conceptual classification:

READ
CREATE
UPDATE
DELETE
TRANSACTION
COMMUNICATION
CONTROL

This taxonomy is illustrative and should evolve with the broader ontology.

⸻

31. Read vs Mutating Actions

A useful distinction is:

Read Action
    ↓
observes state
Mutating Action
    ↓
requests state change

Example:

get_customer

vs:

update_customer

Trust requirements may differ significantly between them.

⸻

32. Action Risk Characteristics

Actions may carry semantic risk characteristics.

Example:

delete_account
    destructive = true

or:

transfer_money
    financial = true

These attributes provide inputs to the Risk model.

They do not themselves constitute a risk decision.

⸻

33. Action Versioning

Action semantics may evolve.

Therefore Actions should be versionable.

Example:

refund_payment:v1
refund_payment:v2

Version changes should be meaningful and controlled.

A consumer should know which Action semantics a contract refers to.

⸻

34. Semantic Versioning

The exact versioning strategy is an implementation decision.

However, Noema should distinguish:

semantic change

from:

implementation change

Changing:

HTTP endpoint

does not necessarily require a new Action version.

Changing:

meaning of refund_payment

may.

⸻

35. Action Schema

Conceptually:

Action {
    id
    version
    name
    description
    inputs
    resources
    preconditions
    postconditions
    characteristics {
        mutability
        idempotency
        reversibility
        destructiveness
        risk
    }
}

This is a conceptual model, not yet the final wire schema.

⸻

36. Action Registry

Noema will likely require a canonical Action Registry.

Conceptually:

Action Registry
├── transfer_money
├── refund_payment
├── create_invoice
├── cancel_subscription
├── update_customer
└── send_notification

The registry provides stable semantic definitions.

⸻

37. Action Registry vs Capability Registry

These should remain separate.

Action Registry

Defines:

What does this operation mean?

Capability Registry

Defines:

Who/what can perform it?

Example:

Action Registry
    refund_payment
          │
          ▼
Capability Registry
    payments.refund
          │
          ▼
Consumer
    payment-service

⸻

38. Multiple Capabilities for One Action

One Action may be executable through multiple Capabilities.

Example:

Action:
send_notification

Capabilities:

email.send
sms.send
push.send

The Intent may specify a communication preference or the system may require clarification.

The Capability layer determines what execution mechanisms are available.

⸻

39. One Capability for Multiple Actions

A Capability may expose multiple Actions.

Example:

payments
├── charge_payment
├── refund_payment
├── cancel_payment
└── retrieve_payment

Capability is therefore not synonymous with Action.

⸻

40. Action Selection

An Intent may contain enough semantic information to identify an Action.

Example:

"Refund the payment."
        ↓
refund_payment

If multiple Actions are semantically plausible:

cancel_payment
refund_payment
void_payment

Noema must resolve the distinction before producing an executable contract.

If ambiguity remains material:

WAITING_FOR_CLARIFICATION

⸻

41. No Guessing at Action Boundaries

A model should not choose an Action merely because it is statistically likely when the semantic consequences differ materially.

For example:

"Stop my subscription."

could potentially mean:

cancel_subscription
pause_subscription
disable_auto_renewal

If the distinction matters:

Ambiguous Intent
        ↓
Clarification

not:

LLM probability
        ↓
cancel_subscription

⸻

42. Action Preconditions vs Trust Conditions

This distinction is important.

Action Precondition

Describes what must be true for the Action to make semantic sense.

Example:

payment.status = CAPTURED

Trust Condition

Describes what must be satisfied for Noema to permit execution.

Example:

Actor authorized
policy satisfied
approval obtained

Therefore:

Precondition ≠ Authorization

⸻

43. Action Postconditions vs Outcome

Similarly:

Postcondition

Describes the intended semantic effect.

Outcome

Describes what actually happened.

Example:

Action:
refund_payment
Expected postcondition:
refund initiated
Actual outcome:
refund transaction ID = xyz

The Action Model must not claim the postcondition occurred simply because the Action Contract was issued.

⸻

44. Action and Context

Some Actions are context-sensitive.

Example:

approve_transaction

may only make sense when:

transaction.status = PENDING

Context determines whether the Action is applicable.

The Context Model supplies that information.

⸻

45. Action and Policy

Policy can constrain an Action.

Example:

Action:
transfer_money
Policy:
Transfers > ₦5M require two-person approval.

The Action remains:

transfer_money

Policy does not redefine the Action.

It governs its execution.

⸻

46. Action and Risk

Risk may depend on Action characteristics.

Example:

transfer_money

has materially different risk characteristics from:

retrieve_account_balance

The Risk Engine can use Action metadata as one input.

Again:

Action risk characteristic
≠
final risk decision

⸻

47. Action and Trust

The Trust Engine evaluates whether a specific instance of an Action may proceed.

For example:

Action:
delete_account

does not mean:

all delete_account Actions are trusted

Trust evaluates:

this Actor
this Resource
this Action
this Context
this Evidence
this Policy
this Risk

⸻

48. Action Instance

The distinction between Action Definition and Action Instance is useful.

Action Definition

refund_payment

Action Instance

refund_payment(
    payment = payment_123,
    amount = ₦50,000
)

The Action Contract represents the authorized execution of an Action Instance.

⸻

49. Action Instance Identity

An Action Instance may have its own identifier:

action_instance_id

This can be useful when a composite Intent contains multiple instances of the same Action.

Example:

send_notification(customer_A)
send_notification(customer_B)

Both use:

Action:
send_notification

but are distinct instances.

⸻

50. Action Lifecycle

The Action Definition itself is relatively static.

The Action Instance has a lifecycle:

IDENTIFIED
     ↓
BOUND
     ↓
VALIDATED
     ↓
TRUSTED
     ↓
CONTRACTED
     ↓
EXECUTING
     ↓
COMPLETED / FAILED

This lifecycle should not be confused with the Action Definition’s registry lifecycle.

⸻

51. Action Lifecycle vs Contract Lifecycle

The Action Instance answers:

What operation is this?

The Action Contract answers:

What exact operation has been authorized for execution?

Therefore:

Action Instance
      ↓
Trust
      ↓
Action Contract

⸻

52. Action Definition Ownership

Noema should own the canonical semantic definition of Actions that form part of its execution ontology.

Execution consumers may provide implementation-specific metadata, but they should not redefine the semantic meaning of a canonical Action unilaterally.

⸻

53. Consumer Mapping

A consumer may declare:

Capability:
payments.refund
implements:
refund_payment

This establishes:

Action
   ↓
Capability
   ↓
Consumer

The mapping must be explicit.

⸻

54. Action Compatibility

A Capability must be compatible with the Action definition.

Compatibility may include:

parameter support
resource support
semantic version
constraint support
execution semantics

A consumer must not claim to implement an Action if its behavior materially differs from the canonical Action semantics.

⸻

55. Action Contract Generation

The Action Model supplies the semantic schema used to construct the Action Contract.

Conceptually:

Action Definition
       +
Action Instance
       +
Trust Decision
       +
Capability
       ↓
Action Contract

⸻

56. Example: Transfer

Action Definition

transfer_money

Required Resources

source_account
destination_account

Required Parameters

amount
currency

Action Instance

source = account_123
destination = account_456
amount = 100000
currency = NGN

Trust

authorization = ALLOW
policy = SATISFIED
risk = ACCEPTABLE

Contract

transfer_money(
    source = account_123,
    destination = account_456,
    amount = 100000,
    currency = NGN
)

⸻

57. Example: Ambiguous Action

User says:

"Stop my subscription."

Possible Actions:

cancel_subscription
pause_subscription
disable_auto_renewal

If context cannot deterministically distinguish them:

Action = unresolved

Therefore:

No Action Contract

and:

WAITING_FOR_CLARIFICATION

⸻

58. Example: Valid Action, Blocked Execution

Intent:
Delete customer account.
Action:
delete_customer_account.
Validation:
VALID.
Trust:
BLOCKED_BY_POLICY.

The Action exists.

The Intent is valid.

But execution is prohibited.

This demonstrates:

Action validity ≠ execution authorization

⸻

59. Example: Valid Action, No Capability

Action:
refund_payment
Validation:
VALID
Trust:
potentially ALLOW
Capability:
payments.refund unavailable

The Action remains valid.

The execution state may become:

WAITING_FOR_CAPABILITY

No Action Contract should be issued to a nonexistent consumer.

⸻

60. Action Model Invariants

Invariant 1

An Action is a semantic operation.

Invariant 2

An Action is not an API endpoint.

Invariant 3

An Action is not an Intent.

Invariant 4

An Action does not grant authorization.

Invariant 5

An Action does not imply execution.

Invariant 6

An Action does not imply successful outcome.

Invariant 7

Action semantics must be deterministic.

Invariant 8

Action parameters must be explicitly typed.

Invariant 9

Material semantic changes require controlled versioning.

Invariant 10

An Action must not silently expand its execution scope.

Invariant 11

Capabilities implement Actions; they do not redefine them.

Invariant 12

An Action Contract binds a specific Action Instance to an authorized execution scope.

Invariant 13

Ambiguous Action selection must not be resolved through unsupported guessing.

Invariant 14

Business-state truth remains with the authoritative execution system.

⸻

61. Canonical Mental Model

The Action Model can be reduced to:

Intent
"What does the Actor want?"
        ↓
Action
"What operation does that Intent represent?"
        ↓
Action Instance
"On what resources, with what parameters?"
        ↓
Capability
"What system can perform it?"
        ↓
Trust
"May this specific instance proceed?"
        ↓
Action Contract
"Exactly what may be executed?"
        ↓
Execution
"Perform it."
        ↓
Outcome
"What actually happened?"

⸻

62. Final Definition

The Action Model defines Actions as stable, typed, implementation-independent semantic operations that can be instantiated by an Intent, evaluated by Trust, bound to an available Capability, and expressed as an explicit Action Contract for execution.

The core invariant is:

Noema separates what an operation means from how it is implemented, whether it is permitted, and whether it actually succeeded. An Action defines the operation; Trust authorizes its instance; the Action Contract scopes its execution; and the consumer establishes the actual Outcome.