> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-017 — Outcome Separate from Trust

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Trust / Execution
Canonical Path: decisions/ADR/ADR-017-outcome-separate-from-trust.md

⸻

1. Decision

Noema SHALL treat Trust and Execution Outcome as separate architectural concepts and separate lifecycle concerns.

A Trust decision establishes whether an Intent is eligible to cross the execution boundary.

An Execution Outcome establishes what actually happened after execution was attempted.

Therefore:

Trust does not determine Outcome, and Outcome does not retroactively determine whether Trust was valid.

The canonical relationship is:

Intent
   ↓
Validation
   ↓
Trust Evaluation
   ↓
Execution Eligibility
   ↓
Execution
   ↓
Outcome

⸻

2. Context

Noema operates at the boundary between probabilistically understood human intent and deterministic execution through existing software systems.

A Trust Engine may establish that an Intent satisfies the conditions required for execution:

Intent
  +
Validation
  +
Authorization
  +
Policy
  +
Evidence
  +
Capability
  +
Constraints
  +
Context
  ↓
READY

However, establishing execution eligibility does not establish that an external system will successfully perform the requested Action.

Execution may fail because of:

* external dependency failure
* timeout
* resource state changes
* consumer-side validation
* concurrency
* network failure
* unavailable service
* business-state changes
* partial execution
* unknown execution result

Therefore, combining Trust and Outcome into a single state would conflate two different questions:

Was the Action permitted to execute?

and:

What happened when execution was attempted?

These questions must remain independent.

⸻

3. Problem

A single lifecycle state such as:

TRUSTED

or:

SUCCESS

cannot adequately represent both execution eligibility and execution result.

For example:

Trust = READY
Execution = FAILED

is entirely valid.

Likewise:

Trust = READY
Execution = COMPLETED

is valid.

The following implication is therefore invalid:

READY → COMPLETED

Similarly:

COMPLETED → Trust was correct

cannot be used as the definition of Trust correctness.

⸻

4. Decision Rationale

Noema separates the two lifecycles.

Trust lifecycle

UNRESOLVED
     ↓
EVALUATING
     ↓
WAITING
     ↓
BLOCKED
     ↓
READY

Execution lifecycle

NOT_STARTED
     ↓
ACCEPTED
     ↓
EXECUTING
     ↓
COMPLETED
       or
FAILED
       or
PARTIAL
       or
UNKNOWN

The exact execution-state taxonomy may evolve, but the architectural separation is normative.

⸻

5. Trust Answers a Different Question

Trust answers:

May this Intent cross the execution boundary under the current established conditions?

Examples of Trust states include:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

A READY Trust state means that Noema has established the required execution eligibility.

It does not mean:

* execution has started
* execution succeeded
* the external system accepted the request
* the requested business state was achieved
* the expected postcondition exists

Therefore:

READY ≠ SUCCESS

⸻

6. Outcome Answers a Different Question

Outcome answers:

What happened after execution was attempted?

Examples include:

COMPLETED
FAILED
PARTIALLY_COMPLETED
UNKNOWN

The Outcome is established through execution evidence and, where applicable, authoritative postcondition verification.

Outcome therefore belongs to the execution side of the architecture.

⸻

7. Canonical Architecture

The recommended conceptual architecture is:

                         Intent
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        Trust Lifecycle          Intent Lifecycle
              │
              ▼
        Execution Eligibility
              │
              ▼
       Execution Contract
              │
              ▼
       Execution Consumer
              │
              ▼
       Execution / Mutation
              │
              ▼
           Outcome

Trust controls the boundary.

Execution produces the outcome.

⸻

8. Trust Does Not Guarantee Success

Consider:

Intent:
Transfer ₦100,000 to Account B

Noema establishes:

Validation = VALID
Authorization = SATISFIED
Policy = SATISFIED
Capability = AVAILABLE
Constraints = SATISFIED
Risk = WITHIN_BOUNDARY
Trust = READY

The execution contract is accepted.

The payment provider subsequently becomes unavailable.

Result:

Trust = READY
Execution = FAILED

This does not imply that the Trust Engine incorrectly established execution eligibility.

It demonstrates that execution occurs in an external and potentially changing environment.

⸻

9. Outcome Does Not Retroactively Define Trust

An execution may succeed even though the architecture must not use success as evidence that the Trust decision was correct.

For example, an implementation could accidentally permit an Action outside the intended authorization boundary and the external system might still execute it.

Therefore:

Execution succeeded

does not establish:

Trust decision was valid

Trust validity must be evaluated according to the Trust rules and evidence that existed at the time of the decision.

⸻

10. Temporal Separation

Trust and execution occur at different points in time.

Conceptually:

T1
Intent resolved
T2
Validation
T3
Trust evaluation
T4
READY
T5
Execution Contract accepted
T6
Execution begins
T7
External system changes
T8
Execution fails

The state at T8 cannot be used to redefine the conditions that existed at T3.

Therefore Noema must preserve the relevant Trust evaluation provenance independently from the eventual Outcome.

⸻

11. TOCTOU Conditions

Noema must account for time-of-check-to-time-of-use conditions.

For example:

T1:
Account balance = ₦1,000,000
T2:
Trust evaluation = READY
T3:
Another transaction reduces balance
T4:
Execution begins
T5:
Consumer rejects transaction

The Trust evaluation and execution outcome describe different points in the system’s temporal state.

Noema must not collapse them into one state.

⸻

12. Consumer Authority

Execution consumers may perform final authoritative checks.

For example:

Noema
  ↓
VALID + TRUSTED
  ↓
Execution Contract
  ↓
Payment Service
  ↓
Final business-state validation

The consumer may reject execution because its authoritative state has changed.

That rejection becomes part of the Execution Outcome.

It does not automatically invalidate the historical Trust decision.

⸻

13. Outcome Verification

Where an Action has an expected postcondition, Noema should distinguish:

Execution requested

from:

Execution completed

and from:

Expected business outcome verified

For example:

Action:
Renew card
Execution:
accepted
Execution:
completed
Postcondition:
new card status = ACTIVE
Outcome:
verified

The precise postcondition-verification model may be defined by the relevant execution and outcome specifications.

⸻

14. Unknown Outcome

Noema must explicitly support situations where execution occurred but the final outcome cannot be established.

Example:

Execution request submitted
        ↓
Network connection lost
        ↓
Consumer result unknown

Noema must not infer:

FAILED

merely because confirmation was unavailable.

Nor may it infer:

COMPLETED

without sufficient evidence.

The result may therefore be:

OUTCOME = UNKNOWN

until authoritative evidence establishes the result.

⸻

15. Partial Execution

Composite or multi-step Actions may produce partial outcomes.

Example:

A → COMPLETED
B → FAILED
C → NOT_EXECUTED

The overall execution outcome may therefore require a representation such as:

PARTIALLY_COMPLETED

The existence of partial execution must not be interpreted as a Trust state.

Trust determined execution eligibility; execution determined what actually occurred.

⸻

16. Historical Trust Preservation

Noema should preserve the Trust decision associated with an execution attempt.

Conceptually:

Trust Evaluation
├── evaluation_id
├── intent_version
├── policy_version
├── evidence
├── authorization
├── capability
├── constraints
├── decision
└── timestamp

Separately:

Execution Record
├── execution_id
├── contract
├── consumer
├── start_time
├── completion_time
├── execution_state
├── outcome
└── outcome_evidence

This permits reconstruction of:

Why was execution permitted?

and:

What happened when execution occurred?

as separate questions.

⸻

17. State Model

The preferred conceptual model is:

Intent
 │
 ├───────────────┐
 │               │
 ▼               ▼
Trust State   Execution State
 │               │
 │               ├── NOT_STARTED
 ├── UNRESOLVED  ├── ACCEPTED
 ├── EVALUATING  ├── EXECUTING
 ├── WAITING     ├── COMPLETED
 ├── BLOCKED     ├── FAILED
 └── READY       ├── PARTIAL
                 └── UNKNOWN

Implementations may use separate state machines or separate state dimensions.

The conceptual separation is canonical.

⸻

18. Execution Boundary

The architectural boundary is:

                 TRUST
                   │
                   │
              READY│
                   ▼
          Execution Contract
                   │
             acceptance
                   │
                   ▼
               EXECUTION
                   │
                   ▼
                OUTCOME

Trust governs entry into execution.

Outcome describes what follows.

⸻

19. Relationship to the Trust State Machine

The Trust State Machine defines transitions such as:

EVALUATING
    ↓
READY

and:

READY
    ↓
material condition changes
    ↓
EVALUATING

Execution begins only after the execution boundary is crossed.

Once execution has begun, the resulting state should not be represented as a Trust judgment merely because it describes the result of execution.

This preserves the distinction between:

execution eligibility

and:

execution outcome

⸻

20. Relationship to Execution Records

An Execution Record should reference the Trust decision that authorized the execution attempt.

Conceptually:

ExecutionRecord {
    execution_id
    intent_id
    intent_version
    trust_evaluation_id
    execution_contract_id
    consumer
    execution_state
    outcome
    outcome_evidence
    timestamps
}

This establishes traceability without merging Trust and Outcome into one abstraction.

⸻

21. Relationship to Business Truth

The final business outcome remains authoritative in the relevant enterprise system.

Noema may record:

Outcome:
COMPLETED

but this does not automatically make Noema the authoritative source for the underlying business state.

Where appropriate, Noema should verify the outcome against the authoritative system.

Therefore:

Noema Outcome Record
        ≠
Enterprise Business State

The outcome is Noema’s record of what it established about execution.

⸻

22. Failure Semantics

The architecture must distinguish at least:

Trust blocked

from:

Execution failed

These are materially different.

Trust failure

Intent
  ↓
Trust
  ↓
BLOCKED
  ↓
No execution

Execution failure

Intent
  ↓
Trust
  ↓
READY
  ↓
Execution
  ↓
FAILED

The first means execution was not permitted.

The second means execution was permitted and attempted but did not successfully complete.

⸻

23. No Retroactive Trust Mutation

An execution outcome must not automatically rewrite the historical Trust decision.

For example:

T1:
Trust = READY
T2:
Execution = FAILED

The system must not rewrite the historical record as:

Trust = BLOCKED

simply because execution failed.

If new evidence demonstrates that the original Trust evaluation was incorrect, Noema may record a separate correction, invalidation, or audit finding according to the relevant governance model.

The original decision must remain reconstructible.

⸻

24. Re-Evaluation After Failure

Execution failure may trigger a new Trust evaluation for a subsequent attempt.

For example:

READY
  ↓
EXECUTING
  ↓
FAILED
  ↓
new conditions
  ↓
EVALUATING

The retry must not automatically inherit the previous Trust decision if material conditions may have changed.

A new execution attempt may require:

* new validation
* refreshed evidence
* renewed authorization
* new policy evaluation
* capability re-evaluation
* new execution contract

⸻

25. Invariants

Invariant 1

Trust determines execution eligibility, not execution success.

Invariant 2

Execution Outcome is separate from Trust State.

Invariant 3

READY does not imply COMPLETED.

Invariant 4

FAILED does not imply the preceding Trust decision was invalid.

Invariant 5

Execution success does not prove that a Trust decision was correct.

Invariant 6

Unknown execution results must not be converted into success or failure without sufficient evidence.

Invariant 7

Execution consumers may perform additional authoritative validation.

Invariant 8

Business systems remain authoritative for their domain state.

Invariant 9

Historical Trust decisions must remain reconstructible.

Invariant 10

A new execution attempt may require a new Trust evaluation when material conditions have changed.

Invariant 11

Trust and Outcome must remain distinguishable in provenance and audit records.

Invariant 12

Partial execution must not be represented as a Trust state.

⸻

26. Canonical Example

User Intent
    │
    ▼
"Renew my card."
    │
    ▼
Resolved Intent
    │
    ▼
Validation
    │
    ▼
Trust Evaluation
    │
    ├── Authorization ✓
    ├── Policy ✓
    ├── Evidence ✓
    ├── Capability ✓
    └── Constraints ✓
    │
    ▼
READY
    │
    ▼
Execution Contract
    │
    ▼
Card Service
    │
    ├── accepted
    │
    ▼
EXECUTING
    │
    ▼
Outcome
    │
    └── COMPLETED

Failure variant:

READY
  ↓
Execution Contract
  ↓
EXECUTING
  ↓
Payment Service Timeout
  ↓
FAILED

The Trust decision remains:

READY

for that historical evaluation.

⸻

27. Architectural Consequence

Noema implementations SHOULD represent Trust and Execution Outcome as separate dimensions of system state.

They MAY be implemented as:

* separate state machines
* separate enums
* separate records
* related lifecycle projections

provided that the semantic distinction remains explicit.

A single combined state enum SHOULD NOT be used if it obscures whether a state describes:

1. execution eligibility, or
2. execution outcome.

⸻

28. Relationship to Other Canonical Concepts

This decision reinforces:

* Trust State Machine — defines execution eligibility lifecycle.
* Validation — establishes whether an Intent is structurally and semantically valid.
* Execution Contract — establishes the explicit boundary through which execution occurs.
* Execution Record — records execution activity and outcome.
* Outcome Engine — establishes and represents execution outcomes.
* Provenance and Auditability — preserves the evidence and history necessary to reconstruct decisions.
* Enterprise Authority — preserves the external system as authoritative for business state.

These concepts should remain complementary rather than collapsed into a single lifecycle abstraction.

⸻

29. Rejected Alternatives

Alternative A — Trust state includes execution outcome

Rejected because it conflates eligibility with result.

Alternative B — Successful execution proves Trust

Rejected because execution success is not the definition of authorization or Trust validity.

Alternative C — Failed execution means Trust was incorrect

Rejected because external execution can fail after a valid Trust decision.

Alternative D — Noema treats unknown execution results as failure

Rejected because absence of confirmation does not establish failure.

Alternative E — Noema treats unknown execution results as success

Rejected because absence of evidence does not establish completion.

⸻

30. Final Decision

Noema SHALL maintain a strict architectural distinction between:

Trust

and:

Execution Outcome

The canonical lifecycle is:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Execution Eligibility
   ↓
Execution
   ↓
Outcome

The fundamental invariant is:

Trust establishes whether Noema may permit execution; Outcome establishes what happened after execution was attempted. Neither concept substitutes for the other.