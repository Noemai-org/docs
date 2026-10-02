Intent

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/intent.md

⸻

1. Definition

Intent is the structured, normalized representation of what the Customer is trying to accomplish through the Customer Account Inquiry workflow.

Intent answers:

What outcome is the Customer trying to achieve?

For this workflow, Intent primarily represents read and support objectives involving existing Customer, Account, Transaction, Statement, and Support resources.

Intent is not:

* the Customer’s raw natural-language request
* Context
* Evidence
* Trust
* Policy
* Action
* Execution
* Outcome
* enterprise Business State
* a model-generated guess that has not been resolved

The relationship is:

Customer Request
      ↓
Intent Interpretation
      ↓
Intent Resolution
      ↓
Context
      ↓
Trust + Policy
      ↓
Action
      ↓
Execution
      ↓
Outcome

Intent therefore establishes the requested objective that the rest of the Noema execution system must preserve.

⸻

2. Purpose

The purpose of Intent in this workflow is to transform a natural-language request into a structured representation that can be:

* understood
* normalized
* resolved
* validated
* grounded
* governed
* planned
* executed
* audited

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

The Intent establishes what the Customer wants, without prematurely determining the enterprise implementation used to satisfy that objective.

⸻

3. Core Principle

Intent represents the Customer’s desired outcome, not the mechanism used to achieve it.

For example:

Intent:
retrieve_statement

does not imply:

GET /statements/{id}

The API operation belongs to the Action, Integration, and Execution layers.

Therefore:

Intent
   ≠
Action
   ≠
Integration
   ≠
Execution

Intent should remain semantically stable even when the execution strategy changes.

⸻

4. Intent vs Customer Request

The Customer Request is the expression presented by the Customer.

Intent is Noema’s normalized representation of the objective expressed by that request.

For example:

Customer Request:
"How much do I have?"
        ↓
Intent:
{
    type: get_account_balance,
    objective: obtain_current_account_balance
}

The original request should remain available as provenance where required.

The normalized Intent must not erase the source expression when reconstruction or audit requires it.

Therefore:

Customer Request
        ↓
Interpretation
        ↓
Intent

rather than:

Customer Request
        ↓
Intent

where the transformation is unobservable.

⸻

5. Intent Categories

The Customer Account Inquiry workflow supports several primary Intent categories:

* account information
* statement retrieval
* transaction search
* spending analysis
* complaint submission

These may map to Actions such as:

get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

The mapping must be explicit.

An Intent must not automatically become executable merely because a superficially similar Action exists.

⸻

6. Account Information Intent

A Customer may ask:

"What's my balance?"
"How much do I have?"
"How much is in my account?"

These requests generally represent:

Intent:
get_account_balance

The linguistic form may vary while the underlying objective remains the same.

The Intent should capture the objective without inventing the specific account unless that account has subsequently been resolved.

⸻

7. Statement Retrieval Intent

Examples:

"Show me my statement."
"I need my statement."
"Get my statement for last month."
"Can I see my June statement?"

These represent:

Intent:
retrieve_statement

The requested period may form part of the Intent parameters and subsequently become normalized Context.

If the enterprise capability requires a period and no deterministic period can be established, the Intent may remain:

INCOMPLETE

or:

CLARIFICATION_REQUIRED

rather than having Noema invent one.

⸻

8. Transaction Search Intent

Examples:

"Show me my transactions from last week."
"Did I pay Netflix this month?"
"Find the ₦50,000 transaction."
"Show my transactions at Amazon."

These generally represent:

Intent:
search_transactions

Search criteria may include:

date_range
merchant
amount
transaction_type
status

The criteria must survive normalization without semantic distortion.

⸻

9. Spending Summary Intent

Examples:

"How much did I spend last month?"
"Where did I spend the most?"
"Give me my spending summary."

These generally represent:

Intent:
get_spending_summary

The requested period and aggregation dimensions must be resolved before execution.

For example:

"How much did I spend last month?"

may establish:

objective = obtain_total_spending
period = previous_calendar_month

The underlying transaction data remains enterprise data.

The resulting summary may be derived data.

⸻

10. Complaint Intent

A Customer may express:

"I want to report a problem."
"I was charged incorrectly."
"I want to make a complaint about this transaction."

The underlying Intent may be:

create_complaint

The complaint details and related Resource must be established before execution.

For example:

Intent:
create_complaint
Required resolution:
customer
related_transaction
complaint_description

The Intent establishes the Customer’s objective.

It does not establish that a Case has actually been created.

⸻

11. Intent Structure

Conceptually:

Intent {
    intent_id
    intent_version
    type
    objective
    principal
    target
    parameters
    constraints
    scope
    status
    source
    provenance
    created_at
    updated_at
}

This is a semantic model rather than a requirement for a literal database schema.

The important property is that the Intent preserves the distinction between:

* requested objective
* unresolved references
* normalized parameters
* resolved resources
* execution requirements
* provenance
* lifecycle state

⸻

12. Intent Type

The Intent Type identifies the requested objective or semantic operation.

Examples:

get_account_balance
retrieve_statement
search_transactions
get_spending_summary
create_complaint

The type must map to an explicitly supported capability.

Noema must not invent an Action because an Intent appears superficially similar to one.

The relationship is:

Intent Type
      ↓
Capability Resolution
      ↓
Supported Action

not:

Intent Type
      ↓
arbitrary model-selected tool

⸻

13. Intent Objective

The Objective describes the desired result in semantic terms.

Example:

Customer:
"How much did I spend last month?"
Objective:
obtain total spending for the requested period

The Objective describes what the Customer wants.

The Action describes the executable capability selected to satisfy that objective.

Therefore:

Objective
   ≠
Implementation

An implementation may change while the Customer’s objective remains unchanged.

⸻

14. Principal

The Intent must identify the Principal on whose behalf the request is being made.

Conceptually:

Intent
   ↓
Principal
   ↓
Customer

The Principal may initially be represented by the authenticated session and subsequently resolved against enterprise identity.

Intent does not itself establish authorization.

Therefore:

Principal identified
      ≠
Principal authorized

Authorization remains a separate Policy-controlled determination.

⸻

15. Target Resource

An Intent may explicitly or implicitly reference a Resource.

Example:

"What's the balance of my account?"

The target may initially be:

account = unresolved

Resolution must occur before consequential execution.

Noema must not invent a Resource identifier merely to make the Intent executable.

⸻

16. Implicit Targets

Natural language frequently omits explicit Resource identifiers.

Example:

"Show me my transactions."

The Customer may not provide:

account_id

Noema may resolve the target from authenticated identity and enterprise Context where Policy permits.

Conceptually:

"my transactions"
       ↓
Principal
       ↓
Eligible Resources
       ↓
Target Resolution

If one eligible Resource exists and Policy permits deterministic defaulting:

single eligible Resource
       ↓
resolved target

If multiple materially relevant Resources remain:

multiple candidates
       ↓
AMBIGUITY
       ↓
CLARIFICATION

⸻

17. Intent Parameters

Intent parameters represent information supplied or implied by the Customer that affects the requested outcome.

Examples:

date_from
date_to
merchant
amount
transaction_type
statement_period
status

For example:

"Show transactions from June."

may produce:

Intent:
search_transactions
Parameters:
period = June

Parameters should be normalized before Action execution.

Normalization must preserve the Customer’s semantic meaning.

⸻

18. Temporal Intent

Customers frequently express time naturally:

last month
this week
yesterday
June
the past three months

Intent captures the temporal requirement before it is transformed into an execution-ready temporal representation.

Example:

"last month"
      ↓
Temporal Resolution
      ↓
period {
    start
    end
    timezone
}

The exact interpretation must use the applicable timezone and current date.

Downstream enterprise systems should receive the resolved temporal representation rather than independently interpreting the original natural-language expression.

⸻

19. Intent Constraints

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

If a requested constraint cannot be satisfied by the available capability, Noema must not silently discard it.

The system should determine the appropriate outcome through Trust, Policy, and Action resolution.

⸻

20. Intent Scope

Intent may contain a requested scope.

Examples:

one account
all eligible accounts
specific date range
specific merchant
specific transaction

Scope must be explicit enough to determine whether the request can safely proceed.

Scope must not silently expand during execution.

For example:

"my savings account"

must not become:

all customer accounts

merely because the latter is easier for an integration to query.

⸻

21. Intent Resolution

Intent Resolution converts a Customer Request into a structured Intent.

Conceptually:

Natural Language
      ↓
Interpretation
      ↓
Candidate Intent
      ↓
Normalization
      ↓
Resolution
      ↓
Resolved Intent

The model may assist with interpretation.

However, model output is only a candidate representation until it passes the required grounding, Trust, and Policy mechanisms.

⸻

22. Candidate Intent vs Resolved Intent

Noema should distinguish between an interpreted candidate and a resolved Intent.

For example:

Model Interpretation:
type = get_account_balance
target = "my account"

does not necessarily establish:

account_id = 9912

The candidate may therefore remain:

target = unresolved

until enterprise identity and Resource resolution establish the target.

Conceptually:

Candidate Intent
      ↓
Grounding
      ↓
Resolution
      ↓
Resolved Intent

This prevents probabilistic model output from being silently promoted to authoritative enterprise identifiers.

⸻

23. Model Interpretation

The LLM may produce:

intent_type
parameters
candidate_resources
constraints
temporal_expressions
candidate_scope

But model output is not automatically trusted.

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

24. Intent Confidence

Model confidence may be useful as an input to Trust.

For example:

Intent:
get_account_balance
Model confidence:
0.96

But confidence does not authorize execution.

Trust must consider additional factors such as:

* ambiguity
* identity resolution
* Resource resolution
* permissions
* Action risk
* enterprise state
* Evidence
* Policy
* Context sufficiency

Therefore:

high model confidence
      ≠
high Trust

and:

high model confidence
      ≠
authorization

⸻

25. Ambiguous Intent

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

Noema should not arbitrarily select an interpretation when the distinction materially affects the requested outcome or execution.

⸻

26. Ambiguous Resource

The Intent may be clear while the Resource remains ambiguous.

Example:

Intent:
get_account_balance
Target:
account = ambiguous

If the Customer has:

Account A
Account B
Account C

Noema should request clarification unless Policy provides a deterministic resolution rule.

This distinction is important:

Intent ambiguity
      ≠
Resource ambiguity

Both may require clarification, but they occur at different semantic layers.

⸻

27. Missing Intent Information

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

Noema must not invent material values to eliminate incompleteness.

⸻

28. Intent Completeness

Intent completeness should be evaluated against the requirements of the intended Action.

For example:

Intent:
search_transactions

may require:

principal
account
search scope

while:

Intent:
retrieve_statement

may additionally require:

statement period

Therefore:

Intent completeness

is contextual to the capability required to satisfy the objective.

An Intent can be semantically understandable while still being operationally incomplete.

⸻

29. Intent and Context

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
authorization_context

Therefore:

Intent
   +
Context
   ↓
Executable Action Candidate

Intent should not absorb the entire Context.

Only information that semantically belongs to the requested objective should remain in Intent.

⸻

30. Intent and Evidence

Evidence does not define the Intent.

Evidence supports decisions concerning the Intent and its resolution or execution.

For example:

Customer message:
"Show me my balance."

provides evidence for the requested objective.

Enterprise identity data may provide evidence for resolving:

"my"

to a specific Principal.

Evidence therefore supports:

Intent Interpretation
Intent Resolution
Resource Resolution
Trust
Execution

without becoming the Intent itself.

⸻

31. Intent and Trust

Trust evaluates whether the Intent is sufficiently grounded and complete to proceed.

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

A valid Intent can still fail Trust requirements.

⸻

32. Intent and Policy

Policy determines what Noema is permitted to do with a particular Intent.

Example:

Intent:
get_account_balance

may be permitted for an authenticated Customer within an authorized account scope.

A different Intent may require stronger verification or may not be available to the Customer.

Therefore:

Intent
   ↓
Policy
   ↓
Allowed / Blocked

Intent itself does not establish permission.

⸻

33. Intent and Action

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

An Intent may map to:

one Action

or, for a compound request:

multiple Actions

The mapping must preserve the original objective.

⸻

34. Intent-to-Action Resolution

Action selection should be based on the resolved Intent, Context, and applicable Policy.

Conceptually:

Resolved Intent
      +
Required Context
      +
Policy
      ↓
Action Candidate
      ↓
Action Validation
      ↓
Executable Action

The LLM may propose an Action candidate.

It must not independently authorize or invoke that Action.

⸻

35. One Intent, Multiple Actions

A Customer may say:

"Show me my balance and my transactions from last month."

This represents one compound Customer objective containing multiple executable requirements.

Conceptually:

Compound Intent
   ├── objective: obtain account balance
   └── objective: obtain transactions for prior month

which may resolve to:

get_account_balance
search_transactions

Each Action retains its own:

* Context
* Preconditions
* authorization
* execution state
* evidence
* Outcome

The compound Intent remains the representation of the Customer’s overall request.

⸻

36. Multiple Intents

A single Customer message may contain multiple independent objectives.

Example:

"Show my balance, find my Netflix payment, and tell me how much I spent last month."

Noema should decompose the request into explicit Intent components:

Compound Intent
   ├── get_account_balance
   ├── search_transactions
   └── get_spending_summary

The decomposition must preserve the relationship between:

original Customer Request

and:

constituent Intent components

⸻

37. Intent Dependencies

Some Intent components depend on information established by others.

Example:

"Show me the transactions for my savings account."

requires:

Principal Resolution
      ↓
Account Resolution
      ↓
Transaction Search

The dependency should be explicit rather than hidden inside model reasoning.

The resolved Intent should therefore be capable of expressing unresolved dependencies where necessary.

⸻

38. Compound Intent Structure

Conceptually:

CompoundIntent {
    intent_id
    objectives[]
    relationships[]
    shared_context_requirements
    scope
    constraints
}

Each constituent objective may become an independently executable Intent component.

For example:

Compound Intent
        │
        ├── Intent A
        │      ↓
        │   Action A
        │
        └── Intent B
               ↓
            Action B

The compound structure must not cause unrelated Context or permissions to leak between Actions.

⸻

39. Intent Lifecycle

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

Possible non-success transitions include:

AMBIGUOUS
     ↓
CLARIFICATION_REQUIRED
INCOMPLETE
     ↓
CLARIFICATION_REQUIRED
REJECTED
CANCELLED
ABANDONED

Intent state must remain distinct from Execution State.

⸻

40. Intent State vs Execution State

These are different dimensions.

For example:

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

And:

Intent:
RESOLVED
Execution:
SUCCEEDED

is valid.

Noema must not collapse these state machines.

The Customer’s objective can remain valid even when execution fails.

⸻

41. Intent Persistence

Noema may persist the Intent lifecycle to support:

* auditability
* recovery
* conversation continuity
* execution reconstruction
* analytics
* clarification
* replanning

Persisted Intent should retain sufficient provenance to understand how it was produced and resolved.

Persistence should respect applicable Data Boundaries and retention requirements.

⸻

42. Intent Provenance

A consequential Intent should be traceable to its source.

Conceptually:

Intent
   ↓
Provenance
   ↓
Customer message / API / event

Useful metadata may include:

intent_id
source
source_reference
created_at
normalized_at
resolver
model_reference
confidence
resolution_evidence
intent_version

Model-specific metadata should not replace the semantic Intent itself.

⸻

43. Intent Versioning

Intent representations may evolve.

Example:

intent_version = 1

This allows Noema to reconstruct which semantic representation was used when an Action was planned or executed.

Changes to Intent schema must not silently reinterpret historical executions.

Historical execution records must retain sufficient version information to preserve semantic meaning.

⸻

44. Intent and Canonical Data

Intent may reference enterprise facts that must eventually be grounded against Canonical Data.

Example:

"Show me my balance."

Intent:

get_account_balance

Canonical enterprise resolution:

Customer
   ↓
Account

Noema uses Canonical Data to ground the execution without becoming the owner of the underlying account data.

The Intent may reference canonical resources without becoming canonical Business State itself.

⸻

45. Intent and Identity

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

Conceptually:

Semantic Reference
      ↓
Identity Resolution
      ↓
Enterprise Principal / Resource

⸻

46. Intent and Data Boundaries

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

Intent minimization should therefore be applied independently from Context minimization.

⸻

47. Intent and Privacy

Natural-language requests may contain sensitive information.

Noema should apply appropriate:

* minimization
* retention
* access control
* redaction
* purpose limitation

to persisted Intent and associated provenance.

The existence of information in the original Customer Request does not mean that every downstream component should receive it.

⸻

48. Intent and Temporal Context

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

This allows Noema to distinguish:

what the Customer said

from:

how Noema normalized it

The normalized representation should retain sufficient provenance when temporal interpretation is consequential.

⸻

49. Intent and Customer Corrections

A Customer may correct a previously expressed Intent.

Example:

Customer:
"Show my transactions."
Noema:
"Which account?"
Customer:
"My savings account."

The original Intent should be updated with the newly supplied information rather than creating an unrelated request.

Conceptually:

Original Intent
      ↓
Clarification
      ↓
Updated Intent
      ↓
Resolution

The lifecycle should preserve the correction and its relationship to the original request.

⸻

50. Intent and Clarification

Clarification is a mechanism for resolving an Intent that cannot safely become executable with the information currently available.

Examples:

Which account do you mean?
Which statement period do you need?
Which transaction are you referring to?

Clarification should request only the information necessary to resolve the material ambiguity or missing requirement.

Noema should not ask unnecessary questions merely because additional Context could be obtained.

⸻

51. Intent and Cancellation

A Customer may cancel before execution.

Example:

Customer:
"Show me my statement."
Customer:
"Never mind."

The Intent may transition to:

CANCELLED

No execution should occur after cancellation where cancellation occurs before the execution boundary, unless a separate valid request is received.

Cancellation must not silently be interpreted as a new objective.

⸻

52. Intent and Replanning

If Context changes before execution, Noema may need to re-evaluate the Intent’s executable representation.

For example:

Account becomes unavailable
        ↓
Original execution plan no longer valid
        ↓
Re-evaluate

Replanning must not silently change the Customer’s requested objective.

Therefore:

Intent
   remains stable
       ↓
Plan
   may change

A changed execution strategy does not constitute a changed Intent.

⸻

53. Intent and Enterprise Events

Enterprise events may affect whether an Intent remains executable.

Example:

Intent:
retrieve_statement
Enterprise Event:
account_closed

The Intent remains:

retrieve_statement

Its execution feasibility may change.

Conceptually:

Intent
   ↓
Updated Context
   ↓
Trust / Policy
   ↓
Re-evaluate

Enterprise state changes should not be rewritten into the Customer’s original objective.

⸻

54. Intent and Failure

Failure occurs during or as a consequence of execution.

The Intent should generally remain intact so Noema can determine whether:

* retry
* recover
* reconcile
* inform
* escalate

is appropriate.

Example:

Intent:
get_account_balance
Execution:
TIMEOUT

The Intent remains valid:

Intent:
get_account_balance

The execution failure does not rewrite what the Customer asked for.

⸻

55. Intent and Unknown Execution

An execution may become:

UNKNOWN

without changing the Intent.

For example:

Intent:
create_complaint
Execution:
UNKNOWN

The Customer’s objective remains:

create_complaint

Noema must reconcile the execution rather than reinterpret the original objective merely because execution status is uncertain.

⸻

56. Intent and Outcome

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

The existence of an Intent does not establish its Outcome.

⸻

57. Intent and Model Output

Model output may contain several semantic classes of information.

For example:

model_intent_type
model_candidate_resource
model_temporal_interpretation
model_candidate_constraints
model_confidence

These should remain distinguishable from resolved enterprise facts.

For example:

model_candidate_account = 123

must not silently become:

canonical_account_id = 123

without the appropriate resolution and grounding.

This distinction is fundamental to Noema’s architecture.

⸻

58. Intent and User-Provided Facts

User-provided information may be part of Intent.

Example:

"I made a payment to Netflix yesterday."

The Customer has supplied:

merchant = Netflix
temporal_reference = yesterday

These are Customer-provided inputs.

They do not automatically establish:

canonical merchant = Netflix
canonical transaction exists
transaction date = yesterday

Where those facts matter to execution, they must be resolved against the relevant enterprise systems.

⸻

59. Intent and Derived Information

Intent may contain derived interpretations where necessary.

For example:

"last month"

may become:

period:
2026-08-01 → 2026-08-31

The normalized period is a derived interpretation of the Customer’s language.

Noema should preserve the distinction between:

Customer expression

and:

Noema-derived normalization

where that distinction matters for auditability or reconstruction.

⸻

60. Intent and Multiple Sources

Intent resolution may use multiple sources.

For example:

Customer Message
      ↓
requested objective
Identity System
      ↓
Principal resolution
Account System
      ↓
Resource resolution
Policy
      ↓
permitted scope

Noema should preserve the provenance of consequential resolution decisions.

Agreement among sources does not automatically make every source authoritative for every proposition.

Authority remains property-specific.

⸻

61. Intent Conflicts

Intent-related information may conflict.

Example:

Customer Request:
"Show me my savings account."
Session Context:
Customer has one savings account.
Enterprise Account System:
Two eligible savings accounts.

Noema must not resolve the conflict through model preference.

Instead:

Conflict
   ↓
Resolution
   ↓
Trust / Policy
   ↓
Continue / Clarify / Escalate

Where ambiguity remains material, clarification is preferable to silent guessing.

⸻

62. Intent and Authorization

Intent identifies the requested objective.

Authorization determines whether the Principal may perform the corresponding Action against the relevant Resource.

Therefore:

Intent:
get_account_balance

does not imply:

authorized = true

The relationship is:

Intent
   +
Principal
   +
Resource
   +
Policy
   ↓
Authorization Decision

Authorization must be established before consequential execution.

⸻

63. Intent and Action Risk

Different Intents may have different execution consequences.

For example:

get_account_balance

is read-oriented.

Whereas:

create_complaint

changes enterprise support state.

Intent therefore contributes to determining the applicable Action and Policy requirements.

The Intent itself does not determine whether execution is safe or permitted.

⸻

64. Intent and Preconditions

An Intent may be semantically resolved while its corresponding Action still lacks required Preconditions.

Example:

Intent:
retrieve_statement

but:

account = unresolved

or:

authorization = unresolved

The Intent remains valid.

The Action remains non-executable until the required Context and Preconditions are satisfied.

Therefore:

Valid Intent
      ≠
Executable Action

⸻

65. Intent and Execution Boundary

Intent exists before the execution boundary.

Conceptually:

Customer Request
      ↓
Intent
      ↓
Context
      ↓
Trust
      ↓
Policy
      ↓
Action
      │
      │ EXECUTION BOUNDARY
      ▼
Enterprise System

Once execution begins, the execution system establishes what actually happened.

Intent must not be rewritten retrospectively based solely on the execution result.

⸻

66. Intent and Recovery

When execution fails or becomes uncertain, the original Intent provides the objective against which recovery is evaluated.

Example:

Intent:
create_complaint
Execution:
UNKNOWN

Recovery may require:

reconciliation

rather than generating a new Intent:

create_complaint_again

The original objective remains stable while the execution state evolves.

⸻

67. Intent and Auditability

For consequential execution, Noema should be able to answer:

What did the Customer request?
How was the request interpreted?
What Intent was produced?
What information was unresolved?
What was subsequently resolved?
What Action was selected?
What Policy applied?
What was executed?
What happened?

The Intent record therefore provides an important semantic link between:

Customer Request

and:

Execution

⸻

68. Intent Reconstruction

Where required, Noema should be capable of reconstructing the Intent that was used for an execution.

Conceptually:

Customer Request
      ↓
Intent Version
      ↓
Resolved Intent
      ↓
Action
      ↓
Execution

Historical reconstruction should not depend on re-running the model and hoping it produces the same interpretation.

The persisted representation and provenance should be sufficient for deterministic reconstruction where required.

⸻

69. Intent and Conversation Continuity

Conversation continuity may allow later Customer messages to provide missing information.

Example:

Customer:
"Show me my transactions."
Noema:
"Which account?"
Customer:
"My savings account."

The second message should be interpreted in relation to the unresolved prior Intent.

Conceptually:

Existing Intent
      +
Clarification Response
      ↓
Updated Intent

Conversation history should therefore contribute only where it is relevant to the current Intent.

⸻

70. Intent and Context Expansion

An Intent may initially require limited Context.

As resolution proceeds, additional Context may become necessary.

Example:

Intent:
get_spending_summary
Initial:
principal resolved
Need:
account
Need:
period
Need:
authorized scope

Context may therefore expand as required by the Intent and Action.

This does not mean the Intent itself should absorb every newly discovered Context fact.

⸻

71. Intent and Context Reduction

Once information has served its purpose, it need not remain attached to every downstream Action.

For example:

Identity Resolution
      ↓
customer_id established

The underlying identity-resolution evidence may remain available for audit while not being passed into an unrelated enterprise Action.

Intent should therefore remain semantically focused even when Context evolves.

⸻

72. Intent and Enterprise Business State

Intent is not enterprise Business State.

For example:

Intent:
get_account_balance

does not mean:

balance = ₦500,000

The balance belongs to the authoritative enterprise system.

Similarly:

Intent:
create_complaint

does not mean:

case exists

The Case exists only when enterprise execution establishes it.

Therefore:

Intent
   ≠
Business State

⸻

73. Intent and Outcome Integrity

Noema must preserve the difference between:

requested outcome

and:

actual outcome

For example:

Intent:
retrieve_statement

does not establish:

statement retrieved

Only verified execution can establish that Outcome.

This prevents the model from converting Customer expectation into enterprise fact.

⸻

74. Intent Model

Conceptually:

Intent {
    intent_id
    intent_version
    type
    objective
    principal
    target
    parameters
    constraints
    scope
    status
    source
    provenance
    created_at
    updated_at
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

75. Intent Relationships

Intent
   │
   ├── expressed_by → Principal
   ├── derived_from → Customer Request
   ├── targets → Resource
   ├── requires → Context
   ├── supported_by → Evidence
   ├── interpreted_by → Model / Resolver
   ├── evaluated_by → Trust
   ├── constrained_by → Policy
   ├── maps_to → Action
   ├── produces → Execution
   └── results_in → Outcome

These relationships must remain semantically distinct.

In particular:

interpreted_by

does not mean:

authorized_by

and:

maps_to

does not mean:

executed

⸻

76. Reference Intent Flow — Balance Inquiry

"What's my balance?"
        ↓
Customer Request
        ↓
Intent
        ↓
get_account_balance
        ↓
Resolve Principal
        ↓
Resolve Account
        ↓
Trust
        ↓
Policy
        ↓
Action
        ↓
Execute

The Intent establishes:

obtain account balance

It does not establish the balance itself.

⸻

77. Reference Intent Flow — Statement Retrieval

"Show my statement from last month."
        ↓
Customer Request
        ↓
Intent
        ↓
retrieve_statement
        ↓
Resolve Account
        ↓
Resolve Period
        ↓
Trust
        ↓
Policy
        ↓
Action
        ↓
Execute

The period should be normalized before enterprise execution.

⸻

78. Reference Intent Flow — Transaction Search

"Find my Netflix payment from last month."
        ↓
Customer Request
        ↓
Intent
        ↓
search_transactions
        ↓
Resolve Account
        ↓
Resolve Merchant
        ↓
Resolve Period
        ↓
Trust
        ↓
Policy
        ↓
Action
        ↓
Execute

The phrase:

Netflix

is initially Customer-provided semantic information.

It does not automatically establish a canonical enterprise merchant identifier.

⸻

79. Reference Intent Flow — Spending Summary

"How much did I spend last month?"
        ↓
Customer Request
        ↓
Intent
        ↓
get_spending_summary
        ↓
Resolve Account
        ↓
Resolve Period
        ↓
Trust
        ↓
Policy
        ↓
Action
        ↓
Execute

The resulting spending figure is determined from the enterprise data and may be classified as derived information.

⸻

80. Reference Intent Flow — Complaint

"I want to report this transaction."
        ↓
Customer Request
        ↓
Intent
        ↓
create_complaint
        ↓
Resolve Customer
        ↓
Resolve Transaction
        ↓
Establish Complaint Details
        ↓
Trust
        ↓
Policy
        ↓
Action
        ↓
Execute

The Intent establishes the objective:

create complaint

It does not establish:

case created

That belongs to Execution and Outcome.

⸻

81. Intent Invariants

Invariant 1

Intent represents the Customer’s requested objective, not its implementation.

Invariant 2

Intent must remain distinct from the raw Customer Request.

Invariant 3

Intent must remain distinct from Action.

Invariant 4

Intent must remain distinct from Execution.

Invariant 5

Intent must remain distinct from Outcome.

Invariant 6

Intent must remain distinct from enterprise Business State.

Invariant 7

Model-generated Intent is not automatically trusted.

Invariant 8

Model confidence does not constitute authorization.

Invariant 9

Identity and Resource references must be grounded before consequential execution.

Invariant 10

Noema must not resolve materially ambiguous Intent through arbitrary guessing.

Invariant 11

Noema must not invent missing Resource identifiers.

Invariant 12

Missing information may only be defaulted when Policy provides a deterministic basis for doing so.

Invariant 13

Intent parameters and constraints must survive normalization and planning without semantic distortion.

Invariant 14

Temporal expressions must be normalized before downstream systems independently interpret them.

Invariant 15

Intent State must remain separate from Execution State.

Invariant 16

A failed Execution must not rewrite the Customer’s original Intent.

Invariant 17

An Unknown Execution must not rewrite the Customer’s original Intent.

Invariant 18

Compound Intent must preserve its constituent objectives and their relationships.

Invariant 19

Each Action derived from a Compound Intent must maintain its own Execution State.

Invariant 20

Customer corrections must update the relevant Intent rather than silently creating a different objective.

Invariant 21

Customer cancellation must prevent execution where cancellation occurs before the execution boundary.

Invariant 22

Replanning may change execution strategy but must not silently change the requested objective.

Invariant 23

Intent persistence must retain sufficient provenance for reconstruction where required.

Invariant 24

Intent versioning must preserve the semantic representation used for historical execution.

Invariant 25

Intent data must respect Data Boundaries and privacy requirements.

Invariant 26

Enterprise events may change Intent executability but do not redefine the Customer’s original objective.

Invariant 27

The model may interpret natural language but must not bypass Trust or Policy.

Invariant 28

An Intent becomes executable only after required Context, Trust, Policy, and Action requirements are satisfied.

Invariant 29

Ambiguity is a state that must be resolved or preserved—not an invitation to guess.

Invariant 30

A candidate model interpretation must remain distinguishable from a resolved Intent where material resolution is still outstanding.

Invariant 31

User-provided information must not automatically become canonical enterprise data.

Invariant 32

Derived Intent information must remain distinguishable from Customer-provided information where the distinction is consequential.

Invariant 33

Intent must not contain more Customer information than is necessary to represent the requested objective.

Invariant 34

Intent-to-Action mapping must be explicit and must not itself imply execution.

Invariant 35

A valid Intent may remain non-executable when required Context or Preconditions are missing.

Invariant 36

Clarification should obtain only the information required to resolve material ambiguity or incompleteness.

Invariant 37

Conversation history may update an unresolved Intent only where the subsequent Customer input is relevant to that Intent.

Invariant 38

Enterprise authority must not be inferred from the existence of an Intent.

Invariant 39

Intent must preserve sufficient provenance to establish how a consequential interpretation or resolution was produced.

Invariant 40

Noema must not manufacture an Outcome from the existence of an Intent.

Invariant 41

Noema must not promote model-selected Resource identifiers to canonical identifiers without grounding.

Invariant 42

Intent scope must not silently expand during planning or execution.

Invariant 43

Intent components in a Compound Intent must retain their semantic relationship to the original Customer Request.

Invariant 44

Intent must remain stable across execution retries and recovery unless the Customer explicitly changes the objective.

Invariant 45

A change in execution strategy does not constitute a change in Intent.

⸻

82. Final Definition

Intent is the structured, normalized representation of the outcome a Customer is trying to achieve.

Within the Customer Account Inquiry workflow:

CUSTOMER REQUEST
       │
       ▼
  INTERPRETATION
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
  INTENT RESOLUTION
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

The architectural rule is:

Intent defines what the Customer wants, not what Noema will do to achieve it.

Noema may use a probabilistic model to interpret the Customer’s request, but the resulting representation must remain distinguishable from unresolved model hypotheses until the required grounding and resolution occur.

A resolved Intent is still not an authorization, an Action, an execution, or an Outcome.

The semantic chain must remain explicit:

REQUEST
   ≠
INTENT
   ≠
CONTEXT
   ≠
TRUST
   ≠
POLICY
   ≠
ACTION
   ≠
EXECUTION
   ≠
OUTCOME

And the deeper architectural rule is:

Noema must preserve the Customer’s objective while allowing Context, Trust, Policy, Action, execution strategy, and recovery state to evolve around it. Noema must never turn a probabilistic interpretation into an enterprise fact merely because doing so makes the workflow easier to execute.