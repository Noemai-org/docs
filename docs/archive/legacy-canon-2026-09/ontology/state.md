> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

# State

**Status:** Foundational Draft  
**Version:** 0.2  
**Domain:** Ontology  
**Canonical Path:** `ontology/state.md`

⸻

1. Definition

A State is a canonical representation of the condition of an Entity, Resource, Process, or other domain object at a defined point or interval in time.

A State answers:

What is true about this thing at this point in time?

Examples:

Account: ACTIVE
Card: BLOCKED
Order: SHIPPED
Payment: COMPLETED
Vehicle: AVAILABLE
Employee: ON_LEAVE
Resource: ALLOCATED

State is not an Action.

ACTIVE

describes a condition.

ActivateAccount

describes an Action intended to change that condition.

State is therefore a representation of domain condition, not an operation.

⸻

2. State in the Noema Model

State connects what is currently true with what an Intent seeks to change.

The canonical relationship is:

Current State
      │
      ▼
    Intent
      │
      ▼
Candidate Action
      │
      ▼
    Trust
      │
      ▼
  Execution
      │
      ▼
   Outcome
      │
      ▼
Resulting State

Example:

Account
Current State:
SUSPENDED
Intent:
Reactivate account
Action:
ReactivateAccount
Outcome:
AccountReactivated
Resulting State:
ACTIVE

This allows Noema to distinguish:

* what is true;
* what is wanted;
* what could change;
* what is permitted to change;
* what actually changed.

⸻

3. State Is Not the Same as Entity

An Entity is the identifiable thing.

A State is a condition of that thing.

Entity:
Account #123
State:
ACTIVE

The Entity may persist while its State changes:

Account #123
    │
    ├── ACTIVE
    ├── SUSPENDED
    ├── ACTIVE
    └── CLOSED

State does not replace the identity of its subject.

⸻

4. State Is Not the Same as Outcome

This distinction is foundational.

State represents what is true.

Outcome represents what resulted from an Action or Execution.

Example:

Action:
SuspendAccount
Outcome:
AccountSuspended
Resulting State:
Account = SUSPENDED

The Outcome establishes what happened.

The State establishes the resulting condition.

An Outcome may therefore support a State transition without being identical to the State itself.

⸻

5. State Is Not the Same as Action

An Action is an operation.

A State is a condition.

Action:
ApproveLoan
State:
APPROVED

The Action may cause the State transition:

PENDING
   │
   │ ApproveLoan
   ▼
APPROVED

⸻

6. State Is Not the Same as Context

Context describes circumstances relevant to interpreting or evaluating an Intent or Action.

State describes the condition of a domain object.

Example:

Context:
User is authenticated.
State:
Account is ACTIVE.

Both may contribute to Trust evaluation, but they remain distinct concepts.

State should not be buried inside an opaque Context representation when it is itself a canonical domain fact.

⸻

7. State Is Not the Same as Constraint

A Constraint limits what may happen.

A State describes what currently is or was true.

Example:

State:
Account balance = $500
Constraint:
Transfer amount <= available balance

The State supplies information against which the Constraint can be evaluated.

⸻

8. State Types

Foundational State categories include:

* Lifecycle State
* Operational State
* Availability State
* Authorization State
* Processing State
* Financial State
* Relationship State
* Health State
* Configuration State

These categories are extensible.

Domain-specific ontologies may define more precise State taxonomies.

Noema should not require every domain to use the same State vocabulary.

⸻

9. Lifecycle State

Lifecycle State describes where an Entity or Resource is within its domain lifecycle.

Example:

Account:
PENDING
ACTIVE
SUSPENDED
CLOSED

Another:

Order:
CREATED
CONFIRMED
FULFILLED
CANCELLED

Lifecycle transitions should be defined by the relevant domain.

⸻

10. Operational State

Operational State describes the current operational condition of a domain object.

Examples:

RUNNING
STOPPED
FAILED
DEGRADED
MAINTENANCE

Example:

Service:
RUNNING

Operational State may affect whether an Action can validly operate on the object.

⸻

11. Availability State

Availability State describes whether a Resource can currently support a particular use.

Examples:

AVAILABLE
UNAVAILABLE
RESERVED
ALLOCATED
OCCUPIED

Availability is often temporal and contextual.

A Resource may be:

AVAILABLE at 10:00

and:

RESERVED at 11:00

Existence therefore does not imply availability.

⸻

12. Authorization State

Authorization State represents the current condition of an authorization-related object or relationship.

Examples:

AUTHORIZED
UNAUTHORIZED
PENDING_APPROVAL
REVOKED
EXPIRED

Authorization State must not replace the canonical Authority model.

Authority establishes the semantic permission relationship.

State describes the current condition of that authority or authorization.

⸻

13. Processing State

Processing State describes the condition of an operation, workflow, or process.

Examples:

PENDING
PROCESSING
COMPLETED
FAILED
CANCELLED

Example:

Payment:
PROCESSING

Processing State is often transient.

⸻

14. Financial State

Financial State represents domain-defined financial conditions.

Examples:

PAID
UNPAID
PARTIALLY_PAID
OVERDUE
REFUNDED

Financial States should be explicitly defined by the relevant domain rather than casually inferred from arbitrary numeric fields.

⸻

15. Configuration State

Configuration State describes whether a configurable object is configured or enabled.

Examples:

ENABLED
DISABLED
CONFIGURED
UNCONFIGURED

Example:

Feature:
ENABLED

⸻

16. State Representation

Conceptually:

State
├── subject
├── type
├── value
├── valid_from
├── valid_until
├── observed_at
├── source
└── provenance

Not every State requires every attribute.

The representation must preserve the distinction between:

* the subject whose condition is represented;
* the semantic State type;
* the State value;
* when the State is valid;
* when it was observed;
* where it came from;
* how it can be traced.

⸻

17. State Subject

Every State must identify what it is the State of.

Example:

Account #123
  └── state: ACTIVE

or:

Vehicle #42
  └── state: AVAILABLE

The subject must be identifiable within the relevant canonical domain.

⸻

18. State Type

A State should have a semantic type.

Examples:

lifecycle
availability
status
balance
capacity
authorization
processing

Noema should avoid treating every arbitrary database field as a canonical State.

A State becomes ontologically meaningful when its semantics are defined.

⸻

19. State Value

A State contains a canonical value appropriate to its State type.

Examples:

ACTIVE
SUSPENDED
AVAILABLE
FAILED
COMPLETED

State values may also be structured.

Example:

State Type:
balance
State Value:
500 USD

The value should preserve the semantics required to evaluate relevant Constraints, Policies, Actions, or Intents.

⸻

20. State Validity

A State may be valid for a defined period.

Example:

State:
AVAILABLE
valid_from:
09:00
valid_until:
12:00

Validity is distinct from observation time.

A State can have been observed at one time while being valid over another defined interval.

This distinction is important for scheduling and Resource availability.

⸻

21. Observed State

A State may represent an observation rather than an authoritative current fact.

Example:

Observed:
Server = HEALTHY

The observation should preserve:

observed_at
source

because the underlying State may have changed after observation.

⸻

22. Current State

Current State is the State Noema resolves as applicable at the relevant evaluation time according to the domain’s authority, validity, provenance, and temporal semantics.

Conceptually:

State History
     │
     ├── 09:00 ACTIVE
     ├── 10:30 SUSPENDED
     ├── 11:00 ACTIVE
     └── 12:00 CLOSED
                     ▲
                     │
              evaluation time

“Current” must therefore be a resolved semantic determination, not merely the most recently retrieved database value.

⸻

23. State History

Where the domain requires temporal auditability, State changes should remain historically reconstructable.

Example:

Account #123
09:00 → ACTIVE
10:15 → SUSPENDED
11:30 → ACTIVE

Historical State is necessary where Trust, audit, reconciliation, or Outcome interpretation depends on what was true at a particular time.

⸻

24. State Transition

A State Transition is a change from one State to another.

State A
   │
   │ Action / Event
   ▼
State B

Example:

SUSPENDED
    │
    │ ReactivateAccount
    ▼
ACTIVE

A State Transition describes the semantic change.

It is not itself the Action that caused the change.

⸻

25. State Transition Is Not an Action

The distinction is:

Action:
ReactivateAccount
Transition:
SUSPENDED → ACTIVE

The Action describes the operation.

The Transition describes the resulting domain change.

⸻

26. State Transition Model

Conceptually:

Transition
├── subject
├── from_state
├── to_state
├── caused_by
├── occurred_at
├── authorized_by
└── supported_by

Example:

Subject:
Account #123
FROM:
SUSPENDED
TO:
ACTIVE
CAUSED BY:
ReactivateAccount
AUTHORIZED BY:
AccountOwnerAuthority

Not every transition requires every attribute, but consequential transitions should preserve sufficient lineage to explain the change.

⸻

27. Valid State Transitions

Not every State should transition to every other State.

Example:

ACTIVE → SUSPENDED
SUSPENDED → ACTIVE
ACTIVE → CLOSED

while:

CLOSED → ACTIVE

may be invalid.

Valid transition semantics are domain-specific and may be constrained by Policy, Constraint, Authority, or current State.

⸻

28. State Machine

A domain may define a finite State machine.

Example:

           ┌──────────┐
           │ PENDING  │
           └────┬─────┘
                │ approve
                ▼
           ┌──────────┐
      ┌────│  ACTIVE  │────┐
      │    └────┬─────┘    │
 suspend│       │ close     │
      ▼         ▼           │
 ┌──────────┐ ┌──────────┐  │
 │SUSPENDED │ │  CLOSED  │◄─┘
 └────┬─────┘ └──────────┘
      │ reactivate
      └────────────► ACTIVE

Where State determines whether an Action is valid, Noema should have access to the relevant transition semantics before the Trust boundary is crossed.

⸻

29. State Preconditions

An Action may require a particular State before execution.

Example:

Action:
ShipOrder
Precondition:
Order = CONFIRMED

If:

Order = CANCELLED

the Action is not valid under that transition model.

State therefore becomes a Trust input.

⸻

30. State Postconditions

An Action may specify an expected resulting State.

Example:

Action:
SuspendAccount
Expected State:
SUSPENDED

This allows Noema to evaluate whether the resulting Outcome established the intended State.

⸻

31. State and Constraint

State frequently provides the values against which Constraints are evaluated.

Example:

State:
Account balance = $500
Constraint:
Transfer amount <= balance
Intent:
Transfer $600

Result:

Constraint:
VIOLATED

The Action should not be treated as permitted merely because a corresponding Capability exists.

⸻

32. State and Policy

Policies may depend on State.

Example:

Policy:
Only active accounts may initiate transfers.
State:
Account = SUSPENDED

The applicable Policy and State together may establish that:

TransferFunds
→ not permitted

The Policy determines the governing rule; State supplies the relevant domain condition.

⸻

33. State and Context

State may contribute to Context used during Intent interpretation and Trust evaluation.

Example:

Context:
Current Account State = SUSPENDED

However, the canonical State should remain independently resolvable rather than existing only as an unstructured Context field.

⸻

34. State and Resource

Resource availability is commonly represented through State.

Example:

Resource:
GPU #4
State:
AVAILABLE

After allocation:

Resource:
GPU #4
State:
ALLOCATED

Resource identity and State remain distinct.

⸻

35. State and Capability

A Capability may exist even when the relevant Resource cannot currently support an Action.

Example:

Capability:
send_payment
Account State:
ACTIVE

versus:

Account State:
CLOSED

The Capability establishes an available ability in the system.

The State determines whether that ability can currently be applied to the particular Resource under consideration.

⸻

36. State and Authority

Authority may itself have State.

Example:

Authority:
RefundApproval
State:
ACTIVE

Later:

State:
REVOKED

The historical Authority relationship remains meaningful, but the current State may prevent it from supporting a consequential Action.

Authority semantics remain defined by the Authority model.

⸻

37. State and Trust

State is a primary deterministic input to Trust.

Conceptually:

Intent
+
Actor
+
Resource
+
Context
+
Policy
+
Constraint
+
Authority
+
Relevant State
+
Evidence
        │
        ▼
      Trust
        │
   ┌────┴────┐
   ▼         ▼
 PERMIT     DENY

The Trust boundary should rely on canonical State resolved from appropriate sources rather than treating model-generated assumptions as established fact.

⸻

38. Unknown State

Noema must distinguish:

KNOWN
UNKNOWN
STALE
CONFLICTING

These states of knowledge are not equivalent to domain State values.

Example:

Account Status:
UNKNOWN

does not mean:

Account Status:
ACTIVE

Unknown State must not silently become a positive State assertion.

⸻

39. Stale State

A previously known State may no longer be sufficiently reliable for the current decision.

Example:

Last known:
Vehicle = AVAILABLE
Observed:
2 hours ago

A booking request may require fresh availability information.

Therefore:

Known ≠ Current

Freshness requirements belong to the relevant evaluation semantics.

⸻

40. Conflicting State

Different sources may report different States.

Example:

Payment Provider:
PAID
Internal Database:
PENDING

Noema should preserve the conflict rather than silently selecting whichever value was retrieved first.

Resolution may depend on:

* source authority;
* temporal validity;
* provenance;
* Policy;
* reconciliation rules;
* evidence.

⸻

41. State Provenance

Consequential State should preserve sufficient provenance.

Example:

Account:
ACTIVE
Source:
Account Service
Observed:
2026-08-23T09:12:00Z

Provenance allows Noema to determine whether the State is sufficiently authoritative for the decision being made.

⸻

42. State Confidence

Some State assertions may be inferred rather than directly established.

Example:

State:
Vehicle = AVAILABLE
Confidence:
0.72

An inferred State should not automatically become authoritative.

Noema should distinguish:

Inferred State

from:

Authoritative State

especially where the State is consequential to execution.

Confidence alone does not establish authority.

⸻

43. Model-Inferred State

The Model may infer a State from natural language.

Example:

User:
"My card was blocked yesterday."

Possible interpretation:

Card State:
BLOCKED

This is a candidate assertion, not automatically an authoritative domain fact.

The canonical flow is:

User Statement
      ↓
Candidate State
      ↓
State Resolution
      ↓
Authoritative / Resolved State

⸻

44. State Resolution

When State matters to execution, Noema should resolve:

1. What is the subject?
2. What State is being asserted?
3. What State type is involved?
4. When was the State true?
5. Who or what observed it?
6. What is the source?
7. Is the source authoritative for this State?
8. Is the State still valid?
9. Are there conflicting assertions?
10. Does the State satisfy the freshness requirements of the decision?

Only after sufficient resolution should the State become a deterministic Trust input.

⸻

45. State Observation vs State Mutation

Noema should distinguish:

State observation

from:

State mutation

An Action may cause a mutation:

Action
  ↓
Execution
  ↓
Outcome
  ↓
State Transition

A read-only observation does not mutate the underlying State.

⸻

46. State Mutation Must Be Explicit

An Action should not implicitly modify arbitrary State.

Example:

UpdateProfile

should have explicit affected domain State rather than silently modifying unrelated domain conditions.

Explicit State effects improve:

* auditability;
* verification;
* replay;
* reconciliation;
* deterministic reasoning.

⸻

47. State and Idempotency

State can help determine whether an intended operation has already been satisfied.

Example:

Intent:
Activate Account
Current State:
ACTIVE

The appropriate semantic interpretation may be:

Desired State already holds.

rather than:

Execute ActivateAccount again.

This helps Noema avoid unnecessary or duplicate execution.

The determination remains subject to the Intent, Policy, and relevant domain semantics.

⸻

48. State and Intent Satisfaction

An Intent may specify or imply a desired State.

Example:

Intent:
"Keep my account active."
Desired State:
Account = ACTIVE

Another:

Intent:
"Cancel my subscription."
Desired State:
Subscription = CANCELLED

Desired State should be represented explicitly where it can be resolved with sufficient semantic confidence.

⸻

49. Desired State vs Current State

These must remain distinct.

Example:

Current State:
SUSPENDED
Desired State:
ACTIVE

The difference creates a State Delta:

Current State
      ↓
State Delta
      ↓
Candidate Action
      ↓
Trust
      ↓
Outcome
      ↓
Desired State

The existence of a State Delta does not by itself establish that an Action is authorized or executable.

⸻

50. State Delta

A State Delta describes an intended or observed change between States.

Example:

Account.status:
SUSPENDED → ACTIVE

or:

Balance:
$500 → $400

State Delta describes change.

It is not itself an Action.

⸻

51. State Delta and Intent

An Intent can often be represented partly through a desired State Delta.

Example:

Intent:
"Move $100 from savings to checking."

Desired changes:

Savings:
$500 → $400
Checking:
$200 → $300

This provides a concrete semantic target against which candidate Actions and Outcomes can be evaluated.

Not every Intent can or should be reduced to a State Delta.

⸻

52. State and Outcome Verification

After execution, Noema should compare expected and observed domain State where applicable.

Example:

Expected:
Account = ACTIVE
Observed:
Account = SUSPENDED

The infrastructure Action may have completed successfully while the intended domain State was not achieved.

Therefore:

Action success
≠
Intent satisfaction

Intent satisfaction requires evaluation of the resulting domain condition and relevant Outcome.

⸻

53. State and Partial Success

An Action may affect multiple States.

Example:

TransferFunds

Expected:

Source balance:
-$100
Destination balance:
+$100

Observed:

Source:
UPDATED
Destination:
UNCHANGED

Noema must be able to represent the resulting partial or inconsistent State changes.

It must not infer complete Intent satisfaction merely because the Action returned successfully.

⸻

54. State Consistency

Where multiple Resources participate in an Action, Noema may need to evaluate whether their resulting States satisfy a domain invariant.

Example:

Transfer:
Source - $100
Destination + $100

Invariant:

Total funds conserved.

If:

Source - $100
Destination + $0

the intended State transition has not been fully satisfied.

State consistency is therefore relevant to Outcome verification and Intent satisfaction.

⸻

55. State and Distributed Systems

In distributed systems, State may be:

* eventually consistent;
* strongly consistent;
* stale;
* replicated;
* cached;
* observed;
* authoritative.

The ontology does not prescribe an underlying consistency model.

However, Trust evaluation must know what State semantics it is relying upon.

⸻

56. State Freshness

Consequential decisions may require State freshness.

Example:

Policy:
Flight availability must be checked within 30 seconds of booking.

Then:

Observed:
Seat available 5 minutes ago

may be insufficient.

Freshness is therefore a property that may participate in Trust evaluation.

⸻

57. State Transition Evidence

A consequential State Transition should be supported by appropriate Evidence where required.

State Transition
      │
      └── supported_by ──► Evidence

Example:

Payment:
PENDING → COMPLETED
Evidence:
Payment Provider Confirmation

Evidence supports the assertion that the transition occurred; it is not itself the State.

⸻

58. State Transition Authority

Consequential State transitions should preserve their Action and Authority lineage where applicable.

State Transition
├── caused_by ──► Action
└── authorized_by ──► Authority

Example:

Account:
ACTIVE → CLOSED
Caused by:
CloseAccount
Authorized by:
AccountOwnerAuthority

⸻

59. State Transition Policy

Policies may constrain which State transitions are permitted.

Example:

Policy:
A closed account cannot be reactivated.

This constrains:

CLOSED
   └── X ──► ACTIVE

Policy therefore contributes to transition validation without replacing the State model itself.

⸻

60. State Transition Graph

A canonical transition can be represented as:

        Current State
              │
              ▼
        Preconditions
              │
              ▼
           Intent
              │
              ▼
        Candidate Action
              │
              ▼
          Trust Gate
              │
              ▼
          Execution
              │
              ▼
           Outcome
              │
              ▼
       State Transition
              │
              ▼
        Resulting State

The resulting State must be established from the Outcome and authoritative observations appropriate to the domain.

⸻

61. State and Noema’s Deterministic Boundary

The Model may infer:

"The user probably wants to reactivate the account."

Noema must resolve the canonical facts needed for execution:

Which account?
Current State?
Desired State?
Allowed transition?
Applicable Policy?
Required Authority?
Available Capability?
Relevant Resource?
Required Evidence?
Expected resulting State?

before execution.

The Model may propose interpretations and candidate Actions.

The canonical State model determines what is established as true for Trust evaluation.

⸻

62. Canonical State Graph

The core relationship model is:

Entity / Resource
       │
       └── has_state ──► State
                              │
                              ├── type
                              ├── value
                              ├── valid_from
                              ├── valid_until
                              ├── observed_at
                              ├── source
                              └── provenance

Transitions:

State A
   │
   │ caused_by
   ▼
Action
   │
   ▼
Outcome
   │
   │ establishes / produces
   ▼
State B

Governance:

Action
   │
   ├── governed_by ──► Policy
   ├── constrained_by ──► Constraint
   └── authorized_by ──► Authority

The exact relationship predicates remain defined by ontology/relationships.md.

⸻

63. Canonical State Invariants

The following are foundational:

1. State describes the condition of a domain object at a defined point or interval in time.
2. State is distinct from Entity.
3. State is distinct from Action.
4. State is distinct from Outcome.
5. State is distinct from Context.
6. State may be current, historical, observed, inferred, stale, or conflicting.
7. Every State must identify its subject.
8. State should have a semantic type and canonical value.
9. Consequential State should have sufficient provenance.
10. State transitions should be explicit where domain correctness depends on them.
11. Actions may cause State transitions; State does not itself constitute an Action.
12. Valid State transitions are domain-specific.
13. Policies and Constraints may restrict valid State transitions.
14. Authority may be required for consequential State transitions.
15. State may serve as a deterministic Trust input.
16. Unknown State must not be treated as a known State.
17. Stale State must not automatically be treated as current State.
18. Conflicting State assertions must not be silently collapsed into one fact.
19. Model-inferred State must not automatically become authoritative State.
20. Expected State and observed/resulting State must remain distinguishable.
21. Successful Action execution does not necessarily imply successful State transition.
22. State observation must remain distinguishable from State mutation.
23. State history should remain reconstructable where required for auditability or Trust.
24. Intent satisfaction should ultimately be evaluated against resulting State and Outcome where applicable.
25. State resolution must account for subject identity, temporal validity, provenance, authority, freshness, and conflicts where consequential.

⸻

64. Canonical Principle

State is Noema’s canonical representation of what is true about a domain object at a defined point or interval in time.

The central distinction is:

Current State
      │
      │ differs from
      ▼
Desired State
      │
      ▼
    Intent
      │
      ▼
Candidate Action
      │
      ▼
     Trust
      │
      ▼
   Execution
      │
      ▼
    Outcome
      │
      ▼
Resulting State

The deeper canonical loop is therefore:

WHAT IS TRUE
      ↓
WHAT IS WANTED
      ↓
WHAT MUST CHANGE
      ↓
WHAT MAY CHANGE
      ↓
WHAT DID CHANGE
      ↓
IS THE DESIRED STATE NOW TRUE?

This gives Noema a canonical representation of change, not merely language interpretation.

The critical architectural boundary remains:

Model proposes
      ↓
Noema resolves
      ↓
Trust evaluates
      ↓
Action executes
      ↓
Outcome is observed
      ↓
State is established
      ↓
Intent satisfaction is evaluated

State therefore provides the canonical truth surface for domain condition against which Noema can distinguish an interpreted request from an authorized operation and, ultimately, an intended change from an actually achieved one.