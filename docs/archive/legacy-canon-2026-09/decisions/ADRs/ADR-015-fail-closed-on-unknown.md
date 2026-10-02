ADR-015 — Fail Closed on Unknown

Status: Accepted
Version: 0.1
Date: 2026-09-19
Decision Type: Foundational
Domain: Trust / Safety / Execution
Canonical Path: decisions/ADRs/ADR-015-fail-closed-on-unknown.md

⸻

1. Decision

Noema shall fail closed whenever a mandatory condition required for validation, Trust evaluation, authorization, policy compliance, capability eligibility, constraint satisfaction, or execution cannot be established.

Unknown must never be silently converted into valid, authorized, trusted, or executable.

The canonical rule is:

Required condition
      ↓
Cannot be established
      ↓
UNKNOWN
      ↓
No READY
      ↓
WAITING / BLOCKED / RE-EVALUATING

The specific resulting state depends on the semantics of the unknown condition.

⸻

2. Context

Noema operates at the boundary between probabilistic understanding and consequential execution.

At that boundary, the system will sometimes encounter conditions that cannot currently be established.

Examples include:

* authorization service unavailable
* required evidence unavailable
* external system unreachable
* capability status unknown
* resource state unavailable
* policy evaluation unavailable
* identity verification unavailable
* evidence freshness cannot be established
* execution precondition cannot be verified
* external dependency returns an indeterminate result

The absence of information is not equivalent to a positive result.

For example:

Authorization = UNKNOWN

must not become:

Authorization = GRANTED

merely because the authorization service failed to respond.

Likewise:

Recipient existence = UNKNOWN

must not become:

Recipient exists = TRUE

because the recipient appears plausible.

⸻

3. Problem

Without an explicit fail-closed rule, Noema could incorrectly interpret unavailable information as permission to proceed.

This creates an unsafe transition:

UNKNOWN
   ↓
assumed satisfied
   ↓
READY
   ↓
EXECUTION

That violates the separation between evidence and inference, and undermines deterministic Trust.

Noema therefore requires a canonical treatment of uncertainty at the execution boundary.

⸻

4. Principle

The foundational principle is:

Noema must not treat the inability to establish a mandatory condition as evidence that the condition is satisfied.

Formally:

UNKNOWN ≠ TRUE
UNKNOWN ≠ VALID
UNKNOWN ≠ AUTHORIZED
UNKNOWN ≠ TRUSTED
UNKNOWN ≠ READY

Unknown remains unknown until sufficient evidence or a deterministic authoritative result establishes the condition.

⸻

5. Scope

This decision applies to mandatory conditions involved in:

* Intent validation
* Intent applicability
* Authorization
* Policy evaluation
* Risk controls
* Capability availability
* Constraints
* Context
* Evidence
* Evidence freshness
* Resource eligibility
* Execution preconditions
* Human approval
* Confirmation requirements
* Other conditions explicitly designated as mandatory by the applicable contract or policy

It applies both during initial evaluation and during re-evaluation.

⸻

6. Unknown Is a First-Class Result

Noema must preserve the distinction between:

TRUE
FALSE
UNKNOWN

where the underlying evaluation semantics support an indeterminate result.

For example:

Authorization
    ├── GRANTED
    ├── DENIED
    └── UNKNOWN

The same principle may apply to:

Evidence
    ├── SATISFIED
    ├── UNSATISFIED
    └── UNKNOWN

or:

Capability
    ├── AVAILABLE
    ├── UNAVAILABLE
    └── UNKNOWN

The exact enumeration is defined by the relevant canonical specification.

The invariant remains:

UNKNOWN cannot satisfy a mandatory positive predicate.

⸻

7. Relationship to Validation

Validation explicitly defines:

VALID
INVALID
INCOMPLETE
UNKNOWN

as distinct outcomes.

Therefore:

UNKNOWN

must not be transformed into:

VALID

simply because the validator lacks access to the information required to determine validity.

For example:

Recipient lookup
       ↓
External registry unavailable
       ↓
UNKNOWN

The resulting Intent cannot become executable solely on the basis of that uncertainty.

⸻

8. Relationship to Trust

Trust evaluation operates on explicit conditions.

Conceptually:

Intent
+
Evidence
+
Authorization
+
Policy
+
Capability
+
Constraints
+
Context
+
Risk
      ↓
Trust Evaluation

If a mandatory input cannot be established:

Trust = not established

The Trust Engine must not substitute an assumption for the missing condition.

Therefore:

UNKNOWN mandatory condition
        ↓
NOT READY

The appropriate Trust State may then be:

WAITING

or:

BLOCKED

depending on why the condition is unknown and whether recovery is possible.

⸻

9. Relationship to READY

READY represents a positive deterministic conclusion that the mandatory Trust requirements have been satisfied.

Therefore:

UNKNOWN

is incompatible with:

READY

when the unknown condition is mandatory.

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

Every mandatory predicate must be established.

An unknown predicate does not satisfy the conjunction.

⸻

10. Unknown vs Denied

Unknown must also remain distinct from denial.

For example:

Authorization service unavailable

does not establish:

Authorization denied

Therefore the system should not automatically produce:

BLOCKED_BY_AUTHORIZATION

if the only fact is that authorization cannot currently be determined.

The result may instead be:

WAITING_FOR_AUTHORIZATION

or another appropriate non-ready state.

The distinction is:

DENIED
→ a negative authoritative result exists
UNKNOWN
→ no authoritative result has been established

⸻

11. Unknown vs Waiting

Unknown may result in WAITING when the missing information is potentially recoverable.

Example:

Authorization service unavailable
        ↓
Authorization = UNKNOWN
        ↓
WAITING_FOR_AUTHORIZATION

or:

Required evidence unavailable
        ↓
Evidence = UNKNOWN
        ↓
WAITING_FOR_EVIDENCE

Waiting communicates:

The Intent is not currently executable, but the missing condition may become established.

⸻

12. Unknown vs Blocked

Unknown may result in BLOCKED where the applicable policy or execution contract explicitly requires the condition to be established before proceeding and recovery is not currently permitted.

The distinction must be defined by the applicable policy or contract.

Noema must not automatically equate every unknown with permanent rejection.

The foundational rule is instead:

UNKNOWN → NOT READY

The subsequent state is determined by explicit semantics.

⸻

13. Fail-Closed Transition

For consequential Actions, the canonical behavior is:

READY
   ↓
Trust dependency unavailable
   ↓
EVALUATING
   ↓
UNKNOWN mandatory condition
   ↓
WAITING / BLOCKED

Never:

dependency unavailable
        ↓
assume satisfied
        ↓
READY

This rule applies particularly to conditions governing authority and execution eligibility.

⸻

14. External Dependency Failure

External systems may fail independently of Noema.

Examples:

* timeout
* connection failure
* service unavailable
* malformed response
* unavailable authorization provider
* unavailable policy service
* unavailable resource registry

Noema must distinguish:

External system says FALSE

from:

External system failed to provide a result

The first may establish a negative condition.

The second establishes uncertainty.

⸻

15. Example — Authorization

Authoritative denial

Authorization Service
        ↓
DENIED
        ↓
BLOCKED_BY_AUTHORIZATION

Service unavailable

Authorization Service
        ↓
UNAVAILABLE
        ↓
Authorization = UNKNOWN
        ↓
WAITING_FOR_AUTHORIZATION

The two conditions must not be conflated.

⸻

16. Example — Evidence

Suppose an Intent requires current account information.

Account State
     ↓
lookup
     ↓
service unavailable

Noema must not conclude:

account state unchanged

Instead:

account state = UNKNOWN

If the state is mandatory for execution:

Trust ≠ READY

The Intent must wait for authoritative evidence or follow the applicable failure policy.

⸻

17. Example — Capability

Suppose an Action requires a payment capability.

If the capability registry reports:

AVAILABLE

the capability condition may be satisfied.

If it reports:

UNAVAILABLE

the Intent may become:

WAITING_FOR_CAPABILITY

If the registry cannot be reached:

CAPABILITY = UNKNOWN

Noema must not interpret this as:

CAPABILITY = AVAILABLE

⸻

18. Example — Evidence Freshness

Suppose an Action requires current account balance.

Noema has:

balance = ₦100,000
retrieved = 30 minutes ago

If the applicable freshness requirement is five minutes, Noema cannot establish that the evidence remains sufficiently fresh.

The condition becomes:

FRESHNESS = UNKNOWN / UNSATISFIED

and the Intent must not become READY on the basis of stale evidence.

⸻

19. Re-Evaluation

Unknown conditions should be recoverable through deterministic re-evaluation when the underlying dependency becomes available.

Example:

WAITING_FOR_AUTHORIZATION
        ↓
authorization service available
        ↓
EVALUATING
        ↓
authorization = GRANTED
        ↓
all other conditions satisfied
        ↓
READY

The system must re-evaluate all relevant mandatory conditions.

It must not assume that satisfying the previously unknown condition automatically makes the Intent ready.

⸻

20. No Direct UNKNOWN → READY

There should be no transition equivalent to:

UNKNOWN
   ↓
READY

The correct conceptual path is:

UNKNOWN
   ↓
condition established
   ↓
EVALUATING
   ↓
deterministic evaluation
   ↓
READY / WAITING / BLOCKED

This preserves Trust State Machine determinism.

⸻

21. Interaction with the Trust State Machine

The Trust State Machine establishes:

WAITING
BLOCKED
READY

as distinct states.

This ADR reinforces the invariant that unknown mandatory conditions cannot produce READY.

The conceptual flow is:

EVALUATING
     │
     ├── requirement satisfied
     │        ↓
     │      READY
     │
     ├── recoverable requirement unknown
     │        ↓
     │      WAITING
     │
     └── prohibited condition
              ↓
            BLOCKED

Unknown therefore participates in Trust evaluation without becoming an implicit positive result.

⸻

22. Interaction with Clarification

Unknown caused by missing human-provided information may result in clarification.

Example:

Recipient = UNKNOWN

because:

"Send the report to John"

matches multiple recipients.

The correct result is not:

choose probable John

but:

WAITING_FOR_CLARIFICATION

The Actor can then provide the missing information.

⸻

23. Interaction with Model Inference

An LLM may generate a candidate interpretation when authoritative information is unavailable.

That does not automatically resolve the unknown condition.

For example:

Model:
"John probably means John Smith."

does not establish:

recipient = John Smith

unless an explicit deterministic rule or authoritative contextual source establishes that mapping.

Probabilistic inference cannot override a mandatory fail-closed condition.

⸻

24. Interaction with Defaults

Defaults must not be used to convert unknown mandatory conditions into satisfied conditions unless the canonical Intent semantics explicitly define that default as authoritative.

For example:

currency = UNKNOWN

must not become:

currency = NGN

merely because NGN is statistically common.

A deterministic account or system rule may establish a default where the applicable specification explicitly permits it.

⸻

25. Interaction with Execution Contracts

An Execution Contract must not be issued as executable authority when mandatory conditions remain unknown.

Conceptually:

Trust Evaluation
       ↓
mandatory condition UNKNOWN
       ↓
NOT READY
       ↓
No executable contract

A contract may exist as a non-executable proposal or pending artifact where the architecture permits this, but it must not be presented as authorized execution.

⸻

26. Interaction with Execution Consumers

The execution consumer remains responsible for final authoritative checks where required.

Even after Noema establishes:

READY

a consumer may discover a changed business condition.

For example:

T1:
Trust = READY
T2:
Account balance changes
T3:
Consumer validates current balance
T4:
Execution rejected

The consumer’s authoritative rejection does not mean Noema should have treated the earlier state as unknown retrospectively.

It demonstrates why final execution checks may remain necessary.

⸻

27. Fail-Closed Does Not Mean Fail-Silent

Fail-closed behavior must remain observable.

When a mandatory condition is unknown, Noema should record appropriate provenance, such as:

state
reason
condition
dependency
timestamp
evaluation_id
Intent version

Example:

Trust State:
WAITING_FOR_AUTHORIZATION
Reason:
AUTHORIZATION_RESULT_UNAVAILABLE
Dependency:
Authorization Service
Evaluation:
eval_123
Timestamp:
...

The exact schema is defined elsewhere.

⸻

28. Auditability

A fail-closed decision must be reconstructible.

The Trust history should make it possible to determine:

1. what condition was required
2. why it could not be established
3. what dependency was involved
4. what state resulted
5. when re-evaluation occurred
6. what evidence eventually resolved the condition
7. what final Trust state resulted

This supports operational debugging and post-execution audit.

⸻

29. Security Implication

Fail-closed behavior reduces the risk that infrastructure failures become accidental authorization.

Without this invariant:

Security dependency failure
        ↓
Unknown
        ↓
Assumption
        ↓
Execution

could create an unintended authority escalation.

With fail-closed behavior:

Security dependency failure
        ↓
Unknown
        ↓
No READY
        ↓
Wait / Block

the absence of an authoritative result does not create authority.

⸻

30. Availability Trade-Off

Fail-closed behavior can reduce availability.

An Intent may remain waiting even when the requested Action would ultimately have been permitted.

This is an intentional consequence of requiring explicit grounds for consequential execution.

The architecture may define recovery mechanisms such as:

* retry
* dependency restoration
* alternate authoritative source
* human intervention
* re-evaluation

But these mechanisms must not bypass the underlying Trust requirement.

⸻

31. Non-Consequential Actions

Not every operation necessarily requires the same fail-closed boundary.

The applicable policy or Action Contract may define whether an unknown condition is material.

For example, an informational response may tolerate uncertainty differently from:

* financial transfer
* account deletion
* permission modification
* security-sensitive operation
* irreversible business-state mutation

The Action’s risk and contract determine which conditions are mandatory.

Where a condition is designated mandatory for execution, this ADR applies.

⸻

32. Determinism

Given the same:

Intent
Context
Evidence
Policies
Authorization State
Capability State
Constraints
Rule Versions

the treatment of an unknown condition must be deterministic.

For example:

Authorization = UNKNOWN

must not produce:

READY

in one evaluation and:

WAITING

in another solely because an LLM produced different reasoning.

The resulting state is governed by explicit rules.

⸻

33. State Transition Invariants

The following invariants are established:

Invariant 1

Unknown mandatory conditions cannot produce READY.

Invariant 2

Unknown is distinct from denied.

Invariant 3

Unknown is distinct from satisfied.

Invariant 4

External dependency failure must not be interpreted as a positive authorization result.

Invariant 5

Probabilistic model confidence cannot resolve a mandatory unknown condition by itself.

Invariant 6

A recoverable unknown condition may produce WAITING.

Invariant 7

A mandatory unknown condition requires re-evaluation before execution eligibility can be established.

Invariant 8

Unknown conditions must be represented in Trust provenance where material to the decision.

Invariant 9

Fail-closed behavior must not silently mutate Intent semantics.

Invariant 10

A previously unknown condition becoming known triggers deterministic re-evaluation rather than automatic readiness.

⸻

34. Canonical Flow

                    ┌──────────────────┐
                    │  EVALUATING      │
                    └────────┬─────────┘
                             │
                  mandatory condition
                             │
                 ┌───────────┴───────────┐
                 │                       │
              KNOWN                   UNKNOWN
                 │                       │
          ┌──────┴──────┐                ▼
          │             │            NOT READY
       SATISFIED     PROHIBITED          │
          │             │          ┌──────┴──────┐
          ▼             ▼          │             │
        READY        BLOCKED     RECOVERABLE   NON-RECOVERABLE
                                     │             │
                                     ▼             ▼
                                  WAITING        BLOCKED
                                     │
                              condition resolved
                                     │
                                     ▼
                                EVALUATING

⸻

35. Relationship to Other Canonical Decisions

This ADR reinforces several existing Noema principles:

* probabilistic inference must not become deterministic authority
* Trust evaluation is deterministic
* capability and permission are distinct
* execution occurs through explicit contracts
* human intervention is a legitimate system state
* Trust is a lifecycle rather than a one-time boolean
* validation distinguishes UNKNOWN from VALID
* enterprise systems remain authoritative for business state

This ADR specifically establishes the behavior when a required condition cannot currently be established.

⸻

36. Consequences

Positive consequences

* prevents uncertainty from becoming accidental authority
* establishes predictable behavior during dependency failures
* preserves the distinction between unknown and denied
* strengthens deterministic Trust evaluation
* supports auditable state transitions
* reduces unsafe execution under incomplete information
* creates a clear recovery path through re-evaluation

Negative consequences

* some otherwise permissible Actions may be delayed
* external dependency failures can reduce execution availability
* additional state handling is required
* systems must explicitly model unknown conditions
* recovery and retry mechanisms become important operational concerns

These are accepted consequences of bounded and deterministic execution.

⸻

37. Implementation Guidance

Implementations should:

1. represent material unknown conditions explicitly
2. avoid defaulting unknown to positive values
3. preserve authoritative negative results separately from unavailable results
4. prevent READY while mandatory conditions remain unknown
5. record the dependency and reason for material unknown conditions
6. trigger deterministic re-evaluation when relevant conditions become available
7. avoid using model confidence as a substitute for authoritative evidence
8. preserve the distinction between waiting and blocked
9. allow Action Contracts and policies to define which conditions are mandatory
10. perform final authoritative checks at the execution consumer where required

⸻

38. What This ADR Does Not Decide

This ADR does not define:

* the complete Trust State Machine
* the complete Validation schema
* the complete Authorization model
* the complete Policy model
* retry strategies
* timeout values
* dependency health architecture
* circuit-breaker behavior
* fallback-provider selection
* Action-specific risk thresholds
* the complete Execution Contract schema

Those concerns belong to their respective canonical specifications.

This ADR establishes the foundational behavior:

Mandatory unknown ≠ permission to proceed.

⸻

39. Final Decision

Noema shall fail closed on unknown mandatory conditions.

A mandatory condition that cannot be established must remain explicitly unknown and must prevent the Intent from becoming READY until deterministic evidence establishes the required condition.

The canonical rule is:

If Noema cannot establish that a mandatory condition is satisfied,
Noema must not behave as though it is satisfied.

Therefore:

UNKNOWN
   ↓
NOT READY
   ↓
WAITING / BLOCKED
   ↓
RE-EVALUATE
   ↓
READY only when all mandatory conditions are established

This preserves the fundamental Noema boundary:

Probabilistic systems may produce possibilities. Deterministic Trust determines whether those possibilities may cross into execution.