Intent Lifecycle

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-lifecycle.md

⸻

1. Definition

The Intent Lifecycle defines the canonical states and transitions through which an Intent passes from initial human expression to resolution, execution, and final Outcome.

An Intent is not a single event.

It is a persistent semantic object that evolves as Noema acquires information, resolves ambiguity, evaluates Trust, invokes Actions, and observes Outcomes.

The lifecycle therefore exists to answer:

What is the current semantic state of this Intent, and what must happen before it can transition to the next state?

⸻

2. Why the Intent Lifecycle Exists

A naive agent architecture often treats a request as:

User Request
     ↓
Model
     ↓
Tool Call
     ↓
Result

This collapses fundamentally different states into one operation.

Noema instead recognizes:

Expression
    ↓
Interpretation
    ↓
Grounding
    ↓
Resolution
    ↓
Validation
    ↓
Trust
    ↓
Execution
    ↓
Outcome

Each stage answers a different question.

⸻

3. The Core Lifecycle

The canonical lifecycle is:

EXPRESSED
    ↓
INTERPRETED
    ↓
GROUNDED
    ↓
RESOLVED
    ↓
EXECUTABLE
    ↓
AUTHORIZED
    ↓
EXECUTING
    ↓
COMPLETED

But an Intent may branch into other states:

                 ┌── AMBIGUOUS
                 │       ↓
INTERPRETED ─────┼── CLARIFICATION_REQUIRED
                 │       ↓
                 │   RESOLVED
                 │
                 └── INVALID
RESOLVED
   ↓
POLICY_BLOCKED
   ↓
REJECTED
EXECUTING
   ├── FAILED
   ├── PARTIALLY_COMPLETED
   └── COMPLETED

The lifecycle is therefore a state machine, not merely a linear pipeline.

⸻

4. Intent Identity Persists Across the Lifecycle

The Intent should retain a stable identity throughout its lifecycle.

Conceptually:

Intent#123

may transition through:

EXPRESSED
→ INTERPRETED
→ AMBIGUOUS
→ RESOLVED
→ EXECUTABLE
→ AUTHORIZED
→ EXECUTING
→ COMPLETED

It should not become a new semantic object merely because its state changes.

This enables:

auditability
traceability
re-evaluation
clarification
retry
cancellation

⸻

5. Lifecycle State vs Intent Meaning

The Intent’s meaning and lifecycle state are different concepts.

For example:

Intent:
RenewCard(Card#123)

may have:

State:
AMBIGUOUS

The Intent still exists.

Its semantic representation is simply incomplete.

Therefore:

Intent ≠ Intent State

⸻

6. EXPRESSed

Definition

EXPRESSED means an Actor has communicated something that may constitute an Intent, but Noema has not yet established its canonical semantic representation.

Example:

“Can you sort out my card?”

At this point Noema has:

Actor:
Known
Expression:
"Can you sort out my card?"
Intent:
Not yet resolved

The expression is evidence from which Intent is derived.

⸻

7. INTERPRETED

Definition

INTERPRETED means Noema has constructed a candidate Intent representation from the Actor’s expression.

Example:

Intent:
ResolveCardIssue
Actor:
User#123
Resource:
Unknown
Outcome:
CardIssueResolved

The interpretation may still contain unresolved fields.

Importantly:

Interpretation is not yet execution authority.

⸻

8. GROUNDED

Definition

GROUNDED means semantic references in the Intent have been connected to canonical concepts, Entities, Resources, Context, or other authoritative evidence.

Example:

Expression:
"Renew the card I used yesterday."
Grounding:
"card I used yesterday"
        ↓
Transaction#981
        ↓
Card#123

The Intent becomes:

RenewCard(Card#123)

Grounding reduces reference ambiguity.

⸻

9. AMBIGUOUS

Definition

AMBIGUOUS means Noema has identified multiple materially plausible interpretations and cannot safely select one.

Example:

Intent:
CancelSubscription
Candidate Resources:
Subscription#123
Subscription#456

Noema should not arbitrarily choose one.

This state is fundamental to Noema’s deterministic Trust architecture.

⸻

10. CLARIFICATION_REQUIRED

Definition

CLARIFICATION_REQUIRED means the Intent cannot safely progress without additional information from the Actor or another authoritative source.

Example:

Intent:
TransferFunds
Amount:
$500
Destination:
UNKNOWN

Noema asks:

“Which account should receive the $500?”

The clarification targets the unresolved semantic field.

⸻

11. CLARIFICATION

Clarification is a lifecycle activity, not necessarily the final state of the Intent.

Conceptually:

AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED
    ↓
Actor Response
    ↓
INTERPRETED / GROUNDED
    ↓
RESOLVED

A single Intent may require multiple clarification cycles.

⸻

12. RESOLVED

Definition

RESOLVED means the semantic representation of the Intent is sufficiently complete and unambiguous for Noema to determine what the Actor means.

Example:

Intent:
TransferFunds
Actor:
User#123
Source:
Checking#1
Destination:
Savings#2
Amount:
$500

The meaning is now resolved.

However:

Resolved does not mean executable.

Trust, Policy, Capability, and current State may still prevent execution.

⸻

13. VALIDATED

A resolved Intent may undergo validation against the canonical ontology and domain rules.

Validation can establish:

required fields exist
types are correct
references are valid
constraints are coherent
relationships are valid

Conceptually:

RESOLVED
   ↓
VALIDATED

Whether VALIDATED is represented as a persistent lifecycle state or as an internal transition is an implementation decision.

The semantic distinction should nevertheless exist.

⸻

14. EXECUTABLE

Definition

EXECUTABLE means Noema has enough semantic information and available Capabilities to construct an executable plan for satisfying the Intent, subject to Trust and Policy.

Example:

Intent:
RenewCard(Card#123)
Capability:
CardRenewal
Required information:
Resolved
Constraint validation:
Passed

The Intent is now actionable.

⸻

15. AUTHORIZED

Definition

AUTHORIZED means the Intent has passed the applicable Trust and Policy requirements and may proceed to execution.

Example:

Intent:
RefundPayment($500)
Trust:
Permitted
Policy:
Permitted
Authority:
Valid

The distinction is critical:

EXECUTABLE ≠ AUTHORIZED

A system may know exactly how to execute something without being permitted to do so.

⸻

16. POLICY_BLOCKED

Definition

POLICY_BLOCKED means the Intent is semantically valid but cannot proceed because a Policy prohibits or restricts execution.

Example:

Intent:
RefundPayment($50,000)
Policy:
Amounts > $10,000 require manager approval

The Intent is not necessarily invalid.

It is blocked by governance.

⸻

17. REJECTED

Definition

REJECTED means Noema has determined that the Intent cannot or should not proceed.

Possible reasons include:

policy violation
insufficient authority
invalid request
unsupported Capability
contradictory Constraints

The reason must be recorded.

⸻

18. EXECUTING

Definition

EXECUTING means one or more Actions associated with the Intent are currently being performed.

Example:

Intent:
RenewCard
State:
EXECUTING
Actions:
VerifyEligibility
CreateReplacementCard

Execution state must not be confused with Intent meaning.

The Intent remains:

RenewCard

regardless of which Action is currently running.

⸻

19. COMPLETED

Definition

COMPLETED means the expected Outcome of the Intent has been satisfied according to the applicable semantic criteria.

Example:

Intent:
RenewCard
Expected Outcome:
Card active
Observed Outcome:
Card active
State:
COMPLETED

Completion is determined by Outcome semantics, not merely successful Action invocation.

⸻

20. FAILED

Definition

FAILED means execution occurred but the expected Outcome was not achieved and the Intent cannot currently proceed automatically.

Example:

Intent:
RenewCard
Action:
CreateReplacementCard
Result:
Provider unavailable
State:
FAILED

Failure should preserve:

failure cause
Actions attempted
observed State
Outcome status

⸻

21. PARTIALLY_COMPLETED

A Composite Intent may be partially completed.

Example:

Composite:
TransferBalance + CloseAccount
TransferBalance:
COMPLETED
CloseAccount:
FAILED

The parent should not be represented simply as:

FAILED

without preserving the constituent states.

A Composite Intent may therefore have:

PARTIALLY_COMPLETED

where semantically appropriate.

⸻

22. CANCELLED

Definition

CANCELLED means the Actor or an authorized system has withdrawn the Intent before successful completion.

Example:

Intent:
BookFlight
State:
EXECUTING
Actor:
"Cancel that."

The Intent transitions to:

CANCELLED

subject to whether cancellation is still possible.

⸻

23. EXPIRED

Definition

EXPIRED means the Intent can no longer be meaningfully satisfied because its temporal validity has elapsed.

Example:

Intent:
BookFlight
Constraint:
DepartToday
CurrentTime:
After departure

The Intent may transition to:

EXPIRED

rather than FAILED.

The distinction matters because the system did not necessarily fail to execute it; its validity window ended.

⸻

24. SUPERSEDED

An Intent may be replaced by a newer Intent from the same Actor.

Example:

Intent A:
BookFlight for Monday
Intent B:
Actually, make it Tuesday.

Intent A may become:

SUPERSEDED

while Intent B becomes the active Intent.

This preserves history without continuing to treat the old request as authoritative.

⸻

25. INVALID

Definition

INVALID means the candidate Intent violates the semantic requirements of the Intent Language or domain ontology.

Example:

TransferFunds
Amount:
"banana"

or:

TransferFunds
Source:
Card#123
Destination:
SameCard#123
Domain Rule:
Source != Destination

Invalidity should be distinguished from ambiguity.

⸻

26. UNSUPPORTED

An Intent may be semantically clear but impossible to satisfy because Noema has no applicable Capability.

Example:

“Teleport me to London.”

Intent:
TeleportPerson
State:
UNSUPPORTED

The meaning is clear.

The system simply cannot satisfy it.

⸻

27. State Transition Rules

Transitions should be governed by explicit conditions.

Examples:

EXPRESSED
→ INTERPRETED

when a candidate semantic representation has been constructed.

INTERPRETED
→ GROUNDED

when material references are grounded.

GROUNDED
→ AMBIGUOUS

when multiple materially plausible interpretations remain.

GROUNDED
→ RESOLVED

when semantic ambiguity is eliminated.

RESOLVED
→ EXECUTABLE

when required Capabilities and execution information exist.

EXECUTABLE
→ AUTHORIZED

when Trust and Policy permit execution.

AUTHORIZED
→ EXECUTING

when execution begins.

EXECUTING
→ COMPLETED

when the expected Outcome is satisfied.

⸻

28. No Silent State Transitions

Noema should not silently move an Intent from:

AMBIGUOUS

to:

RESOLVED

because a Model produced a more confident guess.

A material semantic transition requires evidence sufficient for the relevant state change.

This is central to Noema’s deterministic architecture.

⸻

29. Model Confidence Does Not Define Lifecycle State

Suppose the Model produces:

Confidence:
0.97

for:

CancelSubscription(Subscription#123)

If two subscriptions remain materially plausible, the Intent remains:

AMBIGUOUS

Confidence is evidence.

It is not authority.

⸻

30. Evidence-Driven Transitions

Lifecycle transitions should be supported by evidence.

For example:

AMBIGUOUS
      ↓
Actor clarification
      ↓
RESOLVED

or:

GROUNDED
      ↓
Authoritative database lookup
      ↓
RESOLVED

or:

EXECUTABLE
      ↓
Policy evaluation
      ↓
POLICY_BLOCKED

The transition itself should be auditable.

⸻

31. Lifecycle and Provenance

Every meaningful state transition should ideally record:

previous state
new state
timestamp
actor/system responsible
reason
evidence

Example:

Intent#123
AMBIGUOUS → RESOLVED
Reason:
Actor clarified destination account.
Evidence:
ConversationTurn#42

This creates an auditable semantic history.

⸻

32. Lifecycle and Clarification Loops

Clarification may repeat.

Example:

INTERPRETED
    ↓
AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED
    ↓
Actor response
    ↓
AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED
    ↓
Actor response
    ↓
RESOLVED

Noema must support multiple clarification rounds without losing prior semantic state.

⸻

33. Lifecycle and Intent Modification

An Actor may modify an existing Intent.

Example:

“Book the flight for Friday.”

Then:

“Actually, make it Saturday.”

The Intent may be updated:

Constraint:
date = Saturday

or replaced by a new version.

The canonical model should preserve:

Intent identity
version
change history
superseded values
current values

where required.

⸻

34. Intent Versioning

An Intent may have versions:

Intent#123:v1
Intent#123:v2
Intent#123:v3

Example:

v1:
BookFlight(Monday)
v2:
BookFlight(Tuesday)
v3:
BookFlight(Tuesday, nonstop)

The current version represents the Actor’s current Intent.

Previous versions remain part of the audit history.

⸻

35. Lifecycle and Composite Intents

Composite Intents require both:

parent lifecycle state

and:

child lifecycle states

Example:

Composite:
EmployeeOffboarding
Parent:
EXECUTING
Children:
RevokeGitHub     COMPLETED
DisableEmail     EXECUTING
NotifyManager    RESOLVED

The parent state should be derived according to explicit composition semantics.

⸻

36. Lifecycle and Independent Children

A child Intent may resolve independently of another child.

Example:

Composite:
UpdateProfile
├── UpdateAddress     RESOLVED
├── UpdatePhone       AMBIGUOUS
└── UpdatePreferences RESOLVED

Noema should not discard the resolved semantic information simply because one child requires clarification.

⸻

37. Lifecycle and Parent Completion

A Composite Intent should only reach COMPLETED when its required Outcome semantics are satisfied.

For example:

TransferBalance
CloseAccount

If both are required:

Transfer = COMPLETED
Close = COMPLETED
Parent = COMPLETED

If:

Transfer = COMPLETED
Close = FAILED

then:

Parent ≠ COMPLETED

unless the domain explicitly defines a different success criterion.

⸻

38. Lifecycle and Action Retry

An Action may fail while the Intent remains active.

Example:

Intent:
SendInvoice
Action attempt #1:
FAILED
Retry:
Action attempt #2
Outcome:
SUCCESS

The Intent lifecycle need not become permanently FAILED because one Action attempt failed.

Therefore:

Action State ≠ Intent State

⸻

39. Lifecycle and Execution Attempts

An Intent may have multiple execution attempts.

Conceptually:

Intent#123
Attempt#1
  Action → FAILED
Attempt#2
  Action → SUCCESS
Intent → COMPLETED

The lifecycle should preserve the distinction between:

attempt failure

and:

Intent failure

⸻

40. Lifecycle and Compensation

If an executed Action must be compensated, the Intent may remain active while compensation occurs.

Example:

ChargeCustomer
     ↓
ProvisionService
     ↓
Provisioning fails
     ↓
RefundCustomer

The execution history records the compensation.

The final Intent state depends on its expected Outcome.

⸻

41. Lifecycle and External State

Intent lifecycle should not be confused with business-domain State.

Example:

Intent:
RenewCard
State:
EXECUTING
Card State:
Expired

After execution:

Intent:
COMPLETED
Card State:
Active

The two state systems are related but distinct.

⸻

42. Lifecycle and Outcome Verification

An Action returning success does not necessarily mean the Intent is complete.

Example:

Action:
UpdateDatabase
Result:
Success

But:

Expected Outcome:
Customer can log in

If login remains impossible, the Intent is not completed.

Therefore:

Intent completion is determined by verified Outcome, not merely Action success.

⸻

43. Lifecycle and Determinism

Noema should maintain deterministic rules for lifecycle transitions wherever possible.

For example:

if required_resource_missing
    → CLARIFICATION_REQUIRED
if policy_denied
    → POLICY_BLOCKED
if outcome_verified
    → COMPLETED

The Model may assist with interpretation.

It should not arbitrarily determine lifecycle state transitions.

⸻

44. Lifecycle and the Trust Engine

The Trust Engine operates on an Intent that has reached sufficient semantic resolution.

Conceptually:

Intent
   ↓
Resolved
   ↓
Executable
   ↓
Trust Engine
   ↓
Authorized / Rejected

This preserves the architectural separation:

Model:
"What does the Actor mean?"
Noema:
"Is the meaning sufficiently resolved?"
Trust:
"May it be executed?"
Execution:
"Perform the permitted Action."
Outcome:
"Did the intended state occur?"

⸻

45. Lifecycle and Business State

Noema owns Intent State.

The business system owns Business State.

For example:

Noema:
Intent#123 = EXECUTING
Bank:
Account#456 = OPEN

After successful execution:

Noema:
Intent#123 = COMPLETED
Bank:
Account#456 = CLOSED

Noema observes and reasons about business State but does not become the authoritative owner of it.

⸻

46. Terminal States

A terminal state is a state from which the current Intent cannot normally continue.

Examples:

COMPLETED
FAILED
CANCELLED
EXPIRED
REJECTED
SUPERSEDED
UNSUPPORTED
INVALID

A new Intent may be created or an existing Intent may be explicitly re-opened according to domain rules, but this should not happen implicitly.

⸻

47. Non-Terminal States

Typical non-terminal states include:

EXPRESSED
INTERPRETED
GROUNDED
AMBIGUOUS
CLARIFICATION_REQUIRED
RESOLVED
EXECUTABLE
AUTHORIZED
EXECUTING
PARTIALLY_COMPLETED
POLICY_BLOCKED

The exact persistent state model may evolve, but the semantic distinctions should remain.

⸻

48. Canonical State Machine

                         ┌──────────────┐
                         │  AMBIGUOUS   │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │ CLARIFICATION_REQ. │
                     └─────────┬──────────┘
                               │
                               ▼
┌──────────┐    ┌─────────────┐    ┌───────────┐
│ EXPRESSED├───►│ INTERPRETED ├───►│ GROUNDED  │
└──────────┘    └─────────────┘    └─────┬─────┘
                                         │
                                         ▼
                                  ┌────────────┐
                                  │  RESOLVED  │
                                  └─────┬──────┘
                                        │
                                        ▼
                                  ┌────────────┐
                                  │ EXECUTABLE │
                                  └─────┬──────┘
                                        │
                                        ▼
                                  ┌────────────┐
                                  │ AUTHORIZED │
                                  └─────┬──────┘
                                        │
                                        ▼
                                  ┌────────────┐
                                  │ EXECUTING  │
                                  └─────┬──────┘
                                        │
                         ┌──────────────┼──────────────┐
                         ▼              ▼              ▼
                    COMPLETED       FAILED      PARTIAL

With policy and authority branches:

RESOLVED / EXECUTABLE
        │
        ├── POLICY_BLOCKED
        ├── REJECTED
        └── UNSUPPORTED

⸻

49. Canonical Transition Rules

Rule 1 — Every Intent Has Identity

State changes do not create a new Intent identity.

Rule 2 — State Must Be Explicit

Noema must know the current lifecycle state of every active Intent.

Rule 3 — Ambiguity Blocks Material Execution

An unresolved material ambiguity must transition into clarification rather than silent guessing.

Rule 4 — Resolution Precedes Executability

An Intent cannot become Executable while material semantic fields remain unresolved.

Rule 5 — Executability Does Not Imply Authorization

Capability availability does not grant permission.

Rule 6 — Authorization Precedes Execution

Actions requiring Trust must not execute before the applicable Trust decision.

Rule 7 — Action Success Does Not Equal Intent Completion

Completion requires satisfaction of the expected Outcome.

Rule 8 — Partial Failure Must Be Representable

Composite Intents must preserve individual child states.

Rule 9 — Terminal States Require Explicit Re-entry

Completed, cancelled, rejected, or expired Intents should not silently resume.

Rule 10 — State Transitions Must Be Auditable

Material transitions should retain reason and provenance.

⸻

50. Lifecycle Invariants

Noema should maintain several invariants.

Invariant 1

AMBIGUOUS → EXECUTING

is invalid.

Invariant 2

UNRESOLVED → AUTHORIZED

is invalid.

Invariant 3

EXECUTABLE → AUTHORIZED

requires applicable Trust/Policy evaluation.

Invariant 4

EXECUTING → COMPLETED

requires Outcome satisfaction.

Invariant 5

A child Intent cannot inherit authorization merely because its parent was authorized.

Invariant 6

An Intent cannot silently change semantic meaning while retaining the same version.

⸻

51. Lifecycle and Audit Trail

A canonical audit record might look like:

Intent#123
09:00  EXPRESSED
      Source: User
09:00  INTERPRETED
      Objective: TransferFunds
09:01  GROUNDED
      Destination: Savings#456
09:01  RESOLVED
      Evidence: User clarification
09:01  EXECUTABLE
      Capability: TransferFunds
09:01  AUTHORIZED
      Trust: Permit
09:02  EXECUTING
      Action: Transfer
09:02  COMPLETED
      Outcome: FundsTransferred

This provides a complete semantic history.

⸻

52. Lifecycle and Observability

The lifecycle gives Noema a common vocabulary for operational metrics.

Examples:

clarification_rate
resolution_latency
authorization_latency
execution_latency
completion_rate
failure_rate
policy_block_rate
average_retries
partial_completion_rate

These metrics can reveal where the system is failing:

Interpretation
Resolution
Trust
Execution
Outcome

rather than treating everything as “agent failure.”

⸻

53. Lifecycle and Human Experience

The lifecycle should also determine what the Actor sees.

For example:

AMBIGUOUS
→ "Which account do you mean?"
POLICY_BLOCKED
→ "This requires manager approval."
EXECUTING
→ "I'm processing that now."
COMPLETED
→ "Your card has been renewed."
FAILED
→ "The renewal could not be completed because the card provider is unavailable."

The user-facing experience is therefore a projection of the underlying Intent State.

⸻

54. Lifecycle and Noema’s Core Thesis

The lifecycle reinforces one of Noema’s central architectural claims:

Noema owns Intent State, not Business State.

Noema is responsible for knowing:

what was requested
what was understood
what remains ambiguous
what was clarified
what is executable
what was authorized
what was attempted
what Outcome was observed

The external system remains authoritative for:

accounts
payments
cards
customers
orders
inventory

and other business-domain State.

⸻

55. Final Lifecycle Model

The canonical conceptual model is:

                    HUMAN EXPRESSION
                           │
                           ▼
                       EXPRESSED
                           │
                           ▼
                      INTERPRETED
                           │
                           ▼
                       GROUNDED
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                AMBIGUOUS       RESOLVED
                    │             │
                    ▼             ▼
              CLARIFICATION   EXECUTABLE
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                      AUTHORIZED
                           │
                           ▼
                       EXECUTING
                           │
                 ┌─────────┼─────────┐
                 ▼         ▼         ▼
             COMPLETED   FAILED   PARTIAL

With terminal alternatives:

INVALID
UNSUPPORTED
REJECTED
POLICY_BLOCKED
CANCELLED
EXPIRED
SUPERSEDED

⸻

56. Final Definition

The Intent Lifecycle is the canonical state machine governing an Intent from human expression through interpretation, grounding, resolution, authorization, execution, and verified Outcome, while explicitly representing ambiguity, clarification, rejection, failure, cancellation, expiration, and partial completion.

The shortest canonical formulation is:

An Intent is not merely received and executed; it progresses through a governed semantic lifecycle whose state determines what Noema knows, what remains unresolved, what may happen next, and whether the Actor’s intended Outcome has actually been achieved.