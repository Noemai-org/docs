Canonical Data

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/canonical-data.md

⸻

1. Definition

Canonical Data is the authoritative representation of an enterprise fact, entity, resource, or state within its defined domain and authority boundary.

Canonical Data answers:

“What is the authoritative value of this fact right now?”

For Noema, this distinction is fundamental because Noema operates on enterprise data without necessarily owning it.

Enterprise System
      │
      ▼
Canonical Data
      │
      ├── Context
      ├── Evidence
      ├── Preconditions
      └── Postconditions
              │
              ▼
            Noema

Noema consumes Canonical Data to make execution decisions. It does not automatically become its owner.

⸻

2. Purpose

The purpose of Canonical Data is to establish a precise distinction between:

canonical
derived
cached
observed
inferred
stale
historical

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

They do not necessarily have equal authority.

⸻

3. Core Principle

Data is canonical only within an explicitly defined authority boundary.

There is no universal concept of:

"the canonical customer data"

without defining:

which fact
which domain
which system
which authority
which time

For example:

Customer name
→ CRM
Account balance
→ Ledger
Payment status
→ Payment System

Canonicality is therefore scoped.

⸻

4. Canonical Data vs System of Record

These concepts are related but different.

System of Record

The authoritative system responsible for a domain of facts.

Canonical Data

The authoritative representation of a particular fact, entity, resource, or state within that domain.

System of Record
      │
      ▼
Canonical Data

A System of Record provides the authority; Canonical Data is the authoritative information produced or maintained within that boundary.

⸻

5. Canonical Data vs Context

Context is information available to Noema for reasoning and execution.

Canonical Data is authoritative information.

Therefore:

Context
    may contain
        ↓
Canonical Data

but:

Context ≠ Canonical Data

Context can also contain:

derived information
historical information
external evidence
user-provided information
model interpretations

These should not automatically be treated as canonical.

⸻

6. Canonical Data vs Evidence

Evidence supports a proposition.

Canonical Data represents the authoritative state underlying that proposition.

Example:

Evidence:
"Ledger reports balance = $5,000"
Canonical Data:
Account.balance = $5,000

The evidence records how Noema knows.

Canonical Data describes what the authoritative system says is true.

⸻

7. Canonical Data vs Inference

Inference is not canonical merely because it is highly probable.

Model inference:
customer probably owns account 123

is not equivalent to:

Canonical relationship:
customer 456 → account 123

The latter must come from an authoritative enterprise source or explicitly trusted configuration.

⸻

8. Canonical Data vs Cached Data

A cache can contain a copy of canonical data.

But:

cached = canonical

is not a safe assumption.

The cache must have explicit semantics concerning:

freshness
source
authority
version
expiration
consistency

⸻

9. Canonicality Is Scoped

Canonicality can be scoped by:

tenant
organization
legal entity
domain
resource
field
environment
time
version

For example:

Account.balance

may be canonical in:

Production Ledger / Tenant A

but not:

Analytics Warehouse / Tenant A

⸻

10. Canonical Entity

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

⸻

11. Canonical Resource

A Resource may have canonical state within a System of Record.

Example:

Payment #123
status = SUCCEEDED
amount = $500
currency = USD

The payment system may be canonical for these fields.

Noema can reference them without owning them.

⸻

12. Canonical State

Canonical state is the authoritative current state of a Resource.

Payment
    ↓
status = REFUNDED

If another system reports:

status = SUCCEEDED

Noema must determine which source is authoritative and whether the discrepancy is caused by:

replication lag
eventual consistency
stale cache
different state definitions
actual inconsistency

⸻

13. Field-Level Canonicality

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

⸻

14. Canonical Relationships

Relationships can also have authoritative sources.

Example:

Employee
    ↓ belongs_to
Department

The HRIS may be authoritative for this relationship.

Noema should not infer organizational relationships from:

email domain
past behavior
calendar events
model assumptions

when authoritative enterprise data exists.

⸻

15. Canonical Identifiers

Stable enterprise identifiers should be preferred.

Examples:

customer_id
account_id
employee_id
invoice_id
payment_id
order_id

Noema should preserve these identifiers rather than generating competing identities unnecessarily.

⸻

16. Identity Resolution

Noema may need to resolve:

"John"

to:

employee_id = 4821

This is an intent-resolution problem.

The resulting identity should be grounded against canonical enterprise identity data before consequential execution.

⸻

17. Canonical Data and Intent

Intent often references enterprise Resources indirectly.

Example:

"Refund my last payment."

The phrase:

"my last payment"

must ultimately resolve to a canonical enterprise Resource.

Conceptually:

Natural Language
      ↓
Intent
      ↓
Identity Resolution
      ↓
Enterprise Resource
      ↓
Canonical Data

⸻

18. Canonical Data and Preconditions

Preconditions should use authoritative data whenever the fact is consequential.

Example:

Precondition:
account.balance >= $1,000

Noema should evaluate:

Canonical Account Balance

rather than:

Model-estimated balance

or:

arbitrary cached balance

unless policy explicitly permits the alternative.

⸻

19. Canonical Data and Postconditions

Postconditions may require verification against Canonical Data.

Example:

Action:
freeze_card
Postcondition:
card.status = FROZEN

Noema should verify the state against the authoritative source where required.

Action
 ↓
System
 ↓
Canonical State
 ↓
Postcondition

⸻

20. Canonical Data and Trust

Canonicality affects Trust.

Evidence from an authoritative source generally has greater decision relevance than equivalent information from a derived source.

For example:

Ledger:
balance = $10,000

is stronger for a financial decision than:

Analytics DB:
balance = $10,000

assuming the Ledger is authoritative for balance.

⸻

21. Canonical Data and Determinism

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
Policy
   ↓
Decision

If canonicality cannot be established:

AMBIGUOUS

should remain a legitimate state.

⸻

22. Multiple Sources

Noema may encounter:

Source A → X
Source B → X
Source C → Y

Agreement does not automatically make X canonical.

The question is:

Which source has authority for this fact?

Authority takes precedence over source count.

⸻

23. Conflicting Canonical Sources

Two systems should ideally not both claim canonical authority for the same fact within the same scope.

If they do:

System A → $10,000
System B → $8,000

Noema should not resolve the conflict through probabilistic judgment.

The system should enter an explicit conflict state requiring:

authority resolution
reconciliation
clarification
escalation

according to Policy.

⸻

24. Temporal Canonicality

Canonical data is time-dependent.

Consider:

10:00
balance = $10,000
10:05
balance = $8,000

Both values may have been canonical at different times.

Therefore canonical data may require:

observed_at
effective_at
version

where relevant.

⸻

25. Historical Canonical Data

Historical execution may depend on data that was canonical at the time.

For example:

At T1:
refund_limit = $5,000
At T2:
refund_limit = $2,500

An audit of an execution at T1 should not reinterpret it solely using today’s value.

Noema must preserve enough provenance to reconstruct the relevant historical context.

⸻

26. Versioned Canonical Data

Some systems expose versioned resources.

Example:

Customer:
version = 42

Noema may use version identifiers to ensure that execution decisions are based on the expected state.

This supports optimistic concurrency and deterministic validation.

⸻

27. Freshness

Canonical does not necessarily mean:

currently observed

A canonical system can be temporarily unavailable.

Likewise, a cached copy can be:

recent

without being authoritative.

Therefore:

authority ≠ freshness

Both may matter independently.

⸻

28. Freshness Requirements

Different Actions require different freshness guarantees.

Example:

"Show me my account balance."

may tolerate a small delay.

But:

"Transfer $9,000."

may require current authoritative state.

Freshness requirements should therefore be defined by Action and Policy.

⸻

29. Canonical Data Availability

If canonical data cannot be retrieved:

Ledger unavailable

Noema should not automatically substitute:

cached balance

for a high-risk transaction.

Instead:

Canonical Data Unavailable
        ↓
Trust / Policy
        ↓
Clarify / Retry / Escalate / Reject

⸻

30. Canonical Data and Business State

Canonical Data is closely tied to Business State.

Business Resource
      ↓
Canonical State

Noema may observe this state.

It should not create a competing authoritative state representation unless explicitly owning that domain.

⸻

31. Canonical Data and Noema State

Noema maintains its own state:

Intent
Trust Decision
Action
Execution
Outcome

These are canonical within Noema’s execution domain.

Therefore:

Enterprise Canonical Data

and:

Noema Canonical Data

can coexist without conflict because they belong to different authority domains.

⸻

32. Canonical Data and Execution Truth

Noema can be authoritative for:

execution.status
trust.decision
intervention.status
intent.lifecycle

while the enterprise remains authoritative for:

account.balance
payment.status
employee.status
inventory.quantity

This maintains the architectural boundary established in system-of-record.md.

⸻

33. Canonical Data and Data Boundaries

Noema should only retrieve the minimum Canonical Data necessary for an execution.

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

34. Canonical Data and Permissions

A piece of data can be canonical but inaccessible to a particular principal.

Therefore:

canonical

does not imply:

authorized_to_view

or:

authorized_to_use

Noema must evaluate data access independently.

⸻

35. Canonical Data and Privacy

Canonical enterprise data may contain sensitive information.

Noema should apply:

least privilege
field minimization
purpose limitation
retention controls
redaction
access policies

where applicable.

⸻

36. Canonical Data and Provenance

Consequential data should preserve provenance.

Conceptually:

CanonicalFact {
    resource
    attribute
    value
    source
    observed_at
    effective_at
    version
    authority
}

This allows Noema to answer:

Where did this value come from?

⸻

37. Canonical Data and Evidence

A useful relationship is:

Canonical Data
      ↓
Observed by Noema
      ↓
Evidence
      ↓
Trust Evaluation

The Evidence layer records the observation used by Noema.

⸻

38. Canonical Data and Events

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

⸻

39. Eventual Consistency

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

⸻

40. Derived Data

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

⸻

41. Model-Generated Data

LLM-generated information is not canonical by default.

Examples:

"User probably means account 123."
"Customer is likely high value."
"This appears to be a refund request."

These are interpretations or hypotheses.

They may become executable only after the appropriate grounding and Trust process.

⸻

42. Human-Provided Data

User-provided information is also not automatically canonical.

Example:

"John's account number is 123."

Noema may use it as an input.

For consequential operations, it may need verification against authoritative enterprise data.

⸻

43. Canonical Data Pipeline

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
Context
       │
       ▼
Evidence
       │
       ▼
Trust
       │
       ▼
Action

The direction matters.

Noema does not convert an inference into Canonical Data merely because it used that inference in execution.

⸻

44. Canonicalization

Canonicalization is the process of determining:

which representation
of which fact
from which source
within which scope
is authoritative

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

with mappings to system-specific identities.

⸻

45. Canonicalization Is Not Guessing

If two candidate entities exist:

John Smith
John Smith

Noema must not arbitrarily canonicalize one.

Instead:

Ambiguity
   ↓
Clarification / deterministic resolution

This follows Noema’s core principle:

Ambiguity is a state, not an invitation to guess.

⸻

46. Canonical Data and Identity Resolution

Identity resolution may use:

canonical identifiers
organizational relationships
explicit user confirmation
enterprise mappings
permissions
historical context

The resulting identity should have sufficient evidence for the risk level of the Action.

⸻

47. Canonical Data and Action Planning

Planning may depend on multiple canonical facts.

Example:

Intent:
"Close my account."
Required facts:
account.status
account.balance
pending_transactions
outstanding_refunds

Noema should retrieve the appropriate authoritative data before constructing the final execution path.

⸻

48. Canonical Data and Compound Intent

For compound Intent:

"Refund the payment and close the account."

different Actions may rely on different canonical domains:

refund
→ Payment System
close account
→ Account System

Noema must preserve the authority boundary for each step.

⸻

49. Canonical Data and Compensation

Compensation must operate against canonical Business State.

If:

Action A

changes enterprise state, compensation should invoke an authorized enterprise capability rather than mutate a local Noema copy.

⸻

50. Canonical Data and Reconciliation

Reconciliation compares:

Noema Execution State

against:

Enterprise Canonical State

Example:

Noema:
refund outcome = UNKNOWN
Payment System:
refund.status = COMPLETED

Reconciliation can resolve the execution state.

⸻

51. Canonical Data and Auditability

For consequential Actions, the audit trail should preserve:

fact used
source
authority
observation time
version
Action
Trust decision
Outcome

This makes execution decisions explainable and reconstructable.

⸻

52. Canonical Data and System Migration

Canonical authority may change during system migrations.

Legacy System
      ↓
Migration
      ↓
New System

Noema must understand the effective authority during the migration period.

⸻

53. Canonical Data and Environment

Canonicality must be environment-specific.

Production:
canonical balance = $10,000
Staging:
canonical balance = $500

Staging data must never accidentally satisfy a production execution requirement.

⸻

54. Canonical Data and Tenancy

Canonicality is also tenant-scoped.

Tenant A:
account 123 → $10,000
Tenant B:
account 123 → $2,000

The identifier alone is insufficient.

The authority boundary includes:

tenant
system
resource

⸻

55. Canonical Data and Organizational Boundaries

The same logical resource may be visible across organizational boundaries.

Noema must preserve the enterprise-defined authority and access boundaries.

For example:

Business Unit A
→ owns account
Business Unit B
→ may view account
Business Unit C
→ cannot access account

Canonicality does not erase authorization boundaries.

⸻

56. Canonical Data Model

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

This is a semantic model rather than a requirement for a literal database table.

⸻

57. Canonical Data Relationships

Canonical Data
    │
    ├── belongs_to → Resource
    ├── sourced_from → System
    ├── authoritative_within → Scope
    ├── observed_by → Noema
    ├── supports → Evidence
    ├── constrains → Action
    ├── satisfies → Precondition
    └── verifies → Postcondition

⸻

58. Canonical Data Invariants

Invariant 1

Canonicality must always have an explicit authority boundary.

Invariant 2

A System of Record and Canonical Data are related but distinct concepts.

Invariant 3

Canonical Data must not be confused with Context.

Invariant 4

Evidence describing Canonical Data is not itself the canonical state.

Invariant 5

Model-generated information is not canonical by default.

Invariant 6

User-provided information is not canonical by default.

Invariant 7

Derived and cached data must not silently override canonical data.

Invariant 8

Authority takes precedence over source count when sources disagree.

Invariant 9

Canonicality may be scoped by tenant, organization, domain, resource, field, environment, version, and time.

Invariant 10

Canonicality and freshness are separate properties.

Invariant 11

Consequential Preconditions should use authoritative data appropriate to the Action.

Invariant 12

Consequential Postconditions should be verified against authoritative state where required.

Invariant 13

If canonical data is unavailable, Noema must not silently substitute uncertain data for high-risk execution.

Invariant 14

Canonical identity must be grounded before consequential execution.

Invariant 15

Canonicalization must not rely on probabilistic guessing when ambiguity remains material.

Invariant 16

Canonical enterprise data remains enterprise-owned unless explicitly delegated otherwise.

Invariant 17

Noema may maintain canonical data for its own execution domain without becoming the canonical owner of enterprise Business State.

Invariant 18

Consequential canonical data should retain sufficient provenance for audit and reconstruction.

Invariant 19

Events may provide evidence of changes to canonical data but do not necessarily establish current canonical state.

Invariant 20

Historical canonicality must be preserved where required to reconstruct past execution decisions.

Invariant 21

Canonical Data does not imply authorization to access or use that data.

Invariant 22

Canonicality must not cross tenant, organizational, legal, or environment boundaries implicitly.

Invariant 23

Noema must not create shadow canonical Business State merely for execution convenience.

Invariant 24

Canonical data used for execution must satisfy the freshness requirements defined by the relevant Action and Policy.

Invariant 25

When canonical authority cannot be established, the system must preserve the uncertainty rather than manufacture certainty.

⸻

59. Final Definition

Canonical Data is authoritative enterprise information within a defined scope of authority. Noema uses Canonical Data to ground Context, validate Preconditions, evaluate Trust, and verify Postconditions, while preserving the enterprise’s ownership of Business Truth.

The fundamental relationship is:

SYSTEM OF RECORD
       │
       ▼
CANONICAL DATA
       │
       ▼
   NOEMA CONTEXT
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
       │
       ▼
VERIFY AGAINST
CANONICAL DATA

And the architectural rule is:

Noema can reason over enterprise truth, act upon enterprise truth, and verify against enterprise truth—but it must never silently redefine what that truth is.