> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Ambiguity

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/ambiguity.md

⸻

1. Definition

Ambiguity is the condition in which an Intent admits two or more materially different interpretations that cannot be deterministically distinguished using the evidence currently available to Noema.

Ambiguity is therefore not merely uncertainty.

It is a semantic multiplicity that matters to what Noema would do.

The critical question is:

Would choosing between the remaining interpretations materially change the Intent, its execution, its risk, or its Outcome?

If yes, the Intent contains material ambiguity.

Ambiguity is evaluated at the boundary between interpretation and deterministic execution.

The canonical relationship is:

Model Interpretation
        ↓
Candidate Intent
        ↓
Ambiguity Evaluation
        ↓
Material Ambiguity?
     ┌──┴──┐
    Yes    No
     │      │
     ▼      ▼
 Clarify  Continue

⸻

2. Architectural Position

Ambiguity is a semantic condition that becomes a Trust concern when unresolved ambiguity could cause Noema to commit to the wrong execution path.

The Model may produce a probable interpretation.

Noema must determine whether the available evidence establishes a sufficiently determinate Intent for the Action under consideration.

Therefore:

Natural Language
       ↓
Model Interpretation
       ↓
Candidate Intent
       ↓
Intent Resolution
       ↓
Ambiguity Evaluation
       ↓
Trust
       ↓
Action

Ambiguity does not itself authorize or reject an Action.

It determines whether the Intent is sufficiently resolved for the applicable Trust evaluation to continue.

⸻

3. Ambiguity Is Not Model Uncertainty

These concepts must remain separate.

Model uncertainty

The Model is not highly confident about its interpretation.

Ambiguity

More than one materially different interpretation remains viable given the available evidence.

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

High model confidence does not eliminate competing interpretations.

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

unless authoritative or otherwise sufficient deterministic evidence establishes that B is not actually viable.

The governing principle is:

Probability may assist interpretation. It does not by itself establish semantic resolution.

⸻

5. Material Ambiguity

Not every ambiguity matters.

Consider:

"Send me the report."

Suppose the system can produce the report in:

PDF
HTML
Markdown

If the delivery mechanism, semantic content, Action, and expected Outcome are otherwise identical, the implementation-level format difference may be immaterial.

Now consider:

"Send the payment."

where there are:

Payment#123
Payment#456

Choosing the wrong payment materially changes the Action and Outcome.

Therefore:

Implementation ambiguity
    → potentially immaterial
Semantic or resource ambiguity
    → potentially material

Materiality must be evaluated in the context of the Intent, Action, Policy, and potential Outcome.

⸻

6. Materiality Test

Noema should treat ambiguity as material when selecting between candidate interpretations could change one or more of:

* Actor objective
* Resource
* Entity
* Principal
* Recipient
* Amount
* Scope
* Authorization target
* Constraint
* Policy applicability
* Action
* Execution target
* Side effects
* Risk
* Expected Outcome

A useful test is:

If Noema chooses the wrong candidate, could a reasonable Actor say, “That is not what I asked you to do”?

If yes, the ambiguity should be treated as material unless sufficient evidence resolves it.

⸻

7. Sources of Ambiguity

Ambiguity may arise from:

* language
* references
* entities
* Resources
* scope
* quantifiers
* temporal expressions
* spatial expressions
* constraints
* preferences
* Principal identity
* Context
* enterprise state
* multiple Capabilities
* multiple Actions
* conflicting interpretations
* composite Intents

Ambiguity may occur in any Intent component whose alternative interpretations could materially affect execution.

⸻

8. Linguistic Ambiguity

Natural language itself can support multiple meanings.

Example:

"Book the cheapest flight."

“Cheapest” could mean:

* lowest ticket price
* lowest total trip cost
* lowest price among otherwise acceptable flights

If canonical domain semantics, Context, or Policy do not establish which meaning applies, the Intent remains unresolved.

Noema must not silently invent a semantic definition merely to make the Intent executable.

⸻

9. Referential Ambiguity

A reference may correspond to multiple Entities or Resources.

Example:

"Cancel that subscription."

Possible Resources:

Subscription#123
Subscription#456

If Context and available evidence do not establish which Resource is intended:

AMBIGUOUS_RESOURCE

and the applicable Trust state should prevent consequential execution until the ambiguity is resolved.

⸻

10. Entity Ambiguity

Example:

"Send it to John."

Possible recipients:

John#123
John#456
John#789

If multiple candidates remain materially plausible:

AMBIGUOUS_ENTITY

Noema should preserve the candidate set rather than selecting one through probability alone.

⸻

11. Resource Ambiguity

Example:

"Delete the project."

Possible Resources:

Project#A
Project#B
Project#C

If no deterministic grounding rule identifies one Resource:

AMBIGUOUS_RESOURCE

The existence of a Capability to delete projects does not resolve which project the Actor intended.

⸻

12. Scope Ambiguity

Example:

"Delete the inactive projects."

Possible interpretations:

* delete one inactive project
* delete all inactive projects
* delete inactive projects in the current workspace
* delete inactive projects across all workspaces

If scope materially changes the Outcome, clarification is required.

Scope is therefore part of semantic resolution, not merely an execution detail.

⸻

13. Quantifier Ambiguity

Terms such as:

* a
* one
* any
* all
* each
* every
* some
* none

can materially affect execution.

Example:

"Close an account."

This could mean:

* close any eligible account
* close one particular account

The distinction must be resolved before consequential execution.

⸻

14. Temporal Ambiguity

Example:

"Schedule it for Friday."

Possible meanings may differ because of:

* timezone
* current date
* business calendar
* regional calendar
* “this Friday” versus “next Friday”

If the temporal difference affects execution, Noema must resolve the temporal interpretation through deterministic evidence or clarification.

⸻

15. Spatial Ambiguity

Example:

"Send it to the Lagos office."

If the organization has multiple Lagos locations:

Lagos HQ
Lagos Island
Ikeja

the destination is ambiguous if selecting between them materially affects the Outcome.

⸻

16. Constraint Ambiguity

Example:

"Find me a cheap hotel."

“Cheap” is not necessarily a deterministic constraint.

Potential interpretations include:

* below a defined price
* lowest available price
* below the Actor’s normal spending level
* lowest price within an acceptable quality range

If no canonical definition exists, Noema should not silently invent one.

⸻

17. Preference Ambiguity

Example:

"I'd prefer an earlier flight."

Earlier than:

what?

If Context establishes:

earlier than 18:00

the preference may resolve.

If the reference point remains materially undefined, clarification may be required depending on the Action and its consequences.

⸻

18. Contextual Ambiguity

Context can reduce or resolve ambiguity.

Example:

User:
"Create a project called Noema."
User:
"Add Sarah to it."

“It” may resolve to:

Project#Noema

because the preceding Context establishes the referent.

Context is therefore evidence for semantic resolution.

However, Context must satisfy the applicable evidence requirements before it is treated as determinative.

⸻

19. Context Must Not Manufacture Certainty

The existence of Context does not automatically make an interpretation correct.

Example:

Previous conversation:
User discussed Project A.
Current request:
"Delete the project."

If Project A and Project B are both materially plausible, Noema should not automatically select Project A merely because it was mentioned previously.

Context is evidence.

It is not permission to guess.

The relevant question remains:

Does the available Context deterministically distinguish the candidate interpretations?

⸻

20. Ambiguity Across Intent Components

An Intent may be partially resolved.

Example:

Objective:
RenewCard                    ✓
Principal:
User#123                     ✓
Resource:
Card#123 | Card#456          ✗
Outcome:
Card becomes active          ✓

The Intent remains materially ambiguous because the unresolved Resource affects execution.

The presence of resolved components does not eliminate an unresolved material component.

⸻

21. Partial Resolution

Noema should preserve resolved information even when another component remains ambiguous.

Example:

Intent:
RenewCard
Principal:
User#123
Resource:
AMBIGUOUS
├── Card#123
└── Card#456
Outcome:
Card becomes active

Noema should not discard the resolved Objective, Principal, or Outcome merely because the Resource requires clarification.

Partial resolution is a legitimate intermediate semantic state.

⸻

22. Ambiguity vs Missing Information

These are different conditions.

Missing information

"Transfer money."
Amount:
UNKNOWN
Destination:
UNKNOWN

No competing interpretation necessarily exists.

Required information is simply absent.

Ambiguity

"Transfer $500 to my account."
Destination:
Savings#1
Checking#2

The required semantic dimension exists conceptually but has multiple plausible values.

Therefore:

Missing
    → acquire required information
Ambiguous
    → distinguish competing interpretations

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

Conflict occurs when supplied facts, instructions, or constraints cannot simultaneously hold.

Example:

"Book it for Monday."
"Do not book anything before Tuesday."

This is not simply ambiguity.

It is a contradiction requiring conflict resolution or clarification under the applicable semantics and Policy.

⸻

25. Ambiguity vs Unsupported Intent

Example:

"Teleport me to London."

The meaning may be completely clear.

Therefore:

Ambiguity:
No
Capability:
Unavailable

A resolved Intent is not necessarily executable.

Therefore:

Resolved ≠ Executable

⸻

26. Ambiguity vs Authorization

Example:

"Delete the production database."

The target may be perfectly clear.

Intent:
Resolved

But:

Policy:
Not authorized

This is a Trust and authorization condition, not ambiguity.

Noema must not manufacture ambiguity to explain an authorization failure.

Likewise, authorization must not be used to resolve a genuine semantic ambiguity.

⸻

27. Candidate Set

When material ambiguity exists, Noema should represent the candidate interpretations explicitly where practical.

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

The candidate set should remain traceable to the evidence that produced it.

⸻

28. Ambiguity Must Be Typed

Noema should identify what semantic dimension is ambiguous.

Examples:

AMBIGUOUS_RESOURCE
AMBIGUOUS_ENTITY
AMBIGUOUS_SCOPE
AMBIGUOUS_TIME
AMBIGUOUS_DESTINATION
AMBIGUOUS_CONSTRAINT
AMBIGUOUS_OBJECTIVE
AMBIGUOUS_PRINCIPAL
AMBIGUOUS_ACTION

Typed ambiguity allows clarification and Trust evaluation to target the actual semantic problem.

⸻

29. Ambiguity Severity

Not all material ambiguity has the same consequence.

A useful conceptual classification is:

LOW
MEDIUM
HIGH
CRITICAL

based on potential consequence.

For example:

Output format
    → potentially Low
Meeting time
    → potentially Medium
Bank account
    → potentially High
Production database
    → potentially Critical

Severity is contextual.

It should influence the evidence and confirmation requirements applicable to the Action, but severity must not replace the underlying semantic materiality determination.

⸻

30. Risk-Weighted Ambiguity

Materiality and risk are related but distinct.

An ambiguity may affect the same semantic field while carrying different consequences.

Example:

"Send this document to John."

Sending the wrong document to the wrong John may be relatively low consequence for a public document.

The same ambiguity may be substantially higher consequence for:

ConfidentialAcquisitionAgreement

Trust should therefore evaluate:

Ambiguity
+
Potential Consequence
+
Applicable Policy

rather than ambiguity in isolation.

⸻

31. Ambiguity Thresholds

Noema should not use a universal probability threshold such as:

confidence > 0.8 → execute

because ambiguity is not reducible to a single probability.

Progression should instead depend on:

* semantic completeness
* candidate multiplicity
* materiality
* evidence quality
* evidence authority
* risk
* Policy
* required certainty
* Action requirements

The deterministic Trust boundary must evaluate the relevant conditions rather than map model probability directly to authorization.

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

"Renew my active card."

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

The Model’s distribution does not itself establish:

Card#456 = impossible

Unless sufficient evidence eliminates Card#456, material ambiguity remains.

Model confidence may be retained as interpretive metadata, but it cannot independently convert competing candidates into a single authorized Intent.

⸻

34. Explicit Clarification

Direct Actor clarification is often the strongest mechanism for resolving material ambiguity.

Example:

Noema:
"Which card do you want to renew?"
Actor:
"The Visa ending in 1234."

Candidate set:

Card#123

Resolution:

RESOLVED

The clarification and Actor response become part of the provenance of the resulting Intent resolution.

⸻

35. Clarification Should Be Minimal

Noema should ask only about the ambiguous semantic dimension.

Bad:

"Could you provide more information about what you want to do?"

Good:

"Which card do you want to renew:
Visa ending in 1234 or Mastercard ending in 5678?"

The second form minimizes Actor effort while resolving the specific semantic ambiguity.

This follows the principle of minimum necessary interaction.

⸻

36. Ambiguity and Conversational State

A clarification creates an intermediate Intent state.

Example:

Intent#123
    ↓
AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED
    ↓
Actor response
    ↓
RESOLUTION

The original Intent identity should remain stable.

The clarification should be associated with the unresolved semantic dimension rather than creating an unrelated new Intent.

⸻

37. Ambiguity Must Be Auditable

Noema should be able to explain:

* Why was this Intent considered ambiguous?
* Which candidates existed?
* What evidence supported each candidate?
* Why was the ambiguity material?
* Why was clarification required?
* What evidence resolved it?
* When was the resolution established?

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
    resolved_at
}

The exact implementation may differ.

The semantic requirements remain:

* identify the ambiguous dimension
* preserve relevant candidates
* preserve supporting evidence
* preserve materiality
* preserve resolution history

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

This is a hard architectural invariant.

Ambiguity resolution precedes authorization of an Action whose execution depends on that unresolved semantic dimension.

⸻

40. Ambiguity and Executability

A materially ambiguous Intent is not executable for an Action that depends on the ambiguous dimension.

Ambiguous
    ≠
Executable

Example:

Intent:
DeleteProject
Capability:
DeleteProject ✓
Target:
Project A | Project B ✗

Capability availability does not resolve target ambiguity.

The Action cannot proceed until the target is deterministically established.

⸻

41. Ambiguity and Policy

Policy may constrain the candidate set.

Example:

Intent:
Delete a project
Candidates:
Project A
Project B
Policy:
Actor may only delete Project A

If that Policy is authoritative and semantically applicable to the Intent, it may eliminate Project B.

The resulting candidate set can become:

Project A

However, Policy must not be used merely as a mechanism to select an interpretation that is convenient or executable.

Policy constrains what is permitted.

It does not redefine what the Actor meant.

⸻

42. Ambiguity and Authorization

Authorization should be evaluated against the resolved Intent.

If the Intent is:

DeleteProject(ProjectA)

Trust can evaluate:

May Actor delete ProjectA?

Noema should not first choose whichever Project the Actor is authorized to delete simply because that makes execution possible.

That would constitute Intent substitution.

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

The correct semantic state remains:

AMBIGUOUS_RESOURCE

followed by clarification or another authoritative resolution mechanism.

Authorization cannot be used as a semantic guessing mechanism.

⸻

44. Ambiguity and Safety

Ambiguity becomes particularly important when Actions have irreversible or high-impact side effects.

Examples:

* delete
* transfer
* publish
* send
* cancel
* terminate
* deploy
* revoke

For these operations, Noema should apply the applicable stronger semantic and Trust requirements.

The more consequential the Action, the less tolerance there should be for unresolved material ambiguity.

⸻

45. Irreversibility

A useful architectural principle is:

The more irreversible the potential Action, the less tolerance Noema should have for unresolved material ambiguity.

Example:

"Delete the account."

should require stronger semantic resolution than:

"Show me the account."

The difference is not that the latter can ignore ambiguity.

Rather, the consequence of an incorrect interpretation determines the required Trust boundary.

⸻

46. Ambiguity and Side Effects

Noema should evaluate material ambiguity before consequential side effects begin.

Preferred:

Interpret
   ↓
Resolve
   ↓
Evaluate Ambiguity
   ↓
Trust
   ↓
Action
   ↓
Execution

Not:

Interpret
   ↓
Start Execution
   ↓
Discover Ambiguity

Material semantic uncertainty must be resolved before the Action crosses its execution boundary.

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

Conceptually:

Composite:
PARTIALLY_RESOLVED

Clarification should target the ambiguous child component.

Whether other resolved children may execute independently depends on the Composite Intent’s execution semantics, Action dependencies, Policy, and Trust requirements.

Ambiguity in one child must not automatically authorize or invalidate unrelated children.

⸻

48. Ambiguity Propagation

Ambiguity in one component may propagate to dependent components.

Example:

Source Account:
Checking | Savings

Then:

"Transfer the balance from it to my other account."

The destination interpretation may depend on which source account is selected.

Therefore ambiguity propagation must be dependency-aware.

Noema should preserve dependency relationships rather than resolving downstream references independently from an unresolved upstream component.

⸻

49. Ambiguity and Intent Composition

For a Composite Intent:

Parent
├── Child A
├── Child B
└── Child C

Noema should determine whether ambiguity in one child affects:

only Child B

or:

the entire Composite Intent

This depends on the relationships, dependencies, atomicity requirements, and execution semantics of the Composite Intent.

The semantic state should therefore distinguish:

Child-level ambiguity

from:

Composite-level ambiguity

⸻

50. Ambiguity Resolution Should Preserve History

When ambiguity is resolved:

Card#123 | Card#456
        ↓
     Card#123

Noema should preserve the fact that Card#456 was previously a candidate.

This matters for:

* audit
* debugging
* Trust analysis
* Model evaluation
* system improvement
* Actor disputes
* reconstruction of execution decisions

Resolution should add evidence, not erase the history of the ambiguity.

⸻

51. Ambiguity Is Not Failure

Ambiguity is an expected condition in human-computer interaction.

Therefore:

AMBIGUOUS

should not be treated as:

SYSTEM ERROR

It is a legitimate semantic state requiring resolution.

A clarification path is a normal execution path, not an exception path.

⸻

52. Ambiguity Is a First-Class State

Noema should represent ambiguity explicitly rather than encoding it through:

* null
* empty string
* low confidence
* exception
* generic failure
* arbitrary default selection

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
   ┌───┴────────┐
   │            │
Non-material   Material
   │            │
   ▼            ▼
Proceed       Clarify
                │
                ▼
             New Evidence
                │
                ▼
              Resolve
                │
                ▼
          Trust Evaluation

Ambiguity resolution therefore produces stronger semantic grounding for the subsequent Trust decision.

⸻

54. Example: Non-Material Ambiguity

User:

"Create a report."

Suppose the report system internally has two equivalent rendering engines:

Renderer A
Renderer B

The Actor does not care which implementation is used.

This is implementation-level ambiguity, not necessarily Intent ambiguity.

Noema may proceed if the Action, Outcome, Policy, and relevant execution semantics are invariant across the alternatives.

⸻

55. Example: Material Ambiguity

User:

"Transfer ₦100,000 to John."

Recipients:

John#123
John#456

Both are eligible and materially plausible.

The ambiguity changes the destination of money.

Therefore:

MATERIAL
→ CLARIFICATION REQUIRED

⸻

56. Example: Context Resolves Ambiguity

User:

"Send the invoice to Sarah."

Current Context:

Sarah = Sarah#123
Invoice = Invoice#456

No competing candidate remains after applying the available authoritative Context.

Result:

RESOLVED

⸻

57. Example: Context Does Not Resolve Ambiguity

User:

"Send the invoice to Sarah."

Address book:

Sarah#123
Sarah#456

Conversation contains no identifying information.

Result:

AMBIGUOUS_ENTITY

Noema asks:

"Which Sarah do you mean?"

The clarification targets the unresolved semantic dimension.

⸻

58. Example: Model Guessing Is Not Resolution

User:

"Cancel my account."

Model:

Account#123
confidence = 0.94

But the Actor owns:

Account#123
Account#456

Neither Context nor authoritative evidence distinguishes them.

Result:

AMBIGUOUS_RESOURCE

The 94% confidence score does not authorize execution.

⸻

59. Example: Risk Changes the Required Standard

User:

"Send the document to John."

If the document is:

PublicPressRelease

the consequence of recipient ambiguity may be relatively limited.

If the document is:

ConfidentialAcquisitionAgreement

the same unresolved recipient ambiguity carries substantially greater consequence.

Trust should therefore consider:

Ambiguity
+
Potential Consequence
+
Policy
+
Action Requirements

rather than ambiguity in isolation.

⸻

60. Relationship to Trust

Ambiguity is an input to Trust, not the entirety of Trust.

Conceptually:

TrustDecision =
    f(
        IntentResolution,
        Ambiguity,
        Principal,
        Authorization,
        Evidence,
        Policy,
        Risk,
        Action,
        Context
    )

A resolved Intent may still fail Trust because of:

* missing authorization
* insufficient evidence
* Policy prohibition
* stale enterprise state
* failed preconditions
* organizational boundary violations
* unavailable required data

Conversely, the absence of ambiguity does not imply:

EXECUTE

It only means that semantic multiplicity is not blocking the relevant decision.

⸻

61. Ambiguity and Trust Decisions

Material unresolved ambiguity generally prevents an Action from entering:

EXECUTE

The resulting Trust path may be:

AMBIGUOUS
    ↓
CLARIFY

or, depending on the circumstances:

AMBIGUOUS
    ↓
ESCALATE

if automated clarification cannot safely resolve the condition.

If evidence establishes that the Intent is invalid, unauthorized, unsupported, or otherwise prohibited, the corresponding Trust decision should be represented under that actual condition rather than incorrectly labeled as ambiguity.

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
                Resolved Intent
                       │
                       ▼
                  Trust Engine
                       │
                       ▼
                    Action

The Ambiguity component does not replace Trust.

It establishes whether semantic resolution is sufficient for Trust to evaluate the Action.

⸻

63. Canonical Invariants

Invariant 1

Material ambiguity must block execution of an Action that depends on the unresolved semantic dimension.

Invariant 2

Model confidence alone cannot eliminate material ambiguity.

Invariant 3

Ambiguity must identify the semantic dimension that is unresolved.

Invariant 4

Ambiguity should preserve candidate interpretations where practical.

Invariant 5

Context may resolve ambiguity only when it provides sufficient evidence to distinguish the candidates.

Invariant 6

Policy may constrain or eliminate candidates when the Policy is authoritative and semantically applicable, but must not substitute an authorized interpretation for the Actor’s actual Intent.

Invariant 7

Ambiguity must be evaluated before consequential side effects.

Invariant 8

Clarification should target the smallest unresolved material semantic dimension.

Invariant 9

Resolved information must be preserved even when another component remains ambiguous.

Invariant 10

Ambiguity must be distinguishable from uncertainty, incompleteness, invalidity, contradiction, unsupported capability, and authorization failure.

Invariant 11

Authorization must not be used as a mechanism for guessing between materially ambiguous interpretations.

Invariant 12

Noema must not resolve ambiguity toward the interpretation that is merely most convenient, most executable, or most permissive.

Invariant 13

Ambiguity resolution must preserve sufficient provenance to reconstruct the candidate set, evidence, and resolution.

Invariant 14

Ambiguity in one Action or Intent component must not automatically authorize another Action or component.

Invariant 15

Ambiguity propagation must respect semantic dependencies between Intent components.

Invariant 16

The consequence and reversibility of an Action may require stronger evidence and clarification requirements for resolving material ambiguity.

Invariant 17

An Intent may be semantically resolved while remaining non-executable for independent Trust, Policy, authorization, or Capability reasons.

Invariant 18

Ambiguity is a legitimate semantic state and must not be represented as a generic system failure.

⸻

64. Final Definition

Ambiguity is a first-class Trust condition in which Noema cannot deterministically establish a single materially consequential interpretation of an Intent from the evidence currently available.

When material ambiguity remains, Noema must not convert probabilistic preference into executable commitment.

It must either:

* resolve the ambiguity through sufficient authoritative evidence,
* obtain clarification from the Actor,
* or escalate when the ambiguity cannot safely be resolved through the normal automated path.

The fundamental relationship is:

Probabilistic Interpretation
          ↓
Candidate Intent
          ↓
Ambiguity Evaluation
          ↓
Semantic Resolution
          ↓
Trust
          ↓
Action

The shortest canonical formulation is:

If choosing the wrong interpretation could materially change what happens, Noema must not guess.