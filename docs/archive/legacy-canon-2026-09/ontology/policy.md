> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Policy

Status: Foundational Draft
Version: 0.2
Domain: Ontology
Canonical Path: ontology/policy.md

⸻

1. Definition

A Policy is a governing rule that determines what is permitted, required, prohibited, or conditionally permitted within a defined scope.

A Policy expresses organizational, regulatory, operational, or system-level governance.

It answers:

Under what governing rules may this Intent or Action proceed?

A Policy is distinct from:

* Intent
* Constraint
* Authority
* Trust
* Action
* Enforcement
* Outcome

The fundamental relationship is:

Policy
   +
Authority
   +
Constraint
   +
Context
   +
Evidence
   ↓
Policy Evaluation
   ↓
Trust Decision
   ↓
Action

A Policy is an input to governance evaluation. It is not itself the resulting authorization or trust decision.

⸻

2. Policy’s Role in Noema

Policy establishes governing rules against which an Intent, Action, or resulting process may be evaluated.

Conceptually:

Intent
   │
   ▼
Applicable Policies
   │
   ▼
Policy Evaluation
   │
   ├── PERMIT
   ├── DENY
   ├── REQUIRE
   └── UNKNOWN

Policy therefore participates in the deterministic decision boundary before consequential execution.

Policy may:

* permit an operation;
* prohibit an operation;
* require additional conditions;
* impose restrictions;
* establish preconditions;
* govern handling of Outcomes.

Policy does not itself execute an Action.

⸻

3. Policy Is Not Intent

Intent represents what an Actor wants.

Policy represents what the governing environment permits, prohibits, or requires.

Example:

Intent:
Refund this customer.
Policy:
Refunds above $10,000 require manager approval.

The Policy does not change the Actor’s Intent.

It determines the conditions under which that Intent may be fulfilled.

Therefore:

Intent ≠ Policy

⸻

4. Policy Is Not Constraint

Policy and Constraint are related but distinct.

A Constraint is a condition limiting a particular Intent, Action, or operation.

A Policy is a governing rule that may establish or require such conditions.

Example:

Policy:
Refunds above $10,000 require manager approval.
Derived Constraint:
refund.amount <= 10000

The Policy is the governing rule.

The Constraint is the concrete condition applied to the current operation.

Not every Constraint must originate from a Policy.

A Constraint may also originate from:

* Actor preferences;
* Intent requirements;
* system capabilities;
* resource limitations;
* Context;
* technical requirements.

Therefore:

Policy → may produce Constraint
Policy ≠ Constraint

⸻

5. Policy Is Not Authority

Authority answers:

Who is permitted to perform an operation, within what scope?

Policy answers:

What governing rules determine whether the operation may occur?

Example:

Actor:
Support Agent
Authority:
May issue refunds.
Policy:
Refunds above $10,000 require manager approval.

An Actor may possess Authority to issue refunds while still being unable to perform a particular refund without satisfying additional Policy requirements.

Therefore:

Authority ≠ Policy

⸻

6. Policy Is Not Trust

Trust is Noema’s determination of whether an Intent or Action may proceed given the applicable facts, rules, Authority, Constraints, Context, and Evidence.

Conceptually:

Policy
   +
Authority
   +
Constraints
   +
Context
   +
Evidence
   ↓
Trust Decision

Therefore:

Policy ≠ Trust

A Policy is a governing input.

Trust is the resulting decision.

⸻

7. Policy Is Not Enforcement

Policy evaluation and Policy enforcement are separate concerns.

Policy
   ↓
Policy Evaluation
   ↓
Decision
   ↓
Enforcement

Example:

Policy Evaluation:
DENY
Enforcement:
Do not execute Action.

The Policy system determines what the governing rules say.

The runtime enforces the resulting decision.

⸻

8. Policy Scope

Every Policy should have a defined scope.

Possible scopes include:

* Organization
* Department
* Role
* Actor
* Entity
* Capability
* Action
* Intent
* Resource
* Environment
* Geography
* Time

Example:

Policy:
Finance employees may approve expenses up to $25,000.
Scope:
Department = Finance

Scope determines the domain within which the Policy may be applicable.

⸻

9. Policy Subject

A Policy applies to one or more subjects.

Possible subjects include:

* Actor
* Role
* Organization
* Capability
* Action
* Entity
* Intent
* Resource

Example:

Policy:
Managers may approve expenses above $10,000.
Subject:
Role = Manager

Subject and scope should remain separately representable because they answer different questions.

⸻

10. Policy Effect

A Policy should produce an explicit semantic effect.

Foundational effects are:

ALLOW
DENY
REQUIRE
RESTRICT

Examples:

ALLOW:
Manager may approve expense.
DENY:
Intern may not approve expense.
REQUIRE:
Expense above $10,000 requires approval.
RESTRICT:
Only company-issued cards may be used.

Additional effects may be introduced as the Policy model matures.

⸻

11. Conditional Policies

Policies may be conditional.

Example:

IF
  amount > 10000
THEN
  manager approval required

Another example:

IF
  actor.role = "finance_manager"
AND
  amount <= 25000
THEN
  approval permitted

Policy conditions must be evaluated against explicit Context and Evidence.

A condition should not be satisfied merely because a Model considers it likely to be true.

⸻

12. Policy Conditions

A Policy may contain one or more conditions.

Conceptually:

Policy
├── Scope
├── Subject
├── Conditions
├── Effect
└── Requirements

Conditions may reference:

* Actor
* Entity
* Intent
* Action
* Context
* State
* Time
* Authority
* Evidence

Conditions describe the facts under which the Policy applies or produces its effect.

⸻

13. Policy Requirements

A Policy may impose requirements rather than simply allow or deny.

Example:

Policy:
International transfers above $10,000 require enhanced verification.

The Policy does not necessarily prohibit the transfer.

Instead:

Transfer
   ↓
Requirement:
Enhanced Verification
   ↓
Verification
   ↓
Continue Evaluation

This distinction allows Policy to express conditional permission without collapsing every unmet condition into permanent denial.

⸻

14. Policy Preconditions

A Policy may establish preconditions that must be satisfied before an Intent or Action may proceed.

Example:

Policy:
A customer must complete KYC before withdrawing funds.
Precondition:
KYC = VERIFIED

If the precondition is not satisfied, the resulting Policy evaluation may be:

DENY

or, where the Trust model distinguishes unresolved requirements:

REQUIRE_VERIFICATION

The exact Trust-state vocabulary belongs to the Trust specification.

⸻

15. Policy and Constraints

Policies frequently establish or derive Constraints.

Example:

Policy:
Employees may spend no more than $5,000 without approval.
Derived Constraint:
expense.amount <= 5000

Conceptually:

Policy
   ↓
Constraint
   ↓
Evaluation

However, this relationship is not universal.

A Constraint may exist independently of any Policy.

⸻

16. Policy Hierarchy

Organizations may have multiple Policies operating at different scopes.

Example:

Global Policy
      ↓
Organization Policy
      ↓
Department Policy
      ↓
Role Policy
      ↓
Resource Policy
      ↓
Action-specific Policy

More specific Policies may refine broader Policies.

However, Noema must not assume that specificity automatically determines precedence.

Conflict resolution must be explicit.

⸻

17. Policy Precedence

When Policies conflict, Noema must not silently select one.

Example:

Policy A:
Managers may approve up to $50,000.
Policy B:
This department limits approval to $25,000.

The applicable Policy set must be evaluated according to explicit precedence rules.

Potential precedence dimensions include:

* Authority
* Scope
* Specificity
* Priority
* Jurisdiction
* Temporal validity
* Policy version

The canonical precedence algorithm belongs in the Policy/Trust evaluation specification rather than this ontology definition.

⸻

18. Policy Applicability

Not every Policy applies to every Intent or Action.

Noema must first determine:

Is this Policy applicable?

before determining:

What does this Policy require or permit?

Conceptually:

Policy Set
    ↓
Applicability Evaluation
    ↓
Applicable Policies
    ↓
Policy Evaluation
    ↓
Decision Inputs

Applicability must be based on explicit semantic facts.

⸻

19. Policy Evaluation

Policy Evaluation determines the effects of applicable Policies under the current Context.

Conceptually:

Intent
   +
Actor
   +
Entity
   +
Context
   +
Applicable Policies
   +
Evidence
   ↓
Policy Evaluation

Policy Evaluation should be deterministic.

The same Policy version evaluated against the same relevant facts and evaluation rules should produce the same result.

⸻

20. Policy Evaluation Must Be Deterministic

The Trust Engine should not ask a Model:

“Does this seem allowed?”

Instead, the Model may help identify structured facts.

Example:

Model:
Actor appears to be requesting a refund.

Noema can then evaluate:

refund.amount <= policy.limit

using deterministic rules.

The Model may contribute interpretation.

The Policy evaluator remains authoritative for Policy evaluation.

⸻

21. Policy and Model Reasoning

The Model may assist with:

* interpretation;
* classification;
* extraction;
* entity resolution;
* candidate Intent generation;
* Policy interpretation during Policy authoring.

The Model should not become the authoritative runtime Policy evaluator.

The boundary is:

Model
   ↓
Structured Facts
   ↓
Policy Engine
   ↓
Deterministic Evaluation

This preserves a deterministic governance boundary between probabilistic interpretation and consequential execution.

⸻

22. Policy and Natural Language

Policies may originate as natural-language documents.

Example:

Expenses above $10,000 require director approval.

However, consequential runtime evaluation should ultimately operate on a canonical Policy representation.

Conceptually:

Natural-Language Policy
        ↓
Policy Interpretation
        ↓
Canonical Policy
        ↓
Executable Policy Representation
        ↓
Deterministic Evaluation

The canonical representation is the authoritative semantic representation used for execution decisions.

⸻

23. Policy Compilation

Noema may eventually support compiling Policies into executable representations.

Example:

Human Policy
     ↓
Canonical Policy
     ↓
Policy AST / Rule Representation
     ↓
Policy Evaluator

This can make Policies:

* versionable;
* testable;
* simulatable;
* auditable;
* reproducible.

The compilation mechanism belongs to implementation rather than the ontology itself.

⸻

24. Policy as Data

Policies should be represented as structured domain objects rather than hidden application logic.

Conceptually:

Policy
├── id
├── version
├── scope
├── subject
├── conditions
├── effect
├── requirements
├── priority
├── jurisdiction
├── effective_period
├── provenance
└── status

The eventual serialization schema may evolve without changing the underlying semantic distinctions.

⸻

25. Policy Identification

Policies should have stable identities.

Example:

policy.customer.deletion.legal_hold

Stable identity enables:

* auditing;
* versioning;
* references;
* testing;
* evaluation;
* decision explanation.

A Policy identity should remain distinct from its version.

⸻

26. Policy Versioning

Policies evolve.

Example:

Policy:
expense.approval.limit
v1:
$10,000
v2:
$25,000

A Policy evaluation must identify the applicable Policy version.

Historical decisions must not be retroactively reinterpreted using a newer version.

Therefore:

Published Policy Version
        ↓
Immutable Historical Reference

⸻

27. Policy Effective Time

A Policy may have temporal validity.

Conceptually:

effective_from
effective_until

Example:

Policy v2
Effective:
2026-09-01

An Action performed on:

2026-08-31

must not be evaluated using a Policy version that becomes effective on September 1.

Temporal applicability is therefore part of Policy evaluation.

⸻

28. Policy Jurisdiction

Policies may apply within a defined jurisdiction.

Examples include:

* Country
* State
* Organization
* Business Unit
* Data Region
* Regulatory Domain

Example:

Policy:
Data may only be exported to approved regions.

The applicable jurisdiction must be determined from relevant Context and Entity information.

⸻

29. Explicit Denial

A Policy denial should be represented explicitly.

Example:

Intent:
Delete customer account.
Policy:
Customer records cannot be permanently deleted while
an active legal hold exists.
Result:
DENY

The resulting Policy Decision should retain the Policy responsible for the denial.

⸻

30. Policy Explanation

Consequential Policy decisions should be explainable.

Noema should be able to answer:

Which Policy caused this operation to be permitted, denied, or conditionally permitted?

Example:

Decision:
DENY
Policy:
customer.legal_hold.deletion
Reason:
Active legal hold exists.

The canonical explanation should reference Policy identifiers and evaluated conditions rather than relying solely on generated natural-language explanations.

⸻

31. Policy Provenance

Noema should know where a Policy originated.

Possible sources include:

* Organization
* Regulation
* Contract
* Administrator
* System Configuration
* Security Standard
* Operational Rule

Example:

Policy:
expense.approval.limit
Source:
Finance Governance Document
Version:
2026.3

Policy provenance supports governance, auditability, and reproducibility.

⸻

32. Policy Authority

A Policy must have an authoritative source.

Not every statement that resembles a rule should become a canonical Policy.

For example:

"John usually approves refunds."

is not necessarily a Policy.

Whereas:

"Refunds above $10,000 require Finance Manager approval."

may constitute a Policy when established by an authoritative governance source.

⸻

33. Policy Provenance vs Policy Authority

These concepts are related but distinct.

Provenance:

Where did this Policy come from?

Authority:

Why is this source authorized to establish this Policy?

Example:

Provenance:
Finance Department Policy Manual
Authority:
Chief Financial Officer

Both may be required to establish the legitimacy and traceability of a Policy.

⸻

34. Policy Conflicts

Policies may conflict.

Example:

Policy A:
Managers may approve up to $50,000.
Policy B:
International payments are limited to $10,000.
Intent:
International payment of $30,000.

Noema must identify the applicable conflict and resolve it according to explicit canonical rules.

It must not allow a Model to choose whichever Policy appears more relevant.

If the available information is insufficient to establish the applicable rule, the uncertainty must remain explicit.

⸻

35. Policy Exceptions

Policies may permit explicit exceptions.

Example:

Policy:
Refunds above $10,000 require Director approval.
Exception:
Emergency incidents may bypass the normal approval workflow.

Exceptions must themselves be explicitly represented.

An exception should not silently override the Policy.

⸻

36. Policy Delegation

Policy authority may be delegated.

Example:

Organization
     ↓
Finance Department
     ↓
Finance Manager

Delegated Policy authority should remain traceable.

The ontology should preserve the distinction between:

* the Policy;
* the source establishing the Policy;
* the authority establishing or delegating that Policy;
* the runtime decision produced from the Policy.

⸻

37. Policy and Actor

Policies may apply differently depending on Actor characteristics.

Example:

Policy:
Employees may approve expenses up to $5,000.
Policy:
Managers may approve expenses up to $25,000.

Actor information therefore participates in Policy applicability and evaluation.

Actor attributes used by a Policy should be established through appropriate Context and Evidence.

⸻

38. Policy and Capability

A Capability describes what a system, service, tool, or Actor can do.

A Policy describes the governing conditions under which something may be done.

Example:

Capability:
delete.customer
Policy:
Customer deletion is prohibited while legal hold is active.

Therefore:

Capability ≠ Permission

A system being capable of performing an operation does not make that operation permissible.

⸻

39. Policy and Action

Policies may apply directly to Actions.

Example:

Action:
DeleteCustomer(customer_123)
Policy:
Deletion requires verified identity.

The Action may be structurally valid while remaining ineligible for execution until the Policy requirement is satisfied.

⸻

40. Policy and Intent

Policies may also apply at the Intent level.

Example:

Intent:
Export customer data.
Policy:
Customer data export requires a legitimate business purpose.

This allows Noema to determine that an Intent cannot proceed before constructing an Action when the governing rules make that determination possible at the Intent level.

⸻

41. Policy and Outcome

Policies may govern how Outcomes are handled after execution.

Example:

Policy:
Failed financial transactions must be reconciled within 24 hours.
Outcome:
Transfer Failed
Policy Requirement:
Reconciliation Required
Derived Action:
ReconcileTransfer

Policy therefore need not terminate at the Action boundary.

It may govern post-execution requirements as well.

⸻

42. Policy and Compliance

Policies may encode organizational or regulatory requirements.

Examples include:

* data retention;
* approval requirements;
* financial limits;
* access controls;
* segregation of duties;
* geographic restrictions;
* privacy requirements;
* audit requirements.

Noema should distinguish the Policy from the external regulation or standard from which it originates.

⸻

43. Policy and Regulation

A regulation is an external normative source.

A Policy is a rule adopted by an organization or system to govern behavior.

Conceptually:

Regulation
   ↓
Organizational Policy
   ↓
Constraint / Requirement
   ↓
Runtime Evaluation

The ontology should not collapse Regulation and Policy into the same concept.

⸻

44. Policy and Business Rules

A Business Rule may be an implementation-level expression of a Policy.

Example:

Policy:
Refunds over $10,000 require approval.
Business Rule:
IF refund.amount > 10000
THEN approval_required = true

The Business Rule expresses executable logic.

The Policy remains the governing semantic rule.

Therefore:

Policy ≠ Business Rule

⸻

45. Policy Enforcement

Policy Evaluation and Policy Enforcement remain distinct.

Policy Evaluation
      ↓
Decision
      ↓
Enforcement

Example:

Policy Evaluation:
DENY
Enforcement:
Do not execute Action.

The evaluator determines the governing result.

The runtime applies that result.

⸻

46. Policy Decision

A Policy Decision should be explicit.

Conceptually:

Policy Decision
├── decision
├── applicable_policies
├── satisfied_conditions
├── failed_conditions
├── requirements
└── evidence

Foundational decisions are:

PERMIT
DENY
REQUIRE
UNKNOWN

UNKNOWN is necessary when the facts required for evaluation cannot be established.

⸻

47. Unknown Policy Evaluation

Noema must not convert missing evidence into permission.

Example:

Policy:
Transfers above $10,000 require verified beneficiary.
Beneficiary verification:
UNKNOWN

A valid result may therefore be:

Policy Evaluation:
REQUIRE_VERIFICATION

or, depending on the eventual decision vocabulary:

Policy Evaluation:
UNKNOWN

It must not become:

ALLOW

merely because no contrary evidence has been found.

⸻

48. Policy and Fail-Closed Behavior

For consequential operations, insufficient evidence should generally prevent execution when the applicable Policy requires a condition to be established.

Conceptually:

Required Condition
      ↓
UNKNOWN
      ↓
Compliance Cannot Be Established
      ↓
Do Not Proceed

The precise fail-open/fail-closed semantics belong in the Trust and Policy Enforcement specifications.

The ontology must preserve the distinction between:

SATISFIED

and:

UNKNOWN

⸻

49. Policy Composition

Multiple Policies may compose to establish the effective requirements governing an operation.

Example:

Policy A:
Manager approval required above $10,000.
Policy B:
International transfers above $5,000 require compliance review.
Intent:
International transfer of $20,000.

The effective requirements may therefore be:

Manager Approval
+
Compliance Review

Policy composition must preserve the identity and provenance of the constituent Policies.

⸻

50. Policy Composition Must Be Explicit

Noema should not assume that Policy composition is simply additive.

Policies may:

* grant permission;
* prohibit operations;
* introduce requirements;
* create exceptions;
* restrict scope;
* modify applicability;
* affect precedence.

Therefore the semantics of Policy composition must be explicit and deterministic.

⸻

51. Policy Evaluation Context

Policy evaluation operates against structured Context.

Example:

Actor:
alice
Role:
finance_manager
Intent:
refund_payment
Entity:
payment_123
Amount:
15000
Current Time:
14:30
Location:
Nigeria

Policies can then be evaluated deterministically against these facts.

Context provides the facts.

Policy provides the governing rules.

⸻

52. Policy and Context

The distinction is:

Context = relevant facts
Policy  = governing rules

Example:

Context:
amount = $20,000
Policy:
amount > $10,000 requires approval.

Policy evaluation derives:

approval_required = true

The Policy does not supply the value $20,000.

The Context does.

⸻

53. Policy and Evidence

Evidence establishes or supports the facts required for Policy evaluation.

Example:

Evidence:
Actor role = Finance Manager
Policy:
Finance Managers may approve ≤ $25,000.

Without sufficient trustworthy Evidence:

Actor role = UNKNOWN

Noema cannot safely establish that the Policy condition is satisfied.

⸻

54. Policy Evaluation Must Be Reproducible

Given identical:

Policy Version
+
Input Facts
+
Evaluation Rules

Policy Evaluation should produce the same result.

This makes Policy evaluation:

* auditable;
* testable;
* reproducible;
* explainable.

The evaluation record should preserve enough information to reconstruct the decision.

⸻

55. Policy Decision Record

A consequential Policy evaluation should be recordable.

Conceptually:

Policy Decision
├── decision_id
├── intent_id
├── action_id
├── evaluated_at
├── policy_versions
├── input_facts
├── decision
├── requirements
└── provenance

This allows Noema to explain why an operation was permitted, denied, or made conditional.

⸻

56. Policy Simulation

Policies should be evaluable without executing Actions.

Example:

What would happen if this employee attempted to approve $50,000?

Noema could evaluate:

Policy Simulation
      ↓
DENY

without performing the Action.

Policy simulation supports:

* testing;
* administration;
* debugging;
* compliance;
* workflow design.

⸻

57. Policy Testing

Policies should be testable through deterministic scenarios.

Example:

Given:
actor.role = manager
amount = 5000
Expected:
ALLOW

And:

Given:
actor.role = employee
amount = 50000
Expected:
DENY

Policy behavior can therefore become executable as testable specifications.

⸻

58. Policy Change Impact

Changing a Policy may change whether previously executable Intents remain eligible for execution.

Example:

Old Policy:
Managers may approve ≤ $50,000.
New Policy:
Managers may approve ≤ $25,000.

Noema should be able to identify affected workflows and Actions where practical.

Policy change therefore has potential runtime consequences beyond the Policy record itself.

⸻

59. Policy and Existing Intent State

A resolved Intent does not necessarily remain executable indefinitely.

If the Policy environment changes:

Resolved Intent
      ↓
Policy Changed
      ↓
Re-evaluation Required

The Intent remains historically valid as an Intent.

Its execution eligibility may change.

⸻

60. Policy Re-evaluation

Material changes in:

* Policy;
* Authority;
* Context;
* Entity State;
* Constraints;
* Evidence

may require Trust to be re-evaluated before consequential execution.

This prevents stale governance decisions from being treated as current authorization.

⸻

61. Policy and Time

Some Policies depend on time.

Example:

Policy:
Transactions above $10,000 require additional verification
outside business hours.

The same Intent may therefore produce different Policy evaluations at different times.

Intent
   +
Context(Time)
   ↓
Policy Evaluation

Temporal applicability must be evaluated against the relevant effective Policy version and current Context.

⸻

62. Policy Does Not Guarantee Execution

A Policy may permit an operation while execution still fails.

Example:

Policy:
ALLOW
Trust:
ALLOW
Execution:
FAILED
Outcome:
FAILED

Policy establishes governance conditions.

It does not guarantee operational success.

⸻

63. Policy Does Not Determine Outcome

Likewise:

Policy:
ALLOW
Execution:
SUCCESS
Outcome:
UNSATISFIED

This may occur if the wrong Entity was affected or the original Intent was otherwise not fulfilled.

Therefore:

Policy
   ≠
Execution
   ≠
Outcome
   ≠
Satisfaction

Policy governs eligibility.

Outcome describes what happened.

Satisfaction evaluates whether the original Intent was fulfilled.

⸻

64. Policy and Trust Engine

The Policy system supplies structured governance information to the Trust Engine.

Conceptually:

Intent
  +
Actor
  +
Context
  +
Authority
  +
Constraints
  +
Policies
  +
Evidence
        │
        ▼
   Trust Engine
        │
        ▼
   Trust Decision

The Trust Engine evaluates the available governance information.

It must not invent Policies to justify an execution decision.

⸻

65. Policy Decision vs Trust Decision

These concepts must remain distinct.

Policy Decision

What do the applicable Policies say?

Trust Decision

Given everything Noema knows, should this Action be allowed to proceed?

Example:

Policy Decision:
ALLOW
Authority:
ALLOW
Constraint:
SATISFIED
Evidence:
SUFFICIENT
Trust Decision:
ALLOW

Another example:

Policy Decision:
ALLOW
Authority:
DENY
Trust Decision:
DENY

Therefore:

Policy Decision ≠ Trust Decision

⸻

66. Policy Lifecycle

A Policy may conceptually move through:

DRAFT
   ↓
PROPOSED
   ↓
APPROVED
   ↓
ACTIVE
   ↓
SUSPENDED
   ↓
RETIRED

Only Policies in an applicable authoritative state should participate in runtime evaluation.

The exact lifecycle belongs to Policy Governance rather than this ontology definition.

⸻

67. Policy Retirement

Retiring a Policy must not erase historical evaluations.

Example:

Policy v1:
ACTIVE
Policy v2:
ACTIVE
Historical Decision:
Policy v1

The historical decision remains associated with v1 even after v1 is retired.

Historical governance decisions must remain reproducible.

⸻

68. Policy Immutability

Published Policy versions should be immutable.

If a governing rule changes:

Policy v1

should become:

Policy v2

rather than being silently modified.

This preserves:

* historical truth;
* reproducibility;
* auditability;
* decision lineage.

⸻

69. Canonical Policy Model

A conceptual Policy object is:

Policy
├── id
├── version
├── name
├── description
├── authority
├── scope
├── subject
├── conditions
├── effect
├── requirements
├── priority
├── jurisdiction
├── effective_period
├── provenance
└── status

This is a semantic model rather than a final serialization schema.

Implementation schemas may evolve without changing the underlying distinctions.

⸻

70. Example: Refund Approval

Consider:

Support agents can refund customers up to $1,000. Refunds above $1,000 require manager approval.

A canonical representation may be:

Policy
├── id: refund.approval.limit
├── subject: SupportAgent
├── capability: RefundPayment
├── condition:
│      amount <= 1000
├── effect:
│      ALLOW
│
└── requirement:
       amount > 1000
       → ManagerApproval

Runtime flow:

Actor
  ↓
Intent:
Refund payment
  ↓
Entity:
Payment #123
  ↓
Amount:
$2,500
  ↓
Policy Evaluation
  ↓
Manager Approval Required
  ↓
Trust Evaluation
  ↓
Action permitted only after approval

The Policy establishes the requirement.

The Trust Engine determines whether the complete set of conditions permits the Action.

⸻

71. Example: Card Renewal

Intent:

Renew my card.

Applicable Policies:

Policy A:
Card must not be under fraud investigation.
Policy B:
Identity verification must be current.
Policy C:
Replacement card must be sent to a verified address.

Context:

Fraud Investigation:
false
Identity:
verified
Address:
verified

Policy evaluation:

A → satisfied
B → satisfied
C → satisfied

Result:

Policy Evaluation:
PERMITTED

The Trust Engine may then evaluate whether the Action is permitted to proceed given the complete governance context.

⸻

72. Example: Insufficient Evidence

Intent:

Transfer $20,000.

Policy:

Transfers above $10,000 require verified beneficiary.

Context:

Beneficiary verification:
UNKNOWN

Result:

Policy:
REQUIRE_VERIFICATION

Noema should not proceed merely because the Actor’s request appears legitimate.

The missing fact must remain explicitly unresolved.

⸻

73. Core Policy Invariants

The following are foundational:

1. Policy is a governing rule, not an Intent.
2. Policy is distinct from Constraint.
3. Policy is distinct from Authority.
4. Policy is distinct from Trust.
5. Policy is distinct from Enforcement.
6. Policy evaluation must be deterministic.
7. Applicable Policies must be explicitly identified.
8. Policy conflicts must be resolved by explicit rules.
9. Unknown Evidence must not silently become compliance.
10. Published Policy versions must be immutable.
11. Historical Policy evaluations must remain reproducible.
12. Policy decisions must retain Policy provenance.
13. Policy enforcement must remain distinct from Policy evaluation.
14. Policy permission does not guarantee execution success.
15. Policy permission does not guarantee Intent satisfaction.
16. Policy changes may require Trust re-evaluation.
17. Policy exceptions must be explicit.
18. Policy authority must be traceable.
19. Natural-language Policies must not be the final runtime authority for consequential decisions.
20. The Model may assist in Policy interpretation but must not become the authoritative runtime Policy evaluator.
21. Noema must never silently invent or infer a Policy to justify an execution decision.
22. Policy applicability must be evaluated before Policy effect is applied.
23. Policy evaluation must preserve the Policy version applicable at the relevant time.
24. Unknown facts must remain distinguishable from facts established as false.
25. Policy composition must preserve the identity and provenance of constituent Policies.
26. Policy Decisions must remain distinguishable from Trust Decisions.

⸻

74. Relationship to the Noema Ontology

Policy occupies the governance layer of Noema.

                 ACTOR
                   │
                   ▼
                 INTENT
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     ENTITY     CONTEXT   CONSTRAINT
                   │
                   ▼
                 POLICY
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
    AUTHORITY              EVIDENCE
        │                     │
        └──────────┬──────────┘
                   ▼
                 TRUST
                   │
                   ▼
                 ACTION
                   │
                   ▼
              EXECUTION
                   │
                   ▼
                OUTCOME
                   │
                   ▼
              SATISFACTION

Policy therefore participates in the governance path between semantic representation and consequential execution.

⸻

75. Canonical Governance Relationship

The core relationship is:

Policy
  +
Constraint
  +
Authority
  +
Context
  +
Evidence
       ↓
Policy Evaluation
       ↓
Trust Decision
       ↓
Action
       ↓
Execution
       ↓
Outcome
       ↓
Intent Satisfaction

Each stage answers a different semantic question:

Policy:
What governing rules apply?
Constraint:
What conditions limit this operation?
Authority:
Who may perform it?
Evidence:
What facts establish those conditions?
Policy Evaluation:
What do the applicable Policies require or permit?
Trust:
May Noema allow the consequential Action to proceed?
Action:
What operation is to be performed?
Execution:
What attempt was made?
Outcome:
What actually happened?
Satisfaction:
Did what happened fulfill the original Intent?

⸻

76. Canonical Principle

The central Policy principle is:

A Policy defines the governing rules under which an Intent or Action may proceed; it does not itself constitute Authority, Trust, or execution permission.

Therefore:

Policy
   +
Authority
   +
Constraints
   +
Context
   +
Evidence
        ↓
Policy Evaluation
        ↓
Trust
        ↓
Action

This distinction must remain stable throughout Noema’s architecture.

⸻

77. Relationship to the Semantic Loop

Policy participates in the broader Noema semantic lifecycle:

Actor
  ↓
Intent
  ↓
Resolution
  ↓
Context + Entities + Constraints
  ↓
Applicable Policies
  ↓
Authority + Evidence
  ↓
Policy Evaluation
  ↓
Trust
  ↓
Action
  ↓
Capability
  ↓
Execution
  ↓
Outcome
  ↓
Evidence
  ↓
Intent Satisfaction

The Policy layer therefore does not replace the Intent-to-Outcome loop.

It governs the conditions under which the loop may cross from semantic interpretation into consequential execution.

⸻

78. Final Canonical Statement

Noema’s Policy ontology defines the governing rules that determine what is permitted, prohibited, required, or conditionally permitted within a defined scope.

Policy remains distinct from:

Intent
Constraint
Authority
Trust
Action
Capability
Execution
Outcome
Satisfaction

The semantic boundary is:

Natural Language
       ↓
Intent
       ↓
Context + Entities + Constraints
       ↓
Applicable Policies
       ↓
Authority + Evidence
       ↓
Policy Evaluation
       ↓
Trust
       ↓
Action
       ↓
Capability
       ↓
Execution
       ↓
Outcome
       ↓
Intent Satisfaction

The purpose of this separation is to ensure that Noema can determine, deterministically and auditably:

what is governed, which rules apply, what those rules require or permit, whether their conditions are established, and whether the resulting Action may cross into consequential execution.