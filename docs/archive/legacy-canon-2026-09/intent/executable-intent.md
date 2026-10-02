Executable Intent

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/executable-intent.md

⸻

1. Definition

An Executable Intent is a resolved Intent whose semantic requirements have been sufficiently established for deterministic Trust evaluation and potential execution as one or more Actions.

An Executable Intent is not merely an Intent that a Model understands.

It is an Intent that has crossed the semantic boundary from:

"I think I understand what the Actor wants."

to:

"I have a sufficiently explicit representation of what the Actor wants
to evaluate whether it may be acted upon."

The canonical transition is:

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
Executable Intent
      ↓
Deterministic Trust
      ↓
Action
      ↓
Execution
      ↓
Verification
      ↓
Outcome

⸻

2. Why Executable Intent Exists

Noema needs a stable boundary between probabilistic interpretation and deterministic execution.

Without that boundary, the Model remains implicitly responsible for deciding:

What the Actor meant
What Resource is involved
What Action should happen
Whether it is permitted
Whether the current state permits it

That creates an unsafe execution model:

Source
  ↓
Model
  ↓
Tool

Noema instead establishes:

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
Executable Intent
  ↓
Trust
  ↓
Action Contract
  ↓
Execution

The Executable Intent is the semantic handoff point between Intent interpretation/resolution and deterministic Trust evaluation.

It does not itself authorize execution.

⸻

3. Executable Does Not Mean Authorized

This distinction is fundamental.

An Executable Intent means:

The semantic requirements necessary for Trust evaluation
have been sufficiently established.

It does not mean:

The Intent is permitted to execute.

Therefore:

Executable Intent
       ↓
Trust Evaluation
       ├── EXECUTE
       ├── CLARIFY
       ├── ESCALATE
       └── REJECT

The existence of an Executable Intent does not bypass:

Authority
Policy
Constraints
Current State
Capability requirements
Action Contracts

EXECUTE means that the applicable Trust conditions permit the Action to proceed. It does not mean that execution has succeeded.

⸻

4. Intent States

A simplified Intent lifecycle is:

RECEIVED
    ↓
INTERPRETING
    ↓
VALIDATING
    ↓
ADMITTED
    ↓
RESOLVING
    ↓
┌─────────────────────────┐
│ CLARIFICATION_REQUIRED  │
│ / CLARIFYING            │
└────────────┬────────────┘
             ↓
          RESOLVED
             ↓
       EXECUTABLE
             ↓
        TRUST_PENDING
             ↓
     TRUST DECISION
             ↓
          ACTION
             ↓
        EXECUTION
             ↓
       VERIFICATION
             ↓
          OUTCOME

An Intent should not become Executable merely because a Model has produced a plausible interpretation.

If material information remains unresolved, Noema must resolve it through authoritative Context, State Reconciliation, additional evidence, clarification, escalation, or another explicitly governed mechanism.

⸻

5. Minimum Requirement

An Intent becomes Executable when Noema has established the semantic information necessary to evaluate the intended Action without requiring consequential interpretation by the Model.

The exact requirements are Action- and domain-dependent, but may include:

Actor
Intent
Action
Target Resource(s)
Required parameters
Relevant Context
Required Constraints
Applicable scope
Expected Outcome

Not every Intent requires every field.

The canonical rule is:

An Executable Intent must contain enough resolved semantic
information to determine what is being requested and what
must be evaluated by Trust without requiring the Model to guess.

⸻

6. Example

Human:

"Refund John's duplicate payment."

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

Suppose Noema obtains enterprise observations and performs State Reconciliation:

John has three payments.
Two are identical.
One was already refunded.

The relevant Resource may still be unresolved.

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

Trust can now evaluate whether this resolved request may proceed.

The Executable Intent does not itself establish that Alice is authorized to refund the payment.

⸻

7. Executable Intent as a Semantic Contract

An Executable Intent functions as a semantic contract between Intent Resolution and downstream deterministic evaluation.

It answers:

Who is the Actor?
What does the Actor intend?
What Action represents that Intent?
What Resource is affected?
What parameters are required?
What relevant scope and Context apply?
What Outcome is being pursued?

The execution layer should not need to reinterpret the original natural-language request to determine those semantics.

The contract does not replace:

Trust Contract
Action Contract
Execution Contract

Each remains responsible for its own semantics.

⸻

8. The Model Must Not Be the Executable Intent

The Model may generate a structured representation.

That representation is not automatically canonical.

For example:

{
  "action": "refund_payment",
  "payment_id": "8291"
}

is merely a candidate interpretation until it passes the appropriate validation and resolution process.

The canonical sequence is:

Model Output
    ↓
Candidate Intent
    ↓
Hard Schema Validation
    ↓
Admitted Intent
    ↓
Resolution
    ↓
Executable Intent

Model output remains untrusted.

No free-form Model output may directly become an executable Action request.

⸻

9. Executable Intent Is Canonical

Once established, the Executable Intent is the canonical semantic representation of the request for that Intent version and execution lifecycle.

Downstream systems should not repeatedly reinterpret:

"Refund John's duplicate payment."

Instead they should consume the resolved semantic representation.

This prevents semantic drift between:

Intent
Policy
Trust
Capability
Planning
Action
Execution

The canonical representation must preserve its version and lineage.

⸻

10. Semantic Drift

Without a canonical Executable Intent, different components may interpret the same request differently.

For example:

Model:
Refund Payment #8291
Policy Evaluation:
Refund Customer #123
Execution Adapter:
Refund Transaction #8297

The system has lost semantic integrity.

Executable Intent provides the common semantic reference:

Executable Intent
       ↓
Trust / Policy Evaluation
       ↓
Capability / Action Selection
       ↓
Action Contract
       ↓
Execution

Every downstream stage operates against the same admitted Intent version and resolved semantic bindings.

⸻

11. Executable Intent vs Action

These concepts must remain distinct.

Intent

What the Actor wants to accomplish.

Executable Intent

The resolved representation of that Intent that is sufficiently specified for deterministic Trust evaluation and bounded Action selection.

Action

The typed semantic operation performed to satisfy the Intent.

For example:

Intent:
"Get me my money back for the duplicate charge."
Executable Intent:
Refund Payment #8291
for Customer #123
with Expected Outcome = refunded funds
Action:
RefundPayment(Payment#8291)

Therefore:

Intent ≠ Executable Intent ≠ Action

An Executable Intent may map to one Action or multiple Actions.

⸻

12. One Intent May Produce Multiple Actions

An Executable Intent does not necessarily correspond to a single Action.

Example:

"Close my old account and move the remaining balance to my new account."

Executable Intent:

Actor:
Alice
Intent:
CloseAccountAndTransferBalance
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
      ↓
VerifyClosure

The Executable Intent remains the semantic root.

Each consequential Action remains subject to its applicable Action Contract, Trust requirements, execution controls, and verification.

⸻

13. One Intent May Have Multiple Valid Action Plans

An Intent may be satisfiable through different Action sequences.

For example:

"Get this customer back on the premium plan."

Possible plans might include:

Plan A:
RestoreSubscription

or:

Plan B:
CreateSubscription
+
CancelOldSubscription

The Executable Intent should represent the desired semantic result without prematurely hard-coding implementation details that belong to planning and execution.

The Planner may select among permitted alternatives only within:

Enterprise Action Graph
Capability Registry
Action Registry
Action Contracts
Applicable Policy and Trust constraints

The Planner cannot invent an Action or Capability merely because it would satisfy the Intent.

⸻

14. Executable Intent vs Capability

Capability represents an available bounded ability within the enterprise execution environment.

Executable Intent represents what the Actor wants to accomplish.

For example:

Capability:
RefundPayment
Intent:
"Give the customer their money back."

Noema determines whether an available Capability and corresponding Action can satisfy the Executable Intent.

The human should not need to know the internal Capability name.

Capability existence also does not imply:

permission
authorization
current availability
Trust approval
successful execution

These remain separate concerns.

⸻

15. Executable Intent vs Tool Call

A Tool Call is an implementation-level invocation.

Example:

refund_payment(payment_id=8291)

An Executable Intent is semantic:

Refund Payment #8291
because it was identified as a duplicate,
with Expected Outcome = funds returned to customer.

The Tool Call may be produced from a permitted Action and Action Contract.

It must not replace the semantic Intent.

The canonical relationship is:

Executable Intent
        ↓
Trust
        ↓
Action
        ↓
Capability
        ↓
Action Contract
        ↓
Tool / API / Provider Operation

⸻

16. Required Resolution

An Executable Intent must have resolved all material variables required for its intended Action.

For example:

"Send the report to John."

If three Johns exist within the applicable scope:

Recipient = unresolved

The Intent is not Executable.

Noema may first attempt to resolve the ambiguity through:

Validated Context
Authoritative Identity Data
State Reconciliation
Explicit references
Deterministic resolution rules

If material ambiguity remains:

CLARIFY

If one recipient is sufficiently established:

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

If the optional wording is unknown, Noema can use a valid deterministic default where permitted.

The Executable Intent should contain the semantic requirements necessary for the Action, not every possible piece of metadata.

⸻

18. Executable Intent and Defaults

Defaults may be used when they are:

explicitly defined
domain-valid
non-material
policy-compatible
deterministic
within the applicable scope

For example:

User:
"Schedule a meeting with Sarah tomorrow."

If the organization’s applicable default meeting duration is 30 minutes, Noema may resolve:

Duration:
30 minutes

without clarification.

A default must never silently resolve a material ambiguity involving Actor, Target, Action, authority, scope, parameters, or other consequential semantics.

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

provided that the reference is valid, within scope, sufficiently fresh, and supported by the applicable evidence.

Context is not inherently authoritative.

The canonical relationship is:

Intent
   +
Validated Relevant Context
   +
Applicable State Reconciliation
        ↓
Resolved Semantic State
        ↓
Executable Intent

⸻

20. Executable Intent and Explicit References

Explicit references should generally carry strong semantic weight.

For example:

"Refund invoice #9281."

provides a direct Resource reference.

Noema must still validate the reference and relevant current state, including where applicable:

Invoice #9281 exists
Resource is within applicable scope
Actor is resolved
Resource is eligible for the requested Action
Required enterprise state is current enough

An explicit reference does not bypass Trust.

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
Constraints:
Nonstop
Under $800

The resulting Executable Intent captures the requirements necessary to determine which permissible Action or plan can satisfy the request.

Constraints remain independently evaluable.

Confidence does not satisfy a constraint.

⸻

22. Executable Intent and Policy

Policy should not be confused with Intent.

For example:

Executable Intent:
Refund Payment #8291

A policy may subsequently determine:

Refund amount < $1,000
    → permitted
Refund amount >= $1,000
    → approval required

The semantic Intent does not change merely because Policy changes the Trust decision or introduces a control requirement.

Policy remains a separate deterministic governance layer.

⸻

23. Executable Intent and Authority

The Actor is part of the semantic representation.

Authority is evaluated separately.

Example:

Executable Intent:
Delete Customer #123
Actor:
Alice

Trust then evaluates whether the resolved Actor has the applicable authority for that Action, Resource, and scope.

Therefore:

Executable Intent
    ≠
Authorized Intent

Authorization does not become true merely because the Actor is resolved.

Technical authorization, policy authorization, and business authorization remain distinct where applicable.

⸻

24. Executable Intent and State

An Executable Intent is resolved against relevant enterprise state, but its existence does not freeze that state.

Example:

Intent:
Renew Card #123

At resolution:

Card #123:
Expired
Eligible for renewal

This may produce an Executable Intent.

Before execution:

Card #123:
Already renewed

Noema must evaluate the Action against current applicable state again.

Therefore:

Executable
    ≠
Permanently executable

State Reconciliation may be required before Trust, before execution, or during recovery.

⸻

25. Temporal Validity

An Executable Intent may have temporal validity associated with its semantic assumptions.

For example:

Executable Intent
       ↓
Valid under state at T1
       ↓
Relevant state changes
       ↓
State Reconciliation
       ↓
Trust / Action re-evaluation

The implementation may use:

timestamps
resource versions
state snapshots
validity intervals
policy versions
contract versions

The canonical principle is:

An Executable Intent does not make historical state permanently current.

Current consequential execution must use sufficiently current and authoritative information for the relevant claims.

⸻

26. Executable Intent and Idempotency

Where an Intent can produce consequential Actions, Noema should preserve sufficient semantic identity to support idempotent execution and Outcome verification.

Example:

Intent:
Refund duplicate payment #8291

If execution encounters a network failure, Noema must distinguish:

Action never executed

from:

Action executed but the response was lost

The Executable Intent provides semantic lineage for the operation, but idempotency identity remains Action- and execution-specific.

Unknown execution state must not be treated as success or failure without appropriate verification or State Reconciliation.

⸻

27. Executable Intent and Human Confirmation

Some Executable Intents may require explicit human confirmation before execution.

For example:

Executable Intent:
Transfer $50,000 to Account #123

Trust may determine that a confirmation or approval control is required.

The canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Confirmation is a control requirement or precondition, not a fifth Trust outcome.

Confirmation does not change what the Actor semantically requested.

Approval may establish an additional governance condition, but approval does not itself establish execution success.

⸻

28. Executable Intent and Clarification

Clarification occurs during Intent resolution when required semantic information is missing.

The canonical flow is:

Unresolved Intent
      ↓
Context / State Reconciliation
      ↓
Material ambiguity remains
      ↓
CLARIFICATION_REQUIRED
      ↓
Clarification
      ↓
New Intent Version
      ↓
Resolution
      ↓
Executable Intent

A material clarification response must not mutate an already admitted Intent version.

Instead:

Intent v1
   ↓
Clarification
   ↓
Intent v2
supersedes v1
   ↓
Resolution
   ↓
Executable Intent v2

Clarification can recur during a long-running Intent lifecycle.

⸻

29. Executable Intent and Confidence

Confidence is an input to interpretation and resolution.

Executable Intent is the result of sufficiently successful semantic resolution.

Conceptually:

Candidate Interpretation
        ↓
Confidence / Interpretation Metadata
        +
Evidence
        +
Context / State Reconciliation
        ↓
Semantic Resolution
        ↓
Executable Intent

An Executable Intent should not require downstream components to reinterpret Model confidence.

Once semantic claims have been resolved, downstream components operate on the canonical representation and its supporting provenance.

Confidence does not establish Fact Status, authority, or Trust.

⸻

30. Executable Intent Should Be Deterministically Evaluable

The purpose of an Executable Intent is to provide enough semantic structure for deterministic downstream evaluation.

Given the same relevant:

Executable Intent version
State
Policy version
Authority information
Constraints
Capability / Graph versions
Action Contract version

the applicable deterministic evaluation should have reproducible semantics.

The Model may remain probabilistic upstream.

The Trust boundary must not depend on an unconstrained probabilistic reinterpretation of the original request.

⸻

31. Canonical Structure

Conceptually, an Executable Intent may contain:

ExecutableIntent
├── Identity
├── Version
├── Source
├── Actor
├── Intent
├── Action
├── Resources
├── Parameters
├── Scope
├── Context References
├── Constraints
├── Expected Outcome
├── Resolution
└── Evidence References

Not every field is mandatory for every Intent.

The required fields depend on the semantic requirements of the relevant Action and the conditions necessary for Trust evaluation.

An Executable Intent should reference supporting evidence rather than embedding arbitrary evidence as though it were canonical enterprise truth.

⸻

32. Identity

Every Intent should have a stable identity within its lifecycle.

Conceptually:

Intent ID:
intent_01...

This allows Noema to associate:

Clarifications
Intent Versions
Trust Decisions
Approvals
Actions
Execution Attempts
Events
Outcomes
Audit Records

with the same semantic Intent lineage.

Identity is distinct from version.

⸻

33. Version

Executable Intent is version-specific.

For example:

Intent v1
Resource:
Unknown

After clarification:

Intent v2
Resource:
Card#123
supersedes:
v1

An admitted Intent version is immutable.

A material clarification, correction, or semantic change creates a new Intent Object version rather than mutating the existing one.

Every consequential Trust Decision and execution record must reference the exact Intent version on which it was based.

⸻

34. Evidence and Resolution Provenance

The Executable Intent should retain references to the evidence used to resolve material claims.

For example:

Resource:
Card#123
Resolution:
Resolved
Evidence:
Actor owns Card#123
Card#123 is active
User explicitly selected Card#123
Current enterprise state confirms eligibility

Evidence supports resolution.

It does not become the Intent.

Similarly, Model confidence may be retained as interpretation metadata without becoming authoritative evidence or Fact Status.

⸻

35. Expected Outcome

An Executable Intent should express the Outcome the Actor is attempting to achieve where that Outcome can be meaningfully defined.

Example:

Intent:
Renew Card
Expected Outcome:
Card renewed and active

This distinction is important because:

Action execution

does not necessarily establish:

Intent satisfaction

and:

Expected Outcome

does not establish:

Actual Outcome

Actual Outcome is established through execution observation and verification.

⸻

36. Executable Intent and Outcome Verification

The lifecycle becomes:

Executable Intent
      ↓
Trust
      ↓
Action Contract
      ↓
Execution
      ↓
Observed Enterprise State / Evidence
      ↓
State Reconciliation / Verification
      ↓
Outcome

Noema can therefore distinguish:

Action dispatched

from:

Action completed

and:

Intent satisfied

An EXECUTE Trust decision does not establish any of these outcomes by itself.

⸻

37. Executable Intent Is Not a Workflow

An Executable Intent should not encode every implementation step.

For example:

Wrong abstraction:
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

The Planner determines an appropriate Action sequence within the bounded Enterprise Action Graph, Capability Registry, Action Registry, and Action Contracts.

Executable Intent expresses semantic requirements, not implementation choreography.

⸻

38. Executable Intent Is Not a Prompt

A prompt is an instruction to a Model.

An Executable Intent is a canonical semantic object.

Therefore:

Prompt:
"Please refund John's duplicate payment."

versus:

Executable Intent:
Action:
RefundPayment
Customer:
John
Payment:
Payment#8291
Reason:
DuplicatePayment

The latter can be:

validated
versioned
resolved
audited
evaluated by Trust
planned
executed
verified

without requiring downstream components to reinterpret the original natural-language request.

⸻

39. Executable Intent as the Semantic Boundary

The most important architectural role of Executable Intent is establishing the boundary between probabilistic interpretation and deterministic evaluation.

┌─────────────────────────────────────┐
│         Probabilistic Layer         │
│                                     │
│ Source interpretation               │
│ Language                            │
│ Model inference                     │
│ Retrieval                           │
│ Candidate generation                │
│ Confidence                          │
└──────────────────┬──────────────────┘
                   │
                   ▼
        HARD SCHEMA VALIDATION
                   │
                   ▼
          ADMITTED INTENT
                   │
                   ▼
      RESOLUTION / RECONCILIATION
                   │
                   ▼
        EXECUTABLE INTENT
                   │
                   ▼
┌─────────────────────────────────────┐
│         Deterministic Layer         │
│                                     │
│ Trust                               │
│ Authority                           │
│ Policy                              │
│ Constraints                         │
│ Capability                          │
│ Planning                            │
│ Action Contracts                    │
│ Execution                           │
│ Verification                        │
└─────────────────────────────────────┘

The hard schema validation/admission boundary is important because a Model-generated structure must not become canonical merely because it resembles the Intent schema.

⸻

40. The Canonical Rule

No probabilistic interpretation may directly invoke a consequential Action.

It must first pass through:

Candidate Interpretation
        ↓
Hard Schema Validation
        ↓
Admitted Intent
        ↓
Resolution
        ↓
Executable Intent
        ↓
Deterministic Trust
        ↓
Bounded Action / Action Contract
        ↓
Execution

No free-form Model output may bypass this boundary.

The same principle applies when the Source of Intent is an agent, workflow, system, API, event, or other non-human source.

⸻

41. What Makes an Intent Executable?

An Intent is Executable when Noema has established the semantic information required for the relevant downstream evaluation.

Typically:

✓ Actor is resolved
✓ Intent is resolved
✓ Material Resources are resolved
✓ Required parameters are resolved
✓ Required scope is resolved
✓ Required Context is established
✓ Relevant current state is sufficiently reconciled
✓ Required Constraints are known
✓ Expected Outcome is sufficiently defined where applicable
✓ No material semantic ambiguity remains

Then:

Executable Intent
        ↓
Trust Evaluation

can begin.

Executable does not mean:

✓ Authorized
✓ Permitted
✓ Successfully executed
✓ Outcome achieved

Those are separate states.

⸻

42. What Prevents an Intent From Becoming Executable?

Examples include:

✗ Material ambiguity
✗ Unknown required Resource
✗ Unknown required parameter
✗ Unresolved Actor
✗ Unresolved target
✗ Missing required Context
✗ Conflicting evidence
✗ Unsupported Action
✗ Missing required scope
✗ Insufficient semantic resolution

The appropriate response depends on the reason.

For example:

Material ambiguity
        ↓
CLARIFY

or:

Material uncertainty that cannot be resolved safely
        ↓
ESCALATE

or:

Requested Action is prohibited or cannot be permitted
        ↓
REJECT

These are distinct from execution FAILED and execution UNKNOWN.

⸻

43. Canonical Lifecycle Example

Human:

"Delete the old project."

Step 1 — Interpretation

Intent:
DeleteProject

Step 2 — Candidate Resolution

Project A
Project B
Project C

Step 3 — Evidence and State Reconciliation

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

"Project A."

The response is validated and creates a new Intent version:

Intent v2
supersedes v1

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

Trust evaluates:

Authority:
Valid
Policy:
Permitted
Constraints:
Satisfied
Current State:
Reconciled

The resulting Trust outcome may be:

EXECUTE

if all applicable conditions are satisfied.

Step 8 — Action Contract

DeleteProject

is bound to its registered Action Contract.

Step 9 — Execution

DeleteProject(ProjectA)

Step 10 — Verification and Outcome

Noema verifies the resulting enterprise state and establishes the actual Outcome.

Project A:
Deleted

The Trust decision permitted execution; verification establishes what actually happened.

⸻

44. Canonical Principles

Noema should treat Executable Intent according to these principles:

1. Executable Intent is the semantic handoff point between Intent resolution and deterministic Trust evaluation.
2. Executable does not mean authorized, permitted, or successful.
3. Model output is not automatically an Executable Intent.
4. Hard schema validation and admission precede canonical Intent semantics.
5. Material ambiguity must be resolved before an Intent becomes Executable.
6. Authoritative Context and State Reconciliation should be used to resolve uncertainty where possible before asking the Actor.
7. The Executable Intent must be canonical, typed, and machine-readable.
8. An admitted Intent version is immutable.
9. Material clarification or semantic change creates a new Intent version with explicit lineage.
10. Downstream systems should not reinterpret the original Source of Intent.
11. Executable Intent should preserve the semantic Outcome being pursued where applicable.
12. Trust evaluates the Executable Intent; it does not create or authorize it merely by existence.
13. Actions execute from bounded semantic representations and registered Action Contracts, not directly from Model output.
14. Capability existence does not imply authorization or successful execution.
15. Executable Intent remains subject to current relevant state and Trust evaluation.
16. Confidence informs interpretation and resolution but does not establish authority, Fact Status, or Trust.
17. Unknown and conflicting state must remain explicit rather than being converted into a confident guess.
18. Actual Outcome is established through execution observation and verification, not by the Executable Intent itself.

⸻

45. Final Definition

An Executable Intent is the canonical, sufficiently resolved representation of a Source of Intent from which Noema can deterministically evaluate Trust and derive permissible Actions without requiring further probabilistic interpretation of the original request.

The canonical pipeline is:

Source of Intent
      ↓
Candidate Interpretation
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Context / State Reconciliation
      ↓
Semantic Resolution
      ↓
EXECUTABLE INTENT
      ↓
Deterministic Trust
      ↓
EAG / Capability Selection
      ↓
Action Contract
      ↓
Execution
      ↓
Verification / State Reconciliation
      ↓
Outcome

The shortest formulation is:

Intent expresses what the Actor wants.
Executable Intent makes that meaning explicit enough
for Noema to evaluate it deterministically.
Trust determines whether Noema may act.
Execution determines what happened.
Verification establishes the Outcome.