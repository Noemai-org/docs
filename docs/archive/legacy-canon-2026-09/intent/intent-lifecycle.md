> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Lifecycle

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-lifecycle.md

⸻

1. Definition

The Intent Lifecycle defines the canonical semantic and control states through which an Intent progresses from initial Actor expression through interpretation, grounding, resolution, Executable Intent, Trust evaluation, execution, verification, and final Outcome.

An Intent is not a single event.

It is a persistent semantic object whose lifecycle records how Noema interprets, resolves, governs, executes, and verifies the Actor’s request.

The lifecycle therefore answers:

What is the current state of this Intent,
what has been established,
what remains unresolved,
and what conditions are required
before it can transition?

The lifecycle state must not be confused with the semantic meaning of the Intent or with the State of an external business Resource.

⸻

2. Why the Intent Lifecycle Exists

A naive agent architecture often treats a request as:

Actor Request
     ↓
Model
     ↓
Tool Call
     ↓
Result

This collapses fundamentally different semantic and execution states into one operation.

Noema instead recognizes distinct stages:

Expression
    ↓
Interpretation
    ↓
Grounding
    ↓
Resolution
    ↓
Executable Intent
    ↓
Trust
    ↓
Execution
    ↓
Verification
    ↓
Outcome

Each stage answers a different question.

The lifecycle makes those distinctions explicit and auditable.

⸻

3. The Core Lifecycle

The canonical conceptual lifecycle is:

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
TRUST_PENDING
    ↓
ACTION
    ↓
EXECUTION
    ↓
VERIFICATION
    ↓
OUTCOME

The lifecycle may branch into states such as:

INTERPRETED
    ├── MATERIAL_AMBIGUITY
    │       ↓
    │   CLARIFICATION_REQUIRED
    │       ↓
    │   RESOLVING
    │
    ├── INVALID
    └── GROUNDED
RESOLVED
    ├── EXECUTABLE
    ├── CLARIFICATION_REQUIRED
    ├── ESCALATION_REQUIRED
    └── REJECTED
TRUST
    ├── EXECUTE
    ├── CLARIFY
    ├── ESCALATE
    └── REJECT
EXECUTION
    ├── EXECUTING
    ├── UNKNOWN
    ├── FAILED
    └── VERIFICATION
VERIFICATION
    ├── OUTCOME_ESTABLISHED
    ├── OUTCOME_UNKNOWN
    └── RECOVERY / RE-EVALUATION

The exact persistent state model may evolve, but the semantic distinctions must remain.

⸻

4. Intent Identity Persists Across the Lifecycle

An Intent retains its identity across lifecycle state transitions.

Conceptually:

Intent#123:v1

may progress through:

EXPRESSED
→ INTERPRETED
→ GROUNDED
→ RESOLVED
→ EXECUTABLE
→ TRUST_PENDING
→ EXECUTING
→ VERIFIED

A state transition does not create a new semantic Intent.

This enables:

* auditability
* traceability
* re-evaluation
* clarification
* retry
* cancellation
* causal explanation

A material semantic modification creates a new Intent version rather than silently changing the existing version.

⸻

5. Lifecycle State vs Intent Meaning

Intent meaning and lifecycle state are distinct.

For example:

Intent:
    RenewCard(Card#123)
Lifecycle State:
    AMBIGUOUS

The Intent exists.

Its semantic representation is not sufficiently resolved for execution.

Therefore:

Intent Meaning
    ≠
Intent Lifecycle State

Likewise:

Intent State:
    EXECUTING
Business State:
    Card = EXPIRED

These are different state systems.

⸻

6. EXPRESSED

Definition

EXPRESSED means an Actor has communicated an expression that may constitute an Intent, but Noema has not yet established its canonical semantic representation.

Example:

"Can you sort out my card?"

At this point Noema may have:

Actor:
    known
Expression:
    "Can you sort out my card?"
Canonical Intent:
    not yet established

The expression is evidence from which an Intent candidate may be constructed.

Expression is not itself executable authority.

⸻

7. INTERPRETED

Definition

INTERPRETED means Noema has constructed one or more candidate semantic representations from the Actor’s expression.

Example:

Intent:
    ResolveCardIssue
Actor:
    User#123
Resource:
    unresolved
Expected Outcome:
    CardIssueResolved

The interpretation may still contain unresolved or competing semantic fields.

Interpretation is not authorization.

Model output is not canonical merely because it has been generated.

The candidate representation must pass hard schema validation and admission before becoming a canonical admitted Intent version.

⸻

8. ADMITTED

Definition

ADMITTED means a candidate Intent representation has passed the required hard schema validation and has been admitted as a canonical Intent version.

Admission establishes structural validity.

It does not establish that:

* all semantic references are resolved
* the Intent is executable
* the Actor is authorized
* the requested Action is permitted
* the Outcome will succeed

Conceptually:

Interpretation
      ↓
Hard Schema Validation
      ↓
ADMITTED Intent Version

An admitted Intent version is immutable.

Material semantic changes produce a new version with supersedes.

⸻

9. GROUNDED

Definition

GROUNDED means material semantic references in the Intent have been connected to canonical concepts, Entities, Resources, Context, relationships, or relevant evidence.

Example:

Expression:
    "Renew the card I used yesterday."
Grounding:
    "card I used yesterday"
            ↓
    Transaction#981
            ↓
    Card#123

The Intent may then contain:

RenewCard(Card#123)

Grounding reduces unresolved reference ambiguity.

Grounding does not automatically establish that every fact is authoritative.

Relevant evidence must be evaluated for authority, scope, freshness, and Fact Status.

⸻

10. AMBIGUOUS

Definition

AMBIGUOUS means Noema has identified multiple materially valid interpretations and insufficient evidence to determine which one the Actor intended.

Example:

Intent:
    CancelSubscription
Candidate Resources:
    Subscription#123
    Subscription#456

Noema must not arbitrarily choose one.

Model confidence may rank candidates, but it does not resolve material ambiguity by itself.

Material ambiguity prevents the Intent from becoming Executable Intent until resolved.

⸻

11. CLARIFICATION_REQUIRED

Definition

CLARIFICATION_REQUIRED means a material semantic gap prevents safe resolution and requires additional information from the Actor or an authoritative source.

Example:

Intent:
    TransferFunds
Amount:
    $500
Destination:
    UNKNOWN

Noema may ask:

Which account should receive the $500?

The clarification should target the unresolved semantic field rather than require the Actor to restate the entire request.

CLARIFICATION_REQUIRED is a lifecycle/resolution state.

It is distinct from the Trust outcome CLARIFY.

⸻

12. CLARIFICATION

Clarification is a resolution activity, not simply a terminal lifecycle state.

Conceptually:

AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED
    ↓
Actor Response
    ↓
VALIDATE / INTERPRET
    ↓
RESOLVE

A single Intent may require multiple clarification cycles.

Where a clarification materially changes the semantic meaning of an admitted Intent, the resulting representation becomes a new Intent version.

Noema must preserve the prior version and the clarification provenance.

⸻

13. RESOLVING

RESOLVING represents the active semantic resolution process.

Resolution may use:

* explicit Actor references
* validated Context
* authoritative enterprise data
* State Reconciliation
* relationships
* deterministic rules
* Actor clarification
* evidence and provenance

The objective is to establish what the Actor means, not to determine whether execution is permitted.

Resolution must not silently manufacture missing semantics.

If a material ambiguity remains, the Intent returns to CLARIFICATION_REQUIRED, ESCALATE, or another explicitly defined control state as appropriate.

⸻

14. RESOLVED

Definition

RESOLVED means Noema has established a sufficiently complete and unambiguous semantic representation of the Intent.

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

Resolved does not mean:

* executable
* authorized
* executed
* successful

Trust and execution requirements remain separate.

⸻

15. VALIDATION

A resolved Intent must satisfy the applicable semantic and structural validation requirements before becoming Executable Intent.

Validation can establish:

* required fields exist
* types are correct
* references are valid
* constraints are coherent
* relationships are valid
* scope is valid
* the semantic structure conforms to the canonical ontology

Validation may be an internal transition rather than a persistent lifecycle state.

The distinction remains architecturally important:

Resolved
    ↓
Validation
    ↓
Executable Intent

Hard schema validation also exists earlier at Intent admission. These are distinct validation purposes and must not be conflated.

⸻

16. EXECUTABLE

Definition

EXECUTABLE means the Intent has become an Executable Intent: its material semantic requirements are sufficiently established for deterministic Trust evaluation and potential execution as one or more bounded Actions.

Example:

Intent:
    RenewCard(Card#123)
Required semantic information:
    resolved
Relevant Capability:
    available
Constraints:
    validated

Executable Intent does not mean:

authorized

and does not mean:

successful

Trust remains the authority boundary before consequential execution.

⸻

17. TRUST_PENDING

TRUST_PENDING means an Executable Intent is awaiting the applicable deterministic Trust evaluation.

Trust evaluates the resolved semantic request against relevant:

* Policy
* Authority
* current State
* Constraints
* Capability availability
* governance conditions
* Action and execution requirements

Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

EXECUTE means the resolved path satisfies the applicable Trust conditions and may proceed.

It does not mean the Action has succeeded.

⸻

18. TRUST OUTCOME: EXECUTE

EXECUTE is a Trust decision indicating that the resolved Intent satisfies the applicable conditions for proceeding.

Conceptually:

Executable Intent
      ↓
Trust
      ↓
EXECUTE
      ↓
Action

The distinction is important:

EXECUTE
    ≠
Execution succeeded

Execution still requires Action invocation, execution-state tracking, verification, and Outcome determination.

⸻

19. TRUST OUTCOME: CLARIFY

CLARIFY is a Trust outcome indicating that Noema cannot safely make the required decision without additional information or clarification.

This may occur when a material issue remains unresolved at the Trust boundary.

CLARIFY should not be confused with the Intent resolution mechanism itself.

Conceptually:

Trust
  ↓
CLARIFY
  ↓
Clarification / Resolution
  ↓
New or updated Intent version
  ↓
Trust re-evaluation

Clarification does not grant authority.

⸻

20. TRUST OUTCOME: ESCALATE

ESCALATE is a Trust outcome indicating that Noema cannot safely resolve the decision autonomously and requires an authorized human or organizational process.

Examples may include:

* unresolved authority
* conflicting authoritative evidence
* governance conditions requiring human review
* exceptional policy conditions

Escalation is not equivalent to failure.

The reason and required escalation path must be recorded.

⸻

21. TRUST OUTCOME: REJECT

REJECT is a Trust outcome indicating that the resolved Intent must not proceed.

Possible causes include:

* prohibited capability
* insufficient authority
* policy violation
* unsupported execution path
* invalid Trust conditions
* explicit governance prohibition

The rejection reason must be recorded.

REJECT is distinct from execution failure.

⸻

22. POLICY BLOCKED

POLICY_BLOCKED may be represented as a reason or control state associated with a Trust decision rather than as a fifth Trust outcome.

For example:

Intent:
    RefundPayment($50,000)
Policy:
    Amounts > $10,000 require approval

Trust may produce:

ESCALATE

with reason:

APPROVAL_REQUIRED

or:

REJECT

if Policy explicitly prohibits the operation.

This preserves the canonical four Trust outcomes without collapsing governance reasons into the outcome enumeration.

⸻

23. EXECUTING

Definition

EXECUTING means one or more bounded Actions associated with the Intent are currently being performed.

Example:

Intent:
    RenewCard
State:
    EXECUTING
Actions:
    VerifyEligibility
    RenewCard

Execution state must not be confused with Intent meaning.

The Intent remains:

RenewCard

regardless of which Action is currently running.

⸻

24. UNKNOWN

UNKNOWN is a first-class epistemic or execution state.

For example:

Action submitted
    ↓
Provider timeout
    ↓
Actual external state unknown

A timeout must not automatically become:

FAILED

nor:

COMPLETED

Noema must verify external state before retrying an operation where duplicate execution is consequential.

Unknown may therefore trigger:

Verification
    ↓
State Reconciliation
    ↓
Recovery / Retry / Escalation

The exact representation may be execution-specific, but the distinction must remain.

⸻

25. COMPLETED / OUTCOME SATISFIED

An Intent reaches its terminal successful state only when its Expected Outcome has been satisfied according to applicable semantic and verification criteria.

Example:

Intent:
    RenewCard
Expected Outcome:
    CardActive
Observed State:
    CardActive
Verification:
    Confirmed

Therefore:

COMPLETED

means the Intent’s expected semantic Outcome has been established.

A successful API response alone is insufficient.

⸻

26. FAILED

FAILED means execution and recovery have not established the expected Outcome and the Intent cannot currently proceed automatically.

Example:

Intent:
    RenewCard
Action:
    CreateReplacementCard
Result:
    Provider unavailable

The failure record should preserve:

* cause
* Actions attempted
* execution attempts
* observed State
* verification results
* relevant evidence
* recovery actions

An individual Action failure does not necessarily make the Intent permanently failed.

⸻

27. PARTIALLY_COMPLETED

A Composite Intent may be partially satisfied.

Example:

Composite:
    TransferBalance + CloseAccount
TransferBalance:
    COMPLETED
CloseAccount:
    FAILED

The composite must preserve the constituent states.

A parent-level partial state is appropriate only where the composition semantics permit a partially satisfied composite.

The parent must not be represented simply as FAILED if doing so would erase material child Outcome information.

⸻

28. CANCELLED

CANCELLED means the Actor or an authorized control mechanism has withdrawn the Intent before successful completion, subject to whether cancellation remains possible.

Example:

Intent:
    BookFlight
Control:
    CANCELLED

Cancellation is a control state, not a Trust outcome.

Cancellation must not silently mutate the semantic meaning of an immutable admitted Intent version.

If cancellation materially changes the semantic lifecycle representation, the control event and relevant version relationships must be preserved.

⸻

29. EXPIRED

EXPIRED means the Intent can no longer be meaningfully satisfied within its defined temporal validity.

Example:

Intent:
    BookFlight
Constraint:
    DepartToday
Current Time:
    After departure

The Intent may become:

EXPIRED

rather than FAILED.

The distinction matters because expiration reflects loss of temporal validity rather than necessarily an execution failure.

⸻

30. SUPERSEDED

An Intent version may be superseded by a newer version.

Example:

Intent#123:v1
    BookFlight(Monday)
Intent#123:v2
    BookFlight(Tuesday)
    supersedes = Intent#123:v1

The prior version remains part of the historical record.

SUPERSEDED is a version/control relationship, not a Trust outcome.

An older version must not silently continue to execute after it has been superseded where the superseding change invalidates its authority or semantic applicability.

⸻

31. INVALID

INVALID means the candidate representation violates the semantic or structural requirements of the Intent Language or applicable ontology.

Examples:

TransferFunds
Amount:
    "banana"

or:

TransferFunds
Source:
    Account#123
Destination:
    Account#123
Domain Constraint:
    Source != Destination

Invalidity is distinct from ambiguity.

Ambiguity means multiple materially valid interpretations remain.

Invalidity means the represented interpretation is not valid under the applicable semantic rules.

⸻

32. UNSUPPORTED

An Intent may be semantically clear but lack an available bounded Capability capable of satisfying it.

Example:

"Teleport me to London."
Intent:
    TeleportPerson
Capability:
    unavailable

The meaning may be clear.

The system simply has no supported execution path.

Unsupported capability should not be confused with Trust rejection or execution failure.

⸻

33. State Transition Rules

Transitions should be governed by explicit conditions.

Conceptually:

EXPRESSED
    → INTERPRETED

when a candidate semantic representation has been constructed.

INTERPRETED
    → ADMITTED

when hard schema validation succeeds.

ADMITTED
    → GROUNDED / RESOLVING

when semantic resolution begins.

RESOLVING
    → AMBIGUOUS

when multiple materially valid interpretations remain.

AMBIGUOUS
    → CLARIFICATION_REQUIRED

when additional semantic information is required.

RESOLVING
    → RESOLVED

when material semantic ambiguity has been eliminated.

RESOLVED
    → EXECUTABLE

when the material requirements for Executable Intent are satisfied.

EXECUTABLE
    → TRUST_PENDING

when the Intent is ready for Trust evaluation.

TRUST_PENDING
    → EXECUTE

when applicable Trust conditions are satisfied.

TRUST_PENDING
    → CLARIFY / ESCALATE / REJECT

when the corresponding Trust condition applies.

EXECUTE
    → EXECUTING

when a bounded Action begins.

EXECUTING
    → VERIFICATION

when an Action attempt reaches a state requiring Outcome verification.

VERIFICATION
    → COMPLETED

when the Expected Outcome is verified.

Other terminal or control states may be entered where their explicit conditions apply.

⸻

34. No Silent State Transitions

Noema must not silently move an Intent from:

AMBIGUOUS

to:

RESOLVED

because a Model produced a more confident guess.

A material semantic transition requires evidence sufficient for the relevant transition.

Likewise, Noema must not silently convert:

UNKNOWN

to:

FAILED

or:

COMPLETED

without appropriate verification.

⸻

35. Model Confidence Does Not Define Lifecycle State

Suppose the Model produces:

Confidence:
    0.97

for:

CancelSubscription(Subscription#123)

If:

Subscription#123
Subscription#456

remain materially valid candidates, the Intent remains ambiguous.

Confidence is interpretation metadata.

It is not:

* lifecycle authority
* semantic resolution
* Fact Status
* authorization
* Trust
* Outcome

⸻

36. Evidence-Driven Transitions

Lifecycle transitions should be supported by evidence appropriate to the transition.

Examples:

AMBIGUOUS
      ↓
Actor clarification
      ↓
RESOLVED

or:

GROUNDED
      ↓
Authoritative enterprise lookup
      ↓
RESOLVED

or:

EXECUTABLE
      ↓
Trust evaluation
      ↓
REJECT

or:

EXECUTING
      ↓
External state reconciliation
      ↓
VERIFIED OUTCOME

The evidence supporting a material transition should be auditable.

⸻

37. Lifecycle and Provenance

Every material state transition should record, where applicable:

* previous state
* new state
* timestamp
* responsible Actor or system
* reason
* evidence references
* Intent version
* relevant Policy or Contract version

Example:

Intent#123:v1
AMBIGUOUS → RESOLVED
Reason:
    Actor clarified destination account.
Evidence:
    ConversationTurn#42

This creates an auditable semantic history without requiring disclosure of private Model chain-of-thought.

⸻

38. Lifecycle and Clarification Loops

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
RESOLVING
    ↓
AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED
    ↓
Actor response
    ↓
RESOLVED

Noema must support multiple clarification rounds without losing prior semantic state or provenance.

Each material clarification should be associated with the relevant Intent version.

⸻

39. Lifecycle and Intent Modification

An Actor may modify an Intent.

Example:

"Book the flight for Friday."
then:
"Actually, make it Saturday."

The canonical model should not silently mutate the already-admitted Intent version.

Instead:

Intent#123:v1
    BookFlight(Friday)
Intent#123:v2
    BookFlight(Saturday)
    supersedes = Intent#123:v1

The current version represents the current semantic Intent.

Historical versions remain immutable.

⸻

40. Intent Versioning

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

A version change is required when semantic meaning materially changes.

Versioning preserves:

* prior meaning
* provenance
* clarification history
* Trust decisions
* execution history
* supersession relationships

This prevents historical execution records from being reinterpreted under a later semantic version.

⸻

41. Lifecycle and Composite Intents

Composite Intents require both:

composite lifecycle state

and:

constituent Intent states

Example:

Composite:
    EmployeeOffboarding
Children:
    RevokeGitHub      COMPLETED
    DisableEmail      EXECUTING
    NotifyManager     RESOLVED

The composite state must be derived from explicit composition semantics.

A parent state does not automatically authorize, execute, or complete its children.

Each consequential child remains subject to its own semantic resolution, Trust, Action, execution, and verification requirements.

⸻

42. Lifecycle and Independent Children

A child Intent may resolve independently of another child.

Example:

Composite:
    UpdateProfile
Children:
    UpdateAddress       RESOLVED
    UpdatePhone         AMBIGUOUS
    UpdatePreferences   RESOLVED

Noema should not discard resolved semantic information merely because another child requires clarification.

A child may proceed independently only when:

* the composition semantics permit it
* its own material requirements are resolved
* its own Trust conditions are satisfied
* proceeding does not violate a dependency or shared Constraint

⸻

43. Lifecycle and Parent Completion

A Composite Intent should reach successful completion only when its defined Outcome semantics are satisfied.

For example:

TransferBalance
CloseAccount

If both are required:

TransferBalance = COMPLETED
CloseAccount    = COMPLETED
Parent          = COMPLETED

If:

TransferBalance = COMPLETED
CloseAccount    = FAILED

then the parent cannot be marked COMPLETED unless the composition semantics explicitly define another satisfaction criterion.

Child Outcomes must remain individually auditable.

⸻

44. Lifecycle and Action Retry

An Action may fail while the Intent remains active.

Example:

Intent:
    SendInvoice
Action Attempt #1:
    FAILED
Action Attempt #2:
    SUCCESS
Verified Outcome:
    InvoiceSent

The Intent lifecycle need not become permanently failed because one Action attempt failed.

Therefore:

Action State
    ≠
Intent State

Retry remains bounded by idempotency, Action Contracts, current State, Trust conditions, and verification requirements.

⸻

45. Lifecycle and Execution Attempts

An Intent may have multiple execution attempts.

Conceptually:

Intent#123
Attempt#1
    Action → FAILED
Verification / Recovery
    ↓
Attempt#2
    Action → EXECUTE
    ↓
    VERIFIED
Intent
    → COMPLETED

The lifecycle must preserve the distinction between:

attempt failure

and:

Intent failure

Retries must not assume that an uncertain external operation failed.

External State should be verified before retrying when duplicate execution is consequential.

⸻

46. Lifecycle and Compensation

If an executed Action requires compensation, the Intent lifecycle may remain active while compensation occurs.

Example:

ChargeCustomer
      ↓
ProvisionService
      ↓
Provisioning fails
      ↓
Compensation Action
      ↓
RefundCustomer

Compensation is an execution concern.

Intent Composition and Lifecycle record the semantic dependency and resulting Outcomes but do not imply that every Action is transactionally reversible.

The final Intent state depends on its Expected Outcome and verified resulting State.

⸻

47. Lifecycle and External State

Intent lifecycle must not be confused with business-domain State.

Example:

Noema:
    Intent#123 = EXECUTING
Enterprise:
    Card#456 = EXPIRED

After execution and verification:

Noema:
    Intent#123 = COMPLETED
Enterprise:
    Card#456 = ACTIVE

The systems are related.

They are not the same State model.

The enterprise remains authoritative for relevant business State.

⸻

48. Lifecycle and Outcome Verification

An Action returning success does not necessarily mean the Intent is complete.

Example:

Action:
    UpdateDatabase
Action Result:
    Success
Expected Outcome:
    Customer can log in

If login remains impossible, the Intent is not completed.

Therefore:

Action Success
    ≠
Intent Completion

Completion requires verified satisfaction of the Expected Outcome.

⸻

49. Lifecycle and Determinism

Noema should maintain deterministic rules for lifecycle transitions wherever possible.

Examples:

required material resource unresolved
    → CLARIFICATION_REQUIRED
Trust condition requires additional information
    → CLARIFY
policy requires authorized human review
    → ESCALATE
policy or governance prohibits execution
    → REJECT
verified Expected Outcome
    → COMPLETED
external execution state unknown
    → UNKNOWN / VERIFICATION

The Model may assist with interpretation and candidate generation.

It must not arbitrarily determine lifecycle transitions that have deterministic semantic criteria.

⸻

50. Lifecycle and the Trust Boundary

The lifecycle preserves the architectural separation:

Model:
    What might the Actor mean?
Intent Resolution:
    What does the Actor mean after grounding and reconciliation?
Executable Intent:
    Is the semantic representation sufficiently complete
    for deterministic Trust evaluation?
Trust:
    May this resolved Intent proceed?
Execution:
    Perform the permitted Action.
Verification:
    What actually happened?
Outcome:
    Was the Actor's expected semantic state achieved?

This separation prevents probabilistic interpretation from directly invoking consequential enterprise Actions.

⸻

51. Lifecycle and Business State

Noema owns the lifecycle state of Intent.

The enterprise system owns authoritative Business State.

For example:

Noema:
    Intent#123 = EXECUTING
Enterprise:
    Account#456 = OPEN

After successful execution:

Noema:
    Intent#123 = COMPLETED
Enterprise:
    Account#456 = CLOSED

Noema may observe, reconcile, and reason over Business State.

It does not become the authoritative owner of that external state merely by representing it in Context or State Reconciliation.

⸻

52. Terminal States and Control States

A terminal state is a state from which the current Intent version cannot normally continue.

Conceptual terminal outcomes include:

COMPLETED
FAILED
REJECTED
CANCELLED
EXPIRED
UNSUPPORTED
INVALID
SUPERSEDED

However, terminality is contextual.

A failed execution may lead to recovery and another bounded attempt before the Intent becomes terminal.

A superseded version may remain historically terminal even while a newer version continues.

A new Intent version may be created where the Actor changes the request.

No terminal state should silently reopen itself.

⸻

53. Non-Terminal States

Typical non-terminal semantic or control states include:

EXPRESSED
INTERPRETED
ADMITTED
GROUNDED
RESOLVING
AMBIGUOUS
CLARIFICATION_REQUIRED
RESOLVED
EXECUTABLE
TRUST_PENDING
EXECUTING
VERIFICATION
UNKNOWN
PARTIALLY_COMPLETED

The exact persistence model may evolve.

The semantic distinctions must remain explicit.

⸻

54. Canonical State Model

                         ┌────────────────────┐
                         │ MATERIAL AMBIGUITY │
                         └──────────┬─────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │ CLARIFICATION_REQ. │
                         └──────────┬─────────┘
                                    │
                                    ▼
                              RESOLVING
                                    │
                                    ▼
┌───────────┐   ┌─────────────┐   ┌───────────┐
│ EXPRESSED ├─► │ INTERPRETED ├─► │  ADMITTED │
└───────────┘   └─────────────┘   └─────┬─────┘
                                        │
                                        ▼
                                   GROUNDED
                                        │
                                        ▼
                                   RESOLVED
                                        │
                                        ▼
                                  EXECUTABLE
                                        │
                                        ▼
                                 TRUST_PENDING
                                        │
                   ┌────────────────────┼────────────────────┐
                   ▼                    ▼                    ▼
                EXECUTE               CLARIFY             ESCALATE
                   │                    │                    │
                   ▼                    └──► RESOLVING       │
               EXECUTING                                      │
                   │                                          │
                   ▼                                          │
              VERIFICATION                                    │
                   │                                          │
            ┌──────┼──────┐                                   │
            ▼      ▼      ▼                                   ▼
        COMPLETED UNKNOWN FAILED                            REJECTED
Other lifecycle/control states:
    INVALID
    UNSUPPORTED
    CANCELLED
    EXPIRED
    SUPERSEDED
    PARTIALLY_COMPLETED

Trust outcomes remain exactly:

EXECUTE
CLARIFY
ESCALATE
REJECT

They should not be expanded to include execution outcomes such as SUCCESS or FAILED.

⸻

55. Canonical Transition Rules

Rule 1 — Every Admitted Intent Version Has Identity

State changes do not create a new identity.

Material semantic changes create a new version.

Rule 2 — State Must Be Explicit

Noema must maintain an explicit lifecycle/control state for every active Intent version.

Rule 3 — Material Ambiguity Blocks Executability

An unresolved material ambiguity must not be silently guessed through execution.

Rule 4 — Resolution Precedes Executability

An Intent cannot become Executable Intent while material semantic requirements remain unresolved.

Rule 5 — Executability Does Not Imply Authorization

Capability availability does not grant permission.

Rule 6 — Trust Precedes Consequential Execution

A consequential Action must not execute unless the applicable Trust decision permits it.

Rule 7 — Trust EXECUTE Does Not Mean Success

EXECUTE permits the resolved path to proceed.

It does not establish an Outcome.

Rule 8 — Action Success Does Not Equal Intent Completion

Completion requires verified satisfaction of the Expected Outcome.

Rule 9 — Unknown Is Not Failure

An uncertain external execution state must not be converted into failure without verification.

Rule 10 — Partial Completion Must Be Representable

Composite Intents must preserve individual child states and Outcomes.

Rule 11 — Child Authority Is Independent

A child Intent does not inherit authorization merely because its parent or another child was authorized.

Rule 12 — Terminal States Require Explicit Re-entry or New Version

Completed, cancelled, rejected, expired, or superseded Intent versions must not silently resume.

Rule 13 — State Transitions Must Be Auditable

Material transitions should retain reason, provenance, and relevant evidence.

Rule 14 — Business State Remains External Authority

Intent lifecycle state must not replace authoritative enterprise Business State.

⸻

56. Lifecycle Invariants

Invariant 1

AMBIGUOUS → EXECUTING

is invalid.

Invariant 2

UNRESOLVED → TRUST EXECUTE

is invalid.

Invariant 3

EXECUTABLE → TRUST EXECUTE

requires applicable deterministic Trust evaluation.

Invariant 4

TRUST EXECUTE → CONSEQUENTIAL ACTION

requires the relevant execution controls and Action Contract.

Invariant 5

EXECUTING → COMPLETED

requires verified Expected Outcome satisfaction.

Invariant 6

UNKNOWN → RETRY

is invalid without the applicable verification and idempotency controls.

Invariant 7

A child Intent cannot inherit Trust authorization from a parent.

Invariant 8

An admitted Intent version cannot silently change semantic meaning.

Invariant 9

Lifecycle state cannot establish Business State.

Invariant 10

A later Intent version cannot retroactively rewrite the semantic meaning of an earlier version.

⸻

57. Lifecycle and Audit Trail

A canonical audit record might look like:

Intent#123:v1
09:00  EXPRESSED
       Source: User
09:00  INTERPRETED
       Objective: TransferFunds
09:00  ADMITTED
       Schema: Valid
09:01  GROUNDED
       Destination: Savings#456
09:01  RESOLVED
       Evidence: User clarification
09:01  EXECUTABLE
       Required semantics: Complete
09:01  TRUST
       Decision: EXECUTE
09:02  EXECUTING
       Action: Transfer
09:02  VERIFICATION
       Evidence: Ledger reconciliation
09:02  COMPLETED
       Outcome: FundsTransferred

This provides a causal semantic history from expression through verified Outcome.

⸻

58. Lifecycle and Observability

The lifecycle provides Noema with a common vocabulary for operational metrics.

Examples include:

clarification_rate
resolution_latency
trust_latency
execution_latency
verification_latency
completion_rate
failure_rate
escalation_rate
rejection_rate
average_retries
partial_completion_rate
unknown_rate

These metrics help identify where the system is failing:

Interpretation
Resolution
Trust
Execution
Verification
Outcome

rather than treating every failure as generic “agent failure.”

⸻

59. Lifecycle and Human Experience

The lifecycle should determine what the Actor sees without exposing internal implementation details.

Examples:

CLARIFICATION_REQUIRED
→ "Which account do you mean?"
TRUST / ESCALATE
→ "This requires additional review."
EXECUTING
→ "I'm processing that now."
COMPLETED
→ "Your card has been renewed."
FAILED
→ "The renewal could not be completed because the card provider is unavailable."
UNKNOWN
→ "I can't yet confirm the final status. I'm checking the transaction state."

The user-facing experience is therefore a projection of relevant Intent and execution state.

The interface should communicate material state without exposing private Model reasoning.

⸻

60. Lifecycle and Noema’s Core Thesis

The lifecycle reinforces one of Noema’s central architectural claims:

Noema owns Intent State.
Enterprise systems own Business State.

Noema is responsible for knowing:

* what was expressed
* what was interpreted
* what was admitted
* what was grounded
* what remains ambiguous
* what was clarified
* what was resolved
* what became Executable Intent
* what Trust decided
* what Actions were attempted
* what was verified
* what Outcome was established

The enterprise remains authoritative for:

* accounts
* payments
* cards
* customers
* orders
* inventory
* balances
* ledgers
* transaction state

and other business-domain State.

⸻

61. Final Lifecycle Model

The canonical conceptual model is:

                    ACTOR EXPRESSION
                           │
                           ▼
                       EXPRESSED
                           │
                           ▼
                      INTERPRETED
                           │
                           ▼
                       ADMITTED
                           │
                           ▼
                  GROUNDED / RESOLVING
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                AMBIGUOUS      RESOLVED
                    │             │
                    ▼             ▼
        CLARIFICATION_REQUIRED  EXECUTABLE
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                     TRUST PENDING
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           EXECUTE       CLARIFY     ESCALATE
              │            │            │
              ▼            │            │
          EXECUTING        │            │
              │            │            │
              ▼            │            ▼
         VERIFICATION      │         REJECT
              │            │
        ┌─────┼─────┐      │
        ▼     ▼     ▼      │
    COMPLETED UNKNOWN FAILED

With independent control and terminal states:

INVALID
UNSUPPORTED
CANCELLED
EXPIRED
SUPERSEDED
PARTIALLY_COMPLETED

The lifecycle is not merely a pipeline.

It is a governed state machine connecting semantic interpretation, resolution, Trust, bounded execution, verification, and Outcome.

⸻

62. Final Definition

The Intent Lifecycle is the canonical state machine governing an Intent from Actor expression through interpretation, admission, grounding, resolution, Executable Intent, Trust evaluation, bounded execution, verification, and Outcome, while explicitly representing ambiguity, clarification, rejection, escalation, failure, uncertainty, cancellation, expiration, supersession, and partial completion.

The shortest canonical formulation is:

An Intent is not merely received and executed.
It progresses through a governed semantic lifecycle
whose state records what Noema has established,
what remains unresolved, what may happen next,
what Trust permits, what execution has established,
and whether the Actor's intended Outcome
has actually been achieved.