> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Evidence

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/evidence.md

⸻

1. Definition

Evidence is provenance-bearing information associated with a claim, proposition, Intent, Policy condition, state assertion, or execution condition.

Evidence is information considered in relation to what it is being used to establish, challenge, or verify.

Evidence answers:

“What supports this claim?”

The fundamental relationship is:

Claim
  │
  ▼
Evidence
  │
  ├── Source
  ├── Authority
  ├── Time
  ├── Scope
  ├── Provenance
  └── Fact Status
       │
       ▼
     Trust

Evidence is therefore not simply “data.”

It is data, observation, assertion, or derived information evaluated in relation to a specific claim.

⸻

2. Purpose

Noema operates in environments where information can be:

* incomplete
* stale
* conflicting
* inferred
* user-provided
* system-generated
* authoritative
* unavailable
* revoked
* superseded
* probabilistic

Evidence provides the semantic structure required to distinguish these conditions.

For example:

User:
"Refund my last payment."
Evidence:
Payment System reports payment #9182
status = SUCCEEDED
amount = $400
customer = 123

The Evidence may support identification of the target Payment and evaluation of whether the requested Action can proceed.

Evidence does not itself authorize execution.

⸻

3. Core Principle

Evidence supports a proposition.

It does not automatically make the proposition true.

For example:

Evidence:
CRM says customer_status = ACTIVE
Claim:
Customer 123 is active.

Whether the claim can be treated as authoritative depends on:

* source
* authority
* scope
* freshness
* semantic validity
* reconciliation
* policy
* applicable authorization
* claim requirements

The source of information and the authority of that information are distinct concepts.

⸻

4. Evidence vs Data

Data is information.

Evidence is information associated with a claim or decision and carrying sufficient provenance to evaluate its relevance and reliability.

Data:
payment.status = SUCCEEDED
Evidence:
Payment System observed
payment.status = SUCCEEDED
at 10:42:12
for payment #123
under tenant X

The second representation provides the provenance and scope required to evaluate the first as Evidence.

⸻

5. Evidence vs Canonical Data

Canonical Data represents information treated as authoritative within an explicitly defined authority scope.

Evidence records information used to support, challenge, or verify a claim.

Enterprise System of Record
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
   State Reconciliation
          │
          ▼
     Fact Status
          │
          ▼
    Trust Evaluation

Evidence and Canonical Data are therefore distinct.

Canonicality is scoped.

A source being authoritative for one claim does not make all information from that source canonical for every claim.

⸻

6. Evidence vs Context

Context is the bounded runtime view made available for resolving Intent, evaluating Trust, planning, executing, or verifying an Action.

Evidence is information within that runtime that supports or challenges a particular claim.

Context
 ├── Identity
 ├── State
 ├── Policy
 ├── Canonical Data References
 ├── Evidence
 ├── Constraints
 └── Other permitted information

Therefore:

Context describes what is available.
Evidence describes what supports a claim.

Context does not make its contents authoritative merely by containing them.

⸻

7. Evidence vs Fact Status

Evidence and Fact Status are distinct.

Evidence describes the information supporting a claim.

Fact Status describes the evaluated status of the claim.

Canonical Fact Status values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Evidence:
Ledger reports balance = $10,000.
Claim:
Account #123 balance = $10,000.
Fact Status:
VERIFIED

A different situation may be:

Evidence A:
Ledger reports balance = $10,000.
Evidence B:
Ledger replica reports balance = $8,000.
Claim:
Account #123 balance = ?
Fact Status:
CONFLICTED

Fact Status must not be collapsed into Evidence availability.

⸻

8. Evidence vs Inference

This distinction is critical.

Evidence:
Payment #123 belongs to Customer #456.
Inference:
The user probably means Payment #123.

The first is an observed or asserted proposition.

The second is an interpretation derived from available information.

Noema must not silently convert inference into authoritative Evidence.

Probabilistic interpretation may produce candidate claims, but those claims require appropriate validation and grounding before they can participate in consequential Trust evaluation.

⸻

9. Evidence vs Model Confidence

Model confidence is not Evidence of enterprise truth.

For example:

Model confidence:
0.97

does not establish:

Customer = 123

A model may provide interpretation metadata such as:

interpretation:
"User probably means account 123."
model_confidence:
0.97

This is Evidence about the model’s interpretation.

It is not Evidence that Account #123 is actually owned by the user.

Model confidence is non-authoritative metadata.

⸻

10. Evidence and the Hard Admission Boundary

External information must pass through an explicit validation and admission boundary before being treated as usable Noema Evidence.

Potential sources include:

* enterprise APIs
* databases
* events
* tool responses
* external providers
* user input
* model output
* retrieved enterprise text

The conceptual boundary is:

Untrusted Input
      │
      ▼
Schema Validation
      │
      ▼
Admission / Classification
      │
      ▼
Semantic Validation
      │
      ▼
Evidence

Malformed, structurally invalid, or otherwise inadmissible information must not silently become Evidence.

Schema validation does not itself establish authority.

⸻

11. Evidence and Trust

Evidence is an input to deterministic Trust evaluation.

Evidence
   │
   ├── Authority
   ├── Provenance
   ├── Freshness
   ├── Scope
   ├── Consistency
   ├── Fact Status
   └── Relevance
          │
          ▼
    Trust Evaluation

Trust evaluates whether the available Evidence satisfies the conditions required for the requested operation.

Evidence does not decide the Trust outcome by itself.

⸻

12. Evidence Is Claim-Relative

The same information can be strong Evidence for one claim and weak Evidence for another.

Example:

CRM:
customer.email = user@example.com

Strong Evidence for:

Customer email address

Potentially weak Evidence for:

Customer is authorized to transfer $100,000.

Evidence must therefore always be evaluated relative to the proposition it supports.

⸻

13. Evidence Types

Noema may encounter several semantically distinct Evidence classes:

* canonical-source evidence
* observed evidence
* user-provided evidence
* system evidence
* event evidence
* historical evidence
* derived evidence
* probabilistic evidence
* model-interpretation evidence

These categories should remain distinguishable where the distinction affects Trust, provenance, or auditability.

⸻

14. Canonical-Source Evidence

Canonical-source Evidence originates from a source that is authoritative for the relevant claim within an explicit scope.

Example:

Ledger:
account.balance = $25,000

If the Ledger is authoritative for account balance, this is strong Evidence for that proposition.

The authority does not automatically extend to unrelated claims.

⸻

15. Observed Evidence

Observed Evidence represents something directly observed by Noema or an Integration.

Example:

HTTP response:
status = 200
payment.status = REFUNDED

This is Evidence that the system returned that representation.

Whether the returned value is authoritative depends on:

* source authority
* claim semantics
* scope
* freshness
* validation
* reconciliation requirements

⸻

16. User Evidence

A user can provide Evidence.

Example:

"My employee ID is 4821."

This may be useful for Intent Resolution or identity investigation.

User-provided information does not automatically establish enterprise truth.

For consequential execution it may require verification against an authoritative source.

⸻

17. System Evidence

System Evidence originates from an enterprise or external system.

Examples:

* CRM record
* Payment API response
* HRIS record
* authorization service response
* database query
* policy service response

Its usefulness depends on the source’s authority for the relevant claim.

⸻

18. Event Evidence

Events can provide Evidence that something occurred.

Example:

payment.refunded

This is Evidence that a refund event was emitted.

It is not automatically equivalent to:

payment.status = REFUNDED

unless the event architecture guarantees that semantic relationship.

Event occurrence and current enterprise state must remain distinct.

⸻

19. Historical Evidence

Historical observations may remain relevant to current decisions.

Example:

Customer previously confirmed:
account = 123

This can be useful for understanding prior interaction.

It should not automatically establish:

account = 123

as the current authoritative resource.

Historical Evidence must remain temporally distinguishable from current Evidence.

⸻

20. Derived Evidence

Derived information can support a claim when its derivation is known.

Example:

Evidence:
Customer spent $50,000 in the last 12 months.
Derived from:
transactions 1..482

The derivation chain should be preserved when the derived value affects consequential execution.

Derived Evidence is not equivalent to a direct authoritative observation.

⸻

21. Probabilistic Evidence

Some Evidence is inherently probabilistic.

Example:

Fraud model:
fraud_probability = 0.93

This may support:

Claim:
Transaction has elevated fraud risk.

It is not equivalent to:

Claim:
Transaction is fraudulent.

Probabilistic Evidence must preserve its semantics and uncertainty.

⸻

22. Evidence Provenance

Consequential Evidence should preserve provenance.

Conceptually:

Evidence {
    claim
    source
    authority
    observed_at
    effective_at
    scope
    source_version
    derivation
    provenance
}

This allows Noema to answer:

Where did this Evidence come from?
When was it observed?
What source produced it?
What authority did that source have?
What claim was it used to support?

⸻

23. Evidence Source

Every meaningful Evidence item should identify its source where possible.

Examples:

* Payment API
* Ledger
* CRM
* HRIS
* Policy Engine
* User
* Noema
* External Provider

An unknown source weakens the ability to establish provenance and Trust.

Source identity alone does not establish authority.

⸻

24. Evidence Authority

Source and authority must remain distinct.

Example:

Source:
Analytics DB
Authority:
Reporting metrics

The same source may be authoritative for:

customer segmentation

but not:

account.balance

Evidence must therefore be evaluated against the authority applicable to the specific claim.

⸻

25. Evidence Freshness

Evidence becomes less useful as it becomes stale.

Example:

Evidence:
balance = $10,000
observed 30 minutes ago

For:

"Show me my balance."

this may be acceptable depending on the required freshness.

For:

"Transfer $9,000."

it may be insufficient.

Freshness is therefore claim-, Action-, Policy-, and execution-context-dependent.

⸻

26. Evidence Temporal Semantics

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

This distinction is required for auditability and reconciliation.

⸻

27. Evidence Scope

Evidence must have an explicit or inferable scope.

Possible dimensions include:

* tenant
* organization
* legal entity
* resource
* attribute
* environment
* system
* geographic or regulatory boundary
* time
* workflow
* execution

Evidence from Tenant A must never silently establish a claim about Tenant B.

⸻

28. Evidence Version

When the source provides versions, Noema should preserve them where consequential.

Example:

Account
version = 42

Source versions can help determine whether Evidence corresponds to the expected enterprise state.

Source/data versions are distinct from Noema Contract Versions.

⸻

29. Evidence Strength

Evidence should not be reduced to a single generic confidence score.

Its usefulness depends on dimensions such as:

* authority
* relevance
* freshness
* specificity
* consistency
* provenance
* completeness
* scope
* semantic validity

A highly authoritative but stale observation may be insufficient for an Action requiring current state.

⸻

30. Evidence Relevance

Evidence must directly support the claim being evaluated.

Example:

Claim:
User owns Account #123.
Evidence:
User's authenticated identity matches CRM owner identity.

This may support the claim.

But:

User lives in the same city as account holder.

is weak or irrelevant Evidence for ownership.

⸻

31. Evidence Specificity

Evidence should identify the relevant subject precisely.

Weak:

Account is active.

Strong:

Account #123
status = ACTIVE
observed_at = 10:42

Specificity reduces ambiguity and prevents Evidence from being incorrectly transferred between resources.

⸻

32. Evidence Completeness

A collection of Evidence may still be insufficient.

Example:

Evidence:
Payment #123 exists.

For a refund decision, Noema may additionally require:

* payment status
* payment amount
* refund eligibility
* target identity
* authorization
* applicable policy
* current state

Evidence completeness is determined by the requirements of the Action and Policy.

⸻

33. Evidence Sufficiency

Sufficiency is contextual.

Evidence sufficient for:

displaying payment status

may be insufficient for:

executing a $20,000 refund

The Trust Engine determines whether the available Evidence is sufficient for the requested operation.

⸻

34. Evidence Conflict

Noema may receive:

Evidence A:
Payment = REFUNDED
Evidence B:
Payment = SUCCEEDED

Noema should preserve both observations.

It must not arbitrarily select the observation that makes execution easier.

The conflict should be evaluated through:

Conflict
   ↓
Authority Evaluation
   ↓
Temporal Evaluation
   ↓
State Reconciliation
   ↓
Fact Status
   ↓
Trust Evaluation

⸻

35. Evidence Conflict Does Not Mean Data Error

Conflicting Evidence can occur because of:

* different observation times
* eventual consistency
* different system semantics
* replication lag
* different authority domains
* actual enterprise inconsistency
* incomplete synchronization

Noema should determine which explanation applies rather than assuming corruption.

⸻

36. State Reconciliation and Evidence

State Reconciliation is a first-class consumer and producer of Evidence.

It may consume observations from multiple sources and determine the best-supported representation of current state within an explicit authority scope.

Conceptually:

Enterprise Observations
        │
        ▼
     Evidence
        │
        ▼
State Reconciliation
        │
   ┌────┼────┐
   ▼    ▼    ▼
 State Fact Conflict
        │
        ▼
   Fact Status

State Reconciliation does not invent canonicality.

It applies explicit authority, temporal, freshness, and reconciliation rules to available observations.

⸻

37. Fact Status

Evidence may support a claim whose evaluated status is:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Evidence:
Authoritative Ledger reports balance = $10,000.
Claim:
Account #123 balance = $10,000.
Fact Status:
VERIFIED

If the evidence is insufficient:

Fact Status:
UNKNOWN

Fact Status is not a replacement for Evidence.

It is an evaluated semantic status of the claim.

⸻

38. Negative Evidence

Evidence can establish that something did not occur only under appropriate observation guarantees.

For example:

"No refund found."

does not necessarily establish:

"No refund exists."

Search scope, completeness, authority, and system semantics matter.

⸻

39. Absence of Evidence

Absence of Evidence is not automatically Evidence of absence.

Example:

CRM contains no customer record.

This could mean:

* customer does not exist
* CRM is not authoritative
* lookup failed
* record has not propagated
* search scope was incomplete

Noema must preserve this distinction.

⸻

40. Evidence Availability

Evidence can have explicit availability states such as:

AVAILABLE
UNAVAILABLE
STALE
CONFLICTED
INVALID
UNKNOWN

Unavailable information must not silently become negative Evidence.

⸻

41. Evidence Invalidity

Evidence may become invalid when:

* source authenticity fails
* authorization is revoked
* scope is invalid
* resource is deleted
* version is superseded
* observation expires
* schema becomes incompatible
* source semantics change
* required provenance is lost

Invalid Evidence must not continue satisfying Trust requirements.

⸻

42. Evidence Revocation

Some Evidence can be explicitly revoked.

Example:

Authorization Evidence:
User is authorized to approve payment.

Later:

Authorization service:
authorization revoked

The previous Evidence must no longer be treated as sufficient for a current authorization requirement.

⸻

43. Evidence and Identity

Identity resolution often depends on Evidence.

Example:

Evidence:
authenticated principal = user_123
Evidence:
user_123 owns account_456
Result:
principal may refer to account_456

Identity relationships should be grounded through appropriate authoritative Evidence wherever required.

Identity resolution is distinct from canonicalization.

⸻

44. Evidence and Intent Resolution

Intent Resolution uses Evidence to resolve ambiguous references.

Example:

"Refund my last payment."

Candidate payments:

Payment A
Payment B
Payment C

Evidence may include:

* timestamps
* customer ownership
* payment status
* conversation references
* transaction identifiers

Noema uses the Evidence to resolve the Intent.

If the Evidence cannot uniquely resolve the target, the Intent remains ambiguous.

⸻

45. Evidence and Ambiguity

If Evidence cannot distinguish candidates:

Payment A → plausible
Payment B → plausible

the result remains ambiguous.

Noema must not manufacture certainty.

Ambiguous
    ↓
CLARIFY

Clarification produces a new Intent version where the semantic request materially changes.

Evidence supporting the previous Intent version must not silently transfer to the new version.

⸻

46. Evidence and Authorization

Authorization claims require appropriate Evidence.

For example:

Claim:
Principal can refund Payment #123.

Evidence may come from:

* authorization service
* role assignment
* permission system
* policy engine
* enterprise access-control system

User statements about their own authority are not equivalent to authorization Evidence.

Technical authorization, policy authorization, and business authorization remain distinct.

⸻

47. Evidence and Policy

Policy evaluation may require Evidence.

Example:

Policy:
Refunds above $5,000 require manager approval.
Evidence:
refund.amount = $8,000
manager_approval = ABSENT

Policy evaluation may determine:

approval_required

The Evidence does not itself produce the Trust outcome.

⸻

48. Evidence and Preconditions

Evidence establishes whether Preconditions hold.

Precondition:

payment.status == SUCCEEDED

Evidence:

Payment System:
payment.status = SUCCEEDED

If the Evidence is sufficiently authoritative, fresh, scoped, and otherwise valid, the Precondition may be satisfied.

⸻

49. Evidence and Postconditions

After execution:

Action:
refund_payment

Noema may receive:

Evidence:
Payment System:
status = REFUNDED

This Evidence supports evaluation of the Postcondition.

Execution itself does not establish that the Postcondition was achieved.

Verification requires appropriate Evidence.

⸻

50. Evidence and Execution

Execution should record the Evidence relevant to consequential decisions.

Conceptually:

Execution
   │
   ├── Intent Version
   ├── Context Snapshot
   ├── Preconditions
   ├── Evidence
   ├── Action Contract
   ├── Attempts
   └── Outcome

This creates an auditable causal chain.

⸻

51. Evidence and Outcomes

Outcome determination should use observed Evidence.

Example:

Request submitted
        ↓
Timeout
        ↓
Execution = UNKNOWN
        ↓
Query System of Record
        ↓
Evidence = payment.status REFUNDED
        ↓
Outcome = SUCCESS

The timeout did not establish failure.

Evidence obtained through reconciliation allowed Noema to establish the actual Outcome.

⸻

52. Evidence and Failure

Failures can themselves become Evidence.

Example:

Payment API:
HTTP 403

This is Evidence that the attempted operation was rejected by the API.

It may support:

attempt rejected

but does not necessarily establish:

business operation did not occur

The semantic meaning of the failure must be evaluated against the system’s contract.

⸻

53. Evidence and Retries

Retries require careful interpretation of Evidence.

Example:

Attempt 1:
timeout
Attempt 2:
payment succeeded

The first timeout does not necessarily mean the first attempt failed.

Noema must determine whether the operation may have committed before retrying.

This is particularly important for non-idempotent Actions.

⸻

54. Evidence and Idempotency

Evidence can establish whether an Action has already been executed.

Example:

Evidence:
idempotency_key = abc123
execution status = COMPLETED

This may prevent duplicate execution.

Idempotency Evidence must be evaluated within the semantics and scope of the relevant Action and execution identity.

⸻

55. Evidence and Compensation

Compensation decisions depend on Evidence of prior state and completed Actions.

Example:

Evidence:
Order = CANCELLED
Payment = CHARGED

This may establish that compensation is required.

Compensation must still execute through an authorized enterprise capability and Action Contract.

Noema must not mutate enterprise state locally to simulate compensation.

⸻

56. Evidence and Human Intervention

When automated Trust cannot establish a safe decision, Evidence should be presented to the human operator.

The operator should receive:

* claim
* supporting Evidence
* source
* authority
* timestamps
* scope
* conflicts
* missing Evidence
* relevant policy conditions

rather than merely:

"AI is unsure."

Human intervention should be grounded in the same Evidence chain used by Noema.

⸻

57. Evidence and Auditability

Evidence is fundamental to causal auditability.

An audit trail should be able to answer:

“What did Noema rely upon when it made this decision?”

For example:

Decision:
EXECUTE REFUND
Evidence:
Payment #123 = SUCCEEDED
Principal = user_456
Refund amount = $400
Authorization = VALID
Policy = refunds_under_$5000

The audit should preserve references to the relevant Evidence rather than requiring Noema to become a duplicate System of Record.

⸻

58. Evidence and Explainability

Noema’s explanations should be Evidence-based.

Instead of:

"The model thought this was safe."

Noema should be able to state:

Payment #123 was identified as the target.
The Payment System reported it as refundable.
The principal was authorized.
The applicable policy permitted the amount.

The explanation follows the Evidence and deterministic evaluation chain.

No private model chain-of-thought is required.

⸻

59. Evidence and Determinism

Evidence enables deterministic Trust evaluation when its semantics are explicit.

Evidence
    ↓
Validation
    ↓
State Reconciliation
    ↓
Fact Status
    ↓
Policy Evaluation
    ↓
Trust Decision

Models may assist with interpretation and candidate generation.

They must not be the final authority for consequential Evidence evaluation.

⸻

60. Evidence and Confidence

Confidence may be attached to probabilistic, inferred, or derived information.

But confidence must not replace:

* authority
* provenance
* freshness
* scope
* validation
* policy
* Fact Status

For authoritative enterprise facts, source authority and semantic validity are generally more important than numerical confidence.

⸻

61. Evidence and Model Output

LLM output can provide Evidence about:

* language interpretation
* candidate Intent
* candidate entities
* candidate relationships
* candidate claims

It generally cannot establish authoritative enterprise Business State merely by asserting it.

Example:

Model:
"User probably means account 123."

This is Evidence of a model interpretation.

It is not Evidence that:

account 123 is owned by the user

That claim requires appropriate enterprise Evidence.

⸻

62. Evidence and External Systems

External systems may provide useful Evidence.

Examples:

* shipping provider
* credit bureau
* exchange-rate provider
* identity provider
* external risk service

The authority of the external source must be explicitly defined for the relevant claim.

External Evidence does not automatically become enterprise Canonical Data.

⸻

63. Evidence Chains

Evidence can depend on other Evidence.

Example:

Evidence A:
Transaction records
      ↓
Evidence B:
Total annual spend = $50,000
      ↓
Claim:
Customer qualifies for premium tier

The dependency chain should be preserved when the derived claim affects consequential execution.

⸻

64. Evidence Graph

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
State Reconciliation
  │
  ▼
Fact Status
  │
  ▼
Trust Evaluation
  │
  ▼
Decision

This graph allows Noema to trace decisions back to their supporting information.

⸻

65. Evidence Lifecycle

Conceptually:

DISCOVERED
    ↓
CAPTURED
    ↓
SCHEMA_VALIDATED
    ↓
SEMANTICALLY_VALIDATED
    ↓
AVAILABLE
    ↓
ACTIVE
    ↓
SUPERSEDED
    ↓
EXPIRED / REVOKED

Not every Evidence item passes through every state.

Lifecycle state is distinct from Fact Status.

⸻

66. Evidence Capture

When Noema captures consequential Evidence, it should preserve where applicable:

* source
* claim
* value
* timestamp
* scope
* authority
* source version
* provenance
* derivation
* classification

This prevents the Evidence record from becoming detached from its origin.

⸻

67. Evidence Validation

Evidence validation may verify:

* schema
* source authenticity
* authorization to access
* scope
* required fields
* semantic consistency
* freshness metadata
* provenance
* source version
* permitted use

Validation establishes whether the Evidence is eligible to participate in downstream evaluation.

Validation does not by itself establish that the claim is true.

⸻

68. Evidence Supersession

New Evidence may supersede old Evidence.

Example:

Evidence v1:
account.status = ACTIVE
Evidence v2:
account.status = SUSPENDED

Noema should preserve the historical observation while recognizing that v2 may represent the current observation.

State Reconciliation determines the resulting current claim where multiple observations must be evaluated.

⸻

69. Evidence Expiration

Evidence can expire when its freshness window closes.

Examples:

* authorization evidence
* risk assessment
* quoted price
* account availability
* temporary approval

Expired Evidence should not silently satisfy requirements demanding current information.

⸻

70. Evidence Revocation

Evidence may become invalid before its nominal expiration.

For example:

Approval granted
       ↓
Approval revoked

The Trust Engine must recognize revocation where the authoritative source supports it.

⸻

71. Evidence Retention

Consequential Evidence may need to be retained for:

* audit
* reconciliation
* incident investigation
* compliance
* execution reconstruction
* dispute resolution

Retention policies should follow applicable enterprise and regulatory requirements.

Retention does not imply indefinite duplication of enterprise records.

⸻

72. Evidence Minimization

Noema should retain the Evidence necessary to establish and audit consequential decisions without unnecessarily duplicating enterprise data.

Where possible, Evidence should reference enterprise resources and source records rather than copying entire enterprise records into Noema.

⸻

73. Evidence and Data Boundaries

Evidence must respect:

* tenant boundaries
* organizational boundaries
* legal boundaries
* authorization
* privacy requirements
* data classification
* retention policy
* environment boundaries

Evidence must never become a secondary channel for bypassing enterprise access controls.

Visibility of Evidence does not grant authorization to access or disclose the underlying resource.

⸻

74. Evidence and Noema Ownership

Noema may own Evidence records necessary to explain and reconstruct its decisions.

However:

Evidence owned by Noema

does not mean:

Underlying enterprise data owned by Noema

Noema owns canonical state in its own execution domain, such as:

* Intent
* Trust Decisions
* Execution state
* Outcomes
* intervention/case state

It does not thereby own enterprise Business State.

⸻

75. Evidence and Enterprise Business State

The distinction is:

Enterprise:
owns and governs enterprise Business State.
Noema:
records observations, Evidence, semantic decisions,
execution state, and Outcomes necessary for its execution domain.

Noema must not create a shadow canonical copy of enterprise Business State.

Enterprise Systems of Record remain authoritative within their defined domains.

⸻

76. Evidence and Context Snapshots

A Context Snapshot may contain references to the Evidence used at a particular point in time.

Context Snapshot
      │
      ├── Evidence #1
      ├── Evidence #2
      └── Evidence #3

Context Snapshots should preserve enough semantic identity to reconstruct which Evidence was available to a decision.

Context Snapshot does not become a new System of Record.

⸻

77. Evidence and Long-Running Execution

Long-running executions may accumulate Evidence over time.

Example:

T1:
authorization valid
T2:
payment pending
T3:
payment completed
T4:
postcondition verified

Noema should preserve the temporal sequence rather than collapsing all observations into one final value.

Long-running execution must re-evaluate relevant Evidence when freshness or state changes can affect the execution.

⸻

78. Evidence and Reconciliation

Reconciliation produces evaluated information from new observations.

Example:

Execution:
UNKNOWN
Query Payment System:
status = REFUNDED
New Evidence:
Payment #123 was refunded.
State Reconciliation:
Payment state = REFUNDED
Fact Status:
VERIFIED
Result:
Execution Outcome = SUCCESS

This is a core mechanism for recovering from uncertain execution.

⸻

79. Evidence and the Enterprise Action Graph

The Enterprise Action Graph defines possible enterprise capabilities and relationships.

Evidence grounds the runtime state relevant to those capabilities.

Graph:
Payment System can refund Payment.
Evidence:
Payment #123 is refundable.

The graph provides structural capability.

Evidence provides runtime grounding.

The graph does not become evidence merely because an Action is represented in it.

⸻

80. Evidence and Action Contracts

Action Contracts may require specific Evidence or claims before execution.

Example:

refund_payment
required conditions:
- payment exists
- payment is refundable
- principal authorized
- amount within policy

The Action Contract defines execution semantics and requirements.

Evidence provides the runtime information needed to evaluate those requirements.

⸻

81. Evidence and Planner

The Planner may select or compose execution paths only within:

* Enterprise Action Graph
* Capability Registry
* Action Contracts
* Trust constraints

The Planner cannot:

* invent capabilities
* invent authority
* manufacture Evidence
* bypass Trust
* reinterpret Evidence to make an Action executable
* modify Action Contract semantics

Planner output remains subject to deterministic validation and Trust.

⸻

82. Evidence and Preconditions

A Precondition can be expressed as a claim requiring Evidence.

Example:

Precondition:
Account.status = ACTIVE

Evidence:

Account System:
Account.status = ACTIVE

Trust evaluates whether the Evidence satisfies the Precondition within the applicable scope, freshness, authority, and policy.

⸻

83. Evidence and Postconditions

A Postcondition is similarly a claim requiring verification after execution.

Example:

Postcondition:
Payment.status = REFUNDED

Evidence:

Payment System:
Payment.status = REFUNDED

Noema can then establish that the Postcondition is satisfied.

The Action’s invocation alone does not establish the Postcondition.

⸻

84. Evidence and Unknown

Unknown must remain explicit.

No Evidence that refund succeeded.

must not become:

Refund failed.

The correct semantic state may be:

Execution = UNKNOWN
Outcome = UNKNOWN
Fact Status = UNKNOWN

until sufficient Evidence is obtained.

Unknown is not false.

⸻

85. Evidence and Clarification

Evidence can expose ambiguity.

Example:

Evidence:
Two accounts match the user's description.

This does not mean Evidence failed.

It establishes:

Claim:
Target account cannot yet be uniquely determined.

That condition can deterministically trigger:

CLARIFY

Clarification of a materially different Intent creates a new Intent version.

⸻

86. Evidence and Escalation

If Evidence remains insufficient or conflicting after available automated resolution:

Evidence Conflict
       ↓
State Reconciliation
       ↓
Trust Evaluation
       ↓
ESCALATE

The escalation package should include the relevant Evidence, provenance, conflicts, applicable policy conditions, and unresolved claims.

⸻

87. Evidence and Policy Evaluation

Policy Evaluation consumes Evidence.

Policy
   +
Evidence
   ↓
Policy Evaluation
   ↓
Policy Result
   ↓
Trust Decision

Example:

Policy:
Refund > $5,000 requires approval.
Evidence:
Refund amount = $8,000.
Manager approval = absent.
Policy Result:
REQUIRES_APPROVAL

The policy result is not itself the final Trust outcome.

⸻

88. Evidence and Risk

Risk assessment may consume Evidence such as:

* transaction amount
* account age
* historical behavior
* location
* velocity
* fraud score

Risk is an evaluated decision input or result, not necessarily canonical enterprise data.

The underlying Evidence must remain traceable.

A risk score does not override hard Trust constraints or enterprise authorization.

⸻

89. Evidence and Authorization

Authorization should be established through appropriate authoritative Evidence.

Identity
   ↓
Permission Evidence
   ↓
Authorization Evaluation
   ↓
Trust Decision

A model’s belief that a user “seems authorized” is not sufficient for consequential execution.

Technical authorization, policy authorization, and business authorization remain distinct.

⸻

90. Evidence and Human Confirmation

User confirmation can become Evidence of explicit consent for a particular Action.

Example:

Noema:
"This will transfer $20,000. Continue?"
User:
"Yes."

This creates Evidence that:

The user explicitly confirmed the presented Action.

It does not establish unrelated facts such as:

* account ownership
* balance
* authorization
* eligibility

Confirmation is a control requirement, not a replacement for authorization.

⸻

91. Evidence and Confirmation Scope

Confirmation Evidence must be bound to the Action and Context presented to the user.

A confirmation for:

Transfer $500

must not automatically authorize:

Transfer $5,000

Likewise:

Confirm refund Payment #123

must not automatically confirm:

Refund Payment #456

The confirmed semantic parameters must remain identifiable.

⸻

92. Evidence and Intent Evolution

As Intent changes, its supporting Evidence may change.

Example:

Intent v1
→ Payment #123
Clarification
Intent v2
→ Payment #456

Evidence associated with v1 must not silently carry over to v2 if it no longer applies.

The exact Intent version used by a Trust Decision must be preserved.

⸻

93. Evidence and Intent Immutability

Once an Intent Object is admitted to Trust, its semantic meaning is immutable.

If material clarification or correction occurs:

Intent v1
    ↓
Intent v2
supersedes v1

Evidence must reference the Intent version to which it applies.

Noema must not mutate historical Evidence relationships to make an old decision appear to have been made against a later Intent.

⸻

94. Evidence and Intent Composition

For compound Intent, each Action may have its own Evidence requirements.

Example:

Intent:
Cancel order + refund payment
Action A:
cancel_order
Evidence set A
Action B:
refund_payment
Evidence set B

Evidence must remain linked to the relevant:

* Intent version
* Action
* Resource
* execution scope

Evidence for one Action must not silently satisfy another Action’s requirements.

⸻

95. Evidence and Execution Attempts

Evidence should be associated with the execution attempt that produced or consumed it.

Execution
 ├── Attempt 1
 │     └── Evidence
 ├── Attempt 2
 │     └── Evidence
 └── Final Outcome

This is especially important for:

* retries
* timeouts
* duplicate responses
* reconciliation
* compensation
* recovery

⸻

96. Evidence and Idempotent Recovery

If an execution times out, Noema should seek Evidence about whether the operation committed before retrying.

Example:

Attempt 1:
timeout
       ↓
Query:
idempotency_key = abc123
       ↓
Evidence:
already completed
       ↓
Do not execute again

A timeout is an execution condition, not proof of failure.

⸻

97. Evidence and Compensation

Before compensation, Noema should establish the actual current state.

Expected:

Order cancelled
Payment charged

Evidence:

Order = CANCELLED
Payment = CHARGED

This Evidence supports the compensation decision.

Compensation remains subject to Trust and authorized Action Contracts.

⸻

98. Evidence and Security

All Evidence entering Noema must be treated according to its trust boundary.

The following are untrusted by default:

* user input
* model output
* retrieved enterprise text
* tool responses
* external payloads

The model must not possess enterprise credentials or direct unrestricted enterprise access.

No free-form model output may directly become an executable enterprise operation.

Evidence cannot be used to bypass authorization or data-access boundaries.

⸻

99. Evidence and Read-Only Operations

Evidence is not limited to write Actions.

A read-only operation can be consequential when it exposes protected or sensitive enterprise information.

For example:

"Show me the balance of Account #123."

may require:

* identity Evidence
* account relationship Evidence
* authorization Evidence
* current-state Evidence

Read-only does not mean trust-free.

⸻

100. Evidence and Audit Record

A consequential audit record should conceptually connect:

Intent Version
      ↓
Context Snapshot
      ↓
Evidence
      ↓
Fact Status
      ↓
State Reconciliation
      ↓
Trust Decision
      ↓
Action Contract
      ↓
Execution Attempt
      ↓
Verification Evidence
      ↓
Outcome

This is the causal chain required to reconstruct why an operation was permitted and what actually happened.

⸻

101. Evidence Model

Conceptually:

Evidence {
    evidence_id
    claim
    subject
    predicate
    object
    value
    source
    authority
    scope
    observed_at
    effective_at
    expires_at
    source_version
    classification
    provenance
    derivation
    fact_status
}

This is a semantic model, not a mandatory storage schema.

The model should preserve the distinction between the Evidence itself and the evaluated status of the claim it supports.

⸻

102. Evidence Set

A Trust Decision may require multiple Evidence items.

Conceptually:

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
- eligibility evidence
- risk evidence

Evidence Sets should not imply that all included Evidence has equal authority or semantic status.

⸻

103. Evidence Claim

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

Claims provide the semantic target against which Evidence can be evaluated.

⸻

104. Evidence Relationships

Evidence may participate in relationships such as:

Evidence
   ├── supports → Claim
   ├── sourced_from → System
   ├── derived_from → Evidence
   ├── supersedes → Evidence
   ├── contradicts → Evidence
   ├── scoped_to → Resource
   ├── associated_with → Intent Version
   ├── consumed_by → Trust Decision
   └── verifies → Postcondition

These relationships provide the structure required for causal reconstruction.

⸻

105. Evidence Graph Example

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
      │
      ▼
Payment System
      │
      ▼
Verification Observation
      │
      ▼
Evidence #57
      │
      ▼
Postcondition:
Payment #123 = REFUNDED

The same Evidence model supports both pre-execution Trust and post-execution verification.

⸻

106. Evidence Quality

Evidence quality can be evaluated across dimensions:

Dimension	Question
Authority	Is the source authoritative for this claim?
Relevance	Does it support the current proposition?
Freshness	Is it sufficiently current?
Specificity	Does it identify the exact subject?
Provenance	Can the source and derivation be traced?
Completeness	Are required facts present?
Consistency	Does it conflict with stronger Evidence?
Scope	Does it apply to this tenant, resource, environment, and operation?
Validity	Has the Evidence passed required admission and semantic validation?

No single dimension should automatically determine Trust.

⸻

107. Evidence Is Not a Confidence Score

A common mistake is:

Evidence confidence = 95%

and therefore:

EXECUTE

Noema should instead evaluate:

Evidence
+
Authority
+
Fact Status
+
Policy
+
Authorization
+
Freshness
+
Scope
+
Ambiguity
+
Action requirements

and produce a deterministic Trust state.

⸻

108. Evidence and Canonical Data References

Evidence may reference Canonical Data without becoming Canonical Data itself.

Conceptually:

CanonicalDataReference {
    claim
    subject
    attribute
    value
    source_system
    authority_scope
    observed_at
    effective_at
    source_version
    freshness
    provenance
}

The reference identifies why a particular enterprise representation is considered authoritative for the claim within its scope.

Noema should not infer universal canonicality from a single reference.

⸻

109. Evidence and State Reconciliation Model

Conceptually:

StateReconciliation {
    subject
    observations[]
    authority_rules
    freshness_requirements
    result
    fact_status
    conflicts[]
    reconciled_at
}

Evidence supplies observations.

State Reconciliation evaluates those observations against explicit reconciliation semantics.

The result may be:

* reconciled state
* verified claim
* conflicted claim
* stale state
* unknown state

⸻

110. Evidence and Enterprise Data Boundaries

Evidence may reference enterprise data without taking ownership of it.

The distinction is:

Enterprise System of Record
        │
        │ authoritative within defined domain
        ▼
Enterprise Business State
        │
        ▼
Observation / Evidence
        │
        ▼
Noema execution-domain reasoning

Noema must not create a shadow System of Record for enterprise Business State.

⸻

111. Evidence and Outcome

Outcome is not equivalent to Evidence.

Evidence supports the determination of an Outcome.

Example:

Evidence:
Payment System reports REFUNDED.
Outcome:
SUCCESS

The Outcome is a semantic result of the execution and verification lifecycle.

Similarly:

Evidence unavailable

does not mean:

Outcome = FAILURE

The correct result may remain:

Outcome = UNKNOWN

⸻

112. Evidence and Trust EXECUTE

A Trust Decision of:

EXECUTE

does not mean:

Action succeeded.

It means the resolved Action satisfies the applicable Trust conditions and is permitted to proceed.

Evidence before execution supports permission.

Evidence after execution supports verification.

These are separate stages.

⸻

113. Evidence and Operational Memory

Consequential Evidence may be referenced by Operational Memory.

Operational Memory may preserve:

* cases
* execution attempts
* Evidence references
* reconciliation results
* intervention history
* outcomes
* failure patterns

Operational Memory is not generic AI memory and is not an authority for enterprise Business State.

It records structured operational history.

⸻

114. Evidence and Versioning

Evidence versioning must remain distinct from Contract Versioning.

Relevant version dimensions may include:

source_version
data_version
effective_version
observation_version
contract_version
policy_version

These must not be conflated.

A historical Trust Decision should preserve the versions necessary to reconstruct the Evidence available at decision time.

⸻

115. Evidence and Causal Audit

Causal auditability requires a chain such as:

Claim
  ↓
Source
  ↓
Observation
  ↓
Evidence
  ↓
State Reconciliation
  ↓
Fact Status
  ↓
Trust Decision
  ↓
Action Contract
  ↓
Execution Attempt
  ↓
Verification Evidence
  ↓
Outcome

This is more important than retaining unrestricted internal model reasoning.

Noema must be able to explain the decision through observable semantic inputs and deterministic evaluations.

⸻

116. Evidence and Scope of Authority

Authority must always be interpreted within scope.

Example:

Ledger A
authority:
Account balances
CRM B
authority:
Customer contact information

Neither source should automatically be treated as authoritative for the other’s domain.

Authority may be scoped by:

* claim
* resource
* tenant
* organization
* environment
* legal entity
* time
* system
* operation

⸻

117. Evidence and Authorization Boundaries

Possessing Evidence does not itself grant permission to use or disclose the underlying information.

For example:

Evidence:
Customer #123 has balance $50,000.

does not imply:

Current principal may view Customer #123's balance.

Access authorization must be independently evaluated.

This prevents Evidence from becoming an authorization bypass.

⸻

118. Evidence and Canonicalization

Canonicalization and Evidence are related but distinct.

Canonicalization selects or represents an authoritative interpretation of a claim within an explicit scope.

Evidence provides support for that interpretation.

Canonicalization must not become guessing.

Example:

Evidence:
Two enterprise systems identify different customer IDs.
Result:
CONFLICTED

Noema must not arbitrarily canonicalize one value simply because it is easier to execute.

⸻

119. Evidence and Unknown

Unknown is a valid semantic result when available Evidence cannot establish a claim.

Examples:

Target identity = UNKNOWN
Current state = UNKNOWN
Execution state = UNKNOWN
Outcome = UNKNOWN

Noema must not replace unknown with:

* false
* absent
* failed
* succeeded
* authorized
* unauthorized

without sufficient Evidence.

⸻

120. Core Invariants

Invariant 1

Evidence supports a claim; it does not automatically establish truth.

Invariant 2

Evidence must remain distinguishable from Canonical Data.

Invariant 3

Evidence must remain distinguishable from Context.

Invariant 4

Evidence must remain distinguishable from Fact Status.

Invariant 5

Evidence must remain distinguishable from model inference.

Invariant 6

Model confidence is not a substitute for Evidence.

Invariant 7

Evidence must be evaluated relative to the claim it supports.

Invariant 8

Evidence source and authority must remain distinct.

Invariant 9

Consequential Evidence should preserve provenance.

Invariant 10

Consequential Evidence should preserve relevant temporal metadata.

Invariant 11

Evidence freshness is claim-, Action-, and Policy-dependent.

Invariant 12

Evidence must have an understood scope.

Invariant 13

Evidence from one tenant or organizational boundary must not silently establish claims in another.

Invariant 14

Evidence completeness and Evidence sufficiency are distinct.

Invariant 15

Evidence may be strong for one claim and irrelevant to another.

Invariant 16

Conflicting Evidence must be preserved rather than arbitrarily discarded.

Invariant 17

Authority, not source count, determines which Evidence is applicable when sources conflict.

Invariant 18

Absence of Evidence must not automatically be interpreted as Evidence of absence.

Invariant 19

Unavailable Evidence must not silently become negative Evidence.

Invariant 20

Unknown must remain explicitly distinguishable from false.

Invariant 21

Stale Evidence must not satisfy requirements that demand current state.

Invariant 22

Invalid or revoked Evidence must not continue satisfying Trust requirements.

Invariant 23

Historical Evidence must remain distinguishable from current Evidence.

Invariant 24

Derived Evidence should preserve its derivation chain when consequential.

Invariant 25

User-provided Evidence does not automatically establish enterprise truth.

Invariant 26

Model-generated Evidence about enterprise state does not automatically establish enterprise truth.

Invariant 27

Events provide Evidence of occurrences but do not automatically establish persistent state unless their semantics guarantee it.

Invariant 28

Authorization claims must be supported by appropriate authorization Evidence.

Invariant 29

Identity resolution should use appropriate Evidence before consequential execution.

Invariant 30

Evidence supporting one Intent or Action must not silently transfer to a different Intent version, Resource, or Action.

Invariant 31

User confirmation Evidence must be bound to the specific Action and Context presented for confirmation.

Invariant 32

Evidence required for consequential execution should be captured sufficiently to reconstruct the Trust Decision.

Invariant 33

Evidence should respect enterprise data, privacy, organizational, legal, and authorization boundaries.

Invariant 34

Noema may own Evidence records without becoming the owner of the underlying enterprise Business State.

Invariant 35

Evidence used for retries and recovery must account for the possibility that an operation succeeded even when the original response was unavailable.

Invariant 36

Evidence should support deterministic Trust decisions rather than replace them.

Invariant 37

External payloads, events, tool responses, retrieved text, user input, and model output must not be treated as authoritative Evidence before the applicable validation and admission boundary.

Invariant 38

Schema validation establishes structural admissibility, not authority or truth.

Invariant 39

State Reconciliation must remain distinct from Evidence collection; reconciliation evaluates observations and produces reconciled claims or state with explicit conflict and unknown semantics.

Invariant 40

Fact Status must remain distinct from Evidence, Context, State, Outcome, and Canonical Data.

Invariant 41

Canonicality must be scoped to an explicit claim, authority domain, resource, and applicable context rather than applied universally to an entire source or entity.

Invariant 42

Source, authority, freshness, availability, validity, and authorization are separate dimensions and must not be collapsed into a single trust score.

Invariant 43

Evidence must not grant access to the underlying enterprise resource.

Invariant 44

Noema must not create shadow canonical enterprise Business State merely by retaining Evidence or reconciled observations.

Invariant 45

The Planner must not manufacture Evidence, authority, capabilities, or executable meaning.

Invariant 46

Evidence associated with an admitted Intent must preserve the exact Intent version to which it applies.

Invariant 47

A Trust Decision of EXECUTE does not establish execution success.

Invariant 48

Verification Evidence is required to establish applicable postconditions and actual execution Outcome.

Invariant 49

A timeout or unavailable response must not automatically be interpreted as execution failure.

Invariant 50

When available Evidence cannot establish a safe execution condition, Noema must transition into the appropriate deterministic state, such as clarification, escalation, rejection, or unresolved/unknown execution, rather than manufacture certainty.

⸻

121. Final Definition

Evidence is provenance-bearing information associated with a claim and used by Noema to establish, validate, challenge, reconcile, or verify the conditions required for Intent resolution, Trust evaluation, Action execution, and Outcome verification.

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
          ┌─────────┼─────────┐
          ▼         ▼         ▼
      Authority  Freshness   Scope
          │         │         │
          └─────────┼─────────┘
                    ▼
           STATE RECONCILIATION
                    │
                    ▼
               FACT STATUS
                    │
                    ▼
             TRUST EVALUATION
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     EXECUTE      CLARIFY     ESCALATE
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
    OBSERVATION
        │
        ▼
      EVIDENCE
        │
        ▼
      OUTCOME

Evidence does not tell Noema what to do.

Evidence establishes what Noema can legitimately claim to know about a proposition within a defined scope.

State Reconciliation evaluates observations where current state must be reconstructed.

Fact Status expresses the evaluated status of the resulting claim.

Deterministic Trust determines what the validated, resolved, and reconciled information permits Noema to do.

The key Noema principle is:

Evidence establishes what Noema can legitimately know; deterministic Trust determines what that knowledge permits Noema to do.