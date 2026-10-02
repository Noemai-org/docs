> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Confidence

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/confidence.md

⸻

1. Definition

Confidence is an epistemic signal representing how strongly an interpretation, resolution, or inference is supported by available evidence.

Confidence is not authority, authorization, Trust, or an Outcome.

Noema may use confidence during semantic interpretation and resolution to determine whether additional resolution or evidence is required. Confidence alone must never authorize consequential execution.

The fundamental distinction is:

Confidence
    ↓
How strongly is this interpretation or claim supported?
Trust
    ↓
Are the resolved conditions sufficient to permit this Action?

Therefore:

Confidence informs resolution and Trust.
Confidence does not become Trust.

⸻

2. Why Confidence Exists

Human and system-generated Intent may be expressed through ambiguous, incomplete, contextual, or underspecified information.

Consider:

"Renew my card."

A Model may determine with high confidence that the requested semantic Action is:

RenewCard

But this does not necessarily establish:

Resource:
Card#123

Nor:

Actor:
Resolved principal

Nor:

Authority:
Actor is permitted to renew Card#123

Nor:

Current state:
Card#123 is eligible for renewal

Nor:

Policy:
Renewal is currently permitted

Confidence therefore operates at a specific semantic layer rather than representing a universal judgment about the entire Intent.

⸻

3. Confidence Is Not a Property of the Intent Alone

An Intent may contain multiple semantic claims or candidate resolutions with different confidence levels.

For example:

"Send the report to John."

may produce:

Intent:
SendReport
Confidence: 0.98
Resource:
QuarterlyReport
Confidence: 0.94
Recipient:
John Smith
Confidence: 0.61
Recipient:
John Doe
Confidence: 0.34

The high confidence of the Intent classification does not mean the recipient has been resolved.

The Intent cannot be considered safely resolved merely because its high-level classification is highly confident.

Confidence must therefore be associated with the specific claim, candidate, or resolution being evaluated.

⸻

4. Confidence Is Claim-Specific

Noema should conceptually distinguish confidence associated with different semantic claims.

Examples include:

Intent confidence
Entity confidence
Resource confidence
Action confidence
Parameter confidence
Context interpretation confidence
Capability-selection confidence
Outcome-verification confidence

For example:

Intent:
RefundPayment
Confidence: 0.99
Payment:
Payment#123
Confidence: 0.72
Actor:
Alice
Confidence: 1.00
Action:
RefundPayment
Confidence: 0.99

The weak Resource resolution may still block consequential execution.

Confidence must therefore be evaluated at the granularity relevant to the decision.

⸻

5. Sources of Confidence

Confidence may be informed by multiple sources.

Possible sources include:

Model interpretation
Structured input
Authoritative enterprise observations
Explicit human statements
Validated Context
Historical interaction
Entity matching
Deterministic rules
Domain constraints
State Reconciliation results

These sources do not necessarily have equal epistemic weight or authority.

For example:

Authenticated enterprise identity

may provide stronger support for Actor resolution than:

Model inference from conversation

However, authority and confidence remain distinct concepts.

A source may be authoritative for a particular claim without producing a numerical confidence score, while a Model may produce a high confidence score without possessing authority.

Confidence must therefore be interpreted together with evidence provenance, Fact Status, scope, freshness, and authority.

⸻

6. Confidence Is Not Model Probability

A Model may output:

0.97

for a candidate interpretation.

Noema must not automatically treat:

0.97

as a canonical probability that the interpretation is correct.

Model scores may be:

uncalibrated
model-specific
task-specific
context-sensitive
incomparable across models

Model confidence is therefore non-authoritative interpretation metadata.

It may inform candidate generation and resolution, but it does not establish a canonical fact or authorize an Action.

⸻

7. Confidence vs Certainty

Confidence and certainty are different concepts.

Confidence represents the strength of support for a claim or interpretation.

Established semantic state represents whether the claim has been sufficiently resolved and validated for the relevant decision.

For example:

Model confidence:
99%
Enterprise observations:
Two matching Resources exist.

The Model may be highly confident.

The Resource may still be unresolved.

Therefore:

High confidence ≠ resolved semantic state

Where applicable, Noema should rely on validated evidence, authoritative enterprise state, deterministic resolution, and explicit reconciliation rather than treating confidence as certainty.

⸻

8. Confidence vs Trust

This distinction is foundational.

Confidence asks:

How strongly is this interpretation or claim supported?

Trust asks:

Are the applicable conditions satisfied for Noema to permit this Action?

For example:

Model confidence:
0.99
Authority:
Insufficient

The resulting Trust decision cannot be EXECUTE.

Similarly:

Model confidence:
0.60
Actor:
Authoritatively resolved
Target:
Authoritatively resolved
Policy:
Satisfied
Required constraints:
Satisfied
Relevant enterprise state:
Reconciled

A lower Model confidence score does not automatically prevent execution if the uncertainty represented by that score has been resolved through stronger evidence and deterministic semantics.

Therefore:

Confidence ≠ Trust

Canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Confidence does not create, replace, or select among these outcomes.

⸻

9. Confidence vs Clarification

Confidence may contribute to determining whether clarification is necessary, but clarification must not be based solely on an arbitrary numerical threshold.

A weak model is:

confidence < 0.80
        ↓
CLARIFY

This is insufficient because a confidence score has no universal semantic meaning.

The relevant question is:

Is the required semantic claim sufficiently established
for this specific Intent, scope, Action, and consequence?

If not, Noema must obtain additional evidence, resolve the ambiguity, or use the appropriate control path.

Where a human can resolve a material semantic ambiguity:

CLARIFY

may be the appropriate Trust outcome.

Confidence is one input to this determination, not the decision rule itself.

⸻

10. Confidence Must Be Contextual

The amount and quality of evidence required depends on what is being established and the consequence of being wrong.

For example:

"Show me my profile."

may require less semantic resolution than:

"Delete the customer's account."

An incorrect interpretation of the second request can bind the wrong Resource or produce a materially different Outcome.

Therefore:

Required semantic resolution
        ↑
        │
        │       Higher consequence
        │          /
        │         /
        │        /
        │       /
        │      /
        └────────────────→ Consequence

This does not mean Noema should simply increase a numerical confidence threshold.

Higher consequence should generally require stronger semantic establishment, authoritative evidence, explicit resolution where necessary, and deterministic Trust evaluation.

⸻

11. Confidence Is Part of Semantic Resolution

Confidence can participate in Noema’s interpretation and resolution process.

Conceptually:

Source of Intent
       ↓
Candidate Interpretation
       ↓
Hard Schema Validation
       ↓
Evidence / Context / State Reconciliation
       ↓
Confidence / Interpretation Metadata
       ↓
Semantic Resolution
       ↓
Deterministic Trust

Confidence helps Noema evaluate which candidate interpretations have sufficient support to remain viable.

It does not itself establish canonical Intent semantics.

Once an Intent has been admitted and resolved, downstream execution should rely on the canonical semantic representation rather than repeatedly reinterpreting the original language.

⸻

12. Candidate Interpretations

A Model may produce multiple candidate interpretations.

For example:

User:
"Cancel my subscription."

Candidate interpretations:

CancelSubscription(Account#123)
Confidence: 0.91
CancelSubscription(Account#456)
Confidence: 0.08

If validated Context and current enterprise state establish that Account#123 is the relevant active subscription, the candidate may be resolved.

If multiple subscriptions remain materially valid:

CLARIFY

The highest-confidence candidate must not automatically win merely because its score is highest.

⸻

13. Confidence Should Not Hide Ambiguity

Suppose:

Candidate A: 0.51
Candidate B: 0.49

Selecting A merely because it has the highest score can conceal material ambiguity.

Likewise:

Candidate A: 0.95
Candidate B: 0.05

may still require clarification if the underlying evidence is weak or the Action is sufficiently consequential.

Therefore:

Candidate ranking ≠ semantic resolution

Resolution requires establishing the relevant semantic claim, not merely choosing the highest-ranked candidate.

⸻

14. Confidence and Evidence

A confidence value without provenance has limited semantic value.

Noema should conceptually be able to answer:

Why is this interpretation or resolution supported?

For example:

Recipient:
John Smith
Confidence:
High
Evidence:
1. Actor explicitly named "John Smith"
2. John Smith is present in relevant Context
3. Only one matching John Smith is available within the applicable scope

This is more useful than:

Recipient:
John Smith
Confidence:
0.94

Confidence should therefore be traceable to the evidence and interpretation process that produced it.

⸻

15. Evidence, Authority, and Fact Status

Confidence must not collapse distinct epistemic concepts into one value.

Noema distinguishes at least:

Evidence
Authority
Fact Status
Confidence

Fact Status describes the status of a claim or reconciled fact and may include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

A Model confidence score is not a Fact Status.

Likewise:

Evidence ≠ Fact Status
Confidence ≠ Authority
Confidence ≠ Evidence

An authoritative observation may establish a claim as VERIFIED without requiring a Model confidence score.

Conversely, a Model may be highly confident about a claim that remains UNVERIFIED, CONFLICTED, or UNKNOWN.

⸻

16. Evidence Quality and Provenance

Noema should prefer stronger and more relevant evidence over weaker inference.

A conceptual ordering might be:

Authoritative structured enterprise observation
        ↓
Validated explicit user clarification
        ↓
Validated contextual reference
        ↓
Deterministic domain rule
        ↓
Model-supported interpretation
        ↓
Pure probabilistic inference

This is not a universal ranking for every claim or domain.

Authority is claim-specific, and different sources may be authoritative for different facts.

The important principle is:

Confidence should reflect support and provenance.
Authority must be established independently.

Recency alone does not establish authority.

⸻

17. Confidence Should Be Composable Carefully

An Intent may contain many individually strong claims.

That does not mean the complete Intent is equally resolved.

For example:

Actor:       0.99
Action:      0.98
Resource:    0.62
Amount:      0.97
Destination: 0.91

The weak Resource resolution may dominate the relevant execution risk.

Noema should therefore avoid simplistic aggregation such as:

Overall confidence = average(all confidence values)

A high average does not establish a materially ambiguous Resource, Actor, Action, or parameter.

Confidence aggregation, where used, must preserve the semantics and criticality of individual claims.

⸻

18. Critical Claims

Some claims are critical to a particular Action.

Examples include:

Actor identity
Target Resource
Action type
Amount
Destination
Permission scope
Environment
Recipient
Organizational scope

A low-confidence or unresolved critical claim may prevent the Intent from reaching a deterministically executable state even when all other claims are strongly supported.

Conceptually:

Critical claim unresolved
        ↓
Intent not sufficiently resolved
        ↓
No consequential Action

The exact criticality of a claim is Action- and Contract-specific.

⸻

19. Non-Critical Claims

Other claims may not materially affect execution.

Examples include:

Preferred notification wording
Optional display label
Non-essential metadata

Low confidence in such claims should not necessarily block the Action.

Therefore:

Confidence requirements are semantic and Action-dependent.

The relevant question is whether uncertainty affects the semantics, authority, policy, constraints, target, scope, or expected behavior of the consequential operation.

⸻

20. Confidence and Constraints

Constraints can reduce the candidate space around an uncertain interpretation.

Example:

Intent:
"Book the cheapest flight to London."

Candidates:

Flight A: $700
Flight B: $680
Flight C: $1,200

A validated constraint:

Destination = London

eliminates irrelevant candidates.

Additional constraints may reduce the candidate space further.

Constraint satisfaction can therefore strengthen resolution, but confidence does not satisfy the constraint itself.

Deterministic constraints remain independently enforceable.

⸻

21. Confidence and Context

Context can increase support for an interpretation when it contains relevant, validated information.

Example:

Conversation:
"We've been discussing the Acme contract."
User:
"Send it to Sarah."

Context may support:

Resource:
Acme Contract

However, conversational proximity is not automatically sufficient evidence.

Context must be evaluated for:

relevance
scope
freshness
authority
Fact Status
provenance

Context is not inherently authoritative merely because it is present in Noema.

⸻

22. Confidence and State Reconciliation

Current enterprise state may resolve uncertainty that language alone cannot resolve.

For example:

User:
"Renew my current card."

Multiple cards may exist.

Noema may obtain observations from enterprise systems and perform:

Enterprise Systems of Record
        ↓
Validated Observations
        ↓
State Reconciliation
        ↓
Current Reconciled State
        ↓
Resource Resolution

If reconciliation establishes one current eligible card within the relevant scope, the semantic ambiguity may be resolved without asking the user.

If reconciliation produces:

CONFLICTED

or:

UNKNOWN

and the distinction is material, Noema must not convert that uncertainty into a confident guess.

Clarification, escalation, or rejection then depends on the deterministic rules governing the Intent and Action.

⸻

23. Confidence and Entity Resolution

Entity resolution is a major source of uncertainty.

Example:

"Send it to Mike."

Possible entities:

Mike Johnson
Mike Williams
Mike Brown

Confidence may rank these candidates.

But if multiple candidates remain materially plausible within the applicable scope:

CLARIFY

Entity confidence therefore contributes to Intent resolution without replacing deterministic identity resolution.

⸻

24. Confidence and Resource Resolution

Resources are especially important because selecting the wrong Resource can cause an otherwise valid Action to produce the wrong Outcome.

For example:

"Delete the old project."

Possible Resources:

Project A — archived
Project B — active
Project C — archived

The system must not equate:

"old"

with:

Project A

unless the applicable evidence, Context, and current enterprise state establish that relationship sufficiently.

A high-confidence Model guess does not create Resource authority or establish ownership.

⸻

25. Confidence and Action Selection

Sometimes the Intent is clear but multiple Actions can satisfy it.

Example:

"Make sure the customer gets their money back."

Possible Actions:

RefundPayment
IssueCredit
ReverseCharge
CreateCompensation

Noema should determine whether the domain, EAG, Capability Registry, Context, Policy, and Action semantics establish which Action satisfies the Intent.

If multiple Actions remain semantically valid and materially different:

CLARIFY

may be required.

If deterministic capability-selection or policy rules establish an Action, the planner may select only from the bounded EAG, Capability Registry, Action Registry, and Action Contracts.

The Model’s preference alone is insufficient.

⸻

26. Confidence and Outcome

Confidence may also appear in post-execution verification.

For example:

Expected Outcome:
Customer refunded
Observed enterprise evidence:
Payment status = refunded
Ledger entry created
Customer balance updated

Where Outcome verification can be established deterministically, those authoritative observations should establish the relevant result rather than relying on probabilistic confidence.

The distinction remains:

Confidence:
How strongly is an interpretation or observation supported?
Outcome:
What result has Noema established after execution and verification?

Confidence does not guarantee an Outcome.

Outcome also does not become enterprise Business State merely because Noema records it. Enterprise systems remain authoritative for enterprise business state.

⸻

27. Confidence Should Decrease or Become Invalid When Evidence Conflicts

Conflicting evidence must become an explicit resolution problem.

Example:

Model:
Customer = Acme Corp
CRM:
Customer = Acme Holdings
Billing:
Customer = Acme Corp

Noema must not simply select the Model interpretation with the highest confidence.

The conflict should be represented explicitly and evaluated according to source authority, scope, freshness, and reconciliation semantics.

Possible results include:

RESOLVE
CLARIFY
ESCALATE
REJECT

depending on the applicable deterministic rules.

Confidence cannot erase contradictory evidence.

⸻

28. Confidence Must Be Re-evaluated When Relevant State Changes

An Intent may remain active while enterprise state changes.

Example:

Intent:
Renew card before expiration.

At time T1:

Card:
Active
Eligible

At time T2:

Card:
Already renewed

The earlier interpretation or resolution may no longer support the same Action.

Noema must therefore resolve relevant semantic claims against current applicable state before consequential execution.

Confidence is not necessarily permanent.

More importantly, historical confidence does not override current authoritative state.

⸻

29. Confidence Has a Lifecycle

Conceptually:

Candidate
   ↓
Evidence
   ↓
Confidence / Interpretation Metadata
   ↓
Resolution
   ↓
Trust
   ↓
Action
   ↓
Verification

Confidence should be associated with the Intent version and evidence from which it was derived.

Where an admitted Intent is materially changed, the change creates a new Intent Object version rather than silently mutating the admitted version.

This preserves the relationship between:

Intent version
Evidence
Interpretation
Resolution
Trust Decision
Execution
Outcome

⸻

30. Confidence Must Be Explainable

For consequential Actions, Noema should be able to explain the semantic basis for accepting or rejecting a candidate resolution.

For example:

Resource:
Card#123
Resolution:
Resolved
Evidence:
- Actor owns Card#123
- Card#123 is the only active company card
- User explicitly referred to "my company card"
- Current enterprise state confirms eligibility

This is more useful than exposing only:

Confidence: 0.96

The objective is not to expose private Model chain-of-thought.

The objective is causal semantic traceability:

Claim
    ↓
Evidence
    ↓
Resolution
    ↓
Trust condition
    ↓
Decision

⸻

31. Confidence Is Not a User-Facing Promise

Noema should generally avoid communicating:

"I'm 99% sure."

as though the number were a guarantee.

A more meaningful interaction is:

"I found one active company card ending in 1234, so I can continue."

or:

"I found two active company cards. Which one do you mean?"

The system should communicate established facts and remaining ambiguity rather than exposing Model probabilities as guarantees.

⸻

32. Confidence and Determinism

The goal of the semantic pipeline is not to maximize confidence.

The goal is to establish the semantic conditions necessary for deterministic Trust and bounded execution.

Therefore:

Model / Evidence
       ↓
Confidence / Interpretation Metadata
       ↓
Semantic Resolution
       ↓
Validated and Reconciled State
       ↓
Deterministic Trust
       ↓
Bounded Action

These are related but distinct stages.

High confidence may provide useful support.

Deterministic resolution establishes the canonical semantic state required downstream.

⸻

33. Confidence Thresholds

Noema may use thresholds internally, but thresholds must not become universal Trust rules.

Where thresholds are used, they should be:

contextual
Action-specific
calibrated
evidence-aware
versioned where consequential

A universal rule such as:

confidence >= 0.90
        ↓
EXECUTE

must not be canonical.

For one interpretation task, a score may be useful for candidate generation.

For another, even a very high score may be insufficient because the underlying evidence is ambiguous, stale, conflicted, or unauthorized.

Trust must evaluate the applicable semantic and governance conditions independently.

⸻

34. Confidence and Risk

A useful conceptual relationship is:

Required Evidence
       ↑
       │
       │              Higher-risk Action
       │             /
       │            /
       │           /
       │          /
       │         /
       └────────────────→ Consequence

As the potential consequence of incorrect interpretation increases, Noema should require stronger semantic resolution and evidence.

This does not mean simply increasing a numerical confidence threshold.

It means requiring stronger determinacy around the claims that matter to the Action:

Actor
Action
Target
Scope
Parameters
Authority
Policy
Current State
Constraints

⸻

35. Confidence Must Never Override a Hard Constraint

Suppose:

Confidence:
0.99
Constraint:
Production deployment prohibited during freeze window.

Confidence cannot override the deterministic constraint.

Likewise:

Confidence:
0.99
Authority:
Insufficient

must not become:

EXECUTE

Confidence is subordinate to deterministic constraints, authorization conditions, policy, and other applicable Trust requirements.

⸻

36. Confidence Must Never Override Policy

Similarly:

Model confidence:
0.98

does not override:

Policy:
Refunds above $10,000 require approval.

The appropriate result depends on the actual Trust and Action semantics.

For example, the system may require:

Human approval

as a control requirement before the Action can proceed.

Confidence informs interpretation.

Policy governs permissible behavior.

Approval or confirmation requirements are control conditions, not additional Trust outcomes.

⸻

37. Confidence and the Trust Engine

The relationship can be summarized as:

Candidate Interpretation
          │
          ▼
Evidence / Context / State Reconciliation
          │
          ▼
Confidence / Interpretation Metadata
          │
          ▼
Semantic Resolution
          │
          ▼
Deterministic Trust
     ┌────┼────┬─────┐
     ▼    ▼    ▼     ▼
 EXECUTE CLARIFY ESCALATE REJECT

The important boundary is:

Confidence
    ↓
Supports interpretation and resolution
Trust
    ↓
Determines whether the resolved Action may proceed

CLARIFY is a canonical Trust outcome when unresolved material ambiguity prevents a safe Trust decision.

The clarification mechanism itself belongs to Intent resolution.

⸻

38. Canonical Confidence Model

Conceptually, a confidence-bearing semantic claim can be represented as:

Confidence
├── Claim
├── Candidate / Value
├── Score / Level
├── Supporting Evidence
├── Provenance
├── Timestamp
├── Scope
└── Intent Version

For example:

Claim:
Recipient
Value:
John Smith
Level:
High
Evidence:
Explicit user clarification
Provenance:
Source of Intent
Timestamp:
2026-08-24T09:50:00+01:00
Intent Version:
v2

The exact representation is an implementation concern.

The semantic requirements are canonical:

claim-specific
provenance-aware
scope-aware
time-aware
Intent-version-aware
non-authoritative

⸻

39. Confidence Should Be Observable

For debugging, evaluation, and auditability, Noema should make it possible to inspect:

What candidate interpretation was produced?
What confidence or interpretation metadata supported it?
What evidence supported it?
What uncertainty remained?
What Fact Status applied?
What State Reconciliation occurred?
Why did the uncertainty matter or not matter?
What Trust decision followed?

This is particularly important when an Intent is:

clarified
escalated
rejected
executed

Observability should expose semantic provenance and decision inputs without requiring exposure of private Model reasoning.

⸻

40. Confidence Is Ephemeral; Canonical Resolution Is Durable

A Model’s confidence score may change across:

Models
Model versions
Prompts
Retrieval results
Contexts
Evidence
Enterprise state

Canonical semantic resolution should therefore be more stable than any individual Model score.

The conceptual relationship is:

Model Output
      ↓
Confidence / Interpretation Metadata
      ↓
Evidence / Reconciliation
      ↓
Canonical Resolution
      ↓
Trust
      ↓
Execution

Once an Intent has been resolved and admitted into the deterministic pipeline, downstream execution should depend on the canonical representation and applicable versions rather than repeatedly reinterpreting the original language.

⸻

41. What Confidence Protects Against

Confidence provides an epistemic signal that can help Noema identify:

Ambiguous language
Weak entity matches
Competing interpretations
Incomplete context
Conflicting evidence
Uncertain action selection
Uncertain parameter interpretation
Uncertain outcome verification

It is therefore useful within semantic interpretation and resolution.

It is not a substitute for deterministic validation, State Reconciliation, Trust, or verification.

⸻

42. What Confidence Does Not Do

Confidence does not:

authorize an Actor
override Policy
satisfy a Constraint
prove identity
prove ownership
establish enterprise Business State
establish Fact Status by itself
resolve a material ambiguity by itself
guarantee execution
guarantee an Outcome
replace authoritative evidence
create a Capability
create an Action Contract
bypass Trust

These remain separate semantic, enterprise, Trust, and execution concerns.

⸻

43. Canonical Principles

Noema should follow these principles:

1. Confidence is an epistemic signal, not authority.
2. Confidence is claim-specific.
3. Model confidence is interpretation metadata, not canonical Fact Status.
4. Confidence must have provenance and applicable scope.
5. High confidence does not automatically mean resolved.
6. Candidate ranking does not equal semantic resolution.
7. Material ambiguity must be resolved explicitly.
8. State Reconciliation and authoritative enterprise observations may resolve uncertainty without user clarification.
9. Confidence must not erase UNKNOWN, CONFLICTED, STALE, or UNVERIFIED Fact Status.
10. Consequence affects the quality and determinacy of evidence required.
11. Deterministically established facts should take precedence over probabilistic inference where applicable.
12. Confidence cannot override Policy, Authority, Constraints, or Trust requirements.
13. Trust outcomes remain exactly EXECUTE, CLARIFY, ESCALATE, and REJECT.
14. Confidence does not guarantee execution or Outcome.
15. Material Intent changes create new Intent versions rather than mutating admitted Intent.
16. Downstream execution should depend on canonical semantic resolution, not repeated probabilistic reinterpretation.

⸻

44. Final Definition

Confidence is the epistemic signal representing the strength of support for a semantic interpretation, candidate resolution, or inference within an Intent.

It helps Noema determine which interpretations require further evidence or resolution and may inform clarification and Trust evaluation.

It does not establish authority, Fact Status, enterprise truth, permission, or execution eligibility.

The canonical relationship is:

Source of Intent
       ↓
Candidate Interpretation
       ↓
Hard Schema Validation
       ↓
Evidence / Context / State Reconciliation
       ↓
Confidence / Interpretation Metadata
       ↓
Semantic Resolution
       ↓
Deterministic Trust
       ↓
Bounded Action
       ↓
Execution
       ↓
Verification
       ↓
Outcome

Or, in its shortest form:

Confidence tells Noema how strongly a claim is supported.
Resolution establishes what the Intent means.
Trust determines whether Noema may act.