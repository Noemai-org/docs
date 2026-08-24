Clarification

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: 02-intent/clarification.md

⸻

1. Definition

Clarification is the explicit resolution of an unresolved or ambiguous aspect of an Intent required before Noema can safely determine an Action.

Clarification is not an error condition.

It is a first-class Intent state and interaction mechanism.

When Noema cannot establish sufficient semantic certainty to proceed deterministically, it must transition into clarification rather than infer beyond its permitted boundary.

⸻

2. Why Clarification Exists

Human Intent is frequently incomplete.

For example:

“Send the report to John.”

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
Intent resolution continues

⸻

3. The Core Rule

When a material ambiguity prevents deterministic resolution of an Intent, Noema must clarify rather than guess.

This is one of the fundamental Trust principles of Noema.

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
Trust evaluation
   ↓
Action

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
Model Confidence ≠ Trust

Clarification is determined by the semantic requirements of the Intent and the evidence available to satisfy them.

⸻

5. Material vs Non-Material Ambiguity

Not every ambiguity requires clarification.

Noema should distinguish between:

Non-material ambiguity

An ambiguity that does not affect the resulting Action or Outcome.

Example:

“Send the report to Sarah.”

If Sarah has one canonical identity and the exact wording of the report title is irrelevant to the Action, Noema need not ask unnecessary questions.

Material ambiguity

An ambiguity that can change:

Action
Resource
Actor
Authority
Policy evaluation
Constraint satisfaction
Outcome

Example:

“Transfer $5,000 to my savings account.”

If the Actor has three savings accounts, the target Resource is materially ambiguous.

Clarification is required.

⸻

6. Clarification Is About Resolution, Not Conversation

Noema should not ask questions merely because a Model feels uncertain.

A clarification request must correspond to a specific unresolved semantic requirement.

Bad:

“Could you provide more information?”

Good:

“You have two savings accounts. Which one should receive the $5,000 transfer?”

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

Actor
Entity
Resource
Capability
Action
Parameter
Context
Constraint
Policy
Authority
Outcome

For example:

Intent:
TransferMoney
Clarification Target:
Resource
Question:
Which savings account should receive the transfer?

⸻

8. Clarification State

Clarification is represented as an explicit Intent lifecycle state.

A simplified lifecycle is:

EXPRESSED
    ↓
INTERPRETING
    ↓
RESOLVING
    ↓
┌───────────────┐
│               │
│  CLARIFYING   │
│               │
└───────┬───────┘
        ↓
    RESOLVED
        ↓
     TRUSTED
        ↓
     ACTION

An Intent may enter clarification more than once if multiple independent ambiguities are discovered during resolution.

⸻

9. Clarification Is Not Failure

The following states must remain conceptually distinct:

CLARIFY
DENY
FAIL

Clarify

The system can potentially fulfill the Intent but lacks required information.

Deny

The system has enough information to determine that the requested operation cannot be permitted.

Fail

The system attempted execution but could not successfully complete it.

Therefore:

Missing information → CLARIFY
Prohibited operation → DENY
Execution failure → FAIL

⸻

10. Clarification Must Preserve Intent

A clarification response must refine the existing Intent rather than create an unrelated new Intent.

Example:

Initial Intent:
"Send the contract to John."

Noema asks:

“Which John do you mean?”

Human responds:

“John Smith.”

The resulting Intent is:

SendContract
  Actor: existing Actor
  Resource: existing Contract
  Recipient: John Smith

The original Intent remains the semantic root.

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

“Which John do you mean: John Smith or John Doe?”

The goal is:

Minimum Question
        ↓
Maximum Resolution

⸻

12. Clarification Should Prefer Choices When Possible

When Noema can enumerate valid candidates, clarification should preferably expose those candidates.

Instead of:

“Which account?”

prefer:

“Which account should receive the transfer?”

1. Savings ••••4821
2. Savings ••••9174

This reduces ambiguity in the human response and makes resolution easier to validate.

⸻

13. Clarification Must Not Introduce New Ambiguity

A clarification question should itself be unambiguous.

Bad:

“Which account do you want?”

if the system has multiple account types.

Better:

“Which savings account should receive the transfer?”

The clarification mechanism must reduce semantic uncertainty rather than move it elsewhere.

⸻

14. Clarification and Context

Context can sometimes resolve ambiguity without asking the human.

For example:

“Send this to John.”

If the current Context contains:

Current conversation:
John Smith is the active recipient.

and that context is authoritative and sufficient, Noema may resolve the reference without clarification.

However, contextual inference must remain subject to the same Trust requirements as any other resolution.

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

Resolve from authoritative evidence before asking the human, but never infer beyond what the evidence supports.

⸻

16. Clarification and Trust

Clarification belongs inside the Trust pipeline.

Conceptually:

Intent
  ↓
Resolution
  ↓
Is required information sufficient?
  │
  ├── Yes ──→ Trust Evaluation
  │
  └── No ───→ Clarification

Therefore, clarification is a mechanism for achieving the preconditions necessary for a Trust decision.

⸻

17. Clarification and Authority

Some ambiguity concerns the Actor rather than the target Resource.

Example:

“Approve the payment.”

Noema may know which payment is being discussed but not whether the current Actor is acting:

personally
on behalf of a department
on behalf of an organization

If that distinction affects authority, clarification may be necessary.

However, clarification cannot manufacture authority.

The human answering:

“I’m approving it for the company.”

does not automatically establish that they possess that authority.

Authority must still be independently evaluated.

⸻

18. Clarification and Policy

A clarification may resolve information required to evaluate Policy.

For example:

“Create a new production deployment.”

Noema may require:

Environment
Release
Change window
Approval status

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

explicit
implicit
system-defined
policy-derived
resource-derived
contextual

Example:

“Book me the cheapest flight.”

Possible unresolved constraints:

Destination
Travel date
Departure airport
Cabin
Baggage requirements

Noema should identify which missing constraints materially affect the resulting Action.

It should not ask for constraints that are irrelevant to the requested Outcome.

⸻

20. Clarification and Capabilities

Sometimes the Intent is understood, but the system cannot determine which Capability should satisfy it.

For example:

“Get this document signed.”

Possible Capabilities:

ElectronicSignature
InternalApproval
DocumentWorkflow

If domain semantics or Context cannot establish the intended mechanism, Noema may need clarification.

However, where the Intent specifies the Outcome rather than the implementation, Noema should generally prefer selecting an appropriate Capability itself.

The human should not be forced to understand implementation details unnecessarily.

⸻

21. Clarification Should Not Leak Implementation Details

Noema should generally ask:

“Which account should receive the transfer?”

rather than:

“Which database record should I pass to the transfer_funds capability?”

The human-facing clarification should be expressed in the language of the Intent and relevant domain concepts.

Implementation details belong below the semantic boundary.

⸻

22. Clarification as a Typed Object

Conceptually, a Clarification may contain:

Clarification
├── Intent
├── Target
├── Reason
├── Question
├── Candidates
├── Required Information
├── Evidence
└── Resolution Criteria

For example:

Clarification
  Intent: TransferMoney
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

What was ambiguous?
Why was clarification required?
What question was asked?
What information was provided?
How did the answer resolve the ambiguity?
What Action resulted?

This is particularly important for consequential enterprise operations.

The audit trail should show the transition:

Intent
  ↓
Ambiguity
  ↓
Clarification
  ↓
Human Resolution
  ↓
Resolved Intent
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
Deterministic validation
        ↓
Trust evaluation

The Model assists communication.

Noema owns semantic state.

⸻

25. Clarification Must Be Re-Validated

Human clarification responses are themselves inputs.

For example:

“Use the other one.”

The system must resolve:

"the other one"

against the current clarification context.

It must not blindly accept the response as a valid Resource identifier.

The result must pass through normal resolution and validation.

⸻

26. Clarification Can Be Invalid

A clarification response may:

remain ambiguous
contradict known facts
identify an unavailable Resource
violate a Constraint
fail to satisfy the required field
change the Intent materially

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
CLARIFYING

⸻

27. Clarification Should Have Termination Conditions

A clarification loop must not continue indefinitely.

Possible termination conditions include:

Resolved
Cancelled
Expired
Denied
Maximum clarification attempts reached
Required information unavailable

The exact policy is domain-dependent.

But the semantic lifecycle must always permit termination.

⸻

28. Clarification vs Cancellation

These are different.

CLARIFY

means:

The Intent remains active but requires additional information.

CANCEL

means:

The Actor no longer wants the Intent fulfilled.

For example:

System:
Which account should receive the transfer?
Human:
Never mind, cancel it.

The Intent should transition to:

CANCELLED

not remain indefinitely in:

CLARIFYING

⸻

29. Clarification vs Approval

Approval is not clarification.

Clarification provides missing semantic information.

Approval provides authorization or consent.

Example:

"Which account should receive the transfer?"

→ Clarification

versus:

"This transfer exceeds your normal threshold. Approve?"

→ Approval

The distinction must remain explicit.

Clarification ≠ Approval

⸻

30. Clarification vs Confirmation

Confirmation asks whether the Actor wants to proceed with an already-resolved Action.

Example:

“Transfer $10,000 to Savings Account ••••4821. Proceed?”

Clarification asks:

“Which savings account should receive the transfer?”

Therefore:

Clarification:
What do you mean?
Confirmation:
Do you want to proceed?

They are separate concepts.

⸻

31. Clarification Should Be Rare at the Right Layer

Noema should not repeatedly ask humans to provide information that existing systems already know.

Bad:

“What is your employee ID?”

when the Actor has already been authenticated and resolved.

Better:

Identity system
      ↓
Actor resolved
      ↓
No clarification required

The semantic layer should exploit authoritative Context and Resources before asking the human.

⸻

32. Clarification as a Design Principle

Noema should optimize for:

Resolve what can be known.
Ask only what must be known.
Never guess what matters.

This can be treated as the canonical clarification principle.

⸻

33. Canonical Clarification Rule

Noema may infer non-material details from sufficient authoritative context, but any unresolved detail that can materially alter the Action, authorization, policy evaluation, constraints, or expected Outcome must be resolved explicitly before execution.

This rule establishes the boundary between useful inference and unsafe guessing.

⸻

34. Example: Card Renewal

Consider:

“Renew my company card.”

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

CLARIFY

Question:

“Which card do you want to renew: your corporate card ending in 123 or your virtual card ending in 456?”

The answer completes Resource resolution.

Trust evaluation can then proceed.

⸻

35. Example: Access Grant

Intent:

“Give David the same access as Sarah.”

Noema may need to resolve:

David
Sarah
Scope
Resource
Access set

If Sarah has different permissions across multiple resources, the phrase:

“same access”

may be materially ambiguous.

Noema should identify the unresolved scope.

It might ask:

“Do you mean Sarah’s access to the Engineering repository or her access to the Finance workspace?”

Again, the system is not asking for unnecessary technical details.

It is resolving the semantic ambiguity blocking execution.

⸻

36. Example: Payment Refund

Intent:

“Refund that duplicate payment.”

Context may contain:

Customer: Acme
Payment A: $500
Payment B: $500
Payment C: $1,200

If “duplicate payment” cannot uniquely identify the Resource:

CLARIFY

If evidence establishes Payment B as the duplicate:

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

Wrong Resource
Wrong Actor
Wrong Action
Wrong Scope
Wrong Context
Wrong Policy Interpretation
Wrong Outcome

Its purpose is therefore not conversational quality.

Its purpose is execution correctness.

⸻

39. What Clarification Does Not Protect Against

Clarification does not by itself guarantee:

authorization
policy compliance
safe execution
correct external system state
successful execution

Those remain separate Trust and execution concerns.

Clarification only establishes the information required to continue.

⸻

40. Canonical Summary

Clarification in Noema is:

First-class
Explicit
Typed
Stateful
Minimal
Auditable
Semantically grounded
Deterministically evaluated

It is not:

A Model fallback
A generic error
A conversational filler
An authorization mechanism
A policy bypass
A confirmation prompt

⸻

41. Final Definition

Clarification is the controlled transition by which Noema resolves a material uncertainty in an Intent before that Intent can be safely converted into an Action.

The governing principle is:

If it can be resolved from authoritative context → resolve it.
If it cannot be resolved and does not matter → proceed.
If it cannot be resolved and materially matters → clarify.
If clarification cannot establish a permissible Action → stop.

Or, more simply:

Resolve what can be known. Ask what must be known. Never guess what matters.