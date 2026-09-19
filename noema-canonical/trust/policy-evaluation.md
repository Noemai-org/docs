Policy Evaluation

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/policy-evaluation.md

⸻

1. Definition

Policy Evaluation is the deterministic process by which Noema determines which Policies apply to a resolved Intent and whether the Intent satisfies the conditions imposed by those Policies.

Policy Evaluation answers:

“Given the established Intent, the relevant Actor, Resources, Context, Evidence, and applicable Policies, under what conditions may this Intent proceed?”

Policy Evaluation is distinct from:

* Intent Resolution
* Evidence
* Authorization
* Capability
* Constraints
* Risk
* Execution
* Trust

but contributes directly to the final Trust decision.

Policy Evaluation does not determine what the Actor meant.

It determines the conditions under which an already-established Intent may proceed.

⸻

2. The Core Principle

Policies constrain what may happen.

They do not determine what the Actor intended.

For example, the Actor may express:

“Move $5,000 from savings to checking.”

The Model may interpret that expression.

Noema should resolve it into a semantic representation such as:

TransferFunds(
    actor = User#123,
    source = Account#Savings,
    destination = Account#Checking,
    amount = $5,000
)

Policy Evaluation should operate on that resolved semantic representation rather than on the original natural-language expression.

The fundamental sequence is:

Actor Expression
      ↓
Interpretation
      ↓
Intent Resolution
      ↓
Resolved Intent
      ↓
Policy Applicability
      ↓
Policy Evaluation

⸻

3. Policy Evaluation in the Trust Model

Policy Evaluation participates in the broader Trust pipeline:

Actor Expression
      ↓
Intent Interpretation
      ↓
Intent Resolution
      ↓
Evidence
      ↓
Authorization
      ↓
Policy Evaluation
      ↓
Capability
      ↓
Constraints
      ↓
Risk
      ↓
Trust Decision
      ↓
Execution Boundary
      ↓
Execution
      ↓
Outcome

These components have different responsibilities.

Intent
"What does the Actor want?"
Evidence
"What claims are sufficiently established?"
Authorization
"May this Actor perform this Action?"
Policy
"Under what conditions may it happen?"
Capability
"Can the intended Action be performed?"
Constraints
"What conditions restrict the resolved Intent?"
Risk
"What consequence-sensitive requirements apply?"
Trust
"Is the Intent sufficiently established, permitted,
and ready to cross the execution boundary?"

Noema should not collapse these questions into one generic decision.

⸻

4. Policy Evaluation Is Downstream of Resolution

Policy Evaluation should operate on established semantic objects.

It should not be responsible for resolving:

* ambiguous Actors
* ambiguous Resources
* ambiguous Actions
* unresolved parameters
* uncertain relationships
* natural-language references

For example:

Actor:
"Transfer money to John."

If John has not been resolved to a canonical Resource or Account, Policy Evaluation should not invent the identity.

Instead:

Destination = UNKNOWN
        ↓
Policy-relevant input incomplete
        ↓
UNRESOLVED

Resolution precedes Policy Evaluation where the Policy depends on the unresolved value.

⸻

5. Policy vs Authorization

Policy and Authorization are related but distinct.

Authorization

Authorization answers:

“May this Actor perform this Action on this Resource?”

Example:

User#123
may perform:
TransferFunds
on:
Account#456

Policy

Policy answers:

“Under what conditions may this Action occur?”

Example:

Transfers above ₦10,000,000
require secondary approval.

An Actor may therefore be authorized while the particular Intent remains blocked by Policy.

Example:

Authorization:
ALLOW
Policy:
REQUIRE_APPROVAL

The resulting Trust state is not executable yet.

⸻

6. Policy vs Capability

Capability answers:

“Can the system or consumer perform this Action?”

Policy answers:

“Is this Action permitted under the applicable rules, and under what conditions?”

Example:

Capability:
PaymentProvider#X supports RefundPayment.
Policy:
Refunds after 30 days require manager approval.

The existence of a Capability does not establish permission.

Capability does not override Policy.

⸻

7. Policy vs Constraints

Constraints restrict an Intent, its parameters, or the conditions under which it may proceed.

Example:

Constraint:
Transfer amount must not exceed account limit.
Policy:
Transfers above ₦5,000,000 require approval.

These may overlap operationally, but they have distinct semantic roles.

A Constraint describes a restriction.

A Policy defines a governing rule under which an Intent may or may not proceed.

⸻

8. Policy Is Not Model Judgment

Noema must not reduce Policy Evaluation to:

Model:
"This seems allowed."

Instead:

Resolved Intent
      ↓
Applicable Policies
      ↓
Policy Rules
      ↓
Authoritative Inputs
      ↓
Deterministic Evaluation
      ↓
Policy Result

A Model may assist with:

* discovering candidate Policies
* extracting structured parameters
* identifying potentially relevant Policy domains

But Model output does not itself establish the Policy result.

The Policy Evaluation mechanism determines the result.

⸻

9. Policy Applicability

Before evaluating a Policy, Noema must establish whether that Policy applies to the Intent.

Policy applicability may depend on:

* Actor
* Actor type
* Action
* Resource
* Resource type
* Tenant
* Organization
* Jurisdiction
* Context
* Amount
* Risk
* Time
* Environment
* Intended Outcome
* Business state

The conceptual sequence is:

Resolved Intent
      ↓
Determine Policy Scope
      ↓
Determine Applicability
      ↓
Evaluate Applicable Policies

A Policy that does not apply must not be treated as though it were evaluated and satisfied.

⸻

10. Policy Applicability vs Policy Satisfaction

These are distinct states.

A Policy may be:

NOT_APPLICABLE

because it does not govern the Intent.

A Policy may instead be:

SATISFIED

because it applies and all of its conditions are satisfied.

For example:

Policy:
International transfers require additional verification.
Intent:
TransferFunds(
    source_country = Nigeria,
    destination_country = Nigeria
)
Result:
NOT_APPLICABLE

This is different from:

Policy:
International transfers require additional verification.
Intent:
TransferFunds(
    source_country = Nigeria,
    destination_country = United Kingdom
)
Verification:
completed
Result:
SATISFIED

⸻

11. Policy Evaluation Inputs

Conceptually:

PolicyEvaluation {
    Intent
    Actor
    Resources
    Context
    Evidence
    Authorization
    Capabilities
    ApplicablePolicies
}

The exact implementation schema is not canonical.

The semantic requirement is that Policy Evaluation operate over established inputs rather than raw language.

Where a Policy depends on a fact, that fact should be supported by appropriate Evidence.

⸻

12. Policy Evaluation as a Deterministic Function

Conceptually:

PolicyResult =
    evaluate(
        Intent,
        Actor,
        Context,
        Evidence,
        ApplicablePolicies
    )

Given the same material inputs, Policy versions, and evaluation semantics, Policy Evaluation should produce the same result.

If the result changes, Noema should be able to identify which relevant input changed.

Possible changes include:

* Intent version
* Actor state
* Resource state
* Evidence
* Context
* Policy version
* Policy applicability
* Approval state
* Risk state

⸻

13. Policy Results

Policy Evaluation should produce explicit semantic results.

Useful conceptual results include:

ALLOW
DENY
REQUIRE_APPROVAL
REQUIRE_CONFIRMATION
REQUIRE_VERIFICATION
NOT_APPLICABLE
UNRESOLVED
CONFLICTING

The exact implementation enum is not canonical.

The important principle is that Policy Evaluation should not collapse materially different conditions into a simple binary:

YES / NO

For example:

REQUIRE_APPROVAL

is not equivalent to:

DENY

and:

UNRESOLVED

is not equivalent to:

ALLOW

⸻

14. Allow

ALLOW means the applicable Policy requirements represented by the evaluation have been satisfied.

Example:

Intent:
ViewProject(Project#123)
Policy:
Project members may view projects.
Evidence:
User#123 is a member of Project#123.
Result:
ALLOW

ALLOW does not necessarily mean the overall Trust decision is ALLOW.

Authorization, Capability, Constraints, Risk, and other Trust requirements may still need to be satisfied.

⸻

15. Deny

DENY means an applicable Policy prohibits the Intent from proceeding under the evaluated conditions.

Example:

Intent:
DeleteProductionDatabase(Database#123)
Policy:
Only production administrators may perform destructive operations.
Actor:
Developer
Result:
DENY

A DENY Policy result should prevent the Intent from crossing the execution boundary unless an explicit and authorized Policy mechanism changes the governing conditions.

⸻

16. Require Approval

Example:

Intent:
Transfer ₦20,000,000
Policy:
Transfers > ₦10,000,000 require secondary approval.
Result:
REQUIRE_APPROVAL

This does not necessarily mean the Intent is prohibited.

It means the Intent has not yet satisfied a Policy requirement necessary for execution.

The required approval becomes additional evidence when obtained.

⸻

17. Require Confirmation

Example:

Intent:
Delete Account#123
Policy:
Account deletion requires explicit Actor confirmation.
Result:
REQUIRE_CONFIRMATION

The Intent may already be:

* resolved
* authorized
* policy-applicable
* otherwise valid

but still require explicit confirmation.

Confirmation must be bound to the exact Intent version being confirmed.

⸻

18. Require Verification

Example:

Intent:
Change payout destination.
Policy:
Payout destination changes require verified identity.
Result:
REQUIRE_VERIFICATION

The Actor may have sufficient authorization while still lacking the verification required by Policy.

⸻

19. Not Applicable

A Policy may be evaluated and determined not to govern the Intent.

Example:

Policy:
International transfer verification.
Intent:
Domestic transfer.
Result:
NOT_APPLICABLE

NOT_APPLICABLE does not mean the Policy was satisfied.

It means the Policy does not govern the evaluated Intent.

⸻

20. Unresolved

Policy Evaluation may depend on information that has not yet been established.

Example:

Policy:
Transfers above ₦10,000,000 require approval.
Intent:
Transfer "a large amount."

The amount is unresolved.

Noema cannot determine whether the threshold has been crossed.

Result:

UNRESOLVED

The appropriate next step may be:

* clarification
* evidence retrieval
* Intent resolution
* additional verification

rather than an implicit ALLOW.

⸻

21. Conflicting Policy Inputs

A Policy may depend on Evidence that is itself conflicting.

Example:

CRM:
User#123 owns Account#456
Ledger:
User#789 owns Account#456

Policy:

Only account owners may withdraw.

The Policy cannot safely produce ALLOW until the relevant ownership conflict is resolved.

The result may therefore be represented as:

CONFLICTING

or another explicit unresolved state.

Noema should not arbitrarily select one source merely to complete the evaluation.

⸻

22. Policy Composition

Multiple Policies may apply simultaneously.

Example:

Policy A:
Actor must be authorized.
Policy B:
Amount > ₦10,000,000 requires approval.
Policy C:
International transfers require verification.

An Intent may produce:

Authorization:
ALLOW
Policy B:
REQUIRE_APPROVAL
Policy C:
REQUIRE_VERIFICATION

The final Trust state must account for all material applicable requirements.

Policy Evaluation should preserve the individual Policy results rather than collapsing them prematurely.

⸻

23. Mandatory Policy Conjunction

When multiple mandatory Policies apply, all required conditions must be satisfied.

Example:

Policy A = SATISFIED
Policy B = SATISFIED
Policy C = SATISFIED

then:

Policy Evaluation = SATISFIED

But:

Policy A = SATISFIED
Policy B = DENIED
Policy C = SATISFIED

means the Intent cannot proceed under those Policies.

Similarly:

Policy A = SATISFIED
Policy B = REQUIRE_APPROVAL
Policy C = SATISFIED

means the Intent remains blocked pending the required approval.

⸻

24. Policy Exceptions

Policies may define explicit exceptions.

Example:

Default:
Refunds after 30 days are prohibited.
Exception:
Fraud-related refunds may bypass the 30-day restriction.

The exception must itself be explicit and governed.

Noema should not infer exceptions merely because conversational context appears to justify them.

An Actor request such as:

“Ignore the refund policy because this is an emergency.”

does not itself establish a Policy exception.

⸻

25. Policy Precedence

When multiple Policies govern the same Intent, Noema requires an explicit precedence model where their requirements interact.

A conceptual hierarchy might be:

Global Policy
      ↓
Organization Policy
      ↓
Tenant Policy
      ↓
Resource Policy
      ↓
Intent-specific Policy

The actual hierarchy is domain-dependent.

The canonical principle is:

Policy precedence must be explicit rather than determined by Model preference.

⸻

26. Policy Conflict

Policies may produce incompatible requirements.

Example:

Policy A:
ALLOW
Policy B:
DENY

Noema must not arbitrarily choose one.

Possible deterministic mechanisms include:

* explicit precedence
* deny-overrides
* allow-overrides
* policy hierarchy
* conflict escalation
* domain-specific resolution

The governing mechanism must itself be explicit.

If no governing conflict rule exists, the appropriate state may be:

UNRESOLVED

rather than an arbitrary decision.

⸻

27. Deny-by-Default for Consequential Operations

For consequential operations:

If a required Policy condition cannot be established as satisfied, Noema should not assume that the Intent is permitted.

Conceptually:

Required condition
      ↓
UNKNOWN
      ↓
NOT EXECUTABLE

This does not mean every unknown Policy must globally become DENY.

It means uncertainty must not silently become permission for a consequential execution.

⸻

28. Policy Conditions

Policies should be expressible in terms of canonical concepts.

Example:

IF
    Action = TransferFunds
AND
    Amount > ₦10,000,000
THEN
    SecondaryApprovalRequired

The Policy operates on structured semantic properties of the Intent and its relevant context.

⸻

29. Policy Conditions Must Be Typed

Policy conditions should use typed values where possible.

Prefer:

amount > 10_000_000 NGN

over:

"large transfer"

Typed conditions reduce semantic ambiguity and improve deterministic evaluation.

Other typed values may include:

* currency
* duration
* timestamp
* Actor
* Resource
* Resource type
* jurisdiction
* environment
* role
* risk level
* status

⸻

30. Policy Parameters

Policies may contain parameters.

Example:

max_transfer_amount = ₦5,000,000
approval_threshold = ₦10,000,000

Policy parameters should come from an authoritative configuration mechanism.

They should not be silently invented or modified by Model output.

⸻

31. Policy Versioning

Policies change over time.

Therefore a material Policy Evaluation should identify the Policy version used.

Example:

refund-policy-v4

rather than merely:

refund-policy

This supports:

* auditability
* reproducibility
* historical analysis
* debugging
* deterministic re-evaluation

A Policy version is part of the semantic basis of the decision.

⸻

32. Policy Activation

Policies may have an effective time.

Example:

Policy v2:
effective_from = 2026-09-01

Before that time:

v1

After that time:

v2

Time must therefore be treated as an explicit evaluation input when Policy validity depends on it.

⸻

33. Policy Expiration

Policies may expire.

Example:

PromotionalRefundPolicy:
valid_until = 2026-12-31

After expiration, the Policy must not silently remain applicable.

The applicable Policy set must be determined using the relevant evaluation time.

⸻

34. Policy Scope

Policies should explicitly define their scope where relevant.

Possible scopes include:

* Tenant
* Organization
* Region
* Jurisdiction
* Resource
* Resource type
* Actor class
* Action
* Environment
* Channel

A Policy applying to:

Tenant#A

must not automatically govern:

Tenant#B

⸻

35. Policy Context

Policy Evaluation may depend on Context.

Examples include:

* time
* location
* environment
* transaction channel
* device trust
* risk level
* business state
* incident status

Example:

Policy:
Production deployments are prohibited during incident freeze.
Context:
IncidentFreeze = ACTIVE

The current Context becomes an input to Policy Evaluation.

⸻

36. Policy and Context Changes

If relevant Context changes before execution, the Policy result may change.

Example:

09:00:
Deployments allowed.
09:30:
Incident freeze activated.
09:31:
Deployment attempted.

The current Policy result may be:

DENY

This remains deterministic because the evaluation input changed.

The previous result does not automatically remain valid merely because it was previously ALLOW.

⸻

37. Policy and Evidence

Policy Evaluation depends on Evidence when Policy conditions concern facts external to the Policy itself.

Example:

Policy:
Only account owners may transfer funds.
Evidence:
User#123 owns Account#456.

The Policy can then evaluate the condition.

Without that Evidence:

Ownership = UNKNOWN

there is insufficient basis for an ALLOW decision.

Evidence establishes the relevant fact.

Policy determines what that fact means under the governing rule.

⸻

38. Policy and Authorization

Authorization and Policy may consume the same Evidence while answering different questions.

Example:

Evidence:
User#123 is FinanceManager.

Authorization:

FinanceManager may approve expenses.

Policy:

Expenses above ₦10M require FinanceManager approval.

The same Evidence supports different semantic evaluations.

⸻

39. Policy and Capability

A Policy may constrain use of an available Capability.

Example:

Capability:
DeleteUser
Policy:
DeleteUser may only be used in non-production environments.

The Capability exists.

The Policy determines when that Capability may be exercised.

⸻

40. Policy and Constraints

A Policy may impose a Constraint.

Example:

Policy:
Transfers above ₦5M require approval.

The resulting Policy requirement may be represented as:

ApprovalRequired = true

The resulting condition should remain traceable to the governing Policy.

⸻

41. Policy and Risk

Policy requirements may vary according to Risk.

Example:

Risk:
HIGH
Policy:
High-risk actions require explicit confirmation.

Risk may therefore become an input to Policy Evaluation.

Conversely, Policy may itself define conditions that contribute to Risk.

The two concepts should remain semantically distinct even where they interact.

⸻

42. Policy and Intent Composition

Composite Intents may trigger multiple Policies.

Example:

RefundPayment(Payment#123)
AND
CloseAccount(Account#456)

Applicable Policies may include:

RefundPolicy
AccountClosurePolicy

Each child Intent should be evaluated against its applicable Policies.

Evidence sufficient for one child Intent does not automatically satisfy the Policies of another.

⸻

43. Policy Dependencies

Some Policies depend on other conditions or decisions.

Example:

Policy A:
Only verified users may transfer funds.
Policy B:
International transfers require verification.

A dependency chain may therefore exist:

Verification
      ↓
Policy B satisfied
      ↓
Transfer Policy satisfied

Dependencies should be explicit.

Noema should not rely on an implicit reasoning chain hidden inside Model output.

⸻

44. Policy Preconditions

A Policy may define preconditions.

Example:

To refund:
Order.status = PAID

If:

Order.status = PENDING

the condition fails.

If:

Order.status = UNKNOWN

the Policy may be unresolved.

The distinction is important:

FALSE

is not the same as:

UNKNOWN

⸻

45. Policy Postconditions

Policies may also define conditions expected after execution.

Example:

After AccountClosure:
Account.status = INACTIVE

Postconditions are useful for validating execution outcomes.

They are distinct from pre-execution Policy conditions and do not themselves prove that execution succeeded.

⸻

46. Policy vs Execution Outcome

Policy Evaluation predicts whether an Intent may proceed under applicable rules.

Execution determines what actually happened.

Example:

Policy:
Refund allowed.
Trust:
ALLOW.
Execution:
Payment provider timeout.
Outcome:
FAILED.

Policy satisfaction does not guarantee the intended Outcome.

Similarly:

Policy:
ALLOW.
Execution:
SUCCESS.

does not mean the Policy caused the successful outcome.

The semantic layers remain distinct.

⸻

47. Policy Evaluation and Execution

The typical sequence is:

Resolve
  ↓
Evaluate Policy
  ↓
Trust
  ↓
Create Execution Contract
  ↓
Execute
  ↓
Observe Outcome

The execution consumer should receive the established Policy requirements.

It should not reinterpret Policy from the original natural-language request.

⸻

48. Policy Enforcement

A Policy Evaluation result must be enforceable.

If:

Policy = DENY

the execution path must not continue.

If:

Policy = REQUIRE_APPROVAL

execution should remain blocked until the required condition is satisfied.

If:

Policy = REQUIRE_VERIFICATION

the execution path must not treat ordinary authorization as sufficient.

Policy Evaluation therefore produces requirements that must be respected at the execution boundary.

⸻

49. Policy Decision vs Policy Enforcement

These concepts remain distinct.

Evaluation

Determines:

“What does the Policy require?”

Enforcement

Ensures:

“Is that requirement actually respected?”

Noema may perform Policy Evaluation while an execution consumer participates in enforcement.

The execution consumer must not reinterpret the Policy.

⸻

50. Policy Evaluation and Consumer-Side Execution

An Execution Contract may communicate Policy requirements explicitly.

Example:

ExecutionContract {
    action: TransferFunds
    amount: ₦20,000,000
    policy_status: approval_required
    required_approvals: 2
}

The consumer should not need to rediscover the governing Policy from natural language.

Policy requirements should cross the execution boundary as structured semantics.

⸻

51. Policy Decision Provenance

A material Policy result should be traceable to:

* Policy identity
* Policy version
* Policy scope
* Applicability conditions
* Policy conditions
* Evidence references
* Evaluation context
* Evaluation time
* Evaluation result

Example:

Policy:
large-transfer-v3
Condition:
amount > ₦10M
Evidence:
amount = ₦20M
Result:
REQUIRE_APPROVAL

The provenance chain should allow a later reviewer to understand why the Policy produced that result.

⸻

52. Policy Evaluation Must Be Explainable

A useful explanation should answer:

* Which Policy applied?
* Why did it apply?
* Which version was used?
* Which conditions were evaluated?
* Which conditions were satisfied?
* Which conditions failed?
* What evidence supported those conditions?
* What must happen next?

Example:

“This transfer requires secondary approval because the amount exceeds the ₦10,000,000 approval threshold.”

The explanation should derive from the structured Policy evaluation.

⸻

53. Policy Explanation Must Not Depend on Model Reasoning

The system should not require:

"Ask the Model why it decided this."

The Policy Evaluation mechanism should already know:

Policy
Condition
Evidence
Scope
Version
Result
Requirement

A Model may render the explanation into natural language, but it should not be the authoritative source of the explanation.

⸻

54. Policy Evaluation and Determinism

Policy Evaluation is one of the strongest deterministic components of Noema.

Conceptually:

Intent
+ Evidence
+ Applicable Policy Version
+ Scope
+ Context
        ↓
Deterministic Evaluation
        ↓
Policy Result

Given the same material inputs and evaluation semantics, the same Policy result should be produced.

⸻

55. Policy Evaluation and Ambiguity

If a Policy-relevant value is ambiguous, Policy Evaluation cannot safely complete.

Example:

Policy:
Transfers > ₦10M require approval.
Intent:
"Transfer a large amount."

Amount is unresolved.

Result:

UNRESOLVED

Noema should resolve the ambiguity before making a final Trust decision.

⸻

56. Policy Evaluation and Missing Evidence

Example:

Policy:
Only account owners may withdraw.
Evidence:
Account owner = UNKNOWN.

Result:

UNRESOLVED

not:

ALLOW

Noema should retrieve appropriate Evidence or request clarification where possible.

⸻

57. Policy Evaluation and Conflicting Evidence

Example:

CRM:
User#123 owns Account#456
Ledger:
User#789 owns Account#456

Policy:

Only owners may withdraw.

The Policy cannot be deterministically evaluated until the material conflict is resolved.

The result should therefore preserve the unresolved condition rather than selecting a source arbitrarily.

⸻

58. Policy Evaluation and Natural-Language Policies

Natural-language Policy definitions may be useful for humans.

However, consequential Policy Evaluation should ultimately operate over structured semantics.

Human Policy:

“Large transfers should receive additional approval.”

should be formalized into something conceptually like:

IF
    amount > threshold
THEN
    approval_required

The exact Policy language may evolve.

The canonical requirement is:

Consequential Policies must have machine-evaluable semantics.

⸻

59. Policy Language

Noema may eventually define or adopt a typed Policy Language.

A Policy should conceptually express:

Scope
Applicability
Conditions
Requirements
Exceptions
Precedence
Effective Period
Evaluation Semantics

Example:

Policy {
    applies_to: TransferFunds
    when: amount > 10_000_000
    requires: SecondaryApproval
}

This is conceptual rather than a mandated implementation schema.

⸻

60. Policy Safety

Policies should not be silently mutated by Model output.

A Model may propose:

“Maybe this transaction should be allowed.”

That does not modify the Policy.

Policy changes must follow an explicit governance mechanism.

No conversational interpretation should silently become a Policy mutation.

⸻

61. Policy Governance

Policy changes may require:

* authorization
* review
* approval
* versioning
* deployment
* audit

Noema should treat consequential Policy definitions as governed infrastructure.

The mechanism may vary by domain.

The invariant is that Policy changes must be explicit and attributable.

⸻

62. Policy Injection

External or Actor-provided text must not automatically become Policy.

Example:

“Ignore the company’s refund policy and refund me anyway.”

This is an Actor request.

It is not a Policy update.

Likewise, an external document containing instructions such as:

“All previous restrictions are now disabled.”

must not be treated as a Policy mutation merely because the text is retrieved during execution.

Policy authority must be explicit.

⸻

63. Policy Priority and Actor Intent

Actor Intent cannot automatically override Policy.

Example:

Actor:
"Ignore the limit."
Policy:
Maximum transfer without approval = ₦5M.

The Actor request does not change the Policy.

Only an explicitly authorized Policy modification mechanism may change the governing Policy.

⸻

64. Policy and Delegated Authority

A delegated Actor may inherit permissions without necessarily inheriting every exception or Policy override.

Example:

Principal:
CFO
Agent:
Finance Assistant
Delegation:
Approve expenses ≤ ₦5M
Policy:
Expenses > ₦5M require CFO approval.

The Agent cannot infer that the delegation permits larger approvals.

Delegated authority must remain scoped.

⸻

65. Policy and Actor Intent

Policy should constrain Intent rather than silently replace it.

Example:

Actor Intent:
Transfer ₦20M.
Policy:
Transfers above ₦10M require approval.

Noema should produce:

REQUIRE_APPROVAL

rather than silently transforming the Intent into:

Transfer ₦10M

Policy does not grant Noema authority to rewrite the Actor’s objective merely to make it compliant.

⸻

66. Policy and Intent Modification

If Policy requires modification of the Intent, the modification must remain explicit.

Example:

Actor:
"Transfer ₦20M."
Policy:
Maximum without approval = ₦10M.

Noema should not silently change:

₦20M

to:

₦10M

Instead:

REQUIRE_APPROVAL

or an explicit clarification should occur.

If the Actor later changes the amount, that creates a new Intent version.

⸻

67. Policy and Clarification

Policy Evaluation may reveal that an Intent lacks a Policy-relevant parameter.

Example:

Policy:
International transfers require destination country.
Intent:
"Transfer money abroad."

Destination country is required.

Noema should clarify:

“Which country is the destination?”

The resulting Actor response becomes additional Evidence or Intent information and may produce a new resolved Intent version.

⸻

68. Policy Evaluation and Trust State

Policy results contribute to Trust.

Conceptually:

Authorization = ALLOW
Policy = ALLOW
Capability = AVAILABLE
Constraints = SATISFIED
Evidence = SUFFICIENT
Risk = ACCEPTABLE
        ↓
Trust = ALLOW

But:

Authorization = ALLOW
Policy = REQUIRE_APPROVAL

means:

Trust = NOT_EXECUTABLE_YET

Policy Evaluation therefore contributes to Trust but does not replace the Trust Engine.

⸻

69. Policy Evaluation Is Not the Entire Trust Decision

An Intent can satisfy every Policy and still fail the overall Trust decision because:

* authorization is denied
* capability is unavailable
* evidence is insufficient
* a constraint is violated
* risk requirements are not satisfied
* required confirmation is absent
* execution prerequisites are missing

Therefore:

Policy Evaluation
      ↓
Policy Result
      ↓
Trust Engine
      ↓
Final Trust Decision

Policy Evaluation answers only its own semantic question.

⸻

70. Policy Result Composition

A composite Intent may produce multiple Policy results.

Example:

Child Intent A:
RefundPayment
Policy:
ALLOW
Child Intent B:
CloseAccount
Policy:
REQUIRE_CONFIRMATION

The composite Intent cannot be treated as fully executable merely because one child Intent is allowed.

The Trust Engine must account for all material child Policy results.

⸻

71. Policy Result State Model

Conceptually, Policy results may be understood as distinct semantic states:

NOT_APPLICABLE
      ↓
SATISFIED
      ↓
REQUIRES_CONDITION
      ↓
UNRESOLVED
      ↓
DENIED

This is not necessarily a strict implementation ordering.

The important distinction is between:

* not applicable
* satisfied
* conditionally blocked
* unresolved
* conflicting
* denied

These states should not be collapsed.

⸻

72. Policy Evaluation and Re-Evaluation

Policies may need re-evaluation when material inputs change.

Relevant changes include:

* Intent changes
* Intent version changes
* Actor state changes
* Resource state changes
* Evidence changes
* Evidence expiration
* Policy version changes
* Policy scope changes
* Context changes
* Approval state changes
* Risk state changes
* Execution delay

A Policy result should therefore be associated with the material evaluation inputs on which it depends.

⸻

73. Policy Evaluation and Intent Versioning

If the Intent changes materially, the prior Policy result should not automatically be reused.

Example:

Intent v1:
Transfer ₦5M.
Policy:
ALLOW.

Actor changes the Intent:

Intent v2:
Transfer ₦20M.

The Policy must be evaluated against Intent v2.

The Policy result for v1 is not automatically valid for v2.

⸻

74. Policy Evaluation and Long-Running Workflows

An Intent may remain active for hours or days.

Example:

Day 1:
Deployment approved.
Day 2:
Security freeze activated.
Day 3:
Deployment executes.

The Policy environment has changed.

Noema may therefore require Policy re-evaluation immediately before execution.

This is particularly important for consequential Actions.

⸻

75. Policy Evaluation at Execution Time

For high-impact Actions:

Intent Resolved
      ↓
Policy Evaluated
      ↓
Trust Granted
      ↓
Execution Delayed
      ↓
Relevant State Changes
      ↓
Policy Re-Evaluation
      ↓
Final Trust
      ↓
Execution

The Policy result at resolution time is not necessarily sufficient at execution time.

The required freshness depends on the consequence and materiality of the Policy conditions.

⸻

76. Policy Evaluation and Caching

Policy results may be cached where safe.

However, cache validity must account for relevant inputs such as:

* Policy version
* Policy scope
* Intent version
* Actor state
* Resource state
* Context
* Evidence freshness
* Approval state
* Risk state
* evaluation time

A stale Policy result must not authorize execution merely because it is convenient to reuse.

⸻

77. Policy Evaluation and Idempotency

Policy Evaluation itself should be safe to repeat.

Evaluating:

Intent#123

twice should not alter Policy state merely because evaluation happened twice.

Where practical:

Policy Evaluation

should be side-effect free.

Side effects belong to explicit Actions and execution.

⸻

78. Policy Evaluation Should Prefer Pure Semantics

A strong architectural model is:

Inputs
  ↓
Policy Evaluation
  ↓
Result

rather than:

Policy Evaluation
  ↓
hidden side effects

This makes Policy Evaluation:

* deterministic
* testable
* reproducible
* auditable
* repeatable

External state may still need to be retrieved, but retrieval should support the evaluation rather than hide execution side effects inside it.

⸻

79. Policy Evaluation and External Calls

Policy Evaluation may need authoritative external state.

For example:

Policy Engine
      ↓
Authorization Service
      ↓
Evidence
      ↓
Policy Evaluation

The external service provides evidence or an explicitly defined semantic result.

Noema should avoid a structure where:

Policy Engine
      ↓
"External service said yes."
      ↓
Execute

without preserving what the external assertion establishes, its provenance, scope, validity, and applicability.

⸻

80. Policy Evaluation and Failure

If the Policy Evaluation process cannot retrieve required authoritative state:

Required Policy input:
UNKNOWN

then the consequential Action should generally remain:

UNRESOLVED

or:

NOT_EXECUTABLE

rather than silently becoming:

ALLOW

Infrastructure failure is not Policy satisfaction.

⸻

81. Policy Availability vs Policy Result

These are different conditions.

Policy Not Applicable

Policy:
International transfer verification.
Intent:
Domestic transfer.
Result:
NOT_APPLICABLE

Policy Cannot Be Evaluated

Policy:
International transfer verification.
Required policy service:
UNAVAILABLE
Result:
UNRESOLVED / EVALUATION_FAILURE

The first is a valid semantic Policy result.

The second is an inability to complete evaluation.

Noema should not confuse them.

⸻

82. Policy Evaluation and Infrastructure Failure

Policy Evaluation may depend on:

* Policy Registry
* Configuration Store
* Authorization Service
* Business State
* Identity Provider
* Risk Service
* Evidence Sources

Failure to retrieve required information should be represented as an explicit evaluation condition.

Noema should not convert:

service unavailable

into:

condition satisfied

The system must distinguish:

FALSE
UNKNOWN
UNAVAILABLE
NOT_APPLICABLE

where those distinctions materially affect Trust.

⸻

83. Policy Evaluation and Observability

Policy evaluations should be observable.

Useful metadata includes:

policy_id
policy_version
policy_scope
intent_id
intent_version
evaluation_id
evaluation_time
result
conditions
evidence_references
context

This enables:

* audit
* debugging
* reproducibility
* operational analysis
* Trust reconstruction

⸻

84. Policy Evaluation and Audit

A future auditor should be able to determine:

* What Policy applied?
* Which version?
* What was the Intent?
* Which scope applied?
* What Evidence was used?
* What conditions were evaluated?
* What Context was relevant?
* What was the result?
* What requirements remained?
* Was the Policy re-evaluated before execution?

This is part of trustworthy execution.

⸻

85. Policy Evaluation and Reproducibility

A Policy decision can only be meaningfully reproduced if the material evaluation basis can be reconstructed.

Therefore:

Policy Decision
      ↓
Policy Reference
      ↓
Policy Version
      ↓
Intent Version
      ↓
Evidence References
      ↓
Relevant Context

should be preserved where practical.

The goal is not necessarily to duplicate every external source record.

The goal is to preserve enough provenance to understand what the Policy Engine evaluated.

⸻

86. Policy Evaluation and Evidence Freshness

Evidence used by Policy Evaluation may become stale.

Example:

09:00:
User is Administrator.
10:00:
Role revoked.
10:30:
Policy Evaluation occurs.

Evidence from 09:00 should not automatically establish current authority.

Policy Evaluation must respect the freshness and validity requirements of the underlying Evidence.

⸻

87. Policy Evaluation and Policy Freshness

Policy definitions themselves may change.

Example:

Policy v1:
Transfers above ₦10M require approval.
Policy v2:
Transfers above ₦5M require approval.

An evaluation based on v1 must not silently be represented as an evaluation under v2.

Policy version is therefore part of the decision provenance.

⸻

88. Policy Evaluation and Tenant Isolation

Policy scope must respect tenant boundaries.

A Policy governing:

Tenant#A

must not automatically apply to:

Tenant#B

Likewise, Policy parameters, Evidence, Actor roles, and Resource state from one tenant must not silently satisfy Policy conditions in another tenant.

Tenant isolation is part of Policy applicability and Trust correctness.

⸻

89. Policy Evaluation and Jurisdiction

Where Policies depend on jurisdiction, jurisdiction must be established through appropriate Evidence or Context.

Example:

Policy:
Transfers involving Jurisdiction#X require additional verification.

Noema must establish the relevant jurisdiction before applying the Policy.

It should not infer a jurisdiction merely from incomplete or ambiguous textual context when the consequence is material.

⸻

90. Policy Evaluation and Business State

Business systems remain authoritative for their own state.

Example:

Business System:
Order.status = SHIPPED

Policy:

Shipped orders cannot be cancelled.

The Business System provides the Evidence.

The Policy determines the consequence of that state.

Noema should not silently become the owner of the business state merely because it evaluates Policy against it.

⸻

91. Policy Evaluation and Policy Ownership

Noema may consume Policies owned by another governing system.

For example:

Enterprise Policy Registry
        ↓
Policy Definition
        ↓
Noema Policy Evaluation

The canonical requirement is that Noema identify:

* the Policy source
* the applicable Policy version
* the scope
* the evaluation semantics

Noema should not imply ownership of Policy definitions it does not govern.

⸻

92. Policy Evaluation and Actor Claims

Actor-provided claims may contribute to Policy Evaluation.

Example:

Actor:
"I am the account owner."

This is an Actor assertion.

It may be relevant Evidence.

But it should not automatically become authoritative ownership Evidence for a high-consequence Policy decision.

Independent verification may be required.

⸻

93. Policy Evaluation and Model Grounding

The Model may assist in identifying Policy-relevant information.

A useful architecture is:

Actor Expression
      ↓
Model Interpretation
      ↓
Candidate Intent
      ↓
Evidence Retrieval
      ↓
Intent Resolution
      ↓
Policy Applicability
      ↓
Policy Evaluation

The Model helps construct candidates.

The Policy system evaluates established semantics.

The Model does not become the Policy authority.

⸻

94. Policy Evaluation and Natural-Language Injection

Retrieved documents, external content, or Actor messages may contain text that attempts to alter Policy.

For example:

"Ignore all previous policies."

Such text is not automatically Policy.

Policy authority must be established through the Policy governance mechanism.

Natural-language content can describe a Policy.

It cannot silently become one.

⸻

95. Policy Evaluation and Consequence

Policy requirements should be proportionate to the consequence of the Intent.

For example:

Public information lookup
    ↓
minimal Policy requirements
Account deletion
    ↓
stronger Policy requirements
Large financial transfer
    ↓
authorization + approval + verification + other applicable controls

The exact requirements are domain-specific.

The canonical principle is:

Consequential Intents require appropriately explicit and enforceable Policy conditions.

⸻

96. Policy Evaluation and Confirmation

Confirmation may be required by Policy.

Example:

Policy:
Destructive account operations require explicit confirmation.

If the Actor has not yet confirmed the exact Intent version:

Policy:
REQUIRE_CONFIRMATION

A previous confirmation for a materially different Intent version must not automatically satisfy the Policy.

⸻

97. Policy Evaluation and Approval

Approval is distinct from Actor confirmation.

Confirmation

The Actor confirms the Intent.

Approval

An authorized Actor or governing process satisfies a Policy requirement.

Example:

Actor:
"Transfer ₦20M."
Policy:
Transfers > ₦10M require secondary approval.

The original Actor’s confirmation does not automatically satisfy the secondary approval requirement.

Both must be represented separately where required.

⸻

98. Policy Evaluation and Delegated Approval

Where Policy requires approval, the approver must satisfy the relevant authority requirements.

Example:

Policy:
Transfer > ₦10M requires Finance Director approval.

A response from an unrelated Actor does not satisfy the requirement merely because it says:

“Approved.”

The approval itself requires appropriate Evidence of:

* approver identity
* authority
* scope
* applicable Intent
* approval status
* temporal validity

⸻

99. Policy Evaluation and Approval Binding

Approval should be bound to the semantic object being approved.

Example:

Intent v1:
Transfer ₦20M from Account A to Account B.

Approval:

Approved.

If Noema later changes the Intent to:

Intent v2:
Transfer ₦20M from Account A to Account C.

the approval for v1 must not automatically authorize v2.

Approval is Evidence about a particular semantic version.

⸻

100. Policy Evaluation and Partial Satisfaction

A Policy may have multiple requirements.

Example:

Policy:
International transfer requires:
1. Verified identity
2. Secondary approval
3. Destination screening

Current state:

Verified identity = satisfied
Secondary approval = satisfied
Destination screening = missing

The Policy is not fully satisfied.

The missing condition should remain explicit.

⸻

101. Policy Evaluation and Partial Resolution

Some Policy-relevant values may be resolved while others remain unresolved.

Example:

Intent:
Transfer $500 to John.
Resolved:
Amount = $500
Unresolved:
Destination Account = UNKNOWN

Policy Evaluation may therefore be partially possible but not complete.

Noema should preserve the unresolved component rather than inventing a value.

⸻

102. Policy Evaluation and Clarification Loop

A Policy Evaluation may reveal missing information.

The resulting flow may be:

Resolved Intent
      ↓
Policy Evaluation
      ↓
Missing Policy Input
      ↓
Clarification / Evidence Retrieval
      ↓
New Evidence / Intent Information
      ↓
Re-resolution if necessary
      ↓
Policy Re-evaluation

This loop is valid provided each new semantic state is explicitly represented.

⸻

103. Policy Evaluation and Trust Revalidation

A Trust decision may become invalid when its Policy basis changes.

Example:

Policy:
ALLOW
Later:
Policy version changes.
Execution:
not yet started.

Noema may need to re-evaluate the Policy before execution.

Similarly:

Policy:
ALLOW
Evidence:
permission revoked.

The prior Trust state may no longer be executable.

⸻

104. Policy Evaluation and Execution Boundary

The execution boundary is where Noema’s semantic and Trust decisions become permitted external side effects.

Before crossing that boundary, relevant Policy requirements should be:

* satisfied
* explicitly waived through authorized mechanisms where applicable
* or represented as conditions that prevent execution

The executor should not independently reinterpret whether the Actor was permitted to proceed.

⸻

105. Policy Evaluation and Outcome

Policy Evaluation concerns whether an Intent may proceed.

Outcome concerns what happened after execution.

These must remain distinct.

Policy:
ALLOW
Trust:
ALLOW
Execution:
SUCCESS

is one possible sequence.

Another is:

Policy:
ALLOW
Trust:
ALLOW
Execution:
FAILED

The second does not retroactively mean the Policy was DENY.

The execution result belongs to the Outcome layer.

⸻

106. Canonical Policy Evaluation Flow

                    Resolved Intent
                          │
                          ▼
                   Determine Scope
                          │
                          ▼
                Determine Applicability
                          │
                          ▼
                 Identify Policy Versions
                          │
                          ▼
                 Gather Required Evidence
                          │
                          ▼
                  Validate Inputs
                          │
                          ▼
                  Evaluate Conditions
                          │
            ┌─────────────┼─────────────┐
            │             │             │
            ▼             ▼             ▼
        Satisfied       Blocked       Unknown
            │             │             │
            ▼             ▼             ▼
          ALLOW          DENY      Resolve /
                                   Clarify /
                                   Retrieve
            │
            ▼
       Policy Result
            │
            ▼
       Trust Engine
            │
            ▼
    Execution Boundary

⸻

107. Canonical Trust Relationship

The Trust architecture can therefore be represented as:

                    Resolved Intent
                          │
                          ▼
                       Evidence
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
       Authorization   Policy       Capability
             │        Evaluation        │
             │            │             │
             └────────────┼─────────────┘
                          ▼
                     Constraints
                          │
                          ▼
                         Risk
                          │
                          ▼
                    Trust Decision
                          │
                          ▼
                 Execution Contract
                          │
                          ▼
                     Execution

Policy Evaluation is one deterministic component of this system.

It is neither the whole Trust model nor an alternative name for Trust.

⸻

108. Canonical Invariants

Invariant 1

Policy Evaluation operates on resolved semantic objects, not raw natural language.

Invariant 2

Consequential Policies must be explicit and machine-evaluable.

Invariant 3

Policy Evaluation should be deterministic given the same relevant inputs, Policy versions, scope, and evaluation semantics.

Invariant 4

Policy must remain distinct from Authorization.

Invariant 5

Policy must remain distinct from Capability.

Invariant 6

Policy must remain distinct from Constraints and Risk even where they interact.

Invariant 7

A Model cannot override or silently modify Policy.

Invariant 8

Missing Policy-relevant Evidence must not produce an implicit ALLOW.

Invariant 9

Conflicting Policies require explicit precedence or conflict-resolution semantics.

Invariant 10

Policy decisions must identify the applicable Policy version where material.

Invariant 11

Policy applicability must be established before Policy satisfaction is evaluated.

Invariant 12

Policy scope must be respected, including tenant, organization, resource, jurisdiction, and Actor boundaries where applicable.

Invariant 13

Policy requirements must be proportionate to the consequence of the Intent.

Invariant 14

Policy requirements must not silently mutate the Actor’s Intent.

Invariant 15

Policy results must remain distinguishable from execution Outcomes.

Invariant 16

Policy Evaluation should be repeatable and preferably side-effect free.

Invariant 17

Stale Policy decisions must not authorize execution when relevant Policy inputs have changed.

Invariant 18

NOT_APPLICABLE must remain distinct from ALLOW.

Invariant 19

UNRESOLVED must remain distinct from DENY.

Invariant 20

Infrastructure failure must not silently become Policy satisfaction.

Invariant 21

Approval and confirmation must remain distinct where Policy treats them differently.

Invariant 22

Approval, confirmation, and verification must be bound to the relevant Intent version and scope.

Invariant 23

Policy Evaluation must preserve sufficient provenance to reconstruct material decisions.

Invariant 24

Policy changes must follow an explicit governance mechanism.

Invariant 25

Actor-provided instructions cannot silently become Policy.

Invariant 26

A Policy result at Intent Resolution time does not necessarily remain valid until Execution.

Invariant 27

Long-running or delayed Intents may require Policy re-evaluation before execution.

Invariant 28

Policy Evaluation must not silently become the owner of external Business State.

Invariant 29

A Policy result contributes to Trust but does not itself constitute the final Trust decision.

Invariant 30

Noema must not replace an unresolved Policy condition with an invented assumption.

⸻

109. The Fundamental Distinction

The essential distinction is:

Intent:
"What does the Actor want?"
Evidence:
"What claims are sufficiently established?"
Authorization:
"May this Actor perform this Action?"
Policy:
"Under what conditions may it happen?"
Capability:
"Can the intended Action be performed?"
Constraints:
"What conditions restrict the Intent?"
Risk:
"What consequence-sensitive requirements apply?"
Trust:
"Is the Intent sufficiently established, permitted,
and ready to cross the execution boundary?"
Execution:
"What actually happened?"

Policy Evaluation answers only:

Under what governing rules may this established Intent proceed?

It does not answer what the Actor meant.

It does not establish business facts.

It does not establish authorization by itself.

It does not establish capability.

It does not determine execution success.

It does not constitute the final Trust decision.

⸻

110. Final Definition

Policy Evaluation is the deterministic evaluation of applicable, versioned, scoped, and governed Policies against a resolved Intent and the authoritative Evidence and Context relevant to those Policies, producing explicit requirements or decisions that contribute to Noema’s final Trust decision.

The shortest canonical formulation is:

Policy does not tell Noema what the Actor meant; it determines the conditions under which an established Intent may proceed.