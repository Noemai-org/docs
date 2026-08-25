Action Contracts

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: 04-execution/action-contracts.md

⸻

1. Definition

An Action Contract is the explicit, typed, machine-executable contract produced by Noema that specifies what an execution consumer is authorized to execute, under which conditions, and with what constraints.

The Action Contract is the boundary between:

Intent

and:

Execution

It is the mechanism through which Noema converts a trusted human Intent into an explicit execution instruction without performing the Action itself.

⸻

2. The Core Boundary

The canonical flow is:

User Expression
      ↓
Intent
      ↓
Resolution
      ↓
Validation
      ↓
Trust Evaluation
      ↓
READY
      ↓
Action Contract
      ↓
Execution Consumer
      ↓
Business System

The critical boundary is:

                 NOEMA
──────────────────────────────────
Intent → Trust → Action Contract
──────────────────────────────────
                 ↓
          EXECUTION CONSUMER
                 ↓
          Business System

Noema determines what is permitted to happen.

The execution consumer determines how it actually happens.

⸻

3. Why Action Contracts Exist

A model-generated instruction is not sufficient for consequential execution.

For example:

"Refund John's payment."

is an Intent.

It is not yet an executable instruction.

Noema must establish:

Action:
refund_payment
Actor:
customer_service_agent
Resource:
payment_123
Amount:
₦50,000
Authorization:
approved
Policy:
satisfied
Constraints:
satisfied

Only then can Noema produce a contract that an execution consumer can safely consume.

⸻

4. Intent vs Action Contract

An Intent represents:

What the Actor wants accomplished.

An Action Contract represents:

What an execution consumer is authorized and instructed to perform.

Therefore:

Intent ≠ Action Contract

An Intent is semantic.

An Action Contract is operational.

⸻

5. Action Contract Is Not an API Request

An API request says:

"Call this endpoint with these parameters."

An Action Contract says:

"This specific Action is authorized for this specific Intent, under these explicit conditions."

The execution consumer may translate the contract into:

HTTP
RPC
SQL
SDK call
Queue message
Workflow invocation
CLI command

Noema does not need to know which.

⸻

6. Action Contract as a Typed Boundary

Action Contracts should be strongly typed.

Conceptually:

ActionContract<A, P, C>

where:

A = Action
P = Parameters
C = Conditions

A contract should make invalid execution states difficult or impossible to represent.

⸻

7. Canonical Contract Structure

A conceptual Action Contract contains:

ActionContract {
    contract_id
    intent_id
    action
    actor
    resource
    parameters
    constraints
    authorization
    policy
    evidence
    validity
    execution
}

The exact wire representation remains an implementation concern.

⸻

8. Contract Identity

Every Action Contract requires a unique identity.

contract_id

The identity provides:

traceability
idempotency
auditability
correlation
execution tracking

The contract should also reference the originating:

intent_id

⸻

9. Intent Lineage

An Action Contract must preserve lineage to the Intent that produced it.

Conceptually:

contract.intent_id
contract.intent_version

This allows Noema to answer:

Why does this execution contract exist?

The answer must lead back to the original Intent and its Trust evaluation.

⸻

10. Action

The contract identifies the canonical Action.

Example:

action:
    refund_payment

The Action must reference a known capability in Noema’s ontology.

An execution consumer should not receive arbitrary natural-language instructions as the Action identifier.

Prefer:

refund_payment

over:

"Please refund the customer's payment."

⸻

11. Actor

The contract identifies the Actor on whose authority the Action proceeds.

Example:

actor:
    customer_service_agent_42

The Actor is not necessarily the Model.

This distinction is fundamental.

The Model may interpret an Intent.

The Actor is the entity whose authority is relevant to execution.

⸻

12. Resource

The contract identifies the Resource against which the Action applies.

Example:

resource:
    payment_123

For Actions involving multiple resources:

resources:
    source_account
    destination_account

The resources must be explicitly bound.

⸻

13. Parameters

The contract contains the canonical parameters required by the Action.

Example:

parameters {
    amount: 50000
    currency: NGN
    reason: "duplicate charge"
}

Parameters must be typed according to the Action definition.

⸻

14. No Natural-Language Ambiguity

The execution consumer should not have to infer meaning from prose.

Bad:

instruction:
"Refund roughly fifty thousand naira to John's account."

Better:

action:
refund_payment
parameters:
    amount: 50000
    currency: NGN
    payment_id: payment_123

The execution boundary should be explicit.

⸻

15. Constraints

The Action Contract may carry execution constraints.

Examples:

maximum_amount
allowed_resource
expiration
required_sequence
idempotency_key
execution_window

These constraints become part of the executable boundary.

⸻

16. Authorization

The contract should carry sufficient authorization context for the consumer to verify that execution is permitted.

Conceptually:

authorization {
    decision: ALLOW
    authority: role_or_policy_reference
    evaluated_at: timestamp
    evaluation_id: trust_evaluation_id
}

The exact representation depends on the authorization architecture.

⸻

17. Policy

The contract may reference the policies that governed the Trust decision.

Example:

policy {
    policy_set: payments.v3
    decision: satisfied
}

This provides execution provenance.

⸻

18. Evidence

An Action Contract should reference the evidence supporting the Trust decision when the consumer needs that information.

Example:

evidence [
    identity_verified
    payment_exists
    approval_456
]

The contract should generally reference evidence rather than embedding unnecessary evidence payloads.

⸻

19. Validity

Contracts should have an explicit validity period where required.

Example:

validity {
    issued_at
    expires_at
}

This prevents a contract generated under old conditions from being executed indefinitely.

⸻

20. Execution Context

The contract should identify execution-related metadata.

Example:

execution {
    consumer
    idempotency_key
    mode
    correlation_id
}

The consumer identifier may be:

payment-service
crm-service
warehouse-service
workflow-engine

⸻

21. Contract Status

The Action Contract itself should have a lifecycle.

Conceptually:

ISSUED
ACCEPTED
EXECUTING
COMPLETED
FAILED
EXPIRED
REJECTED
REVOKED

However, this should not be confused with the Trust State Machine.

Trust determines eligibility.

Contract status tracks the contract’s execution lifecycle.

⸻

22. Trust vs Contract

These concepts must remain separate.

Trust:
"May this Action execute?"
Action Contract:
"What exactly may execute?"
Execution:
"Did the consumer execute it?"

Therefore:

READY
   ↓
Action Contract
   ↓
Consumer

⸻

23. Contract Creation Preconditions

An Action Contract must not be created for execution unless the required conditions have been satisfied.

Conceptually:

Intent resolved
AND
Intent validated
AND
Trust = READY
AND
Action capability exists
AND
required parameters are bound

Only then:

Action Contract → issued

⸻

24. No Contract From Ambiguous Intent

Example:

"Delete the account."

If the Actor has three accounts:

account_a
account_b
account_c

Noema must not generate:

resource = account_a

based on probability.

Instead:

WAITING_FOR_CLARIFICATION

No executable contract exists.

⸻

25. Contract Immutability

Once issued, an Action Contract should be treated as immutable.

If something materially changes:

parameters
resource
actor
authorization
policy
constraints
validity

Noema should generate a new contract.

Do not silently mutate the existing contract.

⸻

26. Why Immutability Matters

Suppose:

Contract C1
amount = ₦1M

was approved.

Someone changes it to:

amount = ₦10M

If the same Contract ID remains:

C1

the audit trail becomes ambiguous.

Instead:

C1 → ₦1M
C2 → ₦10M

with a new Trust evaluation.

⸻

27. Contract Versioning

Where contract evolution is required:

contract_id
version

may identify versions.

But a material semantic change should generally produce a new executable contract rather than mutating a live contract.

⸻

28. Consumer-Side Execution

The execution consumer owns the mechanics.

Example:

Noema
  ↓
Action Contract:
refund_payment(payment_123)
  ↓
Payment Service
  ↓
Stripe / Paystack / internal ledger

Noema does not need to know the implementation details of the payment service.

⸻

29. Consumer-Side Validation

The consumer may perform final validation.

Example:

Noema:
READY
Payment Service:
payment_123 already refunded

The consumer can reject execution.

This is correct.

The consumer owns authoritative business-state validation at the point of mutation.

⸻

30. Consumer Must Not Expand the Contract

A consumer should not interpret a contract as permission to perform additional Actions.

If the contract says:

refund_payment(payment_123)

the consumer must not also:

close_customer_account()

unless that Action is explicitly part of the contract’s authorized composition.

⸻

31. Contract Scope

The contract defines the maximum permitted execution scope.

Conceptually:

Contract Scope =
    Action
    +
    Actor
    +
    Resource
    +
    Parameters
    +
    Constraints

Execution outside this scope is unauthorized.

⸻

32. Least Authority

Action Contracts should follow the principle of least authority.

Instead of:

"Payment service, do whatever is necessary."

Noema should issue:

refund_payment
payment_id = payment_123
amount = ₦50,000

The consumer receives only the authority required for the specific Action.

⸻

33. Contract Composition

Multiple Actions may be composed.

Example:

Intent:
"Refund the payment and notify the customer."

could produce:

Contract A:
refund_payment(payment_123)
Contract B:
send_notification(customer_123)

The composition semantics must be explicit.

Noema should not assume:

A success ⇒ B must execute

unless the Intent specifies such dependency.

⸻

34. Dependencies

Contracts may express dependencies.

Example:

Contract A:
refund payment
Contract B:
notify customer
Dependency:
B requires A.success

This creates:

A
↓ success
B

rather than treating the two Actions as unrelated.

⸻

35. Atomicity

If a composite Intent requires atomic execution, the contract must explicitly express that requirement.

For example:

atomic = true

The consumer then needs to support the requested atomicity semantics.

Noema must not imply atomicity merely because multiple Actions came from one Intent.

⸻

36. Idempotency

Consequential Action Contracts should support idempotency where applicable.

Example:

idempotency_key:
contract_7f3a...

If the consumer receives the same contract twice:

C1
C1

it should be able to distinguish:

duplicate delivery

from:

new Action

⸻

37. Replay

Contract replay must be explicitly controlled.

A completed contract should not automatically be executable again.

For example:

COMPLETED
+
replay request

should require explicit replay semantics.

This is especially important for:

payments
deletions
notifications
external mutations

⸻

38. Expiration

A contract can expire.

Example:

issued_at:
10:00
expires_at:
10:05

At 10:06:

EXECUTION REQUEST
       ↓
EXPIRED

The consumer should reject it unless a new contract is issued.

⸻

39. Revocation

A previously issued contract may need to be revoked.

Example:

Contract:
READY
Authorization:
revoked

The contract becomes:

REVOKED

where the execution architecture supports revocation.

⸻

40. Revocation Is Not Guaranteed

If execution has already crossed an irreversible external boundary, revocation may be impossible.

Therefore:

issued
≠
reversible

Noema should model revocation semantics explicitly.

⸻

41. Execution Acknowledgement

The consumer should acknowledge receipt of a contract.

Conceptually:

ISSUED
   ↓
ACCEPTED

Acceptance means:

The consumer has accepted responsibility for processing the contract.

It does not mean:

The Action succeeded.

⸻

42. Execution Result

The consumer should return a structured result.

Conceptually:

ExecutionResult {
    status
    contract_id
    outcome
    evidence
    error
}

Possible status:

SUCCESS
FAILED
REJECTED
UNKNOWN

⸻

43. Unknown Execution Outcome

Distributed systems can produce:

request sent
+
network failure
=
unknown whether Action occurred

The consumer must not falsely report:

FAILED

if it cannot establish whether the mutation happened.

This is why idempotency and reconciliation matter.

⸻

44. Execution Contract vs Business State

An Action Contract is not business state.

Example:

Contract:
refund payment_123

does not mean:

payment_123.refunded = true

Only the authoritative business system can establish that.

⸻

45. Contract Evidence

After execution, the consumer may return evidence:

payment_id
transaction_id
provider_reference
timestamp
result

This becomes part of the execution record and potentially the Intent’s Outcome.

⸻

46. Auditability

An Action Contract should allow an auditor to reconstruct:

Who requested it?
What Intent produced it?
What Action was authorized?
What Trust evaluation authorized it?
What evidence supported the decision?
What consumer received it?
When was it executed?
What happened?

This is one of the primary reasons Action Contracts exist.

⸻

47. Contract Provenance

Conceptually:

contract_id
    ↓
intent_id
    ↓
intent_version
    ↓
validation_id
    ↓
trust_evaluation_id
    ↓
evidence
    ↓
policy versions
    ↓
execution result

This creates a complete causal chain.

⸻

48. Contract Security

Action Contracts should be integrity-protected.

Depending on architecture, this may involve:

signatures
MACs
short-lived credentials
capability tokens
secure transport
consumer authentication

The precise mechanism is implementation-specific.

The principle is not:

“The consumer trusts Noema because it is Noema.”

The principle is:

The consumer can cryptographically or otherwise reliably establish the authenticity and integrity of the contract.

⸻

49. Contract Audience

A contract should identify its intended consumer where relevant.

Example:

consumer:
payment-service

A contract intended for one consumer should not automatically be accepted by another.

⸻

50. Contract Non-Transferability

Unless explicitly designed otherwise:

Contract C

should not be transferable from:

payment-service

to:

account-service

The Action and consumer binding are part of the execution boundary.

⸻

51. Capability Binding

The contract should map to a known Capability.

Conceptually:

Action
   ↓
Capability
   ↓
Execution Consumer

Example:

Action:
refund_payment
Capability:
payments.refund
Consumer:
payment-service

⸻

52. Action Contract and Capability

An Action is semantic.

A Capability is an available ability to perform an Action.

An Action Contract binds them:

Intent:
refund payment
Action:
refund_payment
Capability:
payments.refund
Contract:
execute this specific refund

⸻

53. Noema Does Not Own Business State

The Action Contract should not attempt to duplicate the entire business domain.

For example, Noema should not become the source of truth for:

payment balances
inventory counts
customer records
account states

It should carry the minimum information necessary to authorize and coordinate execution.

⸻

54. Minimal Contract Principle

An Action Contract should contain everything required to execute and verify the permitted Action, but nothing that requires Noema to become the system of record for the consumer’s business domain.

This keeps Noema generic.

⸻

55. Contract Example

A conceptual contract:

ActionContract {
    contract_id: "ac_01J..."
    intent_id: "int_01J..."
    
    action: "refund_payment"
    actor: {
        type: "user"
        id: "agent_42"
    }
    resource: {
        type: "payment"
        id: "payment_123"
    }
    parameters: {
        amount: 50000
        currency: "NGN"
        reason: "duplicate_charge"
    }
    constraints: {
        expires_at: "2026-08-25T12:00:00Z"
    }
    authorization: {
        decision: "ALLOW"
        evaluation_id: "trust_01J..."
    }
    execution: {
        consumer: "payment-service"
        idempotency_key: "ac_01J..."
    }
}

The exact schema is intentionally not yet canonical.

⸻

56. Contract Issuance

The conceptual issuance process is:

Resolved Intent
      ↓
Validation
      ↓
Trust Evaluation
      ↓
READY
      ↓
Capability Binding
      ↓
Parameter Binding
      ↓
Constraint Binding
      ↓
Contract Creation
      ↓
Contract Issued

⸻

57. Contract Acceptance

Contract Issued
      ↓
Consumer receives contract
      ↓
Authenticate sender
      ↓
Verify contract integrity
      ↓
Verify contract validity
      ↓
Verify consumer binding
      ↓
Accept / Reject

⸻

58. Consumer Execution

After acceptance:

ACCEPTED
    ↓
Final business-state validation
    ↓
EXECUTING
    ↓
Business mutation
    ↓
Execution result

The consumer remains responsible for the mutation.

⸻

59. Failure Boundaries

Failures should be attributable to the correct layer.

Intent failure

Ambiguous / unresolved

Validation failure

Malformed / invalid Intent

Trust failure

Unauthorized / prohibited / insufficient evidence

Contract failure

Invalid / expired / malformed contract

Execution failure

Consumer or business system could not complete Action

This distinction is essential for observability and debugging.

⸻

60. Action Contract Invariants

Invariant 1

An Action Contract represents an explicit executable scope.

Invariant 2

A contract must reference its originating Intent.

Invariant 3

A contract must not be issued from an unresolved Intent.

Invariant 4

A contract must not be issued unless required Trust conditions are satisfied.

Invariant 5

A contract is not itself execution.

Invariant 6

A consumer must not infer additional Actions from a contract.

Invariant 7

Material contract changes require a new Trust evaluation and contract.

Invariant 8

Contracts should be immutable once issued.

Invariant 9

Contracts should have explicit validity semantics where required.

Invariant 10

Consequential Actions should support idempotency.

Invariant 11

The consumer remains authoritative for final business-state validation.

Invariant 12

Contract success does not mean business success unless the consumer explicitly establishes that outcome.

Invariant 13

Noema does not become the system of record for the consumer’s business state.

Invariant 14

Every executable contract must be auditable back to its Intent and Trust decision.

⸻

61. Canonical Mental Model

The simplest way to understand the Action Contract is:

Intent
"What does the human want?"
        ↓
Trust
"Is Noema allowed to let this happen?"
        ↓
Action Contract
"Exactly what may happen?"
        ↓
Execution Consumer
"How do we make it happen?"
        ↓
Business System
"Did it actually happen?"

⸻

62. Final Definition

An Action Contract is Noema’s typed execution boundary: an immutable, scoped, auditable representation of a specific Action that has passed Intent resolution, validation, and Trust evaluation and may be consumed by an authorized execution system.

The core invariant is:

Noema never hands an execution system a vague instruction and asks it to figure out what the user meant. Noema resolves the Intent, validates it, establishes Trust, and emits an explicit Action Contract whose scope defines exactly what may be executed.