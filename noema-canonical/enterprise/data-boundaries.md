Data Boundaries

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/data-boundaries.md

⸻

1. Definition

Data Boundaries define what enterprise data Noema may access, what it may retain, what it may transform, what it may expose, and where authority over that data remains.

Data Boundaries prevent Noema from becoming an uncontrolled data aggregation layer.

The fundamental rule is:

Noema may access data necessary to understand, evaluate, and execute Intent, but access does not imply ownership, authority, or truth.

⸻

2. Purpose

Noema operates across enterprise systems.

Those systems may contain:

* customers
* accounts
* transactions
* employees
* permissions
* documents
* financial records
* operational data
* internal policies

Noema therefore needs explicit boundaries around:

* what enters Noema
* what remains external
* what can be persisted
* what can be shared
* what can be derived
* who can access it
* how long it remains available
* what authority the data carries
* what claims the data may support

⸻

3. Core Principle

Noema should ingest the minimum data necessary to perform the current Intent safely and reliably.

This is the principle of data minimization.

Noema should not follow:

“If we can access it, we should ingest it.”

It should follow:

“If the execution journey requires it, retrieve it within the applicable authority, authorization, purpose, tenant, and policy boundaries.”

Data minimization does not mean shallow investigation. A read-only operation may legitimately require deep cross-system investigation and State Reconciliation when that investigation is necessary to establish the current state safely.

⸻

4. Data Ownership and Authority

The enterprise remains authoritative for enterprise Business State.

Enterprise
│
├── owns customer data
├── owns financial data
├── owns transaction data
├── owns employee data
└── owns operational data

Noema may process representations and observations of that data without becoming its owner or authoritative system of record.

Authority is claim-specific. A source may provide an observation without being authoritative for every claim that can be derived from that observation.

⸻

5. Enterprise Data vs Noema Execution-Domain Data

Noema must distinguish enterprise domain data from its own execution-domain data.

Enterprise domain data includes:

* account balances
* transaction state
* customer records
* employee records
* inventory
* permissions
* enterprise resources

Noema execution-domain data includes:

* Intent Objects
* Trust Decisions
* Action selections
* Execution records
* reconciliation state
* execution outcomes
* operational case history
* causal audit records

Noema may own canonical execution-domain state without becoming the canonical owner of enterprise Business State.

This distinction is foundational.

⸻

6. Data Categories

Conceptually, Noema interacts with several categories:

* Intent Data
* Context Data
* Evidence
* Business State
* Observations
* Reconciled Facts
* Fact Status
* Action Data
* Trust Data
* Execution Data
* Outcome Data
* Audit Data
* Integration Data
* Operational Memory
* Secrets

These categories have different authority, retention, sensitivity, and lifecycle requirements.

⸻

7. Intent Data

Intent Data represents the semantic request produced from a Source of Intent.

Examples:

"Refund my last payment."
"Block my card."
"Give Sarah access to the project."

Intent Data may contain sensitive information and must be handled according to enterprise policy.

An Intent Object is not enterprise Business State and does not itself grant authority to perform an action.

Once an Intent Object is admitted to Trust, its semantic meaning is immutable. A material change creates a new Intent version with explicit lineage through supersedes.

⸻

8. Context Data

Context Data is information gathered to interpret, resolve, evaluate, execute, or verify an Intent.

Examples:

* customer status
* account state
* resource ownership
* permissions
* transaction history
* organizational relationships

Context should be scoped to the current Intent wherever possible.

Context is not inherently authoritative. Its admissibility and permitted use depend on:

* authorization
* source
* relevance
* schema validity
* authority
* temporal validity
* Fact Status
* tenant and actor scope

⸻

9. Observations

An Observation is a representation of something Noema received or observed from an enterprise system or integration.

Examples:

Ledger API:
balance = 5000
Payment API:
status = PENDING
Switch event:
transaction_id = tx_123
status = SUCCESS

An Observation is not automatically Business State.

It must pass the applicable schema and admission boundary before it becomes eligible for semantic processing.

Observation persistence does not confer authority.

⸻

10. Hard Schema Validation and Admission

External data entering Noema must cross a hard schema validation and admission boundary before it is treated as usable canonical input.

Conceptually:

External Source
      ↓
Raw Observation / Payload
      ↓
Hard Schema Validation
      ↓
Admission
      ↓
Semantic Classification / Reconciliation

The boundary applies to data received through:

* APIs
* events
* integrations
* tool responses
* external services
* model-generated structured data
* user-provided structured information

Schema validation establishes structural validity.

It does not by itself establish:

* authority
* freshness
* correctness
* authorization
* Fact Status
* enterprise truth

⸻

11. Evidence

Evidence supports claims, Trust decisions, reconciliation, or auditability.

Examples:

* authorization result
* policy version
* account observation
* identity verification result
* risk signal
* enterprise API response
* event observation

Evidence should retain enough provenance to establish what was observed, from where, when, under what version, and how it was used.

Evidence is not synonymous with Fact Status.

⸻

12. Fact Status

Fact Status classifies the current epistemic status of a claim or reconciled fact.

Canonical values are:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

* Evidence
* Context
* Business State
* Outcome
* model confidence

For example:

Evidence:
Ledger response received at 10:32.
Claim:
account.balance = 5000
Fact Status:
VERIFIED

The evidence supports the claim; Fact Status describes the status of the claim.

Model confidence must never be treated as Fact Status.

⸻

13. Business State

Business State belongs to the enterprise.

Noema may observe:

account.balance = 5000

but should not assume:

Noema owns account.balance

The authoritative value remains in the enterprise system of record.

Business State is distinct from Noema’s knowledge of Business State.

For example:

Enterprise truth:
refund.status = SUCCEEDED
Noema knowledge:
UNKNOWN

until an authoritative observation is received and reconciled.

What is true, what Noema has observed, and what Noema has inferred are separate concepts.

⸻

14. Temporal State

Business State must be interpreted with temporal semantics.

Temporal State answers questions such as:

* what was true?
* when did it become effective?
* when did the enterprise observe it?
* when did Noema observe it?
* what is currently believed to be true?
* which observation applies to the requested point in time?

A historical observation does not become current Business State merely because Noema retained it.

Temporal semantics therefore remain distinct from Business State itself.

⸻

15. State Reconciliation

State Reconciliation is a first-class Noema capability.

Its purpose is to reconcile observations from enterprise systems into explicit claims about relevant current or historical state.

Canonical flow:

Enterprise Systems of Record
        ↓
Observations
        ↓
Hard Schema Validation / Admission
        ↓
State Reconciliation
        ↓
Reconciled Facts / Fact Status / Evidence
        ↓
Temporal Context
        ↓
Trust

State Reconciliation considers, where applicable:

* source authority
* temporal validity
* resource identity
* version
* ordering
* freshness
* consistency
* conflicting observations
* eventual consistency
* missing observations
* enterprise-specific reconciliation rules

State Reconciliation does not transfer ownership of Business State to Noema.

⸻

16. Canonicality Is Scoped

“Canonical” must always be interpreted within a defined scope.

A value may be canonical for:

* a particular enterprise claim
* a particular domain
* a particular resource
* a particular field
* a particular tenant
* a particular time
* a particular authority model

Noema’s canonical execution-domain data is separate from enterprise Business State.

Noema must never treat “canonical inside Noema” as equivalent to “authoritative inside the enterprise.”

⸻

17. Action Data

Action Data describes what Noema is permitted to cause in the enterprise.

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

An Action does not create authority merely because the target or parameters were obtained from Business State.

⸻

18. Trust Data

Trust Data includes:

* Trust evaluation
* policy references
* evidence references
* authorization evaluation
* risk evaluation
* decision
* evaluated conditions
* decision context

Trust Data should be durable enough to explain consequential decisions.

A Trust Decision must preserve the semantic and policy versions relevant to the decision.

⸻

19. Execution Data

Execution Data describes what Noema attempted and what occurred during execution.

Examples:

* execution ID
* execution attempt
* execution state
* provider
* request reference
* response status
* failure
* retry
* completion
* unknown state
* verification state

Execution Data belongs to Noema’s execution record.

An execution record does not establish enterprise Business State by itself.

⸻

20. Outcome Data

Outcome Data describes the observed result of an Action.

For example:

Expected:
card frozen
Observed:
enterprise system reports card.status = FROZEN

Outcome is distinct from Business State.

Outcome verification may establish that an enterprise state transition occurred, but the underlying Business State remains authoritative in the enterprise.

Trust EXECUTE is also distinct from Outcome:

EXECUTE
≠
SUCCESS

EXECUTE means the action is permitted to proceed under the evaluated Trust conditions. It does not mean the enterprise action succeeded.

⸻

21. Audit Data

Audit Data provides the historical record of consequential behavior.

It may reference:

* Intent
* exact Intent version
* Action
* Trust Decision
* Execution
* Outcome
* Actor
* Policy
* Evidence
* observations
* reconciliation
* relevant contract and graph versions

Audit Data should not automatically contain every raw payload involved in execution.

Auditability means causal traceability, not indiscriminate data retention or private model chain-of-thought.

⸻

22. Integration Data

Integration Data exists at the boundary between Noema and external systems.

Examples:

* API request metadata
* provider request ID
* provider response ID
* event ID
* schema version
* integration version
* resource version
* correlation ID

Sensitive credentials and secrets must not be treated as ordinary integration data.

⸻

23. Secrets

Secrets have a separate security boundary.

Examples:

* API keys
* OAuth tokens
* client secrets
* private keys
* database credentials
* signing keys

Noema should reference secret material through appropriate secret-management mechanisms rather than embedding secrets into Intent, Context, Action, Trust, or Audit records.

The model must never receive enterprise credentials as ordinary Context.

⸻

24. Data Flow Boundary

The canonical data flow is:

Enterprise Systems of Record
        │
        │ authorized access
        ▼
Observations
        │
        ▼
Hard Schema Validation / Admission
        │
        ▼
State Reconciliation
        │
        ▼
Reconciled Facts / Fact Status / Evidence
        │
        ▼
Temporal Context
        │
        ▼
Deterministic Trust
        │
        ▼
Action / Execution
        │
        │ authorized invocation
        ▼
Enterprise Systems of Record

Noema execution-domain state exists alongside this flow and must not be confused with enterprise Business State.

⸻

25. Read Boundary

Noema should only read enterprise data required for the current execution journey.

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

Where deeper investigation is necessary for safe resolution, the additional reads must still remain within the applicable authorization, purpose, tenant, and data boundaries.

⸻

26. Write Boundary

Noema should only cause enterprise state changes through approved interfaces.

Preferred:

Noema
   ↓
Action Contract
   ↓
Enterprise Capability / API
   ↓
Business State

Avoid:

Noema
   ↓
Direct database mutation

unless explicitly supported and governed by the enterprise architecture.

Noema must not establish a shadow canonical business ledger.

⸻

27. Transformation Boundary

Noema may transform enterprise data into forms required for:

* Intent resolution
* Context
* State Reconciliation
* Trust
* Action construction
* Outcome verification

Transformation does not transfer authority.

Example:

Enterprise:
employee.role = "finance_manager"
Noema:
authorization_context = "may_approve_invoice"

The latter is a derived representation, not necessarily a new authoritative enterprise fact.

⸻

28. Derived Data

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

A derived value may be useful for decision-making without becoming enterprise truth.

⸻

29. Model-Generated Data

Model output is untrusted derived data.

Examples:

* interpreted Intent
* candidate entities
* extracted parameters
* semantic classification
* candidate actions
* model confidence

Model-generated information must not automatically cross the boundary into:

* authoritative Business State
* authoritative Fact Status
* enterprise authority
* execution authorization

The model may propose. Deterministic Noema components validate, reconcile, govern, and constrain.

⸻

30. Data Provenance

Important data used for consequential decisions should preserve provenance.

Conceptually:

Claim / Data
     ↓
Source
     ↓
Authority
     ↓
Observed At
     ↓
Applicable Version
     ↓
Reconciliation
     ↓
Fact Status
     ↓
Used By

This is particularly important for Trust and causal Auditability.

⸻

31. Source Authority

Noema should know where a piece of data came from and what authority that source has for the relevant claim.

For example:

balance
  → Ledger
identity
  → Identity Provider
subscription status
  → Billing System

Source and authority are distinct.

A source can provide useful evidence without being authoritative for every semantic claim derived from its response.

Authority must therefore be claim-specific and enterprise-defined.

⸻

32. Conflicting Data

If two sources disagree:

System A:
ACTIVE
System B:
SUSPENDED

Noema must not silently select one.

State Reconciliation should evaluate:

* source authority
* policy
* temporal validity
* freshness
* resource identity
* version
* operation risk
* reconciliation rules

If the conflict cannot be safely resolved, the resulting Fact Status may be:

CONFLICTED

and the execution journey may require:

CLARIFY
ESCALATE
REJECT

depending on the applicable Trust policy.

⸻

33. Data Freshness

Data has temporal validity.

A relevant observation should conceptually carry:

observed_at
source
authority
resource_version
freshness

where applicable.

For high-risk execution:

stale data
    ↓
may invalidate current Trust conditions
    ↓
reconcile / revalidate

Recency does not equal authority.

A newer observation from a lower-authority source does not automatically supersede an older authoritative observation.

⸻

34. Data at Rest

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

Retention, encryption, access, deletion, and residency requirements should follow that classification.

⸻

35. Data in Transit

Enterprise data crossing into or out of Noema should use approved secure transport mechanisms.

The exact transport is implementation-specific.

The invariant is:

Sensitive enterprise data must not cross integration boundaries without appropriate protection and authorization.

⸻

36. Tenant Boundary

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

Data from one tenant must not become Context, Evidence, Operational Memory, or derived knowledge for another tenant unless explicitly authorized by the applicable enterprise architecture.

⸻

37. Actor Boundary

Data access may depend on the Actor.

Actor A
   ↓
authorized Context
Actor B
   ↓
different authorized Context

The same enterprise resource may expose different information to different actors.

Actor identity must therefore be resolved sufficiently before consequential data access or disclosure.

⸻

38. Purpose Limitation

Data access should have a purpose.

Conceptually:

Intent
   ↓
Purpose
   ↓
Required Data
   ↓
Authorization / Data Boundary
   ↓
Access

If data is unrelated to the current purpose, it should generally not be retrieved merely because it is available.

Purpose does not override authorization or enterprise policy.

⸻

39. Context Isolation

Context gathered for one Intent should not automatically leak into another.

For example:

Intent A
  ↓
private customer information

must not automatically become:

Context for Intent B

without appropriate authorization, relevance, tenant scope, actor scope, and purpose.

⸻

40. Cross-Intent Memory

Historical information can sometimes be useful.

However, reusing it requires considering:

* relevance
* freshness
* authorization
* tenant
* actor
* purpose
* sensitivity
* temporal applicability
* authority

Operational Memory is not a bypass around data boundaries.

Historical retention does not make old information current Business State.

⸻

41. Cross-System Boundary

A single Intent may involve multiple enterprise systems.

Example:

CRM
 ↓
Payment System
 ↓
Inventory
 ↓
Messaging

Noema should expose each integration only to the data necessary for its Action or reconciliation responsibility.

A payment integration should not automatically receive unrelated CRM data.

Cross-system investigation must preserve the distinction between observations from different authorities.

⸻

42. Least Privilege

Noema integrations should follow least privilege.

Integration
    ↓
minimum required permissions
    ↓
minimum required data

This reduces both accidental exposure and blast radius.

Capability and data access should be separately governed.

⸻

43. Action-Specific Data Scope

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

Action requirements do not automatically authorize access to every field on the referenced resource.

⸻

44. Trust-Specific Data Scope

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

Trust inputs should also remain within the authorized data boundary.

⸻

45. Data Boundary Before Trust

The Trust Engine should evaluate only data that Noema is authorized to use.

Enterprise Data
      ↓
Authorization / Data Boundary
      ↓
Permitted Context / Evidence
      ↓
State Reconciliation where required
      ↓
Trust

Unauthorized information must not become hidden Trust evidence.

The ability to technically retrieve information does not establish permission to use it for Trust.

⸻

46. Data Boundary Before Model

The model should not receive unrestricted enterprise data.

Enterprise
    ↓
Data Boundary
    ↓
Relevant Permitted Context
    ↓
Model

This reduces unnecessary exposure and limits the model’s information surface.

The model’s ability to infer a fact does not grant permission to access or disclose the underlying information.

⸻

47. Model Context Isolation

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

Context selection remains subject to authorization, purpose, tenant, actor, sensitivity, and policy.

⸻

48. Prompt Data Is Data

Information inserted into model prompts is still enterprise data.

Therefore:

Prompt
    ≠
safe boundary

Prompt construction must respect the same data-access policies as other Noema components.

A prompt is a data-processing operation, not a security boundary.

⸻

49. Model Output Boundary

Model output should be treated as untrusted derived data until validated.

Model
 ↓
Candidate Intent / Action / Data
 ↓
Hard Schema Validation
 ↓
Resolution / Reconciliation
 ↓
Trust
 ↓
Execution

A model cannot bypass data or authorization boundaries merely by producing a structured Action or claiming authorization.

⸻

50. Data Exfiltration Boundary

Noema must prevent enterprise data from being unintentionally sent to:

* external models
* third-party APIs
* logging systems
* analytics systems
* telemetry providers

unless explicitly authorized.

External processing is itself a data-boundary crossing and must be governed accordingly.

⸻

51. Logging Boundary

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

Logs are not exempt from enterprise data policy.

⸻

52. Audit Boundary

Auditability requires evidence, but auditability does not require storing every payload.

The correct principle is:

Maximum causal explainability within minimum necessary data retention.

Audit records should preserve enough information to reconstruct:

claim
  ↓
source / authority
  ↓
observation
  ↓
validation / admission
  ↓
reconciliation
  ↓
Fact Status
  ↓
Trust Decision
  ↓
Action / Execution
  ↓
Verification
  ↓
Outcome

Private model chain-of-thought is not required.

⸻

53. Redaction

Sensitive fields may need to be:

* redacted
* masked
* tokenized
* hashed
* encrypted
* excluded

depending on their purpose and sensitivity.

Example:

card_number:
**** **** **** 1234

rather than storing the full number.

Redaction must not destroy the minimum information required for causal auditability or safe reconciliation.

⸻

54. Data Retention

Different data classes may have different retention periods.

Example:

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

Retention must respect legal, regulatory, contractual, security, and operational requirements.

⸻

55. Deletion

Deletion must account for dependencies.

Deleting an Intent payload should not necessarily destroy the fact that:

an execution occurred

The audit record may retain a minimal reference while the sensitive payload is removed.

Deletion of a representation in Noema must not be confused with deletion of the underlying enterprise Business State.

⸻

56. Referential Integrity After Deletion

Noema should support references that survive data minimization where necessary.

For example:

Intent:
ID 123
payload:
deleted
Audit:
Intent 123 produced Action 456

The system can retain the execution fact without retaining the original sensitive content indefinitely.

References must remain scoped and must not become a mechanism for retaining prohibited sensitive information indirectly.

⸻

57. Data Residency

Enterprise requirements may constrain where data is processed or stored.

Noema’s data architecture should support enterprise-defined:

* region
* jurisdiction
* storage location
* processing location
* model location

where applicable.

Residency requirements apply to derived and cached representations as well as raw enterprise data when enterprise policy requires it.

⸻

58. External Model Providers

If Noema uses an external model provider, enterprise data crossing that boundary must be governed explicitly.

The integration must establish:

* what data is sent
* why it is sent
* under whose authority it is sent
* where it is processed
* how it is retained
* who can access it
* whether the provider may retain or reuse it

External model use does not relax enterprise data boundaries.

⸻

59. Self-Hosted Models

Self-hosted models can reduce some external data-boundary concerns but do not eliminate them.

Enterprise data still requires:

* access control
* tenant isolation
* retention rules
* model-context isolation
* auditability
* purpose limitation
* least privilege

A model hosted inside the enterprise boundary is still an untrusted computational component with respect to consequential execution semantics.

⸻

60. Data Classification

Noema should support enterprise-defined classifications.

For example:

PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED

The exact taxonomy is enterprise-specific.

Data classification can influence:

* model access
* storage
* logging
* retention
* sharing
* external processing
* execution
* audit

Classification does not itself establish authority or Fact Status.

⸻

61. Data and Policy

Policy may constrain data usage.

Example:

Policy:
Customer financial data may only be accessed
for payment-related operations.

Noema must treat that policy as a Trust and data-access constraint.

A policy may restrict otherwise technically available information.

⸻

62. Data and Authorization

Authorization determines whether an Actor or Noema integration may access data.

Actor
 ↓
Authorization
 ↓
Data Boundary
 ↓
Context

Authorization should precede exposure.

Technical access, policy permission, and business authorization remain distinct concepts.

⸻

63. Data and Capability

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

Data access without an appropriate capability does not create an executable operation.

⸻

64. Data and Trust

Trust should consider whether the information used in a consequential decision was:

* authorized for use
* authoritative for the claim
* relevant
* fresh enough
* schema-valid
* reconciled where necessary
* complete enough for the decision

Therefore Data Boundaries directly influence Trust.

Trust must not manufacture missing authority from available data.

⸻

65. Data and Execution

Execution should receive only the information required by the Action Contract and integration.

Permitted Trust Context
      ↓
approved Action
      ↓
minimal execution payload
      ↓
enterprise system

This reduces accidental data propagation.

The executor must not accept arbitrary model-generated fields outside the Action Contract.

⸻

66. Data and Outcome Verification

Outcome verification may require retrieving Business State after execution.

That retrieval must itself respect:

* authorization
* purpose
* tenant
* actor
* data scope
* freshness
* source authority

Outcome verification is not an unrestricted read operation.

If the authoritative state cannot be established, the outcome may remain UNKNOWN rather than being inferred from a timeout or incomplete response.

⸻

67. Data Boundary Failure

If required data cannot be accessed within policy:

required data
    ↓
access denied

Noema should not attempt to bypass the restriction through:

* another unauthorized integration
* model inference
* cached private data
* historical memory
* indirect reconstruction

Instead, the execution journey should transition according to applicable policy:

CLARIFY
ESCALATE
REJECT

An operational hold or revalidation state may exist in the execution lifecycle, but it is not a fifth Trust outcome.

⸻

68. Missing Data vs Restricted Data

These should remain distinguishable.

MISSING:
data does not exist, is unavailable, or cannot currently be established
RESTRICTED:
data exists but Noema or the relevant Actor is not authorized to access it

The appropriate response may differ.

UNKNOWN should be used where the truth cannot safely be established rather than silently classifying the condition as missing or false.

⸻

69. Inferred Data vs Restricted Data

Noema must not infer restricted information from unrelated accessible information merely to bypass the boundary.

Example:

Restricted:
employee_salary
Accessible:
employee_role
employee_department

The model should not attempt to reconstruct salary from indirect clues.

Inference is not an authorization mechanism.

⸻

70. Data Boundary Violations

Potential violations include:

* cross-tenant access
* unauthorized model exposure
* secret leakage
* sensitive logging
* unapproved external transmission
* direct database access
* context leakage
* improper retention
* unauthorized inference
* use of restricted information
* failure to preserve source authority

Such violations should be detectable and auditable.

⸻

71. Data Boundary as a Trust Constraint

For consequential execution:

Data Boundary
      ↓
Is required information legally,
technically, and policy-wise available?
      ↓
YES → continue
NO  → policy-defined alternative

Noema should never treat unauthorized access as a technical inconvenience that can simply be worked around.

Data availability is not equivalent to data authority.

⸻

72. Recovery and Revalidation

Unknown execution state may require additional Business State reads.

Canonical recovery flow:

Historical Execution State
        ↓
External Operation State
        ↓
Current Authoritative Observation
        ↓
State Reconciliation
        ↓
Fact Status
        ↓
Revalidate Trust / Preconditions
        ↓
Continue / Clarify / Escalate / Reject

Revalidation is a new evaluation against current state.

It must not silently mutate the historical Trust Decision or historical observation that produced the earlier execution attempt.

⸻

73. Intent and Data-Boundary Lineage

Consequential data access should preserve the semantic context that justified the access.

Where applicable, the record should retain:

* Source of Intent
* exact Intent Object version
* resolved Actor
* resolved Action
* resolved Target/Resource
* tenant and scope
* data-access purpose
* relevant authorization
* integration/capability identity
* relevant policy version
* relevant contract version

A material clarification or change to Intent creates a new Intent version with supersedes.

Historical access decisions remain associated with the Intent version under which they were made.

⸻

74. Planner and Data Boundaries

The Planner may select among permitted execution paths but cannot expand data authority.

The Planner cannot:

* invent a capability
* invent authorization
* select an unauthorized data source
* bypass Data Boundaries
* access restricted information through another capability
* modify Action Contract semantics
* treat model inference as enterprise authority

The Planner operates within the Enterprise Action Graph, Capability Registry, Action Contracts, Trust Decision, and applicable data-access constraints.

⸻

75. Replay and Historical Data

Replaying an observation or event is non-executing by default.

Replay must not:

* create a new enterprise occurrence
* mutate historical Business State
* silently create a new Trust Decision
* silently create a new Outcome

Modern reevaluation of historical data is a distinct operation and must be explicitly identified as such.

Historical data remains historical evidence unless reconciled under the applicable temporal and authority rules.

⸻

76. Operational Memory

Operational Memory may retain structured information about:

* previous execution attempts
* cases
* failures
* recovery
* reconciliations
* outcomes
* relevant enterprise observations

Operational Memory is not:

* enterprise Business State
* an enterprise system of record
* generic AI memory
* an authority bypass
* a substitute for current authoritative observation

Historical operational knowledge must be revalidated when current Business State matters.

⸻

77. Canonical Causal Data Flow

The canonical relationship is:

Enterprise Systems of Record
        ↓
Authoritative Domain Data
        ↓
Observations
        ↓
Hard Schema Validation / Admission
        ↓
State Reconciliation
        ↓
Reconciled Facts
        ↓
Fact Status / Evidence
        ↓
Temporal Context
        ↓
Deterministic Trust
        ↓
Action / Execution
        ↓
Verification
        ↓
Outcome
        ↓
Operational Memory / Causal Audit

Separately:

Noema Execution-Domain State
        ↓
Intent
Trust
Action
Execution
Reconciliation State
Outcome
Operational Memory
Audit

Noema’s execution-domain state supports enterprise execution without becoming the authoritative enterprise Business State.

⸻

78. Canonical Invariants

Invariant 1

Enterprise Business State remains authoritative in the enterprise systems of record.

Invariant 2

Noema may process representations of enterprise data without becoming its owner.

Invariant 3

Enterprise Business State and Noema execution-domain state must remain distinct.

Invariant 4

Noema must access only data required for the applicable execution journey.

Invariant 5

Access does not imply ownership or authority.

Invariant 6

External data must cross the applicable hard schema validation and admission boundary before becoming usable canonical input.

Invariant 7

Persistence does not confer authority.

Invariant 8

State Reconciliation is a first-class capability and must not be collapsed into generic Context handling.

Invariant 9

Observations must remain distinguishable from Business State.

Invariant 10

Evidence must remain distinguishable from Fact Status.

Invariant 11

Fact Status must use explicit epistemic semantics and must not be replaced by model confidence.

Invariant 12

Canonicality must always be scoped to a claim, domain, resource, field, authority, tenant, and/or temporal context as applicable.

Invariant 13

Source, authority, freshness, authorization, and relevance are distinct properties.

Invariant 14

A newer observation does not automatically supersede an older authoritative observation.

Invariant 15

Historical observations and snapshots do not become current Business State merely because Noema retained them.

Invariant 16

Derived data must remain distinguishable from authoritative enterprise facts.

Invariant 17

Model-generated information must remain untrusted unless it passes the applicable deterministic validation and governance boundaries.

Invariant 18

Model confidence is not Fact Status.

Invariant 19

Model output must never create enterprise authority.

Invariant 20

Tenant boundaries must be enforced across all data flows.

Invariant 21

Actor authorization must constrain data exposure.

Invariant 22

Sensitive enterprise data must not enter logs or telemetry indiscriminately.

Invariant 23

Secrets must have a stronger boundary than ordinary enterprise data.

Invariant 24

Data crossing external integration boundaries must be explicitly authorized.

Invariant 25

Model prompts are data-processing boundaries and must obey enterprise data policies.

Invariant 26

Data required for Trust must be authorized before being used as evidence.

Invariant 27

Data freshness must be considered when stale information could affect consequential decisions.

Invariant 28

Restricted data must not be reconstructed through inference or indirect information.

Invariant 29

Missing data and unauthorized data access must remain distinguishable.

Invariant 30

Context from one Intent must not automatically leak into another Intent.

Invariant 31

Auditability must not justify indiscriminate data retention.

Invariant 32

Sensitive payloads may be removed while preserving the minimal historical facts necessary for causal auditability.

Invariant 33

Noema must not bypass enterprise data boundaries merely because required information is technically obtainable elsewhere.

Invariant 34

Intent versions used for consequential operations must remain identifiable and immutable after admission to Trust.

Invariant 35

A material Intent change must create a new Intent version rather than silently mutating the historical Intent.

Invariant 36

Consequential operations must preserve sufficiently resolved Actor, Action, Target/Resource, and scope identity.

Invariant 37

The Planner cannot create authority, invent capabilities, expand data access, or bypass Trust and Action Contracts.

Invariant 38

Trust EXECUTE means that an action is permitted to proceed under evaluated conditions; it does not establish business success.

Invariant 39

Outcome is distinct from Business State.

Invariant 40

Unknown must remain explicit when current truth, state, availability, or execution result cannot safely be established.

Invariant 41

Timeout must not automatically be classified as business failure or success.

Invariant 42

Unknown execution must trigger reconciliation and revalidation before a consequential retry or continuation.

Invariant 43

Revalidation must not silently mutate historical Trust Decisions or historical observations.

Invariant 44

Replay of observations or events is non-executing by default and must not create new enterprise occurrences.

Invariant 45

Operational Memory must not become an alternative enterprise system of record or authority bypass.

Invariant 46

Read-only operations may still require Trust when they expose protected data or perform consequential investigation.

Invariant 47

Noema must preserve causal lineage from claim through source, observation, validation, reconciliation, Fact Status, Trust, execution, verification, and Outcome where applicable.

Invariant 48

Data-boundary controls apply equally to raw enterprise data, derived data, cached data, historical data, model context, and external processing.

⸻

79. Final Definition

Data Boundaries define the limits within which Noema may access, process, derive, transmit, retain, and expose enterprise data.

They preserve enterprise ownership and authority while allowing Noema to obtain the minimum relevant information required to resolve Intent, reconcile relevant Business State, evaluate Trust, construct Actions, execute them, and verify Outcomes.

The central architectural rule is:

                 ENTERPRISE
                      │
              owns Business State
                      │
                      ▼
                DATA BOUNDARY
                      │
             authorized minimum
                      │
                      ▼
                 OBSERVATIONS
                      │
                      ▼
          SCHEMA VALIDATION / ADMISSION
                      │
                      ▼
             STATE RECONCILIATION
                      │
                      ▼
              NOEMA CONTEXT / TRUST
                      │
       understands → trusts → executes
                      │
                      ▼
                DATA BOUNDARY
                      │
                      ▼
                 ENTERPRISE

Noema should have enough data to act safely and deterministically, but never so much uncontrolled data authority that it becomes the enterprise’s competing system of record or uncontrolled data plane.