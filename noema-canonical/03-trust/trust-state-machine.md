Trust State Machine

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: 03-trust/trust-state-machine.md

⸻

1. Definition

The Trust State Machine defines the legal states and deterministic transitions through which an Intent passes as Noema establishes whether it may cross the execution boundary.

The Trust Model defines what Trust means.

The Trust Engine defines how Trust is evaluated.

The Trust State Machine defines how Trust evolves over time.

⸻

2. Core Principle

Trust is a lifecycle, not a one-time boolean decision.

An Intent may move through states as:

evidence arrives
authorization changes
clarification occurs
approval is granted
policy changes
risk changes
capabilities become available
context changes
execution begins
execution completes

Therefore:

Trust(t₁) ≠ necessarily Trust(t₂)

⸻

3. Trust State Machine

The canonical conceptual lifecycle is:

                    ┌──────────────────┐
                    │    UNRESOLVED    │
                    └────────┬─────────┘
                             │
                       clarification
                             │
                             ▼
                    ┌──────────────────┐
                    │   EVALUATING     │
                    └────────┬─────────┘
                             │
                ┌────────────┼─────────────┐
                │            │             │
                ▼            ▼             ▼
             WAITING       BLOCKED       READY
                │                          │
                │                          ▼
                │                     EXECUTING
                │                          │
                │                 ┌────────┴────────┐
                │                 ▼                 ▼
                │             COMPLETED           FAILED
                │
                └──── requirement satisfied
                              │
                              ▼
                         EVALUATING

This is the conceptual model. Implementations may use more granular states.

⸻

4. Trust States

The canonical state categories are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY
EXECUTING
COMPLETED
FAILED

Some states may have reason-specific subtypes.

For example:

WAITING_FOR_CLARIFICATION
WAITING_FOR_APPROVAL
WAITING_FOR_CONFIRMATION
WAITING_FOR_EVIDENCE
WAITING_FOR_CAPABILITY

⸻

5. UNRESOLVED

UNRESOLVED means the Intent does not yet contain sufficient semantic information for reliable Trust evaluation.

Example:

"Send the report to John."

where:

John = multiple possible recipients

The Trust Engine must not attempt to resolve this by guessing.

Transition:

UNRESOLVED
    ↓
clarification
    ↓
EVALUATING

⸻

6. EVALUATING

EVALUATING represents the active deterministic assessment of the Intent.

The Trust Engine evaluates applicable:

Evidence
Authorization
Policy
Risk
Capability
Constraints
Context
Freshness

The evaluation should produce a deterministic result.

⸻

7. WAITING

WAITING means the Intent may become executable, but a required condition has not yet been satisfied.

Examples:

WAITING_FOR_APPROVAL
WAITING_FOR_CONFIRMATION
WAITING_FOR_EVIDENCE
WAITING_FOR_CLARIFICATION
WAITING_FOR_CAPABILITY

Waiting is not rejection.

It is an incomplete Trust condition.

⸻

8. BLOCKED

BLOCKED means execution is currently prohibited.

Examples:

Authorization denied
Policy prohibits Action
Constraint violated
Risk exceeds permitted threshold
Actor outside permitted scope
Resource not eligible

A blocked Intent should not cross the execution boundary.

⸻

9. READY

READY means all mandatory Trust requirements have been satisfied.

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

READY means the Intent is eligible to produce or carry an Execution Contract.

It does not mean execution has occurred.

⸻

10. EXECUTING

EXECUTING means the execution consumer has accepted the trusted Intent and execution has begun.

The transition is:

READY
  ↓
Execution Contract accepted
  ↓
EXECUTING

The Trust Engine itself does not execute the Action.

⸻

11. COMPLETED

COMPLETED means the execution layer has reported successful completion.

Conceptually:

EXECUTING
    ↓
successful execution
    ↓
COMPLETED

This is an execution/outcome state, not a Trust evaluation state in the strict sense.

Its presence in the lifecycle exists to show the complete Intent progression.

⸻

12. FAILED

FAILED means execution did not successfully complete.

Examples:

Execution rejected
Timeout
External dependency failure
Consumer failure
Partial failure
Unknown execution result

A Trust decision of READY does not guarantee COMPLETED.

Therefore:

READY ≠ SUCCESS

⸻

13. Trust State vs Intent State

The Trust State Machine should not be confused with the broader Intent lifecycle.

For example:

Intent State:
RESOLVED
Trust State:
WAITING_FOR_APPROVAL

or:

Intent State:
EXECUTING
Trust State:
EXECUTION_AUTHORIZED

Noema should avoid conflating semantic lifecycle with execution lifecycle.

⸻

14. Recommended Conceptual Separation

Intent Lifecycle
        │
        ├── Created
        ├── Resolving
        ├── Resolved
        └── Executing / Completed
       
Trust Lifecycle
        │
        ├── Unresolved
        ├── Evaluating
        ├── Waiting
        ├── Blocked
        └── Ready

Trust is a control lifecycle attached to an Intent.

⸻

15. State Transition Principle

A Trust state may change only as the result of a defined event or a deterministic re-evaluation of relevant conditions.

Trust must not change because:

the Model "feels" more confident
a random retry occurred
a prompt was reformulated
an LLM generated a stronger explanation

⸻

16. Transition Table

Current State	Event	Next State
UNRESOLVED	Required meaning established	EVALUATING
EVALUATING	Requirements missing but recoverable	WAITING
EVALUATING	Requirement prohibits execution	BLOCKED
EVALUATING	All requirements satisfied	READY
WAITING	Missing requirement satisfied	EVALUATING
WAITING	Requirement becomes prohibited	BLOCKED
BLOCKED	Blocking condition removed	EVALUATING
READY	Execution begins	EXECUTING
READY	Material condition changes	EVALUATING
EXECUTING	Execution succeeds	COMPLETED
EXECUTING	Execution fails	FAILED

⸻

17. No Direct WAITING → READY

The canonical transition should be:

WAITING
   ↓
Requirement satisfied
   ↓
EVALUATING
   ↓
READY

Why?

Because satisfying one requirement does not prove that all other requirements remain satisfied.

Example:

Approval received

but meanwhile:

Authorization expired

Therefore the Trust Engine must re-evaluate.

⸻

18. No Direct BLOCKED → READY

Similarly:

BLOCKED
   ↓
Blocking condition removed
   ↓
EVALUATING
   ↓
READY

The removal of one block does not guarantee overall readiness.

⸻

19. No Direct READY → EXECUTING Without an Execution Boundary

READY means:

Noema has established that the Intent is eligible for execution.

The execution layer must explicitly accept the Execution Contract.

Therefore:

READY
    ↓
Execution Contract
    ↓
Consumer acceptance
    ↓
EXECUTING

⸻

20. READY Is Not Permanent

A common mistake would be:

READY = forever trusted

That is incorrect.

A READY Intent can become invalid if:

policy changes
authorization expires
resource state changes
risk changes
context changes
constraints change
evidence expires
capability disappears

Therefore:

READY
  ↓
material change
  ↓
EVALUATING

⸻

21. Trust Invalidation

Trust invalidation is the mechanism by which a previously trusted Intent loses execution eligibility.

Examples:

Authorization revoked
Policy changed
Approval expired
Evidence became stale
Risk threshold changed
Resource became unavailable
Execution capability disappeared

The state should be re-evaluated rather than silently remaining READY.

⸻

22. Trust Expiration

Some Trust decisions may have explicit expiry.

Example:

READY
valid_until = 10:30

At 10:31:

READY
   ↓
expired
   ↓
EVALUATING

The appropriate result may then be:

WAITING
BLOCKED
READY

depending on the new evaluation.

⸻

23. Re-Evaluation

Re-evaluation is central to the State Machine.

Conceptually:

Current State
     ↓
Material Event
     ↓
Collect Current Conditions
     ↓
Evaluate
     ↓
New Trust State

This prevents stale Trust decisions.

⸻

24. Material Events

Examples of material events:

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

These events should trigger re-evaluation when relevant.

⸻

25. Dependency-Aware Re-Evaluation

Not every event needs to invalidate every Intent.

Conceptually:

Policy P1
   ↓
Intent I1
Intent I2
Intent I3

If P1 changes:

I1 → re-evaluate
I2 → re-evaluate
I3 → re-evaluate

while unrelated Intents need not be evaluated.

This provides scalability.

⸻

26. Waiting State Taxonomy

WAITING should identify the missing condition.

Canonical examples:

WAITING_FOR_CLARIFICATION
WAITING_FOR_EVIDENCE
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CONFIRMATION
WAITING_FOR_APPROVAL
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE

The taxonomy should remain extensible.

⸻

27. WAITING_FOR_CLARIFICATION

Used when semantic information is missing.

Example:

Intent:
"Cancel the subscription."
Problem:
Multiple subscriptions exist.
State:
WAITING_FOR_CLARIFICATION

⸻

28. WAITING_FOR_EVIDENCE

Used when the Intent is understood but required evidence has not been established.

Example:

Identity verification required.
Evidence:
missing

Result:

WAITING_FOR_EVIDENCE

⸻

29. WAITING_FOR_AUTHORIZATION

Used when authorization is required but has not yet been established.

This is distinct from:

BLOCKED

because authorization may still be obtained.

⸻

30. WAITING_FOR_CONFIRMATION

Used when the Actor must explicitly confirm the Action.

Example:

"This will permanently delete the account. Continue?"

Until confirmation:

WAITING_FOR_CONFIRMATION

⸻

31. WAITING_FOR_APPROVAL

Used when an authorized approver must approve the Action.

Example:

Transfer > ₦10M

requires secondary approval.

⸻

32. WAITING_FOR_CAPABILITY

Used when the Action is permitted but the required execution capability is temporarily unavailable.

Example:

Payment service unavailable.

The Intent should not be interpreted as denied.

⸻

33. BLOCKED State Taxonomy

BLOCKED should identify why execution is prohibited.

Examples:

BLOCKED_BY_AUTHORIZATION
BLOCKED_BY_POLICY
BLOCKED_BY_CONSTRAINT
BLOCKED_BY_RISK
BLOCKED_BY_SCOPE
BLOCKED_BY_RESOURCE

The exact taxonomy may evolve.

⸻

34. Waiting vs Blocking

This distinction is foundational.

Waiting

"Not yet."

Blocking

"No."

For example:

Approval missing
→ WAITING
Policy prohibits action
→ BLOCKED

⸻

35. Unknown vs Blocked

Unknown is not necessarily denial.

Example:

Authorization service unavailable.

The system does not know whether authorization exists.

Therefore:

Authorization = UNKNOWN

and:

Trust = WAITING / NOT_READY

rather than falsely asserting:

Authorization = DENIED

⸻

36. Fail-Closed Transition

For consequential Actions:

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

⸻

37. Recovery

Trust states should support recoverable transitions.

Example:

WAITING_FOR_CAPABILITY
        ↓
Capability restored
        ↓
EVALUATING
        ↓
READY

Similarly:

BLOCKED_BY_POLICY
        ↓
Policy changes
        ↓
EVALUATING
        ↓
READY

provided all other requirements remain satisfied.

⸻

38. Terminal States

The lifecycle contains execution terminal states:

COMPLETED
FAILED

But Trust itself should generally remain concerned with execution eligibility rather than execution outcomes.

Therefore an implementation may choose to model:

Trust State:
READY

alongside:

Execution State:
EXECUTING
COMPLETED
FAILED

rather than making them one enum.

This distinction should remain open until the implementation architecture is finalized.

⸻

39. Recommended Architectural Separation

A cleaner model is:

                 Intent
                   │
          ┌────────┴────────┐
          ▼                 ▼
    Trust State       Execution State
          │                 │
     UNRESOLVED             │
     EVALUATING             │
     WAITING                │
     BLOCKED                │
     READY             EXECUTING
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                COMPLETED       FAILED

This avoids conflating Trust with Outcome.

⸻

40. Trust State Machine and Outcome

The relationship is:

Trust
 ↓
Execution Eligibility
 ↓
Execution
 ↓
Outcome

Not:

Trust
 ↓
Outcome

Trust cannot determine whether an external system actually succeeds.

⸻

41. Composite Intents

Composite Intents require state aggregation.

Example:

A = READY
B = WAITING_FOR_APPROVAL
C = READY

If execution is atomic:

Composite Trust = WAITING

If B becomes blocked:

A = READY
B = BLOCKED
C = READY
Composite Trust = BLOCKED

⸻

42. Partial Execution

If the Intent explicitly permits partial execution, each component may progress independently.

Example:

A → EXECUTING
B → WAITING
C → READY

But this must be explicitly represented in the Intent semantics.

Noema must not infer permission for partial execution.

⸻

43. Trust and Autonomy

A Trust state does not by itself determine whether the Model may act autonomously.

For example:

Trust:
READY
Policy:
Human approval required for autonomous execution.

The Intent may remain:

WAITING_FOR_APPROVAL

or the model may be represented with a separate autonomy-control state.

The exact representation should be resolved when autonomy semantics are formalized.

⸻

44. Human Intervention

Human intervention should produce explicit state transitions.

Example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING
        ↓
READY

The approval is evidence.

It is not merely a conversational event.

⸻

45. Clarification

Clarification similarly produces a state transition:

UNRESOLVED
     ↓
clarification.requested
     ↓
clarification.received
     ↓
EVALUATING

The new information updates the Intent state.

⸻

46. State Transition Events

A conceptual event vocabulary:

intent.resolved
evidence.satisfied
evidence.expired
authorization.granted
authorization.revoked
policy.satisfied
policy.changed
approval.required
approval.received
approval.revoked
confirmation.required
confirmation.received
capability.available
capability.unavailable
constraint.satisfied
constraint.violated
context.changed
trust.expired
execution.accepted
execution.started
execution.completed
execution.failed

These events are illustrative rather than a final protocol.

⸻

47. Transition Determinism

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
all other conditions satisfied
=
READY

Not:

maybe READY

⸻

48. No Probabilistic Transitions

The State Machine must never contain:

80% chance → READY

or:

Model confidence > 0.8 → READY

Transitions are governed by explicit predicates.

⸻

49. State Transition Guards

Conceptually:

READY

requires:

guard(
    allMandatoryRequirementsSatisfied
)

While:

WAITING_FOR_APPROVAL

requires:

guard(
    approvalRequired
    AND approvalMissing
)

The guards are deterministic.

⸻

50. State Transition Actions

A transition may produce deterministic system effects such as:

create clarification request
record missing requirement
issue approval request
invalidate execution contract
create execution contract
emit trust event

However, Trust transitions should avoid hidden side effects.

⸻

51. Trust State History

Every significant Trust transition should be auditable.

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

This creates a Trust history.

⸻

52. State Transition Provenance

Each transition should record:

previous state
event
new state
timestamp
Intent version
evaluation ID
relevant evidence
reason

This makes Trust explainable after the fact.

⸻

53. State Machine Invariants

Invariant 1

Every state transition must have a defined cause.

Invariant 2

Trust transitions are deterministic.

Invariant 3

Unknown mandatory conditions cannot transition an Intent to READY.

Invariant 4

WAITING and BLOCKED are semantically distinct.

Invariant 5

A material change to a trusted condition can invalidate READY.

Invariant 6

A requirement being satisfied triggers re-evaluation rather than blindly granting Trust.

Invariant 7

A blocked Intent cannot cross the execution boundary.

Invariant 8

An unresolved Intent cannot cross the execution boundary.

Invariant 9

READY does not imply successful execution.

Invariant 10

Execution outcomes do not retroactively determine whether the Trust decision was valid.

Invariant 11

A materially changed Intent requires a new Trust evaluation.

Invariant 12

Trust history must be reconstructible.

⸻

54. Canonical State Flow

The canonical flow is:

                 ┌───────────────┐
                 │  UNRESOLVED   │
                 └───────┬───────┘
                         │
                  meaning established
                         │
                         ▼
                 ┌───────────────┐
                 │  EVALUATING   │
                 └───────┬───────┘
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
         WAITING      BLOCKED       READY
             │                       │
       requirement                   │
         satisfied                   │
             │                       │
             └───────┐               │
                     ▼               ▼
                 EVALUATING      EXECUTING
                                     │
                              ┌──────┴──────┐
                              ▼             ▼
                         COMPLETED        FAILED

And when a trusted Intent becomes invalid:

READY
  ↓
material condition changes
  ↓
EVALUATING
  ↓
WAITING / BLOCKED / READY

⸻

55. Canonical Mental Model

The Trust State Machine can be reduced to four fundamental questions:

1. Do we understand the Intent?
        ↓
2. Have all required conditions been established?
        ↓
3. Is execution permitted?
        ↓
4. Has execution actually begun/completed?

Which produces:

UNRESOLVED
     ↓
EVALUATING
     ↓
WAITING / BLOCKED / READY
     ↓
EXECUTING
     ↓
COMPLETED / FAILED

⸻

56. Final Definition

The Trust State Machine defines how Noema moves an Intent from unresolved or incomplete Trust conditions toward readiness, blocking, execution, and eventual completion, using deterministic transitions driven by explicit events and condition changes.

The central invariant is:

Noema never moves an Intent into READY because it believes the Intent is probably safe. It moves the Intent into READY only when the State Machine’s deterministic guards establish that all mandatory Trust conditions are satisfied.