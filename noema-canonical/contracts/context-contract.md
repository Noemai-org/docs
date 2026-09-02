Context Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/context-contract.md

⸻

1. Definition

A Context Contract defines the information Noema is permitted to use, required to obtain, and expected to preserve when resolving Intent, evaluating Trust, planning Actions, and executing an enterprise workflow.

A Context Contract answers:

“What information is required for this decision, where may it come from, how authoritative is it, and under what conditions may it be used?”

Context is not simply a collection of data.

It is bounded information with explicit:

source
authority
scope
purpose
freshness
provenance
access constraints
confidence
temporal validity

The Contract establishes the boundary between available information and information that is safe and valid to use for a particular decision.

⸻

2. Purpose

The purpose of the Context Contract is to prevent Noema from treating every available piece of information as equally valid for every execution.

Enterprise environments may expose:

canonical data
cached data
derived data
historical data
events
user-provided information
external information
model-generated interpretations

The Context Contract establishes which of these may participate in a particular decision.

Conceptually:

Available Information
        ↓
Context Contract
        ↓
Permitted Context
        ↓
Evidence
        ↓
Trust
        ↓
Action

⸻

3. Core Principle

Context is purpose-bound.

Information being available does not mean it is valid for every decision.

For example:

Customer Name

may be sufficient to display an account profile.

It may be insufficient to authorize:

financial operation

Similarly:

cached account balance

may be acceptable for:

informational response

but not for:

high-risk financial execution

The required Context depends on the Action and Policy.

⸻

4. Context vs Data

Data is information.

Context is information selected and structured for a specific decision or execution.

Therefore:

Data
   ↓
Selection
   ↓
Validation
   ↓
Context

Context carries semantics that raw data does not necessarily have.

For example:

balance = 5000

is data.

balance = 5000
source = ledger
observed_at = T
authority = canonical
purpose = transfer_precondition

is execution-relevant Context.

⸻

5. Context vs Canonical Data

Canonical Data is authoritative information within a defined authority boundary.

Context is information available to Noema for a specific decision.

Therefore:

Canonical Data
      ↓
    Context

but:

Context ≠ Canonical Data

Context may contain canonical data as well as:

evidence
history
user input
derived values
workflow state
environment information

Noema must preserve the distinction.

⸻

6. Context vs Evidence

Context is the information available for reasoning.

Evidence establishes support for a proposition.

Example:

Context:
account_id = ACC-123
Evidence:
Ledger confirms ACC-123 belongs to Customer-456.

Context may contain information that has not yet been sufficiently validated to become Evidence.

Therefore:

Context
   ↓
Validation / Observation
   ↓
Evidence

⸻

7. Context vs Intent

Intent expresses what the Principal wants to accomplish.

Context provides information required to interpret that Intent.

Example:

Intent:
"Show me my balance."
Context:
Principal = Customer-456
Account relationship = ACC-123

Conceptually:

Intent + Context
       ↓
Resolved Intent

Context should help resolve Intent without silently changing its meaning.

⸻

8. Context vs Business State

Business State belongs to the enterprise domain.

Context is Noema’s representation of information about that state.

Example:

Enterprise:
Account.balance = $5,000
Noema Context:
observed balance = $5,000

The Context does not become a competing authoritative account balance.

⸻

9. Context vs Noema State

Noema may maintain its own execution state.

Examples:

intent.status
trust.status
execution.status
intervention.status

These are Noema state.

Context may reference them when relevant, but they should remain conceptually distinct.

Context
   +
Noema State
   ↓
Execution Decision

⸻

10. Context Scope

Every Context Contract should define the scope of the Context.

Possible dimensions include:

Principal
Tenant
Organization
Resource
Action
Intent
Workflow
Environment
Time

Context must not leak across these boundaries implicitly.

⸻

11. Principal Context

Context may contain information about the Principal.

Example:

Principal:
customer_id = C-123
authentication_status = authenticated
session_id = S-456

Only information necessary for the current workflow should be included.

⸻

12. Resource Context

Context may contain information about the Resource targeted by an Action.

Example:

Resource:
Account
account_id = A-123
status = ACTIVE

Resource Context should identify the source and authority of consequential attributes.

⸻

13. Organizational Context

Enterprise decisions may depend on organizational boundaries.

Example:

tenant = T-1
organization = O-12
business_unit = BU-4

Context must preserve these boundaries when they affect authorization or execution.

⸻

14. Temporal Context

Context is time-dependent.

Example:

Account Status:
ACTIVE
observed_at:
2026-08-22T12:00:00Z

A later state may be different.

Therefore Context should preserve temporal information where the decision depends on state at a particular point in time.

⸻

15. Source

Every consequential Context item should identify its source.

Example:

balance:
5000
source:
ledger-api

Possible sources include:

enterprise API
database
event
user input
human operator
configuration
external service

Source establishes provenance, not necessarily authority.

⸻

16. Authority

Context should distinguish source from authority.

Example:

Source:
analytics-db
Authority:
ledger

A source may provide useful information without being authoritative for the fact being represented.

⸻

17. Freshness

Context may become stale.

The Contract should define freshness requirements where relevant.

Example:

Context:
balance = $5,000
observed_at:
10:00
Action:
transfer money
Required freshness:
≤ 30 seconds

If the Context is too old:

STALE_CONTEXT

Noema should retrieve fresh information or enter an appropriate deterministic state.

⸻

18. Freshness Is Action-Specific

The same Context may be acceptable for one Action and unacceptable for another.

Example:

get_balance
→ 5-minute-old balance may be acceptable
financial_write
→ current authoritative balance required

Freshness must therefore be evaluated against the Action and Policy.

⸻

19. Provenance

Context should preserve enough provenance to explain where the information came from.

Conceptually:

ContextItem {
    value
    source
    authority
    observed_at
    effective_at
    version
    provenance
}

This supports:

auditability
trust evaluation
reconciliation
debugging
historical reconstruction

⸻

20. Context Lineage

Noema should be able to establish how a Context value was produced.

Example:

Ledger API
    ↓
Raw Response
    ↓
Normalization
    ↓
Context
    ↓
Evidence

If a derived Context value is used:

Transactions
    ↓
Aggregation
    ↓
spending_summary

the derivation should remain traceable.

⸻

21. Derived Context

Context may contain derived values.

Example:

transactions:
[...]
derived:
monthly_spend = $2,450

Derived Context must be explicitly identified.

It must not silently be treated as canonical enterprise state.

⸻

22. Inferred Context

The model may infer information.

Example:

User:
"Show me what I spent last month."
Model interpretation:
period = previous calendar month

This is an interpretation.

It should remain distinguishable from authoritative enterprise data.

Inference
   ↓
Context Candidate
   ↓
Validation
   ↓
Executable Context

⸻

23. User-Provided Context

User input may become Context.

Example:

User:
"My account number is A-123."

The value can be captured as Context.

For consequential operations, it may require verification.

User Input
   ↓
Context
   ↓
Enterprise Verification
   ↓
Evidence

⸻

24. Human-Provided Context

A human operator may supply Context.

Example:

Support Agent:
Customer identity verified.

The Contract should establish:

who supplied it
when
under what authority
for what purpose

Human-provided information is not automatically canonical.

⸻

25. Event Context

Events may provide Context.

Example:

account.balance.changed

The event may indicate that state changed.

However:

event ≠ necessarily current canonical state

The Contract must define whether an event is sufficient for the relevant decision or whether authoritative verification is required.

⸻

26. Historical Context

Some decisions depend on historical state.

Example:

At T1:
customer had account A-123

Current Context may show:

account A-123
status = CLOSED

Historical execution may still require the earlier relationship.

The Contract should specify when historical Context may be used.

⸻

27. Context Validity

Context may have a validity interval.

Conceptually:

valid_from
valid_until

This is useful for:

authorization
account state
policy versions
identity relationships
workflow state

Expired Context should not be silently reused.

⸻

28. Context Version

Where the underlying source supports versions, Context should preserve them.

Example:

account_version = 42

This allows Noema to determine whether the Context used for execution corresponds to the expected enterprise state.

⸻

29. Context Requirements

A Context Contract should specify required Context.

Example:

Action:
account.balance.read
Required Context:
principal_id
account_id
tenant_id

Optional Context may include:

locale
preferred_currency
display_preferences

Required and optional Context should remain explicit.

⸻

30. Context Sufficiency

Having Context does not mean having sufficient Context.

Example:

Context:
customer_name = John

may be insufficient to resolve:

which John?

Therefore:

Context
   ↓
Sufficiency Check
   ↓
SUFFICIENT / INSUFFICIENT

If insufficient:

CLARIFY

or another deterministic intervention may be required.

⸻

31. Context Completeness

The Contract should define the information required for the relevant decision.

Example:

Complaint Creation
Required:
customer_id
transaction_id
complaint_type
description

Missing required Context should prevent execution.

Missing Context
      ↓
Trust
      ↓
CLARIFY / ESCALATE

⸻

32. Context Ambiguity

Context can itself be ambiguous.

Example:

account:
A-123
A-456

Both may belong to the same Principal.

Noema must not arbitrarily choose one.

Ambiguous Context
       ↓
Deterministic Resolution
       ↓
Clarification / Confirmation

This follows the core Noema principle:

Ambiguity is a state, not an invitation to guess.

⸻

33. Context Conflicts

Two Context sources may disagree.

Example:

CRM:
customer status = ACTIVE
Identity System:
customer status = SUSPENDED

Noema must determine whether:

different definitions
different authority
stale information
replication lag
actual conflict

If authority cannot be established:

CONFLICT

must remain an explicit state.

⸻

34. Context Priority

Context items should not be prioritized merely by:

recency
source count
model confidence

Authority and Policy determine which information is appropriate.

Example:

Ledger
balance = $10,000
Cache
balance = $10,500

The cache being newer does not automatically make it authoritative.

⸻

35. Context Selection

Noema should select only the Context necessary for the current Intent and Action.

Conceptually:

Available Enterprise Information
            ↓
      Context Contract
            ↓
     Relevant Context
            ↓
        Evidence

This limits unnecessary data access.

⸻

36. Data Minimization

The Contract should enforce data minimization.

Example:

Action:
get_account_balance
Required:
account_id

There is no reason to retrieve:

home_address
full_profile
unrelated_transactions

unless another explicit requirement exists.

⸻

37. Purpose Limitation

Context should only be used for the purpose for which it was collected or authorized.

Example:

Identity Context

may establish who the Principal is.

It should not automatically be repurposed to:

infer financial risk

unless permitted by the relevant enterprise Policy.

⸻

38. Permissions

Access to Context must respect Permissions.

A Principal may be authorized to:

view account balance

without being authorized to:

view account owner's full identity profile

Context access must therefore remain field- and purpose-aware where required.

⸻

39. Context and Privacy

Context may contain sensitive enterprise information.

The Contract should define appropriate:

access
redaction
retention
field minimization
purpose restrictions

Noema should not expose Context merely because it was retrieved internally.

⸻

40. Context Retention

Not all Context should be retained indefinitely.

The Contract may define:

retention period
retention purpose
deletion requirements
audit requirements

For example:

temporary Context
→ execution lifetime
audit Context
→ retained according to audit policy

⸻

41. Context and Trust

Trust evaluates whether Context is sufficient and trustworthy for the intended Action.

Context
   ↓
Evidence
   ↓
Trust

Trust may evaluate:

authority
freshness
completeness
consistency
provenance
permissions
scope

The Context Contract defines what information Trust needs.

⸻

42. Context and Preconditions

Preconditions consume Context.

Example:

Precondition:
principal owns account

Required Context:

principal_id
account_id
tenant_id

Required Evidence:

enterprise ownership relationship

The Context Contract therefore supports deterministic precondition evaluation.

⸻

43. Context and Postconditions

Postconditions may require Context from after execution.

Example:

Action:
create_complaint
Postcondition:
complaint exists

Noema may retrieve:

case_id
status
created_at

as post-execution Context for verification.

⸻

44. Context and Planning

Planning uses Context to determine which Actions are applicable.

Example:

Intent:
"Show my transactions."
Context:
account_id = A-123

The planner can select:

transaction.search

Without sufficient Context:

account_id = unknown

the planner may need an identity-resolution step before selecting the final Action.

⸻

45. Context and Execution

Execution consumes the Context defined by the Action Contract.

Context Contract
      ↓
Context
      ↓
Action Contract
      ↓
Execution

Execution should not silently acquire unrelated Context outside the defined boundary.

⸻

46. Context and Integration

Integrations provide many of the sources from which Context is constructed.

Enterprise Integration
       ↓
Source Data
       ↓
Context Construction
       ↓
Context Contract

The Integration Model describes how data is accessed.

The Context Contract describes how that information may participate in Noema’s decision process.

⸻

47. Context and Events

Events can update Context.

Example:

transaction.completed
       ↓
Context Update

However, an event-derived Context value must preserve:

event_id
source
occurred_at
received_at

where necessary.

⸻

48. Context and Temporal State

Context may represent state at different times.

observed_at
effective_at
received_at

These timestamps have different meanings.

For example:

Event occurred:
10:00
Noema received:
10:03

The Context should not confuse receipt time with business-effective time.

⸻

49. Context and Staleness

Context may become stale during an execution.

Example:

Context acquired:
10:00
Execution:
10:10

If the Action requires current state, the Context may no longer satisfy the Contract.

Noema should revalidate or reacquire the relevant Context.

⸻

50. Context Refresh

The Contract may define refresh behavior.

Example:

if balance_context_age > 30 seconds:
    refresh from ledger

Refresh should be deterministic.

The model should not decide arbitrarily when Context is “fresh enough.”

⸻

51. Context Snapshot

For deterministic execution, Noema may create a Context snapshot.

Conceptually:

Context Snapshot
    │
    ├── Principal
    ├── Intent
    ├── Resources
    ├── Evidence
    ├── Policy Version
    └── Relevant Enterprise State

The snapshot can support:

audit
replay
debugging
reconciliation

⸻

52. Context Immutability

Context used for a consequential decision should be immutable for that decision once Trust evaluation begins.

Context Snapshot
       ↓
Trust
       ↓
Decision

If relevant Context changes:

Context Changed
       ↓
Decision Invalidated
       ↓
Re-evaluate

This prevents hidden state changes during execution.

⸻

53. Context Mutation

Context may evolve during a workflow.

For example:

Initial Context
      ↓
Identity resolved
      ↓
Account resolved
      ↓
Balance retrieved

Each update should be explicit and traceable.

Noema should not silently mutate decision-critical Context.

⸻

54. Context Isolation

Context belonging to one execution must not automatically become Context for another.

Example:

Execution A
Customer A
Account A
Execution B
Customer B
Account B

Noema must prevent accidental Context leakage between executions.

⸻

55. Tenant Isolation

Context must preserve tenant boundaries.

Tenant A
   ↓
Context A
Tenant B
   ↓
Context B

Context from Tenant A must never satisfy a Contract for Tenant B unless explicitly permitted by enterprise architecture and Policy.

⸻

56. Environment Isolation

Similarly:

Production Context

must not satisfy:

Staging Action

or vice versa.

Environment is part of Context scope.

⸻

57. Context Security

Context should be treated as security-sensitive execution material.

The Contract must control:

who can access it
which fields are available
how long it persists
which Actions may consume it

Context is therefore part of Noema’s security boundary.

⸻

58. Context Integrity

Noema must protect decision-critical Context against unauthorized modification.

Conceptually:

Source
   ↓
Validated Context
   ↓
Integrity Protection
   ↓
Trust

A model-generated modification must not silently overwrite authoritative Context.

⸻

59. Context and Model Output

Model output may contribute to Context.

Example:

Model:
"last month" = 2026-07-01 → 2026-07-31

This is an interpretation.

It should be represented as:

Context Item:
type = inferred
source = model

and grounded according to the risk and requirements of the Action.

⸻

60. Context and Model Confidence

Model confidence does not establish Context validity.

For example:

Model confidence:
98%
Candidate account:
A-123

does not mean:

Canonical account:
A-123

Trust must evaluate the appropriate enterprise evidence.

⸻

61. Context and Clarification

When Context is insufficient or ambiguous:

Context
   ↓
Sufficiency Check
   ↓
INSUFFICIENT
   ↓
CLARIFY

Clarification becomes part of the execution state.

Noema should not manufacture missing Context.

⸻

62. Context and Escalation

Some Context gaps cannot be resolved automatically.

Example:

Two accounts
same customer
same name
no distinguishing information

If the Action is consequential:

Ambiguity
   ↓
Human Escalation

The Contract should define when this is appropriate.

⸻

63. Context and Unknown State

Context may be unavailable.

Example:

Ledger unavailable

Noema should represent:

Context Unavailable

rather than silently replacing it with an unsupported assumption.

The resulting Trust state may be:

RETRY
CLARIFY
ESCALATE
REJECT

depending on Policy.

⸻

64. Context Conflict Resolution

Noema should resolve Context conflicts through deterministic authority and Policy.

Not:

Source A says X
Source B says Y
Model thinks X is more likely

but:

Authority
   ↓
Policy
   ↓
Resolution

If no deterministic resolution exists:

CONFLICT

must remain explicit.

⸻

65. Context Contract and Action Contract

The two Contracts are complementary.

Context Contract
      ↓
What information is valid and available?
Action Contract
      ↓
What information and conditions are required to execute?

Together:

Context Contract
        +
Action Contract
        ↓
Trust
        ↓
Execution

⸻

66. Context Contract and Evidence Contract

The Context Contract determines what information may participate in a decision.

Evidence semantics determine what observations establish propositions.

Context
   ↓
Observation
   ↓
Evidence

Context should therefore preserve sufficient provenance for Evidence construction.

⸻

67. Context Contract and Policy

Policy may impose additional Context requirements.

Example:

Action:
complaint.create
Base Context:
transaction_id
Policy:
complaints above threshold require transaction amount and account status.

Therefore:

Action Contract
      +
Policy
      ↓
Required Context

⸻

68. Context Contract and Auditability

For consequential decisions, Noema should preserve the relevant Context snapshot or sufficient references to reconstruct it.

Audit should establish:

what Context existed
when it was observed
where it came from
which Contract required it
which Policy applied
which Trust decision consumed it

⸻

69. Context Contract and Reproducibility

A decision should be reproducible to the extent required by its risk and audit requirements.

Conceptually:

Intent
+
Context Snapshot
+
Evidence
+
Policy Version
+
Action Contract Version
      ↓
Trust Decision

This is substantially stronger than relying on an opaque model conversation history.

⸻

70. Context Contract and Recovery

Recovery may require Context that existed before failure.

Example:

Execution:
UNKNOWN

To reconcile it, Noema may need:

idempotency_key
target
principal
Action
execution timestamp

The Context Contract should define which information must survive long enough to support recovery.

⸻

71. Context Contract and Customer Account Inquiry

The Customer Account Inquiry reference workflow may require Context such as:

principal_id
tenant_id
account_id
requested_period
transaction_filters

The exact Context depends on the selected Action.

Example:

"Show my balance."
Required:
principal_id
account_id
"Show my transactions from last month."
Required:
principal_id
account_id
start_date
end_date

⸻

72. Context Contract Example

Conceptually:

ContextContract {
    context_id
    version
    purpose
    scope
    required {
        principal_id
        tenant_id
        resource_id
    }
    optional {
        locale
        time_zone
    }
    source_requirements {
        resource_id:
            authoritative_identity_source
    }
    freshness_requirements {
        balance:
            action_specific
    }
    provenance:
        required
    retention:
        execution_lifetime
}

This is a semantic model rather than a requirement for a literal database table.

⸻

73. Context Item Model

Conceptually:

ContextItem {
    key
    value
    type
    source
    authority
    scope
    purpose
    observed_at
    effective_at
    expires_at
    version
    provenance
    classification
    sensitivity
}

Possible classifications include:

canonical
observed
derived
inferred
user_provided
historical
cached
event_derived

⸻

74. Context Relationships

Context
   │
   ├── references → Principal
   ├── references → Resource
   ├── derived_from → Data
   ├── sourced_from → Integration
   ├── supports → Evidence
   ├── constrains → Intent
   ├── satisfies → Preconditions
   ├── informs → Planning
   ├── consumed_by → Trust
   └── consumed_by → Execution

⸻

75. Context Lifecycle

Context may move through:

DISCOVERED
    ↓
COLLECTED
    ↓
VALIDATED
    ↓
AVAILABLE
    ↓
CONSUMED
    ↓
EXPIRED

Context that becomes invalid should not remain silently usable.

⸻

76. Context Invalidity

Context may become invalid because of:

expiration
source revocation
resource state change
permission change
tenant change
environment change
version mismatch
conflict
integrity failure

Invalid Context should trigger re-evaluation where required.

⸻

77. Context Contract Invariants

Invariant 1

Context must have a defined purpose and scope.

Invariant 2

Available data is not automatically valid Context.

Invariant 3

Context must remain distinct from Canonical Data.

Invariant 4

Context must remain distinct from Evidence.

Invariant 5

Context must preserve source and authority semantics where consequential.

Invariant 6

Authority must not be inferred merely from source availability or recency.

Invariant 7

Context requirements must be Action- and Policy-aware.

Invariant 8

Required Context must be explicit.

Invariant 9

Missing required Context must prevent unsafe execution.

Invariant 10

Ambiguous Context must not be resolved through probabilistic guessing when ambiguity is material.

Invariant 11

Model-generated Context must remain distinguishable from authoritative enterprise information.

Invariant 12

User-provided Context must not automatically become canonical.

Invariant 13

Derived Context must preserve its derivation semantics.

Invariant 14

Context must preserve relevant temporal information.

Invariant 15

Freshness requirements must be explicit where decision correctness depends on current state.

Invariant 16

Stale Context must not satisfy a requirement that demands fresher information.

Invariant 17

Context must respect tenant, organizational, legal, and environment boundaries.

Invariant 18

Context access must respect Permissions.

Invariant 19

Context collection must follow least-privilege and data-minimization principles.

Invariant 20

Context must not be reused for unrelated purposes without authorization.

Invariant 21

Decision-critical Context should be immutable for the duration of the decision.

Invariant 22

Changes to decision-critical Context must invalidate or trigger re-evaluation of affected decisions.

Invariant 23

Context belonging to one execution must not leak into another execution.

Invariant 24

Event-derived Context must preserve appropriate event provenance and temporal semantics.

Invariant 25

Context conflicts must be resolved through authority and Policy, not model preference.

Invariant 26

If authoritative Context is unavailable, Noema must preserve the unavailable state rather than manufacture a substitute.

Invariant 27

Consequential execution must have sufficient Context to establish its Preconditions.

Invariant 28

Context required for recovery and reconciliation must be retained according to Policy.

Invariant 29

Context used for consequential decisions must be sufficiently reconstructable for audit.

Invariant 30

The Context Contract defines what information may participate in a decision; it does not redefine enterprise Business State.

⸻

78. Final Definition

A Context Contract is the authoritative specification of the information required, permitted, and trusted for a particular Noema decision or execution.

It establishes:

WHAT
information is required
WHERE
that information may come from
WHICH
source and authority semantics apply
HOW
fresh the information must be
WHAT
scope and purpose govern its use
HOW
its provenance is preserved
WHICH
data may be derived or inferred
WHEN
the Context becomes invalid
HOW
ambiguity and conflict are handled

The fundamental relationship is:

ENTERPRISE INFORMATION
        │
        ▼
CONTEXT CONTRACT
        │
        ▼
     CONTEXT
        │
        ├── SOURCE
        ├── AUTHORITY
        ├── SCOPE
        ├── PURPOSE
        ├── FRESHNESS
        ├── PROVENANCE
        └── TEMPORAL VALIDITY
                │
                ▼
             EVIDENCE
                │
                ▼
              TRUST
                │
                ▼
             ACTION
                │
                ▼
           EXECUTION

And the architectural rule is:

Noema must never treat available information as automatically valid execution Context. Context is bounded by purpose, authority, scope, freshness, provenance, permissions, and Policy.