Yes. relationships.md should be the relational grammar of the ontology. The individual files define what each concept means; this file defines how those concepts are allowed to relate to one another.

Relationships

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/relationships.md

⸻

1. Purpose

The Noema Ontology defines not only canonical concepts but also the relationships between those concepts.

A concept without defined relationships is insufficient for representing executable intent.

For example:

Intent

has limited meaning by itself.

Noema needs to know:

Who expressed it?
What does it concern?
Under what Context?
Under what Constraints?
Which Policies apply?
Who has Authority?
Which Capabilities can fulfill it?
Which Actions are required?
What Outcomes resulted?
Was the Intent satisfied?

relationships.md defines these semantic connections.

⸻

2. Fundamental Principle

Relationships are semantic facts, not implementation details.

The relationship:

Actor → expresses → Intent

is an ontology fact.

How that relationship is stored in:

* PostgreSQL
* a graph database
* JSON
* protobuf
* an event stream

is an implementation concern.

The ontology must remain storage-independent.

⸻

3. Relationship Model

The foundational Noema relationship graph is:

Actor
  │
  └── expresses ───────────► Intent
                               │
                               ├── concerns ───────► Entity
                               │
                               ├── occurs within ──► Context
                               │
                               ├── constrained by ─► Constraint
                               │
                               ├── governed by ────► Policy
                               │
                               └── fulfilled by ───► Action
                                                        │
                                                        ├── enabled by ──► Capability
                                                        │
                                                        └── produces ────► Outcome
                                                                              │
                                                                              ├── supported by ──► Evidence
                                                                              │
                                                                              └── evaluated as ──► Satisfaction

Authority and Trust govern the transition into execution:

Actor
  │
  └── holds ───────────────► Authority
                               │
Intent + Policy + Context + Constraint + Evidence
                               │
                               ▼
                             Trust
                               │
                               └── permits ───────► Action

⸻

4. Relationship Anatomy

A canonical relationship can be represented conceptually as:

Subject
   │
   │ relationship
   ▼
Object

Example:

Actor
  │
  │ expresses
  ▼
Intent

A relationship may additionally have attributes:

Relationship
├── subject
├── predicate
├── object
├── provenance
├── temporal validity
├── confidence
└── metadata

Not every relationship requires all attributes.

⸻

5. Relationship Vocabulary

Noema should prefer a controlled vocabulary of canonical relationship predicates.

Foundational predicates include:

expresses
targets
concerns
references
occurs_within
constrained_by
governed_by
requires
enabled_by
authorized_by
evaluated_by
permits
denies
fulfills
decomposes_into
derives_from
delegates_to
belongs_to
has_capability
produces
results_in
supported_by
verified_by
satisfies
depends_on
precedes
follows
supersedes
correlates_with
affects
changes
observed_by

This vocabulary should grow deliberately.

⸻

6. Actor → Intent

Relationship

Actor ──expresses──► Intent

Meaning:

The Actor is the source of the Intent.

Example:

Customer
  └── expresses ──► RenewCard

This establishes Intent ownership/origin.

⸻

7. Actor → Authority

Relationship

Actor ──holds──► Authority

Meaning:

The Actor possesses a defined scope of authority.

Example:

FinanceManager
  └── holds ──► RefundApprovalAuthority

Authority must specify its scope.

⸻

8. Actor → Capability

Relationship

Actor ──has_capability──► Capability

This means the Actor or system possesses an ability.

However:

Capability ≠ Authority

Possessing a Capability does not necessarily authorize its use.

⸻

9. Intent → Entity

Relationship

Intent ──concerns──► Entity

Example:

Intent:
Renew Card
  └── concerns ──► Card#1234

An Intent may concern one or multiple Entities.

⸻

10. Intent → Context

Relationship

Intent ──occurs_within──► Context

Context provides information necessary to interpret or evaluate the Intent.

Example:

Intent:
Cancel subscription
Context:
Current authenticated session

⸻

11. Intent → Constraint

Relationship

Intent ──constrained_by──► Constraint

Example:

Intent:
Transfer funds
Constraint:
Maximum amount = $5,000

The Constraint limits how the Intent may be fulfilled.

⸻

12. Intent → Policy

Relationship

Intent ──governed_by──► Policy

This indicates that one or more Policies are applicable to the Intent.

Example:

Intent:
Delete customer
  └── governed_by ──► LegalHoldDeletionPolicy

⸻

13. Intent → Action

Relationship

Intent ──fulfilled_by──► Action

An Intent may map to:

* one Action
* multiple Actions
* alternative Actions
* conditional Actions

Example:

Intent:
Onboard Employee
  ├── fulfilled_by ──► CreateEmployee
  ├── fulfilled_by ──► CreateEmail
  └── fulfilled_by ──► AssignPermissions

⸻

14. Intent → Intent

An Intent may have hierarchical relationships with other Intents.

Decomposition

Intent ──decomposes_into──► Intent

Example:

OnboardEmployee
   ├──► CreateEmployee
   ├──► ProvisionEmail
   └──► AssignPermissions

The child Intents remain semantically distinct from the parent Intent.

⸻

15. Derived Intent

Relationship

Intent ──derives_from──► Intent

Example:

Principal Intent:
Keep inventory above 100 units.
Derived Intent:
Order 50 units.
Derived Intent
  └── derives_from ──► Principal Intent

This relationship is essential for agentic planning.

⸻

16. Intent → Intent Dependencies

Relationship

Intent ──depends_on──► Intent

Example:

ActivateAccount
  └── depends_on ──► CreateAccount

This expresses semantic dependency rather than implementation order.

⸻

17. Action → Capability

Relationship

Action ──enabled_by──► Capability

Example:

RenewCard
  └── enabled_by ──► card.renew

The Capability describes what can be done.

The Action describes what is being done.

⸻

18. Action → Entity

Relationship

Action ──affects──► Entity

Example:

DeactivateAccount
  └── affects ──► Account#123

An Action may affect multiple Entities.

⸻

19. Action → Constraint

Relationship

Action ──constrained_by──► Constraint

Example:

TransferFunds
  └── constrained_by ──► MaxTransferAmount

Constraints may apply at either Intent or Action level.

⸻

20. Action → Policy

Relationship

Action ──governed_by──► Policy

Example:

DeleteCustomer
  └── governed_by ──► LegalHoldPolicy

A Policy may therefore apply at multiple stages.

⸻

21. Action → Authority

Relationship

Action ──authorized_by──► Authority

This indicates the Authority under which the Action may be performed.

Example:

ApproveExpense
  └── authorized_by ──► ManagerApprovalAuthority

⸻

22. Trust → Action

Relationship

Trust ──permits──► Action

This relationship represents the critical execution boundary.

Example:

Trust Decision:
PERMIT
  └── permits ──► TransferFunds

A denied Trust Decision must not produce an executable Action.

⸻

23. Trust → Policy

Relationship

Trust ──evaluates──► Policy

More precisely, Trust evaluation consumes applicable Policies.

The relationship should preserve which Policies contributed to the decision.

⸻

24. Policy → Constraint

Relationship

Policy ──defines──► Constraint

Example:

ExpensePolicy
  └── defines ──► MaximumExpenseConstraint

This relationship makes explicit that Policies can produce concrete runtime conditions.

⸻

25. Policy → Policy

Policies may relate to other Policies.

Refines

Policy ──refines──► Policy

Supersedes

Policy ──supersedes──► Policy

Depends On

Policy ──depends_on──► Policy

These relationships are particularly important for Policy versioning and governance.

⸻

26. Policy → Authority

Relationship

Policy ──requires──► Authority

Example:

HighValueRefundPolicy
  └── requires ──► ManagerApprovalAuthority

⸻

27. Capability → Action

The inverse relationship of Action → Capability is:

Capability ──enables──► Action

Example:

card.renew
  └── enables ──► RenewCard

⸻

28. Capability → Capability

Capabilities may compose.

Capability ──requires──► Capability

Example:

international.transfer
  └── requires ──► beneficiary.verify

This allows capability dependencies to be modeled explicitly.

⸻

29. Execution → Action

Relationship

Execution ──executes──► Action

An Execution represents an attempt to perform an Action.

Multiple Executions may correspond to one Action.

Action
 ├── Execution 1
 ├── Execution 2
 └── Execution 3

This is important for retries.

⸻

30. Execution → Outcome

Relationship

Execution ──produces──► Outcome

An Execution may produce:

* one Outcome
* multiple Outcomes
* an intermediate Outcome
* no immediately observable Outcome

⸻

31. Outcome → Intent

Relationship

Outcome ──evaluated_against──► Intent

This establishes the semantic relationship required to determine whether the original Intent was fulfilled.

⸻

32. Outcome → Evidence

Relationship

Outcome ──supported_by──► Evidence

Example:

PaymentCompleted
  └── supported_by ──► PaymentProviderReceipt

⸻

33. Evidence → Outcome

The inverse relationship:

Evidence ──supports──► Outcome

Evidence does not necessarily constitute an Outcome.

It supports a claim about an Outcome.

⸻

34. Evidence → Entity

Evidence may concern an Entity.

Evidence ──concerns──► Entity

Example:

IdentityVerificationRecord
  └── concerns ──► Customer#123

⸻

35. Outcome → Entity

Relationship

Outcome ──affects──► Entity

Example:

AccountActivated
  └── affects ──► Account#123

⸻

36. Outcome → State

An Outcome may produce or correspond to a State change.

Outcome ──changes──► State

Example:

CardRenewed
  └── changes ──► Card.status

The Outcome and State remain distinct concepts.

⸻

37. Outcome → Outcome

Outcomes may have temporal or causal relationships.

Precedence

Outcome ──precedes──► Outcome

Dependency

Outcome ──depends_on──► Outcome

Supersession

Outcome ──supersedes──► Outcome

Example:

PaymentCompleted
      ↓
PaymentReversed
PaymentReversed
  └── supersedes ──► current interpretation of PaymentCompleted

It does not erase the historical Outcome.

⸻

38. Entity → Entity

Entities may relate to other Entities.

Examples:

Customer ──owns──► Account
Account ──contains──► Transaction
Employee ──belongs_to──► Organization
Card ──belongs_to──► Account

These relationships form the domain graph against which Intent is interpreted.

⸻

39. Concept → Entity

A concrete Entity may instantiate a Concept.

Entity ──instance_of──► Concept

Example:

Card#1234
  └── instance_of ──► PaymentCard

⸻

40. Concept → Concept

Concepts may form semantic hierarchies.

Concept ──subtype_of──► Concept

Example:

CreditCard
  └── subtype_of ──► PaymentCard

This provides the ontology’s conceptual taxonomy.

⸻

41. Context → Entity

Context may reference Entities relevant to an Intent.

Context ──references──► Entity

Example:

CurrentSession
  └── references ──► Customer#123

⸻

42. Context → Context

Context may contain nested or derived Context.

Context ──contains──► Context

Example:

RequestContext
  └── contains ──► AuthenticationContext

⸻

43. Constraint → Entity

A Constraint may apply to an Entity.

Constraint ──applies_to──► Entity

Example:

TransferLimit
  └── applies_to ──► Account#123

⸻

44. Constraint → Action

Constraint ──limits──► Action

Example:

DailyTransferLimit
  └── limits ──► TransferFunds

⸻

45. Constraint → Intent

Constraint ──limits──► Intent

This is useful where a constraint is directly associated with the Actor’s request.

Example:

Intent:
Book flight
Constraint:
Direct flights only

⸻

46. Authority → Actor

The inverse of Actor → Authority:

Authority ──grants_to──► Actor

Example:

RefundApprovalAuthority
  └── grants_to ──► FinanceManager

⸻

47. Authority → Capability

Authority may be scoped to a Capability.

Authority ──covers──► Capability

Example:

RefundAuthority
  └── covers ──► refund.payment

⸻

48. Authority → Entity

Authority may be scoped to particular Entities or resources.

Authority ──scoped_to──► Entity

Example:

AccountManagerAuthority
  └── scoped_to ──► Account#123

⸻

49. Delegation

Authority may be delegated.

Actor ──delegates──► Authority ──to──► Actor

Example:

Director
   │
   └── delegates ──► ApprovalAuthority
                         │
                         └── to ──► Manager

Delegation must preserve:

* delegator
* delegate
* scope
* duration
* conditions

⸻

50. Trust → Evidence

Trust decisions depend on Evidence.

Trust ──based_on──► Evidence

Example:

Trust Decision:
PERMIT
  └── based_on ──► VerifiedIdentityEvidence

⸻

51. Trust → Context

Trust ──evaluates──► Context

The Trust Engine uses Context to determine whether applicable rules are satisfied.

⸻

52. Trust → Constraint

Trust ──evaluates──► Constraint

Example:

Constraint:
amount <= 5000
Trust:
Constraint satisfied

⸻

53. Trust → Authority

Trust ──evaluates──► Authority

Example:

Actor:
SupportAgent
Authority:
Refund ≤ $1,000
Intent:
Refund $5,000
Trust:
DENY

⸻

54. Relationship Cardinality

Relationships should have explicit cardinality where semantically meaningful.

Examples:

Actor
  └── expresses ──► Intent
Intent
  └── may concern ──► one or many Entities
Intent
  └── may be fulfilled by ──► one or many Actions
Action
  └── may have ──► one or many Executions
Execution
  └── may produce ──► zero, one, or many Outcomes

Cardinality should not be imposed merely for database convenience.

⸻

55. Relationship Direction

Canonical relationships should have an explicit direction.

For example:

Actor ──expresses──► Intent

is preferable to an ambiguous:

Actor ↔ Intent

The inverse relationship may be useful:

Intent ──expressed_by──► Actor

but it should have a clearly defined semantic meaning.

⸻

56. Relationship Inverses

Where useful, relationships may define canonical inverses.

Relationship	Inverse
expresses	expressed_by
targets	targeted_by
concerns	concerned_by
governed_by	governs
constrained_by	constrains
enabled_by	enables
authorized_by	authorizes
produces	produced_by
supported_by	supports
affects	affected_by
delegates_to	delegated_from
derives_from	source_of
depends_on	dependency_of
supersedes	superseded_by

Not every inverse needs to be stored physically.

⸻

57. Relationship Attributes

Some relationships require metadata.

Example:

Actor
  └── expresses ──► Intent
        │
        ├── expressed_at
        ├── channel
        └── provenance

Another:

Policy
  └── governs ──► Action
        │
        ├── effective_from
        ├── effective_until
        └── policy_version

Relationship metadata belongs to the relationship rather than either endpoint.

⸻

58. Temporal Relationships

Relationships may be time-bound.

Example:

Actor
  └── holds ──► Authority
        │
        ├── valid_from
        └── valid_until

This is critical for:

* delegation
* authorization
* policy applicability
* entity ownership
* employment relationships
* temporary permissions

⸻

59. Conditional Relationships

Some relationships only exist under conditions.

Example:

Actor
  └── authorized_for ──► Action
        │
        └── condition:
             amount <= $10,000

The condition should be explicit rather than embedded in application code.

⸻

60. Provenance of Relationships

Relationships themselves may require provenance.

Example:

Actor ──holds──► Authority
Provenance:
HR system
Observed:
2026-08-23

This is particularly important for consequential relationships such as:

* Authority
* Ownership
* Identity
* Policy
* Approval
* Delegation

⸻

61. Relationship Confidence

Some relationships may initially be inferred.

Example:

Actor
  └── likely_belongs_to ──► Organization

Noema should distinguish:

Authoritative Relationship

from:

Inferred Relationship

Inferred relationships should not automatically support consequential Trust decisions.

⸻

62. Relationship Evidence

Where a relationship matters to Trust, it should be backed by appropriate Evidence.

Example:

Actor ──holds──► ApprovalAuthority
Evidence:
HR authorization record

The graph should preserve:

Relationship
   ↓
Evidence
   ↓
Provenance

⸻

63. Relationship Conflicts

Noema may encounter conflicting relationships.

Example:

System A:
Alice → Manager
System B:
Alice → Employee

The ontology should represent the conflict rather than silently selecting one.

Resolution requires:

* source authority
* timestamp
* provenance
* Policy
* reconciliation rules

⸻

64. Relationship Lifecycle

Relationships may be:

PROPOSED
ACTIVE
SUSPENDED
EXPIRED
REVOKED
SUPERSEDED

The appropriate lifecycle depends on the relationship type.

For example, an Authority may be REVOKED, while a historical expresses relationship remains permanently valid as a fact about the past.

⸻

65. Relationship Immutability

Historical relationships should not be silently rewritten.

Example:

2025:
Alice ──holds──► ManagerAuthority
2026:
Authority revoked

The historical relationship remains:

Alice held ManagerAuthority during 2025.

The current relationship becomes inactive.

⸻

66. Relationship Semantics vs Graph Implementation

The ontology does not require Noema to use a graph database.

The model may be implemented using:

Relational tables
Document storage
Graph database
Event streams
Typed objects
Hybrid storage

A graph representation is useful because the domain itself is highly relational, but storage technology must not define the ontology.

⸻

67. Core Relationship Graph

The minimum viable relationship graph is:

Actor
  │
  └──expresses──► Intent
                     │
                     ├──concerns──► Entity
                     │
                     ├──occurs_within──► Context
                     │
                     ├──constrained_by──► Constraint
                     │
                     ├──governed_by──► Policy
                     │
                     └──fulfilled_by──► Action
                                           │
                                           ├──enabled_by──► Capability
                                           │
                                           └──executed_as──► Execution
                                                              │
                                                              └──produces──► Outcome
                                                                                 │
                                                                                 ├──supported_by──► Evidence
                                                                                 │
                                                                                 └──evaluated_against──► Intent

Governance:

Actor
  └──holds──► Authority
Authority
  └──covers──► Capability
Policy
  └──defines──► Constraint
Trust
  ├──evaluates──► Policy
  ├──evaluates──► Authority
  ├──evaluates──► Constraint
  ├──based_on──► Evidence
  └──permits──► Action

⸻

68. Relationship Categories

For consistency, relationships can be grouped into semantic categories.

Expression

expresses
expressed_by

Reference

concerns
references
targets

Governance

governed_by
constrained_by
authorized_by

Capability

enabled_by
enables
requires

Execution

fulfilled_by
executes
produces

Evidence

supported_by
supports
verified_by

Causality

derives_from
depends_on
produces
results_in

Temporal

precedes
follows
supersedes

Delegation

delegates_to
delegated_from

Taxonomy

instance_of
subtype_of
belongs_to

⸻

69. Relationship Naming Rules

Canonical relationship predicates should:

1. Use clear semantic verbs.
2. Describe the relationship from Subject → Object.
3. Avoid implementation terminology.
4. Avoid ambiguous verbs such as has where a precise relationship exists.
5. Prefer domain meaning over database terminology.
6. Define inverse relationships where useful.
7. Define cardinality where semantically necessary.
8. Define temporal semantics where applicable.

Prefer:

Actor ──expresses──► Intent

over:

Actor ──has──► Intent

Prefer:

Action ──enabled_by──► Capability

over:

Action ──uses──► Capability

because uses is semantically ambiguous.

⸻

70. Relationship Anti-Patterns

Generic has

Avoid:

Actor has Intent
Actor has Authority
Action has Capability

These relationships have different meanings.

Prefer:

Actor expresses Intent
Actor holds Authority
Action enabled_by Capability

⸻

Implicit Relationships

Do not rely on naming conventions to imply relationships.

Bad:

action.customer_refund

and assume it is related to:

intent.refund_customer

The relationship should be explicit.

⸻

Prompt-Only Relationships

Do not encode critical relationships only inside prompts.

For example:

“The user is the account owner, so let them refund it.”

The ownership relationship should exist as structured data:

Actor ──owns──► Account

⸻

71. Relationship Integrity

Noema should enforce semantic integrity.

For example:

Action ──enabled_by──► Capability

requires the referenced Capability to exist or be resolvable.

Likewise:

Outcome ──evaluated_against──► Intent

should identify the Intent whose satisfaction is being evaluated.

⸻

72. Relationship Validation

Before consequential execution, Noema should validate required relationships.

Example:

Intent
  ├── expressed_by Actor ✓
  ├── concerns Entity ✓
  ├── governed_by Policy ✓
  ├── constrained_by Constraint ✓
  ├── fulfilled_by Action ✓
  └── authorized_by Authority ✗

Result:

Trust:
DENY / REQUIRE AUTHORITY

⸻

73. Relationship Graph as Execution Context

The resolved subgraph surrounding an Intent can become the execution context for Trust.

                 Actor
                   │
                   ▼
                Intent
             /    |    \
            /     |     \
       Entity  Policy  Constraint
                  │
                  ▼
              Authority
                  │
                  ▼
                Trust
                  │
                  ▼
                Action
                  │
                  ▼
               Outcome

Noema does not need the entire enterprise graph for every decision.

It needs the relevant canonical subgraph.

⸻

74. Minimal Intent Subgraph

A minimally executable Intent should be resolvable into something resembling:

Actor
  ↓
Intent
  ↓
Target Entity
  ↓
Relevant Context
  ↓
Applicable Constraints
  ↓
Applicable Policies
  ↓
Required Authority
  ↓
Candidate Action
  ↓
Required Capability

Only after this graph is sufficiently resolved should the Trust boundary be crossed.

⸻

75. Outcome Subgraph

After execution:

Intent
   ↓
Action
   ↓
Execution
   ↓
Outcome
   ├── affects ──► Entity
   ├── supported_by ──► Evidence
   └── evaluated_against ──► Intent

This allows Noema to close the semantic loop.

⸻

76. Canonical Relationship Invariants

The following relationships are foundational:

1. Actor expresses Intent.
2. Intent concerns one or more Entities where applicable.
3. Intent occurs within Context.
4. Intent may be constrained by Constraints.
5. Intent may be governed by Policies.
6. Intent may be fulfilled by one or more Actions.
7. Action is enabled by one or more Capabilities.
8. Action may affect one or more Entities.
9. Action may be governed by Policies.
10. Action may require Authority.
11. Trust evaluates the conditions surrounding an Action.
12. Trust may permit or deny an Action.
13. Execution executes an Action.
14. Execution may produce one or more Outcomes.
15. Outcome affects or describes changes involving Entities where applicable.
16. Outcome may be supported by Evidence.
17. Outcome is evaluated against the originating Intent.
18. Intent may derive from or decompose into other Intents.
19. Authority may be delegated between Actors.
20. Policies may define or produce Constraints.
21. Capabilities may require other Capabilities.
22. Entities may instantiate Concepts.
23. Concepts may form semantic hierarchies.
24. Relationships may have provenance and temporal validity.
25. Consequential relationships must be backed by sufficient Evidence.
26. Unknown relationships must not be silently treated as established facts.
27. Historical relationships must not be silently overwritten.

⸻

77. Canonical Relationship Chain

The primary Noema relationship chain is:

Actor
  │
  │ expresses
  ▼
Intent
  │
  │ concerns
  ▼
Entity
Intent
  │
  ├── occurs_within ──► Context
  ├── constrained_by ─► Constraint
  ├── governed_by ────► Policy
  └── fulfilled_by ───► Action
                            │
                            ├── enabled_by ──► Capability
                            ├── affects ─────► Entity
                            └── executes_as ─► Execution
                                                  │
                                                  └── produces ──► Outcome
                                                                     │
                                                                     ├── supported_by ──► Evidence
                                                                     └── evaluated_against ──► Intent

Governance:

Actor
  │
  └── holds ──► Authority
                  │
                  └── covers ──► Capability
Policy
  │
  └── defines ──► Constraint
Intent + Policy + Constraint + Authority + Context + Evidence
                           │
                           ▼
                         Trust
                           │
                           └── permits ──► Action

⸻

78. Canonical Principle

Noema’s ontology is not merely a collection of nouns. It is a typed semantic graph in which relationships establish who expressed an Intent, what it concerns, what governs it, what constrains it, what authority supports it, what capability can fulfill it, what Action was executed, what Outcome resulted, and whether that Outcome satisfied the original Intent.

The most important invariant is therefore:

Meaning
   ↓
Relationships
   ↓
Resolution
   ↓
Trust
   ↓
Execution
   ↓
Outcome

The relationship graph is the connective tissue of Noema’s canonical model.