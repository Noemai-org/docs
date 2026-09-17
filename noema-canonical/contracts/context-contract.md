Context Contract

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/context-contract.md

⸻

1. Definition

A Context Contract defines the information Noema is permitted to use, required to obtain, and expected to preserve when resolving Intent, evaluating Trust, planning Actions, executing enterprise operations, and verifying Outcomes.

A Context Contract answers:

“What information is required for this decision, where may it come from, what authority does it carry, how current must it be, and under what conditions may it be used?”

Context is not simply a collection of data.

It is bounded information with explicit:

* source
* authority
* scope
* purpose
* freshness
* provenance
* access constraints
* temporal validity
* classification
* derivation semantics

The Contract establishes the boundary between information that is available to Noema and information that is valid and permitted to participate in a particular decision or execution.

⸻

2. Purpose

The purpose of the Context Contract is to prevent Noema from treating every available piece of information as equally valid for every decision.

Enterprise environments may expose:

* canonical data
* cached data
* derived data
* historical data
* events
* user-provided information
* external information
* model-generated interpretations
* operational information
* Noema execution state

The Context Contract establishes which of these may participate in a particular decision and under what conditions.

Conceptually:

Available Information
        ↓
Context Contract
        ↓
Permitted Context
        ↓
Validation / Observation
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

It may be insufficient to authorize or execute:

financial operation

Similarly:

cached account balance

may be acceptable for:

informational response

but not for:

high-risk financial execution

The required Context depends on the Intent, Action, Policy, risk, and current enterprise state.

⸻

4. Context vs Data

Data is information.

Context is information selected, scoped, classified, and structured for a specific decision or execution.

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

Whereas:

balance = 5000
source = ledger
authority = ledger
observed_at = T
purpose = transfer_precondition
scope = account:A-123

is execution-relevant Context.

⸻

5. Context vs Canonical Data

Canonical Data is authoritative information within a defined enterprise authority boundary.

Context is information available to Noema for a specific decision.

Therefore:

Canonical Data
      ↓
    Context

but:

Context ≠ Canonical Data

Context may contain canonical data as well as:

* evidence
* history
* user input
* derived values
* inferred values
* workflow state
* operational information
* environment information

Noema must preserve the distinction.

Noema does not become the authoritative owner of enterprise Business State merely because that state appears in Context.

⸻

6. Context vs Evidence

Context is information available for interpretation, resolution, evaluation, planning, or execution.

Evidence establishes support for a proposition or claim.

Example:

Context:
account_id = ACC-123
Evidence:
Ledger confirms ACC-123 belongs to Customer-456.

Context may contain information that has not yet been sufficiently validated or observed to become Evidence.

Therefore:

Context
   ↓
Validation / Observation
   ↓
Evidence

Evidence should preserve its relationship to the Context from which it was established.

⸻

7. Context vs Intent

Intent expresses what the Source of Intent wants to accomplish.

Context provides information required to interpret, resolve, constrain, or execute that Intent.

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

Model-generated interpretations may contribute candidate Context, but they do not become authoritative merely because the model produced them.

⸻

8. Context vs Business State

Business State belongs to the enterprise domain.

Context is Noema’s bounded representation of information about that state.

Example:

Enterprise:
Account.balance = $5,000
Noema:
Context.balance = $5,000

The Context does not become a competing authoritative account balance.

When current enterprise state is consequential, Noema must obtain and validate the required state through the appropriate authoritative source.

⸻

9. Context vs Noema State

Noema maintains its own execution-domain state.

Examples include:

* Intent state
* Trust state
* execution state
* intervention state
* reconciliation state
* verification state

These are Noema state.

Context may reference Noema state when relevant, but they remain conceptually distinct.

Context
   +
Noema State
   ↓
Execution Decision

⸻

10. Context Scope

Every Context Contract should define the scope of the Context.

Possible dimensions include:

* Tenant
* Organization
* Principal
* Resource
* Intent
* Action
* Execution
* Workflow
* Environment
* Time
* Purpose

Context must not cross these boundaries implicitly.

⸻

11. Principal Context

Context may contain information about the Principal or other relevant Actor.

Example:

principal_id = C-123
authentication_status = authenticated
session_id = S-456

Only information necessary for the current workflow should be included.

Authentication status is not itself authorization to perform an Action.

⸻

12. Resource Context

Context may contain information about the Resource targeted by an Action.

Example:

resource:
    type = Account
    account_id = A-123
    status = ACTIVE

Resource Context should identify the source and authority of consequential attributes.

A resource identifier that has not been deterministically resolved must not be treated as the final execution target.

⸻

13. Organizational Context

Enterprise decisions may depend on organizational boundaries.

Example:

tenant = T-1
organization = O-12
business_unit = BU-4

Context must preserve these boundaries when they affect:

* authorization
* policy
* data access
* execution
* audit
* routing

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
    value = 5000
    source = ledger-api

Possible sources include:

* enterprise API
* database
* event
* user input
* source of intent
* authorized operator
* configuration
* external service
* Noema-generated derivation
* model output

Source establishes provenance, not necessarily authority.

⸻

16. Authority

Context must distinguish source from authority.

Example:

Source:
analytics-db
Authority:
ledger

A source may provide useful information without being authoritative for the fact being represented.

Authority is claim-specific.

A system may be authoritative for one fact and non-authoritative for another.

⸻

17. Freshness

Context may become stale.

The Contract should define freshness requirements where relevant.

Example:

Context:
balance = $5,000
observed_at = 10:00
Action:
transfer money
Required freshness:
≤ 30 seconds

If the Context is too old:

STALE_CONTEXT

Noema should retrieve fresh information, reconcile state, or enter an appropriate deterministic state according to Policy.

⸻

18. Freshness Is Action-Specific

The same Context may be acceptable for one Action and unacceptable for another.

Example:

get_balance
→ 5-minute-old balance may be acceptable
financial_write
→ current authoritative balance required

Freshness must therefore be evaluated against the Action, Policy, risk, and relevant enterprise state.

⸻

19. Provenance

Context should preserve enough provenance to establish where the information came from and how it entered Noema.

Conceptually:

ContextItem {
    value
    source
    authority
    observed_at
    effective_at
    received_at
    version
    provenance
}

This supports:

* auditability
* Trust evaluation
* reconciliation
* debugging
* historical reconstruction
* verification

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
monthly_spend

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

Where a derived value is consequential, its derivation inputs, method, version, and provenance should be reconstructable according to Policy.

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
Schema / Semantic Validation
   ↓
Executable Context

Inference is not Evidence merely because the model is confident.

⸻

23. User-Provided Context

Source-of-Intent input may become Context.

Example:

User:
"My account number is A-123."

The value can be captured as Context.

For consequential operations, it may require enterprise verification.

Source-of-Intent Input
   ↓
Context Candidate
   ↓
Enterprise Verification
   ↓
Evidence

User-provided information does not automatically become authoritative.

⸻

24. Authorized Operator-Provided Context

An authorized operator or other approved source may supply Context.

Example:

Operator:
Customer identity verified.

The Contract should establish:

* who supplied it
* when
* under what authority
* for what purpose
* within which scope
* what claim it supports

Operator-provided information is not automatically canonical enterprise state.

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
Current Context:
account A-123
status = CLOSED

Historical execution or reconstruction may still require the earlier relationship.

The Contract should specify when historical Context may be used and what temporal semantics apply.

⸻

27. Context Validity

Context may have a validity interval.

Conceptually:

valid_from
valid_until

This is useful for:

* authorization
* account state
* policy versions
* identity relationships
* workflow state
* capability availability

Expired Context should not be silently reused.

⸻

28. Context Version

Where the underlying source supports versions, Context should preserve them.

Example:

account_version = 42

This allows Noema to determine whether the Context used for execution corresponds to the expected enterprise state.

Version information may also apply to:

* Policy
* Action Contract
* Enterprise Action Graph
* capability definition
* source schema

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
time_zone
preferred_currency

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

Missing required Context must prevent unsafe execution.

Missing Context
      ↓
Trust
      ↓
CLARIFY / ESCALATE / REJECT

The exact Trust outcome depends on why the Context is missing and whether it can be safely obtained.

⸻

32. Context Ambiguity

Context can itself be ambiguous.

Example:

account:
A-123
A-456
both associated with the same Principal

Noema must not arbitrarily choose one.

Ambiguous Context
       ↓
Deterministic Resolution
       ↓
Clarification / Approved Resolution

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

Noema must determine whether this represents:

* different definitions
* different authority
* stale information
* replication lag
* actual conflict

If authority cannot establish a deterministic resolution:

CONFLICT

must remain an explicit state.

The model must not resolve consequential conflicts by choosing whichever source appears more likely.

⸻

34. Context Priority

Context items should not be prioritized merely by:

* recency
* source count
* model confidence

Authority, scope, Policy, freshness, and purpose determine which information is appropriate.

Example:

Ledger:
balance = $10,000
Cache:
balance = $10,500

The cache being newer does not automatically make it authoritative.

⸻

35. Context Selection

Noema should select only the Context necessary for the current Intent, Action, Policy, and execution requirements.

Conceptually:

Available Enterprise Information
            ↓
      Context Contract
            ↓
     Relevant Context
            ↓
       Validation
            ↓
        Evidence

This limits unnecessary data access and reduces the amount of information exposed to downstream components.

⸻

36. Data Minimization

The Contract should enforce data minimization.

Example:

Action:
get_account_balance
Required:
account_id

There is no reason to retrieve:

* home_address
* full_profile
* unrelated_transactions

unless another explicit requirement exists.

Data minimization applies to both retrieval and downstream exposure.

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

Context access must therefore remain field-, resource-, tenant-, and purpose-aware where required.

Authentication is not sufficient evidence of permission.

⸻

39. Context and Privacy

Context may contain sensitive enterprise information.

The Contract should define appropriate:

* access
* redaction
* retention
* field minimization
* purpose restrictions
* disclosure restrictions

Noema should not expose Context merely because it was retrieved internally.

Internal availability does not imply external disclosure authorization.

⸻

40. Context Retention

Not all Context should be retained indefinitely.

The Contract may define:

* retention period
* retention purpose
* deletion requirements
* audit requirements
* recovery requirements

For example:

temporary Context
→ execution lifetime
audit Context
→ retained according to audit Policy

Retention requirements must account for both privacy and the need to reconstruct consequential decisions.

⸻

41. Context and Trust

Trust evaluates whether the available Context is sufficient, valid, authorized, and appropriate for the intended Action.

Conceptually:

Context
   ↓
Evidence
   ↓
Trust

Trust may evaluate:

* authority
* freshness
* completeness
* consistency
* provenance
* permissions
* scope
* policy applicability
* resource resolution
* actor resolution
* target resolution

The Context Contract defines what information Trust needs to perform that evaluation.

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

Postconditions may require Context obtained after execution.

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

Post-execution Context must not be confused with the Outcome itself.

⸻

44. Context and Planning

Planning uses Context to determine which Actions are applicable.

Example:

Intent:
"Show my transactions."
Context:
account_id = A-123

The Planner can select:

transaction.search

Without sufficient Context:

account_id = UNKNOWN

the Planner may need an identity or resource-resolution step before selecting the final Action.

The Planner cannot use Context to create authority or bypass Trust requirements.

⸻

45. Context and Execution

Execution consumes the Context required by the relevant Action Contract.

Context Contract
      ↓
Context
      ↓
Action Contract
      ↓
Trust
      ↓
Execution

Execution must not silently acquire unrelated Context outside the defined boundary.

Where execution begins after a material state change, the relevant Context must be revalidated or reacquired.

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

The Integration Model describes how information is accessed and normalized.

The Context Contract describes how that information may participate in Noema’s decision and execution processes.

An Adapter must not silently promote provider data into authoritative Context.

⸻

47. Context and Events

Events can update Context.

Example:

transaction.completed
       ↓
Context Update

However, event-derived Context must preserve appropriate:

* event_id
* source
* occurred_at
* received_at
* version
* ordering information where relevant

An event indicates an observation or notification; it does not automatically establish current canonical business state.

⸻

48. Context and Temporal State

Context may represent state at different times.

The following timestamps have different meanings:

observed_at
effective_at
received_at

For example:

Event occurred:
10:00
Noema received:
10:03

The Context should not confuse receipt time with business-effective time.

Temporal semantics are necessary for reliable reconstruction and audit.

⸻

49. Context and Staleness

Context may become stale during an execution.

Example:

Context acquired:
10:00
Execution:
10:10

If the Action requires current state, the Context may no longer satisfy the Contract.

Noema should:

* revalidate
* reacquire
* reconcile
* or stop execution

according to the relevant Contract and Policy.

⸻

50. Context Refresh

The Contract may define refresh behavior.

Example:

if balance_context_age > 30 seconds:
    refresh from ledger

Refresh should be deterministic.

The model should not decide arbitrarily when Context is “fresh enough.”

The refresh requirement should be derived from the Action Contract, Policy, risk, and relevant authority.

⸻

51. Context Snapshot

For deterministic Trust evaluation and consequential execution, Noema may create a Context snapshot.

Conceptually:

Context Snapshot
    │
    ├── Principal
    ├── Intent Version
    ├── Resources
    ├── Evidence References
    ├── Policy Version
    ├── Action Contract Version
    ├── Enterprise Graph Version
    └── Relevant Enterprise State

The snapshot can support:

* audit
* replay
* debugging
* reconciliation
* recovery
* verification

A snapshot is a record of the Context used for a decision; it does not make Noema authoritative for the underlying enterprise state.

⸻

52. Context Immutability

Context used for a consequential Trust decision should be immutable for that decision once the decision boundary is established.

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

This prevents hidden state changes from silently affecting a decision.

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
      ↓
Transaction state reconciled

Each update should be explicit and traceable.

Noema should not silently mutate decision-critical Context.

Material changes should create a new Context version or snapshot rather than altering historical decision inputs.

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

Noema must prevent accidental Context leakage between:

* executions
* tenants
* principals
* organizations
* environments
* resources

unless explicitly permitted by enterprise architecture and Policy.

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

Cross-tenant Context must be explicit, scoped, and auditable where it is permitted at all.

⸻

56. Environment Isolation

Similarly:

Production Context

must not satisfy:

Staging Action

or vice versa.

Environment is part of Context scope.

Production, staging, development, sandbox, and other execution environments must remain distinct unless an explicit integration and Policy permits controlled interaction.

⸻

57. Context Security

Context should be treated as security-sensitive execution material.

The Contract must control:

* who can access it
* which fields are available
* which Actions may consume it
* how long it persists
* which purposes permit its use
* which environments may receive it

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

A model-generated modification must not silently overwrite authoritative or previously established Context.

Context changes must be explicit, attributable, and versioned where required.

⸻

59. Context and Model Output

Model output may contribute to Context.

Example:

Model:
"last month" =
2026-07-01 → 2026-07-31

This is an interpretation.

It should be represented as:

Context Item:
type = inferred
source = model

and grounded according to the requirements and risk of the Action.

Model output is untrusted input to the deterministic boundary.

It must pass schema and semantic validation before becoming executable Context.

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

Confidence may inform candidate generation or routing, but it does not establish authority, authorization, or truth.

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

Clarification becomes part of the Intent and execution state.

Noema should not manufacture missing Context.

Clarification is required when the missing information is necessary to establish a safe and deterministic interpretation or execution path.

⸻

62. Context and Escalation

Some Context gaps cannot be resolved automatically.

Example:

Two accounts
same Principal
same distinguishing attributes
no deterministic resolution

If the Action is consequential:

Ambiguity
   ↓
ESCALATE

The escalation target and conditions should be defined by Policy and workflow configuration.

Escalation is not a fallback for arbitrary model uncertainty; it is a deterministic response to an unresolved condition.

⸻

63. Context and Unknown State

Context may be unavailable or its validity may be unknown.

Example:

Ledger unavailable

Noema should represent:

CONTEXT_UNAVAILABLE

rather than silently replacing it with an unsupported assumption.

The resulting Trust or execution control state may lead to:

CLARIFY
ESCALATE
REJECT

or a controlled retry/reconciliation path where applicable.

UNKNOWN must remain distinct from FALSE.

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
Scope
   ↓
Freshness
   ↓
Policy
   ↓
Deterministic Resolution

If no deterministic resolution exists:

CONFLICT

must remain explicit.

⸻

65. Context Contract and Action Contract

The two Contracts are complementary.

Context Contract
      ↓
What information may participate?
Action Contract
      ↓
What information and conditions are required for execution?

Together:

Context Contract
        +
Action Contract
        ↓
Trust
        ↓
Execution

The Context Contract does not grant permission to execute.

The Action Contract does not make missing or untrusted Context valid.

⸻

66. Context Contract and Evidence Contract

The Context Contract determines what information may participate in a decision.

Evidence semantics determine what observations establish propositions.

Context
   ↓
Observation / Validation
   ↓
Evidence

Context should therefore preserve sufficient provenance, authority, temporal, and derivation semantics for Evidence construction.

⸻

67. Context Contract and Policy

Policy may impose additional Context requirements.

Example:

Action:
complaint.create
Base Context:
transaction_id
Policy:
complaints above threshold require
transaction amount and account status

Therefore:

Action Contract
      +
Policy
      ↓
Required Context

Policy may also impose requirements on:

* freshness
* authority
* scope
* disclosure
* retention
* verification
* reconciliation

⸻

68. Context Contract and Auditability

For consequential decisions, Noema should preserve the relevant Context snapshot or sufficient references to reconstruct it.

Audit should establish:

* what Context was used
* when it was observed
* where it came from
* what authority it carried
* which Context Contract required it
* which Action Contract consumed it
* which Policy applied
* which Trust decision consumed it
* which execution attempt resulted

Auditability means causal traceability, not exposure of private model chain-of-thought.

⸻

69. Context Contract and Reproducibility

A decision should be reproducible to the extent required by its risk and audit requirements.

Conceptually:

Intent Version
+
Context Snapshot
+
Evidence
+
Policy Version
+
Action Contract Version
+
Relevant Graph Version
      ↓
Trust Decision

This is substantially stronger than relying on an opaque model conversation history.

Exact reproduction of external enterprise state is not always possible; where it is not, Noema should preserve sufficient evidence and provenance to reconstruct what was known and why the decision was made.

⸻

70. Context Contract and Recovery

Recovery may require Context that existed before failure.

Example:

Execution:
UNKNOWN

To reconcile it, Noema may need:

* execution_id
* idempotency_key
* target
* principal
* Action
* capability
* execution timestamp
* relevant request fingerprint
* provider reference
* prior evidence

The Context Contract should define which information must survive long enough to support recovery and reconciliation.

Noema must verify an UNKNOWN execution before blindly retrying a potentially side-effecting Action.

⸻

71. Context Contract and State Reconciliation

State Reconciliation is a first-class consumer of Context.

Reconciliation may require:

Enterprise State
+
Execution History
+
Provider Evidence
+
Context Snapshot
      ↓
Reconciled State

Context must preserve enough information to distinguish:

* known state
* stale state
* conflicting state
* unavailable state
* unknown state

Reconciliation must not manufacture certainty from incomplete Context.

⸻

72. Context Contract and Customer Account Inquiry

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

and:

"Show my transactions from last month."
Required:
principal_id
account_id
start_date
end_date

For transaction-exception investigation, additional Context may include:

transaction_id
transaction_reference
requested_operation
relevant timestamps
channel
provider references

The exact requirements remain Action- and workflow-specific.

⸻

73. Context Contract Example

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
    authority_requirements {
        resource_id:
            enterprise_authority
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

74. Context Item Model

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
    received_at
    expires_at
    version
    provenance
    classification
    sensitivity
    derivation
}

Possible classifications include:

canonical
observed
derived
inferred
user_provided
operator_provided
historical
cached
event_derived
operational

The classification describes the nature of the Context item; it does not by itself establish authority.

⸻

75. Context Relationships

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
   ├── consumed_by → Execution
   └── supports → Reconciliation

Context may also reference:

Policy
Action Contract
Capability
Enterprise Graph
Execution
Verification

where required for causal reconstruction.

⸻

76. Context Lifecycle

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

Additional states may include:

INVALID
CONFLICTED
REVOKED
UNAVAILABLE
SUPERSEDED

Context that becomes invalid should not remain silently usable.

Lifecycle state is distinct from the underlying value.

⸻

77. Context Invalidity

Context may become invalid because of:

* expiration
* source revocation
* resource state change
* permission change
* tenant change
* environment change
* version mismatch
* authority change
* conflict
* integrity failure
* policy change
* identity change

Invalid Context should trigger re-evaluation where required.

A Context item becoming invalid does not necessarily invalidate all Context in the same snapshot; invalidity is evaluated against the affected claim, purpose, and decision.

⸻

78. Context Contract Invariants

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

Authority must not be inferred merely from source availability, recency, or source count.

Invariant 7

Context requirements must be Action-, Intent-, Policy-, and risk-aware.

Invariant 8

Required Context must be explicit.

Invariant 9

Missing required Context must prevent unsafe execution.

Invariant 10

Ambiguous Context must not be resolved through probabilistic guessing when ambiguity is material.

Invariant 11

Model-generated Context must remain distinguishable from authoritative enterprise information.

Invariant 12

User-provided or operator-provided Context must not automatically become canonical.

Invariant 13

Derived Context must preserve its derivation semantics.

Invariant 14

Context must preserve relevant temporal information.

Invariant 15

Freshness requirements must be explicit where decision correctness depends on current state.

Invariant 16

Stale Context must not satisfy a requirement that demands fresher information.

Invariant 17

Context must respect tenant, organizational, legal, resource, purpose, and environment boundaries.

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

If authoritative Context is unavailable, Noema must preserve the unavailable or unknown state rather than manufacture a substitute.

Invariant 27

Consequential execution must have sufficient Context to establish its Preconditions.

Invariant 28

Context required for recovery, verification, and reconciliation must be retained according to Policy.

Invariant 29

Context used for consequential decisions must be sufficiently reconstructable for audit.

Invariant 30

The Context Contract defines what information may participate in a decision; it does not redefine enterprise Business State.

Invariant 31

Context does not grant authority to execute an Action.

Invariant 32

Model confidence does not establish Context authority, validity, or truth.

Invariant 33

A Context candidate must pass the required schema and semantic validation before entering the deterministic execution boundary.

Invariant 34

A resolved execution target must be established from sufficient Context and Evidence before consequential execution.

Invariant 35

UNKNOWN Context or execution conditions must not be silently converted into success, failure, or permission.

Invariant 36

Material Context changes after Trust evaluation must not silently alter the decision; the affected decision must be re-evaluated.

Invariant 37

Context snapshots must preserve sufficient references to reconstruct the Intent, Trust decision, execution, and verification path where required.

Invariant 38

Context acquisition and use must not provide the model with credentials or unrestricted access to enterprise systems.

⸻

79. Final Definition

A Context Contract is the authoritative specification of the information required, permitted, and appropriately qualified for a particular Noema decision or execution.

It establishes:

WHAT
information is required

WHERE
that information may come from

WHICH
source and authority semantics apply

HOW
fresh and temporally valid the information must be

WHAT
scope and purpose govern its use

HOW
its provenance and derivation are preserved

WHICH
data may be canonical, observed, derived, inferred, cached, historical, or event-derived

WHEN
the Context becomes invalid or stale

HOW
ambiguity, conflict, unavailability, and change are handled

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
        ├── TEMPORAL VALIDITY
        └── DERIVATION
                │
                ▼
        VALIDATION / OBSERVATION
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
       VERIFICATION / RECOVERY

And the architectural rule is:

Noema must never treat available information as automatically valid execution Context. Context is bounded by purpose, authority, scope, freshness, provenance, permissions, temporal validity, and Policy.

Context enables deterministic reasoning; it does not itself establish authority, permission, business truth, or execution success.