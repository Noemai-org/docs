ADR-011 — Intent State Separate from Execution State

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Intent / Execution
Canonical Path: decisions/ADRs/ADR-011-intent-state-separate-from-execution-state.md

⸻

1. Decision

Noema will maintain a strict architectural distinction between Intent State and Execution State.

Intent State describes the lifecycle and semantic condition of the Intent as understood and managed by Noema.

Execution State describes what has happened, or is happening, when an execution consumer attempts to perform an Action.

These states must not be collapsed into a single lifecycle or treated as interchangeable.

The canonical relationship is:

Intent
   │
   ├───────────────┐
   ▼               ▼
Intent State   Trust State
                   │
                   ▼
          Execution Eligibility
                   │
                   ▼
          Execution Contract
                   │
                   ▼
          Execution State
                   │
                   ▼
               Outcome

⸻

2. Context

Noema operates across several fundamentally different domains of state.

An Intent may progress from being expressed, interpreted, unresolved, clarified, resolved, validated, and eventually eligible for execution.

Separately, an execution consumer may accept an Execution Contract, begin execution, complete successfully, fail, partially complete, or return an unknown result.

These are different facts.

For example:

Intent State:
RESOLVED
Trust State:
READY
Execution State:
FAILED

The execution failure does not mean that the Intent was unresolved.

Similarly:

Intent State:
RESOLVED
Trust State:
BLOCKED
Execution State:
NOT_STARTED

The absence of execution is not an execution failure.

Without an explicit separation, Noema risks incorrectly treating execution outcomes as evidence about semantic understanding or Trust decisions.

⸻

3. Problem

A single state machine creates several ambiguities.

3.1 Semantic ambiguity

If FAILED is an Intent state, it becomes unclear whether:

* the Intent was misunderstood
* validation failed
* Trust was denied
* execution failed
* an external system failed
* the outcome was unknown

These are materially different conditions.

3.2 Trust ambiguity

A successful execution does not prove that a Trust decision was correct.

Likewise, an execution failure does not prove that a Trust decision was incorrect.

Trust establishes execution eligibility.

Execution establishes what happened when an execution consumer attempted the Action.

3.3 Lifecycle ambiguity

An Intent can remain semantically resolved even after execution fails.

The same Intent may subsequently be retried, revised, compensated, or explicitly terminated according to its semantics.

3.4 Ownership ambiguity

Noema owns Intent State.

The execution consumer and/or authoritative enterprise system determines execution and business outcomes.

Combining these states would blur the boundary between Noema-owned intent lifecycle and externally authoritative execution state.

⸻

4. Definitions

4.1 Intent State

Intent State represents the semantic lifecycle of an Intent.

It answers questions such as:

* Has the Intent been created?
* Is its meaning being resolved?
* Is clarification required?
* Has the Intent been resolved?
* Has the Intent been superseded or withdrawn?

The precise Intent lifecycle is defined by the Intent specifications.

⸻

4.2 Trust State

Trust State represents Noema’s current determination of whether the Intent satisfies the conditions required to proceed toward execution.

Conceptual Trust states include:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

The Trust State Machine is defined separately in:

trust/trust-state-machine.md

⸻

4.3 Execution State

Execution State represents the lifecycle of an attempted Action after an Execution Contract crosses the execution boundary.

Conceptual states include:

NOT_STARTED
ACCEPTED
EXECUTING
COMPLETED
FAILED
PARTIAL
UNKNOWN

The exact execution-state taxonomy remains subject to the execution specifications.

⸻

4.4 Outcome

Outcome represents the observed result of execution and, where applicable, the resulting authoritative business state.

Outcome is distinct from both Intent State and Execution State.

⸻

5. Canonical Separation

Noema should conceptually represent the lifecycles as:

┌──────────────────────┐
│     INTENT STATE     │
├──────────────────────┤
│ CREATED              │
│ RESOLVING            │
│ CLARIFICATION        │
│ RESOLVED             │
│ ...                  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     TRUST STATE      │
├──────────────────────┤
│ UNRESOLVED           │
│ EVALUATING           │
│ WAITING              │
│ BLOCKED              │
│ READY                │
└──────────┬───────────┘
           │
           ▼
     Execution Contract
           │
           ▼
┌──────────────────────┐
│   EXECUTION STATE    │
├──────────────────────┤
│ NOT_STARTED          │
│ ACCEPTED             │
│ EXECUTING            │
│ COMPLETED            │
│ FAILED               │
│ PARTIAL              │
│ UNKNOWN              │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       OUTCOME        │
└──────────────────────┘

These are related lifecycles, not one shared state enum.

⸻

6. Intent State Does Not Equal Execution State

The following states must not be treated as synonyms:

RESOLVED ≠ EXECUTING
RESOLVED ≠ COMPLETED
FAILED ≠ UNRESOLVED
BLOCKED ≠ FAILED
READY ≠ COMPLETED

For example:

Intent State = RESOLVED
Trust State  = READY
Execution    = FAILED

is a valid system condition.

The Intent was understood and trusted, but execution did not successfully complete.

⸻

7. Trust Is Also Separate

Trust must not be collapsed into either Intent State or Execution State.

For example:

Intent State = RESOLVED
Trust State  = WAITING_FOR_APPROVAL
Execution    = NOT_STARTED

The Intent is understood.

It is not yet eligible for execution.

No execution failure has occurred.

Likewise:

Intent State = RESOLVED
Trust State  = READY
Execution    = NOT_STARTED

means execution eligibility has been established, but execution has not yet begun.

⸻

8. Execution Does Not Rewrite Intent Semantics

Execution results must not silently mutate the semantic meaning of the Intent.

For example:

Intent:
Transfer ₦100,000 to Account A

If execution fails because the payment provider is unavailable, the Intent does not become:

Intent:
Unknown

The semantic Intent remains identifiable.

The execution record instead captures:

Execution State:
FAILED
Failure:
PAYMENT_PROVIDER_UNAVAILABLE

The system may then determine whether retry, compensation, clarification, or termination is appropriate.

⸻

9. Execution Failure Does Not Invalidate Trust Retroactively

Suppose:

T1:
Intent resolved
T2:
Validation succeeds
T3:
Trust = READY
T4:
Execution begins
T5:
External system fails

The execution failure does not establish that the Trust decision at T3 was invalid.

Trust answers:

Were the required conditions satisfied when execution eligibility was established?

Execution answers:

What happened when the Action was attempted?

These are different questions.

⸻

10. Successful Execution Does Not Prove Trust Correctness

Similarly:

Trust = READY
Execution = COMPLETED

does not mean that execution success retroactively validates every preceding Trust predicate.

The Trust decision remains grounded in its:

* Intent version
* evidence
* authorization
* policy
* constraints
* capabilities
* context
* evaluation rules
* evaluation timestamp

Execution success is an outcome, not a replacement for Trust provenance.

⸻

11. Temporal Relationship

The lifecycles are related temporally but are not required to have identical transitions.

A conceptual sequence is:

Intent:
CREATED
   ↓
RESOLVING
   ↓
RESOLVED
Trust:
UNRESOLVED
   ↓
EVALUATING
   ↓
READY
Execution:
NOT_STARTED
   ↓
ACCEPTED
   ↓
EXECUTING
   ↓
COMPLETED

However, execution may also result in:

FAILED
PARTIAL
UNKNOWN

without changing the historical Intent State.

⸻

12. State Ownership

Noema should distinguish ownership of state.

Noema owns

Intent State
Trust State
Intent provenance
Trust provenance
Execution Contract generation
Execution coordination state

Execution consumers own or report

Execution State
Execution-specific failures
Execution acknowledgements
Execution receipts

Authoritative enterprise systems own

Business State

For example, a payment system remains authoritative for whether money was actually transferred.

Noema may record the execution result and reference authoritative evidence without becoming the business system of record.

⸻

13. Execution State Is Not Business State

Execution State and Business State must also remain distinct.

For example:

Execution State:
COMPLETED

means the execution consumer reports successful completion.

It does not necessarily mean that every downstream business state has been independently verified.

Where required:

Execution
   ↓
Outcome Verification
   ↓
Authoritative Business State

The enterprise system remains authoritative.

⸻

14. Partial Execution

Partial execution further demonstrates why a unified state is inappropriate.

Consider a composite Intent:

A → transfer payment
B → send notification
C → update CRM

Execution may produce:

A → COMPLETED
B → COMPLETED
C → FAILED

The Intent itself may remain:

RESOLVED

while the execution record captures the component-level outcomes.

Noema must not reinterpret the semantic Intent lifecycle merely because one execution component failed.

⸻

15. Unknown Execution Outcome

An execution consumer may lose connectivity after submitting an Action.

For example:

Execution submitted
       ↓
connection lost
       ↓
result unknown

The appropriate execution state may be:

UNKNOWN

rather than:

FAILED

The Intent State remains separate.

This distinction is essential for avoiding duplicate execution when the external system may already have performed the Action.

⸻

16. Retry Semantics

Retry must operate on Execution State and Action semantics rather than assuming a new Intent.

For example:

Intent State:
RESOLVED
Trust:
READY
Execution:
FAILED

A retry may create a new execution attempt associated with the same Intent version, subject to:

* idempotency
* authorization validity
* Trust validity
* execution-contract rules
* resource state
* policy
* retry constraints

Retry does not automatically mean:

new Intent

⸻

17. Intent Mutation

If the Actor materially changes the Intent, the semantic lifecycle must reflect that change.

For example:

Original Intent:
Transfer ₦100,000
Modified Intent:
Transfer ₦500,000

This is not merely a new execution state.

The modified Intent requires a new or incremented Intent version and may require:

Validation
↓
Trust re-evaluation
↓
new Execution Contract

A previous execution authorization must not automatically be reused for a materially different Intent.

⸻

18. Execution Contract Boundary

The separation becomes especially important at the Execution Contract boundary.

The canonical relationship is:

Intent
   ↓
Validation
   ↓
Trust
   ↓
READY
   ↓
Execution Contract
   ↓
Consumer Acceptance
   ↓
Execution State

Once the Execution Contract crosses the execution boundary, Noema is no longer merely determining whether an Intent is eligible.

An execution consumer is attempting to perform the Action.

⸻

19. State Correlation

Although states are separate, they must remain correlated.

An Execution Record should be traceable to:

Intent ID
Intent Version
Trust Evaluation ID
Execution Contract ID
Execution Attempt ID
Consumer
Timestamp
Outcome

This allows Noema to reconstruct:

What did the Actor intend?
        ↓
Which Intent version was resolved?
        ↓
What Trust decision was made?
        ↓
Which contract was issued?
        ↓
Which consumer executed it?
        ↓
What happened?

⸻

20. Historical Reconstruction

Separating the lifecycles enables accurate historical reconstruction.

Example:

09:00
Intent = RESOLVED
09:01
Trust = WAITING_FOR_APPROVAL
09:05
Approval received
09:05
Trust = READY
09:06
Execution = EXECUTING
09:07
Execution = FAILED
09:08
Intent = RESOLVED

The final Intent State does not erase the execution failure.

Likewise, the execution failure does not erase the fact that the Intent was resolved and Trust was previously READY.

⸻

21. Re-Evaluation After Execution

Execution failure may trigger a new Trust evaluation where relevant.

For example:

Execution = FAILED
        ↓
external state changed
        ↓
Trust re-evaluation

But this must be represented as a new evaluation event.

The system must not silently reinterpret the historical Trust state.

⸻

22. State History Is Append-Oriented

Noema should preserve the history of material state transitions.

Conceptually:

Intent History
I1:
CREATED
RESOLVING
RESOLVED
Trust History
T1:
UNRESOLVED
EVALUATING
WAITING_FOR_APPROVAL
EVALUATING
READY
Execution History
E1:
NOT_STARTED
ACCEPTED
EXECUTING
FAILED

This permits independent auditing of each lifecycle.

⸻

23. Anti-Pattern: Unified Lifecycle Enum

The following model is rejected:

enum State {
    CREATED,
    RESOLVING,
    WAITING,
    READY,
    EXECUTING,
    COMPLETED,
    FAILED
}

A single enum obscures which subsystem owns each state and permits invalid interpretations such as:

FAILED → unresolved
COMPLETED → trusted
READY → executed

Instead, state domains should be explicitly separated.

⸻

24. Recommended Conceptual Model

The canonical conceptual model is:

                 ┌────────────────────┐
                 │       INTENT       │
                 │                    │
                 │   Intent State     │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │       TRUST        │
                 │                    │
                 │    Trust State     │
                 └─────────┬──────────┘
                           │
                      Execution
                      Contract
                           │
                           ▼
                 ┌────────────────────┐
                 │     EXECUTION      │
                 │                    │
                 │  Execution State   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │      OUTCOME       │
                 └────────────────────┘

⸻

25. Consequences

Positive consequences

This decision:

* preserves clear ownership boundaries
* prevents execution outcomes from contaminating Intent semantics
* prevents Trust from being conflated with execution success
* supports retries and multiple execution attempts
* supports partial execution
* supports unknown execution outcomes
* improves auditability
* enables independent state-machine evolution
* preserves authoritative ownership of business state
* makes lifecycle reasoning more precise

Costs

The architecture requires:

* multiple correlated state models
* explicit identifiers and versioning
* additional persistence and event modeling
* more careful transition semantics
* explicit correlation between Intent, Trust, Execution, and Outcome records

This complexity is intentional because the underlying concepts are materially different.

⸻

26. Rejected Alternatives

Alternative A — One unified lifecycle

Rejected because semantic, Trust, and execution states have different meanings and owners.

Alternative B — Treat execution failure as Intent failure

Rejected because an execution failure does not necessarily invalidate the Intent.

Alternative C — Treat successful execution as Trust confirmation

Rejected because execution success is an outcome, not evidence that the Trust evaluation was semantically or procedurally correct.

Alternative D — Treat every retry as a new Intent

Rejected because retrying execution does not necessarily represent a new human objective.

Alternative E — Let execution state determine business truth

Rejected because enterprise systems remain authoritative for their respective domains.

⸻

27. Invariants

Invariant 1

Intent State and Execution State are distinct state domains.

Invariant 2

Trust State is distinct from both Intent State and Execution State.

Invariant 3

Execution failure does not automatically mean the Intent was unresolved or invalid.

Invariant 4

Execution success does not retroactively establish Trust.

Invariant 5

A READY Trust state does not imply execution has begun.

Invariant 6

Execution state does not establish authoritative business state by itself.

Invariant 7

A material Intent change requires revalidation and potentially a new Trust evaluation.

Invariant 8

Execution attempts must remain traceable to the Intent version and Execution Contract from which they originated.

Invariant 9

Unknown execution outcomes must remain distinct from confirmed failure.

Invariant 10

Historical Trust and Intent decisions must not be rewritten based on later execution outcomes.

Invariant 11

Multiple execution attempts may correspond to the same Intent where the semantics and contracts permit retry.

Invariant 12

Partial execution must be representable without corrupting the semantic Intent lifecycle.

⸻

28. Relationship to Other Canonical Decisions

This ADR establishes a direct architectural relationship with:

* ADR-003 — Probabilistic / Deterministic Boundary
    Establishes the boundary between probabilistic model behavior and deterministic system authority.
* ADR-004 — Deterministic Trust Evaluation
    Defines Trust as a deterministic evaluation rather than a model-confidence decision.
* ADR-005 — Explicit Execution Contracts
    Defines the contract through which a trusted Intent crosses into execution.
* ADR-006 — Capability / Permission Separation
    Separates what a system can perform from what an Actor is permitted to cause.
* ADR-007 — Enterprise Systems Remain Authoritative
    Establishes ownership of business state outside Noema.
* ADR-008 — Clarification Over Guessing
    Establishes the requirement to resolve material ambiguity rather than manufacture certainty.
* ADR-010 — Trust State Machine
    Defines the lifecycle of Trust independently from the Intent and execution lifecycles.

⸻

29. Canonical Example

A complete lifecycle may therefore look like:

Actor expresses:
"Transfer ₦100,000 to John's account."
        ↓
Intent State:
RESOLVING
        ↓
Recipient ambiguity detected
        ↓
Intent State:
CLARIFICATION_REQUIRED
        ↓
Actor identifies account
        ↓
Intent State:
RESOLVED
        ↓
Validation
        ↓
Trust State:
EVALUATING
        ↓
Approval required
        ↓
Trust State:
WAITING_FOR_APPROVAL
        ↓
Approval received
        ↓
Trust State:
EVALUATING
        ↓
Trust State:
READY
        ↓
Execution Contract issued
        ↓
Execution State:
ACCEPTED
        ↓
Execution State:
EXECUTING
        ↓
Execution State:
COMPLETED
        ↓
Outcome verification
        ↓
Authoritative business system confirms transfer

At no point is one state substituted for another.

⸻

30. Final Principle

Noema must preserve the distinction:

Intent State
    =
What is the semantic lifecycle of the Intent?
Trust State
    =
Has Noema established eligibility to proceed?
Execution State
    =
What happened when the Action was attempted?
Outcome
    =
What result was observed, including authoritative business state where applicable?

The canonical rule is:

An Intent being understood, trusted, executed, and successfully completed are separate facts. Noema must represent them separately.