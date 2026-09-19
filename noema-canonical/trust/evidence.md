Evidence

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/evidence.md

⸻

1. Definition

Evidence is an authoritative or explicitly attributable fact, observation, assertion, or artifact used by Noema to establish, validate, or constrain an Intent or Trust decision.

Evidence answers:

“What do we know, and why are we entitled to rely on it?”

Evidence is therefore one of the foundations of Noema’s deterministic Trust model.

Evidence does not mean that a proposition is inherently true. It means that there is a sufficiently attributable and appropriate basis for establishing that proposition for a particular decision.

⸻

2. Core Principle

Noema should not treat a proposition as established merely because a Model considers it likely.

The canonical distinction is:

Claim
  ↓
Evidence
  ↓
Validation
  ↓
Established Claim
  ↓
Trust Decision

The Model may propose a claim.

Evidence establishes whether that claim can be relied upon.

The distinction between inference and evidence is fundamental.

⸻

3. Evidence Is Not Truth

Evidence supports a proposition.

It is not automatically the proposition itself.

Example:

Evidence:
CRM record says User#123 owns Account#456
Claim:
User#123 owns Account#456

The evidence may itself be:

* stale
* incorrect
* incomplete
* revoked
* conflicting
* outside its applicable scope

Therefore Noema must consider the authority, freshness, provenance, scope, applicability, and integrity of evidence before relying upon it.

⸻

4. Evidence in Noema

Evidence participates across multiple parts of the system:

Actor Expression
       ↓
Model Interpretation
       ↓
Candidate Intent
       ↓
Evidence
       ↓
Resolution
       ↓
Trust
       ↓
Execution

Evidence can establish or constrain:

* Actor identity
* Resource identity
* entity relationships
* permissions
* ownership
* current state
* constraints
* policy applicability
* capability availability
* Intent parameters
* confirmation
* delegation
* execution prerequisites

Evidence is therefore not limited to authorization. It participates in establishing the semantic and operational conditions under which an Intent may proceed.

⸻

5. Evidence Semantics

5.1 Evidence vs. Context

Context and evidence must remain distinct.

Context is information available around an Intent.

Evidence is information actually relied upon to establish or justify a claim or decision.

Example:

Context:
User is chatting from a mobile device.

This is not necessarily evidence that:

User owns Account#123

unless an authoritative mechanism establishes that relationship.

Information being available does not make it evidence.

⸻

5.2 Evidence vs. Model Inference

Suppose the Actor says:

“Transfer the money to Sarah.”

The Model infers:

Sarah = Sarah#123

That is an inference.

Suppose a verified contact directory contains:

Sarah → Contact#123

That is evidence.

The Model may propose the mapping.

Evidence establishes whether the mapping is acceptable for the decision.

⸻

5.3 Evidence vs. Confidence

Confidence describes the strength of a Model’s belief.

Evidence describes the basis for establishing a proposition.

These are not interchangeable.

Example:

Model confidence:
0.98
Evidence:
Verified contact directory maps "Sarah" → Contact#123

A high Model confidence score does not become authoritative merely because the number is high.

Evidence must remain attributable to a source and applicable to the claim being established.

⸻

5.4 Evidence vs. Actor Claims

The Actor’s statement is evidence of what the Actor said.

It is not automatically authoritative evidence that every proposition contained within the statement is true.

Example:

“Transfer money from my account to John’s account.”

This establishes:

Actor wants TransferFunds

It does not necessarily establish:

John's account = Account#456

The latter requires appropriate evidence.

⸻

5.5 Evidence vs. Extraction

Model extraction and evidence validation are separate operations.

The Model may extract:

Claim A
Claim B
Intent C

But:

Extraction ≠ Validation

The Model can identify a proposition without establishing that the proposition is true or sufficiently supported for Trust.

⸻

6. Evidence Provenance

Evidence must be attributable.

Noema should be able to answer:

“Where did this evidence come from?”

Possible sources include:

* CRM
* Identity Provider
* Authorization Service
* Database
* Ledger
* Policy Registry
* User confirmation
* Signed credential
* External API
* System event
* Enterprise SaaS
* Payment provider
* Shipping provider
* Government registry

Evidence without provenance is difficult to trust.

⸻

6.1 Conceptual Evidence Structure

A useful conceptual representation is:

Evidence {
    source
    subject
    claim
    observed_at
    valid_from
    valid_until
    authority
    scope
    provenance
    version
}

This is conceptual rather than a mandated implementation schema.

The required semantics are attribution, applicability, and sufficient information to evaluate whether the evidence may be relied upon.

⸻

6.2 Provenance

Provenance should identify, where material:

* source
* origin
* observation time
* validity period
* version
* authentication status
* derivation
* scope
* applicable context

For derived evidence, provenance should preserve the underlying evidence chain.

⸻

7. Evidence Sources

Evidence may originate from several categories.

7.1 Authoritative System State

Examples:

* Database
* CRM
* Ledger
* Identity Provider
* Directory
* Authorization Service

⸻

7.2 Explicit Actor Input

Examples:

* user clarification
* user confirmation
* user-provided parameter
* explicit declaration

Actor-provided evidence must still be evaluated according to consequence and domain.

⸻

7.3 Delegated Authority

Examples:

* signed delegation
* access token
* service credential
* authorization grant
* delegated permission

⸻

7.4 System Events

Examples:

PaymentCompleted
AccountCreated
RoleRevoked
DeploymentFinished

Events can provide temporal evidence about state transitions.

⸻

7.5 External Systems

Examples:

* payment provider
* shipping provider
* government registry
* enterprise SaaS
* external identity system

External assertions should remain attributable to their source.

⸻

7.6 Derived Evidence

Evidence may be derived from multiple authoritative facts.

Example:

User#123
    member_of → Organization#ABC
Organization#ABC
    owns → Project#456
Rule:
Organization members may view owned projects.

This may establish:

User#123 may view Project#456

The resulting conclusion should preserve the underlying evidence chain.

⸻

8. Evidence Authority

Not all evidence has equal authority.

Authority is contextual.

A source may be authoritative for one proposition but not another.

For example:

Ledger
    authoritative_for → AccountBalance
CRM
    authoritative_for → CustomerProfile
Identity Provider
    authoritative_for → Authentication

Noema should avoid treating a source as universally authoritative.

The relevant question is:

Is this source authoritative for this type of claim?

⸻

8.1 Source Authority

A useful conceptual relationship is:

Source
   ↓
authoritative_for
   ↓
Claim Type

This is stronger than:

Source = trusted

because authority is specific to what the source is responsible for establishing.

⸻

8.2 Evidence Scope

Evidence must preserve scope.

Example:

User#123 is Admin

may actually mean:

User#123 is Admin
Scope:
Organization#ABC

It does not necessarily establish:

User#123 is Admin everywhere

⸻

8.3 Evidence Context

A fact may only be valid within a particular context.

Example:

User#123
Role:
Reviewer
Context:
Project#ABC

This does not necessarily establish:

User#123
Role:
Reviewer
Global Scope

Scope and context are therefore part of evidence semantics.

⸻

9. Evidence Types

9.1 Direct Evidence

Direct evidence establishes a proposition explicitly.

Example:

Database:
User#123.role = Administrator

This directly supports:

User#123 has administrator role.

⸻

9.2 Derived Evidence

Derived evidence results from applying explicit rules to other evidence.

Example:

User#123
    member_of → Organization#ABC
Organization#ABC
    owns → Project#456
Rule:
Organization members may view owned projects.

Result:

User#123 may view Project#456

The derived conclusion should preserve its source evidence and rule.

⸻

9.3 Evidence Chains

A Trust decision may depend on multiple evidence items.

Example:

Evidence A:
User#123 is authenticated.
Evidence B:
User#123 belongs to Organization#ABC.
Evidence C:
Organization#ABC owns Project#456.
Rule:
Organization members may view projects.
Decision:
ALLOWED

The chain matters because removing one material link may invalidate the conclusion.

⸻

9.4 Evidence Graph

Noema’s ontology permits evidence to be represented through relationships:

Evidence
   │
   ├── supports → Claim
   ├── about → Entity
   ├── sourced_from → Source
   ├── valid_during → Context
   ├── derived_from → Evidence
   └── used_by → Decision

This creates a traceable relationship:

Claim
  ↓
Evidence
  ↓
Decision

⸻

10. Evidence for Intent Resolution

Evidence is not limited to Trust.

It can establish Intent semantics.

Example:

Actor:
"Renew my card."
Known cards:
Card#123
Card#456

Evidence:

Card#123.expiry = 2026-08-30
Card#456.expiry = 2027-04-12

If the Actor adds:

“The one expiring this month.”

Evidence can establish:

Card#123

The Model may identify candidate resources.

Evidence establishes the canonical resource where sufficient evidence exists.

⸻

11. Evidence for Entity Resolution

Natural language often references entities indirectly.

Example:

“Send it to my wife.”

Noema may require evidence establishing:

wife → Contact#456

Possible evidence includes:

* verified relationship
* contact record
* explicit prior declaration
* authoritative directory

The Model’s guess alone is not sufficient for a consequential Action.

⸻

12. Evidence for Resource Resolution

Example:

“Delete the staging environment.”

Evidence may establish:

Environment#staging
Project#123
Tenant#ABC

The canonical Resource becomes:

Environment#staging

rather than relying on an unverified textual guess.

⸻

13. Evidence for Intent Parameters

Evidence may establish specific Intent fields.

Example:

Intent:
TransferFunds

Required parameters:

source
destination
amount
currency

Evidence may establish:

amount = ₦500,000
currency = NGN
source = Account#123

If destination remains unresolved, the Intent remains partially unresolved.

Noema should not invent the missing value.

⸻

14. Evidence for Authorization

Authorization may consume evidence such as:

* Actor role
* Resource ownership
* Tenant membership
* Delegation
* ACL
* Permission
* Relationship

Example:

Evidence:
User#123 ∈ Project#456.admins

supports:

Authorization:
ALLOWED

The Model should not determine authorization through semantic intuition.

⸻

15. Evidence for Policy

Evidence can establish whether a Policy applies.

Example:

Transaction.amount = ₦20,000,000

Policy:

Transactions > ₦10,000,000
require secondary approval.

The transaction amount is evidence for Policy evaluation.

The Model may identify the relevant transaction or policy category, but policy applicability should be determined through explicit rules.

⸻

16. Evidence for Capability

Evidence can establish available capabilities.

Example:

PaymentProvider#X
supports:
RefundPayment

The capability registry is evidence that the Action is supported through that provider.

If:

PaymentProvider#X
Currency = NGN

but the declared capability only supports:

Currency = USD

then the capability may be:

UNSUPPORTED

No Model guess should convert an unsupported operation into a supported one.

⸻

17. Evidence for Constraints

Evidence may establish constraints.

Example:

Account.status = Frozen

Constraint:

Frozen accounts cannot transfer funds.

The account state is evidence for evaluating the constraint.

⸻

18. Evidence for Confirmation

Explicit Actor confirmation is a special form of Actor-provided evidence.

Example:

Noema:
Transfer ₦5,000,000 from Account A to Account B. Confirm?
Actor:
Yes.

This supports:

Actor confirmed Intent#123.

The confirmation must be bound to the exact semantic object being confirmed.

⸻

18.1 Confirmation Must Be Bound to an Intent Version

This is critical.

Suppose:

Intent v1:
Transfer ₦5,000 to Account A

Actor:

Yes.

Noema must not then modify the Intent to:

Intent v2:
Transfer ₦5,000,000 to Account B

and reuse the original confirmation.

Confirmation evidence belongs to the specific Intent version it confirms.

A material semantic change requires new confirmation where confirmation is required.

⸻

19. Evidence Freshness

Evidence can become stale.

Example:

09:00:
User is Admin.
10:00:
Role revoked.
10:30:
Authorization evaluated.

Evidence from 09:00 may no longer establish current authorization.

Evidence may therefore require:

observed_at
valid_from
valid_until
version

⸻

20. Evidence Validity

Evidence may have a validity interval.

Example:

Delegation:
09:00 → 17:00

At 18:00:

Delegation evidence:
INVALID

Noema should not rely on expired authority.

⸻

21. Evidence Revocation

Some evidence can be actively revoked.

Examples:

* access token
* delegation
* permission
* credential
* approval
* session

Where the domain requires it, Noema must be able to establish whether evidence has been revoked.

⸻

22. Evidence Versioning

Evidence may change over time.

Example:

Project#123.owner
v1 → User#A
v2 → User#B

Historical Trust decisions should preserve the version of the evidence relied upon.

This allows a historical decision to remain interpretable even after the underlying business state changes.

⸻

23. Evidence Conflicts

Different sources may disagree.

Example:

CRM:
Account owner = User#A
Billing system:
Account owner = User#B

Noema must not arbitrarily choose one.

The conflict itself becomes a Trust-relevant condition:

CONFLICTING_EVIDENCE

Possible resolution mechanisms include:

* authoritative source hierarchy
* source reconciliation
* domain-specific resolution
* human clarification

The applicable mechanism depends on the domain.

⸻

24. Evidence Conflict vs. Ambiguity

These concepts are distinct.

Ambiguity

The Actor’s Intent has multiple plausible interpretations.

Example:

“Delete the account.”

Which account?

Evidence Conflict

Sources disagree about an underlying fact.

Example:

CRM:
Owner = User#A
Billing:
Owner = User#B

Ambiguity concerns unresolved meaning.

Evidence conflict concerns disagreement about the facts supporting meaning or Trust.

They require different handling.

⸻

25. Evidence Completeness

A decision may require multiple pieces of evidence.

Example:

To transfer funds:

* Actor identity
* Source account
* Destination account
* Balance
* Authorization
* Transfer limits

If one material piece is missing:

Transfer:
NOT READY FOR TRUST DECISION

Noema should not fill the gap with an assumption.

⸻

26. Evidence Sufficiency

Evidence does not need to be exhaustive.

It needs to be sufficient for the decision being made.

For example:

View public product description

may require relatively little evidence.

Whereas:

Transfer ₦10,000,000

requires substantially stronger evidence.

Therefore evidence requirements should be proportional to the consequence of the Intent.

⸻

27. Evidence and Risk

Conceptually:

Risk ↑
Evidence Requirement ↑

Examples:

Read public information
    → minimal verification
Delete account
    → identity + authorization
Transfer large funds
    → identity + authorization + confirmation + policy checks

The precise threshold is domain- and policy-dependent.

⸻

28. Evidence and Consequence

Evidence requirements should correspond to potential impact.

Consequential categories include:

* financial
* destructive
* security
* privacy
* legal
* production infrastructure
* external communication

The greater the consequence, the less acceptable unsupported inference becomes.

⸻

29. Evidence and Determinism

Evidence is one of the mechanisms by which Noema converts probabilistic interpretation into deterministic commitment.

Model hypothesis
      ↓
Evidence gathering
      ↓
Evidence validation
      ↓
Resolved Intent

Without sufficient evidence, Noema may need to remain uncertain.

This is consistent with the deterministic Trust principle.

⸻

30. Evidence Does Not Eliminate Uncertainty

Evidence can remain:

* incomplete
* conflicting
* stale
* low-authority
* ambiguous
* outside scope
* unverifiable

Therefore Noema must be capable of representing explicit unresolved states such as:

UNKNOWN
UNVERIFIED
CONFLICTING
INSUFFICIENT

rather than forcing a binary answer.

⸻

31. Evidence Status

A useful conceptual state model is:

UNVERIFIED
    ↓
OBSERVED
    ↓
VALIDATED
    ↓
SUFFICIENT

Possible failure paths include:

OBSERVED
   ↓
STALE
OBSERVED
   ↓
CONFLICTING
OBSERVED
   ↓
REVOKED

These are conceptual states rather than mandatory implementation enums.

⸻

32. Observation vs. Validation

Observation and validation must remain distinct.

Observation

A source reported a fact.

Validation

Noema established that the evidence is sufficiently trustworthy and applicable for the intended decision.

Example:

External API:
"User is Admin."

Observation:

Admin claim received.

Validation:

Source authenticated.
Claim current.
Claim applies to Tenant A.
Claim is authoritative for this claim type.

Only then should the claim be relied upon for a high-impact Trust decision.

⸻

33. Evidence Quality

Evidence quality may be evaluated across several dimensions:

* Authority
* Authenticity
* Freshness
* Specificity
* Completeness
* Scope
* Consistency
* Provenance
* Applicability
* Integrity

Not every decision requires every dimension.

The relevant dimensions depend on the claim and consequence.

⸻

34. Evidence Weighting

Noema should be cautious about representing evidence as arbitrary numerical scores.

Bad:

Evidence confidence = 0.87

without a clear semantic basis.

Prefer explicit properties:

Source:
Identity Provider
Authenticated:
Yes
Observed:
2026-08-25T08:12Z
Valid:
Yes
Scope:
Tenant#ABC

Deterministic rules can then evaluate those properties.

⸻

35. Evidence Score vs. Evidence

An evidence score may be operationally useful.

But:

A score must not replace the semantics of evidence.

For example:

0.93 evidence confidence

does not establish:

* who produced the evidence
* what it establishes
* whether it is current
* whether it applies
* whether it is within scope
* whether it is authentic

Those properties are more important to Trust.

⸻

36. Evidence Aggregation

Multiple evidence items may collectively establish a claim.

Example:

Evidence A:
User authenticated.
Evidence B:
User owns Account#123.
Evidence C:
Account#123 is active.

Together, explicit rules may establish:

User#123 may initiate a transfer from Account#123.

Evidence aggregation must be governed by explicit semantics and rules.

The system should not treat a collection of weak or unrelated facts as authoritative merely because they are numerous.

⸻

37. Evidence Invalidation

A Trust decision may become invalid if its underlying evidence becomes invalid.

Example:

Authorization Decision:
ALLOWED
Underlying permission:
revoked

For long-running workflows, Noema may need to re-evaluate Trust before the final side effect.

⸻

38. Evidence Retrieval

Evidence may need to be actively retrieved.

Examples:

lookup account
lookup permissions
lookup policy
lookup resource
lookup current state
lookup capability

Retrieval is an implementation mechanism.

The canonical requirement is:

Material claims must be supported by appropriate evidence before they are treated as established.

⸻

39. Evidence Retrieval Must Be Scoped

Noema should retrieve evidence relevant to the current Intent and Context.

Example:

Intent:
Refund Order#123

Relevant evidence may include:

* Order status
* Payment status
* Refund policy
* Actor authorization

Irrelevant information should not become part of the Trust basis merely because it was available.

⸻

40. Evidence Acquisition and Clarification

When evidence is insufficient, Noema may ask the Actor for information.

Example:

Noema:
Which John do you mean?
Actor:
John Smith.

The Actor’s response becomes additional evidence.

This creates an evidence acquisition loop:

Intent
  ↓
Missing Evidence
  ↓
Clarification
  ↓
Actor Response
  ↓
New Evidence
  ↓
Resolution

Clarification is therefore an evidence acquisition mechanism.

⸻

41. Evidence and Partial Resolution

Evidence may resolve only part of an Intent.

Example:

“Transfer $500 to John.”

Evidence establishes:

Amount = $500

but not:

John = Account#456

The Intent remains partially unresolved.

Noema should preserve this state instead of pretending the Intent is complete.

⸻

42. Evidence and Natural-Language Claims

Natural language can contain multiple claims.

Example:

“Send $500 to John because he owns the company account.”

This contains:

Intent:
Send $500
Entity:
John
Claim:
John owns the company account

The Intent may be directly expressed by the Actor.

The ownership claim may require independent evidence.

Noema must not treat every proposition in an Actor expression as equally authoritative.

⸻

43. Evidence and Model Grounding

Models can be grounded with evidence.

A useful architecture is:

User Input
    ↓
Model
    ↓
Candidate Claims
    ↓
Evidence Retrieval
    ↓
Evidence Validation
    ↓
Canonical Intent

The Model becomes more reliable without becoming the authority.

⸻

44. Evidence and Delegation

Delegation is itself evidence of authority.

Example:

Principal:
User#123
Delegated Actor:
Agent#456
Authority:
RefundPayment
Scope:
Tenant#ABC
Expiry:
2026-08-25T17:00Z

This evidence establishes whether the Agent can act on behalf of the Principal.

⸻

44.1 Delegation Provenance

A delegated decision may require:

Credential
   ↓
Identity
   ↓
Delegation
   ↓
Authorization
   ↓
Intent

The Trust decision should preserve enough provenance to understand that chain.

⸻

45. Evidence and Tenant Isolation

Evidence must respect tenant boundaries.

A claim from Tenant A should not automatically establish a claim within Tenant B.

This is especially important for:

* identity
* authorization
* ownership
* configuration
* policy
* resources
* delegation

Tenant scope is part of evidence applicability.

⸻

46. Evidence and External Assertions

External systems can make assertions.

Example:

Shipping Provider:
Package#123 delivered.

Noema may use this as evidence for:

Order#456 can be refunded.

But the evidence should preserve:

source = ShippingProvider
claim = delivered
observed_at = ...

rather than treating the external assertion as an unqualified fact.

⸻

47. Evidence and Events

Events can provide temporal evidence.

Example:

PaymentCompleted
at 14:03

This may establish:

Payment#123 was completed at 14:03.

Events are particularly useful when determining state transitions and temporal conditions.

⸻

48. Evidence and Temporal Ordering

Some decisions depend on event ordering.

Example:

PaymentCreated
PaymentSettled
PaymentRefunded

If the Actor asks:

“Refund the payment.”

Noema may need to establish current state and relevant event history.

Evidence ordering can therefore matter.

⸻

49. Evidence and Causality

For complex workflows, evidence may establish causal relationships.

Example:

PaymentCompleted
      ↓
OrderEligibleForFulfillment
      ↓
OrderShipped

The causal chain may support downstream decisions.

Noema should preserve causal relationships where they are material to Trust.

⸻

50. Evidence and Business State

Noema should consume Business State as evidence rather than duplicate ownership of that state.

Example:

Business System:
Order.status = shipped

Noema can use this to evaluate:

Intent:
CancelOrder(Order#123)

against:

Policy:
Shipped orders cannot be cancelled.

The business system remains authoritative for the Order.

⸻

51. Evidence and Intent State

Noema may own the state of an Intent.

Example:

Intent#123
status = awaiting_confirmation

This state can itself become evidence for subsequent decisions.

Example:

Evidence:
Intent#123 was explicitly confirmed by Actor#456.

This does not transfer ownership of Business State to Noema. It establishes the state of the Noema-controlled Intent lifecycle.

⸻

52. Evidence and Identity

Identity evidence establishes who is acting.

Examples:

* authenticated session
* signed token
* verified credential
* service identity
* delegated identity

Noema should distinguish:

Claimed Identity

from:

Verified Identity

The distinction becomes increasingly important as consequence increases.

⸻

53. Evidence and Actor Assertions

Actors can provide evidence through statements.

Example:

“My account number is 123456.”

This is an Actor assertion.

It may be useful for resolution.

For high-risk Actions, however, it may require independent verification.

Noema should not automatically elevate:

Actor assertion

into:

Authoritative fact

⸻

54. Evidence and Composite Intents

A composite Intent may require separate evidence for each component.

Example:

RefundPayment(Payment#123)
AND
CloseAccount(Account#456)

Evidence required for the refund may differ from evidence required for account closure.

Noema should not assume that evidence sufficient for one child Intent automatically establishes the other.

Each consequential child Intent must satisfy its own evidence requirements.

⸻

55. Evidence and Risk-Proportional Explicitness

Evidence should be as explicit as the consequence requires.

Low consequence:

Implicit contextual evidence

may be sufficient.

High consequence:

Explicit confirmation

or:

Authoritative verification

may be required.

Noema should not use one universal evidence threshold for every Intent.

⸻

56. Evidence Threshold

Conceptually:

Required Evidence Strength
        ∝
Potential Consequence

This is a Trust design principle.

The exact threshold is determined by applicable policy, risk, authorization, capability, and domain requirements.

⸻

57. Evidence Security

Evidence itself can be attacked.

Threats include:

* forged evidence
* stale evidence
* tampered evidence
* spoofed sources
* replayed credentials
* cross-tenant evidence
* injected documents
* malicious claims

High-trust evidence may therefore require cryptographic or system-level verification.

⸻

58. Evidence Authenticity

Where appropriate, Noema should establish:

* Who produced the evidence?
* Was it altered?
* Is the source authentic?
* Is the evidence intended for this system?
* Is the evidence within the expected scope?

Possible mechanisms include:

* signatures
* authenticated APIs
* trusted channels
* versioned records
* credential verification

The canonical requirement is authenticity and provenance appropriate to the consequence.

⸻

59. Evidence Replay

Evidence may be valid when first issued but invalid later.

Example:

Authorization token:
issued 09:00
revoked 09:30

Replaying the token at 10:00 must not necessarily establish current authority.

Evidence evaluation must therefore account for:

* revocation
* freshness
* validity interval
* intended scope
* temporal applicability

⸻

60. Evidence and Privacy

Evidence may contain sensitive information.

Evidence handling must therefore respect:

* access controls
* data minimization
* tenant isolation
* retention requirements
* privacy policies

Trust does not imply unrestricted access to evidence.

⸻

61. Evidence Minimization

Noema should use the minimum evidence required to establish the decision.

Example:

Authorization may require:

User#123 has permission X

It may not require exposing the user’s entire profile.

Evidence minimization reduces unnecessary data exposure while preserving sufficient Trust basis.

⸻

62. Evidence Disclosure

The Actor may not always be entitled to see the evidence behind a Trust decision.

For example:

Internal authorization rule:
Confidential

The system may communicate:

“You are not authorized to perform this action.”

without exposing the internal policy or confidential evidence.

Explainability must therefore respect evidence confidentiality.

⸻

63. Evidence and Long-Running Intents

An Intent may remain active for hours or days.

Example:

“Deploy this release after approval.”

Evidence collected Monday may no longer be valid Tuesday.

Noema should distinguish:

Evidence at Resolution

from:

Evidence at Execution

where relevant.

⸻

64. Evidence at Execution Time

For high-impact Actions:

Intent Resolved
      ↓
Evidence Collected
      ↓
Trust Decision
      ↓
Execution Delayed

If the delay is significant, Noema may need to revalidate material evidence.

This is particularly important for:

* authorization
* resource state
* policy applicability
* capability
* confirmation
* constraints

⸻

65. Evidence and Trust Re-Evaluation

A long-running Intent may require:

Resolution
    ↓
Initial Trust
    ↓
Waiting
    ↓
State Change
    ↓
Revalidation
    ↓
Final Trust
    ↓
Execution

This prevents stale evidence from authorizing consequential side effects.

⸻

66. Evidence Invalidation Before Execution

A previously valid Trust decision may require re-evaluation when material evidence changes.

Example:

Initial:
Permission = Valid
Trust = ALLOWED
Before execution:
Permission = Revoked

The system must apply the relevant Trust and execution semantics rather than assuming the original decision remains valid indefinitely.

⸻

67. Evidence and Execution Contracts

Evidence should support the canonical Execution Contract.

Conceptually:

Evidence
   ↓
Resolution
   ↓
Authorization
   ↓
Policy
   ↓
Capability
   ↓
Trust Decision
   ↓
Execution Contract

The Execution Contract should contain references or provenance sufficient to establish the basis of the consequential decision.

The Consumer should not need to reconstruct the evidence chain from natural language.

⸻

68. Evidence and Auditability

Every material Trust decision should ideally be traceable to the evidence that supported it.

Example:

Decision#123
    ├── Intent#456
    ├── Evidence#1
    ├── Evidence#2
    ├── Policy#7
    └── AuthorizationRule#12

This creates an auditable decision graph.

⸻

69. Evidence and Reproducibility

A deterministic decision can only be meaningfully reproduced if its material evidence can be identified.

Therefore:

Decision
   ↓
Evidence References
   ↓
Source Versions

should be preserved where practical.

Reproducibility does not require that Business State remain unchanged.

It requires that the decision’s relevant historical inputs and evidence references be identifiable.

⸻

70. Evidence Retention

Evidence retention should depend on:

* legal requirements
* audit requirements
* privacy requirements
* security requirements
* business requirements

Noema should not retain evidence indefinitely by default.

Where Noema references evidence owned by another system, retention semantics should respect that system’s ownership and applicable requirements.

⸻

71. Evidence Ownership

Noema may reference evidence owned by another system.

Example:

Ledger owns:
Account balance

Noema should preserve a reference to the authoritative evidence rather than necessarily copying the entire record.

This reinforces:

Noema owns Trust decisions, not every piece of Business State.

⸻

72. Evidence and the Canonical Repository

The Ontology should define what kinds of things can act as evidence and how evidence relates to canonical entities and claims.

The Trust layer defines:

* how evidence is evaluated
* how evidence supports decisions
* how evidence conflicts are handled
* how evidence is validated
* how evidence freshness is considered
* how evidence is preserved for material decisions

This separation keeps the repository coherent.

⸻

73. Evidence Relationship to Other Trust Concepts

Evidence interacts with the principal Trust concepts:

Ambiguity
    ↓
determines whether evidence is sufficient to resolve meaning
Authorization
    ↓
uses evidence to establish permission
Determinism
    ↓
requires consequential decisions to be grounded in evidence
Policy
    ↓
uses evidence to evaluate applicable rules
Capability
    ↓
uses evidence to establish whether an Action is supported
Risk
    ↓
influences the required evidence threshold
Trust
    ↓
aggregates evidence-backed determinations

Evidence is therefore a foundational input to Trust rather than merely an audit artifact.

⸻

74. Evidence and Deterministic Failure

Missing or insufficient evidence must produce an explicit system state rather than an invented assumption.

Possible outcomes include:

UNKNOWN
UNVERIFIED
INSUFFICIENT
CONFLICTING
STALE
REVOKED

These are valid system outcomes.

They indicate that Noema has not established the required proposition.

⸻

75. Evidence and Clarification

When evidence is insufficient because the Actor can provide the missing information, clarification is an appropriate next transition.

Example:

Noema:
Which account do you mean?
Actor:
My savings account.

The new Actor response becomes additional evidence.

The system may then resolve:

Account#Savings

subject to the available authoritative evidence.

⸻

76. Evidence and Fail-Closed Trust

For consequential Actions:

Required Evidence
        ↓
Unavailable
        ↓
Do Not Establish Claim
        ↓
Do Not Authorize Execution

Unknown must not silently become allowed.

This is particularly important for:

* financial Actions
* destructive Actions
* security Actions
* privacy-sensitive Actions
* external communications
* production changes

⸻

77. Evidence and Graceful Degradation

Failing closed does not mean producing a useless system.

Noema can transition into recoverable states:

AMBIGUOUS
    ↓
Clarification
UNVERIFIED
    ↓
Request verification
INSUFFICIENT
    ↓
Retrieve additional evidence
CONFLICTING
    ↓
Resolve source conflict

The system remains useful without guessing.

⸻

78. Evidence and Consequential Execution

The more consequential the Action, the less acceptable unsupported inference becomes.

The canonical principle is:

Consequence ↑
     ↓
Required Evidence Strength ↑

This does not require every Action to have the same verification process.

Evidence requirements should be determined by the consequence, domain, risk, policy, and applicable Trust rules.

⸻

79. Canonical Evidence Flow

                 Claim / Intent
                       │
                       ▼
                Evidence Required
                       │
                       ▼
                 Evidence Sources
                       │
                       ▼
                 Evidence Retrieved
                       │
                       ▼
                  Validate Evidence
                       │
              ┌────────┴────────┐
              │                 │
          Sufficient        Insufficient
              │                 │
              ▼                 ▼
       Establish Claim      Clarify /
              │              Retrieve More
              ▼
        Trust Evaluation
              │
              ▼
           Decision

The flow is intentionally compatible with Noema’s deterministic Trust model.

⸻

80. Evidence Decision Model

Conceptually:

Evidence Evaluation =
    f(
        Source,
        Claim,
        Authority,
        Authenticity,
        Freshness,
        Validity,
        Scope,
        Applicability,
        Integrity,
        Context
    )

The exact implementation is an architectural concern.

The semantic requirement is that consequential claims be evaluated against explicit evidence properties rather than Model confidence alone.

⸻

81. Evidence and Canonical Intent

Evidence may establish fields of a typed Intent.

Conceptually:

TransferFunds {
    actor: Actor
    source: Account
    destination: Account
    amount: Money
    constraints: [...]
}

The Model may populate candidate fields.

Evidence and deterministic Resolution establish whether those fields can become canonical.

Trust evaluates the resulting Intent.

Execution receives the established semantic object.

⸻

82. Evidence and Identity Resolution

Natural-language identity references should converge on canonical identifiers when sufficiently supported.

Example:

"my savings account"
        ↓
Evidence
        ↓
Account#123

Once established:

Account#123

should be carried through the execution pipeline.

The executor should not need to resolve:

“my savings account”

again.

⸻

83. Evidence and Retry

Retries must not silently create new semantic interpretations.

Given:

Intent#789

a retry should use the same canonical Intent unless the system explicitly creates a new Intent version.

The Model should not reinterpret the original Actor expression on every retry and thereby create a different evidence or semantic basis.

⸻

84. Evidence and Composite Execution

A composite Intent may contain multiple Trust domains.

Example:

RefundPayment(Payment#123)
AND
CloseAccount(Account#456)

Each child may require separate:

* evidence
* authorization
* policy
* capability
* risk evaluation
* confirmation

The parent Intent must not hide those distinctions.

⸻

85. Evidence and Partial Failure

Suppose:

RefundPayment → Evidence Sufficient → Allowed
CloseAccount → Evidence Insufficient → Not Authorized

Noema must not automatically treat the composite operation as fully authorized.

Composite execution semantics must explicitly define whether:

* partial execution
* rollback
* compensation
* precondition failure

is permitted.

Evidence sufficiency must be evaluated according to the semantics of each consequential child Intent.

⸻

86. Evidence and Business-State Authority

Noema should not manufacture Business State merely because required evidence is unavailable.

For example:

Business System:
Order.status = shipped

Noema may consume this as evidence.

It should not create its own competing claim:

Noema:
Order.status = shipped

unless that is explicitly part of Noema’s own state model.

The authoritative Business State remains owned by the domain system.

⸻

87. Evidence and Versioned Decisions

Rules, policies, capabilities, and evidence can change.

Therefore material Trust decisions should identify relevant versions.

Example:

Policy:
expense-approval-v4
Authorization:
role-model-v7
Capability:
refund-v2
Evidence:
ResourceVersion-42
PermissionVersion-9

A historical decision should remain interpretable in relation to the versions that supported it.

⸻

88. Evidence and Changed State

A previously established claim may no longer hold when authoritative state changes.

Example:

10:00
User is authorized.
11:00
Authorization revoked.
11:01
Same Intent evaluated.

The new decision may legitimately differ because the evidence state changed.

This does not constitute inconsistency if the relevant inputs are different.

⸻

89. Evidence and Decision Snapshots

For consequential decisions, Noema should conceptually be able to construct a decision snapshot:

Decision Snapshot
├── Intent
├── Actor
├── Resources
├── Context
├── Evidence
├── Authorization
├── Policies
├── Capabilities
├── Constraints
└── Decision

The exact storage mechanism is an implementation concern.

The semantic requirement is sufficient traceability to understand the basis of the decision.

⸻

90. Evidence and Explainability

Explainability should expose the decision basis rather than hidden Model reasoning.

Example:

“The request was blocked because the Actor does not have project.delete permission for this project.”

This can be supported by:

Intent
+
Evidence
+
Authorization Rule
+
Decision

Noema does not need to expose an internal Model chain-of-thought.

⸻

91. Evidence and Trust Boundary

The Model may say:

“This appears to be Account#123.”

Evidence may establish:

Account#123

Noema may then establish:

Resolved Intent

Trust may establish:

ALLOWED

The Consumer receives:

Canonical Execution Contract

The progression is:

Model hypothesis
      ↓
Evidence
      ↓
Established claim
      ↓
Canonical Intent
      ↓
Trust Decision
      ↓
Execution

This preserves the deterministic boundary.

⸻

92. Canonical Invariants

Invariant 1

Evidence must have attributable provenance.

Invariant 2

Model inference is not automatically evidence.

Invariant 3

Evidence strength is contextual.

Invariant 4

Evidence must be sufficiently authoritative for the claim being established.

Invariant 5

Stale or revoked evidence must not silently establish current authority.

Invariant 6

Conflicting evidence must not be resolved through arbitrary preference.

Invariant 7

Evidence requirements should be proportional to consequence.

Invariant 8

Explicit Actor confirmation is evidence only for the Intent version it confirms.

Invariant 9

Noema should preserve enough provenance to explain material Trust decisions.

Invariant 10

Noema should consume authoritative Business State rather than silently becoming its owner.

Invariant 11

Missing evidence must result in an explicit unresolved state rather than an invented assumption.

Invariant 12

Evidence used for consequential execution should be appropriately fresh.

Invariant 13

Evidence authority is claim-specific and should not be treated as universally transferable across domains.

Invariant 14

Evidence scope must be preserved; evidence valid in one tenant, resource, context, or authority domain must not silently establish claims outside that scope.

Invariant 15

Observation of evidence and validation of evidence are distinct operations.

Invariant 16

Derived evidence must preserve the provenance of the evidence and rules from which it was derived.

Invariant 17

Evidence used for a consequential decision must be sufficient for that decision, not merely available.

Invariant 18

Actor assertions may establish what the Actor said without automatically establishing the truth of the proposition asserted.

Invariant 19

Evidence invalidation may require Trust re-evaluation before consequential execution.

Invariant 20

Evidence references and relevant source versions should be preserved where required for auditability and reproducibility.

⸻

93. Fundamental Distinction

The most important distinction is:

Model:
"This is probably true."
Evidence:
"This source establishes or supports this claim."
Noema:
"This claim is sufficiently established for this decision."

These are three different states.

They must not be collapsed into one another.

⸻

94. Final Definition

Evidence is the attributable, contextual, appropriately authoritative, and sufficiently valid basis by which Noema establishes claims about Actors, Intents, Resources, state, permissions, policies, capabilities, constraints, and other conditions required for deterministic Trust decisions.

The shortest canonical formulation is:

Noema does not trust an interpretation because the Model is confident; it trusts a decision because the necessary claims are supported by sufficient evidence.