Action Contracts

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/action-contracts.md

⸻

1. Definition

An Action Contract is the explicit, typed, machine-executable contract produced by Noema that defines a specific permitted Action, its resolved execution scope, required inputs, constraints, and verification requirements.

The Action Contract is the boundary between:

Intent and Trust

and:

Execution

It is the mechanism through which Noema converts a validated, resolved Intent and deterministic Trust decision into an explicit execution instruction without requiring the execution consumer to infer semantic meaning.

The Action Contract does not grant authority by itself. Its authority derives from the Trust decision and the enterprise authorization/policy conditions that Trust evaluated.

⸻

2. The Core Boundary

The canonical flow is:

Source of Intent
      ↓
Intent Interpretation
      ↓
Candidate Intent
      ↓
Hard Schema Validation / Admission
      ↓
Admitted Intent
      ↓
Resolution
      ↓
Context / State Reconciliation
      ↓
Deterministic Trust
      ↓
EXECUTE
      ↓
Action Graph / Capability Binding
      ↓
Action Contract
      ↓
Execution Consumer
      ↓
Enterprise System
      ↓
Verification
      ↓
Outcome

The critical boundary is:

                 NOEMA
──────────────────────────────────────────
Intent → Resolution → Trust → Action Contract
──────────────────────────────────────────
                         ↓
                  Execution Consumer
                         ↓
                  Enterprise System

Noema determines which specific Action is permitted to proceed and under what constraints.

The execution consumer determines how that Action is implemented against the enterprise system.

⸻

3. Why Action Contracts Exist

A model-generated instruction is not sufficient for consequential execution.

For example:

"Refund John's payment."

may represent an Intent.

It is not yet an executable instruction.

Before an Action Contract can be issued, Noema must establish, among other things:

Action:
    refund_payment
Actor:
    customer_service_agent
Target Resource:
    payment_123
Parameters:
    amount = 50000
    currency = NGN
Authorization:
    satisfied
Policy:
    satisfied
Preconditions:
    satisfied
Capability:
    payments.refund
Execution Consumer:
    payment-service

Only after the required deterministic conditions are satisfied can Noema produce a contract that an execution consumer can safely consume.

⸻

4. Intent vs Action Contract

An Intent represents:

What the Source of Intent wants accomplished.

An Action Contract represents:

The specific Action that Noema has determined may be executed, together with its explicit execution scope and constraints.

Therefore:

Intent ≠ Action Contract

An Intent is semantic.

An Action Contract is an execution-bound representation of a permitted Action.

An Action Contract must never be treated as a replacement for the Intent from which it originated.

⸻

5. Action Contract Is Not an API Request

An API request says:

Call this interface with these parameters.

An Action Contract says:

Execute this specific Action for this specific resolved Intent, within this explicit scope and under these conditions.

The execution consumer may translate the contract into:

HTTP
RPC
SDK call
Queue message
Workflow invocation
CLI command
Database operation exposed through an approved capability

The implementation mechanism remains an execution-consumer concern.

Noema should not couple Intent semantics to a particular vendor API, protocol, database, or transport.

⸻

6. Action Contract as a Typed Boundary

Action Contracts should be strongly typed.

Conceptually:

ActionContract<A, P, C>

where:

A = Action
P = Parameters
C = Constraints

A contract should make invalid execution states difficult or impossible to represent.

The contract must be schema-validated before issuance and must remain within the semantics of the registered Action Contract definition.

The model cannot create, modify, or expand the semantics of an Action Contract.

⸻

7. Canonical Contract Structure

A conceptual Action Contract contains:

ActionContract {
    contract_id
    intent_id
    intent_version
    action
    capability
    actor
    target
    resources
    parameters
    constraints
    preconditions
    authorization
    policy
    evidence_references
    validity
    consumer
    execution
    verification
}

The exact wire representation remains an implementation concern.

The semantic fields are canonical even when their transport representation differs.

⸻

8. Contract Identity

Every Action Contract requires a unique identity:

contract_id

The identity provides:

traceability
correlation
auditability
execution tracking
idempotency
recovery

The contract must also reference the originating Intent and exact Intent version.

⸻

9. Intent Lineage

An Action Contract must preserve lineage to the exact Intent version that produced it.

Conceptually:

contract.intent_id
contract.intent_version

This allows Noema to answer:

Why does this execution contract exist?

The answer must lead through the exact Intent version, its resolution, the Trust evaluation, and the conditions under which the Action was permitted.

An admitted Intent is immutable once admitted to Trust. If the Intent materially changes, a new Intent version is created with explicit supersedes lineage.

An Action Contract must never silently switch to a new Intent version.

⸻

10. Action

The contract identifies the canonical Action.

Example:

action:
    refund_payment

The Action must reference a known Action definition and supported Capability in Noema’s execution model.

An execution consumer must not receive arbitrary natural-language instructions as the Action identifier.

Prefer:

refund_payment

over:

"Please refund the customer's payment."

The Action identifier is semantic and machine-interpretable.

⸻

11. Actor

The contract identifies the Actor whose authority is relevant to the Action.

Example:

actor:
    customer_service_agent_42

The Actor is not necessarily a human.

It may represent:

human
service
application
agent
workflow
delegated principal
system actor

The Model is not automatically the Actor.

The Model may interpret or propose an Intent.

The Actor is the resolved entity whose authority is relevant to the consequential Action.

⸻

12. Resolved Target and Resource

The contract must identify the exact Resource or Resources against which the Action applies.

Example:

target:
    payment_123

For Actions involving multiple resources:

resources:
    source_account
    destination_account

Consequential execution must not proceed with an unresolved or ambiguous target.

The contract should preserve the resolution identity or reference used to establish the final target binding.

Target binding may include:

resource_type
resource_id
tenant
organization
scope
resource_version
resolution_reference

The execution consumer must not infer a different target.

⸻

13. Parameters

The contract contains the canonical parameters required by the Action.

Example:

parameters {
    amount: 50000
    currency: NGN
    reason: "duplicate_charge"
}

Parameters must conform to the registered Action Contract schema.

Parameters must not introduce semantic authority that was absent from the validated Intent, Trust decision, or Action definition.

Where a parameter depends on current enterprise state, the relevant precondition or reconciliation requirement must be explicit.

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

The execution boundary must be explicit.

If required semantic information remains ambiguous, no executable Action Contract should be issued.

⸻

15. Constraints

The Action Contract may carry explicit execution constraints.

Examples:

maximum_amount
allowed_resource
expiration
required_sequence
execution_window
idempotency_key
tenant_scope
organization_scope
required_confirmation

Constraints define limits on the permitted execution.

They do not give the consumer authority to exceed the scope established by Trust and the Action definition.

⸻

16. Preconditions

An Action Contract should identify material preconditions that must hold for execution.

Examples:

payment_exists
payment_status = eligible_for_refund
actor_authorized
approval_present
resource_version = expected_version

Preconditions that depend on mutable enterprise state should be validated against current authoritative state or through an enterprise-supported atomic conditional operation.

A precondition observed earlier in the execution journey must not automatically be treated as current if the relevant state may have changed.

⸻

17. Authorization

The contract may carry references to the authorization conditions evaluated by Trust.

Conceptually:

authorization {
    decision: ALLOW
    authority_reference
    evaluated_at
    evaluation_id
}

ALLOW here represents an authorization-provider result, not a Noema Trust outcome.

Noema’s canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Technical authorization, policy authorization, and business authorization remain distinct.

Noema does not create enterprise permissions or authority merely by issuing a contract.

⸻

18. Policy

The contract may reference the policies that governed the Trust decision.

Example:

policy {
    policy_set: payments.v3
    policy_version: 3.2
    evaluation_reference: policy_eval_456
}

Policy references provide execution provenance.

The contract must preserve the policy version relevant to the decision rather than relying on an execution consumer to infer which policy version was intended.

⸻

19. Evidence References

An Action Contract may reference the evidence supporting the Trust decision when the consumer requires that information.

Example:

evidence_references [
    identity_verified
    payment_exists
    approval_456
]

Evidence should generally be referenced rather than duplicated unnecessarily inside the contract.

Evidence is not the same as Fact Status.

A reference to evidence does not itself establish that a fact remains current. Where freshness or current state matters, the contract must identify the relevant validation or reconciliation requirement.

⸻

20. Fact Status and Execution

Fact Status is distinct from Evidence, Context, Business State, Outcome, and model confidence.

A relevant fact may have a status such as:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

An Action Contract must not treat model confidence as equivalent to Fact Status.

If a required fact is UNKNOWN, CONFLICTED, or otherwise fails a required precondition, the contract must not authorize execution merely because a model considers one interpretation probable.

⸻

21. Validity

Contracts should have explicit validity semantics where required.

Example:

validity {
    issued_at
    expires_at
}

This prevents a contract generated under old conditions from being executable indefinitely.

Validity is distinct from business-state freshness.

A contract may be within its validity period while the enterprise state required for execution has changed.

⸻

22. Execution Context

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

The execution context must not expand the Action’s semantic scope.

⸻

23. Contract Status

The Action Contract has its own lifecycle.

Conceptually:

ISSUED
ACCEPTED
EXECUTING
COMPLETED
FAILED
EXPIRED
REJECTED
REVOKED
UNKNOWN

These statuses must not be confused with the Trust State Machine.

Trust determines whether a permitted execution path exists.

Contract status tracks the lifecycle of the issued execution contract.

Execution UNKNOWN means Noema cannot establish whether the requested execution occurred. It is not automatically success or failure.

⸻

24. Trust vs Contract

These concepts must remain separate.

Trust:
    Is this specific Action permitted to proceed?
Action Contract:
    Exactly what Action may the consumer execute?
Execution:
    What happened when the consumer attempted it?

Therefore:

EXECUTE
   ↓
Action Contract
   ↓
Consumer

EXECUTE does not mean the Action has succeeded.

⸻

25. Contract Creation Preconditions

An Action Contract must not be issued for consequential execution unless the required conditions have been satisfied.

Conceptually:

Intent admitted
AND
Intent resolved
AND
Actor resolved
AND
Target resolved
AND
Required parameters bound
AND
Required state reconciled
AND
Capability exists
AND
Action Contract schema valid
AND
Trust outcome = EXECUTE

Only then:

Action Contract → ISSUED

A contract must not be issued merely because a model believes an Action is probably appropriate.

⸻

26. No Contract From Ambiguous Intent

Example:

"Delete the account."

If the Actor has:

account_a
account_b
account_c

Noema must not generate:

resource = account_a

based on probability.

Instead:

Trust → CLARIFY

and no executable Action Contract exists.

Clarification that materially changes the Intent produces a new Intent version rather than mutating the existing one.

⸻

27. Contract Immutability

Once issued, an Action Contract should be treated as immutable.

If something materially changes:

parameters
resource
actor
authorization
policy
constraints
validity
capability
Intent version

Noema should not silently mutate the existing contract.

A new contract must be issued following the required Trust evaluation.

⸻

28. Why Immutability Matters

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

with a new Intent/Trust lineage as required.

Historical contracts retain their original meaning.

⸻

29. Contract Versioning

Action Contracts have semantic and implementation versioning concerns.

A contract may reference:

contract_version
action_version
capability_version
intent_version
policy_version
trust_contract_version
graph_version

These are distinct version dimensions.

A material semantic change to an issued executable contract requires a new contract rather than mutation.

Published contract definitions must preserve historical meaning.

⸻

30. Consumer-Side Execution

The execution consumer owns the mechanics.

Example:

Noema
  ↓
Action Contract:
    refund_payment(payment_123)
  ↓
Payment Service
  ↓
Paystack / internal ledger

Noema does not need to know the internal implementation details of the payment service.

However, the consumer must remain within the Action Contract’s scope and the explicit enterprise integration boundary.

⸻

31. Consumer-Side Validation

The consumer may perform final validation.

Example:

Noema:
    EXECUTE
Payment Service:
    payment_123 already refunded

The consumer can reject execution.

This is correct.

The enterprise system remains authoritative for the business state it owns.

Noema’s EXECUTE decision means the execution path is permitted under the evaluated conditions. It does not establish that the enterprise mutation will succeed.

⸻

32. Consumer Must Not Expand the Contract

A consumer must not interpret a contract as permission to perform additional Actions.

If the contract says:

refund_payment(payment_123)

the consumer must not also:

close_customer_account()

unless that Action is explicitly represented in the authorized composition and governed by the applicable contracts and Trust conditions.

The execution consumer must not create authority through interpretation.

⸻

33. Contract Scope

The contract defines the maximum permitted execution scope.

Conceptually:

Contract Scope =
    Action
    +
    Capability
    +
    Actor
    +
    Target
    +
    Parameters
    +
    Constraints
    +
    Consumer

Execution outside this scope is not authorized by the contract.

⸻

34. Least Authority

Action Contracts should follow the principle of least authority.

Instead of:

"Payment service, do whatever is necessary."

Noema should issue:

refund_payment
payment_id = payment_123
amount = ₦50,000

The consumer receives only the authority and execution scope required for the specific Action.

Credentials themselves remain outside model-generated semantics and are managed by the execution/integration boundary.

⸻

35. Contract Composition

Multiple Actions may be composed.

Example:

Intent:
    "Refund the payment and notify the customer."
Contract A:
    refund_payment(payment_123)
Contract B:
    send_notification(customer_123)

The composition semantics must be explicit.

Noema must not assume:

A success ⇒ B must execute

unless the dependency is explicitly defined.

Each consequential Action must remain independently bounded and governed.

⸻

36. Dependencies

Contracts may express dependencies.

Example:

Contract A:
    refund payment
Contract B:
    notify customer
Dependency:
    B requires verified successful completion of A

This creates:

A
↓
verified condition
↓
B

rather than treating the two Actions as unrelated.

A dependency on A.success must not be inferred merely from the ordering of two contracts.

⸻

37. Atomicity

If a composite Intent requires atomic execution, the atomicity requirement must be explicit.

For example:

atomic = true

The execution architecture must support the requested atomicity semantics.

Noema must not imply atomicity merely because multiple Actions originate from one Intent.

Where atomicity is unavailable, the system must represent the limitation explicitly and apply the applicable Trust, execution, compensation, or escalation semantics.

⸻

38. Idempotency

Consequential Action Contracts should support idempotency where applicable.

Example:

idempotency_key:
    ac_01J...

If the consumer receives the same logical contract twice:

C1
C1

it should be able to distinguish:

duplicate delivery

from:

new Action

The idempotency key must be bound to the logical execution identity and Action semantics.

⸻

39. Replay

Contract replay must be explicitly controlled.

A completed contract should not automatically become executable again.

For example:

COMPLETED
+
replay request

must require explicit replay semantics.

Replay is especially important for:

payments
deletions
notifications
external mutations

Historical replay for audit or analysis must not silently recreate a new business occurrence.

⸻

40. Expiration

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

The consumer should reject it unless the execution architecture explicitly permits another governed path.

A new contract may be required after revalidation and Trust evaluation.

⸻

41. Revocation

A previously issued contract may need to be revoked.

Example:

Contract:
    ISSUED
Authorization:
    revoked
Result:
    REVOKED

where the execution architecture supports revocation.

Revocation must not imply that an already completed external mutation has been undone.

⸻

42. Revocation Is Not Guaranteed

If execution has already crossed an irreversible external boundary, revocation may be impossible.

Therefore:

ISSUED
≠
REVERSIBLE

and:

REVOKED
≠
BUSINESS STATE REVERTED

Reversal or compensation is a separate governed Action and must be explicitly authorized.

⸻

43. Execution Acknowledgement

The consumer should acknowledge receipt of a contract.

Conceptually:

ISSUED
   ↓
ACCEPTED

Acceptance means:

The consumer has accepted responsibility for processing the contract.

It does not mean:

The Action succeeded.

The acknowledgement itself should be auditable.

⸻

44. Execution Result

The consumer should return a structured execution result.

Conceptually:

ExecutionResult {
    status
    contract_id
    execution_id
    outcome
    evidence
    error
}

Possible execution statuses include:

SUCCESS
FAILED
REJECTED
UNKNOWN

The precise status vocabulary belongs to the Execution Contract and execution model.

These statuses must not be confused with Noema Trust outcomes.

⸻

45. Unknown Execution Outcome

Distributed systems can produce:

request sent
+
network failure
=
unknown whether Action occurred

The consumer must not falsely report:

FAILED

if it cannot establish whether the mutation happened.

The correct state may be:

UNKNOWN

followed by:

State Reconciliation
        ↓
Authoritative enterprise observation
        ↓
Revalidation

An UNKNOWN execution state must not be blindly retried.

⸻

46. Verification Before Retry

When an execution attempt is unknown, Noema must first determine whether the enterprise operation occurred.

Conceptually:

Execution UNKNOWN
       ↓
Reconcile external operation state
       ↓
Operation occurred?
   ↙             ↘
 YES              UNKNOWN
  ↓                  ↓
Record outcome    Escalate / wait /
                  revalidate

Only where the Action remains necessary and the relevant conditions permit another attempt should a retry be issued.

Idempotency reduces duplicate risk but does not replace reconciliation.

⸻

47. Action Contract vs Business State

An Action Contract is not business state.

Example:

Contract:
    refund payment_123

does not mean:

payment_123.refunded = true

Only the authoritative enterprise system can establish the relevant Business State.

The contract represents permission and execution scope, not established business truth.

⸻

48. Contract Evidence

After execution, the consumer may return evidence such as:

payment_id
transaction_id
provider_reference
resource_version
timestamp
result

This evidence contributes to the execution record and may support determination of the Intent Outcome.

Evidence remains distinct from Fact Status and authoritative Business State.

⸻

49. Outcome

Execution and verification may establish an Outcome for the Intent.

Possible semantic outcomes may include:

SUCCESS
PARTIAL
FAILED
UNKNOWN

The exact Outcome taxonomy is defined separately.

An Outcome is a Noema execution-domain record describing what the execution journey established.

It does not replace the enterprise system of record.

Therefore:

Trust EXECUTE
    ≠
Execution SUCCESS
    ≠
Enterprise Business State

⸻

50. Auditability

An Action Contract should allow an auditor to reconstruct:

Who or what initiated the Intent?
What Intent version produced the contract?
How was the Intent resolved?
What Action was selected?
What Capability supported it?
What Trust evaluation permitted it?
What evidence supported the decision?
What policy versions applied?
What consumer received it?
When was it accepted?
What execution attempts occurred?
What was verified?
What Outcome was established?

This is one of the primary reasons Action Contracts exist.

⸻

51. Contract Provenance

Conceptually:

Source of Intent
    ↓
Intent
    ↓
Intent Version
    ↓
Hard Schema Validation / Admission
    ↓
Resolution
    ↓
State Reconciliation
    ↓
Evidence / Fact Status
    ↓
Trust Decision
    ↓
Capability / Graph Binding
    ↓
Action Contract
    ↓
Execution Attempt
    ↓
Verification
    ↓
Outcome

The causal chain must preserve the exact versions and identities relevant to each consequential decision.

⸻

52. Contract Security

Action Contracts should be integrity-protected.

Depending on architecture, this may involve:

signatures
MACs
capability tokens
short-lived credentials
secure transport
consumer authentication

The precise mechanism is implementation-specific.

The principle is not:

The consumer trusts the contract because it came from Noema.

The principle is:

The consumer can reliably establish the authenticity and integrity of the contract and its intended audience.

The model must not possess credentials that allow it to bypass this boundary.

⸻

53. Contract Audience

A contract should identify its intended consumer where relevant.

Example:

consumer:
    payment-service

A contract intended for one consumer should not automatically be accepted by another.

Consumer binding is part of the execution boundary.

⸻

54. Contract Non-Transferability

Unless explicitly designed otherwise:

Contract C

should not be transferable from:

payment-service

to:

account-service

The Action, Capability, consumer, and execution scope are part of the contract boundary.

A consumer cannot transfer authority merely because another system is technically capable of performing the same operation.

⸻

55. Capability Binding

The contract should map to a known Capability.

Conceptually:

Action
   ↓
Capability
   ↓
Action Contract
   ↓
Execution Consumer

Example:

Action:
    refund_payment
Capability:
    payments.refund
Consumer:
    payment-service

The Capability must exist in the bounded Capability Registry / Enterprise Action Graph.

⸻

56. Action Contract and Capability

An Action is semantic.

A Capability is an available, bounded ability to perform an Action.

An Action Contract binds them:

Intent:
    refund payment
Action:
    refund_payment
Capability:
    payments.refund
Contract:
    execute this specific refund

The Capability Registry and Action Graph constrain what the planner and execution system may select.

Neither the planner nor the model may invent capabilities.

⸻

57. Hard Execution Boundary

No free-form model output should reach execution as an executable instruction.

The required boundary is:

Probabilistic
    ↓
interpretation
candidate generation
proposals
========== HARD BOUNDARY ==========
Deterministic
    ↓
schema validation
resolution
state reconciliation
trust
capability binding
contract validation
execution
verification
recovery

The Action Contract is one of the principal artifacts enforcing this boundary.

The consumer must validate the contract before execution.

⸻

58. Noema Does Not Own Business State

The Action Contract should not attempt to duplicate the entire enterprise business domain.

Noema should not become the source of truth for:

payment balances
inventory counts
customer records
account states
ledger state

It may retain the minimum information and references necessary to authorize, coordinate, execute, verify, and audit the Action.

The enterprise remains authoritative for its designated Business State.

⸻

59. Minimal Contract Principle

An Action Contract should contain everything required to:

identify the permitted Action
bind the actor
bind the target
bind required parameters
enforce constraints
identify the consumer
support execution
support verification
support auditability

but should not require Noema to become the system of record for the consumer’s business domain.

⸻

60. Contract Example

A conceptual contract:

ActionContract {
    contract_id: "ac_01J..."
    intent_id: "int_01J..."
    intent_version: 3
    action: "refund_payment"
    capability: "payments.refund"
    actor: {
        type: "user"
        id: "agent_42"
    }
    target: {
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

The semantic requirements are canonical even where the wire representation remains implementation-specific.

⸻

61. Contract Issuance

The conceptual issuance process is:

Resolved Intent
      ↓
Hard Schema Validation
      ↓
State Reconciliation
      ↓
Trust Evaluation
      ↓
EXECUTE
      ↓
Capability Binding
      ↓
Action Binding
      ↓
Parameter Binding
      ↓
Constraint Binding
      ↓
Contract Schema Validation
      ↓
Contract Creation
      ↓
Contract Issued

The contract is not issued merely because an Action appears plausible.

⸻

62. Contract Acceptance

Contract Issued
      ↓
Consumer receives contract
      ↓
Authenticate sender
      ↓
Verify contract integrity
      ↓
Validate contract schema
      ↓
Verify contract validity
      ↓
Verify consumer binding
      ↓
Validate required execution conditions
      ↓
Accept / Reject

Consumer acceptance is not equivalent to business success.

⸻

63. Consumer Execution

After acceptance:

ACCEPTED
    ↓
Final business-state validation
    ↓
EXECUTING
    ↓
Enterprise mutation
    ↓
Execution result
    ↓
Verification

The consumer remains responsible for performing the mutation through the approved enterprise capability.

The consumer must not bypass the enterprise system’s own authoritative business-state and concurrency controls.

⸻

64. Failure Boundaries

Failures should be attributable to the correct layer.

Intent failure

ambiguous
unresolved
cancelled
invalid semantic request

Validation failure

malformed
schema-invalid
inadmissible Intent

Trust failure

unauthorized
prohibited
insufficient evidence
unresolved required condition

Contract failure

invalid
expired
malformed
integrity failure
wrong consumer
invalid scope

Execution failure

consumer failure
enterprise rejection
business-state precondition failure
transport failure

Verification / Reconciliation uncertainty

execution may have occurred
current state cannot yet be established

This distinction is essential for observability, recovery, and debugging.

⸻

65. State Reconciliation

State Reconciliation is a first-class Noema capability.

An Action Contract may depend on current enterprise state that cannot be established from a single observation.

The relevant flow is:

Enterprise Systems
       ↓
Observations
       ↓
Hard Schema Validation / Admission
       ↓
State Reconciliation
       ↓
Reconciled Facts
       ↓
Fact Status
       ↓
Trust / Preconditions
       ↓
Action Contract

The Action Contract must not convert stale, conflicting, or unknown observations into false certainty.

⸻

66. Read-Only Actions

An Action Contract may represent a read-only Action.

Read-only does not necessarily mean low consequence.

For example:

retrieve_customer_financial_history
inspect_privileged_account
reconcile_transaction_state

may expose protected information or materially affect a consequential decision.

Therefore read-only Actions may still require Trust, authorization, scope validation, and auditability.

⸻

67. Planner Boundary

The Planner may select or compose Actions only within the bounded execution model established by:

Enterprise Action Graph
Capability Registry
Action Contracts
Trust constraints
Policy constraints

The Planner cannot:

invent capabilities
invent authority
modify Action Contracts
expand execution scope
bypass Trust

The Action Contract is the concrete boundary between bounded planning and execution.

⸻

68. Operational Memory

Action Contract lifecycle and execution history may contribute to Noema’s Operational Memory.

Operational Memory may retain:

contract history
execution attempts
verification results
recovery paths
interventions
failure patterns

Operational Memory is not:

enterprise Business State
enterprise authorization
generic model memory

Historical execution records must not become authoritative merely because they are stored by Noema.

⸻

69. Replay and Historical Semantics

Historical Action Contracts must retain their original meaning.

Replaying a contract for:

audit
simulation
testing
reconstruction

must not automatically create a new enterprise business occurrence.

A new execution requires explicit replay semantics and appropriate revalidation.

Historical Trust and contract records must remain historically accurate even when current policies, systems, capabilities, or business state have changed.

⸻

70. Embedded Execution Model

Noema supports two execution modes.

Mode 1: Full-Stack Noema

Source of Intent
      ↓
Noema
      ↓
Intent → Trust → Action Contract
      ↓
Enterprise Systems

Noema can own the full semantic execution journey.

Mode 2: Independent Trust / Execution Boundary

Human / Agent / Application
          ↓
Enterprise Orchestrator
          ↓
Noema
          ↓
Trust / Action Contract
          ↓
Enterprise Execution

In Mode 2, an external agent or orchestrator may own the interaction and planning experience.

Noema remains an independent trust and execution boundary and does not need to own the conversational interface.

⸻

71. Causal Audit Chain

A consequential Action Contract should participate in a causal audit chain:

Source of Intent
      ↓
Intent / Intent Version
      ↓
Authority / Identity
      ↓
Observation
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Fact Status / Evidence
      ↓
Resolution
      ↓
Trust Decision
      ↓
Capability / Graph Binding
      ↓
Action Contract
      ↓
Execution Attempt
      ↓
Verification
      ↓
Outcome

The audit record should preserve references to the relevant:

Intent version
Action version
Capability version
Trust contract version
Policy version
Graph/capability version
Integration mapping version
Execution contract version

No private model chain-of-thought is required to establish causal auditability.

⸻

72. Action Contract Invariants

Invariant 1

An Action Contract represents an explicit executable scope.

Invariant 2

A contract must reference its originating Intent.

Invariant 3

A consequential contract must reference the exact Intent version that produced it.

Invariant 4

A contract must not be issued from an unresolved Intent.

Invariant 5

A contract must not be issued unless the required Trust outcome is EXECUTE.

Invariant 6

A contract must not be issued for an Action outside the registered Capability / Action Graph boundary.

Invariant 7

Actor and consequential target resources must be explicitly resolved.

Invariant 8

Required parameters must be schema-valid and explicitly bound.

Invariant 9

A contract is not execution.

Invariant 10

A consumer must not infer additional Actions from a contract.

Invariant 11

Material contract changes require a new Trust evaluation and contract.

Invariant 12

Issued contracts should be immutable.

Invariant 13

Contracts should have explicit validity semantics where required.

Invariant 14

Consequential Actions should support idempotency where applicable.

Invariant 15

The consumer remains responsible for final business-state validation.

Invariant 16

EXECUTE does not establish business success.

Invariant 17

An execution UNKNOWN state must not be converted into success or failure without verification or reconciliation.

Invariant 18

An UNKNOWN execution must not be blindly retried.

Invariant 19

Contract replay must be explicitly governed.

Invariant 20

Contract scope must not be expanded by the execution consumer.

Invariant 21

Noema must not become the system of record for enterprise Business State.

Invariant 22

Every consequential contract must be auditable back to its Intent and Trust Decision.

Invariant 23

Model confidence must never substitute for required evidence, Fact Status, authorization, or Trust conditions.

Invariant 24

No free-form model output may become an executable Action without passing the deterministic execution boundary.

Invariant 25

Credentials and direct enterprise access must remain outside the model execution boundary.

Invariant 26

State-dependent execution must use current authoritative state or an enterprise-supported mechanism capable of enforcing the required condition.

Invariant 27

Historical contracts must retain their historical meaning.

Invariant 28

Operational Memory must not become enterprise Business State authority.

Invariant 29

Read-only Actions may still require Trust and authorization.

Invariant 30

A consumer must not transfer contract authority to another consumer unless transfer is explicitly supported and governed.

⸻

73. Canonical Mental Model

The simplest way to understand the Action Contract is:

Intent
"What does the Source of Intent want?"
        ↓
Resolution
"What exact Actor, Action, Target, and parameters does that mean?"
        ↓
Trust
"May this specific Action proceed?"
        ↓
Action Contract
"Exactly what may execute, under what constraints?"
        ↓
Execution Consumer
"How do we perform it?"
        ↓
Enterprise System
"What actually happened?"
        ↓
Verification / Reconciliation
"Can we establish what happened?"
        ↓
Outcome
"What did the execution journey establish?"

⸻

74. Final Definition

An Action Contract is Noema’s typed execution boundary: an immutable, scoped, auditable representation of a specific Action that has passed schema validation, Intent resolution, required state reconciliation, and deterministic Trust evaluation and may be consumed by an authorized execution system.

It binds the exact Intent version, resolved Actor, target, Action, Capability, parameters, constraints, consumer, and relevant execution provenance without making Noema the source of truth for the enterprise business state.

The core invariant is:

Noema never hands an execution system a vague instruction and asks it to figure out what the Source of Intent meant. Noema validates and resolves the Intent, evaluates deterministic Trust, binds the permitted Action to an explicit Capability, and emits a typed Action Contract whose scope defines exactly what may be executed.