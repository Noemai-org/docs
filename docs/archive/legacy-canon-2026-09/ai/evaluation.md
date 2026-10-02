> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Evaluation

Status: Foundational
Version: 0.1
Domain: AI
Canonical Path: ai/evaluation.md

⸻

1. Definition

Evaluation is the systematic process by which Noema measures whether an AI-assisted interpretation, decision, transition, or execution-related behavior satisfies defined correctness, safety, reliability, and system invariants.

Evaluation exists to answer:

Did Noema behave correctly according to its defined semantics and constraints?

Evaluation is distinct from:

* Inference — producing a candidate interpretation or decision
* Validation — determining whether a canonical Intent is structurally and semantically valid
* Trust — determining whether an Intent may proceed toward execution
* Execution — performing an Action through an execution consumer
* Outcome verification — determining what actually happened in the external system

Evaluation measures these processes; it does not replace them.

⸻

2. Purpose

Noema uses AI and probabilistic models in parts of the intent lifecycle.

Because those components are probabilistic, Noema must be able to evaluate them independently from the authority mechanisms that govern execution.

Evaluation therefore provides a controlled mechanism for determining whether:

* an interpretation is correct
* an Intent was resolved correctly
* ambiguity was detected appropriately
* clarification was requested when required
* relevant context was retrieved
* canonical fields were populated correctly
* validation behaved correctly
* Trust decisions followed deterministic rules
* action selection respected available capabilities
* execution contracts were constructed correctly
* execution outcomes were represented correctly
* provenance was preserved
* system invariants were maintained

The purpose of evaluation is not merely to measure model quality.

It is to evaluate the behavior of the complete Noema system.

⸻

3. Evaluation Boundary

The canonical distinction is:

AI Model
   ↓
Candidate Interpretation
   ↓
Intent Resolution
   ↓
Validation
   ↓
Trust
   ↓
Action / Contract
   ↓
Execution
   ↓
Outcome
   ↓
Evaluation

Evaluation may observe and assess each stage.

It must not silently alter the semantics of those stages.

Evaluation answers whether the system behaved according to the applicable specification.

⸻

4. Evaluation Is Not Model Confidence

Model confidence is an attribute produced by a probabilistic model.

Evaluation is an independent assessment of behavior.

Therefore:

Model confidence
        ≠
Evaluation result

A model may report high confidence while producing an incorrect Intent.

A model may report low confidence while producing an acceptable candidate that requires clarification.

Noema must therefore avoid using model confidence as a substitute for evaluation.

⸻

5. Evaluation Is Not Trust

Trust determines execution eligibility.

Evaluation determines whether a behavior or decision satisfies the relevant evaluation criteria.

For example:

Intent
  ↓
Trust
  ↓
READY

does not mean:

Evaluation = PASS

unless the relevant evaluation criteria establish that the Trust decision was correct.

Similarly:

Trust = BLOCKED

may be the correct behavior and therefore constitute a successful evaluation result.

The correctness of a system decision must be evaluated against the applicable specification, not against whether the decision resulted in execution.

⸻

6. Evaluation Is Not Validation

Validation determines whether a canonical Intent satisfies required structural and semantic conditions.

Evaluation may assess whether validation itself behaved correctly.

Therefore:

Validation
   ↓
Validation Result
   ↓
Evaluation

For example, if a destination is missing:

Validation:
INCOMPLETE

Evaluation determines whether producing INCOMPLETE was correct for that test case.

⸻

7. Evaluation Targets

Noema evaluation may target:

* Intent interpretation
* Intent resolution
* ambiguity detection
* clarification behavior
* context retrieval
* evidence selection
* canonicalization
* validation
* Trust evaluation
* policy application
* authorization handling
* capability selection
* planning
* action selection
* contract generation
* execution orchestration
* outcome representation
* failure handling
* provenance
* state transitions
* human intervention
* end-to-end workflows

The evaluation target must be explicit.

⸻

8. Evaluation Levels

Evaluation should distinguish at least four levels.

8.1 Component Evaluation

Tests an individual component.

Examples:

* entity extraction
* reference resolution
* ambiguity detection
* policy evaluation
* capability matching

8.2 Contract Evaluation

Tests whether an interface between components satisfies its defined contract.

Examples:

* Intent schema
* ValidationResult
* Trust decision
* Action Contract
* Execution Result

8.3 Workflow Evaluation

Tests a complete Intent lifecycle.

Example:

User Expression
      ↓
Resolution
      ↓
Clarification
      ↓
Validation
      ↓
Trust
      ↓
Contract
      ↓
Execution
      ↓
Outcome

8.4 System Evaluation

Tests Noema as an integrated system across multiple capabilities and external systems.

These levels should not be conflated.

A component can pass while the complete workflow fails.

⸻

9. Evaluation Case

An evaluation should be represented as structured data rather than only as an informal prompt and expected answer.

Conceptually:

EvaluationCase {
    case_id
    input
    context
    expected_intent
    expected_state
    expected_requirements
    expected_trust
    expected_action
    expected_contract
    expected_outcome
    evaluation_criteria
}

The exact schema may evolve.

The important principle is that the evaluation target and expected behavior must be explicit.

⸻

10. Evaluation Dataset

An evaluation dataset is a collection of evaluation cases representing a defined behavior domain.

Datasets may contain:

* normal cases
* ambiguous cases
* incomplete cases
* invalid cases
* adversarial cases
* boundary cases
* authorization cases
* policy cases
* failure cases
* temporal cases
* stale-evidence cases
* multi-entity cases
* composite Intent cases
* partial-execution cases

A dataset should identify its scope and version.

⸻

11. Evaluation Dataset Versioning

Evaluation datasets must be versioned.

Conceptually:

dataset:
intent-resolution-v1
version:
1.2
created:
...
cases:
...

A result should identify the dataset version against which it was produced.

This is necessary because evaluation criteria and test cases can change over time.

⸻

12. Evaluation Criteria

Every evaluation must define what constitutes correct behavior.

Criteria may include:

* exact semantic correctness
* schema conformance
* required-field completeness
* correct ambiguity handling
* correct state transition
* correct Trust result
* correct capability selection
* contract correctness
* outcome correctness
* provenance completeness
* policy compliance
* deterministic behavior

Criteria should be machine-evaluable wherever practical.

⸻

13. Expected Behavior

Expected behavior must be derived from the applicable canonical specification.

For example:

Input:
"Send the invoice to John."
Known context:
three possible Johns
Expected:
WAITING_FOR_CLARIFICATION

The expected result is not:

choose the most likely John

unless an explicit deterministic rule establishes that behavior.

Evaluation therefore measures conformance to Noema semantics rather than apparent plausibility.

⸻

14. Exact Match vs Semantic Match

Different evaluation targets require different comparison methods.

Some outputs should support exact comparison.

Examples:

state = READY
status = INVALID
error_code = INVALID_AMOUNT

Other outputs require semantic comparison.

Examples:

* resolved Intent
* extracted entities
* generated clarification
* plan representation

The evaluation method must correspond to the semantics of the evaluated artifact.

⸻

15. Structured Evaluation

Whenever possible, Noema should evaluate structured representations rather than raw natural-language responses.

For example, rather than evaluating:

“I think you want to transfer fifty thousand naira.”

evaluation should target:

Action:
TRANSFER
Amount:
50000
Currency:
NGN

This reduces dependence on stylistic differences in model output.

⸻

16. Natural-Language Evaluation

Natural-language outputs may still require evaluation.

Examples include:

* clarification questions
* explanations
* human-facing error messages
* summaries
* conversational responses

These should be evaluated against defined criteria rather than superficial textual similarity alone.

For example, a clarification response may be evaluated for:

* identifying the missing field
* avoiding unsupported assumptions
* requesting actionable information
* preserving Intent semantics
* avoiding unauthorized execution

⸻

17. Golden Cases

Golden cases are canonical evaluation cases whose expected behavior has been explicitly established.

They should represent important Noema invariants and representative workflows.

Examples:

Ambiguous recipient
Missing amount
Invalid amount
Expired authorization
Missing approval
Policy prohibition
Unavailable capability
Stale evidence
Successful execution
Execution failure
Unknown execution result

Golden cases should be versioned and maintained as part of the canonical evaluation suite.

⸻

18. Negative Cases

Evaluation must include cases where Noema should not proceed.

Examples:

Ambiguous Intent
        ↓
CLARIFICATION
Unauthorized Action
        ↓
BLOCKED
Missing approval
        ↓
WAITING
Invalid Intent
        ↓
BLOCKED
Unknown mandatory condition
        ↓
NOT READY

A system that succeeds only when it executes cannot be considered correctly evaluated.

Correct refusal, waiting, clarification, and blocking are valid outcomes.

⸻

19. Boundary Cases

Evaluation should explicitly test boundary conditions.

Examples:

* amount exactly at an approval threshold
* amount exactly at a maximum limit
* authorization expiring at execution time
* evidence at its freshness boundary
* capability becoming unavailable
* policy changing between evaluation stages
* resource state changing between validation and execution

Boundary cases are particularly important for deterministic Trust behavior.

⸻

20. Ambiguity Evaluation

Noema must evaluate whether ambiguity is detected correctly.

Example:

"Send it to John."

If:

John A
John B
John C

are all valid candidates, the expected behavior may be:

WAITING_FOR_CLARIFICATION

Selecting one without an explicit resolution rule should be evaluated as incorrect.

⸻

21. Clarification Evaluation

Clarification should be evaluated for semantic correctness.

A correct clarification should:

* identify the unresolved requirement
* request information necessary to resolve it
* avoid inventing facts
* preserve already established Intent information
* allow the lifecycle to continue once the requirement is satisfied

Evaluation should distinguish useful clarification from unnecessary or misleading questioning.

⸻

22. Context Evaluation

Context retrieval may be evaluated for:

* relevance
* sufficiency
* correctness
* provenance
* freshness
* scope

Noema should not treat retrieval of more context as inherently better.

The relevant question is:

Did the system obtain the context required for the decision?

⸻

23. Evidence Evaluation

Evidence may be evaluated for:

* source
* relevance
* validity
* freshness
* applicability
* provenance

Evaluation should distinguish:

Evidence exists

from:

Evidence establishes the required fact

An irrelevant or stale source should not receive credit merely because it contains related information.

⸻

24. Trust Evaluation

Trust evaluation should verify that the Trust Engine produces the state required by the applicable conditions.

For example:

Intent valid
Authorization valid
Policy satisfied
Capability available
Constraints satisfied
Required approval received

should produce:

READY

provided no other mandatory condition prevents execution.

Conversely:

Policy prohibits action

must not produce:

READY

Evaluation therefore tests Trust against explicit predicates.

⸻

25. Trust State-Machine Evaluation

The Trust State Machine should be evaluated for transition correctness.

Examples:

UNRESOLVED
    ↓ clarification
EVALUATING
WAITING_FOR_APPROVAL
    ↓ approval received
EVALUATING

not directly:

WAITING_FOR_APPROVAL
    ↓
READY

Similarly:

READY
    ↓ material condition changes
EVALUATING

must be supported.

Evaluation should verify both allowed and disallowed transitions.

⸻

26. Determinism Evaluation

Deterministic components must produce the same result when supplied with the same:

* Intent
* context
* evidence
* policies
* rules
* capabilities
* relevant versions

Conceptually:

Evaluate(I, C, E, R, V)
=
Evaluate(I, C, E, R, V)

Repeated evaluation must not produce arbitrary state changes.

⸻

27. Probabilistic Component Evaluation

Probabilistic components cannot always be expected to produce byte-for-byte identical outputs.

They should instead be evaluated against defined behavioral criteria.

For example:

Input
  ↓
Candidate Intent

may be evaluated for:

* required fields
* semantic correctness
* entity correctness
* ambiguity handling
* prohibited assumptions

The evaluation criteria must remain independent from superficial wording differences.

⸻

28. Regression Evaluation

Whenever a model, prompt, policy, rule, ontology, schema, or implementation changes, relevant evaluation cases should be rerun.

The purpose is to identify regressions.

Examples:

Model v1
    ↓
passes 94/100
Model v2
    ↓
passes 96/100

The aggregate score alone is insufficient.

Noema must identify which cases changed and why.

⸻

29. Evaluation Deltas

Evaluation should preserve differences between runs.

Conceptually:

Previous Evaluation
        ↓
New Evaluation
        ↓
Changed Cases
        ↓
Analysis

A change in aggregate performance must not conceal regressions in safety-critical cases.

⸻

30. Safety-Critical Cases

Some evaluation cases should be designated as critical.

Examples:

* unauthorized financial transfer
* prohibited data access
* destructive operation without confirmation
* policy-prohibited action
* ambiguous high-impact action
* stale authorization
* missing mandatory approval

A critical-case failure should be surfaced explicitly rather than averaged away.

⸻

31. Evaluation Metrics

Metrics should correspond to the evaluated behavior.

Possible metrics include:

* Intent resolution accuracy
* field accuracy
* ambiguity detection rate
* clarification correctness
* validation correctness
* Trust decision correctness
* state-transition correctness
* contract validity
* execution success representation
* provenance completeness
* false-approval rate
* false-block rate
* unknown-to-valid error rate

No single metric should be treated as a universal measure of Noema quality.

⸻

32. False Approval and False Blocking

Trust-related evaluation should distinguish two important error classes.

False Approval

The system allows an Intent to proceed when the applicable conditions do not permit it.

Should:
BLOCKED
Produced:
READY

False Blocking

The system prevents an Intent from proceeding when the applicable conditions permit it.

Should:
READY
Produced:
BLOCKED

These are different failure modes and should be measured separately.

⸻

33. Unknown-State Evaluation

Evaluation must specifically test whether unknown information is handled correctly.

Example:

Authorization service unavailable

The expected behavior must not silently become:

authorization = denied

or:

authorization = approved

unless an explicit system rule establishes that behavior.

Unknown mandatory conditions must not incorrectly produce READY.

⸻

34. Evaluation of External Dependencies

External systems may be unavailable, stale, inconsistent, or changed.

Evaluation should therefore include simulated or controlled dependency conditions.

Examples:

registry unavailable
policy service unavailable
authorization service unavailable
payment provider timeout
resource state changed

The objective is to establish whether Noema responds according to its fail-closed and lifecycle semantics.

⸻

35. Execution Evaluation

Execution evaluation must distinguish:

READY

from:

EXECUTION SUCCESS

A correctly trusted Intent can still fail during execution.

Evaluation should therefore test:

* execution acceptance
* execution start
* successful completion
* timeout
* rejection
* partial failure
* unknown outcome
* postcondition verification

⸻

36. Outcome Evaluation

The execution consumer remains authoritative for actual business-state outcomes.

Evaluation should therefore assess whether Noema correctly represents the reported outcome.

For example:

Execution result:
unknown

must not be transformed into:

COMPLETED

merely because execution was initiated.

⸻

37. Partial Execution

Composite Intents require explicit evaluation of partial execution behavior.

Example:

A → COMPLETED
B → FAILED
C → WAITING

The evaluation must determine whether such partial progression is permitted by the Intent semantics.

Noema must not infer permission for partial execution merely because individual components are independently executable.

⸻

38. Human Intervention Evaluation

Human intervention must be evaluated as a legitimate lifecycle outcome.

Examples:

ambiguous Intent
    ↓
WAITING_FOR_CLARIFICATION

or:

approval required
    ↓
WAITING_FOR_APPROVAL

Evaluation should verify that the system stops where required rather than attempting to bypass human involvement.

⸻

39. Adversarial Evaluation

Noema should include adversarial cases designed to expose unsafe assumptions.

Examples:

* ambiguous names
* conflicting context
* contradictory evidence
* malformed Intent fields
* misleading natural language
* prompt injection attempts
* unauthorized requests
* stale approvals
* capability spoofing
* conflicting policies
* incomplete external responses

The purpose is to test whether explicit boundaries survive adverse inputs.

⸻

40. Prompt Injection Evaluation

Where models consume external or retrieved content, evaluation should test whether untrusted content can alter Noema’s authority model.

External content must not silently redefine:

* Trust requirements
* authorization
* policy
* capability
* execution boundaries
* system instructions

Evaluation should verify that authority remains grounded in canonical system controls.

⸻

41. Evaluation of Planning

Planning may be probabilistic.

Therefore planning evaluation should focus on whether the resulting plan satisfies explicit constraints.

Evaluation may test:

* required steps
* action ordering
* dependencies
* capability requirements
* authorization requirements
* prohibited actions
* expected outcomes
* recovery behavior

A plausible plan is not necessarily a valid plan.

⸻

42. Evaluation of Action Selection

Action selection should be evaluated against available capabilities and the resolved Intent.

The evaluation should establish:

Intent
+
Required capability
+
Constraints
+
Authority

produce an appropriate Action.

Noema should not receive evaluation credit merely for selecting an Action that appears semantically related.

⸻

43. Evaluation of Contracts

Execution Contracts should be evaluated for structural and semantic correctness.

A contract should be checked for applicable:

* action identity
* target
* inputs
* capability
* authorization
* preconditions
* constraints
* expected effects
* postconditions
* failure semantics
* idempotency
* provenance

An invalid contract must not be treated as successful merely because the selected Action is correct.

⸻

44. Provenance Evaluation

Evaluation should verify that important decisions remain reconstructible.

Relevant provenance may include:

* Intent version
* context version
* evidence references
* policy version
* validation result
* Trust evaluation ID
* action contract
* execution consumer
* timestamps
* state transitions
* outcome

Evaluation should test not only whether the correct decision occurred, but whether Noema can explain how the decision was established.

⸻

45. Evaluation Trace

An evaluation should produce an inspectable trace.

Conceptually:

Evaluation
    │
    ├── Input
    ├── Context
    ├── Candidate Intent
    ├── Validation
    ├── Trust
    ├── Action
    ├── Contract
    ├── Execution
    ├── Outcome
    └── Result

The trace should allow a failed evaluation to be localized to the relevant lifecycle stage.

⸻

46. Evaluation Result

Evaluation should produce a structured result.

Conceptually:

EvaluationResult {
    status
    case_id
    evaluator
    criteria
    observations
    failures
    provenance
}

Possible statuses include:

PASS
FAIL
INCONCLUSIVE
NOT_APPLICABLE

The exact schema may evolve.

⸻

47. PASS

PASS means the evaluated behavior satisfied the defined evaluation criteria.

It does not mean:

* the model is always correct
* the workflow is universally safe
* the external system succeeded
* the system is free of defects

It means the evaluated case satisfied its specified criteria.

⸻

48. FAIL

FAIL means the evaluated behavior violated one or more defined criteria.

A failure should identify:

* the failed criterion
* observed behavior
* expected behavior
* relevant state
* relevant provenance

Whenever possible, failures should be machine-readable.

⸻

49. INCONCLUSIVE

INCONCLUSIVE means evaluation could not establish whether the behavior satisfied the criteria.

Examples:

* required evaluation evidence unavailable
* external dependency unavailable
* expected outcome cannot be established
* evaluator itself encounters an unresolved condition

INCONCLUSIVE must not silently become PASS.

⸻

50. Evaluation Provenance

Every evaluation result should identify, where applicable:

case_id
dataset_id
dataset_version
system_version
model_version
prompt_version
policy_version
ontology_version
rule_versions
timestamp
evaluator_version

This allows evaluation results to be reconstructed and compared over time.

⸻

51. Human Evaluation

Some outputs may require human judgment.

Human evaluation may be appropriate for:

* natural-language quality
* clarification usefulness
* explanation quality
* workflow usability
* edge cases not yet formalized

Human evaluation should remain explicit.

A human judgment should not be represented as though it were a deterministic system predicate.

⸻

52. Automated Evaluation

Automated evaluation should be preferred where the expected behavior can be expressed deterministically.

Examples:

required field exists
state transition is legal
policy predicate satisfied
contract conforms to schema
authorization condition satisfied
unknown condition does not produce READY

Automated evaluation provides repeatability and regression detection.

⸻

53. Evaluator Independence

Where practical, the evaluator should be sufficiently independent from the system being evaluated.

A model should not receive full authority to declare its own output correct merely because it generated that output.

For consequential evaluation, authoritative criteria should derive from:

* canonical specifications
* deterministic rules
* structured expected results
* controlled test conditions
* explicitly identified human judgments

⸻

54. Evaluation Against the Canon

Evaluation criteria should ultimately trace back to canonical Noema semantics.

The chain is:

Canon
  ↓
Specification
  ↓
Contract
  ↓
Evaluation Criteria
  ↓
Evaluation Case
  ↓
Evaluation Result

This ensures evaluation measures conformance to the intended system rather than arbitrary benchmark performance.

⸻

55. Evaluation and Research

Research experiments may use exploratory metrics and hypotheses.

Those results should not automatically become canonical evaluation criteria.

The distinction is:

Research
   ↓
Hypothesis
   ↓
Experiment
   ↓
Evidence
   ↓
Decision
   ↓
Specification / Canon
   ↓
Evaluation Criteria

Evaluation should follow established semantics unless explicitly designated otherwise.

⸻

56. Evaluation and Model Changes

A model change may alter:

* Intent interpretations
* entity resolution
* ambiguity detection
* clarification behavior
* plans
* action selection
* natural-language responses

Therefore model changes should trigger relevant regression evaluation.

A model version should be associated with evaluation results.

⸻

57. Evaluation and Prompt Changes

Prompt changes can materially affect probabilistic behavior.

Prompt versions should therefore be tracked where they influence evaluated behavior.

Conceptually:

Model Version
+
Prompt Version
+
Context
+
Input

should be reproducible sufficiently to understand evaluation changes.

⸻

58. Evaluation and Policy Changes

Policy changes can legitimately change expected Trust behavior.

For example:

Policy v1:
approval required above ₦5M
Policy v2:
approval required above ₦10M

An evaluation result must therefore identify the policy version against which it was evaluated.

A changed result is not necessarily a regression.

⸻

59. Evaluation and Intent Versioning

If the canonical Intent representation changes, evaluation datasets and expected results may require migration.

The evaluation record should identify the Intent schema or version used.

This prevents incompatible historical evaluations from being compared without context.

⸻

60. Regression Gates

Certain evaluation failures should prevent a change from being promoted.

Examples may include:

* unauthorized execution
* false approval
* invalid Trust transition
* loss of mandatory provenance
* execution without required contract
* execution despite unresolved ambiguity

The exact promotion policy belongs to implementation and deployment specifications.

The foundational principle is:

Critical evaluation failures must be visible and cannot be hidden by aggregate performance.

⸻

61. Aggregate Metrics Must Not Hide Critical Failures

Consider:

99 successful cases
1 unauthorized execution

An aggregate score of 99% does not adequately represent the significance of the failure.

Evaluation must therefore preserve case-level results and identify critical failures separately.

⸻

62. Evaluation Coverage

Coverage should be measured across relevant semantic dimensions, not merely number of test cases.

Coverage may include:

* Intent types
* Actions
* entities
* policies
* authorization states
* Trust states
* capabilities
* failure modes
* temporal conditions
* external dependencies
* clarification paths
* execution outcomes

A large dataset can still provide poor coverage if it lacks important states.

⸻

63. State-Machine Coverage

Evaluation should cover all material Trust transitions.

At minimum:

UNRESOLVED → EVALUATING
EVALUATING → WAITING
EVALUATING → BLOCKED
EVALUATING → READY
WAITING → EVALUATING
BLOCKED → EVALUATING
READY → EVALUATING
READY → EXECUTING
EXECUTING → COMPLETED
EXECUTING → FAILED

Illegal transitions should also be tested.

⸻

64. Invariant Evaluation

Noema’s foundational invariants should themselves be evaluated.

Examples:

Invariant

Unknown mandatory conditions cannot produce READY.

Test

Provide unknown mandatory authorization.

Expected

READY = false

Another:

Invariant

Unresolved Intent cannot cross the execution boundary.

Test

Provide materially ambiguous recipient.

Expected

execution not accepted

This turns architectural principles into executable tests.

⸻

65. Evaluation of Fail-Closed Behavior

Evaluation must test conditions where Noema lacks sufficient grounds for execution.

Examples:

authorization unknown
policy unavailable
required evidence stale
capability unavailable
required context unavailable

Expected behavior should follow the applicable state-machine semantics.

Noema must not convert missing evidence into positive authorization.

⸻

66. Evaluation of Recovery

Evaluation should also test legitimate recovery.

Examples:

WAITING_FOR_CAPABILITY
        ↓
capability available
        ↓
EVALUATING
        ↓
READY

and:

BLOCKED
        ↓
blocking condition removed
        ↓
EVALUATING

Recovery must trigger appropriate re-evaluation rather than bypassing the Trust Engine.

⸻

67. Evaluation of Re-Evaluation

Material changes should trigger evaluation of the new state.

Examples:

READY
  ↓
authorization revoked
  ↓
EVALUATING
  ↓
BLOCKED

or:

READY
  ↓
evidence expired
  ↓
EVALUATING
  ↓
WAITING

Evaluation should verify that stale Trust does not remain silently active.

⸻

68. Evaluation of TOCTOU Conditions

Noema must evaluate conditions that change between validation, Trust, and execution.

Example:

T1:
Validation
T2:
Trust = READY
T3:
Business state changes
T4:
Execution

The evaluation should determine whether the execution consumer performs the required authoritative final check.

A successful Trust decision at T2 does not guarantee successful execution at T4.

⸻

69. Evaluation of Outcome Truth

Evaluation must preserve the distinction between:

Action requested

and:

Action completed

For example:

execution.accepted

must not automatically become:

COMPLETED

unless the execution result establishes completion.

⸻

70. Evaluation of Composite Intents

Composite Intents should be evaluated for aggregation behavior.

Example:

A = READY
B = WAITING
C = READY

If execution is atomic:

Composite = WAITING

If partial execution is explicitly permitted:

A → executable
B → waiting
C → executable

Evaluation must follow the declared semantics rather than assuming one aggregation strategy.

⸻

71. Evaluation Does Not Change Authority

Evaluation itself does not authorize execution.

The sequence remains:

Evaluation
    ↓
Evidence about system behavior

not:

Evaluation
    ↓
Permission to execute

Trust and authorization remain governed by their respective canonical mechanisms.

⸻

72. Evaluation Artifacts

Evaluation may produce:

* datasets
* test cases
* expected results
* traces
* metrics
* failure reports
* regression reports
* coverage reports
* evaluation manifests
* benchmark reports

Artifacts should be versioned where they materially affect interpretation of results.

⸻

73. Evaluation History

Noema should preserve historical evaluation results sufficiently to determine:

* what was evaluated
* when it was evaluated
* against which criteria
* using which versions
* what changed
* which cases failed
* whether failures were resolved

This supports system evolution without losing historical context.

⸻

74. Evaluation Lifecycle

The canonical evaluation lifecycle is:

DEFINE
   ↓
CASE
   ↓
RUN
   ↓
OBSERVE
   ↓
COMPARE
   ↓
CLASSIFY
   ↓
REPORT
   ↓
REGRESS / IMPROVE

Where appropriate:

REPORT
   ↓
CANON / SPECIFICATION REVIEW

may follow when evaluation reveals a fundamental contradiction or missing abstraction.

⸻

75. Evaluation and Improvement

Evaluation exists to identify discrepancies between intended and observed behavior.

Conceptually:

Expected Behavior
       ↓
       │
       ├──── compare ──── Observed Behavior
       │
       ▼
Discrepancy
       ↓
Analysis
       ↓
Improvement
       ↓
Re-evaluation

Improvement must not consist solely of optimizing benchmark metrics.

The objective is conformance to Noema’s defined semantics and safety boundaries.

⸻

76. Evaluation Invariants

Invariant 1

Evaluation criteria must be explicit.

Invariant 2

Evaluation must distinguish model confidence from behavioral correctness.

Invariant 3

Evaluation must distinguish Validation from Trust.

Invariant 4

Correct blocking, waiting, and clarification are valid successful outcomes when required by the specification.

Invariant 5

Unknown mandatory information must not receive credit as established information.

Invariant 6

Critical failures must not be hidden by aggregate metrics.

Invariant 7

Evaluation results must be traceable to their inputs, versions, and criteria.

Invariant 8

Evaluation datasets must be versioned when changes can affect interpretation.

Invariant 9

Deterministic system components must be evaluated for deterministic behavior.

Invariant 10

Probabilistic components must be evaluated against explicit behavioral criteria rather than assumed authority.

Invariant 11

Evaluation must test both positive and negative paths.

Invariant 12

Evaluation must cover material Trust State Machine transitions.

Invariant 13

Evaluation must preserve the distinction between execution eligibility and execution outcome.

Invariant 14

Evaluation must not silently mutate the Intent or system state merely to obtain a passing result.

Invariant 15

Evaluation results must be reproducible to the extent required by the evaluated behavior.

⸻

77. Canonical Evaluation Flow

                 Evaluation Definition
                         │
                         ▼
                  Evaluation Case
                         │
                         ▼
                    System Run
                         │
                         ▼
                     Observe
                         │
                         ▼
                    Compare
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
             PASS       FAIL   INCONCLUSIVE
              │          │          │
              └──────────┼──────────┘
                         ▼
                    Evaluation
                       Record
                         │
                         ▼
                 Regression / Review

⸻

78. Canonical Mental Model

Evaluation can be reduced to five questions:

1. What behavior are we evaluating?
2. What behavior does the specification require?
3. What behavior actually occurred?
4. What evidence establishes the difference?
5. What should happen as a result of the evaluation?

This produces:

SPECIFICATION
      ↓
EXPECTED
      ↓
OBSERVED
      ↓
COMPARE
      ↓
RESULT

⸻

79. Relationship to the AI Harness

The AI Harness provides the controlled environment in which AI components can be invoked, observed, constrained, and evaluated.

Conceptually:

AI Harness
    │
    ├── Model
    ├── Prompt
    ├── Context
    ├── Tools
    ├── Inputs
    └── Outputs
          │
          ▼
      Evaluation

The Harness controls the evaluation environment.

Evaluation determines whether the observed behavior satisfies the relevant criteria.

These are separate concerns.

⸻

80. Relationship to the Canon

The Canon establishes foundational principles.

Evaluation operationalizes those principles into observable tests.

For example:

Canon:
Noema must not guess.
Evaluation:
Ambiguous recipient → clarification required.

Or:

Canon:
Unknown mandatory conditions cannot produce READY.
Evaluation:
Authorization unavailable → READY prohibited.

This relationship turns foundational architecture into measurable behavior.

⸻

81. Final Definition

Evaluation is Noema’s systematic mechanism for determining whether AI-assisted and deterministic system behavior conforms to defined Intent semantics, validation rules, Trust requirements, contracts, state transitions, execution boundaries, and canonical invariants.

The core invariant is:

Noema does not evaluate whether an AI output merely appears plausible. It evaluates whether the resulting system behavior conforms to explicit, versioned, and traceable requirements.