Outcome Taxonomy

Status: Foundational
Version: 0.1
Domain: Taxonomy
Canonical Path: taxonomy/outcome-taxonomy.md

⸻

1. Definition

An Outcome is Noema’s canonical representation of what resulted from an Intent and its associated execution lifecycle.

An Outcome records the observed result of processing or executing an Intent.

It answers:

What happened?

It does not answer:

What did the Actor intend?

That is the responsibility of Intent.

It does not answer:

Was the Intent permitted to proceed?

That is the responsibility of Trust.

It does not answer:

What Actions were structurally required?

That is the responsibility of the Action Graph.

It does not answer:

What was contractually permitted?

That is the responsibility of Action Contracts.

Therefore:

Intent
    ↓
Validation
    ↓
Trust
    ↓
Action Graph
    ↓
Action Contracts
    ↓
Execution
    ↓
Outcome

The Outcome is the canonical representation of what Noema can establish about the result.

⸻

2. Core Principle

Noema must distinguish intended result from observed result.

An Actor may intend:

Transfer ₦50,000 to John.

The resulting Outcome may be:

TRANSFER_COMPLETED

or:

TRANSFER_FAILED

or:

TRANSFER_UNKNOWN

The Outcome must represent what actually happened or what can be established about what happened.

Therefore:

Intent ≠ Outcome

An intended result must never be represented as though it were an observed result merely because execution was authorized.

⸻

3. Outcome as an Observed State

An Outcome represents the state established by execution, verification, external evidence, or explicit lifecycle termination.

Conceptually:

Execution
    ↓
Observed Events
    ↓
Verification
    ↓
Outcome

The Outcome may be based on:

* successful execution responses
* authoritative external state
* postcondition verification
* explicit failure responses
* bounded execution termination
* human intervention
* compensation results
* unresolved external state

The source of the Outcome must remain identifiable.

⸻

4. Outcome Does Not Mean Success

Outcome is a neutral semantic category.

An Outcome may represent:

* success
* failure
* partial completion
* blocking
* cancellation
* expiration
* waiting
* rejection
* unknown result
* compensation
* abandonment

Therefore:

Outcome ≠ Success

Success is one possible Outcome classification.

⸻

5. Outcome vs Intent

Intent represents the Actor’s desired objective.

Outcome represents what resulted from processing that objective.

Example:

Intent:
    Replace my card.
Outcome:
    Replacement request created.

The Outcome does not redefine the original Intent.

Similarly:

Intent:
    Send ₦50,000.
Outcome:
    Payment request rejected.

The rejected payment does not mean the Actor intended rejection.

⸻

6. Outcome vs Action State

Action state describes the state of an individual Action.

Outcome describes the resulting semantic state of the relevant execution or Intent.

For example:

Action A → COMPLETED
Action B → FAILED
Action C → NOT_STARTED

may produce:

Outcome:
    PARTIALLY_COMPLETED

Action state therefore contributes evidence to Outcome construction but is not itself the Outcome taxonomy.

⸻

7. Outcome vs Trust State

Trust establishes execution eligibility.

Outcome records what happened after or during execution.

For example:

Trust:
    READY
Execution:
    FAILED
Outcome:
    FAILED

A failed Outcome does not imply that the original Trust decision was incorrect.

Likewise:

Trust:
    BLOCKED

may result in an Outcome such as:

BLOCKED

without any Action having executed.

Trust and Outcome therefore represent different dimensions.

⸻

8. Outcome vs Execution State

Execution State describes operational progress.

Outcome describes the semantic result of that progress.

Example:

Execution:
    COMPLETED
Outcome:
    PAYMENT_CONFIRMED

Or:

Execution:
    UNKNOWN
Outcome:
    PAYMENT_STATUS_UNKNOWN

Execution State is therefore an input to Outcome determination.

⸻

9. Outcome Identity

Every canonical Outcome should have an explicit identity.

Conceptually:

Outcome {
    id
    intent_id
    intent_version
    status
    classification
    result
    evidence
    provenance
    timestamps
    execution_reference
}

The exact schema belongs to the canonical Outcome ontology.

An Outcome identity must remain stable once established.

Material changes should produce a new Outcome version or explicit correction relationship rather than silently rewriting history.

⸻

10. Outcome Status

Outcome status represents the high-level lifecycle state.

A canonical taxonomy may include:

SUCCESS
PARTIAL
FAILED
BLOCKED
CANCELLED
EXPIRED
WAITING
UNKNOWN

The exact statuses may evolve.

The important principle is that materially different result states must remain distinguishable.

⸻

11. Success

A successful Outcome indicates that the required completion conditions were satisfied according to the applicable semantics.

Example:

Intent:
    Renew card.
Outcome:
    SUCCESS

Success should not be inferred merely because an Action returned a successful transport response.

Where required, Noema should verify the relevant postconditions or authoritative external state.

⸻

12. Partial Completion

Partial completion occurs when some required execution components completed while others did not.

Example:

A → COMPLETED
B → COMPLETED
C → FAILED
D → NOT_STARTED

Outcome:

PARTIAL

Partial completion must remain explicit.

It must not be silently converted into:

SUCCESS

or:

FAILED

unless the governing Outcome semantics explicitly define that aggregation.

⸻

13. Failure

A failed Outcome indicates that the required execution objective could not be completed according to established failure semantics.

Examples include:

* Action failure
* contract rejection
* unrecoverable dependency failure
* bounded retry exhaustion
* verified external rejection
* required postcondition failure

Failure should be supported by observable evidence where available.

⸻

14. Blocked Outcome

A blocked Outcome indicates that execution could not proceed because a required condition prevented execution.

Examples:

Approval required
Authorization unavailable
Required capability unavailable
Mandatory dependency unresolved

Blocked differs from failed execution.

For example:

Action never executed
Reason:
    approval missing

should not be represented as:

EXECUTION_FAILED

unless the applicable semantics explicitly define it that way.

⸻

15. Cancelled Outcome

Cancellation indicates that the Intent or execution was explicitly terminated through a cancellation event.

Cancellation may originate from:

* Actor request
* authorized system action
* policy
* lifecycle expiration
* execution control

Cancellation is distinct from failure.

CANCELLED ≠ FAILED

The cancellation source should be recorded.

⸻

16. Expired Outcome

An expired Outcome indicates that the relevant Intent or execution opportunity exceeded its defined temporal validity.

Example:

Intent valid until:
18:00
Execution attempt:
18:15
Outcome:
EXPIRED

Expiration must be governed by explicit temporal semantics.

Noema must not infer expiration merely because an operation took a long time.

⸻

17. Waiting Outcome

A waiting Outcome indicates that the lifecycle remains active but cannot yet complete.

Examples:

* waiting for approval
* waiting for external processing
* waiting for human intervention
* waiting for asynchronous confirmation
* waiting for a scheduled execution point

Waiting is not failure.

WAITING ≠ FAILED

⸻

18. Unknown Outcome

An Unknown Outcome indicates that Noema cannot establish whether the intended operation succeeded or failed.

Example:

REQUEST_PAYMENT
      ↓
network timeout
      ↓
external result unknown

The Outcome must remain:

UNKNOWN

if the external system may have processed the request.

Noema must not convert uncertainty into failure merely because confirmation was not received.

⸻

19. Unknown Is Not Failure

This distinction is foundational.

Consider:

Request sent
Response lost
External state unknown

The correct semantic state may be:

UNKNOWN

not:

FAILED

The system must preserve uncertainty until authoritative evidence establishes the result.

⸻

20. Outcome Classification

Outcome status alone may be insufficient to describe the result.

An Outcome may therefore contain a classification.

Conceptually:

Outcome Classification
COMPLETION
FAILURE
BLOCKING
CANCELLATION
EXPIRATION
WAITING
UNCERTAINTY
COMPENSATION

Classification should remain distinct from detailed domain result codes.

⸻

21. Domain Result

A domain result describes what occurred within the relevant business domain.

Example:

status = SUCCESS
domain_result:
    replacement_request_id = req_123

The domain result should preserve authoritative identifiers and values supplied by the relevant external system.

Noema must not invent domain results.

⸻

22. Outcome Evidence

Every material Outcome should be supported by evidence appropriate to the result.

Evidence may include:

* Action response
* external system confirmation
* authoritative resource state
* postcondition verification
* execution event
* human decision
* compensation result
* timeout information
* contract result

Evidence provenance should be retained.

⸻

23. Outcome Provenance

Outcome provenance records why Noema established a particular result.

Conceptually:

Outcome:
    SUCCESS
Evidence:
    payment_provider_confirmation
Source:
    payment_provider
Timestamp:
    ...
Verification:
    payment.status = SETTLED

Provenance allows the Outcome to be reconstructed without requiring private model reasoning.

⸻

24. Authoritative External State

External systems remain authoritative for business state within their domains.

For example:

Payment Provider
    ↓
payment.status = SETTLED

may provide authoritative evidence for a payment Outcome.

Noema should record the evidence rather than claiming ownership of the external business state.

⸻

25. Outcome Verification

An execution response does not always establish the final business Outcome.

For example:

CREATE_PAYMENT
    ↓
HTTP 202 Accepted

may mean:

Request accepted

rather than:

Payment settled

The Outcome taxonomy must distinguish request acceptance from verified business completion where the domain requires it.

⸻

26. Postcondition Verification

Where an Action Contract defines a required postcondition, Outcome construction may require verification.

Example:

Expected:
    card.status = ACTIVE

Noema may verify:

card.status = ACTIVE

before establishing:

SUCCESS

If verification cannot establish the required condition, the Outcome may remain:

UNKNOWN

or another appropriate state.

⸻

27. Outcome Granularity

Outcomes may exist at multiple levels.

Examples:

Action Outcome
Graph Outcome
Intent Outcome
Composite Outcome

These levels must not be conflated.

An individual Action may succeed while the overall Intent remains partially completed.

⸻

28. Action Outcome

An Action Outcome describes the result of one executable Action.

Example:

Action:
    VERIFY_CARD
Outcome:
    SUCCESS

The Action Outcome may include:

* action identity
* execution identity
* status
* result
* evidence
* failure information
* timestamps
* contract reference

⸻

29. Graph Outcome

A Graph Outcome aggregates the state of the Action Graph.

Example:

A → COMPLETED
B → COMPLETED
C → FAILED

Graph Outcome:

PARTIAL

Graph aggregation rules must be explicit.

The graph must not claim success merely because one terminal node succeeded.

⸻

30. Intent Outcome

The Intent Outcome represents the resulting state of the Intent lifecycle.

Example:

Intent:
    Renew card.
Graph:
    all mandatory Actions completed.
Outcome:
    SUCCESS

The Intent Outcome is the primary semantic result exposed to downstream systems and, where appropriate, the Actor.

⸻

31. Composite Outcomes

A composite Intent may produce multiple related Outcomes.

Example:

Intent:
    Close account,
    transfer balance,
    notify me.

Possible Action Outcomes:

Close Account → SUCCESS
Transfer Balance → FAILED
Notification → SUCCESS

The composite Outcome must preserve component results.

It must not collapse materially different results into a misleading single state.

⸻

32. Outcome Aggregation

Aggregation rules must be explicit.

For example:

Mandatory A = SUCCESS
Mandatory B = SUCCESS
Mandatory C = SUCCESS
→ SUCCESS

Whereas:

Mandatory A = SUCCESS
Mandatory B = FAILED
→ PARTIAL or FAILED

depending on the Intent’s partial-execution semantics.

The aggregation rule must be defined by the applicable execution and Intent semantics.

⸻

33. Mandatory vs Optional Actions

Outcome aggregation must distinguish mandatory and optional Actions.

Example:

Core payment → SUCCESS
Optional notification → FAILED

The Intent may still achieve its primary objective.

However, the notification failure must remain observable.

Therefore:

Primary Outcome:
SUCCESS
Associated Action Outcome:
NOTIFICATION_FAILED

No optional failure should be silently discarded.

⸻

34. Outcome and Partial Execution Policy

The Intent may define whether partial execution is acceptable.

If partial execution is prohibited:

A = SUCCESS
B = FAILED

must not automatically produce:

SUCCESS

The resulting Outcome must reflect the applicable atomicity semantics.

⸻

35. Outcome and Compensation

Compensation produces additional Outcome information.

Example:

A → SUCCESS
B → SUCCESS
C → FAILED
Compensation:
B_COMPENSATE → SUCCESS
A_COMPENSATE → SUCCESS

The final Outcome must distinguish:

Original execution:
PARTIAL / FAILED
Compensation:
SUCCESS

Compensation success does not rewrite the original execution history.

⸻

36. Compensation Is Not Rollback

A compensating Action does not necessarily restore the exact original state.

Therefore:

COMPENSATED ≠ ROLLED_BACK

The Outcome should preserve the actual observed state and the compensation result.

⸻

37. Retry and Outcome

Retries must not create ambiguous duplicate Outcomes.

For example:

Attempt 1:
UNKNOWN
Attempt 2:
SUCCESS

The canonical Outcome should represent the established final state while retaining the attempt history.

Retry history must remain auditable.

⸻

38. Idempotent Execution

Where an Action is idempotent, repeated execution may produce the same domain state.

The Outcome should preserve:

* attempt identity
* idempotency key where applicable
* final authoritative result
* relevant provider response

Idempotency must not cause Noema to assume success without evidence.

⸻

39. Duplicate Execution

If duplicate execution occurs, the Outcome must identify the resulting domain state where possible.

Example:

Payment request executed twice.
Provider:
    duplicate prevented.

Outcome:

SUCCESS

with evidence that the provider enforced idempotency.

If the provider produced two payments, the Outcome must represent the actual observed state.

⸻

40. Outcome Corrections

An Outcome may later be corrected when new authoritative evidence becomes available.

Example:

Initial:
UNKNOWN
Later:
Payment provider confirms SETTLED
Updated:
SUCCESS

The original Outcome must remain reconstructible.

The correction should be represented explicitly.

Conceptually:

Outcome v1
    ↓
new authoritative evidence
    ↓
Outcome v2

⸻

41. Outcome Supersession

A later Outcome may supersede an earlier provisional Outcome.

Supersession must not erase history.

The relationship should identify:

* previous Outcome
* new Outcome
* reason
* evidence
* timestamp
* authority source

⸻

42. Provisional Outcomes

Some Outcomes may initially be provisional.

Example:

REQUEST_ACCEPTED

may indicate that the request entered an external system but final completion has not been established.

A provisional Outcome should be explicitly marked.

It must not be presented as final success.

⸻

43. Final Outcomes

A final Outcome is one for which the relevant completion semantics have been satisfied or the lifecycle has been definitively terminated.

Examples:

SUCCESS
FAILED
CANCELLED
EXPIRED

An Outcome may remain non-final when:

WAITING
UNKNOWN

and the lifecycle permits further evidence or action.

The exact finality semantics belong to the execution lifecycle.

⸻

44. Outcome Finality

Outcome finality must be explicit.

Conceptually:

Outcome {
    status
    final: true | false
}

A non-final Outcome may transition when additional authoritative evidence becomes available.

A final Outcome should not be silently replaced.

⸻

45. Outcome Temporal Semantics

An Outcome should preserve relevant timestamps.

Examples:

execution_started_at
execution_completed_at
observed_at
verified_at
finalized_at

These timestamps answer different questions and should not be conflated.

⸻

46. Outcome Ordering

Where multiple Actions produce related Outcomes, causal ordering should remain reconstructible.

Example:

VERIFY_ELIGIBILITY
    ↓
SUCCESS
REQUEST_REPLACEMENT
    ↓
SUCCESS
DELIVERY
    ↓
FAILED

Outcome records should retain references to the Actions and graph relationships that produced them.

⸻

47. Outcome Dependencies

An Outcome may depend on another Outcome.

Example:

Eligibility Outcome:
SUCCESS
Replacement Outcome:
SUCCESS

The replacement Outcome may therefore reference the eligibility evidence that permitted execution.

Outcome dependencies should remain explicit where they materially affect interpretation.

⸻

48. Outcome and Human Intervention

Human intervention may produce an Outcome.

Example:

HUMAN_REVIEW
    ↓
APPROVED

The approval itself is evidence of a governance event.

It should not automatically be interpreted as successful completion of the underlying business Action.

For example:

Approval:
SUCCESS
Transfer:
PENDING

These are distinct Outcomes.

⸻

49. Outcome and Clarification

Clarification normally belongs to Intent resolution rather than execution Outcome.

For example:

Intent:
    recipient ambiguous
Outcome:
    not yet executable

The canonical lifecycle should ordinarily represent this as an Intent/Resolution state rather than falsely representing it as execution failure.

If the system produces an execution-level terminal result due to unresolved Intent, the relationship must remain explicit.

⸻

50. Outcome and Trust

Trust may determine whether execution is allowed.

Outcome records what happened.

Example:

Trust:
BLOCKED
Reason:
approval required

No execution may occur.

The resulting lifecycle may therefore terminate as:

BLOCKED

The Outcome must preserve the relationship to the Trust decision without treating Trust itself as an Outcome.

⸻

51. Outcome and Policy

Policies may affect Outcome interpretation.

Example:

Policy:
Transfer requires approval above threshold.
Approval:
not obtained.
Outcome:
BLOCKED

Policy determines the requirement.

The Outcome records the resulting lifecycle state.

⸻

52. Outcome and External Failure

External systems may return domain-specific failures.

Examples:

INSUFFICIENT_FUNDS
ACCOUNT_SUSPENDED
RESOURCE_NOT_FOUND
PROVIDER_UNAVAILABLE
RATE_LIMITED
VALIDATION_REJECTED

Noema should preserve the external failure code where appropriate.

It may additionally map it into a canonical Outcome classification.

For example:

External:
INSUFFICIENT_FUNDS
Canonical:
FAILED

The original provider-specific evidence should remain available.

⸻

53. Outcome Error Taxonomy

Outcome errors should be machine-readable.

Conceptual categories include:

EXECUTION_REJECTED
PRECONDITION_FAILED
DEPENDENCY_FAILED
CONTRACT_VIOLATION
CAPABILITY_UNAVAILABLE
AUTHORIZATION_REJECTED
EXTERNAL_SYSTEM_ERROR
TIMEOUT
RETRY_EXHAUSTED
POSTCONDITION_FAILED
COMPENSATION_FAILED
UNKNOWN_EXTERNAL_RESULT

The taxonomy may evolve by domain.

Error codes should not replace the higher-level Outcome classification.

⸻

54. Outcome Reason

An Outcome should provide a canonical reason where one exists.

Example:

status:
FAILED
reason:
PAYMENT_PROVIDER_REJECTED
details:
provider_code = INSUFFICIENT_FUNDS

Reason codes should be deterministic and machine-readable.

Human-readable explanations may accompany them.

⸻

55. Outcome Evidence Strength

Evidence may differ in authority.

For example:

Actor statement
Model inference
Execution response
External authoritative state

The Outcome should distinguish evidence provenance.

A model-generated statement that an Action succeeded must not be treated as equivalent to authoritative external confirmation.

⸻

56. Outcome Confidence

A model or system may attach confidence metadata to an Outcome.

However:

confidence ≠ truth

A confidence score must not override authoritative evidence.

For example:

Model confidence:
0.99
External result:
UNKNOWN

The canonical Outcome remains:

UNKNOWN

until authoritative evidence establishes the result.

⸻

57. Outcome Determinism

Where Outcome construction is governed by deterministic aggregation and verification rules, equivalent inputs should produce equivalent classifications.

Conceptually:

Action Results
+
Contract Semantics
+
Intent Semantics
+
Verification Rules
+
Evidence
+
Rule Versions

should produce a reproducible Outcome classification.

Model variability must not silently alter canonical Outcome state.

⸻

58. Outcome Versioning

An Outcome should be versioned when its canonical representation materially changes.

Conceptually:

Outcome v1:
UNKNOWN
new evidence
Outcome v2:
SUCCESS

The previous version remains reconstructible.

Outcome versioning supports:

* auditability
* reproducibility
* correction
* external reconciliation
* incident investigation

⸻

59. Outcome Provenance Chain

A complete Outcome provenance chain may include:

Intent
    ↓
Intent Version
    ↓
Action Graph
    ↓
Action
    ↓
Action Contract
    ↓
Execution Attempt
    ↓
External Evidence
    ↓
Verification
    ↓
Outcome

This chain allows Noema to explain how an observed result was established without exposing private model reasoning.

⸻

60. Outcome Observability

Noema should make it possible to inspect:

* Intent identity
* Intent version
* graph identity
* graph version
* Action identity
* execution identity
* contract identity
* attempt history
* timestamps
* evidence
* failures
* retries
* compensation
* human intervention
* Outcome state
* Outcome version

Outcome observability is necessary for operational diagnosis and auditability.

⸻

61. Outcome Audit History

Material Outcome changes should be auditable.

Example:

Outcome v1
    UNKNOWN
       ↓
Provider confirmation
       ↓
Outcome v2
    SUCCESS

The audit history should preserve:

* previous state
* new state
* event causing transition
* evidence
* source
* timestamp
* actor or system responsible for the transition

⸻

62. Outcome Immutability

Historical Outcomes must not be silently rewritten.

Once an Outcome has been persisted, material changes should be represented through:

* versioning
* correction
* supersession
* reconciliation

rather than destructive mutation.

This ensures that historical execution behavior remains reconstructible.

⸻

63. Outcome Reconciliation

External systems may later provide information that differs from the initial Outcome.

Example:

Noema:
UNKNOWN
Provider:
SETTLED

Reconciliation should establish the new Outcome from authoritative evidence.

The reconciliation event must remain auditable.

⸻

64. Outcome Conflict

Different evidence sources may disagree.

Example:

Execution response:
FAILED
External state:
COMPLETED

Noema must not silently choose one result.

The conflict should be represented explicitly and resolved according to defined authority and reconciliation rules.

Possible state:

CONFLICTED

if the canonical Outcome model supports it.

Otherwise, the Outcome may remain:

UNKNOWN

until authoritative reconciliation establishes the result.

⸻

65. Outcome and External Authority

When evidence conflicts, authority should be determined by the relevant domain and Action Contract.

For example:

Payment provider

may be authoritative for payment state.

Identity provider

may be authoritative for identity state.

Noema should not claim universal authority over external domain state.

⸻

66. Outcome and Durable Execution

Durable execution requires Outcome state to survive:

* process restart
* worker failure
* network interruption
* retry
* failover
* deployment
* infrastructure replacement

Outcome persistence must therefore be part of the durable execution model.

An in-memory result is not sufficient canonical Outcome state.

⸻

67. Outcome and Recovery

Recovery may resume execution from a previously persisted state.

The recovery process must distinguish:

Action not executed
Action executing
Action completed
Action failed
Action outcome unknown

This prevents recovery from incorrectly repeating an Action whose external result is already unknown or potentially committed.

⸻

68. Outcome and Idempotency

Idempotency is especially important when recovering from unknown execution states.

Example:

Payment request sent
No response
Worker crashes

Before retrying, Noema must determine whether:

* the Action is safely retryable
* an idempotency key exists
* authoritative status can be queried
* the provider guarantees duplicate prevention

Outcome semantics must preserve the uncertainty until it is resolved.

⸻

69. Outcome and Stale State

An Outcome may become stale when external state changes after execution.

For example:

T1:
Account = ACTIVE
T2:
Action succeeds
T3:
Account = SUSPENDED

The historical Outcome remains:

Action succeeded at T2

The later business state does not retroactively change what happened at T2.

Noema must distinguish historical Outcome from current external state.

⸻

70. Outcome and Temporal Truth

An Outcome is a statement about what was established at a particular point in time.

Therefore:

Outcome:
Payment SETTLED at T1

does not necessarily mean:

Payment remains SETTLED at T2

Current business state belongs to the authoritative external system.

Outcome records historical execution truth.

⸻

71. Outcome Notification

An Outcome may be communicated to:

* the Actor
* downstream systems
* audit systems
* observability systems
* external consumers

The representation may differ by consumer.

However, the canonical Outcome must remain stable.

Presentation must not alter semantic state.

⸻

72. Outcome Explanation

A human-readable explanation may accompany an Outcome.

Example:

Status:
FAILED
Reason:
INSUFFICIENT_FUNDS
Explanation:
The payment provider rejected the transfer because the source
account did not have sufficient available funds.

The explanation is derived from canonical evidence.

It must not invent facts absent from the Outcome record.

⸻

73. Outcome Redaction

Outcome records may contain sensitive business information.

Access to Outcome details must therefore respect the applicable security and data-governance boundaries.

Redaction for a consumer must not mutate the canonical Outcome.

Conceptually:

Canonical Outcome
        ↓
Authorization
        ↓
Consumer-specific representation

⸻

74. Outcome Retention

Outcome retention should follow the applicable:

* audit requirements
* regulatory requirements
* business requirements
* privacy requirements
* operational requirements

Retention policies must not destroy information required to reconstruct consequential execution unless the governing policy explicitly permits such deletion.

⸻

75. Outcome Taxonomy Extensibility

The taxonomy must support domain-specific outcomes without destroying canonical semantics.

For example:

Canonical:
SUCCESS
Domain:
CARD_REPLACEMENT_CREATED

or:

Canonical:
FAILED
Domain:
PAYMENT_PROVIDER_INSUFFICIENT_FUNDS

Domain-specific codes should map to canonical classifications.

⸻

76. Outcome Classification Hierarchy

A useful conceptual hierarchy is:

Outcome
│
├── Completion
│   └── SUCCESS
│
├── Partial Completion
│   └── PARTIAL
│
├── Failure
│   └── FAILED
│
├── Blocking
│   └── BLOCKED
│
├── Waiting
│   └── WAITING
│
├── Cancellation
│   └── CANCELLED
│
├── Expiration
│   └── EXPIRED
│
└── Uncertainty
    └── UNKNOWN

The taxonomy may later introduce additional canonical classes where architectural requirements justify them.

⸻

77. Outcome State Transitions

Outcome transitions must occur through defined events and semantics.

Conceptually:

WAITING
   ↓
SUCCESS

or:

WAITING
   ↓
FAILED

or:

UNKNOWN
   ↓
SUCCESS

A transition must have an identifiable cause.

The system must not change Outcome state merely because a model generated a different interpretation.

⸻

78. Invalid Outcome Transitions

The system should reject transitions that violate the Outcome lifecycle.

For example, a finalized historical Outcome should not silently transition because a new execution attempt occurred.

A new attempt should produce new execution evidence and, where necessary, a new Outcome version or reconciliation event.

⸻

79. Outcome Aggregation Invariants

When aggregating Action Outcomes:

1. Mandatory failures must not disappear.
2. Unknown mandatory results must not become success.
3. Partial completion must remain explicit.
4. Optional failures must remain observable.
5. Compensation results must remain distinct.
6. Historical attempts must remain reconstructible.
7. External authoritative evidence must be preserved.
8. Aggregation rules must be deterministic where defined.

⸻

80. Outcome Invariants

Invariant 1

Outcome represents observed or established result, not Actor intention.

Invariant 2

Intent and Outcome are separate semantic objects.

Invariant 3

Execution authorization does not imply execution success.

Invariant 4

Unknown must not silently become failed or successful.

Invariant 5

Partial execution must remain explicit.

Invariant 6

Action Outcomes must not automatically be treated as Intent Outcomes.

Invariant 7

Outcome aggregation rules must be explicit.

Invariant 8

External systems remain authoritative for their business state.

Invariant 9

Outcome evidence and provenance must be retained for material results.

Invariant 10

Historical Outcomes must remain reconstructible.

Invariant 11

Retries must not silently erase previous execution attempts.

Invariant 12

Compensation does not imply rollback.

Invariant 13

A successful request response does not necessarily establish successful business completion.

Invariant 14

Model confidence does not establish Outcome truth.

Invariant 15

Outcome state changes must be caused by defined events, evidence, or deterministic reconciliation.

Invariant 16

A later Outcome must not silently rewrite historical execution.

Invariant 17

Current external business state must not be confused with historical execution Outcome.

Invariant 18

Outcome representation must preserve uncertainty where authoritative evidence is unavailable.

⸻

81. Canonical Outcome Model

Conceptually:

Outcome {
    id
    intent_id
    intent_version
    classification
    status
    finality
    result
    reason
    domain_code
    evidence
    provenance
    graph_id
    graph_version
    action_results
    execution_references
    created_at
    observed_at
    verified_at
    finalized_at
    version
}

The exact schema belongs to the canonical ontology.

The model illustrates the required semantic dimensions rather than prescribing an implementation schema.

⸻

82. Canonical Outcome Flow

The canonical lifecycle is:

Intent
    ↓
Action Graph
    ↓
Action Contract
    ↓
Execution
    ↓
Action Results
    ↓
Evidence
    ↓
Verification
    ↓
Outcome Classification
    ↓
Outcome

Where necessary:

Outcome
    ↓
Reconciliation
    ↓
Updated Outcome

The historical record remains preserved.

⸻

83. Canonical Outcome Questions

The Outcome taxonomy can be reduced to seven questions:

1. What was attempted?
2. What Actions actually executed?
3. What did each Action produce?
4. What evidence establishes those results?
5. Did the Intent’s required completion conditions hold?
6. What remains unknown or unresolved?
7. Is the resulting Outcome final?

These questions provide the basis for canonical Outcome construction.

⸻

84. Relationship to the Noema Architecture

The Outcome taxonomy fits into the broader Noema lifecycle:

                    HUMAN
                      │
                      ▼
                   INTENT
                      │
                      ▼
               INTERPRETATION
                      │
                      ▼
                 RESOLUTION
                      │
                      ▼
                VALIDATION
                      │
                      ▼
                   TRUST
                      │
                      ▼
                ACTION GRAPH
                      │
                      ▼
              ACTION CONTRACTS
                      │
                      ▼
                 EXECUTION
                      │
                      ▼
                VERIFICATION
                      │
                      ▼
                  OUTCOME

Each layer answers a different question.

Intent:
    What does the Actor want?
Validation:
    Is the Intent structurally and semantically valid?
Trust:
    May it proceed?
Action Graph:
    What Actions and dependencies fulfill it?
Action Contract:
    What does each Action permit and require?
Execution:
    What was performed?
Outcome:
    What resulted?

⸻

85. Fundamental Boundary

The fundamental Outcome boundary is:

Execution
    ↓
Observed Evidence
    ↓
Outcome

The Outcome must not be generated merely from what Noema intended to execute.

It must be grounded in what execution and authoritative evidence establish.

Therefore:

Executable Graph
    ≠
Successful Outcome

and:

Execution Attempt
    ≠
Verified Business Result

⸻

86. Final Definition

The Outcome Taxonomy is Noema’s canonical classification and representation of the results established through Intent processing, Action Graph execution, verification, external evidence, and lifecycle termination.

An Outcome distinguishes:

* success from failure
* failure from uncertainty
* blocking from execution failure
* partial completion from complete success
* cancellation from failure
* historical execution state from current external business state
* observed evidence from model inference
* provisional results from final results

Its central invariant is:

Noema must represent what happened according to available authoritative evidence, not what it expected to happen, what it intended to happen, or what a model believes happened.

Therefore:

Intent
    ↓
Validation
    ↓
Trust
    ↓
Action Graph
    ↓
Action Contracts
    ↓
Execution
    ↓
Evidence
    ↓
Verification
    ↓
Outcome

The Outcome is the canonical semantic boundary between what Noema attempted and what Noema can establish actually resulted.