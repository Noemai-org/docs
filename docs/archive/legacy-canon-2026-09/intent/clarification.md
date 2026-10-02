> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Clarification

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/clarification.md

⸻

1. Definition

Clarification is the explicit resolution of an unresolved or ambiguous aspect of an Intent required before Noema can safely determine or continue toward an Action.

Clarification is not an error condition.

It is a first-class Intent lifecycle state and interaction mechanism.

When Noema cannot establish sufficient semantic certainty to proceed deterministically, it must transition into clarification rather than infer beyond its permitted boundary.

Clarification resolves missing semantic information. It does not itself authorize execution or establish enterprise truth.

⸻

2. Why Clarification Exists

Intent is frequently incomplete or ambiguous.

For example:

"Send the report to John."

Noema may know:

Actor: Alice
Intent: SendReport
Resource: Quarterly Report

but discover multiple possible recipients:

John Smith
John Doe
John Williams

The system should not arbitrarily select one.

Instead:

Intent
  ↓
Resolution
  ↓
Ambiguity detected
  ↓
Clarification Required
  ↓
Human response
  ↓
New Intent Version / Resolution
  ↓
Trust evaluation

⸻

3. The Core Rule

When a material ambiguity prevents deterministic resolution of an Intent, Noema must clarify rather than guess.

The unacceptable path is:

Ambiguity
   ↓
Model guess
   ↓
Action

The canonical path is:

Ambiguity
   ↓
Clarification
   ↓
Resolution
   ↓
Hard Validation
   ↓
Context / State Reconciliation
   ↓
Trust evaluation
   ↓
Action

Clarification therefore protects the deterministic boundary between probabilistic interpretation and consequential execution.

⸻

4. Clarification vs Model Confidence

Model confidence does not determine whether clarification is required.

A Model may be highly confident about an interpretation while the available evidence remains insufficient for safe execution.

For example:

Model confidence:
97%
Known:
There are two accounts matching the description.

The correct result may still be:

CLARIFY

Therefore:

Model Confidence ≠ Resolution
Model Confidence ≠ Fact Status
Model Confidence ≠ Authority
Model Confidence ≠ Trust

Clarification is determined by the semantic requirements of the Intent and the evidence available to satisfy them.

Model confidence may be retained as non-authoritative interpretation metadata, but it cannot establish that an ambiguity has been safely resolved.

⸻

5. Material vs Non-Material Ambiguity

Not every ambiguity requires clarification.

Noema should distinguish between:

Non-material ambiguity

An ambiguity that does not affect the resulting Action, authorization, policy evaluation, constraints, or expected Outcome.

Example:

"Send the report to Sarah."

If Sarah has one canonical identity and the exact wording of the report title is irrelevant to the Action, Noema need not ask unnecessary questions.

Material ambiguity

An ambiguity that can change:

* Actor
* Action
* Resource
* Target
* Authority
* Scope
* Policy evaluation
* Constraint satisfaction
* Expected Outcome

Example:

"Transfer $5,000 to my savings account."

If the Actor has three savings accounts, the target Resource is materially ambiguous.

Clarification is required.

⸻

6. Clarification Is About Resolution, Not Conversation

Noema should not ask questions merely because a Model feels uncertain.

A clarification request must correspond to a specific unresolved semantic requirement.

Bad:

"Could you provide more information?"

Good:

"You have two savings accounts. Which one should receive the $5,000 transfer?"

The second question identifies:

Unresolved concept:
Resource
Available candidates:
Savings Account A
Savings Account B

This makes clarification deterministic and auditable.

⸻

7. Clarification Target

Every clarification should identify what part of the Intent remains unresolved.

Possible targets include:

* Actor
* Entity
* Resource
* Target
* Capability
* Action
* Parameter
* Context
* Constraint
* Policy
* Authority
* Scope
* Outcome

For example:

Intent:
TransferMoney
Clarification Target:
Resource
Question:
Which savings account should receive the transfer?

The target should be typed rather than represented only as free-form conversational text.

⸻

8. Clarification State

Clarification is represented as an explicit Intent lifecycle state.

A simplified lifecycle is:

SOURCE
    ↓
INTERPRETING
    ↓
CANDIDATE INTENT
    ↓
HARD SCHEMA VALIDATION
    ↓
ADMITTED
    ↓
RESOLVING
    ↓
┌──────────────────────┐
│ CLARIFICATION        │
│ REQUIRED             │
└──────────┬───────────┘
           ↓
    HUMAN RESPONSE
           ↓
  NEW INTENT VERSION
           ↓
      RESOLVING
           ↓
      RESOLVED
           ↓
       TRUST
           ↓
       ACTION

An Intent may require clarification more than once if multiple independent ambiguities are discovered during resolution.

Clarification is an Intent lifecycle/control state. It is not one of the canonical Trust outcomes.

⸻

9. Clarification Is Not Failure

The following states must remain conceptually distinct:

CLARIFY
REJECT
FAIL

Clarify

The system can potentially fulfill the Intent but lacks required information or has unresolved semantic ambiguity.

Reject

The system has enough information to determine that the requested operation cannot be permitted under applicable Trust conditions.

Fail

The system attempted execution but could not successfully complete it according to execution semantics.

Therefore:

Missing information       → CLARIFY
Prohibited operation      → REJECT
Execution failure         → FAIL

REJECT is the canonical Trust outcome. FAIL is an execution-domain condition.

⸻

10. Clarification Must Preserve Intent Lineage

A clarification response must refine the existing Intent rather than create an unrelated semantic root.

Example:

Initial Intent:

"Send the contract to John."

Noema asks:

"Which John do you mean?"

Human responds:

"John Smith."

The resulting Intent becomes a new version:

Intent v2
Action: SendContract
Actor: existing Actor
Resource: existing Contract
Recipient: John Smith
supersedes: Intent v1

The original admitted Intent remains immutable.

Material clarification produces a new Intent version rather than silently mutating the previous Intent.

⸻

11. Clarification Must Be Minimal

Noema should request the minimum information necessary to remove the blocking ambiguity.

If the system knows:

Actor
Resource
Action
Recipient candidates

it should not ask the human to repeat everything.

Instead:

"Which John do you mean: John Smith or John Doe?"

The goal is:

Minimum Question
        ↓
Maximum Resolution

Minimality must not remove information necessary to establish authority, scope, policy conditions, or safe execution.

⸻

12. Clarification Should Prefer Choices When Possible

When Noema can enumerate valid candidates, clarification should preferably expose those candidates.

Instead of:

"Which account?"

prefer:

"Which account should receive the transfer?"
1. Savings ••••4821
2. Savings ••••9174

Candidate presentation should use only information the Actor is permitted to see.

Candidate enumeration must not itself disclose protected information merely to make clarification easier.

⸻

13. Clarification Must Not Introduce New Ambiguity

A clarification question should itself be sufficiently unambiguous.

Bad:

"Which account do you want?"

if the system has multiple account types.

Better:

"Which savings account should receive the transfer?"

The clarification mechanism must reduce semantic uncertainty rather than move it elsewhere.

⸻

14. Clarification and Context

Context can sometimes resolve ambiguity without asking the human.

For example:

"Send this to John."

If the current Context contains:

Current conversation:
John Smith is the active recipient.

and that context is authoritative and sufficient for the specific claim, Noema may resolve the reference without clarification.

However, contextual inference must remain subject to the same Trust requirements as any other resolution.

Context is available information and may contain Evidence or references to reconciled Facts. It is not automatically authoritative merely because it is present in Context.

Context is evidence.

It is not permission to guess.

⸻

15. Clarification and Evidence

Clarification may be avoided when authoritative evidence can resolve the ambiguity.

For example:

User:
"Renew my card."

If the Actor has exactly one active card eligible for renewal, Noema can resolve:

Resource → Card#123

without asking.

If there are multiple eligible cards:

Card#123
Card#456

and the distinction affects the Action, clarification becomes necessary.

The principle is:

Resolve from authoritative evidence before asking the human,
but never infer beyond what the evidence supports.

Where current enterprise state is required, Noema may use State Reconciliation before deciding that ambiguity remains.

⸻

16. Clarification and Trust

Clarification belongs within the Intent-to-Trust pipeline.

Conceptually:

Intent
  ↓
Resolution
  ↓
Context / State Reconciliation
  ↓
Is required information sufficient?
  │
  ├── Yes ──→ Trust Evaluation
  │
  └── No ───→ Clarification

Clarification is therefore a mechanism for satisfying the semantic and contextual requirements necessary for a Trust decision.

Clarification itself does not produce EXECUTE.

⸻

17. Clarification and Authority

Some ambiguity concerns the Actor rather than the target Resource.

Example:

"Approve the payment."

Noema may know which payment is being discussed but not whether the current Actor is acting:

* personally
* on behalf of a department
* on behalf of an organization

If that distinction affects authority, clarification may be necessary.

However, clarification cannot manufacture authority.

The human answering:

"I'm approving it for the company."

does not automatically establish that they possess that authority.

Authority must still be independently evaluated against authoritative identity, permissions, policy, organizational scope, and applicable enterprise state.

⸻

18. Clarification and Policy

A clarification may resolve information required to evaluate Policy.

For example:

"Create a new production deployment."

Noema may require:

* Environment
* Release
* Change window
* Approval status

If the missing information affects Policy evaluation, clarification may be required before Trust can be determined.

But clarification does not override Policy.

Clarification
    ↓
Information
    ↓
Policy Evaluation

not:

Clarification
    ↓
Policy Bypass

⸻

19. Clarification and Constraints

Constraints may be:

* explicit
* system-defined
* policy-derived
* resource-derived
* contextual
* enterprise-defined

Example:

"Book me the cheapest flight."

Possible unresolved constraints:

* Destination
* Travel date
* Departure airport
* Cabin
* Baggage requirements

Noema should identify which missing constraints materially affect the resulting Action or expected Outcome.

It should not ask for constraints that are irrelevant to the requested Outcome.

⸻

20. Clarification and Capabilities

Sometimes the Intent is understood, but the system cannot determine which Capability should satisfy it.

For example:

"Get this document signed."

Possible Capabilities:

ElectronicSignature
InternalApproval
DocumentWorkflow

If domain semantics or Context cannot establish the intended mechanism, Noema may need clarification.

However, where the Intent specifies the Outcome rather than the implementation, Noema should generally prefer selecting an appropriate Capability itself from the registered Capability and Enterprise Action Graph.

The human should not be forced to understand implementation details unnecessarily.

Capability selection remains bounded by registered capabilities. The Model or clarification mechanism cannot invent a new capability.

⸻

21. Clarification Should Not Leak Implementation Details

Noema should generally ask:

"Which account should receive the transfer?"

rather than:

"Which database record should I pass to the transfer_funds capability?"

The human-facing clarification should be expressed in the language of the Intent and relevant domain concepts.

Implementation details belong below the semantic boundary.

⸻

22. Clarification as a Typed Object

Conceptually, a Clarification may contain:

Clarification
├── Intent Version
├── Target
├── Reason
├── Question
├── Candidates
├── Required Information
├── Evidence References
└── Resolution Criteria

For example:

Clarification
  Intent Version: TransferMoney v1
  Target: Resource
  Reason: Multiple eligible savings accounts
  Question: Which savings account should receive the transfer?
  Candidates:
    - Account#4821
    - Account#9174
  Resolution:
    Exactly one Resource must be selected

The exact implementation is an engineering concern.

The semantic structure is canonical.

⸻

23. Clarification Must Be Auditable

Noema should retain enough information to establish:

* What was ambiguous?
* Which Intent version was affected?
* Why was clarification required?
* What evidence was considered?
* What question was asked?
* Which candidates were presented?
* What information was provided?
* Which Intent version resulted?
* How did the answer resolve the ambiguity?
* What Action resulted?

This is particularly important for consequential enterprise operations.

The causal record should show:

Intent v1
  ↓
Ambiguity
  ↓
Clarification
  ↓
Human Resolution
  ↓
Intent v2 supersedes v1
  ↓
Resolution
  ↓
Trust Decision
  ↓
Action

⸻

24. Clarification and Model Interaction

A Model may generate candidate clarification questions.

But the Model should not independently decide that a clarification is sufficient for execution.

The canonical flow is:

Noema detects unresolved requirement
        ↓
Model may formulate human-readable question
        ↓
Human responds
        ↓
Noema resolves response
        ↓
Hard schema validation
        ↓
Deterministic resolution
        ↓
Context / State Reconciliation
        ↓
Trust evaluation

The Model assists communication.

Noema owns semantic state.

⸻

25. Clarification Must Be Re-Validated

Human clarification responses are themselves inputs.

For example:

"Use the other one."

The system must resolve:

"the other one"

against the current clarification context.

It must not blindly accept the response as a valid Resource identifier.

The resulting candidate must pass through normal schema validation, resolution, scope checks, and applicable Trust conditions.

A clarification response is not authoritative merely because it came from the Actor.

⸻

26. Clarification Can Be Invalid

A clarification response may:

* remain ambiguous
* contradict known facts
* identify an unavailable Resource
* violate a Constraint
* fail to satisfy the required field
* identify a Resource outside permitted scope
* introduce a new material ambiguity
* materially change the requested goal

Noema should then either:

Clarify again

or transition to another appropriate state.

Example:

Question:
Which account should receive the transfer?
Answer:
"My old account."
Result:
Still ambiguous.
State:
CLARIFICATION_REQUIRED

A materially changed goal should not be silently incorporated into the existing Intent version.

⸻

27. Clarification Should Have Termination Conditions

A clarification loop must not continue indefinitely.

Possible termination conditions include:

* Resolved
* Cancelled
* Expired
* Rejected
* Maximum clarification attempts reached
* Required information unavailable
* Required authoritative evidence unavailable

The exact policy is domain-dependent.

But the semantic lifecycle must always permit termination.

An unresolved clarification must never silently fall through to execution.

⸻

28. Clarification vs Cancellation

These are different.

CLARIFY

The Intent remains active but requires additional information.

CANCEL

The Actor no longer wants the Intent fulfilled.

For example:

System:
Which account should receive the transfer?
Human:
Never mind, cancel it.

The Intent should transition to:

CANCELLED

not remain indefinitely in:

CLARIFICATION_REQUIRED

Cancellation does not require a new Action.

⸻

29. Clarification vs Approval

Approval is not clarification.

Clarification provides missing semantic information.

Approval provides authorization or consent where required by the applicable policy or workflow.

Example:

"Which account should receive the transfer?"

→ Clarification

versus:

"This transfer exceeds your normal threshold. Approve?"

→ Approval

The distinction must remain explicit.

Clarification ≠ Approval

Approval does not eliminate the need for Trust evaluation.

⸻

30. Clarification vs Confirmation

Confirmation asks whether the Actor wants to proceed with an already-resolved Action.

Example:

"Transfer $10,000 to Savings Account ••••4821. Proceed?"

Clarification asks:

"Which savings account should receive the transfer?"

Therefore:

Clarification:
What do you mean?
Confirmation:
Do you want to proceed?

They are separate concepts.

Confirmation is a control requirement or precondition where applicable. It is not a Trust outcome.

⸻

31. Clarification Should Be Rare at the Right Layer

Noema should not repeatedly ask humans to provide information that existing authoritative systems already know.

Bad:

"What is your employee ID?"

when the Actor has already been authenticated and resolved.

Better:

Identity System
      ↓
Actor Resolution
      ↓
Resolved Actor
      ↓
No clarification required

The semantic layer should exploit authoritative Context and Resources before asking the human.

⸻

32. Clarification as a Design Principle

Noema should optimize for:

Resolve what can be known.
Ask only what must be known.
Never guess what matters.

This is the canonical clarification principle.

⸻

33. Canonical Clarification Rule

Noema may infer non-material details from sufficient authoritative evidence and context, but any unresolved detail that can materially alter the Action, authorization, policy evaluation, constraints, scope, or expected Outcome must be resolved explicitly before consequential execution.

The resolution must satisfy the applicable schema, evidence, scope, and Trust requirements.

This rule establishes the boundary between useful inference and unsafe guessing.

⸻

34. Example: Card Renewal

Consider:

"Renew my company card."

Noema resolves:

Actor:
Current authenticated user
Resource candidates:
Card#123
Card#456

If only one card is eligible:

Card#123

No clarification is necessary.

If two cards are eligible:

Card#123 — Corporate
Card#456 — Virtual

and the distinction affects the Action:

CLARIFICATION_REQUIRED

Question:

"Which card do you want to renew: your corporate card ending in 123 or your virtual card ending in 456?"

The answer completes Resource resolution.

The resulting Intent version must then pass through normal resolution, Context/State Reconciliation, and Trust evaluation.

⸻

35. Example: Access Grant

Intent:

"Give David the same access as Sarah."

Noema may need to resolve:

David
Sarah
Scope
Resource
Access Set

If Sarah has different permissions across multiple resources, the phrase:

"same access"

may be materially ambiguous.

Noema should identify the unresolved scope.

It might ask:

"Do you mean Sarah's access to the Engineering repository or her access to the Finance workspace?"

Again, the system is not asking for unnecessary technical details.

It is resolving the semantic ambiguity blocking safe execution.

The resulting access decision must still be evaluated independently under applicable authorization and policy.

⸻

36. Example: Payment Refund

Intent:

"Refund that duplicate payment."

Context may contain:

Customer: Acme
Payment A: $500
Payment B: $500
Payment C: $1,200

If available evidence cannot uniquely identify the duplicate payment:

CLARIFICATION_REQUIRED

If authoritative evidence establishes Payment B as the duplicate:

Resource:
Payment B

No clarification is required.

The principle remains:

Evidence before question.
Question before guess.

⸻

37. The Desired Experience

From the human’s perspective, clarification should feel like the system understands the task and is asking only for what it genuinely needs.

The experience should be:

Human:
"Renew my card."
Noema:
"Which card do you mean?
• Corporate card ending 1234
• Virtual card ending 5678"

not:

Noema:
"What card?"
"What is your ID?"
"What is your account?"
"What action should I perform?"
"What system should I use?"

The latter indicates that the semantic layer is failing to resolve information it should already possess.

⸻

38. What Clarification Protects Against

Clarification primarily protects against:

* Wrong Actor
* Wrong Action
* Wrong Resource
* Wrong Target
* Wrong Scope
* Wrong Context
* Wrong Policy Interpretation
* Wrong Authority Assumption
* Wrong Expected Outcome

Its purpose is therefore not conversational quality.

Its purpose is execution correctness.

⸻

39. What Clarification Does Not Protect Against

Clarification does not by itself guarantee:

* authorization
* policy compliance
* safe execution
* correct external system state
* successful execution
* business-state correctness

Those remain separate Trust, State Reconciliation, execution, verification, and enterprise-authority concerns.

Clarification only establishes information required to continue.

⸻

40. Clarification and State Reconciliation

Clarification should not be used to compensate for unresolved enterprise state that Noema can deterministically investigate.

For example, if the system receives:

"Where is my payment?"

and the ambiguity concerns the current state of a known transaction, Noema should not ask the user to supply information that can be obtained through authorized enterprise observations and State Reconciliation.

The preferred sequence is:

Intent
   ↓
Resolve available identifiers
   ↓
Context / State Reconciliation
   ↓
Current reconciled state
   ↓
Continue

Only when the remaining uncertainty is semantic and materially blocks safe continuation should Noema ask the Actor.

State Reconciliation resolves enterprise-state uncertainty.

Clarification resolves Intent-level semantic uncertainty.

⸻

41. Clarification and Fact Status

Clarification decisions may depend on the Fact Status of relevant evidence.

Fact Status values include:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Two candidate accounts

is different from:

One account established as VERIFIED
One account with UNKNOWN current status

Noema must not treat UNKNOWN, STALE, or CONFLICTED evidence as equivalent to verified current state merely because it appears in Context.

Where the ambiguity can be resolved through State Reconciliation, reconciliation should be attempted before asking the human where appropriate.

⸻

42. Clarification and Resolved Identity

Where clarification concerns identity, Noema must distinguish:

* Actor
* Subject
* Principal
* Resource owner
* Delegated identity

A human response cannot by itself establish authoritative identity.

For example:

"Use John's account."

may still require deterministic identity resolution against enterprise identity and resource ownership data.

Identity resolution must precede consequential Trust and execution where identity affects authority.

⸻

43. Clarification and Scope

A clarification response must not expand scope implicitly.

For example:

"Give David access to the repository."

followed by:

"All repositories."

is not merely a clarification if it materially expands the requested scope.

Noema must represent the changed semantic request explicitly.

A material change creates a new Intent version rather than silently expanding the existing Intent.

⸻

44. Clarification and Intent Immutability

Once an Intent Object has been admitted to Trust, its semantic content is immutable.

Clarification may produce:

Intent v1
    ↓
CLARIFICATION_REQUIRED
    ↓
Human response
    ↓
Intent v2
supersedes v1

The historical Intent v1 remains preserved.

Trust decisions, execution records, and audit records must reference the exact Intent version they evaluated.

This preserves causal and historical interpretability.

⸻

45. Clarification and Planner

Clarification must occur before planning when unresolved information could alter the executable plan.

The planner must not silently choose among materially ambiguous alternatives.

Canonical flow:

Intent
   ↓
Resolution
   ↓
Clarification if required
   ↓
Resolved Intent
   ↓
State Reconciliation
   ↓
Trust
   ↓
EAG / Capability Selection
   ↓
Planning

The planner may optimize among valid alternatives only after the semantic request is sufficiently resolved.

It cannot use planning to conceal unresolved Intent ambiguity.

⸻

46. Clarification and Capability Selection

Capability ambiguity should be handled differently from Resource ambiguity.

If multiple capabilities are semantically equivalent and Noema can deterministically select one according to registered policy and capability metadata, no clarification is required.

If the capabilities represent materially different user-facing meanings or outcomes and available evidence cannot determine which was intended, clarification may be required.

Noema should prefer semantic resolution over exposing implementation choices to the user.

⸻

47. Clarification and Security

Clarification is itself a data-disclosure boundary.

Candidate lists, questions, and contextual information must contain only information the Actor is authorized to receive.

For example, when presenting possible recipients, Noema must not expose private information about unrelated enterprise users merely because it would make disambiguation easier.

The system must therefore consider authorization and data boundaries when constructing clarification responses.

A clarification mechanism cannot bypass protected-data controls.

⸻

48. Clarification and Human Intervention

Clarification and Human Intervention are distinct.

Clarification asks the Actor or relevant interaction participant for missing semantic information.

Human Intervention is an explicit decision boundary used when deterministic autonomous continuation is not permitted or cannot safely proceed.

For example:

Which account should receive the transfer?

is clarification.

Where a policy requires an authorized human reviewer to approve an already-resolved high-risk operation:

PENDING_HUMAN_REVIEW

is Human Intervention.

Neither should be conflated with Trust outcomes.

⸻

49. Clarification and Timeout

A timeout while waiting for clarification is not itself an execution failure.

The Intent may transition to an operational state such as:

EXPIRED

or remain pending according to applicable lifecycle policy.

The system must preserve the distinction between:

No response received

and:

Human explicitly cancelled the Intent

Silence must not be interpreted as authorization or confirmation.

⸻

50. Clarification and Events

An event may provide information that resolves an ambiguity.

For example:

Intent:
"Use the latest approved contract."
Event:
Contract#123 approved at 14:03.

The event remains an observation subject to schema validation, provenance, authority, and State Reconciliation.

An event must not automatically resolve a material ambiguity merely because it contains a plausible value.

The event-derived claim must satisfy the applicable evidence and authority requirements.

⸻

51. Clarification and Outcome

Clarification concerns the requested semantic goal.

It must not be confused with the actual Outcome of execution.

For example:

Intent:
"Send the contract to John."
Clarification:
"Which John?"
Resolved Intent:
"Send the contract to John Smith."
Outcome:
"Contract delivery verified."

The clarification resolves the request.

The Outcome describes what actually happened after execution and verification.

⸻

52. Clarification and Enterprise Business State

Clarification must not establish or mutate enterprise business state.

For example:

Human:
"Use account 4821."

This resolves a Resource reference.

It does not establish:

Account 4821 is active.

That fact must come from appropriate enterprise authority and State Reconciliation.

Similarly, clarification cannot establish that a requested transaction succeeded.

Enterprise business state remains owned by the relevant System of Record.

⸻

53. Clarification and Confirmation After Resolution

A resolved Intent may still require confirmation before execution.

For example:

Intent v1
   ↓
Clarification
   ↓
Intent v2
   ↓
Resolved
   ↓
Trust
   ↓
Confirmation Required
   ↓
Execution

Confirmation is a separate execution control.

Clarification does not imply consent to execute.

⸻

54. Clarification and Multiple Ambiguities

An Intent may contain multiple material ambiguities.

Noema may resolve them:

* sequentially
* as a grouped clarification
* through deterministic evidence
* through a structured form

provided that each material ambiguity has an explicit resolution criterion.

For example:

Intent:
"Book me a flight to Paris next Friday."
Unresolved:
Destination interpretation
Departure airport
Travel date

A structured clarification may ask for the required fields together if doing so is more efficient and does not create additional ambiguity.

The resulting Intent version must contain all required resolved semantics.

⸻

55. Clarification and Batch Operations

When an Intent applies to multiple Resources, clarification may be required at different granularities.

For example:

"Archive these customer records."

If some records are uniquely identified and others are ambiguous, Noema should preserve the distinction.

It must not resolve the entire batch through an unsupported assumption.

Possible result:

Resolved:
Records A, B, C
Clarification Required:
Record D

The execution plan must not silently include unresolved Resources.

⸻

56. Clarification and Composite Intent

A composite Intent may contain multiple sub-intents.

Clarification should identify the specific sub-intent affected.

For example:

"Cancel my old card and order a new one."

If the card to cancel is ambiguous but the replacement card is not, clarification should target the cancellation sub-intent rather than blocking unrelated semantic information unnecessarily.

The clarification record should preserve the relationship between the parent Intent and affected sub-intent.

⸻

57. Clarification and No Silent Expansion

A clarification response must not silently expand an Intent beyond its original semantic scope.

For example:

Original:
"Send the report to John."
Clarification:
"Which John?"
Response:
"John Smith, and send it to his whole team too."

The second clause materially expands the requested Action.

Noema must not treat this as merely answering the clarification.

The expanded request requires explicit semantic representation and, where applicable, a new Intent version.

⸻

58. Clarification and Re-Resolution

After a clarification response, Noema must re-run the relevant resolution pipeline.

It must not assume that resolving one field makes all previously evaluated conditions remain valid.

A clarification can change:

* Resource identity
* Scope
* Policy applicability
* Authorization
* Capability selection
* Preconditions
* Risk
* Required confirmation
* Plan

Therefore:

Clarification Response
        ↓
New Intent Version
        ↓
Resolution
        ↓
Context / State Reconciliation
        ↓
Trust Re-evaluation
        ↓
Planning / Execution

Prior Trust decisions must not be silently reused when their evaluated Intent version no longer applies.

⸻

59. Clarification and Historical Reproducibility

Noema must preserve enough information to reconstruct why clarification occurred.

Historical reconstruction should include, where applicable:

* Intent version
* unresolved target
* candidate set
* relevant evidence references
* Fact Status
* clarification question
* Actor response
* resulting Intent version
* resolution result
* subsequent Trust Decision

Historical clarification records are part of causal auditability.

⸻

60. Canonical Clarification Lifecycle

The canonical lifecycle is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Resolution
      ↓
Context / State Reconciliation
      ↓
Material ambiguity?
      │
      ├── No ──→ Trust
      │
      └── Yes
           ↓
      Clarification
           ↓
      Human Response
           ↓
      New Intent Version
           ↓
      Hard Schema Validation
           ↓
      Resolution
           ↓
      Context / State Reconciliation
           ↓
      Trust
           ↓
      Action / Execution

This lifecycle makes clarification part of the deterministic semantic pipeline rather than an informal conversational fallback.

⸻

61. Canonical Clarification Invariants

1. Clarification is a first-class Intent lifecycle state.
2. Clarification is not an error condition.
3. Material ambiguity must not be resolved through unsupported guessing.
4. Model confidence must not determine whether clarification is required.
5. Model confidence is not Fact Status.
6. Model confidence is not authority.
7. Clarification must identify the unresolved semantic requirement.
8. Clarification targets must be typed.
9. Clarification questions should be minimally sufficient.
10. Clarification questions must not introduce material ambiguity.
11. Existing authoritative Context should be used before asking the human where appropriate.
12. State Reconciliation should be used where current enterprise state can deterministically resolve the uncertainty.
13. Context presence alone does not establish authority.
14. Evidence must not be treated as authoritative merely because it exists.
15. Fact Status must remain distinct from Evidence.
16. VERIFIED, UNVERIFIED, STALE, CONFLICTED, and UNKNOWN must remain semantically distinguishable.
17. Human clarification responses are inputs and must be revalidated.
18. A clarification response cannot manufacture authority.
19. Clarification cannot bypass policy.
20. Clarification cannot bypass authorization.
21. Clarification cannot expand enterprise data access.
22. Clarification cannot establish enterprise business truth.
23. Clarification cannot establish execution success.
24. Clarification is distinct from Confirmation.
25. Clarification is distinct from Approval.
26. Clarification is distinct from Human Intervention.
27. Clarification is distinct from Failure.
28. Clarification is distinct from the canonical Trust outcomes.
29. The canonical Trust outcomes remain EXECUTE, CLARIFY, ESCALATE, and REJECT.
30. CLARIFY as a Trust outcome must not be confused with the broader Intent clarification lifecycle mechanism.
31. Trust EXECUTE must not be interpreted as execution success.
32. An unresolved clarification must never silently proceed to execution.
33. Material clarification must create a new Intent version.
34. Admitted Intent versions must remain immutable.
35. New Intent versions must preserve supersedes lineage.
36. Trust decisions must reference the exact Intent version they evaluate.
37. Clarification must not silently mutate a prior Trust decision.
38. Clarification responses must trigger relevant re-resolution.
39. Relevant Context and State Reconciliation must be reconsidered after material clarification.
40. Prior Trust decisions must not be reused when their Intent version no longer applies.
41. Resolved Actor, Action, Target, Resource, and Scope must be preserved where consequential.
42. Capability ambiguity must not be resolved through arbitrary provider or implementation selection.
43. Planner logic must not conceal unresolved semantic ambiguity.
44. Model-generated clarification questions remain non-authoritative.
45. Human-facing clarification must not unnecessarily expose implementation details.
46. Candidate lists must respect applicable data boundaries and authorization.
47. Clarification must not disclose protected information merely to improve disambiguation.
48. Enterprise business state remains authoritative in the relevant System of Record.
49. Clarification must not create shadow canonical business state.
50. Enterprise Events may provide evidence relevant to clarification but do not automatically establish truth.
51. Event-derived claims remain subject to validation, provenance, authority, and reconciliation requirements.
52. Provider or system metadata cannot establish semantic authority merely through declaration.
53. Silence or timeout while awaiting clarification must not be interpreted as approval, confirmation, or authorization.
54. Cancellation must remain distinct from failure to answer.
55. Clarification loops must have explicit termination conditions.
56. Clarification records must preserve sufficient causal audit information.
57. Clarification must preserve historical Intent and resolution lineage.
58. Composite and batch Intents must preserve the identity of the specific unresolved sub-intent or Resource.
59. Material Intent expansion must not be silently incorporated into a clarification response.
60. Clarification must resolve information, not determine permission.
61. Clarification must resolve information, not determine enterprise business Outcome.
62. Clarification must resolve information, not determine execution success.
63. Read-only operations may still require clarification when the target or protected scope is materially ambiguous.
64. Clarification must operate within the same structural security boundary as the rest of Noema.
65. No raw model output may directly become an authoritative clarification resolution.
66. Clarification cannot create a new capability or Action Contract.
67. Clarification cannot grant credentials or permissions.
68. Clarification must not bypass Action Contracts.
69. Clarification must not bypass deterministic Trust.
70. The purpose of clarification is to establish sufficient semantic resolution for safe continuation.
71. Noema should resolve what can be known before asking what must be known.
72. Noema must never guess what materially affects consequential execution.

⸻

62. Final Definition

Clarification is the controlled transition by which Noema resolves a material uncertainty in an Intent before that Intent can be safely converted into an Action.

It is a typed, stateful, auditable mechanism for resolving semantic information that cannot be established from sufficient authoritative evidence or reconciled enterprise state.

Clarification does not grant authority, establish enterprise truth, replace Trust evaluation, or guarantee execution success.

The governing principle is:

If it can be resolved from authoritative evidence or reconciled state
    → resolve it.
If it cannot be resolved and does not materially matter
    → proceed.
If it cannot be resolved and materially matters
    → clarify.
If clarification cannot establish a sufficiently resolved and permissible Intent
    → stop or transition to the appropriate governed state.

Or, more simply:

Resolve what can be known.
Ask what must be known.
Never guess what matters.