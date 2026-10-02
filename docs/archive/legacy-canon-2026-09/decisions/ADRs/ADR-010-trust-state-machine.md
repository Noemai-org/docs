> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-010 — Trust State Machine

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational Architecture
Domain: Trust
Canonical Path: decisions/ADR/ADR-010-trust-state-machine.md

⸻

1. Context

Noema’s Trust model cannot be represented adequately as a single boolean such as:

trusted = true

Trust is a lifecycle condition attached to an Intent.

An Intent may initially be unresolved, become evaluable after clarification, wait for approval or evidence, become blocked by policy or authorization, become ready for execution, and later become invalid if a material condition changes.

Therefore, Trust must have explicit states and deterministic transitions.

The existing canonical Trust concepts establish that:

* Trust is distinct from Intent resolution.
* Trust is distinct from model confidence.
* Trust is evaluated deterministically.
* Unknown mandatory conditions must not produce readiness.
* A READY Intent may become invalid when relevant conditions change.
* Execution is outside the Trust Engine.
* Execution success does not prove that a Trust decision was correct.
* Trust decisions require provenance and auditability.

The architecture therefore requires an explicit Trust State Machine.

⸻

2. Problem

Without an explicit state machine, implementations may introduce implicit or contradictory behavior.

For example:

missing approval → false

does not distinguish between:

* approval is still obtainable,
* approval has been denied,
* approval is unnecessary,
* approval information is unavailable.

Similarly:

trusted = true

does not express what happens when:

* authorization expires,
* evidence becomes stale,
* policy changes,
* capability disappears,
* context changes,
* constraints change.

A boolean Trust representation would therefore obscure important lifecycle semantics and make recovery, invalidation, auditability, and deterministic execution control difficult.

⸻

3. Decision

Noema will represent Trust as an explicit deterministic state machine.

The canonical Trust states are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Execution lifecycle states:

EXECUTING
COMPLETED
FAILED

may be represented alongside Trust as an independent Execution State rather than being treated as Trust states in the strict architectural sense.

The canonical conceptual lifecycle is:

UNRESOLVED
     ↓
EVALUATING
     ↓
 ┌───┼────────┐
 ↓   ↓        ↓
WAITING BLOCKED READY
  │              │
  │              ↓
  └──────→   EXECUTING
                 │
            ┌────┴────┐
            ↓         ↓
       COMPLETED    FAILED

The precise implementation may introduce more granular sub-states while preserving these canonical semantics.

⸻

4. State Semantics

4.1 UNRESOLVED

The Intent does not contain sufficient semantic information for reliable Trust evaluation.

Example:

"Send the report to John."

where multiple possible recipients exist.

The system must not resolve the ambiguity through guessing.

A clarification may cause:

UNRESOLVED
    ↓
EVALUATING

⸻

4.2 EVALUATING

The Trust Engine is actively determining whether the Intent satisfies the applicable Trust requirements.

Evaluation may consider:

* evidence
* authorization
* policy
* risk
* capability
* constraints
* context
* freshness
* validation results

The result must be deterministic with respect to the relevant inputs and rule versions.

⸻

4.3 WAITING

The Intent may become executable, but a required condition has not yet been satisfied.

Examples include:

WAITING_FOR_CLARIFICATION
WAITING_FOR_EVIDENCE
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CONFIRMATION
WAITING_FOR_APPROVAL
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE

Waiting is not rejection.

It represents an incomplete Trust condition.

⸻

4.4 BLOCKED

Execution is currently prohibited.

Examples include:

BLOCKED_BY_AUTHORIZATION
BLOCKED_BY_POLICY
BLOCKED_BY_CONSTRAINT
BLOCKED_BY_RISK
BLOCKED_BY_SCOPE
BLOCKED_BY_RESOURCE

A BLOCKED Intent must not cross the execution boundary.

⸻

4.5 READY

All mandatory Trust requirements have been satisfied.

Conceptually:

Resolved
AND
Required Evidence
AND
Authorization
AND
Policy
AND
Risk Controls
AND
Capability
AND
Constraints
AND
Context
    ↓
READY

READY means:

Noema has established that the Intent is eligible for execution.

It does not mean that execution has occurred or will necessarily succeed.

⸻

5. Execution State Separation

Trust state and execution state should remain conceptually separate.

The preferred architectural model is:

                 Intent
                   │
          ┌────────┴────────┐
          ↓                 ↓
     Trust State       Execution State
          │                 │
     UNRESOLVED             │
     EVALUATING             │
     WAITING                │
     BLOCKED                │
     READY              EXECUTING
                           │
                    ┌──────┴──────┐
                    ↓             ↓
                COMPLETED       FAILED

This prevents Trust from being conflated with execution outcome.

The relationship is:

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

⸻

6. Deterministic Transitions

Given:

Current State
+
Event
+
Current Conditions

the next state must be deterministic.

For example:

WAITING_FOR_APPROVAL
+
approval.received
+
all other requirements satisfied
=
READY

The state machine must not use probabilistic transitions such as:

80% confidence → READY

or:

model confidence > threshold → READY

Model confidence is not a Trust state transition authority.

⸻

7. Canonical Transition Table

Current State	Event / Condition	Next State
UNRESOLVED	Required meaning established	EVALUATING
EVALUATING	Requirements missing but recoverable	WAITING
EVALUATING	Requirement prohibits execution	BLOCKED
EVALUATING	All requirements satisfied	READY
WAITING	Missing requirement satisfied	EVALUATING
WAITING	Requirement becomes prohibited	BLOCKED
BLOCKED	Blocking condition removed	EVALUATING
READY	Execution begins after execution boundary	EXECUTING
READY	Material condition changes	EVALUATING
EXECUTING	Execution succeeds	COMPLETED
EXECUTING	Execution fails	FAILED

⸻

8. No Direct WAITING → READY

Noema will not permit a canonical direct transition from WAITING to READY.

Instead:

WAITING
   ↓
Requirement satisfied
   ↓
EVALUATING
   ↓
READY

The reason is that satisfying one requirement does not establish that all other Trust conditions remain satisfied.

For example:

WAITING_FOR_APPROVAL
        ↓
approval received

does not guarantee that authorization remains valid.

The Trust Engine must therefore re-evaluate.

⸻

9. No Direct BLOCKED → READY

Similarly:

BLOCKED
   ↓
Blocking condition removed
   ↓
EVALUATING
   ↓
READY

Removing one blocking condition does not establish that all other Trust requirements are satisfied.

⸻

10. READY Is Not Permanent

READY represents current execution eligibility.

It is not a permanent Trust grant.

A READY Intent may become invalid when:

* authorization is revoked,
* authorization expires,
* approval expires,
* evidence becomes stale,
* policy changes,
* risk changes,
* context changes,
* constraints change,
* capability becomes unavailable,
* relevant resource state changes.

Therefore:

READY
  ↓
material change
  ↓
EVALUATING

The subsequent result may be:

WAITING
BLOCKED
READY

depending on the new conditions.

⸻

11. Trust Invalidation

Trust invalidation is the mechanism by which a previously trusted Intent loses current execution eligibility.

Examples:

authorization.revoked
policy.changed
approval.expired
evidence.expired
risk.changed
capability.unavailable
resource.changed
context.changed

The system must re-evaluate rather than silently preserving READY.

⸻

12. Trust Expiration

Trust decisions may have explicit validity periods.

For example:

READY
valid_until = 10:30

At expiration:

READY
   ↓
trust.expired
   ↓
EVALUATING

The resulting state is determined by the current conditions.

It may become:

WAITING
BLOCKED
READY

⸻

13. Fail-Closed Behavior

For consequential Actions, unavailable Trust dependencies must not silently result in READY.

For example:

READY
  ↓
Trust dependency unavailable
  ↓
EVALUATING
  ↓
WAITING / BLOCKED

Never:

dependency unavailable
      ↓
READY

Unknown mandatory conditions cannot establish execution eligibility.

⸻

14. Unknown vs Blocked

Unknown information must not automatically be interpreted as denial.

For example:

Authorization service unavailable

does not necessarily mean:

Authorization denied

The appropriate state may instead be:

WAITING

or another explicit not-ready state.

The distinction is:

UNKNOWN ≠ DENIED

⸻

15. Material Events

The following events may trigger Trust re-evaluation when relevant:

intent.updated
intent.resolved
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

Execution events include:

execution.accepted
execution.started
execution.completed
execution.failed

The event vocabulary is conceptual and may evolve into a formal protocol.

⸻

16. Dependency-Aware Re-Evaluation

Trust re-evaluation should be dependency-aware.

If a policy affects:

Intent I1
Intent I2
Intent I3

and that policy changes, those affected Intents may require re-evaluation.

Unrelated Intents need not necessarily be re-evaluated.

Conceptually:

Policy P1
   │
   ├── I1 → re-evaluate
   ├── I2 → re-evaluate
   └── I3 → re-evaluate

This supports scalable Trust evaluation.

⸻

17. Execution Boundary

READY does not authorize the Trust Engine to perform the Action itself.

The canonical transition is:

READY
  ↓
Execution Contract
  ↓
Consumer Acceptance
  ↓
EXECUTING

The execution consumer explicitly accepts the execution contract and begins execution.

The Trust Engine does not execute the Action.

⸻

18. Waiting Taxonomy

WAITING should identify the condition preventing readiness.

Canonical subtypes include:

WAITING_FOR_CLARIFICATION
WAITING_FOR_EVIDENCE
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CONFIRMATION
WAITING_FOR_APPROVAL
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE

The taxonomy remains extensible.

⸻

19. Blocking Taxonomy

BLOCKED should identify why execution is prohibited.

Canonical subtypes include:

BLOCKED_BY_AUTHORIZATION
BLOCKED_BY_POLICY
BLOCKED_BY_CONSTRAINT
BLOCKED_BY_RISK
BLOCKED_BY_SCOPE
BLOCKED_BY_RESOURCE

The taxonomy remains extensible.

⸻

20. Composite Intents

Composite Intents require state aggregation.

For example:

A = READY
B = WAITING_FOR_APPROVAL
C = READY

If execution is atomic:

Composite Trust = WAITING

If:

B = BLOCKED

then:

Composite Trust = BLOCKED

If partial execution is permitted, components may progress independently.

However, Noema must not infer permission for partial execution.

Partial execution must be explicitly represented by the Intent semantics.

⸻

21. Human Intervention

Human intervention must produce explicit state transitions.

For example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING
        ↓
READY

Approval is evidence relevant to the Trust decision.

It is not merely an unstructured conversational event.

Similarly, clarification changes the semantic information available to evaluation:

UNRESOLVED
     ↓
clarification.requested
     ↓
clarification.received
     ↓
EVALUATING

⸻

22. State Transition Guards

Transitions must be governed by explicit predicates.

For example:

READY

requires a guard conceptually equivalent to:

allMandatoryRequirementsSatisfied

while:

WAITING_FOR_APPROVAL

requires conditions equivalent to:

approvalRequired
AND
approvalMissing

The exact predicates belong to the Trust implementation and specifications.

⸻

23. State Transition Effects

A transition may produce deterministic system effects such as:

* creating a clarification request,
* recording a missing requirement,
* issuing an approval request,
* invalidating an execution contract,
* creating an execution contract,
* emitting a Trust event.

Trust transitions should avoid hidden side effects.

⸻

24. Trust History

Significant Trust transitions must be auditable.

A conceptual history may be:

T0: UNRESOLVED
T1: EVALUATING
T2: WAITING_FOR_APPROVAL
T3: EVALUATING
T4: READY
T5: EXECUTING

Each transition should preserve enough information to reconstruct the Trust lifecycle.

⸻

25. Transition Provenance

A Trust transition should record, as applicable:

previous_state
event
new_state
timestamp
intent_version
evaluation_id
relevant_evidence
reason

This establishes an auditable record of how Trust evolved.

⸻

26. State Machine Invariants

Invariant 1

Every Trust transition must have a defined cause.

Invariant 2

Trust transitions are deterministic.

Invariant 3

Unknown mandatory conditions cannot transition an Intent to READY.

Invariant 4

WAITING and BLOCKED are semantically distinct.

Invariant 5

A material change to a trusted condition can invalidate READY.

Invariant 6

Satisfying one requirement triggers re-evaluation rather than blindly granting READY.

Invariant 7

A BLOCKED Intent cannot cross the execution boundary.

Invariant 8

An UNRESOLVED Intent cannot cross the execution boundary.

Invariant 9

READY does not imply successful execution.

Invariant 10

Execution outcomes do not retroactively determine whether a Trust decision was valid.

Invariant 11

A materially changed Intent requires a new Trust evaluation.

Invariant 12

Trust history must be reconstructible.

⸻

27. Relationship to Validation

Validation and Trust remain distinct.

The relationship is:

Intent
  ↓
Validation
  │
  ├── INCOMPLETE → WAITING
  ├── INVALID    → BLOCKED
  ├── UNKNOWN    → WAITING / NOT READY
  └── VALID
        ↓
   Trust Evaluation
        │
        ├── WAITING
        ├── BLOCKED
        └── READY

Validation establishes that the canonical Intent is structurally and semantically valid for its next lifecycle transition.

Trust establishes whether the Intent may proceed toward execution.

Therefore:

VALID ≠ TRUSTED

⸻

28. Relationship to Autonomy

Trust state does not, by itself, determine whether autonomous execution is permitted.

For example:

Trust = READY

may coexist with a policy requiring human approval before autonomous execution.

Autonomy control therefore remains a separate concern from the Trust State Machine.

⸻

29. Relationship to Execution Outcome

A READY Trust decision establishes execution eligibility at a particular point in time.

It does not guarantee execution success.

Therefore:

READY ≠ SUCCESS

A downstream system may reject the execution because business state changed between Trust evaluation and execution.

Execution outcomes must remain separately represented.

⸻

30. Rationale

This decision establishes explicit lifecycle semantics for Trust and prevents several architectural failures:

1. treating Trust as a boolean;
2. treating model confidence as authorization;
3. conflating missing conditions with denial;
4. allowing stale READY states to persist;
5. bypassing re-evaluation after material changes;
6. conflating Trust with execution outcome;
7. allowing execution without an explicit boundary;
8. making Trust transitions non-deterministic;
9. hiding the causes of Trust decisions;
10. making recovery and human intervention implicit.

The state machine provides a common control structure for the Trust Engine while allowing implementation-specific granularity.

⸻

31. Consequences

Positive

Noema gains:

* explicit Trust lifecycle semantics;
* deterministic transition rules;
* clear distinction between waiting and blocking;
* explicit Trust invalidation;
* dependency-aware re-evaluation;
* auditable Trust history;
* clear execution boundaries;
* recoverable lifecycle transitions;
* support for human intervention;
* separation between Trust and execution outcome.

Trade-offs

The model introduces additional state-management complexity.

Implementations must maintain:

* state transitions,
* transition causes,
* relevant dependencies,
* evaluation provenance,
* expiry information,
* re-evaluation triggers.

This complexity is intentional because consequential execution requires explicit lifecycle control.

⸻

32. Non-Goals

This ADR does not define:

* the complete Trust data schema;
* the complete Trust Engine implementation;
* authorization policy language;
* risk-scoring methodology;
* execution contract schema;
* execution consumer implementation;
* the complete Intent lifecycle;
* the final event protocol;
* the final autonomy-control model.

Those concerns belong to their respective canonical specifications.

⸻

33. Canonical Model

The canonical Trust lifecycle is:

UNRESOLVED
     ↓
EVALUATING
     ↓
WAITING / BLOCKED / READY
     ↓
EXECUTING
     ↓
COMPLETED / FAILED

With invalidation:

READY
  ↓
material condition changes
  ↓
EVALUATING
  ↓
WAITING / BLOCKED / READY

And with recovery:

WAITING
   ↓
condition satisfied
   ↓
EVALUATING
   ↓
READY
BLOCKED
   ↓
blocking condition removed
   ↓
EVALUATING
   ↓
READY

⸻

34. Final Decision

Noema will use an explicit, deterministic Trust State Machine to govern the lifecycle of execution eligibility.

Trust is not a permanent boolean and is not derived from model confidence.

The canonical principle is:

Noema moves an Intent into READY only when deterministic state-machine guards establish that all mandatory Trust conditions are satisfied at that point in time.

A READY state remains subject to invalidation when relevant conditions materially change, and execution remains a separate boundary governed by an explicit Execution Contract.