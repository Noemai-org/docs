Executable Intent

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: 02-intent/executable-intent.md

⸻

1. Definition

An Executable Intent is a resolved Intent whose semantic requirements have been sufficiently established to permit deterministic Trust evaluation and potential execution as one or more Actions.

An Executable Intent is not merely an Intent that a Model understands.

It is an Intent that has crossed the semantic boundary from:

"I think I understand what the Actor wants."

to:

"I have a sufficiently explicit representation of what the Actor wants
to evaluate whether it may be acted upon."

The canonical transition is:

Expression
    ↓
Interpretation
    ↓
Resolution
    ↓
Executable Intent
    ↓
Trust
    ↓
Action

⸻

2. Why Executable Intent Exists

Noema needs a stable boundary between probabilistic interpretation and deterministic execution.

Without that boundary, the Model remains implicitly responsible for deciding:

What the user meant
What Resource is involved
What Action should happen
Whether it is allowed
Whether it is safe

That creates an unsafe execution model:

Human
  ↓
Model
  ↓
Tool

Noema instead establishes:

Human
  ↓
Model
  ↓
Intent
  ↓
Resolution
  ↓
Executable Intent
  ↓
Trust
  ↓
Action

The Executable Intent becomes the semantic handoff point between interpretation and execution.

⸻

3. Executable Does Not Mean Authorized

This distinction is fundamental.

An Executable Intent means:

The Intent is sufficiently specified to evaluate for execution.

It does not mean:

The Intent is permitted to execute.

Therefore:

Executable Intent
       ↓
Trust Evaluation
       ├── PERMIT
       ├── CLARIFY
       ├── DENY
       └── REQUIRE_APPROVAL

The existence of an Executable Intent does not bypass:

Authority
Policy
Constraints
State
Capability requirements

⸻

4. Intent States

A simplified Intent lifecycle is:

EXPRESSED
    ↓
INTERPRETING
    ↓
RESOLVING
    ↓
┌────────────────────┐
│                    │
│     CLARIFYING     │
│                    │
└─────────┬──────────┘
          ↓
   EXECUTABLE
          ↓
        TRUST
          ↓
       ACTION
          ↓
      OUTCOME

An Intent should not become Executable merely because a Model has produced a plausible interpretation.

⸻

5. Minimum Requirement

An Intent becomes Executable when Noema has established the semantic information necessary to evaluate the intended Action.

The exact requirements are domain-dependent, but typically include:

Actor
Intent
Action
Target Resource(s)
Required parameters
Relevant Context
Required Constraints
Expected Outcome

Not every Intent requires every field.

The canonical rule is:

An Executable Intent must contain enough resolved semantic information to determine what Action is being requested without requiring the Model to guess.

⸻

6. Example

Human:

“Refund John’s duplicate payment.”

A Model might initially produce:

Intent:
RefundPayment
Actor:
Current User
Customer:
John
Reason:
Duplicate
Payment:
Unknown

This is not yet Executable.

Suppose Noema finds:

John has three payments.
Two are identical.
One was already refunded.

The system may still need to determine which payment is intended.

After sufficient resolution:

Executable Intent
Actor:
Alice
Action:
RefundPayment
Resource:
Payment#8291
Reason:
DuplicatePayment
Expected Outcome:
Payment#8291 refunded to John

Now Trust can be evaluated.

⸻

7. Executable Intent as a Contract

An Executable Intent should function as a semantic contract between:

Intent Resolution

and:

Trust / Execution

The contract answers:

Who is acting?
What do they intend?
What should be acted upon?
What Action represents that Intent?
Under what relevant Context?
What Outcome is expected?

The execution layer should not need to reinterpret the original natural-language request to determine those facts.

⸻

8. The Model Must Not Be the Executable Intent

The Model may generate a structured representation.

That representation is not automatically canonical.

For example:

{
  "action": "refund_payment",
  "payment_id": "8291"
}

is merely a candidate interpretation until Noema validates and resolves it.

The canonical sequence is:

Model Output
    ↓
Candidate Intent
    ↓
Validation
    ↓
Resolution
    ↓
Executable Intent

⸻

9. Executable Intent Is Canonical

Once established, the Executable Intent should become the canonical semantic representation of the request for that execution lifecycle.

Downstream systems should not repeatedly reinterpret:

"Refund John's duplicate payment."

Instead they should consume the resolved representation.

This prevents semantic drift.

⸻

10. Semantic Drift

Without a canonical Executable Intent, different components may interpret the same request differently.

For example:

Model:
Refund Payment #8291
Policy Engine:
Refund Customer #123
Execution Adapter:
Refund Transaction #8297

The system has now lost semantic integrity.

Executable Intent provides the common reference:

Canonical Intent
       ↓
Policy
       ↓
Capability
       ↓
Action

All layers operate against the same semantic meaning.

⸻

11. Executable Intent vs Action

These concepts must remain distinct.

Intent

What the Actor wants to accomplish.

Executable Intent

The resolved representation of that Intent that is sufficiently specified for execution evaluation.

Action

The operation performed to satisfy the Intent.

For example:

Intent:
"Get me my money back for the duplicate charge."
Executable Intent:
Refund Payment #8291
for Customer #123
with expected Outcome = refunded funds
Action:
RefundPayment(Payment#8291)

Therefore:

Intent ≠ Action

even when an Intent maps directly to one Action.

⸻

12. One Intent May Produce Multiple Actions

An Executable Intent does not necessarily correspond to a single Action.

Example:

“Close my old account and move the remaining balance to my new account.”

Executable Intent:

Actor:
Alice
Intent:
CloseAccount
Resources:
OldAccount
NewAccount
Expected Outcome:
Balance transferred
Old account closed

Actions might be:

TransferBalance
    ↓
VerifyTransfer
    ↓
CloseAccount

The Executable Intent remains the semantic root.

⸻

13. One Intent May Have Multiple Valid Action Plans

An Intent may be satisfiable through different Action sequences.

For example:

“Get this customer back on the premium plan.”

Possible plans:

Plan A:
RestoreSubscription
Plan B:
CreateSubscription
+
CancelOldSubscription

The Executable Intent should represent the desired semantic Outcome rather than prematurely hard-code implementation details.

Capability and policy resolution may determine which Action plan is appropriate.

⸻

14. Executable Intent vs Capability

Capability represents what a system or Actor is capable of doing.

Executable Intent represents what the Actor wants to accomplish.

For example:

Capability:
RefundPayment
Intent:
"Give the customer their money back."

Noema determines whether:

RefundPayment

is an appropriate Capability/Action for satisfying the Executable Intent.

The human should not need to know the internal Capability name.

⸻

15. Executable Intent vs Tool Call

A Tool Call is an implementation-level operation.

Example:

refund_payment(payment_id=8291)

An Executable Intent is semantic:

Refund Payment #8291
because it was identified as a duplicate,
with expected Outcome = funds returned to customer.

The Tool Call may be generated from the Executable Intent.

It must not replace it.

Executable Intent
        ↓
Action
        ↓
Capability
        ↓
Tool / API

⸻

16. Required Resolution

An Executable Intent must have resolved all material variables.

For example:

"Send the report to John."

If three Johns exist:

Recipient = unresolved

The Intent is not Executable.

Noema must:

CLARIFY

If one John is uniquely established:

Recipient = John Smith

the Intent may become Executable.

⸻

17. Non-Material Variables

Not every missing field prevents execution.

For example:

Intent:
SendReport
Required:
Recipient
Report
Optional:
Notification wording
Email formatting preference

If the optional wording is unknown, Noema can use a valid default.

The Executable Intent should contain the semantic requirements necessary for the Action, not every possible piece of metadata.

⸻

18. Executable Intent and Defaults

Defaults may be used when they are:

explicitly defined
domain-valid
non-material
policy-compatible
deterministic

For example:

User:
"Schedule a meeting with Sarah tomorrow."

If the organization’s default meeting duration is 30 minutes, Noema may resolve:

Duration:
30 minutes

without clarification.

But a default must never silently resolve a material ambiguity.

⸻

19. Executable Intent and Context

Context can supply information required to make an Intent Executable.

Example:

Current Context:
Viewing Invoice #9281
User:
"Refund this."

Context may resolve:

Resource:
Invoice #9281

provided that the contextual reference is valid and sufficiently authoritative.

Thus:

Intent + Context
        ↓
Executable Intent

when the context legitimately resolves the required semantics.

⸻

20. Executable Intent and Explicit References

Explicit user references should generally carry strong semantic weight.

For example:

“Refund invoice #9281.”

provides a direct Resource reference.

Noema should still validate that:

Invoice #9281 exists
Actor can access it
Invoice is eligible for refund

Explicit reference does not bypass Trust.

⸻

21. Executable Intent and Constraints

Constraints may be encoded into or associated with the Executable Intent.

Example:

Intent:
BookFlight
Destination:
London
Date:
September 12
Constraint:
Nonstop
Constraint:
Under $800

The resulting Executable Intent captures the requirements necessary for selecting a valid Action.

Constraints remain independently evaluable.

⸻

22. Executable Intent and Policy

Policy should not be confused with Intent.

For example:

Executable Intent:
Refund Payment #8291

Policy may subsequently determine:

Refund amount < $1,000
    → permitted
Refund amount >= $1,000
    → approval required

The Intent does not change merely because Policy changes the Trust outcome.

⸻

23. Executable Intent and Authority

The Actor is part of the semantic Intent representation.

But authority is evaluated separately.

Example:

Executable Intent:
Delete Customer #123
Actor:
Alice

Trust then evaluates:

Does Alice have authority to delete Customer #123?

Therefore:

Executable Intent
    ≠
Authorized Intent

Authorization is a Trust decision.

⸻

24. Executable Intent and State

An Executable Intent is resolved against relevant state.

Example:

Intent:
Renew Card #123

At resolution:

Card #123:
Expired
Eligible for renewal

This may produce an Executable Intent.

But if the state changes before execution:

Card #123:
Already renewed

Noema must re-evaluate the Action against current state.

Executable does not mean permanently executable.

⸻

25. Temporal Validity

Executable Intent may therefore have a validity period.

For example:

Executable Intent
    ↓
Valid at T1
    ↓
State changes
    ↓
Trust reevaluation

The exact implementation may use:

timestamps
versions
state snapshots
resource revisions

The canonical principle is:

An Executable Intent must remain semantically valid against the state under which the Action will execute.

⸻

26. Executable Intent and Idempotency

Where an Intent can produce consequential Actions, Noema should preserve enough semantic identity to determine whether an Action has already been performed.

Example:

Intent:
Refund duplicate payment #8291

If the system retries after a network failure, it must distinguish:

Action never executed

from:

Action executed but response was lost

Executable Intent can provide the semantic root for idempotent execution and Outcome verification.

⸻

27. Executable Intent and Human Confirmation

Some Executable Intents may require explicit human confirmation before execution.

For example:

Executable Intent:
Transfer $50,000 to Account #123

Trust may determine:

REQUIRE_CONFIRMATION

The Intent remains the same.

Confirmation does not change what the Actor wants.

It establishes an additional authorization or consent condition.

⸻

28. Executable Intent and Clarification

Clarification happens before Executable Intent when required semantic information is missing.

Unresolved Intent
      ↓
CLARIFY
      ↓
Resolution
      ↓
Executable Intent

If new information creates another material ambiguity, the Intent can return to clarification.

Therefore:

Executable
    ↕
Clarifying

may occur more than once during a long-running Intent lifecycle.

⸻

29. Executable Intent and Confidence

Confidence is an input into resolution.

Executable Intent is the result of successful resolution.

Candidate Interpretation
        ↓
Confidence + Evidence
        ↓
Resolution
        ↓
Executable Intent

An Executable Intent should not require downstream components to interpret Model confidence again.

Once the semantic claims have been resolved, their canonical values become authoritative for that lifecycle.

⸻

30. Executable Intent Should Be Deterministic

Given the same:

Executable Intent
+
relevant State
+
Policy
+
Authority
+
Constraints

the Trust evaluation should produce the same semantic decision.

This is a central architectural property.

The Model may be probabilistic upstream.

The Trust boundary should not be.

⸻

31. Canonical Structure

Conceptually, an Executable Intent may contain:

ExecutableIntent
├── Identity
├── Actor
├── Intent
├── Action
├── Resources
├── Parameters
├── Context
├── Constraints
├── ExpectedOutcome
├── Evidence
├── Resolution
└── Version

Not every field is mandatory for every Intent.

The required fields depend on the semantic requirements of the Action.

⸻

32. Identity

Every Executable Intent should have a stable identity within its lifecycle.

Conceptually:

Intent ID:
intent_01...

This allows Noema to associate:

Clarifications
Trust decisions
Approvals
Actions
Events
Outcomes
Audit records

with the same semantic Intent.

⸻

33. Version

Executable Intent may evolve during clarification or resolution.

For example:

Intent v1
Resource:
Unknown

After clarification:

Intent v2
Resource:
Card#123

The history should preserve the semantic evolution.

This is especially important when the Intent results in consequential Actions.

⸻

34. Evidence

The Executable Intent should retain references to the evidence used to resolve material claims.

For example:

Resource:
Card#123
Evidence:
Actor owns Card#123
Card#123 is active
User explicitly selected Card#123

The evidence does not become the Intent.

It supports the resolution of the Intent.

⸻

35. Expected Outcome

An Executable Intent should express the Outcome the Actor is attempting to achieve where that Outcome can be meaningfully defined.

Example:

Intent:
Renew Card
Expected Outcome:
Card renewed and active

This is important because:

Action success

does not necessarily mean:

Intent satisfaction

⸻

36. Executable Intent and Outcome Verification

The lifecycle becomes:

Executable Intent
      ↓
Trust
      ↓
Action
      ↓
Observed State
      ↓
Outcome Verification

Noema can therefore distinguish:

Executed

from:

Satisfied

This distinction is central to trustworthy automation.

⸻

37. Executable Intent Is Not a Workflow

An Executable Intent should not encode every implementation step.

For example:

Wrong:
Step 1:
POST /customers/123
Step 2:
GET /plans
Step 3:
POST /subscription
Step 4:
POST /email

That is a workflow or execution plan.

Instead:

Executable Intent:
Restore Customer #123 to Premium Plan

The execution system determines the appropriate Actions and sequence.

⸻

38. Executable Intent Is Not a Prompt

A prompt is an instruction to a Model.

An Executable Intent is a semantic object.

Therefore:

Prompt:
"Please refund John's duplicate payment."
Executable Intent:
RefundPayment(
    Customer=John,
    Payment=#8291
)

The latter can be:

validated
audited
versioned
authorized
executed
verified

without depending on natural-language interpretation.

⸻

39. Executable Intent as the Semantic Boundary

The most important architectural role of Executable Intent is establishing this boundary:

┌──────────────────────────────────┐
│       Probabilistic Layer        │
│                                  │
│ Language                         │
│ Model interpretation             │
│ Retrieval                        │
│ Candidate generation             │
│ Confidence                       │
└────────────────┬─────────────────┘
                 │
                 ▼
        EXECUTABLE INTENT
                 │
                 ▼
┌──────────────────────────────────┐
│       Deterministic Layer        │
│                                  │
│ Trust                            │
│ Authority                        │
│ Policy                           │
│ Constraints                     │
│ Capability                      │
│ State                            │
│ Execution                        │
│ Outcome verification             │
└──────────────────────────────────┘

This boundary is one of the most important concepts in Noema.

⸻

40. The Canonical Rule

No probabilistic interpretation may directly invoke a consequential Action. It must first resolve into an Executable Intent that can be evaluated deterministically by the Trust layer.

This is a core Noema invariant.

⸻

41. What Makes an Intent Executable?

An Intent is Executable when:

✓ Actor is resolved
✓ Intent is resolved
✓ Material Resources are resolved
✓ Required parameters are resolved
✓ Required Context is established
✓ Relevant Constraints are known
✓ Expected Outcome is sufficiently defined
✓ No material ambiguity remains

Then:

Executable Intent
        ↓
Trust Evaluation

can begin.

⸻

42. What Prevents an Intent From Becoming Executable?

Examples include:

✗ Material ambiguity
✗ Unknown Resource
✗ Unknown required parameter
✗ Unresolved Actor
✗ Missing required Context
✗ Conflicting evidence
✗ Unsupported Action
✗ Missing required Outcome definition

The appropriate response may be:

CLARIFY

or:

DENY

depending on the reason.

⸻

43. Canonical Lifecycle Example

Human:

“Delete the old project.”

Step 1 — Interpretation

Intent:
DeleteProject

Step 2 — Candidate Resolution

Project A
Project B
Project C

Step 3 — Evidence

Project A:
Archived 2 years ago
Project B:
Active
Project C:
Archived 3 months ago

Step 4 — Clarification

If “old” remains materially ambiguous:

CLARIFY

Step 5 — Resolution

Human:

“Project A.”

Step 6 — Executable Intent

Actor:
Alice
Intent:
DeleteProject
Resource:
Project A
Expected Outcome:
Project A deleted

Step 7 — Trust

Authority:
Valid
Policy:
Permitted
Constraints:
Satisfied

Step 8 — Action

DeleteProject(ProjectA)

Step 9 — Outcome

Project A:
Deleted

The Intent lifecycle is complete.

⸻

44. Canonical Principles

Noema should treat Executable Intent according to these principles:

1. Executable Intent is the semantic handoff point between interpretation and execution.

2. Executable does not mean authorized.

3. Model output is not automatically an Executable Intent.

4. Material ambiguity must be resolved before an Intent becomes Executable.

5. The Executable Intent must be canonical and machine-readable.

6. Downstream systems should not reinterpret the original human expression.

7. Executable Intent should preserve the semantic Outcome being pursued.

8. Trust evaluates Executable Intent; it does not create it.

9. Actions execute from the resolved semantic representation, not directly from Model output.

10. Executable Intent remains subject to current state and Trust evaluation.

⸻

45. Final Definition

An Executable Intent is the canonical, sufficiently resolved representation of an Actor’s Intent from which Noema can deterministically evaluate Trust and derive permissible Actions without requiring further probabilistic interpretation of the original request.

The fundamental pipeline is:

Human Intent
      ↓
Model Interpretation
      ↓
Evidence + Confidence
      ↓
Resolution
      ↓
┌─────────────────────┐
│ EXECUTABLE INTENT   │
└──────────┬──────────┘
           ↓
       TRUST ENGINE
           ↓
     ┌─────┼─────┐
     ↓     ↓     ↓
  PERMIT CLARIFY DENY
     ↓
   ACTION
     ↓
  OUTCOME

The shortest formulation is:

Intent expresses what the Actor wants. Executable Intent makes that desire explicit enough for Noema to decide whether and how it may act.