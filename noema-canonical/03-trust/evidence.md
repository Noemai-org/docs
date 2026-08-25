Evidence

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: 03-trust/evidence.md

⸻

1. Definition

Evidence is an authoritative or explicitly attributable fact, observation, assertion, or artifact used by Noema to establish, validate, or constrain an Intent or Trust decision.

Evidence answers:

“What do we know, and why are we entitled to rely on it?”

Evidence is therefore one of the foundations of Noema’s deterministic Trust model.

⸻

2. The Core Principle

Noema should not treat a proposition as established merely because a Model considers it likely.

Instead:

Claim
  ↓
Evidence
  ↓
Validation
  ↓
Established Fact
  ↓
Trust Decision

The distinction between inference and evidence is fundamental.

⸻

3. Evidence Is Not Truth

Evidence supports a proposition.

It is not automatically the proposition itself.

For example:

Evidence:
CRM record says User#123 owns Account#456

supports:

Claim:
User#123 owns Account#456

The evidence may itself be:

stale
incorrect
incomplete
revoked
conflicting

Therefore Noema must consider the authority, freshness, provenance, and applicability of evidence.

⸻

4. Evidence in Noema

Evidence participates across multiple parts of the system:

                    Actor Expression
                           │
                           ▼
                    Model Interpretation
                           │
                           ▼
                     Candidate Intent
                           │
                           ▼
                       Evidence
                           │
                           ▼
                     Resolution
                           │
                           ▼
                         Trust
                           │
                           ▼
                       Execution

Evidence can establish:

Actor identity
Resource identity
relationships
permissions
current state
constraints
policy applicability
capability availability
Intent parameters
confirmation
delegation
execution prerequisites

⸻

5. Evidence vs Context

These concepts must remain distinct.

Context

Information available around an Intent.

Evidence

Information that is actually relied upon to establish or justify a claim or decision.

For example:

Context:
User is chatting from a mobile device.

This is not necessarily evidence that:

User owns Account#123

unless an authoritative mechanism establishes that relationship.

⸻

6. Evidence vs Model Inference

Suppose the user says:

“Transfer the money to Sarah.”

The Model infers:

Sarah = Sarah#123

That is an inference.

Suppose the user’s verified contacts contain:

Sarah → Contact#123

That is evidence.

The Model may propose the mapping.

The evidence establishes whether it is acceptable.

⸻

7. Evidence vs Confidence

Confidence describes the strength of a Model’s belief.

Evidence describes the basis for establishing a proposition.

These are not interchangeable.

Model confidence:
0.98
Evidence:
Contact directory explicitly maps "Sarah" → Contact#123

The second is materially stronger for Trust.

A 99.9% Model confidence score does not become authoritative merely because the number is high.

⸻

8. Evidence Must Be Attributable

Noema should be able to answer:

Where did this evidence come from?

Examples:

CRM
Identity Provider
Authorization Service
Database
Policy Registry
User confirmation
Signed credential
External API
System event
Execution result

Evidence without provenance is difficult to trust.

⸻

9. Evidence Provenance

A useful conceptual structure is:

Evidence {
    source
    subject
    claim
    observed_at
    valid_from
    valid_until
    authority
    provenance
    version
}

This is conceptual rather than a mandated implementation schema.

⸻

10. Evidence Sources

Evidence may originate from:

10.1 Authoritative System State

Database
CRM
Ledger
Identity Provider
Directory

10.2 Explicit Actor Input

User clarification
User confirmation
User-provided parameter

10.3 Delegated Authority

Signed delegation
Access token
Service credential
Authorization grant

10.4 System Events

PaymentCompleted
AccountCreated
RoleRevoked
DeploymentFinished

10.5 External Systems

Payment provider
Shipping provider
Government registry
Enterprise SaaS

10.6 Derived Evidence

Evidence may sometimes be derived from multiple authoritative facts.

But derived evidence should preserve its provenance.

⸻

11. Evidence Hierarchy

Not all evidence has equal authority.

A conceptual hierarchy is:

Direct authoritative state
        ↓
Signed / authenticated assertion
        ↓
Explicit Actor confirmation
        ↓
Trusted system observation
        ↓
Derived evidence
        ↓
Model inference
        ↓
Unverified assumption

The exact ordering can vary by domain.

The important principle is:

Evidence strength is contextual and must not be reduced to Model confidence.

⸻

12. Direct Evidence

Direct evidence establishes a proposition explicitly.

Example:

Database:
User#123.role = Administrator

This directly supports:

User#123 has administrator role.

⸻

13. Derived Evidence

Evidence can be derived.

Example:

User#123
    member_of → Organization#ABC
Organization#ABC
    owns → Project#456
Rule:
Organization members may view owned projects.

This can establish:

User#123 may view Project#456

But the resulting authorization decision should preserve the underlying chain.

⸻

14. Evidence Chains

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

The chain matters because removing one link may invalidate the conclusion.

⸻

15. Evidence Graph

Noema’s ontology naturally permits evidence to be represented as relationships:

Evidence
   │
   ├── supports → Claim
   ├── about → Entity
   ├── sourced_from → Source
   ├── valid_during → Context
   └── used_by → Decision

This creates a traceable relationship between:

Claim
→ Evidence
→ Decision

⸻

16. Evidence for Intent Resolution

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

If the user’s context specifies:

“The one expiring this month.”

the evidence can resolve:

Card#123

⸻

17. Evidence for Entity Resolution

Natural language often references entities indirectly.

Example:

“Send it to my wife.”

Noema may require evidence establishing:

wife → Contact#456

Possible evidence:

verified relationship
contact record
explicit prior declaration

The Model’s guess is not sufficient for a consequential Action.

⸻

18. Evidence for Resource Resolution

Example:

“Delete the staging environment.”

Evidence may establish:

Environment#staging
Project#123
Tenant#ABC

The canonical Resource becomes:

Environment#staging

rather than relying on a textual guess.

⸻

19. Evidence for Authorization

Authorization may consume evidence such as:

Actor role
Resource ownership
Tenant membership
Delegation
ACL
Permission

Example:

Evidence:
User#123 ∈ Project#456.admins

supports:

Authorization:
ALLOWED

⸻

20. Evidence for Policy

Evidence can establish whether a Policy applies.

Example:

Transaction.amount = ₦20,000,000

Policy:

Transactions > ₦10,000,000 require secondary approval.

The transaction amount is evidence supporting Policy evaluation.

⸻

21. Evidence for Capability

Evidence can establish available capabilities.

Example:

PaymentProvider#X
supports:
RefundPayment

The capability registry is evidence that the Action can be performed through that provider.

⸻

22. Evidence for Constraints

Evidence may establish constraints.

Example:

Account.status = Frozen

Constraint:

Frozen accounts cannot transfer funds.

The account state is evidence for the constraint evaluation.

⸻

23. Evidence for Confirmation

Explicit confirmation is a special form of Actor-provided evidence.

Example:

Noema:
Transfer ₦5,000,000 from Account A to Account B. Confirm?
Actor:
Yes.

The Yes supports:

Actor confirmed canonical Intent#123.

The confirmation should be tied to the exact Intent version being confirmed.

⸻

24. Confirmation Must Be Bound to an Intent

This is critical.

Suppose:

Intent v1:
Transfer ₦5,000 to Account A

Actor says:

Yes.

Then Noema changes it to:

Intent v2:
Transfer ₦5,000,000 to Account B

The original confirmation must not be reused.

Confirmation evidence must be bound to the specific semantic object that was confirmed.

⸻

25. Evidence Freshness

Evidence can expire.

Example:

09:00:
User is Admin.
10:00:
Role revoked.
10:30:
Authorization evaluated.

Evidence from 09:00 may no longer establish current authorization.

Therefore evidence may need:

observed_at
valid_from
valid_until
version

⸻

26. Evidence Validity

Evidence may have a validity interval:

valid_from
valid_until

Example:

Delegation:
09:00 → 17:00

At 18:00:

Delegation evidence:
INVALID

Noema should not rely on expired authority.

⸻

27. Evidence Revocation

Some evidence can be actively revoked.

Examples:

access token
delegation
permission
credential
approval
session

The system should be able to establish revocation where the domain requires it.

⸻

28. Evidence Versioning

Evidence may change over time.

Example:

Project#123.owner
v1 → User#A
v2 → User#B

Historical Trust decisions should preserve which version was relied upon.

⸻

29. Evidence Conflicts

Different sources may disagree.

Example:

CRM:
Account owner = User#A
Billing system:
Account owner = User#B

Noema must not arbitrarily choose one.

The conflict itself becomes a Trust-relevant condition:

CONFLICTING_EVIDENCE

Possible resolution:

authoritative source hierarchy
source reconciliation
human clarification
domain-specific resolution

⸻

30. Evidence Conflict Is Not Ambiguity

These concepts differ.

Ambiguity

The Actor’s Intent has multiple plausible interpretations.

Evidence Conflict

Authoritative or purportedly authoritative sources disagree about the underlying facts.

Example:

Ambiguity:
"Delete the account."
Which account?
Conflict:
Two systems disagree about who owns the account.

They require different handling.

⸻

31. Evidence Completeness

A decision may require multiple pieces of evidence.

Example:

To transfer funds:
Actor identity
Source account
Destination account
Balance
Authorization
Transfer limits

If one material piece is missing:

Transfer:
NOT READY FOR TRUST DECISION

Noema should not fill the gap with an assumption.

⸻

32. Evidence Sufficiency

Evidence does not need to be exhaustive.

It needs to be sufficient for the decision being made.

For example, viewing a public product description may require little evidence.

Transferring ₦10 million requires considerably stronger evidence.

Therefore:

Evidence requirements should be proportional to the consequence of the Intent.

⸻

33. Evidence and Risk

High-risk Actions should require stronger evidence.

Conceptually:

Risk ↑
Evidence requirement ↑

For example:

Read public information
    → minimal verification
Delete account
    → identity + authorization
Transfer large funds
    → identity + authorization + confirmation + policy checks

⸻

34. Evidence and Consequence

Evidence requirements should correspond to potential impact.

Consequential categories include:

financial
destructive
security
privacy
legal
production infrastructure
external communication

The greater the consequence, the less acceptable unsupported inference becomes.

⸻

35. Evidence and Determinism

Evidence is one of the mechanisms that converts probabilistic interpretation into deterministic commitment.

Model hypothesis
      ↓
Evidence gathering
      ↓
Evidence validation
      ↓
Resolved Intent

Without evidence, Noema may need to remain uncertain.

⸻

36. Evidence Does Not Eliminate Uncertainty

Evidence can still be:

incomplete
conflicting
stale
low-authority
ambiguous

Therefore Noema must be capable of representing:

UNKNOWN
UNVERIFIED
CONFLICTING
INSUFFICIENT

rather than forcing a binary answer.

⸻

37. Evidence Status

A useful conceptual state model:

UNVERIFIED
    ↓
OBSERVED
    ↓
VALIDATED
    ↓
SUFFICIENT

Possible failure paths:

OBSERVED
   ↓
STALE
OBSERVED
   ↓
CONFLICTING
OBSERVED
   ↓
REVOKED

These are conceptual states, not necessarily required implementation enums.

⸻

38. Evidence Observation vs Validation

These must remain distinct.

Observation

A source reported this fact.

Validation

Noema established that the evidence is sufficiently trustworthy for the intended decision.

Example:

External API:
"User is Admin."

Observation:

Admin claim received.

Validation:

Source authenticated.
Claim current.
Claim applicable to Tenant A.

Only then should the claim be used for a high-impact Trust decision.

⸻

39. Evidence Authority

Authority is contextual.

A source may be authoritative for one proposition but not another.

Example:

Ledger:
authoritative for account balance
CRM:
authoritative for customer profile
Identity Provider:
authoritative for authentication

Noema should avoid treating a source as universally authoritative.

⸻

40. Source Authority

A useful conceptual relationship:

Source
   ↓
authoritative_for
   ↓
Claim Type

For example:

Ledger
   ↓
authoritative_for
   ↓
AccountBalance

This is stronger than a generic:

Ledger = trusted

⸻

41. Evidence Scope

Evidence should have a scope.

Example:

User#123 is Admin

may mean:

Admin within Organization#ABC

not:

Admin everywhere.

Evidence must therefore preserve relevant scope.

⸻

42. Evidence Context

A fact may only be valid within a context.

Example:

User#123
has role:
Reviewer
Context:
Project#ABC

That does not necessarily establish:

User#123
has role:
Reviewer

globally.

⸻

43. Evidence and Tenant Isolation

Evidence must respect tenant boundaries.

A claim from Tenant A should not automatically establish a claim within Tenant B.

This is especially important for:

identity
authorization
ownership
configuration
policy
resources

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

This evidence establishes whether the Agent can act on the Principal’s behalf.

⸻

45. Evidence and Provenance Chains

A delegated decision might require:

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

46. Evidence and External Assertions

External systems can make assertions.

Example:

Shipping Provider:
Package#123 delivered.

Noema may use this as evidence for:

Order#456 can be refunded.

But it should preserve:

source = ShippingProvider
claim = delivered
observed_at = ...

rather than treating the assertion as an unqualified fact.

⸻

47. Evidence and Events

Events can provide temporal evidence.

Example:

PaymentCompleted
at 14:03

This can establish:

Payment#123 was completed at 14:03.

Events are particularly useful when determining state transitions.

⸻

48. Evidence and Business State

Noema should consume business state as evidence rather than duplicate ownership of that state.

For example:

Business System:
Order.status = shipped

Noema can use this to evaluate:

Intent:
CancelOrder(Order#123)

Policy:

Shipped orders cannot be cancelled.

The business system remains authoritative for the Order.

⸻

49. Evidence and Intent State

Noema may own the state of an Intent:

Intent#123
status = awaiting_confirmation

This itself can become evidence for later decisions.

For example:

Evidence:
Intent#123 was explicitly confirmed by Actor#456.

⸻

50. Evidence and Identity

Identity evidence establishes who is acting.

Examples:

authenticated session
signed token
verified credential
service identity
delegated identity

Noema should distinguish:

claimed identity

from:

verified identity

⸻

51. Evidence and Actor Claims

Actors can provide evidence through statements.

Example:

“My account number is 123456.”

This is an Actor assertion.

It may be useful for resolution.

But for high-risk Actions it may require independent verification.

The system should not automatically elevate:

Actor assertion

to:

authoritative fact

⸻

52. Evidence and User Intent

The Actor’s expression is evidence of what the Actor said.

It is not necessarily evidence that every proposition inside the expression is true.

Example:

“Transfer money from my account to John’s account.”

This establishes:

Actor wants TransferFunds.

It does not establish:

John's account is Account#456.

That requires additional evidence.

⸻

53. Evidence and Natural-Language Claims

Natural language can contain multiple claims:

“Send $500 to John because he owns the company account.”

This contains:

Intent:
Send $500
Entity:
John
Claim:
John owns the company account

Noema must not treat the entire sentence as equally authoritative.

The Intent may come directly from the Actor.

The ownership claim may require external evidence.

⸻

54. Evidence and Semantic Parsing

The Model may extract:

Claim A
Claim B
Intent C

but extraction is not validation.

This distinction should remain explicit:

Extraction
   ≠
Validation

⸻

55. Evidence and Model Grounding

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

56. Evidence Retrieval

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

57. Evidence Retrieval Must Be Scoped

Noema should retrieve only evidence relevant to the current Intent and Context.

Example:

Intent:
Refund Order#123

Relevant:

Order status
Payment status
Refund policy
Actor authorization

Irrelevant information should not become part of the Trust basis merely because it was available.

⸻

58. Evidence and Privacy

Evidence may contain sensitive information.

Therefore evidence handling must respect:

access controls
data minimization
tenant isolation
retention requirements
privacy policies

Trust does not imply unrestricted access to evidence.

⸻

59. Evidence Minimization

Noema should use the minimum evidence required to establish the decision.

For example, authorization may require:

User#123 has permission X

It may not require exposing the user’s entire profile.

This reduces unnecessary data exposure.

⸻

60. Evidence Disclosure

The Actor may not always be entitled to see the evidence behind a Trust decision.

For example:

Internal authorization rule:
Confidential

The system may communicate:

“You are not authorized to perform this action.”

without exposing the internal policy.

⸻

61. Evidence and Security

Evidence itself can be attacked.

Threats include:

forged evidence
stale evidence
tampered evidence
spoofed source
replayed credentials
cross-tenant evidence
injected documents
malicious claims

Therefore high-trust evidence may require cryptographic or system-level verification.

⸻

62. Evidence Authenticity

Where appropriate, Noema should establish:

Who produced the evidence?
Was it altered?
Is the source authentic?
Is the evidence intended for this system?

The mechanism could involve:

signatures
authenticated APIs
trusted channels
versioned records

The canonical requirement is provenance and authenticity appropriate to consequence.

⸻

63. Evidence Replay

Evidence may be valid when first issued but invalid later.

Example:

Authorization token:
issued 09:00
revoked 09:30

Replaying the token at 10:00 must not necessarily establish current authority.

Evidence must therefore account for revocation and freshness.

⸻

64. Evidence and Temporal Ordering

Some decisions depend on ordering.

Example:

PaymentCreated
PaymentSettled
PaymentRefunded

If the Actor asks:

“Refund the payment.”

Noema may need to establish the current state and event history.

Evidence ordering can matter.

⸻

65. Evidence and Causality

For complex workflows, evidence may establish causal relationships.

Example:

PaymentCompleted
    ↓
OrderEligibleForFulfillment
    ↓
OrderShipped

The causal chain can support downstream decisions.

Noema should preserve causal relationships where material to Trust.

⸻

66. Evidence and Composite Intents

A composite Intent may require separate evidence for each component.

Example:

RefundPayment(Payment#123)
AND
CloseAccount(Account#456)

Evidence needed for the refund may differ from evidence needed for account closure.

Noema should not assume that evidence sufficient for one child Intent automatically establishes the other.

⸻

67. Evidence and Partial Resolution

Some evidence may resolve only part of an Intent.

Example:

"Transfer $500 to John."

Evidence establishes:

Amount = $500

but not:

John = Account#456

The Intent remains partially unresolved.

Noema should preserve this state instead of pretending the Intent is complete.

⸻

68. Evidence and Clarification

When evidence is insufficient, Noema can ask the Actor for information.

Example:

Noema:
Which John do you mean?

The Actor’s response becomes additional evidence.

This creates an evidence acquisition loop:

Intent
 ↓
Missing evidence
 ↓
Clarification
 ↓
Actor response
 ↓
New evidence
 ↓
Resolution

⸻

69. Evidence and Explicitness

Evidence should be as explicit as the consequence requires.

Low consequence:

Implicit contextual evidence may be sufficient.

High consequence:

Explicit confirmation or authoritative verification may be required.

Noema should not use one universal evidence threshold.

⸻

70. Evidence Threshold

Conceptually:

Required Evidence Strength
        ∝
Potential Consequence

This should guide Trust design.

⸻

71. Evidence Quality Dimensions

Evidence quality can be evaluated across:

Authority
Authenticity
Freshness
Specificity
Completeness
Scope
Consistency
Provenance
Applicability
Integrity

Not every decision requires every dimension.

⸻

72. Evidence Weighting

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

73. Evidence vs Evidence Score

An evidence score can be useful operationally.

But:

A score must not replace the semantics of evidence.

For example:

0.93 evidence confidence

does not tell us:

who produced the evidence
what it establishes
whether it is current
whether it applies

Those properties matter more.

⸻

74. Evidence Aggregation

Multiple evidence items can collectively establish a claim.

Example:

Evidence A:
User authenticated.
Evidence B:
User owns Account#123.
Evidence C:
Account#123 is active.

Together:

User#123 may initiate a transfer from Account#123.

Aggregation should be governed by explicit rules.

⸻

75. Evidence Invalidation

A Trust decision may become invalid if its underlying evidence becomes invalid.

Example:

Authorization decision:
ALLOWED
Underlying permission:
revoked

For long-running workflows, Noema may need to re-evaluate Trust before the final side effect.

⸻

76. Evidence at Execution Time

For high-impact Actions:

Intent resolved
      ↓
Evidence collected
      ↓
Trust decision
      ↓
Execution delayed

If the delay is significant, the system may need to revalidate material evidence.

⸻

77. Evidence and Long-Running Intents

An Intent can remain active for hours or days.

Example:

"Deploy this release after approval."

Evidence collected Monday may no longer be valid Tuesday.

Noema should distinguish:

evidence at resolution

from:

evidence at execution

where relevant.

⸻

78. Evidence and Trust Re-Evaluation

A long-running Intent may require:

Resolution
    ↓
Initial Trust
    ↓
Waiting
    ↓
State change
    ↓
Revalidation
    ↓
Final Trust
    ↓
Execution

This prevents stale evidence from authorizing consequential side effects.

⸻

79. Evidence and Auditability

Every material Trust decision should ideally be traceable to evidence.

Example:

Decision#123
    ├── Intent#456
    ├── Evidence#1
    ├── Evidence#2
    ├── Policy#7
    └── AuthorizationRule#12

This creates an auditable decision graph.

⸻

80. Evidence and Reproducibility

A deterministic decision can only be meaningfully reproduced if its material evidence can be identified.

Therefore:

Decision
   ↓
Evidence References
   ↓
Source Versions

should be preserved where practical.

⸻

81. Evidence Retention

Evidence retention should depend on:

legal requirements
audit requirements
privacy requirements
security requirements
business requirements

Noema should not retain evidence indefinitely by default.

⸻

82. Evidence Ownership

Noema may reference evidence owned by another system.

For example:

Ledger owns balance state.

Noema should preserve a reference to the authoritative evidence rather than necessarily copying the entire record.

This reinforces:

Noema owns Trust decisions, not every piece of Business State.

⸻

83. Evidence and the Canonical Repository

The Ontology should define what kinds of things can act as evidence.

The Trust layer defines:

how evidence is evaluated
how evidence supports decisions
how evidence conflicts are handled
how evidence is preserved

This separation keeps the repository coherent.

⸻

84. Evidence Relationship to Other Trust Concepts

Ambiguity
    ↓
determines whether evidence is sufficient to resolve meaning
Authorization
    ↓
uses evidence to establish permission
Determinism
    ↓
requires decisions to be grounded in evidence
Policy
    ↓
uses evidence to evaluate applicable rules
Trust
    ↓
aggregates evidence-backed decisions

⸻

85. Canonical Evidence Flow

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

⸻

86. Canonical Invariants

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

⸻

87. The Fundamental Distinction

The most important distinction is:

Model:
"This is probably true."
Evidence:
"This source establishes this claim."
Noema:
"This claim is sufficiently established for this decision."

These are three different states.

⸻

88. Final Definition

Evidence is the attributable, contextual, and appropriately authoritative basis by which Noema establishes claims about Actors, Intents, Resources, state, permissions, policies, capabilities, and other conditions required for deterministic Trust decisions.

The shortest canonical formulation is:

Noema does not trust an interpretation because the Model is confident; it trusts a decision because the necessary claims are supported by sufficient evidence.