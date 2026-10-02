> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Provenance

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/provenance.md

⸻

1. Definition

Provenance is the structured lineage of information through Noema.

It records where information originated, when it was observed and received, what scope and authority it carries, how it was validated or transformed, how its Fact Status was established, and how it contributed to an Intent, State Reconciliation result, Trust Decision, Action, Execution, or Outcome.

Provenance answers:

“Why does Noema have or use this information, where did it come from, and how did it contribute to what happened?”

Provenance is therefore a foundational property of Noema’s data model, State Reconciliation, Trust Engine, execution system, and causal audit model.

⸻

2. Purpose

Noema operates across multiple sources:

* Enterprise APIs
* Databases
* Events
* Documentation
* Policies
* Workflows
* Human input
* Configuration
* External systems
* Enterprise System-of-Record interfaces
* Noema internal execution state

These sources may disagree, change over time, become unavailable, or provide incomplete information.

A value without provenance is often insufficient for consequential execution.

For example:

status = APPROVED

is materially weaker than:

status = APPROVED
source = HR System
resource = employee/123
observed_at = 2026-08-27T09:31:02Z
scope = Nigeria Operations

Provenance makes the distinction explicit.

⸻

3. Core Principle

Noema should know not only what information it has, but:

* where it came from
* when it was observed
* when Noema received it
* what resource and scope it applies to
* what authority the source has for the relevant claim
* whether it was validated
* what Fact Status applies
* how it was transformed or derived
* how it contributed to a consequential decision

Provenance is therefore part of the semantic basis for trustworthy execution.

⸻

4. Provenance Is Not Data Ownership

Provenance records the origin and lineage of information.

It does not transfer ownership or authority over enterprise information to Noema.

For example:

Enterprise Ledger
    owns:
    account balance
Noema
    records:
    balance observed = $10,000
    source = Ledger
    observed_at = ...

The Ledger remains authoritative for the enterprise balance within its defined domain.

Noema owns the record of how that observation was used within Noema’s execution domain.

⸻

5. Provenance and Noema-Owned Canonical Data

Noema may have canonical data within its own execution domain.

Examples include:

* Intent versions
* Trust Decisions
* Execution state
* Execution attempts
* Noema Outcomes
* intervention state
* case state
* audit records
* provenance records

This does not make Noema the canonical owner of external enterprise business state.

Canonicality is therefore scoped.

Enterprise canonicality
    =
authoritative business state within an enterprise domain
Noema canonicality
    =
authoritative semantic/execution state within Noema's domain

⸻

6. Provenance and Canonical Data

Canonical Data must not be interpreted as universally authoritative.

A canonical value must be understood within the scope of:

* claim
* field
* resource
* organization
* tenant
* environment
* source authority
* effective time
* observation time
* policy

For enterprise business facts, the System of Record remains authoritative within its defined domain.

Provenance records that relationship.

⸻

7. Provenance and Trust

Trust decisions depend on Evidence.

Evidence without provenance is difficult to evaluate.

Conceptually:

Source
  ↓
Observation
  ↓
Validation / Admission
  ↓
Evidence
  ↓
State Reconciliation
  ↓
Fact Status
  ↓
Trust Evaluation
  ↓
Decision

Provenance establishes the relationships between these layers.

⸻

8. Provenance and Hard Admission

External information is not authoritative merely because Noema received or persisted it.

External payloads, events, tool responses, model outputs, and other untrusted inputs must pass through the appropriate validation and admission boundary before becoming eligible for authoritative semantic use.

Conceptually:

External Input
      ↓
Untrusted
      ↓
Schema Validation
      ↓
Semantic Validation / Classification
      ↓
Admitted Representation
      ↓
Evidence / Context / State Reconciliation

Persistence of an unvalidated value does not make that value trusted.

⸻

9. Provenance of Unvalidated Information

Noema may retain raw or unvalidated information when required for:

* diagnostics
* incident investigation
* forensic analysis
* debugging
* source reconciliation
* compliance
* controlled replay

However, such information must remain explicitly classified as unvalidated.

It must not silently become authoritative Evidence merely because it is persisted.

⸻

10. Provenance and Fact Status

Fact Status is distinct from provenance.

Provenance answers:

Where did this information come from?

Fact Status answers:

What is the current epistemic status of this claim within the relevant evaluation?

Canonical Fact Status values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

A claim may have excellent provenance and still be stale or conflicted.

A claim may also be unverified even when its source is known.

⸻

11. Provenance Is Not Evidence

Provenance identifies lineage.

Evidence supports a claim.

For example:

Evidence:
payment.status = SUCCEEDED
Provenance:
source = Payment System
resource = payment/123
operation = GET /payments/123
observed_at = ...

The provenance does not itself establish that the payment succeeded.

It establishes where and when the supporting observation originated.

⸻

12. Provenance Is Not Context

Context is information relevant to an Intent or execution.

Provenance is lineage attached to that information.

A Context Snapshot may reference Evidence and provenance without becoming authoritative enterprise state.

Context Snapshot
    ├── identity → Evidence → Provenance
    ├── payment → Evidence → Provenance
    └── policy → Evidence → Provenance

⸻

13. Provenance Is Not State

State represents a condition or semantic state within a defined domain.

Provenance explains the observations and information used to establish or evaluate that state.

For example:

State:
payment.status = REFUNDED
Provenance:
Payment System
observed_at = 10:45
operation = GET /payments/123

The provenance does not become the state itself.

⸻

14. Provenance Is Not Outcome

An Outcome represents what Noema establishes happened as a result of execution or verification.

Provenance supports the establishment of that Outcome.

Action response:
202 Accepted
Later observation:
payment.status = REFUNDED
Outcome:
REFUNDED
Provenance:
Payment System observation at 10:45

An Action response alone does not necessarily establish the Outcome.

⸻

15. Provenance and Determinism

Noema’s Trust Engine is deterministic.

Determinism requires the inputs to a decision to be identifiable and reproducible at the semantic level.

For example:

Trust Decision:
EXECUTE
Based on:
Evidence #42
Policy #17
Context Snapshot #81
Action Contract #9
Intent version #3

Without provenance, reconstructing the decision becomes difficult or impossible.

⸻

16. Provenance and the Model

Model output is untrusted interpretation.

The model may infer:

"The user probably means payment #123."

Noema must distinguish that inference from authoritative Evidence.

Conceptually:

Model inference
    ↓
candidate resource = payment/123
    ↓
Enterprise lookup
    ↓
Evidence
    ↓
State Reconciliation
    ↓
confirmed resource = payment/123

The candidate and confirmation have different provenance and epistemic status.

⸻

17. Provenance Categories

Noema may distinguish provenance by source type:

* User
* Enterprise System
* Enterprise System of Record
* Policy
* Configuration
* Documentation
* Event
* Human Operator
* Model
* Derived Computation
* Noema Internal State
* External System
* Test or Synthetic Source

Each source type carries different semantic properties.

No source category is universally authoritative.

⸻

18. Source Is Not Authority

Source identity and source authority are separate concepts.

source = CRM

does not mean:

CRM = authoritative for every claim

Authority must be evaluated for the specific claim, resource, scope, and decision.

⸻

19. Authority Is Claim-Specific

A source may be authoritative for one claim and non-authoritative for another.

For example:

Ledger
    authoritative for:
    account balance
Identity Provider
    authoritative for:
    identity status
CRM
    authoritative for:
    customer segmentation

Provenance should preserve the source identity and, where relevant, the semantic authority basis.

⸻

20. User-Originated Information

A user may provide:

"Refund my last payment."

The provenance is:

source_type = USER
source_id = interaction/request
observed_at = ...

The statement represents user-originated Intent information.

It does not automatically establish:

* payment identity
* payment state
* authorization
* ownership
* refund eligibility

Those require additional evidence and deterministic resolution.

⸻

21. Enterprise-Originated Information

An enterprise system may provide:

payment_id = 123
status = SUCCEEDED
amount = 500

Provenance should identify, where applicable:

* system
* resource
* operation
* observation time
* receipt time
* response identity
* source version
* scope
* environment

⸻

22. Policy-Originated Information

A policy may establish:

refunds above $10,000 require approval

Its provenance should identify:

* policy
* policy version
* effective period
* organization
* tenant
* environment
* scope

Policy provenance is essential for reconstructing historical Trust decisions.

⸻

23. Documentation-Originated Information

Documentation may describe:

POST /payments/{id}/refund

This can contribute to an Action Contract or Enterprise Action Graph.

However, documentation does not establish:

* current runtime availability
* current authorization
* current business state
* current policy
* successful execution

Runtime evidence and explicit enterprise configuration remain necessary.

⸻

24. Event-Originated Information

An event might state:

payment.refunded

Provenance should preserve, where available:

* event_id
* source_system
* event_type
* event_version
* emitted_at
* received_at
* sequence
* correlation identifiers

An event is evidence of an occurrence.

It is not automatically a complete representation of current enterprise state.

⸻

25. Human-Originated Information

A human operator may explicitly approve an Action.

For example:

Operator:
approved refund of payment/123

The provenance should identify:

* principal
* authorization context
* organization
* decision
* timestamp
* reason where required
* applicable policy or exception

Human intervention must not silently rewrite an earlier automated decision.

⸻

26. Model-Originated Information

Model output is a distinct provenance class.

Example:

MODEL
Inference:
payment candidate = payment/123
confidence = 0.91

This must not be represented as:

ENTERPRISE_SYSTEM
confirmed:
payment/123

The distinction is structural.

⸻

27. Model Confidence Is Not Fact Status

Model confidence is interpretation metadata.

It is not:

* Evidence
* Fact Status
* authorization
* source authority
* proof of correctness

For example:

model_confidence = 0.98
Fact Status = UNKNOWN

is valid.

Likewise:

model_confidence = 0.62
Fact Status = VERIFIED

may be valid when authoritative enterprise Evidence independently verifies the claim.

⸻

28. Derived Information

Noema may derive information from multiple sources.

Example:

Evidence A:
payment amount = $8,000
Evidence B:
refund policy threshold = $10,000
Derived:
approval not required

The derived conclusion must retain references to the inputs from which it was produced.

⸻

29. Derived Facts Are Not Independent Sources

A derived fact does not become independently authoritative merely because Noema calculated it.

Its provenance should preserve:

* source observations
* transformations
* rules
* policy
* versions
* evaluation time

This allows the derived result to be reevaluated when dependencies change.

⸻

30. Provenance Graph

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
   State Reconciliation
            │
            ▼
      Trust Evaluation
            │
            ▼
          Action

The graph allows Noema to trace a consequential decision backward to its supporting information.

⸻

31. Provenance as a Graph

A useful conceptual model is:

Source
  ↓
Observation
  ↓
Validation / Admission
  ↓
Evidence
  ↓
Claim
  ↓
State Reconciliation
  ↓
Fact Status
  ↓
Decision
  ↓
Action
  ↓
Outcome

Each edge answers:

“How did this information contribute to what happened?”

⸻

32. State Reconciliation and Provenance

State Reconciliation is a first-class Noema capability.

It compares observations and establishes the best supported current state within the relevant execution context.

Conceptually:

Observation
    ↓
Provenance
    ↓
State Reconciliation
    ↓
Fact / State

Reconciliation may produce:

* VERIFIED
* STALE
* CONFLICTED
* UNKNOWN

and other state-specific results as defined by the relevant contracts.

Provenance preserves the observations and sources used by reconciliation.

⸻

33. Provenance Does Not Perform Reconciliation

Provenance records lineage.

It does not itself determine which observation wins.

The reconciliation process must use deterministic rules, source authority, scope, temporal semantics, and applicable policy.

Provenance
    ↓
State Reconciliation
    ↓
Reconciled State / Fact Status

not:

Provenance
    ↓
automatic truth

⸻

34. Reconciliation of Conflicting Evidence

Multiple sources may produce conflicting information.

Example:

CRM:
customer.status = ACTIVE
Identity System:
customer.status = SUSPENDED

Provenance allows Noema to preserve both observations.

State Reconciliation and applicable policy determine whether the result is:

* VERIFIED
* CONFLICTED
* UNKNOWN
* another permitted state

The conflict must not be silently discarded.

⸻

35. Provenance Record

Conceptually:

Provenance {
    provenance_id
    source_type
    source_id
    source_system
    resource_ref
    operation_ref
    observed_at
    received_at
    effective_at
    version
    scope
    environment
    authority_basis
    integrity
}

The exact schema is implementation-dependent.

⸻

36. Source Identity

A source should be identifiable.

For example:

source_type = ENTERPRISE_SYSTEM
source_system = Payment System

is more useful than:

source = API

when multiple APIs exist.

⸻

37. Source Resource

Where applicable, provenance should identify the resource from which information originated.

resource_type = payment
resource_id = 123

This allows later verification and reconciliation.

⸻

38. Source Operation

The operation that produced the information may matter.

For example:

GET /payments/123

versus:

GET /payments/123/refund-status

Both may refer to the same resource while producing different evidence.

⸻

39. Observation Time

Every time-sensitive observation should have an observation timestamp.

observed_at = 10:32:15

This prevents historical observations from being mistaken for current facts.

⸻

40. Effective Time

Some information has a semantic effective time distinct from observation time.

For example:

Policy effective_at = Jan 1
observed_at = Jan 10

Both timestamps may matter.

⸻

41. Received Time

Noema may also record:

received_at = 10:32:18

This distinguishes:

when the source observed something

from:

when Noema received it

This distinction matters in distributed systems.

⸻

42. Event Time vs Processing Time

For events:

event_time

may differ from:

processing_time

Both may be relevant to provenance.

⸻

43. Version

Sources may evolve.

A provenance record may therefore include, where relevant:

* schema version
* API version
* event version
* policy version
* contract version
* integration mapping version
* source application version

Semantic versions should not be conflated with transport or schema versions.

⸻

44. Provenance and Temporal Validity

Information may have an effective period.

Example:

Policy v4
effective_from = Jan 1
effective_until = Jun 30

Noema must be able to determine whether the policy was applicable when a decision occurred.

⸻

45. Provenance and Freshness

Provenance enables freshness evaluation.

Example:

Evidence:
balance = $100,000
observed_at = 09:00

At:

10:30

the evidence may be too old for a high-risk transfer.

The value has not necessarily become false.

Its Fact Status or execution usability may have become:

STALE

or otherwise unsuitable under the applicable policy.

⸻

46. Provenance and Evidence Freshness

A Trust Policy may define:

Evidence:
balance
Maximum age:
60 seconds

Noema can evaluate:

current_time - observed_at

against the applicable policy.

Freshness requirements are claim- and action-specific.

⸻

47. Provenance and Canonical Data References

Persistence may store references to Canonical Data rather than duplicating enterprise state.

For example:

canonical_data_ref:
ledger/account/123

This reference does not mean that Noema owns the referenced enterprise state.

The reference preserves the relationship between Noema execution data and the enterprise authority.

⸻

48. Provenance and Context Snapshots

A Context Snapshot is a historical runtime view.

It may contain:

* Evidence references
* provenance references
* Intent version
* policy version
* Action Contract version
* graph/capability version
* reconciliation result

Persisting the snapshot does not make it current enterprise state.

⸻

49. Provenance and Historical Context

A historical Context Snapshot answers:

What information was available to Noema at that point?

It does not answer:

What is true in the enterprise now?

Current consequential decisions must obtain or reconcile current state as required.

⸻

50. Provenance and Intent Resolution

Intent resolution may produce:

user said:
"refund my last payment"
candidate resource:
payment/123

The resolution should be traceable.

For example:

Candidate:
payment/123
Supporting evidence:
latest completed payment
timestamp = ...
source = Payment System

This distinguishes candidate generation from confirmation.

⸻

51. Provenance and Ambiguity

Ambiguity may arise because evidence is insufficient or conflicting.

Example:

"Cancel the subscription."

Noema finds:

subscription A
subscription B

Both have plausible supporting Evidence.

The correct response is not to fabricate certainty.

Noema should enter deterministic clarification or another applicable Trust state.

⸻

52. Provenance and Clarification

A clarification can provide additional provenance.

Example:

Noema:
Which subscription do you mean?
User:
The business subscription.

The new user statement becomes additional input to Intent resolution.

It does not automatically establish all required enterprise facts.

⸻

53. Provenance and Confidence

Confidence should not replace provenance.

A model may have:

confidence = 0.98

but if the underlying Evidence is weak or ambiguous, clarification may still be required.

Conversely, authoritative enterprise Evidence may be decisive without any probabilistic confidence score.

⸻

54. Provenance and Trust Evidence

Trust evaluation should be able to answer:

Which Evidence supported this decision?

For example:

Trust Decision:
EXECUTE
Evidence:
E1 payment ownership confirmed
E2 payment status = SUCCEEDED
E3 user authorization confirmed
E4 amount below approval threshold

Each Evidence item should have provenance.

⸻

55. Provenance and Trust EXECUTE

A persisted:

Trust Decision = EXECUTE

means that the resolved path satisfied the applicable Trust conditions and was permitted to proceed.

It does not mean:

Action succeeded

or:

Enterprise state changed successfully

Those require Execution and Verification evidence.

⸻

56. Provenance and Policy Evaluation

A policy decision should identify:

* policy version
* policy scope
* inputs
* evaluation time
* applicable environment
* result
* relevant provenance

This makes policy evaluation auditable.

⸻

57. Provenance and Authorization

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

without being able to identify the basis.

Technical authorization, policy authorization, and business authorization remain distinct.

⸻

58. Provenance and Action Contracts

Action Contracts may originate from:

* API schemas
* OpenAPI documents
* SDKs
* documentation
* human configuration
* enterprise integration
* Enterprise Action Graph configuration

The Contract and its provenance should remain distinguishable.

A model-generated function is not itself an Action Contract.

⸻

59. Provenance and Integration Mapping

An integration mapping such as:

"completed" → SUCCEEDED

should identify where the mapping came from.

For example:

source = Payment API integration
version = 3

This makes semantic interpretation traceable.

⸻

60. Provenance and Enterprise Action Graph

The Enterprise Action Graph is a bounded representation of enterprise capabilities, actions, relationships, and execution-relevant semantics.

Its nodes and mappings may originate from:

* APIs
* schemas
* documentation
* policies
* configuration
* workflows
* events
* runtime observations

Provenance should preserve the origin of those definitions.

⸻

61. Provenance and Planner Bounds

A persisted plan must remain attributable to the bounded execution model.

The Planner may select or compose actions only within:

* Enterprise Action Graph
* Capability Registry
* Action Contract Registry
* Trust-approved execution constraints

Provenance must not be used to legitimize a model-generated capability that was never registered.

⸻

62. Provenance and Execution

An Execution should preserve references to the information that led to it.

Conceptually:

Execution
 ├── Intent
 ├── Context
 ├── State Reconciliation
 ├── Trust Decision
 ├── Action Contract
 ├── Evidence
 └── Provenance

Each component should be traceable through the relevant lineage.

⸻

63. Provenance and Outcome

Outcome observations require provenance.

Example:

Outcome:
refund succeeded
Source:
Payment System
Operation:
GET /payments/123
observed_at:
10:45

This distinguishes verified success from assumed success.

⸻

64. Provenance and Unknown Outcomes

If an Action times out:

Action:
refund_payment
Execution state:
UNKNOWN

the timeout itself has provenance:

source = network/client
observed_at = ...

It does not establish that the external Action failed.

⸻

65. Provenance and Reconciliation

Reconciliation compares observations from different points in time or different systems.

Example:

Execution:
UNKNOWN
Later observation:
Payment System → REFUNDED

Provenance establishes that the later observation came from the relevant source and when it was observed.

⸻

66. Provenance and Recovery

During recovery, Noema should know:

what it knew before failure

and:

what it knows now

Provenance provides the temporal distinction.

Recovery must not assume historical Evidence remains sufficient for current execution.

⸻

67. Provenance and Revalidation

Recovery may compare:

Historical Evidence

with:

Current Evidence

and determine whether the original Trust or execution conditions remain valid.

Historical provenance remains historical.

Current evaluation creates a new evaluation context.

⸻

68. Provenance and Persistence

Provenance is not necessarily the raw source data.

Persistence may store:

Evidence
+
Provenance metadata

while retaining only references to the original enterprise record.

This minimizes unnecessary duplication.

⸻

69. Provenance and Data Minimization

Noema generally does not need to store an entire source payload merely to establish:

source = Ledger
resource = account/123
observed_at = ...
claim = balance = $10,000

Full payloads should be retained only when required for:

* audit
* recovery
* reconciliation
* legal/compliance requirements
* debugging
* explicit enterprise requirements

⸻

70. Provenance and Integrity

Provenance is useful only if its integrity can be trusted.

Depending on requirements, Noema may use:

* hashes
* signatures
* immutable records
* source-issued identifiers
* checksums

to establish that Evidence or referenced source material has not been altered.

⸻

71. Source-Signed Evidence

Some enterprise systems may provide signed or otherwise verifiable responses.

Noema can preserve the relevant verification information.

This strengthens the Evidence model but does not eliminate the need for semantic authority and scope evaluation.

⸻

72. Provenance and Epistemic Strength

Evidence can have different epistemic characteristics.

Conceptually:

Authoritative verified observation
        ↓
Authoritative observation
        ↓
Verified derived fact
        ↓
Human assertion
        ↓
Model inference
        ↓
Unverified assumption

This is not a universal ranking.

Policy determines what Evidence is acceptable for a particular Action.

⸻

73. Provenance and Human Confirmation

A human confirmation may resolve an interpretation.

Example:

Model:
candidate = payment/123
User:
Yes, that payment.

The resulting Intent state has additional user-originated provenance.

Human confirmation does not automatically make unrelated enterprise facts true.

⸻

74. Provenance and Derived Facts

Derived facts should retain their dependency graph.

Example:

A:
payment.amount = $5,000
B:
policy.threshold = $10,000
Derived:
approval_required = false

If either A or B changes, the derived result may require reevaluation.

⸻

75. Provenance and Dependency Graphs

Conceptually:

Evidence A ──┐
             ├──> Derived Fact ──> Trust Decision
Evidence B ──┘

Dependencies should remain explicit for consequential decisions.

⸻

76. Provenance and Policy Changes

If a policy changes:

Policy v12:
approval required > $10k
Policy v13:
approval required > $5k

historical decisions must continue to reference v12 where v12 governed the decision.

A new evaluation under v13 is a new semantic event.

⸻

77. Provenance and Action Contract Changes

Likewise:

Action Contract v3

must remain distinguishable from:

Action Contract v4

for historical executions.

⸻

78. Provenance and Versioned Semantics

Provenance should distinguish:

* semantic contract version
* schema version
* transport version
* source version
* policy version
* integration mapping version
* observation time
* effective time

These are related but not interchangeable.

⸻

79. Provenance and Intent Versioning

Every consequential decision must reference the exact Intent version used.

Once an Intent is admitted to Trust, its semantic meaning is immutable.

A material change creates a new Intent version with:

version = n + 1
supersedes = previous_version

Clarification that changes the meaning of the request therefore creates a new Intent version.

Historical provenance must preserve the exact version used.

⸻

80. Provenance and State Reconciliation Versions

Where reconciliation logic or relevant semantic definitions are versioned, provenance should preserve the versions necessary to reconstruct the reconciliation context.

The historical result must not silently acquire a new meaning because reconciliation rules later change.

⸻

81. Provenance and Integration Versioning

Integration mappings may change over time.

Historical provenance must preserve the integration version that interpreted the source observation.

Current integrations may differ without rewriting historical lineage.

⸻

82. Provenance and Schema Evolution

Provenance records should remain interpretable as Noema evolves.

Important metadata may include:

provenance_schema_version
source_schema_version
semantic_version

Schema compatibility must not silently alter historical semantic meaning.

⸻

83. Provenance and Causality

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

without relying on regenerated model narratives.

⸻

84. Provenance and Auditability

Auditability requires more than timestamps.

A useful audit trail must establish:

* who
* what
* when
* where
* based on what
* under which policy
* using which Intent version
* using which Action Contract
* with what execution result
* with what verified Outcome

Provenance supplies much of the “based on what” component.

⸻

85. Provenance and Explainability

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

Explanation is therefore evidence-backed reconstruction, not an assertion generated solely by a model.

⸻

86. Provenance and Accountability

For consequential Actions, Noema should be able to demonstrate that its decision was based on identifiable information.

This is especially important for:

* financial Actions
* identity Actions
* access-control Actions
* employment Actions
* compliance Actions
* security Actions

⸻

87. Provenance and Enterprise Boundaries

Provenance must preserve organizational scope.

Example:

source:
HR System
organization:
Nigeria Operations

Information originating from one organizational boundary must not automatically be treated as applicable to another.

⸻

88. Provenance and Tenant Boundaries

Similarly:

Tenant A

and:

Tenant B

must have independent provenance contexts.

A source record from Tenant A cannot silently become Evidence for Tenant B.

⸻

89. Provenance and Data Boundaries

Provenance should identify relevant boundaries such as:

* tenant
* organization
* environment
* region
* system
* resource
* data classification

where these affect interpretation, authorization, or applicability.

⸻

90. Provenance and Source Reliability

Historical source behavior may inform operational decisions, but reliability must not be confused with authority.

For example:

source reliability = 99.9%

does not mean:

source is authoritative for every claim

Reliability and semantic authority are separate properties.

⸻

91. Provenance and Source Failure

If a source is unavailable:

Ledger unavailable

Noema should not infer:

balance = 0

unless an explicit policy defines that inference.

The absence of an authoritative observation must remain visible.

⸻

92. Provenance and Absence

Absence of Evidence is not automatically Evidence of absence.

For example:

No authorization record found.

is not automatically equivalent to:

User is unauthorized.

The applicable policy determines what the absence means.

⸻

93. Provenance and Negative Evidence

Negative Evidence should identify how it was established.

Example:

No active subscription found

could originate from:

Subscription System
query = ...
scope = ...
observed_at = ...

The query semantics and observation time matter.

⸻

94. Provenance and Query Semantics

A source response is meaningful only in the context of the query that produced it.

For example:

GET /payments?status=succeeded&limit=1

may support:

“This is the most recent succeeded payment.”

but not necessarily:

“This is the user’s only payment.”

Provenance should preserve enough query context to prevent overinterpretation.

⸻

95. Provenance and Source Scope

Evidence should carry scope where relevant.

Example:

balance:
$10,000
scope:
USD operating account

Without scope, the value may be ambiguous.

⸻

96. Provenance and Resource Identity

Resource identity should be explicit.

resource_type = account
resource_id = 123

rather than relying entirely on natural-language labels.

⸻

97. Provenance and Identity

Identity claims should preserve their source.

Example:

principal:
user/123
identity_provider:
Identity Provider
authentication_time:
...

This allows authorization decisions to reference an identifiable identity assertion.

⸻

98. Provenance and Authentication

Authentication evidence and authorization evidence are distinct.

Authentication:
Who are you?
Authorization:
What are you allowed to do?

Provenance should preserve both where relevant.

⸻

99. Provenance and Authorization Chains

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

100. Provenance and Configuration

Configuration can influence execution.

For example:

refund approval threshold = $10,000

The provenance should identify:

* configuration source
* version
* scope
* environment
* effective time

where that configuration affects Trust.

⸻

101. Provenance and Environment

Environment can matter.

production
staging
development

Evidence, Action Contracts, or configuration from staging must not silently support production execution.

⸻

102. Provenance and Integration Environment

For every external observation, Noema should be able to distinguish:

* production API
* sandbox API
* test fixture
* mock

when relevant.

⸻

103. Provenance and Synthetic Data

Test or synthetic Evidence must never be mistaken for production Evidence.

The provenance should explicitly identify:

source_type = TEST

or equivalent.

⸻

104. Provenance and Security

Provenance metadata can itself be sensitive.

For example:

* which system a company uses
* which administrator approved an Action
* which account was accessed
* which resources were queried

Therefore provenance must be subject to appropriate:

* authorization
* access control
* tenant isolation
* organizational boundaries
* retention policy
* data classification

⸻

105. Provenance and Redaction

When source information is sensitive, Noema may retain:

* source identifier
* claim
* timestamp
* integrity metadata
* reference
* scope

without exposing the complete underlying payload.

Redaction must not destroy the minimum lineage required for audit and recovery.

⸻

106. Provenance and Retention

Provenance retention should be aligned with the Evidence and decision it supports.

If a Trust Decision must remain auditable for seven years, the provenance required to explain it may also need to survive for seven years, subject to applicable requirements.

⸻

107. Provenance and Deletion

Deleting source data does not necessarily require deleting every historical provenance record.

Noema may retain a minimal historical record such as:

source
resource reference
claim
timestamp
integrity information

subject to enterprise, privacy, contractual, and legal requirements.

⸻

108. Provenance and Persistence

Provenance should be durable whenever it supports a consequential decision.

For example:

Transfer executed

should not lose:

why the beneficiary was considered valid

simply because a temporary cache expired.

⸻

109. Provenance and Recovery

Recovery may require determining:

What Evidence was used before the failure?

Persisted provenance provides that answer.

⸻

110. Provenance and Reconciliation

Reconciliation should preserve both sides:

Expected:
refund pending
Observed:
refund succeeded

with provenance for each observation.

⸻

111. Provenance and Outcome Verification

An Outcome should be considered verified only when supported by appropriate Evidence.

For example:

Action response:
202 Accepted

does not necessarily establish:

refund completed

A later authoritative observation may establish the Outcome.

⸻

112. Provenance and Asynchronous Execution

For asynchronous Actions:

Action submitted
      ↓
operation_id = 987
      ↓
event received
      ↓
operation completed

provenance should link the observations.

⸻

113. Provenance and External Operation Identity

External operation IDs are important provenance anchors.

Noema Execution:
exec_123
External Operation:
op_987

The relationship should be durable.

⸻

114. Provenance and Event Ordering

When multiple events arrive:

event A
event B
event C

provenance should preserve:

* event IDs
* event timestamps
* source sequence
* versions
* correlation IDs
* causal references

where available.

⸻

115. Provenance and Duplicate Events

Duplicate events should remain distinguishable from independent events when possible.

An event_id allows Noema to recognize:

same event received twice

rather than:

two independent events

⸻

116. Provenance and Event Authenticity

Where the source provides authenticity guarantees, Noema should preserve the relevant identifiers or verification results.

Authenticity does not automatically establish semantic authority for every claim.

⸻

117. Provenance and Model Traceability

Noema may retain model metadata relevant to a consequential inference:

* model
* model version
* inference identifier
* relevant prompt/context version
* timestamp

subject to privacy and retention requirements.

The purpose is traceability, not treating the model as an authoritative source.

⸻

118. Provenance and Intent Language

An Intent should be traceable back to the information from which it was constructed.

Conceptually:

Source of Intent
      ↓
Interpretation
      ↓
Candidate Intent
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolution

Each transformation may have provenance.

⸻

119. Provenance and Intent Composition

For compound Intent:

"Cancel the subscription and refund the last payment."

Noema may produce:

Intent
 ├── cancel_subscription
 └── refund_payment

Each component should preserve its relationship to the original Intent and supporting Evidence.

⸻

120. Provenance and Planning

A plan should identify why each Action is included.

Example:

Plan:
1. Verify payment
2. Refund payment
3. Cancel subscription

The plan may reference:

* Intent
* Trust Decision
* Action dependencies
* Context
* Enterprise Action Graph
* Action Contracts

The plan cannot create authority that Trust did not grant.

⸻

121. Provenance and Compensation

Compensation decisions should identify the Evidence that established the need for compensation.

Example:

Subscription creation succeeded
Payment capture failed

may lead to:

compensate subscription creation

The causal chain should remain traceable.

⸻

122. Provenance and Failure

Failure records should distinguish:

* source-reported failure
* Noema-observed failure
* timeout
* unknown outcome
* policy rejection
* authorization rejection
* validation failure
* reconciliation conflict

Each has different provenance.

⸻

123. Provenance and Human Intervention

When a human intervenes:

operator approved

the provenance should capture:

* principal
* authorization context
* decision
* time
* scope
* reason where required

The intervention becomes a new historical decision rather than a rewrite of the original decision.

⸻

124. Provenance and Audit Reconstruction

A mature Noema audit query should be able to traverse:

Outcome
 ← Execution
 ← Action
 ← Trust Decision
 ← Evidence
 ← State Reconciliation
 ← Provenance
 ← Source

This is the provenance chain.

⸻

125. Provenance and Explainability Boundary

Noema should explain decisions using persisted semantic facts and provenance.

It should not rely solely on regenerated model narratives.

A generated explanation may be useful as a presentation layer, but the underlying explanation must remain evidence-backed.

Noema does not need to expose private model chain-of-thought to establish causal accountability.

⸻

126. Provenance and Source Substitution

An enterprise may replace an integration.

Payment Provider A
        ↓
Payment Provider B

Historical provenance must still identify Provider A for historical observations.

Current executions may use Provider B.

⸻

127. Provenance and Integration Evolution

This allows Noema to preserve:

historical semantic lineage

while supporting:

current integration architecture

without rewriting history.

⸻

128. Provenance and Data Lineage

Provenance is the foundation of Noema’s data lineage.

Source
 ↓
Observation
 ↓
Validation
 ↓
Evidence
 ↓
State Reconciliation
 ↓
Fact Status
 ↓
Decision
 ↓
Action
 ↓
Outcome

Lineage makes the flow of information through the system explicit.

⸻

129. Provenance and Semantic Lineage

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
State Reconciliation
   ↓
policy input

This is semantic provenance.

⸻

130. Provenance and Normalization

Different systems may express the same concept differently.

Payment API:
"completed"
Noema:
SUCCEEDED

Provenance should preserve the source representation and the normalization that produced the Noema interpretation where necessary.

⸻

131. Provenance and Transformation

A transformed value should retain its source relationship.

Example:

$10,000

becomes:

10000 USD

The transformation should not destroy provenance.

⸻

132. Provenance and Aggregation

Aggregated values may depend on multiple sources.

Example:

total outstanding = $15,000

may derive from:

Invoice A = $5,000
Invoice B = $10,000

The resulting value should preserve its dependencies where it affects execution.

⸻

133. Provenance and Derived Authorization

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

134. Provenance and Source Freshness

Different sources may have different freshness characteristics:

* real-time API
* event stream
* hourly batch
* daily report

Provenance allows Trust policies to account for those differences.

⸻

135. Provenance and Reliability

Reliability metadata may be useful operationally:

* source availability
* latency
* error rate

but it must not replace semantic authority.

A highly reliable source can still be the wrong source for a particular claim.

⸻

136. Provenance and Trust Policy

Trust policies may evaluate provenance attributes such as:

* source authority
* freshness
* integrity
* scope
* identity
* version
* environment
* Fact Status

This makes Evidence quality explicit.

⸻

137. Provenance and Risk

Higher-risk Actions generally require stronger provenance.

For example:

Low risk:
read employee name
High risk:
terminate employee access

The latter may require authoritative:

* identity
* authorization
* policy
* resource
* current-state Evidence

⸻

138. Provenance and Risk-Adaptive Evidence

Conceptually:

Risk
 ↓
Required Evidence
 ↓
Required Provenance
 ↓
Trust threshold

The more consequential the Action, the stronger the Evidence lineage requirements may become.

⸻

139. Provenance and Enterprise Policy

Enterprises may define which sources are acceptable for particular decisions.

Example:

Beneficiary verification:
must originate from Identity System

Noema should not substitute an arbitrary source merely because it contains a plausible value.

⸻

140. Provenance and Source Allowlisting

For sensitive Actions, policies may explicitly specify:

* allowed source types
* required source systems
* minimum freshness
* required integrity
* required scope
* required environment

This creates deterministic Evidence requirements.

⸻

141. Provenance and Evidence Sufficiency

A Trust Engine should be able to determine:

Evidence sufficient

versus:

Evidence insufficient

Provenance supplies information needed for this evaluation.

⸻

142. Provenance and Evidence Conflict

When Evidence conflicts:

Source A says:
ACTIVE
Source B says:
SUSPENDED

Noema should not hide the conflict.

It should retain both provenance chains and allow deterministic policy and reconciliation to determine the appropriate state or Trust outcome.

⸻

143. Provenance and Uncertainty

Uncertainty should be represented explicitly.

Examples:

* unknown source
* stale observation
* conflicting evidence
* unverified inference
* incomplete scope
* unavailable source

These are preferable to silently converting uncertainty into certainty.

⸻

144. Provenance and Negative Assertions

A statement such as:

"No matching account exists."

requires provenance showing:

* what system was queried
* what query was made
* when it was made
* what scope was searched
* what response was received

Otherwise the assertion is difficult to validate.

⸻

145. Provenance and Query Reproducibility

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

146. Provenance and API Responses

Noema need not retain every API response.

It should retain sufficient metadata to establish:

* which response
* from which system
* at what time
* for which resource
* under which operation
* supported which claim
* with what version

⸻

147. Provenance and Database Queries

If Noema obtains Evidence from a database or query service, provenance should identify the relevant logical source and query context rather than exposing unnecessary raw data.

⸻

148. Provenance and Documentation

Documentation-derived information should have an explicit epistemic classification.

For example:

Documentation says:
endpoint accepts DELETE

does not establish:

endpoint currently permits this caller

Runtime Evidence is required for the latter.

⸻

149. Provenance and Configuration Drift

If configuration changes:

approval threshold:
$10,000 → $5,000

provenance allows Noema to determine which configuration applied to a historical decision.

⸻

150. Provenance and System Drift

External systems evolve.

An API may change:

status:
completed → settled

Provenance and integration versions allow Noema to identify how the old and new representations were interpreted.

⸻

151. Provenance and Reproducibility

A consequential decision should ideally be reproducible at the semantic level.

That means Noema should be able to reconstruct:

* Intent version
* Context Snapshot
* observations
* State Reconciliation inputs and result
* Fact Status
* Evidence
* Policy
* Action Contract
* Trust inputs
* decision

from persisted lineage.

⸻

152. Provenance and Replay

Replay uses provenance to reconstruct the historical semantic environment.

Replay must be non-executing by default.

Historical replay must not:

* mutate historical meaning
* silently adopt current policy
* silently adopt current Intent meaning
* dispatch consequential Actions

unless a separate, explicitly authorized execution path is invoked.

⸻

153. Provenance and Historical Truth

The objective is not to reconstruct what would be true today.

It is to reconstruct:

What Noema knew, from which sources, under which semantic versions, at the time the decision was made.

That distinction is essential.

⸻

154. Provenance and Current Truth

Current truth must be obtained from current authoritative sources and, where necessary, State Reconciliation.

Historical provenance cannot substitute for current state when making a new consequential decision.

⸻

155. Provenance and Decision Revalidation

A historical decision may therefore be represented as:

Historical:
EXECUTE
Current:
requires revalidation

This avoids treating historical Evidence as permanently authoritative.

⸻

156. Provenance and Temporal Reasoning

Noema should distinguish at least:

* event occurred at
* source observed at
* source effective at
* Noema received at
* decision made at
* Action executed at
* Outcome observed at

These timestamps can differ.

⸻

157. Provenance and Clock Skew

Distributed systems may have clock differences.

Therefore timestamps should not automatically be treated as perfect causal ordering.

Where available, Noema should preserve:

* sequence numbers
* event IDs
* causal references
* source ordering information

alongside timestamps.

⸻

158. Provenance and Causal Ordering

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

159. Provenance and Source Identity Changes

If a source system is renamed, migrated, or replaced, historical provenance must retain the identity applicable at the time.

⸻

160. Provenance and Integration Ownership

Noema should know:

which integration produced the observation

but integration ownership does not imply business-state ownership.

⸻

161. Provenance and External References

Stable external identifiers improve traceability:

* transaction_id
* event_id
* operation_id
* request_id
* resource_id
* case_id

These should be preserved where useful.

⸻

162. Provenance and Correlation

A correlation ID may connect:

user request
    ↓
Noema Intent
    ↓
Noema Execution
    ↓
external request
    ↓
external event
    ↓
Outcome

This creates end-to-end lineage.

⸻

163. Provenance and Audit Queries

An auditor should be able to ask:

“Why was this Action executed?”

and navigate:

Execution
 → Trust Decision
 → Policy
 → Evidence
 → State Reconciliation
 → Provenance
 → Source

without relying solely on runtime logs.

⸻

164. Provenance and Accountability Boundary

The provenance chain establishes what Noema did with information.

It does not establish that the source information itself was universally correct.

Noema can prove:

“We received X from System Y.”

That is different from:

“System Y was objectively correct.”

⸻

165. Provenance and Source Trust

Source trust may itself be governed by enterprise policy.

For example:

Payment status:
must come from Payment System
Identity:
must come from Identity Provider

The provenance model makes these constraints enforceable.

⸻

166. Provenance and Evidence Hierarchy

A practical conceptual hierarchy is:

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

Policy determines acceptable Evidence for each Action.

⸻

167. Provenance and Noema’s Trust Boundary

The Trust Engine should not ask only:

“What value do we have?”

It should ask:

“What value do we have, where did it come from, when was it observed, what scope does it apply to, what is its Fact Status, and is that source acceptable for this decision?”

That is provenance-aware Trust evaluation.

⸻

168. Provenance and Action Selection

Action selection may depend on provenance.

For example:

beneficiary verified by authoritative system

may permit:

TRANSFER

while:

beneficiary inferred from user text

may only permit:

CLARIFY

The Planner does not independently establish authority.

⸻

169. Provenance and Execution Permission

Provenance can therefore become part of execution preconditions.

Example:

Precondition:
beneficiary_identity
Required source:
Identity System
Freshness:
< 5 minutes
Fact Status:
VERIFIED

If the condition is not satisfied, the Action must not execute.

⸻

170. Provenance and Preconditions

A Precondition can reference provenance attributes.

Example:

Precondition:
payment.status = SUCCEEDED
Required source:
Payment System
Maximum age:
60 seconds
Fact Status:
VERIFIED

This creates a deterministic execution gate.

⸻

171. Provenance and Postconditions

Postconditions also require provenance.

Example:

Postcondition:
payment.status = REFUNDED

should be verified through an acceptable source.

A successful API response alone may not satisfy the postcondition.

⸻

172. Provenance and Outcome Verification

The distinction is:

Action response

versus:

Verified Outcome

Provenance establishes the Evidence behind the latter.

⸻

173. Provenance and Failure Recovery

If an external operation is uncertain:

timeout

Noema can use provenance to query the authoritative source and establish:

succeeded
failed
still pending
unknown

The new observation receives new provenance.

⸻

174. Provenance and Reconciliation Loop

Conceptually:

UNKNOWN
   ↓
Query authoritative source
   ↓
Observation
   ↓
Validation
   ↓
Evidence
   ↓
Provenance
   ↓
State Reconciliation
   ↓
Fact Status / Resolved State

Historical provenance is retained alongside the new observation.

⸻

175. Provenance and Enterprise Action Graph

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

This allows Noema to understand not only what an enterprise system can do, but what information it provides and under what semantic conditions that information may be used.

⸻

176. Provenance and Action Graph Construction

Action Graph nodes may originate from:

* API schemas
* documentation
* events
* configuration
* policies
* workflows
* runtime observations

Each source should remain identifiable.

⸻

177. Provenance and Canonicalization

When multiple sources describe the same concept:

CRM customer
Identity customer
Billing customer

Noema may construct a canonical relationship.

The provenance of that relationship must remain visible.

Canonicalization must not erase source identity.

⸻

178. Provenance and Entity Resolution

Entity resolution is particularly provenance-sensitive.

Example:

"John"

could match:

customer/123
customer/456

The Evidence supporting the selected entity must be explicit.

If insufficient:

CLARIFY

or another applicable Trust outcome must result.

⸻

179. Provenance and Intent Resolution

Intent Resolution therefore becomes:

Candidate generation
      ↓
Evidence collection
      ↓
Provenance evaluation
      ↓
State Reconciliation
      ↓
Candidate confirmation
      ↓
Resolved Intent

rather than merely model-based classification.

⸻

180. Provenance and Semantic Confidence

Confidence can be attached to inferred relationships, but provenance should identify whether confidence comes from:

* model probability
* rule evaluation
* source authority
* human confirmation

These are different epistemic mechanisms.

⸻

181. Provenance and Human Overrides

If a human overrides a system decision:

Trust:
REJECT
Human:
approve exception

the override should be represented as a new decision with its own provenance.

It must not rewrite the original decision.

⸻

182. Provenance and Exception Handling

An exception may require:

* reason
* principal
* authorization
* policy reference
* time
* scope
* affected Intent/Execution

This creates a traceable exception path.

⸻

183. Provenance and Policy Exceptions

Policy exceptions should be distinguishable from normal policy evaluation.

Normal:
policy → REJECT
Exception:
authorized human override → permitted execution

Both remain in history.

⸻

184. Provenance and Audit Integrity

A mature Noema system should be able to demonstrate:

this decision
was based on
these Evidence records
which originated from
these sources
at these times
under these policies
and these semantic versions

That is stronger than ordinary application logging.

⸻

185. Provenance and Data Lineage Invariant

Every consequential decision should have traceable lineage to the Evidence, policy, Intent version, and Action Contract inputs that materially influenced it.

⸻

186. Provenance and Unknown Source

If Noema cannot establish where a consequential value came from:

source = UNKNOWN

must be represented explicitly.

Noema must not invent provenance.

Depending on policy, unknown provenance may block execution.

⸻

187. Provenance and Missing Provenance

Missing provenance is itself a data-quality condition.

For example:

Evidence:
beneficiary_verified = true
Provenance:
missing

A high-risk Action may require:

CLARIFY
ESCALATE
REJECT

rather than accepting the value.

⸻

188. Provenance and Trust State

Trust state can depend on provenance sufficiency.

Conceptually:

Evidence available
      ↓
Provenance sufficient?
      │
   ┌──┴──┐
  YES    NO
   │      │
   ▼      ▼
Evaluate  CLARIFY /
Trust     ESCALATE /
          REJECT

The applicable policy determines the outcome.

⸻

189. Provenance and Validation

Validation can verify:

* source exists
* source is recognized
* resource exists
* observation is within scope
* timestamp is valid
* version is supported
* integrity is intact
* environment is correct

This should occur before Evidence becomes trusted input to consequential decisions.

⸻

190. Provenance and Evidence Validation

An Evidence object may therefore contain:

Evidence {
    claim
    provenance
    fact_status
    validation
}

rather than merely:

claim

⸻

191. Provenance and Source Validation

Noema should validate that the source is recognized for the relevant semantic purpose.

For example:

Payment status

may require:

Payment System

rather than:

CRM note

⸻

192. Provenance and Policy-Driven Validation

The acceptable provenance for a claim should be policy-driven.

Different Actions may require different source guarantees.

⸻

193. Provenance and Risk-Adaptive Validation

For low-risk Actions:

source = trusted cache

might be sufficient.

For high-risk Actions:

source = authoritative live system
freshness < threshold
integrity verified
Fact Status = VERIFIED

may be required.

⸻

194. Provenance and Performance

Provenance should not require storing massive payloads or constructing expensive graphs for every low-value interaction.

Noema should use appropriate levels of provenance based on:

* risk
* consequence
* audit requirements
* retention
* execution semantics
* data sensitivity

⸻

195. Provenance and Storage Efficiency

Large source payloads may be referenced by:

* URI
* object ID
* content hash
* external record ID
* event ID
* operation ID

rather than copied into Noema.

⸻

196. Provenance and Content Hashes

A hash can establish that a referenced payload has not changed.

Conceptually:

payload_hash = H(payload)

This can strengthen audit integrity without storing the entire payload.

⸻

197. Provenance and Tamper Evidence

For highly sensitive deployments, provenance records may be chained:

Record A
  ↓ hash
Record B
  ↓ hash
Record C

creating tamper-evident history.

This is an implementation option, not a core semantic requirement.

⸻

198. Provenance and Immutable History

Historical provenance should be immutable where it contributes to auditability.

Corrections should generally create new records rather than silently rewriting history.

⸻

199. Provenance and Corrections

If an Evidence record was incorrect:

Evidence E1:
status = ACTIVE

and later corrected:

Evidence E2:
status = SUSPENDED

Noema should preserve E1 as the historical observation and record E2 as the later observation or correction.

Historical lineage must remain intact.

⸻

200. Provenance and Historical Reconstruction

This allows Noema to answer both:

“What was observed at the time?”

and:

“What is known now?”

without conflating them.

⸻

201. Provenance and Current Re-evaluation

A historical Intent can be evaluated under current conditions for analysis, but the result is a new evaluation.

It must not overwrite historical provenance or historical Trust Decisions.

⸻

202. Provenance and Audit Queries

Useful queries include:

* Which source supported this decision?
* Which Evidence supported this Action?
* What was the Fact Status at decision time?
* When was this Evidence observed?
* Which policy version was used?
* Which Intent version was used?
* Which Action Contract version was used?
* Which system confirmed the Outcome?
* Which human approved the exception?
* Which external operation corresponds to this Execution?
* Which reconciliation established the current state?

The provenance model should make these queries possible.

⸻

203. Provenance and Debugging

When Noema behaves unexpectedly, engineers should be able to trace:

unexpected Action
    ↓
Trust Decision
    ↓
resolved Intent
    ↓
Evidence
    ↓
State Reconciliation
    ↓
source
    ↓
original observation

This reduces debugging ambiguity.

⸻

204. Provenance and Evaluation

Provenance can support offline evaluation of:

* Intent resolution
* entity resolution
* State Reconciliation
* Trust decisions
* policy behavior
* Action selection
* execution outcomes

without requiring historical enterprise systems to be queried again.

⸻

205. Provenance and Model Evaluation

Model predictions can be compared against authoritative outcomes.

Example:

Model:
payment/123
Authoritative:
payment/456

Provenance reveals both sources and allows error analysis.

⸻

206. Provenance and Learning

Historical provenance can support improving Noema’s models and policies.

However, learning systems must not retroactively alter the provenance or semantic meaning of historical executions.

⸻

207. Provenance and Governance

Governance teams can use provenance to determine:

* what data influenced automation
* which systems supplied it
* which policies governed it
* which Intent version was used
* which human approved exceptions
* what was verified after execution

This is particularly valuable in enterprise AI systems.

⸻

208. Provenance and Regulatory Audit

Where required, provenance can support questions such as:

* What information was used?
* Where did it come from?
* When was it obtained?
* What rule governed the decision?
* Which version of the request was acted upon?
* Who approved the Action?
* What evidence established the Outcome?

Exact requirements depend on jurisdiction and industry.

⸻

209. Provenance and Accountability

The central accountability chain is:

SOURCE
  ↓
OBSERVATION
  ↓
VALIDATION
  ↓
EVIDENCE
  ↓
RECONCILIATION
  ↓
FACT STATUS
  ↓
DECISION
  ↓
ACTION
  ↓
OUTCOME

Noema should preserve this chain for consequential execution.

⸻

210. Provenance and Noema’s System Boundary

Noema owns the provenance of its execution journey.

It does not claim ownership of the underlying enterprise facts.

Therefore:

Enterprise:
owns authoritative business fact
Noema:
owns the record of how the fact was observed,
validated, reconciled, and used

This distinction must remain explicit.

⸻

211. Provenance and System of Record

The System of Record remains authoritative for enterprise state within its defined domain.

Noema’s provenance record establishes:

what Noema observed from that System of Record

not:

Noema became the System of Record

⸻

212. Provenance and No Shadow Canonical State

Noema must not create shadow canonical enterprise state merely because it persists observations.

For example:

Persisted:
account.balance = $10,000

does not mean:

Noema owns account.balance

The persisted value remains an observation or execution-domain representation unless Noema is explicitly authoritative for that particular semantic domain.

⸻

213. Provenance and Execution Record

A useful Execution record may contain:

Execution
 ├── intent_ref
 ├── action_ref
 ├── trust_decision_ref
 ├── evidence_refs
 ├── reconciliation_refs
 ├── provenance_refs
 ├── attempt_refs
 └── outcome_ref

This keeps lineage explicit.

⸻

214. Provenance and Data Model

At the data-model level:

Claim
   │
   └── supported_by → Evidence
                         │
                         ├── has_fact_status → Fact Status
                         │
                         └── originated_from → Provenance
                                                   │
                                                   └── Source

This separates semantic claims from their origins.

⸻

215. Provenance and Evidence Model

Evidence should therefore not be modeled as merely:

key = value

but conceptually as:

Evidence {
    claim
    provenance
    fact_status
    observed_at
    scope
    validation
}

⸻

216. Provenance and Context Model

Context may contain references to Evidence rather than unmanaged copies.

Context
 ├── identity → Evidence
 ├── payment → Evidence
 └── policy → Evidence

This allows Context to remain traceable.

⸻

217. Provenance and Trust Model

Trust evaluates Evidence according to:

* authority
* freshness
* integrity
* scope
* Fact Status
* policy
* risk
* authorization requirements

Provenance provides the metadata required for these evaluations.

⸻

218. Provenance and Execution Model

Execution consumes decisions derived from provenance-backed Evidence.

This allows the execution record to answer:

“Why was this Action permitted?”

The answer must ultimately resolve to deterministic Trust conditions and their supporting lineage.

⸻

219. Provenance and Postconditions

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

220. Provenance and Temporal Chains

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

221. Provenance and Eventual Consistency

Enterprise systems may be eventually consistent.

Therefore:

Action submitted

followed immediately by:

status = PENDING

does not necessarily contradict:

status = REFUNDED

five minutes later.

Provenance and observation time explain the temporal transition.

⸻

222. Provenance and Source Freshness Policy

Trust policies may define:

Evidence freshness requirement

rather than treating all persisted data as equally current.

⸻

223. Provenance and Evidence Expiration

Evidence may become unusable without becoming historically invalid.

For example:

Evidence:
balance = $100,000
observed 10 minutes ago

may remain valid historical Evidence but fail:

maximum_age = 60 seconds

as an execution precondition.

⸻

224. Provenance and Semantic Expiration

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

225. Provenance and Source Availability

When the authoritative source is unavailable, Noema can determine whether existing Evidence remains acceptable based on:

* provenance
* Fact Status
* freshness
* scope
* risk
* policy

Availability alone must not become an implicit authorization to use stale information.

⸻

226. Provenance and Graceful Degradation

Some low-risk operations may tolerate stale or secondary Evidence.

High-risk operations may not.

Degradation behavior should therefore be policy-driven.

⸻

227. Provenance and Trust Outcomes

Insufficient provenance may lead to:

CLARIFY

or:

ESCALATE

or:

REJECT

rather than:

EXECUTE

Trust outcomes remain exactly:

EXECUTE
CLARIFY
ESCALATE
REJECT

⸻

228. Provenance and Clarification Semantics

Clarification can specifically target missing provenance or missing supporting Evidence.

Example:

“Which account should I use?”

The objective is to acquire the information necessary for deterministic resolution, not to ask for arbitrary additional information.

⸻

229. Provenance and Enterprise Action Safety

The stronger the consequence, the stronger the provenance requirements may need to be.

The relationship is:

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

230. Provenance and Operational Memory

Operational Memory may retain structured execution and case history derived from provenance.

It may support:

* recovery
* recurring failure analysis
* operational investigation
* case reconstruction
* evaluation
* improvement

Operational Memory is not generic AI memory and is not enterprise business-state authority.

⸻

231. Provenance and Read-Only Operations

Read-only does not mean semantically inconsequential.

An operation that only retrieves protected information may still require:

* authorization
* Trust evaluation
* provenance
* auditability

Provenance must therefore support consequential read paths as well as writes.

⸻

232. Provenance and Security Boundary

The following are untrusted by default:

* user input
* model output
* retrieved text
* external tool responses
* external payloads
* unvalidated events

Noema must not allow persistence or provenance metadata to confer authority on these inputs.

The model has no direct enterprise credentials or unrestricted enterprise access.

⸻

233. Provenance and Secrets

Secrets should not be embedded in provenance records.

Credentials, tokens, private keys, and other secret material must remain in the appropriate secret-management boundary.

Provenance may identify the credential or integration context without storing the secret itself.

⸻

234. Provenance and Causal Audit

A consequential audit chain should be able to traverse:

Intent version
    ↓
Interpretation / resolution
    ↓
Observation
    ↓
Validation / admission
    ↓
State Reconciliation
    ↓
Fact Status
    ↓
Evidence
    ↓
Trust Decision
    ↓
Action Contract
    ↓
Execution Attempt
    ↓
Verification
    ↓
Outcome

This is causal auditability.

⸻

235. Provenance and Persistence Failure

If provenance required for a consequential Action cannot be durably recorded, Noema should normally block or escalate the Action when the missing persistence would make the execution unauditable or unrecoverable.

If persistence fails after dispatch, the execution must be treated as potentially uncertain and reconciled against the relevant enterprise source.

⸻

236. Provenance and Exactly-Once Logical Effects

Provenance does not create exactly-once delivery.

Noema should not claim message-level exactly-once semantics merely because provenance is persisted.

The goal is safe logical effects through:

* durable execution identity
* idempotency
* provenance
* reconciliation
* verification

where supported by the enterprise system.

⸻

237. Provenance and Unknown

Unknown is first-class.

Unknown may apply to:

* source
* fact
* state
* target
* execution
* outcome
* reconciliation

For example:

Execution:
UNKNOWN
Provenance:
timeout observed at 10:04
Enterprise state:
not yet reconciled

Noema must not convert the timeout into FAILED without evidence establishing failure.

⸻

238. Provenance and Historical Semantics

Historical provenance must preserve the semantic versions relevant to the decision:

* Intent version
* Trust Contract version
* Action Contract version
* Execution Contract version
* Policy version
* relevant Context Contract version
* Event Contract version where applicable
* integration mapping version
* graph/capability version where applicable

This prevents future changes from silently rewriting historical meaning.

⸻

239. Provenance and Versioned Meaning

Versioning must preserve:

what a piece of information meant at the time it was used.

A source may change.

A policy may change.

An Action Contract may change.

An integration mapping may change.

None of these changes should silently alter historical provenance.

⸻

240. Core Invariants

Invariant 1

Every consequential decision must have traceable provenance to the Evidence and policy inputs that materially influenced it.

Invariant 2

Provenance identifies the origin and lineage of information; it does not transfer ownership of enterprise state to Noema.

Invariant 3

Enterprise Systems of Record remain authoritative for enterprise business state within their defined domains.

Invariant 4

Noema may be canonical for its own execution-domain state without becoming canonical for enterprise business state.

Invariant 5

Unvalidated external information must not become authoritative merely because it is persisted.

Invariant 6

Hard schema validation and admission must precede authoritative semantic use of external inputs.

Invariant 7

Raw or unvalidated payloads retained for diagnostics must remain explicitly classified as unvalidated.

Invariant 8

Evidence must remain distinguishable from its provenance.

Invariant 9

Fact Status must remain distinct from Evidence and Provenance.

Invariant 10

Canonical Data must remain scoped to its claim, authority, resource, organization, tenant, environment, or other applicable semantic boundary.

Invariant 11

Source identity must remain distinct from source authority.

Invariant 12

Source authority must be evaluated for the relevant claim rather than assumed universally.

Invariant 13

Model inference must remain distinguishable from authoritative enterprise observation.

Invariant 14

Model confidence must never be treated as Evidence, Fact Status, authority, or authorization.

Invariant 15

Human assertions must remain distinguishable from enterprise-system observations.

Invariant 16

Derived facts must retain references to the Evidence from which they were derived.

Invariant 17

Contradictory Evidence must remain distinguishable rather than being silently collapsed.

Invariant 18

Unknown provenance must never be silently converted into trusted provenance.

Invariant 19

Missing provenance may be treated as insufficient Evidence for consequential execution.

Invariant 20

Historical observations must preserve their observation time.

Invariant 21

Source observation time, effective time, and Noema receipt time must remain distinguishable where temporal reasoning matters.

Invariant 22

Historical provenance must not be silently rewritten when source data changes.

Invariant 23

Historical decisions must retain the exact Intent version used.

Invariant 24

Historical decisions must retain the relevant Policy and Action Contract versions.

Invariant 25

Historical decisions should retain the relevant Trust, Context, Event, Execution, integration, graph, and capability versions where necessary for reconstruction.

Invariant 26

Context Snapshots must remain distinguishable from current enterprise state.

Invariant 27

State Reconciliation must remain distinct from provenance.

Invariant 28

State Reconciliation must preserve the observations and provenance used to establish or evaluate reconciled state.

Invariant 29

Fact Status must remain explicit where it materially affects Trust or execution.

Invariant 30

Historical Evidence may explain a historical decision but must not automatically substitute for current state during new consequential execution.

Invariant 31

Recovery must distinguish historical Evidence from newly acquired Evidence.

Invariant 32

Recovery of uncertain execution must use current enterprise Evidence and State Reconciliation before retrying or continuing where required.

Invariant 33

A persisted Trust decision of EXECUTE must not be interpreted as proof of Action success.

Invariant 34

An Action response must not automatically be treated as a verified Outcome.

Invariant 35

Outcome verification must identify the Evidence and source that established the Outcome.

Invariant 36

Unknown execution or Outcome must not be silently classified as success or failure.

Invariant 37

Provenance must preserve causal lineage from Source through Observation, Evidence, Decision, Action, and Outcome for consequential execution.

Invariant 38

Planner output must remain bounded by the Enterprise Action Graph, Capability Registry, Action Contracts, and Trust constraints.

Invariant 39

Provenance must never be used to legitimize a model-generated capability or authority that was not explicitly registered and permitted.

Invariant 40

Model, user, retrieved text, and external tool output must not acquire authority merely through persistence.

Invariant 41

Secrets and credentials must not be persisted as provenance data.

Invariant 42

Provenance must respect tenant, organizational, environmental, regional, security, privacy, and data-classification boundaries.

Invariant 43

Provenance should minimize unnecessary duplication of enterprise payloads.

Invariant 44

Sensitive provenance must remain subject to appropriate access control and retention policy.

Invariant 45

Provenance required for consequential audit and recovery must be durable.

Invariant 46

Replay must preserve historical provenance and must not accidentally dispatch consequential Actions.

Invariant 47

Corrections must create new historical records rather than silently rewriting prior observations.

Invariant 48

Current consequential execution must use current authoritative state and applicable Trust conditions rather than relying solely on historical provenance.

Invariant 49

Source reliability must not be treated as semantic authority.

Invariant 50

Absence of Evidence must not automatically be interpreted as Evidence of absence.

Invariant 51

Negative assertions must preserve the query, scope, source, and observation context necessary to evaluate them.

Invariant 52

Read-only operations may still require provenance, authorization, and Trust when they access consequential or protected information.

Invariant 53

Provenance must preserve sufficient semantic lineage to explain why an Action was permitted.

Invariant 54

Noema must be able to distinguish what was known historically from what is known currently.

Invariant 55

Operational Memory may preserve structured provenance-backed execution history but is not generic AI memory or enterprise business-state authority.

Invariant 56

A provenance record may establish what Noema received and used; it does not establish that the source itself was objectively correct.

Invariant 57

The provenance model must preserve the distinction between source, observation, Evidence, Fact Status, Context, state, decision, Action, and Outcome.

Invariant 58

Noema must be able to answer:

“What did we know, where did we get it, when did we get it, what was its status, and how did it affect what we did?”

⸻

241. Final Definition

Provenance is the lineage of knowledge through Noema.

It identifies where information originated, when it was observed and received, what scope and authority it carries, how it was validated, transformed, reconciled, or derived, what Fact Status applies to it, and how it contributed to Intent resolution, Trust evaluation, execution, verification, and Outcome determination.

Provenance allows Noema to distinguish:

* authoritative enterprise observations from model inference
* Evidence from Provenance
* Evidence from Fact Status
* historical observations from current state
* Context Snapshots from enterprise truth
* Noema execution-domain canonical data from enterprise business-state authority
* Action permission from Action success
* Action responses from verified Outcomes
* known information from unknown information
* source identity from source authority

The canonical lineage is:

                    SOURCE
                       │
                       ▼
                  OBSERVATION
                       │
                       ▼
              VALIDATION / ADMISSION
                       │
                       ▼
                    EVIDENCE
                       │
                       ▼
              STATE RECONCILIATION
                       │
                       ▼
               FACT STATUS / STATE
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
                   EXECUTION
                       │
                       ▼
                  VERIFICATION
                       │
                       ▼
                    OUTCOME
                       │
                       ▼
             OPERATIONAL MEMORY
                  / AUDIT
                       │
                       └──────────► provenance

Enterprise Systems of Record remain authoritative for enterprise business state and feed observations into this chain.

Noema owns the semantic and execution lineage of how those observations were used.

The key principle is:

Noema should never have to say only “we knew X.” It should be able to say “we knew X because this source provided this observation, at this time, within this scope, with this Fact Status, under this semantic context, and that Evidence contributed to this decision.”