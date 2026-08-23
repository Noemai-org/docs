Yes. I’d make entities.md the ontology-level definition of what can exist as a distinct identifiable thing in Noema. This is important because we don’t want every noun extracted from a user’s request to become an entity, and we don’t want entities to collapse into Actors, Resources, or Concepts.

Entities

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/entities.md

⸻

1. Definition

An Entity is a distinct, identifiable thing that can be represented, referenced, related, observed, or acted upon within a Noema domain.

An Entity answers:

What distinct thing are we talking about?

Examples:

Customer
Account
Card
Subscription
Payment
Invoice
Employee
Organization
Document
Vehicle
Order

An Entity may participate in an Intent, serve as the target of an Action, provide Context, possess State, or appear in an Outcome.

⸻

2. Why Entities Exist

Natural language contains many nouns:

“Renew my expired Visa card linked to my primary account.”

A model may extract:

Visa
card
primary account
customer

But Noema must determine which of these represent actual domain Entities.

The ontology therefore distinguishes:

Language Term
      │
      ▼
Candidate Entity
      │
      ▼
Entity Resolution
      │
      ▼
Canonical Entity

Entity extraction is not the same thing as Entity resolution.

⸻

3. Entity vs Concept

A Concept describes a type or abstract idea.

An Entity represents a distinct identifiable instance.

Example:

Concept:
Customer
Entity:
customer_12345
Concept:
Payment
Entity:
payment_98765

Therefore:

Concept describes what something is; Entity identifies which particular thing it is.

⸻

4. Entity vs Actor

An Actor is an entity capable of participating in an Intent or causing an Action.

Therefore:

Actor ⊂ Entity

conceptually.

But not every Entity is an Actor.

For example:

Customer        → Actor
Bank            → Actor
Account         → Entity
Card            → Entity
Invoice         → Entity
Payment         → Entity

An Account cannot independently express Intent merely because it is an Entity.

⸻

5. Entity vs Resource

A Resource is an Entity that an Action can operate on, inspect, create, modify, or otherwise affect.

Therefore:

Resource ⊂ Entity

in contexts where the Entity is actionable.

For example:

Entity:
Customer
Resource:
Customer record being updated

The distinction is contextual.

An Entity may exist without currently being a Resource for the Action under consideration.

⸻

6. Entity vs Intent

Intent represents an objective.

An Entity represents a thing involved in that objective.

Intent:
"Renew my card."
Entity:
Card #1234

The Intent describes what the Actor wants.

The Entity identifies what the Intent concerns.

⸻

7. Entity vs Action

An Action represents an operation.

An Entity is often the subject or target of that operation.

Action:
RenewCard
Target Entity:
Card #1234

Therefore:

Entity ≠ Action

⸻

8. Entity vs State

State describes the condition of an Entity.

Entity:
Card #1234
State:
expired

The Entity persists conceptually while its State may change.

Card
  │
  ├── State: active
  │
  ├── State: expired
  │
  └── State: cancelled

State and Entity must therefore remain distinct.

⸻

9. Entity Identity

An Entity must have an identity sufficient to distinguish it from other instances of the same Concept.

Conceptually:

Entity
├── entity_type
├── entity_id
├── source
└── provenance

For example:

entity_type:
Card
entity_id:
card_12345
source:
Banking System

The exact identifier format is implementation-specific.

⸻

10. Identity Is Not Identifier

An Identifier is a value used to reference an Entity.

Identity represents the semantic continuity of the Entity.

For example:

Card:
entity_id = card_12345
External ID:
411111******

An Entity may have multiple identifiers across systems.

Card
 ├── Noema ID
 ├── Banking System ID
 ├── CRM ID
 └── External Reference

Noema should not assume that two identifiers represent different Entities merely because their values differ.

⸻

11. Entity Types

Entities should be associated with a canonical Entity Type.

Examples:

Customer
Account
Card
Payment
Invoice
Order
Subscription
Organization
Employee
Document

Entity Types are concepts.

Instances of those types are Entities.

Entity Type:
Card
Entities:
card_001
card_002
card_003

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

expired is a state value, not another Entity.

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

They should not be represented merely as arbitrary strings.

⸻

14. Common Entity Relationships

Examples include:

owns
belongs_to
contains
contains_item
linked_to
associated_with
created_by
managed_by
assigned_to
depends_on
references
parent_of
child_of
member_of
located_at

The canonical relationship vocabulary should be defined separately.

⸻

15. Entity Relationships Are Directional

A relationship has semantic direction.

Customer
   │
   └── owns ───► Account

This is not necessarily equivalent to:

Account
   └── owns ───► Customer

The inverse relationship may instead be:

Account
   └── owned_by ───► Customer

Noema should preserve relationship semantics rather than infer them from arbitrary language.

⸻

16. Entity Cardinality

Relationships may have cardinality.

Examples:

Customer
   └── owns ───► 0..N Accounts
Card
   └── linked_to ───► 1 Account

Cardinality may be important to Intent resolution.

For example:

“Cancel my account.”

If the Actor owns five accounts, the target Entity is ambiguous.

Noema must not arbitrarily select one.

⸻

17. Entity Resolution

Entity Resolution is the process of determining which canonical Entity a reference refers to.

Example:

User:
"Renew my Visa card."
Candidate references:
- card_1234
- card_5678
- card_9012

Context may establish:

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
Resolved Entity

⸻

18. Entity Ambiguity

Multiple Entities may match a reference.

Example:

User:
"Cancel my subscription."
Entities:
subscription_pro
subscription_enterprise

If Context cannot deterministically resolve the target:

Entity Ambiguity
      ↓
Clarification Required

Noema must not choose an Entity merely because one candidate has a higher model probability.

⸻

19. Entity Identity Across Systems

The same real-world Entity may appear in multiple systems.

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

Entity linking should preserve the evidence supporting the resolution.

⸻

21. Entity Resolution Confidence

Entity resolution may initially be probabilistic.

For example:

Candidate A: 0.82
Candidate B: 0.13
Candidate C: 0.05

These scores may help prioritize candidates.

But:

Probability does not establish canonical Entity resolution when the distinction is material to execution.

Noema may require deterministic evidence or clarification.

Probabilistic Candidate Resolution
             │
             ▼
Deterministic Validation
             │
       ┌─────┴─────┐
       ▼           ▼
   Resolved     Ambiguous

⸻

22. Entity Provenance

Entity identity and attributes should have provenance where material.

For example:

Entity:
Customer N001
Source:
CRM
External ID:
C123
Resolved from:
"my customer account"

Provenance helps answer:

Why does Noema believe this is the Entity being referenced?

⸻

23. Entity Authority

Different systems may be authoritative for different Entity attributes.

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

Authority may therefore exist at the attribute or domain level.

⸻

24. Entity State

Entities may have State.

Card
   │
   └── State
       ├── active
       ├── expired
       ├── blocked
       └── cancelled

State changes do not necessarily create a new Entity.

Same Entity
    │
    ├── active
    ├── expired
    └── renewed

The authoritative system remains responsible for the business state.

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

Not every Entity has every state.

⸻

26. Entity Creation

Some Actions create Entities.

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

until the authoritative system confirms creation.

⸻

27. Entity Mutation

Actions may modify existing Entities.

Action:
UpdateCustomerAddress
Target:
Customer #123

The Action modifies the Entity’s state or attributes.

It does not necessarily create a new Entity.

⸻

28. Entity Deletion

Deletion is a semantic operation affecting Entity lifecycle.

Action:
DeleteAccount
Target:
Account #123

The resulting business semantics depend on the authoritative system.

Deletion may mean:

Hard deletion
Soft deletion
Deactivation
Anonymization
Archival

Noema should not infer which semantic applies without the relevant system contract.

⸻

29. Entity Ownership

Entities may have ownership relationships.

Customer
   │
   └── owns ───► Account

Ownership may influence:

* Authority
* Context
* Action eligibility
* Resource access
* Trust

But ownership itself must be represented as a relationship.

It should not simply be inferred from Actor identity.

⸻

30. Entity Membership

Some Entities participate in collections or organizational structures.

Employee
   │
   └── member_of ───► Organization

Membership may influence Context and Authority.

It does not necessarily establish ownership.

⸻

31. Entity Hierarchy

Entities may have hierarchical relationships.

Examples:

Organization
   └── Department
          └── Team
                └── Employee

Or:

Order
   └── Order Item
          └── Product

Hierarchy should be explicit.

Noema must not infer arbitrary parent-child relationships from naming alone.

⸻

32. Entity Composition

An Entity may contain other Entities.

Order
 ├── OrderItem
 ├── OrderItem
 └── OrderItem

Composition differs from simple association.

If an Order is deleted, the lifecycle semantics of its Order Items depend on the domain model.

⸻

33. Entity References

An Intent may refer to an Entity using:

Explicit Identifier

"Cancel account 12345."

Descriptive Reference

"Cancel my primary account."

Relational Reference

"Cancel the account linked to my card."

Deictic Reference

"Cancel this account."

Implicit Reference

"Renew it."

The last case requires Context to resolve the referenced Entity.

⸻

34. Entity Resolution and Context

Entity resolution is heavily dependent on Context.

Reference
   +
Context
   +
Evidence
   ↓
Candidate Entities
   ↓
Entity Resolution

For example:

User:
"Renew my card."
Context:
Current conversation concerns card ending 1234.
Resolved Entity:
card_1234

⸻

35. Entity Resolution and Constraints

Constraints may narrow the candidate Entity set.

Intent:
"Renew my active card."
Candidates:
card_1234 → expired
card_5678 → active
card_9012 → cancelled

Constraint:

status = active

Candidate set becomes:

card_5678

Constraints therefore participate in Entity resolution where applicable.

⸻

36. Entity Resolution and Authority

Authority may also constrain which Entities an Actor can access or act upon.

Actor:
Finance Manager
Authority:
May modify corporate accounts.
Entities:
personal_account
corporate_account

The personal account may therefore be excluded from actionable candidates.

Authority is not merely an Entity filter, however; it is evaluated independently.

⸻

37. Entity Resolution and Trust

Material Entity resolution should be established before Trust is granted to an Action targeting that Entity.

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

"Delete my account"

while the target account remains ambiguous.

⸻

38. Entity and Resource Boundary

An Entity becomes a Resource when it is relevant as an object of an Action.

For example:

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
   └── Actor in a procurement Intent

The same Entity may participate differently depending on context.

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

⸻

41. Entity and Relationship Model

The Noema ontology can therefore represent:

Entity
   │
   ├── has ───────► Attribute
   │
   ├── has ───────► State
   │
   ├── relates ───► Entity
   │
   └── participates in ───► Intent / Action / Outcome

This provides the basis for a domain graph without requiring Noema to mandate a graph database.

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

An Intent may traverse these relationships:

"Renew the card linked to my primary account."

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

⸻

43. Entity Canonicalization

Different references may identify the same Entity.

"my main account"
"primary account"
"the account ending 4421"
"account 123"

These may resolve to:

account_123

Canonicalization should preserve:

* original reference
* resolved Entity
* resolution evidence
* source
* timestamp

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

Noema should preserve the underlying source identifiers.

⸻

45. Entity Split

Conversely, one previously identified Entity may later be discovered to represent multiple real-world Entities.

For example:

CRM Customer C123

may incorrectly contain data for two individuals.

The ontology must permit Entity identity correction without silently rewriting historical records.

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

The Entity may remain the same despite attribute changes.

Therefore:

Entity Identity
        ≠
Current Attribute Values

⸻

47. Entity Versioning

Some Entities or representations may require versioning.

For example:

Document
   ├── Version 1
   ├── Version 2
   └── Version 3

Whether versions are separate Entities or States depends on the domain model.

Noema should not impose a universal interpretation.

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

⸻

49. Entity Security Boundary

Entity references may expose access-control boundaries.

For example:

Actor:
User A
Intent:
"Delete account 123."
Entity:
account_123

The existence of an Entity identifier does not establish that the Actor may access or modify it.

Entity resolution and authorization must therefore remain separate.

Entity Resolution
        ↓
Authorization

⸻

50. Entity and Privacy

Entity identity may involve sensitive information.

Noema should minimize unnecessary exposure of:

* identifiers
* personal attributes
* credentials
* financial information
* private relationships

The ontology defines semantic identity.

It does not require all Entity attributes to be exposed to every component.

⸻

51. Entity Model

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

This is an ontology-level model.

It is not a persistence schema.

⸻

52. Entity Resolution Model

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

⸻

53. Entity Lifecycle Model

Conceptually:

Referenced
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

⸻

54. Canonical Distinctions

Noema must preserve:

Entity       ≠ Concept
Entity       ≠ Intent
Entity       ≠ Action
Entity       ≠ State
Entity       ≠ Identifier
Entity       ≠ Actor
Entity       ≠ Resource

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

⸻

55. Core Invariants

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

Entity relationships must be semantically explicit.

Invariant 14

Noema must not infer ownership, membership, or authority merely from Entity identity.

Invariant 15

An Entity must be resolved before a material Action targeting that Entity is trusted for execution.

Invariant 16

The existence of an Entity does not imply that the current Actor is authorized to access or modify it.

Invariant 17

Probabilistic entity resolution may generate candidates but must not silently establish material identity where deterministic resolution is required.

Invariant 18

Historical Entity identity must remain auditable when entities are merged, split, or re-canonicalized.

⸻

56. Relationship to Other Ontology Documents

This document defines the general semantics of Entities.

Related documents:

01-ontology/
├── concepts.md
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
   ├── participates in Intent
   ├── is targeted by Action
   └── appears in Outcome

⸻

57. Canonical Summary

An Entity is a distinct, identifiable thing that can participate in, be referenced by, or be affected by an Intent, Action, or Outcome within a Noema domain.

The core model is:

Concept
   │
   │ defines
   ▼
Entity
   │
   ├── has ─────────► State
   ├── has ─────────► Attributes
   ├── relates to ──► Entity
   │
   ├── may act as ──► Actor
   └── may serve as ► Resource

And the most important operational boundary is:

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
          ▼
 Authorization / Constraints
          │
          ▼
        Trust
          │
          ▼
        Action

Noema must know not only what an Actor wants to do, but which Entity that Intent is actually about before it crosses the Trust boundary.