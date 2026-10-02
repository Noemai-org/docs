Principles

Status: Foundational
Version: 0.2
Domain: Thesis
Canonical Path: thesis/principles.md

⸻

1. Purpose

This document defines the principles that govern the design, architecture, and evolution of Noema.

These are not implementation preferences.

They are the architectural invariants behind the Noema thesis.

When architectural decisions conflict, these principles should be used to determine which direction is consistent with Noema as Trusted Enterprise Execution Infrastructure.

The principles also establish boundaries between:

* probabilistic interpretation and deterministic execution
* Intent and Action
* capability and authority
* evidence and inference
* state and outcome
* enterprise business state and Noema execution state
* possibility and legitimacy
* execution attempt and verified result

⸻

2. Intent Is the Primary Abstraction

Noema is fundamentally an Intent system.

The central question is not:

What tool should the Model call?

It is:

What does the source of Intent intend to accomplish?

The system therefore begins with:

Source of Intent
      ↓
Intent

rather than:

Actor
      ↓
Tool Call

Tools, APIs, capabilities, and Actions are mechanisms downstream of Intent.

⸻

3. Intent Must Be Separated From Execution

An Intent is not an Action.

Intent:
"Renew my card."
Action:
RenewCard(...)

The same Intent may be fulfilled through different Actions depending on:

* Capability
* Resource
* Context
* State
* Policy
* Constraint
* Authority
* available enterprise systems

Therefore:

Intent describes desired meaning; Action describes executable behavior.

⸻

4. The Model May Interpret, but Noema Must Decide

Model inference is probabilistic.

Noema’s consequential execution boundary must be deterministic wherever correctness requires determinism.

The conceptual flow is:

Source of Intent
      ↓
Model / Inference
      ↓
Candidate Interpretation
      ↓
Typed Intent
      ↓
Schema Validation
      ↓
Deterministic Noema
      ↓
Trust
      ↓
Action

The Model proposes.

Noema determines what is valid, authorized, constrained, and executable.

Model confidence must never substitute for deterministic Trust.

⸻

5. Typed Semantics Must Cross a Hard Boundary

Free-form model output must not directly enter consequential execution.

The transition from probabilistic interpretation to deterministic execution must pass through an explicit, versioned, schema-validated representation.

Conceptually:

Probabilistic
────────────────────────
Natural Language
      ↓
Model Interpretation
      ↓
Candidate Intent
────────────────────────
Hard Schema Boundary
────────────────────────
Validated Intent
      ↓
Deterministic Resolution
      ↓
Trust
      ↓
Execution

This boundary is architectural, not merely an implementation convention.

⸻

6. Uncertainty Must Not Become an Execution Guess

When Noema cannot establish the required meaning or state, it must not silently guess.

The preferred progression is:

Insufficient certainty
        ↓
Clarify / Request Evidence / Escalate / Reject

not:

Insufficient certainty
        ↓
Best Guess
        ↓
Execute

This applies to:

* Actor identity
* Intent
* Entity
* Resource
* Capability
* Authority
* Policy applicability
* State
* Action parameters
* execution outcome

⸻

7. Unknown Is a First-Class State

Noema must distinguish:

KNOWN
FALSE
UNKNOWN

where the domain semantics require such a distinction.

Unknown is not equivalent to false.

If Noema cannot establish that an Actor is authorized, that does not automatically mean the Actor is unauthorized.

The authorization fact may simply be unknown.

Likewise:

Provider Timeout
      ↓
Outcome = UNKNOWN

does not mean:

Provider Timeout
      ↓
Outcome = FAILURE

Unknown must remain explicit until sufficient evidence establishes a more specific state.

⸻

8. Noema Must Preserve Fact Status

Facts used in consequential decisions must preserve their epistemic status.

A fact may be:

* KNOWN
* INFERRED
* AMBIGUOUS
* UNAVAILABLE
* STALE
* CONTRADICTORY
* UNKNOWN
* UNAUTHORIZED

These statuses are not interchangeable with model confidence.

A highly confident inference is still an inference.

An authoritative fact that is stale is still stale.

The system must preserve the distinction.

⸻

9. Noema Owns Intent and Execution-Domain State, Not Business State

Noema should maintain the state required to understand, govern, execute, verify, and explain Intent.

This includes state such as:

* Intent State
* Trust State
* Action State
* Execution State
* Verification State
* Outcome State
* provenance and execution history

Connected enterprise systems continue to own their domain-specific business state.

For example:

Bank
  → Account / Ledger / Transaction State
CRM
  → Customer State
ERP
  → Order / Inventory State
HRIS
  → Employee State

Noema may observe, resolve, reconcile, and act upon these states.

It does not automatically own them.

⸻

10. Canonical Meaning Must Be Explicit

Important semantic concepts must have canonical representations.

Natural language:

"my card"

should eventually resolve to something such as:

Resource:
Card#123

Likewise:

"renew it"

must resolve into canonical Intent and target semantics.

Noema should not depend on critical meaning remaining implicit inside prompts, conversation history, tool descriptions, or undocumented application conventions.

⸻

11. Ontology Before Automation

Noema should establish what a concept means before optimizing how it is executed.

The foundational vocabulary includes concepts such as:

* Actor
* Identity
* Intent
* Entity
* Resource
* Context
* Capability
* Action
* Policy
* Constraint
* Authority
* State
* Evidence
* Execution
* Outcome

Automation built on ambiguous semantics produces fragile systems.

⸻

12. Semantics Before Syntax

Noema should care more about:

What does this operation mean?

than:

How is this operation represented or transported?

REST, GraphQL, gRPC, MCP, SDKs, CLI commands, events, and other mechanisms may represent or trigger related semantic operations.

The canonical semantic model must remain independent of transport.

⸻

13. Actions Must Have Explicit Semantics

An Action should not merely be a function call.

It should describe a meaningful, governed operation against canonical objects.

Conceptually:

Action
├── Capability
├── Actor
├── Resource / Target
├── Parameters
├── Preconditions
├── Constraints
├── Authority
├── Policy Requirements
├── Execution Contract
└── Expected Outcome

An Action must be sufficiently explicit that its execution semantics are not dependent on hidden model reasoning.

⸻

14. Capability Describes Possibility

A Capability answers:

What can this enterprise-connected system accomplish?

It does not answer:

What should happen right now?

For example:

Capability:
refund_payment

does not imply:

Intent:
Refund this payment

Capability establishes technical or semantic possibility.

Intent establishes desired behavior.

⸻

15. Capability Is Not Permission

The existence of a Capability does not imply that an Actor is authorized to invoke it.

Capability:
delete_customer

is distinct from:

Authority:
SupportAgent may delete Customer

Therefore:

Capability ≠ Permission
Capability ≠ Authority

Noema must preserve these distinctions throughout resolution and execution.

⸻

16. Capability Is Not Eligibility

A Capability may exist without being applicable to the current execution.

For example:

Capability exists
        ≠
Capability is eligible

Eligibility may depend on:

* Actor
* Resource
* current State
* Context
* Policy
* Constraints
* authority
* enterprise configuration
* capability availability

Noema must distinguish existence, availability, eligibility, and authorization.

⸻

17. Authority Is Specific to the Intended Execution

Authority should not be treated as an abstract permission attached permanently to an Actor.

The relevant question is whether the Actor has appropriate authority for the specific intended operation against the specific target in the current context.

Conceptually:

Actor
+
Action
+
Target
+
Context
+
Current State
+
Authority

must be evaluated together.

Noema must not infer broad authority from narrow authorization evidence.

⸻

18. Technical Authorization, Policy Authorization, and Business Authorization Are Distinct

Authorization has multiple dimensions.

A system may establish:

Technical Authorization
→ Can this identity invoke this capability?
Policy Authorization
→ Do applicable policies permit this operation?
Business Authorization
→ Is this operation legitimate for this actor, target,
  state, and business context?

These dimensions may be supplied by different enterprise systems.

Noema should preserve the distinction rather than collapsing them into one generic permission flag.

⸻

19. Policy Is Separate From Authority

Authority determines whether an Actor has a relevant right or authorization.

Policy determines the governing conditions under which an operation may occur.

For example:

Authority:
Manager may approve refunds.
Policy:
Refunds above $10,000 require Finance approval.

Both may be necessary before execution.

Policy must also be evaluated against the applicable policy version and execution context.

⸻

20. Constraints Are First-Class

Constraints should not be hidden inside arbitrary application code or prompts when they materially affect execution.

Examples:

Transfer ≤ available balance
Refund ≤ original payment
Booking must occur before departure
Only one allocation at a time

Constraints should be inspectable, versionable where necessary, and deterministically evaluable.

⸻

21. State Is a Trust Input

Noema must reason about relevant current State before executing an Action.

Conceptually:

Intent
+
Context
+
Current State
+
Capability
+
Authority
+
Policy
+
Constraints
+
Evidence

must inform Trust and execution.

Example:

Intent:
Close account
Current State:
Account already closed

The correct behavior may be to recognize that the desired State is already satisfied rather than execute another operation.

⸻

22. State Is Not Outcome

State describes a condition of a Resource, Entity, system, or execution domain.

Outcome describes what has been established to have happened as a result of an execution or Intent.

These concepts must not be collapsed.

For example:

Transaction State:
PENDING

is not necessarily:

Outcome:
FAILURE

Likewise:

Action:
HTTP 200

does not necessarily establish:

Outcome:
SUCCESS

State and Outcome have distinct semantics.

⸻

23. Evidence Is Not Inference

Noema must distinguish:

* observed fact
* retrieved fact
* enterprise assertion
* user assertion
* model inference
* system-derived fact
* reconciled fact

For example:

Account Status:
ACTIVE
Source:
Bank API
Observed:
2026-08-25T10:00:00Z

is materially different from:

Account Status:
ACTIVE
Source:
Model inference

Consequential decisions should prefer authoritative evidence appropriate to the claim.

⸻

24. Evidence Must Carry Provenance

For consequential facts, Noema should know:

* what the fact is
* where it came from
* when it was observed
* how it was derived
* what scope it applies to
* whether the source is authoritative for that claim
* whether it is stale or contradicted

A fact without sufficient provenance may be insufficient for Trust.

⸻

25. Absence of Evidence Is Not Evidence of Permission

Noema must never reason:

No restriction found
        ↓
Therefore permitted

Instead, required authority, policy, state, evidence, and constraints must be explicitly satisfied where the operation requires them.

Missing evidence should remain missing.

⸻

26. Trust Must Be Deterministic

The Trust Engine should produce a deterministic decision from canonical inputs.

Conceptually:

Trust(
    Intent,
    Actor,
    Target,
    Capability,
    Authority,
    Policy,
    Constraint,
    Context,
    State,
    Evidence
)

should produce a defined decision.

Canonical Trust decisions include:

EXECUTE
CLARIFY
ESCALATE
REJECT

Additional execution-control or epistemic states such as:

CONFIRM
WAIT
UNKNOWN

may be required by particular execution semantics, but they must not be confused with the core distinction between permitting and refusing an Action.

The Model must not directly control the Trust decision.

⸻

27. Trust Is Not Model Confidence

A Model may return:

confidence = 0.97

That does not mean:

trust = 0.97

Model confidence describes confidence in an interpretation.

Trust describes whether Noema can legitimately permit a consequential Action given the canonical execution context.

These are fundamentally different dimensions.

⸻

28. Resolution Must Precede Execution

Before an Action executes, Noema should resolve the semantic objects required to execute it.

Depending on the Action, this may include:

* Actor
* Intent
* Entity
* Resource / Target
* Capability
* Parameters
* Context
* State
* Authority
* Policy
* Constraints
* required Evidence

The general flow is:

Interpret
   ↓
Schema Validate
   ↓
Resolve
   ↓
Reconcile
   ↓
Validate
   ↓
Trust
   ↓
Plan
   ↓
Execute

⸻

29. No Hidden Semantic State

Critical meaning must not exist only inside:

* prompts
* model context
* undocumented code
* tool descriptions
* application-specific conventions
* transient conversational assumptions

If a concept affects whether an Action is permitted, executed, verified, or explained, its relevant semantics should be representable in the canonical system.

⸻

30. The Canonical Representation Is the Contract

Once an Intent has crossed the schema boundary and been resolved into canonical form, downstream systems should operate on that representation rather than repeatedly reinterpreting the original natural language.

Source of Intent
      ↓
Canonical Intent
      ↓
Action
      ↓
Execution
      ↓
Outcome

This prevents semantic drift across the execution pipeline.

⸻

31. Intent Objects Must Be Versioned and Immutable After Admission to Trust

Once an Intent has been admitted into the Trust process, its canonical representation must not be silently overwritten.

If meaning changes materially:

Intent v1
      ↓
supersedes
      ↓
Intent v2

The amendment must be explicit and auditable.

Historical execution must remain attributable to the exact Intent version that governed it.

⸻

32. Natural Language Is an Interface, Not the Canon

Users and systems may express Intent through natural language.

Natural language is input.

Canonical Intent is meaning.

Action is execution.

Outcome is established result.

Noema should not treat conversational text as the ultimate representation of consequential Intent.

⸻

33. The Same Intent Should Be Interface-Independent

Intent should be representable regardless of whether it originated from:

* Chat
* Voice
* UI
* API
* Event
* Agent
* Application
* Messaging system

For example:

"Renew my card."

may originate from a chat interface, while an application may emit a structured request.

The canonical semantic representation should not depend on either surface.

⸻

34. Explicit Beats Implicit

If an important relationship matters to execution, represent it explicitly.

Prefer:

Actor
  └── has_authority_for ──► Action / Capability / Scope

over hidden application conventions.

Prefer:

Action
  └── targets ──► Resource

over targets inferred from arbitrary arguments.

Prefer:

Fact
  └── supported_by ──► Evidence

over untraceable assertions.

⸻

35. Determinism at the Boundary, Probabilism at the Edge

Noema should allow probabilistic systems where they create value:

* language understanding
* intent classification
* entity matching
* retrieval
* candidate generation
* plan proposal

But deterministic boundaries must surround consequential execution.

             Probabilistic
                 Model
                   ↓
          Candidate Meaning
                   ↓
        ┌────────────────────┐
        │ Hard Noema Boundary│
        └────────────────────┘
                   ↓
          Canonical Semantics
                   ↓
             Deterministic
        Resolution / Trust /
        Execution / Verification

This is a central architectural principle.

⸻

36. Clarification Is a First-Class Outcome

Clarification is not an error condition.

It is a legitimate system behavior when required information or semantic resolution is insufficient.

Intent
   ↓
Material ambiguity
   ↓
CLARIFY

A good Noema system should sometimes ask a question rather than perform an operation.

⸻

37. Escalation Is a First-Class Control

Some cases cannot be safely resolved by automated execution.

Examples include:

* unresolved material ambiguity
* contradictory enterprise state
* insufficient authority
* unresolved policy conflict
* execution requiring human judgment
* irrecoverable uncertainty

In these cases:

Noema
  ↓
ESCALATE
  ↓
Human / Enterprise Operator

is correct system behavior.

Escalation is not merely an automation failure.

⸻

38. Refusal Is Valid System Behavior

Noema must be able to refuse execution.

If:

Policy prohibits Action

then refusal is correct behavior.

Likewise, if authority is insufficient or a capability is prohibited, execution must stop.

Trustworthy execution requires the ability to say:

REJECT

without treating rejection as a system malfunction.

⸻

39. Human Approval Is a First-Class Control

Some Actions should require explicit human approval.

Intent
 ↓
Trust
 ↓
Approval Required
 ↓
Human Decision
 ↓
Execution

Noema should not equate autonomy with quality.

For high-impact operations, human intervention may be the correct operating point.

⸻

40. Least Privilege

Noema should use the minimum authority and capability necessary to satisfy an Intent.

If an Intent requires:

read_customer

Noema should not automatically request:

admin_customer

Likewise, an Action should operate against the smallest appropriate Resource and organizational scope.

⸻

41. Minimum Sufficient Action

Noema should prefer the smallest Action that fully satisfies the Intent.

Example:

Intent:
Change email address.

If:

UpdateEmail

is sufficient, Noema should not execute:

UpdateEntireCustomerProfile

unless required.

This reduces:

* blast radius
* unintended mutations
* authorization complexity
* failure modes
* recovery complexity

⸻

42. Minimum Sufficient Information

Noema should request only the information necessary to resolve and execute an Intent.

Bad:

Please provide all your account details.

Better:

Which of your two accounts should I use?

The objective is not maximum information.

It is sufficient information for safe and deterministic resolution.

⸻

43. Side Effects Must Be Explicit

An Action should make its meaningful side effects discoverable.

For example:

Action:
CancelSubscription
Effects:
Subscription → CANCELLED
Future billing → stopped
Access → retained until end of period

Noema should not execute consequential side effects that are invisible in the canonical Action semantics.

⸻

44. Read and Write Must Be Distinct

Noema should distinguish:

READ

from:

MUTATE

and:

DESTRUCTIVE

operations.

The Trust requirements for:

GetCustomer

should not automatically be equivalent to:

DeleteCustomer

Read-only operations can still require significant semantic resolution, authorization, evidence, and cross-system investigation.

⸻

45. Destructive and Consequential Actions Require Stronger Semantics

Actions that:

* delete
* transfer
* publish
* approve
* cancel
* revoke
* deploy
* send
* charge

may produce irreversible or consequential effects.

They should generally require stronger validation, authority, policy evaluation, and verification than informational operations.

⸻

46. Reversibility Matters

Noema should understand whether an Action is:

* reversible
* partially reversible
* irreversible

Irreversibility should influence Trust requirements, execution planning, recovery strategy, and human-approval requirements.

⸻

47. Idempotency Is a Semantic Requirement

Consequential execution must account for duplicate requests, retries, restarts, replay, and network uncertainty.

If an Intent has already been satisfied, Noema should avoid unnecessary duplicate execution.

For consequential Actions, an idempotency key should exist before execution where required by the execution contract.

The execution system must distinguish:

Same logical Action

from:

Different execution attempts

so that retries do not accidentally create duplicate effects.

⸻

48. Timeout Does Not Mean Failure

A timeout establishes that Noema did not receive sufficient confirmation within the expected period.

It does not establish that the external Action failed.

Therefore:

Execution Attempt
      ↓
Timeout
      ↓
UNKNOWN
      ↓
Verify / Reconcile

rather than:

Timeout
  ↓
Assume Failure
  ↓
Retry

This principle is critical for consequential operations.

⸻

49. Verify Before Retrying an Unknown Execution

If an execution may have succeeded but its result is unknown, Noema must verify or reconcile before issuing a potentially duplicative retry.

Attempt
  ↓
Unknown Result
  ↓
Verification / Reconciliation
  ↓
Established Result

Only when appropriate should a subsequent execution attempt occur.

⸻

50. Execution Success Is Not Intent Success

This distinction is foundational.

Action Success
      ≠
Intent Satisfaction

An HTTP 200, accepted request, or successful adapter invocation does not necessarily establish that the desired business Outcome occurred.

Noema must evaluate resulting state and available evidence.

⸻

51. Outcomes Must Be Verifiable

Where practical, Noema should verify that the expected Outcome actually occurred.

For example:

Expected:
Account → ACTIVE
Observed:
Account → ACTIVE

may establish successful completion.

If the observed state differs or cannot be established:

Outcome
→ NOT ESTABLISHED / UNKNOWN / FAILED

as appropriate.

Verification is part of execution, not an optional post-processing feature.

⸻

52. External Systems Remain Authoritative for Their Domain State

When Noema modifies an external Resource, the external system should remain authoritative for its resulting domain state unless the architecture explicitly establishes another authority.

For example:

Payment Provider

may remain authoritative for:

Payment = SETTLED

Noema should not declare a payment settled simply because its Action returned successfully.

⸻

53. State Reconciliation Is a First-Class Capability

Enterprise systems may provide conflicting, delayed, stale, incomplete, or differently scoped representations of the same real-world state.

Noema must be able to reconcile relevant observations before consequential decisions.

Reconciliation must preserve:

* source
* authority
* observation time
* effective time where available
* freshness
* contradictions
* uncertainty
* provenance

Conflicting state must not be silently collapsed into whichever source is most convenient.

⸻

54. Temporal Semantics Matter

Intent, State, Policy, Authority, and Evidence are interpreted relative to time.

Consider:

Book the room tomorrow.

The system may need to resolve:

* date
* time
* timezone
* resource
* availability
* applicable policy

Likewise, a policy valid yesterday may not govern an execution today.

Noema must treat temporal information as semantic data, not incidental metadata.

⸻

55. Scope Must Be Explicit

An operation may be scoped to:

* Actor
* Tenant
* Organization
* Project
* Account
* Environment
* Region
* Resource

Noema must not silently broaden scope.

For example:

Delete my test deployments.

must not become:

Delete all deployments.

Scope is part of execution legitimacy.

⸻

56. No Silent Escalation of Authority

Noema must not escalate an Intent into a more powerful Action merely because the more powerful Action is technically easier.

Requested:

READ

Executed:

READ + MODIFY

is unacceptable unless the additional operation is explicitly authorized and semantically required.

⸻

57. No Silent Expansion of Intent

Likewise:

Renew my card.

must not automatically imply:

* change address
* change billing plan
* increase credit limit
* order additional cards

unless those effects are explicitly part of the canonical Action or required by established domain semantics.

Noema must preserve the semantic scope of the original Intent.

⸻

58. Semantic Equivalence Must Be Preserved

Different expressions may resolve to the same canonical Intent.

For example:

"Renew my card."
"Get me a new card when this one expires."
"Replace my expiring card."

may represent equivalent or closely related semantics depending on context.

The canonical representation should capture meaning rather than surface wording.

⸻

59. Semantic Differences Must Be Preserved

Conversely, similar language may represent materially different Intents.

For example:

"Cancel my subscription."
"Pause my subscription."
"Stop charging me."
"Delete my subscription."

must not be collapsed merely because they are linguistically similar.

Semantic distinctions matter whenever they produce different Actions, authorities, constraints, or Outcomes.

⸻

60. Domain Semantics Must Be Composable

Noema should allow domains and enterprises to define their own:

* Entities
* Resources
* Capabilities
* Policies
* Constraints
* States
* Actions
* Outcomes

while using the same foundational ontology.

The goal is:

Universal Primitives
        +
Domain-Specific Semantics
        =
Executable Domain Intent

The universal core should remain stable while domain intelligence is introduced through explicit configuration and governed enterprise semantics.

⸻

61. Core Semantics Must Remain Domain-Agnostic

The foundational meaning of:

* Intent
* Actor
* Action
* Resource
* Capability
* Policy
* Constraint
* Authority
* Outcome
* State
* Context
* Evidence

should not depend on banking, healthcare, logistics, HR, or another particular industry.

Domains extend the primitives.

They should not casually redefine them.

⸻

62. Domain Logic Should Remain Domain-Owned

Noema should not become the ultimate owner of every domain rule.

For example:

Bank
  → Ledger semantics
Airline
  → Seat inventory semantics
Hospital
  → Clinical workflow semantics
ERP
  → Procurement semantics

Noema provides the common semantic execution layer through which relevant domain semantics can participate in governed execution.

Domain-specific intelligence should be represented explicitly through enterprise configuration, capabilities, adapters, policies, contracts, lexicons, and other governed assets.

⸻

63. Canonical Primitives Should Remain Small

Noema should resist continuously adding primitives.

A new primitive should exist only when existing concepts cannot accurately represent the required semantics.

The objective is:

Minimum ontology, maximum expressive power.

A concept should become foundational only when it is necessary across meaningful execution semantics rather than because one domain happens to need it.

⸻

64. Auditability Is a Design Requirement

For consequential Actions, Noema should be able to reconstruct the causal execution chain:

Who initiated
      ↓
What was intended
      ↓
How Intent was interpreted
      ↓
What was ambiguous
      ↓
How it was resolved
      ↓
What authority applied
      ↓
What policy applied
      ↓
What state and evidence were observed
      ↓
What Action was selected
      ↓
What was executed
      ↓
What the downstream system returned
      ↓
What was verified
      ↓
What final Outcome was established

Auditability must not be bolted onto the system after execution.

⸻

65. Explainability Means Traceability

Noema does not need to expose private Model reasoning.

It should instead provide an operationally useful decision trace.

For example:

Intent:
Renew Card
Resource:
Card #123
Capability:
renew_card
Authority:
Cardholder
Policy:
Card renewal permitted
Constraint:
Card must be eligible
Trust:
EXECUTE
Action:
RenewCard
Outcome:
Renewal accepted
Verification:
Confirmed by enterprise system

Explainability means being able to establish why the system acted, what it relied upon, and what happened.

⸻

66. Failure Must Be Explicit

Noema should represent meaningful failure conditions explicitly.

Examples include:

INTERPRETATION_FAILED
RESOLUTION_FAILED
AUTHORITY_FAILED
POLICY_FAILED
CONSTRAINT_FAILED
EXECUTION_FAILED
VERIFICATION_FAILED
RECONCILIATION_FAILED

A generic:

Something went wrong.

is insufficient for a system whose purpose is trustworthy execution.

⸻

67. Partial Failure Must Be Representable

Multi-step Intent execution may partially succeed.

Noema must preserve the actual execution state.

For example:

Step A → SUCCEEDED
Step B → FAILED
Step C → NOT_STARTED

must not be collapsed into:

Action → FAILED

without preserving the underlying execution history and consequences.

Partial success may require compensation, reconciliation, escalation, or replanning.

⸻

68. Compensation Must Not Be Assumed

If an Action fails after partial execution, Noema must not assume that simply executing an inverse Action restores the original State.

Compensation is domain-specific.

The system should explicitly represent whether compensation is:

* available
* required
* safe
* verified
* unavailable

Otherwise, reconciliation or human intervention may be required.

⸻

69. Recovery Must Preserve Uncertainty

Recovery must not destroy uncertainty merely to move execution forward.

When execution state is unknown, recovery should prefer:

Verify
→ Reconcile
→ Establish State
→ Retry / Re-plan / Escalate

rather than:

Unknown
→ Assume
→ Continue

Recovery is governed execution, not permission to guess.

⸻

70. Bounded Autonomy Is Preferable to Maximum Autonomy

Autonomy should be bounded by:

* Authority
* Policy
* Constraint
* Context
* State
* Evidence
* Risk
* Reversibility
* capability boundaries

The objective is not:

Maximum autonomy.

It is:

Maximum useful autonomy within a defined trust boundary.

Autonomy metrics must therefore be evaluated alongside unsafe execution, false blocking, intervention, and verification quality.

⸻

71. Correctness Comes Before Autonomy

The system should optimize in this order:

Correctness
   ↓
Safety
   ↓
Determinism
   ↓
Auditability
   ↓
Reliability
   ↓
Useful Autonomy
   ↓
Optimization

Autonomy that produces incorrect or unauthorized Actions is negative value.

⸻

72. The System Must Be Able to Stop

A trustworthy execution system requires valid non-execution terminal behaviors.

Noema must be comfortable with:

CLARIFY
ESCALATE
REJECT
WAIT

where appropriate.

The ability to say:

I cannot safely determine this.

is a feature, not a failure.

⸻

73. Structural Safety Is Preferable to Statistical Safety

Critical safety properties should not depend solely on the Model behaving correctly.

Noema should structurally constrain what can reach execution.

For example:

Model Output
     ↓
Schema Validation
     ↓
Registered Capability
     ↓
Bounded Action Contract
     ↓
Deterministic Trust
     ↓
Execution Controller

rather than:

Model
  ↓
Arbitrary Tool

A compromised, hallucinating, or manipulated Model must not automatically gain authority to execute prohibited operations.

⸻

74. Capabilities Must Be Explicitly Registered

An operation should not become executable merely because an API, HTTP endpoint, SQL query, or tool technically exists.

Capabilities must be explicit and governed.

Model-generated capability proposals may assist discovery.

They must not automatically become canonical executable capabilities.

Unregistered operations must not reach consequential execution.

⸻

75. Prohibited Operations Must Be Structurally Unavailable

If an operating environment prohibits an operation, that prohibition should not depend solely on Model behavior or natural-language instructions.

For example, in the fintech POC, monetary movement must be structurally unavailable.

Prohibited operations include:

* transferring money
* refunding money
* reversing transactions
* adjusting balances
* initiating payment instructions
* other financial movement

The system should make prohibited execution impossible through the normal capability and execution path.

⸻

76. Security Must Not Depend on Model Confidence

Noema must assume that:

* user input is untrusted
* Model output is untrusted
* retrieved enterprise text is untrusted
* tool responses are untrusted
* external data may be stale or manipulated

Model confidence must never be the basis for granting authority.

Models should not possess unrestricted enterprise credentials or direct access to enterprise systems.

Consequential execution must pass through governed Noema boundaries.

⸻

77. Integration Should Follow Semantics

Noema should not design its ontology around the quirks of an individual integration.

Bad:

Provider has X field
        ↓
Noema defines X as a universal primitive

Better:

Noema defines:
Payment
Provider Adapter maps:
Provider PaymentIntent
        ↕
Noema Payment

The canonical model comes first.

⸻

78. Adapters Translate; They Do Not Redefine

External systems should be connected through adapters that translate:

External Semantics
       ↕
Noema Canonical Semantics

Adapters may handle:

* protocol translation
* authentication
* request mapping
* response normalization
* error mapping
* provider constraints
* idempotency
* timeout semantics
* reconciliation
* observability

Adapters must not redefine Intent, Trust, Authority, or canonical ontology.

⸻

79. Enterprise Systems Remain the System of Record

Noema should generally operate above and across existing enterprise systems.

The architecture is:

                       Noema
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
         CRM             ERP         Payments
          │              │              │
          ▼              ▼              ▼
      Business        Business       Business
        State           State          State

Noema provides the semantic execution boundary.

Enterprise systems remain authoritative for their domain state.

⸻

80. Noema Is an Embedded Enterprise Capability, Not Merely an Internal Tool

Noema should be capable of being embedded into enterprise products so that an enterprise’s own customers and users can interact with consequential operations through Noema’s trust and execution infrastructure.

This means Noema’s boundary is not defined solely around internal enterprise employees.

The source of Intent may be:

Enterprise Customer
Enterprise Employee
Enterprise Agent
Enterprise Application
Automated System

The semantic and trust boundary remains the same.

⸻

81. Noema Should Support Multiple Operating Modes

Noema has two conceptual operating modes.

Mode 1:

Source of Intent
      ↓
Noema
      ↓
Enterprise Systems

Noema provides the full semantic execution path.

Mode 2:

Human / Existing Agent / Orchestrator
              ↓
           Noema
       Trust Boundary
              ↓
      Enterprise Execution

In Mode 2, an enterprise may retain its existing interaction or orchestration layer while inserting Noema as an independent trust and execution boundary before consequential Actions.

The underlying semantic principles remain the same.

⸻

82. Workflow and Orchestration Are Downstream of Semantics

Noema may plan and coordinate multiple Actions.

However, the existence of a workflow or execution graph does not replace the semantic model.

The relationship is:

Intent
   ↓
Resolution
   ↓
Trust
   ↓
Plan / Action Graph
   ↓
Execution
   ↓
Verification
   ↓
Outcome

The workflow is an execution mechanism.

The Intent remains the semantic origin.

⸻

83. Durable Execution Is a Substrate, Not the Thesis

Noema should use appropriate durable execution primitives rather than rebuilding infrastructure whose semantics are already sufficiently solved.

Durable execution provides reliability for:

* retries
* persistence
* recovery
* long-running operations
* execution coordination

Noema provides the semantic governance surrounding those operations.

Durability is necessary infrastructure.

It is not the definition of Noema.

⸻

84. Operational Memory Is Not Generic Model Memory

Noema may maintain structured operational history.

This is not equivalent to generic conversational or vector-store memory.

Operational Memory concerns information such as:

* prior execution
* case history
* failure patterns
* recovery attempts
* verification results
* operational conditions
* enterprise execution knowledge

Operational Memory must not become an authority substitute for current enterprise state or current policy.

⸻

85. Operational Learning Must Not Become Self-Authorization

Execution history may inform:

* evaluation
* failure learning
* recovery
* system improvement
* operational analysis

It must not silently rewrite:

* canonical ontology
* capabilities
* policies
* authority
* execution contracts
* safety constraints
* enterprise graph semantics

Learned or model-generated changes must pass through explicit governance before becoming canonical.

⸻

86. Audit History Must Be Append-Only in Meaning

Corrections to canonical history should not silently erase what previously happened.

If a previous interpretation, state observation, or execution record was incorrect, the correction should be represented explicitly.

The system must preserve the distinction between:

What was previously believed

and:

What is now established

This is necessary for causal reconstruction and operational trust.

⸻

87. Noema Should Prefer Minimum Necessary Blast Radius

The scope of an Action should be no broader than necessary to satisfy the Intent.

This applies to:

* data access
* capability access
* Resource scope
* organizational scope
* mutation scope
* credentials
* execution permissions

The smaller the legitimate execution surface, the smaller the potential failure and security blast radius.

⸻

88. Noema Must Preserve Semantic Boundaries Across Failures

Failure in one layer must not silently rewrite the meaning of another layer.

For example:

Provider Failure
      ≠
Intent Failure
Model Uncertainty
      ≠
Authorization Failure
Execution Timeout
      ≠
Business Outcome Failure
Missing Evidence
      ≠
False Fact

Each layer should preserve its own semantics while exposing the information required for downstream decisions.

⸻

89. Semantic Compression Is a Core Design Objective

Noema’s value should increase as complex human intent can be represented through a small, stable set of precise canonical primitives.

Conceptually:

Human Expression
       ↓
Complex Intent
       ↓
Canonical Representation
       ↓
Executable Semantics

The canonical representation should be more precise than the original expression without requiring the original expression to remain the execution contract.

⸻

90. The Canonical Model Must Outlive the Model

Models will change.

Prompt techniques will change.

Integration protocols will change.

Infrastructure will change.

The canonical semantic model should remain comparatively stable.

Model              → Replaceable
Prompt             → Replaceable
Transport          → Replaceable
Integration        → Replaceable
Storage            → Replaceable
Execution Runtime  → Replaceable
Ontology           → Durable
Intent Model       → Durable
Trust Model        → Durable
Action Semantics   → Durable
Execution Semantics→ Durable
Outcome Semantics  → Durable

⸻

91. Implementation Technology Must Remain Replaceable

The architecture should permit replacement of:

* Model
* Database
* Graph Store
* Vector Store
* Queue
* Transport
* Integration
* Execution Runtime
* Retrieval system

without changing the fundamental Noema thesis.

Implementation choices serve the canonical model.

The canonical model should not become an accidental abstraction of the implementation.

⸻

92. The Canonical Architecture Must Be Auditable Through Its Invariants

Every major architectural component should have explicit invariants.

Examples include:

No free-form Model output reaches execution.
No unregistered Capability reaches execution.
Material ambiguity cannot produce EXECUTE.
Unknown execution outcomes cannot be silently classified as failure.
Consequential retries require appropriate idempotency and verification.
Enterprise business state remains owned by authoritative enterprise systems.
Trust decisions use canonical inputs rather than Model confidence.
Prohibited capabilities cannot be invoked through normal execution paths.
Consequential decisions must be reconstructable.

These invariants should be testable.

⸻

93. The Architecture Must Fail Closed for Consequential Execution

When required information, authority, policy, capability, or state cannot be established, Noema should not silently widen permissions or invent missing information.

For consequential execution:

Missing required condition
        ↓
Do not execute

The system may instead:

Clarify
Request Evidence
Wait
Escalate
Reject

depending on the nature of the missing condition.

⸻

94. Optimize Against Unsafe Autonomy, Not Raw Autonomy

Autonomous Resolution Rate is useful only when evaluated together with safety and correctness.

Noema should measure at least concepts such as:

* Autonomous Resolution Rate
* Intervention Rate
* Unsafe Rate
* False Block Rate
* Resolution Time
* Verification Success
* Escalation Rate

The desired operating point is the highest useful autonomy within the zero-unsafe region, not the highest possible automation rate.

⸻

95. The System Must Be Tested Adversarially

A trustworthy execution system cannot be validated only with happy-path examples.

Testing should include:

* ambiguous intent
* conflicting state
* stale evidence
* unknown outcomes
* duplicate submissions
* replay
* timeout after possible success
* insufficient authority
* confused-deputy scenarios
* policy conflicts
* prompt injection
* malicious or misleading retrieved content
* code-switched language
* incomplete context
* unavailable systems
* prohibited capabilities

Safety-critical invariants must be release-gating.

⸻

96. The Product Wedge Must Not Redefine the Universal Architecture

A particular domain may provide the first commercial or technical proving environment.

That domain does not redefine Noema’s universal semantics.

The hierarchy is:

Noema
  ↓
Trusted Enterprise Execution Infrastructure
  ↓
Intent Computing
  ↓
Domain
  ↓
Specific Execution Problem
  ↓
POC / Wedge

Domain-specific implementation should prove the horizontal architecture rather than replace it.

⸻

97. The Ultimate Principle

All other principles ultimately serve one idea:

Noema exists to make intent executable without making uncertainty, authority, policy, state, or execution outcomes invisible.

The canonical conceptual pipeline is:

             SOURCE OF INTENT
                    │
                    ▼
                 INTENT
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Context    Actor    Entities
          │         │         │
          └─────────┼─────────┘
                    ▼
           Canonical Meaning
                    │
             Schema Validation
                    │
                    ▼
            State / Evidence
             Reconciliation
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Resource Capability Authority
          │         │         │
          └─────────┼─────────┘
                    ▼
              Policy / Constraints
                    │
                    ▼
                 TRUST
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       EXECUTE    CLARIFY   ESCALATE
          │                    │
          │                    ▼
          │                  HUMAN
          │
          ▼
        ACTION
          │
          ▼
      EXECUTION
          │
          ├──────────────┐
          ▼              ▼
      VERIFIED        UNKNOWN
          │              │
          │        VERIFY / RECONCILE
          │              │
          └───────┬──────┘
                  ▼
               OUTCOME
                  │
                  ▼
           RESULTING STATE
                  │
                  ▼
        INTENT SATISFIED?

And the governing rule is:

Interpret probabilistically. Validate at a hard boundary. Resolve canonically. Decide deterministically. Execute explicitly. Verify the outcome. Preserve uncertainty. Record the causal history.