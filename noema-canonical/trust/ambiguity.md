Ambiguity

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: trust/ambiguity.md

⸻

1. Definition

Ambiguity is the condition in which an Intent admits two or more materially different interpretations that cannot be deterministically distinguished using the evidence currently available to Noema.

Ambiguity is therefore not merely uncertainty.

It is a semantic multiplicity that matters to what Noema would do.

The critical question is:

Would choosing between the remaining interpretations materially change the Intent, its execution, its risk, or its Outcome?

If yes, the Intent is ambiguous.

⸻

2. Why Ambiguity Belongs in Trust

Ambiguity is fundamentally a semantic property, but in Noema it becomes a Trust boundary because unresolved ambiguity must prevent uncontrolled execution.

The Model may produce the most probable interpretation.

Noema must determine whether that probability is sufficient to permit commitment.

Therefore:

Model
  ↓
Candidate Intent
  ↓
Ambiguity Evaluation
  ↓
┌───────────────────────┐
│ Material ambiguity?   │
└───────────┬───────────┘
            │
       ┌────┴────┐
      Yes        No
       │          │
       ▼          ▼
 Clarification  Proceed

⸻

3. Ambiguity Is Not Model Uncertainty

These concepts must remain separate.

Model uncertainty

“The Model is not very confident about its interpretation.”

Ambiguity

“More than one materially different interpretation remains plausible.”

A Model may be uncertain while the Intent is unambiguous.

Example:

User:
"Renew my card."
Only one eligible card exists.
Model confidence:
0.82
Result:
UNAMBIGUOUS

The deterministic domain evidence resolves the reference.

Conversely:

User:
"Renew my card."
Two eligible cards exist.
Model confidence:
0.99

Result:

AMBIGUOUS

High confidence does not eliminate competing interpretations.

⸻

4. Core Principle

Noema must not resolve material ambiguity by probability alone.

If two materially different interpretations remain viable:

Interpretation A = 0.75
Interpretation B = 0.25

Noema must not automatically execute A merely because it has the higher probability.

Instead:

AMBIGUOUS
    ↓
CLARIFICATION

unless deterministic evidence establishes that B is not actually viable.

⸻

5. Material Ambiguity

Not every ambiguity matters.

Consider:

“Send me the report.”

Suppose the system can produce the report in:

PDF
HTML
Markdown

If the delivery mechanism and Outcome are otherwise identical, the format difference may not be material.

Now consider:

“Send the payment.”

where there are:

Payment#123
Payment#456

Choosing the wrong payment materially changes the Action and Outcome.

Therefore:

format ambiguity
    → potentially immaterial
resource ambiguity
    → potentially material

Materiality must be evaluated in context.

⸻

6. Materiality Test

Noema should treat ambiguity as material when selecting between candidate interpretations could change one or more of:

Actor objective
Resource
Entity
recipient
amount
scope
authorization
Constraint
Policy applicability
Action
execution target
side effects
risk
Expected Outcome

A useful test is:

If Noema chooses the wrong candidate, could a reasonable Actor say “that is not what I asked you to do”?

If yes, treat the ambiguity as material unless stronger evidence resolves it.

⸻

7. Sources of Ambiguity

Ambiguity may arise from:

language
references
entities
Resources
scope
quantifiers
temporal expressions
spatial expressions
constraints
preferences
Actor identity
Context
domain state
multiple Capabilities
multiple Actions
conflicting instructions
composite Intents

⸻

8. Linguistic Ambiguity

Natural language itself can support multiple meanings.

Example:

“Book the cheapest flight.”

“Cheapest” could mean:

lowest ticket price
lowest total trip cost
lowest price among acceptable flights

If the canonical domain semantics do not establish which meaning applies, the Intent remains unresolved.

⸻

9. Referential Ambiguity

A reference may correspond to multiple Entities or Resources.

Example:

“Cancel that subscription.”

Possible Resources:

Subscription#123
Subscription#456

If Context does not establish which one:

AMBIGUOUS

⸻

10. Entity Ambiguity

Example:

“Send it to John.”

Possible recipients:

John#123
John#456
John#789

If multiple candidates remain materially plausible:

AMBIGUOUS

⸻

11. Resource Ambiguity

Example:

“Delete the project.”

Possible Resources:

Project#A
Project#B
Project#C

If no deterministic grounding rule identifies one:

AMBIGUOUS

⸻

12. Scope Ambiguity

Example:

“Delete the inactive projects.”

Possible interpretations:

delete one inactive project
delete all inactive projects
delete projects in the current workspace
delete inactive projects across all workspaces

If scope materially changes the Outcome, clarification is required.

⸻

13. Quantifier Ambiguity

Terms such as:

a
one
any
all
each
every
some
none

can materially affect execution.

Example:

“Close an account.”

This could mean:

close any eligible account
close one particular account

The distinction must be resolved before execution.

⸻

14. Temporal Ambiguity

Example:

“Schedule it for Friday.”

Possible meanings may differ because of:

timezone
current date
business calendar
regional calendar
"this Friday" vs "next Friday"

If the temporal difference affects execution, Noema must resolve it deterministically or clarify.

⸻

15. Spatial Ambiguity

Example:

“Send it to the Lagos office.”

If the organization has multiple Lagos locations:

Lagos HQ
Lagos Island
Ikeja

the location is ambiguous if the destination materially affects the Outcome.

⸻

16. Constraint Ambiguity

Example:

“Find me a cheap hotel.”

“Cheap” is not necessarily a deterministic constraint.

Potential interpretations:

< ₦100,000/night
lowest available price
below user's normal spending
lowest price within acceptable quality

If no canonical definition exists, Noema should not invent one silently.

⸻

17. Preference Ambiguity

Example:

“I’d prefer an earlier flight.”

Earlier than:

what?

If Context establishes:

earlier than 18:00

the preference may resolve.

If not, clarification may be necessary depending on the Action.

⸻

18. Contextual Ambiguity

Context can sometimes resolve ambiguity.

Example:

User:
Create a project called Noema.
User:
Add Sarah to it.

“It” refers to:

Project#Noema

because the preceding Context establishes the referent.

Context can therefore reduce ambiguity.

But Context should not be assumed merely because it is available.

⸻

19. Context Must Not Manufacture Certainty

The existence of Context does not make an interpretation correct.

Example:

Previous conversation:
User discussed Project A.
Current request:
"Delete the project."

If Project A and Project B are both active and materially plausible, Noema should not automatically assume Project A merely because it was mentioned previously.

Context is evidence, not permission to guess.

⸻

20. Ambiguity Across Intent Components

An Intent may be partially resolved.

Example:

Objective:
RenewCard          ✓
Actor:
User#123           ✓
Resource:
Card#123 | Card#456   ✗
Outcome:
Card becomes active ✓

The Intent is still materially ambiguous because the unresolved Resource affects execution.

⸻

21. Partial Resolution

Noema should preserve resolved information even when another component remains ambiguous.

Example:

Intent:
RenewCard
Actor:
User#123
Resource:
AMBIGUOUS
├── Card#123
└── Card#456
Outcome:
Card becomes active

Noema should not discard the resolved Objective or Outcome merely because the Resource requires clarification.

⸻

22. Ambiguity vs Missing Information

These are different.

Missing

“Transfer money.”

Amount:
UNKNOWN
Destination:
UNKNOWN

No competing interpretation necessarily exists.

Ambiguous

“Transfer $500 to my account.”

Destination:
Savings#1
Checking#2

The required information exists conceptually but has multiple plausible values.

⸻

23. Ambiguity vs Invalidity

Invalidity means the Intent cannot be valid as expressed.

Example:

Transfer:
Amount = "banana"

Ambiguity means multiple valid interpretations exist.

Example:

Destination:
Savings
or
Checking

The remediation differs:

Invalid
    → reject / correct
Ambiguous
    → resolve / clarify

⸻

24. Ambiguity vs Conflict

Conflict occurs when supplied facts or constraints cannot simultaneously hold.

Example:

"Book it for Monday."
"Do not book anything before Tuesday."

This is not simply ambiguity.

It is a contradiction requiring conflict resolution or clarification.

⸻

25. Ambiguity vs Unsupported Intent

Example:

“Teleport me to London.”

The meaning may be completely clear.

Ambiguity:
No
Capability:
Unavailable

Therefore:

Resolved ≠ Executable

⸻

26. Ambiguity vs Authorization

Example:

“Delete the production database.”

The target may be perfectly clear.

Intent:
Resolved

But:

Policy:
Not authorized

This is a Trust decision, not ambiguity.

⸻

27. Candidate Set

When ambiguity exists, Noema should represent the candidate interpretations explicitly.

Conceptually:

AmbiguousValue<T> {
    candidates: [
        T1,
        T2,
        ...
    ]
    evidence: [...]
}

Example:

Resource:
Candidates:
├── Card#123
└── Card#456

This is preferable to collapsing the value into an arbitrary selection.

⸻

28. Ambiguity Must Be Typed

Noema should know what is ambiguous.

For example:

AMBIGUOUS_RESOURCE
AMBIGUOUS_ENTITY
AMBIGUOUS_SCOPE
AMBIGUOUS_TIME
AMBIGUOUS_DESTINATION
AMBIGUOUS_CONSTRAINT
AMBIGUOUS_OBJECTIVE

This allows clarification to target the actual semantic problem.

⸻

29. Ambiguity Severity

Not all ambiguity has equal consequence.

A useful conceptual classification is:

Low
Medium
High
Critical

based on potential consequences.

For example:

Output format
    → Low
Meeting time
    → Medium
Bank account
    → High
Production database
    → Critical

Severity should influence whether Noema requires explicit clarification and how much evidence is necessary.

⸻

30. Risk-Weighted Ambiguity

Materiality and risk are related but distinct.

An ambiguity may affect the same semantic field while carrying different consequences.

Example:

"Send this document to John."

Sending to the wrong John may be:

low risk

for a public document but:

critical risk

for confidential financial information.

Trust therefore needs to evaluate ambiguity in conjunction with consequence.

⸻

31. Ambiguity Thresholds

Noema should not use a universal probability threshold such as:

confidence > 0.8 → execute

because ambiguity is not reducible to a single probability.

Instead, progression should depend on:

semantic completeness
candidate multiplicity
materiality
evidence quality
risk
Policy
required certainty

⸻

32. Deterministic Elimination

Ambiguity can disappear when authoritative evidence eliminates candidates.

Example:

Candidates:
Card#123
Card#456

Evidence:

Card#456 is cancelled.

Intent:

“Renew my active card.”

Candidate set becomes:

Card#123

Result:

RESOLVED

This is deterministic resolution, not probabilistic guessing.

⸻

33. Model Confidence Cannot Eliminate Candidates

Suppose:

Card#123 → 98%
Card#456 → 2%

The Model’s distribution does not itself prove:

Card#456 = impossible

Unless Noema has deterministic evidence that removes Card#456, material ambiguity remains.

⸻

34. Explicit Clarification

The strongest mechanism for resolving ambiguity is often direct Actor clarification.

Example:

Noema:
Which card do you want to renew?
Actor:
The Visa ending in 1234.

Candidate set:

Card#123

Resolution:

RESOLVED

The clarification itself becomes provenance.

⸻

35. Clarification Should Be Minimal

Noema should ask only about the ambiguous semantic dimension.

Bad:

“Could you provide more information about what you want to do?”

Good:

“Which card do you want to renew: Visa ending in 1234 or Mastercard ending in 5678?”

The latter minimizes Actor effort while preserving deterministic resolution.

⸻

36. Ambiguity and Conversational State

A clarification creates an intermediate Intent state.

Example:

Intent#123
    ↓
AMBIGUOUS
    ↓
CLARIFICATION_REQUESTED
    ↓
Actor response
    ↓
RESOLUTION

The original Intent identity should remain stable.

⸻

37. Ambiguity Must Be Auditable

Noema should be able to explain:

Why was this Intent considered ambiguous?
Which candidates existed?
What evidence supported each?
Why was clarification required?
What resolved it?

Example:

Ambiguity:
Resource
Candidates:
Card#123
Card#456
Reason:
Both cards were active and matched "my card."
Resolution:
Actor selected Card#123.

⸻

38. Ambiguity and Provenance

Every material ambiguity should have provenance where practical.

Conceptually:

Ambiguity {
    type
    candidates
    evidence
    materiality
    severity
    detected_at
    resolution
}

The exact implementation may differ.

The semantic requirements should remain.

⸻

39. Ambiguity and Trust State

An Intent with unresolved material ambiguity must not enter an execution-authorized state.

Conceptually:

AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED

and not:

AMBIGUOUS
    ↓
AUTHORIZED

This should be a hard invariant.

⸻

40. Ambiguity and Executability

A materially ambiguous Intent is not executable.

Ambiguous
    ≠
Executable

Even if a Capability exists.

Example:

Intent:
DeleteProject
Capability:
DeleteProject ✓
Target:
Project A | Project B ✗

Capability availability does not resolve target ambiguity.

⸻

41. Ambiguity and Policy

Policy may sometimes constrain the candidate set.

Example:

Intent:
Delete a project
Candidates:
Project A
Project B
Policy:
Actor may only delete Project A

If that Policy is authoritative and semantically applicable, it may eliminate Project B.

The result can become:

Project A

However, Policy should not be used as an excuse to rewrite an otherwise clear Actor Intent.

⸻

42. Ambiguity and Authorization

Authorization should be evaluated against the resolved Intent.

If the Intent is:

DeleteProject(ProjectA)

then Trust can evaluate:

May Actor delete ProjectA?

It should not first choose whichever project the Actor is authorized to delete simply because that makes execution possible.

That would be intent substitution.

⸻

43. Noema Must Not Resolve Toward Convenience

This is a critical invariant.

Suppose:

Actor:
"Delete the project."
Projects:
A, B
Actor can delete:
A
Actor cannot delete:
B

Noema must not conclude:

Project A

simply because A is executable.

The correct result remains:

AMBIGUOUS

followed by clarification.

⸻

44. Ambiguity and Safety

Ambiguity becomes particularly important when Actions have irreversible or high-impact side effects.

Examples:

delete
transfer
publish
send
cancel
terminate
deploy
revoke

For these operations, Noema should apply stricter ambiguity requirements.

⸻

45. Irreversibility

A useful principle is:

The more irreversible the potential Action, the less tolerance Noema should have for unresolved ambiguity.

Example:

"Delete the account."

should require stronger semantic resolution than:

"Show me the account."

⸻

46. Ambiguity and Side Effects

Noema should evaluate ambiguity before side effects begin.

Preferred:

Interpret
  ↓
Resolve
  ↓
Evaluate ambiguity
  ↓
Trust
  ↓
Execute

Not:

Interpret
  ↓
Start execution
  ↓
Discover ambiguity

⸻

47. Ambiguity in Composite Intents

A Composite Intent may contain both resolved and ambiguous children.

Example:

Intent:
"Refund the payment and notify John."
RefundPayment:
Resolved
Notify:
Recipient = John#123 | John#456

The parent should not be treated as fully resolved.

Composite:
PARTIALLY_RESOLVED

and clarification should target the recipient.

⸻

48. Ambiguity Propagation

Ambiguity in one component may propagate to dependent components.

Example:

Source Account:
Checking | Savings

then:

"Transfer the balance from it to my other account."

The destination interpretation may depend on which source is selected.

Therefore ambiguity propagation must be dependency-aware.

⸻

49. Ambiguity and Intent Composition

For a Composite Intent:

Parent
├── Child A
├── Child B
└── Child C

Noema should know whether ambiguity in one child affects:

only Child B

or:

the entire Composite Intent

This depends on the relationships and execution semantics.

⸻

50. Ambiguity Resolution Should Preserve History

When ambiguity is resolved:

Card#123 | Card#456
        ↓
     Card#123

Noema should preserve the fact that Card#456 was previously a candidate.

This matters for:

audit
debugging
Trust analysis
Model evaluation
system improvement
Actor disputes

⸻

51. Ambiguity Is Not Failure

Ambiguity is an expected condition in human-computer interaction.

Therefore:

AMBIGUOUS

should not be treated as:

SYSTEM ERROR

It is a legitimate Intent state requiring additional information.

⸻

52. Ambiguity Is a First-Class State

Noema should represent ambiguity explicitly rather than encoding it through:

null
empty string
low confidence
exception
generic failure

Conceptually:

Intent
  └── Resolution
        └── Ambiguity

This is semantically richer and operationally safer.

⸻

53. Canonical Ambiguity Lifecycle

Candidate Intent
       ↓
Candidate Evaluation
       ↓
Ambiguity Detected
       ↓
Materiality Evaluation
       │
   ┌───┴────┐
   │        │
Non-material Material
   │        │
   ▼        ▼
 Proceed   Clarify
            │
            ▼
         New Evidence
            │
            ▼
          Resolve

⸻

54. Example: Non-Material Ambiguity

User:

“Create a report.”

Suppose the report system internally has two equivalent rendering engines:

Renderer A
Renderer B

The Actor does not care which implementation is used.

This is implementation ambiguity, not Intent ambiguity.

Noema may proceed.

⸻

55. Example: Material Ambiguity

User:

“Transfer ₦100,000 to John.”

Recipients:

John#123
John#456

Both are eligible.

The ambiguity changes the destination of money.

Therefore:

MATERIAL
→ CLARIFICATION REQUIRED

⸻

56. Example: Context Resolves Ambiguity

User:

“Send the invoice to Sarah.”

Current conversation:

Sarah = Sarah#123
Invoice = Invoice#456

No competing candidates remain.

Result:

RESOLVED

⸻

57. Example: Context Does Not Resolve Ambiguity

User:

“Send the invoice to Sarah.”

Address book:

Sarah#123
Sarah#456

Conversation contains no identifying information.

Result:

AMBIGUOUS_ENTITY

Noema asks:

“Which Sarah do you mean?”

⸻

58. Example: Model Guessing Is Not Resolution

User:

“Cancel my account.”

Model:

Account#123
confidence = 0.94

But the Actor owns:

Account#123
Account#456

Neither Context nor authoritative evidence distinguishes them.

Result:

AMBIGUOUS

The 94% confidence score does not authorize execution.

⸻

59. Example: Risk Changes the Required Standard

User:

“Send the document to John.”

If the document is:

PublicPressRelease

minor recipient ambiguity may have lower consequence.

If the document is:

ConfidentialAcquisitionAgreement

the same ambiguity becomes substantially higher risk.

Trust should therefore consider:

Ambiguity
+
Potential Consequence

rather than ambiguity in isolation.

⸻

60. Trust Decision

A useful conceptual model is:

TrustDecision =
    f(
        IntentResolution,
        Ambiguity,
        ActorAuthority,
        Policy,
        Risk,
        Capability,
        Context
    )

Ambiguity is therefore one input into the Trust decision, not the entirety of Trust.

⸻

61. Canonical Invariants

Invariant 1

Material ambiguity must block execution.

Invariant 2

Model confidence alone cannot eliminate material ambiguity.

Invariant 3

Ambiguity must identify the semantic dimension that is unresolved.

Invariant 4

Ambiguity should preserve candidate interpretations where possible.

Invariant 5

Context may resolve ambiguity only when it provides sufficient evidence.

Invariant 6

Policy must not be used to substitute an authorized interpretation for the Actor’s actual Intent.

Invariant 7

Ambiguity must be evaluated before consequential side effects.

Invariant 8

Clarification should target the smallest unresolved material dimension.

Invariant 9

Resolved information must be preserved even when another component remains ambiguous.

Invariant 10

Ambiguity must be distinguishable from uncertainty, incompleteness, invalidity, contradiction, unsupported capability, and authorization failure.

⸻

62. Architectural Position

Ambiguity sits at the boundary between probabilistic interpretation and deterministic commitment:

                 Human Expression
                       │
                       ▼
                Model Interpretation
                       │
                       ▼
                Candidate Intent
                       │
                       ▼
              ┌──────────────────┐
              │ Ambiguity Engine  │
              └────────┬─────────┘
                       │
             ┌─────────┴─────────┐
             │                   │
        Material?            Not Material
             │                   │
            Yes                  │
             │                   │
             ▼                   ▼
       Clarification          Resolution
             │                   │
             └─────────┬─────────┘
                       ▼
                Canonical Intent
                       │
                       ▼
                  Trust Engine
                       │
                       ▼
                    Action

⸻

63. Final Definition

Ambiguity is a first-class Trust condition in which Noema cannot deterministically establish a single materially consequential interpretation of an Intent from the evidence available. When material ambiguity remains, Noema must not convert probabilistic preference into executable commitment; it must resolve the ambiguity through authoritative evidence or obtain clarification from the Actor.

The shortest canonical formulation is:

If choosing the wrong interpretation could materially change what happens, Noema must not guess.