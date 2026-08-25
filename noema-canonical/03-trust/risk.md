Risk

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: 03-trust/risk.md

⸻

1. Definition

Risk is the potential for an Intent or its execution to produce an undesirable consequence, considering the Action, Resources, Context, Actor, Outcome, and conditions under which execution occurs.

Risk answers:

“What could go wrong, and how consequential would it be if this Intent were executed?”

Risk is a Trust input, not a substitute for authorization, policy, evidence, or determinism.

⸻

2. The Core Principle

Noema must distinguish whether an Intent is understood and permitted from whether executing it carries consequential risk.

An Intent can be:

well understood
authorized
policy-compliant
technically executable

and still be high risk.

Example:

Intent:
Delete production database.
Intent Resolution:
CLEAR
Authorization:
ALLOWED
Capability:
AVAILABLE
Policy:
ALLOWED
Risk:
CRITICAL

The Trust Engine must account for that risk before execution.

⸻

3. Risk in the Trust Model

Conceptually:

Intent
  ↓
Resolution
  ↓
Evidence
  ↓
Authorization
  ↓
Policy Evaluation
  ↓
Risk Evaluation
  ↓
Capability / Constraints
  ↓
Trust Decision
  ↓
Execution

Risk is therefore one dimension of Trust.

It does not replace the other dimensions.

⸻

4. Risk Is Not Uncertainty

These concepts must remain distinct.

Uncertainty

Noema does not know enough about the Intent or relevant state.

Risk

Noema understands what would happen but recognizes that the consequences could be significant.

Example:

Unknown account:
UNCERTAINTY
Known account, transfer of ₦50M:
RISK

Uncertainty may prevent resolution.

Risk may require additional safeguards.

⸻

5. Risk Is Not Model Confidence

A Model may be:

99.9% confident

that the user wants:

DeleteProductionDatabase()

That does not make the Action low risk.

Therefore:

Model Confidence ≠ Risk

and:

Model Confidence ≠ Trust

⸻

6. Risk Is Not Policy

Policy may say:

"Transfers above ₦10M require secondary approval."

Risk asks:

"How consequential is this transfer?"

Policy may use Risk as an input:

IF risk = HIGH
THEN approval_required

But Risk and Policy remain separate concepts.

⸻

7. Risk Is Not Authorization

Authorization answers:

May this Actor perform the Action?

Risk answers:

What is the consequence if the Action is performed?

An administrator may be fully authorized to delete a production database.

That does not make the operation low risk.

⸻

8. Risk Is Not Capability

A system may have the capability:

DeleteDatabase

while the Action remains:

CRITICAL_RISK

Technical ability does not imply acceptable risk.

⸻

9. Risk Is Not Outcome

Risk describes potential consequences.

Outcome describes what actually happened.

Risk:
High
Execution:
Successful
Outcome:
Database deleted.

Risk does not predict the actual Outcome with certainty.

⸻

10. Risk Has Two Fundamental Dimensions

A useful conceptual model is:

Risk ≈ Likelihood × Consequence

Where:

Likelihood

How plausible is the undesirable event?

Consequence

How severe would the impact be?

Noema should avoid treating this equation as a universal numerical implementation requirement.

The canonical principle is:

Risk considers both the probability and consequence of undesirable outcomes.

⸻

11. Consequence

Consequences may include:

financial loss
data loss
privacy violation
security compromise
service disruption
irreversible state change
legal exposure
reputational damage
physical harm
organizational impact

The applicable consequence categories depend on the domain.

⸻

12. Risk Dimensions

A Noema risk model may consider:

Impact
Reversibility
Blast Radius
Likelihood
Sensitivity
Irreversibility
Scope
Authorization Boundary
Externality
Persistence

Not every Action requires every dimension.

⸻

13. Impact

Impact measures the magnitude of the potential consequence.

Example:

Read profile:
LOW
Change email:
MEDIUM
Delete account:
HIGH
Delete production database:
CRITICAL

⸻

14. Reversibility

An Action that can easily be undone generally presents lower risk than an irreversible Action.

Example:

Update draft:
LOW
Delete record with recovery:
MEDIUM
Permanently destroy records:
HIGH

Reversibility should therefore be a first-class risk dimension.

⸻

15. Blast Radius

Blast radius describes how many entities or systems could be affected.

Example:

Update one customer:
LOW
Update 10,000 customers:
HIGH
Modify global production configuration:
CRITICAL

A seemingly simple Action can become high risk when its scope expands.

⸻

16. Scope

Risk depends on the scope of the Intent.

Compare:

Delete User#123

with:

Delete all users in Tenant#ABC

The semantic Action may be similar.

The risk is not.

⸻

17. Resource Criticality

Some Resources are inherently more consequential.

Examples:

production database
payment account
identity provider
security configuration
customer PII
financial ledger

Risk evaluation should account for Resource criticality.

⸻

18. Action Criticality

Actions themselves can have different inherent risk.

Example:

Read
Write
Modify permissions
Transfer funds
Delete
Deploy
Publish
Execute code

Destructive, privileged, or externally consequential Actions generally require stronger safeguards.

⸻

19. Actor Context

Risk can depend on who is acting.

Example:

Employee
Service Account
Administrator
External Contractor
Automated Agent

The same Action may carry different risk depending on the Actor and authority context.

However:

Actor identity must not be used as a substitute for objective consequence.

An administrator performing a destructive Action does not make the Action inherently safe.

⸻

20. Contextual Risk

Risk can change with Context.

Examples:

normal business hours
incident response
maintenance window
security incident
emergency mode
high-volume period

Example:

Deploy during maintenance window:
LOWER RISK
Deploy during active incident:
HIGHER RISK

⸻

21. Temporal Risk

Risk can vary over time.

Example:

Transfer before payroll:
HIGH
Transfer after settlement:
LOWER

The same Intent may have different risk profiles depending on when it executes.

⸻

22. Environmental Risk

Environment is another important dimension.

development
staging
production

Compare:

Delete staging database:
MEDIUM
Delete production database:
CRITICAL

The Action is identical.

The Resource context changes the risk.

⸻

23. Externality

Some Actions affect parties outside the immediate Actor.

Examples:

send email to customer
publish public announcement
issue payment
cancel supplier contract
modify third-party data

External consequences increase the need for explicit Trust controls.

⸻

24. Persistence

Some changes have long-lasting consequences.

Example:

Change temporary setting:
LOWER
Change permanent account ownership:
HIGHER

Persistent state changes should generally receive greater scrutiny.

⸻

25. Risk Categories

A conceptual taxonomy may include:

FINANCIAL
SECURITY
PRIVACY
DATA
OPERATIONAL
LEGAL
REPUTATIONAL
ACCESS
DESTRUCTIVE
EXTERNAL

These categories may overlap.

An Intent can carry multiple risk categories.

⸻

26. Composite Risk

Example:

Intent:
Export customer database.
Risk:
DATA = HIGH
PRIVACY = HIGH
SECURITY = HIGH
OPERATIONAL = MEDIUM

The Trust Engine should be able to reason about multiple risk dimensions.

⸻

27. Risk Classification

A simple canonical classification could be:

LOW
MEDIUM
HIGH
CRITICAL

These labels are useful for communicating risk.

However, the canonical repository should not assume that four levels are sufficient for every domain.

⸻

28. Risk Classification Must Be Deterministic

Given the same:

Intent
Actor
Resource
Context
Evidence
Risk Rules

Noema should produce the same risk classification.

For example:

IF
    Action = Delete
AND
    Resource.environment = production
THEN
    Risk = CRITICAL

⸻

29. Risk Rules

Risk should be evaluated using explicit rules.

Example:

IF amount > ₦10,000,000
THEN financial_risk = HIGH

Another:

IF resource.environment = production
AND action = Delete
THEN destructive_risk = CRITICAL

The Model may identify relevant dimensions, but the final classification should be deterministic.

⸻

30. Risk Evaluation Inputs

Conceptually:

RiskEvaluation {
    Intent
    Actor
    Resources
    Context
    Evidence
    Action
    Outcome assumptions
}

The implementation may differ.

The semantic requirement is that risk be evaluated from established facts.

⸻

31. Risk Evaluation Should Not Depend on Raw Language

Example:

User:
"Please wipe the old production database."

The Model can interpret:

Action = Delete
Resource = ProductionDatabase#123

Risk Evaluation should then operate on:

Delete(ProductionDatabase#123)

not on the phrase:

“wipe the old production database.”

⸻

32. Risk and Intent Resolution

Risk evaluation should normally occur after the consequential parts of an Intent are resolved.

Example:

"Delete my account."

If there are three accounts:

Account A
Account B
Account C

Noema should first resolve the Resource.

Risk cannot be accurately evaluated until the target is known.

⸻

33. Risk and Ambiguity

Ambiguity can itself prevent meaningful risk evaluation.

Example:

"Delete the database."

Unknown:

which database?

If one possible target is staging and another is production, the risk difference is enormous.

Therefore:

Noema must resolve material ambiguity before using risk to justify execution.

⸻

34. Risk and Evidence

Risk evaluation may require evidence.

Example:

Intent:
Delete Account#123.
Evidence:
Account type = production customer account.

Without the evidence, Noema may not know the true consequence.

Therefore risk may remain:

UNRESOLVED

rather than being classified as low.

⸻

35. Risk and Policy

Policy can consume Risk.

Example:

IF Risk >= HIGH
THEN explicit confirmation required.

The relationship is:

Risk Evaluation
      ↓
Policy Evaluation
      ↓
Trust Decision

Risk does not directly become Policy.

⸻

36. Risk and Authorization

Risk does not grant or revoke authorization.

Example:

Actor:
Authorized
Risk:
CRITICAL

The system may require additional safeguards.

But Risk itself is not an authorization rule.

⸻

37. Risk and Confirmation

A high-risk Intent may require explicit confirmation.

Example:

Risk:
HIGH
Policy:
High-risk destructive actions require confirmation.

Then:

Trust:
WAITING_FOR_CONFIRMATION

Confirmation becomes new evidence.

⸻

38. Risk and Approval

Risk can trigger approval requirements.

Example:

Risk:
HIGH
Policy:
High-risk financial Actions require two approvers.

Result:

REQUIRE_APPROVAL

The approval process should be explicit and auditable.

⸻

39. Risk and Capability

Capability availability does not reduce risk.

Example:

Capability:
DeleteProductionDatabase = available
Risk:
CRITICAL

The Action is technically possible but remains consequential.

⸻

40. Risk and Constraints

Constraints can limit risk.

Example:

Constraint:
Maximum transfer = ₦1,000,000

This may reduce financial exposure.

But the existence of a constraint does not itself prove that the resulting Action is safe.

⸻

41. Risk Mitigation

Risk should not only classify an Intent.

It can identify required mitigations.

Examples:

confirmation
approval
verification
transaction limit
dry run
backup
restricted capability
additional authorization
human review

Conceptually:

Risk
 ↓
Mitigation Requirements
 ↓
Policy
 ↓
Trust

⸻

42. Risk Mitigation Must Be Explicit

Noema should not silently alter an Intent to reduce risk.

Example:

Actor:
Transfer ₦20M.
Risk:
HIGH.

Noema should not silently change:

₦20M → ₦5M

Instead:

REQUIRE_APPROVAL

or another explicit mitigation should be applied.

⸻

43. Risk Acceptance

Some organizations may permit explicit acceptance of certain risks.

Example:

Risk:
HIGH
Authorized Approver:
CFO
Risk Acceptance:
Approved

Risk acceptance is itself an auditable decision.

It should not be inferred from ordinary Actor intent.

⸻

44. Risk Thresholds

Policies may define thresholds.

Example:

LOW:
No additional controls.
MEDIUM:
Explicit confirmation.
HIGH:
Secondary approval.
CRITICAL:
Human review + elevated authorization.

These thresholds are domain-specific.

The canonical repository should define the concept, not impose universal operational thresholds.

⸻

45. Risk Escalation

Risk may trigger escalation.

Example:

LOW
  ↓
No escalation
HIGH
  ↓
Approval
CRITICAL
  ↓
Human review

Escalation should be policy-driven.

⸻

46. Risk and Human-in-the-Loop

Some Actions may be too consequential for autonomous execution.

Example:

Risk = CRITICAL

Policy:

Critical-risk Actions require human approval.

Noema should transition into an explicit state rather than asking the Model to “be more careful.”

⸻

47. Risk and Bounded Autonomy

Risk is central to bounded autonomy.

Conceptually:

Risk
  ↓
Autonomy Boundary
  ↓
Required Controls
  ↓
Execution

Low-risk Actions may execute automatically.

High-risk Actions may require:

confirmation
approval
human intervention

This provides a principled boundary around Agent autonomy.

⸻

48. Risk and Execution Authority

Noema should distinguish:

"Can execute"

from:

"May execute autonomously."

An Action can be technically executable but outside the Agent’s autonomous risk boundary.

⸻

49. Risk and Consumer-Side Execution

The execution consumer should receive relevant risk requirements.

Example:

ExecutionContract {
    action: DeleteResource
    resource: ProductionDatabase#123
    risk: CRITICAL
    human_approval: REQUIRED
}

The consumer should enforce the contract rather than infer risk from raw text.

⸻

50. Risk and Execution Contracts

Risk-related requirements should be represented as typed conditions.

Example:

risk_classification = HIGH
required_approval = 2
confirmation_required = true

This makes the autonomy boundary executable.

⸻

51. Risk and Auditability

A consequential decision should preserve:

Risk classification
Risk rules
Risk inputs
Risk evidence
Mitigations
Approvals
Final Trust decision

This allows an auditor to reconstruct why additional controls were required.

⸻

52. Risk Provenance

A Risk classification should be traceable to its basis.

Example:

Risk:
HIGH
Because:
Action = TransferFunds
Amount = ₦20M
Resource = CorporateAccount
Rule = FinancialRiskThreshold-v3

This is preferable to:

Risk:
0.83

with no semantic explanation.

⸻

53. Risk Scores

A numerical risk score may be useful operationally.

For example:

risk_score = 87

But:

A numerical score must not replace the semantic basis for the classification.

A score without an interpretable rule is difficult to audit and govern.

⸻

54. Risk and Model Scores

Noema should keep:

Model confidence

separate from:

Risk score

They represent different things.

Model confidence:
How confident is the Model in its interpretation?
Risk:
How consequential could execution be?

⸻

55. Risk and Intent Lifecycle

Risk may change throughout an Intent’s lifecycle.

Example:

DRAFT
  ↓
RESOLVED
  ↓
AUTHORIZED
  ↓
APPROVED
  ↓
EXECUTING

Changes in:

resource state
amount
context
policy
time
actor authority

may change risk.

⸻

56. Risk Re-Evaluation

Risk should be re-evaluated when material inputs change.

Examples:

Intent changes
Resource changes
Amount changes
Scope changes
Context changes
Policy changes
Risk rules change
Execution is delayed

⸻

57. Risk at the Execution Boundary

For consequential Actions, risk should be considered immediately before execution.

Conceptually:

Resolved Intent
      ↓
Trust
      ↓
Execution Boundary
      ↓
Risk Revalidation
      ↓
Execute

This is especially important for long-running workflows.

⸻

58. Risk and State Changes

Suppose:

Intent:
Deploy version 4.

At resolution:

Risk = MEDIUM

Before execution:

Production incident begins.

Risk may become:

HIGH

Noema should not blindly reuse the old decision.

⸻

59. Risk and Partial Execution

Composite Intents may have different risk levels per Action.

Example:

Refund payment
Risk = MEDIUM
Close account
Risk = HIGH

The composite Intent should not simply be labeled:

MEDIUM

without preserving the higher-risk component.

⸻

60. Risk Aggregation

For composite Intents, risk may be aggregated using a deterministic rule.

For example:

Composite Risk =
maximum child risk

or:

Composite Risk =
policy-defined aggregation

The exact mechanism is domain-dependent.

The aggregation rule must be explicit.

⸻

61. Risk and Dependencies

One Action can increase the risk of another.

Example:

Disable security monitoring
      ↓
Deploy production change

The second Action may be substantially riskier because the first changes the execution context.

Noema should account for material dependencies where they are known.

⸻

62. Risk and Sequencing

In a composite workflow:

A → B → C

risk may depend on sequence.

Example:

Backup database
→ Delete database

is materially different from:

Delete database
→ Backup database

Risk evaluation should therefore operate on the actual planned Action structure when sequence matters.

⸻

63. Risk and Preconditions

Risk can depend on Preconditions.

Example:

Delete Database

with:

BackupCompleted = true

may be lower risk than:

BackupCompleted = false

The precondition itself becomes part of the Trust model.

⸻

64. Risk and Postconditions

Risk can also depend on expected Postconditions.

Example:

Delete Resource

Expected:

Resource no longer exists.

If deletion leaves dependent resources orphaned, the risk may be higher.

⸻

65. Risk and Side Effects

Side effects are central to risk.

Examples:

database mutation
financial transaction
external communication
permission change
data deletion
deployment

A read-only informational response generally carries substantially less execution risk than an irreversible side effect.

⸻

66. Informational vs Consequential Intents

A useful distinction is:

Informational:
"What's my account balance?"
Consequential:
"Transfer ₦5,000."

Risk controls should primarily intensify as an Intent crosses into consequential side effects.

⸻

67. Risk and Read Operations

Read operations can still carry risk.

Example:

Export all employee salaries.

Although technically a read, it may have:

privacy risk
security risk
compliance risk

Therefore:

Risk is about consequence, not merely whether an Action writes data.

⸻

68. Risk and Public Actions

Publishing information may be highly consequential even if it does not modify internal state.

Example:

Publish company announcement.

Potential:

reputational risk
legal risk
externality

Risk evaluation should capture this.

⸻

69. Risk and Security-Sensitive Actions

Examples:

rotate credentials
disable MFA
modify firewall rules
grant administrator access

These may carry high security risk even when the technical operation is simple.

⸻

70. Risk and Destructive Actions

Destructive Actions generally deserve explicit risk treatment.

Examples:

Delete
Revoke
Terminate
Destroy
Purge
Disable

But destructiveness alone does not determine the final classification; scope and consequence matter.

⸻

71. Risk and Financial Actions

Financial Actions often require:

amount
currency
source
destination
authorization
limits
policy

Risk should account for transaction magnitude and exposure.

⸻

72. Risk and Privacy

Actions involving sensitive data may carry elevated privacy risk.

Examples:

Export
Share
Publish
Transfer
Delete

Risk depends on:

data sensitivity
recipient
scope
jurisdiction
purpose
retention

⸻

73. Risk and Legal / Compliance Context

Some Actions may have regulatory consequences.

Example:

Delete financial records.

Even if the Actor is authorized, retention requirements may create:

compliance risk

Policy Evaluation should enforce applicable rules.

Risk identifies the potential consequence.

⸻

74. Risk and Failure

Risk should consider not only malicious misuse but also ordinary failure.

Examples:

API failure
partial execution
incorrect target
duplicate execution
timeout
state divergence

A high-impact Action with poor rollback characteristics may have elevated operational risk.

⸻

75. Risk and Idempotency

Non-idempotent Actions can carry additional execution risk.

Example:

ChargeCard

If repeated accidentally:

duplicate charge

The risk model may therefore consider idempotency characteristics.

⸻

76. Risk and Rollback

Rollback availability can reduce consequence.

Example:

Configuration change

with:

instant rollback

versus:

irreversible migration

Risk evaluation may incorporate rollback capability.

⸻

77. Risk and Recovery

Recovery capability is distinct from reversibility.

An Action may not be reversible but may have a recovery mechanism.

Example:

Delete database

with:

verified backup

is still destructive, but the potential consequence may differ from deletion without recovery.

⸻

78. Risk and Blast Radius Controls

Risk can be mitigated by reducing scope.

Example:

Update 100,000 records

could be changed explicitly by the Actor to:

Update 1,000 records

But Noema should not silently reduce the scope.

The mitigation must be explicit.

⸻

79. Risk and Dry Runs

A dry run can reduce execution risk.

Example:

Deploy configuration

may first become:

Validate configuration without applying changes.

If the Actor explicitly requests the dry run, it becomes a different Intent.

⸻

80. Risk and Human Review

Human review is not evidence that an Action is safe.

It is a mitigation mechanism.

Example:

Risk:
CRITICAL
Policy:
Human approval required.
Approval:
Granted.

The risk remains:

CRITICAL

The Trust conditions have changed.

⸻

81. Risk Acceptance Does Not Erase Risk

After approval:

Risk = HIGH
Approval = GRANTED

not:

Risk = LOW

This distinction is important for auditability.

⸻

82. Risk and Trust

Trust should not mean:

“Risk is low.”

Instead:

Trust determines whether the known risk is acceptable under the applicable controls and authority.

Conceptually:

Risk
+
Policy
+
Authorization
+
Evidence
+
Constraints
+
Required Mitigations
        ↓
Trust Decision

⸻

83. Risk Decision Matrix

A conceptual model:

Risk	Policy	Authorization	Result
Low	Satisfied	Allowed	May execute
Medium	Satisfied	Allowed	May require confirmation
High	Satisfied	Allowed	May require approval
Critical	Satisfied	Allowed	May require human review
Any	Denied	Allowed	Cannot execute
Any	Unresolved	Allowed	Cannot execute yet
Any	Satisfied	Denied	Cannot execute

The exact thresholds belong to Policy, not to Risk itself.

⸻

84. Risk and Deterministic Trust

Risk contributes to deterministic Trust by replacing vague judgments such as:

“This feels dangerous.”

with explicit semantics:

Action = Delete
Resource = ProductionDatabase
Environment = Production
BlastRadius = TenantWide
Reversible = No
RiskClassification = CRITICAL

The resulting control requirement can then be deterministic.

⸻

85. Risk Evaluation Should Be Explainable

A useful explanation should answer:

What is risky?
Why is it risky?
What evidence establishes the risk factors?
Which rule produced the classification?
What mitigation is required?

Example:

“This action is classified as high risk because it transfers ₦20,000,000 and cannot be reversed after settlement. The applicable policy requires secondary approval.”

⸻

86. Risk Evaluation Must Not Be a Model Monologue

Noema should not depend on an LLM generating:

“I think this is risky because…”

Instead, it should derive the result from explicit risk factors and rules.

The Model can assist with:

candidate risk factors
semantic extraction

The Trust layer should determine the final classification.

⸻

87. Risk Evaluation and Model Assistance

A safe architecture is:

Model
 ↓
Candidate Risk Factors
 ↓
Canonicalization
 ↓
Evidence
 ↓
Deterministic Risk Rules
 ↓
Risk Classification

This allows probabilistic interpretation without making Risk itself probabilistic.

⸻

88. Risk and Evidence Provenance

Risk factors should have evidence.

Example:

Risk Factor:
Production Resource
Evidence:
Environment#123.type = production

Another:

Risk Factor:
Irreversible
Evidence:
Delete API has no restore operation.

This creates a defensible risk determination.

⸻

89. Risk and Capability Metadata

Capability definitions may expose risk-relevant properties.

Example:

Capability:
DeleteResource
Properties:
destructive = true
reversible = false
external_side_effect = true

These properties can contribute to risk evaluation.

⸻

90. Risk and Action Ontology

The Action ontology should identify semantic properties relevant to risk.

For example:

Action:
Delete
Properties:
destructive
state-changing
potentially irreversible

Risk Evaluation combines these properties with Context and Resource information.

⸻

91. Risk and Resource Ontology

Resources may have risk-relevant properties.

Example:

Resource:
ProductionDatabase
Properties:
criticality = critical
environment = production
contains_sensitive_data = true

Risk can then be derived deterministically.

⸻

92. Risk and Context Ontology

Context may establish:

maintenance_window
incident_active
emergency
business_critical_period

These can materially affect risk.

⸻

93. Risk and Outcome Ontology

Expected Outcomes can inform consequence evaluation.

Example:

Expected Outcome:
Customer account permanently deleted.

This establishes a different consequence profile from:

Expected Outcome:
Customer account temporarily suspended.

⸻

94. Risk and State

Current state may determine risk.

Example:

Database.status = recovering

A migration may therefore carry higher operational risk.

State must be established through evidence.

⸻

95. Risk and Relationships

Relationships can affect blast radius.

Example:

Account
  owns
  ↓
100,000 Orders

Deleting the Account may indirectly affect all 100,000 Orders.

The relationship graph can therefore provide risk-relevant context.

⸻

96. Risk and Entity Resolution

Risk cannot be accurately evaluated if the target entity is unresolved.

Example:

"Delete the account."

If:

Account A = test
Account B = production

the unresolved identity is materially relevant to risk.

Therefore:

Entity Resolution
        ↓
Risk Evaluation

must be respected where the entity changes consequence.

⸻

97. Risk and Constraint Resolution

Risk can depend on resolved constraints.

Example:

Transfer:
₦5M

Constraint:

Daily limit = ₦10M

The action remains within the limit.

But:

Transfer:
₦20M

may cross both policy and risk thresholds.

⸻

98. Risk and Authorization Scope

Authorization scope can affect risk.

Example:

Actor:
Authorized to modify one resource.

Intent:

Modify 100 resources.

The authorization mismatch may prevent execution.

Risk evaluation should not interpret broad intent from narrow authority.

⸻

99. Risk and Autonomy Levels

Noema may eventually define autonomy boundaries such as:

AUTONOMOUS
CONFIRMATION_REQUIRED
APPROVAL_REQUIRED
HUMAN_REQUIRED
PROHIBITED

Risk can contribute to selecting the appropriate boundary.

But the actual autonomy decision belongs to Trust / Policy.

⸻

100. Risk and Noema’s Core Thesis

Noema exists to turn ambiguous human intent into safe, executable intent.

Risk is what allows Noema to distinguish:

"understood"

from:

"safe to execute autonomously."

That distinction is fundamental.

⸻

101. Canonical Risk Flow

                 Resolved Intent
                       │
                       ▼
                Identify Effects
                       │
                       ▼
               Identify Risk Factors
                       │
                       ▼
             Gather Supporting Evidence
                       │
                       ▼
             Evaluate Risk Rules
                       │
                       ▼
              Risk Classification
                       │
                       ▼
              Determine Mitigations
                       │
                       ▼
                Policy Evaluation
                       │
                       ▼
                 Trust Decision

⸻

102. Canonical Invariants

Invariant 1

Risk is distinct from uncertainty, confidence, authorization, capability, policy, and Outcome.

Invariant 2

Risk must be evaluated against resolved semantic objects, not raw natural language.

Invariant 3

Risk classification should be deterministic given the same relevant inputs and risk rules.

Invariant 4

Risk must be grounded in identifiable factors and, where material, supporting evidence.

Invariant 5

Risk is about consequence, not merely whether an Action mutates state.

Invariant 6

Risk should account for impact, scope, reversibility, and other materially relevant dimensions.

Invariant 7

High risk does not automatically mean prohibited.

Invariant 8

Low risk does not automatically mean authorized.

Invariant 9

Risk does not modify an Actor’s Intent without explicit authorization.

Invariant 10

Risk mitigation must be explicit and auditable.

Invariant 11

Risk acceptance does not erase or lower the underlying risk classification.

Invariant 12

Material changes to Intent, Context, Resource state, or other risk inputs may require re-evaluation.

Invariant 13

Risk requirements should be proportional to the potential consequence of execution.

Invariant 14

Composite Intents must preserve material risk differences between constituent Actions.

Invariant 15

Risk classification should be explainable from explicit factors and rules rather than Model-generated judgment.

⸻

103. The Fundamental Distinction

The core distinction is:

Intent:
"What does the Actor want?"
Authorization:
"May they do it?"
Policy:
"Under what conditions may they do it?"
Risk:
"What could happen if they do it?"
Mitigation:
"What additional controls are required?"
Trust:
"Is it acceptable to cross the execution boundary?"

⸻

104. Final Definition

Risk is the structured assessment of the potential consequence and likelihood of undesirable outcomes arising from an Intent, considering its Action, Resources, Context, scope, reversibility, and other material factors.

The shortest canonical formulation is:

Risk does not determine whether an Intent is allowed; it determines how consequential execution could be and what level of control may be required before Noema permits it to proceed.