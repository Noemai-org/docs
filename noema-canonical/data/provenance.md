Provenance

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/provenance.md

⸻

1. Definition

Provenance is the record of where a piece of information came from, when it was observed, how it was interpreted, and how it contributed to an Intent, Trust decision, Action, or Outcome.

Provenance answers:

“Why does Noema believe this, and where did that belief come from?”

It is therefore a foundational property of Noema’s data model, Trust Engine, and audit system.

⸻

2. Purpose

Noema operates across multiple sources:

Enterprise APIs
Databases
Events
Documentation
Policies
Workflows
Human input
Configuration
External systems

These sources may disagree, change over time, or provide incomplete information.

A value without provenance is often insufficient for consequential execution.

For example:

status = APPROVED

is materially weaker than:

status = APPROVED
source = HR System
observed_at = 2026-08-27T09:31:02Z
resource = employee/123

⸻

3. Core Principle

Noema should know not only what information it has, but why that information is considered relevant and where it originated.

⸻

4. Provenance Is Not Data Ownership

Provenance records the origin of information.

It does not transfer ownership of that information to Noema.

For example:

Enterprise Ledger
    owns:
    account balance
Noema
    records:
    balance observed = $10,000
    source = Ledger
    observed_at = ...

The Ledger remains authoritative.

⸻

5. Provenance and Trust

Trust decisions depend on Evidence.

Evidence without provenance is difficult to evaluate.

Therefore:

Source
  ↓
Observation
  ↓
Evidence
  ↓
Trust Evaluation
  ↓
Decision

Provenance establishes the relationship between these layers.

⸻

6. Provenance and Determinism

Noema’s Trust Engine is deterministic.

That requires the inputs to a decision to be identifiable.

For example:

Trust Decision:
EXECUTE
Based on:
Evidence #42
Policy #17
Context Snapshot #81

Without provenance, the same decision may become impossible to reconstruct.

⸻

7. Provenance and the Model

The model may infer:

"The user probably means payment #123."

Noema should distinguish that inference from authoritative evidence.

For example:

Model inference
    ↓
candidate resource = payment/123
    ↓
Enterprise lookup
    ↓
confirmed resource = payment/123

The provenance of the candidate and the confirmation are different.

⸻

8. Provenance Categories

Noema may distinguish provenance by source type:

User
Enterprise System
Policy
Configuration
Documentation
Event
Human Operator
Model
Derived Computation
Noema Internal State

Each source carries different epistemic weight.

⸻

9. User-Originated Information

A user may provide:

“Refund my last payment.”

The provenance is:

source = USER
source_id = interaction/request
observed_at = ...

The statement represents user Intent.

It does not automatically establish the identity of the payment.

⸻

10. Enterprise-Originated Information

An enterprise system may provide:

payment_id = 123
status = SUCCEEDED
amount = 500

Provenance should identify:

system
resource
operation
observation time
response/version identity

⸻

11. Policy-Originated Information

A policy may establish:

refunds above $10,000 require approval

Its provenance should identify:

policy
version
effective period
organization/scope

⸻

12. Documentation-Originated Information

Documentation may describe:

POST /payments/{id}/refund

This can contribute to an Action Contract.

But documentation is not equivalent to runtime authorization or current system behavior.

Provenance makes this distinction explicit.

⸻

13. Event-Originated Information

An event might state:

payment.refunded

Provenance should preserve:

event_id
source_system
event_type
event_version
emitted_at
received_at

The event is evidence of an occurrence, not necessarily a complete representation of current state.

⸻

14. Human-Originated Information

A human operator may explicitly approve an Action.

For example:

Operator:
approved refund of payment/123

The provenance should identify the approving principal and relevant authorization context.

⸻

15. Model-Originated Information

Model output is a distinct provenance class.

Example:

MODEL
Inference:
payment candidate = payment/123
confidence = 0.91

This must not be represented as though:

ENTERPRISE_SYSTEM
confirmed:
payment/123

The distinction is essential.

⸻

16. Derived Information

Noema may derive information from multiple sources.

Example:

Evidence A:
payment amount = $8,000
Evidence B:
refund policy threshold = $10,000
Derived:
approval not required

The derived conclusion should retain references to the inputs from which it was produced.

⸻

17. Provenance Graph

Conceptually:

User Input
    │
    ▼
Intent
    │
    ├───────────────┐
    ▼               ▼
Evidence A       Evidence B
    │               │
    └───────┬───────┘
            ▼
      Derived Fact
            │
            ▼
      Trust Evaluation
            │
            ▼
          Action

The graph allows Noema to trace a decision backward to its sources.

⸻

18. Provenance as a Graph

A useful conceptual model is:

Source
  ↓
Observation
  ↓
Evidence
  ↓
Claim
  ↓
Decision
  ↓
Action
  ↓
Outcome

Each edge answers:

“How did this information contribute to what happened?”

⸻

19. Provenance Record

Conceptually:

Provenance {
    provenance_id
    source_type
    source_id
    source_system
    resource_ref
    observed_at
    received_at
    version
    scope
    integrity
}

The exact schema is implementation-dependent.

⸻

20. Source Identity

A source should be identifiable.

For example:

source_type = ENTERPRISE_SYSTEM
source_system = Stripe

is more useful than:

source = API

when multiple APIs exist.

⸻

21. Source Resource

Where applicable, provenance should identify the resource from which information originated.

resource_type = payment
resource_id = 123

This allows later verification.

⸻

22. Source Operation

The operation that produced the information may also matter.

For example:

GET /payments/123

versus:

GET /payments/123/refund-status

Both may refer to the same resource while providing different evidence.

⸻

23. Observation Time

Every time-sensitive observation should have an observation timestamp.

observed_at = 10:32:15

This prevents historical observations from being mistaken for current facts.

⸻

24. Received Time

Noema may also record:

received_at = 10:32:18

This distinguishes:

when the source observed something

from:

when Noema received it

The distinction is important in distributed systems.

⸻

25. Event Time vs Processing Time

For events:

event_time

may differ from:

processing_time

Both may be relevant to provenance.

⸻

26. Version

Sources may evolve.

A provenance record may therefore include:

schema_version
api_version
event_version
policy_version
contract_version

where relevant.

⸻

27. Provenance and Temporal Validity

Information may have an effective period.

Example:

Policy v4
effective_from = Jan 1
effective_until = Jun 30

Noema must be able to determine whether the policy was applicable when a decision occurred.

⸻

28. Provenance and Freshness

Provenance enables freshness evaluation.

Example:

Evidence:
balance = $100,000
observed_at = 09:00

At:

10:30

the evidence may be too old for a high-risk transfer.

The value has not necessarily become false.

It has become potentially stale.

⸻

29. Provenance and Evidence Freshness

A Trust Policy may define:

Evidence:
balance
Maximum age:
60 seconds

Noema can then evaluate:

current_time - observed_at

against the policy.

⸻

30. Provenance and Contradictory Evidence

Multiple sources may produce conflicting information.

Example:

CRM:
customer.status = ACTIVE
Identity System:
customer.status = SUSPENDED

Provenance allows Noema to preserve both observations rather than collapsing them prematurely.

⸻

31. Source Authority

When sources conflict, Noema may need an authority hierarchy.

For example:

Identity Provider
    >
CRM

for identity status.

Authority should be explicitly modeled rather than inferred ad hoc.

⸻

32. Authority Is Contextual

A source is not universally authoritative.

For example:

Ledger
    authoritative for balances
CRM
    authoritative for customer segmentation

Provenance should therefore capture the source’s semantic role where relevant.

⸻

33. Provenance and Canonical Data

Canonical Data should identify its authoritative source.

Example:

Canonical:
Customer #123
Authority:
CRM
Observed:
2026-08-27T10:20

This allows Noema to distinguish canonical information from derived or cached representations.

⸻

34. Provenance and Context

Context is a collection of information relevant to an Intent.

Each consequential Context element should be traceable to its origin where practical.

Context
 ├── identity → Identity Provider
 ├── balance → Ledger
 ├── policy → Policy Store
 └── payment → Payment System

⸻

35. Provenance and Intent Resolution

Intent resolution may produce:

user said:
"refund my last payment"
resolved resource:
payment/123

The resolution should be traceable.

For example:

Candidate:
payment/123
Evidence:
latest completed payment
timestamp = ...

This helps distinguish inference from confirmation.

⸻

36. Provenance and Ambiguity

Ambiguity may arise because provenance is insufficient.

Example:

"Cancel the subscription."

Noema finds:

subscription A
subscription B

Both have plausible provenance.

The correct response is not to fabricate certainty.

Noema should enter clarification.

⸻

37. Provenance and Clarification

A clarification can resolve provenance ambiguity.

Example:

Noema:
Which subscription do you mean?
User:
The business subscription.

The new user statement becomes additional provenance contributing to Intent resolution.

⸻

38. Provenance and Confidence

Confidence should not replace provenance.

A model may have:

confidence = 0.98

but if the underlying evidence is weak, the decision may still require clarification.

Conversely, authoritative enterprise evidence may be decisive even without a probabilistic confidence score.

⸻

39. Provenance and Trust Evidence

Trust evaluation should be able to answer:

Which evidence supported this decision?

For example:

Trust Decision:
EXECUTE
Evidence:
E1 payment ownership confirmed
E2 payment status = SUCCEEDED
E3 user authorized for refund
E4 amount below approval threshold

Each Evidence item should have provenance.

⸻

40. Provenance and Policy Evaluation

A policy decision should identify:

policy version
policy scope
inputs
evaluation time
result

This makes policy evaluation auditable.

⸻

41. Provenance and Authorization

Authorization evidence should identify its source.

For example:

principal:
user/123
authorization source:
IAM
role:
finance-admin
observed_at:
...

Noema should not merely record:

authorized = true

without being able to identify why.

⸻

42. Provenance and Action Contracts

Action Contracts may originate from:

API schema
OpenAPI document
SDK
documentation
human configuration
enterprise integration

The contract should preserve its provenance.

This matters when the underlying API changes.

⸻

43. Provenance and Integration Mapping

An integration mapping such as:

"completed" → SUCCEEDED

should identify where the mapping came from.

For example:

source = Payment API integration
version = 3

This makes semantic interpretation traceable.

⸻

44. Provenance and Execution

An Execution should preserve references to the information that led to it.

Conceptually:

Execution
 ├── Intent
 ├── Context
 ├── Trust Decision
 ├── Action Contract
 └── Evidence

Each can lead back through provenance.

⸻

45. Provenance and Outcome

Outcome observations also require provenance.

Example:

Outcome:
refund succeeded
Source:
Payment System
operation:
GET /payments/123
observed_at:
10:45

This distinguishes verified success from assumed success.

⸻

46. Provenance and Unknown Outcomes

If an Action times out:

Action:
refund_payment
Result:
UNKNOWN

the timeout itself has provenance:

source = network/client
observed_at = ...

It does not establish that the external Action failed.

⸻

47. Provenance and Reconciliation

Reconciliation compares observations from different points in time or different systems.

Attempt:
UNKNOWN
Later observation:
Payment System → REFUNDED

Provenance establishes that the later observation came from the authoritative system.

⸻

48. Provenance and Recovery

During recovery, Noema should know:

what it knew before failure

and:

what it knows now

Provenance provides the temporal distinction.

⸻

49. Provenance and Persistence

Provenance is not necessarily the raw source data.

Persistence may store:

Evidence
+
Provenance metadata

while retaining only references to the original enterprise record.

This minimizes unnecessary duplication.

⸻

50. Provenance and Data Minimization

Provenance should itself follow data minimization.

Noema generally does not need to store an entire source payload simply to establish:

source = Ledger
resource = account/123
observed_at = ...
claim = balance = $10,000

unless the payload is required for audit, recovery, or another explicit purpose.

⸻

51. Provenance and Integrity

Provenance is useful only if its integrity can be trusted.

Depending on requirements, Noema may use:

hashes
signatures
immutable records
source-issued identifiers
checksums

to establish that Evidence has not been altered.

⸻

52. Source-Signed Evidence

Some enterprise systems may provide signed or otherwise verifiable responses.

Noema can preserve the relevant verification information.

This strengthens the Trust Engine’s evidence model.

⸻

53. Provenance and Trust Levels

Evidence can have different epistemic strength.

Conceptually:

Authoritative source
      ↓
Verified observation
      ↓
Derived fact
      ↓
Model inference
      ↓
Unverified assumption

Noema should not collapse these into one undifferentiated category.

⸻

54. Provenance and Model Inference

A model inference can be useful.

For example:

Inference:
"last payment" = payment/123

But it remains:

INFERENCE

until supported or confirmed by appropriate evidence.

This distinction is fundamental to safe agentic execution.

⸻

55. Provenance and Human Confirmation

Human confirmation may elevate an unresolved interpretation.

Example:

Model:
candidate = payment/123
User:
Yes, that payment.

The resulting Intent state now has additional user-originated provenance.

⸻

56. Provenance and Derived Facts

Derived facts should retain their dependency graph.

Example:

A:
payment.amount = $5,000
B:
policy.threshold = $10,000
Derived:
approval_required = false

If either A or B changes, the derived result may need reevaluation.

⸻

57. Provenance and Dependency Graphs

Conceptually:

Evidence A ──┐
             ├──> Derived Fact ──> Trust Decision
Evidence B ──┘

This makes dependencies explicit.

⸻

58. Provenance and Policy Changes

If a policy changes:

Policy v12:
approval required > $10k
Policy v13:
approval required > $5k

historical decisions must continue to reference v12 where v12 was the policy used.

⸻

59. Provenance and Action Contract Changes

Likewise:

Action Contract v3

must remain distinguishable from:

Action Contract v4

for historical executions.

⸻

60. Provenance and Schema Evolution

Provenance records should remain interpretable as Noema evolves.

Important metadata may include:

provenance_schema_version
source_version
semantic_version

where necessary.

⸻

61. Provenance and Causality

Provenance should support causal relationships.

Example:

Evidence E1
    ↓
Trust Decision D1
    ↓
Action A1
    ↓
Outcome O1

This allows Noema to answer:

“What caused this Action to be executed?”

⸻

62. Provenance and Auditability

Auditability requires more than timestamps.

A useful audit trail must establish:

who
what
when
where
based on what
under which policy
using which Action Contract
with what result

Provenance supplies much of the “based on what” component.

⸻

63. Provenance and Explainability

When Noema explains a decision:

“The transfer was blocked because the beneficiary account was not verified.”

the system should be able to identify:

claim:
beneficiary unverified
source:
Identity System
observation:
...
policy:
transfer-policy.v7

This turns explanation from narrative generation into evidence-backed reconstruction.

⸻

64. Provenance and Accountability

For consequential Actions, Noema should be able to demonstrate that its decision was based on identifiable information.

This is especially important for:

financial Actions
identity Actions
access-control Actions
employment Actions
compliance Actions
security Actions

⸻

65. Provenance and Enterprise Boundaries

Provenance must preserve organizational scope.

Example:

source:
HR System
organization:
Nigeria Operations

A piece of Evidence originating from one organizational boundary should not automatically be treated as applicable to another.

⸻

66. Provenance and Tenant Boundaries

Similarly:

Tenant A

and:

Tenant B

must have independent provenance contexts.

A source record from Tenant A cannot silently become Evidence for Tenant B.

⸻

67. Provenance and Data Boundaries

Provenance should identify relevant boundaries such as:

tenant
organization
environment
region
system
resource

where these affect interpretation or authorization.

⸻

68. Provenance and Source Reliability

Historical source behavior may inform operational decisions, but reliability should not be confused with authority.

For example:

Source reliability = 99.9%

does not mean:

source is authoritative for every claim

These are separate concepts.

⸻

69. Provenance and Source Failure

If a source is unavailable:

Ledger unavailable

Noema should not infer:

balance = 0

unless an explicit policy permits that inference.

Provenance makes the absence of authoritative Evidence visible.

⸻

70. Provenance and Absence

Absence of Evidence is itself meaningful.

For example:

No authorization record found.

is not automatically equivalent to:

User is unauthorized.

The policy must determine what the absence means.

⸻

71. Provenance and Negative Evidence

Negative Evidence should identify how it was established.

Example:

No active subscription found

could originate from:

subscription system query

at a specific time.

The query semantics and observation time matter.

⸻

72. Provenance and Query Semantics

A source response is only meaningful in the context of the query that produced it.

For example:

GET /payments?status=succeeded&limit=1

may support:

“This is the most recent succeeded payment.”

but not necessarily:

“This is the user’s only payment.”

Provenance should preserve enough query context to avoid overinterpreting evidence.

⸻

73. Provenance and Source Scope

Evidence should carry scope where relevant.

Example:

balance:
$10,000
scope:
USD operating account

Without scope, the value may be ambiguous.

⸻

74. Provenance and Resource Identity

Resource identity should be explicit.

resource_type = account
resource_id = 123

rather than relying entirely on natural-language labels.

⸻

75. Provenance and Identity

Identity claims should preserve their source.

Example:

principal:
user/123
identity_provider:
Okta
authentication_time:
...

This allows authorization decisions to reference an identifiable identity assertion.

⸻

76. Provenance and Authentication

Authentication evidence and authorization evidence are distinct.

Authentication:
Who are you?
Authorization:
What are you allowed to do?

Provenance should preserve both where relevant.

⸻

77. Provenance and Authorization Chains

An authorization decision may depend on:

User identity
   ↓
Role membership
   ↓
Permission
   ↓
Resource scope
   ↓
Action

Each claim may have a different source.

The resulting authorization decision should retain those dependencies.

⸻

78. Provenance and Configuration

Configuration can influence execution.

For example:

refund approval threshold = $10,000

The provenance should identify:

configuration source
version
scope
effective time

where that configuration affects Trust.

⸻

79. Provenance and Environment

Environment can matter.

production
staging
development

An Action Contract or Evidence from staging should not silently support production execution.

⸻

80. Provenance and Integration Environment

For every external observation, Noema should be able to distinguish:

production API
sandbox API
test fixture
mock

when relevant.

⸻

81. Provenance and Synthetic Data

Test or synthetic Evidence must never be mistaken for production Evidence.

The provenance should explicitly identify:

source_type = TEST

or equivalent.

⸻

82. Provenance and Security

Provenance metadata can itself be sensitive.

For example:

which system a company uses
which administrator approved an Action
which account was accessed

Therefore provenance must be subject to appropriate access controls.

⸻

83. Provenance and Redaction

When source information is sensitive, Noema may retain:

source identifier
claim
timestamp
integrity metadata

without exposing the complete underlying payload.

⸻

84. Provenance and Retention

Provenance retention should be aligned with the Evidence and decision it supports.

If a Trust Decision must remain auditable for seven years, the provenance required to explain it may also need to survive for seven years.

⸻

85. Provenance and Deletion

Deleting source data does not necessarily invalidate a historical provenance record.

Noema may retain a minimal historical record such as:

source
resource reference
claim
timestamp
integrity information

subject to applicable enterprise and legal requirements.

⸻

86. Provenance and Persistence

Provenance should be durable whenever it supports a consequential decision.

For example:

Transfer executed

should not lose:

why the beneficiary was considered valid

simply because a temporary cache expired.

⸻

87. Provenance and Recovery

Recovery may require determining:

What evidence was used before the crash?

Persisted provenance provides that answer.

⸻

88. Provenance and Revalidation

Recovery may compare:

Historical Evidence

with:

Current Evidence

and determine whether the original decision remains valid.

⸻

89. Provenance and Reconciliation

Reconciliation should preserve both sides:

Expected:
refund pending
Observed:
refund succeeded

with provenance for each observation.

⸻

90. Provenance and Outcome Verification

An Outcome should be considered verified only when supported by appropriate Evidence.

Action response:
202 Accepted

does not necessarily establish:

refund completed

Provenance allows Noema to distinguish the immediate response from the later verified Outcome.

⸻

91. Provenance and Asynchronous Execution

For asynchronous Actions:

Action submitted
      ↓
operation_id = 987
      ↓
event received
      ↓
operation completed

provenance should link these observations.

⸻

92. Provenance and External Operation Identity

External operation IDs are important provenance anchors.

Noema Execution:
exec_123
External Operation:
op_987

The relationship should be durable.

⸻

93. Provenance and Event Ordering

When multiple events arrive:

event A
event B
event C

provenance should preserve:

event IDs
event timestamps
source sequence
versions

where available.

This helps Noema reason about ordering and causality.

⸻

94. Provenance and Duplicate Events

Duplicate events should remain distinguishable from independent events when possible.

An event_id allows Noema to recognize:

same event received twice

rather than:

two separate events

⸻

95. Provenance and Event Authenticity

Where the source provides authenticity guarantees, Noema should preserve the relevant identifiers or verification results.

⸻

96. Provenance and Model Traceability

Noema may retain model metadata relevant to a consequential inference:

model
model version
prompt/context version
inference identifier
timestamp

subject to privacy and retention requirements.

The purpose is traceability, not treating the model as an authoritative source.

⸻

97. Provenance and Model Confidence

If model confidence contributes to a decision, the confidence value may be persisted as part of the inference provenance.

However:

confidence ≠ evidence

and:

confidence ≠ authorization

⸻

98. Provenance and Deterministic Clarification

Suppose the model produces:

candidate = customer/123
confidence = 92%

but two customers match.

The provenance graph exposes:

two plausible candidates

The Trust Engine can deterministically transition to:

CLARIFY

rather than selecting one arbitrarily.

⸻

99. Provenance and Intent Language

An executable Intent should be traceable back to the information from which it was constructed.

Conceptually:

Natural Language
      ↓
Intent Representation
      ↓
Resolved Intent
      ↓
Executable Intent

Each transformation may have provenance.

⸻

100. Provenance and Intent Composition

For compound Intent:

“Cancel the subscription and refund the last payment.”

Noema may produce:

Intent
 ├── cancel_subscription
 └── refund_payment

Each component should preserve its relationship to the original user Intent and supporting Evidence.

⸻

101. Provenance and Planning

A plan should identify why each Action is included.

Plan:
1. Verify payment
2. Refund payment
3. Cancel subscription

The plan may reference:

Intent
Policy
Action dependencies
Context

This creates traceability from Intent to execution plan.

⸻

102. Provenance and Compensation

Compensation decisions should identify the Evidence that established the need for compensation.

Example:

Subscription creation succeeded
Payment capture failed

This can lead to:

compensate subscription creation

The causal chain should remain traceable.

⸻

103. Provenance and Failure

Failure records should distinguish:

source-reported failure
Noema-observed failure
timeout
unknown outcome
policy rejection
authorization rejection

Each has different provenance.

⸻

104. Provenance and Human Intervention

When a human intervenes:

operator approved

the provenance should capture:

principal
authorization context
decision
time
reason

where required.

⸻

105. Provenance and Audit Reconstruction

A mature Noema audit query should be able to traverse:

Outcome
 ← Execution
 ← Action
 ← Trust Decision
 ← Evidence
 ← Provenance
 ← Source

This is the provenance chain.

⸻

106. Provenance and Explainability Boundary

Noema should explain decisions using persisted semantic facts and provenance.

It should not rely solely on regenerated model narratives.

A generated explanation may be useful as a presentation layer, but the underlying explanation must remain evidence-backed.

⸻

107. Provenance and Source Substitution

An enterprise may replace an integration.

Payment Provider A
        ↓
Payment Provider B

Historical provenance must still identify Provider A for historical observations.

Current executions may use Provider B.

⸻

108. Provenance and Integration Evolution

This allows Noema to preserve:

historical truth

while supporting:

current integration architecture

without rewriting history.

⸻

109. Provenance and Data Lineage

Provenance is the foundation of Noema’s data lineage.

Source
 ↓
Observation
 ↓
Evidence
 ↓
Context
 ↓
Decision
 ↓
Action
 ↓
Outcome

Lineage makes the flow of information through the system explicit.

⸻

110. Provenance and Semantic Lineage

Noema should care not only about:

“Where did this value come from?”

but also:

“How did this value become meaningful to the decision?”

For example:

API response
   ↓
field extraction
   ↓
semantic normalization
   ↓
Evidence
   ↓
policy input

This is semantic provenance.

⸻

111. Provenance and Normalization

Different systems may express the same concept differently.

Payment API:
"completed"
Noema:
SUCCEEDED

Provenance should preserve the source representation and the normalization that produced the canonical Noema interpretation where necessary.

⸻

112. Provenance and Transformation

A transformed value should retain its source relationship.

Example:

$10,000

becomes:

10000 USD

The transformation should not destroy provenance.

⸻

113. Provenance and Aggregation

Aggregated values may depend on multiple sources.

Example:

total outstanding = $15,000

may derive from:

Invoice A = $5,000
Invoice B = $10,000

The resulting value should preserve its dependencies where it affects execution.

⸻

114. Provenance and Derived Authorization

Similarly:

role membership
+
resource ownership
+
policy

may derive:

authorized = true

The authorization result should preserve those dependencies.

⸻

115. Provenance and Source Freshness

Different sources may have different freshness characteristics.

real-time API
event stream
hourly batch
daily report

Provenance allows Trust policies to account for those differences.

⸻

116. Provenance and Reliability

Reliability metadata may be useful operationally:

source availability
latency
error rate

but it should not replace semantic authority.

A highly reliable source can still be the wrong source for a particular claim.

⸻

117. Provenance and Trust Policy

Trust policies may evaluate provenance attributes such as:

source authority
freshness
integrity
scope
identity
version

This makes Evidence quality explicit.

⸻

118. Provenance and Risk

Higher-risk Actions should generally require stronger provenance.

For example:

Low risk:
read employee name
High risk:
terminate employee access

The latter may require authoritative identity, authorization, policy, and resource evidence.

⸻

119. Provenance and Risk-Adaptive Evidence

Conceptually:

Risk
 ↓
Required Evidence
 ↓
Required Provenance
 ↓
Trust threshold

The more consequential the Action, the stronger the evidence lineage should be.

⸻

120. Provenance and Enterprise Policy

Enterprises may define which sources are acceptable for particular decisions.

Example:

Beneficiary verification:
must originate from Identity System

Noema should not substitute an arbitrary source merely because it contains a plausible value.

⸻

121. Provenance and Source Allowlisting

For sensitive Actions, policies may explicitly specify:

allowed source types
required source systems
minimum freshness
required integrity

This creates deterministic evidence requirements.

⸻

122. Provenance and Evidence Sufficiency

A Trust Engine should be able to determine:

Evidence sufficient

versus:

Evidence insufficient

Provenance supplies information needed for this evaluation.

⸻

123. Provenance and Evidence Conflict

When Evidence conflicts:

Source A says:
ACTIVE
Source B says:
SUSPENDED

Noema should not hide the conflict.

It should retain both provenance chains and allow Policy to determine the appropriate transition:

CLARIFY
ESCALATE
REJECT
REVALIDATE

⸻

124. Provenance and Uncertainty

Uncertainty should be represented explicitly.

Examples:

unknown source
stale observation
conflicting evidence
unverified inference
incomplete scope

These are preferable to silently converting uncertainty into certainty.

⸻

125. Provenance and Negative Assertions

A statement such as:

"No matching account exists."

requires provenance showing:

what system was queried
what query was made
when it was made
what scope was searched

Otherwise the assertion is difficult to validate.

⸻

126. Provenance and Query Reproducibility

For important Evidence, Noema may need enough information to reconstruct the source query.

Conceptually:

source
operation
parameters
timestamp
resource scope
response identifier

Sensitive parameters should be appropriately protected.

⸻

127. Provenance and API Responses

Noema need not retain every API response.

It should retain sufficient metadata to establish:

which response
from which system
at what time
for which resource
supported which claim

⸻

128. Provenance and Database Queries

If Noema obtains Evidence from a database or query service, provenance should identify the relevant logical source and query context rather than exposing unnecessary raw data.

⸻

129. Provenance and Documentation

Documentation-derived information should have an explicit epistemic classification.

For example:

Documentation says:
endpoint accepts DELETE

does not establish:

endpoint currently permits this caller

Runtime evidence is required for the latter.

⸻

130. Provenance and Configuration Drift

If configuration changes:

approval threshold:
$10,000 → $5,000

provenance allows Noema to determine which configuration applied to a historical decision.

⸻

131. Provenance and System Drift

External systems evolve.

An API may change:

status:
completed → settled

Provenance and integration versions allow Noema to identify how the old and new representations were interpreted.

⸻

132. Provenance and Reproducibility

A consequential decision should ideally be reproducible at the semantic level.

That means Noema should be able to reconstruct:

Intent
Context
Evidence
Policy
Action Contract
Trust inputs

from persisted provenance.

⸻

133. Provenance and Replay

Replay uses provenance to reconstruct the historical environment.

But replay must remain non-executing unless explicitly authorized.

⸻

134. Provenance and Historical Truth

The objective is not to reconstruct what would be true today.

It is to reconstruct:

What Noema knew, from which sources, at the time the decision was made.

That distinction is essential.

⸻

135. Provenance and Current Truth

Current truth must be obtained from current authoritative sources.

Historical provenance cannot substitute for current state when making a new consequential decision.

⸻

136. Provenance and Decision Revalidation

A historical decision may therefore be represented as:

Historical:
EXECUTE
Current:
requires revalidation

This avoids treating historical Evidence as permanently authoritative.

⸻

137. Provenance and Temporal Reasoning

Noema should distinguish at least:

event occurred at
source observed at
Noema received at
decision made at
Action executed at
Outcome observed at

These timestamps can differ.

⸻

138. Provenance and Clock Skew

Distributed systems may have clock differences.

Therefore timestamps should not automatically be treated as perfect causal ordering.

Where available, Noema should preserve:

sequence numbers
event IDs
causal references

alongside timestamps.

⸻

139. Provenance and Causal Ordering

For example:

Event A
sequence = 101
Event B
sequence = 102

may establish stronger ordering than:

A timestamp = 10:00:01
B timestamp = 10:00:00

when clocks are unreliable.

⸻

140. Provenance and Source Identity Changes

If a source system is renamed, migrated, or replaced, historical provenance must retain the identity applicable at the time.

⸻

141. Provenance and Integration Ownership

Noema should know:

which integration produced the observation

but integration ownership does not imply business-state ownership.

⸻

142. Provenance and External References

Stable external identifiers improve traceability:

transaction_id
event_id
operation_id
request_id
resource_id

These should be preserved where useful.

⸻

143. Provenance and Correlation

A correlation ID may connect:

user request
Noema execution
external request
external event
outcome

This creates end-to-end lineage.

⸻

144. Provenance and Audit Queries

An auditor should be able to ask:

“Why was this Action executed?”

and navigate:

Execution
 → Trust Decision
 → Policy
 → Evidence
 → Source

without relying on runtime logs.

⸻

145. Provenance and Accountability Boundary

The provenance chain should establish what Noema did with information.

It does not establish that the source information itself was universally correct.

This distinction is important:

Noema can prove:
"We received X from System Y."

That is different from:

"System Y was objectively correct."

⸻

146. Provenance and Source Trust

Source trust may itself be governed by enterprise policy.

For example:

Payment status:
must come from Payment System
Identity:
must come from Identity Provider

The provenance model makes these constraints enforceable.

⸻

147. Provenance and Evidence Hierarchy

A practical conceptual hierarchy:

Authoritative verified observation
        ↓
Authoritative observation
        ↓
Trusted derived fact
        ↓
Human assertion
        ↓
Model inference
        ↓
Unverified assumption

This is not a universal ranking.

Policy determines the acceptable Evidence for each Action.

⸻

148. Provenance and Noema’s Trust Boundary

The Trust Engine should not ask only:

“What value do we have?”

It should ask:

“What value do we have, where did it come from, how fresh is it, what scope does it apply to, and is that source acceptable for this decision?”

That is provenance-aware Trust evaluation.

⸻

149. Provenance and Action Selection

Action selection may depend on provenance.

For example:

beneficiary verified by authoritative system

may permit:

TRANSFER

while:

beneficiary inferred from user text

may only permit:

CLARIFY

⸻

150. Provenance and Execution Permission

Provenance can therefore become part of the preconditions for execution.

Example:

Precondition:
beneficiary_identity
    source = Identity System
    freshness < 5 minutes

If the condition is not satisfied:

do not execute

⸻

151. Provenance and Preconditions

A Precondition can reference provenance attributes.

Precondition:
payment.status = SUCCEEDED
Required source:
Payment System
Maximum age:
60 seconds

This creates a deterministic execution gate.

⸻

152. Provenance and Postconditions

Postconditions also require provenance.

Postcondition:
payment.status = REFUNDED

should be verified through an acceptable source.

A successful API response alone may not satisfy the postcondition.

⸻

153. Provenance and Outcome Verification

The difference is:

Action response

versus:

Verified Outcome

Provenance establishes the evidence behind the latter.

⸻

154. Provenance and Failure Recovery

If an external operation is uncertain:

timeout

Noema can use provenance to query the authoritative system and establish:

succeeded
failed
still pending

⸻

155. Provenance and Reconciliation Loop

Conceptually:

UNKNOWN
   ↓
Query authoritative source
   ↓
Observation
   ↓
Evidence
   ↓
Provenance
   ↓
Reconciliation
   ↓
RESOLVED

⸻

156. Provenance and Enterprise Action Graph

The Enterprise Action Graph can incorporate provenance.

For example:

System
   ↓
Capability
   ↓
Action
   ↓
Resource
   ↓
Evidence Source

This allows Noema to understand not just what an enterprise system can do, but how its information should be trusted.

⸻

157. Provenance and Action Graph Construction

Action Graph nodes may originate from:

API schemas
documentation
events
configuration
policies
runtime observations

Each source should remain identifiable.

⸻

158. Provenance and Canonicalization

When multiple sources describe the same concept:

CRM customer
Identity customer
Billing customer

Noema may construct a canonical relationship.

The provenance of that relationship must remain visible.

⸻

159. Provenance and Entity Resolution

Entity resolution is particularly provenance-sensitive.

Example:

"John"

could match:

customer/123
customer/456

The evidence supporting the selected entity must be explicit.

If insufficient:

CLARIFY

⸻

160. Provenance and Intent Resolution

Intent Resolution therefore becomes:

Candidate generation
      ↓
Evidence collection
      ↓
Provenance evaluation
      ↓
Candidate confirmation
      ↓
Resolved Intent

rather than merely model-based classification.

⸻

161. Provenance and Semantic Confidence

Confidence can be attached to inferred relationships, but provenance should identify whether confidence comes from:

model probability
rule evaluation
source authority
human confirmation

These are different epistemic mechanisms.

⸻

162. Provenance and Human Overrides

If a human overrides a system decision:

Trust:
REJECT
Human:
approve exception

the override should be explicitly represented as a new decision with its own provenance.

It should not rewrite the original decision.

⸻

163. Provenance and Exception Handling

An exception may require:

reason
principal
authorization
policy reference
time
scope

This creates a traceable exception path.

⸻

164. Provenance and Policy Exceptions

Policy exceptions should be distinguishable from normal policy evaluation.

Normal:
policy → REJECT
Exception:
authorized human override → EXECUTE

Both should remain in history.

⸻

165. Provenance and Audit Integrity

A mature Noema system should be able to demonstrate:

this decision
was based on
these Evidence records
which originated from
these sources
at these times
under these policies

That is stronger than ordinary application logging.

⸻

166. Provenance and Data Lineage Invariant

Every consequential decision should have a traceable lineage to the Evidence and Policy inputs that materially influenced it.

⸻

167. Provenance and Unknown Source

If Noema cannot establish where a consequential value came from, the provenance should reflect:

source = UNKNOWN

rather than inventing a source.

Depending on policy, this may block execution.

⸻

168. Provenance and Missing Provenance

Missing provenance is itself a data-quality condition.

For example:

Evidence:
beneficiary_verified = true
Provenance:
missing

A high-risk Action may require:

REJECT

or:

CLARIFY

rather than accepting the value.

⸻

169. Provenance and Trust State

Trust state can depend on provenance quality.

Conceptually:

Evidence available
      ↓
Provenance sufficient?
      │
   ┌──┴──┐
  YES    NO
   │      │
   ▼      ▼
Evaluate  Clarify /
Trust     Escalate

⸻

170. Provenance and Validation

Validation can verify:

source exists
resource exists
observation is within scope
timestamp is valid
version is supported
integrity is intact

This should occur before Evidence becomes trusted input to consequential decisions.

⸻

171. Provenance and Evidence Validation

An Evidence object may therefore contain:

claim
provenance
validation_status

rather than simply:

claim

⸻

172. Provenance and Source Validation

Noema should validate that the source itself is recognized for the relevant semantic purpose.

For example:

Payment status

may require:

Payment System

rather than:

CRM note

⸻

173. Provenance and Policy-Driven Validation

The acceptable provenance for a claim should be policy-driven.

Different Actions may require different source guarantees.

⸻

174. Provenance and Risk-Adaptive Validation

For low-risk Actions:

source = trusted cache

might be sufficient.

For high-risk Actions:

source = authoritative live system
freshness < threshold
integrity verified

may be required.

⸻

175. Provenance and Performance

Provenance should not require storing massive payloads or constructing expensive graphs for every low-value interaction.

Noema should use appropriate levels of provenance based on:

risk
consequence
audit requirements
retention
execution semantics

⸻

176. Provenance and Storage Efficiency

Large source payloads may be referenced by:

URI
object ID
content hash
external record ID

rather than copied into Noema.

⸻

177. Provenance and Content Hashes

A hash can establish that a referenced payload has not changed.

Conceptually:

payload_hash = H(payload)

This can strengthen audit integrity without storing the entire payload.

⸻

178. Provenance and Tamper Evidence

For highly sensitive deployments, provenance records may be chained:

Record A
  ↓ hash
Record B
  ↓ hash
Record C

creating tamper-evident history.

This is an implementation option, not a core semantic requirement.

⸻

179. Provenance and Immutable History

Historical provenance should be immutable where it contributes to auditability.

Corrections should generally create new records rather than silently rewriting history.

⸻

180. Provenance and Corrections

If an Evidence record was incorrect:

Evidence E1:
status = ACTIVE

and later corrected:

Evidence E2:
status = SUSPENDED

Noema should preserve E1 as the historical observation and record E2 as the correction.

⸻

181. Provenance and Historical Reconstruction

This allows Noema to answer both:

“What was actually observed at the time?”

and:

“What is known now?”

without conflating them.

⸻

182. Provenance and Current Re-evaluation

A historical Intent can be evaluated under current conditions for analysis, but the result is a new evaluation.

It must not overwrite historical provenance.

⸻

183. Provenance and Audit Queries

Useful queries include:

Which source supported this decision?
Which Evidence supported this Action?
When was this Evidence observed?
Which policy version was used?
Which system confirmed the Outcome?
Which human approved the exception?
Which external operation corresponds to this Execution?

The provenance model should make these queries possible.

⸻

184. Provenance and Debugging

When Noema behaves unexpectedly, engineers should be able to trace:

unexpected Action
    ↓
Trust decision
    ↓
Evidence
    ↓
source
    ↓
original observation

This dramatically reduces debugging ambiguity.

⸻

185. Provenance and Evaluation

Provenance can support offline evaluation of:

intent resolution
entity resolution
trust decisions
policy behavior
action selection
execution outcomes

without needing to re-query historical systems.

⸻

186. Provenance and Model Evaluation

Model predictions can be compared against authoritative outcomes.

Example:

Model:
payment/123
Authoritative:
payment/456

Provenance reveals both sources and allows error analysis.

⸻

187. Provenance and Learning

Historical provenance can support improving Noema’s models and policies.

However, learning systems must not retroactively alter the provenance of historical executions.

⸻

188. Provenance and Governance

Governance teams can use provenance to determine:

what data influenced automation
which systems supplied it
which policies governed it
who approved exceptions

This is particularly valuable in enterprise AI systems.

⸻

189. Provenance and Regulatory Audit

Where required, provenance can support regulatory questions such as:

What information was used?
Where did it come from?
When was it obtained?
What rule governed the decision?
Who approved the action?

The exact requirements depend on jurisdiction and industry.

⸻

190. Provenance and Accountability

The central accountability chain is:

SOURCE
  ↓
OBSERVATION
  ↓
EVIDENCE
  ↓
DECISION
  ↓
ACTION
  ↓
OUTCOME

Noema should preserve this chain for consequential execution.

⸻

191. Provenance and Noema’s System Boundary

Noema owns the provenance of its execution journey.

It does not claim ownership of the underlying enterprise facts.

Therefore:

Enterprise:
owns fact
Noema:
owns record of how that fact was used

This distinction should remain explicit.

⸻

192. Provenance and System of Record

The System of Record remains authoritative for enterprise state.

Noema’s provenance record establishes:

what Noema observed from that System of Record

not:

Noema became the System of Record.

⸻

193. Provenance and Execution Record

A useful Execution record may therefore contain:

Execution
 ├── intent_ref
 ├── action_ref
 ├── trust_decision_ref
 ├── evidence_refs
 ├── provenance_refs
 ├── attempt_refs
 └── outcome_ref

This keeps lineage explicit.

⸻

194. Provenance and Data Model

At the data-model level:

Claim
   │
   └── supported_by → Evidence
                         │
                         └── originated_from → Provenance
                                                   │
                                                   └── Source

This separates semantic claims from their origins.

⸻

195. Provenance and Evidence Model

Evidence should therefore not be modeled as merely:

key = value

but conceptually as:

Evidence {
    claim
    provenance
    observed_at
    scope
    validation
}

⸻

196. Provenance and Context Model

Context may contain references to Evidence rather than unmanaged copies.

Context
 ├── identity → Evidence
 ├── payment → Evidence
 └── policy → Evidence

This allows the Context to remain traceable.

⸻

197. Provenance and Trust Model

Trust evaluates Evidence according to:

authority
freshness
integrity
scope
policy
risk

Provenance provides the metadata required for these evaluations.

⸻

198. Provenance and Execution Model

Execution consumes decisions that were derived from provenance-backed Evidence.

This allows the execution record to answer:

“Why was this Action permitted?”

⸻

199. Provenance and Postconditions

Postcondition verification should produce new Evidence with new provenance.

Example:

Before:
payment.status = SUCCEEDED
Action:
refund_payment
After:
payment.status = REFUNDED

The second status is a new observation.

⸻

200. Provenance and Temporal Chains

A complete execution may therefore have:

10:00
Intent received
10:01
Payment observed
10:02
Trust evaluated
10:03
Refund submitted
10:05
Payment observed as refunded

Each observation has its own provenance.

⸻

201. Provenance and Eventual Consistency

Enterprise systems may be eventually consistent.

Therefore:

Action submitted

followed immediately by:

status = PENDING

does not necessarily contradict:

status = REFUNDED

five minutes later.

Provenance and observation time explain the transition.

⸻

202. Provenance and Source Freshness Policy

Trust policies may define:

Evidence freshness requirement

rather than treating all persisted data as equally current.

⸻

203. Provenance and Evidence Expiration

Evidence may become unusable without becoming historically invalid.

For example:

Evidence:
balance = $100,000
observed 10 minutes ago

may remain valid historical evidence but fail a:

maximum_age = 60 seconds

execution precondition.

⸻

204. Provenance and Semantic Expiration

Different facts have different natural lifetimes.

Employee name:
slow-changing
Account balance:
rapidly changing
Authentication:
short-lived
Policy:
version-bound

Provenance allows policies to evaluate these lifetimes explicitly.

⸻

205. Provenance and Source Availability

When the authoritative source is unavailable, Noema can determine whether existing Evidence remains acceptable based on its provenance and freshness.

⸻

206. Provenance and Graceful Degradation

Some low-risk operations may tolerate stale or secondary Evidence.

High-risk operations may not.

Therefore degradation behavior should be policy-driven.

⸻

207. Provenance and Trust Outcomes

Insufficient provenance may lead to:

CLARIFY

or:

ESCALATE

or:

REJECT

rather than:

EXECUTE

⸻

208. Provenance and Clarification Semantics

Clarification can specifically target missing provenance.

Example:

“Which account should I use?”

rather than:

“I don’t know.”

The goal is to acquire the missing Evidence necessary for deterministic execution.

⸻

209. Provenance and Enterprise Action Safety

The stronger the consequence, the stronger the provenance requirement should be.

This creates a direct relationship:

Consequence
    ↓
Evidence requirement
    ↓
Provenance requirement
    ↓
Trust threshold
    ↓
Execution permission

⸻

210. Core Invariants

Invariant 1

Every consequential decision must have traceable provenance to the Evidence that materially influenced it.

Invariant 2

Provenance identifies the origin of information; it does not transfer ownership of enterprise state to Noema.

Invariant 3

Model inference must remain distinguishable from authoritative enterprise observation.

Invariant 4

Human assertions must remain distinguishable from system-generated facts.

Invariant 5

Derived facts must retain references to the Evidence from which they were derived.

Invariant 6

Historical observations must preserve their observation time.

Invariant 7

Source time and Noema receipt time must remain distinguishable where temporal reasoning matters.

Invariant 8

Historical provenance must not be silently rewritten when source data changes.

Invariant 9

Historical decisions must retain the Policy and Action Contract versions relevant to those decisions.

Invariant 10

Contradictory Evidence must remain distinguishable rather than being silently collapsed.

Invariant 11

Unknown provenance must never be silently converted into trusted provenance.

Invariant 12

Missing provenance may be treated as insufficient Evidence for consequential execution.

Invariant 13

Source authority must be evaluated in context rather than assumed universally.

Invariant 14

Evidence freshness must be evaluated according to Action and Policy requirements.

Invariant 15

Persisted provenance must preserve sufficient lineage for recovery and audit.

Invariant 16

Provenance must respect tenant, organizational, security, and data boundaries.

Invariant 17

Provenance should minimize unnecessary duplication of source data.

Invariant 18

Sensitive provenance must remain subject to appropriate access control and retention policy.

Invariant 19

Outcome verification must identify the source that established the Outcome.

Invariant 20

An Action response must not automatically be treated as a verified Outcome.

Invariant 21

Historical Evidence may explain a historical decision but must not automatically substitute for current state during new execution.

Invariant 22

Recovery must distinguish historical Evidence from newly acquired Evidence.

Invariant 23

Reconciliation must preserve the provenance of both expected and observed states.

Invariant 24

Replay must preserve historical provenance and must not accidentally execute Actions.

Invariant 25

Provenance should support causal lineage from:

Source → Evidence → Decision → Action → Outcome

Invariant 26

Noema must be able to answer:

“What did we know, where did we get it, when did we get it, and how did it affect what we did?”

⸻

211. Final Definition

Provenance is the lineage of knowledge through Noema. It identifies where information originated, when it was observed, what scope and authority it carries, how it was transformed or derived, and how it contributed to decisions and execution. Provenance allows Noema to distinguish authoritative facts from inference, historical observations from current state, and evidence from assumption—making consequential automation traceable, auditable, and deterministic.

The canonical chain is:

                    SOURCE
                       │
                       ▼
                  OBSERVATION
                       │
                 provenance
                       │
                       ▼
                    EVIDENCE
                       │
                       ▼
                     CLAIM
                       │
                       ▼
               TRUST / POLICY
                       │
                       ▼
                    DECISION
                       │
                       ▼
                     ACTION
                       │
                       ▼
                   OUTCOME
                       │
                       ▼
                NEW EVIDENCE
                       │
                       └──────────► provenance

The key principle is:

Noema should never have to say only “we knew X.” It should be able to say “we knew X because this source told us X, at this time, within this scope, and that evidence contributed to this decision.”