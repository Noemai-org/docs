> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Entities

Status: Foundational
Version: 0.2
Domain: Ontology
Canonical Path: ontology/entities.md

⸻

1. Definition

An Entity is a distinct, identifiable thing that can be represented, referenced, related, observed, or acted upon within a Noema domain.

An Entity answers:

What distinct thing are we talking about?

Examples:

* Customer
* Account
* Card
* Subscription
* Payment
* Invoice
* Employee
* Organization
* Document
* Vehicle
* Order

An Entity may:

* participate in an Intent
* serve as the target of an Action
* provide or be represented within Context
* possess State
* participate in Relationships
* appear in an Outcome
* be subject to Constraints
* be subject to Authority and Policy
* be referenced by one or more system identifiers

The ontology must distinguish the thing being referred to from the language used to refer to it, the identifiers used by systems to represent it, and the permissions governing access to it.

⸻

2. Why Entities Exist

Natural language contains many nouns and noun phrases:

“Renew my expired Visa card linked to my primary account.”

A model may extract:

* Visa
* card
* primary account
* customer

But extraction alone does not establish which canonical domain objects those references denote.

The ontology therefore distinguishes:

Language Reference
      │
      ▼
Candidate Entity References
      │
      ▼
Candidate Entities
      │
      ▼
Entity Resolution
      │
      ▼
Canonical Entity

Entity extraction is not the same as Entity resolution.

Entity resolution is not the same as authorization.

Authorization is not the same as permission to assume identity.

These distinctions are material whenever an Entity is involved in consequential execution.

⸻

3. Entity vs Concept

A Concept describes a type, category, abstraction, or semantic class.

An Entity represents a distinct identifiable instance of such a Concept.

Example:

Concept:
Customer
Entity:
customer_12345

And:

Concept:
Payment
Entities:
payment_001
payment_002
payment_003

Therefore:

Concept describes what something is; Entity identifies which particular thing it is.

A Concept may have many Entity instances.

An Entity must not be confused with the definition of its type.

⸻

4. Entity vs Actor

An Actor is an Entity capable of participating in an Intent or causing or authorizing an Action according to the applicable model.

Conceptually:

Actor ⊂ Entity

But not every Entity is an Actor.

For example:

Customer        → may act as Actor
Employee        → may act as Actor
Organization    → may act as Actor
Account         → Entity
Card            → Entity
Invoice         → Entity
Payment         → Entity

Whether an Entity can act as an Actor depends on the relevant semantic and authority model.

Actor status does not automatically establish Authority.

⸻

5. Entity vs Resource

A Resource is an Entity that occupies the Resource role with respect to an Action, Context, or execution.

Conceptually:

Resource ⊂ Entity

where the Entity is actionable, inspectable, creatable, modifiable, or otherwise affected in the relevant context.

For example:

Entity:
Account
Action:
ReadAccountBalance
Role:
Resource

The distinction is contextual.

An Entity may exist without being a Resource for the Action under consideration.

Resource status does not itself establish authorization.

⸻

6. Entity vs Intent

An Intent represents what an Actor is trying to accomplish.

An Entity represents a thing involved in, referenced by, or affected by that objective.

Example:

Intent:
"Renew my card."
Entity:
Card #1234

The Intent defines the objective.

The Entity identifies what the objective concerns.

Therefore:

Intent ≠ Entity

An Intent may involve multiple Entities.

⸻

7. Entity vs Action

An Action represents an operation.

An Entity is often the subject, target, source, destination, or object of that operation.

Example:

Action:
RenewCard
Target Entity:
Card #1234

Therefore:

Entity ≠ Action

The Entity is what the Action operates upon or involves.

The Action is what is done.

⸻

8. Entity vs State

State describes the condition of an Entity at a particular point in time or within a relevant state model.

Example:

Entity:
Card #1234
State:
expired

The Entity remains conceptually distinct from its State.

For example:

Card
  │
  ├── active
  ├── expired
  ├── blocked
  └── cancelled

State may change while Entity identity remains continuous.

Therefore:

Entity Identity ≠ Entity State

The authoritative system remains responsible for authoritative Business State.

⸻

9. Entity Identity

An Entity must have an identity sufficient to distinguish it from other instances of the same Concept within the relevant domain.

Conceptually:

Entity
├── identity
├── type
├── identifiers
├── source
└── provenance

For example:

Entity Type:
Card
Entity Identity:
card_12345
Source:
Banking System

The exact identity and identifier mechanisms are implementation-specific.

The ontology requires semantic identity, not a particular storage technology.

⸻

10. Identity Is Not Identifier

An Identifier is a value used to reference an Entity.

Identity represents the semantic continuity of the Entity.

An Entity may have multiple identifiers across systems.

For example:

Card
 ├── Noema Identifier
 ├── Banking System Identifier
 ├── CRM Identifier
 └── External Reference

Therefore:

Entity Identity
        ≠
System Identifier

Noema must not assume that two identifiers represent different Entities merely because their values differ.

Conversely, Noema must not assume that equal-looking identifiers establish Entity identity without the relevant authority or resolution evidence.

⸻

11. Entity Types

Entities should be associated with a canonical Entity Type.

Examples:

* Customer
* Account
* Card
* Payment
* Invoice
* Order
* Subscription
* Organization
* Employee
* Document

Entity Types are Concepts.

Instances of those types are Entities.

Example:

Entity Type:
Card
Entities:
card_001
card_002
card_003

The canonical vocabulary for Entity Types belongs to the ontology.

⸻

12. Entity Attributes

An Entity may possess attributes.

For example:

Card
├── id
├── type
├── last_four
├── expiry_date
└── status

Attributes describe the Entity.

They are not necessarily independent Entities.

For example:

Card.status = expired

expired is a State value, not another Entity.

Attribute values may have their own:

* source
* authority
* provenance
* effective time
* observation time
* validity
* version

Noema should therefore distinguish Entity identity from the current values of its attributes.

⸻

13. Entity Relationships

Entities may be related to one another.

Example:

Customer
   │
   ├── owns ───────► Account
   │
   └── owns ───────► Card
                         │
                         └── linked_to ──► Account

Relationships are first-class semantic constructs.

They should not be represented merely as arbitrary strings embedded in model output.

A Relationship should preserve its:

* source Entity
* target Entity
* relationship type
* direction
* applicable scope
* provenance where material
* temporal validity where applicable

⸻

14. Common Entity Relationships

Examples include:

* owns
* owned_by
* belongs_to
* contains
* contains_item
* linked_to
* associated_with
* created_by
* managed_by
* assigned_to
* depends_on
* references
* parent_of
* child_of
* member_of
* located_at

The canonical relationship vocabulary should be defined separately.

This document establishes that relationships are semantic constructs; it does not define the complete relationship vocabulary.

⸻

15. Entity Relationships Are Directional

A Relationship has semantic direction.

For example:

Customer
   │
   └── owns ───► Account

is not necessarily equivalent to:

Account
   └── owns ───► Customer

The inverse may instead be:

Account
   └── owned_by ───► Customer

Noema must preserve Relationship semantics rather than infer inverse semantics from arbitrary language.

⸻

16. Entity Cardinality

Relationships may have cardinality.

Examples:

Customer
   └── owns ───► 0..N Accounts
Card
   └── linked_to ───► 1 Account

Cardinality may be material to Intent and Entity resolution.

For example:

“Cancel my account.”

If the Actor has five Accounts, the target Entity remains ambiguous unless additional Context or evidence resolves the reference.

Noema must not arbitrarily select one.

⸻

17. Entity Resolution

Entity Resolution is the process of determining which canonical Entity a reference refers to.

Example:

User:
"Renew my Visa card."
Candidate Entities:
- card_1234
- card_5678
- card_9012

Relevant Context and Evidence may establish:

card_1234

as the intended Entity.

Conceptually:

Natural Language Reference
        │
        ▼
Candidate Entities
        │
        ▼
Context + Evidence
        │
        ▼
Entity Resolution
        │
        ▼
Resolved Entity

A resolution result should be explicit when the Entity is material to subsequent execution.

⸻

18. Entity Ambiguity

Multiple Entities may match the same reference.

Example:

User:
"Cancel my subscription."
Entities:
subscription_pro
subscription_enterprise

If Context and Evidence cannot deterministically resolve the target:

Entity Ambiguity
      ↓
Clarification Required

Noema must not choose an Entity merely because one candidate has a higher model probability when the distinction is material to execution.

Ambiguity is a state requiring resolution, not an invitation to guess.

⸻

19. Entity Identity Across Systems

The same real-world Entity may appear in multiple enterprise systems.

For example:

Customer
   │
   ├── CRM ID: C123
   ├── Billing ID: B456
   ├── Support ID: S789
   └── Noema ID: N001

These may represent the same underlying Entity.

Noema therefore requires a distinction between:

Entity Identity
        ≠
System Identifier

Cross-system identity must be established according to the applicable identity and resolution mechanisms.

⸻

20. Entity Linking

Entity Linking associates a reference in an Intent or Context with a canonical Entity.

Example:

User:
"Use my primary account."
Reference:
"primary account"
Context:
Customer has:
- Savings Account
- Current Account
- Primary Account
Resolved Entity:
account_123

Entity Linking should preserve sufficient evidence and provenance to explain the basis of a material resolution.

⸻

21. Entity Resolution Confidence

Entity resolution may initially be probabilistic.

For example:

Candidate A: 0.82
Candidate B: 0.13
Candidate C: 0.05

Such scores may help prioritize candidates.

However:

Probability does not establish canonical Entity resolution when the distinction is material to execution.

Conceptually:

Probabilistic Candidate Resolution
             │
             ▼
Deterministic Validation
             │
       ┌─────┴─────┐
       ▼           ▼
   Resolved     Ambiguous

The confidence of a model is not itself authoritative evidence of Entity identity.

⸻

22. Entity Provenance

Entity identity, attributes, and material resolution decisions should preserve provenance where required.

For example:

Entity:
Customer N001
Source:
CRM
External ID:
C123
Resolved From:
"my customer account"

Provenance should allow Noema to establish:

* what was resolved
* from what reference
* using which information
* from which source
* at what time
* under which relevant version or authority

The purpose is traceability, not exposure of private model reasoning.

⸻

23. Entity Authority

Different systems may be authoritative for different attributes or domains of an Entity.

For example:

Customer
├── Name
│    └── CRM authoritative
│
├── Balance
│    └── Banking System authoritative
│
└── Subscription Status
     └── Billing System authoritative

Noema must not assume that one source is authoritative for every property of an Entity.

Authority may therefore exist at:

* Entity level
* Attribute level
* Domain level
* System level

The applicable authority must remain identifiable for material decisions.

⸻

24. Entity State

Entities may have State.

Example:

Card
   │
   └── State
       ├── active
       ├── expired
       ├── blocked
       └── cancelled

State changes do not necessarily create a new Entity.

For example:

Same Entity
    │
    ├── active
    ├── expired
    └── renewed

The authoritative system remains responsible for authoritative Business State.

Noema’s representation of State must not silently become the enterprise System of Record.

⸻

25. Entity Lifecycle

Entities may have a lifecycle.

Conceptually:

PROPOSED
   ↓
CREATED
   ↓
ACTIVE
   ↓
MODIFIED
   ↓
SUSPENDED
   ↓
DEACTIVATED

The lifecycle depends on the Entity Type.

Not every Entity has every lifecycle state.

Lifecycle state must remain distinct from:

* Entity identity
* Action state
* Execution state
* Outcome state

⸻

26. Entity Creation

Some Actions create Entities.

Example:

Action:
CreateSubscription
Result:
Subscription Entity

Conceptually:

Action
   ↓
Execution
   ↓
Outcome
   ↓
New Entity

Noema should distinguish:

Requested Entity
        ≠
Successfully Created Entity

until the authoritative enterprise system confirms creation.

A model-generated representation of a proposed Entity does not establish that the Entity exists.

⸻

27. Entity Mutation

Actions may modify existing Entities.

Example:

Action:
UpdateCustomerAddress
Target:
Customer #123

The Action modifies the Entity’s attributes or State.

It does not necessarily create a new Entity.

After consequential mutation, Noema may require fresh Context to establish the resulting enterprise State.

⸻

28. Entity Deletion

Deletion is a semantic operation affecting Entity lifecycle.

Example:

Action:
DeleteAccount
Target:
Account #123

The resulting semantics depend on the authoritative system.

Deletion may mean:

* hard deletion
* soft deletion
* deactivation
* anonymization
* archival

Noema should not infer which semantic applies without the relevant system or Action Contract.

A requested deletion is not evidence that deletion has occurred.

⸻

29. Entity Ownership

Entities may have ownership Relationships.

Example:

Customer
   │
   └── owns ───► Account

Ownership may influence:

* Authority
* Context
* Action eligibility
* Resource access
* Trust

But ownership itself must be represented as a Relationship.

It should not simply be inferred from Actor identity.

Ownership also does not automatically establish unrestricted authority over every operation involving the Entity.

⸻

30. Entity Membership

Some Entities participate in collections or organizational structures.

Example:

Employee
   │
   └── member_of ───► Organization

Membership may influence:

* Context
* Authority
* Policy applicability
* Resource scope

It does not necessarily establish ownership.

⸻

31. Entity Hierarchy

Entities may have hierarchical Relationships.

Examples:

Organization
   └── Department
          └── Team
                └── Employee

or:

Order
   └── Order Item
          └── Product

Hierarchy should be explicit.

Noema must not infer arbitrary parent-child Relationships from naming alone.

⸻

32. Entity Composition

An Entity may contain other Entities.

Example:

Order
 ├── OrderItem
 ├── OrderItem
 └── OrderItem

Composition differs from simple association.

If an Order is deleted, the lifecycle semantics of its Order Items depend on the domain model.

Noema should not infer cascading lifecycle behavior without an applicable domain or system specification.

⸻

33. Entity References

An Intent may refer to an Entity using different reference forms.

Explicit Identifier

“Cancel account 12345.”

Descriptive Reference

“Cancel my primary account.”

Relational Reference

“Cancel the account linked to my card.”

Deictic Reference

“Cancel this account.”

Implicit Reference

“Renew it.”

The last case requires Context to resolve the referenced Entity.

Reference form does not determine resolution by itself.

⸻

34. Entity Resolution and Context

Entity resolution is heavily dependent on Context.

Conceptually:

Reference
   +
Context
   +
Evidence
        ↓
Candidate Entities
        ↓
Entity Resolution

Example:

User:
"Renew my card."
Context:
Current conversation concerns card ending 1234.
Resolved Entity:
card_1234

Context may provide the information necessary for resolution, but Context itself does not make an Entity canonical.

⸻

35. Entity Resolution and Constraints

Constraints may narrow the candidate Entity set.

Example:

Intent:
"Renew my active card."
Candidates:
card_1234 → expired
card_5678 → active
card_9012 → cancelled

Applicable Constraint:

status = active

Candidate set becomes:

card_5678

Constraints therefore participate in Entity resolution where applicable.

However, a Constraint should not be used to manufacture an Entity that has not otherwise been established.

⸻

36. Entity Resolution and Authority

Authority may constrain which Entities an Actor can access or act upon.

Example:

Actor:
Finance Manager
Authority:
May modify corporate accounts.
Entities:
personal_account
corporate_account

The personal account may be excluded from actionable candidates.

Authority is not merely an Entity filter, however.

Entity resolution and Authority evaluation remain separate semantic operations.

Entity Resolution
        ↓
Authority Evaluation

An Entity can be correctly resolved without the Actor being authorized to act upon it.

⸻

37. Entity Resolution and Trust

Material Entity resolution should be established before Trust is granted to an Action targeting that Entity.

Conceptually:

Intent
  ↓
Entity Resolution
  ↓
Constraint / Authority Evaluation
  ↓
Trust
  ↓
Action

Noema should not execute:

“Delete my account”

while the target Account remains materially ambiguous.

The existence of a plausible candidate is not sufficient where deterministic resolution is required.

⸻

38. Entity and Resource Boundary

An Entity becomes a Resource when it occupies the Resource role for a particular operation.

Example:

Entity:
Account
Action:
ReadAccountBalance
Role:
Resource

Therefore:

Resource is a contextual role an Entity can occupy.

This distinction prevents the ontology from treating every Entity as permanently actionable.

⸻

39. Entity and Actor Boundary

Likewise:

Actor is a contextual role an Entity can occupy when it participates as a source of Intent or Action.

For example:

Organization
   │
   ├── Entity
   │
   └── Actor in a procurement Intent

The same Entity may therefore participate differently depending on Context and the relevant semantic role.

Actor role does not independently establish Authority.

⸻

40. Entity and Concept Boundary

The ontology should distinguish:

Concept
   │
   └── defines type
          │
          ▼
Entity
   │
   └── identifies instance

For example:

Concept:
Payment
Entities:
payment_001
payment_002
payment_003

A Concept is not made into an Entity merely because a model mentions it.

⸻

41. Entity and Relationship Model

The Noema ontology can therefore represent:

Entity
   │
   ├── has ─────────► Attribute
   │
   ├── has ─────────► State
   │
   ├── relates ─────► Entity
   │
   └── participates ─► Intent / Action / Outcome

This provides the semantic basis for a domain graph without requiring Noema to mandate a graph database.

The graph is an ontological representation, not a persistence requirement.

⸻

42. Entity Graph

A conceptual example:

Customer
   │
   ├── owns ─────────► Account
   │                     │
   │                     └── has ──► Balance
   │
   ├── owns ─────────► Card
   │                     │
   │                     └── linked_to ──► Account
   │
   └── has ──────────► Subscription

An Intent may traverse these Relationships:

“Renew the card linked to my primary account.”

Resolution:

Customer
   │
   └── owns
        ↓
Primary Account
        │
        └── linked_to
               ↓
             Card
               │
               ▼
          Target Entity

Relationship traversal must remain bounded by Context, Authority, Policy, and applicable Constraints.

⸻

43. Entity Canonicalization

Different references may identify the same Entity.

Examples:

“my main account”

“primary account”

“the account ending 4421”

“account 123”

These may resolve to:

account_123

Canonicalization should preserve:

* original reference
* resolved Entity
* resolution evidence
* source
* timestamp
* applicable Context
* relevant authority where material

Canonicalization must not erase the distinction between the original language reference and the canonical Entity.

⸻

44. Entity Merge

Multiple system records may later be determined to represent the same Entity.

For example:

CRM Customer C123
Billing Customer B456
Support Customer S789

may resolve to:

Canonical Customer N001

Entity merging must be deterministic and auditable.

Noema should preserve the underlying source identifiers and historical identity relationships.

A merge must not silently rewrite historical execution records.

⸻

45. Entity Split

Conversely, one previously identified Entity may later be discovered to represent multiple real-world Entities.

For example:

CRM Customer C123

may incorrectly contain data for two individuals.

The ontology must permit Entity identity correction without silently rewriting historical records.

Historical references must remain reconstructable according to the identity model applicable at the time.

⸻

46. Entity Temporal Identity

An Entity may persist across changes in attributes.

For example:

Customer:
Jane Doe
Name changes:
Jane Doe
   ↓
Jane Smith

The Entity may remain the same despite the attribute change.

Therefore:

Entity Identity
        ≠
Current Attribute Values

Identity must not be reconstructed solely from mutable attributes when a stronger identity mechanism exists.

⸻

47. Entity Versioning

Some Entities or representations may require versioning.

For example:

Document
   ├── Version 1
   ├── Version 2
   └── Version 3

Whether versions are separate Entities, representations of the same Entity, or States depends on the domain model.

Noema should not impose a universal interpretation.

Where versioning is material to execution, the relevant version must remain identifiable.

⸻

48. Entity Provenance and Audit

Material Entity operations should preserve provenance.

For example:

Entity:
account_123
Action:
UpdateAccountAddress
Actor:
customer_456
Execution:
execution_789
Outcome:
Address updated

This creates a traceable chain:

Actor
  ↓
Intent
  ↓
Entity
  ↓
Action
  ↓
Execution
  ↓
Outcome

The trace should distinguish:

* requested target
* resolved target
* authoritative target
* actual affected Entity
* resulting Outcome

where those differ.

⸻

49. Entity Security Boundary

Entity references may expose access-control boundaries.

Example:

Actor:
User A
Intent:
"Delete account 123."
Entity:
account_123

The existence of an Entity identifier does not establish that the Actor may access or modify it.

Therefore:

Entity Resolution
        ↓
Authorization
        ↓
Trust

Entity resolution and authorization must remain separate.

A successfully resolved Entity may still be unauthorized.

⸻

50. Entity and Privacy

Entity identity may involve sensitive information.

Noema should minimize unnecessary exposure of:

* identifiers
* personal attributes
* credentials
* financial information
* private relationships
* sensitive classifications

The ontology defines semantic identity.

It does not require all Entity attributes to be exposed to every component.

Entity resolution should therefore operate within applicable data-access and purpose boundaries.

⸻

51. Entity and Context

Entities are frequently represented within Context.

For example:

Context
   │
   ├── Principal
   ├── Intent
   ├── Candidate Entities
   ├── Resolved Entities
   ├── Relationships
   ├── Entity State
   └── Entity Attributes

Context provides information relevant to a decision.

It does not become the owner of the Entity.

Likewise:

Context Entity Representation
        ≠
Canonical Enterprise Entity

The authoritative system remains responsible for the underlying enterprise Entity and its authoritative attributes.

⸻

52. Entity and Evidence

Evidence may support claims about Entity identity, attributes, relationships, or state.

For example:

Claim:
account_123 is the customer's primary account.
Evidence:
Customer profile from authoritative system.
Observed:
2026-09-01
Version:
482

Therefore:

Entity
   +
Evidence
   +
Provenance

may establish the basis for a material Entity resolution.

Evidence and Entity identity remain distinct concepts.

⸻

53. Entity and Constraints

Constraints may apply to Entities or restrict which Entities may participate in an Action.

Examples:

Only accounts owned by the requesting organization.
Only active cards may be renewed.
Only invoices belonging to the current tenant may be modified.

Constraints may therefore narrow the set of permissible Entity targets.

However:

Constraint
        ≠
Entity

A Constraint limits permissible operations or candidates; it does not create or identify the Entity itself.

⸻

54. Entity and Authority

Authority determines what an Actor or Principal is permitted to cause with respect to an Entity.

For example:

Entity:
Corporate Account
Actor:
Finance Manager
Authority:
May initiate transfers from corporate accounts.

The Authority relationship does not alter the Entity’s identity.

Likewise:

Entity Existence
        ≠
Entity Accessibility
        ≠
Entity Actionability
        ≠
Authority

These distinctions must remain explicit.

⸻

55. Entity and Capability

A Capability describes what an executing system can technically or operationally do.

For example:

Capability:
payments.transfer.create

An Entity may be a valid target of that Capability.

But:

Capability
        ≠
Entity Authority

The existence of a Capability does not establish that a particular Actor may use it against a particular Entity.

Capability, Authority, Constraint, and Trust must therefore remain distinct.

⸻

56. Entity and Outcome

An Outcome records what resulted from an Action or Execution.

For example:

Action:
CreateSubscription
Target:
Customer_123
Outcome:
Subscription_456 created

The requested Entity, targeted Entity, affected Entity, and Entity appearing in the Outcome may differ.

Noema must not infer successful Entity mutation or creation merely from an Action request.

The authoritative system must establish the resulting enterprise state where required.

⸻

57. Entity Model

Conceptually:

Entity
├── identity
├── type
├── identifiers
├── attributes
├── relationships
├── state
├── source
├── authority
├── temporal validity
└── provenance

This is an ontology-level semantic model.

It is not a persistence schema.

Implementations may represent these semantics differently.

⸻

58. Entity Resolution Model

Conceptually:

Reference
   │
   ▼
Candidate Entity Set
   │
   ├── Context
   ├── Evidence
   ├── Relationships
   ├── Constraints
   └── Authority
        │
        ▼
Resolution Decision
        │
   ┌────┴─────┐
   ▼          ▼
Resolved   Ambiguous

A resolution decision should be explicit when material.

Possible semantic outcomes may include:

* Resolved
* Ambiguous
* Unresolved
* Not Found
* Conflicting
* Insufficient Evidence

The exact operational state vocabulary belongs to the relevant resolution and Trust specifications.

⸻

59. Entity Lifecycle Model

Conceptually:

Referenced
    ↓
Candidate
    ↓
Resolved
    ↓
Validated
    ↓
Targeted
    ↓
Affected
    ↓
Observed Outcome

Not every Entity passes through every stage.

These stages describe the Entity’s role in an execution journey.

They must not be confused with the Entity’s own enterprise lifecycle.

For example:

Entity Lifecycle:
ACTIVE
Noema Execution Role:
TARGETED

Both may be true simultaneously.

⸻

60. Entity Identity Correction

Entity identity may require correction when new authoritative information becomes available.

Examples include:

* duplicate detection
* incorrect linking
* Entity merge
* Entity split
* cross-system reconciliation
* identifier correction

Corrections must preserve historical traceability.

Noema should distinguish:

Current Canonical Identity
        ≠
Historical Identity Assertion

Historical execution records must remain interpretable according to the identity information applicable when the execution occurred.

⸻

61. Entity Existence vs Representation

A representation of an Entity is not necessarily proof that the Entity currently exists in the authoritative enterprise domain.

For example:

Model:
"Subscription created."

does not establish:

Enterprise:
Subscription exists.

Similarly:

Context:
account_123

does not by itself establish current canonical existence.

Where Entity existence is material, Noema should rely on the applicable authoritative source or evidence.

⸻

62. Entity and Staleness

Entity information may become stale.

For example:

Context at 10:00:
Card.status = active
Enterprise at 10:05:
Card.status = blocked

The Entity identity may remain correct while its State representation becomes stale.

Therefore:

Entity Identity
        ≠
Freshness of Entity Information

Noema must evaluate freshness independently when current Entity State is material to execution.

⸻

63. Entity and Temporal Validity

Entity relationships, attributes, and representations may have temporal validity.

For example:

Customer
   │
   └── primary_account ──► Account A
       Valid:
       2026-01-01 → 2026-06-30

After that period:

Customer
   │
   └── primary_account ──► Account B

Noema must distinguish historical relationships from current relationships.

Temporal validity is therefore part of Entity semantics where the domain requires it.

⸻

64. Entity and Data Minimization

Entity resolution does not require exposing every attribute of every candidate Entity.

For example, resolving:

“my current account”

may require:

* account identifier
* account status
* ownership relationship
* account role

It may not require:

* full transaction history
* home address
* unrelated customer information

Noema should retrieve only the Entity information necessary for the current purpose.

This follows the broader Context principle of purpose-bound information.

⸻

65. Entity and Tenant / Organizational Boundaries

Entity identity and Entity access may be bounded by:

* tenant
* organization
* legal entity
* business unit
* environment
* data classification
* resource ownership

The same identifier or Entity Type may exist across organizational boundaries without representing an Entity that the current Actor may access.

Noema must therefore preserve organizational and tenancy scope during Entity resolution.

⸻

66. Entity and Ambiguous Identity

An Entity reference may remain unresolved even when several plausible candidates exist.

Example:

Reference:
"my account"
Candidates:
Account A
Account B
Account C

The correct semantic state is:

Multiple Candidate Entities
        ↓
Ambiguous

not:

Most likely Entity

when the Entity distinction is consequential.

Noema should preserve candidate identity until sufficient Context, Evidence, deterministic rules, or explicit clarification resolves the ambiguity.

⸻

67. Entity and Human Clarification

Human clarification may supply information necessary for Entity resolution.

Example:

User:
"Show my statement."
Context:
Account A
Account B
       ↓
Noema:
"Which account would you like the statement for?"
       ↓
User:
"My current account."
       ↓
Updated Context
       ↓
Entity Resolution

The clarification becomes additional Context.

It does not automatically become authoritative enterprise data.

⸻

68. Entity and Probabilistic Models

Models may assist with:

* Entity extraction
* candidate generation
* Entity linking
* reference interpretation
* relationship identification

For example:

User:
"the card I used yesterday"
Model:
Candidate cards:
card_123
card_456

The model may generate useful candidates.

However:

Model confidence is not Entity authority.

Material Entity resolution must be validated through applicable Context, Evidence, Authority, Constraints, or explicit clarification.

⸻

69. Entity and Bounded Autonomy

Entity resolution is a fundamental boundary on autonomous execution.

An autonomous system must not merely know:

“What operation should I perform?”

It must also know:

“Which Entity is that operation actually about?”

Conceptually:

Intent
   │
   ▼
Candidate Entities
   │
   ▼
Entity Resolution
   │
   ▼
Constraints / Authority
   │
   ▼
Trust
   │
   ▼
Action

An Action targeting an unresolved material Entity must not cross the Trust boundary merely because the model can produce a plausible target.

⸻

70. Entity and Action Targeting

An Action may target one or more Entities.

Conceptually:

Action
├── Actor
├── Target Entity
├── Source Entity
├── Destination Entity
└── Related Entities

These roles must remain semantically distinct.

For example:

TransferFunds
Source:
Account A
Destination:
Account B
Actor:
Customer C

The Actor, source Entity, and destination Entity are different semantic roles even when they are related.

⸻

71. Entity and Action Preconditions

Entity State and attributes may participate in Action Preconditions.

Example:

Action:
RenewCard
Target:
card_123
Precondition:
card.status = expired

The Entity identifies the target.

The State provides the relevant condition.

The Precondition establishes what must be true for the Action to proceed.

Therefore:

Entity
   +
State
   +
Precondition

must not be collapsed into one concept.

⸻

72. Entity and Postconditions

An Action may produce changes to an Entity.

Example:

Action:
RenewCard
Target:
card_123
Expected Postcondition:
card.status = active

The Action itself does not establish that the Postcondition occurred.

Noema must obtain sufficient authoritative evidence after execution when verification is material.

Conceptually:

Action
   ↓
Enterprise Execution
   ↓
Entity State Change
   ↓
Fresh Context / Evidence
   ↓
Postcondition
   ↓
Outcome

⸻

73. Entity and Execution Reconciliation

When execution fails or times out, the Entity may have changed even when Noema does not know whether the Action completed.

Example:

Action:
UpdateAccount
       ↓
Timeout
       ↓
Noema:
Execution Result = UNKNOWN

Noema must not assume:

Entity unchanged

or:

Entity changed

without appropriate evidence.

Instead:

Unknown Execution Result
        ↓
Refresh / Reconcile Entity State
        ↓
Determine Actual State

This is particularly important for non-idempotent Actions.

⸻

74. Entity and Historical Reconstruction

Historical Entity information may be necessary to reconstruct an earlier execution.

Conceptually:

Historical Intent
       +
Historical Context
       +
Historical Entity Resolution
       +
Historical Evidence
       +
Historical Policy
       ↓
Historical Decision

Historical identity and relationships must remain distinguishable from their current values.

This allows Noema to answer:

Which Entity did Noema believe it was acting upon at the time?

without incorrectly substituting today’s Entity relationships.

⸻

75. Entity Canonicality

A canonical Entity is an Entity whose identity has been established within the applicable authority and domain boundaries.

Canonicality should not be inferred solely from:

* model confidence
* frequency of occurrence
* textual similarity
* identifier resemblance
* recency
* majority vote
* presence in Context

Canonicality must be grounded in the applicable identity, resolution, and authority mechanisms.

⸻

76. Entity Model Boundaries

The Entity ontology establishes semantic identity and participation.

It does not itself define:

* authentication
* authorization policy
* Action execution
* enterprise persistence
* database schemas
* API protocols
* identity-provider implementation
* Trust thresholds
* business-specific Entity Types

Those concerns belong to their respective canonical domains.

⸻

77. Canonical Distinctions

Noema must preserve:

Entity       ≠ Concept
Entity       ≠ Intent
Entity       ≠ Action
Entity       ≠ State
Entity       ≠ Identifier
Entity       ≠ Actor
Entity       ≠ Resource
Entity       ≠ Context
Entity       ≠ Evidence
Entity       ≠ Authority
Entity       ≠ Capability
Entity       ≠ Outcome

And:

Entity Resolution
        ≠
Authorization

And:

Entity Existence
        ≠
Entity Accessibility

And:

Entity Identity
        ≠
Attribute Values

And:

Entity Identity
        ≠
Entity State

And:

Entity Representation
        ≠
Canonical Enterprise Entity

And:

Model Confidence
        ≠
Canonical Identity

⸻

78. Core Invariants

Invariant 1

An Entity is a distinct identifiable thing within a domain.

Invariant 2

A Concept defines a type; an Entity represents an instance.

Invariant 3

Not every Entity is an Actor.

Invariant 4

Not every Entity is a Resource.

Invariant 5

Entity identity must remain distinct from system-specific identifiers.

Invariant 6

An Entity may have multiple identifiers across systems.

Invariant 7

Entity resolution must be distinguished from authorization.

Invariant 8

Ambiguous Entity resolution must not silently become deterministic selection.

Invariant 9

Material Entity resolution must preserve sufficient evidence and provenance.

Invariant 10

Entity attributes may change without changing Entity identity.

Invariant 11

Entity State must remain distinct from Entity identity.

Invariant 12

The authoritative system for an Entity or its attributes must remain identifiable.

Invariant 13

Entity Relationships must be semantically explicit.

Invariant 14

Noema must not infer ownership, membership, or Authority merely from Entity identity.

Invariant 15

An Entity must be resolved before a material Action targeting that Entity is trusted for execution.

Invariant 16

The existence of an Entity does not imply that the current Actor is authorized to access or modify it.

Invariant 17

Probabilistic Entity resolution may generate candidates but must not silently establish material identity where deterministic resolution is required.

Invariant 18

Historical Entity identity must remain auditable when Entities are merged, split, or re-canonicalized.

Invariant 19

An Entity representation in Context does not become canonical enterprise state merely because Noema stores or consumes it.

Invariant 20

Entity attributes and State may have different authorities from Entity identity.

Invariant 21

Entity freshness must be evaluated independently from Entity identity.

Invariant 22

A resolved Entity does not automatically become an authorized Resource.

Invariant 23

Constraints may narrow Entity candidates but must not manufacture Entity identity.

Invariant 24

Model confidence must not substitute for authoritative Entity resolution when the distinction is material.

Invariant 25

Entity references must preserve sufficient scope to prevent cross-tenant, cross-organization, or cross-domain resolution where such boundaries apply.

Invariant 26

Entity relationships must preserve direction and, where material, temporal validity.

Invariant 27

A requested Entity mutation or creation does not establish that the Entity was actually created or modified.

Invariant 28

After an uncertain or failed execution, Noema must not infer the resulting Entity State without sufficient evidence.

Invariant 29

Historical Entity identity and relationships must remain distinguishable from current Entity identity and relationships.

Invariant 30

Noema must preserve the distinction between an Entity, the representation of that Entity, and the authoritative enterprise record of that Entity.

Invariant 31

Material Entity resolution must remain within applicable Context, authorization, privacy, tenancy, organizational, and Policy boundaries.

Invariant 32

An Entity may participate in different semantic roles without those roles becoming properties that permanently redefine the Entity.

Invariant 33

Entity existence, Entity accessibility, Entity actionability, and Authority must remain distinct.

Invariant 34

Entity resolution must be sufficiently established before an Action can be trusted when the Entity is material to the Action.

Invariant 35

Noema must preserve uncertainty about Entity identity rather than manufacture certainty when authoritative resolution is unavailable.

⸻

79. Relationship to Other Ontology Documents

This document defines the general semantics of Entities.

Related documents:

01-ontology/
├── concepts.md
├── entities.md
├── actor.md
├── action.md
├── capability.md
├── intent.md
├── context.md
├── constraint.md
├── policy.md
├── authority.md
├── resource.md
├── state.md
├── outcome.md
└── relationships.md

The important relationship is:

Concept
   ↓
Entity
   │
   ├── may become Actor
   ├── may become Resource
   ├── has State
   ├── has Attributes
   ├── participates in Intent
   ├── is targeted by Action
   ├── participates in Relationships
   └── appears in Outcome

Entity resolution also connects directly to:

Context
Evidence
Constraints
Authority
Trust

because material execution depends on knowing which Entity the Intent concerns and whether that Entity may legitimately be acted upon.

⸻

80. Relationship to Trust

Entity resolution is upstream of Trust when Entity identity is material.

Conceptually:

Intent
   │
   ▼
Entity Resolution
   │
   ├── unresolved ─────► Clarification / Escalation
   │
   └── resolved
          │
          ▼
    Context / Evidence
          │
          ▼
 Constraints / Authority
          │
          ▼
        Trust
          │
          ▼
        Action

Trust therefore should not be interpreted as independently validating an unresolved target.

A system cannot safely determine whether an Actor is authorized to perform an Action against an Entity if the relevant Entity itself remains materially ambiguous.

⸻

81. Relationship to Bounded Execution

Entity identity is one of the boundaries that converts an open-ended natural-language request into a bounded execution target.

For example:

USER
 │
 ▼
INTENT
 │
 ▼
ENTITY REFERENCE
 │
 ▼
CANDIDATE ENTITIES
 │
 ▼
ENTITY RESOLUTION
 │
 ▼
CONSTRAINTS + AUTHORITY
 │
 ▼
TRUST
 │
 ▼
ACTION
 │
 ▼
ENTERPRISE
 │
 ▼
FRESH ENTITY STATE
 │
 ▼
POSTCONDITION
 │
 ▼
OUTCOME

This prevents a model from moving directly from:

“the account”

to:

“account_123”

without the intermediate semantic and authorization boundaries required by Noema.

⸻

82. Canonical Summary

An Entity is a distinct, identifiable thing that can participate in, be referenced by, or be affected by an Intent, Action, or Outcome within a Noema domain.

The core model is:

Concept
   │
   │ defines type
   ▼
Entity
   │
   ├── has ─────────► State
   ├── has ─────────► Attributes
   ├── relates to ──► Entity
   │
   ├── may act as ──► Actor
   └── may serve as ► Resource

The operational resolution model is:

Natural Language Reference
          │
          ▼
   Candidate Entities
          │
          ▼
Context + Evidence + Relationships
          │
          ▼
   Entity Resolution
          │
          ├── unresolved / ambiguous
          │          │
          │          ▼
          │      Clarification
          │
          ▼
Constraints + Authority
          │
          ▼
        Trust
          │
          ▼
        Action
          │
          ▼
     Enterprise System
          │
          ▼
     Fresh Entity State
          │
          ▼
     Postcondition
          │
          ▼
        Outcome

The most important operational boundary is:

Noema must know not only what an Actor wants to do, but which Entity that Intent is actually about before the Intent crosses the Trust boundary.

And the corresponding ontology rule is:

Entity identity must remain distinct from language references, system identifiers, Context representations, State, Authority, and model confidence.

Noema may extract, link, canonicalize, and reason about Entities, but it must preserve the identity, authority, provenance, temporal validity, organizational scope, and uncertainty of those Entities throughout the execution journey.

⸻

Update result

I have not shortened the supplied Entity specification. The update preserves its original semantic coverage and 57-section progression while extending the areas that matter to the emerging Noema Canon:

* Entity ↔ Context is now explicit rather than leaving Entity representation inside Context implicit.
* Entity ↔ Evidence is separated from Entity identity and resolution.
* Entity ↔ Authority is separated from both resolution and accessibility.
* Entity ↔ Capability is separated from technical ability to operate on an Entity.
* Entity ↔ Outcome now distinguishes requested/targeted Entity from actually affected Entity.
* Entity existence vs representation is made explicit.
* Entity freshness is separated from Entity identity.
* Temporal Entity relationships are explicitly recognized.
* Entity identity correction covers merge, split, and re-canonicalization without destroying history.
* Execution reconciliation is added for the important case where an Action times out or returns an unknown result.
* Action targeting distinguishes Actor, source, destination, target, and related Entities.
* Precondition/Postcondition semantics are tied back to Entity and Entity State.
* The invariants have been strengthened from 18 to 35, particularly around canonicality, authority, uncertainty, organizational boundaries, and the distinction between enterprise truth and Noema’s representations.
* The central Noema boundary is now explicit: Entity Resolution → Constraints/Authority → Trust → Action, rather than allowing Entity resolution to collapse into model inference.

The resulting entities.md is therefore still an ontology document, not a storage/schema document, while giving Entity the stronger role it needs as the identity boundary between natural-language Intent and bounded enterprise execution.