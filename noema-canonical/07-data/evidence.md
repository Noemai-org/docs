Evidence

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: 07-data/evidence.md

⸻

1. Definition

Evidence is a provenance-bearing observation, fact, assertion, or signal used by Noema to establish whether a proposition, Intent, Policy condition, or execution state can be trusted.

Evidence answers:

“What supports the claim that this is true?”

This distinction is central to Noema.

Claim
  │
  ▼
Evidence
  │
  ├── Source
  ├── Authority
  ├── Time
  ├── Scope
  └── Provenance
       │
       ▼
     Trust

Evidence is therefore not simply “data.”

It is data considered in relation to a claim or decision.

⸻

2. Purpose

Noema must make consequential decisions in environments where information can be:

* incomplete
* stale
* conflicting
* inferred
* user-provided
* system-generated
* authoritative
* unavailable

Evidence provides the structure needed to reason about these differences.

For example:

User:
"Refund my last payment."
Evidence:
Payment System reports payment #9182
status = SUCCEEDED
amount = $400
customer = 123

The evidence allows Noema to establish what the Intent refers to and whether the requested Action can proceed.

⸻

3. Core Principle

Evidence supports a proposition; it does not automatically make the proposition true.

For example:

Evidence:
CRM says customer_status = ACTIVE

supports:

Claim:
Customer 123 is active.

But whether that claim is authoritative depends on:

source
authority
scope
freshness
policy

⸻

4. Evidence vs Data

Data is information.

Evidence is information in support of a particular claim or decision.

Data:
payment.status = SUCCEEDED
Evidence:
Payment System observed payment.status = SUCCEEDED
at 10:42:12
for payment #123

The second representation provides the provenance necessary to evaluate the first.

⸻

5. Evidence vs Canonical Data

Canonical Data represents authoritative enterprise information.

Evidence records information used to support a decision.

Canonical Data
     │
     ▼
Observation
     │
     ▼
Evidence
     │
     ▼
Trust Decision

Canonical Data can generate strong evidence, but:

Evidence ≠ Canonical Data

⸻

6. Evidence vs Context

Context is the broader runtime information available to Noema.

Evidence is information within that Context that supports a specific proposition.

Context
 ├── Identity
 ├── Policy
 ├── State
 ├── Canonical Data
 └── Evidence

Therefore:

Context describes what is available; Evidence describes what supports a claim.

⸻

7. Evidence vs Inference

This distinction is critical.

Evidence:
Payment #123 belongs to Customer #456.
Inference:
The user probably means Payment #123.

The first is an observed fact.

The second is a conclusion derived from available facts.

Noema must not silently convert inference into evidence.

⸻

8. Evidence vs Model Confidence

LLM confidence is not evidence.

For example:

Model confidence:
0.97

does not establish:

Customer = 123

Evidence must originate from an identifiable source or explicit assertion.

The model may interpret evidence.

It does not manufacture authoritative evidence through confidence.

⸻

9. Evidence and Trust

Evidence is an input to the Trust Engine.

Evidence
   │
   ├── authority
   ├── provenance
   ├── freshness
   ├── consistency
   └── scope
          │
          ▼
     Trust Evaluation

Trust evaluates whether the evidence is sufficient for the requested Action.

⸻

10. Evidence Is Claim-Relative

The same information can be strong evidence for one claim and weak evidence for another.

Example:

CRM:
customer.email = user@example.com

Strong evidence for:

Customer email address

Potentially weak evidence for:

Customer is authorized to transfer $100,000

Evidence must therefore always be evaluated relative to the proposition it supports.

⸻

11. Evidence Types

Noema may encounter several evidence classes:

Canonical Evidence
Observed Evidence
User Evidence
System Evidence
Event Evidence
Historical Evidence
Derived Evidence
Inference

These should remain semantically distinguishable.

⸻

12. Canonical Evidence

Evidence originating directly from the authoritative System of Record for the relevant fact.

Example:

Ledger:
account.balance = $25,000

If the Ledger is authoritative for account balance, this is strong evidence for that proposition.

⸻

13. Observed Evidence

Evidence representing something directly observed by Noema.

Example:

HTTP response:
status = 200
payment.status = REFUNDED

The observation is evidence that the system returned that state.

Whether the returned state is canonical depends on the source.

⸻

14. User Evidence

A user can provide evidence.

Example:

“My employee ID is 4821.”

This may be useful evidence for Intent Resolution.

But user-provided evidence does not automatically establish enterprise truth.

For consequential execution it may require verification.

⸻

15. System Evidence

System Evidence originates from an enterprise system.

Examples:

CRM record
Payment API response
HRIS record
Authorization service response
Database query

Its strength depends on the system’s authority for the relevant claim.

⸻

16. Event Evidence

Events can provide evidence that something occurred.

Example:

payment.refunded

This is evidence that a refund event was emitted.

It is not automatically equivalent to:

payment.status = REFUNDED

unless the event architecture guarantees that semantic relationship.

⸻

17. Historical Evidence

Historical observations may be relevant to decisions.

Example:

Customer previously confirmed:
account = 123

This can be useful for understanding a conversation.

It should not automatically establish that:

account = 123

remains the current authoritative resource.

⸻

18. Derived Evidence

Derived information can support a claim when its derivation is known.

Example:

Evidence:
Customer spent $50,000 in the last 12 months.
Derived from:
transactions 1..482

The derivation chain should be preserved when the derived value affects consequential execution.

⸻

19. Evidence Provenance

Evidence must preserve provenance where consequential.

Conceptually:

Evidence {
    claim
    source
    authority
    observed_at
    effective_at
    scope
    version
    derivation
}

This allows Noema to answer:

Where did this evidence come from?

⸻

20. Evidence Source

Every meaningful Evidence item should identify its source where possible.

Examples:

Payment API
Ledger
CRM
HRIS
Policy Engine
User
Noema
External Provider

An unknown source weakens the ability to establish trust.

⸻

21. Evidence Authority

Source and authority must remain distinct.

Source:
Analytics DB
Authority:
Reporting metrics

The same source may have:

Authority:
customer segmentation
Authority:
account.balance = NO

Evidence must therefore be evaluated against the authority of the specific claim.

⸻

22. Evidence Freshness

Evidence becomes less useful when it becomes stale.

Example:

Evidence:
balance = $10,000
observed 30 minutes ago

For:

"Show me my balance."

this may be acceptable depending on requirements.

For:

"Transfer $9,000."

it may be insufficient.

Freshness is therefore Action-dependent.

⸻

23. Evidence Temporal Semantics

Evidence may contain multiple timestamps:

observed_at
effective_at
created_at
expires_at

These answer different questions.

Example:

effective_at:
payment was refunded at 10:30
observed_at:
Noema learned this at 10:31

This distinction matters for auditability.

⸻

24. Evidence Scope

Evidence must have an explicit or inferable scope.

Possible dimensions:

tenant
organization
resource
attribute
environment
system
time

Evidence from Tenant A should never silently establish a claim about Tenant B.

⸻

25. Evidence Version

When the source provides versions, Noema should preserve them where useful.

Example:

Account
version = 42

This helps determine whether evidence was based on the expected state.

⸻

26. Evidence Strength

Evidence should not be reduced to a single generic confidence score.

Its usefulness depends on several dimensions:

authority
relevance
freshness
specificity
consistency
provenance
completeness

A highly authoritative but stale fact may be less useful than a fresh authoritative observation.

⸻

27. Evidence Relevance

Evidence must directly support the claim being evaluated.

Example:

Claim:
User owns Account #123.
Evidence:
User's email matches CRM email.

This may support the claim.

But:

User lives in the same city as account holder.

is weak or irrelevant evidence for ownership.

⸻

28. Evidence Specificity

Evidence should identify the relevant subject precisely.

Weak:

Account is active.

Strong:

Account #123
status = ACTIVE
observed at 10:42

Specificity reduces ambiguity.

⸻

29. Evidence Completeness

A collection of Evidence may still be insufficient.

Example:

Evidence:
Payment #123 exists.

For a refund decision, Noema may additionally require:

payment.status
payment.amount
refund eligibility
principal authorization

Evidence completeness is determined by the Action and Policy requirements.

⸻

30. Evidence Sufficiency

Sufficiency is contextual.

Evidence sufficient for:
displaying payment status
Evidence insufficient for:
executing a $20,000 refund

The Trust Engine determines sufficiency.

⸻

31. Evidence Conflict

Noema may receive:

Evidence A:
Payment = REFUNDED
Evidence B:
Payment = SUCCEEDED

Noema should preserve both observations.

It should not arbitrarily select the one that makes execution easier.

Instead:

Conflict
   ↓
Authority Resolution
   ↓
Policy
   ↓
Clarify / Escalate / Resolve

⸻

32. Evidence Conflict Does Not Mean Data Error

Conflicting Evidence can occur because:

different observation times
eventual consistency
different system semantics
replication lag
different authority domains
actual inconsistency

Noema should determine which explanation applies rather than assuming corruption.

⸻

33. Negative Evidence

Evidence can establish that something did not occur only under appropriate observation guarantees.

For example:

"No refund found."

does not necessarily establish:

"No refund exists."

The search scope, completeness, and source authority matter.

⸻

34. Absence of Evidence

Absence of evidence is not automatically evidence of absence.

Example:

CRM contains no customer record.

This could mean:

customer does not exist

or:

CRM is not authoritative

or:

lookup failed

or:

record has not propagated

Noema must preserve this distinction.

⸻

35. Evidence Availability

Evidence can have explicit availability states:

AVAILABLE
UNAVAILABLE
STALE
CONFLICTED
INVALID
UNKNOWN

This prevents Noema from treating unavailable information as negative evidence.

⸻

36. Evidence Invalidity

Evidence may become invalid when:

source revoked
authorization revoked
resource deleted
version superseded
observation expires
policy changes

Invalid evidence must not continue satisfying Trust requirements.

⸻

37. Evidence Revocation

Some evidence can be explicitly revoked.

Example:

Authorization evidence:
User is authorized to approve payment.

If the authorization service subsequently reports:

authorization revoked

the previous evidence must no longer be treated as sufficient.

⸻

38. Evidence and Identity

Identity resolution often depends on Evidence.

Example:

Evidence:
authenticated principal = user_123
Evidence:
user_123 owns account_456
Result:
principal may refer to account_456

Identity should be grounded through authoritative relationships wherever required.

⸻

39. Evidence and Intent Resolution

Intent Resolution uses Evidence to resolve ambiguous references.

Example:

“Refund my last payment.”

Candidate payments:

Payment A
Payment B
Payment C

Evidence may include:

timestamps
customer ownership
payment status
conversation references

Noema uses this evidence to resolve the Intent.

⸻

40. Evidence and Ambiguity

If Evidence cannot distinguish candidates:

Payment A → plausible
Payment B → plausible

the result remains ambiguous.

Noema should not manufacture certainty.

Ambiguous
   ↓
Clarification

⸻

41. Evidence and Authorization

Authorization claims require evidence.

For example:

Claim:
Principal can refund Payment #123.

Evidence may come from:

authorization service
role assignment
policy engine
enterprise permissions

User statements about their own authority are not equivalent to authorization evidence.

⸻

42. Evidence and Policy

Policy evaluation may require evidence.

Example:

Policy:
Refunds above $5,000 require manager approval.
Evidence:
refund.amount = $8,000
manager_approval = ABSENT

The Policy Engine can then determine:

approval_required

⸻

43. Evidence and Preconditions

Evidence establishes whether Preconditions hold.

Precondition:
payment.status == SUCCEEDED

Evidence:

Payment System:
payment.status = SUCCEEDED

If the evidence is sufficiently authoritative and fresh, the precondition may be satisfied.

⸻

44. Evidence and Postconditions

After execution:

Action:
refund_payment

Noema may receive:

Evidence:
Payment System:
status = REFUNDED

This evidence supports the Postcondition.

⸻

45. Evidence and Execution

Execution should record the evidence relevant to consequential decisions.

Conceptually:

Execution
   │
   ├── Intent
   ├── Context
   ├── Preconditions
   ├── Evidence
   ├── Action
   ├── Attempts
   └── Outcome

This creates an auditable chain.

⸻

46. Evidence and Outcomes

Outcome determination should use observed Evidence.

For example:

Request submitted
        ↓
Timeout
        ↓
Outcome = UNKNOWN
        ↓
Query System of Record
        ↓
Evidence = payment.status REFUNDED
        ↓
Outcome = SUCCESS

Evidence allows Noema to move from uncertainty to a verified outcome.

⸻

47. Evidence and Failure

Failures can themselves become Evidence.

Example:

Payment API:
HTTP 403

This is evidence that the attempted operation was rejected by the API.

It may support:

Action failed

but does not necessarily establish:

Business operation did not occur

depending on the system’s semantics.

⸻

48. Evidence and Retries

Retries require careful interpretation of Evidence.

Example:

Attempt 1:
timeout
Attempt 2:
payment succeeded

The first timeout does not necessarily mean the first attempt failed.

Noema must determine whether the operation may have been committed before retrying.

This is especially important for non-idempotent Actions.

⸻

49. Evidence and Idempotency

Evidence can establish whether an Action has already been executed.

Example:

Evidence:
idempotency_key = abc123
execution status = COMPLETED

This can prevent duplicate execution.

⸻

50. Evidence and Compensation

Compensation decisions depend on evidence of prior state and completed Actions.

Example:

Evidence:
Order cancelled
Payment not refunded

This may establish that compensation is required.

⸻

51. Evidence and Human Intervention

When automated Trust cannot establish a safe decision, Evidence should be presented to the human operator.

The human should receive:

claim
supporting evidence
source
authority
timestamps
conflicts
missing evidence

rather than merely:

"AI is unsure."

⸻

52. Evidence and Auditability

Evidence is fundamental to auditability.

An audit trail should be able to answer:

What did Noema rely upon when it made this decision?

For example:

Decision:
EXECUTE REFUND
Evidence:
Payment #123 = SUCCEEDED
Principal = user_456
Refund amount = $400
Policy = refunds_under_$5000
Authorization = VALID

⸻

53. Evidence and Explainability

Noema’s explanation should be evidence-based.

Instead of:

“The model thought this was safe.”

Noema should be able to state:

Payment #123 was identified as the target.
The Payment System reported it as refundable.
The principal was authorized.
The applicable refund policy permitted the amount.

The explanation follows the evidence chain.

⸻

54. Evidence and Determinism

Evidence enables deterministic Trust decisions when its semantics are explicit.

Evidence
   ↓
Validation
   ↓
Policy Evaluation
   ↓
Trust State

The model may assist with interpretation.

The resulting evidence evaluation must remain governed by deterministic rules.

⸻

55. Evidence and Confidence

Confidence may be attached to certain forms of evidence, particularly probabilistic or derived evidence.

But confidence should not replace:

authority
provenance
freshness
policy

For authoritative enterprise facts, source authority is often more important than a numerical confidence score.

⸻

56. Evidence and Probabilistic Information

Some evidence is inherently probabilistic.

Example:

Fraud model:
fraud_probability = 0.93

This is valid evidence for:

Claim:
Transaction has elevated fraud risk.

It is not equivalent to:

Claim:
Transaction is fraudulent.

The Data Model must preserve the distinction.

⸻

57. Evidence and Model Output

LLM output can be treated as evidence about:

language interpretation
candidate intent
candidate entities

but generally not as authoritative evidence about enterprise Business State.

Example:

Model:
"User probably means account 123."

This is evidence of a model interpretation, not evidence that account 123 is actually the user’s account.

⸻

58. Evidence and External Systems

External systems may provide useful Evidence.

Examples:

shipping provider
credit bureau
exchange-rate provider
identity provider

The authority of the external source must be defined for the relevant claim.

⸻

59. Evidence Chains

Evidence can depend on other Evidence.

Evidence A:
Transaction records
      ↓
Evidence B:
Total annual spend = $50,000
      ↓
Claim:
Customer qualifies for premium tier

The dependency chain should be preserved when the claim affects execution.

⸻

60. Evidence Graph

Evidence can be modeled as a graph:

Source
  │
  ▼
Observation
  │
  ▼
Evidence
  │
  ▼
Claim
  │
  ▼
Trust Evaluation
  │
  ▼
Decision

This graph allows Noema to trace decisions back to their supporting information.

⸻

61. Evidence Lifecycle

Conceptually:

DISCOVERED
    ↓
CAPTURED
    ↓
VALIDATED
    ↓
ACTIVE
    ↓
SUPERSEDED
    ↓
EXPIRED / REVOKED

Not every Evidence item will pass through every state.

⸻

62. Evidence Capture

When Noema captures consequential Evidence, it should preserve:

source
claim
value
timestamp
scope
authority
version
provenance

This prevents the evidence record from becoming detached from its origin.

⸻

63. Evidence Validation

Evidence validation may verify:

schema
source authenticity
authorization
scope
freshness
consistency
required fields

Validation establishes whether the Evidence can participate in Trust evaluation.

⸻

64. Evidence Supersession

New Evidence may supersede old Evidence.

Example:

Evidence v1:
account.status = ACTIVE
Evidence v2:
account.status = SUSPENDED

Noema should preserve the historical observation while recognizing that v2 may be the current observation.

⸻

65. Evidence Expiration

Evidence can expire when its freshness window closes.

Examples:

authorization evidence
risk assessment
quoted price
account availability
temporary approval

Expired evidence should not silently satisfy current requirements.

⸻

66. Evidence Revocation

Evidence may also become invalid before expiration.

For example:

approval granted
       ↓
approval revoked

The Trust Engine must recognize revocation where the source supports it.

⸻

67. Evidence Retention

Consequential Evidence may need to be retained for:

audit
reconciliation
incident investigation
compliance
execution reconstruction

Retention policies should follow enterprise requirements.

⸻

68. Evidence Minimization

Noema should retain the evidence necessary to establish and audit consequential decisions without unnecessarily duplicating enterprise data.

Evidence should generally reference enterprise resources rather than copying entire enterprise records.

⸻

69. Evidence and Data Boundaries

Evidence must respect:

tenant boundaries
organizational boundaries
authorization
privacy requirements
data classification
retention policy

Evidence must not become a secondary channel for bypassing enterprise access controls.

⸻

70. Evidence and Noema Ownership

Noema may own Evidence records necessary to explain its decisions.

However:

Evidence owned by Noema

does not mean:

underlying enterprise data owned by Noema

The enterprise remains the authority for enterprise Business State.

⸻

71. Evidence and Canonical Data Ownership

The distinction is:

Enterprise:
owns and governs Canonical Data
Noema:
records evidence of observations and decisions involving that data

Noema should preserve references and provenance where possible rather than becoming a shadow System of Record.

⸻

72. Evidence and Context Snapshots

A Context Snapshot may contain references to the Evidence used at that point.

Context Snapshot
      │
      ├── Evidence #1
      ├── Evidence #2
      └── Evidence #3

This makes historical decision reconstruction possible.

⸻

73. Evidence and Long-Running Execution

Long-running executions may accumulate Evidence over time.

T1:
authorization valid
T2:
payment pending
T3:
payment completed
T4:
postcondition verified

Noema should preserve the temporal sequence rather than collapsing these observations into one final value.

⸻

74. Evidence and Reconciliation

Reconciliation produces new Evidence.

Example:

Execution:
UNKNOWN
Query Payment System:
status = REFUNDED
New Evidence:
Payment #123 was refunded.
Result:
Execution Outcome = SUCCESS

This is a core mechanism for recovering from uncertain execution.

⸻

75. Evidence and the Enterprise Action Graph

The Enterprise Action Graph defines possible Actions and relationships.

Evidence grounds the runtime state of those relationships.

Graph:
Payment System can refund Payment.
Evidence:
Payment #123 is refundable.

The graph provides structural capability.

Evidence provides runtime truth.

⸻

76. Evidence and Action Contracts

Action Contracts may require Evidence before execution.

Example:

refund_payment
required evidence:
- payment exists
- payment is refundable
- principal authorized
- amount within policy

The Action Contract therefore defines part of the Evidence requirement.

⸻

77. Evidence and Preconditions

A Precondition can be expressed as a claim requiring Evidence.

Precondition:
Account.status = ACTIVE

Evidence:

Account System:
Account.status = ACTIVE

The Trust Engine evaluates whether that Evidence is sufficient.

⸻

78. Evidence and Postconditions

A Postcondition is similarly a claim that must be supported after execution.

Postcondition:
Payment.status = REFUNDED

Evidence:

Payment System:
Payment.status = REFUNDED

Noema can then mark the Postcondition as satisfied.

⸻

79. Evidence and Unknown

Unknown must remain explicit.

No evidence that refund succeeded.

should not become:

Refund failed.

The correct state may be:

Outcome = UNKNOWN

until sufficient Evidence is obtained.

⸻

80. Evidence and Clarification

Evidence can expose ambiguity.

Example:

Evidence:
Two accounts match the user's description.

This does not mean Evidence failed.

It means the Evidence establishes:

Claim:
Target account cannot yet be uniquely determined.

That can deterministically trigger clarification.

⸻

81. Evidence and Escalation

If Evidence remains insufficient or conflicting after available automated resolution:

Evidence Conflict
       ↓
Trust Evaluation
       ↓
ESCALATE

The escalation package should include the relevant evidence and its provenance.

⸻

82. Evidence and Policy Evaluation

Policy Evaluation consumes Evidence.

Policy
   +
Evidence
   ↓
Policy Evaluation
   ↓
Decision

For example:

Policy:
Refund > $5,000 requires approval.
Evidence:
Refund amount = $8,000.
Manager approval = absent.
Decision:
REQUIRES_APPROVAL

⸻

83. Evidence and Risk

Risk assessment may consume Evidence such as:

transaction amount
account age
historical behavior
location
velocity
fraud score

Risk is itself a decision output, not necessarily canonical data.

The underlying Evidence must remain traceable.

⸻

84. Evidence and Authorization

Authorization should be established through authoritative Evidence where possible.

Identity
   ↓
Permission Evidence
   ↓
Authorization Decision

A model’s belief that a user “seems authorized” is not sufficient for consequential execution.

⸻

85. Evidence and Human Confirmation

User confirmation can become Evidence of explicit consent for a particular Action.

Example:

Noema:
"This will transfer $20,000. Continue?"
User:
"Yes."

This creates evidence that:

the user explicitly confirmed the presented Action

It does not establish unrelated facts such as:

account ownership
balance
authorization

⸻

86. Evidence and Confirmation Scope

Confirmation Evidence must be bound to the Action and Context presented to the user.

A confirmation for:

Transfer $500

must not automatically authorize:

Transfer $5,000

Likewise:

Confirm refund Payment #123

must not automatically confirm:

refund Payment #456

⸻

87. Evidence and Intent Evolution

As Intent changes, its supporting Evidence may change.

Intent v1
→ Payment #123
Clarification
Intent v2
→ Payment #456

Evidence associated with v1 should not silently carry over to v2 if it no longer applies.

⸻

88. Evidence and Intent Composition

For compound Intent, each Action may have its own Evidence requirements.

Intent:
Cancel order + refund payment
Action A:
cancel_order
Evidence set A
Action B:
refund_payment
Evidence set B

Evidence must remain linked to the relevant Action and Resource.

⸻

89. Evidence and Execution Attempts

Evidence should be associated with the execution attempt that produced or consumed it.

Execution
 ├── Attempt 1
 │     └── Evidence
 ├── Attempt 2
 │     └── Evidence
 └── Final Outcome

This is especially important for retries and recovery.

⸻

90. Evidence and Idempotent Recovery

If an execution times out, Noema should seek Evidence about whether the operation committed before retrying.

Attempt 1:
timeout
       ↓
Query:
"idempotency_key = abc123"
       ↓
Evidence:
already completed
       ↓
Do not execute again

⸻

91. Evidence and Compensation

Before compensation, Noema should establish the actual current state.

Expected:
Order cancelled
Payment charged
Evidence:
Order = CANCELLED
Payment = CHARGED

This Evidence supports the compensation decision.

⸻

92. Evidence and Audit Record

A consequential audit record should conceptually connect:

Intent
  ↓
Context
  ↓
Evidence
  ↓
Trust Decision
  ↓
Action
  ↓
Execution
  ↓
Outcome

Evidence is the connective tissue between information and decision.

⸻

93. Evidence Model

Conceptually:

Evidence {
    evidence_id
    claim
    subject
    value
    source
    authority
    scope
    observed_at
    effective_at
    expires_at
    version
    classification
    provenance
    derivation
}

This is a semantic model, not a mandatory storage schema.

⸻

94. Evidence Set

A Trust decision may require multiple Evidence items.

EvidenceSet {
    evidence[]
    purpose
    scope
    collected_at
}

Example:

EvidenceSet: refund_payment
- identity evidence
- payment evidence
- authorization evidence
- policy evidence
- risk evidence

⸻

95. Evidence Claim

Evidence should be associated with an explicit claim.

Conceptually:

Claim {
    subject
    predicate
    object
}

Example:

subject:
Payment #123
predicate:
status
object:
SUCCEEDED

This allows evidence to be reasoned about systematically.

⸻

96. Evidence Relationships

Evidence
   ├── supports → Claim
   ├── sourced_from → System
   ├── derived_from → Evidence
   ├── supersedes → Evidence
   ├── contradicts → Evidence
   ├── scoped_to → Resource
   └── used_by → Trust Decision

⸻

97. Evidence Graph Example

Payment System
      │
      ▼
Observation
      │
      ▼
Evidence #42
      │
      ▼
Claim:
Payment #123 is refundable
      │
      ▼
Precondition
      │
      ▼
Trust Evaluation
      │
      ▼
EXECUTE

⸻

98. Evidence Quality

Evidence quality can be evaluated across dimensions:

Dimension	Question
Authority	Is the source authoritative for this claim?
Relevance	Does it support the current proposition?
Freshness	Is it sufficiently current?
Specificity	Does it identify the exact subject?
Provenance	Can the source be traced?
Completeness	Are required facts present?
Consistency	Does it conflict with stronger evidence?
Scope	Does it apply to this tenant/resource/environment?

No single dimension should automatically determine Trust.

⸻

99. Evidence Is Not a Confidence Score

A common mistake is:

Evidence confidence = 95%

and therefore:

execute

Noema should instead evaluate:

Evidence
+
Authority
+
Policy
+
Risk
+
Authorization
+
Freshness
+
Ambiguity

and produce a deterministic Trust state.

⸻

100. Core Invariants

Invariant 1

Evidence supports a claim; it does not automatically establish truth.

Invariant 2

Evidence must remain distinguishable from Canonical Data.

Invariant 3

Evidence must remain distinguishable from Context.

Invariant 4

Evidence must remain distinguishable from model inference.

Invariant 5

Model confidence is not a substitute for Evidence.

Invariant 6

Evidence must be evaluated relative to the claim it supports.

Invariant 7

Evidence source and authority must remain distinct.

Invariant 8

Consequential Evidence should preserve provenance.

Invariant 9

Consequential Evidence should preserve relevant temporal metadata.

Invariant 10

Evidence freshness is Action- and Policy-dependent.

Invariant 11

Evidence must have an understood scope.

Invariant 12

Evidence from one tenant or organizational boundary must not silently establish claims in another.

Invariant 13

Evidence completeness and Evidence sufficiency are distinct.

Invariant 14

Evidence may be strong for one claim and irrelevant to another.

Invariant 15

Conflicting Evidence must be preserved rather than arbitrarily discarded.

Invariant 16

Authority, not source count, determines which Evidence should prevail when sources conflict.

Invariant 17

Absence of Evidence must not automatically be interpreted as Evidence of absence.

Invariant 18

Unavailable Evidence must not silently become negative Evidence.

Invariant 19

Unknown must remain explicitly distinguishable from false.

Invariant 20

Stale Evidence must not satisfy requirements that demand current state.

Invariant 21

Invalid or revoked Evidence must not continue satisfying Trust requirements.

Invariant 22

Historical Evidence must remain distinguishable from current Evidence.

Invariant 23

Derived Evidence should preserve its derivation chain when consequential.

Invariant 24

User-provided Evidence does not automatically establish enterprise truth.

Invariant 25

Model-generated Evidence about enterprise state does not automatically establish enterprise truth.

Invariant 26

Events provide Evidence of occurrences but do not automatically establish persistent state unless their semantics guarantee it.

Invariant 27

Authorization claims must be supported by appropriate authorization Evidence.

Invariant 28

Identity resolution should use appropriate Evidence before consequential execution.

Invariant 29

Evidence supporting one Intent or Action must not silently transfer to a different Intent, Resource, or Action.

Invariant 30

User confirmation Evidence must be bound to the specific Action and Context presented for confirmation.

Invariant 31

Evidence required for consequential execution should be captured sufficiently to reconstruct the Trust decision.

Invariant 32

Evidence should respect enterprise data, privacy, organizational, and authorization boundaries.

Invariant 33

Noema may own Evidence records without becoming the owner of the underlying enterprise Business State.

Invariant 34

Evidence used for retries and recovery must account for the possibility that an operation succeeded even when the original response was unavailable.

Invariant 35

Evidence should support deterministic Trust decisions rather than replace them.

Invariant 36

When available Evidence cannot establish a safe execution condition, Noema must transition into the appropriate deterministic state—such as clarification, escalation, retry, or rejection—rather than manufacture certainty.

⸻

101. Final Definition

Evidence is provenance-bearing information associated with a claim and used by Noema to establish, validate, or challenge the conditions required for Intent resolution, Trust evaluation, Action execution, and Outcome verification.

The fundamental relationship is:

                 SOURCE
                   │
                   ▼
               OBSERVATION
                   │
                   ▼
                EVIDENCE
                   │
                   ▼
                 CLAIM
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
      Authority Freshness Scope
          │        │        │
          └────────┼────────┘
                   ▼
             TRUST ENGINE
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     EXECUTE    CLARIFY    ESCALATE
        │
        ▼
      ACTION
        │
        ▼
    OBSERVATION
        │
        ▼
      EVIDENCE
        │
        ▼
      OUTCOME

And the key Noema principle is:

Evidence does not tell Noema what to do. Evidence establishes what Noema can legitimately know; Trust determines what that knowledge permits Noema to do.