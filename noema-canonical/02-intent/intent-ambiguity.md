Intent Ambiguity

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: 02-intent/intent-ambiguity.md

⸻

1. Definition

Intent Ambiguity is the condition in which an Actor’s expression admits multiple materially different interpretations and the available evidence is insufficient to determine which interpretation represents the Actor’s intended meaning.

Ambiguity is therefore not simply:

The Model is uncertain.

It is:

Multiple plausible semantic states remain
and the distinction matters.

The canonical relationship is:

Expression
    ↓
Candidate Interpretations
    ↓
Evidence
    ↓
Resolution
    │
    ├── One materially valid interpretation
    │        ↓
    │   Resolved Intent
    │
    └── Multiple materially valid interpretations
             ↓
          Ambiguity
             ↓
        Clarification

⸻

2. Why Intent Ambiguity Exists

Human language is inherently underspecified.

An Actor may omit:

Actor
Resource
Recipient
Scope
Time
Amount
Action
Context
Constraints

or refer to them indirectly:

“Send it to John.”

“Delete the old one.”

“Renew my card.”

“Give Sarah the same access.”

The human may consider these expressions perfectly understandable because they possess contextual knowledge that is not explicitly encoded in the utterance.

Noema’s responsibility is to determine whether the available context and evidence are sufficient to recover that meaning without guessing.

⸻

3. Ambiguity Is Not the Same as Uncertainty

These concepts must remain distinct.

Uncertainty

The system has limited confidence in an interpretation.

Ambiguity

Multiple materially distinct interpretations remain possible.

For example:

User:
"Send it to John."

If there is exactly one John but the Model is only 70% confident that “it” refers to the current document, there is uncertainty.

If there are three Johns:

John Smith
John Doe
John Williams

there is ambiguity.

A useful distinction is:

Uncertainty:
How strongly is one interpretation supported?
Ambiguity:
How many materially different interpretations remain?

⸻

4. Ambiguity Is Not Always a Problem

Noema should not attempt to eliminate every ambiguity in natural language.

Some ambiguity is immaterial.

Example:

“Send Sarah the report quickly.”

Whether “quickly” means:

within 2 minutes
within 5 minutes
within 10 minutes

may not matter if the Capability simply sends the report immediately.

If the Action and Outcome are unaffected:

Ambiguity exists
        ↓
No material consequence
        ↓
Proceed

The canonical rule is:

Only ambiguity that can materially affect the resulting Intent, Action, Trust decision, or Outcome requires resolution.

⸻

5. Material Ambiguity

An ambiguity is material when choosing between interpretations could change one or more of:

Actor
Resource
Action
Capability
Scope
Parameter
Constraint
Policy evaluation
Authority
Expected Outcome

Example:

“Delete the old customer account.”

If there are two old customer accounts, selecting the wrong one is materially consequential.

Therefore:

Material ambiguity
        ↓
Cannot become Executable Intent
        ↓
Clarification required

⸻

6. Ambiguity as a Set of Candidate Intents

A useful conceptual model is:

Expression
    ↓
{Intent₁, Intent₂, Intent₃, ...}

For example:

“Close my account.”

could produce:

Intent₁:
CloseBankAccount(Account A)
Intent₂:
CloseBankAccount(Account B)
Intent₃:
CloseInvestmentAccount(Account C)

If evidence cannot distinguish them, the Intent remains ambiguous.

⸻

7. Candidate Interpretations Must Be Semantically Distinct

Noema should not treat superficial linguistic variations as separate Intent candidates.

For example:

"Cancel my subscription."
"Please cancel my subscription."
"I want my subscription cancelled."

These may all map to:

CancelSubscription

There is no meaningful ambiguity.

Ambiguity exists when the candidate interpretations lead to materially different semantic states.

⸻

8. Types of Intent Ambiguity

Intent ambiguity can arise at different semantic layers.

Common categories include:

Actor ambiguity
Entity ambiguity
Resource ambiguity
Action ambiguity
Capability ambiguity
Parameter ambiguity
Scope ambiguity
Context ambiguity
Temporal ambiguity
Spatial ambiguity
Reference ambiguity
Constraint ambiguity
Outcome ambiguity

These categories should remain conceptually distinct because the resolution strategy may differ.

⸻

9. Actor Ambiguity

Actor ambiguity occurs when Noema cannot establish who is responsible for the Intent.

Example:

“Approve the invoice for me.”

Potential Actors:

Current user
Manager
Finance department
Company

If Actor identity affects Authority or Policy, the ambiguity is material.

Noema must resolve the Actor before proceeding.

⸻

10. Entity Ambiguity

Entity ambiguity occurs when an expression refers to multiple possible entities.

Example:

“Send it to Alex.”

Candidates:

Alex Johnson
Alex Smith
Alex Brown

If multiple candidates remain valid:

CLARIFY

⸻

11. Resource Ambiguity

Resource ambiguity occurs when the target Resource cannot be uniquely identified.

Example:

“Delete the project.”

Possible Resources:

Project Alpha
Project Beta
Project Gamma

If Context or other evidence cannot identify the intended project, the Intent is ambiguous.

⸻

12. Action Ambiguity

Action ambiguity occurs when the Actor’s desired operation itself is unclear.

Example:

“Fix the customer account.”

Potential Actions:

UpdateProfile
ResetPassword
UnlockAccount
RestoreSubscription

The Outcome may provide additional evidence.

But if materially different Actions remain plausible, Noema should clarify.

⸻

13. Capability Ambiguity

Capability ambiguity occurs when multiple Capabilities could satisfy the same high-level Intent and the distinction matters to the Actor or Policy.

Example:

“Notify the customer.”

Possible Capabilities:

Email
SMS
PushNotification

If the Actor has specified:

“Send them a message.”

the appropriate Capability may be selected from Context and Policy.

But if the delivery channel materially matters and cannot be inferred:

CLARIFY

⸻

14. Parameter Ambiguity

Parameter ambiguity occurs when a required parameter admits multiple values.

Example:

“Transfer $500.”

Possible destinations:

Savings Account
Checking Account
Brokerage Account

The amount is resolved.

The destination is not.

The Intent remains ambiguous.

⸻

15. Scope Ambiguity

Scope ambiguity concerns the boundaries of the requested Action.

Example:

“Give David access.”

Access to what?

Repository
Workspace
Organization
Project
Environment

If the scope materially affects the Outcome, clarification is required.

⸻

16. Temporal Ambiguity

Temporal ambiguity occurs when a time reference admits multiple materially different interpretations.

Examples:

“Schedule it for Friday.”

Which Friday?

“Send this later.”

When?

“Cancel the meeting tomorrow.”

Which timezone?

Temporal ambiguity may be resolved through Context.

If not, it must be clarified when timing materially affects the Action.

⸻

17. Spatial Ambiguity

Spatial ambiguity occurs when a location reference is not sufficiently resolved.

Example:

“Book the flight from London.”

Possible departure locations:

Heathrow
Gatwick
Stansted

If airport selection materially affects the booking, the ambiguity must be resolved.

⸻

18. Reference Ambiguity

Reference ambiguity occurs when pronouns, aliases, or contextual references can refer to multiple Resources or Entities.

Examples:

“Send it to her.”

“Delete that one.”

“Use the other account.”

Noema should resolve references using available Context and evidence.

If multiple materially valid references remain:

CLARIFY

⸻

19. Constraint Ambiguity

Sometimes the requested Action is clear but the Constraints are not.

Example:

“Book me the cheapest flight.”

Potential interpretation:

Cheapest absolute price

versus:

Cheapest acceptable flight

where “acceptable” includes:

reasonable departure time
checked baggage
preferred airport

If these distinctions materially change the resulting Action, Noema must resolve the relevant Constraints.

⸻

20. Outcome Ambiguity

Outcome ambiguity occurs when multiple materially different Outcomes could satisfy the same expression.

Example:

“Get the customer back online.”

Possible Outcomes:

Unlock account
Reset password
Restore subscription
Restore network access

The expression describes a goal but not necessarily the mechanism.

Noema should use Context and domain knowledge to resolve the intended Outcome.

If multiple Outcomes remain materially plausible:

CLARIFY

⸻

21. Ambiguity and Context

Context is one of the primary mechanisms for resolving ambiguity.

Example:

Current screen:
Invoice #9281
User:
"Refund this."

Context provides:

Resource = Invoice #9281

The Intent may therefore become resolved without asking.

However:

Context may resolve ambiguity only when the context is sufficiently authoritative and relevant.

Proximity alone is not enough.

⸻

22. Ambiguity and Evidence

Noema should attempt to resolve ambiguity through evidence before asking the human.

Conceptually:

Ambiguity
    ↓
Search authoritative Context
    ↓
Search relevant Resources
    ↓
Apply Constraints
    ↓
Evaluate relationships
    ↓
Candidate reduction
    ↓
Resolved?
   / \
 Yes  No
  ↓    ↓
Proceed Clarify

This prevents unnecessary clarification.

⸻

23. Ambiguity and Confidence

Confidence can help rank candidate interpretations.

Example:

John Smith: 0.81
John Doe:   0.19

But ranking is not resolution.

If both remain materially plausible:

Ambiguous

even if one candidate has a higher Model score.

Therefore:

The highest-confidence candidate is not automatically the correct candidate.

⸻

24. Ambiguity and Deterministic Resolution

Where authoritative data can establish a unique answer, ambiguity should be eliminated deterministically.

Example:

User:
"Renew my card."
Available cards:
Card A — expired
Card B — active

If only expired cards are eligible for renewal:

Resource = Card A

The Intent is resolved.

No clarification is necessary.

⸻

25. Ambiguity and Clarification

When material ambiguity remains after available evidence has been exhausted:

Ambiguous Intent
       ↓
Clarification

Clarification should identify the exact unresolved semantic dimension.

Bad:

“Can you clarify?”

Good:

“Which card do you want to renew: the corporate card ending 1234 or the virtual card ending 5678?”

The second makes the ambiguity explicit and bounded.

⸻

26. Ambiguity Must Be Localized

Noema should identify where the ambiguity exists.

For example:

Intent:
RefundPayment
Actor:
Resolved
Action:
Resolved
Customer:
Resolved
Payment:
AMBIGUOUS
Amount:
Resolved

This is superior to:

Intent:
Uncertain

Localization makes clarification precise and makes the resolution state inspectable.

⸻

27. Ambiguity Should Not Propagate Unnecessarily

If one field is ambiguous, Noema should not treat every other field as uncertain.

For example:

Actor: Alice              RESOLVED
Action: Refund            RESOLVED
Customer: John            RESOLVED
Payment: ?                AMBIGUOUS

Only the unresolved claim blocks execution.

This supports targeted clarification.

⸻

28. Ambiguity and Executable Intent

An Intent containing unresolved material ambiguity cannot become an Executable Intent.

Material ambiguity
        ↓
Intent unresolved
        ↓
No Executable Intent

After clarification:

Resolved Intent
        ↓
Executable Intent

This creates a hard semantic boundary.

⸻

29. Ambiguity and Trust

Trust should not attempt to make a decision against a materially ambiguous Intent.

The correct sequence is:

Intent
  ↓
Ambiguity Detection
  ↓
Clarification / Resolution
  ↓
Executable Intent
  ↓
Trust Evaluation

Not:

Ambiguous Intent
  ↓
Trust
  ↓
Best Guess
  ↓
Action

⸻

30. Ambiguity and Policy

Policy may itself eliminate ambiguity.

Example:

User:
"Refund the payment."
Two payments exist.
Policy:
Only payments made within the last 24 hours are refundable.

If only one payment satisfies the Policy:

Payment #8291

the candidate set may become deterministic.

Policy can therefore constrain resolution.

However:

Policy should not be used to invent the Actor’s Intent.

It can eliminate impossible candidates but should not arbitrarily select between materially valid ones.

⸻

31. Ambiguity and Constraints

Constraints can similarly reduce ambiguity.

Example:

“Send the report to the finance team.”

Possible groups:

Finance
Finance Operations
Finance Leadership

Constraint:

Recipient must be a team with external-email capability.

If only one candidate satisfies the constraint, the ambiguity can be resolved.

⸻

32. Ambiguity and Negative Evidence

Noema should consider evidence that eliminates candidates, not only evidence supporting candidates.

Example:

Two cards match "my card."
Card A:
Inactive
Card B:
Active

If the requested Action is:

RenewCard

Card A may be excluded by eligibility constraints.

Negative evidence is therefore useful for candidate elimination.

⸻

33. Ambiguity and Contradiction

Ambiguity and contradiction are distinct.

Ambiguity

Multiple interpretations are possible.

Contradiction

Available evidence directly conflicts.

Example:

User:
"Send it to John."
Context:
John Smith
Directory:
John Smith
John Doe

This is ambiguity.

But:

User explicitly selected:
John Smith
Authorization record:
John Smith is not a valid recipient

may be a contradiction between Intent and system state.

Contradiction may require:

Clarification
Denial
Error

depending on the domain.

⸻

34. Ambiguity and Missing Information

Missing information does not automatically equal ambiguity.

Example:

“Send the report.”

If there is only one obvious recipient defined by the workflow, the recipient may be supplied by Context.

If there are no possible recipients, the issue may be incompleteness rather than ambiguity.

The distinction is:

Ambiguity:
Multiple plausible values.
Missing information:
No sufficient value is currently available.

Both may result in clarification, but their semantic causes differ.

⸻

35. Ambiguity and Underspecification

Underspecification is broader than ambiguity.

Example:

“Send the report.”

The request may omit the recipient entirely.

There may be:

zero candidates

rather than:

multiple candidates

Noema should distinguish:

Ambiguity:
Too many plausible interpretations.
Underspecification:
Insufficient information to establish an interpretation.

⸻

36. Ambiguity Severity

Not every ambiguity has equal risk.

A useful conceptual classification is:

Informational
Low
Material
High-risk
Critical

For example:

"Show me John's profile."

may have relatively low consequence.

Whereas:

"Transfer John's $50,000."

has high consequence.

The severity should influence how aggressively Noema requires resolution.

⸻

37. Ambiguity and Consequence

A useful canonical principle is:

The greater the consequence of choosing incorrectly, the less ambiguity Noema may tolerate.

This does not mean:

High consequence → ask every possible question.

It means:

High consequence
      ↓
Require stronger evidence
      ↓
Require stronger semantic resolution

⸻

38. Ambiguity Should Be Explainable

For every blocking ambiguity, Noema should be able to answer:

What is ambiguous?
What candidates exist?
Why are they materially different?
What evidence was considered?
Why couldn't the system resolve them?
What clarification would resolve them?

Example:

Ambiguous Field:
Resource
Candidates:
Card #1234
Card #5678
Reason:
Both are active cards owned by the Actor.
Resolution:
Actor must select one.

⸻

39. Ambiguity as a First-Class State

Ambiguity should not be represented solely as an error string.

Conceptually:

Intent State:
AMBIGUOUS

with associated information:

Ambiguous Field
Candidates
Evidence
Reason
Required Resolution

This allows Noema to treat ambiguity as part of the Intent lifecycle.

⸻

40. Ambiguity and Auditability

For consequential workflows, Noema should preserve the ambiguity that existed before execution.

Example:

Original Intent:
"Renew my card."
Ambiguity:
Two eligible cards.
Clarification:
Which card?
Human:
Corporate card ending 1234.
Resolution:
Card #1234.
Action:
RenewCard(#1234).

This creates an auditable semantic chain.

⸻

41. Ambiguity Should Not Be Hidden by the Model

A Model may internally choose:

Card #1234

even when:

Card #1234
Card #5678

are equally valid.

Noema must not treat the Model’s selection as resolution merely because the Model produced a single output.

The semantic layer must retain the ability to detect competing candidates.

⸻

42. Ambiguity and Retrieval

Retrieval can reduce ambiguity by introducing evidence.

Example:

User:
"Renew the card I used last month."

Retrieval finds:

Card #1234:
Used on July 18
Card #5678:
Never used

The Resource can be resolved.

Retrieval therefore contributes evidence to Intent resolution.

But retrieved information should still be evaluated for:

Authority
Freshness
Relevance
Consistency

Retrieval does not automatically make a fact authoritative.

⸻

43. Ambiguity and External State

External systems can introduce or remove ambiguity.

Example:

At T1:

One active card

At T2:

Two active cards

An Intent that was previously resolvable may become ambiguous.

Therefore:

Ambiguity is evaluated against relevant state at the time of resolution and, where necessary, execution.

⸻

44. Ambiguity and Race Conditions

Consider:

User:
"Cancel my subscription."

At resolution:

Subscription #123

is uniquely identified.

Before execution, another subscription becomes associated with the Actor.

Noema must ensure that the Action remains bound to the resolved Resource rather than reinterpreting the original language against the new state.

Executable Intent provides this semantic binding.

⸻

45. Canonical Resolution Strategy

Noema should follow this order:

1. Parse the expression.
        ↓
2. Identify candidate semantic interpretations.
        ↓
3. Use authoritative Context.
        ↓
4. Use relevant Resources and relationships.
        ↓
5. Apply Constraints and Policy-derived restrictions.
        ↓
6. Evaluate evidence and confidence.
        ↓
7. Determine whether one materially valid interpretation remains.
        ↓
8. If yes → resolve.
        ↓
9. If no → clarify.

This makes ambiguity handling systematic rather than conversationally improvised.

⸻

46. Canonical Ambiguity Rule

Noema must not collapse multiple materially valid interpretations into one merely because one interpretation is more probable. It must either establish a sufficient evidentiary basis for resolution or explicitly obtain the missing distinction from the Actor.

This is a core Trust invariant.

⸻

47. What Intent Ambiguity Protects Against

Intent ambiguity handling protects against:

Wrong Resource
Wrong Recipient
Wrong Action
Wrong Scope
Wrong Account
Wrong Customer
Wrong Environment
Wrong Policy Evaluation
Wrong Outcome

It is therefore a foundational safety mechanism.

⸻

48. What Intent Ambiguity Does Not Mean

Intent ambiguity does not mean:

The Model failed.
The user communicated badly.
No Action is possible.
Every missing field requires clarification.
Every low confidence score is ambiguity.
The system must always ask the human.

The goal is not maximal questioning.

The goal is correct semantic resolution with minimal friction.

⸻

49. Canonical Principles

1. Ambiguity is a semantic condition, not a Model error.

2. Only material ambiguity blocks execution.

3. Multiple candidates do not automatically constitute material ambiguity.

4. Missing information and ambiguity are distinct conditions.

5. Confidence ranks evidence; it does not resolve ambiguity by itself.

6. Authoritative Context should be used before asking the human.

7. Constraints and valid evidence should reduce candidate space.

8. A Model must not silently collapse material ambiguity.

9. Blocking ambiguity must be localized to the specific unresolved semantic claim.

10. Material ambiguity prevents an Intent from becoming Executable.

11. Clarification should ask only for the distinction required to resolve the ambiguity.

12. Ambiguity resolution must remain auditable.

⸻

50. Final Definition

Intent Ambiguity is the presence of multiple materially distinct interpretations of an Actor’s expression that cannot be deterministically distinguished using available authoritative evidence, Context, Constraints, and semantic relationships.

The canonical flow is:

Actor Expression
       ↓
Candidate Interpretations
       ↓
Evidence + Context
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
  Resolved       Ambiguous
       │           │
       ▼           ▼
Executable     Clarification
  Intent           │
       │            ▼
       │        Resolution
       │            │
       └────────────┘
              ↓
            Trust
              ↓
            Action

The shortest canonical formulation is:

Ambiguity exists when Noema has more than one materially valid answer and insufficient evidence to know which one the Actor intended.