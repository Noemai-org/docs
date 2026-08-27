Data Boundaries

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/data-boundaries.md

⸻

1. Definition

Data Boundaries define what enterprise data Noema may access, what it may retain, what it may transform, what it may expose, and where authority over that data remains.

Data Boundaries prevent Noema from becoming an uncontrolled data aggregation layer.

The fundamental rule is:

Noema may access data necessary to understand and execute Intent,
but access does not imply ownership.

⸻

2. Purpose

Noema operates across enterprise systems.

Those systems may contain:

customers
accounts
transactions
employees
permissions
documents
financial records
operational data
internal policies

Noema therefore needs explicit boundaries around:

what enters Noema
what remains external
what can be persisted
what can be shared
what can be derived
who can access it
how long it remains available

⸻

3. Core Principle

Noema should ingest the minimum data necessary to perform the current Intent safely and reliably.

This is the principle of data minimization.

Noema should not follow:

"If we can access it, we should ingest it."

It should follow:

"If the execution journey requires it, retrieve it
within the authority and policy boundaries."

⸻

4. Data Ownership

The enterprise remains authoritative for enterprise data.

Enterprise
    │
    ├── owns customer data
    ├── owns financial data
    ├── owns transaction data
    ├── owns employee data
    └── owns operational data

Noema may process representations of that data without becoming its owner.

⸻

5. Noema’s Data Categories

Conceptually, Noema interacts with several categories:

Intent Data
Context Data
Evidence
Business State
Action Data
Trust Data
Execution Data
Outcome Data
Audit Data
Integration Data

These categories have different retention and sensitivity requirements.

⸻

6. Intent Data

Intent Data represents what a user or agent requested.

Examples:

"Refund my last payment."
"Block my card."
"Give Sarah access to the project."

Intent Data may contain sensitive information and must be handled according to enterprise policy.

⸻

7. Context Data

Context Data is information gathered to interpret or execute an Intent.

Examples:

customer status
account state
resource ownership
permissions
transaction history
organizational relationships

Context should be scoped to the current Intent wherever possible.

⸻

8. Evidence

Evidence supports Trust decisions.

Examples:

authorization result
policy version
account status
identity verification
risk signal
enterprise API response

Evidence should retain enough provenance to explain consequential decisions.

⸻

9. Business State

Business State belongs to the enterprise.

Noema may observe:

account.balance = 5000

but should not assume:

Noema owns account.balance

The authoritative value remains in the enterprise system.

⸻

10. Action Data

Action Data describes what Noema intends to cause in the enterprise.

Example:

Action:
freeze_card
Target:
card_123
Reason:
user_requested
Contract:
freeze-card.v2

Action Data is Noema-owned execution information, but may reference enterprise resources.

⸻

11. Trust Data

Trust Data includes:

Trust evaluation
policy references
evidence references
authorization result
risk result
decision

Trust Data should be durable enough to explain consequential decisions.

⸻

12. Execution Data

Execution Data describes what Noema attempted and what occurred during execution.

Examples:

execution_id
attempt
state
provider
request reference
response status
failure
retry
completion

Execution Data belongs to Noema’s execution record.

⸻

13. Outcome Data

Outcome Data describes the observed result of an Action.

For example:

Expected:
card frozen
Observed:
enterprise system reports card.status = FROZEN

The enterprise remains authoritative for the underlying state.

⸻

14. Audit Data

Audit Data provides the historical record of consequential behavior.

It may reference:

Intent
Action
Trust
Execution
Outcome
Actor
Policy
Evidence

Audit Data should not automatically contain every raw payload involved in execution.

⸻

15. Integration Data

Integration Data exists at the boundary between Noema and external systems.

Examples:

API request metadata
provider request ID
provider response ID
event ID
schema version
integration version

Sensitive credentials and secrets must not be treated as ordinary integration data.

⸻

16. Secrets

Secrets should have a separate security boundary.

Examples:

API keys
OAuth tokens
client secrets
private keys
database credentials
signing keys

Noema should reference secret material through appropriate secret-management mechanisms rather than embedding secrets into Intent, Context, Action, Trust, or Audit records.

⸻

17. Data Flow Boundary

The canonical flow is:

Enterprise
   │
   │ authorized access
   ▼
Noema Context
   │
   ▼
Intent / Trust / Action
   │
   ▼
Execution
   │
   │ authorized invocation
   ▼
Enterprise

Data should cross these boundaries intentionally.

⸻

18. Read Boundary

Noema should only read enterprise data required for the current operation.

Example:

Intent:
"Transfer $500 from my account."
Required:
account identity
account status
available balance
authorization
transfer limits

Not necessarily:

entire customer profile
full transaction history
unrelated accounts

⸻

19. Write Boundary

Noema should only cause enterprise state changes through approved interfaces.

Preferred:

Noema
   ↓
Action Contract
   ↓
Enterprise API
   ↓
Business State

Avoid:

Noema
   ↓
direct database mutation

unless explicitly supported by the enterprise architecture.

⸻

20. Transformation Boundary

Noema may transform enterprise data into forms required for:

Intent resolution
Context
Trust
Action construction
Outcome verification

Transformation does not transfer authority.

Example:

Enterprise:
employee.role = "finance_manager"
Noema:
authorization_context = "may_approve_invoice"

The latter is a derived representation, not necessarily a new authoritative fact.

⸻

21. Derived Data

Noema may derive information.

Examples:

eligible_for_refund = true
risk_level = HIGH
candidate_customer = customer_123

Derived data must remain distinguishable from authoritative enterprise facts.

Authoritative:
enterprise says X
Derived:
Noema concludes Y from X

⸻

22. Model-Generated Data

Model output is another category.

Examples:

interpreted Intent
candidate entities
extracted parameters
semantic classification
confidence

Model-generated information must not automatically cross the boundary into authoritative Business State.

⸻

23. Data Provenance

Important data used for consequential decisions should preserve provenance.

Conceptually:

Data
 ↓
Source
 ↓
Observed at
 ↓
Version / authority
 ↓
Used by

This is particularly important for Trust and Auditability.

⸻

24. Source Authority

Noema should know where a piece of data came from.

For example:

balance
  → Ledger
identity
  → Identity Provider
subscription status
  → Billing System

Source authority should be part of the enterprise integration model.

⸻

25. Conflicting Data

If two sources disagree:

System A:
ACTIVE
System B:
SUSPENDED

Noema must not silently select one.

The appropriate behavior depends on:

source authority
policy
risk
freshness
operation

If uncertainty cannot be safely resolved:

CLARIFY
ESCALATE
REJECT
HOLD

may be appropriate.

⸻

26. Data Freshness

Data has temporal validity.

A data record should conceptually carry:

observed_at
source
freshness

where relevant.

For high-risk execution:

stale data
    ↓
may invalidate Trust

⸻

27. Data at Rest

Persisted Noema data should be classified according to sensitivity.

Examples:

Low:
execution metadata
Medium:
Intent parameters
High:
financial or identity-related Context
Critical:
credentials and secrets

The actual classification belongs to enterprise policy.

⸻

28. Data in Transit

Enterprise data crossing into or out of Noema should use approved secure transport mechanisms.

The exact transport is implementation-specific.

The invariant is:

Sensitive enterprise data must not cross integration boundaries without appropriate protection.

⸻

29. Tenant Boundary

Noema must maintain strict tenant isolation.

Tenant A
 ├── Intent A
 ├── Context A
 ├── Trust A
 └── Execution A
Tenant B
 ├── Intent B
 ├── Context B
 ├── Trust B
 └── Execution B

Data from one tenant must not become Context for another tenant unless explicitly authorized.

⸻

30. Actor Boundary

Data access may also depend on the Actor.

Actor A
   ↓
authorized Context
Actor B
   ↓
different authorized Context

The same enterprise resource may expose different information to different actors.

⸻

31. Purpose Limitation

Data access should have a purpose.

Conceptually:

Intent
   ↓
Purpose
   ↓
Required Data
   ↓
Access

If data is unrelated to the current purpose, it should generally not be retrieved merely because it is available.

⸻

32. Context Isolation

Context gathered for one Intent should not automatically leak into another.

For example:

Intent A
  ↓
private customer information

must not automatically become:

Context for Intent B

without appropriate authorization and relevance.

⸻

33. Cross-Intent Memory

Historical information can sometimes be useful.

However, reusing it requires considering:

relevance
freshness
authorization
tenant
actor
purpose
sensitivity

Memory is therefore not a bypass around data boundaries.

⸻

34. Cross-System Boundary

A single Intent may involve multiple enterprise systems.

Example:

CRM
 ↓
Payment System
 ↓
Inventory
 ↓
Messaging

Noema should expose each integration only to the data necessary for its Action.

A payment integration should not automatically receive unrelated CRM data.

⸻

35. Least Privilege

Noema integrations should follow least privilege.

Integration
    ↓
minimum required permissions
    ↓
minimum required data

This reduces both accidental exposure and blast radius.

⸻

36. Action-Specific Data Scope

An Action Contract may define required data.

Example:

Action:
refund_payment
Requires:
payment_id
payment_status
refund_limit
authorization

This creates an explicit relationship between execution capability and data requirements.

⸻

37. Trust-Specific Data Scope

Trust evaluation may require different data from execution.

For example:

Trust:
authorization
risk
policy
account state
Execution:
payment ID
amount
destination

Noema should not automatically pass every Trust input into the execution layer.

⸻

38. Data Boundary Before Trust

The Trust Engine should evaluate only data that Noema is authorized to use.

Enterprise Data
      ↓
Authorization / Data Boundary
      ↓
Permitted Context
      ↓
Trust

Unauthorized information must not become hidden Trust evidence.

⸻

39. Data Boundary Before Model

The model should not receive unrestricted enterprise data.

Enterprise
    ↓
Data Boundary
    ↓
Relevant Context
    ↓
Model

This reduces unnecessary exposure and limits the model’s information surface.

⸻

40. Model Context Isolation

The model should receive only the context necessary for the task.

For example:

User:
"Cancel my order."
Model may need:
order candidates
order status
relevant customer identity
Model does not necessarily need:
full payment history
unrelated employee records
internal credentials

⸻

41. Prompt Data Is Data

Information inserted into model prompts is still enterprise data.

Therefore:

Prompt
    ≠
safe boundary

Prompt construction must respect the same data-access policies as other Noema components.

⸻

42. Model Output Boundary

Model output should be treated as untrusted derived data until validated.

Model
 ↓
candidate Action
 ↓
Validation
 ↓
Trust
 ↓
Execution

A model cannot bypass data or authorization boundaries merely by producing a structured Action.

⸻

43. Data Exfiltration Boundary

Noema must prevent enterprise data from being unintentionally sent to:

external models
third-party APIs
logging systems
analytics systems
telemetry providers

unless explicitly authorized.

⸻

44. Logging Boundary

Raw enterprise payloads should not automatically enter logs.

Bad:

log(request.body)

when the body contains sensitive information.

Preferred:

log:
request_id
action_id
status
error_code

with sensitive payloads handled through controlled mechanisms.

⸻

45. Audit Boundary

Auditability requires evidence, but auditability does not require storing every payload.

The correct principle is:

Maximum explainability
within minimum necessary data retention.

⸻

46. Redaction

Sensitive fields may need to be:

redacted
masked
tokenized
hashed
encrypted
excluded

depending on their purpose and sensitivity.

Example:

card_number:
**** **** **** 1234

rather than storing the full number.

⸻

47. Data Retention

Different data classes may have different retention periods.

Intent:
X days
Execution:
Y days
Audit:
Z years
Sensitive payload:
shorter retention
Secrets:
never retained as ordinary records

Actual values should be enterprise-configurable.

⸻

48. Deletion

Deletion must account for dependencies.

Deleting an Intent payload should not necessarily destroy the fact that:

an execution occurred

The audit record may retain a minimal reference while the sensitive payload is removed.

⸻

49. Referential Integrity After Deletion

Noema should support references that survive data minimization where necessary.

For example:

Intent:
ID 123
payload:
deleted
Audit:
Intent 123 produced Action 456

The system can retain the execution fact without retaining the original sensitive content indefinitely.

⸻

50. Data Residency

Enterprise requirements may constrain where data is processed or stored.

Noema’s data architecture should support enterprise-defined:

region
jurisdiction
storage location
processing location
model location

where applicable.

⸻

51. External Model Providers

If Noema uses an external model provider, enterprise data crossing that boundary must be governed explicitly.

The integration must establish:

what data is sent
why it is sent
where it is processed
how it is retained
who can access it

⸻

52. Self-Hosted Models

Self-hosted models can reduce some external data-boundary concerns but do not eliminate them.

Enterprise data still requires:

access control
tenant isolation
retention rules
model-context isolation
auditability

⸻

53. Data Classification

Noema should support enterprise-defined classifications.

For example:

PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED

The exact taxonomy is enterprise-specific.

Data classification can influence:

model access
storage
logging
retention
sharing
execution

⸻

54. Data and Policy

Policy may constrain data usage.

Example:

Policy:
Customer financial data may only be accessed
for payment-related operations.

Noema must treat that policy as a Trust/data-access constraint.

⸻

55. Data and Authorization

Authorization determines whether an Actor or Noema integration may access data.

Actor
 ↓
Authorization
 ↓
Data Boundary
 ↓
Context

Authorization should precede exposure.

⸻

56. Data and Capability

Capability describes what an integration can do.

Data Boundary describes what information it may access.

These are related but distinct.

Capability:
refund_payment
Data Scope:
payment_id
payment_status
refund_limit

A capability without appropriate data access may be unusable.

⸻

57. Data and Trust

Trust should consider whether the evidence used was:

authorized
authoritative
relevant
fresh
complete enough

Therefore data boundaries directly influence Trust.

⸻

58. Data and Execution

Execution should receive only the information required by the Action Contract and integration.

Trust Context
      ↓
approved Action
      ↓
minimal execution payload
      ↓
enterprise system

This reduces accidental data propagation.

⸻

59. Data and Outcome Verification

Outcome verification may require retrieving Business State after execution.

That retrieval must itself respect:

authorization
purpose
tenant
data scope
freshness

Outcome verification is not an unrestricted read operation.

⸻

60. Data Boundary Failure

If required data cannot be accessed within policy:

required data
    ↓
access denied

Noema should not attempt to bypass the restriction through:

another integration
model inference
cached private data
historical memory

Instead, the execution journey should transition according to policy:

CLARIFY
ESCALATE
REJECT
HOLD

⸻

61. Missing Data vs Restricted Data

These should remain distinguishable.

MISSING:
data does not exist or cannot be found
RESTRICTED:
data exists but Noema is not authorized to access it

The appropriate response may differ.

⸻

62. Inferred Data vs Restricted Data

Noema must not infer restricted information from unrelated accessible information merely to bypass the boundary.

Example:

Restricted:
employee_salary
Accessible:
employee_role
employee_department

The model should not attempt to reconstruct salary from indirect clues.

⸻

63. Data Boundary Violations

Potential violations include:

cross-tenant access
unauthorized model exposure
secret leakage
sensitive logging
unapproved external transmission
direct database access
context leakage
improper retention

Such violations should be detectable and auditable.

⸻

64. Data Boundary as a Trust Constraint

For consequential execution:

Data Boundary
      ↓
Is required information legally and technically available?
      ↓
YES → continue
NO  → policy-defined alternative

Noema should never treat unauthorized access as a technical inconvenience that can simply be worked around.

⸻

65. Canonical Data Flow

                ENTERPRISE
                     │
                     │
              Authoritative Data
                     │
                     ▼
             Data Boundary
                     │
           ┌─────────┴─────────┐
           ▼                   ▼
        Context              Evidence
           │                   │
           └─────────┬─────────┘
                     ▼
                  Trust
                     │
                     ▼
                   Action
                     │
             Minimal Payload
                     │
                     ▼
                Execution
                     │
                     ▼
                Enterprise
                     │
                     ▼
             Business State
                     │
                     ▼
                 Outcome

⸻

66. Canonical Invariants

Invariant 1

Enterprise data remains owned by the enterprise.

Invariant 2

Noema must access only data required for the current execution journey.

Invariant 3

Access does not imply ownership.

Invariant 4

Business State must remain authoritative in the enterprise system of record.

Invariant 5

Derived data must remain distinguishable from authoritative data.

Invariant 6

Model-generated information must not become authoritative Business State without appropriate validation and authority.

Invariant 7

Tenant boundaries must be enforced across all data flows.

Invariant 8

Actor authorization must constrain data exposure.

Invariant 9

Sensitive enterprise data must not enter logs or telemetry indiscriminately.

Invariant 10

Secrets must have a stronger boundary than ordinary enterprise data.

Invariant 11

Data crossing external integration boundaries must be explicitly authorized.

Invariant 12

Model prompts are data-processing boundaries and must obey enterprise data policies.

Invariant 13

Data required for Trust must be authorized before being used as evidence.

Invariant 14

Data freshness must be considered when stale information could affect consequential decisions.

Invariant 15

Restricted data must not be reconstructed through inference or indirect information.

Invariant 16

Missing data and unauthorized data access must remain distinguishable.

Invariant 17

Context from one Intent must not automatically leak into another Intent.

Invariant 18

Auditability must not justify indiscriminate data retention.

Invariant 19

Sensitive payloads may be removed while preserving the minimal historical facts necessary for auditability.

Invariant 20

Noema must not bypass enterprise data boundaries merely because required information is technically obtainable elsewhere.

⸻

67. Final Definition

Data Boundaries define the limits within which Noema may access, process, derive, transmit, retain, and expose enterprise data. They preserve enterprise ownership and authority while allowing Noema to obtain the minimum relevant information required to resolve Intent, evaluate Trust, construct Actions, execute them, and verify Outcomes.

The central architectural rule is:

                 ENTERPRISE
                      │
               owns the data
                      │
                      ▼
               DATA BOUNDARY
                      │
             minimum necessary
                      │
                      ▼
                   NOEMA
                      │
       understands → trusts → executes
                      │
                      ▼
               DATA BOUNDARY
                      │
                      ▼
                 ENTERPRISE

Noema should have enough data to act safely, but never so much authority over data that it becomes the enterprise’s uncontrolled data plane.