> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Actions

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/actions.md

⸻

1. Definition

An Action is a typed, bounded, policy-constrained executable operation through which Noema invokes an enterprise capability to satisfy a resolved Intent.

Within the Customer Account Inquiry workflow, Actions are deliberately limited to read and support operations.

The reference Actions are:

* get_account_balance
* retrieve_statement
* search_transactions
* get_spending_summary
* create_complaint

An Action is not:

* Intent
* Executable Intent
* Workflow
* Workflow Step
* Workflow Plan
* Tool
* Integration
* API Request
* Business State
* Context
* Evidence
* Outcome

The distinction is fundamental:

Intent
   ↓
Intent Resolution
   ↓
Executable Intent
   ↓
Workflow
   ↓
Workflow Step
   ↓
Action
   ↓
Enterprise Capability
   ↓
Execution
   ↓
Outcome / Evidence

An Intent expresses what the Customer wants.

A Workflow coordinates how the resolved Intent is accomplished.

An Action expresses the specific executable operation that Noema is permitted to invoke.

⸻

2. Purpose

The purpose of the Action model is to establish the executable boundary between:

Customer Intent
       ↓
Intent Resolution
       ↓
Executable Intent
       ↓
Workflow Planning
       ↓
Action
       ↓
Enterprise Capability
       ↓
Execution
       ↓
Outcome

Actions provide the controlled interface through which Noema interacts with enterprise systems.

They prevent natural-language Intent, model output, or dynamically generated plans from becoming unrestricted instructions to enterprise infrastructure.

The Action contract therefore establishes what operation may be executed, against which Resource, with which inputs, under which authority, Preconditions, Policy, and Trust requirements.

⸻

3. Action as the Execution Boundary

The Action is the semantic boundary between determining what should be executed and requesting that the enterprise capability perform or return something.

Reasoning / Resolution
        ↓
Intent
        ↓
Workflow Planning
        ↓
Trust / Policy
        ↓
Action
        │
        ├── execution boundary
        ▼
Enterprise Capability
        ↓
Execution
        ↓
Outcome + Evidence

Before the Action boundary, Noema may resolve Intent, construct Context, plan a Workflow, evaluate Policy, and determine whether execution is permitted.

After the Action boundary, Noema must rely on execution evidence rather than model expectation.

The model does not remain responsible for deciding what operation is performed once a defined Action has been established and approved.

⸻

4. Reference Action Set

The Customer Account Inquiry workflow defines five initial Actions:

Action	Purpose	Primary Domain	State Effect
get_account_balance	Retrieve the current account balance	Account / Ledger	Read
retrieve_statement	Retrieve an account statement	Statement	Read
search_transactions	Search account transactions	Transaction	Read
get_spending_summary	Retrieve or calculate an authorized spending summary	Transaction / Analytics	Read / Derived Read
create_complaint	Create a customer complaint or support case	Support	Support-System Write

These Actions are sufficient to demonstrate the initial read/support wedge without introducing financial write operations.

The Action set is intentionally bounded.

An enterprise capability does not automatically become a supported Noema Action merely because an API exposes it.

⸻

5. Action Identity

Every executable Action should have a stable identity.

Conceptually:

Action {
    action_id
    name
    version
}

Examples:

account.balance.read
transaction.search
statement.retrieve
spending.summary.read
support.complaint.create

The identity should be stable enough to support:

* authorization
* Policy
* Trust evaluation
* execution
* observability
* auditability
* versioning
* replay analysis
* Workflow reconstruction

Natural-language labels should not be the sole Action identity.

⸻

6. Action Version

Actions may evolve.

Examples:

search_transactions:v1
search_transactions:v2

A version change may affect:

* input schema
* output schema
* authorization requirements
* semantics
* Preconditions
* Postconditions
* risk classification
* idempotency
* timeout behavior
* retry behavior
* failure semantics

Execution records should preserve the Action version used.

Historical execution must remain interpretable according to the Action contract that governed that execution.

⸻

7. Action Contract

Every executable Action should have an explicit semantic contract.

Conceptually:

Action Contract {
    identity
    purpose
    actor_requirements
    principal_requirements
    target
    scope
    input_schema
    output_schema
    preconditions
    postconditions
    authorization_requirements
    trust_requirements
    policy_requirements
    risk_class
    idempotency
    timeout
    retry_policy
    failure_policy
    verification_requirements
    provenance_requirements
}

The exact representation may vary by implementation.

The semantic contract must remain explicit.

The contract is the bounded execution surface through which Noema may invoke the enterprise capability.

⸻

8. Action Input

Action inputs must be typed.

Example:

search_transactions {
    account_id: AccountID
    date_from: Timestamp
    date_to: Timestamp
    filters: TransactionFilters
}

Noema should not pass unrestricted natural-language strings directly into consequential enterprise operations when a typed contract can be established.

Natural language belongs primarily at the Intent layer.

Typed, validated data belongs at the Action layer.

The Action contract should define:

* required fields
* optional fields
* data types
* valid ranges
* enumerations
* temporal semantics
* resource identifiers
* scope constraints

⸻

9. Action Output

Action outputs should also be typed.

For example:

get_account_balance
        ↓
BalanceResult

rather than:

get_account_balance
        ↓
arbitrary model-readable text

Typed outputs make downstream:

* validation
* verification
* Postcondition evaluation
* Workflow transitions
* audit
* reconciliation

more deterministic.

An Action output is not automatically canonical Business State.

Its authority depends on the enterprise source and the semantics of the Action.

⸻

10. Action Target

Every Action must identify the enterprise Resource or capability against which it operates.

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

Noema must not silently substitute an alternative Resource because it happens to be available.

⸻

11. Action Scope

Every Action must operate within an explicit scope.

Possible dimensions include:

* tenant
* organization
* Principal
* account
* Resource
* environment
* time range

Example:

search_transactions
    account = ACC-123
    period = 2026-08-01 → 2026-08-31

An Action must not silently expand its scope beyond the resolved Intent and applicable Policy.

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

12. Action: get_account_balance

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

Noema does not calculate, infer, or invent the balance.

The returned balance is an observation from the enterprise source at a particular point in time.

⸻

13. Action: retrieve_statement

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

The Statement System remains authoritative for the statement Resource.

The requested period must be explicitly resolved before execution.

Temporal interpretation must not remain implicit at the Action boundary.

⸻

14. Action: search_transactions

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

The query must operate only against Resources for which the Principal has the required authority.

⸻

15. Action: get_spending_summary

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

If the result is calculated from transaction data:

Transactions
      ↓
Aggregation
      ↓
Spending Summary

the result is derived data rather than canonical Business State.

It must not be represented as an authoritative ledger fact unless the enterprise explicitly defines it as such.

⸻

16. Action: create_complaint

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

Because this Action mutates Support-System state, its authorization, idempotency, Policy, and verification requirements must be explicit.

⸻

17. Action and Intent

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

The final Action must be selected through Noema’s resolution and Workflow semantics.

An Action must not be selected merely because a model generated a plausible operation.

⸻

18. Action and Executable Intent

An executable Intent defines what Noema is permitted and expected to accomplish.

The Action is one executable operation through which the Workflow operationalizes that Intent.

Executable Intent
        ↓
Workflow
        ↓
Workflow Step
        ↓
Action

Every consequential Action should remain traceable to:

* the initiating Intent
* the relevant Workflow
* the relevant Workflow Step
* the Principal
* the Resource
* applicable Policy
* relevant Trust evaluation

⸻

19. Action and Workflow

A Workflow coordinates multiple Actions.

An Action performs one bounded operation.

Workflow
   │
   ├── Step A → Action A
   ├── Step B → Action B
   ├── Step C → Decision
   └── Step D → Action C

Therefore:

Workflow ≠ Action

For example:

Workflow:
customer_account_inquiry
Possible Actions:
get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

The Workflow determines the relationship, ordering, dependencies, waiting, verification, and failure behavior between Actions.

The Action defines the executable operation itself.

⸻

20. Action and Workflow Step

A Workflow Step is the execution position within a Workflow.

An Action is the executable operation associated with an Action Step.

Conceptually:

Workflow Step {
    step_id
    type
    dependencies
    state
}

For an Action Step:

Workflow Step
      ↓
Action
      ↓
Execution
      ↓
Outcome

Not every Workflow Step is necessarily an Action.

A Workflow may also contain:

* decisions
* waits
* human intervention
* verification
* compensation

This distinction prevents the Action model from absorbing Workflow semantics.

⸻

21. Action and Planning

Planning determines which Actions are required and how they are coordinated within the Workflow.

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

Planning may be dynamic.

However, a dynamically proposed Action must correspond to a defined executable Action contract before execution.

The model may propose.

Noema validates.

⸻

22. Candidate Action vs Executable Action

A model or planning process may produce a candidate Action.

For example:

Model
   ↓
Candidate:
search_transactions

This does not itself establish permission to execute.

The candidate must pass Noema’s execution controls:

Candidate Action
       ↓
Action Resolution
       ↓
Contract Validation
       ↓
Target Resolution
       ↓
Preconditions
       ↓
Authorization
       ↓
Trust
       ↓
Policy
       ↓
Executable Action

A model-generated operation is therefore not equivalent to an authorized executable Action.

⸻

23. Action Preconditions

An Action may have Preconditions.

For example:

get_account_balance
Preconditions:
    Principal authenticated
    Account resolved
    Principal authorized for Account

Execution should not proceed when required Preconditions are unsatisfied.

Conceptually:

Preconditions
      ↓
   satisfied?
    /     \
  yes      no
   ↓        ↓
Action   Block / Clarify / Escalate

Preconditions must be evaluated against appropriately current and authoritative information.

⸻

24. Action Postconditions

An Action may define Postconditions.

For example:

retrieve_statement
Postcondition:
requested Statement was retrieved

For:

create_complaint

a Postcondition may be:

Support System contains the newly created case

Postconditions should be verified using authoritative state where required.

An API response alone does not necessarily establish the Postcondition.

⸻

25. Action and Canonical Data

Actions should use authoritative enterprise data when required for consequential execution decisions.

Example:

get_account_balance
        ↓
Ledger
        ↓
Canonical Balance

Noema should not substitute a model inference for authoritative enterprise state.

Where enterprise state is required to satisfy an Action Precondition, the relevant System of Record remains authoritative.

⸻

26. Action and Context

Context supplies information required to construct and execute an Action.

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

Context should remain scoped to the relevant Workflow and Step where possible.

⸻

27. Action and Evidence

Action execution can generate Evidence.

Example:

get_account_balance
        ↓
Ledger Response
        ↓
Evidence

Evidence should preserve enough information to establish:

* source
* observation time
* Resource
* result
* Action identity
* Action version
* provenance

Evidence supports verification, Workflow transitions, auditability, and reconstruction.

Evidence is not automatically equivalent to canonical Business State.

⸻

28. Action and Business State

Read Actions observe Business State.

For example:

get_account_balance
    ↓
Account Balance

does not mutate the balance.

Likewise:

search_transactions
    ↓
Transactions

does not change transaction state.

This is a deliberate property of the Phase 1 reference workflow.

create_complaint is different: it creates state in the Support System.

The distinction is therefore:

Read Action
    → observes enterprise Business State
Support Write Action
    → mutates Support-System state

The enterprise system remains authoritative for the state it owns.

⸻

29. Action and Noema State

Although Noema does not own enterprise Business State, it owns the state of its own execution.

For example:

Action State:
    PLANNED
    AUTHORIZED
    EXECUTING
    SUCCEEDED
    FAILED
    UNKNOWN

Therefore:

Enterprise
    → owns Business State
Noema
    → owns Action / Execution State

Noema must not confuse its own execution state with the state of the enterprise Resource.

⸻

30. Action and Enterprise Capability

An Action is a semantic abstraction over an enterprise capability.

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

31. Action vs API

An API is an interface exposed by an enterprise system.

An Action is a semantic executable operation recognized by Noema.

For example:

Enterprise API:
GET /accounts/{id}/balance
Noema Action:
get_account_balance

The API is an implementation interface.

The Action is the semantic execution unit.

An Action may therefore remain stable while its underlying API or transport implementation changes.

⸻

32. Action vs Tool / Integration

A Tool or Integration is a mechanism through which Noema interacts with an external capability.

An Action describes the operation being performed.

Action
   ↓
Tool / Integration
   ↓
Enterprise API
   ↓
Enterprise System

One Tool may expose multiple Actions.

One Action may potentially be implemented through different integrations.

The Action contract should not be reduced to the implementation mechanism.

⸻

33. Action Authorization

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

Authorization must not be inferred merely because the Customer requested the information.

The existence of an Intent does not itself establish authority to execute the Action.

⸻

34. Action and Trust

Trust determines whether the relevant execution conditions are sufficiently established for the Action to proceed.

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

The Action itself does not decide whether uncertain information is trustworthy.

Trust and Policy determine whether execution is permitted.

Trust should not automatically be treated as permanently valid across an entire Workflow.

A later Action may introduce:

* higher risk
* different Resource
* different authority
* different Policy
* changed Business State

and therefore require a new Trust evaluation.

⸻

35. Action and Policy

Policy constrains Action execution.

Policy may define:

* allowed Actions
* required approvals
* risk thresholds
* sequencing requirements
* data requirements
* retry limits
* timeout behavior
* human intervention
* verification requirements
* completion conditions

Conceptually:

Action
   ↓
Policy Evaluation
   ↓
Permitted / Blocked

An Action contract defines executable semantics.

Policy determines whether those semantics may be exercised in the current context.

⸻

36. Action Risk

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

Risk classification should be based on the actual Business State affected.

create_complaint changes Support-System state but does not move money or alter financial account state.

Risk classification therefore must not be based solely on whether an operation is technically a write.

⸻

37. Action Minimization

Noema should execute the smallest Action or Action set necessary to satisfy the resolved Intent.

Example:

Intent:
"What is my balance?"
Required:
get_account_balance

Noema should not retrieve:

* full transaction history
* complete customer profile
* all account statements

unless required by the resolved Intent, Workflow semantics, Policy, or verification requirements.

Action minimization reduces:

* data exposure
* execution complexity
* latency
* unnecessary enterprise load
* risk

⸻

38. Action Data Boundaries

Action inputs and outputs should contain only the data required by the Action.

For example:

search_transactions

may require:

account_id
date_range
filters

It should not automatically receive:

* full customer profile
* unrelated accounts
* internal authentication secrets
* unrelated financial information

Action composition must not become an excuse for unrestricted data aggregation.

⸻

39. Action Dependency

Actions may depend on outputs from previous Workflow Steps.

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

Dependency satisfaction must be explicit rather than inferred from Workflow ordering alone.

⸻

40. Action Composition

Actions may be composed into a Workflow.

Example:

resolve_identity
      ↓
resolve_account
      ↓
search_transactions
      ↓
get_spending_summary

The resulting execution plan remains a sequence or graph of typed Actions coordinated by the Workflow.

Composition must preserve:

* authorization
* Trust
* Preconditions
* Postconditions
* Policy
* failure semantics
* data boundaries
* Resource boundaries

⸻

41. Action Failure

An Action can fail because of:

* validation failure
* authorization failure
* enterprise rejection
* timeout
* network failure
* service unavailability
* conflicting state
* invalid input
* unexpected response

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

42. Action Outcome

An Action Outcome describes the established result of execution.

Possible states include:

SUCCEEDED
FAILED
REJECTED
UNKNOWN

The exact semantics must distinguish:

* execution facts
* enterprise responses
* verification results
* assumptions

An Outcome should be established from execution evidence and applicable verification rather than inferred from the absence of an error.

⸻

43. Action Verification

Where required, Noema should verify the resulting state against the authoritative enterprise system.

Example:

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

A successful transport response does not necessarily establish that the intended enterprise state exists.

⸻

44. Action Timeout

Actions should have bounded execution time.

Conceptually:

Action
    ↓
Timeout
    ↓
UNKNOWN

A timeout does not necessarily mean the enterprise Action failed.

The enterprise system may have accepted or completed the request while the response was lost.

Noema must distinguish:

FAILED

from:

UNKNOWN

when the execution semantics require it.

⸻

45. Action Retry

Retries must be governed by the Action contract and failure Policy.

A retry may be appropriate for:

* temporary network failure
* transient service unavailability
* timeout

A retry is not automatically appropriate for:

* authorization denied
* invalid input
* ambiguous identity
* unresolved Resource
* Policy rejection

Retry behavior must be explicit.

⸻

46. Action Idempotency

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

Therefore an idempotency strategy should be defined.

For example:

idempotency_key
    ↓
Support System

Noema must not assume that every Action is naturally idempotent.

⸻

47. Action Unknown State

An Action may enter:

UNKNOWN

when Noema cannot establish whether the enterprise operation completed.

Example:

Request sent
    ↓
Connection lost
    ↓
Outcome UNKNOWN

Noema must not assume:

UNKNOWN = FAILED

or:

UNKNOWN = SUCCEEDED

without appropriate evidence.

Where required, reconciliation should establish the state before retrying a consequential operation.

⸻

48. Action and Reconciliation

When the execution result is unknown, Noema may reconcile against authoritative enterprise state.

Example:

create_complaint
      ↓
UNKNOWN
      ↓
Reconciliation
      ↓
Support System
      ↓
Case found
      ↓
Action = SUCCEEDED

Reconciliation prevents duplicate execution caused by treating uncertainty as failure.

The reconciliation source should be authoritative for the relevant Resource.

⸻

49. Action and Ambiguity

An Action must not execute against an unresolved consequential target.

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

The Action does not choose between candidates merely because one appears more likely.

⸻

50. Action and Human Intervention

An Action may transition to human intervention when:

* Trust is insufficient
* authorization is unclear
* enterprise data conflicts
* Policy requires review
* execution state is unknown
* an exception cannot be resolved deterministically

Conceptually:

Action
   ↓
Uncertainty / Exception
   ↓
Human Intervention
   ↓
Decision
   ↓
Resume / Reject / Escalate

Human intervention must be attributable and auditable.

⸻

51. Action and Temporal State

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

A relative expression such as “yesterday” should therefore be resolved before the Action boundary when its exact temporal meaning matters.

⸻

52. Action and Staleness

Action Preconditions may depend on enterprise state that changes over time.

Example:

Observed:
Account status = ACTIVE
Time passes
Current:
Account status = CLOSED

Noema must not automatically treat earlier Context or Evidence as current truth.

Freshness requirements should be determined by:

* Action
* Resource
* Policy
* risk

Consequential Actions may require fresh verification before execution.

⸻

53. Action and Concurrency

Enterprise state may change between Action Steps.

Example:

Step 1:
balance = $10,000
External change
Step 2:
balance = $2,000

Noema must respect enterprise concurrency semantics.

It should not assume that state observed earlier in the Workflow remains valid throughout execution.

Where required, the Action must use enterprise-supported mechanisms such as:

* resource versions
* optimistic concurrency
* conditional requests
* enterprise locking
* revalidation

⸻

54. Action and Resource Version

An Action may depend on a Resource version.

Example:

Account:
version = 42
Action expects:
version = 42
Enterprise system responds:
version = 43

The Workflow may need to:

* re-read
* revalidate
* re-plan
* clarify
* abort

according to Policy and Workflow semantics.

Noema must not silently treat a stale Resource version as current.

⸻

55. Action and Enterprise Authority

The enterprise system remains authoritative for the Business State affected or observed by an Action.

For example:

Noema:
Action = get_account_balance
Outcome = SUCCEEDED
Ledger:
balance = $4,250

Noema’s successful Action execution does not make Noema the authority for the balance.

Similarly:

Noema:
create_complaint = SUCCEEDED
Support System:
case = CASE-123

The Support System remains authoritative for the case.

⸻

56. Action and Noema System of Record

Noema may be authoritative for its own execution records, including:

* Action State
* execution identity
* execution attempt
* Trust Decision
* Policy Decision
* intervention state
* execution Outcome

The enterprise remains authoritative for its own Business State.

Therefore:

Noema System of Record
        │
        ├── Intent
        ├── Workflow
        ├── Workflow Step
        ├── Trust
        └── Execution

while:

Enterprise Systems of Record
        │
        ├── Account
        ├── Payment
        ├── Customer
        ├── Transaction
        └── Support Case

remain separate.

⸻

57. Action and Events

Enterprise Events may provide Evidence relevant to an Action.

Example:

Transaction System
      ↓
transaction.updated
      ↓
Noema

Events may support:

* Context
* Workflow transitions
* verification
* reconciliation

They do not automatically replace authoritative Action execution or current-state verification.

An event indicates that an event occurred; where current authoritative state matters, Noema may still query the System of Record.

⸻

58. Action Provenance

Execution records should preserve sufficient provenance to reconstruct the operation.

Conceptually:

Action ID
Action Version
Intent Reference
Workflow ID
Step ID
Principal
Actor
Target
Inputs
Source System
Execution Time
Result
Outcome
Verification

This establishes provenance for the execution journey.

Where sensitive data is involved, provenance must remain subject to applicable data-access and security boundaries.

⸻

59. Action Auditability

For consequential operations, Noema should be able to reconstruct:

* which Intent
* which Workflow
* which Workflow Step
* which Action
* which Action version
* which Actor
* which Principal
* which Resource
* which scope
* which Policy
* which Trust decision
* which enterprise system
* which inputs
* which result
* which Evidence
* which Outcome
* which verification

This is a core requirement of the Action model.

⸻

60. Action Execution Record

Conceptually:

Action Execution {
    execution_id
    intent_id
    workflow_id
    step_id
    action_id
    action_version
    actor
    principal
    target
    scope
    inputs
    started_at
    completed_at
    source_system
    result
    outcome
    evidence
    verification
    retry_count
    policy_reference
    trust_reference
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

61. Action Determinism

Once an Action has been resolved and approved:

Action
+
typed inputs
+
resolved target
+
approved Policy
+
satisfied Preconditions

must determine a specific execution operation.

The model should not remain responsible for deciding what operation is performed after the Action boundary has been established.

If the Action requires dynamic parameters, those parameters must be resolved and validated through the Action contract.

⸻

62. Action Contract vs Model Output

Model output is not an Action contract.

For example:

Model:
"Use the account balance API."

does not establish an executable Action.

The valid path is:

Model / Resolution
       ↓
Candidate Action
       ↓
Defined Action Registry / Contract
       ↓
Target + Input Validation
       ↓
Authorization
       ↓
Trust
       ↓
Policy
       ↓
Executable Action

Noema executes defined Actions rather than arbitrary operations generated by the model.

⸻

63. Action Capability Boundary

The Action set defines the capabilities Noema has explicitly recognized for the reference workflow.

For example:

Supported:
get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

This does not imply support for every operation exposed by the underlying enterprise systems.

The supported Action surface is intentionally narrower than the enterprise API surface.

⸻

64. Unsupported Actions

The workflow must explicitly recognize when an Intent does not map to an available Action.

Example:

Intent:
"Transfer $5,000 to John."

No corresponding Phase 1 Action exists.

Therefore:

Intent
    ↓
No supported Action
    ↓
REJECT / ESCALATE

Noema must not manufacture an Action because an enterprise API happens to expose a corresponding capability.

This preserves the boundary between enterprise capability and Noema-supported capability.

⸻

65. Action Selection

The mapping from resolved Intent to Action should be explicit.

Examples:

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

These examples represent semantic mappings, not unrestricted natural-language-to-API translation.

⸻

66. Action Selection and Workflow Construction

Action selection is part of Workflow construction.

Conceptually:

Intent
   ↓
Intent Resolution
   ↓
Executable Intent
   ↓
Workflow Construction
   ↓
Action Selection
   ↓
Action Validation
   ↓
Execution

The selected Action must remain within:

* the resolved Intent
* available enterprise capabilities
* the Action registry
* authorization scope
* Policy
* Trust
* Resource constraints

⸻

67. Action Scope Must Not Expand

The Action selected must satisfy the resolved Intent without silently broadening it.

Example:

Intent:
"Show transactions from August."
Valid:
search_transactions
    account = resolved account
    period = August

It should not silently become:

search_transactions
    all accounts
    all historical transactions

unless the resolved Intent and applicable authorization explicitly permit that scope.

⸻

68. Action and Least Privilege

Action execution should follow least-privilege principles.

The Action should request only:

* the required Resource
* the required fields
* the required time range
* the required operation
* the required enterprise capability

The fact that a broader enterprise capability is available does not justify broader access.

⸻

69. Action and Security

Action execution must preserve security boundaries.

An Action must not become a mechanism for:

* privilege escalation
* tenant crossing
* authorization bypass
* data leakage
* unauthorized delegation

Each consequential Action remains subject to relevant security, authorization, Trust, and Policy requirements.

⸻

70. Action and Principal Attribution

The technical execution identity may differ from the originating Customer or Principal.

For example:

Customer Principal
       ↓
Noema
       ↓
Service Execution Identity
       ↓
Enterprise System

The execution record must preserve attribution to the originating Principal and the technical Actor where relevant.

This allows Noema to distinguish:

* who requested the operation
* who was authorized
* which execution identity invoked the enterprise capability
* which system performed the operation

⸻

71. Action and Human Approval

Some Actions may require human approval.

Conceptually:

Action
   ↓
Approval Required
   ↓
Approver
   ↓
Approved
   ↓
Execute

Approval should be bound to the relevant:

* Intent
* Workflow
* Workflow Step
* Action
* Resource
* parameters
* scope
* approving Principal

where required.

Approval must not silently become authorization for unrelated Actions.

⸻

72. Action and Cancellation

An Action may be cancelled before execution when Workflow and Policy permit cancellation.

Once enterprise execution has begun, cancellation may not be equivalent to rollback.

For example:

Action
   ↓
Request submitted
   ↓
Cancellation requested

does not necessarily establish:

Enterprise operation = cancelled

Current enterprise state must be established according to the relevant Action semantics.

⸻

73. Action and Irreversibility

Some Actions may be irreversible or only partially reversible.

The Phase 1 reference workflow excludes major financial write operations, but Action contracts should nevertheless distinguish:

* reversible operations
* compensatable operations
* non-reversible operations

Noema must not assume compensation exists merely because an Action failed later.

⸻

74. Action and Compensation

Compensation belongs primarily to Workflow semantics.

An Action may expose semantics relevant to compensation, but the Workflow determines whether compensation is required.

For example:

Workflow
   ↓
Action A = SUCCESS
Action B = SUCCESS
Action C = FAILED
   ↓
Compensation

Compensation may invoke additional defined Actions.

Compensation is not guaranteed to restore the exact prior Business State.

⸻

75. Action and Workflow Recovery

Action failure may cause the Workflow to:

* retry
* wait
* reconcile
* clarify
* escalate
* compensate
* fail

The Action contract supplies the relevant execution semantics.

The Workflow determines how that result affects the broader execution journey.

Therefore:

Action Failure
       ↓
Action Failure Policy
       ↓
Workflow Transition

⸻

76. Action History

Consequential Action execution history should be append-oriented where possible.

Noema should preserve:

* Action invocation
* execution attempt
* state transition
* Policy decision
* Trust decision
* Evidence
* result
* Outcome
* retry
* reconciliation
* human intervention

Historical execution should not be silently overwritten.

⸻

77. Action and Workflow Audit Trail

A consequential Action should remain reconstructable within its Workflow.

Conceptually:

Intent
   ↓
Workflow
   ↓
Workflow Step
   ↓
Action
   ↓
Trust
   ↓
Policy
   ↓
Execution
   ↓
Evidence
   ↓
Outcome

This allows Noema to explain:

* what operation was selected
* why it was selected
* who authorized it
* what Resource it targeted
* what evidence was available
* what enterprise system was invoked
* what actually happened

⸻

78. Action and Verification Boundary

The Action execution result and the verified enterprise state are distinct concepts.

For example:

Action:
create_complaint
Execution:
request accepted
Verification:
case exists in Support System

The Workflow may require the second fact before treating the Action as fully established.

Therefore:

API Response
    ≠ automatically
Verified Business State

Verification semantics must be defined by Action and Policy.

⸻

79. Action and External State Changes

Enterprise state may change independently of Noema.

For example:

Noema observes:
Account ACTIVE
External system changes:
Account CLOSED
Noema later executes an Action

The Action must evaluate current relevant state when required.

Earlier Context must not automatically satisfy current Preconditions.

⸻

80. Action and Long-Running Execution

An Action may involve an asynchronous enterprise operation.

For example:

Action
   ↓
Request submitted
   ↓
WAITING
   ↓
External Event
   ↓
Verification
   ↓
Outcome

Noema must not simulate completion merely because the expected external operation is likely to complete.

The Action remains unresolved until its defined execution semantics establish an Outcome.

⸻

81. Action and Events vs Current State

An event may establish that something happened.

It does not necessarily establish what the current state is.

Example:

transaction.updated

may indicate a transaction update event occurred.

If a consequential Action depends on the current transaction state, Noema may need to query the authoritative enterprise source.

⸻

82. Action and Reference Workflow Boundary

The Customer Account Inquiry reference workflow intentionally excludes financial write Actions such as:

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

83. Reference Action Graph

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
                          POLICY
                            │
                            ▼
                          ACTION
                            │
          ┌─────────────────┼──────────────────┐
          │                 │                  │
          ▼                 ▼                  ▼
      BALANCE          STATEMENT         TRANSACTIONS
          │                 │                  │
          └─────────────────┼──────────────────┘
                            │
                            ▼
                    SPENDING SUMMARY
                            │
                            ▼
                    COMPLAINT LOGGING
                            │
                            ▼
                      SUPPORT SYSTEM

The actual path is determined by the resolved Intent and Workflow.

The graph represents available Action relationships, not a mandatory sequence.

⸻

84. Reference Action Execution

A representative execution path is:

Customer Intent
       ↓
Intent Resolution
       ↓
Workflow Construction
       ↓
Action Selection
       ↓
Target Resolution
       ↓
Input Validation
       ↓
Trust Evaluation
       ↓
Authorization
       ↓
Policy Evaluation
       ↓
Preconditions
       ↓
Action Execution
       ↓
Enterprise Result
       ↓
Verification
       ↓
Outcome
       ↓
Workflow Transition

Each boundary has distinct semantics.

Noema must not collapse them into a single model-generated operation.

⸻

85. Action Execution Does Not Establish Workflow Success

A successful Action does not necessarily mean the Workflow succeeded.

Example:

Action A
   ↓
SUCCEEDED
Action B
   ↓
FAILED

The Workflow may therefore be:

FAILED

or:

PARTIALLY_COMPLETED

according to Workflow semantics and Policy.

Likewise:

Action = SUCCEEDED

does not automatically establish:

Workflow = SUCCEEDED

⸻

86. Action Outcome Does Not Equal Enterprise Outcome

An Action execution Outcome describes what Noema established about the Action execution.

It must not be confused with the complete enterprise Business State.

For example:

Action:
retrieve_statement
Outcome:
SUCCEEDED

means the retrieval operation was established as successful.

It does not mean Noema owns the Statement or becomes the authoritative source for it.

⸻

87. Action Invariants

Invariant 1

Every executable operation must correspond to a defined Action.

Invariant 2

Intent and Action are distinct semantic objects.

Invariant 3

Workflow and Action are distinct semantic objects.

Invariant 4

A Workflow Step and an Action are distinct concepts even when an Action Step invokes an Action.

Invariant 5

Natural-language Intent must not directly become an unrestricted enterprise API invocation.

Invariant 6

Every Action must have an explicit executable contract.

Invariant 7

Action inputs and outputs must be typed.

Invariant 8

Every consequential Action must have an explicit target and scope.

Invariant 9

Action authorization must be evaluated independently of Intent interpretation.

Invariant 10

Action execution must satisfy required Preconditions.

Invariant 11

Required Postconditions must be verified according to Action and Policy semantics.

Invariant 12

Noema must not execute an Action against an unresolved consequential Resource.

Invariant 13

Ambiguity must transition to clarification, escalation, or another deterministic Policy-defined state.

Invariant 14

Action failure must never be represented as successful execution.

Invariant 15

Unknown execution state must remain distinguishable from failure.

Invariant 16

Retry behavior must be explicitly defined by Action and Policy.

Invariant 17

Idempotency must be explicitly defined for Actions whose repeated execution could mutate state.

Invariant 18

Action scope must not expand implicitly beyond the resolved Intent.

Invariant 19

Action execution must respect enterprise data boundaries and least privilege.

Invariant 20

Noema must preserve the distinction between an Action and the underlying enterprise API, Tool, or Integration.

Invariant 21

Enterprise Systems remain authoritative for Business State accessed or modified by Actions.

Invariant 22

Noema remains authoritative only for the execution state it owns.

Invariant 23

Action execution should preserve sufficient provenance for audit and reconstruction.

Invariant 24

Model-generated information must not silently become Action input where deterministic enterprise data is required.

Invariant 25

Action selection must be deterministic once the required Intent, Trust, Policy, Context, Target, and contract conditions have been satisfied.

Invariant 26

An enterprise capability does not automatically become a supported Noema Action.

Invariant 27

The Phase 1 Customer Account Inquiry workflow must remain limited to the defined read and support operations.

Invariant 28

A candidate Action proposed by a model is not an executable Action until validated against a defined Action contract.

Invariant 29

Action execution must remain attributable to the originating Principal and relevant technical execution identity.

Invariant 30

Trust must not automatically be treated as permanently valid for every Action in a Workflow.

Invariant 31

Policy may constrain an Action even when the Action contract itself permits the operation.

Invariant 32

Action execution must not rely on stale Context when current enterprise state is required.

Invariant 33

An Action timeout or lost response must not automatically establish enterprise failure.

Invariant 34

Unknown execution state must be reconciled where necessary before repeating a potentially consequential operation.

Invariant 35

Action verification requirements must be explicit where an execution response alone does not establish the required Postcondition.

Invariant 36

Action execution must not silently change the resolved Intent.

Invariant 37

Action composition must preserve authorization, Trust, Policy, data, Resource, and failure boundaries.

Invariant 38

An Action Outcome must remain distinguishable from authoritative enterprise Business State.

Invariant 39

Historical Action execution must remain reconstructable under the Action version and relevant execution context that governed it.

Invariant 40

Action execution must not become a mechanism for privilege escalation, tenant crossing, or authorization bypass.

Invariant 41

Action inputs must contain only the data required for the defined operation.

Invariant 42

Action Preconditions must be evaluated against appropriately current and authoritative information where required.

Invariant 43

Events may support Action Context and verification but do not automatically replace authoritative current-state verification.

Invariant 44

A successful Action does not automatically establish successful Workflow completion.

Invariant 45

A defined enterprise API operation does not become executable merely because the underlying system exposes it.

⸻

88. Final Action Model

An Action is a typed, bounded, policy-constrained executable operation through which Noema invokes a defined enterprise capability to satisfy a resolved Intent.

The fundamental relationship is:

CUSTOMER INTENT
       │
       ▼
INTENT RESOLUTION
       │
       ▼
EXECUTABLE INTENT
       │
       ▼
WORKFLOW
       │
       ▼
WORKFLOW STEP
       │
       ▼
CONTEXT + EVIDENCE
       │
       ▼
TRUST + AUTHORIZATION + POLICY
       │
       ▼
ACTION CONTRACT
       │
       ▼
TYPED INPUTS + TARGET
       │
       ▼
ACTION
       │
       ▼
ENTERPRISE CAPABILITY
       │
       ▼
EXECUTION
       │
       ├──────────────┐
       ▼              ▼
    OUTCOME        EVIDENCE
       │              │
       └───────┬──────┘
               ▼
          VERIFICATION
               │
               ▼
        WORKFLOW TRANSITION

A more complete execution journey is:

Intent
   ↓
Intent Resolution
   ↓
Executable Intent
   ↓
Workflow Planning
   ↓
Candidate Action
   ↓
Action Resolution
   ↓
Contract Validation
   ↓
Target + Input Resolution
   ↓
Trust
   ↓
Authorization
   ↓
Policy
   ↓
Preconditions
   ↓
Action
   ↓
Execution
   ↓
Outcome + Evidence
   ↓
Verification
   │
   ├── Retry
   ├── Reconcile
   ├── Wait
   ├── Clarify
   ├── Escalate
   ├── Compensate
   └── Continue
   ↓
Workflow

The architectural rule is:

Noema does not execute what the model happens to suggest. Noema executes a defined Action whose identity, inputs, target, authority, Preconditions, execution semantics, and Outcome are explicitly bounded by contract, Trust, and Policy.

The Action is the controlled execution boundary between Noema’s semantic execution model and an enterprise capability.

The enterprise remains authoritative for the Business State that the Action accesses or modifies. Noema remains responsible for the execution journey, execution state, evidence, and Workflow coordination that surround that Action.