Outcomes

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/outcomes.md

⸻

1. Definition

An Outcome is the explicit representation of what resulted from an executed Action relative to the Customer’s requested Intent.

Outcome answers:

“What actually happened as a result of the execution?”

Outcome is not the same as:

Intent
Action
Execution State
Enterprise State
Failure
Evidence

The relationship is:

Intent
   ↓
Action
   ↓
Execution
   ↓
Outcome

Outcome describes the result produced by that execution.

⸻

2. Purpose

The purpose of Outcome is to establish a clear, verifiable representation of execution results.

For the Customer Account Inquiry workflow, an Outcome allows Noema to determine whether the Customer’s requested objective was:

satisfied
partially satisfied
not satisfied
not determinable

This distinction is essential because successful execution of an Action does not automatically mean that the Customer’s Intent was satisfied.

⸻

3. Core Principle

Outcome must be grounded in execution evidence.

Noema must not infer successful completion merely because:

the API returned successfully
the model expected success
the request was accepted
the Action was attempted

Instead:

Action
   ↓
Execution
   ↓
Evidence
   ↓
Outcome

The Outcome must reflect what can actually be established.

⸻

4. Outcome vs Execution

Execution describes the process of attempting an Action.

Outcome describes what resulted.

For example:

Action:
get_account_balance
Execution:
completed
Outcome:
balance = ₦250,000

Execution answers:

“Did the execution process complete?”

Outcome answers:

“What did that execution produce?”

⸻

5. Outcome vs Intent

Intent represents the requested objective.

Outcome represents the result relative to that objective.

Example:

Intent:
"How much is in my account?"
Outcome:
balance = ₦250,000

The two must remain distinct.

Intent ≠ Outcome

⸻

6. Outcome vs Enterprise State

Enterprise Business State belongs to the enterprise System of Record.

For example:

Enterprise:
account.balance = ₦250,000

Noema may receive this as the result of an Action.

Noema’s Outcome is:

balance retrieved = ₦250,000

The enterprise system remains authoritative for the underlying account state.

⸻

7. Outcome Categories

The Customer Account Inquiry workflow may produce:

SUCCESS
PARTIAL
FAILED
UNKNOWN
NO_RESULT

These categories describe the ability to establish the requested result.

They must remain semantically distinct.

⸻

8. Successful Outcome

A successful Outcome means the requested objective was satisfied and the expected result was established.

Example:

Intent:
get_account_balance
Outcome:
balance = ₦500,000

Conceptually:

Intent
   ↓
Action
   ↓
Execution
   ↓
Verified Result
   ↓
SUCCESS

⸻

9. Partial Outcome

A Partial Outcome occurs when only part of a Compound Intent is satisfied.

Example:

Intent:
"Show my balance and my transactions."
get_account_balance
    → SUCCESS
search_transactions
    → FAILED

Overall:

PARTIAL

The individual Action Outcomes must remain available.

Noema must not represent the entire request as successful.

⸻

10. Failed Outcome

A Failed Outcome means the requested objective was not achieved and the failure is established.

Example:

Intent:
retrieve_statement
Enterprise:
statement unavailable
Outcome:
FAILED

The associated Failure record should explain why.

Outcome
   ↓
Failure

⸻

11. Unknown Outcome

Unknown means Noema cannot establish whether the requested objective was achieved.

Example:

Intent:
create_complaint
Request:
sent
Response:
timeout
Enterprise state:
not yet verified

The correct result is:

UNKNOWN

not:

FAILED

and not:

SUCCESS

⸻

12. No Result

An Action may execute successfully but produce no matching result.

Example:

Intent:
"Find my Netflix payment."
Execution:
SUCCESS
Search Result:
no matching transaction

The Outcome may be:

NO_RESULT

This is materially different from an execution failure.

The search capability worked; no matching Resource was found.

⸻

13. Empty Result vs Failure

These states must remain distinct.

Search executed
      ↓
No matching transactions
      ↓
NO_RESULT

is different from:

Transaction system unavailable
      ↓
FAILED

The first establishes that no result was found.

The second establishes that the requested search could not be completed.

⸻

14. Outcome Structure

Conceptually:

Outcome {
    outcome_id
    execution_id
    action_id
    status
    result
    evidence
    source
    produced_at
    verified_at
    completeness
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

15. Outcome Status

Outcome status should be machine-readable.

Examples:

SUCCESS
PARTIAL
FAILED
UNKNOWN
NO_RESULT

The status should not depend on natural-language interpretation.

⸻

16. Outcome Payload

The payload contains the result produced by the Action.

For example:

get_account_balance
Outcome:
{
    balance: 250000,
    currency: "NGN"
}

The payload should contain only information necessary to satisfy the Intent and applicable Data Boundaries.

⸻

17. Balance Inquiry Outcome

Example:

Intent:
"What's my balance?"
Action:
get_account_balance
Outcome:
SUCCESS
Result:
balance = ₦250,000
currency = NGN

The value should be grounded in the authoritative enterprise source appropriate for account balance.

⸻

18. Statement Retrieval Outcome

Example:

Intent:
"Show me my statement for August."
Action:
retrieve_statement
Outcome:
SUCCESS
Result:
statement retrieved
period = August

If the enterprise system confirms that no statement exists:

NO_RESULT

If the enterprise system is unavailable:

FAILED

If the request timed out and the state cannot be established:

UNKNOWN

⸻

19. Transaction Search Outcome

Example:

Intent:
"Find my Netflix payment."
Action:
search_transactions
Outcome:
SUCCESS
Result:
matching transaction(s)

If no matching transaction exists:

NO_RESULT

The absence of a transaction must not be represented as a system failure.

⸻

20. Spending Summary Outcome

Example:

Intent:
"How much did I spend last month?"
Action:
get_spending_summary
Outcome:
SUCCESS
Result:
total_spending = ₦850,000
period = July

The aggregation should be grounded in the enterprise transaction data or an explicitly trusted enterprise-derived source.

⸻

21. Complaint Outcome

Complaint creation is a state-changing operation within this reference workflow.

Example:

Intent:
"I want to report this transaction."
Action:
create_complaint
Outcome:
SUCCESS
Result:
case_id = CASE-123
status = OPEN

The Case identifier should be sourced from the enterprise system.

⸻

22. Complaint Unknown Outcome

Example:

create_complaint
      ↓
request sent
      ↓
timeout

If Noema cannot establish whether the Case was created:

UNKNOWN

Noema should reconcile against the authoritative complaint system before retrying or claiming success.

⸻

23. Outcome Verification

Where required, the Outcome should be verified against authoritative enterprise state.

Example:

Action
   ↓
Enterprise System
   ↓
Response
   ↓
Verification
   ↓
Outcome

For consequential Actions, a successful HTTP response alone may be insufficient.

⸻

24. Outcome Evidence

An Outcome should be supported by Evidence.

Examples:

enterprise response
resource identifier
returned data
query result
verification response
enterprise event

Conceptually:

Outcome
   ↓
Evidence
   ↓
Source

This makes the Outcome reconstructable.

⸻

25. Outcome Provenance

Noema should be able to establish:

where the result came from
when it was produced
which Action produced it
which enterprise system supplied it
whether it was verified

Conceptually:

Outcome {
    source
    observed_at
    verified_at
    version
    provenance
}

⸻

26. Outcome Freshness

An Outcome may become stale.

Example:

10:00
balance = ₦500,000
10:10
new transaction occurs
10:15
old Outcome still says ₦500,000

The old Outcome remains a record of what was observed at 10:00.

It should not automatically be treated as current enterprise state.

⸻

27. Outcome Temporal Semantics

Outcome should preserve relevant temporal information.

At minimum, where applicable:

produced_at
observed_at
verified_at

This allows Noema to distinguish:

what happened
when it happened
when Noema learned about it
when Noema verified it

⸻

28. Outcome and Canonical Data

The enterprise System of Record remains authoritative for enterprise Business State.

For example:

Enterprise:
Account.balance = ₦500,000

Noema may produce:

Outcome:
balance retrieved = ₦500,000

The Outcome is an observation/result of execution.

It does not become a competing canonical account state.

⸻

29. Outcome and Context

Outcome may update the Context available to subsequent Actions.

Example:

get_account_balance
      ↓
Outcome:
balance = ₦500,000
      ↓
Context updated

However, the Outcome should not be silently promoted into permanent enterprise truth.

⸻

30. Outcome and Evidence

The relationship is:

Enterprise System
      ↓
Observation
      ↓
Evidence
      ↓
Outcome

Evidence supports the Outcome.

Outcome represents the structured result that Noema exposes to the next stage of the workflow.

⸻

31. Outcome and Trust

Trust determines whether the result is sufficiently reliable for the intended use.

For example:

Outcome:
balance = ₦500,000
Source:
authoritative Ledger
Verified:
yes

provides stronger grounding than:

Outcome:
balance = ₦500,000
Source:
stale cache

Outcome and Trust therefore remain separate concepts.

⸻

32. Outcome and Policy

Policy determines how Noema may use an Outcome.

For example:

Outcome:
balance = ₦500,000

may be sufficient to answer a Customer inquiry.

A different Action may require:

freshness < threshold
authoritative verification
specific version

Therefore:

Outcome
   ↓
Policy
   ↓
Permitted Use

⸻

33. Outcome and Postconditions

A Postcondition establishes whether the expected result of an Action was achieved.

For example:

Action:
create_complaint
Postcondition:
case exists

If the Case is verified:

Outcome:
SUCCESS

If it cannot be verified:

Outcome:
UNKNOWN

The Postcondition therefore contributes directly to Outcome determination.

⸻

34. Outcome and Failure

Failure explains why an Outcome is unsuccessful.

Example:

Outcome:
FAILED
Failure:
STATEMENT_SERVICE_UNAVAILABLE

Failure should not replace the Outcome.

They represent different semantic layers:

Outcome
   ↓
what happened
Failure
   ↓
why it failed

⸻

35. Outcome and Unknown

Unknown represents insufficient evidence to establish the result.

Outcome:
UNKNOWN
Reason:
execution result not established

Unknown should trigger the applicable:

reconciliation
retry
escalation
human intervention

path according to Policy.

⸻

36. Outcome and Compound Intent

A Compound Intent should produce a structured collection of Outcomes.

Example:

Intent:
"Show my balance and my spending summary."
Outcomes:
    get_account_balance
        → SUCCESS
    get_spending_summary
        → SUCCESS

The parent workflow can then derive an overall result.

⸻

37. Aggregate Outcome

An aggregate Outcome summarizes multiple Action Outcomes.

Example:

Action A → SUCCESS
Action B → SUCCESS
Action C → FAILED
Aggregate:
PARTIAL

The aggregate must never erase the underlying Action Outcomes.

⸻

38. Outcome Completeness

An Outcome may be technically successful but incomplete relative to the Intent.

Example:

Intent:
"Show all my transactions for July."
Result:
first 50 transactions

If the enterprise capability returned a paginated result and Noema has not retrieved all required pages, the Outcome may not yet satisfy the Intent.

Completeness must therefore be explicit where relevant.

⸻

39. Pagination

For collection-based Actions:

search_transactions

the Outcome may include:

items
page
page_size
has_more
continuation

Noema must determine whether the Customer requested:

first page
all results
a bounded result set

before treating the Outcome as complete.

⸻

40. Outcome Ordering

For multiple Actions, Outcomes should preserve execution relationships.

Example:

resolve_account
      ↓
get_account_balance
      ↓
search_transactions

Each Outcome should remain associated with its originating Action and execution.

This allows the execution journey to be reconstructed.

⸻

41. Outcome Persistence

Noema may persist Outcomes to support:

auditability
customer history
execution reconstruction
reconciliation
analytics
recovery

Persisted Outcomes should preserve their provenance and temporal semantics.

⸻

42. Outcome Versioning

Outcome schemas and representations may evolve.

Historical Outcomes must remain interpretable according to the schema under which they were created.

Example:

outcome_version = 1

should remain reconstructable even if later versions introduce additional fields.

⸻

43. Outcome and Customer Communication

Customer-facing responses should be generated from the verified Outcome.

Example:

Outcome:
SUCCESS
balance = ₦250,000

Customer response:

Your current balance is ₦250,000.

If:

Outcome:
UNKNOWN

the Customer should not receive a fabricated result.

⸻

44. Outcome Communication for No Result

For:

search_transactions

with no matches:

Outcome:
NO_RESULT

the Customer-facing response should communicate absence of a matching result rather than system failure.

The distinction matters because:

NO_RESULT

means the search completed without finding a match.

⸻

45. Outcome Communication for Failure

If:

Outcome:
FAILED

Noema should communicate the failure accurately without exposing unnecessary internal implementation details.

The response should not imply that the requested result was obtained.

⸻

46. Outcome Communication for Unknown

If:

Outcome:
UNKNOWN

Noema should communicate that the result could not yet be confirmed.

It should not convert uncertainty into:

success

or:

failure

without evidence.

⸻

47. Outcome and Human Intervention

Human intervention may be required when an Outcome cannot be established automatically.

Example:

Outcome:
UNKNOWN
      ↓
Policy
      ↓
Human Intervention

The intervention process may subsequently establish:

SUCCESS
FAILED

or another defined terminal state.

The original Unknown state should remain part of the execution history.

⸻

48. Outcome and Reconciliation

Reconciliation is particularly important when execution produces an Unknown result.

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

The final Outcome reflects the reconciled enterprise state.

The original uncertainty remains auditable.

⸻

49. Outcome and Idempotency

For state-changing Actions, an Unknown Outcome may require idempotency-aware reconciliation before another attempt.

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

⸻

50. Outcome Model

Conceptually:

Outcome {
    outcome_id
    execution_id
    action_id
    action_version
    status
    result
    completeness
    source
    evidence
    produced_at
    observed_at
    verified_at
    provenance
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

51. Outcome Relationships

Outcome
   │
   ├── produced_by → Execution
   ├── corresponds_to → Intent
   ├── represents → Result
   ├── supported_by → Evidence
   ├── sourced_from → Enterprise System
   ├── verified_by → Postcondition
   ├── constrained_by → Policy
   └── may_trigger → Reconciliation

⸻

52. Reference Outcome Flows

Balance Inquiry

Customer Request
      ↓
Intent
      ↓
get_account_balance
      ↓
Enterprise Ledger
      ↓
Verified Balance
      ↓
SUCCESS

Statement Retrieval

Customer Request
      ↓
Intent
      ↓
retrieve_statement
      ↓
Statement System
      ↓
Statement Found
      ↓
SUCCESS

Transaction Search

Customer Request
      ↓
Intent
      ↓
search_transactions
      ↓
Transaction System
      ↓
No Matching Transaction
      ↓
NO_RESULT

Spending Summary

Customer Request
      ↓
Intent
      ↓
get_spending_summary
      ↓
Transaction Data
      ↓
Verified Summary
      ↓
SUCCESS

Complaint Creation

Customer Request
      ↓
Intent
      ↓
create_complaint
      ↓
Complaint System
      ↓
Case Created
      ↓
Verified Case
      ↓
SUCCESS

⸻

53. Outcome Invariants

Invariant 1

Outcome must represent what resulted from execution relative to the Intent.

Invariant 2

Outcome must remain distinct from Intent.

Invariant 3

Outcome must remain distinct from Action.

Invariant 4

Outcome must remain distinct from Execution State.

Invariant 5

Outcome must be grounded in execution evidence.

Invariant 6

Successful transport does not automatically establish successful Business Outcome.

Invariant 7

A successful Action may still produce NO_RESULT.

Invariant 8

NO_RESULT must remain distinct from FAILURE.

Invariant 9

UNKNOWN must remain distinct from FAILURE.

Invariant 10

Unknown must not be converted into success or failure without sufficient evidence.

Invariant 11

Failed Outcomes should retain the associated Failure classification.

Invariant 12

Compound Intents must preserve individual Action Outcomes.

Invariant 13

Aggregate Outcomes must not erase constituent Outcomes.

Invariant 14

Outcome completeness must be explicit where the requested result may be partial or paginated.

Invariant 15

Outcome must preserve sufficient provenance to establish its source.

Invariant 16

Outcome temporal information must be preserved where relevant.

Invariant 17

Outcome must not become competing canonical enterprise Business State.

Invariant 18

Enterprise Systems remain authoritative for the enterprise state represented by an Outcome.

Invariant 19

Outcome freshness must be distinguished from enterprise authority.

Invariant 20

Customer-facing responses must reflect the verified Outcome.

Invariant 21

The model may explain an Outcome but must not fabricate one.

Invariant 22

State-changing Actions with Unknown Outcomes must consider reconciliation and idempotency before retry.

Invariant 23

Outcome data must respect Data Boundaries and privacy requirements.

Invariant 24

Human intervention may resolve an Unknown Outcome, but the original uncertainty must remain auditable.

Invariant 25

Noema must never manufacture an Outcome merely to satisfy the Customer’s requested Intent.

⸻

54. Final Definition

Outcome is the evidence-grounded representation of what resulted from executing an Action in relation to the Customer’s Intent.

The fundamental relationship is:

CUSTOMER REQUEST
       ↓
     INTENT
       ↓
     ACTION
       ↓
   EXECUTION
       ↓
    EVIDENCE
       ↓
    OUTCOME
       │
       ├── SUCCESS
       ├── PARTIAL
       ├── NO_RESULT
       ├── FAILED
       └── UNKNOWN

And the architectural rule is:

Noema must represent Outcomes according to what execution evidence establishes. Success must be verified, failure must be classified, no-result must remain distinct from failure, and uncertainty must remain explicitly unknown until sufficient evidence establishes the actual result.