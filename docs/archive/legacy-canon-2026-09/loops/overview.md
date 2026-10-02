> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Overview

# Loops
Status: Foundational
Version: 0.1
Domain: Loops
Canonical Path: loops/overview.md
⸻
## 1. Definition
Noema’s Loops are explicit control structures through which an Intent, its execution, its unresolved conditions, and the resulting operational knowledge may move through repeated evaluation.
A Loop exists because Noema operates in an environment where:
* semantic information may be incomplete
* execution may be asynchronous
* external state may change
* Actions may fail
* outcomes may be uncertain
* human intervention may be required
* operational conditions may evolve
A Loop therefore represents controlled continuation.
It does not represent uncontrolled recursion.
The canonical principle is:
```text
Condition
   ↓
Evaluation
   ↓
Action
   ↓
Observation
   ↓
Re-evaluation

The loop continues only while its governing semantics permit continuation.

⸻

2. Why Loops Exist

Noema cannot assume that every Intent can proceed through a single linear lifecycle.

Examples include:

Intent
  ↓
Missing information
  ↓
Clarification
  ↓
Updated Intent
  ↓
Validation

or:

Action
  ↓
Execution
  ↓
Unknown outcome
  ↓
Recovery / observation
  ↓
Re-evaluation

or:

Execution
  ↓
Observed failure
  ↓
Operational learning
  ↓
Updated operational knowledge

Loops provide explicit semantics for these recurring transitions.

⸻

3. Core Principle

Noema must never create an implicit loop merely because a model continues generating actions, questions, or plans.

Every consequential loop must have:

* an explicit entry condition
* an explicit continuation condition
* a defined state
* bounded or governed repetition
* observable transitions
* a termination condition
* failure semantics
* provenance

Therefore:

Loop ≠ repeated model generation

A Loop is an architectural control structure.

⸻

4. Loop Taxonomy

The canonical Noema architecture currently recognizes three primary loops:

1. Clarification Loop
2. Execution Loop
3. Operational Learning Loop

Conceptually:

                 ┌───────────────────┐
                 │   Clarification   │
                 │       Loop        │
                 └─────────┬─────────┘
                           │
                           ▼
                    Resolved Intent
                           │
                           ▼
                 ┌───────────────────┐
                 │    Execution      │
                 │       Loop        │
                 └─────────┬─────────┘
                           │
                           ▼
                        Outcome
                           │
                           ▼
                 ┌───────────────────┐
                 │    Operational    │
                 │     Learning      │
                 │       Loop        │
                 └───────────────────┘

These loops have different responsibilities.

They must not be collapsed into one generalized feedback mechanism.

⸻

5. Clarification Loop

The Clarification Loop governs unresolved semantic Intent.

Its purpose is to establish information required to resolve what the Actor intends.

Conceptually:

Candidate Intent
      ↓
Semantic Evaluation
      ↓
Required information missing?
      │
   ┌──┴──┐
   │     │
  Yes    No
   │     │
   ▼     ▼
Clarify  Resolved Intent
   │
   ▼
Actor Response
   │
   ▼
Intent Re-resolution

The Clarification Loop belongs primarily to the Intent Engine boundary.

It must not become an execution mechanism.

⸻

6. Execution Loop

The Execution Loop governs the controlled progression of an executable Action Graph through execution.

Conceptually:

Executable Action Graph
          ↓
Ready Action
          ↓
Contract Validation
          ↓
Execution
          ↓
Observation
          ↓
State Transition
          ↓
Next Ready Action

The loop may encounter:

* success
* failure
* retry
* waiting
* human intervention
* compensation
* unknown outcome
* graph invalidation
* material external-state change

The Execution Loop must follow explicit Action Contract and graph semantics.

It must not improvise execution behavior.

⸻

7. Operational Learning Loop

The Operational Learning Loop governs the conversion of observed execution behavior into controlled operational knowledge.

Conceptually:

Execution
    ↓
Outcome
    ↓
Observation
    ↓
Analysis
    ↓
Operational Knowledge
    ↓
Engineering / Policy / Capability Change
    ↓
Future Execution

The Operational Learning Loop does not silently modify historical execution.

Learning applies to future behavior through explicitly governed changes.

Operational learning must therefore remain distinct from:

* Intent resolution
* Trust evaluation
* execution authorization
* historical outcome reconstruction

⸻

8. Loops Are Not Authority

A Loop does not itself establish authority.

For example:

Execution Loop
     ↓
Retry

does not mean that retry is permitted.

The applicable Action Contract must establish retry semantics.

Similarly:

Clarification Loop
     ↓
Actor response

does not mean that the response automatically establishes semantic truth.

The Intent Engine must resolve the response.

And:

Operational Learning
     ↓
New policy

does not mean that the learning system may directly change policy.

The appropriate governance mechanism must authorize the change.

⸻

9. Loop State

Every Loop should have explicit state.

Conceptually:

Loop {
    id
    type
    subject
    iteration
    state
    entry_condition
    continuation_condition
    termination_condition
    limits
    provenance
}

Possible states include:

NOT_STARTED
ACTIVE
WAITING
BLOCKED
TERMINATING
COMPLETED
FAILED
ABORTED
UNKNOWN

The exact state model may vary by Loop.

Loop state must not be conflated with Intent state, Trust state, Graph state, or Execution state.

⸻

10. Loop Identity

Each Loop should have a stable identity.

For example:

clarification_loop_id
execution_loop_id
learning_loop_id

The identity permits Noema to distinguish:

* one loop instance from another
* iterations within a loop
* loop revisions
* loop termination
* loop history

A loop iteration is not a new loop identity.

⸻

11. Iteration

Each Loop iteration should be explicitly observable.

Conceptually:

Loop
  ↓
Iteration 1
  ↓
Observation
  ↓
Iteration 2
  ↓
Observation
  ↓
Iteration 3

Each iteration should preserve:

* iteration number
* triggering event
* input state
* evaluation result
* action taken
* resulting state
* timestamp
* provenance

This permits reconstruction of loop behavior.

⸻

12. Loop Entry

A Loop must have an explicit entry condition.

Examples:

Clarification Loop:

required semantic information unresolved

Execution Loop:

executable graph contains ready actions

Operational Learning Loop:

new operational observation available for analysis

A Loop must not begin merely because a model believes continuation would be useful.

⸻

13. Loop Continuation

Continuation must be determined by explicit conditions.

Examples:

Clarification:
continue while required semantic information remains unresolved
Execution:
continue while mandatory executable work remains
Learning:
continue while defined analysis and governance stages remain incomplete

Continuation must be deterministic where the governing semantics require determinism.

⸻

14. Loop Termination

Every Loop must have explicit termination semantics.

Termination may result from:

* successful completion
* resolution
* cancellation
* timeout
* retry exhaustion
* unrecoverable failure
* policy prohibition
* external termination
* resource exhaustion
* explicit Actor decision

A Loop without a defined termination mechanism is not a valid production control structure.

⸻

15. Bounded Repetition

Noema must distinguish between:

bounded iteration

and:

unbounded repetition

A Loop may be bounded by:

* maximum iterations
* maximum retries
* timeout
* deadline
* resource budget
* state-transition limit
* policy-defined threshold

Where an inherently open-ended process is legitimate, it must still have explicit governance and termination conditions.

⸻

16. Loop Safety

A Loop must not repeatedly perform consequential operations without explicit authorization for repetition.

For example:

CREATE_PAYMENT
   ↓
retry
   ↓
CREATE_PAYMENT

requires idempotency and retry semantics.

The existence of a Loop does not establish permission to repeat an Action.

⸻

17. Loop and Idempotency

Repeated execution must respect Action idempotency semantics.

Conceptually:

Loop
 ↓
Action Attempt
 ↓
Unknown
 ↓
Retry?

Before retrying, Noema must establish whether:

* retry is permitted
* the Action is idempotent
* an idempotency key exists
* the external system supports safe repetition
* the failure class is retryable

The Loop must defer to the applicable Action Contract.

⸻

18. Loop and Unknown Outcomes

An unknown result must not automatically become:

FAILED

or:

SUCCESS

For example:

Action
  ↓
network timeout
  ↓
UNKNOWN
  ↓
Outcome Resolution

The Loop may then:

* wait
* query authoritative state
* retry where permitted
* escalate
* terminate as unknown

The appropriate behavior must be explicitly defined.

⸻

19. Loop and External State

External state may change between iterations.

Therefore:

Iteration 1:
Account = ACTIVE
Iteration 2:
Account = SUSPENDED

The Loop must not assume that observations from an earlier iteration remain current.

Consequential transitions may require fresh authoritative checks.

⸻

20. Loop and Re-Evaluation

A Loop exists partly because the environment may change.

Therefore an iteration may produce:

State Change
     ↓
Re-evaluation
     ↓
Continue

or:

State Change
     ↓
Re-evaluation
     ↓
Terminate

Re-evaluation must use the current applicable state and rules.

Historical observations remain historical.

⸻

21. Loop and Trust

Loops do not bypass Trust.

If a material Intent change occurs during a loop:

Intent v1
   ↓
Execution
   ↓
Material change
   ↓
Intent v2
   ↓
Validation
   ↓
Trust re-evaluation

The previous Trust decision must not silently transfer to the changed Intent.

Similarly, a changed Action Graph may require revalidation before execution continues.

⸻

22. Loop and Action Graph

The Action Graph provides the explicit execution structure.

The Execution Loop traverses that structure according to its semantics.

Therefore:

Action Graph
     ↓
Execution Loop
     ↓
Action execution

The Loop does not redefine the graph.

If the graph must materially change, that change must be explicit and versioned.

⸻

23. Loop and Action Contracts

Action Contracts define executable obligations.

The Loop is responsible for applying those semantics over time.

For example, a contract may specify:

max_attempts = 3
retryable = TIMEOUT
idempotency_required = true

The Execution Loop applies these rules.

It must not invent:

max_attempts = 10

because the model believes additional retries may help.

⸻

24. Human Intervention

Human intervention may suspend or alter a Loop.

Example:

Execution
   ↓
Approval required
   ↓
WAITING_FOR_HUMAN
   ↓
Approval
   ↓
Re-evaluation
   ↓
Continue

Human intervention must be represented explicitly.

Silence is not approval.

Conversational continuation is not automatically approval.

⸻

25. Clarification Does Not Equal Approval

The Clarification Loop resolves semantic meaning.

Approval governs authorization or governance conditions.

Therefore:

Clarification response

must not automatically be interpreted as:

Approval

The two loops may interact but must retain distinct semantics.

⸻

26. Loop Cancellation

A Loop may be cancelled.

Cancellation should be an explicit event:

ACTIVE
  ↓
cancel requested
  ↓
CANCELLING
  ↓
CANCELLED

Cancellation semantics must define whether:

* current work stops immediately
* in-flight work completes
* compensation is required
* external cancellation is attempted
* the resulting outcome is partial

The implementation must not assume cancellation is equivalent to rollback.

⸻

27. Loop Timeouts

Loops may have deadlines.

Example:

Clarification deadline = 24 hours

or:

Execution deadline = 30 minutes

When a deadline is reached, the Loop must transition according to explicit semantics.

Timeout must not silently become success.

⸻

28. Loop Failure

A Loop may fail even when individual iterations succeeded.

For example:

Iteration 1 = SUCCESS
Iteration 2 = SUCCESS
Iteration 3 = FAILURE

The Loop outcome must reflect the defined aggregate semantics.

Partial progress must remain observable.

⸻

29. Loop Recovery

Recovery from Loop failure must be explicit.

Possible responses include:

RETRY
RESUME
COMPENSATE
ESCALATE
TERMINATE
REPLAN

Recovery behavior must be governed by the relevant architecture and contracts.

The Loop must not dynamically invent recovery behavior.

⸻

30. Loop Re-entry

A terminated Loop may or may not be eligible for re-entry.

If re-entry is permitted, it must create an explicit new Loop instance or governed continuation.

For example:

Execution Loop 1
     ↓
TERMINATED
     ↓
material change
     ↓
Execution Loop 2

The relationship between the two instances must be recorded.

A terminated loop must not silently resume.

⸻

31. Loop Nesting

Loops may contain sub-loops.

For example:

Execution Loop
     ↓
   Action
     ↓
Retry Loop

or:

Clarification Loop
     ↓
External Evidence Retrieval
     ↓
Resolution Loop

Nested loops must retain explicit ownership and termination semantics.

An inner loop must not silently override the state of its parent.

⸻

32. Loop Composition

Multiple loops may interact.

Conceptually:

Clarification
      ↓
Execution
      ↓
Outcome
      ↓
Operational Learning

However, the output of one loop does not automatically become permission for another.

Each transition must satisfy the receiving subsystem’s requirements.

⸻

33. Loop Events

Conceptual loop events include:

loop.started
loop.iteration_started
loop.iteration_completed
loop.waiting
loop.blocked
loop.resumed
loop.retry_requested
loop.retry_exhausted
loop.intervention_required
loop.re_evaluation_required
loop.completed
loop.failed
loop.cancelled
loop.expired
loop.terminated

These events are illustrative.

The canonical event taxonomy may be defined separately.

⸻

34. Loop Observability

Noema should be able to reconstruct:

* why the Loop started
* what state existed at entry
* which iterations occurred
* what each iteration observed
* what decisions were made
* which Actions were executed
* which conditions changed
* why continuation occurred
* why termination occurred
* what final state resulted

This is required for reliable operation and auditability.

⸻

35. Loop Provenance

Each consequential transition should retain provenance.

Provenance may include:

* triggering event
* source state
* rule version
* contract version
* graph version
* Intent version
* actor input
* external evidence
* execution result
* system component
* timestamp

The goal is reconstructibility.

It is not necessary to retain private model reasoning.

⸻

36. Model Participation

Models may participate in loops.

Examples:

LLM → candidate clarification
LLM → candidate recovery strategy
LLM → operational analysis

However, model output remains advisory unless a deterministic governing mechanism explicitly establishes its authority for the relevant operation.

Models must not silently control Loop state.

⸻

37. No Model-Controlled Recursion

A model must not be allowed to generate:

Action
  ↓
Action
  ↓
Action
  ↓
...

without an explicit Loop boundary.

Likewise, a model must not extend a loop indefinitely because it believes additional work is useful.

Loop continuation belongs to system-defined semantics.

⸻

38. Loop Determinism

Where Loop behavior is governed by deterministic rules, equivalent inputs and state should produce reproducible transitions.

Model-assisted components may introduce probabilistic proposals.

The authoritative state transition must remain governed by explicit system rules.

⸻

39. Loop State Machines

Each Loop should be representable as a state machine.

Example:

NOT_STARTED
     ↓
ACTIVE
  ┌──┼───────────┐
  ↓  ↓           ↓
WAIT BLOCKED   FAILED
  │  │           │
  └──┴─────┬─────┘
            ↓
         RESUMED
            ↓
          ACTIVE
            ↓
       COMPLETED

The exact state machine depends on the Loop type.

The important principle is explicit state transition.

⸻

40. Loop Invariants

The following invariants apply across Noema Loops.

Invariant 1

Every consequential Loop must have explicit entry and termination semantics.

Invariant 2

Loop continuation must be governed by explicit conditions.

Invariant 3

Loop repetition must not itself grant execution authority.

Invariant 4

Repeated Actions must respect Action Contract and idempotency semantics.

Invariant 5

Unknown outcomes must remain explicitly unknown until resolved.

Invariant 6

Material state changes may require re-evaluation.

Invariant 7

Loops must not silently bypass Trust.

Invariant 8

Loop state must remain distinct from Intent, Trust, Graph, and Execution state.

Invariant 9

Loop iterations must be observable.

Invariant 10

Loop transitions must be auditable.

Invariant 11

Model output must not silently control consequential Loop state.

Invariant 12

Unbounded repetition is prohibited unless explicitly governed.

Invariant 13

Cancellation is distinct from failure.

Invariant 14

Timeout is distinct from success.

Invariant 15

A terminated Loop must not silently resume.

Invariant 16

Operational learning must not silently mutate historical execution.

⸻

41. Canonical Loop Relationships

The broader Noema lifecycle can be represented as:

Actor
  ↓
Expression
  ↓
Intent Engine
  ↓
┌─────────────────────┐
│ Clarification Loop  │
└──────────┬──────────┘
           ↓
     Canonical Intent
           ↓
      Validation
           ↓
         Trust
           ↓
     Action Graph
           ↓
┌─────────────────────┐
│  Execution Loop     │
└──────────┬──────────┘
           ↓
        Outcome
           ↓
┌─────────────────────┐
│ Operational Learning│
│       Loop          │
└─────────────────────┘

Each Loop operates on a different architectural concern.

⸻

42. Loop Boundaries

The three primary Loops have distinct boundaries.

Clarification Loop

Concern:

What does the Actor mean?

Primary authority:

Intent Engine

Execution Loop

Concern:

How does the executable Action Graph progress?

Primary authorities:

Action Graph
Action Contracts
Execution architecture
Trust requirements

Operational Learning Loop

Concern:

What operational knowledge should future system behavior incorporate?

Primary authorities:

Operational governance
Engineering controls
Policy governance
Capability governance

These concerns must not be conflated.

⸻

43. Loop Interaction With Outcome

Outcome is an observation of what occurred.

It may cause:

Execution
   ↓
Outcome
   ↓
Re-evaluation

But Outcome does not automatically rewrite:

* Intent
* Trust
* Action Graph
* Action Contract

Any such change must occur through an explicit transition.

⸻

44. Loop and Replanning

Replanning may be required when the existing Action Graph can no longer satisfy its execution conditions.

Conceptually:

Execution
   ↓
Material change
   ↓
Graph invalidation
   ↓
Replanning
   ↓
Graph v2
   ↓
Validation / Trust
   ↓
Execution

Replanning is therefore a governed transition.

It is not an implicit property of the Execution Loop.

⸻

45. Loop and Durable Execution

Loops may span substantial periods.

Examples:

Waiting for approval
Waiting for clarification
Waiting for external system recovery
Waiting for delivery confirmation

The system must therefore preserve sufficient durable state to resume the Loop correctly.

Durability must preserve:

* Loop identity
* iteration state
* relevant Intent version
* graph version
* Action state
* pending dependencies
* deadlines
* retry state
* provenance

The Loop must be resumable without relying on ephemeral model context.

⸻

46. Loop and Failure Recovery

Failure recovery belongs to the applicable recovery semantics.

A Loop may initiate recovery, but recovery must respect:

* Action Contracts
* idempotency
* compensation
* deadlines
* Trust requirements
* external system authority

Failure must not cause uncontrolled repetition.

⸻

47. Loop and Security

Loops must not provide an avenue for privilege escalation.

For example:

failed authorization
   ↓
retry
   ↓
authorization succeeds

must not occur merely because the Loop repeated the request.

Authorization must be evaluated according to the governing Trust and security semantics.

Similarly, a model must not use repeated loop iterations to discover capabilities that were previously unavailable.

⸻

48. Loop and Resource Control

Loops consume resources.

Controls may include:

* iteration limits
* concurrency limits
* execution budgets
* rate limits
* queue limits
* timeout
* backoff
* circuit breakers

Resource controls are engineering constraints.

They must not silently change semantic Intent.

⸻

49. Loop and Scalability

Loops must be designed for potentially large numbers of concurrent instances.

A scalable implementation should avoid requiring:

* persistent in-memory state for every loop
* unbounded polling
* synchronous blocking across long waits
* repeated full graph reconstruction

Durable event/state mechanisms should permit suspended loops to consume minimal active resources.

⸻

50. Loop and Observability

Loop observability should support both:

Operational visibility

How many loops are active?
How long are they waiting?
Where are they blocked?
What failures are recurring?

Reconstruction

Why did this Loop continue?
Why did it stop?
What state existed at each iteration?

Metrics alone are insufficient for reconstruction.

Logs alone are insufficient for reliable aggregate analysis.

Noema should preserve structured loop events and state.

⸻

51. Loop Testing

Loops require testing beyond ordinary unit tests.

Testing should include:

* state-transition tests
* termination tests
* timeout tests
* retry tests
* idempotency tests
* crash-recovery tests
* duplicate-event tests
* concurrent-iteration tests
* stale-state tests
* unknown-outcome tests
* cancellation tests
* compensation tests
* long-duration tests
* property-based tests where appropriate

The goal is to establish that loops remain bounded, recoverable, and semantically correct under failure.

⸻

52. Loop Failure Modes

Noema should explicitly distinguish:

Infinite repetition

Continuation never reaches a termination condition.

→ Must be prevented by bounds or governance.

Premature termination

Loop stops before required conditions are satisfied.

→ Must be detected by completion semantics.

Incorrect continuation

Loop continues after continuation conditions cease to hold.

→ Must transition according to explicit state rules.

Unsafe repetition

An Action is repeated without appropriate idempotency or contract semantics.

→ Must be blocked.

State loss

Loop cannot resume after interruption.

→ Durable state must prevent this.

Semantic drift

Loop changes the meaning of the Intent through repeated processing.

→ Intent versioning and semantic boundaries must prevent this.

Authority drift

Loop repetition is treated as permission.

→ Trust and Contract boundaries must prevent this.

⸻

53. Canonical Loop Contract

Conceptually:

LoopContract {
    loop_type
    subject
    entry_condition
    continuation_condition
    termination_condition
    state_model
    iteration_policy
    timeout_policy
    retry_policy
    failure_policy
    cancellation_policy
    durability_requirements
    provenance_requirements
}

The exact schema may evolve.

The architectural principle is that Loop behavior must be explicit.

⸻

54. Loop Lifecycle

The generalized lifecycle is:

DEFINED
   ↓
STARTED
   ↓
ACTIVE
   ↓
ITERATING
   ↓
OBSERVING
   ↓
RE-EVALUATING
   ↓
┌───────────────┐
│ CONTINUE      │
│ WAIT          │
│ BLOCK         │
│ RECOVER       │
│ TERMINATE     │
└───────────────┘

A Loop may transition between these states according to its specific semantics.

⸻

55. Canonical Mental Model

Noema Loops answer five questions:

1. Why did the process continue?
2. What changed since the previous iteration?
3. What is permitted to happen next?
4. What prevents uncontrolled repetition?
5. What condition ends the Loop?

This produces:

Trigger
  ↓
State
  ↓
Evaluation
  ↓
Permitted Transition
  ↓
Observation
  ↓
Continue / Wait / Recover / Terminate

⸻

56. Final Definition

Noema’s Loops are explicit, governed control structures that permit semantic clarification, durable execution, recovery, and operational learning to continue across changing conditions without collapsing distinct architectural responsibilities.

The central invariant is:

Noema does not loop because a model keeps asking,
planning, or acting.
Noema loops because an explicit system-defined condition
requires another governed evaluation or transition.

The primary loops are:

Clarification Loop
        ↓
Canonical Intent
        ↓
Execution Loop
        ↓
Outcome
        ↓
Operational Learning Loop

Each loop remains bounded by explicit state, authority, contracts, provenance, observability, and termination semantics.