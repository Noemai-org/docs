Action Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/action-contract.md

⸻

1. Definition

An Action Contract is the explicit, machine-interpretable definition of what Noema is permitted to execute against an enterprise capability.

An Action Contract answers:

“What exactly is this Action, what does it require, what may it do, and how can its result be verified?”

An Action Contract defines the boundary between Noema’s execution system and an enterprise capability.

Intent
   ↓
Trust
   ↓
Action Contract
   ↓
Execution
   ↓
Outcome

The Action Contract is therefore not merely an API description.

It defines the semantic and operational contract required for safe execution.

⸻

2. Purpose

The purpose of an Action Contract is to make enterprise Actions explicit, bounded, verifiable, and executable.

An Action Contract establishes:

identity
purpose
inputs
target
preconditions
permissions
constraints
execution semantics
idempotency
timeouts
retry behavior
postconditions
outcomes
failure semantics
data boundaries
audit requirements

This allows Noema to execute enterprise capabilities without relying on undocumented assumptions.

⸻

3. Core Principle

An Action must never be executed merely because the model generated a plausible tool call.

The model may propose:

Action:
get_account_balance

But execution requires a valid Action Contract.

Model Interpretation
        ↓
Action Candidate
        ↓
Action Contract
        ↓
Trust
        ↓
Execution

The Contract establishes what the Action means and the boundaries within which it may execute.

⸻

4. Action Identity

Every Action Contract must have a stable identity.

Conceptually:

Action:
get_account_balance
Action ID:
account.balance.read
Version:
1

The identity should remain stable across executions.

Versioning allows the semantics or execution requirements of an Action to evolve without making historical executions uninterpretable.

⸻

5. Action Name

An Action should have a human-readable name.

Example:

get_account_balance

The name should describe the capability rather than the implementation mechanism.

Prefer:

get_account_balance

over:

GET /v2/accounts/{id}/balance

The HTTP endpoint is an implementation detail.

The Action represents the enterprise capability.

⸻

6. Action Purpose

The Contract must define what the Action accomplishes.

Example:

Purpose:
Retrieve the current available balance for an authorized account.

Purpose prevents an implementation from silently acquiring semantics that were never part of the Action definition.

⸻

7. Action Scope

An Action Contract must define its scope.

Example:

Scope:
Account Balance
Operation:
Read
Side Effects:
None

This allows Noema to distinguish:

read
write
delete
submit
approve

and other classes of enterprise operation.

⸻

8. Read vs Write Semantics

The Contract must explicitly identify whether an Action changes enterprise state.

Example:

get_account_balance
→ READ
create_complaint
→ WRITE

This distinction affects Trust, idempotency, retries, confirmation, auditability, and recovery.

Noema must never infer that an Action is read-only merely because its name sounds harmless.

⸻

9. Target

The Action Contract must define the Resource against which the Action operates.

Example:

Action:
get_account_balance
Target:
Account

The target may be:

Account
Transaction
Statement
Customer
Complaint

or another enterprise Resource.

⸻

10. Target Resolution

The Contract should specify how the Target is identified.

Example:

Target:
Account
Required identifier:
account_id

Natural-language references such as:

"my account"
"my savings"
"that transaction"

must be resolved before execution.

The Contract defines the final target shape expected by the enterprise capability.

⸻

11. Inputs

The Contract defines the inputs required to execute the Action.

Example:

get_account_balance {
    account_id
}

Inputs should be explicit and typed.

Noema should not pass arbitrary model-generated fields into an enterprise capability.

⸻

12. Input Semantics

Each input must have defined semantics.

Example:

account_id:
Stable enterprise identifier for the target Account.

The Contract should establish:

type
requiredness
format
authority
validation
allowed values

where applicable.

⸻

13. Input Validation

Inputs must be validated before execution.

Example:

account_id
→ required
→ string
→ valid enterprise identifier

Invalid inputs should prevent execution.

Invalid Input
      ↓
Trust / Contract Validation
      ↓
REJECT

The enterprise system should not be used as the first line of validation for conditions that Noema can deterministically establish.

⸻

14. Preconditions

The Action Contract must define conditions that must hold before execution.

Example:

Preconditions:
- Principal is authenticated
- Principal is authorized
- Account exists
- Account belongs to the permitted scope

The Contract defines what is required.

Trust determines whether those requirements are currently satisfied.

Action Contract
      ↓
Required Preconditions
      ↓
Trust

⸻

15. Preconditions vs Trust

These concepts must remain distinct.

Precondition:
Account must exist.
Trust:
Account existence has been established.

The Contract declares the requirement.

Trust evaluates the current evidence against that requirement.

⸻

16. Permissions

The Contract should define the authorization capability required by the Action.

Example:

Required Permission:
account.read

Noema must verify that the current Principal has the required permission within the applicable enterprise boundary.

⸻

17. Organizational Scope

The Contract may define organizational restrictions.

Example:

Scope:
Customer's own accounts

or:

Scope:
Tenant-local accounts

The Contract must not assume that possession of an identifier grants authority over the corresponding Resource.

⸻

18. Data Requirements

The Contract should specify the minimum data required to execute the Action.

Example:

get_account_balance
Required:
account_id
principal_id

Noema should not retrieve unrelated enterprise information merely because it is available.

This supports least privilege and Data Boundaries.

⸻

19. Data Boundary

The Action Contract may explicitly constrain the fields an Action may receive or return.

Example:

Input:
account_id
Output:
balance
currency
observed_at

The Action should not automatically expose:

customer_address
full_transaction_history
internal_risk_score

when they are not required.

⸻

20. Output

The Contract defines the expected output.

Example:

get_account_balance
Output:
{
    balance
    currency
}

Output schemas should be explicit and versioned.

This allows Noema to distinguish valid results from malformed or unexpected responses.

⸻

21. Output Authority

The Contract should identify the enterprise system authoritative for the returned data.

Example:

Output:
account.balance
Authority:
Account Ledger

This prevents Noema from treating arbitrary derived or cached responses as equivalent to canonical enterprise state.

⸻

22. Postconditions

The Contract defines what should be true after execution.

For a read Action:

Postcondition:
A current account balance has been retrieved from the authoritative source.

For a state-changing Action:

Postcondition:
A complaint exists with a valid enterprise case identifier.

Postconditions provide the basis for Outcome verification.

⸻

23. Postconditions vs Outcomes

The Contract declares the expected postcondition.

Execution establishes what happened.

Outcome represents the resulting state.

Contract
   ↓
Expected Postcondition
   ↓
Execution
   ↓
Evidence
   ↓
Outcome

A postcondition is therefore not proof that the Action succeeded.

⸻

24. Execution Semantics

The Contract must define how the Action is executed.

This may include:

protocol
endpoint
method
authentication mechanism
request format
response format
timeout
transport requirements

These are execution details beneath the semantic Action definition.

Action
   ↓
Contract
   ↓
Integration
   ↓
Enterprise Capability

⸻

25. Integration Binding

An Action Contract may bind an Action to one or more enterprise integrations.

Example:

Action:
get_account_balance
Integration:
Ledger API
Capability:
GET /accounts/{account_id}/balance

The endpoint is not the Action itself.

The Action is the stable semantic capability.

The Integration provides its implementation.

⸻

26. Contract and Integration Model

The relationship is:

Action Contract
      ↓
Integration Binding
      ↓
Enterprise Capability
      ↓
Execution

This allows the same semantic Action to potentially be implemented through:

REST API
GraphQL API
gRPC
SDK
database procedure
enterprise workflow

without changing the meaning of the Action.

⸻

27. Authentication

The Contract should specify the authentication requirements for the underlying enterprise capability.

Examples:

OAuth token
service credential
mTLS
delegated identity
enterprise session

Authentication establishes how Noema communicates with the enterprise system.

It does not by itself establish that the Customer is authorized to perform the Action.

⸻

28. Authorization

Authorization must be evaluated separately from authentication.

Authentication:
Who is making the request?
Authorization:
Is that Principal allowed to perform this Action against this Resource?

The Action Contract should define the authorization capability required.

⸻

29. Idempotency

State-changing Actions should define idempotency semantics.

Example:

create_complaint
Idempotency:
Supported
Key:
customer_id + transaction_id + complaint_type

This becomes important when execution produces an Unknown result.

Noema should be able to determine whether retrying could create duplicate enterprise state.

⸻

30. Retry Semantics

The Contract should define whether and under what conditions the Action may be retried.

Example:

Retryable:
network timeout
temporary service unavailable
Not Retryable:
authorization failure
invalid input
policy rejection

Retry behavior must be Action-specific.

Noema must not apply generic retries blindly to every enterprise capability.

⸻

31. Timeout Semantics

The Contract should define an execution timeout appropriate to the capability.

Example:

timeout:
5 seconds

A timeout does not necessarily mean the Action failed.

For state-changing operations:

timeout
   ↓
execution state UNKNOWN

may be the correct result until enterprise state is reconciled.

⸻

32. Failure Semantics

The Contract should define expected failure categories.

Examples:

INVALID_INPUT
UNAUTHORIZED
FORBIDDEN
NOT_FOUND
RATE_LIMITED
TEMPORARY_UNAVAILABLE
TIMEOUT
CONFLICT
UNKNOWN

Failure classification should be machine-readable.

This allows Noema to determine appropriate recovery behavior.

⸻

33. Failure vs Rejection

A Contract rejection occurs before execution.

Example:

Permission missing
      ↓
Trust
      ↓
REJECT

An enterprise failure occurs after execution has been authorized.

Trust
   ↓
EXECUTE
   ↓
Enterprise API
   ↓
FORBIDDEN
   ↓
Execution FAILED

The two must remain distinguishable.

⸻

34. Unknown Execution

The Contract must account for situations where execution status cannot immediately be established.

Example:

Request sent
      ↓
Timeout
      ↓
No definitive response

The result may be:

UNKNOWN

rather than:

FAILED

The Contract should define how such states are reconciled.

⸻

35. Reconciliation

An Action Contract may define the capability used to determine whether an uncertain execution occurred.

Example:

create_complaint
      ↓
UNKNOWN
      ↓
lookup_complaint_by_idempotency_key
      ↓
existing Case found
      ↓
SUCCESS

Reconciliation is especially important for state-changing Actions.

⸻

36. Side Effects

The Contract must explicitly identify expected side effects.

Example:

get_account_balance
Side Effects:
none
create_complaint
Side Effects:
creates enterprise complaint record

Noema must not assume an Action is side-effect-free unless the Contract establishes it.

⸻

37. Action Atomicity

Where applicable, the Contract should define whether the Action is atomic.

Example:

create_complaint

may be atomic within the complaint system.

A Compound Intent containing multiple Actions is not automatically atomic as a whole.

Action A
   ↓
Action B
   ↓
Action C

Each Action retains its own Contract and execution semantics.

⸻

38. Transaction Boundaries

The Contract should define the enterprise transaction boundary where relevant.

Noema must not assume that multiple Actions across independent enterprise systems share a transaction.

Example:

Payment System
      +
Account System

may require separate executions and recovery semantics.

⸻

39. Compensation

Where an Action participates in a workflow requiring compensation, the Contract may define a compensating capability.

Example:

Action:
create_record
Compensation:
cancel_record

Compensation is not equivalent to rollback.

The enterprise system may expose a separate Action with separate authorization and semantics.

⸻

40. Human Intervention

An Action Contract may specify conditions requiring human intervention.

Example:

Human Review:
required when enterprise identity cannot be deterministically resolved.

Human intervention should be represented explicitly rather than hidden inside model behavior.

⸻

41. Confirmation Requirements

The Contract may require explicit Customer confirmation.

Example:

Confirmation:
required

Trust may establish that all other conditions are satisfied while the Action remains blocked pending confirmation.

Trust
   ↓
WAITING_FOR_CONFIRMATION
   ↓
Customer Confirmation
   ↓
EXECUTE

⸻

42. Risk Classification

Actions should have an explicit risk classification.

Example:

get_account_balance
Risk:
LOW
create_complaint
Risk:
MODERATE

Risk classification may influence:

Trust requirements
freshness
confirmation
audit requirements
human review
retry behavior

The classification should be defined by Policy rather than model judgment.

⸻

43. Freshness Requirements

The Contract may define how fresh required enterprise data must be.

Example:

Balance:
must be retrieved from authoritative source during execution.

This prevents stale Context from being used where current state is required.

⸻

44. Version Requirements

An Action may require a specific enterprise Resource version.

Example:

account_version = 42

This can support optimistic concurrency and prevent execution against unexpectedly changed state.

⸻

45. Concurrency

The Contract may define concurrency expectations.

Examples:

single-flight
optimistic concurrency
exclusive execution
safe concurrent execution

This becomes important when multiple Noema executions may target the same enterprise Resource.

⸻

46. Ordering

Some Actions require a specific execution order.

Example:

resolve_transaction
      ↓
create_complaint

The complaint Action cannot execute until the transaction Target has been resolved.

Contract dependencies should be explicit.

⸻

47. Action Dependencies

Conceptually:

Action B
requires:
Outcome A

Example:

resolve_account
      ↓
get_account_balance

The dependency should be represented explicitly in the execution plan.

Noema must not rely on accidental execution ordering.

⸻

48. Compound Intent

A Compound Intent produces multiple Action Contracts.

Example:

Intent:
"Show my balance and find my transactions."
Actions:
    get_account_balance
    search_transactions

Each Action must retain its own:

Contract
Trust requirements
Execution
Outcome
Failure semantics

The parent workflow coordinates them without collapsing their boundaries.

⸻

49. Contract and Planning

Planning selects Actions that can satisfy the Intent.

Intent
   ↓
Plan
   ↓
Candidate Actions
   ↓
Action Contracts
   ↓
Trust
   ↓
Execution

The planner must only select Actions whose Contracts are compatible with the requested objective.

⸻

50. Contract and Trust

The Contract defines the rules.

Trust evaluates whether the current execution satisfies them.

Action Contract
      ↓
Requirements
      ↓
Current Context + Evidence
      ↓
Trust
      ↓
Decision

Trust cannot weaken Contract requirements.

⸻

51. Contract and Policy

Policy may impose constraints beyond the Action’s technical Contract.

Example:

Action Contract:
account.read is executable by an authorized Principal.
Policy:
Customer may only access accounts belonging to the authenticated Customer.

Therefore:

Contract + Policy
       ↓
Trust Requirements

The Action is executable only when both are satisfied.

⸻

52. Contract and Canonical Data

The Contract may specify which enterprise source provides authoritative inputs or outputs.

Example:

get_account_balance
Canonical Source:
Ledger

Noema should use the appropriate authoritative source when the Contract requires canonical state.

⸻

53. Contract and Context

Context supplies the runtime values required by the Contract.

Example:

Action Contract:
account_id required
Context:
account_id = ACC-123

If Context does not contain a sufficiently grounded account_id:

Trust:
CLARIFY

or:

Trust:
ESCALATE

depending on the resolution path.

⸻

54. Contract and Evidence

Evidence establishes that Contract requirements are satisfied.

Example:

Contract:
Principal must own Account.
Evidence:
Enterprise Identity System confirms:
Customer 123 → Account 456

Trust can then evaluate the requirement deterministically.

⸻

55. Contract and Outcome

The Contract defines expected outputs and Postconditions.

Execution produces evidence.

Outcome records what was established.

Contract
   ↓
Expected Result
   ↓
Execution
   ↓
Evidence
   ↓
Outcome

⸻

56. Contract and Auditability

Consequential Actions should preserve the Contract version used for execution.

An audit record should be able to establish:

Action ID
Action version
Intent
Principal
Target
inputs
Policy
Trust decision
execution
Outcome
evidence

This allows historical execution to be reconstructed even after the Contract evolves.

⸻

57. Contract Versioning

Contracts must be versioned when their semantics or execution requirements change.

Example:

account.balance.read:v1
account.balance.read:v2

A new version may change:

input schema
output schema
authorization requirements
freshness requirements
postconditions
failure semantics
integration binding

Historical executions must retain the version actually used.

⸻

58. Backward Compatibility

Changing a Contract is not merely an implementation change if the semantic behavior changes.

For example:

v1:
returns available balance
v2:
returns ledger balance

This is a semantic change and should require explicit versioning.

⸻

59. Contract Integrity

Noema must ensure that the Contract used for execution is the intended Contract version.

The model must not be allowed to modify Contract semantics at runtime.

Model
   ↓
Candidate Action
   ↓
Registered Contract
   ↓
Validation
   ↓
Execution

The authoritative Contract comes from trusted configuration or registry.

⸻

60. Contract Registry

Noema may maintain an Action Contract Registry.

Conceptually:

Action Registry
      │
      ├── account.balance.read:v1
      ├── account.statement.read:v1
      ├── transaction.search:v1
      ├── spending.summary.read:v1
      └── complaint.create:v1

The Registry provides the canonical definitions of executable Actions available to Noema.

⸻

61. Contract Discovery

The model should not invent Actions.

It should select from Actions exposed through the trusted Action Registry.

Intent
   ↓
Candidate Action
   ↓
Action Registry
   ↓
Known Contract

If no suitable Contract exists:

UNSUPPORTED_ACTION

The system should not manufacture an enterprise capability.

⸻

62. Contract Validation

Before execution, Noema should validate:

Action exists
Contract version exists
inputs valid
Target resolved
permissions satisfied
preconditions satisfied
Policy satisfied
integration available
execution constraints satisfied

Only then may execution proceed.

⸻

63. Contract Lifecycle

An Action Contract may move through:

DRAFT
   ↓
VALIDATED
   ↓
ACTIVE
   ↓
DEPRECATED
   ↓
RETIRED

Only appropriate lifecycle states should be executable.

Historical Contracts should remain available for reconstruction where required.

⸻

64. Contract Deprecation

A Contract should not be silently removed if historical executions depend on it.

Example:

v1 → DEPRECATED
v2 → ACTIVE

New executions use v2.

Historical executions remain associated with v1.

⸻

65. Contract and Environment

Contracts may be environment-specific.

Example:

Production:
ledger-prod
Staging:
ledger-staging

A production Action must never accidentally bind to a staging integration.

Environment must therefore be part of the execution boundary.

⸻

66. Contract and Tenancy

Where integrations are tenant-specific, the Contract must preserve tenant scope.

Example:

Tenant A
   ↓
Ledger A
Tenant B
   ↓
Ledger B

An Action Contract must not allow an enterprise capability from one tenant to be silently used for another.

⸻

67. Contract and Observability

Execution should emit structured telemetry associated with the Contract.

Useful fields include:

action_id
action_version
execution_id
integration_id
started_at
completed_at
status
outcome
failure_code

Observability must not expose sensitive input or output data unnecessarily.

⸻

68. Contract and Security

Action Contracts are security boundaries.

They define:

what can be executed
against which Resources
by which Principals
using which capabilities
with which inputs
and under which conditions

A Contract should therefore be treated as executable security-relevant configuration.

⸻

69. Contract and Least Privilege

An Action should request only the permissions and data required for its purpose.

Example:

get_account_balance
Permission:
account.read
Required Data:
account_id

It should not require:

account.admin
customer.write
transaction.delete

unless those capabilities are genuinely necessary.

⸻

70. Contract and Customer Account Inquiry

The reference workflow may expose Actions such as:

account.balance.read
account.statement.read
transaction.search
spending.summary.read
complaint.create

Each Action must have its own Contract.

Customer Account Inquiry
          │
          ├── Balance Contract
          ├── Statement Contract
          ├── Transaction Search Contract
          ├── Spending Summary Contract
          └── Complaint Contract

The workflow itself does not redefine the Action semantics.

⸻

71. Example: Balance Action Contract

Conceptually:

ActionContract {
    id: "account.balance.read"
    version: "1"
    operation: READ
    target: Account
    inputs: {
        account_id
    }
    required_permission:
        account.read
    preconditions: [
        principal_authenticated,
        account_exists,
        principal_authorized
    ]
    output: {
        balance,
        currency
    }
    postconditions: [
        balance_retrieved_from_authoritative_source
    ]
    side_effects:
        none
}

⸻

72. Example: Complaint Action Contract

Conceptually:

ActionContract {
    id: "complaint.create"
    version: "1"
    operation: WRITE
    target: Complaint
    inputs: {
        transaction_id,
        complaint_type,
        description
    }
    required_permission:
        complaint.create
    preconditions: [
        principal_authenticated,
        transaction_resolved,
        required_fields_present
    ]
    output: {
        case_id,
        status
    }
    postconditions: [
        complaint_exists
    ]
    idempotency:
        required
    side_effects:
        creates_complaint
}

⸻

73. Contract Model

Conceptually:

ActionContract {
    action_id
    version
    purpose
    operation
    target
    inputs
    outputs
    permissions
    preconditions
    postconditions
    data_boundaries
    organizational_scope
    integration
    authentication
    authorization
    timeout
    retry_policy
    idempotency
    side_effects
    atomicity
    dependencies
    confirmation
    risk
    failure_semantics
    reconciliation
    audit_requirements
}

This is a semantic model rather than a requirement for a literal database table.

⸻

74. Action Contract Relationships

Action Contract
   │
   ├── defines → Action
   ├── targets → Resource
   ├── requires → Preconditions
   ├── requires → Permissions
   ├── constrained_by → Policy
   ├── binds_to → Integration
   ├── consumes → Context
   ├── grounded_by → Evidence
   ├── gates → Execution
   ├── verifies → Postconditions
   ├── produces → Outcome
   ├── defines → Failure Semantics
   └── requires → Auditability

⸻

75. Action Contract Invariants

Invariant 1

Every executable Action must have a valid Action Contract.

Invariant 2

An Action Contract must have a stable identity and version.

Invariant 3

The semantic Action must remain distinct from its underlying API or integration implementation.

Invariant 4

The model must not invent or modify Action Contract semantics.

Invariant 5

Action inputs must be explicitly defined and validated.

Invariant 6

Action Targets must be resolved before execution.

Invariant 7

Required permissions must be explicitly defined.

Invariant 8

Preconditions must be explicitly defined where required.

Invariant 9

Trust evaluates whether Contract requirements are satisfied; it does not redefine those requirements.

Invariant 10

Read and write semantics must be explicit.

Invariant 11

Expected side effects must be explicitly defined.

Invariant 12

State-changing Actions must define appropriate idempotency semantics.

Invariant 13

Retry behavior must be Action-specific.

Invariant 14

Timeout does not automatically imply execution failure when enterprise state remains uncertain.

Invariant 15

Unknown execution states must have an explicit reconciliation path where required.

Invariant 16

Outputs must have defined schemas.

Invariant 17

Postconditions must be explicit where verification is required.

Invariant 18

Outcome must be derived from execution evidence rather than assumed from the Contract.

Invariant 19

Contract requirements must respect enterprise Data Boundaries.

Invariant 20

Contract authorization must remain distinct from authentication.

Invariant 21

Contract scope must respect tenant, organizational, legal, and environment boundaries.

Invariant 22

Compound Intents must preserve individual Action Contract boundaries.

Invariant 23

A Contract for one Action must not implicitly authorize another Action.

Invariant 24

Contract versions used for execution must be preserved for auditability.

Invariant 25

Deprecated Contracts must not silently change the semantics of historical executions.

Invariant 26

Production Actions must not silently bind to non-production enterprise capabilities.

Invariant 27

Contract configuration is security-relevant and must be governed accordingly.

Invariant 28

An Action must request only the permissions and data necessary for its defined purpose.

Invariant 29

Noema must not execute an enterprise capability whose Contract cannot be established.

Invariant 30

An Action Contract defines the executable boundary; it does not transfer ownership of enterprise Business State to Noema.

⸻

76. Final Definition

An Action Contract is the authoritative definition of an executable enterprise capability within Noema.

It establishes:

WHAT
the Action means
WHO
may execute it
WHAT
Resource it targets
WHAT
inputs it requires
WHICH
Preconditions must hold
WHICH
Policies and permissions apply
HOW
it is executed
WHAT
side effects may occur
HOW
failure and uncertainty are handled
WHAT
Postconditions must be verified
WHAT
Outcome can be produced

The fundamental relationship is:

INTENT
   ↓
ACTION
   ↓
ACTION CONTRACT
   │
   ├── INPUTS
   ├── TARGET
   ├── PERMISSIONS
   ├── PRECONDITIONS
   ├── POLICY
   ├── DATA BOUNDARIES
   ├── EXECUTION SEMANTICS
   ├── IDEMPOTENCY
   ├── RETRIES
   ├── FAILURE SEMANTICS
   └── POSTCONDITIONS
            │
            ▼
          TRUST
            │
            ▼
        EXECUTION
            │
            ▼
          EVIDENCE
            │
            ▼
          OUTCOME

And the architectural rule is:

Noema may only execute enterprise capabilities through explicit, trusted Action Contracts. The model may select an Action, but the Contract defines what that Action means, what it requires, what it is allowed to do, and how its result must be established.