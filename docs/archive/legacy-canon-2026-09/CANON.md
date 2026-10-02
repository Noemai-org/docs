> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

CANON.md

# Noema Canon
Status: Foundational
Version: 0.2
Purpose: Define the principles, boundaries, terminology, lifecycle, and invariants that constitute Noema.
⸻
## 1. Purpose
Noema is an intent infrastructure layer for turning human intent into validated, trusted, executable actions across existing software systems.
Noema exists between human intent and enterprise execution.
Its fundamental responsibility is to establish a reliable boundary between what an Actor means and what an existing system is permitted and capable of doing.
Noema does not replace enterprise systems, databases, or business applications.
Instead, Noema:
* represents Intent
* resolves Intent
* contextualizes Intent
* validates Intent
* establishes Evidence
* evaluates Trust
* determines execution eligibility
* selects applicable Capabilities
* creates or carries Execution Contracts
* coordinates execution through existing systems
* records provenance
* observes and represents Outcomes
Noema therefore separates:
* interpretation from resolution
* resolution from validation
* validation from trust
* trust from execution
* intent state from business state
* probabilistic inference from deterministic evaluation
* capability from authorization
* authorization from trust
* planning from execution
* execution from outcome
* Noema state from enterprise business truth
⸻
## 2. The Core Thesis
Human intent should be expressible as a structured, verifiable, and executable object rather than remaining trapped inside an application-specific interface.
Traditional software requires humans to translate their goals into the vocabulary and interaction model of each application.
Noema reverses this relationship.
The Actor expresses what they want.
Noema resolves that expression into a canonical Intent representation, establishes the context and evidence required to evaluate it, validates its structure and applicability, evaluates whether its applicable Trust requirements are satisfied, and maps the trusted Intent onto executable Capabilities exposed by systems that can fulfill it.
The application remains authoritative for its domain.
Noema becomes responsible for the intent-to-action boundary.
The canonical lifecycle is therefore:
Human Expression
      ↓
Interpretation
      ↓
Intent
      ↓
Resolution
      ↓
Validation
      ↓
Trust
      ↓
Execution Eligibility
      ↓
Execution Contract
      ↓
Execution
      ↓
Outcome
⸻
## 3. What Noema Owns
Noema owns Intent state and the state associated with Noema's intent-to-action lifecycle.
This includes, but is not limited to:
* expressed Intent representation
* Intent interpretation and resolution
* ambiguity and clarification state
* contextualized Intent
* Intent constraints
* Intent provenance
* Validation state
* Trust requirements
* Trust state
* Trust evaluation history
* execution eligibility
* Action selection
* Execution Contract state
* execution coordination state
* provenance of decisions made by Noema
* the relationship between Intent and executable Actions
Noema does not own the authoritative business state of the systems it operates against.
For example, if a banking system is authoritative for an account's balance, Noema does not become the source of truth for that balance.
Noema may observe, reason about, validate against, and act upon that state through defined interfaces.
Therefore:
> Noema owns Intent state, not business state.
This is a foundational architectural boundary.
⸻
## 4. The Noema Boundary
Noema sits between human intent and existing systems.
```text
Human
  │
  │ expresses
  ▼
Intent Expression
  │
  │ interpret / resolve
  ▼
Resolved Intent
  │
  │ validate
  ▼
Validated Intent
  │
  │ evaluate
  ▼
Trust Decision
  │
  │ establish eligibility
  ▼
Execution Contract
  │
  │ accepted by consumer
  ▼
Execution
  │
  │ produces
  ▼
Business Outcome

Noema does not need to own the systems on either side of this boundary.

Its value comes from making the boundary between what an Actor means and what a system may execute explicit, reliable, inspectable, and enforceable.

⸻

5. The Probabilistic / Deterministic Boundary

AI models are inherently probabilistic.

Noema may use probabilistic models to:

* interpret natural language
* identify candidate Intents
* extract entities
* infer relationships
* retrieve relevant context
* propose Actions
* generate clarification questions
* construct candidate plans
* assist with contextualization

However:

Probabilistic inference must not be silently converted into deterministic authority.

The deterministic Noema layers establish the boundary between probabilistic understanding and executable action.

The Model may propose.

Noema must establish.

The Model may infer.

Noema must validate.

The Model may be uncertain.

Noema must represent that uncertainty explicitly.

The Model must not directly establish execution authority.

⸻

6. Noema Must Not Guess

When Noema lacks sufficient information to establish what the Actor intends, it must not manufacture certainty.

Insufficient semantic certainty must produce an explicit state.

That state is unresolved or clarification-required.

Actor Expression
       ↓
Interpretation
       ↓
Resolution
       │
   ┌───┴────┐
   │        │
Resolved  Unresolved
   │        │
   ▼        ▼
Validation Clarification
             │
             ▼
          Resolution

Clarification is not an error condition.

It is a legitimate lifecycle state.

When Noema cannot establish material Intent semantics, the correct action is to ask rather than guess.

Context may resolve ambiguity when the context provides an explicit, authoritative basis for doing so.

Context must never be used to manufacture certainty merely because one interpretation appears probable.

⸻

7. Intent Is a First-Class Object

An Intent is a canonical semantic representation of an Actor’s desired objective, including the entities, parameters, constraints, and temporal requirements necessary to express what the Actor intends to accomplish.

An Intent is not merely a string extracted from a conversation.

Conceptually:

Intent
├── actor
├── objective
├── action
├── subject / resources
├── parameters
├── context
├── constraints
├── temporal requirements
├── desired outcome
├── required capabilities
├── provenance
└── lifecycle state

The exact schema is defined elsewhere in the canonical ontology and Intent specifications.

Human language is an input to Intent resolution.

It is not itself the executable representation of Intent.

⸻

8. Intent Must Be Contextual

Intent cannot always be established from an Actor’s expression alone.

Noema may require:

* Actor identity
* organizational context
* current business state
* relevant resource state
* policies
* authorization information
* available Capabilities
* temporal information
* workflow state
* external Evidence
* prior interaction state where explicitly relevant

Context is therefore a first-class input to Intent resolution, Validation, and Trust evaluation where applicable.

However:

Context may resolve ambiguity, but context must not manufacture authority.

Context must itself be relevant, inspectable, and governed by the requirements of the operation.

Noema should not collect or incorporate context merely because it is available.

⸻

9. Resolution, Validation, and Trust Are Distinct

Noema must preserve three distinct questions:

Resolution

What does the Actor mean?

Validation

Is the resulting Intent structurally complete, semantically applicable, and valid for its next lifecycle transition?

Trust

Given this valid Intent and its applicable conditions, may it cross the execution boundary?

Therefore:

Interpretation
      ↓
Resolution
      ↓
Validation
      ↓
Trust

These layers must not be collapsed into one probabilistic judgment.

An Intent may be:

* unresolved
* resolved but incomplete
* valid but untrusted
* trusted but not autonomously executable
* ready for execution
* executed
* completed or failed

Each represents a materially different condition.

⸻

10. Validation Is Deterministic

Validation is the deterministic verification layer for establishing that a resolved Intent is structurally complete, semantically applicable, and consistent with the explicit rules, references, Evidence, constraints, and Context required for its next lifecycle transition.

Validation may include:

* structural validation
* required-field validation
* type validation
* reference validation
* domain validation
* cross-field validation
* cross-entity validation
* constraint validation
* context validation
* temporal validation
* freshness validation
* capability representation validation

Validation produces a structured result rather than a simple boolean.

Conceptually:

ValidationResult {
    status
    errors
    warnings
    requirements
    evidence
}

The canonical result states are:

VALID
INVALID
INCOMPLETE
UNKNOWN

Unknown information must not be treated as valid information.

Therefore:

UNKNOWN ≠ VALID

Validation must not silently modify the Intent to make it valid.

⸻

11. Validation Does Not Equal Trust

Validation establishes whether the Intent is valid for its next lifecycle transition.

Trust establishes whether the applicable conditions for execution eligibility have been satisfied.

Therefore:

Valid ≠ Trusted.

For example:

Valid Intent
     ↓
Authorization denied
     ↓
Trust = BLOCKED

A valid Intent may therefore remain blocked.

Similarly:

Valid Intent
     ↓
Approval required
     ↓
Trust = WAITING

Validation must not become a duplicate Trust Engine.

⸻

12. Validation Must Not Guess

If validation cannot establish a required fact, it must represent that condition explicitly.

Example:

recipient = customer_123
customer registry unavailable

The result is:

Recipient validation = UNKNOWN

not:

Recipient exists = TRUE

Likewise, if:

recipient = "John"

and multiple authoritative records match:

Validation = INCOMPLETE

or the corresponding semantic ambiguity remains unresolved.

Noema must not select a recipient merely because one candidate appears statistically likely.

⸻

13. Trust Is a Structured Decision

Trust is not:

* a probability
* a model confidence score
* a scalar
* a feeling
* a heuristic judgment

Trust is a structured decision over explicit conditions.

Conceptually:

                    Intent
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Evidence   Authorization   Context
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Policy Evaluation
                       │
                       ▼
                  Risk Evaluation
                       │
                       ▼
                Constraint Check
                       │
                       ▼
               Capability Check
                       │
                       ▼
                 Trust Decision
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
           READY              NOT READY

The applicable dimensions depend on the Intent and its governing requirements.

⸻

14. Trust Is a Property of an Intent Instance

Trust does not exist in isolation.

There is no meaningful:

Trust = 0.9

without specifying:

* Trust of what?
* For which Actor?
* Under which conditions?
* At what time?
* Based on which Evidence?
* Under which Policy versions?
* For which Intent version?
* With which Capabilities?
* Under which Constraints?

Trust is therefore evaluated against a specific Intent instance and its governing conditions.

A conceptual Trust tuple is:

Trust =
(
    Intent,
    Actor,
    Context,
    Evidence,
    Authorization,
    Policy,
    Risk,
    Capability,
    Constraints,
    Time
)

⸻

15. Trust Is Relational and Contextual

Trust is not an intrinsic property of an Action.

For example:

Transfer ₦1,000

may be executable for one Actor and blocked for another.

Likewise:

Deploy application

may be executable in one environment and require approval in another.

Therefore:

Trust is relational and contextual.

The same Action does not imply the same Trust result across Actors, resources, environments, or times.

⸻

16. Trust Dimensions

The canonical Trust Model may evaluate:

* Resolution
* Evidence
* Authorization
* Policy
* Risk
* Capability
* Constraints
* Context
* Freshness

Not every Intent requires every dimension at equal strength.

The applicable requirements are determined by the semantics and governance surrounding the Intent.

Trust therefore evaluates applicable requirements rather than blindly requiring every possible dimension.

⸻

17. Trust Preconditions

Conceptually:

TrustRequirements {
    resolution
    evidence
    authorization
    policy
    risk_controls
    capabilities
    constraints
    confirmations
    approvals
}

Each requirement has an explicit state.

A useful condition-state vocabulary is:

SATISFIED
UNSATISFIED
UNKNOWN
REQUIRED
NOT_APPLICABLE
EXPIRED

The exact implementation may evolve, but the semantic distinction must remain.

⸻

18. Unknown Must Not Become Ready

Unknown is an important internal condition.

For example:

Authorization service unavailable

must produce:

Authorization = UNKNOWN

not:

Authorization = ALLOWED

For consequential Actions:

UNKNOWN → NOT READY

Fail-closed semantics therefore mean:

Noema does not treat unavailable or unestablished mandatory conditions as satisfied.

Fail-closed does not require permanent denial.

An unresolved condition may transition to Waiting and subsequently be re-evaluated when the requirement becomes established.

⸻

19. Authorization Is Not Trust

Authorization answers:

May this Actor perform this Action?

Trust answers:

Have all applicable conditions for this particular Intent been satisfied such that it may cross the execution boundary?

Therefore:

Authorized ≠ Trusted

Authorization is one dimension of Trust, not a substitute for Trust.

⸻

20. Policy Is Not Trust

Policy establishes the rules under which an Intent may proceed.

A Policy may produce:

ALLOW
DENY
REQUIRE_APPROVAL
REQUIRE_CONFIRMATION
REQUIRE_ADDITIONAL_EVIDENCE

Trust incorporates the applicable Policy result into the overall decision.

Therefore:

PolicySatisfied ≠ TrustReady

⸻

21. Risk Is Not Trust

Risk describes the potential consequence profile associated with an Intent.

Risk may determine:

* required Evidence
* approval requirements
* confirmation requirements
* execution limits
* autonomy requirements
* additional controls

Risk does not necessarily imply denial.

Therefore:

RiskAcceptable ≠ TrustReady

⸻

22. Capability Is Not Permission

Capability establishes whether the required Action can be performed by an execution consumer.

Authorization establishes whether the Actor may cause the Action.

Trust establishes whether all applicable conditions have been satisfied.

Therefore:

CapabilityAvailable ≠ Authorized
CapabilityAvailable ≠ TrustReady
Authorized ≠ TrustReady

Noema must preserve these distinctions.

⸻

23. Constraints Are Explicit Boundaries

Constraints define explicit boundaries within which an Intent may execute.

Examples include:

amount ≤ ₦5M
resource belongs to Actor
execution only during business hours
maximum 3 retries
destination must be within approved region

Constraint satisfaction is part of Validation and/or Trust according to where the constraint is defined and what it governs.

A hard constraint violation must not silently become executable.

⸻

24. Freshness Is a Trust Concern

Evidence existing is insufficient when the decision depends on current state.

Noema must distinguish:

Evidence Exists

from:

Evidence Is Fresh Enough

Freshness may apply to:

* authorization
* approval
* resource state
* external system state
* risk conditions
* contextual information
* other time-sensitive Evidence

An expired or stale requirement must be re-evaluated.

⸻

25. Trust Is Deterministic

Given the same:

* Intent version
* Actor
* Evidence
* Policy versions
* Authorization state
* Risk rules
* Capabilities
* Constraints
* Context
* Freshness state

the Trust evaluation must produce the same result.

Conceptually:

Trust(I, A, E, P, R, C, K, X, F)
    → deterministic Trust Decision

The exact implementation may use different evaluation mechanisms, but the semantic result must not depend on arbitrary probabilistic variation.

⸻

26. Model Confidence Is Not Trust

A Model may produce:

confidence = 0.92

That is not a Trust decision.

The canonical flow is:

Model
  ↓
Intent Candidate
  ↓
Resolution
  ↓
Validation
  ↓
Trust

Model confidence may inform interpretation or identify uncertainty.

It does not establish execution authority.

A high-confidence interpretation can still be:

Trust = BLOCKED

A lower-confidence interpretation may instead require:

Clarification

Confidence and Trust therefore remain separate concepts.

⸻

27. Trust State Is Explicit

Trust must be represented as explicit lifecycle state.

The canonical Trust categories are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Reason-specific subtypes may be used.

Examples:

WAITING_FOR_CLARIFICATION
WAITING_FOR_EVIDENCE
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CONFIRMATION
WAITING_FOR_APPROVAL
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE

and:

BLOCKED_BY_AUTHORIZATION
BLOCKED_BY_POLICY
BLOCKED_BY_CONSTRAINT
BLOCKED_BY_RISK
BLOCKED_BY_SCOPE
BLOCKED_BY_RESOURCE

Waiting and blocking are not different confidence levels.

They are different semantic conditions.

WAITING = not yet
BLOCKED  = prohibited

⸻

28. Trust State Machine

The Trust State Machine defines how Trust evolves over time.

The canonical conceptual lifecycle is:

                    ┌──────────────────┐
                    │    UNRESOLVED    │
                    └────────┬─────────┘
                             │
                       meaning established
                             │
                             ▼
                    ┌──────────────────┐
                    │    EVALUATING    │
                    └────────┬─────────┘
                             │
                ┌────────────┼─────────────┐
                │            │             │
                ▼            ▼             ▼
             WAITING       BLOCKED       READY
                │                          │
                │                          ▼
                │                     Execution
                │                          │
                │                          ▼
                │                       Outcome
                │
                └──── requirement satisfied
                              │
                              ▼
                         EVALUATING

Trust is therefore a lifecycle, not a one-time boolean decision.

⸻

29. No Direct WAITING → READY

The canonical transition is:

WAITING
   ↓
Requirement satisfied
   ↓
EVALUATING
   ↓
READY

Satisfying one requirement does not prove that all other requirements remain satisfied.

Example:

Approval received

while:

Authorization expired

The Trust Engine must re-evaluate.

⸻

30. No Direct BLOCKED → READY

Likewise:

BLOCKED
   ↓
Blocking condition removed
   ↓
EVALUATING
   ↓
READY

Removing one block does not establish that every other requirement is satisfied.

⸻

31. READY Is Not Permanent

READY means:

At the evaluated time and under the evaluated conditions, the Intent satisfies the applicable Trust requirements for execution eligibility.

READY does not mean permanently trusted.

A READY Intent may become invalid because:

* authorization changes
* policy changes
* Evidence expires
* Context changes
* risk changes
* Capability disappears
* Constraints change
* resource state changes
* the Intent changes materially

Therefore:

READY
  ↓
material change
  ↓
EVALUATING

⸻

32. Trust and Intent Version

Trust belongs to an Intent version.

Conceptually:

Intent v1
   ↓
Trust Evaluation v1

If the Intent materially changes:

Intent v2
   ↓
new Trust Evaluation

Trust must not silently carry across material Intent changes.

⸻

33. Trust Re-Evaluation

Trust must be re-evaluated when a material input changes.

Examples include:

* Intent changes
* Actor changes
* Evidence changes
* Evidence expires
* Authorization changes
* Policy changes
* Risk changes
* Capability changes
* Constraints change
* Context changes
* Trust validity expires

A dependency-aware implementation may re-evaluate only affected Intents, provided correctness is preserved.

⸻

34. Trust Evaluation vs Trust Decision

These are conceptually distinct.

Evaluation asks:

What did Noema inspect?

Decision asks:

What did Noema conclude?

For example:

Trust Evaluation
    ↓
17 conditions examined
    ↓
Trust Decision
    ↓
WAITING_FOR_APPROVAL

A Trust Evaluation should therefore preserve the inputs, requirements, results, and provenance supporting the final decision.

⸻

35. Trust Evaluation Record

Conceptually:

TrustEvaluation {
    id
    intent
    intent_version
    evaluated_at
    conditions
    requirements
    evidence
    policy_results
    authorization_result
    risk_result
    capability_result
    constraint_results
    status
    reasons
}

The exact schema is implementation-specific.

The semantic requirement is that the decision be reconstructible from explicit recorded inputs and rules.

⸻

36. Trust Decision Reasons

Every non-ready decision should expose deterministic reasons.

Example:

status:
BLOCKED
reasons:
[
    AUTHORIZATION_DENIED,
    POLICY_PROHIBITS_ACTION
]

Reasons should be machine-readable.

Waiting states should identify what is required next.

Example:

status:
WAITING_FOR_APPROVAL
requirements:
[
    SECONDARY_APPROVAL
]

This allows Noema to transition the Intent rather than merely returning an opaque error.

⸻

37. Trust and Clarification

Semantic uncertainty belongs to the Resolution lifecycle.

Example:

Intent
  ↓
AMBIGUOUS
  ↓
CLARIFICATION
  ↓
RESOLVED
  ↓
VALIDATION
  ↓
TRUST

If a required semantic field is missing, Noema should request clarification rather than attempt to authorize or execute an incomplete Intent.

⸻

38. Trust and Approval

Approval is distinct from authorization.

Authorization establishes whether an Actor has authority within an applicable scope.

Approval establishes that an authorized approval requirement has been satisfied.

Conceptually:

Trust Evaluation
      ↓
WAITING_FOR_APPROVAL
      ↓
Approval received
      ↓
EVALUATING
      ↓
READY

Approval is Evidence supporting the Trust decision.

⸻

39. Trust and Confirmation

Confirmation is distinct from approval.

Confirmation means:

The Actor confirms the Action.

Approval means:

An authorized Actor grants required permission for the Action.

Noema must preserve this distinction.

For example:

WAITING_FOR_CONFIRMATION

must not be satisfied merely because an approval exists.

⸻

40. Trust and Autonomy

Trust and autonomy are related but distinct.

An Intent may be sufficiently trusted for execution eligibility while still requiring human confirmation or approval for autonomous execution.

Conceptually:

Trust:
READY
Autonomy:
CONFIRMATION_REQUIRED

or:

Trust:
READY
Autonomy:
APPROVAL_REQUIRED

Therefore:

Execution eligibility and autonomy eligibility are distinct concepts.

The exact autonomy model is defined by the relevant autonomy specifications.

⸻

41. Actions Must Be Explicit

Noema must not treat arbitrary Model-generated instructions as executable Actions.

Execution must occur through defined Capabilities and Action Contracts.

An executable Action should establish, where applicable:

* Action identity
* target
* inputs
* required Capability
* authorization requirements
* preconditions
* constraints
* expected side effects
* postconditions
* failure semantics
* idempotency semantics
* audit requirements

Conceptually:

Trusted Intent
      ↓
Action Selection
      ↓
Action Contract
      │
      ├── Preconditions
      ├── Authorization
      ├── Constraints
      ├── Capability
      └── Execution Scope
      ↓
Execution
      ↓
Postcondition / Outcome Verification

Noema executes contracts, not Model output.

⸻

42. Trust and the Execution Boundary

The canonical boundary is:

Before Trust:
Interpretation
Resolution
Validation
Evidence
Evaluation
Governance

and:

After Trust:
Execution eligibility
Execution Contract
Consumer acceptance
Execution
Outcome

A READY Trust decision enables the Intent to produce or carry an Execution Contract.

READY does not itself execute the Action.

⸻

43. Execution Requires an Explicit Boundary

The canonical transition is:

READY
   ↓
Execution Contract
   ↓
Consumer acceptance
   ↓
Execution

There must not be an implicit:

READY → EXECUTING

without an explicit execution boundary.

The execution consumer remains authoritative over whether it can actually accept and perform the requested Action.

⸻

44. Trust Does Not Guarantee Execution Success

Trust establishes execution eligibility under Noema’s control.

It does not guarantee that the external system will accept or successfully complete the Action.

For example:

Trust = READY

does not mean:

Database transaction = guaranteed

or:

Payment = guaranteed

The execution consumer may perform additional authoritative checks.

Therefore:

READY ≠ SUCCESS

⸻

45. Execution and Outcome Are Distinct

The canonical relationship is:

Trust
  ↓
Execution Eligibility
  ↓
Execution
  ↓
Outcome

Trust precedes execution.

Outcome follows execution.

An execution may result in:

* success
* failure
* partial completion
* rejection
* timeout
* unknown outcome

The Outcome belongs to the execution lifecycle and must not be confused with the Trust decision that preceded it.

⸻

46. Noema Does Not Own Business Truth

Enterprise systems remain authoritative for their respective domains.

Examples include:

* payment processors owning payment state
* identity providers owning identity state
* CRMs owning customer records
* HR systems owning employee records
* banking systems owning account state

Noema may coordinate across these systems, but it must not silently create a competing source of truth.

When Noema requires information, it should obtain that information through explicit interfaces and retain appropriate provenance.

When Noema causes business state to change, the authoritative system remains the system of record.

⸻

47. Consumer-Side Validation Is Expected

The execution consumer may perform additional validation.

For example:

Noema:
Intent valid
+
Trust READY

followed by:

Payment Service:
Account balance changed

The consumer may reject execution.

This does not necessarily mean Noema’s earlier Validation or Trust evaluation was incorrect.

Business state may change between:

Validation
   ↓
Trust
   ↓
Execution

The consumer remains authoritative for final business-state validity.

⸻

48. Race Conditions and TOCTOU

Consequential execution can encounter time-of-check/time-of-use conditions.

Conceptually:

T1: Validation
T2: Trust
T3: Execution

A condition may change between these stages.

Therefore Noema must not assume that a prior Validation or Trust decision guarantees execution success.

Where required, execution consumers must perform final authoritative checks.

⸻

49. Every Action Has a Boundary

Noema must know what it is permitted to do.

Autonomy therefore exists within explicit boundaries.

Those boundaries may include:

* Actor authorization
* organizational Policy
* Action Contracts
* financial limits
* data-access boundaries
* Risk thresholds
* approval requirements
* Capabilities
* temporal Constraints
* human-in-the-loop requirements

Noema must never interpret:

"be autonomous"

as permission to invent its own authority.

Autonomy is bounded by explicit authority, Policy, Capability, and Contract.

⸻

50. Human Intervention Is a First-Class State

Noema must be capable of stopping progression and requesting human intervention.

Human intervention may be appropriate when:

* Intent remains ambiguous
* required Evidence is unavailable
* Policy requires approval
* Authorization cannot be established
* Risk controls require intervention
* confirmation is required
* Capability is unavailable
* an execution contract cannot establish required conditions
* execution produces an unexpected state
* business rules require human judgment

Human intervention is not necessarily failure.

It is a legitimate outcome of bounded autonomy.

⸻

51. Failure Is Part of the Model

Noema must treat failure as a first-class lifecycle condition.

Failures may occur during:

* interpretation
* resolution
* context acquisition
* validation
* Trust evaluation
* Capability discovery
* authorization
* planning
* contract creation
* execution
* postcondition verification

Noema must distinguish among:

* unresolved meaning
* incomplete information
* unknown information
* invalid Intent
* denied authority
* unavailable Capability
* prohibited Policy
* violated Constraint
* required approval
* required confirmation
* execution failure
* partial execution
* unknown execution outcome

A generic FAILED result is insufficient where a more precise state can be established.

⸻

52. Explicit State Is Preferred Over Implicit Behavior

Important system conditions must be represented as explicit state rather than inferred from side effects or application behavior.

Examples include:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY
EXECUTING
COMPLETED
FAILED

with reason-specific states or attributes where appropriate.

The precise Trust State Machine is defined in the canonical Trust specifications.

The principle is:

If a condition materially affects what Noema may do next, that condition should be representable as explicit state.

⸻

53. Intent Lifecycle and Trust Lifecycle Are Distinct

Noema must not collapse the semantic Intent lifecycle into the Trust lifecycle or execution lifecycle.

Conceptually:

Intent Lifecycle
    │
    ├── Created
    ├── Resolving
    ├── Resolved
    └── Completed / Superseded

while:

Trust Lifecycle
    │
    ├── UNRESOLVED
    ├── EVALUATING
    ├── WAITING
    ├── BLOCKED
    └── READY

and:

Execution Lifecycle
    │
    ├── Not Started
    ├── EXECUTING
    ├── COMPLETED
    └── FAILED

An implementation may represent these using separate state models or coordinated lifecycle structures.

The semantic distinction must remain.

⸻

54. Composite Intents

Composite Intents contain multiple semantic or executable components.

For:

Intent = A + B + C

Trust should evaluate the applicable requirements of each component and derive the composite result according to deterministic composition semantics.

For an atomic composite:

A = READY
B = READY
C = BLOCKED

then:

Composite Trust = BLOCKED

unless the Intent explicitly permits partial execution.

Noema must not infer permission for partial execution.

⸻

55. Partial Execution

If an Intent explicitly permits partial execution, its components may progress independently.

Example:

A → EXECUTING
B → WAITING
C → READY

The permission for this behavior must be explicit in the Intent semantics or governing Contract.

Noema must not assume that a composite Intent may be partially executed merely because some components are READY.

⸻

56. Trust and Auditability

Trust decisions must be reconstructible without requiring the Model to remember what it did.

The system should preserve, where applicable:

* Intent version
* Validation result
* Evidence references
* Policy versions
* Authorization result
* Risk evaluation
* Constraint results
* Capability result
* Context
* freshness state
* Trust requirements
* Trust decision
* decision reasons
* timestamp
* evaluation identifier

The purpose is deterministic reconstruction and auditability.

⸻

57. Validation Provenance

Every Validation result should be traceable to:

* rule
* rule version
* input
* Evidence
* Context
* timestamp
* result

Example:

Rule:
TRANSFER_AMOUNT_POSITIVE
Input:
amount = -500
Result:
INVALID

Validation must be explainable through structured provenance rather than requiring an LLM to fabricate a rationale.

⸻

58. Trust Provenance

Every significant Trust decision should identify the conditions and sources that established it.

Example:

Requirement:
SECONDARY_APPROVAL
Satisfied by:
Approval#A123
Approved by:
Actor#456
For:
Intent#789
Intent Version:
3

Trust provenance must remain tied to the specific Intent version and governing conditions.

⸻

59. State Transition Provenance

Every significant lifecycle transition should record:

* previous state
* event
* new state
* timestamp
* Intent version
* evaluation ID
* relevant Evidence
* reason

Conceptually:

T0:
UNRESOLVED
T1:
EVALUATING
T2:
WAITING_FOR_APPROVAL
T3:
EVALUATING
T4:
READY
T5:
EXECUTING

This creates a reconstructible lifecycle history.

⸻

60. Canonical State Transition Principles

Trust state may change only because of:

* a defined event
* a material condition change
* deterministic re-evaluation
* an explicit lifecycle transition

Trust must not change because:

* the Model “feels” more confident
* a random retry occurred
* a prompt was reformulated without changing Intent semantics
* an LLM generated a stronger explanation
* an unrecorded internal heuristic changed

Given:

Current State
+
Event
+
Current Conditions

the next state must be deterministic.

⸻

61. No Probabilistic Trust Transitions

The Trust State Machine must never contain transitions such as:

80% chance → READY

or:

Model confidence > 0.8 → READY

Trust transitions are governed by explicit predicates.

For example:

READY

requires a guard equivalent to:

allMandatoryRequirementsSatisfied

while:

WAITING_FOR_APPROVAL

requires conditions equivalent to:

approvalRequired
AND
approvalMissing

The exact implementation may differ, but the semantic guards must be explicit and deterministic.

⸻

62. Noema Is Not a Chatbot

A conversational interface may be one way humans interact with Noema.

It is not the definition of Noema.

Noema is concerned with:

intent → validation → trust → action → outcome

rather than:

prompt → response

The interface may eventually be:

* chat
* voice
* API
* embedded UI
* workflow
* agent
* application
* automation

The canonical abstraction remains independent of the presentation layer.

⸻

63. Noema Is Not an ERP, CRM, Database, or System of Record

Noema should not reproduce the functionality of every system it integrates with.

Its purpose is not to become another enterprise application.

Instead, Noema makes existing Capabilities intent-addressable while preserving the authority of the systems that own the underlying business domains.

Enterprise systems own domain capabilities and business truth.

Noema owns the intent-to-action boundary.

⸻

64. Noema Is Not an Unbounded Autonomous Agent

Noema may use agents internally.

It may employ:

* planning
* reasoning
* retrieval
* tool use
* decomposition
* workflow coordination
* other agentic mechanisms

But agentic behavior does not define the authority model.

The canonical authority model remains:

Intent
  ↓
Resolution
  ↓
Validation
  ↓
Trust
  ↓
Contract
  ↓
Execution

Agents operate inside these boundaries.

They do not define the boundaries.

⸻

65. Canonical Knowledge Has Authority

Not all information in the Noema repository is equally authoritative.

The repository distinguishes between:

Canon

Defines what Noema currently considers foundationally true.

Specification

Defines precise behavior, schemas, contracts, and semantics derived from the Canon.

Architecture

Defines how the current implementation realizes those Specifications.

Decision Records

Explain why important architectural or canonical decisions were made.

Research

Contains hypotheses, experiments, external findings, and ideas that may influence future decisions.

Reference Workflows

Demonstrate canonical concepts in real-world scenarios.

Strategy

Defines commercial and organizational direction.

These categories must not be silently conflated.

Research may challenge the Canon.

It does not become Canon automatically.

⸻

66. The Canon Can Change, but Not Casually

The Canon is authoritative, but it is not immutable.

A foundational principle may change when:

* evidence invalidates it
* implementation reveals a fundamental contradiction
* a new requirement exposes a missing abstraction
* the commercial or technical model changes materially

Changes to the Canon must be deliberate.

A canonical change should normally include:

1. the principle being changed
2. the reason for the change
3. evidence supporting the change
4. affected Specifications
5. affected Contracts
6. affected implementations
7. migration implications
8. an ADR documenting the decision

The Canon must not silently drift.

⸻

67. Canonical Language Must Be Precise

Noema’s terminology is part of its architecture.

The following concepts must not be treated as interchangeable:

* Intent
* Resolution
* Validation
* Evidence
* Context
* Trust
* Confidence
* Authorization
* Permission
* Policy
* Risk
* Capability
* Constraint
* Action
* Contract
* Execution
* Outcome
* State

In particular:

Resolution ≠ Validation
Validation ≠ Trust
Trust ≠ Authorization
Trust ≠ Confidence
Capability ≠ Permission
Execution ≠ Outcome
Business State ≠ Intent State

The canonical glossary is therefore normative.

⸻

68. The First Workflow Is a Proof, Not the Product

Noema’s first commercial workflow may focus on a narrow enterprise problem such as card renewal.

That workflow exists to prove the underlying system.

The workflow should demonstrate that Noema can:

1. understand a real human objective
2. resolve its meaning
3. acquire relevant Context
4. distinguish established meaning from ambiguity
5. ask for clarification when necessary
6. deterministically validate the resulting Intent
7. establish relevant Evidence
8. deterministically evaluate Trust
9. distinguish authorization, Policy, Capability, Risk, and Constraints
10. select an applicable Capability
11. create and enforce a typed Execution Contract
12. interact with existing systems
13. verify the resulting Outcome
14. maintain an auditable Intent lifecycle
15. stop and request human intervention when required

The workflow should constrain Noema enough to make the system measurable without defining the limits of the platform.

⸻

69. The Fundamental Noema Loop

The canonical lifecycle is:

EXPRESS
   ↓
INTERPRET
   ↓
RESOLVE
   ↓
CONTEXTUALIZE
   ↓
VALIDATE
   ↓
EVALUATE TRUST
   ↓
PLAN / SELECT ACTION
   ↓
CONTRACT
   ↓
EXECUTE
   ↓
VERIFY
   ↓
OUTCOME

At any point where Noema cannot safely proceed, the lifecycle may transition to:

CLARIFY
WAIT
BLOCK
ESCALATE

The system must not skip a required state merely to produce an apparently successful outcome.

⸻

70. The Core Invariants

The following are foundational Noema invariants.

Invariant 1

Noema owns Intent state, not authoritative business state.

Invariant 2

Human language is input to Intent resolution, not the executable representation of Intent.

Invariant 3

Model confidence is not execution authority.

Invariant 4

Noema must not guess when Intent semantics are materially ambiguous.

Invariant 5

Resolution, Validation, Trust, and Execution are distinct semantic layers.

Invariant 6

Validation is deterministic.

Invariant 7

Unknown information must not be treated as established information.

Invariant 8

Trust evaluation is deterministic with respect to its governing inputs and versions.

Invariant 9

Unknown mandatory Trust conditions cannot produce READY.

Invariant 10

Authorization does not imply Trust.

Invariant 11

Policy satisfaction does not imply Trust.

Invariant 12

Capability availability does not imply Trust.

Invariant 13

Risk acceptance does not imply Trust.

Invariant 14

Validation does not authorize or execute Actions.

Invariant 15

Execution occurs only through explicit Capabilities and Contracts.

Invariant 16

Capability and permission are distinct.

Invariant 17

Autonomy is bounded by explicit authority, Policy, Capability, and Contract.

Invariant 18

WAITING and BLOCKED are semantically distinct.

Invariant 19

Material changes to Trust inputs require re-evaluation.

Invariant 20

Material Intent changes require a new or re-established Trust evaluation.

Invariant 21

Trust decisions must be traceable to their inputs, requirements, rules, and Evidence.

Invariant 22

READY does not guarantee execution success.

Invariant 23

Execution outcomes do not retroactively establish that a Trust decision was valid.

Invariant 24

Enterprise systems remain authoritative for their business domains.

Invariant 25

Human intervention is a valid lifecycle state.

Invariant 26

Important execution conditions must be represented as explicit state.

Invariant 27

The conversational interface is not the Noema abstraction.

Invariant 28

Noema must fail closed for consequential execution when mandatory conditions cannot be established.

Invariant 29

Fail-closed uncertainty may result in WAITING rather than permanent denial where the condition is recoverable.

Invariant 30

Research may challenge the Canon but does not become Canon automatically.

Invariant 31

Canonical concepts must have precise, stable definitions.

⸻

71. The Canonical Distinction

The canonical Noema chain is:

Model
"What might the Actor mean?"
        ↓
Intent
"What does the Actor mean?"
        ↓
Resolution
"Is that meaning sufficiently established?"
        ↓
Validation
"Is the Intent well-formed and applicable?"
        ↓
Evidence
"What facts support the relevant conditions?"
        ↓
Authorization
"May the Actor perform the Action?"
        ↓
Policy
"Under what rules may it happen?"
        ↓
Risk
"What controls are required?"
        ↓
Capability
"Can it be performed?"
        ↓
Constraints
"What limits must hold?"
        ↓
Context
"Is it valid here and now?"
        ↓
Trust
"May this Intent cross the execution boundary?"
        ↓
Contract
"What exact Action is authorized for execution?"
        ↓
Execution
"Perform the Action."
        ↓
Outcome
"What actually happened?"

The ordering of individual Trust inputs may vary according to dependencies, but the semantic distinctions must remain.

⸻

72. The Ultimate Abstraction

The simplest expression of Noema is:

Human Intent
     ↓
Meaning
     ↓
Validation
     ↓
Trust
     ↓
Action
     ↓
Outcome

Everything else in Noema exists to make those transitions reliable.

The long-term objective is not merely to make AI better at understanding language.

It is to create a standard infrastructure for expressing, validating, trusting, and executing human Intent across software systems without surrendering control, authority, or deterministic governance to probabilistic models.

⸻

73. Canonical Test

Whenever a proposed feature, architecture decision, abstraction, integration, or workflow is introduced, the following questions should be answerable:

1. What Intent does this represent?
2. What semantic state does Noema own?
3. What business state remains owned by another system?
4. What establishes the meaning of the Intent?
5. What makes the Intent sufficiently resolved?
6. What makes the Intent structurally and semantically valid?
7. What Evidence establishes the relevant conditions?
8. What authority permits the Action?
9. What Policies govern it?
10. What Risk controls apply?
11. What Capability performs it?
12. What Constraints must hold?
13. What makes the Intent trusted?
14. What Contract governs execution?
15. What happens if information is unknown?
16. What happens if the Intent is ambiguous?
17. What happens if Trust requirements are incomplete?
18. What happens if a previously READY Intent becomes invalid?
19. What happens if execution fails?
20. What happens if execution produces an unknown outcome?
21. How is the Outcome verified?
22. What provenance is retained?
23. What happens when a human must intervene?
24. Which system remains authoritative for business truth?
25. Does the proposal strengthen or violate the canonical boundaries of Noema?

If these questions cannot be answered, the proposal is not yet sufficiently defined to become part of the Noema system.

⸻

74. The Canon in One Sentence

Noema is the deterministic intent-to-action boundary that transforms probabilistically understood human Intent into validated, trusted, and contractually executable Actions across existing systems while preserving explicit authority, contextual governance, provenance, and ownership of business truth.

This version makes the **new canonical separation** explicit:
**Interpretation → Resolution → Validation → Trust → Contract → Execution → Outcome**
and prevents the three Trust-folder documents from being collapsed into one concept. In particular, `CANON.md` now treats **Validation as its own deterministic layer**, **Trust as the execution-eligibility decision**, and **Execution/Outcome as separate lifecycles** rather than treating `TRUSTED`, `READY`, and `SUCCEEDED` as interchangeable states.