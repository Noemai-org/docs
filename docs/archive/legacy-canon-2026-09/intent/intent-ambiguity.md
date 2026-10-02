> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Ambiguity

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-ambiguity.md

⸻

1. Definition

Intent Ambiguity is the condition in which an Actor’s expression admits multiple materially distinct interpretations and available evidence is insufficient to determine which interpretation represents the Actor’s intended meaning.

Ambiguity is therefore not simply:

The Model is uncertain.

It is:

Multiple materially valid semantic interpretations remain, and the distinction matters.

The canonical relationship is:

Actor Expression
       ↓
Candidate Interpretations
       ↓
Hard Schema Validation
       ↓
Admitted Intent
       ↓
Evidence + Context + State Reconciliation
       ↓
Candidate Reduction
       │
       ├── One materially valid interpretation
       │          ↓
       │      Resolved Intent
       │          ↓
       │   Executable Intent
       │
       └── Multiple materially valid interpretations
                  ↓
              Ambiguity
                  ↓
             Clarification
                  ↓
          New Intent Version

Ambiguity is therefore a semantic property of an admitted Intent and its unresolved claims, not a property of the Model alone.

⸻

2. Purpose

Intent Ambiguity exists so that Noema can distinguish between:

1. an Intent that is merely expressed imperfectly,
2. an Intent that can be resolved using available evidence,
3. an Intent that remains materially ambiguous,
4. an Intent that is underspecified because required information is unavailable,
5. an Intent whose requirements conflict with authoritative state or policy.

This distinction prevents Noema from treating every uncertainty as a reason to ask the Actor while also preventing probabilistic interpretation from silently becoming semantic authority.

The objective is:

Resolve what can be resolved deterministically, identify what cannot, and request only the information necessary to establish the intended meaning.

⸻

3. Why Intent Ambiguity Exists

Human language is inherently underspecified.

An Actor may omit:

* Actor
* Resource
* Recipient
* Scope
* Time
* Amount
* Action
* Context
* Constraints
* Expected Outcome

or refer to them indirectly:

"Send it to John."
"Delete the old one."
"Renew my card."
"Give Sarah the same access."

The Actor may consider these expressions understandable because they possess contextual knowledge that is not explicitly encoded in the expression.

Noema must determine whether that missing semantic information can be recovered from valid Context, enterprise state, Evidence, relationships, Constraints, and other authoritative sources without guessing.

⸻

4. Ambiguity Is Not the Same as Uncertainty

These concepts must remain distinct.

Uncertainty

Uncertainty concerns the strength or quality of support for a claim or interpretation.

Ambiguity

Ambiguity exists when multiple materially distinct interpretations remain possible.

For example:

"Send it to John."

If there is exactly one John but the Model is only moderately confident that “it” refers to the current document, there may be uncertainty.

If there are three valid recipients:

John Smith
John Doe
John Williams

and available evidence cannot distinguish them, there is ambiguity.

The useful distinction is:

Uncertainty:
How strongly is a candidate supported?
Ambiguity:
How many materially valid candidates remain?

A single candidate may have low confidence without being ambiguous.

Multiple candidates may exist without creating material ambiguity if Constraints or Policy eliminate all but one.

⸻

5. Ambiguity Is Not Always a Problem

Noema should not attempt to eliminate every linguistic ambiguity.

Some ambiguity is immaterial.

Example:

"Send Sarah the report quickly."

Suppose “quickly” could mean:

within 2 minutes
within 5 minutes
within 10 minutes

but the available Action sends the report immediately and the distinction has no effect on the resulting Action or Outcome.

Then:

Ambiguity exists
       ↓
No material consequence
       ↓
No blocking resolution required

The canonical rule is:

Only ambiguity that can materially affect the resulting Intent, Action, Trust evaluation, execution, or Outcome requires resolution.

This does not mean Noema may ignore ambiguity arbitrarily. The semantic distinction must genuinely be immaterial to the consequential operation.

⸻

6. Material Ambiguity

An ambiguity is material when selecting between candidate interpretations could change one or more consequential semantic properties, including:

* Actor
* Action
* Resource
* Entity
* Capability
* Parameter
* Scope
* Constraint
* Authority
* Policy evaluation
* Expected Outcome
* Execution path

Example:

"Delete the old customer account."

If two accounts satisfy the description and selecting the wrong one would produce a different Action target:

Account A
Account B

the ambiguity is material.

Therefore:

Material Ambiguity
       ↓
Intent cannot become Executable Intent
       ↓
Resolution required

Materiality is consequence-dependent. The same unresolved field may be immaterial for one Action and consequential for another.

⸻

7. Ambiguity as a Candidate Set

A useful conceptual model is:

Expression
    ↓
{Candidate₁, Candidate₂, Candidate₃, ...}

For example:

"Close my account."

could initially produce:

Candidate 1:
CloseBankAccount(Account A)
Candidate 2:
CloseBankAccount(Account B)
Candidate 3:
CloseInvestmentAccount(Account C)

Noema then evaluates available evidence, Context, State, Constraints, relationships, and applicable policy restrictions.

If one materially valid candidate remains, the Intent can be resolved.

If multiple materially valid candidates remain, the Intent is ambiguous.

⸻

8. Candidate Interpretations Must Be Semantically Distinct

Noema should not treat superficial linguistic variation as semantic ambiguity.

For example:

"Cancel my subscription."
"Please cancel my subscription."
"I want my subscription cancelled."

may all resolve to:

CancelSubscription

These are different expressions but not materially different Intent candidates.

Ambiguity exists when candidate interpretations represent materially different semantic states, targets, actions, constraints, or outcomes.

⸻

9. Types of Intent Ambiguity

Intent ambiguity can arise at different semantic layers.

Common categories include:

* Actor ambiguity
* Entity ambiguity
* Resource ambiguity
* Action ambiguity
* Capability ambiguity
* Parameter ambiguity
* Scope ambiguity
* Context ambiguity
* Temporal ambiguity
* Spatial ambiguity
* Reference ambiguity
* Constraint ambiguity
* Outcome ambiguity

These categories should remain conceptually distinct because their resolution strategies may differ.

⸻

10. Actor Ambiguity

Actor ambiguity occurs when Noema cannot establish which Actor is responsible for the Intent.

Example:

"Approve the invoice for me."

Potential interpretations may involve:

Current user
Manager
Finance department
Company representative

Actor resolution is particularly consequential because Authority and Policy evaluation may depend on the resolved Actor.

Noema must not infer Authority merely because an Actor candidate appears plausible.

Actor identity and authorization remain separate concerns.

⸻

11. Entity Ambiguity

Entity ambiguity occurs when an expression refers to multiple possible Entities.

Example:

"Send it to Alex."

Possible candidates:

Alex Johnson
Alex Smith
Alex Brown

If multiple candidates remain materially valid after available evidence is evaluated:

CLARIFY

The clarification should identify the exact distinction required rather than asking the Actor to restate the entire request.

⸻

12. Resource Ambiguity

Resource ambiguity occurs when the target Resource cannot be uniquely identified.

Example:

"Delete the project."

Possible Resources:

Project Alpha
Project Beta
Project Gamma

If Context, explicit references, enterprise state, or other Evidence cannot uniquely establish the intended Resource, the Intent remains materially ambiguous.

⸻

13. Action Ambiguity

Action ambiguity occurs when the Actor’s desired operation itself is unclear.

Example:

"Fix the customer account."

Potential Actions:

UpdateProfile
ResetPassword
UnlockAccount
RestoreSubscription

Context, current state, stated Outcome, and domain-specific relationships may reduce the candidate set.

If materially different Actions remain valid, Noema must not select one merely because it is statistically more probable.

Resolution or clarification is required.

⸻

14. Capability Ambiguity

Capability ambiguity occurs when multiple Capabilities could satisfy the same high-level Intent and the distinction materially affects execution, policy, or expected Outcome.

Example:

"Notify the customer."

Potential Capabilities:

Email
SMS
PushNotification

Noema may select a Capability through bounded enterprise configuration, Context, Policy, and the Enterprise Action Graph when those establish a deterministic path.

If the delivery channel materially matters and cannot be established:

CLARIFY

Capability selection must remain bounded by the Capability Registry and Enterprise Action Graph. The Model must not invent an unavailable Capability.

⸻

15. Parameter Ambiguity

Parameter ambiguity occurs when a required parameter admits multiple materially valid values.

Example:

"Transfer $500."

Potential destinations:

Savings Account
Checking Account
Brokerage Account

The amount is resolved.

The destination is not.

If the destination materially affects the Action, the Intent remains ambiguous.

A parameter should not be defaulted merely because one value is statistically common.

⸻

16. Scope Ambiguity

Scope ambiguity concerns the boundaries within which an Action applies.

Example:

"Give David access."

Potential scopes:

Repository
Workspace
Organization
Project
Environment

If scope changes the resulting Authority, Action, Policy evaluation, or Outcome, the scope must be resolved.

Scope should therefore be represented explicitly in the canonical Intent where it is consequential.

⸻

17. Temporal Ambiguity

Temporal ambiguity occurs when a temporal expression admits multiple materially different interpretations.

Examples:

"Schedule it for Friday."
"Send this later."
"Cancel the meeting tomorrow."

Questions may include:

Which Friday?
What time?
Which timezone?
Which occurrence?

Temporal ambiguity may be resolved through validated Context, explicit scheduling configuration, or deterministic defaults when those are valid and non-material.

If timing materially affects the Action and cannot be resolved:

CLARIFY

Temporal validity should be evaluated against the relevant Intent, Action, Policy, and current state rather than treated as a universal property.

⸻

18. Spatial Ambiguity

Spatial ambiguity occurs when a location reference cannot be sufficiently resolved.

Example:

"Book the flight from London."

Possible departure locations:

Heathrow
Gatwick
Stansted

If airport selection materially affects the Action or Outcome and available Context cannot establish the intended location:

CLARIFY

⸻

19. Reference Ambiguity

Reference ambiguity occurs when pronouns, aliases, descriptions, or contextual references can refer to multiple Resources or Entities.

Examples:

"Send it to her."
"Delete that one."
"Use the other account."

Noema should resolve references through available Context, explicit references, enterprise state, Evidence, and semantic relationships.

If multiple materially valid references remain:

CLARIFY

Reference resolution must preserve the resolved Resource or Entity binding rather than leaving the Action to reinterpret the original expression later.

⸻

20. Constraint Ambiguity

Sometimes the Action is clear but the Constraints governing how it should be performed are not.

Example:

"Book me the cheapest flight."

Potential interpretations:

Absolute lowest price

versus:

Lowest price satisfying acceptable travel constraints

where acceptable could include:

Departure time
Arrival time
Checked baggage
Preferred airport
Number of stops

If these interpretations materially change the resulting Action or Outcome, the relevant Constraints must be resolved.

Noema should not silently manufacture preferences that materially affect the requested Outcome.

⸻

21. Outcome Ambiguity

Outcome ambiguity occurs when an expression describes a desired result that could correspond to multiple materially different outcomes.

Example:

"Get the customer back online."

Potential Outcomes:

Unlock account
Reset password
Restore subscription
Restore network access

Context, current state, enterprise configuration, and domain relationships may establish the appropriate semantic Outcome.

However, Noema must distinguish:

Desired Outcome

from:

Implementation Action

The Actor may specify an Outcome without specifying the implementation.

The Planner may select an implementation only within the bounded Enterprise Action Graph, Capability Registry, and Action Contracts.

⸻

22. Ambiguity and Context

Context is one of the primary mechanisms for resolving ambiguity.

Example:

Current screen:
Invoice #9281
Actor:
"Refund this."

Context may provide:

Resource = Invoice #9281

The Intent may therefore become resolved without asking the Actor.

However:

Context is not inherently authoritative.

Context must be evaluated for:

* Relevance
* Scope
* Freshness
* Authority
* Consistency
* Temporal validity

Proximity alone is not sufficient evidence.

⸻

23. Ambiguity and State Reconciliation

Current enterprise state can reduce or eliminate ambiguity.

For example:

Actor:
"Renew my card."

Enterprise state:

Card A → expired
Card B → active

If the applicable renewal rules establish that only expired cards are eligible, the candidate set may reduce deterministically to Card A.

State Reconciliation is therefore a first-class resolution mechanism.

The canonical distinction is:

Retrieved State
       ↓
State Reconciliation
       ↓
Reconciled State
       ↓
Candidate Reduction
       ↓
Resolution

Noema should not ask the Actor to resolve an ambiguity that authoritative current state can deterministically resolve.

⸻

24. Ambiguity and Evidence

Noema should attempt to resolve material ambiguity through available Evidence before asking the Actor.

Conceptually:

Ambiguity
    ↓
Evaluate authoritative sources
    ↓
Evaluate relevant Context
    ↓
Evaluate Resources and relationships
    ↓
Reconcile current state
    ↓
Apply Constraints
    ↓
Apply policy-derived restrictions
    ↓
Reduce candidates
    ↓
Resolved?
   /   \
 Yes    No
  ↓      ↓
Resolve Clarify

Evidence does not become authoritative merely because it was retrieved.

Its authority, freshness, scope, provenance, and consistency must be evaluated for the claim being resolved.

⸻

25. Ambiguity and Confidence

Confidence may help rank candidate interpretations.

Example:

John Smith: 0.81
John Doe:   0.19

But ranking is not resolution.

If both candidates remain materially valid:

Ambiguous

even though one candidate has a higher Model score.

The canonical rule is:

Model confidence may inform candidate evaluation but cannot by itself establish semantic resolution.

Confidence is an epistemic signal. It is not Authority, Fact Status, Trust, or authorization.

⸻

26. Ambiguity and Deterministic Resolution

Where authoritative evidence can establish a unique answer, ambiguity should be eliminated deterministically.

Example:

Actor:
"Renew my card."
Available cards:
Card A — expired
Card B — active

Applicable eligibility condition:

Only expired cards may be renewed.

Therefore:

Resource = Card A

The Intent is resolved without clarification.

This is preferable to asking the Actor when the enterprise state already contains sufficient evidence.

⸻

27. Ambiguity and Clarification

When material ambiguity remains after available resolution mechanisms have been exhausted, clarification is required.

Clarification should identify the exact unresolved semantic dimension.

Bad:

"Can you clarify?"

Good:

"Which card do you want to renew: the corporate card ending 1234 or the virtual card ending 5678?"

The second formulation:

* localizes the ambiguity,
* exposes the bounded candidates,
* asks only for the missing distinction,
* preserves the rest of the resolved Intent.

Clarification is a resolution mechanism. It does not grant authority, establish enterprise truth, bypass Trust, or imply execution success.

⸻

28. Ambiguity Must Be Localized

Noema should identify precisely where the ambiguity exists.

Example:

Intent:
RefundPayment
Actor:
RESOLVED
Action:
RESOLVED
Customer:
RESOLVED
Payment:
AMBIGUOUS
Amount:
RESOLVED

This is superior to representing the entire Intent as:

Intent:
UNCERTAIN

Localization makes the resolution state inspectable and enables targeted clarification.

⸻

29. Ambiguity Should Not Propagate Unnecessarily

If one semantic claim is ambiguous, Noema should not automatically mark unrelated claims as ambiguous.

Example:

Actor:      Alice       RESOLVED
Action:     Refund      RESOLVED
Customer:   John        RESOLVED
Payment:    ?           AMBIGUOUS
Amount:     $500        RESOLVED

Only the unresolved material claim blocks progression.

This preserves the distinction between:

Known
Unknown
Ambiguous
Conflicted

and prevents uncertainty from contaminating the entire Intent representation.

⸻

30. Ambiguity and Executable Intent

An Intent containing unresolved material ambiguity cannot become an Executable Intent.

Material Ambiguity
       ↓
Intent Unresolved
       ↓
No Executable Intent

After sufficient resolution:

Resolved Intent
       ↓
Executable Intent

Executable Intent is the semantic handoff to deterministic Trust evaluation.

It does not mean the Intent is authorized or that execution will succeed.

⸻

31. Ambiguity and Trust

Trust must not resolve materially ambiguous semantics by selecting a best guess.

The canonical sequence is:

Intent
   ↓
Ambiguity Detection
   ↓
Resolution / Clarification
   ↓
Executable Intent
   ↓
Trust Evaluation
   ↓
EXECUTE / CLARIFY / ESCALATE / REJECT
   ↓
Action

Not:

Ambiguous Intent
       ↓
Trust
       ↓
Best Guess
       ↓
Action

Trust evaluates whether a sufficiently resolved Intent may proceed under applicable authority, policy, constraints, capability, and current state.

Trust does not substitute for semantic resolution.

⸻

32. Ambiguity and Policy

Policy may reduce ambiguity by eliminating candidates that are not eligible.

Example:

Actor:
"Refund the payment."

Two payments exist.

Applicable policy:

Only payments made within the last 24 hours are refundable.

If only one payment satisfies the relevant eligibility condition:

Payment #8291

the candidate set may become deterministic.

However:

Policy may constrain candidate space, but it must not invent the Actor’s Intent.

Policy may eliminate invalid candidates. It should not arbitrarily choose between multiple materially valid candidates merely because one is more convenient to execute.

⸻

33. Ambiguity and Constraints

Constraints can similarly reduce candidate space.

Example:

"Send the report to the finance team."

Potential groups:

Finance
Finance Operations
Finance Leadership

Constraint:

Recipient must be a team with external-email capability.

If only one candidate satisfies the relevant constraint, ambiguity may be eliminated.

Constraints must themselves be resolved and valid before they are used to establish semantic uniqueness.

⸻

34. Ambiguity and Negative Evidence

Noema should evaluate evidence that eliminates candidates, not only evidence that supports candidates.

Example:

"Renew my card."

Two cards match the expression:

Card A → inactive
Card B → active

If the Action requires an eligible card and only Card B satisfies the relevant condition, the ineligible candidate can be eliminated.

Negative evidence therefore contributes to candidate reduction.

The elimination must be based on authoritative or otherwise valid evidence and applicable deterministic rules.

⸻

35. Ambiguity and Contradiction

Ambiguity and contradiction are distinct semantic conditions.

Ambiguity

Multiple interpretations remain possible.

Contradiction

Available information directly conflicts.

Example:

Actor:
"Send it to John Smith."
Directory:
John Smith exists.

There may be no ambiguity about the recipient.

But if the current authorization state establishes:

John Smith is not an eligible recipient.

the problem is not recipient ambiguity. It is a conflict between the requested Intent and current authoritative state or policy.

The resulting Trust or execution behavior may be:

CLARIFY
ESCALATE
REJECT

depending on the applicable semantics.

Noema must not relabel contradictions as ambiguity merely because both can block execution.

⸻

36. Ambiguity and Missing Information

Missing information does not automatically equal ambiguity.

Example:

"Send the report."

If a workflow deterministically defines one recipient, the recipient may be supplied through valid Context.

If no recipient exists or can be established, the problem may be missing information rather than multiple competing interpretations.

The distinction is:

Ambiguity:
Multiple materially valid values remain.
Missing information:
No sufficient value is currently available.

Both may require clarification, but their semantic causes should remain distinct.

⸻

37. Ambiguity and Underspecification

Underspecification is broader than ambiguity.

Example:

"Send the report."

The expression may omit the recipient entirely.

There may be:

Zero established candidates

rather than:

Multiple candidates

Noema should distinguish:

Ambiguity:
Too many materially valid interpretations.
Underspecification:
Insufficient information to establish an interpretation.
Missing information:
A required value is unavailable from the currently valid sources.

These conditions may converge on clarification but should not be collapsed into one state.

⸻

38. Ambiguity Severity

Not every ambiguity carries the same consequence.

A conceptual classification may include:

Informational
Low
Material
High-risk
Critical

For example:

"Show me John's profile."

may have lower consequence than:

"Transfer John's $50,000."

Severity should influence the strength and quality of evidence required for resolution.

However, severity should not become a substitute for semantic analysis.

The question remains:

Can Noema establish the intended meaning sufficiently for the consequential operation?

⸻

39. Ambiguity and Consequence

A foundational principle is:

The greater the consequence of choosing incorrectly, the stronger the semantic resolution and evidentiary basis Noema must require.

This does not mean:

High consequence
       ↓
Ask every possible question

It means:

Higher consequence
       ↓
Higher cost of incorrect interpretation
       ↓
Stronger required resolution
       ↓
Less tolerance for unresolved material ambiguity

Noema should optimize for minimal necessary clarification, not maximal questioning.

⸻

40. Ambiguity Should Be Explainable

For every blocking ambiguity, Noema should be able to establish:

What is ambiguous?
What candidates exist?
Why are they materially different?
What evidence was considered?
What evidence eliminated candidates?
Why could the remaining candidates not be distinguished?
What clarification would resolve the distinction?

Example:

Ambiguous Field:
Resource
Candidates:
Card #1234
Card #5678
Reason:
Both are active cards owned by the Actor.
Evidence Considered:
Customer account state
Card status
Ownership records
Current Intent Context
Resolution:
Actor must select one.

This supports causal auditability without requiring disclosure of private Model chain-of-thought.

⸻

41. Ambiguity as a First-Class State

Ambiguity should not be represented solely as an error string.

Conceptually:

Intent Resolution State:
AMBIGUOUS

with associated structured information:

Ambiguous Claim
Candidates
Candidate Evidence
Materiality
Reason
Required Resolution
Intent Version
Provenance

Ambiguity therefore becomes inspectable state within the Intent lifecycle rather than an incidental conversational failure.

The exact lifecycle state should remain distinct from the four canonical Trust outcomes:

EXECUTE
CLARIFY
ESCALATE
REJECT

An ambiguous Intent may cause a Trust CLARIFY decision when unresolved ambiguity prevents safe Trust evaluation, but ambiguity itself is not synonymous with the Trust outcome CLARIFY.

⸻

42. Ambiguity and Auditability

For consequential workflows, Noema should preserve the ambiguity that existed before execution.

Example:

Original Intent:
"Renew my card."
Ambiguity:
Two eligible cards.
Clarification:
"Which card?"
Actor:
"Corporate card ending 1234."
Resolution:
Card #1234.
Intent Version:
v2 supersedes v1.
Action:
RenewCard(#1234).

This creates an auditable semantic chain from original expression through clarification, resolution, Action, and eventual Outcome.

Material clarification must create a new Intent version rather than silently mutating the admitted Intent.

⸻

43. Ambiguity Should Not Be Hidden by the Model

A Model may produce:

Card #1234

even when:

Card #1234
Card #5678

are both materially valid.

Noema must not treat the Model’s selection as semantic resolution merely because the Model produced a single output.

Model output is untrusted candidate-generation material.

Hard schema validation, semantic resolution, Evidence evaluation, State Reconciliation, and deterministic governance establish canonical Noema semantics.

⸻

44. Ambiguity and Retrieval

Retrieval can reduce ambiguity by introducing relevant Evidence.

Example:

Actor:
"Renew the card I used last month."

Retrieval finds:

Card #1234:
Used on July 18
Card #5678:
Never used

The candidate set may therefore reduce to:

Card #1234

Retrieval contributes Evidence to Intent resolution.

However, retrieved information must still be evaluated for:

* Authority
* Freshness
* Relevance
* Scope
* Provenance
* Consistency

Retrieval does not automatically establish Fact Status or authority.

⸻

45. Ambiguity and External State

External systems can introduce or remove ambiguity.

Example:

At T1:
One active card
At T2:
Two active cards

An Intent that was previously resolvable may become ambiguous under changed state.

Therefore ambiguity must be evaluated against the relevant state at the time of resolution and, where necessary, again against current state before execution.

State changes do not permit Noema to silently reinterpret a previously resolved Intent.

⸻

46. Ambiguity and Race Conditions

Consider:

Actor:
"Cancel my subscription."

At resolution:

Subscription #123

is uniquely identified.

Before execution, another subscription becomes associated with the Actor.

Noema must not reinterpret the original expression against the new state and silently switch the target.

The resolved Intent must remain semantically bound to:

Subscription #123

subject to current Trust, Action Contract, state, and execution checks.

Executable Intent therefore provides semantic binding across the transition from interpretation to execution.

⸻

47. Ambiguity and Intent Versioning

Clarification can change the semantic content of an Intent.

Because admitted Intent versions are immutable:

Intent v1
   ↓
Material Ambiguity
   ↓
Clarification
   ↓
Intent v2
   ↓
supersedes: v1
   ↓
Resolution

Noema must not mutate v1 in place to make the historical record appear as though the ambiguity never existed.

This preserves:

* Semantic lineage
* Auditability
* Provenance
* Reproducibility
* Causal explanation

A clarification that does not materially alter the semantic Intent may not require a new Intent version, but any material semantic change must.

⸻

48. Canonical Resolution Strategy

Noema should follow this general order:

1. Parse the expression.
        ↓
2. Generate candidate semantic interpretations.
        ↓
3. Hard schema validation and admission.
        ↓
4. Resolve Actor, Action, Resources, Parameters,
   Scope, Constraints, and Expected Outcome where applicable.
        ↓
5. Use authoritative Context.
        ↓
6. Reconcile relevant enterprise state.
        ↓
7. Evaluate relevant Evidence and relationships.
        ↓
8. Apply valid Constraints and policy-derived restrictions.
        ↓
9. Reduce the candidate set.
        ↓
10. Determine whether one materially valid
    interpretation remains.
        ↓
    ┌───────────────┐
    │ One candidate?│
    └───────┬───────┘
        YES │ NO
            │
        ┌───┴────┐
        ↓        ↓
     Resolve   Ambiguous
        │        │
        │        ↓
        │   Targeted Clarification
        │        │
        │        ↓
        │   New Intent Version
        │        │
        └────────┘
             ↓
       Executable Intent
             ↓
           Trust

This makes ambiguity handling systematic rather than conversationally improvised.

⸻

49. Canonical Ambiguity Rule

Noema must not collapse multiple materially valid interpretations into one merely because one interpretation is more probable.

It must either:

1. establish sufficient evidentiary basis for deterministic resolution, or
2. explicitly obtain the missing distinction from the Actor.

This is a foundational semantic and Trust invariant.

The shortest form is:

Probability may rank candidates. It may not authorize Noema to choose among materially valid alternatives without sufficient resolution.

⸻

50. What Intent Ambiguity Protects Against

Intent ambiguity handling protects against:

* Wrong Resource
* Wrong Recipient
* Wrong Action
* Wrong Scope
* Wrong Account
* Wrong Customer
* Wrong Environment
* Wrong Parameter
* Wrong Policy Evaluation
* Wrong Execution Path
* Wrong Outcome

It is therefore a foundational safety mechanism between probabilistic interpretation and deterministic execution.

⸻

51. What Intent Ambiguity Does Not Mean

Intent ambiguity does not mean:

* The Model failed.
* The Actor communicated badly.
* No Action is possible.
* Every missing field requires clarification.
* Every low confidence score is ambiguity.
* Every multiple-candidate situation is material ambiguity.
* The system must always ask the Actor.
* Trust should resolve semantic uncertainty by choosing the most probable candidate.

The objective is not maximal questioning.

The objective is correct semantic resolution with minimal necessary friction.

⸻

52. Canonical Principles

1. Ambiguity is a semantic condition, not a Model error.
2. Ambiguity concerns materially distinct interpretations, not superficial linguistic variation.
3. Only material ambiguity blocks progression toward Executable Intent.
4. Multiple candidates do not automatically constitute material ambiguity.
5. Missing information, underspecification, ambiguity, and contradiction are distinct conditions.
6. Confidence ranks or supports candidates; it does not establish semantic resolution by itself.
7. Authoritative Context should be evaluated before asking the Actor.
8. State Reconciliation is a first-class mechanism for reducing ambiguity.
9. Constraints and valid policy restrictions may eliminate candidates but must not invent the Actor’s Intent.
10. Retrieved information is Evidence, not automatically authoritative truth.
11. Model output must not silently collapse material ambiguity.
12. Ambiguity should be localized to the specific unresolved semantic claim.
13. Unrelated resolved claims should not become ambiguous merely because one claim is unresolved.
14. Material ambiguity prevents an Intent from becoming Executable Intent.
15. Clarification should request only the semantic distinction necessary for resolution.
16. Material clarification must preserve Intent lineage through immutable versioning.
17. Ambiguity resolution must remain auditable and causally explainable.
18. Trust must evaluate sufficiently resolved semantics rather than selecting a best guess.
19. Resolution does not imply authorization.
20. Executable Intent does not imply execution success.

⸻

53. Final Definition

Intent Ambiguity is the presence of multiple materially distinct interpretations of an Actor’s expression that remain valid after available Evidence, Context, State Reconciliation, Constraints, relationships, and applicable policy-derived restrictions have been evaluated, such that Noema cannot deterministically establish which interpretation represents the Actor’s intended meaning.

The canonical flow is:

Actor Expression
       ↓
Candidate Interpretations
       ↓
Hard Schema Validation
       ↓
Admitted Intent
       ↓
Evidence + Context + State Reconciliation
       ↓
Candidate Reduction
       ↓
┌──────────────────────────┐
│ One material candidate?  │
└────────────┬─────────────┘
             │
       ┌─────┴─────┐
       │           │
      YES          NO
       │           │
       ▼           ▼
  Resolved      Ambiguous
    Intent          │
       │            ▼
       │      Targeted Clarification
       │            │
       │            ▼
       │       New Intent Version
       │            │
       └────────────┘
              ↓
      Executable Intent
              ↓
            Trust
              ↓
            Action

The shortest canonical formulation is:

Ambiguity exists when Noema has more than one materially valid interpretation and insufficient evidence to establish which one the Actor intended.