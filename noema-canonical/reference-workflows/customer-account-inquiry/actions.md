Actions

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/actions.md

⸻

1. Definition

An Action is a typed, executable operation that Noema may invoke against an enterprise capability to satisfy a resolved Intent.

Within the Customer Account Inquiry workflow, Actions are deliberately limited to read and support operations.

The reference Actions are:

get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

An Action is not:

Intent
Plan
Tool
API Request
Business State
Outcome

An Intent expresses what the Customer wants.

An Action expresses the specific operation that can be executed.

⸻

2. Purpose

The purpose of the Action model is to establish the executable boundary between:

Customer Intent
       ↓
Resolved Intent
       ↓
Action
       ↓
Enterprise Capability
       ↓
Outcome

Actions provide the controlled interface through which Noema interacts with enterprise systems.

They prevent natural-language intent from becoming an unrestricted instruction to enterprise infrastructure.

⸻

3. Reference Action Set

The Customer Account Inquiry workflow defines five initial Actions:

Action	Purpose	Primary Domain
get_account_balance	Retrieve the current account balance	Account / Ledger
retrieve_statement	Retrieve an account statement	Statement
search_transactions	Search account transactions	Transaction
get_spending_summary	Retrieve or calculate an authorized spending summary	Transaction / Analytics
create_complaint	Create a customer complaint or support case	Support

These Actions are sufficient to demonstrate the initial read/support wedge without introducing financial write operations.

⸻

4. Action: get_account_balance

get_account_balance retrieves the current balance for an authorized account.

Conceptually:

get_account_balance(
    account_id
)

Expected result:

{
    account_id
    balance
    currency
    observed_at
}

The authoritative source should be the enterprise System of Record for account balance.

Noema does not calculate or invent the balance.

⸻

5. Action: retrieve_statement

retrieve_statement retrieves a statement associated with an authorized account and statement period.

Conceptually:

retrieve_statement(
    account_id,
    period
)

Expected result may include:

{
    statement_id
    account_id
    period
    document
    status
}

The Statement System remains authoritative for the statement resource.

⸻

6. Action: search_transactions

search_transactions retrieves transactions matching an authorized query.

Conceptually:

search_transactions(
    account_id,
    filters
)

Possible filters include:

date_range
amount_range
merchant
transaction_type
status

The Action must preserve the authorization boundary of the requesting Principal.

For example:

Customer A
    ↓
search_transactions
    ↓
Account A

must not silently become:

Customer A
    ↓
search_transactions
    ↓
Account B

⸻

7. Action: get_spending_summary

get_spending_summary retrieves or produces an authorized summary of spending activity.

Conceptually:

get_spending_summary(
    account_id,
    period,
    grouping
)

Possible grouping dimensions include:

category
merchant
time
transaction_type

The source and derivation semantics must be explicit.

If the result is calculated from transaction data, the result is derived data rather than canonical Business State.

For example:

Transactions
    ↓
Aggregation
    ↓
Spending Summary

The summary must not be represented as though it were an authoritative ledger fact unless the enterprise explicitly defines it as such.

⸻

8. Action: create_complaint

create_complaint creates a complaint or support case within the enterprise Support System.

Conceptually:

create_complaint(
    customer_id,
    subject,
    description,
    related_resource
)

Expected result:

{
    case_id
    status
    created_at
}

The Support System becomes authoritative for the resulting case.

Noema records the execution journey but does not become the System of Record for the complaint.

⸻

9. Action Characteristics

Every Action should have explicit characteristics.

Conceptually:

Action {
    action_id
    name
    version
    domain
    target
    input_schema
    output_schema
    preconditions
    postconditions
    authorization_requirements
    risk_class
    idempotency
    timeout
    retry_policy
    failure_policy
}

The exact representation may vary by implementation.

The semantic contract must remain explicit.

⸻

10. Action Identity

Each executable Action should have a stable identifier.

Example:

action_id:
account.balance.read

or:

action_id:
transaction.search

The identifier should be stable enough to support:

auditability
authorization
policy
execution
observability
versioning
replay analysis

Natural-language labels should not be the sole Action identity.

⸻

11. Action Version

Actions may evolve.

Example:

search_transactions:v1
search_transactions:v2

A version change may affect:

input schema
output schema
authorization
semantics
preconditions
postconditions
failure behavior

Execution records should preserve the Action version used.

⸻

12. Action Input

Action inputs must be typed.

Example:

search_transactions {
    account_id: AccountID
    date_from: Timestamp
    date_to: Timestamp
}

Noema should not pass unrestricted natural-language strings directly into consequential enterprise operations when a typed contract can be established.

Natural language belongs primarily at the Intent layer.

Typed data belongs at the Action layer.

⸻

13. Action Output

Action outputs should also be typed.

For example:

get_account_balance
    ↓
BalanceResult

rather than:

get_account_balance
    ↓
arbitrary model-readable text

Typed outputs make downstream validation and postcondition evaluation deterministic.

⸻

14. Action Target

An Action must identify the enterprise Resource or capability it operates against.

Examples:

get_account_balance
    → Account
retrieve_statement
    → Statement
search_transactions
    → Transaction collection
get_spending_summary
    → Spending data
create_complaint
    → Support Case

The target must be resolved before execution where the Action requires a specific Resource.

⸻

15. Action and Intent

Intent and Action are distinct.

Example:

Intent:
"How much money do I have?"
        ↓
Resolved Intent:
account_balance_inquiry
        ↓
Action:
get_account_balance

The model may assist with Intent interpretation.

The final Action must be selected through Noema’s deterministic resolution process.

⸻

16. Action and Planning

Planning determines the Action sequence required to satisfy an Intent.

For a simple balance inquiry:

Intent
   ↓
resolve identity
   ↓
resolve account
   ↓
get_account_balance
   ↓
verify result
   ↓
respond

For a statement request:

Intent
   ↓
resolve identity
   ↓
resolve account
   ↓
resolve period
   ↓
retrieve_statement
   ↓
verify result
   ↓
respond

Planning must not introduce Actions that exceed the resolved Intent.

⸻

17. Action and Preconditions

An Action may have Preconditions.

For example:

get_account_balance
Preconditions:
    principal authenticated
    account resolved
    principal authorized for account

Execution should not proceed when required Preconditions are unsatisfied.

Preconditions
      ↓
  satisfied?
    /     \
  yes      no
   ↓        ↓
Action   Block / Clarify / Escalate

⸻

18. Action and Postconditions

An Action may define Postconditions.

For example:

retrieve_statement
Postcondition:
    requested statement was retrieved

For:

create_complaint

a Postcondition may be:

Support System contains the newly created case

Postconditions should be verified using authoritative state where required.

⸻

19. Action and Trust

Trust determines whether the Action may proceed.

Conceptually:

Intent
   ↓
Context
   ↓
Evidence
   ↓
Trust
   ↓
Action

The Action itself must not decide whether uncertain information is trustworthy.

Trust and Policy determine whether execution is permitted.

⸻

20. Action and Authorization

Authorization is evaluated independently of Intent interpretation.

Conceptually:

Principal
    +
Action
    +
Resource
    +
Scope
    ↓
Authorization

For example:

Customer A
    +
search_transactions
    +
Account A
    ↓
ALLOW

Authorization should not be inferred merely because the Customer requested the information.

⸻

21. Action and Canonical Data

Actions should use Canonical Data when required for consequential decisions.

Example:

get_account_balance
        ↓
Ledger
        ↓
Canonical Balance

Noema should not substitute a model inference for authoritative enterprise state.

⸻

22. Action and Context

Context supplies the information required to construct and execute an Action.

Example:

Context
├── principal_id
├── account_id
├── requested_period
└── authorization_context

Context is not itself the Action.

Context
    ↓
Action Inputs
    ↓
Action

Only the required Context should be supplied to the Action.

⸻

23. Action and Evidence

Action execution can generate Evidence.

Example:

get_account_balance
        ↓
Ledger Response
        ↓
Evidence

The Evidence should preserve enough information to establish:

source
observation time
resource
result
version
provenance

This allows Noema to explain the basis of the resulting Outcome.

⸻

24. Action and Business State

Read Actions observe Business State.

For example:

get_account_balance
    ↓
Account Balance

The Action does not mutate the balance.

Likewise:

search_transactions
    ↓
Transactions

does not change the transaction state.

This is a deliberate property of the Phase 1 reference workflow.

⸻

25. Action and Noema State

Although Noema does not own the enterprise Business State, it owns the state of its own execution.

For example:

Action State:
    planned
    authorized
    executing
    succeeded
    failed

Therefore:

Enterprise
    → owns Business State
Noema
    → owns Execution State

⸻

26. Action and Enterprise Capability

An Action is an abstraction over an enterprise capability.

Conceptually:

Noema Action
      ↓
Integration
      ↓
Enterprise API / Service
      ↓
Enterprise System

For example:

get_account_balance
      ↓
Account API
      ↓
Ledger

Noema should not couple the semantic Action definition unnecessarily to a particular transport mechanism.

⸻

27. Action vs API

An API is an interface exposed by a system.

An Action is a semantic executable operation recognized by Noema.

For example:

Enterprise API:
GET /accounts/{id}/balance
Noema Action:
get_account_balance

The API is an implementation interface.

The Action is the semantic execution unit.

⸻

28. Action vs Tool

A Tool is an integration mechanism that allows Noema to interact with an external capability.

An Action describes the operation being performed.

Action
   ↓
Tool / Integration
   ↓
Enterprise API

One Tool may expose multiple Actions.

One Action may potentially be implemented through different integrations.

⸻

29. Action Contracts

Every Action should have an explicit contract.

Conceptually:

Action Contract {
    identity
    purpose
    actor_requirements
    input_schema
    output_schema
    target
    preconditions
    authorization
    trust_requirements
    postconditions
    idempotency
    timeout
    retry_policy
    failure_policy
}

The contract defines the boundary within which Noema may execute.

⸻

30. Action Risk

Actions should have explicit risk classification.

For the reference workflow:

get_account_balance
    → read
retrieve_statement
    → read
search_transactions
    → read
get_spending_summary
    → read / derived read
create_complaint
    → support write

create_complaint changes support-system state but does not move money or alter financial account state.

Risk classification should therefore be based on the actual Business State affected.

⸻

31. Action Scope

Every Action must operate within an explicit scope.

Possible dimensions include:

tenant
organization
principal
account
resource
environment
time range

For example:

search_transactions
    account = 123
    period = 2026-08-01 → 2026-08-31

An Action should not silently expand its scope beyond the resolved request.

⸻

32. Action Minimization

Noema should execute the smallest Action necessary to satisfy the Intent.

Example:

Intent:
"What is my balance?"
Required:
get_account_balance

Noema should not retrieve:

full transaction history
complete customer profile
all account statements

unless required by Policy or the workflow.

This reduces:

data exposure
execution complexity
latency
risk

⸻

33. Action Composition

Actions may be composed into a workflow.

Example:

resolve_identity
      ↓
resolve_account
      ↓
search_transactions
      ↓
get_spending_summary

The resulting execution plan remains a sequence of typed Actions.

Composition must preserve:

authorization
Trust
Preconditions
Postconditions
failure semantics
data boundaries

⸻

34. Action Dependencies

Actions may depend on outputs from previous Actions.

Example:

resolve_identity
       ↓
customer_id
       ↓
resolve_account
       ↓
account_id
       ↓
get_account_balance

A dependent Action must not execute until its required dependency has produced an acceptable result.

⸻

35. Action Failure

An Action can fail because of:

validation failure
authorization failure
enterprise rejection
timeout
network failure
unavailability
conflicting state
invalid input
unexpected response

Failure must be represented explicitly.

Action
   ↓
Failure
   ↓
Failure Policy
   ↓
Retry / Clarify / Escalate / Reject / Recover

Noema must not represent an unknown execution result as success.

⸻

36. Action Retry

Retries must be governed by the Action contract and failure Policy.

A retry may be appropriate for:

temporary network failure
transient service unavailable
timeout

A retry is not automatically appropriate for:

authorization denied
invalid input
ambiguous identity
policy rejection

Retry semantics must be explicit.

⸻

37. Action Idempotency

Idempotency must be defined per Action.

For read Actions:

get_account_balance
retrieve_statement
search_transactions
get_spending_summary

repeated execution should not intentionally mutate the underlying Business State.

For:

create_complaint

duplicate execution could create duplicate cases.

Therefore, an idempotency strategy should be defined.

For example:

idempotency_key
    ↓
Support System

Noema must not assume that every Action is naturally idempotent.

⸻

38. Action Timeout

Actions should have bounded execution time.

Conceptually:

Action
    ↓
Timeout
    ↓
UNKNOWN

A timeout does not necessarily mean the enterprise Action failed.

The enterprise system may have accepted the request while the response was lost.

Noema must distinguish:

FAILED

from:

UNKNOWN

when the execution semantics require it.

⸻

39. Action Outcome

An Action Outcome describes what happened after execution.

Possible states include:

SUCCEEDED
FAILED
REJECTED
UNKNOWN

The Outcome should be determined from execution evidence and verification rather than inferred from the absence of an error.

⸻

40. Action Verification

Where required, Noema should verify the resulting state against the authoritative enterprise system.

For example:

create_complaint
      ↓
Support System
      ↓
case_id returned
      ↓
verify case
      ↓
Outcome

Verification requirements depend on Action semantics and Policy.

⸻

41. Action and Ambiguity

An Action must not execute against an unresolved target.

Example:

Intent:
"Show my transactions."
Possible accounts:
Account A
Account B

If the relevant account cannot be deterministically established:

search_transactions
        ↓
BLOCKED
        ↓
CLARIFICATION

The Action does not choose between the candidates.

⸻

42. Action and Human Intervention

An Action may transition to human intervention when:

Trust is insufficient
authorization is unclear
enterprise data conflicts
policy requires review
execution state is unknown

Conceptually:

Action
   ↓
Uncertainty
   ↓
Human Intervention
   ↓
Decision
   ↓
Resume / Reject / Escalate

Human intervention must itself be auditable.

⸻

43. Action and Data Boundaries

Action inputs and outputs should contain only the data required by the Action.

For example:

search_transactions

may require:

account_id
date_range
filters

It should not automatically receive:

full customer profile
unrelated accounts
internal authentication secrets
unrelated financial information

Action contracts therefore enforce data minimization.

⸻

44. Action and Temporal State

Some Actions depend on temporal constraints.

Example:

search_transactions
    period = yesterday

The Action contract should preserve the resolved time interval rather than leaving temporal interpretation implicit.

For example:

date_from
date_to
timezone

This prevents ambiguity during execution and audit.

⸻

45. Action and Provenance

Execution records should preserve:

Action ID
Action version
inputs
target
source system
execution time
result
Outcome

This establishes provenance for the execution journey.

⸻

46. Action and Auditability

For consequential operations, Noema should be able to reconstruct:

which Intent
which Action
which Actor
which Principal
which Resource
which Policy
which Trust decision
which enterprise system
which result
which Outcome

This is a core requirement of the Action model.

⸻

47. Action and Events

Enterprise Events may provide evidence relevant to an Action.

Example:

Transaction System
      ↓
transaction.updated
      ↓
Noema

Events may support Context and verification.

They do not automatically replace authoritative Action execution or state verification.

⸻

48. Action Execution Boundary

The Action is the boundary where Noema transitions from reasoning about what should happen to requesting that something happen.

Reasoning
    ↓
Intent
    ↓
Trust
    ↓
Policy
    ↓
Action
    │
    ├── execution boundary
    ▼
Enterprise System

After this boundary, Noema must rely on execution evidence rather than model expectation.

⸻

49. Action Determinism

Once an Action has been resolved and approved:

Action
+
typed inputs
+
approved policy
+
satisfied Preconditions

must determine a specific execution operation.

The model should not remain responsible for deciding what operation is performed after the Action boundary has been established.

⸻

50. Action Model

Conceptually:

Action {
    id
    version
    intent_reference
    actor
    principal
    target
    inputs
    output
    preconditions
    postconditions
    authorization
    trust_requirements
    risk_class
    idempotency
    timeout
    retry_policy
    failure_policy
    provenance
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

51. Reference Action Graph

The Customer Account Inquiry workflow can be represented as:

                    INTENT
                       │
                       ▼
               IDENTITY RESOLUTION
                       │
                       ▼
                RESOURCE RESOLUTION
                       │
                       ▼
                    TRUST
                       │
                       ▼
                  AUTHORIZATION
                       │
                       ▼
                    ACTION
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
   BALANCE        STATEMENT       TRANSACTIONS
        │              │               │
        └──────────────┼───────────────┘
                       │
                       ▼
                 SPENDING SUMMARY
                       │
                       ▼
                 COMPLAINT LOGGING
                       │
                       ▼
                 SUPPORT SYSTEM

The actual path is determined by the resolved Intent.

⸻

52. Reference Action Selection

The mapping from Intent to Action should be explicit.

"What's my balance?"
        ↓
get_account_balance
"Show my statement."
        ↓
retrieve_statement
"Find my transaction from yesterday."
        ↓
search_transactions
"How much did I spend last month?"
        ↓
get_spending_summary
"I don't recognize this transaction."
        ↓
create_complaint

The examples represent semantic mappings, not unrestricted natural-language-to-API translation.

⸻

53. Unsupported Actions

The workflow must explicitly recognize when an Intent does not map to an available Action.

Example:

"Transfer $5,000 to John."

No corresponding Phase 1 Action exists.

Therefore:

Intent
    ↓
No supported Action
    ↓
REJECT / ESCALATE

Noema must not manufacture an Action because an enterprise API happens to expose a corresponding capability.

⸻

54. Action Boundary and Commercial Scope

The reference workflow intentionally excludes financial write Actions such as:

transfer_money
make_payment
withdraw_funds
refund_payment
close_account
change_account_details

These may be future capabilities.

They are not part of this reference workflow.

The purpose of the current Action set is to demonstrate safe, high-frequency account support and information retrieval.

⸻

55. Action Invariants

Invariant 1

Every executable operation must correspond to a defined Action.

Invariant 2

Intent and Action are distinct semantic objects.

Invariant 3

Natural-language Intent must not directly become an unrestricted enterprise API invocation.

Invariant 4

Every Action must have an explicit executable contract.

Invariant 5

Action inputs and outputs must be typed.

Invariant 6

Every consequential Action must have an explicit target and scope.

Invariant 7

Action authorization must be evaluated independently of Intent interpretation.

Invariant 8

Action execution must satisfy required Preconditions.

Invariant 9

Required Postconditions must be verified according to Action and Policy.

Invariant 10

Noema must not execute an Action against an unresolved consequential Resource.

Invariant 11

Ambiguity must transition to clarification, escalation, or another deterministic Policy-defined state.

Invariant 12

Action failure must never be represented as successful execution.

Invariant 13

Unknown execution state must remain distinguishable from failure.

Invariant 14

Retry behavior must be explicitly defined by Action and Policy.

Invariant 15

Idempotency must be explicitly defined for Actions whose repeated execution could mutate state.

Invariant 16

Action scope must not expand implicitly beyond the resolved Intent.

Invariant 17

Action execution must respect enterprise data boundaries and least privilege.

Invariant 18

Noema must preserve the distinction between an Action and the underlying enterprise API or Tool.

Invariant 19

Enterprise Systems remain authoritative for Business State accessed by Actions.

Invariant 20

Noema remains authoritative only for the execution state it owns.

Invariant 21

Action execution should preserve sufficient provenance for audit and reconstruction.

Invariant 22

Model-generated information must not silently become Action input where deterministic enterprise data is required.

Invariant 23

Action selection must be deterministic once the required Intent, Trust, Policy, and Context conditions have been satisfied.

Invariant 24

An enterprise capability does not automatically become a supported Noema Action.

Invariant 25

The Phase 1 Customer Account Inquiry workflow must remain limited to the defined read and support operations.

⸻

56. Final Definition

An Action is a typed, bounded, policy-constrained executable operation through which Noema invokes an enterprise capability to satisfy a resolved Intent.

The fundamental relationship is:

CUSTOMER INTENT
       │
       ▼
INTENT RESOLUTION
       │
       ▼
CONTEXT + EVIDENCE
       │
       ▼
TRUST + POLICY
       │
       ▼
ACTION
       │
       ▼
ENTERPRISE CAPABILITY
       │
       ▼
BUSINESS STATE
       │
       ▼
OUTCOME
       │
       ▼
VERIFICATION

And the architectural rule is:

Noema does not execute what the model happens to suggest. Noema executes a defined Action whose inputs, authority, Preconditions, execution semantics, and Outcome are explicitly bounded by contract and Policy.