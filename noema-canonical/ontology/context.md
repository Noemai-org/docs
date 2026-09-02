Yes. And this time I’ll keep it aligned with the current Noema Canon, particularly the distinction between ontology, context, enterprise truth, intent, evidence, and trust. This is 01-ontology/context.md, so it should define the concept at the ontology level rather than instantiate a specific workflow.

Context

Status: Foundational
Version: 0.1
Domain: Ontology
Canonical Path: ontology/context.md

⸻

1. Definition

Context is the bounded set of information relevant to interpreting an Intent, resolving ambiguity, evaluating Trust, planning an Action, executing that Action, or verifying its Outcome.

Context answers:

“What information is relevant to this decision or execution at this point in time?”

Context is not synonymous with:

Enterprise State
Canonical Data
Evidence
Intent
Business State
Model Input
Conversation History

It is the information made available to Noema for a particular execution journey.

Conceptually:

Enterprise Systems
       │
       ▼
Relevant Information
       │
       ▼
     Context
       │
       ├── Intent Resolution
       ├── Trust Evaluation
       ├── Planning
       ├── Execution
       └── Verification

⸻

2. Purpose

The purpose of Context is to provide Noema with enough relevant information to make an explicit and bounded decision.

Context allows Noema to establish things such as:

Who is acting?
What is being requested?
What Resource is involved?
What is the current relevant state?
Which policies apply?
What permissions exist?
What evidence supports the decision?
What happened previously?
What constraints apply?
What information is still missing?

Context should therefore be decision-oriented, rather than indiscriminately comprehensive.

⸻

3. Core Principle

Context is relevant information within a defined scope.

More context does not necessarily produce better decisions.

Excess context can introduce:

irrelevant information
stale information
conflicting information
privacy exposure
authorization complexity
model confusion
unnecessary data dependencies

Therefore:

Noema should retrieve and expose the minimum Context necessary for the current decision or Action.

⸻

4. Context Is Scoped

Context always exists within a scope.

Relevant dimensions may include:

Intent
Workflow
Action
Resource
Principal
Tenant
Organization
Environment
Time
Policy
Execution State

For example:

Context for:
"Show my balance"

may differ substantially from:

Context for:
"Transfer $9,000"

even when both involve the same customer and account.

⸻

5. Context Is Dynamic

Context is not necessarily static for the lifetime of an Intent.

Enterprise state may change.

Policies may change.

Permissions may change.

Risk may change.

Execution state may change.

Therefore:

Context(T1)
      ≠
Context(T2)

in general.

Noema must determine when Context remains valid and when it must be refreshed.

⸻

6. Context vs Canonical Data

Canonical Data is authoritative information within a defined enterprise authority boundary.

Context is information assembled for Noema’s reasoning or execution.

Therefore:

Canonical Data
       ↓
     Context

may be valid.

But:

Context
       ↓
Canonical Data

must not happen automatically.

For example:

Ledger:
balance = $10,000
Noema Context:
balance = $10,000

The Context contains the value.

The Ledger remains authoritative for the underlying Business State.

⸻

7. Context vs Business State

Business State belongs to the enterprise systems that own the relevant business domain.

Examples:

Account.balance
Payment.status
Card.status
Customer.status
Inventory.quantity

Noema may observe these values through Context.

It does not thereby become their owner.

Enterprise System
       │
       ▼
Business State
       │
       ▼
     Context
       │
       ▼
     Noema

This preserves the enterprise authority boundary.

⸻

8. Context vs Noema State

Noema also has its own state.

Examples:

Intent State
Trust State
Action State
Execution State
Intervention State
Outcome State

These are canonical within Noema’s execution domain.

Therefore two different authority domains can coexist:

Enterprise Canonical State
        │
        │
        ▼
     Context
        │
        │
        ▼
Noema Execution State

Neither should silently replace the other.

⸻

9. Context vs Intent

Intent represents what a Principal is trying to accomplish.

Context provides information that helps Noema understand that Intent.

Example:

Intent:
"Show me my transactions from last month."
Context:
customer_id
account_id
available accounts
date
transaction access permissions

Context helps resolve the Intent.

It does not become the Intent itself.

⸻

10. Context vs Evidence

Evidence supports a proposition or decision.

Context is the information available for reasoning or execution.

For example:

Context:
account.balance = $10,000

Evidence may record:

Source:
Ledger
Observed:
2026-09-01T10:15:00
Value:
account.balance = $10,000
Version:
482

Therefore:

Context
   +
Provenance
   ↓
Evidence

may describe why a Context value should be trusted.

⸻

11. Context vs Model Input

Context may be provided to a model.

But:

Model Input ⊂ Context

is often more appropriate than:

Model Input = Entire Context

The model should receive only the information necessary for its particular task.

For example, Intent Resolution may require:

User request
Relevant account identifiers
Available resources
Relevant conversation history

It may not require:

Full transaction history
Unrelated customer data
Internal security metadata

⸻

12. Context vs Model Output

Model output may add interpretations to the execution journey.

Examples:

"The user is asking for a spending summary."
"Account 123 is probably the intended account."
"The user may mean transactions from August."

These are model-derived interpretations.

They are not automatically canonical Context.

They must retain their appropriate semantic classification.

Model Output
      ↓
Interpretation
      ↓
Validation / Grounding
      ↓
Context

where applicable.

⸻

13. Context Components

Context may contain several categories of information.

Conceptually:

Context
   │
   ├── Identity
   ├── Intent
   ├── Resources
   ├── Business State
   ├── Policy
   ├── Permissions
   ├── Evidence
   ├── Temporal State
   ├── Organizational State
   ├── Conversation
   └── Execution State

Not every execution requires every category.

⸻

14. Identity Context

Identity Context establishes the Principal relevant to the execution.

Examples:

principal_id
customer_id
organization_id
tenant_id
authentication state
identity verification state

Identity Context is especially important when an Intent references:

"my account"
"my transactions"
"my statement"
"our organization"

Identity must be grounded appropriately before consequential execution.

⸻

15. Resource Context

Resource Context identifies the enterprise Resources relevant to the Intent.

Examples:

account
payment
transaction
invoice
customer
order

For example:

Intent:
"Show my balance."
Context:
customer_id = C-123
account_id = A-456

If multiple Resources are possible, Context may expose the ambiguity rather than resolving it arbitrarily.

⸻

16. Business-State Context

Business-State Context represents relevant enterprise state.

Examples:

account.status
account.balance
payment.status
transaction.amount
transaction.date

The underlying state remains owned by the appropriate enterprise System of Record.

Context is the representation consumed by Noema.

⸻

17. Policy Context

Policy Context contains rules relevant to the current decision.

Examples:

access policy
transaction limits
retention policy
approval requirements
risk thresholds
execution constraints

Policy Context must be temporally and organizationally scoped.

A Policy applicable to one tenant or environment must not silently apply to another.

⸻

18. Authorization Context

Authorization Context contains information necessary to determine whether a Principal may perform an Action against a Resource.

Examples:

Principal
Role
Permissions
Resource
Tenant
Organization
Delegation
Action

Context provides the information.

The Trust Engine determines whether authorization requirements are satisfied.

⸻

19. Temporal Context

Many decisions depend on time.

Temporal Context may include:

current time
effective time
observation time
resource timestamps
policy validity
execution time
historical state

For example:

Current Time:
2026-09-01
Transaction Range:
2026-08-01 → 2026-08-31

Temporal Context should use the appropriate timezone and enterprise semantics.

⸻

20. Historical Context

Historical information may be relevant to an execution.

Examples:

previous Intent
previous clarification
previous Action
previous execution attempt
previous approval
previous failure
previous Policy version

Historical Context should not automatically override current canonical Business State.

Its purpose is to provide relevant temporal information.

⸻

21. Conversation Context

Conversation history may be part of Context.

Example:

User:
"Show my transactions."
Noema:
"Which account?"
User:
"My current account."

The second message depends on the first.

Conversation Context can therefore contribute to Intent Resolution.

However:

Conversation history is not authoritative enterprise state.

⸻

22. Execution Context

Execution Context represents the current Noema execution journey.

Examples:

workflow_id
intent_id
action_id
current execution state
previous attempts
pending Actions
completed Actions
failure state
intervention state

This is distinct from enterprise Business State.

For example:

Noema:
execution.status = AWAITING_VERIFICATION
Enterprise:
account.status = ACTIVE

Both may be valid simultaneously.

⸻

23. Context and Ambiguity

Context can reduce ambiguity.

It can also reveal ambiguity.

Example:

Intent:
"Show my account."
Context:
Account A
Account B
Account C

The Context establishes that multiple candidates exist.

It does not justify guessing.

Therefore:

Ambiguity
    ↓
Clarification

may be the correct next state.

This follows the Noema principle:

Ambiguity is a state, not an invitation to guess.

⸻

24. Context and Determinism

Context is one of the inputs to deterministic decision-making.

Conceptually:

Intent
   +
Context
   +
Evidence
   +
Policy
   +
Authorization
   +
Risk
   ↓
Trust Decision

The model may help construct or interpret Context.

The final execution decision must be governed by deterministic rules and enterprise constraints.

⸻

25. Context and Trust

Trust evaluates whether the available Context is sufficient and reliable enough for the intended Action.

Trust may consider:

authority
freshness
provenance
authorization
policy
risk
completeness
ambiguity
validation

Therefore:

Context
   ↓
Trust

does not mean that all Context is automatically trusted.

⸻

26. Context Completeness

Context completeness is Action-specific.

For one Action:

"Show my balance."

the required Context may be:

identity
account
balance
authorization

For another:

"Find my transactions from August."

it may require:

identity
account
date range
transaction access
transaction data

Therefore:

Context is complete when it contains the information required for the current decision, not when it contains everything known about the Principal or Resource.

⸻

27. Context Freshness

Context may become stale.

Example:

10:00
Context:
balance = $10,000
10:05
Enterprise:
balance = $8,000

The original Context may still be historically accurate.

It may no longer be suitable for a consequential Action.

Therefore Context must distinguish:

correct when observed

from:

current enough for this Action

⸻

28. Context Refresh

Noema may refresh Context when:

Action risk is high
freshness requirement has expired
enterprise state may have changed
Policy requires current state
Preconditions require fresh data
Postconditions require verification

Conceptually:

Existing Context
       ↓
Freshness Check
       ↓
Refresh Required
       ↓
Enterprise System
       ↓
Updated Context

⸻

29. Context Snapshots

Noema may create a Context Snapshot representing the information used for a particular decision.

Conceptually:

ContextSnapshot {
    intent
    principal
    resources
    facts
    policies
    evidence
    timestamp
    versions
}

Snapshots support:

auditability
reconstruction
debugging
decision explanation
historical analysis

A snapshot does not become the current enterprise truth.

⸻

30. Context and Preconditions

Preconditions depend on Context.

Example:

Precondition:
account.status = ACTIVE

Context supplies the relevant state:

account.status = ACTIVE

Trust evaluates whether that information is sufficiently authoritative and current to satisfy the Precondition.

⸻

31. Context and Postconditions

Postconditions may require Context after an Action.

Example:

Action:
retrieve_statement

Postcondition:

statement successfully retrieved

Noema may need new Context after execution to establish the Outcome.

For state-changing Actions, this distinction becomes even more important:

Action
   ↓
Enterprise State Change
   ↓
Fresh Context
   ↓
Postcondition

⸻

32. Context and Planning

Planning uses Context to determine the feasible execution path.

Example:

Intent:
"Show my spending for August."
Context:
customer
accounts
transactions
date range
permissions

The Planner may determine:

resolve account
→ retrieve transactions
→ aggregate spending
→ return result

Planning must operate within the authority, Policy, and Trust boundaries established elsewhere in the Canon.

⸻

33. Context and Execution

Execution consumes the Context required by the Action Contract.

For example:

Action:
search_transactions

may require:

principal_id
account_id
start_date
end_date
authorization

The Action should not receive arbitrary enterprise data merely because it exists in the broader Context.

⸻

34. Context and Read Operations

Noema’s initial commercial wedge emphasizes read and support operations.

Examples:

balance inquiries
statement retrieval
transaction search
spending summaries
complaint logging

These operations still require Context.

For example:

"How much did I spend last month?"

may require:

identity
account
date range
transactions
currency
authorization

The fact that an operation is read-oriented does not eliminate Trust requirements.

⸻

35. Context and Financial Writes

Future financial write operations may require substantially stronger Context guarantees.

For example:

"Transfer $9,000 to John."

may require:

identity
recipient identity
source account
destination account
balance
limits
authorization
risk
policy
confirmation
freshness

The Context requirements therefore scale with Action risk.

⸻

36. Context and Data Minimization

Noema should apply the principle:

Retrieve what is necessary for the decision, and no more.

For example, a transaction search may require:

account_id
date range
transaction fields

It does not automatically require:

full customer profile
home address
unrelated accounts
complete account history

Context should therefore be purpose-bound.

⸻

37. Context and Data Boundaries

Context must respect enterprise data boundaries.

These may include:

tenant
organization
legal entity
business unit
environment
data classification
resource ownership

Noema must not construct a Context that crosses these boundaries implicitly.

⸻

38. Context and Permissions

The fact that Noema can technically retrieve information does not mean that information should enter Context.

Access must remain bounded by:

authorization
purpose
scope
data policy

Therefore:

Accessible Data
      ≠
Permitted Context

⸻

39. Context and Provenance

Consequential Context should preserve provenance where required.

Conceptually:

ContextFact {
    name
    value
    source
    authority
    observed_at
    effective_at
    version
}

This allows Noema to determine:

Where did this information come from?
When was it observed?
Who or what is authoritative?
Which version was used?

⸻

40. Context and Conflicting Information

Context may contain conflicting values.

Example:

Ledger:
balance = $10,000
Cache:
balance = $8,000

Noema should not resolve the conflict through:

model confidence
majority vote
arbitrary source selection

Instead, it should apply the authority model.

If the conflict remains consequential:

CONFLICT
   ↓
Trust / Policy
   ↓
Clarify / Escalate / Reject

as appropriate.

⸻

41. Context and Missing Information

Required Context may be unavailable.

Example:

Identity available
Account available
Policy available
Balance unavailable

If the Action requires current balance:

Context Incomplete
       ↓
Trust
       ↓
Retry / Clarify / Escalate / Reject

Noema should not invent the missing value.

⸻

42. Context and Human Intervention

A human may supply additional information or make a decision when automated Context is insufficient.

Example:

Automated Context
       ↓
Insufficient
       ↓
Human Review
       ↓
Additional Evidence / Decision
       ↓
Updated Context

The human intervention itself becomes part of the execution record and should preserve its authority and scope.

⸻

43. Context and Events

Events may contribute to Context.

Example:

Enterprise System
       ↓
account.balance.changed
       ↓
Event
       ↓
Noema
       ↓
Context Update

An event represents an observation or notification of change.

It does not necessarily establish the complete current canonical state.

Where required, Noema should verify against the System of Record.

⸻

44. Context and Eventual Consistency

Context may originate from eventually consistent projections.

Therefore:

System of Record
       ↓
Event
       ↓
Projection
       ↓
Context

may produce temporarily stale information.

Noema must understand the consistency semantics before using such Context for consequential decisions.

⸻

45. Context and Idempotency

Execution Context may contain information about previous attempts.

Example:

workflow_id = W-123
action_id = A-456
attempt = 2
previous_result = UNKNOWN

This information can help determine whether an Action should be retried or whether its prior execution must first be reconciled.

⸻

46. Context and Failure

Failure Context records information relevant to understanding an unsuccessful execution.

Examples:

Action attempted
failure type
source system
timestamp
attempt number
enterprise response
last known state

This information supports:

retry
recovery
compensation
human intervention
audit

⸻

47. Context and Recovery

Recovery may require Context different from the Context used for the original attempt.

For example:

Attempt 1
   ↓
Timeout
   ↓
Enterprise state may have changed
   ↓
Refresh Context
   ↓
Re-evaluate
   ↓
Retry / Reconcile / Escalate

Noema must not assume that stale Context remains valid after failure.

⸻

48. Context and Auditability

For consequential execution, Noema should preserve enough Context to reconstruct the decision.

Relevant information may include:

Principal
Intent
Resources
Relevant enterprise facts
Policy
Evidence
Authorization
Trust decision
Action
Timestamp
Versions
Outcome

Sensitive data should be subject to applicable retention and access policies.

⸻

49. Context and Reconstruction

A historical execution should be reconstructable without pretending that historical Context is today’s Context.

Conceptually:

Historical Intent
       +
Historical Context
       +
Historical Evidence
       +
Historical Policy
       ↓
Historical Decision

This is essential for auditability.

⸻

50. Context Lifecycle

Context may move through several semantic states:

REQUESTED
    ↓
ASSEMBLED
    ↓
VALIDATED
    ↓
AVAILABLE
    ↓
CONSUMED
    ↓
REFRESHED
    ↓
EXPIRED

These are conceptual states.

A particular implementation may represent them differently.

⸻

51. Context Expiration

Context should be considered expired when its freshness or validity no longer satisfies the requirements of the current decision.

Expiration may result from:

time
enterprise state change
Policy change
permission change
Resource change
workflow transition
risk change

Expired Context may remain useful historically.

It should not necessarily be used for current execution.

⸻

52. Context Partitioning

Large Context should be partitionable by purpose.

For example:

Intent Context
      │
      ├── Identity Context
      ├── Resource Context
      └── Conversation Context
Trust Context
      │
      ├── Authorization
      ├── Policy
      ├── Evidence
      └── Risk
Execution Context
      │
      ├── Action
      ├── Preconditions
      ├── Attempts
      └── Outcomes

This reduces unnecessary data exposure and makes semantic ownership clearer.

⸻

53. Context and Authority

Every consequential Context fact should have an identifiable authority where applicable.

The authority hierarchy should not be replaced by:

recency
frequency
model confidence
source count

For example:

Ledger
   ↓
Canonical Balance
Analytics DB
   ↓
Derived Balance

Both may appear in Context.

They do not have equivalent authority.

⸻

54. Context and Confidence

Context should not be reduced to one global confidence score.

Different Context elements may have different semantic status:

Canonical
Derived
Observed
User-provided
Model-inferred
Historical
Stale
Unknown

For example:

account_id
→ canonical
spending_category
→ derived
user statement
→ user-provided
intent interpretation
→ model-derived

The system should preserve these distinctions.

⸻

55. Context and Uncertainty

Uncertainty should be represented explicitly.

For example:

account_id = UNKNOWN

is preferable to:

account_id = probably 123

when the account identifier is consequential.

Likewise:

Context:
multiple candidate accounts

is preferable to silently selecting one.

Noema should preserve uncertainty until it can be resolved according to deterministic rules, Policy, or explicit user confirmation.

⸻

56. Context and Clarification

Clarification is a mechanism for completing Context when information required for Intent or Action remains unresolved.

Example:

User:
"Show my statement."
Context:
Account A
Account B
        ↓
Clarification:
"Which account would you like the statement for?"

The answer becomes additional Context.

This allows the execution journey to progress without guessing.

⸻

57. Context and Enterprise Integration

Integrations provide mechanisms for acquiring Context.

Examples:

REST APIs
GraphQL APIs
event streams
databases
identity providers
policy systems
enterprise applications

The integration mechanism is not itself Context.

It is the mechanism through which Context may be acquired.

⸻

58. Context and Integration Failure

If an integration fails:

Enterprise API
      ↓
Unavailable
      ↓
Required Context Missing

Noema must apply the relevant Trust and Policy rules.

It should not silently substitute arbitrary information merely to keep the Workflow moving.

⸻

59. Context Model

Conceptually:

Context {
    principal
    intent
    resources
    facts
    policies
    permissions
    evidence
    temporal_state
    organizational_state
    conversation
    execution_state
}

This is a semantic model.

It does not require a literal database object with these exact fields.

⸻

60. Context Fact

An individual Context fact may be represented conceptually as:

ContextFact {
    subject
    attribute
    value
    source
    authority
    classification
    observed_at
    effective_at
    expires_at
    version
    provenance
}

Not every field is required for every fact.

The model exists to preserve the semantics necessary for Trust and execution.

⸻

61. Context Relationships

Context connects the major Noema concepts:

Principal
    │
    ▼
Intent
    │
    ▼
Context
    │
    ├── references → Resource
    ├── contains → Facts
    ├── includes → Policy
    ├── includes → Evidence
    ├── constrained_by → Permissions
    ├── bounded_by → Organization
    ├── scoped_by → Time
    └── tracks → Execution

Context therefore acts as a semantic bridge between Intent and enterprise execution.

⸻

62. Context in the Noema Execution Model

The broader Noema flow is:

USER
 │
 ▼
INTENT
 │
 ▼
INTENT RESOLUTION
 │
 ▼
CONTEXT
 │
 ▼
TRUST
 │
 ├── Clarify
 ├── Escalate
 ├── Reject
 └── Execute
          │
          ▼
       ACTION
          │
          ▼
      ENTERPRISE
          │
          ▼
   FRESH CONTEXT
          │
          ▼
    POSTCONDITION
          │
          ▼
       OUTCOME

Context therefore participates throughout the execution journey rather than existing only at the beginning.

⸻

63. Context and Noema’s Commercial Wedge

Noema’s initial commercial wedge focuses on read and support operations:

balance inquiries
statement retrieval
transaction search
spending summaries
complaint logging

Even these apparently simple operations require Context.

For example:

"How much did I spend last month?"

requires Noema to establish:

Principal
Account
Date Range
Relevant Transactions
Currency
Authorization

The value of Noema is therefore not merely retrieving data.

It is resolving natural-language Intent into a bounded, authorized, trustworthy enterprise operation.

⸻

64. Context and Future Expansion

The Context model should support future higher-risk operations without assuming that they belong to the initial wedge.

Future Actions may require stronger guarantees around:

authorization
freshness
confirmation
risk
policy
identity
financial state
execution verification

The Context model should therefore be extensible while preserving the same authority boundaries.

⸻

65. Context Invariants

Invariant 1

Context is bounded information relevant to a particular decision or execution.

Invariant 2

Context is not synonymous with enterprise Business State.

Invariant 3

Context does not become canonical merely because Noema stores or consumes it.

Invariant 4

Enterprise Systems of Record remain authoritative for their respective Business State.

Invariant 5

Context must preserve the authority semantics of the information it contains.

Invariant 6

Context must be scoped by the relevant Principal, Resource, Action, organization, tenant, environment, and time where applicable.

Invariant 7

Context should contain the minimum information necessary for the current decision.

Invariant 8

Context completeness is Action-specific.

Invariant 9

Context freshness is independent of authority.

Invariant 10

Stale Context must not be used for consequential execution when freshness requirements are not satisfied.

Invariant 11

Model-generated interpretations must remain distinguishable from authoritative enterprise facts.

Invariant 12

User-provided information is not canonical by default.

Invariant 13

Derived information is not canonical by default.

Invariant 14

Evidence and Context are related but semantically distinct.

Invariant 15

Conversation history may contribute to Context but cannot redefine enterprise Business State.

Invariant 16

Conflicting Context must not be resolved through probabilistic guessing when authoritative resolution is required.

Invariant 17

Missing consequential Context must remain explicitly represented.

Invariant 18

Ambiguity revealed by Context must remain an explicit state until deterministically resolved.

Invariant 19

Context used for consequential execution should retain sufficient provenance for audit and reconstruction.

Invariant 20

Context may need to be refreshed between planning, execution, retry, and verification.

Invariant 21

Historical Context must remain distinguishable from current Context.

Invariant 22

Context must respect enterprise authorization, privacy, tenancy, organizational, legal, and environment boundaries.

Invariant 23

Noema must not create shadow canonical Business State merely by maintaining Context.

Invariant 24

Context should be partitioned according to purpose and least-privilege requirements.

Invariant 25

The model may use Context probabilistically, but consequential execution must be governed by deterministic Trust and Policy.

Invariant 26

Context availability does not imply Context validity.

Invariant 27

Context authority does not imply permission to access or use the underlying information.

Invariant 28

Events may contribute to Context without necessarily establishing current canonical state.

Invariant 29

Context snapshots may support auditability without becoming the current enterprise truth.

Invariant 30

When required Context cannot be established, Noema must preserve the uncertainty rather than manufacture certainty.

⸻

66. Final Definition

Context is the bounded, relevant, authority-aware information available to Noema for interpreting Intent, resolving ambiguity, evaluating Trust, planning Actions, executing against enterprise systems, and verifying Outcomes.

The fundamental relationship is:

ENTERPRISE SYSTEMS
       │
       ▼
RELEVANT FACTS
       │
       ▼
     CONTEXT
       │
       ├───────────────┐
       ▼               ▼
INTENT RESOLUTION    TRUST
       │               │
       └───────┬───────┘
               ▼
            ACTION
               │
               ▼
        ENTERPRISE SYSTEM
               │
               ▼
        FRESH CONTEXT
               │
               ▼
          POSTCONDITION
               │
               ▼
            OUTCOME

And the architectural rule is:

Context is what Noema needs to know to make and execute a decision—not everything the enterprise knows.

Noema may assemble, store, transform, and reason over Context, but it must preserve the authority, provenance, scope, freshness, and ownership of the information from which that Context is derived.