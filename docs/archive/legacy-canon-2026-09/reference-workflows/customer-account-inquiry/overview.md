> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Customer Account Inquiry

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/overview.md

⸻

1. Definition

Customer Account Inquiry is Noema’s reference workflow for demonstrating how natural-language Customer requests are transformed into bounded, authorized, trustworthy enterprise operations.

The workflow represents Noema’s initial commercial wedge:

Read Operations
+
Support Operations

Specifically:

* balance inquiries
* statement retrieval
* transaction search
* spending summaries
* complaint logging

The workflow does not authorize or execute financial state-changing operations.

Its purpose is to demonstrate the Noema execution model against realistic enterprise systems while keeping the initial operational risk bounded.

The workflow establishes the complete semantic path:

Customer Request
       ↓
Intent
       ↓
Context
       ↓
Evidence
       ↓
Trust
       ↓
Policy / Authorization
       ↓
Action
       ↓
Execution
       ↓
Evidence
       ↓
Outcome
       ↓
Customer Response

Noema owns the orchestration of this journey.

Enterprise systems remain authoritative for the underlying enterprise Business State.

⸻

2. Purpose

The purpose of this reference workflow is to provide a concrete implementation model for Noema’s core architecture.

It demonstrates how Noema transforms:

Natural Language
       ↓
Intent Resolution
       ↓
Intent
       ↓
Context Assembly
       ↓
Evidence
       ↓
Trust
       ↓
Policy / Authorization
       ↓
Action Selection
       ↓
Execution
       ↓
Enterprise System
       ↓
Verification
       ↓
Outcome
       ↓
Response

The workflow is intentionally narrow.

It proves that Noema can allow Customers to interact with enterprise capabilities without requiring them to understand the underlying application structure.

The workflow also demonstrates that:

* interpretation is distinct from authorization
* Intent is distinct from Action
* Action is distinct from Execution
* Execution State is distinct from Outcome
* Outcome is distinct from enterprise Business State
* model confidence is not authorization
* successful transport does not automatically establish successful Business Outcome
* ambiguity must remain explicit when it cannot be deterministically resolved
* enterprise systems remain authoritative for the state Noema reasons over

⸻

3. Commercial Context

Noema’s initial commercial value proposition is not the abstract concept of Intent Computing.

The initial value is:

* reduce customer support calls
* reduce onboarding friction
* increase task completion
* allow Customers to complete common tasks
* allow Customers to interact with enterprise capabilities without learning the application

Customer Account Inquiry provides a concrete environment in which this value can be demonstrated.

A Customer can express an objective naturally:

"What's my balance?"
"Show me my statement."
"Find the transaction where I spent $200."
"How much did I spend on restaurants last month?"
"I want to report a problem with this transaction."

Noema converts these requests into structured, bounded enterprise operations.

⸻

4. Scope

The reference workflow covers:

* Balance Inquiry
* Statement Retrieval
* Transaction Search
* Spending Summary
* Complaint Logging

The workflow includes the supporting activities required to perform these operations safely:

* Intent resolution
* identity resolution
* resource resolution
* context acquisition
* evidence acquisition
* authorization
* policy evaluation
* trust evaluation
* action selection
* enterprise integration
* precondition evaluation
* execution coordination
* postcondition evaluation
* result validation
* outcome determination
* response generation
* audit recording

⸻

5. Explicit Non-Goals

The reference workflow does not initially cover:

* money transfers
* payments
* withdrawals
* financial state mutation
* card replacement
* card renewal
* account closure
* credit limit changes
* beneficiary creation
* other high-risk financial writes

These may become future workflows as Noema expands beyond the initial read/support wedge.

They should not be implicitly introduced into this reference workflow.

⸻

6. Reference Workflow Principle

The workflow exists to prove a broader architectural principle:

Natural-language interaction can be converted into deterministic enterprise execution without requiring the Customer to understand the underlying application.

The Customer expresses:

What they want

Noema determines:

What that means
What information is required
What Principal is represented
What Resource is being referenced
Whether the request is sufficiently grounded
Whether required authorization exists
Whether Policy permits the operation
Which Action is appropriate
Which enterprise system owns the relevant state
Whether execution completed
Whether the expected postconditions were established
What Outcome can be established

Noema must not substitute probabilistic interpretation for deterministic governance at the execution boundary.

⸻

7. Primary Actors

The reference workflow involves several actors.

Customer
    ↓
Noema
    ↓
Enterprise Systems

Supporting actors and systems may include:

* Identity System
* Policy System
* Account System
* Ledger
* Transaction System
* Statement System
* Support / Case Management System
* Human Support Agent

Noema does not replace these enterprise systems.

It orchestrates access to their capabilities through defined interfaces and bounded Actions.

⸻

8. Customer

The Customer is the Principal initiating the Intent.

Examples:

"What's my current balance?"
"Show my August statement."
"Find my last transaction."
"How much did I spend last month?"
"I want to report this transaction."

The Customer’s natural-language request is the starting point of the workflow.

The request itself does not automatically establish:

* identity
* authorization
* Resource
* Intent certainty
* enterprise Business State
* execution authority

These must be established through the Noema pipeline.

⸻

9. Noema

Noema acts as the Intent-to-Execution layer.

Its responsibilities include:

* Intent interpretation
* Intent normalization
* Intent resolution
* identity resolution
* Resource resolution
* Context assembly
* Evidence evaluation
* ambiguity handling
* Trust evaluation
* Policy evaluation
* authorization evaluation
* Action selection
* precondition evaluation
* execution coordination
* postcondition evaluation
* Outcome determination
* verification
* auditability

Noema does not become the System of Record for the enterprise Business State being queried or acted upon.

Noema owns the workflow state necessary to coordinate the operation.

⸻

10. Enterprise Systems

Enterprise systems remain authoritative for their respective domains.

For example:

Account System
    → account state
Ledger
    → balance
Transaction System
    → transaction state
Statement System
    → statements
Support System
    → complaints / cases

Noema consumes these systems through defined integrations.

The enterprise remains the authority for Business State.

Noema may maintain observations, Outcomes, execution records, and derived workflow state without becoming a competing System of Record.

⸻

11. Core Workflow

The reference workflow follows:

Customer Request
       │
       ▼
Intent Resolution
       │
       ▼
Intent
       │
       ▼
Context Assembly
       │
       ▼
Evidence
       │
       ▼
Trust / Policy / Authorization
       │
       ├── Clarify
       ├── Escalate
       ├── Reject
       └── Proceed
                │
                ▼
              Action
                │
                ▼
          Preconditions
                │
                ▼
            Execution
                │
                ▼
       Enterprise System
                │
                ▼
          Result / State
                │
                ▼
         Postconditions
                │
                ▼
          Verification
                │
                ▼
             Outcome
                │
                ▼
       Customer Response

The execution path must not bypass Trust, Policy, Authorization, or required verification merely because the requested operation is read-only.

⸻

12. Intent

Intent represents the structured representation of the outcome the Customer is trying to achieve.

Examples:

"What's my balance?"
    ↓
get_account_balance
"Show me my statement."
    ↓
retrieve_statement
"Find my Netflix payment."
    ↓
search_transactions
"How much did I spend last month?"
    ↓
get_spending_summary
"I want to report this transaction."
    ↓
create_complaint

Intent represents the Customer’s objective.

It does not represent the implementation used to satisfy that objective.

Therefore:

Intent
   ≠
Action

⸻

13. Intent Resolution

Intent Resolution converts the Customer’s request into a structured Intent.

Conceptually:

Natural Language
       ↓
Intent Resolution
       ↓
Structured Intent

Example:

Customer:
"How much did I spend last month?"
Intent:
type = get_spending_summary
objective = obtain total spending for requested period
parameters:
    period = previous calendar month

The model may assist with interpretation.

However, model-generated Intent is not automatically trusted.

The resulting Intent must be normalized, grounded, and evaluated through the applicable Context, Evidence, Trust, Policy, and Authorization mechanisms before it becomes executable.

⸻

14. Intent Structure

Conceptually:

Intent {
    intent_id
    type
    objective
    principal
    target
    parameters
    constraints
    scope
    status
    source
    created_at
    updated_at
    provenance
}

This is a semantic model rather than a requirement for a literal database schema.

Intent may preserve:

* Customer objective
* Principal reference
* Resource reference
* parameters
* constraints
* scope
* lifecycle state
* provenance

⸻

15. Intent and Context

Intent describes what the Customer wants.

Context provides the bounded information required to understand and execute that request.

Depending on the request, Context may include:

* Principal
* eligible Accounts
* target Resource
* transaction information
* statement period
* date range
* currency
* permissions
* relevant enterprise state
* Policy
* Evidence
* execution history

Conceptually:

Intent
   +
Context
   ↓
Executable Action Candidate

Context must remain bounded to the requirements of the current workflow.

Noema should not copy unrelated Customer information into Context merely because that information is available.

⸻

16. Evidence

Evidence supports decisions made during the workflow.

Examples include:

* authenticated identity information
* enterprise Resource records
* authorization information
* Policy decisions
* enterprise responses
* transaction records
* statement records
* verification responses
* enterprise events

Evidence does not itself become Intent, Action, or Outcome.

The relationship is:

Claim / Decision
      ↓
Evidence
      ↓
Source

Evidence should be traceable to its source where required.

⸻

17. Ambiguity

The workflow explicitly treats ambiguity as a state.

Example:

Customer:
"Show my transactions."
Context:
Account A
Account B
Account C

If Noema cannot deterministically determine which Account the Customer means:

AMBIGUOUS
     ↓
CLARIFICATION

Noema should not select an Account merely because one appears statistically more likely.

The principle is:

Ambiguity is a state, not an invitation to guess.

This applies both to Intent and to Resource resolution.

⸻

18. Identity and Resource Resolution

Natural-language references frequently require resolution.

Examples:

my account
my card
my transactions
John's account
the account I used yesterday

Intent captures the semantic reference.

Identity Resolution determines the enterprise Principal.

Resource Resolution determines the enterprise Resource.

These remain distinct operations.

Conceptually:

"my transactions"
       ↓
Principal Resolution
       ↓
Eligible Resources
       ↓
Resource Resolution
       ↓
Target

Noema must not invent Resource identifiers.

If materially ambiguous candidates remain and no deterministic Policy rule resolves them:

CLARIFY

⸻

19. Context Resolution and Defaulting

Missing information does not always require clarification.

For example:

"Show me my transactions."

If the Customer has a single eligible Account and Policy permits deterministic defaulting, the Account may be resolved automatically.

However:

"Show me my statement."

may require a statement period if the enterprise capability requires one.

Noema must distinguish:

missing but safely defaultable

from:

missing and materially ambiguous

Only the former may be defaulted, and only where Policy provides a deterministic basis.

⸻

20. Temporal Resolution

Natural-language temporal expressions must be preserved semantically before normalization.

Examples:

* yesterday
* this week
* last month
* June
* the past three months

Conceptually:

"last month"
       ↓
Temporal Resolution
       ↓
{
    start
    end
    timezone
}

The applicable timezone and current date must be used.

Downstream systems must not independently reinterpret the original temporal expression.

⸻

21. Trust

Trust determines whether Noema has sufficient grounds to proceed.

Trust may evaluate:

* identity
* authorization
* Policy
* Evidence
* data authority
* freshness
* ambiguity
* Action risk
* validation requirements
* enterprise state

The workflow decision must be explicit:

EXECUTE
CLARIFY
ESCALATE
REJECT

The system must not produce:

probably execute

as an execution state.

Model confidence may contribute to Trust but does not constitute Trust or authorization.

Therefore:

high model confidence
        ≠
authorization

⸻

22. Authorization

Read access remains authorization-sensitive.

For example:

Customer A
    ↓
Account A
    ↓
Transactions

does not imply:

Customer A
    ↓
Account B

Noema must establish that the Principal is authorized to access the requested Resource.

Read-only does not mean permission-free.

Authorization remains distinct from Intent and Trust.

⸻

23. Policy

Policy determines what Noema is permitted to do with a given Intent, Context, Action, and Outcome.

Policy may determine:

* whether an operation is permitted
* whether a Resource may be accessed
* whether defaulting is allowed
* whether stronger verification is required
* whether an Outcome is sufficiently fresh
* whether reconciliation is required
* whether retry is permitted
* whether human intervention is required

Intent does not establish permission.

Trust does not replace Policy.

⸻

24. Action Mapping

Resolved Intents map to bounded Actions.

Conceptually:

Intent
   ↓
Action Selection
   ↓
Action

Examples:

get_account_balance
    → retrieve_balance
retrieve_statement
    → retrieve_statement
search_transactions
    → search_transactions
get_spending_summary
    → calculate_spending_summary
create_complaint
    → create_complaint

The exact Action vocabulary must remain explicit and supported.

Noema must not invent an Action merely because an Intent appears superficially similar to an available capability.

Each Action is governed by an Action Contract.

⸻

25. Action Contracts

Actions are executable capabilities, not merely labels.

An Action Contract should establish the requirements necessary to execute the Action safely.

Depending on the Action, these may include:

* required Intent type
* required Principal
* required Resource
* required parameters
* preconditions
* authorization requirements
* Policy requirements
* required Evidence
* enterprise integration
* expected postconditions
* verification requirements
* failure semantics
* idempotency requirements where applicable
* data boundaries

The Action Contract defines how an executable capability may be invoked.

Intent remains the Customer’s requested objective.

⸻

26. Read Operations

The first four operations are primarily information retrieval:

retrieve_balance
retrieve_statement
search_transactions
calculate_spending_summary

These operations read enterprise state without changing the underlying financial state.

They still require:

* identity
* Resource resolution
* authorization
* appropriate data authority
* appropriate freshness
* Policy evaluation
* Trust evaluation
* validation

A read operation may therefore be blocked, clarified, escalated, or rejected even though it does not mutate enterprise state.

⸻

27. Complaint Logging

Complaint Logging is included because Customer support interactions are an important part of the initial commercial wedge.

A request such as:

"I don't recognize this transaction."

may resolve into:

Intent:
create_complaint

The resulting Action may create a support case.

Although this changes support-system state, it does not directly mutate financial state.

Its execution therefore remains within the bounded Phase 1 scope.

Complaint creation is nevertheless a state-changing Action within the support domain and must therefore have explicit execution, postcondition, verification, and Outcome semantics.

⸻

28. Preconditions

Before an Action executes, required preconditions must be established.

Examples:

retrieve_balance
    → Principal resolved
    → Account resolved
    → authorization established
retrieve_statement
    → Principal resolved
    → Account resolved
    → statement period resolved
    → authorization established
create_complaint
    → Principal resolved
    → related transaction resolved where required
    → support authorization established

Preconditions must be explicit rather than hidden inside model reasoning.

Failure to satisfy a required precondition prevents execution.

⸻

29. Enterprise Boundary

The workflow preserves the boundary:

Noema
    │
    ├── owns Intent State
    ├── owns Context required for orchestration
    ├── owns Trust State
    ├── owns Action State
    ├── owns Execution State
    ├── owns Outcome records
    └── owns workflow provenance
Enterprise
    │
    ├── owns Account State
    ├── owns Balance
    ├── owns Transaction State
    ├── owns Statement State
    └── owns Support Case State

Noema coordinates.

Enterprise systems remain authoritative for enterprise Business State.

An Outcome observed by Noema does not become a competing canonical enterprise state.

⸻

30. Read vs Write Boundary

The distinction between read and write operations is explicit.

Phase 1
────────
Read / Support
Phase 2
────────
Financial Writes
Later
──────
Cross-Enterprise Orchestration

The reference workflow represents Phase 1.

It should not be interpreted as a complete representation of Noema’s eventual execution surface.

Financial write operations must be introduced through separately defined workflows with their own Action Contracts and stronger Trust requirements.

⸻

31. Execution

Execution describes the process of attempting an Action.

It is distinct from Outcome.

For example:

Action:
get_account_balance
Execution:
completed
Outcome:
balance = ₦250,000

Execution State may include states such as:

PENDING
RUNNING
SUCCEEDED
FAILED
TIMEOUT
UNKNOWN
CANCELLED

The exact Execution State vocabulary is governed by the canonical Execution model.

Execution State must not be conflated with Outcome.

For example:

Execution:
SUCCEEDED
Outcome:
NO_RESULT

is valid for a search operation.

Likewise:

Execution:
TIMEOUT
Outcome:
UNKNOWN

may be valid where the resulting enterprise state cannot be established.

⸻

32. Verification and Postconditions

Noema should validate that the Action produced the expected result.

For read operations this may involve:

* response received
* schema valid
* Resource matches request
* Principal matches
* data within requested scope
* required result fields present
* freshness requirements satisfied

For complaint logging:

* Case created
* Case identifier returned
* Case associated with correct Principal
* Case associated with correct Resource where applicable

Verification must establish the relevant postconditions.

A successful HTTP response alone does not necessarily establish successful Business Outcome.

⸻

33. Outcome

Every completed Action must result in an explicit Outcome representation describing what execution established relative to the Intent.

Possible Outcome statuses include:

SUCCESS
PARTIAL
NO_RESULT
FAILED
UNKNOWN

These statuses remain semantically distinct.

SUCCESS

The requested objective was satisfied and the expected result was established.

PARTIAL

Only part of a Compound Intent was satisfied.

NO_RESULT

Execution succeeded, but no matching result was established.

FAILED

The requested objective was not achieved and failure is established.

UNKNOWN

Noema cannot establish whether the requested objective was achieved.

The Outcome must be grounded in execution evidence.

⸻

34. Outcome vs Execution

The distinction is explicit:

Execution
    ↓
Did the execution process complete?
Outcome
    ↓
What did the execution establish relative to the Intent?

For example:

search_transactions
       ↓
Execution = SUCCESS
       ↓
No matching transaction
       ↓
Outcome = NO_RESULT

This is different from:

search_transactions
       ↓
Transaction System unavailable
       ↓
Outcome = FAILED

And different again from:

request sent
       ↓
timeout
       ↓
enterprise state unverified
       ↓
Outcome = UNKNOWN

⸻

35. Outcome vs Enterprise State

Enterprise Business State remains owned by the authoritative enterprise system.

For example:

Enterprise:
Account.balance = ₦250,000

Noema may record:

Outcome:
balance retrieved = ₦250,000

The Outcome is an observation/result of execution.

It does not become the canonical Account balance.

An Outcome may become stale without becoming incorrect as a historical observation.

⸻

36. Outcome Evidence

Outcomes must be grounded in Evidence.

Evidence may include:

* enterprise response
* Resource identifier
* returned data
* query result
* verification response
* enterprise event
* postcondition verification

Conceptually:

Execution
    ↓
Evidence
    ↓
Outcome

Noema must not manufacture an Outcome merely to satisfy the Customer’s Intent.

⸻

37. Outcome Freshness

An Outcome may become stale.

Example:

10:00
balance = ₦500,000
10:10
new transaction occurs
10:15
previous Outcome still says ₦500,000

The previous Outcome remains a record of what was observed at 10:00.

It should not automatically be treated as current enterprise Business State.

Where Policy requires current state, Noema must obtain sufficiently fresh evidence.

⸻

38. Outcome Communication

Customer-facing responses should be generated from the verified Outcome.

Example:

Outcome:
SUCCESS
balance = ₦250,000

Customer response:

Your current balance is ₦250,000.

If:

Outcome:
NO_RESULT

the response should communicate that no matching result was found.

If:

Outcome:
FAILED

the response should communicate that the requested operation was not completed.

If:

Outcome:
UNKNOWN

the response must communicate that the result could not yet be confirmed.

Noema must not convert uncertainty into success or failure without sufficient evidence.

⸻

39. Compound Intents

A single Customer message may contain multiple objectives.

Example:

"Show my balance, find my Netflix payment,
and tell me how much I spent last month."

Noema should preserve the constituent Intent components:

Compound Intent
   ├── get_account_balance
   ├── search_transactions
   └── get_spending_summary

Each Action retains its own lifecycle.

Each Action retains its own Execution State and Outcome.

⸻

40. Aggregate Outcomes

A Compound Intent may produce an aggregate Outcome.

Example:

get_account_balance
    → SUCCESS
search_transactions
    → SUCCESS
get_spending_summary
    → FAILED

Overall:

PARTIAL

The aggregate Outcome must not erase the underlying Action Outcomes.

The individual Outcomes remain necessary for:

* customer communication
* auditability
* recovery
* reconciliation
* analytics
* execution reconstruction

⸻

41. Outcome Completeness

An Outcome may be technically successful but incomplete relative to the Customer’s requested scope.

Example:

Intent:
"Show all my transactions for July."
Result:
first 50 transactions

If the enterprise capability returned a paginated result and Noema has not retrieved all required pages, the Outcome may not yet satisfy the Intent.

Completeness must therefore be explicit where relevant.

For collection-based Actions, Noema must determine whether the Customer requested:

* first page
* all results
* a bounded result set

before treating the Outcome as complete.

⸻

42. Pagination

For collection-based Actions such as:

search_transactions

the Outcome may include:

items
page
page_size
has_more
continuation

Pagination state must remain associated with the Action and Outcome.

Noema must not claim that a complete requested collection was returned when the required result remains incomplete.

⸻

43. Failure Handling

Failures are explicit workflow states.

Examples:

* Identity unavailable
* Account unavailable
* Enterprise system unavailable
* Policy unavailable
* Data unavailable
* Authorization failure
* Timeout
* Malformed response
* Conflicting data
* Verification failure

Noema determines whether to:

* retry
* reconcile
* clarify
* escalate
* reject
* terminate

according to the relevant Policy and Action Contract.

A Failure explains why an Outcome was unsuccessful.

The Outcome and Failure remain separate semantic layers.

⸻

44. Unknown and Reconciliation

Unknown represents insufficient evidence to establish the result.

Example:

create_complaint
      ↓
request sent
      ↓
timeout
      ↓
Outcome = UNKNOWN

Noema must not immediately assume either success or failure.

For state-changing Actions, Noema should reconcile against the authoritative enterprise system before retrying or claiming success where Policy requires this.

Example:

create_complaint
      ↓
UNKNOWN
      ↓
query Complaint System
      ↓
case_id = CASE-123
      ↓
SUCCESS

The original uncertainty remains auditable.

⸻

45. Idempotency

For state-changing Actions, Unknown Outcomes must be handled with appropriate idempotency semantics.

Example:

create_complaint
      ↓
UNKNOWN
      ↓
check existing request
      ↓
Case found
      ↓
SUCCESS

Noema should not create duplicate enterprise state merely because the first Outcome was uncertain.

The applicable Action Contract and Policy determine whether reconciliation, retry, or another recovery strategy is permitted.

⸻

46. Human Intervention

Human intervention may occur when automated execution cannot safely continue.

Examples:

* identity ambiguity
* enterprise data conflict
* unsupported complaint condition
* Policy exception
* system inconsistency
* unresolved Unknown Outcome

Human intervention is not an uncontrolled escape hatch.

It is an explicit workflow/execution state with its own audit trail.

An original Unknown Outcome remains part of the execution history even if subsequent human intervention establishes the final result.

⸻

47. Customer Corrections

A Customer may correct a previously expressed Intent.

Example:

Customer:
"Show my transactions."
Noema:
"Which account?"
Customer:
"My savings account."

The newly supplied information should update the relevant Intent and Context.

Conceptually:

Original Intent
      ↓
Clarification
      ↓
Updated Intent
      ↓
Resolution

The correction must not silently become an unrelated objective.

⸻

48. Cancellation

A Customer may cancel before execution.

Example:

Customer:
"Show my statement."
Customer:
"Never mind."

The relevant Intent may transition to:

CANCELLED

No execution should occur after cancellation where cancellation occurs before the execution boundary, unless a separate valid request is subsequently received.

⸻

49. Replanning

If Context or enterprise state changes before execution, Noema may need to re-evaluate the executable representation.

Example:

Account becomes unavailable
        ↓
Original plan no longer valid
        ↓
Re-evaluate

Replanning may change:

* Action sequence
* Resource resolution
* execution strategy
* enterprise integration path

It must not silently change the Customer’s requested objective.

Therefore:

Intent
   remains stable
       ↓
Plan
   may change

⸻

50. Enterprise Events

Enterprise events may affect whether an Intent remains executable.

Example:

Intent:
retrieve_statement
Enterprise Event:
account_closed

The Intent remains what the Customer requested.

Its execution feasibility may change.

Conceptually:

Intent
   ↓
Updated Context
   ↓
Trust / Policy
   ↓
Re-evaluate

Enterprise events do not redefine the Customer’s original objective.

⸻

51. Auditability

A reference execution should preserve enough information to reconstruct:

* Principal
* Intent
* Context
* Evidence
* Policy
* Authorization
* Trust Decision
* Action
* Action version
* Preconditions
* Enterprise Request
* Enterprise Response
* Postconditions
* Verification
* Outcome
* timestamps
* provenance

Sensitive enterprise information remains subject to applicable Data Boundaries, privacy, access-control, minimization, and retention requirements.

⸻

52. Provenance

Consequential workflow state should be traceable to its source.

For Intent, useful metadata may include:

intent_id
source
created_at
normalized_at
resolver
model_reference
confidence
resolution_evidence

For Outcome, useful metadata may include:

outcome_id
execution_id
action_id
action_version
source
produced_at
observed_at
verified_at
evidence
provenance

Model-specific metadata must not replace the semantic object itself.

⸻

53. Versioning

Intent, Action, and Outcome representations may evolve.

Historical records must remain interpretable according to the semantic representation under which they were created.

For example:

intent_version = 1
outcome_version = 1
action_version = 1

Schema changes must not silently reinterpret historical executions.

Action versions are particularly important because an historical Outcome must remain interpretable in relation to the Action Contract that produced it.

⸻

54. Data Boundaries and Privacy

Intent, Context, Evidence, Execution records, and Outcomes must respect Noema’s Data Boundaries.

The workflow should apply appropriate:

* minimization
* purpose limitation
* access control
* redaction
* retention
* provenance

The complete Customer profile should not be copied into Intent or Context merely because it is available.

For example:

Intent:
search_transactions

does not require unrelated:

home_address
date_of_birth

unless explicitly required by the workflow.

⸻

55. Canonical Data

The workflow relies on enterprise systems as authoritative sources.

For example:

Balance
    ↓
Ledger
Transaction
    ↓
Transaction System
Statement
    ↓
Statement System
Complaint
    ↓
Support System

Noema may use:

* caches
* projections
* events
* derived data

where Policy permits.

However, these must not silently override canonical enterprise data.

Derived information must remain distinguishable from canonical enterprise facts.

For example, a spending category calculated by Noema is a derived interpretation of transaction data and must not automatically be represented as canonical enterprise classification.

⸻

56. Example: Balance Inquiry

Customer:

"What's my balance?"

Resolution:

Intent:
get_account_balance

Context:

Principal
Account
Authorization

Action:

retrieve_balance

Enterprise:

Ledger

Execution:

Enterprise request
        ↓
Ledger response

Verification:

Principal matches
Account matches
Response valid
Balance current enough for Policy

Outcome:

SUCCESS
balance = ₦250,000
currency = NGN

The Ledger remains authoritative for the balance.

⸻

57. Example: Transaction Search

Customer:

"Find the transaction where I spent $120 at Amazon last month."

Resolution:

Intent:
search_transactions
Parameters:
amount = $120
merchant = Amazon
period = previous month

Context:

Principal
Account
Transaction access
Date range

Action:

search_transactions

The result is validated against the requested constraints before being returned.

If no matching transaction is established:

Outcome:
NO_RESULT

If the transaction system cannot complete the search:

Outcome:
FAILED

If execution times out and the result cannot be established:

Outcome:
UNKNOWN

⸻

58. Example: Spending Summary

Customer:

"How much did I spend on restaurants last month?"

Resolution:

Intent:
get_spending_summary
Parameters:
category = restaurants
period = previous month

Noema determines the relevant enterprise data and applies the appropriate aggregation semantics.

The result should preserve the distinction between:

canonical transaction data

and:

derived spending classification

The derived classification must not be presented as canonical enterprise truth merely because Noema calculated it.

A successful Outcome should establish the requested aggregation and its applicable period.

⸻

59. Example: Statement Retrieval

Customer:

"Show me my August statement."

Noema resolves:

Principal
Statement Period
Relevant Account

If the Customer has multiple eligible Accounts:

AMBIGUOUS
     ↓
CLARIFICATION

Once resolved:

retrieve_statement
        ↓
Statement System
        ↓
Statement
        ↓
Verification
        ↓
Outcome
        ↓
Customer

If the Statement System establishes that no statement exists:

NO_RESULT

If the Statement System is unavailable:

FAILED

If the request times out and the existence or retrieval state cannot be established:

UNKNOWN

⸻

60. Example: Complaint Logging

Customer:

"I don't recognize this transaction."

Noema may resolve:

Intent:
create_complaint

Context may include:

Principal
Transaction
Account
Transaction details
Support permissions

Action:

create_complaint

Expected postcondition:

Case exists

Successful verification:

Case created
Case identifier returned
Case associated with correct Principal
Case associated with correct Resource where applicable

Outcome:

SUCCESS
case_id = CASE-123
status = OPEN

The financial transaction itself is not modified by this workflow.

⸻

61. Reference Workflow Boundaries

The workflow begins when:

Customer Request

enters Noema.

It reaches its terminal workflow result when:

Outcome

has been established and the applicable Customer communication or escalation path has been determined.

It does not own:

* Customer database
* Ledger
* transaction database
* statement store
* support database
* enterprise identity system

It does not redefine their authority.

Noema owns the orchestration state necessary to move from Intent to verified Outcome.

⸻

62. Relationship to the Canon

This workflow is an implementation reference for concepts defined elsewhere in the Canon.

It depends on:

* Intent
* Context
* Trust
* Authorization
* Policy
* Evidence
* Action
* Action Contract
* Preconditions
* Postconditions
* Execution
* Outcome
* Failure
* Auditability
* Enterprise Boundaries
* Canonical Data
* Identity Resolution
* Resource Resolution

It must not redefine those concepts.

Where this workflow requires a concept, the corresponding canonical definition takes precedence.

⸻

63. Reference Workflow Architecture

The complete reference architecture is:

                         CUSTOMER
                            │
                            ▼
                      NATURAL LANGUAGE
                            │
                            ▼
                          INTENT
                            │
                            ▼
                    INTENT RESOLUTION
                            │
                            ▼
                         CONTEXT
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
        AUTHORIZATION     POLICY        EVIDENCE
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                          TRUST
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           CLARIFY       ESCALATE       REJECT
                            │
                            ▼
                         ACTION
                            │
                            ▼
                     PRECONDITIONS
                            │
                            ▼
                       EXECUTION
                            │
                            ▼
                    ENTERPRISE SYSTEM
                            │
                            ▼
                          RESULT
                            │
                            ▼
                    POSTCONDITIONS
                            │
                            ▼
                       VERIFICATION
                            │
                            ▼
                         OUTCOME
                            │
                            ▼
                         CUSTOMER

The critical architectural distinction is:

Intent
    = what the Customer wants
Action
    = what capability Noema invokes
Execution
    = the attempt to invoke that capability
Outcome
    = what execution established
Enterprise State
    = the authoritative state owned by the enterprise

⸻

64. Reference Workflow Invariants

Invariant 1

The workflow is limited to Noema’s initial read/support commercial wedge.

Invariant 2

Card renewal is not part of this reference workflow.

Invariant 3

Financial state-changing operations are outside the Phase 1 reference workflow.

Invariant 4

Read operations still require appropriate Identity, Resource Resolution, Authorization, Trust, and Policy evaluation.

Invariant 5

Noema does not become the System of Record for enterprise Business State.

Invariant 6

Enterprise Systems remain authoritative for their respective domains.

Invariant 7

Natural-language interpretation does not by itself authorize execution.

Invariant 8

Ambiguity must be represented explicitly when it remains material.

Invariant 9

Noema must not resolve consequential ambiguity through probabilistic guessing.

Invariant 10

Every executable Intent must resolve to a bounded Action.

Invariant 11

Actions must operate within defined enterprise authority and Data Boundaries.

Invariant 12

Enterprise data used for consequential decisions must satisfy the required authority and freshness guarantees.

Invariant 13

Model-generated interpretations must remain distinguishable from canonical enterprise facts.

Invariant 14

Model confidence does not constitute authorization.

Invariant 15

Identity and Resource references must be grounded before consequential execution.

Invariant 16

Missing information may only be defaulted when Policy provides a deterministic basis for doing so.

Invariant 17

Intent parameters, temporal requirements, constraints, and scope must survive normalization and planning without semantic distortion.

Invariant 18

Intent must remain distinct from Action.

Invariant 19

Action must remain distinct from Execution.

Invariant 20

Execution State must remain distinct from Outcome.

Invariant 21

Outcome must be grounded in execution evidence.

Invariant 22

Successful transport does not automatically establish successful Business Outcome.

Invariant 23

A successful Action may still produce NO_RESULT.

Invariant 24

NO_RESULT must remain distinct from FAILED.

Invariant 25

UNKNOWN must remain distinct from FAILED.

Invariant 26

Unknown must not be converted into success or failure without sufficient evidence.

Invariant 27

Execution failure must not rewrite the Customer’s original Intent.

Invariant 28

Compound Intents must preserve their constituent objectives and relationships.

Invariant 29

Each Action derived from a Compound Intent must maintain its own Execution State and Outcome.

Invariant 30

Aggregate Outcomes must not erase constituent Action Outcomes.

Invariant 31

Outcome completeness must be explicit where the requested result may be partial or paginated.

Invariant 32

Execution success requires the verification required by the relevant Action Contract and Policy.

Invariant 33

Postconditions must contribute to Outcome determination where required.

Invariant 34

Outcome must preserve sufficient provenance to establish its source.

Invariant 35

Outcome temporal information must be preserved where relevant.

Invariant 36

Outcome must not become competing canonical enterprise Business State.

Invariant 37

Enterprise Systems remain authoritative for the enterprise state represented by an Outcome.

Invariant 38

Outcome freshness must be distinguished from enterprise authority.

Invariant 39

Customer-facing responses must reflect the verified Outcome.

Invariant 40

The model may interpret or explain workflow state but must not fabricate Intent, Evidence, Outcome, or enterprise facts.

Invariant 41

State-changing Actions with Unknown Outcomes must consider reconciliation and idempotency before retry.

Invariant 42

Human intervention must be an explicit and auditable workflow state.

Invariant 43

Customer corrections must update the relevant Intent rather than silently creating a different objective.

Invariant 44

Customer cancellation must prevent execution where cancellation occurs before the execution boundary.

Invariant 45

Replanning may change execution strategy but must not silently change the requested objective.

Invariant 46

Enterprise events may change Intent executability but do not redefine the Customer’s original objective.

Invariant 47

Intent, Context, Evidence, Execution, and Outcome data must respect Data Boundaries and privacy requirements.

Invariant 48

Intent persistence must retain sufficient provenance for reconstruction where required.

Invariant 49

Historical Intent, Action, Execution, and Outcome records must remain interpretable according to the semantic versions under which they were created.

Invariant 50

Complaint Logging may create support-system state while remaining within the Phase 1 boundary because it does not directly mutate financial state.

Invariant 51

Future financial write operations must be introduced through separately defined workflows and stronger Trust requirements.

Invariant 52

Noema must never manufacture an Outcome merely to satisfy the Customer’s requested Intent.

Invariant 53

Ambiguity is a state that must be resolved or preserved—not an invitation to guess.

⸻

65. Final Definition

Customer Account Inquiry is Noema’s reference workflow for converting natural-language Customer requests into bounded, authorized, trustworthy read and support operations against enterprise systems.

It demonstrates the initial commercial wedge:

balance inquiries
statement retrieval
transaction search
spending summaries
complaint logging

through the Noema execution model:

NATURAL LANGUAGE
       ↓
INTENT
       ↓
CONTEXT
       ↓
EVIDENCE
       ↓
TRUST
       ↓
POLICY / AUTHORIZATION
       ↓
ACTION
       ↓
EXECUTION
       ↓
ENTERPRISE SYSTEM
       ↓
VERIFICATION
       ↓
OUTCOME
       ↓
CUSTOMER RESPONSE

The fundamental architectural rule is:

Noema owns the journey from Customer Intent to verified Outcome; the enterprise remains the authority for the Business State Noema reasons over.

The workflow therefore preserves the central separation:

Intent
    ↓
what the Customer wants
Action
    ↓
the bounded capability selected to satisfy it
Execution
    ↓
the attempt to invoke that capability
Outcome
    ↓
what the execution established
Enterprise Business State
    ↓
the authoritative state owned by the enterprise

Noema may use probabilistic models to interpret natural language, but model interpretation does not itself establish identity, authorization, Resource resolution, Policy permission, execution success, or Business Outcome.

Those determinations must be grounded through the applicable Context, Evidence, Trust, Policy, Action Contract, Execution, and verification mechanisms.