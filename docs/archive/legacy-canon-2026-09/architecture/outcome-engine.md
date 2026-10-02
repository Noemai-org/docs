Outcome Engine

Status: Foundational
Version: 0.2
Domain: Architecture
Canonical Path: architecture/outcome-engine.md

⸻

1. Definition

The Outcome Engine is the canonical Noema architectural component responsible for determining, recording, and interpreting what happened after an Intent has crossed the execution boundary.

It establishes the semantic boundary between:

* execution activity
* observed execution results
* expected outcomes
* actual outcomes
* business-state changes
* verified business outcomes
* success
* failure
* partial completion
* cancellation
* unresolved or unknown results

The Outcome Engine does not execute Actions.

Its responsibility begins with the evidence produced by execution and determines what outcome, if any, Noema can establish from that evidence.

Therefore:

Execution is an activity. Outcome is an established interpretation of what that activity produced.

The Outcome Engine operates after, and in coordination with, the Execution layer.

⸻

2. Purpose

The purpose of the Outcome Engine is to establish a durable, auditable representation of what happened as a result of attempting to execute an Intent.

It allows Noema to answer:

* What execution occurred?
* What outcome was expected?
* What evidence was produced?
* Which system supplied that evidence?
* Was the expected result achieved?
* Was the result verified?
* Was the result partial?
* Did execution fail?
* Is the outcome still pending?
* Is the outcome unknown?
* Was reconciliation required?
* Did the outcome subsequently become known?
* Which rules established the outcome?

The Outcome Engine therefore provides the architectural boundary between execution history and outcome determination.

⸻

3. Core Principle

The foundational principle is:

Execution is not outcome.

An execution request may be accepted without producing the intended business result.

An API may return successfully while the underlying business state remains unresolved.

A consumer may report success while an authoritative business system later reports failure.

A request may time out after the external system has already performed the Action.

Therefore:

Trusted Intent
      ↓
Execution Contract
      ↓
Execution
      ↓
Execution Record
      ↓
Observed Evidence
      ↓
Outcome Determination
      ↓
Outcome

Noema must not infer successful completion merely because:

* an execution request was sent
* an execution request was accepted
* an Action began
* a consumer returned successfully
* an API returned a positive response
* a workflow reached a terminal step
* a model interpreted a response as positive
* an external response is ambiguous

The Outcome Engine establishes an outcome only from defined evidence and outcome rules.

⸻

4. Position in the Noema Lifecycle

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

The Outcome Engine therefore belongs to the post-execution determination layer.

It consumes execution records and relevant evidence.

It does not replace:

* Intent
* Validation
* Trust
* Execution Planning
* Execution Contract
* Execution
* authoritative external business state

⸻

5. What the Outcome Engine Owns

The Outcome Engine owns Noema’s representation of an execution outcome.

This includes:

* expected outcome
* observed execution result
* outcome status
* outcome evidence
* outcome provenance
* outcome verification
* postcondition evaluation
* partial completion state
* failure classification
* unknown outcome state
* cancellation state
* outcome timestamps
* outcome transitions
* outcome history
* reconciliation state where applicable

This does not make Noema the authoritative owner of the underlying business state.

For example:

Payment System
      ↓
Authoritative payment state
Noema
      ↓
Observed evidence
      ↓
Outcome determination

Noema records and interprets what it establishes from the authoritative system.

The external system remains authoritative for its own business domain.

⸻

6. Outcome vs Execution

Execution answers:

Did an execution attempt occur, and what did the execution consumer report?

Outcome answers:

What result can Noema establish from that execution and the available evidence?

These are distinct questions.

For example:

Execution:
API request accepted
Outcome:
PENDING

or:

Execution:
Transfer request submitted
Outcome:
COMPLETED

or:

Execution:
Request timed out
Outcome:
UNKNOWN

Therefore:

EXECUTED ≠ SUCCESSFUL

⸻

7. Outcome vs Intent

The intended result and actual result must remain distinct.

Example:

Intent:
Transfer ₦100,000 to Account B
Expected Outcome:
Account B receives ₦100,000
Observed Result:
Transfer rejected by payment system

Noema must preserve both the expected result and the observed result.

An unsuccessful outcome must not rewrite the historical meaning of the Intent.

⸻

8. Expected Outcome

An Intent or Action Contract may define an expected outcome.

Conceptually:

ExpectedOutcome {
    state_change
    affected_resource
    expected_value
    expected_conditions
    postconditions
    verification_requirements
}

The Expected Outcome describes what successful execution is intended to produce.

It is not evidence that the result occurred.

Therefore:

Expected Outcome
        ≠
Observed Outcome

⸻

9. Observed Outcome

An observed outcome is derived from evidence available after or during execution.

Relevant evidence may include:

* execution response
* execution consumer response
* authoritative external-system response
* resource state
* transaction identifier
* event confirmation
* postcondition verification
* consumer acknowledgment
* authoritative status lookup
* reconciliation result

The Outcome Engine must distinguish between what was expected and what was actually established.

⸻

10. Outcome Verification

Where an Action or Execution Contract defines postconditions, the Outcome Engine may be required to verify them.

Conceptually:

Execution
   ↓
Expected Postconditions
   ↓
Observe Relevant State
   ↓
Compare
   ↓
Outcome Determination

Example:

Action:
Activate Card
Expected Postcondition:
Card.status = ACTIVE

The Outcome Engine observes the relevant authoritative state.

If:

Card.status = ACTIVE

the expected outcome may be established as:

COMPLETED

If the observed state does not satisfy the postcondition, successful completion has not been established.

Execution returning without an error is therefore not sufficient where postcondition verification is required.

⸻

11. Outcome States

The canonical conceptual outcome states are:

PENDING
COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN
CANCELLED

Implementations may introduce more granular subtypes.

Examples include:

FAILED_BY_CONSUMER
FAILED_BY_EXTERNAL_SYSTEM
FAILED_POSTCONDITION
UNKNOWN_EXTERNAL_STATE
PARTIAL_EXECUTION
CANCELLED_BY_ACTOR

The exact taxonomy may evolve while preserving the underlying semantic distinctions.

⸻

12. PENDING

PENDING means that execution has been accepted or begun, but the final outcome has not yet been established.

Example:

Execution accepted
      ↓
External processing ongoing
      ↓
PENDING

PENDING is neither success nor failure.

It represents an unresolved but potentially progressing execution.

⸻

13. COMPLETED

COMPLETED means that Noema has sufficient evidence to establish that the expected execution outcome was achieved.

Conceptually:

Execution
   ↓
Evidence
   ↓
Expected conditions satisfied
   ↓
COMPLETED

Completion should be supported by explicit evidence appropriate to the Action and its Execution Contract.

⸻

14. FAILED

FAILED means that the requested execution did not successfully produce the intended result and that failure has been established.

Examples include:

* Action rejected
* required precondition failed
* external system rejected the operation
* execution consumer reported failure
* postcondition was definitively violated
* authoritative business system established failure

Failure should include structured reasons where available.

⸻

15. PARTIALLY_COMPLETED

Some Actions contain multiple independently executable components.

For example:

Component A → COMPLETED
Component B → FAILED
Component C → COMPLETED

If the Intent or Action Contract explicitly permits partial execution, the aggregate outcome may be:

PARTIALLY_COMPLETED

Noema must not infer that partial completion is permitted merely because an Action contains multiple components.

Partial execution semantics must be established explicitly.

⸻

16. UNKNOWN

UNKNOWN means that Noema cannot establish whether the intended outcome occurred.

Example:

Request submitted
      ↓
Network failure
      ↓
No authoritative response
      ↓
UNKNOWN

Noema must not represent this as:

FAILED

unless failure has been established.

It must also not represent it as:

COMPLETED

without evidence.

Therefore:

UNKNOWN is a first-class outcome state.

⸻

17. CANCELLED

CANCELLED means that execution was intentionally terminated before successful completion.

Cancellation may result from:

* Actor request
* policy requirement
* supported execution revocation
* workflow termination
* external-system cancellation

Where supported by the underlying system, Noema should distinguish:

Cancellation Requested

from:

Cancellation Confirmed

A cancellation request does not itself establish that the underlying execution was successfully cancelled.

⸻

18. Outcome Determination

The Outcome Engine conceptually evaluates:

Execution Record
      +
Expected Outcome
      +
Observed Evidence
      +
Postconditions
      +
Outcome Rules
      ↓
Outcome Evaluation
      ↓
Outcome

Outcome determination should be deterministic with respect to the relevant inputs, evidence, and rule versions.

⸻

19. Outcome Determination Is Not Model Judgment

An LLM may assist in interpreting unstructured execution responses where necessary.

However, authoritative outcome determination must not depend solely upon model judgment.

The architecture should not rely on:

"The model thinks the operation succeeded."

Instead:

Execution Evidence
      ↓
Defined Outcome Rules
      ↓
Outcome Determination

Where model-assisted interpretation is necessary, the interpreted information should remain distinguishable from authoritative evidence.

The system must preserve the provenance of that interpretation.

⸻

20. Outcome Evidence

Consequential outcomes should preserve evidence provenance.

Conceptually:

OutcomeEvidence {
    source
    evidence_type
    observed_at
    reference
    authority
    freshness
}

Example:

Source:
Payment Provider
Evidence:
Transaction ID = TX-789
Status = SETTLED
Observed At = 14:32

or:

Source:
CRM
Evidence:
Customer Record
Status = ACTIVE
Observed At = 09:15

Evidence should be referenced rather than duplicated unnecessarily.

⸻

21. Authoritative Sources

The Outcome Engine must distinguish among:

* execution consumer
* authoritative business system
* Noema observation
* derived outcome

For example:

Payment Provider
      ↓
Authoritative payment state
      ↓
Noema observes state
      ↓
Outcome determination

Noema does not become the owner of the payment state merely because it observed it.

⸻

22. Postcondition Verification

Action Contracts may define postconditions.

Example:

Action:
Activate Card
Precondition:
Card exists
Postcondition:
Card.status = ACTIVE

The Outcome Engine may verify the postcondition against the authoritative system.

If:

Card.status = ACTIVE

then the expected outcome may be established.

If:

Card.status = BLOCKED

the intended outcome has not been achieved.

Execution success and postcondition success must therefore remain distinguishable.

⸻

23. Outcome and Business State

Business state may change independently of Noema.

The relationship is:

Noema Execution
       ↓
External System
       ↓
Business State

The Outcome Engine may observe relevant business state through defined interfaces.

It must not maintain a competing authoritative business state merely to simplify outcome determination.

⸻

24. Temporal Outcome Verification

Outcome verification may occur asynchronously.

Example:

T1
Execution submitted
T2
Execution accepted
T3
External processing
T4
Business state changed
T5
Outcome verified

Therefore:

Execution Time ≠ Outcome Time

Noema should preserve the relevant timestamps independently.

⸻

25. Eventual Outcomes

Some Actions cannot establish their final outcome immediately.

Example:

Loan application submitted
        ↓
PENDING
        ↓
APPROVED

or:

PENDING
        ↓
REJECTED

The Outcome Engine must therefore support asynchronous outcome progression.

The initial outcome does not necessarily represent the final outcome.

⸻

26. Outcome Reconciliation

Execution evidence and authoritative business state may disagree.

Example:

Execution Consumer:
SUCCESS
Authoritative System:
Transaction = FAILED

The Outcome Engine must not silently select one representation.

The discrepancy must be explicitly represented and processed through reconciliation.

Conceptually:

Execution Evidence
        +
Authoritative State
        ↓
Reconciliation
        ↓
Resolved Outcome

⸻

27. Unknown Outcome Recovery

An unknown outcome may later become known.

Example:

EXECUTION
   ↓
UNKNOWN
   ↓
Authoritative Lookup
   ↓
COMPLETED

or:

UNKNOWN
   ↓
Authoritative Lookup
   ↓
FAILED

Therefore:

UNKNOWN is not necessarily terminal.

The Outcome Engine must support subsequent evidence that resolves an earlier unknown state.

⸻

28. Outcome State History

Outcome transitions must remain auditable.

Example:

T0:
PENDING
T1:
UNKNOWN
T2:
COMPLETED

The final state alone is insufficient to explain what Noema knew at each point in time.

The historical progression must therefore remain reconstructible.

⸻

29. Outcome Transition Provenance

Each material outcome transition should preserve, where applicable:

* previous outcome
* triggering event
* new outcome
* timestamp
* execution ID
* evidence references
* evaluation ID
* verification result
* reason
* relevant rule version

Conceptually:

OutcomeTransition {
    previous_state
    event
    new_state
    timestamp
    execution_id
    evidence
    reason
    rule_version
}

⸻

30. Outcome Determinism

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
Deterministic Result

Determinism is necessary for auditability and historical reconstruction.

⸻

31. Outcome Rule Versioning

Outcome rules may evolve.

Therefore every outcome evaluation should identify the relevant:

rule_id
rule_version

A historical outcome must remain reconstructible even after the current outcome rules have changed.

The current rule set must not silently rewrite historical outcome determinations.

⸻

32. Consumer Failure vs Business Failure

Consumer-level failure and business-level failure must remain distinct.

Example:

Execution Consumer:
TIMEOUT

does not necessarily establish:

Business Action:
FAILED

The request may have reached the external system before the timeout.

Therefore the appropriate initial outcome may be:

UNKNOWN

until authoritative business state can be established.

This distinction is essential for consequential operations.

⸻

33. Idempotency and Outcomes

Outcome determination must account for idempotency.

Example:

Request A
   ↓
Payment submitted
   ↓
Response lost
   ↓
UNKNOWN

A blind retry could produce duplicate execution.

Therefore:

UNKNOWN

may require reconciliation before another execution attempt is permitted.

The Outcome Engine should expose sufficient state for the Execution layer to apply the Action’s idempotency semantics.

⸻

34. Outcome and Retry

Retry is not equivalent to failure recovery.

A retry may be safe only when:

* the previous execution is known to have failed
* the Action is retryable
* idempotency semantics permit retry
* relevant preconditions remain valid
* the Execution Contract permits the retry

An unknown outcome must not automatically trigger another execution attempt.

⸻

35. Outcome and Partial Execution

Composite Actions may have different outcomes for individual components.

Example:

Component A → COMPLETED
Component B → FAILED
Component C → PENDING

The aggregate outcome depends on the declared semantics of the Intent and Action Contract.

Noema must not infer:

all-or-nothing

or:

partial success permitted

unless those semantics are explicitly established.

⸻

36. Outcome and Compensation

Some Actions may require compensating Actions after partial or unsuccessful execution.

Example:

A completed
B failed
      ↓
Compensation required

The Outcome Engine should record that compensation is required or that compensation occurred.

It must not silently reinterpret the original outcome.

The relationship is:

Original Outcome
      ↓
Compensation Requirement
      ↓
Compensation Execution
      ↓
New Outcome

The original execution history remains intact.

⸻

37. Outcome Does Not Rewrite Trust

If an Intent was correctly marked READY and execution subsequently fails, that failure does not retroactively establish:

Trust = INVALID

The distinction remains:

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

38. Outcome Does Not Rewrite Validation

Execution failure does not automatically imply that the original Intent was invalid.

A valid and trusted Intent may encounter:

* external failure
* timeout
* unavailable resource
* changed business state
* consumer failure
* postcondition failure

Validation and outcome therefore remain separate architectural concerns.

⸻

39. Outcome and Intent Lifecycle

A broader Intent lifecycle may include:

RESOLVED
   ↓
TRUSTED
   ↓
EXECUTING
   ↓
COMPLETED

or:

EXECUTING
   ↓
FAILED

The Outcome Engine provides the evidence and determination required to establish the execution result.

The Intent lifecycle may reference the resulting outcome without collapsing the Intent model and Outcome model into one record.

⸻

40. Outcome and Execution Record

The Execution Record captures execution activity.

The Outcome Engine evaluates that execution activity and its associated evidence.

Conceptually:

Execution Record
      ↓
Outcome Engine
      ↓
Outcome Record

The two records should remain independently auditable.

The Execution Record answers what execution occurred.

The Outcome Record answers what result Noema established from that execution.

⸻

41. Outcome Record

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

The architectural requirement is that the Outcome Record remain attributable to the relevant Intent, execution, evidence, and determination rules.

⸻

42. Outcome Correlation

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

* what was intended
* what was authorized
* what was executed
* what evidence was observed
* what outcome was established

⸻

43. Outcome and External Events

External systems may emit events after execution.

Examples:

payment.submitted
payment.settled

The Outcome Engine may consume such events when they provide relevant evidence.

External events should preserve, where available:

* source
* event identity
* timestamp
* event version
* correlation identifier
* authority

These properties support deterministic correlation and reconciliation.

⸻

44. Duplicate Events

External systems may emit duplicate events.

Outcome processing should therefore be idempotent where the source semantics require it.

The same authoritative event must not produce multiple contradictory outcome transitions merely because it was delivered more than once.

Event identity and correlation should be used to establish whether an event has already been incorporated into the outcome history.

⸻

45. Out-of-Order Events

External events may arrive out of order.

For example:

payment.settled

may arrive before:

payment.submitted

The Outcome Engine should use:

* event identity
* event timestamps
* event versions
* correlation identifiers
* authoritative current state

where available.

Message arrival order must not automatically be treated as business-state order.

⸻

46. Outcome Freshness

An outcome is based on evidence observed at a particular time.

Therefore Noema must distinguish:

Outcome established at T1

from:

Current business state at T2

A completed outcome does not imply that the affected resource remains in the same state indefinitely.

⸻

47. Outcome vs Current State

Example:

T1:
Card activation completed.
T2:
Card later suspended.

The activation outcome remains:

COMPLETED

while the current business state is:

SUSPENDED

These are not contradictory.

The Outcome describes what happened to the Action.

Current State describes the present state of the affected resource.

⸻

48. Outcome Verification Failure

Verification itself may fail.

Example:

Execution completed
      ↓
Postcondition lookup unavailable
      ↓
Outcome cannot be established

The appropriate outcome may therefore be:

UNKNOWN

rather than:

FAILED

unless authoritative evidence establishes failure.

Failure of verification is not automatically failure of the underlying Action.

⸻

49. Outcome Escalation

Certain unknown or contradictory outcomes may require human intervention.

Example:

Payment request
      ↓
UNKNOWN
      ↓
Authoritative systems disagree
      ↓
HUMAN_INTERVENTION_REQUIRED

Human intervention should be represented explicitly.

It must not be hidden inside retry behavior or informal operational procedures.

⸻

50. Outcome Notifications

Outcome changes may produce events such as:

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

The exact event vocabulary may evolve.

⸻

51. Outcome Provenance

Outcome provenance must establish:

* what happened
* how Noema knows
* which system supplied the evidence
* when the evidence was observed
* which rule established the outcome
* which verification was performed
* whether the evidence was authoritative

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

This is necessary for auditability, reconciliation, and dispute resolution.

⸻

52. Outcome and Auditability

A consequential outcome must be reconstructible after the fact.

An auditor should be able to determine:

1. What was intended?
2. What was authorized?
3. What execution occurred?
4. What evidence was available?
5. What outcome was determined?
6. Which authoritative system supplied the evidence?
7. When was the outcome established?
8. Did the outcome subsequently change?
9. Was reconciliation required?
10. Was human intervention involved?
11. Which outcome rules were used?

The Outcome Engine therefore forms a critical component of Noema’s audit architecture.

⸻

53. Outcome Invariants

Invariant 1

Execution does not equal outcome.

Invariant 2

Outcome determination must be based on explicit evidence.

Invariant 3

UNKNOWN must not be represented as success.

Invariant 4

UNKNOWN must not be represented as failure without evidence.

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

Invariant 17

A consumer success response is not automatically authoritative business-state evidence.

Invariant 18

Verification failure must remain distinguishable from verified business failure.

Invariant 19

Historical outcome determinations must remain reconstructible under their original rule versions.

Invariant 20

Retry must not erase or replace the outcome history of the prior execution attempt.

⸻

54. Canonical Outcome Flow

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

Cancellation may enter the flow where explicitly supported:

Execution
   ↓
Cancellation
   ↓
CANCELLED

⸻

55. Relationship to the Trust State Machine

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

For example:

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

Trust and Outcome must not be collapsed into a single semantic decision.

⸻

56. Relationship to the Execution Planner

The Execution Planner determines how a trusted Intent is translated into an executable sequence.

The Outcome Engine does not plan execution.

The relationship is:

Intent
  ↓
Execution Planner
  ↓
Execution Plan
  ↓
Execution
  ↓
Outcome Engine
  ↓
Outcome

The Planner determines what should be executed.

The Outcome Engine determines what resulted from execution.

⸻

57. Relationship to the Execution Record

The Execution Record captures execution activity, including relevant requests, responses, consumers, timestamps, and execution state.

The Outcome Engine consumes the Execution Record and associated evidence.

Conceptually:

Execution Record
        │
        ├── request
        ├── consumer
        ├── timestamps
        ├── execution state
        ├── responses
        └── references
                │
                ▼
          Outcome Engine
                │
                ▼
             Outcome

The Outcome Engine must not reconstruct execution history by inference where the Execution Record already provides the authoritative execution history.

⸻

58. Relationship to Operational Memory

Outcome records become part of Noema’s operational history.

Operational Memory may use outcomes to establish:

* what happened previously
* whether an Intent was completed
* whether reconciliation occurred
* whether an execution remains pending
* what evidence was observed
* whether follow-up may be required

Outcome history must remain distinguishable from authoritative business state.

⸻

59. Outcome and Learning

Historical outcomes may provide information useful for future system behavior.

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

60. Outcome and Idempotent Recovery

For consequential Actions, the Outcome Engine should provide sufficient information to determine whether another execution attempt could create duplication or inconsistency.

Example:

UNKNOWN
+
transaction reference exists

may require reconciliation before retry.

This protects against:

Lost Response
      ↓
Blind Retry
      ↓
Duplicate Action

The Outcome Engine therefore participates in safe recovery without itself becoming the execution authority.

⸻

61. Outcome and Compensation

Where a failed or partial execution requires compensation, the compensation must be represented as a new explicit Action.

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

Compensation does not rewrite the original execution record or outcome.

⸻

62. Outcome State Transition Principle

An outcome state may change only because of a defined source of evidence or state transition.

Permitted causes include:

* defined execution event
* authoritative external evidence
* postcondition verification
* reconciliation
* explicit cancellation
* deterministic re-evaluation under defined rules

An outcome must not change merely because:

* an LLM appears more confident
* a retry occurred without new evidence
* a user expects success
* an execution response merely sounds positive
* the current business state changed in a way unrelated to the original Action

Outcome transitions must therefore be attributable to observable evidence or an explicit architectural operation.

⸻

63. Canonical Mental Model

The Outcome Engine can be reduced to four questions:

1. Did execution occur?

Answered through:

Execution Record

2. What evidence exists?

Answered through:

Observed Evidence

3. Did the expected conditions occur?

Answered through:

Verification

and, where applicable:

Postcondition Evaluation

4. What outcome can Noema establish?

The result is one of the applicable outcome states:

PENDING
COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN
CANCELLED

⸻

64. Fundamental Boundary

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

Each stage answers a different architectural question:

Stage	Question
Meaning	What does the Actor intend?
Validation	Is the Intent well formed and applicable?
Trust	May the Intent proceed?
Action	What executable operation represents the Intent?
Execution	What did the system attempt and report?
Outcome	What result can Noema establish from the evidence?

Noema should preserve these distinctions.

⸻

65. Canonical Relationship

The complete relationship among execution, evidence, and outcome is:

                         ┌──────────────┐
                         │    Intent    │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │  Validation  │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │    Trust     │
                         └──────┬───────┘
                                │
                              READY
                                │
                                ▼
                         ┌──────────────┐
                         │Action/Plan   │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   Contract   │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │  Execution   │
                         └──────┬───────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │Execution Record │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    Evidence     │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Outcome Engine  │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │     Outcome     │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Verification   │
                       └─────────────────┘

This separation preserves the Noema boundary between:

* understanding
* validation
* Trust
* authorization
* execution
* evidence
* outcome determination
* authoritative business state

⸻

66. Final Definition

The Outcome Engine is the canonical Noema architectural component responsible for establishing, recording, and maintaining the outcome of an execution using the relevant Execution Record, expected outcome, observed evidence, postconditions, authoritative external state, reconciliation processes, and versioned outcome rules.

It does not execute Actions.

It does not replace authoritative external business systems.

It does not retroactively rewrite Intent, Validation, or Trust.

Its fundamental responsibility is to determine what result Noema can legitimately establish from the evidence available after execution.

The core invariant is:

Noema does not declare an Action successful merely because execution was attempted or accepted. It establishes an outcome only when the available evidence supports that determination. When the result cannot be established, Noema represents that uncertainty explicitly rather than inventing success or failure.