Trust State Machine

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/trust-state-machine.md

⸻

1. Definition

The Trust State Machine defines the legal states and deterministic transitions through which an Intent passes as Noema establishes whether it may cross the execution boundary.

The three Trust artifacts have distinct responsibilities:

* Trust Model — defines what Trust means.
* Trust Engine — evaluates whether the current conditions satisfy the Trust Model.
* Trust State Machine — defines how Trust and execution eligibility evolve over time.

The State Machine therefore governs state transition, not the underlying semantic definition of Trust.

⸻

2. Core Principle

Trust is a lifecycle, not a one-time boolean decision.

An Intent may move through states as:

* evidence arrives
* semantic ambiguity is resolved
* authorization changes
* approval is granted or revoked
* confirmation is received
* policy changes
* risk changes
* capabilities become available or unavailable
* constraints change
* context changes
* Trust expires
* execution begins
* execution completes

Therefore:

Trust(t₁) ≠ necessarily Trust(t₂)

A previously READY Intent may become non-ready before execution if a material governing condition changes.

⸻

3. State-Machine Scope

The Trust State Machine governs Trust eligibility and its transition toward execution.

It does not become the authoritative state machine for:

* external business systems
* business transactions
* application workflows
* execution-provider internals
* external system outcomes

Those systems retain their own state.

This distinction is important because:

Trust State
    ≠
Business State
    ≠
Execution Outcome

⸻

4. Canonical Trust Lifecycle

The conceptual Trust lifecycle is:

                    ┌──────────────────┐
                    │    UNRESOLVED    │
                    └────────┬─────────┘
                             │
                      meaning established
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

This is a conceptual model.

The implementation may use separate Trust and Execution state machines, as described below.

⸻

5. Canonical State Categories

The foundational Trust states are:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Execution states are:

EXECUTING
COMPLETED
FAILED

Reason-specific subtypes may be attached to Trust states.

For example:

WAITING
  ├── WAITING_FOR_CLARIFICATION
  ├── WAITING_FOR_EVIDENCE
  ├── WAITING_FOR_AUTHORIZATION
  ├── WAITING_FOR_CONFIRMATION
  ├── WAITING_FOR_APPROVAL
  ├── WAITING_FOR_CAPABILITY
  └── WAITING_FOR_RESOURCE

and:

BLOCKED
  ├── BLOCKED_BY_AUTHORIZATION
  ├── BLOCKED_BY_POLICY
  ├── BLOCKED_BY_CONSTRAINT
  ├── BLOCKED_BY_RISK
  ├── BLOCKED_BY_SCOPE
  └── BLOCKED_BY_RESOURCE

The taxonomy is extensible.

The semantic categories are canonical; exact implementation enums are not yet fixed.

⸻

6. UNRESOLVED

UNRESOLVED means the Intent does not yet contain sufficient semantic information for reliable Trust evaluation.

Example:

Intent:
"Send the report to John."
Problem:
John = multiple possible recipients

Noema must not resolve material ambiguity by guessing.

The appropriate transition is:

UNRESOLVED
    ↓
clarification
    ↓
Intent updated
    ↓
EVALUATING

⸻

7. EVALUATING

EVALUATING represents deterministic assessment of the current Intent state.

The Trust Engine evaluates the applicable:

* Resolution
* Evidence
* Authorization
* Policy
* Risk
* Capability
* Constraints
* Context
* Freshness
* other governing Trust requirements

The result must be deterministic for the same relevant inputs and rule versions.

EVALUATING is therefore an assessment state, not a confidence level.

⸻

8. WAITING

WAITING means:

The Intent may become executable, but one or more required conditions have not yet been satisfied.

Examples:

WAITING_FOR_APPROVAL
WAITING_FOR_CONFIRMATION
WAITING_FOR_EVIDENCE
WAITING_FOR_CLARIFICATION
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE

Waiting is recoverable.

It does not mean the Action is prohibited.

⸻

9. BLOCKED

BLOCKED means:

A governing condition currently prohibits execution.

Examples:

* authorization denied
* policy prohibits the Action
* constraint violated
* risk exceeds permitted threshold
* Actor is outside permitted scope
* resource is ineligible
* Action is prohibited in the current Context

A BLOCKED Intent cannot cross the execution boundary.

⸻

10. READY

READY means all mandatory Trust requirements applicable to the Intent have been satisfied.

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
    AND
Freshness
    ↓
READY

Only applicable requirements participate.

For example, an Intent that does not require approval must not be forced through an approval state.

READY means:

Execution Eligible

It does not mean:

Execution Started

and does not mean:

Execution Successful

⸻

11. EXECUTING

EXECUTING means the execution consumer has accepted the Execution Contract and execution has begun.

Conceptually:

READY
   ↓
Execution Contract
   ↓
Consumer acceptance
   ↓
EXECUTING

The Trust Engine does not perform the Action.

The execution consumer does.

⸻

12. COMPLETED

COMPLETED means the execution layer has reported successful completion according to the applicable execution semantics.

Conceptually:

EXECUTING
    ↓
successful execution
    ↓
COMPLETED

This is primarily an execution/outcome state rather than a Trust state.

⸻

13. FAILED

FAILED means execution did not reach successful completion.

Possible execution outcomes include:

* rejected
* failed
* timed out
* dependency failure
* consumer failure
* partial execution
* unknown execution result

Therefore:

READY ≠ SUCCESS

A failed execution does not, by itself, establish that the preceding Trust decision was incorrect.

⸻

14. Trust State vs Intent State

The Trust State Machine must not be confused with the broader Intent lifecycle.

For example:

Intent State:
RESOLVED
Trust State:
WAITING_FOR_APPROVAL

or:

Intent State:
RESOLVED
Trust State:
READY

The Intent lifecycle describes the semantic lifecycle of the Intent.

The Trust lifecycle describes whether its execution is currently eligible.

⸻

15. Trust State vs Execution State

A stronger architectural separation is:

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

This prevents Trust from becoming a disguised execution-status model.

A production implementation may therefore maintain:

TrustState
ExecutionState

as distinct but related state machines.

⸻

16. State Transition Principle

A Trust transition may occur only because of:

1. an explicit state-machine event, or
2. deterministic re-evaluation caused by a material condition change.

Trust must not change because:

* the Model “feels” more confident
* an LLM generated a stronger explanation
* a prompt was reformulated without semantic effect
* a random retry occurred
* a model confidence score increased
* an untrusted component asserted READY

⸻

17. Canonical Transition Table

Current State	Event / Condition	Next State
UNRESOLVED	Required meaning established	EVALUATING
EVALUATING	Requirements missing but recoverable	WAITING
EVALUATING	Requirement prohibits execution	BLOCKED
EVALUATING	All mandatory requirements satisfied	READY
WAITING	Missing requirement changes	EVALUATING
WAITING	Requirement becomes prohibited	BLOCKED
BLOCKED	Blocking condition changes	EVALUATING
READY	Execution begins	EXECUTING
READY	Material condition changes	EVALUATING
EXECUTING	Execution succeeds	COMPLETED
EXECUTING	Execution fails	FAILED

The exact transition event vocabulary may evolve, but the semantic rules must remain deterministic.

⸻

18. No Direct WAITING → READY

The canonical transition is:

WAITING
    ↓
Requirement satisfied
    ↓
EVALUATING
    ↓
READY

Noema must not assume that satisfying one requirement means every other requirement remains satisfied.

Example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING
        ↓
Authorization expired
        ↓
WAITING / BLOCKED

The re-evaluation is therefore essential.

⸻

19. No Direct BLOCKED → READY

Similarly:

BLOCKED
    ↓
Blocking condition removed
    ↓
EVALUATING
    ↓
READY

Removal of one blocking condition does not prove that all other conditions are satisfied.

⸻

20. No Direct READY → EXECUTING Without an Execution Boundary

READY means Noema has established execution eligibility.

The consumer must still accept the Execution Contract.

Therefore:

READY
    ↓
Execution Contract issued
    ↓
Consumer acceptance
    ↓
EXECUTING

This preserves the boundary between Noema’s authorization of execution eligibility and the consumer’s actual execution.

⸻

21. READY Is Conditional

READY must never be interpreted as permanent Trust.

A READY Intent may become non-ready when:

* authorization expires or is revoked
* evidence becomes stale
* policy changes
* risk changes
* constraints change
* resource state changes
* Context changes
* capability becomes unavailable
* approval expires
* Intent semantics materially change

Therefore:

READY
  ↓
material change
  ↓
EVALUATING
  ↓
WAITING / BLOCKED / READY

⸻

22. Trust Invalidation

Trust invalidation occurs when a previously established execution condition is no longer valid.

Examples:

Authorization revoked
Approval expired
Evidence expired
Policy changed
Risk threshold changed
Capability unavailable
Resource state changed
Context changed
Constraint violated

The correct response is not to preserve the previous READY state.

The Intent must be re-evaluated.

⸻

23. Trust Expiration

Some Trust decisions may have explicit temporal validity.

Example:

Trust:
READY
valid_until:
10:30

At 10:31:

READY
   ↓
expired
   ↓
EVALUATING

The new evaluation may result in:

WAITING
BLOCKED
READY

depending on current conditions.

⸻

24. Re-Evaluation

Re-evaluation is central to the State Machine.

Conceptually:

Current State
     ↓
Material Event
     ↓
Collect Current Conditions
     ↓
Trust Evaluation
     ↓
New State

This prevents stale Trust from crossing the execution boundary.

⸻

25. Material Events

Illustrative material events include:

intent.resolved
intent.updated
evidence.added
evidence.expired
authorization.granted
authorization.revoked
approval.received
approval.revoked
approval.expired
confirmation.received
policy.changed
risk.changed
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

26. Dependency-Aware Re-Evaluation

Noema should avoid treating every event as globally invalidating every Intent.

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

This allows Trust to scale without weakening determinism.

⸻

27. Waiting State Taxonomy

WAITING should identify the missing condition.

Canonical examples:

WAITING_FOR_CLARIFICATION
WAITING_FOR_EVIDENCE
WAITING_FOR_AUTHORIZATION
WAITING_FOR_CONFIRMATION
WAITING_FOR_APPROVAL
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE

A future implementation may add additional subtypes.

⸻

28. WAITING_FOR_CLARIFICATION

Used when the missing requirement is semantic.

Example:

Intent:
"Cancel the subscription."
Problem:
Multiple subscriptions exist.

State:

WAITING_FOR_CLARIFICATION

After clarification:

Intent updated
    ↓
EVALUATING

⸻

29. WAITING_FOR_EVIDENCE

Used when the Intent is sufficiently understood but required evidence has not yet been established.

Example:

Identity verification required
Evidence = missing

Result:

WAITING_FOR_EVIDENCE

⸻

30. WAITING_FOR_AUTHORIZATION

Used when authorization is required but has not yet been established and may still be obtained.

This is distinct from:

BLOCKED_BY_AUTHORIZATION

where authorization has explicitly been denied or the Actor is outside permitted authority.

⸻

31. WAITING_FOR_CONFIRMATION

Used when the Actor must explicitly confirm the Action.

Example:

"This will permanently delete 15,000 records. Continue?"

Until the required confirmation is established:

WAITING_FOR_CONFIRMATION

Confirmation becomes structured evidence for the Trust evaluation.

⸻

32. WAITING_FOR_APPROVAL

Used when a separate authorized approver must approve the Action.

Example:

Transfer > ₦10M
        ↓
Secondary approval required
        ↓
WAITING_FOR_APPROVAL

Approval must be bound to the applicable Intent scope and version.

⸻

33. WAITING_FOR_CAPABILITY

Used when execution is permitted in principle but the required execution capability is temporarily unavailable.

Example:

Payment capability:
UNAVAILABLE

Result:

WAITING_FOR_CAPABILITY

The Action is not thereby denied.

⸻

34. BLOCKED State Taxonomy

BLOCKED should identify why execution is prohibited.

Examples:

BLOCKED_BY_AUTHORIZATION
BLOCKED_BY_POLICY
BLOCKED_BY_CONSTRAINT
BLOCKED_BY_RISK
BLOCKED_BY_SCOPE
BLOCKED_BY_RESOURCE

This provides deterministic, machine-readable explanation.

⸻

35. Waiting vs Blocking

This distinction is foundational:

WAITING
"Not yet."
BLOCKED
"No, under the current conditions."

Examples:

Approval missing
→ WAITING
Policy prohibits Action
→ BLOCKED

A blocked condition must not be represented as merely low confidence.

⸻

36. Unknown vs Blocked

UNKNOWN is a condition state, not necessarily a Trust state.

Example:

Authorization service unavailable.

Correct interpretation:

Authorization = UNKNOWN

not:

Authorization = ALLOWED

and not necessarily:

Authorization = DENIED

For consequential Actions:

UNKNOWN mandatory condition
        ↓
NOT READY

The eventual Trust state may be WAITING if the condition is recoverable, or BLOCKED if applicable policy explicitly prohibits proceeding under uncertainty.

⸻

37. Fail-Closed Transition

For consequential Actions:

READY
  ↓
Trust dependency becomes unavailable
  ↓
EVALUATING
  ↓
WAITING / BLOCKED

Never:

dependency unavailable
      ↓
READY

Unknown must not silently satisfy a mandatory Trust condition.

⸻

38. Recovery

Trust states must support recoverable transitions.

Example:

WAITING_FOR_CAPABILITY
        ↓
Capability restored
        ↓
EVALUATING
        ↓
READY

Likewise:

BLOCKED_BY_POLICY
        ↓
Policy changes
        ↓
EVALUATING
        ↓
READY

provided all other mandatory conditions are satisfied.

⸻

39. Terminal Execution States

The lifecycle contains execution terminal states:

COMPLETED
FAILED

However, Trust itself should generally remain concerned with execution eligibility.

A production architecture may therefore represent:

Trust State:
READY
Execution State:
EXECUTING

and later:

Trust State:
READY
Execution State:
COMPLETED

rather than collapsing both concepts into one enum.

This separation remains the preferred conceptual model until implementation semantics are finalized.

⸻

40. Trust and Outcome

The canonical relationship is:

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

Trust does not determine whether an external system succeeds.

⸻

41. Composite Intents

Composite Intents require deterministic state aggregation.

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

unless the Intent explicitly defines another composition policy.

⸻

42. Partial Execution

If an Intent explicitly permits partial execution, components may progress independently.

Example:

A → EXECUTING
B → WAITING
C → READY

But Noema must not infer permission for partial execution.

Partial execution must be established by the Intent’s semantics and governing policy.

⸻

43. Atomicity

For an atomic composite Intent:

A + B + C

the required Trust conditions must hold for the composite execution unit.

The State Machine must not permit:

A executes
B blocked
C executes

when the Intent semantics require atomic execution.

⸻

44. Trust and Autonomy

Trust state and autonomy level are related but distinct.

For example:

Trust:
READY
Autonomy:
APPROVAL_REQUIRED

may be meaningful if the Action is executable after an approval control, even though it is not eligible for autonomous execution.

The Trust Model should therefore distinguish:

Execution Eligibility

from:

Autonomy Eligibility

where required by the policy model.

⸻

45. Human Intervention

Human intervention produces explicit state transitions.

Example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING
        ↓
READY

The approval is structured evidence.

It is not merely a conversational event.

The Model must never simulate or fabricate approval.

⸻

46. Clarification

Clarification similarly produces a state transition:

UNRESOLVED
     ↓
clarification.requested
     ↓
clarification.received
     ↓
Intent updated
     ↓
EVALUATING

The new information becomes part of the Intent’s resolved semantic state.

⸻

47. State Transition Guards

Transitions must be governed by explicit predicates.

For example:

READY

requires:

guard(
    allMandatoryRequirementsSatisfied
    AND
    noBlockingCondition
)

while:

WAITING_FOR_APPROVAL

requires something equivalent to:

guard(
    approvalRequired
    AND
    approvalMissing
    AND
    noCurrentBlockingCondition
)

The exact predicates are implementation-specific.

Their deterministic nature is canonical.

⸻

48. No Probabilistic Transitions

The State Machine must never contain transitions such as:

80% chance → READY

or:

Model confidence > 0.8 → READY

Trust transitions are governed by explicit predicates.

⸻

49. State Transition Actions

A transition may cause deterministic system effects such as:

* create clarification request
* record missing requirement
* issue approval request
* invalidate a stale Execution Contract
* create an Execution Contract
* emit a Trust event
* record a Trust evaluation

However, state transitions must not hide arbitrary side effects.

The State Machine should remain auditable and predictable.

⸻

50. Execution Contract Invalidation

A particularly important consequence of Trust invalidation is Execution Contract invalidation.

If:

Trust = READY

and a material condition changes before execution:

READY
   ↓
material change
   ↓
EVALUATING

then any previously issued Execution Contract must not automatically remain executable.

Conceptually:

Trust invalidated
      ↓
Execution Contract invalidated
      ↓
Re-evaluation
      ↓
New Execution Contract if READY

This prevents stale authorization from crossing the execution boundary.

⸻

51. Trust State History

Every significant Trust transition should be auditable.

Example:

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

This creates a reconstructible Trust history.

⸻

52. State Transition Provenance

Each significant transition should record at least:

previous_state
event
new_state
timestamp
intent_id
intent_version
evaluation_id
relevant_evidence
reason

Where applicable, it should also preserve:

policy_versions
authorization_reference
risk_rule_version
constraint_results
context_reference

This allows Noema to reconstruct why the transition occurred.

⸻

53. Trust Evaluation and State Transition

The Trust Engine evaluates conditions.

The State Machine interprets the resulting evaluation.

Conceptually:

Intent State
     ↓
Trust Evaluation
     ↓
Trust Decision
     ↓
State Transition

For example:

Evaluation:
approval missing
Decision:
WAITING_FOR_APPROVAL
State:
WAITING

The State Machine should not independently invent Trust conditions that the Trust Model does not define.

⸻

54. State Machine and Determinism

Given:

Current State
+
Material Event
+
Current Relevant Conditions
+
Applicable Rule Versions

the next state must be deterministic.

Example:

WAITING_FOR_APPROVAL
+
approval.received
+
all other mandatory conditions satisfied
=
READY

Not:

maybe READY

⸻

55. Re-Entrancy and Duplicate Events

Implementations should make state transitions robust to duplicate or replayed events.

For example, receiving the same:

approval.received

event more than once should not create multiple Trust transitions or mutate authorization semantics.

Trust evaluation should remain idempotent for the same Intent state and relevant inputs.

⸻

56. Ordering and Stale Events

State transitions must account for event ordering.

A stale event must not overwrite a newer Trust state.

For example:

T1: authorization.granted
T2: authorization.revoked

A delayed replay of the authorization.granted event must not silently restore:

READY

without evaluating the current authoritative authorization state.

The current condition set, not event arrival order alone, determines Trust.

⸻

57. Intent Versioning

Trust belongs to an Intent version.

Conceptually:

Intent v1
   ↓
Trust Evaluation v1

If the Intent materially changes:

Intent v2
   ↓
new Trust Evaluation

Trust must not silently transfer between materially different Intent versions.

Example:

v1:
Transfer ₦1M
v2:
Transfer ₦20M

The State Machine must require re-evaluation.

⸻

58. Trust and Semantic Change

Not every update to an Intent is necessarily material.

A future implementation may distinguish:

non-material update

from:

material semantic change

Material changes include changes to:

* Action
* Resource
* Actor
* scope
* amount
* destination
* constraints
* execution conditions
* other Trust-relevant semantics

A material change invalidates the prior Trust evaluation.

⸻

59. Dependency-Aware Invalidation

Trust invalidation should eventually support dependency relationships.

Conceptually:

Policy P1
   ↓
Intent I7

or:

Authorization A2
   ↓
Intent I7

If P1 or A2 changes, I7 becomes a candidate for re-evaluation.

This provides a path toward efficient large-scale Trust evaluation.

⸻

60. Trust and External State

Trust does not guarantee external business-state validity.

For example:

Trust = READY

does not mean:

Database transaction = guaranteed

It means:

Noema has established that the Intent satisfies the applicable conditions under Noema’s Trust model for crossing the execution boundary.

The consumer remains authoritative over its own business invariants.

⸻

61. TOCTOU Consideration

Trust state can become stale between evaluation and execution.

Example:

Check:
Account balance sufficient
Time passes
Execute:
Balance no longer sufficient

Therefore high-consequence execution may require:

Trust Evaluation
      ↓
Execution Preparation
      ↓
Final validation / consumer enforcement
      ↓
Execution

The external system must enforce authoritative transactional conditions.

⸻

62. Trust and Consumer Enforcement

Noema’s Trust State Machine must not replace consumer-side business invariants.

For example:

Noema:
Trust = READY

The bank or payment system may still enforce:

balance >= amount

transactionally.

This preserves the boundary between:

Execution Eligibility

and:

Business-State Validity

⸻

63. Trust and Execution Outcome

After execution begins:

Trust:
READY
Execution:
EXECUTING
Outcome:
SUCCESS / FAILED / PARTIAL / UNKNOWN

A successful outcome does not retrospectively make Trust valid.

Likewise, a failed outcome does not necessarily make the preceding Trust decision invalid.

The two concerns must remain causally distinct.

⸻

64. State Machine Invariants

Invariant 1

Every Trust state transition must have a defined cause.

Invariant 2

Trust transitions are deterministic.

Invariant 3

Unknown mandatory conditions cannot transition an Intent to READY.

Invariant 4

WAITING and BLOCKED are semantically distinct.

Invariant 5

A material change to a Trust-relevant condition can invalidate READY.

Invariant 6

Satisfying one requirement triggers re-evaluation rather than blindly granting Trust.

Invariant 7

A BLOCKED Intent cannot cross the execution boundary.

Invariant 8

An UNRESOLVED Intent cannot cross the execution boundary.

Invariant 9

READY does not imply successful execution.

Invariant 10

Execution outcomes do not retroactively determine whether the Trust decision was valid.

Invariant 11

A materially changed Intent requires a new Trust evaluation.

Invariant 12

Trust history must be reconstructible.

Invariant 13

A stale or invalidated Execution Contract must not remain executable.

Invariant 14

Duplicate or stale events must not silently produce an invalid Trust state.

Invariant 15

The current authoritative condition set governs Trust; event arrival alone does not establish Trust.

Invariant 16

No Model output may directly cause a Trust transition to READY.

Invariant 17

Partial execution cannot be inferred merely because individual components are READY.

Invariant 18

Trust state and external business state remain distinct.

⸻

65. Canonical State Flow

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

66. Canonical Mental Model

The State Machine can be reduced to four questions:

1. Do we understand the Intent?

UNRESOLVED

2. Are we evaluating its current Trust conditions?

EVALUATING

3. Has execution eligibility been established?

WAITING
BLOCKED
READY

4. Has execution actually occurred?

EXECUTING
COMPLETED
FAILED

Thus:

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

67. Canonical Relationship of Trust Artifacts

The three foundational Trust documents should be understood as:

                 TRUST MODEL
              "What does Trust mean?"
                       │
                       ▼
                TRUST ENGINE
          "What is Trust right now?"
                       │
                       ▼
           TRUST STATE MACHINE
        "How does Trust evolve over time?"

Together:

Trust Model
    ↓
defines semantics
Trust Engine
    ↓
evaluates semantics
Trust State Machine
    ↓
governs transitions

This separation should remain canonical.

⸻

68. Architectural Boundary

The resulting Noema boundary is:

Natural Language
       ↓
Model Interpretation
       ↓
Intent
       ↓
Resolution
       ↓
Evidence
       ↓
Trust Evaluation
       ↓
Trust State
       ↓
READY
       ↓
Execution Contract
       ↓
Consumer
       ↓
Execution
       ↓
Outcome

The State Machine does not execute.

The Trust Engine does not execute.

The Model does not authorize execution.

The execution consumer performs the Action.

⸻

69. Final Definition

The Trust State Machine defines how Noema moves an Intent through deterministic Trust and execution-eligibility states as semantic resolution, evidence, authorization, policy, risk, capability, constraints, context, freshness, and execution conditions change over time.

Its fundamental rule is:

Noema moves an Intent into READY only when the State Machine’s deterministic guards establish that all mandatory Trust conditions are currently satisfied.

And its temporal rule is:

READY is conditional, not permanent. Any material change to a Trust-relevant condition requires re-evaluation before execution may proceed.