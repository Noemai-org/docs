> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-013 — Bounded Autonomy

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Trust / Autonomy
Canonical Path: decisions/ADRs/ADR-013-bounded-autonomy.md

⸻

1. Decision

Noema autonomy shall be explicitly bounded by authority, policy, capability, contract, constraints, risk controls, and human-intervention requirements.

Noema must never interpret a general instruction such as:

“Act autonomously.”

as unrestricted authority to determine what it may do.

Autonomy describes how much execution can proceed without additional human intervention. It does not independently establish whether execution is permitted.

The canonical authority model is:

Intent
   ↓
Understanding
   ↓
Validation
   ↓
Trust
   ↓
Authority
   ↓
Capability
   ↓
Execution Contract
   ↓
Execution

Agents, models, planners, and other probabilistic components operate within these boundaries.

They do not define the boundaries.

⸻

2. Context

Noema is intended to enable human intent to become executable across existing software systems.

This necessarily introduces autonomous behavior.

Noema may need to:

* interpret intent
* gather context
* retrieve evidence
* resolve entities
* select capabilities
* construct execution plans
* determine whether clarification is required
* prepare execution contracts
* invoke authorized capabilities
* monitor execution
* verify outcomes
* recover from defined failures

Without explicit boundaries, these capabilities could allow a model or agent to progressively expand the scope of an action beyond what the Actor actually authorized.

The central architectural problem is therefore not whether Noema should be autonomous.

It is:

Under what explicit conditions may Noema act without additional human intervention?

⸻

3. Problem Statement

Probabilistic systems can generate actions that appear reasonable while exceeding the authority established by the Intent.

For example, a user may authorize:

Renew my card.

A system might infer additional actions such as:

* changing the delivery address
* changing account preferences
* cancelling the existing card
* ordering additional cards
* contacting unrelated parties

Those actions may be operationally related to the objective but are not automatically authorized merely because they could contribute to achieving it.

Therefore:

Useful
≠
Authorized

and:

Autonomous
≠
Unrestricted

⸻

4. Decision Principles

Noema adopts the following principles.

4.1 Autonomy Is Bounded

Every autonomous action must operate within explicit boundaries.

Those boundaries may include:

* Actor authority
* Intent scope
* Policy
* Capability
* Action Contract
* Constraints
* Risk thresholds
* Resource limits
* Temporal limits
* Approval requirements
* Confirmation requirements
* Human-intervention requirements

⸻

4.2 Trust Precedes Autonomous Execution

Autonomy cannot bypass Trust.

The canonical sequence remains:

Intent
   ↓
Validation
   ↓
Trust Evaluation
   ↓
Execution Eligibility
   ↓
Execution

A model or agent cannot establish its own Trust merely by deciding that an action is safe.

⸻

4.3 Capability Does Not Establish Authority

The existence of a capability does not grant permission to invoke it.

For example:

Capability:
cancel_account

does not imply:

Actor may cancel account

Authority must be established independently.

⸻

4.4 Intent Scope Constrains Autonomy

Autonomous execution must remain within the semantic scope of the resolved Intent.

Noema must not silently expand the Intent because an additional action appears useful.

Conceptually:

Resolved Intent
      ↓
Permitted Scope
      ↓
Candidate Actions
      ↓
Authorized Actions

Actions outside the established scope require a new evaluation and, where necessary, clarification or approval.

⸻

4.5 Human Intervention Is a Valid Outcome

Autonomy does not require Noema to complete every Intent without human involvement.

Noema may legitimately transition to:

WAITING
BLOCKED
CLARIFICATION_REQUIRED
APPROVAL_REQUIRED
CONFIRMATION_REQUIRED
HUMAN_INTERVENTION_REQUIRED

Stopping is preferable to exceeding established authority.

⸻

5. Autonomy Boundary

The canonical autonomy boundary is:

                 Human
                   │
                   ▼
                Intent
                   │
                   ▼
             Interpretation
                   │
                   ▼
               Resolution
                   │
                   ▼
              Validation
                   │
                   ▼
                 Trust
                   │
          ┌────────┴────────┐
          │                 │
       Allowed          Not Allowed
          │                 │
          ▼                 ▼
      Autonomy         WAIT / BLOCK
          │
          ▼
    Action Contract
          │
          ▼
       Execution

Autonomy exists only inside the permitted execution region.

⸻

6. Autonomous Action Requirements

Before an autonomous Action may cross the execution boundary, Noema must establish, as applicable:

1. The Intent is sufficiently resolved.
2. The Intent is structurally and semantically valid.
3. The Action is within Intent scope.
4. Required evidence is available and sufficiently fresh.
5. Required authorization is established.
6. Applicable policy permits the Action.
7. Required capabilities are available.
8. Constraints are satisfied.
9. Risk remains within the permitted boundary.
10. Required approvals or confirmations have been obtained.
11. The Action Contract is valid.
12. No material condition has invalidated the Trust decision.

Conceptually:

Resolved
   AND
Valid
   AND
In Scope
   AND
Authorized
   AND
Policy Compliant
   AND
Capability Available
   AND
Constraints Satisfied
   AND
Risk Permitted
   AND
Required Approval/Confirmation
   AND
Contract Valid
        ↓
Autonomous Execution Eligible

⸻

7. Autonomy Levels

Noema may represent autonomy using explicit levels where required by implementation.

A conceptual model is:

LEVEL 0 — No Autonomous Execution

No execution occurs without human action.

LEVEL 1 — Assisted Execution

Noema prepares an action but requires human confirmation.

LEVEL 2 — Bounded Autonomous Execution

Noema may execute within explicitly defined authority and policy boundaries.

LEVEL 3 — Conditional Autonomy

Noema may execute automatically while defined conditions remain satisfied, with escalation when those conditions fail.

The exact numerical taxonomy is implementation-dependent.

The canonical principle is that autonomy level must be explicit rather than inferred from model behavior.

⸻

8. Autonomy Is Not a Trust State

Autonomy and Trust are related but distinct.

Trust answers:

May this Intent proceed toward execution?

Autonomy answers:

May Noema proceed without additional human intervention within the established boundaries?

Therefore:

Trust = READY

does not necessarily mean:

Autonomous execution permitted

For example:

Trust:
READY
Policy:
Human confirmation required

The resulting state may be:

WAITING_FOR_CONFIRMATION

⸻

9. Autonomy Is Not Model Confidence

Model confidence must never be used as an autonomous authority threshold.

Invalid:

Model confidence > 0.95
        ↓
Execute autonomously

Canonical:

Model
  ↓
Candidate Intent / Action
  ↓
Deterministic Validation
  ↓
Trust
  ↓
Authority + Policy + Contract
  ↓
Autonomous Execution Eligibility

A highly confident model output can still be outside the permitted autonomy boundary.

⸻

10. Scope Expansion

Noema must distinguish between:

Scope-preserving actions

Actions necessary to fulfill the established Intent and explicitly permitted by its contracts and policies.

Scope-expanding actions

Actions that introduce a materially different objective, resource, authority, or side effect.

Scope expansion must not occur implicitly.

Example:

Intent:
Replace expired card

does not automatically authorize:

Change billing address

even if the system believes that doing so would improve the replacement process.

If the additional action is necessary, Noema must establish the appropriate authorization and semantic basis rather than silently extending the Intent.

⸻

11. Bounded Planning

Planning may be autonomous within the permitted boundary.

For example:

Intent:
Renew card

Noema may determine a sequence such as:

Check card status
      ↓
Verify eligibility
      ↓
Create renewal request
      ↓
Submit request
      ↓
Verify result

provided those operations are covered by the relevant capabilities, authority, policy, constraints, and contracts.

Planning does not create new authority.

⸻

12. Agentic Components

Noema may use agentic components for:

* planning
* retrieval
* reasoning
* tool selection
* context acquisition
* decomposition
* recovery planning
* clarification generation

However, agents remain subordinate to Noema’s authority model.

The relationship is:

Noema Boundary
       │
       ▼
Agent
       │
       ├── Reason
       ├── Retrieve
       ├── Plan
       └── Propose
       │
       ▼
Deterministic Controls
       │
       ▼
Execution Contract
       │
       ▼
Execution

The agent cannot redefine the boundary in which it operates.

⸻

13. Human Approval

Where policy or risk requires human approval, autonomy terminates at the approval boundary.

Example:

Transfer
   ↓
Trust Evaluation
   ↓
Approval Required
   ↓
WAITING_FOR_APPROVAL
   ↓
Human Approval
   ↓
Re-evaluation
   ↓
READY

Approval should be treated as explicit evidence.

It must not be inferred from:

* silence
* previous approval
* conversational tone
* model confidence
* assumed user preference

unless an explicit policy establishes such behavior.

⸻

14. Human Confirmation

Confirmation is distinct from approval.

Confirmation may establish that the Actor understands and accepts a specific consequential action.

Example:

Action:
Delete account permanently
State:
WAITING_FOR_CONFIRMATION

A valid confirmation may transition the Intent back through Trust evaluation.

confirmation.received
        ↓
EVALUATING
        ↓
READY

⸻

15. Risk Boundaries

Autonomous execution should be bounded by explicit risk controls.

Risk controls may consider:

* financial magnitude
* data sensitivity
* reversibility
* external impact
* number of affected resources
* privilege level
* action criticality
* downstream consequences
* uncertainty
* policy-defined thresholds

Risk controls must be represented as explicit conditions rather than informal model judgment.

⸻

16. Reversibility

Autonomy may be constrained by whether an Action is reversible.

Conceptually:

Low-impact / reversible
        ↓
Potentially broader autonomy
High-impact / irreversible
        ↓
Stricter controls

The exact thresholds belong to policy and Trust specifications.

Noema must not independently determine that an irreversible action is acceptable merely because it appears useful.

⸻

17. Material Change Invalidates Autonomous Authority

Autonomous eligibility is not permanent.

A previously permitted Action may require re-evaluation when:

* policy changes
* authorization changes
* evidence expires
* context changes
* resource state changes
* capability changes
* risk changes
* Intent changes
* execution conditions change

Therefore:

AUTONOMOUSLY ELIGIBLE
        ↓
Material Change
        ↓
RE-EVALUATE

Noema must not continue autonomous execution based on stale authority.

⸻

18. Execution-Time Controls

Autonomy must remain bounded during execution, not only before execution.

Execution consumers may perform final checks against authoritative business state.

For example:

T1:
Trust = READY
T2:
Execution begins
T3:
Account state changed
T4:
Consumer rejects Action

The consumer remains authoritative for its business state.

Autonomous execution does not override the execution system’s final authoritative checks.

⸻

19. Failure and Escalation

When an autonomous process encounters a condition outside its authority boundary, it should not improvise.

Possible outcomes include:

WAITING
BLOCKED
CLARIFICATION_REQUIRED
APPROVAL_REQUIRED
HUMAN_INTERVENTION_REQUIRED
FAILED

The appropriate transition depends on the specific condition.

The key principle is:

Boundary violation must result in controlled state transition, not autonomous improvisation.

⸻

20. Partial Execution

Autonomy does not imply permission for partial execution.

For composite Intents:

A
B
C

Noema must know whether partial execution is permitted.

If partial execution is not explicitly authorized:

A = READY
B = BLOCKED
C = READY
Composite execution
        ↓
BLOCKED

If partial execution is explicitly permitted, the individual components may progress independently according to their own Trust and execution states.

⸻

21. Autonomy and Execution Contracts

The Execution Contract is the concrete boundary through which autonomous execution occurs.

Conceptually:

Trusted Intent
      ↓
Autonomy Check
      ↓
Action Contract
      ↓
Execution Consumer

The contract should constrain:

* action
* target
* inputs
* authority
* capability
* preconditions
* constraints
* permitted side effects
* postconditions
* failure semantics
* idempotency
* audit requirements

Autonomy therefore operates through typed contracts rather than unrestricted tool access.

⸻

22. Auditability

Autonomous actions must be auditable.

The execution record should make it possible to establish:

* which Intent initiated the action
* which Actor was represented
* which autonomy boundary applied
* which policies applied
* which authorization was established
* which evidence supported the decision
* which capability was selected
* which Action Contract governed execution
* when execution began
* what system executed the Action
* what outcome occurred
* whether human intervention occurred

The audit trail should describe system decisions and events without requiring access to private model chain-of-thought.

⸻

23. Security Boundary

Autonomy must not create a privilege-escalation mechanism.

In particular:

Model
  ↓
Agent
  ↓
Tool

must not become:

Model
  ↓
Implicit Authority

Tool access must remain bounded by the same authority and Trust model as other execution paths.

⸻

24. Recovery

Autonomous recovery may occur only within the permitted recovery boundary.

For example, if an Action fails because of a transient dependency:

Execution Failure
      ↓
Known Recoverable Failure
      ↓
Permitted Recovery Strategy
      ↓
Re-execution

The recovery strategy must not introduce unauthorized Actions.

A failure to perform Action A does not automatically authorize Action B simply because B might achieve a similar outcome.

⸻

25. Autonomy and Outcome

Autonomy concerns permission to act.

Outcome concerns what actually happened.

Therefore:

Autonomy
   ↓
Execution
   ↓
Outcome

A permitted autonomous Action may still:

* fail
* partially complete
* produce an unexpected outcome
* be rejected by the consumer
* produce an unknown result

Autonomy must not be interpreted as a guarantee of successful execution.

⸻

26. Canonical Invariants

Invariant 1

Autonomy is bounded by explicit authority.

Invariant 2

Autonomy does not establish Trust.

Invariant 3

Trust does not necessarily imply autonomous execution.

Invariant 4

Capability does not imply permission.

Invariant 5

Model confidence does not establish autonomous authority.

Invariant 6

Autonomous execution must remain within the resolved Intent scope.

Invariant 7

Scope expansion requires explicit evaluation.

Invariant 8

Human approval and confirmation are explicit evidence when required.

Invariant 9

Material changes invalidate previously established autonomous eligibility.

Invariant 10

Autonomous agents cannot redefine their own authority boundaries.

Invariant 11

Execution Contracts constrain autonomous execution.

Invariant 12

Autonomous execution must be auditable.

Invariant 13

Unknown mandatory conditions must not be treated as authorization.

Invariant 14

Boundary violations must produce controlled state transitions rather than autonomous improvisation.

Invariant 15

Autonomy does not guarantee execution success.

⸻

27. Canonical Autonomy Flow

                Human Intent
                     │
                     ▼
               Interpretation
                     │
                     ▼
                 Resolution
                     │
                     ▼
                Validation
                     │
                     ▼
               Trust Evaluation
                     │
              ┌──────┴──────┐
              │             │
           Allowed       Not Allowed
              │             │
              ▼             ▼
      Autonomy Boundary   WAIT / BLOCK
              │
              ▼
       Action Selection
              │
              ▼
       Execution Contract
              │
              ▼
           Execute
              │
              ▼
          Verify
              │
              ▼
           Outcome

⸻

28. Relationship to Bounded Autonomy

The canonical Noema model is therefore:

Human Intent
      ↓
Semantic Understanding
      ↓
Deterministic Validation
      ↓
Deterministic Trust
      ↓
Explicit Authority
      ↓
Bounded Autonomy
      ↓
Explicit Execution Contract
      ↓
Execution
      ↓
Outcome

The objective is not to eliminate autonomous behavior.

The objective is to make autonomous behavior explicitly authorized, bounded, observable, and revocable.

⸻

29. Consequences

Positive Consequences

This decision:

* prevents autonomous behavior from becoming implicit authority
* separates model reasoning from execution permission
* allows Noema to support agentic workflows safely
* makes autonomy policy-addressable
* provides explicit escalation points
* supports auditability
* enables different autonomy levels for different Actions
* prevents scope expansion from becoming an implicit agent behavior
* preserves enterprise systems as authoritative business systems

Costs

This decision also introduces:

* additional state and policy evaluation
* explicit authority modeling
* additional execution checks
* more complex contracts
* greater implementation complexity
* potential human intervention in workflows that could otherwise proceed automatically

These costs are accepted because unrestricted autonomy would violate Noema’s foundational authority boundaries.

⸻

30. Relationship to Other Canonical Decisions

This ADR depends upon and reinforces:

* ADR-003 — Probabilistic / Deterministic Boundary
* ADR-004 — Deterministic Trust Evaluation
* ADR-005 — Explicit Execution Contracts
* ADR-006 — Capability / Permission Separation
* ADR-007 — Enterprise Systems Remain Authoritative
* ADR-008 — Clarification Over Guessing
* ADR-010 — Trust State Machine
* ADR-011 — Intent State Separate from Execution State
* ADR-012 — Provenance and Auditability

Together they establish:

Probabilistic Understanding
          ↓
Deterministic Validation
          ↓
Deterministic Trust
          ↓
Explicit Authority
          ↓
Bounded Autonomy
          ↓
Execution Contract
          ↓
Enterprise Execution
          ↓
Authoritative Outcome

⸻

31. Final Decision Statement

Noema adopts bounded autonomy as a foundational architectural principle.

Noema may act autonomously only within explicitly established boundaries of Intent, authority, policy, capability, contract, constraints, risk, and context.

Agents and models may reason, plan, retrieve, propose, and coordinate within those boundaries, but they cannot establish or expand their own authority.

The canonical rule is:

Autonomy determines how Noema may act within an established authority boundary; it does not determine what Noema is authorized to do.