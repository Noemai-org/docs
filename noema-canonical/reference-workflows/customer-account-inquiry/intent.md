Intent

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/intent.md

⸻

1. Definition

Intent is the normalized representation of what the Customer is trying to accomplish through the Customer Account Inquiry workflow.

Intent answers:

“What outcome is the Customer trying to achieve?”

For this workflow, Intent is primarily concerned with read and support operations involving existing Customer and account information.

Intent is not:

natural language
Action
execution
enterprise state
model-generated guess

The relationship is:

Customer Request
      ↓
Intent
      ↓
Context
      ↓
Trust
      ↓
Action
      ↓
Execution

⸻

2. Purpose

The purpose of Intent in this workflow is to transform an ambiguous natural-language request into a structured representation that can be evaluated deterministically.

For example:

Customer:
"How much money do I have?"
Intent:
get_account_balance

Or:

Customer:
"Show me what I spent last month."
Intent:
get_spending_summary

The Intent establishes the requested objective without prematurely deciding how the enterprise system will fulfill it.

⸻

3. Core Principle

Intent represents the Customer’s desired outcome, not the implementation used to achieve it.

For example:

Intent:
retrieve_statement

does not imply:

GET /statements/{id}

The API call belongs to Integration and Execution.

Therefore:

Intent
   ≠
Action Implementation

⸻

4. Intent Categories

The Customer Account Inquiry workflow supports several primary Intent categories:

account information
statement retrieval
transaction search
spending analysis
complaint submission

These may map to Actions such as:

get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

The mapping must be explicit.

⸻

5. Account Information Intent

A Customer may ask:

"What's my balance?"
"How much do I have?"
"How much is in my account?"

These requests generally represent:

Intent:
get_account_balance

The linguistic form may vary while the underlying Intent remains the same.

⸻

6. Statement Retrieval Intent

Examples:

"Show me my statement."
"I need my statement."
"Get my statement for last month."
"Can I see my June statement?"

These represent:

Intent:
retrieve_statement

The requested period may form part of the Context required to execute the Intent.

⸻

7. Transaction Search Intent

Examples:

"Show me my transactions from last week."
"Did I pay Netflix this month?"
"Find the ₦50,000 transaction."
"Show my transactions at Amazon."

These represent:

Intent:
search_transactions

The search criteria belong to the Intent’s parameters or associated Context.

⸻

8. Spending Summary Intent

Examples:

"How much did I spend last month?"
"Where did I spend the most?"
"Give me my spending summary."

These represent:

Intent:
get_spending_summary

The requested period and aggregation dimensions must be resolved before execution.

⸻

9. Complaint Intent

A Customer may express:

"I want to report a problem."
"I was charged incorrectly."
"I want to make a complaint about this transaction."

The underlying Intent may be:

create_complaint

The specific complaint details and related enterprise Resource must be established before execution.

⸻

10. Intent Structure

Conceptually:

Intent {
    intent_id
    type
    objective
    principal
    target
    parameters
    constraints
    requested_scope
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

11. Intent Type

The Intent Type identifies the requested operation.

Examples:

get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

The type must map to an explicitly supported capability.

Noema must not invent an Action because an Intent appears superficially similar to one.

⸻

12. Intent Objective

The Objective describes the desired result.

Example:

Customer:
"How much did I spend last month?"
Objective:
obtain total spending for the requested period

The objective describes what the Customer wants.

The Action describes how Noema will cause or obtain that result.

⸻

13. Principal

The Intent must identify the Principal on whose behalf the request is being made.

Conceptually:

Intent
   ↓
Principal
   ↓
Customer

The Principal may initially be represented by the authenticated session and subsequently resolved against enterprise identity.

Intent does not itself establish authorization.

⸻

14. Target Resource

An Intent may explicitly or implicitly reference a Resource.

Example:

"What's the balance of my account?"

The target may initially be:

account = unresolved

Resolution must occur before consequential execution.

Noema must not invent a Resource identifier.

⸻

15. Implicit Targets

Natural language often omits explicit Resource identifiers.

Example:

"Show me my transactions."

The Customer may not provide:

account_id

Noema may resolve the target from authenticated identity and enterprise context where Policy permits.

Conceptually:

"my transactions"
       ↓
Principal
       ↓
Eligible Accounts
       ↓
Target Resolution

If multiple candidates remain materially ambiguous:

Clarification

is required.

⸻

16. Intent Parameters

Intent parameters represent information supplied or implied by the Customer that affects the requested outcome.

Examples:

date_from
date_to
merchant
amount
transaction_type
statement_period

For example:

"Show transactions from June."
Intent:
search_transactions
Parameters:
period = June

Parameters should be normalized before Action execution.

⸻

17. Temporal Intent

Customers frequently express time naturally:

last month
this week
yesterday
June
the past three months

Intent captures the temporal requirement.

Noema should subsequently normalize it into an explicit temporal representation.

Example:

"last month"
      ↓
2026-08-01
      ↓
2026-08-31

The exact interpretation must use the applicable timezone and current date.

⸻

18. Intent Constraints

Customers may impose constraints on the requested result.

Examples:

"Show only successful transactions."
"Show transactions above ₦100,000."
"Give me my statement as a PDF."

Conceptually:

Intent
 ├── objective
 ├── parameters
 └── constraints

Constraints must be preserved through planning and execution where supported.

⸻

19. Intent Scope

Intent may contain a requested scope.

Examples:

one account
all eligible accounts
specific date range
specific merchant
specific transaction

Scope must be explicit enough to determine whether the request is executable.

⸻

20. Intent Resolution

Intent Resolution converts natural language into the structured Intent representation.

Natural Language
      ↓
Intent Resolution
      ↓
Structured Intent

The model may assist with this transformation.

However, the resulting Intent must pass through Noema’s Trust and Policy mechanisms before execution.

⸻

21. Model Interpretation

The LLM may produce:

intent_type
parameters
candidate_resources
constraints

But the model’s output is not automatically trusted.

For example:

User:
"Show me John's balance."
Model:
account_id = 123

Noema must not treat:

123

as authoritative merely because the model selected it.

Identity and Resource resolution must be grounded against enterprise data.

⸻

22. Intent Confidence

Model confidence may be useful as an input to Trust.

For example:

Intent:
get_account_balance
Model confidence:
0.96

But confidence does not authorize execution.

The Trust layer must consider additional factors such as:

ambiguity
identity
permissions
Action risk
enterprise state
Policy

Therefore:

high model confidence
      ≠
authorization

⸻

23. Ambiguous Intent

Some requests may correspond to multiple possible Intents.

Example:

"Show me my account."

This could mean:

account balance
account details
account statement

If the intended objective cannot be deterministically established:

AMBIGUOUS
   ↓
CLARIFY

Noema should not arbitrarily select an interpretation when the distinction affects execution.

⸻

24. Ambiguous Resource

The Intent may be clear while the Resource is ambiguous.

Example:

Intent:
get_account_balance
Target:
account = ambiguous

If the Customer has multiple eligible accounts:

Account A
Account B
Account C

Noema should request clarification unless Policy provides a deterministic resolution rule.

⸻

25. Missing Intent Information

An Intent may be structurally valid but incomplete.

Example:

"Show me transactions."

If the Customer has a single eligible account and Policy permits defaulting, the target may be resolved automatically.

But:

"Show me the statement."

may require a period if the enterprise capability requires one.

The system should distinguish:

missing but safely defaultable

from:

missing and materially ambiguous

⸻

26. Intent and Context

Intent describes what the Customer wants.

Context provides the information necessary to understand and execute that request.

Example:

Intent:
get_account_balance
Context:
authenticated_customer
eligible_account
currency
account_status

Therefore:

Intent
   +
Context
   ↓
Executable Action Candidate

⸻

27. Intent and Evidence

Evidence does not define the Intent.

Evidence supports decisions about the Intent and its execution.

For example:

Customer message:
"Show me my balance."

provides evidence of the requested objective.

Enterprise identity data provides evidence for resolving:

"my"

to a specific Principal.

⸻

28. Intent and Trust

Trust evaluates whether the Intent is sufficiently grounded to proceed.

Conceptually:

Intent
   ↓
Context
   ↓
Evidence
   ↓
Trust

Trust may determine:

EXECUTE
CLARIFY
ESCALATE
REJECT

The model should not bypass this decision.

⸻

29. Intent and Policy

Policy determines what Noema is permitted to do with a particular Intent.

Example:

Intent:
get_account_balance

may be permitted for an authenticated Customer.

A different Intent may require stronger verification.

Therefore:

Intent
   ↓
Policy
   ↓
Allowed / Blocked

Intent itself does not establish permission.

⸻

30. Intent and Action

Intent identifies the desired outcome.

Action represents an executable capability.

Example:

Intent:
"I want to know my balance."
        ↓
Action:
get_account_balance

The mapping should be explicit:

Intent
   ↓
Action Selection

An Intent may map to one Action or, for compound requests, multiple Actions.

⸻

31. One Intent, Multiple Actions

A Customer may say:

"Show me my balance and my transactions from last month."

This represents one compound Intent with multiple executable requirements.

Intent
   ├── get_account_balance
   └── search_transactions

Each Action retains its own execution lifecycle.

⸻

32. Multiple Intents

A single Customer message may contain multiple independent objectives.

Example:

"Show my balance, find my Netflix payment, and tell me how much I spent last month."

Noema should decompose the request into explicit Intent components.

Compound Intent
   ├── get_account_balance
   ├── search_transactions
   └── get_spending_summary

The decomposition must preserve the relationship between the original request and its constituent Intents.

⸻

33. Intent Dependencies

Some Intent components depend on others.

Example:

"Show me the transactions for my savings account."

requires:

Principal Resolution
      ↓
Account Resolution
      ↓
Transaction Search

The dependency should be explicit rather than hidden inside model reasoning.

⸻

34. Intent Lifecycle

Conceptually:

RAW
 ↓
INTERPRETED
 ↓
NORMALIZED
 ↓
RESOLVED
 ↓
TRUSTED
 ↓
ACTIONABLE

Possible terminal states include:

CLARIFICATION_REQUIRED
REJECTED
ABANDONED
COMPLETED

Intent state should remain distinct from Execution State.

⸻

35. Intent State vs Execution State

These are different dimensions.

Intent:
RESOLVED
Execution:
FAILED

is valid.

Likewise:

Intent:
RESOLVED
Execution:
UNKNOWN

is valid.

Noema must not collapse the two state machines.

⸻

36. Intent Persistence

Noema may persist the Intent lifecycle to support:

auditability
recovery
conversation continuity
execution reconstruction
analytics

Persisted Intent should retain sufficient provenance to understand how it was produced.

⸻

37. Intent Provenance

A consequential Intent should be traceable to its source.

Conceptually:

Intent
   ↓
source
   ↓
Customer message / API / event

Useful metadata may include:

intent_id
source
created_at
normalized_at
resolver
model_reference
confidence
resolution_evidence

Model-specific metadata should not replace the semantic Intent itself.

⸻

38. Intent Versioning

Intent representations may evolve.

Example:

intent_version = 1

This allows Noema to reconstruct which semantic representation was used when an Action was planned.

Changes to Intent schema must not silently reinterpret historical executions.

⸻

39. Intent and Canonical Data

Intent may reference enterprise facts that must eventually be grounded against Canonical Data.

Example:

"Show me my balance."

Intent:

get_account_balance

Canonical enterprise resolution:

Customer → Account

Noema uses Canonical Data to ground the execution without becoming the owner of the underlying account data.

⸻

40. Intent and Identity

Pronouns and natural-language references frequently require identity resolution.

Examples:

my account
my card
my transactions
John's account
the account I used yesterday

Intent captures the semantic reference.

Identity Resolution determines the enterprise identity.

These must remain distinct.

⸻

41. Intent and Data Boundaries

Intent should contain only the information necessary to represent the Customer’s requested objective.

The complete Customer profile should not be copied into the Intent merely because it exists in Context.

For example:

Intent:
search_transactions

does not require:

home_address
date_of_birth
unrelated profile data

unless explicitly required by the workflow.

⸻

42. Intent and Privacy

Natural-language requests may contain sensitive information.

Noema should apply appropriate:

minimization
retention
access control
redaction
purpose limitation

to persisted Intent and associated Context.

⸻

43. Intent and Temporal Context

Temporal expressions should be preserved semantically before normalization.

Example:

"last month"

should initially remain associated with the Customer’s Intent.

Normalization then produces:

period {
    start
    end
    timezone
}

This prevents downstream systems from independently interpreting the original language.

⸻

44. Intent and Customer Corrections

A Customer may correct a previously expressed Intent.

Example:

Customer:
"Show my transactions."
Noema:
"Which account?"
Customer:
"My savings account."

The original Intent should be updated with the newly supplied information rather than creating an unrelated request.

Original Intent
      ↓
Clarification
      ↓
Updated Intent

The lifecycle should preserve the correction.

⸻

45. Intent and Cancellation

A Customer may cancel before execution.

Example:

Customer:
"Show my statement."
Customer:
"Never mind."

The Intent may transition to:

CANCELLED

No execution should occur after cancellation unless a separate valid request is received.

⸻

46. Intent and Replanning

If Context changes before execution, Noema may need to re-evaluate the Intent’s executable representation.

For example:

Account becomes unavailable
        ↓
Original plan no longer valid
        ↓
Re-evaluate

Replanning must not silently change the Customer’s requested objective.

Intent
   remains stable
      ↓
Plan
   may change

⸻

47. Intent and Enterprise Events

Enterprise events may affect whether an Intent remains executable.

Example:

Intent:
retrieve_statement
Enterprise Event:
account_closed

The Intent remains what the Customer requested.

Its execution feasibility may change.

Intent
   ↓
Updated Context
   ↓
Trust / Policy
   ↓
Re-evaluate

⸻

48. Intent and Failure

Failure occurs during execution.

The Intent should generally remain intact so Noema can determine whether:

retry
recover
inform
escalate

is appropriate.

Example:

Intent:
get_account_balance
Execution:
TIMEOUT
Intent:
still valid

The failure does not rewrite what the Customer asked for.

⸻

49. Intent and Outcome

The Outcome describes what happened relative to the requested Intent.

Example:

Intent:
retrieve_statement
Execution:
SUCCEEDED
Outcome:
statement retrieved

Or:

Intent:
retrieve_statement
Execution:
FAILED
Outcome:
statement not retrieved

Intent and Outcome must remain separate.

⸻

50. Intent Model

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

⸻

51. Intent Relationships

Intent
   │
   ├── expressed_by → Principal
   ├── targets → Resource
   ├── requires → Context
   ├── supported_by → Evidence
   ├── evaluated_by → Trust
   ├── constrained_by → Policy
   ├── maps_to → Action
   ├── produces → Execution
   └── results_in → Outcome

⸻

52. Reference Intent Flows

Balance Inquiry

"What's my balance?"
        ↓
Intent
        ↓
get_account_balance
        ↓
Resolve Account
        ↓
Trust
        ↓
Execute

Statement Retrieval

"Show my statement from last month."
        ↓
Intent
        ↓
retrieve_statement
        ↓
Resolve Account + Period
        ↓
Trust
        ↓
Execute

Transaction Search

"Find my Netflix payment from last month."
        ↓
Intent
        ↓
search_transactions
        ↓
Resolve Account + Merchant + Period
        ↓
Trust
        ↓
Execute

Spending Summary

"How much did I spend last month?"
        ↓
Intent
        ↓
get_spending_summary
        ↓
Resolve Account + Period
        ↓
Trust
        ↓
Execute

Complaint

"I want to report this transaction."
        ↓
Intent
        ↓
create_complaint
        ↓
Resolve Customer + Transaction
        ↓
Trust
        ↓
Execute

⸻

53. Intent Invariants

Invariant 1

Intent represents the Customer’s requested objective, not its implementation.

Invariant 2

Intent must remain distinct from Action.

Invariant 3

Intent must remain distinct from Execution.

Invariant 4

Intent must remain distinct from enterprise Business State.

Invariant 5

Model-generated Intent is not automatically trusted.

Invariant 6

Model confidence does not constitute authorization.

Invariant 7

Identity and Resource references must be grounded before consequential execution.

Invariant 8

Noema must not resolve materially ambiguous Intent through arbitrary guessing.

Invariant 9

Noema must not invent missing Resource identifiers.

Invariant 10

Missing information may only be defaulted when Policy provides a deterministic basis for doing so.

Invariant 11

Intent parameters and constraints must survive normalization and planning without semantic distortion.

Invariant 12

Temporal expressions must be normalized before being interpreted independently by downstream systems.

Invariant 13

Intent State must remain separate from Execution State.

Invariant 14

A failed Execution must not rewrite the Customer’s original Intent.

Invariant 15

Compound Intent must preserve its constituent objectives and their relationships.

Invariant 16

Each Action derived from a Compound Intent must maintain its own Execution State.

Invariant 17

Customer corrections must update the relevant Intent rather than silently creating a different objective.

Invariant 18

Customer cancellation must prevent execution where cancellation occurs before the execution boundary.

Invariant 19

Replanning may change execution strategy but must not silently change the requested objective.

Invariant 20

Intent persistence must retain sufficient provenance for reconstruction where required.

Invariant 21

Intent data must respect Data Boundaries and privacy requirements.

Invariant 22

Enterprise events may change Intent executability but do not redefine the Customer’s original objective.

Invariant 23

The model may interpret natural language but must not bypass Trust or Policy.

Invariant 24

An Intent becomes executable only after required Context, Trust, Policy, and Action requirements are satisfied.

Invariant 25

Ambiguity is a state that must be resolved or preserved—not an invitation to guess.

⸻

54. Final Definition

Intent is the structured representation of the outcome a Customer is trying to achieve.

Within the Customer Account Inquiry workflow:

CUSTOMER REQUEST
       │
       ▼
     INTENT
       │
       ├── Objective
       ├── Principal
       ├── Target
       ├── Parameters
       ├── Constraints
       └── Scope
       │
       ▼
    CONTEXT
       │
       ▼
     TRUST
       │
       ▼
     POLICY
       │
       ▼
     ACTION
       │
       ▼
   EXECUTION
       │
       ▼
    OUTCOME

And the architectural rule is:

Intent defines what the Customer wants, not what Noema will do to achieve it. Noema may use a probabilistic model to interpret the request, but the resulting Intent must be grounded, resolved, and governed by Trust and Policy before it can become an executable Action.