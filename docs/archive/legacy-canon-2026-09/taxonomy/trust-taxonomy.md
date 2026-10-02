Trust Taxonomy

Status: Foundational
Version: 0.1
Domain: Taxonomy
Canonical Path: taxonomy/trust-taxonomy.md

⸻

1. Definition

Trust is Noema’s structured determination of whether an Intent is permitted to proceed toward execution under the applicable authority, policy, authorization, risk, evidence, and governance conditions.

Trust does not establish what the Actor intends.

Trust does not define how the Intent will be executed.

Trust does not perform Actions.

Trust establishes whether the resolved and validated Intent may cross the applicable execution boundary.

The canonical relationship is:

Expression
    ↓
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

Therefore:

Intent establishes what the Actor intends. Validation establishes whether that Intent is valid. Trust establishes whether it may proceed. Execution establishes what actually happened.

⸻

2. Purpose

The Trust Taxonomy provides the canonical vocabulary for representing the conditions governing execution eligibility.

It exists to prevent different forms of authority, evidence, permission, policy, approval, and risk from being collapsed into a single undifferentiated concept of “trust.”

Trust must be decomposable into explicit dimensions.

Conceptually:

Trust
├── Identity
├── Authentication
├── Authorization
├── Authority
├── Policy
├── Consent
├── Approval
├── Risk
├── Evidence
├── Preconditions
├── Constraints
├── Temporal validity
└── Governance

Not every Intent requires every dimension.

The applicable Trust requirements depend on the Intent, Action, Actor, capabilities, policies, and execution context.

⸻

3. Core Principle

Trust is not a feeling, score, probability, or model confidence.

Trust is an explicit architectural determination based on defined requirements and evidence.

Therefore:

Model confidence
        ≠
Trust

and:

Identity
        ≠
Authorization

and:

Authorization
        ≠
Approval

and:

Approval
        ≠
Consent

and:

Capability
        ≠
Permission

and:

Trust
        ≠
Execution success

Each concept must retain its own semantic meaning.

⸻

4. Trust Is Multi-Dimensional

A Trust decision may depend on several independent dimensions.

For example:

Actor Identity
      +
Authentication
      +
Authorization
      +
Policy Compliance
      +
Required Approval
      +
Required Consent
      +
Risk Conditions
      +
Evidence Sufficiency
      +
Temporal Validity
      +
Action Preconditions
      ↓
Trust Decision

A failure in one required dimension may prevent execution even when all other dimensions are satisfied.

⸻

5. Trust vs Intent

Intent answers:

What does the Actor want?

Trust answers:

May that Intent proceed under the applicable governance conditions?

Example:

Intent:
Transfer ₦50,000 to customer_123

Trust may establish:

Actor identified
Actor authenticated
Authorization valid
Transfer policy satisfied
No approval required
Risk conditions satisfied
Required evidence available

Only then may the Intent proceed toward execution.

Therefore:

Resolved Intent
        ≠
Trusted Intent

⸻

6. Trust vs Validation

Validation and Trust are separate architectural concerns.

Validation determines whether the Intent is structurally and semantically valid.

Trust determines whether the valid Intent may proceed.

Conceptually:

Intent
  ↓
Validation
  ↓
Valid
  ↓
Trust
  ↓
Execution Eligibility

An Intent may be:

VALID
+
NOT TRUSTED

For example, an Intent may be structurally correct but require approval that has not yet been obtained.

⸻

7. Trust vs Action Graph

The Action Graph represents execution structure.

It does not grant authorization.

Therefore:

Trust
  ↓
Execution Eligibility
  ↓
Action Graph

A graph containing:

TRANSFER_FUNDS

does not establish that the Actor is authorized to transfer funds.

Authorization must be independently established by the Trust system and applicable Action Contract.

⸻

8. Trust vs Action Contract

An Action Contract defines the executable interface, obligations, constraints, and conditions of an Action.

Trust determines whether the Actor and Intent satisfy the authority required to reach that execution boundary.

Conceptually:

Intent
   ↓
Trust
   ↓
Action Graph
   ↓
Action Contract
   ↓
Execution Consumer

Action Contracts may impose additional execution-time conditions.

Trust does not eliminate those requirements.

⸻

9. Trust vs Capability

A capability establishes that a system exposes an operation.

For example:

Capability:
card.replacement.create

This does not establish:

Actor is authorized to replace the card

Therefore:

Capability ≠ Authorization

Capability discovery and Trust evaluation must remain separate.

⸻

10. Trust Subject

A Trust decision must have an identifiable subject.

The subject is generally the Intent and its associated Actor.

Conceptually:

TrustSubject {
    actor
    intent
    intent_version
    requested_actions
    target_resources
    relevant_context
}

The Trust subject must remain stable enough to determine what exactly was evaluated.

A Trust decision for one Intent version must not silently transfer to a materially different Intent.

⸻

11. Trust Decision

A Trust Decision represents the result of evaluating applicable Trust requirements.

Conceptually:

TrustDecision {
    decision
    subject
    requirements
    satisfied
    unsatisfied
    unknown
    evidence
    policy_versions
    authorization_context
    evaluation_id
    timestamp
    expiry
    provenance
}

Possible decision states include:

READY
WAITING
BLOCKED
DENIED
UNKNOWN
EXPIRED

The exact state machine belongs to the Trust architecture.

⸻

12. Trust Requirement

A Trust Requirement expresses a condition that must be satisfied before an Intent or Action may proceed.

Conceptually:

TrustRequirement {
    id
    type
    subject
    condition
    evidence_required
    blocking
    status
    provenance
}

Examples:

Actor must be authenticated
Actor must be authorized
Approval must be obtained
Consent must be present
Risk threshold must be satisfied
Required evidence must be available
Policy condition must hold
Action precondition must be satisfied

⸻

13. Requirement Status

Trust requirements should distinguish at least:

SATISFIED
UNSATISFIED
UNKNOWN
NOT_APPLICABLE
EXPIRED
REVOKED
PENDING

These states must not be collapsed.

In particular:

UNKNOWN ≠ SATISFIED

An unavailable authorization result cannot be treated as authorization.

⸻

14. Identity

Identity establishes which Actor or principal is associated with the Intent.

Conceptually:

Identity:
actor = actor_123

Identity answers:

Who is the Actor?

Identity alone does not establish:

May this Actor perform the requested Action?

Therefore:

Identity ≠ Authorization

⸻

15. Authentication

Authentication establishes that the Actor has satisfied the applicable mechanism for proving or asserting control of an identity.

Examples may include:

authenticated_session
strong_authentication
device_authentication
organizational_authentication
delegated_identity

Authentication is evidence relevant to Trust.

It does not by itself establish authorization.

⸻

16. Authorization

Authorization establishes whether an Actor or principal is permitted to perform a specified Action against a specified resource under specified conditions.

Conceptually:

Authorization(
    Actor,
    Action,
    Resource,
    Context
)
→
ALLOW | DENY | UNKNOWN

Authorization should be evaluated against the actual Action and resource rather than merely the broad Intent category.

⸻

17. Authority

Authority represents the basis on which an Actor or system is permitted to act.

Authority may arise from:

* ownership
* delegated authority
* organizational role
* legal authority
* contractual authority
* explicit delegation
* system-defined authority

The exact authority model depends on the domain.

Authority should not be inferred merely from possession of an identifier.

⸻

18. Delegation

An Actor may act through delegated authority.

Conceptually:

Principal
    ↓
Delegation
    ↓
Delegate
    ↓
Action

Delegation should specify:

* delegator
* delegate
* permitted scope
* applicable resources
* temporal validity
* constraints
* revocation status

Delegation must not silently expand beyond its defined scope.

⸻

19. Consent

Consent represents an explicit authorization or agreement from the relevant Actor where the governing semantics require it.

Consent is distinct from authentication and authorization.

For example:

Actor authenticated
        ↓
Actor authorized
        ↓
Consent required
        ↓
Consent obtained

A valid authentication event must not be interpreted as consent unless the applicable semantics explicitly establish that equivalence.

⸻

20. Confirmation

Confirmation represents explicit Actor confirmation of a specific pending action or decision where confirmation is required.

Example:

DELETE_ACCOUNT
      ↓
CONFIRMATION_REQUIRED
      ↓
Actor confirms
      ↓
EXECUTE

Confirmation should be bound to the relevant Intent, Action, scope, and version.

A later materially changed Intent must not automatically inherit an earlier confirmation.

⸻

21. Approval

Approval represents authorization granted through an organizational or governance process.

Example:

Transfer > policy threshold
        ↓
Approval required
        ↓
Approved
        ↓
Execution eligible

Approval is distinct from Actor confirmation.

An organizational approver may authorize an operation even when the Actor is not the approver.

⸻

22. Approval Scope

Approval must be evaluated against its scope.

Relevant dimensions may include:

* Intent
* Action
* amount
* resource
* Actor
* destination
* time
* policy
* organizational authority

Approval for one Action must not automatically authorize another Action.

⸻

23. Approval Expiration

Approvals may expire.

Example:

Approval
valid_until = T1
T2 > T1

At T2:

Approval = EXPIRED

Noema must not silently treat expired approval as current approval.

⸻

24. Revocation

Trust-relevant authority may be revoked.

Examples:

authorization revoked
delegation revoked
approval revoked
consent withdrawn
credential revoked
capability withdrawn

Revocation may invalidate a previously executable Intent depending on the applicable semantics.

⸻

25. Policy

Policy establishes rules governing whether an Intent or Action may proceed.

Examples:

Transfer limit
Approval threshold
Restricted destination
Required verification
Business-hour restriction
Segregation-of-duty requirement

Policy is distinct from authorization.

An Actor may have general authorization while a specific policy prohibits a particular operation.

⸻

26. Policy Versioning

Trust decisions must identify the applicable policy versions.

Conceptually:

Trust Evaluation:
policy_set = 17
policy_version = 4

A later policy change must not silently rewrite historical Trust decisions.

Material policy changes may require re-evaluation.

⸻

27. Policy Conflict

Multiple policies may apply to the same Intent.

The architecture must define how conflicts are resolved.

Possible semantics may include:

DENY overrides ALLOW
more restrictive policy applies
explicit precedence order
policy conflict → BLOCKED

The applicable policy semantics must be deterministic and versioned.

The Trust system must not resolve policy conflicts through arbitrary model judgment.

⸻

28. Risk

Risk represents conditions associated with potential harm, loss, abuse, fraud, or other undesirable consequences relevant to the requested execution.

Risk evaluation may consider:

* Action
* Actor
* resource
* amount
* destination
* context
* historical evidence
* policy
* environmental conditions

Risk does not itself determine Intent meaning.

⸻

29. Risk Is Not Trust

Risk and Trust are related but distinct.

For example:

Risk = LOW

does not necessarily mean:

Authorization = ALLOWED

Similarly:

Risk = HIGH

does not necessarily mean:

Authorization = DENIED

Risk controls may instead require:

additional verification
approval
human review
stronger authentication
additional evidence

⸻

30. Risk Conditions

Risk requirements may produce explicit conditions.

Example:

HIGH_RISK
    ↓
ADDITIONAL_VERIFICATION
    ↓
APPROVAL
    ↓
EXECUTION

These requirements may affect the Action Graph.

The Trust taxonomy represents the requirement.

The Action Graph represents the resulting execution dependency.

⸻

31. Evidence

Evidence is information used to establish Trust-relevant conditions.

Examples include:

* authentication evidence
* authorization records
* approval records
* consent records
* policy evaluation results
* external system state
* identity records
* transaction records
* capability metadata

Evidence must retain provenance.

⸻

32. Evidence Is Not Authority

Evidence supports a Trust determination.

It does not necessarily constitute authority itself.

For example:

Identity record

may establish identity but does not necessarily establish authorization.

Therefore:

Evidence
    ↓
supports evaluation
    ↓
Trust Decision

rather than:

Evidence
    ↓
automatic authorization

⸻

33. Evidence Freshness

Trust-relevant evidence may have a validity period.

Conceptually:

Evidence
created_at = T1
valid_until = T2

After T2:

Evidence = EXPIRED

The Trust system must not silently treat stale evidence as current when freshness is material.

⸻

34. Evidence Revocation

Evidence may become invalid after issuance.

Examples:

credential revoked
authorization revoked
approval withdrawn
delegation revoked
resource ownership changed

Trust evaluation must account for revocation where applicable.

⸻

35. Evidence Conflict

Multiple evidence sources may disagree.

Example:

System A:
authorization = ALLOW
System B:
authorization = REVOKED

The Trust system must apply explicit source authority and conflict-resolution semantics.

It must not arbitrarily select the most convenient evidence.

⸻

36. Unknown Trust Conditions

Trust must represent unknown conditions explicitly.

Example:

Authorization service unavailable

This produces:

authorization = UNKNOWN

not:

authorization = ALLOW

and not necessarily:

authorization = DENY

The correct downstream state depends on the governing requirement.

For a mandatory authorization check:

UNKNOWN → BLOCKED / WAITING

unless the applicable policy explicitly defines another behavior.

⸻

37. Trust Preconditions

Trust may require preconditions before execution.

Examples:

Actor authenticated
resource active
authorization valid
approval present
policy satisfied
risk check completed

An unmet mandatory precondition prevents the relevant execution boundary from being crossed.

⸻

38. Execution-Time Preconditions

Some conditions must be checked again immediately before execution because external state may change.

Example:

T1:
Authorization = valid
T2:
Authorization revoked
T3:
Execute

The execution consumer may reject the Action.

This reflects the difference between:

Trust evaluation state

and:

execution-time business state

⸻

39. Time-Bounded Trust

Trust decisions may be temporally bounded.

Conceptually:

Trust:
READY
valid_from = T1
valid_until = T2

After T2:

Trust = EXPIRED

A new evaluation may be required.

Trust must not be assumed to remain valid indefinitely.

⸻

40. Scope-Bounded Trust

Trust decisions should have explicit scope.

A decision may apply to:

* a specific Intent
* an Intent version
* a specific Action
* a resource
* an amount
* a destination
* a capability
* a time period

A Trust decision must not silently expand beyond its evaluated scope.

⸻

41. Trust Inheritance

Trust should not automatically propagate from one semantic object to another.

For example:

Intent A → TRUSTED

does not imply:

Intent B → TRUSTED

Likewise:

Intent v1 → TRUSTED

does not automatically imply:

Intent v2 → TRUSTED

when v2 materially changes the Intent.

⸻

42. Trust Re-Evaluation

Trust must be re-evaluated when material conditions change.

Examples:

* Intent changes
* Actor changes
* authorization changes
* policy changes
* approval changes
* consent changes
* risk changes materially
* required evidence expires
* capability changes
* execution context changes
* relevant resource state changes

Conceptually:

Trusted Intent
      ↓
Material Change
      ↓
Trust Re-Evaluation
      ↓
New Trust Decision

⸻

43. Trust Decision States

The canonical Trust taxonomy may distinguish:

READY

All mandatory Trust requirements required for the current execution boundary are satisfied.

READY

does not guarantee execution success.

WAITING

Execution cannot proceed because a required condition is expected but not yet resolved.

Examples:

approval pending
authentication pending
external evidence pending
human review pending

BLOCKED

Execution cannot proceed because a required condition is currently unsatisfied or unavailable.

DENIED

A governing authority explicitly prohibits the requested execution.

UNKNOWN

The Trust system cannot currently determine whether a required condition is satisfied.

EXPIRED

A previously valid Trust determination is no longer temporally valid.

⸻

44. READY Does Not Mean Successful

The distinction is fundamental:

Trust = READY

means:

The Intent satisfies the applicable Trust requirements for proceeding to the next execution boundary.

It does not mean:

Execution = SUCCESS

External systems may still reject, fail, timeout, or produce unknown outcomes.

⸻

45. BLOCKED vs DENIED

These states must remain distinct.

BLOCKED

A required condition is not currently satisfied, but the condition may potentially become satisfied.

Example:

Approval pending

DENIED

A governing rule or authority explicitly prohibits the operation.

Example:

Policy prohibits transfer to destination X

Therefore:

BLOCKED ≠ DENIED

⸻

46. WAITING vs UNKNOWN

These states may overlap operationally but should retain different semantics.

WAITING

The system knows which condition is pending.

Example:

Waiting for approval.

UNKNOWN

The system cannot currently determine the state of a required condition.

Example:

Authorization service unavailable.

Where the architecture requires the distinction, the Trust system must preserve it.

⸻

47. Trust Decision Composition

A composite Trust decision may be represented as:

TrustDecision
├── Identity
├── Authentication
├── Authorization
├── Policy
├── Consent
├── Approval
├── Risk
├── Evidence
├── Preconditions
└── Temporal validity

Each dimension should retain its own result.

This prevents:

Trust = false

from becoming the only available explanation for why execution cannot proceed.

⸻

48. Trust Evaluation

Conceptually:

EvaluateTrust(
    Intent,
    IntentVersion,
    Actor,
    Context,
    Evidence,
    Policies,
    Authorizations,
    Approvals,
    RiskRules,
    TrustRules
)
→ TrustDecision

The result must be:

* explicit
* structured
* traceable
* versioned
* scoped
* time-aware
* auditable

⸻

49. Trust Provenance

A Trust decision should preserve sufficient provenance to reconstruct why the decision was reached.

Relevant provenance may include:

* Intent ID
* Intent version
* Actor
* authorization source
* policy versions
* approval references
* consent references
* risk evaluation
* evidence references
* Trust rule versions
* evaluation timestamp
* expiry
* evaluator identity
* decision ID

Trust provenance does not require exposing private model reasoning.

⸻

50. Model Output and Trust

An LLM may propose:

Actor is probably authorized.

That statement is not a Trust decision.

Likewise:

confidence = 0.98

does not establish authorization.

Trust-relevant claims must be established through authoritative evidence and deterministic Trust rules.

Therefore:

Model inference
        ≠
Trust evidence

unless explicitly incorporated through an approved Trust mechanism.

⸻

51. Trust and Probabilistic Signals

Probabilistic signals may contribute to risk or investigation.

For example:

fraud_risk_score = 0.87

The score may trigger:

ADDITIONAL_VERIFICATION

or:

HUMAN_REVIEW

But a probabilistic signal must not silently become an unconditional authorization or denial unless the governing policy explicitly defines that behavior.

⸻

52. Trust and Human Review

Human review may be a Trust requirement.

Example:

Risk condition
      ↓
Human Review Required
      ↓
Approved
      ↓
Trust Re-Evaluation

Human review should be represented explicitly.

It should not be conflated with execution failure.

⸻

53. Trust and Clarification

Clarification primarily belongs to Intent resolution.

However, clarification may reveal information required for Trust.

Example:

Intent:
Transfer to John
Clarification:
Which John?
Resolved Intent:
Transfer to John_123
Trust:
Evaluate authorization for John_123

The Trust system must evaluate the resolved semantic object rather than assuming authorization from the clarification itself.

⸻

54. Trust and Action Graph Construction

A candidate Action Graph may be constructed before Trust is complete.

For example:

Intent
   ↓
Candidate Action Graph
   ↓
Trust Evaluation

The graph remains non-executable until applicable Trust requirements are satisfied.

Therefore:

Candidate Graph ≠ Trusted Execution

⸻

55. Trust and Graph Revision

If Trust evaluation introduces additional requirements, the Action Graph may need revision.

Example:

Transfer
   ↓
Risk evaluation
   ↓
Approval required

The resulting graph may become:

Transfer Request
      ↓
Approval
      ↓
Execute Transfer

The Trust requirement establishes the governance condition.

The Action Graph represents the execution dependency.

⸻

56. Trust and Execution

The canonical boundary is:

Intent
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Action Contract
  ↓
Execution

Execution must not occur merely because:

* the model generated an Action
* the Intent is resolved
* the graph is structurally valid
* a capability exists
* a previous Trust decision existed

The applicable Trust requirements must be satisfied for the relevant execution boundary.

⸻

57. Execution-Time Trust Checks

Trust may be evaluated more than once.

For consequential Actions:

Pre-execution Trust
        ↓
Action Contract
        ↓
Execution-time checks
        ↓
Execution

This supports protection against time-of-check/time-of-use conditions.

The later check does not necessarily invalidate the earlier Trust decision; it establishes whether execution remains eligible under current conditions.

⸻

58. Trust and External State

External systems remain authoritative for their business state.

For example:

Account.status = SUSPENDED

may be authoritative in the account system.

Noema may use that state in Trust evaluation.

It should not silently claim ownership of the underlying business state.

⸻

59. Trust and Stale State

Trust decisions may become stale.

Example:

T1:
Authorization = ALLOW
T2:
Authorization revoked
T3:
Old Trust decision reused

The architecture must define freshness and re-evaluation requirements.

A stale Trust decision must not silently authorize execution when current conditions materially differ.

⸻

60. Trust Revocation

A Trust decision may need to be revoked before execution if a governing condition changes.

Examples:

authorization revoked
approval withdrawn
consent withdrawn
policy changed
risk condition changed
evidence invalidated
Intent superseded

Revocation should be explicit and auditable.

⸻

61. Trust Expiration

Trust may expire without explicit revocation.

For example:

Trust valid for 15 minutes

After expiration:

Trust = EXPIRED

The Intent may require re-evaluation before execution.

⸻

62. Trust and Atomicity

Trust must respect the Intent and Action Graph’s atomicity semantics.

If an Intent requires atomic treatment of multiple Actions, satisfying Trust for only one component does not necessarily authorize partial execution.

Example:

A = TRUSTED
B = WAITING_FOR_APPROVAL

If A and B are governed as an atomic unit:

Execute A

must not occur merely because A independently satisfies its Trust conditions.

⸻

63. Trust and Partial Execution

Partial execution must be governed explicitly.

The fact that individual Actions are authorized does not automatically mean that partial execution is permissible.

The applicable semantics must establish whether:

A authorized
B blocked

permits:

A executes

or requires:

entire Intent blocked

⸻

64. Trust and Compensation

Compensating Actions may have their own Trust requirements.

A failure does not automatically authorize arbitrary compensating behavior.

For example:

Payment
   ↓
Failure
   ↓
Refund

The refund Action may require:

* authorization
* policy evaluation
* capability availability
* Action Contract validation
* execution-time checks

Compensation is therefore not an implicit Trust bypass.

⸻

65. Trust and Retry

Retry does not create new authorization automatically.

A retry must respect:

* original Trust scope
* Trust expiry
* authorization validity
* policy changes
* Action Contract semantics
* idempotency
* execution-time conditions

If Trust has expired or materially changed, re-evaluation may be required.

⸻

66. Trust and Unknown Outcomes

An unknown execution outcome does not automatically invalidate Trust.

Example:

Trust = READY
Execute
Network timeout
Outcome = UNKNOWN

The Trust decision may remain historically valid for the attempted execution while the execution outcome remains unresolved.

These are separate dimensions.

⸻

67. Trust and Outcome

Trust describes eligibility.

Outcome describes what happened.

Therefore:

Trust:
READY
Outcome:
FAILED

is valid.

Likewise:

Trust:
READY
Outcome:
UNKNOWN

is valid.

Execution failure does not retroactively mean that the Trust decision was necessarily incorrect.

⸻

68. Trust Taxonomy Categories

The canonical Trust taxonomy may therefore be organized as:

TRUST
│
├── IDENTITY
│   ├── Identity
│   └── Authentication
│
├── AUTHORITY
│   ├── Authorization
│   ├── Delegation
│   └── Ownership / Role
│
├── GOVERNANCE
│   ├── Policy
│   ├── Approval
│   ├── Consent
│   └── Confirmation
│
├── RISK
│   ├── Risk Assessment
│   ├── Risk Conditions
│   └── Additional Controls
│
├── EVIDENCE
│   ├── Evidence
│   ├── Freshness
│   ├── Provenance
│   └── Revocation
│
├── EXECUTION CONDITIONS
│   ├── Preconditions
│   ├── Constraints
│   ├── Temporal Validity
│   └── Execution-Time Checks
│
└── DECISION
    ├── READY
    ├── WAITING
    ├── BLOCKED
    ├── DENIED
    ├── UNKNOWN
    └── EXPIRED

⸻

69. Trust Requirement Hierarchy

Trust requirements may be represented hierarchically.

For example:

Execute Transfer
│
├── Actor Identity
│
├── Authentication
│
├── Authorization
│
├── Policy Compliance
│
├── Risk Requirement
│   └── Additional Verification
│
├── Approval Requirement
│
└── Execution-Time Preconditions

This allows Noema to explain which requirement prevents execution without reducing Trust to a single boolean.

⸻

70. Trust Decision Algebra

Where appropriate, Trust requirements may be composed using explicit logical relationships.

For example:

A AND B

requires both conditions.

A OR B

permits either condition where the governing semantics explicitly allow alternatives.

Example:

Strong Authentication
AND
Authorization
AND
(Approval OR PolicyExemption)

The composition rules must be explicit.

A model must not invent logical relationships between Trust requirements.

⸻

71. Mandatory vs Advisory Conditions

Trust requirements should distinguish:

MANDATORY

from:

ADVISORY

A mandatory condition can block execution.

An advisory signal may inform evaluation without independently determining eligibility.

For example:

Risk score = elevated

may be advisory until policy converts it into:

Additional verification required

⸻

72. Trust Constraints

A Trust decision may include constraints under which execution is permitted.

Examples:

maximum_amount = ₦100,000
valid_until = 18:00
destination = customer_123
capability = payment.transfer

Execution outside those constraints requires new evaluation.

⸻

73. Trust Scope Narrowing

A Trust evaluation may narrow the permissible execution scope.

Example:

Requested:
Transfer ₦500,000
Trust-approved:
Transfer up to ₦100,000

The Action Graph must not execute the broader operation merely because the original Intent requested it.

If the Intent cannot be satisfied within the approved scope, the system must re-evaluate or block execution.

⸻

74. Trust Scope Expansion

Trust must never be expanded implicitly.

If an Intent changes from:

Transfer ₦50,000

to:

Transfer ₦500,000

the earlier Trust decision must not automatically apply.

A material change requires appropriate re-evaluation.

⸻

75. Trust and Resource Scope

Authorization may depend on the specific resource.

For example:

Actor authorized for Account A

does not imply:

Actor authorized for Account B

Trust decisions must preserve resource scope.

⸻

76. Trust and Destination Scope

Destination may be Trust-relevant.

Example:

Actor authorized to transfer funds

does not necessarily mean:

Actor authorized to transfer funds to every destination.

Destination restrictions must remain explicit.

⸻

77. Trust and Amount Scope

Financial or quantitative Actions may require amount-specific Trust evaluation.

Example:

≤ ₦100,000 → no approval
> ₦100,000 → approval required

The Trust taxonomy must permit amount-dependent requirements without collapsing them into generic authorization.

⸻

78. Trust and Temporal Context

Trust requirements may depend on time.

Examples:

authorization valid during business hours
approval valid for 24 hours
session expires after 30 minutes
policy changes at midnight

Temporal conditions must be evaluated explicitly.

⸻

79. Trust and Context

Context may affect Trust.

Relevant context may include:

* Actor role
* device
* location where legitimately available
* session
* organizational environment
* resource state
* transaction characteristics
* time
* policy environment

Context must not become an implicit authority mechanism.

A contextual signal is Trust-relevant only according to explicit rules.

⸻

80. Trust and Location

Where location is relevant to a Trust decision, the location source, precision, freshness, and authority must be explicit.

A model must not infer location merely because a contextual signal appears plausible.

Location evidence must not be treated as authoritative unless the applicable Trust rules establish its authority.

⸻

81. Trust and Security Controls

Security controls may contribute to Trust requirements.

Examples:

multi-factor authentication
device verification
session validation
credential validation
network controls
privilege checks

Security controls are mechanisms supporting Trust.

They are not themselves equivalent to the complete Trust decision.

⸻

82. Trust and Least Privilege

Trust decisions should not grant more authority than necessary for the requested Action.

Conceptually:

Requested scope
      ↓
Required authority
      ↓
Minimum sufficient permission

An Action should not obtain broader authority merely because a capability exposes broader functionality.

⸻

83. Trust and Separation of Duties

Some Actions may require independent parties or systems to satisfy separate governance requirements.

Example:

Requester
    ↓
Creates Transfer
Approver
    ↓
Approves Transfer
Executor
    ↓
Executes Transfer

The Trust taxonomy should preserve these distinct roles.

A requester must not automatically satisfy an independent approval requirement.

⸻

84. Trust and Organizational Governance

Trust may incorporate organizational controls such as:

* approval hierarchy
* spending authority
* role restrictions
* segregation of duties
* departmental boundaries
* delegated authority
* escalation requirements

These controls must be explicit and versioned.

⸻

85. Trust and External Authorization Systems

Noema may depend on external authorization systems.

For example:

Noema
   ↓
Authorization Service
   ↓
ALLOW

The external service may be authoritative for the authorization decision.

Noema should preserve:

* source
* decision
* scope
* timestamp
* expiration
* relevant policy version
* evidence reference

⸻

86. Trust Decision Provenance

A Trust decision should permit reconstruction of:

1. the Intent evaluated
2. the Intent version
3. the Actor
4. the Actions under consideration
5. applicable policies
6. authorization evidence
7. approval evidence
8. consent evidence
9. risk evaluation
10. Trust rules
11. decision
12. decision timestamp
13. decision expiry
14. subsequent revocation or invalidation events

This supports auditability without requiring private model reasoning.

⸻

87. Trust Evaluation Identity

Each Trust evaluation should have an explicit identity.

Conceptually:

trust_evaluation_id

This allows Noema to distinguish:

Intent v7
Trust Evaluation 14

from:

Intent v7
Trust Evaluation 15

after a material environmental change.

⸻

88. Trust Decision Versioning

Where Trust rules materially change, the evaluation should preserve the applicable versions.

Conceptually:

Intent Version: 7
Trust Evaluation: 14
Trust Rules: 5
Policy Set: 17
Authorization Policy: 9

This enables historical reconstruction.

⸻

89. Trust Audit History

Trust-relevant changes should produce an auditable history.

Example:

Trust Evaluation 1
    ↓
READY
Authorization revoked
    ↓
Trust invalidated
Trust Evaluation 2
    ↓
BLOCKED

The historical READY decision should not be overwritten.

⸻

90. Trust Decision Events

Illustrative events include:

trust.evaluation_started
trust.requirement_identified
trust.requirement_satisfied
trust.requirement_failed
trust.requirement_unknown
trust.approval_required
trust.approval_received
trust.approval_revoked
trust.consent_received
trust.consent_withdrawn
trust.authorization_granted
trust.authorization_revoked
trust.policy_changed
trust.risk_escalated
trust.ready
trust.blocked
trust.denied
trust.expired
trust.revoked
trust.re_evaluated

These are architectural events rather than a final protocol.

⸻

91. Trust Failure Semantics

Trust failure should identify the failed dimension.

Examples:

AUTHORIZATION_DENIED
APPROVAL_REQUIRED
CONSENT_MISSING
POLICY_VIOLATION
RISK_CONTROL_REQUIRED
EVIDENCE_UNAVAILABLE
EVIDENCE_EXPIRED
AUTHENTICATION_REQUIRED
AUTHORITY_EXPIRED
PRECONDITION_UNSATISFIED
TRUST_EXPIRED

A generic:

TRUST_FAILED

may exist operationally but should not replace the more specific cause where known.

⸻

92. Trust Unknown Semantics

Unknown Trust conditions must preserve the reason for uncertainty.

Examples:

AUTHORIZATION_UNKNOWN
EVIDENCE_UNKNOWN
RISK_UNKNOWN
POLICY_UNKNOWN
RESOURCE_STATE_UNKNOWN

Unknown must not be silently converted to:

ALLOW

unless an explicit fail-open policy governs that exact condition.

Such a policy itself must be explicit, versioned, and auditable.

⸻

93. Fail-Open and Fail-Closed

Trust architecture must explicitly define the behavior when a Trust dependency is unavailable.

For a mandatory authorization requirement:

Authorization unavailable
        ↓
UNKNOWN
        ↓
BLOCKED

A domain may explicitly define a fail-open behavior for a particular low-risk condition, but such behavior must never be assumed by the model or execution consumer.

The default semantics for consequential authorization should remain explicit rather than implicit.

⸻

94. Trust and Emergency Paths

Emergency or exceptional execution paths may exist.

They must not bypass Trust invisibly.

An emergency path should have explicit:

* authority
* scope
* conditions
* approval requirements
* audit requirements
* expiration
* post-event review

Emergency execution is still governed execution.

⸻

95. Trust and Escalation

When Trust requirements cannot be satisfied automatically, Noema may escalate.

Example:

Risk condition
    ↓
Human Review
    ↓
Approval
    ↓
Trust Re-Evaluation

Escalation does not itself establish Trust.

It creates a path toward satisfying a Trust requirement.

⸻

96. Trust and Durable Execution

Durable execution must preserve Trust state across retries, restarts, delays, and long-running workflows.

For example:

Trust READY
   ↓
WAIT 24 hours
   ↓
Resume

The system must determine whether the Trust decision remains valid.

It must not assume that durable persistence of a Trust decision implies continued validity.

⸻

97. Trust and Long-Running Intents

Long-running Intents may require periodic or event-driven Trust re-evaluation.

Examples:

* approvals expire
* credentials expire
* policies change
* authorization changes
* resource state changes
* risk conditions change

Therefore:

Long-running Intent
        ↓
Trust validity window
        ↓
Re-evaluation when required

⸻

98. Trust and Material Change

A material change must invalidate or trigger re-evaluation of affected Trust decisions.

Material changes include:

* Actor changes
* Intent changes
* Action changes
* resource changes
* amount changes
* destination changes
* authorization changes
* policy changes
* approval changes
* consent changes
* risk changes
* relevant external state changes

The exact invalidation semantics depend on the Trust requirement affected.

⸻

99. Trust and Superseded Intents

When an Intent is superseded:

Intent v1
    ↓
SUPERSEDED
    ↓
Intent v2

Trust associated with v1 must not automatically transfer to v2 if the semantic change is material.

A new Trust evaluation may be required.

⸻

100. Trust and Cancellation

Cancellation terminates the lifecycle of an Intent.

Trust does not override cancellation.

Example:

Intent = RESOLVED
Trust = READY
Actor cancels
Intent = CANCELLED

Execution must respect the cancellation semantics and any already-committed Actions.

⸻

101. Trust and Outcome Reconciliation

Execution may reveal information relevant to Trust after the fact.

For example:

External system:
authorization rejected

The execution outcome may trigger Trust state reconciliation.

However, the system should preserve the distinction between:

Trust decision

and:

execution result

Historical Trust decisions must not be rewritten merely because execution later failed.

⸻

102. Trust and Business State

Trust may depend on external business state.

For example:

Account.status = ACTIVE

may be a prerequisite for execution.

Noema may evaluate that condition while the external system remains authoritative for the state.

If the state changes:

ACTIVE → SUSPENDED

the applicable Trust or execution condition may become unsatisfied.

⸻

103. Trust and TOCTOU

Trust evaluation occurs at a point in time.

Therefore:

Check
  ↓
Time passes
  ↓
Execute

does not guarantee that the conditions remain unchanged.

Consequential Actions should use execution-time checks where required.

This is especially important for:

* authorization
* balances
* ownership
* resource status
* approval
* policy
* risk
* security credentials

⸻

104. Trust Does Not Guarantee Success

The central distinction is:

Trust = permission to proceed

not:

Trust = guaranteed successful execution

Therefore:

Trusted Intent
    ↓
Executable Action
    ↓
External Failure
    ↓
Failed Outcome

is a valid lifecycle.

⸻

105. Canonical Trust Flow

The canonical Trust lifecycle is:

Resolved Intent
       ↓
Validation
       ↓
Trust Requirements
       ↓
Evidence Collection
       ↓
Identity / Authentication
       ↓
Authorization
       ↓
Policy Evaluation
       ↓
Consent / Approval
       ↓
Risk Evaluation
       ↓
Precondition Evaluation
       ↓
Temporal Validation
       ↓
Trust Decision
       │
       ├── READY
       ├── WAITING
       ├── BLOCKED
       ├── DENIED
       ├── UNKNOWN
       └── EXPIRED
       ↓
Action Graph

Not every Intent traverses every branch.

The applicable Trust requirements are determined by the semantics of the Intent and Actions.

⸻

106. Trust Taxonomy and Action Graph

The relationship can be represented as:

Intent
   ↓
Trust Requirements
   ↓
Trust Decision
   ↓
Action Graph
   ↓
Action Contracts
   ↓
Execution

Where Trust requirements introduce execution dependencies:

Transfer
   ↓
Approval Required
   ↓
Approval
   ↓
Execute Transfer

the Trust taxonomy defines the governance concept.

The Action Graph defines the operational dependency.

⸻

107. Trust Taxonomy and Intent Taxonomy

The Intent Taxonomy classifies what the Actor intends.

The Trust Taxonomy classifies the conditions governing whether that Intent may proceed.

Therefore:

Intent Taxonomy
"What is being requested?"
        ↓
Trust Taxonomy
"What conditions govern whether it may proceed?"

The two taxonomies must remain independent.

⸻

108. Trust Taxonomy and Outcome Taxonomy

The Trust Taxonomy describes execution eligibility.

The Outcome Taxonomy describes what occurred.

Therefore:

Trust:
READY
Outcome:
FAILED

or:

Trust:
READY
Outcome:
COMPLETED

are both possible.

The Outcome Taxonomy must not be inferred solely from the Trust decision.

⸻

109. Trust State Must Not Be Reconstructed from Outcome

A successful Outcome does not prove that a Trust decision was correctly represented at the time of execution.

Likewise, a failed Outcome does not prove that Trust was invalid.

Historical Trust and Outcome records must remain independently reconstructible.

⸻

110. Canonical Trust Record

Conceptually:

TrustRecord {
    trust_evaluation_id
    intent_id
    intent_version
    actor
    decision
    requirements
    satisfied_requirements
    unsatisfied_requirements
    unknown_requirements
    evidence
    authorization
    policies
    approvals
    consent
    risk
    constraints
    scope
    valid_from
    valid_until
    rules_version
    provenance
    created_at
}

The exact schema belongs to the Trust architecture.

⸻

111. Trust Decision Determinism

Where Trust rules are deterministic, evaluation should be reproducible from:

Intent
+
Intent version
+
Actor
+
Context
+
Evidence
+
Authorization state
+
Policies
+
Approvals
+
Consent
+
Risk rules
+
Trust rules
+
Versions

Model variability must not silently alter deterministic Trust decisions.

⸻

112. No Hidden Trust

Trust-relevant conditions must not exist only inside model reasoning.

For example:

LLM internally believes:
"this action is probably safe"

does not constitute a Trust record.

Trust-relevant conditions must be explicit, inspectable, and attributable.

⸻

113. No Implicit Authority Escalation

A model, graph, capability, or Action Contract must not obtain additional authority merely by requesting it.

For example:

Model proposes:
TRANSFER_FUNDS

does not establish:

Actor authorized to transfer funds

Likewise:

Action Graph contains:
ADMIN_DELETE

does not grant administrative authority.

Authority must originate from the applicable Trust mechanisms.

⸻

114. Trust and Least Privilege

Trust decisions should establish the minimum authority necessary to satisfy the Intent.

The system should avoid treating broad capability exposure as permission for unrestricted execution.

Conceptually:

Intent scope
      ↓
Required Action scope
      ↓
Minimum sufficient authority

⸻

115. Trust and Auditability

Every consequential Trust decision should be auditable.

An auditor should be able to determine:

What Intent was evaluated?
Which version?
Who was the Actor?
Which Actions were considered?
Which Trust requirements applied?
Which evidence was used?
Which policies applied?
Which approvals existed?
What decision was made?
When was it made?
When did it expire?
Was it later revoked?

This is a core architectural property.

⸻

116. Trust and Privacy

Trust provenance must provide sufficient evidence for accountability without requiring unnecessary disclosure of sensitive information.

The architecture should preserve references to authoritative evidence rather than duplicating sensitive data unnecessarily.

Trust auditability must not become unrestricted data replication.

⸻

117. Trust and Security Boundary

The Trust subsystem is a security and governance boundary.

It must prevent:

* unauthorized execution
* authority escalation
* stale authorization reuse
* approval bypass
* consent bypass
* policy bypass
* model-mediated privilege escalation
* hidden execution authority

Trust must remain independently enforceable from model behavior.

⸻

118. Trust Invariants

Invariant 1

Trust does not define Intent meaning.

Invariant 2

Trust does not execute Actions.

Invariant 3

A valid Intent is not automatically trusted.

Invariant 4

Identity does not imply authorization.

Invariant 5

Authentication does not imply authorization.

Invariant 6

Capability does not imply permission.

Invariant 7

Approval does not automatically imply authorization outside its scope.

Invariant 8

Consent does not automatically establish organizational authorization.

Invariant 9

Unknown Trust conditions must not silently become satisfied.

Invariant 10

Trust decisions must be scoped.

Invariant 11

Trust decisions may expire.

Invariant 12

Trust decisions may be revoked.

Invariant 13

Material Intent changes require appropriate Trust re-evaluation.

Invariant 14

Material policy or authorization changes may require Trust re-evaluation.

Invariant 15

A model-generated confidence value is not a Trust decision.

Invariant 16

Trust must not be inferred from graph structure.

Invariant 17

Trust must not grant capabilities that the Actor is not otherwise authorized to use.

Invariant 18

Trust must preserve relevant provenance.

Invariant 19

Trust state and execution state are separate dimensions.

Invariant 20

Trust readiness does not guarantee execution success.

Invariant 21

Execution failure does not retroactively imply that the Trust decision was invalid.

Invariant 22

Historical Trust decisions must remain reconstructible.

Invariant 23

Partial execution must respect the Trust and atomicity semantics of the Intent.

Invariant 24

Retry does not automatically extend Trust validity.

Invariant 25

Compensation does not automatically inherit execution authority.

Invariant 26

A stale Trust decision must not silently cross an execution boundary when freshness is material.

Invariant 27

Trust requirements must be explicit rather than hidden inside model reasoning.

Invariant 28

Trust must never become a mechanism for semantic mutation of the Actor’s Intent.

⸻

119. Canonical Mental Model

The Trust Taxonomy can be reduced to five questions:

1. Who is acting?
2. What authority permits the requested Action?
3. What policies, approvals, consent, and risk controls apply?
4. What evidence establishes that those conditions are satisfied?
5. Are those conditions still valid for this specific Intent and execution boundary?

Which produces:

Actor
  ↓
Intent
  ↓
Requirements
  ↓
Evidence
  ↓
Trust Evaluation
  ↓
Trust Decision
  ↓
Execution Eligibility

⸻

120. Final Definition

The Trust Taxonomy is Noema’s canonical classification of the identities, authorities, permissions, policies, approvals, consent, risk conditions, evidence, constraints, temporal conditions, and governance requirements that determine whether a resolved and validated Intent may proceed toward execution.

Its central invariant is:

Trust establishes execution eligibility; it does not establish Intent meaning, grant arbitrary authority, define execution structure, or guarantee execution success.

The canonical boundary is:

Interpretation
      ↓
Intent Engine
      ↓
Canonical Intent
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

And the fundamental distinction remains:

Intent
"What does the Actor want?"
Validation
"Is that Intent valid?"
Trust
"May that Intent proceed?"
Action Graph
"How is the permitted objective structurally realized?"
Action Contract
"What does each executable Action permit and require?"
Execution
"What was actually performed?"
Outcome
"What actually happened?"

Noema therefore treats Trust not as a model-generated judgment, confidence score, or opaque authorization heuristic, but as an explicit, scoped, versioned, evidence-backed, and auditable control boundary governing whether an Intent may proceed.