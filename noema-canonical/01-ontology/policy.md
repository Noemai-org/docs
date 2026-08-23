Yes. policy.md is an important one because we need to be very precise about Policy vs Constraint vs Authority vs Trust. If we blur those, the Trust Engine becomes ambiguous.

Policy

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/policy.md

⸻

1. Definition

A Policy is a governing rule that determines what is permitted, required, prohibited, or conditionally permitted within a defined scope.

A Policy expresses organizational, regulatory, operational, or system-level governance.

It answers:

Under what governing rules may this Intent or Action proceed?

A Policy is not itself an Action, Constraint, Authority, or Trust decision.

⸻

2. Policy’s Role in Noema

Policy provides the governing rules against which an Intent or Action can be evaluated.

Intent
   │
   ▼
Policy Evaluation
   │
   ├── Permitted
   ├── Prohibited
   ├── Conditionally Permitted
   └── Requires Additional Conditions

Policy therefore participates in the deterministic decision boundary before consequential execution.

⸻

3. Policy Is Not Intent

Intent represents what an Actor wants.

Policy represents what the governing environment allows or requires.

Intent:
Refund this customer.
Policy:
Refunds above $10,000 require manager approval.

The Intent does not change because of the Policy.

The Policy determines the conditions under which the Intent may be fulfilled.

⸻

4. Policy Is Not Constraint

These concepts are related but distinct.

A Constraint limits an individual Intent, Action, or operation.

A Policy establishes a governing rule from which constraints or requirements may be derived.

Example:

Policy:
Refunds above $10,000 require manager approval.
Constraint:
refund.amount <= $10,000

The Policy is the governing rule.

The Constraint is the concrete condition applied to the current operation.

⸻

5. Policy Is Not Authority

Authority answers:

Who is permitted to perform this operation?

Policy answers:

What rules govern whether this operation may occur?

Example:

Actor:
Support Agent
Authority:
Can issue refunds.
Policy:
Refunds above $10,000 require manager approval.

The Actor may have the Capability and Authority to issue refunds while still being unable to perform this particular refund without additional approval.

⸻

6. Policy Is Not Trust

Trust is Noema’s decision about whether an Intent or Action may proceed given the available facts, Policies, Constraints, Authority, Context, and Evidence.

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

A Policy is an input to the decision.

Trust is the resulting decision.

⸻

7. Policy Scope

Every Policy should have a defined scope.

Possible scopes include:

Organization
Department
Role
Actor
Entity
Capability
Action
Intent
Resource
Environment
Geography
Time

Example:

Policy:
Finance employees may approve expenses up to $25,000.

Scope:

Department = Finance

⸻

8. Policy Subject

A Policy applies to one or more subjects.

Examples:

Actor
Role
Organization
Capability
Action
Entity
Intent
Resource

Example:

Policy:
Managers may approve expenses above $10,000.

Subject:

Role = Manager

⸻

9. Policy Effect

A Policy should produce an explicit semantic effect.

Foundational effects are:

ALLOW
DENY
REQUIRE
RESTRICT

Where appropriate, additional effects may be introduced.

Example:

ALLOW:
Manager may approve expense.
DENY:
Intern may not approve expense.
REQUIRE:
Expense above $10,000 requires approval.
RESTRICT:
Only company-issued cards may be used.

⸻

10. Conditional Policies

Policies may be conditional.

Example:

IF
  amount > $10,000
THEN
  manager approval required

Another example:

IF
  actor.role = "finance_manager"
AND
  amount <= $25,000
THEN
  approval permitted

The condition must be evaluated against explicit Context and Evidence.

⸻

11. Policy Conditions

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

⸻

12. Policy Requirements

A Policy may impose requirements rather than simply allow or deny.

Example:

Policy:
International transfers above $10,000 require enhanced verification.

The Policy does not necessarily deny the transfer.

Instead:

Transfer
   ↓
Requirement:
Enhanced Verification
   ↓
Verification
   ↓
Continue evaluation

This distinction is important.

⸻

13. Policy Preconditions

Some Policies establish preconditions.

Example:

Policy:
A customer must complete KYC before withdrawing funds.

Canonical interpretation:

Intent:
Withdraw Funds
Policy:
KYC required
Precondition:
KYC = VERIFIED

If the precondition is not satisfied:

Trust:
DENIED

or:

Trust:
BLOCKED_PENDING_REQUIREMENT

depending on Noema’s eventual Trust model.

⸻

14. Policy and Constraints

Policies frequently produce Constraints.

Example:

Policy:
Employees may spend no more than $5,000 without approval.
Derived Constraint:
expense.amount <= 5000

Therefore:

Policy
  ↓
Constraint
  ↓
Evaluation

But not every Constraint necessarily originates from a Policy.

A Constraint may originate from:

* Actor preference
* Intent
* System capability
* Resource limitations
* Context
* Technical requirements

⸻

15. Policy Hierarchy

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

Noema must define conflict resolution explicitly rather than assuming that specificity always wins.

⸻

16. Policy Precedence

When Policies conflict, Noema must not silently select one.

Example:

Policy A:
Managers may approve up to $50,000.
Policy B:
This department limits approval to $25,000.

The applicable Policy set must be evaluated according to explicit precedence rules.

Potential precedence dimensions include:

Authority
Scope
Specificity
Priority
Jurisdiction
Temporal validity
Policy version

The canonical precedence algorithm belongs in the Trust/Policy evaluation specification, not in this ontology definition.

⸻

17. Deny vs Allow

A Policy may explicitly permit or prohibit an operation.

Example:

Policy A:
ALLOW managers to approve expenses.
Policy B:
DENY approval of expenses from restricted vendors.

The system must resolve the interaction deterministically.

Noema must not depend on model judgment to resolve Policy conflicts.

⸻

18. Explicit Denial

A Policy denial should be represented explicitly.

Example:

Intent:
Delete customer account.
Policy:
Customer records cannot be permanently deleted while an active legal hold exists.
Result:
DENIED

The system should preserve the Policy responsible for the denial.

⸻

19. Policy Explanation

A consequential Policy decision should be explainable.

Noema should be able to answer:

Which Policy caused this Action to be permitted or denied?

Example:

Decision:
DENIED
Policy:
customer.legal_hold.deletion
Reason:
Active legal hold exists.

The explanation should reference canonical Policy identifiers rather than relying solely on generated natural-language explanations.

⸻

20. Policy Identification

Policies should have stable identities.

Example:

policy.customer.deletion.legal_hold

This enables:

* auditing
* versioning
* references
* testing
* policy evaluation
* decision explanations

⸻

21. Policy Versioning

Policies evolve.

Example:

Policy:
expense.approval.limit
v1:
$10,000
v2:
$25,000

A Policy evaluation should be associated with the applicable Policy version.

Historical decisions should not be retroactively reinterpreted using the latest Policy version.

⸻

22. Policy Effective Time

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

should not be evaluated using a Policy that becomes effective on September 1.

⸻

23. Policy Jurisdiction

Policies may apply within a particular jurisdiction.

Examples:

Country
State
Organization
Business Unit
Data Region
Regulatory Domain

Example:

Policy:
Data may only be exported to approved regions.

The applicable jurisdiction must be determined from Context and Entity information.

⸻

24. Policy Applicability

Not every Policy applies to every Intent.

Noema must first determine:

Is this Policy applicable?

before evaluating:

Does this Policy allow or deny the operation?

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

⸻

25. Policy Evaluation

Policy evaluation determines the effect of applicable Policies under the current Context.

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

The evaluation should be deterministic.

⸻

26. Policy Evaluation Must Be Deterministic

The Trust Engine must not ask the Model:

“Does this seem allowed?”

Instead, the Model may help identify structured facts.

For example:

Model:
Actor appears to be requesting a refund.

Noema then evaluates:

refund.amount <= policy.limit

using deterministic rules.

⸻

27. Policy and Model Reasoning

The Model can assist with:

Interpretation
Classification
Extraction
Entity Resolution
Candidate Intent Generation

The Model should not be the authoritative Policy evaluator.

The boundary is:

Model
  ↓
Structured Facts
  ↓
Noema Policy Engine
  ↓
Deterministic Evaluation

⸻

28. Policy and Natural Language

Policies may originate as natural-language documents.

Example:

“Expenses above $10,000 require director approval.”

But runtime evaluation should ultimately operate on canonical representations.

Natural Language Policy
        ↓
Policy Interpretation
        ↓
Canonical Policy
        ↓
Executable Policy Representation
        ↓
Deterministic Evaluation

The canonical representation should be authoritative for execution.

⸻

29. Policy Compilation

Noema may eventually support compiling Policies into executable representations.

Example:

Human Policy
     ↓
Canonical Policy
     ↓
Policy AST / Rule Representation
     ↓
Policy Evaluator

This allows policies to be:

* versioned
* tested
* simulated
* audited
* evaluated consistently

⸻

30. Policy as Data

Policies should be treated as structured domain objects rather than hidden application logic.

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
└── provenance

The eventual schema may evolve.

⸻

31. Policy Provenance

Noema should know where a Policy originated.

Possible sources:

Organization
Regulation
Contract
Administrator
System Configuration
Security Standard
Operational Rule

Example:

Policy:
expense.approval.limit
Source:
Finance Governance Document
Version:
2026.3

⸻

32. Policy Authority

A Policy must itself have an authoritative source.

Not every statement that looks like a rule should become a Policy.

For example:

"John usually approves refunds."

is not necessarily a Policy.

Whereas:

"Refunds above $10,000 require Finance Manager approval."

may constitute a Policy if established by an authoritative governance source.

⸻

33. Policy Provenance vs Policy Authority

These are related but distinct.

Provenance:

Where did this Policy come from?

Authority:

Why is this source authorized to establish this Policy?

Example:

Provenance:
Finance Department Policy Manual
Authority:
Chief Financial Officer

⸻

34. Policy Conflicts

Policies can conflict.

Example:

Policy A:
Managers may approve up to $50,000.
Policy B:
International payments are limited to $10,000.
Intent:
International payment of $30,000.

Noema must identify the conflict and resolve it according to canonical precedence rules.

It must not let an LLM choose whichever Policy “sounds more relevant.”

⸻

35. Policy Exceptions

Some Policies may permit explicit exceptions.

Example:

Policy:
Refunds above $10,000 require Director approval.
Exception:
Emergency incidents may bypass the normal approval workflow.

Exceptions must themselves be modeled explicitly.

An exception should not simply override the Policy invisibly.

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

⸻

37. Policy and Actor

Policies may apply differently depending on Actor characteristics.

Example:

Policy:
Employees may approve expenses up to $5,000.
Policy:
Managers may approve expenses up to $25,000.

Actor context therefore participates in Policy evaluation.

⸻

38. Policy and Capability

A Capability says:

The system can do this.

A Policy says:

Under these conditions, this may or may not be done.

Example:

Capability:
delete.customer
Policy:
Customer deletion prohibited while legal hold is active.

Therefore:

Capability ≠ Permission

A system being capable of something does not make it permissible.

⸻

39. Policy and Action

Policies may apply directly to Actions.

Example:

Action:
DeleteCustomer(customer_123)
Policy:
Deletion requires verified identity.

The Action is structurally valid but cannot proceed until the Policy requirement is satisfied.

⸻

40. Policy and Intent

Policies may also apply at the Intent level.

Example:

Intent:
Export customer data.
Policy:
Customer data export requires a legitimate business purpose.

This allows Noema to reject an Intent before constructing an Action.

⸻

41. Policy and Outcome

Policies may govern not only whether an Action may execute but also how Outcomes are handled.

Example:

Policy:
Failed financial transactions must be reconciled within 24 hours.

The Policy may therefore trigger requirements after an Outcome occurs.

Outcome:
Transfer Failed
Policy:
Reconciliation Required
Derived Action:
ReconcileTransfer

⸻

42. Policy and Compliance

Policies may encode organizational or regulatory requirements.

Examples:

Data retention
Approval requirements
Financial limits
Access controls
Segregation of duties
Geographic restrictions
Privacy requirements
Audit requirements

Noema should distinguish the Policy from the external regulation or standard from which it originates.

⸻

43. Policy and Regulation

A regulation is an external normative source.

A Policy is the rule adopted by an organization or system to govern behavior.

Example:

Regulation
   ↓
Organizational Policy
   ↓
Constraint
   ↓
Runtime Evaluation

The ontology should not collapse these concepts.

⸻

44. Policy and Business Rules

A Business Rule may be an implementation-level representation of a Policy.

For example:

Policy:
Refunds over $10,000 require approval.
Business Rule:
IF refund.amount > 10000
THEN approval_required = true

The Business Rule is an executable expression of the Policy.

⸻

45. Policy Enforcement

Policy evaluation and Policy enforcement should remain distinct.

Policy Evaluation
      ↓
Decision
      ↓
Enforcement

For example:

Policy Evaluation:
DENY
Enforcement:
Do not execute Action.

The Policy Engine determines the decision.

The runtime enforces it.

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

Possible decisions include:

PERMIT
DENY
REQUIRE
UNKNOWN

UNKNOWN is important when the facts required for evaluation are unavailable.

⸻

47. Unknown Policy Evaluation

Noema must not convert missing evidence into permission.

Example:

Policy:
Transfers above $10,000 require verified beneficiary.
Beneficiary verification:
UNKNOWN

Correct result:

Policy Evaluation:
UNKNOWN / REQUIRE_VERIFICATION

Not:

ALLOW

⸻

48. Policy and Fail-Closed Behavior

For consequential operations, insufficient evidence should generally prevent execution when the Policy requires certainty.

Conceptually:

Required condition
      ↓
Unknown
      ↓
Cannot establish compliance
      ↓
Do not proceed

The precise fail-open/fail-closed behavior belongs to the Trust and Policy Enforcement specifications, but the ontology must preserve the distinction.

⸻

49. Policy Composition

Multiple Policies may compose to determine the applicable requirements.

Policy A
+
Policy B
+
Policy C
      ↓
Effective Policy Set

For example:

Policy A:
Manager approval required above $10,000.
Policy B:
International transfers above $5,000 require compliance review.
Intent:
International transfer of $20,000.

Effective requirements:

Manager Approval
+
Compliance Review

⸻

50. Policy Monotonicity

Noema should be cautious about assuming that adding Policies always makes a decision more restrictive.

Some Policies may:

* grant permission
* introduce requirements
* create exceptions
* alter scope
* modify precedence

Therefore Policy composition requires explicit semantics.

⸻

51. Policy Evaluation Context

Policy evaluation should operate against a structured Context.

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

⸻

52. Policy Evaluation Must Be Reproducible

Given identical:

Policy Version
+
Input Facts
+
Evaluation Rules

the Policy evaluation should produce the same result.

This makes the Trust Engine:

* auditable
* testable
* reproducible
* explainable

⸻

53. Policy Decision Record

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

This allows Noema to explain why an Action was permitted or denied.

⸻

54. Policy Simulation

Policies should ideally be evaluable without executing Actions.

Example:

"What would happen if this employee attempted to approve $50,000?"

Noema could evaluate:

Policy Simulation
      ↓
DENIED

without performing the Action.

This becomes valuable for:

* testing
* administration
* debugging
* compliance
* workflow design

⸻

55. Policy Testing

Policies should be testable using deterministic scenarios.

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

Policy behavior should therefore be executable as testable specifications.

⸻

56. Policy Change Impact

Changing a Policy can change whether previously valid Intents remain executable.

Example:

Old Policy:
Managers may approve ≤ $50,000.
New Policy:
Managers may approve ≤ $25,000.

Noema should be able to identify affected workflows and Actions where practical.

⸻

57. Policy and Existing Intent State

A resolved Intent does not necessarily remain executable forever.

If the Policy environment changes:

Resolved Intent
      ↓
Policy Changed
      ↓
Re-evaluation Required

The Intent remains historically valid as an Intent.

Its execution eligibility may change.

⸻

58. Policy Re-evaluation

Material changes in:

* Policy
* Authority
* Context
* Entity State
* Constraints
* Evidence

may require Trust to be re-evaluated before execution.

This prevents stale authorization decisions.

⸻

59. Policy and Time

Some Policies depend on time.

Example:

Policy:
Transactions above $10,000 require additional verification outside business hours.

The same Intent may therefore produce different Policy evaluations at different times.

Intent
   +
Context(time)
   ↓
Policy Evaluation

⸻

60. Policy and Context

Context provides the facts.

Policy provides the rules.

Context = facts
Policy  = governing rules

Example:

Context:
amount = $20,000
Policy:
amount > $10,000 requires approval

The Policy evaluation derives:

approval_required = true

⸻

61. Policy and Evidence

Evidence establishes the facts needed to evaluate a Policy.

Evidence:
Actor role = Finance Manager
Policy:
Finance Managers may approve ≤ $25,000.

Without trustworthy evidence:

Actor role = UNKNOWN

Noema cannot safely infer that the Policy condition is satisfied.

⸻

62. Policy and Trust Engine

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

The Trust Engine should not invent Policies.

It evaluates applicable Policies.

⸻

63. Policy Decision vs Trust Decision

These should remain distinct.

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

Or:

Policy Decision:
ALLOW
Authority:
DENY
Trust Decision:
DENY

⸻

64. Policy Does Not Guarantee Execution

A Policy may permit an Action while execution still fails.

Policy:
ALLOW
Trust:
ALLOW
Execution:
FAILED
Outcome:
FAILED

Policy only determines governance eligibility.

It does not guarantee operational success.

⸻

65. Policy Does Not Determine Outcome

Likewise:

Policy:
ALLOW
Execution:
SUCCESS
Outcome:
UNSATISFIED

if the wrong Entity was affected or the Intent was otherwise not fulfilled.

Policy and Outcome therefore remain independent semantic dimensions.

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

The exact lifecycle belongs to Policy Governance rather than this ontology document.

⸻

67. Policy Retirement

Retiring a Policy should not erase historical evaluations.

Example:

Policy v1:
ACTIVE
Policy v2:
ACTIVE
Historical Decision:
Policy v1

The historical decision remains associated with v1 even after v1 is retired.

⸻

68. Policy Immutability

Published Policy versions should be immutable.

If a rule changes:

Policy v1

should become:

Policy v2

rather than being silently modified.

This ensures reproducibility.

⸻

69. Canonical Policy Model

A conceptual Policy object:

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

The implementation schema may evolve without changing these semantic distinctions.

⸻

70. Example

Consider:

“Support agents can refund customers up to $1,000. Refunds above $1,000 require manager approval.”

Canonical representation:

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

The resulting runtime flow:

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

⸻

71. Another Example: Card Renewal

Intent:
Renew my card.

Applicable Policies:

Policy A:
Card must not be under fraud investigation.
Policy B:
Identity verification must be current.
Policy C:
Replacement card must be sent to verified address.

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

The Trust Engine may then determine whether the Action is trusted to proceed.

⸻

72. Another Example: Insufficient Evidence

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

Noema should not proceed simply because the Actor’s request appears legitimate.

⸻

73. Canonical Invariants

The following are foundational Policy invariants:

1. Policy is a governing rule, not an Intent.
2. Policy is distinct from Constraint.
3. Policy is distinct from Authority.
4. Policy is distinct from Trust.
5. Policy evaluation must be deterministic.
6. Applicable Policies must be explicitly identified.
7. Policy conflicts must be resolved by explicit rules.
8. Unknown evidence must not silently become compliance.
9. Published Policy versions must be immutable.
10. Historical Policy evaluations must remain reproducible.
11. Policy decisions must retain Policy provenance.
12. Policy enforcement must remain distinct from Policy evaluation.
13. Policy permission does not guarantee execution success.
14. Policy permission does not guarantee Intent satisfaction.
15. Policy changes may require Trust re-evaluation.
16. Policy exceptions must be explicit.
17. Policy authority must be traceable.
18. Natural-language Policies must not be the final runtime authority for consequential decisions.
19. The Model may assist in Policy interpretation but must not become the authoritative Policy evaluator.
20. Noema must never silently invent or infer a Policy to justify an execution decision.

⸻

74. Relationship to the Ontology

Policy sits primarily within the governance layer of Noema.

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

⸻

75. Canonical Principle

A Policy defines what is governed; a Constraint defines what is limited; Authority defines who may act; Trust determines whether Noema permits the Action under the applicable facts and rules.

The resulting boundary is:

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
     Trust
       ↓
     Action

This distinction should remain non-negotiable throughout Noema’s architecture.

The next ontology document I’d put after policy.md is authority.md, because we now have the four pieces that feed the Trust Engine becoming increasingly clear:

Intent
   ↓
Constraints + Policies + Authority + Evidence
   ↓
Trust
   ↓
Action

That will let us define exactly what “who is allowed to do what, on whose behalf, and within what scope” means before we move deeper into the runtime model.