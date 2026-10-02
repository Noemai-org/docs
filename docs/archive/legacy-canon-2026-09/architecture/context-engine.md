> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Context Engine

Status: Foundational
Version: 0.2
Domain: Architecture
Canonical Path: architecture/context-engine.md

⸻

1. Definition

The Context Engine is the Noema architectural component responsible for determining, acquiring, assembling, validating, maintaining, and providing the contextual information required to resolve, validate, trust, plan, execute, and verify an Intent.

The Context Engine answers:

What information about the Actor, resources, environment, relationships, policies, capabilities, prior operational state, external systems, and temporal conditions is relevant to this Intent?

The Context Engine does not determine what the Actor means.

That responsibility belongs to the Intent Engine and Intent Resolution.

The Context Engine does not determine whether an Intent may execute.

That responsibility belongs to the Trust Engine.

The Context Engine provides the relevant contextual information and provenance required by those downstream decisions.

Its fundamental architectural purpose is therefore:

Acquire the right context, preserve what is known and unknown, establish provenance and freshness, and make relevant context available without converting context into authority.

⸻

2. Core Principle

An Intent cannot always be understood, validated, trusted, or executed from the Actor’s expression alone.

Noema therefore treats Context as a first-class architectural concern.

The canonical relationship is:

Intent
   │
   ▼
Context Requirements
   │
   ▼
Context Acquisition
   │
   ▼
Context Assembly
   │
   ▼
Context Validation
   │
   ▼
Context Provided to:
   ├── Intent Resolution
   ├── Validation
   ├── Trust
   ├── Execution Planning
   └── Outcome Verification

Context supports downstream decision-making.

Context does not itself constitute:

* Intent
* validity
* authorization
* Trust
* execution authority
* business truth

⸻

3. Architectural Position

The Context Engine is a cross-cutting architectural capability.

Conceptually:

                    Intent
                      │
                      ▼
             Context Requirements
                      │
                      ▼
               Context Engine
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Intent Engine   Validation     Trust Engine
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
              Execution Planner
                      │
                      ▼
               Action Contract
                      │
                      ▼
             Execution Consumer
                      │
                      ▼
                    Outcome

The Context Engine does not replace these components.

It supplies contextual information to them.

⸻

4. Context vs Intent

Intent and Context must remain distinct.

Intent represents what the Actor wants to accomplish.

Context represents the relevant conditions, facts, relationships, evidence, environmental state, and historical information surrounding that Intent.

For example:

Intent:
Transfer ₦500,000 to John.

Relevant Context may include:

Actor = customer_123
Source Account = account_456
Account Balance = ₦2,000,000
John = customer_789
Currency = NGN
Transfer Policy = policy_17
Capability = transfer_v2
Current Time = T

The Intent expresses the objective.

The Context provides information necessary to interpret and evaluate that objective.

Context must not silently become part of the Intent merely because it was retrieved.

⸻

5. Context Is Not Authority

Context may contain information about authority.

It is not itself authority.

For example:

Context:
Actor = employee_123
Role = finance_manager

does not by itself establish:

Authorization = granted

The Trust Engine must determine whether authoritative authorization evidence establishes permission for the requested Action under the applicable scope.

Therefore:

Context
   │
   ▼
Evidence
   │
   ▼
Trust Evaluation
   │
   ▼
Execution Eligibility

The Context Engine supplies relevant information.

The Trust Engine establishes the consequence of that information for execution eligibility.

⸻

6. Context Is Not Business Truth

Noema does not become the authoritative owner of external business state merely because the Context Engine retrieves or represents it.

For example:

CRM
 └── customer record
Banking System
 └── account balance
Identity Provider
 └── identity status
Payment Provider
 └── payment state

Those systems remain authoritative for their respective domains.

The Context Engine may retrieve relevant facts from them.

It must preserve sufficient provenance to establish:

* which source supplied the information
* what was observed
* when it was observed
* when it was retrieved
* what authority the source has for that fact
* whether the information remains sufficiently fresh

⸻

7. Context Requirements

Context must be acquired because it is required by the Intent, Action, policy, Validation, Trust, or execution semantics.

Noema should not treat all available information as relevant Context.

The conceptual flow is:

Intent
   │
   ▼
Determine Context Requirements
   │
   ▼
Acquire Required Context
   │
   ▼
Evaluate Sufficiency

Potential Context requirements include:

* Actor identity
* Actor scope
* Resource identity
* Resource state
* relationships
* authorization
* applicable policy
* capability
* current time
* execution window
* external evidence
* prior operational history
* constraints
* environmental conditions
* approval state
* confirmation state
* freshness requirements

The exact requirements depend on the Intent and the downstream operation.

⸻

8. Minimum Necessary Context

The Context Engine should acquire the minimum Context necessary to perform the required operation.

Conceptually:

Intent
   │
   ▼
Required Context
   │
   ▼
Minimum Necessary Context
   │
   ▼
Acquire

Availability does not establish relevance.

The fact that Noema can access information does not mean that Noema should retrieve it.

This supports:

* privacy
* security
* bounded reasoning
* performance
* explainability
* tenant isolation

⸻

9. Context Acquisition

The Context Engine may acquire information from:

* Noema-owned operational state
* Operational Memory
* enterprise systems
* identity providers
* authorization systems
* policy repositories
* capability registries
* external services
* evidence sources
* explicit Actor-provided information
* previously established contextual observations

Conceptually:

                     Context Engine
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     Noema State       Enterprise        External
                         Systems          Sources
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    Context Assembly

Acquisition should be explicit, traceable, and governed by the applicable access boundaries.

⸻

10. Context Source Authority

Different sources may have different authority for different facts.

For example:

Identity Provider
    → identity
Banking System
    → account state
Payment Provider
    → payment state
Authorization System
    → authorization state
Policy Repository
    → policy definition

Authority is therefore fact-specific.

A source authoritative for one domain must not automatically become authoritative for another.

The Context Engine should preserve source authority metadata where it materially affects downstream decisions.

⸻

11. Context Assembly

Raw information from multiple sources must be assembled into a coherent Context representation.

A conceptual Context may contain:

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
├── operational history
└── provenance

Context assembly must preserve distinctions between:

* source facts
* evidence
* derived values
* interpretations
* external authoritative state
* Noema-owned state
* historical observations
* current observations
* unknown conditions
* conflicting conditions

Noema must not silently convert an inference into an authoritative fact.

⸻

12. Context Facts

A Context fact should be represented with sufficient metadata to establish what the fact means and where it came from.

Conceptually:

ContextFact {
    subject
    predicate
    value
    source
    source_reference
    authority
    observed_at
    retrieved_at
    freshness
    validity
    provenance
}

The exact implementation schema is not prescribed here.

The architectural requirement is that materially relevant Context remain interpretable and traceable.

⸻

13. Context Provenance

Every externally sourced Context fact that materially contributes to a consequential decision should be traceable.

Conceptually:

Context Fact
├── value
├── source
├── source_reference
├── authority
├── retrieved_at
├── observed_at
├── freshness
└── provenance

For example:

account.balance = ₦2,000,000
source:
Banking System
observed_at:
T0
retrieved_at:
T1

This allows downstream systems to determine whether the information is suitable for the decision being made.

⸻

14. Observation Time vs Retrieval Time

Context must distinguish when a fact was observed from when Noema retrieved it.

For example:

observed_at  = 10:00
retrieved_at = 10:03

These timestamps have different meanings.

In distributed systems, additional timestamps may be relevant:

* source event time
* observation time
* request time
* retrieval time
* persistence time
* evaluation time

The Context Engine should preserve the temporal information required to determine freshness and ordering.

⸻

15. Context Freshness

Context can become stale.

A fact retrieved at one point in time may no longer represent current external state.

Example:

T1:
Balance = ₦2,000,000
T2:
Withdrawal occurs
T3:
Noema attempts transfer

The Context Engine must not imply that the T1 balance is necessarily current at T3.

Freshness requirements may depend on:

* Intent
* Action
* policy
* evidence type
* resource
* execution consumer
* risk
* temporal sensitivity

Freshness is therefore semantic, not merely a generic cache duration.

⸻

16. Context Validity

Context validity is distinct from Context availability.

A Context fact may exist but no longer be valid for the current decision.

Examples:

Authorization:
exists
but:
expired

or:

Resource:
exists
but:
deleted

or:

Policy:
retrieved
but:
superseded

The Context Engine should expose sufficient metadata for downstream Validation and Trust to determine whether the Context remains usable.

⸻

17. Context Completeness

The Context Engine should determine whether required Context has been established.

Conceptually:

Required Context
       │
       ▼
Available Context
       │
       ▼
Compare
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
Complete Incomplete Unknown

Incomplete Context must not silently be treated as complete.

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
Missing:
Destination
Authorization

Missing requirements should be explicit.

⸻

18. Unknown Context

Context may be unknown because a source cannot provide the required information.

Example:

Customer Registry
       │
       ▼
Service unavailable

The correct result is not:

Customer does not exist

and not:

Customer exists

The result is:

UNKNOWN

Unknown information must remain distinguishable from negative information.

This distinction is foundational to Noema’s fail-closed architecture.

⸻

19. Context Acquisition Failure

Acquisition may fail because of:

* timeout
* unavailable service
* authentication failure
* authorization failure
* malformed response
* stale source
* conflicting source
* invalid source response
* network failure
* dependency failure

The Context Engine must distinguish:

Fact = false

from:

Fact = unknown

from:

Fact = unavailable

The failure of a source does not establish the opposite business fact.

⸻

20. Conflicting Context

Different sources may provide conflicting information.

Example:

Source A:
account.status = ACTIVE
Source B:
account.status = CLOSED

Noema must not silently select one merely because it appears convenient.

The system should apply an explicit source-authority or reconciliation rule where one exists.

If the conflict cannot be deterministically resolved, the Context should preserve the conflict.

Downstream Validation or Trust must then determine the appropriate consequence.

⸻

21. Context and Clarification

Some missing Context can be supplied by the Actor.

Example:

Intent:
"Send the invoice."
Required Context:
Destination
Context:
Destination = UNKNOWN

Noema may request clarification.

The resulting information can then become Context used to resolve and validate the Intent.

Conceptually:

Missing Context
      │
      ▼
Clarification Request
      │
      ▼
Actor Response
      │
      ▼
Context Update
      │
      ▼
Re-resolution / Validation

Noema must not manufacture missing Context through probabilistic guessing.

⸻

22. Context and Intent Resolution

Context may help resolve references and ambiguity.

Example:

User:
"Send it to John."

Potential candidates:

John A
John B
John C

Relevant Context might include:

* current conversation
* active workflow
* organizational scope
* recent interaction
* previously established entities
* Actor-specific relationships

If Context deterministically establishes the intended John, resolution may proceed.

If multiple materially plausible candidates remain:

Intent = UNRESOLVED

and clarification is required.

Context may reduce ambiguity.

It must not manufacture certainty.

⸻

23. Context and Natural-Language References

Natural language may contain references such as:

* “the account”
* “my usual card”
* “that customer”
* “the previous payment”
* “same as before”
* “the other one”

The Context Engine may provide the information required to resolve those references.

Reference resolution must remain explicit.

If the available Context does not uniquely establish the reference, Noema must preserve the ambiguity rather than silently selecting a candidate.

⸻

24. Context and Defaults

Defaults may be applied only where canonical Intent or Action semantics explicitly define them.

For example:

Currency:
account.default_currency

may be valid where the account currency is authoritative and the Action semantics permit that default.

But:

Recipient:
most_recent_contact

must not be selected merely because it appears likely.

Context may support an explicit default.

It must not silently create one.

⸻

25. Context and Validation

Validation consumes Context to determine whether a resolved Intent satisfies its structural and semantic requirements.

Example:

Intent:
Close incident INC-123
Context:
INC-123.status = RESOLVED

Validation may determine that the Intent is no longer applicable.

The Context Engine provides the relevant fact.

Validation determines its implication for the Intent.

Therefore:

Context ≠ Validation

⸻

26. Context and Trust

Trust depends on relevant Context.

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
        │
        ▼
Trust Evaluation

The Context Engine supplies the relevant information.

The Trust Engine applies deterministic Trust rules.

Therefore:

Context ≠ Trust
Context Engine ≠ Trust Engine

Context completeness does not imply Trust readiness.

⸻

27. Context and Authorization

Authorization information may originate from an authoritative authorization system.

The Context Engine may acquire:

* Actor
* Role
* Resource
* Permission
* Scope
* Validity period
* Authorization reference

The Trust Engine determines whether that authorization evidence establishes execution eligibility for the current Intent.

Authorization information must retain sufficient provenance and temporal information.

⸻

28. Context and Policy

Policies are contextual inputs to evaluation.

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

The Context Engine may identify and retrieve applicable policy.

The Trust Engine determines the policy’s effect on execution eligibility.

Example:

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

29. Context and Capability

Capabilities are contextual to the requested Action.

Example:

Action:
REFUND_PAYMENT
Capability Registry:
refund_v2 = available

The Context Engine may establish capability availability and provide relevant metadata.

Trust evaluates whether the capability may be used for the specific Intent.

Capability availability may change over time.

Therefore capability Context may require refresh or revalidation.

⸻

30. Context and Time

Time is Context.

Relevant temporal information may include:

* current time
* execution window
* authorization validity
* approval expiration
* evidence freshness
* resource reservation
* policy effective date
* capability availability window

Temporal conditions should be represented explicitly where they materially affect evaluation.

Example:

Authorization:
valid_from = T1
valid_until = T2
Current Time:
T3
Result:
Authorization expired

Time-sensitive Context may therefore cause downstream Trust re-evaluation.

⸻

31. Context and Scope

Context may establish organizational, geographic, resource, or other scope.

Examples:

Actor:
employee_123
Organization:
company_A
Resource:
account_456
Scope:
company_A

Scope information may affect:

* authorization
* policy
* resource eligibility
* capability
* execution

Scope must be explicit where it materially affects the decision.

⸻

32. Context and Relationships

Some Intent evaluations depend on relationships rather than isolated facts.

Examples:

Actor ──owns──────> Resource
Actor ──manages───> Account
Customer ──has────> Subscription
Employee ──belongs_to──> Organization

The Context Engine may provide these relationships as contextual facts.

Relationship provenance should be retained when the relationship contributes materially to Validation or Trust.

⸻

33. Context Graph

A future implementation may represent Context as a graph.

Conceptually:

                 Actor
                  │
          ┌───────┼────────┐
          │       │        │
          ▼       ▼        ▼
      Resource   Role   Organization
          │
          ▼
        State
          │
          ▼
       Policy
          │
          ▼
      Capability

A graph model is useful where decisions depend on relationships across multiple entities.

The graph is an implementation option, not a canonical storage requirement.

⸻

34. Context Normalization

External systems may represent equivalent concepts differently.

For example:

Banking System:
ACTIVE
CRM:
active_customer

The Context Engine may normalize those representations into canonical Noema representations where an explicit mapping exists.

Normalization must preserve the original source representation.

Conceptually:

External Value
      │
      ▼
Explicit Mapping
      │
      ▼
Canonical Context Representation
      +
Source Provenance

Noema must not silently alter the semantics of an external fact.

⸻

35. Derived Context

Context may contain values derived from source facts.

Example:

Balance = ₦2M
Requested Transfer = ₦500K
Derived:
Remaining Balance = ₦1.5M

Derived Context must remain distinguishable from source facts.

Conceptually:

Source Facts
     │
     ▼
Deterministic Transformation
     │
     ▼
Derived Context

Where a derived value materially contributes to a decision, the derivation and source references should remain reconstructible.

⸻

36. Context Evidence

Context and Evidence are related but distinct.

A Context representation may contain a fact:

recipient_exists = true

while the Evidence supporting that fact may be:

Customer Registry Response

The Context Engine may assemble the contextual representation.

The Evidence model preserves the underlying support and provenance.

This distinction allows downstream Trust to determine whether the evidence is authoritative and sufficiently fresh.

⸻

37. Context and Operational Memory

Operational Memory may provide historical Context relevant to the current Intent.

Examples include:

* prior Intent versions
* prior clarifications
* previous execution attempts
* historical observations
* prior approvals
* previous Trust evaluations
* execution correlations

However:

Historical Context
≠
Current Truth

A previous observation may be useful for continuity without establishing current external state.

The Context Engine should therefore distinguish historical observations from current Context.

⸻

38. Context and Memory Freshness

Historical information retrieved from Operational Memory must retain its temporal characteristics.

Example:

10:00
Account balance = ₦100,000

does not establish:

11:00
Account balance = ₦100,000

unless the applicable semantics explicitly establish that the value remains valid.

Memory provides historical information.

The Context Engine determines whether that information is relevant to the current operation and whether it satisfies the applicable freshness requirements.

⸻

39. Context Snapshots

For consequential decisions, Noema should be able to reconstruct the relevant Context used at evaluation time.

Conceptually:

Context Snapshot
├── Intent Version
├── Facts
├── Evidence
├── Policies
├── Authorization
├── Capabilities
├── Temporal State
├── Historical References
└── Provenance

A Context Snapshot does not make Noema the permanent source of truth for external systems.

It preserves the decision environment sufficiently to support auditability and reconstruction.

⸻

40. Context Versioning

Context may change independently of Intent.

Therefore a Context representation used for a consequential evaluation should be identifiable by version, snapshot, or equivalent reference.

Example:

Intent Version:
7
Context Version:
42
Trust Evaluation:
evaluation_103

This allows historical decisions to be reconstructed without confusing later Context with earlier Context.

⸻

41. Context Dependencies

An Intent may depend on only a subset of available Context.

Example:

Intent I1
   ├── Actor
   ├── Account
   └── Balance
Intent I2
   ├── Actor
   ├── Customer
   └── Subscription

A change to subscription state should not necessarily invalidate I1.

Context dependencies should therefore be explicit where practical.

This supports selective acquisition and selective re-evaluation.

⸻

42. Context Materiality

Not every Context change is material.

A Context change is material when it can affect:

* Intent interpretation
* Validation
* Trust
* Action selection
* execution eligibility
* execution safety
* expected outcome

Therefore Noema should distinguish:

Context Change

from:

Material Context Change

Only material changes need to invalidate dependent decisions.

⸻

43. Context Invalidation

Context may become invalid because:

* source state changed
* evidence expired
* authorization was revoked
* policy changed
* capability became unavailable
* resource state changed
* Context was superseded
* source data became unavailable
* required freshness was exceeded

Conceptually:

Context Change
      │
      ▼
Identify Dependents
      │
      ▼
Invalidate Affected Evaluation
      │
      ▼
Re-acquire / Revalidate Context
      │
      ▼
Re-evaluate

The Context Engine does not itself determine whether the new Context produces approval or blocking.

That remains the responsibility of downstream components.

⸻

44. Context Refresh

Context refresh may be required when:

* an evaluation is retried
* an Intent changes
* a relevant dependency changes
* evidence expires
* authorization changes
* policy changes
* execution is delayed
* Context exceeds its freshness requirement
* a consumer requires current state

Refresh should be dependency-aware rather than indiscriminate.

A refresh must not silently replace the Context previously used for a consequential decision.

⸻

45. Context Re-Evaluation

Context changes may trigger downstream re-evaluation.

Conceptually:

Existing Context
      │
      ▼
Material Change
      │
      ▼
Context Refresh
      │
      ▼
Validation / Trust Re-evaluation

A Context change does not automatically imply:

APPROVED

or:

REJECTED

Its consequence must be determined by the applicable Validation and Trust rules.

⸻

46. Context Contract

A conceptual Context interface may expose:

GetContext(
    Intent,
    Requirements,
    Sources,
    Constraints
)
→ ContextResult

The operation is conceptual rather than a final API contract.

The result should make clear:

* what was requested
* what was acquired
* what was unavailable
* what remains unknown
* what conflicts exist
* where information came from
* when information was observed
* when information was retrieved
* whether freshness requirements were satisfied
* which requirements remain unsatisfied

⸻

47. Context Result

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

The important requirement is that materially different information states remain distinguishable.

⸻

48. Context State

The Context Engine may maintain its own lifecycle.

A conceptual lifecycle is:

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

Context state must remain separate from:

* Intent state
* Validation state
* Trust state
* Execution state

⸻

49. Context vs Trust State

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

50. Context vs Validation State

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

51. Context and LLMs

LLMs may assist in identifying potentially relevant Context.

For example:

User:
"Can I renew my card?"
Candidate Context:
- card
- card status
- expiry
- account
- eligibility policy

The model’s proposal is not authoritative.

Required Context should ultimately be established through:

* Intent schemas
* Action definitions
* policy requirements
* declared dependencies
* deterministic system requirements
* canonical architecture

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

The LLM may propose.

The Context architecture establishes what is actually required.

⸻

52. Context and Model-Derived Information

A model-generated assertion must not silently become a Context fact.

For example:

LLM:
"The customer probably owns this account."

is not equivalent to:

Authoritative Evidence:
Customer Registry establishes ownership.

Model-derived information may be represented as a candidate interpretation or derived signal where appropriate, but it must remain distinguishable from authoritative Context.

⸻

53. Context and Planning

The Execution Planner may consume Context relevant to Action selection.

Examples:

* available capabilities
* resource state
* execution constraints
* consumer requirements
* prior execution failures
* current environment

The Context Engine supplies the information.

The Execution Planner determines how the trusted objective can be fulfilled.

Planning must not convert contextual information into authority that Trust has not established.

⸻

54. Context and Composite Intents

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

Noema should not assume that a single global Context object is sufficient for every component.

⸻

55. Context and Partial Execution

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

Whether A and C may proceed depends on the semantics of the Composite Intent and execution contract.

The Context Engine does not infer permission for partial execution.

⸻

56. Context and Atomicity

Where multiple components depend on a shared Context condition, that dependency should be explicit.

For example:

Composite Intent
      │
      ├── Component A
      ├── Component B
      └── Component C
             │
             ▼
       Shared Resource

If the shared resource state changes materially, dependent Context may need to be refreshed for the affected components.

Atomicity remains an Intent and execution concern, not a Context decision.

⸻

57. Context Auditability

For consequential decisions, Noema should be able to answer:

* What Context was requested?
* Why was it required?
* Which sources were consulted?
* What facts were returned?
* Which facts were unknown?
* Which facts were unavailable?
* Which facts were stale?
* Which facts conflicted?
* Which Context contributed to the decision?
* When was it acquired?
* When was it observed?
* What authority did the source have?
* Which Context version or snapshot was used?

This supports Trust provenance and post-execution investigation.

⸻

58. Context Security

Context may contain sensitive enterprise information.

The Context Engine must therefore respect:

* access boundaries
* source permissions
* credential boundaries
* tenant boundaries
* organizational boundaries
* data minimization
* retention requirements
* security classifications

The Context Engine must not become an unrestricted enterprise data aggregation layer merely because Noema can technically access multiple systems.

⸻

59. Context Isolation

Where Noema operates across multiple tenants, organizations, or security domains, Context must remain appropriately isolated.

Conceptually:

Tenant A Context
       ≠
Tenant B Context

Context from one security domain must not silently influence an Intent in another.

Cross-domain access must be explicit and authorized.

⸻

60. Context Access

The existence of Context does not imply that Noema is authorized to retrieve it.

For example:

Context exists

does not mean:

Noema may retrieve Context

Acquisition is itself a controlled operation governed by:

* credentials
* permissions
* source authorization
* integration contracts
* applicable policy
* tenant boundaries

The Context Engine must therefore preserve the distinction between availability and accessibility.

⸻

61. Context Caching

Context may be cached where the applicable freshness requirements permit it.

Caching is not inherently safe or unsafe.

Its validity depends on the semantics of the consuming operation.

For example:

Static organization metadata

may tolerate longer caching than:

Account balance

Therefore cache validity should be determined by the semantic freshness requirement rather than a generic cache duration.

⸻

62. Context and Race Conditions

Context may change between:

Context Acquisition
        ↓
Validation
        ↓
Trust
        ↓
Execution

This creates potential time-of-check/time-of-use conditions.

Therefore:

Context at T1

does not guarantee:

Business state at T3

For consequential Actions, the execution consumer may need to perform final authoritative checks.

The Context Engine must not imply that a Context Snapshot guarantees successful execution.

⸻

63. Consumer-Side Context Validation

Execution consumers may perform final Context checks against authoritative live state.

Example:

Noema Context:
Account eligible
Execution Consumer:
Account state changed

The consumer may reject the Action.

This does not necessarily invalidate the Context used by Noema at the earlier evaluation time.

It demonstrates that external business state may change between evaluation and execution.

⸻

64. Context and Outcome

Context may support outcome verification.

Example:

Pre-execution:
Card status = ACTIVE
Action:
Replace Card
Post-execution:
Card status = REPLACED

The post-execution state remains authoritative in the external system.

Noema may retain the observed outcome and provenance without becoming the external system of record.

⸻

65. Context and Outcome Verification

Post-execution Context may be acquired to determine whether the reported execution outcome corresponds to the expected external state.

For example:

Execution:
accepted
Postcondition:
Payment Provider confirms settlement

The Context Engine may acquire the relevant authoritative evidence.

The Outcome layer determines the meaning of that evidence.

The Context Engine provides the information; it does not independently declare business success.

⸻

66. Context and Reconciliation

Where multiple Context sources represent the same domain fact, Noema may need explicit reconciliation semantics.

A reconciliation mechanism may consider:

* source authority
* observation time
* freshness
* version
* consistency
* conflict rules

The result should remain traceable to the underlying sources.

Reconciliation must not become an implicit preference for whichever source is easiest to access.

⸻

67. Context and Distributed Systems

The Context Engine operates across potentially distributed systems.

It should therefore account for:

* delayed responses
* duplicated responses
* reordered events
* eventual consistency
* partial availability
* stale reads
* network failures
* unknown source state
* conflicting observations

Stable identifiers and provenance should be used where necessary to distinguish these conditions.

⸻

68. Context and Event Ordering

Where Context is constructed from events, the system should retain sufficient ordering information.

Useful metadata may include:

* event ID
* sequence number
* source timestamp
* observation timestamp
* causation ID
* correlation ID

Wall-clock time alone may be insufficient to establish causal ordering in distributed systems.

⸻

69. Context and Causation

Where Context changes because of an identifiable event, the relationship may be retained.

For example:

account.status.changed
        │
        ▼
Context invalidated

or:

policy.changed
        │
        ▼
Applicable Context refreshed

Causation improves explainability and targeted re-evaluation.

⸻

70. Context Dependency Graph

A future implementation may explicitly represent Context dependencies:

Intent
 │
 ├── requires → Actor
 ├── requires → Resource
 ├── requires → Policy
 ├── requires → Authorization
 ├── requires → Capability
 └── requires → Evidence

Each dependency may identify:

* source
* authority
* freshness requirement
* access requirement
* validation rule
* downstream consumers
* invalidation triggers

This enables targeted Context acquisition and re-evaluation.

⸻

71. Context Events

A conceptual Context event vocabulary includes:

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

The architectural principle is that material Context changes must be representable and capable of triggering appropriate downstream re-evaluation.

⸻

72. Context Transition Principles

Context transitions should be:

* explicit
* traceable
* dependency-aware
* provenance-preserving
* distinguishable by cause
* compatible with freshness requirements

The system should not silently replace a Context Snapshot previously used for a consequential decision.

A new Context state should be identifiable as new information.

⸻

73. Context Consistency

The Context Engine must make its consistency semantics explicit.

For example, a Context assembled from several external systems may contain observations captured at different times:

Account:
observed_at = T1
Authorization:
observed_at = T2
Policy:
effective_at = T0

The Context Engine must not imply that all facts describe the external world at exactly the same instant unless that guarantee actually exists.

For consequential decisions, temporal differences between Context facts may themselves be decision-relevant.

⸻

74. Context Snapshot Integrity

When a Context Snapshot materially contributes to a consequential decision, the snapshot should be protected against silent modification.

The architecture should support sufficient guarantees around:

* integrity
* provenance
* versioning
* source references
* timestamps
* tenant isolation
* access control

The exact technical mechanism is implementation-specific.

⸻

75. Context Retention

Context retention should follow explicit policy.

Not every retrieved Context fact needs indefinite retention.

Retention may depend on:

* operational necessity
* audit requirements
* privacy requirements
* security requirements
* regulatory requirements
* contractual requirements
* sensitivity
* downstream reproducibility requirements

The Context Engine should avoid becoming an uncontrolled secondary copy of every connected system.

⸻

76. Context Privacy and Minimization

The Context Engine should acquire and retain only the information necessary for the declared operational purpose.

It should distinguish:

Required for operational continuity

from:

Available but unnecessary

Availability does not establish a retention requirement.

Where a reference is sufficient, Noema should prefer a reference over unnecessary duplication of sensitive data.

⸻

77. Context and Tenant Boundaries

Where Noema serves multiple organizations or tenants, Context retrieval must preserve tenant boundaries.

A Context fact belonging to Tenant A must not become available to an Intent belonging to Tenant B unless an explicit cross-tenant relationship and authorization exists.

Tenant isolation therefore applies not only to storage but also to:

* acquisition
* retrieval
* caching
* Context assembly
* Context snapshots
* downstream delivery

⸻

78. Context and Corrections

A source may later establish that an earlier Context observation was incorrect.

The architecture should preserve:

What Noema observed at the time

and:

What later evidence established

rather than silently rewriting the historical Context used by an earlier decision.

This allows consequential decisions to remain explainable even when the underlying Context later changes.

⸻

79. Context and Versioned Semantics

Context must be interpretable according to the schemas and mappings applicable when it was used.

Where necessary, Context should reference:

* Context schema version
* Intent schema version
* policy version
* Action version
* source schema version
* normalization mapping version
* capability version

This prevents historical Context from becoming semantically ambiguous as Noema evolves.

⸻

80. Context and Reproducibility

For consequential decisions, Noema should retain enough information to reconstruct the Context relevant to the decision.

This may include:

* Intent version
* Context Snapshot reference
* source references
* evidence references
* policy references
* authorization references
* capability references
* observation timestamps
* retrieval timestamps
* freshness evaluation
* normalization or transformation versions

Reproducibility does not necessarily require storing every input byte indefinitely.

It requires sufficient provenance to explain the Context available to the decision.

⸻

81. Context and Determinism

Context acquisition itself may be dynamic because external systems change.

Therefore the Context Engine cannot guarantee that repeated acquisition at different times produces identical results.

What must remain deterministic is the interpretation of a defined Context Snapshot by deterministic downstream components.

Conceptually:

Context Snapshot
+
Intent Version
+
Rules
+
Policy Version
        ↓
Deterministic Evaluation

The Context Engine should therefore preserve the snapshot and provenance used for consequential decisions.

⸻

82. Context and Failure Semantics

The Context Engine should expose meaningful failure distinctions.

At minimum, downstream systems may need to distinguish:

AVAILABLE

from:

UNKNOWN

from:

UNAVAILABLE

from:

STALE

from:

CONFLICTED

from:

INVALID

These states have materially different implications.

A generic:

FAILED

result should not erase decision-relevant distinctions where they can be preserved.

⸻

83. Context Must Not Manufacture Certainty

The Context Engine must never transform uncertainty into certainty merely to satisfy downstream requirements.

For example:

Customer Registry unavailable

must not become:

Customer does not exist

and:

Two possible recipients

must not become:

Recipient = John A

and:

Authorization unavailable

must not become:

Authorization granted

Uncertainty must remain explicit.

⸻

84. Context and Trust Fail-Closed Semantics

The Context Engine does not itself decide the final Trust state.

However, it must preserve unknown and unavailable conditions so that the Trust Engine can apply fail-closed semantics.

Conceptually:

Required Context
       ↓
Unavailable
       ↓
UNKNOWN
       ↓
Trust Evaluation
       ↓
WAITING / BLOCKED

Never:

Unavailable
       ↓
Assumed satisfied
       ↓
READY

The Trust Engine remains responsible for the final Trust decision.

⸻

85. Context Does Not Grant Authorization

A particularly important boundary is:

Context:
Actor previously performed Action successfully

does not establish:

Actor is authorized to perform Action now

Similarly:

Context:
Previous Trust = READY

does not establish:

Current Trust = READY

Historical Context can inform continuity.

It cannot silently transfer authority.

⸻

86. Context and Human Interaction

Human responses may become Context.

Examples include:

* clarification
* confirmation
* approval
* explicitly supplied parameters
* correction of previously stated information

However, the semantic role of each response must remain explicit.

For example:

Clarification

is not automatically:

Approval

and:

Confirmation

is not automatically:

Authorization

The receiving architectural component determines the consequence of the information.

⸻

87. Context and Human Agency

Context should support human agency by making relevant information available without silently converting inference into authority.

Where uncertainty materially affects an Actor’s objective, Noema should preserve that uncertainty and, where appropriate, request clarification or confirmation.

The Context Engine should therefore optimize for:

* relevance
* transparency
* provenance
* boundedness
* explicit uncertainty

rather than maximum information retrieval.

⸻

88. Context and Execution Boundary

The Context Engine supports execution but does not perform execution.

The architectural relationship is:

Intent
   ↓
Context
   ↓
Validation
   ↓
Trust
   ↓
Execution Planning
   ↓
Action Contract
   ↓
Execution Consumer
   ↓
External System

The execution consumer remains responsible for actual business-system mutation.

The Context Engine must not silently perform business Actions while acquiring Context.

⸻

89. Context Must Not Hide Side Effects

Context acquisition should have explicitly defined side-effect semantics.

Read operations intended to acquire Context should not silently mutate unrelated business state.

If a source interaction necessarily produces a side effect, that side effect must be represented explicitly in the relevant architecture.

The Context Engine must not become an implicit execution mechanism.

⸻

90. Context Anti-Patterns

Noema should avoid at least the following anti-patterns.

Anti-pattern 1 — Context as business truth

Retrieved observation
        ↓
Permanent current truth

Anti-pattern 2 — Context as authority

Role = manager
        ↓
Authorization granted

Anti-pattern 3 — Context as hidden model state

Retrieved information
        ↓
Invisible LLM influence

Anti-pattern 4 — Context as unrestricted data aggregation

Everything accessible
        ↓
Everything retrieved

Anti-pattern 5 — Context as certainty

Unknown
   ↓
Guess
   ↓
Fact

Anti-pattern 6 — Context as permanent freshness

Old observation
   ↓
Current state

Anti-pattern 7 — Context as Trust

Context complete
   ↓
READY

Anti-pattern 8 — Context as execution authority

Context says eligible
   ↓
Action executed

Context provides information.

Downstream architectural components determine its meaning and consequence.

⸻

91. Context Invariants

Invariant 1

Context is distinct from Intent.

Invariant 2

Context is not permission.

Invariant 3

Context is not Trust.

Invariant 4

Context is not authoritative business state merely because Noema retrieved it.

Invariant 5

Unknown Context must not be treated as established fact.

Invariant 6

Material Context must have sufficient provenance.

Invariant 7

Context freshness must be considered where decisions depend on time-sensitive information.

Invariant 8

Context acquisition must respect access boundaries.

Invariant 9

Context should be acquired according to explicit requirements rather than indiscriminately.

Invariant 10

Context may support clarification but must not manufacture certainty.

Invariant 11

Material Context changes may require downstream revalidation or Trust re-evaluation.

Invariant 12

Conflicting Context must not be silently reconciled without an explicit rule.

Invariant 13

Derived Context must remain distinguishable from source facts.

Invariant 14

Context completeness does not imply Validation success.

Invariant 15

Context completeness does not imply Trust readiness.

Invariant 16

Context availability does not guarantee execution success.

Invariant 17

Historical Context does not automatically establish current truth.

Invariant 18

Historical Trust does not automatically establish current Trust.

Invariant 19

Context from one tenant or security domain must not silently influence another.

Invariant 20

Consequential Context used for evaluation must remain reconstructible to the extent required by the applicable audit and governance requirements.

Invariant 21

Context acquisition must preserve the distinction between false, unknown, unavailable, stale, and conflicting information.

Invariant 22

The Context Engine does not execute business Actions.

⸻

92. Canonical Context Flow

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
          Noema State   Enterprise    External
                         Systems      Sources
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
          COMPLETE      INCOMPLETE     UNKNOWN
              │             │             │
              ▼             ▼             ▼
        Downstream      Clarify /      Not Ready /
        Evaluation      Acquire       Re-evaluate
              │
              ▼
         Validation
              │
              ▼
            Trust
              │
              ▼
           Planning
              │
              ▼
          Execution
              │
              ▼
            Outcome

The canonical flow is:

Determine requirements → Acquire → Assemble → Validate → Provide → Refresh when materially changed

⸻

93. Canonical Relationship to Other Architecture Components

The Context Engine relates to the major Noema components as follows:

Intent Engine
      │
      ├──────────────► Context Engine
      │
      ▼
Intent Resolution
      │
      ▲
      │
Context Engine
      │
      ├──────────────► Validation
      │
      ├──────────────► Trust Engine
      │
      ├──────────────► Execution Planner
      │
      └──────────────► Outcome Verification

The Context Engine provides relevant information without assuming responsibility for the decisions made by those components.

⸻

94. Canonical Mental Model

The Context Engine can be reduced to seven questions:

1. What Context does this Intent require?
2. Where does that Context come from?
3. Which source is authoritative for each material fact?
4. Is the Context available, valid, sufficiently fresh, and non-conflicting?
5. What remains unknown or unresolved?
6. What provenance supports each material contextual fact?
7. Which downstream decision depends on the Context, and when must it be refreshed?

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
Preserve Provenance
   ↓
Provide
   ↓
Refresh when materially changed

⸻

95. Fundamental Distinctions

Noema should preserve the following distinctions:

What does the Actor mean?
        ↓
Intent Engine
What context is relevant?
        ↓
Context Engine
Is the Intent valid?
        ↓
Validation
May the Intent proceed?
        ↓
Trust Engine
How should the objective be fulfilled?
        ↓
Execution Planner
What actually happened?
        ↓
Execution / Outcome
What is true in the external domain?
        ↓
Authoritative external system

The Context Engine connects these layers without collapsing their meanings.

⸻

96. Final Definition

The Context Engine is Noema’s architectural layer for determining, acquiring, assembling, validating, maintaining, and providing the contextual information required to resolve, validate, trust, plan, execute, and verify an Intent.

Its central invariant is:

Noema must distinguish what is known from what is unknown, where a fact came from, when it was observed, whether it remains sufficiently fresh, what authority the source has, and which decision depends upon it.

Context enables deterministic decision-making.

Context does not become the decision.

Context does not become authorization.

Context does not become Trust.

Context does not become external business truth.

The Context Engine provides the relevant information and preserves its provenance so that the appropriate downstream architectural component can make the corresponding decision.