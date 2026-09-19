Context Engine

Status: Foundational
Version: 0.1
Domain: Architecture
Canonical Path: architecture/context-engine.md

⸻

1. Definition

The Context Engine is the Noema architectural component responsible for acquiring, organizing, evaluating, and providing the contextual information required to understand, validate, trust, and execute an Intent.

The Context Engine answers:

What information about the Actor, environment, resources, policies, capabilities, prior state, and external systems is relevant to this Intent?

It does not decide whether an Intent may execute.

That responsibility belongs to the Trust Engine.

The Context Engine provides the information on which downstream deterministic decisions can operate.

⸻

2. Core Principle

Intent cannot always be understood or evaluated from the user’s expression alone.

Noema therefore treats context as a first-class architectural concern.

The fundamental relationship is:

Intent
   ↓
Context Requirements
   ↓
Context Acquisition
   ↓
Context Assembly
   ↓
Context Validation
   ↓
Context Provided to:
   ├── Resolution
   ├── Validation
   ├── Trust
   └── Execution Planning

Context supports decision-making.

Context does not itself constitute authority.

⸻

3. Context vs Intent

Intent and Context must remain distinct.

Intent represents what the Actor wants to accomplish.

Context represents the relevant conditions, facts, relationships, evidence, and environmental state surrounding that Intent.

For example:

Intent:
Transfer ₦500,000 to John.
Context:
Actor = customer_123
Account = account_456
Account balance = ₦2,000,000
John = customer_789
Currency = NGN
Transfer policy = policy_17
Available capability = transfer_v2
Current time = ...

The Intent describes the objective.

The Context provides information necessary to interpret and evaluate that objective.

⸻

4. Context Is Not Permission

Context may contain authorization information.

It must not be conflated with authorization itself.

For example:

Context:
Actor = employee_123
Role = finance_manager

does not by itself mean:

Authorization = granted

The Trust Engine must evaluate whether the available authorization evidence permits the requested Action under the applicable policy and scope.

Therefore:

Context
   ↓
Evidence
   ↓
Trust Evaluation
   ↓
Authorization Decision

The Context Engine supplies relevant information.

The Trust Engine establishes whether that information satisfies the applicable Trust requirements.

⸻

5. Context Is Not Business Truth

Noema does not become the authoritative owner of external business state merely because the Context Engine retrieves it.

For example:

CRM
 └── customer record
Banking System
 └── account balance
Identity Provider
 └── identity status
Payment Provider
 └── payment state

These systems remain authoritative for their respective domains.

The Context Engine may retrieve and represent relevant facts from them.

It must preserve provenance indicating where those facts originated.

⸻

6. Context Requirements

Context should be acquired because it is required by an Intent or a downstream decision.

Noema should avoid treating all available information as relevant context.

Conceptually:

Intent
   ↓
Determine Required Context
   ↓
Acquire Relevant Context
   ↓
Evaluate Sufficiency

Examples of context requirements include:

Actor identity
Resource identity
Resource state
Authorization
Policy
Capability
Current time
Location or organizational scope
Prior interaction
External evidence
Execution constraints

The exact requirements depend on the Intent and Action.

⸻

7. Context Acquisition

The Context Engine may acquire information from:

* Noema-owned state
* enterprise systems
* identity providers
* authorization systems
* policy repositories
* capability registries
* external services
* previously established evidence
* explicit Actor-provided information

Conceptually:

                Context Engine
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Noema State    Enterprise      External
                    Systems        Sources
       │              │              │
       └──────────────┼──────────────┘
                      ▼
                Context Assembly

Acquisition should be explicit and traceable.

⸻

8. Context Assembly

Raw information from multiple sources must be assembled into a coherent Context representation.

For example:

Context
├── actor
├── organization
├── resources
├── relationships
├── policies
├── authorization
├── capabilities
├── evidence
├── temporal state
├── environmental state
└── provenance

Context assembly must preserve distinctions between:

* facts
* evidence
* interpretations
* derived values
* external authoritative state
* Noema-owned state

Noema must not silently convert an inference into an authoritative fact.

⸻

9. Context Provenance

Every externally sourced contextual fact that materially contributes to a decision should be traceable.

Conceptually:

Context Fact
├── value
├── source
├── source_reference
├── retrieved_at
├── observed_at
├── freshness
└── provenance

For example:

account.balance = ₦2,000,000
source:
Banking System
retrieved_at:
T1
observed_at:
T0

This allows downstream systems to determine whether the information remains suitable for the decision.

⸻

10. Context Freshness

Context can become stale.

A fact retrieved at one point in time may no longer accurately represent external state.

Therefore Context should be evaluated with respect to freshness.

Example:

T1:
Balance = ₦2,000,000
T2:
New withdrawal occurs
T3:
Noema attempts transfer

The Context Engine must not imply that the T1 balance is necessarily current at T3.

Freshness requirements may be defined by:

* Intent
* Action
* policy
* evidence type
* resource
* execution consumer

⸻

11. Context Validity

Context validity is distinct from context availability.

A context fact may exist but be invalid for the current decision.

Examples:

Authorization:
exists
but:
Authorization:
expired

or:

Resource:
exists
but:
Resource:
deleted

or:

Policy:
retrieved
but:
Policy:
superseded

Therefore the Context Engine should expose sufficient metadata for downstream validation and Trust evaluation.

⸻

12. Context Completeness

The Context Engine should be able to determine whether the required Context has been established.

Conceptually:

Required Context
       ↓
Available Context
       ↓
Compare
       ↓
Complete / Incomplete / Unknown

An incomplete Context must not be silently treated as complete.

Example:

Required:
Actor
Source Account
Destination
Currency
Authorization
Available:
Actor
Source Account
Currency
Result:
Incomplete

The missing requirements should be explicit.

⸻

13. Unknown Context

Context may be unavailable because an external dependency cannot provide the required information.

Example:

Customer Registry
       ↓
Unavailable

The correct result is not:

Customer does not exist

nor:

Customer exists

The result is:

UNKNOWN

Unknown information must remain distinguishable from negative information.

This is essential to Noema’s fail-closed architecture.

⸻

14. Context and Clarification

Some Context can be supplied by the Actor.

Example:

Intent:
"Send the invoice."
Required Context:
Destination
Context:
Destination = unknown

Noema may request clarification.

The resulting information can then become part of the Context used to resolve and validate the Intent.

Conceptually:

Missing Context
      ↓
Clarification Request
      ↓
Actor Response
      ↓
Context Update
      ↓
Re-resolution / Validation

Noema must not manufacture the missing Context through probabilistic guessing.

⸻

15. Context and Intent Resolution

Context may help resolve ambiguity.

Example:

User:
"Send it to John."
Potential Johns:
John A
John B
John C

Relevant Context might include:

* current conversation
* active customer record
* recent workflow
* organizational scope
* previously identified entities

If that Context deterministically establishes the intended John, resolution may proceed.

If it does not:

Intent = unresolved

and clarification is required.

Context may reduce ambiguity.

It must not manufacture certainty.

⸻

16. Context and Validation

The Validation layer consumes Context to establish whether the resolved Intent is structurally and semantically applicable.

For example:

Intent:
Close incident INC-123

Context:

INC-123.status = RESOLVED

Validation may determine that the Intent is no longer applicable.

The Context Engine provides the relevant fact.

Validation determines the implication for the Intent.

⸻

17. Context and Trust

Trust evaluation depends on relevant Context.

For example:

Intent
+
Actor
+
Authorization
+
Policy
+
Resource State
+
Evidence
+
Capability
+
Current Conditions
        ↓
Trust Evaluation

The Context Engine supplies the relevant information.

The Trust Engine applies the deterministic rules.

Therefore:

Context ≠ Trust

and:

Context Engine ≠ Trust Engine

⸻

18. Context and Capability

Capabilities are contextual to the requested Action.

For example:

Action:
REFUND_PAYMENT
Capability Registry:
refund_v2 available

The Context Engine may establish that the capability exists and provide its relevant metadata.

Trust evaluates whether that capability may be used for the specific Intent.

Capability availability may change over time.

Therefore capability Context may require re-acquisition or revalidation.

⸻

19. Context and Policy

Policies are contextual inputs to Intent evaluation.

A policy may depend on:

* Actor
* organization
* Action
* resource
* amount
* jurisdiction
* time
* risk classification
* approval level

The Context Engine may retrieve the applicable policies.

The Trust Engine determines their effect on execution eligibility.

For example:

Policy:
Transfers above ₦5M require approval.
Intent:
Transfer ₦10M.
Context:
Applicable policy identified.
Trust:
WAITING_FOR_APPROVAL

The Context Engine identifies the policy.

The Trust Engine evaluates it.

⸻

20. Context and Authorization

Authorization information may originate from an external authorization system.

The Context Engine may acquire:

Actor
Role
Resource
Permission
Scope
Expiration

Trust determines whether the authorization evidence is sufficient for the requested Action.

Authorization should therefore be represented with sufficient provenance and temporal information.

⸻

21. Context and Time

Time is contextual.

Some decisions depend on:

* current time
* execution window
* authorization validity
* approval expiry
* evidence freshness
* resource reservation
* policy effective date

Noema should therefore represent relevant temporal conditions explicitly.

For example:

Authorization:
valid_from = T1
valid_until = T2
Current Time:
T3
Result:
Authorization expired

Time-sensitive Context may cause Trust re-evaluation.

⸻

22. Context and Scope

Context may establish organizational or resource scope.

Examples:

Actor:
employee_123
Organization:
company_A
Resource:
account_456
Scope:
company_A

Scope information can be relevant to:

* authorization
* policy
* resource eligibility
* capability
* execution

Scope must be explicit where it materially affects the decision.

⸻

23. Context and Relationships

Some Intent evaluations depend on relationships rather than isolated facts.

Examples:

Actor ──owns──> Resource
Actor ──manages──> Account
Customer ──has──> Subscription
Employee ──belongs_to──> Organization

The Context Engine may provide these relationships as contextual facts.

Relationship provenance should be retained when the relationship contributes materially to validation or Trust.

⸻

24. Context Graph

A future implementation may represent Context as a graph.

Conceptually:

                 Actor
                  │
          ┌───────┼────────┐
          │       │        │
          ▼       ▼        ▼
      Resource  Role   Organization
          │
          ▼
        State
          │
          ▼
       Policy
          │
          ▼
      Capability

The graph model is useful when decisions depend on relationships across multiple entities.

The exact implementation remains an architectural decision.

⸻

25. Context Snapshots

For consequential decisions, Noema should be able to reconstruct the relevant Context available at evaluation time.

Conceptually:

Context Snapshot
├── Intent version
├── Facts
├── Evidence
├── Policies
├── Authorization
├── Capabilities
├── Temporal state
└── Provenance

This does not require Noema to become the permanent source of truth for external systems.

It means Noema retains sufficient decision provenance to reconstruct what information supported its decision.

⸻

26. Context Versioning

Context may change independently of Intent.

Therefore Context should be versionable or otherwise identifiable at the point of evaluation.

Example:

Intent Version:
7
Context Version:
42
Trust Evaluation:
evaluation_103

This allows historical decisions to be reconstructed without confusing later Context with earlier Context.

⸻

27. Context Dependencies

An Intent may depend on a subset of available Context.

For example:

Intent I1
   ├── Actor
   ├── Account
   └── Balance
Intent I2
   ├── Actor
   ├── Customer
   └── Subscription

A change to subscription state should not necessarily invalidate I1.

Therefore Context dependencies should be explicit where practical.

This supports selective re-evaluation.

⸻

28. Context Invalidation

Context may become invalid because:

* source state changed
* evidence expired
* authorization was revoked
* policy changed
* capability became unavailable
* resource state changed
* context was superseded
* source data became unavailable

When material Context changes, dependent Intent evaluations may need to be re-run.

Conceptually:

Context Change
      ↓
Identify Dependents
      ↓
Invalidate Affected Evaluation
      ↓
Re-acquire / Revalidate Context
      ↓
Re-evaluate

⸻

29. Context Acquisition Failure

Context acquisition can fail for many reasons:

Timeout
Unavailable service
Authentication failure
Malformed response
Stale source
Conflicting sources
Unknown source state

Noema should distinguish acquisition failure from the business fact being false.

For example:

Registry unavailable

does not mean:

Customer does not exist

The downstream state should reflect the uncertainty.

⸻

30. Conflicting Context

Different sources may provide conflicting information.

Example:

Source A:
account.status = ACTIVE
Source B:
account.status = CLOSED

Noema should not silently select one because it appears more convenient.

The system should apply an explicit source-authority or reconciliation rule where one exists.

If no authoritative resolution exists, the Context should preserve the conflict and downstream evaluation should treat the unresolved conflict appropriately.

⸻

31. Source Authority

Context sources may have different authority for different facts.

For example:

Identity Provider
    → identity
Banking System
    → account state
Payment Provider
    → payment state

Authority is therefore fact-specific.

A source authoritative for one domain must not automatically become authoritative for another.

⸻

32. Context Normalization

External systems may represent the same concept differently.

For example:

Banking System:
ACTIVE
CRM:
active_customer

The Context Engine may normalize external representations into canonical Noema representations where the mapping is explicitly defined.

Normalization must preserve the original source information.

Conceptually:

External Value
      ↓
Explicit Mapping
      ↓
Canonical Context Representation
      +
Source Provenance

Noema must not silently change the semantics of external facts.

⸻

33. Context Transformation

Derived Context may be calculated from source facts.

Example:

Balance = ₦2M
Requested Transfer = ₦500K
Derived:
Remaining Balance = ₦1.5M

Derived values must be distinguishable from source facts.

Conceptually:

Source Fact
     ↓
Deterministic Transformation
     ↓
Derived Context

The provenance of the derivation should be retained where it materially contributes to a decision.

⸻

34. Context Evidence

Context and Evidence are related but not identical.

A Context object may contain evidence supporting a fact.

For example:

Context:
recipient_exists = true
Evidence:
Customer Registry response

The Context Engine may assemble the contextual fact.

The Evidence model should preserve the underlying support and provenance.

⸻

35. Context Privacy and Minimization

The Context Engine should acquire only the information necessary for the current Intent and its required decisions.

It should avoid indiscriminate retrieval of unrelated data.

Conceptually:

Intent Requirements
      ↓
Minimum Necessary Context
      ↓
Acquire

This supports:

* privacy
* security
* performance
* explainability
* bounded data access

Context should be relevant, not merely available.

⸻

36. Context Access

Access to Context should itself respect applicable authority boundaries.

Noema should not assume:

Context exists

means:

Noema may retrieve it.

The ability to access Context is governed by the applicable credentials, permissions, policies, and integration contracts.

Context acquisition is therefore itself a controlled operation.

⸻

37. Context Caching

Context may sometimes be cached.

Caching is acceptable only when the freshness requirements of the consuming decision permit it.

For example:

Static organization metadata

may tolerate longer caching than:

Account balance

Therefore cache validity should be determined by the semantic requirements of the Context rather than by a generic cache duration alone.

⸻

38. Context and Race Conditions

Context may change between:

Context acquisition
        ↓
Validation
        ↓
Trust
        ↓
Execution

This creates a potential TOCTOU condition.

Therefore:

Context at T1

does not guarantee:

Business state at T3

For consequential Actions, the execution consumer may need to perform final authoritative checks.

The Context Engine must not imply that a Context snapshot guarantees successful execution.

⸻

39. Context Refresh

A Context refresh may be required when:

* an evaluation is retried
* an Intent changes
* a relevant dependency changes
* evidence expires
* an authorization changes
* policy changes
* execution is delayed
* the Context exceeds its freshness requirements

Refresh should be dependency-aware rather than indiscriminate.

⸻

40. Context Re-Evaluation

Context changes may trigger downstream re-evaluation.

Conceptually:

Existing Context
      ↓
Material Change
      ↓
Context Refresh
      ↓
Validation / Trust Re-evaluation

A Context change does not automatically imply rejection or approval.

Its effect must be determined by the applicable validation and Trust rules.

⸻

41. Context Contract

Conceptually:

GetContext(
    Intent,
    Requirements,
    Sources,
    Constraints
)
→ ContextResult

A ContextResult should make clear:

* what was requested
* what was acquired
* what was unavailable
* what remains unknown
* where the information came from
* when it was observed
* when it was retrieved
* whether freshness requirements were satisfied

⸻

42. Context Result

A conceptual result structure is:

ContextResult {
    status
    facts
    evidence
    requirements
    unknowns
    conflicts
    provenance
    retrieved_at
}

Possible statuses include:

COMPLETE
INCOMPLETE
UNKNOWN
CONFLICTED
FAILED

The exact protocol remains implementation-dependent.

⸻

43. Context and Failure Semantics

The Context Engine must preserve the distinction between:

Fact = false

and:

Fact = unknown

and:

Fact = unavailable

and:

Fact = conflicting

These conditions have different implications for Validation and Trust.

They must not collapse into a generic failure state when doing so would destroy decision-relevant information.

⸻

44. Context and Determinism

Context acquisition itself may involve dynamic external systems.

Therefore the Context Engine cannot necessarily guarantee that repeated acquisition at different times returns identical results.

What must remain deterministic is the interpretation of a given Context snapshot by deterministic downstream components.

Conceptually:

Context Snapshot
+
Rules
+
Policy Version
+
Intent Version
        ↓
Deterministic Evaluation

The Context Engine should therefore preserve the snapshot and provenance used for consequential decisions.

⸻

45. Context and LLMs

LLMs may assist in identifying what Context might be relevant.

For example:

User:
"Can I renew my card?"
Model:
Candidate context:
- card
- card status
- expiry
- account
- eligibility policy

The Context Engine must not treat the model’s proposal as authoritative.

Required Context should ultimately be established through explicit schemas, Action definitions, policies, dependencies, or deterministic system requirements.

The architecture is therefore:

LLM
 ↓
Candidate Context Requirements
 ↓
Deterministic Context Requirements
 ↓
Context Acquisition
 ↓
Context Result

⸻

45. Context and Natural Language

Natural language may contain contextual references:

"the account"
"my usual card"
"that customer"
"the previous payment"

The Context Engine may provide the information necessary to resolve such references.

However, reference resolution must remain explicit.

If multiple candidates remain materially plausible:

UNKNOWN / AMBIGUOUS

rather than a guessed selection.

⸻

46. Context and Defaults

Defaults may be applied only where canonical Intent or Action semantics explicitly define them.

For example:

Currency:
account.default_currency

may be valid if the account’s currency is authoritative and the Action permits that default.

But:

Recipient:
most_recent_contact

must not be selected merely because it appears likely.

Context may support a default.

It must not silently create one.

⸻

47. Context and Composite Intents

Composite Intents may require multiple Context sets.

Example:

Composite Intent
├── Transfer
│   ├── source account
│   ├── destination
│   └── balance
│
├── Notify
│   └── recipient contact
│
└── Record
    └── CRM customer

Each component may have distinct Context dependencies.

Noema should avoid assuming that one global Context object is sufficient for every component.

⸻

48. Context and Partial Execution

If partial execution is explicitly permitted, each component may have independent Context requirements.

Example:

A:
Context complete
Trust ready
B:
Context incomplete
Waiting
C:
Context complete
Trust ready

Whether A and C may proceed depends on the semantics of the Composite Intent and its execution contract.

The Context Engine does not infer permission for partial execution.

⸻

49. Context Auditability

For consequential decisions, Noema should be able to answer:

* What Context was requested?
* Which sources were consulted?
* What facts were returned?
* Which facts were unknown?
* Which facts were stale?
* Which facts conflicted?
* Which Context contributed to the decision?
* When was it acquired?
* What version or source state was used?

This supports Trust provenance and post-execution investigation.

⸻

50. Context Security

Context can contain sensitive enterprise information.

The Context Engine must therefore respect:

* access boundaries
* data minimization
* source permissions
* credential boundaries
* tenant boundaries
* organizational boundaries
* retention requirements

Context must not become an unrestricted data aggregation layer merely because Noema can technically access multiple systems.

⸻

51. Context Isolation

Where Noema operates across multiple tenants, organizations, or security domains, Context must remain appropriately isolated.

Conceptually:

Tenant A Context
       ≠
Tenant B Context

Noema must not allow contextual information from one security domain to silently influence an Intent in another.

Cross-domain access must be explicit and authorized.

⸻

52. Context Ownership

Noema may own the representation of contextual information required for Intent processing.

It does not necessarily own the underlying fact.

For example:

Noema owns:
Context representation used for evaluation.
Banking System owns:
Account balance.

This distinction should remain explicit.

⸻

53. Context Lifecycle

Context itself may have a lifecycle:

REQUESTED
   ↓
ACQUIRING
   ↓
ASSEMBLED
   ↓
VALIDATED
   ↓
AVAILABLE
   ↓
STALE / INVALIDATED
   ↓
REFRESHED

The exact Context lifecycle may be represented separately from Intent and Trust states.

The important principle is that Context can change independently.

⸻

54. Context vs Trust State

These states must not be conflated.

For example:

Context:
COMPLETE
Trust:
WAITING_FOR_APPROVAL

or:

Context:
COMPLETE
Trust:
BLOCKED_BY_POLICY

or:

Context:
INCOMPLETE
Trust:
NOT_READY

Complete Context does not imply Trust.

⸻

55. Context vs Validation State

Similarly:

Context:
COMPLETE
Validation:
INVALID

or:

Context:
INCOMPLETE
Validation:
INCOMPLETE

Context provides information.

Validation determines whether the Intent satisfies its applicable structural and semantic requirements.

⸻

56. Context Dependency Graph

A future architecture may explicitly model:

Intent
 │
 ├── requires → Actor
 ├── requires → Resource
 ├── requires → Policy
 ├── requires → Authorization
 ├── requires → Capability
 └── requires → Evidence

Each dependency can identify:

* source
* freshness requirement
* authority
* access requirement
* validation rule
* downstream consumers

This would allow targeted context acquisition and re-evaluation.

⸻

57. Context Materiality

Not every Context change is material.

A Context change is material when it can affect:

* Intent interpretation
* validation
* Trust
* action selection
* execution eligibility
* execution safety
* expected outcome

Noema should therefore distinguish:

Context change

from:

Material Context change

Only material changes need to invalidate dependent decisions.

⸻

58. Context Events

A conceptual event vocabulary includes:

context.requested
context.acquiring
context.available
context.updated
context.expired
context.invalidated
context.refreshed
context.unavailable
context.conflicted
context.source_changed

These events are illustrative rather than a final protocol.

⸻

59. Context Transition Principles

Context transitions should be:

* explicit
* traceable
* dependency-aware
* deterministic where rules are applied
* distinguishable by cause

The system should not silently replace a previously used Context snapshot without recording the change.

⸻

60. Context and Execution

Context supports execution but does not perform execution.

The relationship is:

Intent
   ↓
Context
   ↓
Validation
   ↓
Trust
   ↓
Action Contract
   ↓
Execution Consumer

The execution consumer remains authoritative for the actual mutation of business state.

⸻

61. Consumer-Side Context Validation

Execution consumers may perform final Context checks.

Example:

Noema Context:
Account eligible
Execution Consumer:
Account state changed

The consumer may reject execution.

This does not necessarily invalidate the Context used by Noema at the earlier evaluation time.

It demonstrates that external business state can change between evaluation and execution.

⸻

62. Context and Outcome

Context can support outcome verification.

Example:

Pre-execution:
Card status = ACTIVE
Action:
Replace card
Post-execution:
Card status = REPLACED

The post-execution state remains authoritative in the external system.

Noema records the observed outcome and its provenance rather than becoming the system of record.

⸻

63. Context Invariants

Invariant 1

Context is distinct from Intent.

Invariant 2

Context is not permission.

Invariant 3

Context is not Trust.

Invariant 4

Context is not the authoritative business state of external systems.

Invariant 5

Unknown Context must not be treated as established fact.

Invariant 6

Material Context should have provenance.

Invariant 7

Context freshness must be considered where time-sensitive decisions depend on it.

Invariant 8

Context acquisition must respect access boundaries.

Invariant 9

Context should be acquired according to explicit requirements rather than indiscriminately.

Invariant 10

Context may support clarification but must not manufacture certainty.

Invariant 11

Context changes may require downstream revalidation or Trust re-evaluation.

Invariant 12

Conflicting Context must not be silently reconciled without an explicit rule.

Invariant 13

Derived Context must remain distinguishable from source facts.

Invariant 14

Context completeness does not imply Trust readiness.

Invariant 15

Context availability does not guarantee execution success.

Invariant 16

Noema must preserve sufficient Context provenance to reconstruct consequential decisions.

⸻

64. Canonical Context Flow

                    Intent
                       │
                       ▼
             Context Requirements
                       │
                       ▼
              Context Acquisition
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Internal     Enterprise    External
        State         Systems      Sources
          │            │            │
          └────────────┼────────────┘
                       ▼
                Context Assembly
                       │
                       ▼
              Context Validation
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       COMPLETE     INCOMPLETE    UNKNOWN
          │             │            │
          ▼             ▼            ▼
     Downstream      Clarify /    Not Ready /
     Evaluation      Acquire      Re-evaluate
          │
          ▼
     Validation
          │
          ▼
        Trust
          │
          ▼
       Execution

⸻

65. Canonical Mental Model

The Context Engine can be reduced to five questions:

1. What context does this Intent require?
2. Where does that context come from?
3. Is the context available, valid, and sufficiently fresh?
4. What provenance supports each material contextual fact?
5. What downstream decision depends on that context?

The resulting abstraction is:

Intent
   ↓
Required Context
   ↓
Acquire
   ↓
Assemble
   ↓
Validate
   ↓
Provide
   ↓
Re-evaluate when material Context changes

⸻

66. Final Definition

The Context Engine is Noema’s architectural layer for acquiring, assembling, validating, and maintaining the contextual information required to resolve, validate, trust, and execute an Intent.

Its central invariant is:

Noema must distinguish between what is known, what is unknown, where a fact came from, how fresh it is, and whether that fact is authoritative for the decision being made.

Context enables deterministic decision-making.

It does not become the decision itself.