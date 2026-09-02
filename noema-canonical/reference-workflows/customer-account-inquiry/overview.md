Customer Account Inquiry

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/overview.md

⸻

1. Definition

Customer Account Inquiry is Noema’s reference workflow for demonstrating how natural-language customer requests are resolved into bounded, authorized, trustworthy enterprise read and support operations.

The workflow represents the initial Noema commercial wedge:

Read Operations
+
Support Operations

Specifically:

balance inquiries
statement retrieval
transaction search
spending summaries
complaint logging

The workflow does not authorize or execute financial state-changing operations.

Its purpose is to demonstrate the core Noema execution model against realistic enterprise systems while keeping the initial operational risk bounded.

⸻

2. Purpose

The purpose of this reference workflow is to provide a concrete implementation model for Noema’s core architecture.

It demonstrates how Noema transforms:

Natural Language
       ↓
Intent
       ↓
Intent Resolution
       ↓
Context
       ↓
Trust
       ↓
Action
       ↓
Enterprise System
       ↓
Verification
       ↓
Response

The workflow is intentionally narrow.

It proves that Noema can allow customers to interact with enterprise capabilities without requiring them to understand the underlying application structure.

⸻

3. Commercial Context

Noema’s initial commercial value proposition is not the abstract concept of Intent Computing.

The initial value is:

reduce customer support calls
reduce onboarding friction
increase task completion
allow customers to complete common tasks
without learning the application

Customer Account Inquiry provides a concrete environment in which this value can be demonstrated.

A customer can express an objective naturally:

"What's my balance?"
"Show me my statement."
"Find the transaction where I spent $200."
"How much did I spend on restaurants last month?"
"I want to report a problem with this transaction."

Noema converts these requests into structured enterprise operations.

⸻

4. Scope

The reference workflow covers:

Balance Inquiry
Statement Retrieval
Transaction Search
Spending Summary
Complaint Logging

The workflow includes the supporting activities required to perform these operations safely:

identity resolution
resource resolution
context acquisition
authorization
policy evaluation
trust evaluation
action selection
enterprise integration
result validation
response generation
audit recording

⸻

5. Explicit Non-Goals

The reference workflow does not initially cover:

money transfers
payments
withdrawals
financial state mutation
card replacement
card renewal
account closure
credit limit changes
beneficiary creation
other high-risk financial writes

These may become future workflows as Noema expands beyond the initial read/support wedge.

They should not be implicitly introduced into this reference workflow.

⸻

6. Reference Workflow Principle

The workflow exists to prove a broader architectural principle:

Natural-language interaction can be converted into deterministic enterprise execution without requiring the user to understand the underlying application.

The user expresses:

What they want

Noema determines:

What that means
What information is required
Whether the request is sufficiently grounded
Whether the Principal is authorized
Which Action is appropriate
Which enterprise system owns the relevant state
Whether the result satisfies the expected Outcome

⸻

7. Primary Actors

The reference workflow involves several actors.

Customer
    ↓
Noema
    ↓
Enterprise Systems

Supporting actors may include:

Identity System
Policy System
Account System
Transaction System
Statement System
Support / Case Management System
Human Support Agent

Noema does not replace these enterprise systems.

It orchestrates access to their capabilities through defined interfaces.

⸻

8. Customer

The Customer is the Principal initiating the Intent.

Examples:

"What's my current balance?"
"Show my August statement."
"Find my last transaction."
"How much did I spend last month?"
"I want to report this transaction."

The customer’s natural-language request is the starting point of the workflow.

The request itself does not automatically establish:

identity
authorization
resource
intent certainty
enterprise state

These must be established through the Noema pipeline.

⸻

9. Noema

Noema acts as the Intent-to-Execution layer.

Its responsibilities include:

Intent interpretation
Intent resolution
Context assembly
Ambiguity handling
Trust evaluation
Policy evaluation
Authorization evaluation
Action selection
Execution coordination
Outcome verification
Auditability

Noema does not become the System of Record for the enterprise Business State being queried.

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

⸻

11. Core Workflow

The reference workflow follows:

Customer Request
       │
       ▼
Intent Recognition
       │
       ▼
Intent Resolution
       │
       ▼
Context Assembly
       │
       ▼
Trust Evaluation
       │
       ├── Clarify
       ├── Escalate
       ├── Reject
       └── Execute
                │
                ▼
             Action
                │
                ▼
       Enterprise System
                │
                ▼
          Result / State
                │
                ▼
           Verification
                │
                ▼
             Outcome
                │
                ▼
          Customer Response

Noema does not skip Trust simply because the requested operation is read-only.

⸻

12. Intent Examples

The workflow supports natural-language requests such as:

"What's my balance?"
"How much money do I have?"
"Show me my latest statement."
"Give me my transactions from August."
"How much did I spend on food last month?"
"I don't recognize this transaction."

These requests may have different surface forms while mapping to structured Actions.

For example:

"What's my balance?"
"How much money do I have?"
"What's left in my account?"

may all resolve to:

balance_inquiry

⸻

13. Intent Resolution

Intent resolution converts the customer’s request into a structured Intent.

Conceptually:

Natural Language
       ↓
Intent

Example:

User:
"How much did I spend last month?"
Intent:
operation = spending_summary
period = previous_calendar_month
principal = current_customer

Intent resolution may require additional Context before becoming executable.

⸻

14. Ambiguity

The workflow explicitly treats ambiguity as a state.

Example:

User:
"Show my transactions."
Context:
Account A
Account B
Account C

If Noema cannot deterministically determine which account the customer means:

AMBIGUOUS
     ↓
CLARIFICATION

Noema should not select an account merely because one appears statistically more likely.

The principle is:

Ambiguity is a state, not an invitation to guess.

⸻

15. Context

Context contains the bounded information required for the current operation.

Depending on the request, this may include:

Principal
Account
Transaction data
Statement period
Date range
Currency
Permissions
Relevant enterprise state
Policy
Evidence
Execution history

Context is assembled according to the requirements of the current Intent and Action.

⸻

16. Trust

Trust determines whether Noema has sufficient grounds to proceed.

Trust may evaluate:

identity
authorization
policy
evidence
data authority
freshness
ambiguity
risk
validation

The output is deterministic:

EXECUTE
CLARIFY
ESCALATE
REJECT

The system must not produce:

probably execute

as an execution state.

⸻

17. Authorization

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

⸻

18. Data Authority

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

Noema may use caches, projections, events, and derived data where Policy permits.

However, these must not silently override canonical enterprise data.

⸻

19. Action Mapping

Resolved Intents map to bounded Actions.

Conceptually:

Intent
   ↓
Action

Examples:

balance inquiry
    → retrieve_balance
statement retrieval
    → retrieve_statement
transaction search
    → search_transactions
spending summary
    → calculate_spending_summary
complaint logging
    → create_complaint

Each Action is governed by an Action Contract.

⸻

20. Read Operations

The first four operations are primarily information retrieval:

retrieve_balance
retrieve_statement
search_transactions
calculate_spending_summary

These operations read enterprise state without changing the underlying financial state.

They still require:

identity
authorization
data grounding
appropriate freshness
validation

⸻

21. Complaint Logging

Complaint Logging is included because customer support interactions are an important part of the initial commercial wedge.

A request such as:

"I don't recognize this transaction."

may resolve into:

complaint_logging

The resulting Action may create a support case.

Although it changes support-system state, it does not directly mutate financial state.

Its execution therefore remains within the bounded Phase 1 scope.

⸻

22. Enterprise Boundary

The workflow preserves the boundary:

Noema
    │
    ├── owns Intent State
    ├── owns Trust State
    ├── owns Action State
    └── owns Execution State
Enterprise
    │
    ├── owns Account State
    ├── owns Balance
    ├── owns Transaction State
    ├── owns Statement State
    └── owns Support Case State

Noema coordinates.

Enterprise systems remain authoritative.

⸻

23. Read vs Write Boundary

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

⸻

24. Outcome

Every workflow execution produces an explicit Outcome.

Examples:

BALANCE_RETURNED
STATEMENT_RETRIEVED
TRANSACTIONS_RETURNED
SPENDING_SUMMARY_RETURNED
COMPLAINT_CREATED

Failure outcomes should also be explicit:

AMBIGUOUS
UNAUTHORIZED
DATA_UNAVAILABLE
POLICY_REJECTED
EXECUTION_FAILED
VERIFICATION_FAILED
HUMAN_INTERVENTION_REQUIRED

⸻

25. Verification

Noema should validate that the Action produced the expected result.

For read operations this may involve:

response received
schema valid
resource matches request
identity matches Principal
data within requested scope

For complaint logging:

case created
case identifier returned
case associated with correct Principal
case associated with correct Resource where applicable

Verification prevents an enterprise response from being treated as successful merely because an API call returned successfully.

⸻

26. Failure Handling

Failures are explicit workflow states.

Examples:

Identity unavailable
Account unavailable
Enterprise system unavailable
Policy unavailable
Data unavailable
Authorization failure
Timeout
Malformed response
Conflicting data
Verification failure

Noema determines whether to:

retry
clarify
escalate
reject
terminate

according to the relevant Policy and Action Contract.

⸻

27. Human Intervention

Human intervention may occur when automated execution cannot safely continue.

Examples:

identity ambiguity
enterprise data conflict
unsupported complaint condition
policy exception
system inconsistency

Human intervention is not an uncontrolled escape hatch.

It is an explicit execution state with its own audit trail.

⸻

28. Auditability

A reference execution should preserve enough information to reconstruct:

Principal
Intent
Context
Evidence
Policy
Authorization
Trust Decision
Action
Enterprise Request
Enterprise Response
Outcome
Timestamp

Sensitive enterprise information remains subject to the applicable data boundaries and retention policies.

⸻

29. Example: Balance Inquiry

User:
"What's my balance?"

Resolution:

Intent:
balance_inquiry

Context:

Principal
Account
Authorization

Action:

retrieve_balance

Enterprise:

Ledger

Outcome:

BALANCE_RETURNED

Response:

Customer receives the current permitted balance.

The Ledger remains authoritative for the balance.

⸻

30. Example: Transaction Search

User:
"Find the transaction where I spent $120 at Amazon last month."

Resolution:

Intent:
transaction_search
Constraints:
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

⸻

31. Example: Spending Summary

User:
"How much did I spend on restaurants last month?"

Resolution:

Intent:
spending_summary
Category:
restaurants
Period:
previous month

Noema determines the relevant enterprise data and applies the appropriate aggregation semantics.

The result should preserve the distinction between:

canonical transaction data

and:

derived spending classification

The latter must not be presented as canonical enterprise truth merely because Noema calculated it.

⸻

32. Example: Statement Retrieval

User:
"Show me my August statement."

Noema resolves:

Principal
Statement Period
Relevant Account

If the customer has multiple eligible accounts:

Ambiguous
     ↓
Clarification

Once resolved:

retrieve_statement
        ↓
Statement System
        ↓
Statement
        ↓
Verification
        ↓
Customer

⸻

33. Example: Complaint Logging

User:
"I don't recognize this transaction."

Noema may resolve:

Intent:
complaint_logging

Context may include:

Principal
Transaction
Account
Transaction details
Support permissions

Action:

create_complaint

Outcome:

COMPLAINT_CREATED

The financial transaction itself is not modified by this workflow.

⸻

34. Reference Workflow Boundaries

The workflow begins when:

Customer Intent

enters Noema.

It ends when:

Verified Outcome

is produced and communicated.

It does not own:

customer database
ledger
transaction database
statement store
support database
enterprise identity system

It does not redefine their authority.

⸻

35. Relationship to the Canon

This workflow is an implementation reference for concepts defined elsewhere in the Canon.

It depends on:

Intent
Context
Trust
Authorization
Policy
Evidence
Action
Preconditions
Postconditions
Execution
Failure
Auditability
Enterprise Boundaries
Canonical Data

It must not redefine those concepts.

Where this workflow requires a concept, the corresponding canonical definition takes precedence.

⸻

36. Reference Workflow Architecture

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
                    ENTERPRISE SYSTEM
                            │
                            ▼
                          RESULT
                            │
                            ▼
                       VERIFICATION
                            │
                            ▼
                         OUTCOME
                            │
                            ▼
                         CUSTOMER

⸻

37. Reference Workflow Invariants

Invariant 1

The workflow is limited to Noema’s initial read/support commercial wedge.

Invariant 2

Card renewal is not part of this reference workflow.

Invariant 3

Financial state-changing operations are outside the Phase 1 reference workflow.

Invariant 4

Read operations still require appropriate Identity, Authorization, Trust, and Policy evaluation.

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

Actions must operate within defined enterprise authority and data boundaries.

Invariant 12

Enterprise data used for consequential decisions must satisfy the required authority and freshness guarantees.

Invariant 13

Model-generated interpretations must remain distinguishable from canonical enterprise facts.

Invariant 14

Execution success requires appropriate verification.

Invariant 15

Failures must produce explicit workflow states.

Invariant 16

Human intervention must be an explicit and auditable execution state.

Invariant 17

Noema’s execution state must remain distinct from enterprise Business State.

Invariant 18

The workflow must preserve sufficient information for audit and reconstruction.

Invariant 19

Complaint Logging may create support-system state while remaining within the Phase 1 boundary because it does not directly mutate financial state.

Invariant 20

Future financial write operations must be introduced through separately defined workflows and stronger Trust requirements.

⸻

38. Final Definition

Customer Account Inquiry is Noema’s reference workflow for converting natural-language customer requests into bounded, authorized, trustworthy read and support operations against enterprise systems.

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
TRUST
       ↓
ACTION
       ↓
ENTERPRISE SYSTEM
       ↓
VERIFICATION
       ↓
OUTCOME

The fundamental architectural rule is:

Noema owns the journey from customer Intent to verified Outcome; the enterprise remains the authority for the Business State Noema reasons over.