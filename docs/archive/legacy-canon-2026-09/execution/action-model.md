> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Action Model

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/action-model.md

⸻

1. Definition

The Action Model defines the canonical representation, semantics, lifecycle, and relationships of Actions within Noema.

An Action is a typed semantic operation that represents an operation a validated Intent may request to perform.

It answers:

What operation is intended to occur?

It does not by itself answer:

* Who may perform it?
* Whether it is currently permitted?
* Which Capability can perform it?
* How it is executed?
* What happened after execution?

Those concerns belong to Actor, Trust, Capability, Action Contract, Execution, Verification, and Outcome respectively.

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

The Action Model sits between semantic Intent and implementation.

⸻

3. Action in the Noema Model

The canonical relationship is:

Source of Intent
      │
      ▼
Intent
      │
      │ resolves to
      ▼
Action
      │
      │ bound to
      ▼
Action Instance
      │
      │ supported by
      ▼
Capability
      │
      │ evaluated by
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
Verification
      │
      ▼
Outcome

This relationship is foundational to Noema’s execution model.

⸻

4. Action vs Intent

An Intent represents desired meaning.

An Action represents an operation contained within that meaning.

Therefore:

Intent ≠ Action

Example:

Intent:
    "Move ₦100,000 from my savings account to my current account."
Action:
    transfer_money

The Intent carries semantic context such as:

Actor
Action
Resources
Parameters
Constraints
Context
Desired Outcome

The Action identifies the operation itself.

The Action Model must not absorb the complete semantics of Intent.

⸻

5. Action vs Capability

An Action describes what can be done conceptually.

A Capability describes an available bounded ability to perform an Action.

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

Capability availability is an execution concern, not a redefinition of Action semantics.

⸻

6. Action vs Action Contract

An Action is semantic.

An Action Contract is executable and scoped.

Example:

Action:
    refund_payment
Action Contract:
    refund payment_123
    amount = ₦50,000
    currency = NGN
    consumer = payment-service
    expires_at = ...

The Action is reusable semantic meaning.

The Action Contract binds a specific Action Instance to an authorized execution scope.

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

* stable
* machine-readable
* unique within its namespace
* implementation-independent

The identifier represents semantic identity, not a transport operation.

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

An Action description must not silently introduce additional Actions or execution scope.

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

The Action definition establishes the semantic schema for those inputs.

⸻

12. Action Parameters

Parameters instantiate an Action.

For example:

Action:
    refund_payment
Parameters:
    payment = payment_123
    amount = 50000
    currency = NGN
    reason = duplicate_charge

The Action definition specifies which parameters are possible or required.

The Intent supplies or determines their values through deterministic resolution and validation.

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

Conditional parameters may depend on other parameters or explicit Action semantics.

A missing required parameter prevents creation of a valid Action Instance.

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

These constraints contribute to deterministic validation.

They do not themselves establish authorization.

⸻

15. Action Preconditions

An Action may define semantic preconditions.

Example:

refund_payment
Precondition:
    payment.status = CAPTURED

The Action Model defines that the condition is semantically relevant.

It does not necessarily own the underlying state.

The authoritative enterprise system may provide the state used to establish whether the precondition currently holds.

Where multiple enterprise observations are required, State Reconciliation may be necessary before the precondition can be treated as satisfied.

⸻

16. Action Postconditions

Actions may define expected semantic postconditions.

Example:

refund_payment
Expected Postcondition:
    refund initiated

A postcondition describes the intended semantic effect.

It does not establish that the effect occurred.

Actual execution and verification determine what happened.

⸻

17. Action Semantics

An Action should define:

* What does this Action mean?
* What resources does it operate on?
* What parameters does it accept?
* What semantic conditions must hold?
* What effect does it request?

It should not define:

* Which HTTP endpoint to call
* Which database query to execute
* Which SDK method to invoke
* Which credentials to use

Those belong to the Capability, Integration, Action Contract, and Execution layers.

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

The exact resource must be resolved before consequential execution.

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

because the semantic role of each Resource is explicit.

The roles become part of Action Instance binding and Action Contract scope.

⸻

20. Action and Actor

Actions may define Actor requirements.

Example:

delete_customer

may require an authority class such as:

customer_admin

However, the Action itself does not grant authorization.

It defines semantic requirements that may be relevant to Trust evaluation.

Trust determines whether the actual resolved Actor may perform the specific Action against the specific target under current conditions.

⸻

21. Action Scope

An Action should have a clearly defined semantic scope.

For example:

refund_payment

means refunding a specific eligible payment.

It should not implicitly include:

close_account
send_email
delete_customer

unless those operations are explicitly modeled as part of a composite Action.

An Action must not silently expand its semantic or execution scope.

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

Technical atomicity is an execution property and must not be inferred from semantic atomicity.

⸻

23. Composite Actions

Some Intent expressions may resolve to multiple Actions.

Example:

"Refund the payment and notify the customer."

may resolve to:

refund_payment
send_notification

The Action Model should support composition without forcing unrelated operations into one Action definition.

Each Action retains its own semantics and execution boundary.

⸻

24. Action Composition

A composite execution graph may look like:

refund_payment
      │
      ▼
send_notification

where the second Action depends on verified successful completion of the first.

Alternatively:

refund_payment ─────┐
                    ├──→ complete
send_notification ──┘

where they are independent.

The dependency semantics must be explicit.

Noema must not infer dependency solely from textual ordering.

⸻

25. Action Dependencies

Actions may declare dependencies on other Action Instances.

Example:

notify_customer
requires:
    refund_payment.success

This allows Noema to model execution ordering without embedding implementation logic into the Action definition.

A dependency on success must refer to a verified execution condition rather than merely the issuance or acceptance of another Action Contract.

⸻

26. Action Idempotency

An Action definition should indicate its semantic repeatability characteristics.

For example:

get_customer

is generally repeatable.

Whereas:

charge_card

is not inherently idempotent.

The Action Model should expose this semantic property.

It does not replace the consumer’s concrete idempotency mechanism.

⸻

27. Idempotency Semantics

Possible conceptual classifications include:

SAFE_TO_REPEAT
IDEMPOTENCY_SUPPORTED
NOT_IDEMPOTENT
UNKNOWN

These classifications inform Action Contract and execution behavior.

They do not guarantee that a particular integration is idempotent.

Integration-specific idempotency behavior must be represented separately.

⸻

28. Reversibility

Actions may also have semantic reversibility characteristics.

Example:

create_invoice

may be reversible through:

cancel_invoice

But these are distinct Actions.

Noema must not assume:

Action A
+
failure
=
inverse Action A

unless a compensation or reversal relationship is explicitly modeled.

⸻

29. Destructive Actions

The Action Model should identify Actions with destructive or potentially irreversible effects.

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

Whereas:

calculate_quote

may be read-only.

A conceptual classification may include:

READ
CREATE
UPDATE
DELETE
TRANSACTION
COMMUNICATION
CONTROL

This taxonomy is illustrative and should evolve with the broader ontology.

Side-effect classification does not itself determine Risk or Trust.

⸻

31. Read vs Mutating Actions

A useful distinction is:

Read Action
    ↓
observes or retrieves state
Mutating Action
    ↓
requests a state change

Example:

get_customer
vs
update_customer

Trust requirements may differ significantly between them.

Read-only must not automatically be treated as non-consequential. Protected data access, reconciliation, or privileged investigation may still require deterministic Trust and authorization.

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

Risk characteristics describe the Action.

Risk evaluation determines the relevant decision for a specific Action Instance and context.

⸻

33. Action Versioning

Action semantics may evolve.

Therefore Actions should be versionable.

Example:

refund_payment:v1
refund_payment:v2

Version changes must be meaningful and controlled.

A consequential Action Contract must identify which Action semantics it references.

⸻

34. Semantic vs Implementation Versioning

Noema must distinguish:

semantic change

from:

implementation change

Changing:

HTTP endpoint

does not necessarily require a new Action version.

Changing the meaning of:

refund_payment

may require a new Action version.

Transport, integration, Capability, and Action Contract versions remain separate version dimensions.

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
    dependencies
    composition
}

This is a conceptual model, not yet the final wire schema.

⸻

36. Action Registry

Noema requires a canonical Action Registry for the Actions that form part of its execution ontology.

Conceptually:

Action Registry
├── transfer_money
├── refund_payment
├── create_invoice
├── cancel_subscription
├── update_customer
└── send_notification

The registry provides stable semantic definitions.

Registry entries must be versioned and preserve historical meaning.

⸻

37. Action Registry vs Capability Registry

These must remain separate.

Action Registry

Defines:

What does this operation mean?

Capability Registry

Defines:

What bounded ability is available to perform it, and through which execution boundary?

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

Neither registry should be treated as a substitute for the other.

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

The appropriate Capability may depend on Intent parameters, Context, enterprise configuration, policy, or explicit user preference.

If the distinction materially affects the requested outcome and cannot be resolved deterministically, clarification may be required.

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

A Capability represents an available bounded ability; an Action represents semantic meaning.

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

Noema must resolve the distinction before producing an executable Action Contract.

If the distinction remains materially ambiguous:

CLARIFY

and no executable Action Contract exists.

⸻

41. No Guessing at Action Boundaries

A model must not select an Action merely because it is statistically likely when the semantic consequences differ materially.

For example:

"Stop my subscription."

could mean:

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

Probabilistic interpretation may generate candidates.

Deterministic resolution determines whether a specific Action can be admitted for execution.

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

Actor resolved
authorization satisfied
policy satisfied
required evidence available
risk constraints satisfied

Therefore:

Precondition ≠ Authorization

An Action may be semantically valid while a specific Action Instance is not permitted to execute.

⸻

43. Action Postconditions vs Outcome

Similarly:

Postcondition

Describes the intended semantic effect.

Outcome

Describes what execution and verification establish actually happened.

Example:

Action:
    refund_payment
Expected Postcondition:
    refund initiated
Actual Outcome:
    refund transaction ID = xyz

The Action Model must not claim that the postcondition occurred merely because the Action Contract was issued or accepted.

⸻

44. Action and Context

Some Actions are context-sensitive.

Example:

approve_transaction

may only make sense when:

transaction.status = PENDING

Context provides information used to establish applicability.

Where current enterprise state is required, State Reconciliation may be necessary before Context can support an Action precondition.

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

Policy constrains whether a specific Action Instance may proceed.

⸻

46. Action and Risk

Risk may depend on Action characteristics.

Example:

transfer_money

has materially different risk characteristics from:

retrieve_account_balance

The Risk model can use Action metadata as one input.

Again:

Action Risk Characteristic
≠
Final Risk Decision

⸻

47. Action and Trust

The Trust Engine evaluates whether a specific instance of an Action may proceed.

For example:

Action:
    delete_account

does not mean:

all delete_account Actions are trusted

Trust evaluates the specific:

Actor
Action
Target
Context
Evidence
Policy
Authorization
Risk
Intent version

The Action Model defines semantics.

Trust makes the deterministic permission decision.

⸻

48. Action Instance

The distinction between Action Definition and Action Instance is fundamental.

Action Definition

refund_payment

Action Instance

refund_payment(
    payment = payment_123,
    amount = ₦50,000
)

The Action Definition defines what the operation means.

The Action Instance binds that meaning to specific resources and parameters.

The Action Contract represents the authorized execution scope of the Action Instance.

⸻

49. Action Instance Identity

An Action Instance may have its own identifier:

action_instance_id

This is useful when a composite Intent contains multiple instances of the same Action.

Example:

send_notification(customer_A)
send_notification(customer_B)

Both use:

Action:
    send_notification

but they are distinct Action Instances.

⸻

50. Action Lifecycle

The Action Definition itself is relatively static.

The Action Instance has an execution-oriented lifecycle:

IDENTIFIED
     ↓
BOUND
     ↓
VALIDATED
     ↓
READY_FOR_TRUST
     ↓
TRUSTED
     ↓
CONTRACTED
     ↓
EXECUTING
     ↓
VERIFYING
     ↓
COMPLETED / FAILED / UNKNOWN

These statuses describe the Action Instance lifecycle.

They should not be confused with:

* Action Registry lifecycle
* Trust outcomes
* Action Contract lifecycle
* Execution result
* Intent status

The canonical Trust outcome remains:

EXECUTE
CLARIFY
ESCALATE
REJECT

TRUSTED above is shorthand for an Action Instance having received the applicable Trust EXECUTE decision, not a fifth Trust outcome.

⸻

51. Action Lifecycle vs Contract Lifecycle

The Action Instance answers:

What operation is this specific instance of?

The Action Contract answers:

What exact operation has been authorized for execution?

Therefore:

Action Instance
      ↓
Trust
      ↓
Action Contract

The contract then crosses the execution boundary.

⸻

52. Action Definition Ownership

Noema should own the canonical semantic definition of Actions that form part of its execution ontology.

Execution consumers may provide implementation-specific metadata, but they should not redefine the semantic meaning of a canonical Action unilaterally.

Enterprise-specific domain configuration may determine which Actions exist or are supported in a particular environment, but such configuration must remain explicit and versioned.

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

A system must not be considered a valid Action consumer merely because it exposes a technically compatible API.

⸻

54. Action Compatibility

A Capability must be compatible with the Action definition.

Compatibility may include:

parameter support
resource support
semantic version
constraint support
execution semantics
verification semantics
idempotency semantics

A consumer must not claim to implement an Action if its behavior materially differs from the canonical Action semantics.

Semantic incompatibility requires a distinct Action or Capability version, explicit translation, or another governed compatibility mechanism.

⸻

55. Action Contract Generation

The Action Model supplies the semantic schema used to construct an Action Contract.

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

The Action Contract adds execution scope, validity, consumer binding, provenance, and other execution-specific constraints.

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

authorization = satisfied
policy = satisfied
risk = satisfied

Action Contract

transfer_money(
    source = account_123,
    destination = account_456,
    amount = 100000,
    currency = NGN
)

The contract remains subject to execution-time validation and verification.

⸻

57. Example: Ambiguous Action

Source of Intent:

"Stop my subscription."

Possible Actions:

cancel_subscription
pause_subscription
disable_auto_renewal

If Context and Intent semantics cannot deterministically distinguish them:

Action = unresolved

Therefore:

No Action Contract

and:

Trust → CLARIFY

No probabilistic preference should silently become an executable Action.

⸻

58. Example: Valid Action, Blocked Execution

Intent:

Delete customer account.

Action:

delete_customer_account

Validation:

VALID

Trust:

REJECT

because policy prohibits the operation.

The Action exists.

The Intent can be semantically valid.

Execution is still prohibited.

This demonstrates:

Action validity
≠
execution authorization

⸻

59. Example: Valid Action, No Capability

Action:

refund_payment

Validation:

VALID

Trust:

EXECUTE

Capability:

payments.refund unavailable

The Action remains valid.

However, no executable Action Contract can be issued to a nonexistent or unavailable Capability.

The execution journey may enter an operational state such as:

WAITING_FOR_CAPABILITY

This is not a Trust outcome.

⸻

60. Hard Boundary Between Semantics and Execution

The Action Model participates in the deterministic execution boundary:

Probabilistic
    ↓
interpret / propose candidate Action
========== HARD BOUNDARY ==========
Deterministic
    ↓
schema validation
Action resolution
parameter validation
resource binding
State Reconciliation
Trust
Capability binding
Action Contract
Execution
Verification

The model may propose an Action candidate.

It cannot directly create an executable Action instance or bypass the Action Registry, Capability Registry, Trust, or Action Contract boundary.

⸻

61. Action Model Invariants

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

An Action does not imply successful Outcome.

Invariant 7

Action semantics must be deterministic.

Invariant 8

Action parameters must be explicitly typed.

Invariant 9

Action resource roles must be explicit where multiple Resources are involved.

Invariant 10

Material semantic changes require controlled versioning.

Invariant 11

An Action must not silently expand its semantic or execution scope.

Invariant 12

Capabilities implement Actions; they do not redefine their canonical semantics.

Invariant 13

An Action Contract binds a specific Action Instance to an authorized execution scope.

Invariant 14

Ambiguous Action selection must not be resolved through unsupported guessing.

Invariant 15

Action preconditions are distinct from Trust authorization conditions.

Invariant 16

Action postconditions are not evidence that the Action succeeded.

Invariant 17

Business-state truth remains with the authoritative enterprise system.

Invariant 18

Action Instance identity must distinguish multiple instances of the same Action.

Invariant 19

Action composition and dependencies must be explicit.

Invariant 20

Semantic idempotency characteristics must not be confused with an integration’s concrete idempotency mechanism.

Invariant 21

Reversal and compensation must be explicitly modeled and must not be inferred from failure.

Invariant 22

Risk characteristics are inputs to Risk evaluation and do not themselves constitute a risk decision.

Invariant 23

The Action Model must remain implementation-independent.

Invariant 24

No model output may directly become an executable Action without passing the deterministic validation and execution boundary.

Invariant 25

State-dependent Action preconditions must be established from appropriate current enterprise observations or reconciliation.

Invariant 26

An unavailable Capability does not invalidate the semantic definition of an Action.

Invariant 27

Read-only Actions may still be consequential and may require Trust and authorization.

Invariant 28

Historical Action semantics must remain stable for the version referenced by historical execution records.

⸻

62. Canonical Mental Model

The Action Model can be reduced to:

Intent
"What does the Source of Intent want?"
        ↓
Action
"What operation does that Intent represent?"
        ↓
Action Instance
"On what Resources, with what Parameters?"
        ↓
Capability
"What bounded execution ability can perform it?"
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
Verification
"Can we establish what happened?"
        ↓
Outcome
"What did the execution journey establish?"

⸻

63. Final Definition

The Action Model defines Actions as stable, typed, implementation-independent semantic operations that can be identified from Intent, instantiated against resolved Resources and Parameters, evaluated by deterministic Trust, bound to an available Capability, and expressed as an explicit Action Contract for execution.

The core invariant is:

Noema separates what an operation means from how it is implemented, whether it is permitted, and whether it actually succeeded. An Action defines the operation; an Action Instance binds it to a specific target and parameters; Trust determines whether that instance may proceed; the Action Contract scopes its execution; and the execution and verification layers establish the actual Outcome.