Outcome Engine

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/outcome-engine.md

⸻

1. Definition

The Outcome Engine is the Noema architectural component responsible for determining, recording, and interpreting what happened after an Intent was submitted for execution.

The Outcome Engine establishes the boundary between:

* execution activity
* observed execution results
* business-state changes
* expected outcomes
* actual outcomes
* success, failure, partial completion, and unknown results

Its purpose is not to execute Actions.

Its purpose is to establish:

What happened as a result of attempting to execute this Intent?

The Outcome Engine therefore operates after, and in coordination with, the Execution layer.

⸻

2. Core Principle

Execution is not outcome.

A system may accept an Action without successfully producing the intended business result.

Therefore:

Trusted Intent
      ↓
Execution Contract
      ↓
Execution
      ↓
Observed Result
      ↓
Outcome Determination

Noema must not infer successful completion merely because:

* an execution request was sent
* a consumer accepted a contract
* an API returned successfully
* a workflow reached its final step
* an external system returned an ambiguous response

The outcome must be established from explicit evidence.

⸻

3. Outcome Engine Position

The canonical architectural relationship is:

Intent
   ↓
Resolution
   ↓
Validation
   ↓
Trust
   ↓
Planning
   ↓
Execution Contract
   ↓
Execution
   ↓
Outcome Engine
   ↓
Outcome

The Outcome Engine consumes execution evidence and determines the resulting outcome state.

It does not replace the authoritative system of record.

⸻

4. What the Outcome Engine Owns

The Outcome Engine owns Noema’s representation of execution outcome.

This includes:

* expected outcome
* observed execution result
* outcome status
* outcome evidence
* outcome provenance
* outcome verification
* partial completion state
* failure classification
* unknown outcome state
* outcome timestamps
* relationship between execution and outcome
* outcome history

Noema does not thereby become the authoritative owner of the underlying business state.

For example:

Payment System
    ↓
Authoritative payment state
Noema
    ↓
Observed and recorded outcome

Noema records what it established happened.

The external system remains authoritative for its domain state.

⸻

5. Outcome vs Execution

Execution answers:

Did the execution attempt occur?

Outcome answers:

What resulted from that execution?

These are different questions.

Example:

Execution:
API request accepted
Outcome:
Payment status remains unknown

Another example:

Execution:
Transfer request submitted
Outcome:
Transfer completed

Therefore:

EXECUTED ≠ SUCCESSFUL

⸻

6. Outcome vs Intent

The intended result and actual result must remain distinct.

Example:

Intent:

Transfer ₦100,000 to Account B.

Expected Outcome:

Account B receives ₦100,000

Observed Outcome:

Transfer rejected by payment system

Noema must preserve both.

It must not rewrite the Intent merely because execution produced a different result.

⸻

7. Expected Outcome

An Intent or Action Contract may define an expected outcome.

Conceptually:

Expected Outcome
├── state change
├── affected resource
├── expected value
├── expected conditions
├── postconditions
└── verification requirements

The expected outcome establishes what successful execution should produce.

It is not itself evidence that the result occurred.

⸻

8. Observed Outcome

An observed outcome is derived from evidence available after execution.

Evidence may include:

* execution response
* external system response
* resource state
* transaction identifier
* event confirmation
* postcondition check
* consumer acknowledgment
* authoritative system query

The Outcome Engine should distinguish:

Expected
     ≠
Observed

⸻

9. Outcome Verification

Where an Action Contract specifies postconditions, the Outcome Engine should verify them.

Conceptually:

Execution
   ↓
Expected Postconditions
   ↓
Observe Relevant State
   ↓
Compare
   ↓
Outcome

Example:

Expected:

Card status = ACTIVE

Observed:

Card status = ACTIVE

Result:

COMPLETED

If the observed state does not satisfy the postcondition:

Execution occurred
but
Expected outcome not established

The result must not be represented as successful merely because execution returned without an error.

⸻

10. Outcome States

The canonical conceptual outcome states are:

PENDING
COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN
CANCELLED

Implementations may introduce more granular subtypes.

For example:

FAILED_BY_CONSUMER
FAILED_BY_EXTERNAL_SYSTEM
FAILED_POSTCONDITION
UNKNOWN_EXTERNAL_STATE
PARTIAL_EXECUTION
CANCELLED_BY_ACTOR

The exact taxonomy may evolve.

⸻

11. PENDING

PENDING means execution has begun or has been accepted, but the final outcome has not yet been established.

Example:

Execution accepted
      ↓
External processing ongoing
      ↓
PENDING

Pending is not failure.

It is also not success.

⸻

12. COMPLETED

COMPLETED means Noema has sufficient evidence that the expected execution outcome was achieved.

Conceptually:

Execution
   ↓
Expected conditions satisfied
   ↓
COMPLETED

Completion should be supported by explicit evidence.

⸻

13. FAILED

FAILED means the requested execution did not produce the intended result and the failure has been established.

Examples:

* Action rejected
* Required precondition failed
* External system rejected operation
* Execution consumer reported failure
* Postcondition was definitively violated

A failure should include structured reasons where available.

⸻

14. PARTIALLY_COMPLETED

Some Actions may contain multiple independently executable components.

Example:

A → completed
B → failed
C → completed

If the Intent explicitly permits partial execution:

Outcome = PARTIALLY_COMPLETED

Noema must not infer permission for partial completion.

Partial execution semantics must be defined by the Intent or Action Contract.

⸻

15. UNKNOWN

UNKNOWN means Noema cannot establish whether the intended outcome occurred.

Example:

Request submitted
      ↓
Network failure
      ↓
No authoritative response
      ↓
UNKNOWN

The correct representation is not:

FAILED

unless failure has actually been established.

Nor:

COMPLETED

without evidence.

Therefore:

Unknown is a first-class outcome.

⸻

16. CANCELLED

CANCELLED means execution was intentionally terminated before successful completion.

Cancellation may occur because:

* Actor requested cancellation
* policy required cancellation
* execution was revoked where supported
* workflow was terminated
* external system cancelled the operation

Cancellation semantics should distinguish:

Cancellation requested

from:

Cancellation confirmed

where the underlying system supports such a distinction.

⸻

17. Outcome Determination

The Outcome Engine should conceptually perform:

Execution Record
      +
Expected Outcome
      +
Observed Evidence
      +
Postconditions
      ↓
Outcome Evaluation
      ↓
Outcome

The evaluation must be deterministic with respect to the relevant inputs and rules.

⸻

18. Outcome Determination Is Not Model Judgment

An LLM may help interpret unstructured execution responses where necessary.

However, the authoritative outcome should be established through explicit rules and evidence.

The architecture must not rely on:

“The model thinks the operation succeeded.”

Instead:

Execution Evidence
      ↓
Deterministic Outcome Rules
      ↓
Outcome

Where interpretation is genuinely required, the interpreted result should remain distinguishable from authoritative evidence.

⸻

19. Outcome Evidence

Every consequential outcome should have provenance.

Conceptually:

OutcomeEvidence {
    source
    evidence_type
    observed_at
    reference
    authority
    freshness
}

Examples:

Payment Provider
Transaction ID
Status = SETTLED
Observed = 14:32

or:

CRM
Customer Record
Status = ACTIVE
Observed = 09:15

Evidence should be referenced rather than duplicated unnecessarily.

⸻

20. Authoritative Sources

The Outcome Engine must understand the distinction between:

* execution consumer
* authoritative business system
* Noema observation
* derived outcome

For example:

Payment Provider
       ↓
Authoritative payment state
Noema
       ↓
Observes payment state
       ↓
Records outcome

Noema should not claim ownership of a business state merely because it observed it.

⸻

21. Postcondition Verification

Action Contracts may define postconditions.

Example:

Action:
Activate Card
Precondition:
Card exists
Postcondition:
Card.status = ACTIVE

The Outcome Engine may verify:

Card.status

after execution.

If:

ACTIVE

then:

COMPLETED

If:

BLOCKED

then the intended outcome has not been achieved.

⸻

22. Outcome and Business State

Business state may change independently of Noema.

Therefore:

Noema Execution
       ↓
External System
       ↓
Business State

The Outcome Engine observes relevant business state through defined interfaces.

It should not maintain a competing authoritative state merely to simplify outcome determination.

⸻

23. Temporal Outcome Verification

Outcome verification may be asynchronous.

Example:

T1
Execution submitted
T2
Execution accepted
T3
Processing
T4
Business state changed
T5
Outcome verified

Therefore:

Execution Time ≠ Outcome Time

Noema should retain both where relevant.

⸻

24. Eventual Outcomes

Some Actions cannot establish their final outcome immediately.

Example:

Loan application submitted

The immediate result may be:

PENDING

Later:

APPROVED

or:

REJECTED

The Outcome Engine must support asynchronous outcome progression.

⸻

25. Outcome Reconciliation

When execution and business-state observations disagree, Noema may need reconciliation.

Example:

Execution Consumer:
SUCCESS
Authoritative System:
Transaction = FAILED

The Outcome Engine must not silently select one.

The discrepancy should produce an explicit reconciliation state or outcome determination process.

Conceptually:

Execution Evidence
        +
Authoritative State
        ↓
Reconciliation
        ↓
Resolved Outcome

⸻

26. Unknown Outcome Recovery

An unknown outcome may later become known.

Example:

EXECUTION
   ↓
UNKNOWN
   ↓
authoritative lookup
   ↓
COMPLETED

or:

UNKNOWN
   ↓
authoritative lookup
   ↓
FAILED

Therefore:

UNKNOWN

need not be terminal.

⸻

27. Outcome State History

Outcome transitions should be auditable.

Example:

T0:
PENDING
T1:
UNKNOWN
T2:
COMPLETED

This history is important because the final outcome alone does not explain what Noema knew at each point in time.

⸻

28. Outcome Transition Provenance

A transition should record, where applicable:

* previous outcome
* triggering event
* new outcome
* timestamp
* Execution ID
* Intent version
* evaluation ID
* evidence references
* verification result
* reason

Conceptually:

OutcomeTransition {
    previous_state
    event
    new_state
    timestamp
    execution_id
    evidence
    reason
}

⸻

29. Outcome Determinism

Given the same:

* Execution Record
* Expected Outcome
* Evidence
* Postconditions
* Outcome Rules
* Rule Versions

the Outcome Engine should produce the same outcome determination.

Conceptually:

Outcome(
    Execution,
    Expected,
    Evidence,
    Rules
)
=
deterministic result

⸻

30. Outcome Rule Versioning

Outcome rules may evolve.

Therefore an outcome evaluation should identify the relevant:

rule_id
rule_version

This permits historical reconstruction.

A historical outcome should not become inexplicable merely because the current rule set changed.

⸻

31. Consumer Failure vs Business Failure

These should remain distinct.

Example:

Execution Consumer:
timeout

does not necessarily mean:

Business Action:
failed

The request may have reached the external system before the timeout.

Therefore the outcome may initially be:

UNKNOWN

until authoritative state can be established.

This distinction is essential for consequential operations.

⸻

32. Idempotency and Outcomes

Outcome determination must account for idempotency.

Example:

Request A
   ↓
Payment submitted
   ↓
Response lost
   ↓
UNKNOWN

A retry without determining the prior outcome could create duplicate execution.

Therefore:

UNKNOWN

may require reconciliation before another execution attempt is permitted.

The Outcome Engine should expose sufficient state for the Execution layer to apply the Action Contract’s idempotency semantics.

⸻

33. Outcome and Retry

Retry is not equivalent to failure recovery.

A retry may be safe only when:

* the prior execution is known to have failed
* the Action is explicitly retryable
* idempotency semantics permit retry
* relevant conditions remain valid

An unknown outcome must not automatically trigger a retry.

⸻

34. Outcome and Partial Execution

Composite Actions may produce different outcomes per component.

Example:

Component A → COMPLETED
Component B → FAILED
Component C → PENDING

The composite outcome depends on the declared semantics of the Intent and Action Contract.

Noema must not infer:

all-or-nothing

or:

partial success permitted

unless the contract establishes it.

⸻

35. Outcome and Compensation

Some Actions may support compensating Actions.

Example:

A completed
B failed
↓
Compensation required

The Outcome Engine should record that compensation is required or has occurred.

It should not silently reinterpret the original outcome.

Conceptually:

Original Outcome
      ↓
Compensation Requirement
      ↓
Compensation Execution
      ↓
New Outcome

The original execution history remains intact.

⸻

36. Outcome Does Not Rewrite Trust

If an Intent was correctly marked READY and execution later fails, the failure does not retroactively mean:

Trust = invalid

The distinction is:

Trust:
Was execution permitted?
Outcome:
What happened when execution was attempted?

Therefore:

READY
   ↓
EXECUTING
   ↓
FAILED

is a valid lifecycle.

⸻

37. Outcome Does Not Rewrite Validation

Similarly, execution failure does not automatically imply that the original Intent was invalid.

A valid and trusted Intent may encounter:

* external failure
* timeout
* unavailable resource
* changed business state
* consumer failure

Validation and outcome must remain separate.

⸻

38. Outcome and Intent Lifecycle

The broader Intent lifecycle may contain:

RESOLVED
TRUSTED
EXECUTING
COMPLETED
FAILED

The Outcome Engine provides the evidence needed to establish the execution result.

The Intent lifecycle should reference the outcome rather than conflating the two models.

⸻

39. Outcome and Execution Record

The Execution Record establishes what Noema attempted or what the execution consumer reported.

The Outcome Engine determines what that execution resulted in.

Conceptually:

Execution Record
      ↓
Outcome Engine
      ↓
Outcome Record

The two records should remain independently auditable.

⸻

40. Outcome Record

A conceptual Outcome Record may contain:

OutcomeRecord {
    outcome_id
    intent_id
    execution_id
    expected_outcome
    actual_outcome
    status
    evidence
    verified_at
    rule_version
    provenance
}

The exact schema belongs to the implementation specification.

⸻

41. Outcome Correlation

Every outcome should be correlated to the execution and Intent that produced it.

Conceptually:

Intent ID
    │
    ▼
Execution ID
    │
    ▼
Outcome ID

This allows Noema to reconstruct:

What was intended?
What was authorized?
What was executed?
What happened?

⸻

42. Outcome and External Events

External systems may emit events after execution.

Example:

payment.submitted
payment.settled

The Outcome Engine may consume these events to establish the final outcome.

External events should retain:

* source
* event identity
* timestamp
* event version
* correlation identifier
* authority

⸻

43. Duplicate Events

External systems may emit duplicate events.

Outcome processing should therefore be idempotent where the source semantics require it.

The same authoritative event should not produce multiple contradictory outcome transitions merely because it was delivered more than once.

⸻

44. Out-of-Order Events

Events may arrive out of order.

Example:

settled

arrives before:

submitted

The Outcome Engine should use event identity, timestamps, versions, and authoritative state where available rather than assuming message arrival order equals business-state order.

⸻

45. Outcome Freshness

An outcome is based on evidence observed at a particular time.

Therefore Noema should distinguish:

Outcome established at T1

from:

Current business state at T2

A completed outcome does not imply that the resource remains in the same state forever.

⸻

46. Outcome vs Current State

Example:

T1:
Card activation completed.
T2:
Card later suspended.

The outcome of the activation Action remains:

COMPLETED

The current business state is now:

SUSPENDED

These are not contradictory.

Outcome describes what happened to the Action.

Current state describes the resource now.

⸻

47. Outcome Verification Failure

Verification itself may fail.

Example:

Execution completed
      ↓
Postcondition lookup unavailable
      ↓
Outcome cannot be established

The result may be:

UNKNOWN

rather than:

FAILED

unless the business system provides authoritative evidence of failure.

⸻

48. Outcome Escalation

Certain unknown or contradictory outcomes may require human intervention.

Example:

Payment request
   ↓
UNKNOWN
   ↓
Authoritative systems disagree
   ↓
HUMAN_INTERVENTION_REQUIRED

Human intervention should be represented explicitly rather than hidden inside retry behavior.

⸻

49. Outcome Notifications

Outcome changes may emit events such as:

outcome.pending
outcome.completed
outcome.failed
outcome.partial
outcome.unknown
outcome.reconciled

These events may be consumed by:

* workflows
* user interfaces
* audit systems
* monitoring systems
* downstream orchestration

The event vocabulary is illustrative and may evolve.

⸻

50. Outcome Provenance

Outcome provenance should establish:

What happened?
How do we know?
Which system told us?
When did we observe it?
Which rule established the outcome?

Conceptually:

Outcome
   ↓
Evidence
   ↓
Source
   ↓
Observation
   ↓
Rule

This is necessary for auditability and dispute resolution.

⸻

51. Outcome and Auditability

A consequential outcome should be reconstructible after the fact.

An auditor should be able to determine:

1. What was intended?
2. What was authorized?
3. What execution occurred?
4. What evidence was available?
5. What outcome was determined?
6. Which authoritative system supplied the evidence?
7. When was the outcome established?
8. Did the outcome later change?
9. Was reconciliation required?
10. Was human intervention involved?

⸻

52. Outcome Invariants

Invariant 1

Execution does not equal outcome.

Invariant 2

Outcome must be based on explicit evidence.

Invariant 3

Unknown must not be represented as success.

Invariant 4

Unknown must not be represented as failure without evidence.

Invariant 5

Expected outcome and observed outcome must remain distinct.

Invariant 6

Noema does not become the authoritative owner of external business state merely by observing it.

Invariant 7

Outcome determination must be deterministic with respect to its defined inputs and rules.

Invariant 8

Outcome rules must be versionable.

Invariant 9

Outcome transitions must be auditable.

Invariant 10

A successful Trust decision does not guarantee successful execution.

Invariant 11

Execution failure does not retroactively invalidate Trust.

Invariant 12

Execution failure does not automatically invalidate Intent semantics.

Invariant 13

Partial execution must be explicitly permitted by the relevant Intent or Action Contract.

Invariant 14

Unknown outcomes must support reconciliation.

Invariant 15

Outcome describes the result of an Action, not necessarily the current state of the affected resource.

Invariant 16

Noema must not silently convert uncertain execution into a definitive outcome.

⸻

53. Canonical Outcome Flow

              Execution
                  │
                  ▼
          Execution Record
                  │
                  ▼
        Expected Outcome
                  │
                  ▼
        Observed Evidence
                  │
                  ▼
       Postcondition Checks
                  │
                  ▼
         Outcome Evaluation
                  │
       ┌──────────┼───────────┐
       ▼          ▼           ▼
   PENDING    COMPLETED     FAILED
       │
       ├───────────────┐
       ▼               ▼
   UNKNOWN     PARTIALLY_COMPLETED
       │
       ▼
   RECONCILIATION
       │
       ▼
 COMPLETED / FAILED

⸻

54. Relationship to the Trust State Machine

The Trust State Machine determines execution eligibility.

The Outcome Engine determines execution result.

The conceptual relationship is:

Trust
  ↓
READY
  ↓
Execution
  ↓
Outcome

Therefore:

Trust State:
READY
Execution State:
EXECUTING
Outcome:
PENDING

Later:

Outcome:
COMPLETED

or:

Outcome:
FAILED

Trust and Outcome should not be collapsed into one semantic decision.

⸻

55. Relationship to the Execution Planner

The Execution Planner determines how a trusted Intent should be translated into an executable sequence.

The Outcome Engine does not plan the execution.

It evaluates what happened after execution.

Intent
  ↓
Execution Planner
  ↓
Execution Plan
  ↓
Execution
  ↓
Outcome Engine

⸻

56. Relationship to the Execution Record

The Execution Record captures execution activity.

The Outcome Engine consumes that record and associated evidence.

Execution Record
        │
        ├── request
        ├── consumer
        ├── timestamps
        ├── status
        ├── responses
        └── references
                │
                ▼
          Outcome Engine
                │
                ▼
            Outcome

⸻

57. Relationship to Operational Memory

Outcome records become part of Noema’s operational history.

Operational Memory may use outcomes to establish:

* what happened previously
* whether an Intent was completed
* whether reconciliation occurred
* whether an execution remains pending
* what evidence was observed
* what follow-up may be required

Outcome history should remain distinguishable from authoritative business state.

⸻

58. Outcome and Learning

Historical outcomes may provide useful information for future system behavior.

For example:

Repeated external timeout

may inform:

* operational monitoring
* capability health
* retry policy
* planning heuristics
* system diagnostics

However, historical outcome patterns must not silently become authorization.

Outcome history is evidence about what happened previously.

It is not automatically permission for future execution.

⸻

59. Outcome and Idempotent Recovery

For consequential Actions, the Outcome Engine should provide sufficient information to determine whether another execution attempt could create duplication or inconsistency.

Example:

UNKNOWN
+
transaction reference exists

may require reconciliation before retry.

This protects against:

lost response
     ↓
blind retry
     ↓
duplicate Action

⸻

60. Outcome and Compensation

Where a failed composite execution requires compensation, the compensation should be represented as a new explicit Action.

Example:

Original Action
      ↓
PARTIALLY_COMPLETED
      ↓
Compensation Required
      ↓
New Intent / Action
      ↓
Trust
      ↓
Execution
      ↓
New Outcome

The original outcome remains historically accurate.

⸻

61. Outcome State Transition Principle

An outcome state may change only because of:

* a defined execution event
* authoritative external evidence
* postcondition verification
* reconciliation
* explicit cancellation
* deterministic re-evaluation

It must not change because:

* an LLM appears more confident
* a retry occurred without new evidence
* a user expects success
* an execution response merely sounds positive

⸻

62. Canonical Mental Model

The Outcome Engine can be reduced to four questions:

1. Did execution occur?

Execution Record

2. What evidence exists?

Observed Evidence

3. Did the expected postconditions occur?

Verification

4. What outcome can Noema establish?

PENDING
COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN
CANCELLED

⸻

63. Fundamental Boundary

The complete Noema chain is:

Human Intent
      ↓
Meaning
      ↓
Validation
      ↓
Trust
      ↓
Action
      ↓
Execution
      ↓
Outcome

Each stage answers a different question:

Meaning:
What does the Actor intend?
Validation:
Is the Intent well formed and applicable?
Trust:
May the Intent proceed?
Action:
What executable capability represents it?
Execution:
What did the system attempt?
Outcome:
What actually happened?

Noema should preserve these distinctions.

⸻

64. Final Definition

The Outcome Engine is the deterministic Noema component responsible for establishing, recording, and maintaining the outcome of an execution using explicit execution records, expected outcomes, observed evidence, postconditions, authoritative external state, and versioned outcome rules.

The core invariant is:

Noema does not declare an Action successful because execution was attempted. It declares an outcome only when the available evidence establishes what happened. When the result cannot be established, Noema represents that uncertainty explicitly rather than inventing success or failure.