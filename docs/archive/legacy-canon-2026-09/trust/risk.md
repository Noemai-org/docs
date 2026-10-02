Risk

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/risk.md

⸻

1. Definition

Risk is the structured assessment of the potential for an Intent or its execution to produce an undesirable consequence, considering the Action, Resources, Context, Actor, expected Outcome, scope, reversibility, and other material conditions under which execution occurs.

Risk answers:

“What could happen if this Intent is executed, how consequential could the undesirable outcomes be, and what controls may therefore be required?”

Risk is a Trust input.

Risk is distinct from:

* Intent
* Intent Resolution
* Uncertainty
* Model Confidence
* Evidence
* Authorization
* Policy
* Capability
* Constraints
* Execution
* Outcome

Risk does not by itself determine whether an Intent is authorized or permitted.

⸻

2. The Core Principle

Noema must distinguish whether an Intent is understood and permitted from whether executing it carries consequential risk.

An Intent can be:

* well understood
* resolved
* authorized
* policy-compliant
* technically executable

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

3. Risk Evaluation

Risk Evaluation is the deterministic process by which Noema identifies material risk factors associated with a resolved Intent, establishes the relevant evidence, evaluates applicable Risk Rules, and produces a Risk Classification and, where applicable, required mitigation conditions.

Conceptually:

Resolved Intent
      ↓
Identify Effects
      ↓
Identify Risk Factors
      ↓
Gather Evidence
      ↓
Evaluate Risk Rules
      ↓
Risk Classification
      ↓
Determine Mitigations
      ↓
Trust

The Model may assist with candidate risk-factor identification.

The canonical Risk result must be grounded in established semantic objects, evidence, and explicit rules.

⸻

4. Risk in the Trust Model

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

The exact ordering of Trust evaluations may vary where dependencies require it.

The architectural principle is:

Risk is one dimension of Trust and does not replace the other Trust dimensions.

⸻

5. Risk Is Not Uncertainty

These concepts must remain distinct.

Uncertainty

Noema does not know enough about the Intent or relevant state.

Risk

Noema understands the relevant Intent and state sufficiently to identify potentially consequential outcomes.

Example:

Unknown account:
UNCERTAINTY
Known account, transfer of ₦50M:
RISK

Uncertainty may prevent resolution or risk evaluation.

Risk may require additional safeguards.

A system must not convert uncertainty into low risk merely because no risk has yet been established.

⸻

6. Risk Is Not Model Confidence

A Model may be:

99.9% confident

that the Actor wants:

DeleteProductionDatabase()

That does not make the Action low risk.

Therefore:

Model Confidence ≠ Risk

and:

Model Confidence ≠ Trust

Model confidence concerns the reliability of an interpretation.

Risk concerns the potential consequences of execution.

⸻

7. Risk Is Not Policy

Policy may say:

Transfers above ₦10M require secondary approval.

Risk asks:

How consequential is this transfer?

Policy may use Risk as an input:

IF risk >= HIGH
THEN approval_required

But Risk and Policy remain separate concepts.

Risk identifies potential consequence.

Policy determines what conditions or controls apply.

⸻

8. Risk Is Not Authorization

Authorization answers:

May this Actor perform the Action?

Risk answers:

What could happen if the Action is performed?

An administrator may be fully authorized to delete a production database.

That does not make the operation low risk.

⸻

9. Risk Is Not Capability

A system may have the capability:

DeleteDatabase

while the Action remains:

CRITICAL_RISK

Technical ability does not imply acceptable risk.

⸻

10. Risk Is Not Constraint

A Constraint limits what an Intent may do.

Risk evaluates the potential consequence of doing it.

Example:

Constraint:
Maximum transfer = ₦1M
Risk:
Transfer exposes ₦1M of financial value.

A Constraint may mitigate risk, but the two concepts remain distinct.

⸻

11. Risk Is Not Outcome

Risk describes potential undesirable consequences.

Outcome describes what actually happened.

Example:

Risk:
HIGH
Execution:
Successful
Outcome:
Database deleted.

Risk does not determine the actual Outcome.

Likewise:

Risk:
CRITICAL
Execution:
Failed before mutation.
Outcome:
No database deletion.

The existence of high risk does not imply that the undesirable outcome occurred.

⸻

12. Risk Is Not Trust

Trust is the broader determination of whether an Intent may cross the execution boundary under the applicable authority, evidence, policy, capability, constraints, risk controls, and other requirements.

Risk contributes to Trust.

Risk does not equal Trust.

⸻

13. Two Fundamental Risk Dimensions

A useful conceptual model is:

Risk ≈ Likelihood × Consequence

Where:

Likelihood

How plausible is the undesirable event?

Consequence

How severe would the impact be if it occurred?

Noema should not treat this equation as a universal numerical implementation requirement.

The canonical principle is:

Risk considers both the likelihood and consequence of undesirable outcomes where those dimensions can be meaningfully established.

Some Risk Rules may classify risk without an explicit numerical likelihood calculation.

⸻

14. Consequence

Potential consequences may include:

* financial loss
* data loss
* privacy violation
* security compromise
* service disruption
* irreversible state change
* legal exposure
* regulatory exposure
* reputational damage
* physical harm
* organizational impact
* external-party impact

The applicable consequence categories depend on the domain.

⸻

15. Risk Factors

Risk Evaluation may consider factors including:

* Impact
* Likelihood
* Reversibility
* Irreversibility
* Blast Radius
* Scope
* Resource Criticality
* Action Criticality
* Sensitivity
* Persistence
* Externality
* Environmental State
* Temporal Context
* Actor Context
* Recovery Capability
* Rollback Capability
* Idempotency
* Dependency Structure
* Expected Outcome
* Failure Modes

Not every Intent requires every factor.

Risk Evaluation should consider the factors material to the Intent.

⸻

16. Impact

Impact measures the magnitude of potential consequence.

Example:

Read profile:
LOW
Change email:
MEDIUM
Delete account:
HIGH
Delete production database:
CRITICAL

Impact should be established from semantic and contextual facts rather than Model judgment alone.

⸻

17. Likelihood

Likelihood concerns how plausible a material undesirable event is.

Examples may include:

Rare
Possible
Likely
Highly likely

The exact classification is domain-dependent.

Where likelihood cannot be meaningfully established, Noema should preserve that uncertainty rather than fabricate precision.

⸻

18. Reversibility

An Action that can easily be undone generally presents a different risk profile from an irreversible Action.

Example:

Update draft:
LOWER RISK
Delete record with recovery:
MEDIUM
Permanently destroy records:
HIGHER RISK

Reversibility should therefore be a first-class risk factor.

⸻

19. Irreversibility

Irreversibility is closely related to reversibility but may be represented explicitly when the absence of recovery is itself consequential.

Example:

DeleteResource
restore_available = false

This is materially different from:

DeleteResource
restore_available = true

The Risk model should preserve this distinction where relevant.

⸻

20. Blast Radius

Blast radius describes how many entities, resources, users, systems, or external parties could be affected.

Example:

Update one customer:
LOW
Update 10,000 customers:
HIGH
Modify global production configuration:
CRITICAL

A seemingly simple Action can become high risk when its scope expands.

⸻

21. Scope

Risk depends on the scope of the Intent.

Compare:

Delete User#123

with:

Delete all users in Tenant#ABC

The semantic Action may be similar.

The risk is not.

Scope must therefore be represented explicitly where it materially affects consequence.

⸻

22. Resource Criticality

Some Resources are inherently more consequential.

Examples:

* production database
* payment account
* identity provider
* security configuration
* customer PII
* financial ledger
* credential store
* production infrastructure

Risk Evaluation should account for Resource criticality.

⸻

23. Action Criticality

Actions themselves can have different inherent risk characteristics.

Examples:

Read
Write
Modify permissions
Transfer funds
Delete
Deploy
Publish
Execute code

Destructive, privileged, externally consequential, or irreversible Actions generally require stronger risk controls.

However, Action type alone does not determine final risk.

Scope and Context remain relevant.

⸻

24. Actor Context

Risk can depend on the Actor and authority context.

Examples:

* Employee
* Service Account
* Administrator
* External Contractor
* Automated Agent

The same Action may have different risk characteristics depending on the Actor context.

However:

Actor identity must not be used as a substitute for objective consequence.

An administrator performing a destructive Action does not make the Action inherently safe.

⸻

25. Contextual Risk

Risk can change with Context.

Examples:

* normal business hours
* incident response
* maintenance window
* security incident
* emergency mode
* high-volume period
* regulatory reporting period

Example:

Deploy during approved maintenance window:
LOWER RISK
Deploy during active incident:
HIGHER RISK

⸻

26. Temporal Risk

Risk can vary over time.

Example:

Transfer before payroll:
HIGH
Transfer after settlement:
LOWER

The same Intent may have different risk profiles depending on when execution occurs.

⸻

27. Environmental Risk

Environment is an important risk factor.

Examples:

development
staging
production

Compare:

Delete staging database:
MEDIUM
Delete production database:
CRITICAL

The Action is identical.

The Resource environment changes the risk.

⸻

28. Externality

Some Actions affect parties outside the immediate Actor or organization.

Examples:

* send email to customer
* publish public announcement
* issue payment
* cancel supplier contract
* modify third-party data
* transmit sensitive information

External consequences should be represented as risk factors where material.

⸻

29. Persistence

Some changes have long-lasting consequences.

Example:

Change temporary setting:
LOWER
Change permanent account ownership:
HIGHER

Persistent state changes should generally receive greater scrutiny where their consequences are material.

⸻

30. Risk Categories

A conceptual taxonomy may include:

FINANCIAL
SECURITY
PRIVACY
DATA
OPERATIONAL
LEGAL
COMPLIANCE
REPUTATIONAL
ACCESS
DESTRUCTIVE
EXTERNAL

These categories may overlap.

An Intent can carry multiple risk categories simultaneously.

⸻

31. Composite Risk

Example:

Intent:
Export customer database.
Risk:
DATA = HIGH
PRIVACY = HIGH
SECURITY = HIGH
OPERATIONAL = MEDIUM

The Trust Engine should be able to preserve multiple risk dimensions.

A single aggregate classification must not erase materially important category-level risk.

⸻

32. Risk Classification

A simple conceptual classification may be:

LOW
MEDIUM
HIGH
CRITICAL

These labels are useful for communicating risk.

However, the canonical repository must not assume that four levels are sufficient for every domain.

Domains may define additional or different classifications.

⸻

33. Risk Classification Is Not Risk Acceptance

These concepts must remain separate.

Example:

Risk:
CRITICAL
Required control:
Human approval
Approval:
Granted

The Risk remains:

CRITICAL

Approval changes the Trust conditions.

It does not erase the underlying risk.

⸻

34. Risk Classification Is Not Permission

A low-risk classification does not mean:

ALLOW

Likewise:

HIGH

does not necessarily mean:

DENY

The relationship is:

Risk Classification
        ↓
Policy / Trust Rules
        ↓
Required Controls
        ↓
Trust Decision

⸻

35. Risk Classification Must Be Deterministic

Given the same:

* Intent
* Actor
* Resources
* Context
* Evidence
* Risk Rules
* relevant state

Noema should produce the same Risk Classification.

Example:

IF
    Action = Delete
AND
    Resource.environment = production
THEN
    Risk = CRITICAL

⸻

36. Risk Rules

Risk should be evaluated using explicit rules.

Example:

IF amount > ₦10,000,000
THEN financial_risk = HIGH

Another:

IF resource.environment = production
AND action = Delete
THEN destructive_risk = CRITICAL

The Model may identify candidate factors.

The final classification should be produced by deterministic Risk Rules.

⸻

37. Risk Evaluation Inputs

Conceptually:

RiskEvaluation {
    Intent
    Actor
    Resources
    Context
    Evidence
    Action
    ExpectedOutcome
    Preconditions
    Constraints
    RelevantCapabilities
    RiskRules
}

The exact implementation is not canonical.

The semantic requirement is that Risk Evaluation operate from established facts and explicit rules.

⸻

38. Risk Evaluation Must Operate on Resolved Semantics

Example:

Actor:

“Please wipe the old production database.”

The Model may interpret:

Action = Delete
Resource = ProductionDatabase#123

Risk Evaluation should operate on:

Delete(ProductionDatabase#123)

rather than on:

“wipe the old production database.”

⸻

39. Risk and Intent Resolution

Risk Evaluation should normally occur after the consequential portions of an Intent are resolved.

Example:

“Delete my account.”

If there are:

Account A
Account B
Account C

Noema should first resolve the Resource.

Risk cannot be accurately evaluated until the target is known.

⸻

40. Risk and Material Ambiguity

Ambiguity can prevent meaningful Risk Evaluation.

Example:

“Delete the database.”

Possible targets:

Database A = staging
Database B = production

The risk difference is material.

Therefore:

Noema must resolve material ambiguity before using Risk to justify execution.

⸻

41. Risk and Evidence

Risk Evaluation may require evidence.

Example:

Intent:
Delete Account#123
Evidence:
Account.type = production_customer_account

Without the evidence, Noema may not know the true consequence.

Risk may therefore remain unresolved.

⸻

42. Risk Evaluation States

Risk Evaluation may need explicit states beyond a simple classification.

Conceptually:

CLASSIFIED
UNRESOLVED
INSUFFICIENT_EVIDENCE
CONFLICTING_EVIDENCE
EVALUATION_FAILED

These states must not be confused with:

LOW
MEDIUM
HIGH
CRITICAL

A risk classification describes established risk.

An unresolved state describes insufficient basis for classification.

⸻

43. Missing Risk Evidence

Example:

Policy:
Delete production resources requires elevated controls.
Intent:
Delete Resource#123.
Resource.environment:
UNKNOWN

Noema should not infer:

LOW

merely because production status is unknown.

The appropriate result may be:

RISK_UNRESOLVED

until the relevant state is established.

⸻

44. Conflicting Risk Evidence

Example:

Inventory:
Resource#123 = staging
Deployment system:
Resource#123 = production

If environment materially affects risk, the conflict must be resolved before relying on the classification.

Conceptually:

CONFLICTING_EVIDENCE

or an equivalent unresolved state.

⸻

45. Risk and Policy

Policy can consume Risk.

Example:

IF Risk >= HIGH
THEN explicit confirmation required.

The relationship is:

Risk Evaluation
      ↓
Risk Classification
      ↓
Policy Evaluation
      ↓
Trust Decision

Risk does not directly become Policy.

⸻

46. Risk and Authorization

Risk does not grant or revoke Authorization.

Example:

Authorization:
ALLOWED
Risk:
CRITICAL

The system may require additional safeguards.

Risk itself is not an Authorization rule.

⸻

47. Risk and Capability

Capability availability does not reduce Risk.

Example:

Capability:
DeleteProductionDatabase = AVAILABLE
Risk:
CRITICAL

The Action is technically possible but remains consequential.

⸻

48. Risk and Constraints

Constraints can reduce exposure.

Example:

Constraint:
Maximum transfer = ₦1,000,000

This may reduce financial exposure.

But the existence of a Constraint does not itself prove that the resulting Action is safe.

⸻

49. Risk and Confirmation

A high-risk Intent may require explicit confirmation.

Example:

Risk:
HIGH
Policy:
High-risk destructive Actions require confirmation.

Result:

REQUIRE_CONFIRMATION

Confirmation becomes additional evidence in the Trust process.

⸻

50. Risk and Approval

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

51. Risk Mitigation

Risk Evaluation may identify controls required to reduce or govern exposure.

Examples:

* confirmation
* approval
* verification
* transaction limit
* dry run
* backup
* restricted capability
* additional authorization
* human review
* reduced execution scope
* staged execution

Conceptually:

Risk
 ↓
Mitigation Requirements
 ↓
Policy
 ↓
Trust

⸻

52. Risk Mitigation Must Be Explicit

Noema must not silently alter an Intent to reduce Risk.

Example:

Actor:
Transfer ₦20M.
Risk:
HIGH

Noema should not silently change:

₦20M → ₦5M

Instead, it should produce an explicit requirement such as:

REQUIRE_APPROVAL

or another applicable mitigation.

⸻

53. Risk Mitigation Does Not Change the Original Intent

Mitigation must remain traceable to the original Intent.

Example:

Original Intent:
Transfer ₦20M.
Risk:
HIGH
Mitigation:
Secondary approval required.

The system must not represent the original Intent as though it had always been:

Transfer ₦10M.

Intent modification requires an explicit semantic transition.

⸻

54. Risk Acceptance

Some organizations may permit explicit acceptance of certain risks.

Example:

Risk:
HIGH
Authorized Approver:
CFO
Risk Acceptance:
APPROVED

Risk acceptance is itself an auditable decision.

It should not be inferred from ordinary Actor Intent.

⸻

55. Risk Acceptance Does Not Erase Risk

After acceptance:

Risk = HIGH
Acceptance = GRANTED

not:

Risk = LOW

Risk acceptance changes the Trust state.

It does not rewrite the Risk classification.

⸻

56. Risk Thresholds

Policies may define operational thresholds.

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

The canonical repository should define the relationship between Risk and control requirements without imposing universal operational thresholds.

⸻

57. Risk Escalation

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

Escalation should be determined by applicable Policy and Trust rules.

Risk identifies the condition; Policy determines the required response.

⸻

58. Risk and Human-in-the-Loop

Some Actions may be too consequential for autonomous execution.

Example:

Risk = CRITICAL

Policy:

Critical-risk Actions require human approval.

Noema should transition into an explicit Trust state rather than asking the Model to “be more careful.”

⸻

59. Risk and Bounded Autonomy

Risk is central to bounded autonomy.

Conceptually:

Risk
  ↓
Autonomy Boundary
  ↓
Required Controls
  ↓
Execution

Lower-risk Actions may be eligible for autonomous execution.

Higher-risk Actions may require:

* confirmation
* approval
* human intervention
* restricted execution
* prohibition

The actual autonomy decision belongs to Trust and Policy, not Risk alone.

⸻

60. Risk and Execution Authority

Noema must distinguish:

Can execute

from:

May execute autonomously.

An Action can be technically executable while remaining outside the Agent’s autonomous risk boundary.

⸻

61. Risk and Consumer-Side Execution

The execution consumer should receive relevant risk requirements.

Example:

ExecutionContract {
    action: DeleteResource
    resource: ProductionDatabase#123
    risk_classification: CRITICAL
    human_approval: REQUIRED
}

The consumer should enforce the contract rather than infer Risk from raw text.

⸻

62. Risk and Execution Contracts

Risk-related requirements should be represented as typed conditions.

Example:

risk_classification = HIGH
required_approval = 2
confirmation_required = true

This makes the autonomy boundary executable and auditable.

⸻

63. Risk and Policy Enforcement

Risk identifies the condition.

Policy determines the required control.

Trust determines whether the execution boundary may be crossed.

Therefore:

Risk:
CRITICAL
Policy:
Human approval required
Approval:
Granted
Trust:
Potentially executable

The consumer must enforce the resulting Execution Contract.

⸻

64. Risk and Execution

Risk does not guarantee an Outcome.

Example:

Risk:
HIGH
Policy:
ALLOW
Trust:
ALLOW
Execution:
Provider timeout
Outcome:
FAILED

The execution result remains distinct from the Risk classification.

⸻

65. Risk at the Execution Boundary

For consequential Actions, Risk should be considered immediately before execution.

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

66. Risk Re-Evaluation

Risk should be re-evaluated when material inputs change.

Examples:

* Intent changes
* Resource changes
* Amount changes
* Scope changes
* Actor changes
* Context changes
* Resource state changes
* Policy changes
* Risk Rules change
* Evidence changes or expires
* Execution is delayed
* Dependencies change

A prior Risk result must not automatically remain valid after material inputs change.

⸻

67. Risk and Long-Running Workflows

Example:

Day 1:
Deployment approved.
Day 2:
Security freeze activated.
Day 3:
Deployment executes.

The original Risk assessment may no longer be sufficient.

Noema may require Risk and Policy re-evaluation immediately before execution.

⸻

68. Risk and State Changes

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

69. Risk and Evidence Freshness

Risk-relevant evidence may become stale.

Example:

Evidence:
Resource.environment = staging

If the resource is later promoted to production, the original Risk result may no longer be valid.

Risk Evaluation must account for evidence freshness where relevant.

⸻

70. Risk and Caching

Risk results may be cached where safe.

However, cache validity must account for relevant:

* Risk Rule version
* Intent version
* Actor state
* Resource state
* Context
* Evidence freshness
* Policy version
* execution timing

A stale Risk result must not be reused simply because it is convenient.

⸻

71. Risk Evaluation Should Be Repeatable

Evaluating the same established Risk inputs repeatedly should not itself change Risk state.

Conceptually:

Inputs
  ↓
Risk Evaluation
  ↓
Result

Risk Evaluation should preferably be side-effect free.

Side effects belong to explicit Actions and execution.

⸻

72. Risk and External Calls

Risk Evaluation may need external state.

Those calls should retrieve evidence rather than allow arbitrary external systems to implicitly determine Risk.

For example:

Risk Engine
    ↓
Resource Service
    ↓
Evidence
    ↓
Risk Evaluation

rather than:

Risk Engine
    ↓
"External service said low risk"
    ↓
ALLOW

without preserving the underlying semantic basis.

⸻

73. Risk Evaluation Failure

If the Risk Engine cannot retrieve required authoritative state:

Risk:
UNKNOWN

The correct result for a consequential Action is generally:

UNRESOLVED

or:

NOT_EXECUTABLE

rather than:

LOW

or:

ALLOW

⸻

74. Risk Availability vs Risk Result

These are different:

Risk:
NOT APPLICABLE

versus:

Risk:
COULD NOT BE EVALUATED

The first is a semantic result.

The second is an evaluation or infrastructure failure.

Noema should not confuse them.

⸻

75. Risk Provenance

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

76. Risk Evidence Provenance

Risk factors should have supporting evidence.

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

This creates a defensible Risk determination.

⸻

77. Risk Rules Must Be Versioned

Risk Rules may change.

Therefore a consequential Risk Classification should identify the relevant Rule version.

Example:

financial-risk-v3

rather than merely:

financial-risk

This enables reproducibility and audit.

⸻

78. Risk Rule Activation

Risk Rules may have effective times.

Example:

risk-policy-v2
effective_from = 2026-09-01

Before the effective time:

v1

After:

v2

Time must therefore be an explicit input where relevant.

⸻

79. Risk Rule Scope

Risk Rules should explicitly define scope where relevant.

Examples:

* Tenant
* Organization
* Region
* Resource
* Resource type
* Actor class
* Action
* Environment

A rule applying to:

Tenant#A

should not automatically govern:

Tenant#B

⸻

80. Risk and Capability Metadata

Capability definitions may expose risk-relevant properties.

Example:

Capability:
DeleteResource
Properties:
destructive = true
reversible = false
external_side_effect = true

These properties can contribute to Risk Evaluation.

Capability metadata is evidence about the Action’s characteristics.

It does not itself determine the final Risk.

⸻

81. Risk and Action Ontology

The Action ontology should identify semantic properties relevant to Risk.

Example:

Action:
Delete
Properties:
destructive
state-changing
potentially irreversible

Risk Evaluation combines these properties with Resource and Context information.

⸻

82. Risk and Resource Ontology

Resources may have Risk-relevant properties.

Example:

Resource:
ProductionDatabase
Properties:
criticality = critical
environment = production
contains_sensitive_data = true

Risk can then be derived deterministically.

⸻

83. Risk and Context Ontology

Context may establish:

maintenance_window
incident_active
emergency
business_critical_period

These can materially affect Risk.

⸻

84. Risk and Outcome Ontology

Expected Outcomes can inform consequence evaluation.

Example:

Expected Outcome:
Customer account permanently deleted.

This establishes a different consequence profile from:

Expected Outcome:
Customer account temporarily suspended.

Expected Outcome is not actual Outcome.

⸻

85. Risk and State

Current state may determine Risk.

Example:

Database.status = recovering

A migration may therefore carry higher operational Risk.

State must be established through evidence.

⸻

86. Risk and Relationships

Relationships can affect blast radius.

Example:

Account
  owns
   ↓
100,000 Orders

Deleting the Account may indirectly affect all 100,000 Orders.

The relationship graph can therefore provide Risk-relevant context.

⸻

87. Risk and Entity Resolution

Risk cannot be accurately evaluated if the target entity is unresolved.

Example:

“Delete the account.”

If:

Account A = test
Account B = production

the unresolved identity is materially relevant to Risk.

Therefore:

Entity Resolution
        ↓
Risk Evaluation

must be respected where entity identity changes consequence.

⸻

88. Risk and Constraint Resolution

Risk can depend on resolved Constraints.

Example:

Transfer:
₦5M
Constraint:
Daily limit = ₦10M

The transfer remains within the limit.

But:

Transfer:
₦20M

may cross both Policy and Risk thresholds.

⸻

89. Risk and Authorization Scope

Authorization scope can affect Risk context.

Example:

Actor:
Authorized to modify one Resource.
Intent:
Modify 100 Resources.

The authorization mismatch may prevent execution.

Risk Evaluation should not interpret narrow authority as permission for broader scope.

⸻

90. Risk and Composite Intents

Composite Intents may contain Actions with materially different Risk.

Example:

Refund payment
Risk = MEDIUM
Close account
Risk = HIGH

The composite Intent should preserve the Risk of each constituent Action.

It should not simply be represented as:

MEDIUM

without preserving the higher-risk component.

⸻

91. Risk Aggregation

For Composite Intents, Risk may be aggregated using a deterministic rule.

Possible mechanisms include:

Composite Risk = maximum child risk

or:

Composite Risk = policy-defined aggregation

The exact mechanism is domain-dependent.

The aggregation rule must be explicit.

A composite classification must not conceal a materially higher-risk constituent Action.

⸻

92. Risk and Dependencies

One Action can increase the Risk of another.

Example:

Disable security monitoring
        ↓
Deploy production change

The second Action may be substantially riskier because the first changes the execution Context.

Noema should account for material dependencies where they are established.

⸻

93. Risk and Sequencing

In a composite workflow:

A → B → C

Risk may depend on sequence.

Example:

Backup database
→ Delete database

is materially different from:

Delete database
→ Backup database

Risk Evaluation should therefore operate on the actual planned Action structure when sequence materially affects consequence.

⸻

94. Risk and Preconditions

Risk can depend on Preconditions.

Example:

Delete Database
Precondition:
BackupCompleted = true

may be lower risk than:

BackupCompleted = false

The precondition therefore becomes part of the Trust model.

⸻

95. Risk and Postconditions

Risk can also depend on expected Postconditions.

Example:

Delete Resource
Expected:
Resource no longer exists.

If deletion leaves dependent Resources orphaned, the Risk may be higher.

⸻

96. Risk and Side Effects

Side effects are central to Risk.

Examples:

* database mutation
* financial transaction
* external communication
* permission change
* data deletion
* deployment
* credential rotation

A read-only informational response generally carries substantially less execution Risk than an irreversible side effect.

However, read operations can still be high risk when their consequence is significant.

⸻

97. Informational vs Consequential Intents

A useful distinction is:

Informational

“What’s my account balance?”

Consequential

“Transfer ₦5,000.”

Risk controls should generally intensify as an Intent crosses into consequential side effects.

This is a risk distinction, not an authorization rule.

⸻

98. Risk and Read Operations

Read operations can still carry Risk.

Example:

Export all employee salaries.

Although technically a read, it may create:

* privacy risk
* security risk
* compliance risk

Therefore:

Risk is about consequence, not merely whether an Action writes data.

⸻

99. Risk and Public Actions

Publishing information may be highly consequential even if it does not modify internal state.

Example:

Publish company announcement.

Potential risks include:

* reputational risk
* legal risk
* externality
* market impact

Risk Evaluation should capture these where material.

⸻

100. Risk and Security-Sensitive Actions

Examples:

* rotate credentials
* disable MFA
* modify firewall rules
* grant administrator access
* change security configuration

These may carry high security Risk even when the technical operation is simple.

⸻

101. Risk and Destructive Actions

Destructive Actions generally deserve explicit Risk treatment.

Examples:

* Delete
* Revoke
* Terminate
* Destroy
* Purge
* Disable

But destructiveness alone does not determine final classification.

Scope, Resource criticality, reversibility, Context, and consequence also matter.

⸻

102. Risk and Financial Actions

Financial Actions often require:

* amount
* currency
* source
* destination
* authorization
* limits
* Policy
* relevant Context

Risk should account for transaction magnitude and financial exposure.

⸻

103. Risk and Privacy

Actions involving sensitive data may carry elevated privacy Risk.

Examples:

* Export
* Share
* Publish
* Transfer
* Delete

Risk may depend on:

* data sensitivity
* recipient
* scope
* jurisdiction
* purpose
* retention
* exposure

⸻

104. Risk and Legal / Compliance Context

Some Actions may have regulatory consequences.

Example:

Delete financial records.

Even if the Actor is authorized, retention requirements may create:

COMPLIANCE RISK

Policy Evaluation should enforce applicable rules.

Risk identifies the potential consequence.

⸻

105. Risk and Failure Modes

Risk should consider not only malicious misuse but also ordinary execution failure.

Examples:

* API failure
* partial execution
* incorrect target
* duplicate execution
* timeout
* state divergence
* dependency failure
* stale state

A high-impact Action with poor rollback characteristics may have elevated operational Risk.

⸻

106. Risk and Idempotency

Non-idempotent Actions can carry additional execution Risk.

Example:

ChargeCard

If repeated accidentally:

duplicate charge

Risk Evaluation may therefore consider idempotency characteristics.

⸻

107. Risk and Rollback

Rollback availability can reduce potential consequence.

Example:

Configuration change

with:

instant rollback

versus:

irreversible migration

Risk Evaluation may incorporate rollback capability where it materially affects recovery.

⸻

108. Risk and Recovery

Recovery capability is distinct from reversibility.

An Action may not be reversible but may have a recovery mechanism.

Example:

Delete database

with:

verified backup

is still destructive, but the potential consequence may differ from deletion without recovery.

Recovery capability should therefore remain explicit.

⸻

109. Risk and Blast Radius Controls

Risk can be mitigated by reducing scope.

Example:

Update 100,000 records

could be explicitly changed by the Actor to:

Update 1,000 records

But Noema must not silently reduce the scope.

The mitigation must be explicit.

⸻

110. Risk and Dry Runs

A dry run can reduce execution Risk.

Example:

Deploy configuration

may first become:

Validate configuration without applying changes.

If the Actor explicitly requests the dry run, it is a different Intent.

Noema should not silently substitute a dry run for the requested Action.

⸻

111. Risk and Human Review

Human review is not evidence that an Action is safe.

It is a mitigation mechanism.

Example:

Risk:
CRITICAL
Policy:
Human approval required.
Approval:
Granted.

The Risk remains:

CRITICAL

The Trust conditions have changed.

⸻

112. Risk and Autonomy Levels

Noema may eventually define autonomy boundaries such as:

AUTONOMOUS
CONFIRMATION_REQUIRED
APPROVAL_REQUIRED
HUMAN_REQUIRED
PROHIBITED

Risk can contribute to determining the applicable boundary.

But the actual autonomy decision belongs to Trust and Policy.

Risk does not independently assign an execution permission.

⸻

113. Risk and Trust

Trust should not mean:

“Risk is low.”

Instead:

Trust determines whether the known Risk is acceptable under the applicable authority, Policy, evidence, constraints, capabilities, and required controls.

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
Capability
+
Required Mitigations
        ↓
Trust Decision

⸻

114. Risk Does Not Override Policy

Example:

Risk:
LOW

does not override:

Policy:
DENY

Likewise:

Risk:
HIGH

does not automatically establish:

Policy:
DENY

Risk and Policy retain distinct semantic roles.

⸻

115. Risk Does Not Override Authorization

Example:

Risk:
LOW
Authorization:
DENIED

The Intent cannot execute.

Conversely:

Risk:
CRITICAL
Authorization:
ALLOWED

The Intent may still require additional controls.

⸻

116. Risk Does Not Override Capability

Example:

Risk:
LOW
Capability:
UNAVAILABLE

The Action cannot execute.

Risk cannot create a missing Capability.

⸻

117. Risk Does Not Override Evidence

If required evidence is missing:

Risk:
UNKNOWN

Noema must not convert the absence of evidence into:

LOW RISK

Evidence sufficiency remains a separate Trust condition.

⸻

118. Risk Decision Matrix

A conceptual model:

Risk	Policy	Authorization	Result
Low	Satisfied	Allowed	May execute if all other Trust conditions are satisfied
Medium	Satisfied	Allowed	May require confirmation
High	Satisfied	Allowed	May require approval
Critical	Satisfied	Allowed	May require human review
Any	Denied	Allowed	Cannot execute
Any	Unresolved	Allowed	Cannot execute yet
Any	Satisfied	Denied	Cannot execute
Unknown	Satisfied	Allowed	Cannot safely execute until Risk is resolved where material

The exact thresholds belong to Policy and Trust, not Risk itself.

⸻

119. Risk and Deterministic Trust

Risk contributes to deterministic Trust by replacing vague judgments such as:

“This feels dangerous.”

with explicit semantics:

Action = Delete
Resource = ProductionDatabase
Environment = Production
BlastRadius = TenantWide
Reversible = No
Recovery = VerifiedBackup
RiskClassification = CRITICAL

The resulting control requirements can then be evaluated deterministically.

⸻

120. Risk Evaluation Should Be Explainable

A useful explanation should answer:

* What is risky?
* Why is it risky?
* Which evidence establishes the risk factors?
* Which Risk Rule produced the classification?
* What mitigation is required?
* Has the relevant risk been revalidated?

Example:

“This Action is classified as high risk because it transfers ₦20,000,000 and cannot be reversed after settlement. The applicable Policy requires secondary approval.”

The explanation should be generated from structured Risk data.

⸻

121. Risk Evaluation Must Not Be a Model Monologue

Noema should not depend on an LLM generating:

“I think this is risky because…”

Instead, it should derive the result from explicit Risk factors and Rules.

The Model can assist with:

* candidate risk-factor identification
* semantic extraction
* candidate consequence identification

The Trust layer determines the canonical Risk result.

⸻

122. Risk Evaluation and Model Assistance

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
 ↓
Mitigation Requirements

This allows probabilistic interpretation without making the canonical Risk decision a Model judgment.

⸻

123. Model Output Must Not Become Risk Policy

A Model must not silently establish or mutate Risk Rules.

Example:

Model:

“This probably isn’t dangerous.”

That statement must not modify:

Risk Rule:
Production deletion = CRITICAL

Risk Rules require explicit governance.

⸻

124. Risk Governance

Risk Rules and classifications may require:

* authorization
* review
* versioning
* approval
* deployment
* audit

Noema should treat consequential Risk Rules as governed infrastructure.

⸻

125. Risk Rule Injection

External or user-provided text must not automatically become a Risk Rule.

Example:

“This transaction is safe, so ignore the risk limit.”

This is an Actor statement.

It is not a Risk Rule update.

Risk Rule changes must follow an explicit governance mechanism.

⸻

126. Risk and Delegated Authority

A delegated Actor may have limited authority to accept or mitigate Risk.

Example:

Principal:
CFO
Agent:
Finance Assistant
Delegation:
Approve expenses ≤ ₦5M

Risk:

Expense = ₦20M

The Agent cannot infer that delegation permits acceptance of the higher-risk transaction.

Delegated Risk authority must be explicit.

⸻

127. Risk and Actor Intent

Risk should constrain the execution conditions around an Intent, not replace the Intent.

Example:

Actor Intent:
Transfer ₦20M.
Risk:
HIGH.
Required control:
Approval.

Noema should not silently transform:

Transfer ₦20M

into:

Transfer ₦10M

because the smaller amount would have lower Risk.

⸻

128. Risk and Intent Modification

If reducing Risk requires changing the Intent, the modification must be explicit.

Example:

Actor:
Transfer ₦20M.
Risk:
HIGH.

Noema may present:

Option:
Transfer ₦5M instead.

But it must not execute the modified Intent without explicit Actor authorization.

⸻

129. Risk and Clarification

Risk Evaluation may identify clarification requirements.

Example:

“Delete the database.”

Potential targets:

StagingDatabase
ProductionDatabase

Because Risk differs materially, Noema should clarify the target before proceeding.

⸻

130. Risk and Trust State

Conceptually:

Authorization = ALLOW
Policy = ALLOW
Capability = AVAILABLE
Constraints = SATISFIED
Evidence = SUFFICIENT
Risk = ACCEPTABLE UNDER APPLICABLE CONTROLS
        ↓
Trust = ALLOW

But:

Authorization = ALLOW
Policy = REQUIRE_APPROVAL
Risk = HIGH

means:

Trust = NOT_EXECUTABLE_YET

Risk contributes to the Trust state but does not determine it alone.

⸻

131. Risk and Long-Lived Trust Decisions

A Risk result should be associated with the Intent version and relevant evaluation inputs.

A decision made for:

Intent#123 v1

must not automatically be reused for:

Intent#123 v2

if the Risk-relevant semantics changed.

⸻

132. Risk and Execution Delay

If execution is delayed, Risk may need to be revalidated.

Example:

09:00
Risk = MEDIUM
12:00
Incident begins
12:05
Execution requested

The original Risk result may no longer be valid.

⸻

133. Risk and State Revalidation

Immediately before execution, Noema should revalidate material Risk inputs where required.

Potential inputs include:

* Resource state
* Environment
* Scope
* Amount
* Actor authority
* Context
* Dependencies
* Evidence freshness
* Risk Rule version

This prevents stale Risk classifications from crossing the execution boundary.

⸻

134. Risk and Partial Execution

Composite workflows may partially execute.

Example:

Action A:
Refund payment
Risk = MEDIUM
Action B:
Close account
Risk = HIGH

If Action A executes successfully but Action B fails, the resulting Outcome must preserve the distinct Risk and execution state of each component.

Risk must not be inferred from the aggregate Outcome.

⸻

135. Risk and Transaction Boundaries

Where multiple Actions execute atomically, Risk may consider the combined consequence.

Where Actions execute independently, each Action may require separate Risk Evaluation.

The execution model therefore matters to Risk Evaluation.

⸻

136. Risk and Failure Recovery

Risk should account for material failure modes.

Example:

Action:
TransferFunds
Failure:
Timeout after provider acceptance
Potential consequence:
Unknown settlement state

This may produce operational Risk independent of the financial value itself.

⸻

137. Risk and Duplicate Execution

Non-idempotent operations may produce elevated Risk because repeated execution can multiply consequences.

Example:

ChargeCard

If executed twice:

DuplicateCharge

Risk Evaluation should account for duplicate-execution characteristics where material.

⸻

138. Risk and Dependency State

Dependencies can materially change Risk.

Example:

Payment Provider:
Healthy

versus:

Payment Provider:
Degraded

The same financial Action may have a different operational Risk profile.

Dependency state must be established through evidence.

⸻

139. Risk and Resource Relationships

Risk may propagate through relationships.

Example:

Customer
   ↓ owns
Account
   ↓ contains
Funds

An Action against the Customer may indirectly affect Accounts and financial Resources.

The semantic relationship graph may therefore be relevant to Risk Evaluation.

⸻

140. Risk and Scope Expansion

Risk should be sensitive to scope changes.

Example:

Original:
Delete User#123

versus:

Updated:
Delete all users in Tenant#123

The Action family may be identical.

The Risk is materially different because the blast radius changed.

⸻

141. Risk and External Recipients

Data-sharing Risk may depend on the recipient.

Example:

Share customer data with:
Internal compliance team

versus:

Share customer data with:
External third party

The Action is similar.

The consequence profile may differ substantially.

⸻

142. Risk and Jurisdiction

Where applicable, jurisdiction can affect consequence.

Example:

Data:
Customer PII
Recipient:
External processor
Jurisdiction:
Region A

versus:

Jurisdiction:
Region B

Risk Evaluation may therefore consume jurisdiction as a Context input where relevant.

Policy remains responsible for applicable legal or organizational requirements.

⸻

143. Risk and Sensitive Data

Sensitive data can increase Risk even for non-destructive Actions.

Examples:

Read
Export
Share
Publish
Transfer

Risk should therefore account for data sensitivity where material.

⸻

144. Risk and Public Visibility

Public exposure can substantially increase consequence.

Example:

Internal draft:
LOWER
Public publication:
HIGHER

Visibility is therefore a potential Risk factor.

⸻

145. Risk and Production State

Production status is often a major Risk factor.

Example:

Environment:
production
Action:
Delete
Resource:
Database

This combination may satisfy a deterministic Rule producing:

CRITICAL

The classification should be traceable to the underlying factors.

⸻

146. Risk and Incident State

Incident state may alter Risk.

Example:

IncidentActive = true

A normally routine deployment may therefore become high Risk.

The current state must be established as evidence.

⸻

147. Risk and Maintenance Windows

Maintenance windows may reduce certain operational risks.

Example:

Deployment:
Within approved maintenance window

versus:

Deployment:
Outside maintenance window

The Risk difference should be represented through explicit Rules where material.

⸻

148. Risk and Emergency Context

Emergency Context may alter the applicable Risk controls.

However:

Emergency Context must not automatically erase Risk.

An emergency may justify different Policy requirements, but the Risk classification remains a description of potential consequence.

⸻

149. Risk and Human Oversight

Human oversight is a control mechanism.

It does not convert:

CRITICAL

into:

LOW

The correct semantic model is:

Risk = CRITICAL
Required Control = Human Review
Review = Completed
Trust = Potentially Executable

⸻

150. Risk and Auditability

A consequential decision should preserve:

* Risk classification
* Risk categories
* Risk factors
* Risk Rules
* Risk Rule version
* Risk inputs
* Evidence references
* Mitigations
* Approvals
* Risk acceptance
* Final Trust decision
* evaluation timestamp

This allows an auditor to reconstruct why controls were required.

⸻

151. Risk Evaluation Observability

Useful metadata includes:

risk_evaluation_id
intent_id
intent_version
risk_rule_ids
risk_rule_versions
risk_classification
risk_categories
risk_factors
evidence_references
mitigation_requirements
timestamp
scope

Observability should support both operational debugging and historical reconstruction.

⸻

152. Risk Evaluation Identity

A Risk Evaluation should be associated with a specific semantic state.

Conceptually:

RiskEvaluation {
    evaluation_id
    intent_id
    intent_version
    inputs
    evidence
    rules
    classification
    mitigations
    evaluated_at
}

This makes Risk decisions reproducible and auditable.

⸻

153. Risk Result Provenance

A Risk result should allow Noema to answer:

Why was this Intent classified this way?

For example:

RiskClassification:
HIGH
Factors:
amount = ₦20M
resource_type = corporate_account
action = transfer
Rule:
financial-risk-v3
Evidence:
Account#123
Transfer#456

⸻

154. Risk Scores

A numerical Risk score may be useful operationally.

For example:

risk_score = 87

But:

A numerical score must not replace the semantic basis for the classification.

A score without interpretable factors and Rules is difficult to audit and govern.

⸻

155. Risk Scores Must Not Create False Precision

Noema should avoid implying that:

0.83

has objective meaning unless the scoring methodology defines it.

A semantic classification such as:

HIGH

must remain traceable to the factors and Rules that produced it.

⸻

156. Risk and Model Scores

Noema must keep:

Model confidence

separate from:

Risk score

They represent different things.

Model confidence:

How confident is the Model in its interpretation?

Risk:

How consequential could execution be?

⸻

157. Risk and Probabilistic Models

Probabilistic techniques may be useful in Risk analysis.

However, the canonical Trust result must preserve:

* the relevant assumptions
* evidence
* Rule or model version
* classification basis
* uncertainty
* mitigation requirements

A probabilistic model must not become an opaque substitute for Trust semantics.

⸻

158. Risk and Deterministic Classification

Where the relevant inputs and Rules are established:

Inputs
+
Evidence
+
Risk Rules
        ↓
Deterministic Classification

The same relevant inputs should produce the same canonical result.

⸻

159. Risk and Unresolved Probability

If a Risk Rule requires information that cannot be established, Noema should preserve the unresolved state.

Example:

Rule:
High-value transactions require elevated controls.
Amount:
UNKNOWN

Noema should not invent:

Amount = ₦1M

to force a low-risk result.

⸻

160. Risk and Policy Dependencies

Risk may be a Policy input.

Example:

Risk = HIGH
        ↓
Policy:
ApprovalRequired = true

The dependency should be explicit.

Risk does not directly invoke execution.

⸻

161. Risk and Mitigation Dependencies

Some mitigations may depend on other Trust decisions.

Example:

Risk:
CRITICAL
Required:
Human approval
Human approval:
Requires verified approver identity.

The resulting dependency chain should remain explicit.

⸻

162. Risk and Verification

Verification may reduce uncertainty or establish authority, but it does not necessarily reduce underlying Risk.

Example:

Identity verified:
TRUE
Risk:
CRITICAL

Verification establishes a Trust condition.

It does not transform the consequence profile.

⸻

163. Risk and Approval

Approval may authorize acceptance of Risk under Policy.

Example:

Risk:
HIGH
Policy:
Secondary approval required.
Approval:
GRANTED

The correct state is not:

Risk:
LOW

but:

Risk:
HIGH
Approval:
GRANTED

⸻

164. Risk and Confirmation

Confirmation establishes that the Actor explicitly accepts or reaffirms the requested Action where Policy requires it.

Example:

Risk:
HIGH
Policy:
Explicit confirmation required.
Confirmation:
RECEIVED

The Risk remains:

HIGH

⸻

165. Risk and Execution Contract

The final Execution Contract should preserve relevant Risk requirements.

Example:

ExecutionContract {
    intent_id: Intent#123
    action: DeleteResource
    resource: ProductionDatabase#123
    risk_classification: CRITICAL
    required_controls: [
        human_approval,
        backup_verified
    ]
}

The execution consumer should enforce the contract.

⸻

166. Risk and Consumer Responsibility

The execution consumer may enforce Risk-derived requirements but should not reinterpret the Risk classification.

For example:

Risk:
CRITICAL
Required:
Human approval

The consumer should not decide:

“The resource looks harmless, so I will execute.”

Consumer-side execution must remain bounded by the canonical Execution Contract.

⸻

167. Risk and Trust Boundary

The execution boundary should not be crossed merely because:

Capability = AVAILABLE

or:

Authorization = ALLOWED

The relevant Risk controls must also be satisfied.

⸻

168. Risk and Noema’s Autonomy Model

Risk provides a principled input into the distinction between:

understood

and:

safe to execute autonomously

An Agent may understand an Intent perfectly while still being prohibited from executing it autonomously because its Risk exceeds the applicable autonomy boundary.

⸻

169. Risk and Bounded Autonomy

A bounded-autonomy model may conceptually operate as:

Resolved Intent
      ↓
Risk Classification
      ↓
Autonomy Boundary
      ↓
Required Controls
      ↓
Trust
      ↓
Execution Contract
      ↓
Consumer Execution

This allows Noema to express:

AUTONOMOUS

without implying that all technically executable Actions are autonomous.

⸻

170. Risk and Prohibition

Some Actions may be prohibited regardless of Risk classification.

Example:

Policy:
Action prohibited.

Risk does not override the prohibition.

Conversely, a high-risk Action may be permissible under explicit authority and controls.

Therefore:

High Risk ≠ Automatically Prohibited

and:

Low Risk ≠ Automatically Permitted

⸻

171. Risk and Proportionality

Risk controls should be proportional to the potential consequence.

Low-consequence Actions should not automatically require the same controls as irreversible, high-impact Actions.

Conversely, high-consequence Actions should not receive weak controls merely because their execution is technically simple.

⸻

172. Risk and Over-Control

Noema should avoid using Risk as a justification for arbitrary restrictions.

A Risk requirement should be traceable to:

Risk Factor
+
Evidence
+
Risk Rule

This supports explainable and governable autonomy.

⸻

173. Risk and Under-Control

Noema should also avoid allowing low apparent Risk to mask material unknowns.

Example:

Resource Criticality:
UNKNOWN

must not automatically become:

LOW

Unknown material factors must remain unresolved.

⸻

174. Risk and Materiality

Not every unknown matters equally.

Example:

Resource color:
UNKNOWN

may be irrelevant.

But:

Resource environment:
UNKNOWN

may be critical if production status changes the Risk classification.

Risk Evaluation should therefore focus on material Risk inputs.

⸻

175. Risk and Semantic Completeness

Risk Evaluation does not require every possible property of an Intent to be known.

It requires sufficient resolution of the properties that materially affect Risk.

This is consistent with Noema’s broader principle of resolving what matters for the decision being made.

⸻

176. Risk and Consequence Graph

For complex Actions, Risk may be derived from an effect structure.

Conceptually:

Intent
  ↓
Action
  ↓
Direct Effects
  ↓
Dependent Effects
  ↓
External Effects
  ↓
Potential Consequences

This allows Risk Evaluation to account for consequences beyond the immediate Resource mutation.

⸻

177. Risk and Side-Effect Graph

Example:

Delete Account
      ↓
Disable Login
      ↓
Cancel Subscription
      ↓
Terminate Services
      ↓
External Customer Impact

The Risk model should preserve materially consequential downstream effects where they are established.

⸻

178. Risk and Unknown Effects

If material downstream effects are unknown, the Risk result may remain unresolved.

Noema should not assume:

No known side effects = No side effects

Absence of evidence is not automatically evidence of low Risk.

⸻

179. Risk and Capability Semantics

Capability metadata may establish known properties of an Action.

Example:

Capability:
DeleteAccount
Properties:
reversible = false
external_effect = true
idempotent = false

These properties may be consumed by Risk Rules.

The Capability itself does not determine whether the Action is allowed.

⸻

180. Risk and Action Semantics

Actions should expose semantic properties where relevant.

Example:

Delete:
destructive = true
state_changing = true
potentially_irreversible = true

Risk Evaluation combines these with Resource and Context.

⸻

181. Risk and Resource Semantics

Resources should expose risk-relevant properties where appropriate.

Example:

ProductionDatabase:
criticality = critical
environment = production
contains_sensitive_data = true
recoverability = verified_backup

These become inputs to Risk Evaluation.

⸻

182. Risk and Context Semantics

Context should expose relevant environmental state.

Example:

incident_active = true
maintenance_window = false
emergency_mode = false

Risk Rules can then evaluate these properties deterministically.

⸻

183. Risk and Evidence Authority

Risk-relevant evidence should come from authoritative or sufficiently trusted sources.

Example:

Production status

should preferably come from the system that governs deployment state rather than from an unverified conversational assertion.

⸻

184. Risk and Evidence Conflict

If authoritative sources disagree about a material Risk factor, the Risk result should not silently choose one.

Example:

Deployment System:
production
Inventory System:
staging

If environment determines Risk, the conflict requires reconciliation or an explicit conflict rule.

⸻

185. Risk and Risk Rule Conflict

If two Risk Rules produce incompatible classifications:

Rule A:
Risk = HIGH
Rule B:
Risk = CRITICAL

Noema requires an explicit aggregation or precedence mechanism.

Possible mechanisms include:

* maximum severity
* explicit precedence
* category-specific aggregation
* domain-defined conflict rules

The mechanism must be deterministic.

⸻

186. Risk Rule Precedence

Risk Rules may exist at different scopes.

For example:

Global Risk Rule
      ↓
Organization Risk Rule
      ↓
Tenant Risk Rule
      ↓
Resource Risk Rule
      ↓
Action-specific Risk Rule

The hierarchy is domain-dependent.

The key principle is:

Risk Rule precedence must be explicit rather than determined by Model preference.

⸻

187. Risk Rule Exceptions

Risk Rules may define explicit exceptions.

Example:

Default:
Production deployment during incident = CRITICAL
Exception:
Emergency incident-response deployment under approved emergency procedure.

The exception must itself be explicit and governed.

Noema should not infer exceptions from conversational context.

⸻

188. Risk Rule Parameters

Risk Rules may contain parameters.

Example:

financial_risk_threshold = ₦10M
critical_blast_radius = 10000

Risk Evaluation should resolve these parameters from authoritative configuration.

⸻

189. Risk Rule Mutation

A Model must not silently mutate Risk Rules.

Example:

Risk Rule:
Transfers > ₦10M = HIGH

Model:

“This particular transfer seems safe.”

does not modify the Rule.

Risk Rule changes require explicit governance.

⸻

190. Risk and Policy Governance

Risk Rules and Policies may interact, but they remain separately governed artifacts.

Example:

Risk Rule:
Production deletion = CRITICAL
Policy:
Critical Actions require human approval

Changing either artifact should be independently auditable.

⸻

191. Risk and Intent Lifecycle

Risk may change throughout an Intent lifecycle.

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

* Resource state
* Amount
* Scope
* Context
* Policy
* Actor authority
* Risk Rules
* Time

may change Risk.

⸻

192. Risk Evaluation Across Lifecycle States

A Risk result should be associated with the semantic state against which it was evaluated.

Example:

Intent#123 v1
RiskEvaluation#456
Risk = HIGH

If the Intent becomes:

Intent#123 v2

because its amount changes, a new Risk Evaluation may be required.

⸻

193. Risk and Approval Expiration

Approval does not necessarily remain valid indefinitely.

If the Risk-relevant state changes, the approval may no longer satisfy current Trust requirements.

Example:

Approval:
09:00
Incident begins:
10:00
Execution:
11:00

Revalidation may be required.

⸻

194. Risk and Time-Bounded Controls

Risk mitigations may themselves have validity periods.

Example:

Human approval valid for:
30 minutes

After expiration, Trust may require revalidation.

⸻

195. Risk and Idempotent Evaluation

Risk Evaluation itself should be safe to repeat.

Evaluating:

Intent#123

twice should not alter Risk state merely because evaluation occurred twice.

Evaluation should preferably be side-effect free.

⸻

196. Risk and Audit Reconstruction

A future auditor should be able to determine:

* What was the Intent?
* Which version?
* What Action was involved?
* Which Resources were affected?
* What was the Context?
* Which Risk factors were identified?
* What evidence supported them?
* Which Rules applied?
* Which versions?
* What classification resulted?
* What mitigations were required?
* Were they satisfied?
* What Trust decision followed?
* What actually happened?

This is part of trustworthy execution.

⸻

197. Canonical Risk Evaluation Flow

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
                Resolve Risk Inputs
                       │
                       ▼
                Load Risk Rules
                       │
                       ▼
               Evaluate Risk Rules
                       │
              ┌────────┼──────────┐
              │        │          │
           Classified Unresolved Conflict
              │        │          │
              ▼        ▼          ▼
        Classification Resolve   Reconcile
              │        │          │
              └────────┴──────────┘
                       │
                       ▼
              Determine Mitigations
                       │
                       ▼
                 Policy Evaluation
                       │
                       ▼
                 Trust Decision
                       │
                       ▼
              Execution Contract
                       │
                       ▼
              Risk Revalidation
                       │
                       ▼
                    Execute

⸻

198. Canonical Risk Object

Conceptually:

RiskEvaluation {
    evaluation_id
    intent_id
    intent_version
    classification
    categories
    factors
    evidence
    risk_rules
    risk_rule_versions
    mitigation_requirements
    evaluated_at
    valid_until
    status
}

The exact schema is implementation-specific.

The semantic requirements are canonical.

⸻

199. Canonical Risk Result

A Risk Result should conceptually distinguish:

classification
status
factors
evidence
rules
mitigations

For example:

RiskResult {
    status: CLASSIFIED
    classification: HIGH
    factors: [
        high_transaction_value,
        external_financial_effect,
        limited_reversibility
    ]
    rule: financial-risk-v3
    mitigations: [
        secondary_approval
    ]
}

⸻

200. Risk Classification vs Mitigation

These must remain distinct.

Example:

Risk Classification:
CRITICAL
Mitigation:
Human approval required.

The mitigation does not rewrite the classification.

This distinction preserves auditability.

⸻

201. Risk Classification vs Trust Result

These must also remain distinct.

Example:

Risk:
HIGH
Policy:
Satisfied
Authorization:
Allowed
Capability:
Available
Required approval:
Granted
Trust:
ALLOW

The Risk remains:

HIGH

⸻

202. Risk and Final Trust Decision

Conceptually:

Intent
+
Evidence
+
Authorization
+
Policy
+
Capability
+
Constraints
+
Risk
+
Mitigations
        ↓
Trust

The Trust Engine integrates these dimensions.

Risk does not make the final decision independently.

⸻

203. Risk and Execution Outcome

The canonical relationship is:

Risk
  ↓
Trust
  ↓
Execution
  ↓
Outcome

Risk describes potential consequence.

Trust determines whether execution conditions are satisfied.

Execution produces the actual Outcome.

⸻

204. Risk and Noema’s Core Thesis

Noema exists to turn ambiguous human Intent into safe, executable Intent.

Risk provides the semantic distinction between:

understood

and:

safe to execute autonomously

An Intent can be completely understood without being appropriate for autonomous execution.

That distinction is fundamental to Noema.

⸻

205. Canonical Invariants

Invariant 1

Risk is distinct from Uncertainty, Model Confidence, Authorization, Capability, Policy, Constraints, and Outcome.

Invariant 2

Risk Evaluation operates on resolved semantic objects rather than raw natural language.

Invariant 3

Risk Classification should be deterministic given the same relevant inputs, evidence, and Risk Rules.

Invariant 4

Risk must be grounded in identifiable factors and, where material, supporting evidence.

Invariant 5

Risk concerns potential consequence and likelihood where those dimensions are meaningfully established.

Invariant 6

Risk is about consequence, not merely whether an Action mutates state.

Invariant 7

Risk should account for scope, impact, reversibility, blast radius, Resource criticality, Context, and other materially relevant factors.

Invariant 8

High Risk does not automatically mean prohibited.

Invariant 9

Low Risk does not automatically mean authorized or executable.

Invariant 10

Risk does not grant or revoke Authorization.

Invariant 11

Risk does not create or replace Capability.

Invariant 12

Risk does not silently modify an Actor’s Intent.

Invariant 13

Risk mitigation must be explicit and auditable.

Invariant 14

Risk acceptance does not erase or lower the underlying Risk Classification.

Invariant 15

Material changes to Intent, Context, Resource state, Actor authority, Evidence, Policy, or Risk Rules may require Risk re-evaluation.

Invariant 16

Risk decisions must identify the material Risk Rule version where applicable.

Invariant 17

Missing material Risk evidence must not produce an implicit low-risk classification.

Invariant 18

Conflicting material Risk evidence requires explicit reconciliation or an unresolved state.

Invariant 19

Conflicting Risk Rules require explicit precedence or aggregation semantics.

Invariant 20

Composite Intents must preserve material Risk differences between constituent Actions.

Invariant 21

Risk Classification must remain distinct from mitigation and Trust outcome.

Invariant 22

Risk requirements should be proportional to potential consequence.

Invariant 23

Risk Evaluation should be repeatable and preferably side-effect free.

Invariant 24

Stale Risk decisions must not authorize execution when relevant Risk inputs have changed.

Invariant 25

Risk explanations should be derivable from explicit factors, evidence, and Rules rather than Model-generated judgment.

Invariant 26

Consumer-side execution must enforce Risk-derived requirements represented in the Execution Contract.

Invariant 27

Risk does not override Policy, Authorization, Capability, Evidence, or other Trust requirements.

Invariant 28

Risk acceptance or human approval changes the Trust conditions but does not change the underlying Risk Classification.

⸻

206. The Fundamental Distinction

The essential distinction is:

Intent:
"What does the Actor want?"
Authorization:
"May this Actor perform the Action?"
Policy:
"Under what conditions may it happen?"
Capability:
"Can the system or consumer perform it?"
Risk:
"What could happen if it happens, and how consequential could that be?"
Mitigation:
"What additional controls are required?"
Trust:
"Is the Intent ready and permitted to cross the execution boundary?"
Execution:
"What actually happened when the Action was attempted?"
Outcome:
"What was the resulting state?"

Risk answers only its part of this chain.

⸻

207. Final Definition

Risk is the structured assessment of the potential for an Intent or its execution to produce undesirable consequences, considering the Action, Resources, Context, Actor, scope, reversibility, likelihood, expected effects, and other material factors, using explicit evidence and Risk Rules.

Risk Evaluation produces an explicit Risk Classification and, where applicable, mitigation requirements that contribute to Noema’s final Trust decision.

The shortest canonical formulation is:

Risk does not determine whether an Intent is allowed; it determines how consequential execution could be and what level of control may be required before Noema permits the Intent to proceed.