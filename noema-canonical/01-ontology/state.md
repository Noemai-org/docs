Yes. state.md should define the condition of an Entity or Resource at a particular point in time. It is important for Noema because state is what lets the system distinguish what the user intends from what is currently true, and therefore determine whether an Action is valid and whether an Outcome actually changed anything.

State

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/state.md

⸻

1. Definition

A State is a canonical representation of the condition of an Entity, Resource, Process, or other domain object at a particular point in time.

A State answers:

What is true about this thing now, or at a defined point in time?

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

⸻

2. State in the Noema Model

State connects Intent, Action, and Outcome.

Current State
      │
      ▼
    Intent
      │
      ▼
    Action
      │
      ▼
   Outcome
      │
      ▼
Resulting State

For example:

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

⸻

3. State Is Not the Same as Entity

An Entity is the thing.

State is the condition of the thing.

Entity:
Account #123
State:
ACTIVE

The Entity can persist while its State changes.

Account #123
    │
    ├── ACTIVE
    ├── SUSPENDED
    ├── ACTIVE
    └── CLOSED

⸻

4. State Is Not the Same as Outcome

This distinction is critical.

State

What is true.

Outcome

What happened as the result of an Action or event.

Example:

Action:
SuspendAccount
Outcome:
AccountSuspended
State:
Account = SUSPENDED

The Outcome represents the transition/result.

The State represents the resulting condition.

⸻

5. State Is Not the Same as Action

Action:
ApproveLoan
State:
APPROVED

An Action is an operation.

A State is a condition.

⸻

6. State Is Not the Same as Context

Context describes the circumstances surrounding an Intent or Action.

State describes the condition of a domain object.

Example:

Context:
User is authenticated.
State:
Account is ACTIVE.

Both may affect Trust evaluation, but they represent different concepts.

⸻

7. State Is Not the Same as Constraint

A Constraint restricts what may happen.

A State describes what currently is.

Example:

State:
Account balance = $500
Constraint:
Transfer amount must be <= available balance

The State provides the value against which the Constraint may be evaluated.

⸻

8. State Types

Foundational State categories include:

Lifecycle State
Operational State
Availability State
Authorization State
Processing State
Financial State
Relationship State
Health State
Configuration State

Domains may define more specific State taxonomies.

⸻

9. Lifecycle State

Describes where an Entity or Resource is in its lifecycle.

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

Lifecycle States generally have defined transition rules.

⸻

10. Operational State

Describes whether something is currently functioning or operating.

Examples:

RUNNING
STOPPED
FAILED
DEGRADED
MAINTENANCE

Example:

Service:
RUNNING

⸻

11. Availability State

Describes whether a Resource can currently be used.

Examples:

AVAILABLE
UNAVAILABLE
RESERVED
ALLOCATED
OCCUPIED

Availability is often contextual and temporal.

A Resource may be:

AVAILABLE at 10:00

but:

RESERVED at 11:00

⸻

12. Authorization State

Represents authorization-related conditions.

Examples:

AUTHORIZED
UNAUTHORIZED
PENDING_APPROVAL
REVOKED
EXPIRED

Authorization State should not replace the canonical Authority model.

Authority defines the permission relationship.

State describes its current condition.

⸻

13. Processing State

Used for operations or workflows.

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

Examples:

PAID
UNPAID
PARTIALLY_PAID
OVERDUE
REFUNDED

These states should be domain-defined rather than inferred casually from arbitrary numeric fields.

⸻

15. Configuration State

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

Not every State requires every field.

⸻

17. State Subject

Every State must describe what it is the state of.

Example:

Account #123
  └── state: ACTIVE

or:

Vehicle #42
  └── state: AVAILABLE

The subject must be identifiable.

⸻

18. State Value

The State contains a canonical value.

Examples:

ACTIVE
SUSPENDED
AVAILABLE
FAILED
COMPLETED

Where appropriate, State may contain structured values.

Example:

Account Balance:
500 USD

Here:

State Type:
balance
State Value:
500 USD

⸻

19. State Type

A State should have a semantic type.

Examples:

lifecycle
availability
status
balance
capacity
authorization
processing

Avoid treating every arbitrary field as a canonical State without semantic definition.

⸻

20. State Validity

State may be valid for a defined period.

State:
AVAILABLE
valid_from:
09:00
valid_until:
12:00

This matters for scheduling and Resource availability.

⸻

21. Observed State

A State may be an observation rather than an authoritative fact.

Example:

Observed:
Server = HEALTHY

The observation should preserve:

observed_at
source

because the State may change after observation.

⸻

22. Current State

The current State is the latest authoritative State applicable at the current point in time.

Conceptually:

State History
     │
     ├── 09:00 ACTIVE
     ├── 10:30 SUSPENDED
     ├── 11:00 ACTIVE
     └── 12:00 CLOSED
                     ▲
                     │
                Current State

The system must define how “current” is determined.

⸻

23. State History

State changes should be historically reconstructable where the domain requires it.

Example:

Account #123
09:00 → ACTIVE
10:15 → SUSPENDED
11:30 → ACTIVE

This provides temporal context for Trust and audit decisions.

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

⸻

25. State Transition Is Not an Action

The distinction:

Action:
ReactivateAccount
Transition:
SUSPENDED → ACTIVE

The Action is the operation.

The transition is the resulting state change.

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

Account #123
FROM:
SUSPENDED
TO:
ACTIVE
CAUSED BY:
ReactivateAccount
AUTHORIZED BY:
AccountOwnerAuthority

⸻

27. Valid State Transitions

Not every State should transition to every other State.

Example:

Account:
ACTIVE → SUSPENDED
SUSPENDED → ACTIVE
ACTIVE → CLOSED

But:

CLOSED → ACTIVE

may be invalid.

The valid transition graph is domain-specific.

⸻

28. State Machine

A domain may define a finite state machine.

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

Noema should know the allowed transition semantics where State determines whether an Action is valid.

⸻

29. State Preconditions

An Action may require a particular State before execution.

Action:
ShipOrder
Precondition:
Order = CONFIRMED

If:

Order = CANCELLED

the Action is not valid.

This becomes a Trust input.

⸻

30. State Postconditions

An Action may specify an expected resulting State.

Action:
SuspendAccount
Expected State:
SUSPENDED

This allows Noema to evaluate whether the Outcome produced the intended state.

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

Trust should not permit the Action.

⸻

32. State and Policy

Policies may depend on State.

Example:

Policy:
Only active accounts may initiate transfers.
State:
Account = SUSPENDED

Therefore:

TransferFunds
→ DENIED

⸻

33. State and Context

State can be part of the Context used to interpret an Intent.

Example:

Context:
Current Account State = SUSPENDED

However, State should remain independently addressable as a canonical fact rather than being buried inside an opaque Context object.

⸻

34. State and Resource

Resource availability is a State.

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

⸻

35. State and Capability

A Capability may be available only when the relevant Resource or Actor is in an appropriate State.

Example:

Capability:
send_payment
Account State:
ACTIVE

versus:

Account State:
CLOSED

The Capability may still exist, but the Action cannot necessarily be performed against that Resource.

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

The historical Authority relationship remains meaningful, but current execution should treat it as unavailable.

⸻

37. State and Trust

State is one of the primary deterministic inputs into Trust.

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
Current State
+
Evidence
        │
        ▼
      Trust
        │
   ┌────┴────┐
   ▼         ▼
 PERMIT     DENY

The Trust Engine should evaluate canonical State rather than relying solely on model-generated assumptions.

⸻

38. Unknown State

Noema must distinguish:

KNOWN STATE
UNKNOWN STATE
STALE STATE
CONFLICTING STATE

These are not equivalent.

Example:

Account Status:
UNKNOWN

does not mean:

Account Status:
ACTIVE

Noema must not infer the latter without sufficient evidence.

⸻

39. Stale State

A previously known State may no longer be reliable.

Example:

Last known:
Vehicle = AVAILABLE
Observed:
2 hours ago

A booking request now may require fresh availability information.

Therefore:

Known ≠ Current

⸻

40. Conflicting State

Different authoritative or semi-authoritative sources may disagree.

Example:

Payment Provider:
PAID
Internal Database:
PENDING

Noema should preserve the conflict.

It should not silently choose a value merely because one source was retrieved first.

⸻

41. State Provenance

Every consequential State should have provenance.

Example:

Account:
ACTIVE
Source:
Account Service
Observed:
2026-08-23T09:12:00Z

This allows Trust to determine whether the State is sufficiently authoritative.

⸻

42. State Confidence

Where State is inferred rather than directly observed:

State:
Vehicle = AVAILABLE
Confidence:
0.72

This should not automatically be treated as authoritative.

Noema should distinguish:

Inferred State

from:

Authoritative State

particularly for consequential Actions.

⸻

43. Model-Inferred State

The Model may infer State from natural language.

Example:

“My card was blocked yesterday.”

Possible interpretation:

Card State:
BLOCKED

But Noema should treat this as a claim requiring resolution against authoritative state where execution depends on it.

User Statement
      ↓
Candidate State
      ↓
State Resolution
      ↓
Authoritative State

⸻

44. State Resolution

When State matters to execution, Noema should resolve:

What is the subject?
What State is being asserted?
When was it true?
Who/what observed it?
Is the source authoritative?
Is it still valid?

Only then should the State become a deterministic Trust input.

⸻

45. State Mutation

Noema should distinguish between:

State observation

and:

State mutation

An Action may cause a mutation:

Action
  ↓
Execution
  ↓
Outcome
  ↓
State Transition

A read-only observation does not mutate State.

⸻

46. State Mutation Must Be Explicit

An Action should not implicitly modify arbitrary State.

Example:

UpdateProfile

should have explicit affected State:

CustomerProfile

rather than silently changing unrelated domain state.

This supports auditability and deterministic reasoning.

⸻

47. State and Idempotency

State is important for determining whether an Action has already been applied.

Example:

Intent:
Activate Account
Current State:
ACTIVE

Possible interpretations include:

Already satisfied

rather than:

Execute ActivateAccount again

This is a key mechanism for avoiding unnecessary or duplicate execution.

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

The desired State should be derived explicitly where possible.

⸻

49. Desired State vs Current State

These must remain distinct.

Current State:
SUSPENDED
Desired State:
ACTIVE

The gap between them creates the need for Action.

Current State
      ↓
State Delta
      ↓
Candidate Action
      ↓
Outcome
      ↓
Desired State

This is a powerful representation for Noema’s intent model.

⸻

50. State Delta

A State Delta describes the intended or observed change between States.

Example:

Account.status:
SUSPENDED → ACTIVE

or:

Balance:
$500 → $400

State Delta is not itself an Action.

It describes change.

⸻

51. State Delta and Intent

An Intent can often be represented as a desired State Delta.

Example:

“Move $100 from savings to checking.”

Desired changes:

Savings:
$500 → $400
Checking:
$200 → $300

This gives Noema a precise semantic target against which candidate Actions can be evaluated.

⸻

52. State and Outcome Verification

After execution:

Expected:
Account = ACTIVE
Observed:
Account = SUSPENDED

Then:

Intent:
NOT SATISFIED

The Action may have executed successfully from an infrastructure perspective while failing to achieve the intended domain Outcome.

This distinction is fundamental.

⸻

53. State and Partial Success

Some Actions modify multiple States.

Example:

TransferFunds

Expected:

Source balance: -$100
Destination balance: +$100

If only the source changes:

Source:
UPDATED
Destination:
UNCHANGED

Noema must be able to represent partial or inconsistent Outcomes.

It must not infer complete Intent satisfaction merely because the Action returned successfully.

⸻

54. State Consistency

Where multiple Resources participate in an Action, Noema should be able to determine whether their resulting States satisfy the intended invariant.

Example:

Transfer:
Source - $100
Destination + $100

Invariant:

Total funds conserved.

If:

Source - $100
Destination + $0

the intended State transition has not been satisfied.

⸻

55. State and Distributed Systems

In distributed systems, State may be:

eventually consistent
strongly consistent
stale
replicated
cached
observed
authoritative

Noema’s ontology does not dictate the underlying consistency model.

However, Trust decisions must know what State semantics they are relying on.

⸻

56. State Freshness

For consequential operations, State may require a freshness requirement.

Example:

Policy:
Flight availability must be checked within 30 seconds of booking.

Then:

Observed:
Seat available 5 minutes ago

is insufficient.

Freshness becomes part of the Trust evaluation.

⸻

57. State Transitions and Evidence

A State Transition should be supported by Evidence where required.

State Transition
      │
      └── supported_by ──► Evidence

Example:

Payment:
PENDING → COMPLETED
Evidence:
Payment Provider Confirmation

⸻

58. State Transition Authority

Consequential State transitions should identify the Action and Authority responsible.

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

Policies may define allowed transitions.

Example:

Policy:
A closed account cannot be reactivated.

This establishes:

CLOSED
   └──X──► ACTIVE

The Policy therefore becomes part of the transition validation.

⸻

60. State Transition Graph

A canonical transition can be modeled as:

        Current State
              │
              ▼
        Preconditions
              │
              ▼
           Intent
              │
              ▼
            Action
              │
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

⸻

61. State and Noema’s Deterministic Boundary

This is one of the most important principles for the architecture.

The Model may infer:

"The user probably wants to reactivate the account."

But Noema must resolve:

Which account?
Current State?
Allowed transition?
Applicable Policy?
Required Authority?
Available Capability?
Expected resulting State?

before execution.

The Model can propose.

The canonical State model determines what is actually true.

⸻

62. Canonical State Graph

The core relationship model is:

Entity / Resource
       │
       └── has_state ──► State
                              │
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
   │ produces
   ▼
State B

Governance:

Action
   │
   ├── governed_by ──► Policy
   ├── constrained_by ─► Constraint
   └── authorized_by ──► Authority

⸻

63. Canonical State Invariants

The following are foundational:

1. State describes the condition of a domain object at a point in time.
2. State is distinct from Entity.
3. State is distinct from Action.
4. State is distinct from Outcome.
5. State is distinct from Context.
6. State may be current, historical, observed, inferred, stale, or conflicting.
7. State must identify its subject.
8. Consequential State should have sufficient provenance.
9. State transitions should be explicit where domain correctness depends on them.
10. Actions cause State changes; States do not cause Actions by themselves.
11. Valid State transitions are domain-specific.
12. Policies and Constraints may restrict valid transitions.
13. Authority may be required for State transitions.
14. State may serve as a deterministic Trust input.
15. Unknown State must not be treated as a known State.
16. Stale State must not automatically be treated as current State.
17. Model-inferred State must not automatically become authoritative State.
18. Expected State and Observed State must remain distinguishable.
19. Successful Action execution does not necessarily imply successful State transition.
20. Intent satisfaction should ultimately be evaluated against resulting State and Outcome where applicable.

⸻

64. Canonical Principle

State is Noema’s representation of what is true about the domain at a particular point in time.

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

This gives Noema a concrete way to reason about change rather than merely interpreting language.

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

That loop is one of the strongest foundations for the Noema Intent OS.