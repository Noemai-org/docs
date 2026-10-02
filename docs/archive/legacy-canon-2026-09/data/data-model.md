> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Data Model

Status: Foundational
Version: 0.1
Domain: Data
Canonical Path: data/data-model.md

⸻

1. Definition

The Noema Data Model defines the semantic structure, relationships, provenance, authority, temporal meaning, and lifecycle of information used to resolve Intent, reconcile enterprise state, evaluate Trust, execute Actions, and verify Outcomes.

The Data Model answers:

“What kinds of information does Noema operate on, how are they related, what does each piece of information mean, and what authority does it have?”

It is not simply a database schema.

The Data Model is the semantic contract underlying Noema’s data layer.

It defines meaning without requiring Noema to become the owner or System of Record for enterprise Business Data.

⸻

2. Purpose

Noema operates across enterprise systems that each have their own:

* schemas
* identifiers
* APIs
* databases
* event models
* terminology
* state representations
* authority boundaries

Noema requires a common semantic model without requiring every enterprise system to adopt Noema’s internal storage model.

Enterprise Systems
       │
       ▼
Validated Integration / Observation
       │
       ▼
Noema Data Model
       │
 ┌─────┼────────────┐
 ▼     ▼            ▼
Intent Trust     Execution
       │
       ▼
State Reconciliation

The Data Model therefore provides the semantic bridge between heterogeneous enterprise information and deterministic Noema execution.

⸻

3. Core Principle

Noema’s Data Model represents meaning, not ownership.

Noema may represent:

* Customer
* Account
* Payment
* Employee
* Organization
* Order
* Policy
* Capability
* Action
* Execution

without becoming the System of Record for those entities.

The model provides a semantic representation that allows Noema to reason across heterogeneous enterprise systems while preserving enterprise ownership and authority.

⸻

4. Semantic Model vs Physical Schema

The Data Model should not be confused with a database schema.

Semantic Model
     ↓
defines meaning
Physical Schema
     ↓
defines storage

For example, Noema may define:

Payment.status

while one enterprise exposes:

payment_status

and another:

state

The Integration layer maps the enterprise representation into the Noema semantic model.

The semantic model defines what Payment.status means.

It does not dictate how the enterprise stores that value.

⸻

5. Data Model Layers

The Noema Data Model can be understood as several related semantic domains:

┌──────────────────────────────────┐
│          Intent Data             │
├──────────────────────────────────┤
│       Context / Fact Data        │
├──────────────────────────────────┤
│     Trust / Decision Data        │
├──────────────────────────────────┤
│       Execution Data             │
├──────────────────────────────────┤
│     Enterprise Data References   │
├──────────────────────────────────┤
│     Evidence / Observation Data  │
├──────────────────────────────────┤
│       Provenance / Lineage       │
└──────────────────────────────────┘

These layers should remain semantically distinguishable.

In particular:

Enterprise Business State
        ≠
Noema Execution State
        ≠
Context
        ≠
Evidence
        ≠
Fact Status
        ≠
Outcome

⸻

6. Core Data Categories

Noema operates on several fundamental semantic categories:

* Entity
* Resource
* Identity
* Attribute
* State
* Relationship
* Context
* Evidence
* Fact
* Fact Status
* Canonical Data
* Constraint
* Policy
* Action
* Intent
* Execution
* Outcome
* Provenance
* Observation
* Failure

These categories form the foundation of the Noema semantic model.

⸻

7. Entity

An Entity represents a distinct enterprise subject.

Examples:

* Customer
* Employee
* Organization
* Account
* Vendor

An Entity has identity and relationships with other entities.

Entity
 ├── identity
 ├── attributes
 └── relationships

An Entity representation in Noema does not imply that Noema owns the enterprise Entity.

⸻

8. Resource

A Resource represents something that can be referenced or acted upon.

Examples:

* Payment
* Order
* Account
* Invoice
* Subscription
* Card

A Resource may be associated with an Entity.

Customer
   │
   └── owns → Account

Resource identity and ownership must be resolved through appropriate enterprise information rather than inferred solely from conversational context.

⸻

9. Identity

Identity establishes what an Entity or Resource refers to.

Conceptually:

Identity {
    type
    identifier
    namespace
    source
    scope
}

Identity is critical because natural-language Intent frequently refers to Resources indirectly.

Identity must preserve sufficient scope to distinguish:

* tenants
* organizations
* environments
* namespaces
* resource domains

Identity resolution may produce candidates before a single authoritative Resource is established.

⸻

10. Attribute

An Attribute describes a property of an Entity or Resource.

Examples:

* Account.balance
* Payment.amount
* Payment.currency
* Order.status
* Employee.department

Attributes may have:

value
type
source
authority_scope
observed_at
effective_at
version
freshness
fact_status
provenance

Attribute-level authority is important because a single source may be authoritative for some attributes but not others.

⸻

11. State

State describes the condition of a Resource or Noema object at a particular point in time.

Examples:

Payment = SUCCEEDED
Account = ACTIVE
Execution = RUNNING
Intent = RESOLVED

State should be modeled explicitly rather than inferred from arbitrary fields whenever state semantics are consequential.

State must always be interpreted within an authority domain.

⸻

12. State Ownership

State belongs to an authority domain.

For example:

Enterprise:
Account.status
Noema:
Execution.status

Noema should not silently replace enterprise state with a local approximation.

Noema may maintain observations, references, reconciled representations, or cached values of enterprise state, but those representations do not become the enterprise System of Record.

⸻

13. Relationship

Relationships connect entities, resources, actions, systems, and other semantic objects.

Examples:

Customer ──owns──> Account
Account ──has──> Payment
Action ──operates_on──> Resource
Policy ──governs──> Action
System ──provides──> Capability
Intent ──refers_to──> Resource

Relationships are first-class semantic information.

Relationships may themselves have:

* source
* authority
* scope
* effective time
* expiration
* provenance

⸻

14. Context

Context is the bounded, relevant information state surrounding a particular Intent, Trust evaluation, Action, Execution, Verification, or Reconciliation operation.

Context may contain:

* identity
* entities
* resources
* states
* policy information
* evidence
* observations
* system information
* historical information
* canonical data references
* derived information

Context provides runtime grounding for the rest of the model.

Context does not itself establish authority.

⸻

15. Evidence

Evidence represents information supporting or challenging a proposition, decision, or outcome.

Conceptually:

Evidence {
    subject
    claim
    source
    observed_at
    effective_at
    authority_scope
    provenance
}

Evidence is not synonymous with truth.

Its ability to support a claim depends on:

* source
* authority
* identity
* scope
* freshness
* consistency
* temporal applicability
* reconciliation

Evidence should therefore not contain an undifferentiated confidence value as a substitute for semantic status.

⸻

16. Fact

A Fact is a semantic claim about an Entity, Resource, relationship, state, or other subject.

Examples:

Payment:123
status = SUCCEEDED
Account:456
status = ACTIVE

A Fact may be supported by one or more Evidence items and may reference Canonical Data.

A Fact is not automatically verified merely because it exists in the Data Model.

⸻

17. Fact Status

Fact Status describes the semantic status of a claim after the relevant observations, authority, freshness, and reconciliation conditions have been evaluated.

A foundational vocabulary is:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status is distinct from:

* Evidence
* Context
* Canonical Data
* model confidence
* execution state
* Outcome

For example:

Evidence:
Payment System observed status = SUCCEEDED
Fact Status:
STALE

is possible if the observation is authoritative but no longer sufficiently current for the current operation.

⸻

18. Canonical Data

Canonical Data represents an authoritative enterprise representation or claim within a defined authority boundary.

Canonicality is claim-specific.

A System of Record may be authoritative for:

Account.balance

without being authoritative for:

Customer.email

The Data Model must preserve the distinction between:

* canonical
* observed
* derived
* inferred
* cached
* historical
* user-provided
* unknown

Canonicality is not universal truth.

It is authority within a defined scope.

⸻

19. Canonical Data Reference

Noema should generally represent enterprise Canonical Data through semantic references rather than creating a shadow canonical enterprise object.

Conceptually:

CanonicalDataReference {
    claim
    subject
    attribute
    value
    source_system
    authority_scope
    observed_at
    effective_at
    source_version
    freshness
    provenance
}

This model allows Noema to preserve the semantic relationship to enterprise truth without claiming ownership of the underlying enterprise data.

⸻

20. Constraint

A Constraint limits what may be valid, permitted, or executable.

Examples:

refund.amount <= 5000
account.status = ACTIVE
transfer.currency = USD

Constraints may originate from:

* Policy
* Action Contract
* System Capability
* Business Rule
* Resource State
* Enterprise Configuration
* execution requirements

Constraints must retain their semantic source.

⸻

21. Policy

Policy determines what is permitted, required, prohibited, or conditionally allowed.

Examples:

refunds above $5,000 require approval
employees cannot modify their own payroll
transfers above $50,000 require MFA

Policy is part of the semantic model but its normative authority must come from an applicable enterprise or Noema policy source.

Policy is not simply another Context value.

The Trust Engine evaluates applicable Policy deterministically.

⸻

22. Action

An Action represents a bounded executable operation.

Examples:

* refund_payment
* freeze_card
* create_user
* transfer_funds
* cancel_order

Actions operate against Resources through explicitly registered enterprise Capabilities and Action Contracts.

Action
   ↓
Action Contract
   ↓
Capability
   ↓
Enterprise System
   ↓
Resource

An Action cannot be invented by a model at execution time.

The permitted Action surface must come from explicit Noema configuration and enterprise integration semantics.

⸻

23. Intent

Intent represents the semantic objective expressed by a Source of Intent.

A Source of Intent may be:

* human
* agent
* system
* workflow
* API/application
* enterprise event
* other registered source

Example:

“Refund my last payment.”

may resolve to:

Intent {
    objective = REFUND
    resource = Payment:123
}

An Intent is not itself an Action.

Intent represents what is requested.

Action represents what can be executed.

⸻

24. Intent vs Action

Intent:
"What is being requested?"
Action:
"What registered operation can execute that request?"

Example:

Intent:
"Get me a refund."
Action:
refund_payment(payment_id)

The Data Model preserves this distinction.

Intent does not grant execution authority.

⸻

25. Intent Version

Consequential processing must identify the exact Intent version being evaluated.

An admitted Intent is immutable.

If the semantic Intent changes:

Intent v1
      ↓
clarification / material change
      ↓
Intent v2
supersedes v1

Noema must not silently mutate the meaning of an admitted Intent.

Trust and execution records should reference the exact Intent version that they evaluate or execute.

⸻

26. Outcome

Outcome represents what Noema establishes about an attempted Action after execution and verification.

Examples may include:

* SUCCESS
* FAILED
* PARTIAL
* REQUIRES_INTERVENTION
* UNKNOWN

Outcome should be grounded in observed and reconciled execution results rather than inferred solely from Action submission.

Outcome is not the same thing as enterprise Business State.

Noema Outcome
      ≠
Enterprise Business State

⸻

27. Execution

Execution represents a concrete attempt to perform an Action.

Conceptually:

Execution {
    execution_id
    intent_version
    action
    context_reference
    state
    attempts
    outcome
    timestamps
}

Execution connects a governed Intent and Action to real-world enterprise system activity.

An Execution may have multiple attempts while retaining one logical execution identity.

⸻

28. Execution Data vs Enterprise Data

Noema must distinguish:

Enterprise Data

from:

Noema Execution Data

For example:

Enterprise:
payment.status = REFUNDED
Noema:
execution.status = COMPLETED

The two values are related but describe different semantic domains.

Noema Execution Data must not be treated as a replacement for enterprise Business State.

⸻

29. Observation

An Observation records something observed from a source at a particular time.

Conceptually:

Observation {
    subject
    claim
    value
    source
    observed_at
    effective_at
    source_version
    provenance
}

Observations are important because Noema frequently operates with information that is:

* temporally bounded
* eventually consistent
* cached
* incomplete
* conflicting

An Observation is not automatically a Fact, and a Fact is not automatically verified.

⸻

30. Provenance

Every consequential data item should have sufficient provenance.

Conceptually:

Provenance {
    source
    authority_scope
    observed_at
    effective_at
    version
    transformation
    parent_references
}

This allows Noema to determine:

“Where did this information come from, how was it transformed, and what authority did the source have?”

Provenance is essential for causal auditability.

⸻

31. Source

Source identifies where information originated.

Examples:

* CRM
* Ledger
* Payment API
* HRIS
* Event Bus
* User
* Noema
* external provider

Source and authority are distinct.

Source ≠ Authority

A source may provide information without being authoritative for that particular fact.

⸻

32. Authority

Authority determines whether a source is authoritative for a particular claim.

For example:

Source:
Analytics DB
Authority for:
reporting metrics
Authority for:
account.balance
NO

Authority is:

* claim-specific
* scope-specific
* temporal
* potentially field-level
* potentially resource-level

The Data Model must not equate source presence with authority.

⸻

33. Scope

Data must have an understood scope.

Possible dimensions include:

* tenant
* organization
* legal entity
* business unit
* environment
* system
* resource
* attribute
* namespace
* time
* purpose

Scope prevents accidental cross-boundary interpretation.

Scope must be preserved through integration, Context assembly, State Reconciliation, Trust, and Execution.

⸻

34. Temporal Data

Data may have multiple relevant timestamps:

observed_at
effective_at
created_at
updated_at
expires_at

These timestamps answer different questions.

For example:

effective_at
→ when the fact became applicable
observed_at
→ when Noema learned of the observation
expires_at
→ when the observation or representation ceases to satisfy its applicable validity requirement

Temporal semantics are essential for reconciliation and long-running execution.

⸻

35. Version

Data may be versioned.

Example:

Account
version = 42

Version information supports:

* optimistic concurrency
* revalidation
* State Reconciliation
* auditability
* causal reconstruction

Data versioning is distinct from Contract Versioning.

A source data version does not replace the semantic version of a Noema Contract.

⸻

36. Freshness

Freshness describes how current an observation or representation is relative to the requirement of an operation.

Freshness is not identical to authority.

canonical + stale

is possible.

Likewise:

fresh + non-canonical

is possible.

Freshness requirements are determined by the claim, Action, Policy, risk, and system semantics.

⸻

37. Uncertainty

The Data Model must represent uncertainty explicitly.

Possible semantic conditions include:

* KNOWN
* UNKNOWN
* AMBIGUOUS
* CONFLICTED
* STALE
* UNAVAILABLE
* INVALID

These must not be collapsed into a generic null.

Unknown is particularly important because:

UNKNOWN ≠ FAILED
UNKNOWN ≠ ABSENT
UNKNOWN ≠ FALSE

⸻

38. Derived Data

Derived information should retain its derivation semantics.

Example:

customer_risk_score

may be calculated from:

transaction_history
payment_history
account_age

The resulting value should not be mistaken for canonical enterprise data unless the enterprise explicitly defines it as authoritative.

Derived data should preserve sufficient dependency information where its use is consequential.

⸻

39. Inferred Data

Inference represents a conclusion generated from available information.

Example:

likely_account = 123

Inference should be distinguishable from verified identity:

verified_account = 123

This distinction is particularly important during Intent Resolution.

Model-generated inference is candidate information.

It is not automatically Evidence, Fact Status VERIFIED, authority, or authorization.

⸻

40. User-Provided Data

User-provided information is an important input to the Data Model.

Example:

“Use account 123.”

This creates an input claim.

It does not automatically establish:

* account 123 exists
* user owns account 123
* user is authorized to operate account 123
* account 123 is currently active

Those facts require appropriate enterprise verification.

⸻

41. Data Classification

A useful semantic classification is:

CANONICAL
OBSERVED
DERIVED
INFERRED
USER_PROVIDED
HISTORICAL
UNKNOWN

Classification should be preserved where it affects:

* Trust
* authorization
* Policy
* reconciliation
* execution
* verification
* auditability

Classification is not a substitute for Fact Status.

⸻

42. Data Dependencies

Data objects may depend on other objects.

Example:

Risk Score
   ↓ depends_on
Transaction History
   ↓ sourced_from
Ledger

Dependency relationships support:

* provenance
* recomputation
* invalidity detection
* impact analysis
* auditability

A derived value should not silently remain valid after a material dependency changes.

⸻

43. Data Lineage

Lineage represents how a value or claim was produced.

Enterprise Observation
      ↓
Transformation
      ↓
Derived Data
      ↓
Context
      ↓
Evidence
      ↓
State Reconciliation
      ↓
Trust Decision

For consequential Actions, Noema should be able to trace this path where feasible.

Lineage is about causal reconstruction, not exposing private model chain-of-thought.

⸻

44. Data Relationships

The core semantic relationships include:

Entity ──has──> Attribute
Entity ──has──> Resource
Resource ──has──> State
Resource ──related_to──> Resource
Intent ──refers_to──> Resource
Intent ──resolves_to──> Action
Action ──operates_on──> Resource
Action ──requires──> Context
Action ──requires──> Preconditions
Action ──produces──> Execution
Policy ──governs──> Action
Evidence ──supports──> Fact
Observation ──supports──> Evidence
Data ──sourced_from──> System
State ──reconciled_by──> State Reconciliation
Fact ──has_status──> Fact Status

⸻

45. The Noema Data Graph

These relationships form a semantic graph:

                    Policy
                      │
                    governs
                      ▼
Intent ───────────> Action
  │                   │
refers_to          operates_on
  │                   │
  ▼                   ▼
Resource ─────────> State
  │                   │
  │                   ▼
  │              Observation
  │                   │
  ▼                   ▼
Canonical Data ──> Evidence
                      │
                      ▼
              State Reconciliation
                      │
                      ▼
                 Fact Status
                      │
                      ▼
                    Trust
                      │
                      ▼
                  Execution
                      │
                      ▼
                   Outcome

This is not necessarily a requirement that Noema use a graph database.

It is a description of the semantic relationships that Noema must preserve.

⸻

46. Data Model and Enterprise Action Graph

The Enterprise Action Graph describes what an enterprise can do and how its capabilities, systems, resources, and actions relate.

The Data Model describes the information required to understand, govern, execute, and verify those operations.

Enterprise Action Graph
          +
Noema Data Model
          ↓
Runtime Context
          ↓
State Reconciliation
          ↓
Trust
          ↓
Execution

The two are related but distinct.

The Action Graph is structural execution knowledge.

The Data Model is semantic information structure.

⸻

47. Data Model and Integration

Integration translates enterprise-specific representations into Noema’s semantic model.

Example:

Enterprise A:

{
    payment_status: "completed"
}

Enterprise B:

{
    state: "succeeded"
}

Both may map to:

Payment.status = SUCCEEDED

The Integration layer handles translation and validation.

The Data Model defines the meaning of Payment.status.

Integration does not automatically establish that the mapped value is current or authoritative.

⸻

48. Data Model and Hard Validation

Enterprise data, events, tool responses, and external observations are untrusted inputs until they pass the appropriate validation and admission boundary.

Conceptually:

External Representation
        ↓
Integration Boundary
        ↓
Schema Validation
        ↓
Semantic Validation
        ↓
Admission
        ↓
Data Model
        ↓
Context / Reconciliation

Hard schema validation establishes structural validity.

It does not establish:

* enterprise authority
* freshness
* authorization
* Fact Status
* policy compliance
* execution permission

No free-form model output should bypass this boundary.

⸻

49. Data Model and APIs

APIs expose enterprise data and capabilities.

The Data Model determines how returned information is semantically represented.

API Response
     ↓
Integration Mapping
     ↓
Schema Validation
     ↓
Data Model
     ↓
Context

API responses should retain their source, scope, version, and relevant temporal semantics.

⸻

50. Data Model and Events

Events represent occurrences or observations.

For example:

payment.refunded

may provide an observation relevant to:

Payment.status

The event model should map cleanly into the Data Model without conflating:

Event Occurrence

with:

Current Enterprise State

State Reconciliation may need to query the authoritative enterprise source after an event to establish current state.

Event absence is not automatically proof that an occurrence did not happen.

⸻

51. Data Model and State

State is a first-class concept because Noema frequently asks:

“What is true about this Resource now?”

For example:

Account.status = ACTIVE

is semantically different from:

Account.status_changed_at = ...

State should therefore not be reduced to arbitrary event history.

Current state may require reconciliation across multiple observations.

⸻

52. Data Model and State Reconciliation

State Reconciliation is a first-class operation over Data Model information.

It determines what enterprise state can be established from available observations, authority boundaries, versions, temporal information, and consistency rules.

Observations
     │
     ├── Source A
     ├── Source B
     ├── Events
     └── Cached State
           │
           ▼
   State Reconciliation
           │
     ┌─────┼──────┐
     ▼     ▼      ▼
 Resolved Conflict Unknown
 State

Reconciliation must not invent facts or promote non-authoritative information into canonical truth.

Its result may remain:

* VERIFIED
* STALE
* CONFLICTED
* UNKNOWN

depending on the claim and available evidence.

⸻

53. Data Model and Policy

Policy may depend on Data Model values.

Example:

if transfer.amount > 50000
then approval_required

The Data Model must represent the relationship among:

* Policy
* Amount
* Action
* Principal
* Resource
* Approval Requirement
* applicable state

Trust evaluates the resulting conditions deterministically.

⸻

54. Data Model and Preconditions

Preconditions consume Data Model values.

Example:

account.status == ACTIVE

The referenced state must resolve to an appropriately authoritative and sufficiently fresh value for the Action.

If the required fact is unknown, conflicted, or otherwise insufficient, Noema must not treat the precondition as satisfied merely because a stale or inferred value exists.

⸻

55. Data Model and Postconditions

Postconditions also reference Data Model values.

Example:

payment.status == REFUNDED

The resulting state should be verified through the appropriate enterprise source or reconciliation path.

An Action response alone does not necessarily establish that the postcondition is true.

⸻

56. Data Model and Trust

Trust evaluates relationships among:

* Intent
* actor
* Action
* Resource
* data
* authority
* Policy
* evidence
* Fact Status
* state
* risk
* capabilities

The Data Model provides the semantic substrate on which Trust operates.

Trust does not create enterprise authority.

It evaluates whether the resolved operation satisfies the applicable deterministic conditions.

⸻

57. Data Model and Determinism

Deterministic execution requires explicit semantics.

For example:

balance = 10000

is insufficient without knowing:

* which account
* which currency
* which enterprise system
* which timestamp
* which tenant
* which legal entity
* which authority boundary
* what Fact Status applies

The Data Model should provide the structure necessary to answer these questions.

⸻

58. Data Model and Ambiguity

Ambiguity exists when the Data Model cannot uniquely resolve a reference.

Example:

“my account”

may map to:

Account A
Account B
Account C

Noema should preserve this ambiguity until deterministic resolution is possible.

The model may generate candidate interpretations, but candidate generation is not authoritative identity resolution.

⸻

59. Data Model and Identity Resolution

Identity resolution maps references to enterprise entities or Resources.

"John's account"
      ↓
Candidate Accounts
      ↓
Identity Resolution
      ↓
Resolved Enterprise Account

The Data Model provides the identifiers, relationships, scope, and authority metadata needed to perform that resolution.

A resolved Resource must be sufficiently specific before consequential execution.

⸻

60. Data Model and Compound Intent

Compound Intent may produce multiple Actions operating across multiple Resource types.

Example:

“Cancel my order, refund the payment, and close the account.”

may map to:

Order
  ↓
cancel_order
Payment
  ↓
refund_payment
Account
  ↓
close_account

The Data Model provides the relationships connecting these Resources.

Each Action may have distinct:

* Context requirements
* Policies
* Preconditions
* authorities
* capabilities
* execution semantics

Compound Intent does not imply that all Actions share one authority boundary.

⸻

61. Data Model and Ownership

Ownership is represented explicitly.

Example:

Customer
   │
 owns
   ▼
Account

Ownership should not be inferred solely from:

* email
* name
* phone number
* conversation history

when authoritative enterprise relationships exist.

Ownership itself is a claim whose authority is enterprise-specific.

⸻

62. Data Model and Permissions

Permission data helps determine whether a Principal may perform an Action against a Resource.

Principal
    │
    ▼
Authorization Context
    │
    ▼
Action
    │
    ▼
Resource

Permission is not inferred simply from Resource visibility.

Technical authorization, policy authorization, and business authorization remain distinct concepts.

The Data Model represents the information required to evaluate them; it does not manufacture permission.

⸻

63. Data Model and Organizational Boundaries

The Data Model must preserve organizational relationships and boundaries.

Organization
    │
    ├── Business Unit
    ├── Team
    └── Principal

These relationships can affect:

* authorization
* Policy
* Resource visibility
* Action availability
* data access

Cross-organizational relationships must be explicit rather than inferred from proximity in Context.

⸻

64. Data Model and Data Boundaries

Data access must respect:

* tenant
* organization
* legal entity
* environment
* classification
* purpose
* permission

The Data Model does not grant access merely by representing a piece of data.

A value can be canonical within an enterprise and still be unavailable to the current Noema operation.

⸻

65. Data Model and Auditability

The Data Model should support reconstructing:

* what was requested
* what Intent version was admitted
* what was known
* what was observed
* what was authoritative
* what Fact Status applied
* what state was reconciled
* what Action was selected
* what Policy applied
* what Trust decision was made
* what Execution occurred
* what was verified
* what Outcome resulted

This is essential for enterprise-grade automation.

⸻

66. Immutable Observations

Where appropriate, observations used for consequential decisions should be immutable.

Instead of:

balance = $10,000

being overwritten with:

balance = $8,000

Noema may preserve:

Observation 1:
balance = $10,000
Observation 2:
balance = $8,000

This improves:

* auditability
* temporal reasoning
* reconciliation
* causal reconstruction

Noema should not silently rewrite historical observations to match later state.

⸻

67. Data Model and Long-Running Execution

Data may change during execution.

Therefore an Execution may need to retain:

* initial Context
* Context version
* current Context
* reconciled Context
* revalidated Context
* observed changes
* relevant source versions

This allows Noema to determine whether Preconditions remain valid.

A long-running Execution must not assume that state established at T1 remains valid at T2.

⸻

68. Data Model and Reconciliation

Reconciliation compares expected, observed, and authoritative state.

Example:

Expected:
payment.status = REFUNDED
Observed:
payment.status = SUCCEEDED

The Data Model provides the common semantic representation required to identify the discrepancy.

Reconciliation may then establish:

* the expected state has not occurred
* the observed state is stale
* the sources conflict
* the execution result is unknown
* further verification is required

Reconciliation must not silently convert discrepancies into success or failure.

⸻

69. Data Model and Failure

Failures should be represented semantically rather than as arbitrary strings.

Conceptually:

Failure {
    type
    source
    phase
    retryable
    recoverable
    details
}

Failure information should preserve enough context to determine whether the failure concerns:

* Intent resolution
* Trust
* Context acquisition
* State Reconciliation
* Action execution
* verification
* integration
* enterprise availability

A timeout must not automatically be classified as a business failure.

⸻

70. Data Model and Unknown Outcomes

An Action may succeed at the enterprise boundary while Noema fails to observe the result.

Example:

Request sent
     ↓
Timeout
     ↓
Result UNKNOWN

The Data Model must support:

Outcome = UNKNOWN

rather than incorrectly recording:

Outcome = FAILED

Unknown execution state should normally trigger verification or reconciliation before a potentially duplicative retry.

⸻

71. Data Model and Idempotency

Execution records should connect Actions with their execution identity and idempotency identity.

Action
   │
   └── idempotency_key
             ↓
        Execution

This allows Noema to distinguish:

new logical execution

from:

retry / continuation of existing execution

Idempotency semantics belong to execution and Action contracts, while the Data Model provides the relationships required to represent them.

⸻

72. Data Model and Compensation

Compensation requires knowledge of:

* prior Action
* prior state
* current state
* available capabilities
* applicable Policy
* execution history

The Data Model therefore provides the semantic information required to determine whether compensation is possible.

Compensation is not a local data rewrite.

It must execute through authorized enterprise capabilities and preserve causal linkage to the original execution.

⸻

73. Data Model and Human Intervention

When Noema cannot safely continue, intervention records should reference the relevant semantic objects:

* Intent
* Intent version
* Action
* Resource
* Context
* Policy
* Evidence
* Fact Status
* Failure
* Execution
* Reconciliation result

This gives the human operator the information required to understand the case without requiring access to private model reasoning.

⸻

74. Data Model and Noema Ownership Boundary

Noema should own the semantic and execution-domain data necessary to operate its Trust and Execution systems.

The enterprise remains authoritative for enterprise Business State.

Conceptually:

Noema owns:
- Intent lifecycle
- Trust Decisions
- Execution records
- Action semantics
- execution-domain Outcomes
- intervention / case state
- operational execution history
Enterprise owns:
- Accounts
- Balances
- Payments
- Orders
- Employees
- Business transactions
- enterprise permissions
- enterprise Business State

The exact boundary is enterprise-specific.

Noema may store references, observations, evidence, and historical representations of enterprise data without becoming the canonical owner of that data.

⸻

75. Operational Memory

Operational Memory stores structured information about prior Noema operations, including:

* Intent history
* Trust decisions
* executions
* interventions
* failures
* reconciliations
* outcomes
* learned operational patterns

Operational Memory is not:

* generic AI memory
* a vector store by definition
* a replacement for enterprise Business Data
* an authority source merely because it contains historical information

Operational Memory may provide Context and historical Evidence, but its authority must remain explicitly classified.

⸻

76. Canonical Data Model Flow

The foundational relationship is:

Enterprise Systems of Record
          │
          ▼
Validated Integration / Observation
          │
          ▼
Canonical Data Reference
          │
          ▼
      Data Model
          │
          ▼
        Context
          │
          ▼
 State Reconciliation
          │
          ▼
 Evidence + Fact Status
          │
          ▼
         Trust
          │
          ▼
      Execution
          │
          ▼
      Verification
          │
          ▼
   Enterprise State

The Data Model provides the semantic bridge between enterprise truth and Noema execution.

It does not become a replacement System of Record.

⸻

77. Conceptual Core Schema

A simplified conceptual model is:

Principal
   │
   ▼
Intent
   │
   ├──────────────► Context
   │                    │
   │                    ▼
   │                 Evidence
   │                    │
   ▼                    ▼
Resource ────────► State Reconciliation
   │                    │
   ▼                    ▼
State              Fact Status
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
                      Outcome
                         │
                         ▼
                    Verification

This represents semantic relationships rather than a mandatory physical database structure.

⸻

78. Data Model and Security Boundary

The Data Model participates in Noema’s structural security boundary.

The following must be treated as untrusted until appropriately validated and admitted:

* user input
* model output
* retrieved documents
* external tool responses
* enterprise responses
* event payloads

The Data Model must not provide a path for untrusted content to become:

* enterprise authority
* Policy
* Action Contract
* authorization
* execution instruction

without an explicit deterministic admission and validation path.

The model must not receive credentials or direct enterprise access merely because data is represented in the Data Model.

⸻

79. Data Model and Model Independence

Noema’s semantic Data Model must remain independent of any particular AI model.

Models may:

* interpret Intent
* generate candidate references
* identify potential Context
* propose plans
* summarize information

But models must not define:

* enterprise authority
* canonical truth
* Fact Status
* Policy semantics
* Action Contract semantics
* execution authority

The Data Model therefore forms part of the deterministic semantic substrate surrounding probabilistic model behavior.

⸻

80. Data Model and Verification

Verification uses the Data Model to determine whether expected postconditions correspond to observed enterprise state.

Conceptually:

Action
   ↓
Execution
   ↓
Expected Postcondition
   ↓
Enterprise Observation
   ↓
State Reconciliation
   ↓
Fact Status
   ↓
Verified Outcome

An enterprise API response may be Evidence without being sufficient to establish the final Outcome.

Verification must preserve the distinction between:

* request accepted
* execution completed
* enterprise state changed
* postcondition established

⸻

81. Core Invariants

Invariant 1

The Data Model is semantic, not merely a storage schema.

Invariant 2

Noema’s semantic representation does not transfer ownership of enterprise data.

Invariant 3

Enterprise-specific schemas must be mapped into the Noema semantic model through explicit integration semantics.

Invariant 4

Entities, Resources, State, Context, Evidence, Facts, Policies, Actions, Executions, and Outcomes are distinct semantic concepts.

Invariant 5

Intent and Action must remain distinct.

Invariant 6

Enterprise Business State and Noema Execution State must remain distinct.

Invariant 7

Canonical Data must remain distinguishable from derived, inferred, cached, observed, historical, and user-provided data.

Invariant 8

Data used for consequential execution should retain sufficient provenance.

Invariant 9

Authority and source are distinct concepts.

Invariant 10

Authority and freshness are distinct concepts.

Invariant 11

Authority, availability, and authorization are distinct concepts.

Invariant 12

Fact Status must remain distinct from Evidence, Context, Canonical Data, State, Outcome, and model confidence.

Invariant 13

Unknown, ambiguous, stale, unavailable, invalid, and conflicted states must remain semantically distinguishable where consequential.

Invariant 14

Identity must include sufficient scope to prevent accidental cross-entity or cross-tenant resolution.

Invariant 15

Relationships are first-class semantic information.

Invariant 16

Temporal information must be preserved when it affects interpretation, reconciliation, or execution.

Invariant 17

Version information should be preserved when required for concurrency, validation, reconciliation, or auditability.

Invariant 18

User-provided information must not automatically become canonical enterprise data.

Invariant 19

Model inference must not automatically become canonical enterprise data, Evidence, verified Fact Status, or authority.

Invariant 20

Events must remain distinguishable from persistent or current enterprise state.

Invariant 21

Context must remain distinguishable from Business State.

Invariant 22

Policy constrains data-driven execution; data does not override Policy.

Invariant 23

Representation of data does not grant authorization to access or use it.

Invariant 24

Data access must respect enterprise organizational, tenant, legal, environmental, and purpose boundaries.

Invariant 25

Noema must not create shadow canonical representations of enterprise Business State merely for convenience.

Invariant 26

Execution data must be sufficient to connect Intent, Intent version, Context, Action, Execution, Verification, and Outcome.

Invariant 27

Unknown execution outcomes must not be incorrectly converted into failure or success.

Invariant 28

Data required for consequential execution must be revalidated when freshness or state requirements demand it.

Invariant 29

Historical observations required for auditability must not be silently overwritten.

Invariant 30

Derived data should preserve its dependency and derivation semantics where consequential.

Invariant 31

The Data Model must support deterministic reasoning without requiring the underlying model to be deterministic.

Invariant 32

The Data Model must preserve enough structure to distinguish what is known, what is authoritative, what is inferred, what is uncertain, and what changed.

Invariant 33

State Reconciliation is a first-class operation over enterprise observations and state representations.

Invariant 34

State Reconciliation must not invent canonicality or promote non-authoritative observations into enterprise truth.

Invariant 35

A canonical source may still produce a stale, unavailable, or otherwise insufficient observation for a particular operation.

Invariant 36

Hard schema validation establishes structural validity but does not establish authority, freshness, authorization, or Fact Status.

Invariant 37

Untrusted external or model-generated information must not bypass the schema validation and semantic admission boundary.

Invariant 38

Intent versions admitted to Trust are immutable; material semantic changes require a new version with explicit lineage.

Invariant 39

Trust decisions and consequential executions must preserve the exact semantic versions of the Intent and other relevant governing artifacts.

Invariant 40

Noema Outcome must not be treated as a replacement for enterprise Business State.

Invariant 41

Read-only data access may be consequential and must remain subject to authorization and data-boundary requirements.

Invariant 42

Operational Memory is not an enterprise System of Record and does not become authoritative merely by retaining historical information.

Invariant 43

Compensation must operate through authorized enterprise capabilities rather than local mutation of shadow business state.

Invariant 44

A source count or agreement among sources does not itself establish authority.

Invariant 45

Canonicality is claim-, scope-, resource-, and time-specific.

Invariant 46

The absence of a Data Model observation must not automatically be interpreted as absence of the underlying enterprise fact.

Invariant 47

Timeouts and retrieval failures must not automatically be converted into negative enterprise facts.

Invariant 48

The Data Model must preserve enough lineage to connect consequential decisions to the enterprise observations on which they depended.

Invariant 49

A Data Model representation must not silently expand the authority, scope, or semantics of the underlying enterprise data.

Invariant 50

Noema’s Data Model must remain semantically independent of any particular AI model or model provider.

⸻

82. Final Definition

The Noema Data Model is the semantic foundation through which Noema represents and relates enterprise entities, Resources, identities, state, Context, Evidence, Facts, Policies, Actions, Executions, Outcomes, observations, and provenance while preserving authority, temporal semantics, uncertainty, reconciliation, and enterprise ownership boundaries.

Its fundamental role is:

ENTERPRISE TRUTH
      │
      ▼
VALIDATED OBSERVATIONS
      │
      ▼
SEMANTIC DATA MODEL
      │
      ▼
CANONICAL DATA REFERENCES
      │
      ▼
RUNTIME CONTEXT
      │
      ▼
STATE RECONCILIATION
      │
      ▼
EVIDENCE + FACT STATUS
      │
      ▼
TRUST
      │
      ▼
EXECUTION
      │
      ▼
VERIFICATION
      │
      ▼
OBSERVED ENTERPRISE STATE

The central rule is:

Noema’s Data Model should make enterprise information understandable, reconcilable, governable, and executable without making Noema the owner of that information.