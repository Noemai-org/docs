Trust Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/trust-contract.md

⸻

1. Definition

A Trust Contract is the canonical contract that defines the deterministic conditions, evidence requirements, policy constraints, and decision semantics governing whether a resolved Intent and proposed Action may proceed.

The Trust Contract is the formal boundary between understanding what the user wants and allowing the system to act on it.

⸻

2. Purpose

The Trust Contract exists to ensure that consequential system behavior is governed by explicit, inspectable, and reproducible rules rather than model confidence or implicit application logic.

It establishes:

* what must be known
* what must be verified
* what evidence is sufficient
* what policies apply
* what permissions are required
* what risks are acceptable
* what conditions require clarification
* what conditions require escalation
* what conditions require rejection
* when execution may proceed

⸻

3. Core Question

The Trust Contract answers:

Given this Intent, Context, Evidence, and proposed Action, is Noema permitted to proceed?

The canonical decision is one of:

EXECUTE
CLARIFY
ESCALATE
REJECT

There is no implicit fifth state of:

PROBABLY EXECUTE

⸻

4. Trust Is a Decision Boundary

Trust is not a feeling, score, or general assessment of whether something “looks safe.”

It is a deterministic decision boundary.

Intent
  +
Context
  +
Evidence
  +
Policy
  +
Permissions
  +
Risk
       ↓
Trust Evaluation
       ↓
EXECUTE / CLARIFY / ESCALATE / REJECT

⸻

5. Trust Is Not Model Confidence

Model confidence describes the model’s confidence in its interpretation.

Trust determines whether the resulting operation may proceed.

Model Confidence
      ↓
Interpretation Evidence
Trust Decision
      ↓
Execution Authorization

A model can be highly confident and the Trust Engine can still reject the operation.

A model can be uncertain and the Trust Engine can require clarification.

⸻

6. Trust Is Not Intent

Intent answers:

What does the user want?

Trust answers:

May Noema proceed with this request?

Therefore:

Intent ≠ Trust

A perfectly valid Intent may produce REJECT.

⸻

7. Trust Is Not Authorization Alone

Authorization is one input to trust.

Trust may also depend on:

* identity
* permissions
* evidence
* policy
* ambiguity
* resource scope
* action risk
* temporal constraints
* organizational boundaries
* execution conditions

Therefore:

Authorization ⊂ Trust Evaluation

⸻

8. Trust Is Not Security Alone

Security controls are important inputs to trust but do not fully define it.

Trust encompasses the broader question of whether Noema has enough deterministic basis to allow a particular operation.

This includes semantic certainty and operational conditions in addition to conventional security.

⸻

9. Deterministic Trust

The Trust Engine must be deterministic.

Given the same:

Intent
Context
Evidence
Policy
Permissions
Action
Trust Contract version

the same applicable rules should produce the same decision.

Same Inputs + Same Policy
             ↓
        Same Decision

⸻

10. Probabilistic Interpretation Boundary

The model may be probabilistic.

The Trust Engine may not be.

Natural Language
       ↓
LLM Interpretation
       ↓
Intent
       ↓
Deterministic Trust Engine
       ↓
Decision

This is one of Noema’s foundational architectural boundaries.

⸻

11. Trust Decision

A Trust Decision is the concrete result of evaluating a Trust Contract against a particular Intent and proposed Action.

Conceptually:

Trust Decision
├── decision_id
├── intent_id
├── action_id
├── policy_version
├── contract_version
├── decision
├── reasons
├── evidence
├── evaluated_conditions
├── timestamp
└── provenance

⸻

12. Trust Decision Identity

Every persisted Trust Decision must have a stable unique identifier.

decision_id

This allows the decision to be referenced by:

* Actions
* Executions
* Events
* Audit records
* Recovery processes
* Investigations

⸻

13. Decision Outcomes

The canonical Trust outcomes are:

EXECUTE

The Intent and proposed Action satisfy applicable trust requirements and may proceed.

CLARIFY

Required information is ambiguous, missing, conflicting, or insufficiently established.

ESCALATE

The request requires human or higher-authority review.

REJECT

The request cannot or must not proceed under applicable policy or authority.

⸻

14. EXECUTE

EXECUTE means the Trust Engine has established that the proposed operation satisfies the applicable trust conditions.

It does not mean:

* execution has succeeded
* the enterprise state has changed
* the requested outcome has been achieved

It means the operation is authorized to proceed into execution.

⸻

15. CLARIFY

CLARIFY means Noema cannot safely proceed because a required semantic or contextual uncertainty remains unresolved.

Examples:

ambiguous account
ambiguous customer
missing date range
conflicting target
insufficient identity resolution
unclear requested scope

Clarification is a deterministic outcome, not an LLM retry loop.

⸻

16. ESCALATE

ESCALATE means the operation requires human or higher-level review.

Examples:

policy exception
high-risk operation
insufficient authority
conflicting authoritative evidence
enterprise-specific approval requirement

Escalation preserves the original Intent and Trust evaluation.

⸻

17. REJECT

REJECT means the request must not proceed.

Examples:

unauthorized identity
forbidden operation
policy violation
invalid scope
unsupported operation
insufficient required evidence

A rejection must include an attributable reason.

⸻

18. Trust Inputs

A Trust Evaluation may consume:

Intent
Context
Evidence
Action
Identity
Permissions
Policies
Risk constraints
Temporal constraints
Organizational boundaries
Resource state
Contract versions

Only inputs within their authoritative scope should be treated as authoritative.

⸻

19. Trust Evidence

Evidence is information used to establish whether trust conditions are satisfied.

Evidence may include:

* authenticated identity
* enterprise records
* permissions
* policy configuration
* canonical data
* prior verified state
* explicit user confirmation
* execution history
* provider responses

Evidence must retain provenance and authority.

⸻

20. Evidence Authority

Trust must evaluate evidence according to authority, not merely quantity.

For example:

One authoritative enterprise record
        >
Multiple stale or unofficial records

More evidence does not necessarily mean better evidence.

⸻

21. Evidence Freshness

Evidence may become stale.

Trust evaluation should consider:

* timestamp
* validity interval
* freshness requirements
* source authority
* action risk

A previously valid fact may no longer satisfy a current trust condition.

⸻

22. Evidence Conflict

Conflicting evidence must be represented explicitly.

For example:

Source A → account ACTIVE
Source B → account CLOSED

Trust must not silently select one merely because it appears more likely.

The applicable authority hierarchy must determine the result.

If the conflict cannot be deterministically resolved, the outcome may be:

CLARIFY
ESCALATE
REJECT

depending on policy.

⸻

23. Trust Policy

Trust decisions must be governed by explicit policy.

Policy may define:

* permitted actions
* required permissions
* evidence thresholds
* risk thresholds
* clarification requirements
* escalation conditions
* approval requirements
* temporal constraints
* organizational restrictions

Policy must be versioned.

⸻

24. Policy Version

Every consequential Trust Decision should reference the policy version under which it was evaluated.

policy_version

This ensures that historical decisions remain explainable even after policy changes.

⸻

25. Trust Preconditions

A Trust Contract may define preconditions that must hold before EXECUTE is possible.

Examples:

identity resolved
target resolved
required permissions present
required evidence available
action supported
policy satisfied
risk threshold satisfied
scope valid

A failed precondition must produce the appropriate deterministic outcome.

⸻

26. Trust Postconditions

A Trust Decision should establish what the decision guarantees.

For EXECUTE:

The Action may proceed.

It does not guarantee:

execution success
provider availability
business-state change
requested outcome

Those are determined later.

⸻

27. Trust and Identity

Identity must be sufficiently established before a trust decision can authorize operations that depend on identity.

For example:

"Show my balance."

may have a perfectly clear semantic interpretation while the identity of “my” remains unresolved.

Trust cannot convert semantic clarity into identity certainty.

⸻

28. Trust and Scope

Trust decisions must respect scope.

Scope may include:

* tenant
* organization
* legal entity
* customer
* account
* resource
* environment
* channel

An operation that is valid in one scope may be invalid in another.

⸻

29. Trust and Permissions

Permissions determine whether an identity is permitted to perform or access a particular operation.

Trust must verify applicable permissions according to authoritative enterprise policy.

Noema cannot manufacture permissions through intent interpretation.

⸻

30. Trust and Context

Context provides information required to evaluate trust.

For example:

Intent:
Retrieve statement
Context:
customer identity
account
date range
tenant
channel
permissions

Trust evaluates whether the resulting request satisfies policy.

Context is evidence for evaluation; it is not itself a trust decision.

⸻

31. Trust and Canonical Data

Canonical Data may provide authoritative facts required for trust evaluation.

For example:

Canonical Data:
customer owns account

may support:

target account resolution

The enterprise system remains authoritative for the underlying business fact.

⸻

32. Trust and Action

Trust evaluates a specific proposed Action.

Therefore:

Intent
  ↓
Action
  ↓
Trust Evaluation

or, where policy requires trust before final action selection:

Intent
  ↓
Trust Constraints
  ↓
Action
  ↓
Final Trust Evaluation

The exact pipeline may vary by workflow, but consequential execution must have an explicit trust decision.

⸻

33. Trust and Execution

Trust authorizes an execution path.

It does not perform execution.

Trust
  ↓
Authorization
  ↓
Execution

Execution must verify that the applicable Trust Decision is valid for the Action being executed.

⸻

34. Trust and Events

Trust Decisions produce events that communicate what happened.

For example:

TrustEvaluated
TrustApproved
TrustClarificationRequired
TrustEscalated
TrustRejected

Events record occurrences.

They do not independently grant authorization.

⸻

35. Trust and Outcomes

Trust evaluates whether an operation may proceed.

Outcome evaluation determines what actually happened.

Trust:
EXECUTE
Execution:
COMPLETED
Outcome:
VERIFIED

These are separate states.

EXECUTE must never be interpreted as SUCCESS.

⸻

36. Trust and Unknown

Trust must be capable of handling uncertainty explicitly.

For example:

Required evidence:
UNKNOWN

may prevent EXECUTE.

The Trust Engine should not manufacture certainty to satisfy a binary decision requirement.

The appropriate result may be:

CLARIFY
ESCALATE
REJECT

depending on the source of uncertainty and policy.

⸻

37. Trust and Ambiguity

Material ambiguity is a trust concern because ambiguous execution targets can produce unintended consequences.

For example:

Two accounts match the user's request.

Even if the model strongly prefers one account, Trust may require:

CLARIFY

The ambiguity itself becomes an explicit execution constraint.

⸻

38. Trust and Risk

Trust evaluation may classify actions according to risk.

Conceptually:

Low Risk
→ lower verification requirements
Higher Risk
→ stronger evidence / confirmation
High Risk
→ escalation or rejection

Risk policy must be explicit and versioned.

⸻

39. Trust and Read Operations

Phase 1 read-oriented operations still require trust evaluation.

Examples include:

balance inquiry
statement retrieval
transaction search
spending summary
complaint logging

Trust is not limited to money-moving operations.

Even read access can involve identity, privacy, permissions, and organizational boundaries.

⸻

40. Trust and Human Confirmation

Some operations may require explicit user confirmation before execution.

For example:

Intent
  ↓
Trust Evaluation
  ↓
CONFIRMATION_REQUIRED
  ↓
User Confirmation
  ↓
Trust Re-evaluation
  ↓
EXECUTE

If confirmation is required by policy, model confidence cannot substitute for it.

⸻

41. Trust and Clarification

Clarification and confirmation are distinct.

Clarification resolves uncertainty about what the user means.

Confirmation establishes explicit user approval where policy requires it.

Clarification:
"What account do you mean?"
Confirmation:
"Do you want me to proceed?"

They must not be conflated.

⸻

42. Trust and Human Escalation

Escalation is required when deterministic rules establish that automated execution should not continue.

The escalation record should preserve:

* Intent
* Context
* Evidence
* proposed Action
* Trust Decision
* policy
* reason
* required reviewer
* timestamp

The human should not have to reconstruct the request from raw logs.

⸻

43. Trust Decision Reasons

Every non-trivial Trust Decision should include machine-readable reasons.

Examples:

AMBIGUOUS_TARGET
MISSING_PERMISSION
INSUFFICIENT_EVIDENCE
POLICY_VIOLATION
HIGH_RISK
IDENTITY_UNRESOLVED
SCOPE_CONFLICT

Human-readable explanations may be generated from these canonical reasons.

⸻

44. Trust Decision Explainability

A Trust Decision must be explainable in terms of deterministic inputs and rules.

For example:

Decision:
REJECT
Reason:
MISSING_PERMISSION
Policy:
customer-data-read-v3
Evidence:
permission set P-4821
Evaluated:
2026-08-23T10:15:00Z

“Model wasn’t confident” is not an adequate Trust explanation.

⸻

45. Trust Auditability

A consequential Trust Decision should be reconstructable.

The audit trail should establish:

what was evaluated
which Intent was evaluated
which Action was evaluated
what Context was used
what Evidence was considered
which policy applied
which contract version applied
what decision resulted
why it resulted

⸻

46. Trust Immutability

Once a Trust Decision has authorized or rejected a consequential operation, the historical decision must remain immutable or reconstructable.

If policy changes later:

Old decision
≠
new policy evaluation

Historical execution must retain its original decision lineage.

⸻

47. Trust Re-evaluation

A Trust Decision may require re-evaluation when relevant conditions change.

Examples:

* permissions change
* evidence expires
* policy changes
* context changes
* Action changes
* target changes
* significant time passes

A previous EXECUTE decision must not automatically remain valid forever.

⸻

48. Trust Expiration

Some Trust Decisions should have an explicit validity window.

Conceptually:

EXECUTE
   │
   ├── valid_from
   └── valid_until

After expiration, Noema must re-evaluate rather than assume the original authorization remains valid.

⸻

49. Trust and Time

Time may affect trust.

Examples:

business hours
temporary permissions
session expiration
evidence freshness
policy effective dates
approval validity

Trust evaluation must use explicit temporal semantics where applicable.

⸻

50. Trust and Organizational Policy

Enterprise-specific policy may determine whether an operation can proceed.

For example:

Organization A:
automatic execution permitted
Organization B:
human approval required

The Trust Contract must support policy variation without changing the underlying semantic meaning of Intent or Action.

⸻

51. Trust and Environment

Trust decisions must distinguish environments where applicable.

development
staging
production

A decision valid in staging must not automatically authorize an equivalent operation in production.

⸻

52. Trust and Tenant Isolation

Trust evaluation must respect tenant boundaries.

Evidence, permissions, policies, and context from one tenant must not silently influence a decision for another tenant.

Tenant A Context
       ≠
Tenant B Context

unless an explicit cross-tenant authority relationship exists.

⸻

53. Trust and Provider Boundaries

Trust should be evaluated against canonical Noema semantics rather than provider-specific behavior.

For example:

Canonical Action
      ↓
Trust
      ↓
Provider Adapter

The integration provider cannot redefine whether the user is trusted.

⸻

54. Trust and Integration Failure

Integration availability is not necessarily a Trust Decision.

For example:

Trust:
EXECUTE
Integration:
UNAVAILABLE

The correct state is an execution or integration failure, not a retroactive trust rejection.

This preserves causal boundaries.

⸻

55. Trust and Recovery

Trust conditions may need to be re-evaluated during recovery.

For example:

Execution fails
      ↓
Retry requested
      ↓
Trust conditions re-evaluated
      ↓
Retry allowed / blocked

Recovery must not blindly inherit an authorization if the relevant conditions have changed.

⸻

56. Trust and Reconciliation

Reconciliation establishes external business state after uncertain execution.

It does not replace the original Trust Decision.

Trust
  ↓
EXECUTE
  ↓
Execution
  ↓
UNKNOWN
  ↓
Reconciliation

Trust determines whether the action was permitted.

Reconciliation determines what happened.

⸻

57. Trust and Compensation

If a workflow requires compensation after partial execution, the compensating Action must be evaluated under its own applicable trust requirements.

Authorization for the original Action does not automatically authorize unrelated compensating operations.

⸻

58. Trust and Contract Versioning

A Trust Decision should reference:

Trust Contract version
Policy version
Intent Contract version
Action Contract version

where applicable.

This enables deterministic historical reconstruction.

⸻

59. Trust Decision Lifecycle

The conceptual lifecycle is:

INPUTS COLLECTED
      ↓
VALIDATE
      ↓
EVALUATE POLICY
      ↓
EVALUATE EVIDENCE
      ↓
EVALUATE PERMISSIONS
      ↓
EVALUATE RISK
      ↓
EVALUATE AMBIGUITY
      ↓
DECIDE
      ↓
EXECUTE / CLARIFY / ESCALATE / REJECT

The evaluation itself must be deterministic.

⸻

60. Trust Evaluation Model

Conceptually:

┌─────────────────────────────────────┐
│          Trust Evaluation           │
├─────────────────────────────────────┤
│ Intent                              │
│ Context                             │
│ Evidence                            │
│ Identity                            │
│ Permissions                        │
│ Policy                              │
│ Action                              │
│ Risk                                │
│ Temporal Constraints                │
│ Organizational Scope               │
│ Contract Versions                   │
└──────────────────┬──────────────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Deterministic   │
          │ Trust Engine     │
          └────────┬────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
   EXECUTE      CLARIFY     ESCALATE
                   │
                   └────────────── REJECT

⸻

61. Trust Contract Data Model

A conceptual Trust Decision may be represented as:

TrustDecision {
    decision_id
    intent_id
    action_id
    decision
    policy_version
    contract_version
    identity
    scope
    evaluated_conditions
    evidence_refs
    permission_refs
    risk_class
    reasons
    valid_from
    valid_until
    created_at
}

The implementation may vary, but the semantic fields must remain explicit.

⸻

62. Trust and Deterministic Policy Evaluation

Trust policy should be represented in a form that can be evaluated consistently.

The system should avoid decisions based on opaque instructions such as:

"Use your judgment."

Instead, policies should express explicit conditions and outcomes.

For example:

IF identity_unresolved
THEN CLARIFY
IF required_permission_missing
THEN REJECT
IF high_risk AND approval_required
THEN ESCALATE
IF all_required_conditions_satisfied
THEN EXECUTE

⸻

63. Trust Decision Precedence

Where multiple conditions apply, policy must define deterministic precedence.

For example:

REJECT
   >
ESCALATE
   >
CLARIFY
   >
EXECUTE

The exact precedence may vary by policy.

What must not vary is the existence of an explicit precedence rule.

⸻

64. Trust Does Not Guess

Trust must never fill missing information merely because a likely value exists.

For example:

Two accounts match.
Model:
Account A = 91%
Account B = 9%

The Trust Engine does not convert this into:

EXECUTE Account A

if policy requires unambiguous target resolution.

It produces:

CLARIFY

or another policy-defined outcome.

⸻

65. Trust Is the Enforcement Boundary

The Trust Engine is where Noema turns semantic understanding into an enforceable decision.

Probabilistic Model
        ↓
Intent
        ↓
Context
        ↓
┌──────────────────────────────┐
│       TRUST BOUNDARY         │
│                              │
│ deterministic enforcement    │
└──────────────┬───────────────┘
               ↓
           Action / Stop

No consequential execution should bypass this boundary.

⸻

66. Trust and the Enterprise System of Record

Trust may consume enterprise-authoritative information.

It must not replace that authority.

For example:

Enterprise:
authoritative permission state
Noema:
Trust Decision

Noema records the decision it made.

The enterprise remains authoritative for the underlying permission or business fact.

⸻

67. Trust and Noema State of Record

Noema may be authoritative for:

* Trust Decisions
* trust evaluation history
* policy references
* decision reasons
* trust lifecycle state

This is execution-domain state owned by Noema.

⸻

68. Trust Observability

Trust evaluation should expose operational metrics such as:

* decision latency
* decision distribution
* clarification rate
* rejection rate
* escalation rate
* execution authorization rate
* policy failure rate
* evidence failure rate
* permission failure rate

These metrics should help identify both product and policy problems.

⸻

69. Trust Safety Boundary

The Trust Contract is a safety boundary against:

* ambiguous execution
* unauthorized access
* policy violations
* invalid scope
* insufficient evidence
* stale authorization
* accidental cross-tenant execution
* model overreach
* integration misuse

It is therefore a core component of Noema’s trust architecture rather than a secondary validation layer.

⸻

70. Trust Contract Invariants

Invariant 1

Trust evaluation is deterministic.

Invariant 2

Model confidence does not independently authorize execution.

Invariant 3

Every consequential Trust Decision has a stable identity.

Invariant 4

Every Trust Decision has an explicit outcome.

Invariant 5

The canonical outcomes are EXECUTE, CLARIFY, ESCALATE, and REJECT.

Invariant 6

EXECUTE means authorized to proceed, not successfully executed.

Invariant 7

CLARIFY represents unresolved material uncertainty.

Invariant 8

ESCALATE represents a policy-defined requirement for human or higher-authority review.

Invariant 9

REJECT prevents the proposed operation from proceeding.

Invariant 10

Trust does not redefine Intent.

Invariant 11

Trust does not perform Execution.

Invariant 12

Trust does not establish enterprise business outcomes.

Invariant 13

Identity must satisfy applicable requirements before execution may be authorized.

Invariant 14

Permissions must be evaluated against authoritative enterprise policy.

Invariant 15

Trust decisions must respect tenant and organizational boundaries.

Invariant 16

Material ambiguity must not be silently resolved through probabilistic guessing.

Invariant 17

Evidence authority must be evaluated explicitly.

Invariant 18

Evidence freshness must be considered where required.

Invariant 19

Conflicting authoritative evidence must not be silently collapsed.

Invariant 20

Trust policy must be explicit and versioned.

Invariant 21

Consequential Trust Decisions must retain policy lineage.

Invariant 22

Trust Decisions must be explainable through evaluated conditions and reasons.

Invariant 23

Historical Trust Decisions must remain reconstructable.

Invariant 24

Trust Decisions may require re-evaluation when relevant conditions change.

Invariant 25

Expired Trust Decisions must not be treated as permanently valid.

Invariant 26

A change in integration availability must not retroactively change a Trust Decision.

Invariant 27

Recovery may require Trust re-evaluation.

Invariant 28

Reconciliation determines external outcome and does not replace Trust authorization.

Invariant 29

Compensating operations require their own applicable trust evaluation.

Invariant 30

Trust must remain independent of provider-specific integration semantics.

Invariant 31

No consequential execution may bypass the Trust enforcement boundary.

Invariant 32

Trust uncertainty must remain explicitly representable.

Invariant 33

Trust decisions must preserve provenance.

Invariant 34

Trust state must remain distinct from enterprise business state.

Invariant 35

Trust policy precedence must be deterministic.

Invariant 36

Human confirmation cannot be replaced by model confidence when policy requires explicit confirmation.

Invariant 37

Trust decisions must preserve the distinction between clarification and escalation.

Invariant 38

Noema owns Trust Decision state within its execution domain.

Invariant 39

Enterprise systems remain authoritative for enterprise permissions and business facts.

Invariant 40

The Trust Contract must never authorize an operation solely because the model believes it is probably correct.

⸻

71. Final Definition

The Trust Contract is Noema’s canonical definition of the deterministic boundary that decides whether a resolved Intent and proposed Action may proceed.

It evaluates:

Intent
+
Context
+
Evidence
+
Identity
+
Permissions
+
Policy
+
Risk
+
Scope
+
Temporal Constraints
+
Action

and produces one of four canonical outcomes:

EXECUTE
CLARIFY
ESCALATE
REJECT

The Trust Contract exists because understanding a user’s intent is not equivalent to having permission to act on it.

Its governing principle is:

The model may interpret probabilistically; Noema must decide trust deterministically.

Trust therefore forms the enforcement boundary between what the system believes the user means and what the system is permitted to do.

Noema must never replace unresolved ambiguity with probabilistic confidence, never treat authorization as equivalent to successful execution, and never allow a model’s confidence to become execution authority.

Trust is the deterministic decision that makes execution permissible—not the execution itself, and not a prediction that execution will probably be safe.