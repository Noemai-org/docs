Canonical Data

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/canonical-data.md

⸻

1. Definition

Canonical Data is the authoritative representation of an enterprise fact, entity, resource, relationship, or state within a defined authority boundary.

Canonical Data answers:

What does the authoritative enterprise source establish about this fact, resource, or state within the applicable scope and time?

For Noema, this distinction is fundamental because Noema operates on enterprise data without necessarily owning it.

Enterprise System
      │
      ▼
Canonical Data
      │
      ├── State Reconciliation
      ├── Context
      ├── Evidence
      ├── Preconditions
      └── Postconditions
              │
              ▼
            Noema

Noema consumes or observes Canonical Data to establish relevant enterprise state and make execution decisions.

It does not automatically become the owner or authority of that data.

⸻

2. Purpose

The purpose of Canonical Data is to establish a precise distinction between:

* canonical
* derived
* cached
* observed
* inferred
* stale
* historical
* reconciled
* conflicting
* unknown

Enterprise environments commonly contain many representations of the same information.

For example:

Ledger:
balance = $10,000
Cache:
balance = $10,000
Analytics DB:
balance = $10,000
CRM:
balance = $10,000

These values may look identical.

They do not necessarily have equal authority, freshness, scope, or semantic meaning.

⸻

3. Core Principle

Data is canonical only within an explicitly defined authority boundary.

There is no universal concept of:

“the canonical customer data”

without defining:

* which fact
* which domain
* which system
* which authority
* which scope
* which resource
* which time
* which version

For example:

Customer identity
→ Identity System
Account balance
→ Ledger
Payment status
→ Payment System

Canonicality is therefore scoped.

⸻

4. Canonical Data vs System of Record

These concepts are related but different.

System of Record

The authoritative enterprise system responsible for a defined domain of facts or state.

Canonical Data

The authoritative representation of a particular fact, entity, resource, relationship, or state within that authority boundary.

System of Record
      │
      ▼
Canonical Data

A System of Record provides the authority boundary.

Canonical Data is the authoritative information maintained or established within that boundary.

A System of Record may therefore be canonical for some facts while another system remains canonical for different facts.

⸻

5. Canonical Data vs Context

Context is information available to Noema for Intent resolution, Trust evaluation, planning, execution, verification, or explanation.

Canonical Data is authoritative information within a defined enterprise authority boundary.

Therefore:

Context
    may contain
        ↓
Canonical Data

but:

Context ≠ Canonical Data

Context can also contain:

* derived information
* historical information
* external evidence
* user-provided information
* Noema operational information
* model interpretations

These should not automatically be treated as canonical.

The Context Contract defines permitted and required contextual information; it does not itself establish enterprise authority.

⸻

6. Canonical Data vs Evidence

Evidence supports a proposition or records an observation.

Canonical Data represents the authoritative enterprise information underlying that proposition.

Example:

Evidence:
"Ledger reports balance = $5,000"
Canonical Data:
Account.balance = $5,000

The Evidence records how Noema obtained or observed the value.

Canonical Data describes what the authoritative enterprise source establishes.

Evidence is therefore not automatically canonical merely because it references a canonical source.

⸻

7. Canonical Data vs Fact Status

Fact Status describes the semantic status of a claim as established for Noema’s purposes.

Canonical Data describes authoritative enterprise information.

These concepts must remain distinct.

A canonical source may provide information that Noema has:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

depending on what can currently be established about the claim, freshness, reconciliation, and authority.

Therefore:

Canonical Data
      ≠
Fact Status

Fact Status is evaluated for a particular claim in a particular context.

It is not a replacement for enterprise authority.

⸻

8. Canonical Data vs Inference

Inference is not canonical merely because it is highly probable.

For example:

Model inference:
customer probably owns account 123

is not equivalent to:

Canonical relationship:
customer 456 → account 123

The latter must be established by an authoritative enterprise source or explicitly trusted configuration.

Model confidence does not establish canonicality.

⸻

9. Canonical Data vs Cached Data

A cache can contain a copy of canonical data.

But:

cached = canonical

is not a safe assumption.

A cached representation must have explicit semantics concerning:

* source
* authority
* freshness
* version
* expiration
* consistency
* scope
* reconciliation status

A cache may be useful for read-only or low-risk operations while being insufficient for a consequential Action.

⸻

10. Canonicality Is Scoped

Canonicality can be scoped by:

* tenant
* organization
* legal entity
* domain
* resource
* field
* relationship
* environment
* time
* version
* authority boundary

For example:

Account.balance

may be canonical in:

Production Ledger / Tenant A

but not:

Analytics Warehouse / Tenant A

The identifier alone does not establish canonicality.

⸻

11. Canonical Entity

An enterprise Entity may have multiple representations.

Example:

Customer
   │
   ├── CRM representation
   ├── Billing representation
   └── Support representation

One system may be canonical for:

customer identity

while another is canonical for:

billing relationship

Noema must avoid treating all representations as equivalent.

Entity canonicality must be defined at the level necessary to establish the relevant fact.

⸻

12. Canonical Resource

A Resource may have canonical state within a System of Record.

Example:

Payment #123
status   = SUCCEEDED
amount   = $500
currency = USD

The payment system may be canonical for these fields.

Noema can reference these values without owning the enterprise Resource or becoming the enterprise source of truth.

⸻

13. Canonical State

Canonical State is the authoritative state established for a Resource within its applicable enterprise authority boundary.

Example:

Payment
    ↓
status = REFUNDED

If another system reports:

status = SUCCEEDED

Noema must determine whether the discrepancy is caused by:

* replication lag
* eventual consistency
* stale cache
* different state definitions
* different authority scopes
* actual inconsistency
* incomplete observation
* an unresolved transition

Noema must not resolve the conflict through probabilistic preference.

⸻

14. Field-Level Canonicality

Canonicality may exist at the field level.

For example:

Customer
├── name
│   └── CRM
├── credit_limit
│   └── Credit System
└── payment_status
    └── Billing System

Therefore, saying:

CRM is canonical for Customer

may be too coarse.

More precise:

CRM is canonical for Customer.name

The same principle applies to relationships and state attributes.

⸻

15. Canonical Relationships

Relationships can also have authoritative sources.

Example:

Employee
    ↓ belongs_to
Department

The HRIS may be authoritative for this relationship.

Noema should not infer organizational relationships from:

* email domain
* past behavior
* calendar events
* model assumptions

when authoritative enterprise data exists.

A relationship may be canonical even when neither endpoint’s entire representation is canonical in the same system.

⸻

16. Canonical Identifiers

Stable enterprise identifiers should be preferred.

Examples:

customer_id
account_id
employee_id
invoice_id
payment_id
order_id

Noema should preserve these identifiers rather than generating competing enterprise identities unnecessarily.

Noema may maintain its own execution identifiers, but these do not replace enterprise identifiers.

⸻

17. Identity Resolution

Noema may need to resolve:

"John"

to:

employee_id = 4821

This is an Intent-resolution and identity-resolution problem.

The resulting identity must be grounded against canonical enterprise identity data before consequential execution.

If multiple authoritative candidates remain, ambiguity remains unresolved.

⸻

18. Canonical Data and Intent

Intent often references enterprise Resources indirectly.

Example:

"Refund my last payment."

The phrase:

"my last payment"

must ultimately resolve to a specific enterprise Resource.

Conceptually:

Source of Intent
      ↓
Intent
      ↓
Identity / Target Resolution
      ↓
Enterprise Resource
      ↓
Canonical Data

The model may propose a candidate interpretation.

Canonical enterprise data establishes whether the referenced Resource actually exists and satisfies the required identity and scope conditions.

⸻

19. Canonical Data and Preconditions

Preconditions should use authoritative data whenever the fact is consequential.

Example:

Precondition:
account.balance >= $1,000

Noema should evaluate:

Canonical Account Balance

rather than:

Model-estimated balance

or an arbitrary cached balance.

An alternative source may be permitted only where the relevant Action, Policy, and freshness semantics explicitly allow it.

⸻

20. Canonical Data and Postconditions

Postconditions may require verification against Canonical Data.

Example:

Action:
freeze_card
Postcondition:
card.status = FROZEN

Noema should verify the state against the authoritative enterprise source where required.

Action
  ↓
Enterprise System
  ↓
Canonical State
  ↓
Verification
  ↓
Postcondition

An API response alone is not necessarily equivalent to verified enterprise state.

⸻

21. Canonical Data and Trust

Canonicality affects Trust.

Evidence from an authoritative source generally has greater decision relevance than equivalent information from a derived source.

For example:

Ledger:
balance = $10,000

is stronger for a financial decision than:

Analytics DB:
balance = $10,000

assuming the Ledger is authoritative for balance.

However, source authority alone does not eliminate the need to evaluate:

* freshness
* scope
* temporal validity
* integrity
* reconciliation
* permissions
* claim-specific authority

⸻

22. Canonical Data and Determinism

Canonical Data supports deterministic execution.

Instead of:

System A → X
System B → Y
Model → probably X

Noema should establish:

Authority
   ↓
Canonical Data
   ↓
State Reconciliation
   ↓
Fact Status
   ↓
Policy
   ↓
Decision

If canonicality cannot be established for a consequential claim, the uncertainty must remain explicit.

Possible states include:

UNKNOWN
CONFLICTED
UNVERIFIED
STALE

rather than an invented canonical value.

⸻

23. Multiple Sources

Noema may encounter:

Source A → X
Source B → X
Source C → Y

Agreement does not automatically make X canonical.

The question is:

Which source has authority for this fact within this scope?

Authority takes precedence over source count.

Multiple agreeing non-authoritative sources do not collectively become authoritative merely because they agree.

⸻

24. Conflicting Canonical Sources

Two systems should ideally not both claim canonical authority for the same fact within the same scope.

If they do:

System A → $10,000
System B → $8,000

Noema should not resolve the conflict through probabilistic judgment.

The system should enter an explicit conflict state requiring:

* authority resolution
* State Reconciliation
* clarification
* escalation

according to Policy.

If the conflict cannot be deterministically resolved, the relevant Fact Status remains CONFLICTED or UNKNOWN.

⸻

25. Temporal Canonicality

Canonical Data is time-dependent.

Consider:

10:00
balance = $10,000
10:05
balance = $8,000

Both values may have been canonical at different times.

Therefore canonical data may require:

* observed_at
* effective_at
* valid_from
* valid_until
* version

where relevant.

Historical canonicality must not be overwritten merely because a newer value exists.

⸻

26. Historical Canonical Data

Historical execution may depend on data that was canonical at the time.

For example:

At T1:
refund_limit = $5,000
At T2:
refund_limit = $2,500

An audit of an execution at T1 should not reinterpret it solely using today’s value.

Noema must preserve enough provenance and version information to reconstruct the relevant historical context.

⸻

27. Versioned Canonical Data

Some systems expose versioned resources.

Example:

Customer:
version = 42

Noema may use version identifiers to ensure that execution decisions are based on the expected state.

This supports:

* optimistic concurrency
* deterministic validation
* state comparison
* reconciliation
* historical reconstruction

A resource version is not necessarily a contract version and must not be conflated with one.

⸻

28. Freshness

Canonical does not necessarily mean:

currently observed

A canonical system can be temporarily unavailable.

Likewise, a cached copy can be:

recent

without being authoritative.

Therefore:

authority ≠ freshness

Both may matter independently.

Freshness is evaluated against the claim, Action, Policy, and temporal requirements.

⸻

29. Freshness Requirements

Different Actions require different freshness guarantees.

Example:

"Show me my account balance."

may tolerate a small delay.

But:

"Transfer $9,000."

may require current authoritative state.

Freshness requirements should therefore be defined by the relevant Action and Policy.

A value cannot be considered sufficiently fresh merely because it was retrieved recently if the underlying source is stale or non-authoritative.

⸻

30. Canonical Data Availability

If canonical data cannot be retrieved:

Ledger unavailable

Noema should not automatically substitute:

cached balance

for a high-risk transaction.

Instead:

Canonical Data Unavailable
        ↓
State Reconciliation / Trust / Policy
        ↓
Clarify / Retry / Escalate / Reject

The permitted response depends on the Action and Policy.

⸻

31. Canonical Data and Business State

Canonical Data is closely tied to enterprise Business State.

Business Resource
      ↓
Canonical State

Noema may observe, reconcile, and act upon this state.

It should not create a competing authoritative state representation unless explicitly owning that domain.

The enterprise remains the source of truth for enterprise business state.

⸻

32. Canonical Data and Noema State

Noema maintains its own execution-domain state:

* Intent
* Intent version
* Trust Decision
* Action
* Execution
* Execution state
* Outcome
* intervention state
* operational history

These are canonical within Noema’s execution domain.

Therefore:

Enterprise Canonical Data

and:

Noema Canonical Data

can coexist without conflict because they belong to different authority domains.

Noema’s execution-domain authority does not make Noema authoritative for enterprise Business State.

⸻

33. Canonical Data and Execution Truth

Noema can be authoritative for:

execution.status
trust.decision
intervention.status
intent.lifecycle
execution.outcome

while the enterprise remains authoritative for:

account.balance
payment.status
employee.status
inventory.quantity

This maintains the boundary between Noema execution-domain state and enterprise Business State.

An Outcome describing what Noema established about an execution is not automatically a replacement for the underlying enterprise state.

⸻

34. Canonical Data and Data Boundaries

Noema should retrieve only the minimum Canonical Data necessary for an execution.

For example:

Action:
refund payment

may require:

payment_id
payment.status
payment.amount
payment.currency

It may not require:

customer.home_address
full transaction history
unrelated profile information

Canonicality does not imply unrestricted accessibility.

⸻

35. Canonical Data and Permissions

A piece of data can be canonical but inaccessible to a particular principal.

Therefore:

canonical

does not imply:

authorized_to_view

or:

authorized_to_use

Noema must evaluate data access independently.

Enterprise permissions remain authoritative for enterprise access.

Noema must not infer permission from data availability.

⸻

36. Canonical Data and Privacy

Canonical enterprise data may contain sensitive information.

Noema should apply, where applicable:

* least privilege
* field minimization
* purpose limitation
* retention controls
* redaction
* access policies
* tenant isolation
* organizational boundaries

A fact can be canonical and still be prohibited from disclosure or use for a particular Intent.

⸻

37. Canonical Data and Provenance

Consequential data should preserve provenance.

Conceptually:

CanonicalFact {
    subject
    attribute
    value
    source
    authority_scope
    observed_at
    effective_at
    version
    provenance
}

This allows Noema to answer:

Where did this value come from?

and:

Why was this source treated as authoritative for this claim?

⸻

38. Canonical Data and Evidence

A useful relationship is:

Canonical Data
      ↓
Observed / retrieved by Noema
      ↓
Evidence
      ↓
Fact Status
      ↓
Trust Evaluation

The Evidence layer records the observation used by Noema.

Fact Status records what Noema can establish about the relevant claim.

Neither layer should silently replace the enterprise source of truth.

⸻

39. Canonical Data and Events

Events may communicate changes to Canonical Data.

Example:

Ledger
   ↓
account.balance.changed
   ↓
Event Bus
   ↓
Noema

The event can provide evidence of change.

For authoritative verification, Noema may still query the System of Record.

An event’s existence does not automatically establish the current canonical state.

⸻

40. Eventual Consistency

If the enterprise architecture is eventually consistent:

System of Record
      ↓
Event
      ↓
Projection
      ↓
Noema

the projection may temporarily differ from the canonical source.

Noema must know the consistency semantics before relying on that projection for consequential decisions.

State Reconciliation may be required to establish whether the projected state is sufficiently current and authoritative.

⸻

41. Derived Data

Derived data may be extremely useful.

Examples:

customer_risk_score
lifetime_value
fraud_probability
search_rank
aggregated_spend

But derived data should be explicitly classified as:

derived

rather than silently promoted to canonical truth.

A derived value may be authoritative for a particular enterprise decision if the enterprise explicitly defines it as such. In that case, its authority boundary must be explicit.

⸻

42. Model-Generated Data

LLM-generated information is not canonical by default.

Examples:

"User probably means account 123."
"Customer is likely high value."
"This appears to be a refund request."

These are interpretations or hypotheses.

They may contribute to candidate Intent, resolution, or planning.

They cannot become canonical enterprise data merely because a model produced them or because Noema stores them.

Canonical enterprise facts require authoritative grounding.

⸻

43. Human-Provided Data

User-provided information is also not automatically canonical.

Example:

"John's account number is 123."

Noema may use it as an input to resolution.

For consequential operations, it may need verification against authoritative enterprise data.

Human-provided information can therefore be:

input
evidence
constraint
candidate identifier

without becoming canonical enterprise state.

⸻

44. Canonical Data Pipeline

A typical Noema flow is:

Enterprise Systems
       │
       ▼
Canonical Data
       │
       ▼
Integration
       │
       ▼
State Reconciliation
       │
       ▼
Context
       │
       ▼
Evidence / Fact Status
       │
       ▼
Trust
       │
       ▼
Action
       │
       ▼
Execution
       │
       ▼
Verification
       │
       ▼
Canonical Enterprise State

The direction matters.

Noema does not convert an inference, model output, or local execution state into Canonical Data merely because it used that information during execution.

⸻

45. Canonicalization

Canonicalization is the process of determining:

* which representation
* of which fact
* from which source
* within which scope
* at which time
* under which authority

is authoritative.

Example:

CRM:
C-123
Billing:
847291
Identity:
USR-991

Canonicalization may establish:

Enterprise Customer:
customer_id = 123

with explicit mappings to system-specific identities.

Canonicalization may require State Reconciliation where multiple sources describe the same Resource.

⸻

46. Canonicalization Is Not Guessing

If two candidate entities exist:

John Smith
John Smith

Noema must not arbitrarily canonicalize one.

Instead:

Ambiguity
   ↓
Deterministic Resolution
   ↓
or
   ↓
Clarification

This follows Noema’s core principle:

Ambiguity is a state, not an invitation to guess.

A probabilistic ranking may propose candidates, but it does not establish canonical identity.

⸻

47. Canonical Data and Identity Resolution

Identity resolution may use:

* canonical identifiers
* organizational relationships
* explicit user confirmation
* enterprise mappings
* permissions
* historical context
* resource relationships
* temporal constraints

The resulting identity should have sufficient evidence and Fact Status for the risk level of the Action.

A resolved identity must be bound to the relevant actor, tenant, organization, and resource scope before consequential execution.

⸻

48. Canonical Data and Action Planning

Planning may depend on multiple canonical facts.

Example:

Intent:
"Close my account."
Required facts:
account.status
account.balance
pending_transactions
outstanding_refunds

Noema should retrieve or reconcile the appropriate authoritative data before constructing the final execution path.

Planning must not invent missing canonical facts.

If required facts remain unknown, conflicted, stale, or insufficiently authorized, the planner must preserve those conditions rather than treating them as satisfied.

⸻

49. Canonical Data and Compound Intent

For compound Intent:

"Refund the payment and close the account."

different Actions may rely on different canonical domains:

refund
→ Payment System
close account
→ Account System

Noema must preserve the authority boundary for each step.

A single Intent does not imply that one system becomes canonical for all facts required by its Actions.

⸻

50. Canonical Data and Compensation

Compensation must operate against canonical Business State.

If:

Action A

changes enterprise state, compensation should invoke an authorized enterprise capability rather than mutate a local Noema copy.

Noema must not attempt to restore enterprise state by editing its own representation of that state.

⸻

51. Canonical Data and State Reconciliation

State Reconciliation is the first-class mechanism for establishing the current enterprise state relevant to Noema.

Reconciliation may compare:

Multiple enterprise observations
        +
events
        +
resource versions
        +
authoritative source state
        ↓
Reconciled State
        ↓
Fact Status

Example:

Noema:
refund outcome = UNKNOWN
Payment System:
refund.status = COMPLETED

Reconciliation can establish that the enterprise action completed and allow Noema to update its execution-domain state accordingly.

Reconciliation does not transfer ownership of the enterprise state to Noema.

⸻

52. Canonical Data and Auditability

For consequential Actions, the audit trail should preserve:

* fact used
* claim evaluated
* source
* authority scope
* observation time
* effective time
* resource version
* Fact Status
* reconciliation identity where applicable
* Intent version
* Action Contract version
* Trust Decision
* Execution
* Outcome

This makes execution decisions explainable and reconstructable without requiring access to private model chain-of-thought.

⸻

53. Canonical Data and System Migration

Canonical authority may change during system migrations.

Legacy System
      ↓
Migration
      ↓
New System

Noema must understand the effective authority during the migration period.

A migration must define:

* effective authority
* transition period
* coexistence semantics
* identifier mapping
* consistency expectations
* historical interpretation

Noema must not assume that the newest system is automatically authoritative.

⸻

54. Canonical Data and Environment

Canonicality must be environment-specific.

Production:
canonical balance = $10,000
Staging:
canonical balance = $500

Staging data must never accidentally satisfy a production execution requirement.

Environment is therefore part of the authority boundary.

⸻

55. Canonical Data and Tenancy

Canonicality is also tenant-scoped.

Tenant A:
account 123 → $10,000
Tenant B:
account 123 → $2,000

The identifier alone is insufficient.

The authority boundary includes:

* tenant
* system
* organization
* resource
* environment

Noema must not resolve an identifier across tenant boundaries merely because the identifier is syntactically valid.

⸻

56. Canonical Data and Organizational Boundaries

The same logical Resource may be visible across organizational boundaries.

Noema must preserve enterprise-defined authority and access boundaries.

For example:

Business Unit A
→ owns account
Business Unit B
→ may view account
Business Unit C
→ cannot access account

Canonicality does not erase authorization boundaries.

An enterprise may establish authority for a fact while separately restricting which actors or applications may access it.

⸻

57. Canonical Data Model

Conceptually:

CanonicalData {
    subject
    attribute
    value
    source_system
    authority_scope
    observed_at
    effective_at
    version
    freshness
    provenance
}

Where useful, a claim-level representation may additionally track:

claim_id
fact_status
reconciliation_id
valid_from
valid_until

This is a semantic model rather than a requirement for a literal database table.

⸻

58. Canonical Data Relationships

Canonical Data
    │
    ├── belongs_to → Resource
    ├── sourced_from → System
    ├── authoritative_within → Authority Scope
    ├── observed_by → Noema
    ├── supports → Evidence
    ├── contributes_to → Fact Status
    ├── reconciled_by → State Reconciliation
    ├── constrains → Action
    ├── satisfies → Precondition
    └── verifies → Postcondition

Canonical Data does not itself become:

Trust Decision
Outcome
Noema Execution State

Those are distinct semantic objects.

⸻

59. Canonical Data and Unknown

Noema must preserve unknown state when canonical enterprise truth cannot be established.

Examples:

Source unavailable
Resource not found
Conflicting authoritative observations
Version cannot be established
Freshness requirement cannot be satisfied
Authority boundary is unresolved

These conditions must not be converted into:

false
success
failure
probably true

without an explicit semantic basis.

Unknown is an information state, not an error value that may be freely collapsed.

⸻

60. Canonical Data and Security Boundary

Enterprise data presented to Noema must be treated according to explicit integration and access boundaries.

The following are not authoritative merely because they contain enterprise-looking information:

* model output
* user input
* retrieved text
* arbitrary tool output
* unvalidated API responses
* unvalidated event payloads

Data entering Noema must pass the appropriate validation, integration, permission, provenance, and semantic checks before it can contribute to consequential decisions.

The model must not have direct credentials or unrestricted access to enterprise systems.

⸻

61. Canonical Data and Mode 1 / Mode 2

Canonical Data semantics apply in both Noema operating modes.

Mode 1

Noema receives the Source of Intent, resolves relevant enterprise state, evaluates Trust, executes through bounded capabilities, and verifies against enterprise systems.

Mode 2

An enterprise agent or orchestrator may handle interaction and produce a canonical Intent or Action candidate.

Noema still establishes its own hard validation, state requirements, Trust boundary, and execution semantics.

In neither mode does Noema assume ownership of enterprise Business State merely because it participates in its execution.

⸻

62. Canonical Data and Operational Memory

Operational Memory may preserve historical observations, execution cases, reconciliation results, and decisions.

Operational Memory is not automatically canonical enterprise data.

For example:

Operational Memory:
"Payment 123 was observed as SUCCEEDED at T1."

does not mean:

Payment System:
payment.status = SUCCEEDED

Operational Memory can support historical reconstruction and future resolution, but enterprise authority remains defined by the applicable System of Record and authority boundary.

⸻

63. Canonical Data and Read-Only Operations

Read-only does not mean semantically inconsequential.

A read operation may expose:

* financial information
* personal information
* organizational information
* protected operational state

Therefore, canonical data used by a read-only Action may still require:

* identity resolution
* permission evaluation
* scope validation
* Trust evaluation
* freshness checks
* auditability

The absence of a write does not remove the authority boundary.

⸻

64. Canonical Data and Outcome

Canonical Data must remain distinct from Outcome.

For example:

Enterprise:
refund.status = COMPLETED

is enterprise state.

Noema may establish:

Outcome:
refund_verified

as the result of its execution and verification process.

The Outcome describes what Noema established about the execution.

It does not replace the enterprise Resource state.

⸻

65. Canonical Data and Contract Versioning

Canonical data semantics may depend on the versions of the contracts that interpret them.

A consequential record may therefore need to retain:

* Contract Version
* Policy Version
* resource version
* source system version
* reconciliation version
* observation time

A newer contract must not silently reinterpret historical canonical data in a way that changes the meaning of a prior decision.

⸻

66. Canonical Data Invariants

Invariant 1

Canonicality must always have an explicit authority boundary.

Invariant 2

A System of Record and Canonical Data are related but distinct concepts.

Invariant 3

Canonical Data must not be confused with Context.

Invariant 4

Evidence describing Canonical Data is not itself the canonical state.

Invariant 5

Fact Status is distinct from Canonical Data, Evidence, Context, Business State, and Outcome.

Invariant 6

Model-generated information is not canonical by default.

Invariant 7

User-provided information is not canonical by default.

Invariant 8

Derived and cached data must not silently override canonical data.

Invariant 9

Authority takes precedence over source count when sources disagree.

Invariant 10

Canonicality may be scoped by tenant, organization, domain, resource, field, environment, version, and time.

Invariant 11

Canonicality and freshness are separate properties.

Invariant 12

Consequential Preconditions should use authoritative data appropriate to the Action.

Invariant 13

Consequential Postconditions should be verified against authoritative state where required.

Invariant 14

If canonical data is unavailable, Noema must not silently substitute uncertain data for high-risk execution.

Invariant 15

Canonical identity must be grounded before consequential execution.

Invariant 16

Canonicalization must not rely on probabilistic guessing when ambiguity remains material.

Invariant 17

Canonical enterprise data remains enterprise-owned unless explicitly delegated otherwise.

Invariant 18

Noema may maintain canonical data for its own execution domain without becoming the canonical owner of enterprise Business State.

Invariant 19

Consequential canonical data should retain sufficient provenance for audit and reconstruction.

Invariant 20

Events may provide evidence of changes to canonical data but do not necessarily establish current canonical state.

Invariant 21

Historical canonicality must be preserved where required to reconstruct past execution decisions.

Invariant 22

Canonical Data does not imply authorization to access or use that data.

Invariant 23

Canonicality must not cross tenant, organizational, legal, or environment boundaries implicitly.

Invariant 24

Noema must not create shadow canonical Business State merely for execution convenience.

Invariant 25

Canonical data used for execution must satisfy the freshness requirements defined by the relevant Action and Policy.

Invariant 26

When canonical authority cannot be established, the system must preserve the uncertainty rather than manufacture certainty.

Invariant 27

State Reconciliation is the first-class mechanism for resolving relevant observations of enterprise state; Noema must not substitute probabilistic judgment for reconciliation.

Invariant 28

A reconciled observation does not transfer ownership of enterprise Business State to Noema.

Invariant 29

An enterprise event does not become canonical current state merely because it is authenticated or successfully delivered.

Invariant 30

A source’s authority is claim-specific and scope-specific.

Invariant 31

Canonical Data may be inaccessible even when its existence and authority are established.

Invariant 32

Noema must not infer enterprise authorization from the canonicality of a fact.

Invariant 33

Noema must not treat model confidence as evidence of canonicality.

Invariant 34

Canonical Data used in consequential execution must be attributable to the exact scope, resource, and temporal conditions under which it was evaluated.

Invariant 35

Conflicting authoritative observations must remain explicit until resolved by deterministic reconciliation or applicable policy.

Invariant 36

Unknown canonical state must not be silently converted into success, failure, authorization, or certainty.

Invariant 37

Canonical Data and Noema execution-domain state must remain distinct authority domains.

Invariant 38

Noema must not silently mutate enterprise Business State to reconcile its own execution state.

Invariant 39

Canonical Data required for a consequential Action must satisfy the relevant contract, policy, permission, freshness, and Fact Status requirements.

Invariant 40

Historical canonical data must remain interpretable under the authority and semantic conditions applicable to the historical execution.

⸻

67. Final Definition

Canonical Data is authoritative enterprise information within a defined scope of authority.

Noema uses Canonical Data to ground Context, resolve enterprise Resources, establish relevant state through State Reconciliation, validate Preconditions, evaluate Trust, and verify Postconditions, while preserving the enterprise’s ownership of Business Truth.

The fundamental relationship is:

SYSTEM OF RECORD
       │
       ▼
CANONICAL DATA
       │
       ▼
STATE RECONCILIATION
       │
       ▼
NOEMA CONTEXT
       │
       ▼
EVIDENCE + FACT STATUS
       │
       ▼
TRUST
       │
       ▼
ACTION
       │
       ▼
EXECUTION
       │
       ▼
VERIFICATION
       │
       ▼
CANONICAL ENTERPRISE STATE

And the architectural rule is:

Noema can reason over enterprise truth, act upon enterprise truth, reconcile observations of enterprise truth, and verify against enterprise truth—but it must never silently redefine what that truth is.

Canonical Data therefore establishes the boundary between enterprise authority and Noema execution-domain state, allowing Noema to operate deterministically over enterprise systems without becoming an unauthorized competing source of business truth.