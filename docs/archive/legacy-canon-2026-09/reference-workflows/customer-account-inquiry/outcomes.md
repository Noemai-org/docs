Outcomes

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/outcomes.md

⸻

1. Definition

An Outcome is the explicit, evidence-grounded representation of what resulted from an executed Action relative to the Customer’s requested Intent.

Outcome answers:

“What can Noema establish as having resulted from the execution?”

Outcome is not the same as:

* Intent
* Context
* Trust
* Policy
* Action
* Execution
* Execution State
* Enterprise State
* Evidence
* Failure

The relationship is:

Intent
   ↓
Action
   ↓
Execution
   ↓
Evidence
   ↓
Outcome

Outcome describes the established result of execution in relation to the requested Intent.

⸻

2. Purpose

The purpose of Outcome is to establish a clear, structured, and verifiable representation of what resulted from an Action.

For the Customer Account Inquiry workflow, an Outcome allows Noema to determine whether the Customer’s requested objective was:

* satisfied
* partially satisfied
* not satisfied
* not found
* not yet determinable

This distinction is essential because successful execution of an Action does not automatically mean that the Customer’s Intent was satisfied.

⸻

3. Core Principle

Outcome must be grounded in execution Evidence.

Noema must not infer successful completion merely because:

* the API returned successfully
* the model expected success
* the request was accepted
* the Action was attempted
* a transport-level response was received

Instead:

Action
   ↓
Execution
   ↓
Evidence
   ↓
Verification where required
   ↓
Outcome

The Outcome must reflect what execution evidence actually establishes.

The model may explain an established Outcome, but it must not manufacture one.

⸻

4. Outcome vs Intent

Intent represents what the Customer wants to accomplish.

Outcome represents what resulted from executing an Action in relation to that Intent.

Example:

Intent:
"How much is in my account?"
Outcome:
balance = ₦250,000

The two must remain distinct.

Intent ≠ Outcome

A failed or unknown execution does not rewrite the original Intent.

⸻

5. Outcome vs Action

An Action represents an executable capability.

An Outcome represents what that Action produced.

Example:

Action:
get_account_balance
Outcome:
balance = ₦250,000
currency = NGN

Therefore:

Action
   ↓
Execution
   ↓
Outcome

The Outcome must remain associated with the Action that produced it.

⸻

6. Outcome vs Execution

Execution describes the process of attempting or performing an Action.

Outcome describes what resulted.

For example:

Action:
get_account_balance
Execution:
completed
Outcome:
balance = ₦250,000

Execution answers:

“What happened during the execution process?”

Outcome answers:

“What result was established by that execution?”

Execution State and Outcome Status must therefore remain distinct.

⸻

7. Outcome vs Enterprise State

Enterprise Business State belongs to the authoritative enterprise System of Record.

For example:

Enterprise:
account.balance = ₦250,000

Noema may receive this value through an Action and produce:

Outcome:
balance retrieved = ₦250,000

The Outcome is an observation/result of execution.

It does not become a competing canonical representation of the underlying enterprise state.

Enterprise State
      ↓
Observation
      ↓
Evidence
      ↓
Outcome

The enterprise system remains authoritative for the underlying Business State.

⸻

8. Outcome Categories

The Customer Account Inquiry workflow may produce the following Outcome statuses:

SUCCESS
PARTIAL
NO_RESULT
FAILED
UNKNOWN

These statuses must remain semantically distinct.

They should be machine-readable and must not depend on natural-language interpretation.

⸻

9. Successful Outcome

A successful Outcome means that the requested objective was satisfied and the expected result was established by sufficient Evidence.

Example:

Intent:
get_account_balance
Action:
get_account_balance
Outcome:
SUCCESS
Result:
balance = ₦500,000

Conceptually:

Intent
   ↓
Action
   ↓
Execution
   ↓
Evidence
   ↓
Verified Result
   ↓
SUCCESS

⸻

10. Partial Outcome

A Partial Outcome occurs when a Compound Intent contains multiple executable requirements and only some are successfully satisfied.

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

Noema must not represent the entire request as:

SUCCESS

when one or more required components were not satisfied.

Likewise, the aggregate Outcome must not erase the constituent Action Outcomes.

⸻

11. Failed Outcome

A Failed Outcome means that the requested objective was not achieved and the unsuccessful execution condition is established.

Example:

Intent:
retrieve_statement
Enterprise:
statement unavailable
Outcome:
FAILED

The associated Failure record should establish why the Outcome failed.

Outcome
   ↓
FAILED
   ↓
Failure

Failure and Outcome represent different semantic layers:

Outcome
   ↓
what resulted
Failure
   ↓
why execution failed

⸻

12. Unknown Outcome

Unknown means that Noema cannot establish whether the requested objective was achieved.

Example:

Intent:
create_complaint
Request:
sent
Response:
timeout
Enterprise state:
not yet verified

The correct Outcome is:

UNKNOWN

Noema must not convert the Unknown state into:

FAILED

or:

SUCCESS

without sufficient Evidence.

Unknown is therefore not equivalent to Failure.

UNKNOWN ≠ FAILED

⸻

13. No Result

An Action may execute successfully but establish that no matching result exists.

Example:

Intent:
"Find my Netflix payment."
Execution:
SUCCESS
Search Result:
no matching transaction

The Outcome may be:

NO_RESULT

This is materially different from an execution Failure.

The search capability worked and established that no matching Resource was found.

⸻

14. Empty Result vs Failure

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

The first establishes the absence of a matching result.

The second establishes that the requested operation was not successfully completed.

Therefore:

NO_RESULT ≠ FAILED

⸻

15. Outcome Structure

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

16. Outcome Status

Outcome status should be stable and machine-readable.

The reference statuses are:

SUCCESS
PARTIAL
NO_RESULT
FAILED
UNKNOWN

Status must be determined from execution semantics and Evidence rather than from model interpretation.

⸻

17. Outcome Payload

The Outcome payload contains the result produced or established by the Action.

For example:

get_account_balance
Outcome:
{
    balance: 250000,
    currency: "NGN"
}

The payload should contain only information necessary to satisfy the Intent and applicable Data Boundaries.

Noema should not copy unrelated enterprise data into the Outcome merely because it was present in an enterprise response.

⸻

18. Balance Inquiry Outcome

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

The Outcome represents the balance retrieved through the execution.

It does not become a new canonical account state owned by Noema.

⸻

19. Statement Retrieval Outcome

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

If the enterprise system definitively rejects or cannot complete the requested operation:

FAILED

If the request times out and the resulting enterprise state cannot be established:

UNKNOWN

The classification must follow the available execution Evidence.

⸻

20. Transaction Search Outcome

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

The absence of a transaction must not be represented as a system Failure.

If the Transaction System cannot perform the search and the unsuccessful execution is established:

FAILED

If the result cannot be established because execution state is uncertain:

UNKNOWN

⸻

21. Spending Summary Outcome

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

The aggregation should be grounded in authoritative enterprise transaction data or an explicitly trusted enterprise-derived source.

The Outcome must preserve the period and scope to which the result applies.

⸻

22. Complaint Outcome

Complaint creation is a state-changing Action within this reference workflow.

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

The Case identifier should be sourced from the enterprise complaint system.

Where required, successful completion should include verification of the expected Postcondition.

⸻

23. Complaint Unknown Outcome

Example:

create_complaint
      ↓
request sent
      ↓
timeout

If Noema cannot establish whether the Case was created:

UNKNOWN

Noema should reconcile against the authoritative complaint system before:

* retrying
* creating another Case
* claiming success
* claiming failure

The original Unknown state must remain auditable.

⸻

24. Outcome Verification

Where required by Action semantics, the Outcome must be verified against authoritative enterprise state.

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

For consequential Actions, a successful transport response alone may be insufficient.

Example:

HTTP 200
      ↓
expected case_id absent
      ↓
Postcondition not established
      ↓
UNKNOWN / VERIFICATION_FAILED

The exact resulting state must follow the Action Contract and Policy.

⸻

25. Transport Success vs Business Outcome

Transport success does not automatically establish Business Success.

Example:

HTTP 200
{
    status: "REJECTED"
}

The enterprise capability successfully responded, but the requested Business Action did not succeed.

Therefore:

Transport Success
      ≠
Business Success

The Outcome must represent the semantic result established by the enterprise response.

⸻

26. Outcome Evidence

An Outcome should be supported by relevant Evidence.

Examples include:

* enterprise response
* enterprise resource identifier
* returned data
* query result
* verification response
* enterprise event
* postcondition verification

Conceptually:

Outcome
   ↓
Evidence
   ↓
Source

Evidence must be sufficient to support the Outcome being asserted.

⸻

27. Outcome Provenance

Noema should be able to establish:

* where the result came from
* when it was produced
* which Action produced it
* which Execution produced it
* which enterprise system supplied it
* whether it was verified
* which version of the Action was executed

Conceptually:

Outcome {
    source
    observed_at
    verified_at
    version
    provenance
}

Outcome provenance should support reconstruction of consequential execution.

⸻

28. Outcome Temporal Semantics

Outcome should preserve relevant temporal information.

Where applicable:

produced_at
observed_at
verified_at

These allow Noema to distinguish:

what was observed
when it was produced
when Noema received it
when it was verified

Temporal information must not be discarded merely because the Customer-facing response does not expose it.

⸻

29. Outcome Freshness

An Outcome may become stale without becoming invalid as a historical observation.

Example:

10:00
balance = ₦500,000
10:10
new transaction occurs
10:15
old Outcome:
balance = ₦500,000

The Outcome remains a record of what was observed at 10:00.

It must not automatically be treated as the current enterprise state at 10:15.

Therefore:

Outcome Freshness
      ≠
Enterprise Authority

⸻

30. Outcome and Canonical Data

The enterprise System of Record remains authoritative for enterprise Business State.

For example:

Enterprise:
Account.balance = ₦500,000

Noema may produce:

Outcome:
balance retrieved = ₦500,000

The Outcome is an execution result or observation.

It does not become competing canonical enterprise Business State.

⸻

31. Outcome and Context

An Outcome may update the Context available to subsequent Actions.

Example:

get_account_balance
      ↓
Outcome:
balance = ₦500,000
      ↓
Context updated

However, the Outcome should not be silently promoted into permanent enterprise truth.

A derived Context value must retain appropriate provenance and temporal semantics where it may influence subsequent execution.

⸻

32. Outcome and Trust

Trust and Outcome are separate concepts.

Outcome establishes what execution produced.

Trust determines whether the result is sufficiently grounded and reliable for the intended use.

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

The Outcome therefore does not eliminate the need for Trust evaluation where Policy requires it.

⸻

33. Outcome and Policy

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

An Outcome being recorded does not automatically authorize every possible downstream use of its data.

⸻

34. Outcome and Postconditions

A Postcondition establishes whether the expected result of an Action was achieved.

For example:

Action:
create_complaint
Postcondition:
case exists

If the Case is verified:

Outcome:
SUCCESS

If the Case cannot be established:

Outcome:
UNKNOWN

The Postcondition therefore contributes directly to Outcome determination where required.

⸻

35. Outcome and Failure

Failure explains an established unsuccessful execution condition.

Example:

Outcome:
FAILED
Failure:
STATEMENT_SERVICE_UNAVAILABLE

They represent different semantic layers:

Outcome
   ↓
what resulted
Failure
   ↓
why the requested execution failed

A Failed Outcome should retain its associated Failure classification and evidence.

⸻

36. Outcome and Unknown

Unknown represents insufficient Evidence to establish the requested result.

Example:

Outcome:
UNKNOWN
Reason:
execution result not established

Unknown may trigger:

* reconciliation
* retry
* escalation
* human intervention

according to Action semantics and Policy.

Noema must not convert Unknown into a definitive Success or Failure merely to complete the conversation.

⸻

37. Outcome and Compound Intent

A Compound Intent should produce a structured collection of Action Outcomes.

Example:

Intent:
"Show my balance and my spending summary."
Outcomes:
get_account_balance
    → SUCCESS
get_spending_summary
    → SUCCESS

The parent workflow may derive an aggregate Outcome from these constituent Outcomes.

The constituent Outcomes must remain independently addressable.

⸻

38. Aggregate Outcome

An aggregate Outcome summarizes multiple Action Outcomes.

Example:

Action A → SUCCESS
Action B → SUCCESS
Action C → FAILED
Aggregate:
PARTIAL

The aggregate must not erase the underlying Action Outcomes.

The aggregate is a summary of the execution set, not a replacement for its constituent records.

⸻

39. Outcome Completeness

An Outcome may be technically successful but incomplete relative to the Customer’s Intent.

Example:

Intent:
"Show all my transactions for July."
Result:
first 50 transactions

If the enterprise capability returned a paginated result and Noema has not retrieved all required pages, the Outcome may not yet satisfy the Intent.

Therefore:

Execution Success
      ≠
Intent Satisfaction

where the requested result is incomplete.

Completeness must be explicit where relevant.

⸻

40. Pagination

For collection-based Actions such as:

search_transactions

the Outcome may include:

items
page
page_size
has_more
continuation

Noema must determine whether the Customer requested:

* the first page
* all results
* a bounded result set

before treating the Outcome as complete.

Pagination state should remain associated with the Outcome where additional execution is required to satisfy the Intent.

⸻

41. Outcome Ordering and Execution Relationships

For multiple Actions, Outcomes should preserve their execution relationships.

Example:

resolve_account
      ↓
get_account_balance
      ↓
search_transactions

Each Outcome should remain associated with its originating Action and Execution.

This allows the execution journey and dependencies to be reconstructed.

⸻

42. Outcome Persistence

Noema may persist Outcomes to support:

* auditability
* customer history
* execution reconstruction
* reconciliation
* analytics
* recovery

Persisted Outcomes should preserve their provenance and temporal semantics.

Persistence does not make an Outcome permanent enterprise truth.

⸻

43. Outcome Versioning

Outcome schemas and representations may evolve.

Historical Outcomes must remain interpretable according to the schema under which they were created.

Example:

outcome_version = 1

must remain reconstructable even if later versions introduce additional fields.

Changes to Outcome representation must not silently reinterpret historical execution results.

⸻

44. Outcome and Data Boundaries

Outcome data must respect applicable enterprise Data Boundaries.

Only information necessary for the requested objective and permitted downstream use should be retained or exposed.

For example:

Intent:
search_transactions

does not justify copying unrelated Customer profile information into the Outcome.

Enterprise responses should be minimized before becoming persistent Outcome data where appropriate.

⸻

45. Outcome and Privacy

Natural-language requests and enterprise responses may contain sensitive information.

Noema should apply applicable:

* minimization
* retention
* access control
* redaction
* purpose limitation

to persisted Outcomes and associated Evidence.

The Outcome should contain only information necessary for its semantic purpose.

⸻

46. Outcome and Customer Communication

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

the Customer must not receive a fabricated result.

Likewise, a Failed Outcome must not be communicated as though the requested operation succeeded.

⸻

47. Outcome Communication for No Result

For:

search_transactions

with no matches:

Outcome:
NO_RESULT

the Customer-facing response should communicate that no matching result was found.

It should not describe the situation as a system failure.

The distinction is:

NO_RESULT
=
search completed and no match was established
FAILED
=
requested operation was not successfully completed

⸻

48. Outcome Communication for Failure

If:

Outcome:
FAILED

Noema should communicate the failure accurately without exposing unnecessary internal implementation details.

The response should not imply that the requested result was obtained.

For example:

The statement could not be retrieved right now.

is materially different from claiming that a statement was retrieved.

⸻

49. Outcome Communication for Unknown

If:

Outcome:
UNKNOWN

Noema should communicate that the result could not yet be confirmed.

It should not convert uncertainty into:

success

or:

failure

without sufficient Evidence.

Where appropriate, the response should indicate that Noema is verifying or reconciling the result.

⸻

50. Outcome and Human Intervention

Human intervention may be required when an Outcome cannot be established automatically.

Example:

Outcome:
UNKNOWN
      ↓
Policy
      ↓
Human Intervention

The intervention may subsequently establish:

SUCCESS

or:

FAILED

or another defined terminal state.

The original Unknown state must remain part of the execution history.

⸻

51. Outcome and Reconciliation

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

Reconciliation must not erase the fact that the initial execution result was Unknown.

⸻

52. Outcome and Idempotency

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

The decision to retry must follow the Action’s semantics and Policy.

⸻

53. Outcome and Failure Recovery

A Failed Outcome may enter a Policy-governed recovery path.

Conceptually:

Outcome
   ↓
FAILED
   ↓
Failure Classification
   ↓
Policy
   ├── Retry
   ├── Recover
   ├── Reconcile
   ├── Escalate
   └── Reject

The recovery path must not be selected solely through model intuition.

For Unknown Outcomes:

UNKNOWN
   ↓
Policy
   ├── Reconcile
   ├── Retry
   ├── Escalate
   └── Human Intervention

The applicable path depends on the Action semantics and Policy.

⸻

54. Outcome and Blocked Actions

A downstream Action that was never executed because of an upstream failure must not receive an Outcome equivalent to a failed execution.

Example:

resolve_account
      ↓
FAILED
      ↓
search_transactions
      ↓
BLOCKED

The downstream Action did not itself execute and therefore should not be represented as:

FAILED

Its execution state must remain distinguishable from the Outcome of an Action that actually ran.

⸻

55. Outcome and Failure Cascades

Noema should prevent one root failure from being incorrectly represented as multiple independent execution failures.

Example:

Transaction System unavailable
        ↓
search_transactions
        ↓
FAILED
        ↓
get_spending_summary
        ↓
BLOCKED

The root dependency failure should remain identifiable.

Aggregate and downstream records should preserve the causal relationship.

⸻

56. Outcome and Enterprise Events

Enterprise events may affect whether an Outcome remains current or whether subsequent Actions can rely on it.

Example:

10:00
Outcome:
balance = ₦500,000
10:10
Enterprise Event:
new transaction

The existing Outcome remains a record of the 10:00 observation.

It should not automatically be treated as the current enterprise state after the event.

A subsequent Action may be required when current state is required by Intent or Policy.

⸻

57. Outcome and Customer Corrections

If the Customer corrects an Intent before or during execution, the resulting Outcome must remain associated with the Intent version or Action execution that produced it.

Example:

Customer:
"Show my transactions."
Clarification:
"Which account?"
Customer:
"My savings account."

The resulting Outcome should correspond to the updated Intent and resolved target.

Historical Outcomes from prior executions must not silently be reinterpreted as results for the corrected Intent.

⸻

58. Outcome and Cancellation

If a Customer cancels an Intent before execution:

Intent
   ↓
CANCELLED

no new execution should occur for that cancelled Intent unless a separate valid request is received.

If an Action has already executed, cancellation does not erase the resulting Execution or Outcome.

The execution history must remain auditable.

⸻

59. Outcome and Replanning

Replanning may change how Noema executes an Intent without changing the semantic meaning of the resulting Outcome.

Example:

Intent:
retrieve_statement
Original plan
      ↓
changed Context
      ↓
Replanned Action
      ↓
Execution
      ↓
Outcome

The Outcome must remain associated with the Intent and actual Action execution that produced it.

Replanning must not silently transform an unsuccessful result into a successful one.

⸻

60. Outcome and Intent Lifecycle

Outcome occurs downstream of the Intent lifecycle.

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
 ↓
EXECUTION
 ↓
OUTCOME

Intent State and Outcome Status remain separate dimensions.

For example:

Intent:
RESOLVED
Execution:
FAILED
Outcome:
FAILED

or:

Intent:
RESOLVED
Execution:
UNKNOWN
Outcome:
UNKNOWN

These are valid combinations.

⸻

61. Outcome Provenance and Model Separation

The model may participate in producing Customer-facing language from a structured Outcome.

The architecture should remain:

Execution
   ↓
Evidence
   ↓
Outcome Classification
   ↓
Structured Outcome
   ↓
Model Explanation

not:

Execution
   ↓
Model
   ↓
invented Outcome

The model must not independently manufacture:

* success
* failure
* no result
* unknown
* verification

without the underlying execution semantics and Evidence establishing them.

⸻

62. Outcome Model

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

63. Outcome Relationships

Outcome
   │
   ├── produced_by → Execution
   ├── corresponds_to → Intent
   ├── represents → Result
   ├── supported_by → Evidence
   ├── sourced_from → Enterprise System
   ├── verified_by → Postcondition
   ├── constrained_by → Policy
   ├── may_trigger → Reconciliation
   ├── may_trigger → Recovery
   └── may_require → Human Intervention

These relationships should preserve the distinction between what happened, why it happened, where it came from, and what Noema is permitted to do with it.

⸻

64. Reference Outcome Flows

Balance Inquiry

Customer Request
      ↓
Intent
      ↓
get_account_balance
      ↓
Enterprise Ledger
      ↓
Evidence
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
Evidence
      ↓
Statement Found
      ↓
SUCCESS

If no statement exists:

Statement System
      ↓
No Statement
      ↓
NO_RESULT

If the operation fails:

Statement System
      ↓
Established Failure
      ↓
FAILED

If the result cannot be established:

Statement System
      ↓
Uncertain Execution Result
      ↓
UNKNOWN

Transaction Search

Customer Request
      ↓
Intent
      ↓
search_transactions
      ↓
Transaction System
      ↓
Evidence
      ↓
Matching Transaction
      ↓
SUCCESS

No matching transaction:

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
Verification
      ↓
SUCCESS

Unknown:

create_complaint
      ↓
request sent
      ↓
timeout
      ↓
UNKNOWN
      ↓
reconciliation
      ↓
enterprise state established
      ↓
SUCCESS / FAILED

⸻

65. Outcome State Model

Conceptually:

                 EXECUTION
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       SUCCESS    FAILURE   UNKNOWN
          │         │         │
          │         │         └──→ Reconcile /
          │         │              Retry /
          │         │              Escalate
          │         │
          ↓         ↓
       OUTCOME   OUTCOME
          │         │
          └────┬────┘
               ↓
       Intent Satisfaction
               │
       ┌───────┼────────┐
       ↓       ↓        ↓
    SUCCESS  NO_RESULT PARTIAL

The precise transition depends on Action semantics, Evidence, completeness, and Policy.

⸻

66. Outcome Lifecycle

Action
   ↓
Execution
   ↓
Evidence Collected
   ↓
Result Evaluated
   ↓
Postcondition Verified Where Required
   ↓
Outcome Classified
   ↓
Outcome Recorded
   ↓
Policy / Downstream Use
   ├── Communicate
   ├── Continue
   ├── Reconcile
   ├── Recover
   ├── Escalate
   └── Human Intervention

The lifecycle must remain deterministic and auditable.

⸻

67. Outcome Determination Rules

Outcome determination should follow explicit semantic rules.

Conceptually:

Execution
   ↓
Did execution establish a result?
   │
   ├── No
   │    ↓
   │   Is the result definitively unsuccessful?
   │        ├── Yes → FAILED
   │        └── No  → UNKNOWN
   │
   └── Yes
        ↓
   Was the requested result established?
        │
        ├── Yes → SUCCESS
        │
        └── No
             ↓
       Was absence of a matching result established?
             ├── Yes → NO_RESULT
             └── No  → FAILED / UNKNOWN

For Compound Intents:

Action Outcomes
      ↓
Aggregate
      ├── all satisfied → SUCCESS
      ├── none satisfied → applicable failure/no-result/unknown
      └── mixed → PARTIAL

The exact classification remains subject to Action semantics and Policy.

⸻

68. Outcome Invariants

Invariant 1

Outcome must represent what resulted from execution relative to the Intent.

Invariant 2

Outcome must remain distinct from Intent.

Invariant 3

Outcome must remain distinct from Action.

Invariant 4

Outcome must remain distinct from Execution State.

Invariant 5

Outcome must be grounded in execution Evidence.

Invariant 6

Successful transport does not automatically establish successful Business Outcome.

Invariant 7

A successful Action may still produce NO_RESULT.

Invariant 8

NO_RESULT must remain distinct from FAILURE.

Invariant 9

UNKNOWN must remain distinct from FAILURE.

Invariant 10

Unknown must not be converted into Success or Failure without sufficient Evidence.

Invariant 11

Failed Outcomes should retain the associated Failure classification and supporting Evidence.

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

Downstream Actions blocked by an upstream failure must remain distinguishable from Actions that actually failed.

Invariant 26

Outcome classification must preserve causal relationships between dependencies, executions, failures, and downstream blocked Actions.

Invariant 27

A transport-level response must not be treated as sufficient evidence of Business Success where Action semantics require verification.

Invariant 28

Postcondition failure must prevent an Action from being represented as successfully completed when the expected postcondition cannot be established.

Invariant 29

An Outcome must remain associated with the specific Execution and Action version that produced it.

Invariant 30

Historical Outcomes must remain interpretable according to the semantic representation under which they were created.

Invariant 31

An Outcome must not be silently reinterpreted as the result of a later corrected Intent or different Resource.

Invariant 32

An Outcome must preserve the temporal distinction between when a result was produced, observed, and verified where applicable.

Invariant 33

Outcome payloads must contain only information necessary for the requested objective and permitted downstream use.

Invariant 34

An Outcome must not be created merely because the Customer expects or requests a particular result.

Invariant 35

Recovery and downstream use of an Outcome must follow explicit Action semantics and Policy rather than probabilistic model judgment.

Invariant 36

A Customer-facing explanation must not contain claims stronger than the Outcome and its supporting Evidence establish.

⸻

69. Final Definition

Outcome is the evidence-grounded representation of what resulted from executing an Action in relation to the Customer’s Intent.

The fundamental relationship is:

CUSTOMER REQUEST
       ↓
     INTENT
       ↓
     CONTEXT
       ↓
      TRUST
       ↓
     POLICY
       ↓
     ACTION
       ↓
   EXECUTION
       ↓
    EVIDENCE
       ↓
   VERIFICATION
       ↓
    OUTCOME
       │
       ├── SUCCESS
       ├── PARTIAL
       ├── NO_RESULT
       ├── FAILED
       └── UNKNOWN

And the architectural rule is:

Noema must represent Outcomes according to what execution Evidence establishes. Success must be verified where required, Failure must be classified from established execution conditions, NO_RESULT must remain distinct from Failure, and uncertainty must remain explicitly UNKNOWN until sufficient Evidence establishes the actual result. Outcomes must remain distinct from canonical enterprise state, preserve provenance and temporal semantics, and provide the authoritative basis for Customer-facing claims about what Noema actually established.