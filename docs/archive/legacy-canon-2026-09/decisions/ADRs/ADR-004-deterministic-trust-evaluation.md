ADR-004 — Deterministic Trust Evaluation

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Trust
Canonical Path: decisions/ADRs/ADR-004-deterministic-trust-evaluation.md

⸻

1. Context

Noema uses probabilistic AI systems to interpret human expression, resolve intent, retrieve context, and propose actions.

Those systems are useful precisely because they can operate under ambiguity and incomplete information. However, probabilistic inference cannot by itself establish whether an Intent is permitted to cross the execution boundary.

Noema therefore requires a deterministic Trust mechanism that evaluates whether a resolved and validated Intent satisfies the conditions required for execution.

The distinction is foundational:

The Model may propose.
The Trust Engine must establish.

A model’s confidence, reasoning, ranking, or probability must not silently become execution authority.

⸻

2. Problem

Without deterministic Trust evaluation, Noema risks allowing execution decisions to depend on:

* model confidence
* prompt formulation
* model version
* stochastic generation
* implicit assumptions
* undocumented business rules
* incomplete evidence
* transient contextual interpretation
* probabilistic judgments about authorization or policy

This would make execution authority dependent on a probabilistic component whose behavior is not itself a sufficient authorization mechanism.

It would also make Trust difficult to audit and reproduce.

For consequential Actions, Noema must instead be able to answer:

1. What Intent was evaluated?
2. What evidence was available?
3. What authorization applied?
4. What policies applied?
5. What constraints applied?
6. What capabilities were available?
7. What contextual conditions existed?
8. What risk controls applied?
9. Which rules produced the decision?
10. Why was the Intent READY, WAITING, or BLOCKED?

⸻

3. Decision

Noema will use a deterministic Trust evaluation layer as the authoritative mechanism for establishing execution eligibility.

Trust evaluation MUST be based on explicit:

* Intent state
* validation result
* evidence
* authorization
* policy
* capability
* constraints
* context
* risk controls
* freshness requirements
* rule versions

The Trust Engine MUST NOT use model confidence as a direct authorization predicate.

Conceptually:

Resolved Intent
      ↓
Validation
      ↓
Trust Evaluation
      │
      ├── WAITING
      ├── BLOCKED
      └── READY

The resulting Trust state determines whether the Intent is eligible to cross the execution boundary.

⸻

4. Determinism Requirement

Given the same:

Intent
Context
Evidence
Authorization
Policy
Capability
Constraints
Risk Rules
Rule Versions

the Trust Engine must produce the same Trust decision.

Conceptually:

TrustEvaluation(
    Intent,
    Context,
    Evidence,
    Authorization,
    Policy,
    Capability,
    Constraints,
    Risk,
    Rules
)
→
Deterministic Trust Result

A Trust decision must therefore not change merely because:

* an LLM was sampled differently
* a prompt was reformulated without changing the canonical Intent
* a model produced a different confidence score
* a retry produced different wording
* a stronger explanation was generated

Material changes to the underlying inputs may legitimately cause a different result.

⸻

5. Trust Is Not Model Confidence

Model confidence and Trust represent different concepts.

Model confidence

Describes the degree to which a probabilistic model supports an interpretation or prediction.

Trust

Describes whether Noema has established sufficient deterministic grounds for the Intent to proceed toward execution.

Therefore:

Model confidence ≠ Trust

And:

High model confidence
        ≠
READY

Likewise:

Low model confidence
        ≠
BLOCKED

Low confidence may instead require clarification, additional evidence, or another evaluation step.

⸻

6. Trust Inputs

The Trust Engine may evaluate the following categories.

6.1 Intent

The canonical Intent being evaluated.

The Intent must already have sufficient semantic resolution for the Trust Engine to evaluate it meaningfully.

6.2 Validation

Validation establishes that the Intent is structurally and semantically suitable for evaluation.

Trust does not replace Validation.

Validation:
"Is this Intent valid?"
Trust:
"May this valid Intent proceed?"

6.3 Evidence

Evidence establishes relevant facts required by Trust predicates.

Evidence may include:

* identity information
* authorization records
* resource state
* policy information
* approvals
* confirmations
* contextual facts
* external system state

Evidence must be appropriately attributable and sufficiently fresh for the decision.

6.4 Authorization

Authorization establishes whether the Actor is permitted to cause the requested Action within the applicable scope.

6.5 Policy

Policies establish governance requirements and prohibitions.

For example:

Transfer > ₦5M
        ↓
Approval required

The Intent may remain valid while Trust remains:

WAITING_FOR_APPROVAL

6.6 Capability

Capability establishes whether the required execution operation exists and is available to the relevant execution consumer.

Capability does not itself establish permission.

6.7 Constraints

Constraints establish explicit conditions that must hold for execution.

6.8 Context

Context may affect whether the Action is currently permissible.

6.9 Risk Controls

Risk rules may establish conditions under which an Action requires additional controls, approval, or blocking.

⸻

7. Trust Result

The Trust Engine should produce a structured result rather than a bare boolean.

Conceptually:

TrustResult {
    state
    reasons
    satisfied_requirements
    missing_requirements
    blocking_conditions
    evidence
    evaluation_id
    rule_versions
    valid_until
}

The exact schema is defined elsewhere.

The canonical principle is that a Trust decision must be explainable through explicit predicates and evidence.

⸻

8. Canonical Trust States

The Trust Engine participates in the Trust State Machine.

The principal Trust states are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Execution states such as:

EXECUTING
COMPLETED
FAILED

may be represented separately as defined by the Trust State Machine and execution architecture.

The important distinction is:

READY ≠ EXECUTING
READY ≠ COMPLETED
READY ≠ SUCCESS

READY means that Noema has established execution eligibility.

It does not mean that execution has occurred or will necessarily succeed.

⸻

9. Waiting vs Blocking

Trust evaluation must preserve the distinction between incomplete conditions and prohibited conditions.

Waiting

A required condition is not yet satisfied but may become satisfied.

Examples:

WAITING_FOR_APPROVAL
WAITING_FOR_CONFIRMATION
WAITING_FOR_EVIDENCE
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CAPABILITY

Blocking

A condition currently prohibits execution.

Examples:

BLOCKED_BY_AUTHORIZATION
BLOCKED_BY_POLICY
BLOCKED_BY_CONSTRAINT
BLOCKED_BY_RISK
BLOCKED_BY_SCOPE

Therefore:

Not yet
   ≠
No

⸻

10. Unknown Must Not Become Trusted

An unavailable dependency must not be interpreted as a positive Trust condition.

For example:

Authorization service unavailable

does not establish:

Authorization = granted

The correct result is an unresolved condition requiring appropriate handling.

For consequential Actions, this must result in a non-READY Trust state.

Conceptually:

Required Trust dependency unavailable
              ↓
          EVALUATING
              ↓
       WAITING / BLOCKED

Never:

Dependency unavailable
        ↓
      READY

⸻

11. Fail-Closed Principle

Noema must fail closed when mandatory conditions required for execution cannot be established.

This does not mean every unavailable dependency must always produce BLOCKED.

Depending on the semantics, the result may be:

WAITING

or:

BLOCKED

But it must not be:

READY

unless all mandatory Trust predicates have been satisfied.

⸻

12. Trust Re-Evaluation

Trust is not a one-time decision.

A previously READY Intent may become invalid because:

* authorization was revoked
* authorization expired
* policy changed
* evidence became stale
* risk conditions changed
* resource state changed
* capability became unavailable
* context changed
* constraints changed
* the Intent itself changed

Therefore:

READY
   ↓
material condition changes
   ↓
EVALUATING
   ↓
WAITING / BLOCKED / READY

The Trust Engine must re-evaluate rather than assuming that prior Trust remains permanently valid.

⸻

13. Trust Expiration

Trust decisions may have explicit validity periods.

Example:

READY
valid_until = 10:30

After expiry:

READY
  ↓
expired
  ↓
EVALUATING

The subsequent evaluation may result in:

WAITING
BLOCKED
READY

depending on the current conditions.

⸻

14. Material Events

Material events should trigger Trust re-evaluation when they affect a Trust dependency.

Examples include:

intent.resolved
intent.updated
evidence.added
evidence.expired
authorization.granted
authorization.revoked
approval.granted
approval.expired
policy.changed
risk.changed
capability.available
capability.unavailable
constraint.changed
context.changed
trust.expired

Not every event must invalidate every Intent.

Re-evaluation should therefore be dependency-aware.

⸻

15. Dependency-Aware Evaluation

Trust dependencies should be identifiable where practical.

Conceptually:

Policy P1
   ↓
 ┌─┼────────┐
 ↓ ↓        ↓
I1 I2       I3

If P1 changes, only Intents depending upon P1 need to be reconsidered.

This permits Trust evaluation to scale without unnecessarily reevaluating unrelated Intents.

⸻

16. Deterministic Guards

Trust transitions must be governed by explicit predicates.

For example:

READY

requires a guard conceptually equivalent to:

allMandatoryRequirementsSatisfied

While:

WAITING_FOR_APPROVAL

requires conditions such as:

approvalRequired
AND
approvalMissing

And:

BLOCKED_BY_POLICY

requires conditions such as:

policyProhibitsAction

The exact predicate definitions belong to the Trust specification and applicable policies.

⸻

17. No Probabilistic State Transitions

Trust state transitions must not be defined as probabilistic thresholds.

Invalid:

model_confidence > 0.8
        ↓
READY

Invalid:

80% confidence
        ↓
execute

Valid:

Required predicates satisfied
        ↓
READY

The State Machine must operate on explicit conditions rather than probabilistic confidence thresholds.

⸻

18. Trust and the Execution Boundary

READY establishes eligibility.

It does not itself execute the Action.

The canonical boundary is:

Trust Evaluation
      ↓
READY
      ↓
Execution Contract
      ↓
Consumer Acceptance
      ↓
EXECUTING

The Trust Engine does not perform the business Action.

The execution consumer remains responsible for executing the Action through its defined interface.

⸻

19. Execution Consumer Validation

The execution consumer may perform additional authoritative checks.

For example:

T1
Noema validates balance
T2
Trust becomes READY
T3
Account balance changes
T4
Execution consumer checks current balance
T5
Execution rejected

This does not necessarily mean that the earlier Trust decision was incorrect.

Business state may change between evaluation and execution.

Therefore the execution consumer remains authoritative over the final business-state mutation.

⸻

20. Trust and Race Conditions

Consequential Actions may encounter time-of-check/time-of-use conditions.

Conceptually:

T1 → Validation
T2 → Trust
T3 → Contract
T4 → Execution

A condition established at T2 may no longer hold at T4.

Noema must therefore avoid treating Trust evaluation as a guarantee of business-state success.

Where required, execution consumers should perform final authoritative checks.

⸻

21. Trust Provenance

Every material Trust evaluation should be reconstructible.

The evaluation should conceptually retain:

evaluation_id
intent_version
timestamp
trust_state
input references
evidence references
policy versions
authorization result
capability result
constraint results
risk results
decision reasons
valid_until

This enables Noema to answer:

Why was this Intent trusted at this point in time?

without relying on hidden model reasoning.

⸻

22. Trust History

Trust state transitions should be auditable.

Example:

T0  UNRESOLVED
T1  EVALUATING
T2  WAITING_FOR_APPROVAL
T3  EVALUATING
T4  READY
T5  EXECUTING

Each transition should have an explicit cause.

Conceptually:

previous_state
+
event
+
current_conditions
=
new_state

⸻

23. Deterministic Transition Principle

Given:

Current State
+
Event
+
Current Conditions

the resulting state must be deterministic.

For example:

WAITING_FOR_APPROVAL
+
approval.received
+
all other Trust conditions satisfied
=
READY

The result must not be:

maybe READY

or:

READY because the model appears confident

⸻

24. Separation of Trust and Outcome

Trust determines execution eligibility.

Execution determines what happened.

Therefore:

Trust
  ↓
Execution Eligibility
  ↓
Execution
  ↓
Outcome

not:

Trust
  ↓
Outcome

A successful outcome does not prove that the original Trust decision was correct.

Likewise, an execution failure does not automatically prove that the Trust decision was invalid.

⸻

25. Composite Intents

Composite Intents require deterministic aggregation.

For example:

A = READY
B = WAITING_FOR_APPROVAL
C = READY

For an atomic composite Action:

Composite Trust = WAITING

If:

B = BLOCKED

then:

Composite Trust = BLOCKED

The aggregation semantics must be defined by the Intent’s execution semantics.

Noema must not infer permission for partial execution merely because some components are trusted.

⸻

26. Partial Execution

Partial execution must be explicit.

If an Intent permits independent execution:

A → EXECUTING
B → WAITING
C → READY

may be valid.

If the Intent requires atomic execution, the composite must not proceed until the required components satisfy the applicable Trust conditions.

Partial execution must therefore be an explicit semantic property rather than an implementation convenience.

⸻

27. Human Approval

Human approval is a Trust input, not merely a conversational event.

Example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING
        ↓
READY

The approval should be represented as attributable evidence with appropriate scope and validity.

Receiving approval does not bypass the rest of Trust evaluation.

⸻

28. Clarification

Clarification changes the Intent or supplies information necessary for evaluation.

Conceptually:

UNRESOLVED
     ↓
clarification.requested
     ↓
clarification.received
     ↓
updated Intent
     ↓
EVALUATING

The Trust Engine must evaluate the resulting Intent rather than assuming that clarification automatically makes it trusted.

⸻

29. Trust and Autonomy

Trust does not by itself determine whether autonomous execution is permitted.

For example:

Trust = READY

may coexist with:

Policy = human approval required for autonomous execution

In such a case, execution remains subject to the applicable autonomy control.

The authority model must therefore distinguish:

Trust eligibility

from:

Autonomous execution permission

where the architecture requires that distinction.

⸻

30. Relationship to Validation

The canonical sequence is:

Intent
  ↓
Validation
  ↓
Trust Evaluation

Validation establishes:

Is this Intent structurally and semantically valid?

Trust establishes:

May this valid Intent proceed?

Therefore:

VALID ≠ TRUSTED

A valid Intent can remain:

WAITING

or:

BLOCKED

⸻

31. Relationship to Capability

Capability and Trust are distinct.

Capability asks:

Can the system perform this Action?

Trust asks:

Has Noema established sufficient grounds for this Intent to proceed?

A capability may exist while execution remains prohibited.

Conversely, an Intent may be permitted in principle while the required capability is temporarily unavailable.

⸻

32. Relationship to Authorization

Authorization is one of the conditions Trust may evaluate.

The distinction is:

Authorization
    ↓
Is the Actor permitted?
Trust
    ↓
Have all conditions required for execution eligibility been satisfied?

Authorization is therefore necessary in many cases but is not necessarily sufficient for Trust.

⸻

33. Relationship to Policy

Policy establishes governance requirements.

A policy may:

* permit an Action
* prohibit an Action
* require approval
* impose limits
* require additional evidence
* require human intervention

Trust evaluates the applicable policy conditions.

A policy requirement should not automatically be treated as an invalid Intent when the requirement can still be satisfied.

⸻

34. Relationship to Risk

Risk controls may produce additional Trust requirements.

For example:

Risk threshold exceeded
        ↓
additional approval required

or:

Risk condition prohibited
        ↓
BLOCKED

The exact risk semantics belong to the applicable Trust and policy specifications.

The Trust Engine must not substitute a model’s subjective risk estimate for an explicit risk control where deterministic enforcement is required.

⸻

35. Relationship to Evidence

Evidence supports Trust predicates.

Evidence must be:

* attributable
* relevant
* sufficiently fresh
* applicable to the Intent
* traceable to its source where required

Evidence existing somewhere in the system does not automatically establish that it is sufficient for the Trust decision.

⸻

36. Rule Versioning

Trust rules can evolve.

Therefore Trust evaluations must identify the applicable rule and policy versions.

Conceptually:

rule_id
rule_version
policy_id
policy_version

This allows historical decisions to be reconstructed even after the governing rules change.

⸻

37. Trust Reproducibility

A historical Trust decision should be reproducible to the extent that the relevant:

* Intent version
* evidence
* context
* authorization state
* policy version
* capability information
* rule versions

remain available.

Reproducibility does not require reproducing hidden model reasoning.

It requires reconstructing the deterministic Trust inputs and predicates.

⸻

38. Side Effects

Trust evaluation should avoid hidden business side effects.

A Trust evaluation may produce system-level effects such as:

* recording an evaluation
* emitting a Trust event
* creating a requirement
* invalidating a stale execution contract
* requesting additional approval

But Trust evaluation must not itself perform the requested business Action.

⸻

39. Canonical Trust Flow

                Resolved Intent
                       │
                       ▼
                  Validation
                       │
                       ▼
                 EVALUATING
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       WAITING      BLOCKED        READY
                                     │
                                     ▼
                              Execution Contract
                                     │
                                     ▼
                               Consumer Accepts
                                     │
                                     ▼
                                  EXECUTING

At any point, a material Trust dependency change may cause:

READY
  ↓
EVALUATING
  ↓
WAITING / BLOCKED / READY

⸻

40. Consequences

Positive consequences

This decision provides:

* deterministic execution eligibility
* separation between AI inference and authority
* auditable Trust decisions
* reproducible Trust evaluation
* explicit handling of uncertainty
* explicit handling of authorization and policy
* safer recovery from changing conditions
* clearer separation between Trust and execution
* stronger interoperability with enterprise systems

Costs

This decision requires:

* explicit Trust predicates
* structured evidence
* rule and policy versioning
* Trust state management
* dependency tracking
* re-evaluation mechanisms
* audit infrastructure
* careful definition of authorization and policy semantics

The additional structure is intentional.

Noema’s purpose is not merely to generate actions. It is to establish the conditions under which actions may safely cross the execution boundary.

⸻

41. Rejected Alternatives

41.1 Model Confidence as Trust

Rejected.

A probabilistic confidence score is not a deterministic authorization mechanism.

41.2 LLM-Based Trust Decision

Rejected as the authoritative Trust mechanism.

An LLM may assist with interpretation or proposal, but it cannot be the final deterministic authority for consequential execution.

41.3 Boolean Trust

Rejected as insufficient.

A simple:

trusted = true / false

cannot adequately represent:

* waiting
* missing evidence
* pending approval
* temporary capability unavailability
* policy-based blocking
* expiration
* re-evaluation

41.4 Permanent Trust

Rejected.

Trust is conditional and time-dependent.

41.5 Trust Implied by Validation

Rejected.

A valid Intent may still lack authorization, approval, capability, or other required conditions.

⸻

42. Invariants Established by This ADR

Invariant 1

Trust evaluation is deterministic.

Invariant 2

Model confidence is not execution authority.

Invariant 3

Unknown mandatory conditions cannot establish READY.

Invariant 4

Trust must distinguish waiting from blocking.

Invariant 5

Trust decisions may be invalidated by material changes.

Invariant 6

Trust transitions are driven by explicit events and deterministic conditions.

Invariant 7

A READY Intent is eligible for execution but has not necessarily executed.

Invariant 8

Trust does not guarantee successful execution.

Invariant 9

Trust evaluation does not execute business Actions.

Invariant 10

Trust decisions must be auditable and attributable to explicit inputs and rules.

Invariant 11

Trust rules must be versionable.

Invariant 12

A previously trusted Intent may require re-evaluation.

⸻

43. Relationship to Other Canonical Documents

This ADR establishes the foundational decision that Trust evaluation is deterministic.

The detailed semantics should remain distributed according to Noema’s canonical document hierarchy:

CANON.md
   ↓
Trust Model
   ↓
Trust Engine
   ↓
Trust State Machine
   ↓
Validation
   ↓
Action / Execution Contracts

This ADR records why deterministic Trust evaluation is a foundational architectural decision.

The relevant specifications define how that decision is expressed operationally.

⸻

44. Final Decision

Noema will treat Trust as a deterministic control layer between probabilistic intent understanding and executable action.

The Trust Engine may consume probabilistically produced Intent representations and contextual evidence, but its execution-eligibility decision must be established through explicit, deterministic conditions.

The canonical boundary is:

Probabilistic Understanding
           ↓
Canonical Intent
           ↓
Deterministic Validation
           ↓
Deterministic Trust Evaluation
           ↓
Execution Eligibility
           ↓
Explicit Action Contract
           ↓
Execution

The governing principle is:

Noema does not execute because the Model is confident. Noema executes only when the deterministic Trust conditions required for execution have been established.