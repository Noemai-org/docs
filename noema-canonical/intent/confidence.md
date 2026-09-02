Confidence

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/confidence.md

⸻

1. Definition

Confidence is a measure of how strongly an interpretation, resolution, or inference is supported by the available evidence.

Confidence is an epistemic signal, not an authorization decision.

Noema may use confidence to determine whether additional resolution is necessary, but confidence alone must never authorize consequential execution.

The fundamental distinction is:

Confidence
    ↓
How strongly do we believe this interpretation?
Trust
    ↓
Are we justified in executing this Action?

Therefore:

Confidence informs Trust. Confidence does not become Trust.

⸻

2. Why Confidence Exists

Human Intent is expressed through ambiguous, incomplete, and contextual language.

Consider:

“Renew my card.”

A Model may determine with high confidence that the user means:

Intent:
RenewCard

But that does not necessarily establish:

Resource:
Card#123

Nor:

Authority:
Actor is permitted to renew Card#123

Nor:

Policy:
Renewal is currently permitted

Confidence therefore operates at a specific semantic layer.

⸻

3. Confidence Is Not a Property of the Intent Alone

An Intent may contain multiple interpretations or resolutions with different confidence levels.

For example:

"Send the report to John."

could produce:

Intent:
SendReport              confidence: 0.98
Resource:
QuarterlyReport          confidence: 0.94
Recipient:
John Smith               confidence: 0.61
John Doe                 confidence: 0.34

The overall Intent cannot be considered safely resolved merely because the high-level classification is highly confident.

Confidence must be associated with the specific claim or resolution being evaluated.

⸻

4. Confidence Is Claim-Specific

Noema should conceptually distinguish:

Intent confidence
Entity confidence
Resource confidence
Capability confidence
Action confidence
Parameter confidence
Context confidence

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
Capability:
RefundPayment
Confidence: 0.99

The weak Resource resolution may still block execution.

⸻

5. Sources of Confidence

Confidence may be derived from multiple sources.

Possible sources include:

Model interpretation
Structured input
Authoritative system data
Explicit user statements
Context
Historical interaction
Entity matching
Deterministic rules
Domain constraints

These sources do not necessarily have equal epistemic weight.

For example:

Authenticated identity

should generally carry stronger authority for Actor resolution than:

Model inference from conversation

Confidence must therefore be interpreted together with evidence provenance.

⸻

6. Confidence Is Not Model Probability

A Model may output:

0.97

for a candidate interpretation.

Noema should not automatically treat:

0.97

as a canonical probability that the interpretation is correct.

Model scores can be:

uncalibrated
model-specific
task-specific
context-sensitive
incomparable

Therefore, Noema should treat Model confidence as evidence, not as ground truth.

⸻

7. Confidence vs Certainty

Confidence and certainty are different.

Confidence

Represents the strength of available evidence.

Certainty

Represents whether the system has established a fact sufficiently for the relevant decision.

For example:

Model confidence:
99%
Authoritative evidence:
Two matching Resources exist.

The Model may be highly confident.

The Resource may still be unresolved.

Therefore:

High confidence ≠ certainty

⸻

8. Confidence vs Trust

This distinction is foundational.

Confidence asks:

How likely is this interpretation to be correct?

Trust asks:

Is the resulting Action sufficiently justified to execute?

For example:

Model confidence:
0.99
Actor authority:
Invalid

The correct Trust decision is:

DENY

Likewise:

Model confidence:
0.60
All relevant facts:
Deterministically established
Policy:
Satisfied
Authority:
Valid
Constraints:
Satisfied

A system may still be able to execute if the relevant uncertainty has been resolved through stronger evidence.

Thus:

Confidence ≠ Trust

⸻

9. Confidence vs Clarification

Confidence may contribute to the decision to clarify, but clarification should not be based solely on an arbitrary numerical threshold.

Bad model:

confidence < 0.80
    ↓
CLARIFY

This is insufficient because a confidence score has no universal semantic meaning.

Better:

Is the required semantic claim sufficiently established
for this specific Intent and Action?

If not:

CLARIFY

Confidence is one signal in that determination.

⸻

10. Confidence Must Be Contextual

The acceptable level of confidence depends on the consequence of being wrong.

For example:

"Show me my profile."

A low-risk ambiguity may be tolerable if the system can safely resolve it.

But:

"Delete the customer's account."

requires much stronger resolution because an incorrect interpretation has a materially different Outcome.

Therefore:

Required confidence is a function of consequence, not a universal number.

Conceptually:

Required Resolution
        ↑
        │
        │      High consequence
        │       /
        │      /
        │     /
        │    /
        │   /
        └────────────────→ Consequence

⸻

11. Confidence Is Part of Resolution

Noema’s semantic resolution process can be represented as:

Human Expression
       ↓
Candidate Interpretations
       ↓
Evidence Collection
       ↓
Confidence Assessment
       ↓
Resolution
       ↓
Trust Evaluation

Confidence helps Noema determine which interpretations have sufficient support to remain candidates.

⸻

12. Candidate Interpretations

A Model may produce multiple interpretations.

For example:

User:
"Cancel my subscription."

Candidate interpretations:

CancelSubscription(Account#123)
Confidence: 0.91
CancelSubscription(Account#456)
Confidence: 0.08

If authoritative Context establishes that Account#123 is the active subscription, the candidate can be resolved.

If multiple subscriptions remain valid:

CLARIFY

The highest confidence candidate should not automatically win.

⸻

13. Confidence Should Not Hide Ambiguity

Suppose:

Candidate A: 0.51
Candidate B: 0.49

Selecting A merely because it has the highest score would conceal a material ambiguity.

Likewise:

Candidate A: 0.95
Candidate B: 0.05

may still require clarification if the Action is highly consequential and the evidence is weak.

Therefore:

Ranking candidates is not the same as resolving them.

⸻

14. Confidence and Evidence

A confidence value without provenance has limited meaning.

Noema should conceptually be able to answer:

Why is this interpretation confident?

For example:

Recipient:
John Smith
Confidence:
High
Evidence:
1. Actor explicitly named "John Smith"
2. John Smith is in the current Context
3. Only one matching John Smith exists

This is more useful than:

Recipient:
John Smith
Confidence:
0.94

⸻

15. Evidence Hierarchy

Noema should prefer stronger evidence over weaker inference.

A conceptual hierarchy might be:

Explicit structured fact
        ↓
Authoritative system state
        ↓
Explicit human clarification
        ↓
Validated contextual reference
        ↓
Deterministic domain rule
        ↓
Model interpretation
        ↓
Pure probabilistic inference

This is not necessarily a universal ranking for every domain.

The important principle is:

Confidence should reflect the quality and provenance of evidence, not merely the Model’s numerical score.

⸻

16. Confidence Should Be Composable Carefully

An Intent may contain many individually confident claims.

That does not mean the complete Intent is equally confident.

For example:

Actor:       0.99
Action:      0.98
Resource:    0.62
Amount:      0.97
Destination: 0.91

The weak Resource resolution may dominate execution risk.

Noema should therefore avoid simplistic aggregation such as:

Overall confidence = average(all confidence values)

A 95% average does not make a materially ambiguous Resource safe.

⸻

17. Critical Claims

Some claims are critical to an Action.

Examples:

Actor identity
Target Resource
Amount
Destination
Permission scope
Action type
Environment
Recipient

A low-confidence critical claim may block execution even when all other claims are highly confident.

Conceptually:

Critical claim unresolved
        ↓
Intent unresolved
        ↓
No Action

⸻

18. Non-Critical Claims

Other claims may not materially affect execution.

For example:

Preferred wording of notification
Optional display label
Non-essential metadata

Low confidence in these claims should not necessarily block the Action.

Therefore:

Confidence requirements are semantic and action-dependent.

⸻

19. Confidence and Constraints

Constraints can provide deterministic boundaries around uncertain interpretations.

Example:

Intent:
"Book the cheapest flight to London."
Candidates:
Flight A: $700
Flight B: $680
Flight C: $1,200

A Constraint:

Destination = London

eliminates irrelevant candidates.

Additional Constraints may reduce the candidate space further.

Confidence can therefore improve through constraint satisfaction.

⸻

20. Confidence and Context

Context can increase confidence when it provides relevant evidence.

Example:

Conversation:
"We've been discussing the Acme contract."
User:
"Send it to Sarah."

Context may strongly support:

Resource:
Acme Contract

However, Context must be relevant and sufficiently authoritative.

Noema should not treat arbitrary conversational proximity as proof.

⸻

21. Confidence and Entity Resolution

Entity resolution is a major source of uncertainty.

Example:

“Send it to Mike.”

Possible entities:

Mike Johnson
Mike Williams
Mike Brown

Confidence may rank these candidates.

But if multiple candidates remain materially plausible:

CLARIFY

Entity confidence therefore feeds into Intent resolution.

⸻

22. Confidence and Resource Resolution

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

unless the evidence establishes that relationship sufficiently.

⸻

23. Confidence and Action Selection

Sometimes the Intent is clear but multiple Actions can satisfy it.

Example:

“Make sure the customer gets their money back.”

Possible Actions:

RefundPayment
IssueCredit
ReverseCharge
CreateCompensation

Noema should determine whether the domain and Context establish which Action satisfies the Intent.

If multiple Actions remain semantically valid and materially different:

CLARIFY

or select according to an explicit Policy or Capability-selection rule.

The Model’s preference alone is insufficient.

⸻

24. Confidence and Outcome

Confidence can also apply after execution.

For example:

Expected Outcome:
Customer refunded
Observed evidence:
Payment status = refunded
Ledger entry created
Customer balance updated

Confidence in Outcome satisfaction can therefore be based on evidence from the external systems.

However, where Outcome verification can be deterministic, deterministic evidence should take precedence over probabilistic confidence.

⸻

25. Confidence Should Decrease When Evidence Conflicts

Conflicting evidence should affect resolution.

Example:

Model:
Customer = Acme Corp
CRM:
Customer = Acme Holdings
Billing:
Customer = Acme Corp

Noema should not simply select the highest-confidence Model interpretation.

Conflict must become an explicit resolution problem.

Possible result:

RESOLVE
CLARIFY
REQUIRE_EVIDENCE

depending on the domain and consequences.

⸻

26. Confidence Should Be Recomputed When State Changes

An Intent may remain active while external state changes.

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

The original confidence about the required Action is no longer sufficient.

Noema must resolve against current relevant state.

Confidence is therefore not necessarily permanent.

⸻

27. Confidence Has a Lifecycle

Conceptually:

Candidate
   ↓
Evidence
   ↓
Confidence
   ↓
Resolution
   ↓
Trust
   ↓
Action

Confidence should be associated with the version of the Intent and the evidence from which it was derived.

This supports reproducibility and auditability.

⸻

28. Confidence Must Be Explainable

For consequential Actions, Noema should be able to explain why a semantic claim was accepted.

For example:

Resource:
Card#123
Resolution:
Resolved
Evidence:
- Actor owns Card#123
- Card#123 is the only active company card
- User explicitly used singular "my company card"

This is more valuable than exposing only:

Confidence: 0.96

The goal is not to expose Model internals.

The goal is to expose the semantic basis of the decision.

⸻

29. Confidence Is Not a User-Facing Promise

Noema should avoid communicating:

“I’m 99% sure.”

as though that were a guarantee.

A more meaningful interaction is:

“I found one active company card ending in 1234, so I can proceed.”

Or:

“I found two active company cards. Which one do you mean?”

The system should communicate resolved facts and remaining ambiguity rather than Model probabilities.

⸻

30. Confidence and Determinism

The goal of the resolution pipeline is not to maximize confidence.

The goal is to reach a state where the required semantic claims are sufficiently established for deterministic execution.

Therefore:

High Confidence
       ↓
Useful evidence
Deterministic Resolution
       ↓
Executable semantic state

These are related but distinct outcomes.

⸻

31. Confidence Thresholds

Noema may use thresholds internally, but thresholds must be:

contextual
action-specific
calibrated
evidence-aware

A universal rule such as:

confidence >= 0.90 → execute

must not be a canonical Trust rule.

For one operation:

0.90

might be more than sufficient.

For another:

0.99

may still be insufficient if the underlying evidence is ambiguous.

⸻

32. Confidence and Risk

A useful conceptual relationship is:

Required Evidence
       ↑
       │
       │              High-risk Action
       │             /
       │            /
       │           /
       │          /
       │         /
       └────────────────→ Consequence

As the potential consequence of an incorrect Action increases, Noema should require stronger semantic resolution and evidence.

This does not mean simply increasing a numeric confidence threshold.

It means increasing the quality and determinacy of the evidence required for Trust.

⸻

33. Confidence Should Never Override a Hard Constraint

Suppose:

Confidence:
0.99
Constraint:
Production deployment prohibited during freeze window.

The correct result is:

DENY

Confidence cannot override a deterministic Constraint.

Likewise:

Confidence:
0.99
Authority:
Insufficient

must not become:

PERMIT

⸻

34. Confidence Should Never Override Policy

Similarly:

Model confidence:
0.98

does not override:

Policy:
Refunds above $10,000 require approval.

The correct transition is:

Confidence
    ↓
Resolved Intent
    ↓
Policy Evaluation
    ↓
REQUIRE_APPROVAL

Confidence informs interpretation.

Policy governs permissible behavior.

⸻

35. Confidence and the Trust Engine

The relationship can be summarized as:

                 Evidence
                    │
                    ▼
             Confidence
                    │
                    ▼
             Intent Resolution
                    │
                    ▼
             Trust Evaluation
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       PERMIT     CLARIFY    DENY

The important boundary is:

Confidence → Resolution
Trust      → Decision

⸻

36. Canonical Confidence Model

Conceptually, a confidence-bearing semantic claim can be represented as:

Confidence
├── Claim
├── Value
├── Level / Score
├── Evidence
├── Provenance
├── Timestamp
└── Scope

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
User
Timestamp:
2026-08-24T09:50:00+01:00

The exact representation is an implementation concern.

The semantic requirements are canonical.

⸻

37. Confidence Should Be Observable

For debugging and auditing, Noema should make it possible to inspect:

What did the system believe?
Why did it believe it?
What evidence supported it?
What uncertainty remained?
Why did that uncertainty matter or not matter?

This is especially important when an Action is:

denied
clarified
approved
executed

⸻

38. Confidence Is Ephemeral; Canonical Resolution Is Durable

A Model’s confidence score may change across:

Models
versions
prompts
retrieval results
contexts

The resolved semantic state should be more stable.

Therefore:

Model output
   ↓
Confidence / Evidence
   ↓
Canonical Resolution

Once resolved and validated, downstream execution should depend on the canonical representation rather than repeatedly reinterpreting the original language.

⸻

39. What Confidence Protects Against

Confidence helps Noema detect:

Ambiguous language
Weak entity matches
Competing interpretations
Incomplete context
Conflicting evidence
Uncertain action selection
Uncertain outcome verification

It provides an epistemic signal for the semantic layer.

⸻

40. What Confidence Does Not Do

Confidence does not:

authorize an Actor
override Policy
satisfy a Constraint
prove identity
prove ownership
guarantee execution
guarantee an Outcome
replace evidence

These remain separate semantic and Trust concerns.

⸻

41. Canonical Principles

Noema should follow these principles:

1. Confidence is evidence, not authority.

2. Confidence is claim-specific.

3. Confidence must have provenance.

4. High confidence does not automatically mean resolved.

5. Candidate ranking does not equal semantic resolution.

6. Material ambiguity must be resolved explicitly.

7. Consequence affects the required level of evidence.

8. Deterministic facts outrank probabilistic inference where applicable.

9. Confidence cannot override Policy, Authority, or Constraints.

10. Trust, not confidence, determines whether an Action may execute.

⸻

42. Final Definition

Confidence is the epistemic signal representing the strength of evidence supporting a semantic interpretation or resolution within an Intent. It helps Noema determine whether further resolution is necessary, but it is never sufficient by itself to authorize execution.

The canonical relationship is:

Human Expression
       ↓
Model / Evidence
       ↓
Confidence
       ↓
Semantic Resolution
       ↓
Trust
       ↓
Action
       ↓
Outcome

Or, in the shortest form:

Confidence tells Noema how strongly it believes. Trust determines whether Noema may act.