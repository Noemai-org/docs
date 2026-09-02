Context

Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/context.md

⸻

1. Definition

Context is the structured set of information available to Noema for understanding, validating, planning, executing, and verifying an Intent within a specific execution journey.

For the Customer Account Inquiry workflow, Context provides the information required to determine:

who is asking
what they are asking about
which enterprise resources are relevant
what information is available
what authority applies
what constraints apply
what has already happened

Context is not itself Intent.

Context is not Business State.

Context is not Evidence.

Context is the information envelope within which Noema makes execution decisions.

Conceptually:

Principal
     │
     ├── Identity
     ├── Intent
     ├── Enterprise State
     ├── Permissions
     ├── History
     ├── Evidence
     └── Policy
             │
             ▼
          Context
             │
             ▼
        Trust + Action

⸻

2. Purpose

The purpose of Context in this workflow is to provide sufficient information for Noema to execute customer account inquiries without requiring unrestricted access to enterprise data.

Context should answer:

What does Noema need to know
to safely perform this specific task?

The answer should be:

the minimum sufficient context

rather than:

everything available about the customer

⸻

3. Core Principle

Context is task-scoped.

A Customer Account Inquiry should only receive the information required for the resolved Intent and Action.

For example:

Intent:
"What is my account balance?"

may require:

customer_id
account_id
account_type
authorization_context

It does not automatically require:

full transaction history
home address
employment information
other accounts
complete customer profile

Context therefore follows the principle:

Context should be sufficient for execution, but no broader than necessary.

⸻

4. Context Is Not Truth

Context may contain information from multiple sources.

For example:

Context
├── Canonical Data
├── Evidence
├── Derived Data
├── Historical Data
├── User Input
└── Noema Execution State

These categories do not have equal authority.

Context is the container in which information is made available.

It does not automatically make that information authoritative.

Therefore:

Context ≠ Truth

⸻

5. Context and Canonical Data

Canonical Data represents authoritative enterprise information within a defined authority boundary.

Context may contain Canonical Data.

For example:

Context
    │
    └── Account.balance
            │
            └── source = Ledger

The Context carries the information.

The Ledger establishes its authority.

Noema must preserve that distinction.

⸻

6. Context and Evidence

Evidence records information that supports a proposition or execution decision.

Context may include Evidence.

Example:

Context
   │
   └── Evidence
          │
          └── Ledger observed account balance

The Evidence provides provenance for information used during execution.

Therefore:

Context
   contains
      ↓
Evidence
Context
   does not become
      ↓
Evidence

⸻

7. Context and Intent

Intent describes what the Principal wants to accomplish.

Context provides information needed to understand and execute that Intent.

Example:

Intent:
"How much do I have?"
Context:
customer_id = 4821
account_id = 9912
currency = NGN
authenticated = true

Together:

Intent
   +
Context
   ↓
Action Resolution

Context does not replace Intent.

⸻

8. Context and Principal

The Principal is the identity under whose authority the request is being made.

For the Customer Account Inquiry workflow:

Principal
    ↓
Customer
    ↓
Authenticated Identity

Context may contain:

principal_id
authentication_state
session_id
organization
tenant

where required.

The Principal identity must be grounded against enterprise identity data where consequential access is involved.

⸻

9. Context and Identity Resolution

Natural-language requests frequently contain ambiguous identity references.

Example:

"Show my account balance."

The phrase:

my account

must resolve to an authorized enterprise Resource.

Conceptually:

Principal
    ↓
Identity Resolution
    ↓
Customer
    ↓
Account

If multiple candidate resources exist and Policy requires certainty:

Ambiguity
    ↓
Clarification

Context must not silently resolve material ambiguity through probabilistic guessing.

⸻

10. Context and Resource Resolution

The workflow may involve multiple enterprise Resources.

Examples:

Customer
Account
Transaction
Statement
Support Case

Context should contain only the Resources relevant to the current Action.

For example:

get_account_balance
    ↓
account_id

while:

create_complaint
    ↓
customer_id
related_transaction_id

may require additional identifiers.

⸻

11. Context and Account Scope

Account identity must include sufficient scope to prevent accidental cross-account access.

Conceptually:

Account {
    tenant
    organization
    account_id
}

The exact fields depend on the enterprise environment.

The important property is:

identifier + authority scope

rather than identifier alone.

⸻

12. Context and Authorization

Context may contain authorization-relevant information.

For example:

principal_id
account_id
relationship
permissions
organization
scope

Authorization should then be evaluated according to enterprise Policy.

The presence of an account identifier in Context does not imply that the Principal is authorized to access it.

Therefore:

Context contains resource
        ≠
Principal authorized for resource

⸻

13. Context and Permissions

Permissions constrain what Noema may do with Context.

A Customer may be allowed to:

read balance
read transactions
retrieve statements
create complaints

but not:

access another customer's account
modify account ownership
execute financial transfers

Context must not be used to bypass enterprise authorization.

⸻

14. Context and Business State

Business State belongs to the enterprise systems that own the relevant domain.

For example:

Ledger
    ↓
Account Balance

Noema may retrieve this state into Context.

It does not become the owner of the balance.

Therefore:

Enterprise Business State
          ↓
        Context

rather than:

Context
   ↓
new Noema Business State

⸻

15. Context and Noema State

Noema owns state about the execution journey.

Examples:

intent_status
trust_status
action_status
execution_status
intervention_status

This may appear in Context when required for continuation or recovery.

Conceptually:

Enterprise State
       +
Noema Execution State
       ↓
Context

These states must remain semantically distinct.

⸻

16. Context and Temporal State

Context may contain time-related information.

Examples:

request_time
current_time
effective_time
observed_at
date_from
date_to
timezone

Temporal interpretation must be explicit.

For example:

"transactions from yesterday"

should resolve into an explicit interval before Action execution.

Conceptually:

Natural Language
       ↓
Temporal Resolution
       ↓
date_from + date_to + timezone

⸻

17. Context and Historical State

Previous interactions may be relevant to the current execution.

Examples:

previous clarification
previous Action
previous failure
previous customer response

Historical information should only be included when it is relevant to the current Intent.

Historical Context must not silently override current canonical enterprise state.

⸻

18. Context and Evidence Freshness

Information inside Context may have different freshness characteristics.

For example:

Ledger observation:
10 seconds old
Transaction projection:
5 minutes old
Customer-provided information:
2 hours old

Context should preserve freshness information where it affects Trust or execution.

Freshness is distinct from authority.

fresh ≠ canonical
canonical ≠ necessarily fresh

⸻

19. Context and Provenance

Consequential Context should preserve provenance.

Conceptually:

ContextFact {
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
Who is authoritative for it?

⸻

20. Context Assembly

Context should be assembled from relevant sources.

Conceptually:

Intent
   │
   ▼
Required Context
   │
   ├── Identity
   ├── Enterprise Data
   ├── Permissions
   ├── Evidence
   ├── Temporal State
   └── Execution State
            │
            ▼
         Context

Context assembly should be driven by the requirements of the Action and Policy.

⸻

21. Context Should Be Minimal

Noema should prefer:

minimum sufficient context

over:

maximum available context

This reduces:

privacy exposure
security risk
reasoning complexity
latency
token usage
data leakage

Context minimization is therefore both a security and execution principle.

⸻

22. Context Expansion

Context may expand during execution when new information becomes necessary.

Example:

Initial Context
    ↓
customer_id
Need account
    ↓
account_id
Need statement
    ↓
statement period

Context should grow based on actual execution requirements rather than being fully populated upfront.

⸻

23. Context Reduction

Information that is no longer required may be removed or excluded from downstream Actions.

For example:

Identity Resolution
    ↓
customer_id established

An internal identity-resolution artifact may not need to be passed to every subsequent enterprise capability.

Context should therefore support controlled propagation.

⸻

24. Context and Data Boundaries

Context must respect enterprise Data Boundaries.

For example:

Customer Account Inquiry
        ↓
Account Data

does not automatically authorize access to:

internal fraud models
employee records
other customers
restricted operational data

Context assembly must respect:

tenant boundaries
organizational boundaries
legal boundaries
permission boundaries
purpose boundaries

⸻

25. Context and Data Minimization

For:

get_account_balance

the required Context may be:

principal_id
account_id
authorization_context

For:

search_transactions

it may additionally require:

date_range
filters

For:

create_complaint

it may require:

customer_id
complaint_description
related_resource

The Context schema therefore depends on the Action.

⸻

26. Context and Action Selection

Context can determine which Actions are available or appropriate.

Example:

Intent:
"How much did I spend last month?"

Context establishes:

principal = customer
account = 123
period = previous calendar month

This supports:

get_spending_summary

rather than:

search_transactions

alone, when the resolved Intent requires an aggregate result.

⸻

27. Context and Planning

Planning uses Context to determine Action dependencies.

Example:

Context:
customer_id = 123
account_id = unknown
period = 2026-08

The plan may require:

resolve account
      ↓
search transactions
      ↓
get spending summary

Context therefore evolves alongside the execution plan.

⸻

28. Context and Preconditions

Preconditions consume Context.

Example:

Precondition:
Principal authorized for Account

requires:

principal_id
account_id
authorization information

If required Context is missing:

Precondition
      ↓
Cannot evaluate
      ↓
Execution blocked

Missing information is not equivalent to a satisfied Precondition.

⸻

29. Context and Postconditions

Postcondition verification may update Context.

Example:

create_complaint
      ↓
case_id
      ↓
verification
      ↓
case.status

The resulting information may become part of the execution Context and Evidence.

⸻

30. Context and Trust

Trust evaluates the quality and sufficiency of information available in Context.

For example:

Context
   ├── canonical account
   ├── authenticated principal
   ├── authorization evidence
   └── temporal information
             │
             ▼
           Trust

If Context contains unresolved ambiguity:

Trust
   ↓
Insufficient
   ↓
Clarify / Escalate

Trust must not manufacture certainty from incomplete Context.

⸻

31. Context and Model Output

The model may contribute information to Context.

Examples:

interpreted intent
extracted merchant
extracted date range
candidate account
candidate Action

These values must retain their semantic classification.

For example:

model_candidate_account

must not silently become:

canonical_account_id

without the appropriate grounding.

⸻

32. Context and User Input

User-provided information can be part of Context.

Example:

"I made a payment to Netflix yesterday."

The phrase may produce:

merchant = Netflix
date = yesterday

These are inputs or interpretations.

They are not automatically canonical enterprise facts.

Where necessary, they must be validated against enterprise data.

⸻

33. Context and Derived Data

Context may contain derived information.

Example:

spending_last_month = ₦450,000

If calculated from transactions, this should be classified as derived.

Noema must preserve the distinction between:

canonical transaction

and:

derived spending summary

⸻

34. Context and Multiple Sources

Context may contain information from several systems.

Example:

Identity System
      ↓
principal_id
Account System
      ↓
account_id
Ledger
      ↓
balance
Transaction System
      ↓
transactions
Support System
      ↓
existing cases

Noema must preserve the authority and provenance of each source.

Agreement between sources does not automatically establish authority.

⸻

35. Context Conflicts

Context may contain conflicting information.

Example:

Account System:
account status = ACTIVE
Projection:
account status = CLOSED

Noema should not resolve this conflict through model preference.

Instead:

Conflict
   ↓
Authority Resolution
   ↓
Trust / Policy
   ↓
Continue / Clarify / Escalate / Reject

⸻

36. Context Unavailability

Required Context may be unavailable.

Example:

Ledger unavailable

If the Action requires current authoritative balance:

Context incomplete
       ↓
Trust / Policy
       ↓
Retry / Clarify / Escalate / Reject

A missing authoritative fact should not silently be replaced with an uncertain value when Policy prohibits it.

⸻

37. Context and Read Operations

The initial Customer Account Inquiry workflow is primarily read-oriented.

Typical Context requirements are therefore:

identity
resource
scope
filters
time
authorization

The workflow does not require unrestricted mutation Context.

⸻

38. Context and Complaint Logging

create_complaint is the principal support-state-changing Action in the workflow.

Its Context may include:

customer_id
complaint_description
related_transaction
related_account
previous relevant interaction

Only the relevant information should be passed to the Support System.

Noema should not attach the customer’s entire Context to a complaint automatically.

⸻

39. Context and Compound Intent

A Customer may issue:

"Show me what I spent last month and open a complaint about the Netflix transaction."

This may produce multiple Context requirements:

customer identity
account
period
transaction
merchant
complaint description

The Context must remain partitionable by Action.

Conceptually:

Compound Intent
       ↓
Action A Context
       +
Action B Context

Not every Action receives every Context field.

⸻

40. Context Partitioning

Context should be partitioned according to execution boundaries.

Example:

Global Execution Context
        │
        ├── Identity Context
        ├── Account Context
        ├── Transaction Context
        └── Support Context

An enterprise integration should receive only the portion required for its Action.

⸻

41. Context and External Integrations

Integrations translate Noema Context into enterprise-specific requests.

Conceptually:

Noema Context
      ↓
Action Contract
      ↓
Integration
      ↓
Enterprise API

The Integration should not be responsible for inventing missing Context.

If required information is absent, execution should stop according to Policy.

⸻

42. Context and Execution State

Context may track the current execution position.

Example:

Action:
search_transactions
State:
EXECUTING

After execution:

Action:
search_transactions
State:
SUCCEEDED

Execution state belongs to Noema.

Transaction state belongs to the enterprise.

⸻

43. Context and Recovery

When execution fails, sufficient Context should be retained to determine whether recovery is possible.

Example:

Action:
retrieve_statement
Failure:
timeout

Recovery may require:

action_id
statement_id
account_id
request_id
attempt

Context should therefore support controlled recovery without requiring reconstruction from model memory.

⸻

44. Context and Idempotency

For Actions that can create state, Context may contain an idempotency key.

Example:

create_complaint
      ↓
idempotency_key

The key should be stable across retries of the same logical Action execution.

Noema should distinguish:

new execution

from:

retry of existing execution

⸻

45. Context and Auditability

For consequential execution, the execution record should preserve the relevant Context snapshot or sufficient references to reconstruct it.

This should allow Noema to answer:

What did Noema know?
When did it know it?
Where did the information come from?
What Action did it enable?
What Policy applied?

The objective is not to retain every piece of available data.

It is to retain enough information to reconstruct the decision and execution path.

⸻

46. Context Lifecycle

Context evolves through the execution lifecycle.

REQUEST
   ↓
INITIAL CONTEXT
   ↓
IDENTITY RESOLUTION
   ↓
ENRICHED CONTEXT
   ↓
TRUST
   ↓
ACTION
   ↓
EXECUTION EVIDENCE
   ↓
UPDATED CONTEXT
   ↓
POSTCONDITION
   ↓
FINAL CONTEXT

Context is therefore dynamic.

It is not necessarily a single immutable object created at request time.

⸻

47. Context Snapshot

At important execution boundaries, Noema may create a Context Snapshot.

Examples:

pre-trust snapshot
pre-action snapshot
post-action snapshot
postcondition snapshot

Snapshots support:

audit
debugging
recovery
reconstruction

The exact persistence strategy is an implementation concern.

⸻

48. Context Freshness

Context facts may expire.

For example:

balance observed at 09:00

may no longer satisfy a requirement at:

09:30

if the Action requires current state.

Freshness requirements therefore belong to the relevant Action and Policy.

⸻

49. Context Expiration

Context should support explicit expiration semantics where required.

Conceptually:

ContextFact {
    value
    observed_at
    expires_at
}

Not every Context fact requires an expiration time.

Only facts whose validity changes materially over time need explicit freshness handling.

⸻

50. Context and Environment

Context must preserve environment boundaries.

For example:

environment = production

must not be silently mixed with:

environment = staging

A production Action must never be satisfied using staging Context merely because the values appear plausible.

⸻

51. Context and Tenancy

Context must preserve tenant boundaries.

Example:

tenant = A
account_id = 123

must remain distinct from:

tenant = B
account_id = 123

The identifier alone is insufficient.

Tenant identity is part of the execution boundary.

⸻

52. Context and Organizational Boundaries

Where an enterprise contains multiple organizational units, Context should preserve relevant organizational scope.

For example:

organization
business_unit
legal_entity

may affect:

resource visibility
authorization
policy
available Actions

Context must not collapse these boundaries.

⸻

53. Context Model

Conceptually:

Context {
    execution_id
    principal
    tenant
    organization
    intent
    resources
    canonical_data
    evidence
    derived_data
    permissions
    temporal_state
    policy
    trust_state
    execution_state
    provenance
}

This is a semantic model rather than a requirement for a literal database schema.

⸻

54. Context Relationships

Context
   │
   ├── contains → Intent
   ├── contains → Principal
   ├── contains → Resource References
   ├── contains → Canonical Data
   ├── contains → Evidence
   ├── contains → Derived Data
   ├── contains → Permissions
   ├── contains → Temporal State
   ├── contains → Trust State
   └── contains → Execution State

These relationships do not imply equal authority among the contained information.

⸻

55. Context Invariants

Invariant 1

Context must be scoped to an execution journey.

Invariant 2

Context must not be treated as inherently authoritative.

Invariant 3

Canonical Data retains its authority independently of Context.

Invariant 4

Evidence retains its provenance independently of Context.

Invariant 5

Model-generated information must retain its classification as interpretation or hypothesis until grounded.

Invariant 6

User-provided information must not automatically become canonical enterprise data.

Invariant 7

Context must contain the minimum information necessary for the relevant execution.

Invariant 8

Context must respect enterprise data, tenant, organizational, legal, and permission boundaries.

Invariant 9

Resource identifiers must retain sufficient scope to prevent accidental cross-resource execution.

Invariant 10

Missing required Context must not be treated as a satisfied Precondition.

Invariant 11

Ambiguous Context must not be resolved through probabilistic guessing when Policy requires deterministic resolution.

Invariant 12

Context freshness must be considered when freshness affects the Action.

Invariant 13

Authority and freshness are independent properties of Context data.

Invariant 14

Context may contain information from multiple sources without making those sources equally authoritative.

Invariant 15

Conflicting Context must be resolved according to authority and Policy rather than model preference.

Invariant 16

Noema must not create competing canonical Business State merely by maintaining Context.

Invariant 17

Context passed to an enterprise integration must be limited to the data required by the Action.

Invariant 18

Context must preserve sufficient provenance for consequential decisions.

Invariant 19

Context must preserve the distinction between enterprise Business State and Noema Execution State.

Invariant 20

Context must support deterministic reconstruction of relevant execution decisions where required.

Invariant 21

Context should evolve as execution requirements change rather than being populated indiscriminately.

Invariant 22

Context must not silently cross environment boundaries.

Invariant 23

Context must not silently cross tenant or organizational boundaries.

Invariant 24

Context associated with a retry must preserve the identity of the original logical Action execution.

Invariant 25

Context is an execution resource, not a substitute for enterprise authority.

⸻

56. Final Definition

Context is the minimum sufficient, structured information available to Noema during an execution journey.

For the Customer Account Inquiry workflow:

PRINCIPAL
    │
    ▼
INTENT
    │
    ▼
CONTEXT
    │
    ├── Identity
    ├── Resource
    ├── Canonical Data
    ├── Evidence
    ├── Permissions
    ├── Temporal State
    └── Execution State
    │
    ▼
TRUST + POLICY
    │
    ▼
ACTION
    │
    ▼
ENTERPRISE SYSTEM
    │
    ▼
OUTCOME

And the architectural rule is:

Noema should know enough to execute safely, but never assume that everything it knows is true, authoritative, or necessary.