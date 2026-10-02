Context API

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/context-api.md

⸻

1. Definition

The Context API is the interface through which Noema receives, resolves, exposes, and manages contextual information required to interpret, trust, and execute Intent and Actions.

Context provides the information surrounding an Intent or Action that determines how that request should be understood and whether it may safely execute.

Conceptually:

Intent
  +
Context
  ↓
Meaning
  ↓
Trust
  ↓
Execution

Context is therefore not merely metadata.

It is part of the conditions under which an Intent becomes executable.

⸻

2. Purpose

The Context API provides a structured boundary for supplying and retrieving context such as:

actor
tenant
session
conversation
channel
environment
time
location
resource state
previous actions
organizational context
authorization context
execution context

The API allows this information to participate in Noema’s decision process without requiring consumers to embed all contextual information directly into an Intent.

⸻

3. Core Principle

Context must influence interpretation and execution only according to explicit semantics; Noema must never treat arbitrary contextual data as authoritative merely because it was supplied by a caller.

For example:

channel = mobile

may be useful context.

But:

user_is_admin = true

should not become an authorization fact merely because a client supplied it.

⸻

4. Context Is Not Intent

Intent answers:

What does the Actor want to accomplish?

Context answers:

Under what circumstances should that Intent be interpreted and executed?

Example:

Intent:
"Renew my card."
Context:
Actor = Tunde
Channel = mobile
Card = card_123
Tenant = bank_001
Session = session_456

The context helps Noema resolve the Intent against the correct entities and policies.

⸻

5. Context Is Not Business State

Noema may consume business state as context.

It should not therefore become the authoritative owner of that state.

For example:

Enterprise System
    ↓
account.balance = ₦500,000
    ↓
Noema Context

Noema may use the balance to evaluate an Action.

The enterprise system remains authoritative for the balance.

⸻

6. Context Sources

Context may originate from multiple sources:

user
application
enterprise API
authentication system
authorization system
conversation
session
event stream
Action execution
external provider
Noema's historical execution record

The Context API should preserve source provenance where the distinction matters.

⸻

7. Context Provenance

Context should be attributable to a source.

Conceptually:

{
  "key": "account_status",
  "value": "active",
  "source": {
    "type": "enterprise_api",
    "reference": "account-service"
  }
}

This allows Noema to reason about:

where did this fact come from?
when was it observed?
can it be trusted?

⸻

8. Context Trust

Not all context has equal trust.

Conceptually:

User supplied
      ↓
Application supplied
      ↓
Authenticated system
      ↓
Authoritative enterprise source

The actual trust hierarchy is policy-defined.

The important principle is:

Context provenance and trustworthiness must be explicit.

⸻

9. Context Categories

A useful canonical classification is:

Identity Context
Temporal Context
Spatial Context
Session Context
Conversation Context
Resource Context
Organizational Context
Authorization Context
Execution Context
Historical Context
Environmental Context

These categories are semantic rather than implementation-specific.

⸻

10. Identity Context

Identity context establishes who is involved.

Example:

Actor:
customer_123
Caller:
application_456
Tenant:
enterprise_789

Identity context must distinguish:

who is calling

from:

who the Action is for

and:

who owns the affected Resource

⸻

11. Temporal Context

Temporal context describes time relevant to interpretation or execution.

Examples:

current time
business hours
deadline
expiration
effective date
previous event timestamp
authorization expiry

Example:

"Cancel the transfer before 5 PM."

requires temporal context.

⸻

12. Spatial Context

Some Actions depend on location.

Examples:

country
region
branch
service area
device location
jurisdiction

Location should only be treated as authoritative when obtained through an appropriate trusted source.

⸻

13. Session Context

A session may establish continuity across interactions.

Example:

session_id = sess_123

It can connect:

conversation
Intent
clarification
confirmation
Action

However, session continuity must not automatically imply authorization continuity.

⸻

14. Conversation Context

Conversation context provides information from previous turns that may affect Intent resolution.

Example:

User:
"Transfer ₦50,000 to John."
Assistant:
"Which John?"
User:
"The one I sent money to yesterday."

The second statement cannot be interpreted correctly without conversational context.

⸻

15. Conversation Context Is Not Permanent Truth

Previous conversational statements should not automatically become permanent facts.

For example:

User:
"My account number is 123."

does not necessarily establish that:

account_number = 123

is authoritative forever.

Context should have:

scope
source
timestamp
validity
trust

where appropriate.

⸻

16. Resource Context

Resource context describes the state of resources relevant to an Intent or Action.

Example:

card.status = LOST

This may determine whether:

issue_replacement_card

is valid.

Resource context should generally reference the authoritative resource rather than duplicate its entire state into Noema.

⸻

17. Organizational Context

Enterprise workflows often depend on organizational structure.

Examples:

department
team
branch
role
manager
cost center
business unit

This may influence:

policy
authorization
routing
approval requirements
risk

⸻

18. Authorization Context

Authorization context describes facts relevant to access decisions.

Examples:

authenticated principal
roles
permissions
scopes
delegation
approval state
policy version

Authorization context should come from trusted authorization mechanisms.

⸻

19. Execution Context

Execution context describes conditions surrounding an Action attempt.

Examples:

execution_id
attempt_id
consumer
provider
environment
deadline
retry_count
correlation_id

This allows the executor and Trust Engine to reason about the current execution attempt.

⸻

20. Historical Context

Historical context describes relevant prior events.

Example:

customer requested replacement card yesterday

or:

previous transfer attempt failed

Historical context can influence interpretation and execution.

But historical occurrence does not necessarily mean current validity.

⸻

21. Environmental Context

Environmental context describes the current execution environment.

Examples:

production
staging
provider availability
system health
maintenance window
network conditions

Environmental context may affect execution eligibility.

⸻

22. Context Scope

Context must have a defined scope.

Possible scopes include:

request
session
conversation
Intent
Action
execution
attempt
tenant
system

A context value must not automatically leak from one scope into another.

⸻

23. Context Lifetime

Context may be:

ephemeral
session-bound
Intent-bound
Action-bound
execution-bound
persistent

For example:

device_network = wifi

may be ephemeral.

Whereas:

tenant_id = enterprise_123

may persist across many Actions.

⸻

24. Context Freshness

Context may become stale.

Example:

balance = ₦100,000
observed_at = 10:00

At:

10:30

that information may no longer be sufficient for a consequential transaction.

Context should therefore support freshness semantics where required.

⸻

25. Context Version

Where context changes over time, Noema should be able to identify the version or observation from which a decision was made.

Conceptually:

resource_version = 42

This is particularly useful for:

optimistic concurrency
race detection
reconciliation
auditability

⸻

26. Context Snapshot

Before consequential execution, Noema may establish a context snapshot.

Conceptually:

Context Snapshot
----------------
Actor
Tenant
Resource state
Authorization
Policy
Time
Environment
Relevant history

The snapshot records the contextual basis for a decision.

⸻

27. Context Snapshot Is Not Frozen Reality

A snapshot means:

what Noema knew at decision time

It does not mean:

the enterprise system cannot change afterward

Therefore external systems remain authoritative for current business state.

⸻

28. Context Resolution

Context may need to be resolved before an Action becomes executable.

Example:

"Send it to John."

requires resolving:

"it"
"John"

against contextual information.

Conceptually:

Raw Intent
    ↓
Context Resolution
    ↓
Resolved References
    ↓
Executable Intent

⸻

29. Context Resolution Must Not Invent Facts

If context does not uniquely resolve an entity:

John Smith
John Doe
John Williams

Noema should not select one arbitrarily.

Instead:

AMBIGUOUS
   ↓
CLARIFICATION

This aligns with Noema’s deterministic handling of ambiguity.

⸻

30. Context and Ambiguity

Context exists partly to reduce ambiguity.

For example:

"Send it to John."

may be ambiguous globally.

But:

previous recipient = John Smith

may resolve it.

However, the contextual evidence must be sufficiently strong under policy.

⸻

31. Context Confidence

Context itself may have confidence or certainty characteristics.

For example:

location:
source = device
accuracy = 10m

Noema may determine whether that is sufficient for the Action.

The model should not silently convert uncertain context into deterministic fact.

⸻

32. Context and Evidence

Context can become evidence for a decision.

For example:

Source:
authorization_service
Observation:
user has permission X
Observed:
2026-08-27T10:00

The Trust Engine can then evaluate whether that evidence satisfies the relevant policy.

⸻

33. Context and Trust

The Trust Engine may evaluate context according to:

source
provenance
freshness
scope
integrity
confidence
authorization
policy

Therefore:

Context
  ↓
Evidence
  ↓
Deterministic Trust Engine

rather than:

Context
  ↓
automatic truth

⸻

34. Context Injection

Consumers should be able to provide contextual information when appropriate.

Conceptually:

{
  "context": {
    "channel": "mobile",
    "session_id": "sess_123"
  }
}

But externally supplied context should be treated as claims until validated.

⸻

35. Context Retrieval

Noema may need to retrieve context from enterprise systems.

Conceptually:

Noema
  ↓
Context API
  ↓
Enterprise Context Provider
  ↓
Account / Resource / Policy State

The Context API should support controlled retrieval rather than unrestricted data access.

⸻

36. Context Providers

A context provider supplies information relevant to a decision.

Examples:

Identity Provider
Authorization Service
CRM
Core Banking System
HR System
Payment Provider
Resource API
Event Store

The provider remains authoritative for the information it owns.

⸻

37. Context Provider Contract

A provider should define:

context type
source identity
schema
freshness
availability
trust characteristics
versioning

This prevents Noema from treating arbitrary external responses as interchangeable context.

⸻

38. Context API and Enterprise Action Graph

Context is one of the inputs used to construct and traverse the Enterprise Action Graph.

Conceptually:

Enterprise APIs
Documentation
Policies
Events
Workflows
        +
Context
        ↓
Enterprise Action Graph

Context allows Noema to determine which parts of the graph are relevant to the current execution.

⸻

39. Context and Action Contracts

An Action Contract may declare required context.

Example:

Action:
transfer_funds
Required Context:
Actor
Account
Authorization
Currency
Current balance
Risk state

The Action should not execute until required context is available and sufficiently trusted.

⸻

40. Required vs Optional Context

Contracts should distinguish:

required context
optional context
advisory context

For example:

customer_id → required
channel → optional
device_type → advisory

Missing required context should prevent execution.

⸻

41. Context Constraints

Context can have constraints.

Example:

currency = NGN

or:

actor.tenant == resource.tenant

or:

authorization.expires_at > execution.start

These constraints can become preconditions for execution.

⸻

42. Context Consistency

Noema may receive contradictory context.

Example:

tenant = bank_A
resource.tenant = bank_B

This must not be silently resolved.

The system should produce:

CONTEXT_CONFLICT

and transition into the appropriate Trust or clarification state.

⸻

43. Context Conflicts

Potential conflict categories include:

identity conflict
tenant conflict
resource conflict
authorization conflict
temporal conflict
version conflict
source conflict

The resolution strategy should be policy-defined.

⸻

44. Context Precedence

When multiple sources provide different values:

Source A → status = ACTIVE
Source B → status = BLOCKED

Noema needs an explicit precedence or reconciliation policy.

It should not rely on:

latest response wins

without semantic justification.

⸻

45. Context and Time

Context-dependent decisions must account for temporal validity.

Example:

authorization valid at 10:00
authorization revoked at 10:05
Action executes at 10:10

The API must allow the Trust layer to determine which authorization state governs execution.

⸻

46. Context and Historical State

Historical context should be distinguishable from current context.

previous_balance = ₦100,000
current_balance = ₦20,000

These are not interchangeable.

The API should preserve temporal semantics.

⸻

47. Context and User Confirmation

Confirmation is contextual information, but it has special trust requirements.

Example:

User confirmed:
"Yes, transfer ₦5,000,000."

Noema should record:

who confirmed
what was confirmed
when
under which session
against which proposed Action

A generic:

confirmed = true

is insufficient for consequential Actions.

⸻

48. Context and Clarification

Clarification responses should update the relevant context or Intent state explicitly.

Example:

Question:
"Which John?"
Answer:
"John Smith."

This should produce something semantically equivalent to:

recipient = John Smith

rather than merely storing the raw conversation text.

⸻

49. Context and Execution Recovery

Context should support recovery after failures.

If an executor crashes:

Action
Execution
Attempt
Context Snapshot

must remain recoverable.

The new attempt should know the relevant contextual basis without relying on ephemeral process memory.

⸻

50. Context and Retries

Retries may require fresh context.

For example:

Attempt 1:
balance = ₦100,000
Attempt 2:
balance = ₦50,000

The retry must not blindly reuse stale context.

Therefore:

Retryable execution does not imply reusable context.

⸻

51. Context and Reconciliation

Reconciliation often exists specifically to obtain authoritative context after an uncertain execution.

UNKNOWN
   ↓
Context retrieval
   ↓
Provider state
   ↓
Evidence
   ↓
Outcome

This is particularly important for financial or otherwise consequential Actions.

⸻

52. Context API and Determinism

Context acquisition may involve probabilistic interpretation upstream, but once context becomes part of a Trust decision it should have explicit semantics.

For a deterministic decision, Noema should know:

what context was used
where it came from
when it was observed
why it was trusted

⸻

53. Context API and LLMs

An LLM may extract contextual information from natural language.

For example:

User:
"Use the account I normally use."

The model may identify candidate context.

But the model should not independently establish:

account = account_123

for a consequential Action.

Noema must resolve that candidate against deterministic evidence and policy.

⸻

54. Context API and Probabilistic Information

Some context may inherently be uncertain:

estimated location
inferred preference
predicted intent
likely entity

Such information should carry appropriate uncertainty rather than being promoted to authoritative fact.

⸻

55. Context API and Privacy

Context can contain sensitive enterprise or user information.

The API should therefore enforce:

least privilege
tenant isolation
field-level access where necessary
purpose limitation
retention policies
auditability

Noema should only expose context necessary for the relevant execution.

⸻

56. Context Minimization

Consumers should not provide or request context simply because it is available.

The preferred model is:

required context
    ↓
retrieve only what is necessary
    ↓
evaluate
    ↓
discard or retain according to policy

This reduces both security and reasoning complexity.

⸻

57. Context API and Authorization

Context retrieval itself may require authorization.

For example:

Noema
  ↓
Request account balance

The context provider should verify that Noema is permitted to retrieve that information.

Context access is therefore itself an enterprise integration concern.

⸻

58. Context API and Tenant Isolation

Every contextual resource should have clear tenancy semantics where applicable.

Conceptually:

Tenant A
 └── Context
      └── Resources
Tenant B
 └── Context
      └── Resources

Noema must not permit cross-tenant context contamination.

⸻

59. Context API and Caching

Context may be cached where appropriate.

But cached context must carry:

source
observed_at
expires_at / freshness policy
version

A cached value must not be treated as current indefinitely.

⸻

60. Context Invalidation

Context may become invalid because:

authorization revoked
resource changed
session expired
tenant changed
policy changed
provider state changed
time window expired

The API should support invalidation or freshness evaluation.

⸻

61. Context Snapshot for Audit

For consequential Actions, Noema should be able to reconstruct:

Context at decision time

without necessarily storing every underlying data field permanently.

References to authoritative sources may be sufficient where permitted.

⸻

62. Context API Resource Model

Conceptually:

{
  "context_id": "ctx_123",
  "scope": "action",
  "action_id": "act_456",
  "values": {
    "channel": "mobile",
    "tenant_id": "tenant_789"
  },
  "observations": [
    {
      "key": "account_status",
      "value": "active",
      "source": "account_service",
      "observed_at": "..."
    }
  ]
}

This is illustrative, not a finalized wire schema.

⸻

63. Canonical Context Operations

The Context API may conceptually support:

Create Context
Get Context
Resolve Context
Query Context
Refresh Context
Invalidate Context
Snapshot Context
Attach Context
Detach Context

Not every operation needs to be publicly exposed.

⸻

64. Attach Context

Context may be attached to:

Intent
Action
Execution
Attempt
Session

The scope must be explicit.

⸻

65. Refresh Context

A consumer may request fresh context when existing context is stale.

Conceptually:

POST /contexts/{id}/refresh

The resulting context should preserve the provenance of newly retrieved observations.

⸻

66. Invalidate Context

Context can be explicitly invalidated.

Example:

authorization context revoked

The resulting state may cause an Action to transition from:

READY

to:

BLOCKED

before execution.

⸻

67. Context Query

Context queries should be constrained by:

tenant
scope
purpose
authorization
data classification

Noema should not expose a generic:

give me everything you know

interface.

⸻

68. Context API and Events

Context may be updated through events.

Example:

ACCOUNT_BLOCKED
AUTHORIZATION_REVOKED
CARD_STATUS_CHANGED
USER_ROLE_CHANGED

Noema can use these events to invalidate or update contextual observations.

⸻

69. Context and Event Ordering

Distributed events may arrive out of order.

Therefore Noema should use:

event timestamp
sequence
resource version
causal information

where available.

It should not assume:

last received = latest state

without evidence.

⸻

70. Context and Concurrency

Context can change while an Action is executing.

Example:

Action starts
   ↓
account status changes
   ↓
Action continues

The Action Contract and Trust policy determine whether the change requires:

abort
pause
re-evaluate
continue

⸻

71. Context and Preconditions

Context is often the input to precondition evaluation.

Context
  ↓
Precondition
  ↓
Satisfied?

For example:

context.account.status == "active"

may satisfy:

precondition:
account must be active

⸻

72. Context and Postconditions

Context can also be used to establish whether an Outcome occurred.

Example:

Before:
card.status = LOST
After:
card.status = REPLACEMENT_PENDING

The difference between contextual observations can establish evidence for the postcondition.

⸻

73. Context and Outcomes

An Outcome should record the relevant contextual basis when necessary.

For example:

Outcome:
replacement_card_created
Context:
card_456
observed provider state
execution timestamp

This makes the Outcome auditable.

⸻

74. Context API and System of Record

Noema may become the system of record for:

context observations used in execution decisions

but not necessarily for:

the underlying enterprise state itself

This distinction should remain explicit.

⸻

75. Context API and Canonical Documentation

The Context API should align with:

ontology/context.md
intent/intent-model.md
trust/evidence.md
trust/determinism.md
execution/preconditions.md
execution/postconditions.md
execution/retries.md
interfaces/action-api.md

It should not redefine those concepts independently.

⸻

76. Canonical Flow

Context Sources
      │
      ▼
 Context API
      │
      ▼
Context Resolution
      │
      ├──────────────┐
      ▼              ▼
Intent Context   Execution Context
      │              │
      └──────┬───────┘
             ▼
        Trust Engine
             │
             ▼
      Policy / Preconditions
             │
             ▼
          Execution
             │
             ▼
      Evidence / Outcome

⸻

77. Context Failure

Context retrieval may fail.

Examples:

provider unavailable
stale data
invalid response
authorization denied
conflicting observations
resource not found

The system should distinguish:

context unavailable

from:

context says Action is invalid

These are different conditions.

⸻

78. Context Unavailable

If required context cannot be obtained:

Action
   ↓
required context unavailable
   ↓
BLOCKED / WAITING / INTERVENTION

Noema should not guess the missing context.

⸻

79. Context Conflict

If trusted sources disagree:

Source A → ACTIVE
Source B → BLOCKED

Noema should transition into a deterministic conflict-handling state rather than selecting whichever value appears more plausible.

⸻

80. Context and Clarification

Not all context failures require the user.

If the missing context is:

"Which John?"

clarification may be appropriate.

If it is:

"Current account balance unavailable."

the correct response may be:

WAIT
RETRY
RECONCILE
ESCALATE

rather than asking the user something they cannot resolve.

⸻

81. Context API Invariants

Invariant 1

Context is distinct from Intent.

Invariant 2

Context is distinct from authoritative enterprise business state.

Invariant 3

Every consequential contextual observation should have identifiable provenance.

Invariant 4

Caller-supplied context is untrusted until validated where trust matters.

Invariant 5

Context has explicit scope.

Invariant 6

Context has explicit lifetime or freshness semantics where required.

Invariant 7

Stale context must not silently satisfy freshness-sensitive requirements.

Invariant 8

Conflicting trusted context must not be resolved through arbitrary preference.

Invariant 9

Missing required context must not be guessed.

Invariant 10

Context must not bypass Authorization or Policy.

Invariant 11

Context used for consequential decisions must be auditable.

Invariant 12

Context retrieval must respect tenant and authorization boundaries.

Invariant 13

Historical context must remain distinguishable from current context.

Invariant 14

Retry does not automatically permit reuse of stale context.

Invariant 15

Context uncertainty must remain explicit until resolved.

Invariant 16

Noema may consume enterprise state as context without becoming its system of record.

Invariant 17

Context resolution must not silently create facts unsupported by evidence.

Invariant 18

Context semantics (Grounding) must remain consistent across Intent, Trust, and Execution.

⸻

82. Canonical Mental Model

                 CONTEXT SOURCES
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
   Enterprise       Identity        Conversation
    Systems          Systems           History
       │               │                │
       └───────────────┼────────────────┘
                       ▼
                 CONTEXT API
                       │
                       ▼
               CONTEXT RESOLUTION
                       │
              ┌────────┴────────┐
              ▼                 ▼
           INTENT             ACTION
           CONTEXT           CONTEXT
              │                 │
              └────────┬────────┘
                       ▼
                  TRUST ENGINE
                       │
                       ▼
                 EXECUTION
                       │
                       ▼
                 EVIDENCE
                       │
                       ▼
                   OUTCOME

⸻

83. Canonical Architecture Invariants

The Context API strictly adheres to the core Noema invariants:

*   **Fail-Closed on Unknown:** If context required for a decision cannot be reliably established or trusted, the system must fail closed. Missing context must not default to 'allow'.
*   **No Hidden Authority:** Contextual claims supplied by an external entity are treated as observations, not authoritative truths, until verified against policy.
*   **Deterministic Trust Evaluation:** All contextual evidence is evaluated deterministically by the Trust Engine without probabilistic guessing.
*   **Consumer-Side Authoritative Validation:** The source system of the context remains authoritative for its business state; Noema only holds a temporal observation of that state.

⸻

84. Final Definition

The Context API is Noema’s interface for managing the contextual information surrounding Intent and execution. It provides structured, scoped, provenance-aware context to the Intent, Trust, and Execution layers while preserving the distinction between contextual observation and authoritative enterprise state.

The core principle is:

Context informs Noema’s decisions; it does not become truth merely because it exists. Every consequential contextual fact must be attributable, appropriately trusted, sufficiently fresh, correctly scoped, and evaluated according to policy before it can influence execution.