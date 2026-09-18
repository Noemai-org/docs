# Relationships
Status: Foundational Draft
Version: 0.2
Domain: Ontology
Canonical Path: ontology/relationships.md
⸻
## 1. Definition
A Relationship is a canonical semantic connection between two or more ontology concepts, entities, or semantic objects.
A Relationship expresses how one subject relates to another object within the Noema model.
It answers:
> How are these concepts or objects semantically connected?
Examples:
Actor → expresses → Intent
Intent → concerns → Entity
Intent → governed_by → Policy
Action → enabled_by → Capability
Execution → produces → Outcome
Outcome → supported_by → Evidence
Relationships are part of Noema's semantic model.
They are not database joins, implementation references, or merely inferred associations.
⸻
## 2. Purpose
Noema requires explicit relationships because canonical concepts do not have sufficient meaning in isolation.
For example:
Intent
does not establish:
- who expressed it;
- what it concerns;
- under what Context it exists;
- what Constraints apply;
- which Policies govern it;
- what Authority is relevant;
- which Capability can fulfill it;
- which Action fulfills it;
- what Outcome resulted;
- whether the Outcome satisfies the Intent.
Relationships establish these semantic connections.
Therefore:
Concepts define the things Noema understands.
Relationships define how those things are connected.
⸻
## 3. Fundamental Principle
Relationships are semantic facts.
For example:
Actor
  │
  └── expresses ──► Intent
is an ontological statement.
Its implementation may use:
- relational tables;
- graph storage;
- documents;
- typed objects;
- event streams;
- hybrid storage.
The implementation must not redefine the semantics of the Relationship.
Noema's ontology therefore remains storage-independent.
⸻
## 4. Canonical Relationship Form
A canonical Relationship has the conceptual form:
Subject
   │
   │ Predicate
   ▼
Object
Example:
Actor
   │
   │ expresses
   ▼
Intent
Conceptually:
Relationship
├── subject
├── predicate
└── object
A Relationship may additionally carry attributes when required:
Relationship
├── subject
├── predicate
├── object
├── provenance
├── temporal_validity
├── conditions
├── confidence
└── metadata
These attributes describe the Relationship itself.
They should not be confused with attributes belonging to either endpoint.
⸻
## 5. Relationship Direction
Canonical Relationships have an explicit semantic direction.
Example:
Actor → expresses → Intent
is distinct from:
Intent → expressed_by → Actor
The latter may be defined as an inverse relationship.
Noema should avoid ambiguous bidirectional relationships such as:
Actor ↔ Intent
unless the underlying semantics are explicitly defined.
The direction of a Relationship must be interpreted from its Subject toward its Object.
⸻
## 6. Canonical Relationship Vocabulary
Noema should use a controlled vocabulary of canonical Relationship predicates.
Foundational predicates include:
### Expression
expresses
expressed_by
### Reference
concerns
concerned_by
references
targets
### Context
occurs_within
contains
### Constraint
constrained_by
constrains
applies_to
limits
### Governance
governed_by
governs
authorized_by
authorizes
### Capability
enabled_by
enables
requires
### Fulfillment and Derivation
fulfilled_by
fulfills
decomposes_into
derives_from
source_of
### Execution
executes
executed_as
produces
produced_by
results_in
### Evidence
supported_by
supports
verified_by
### Authority and Delegation
holds
grants_to
covers
scoped_to
delegates_to
delegated_from
### Causality and Dependency
depends_on
affects
changes
### Temporal Relationships
precedes
follows
supersedes
superseded_by
### Taxonomy
instance_of
subtype_of
belongs_to
### Evaluation
evaluated_by
evaluates
evaluated_against
satisfies
This vocabulary is foundational and may evolve through explicit ontology changes.
New predicates should not be introduced merely because an implementation requires a convenient relationship name.
⸻
## 7. Actor → Intent
Relationship:
Actor → expresses → Intent
Meaning:
The Actor is the source of an Intent.
Example:
Customer
  └── expresses ──► RenewCard
This relationship establishes the origin of the Intent.
The Relationship itself does not determine whether the Intent is authorized, trusted, or executable.
Those questions belong to Authority, Policy, Constraint, Evidence, and Trust.
⸻
## 8. Actor → Authority
Relationship:
Actor → holds → Authority
Meaning:
The Actor is associated with an Authority within a defined scope and, where applicable, temporal validity.
Example:
FinanceManager
  └── holds ──► RefundApprovalAuthority
The existence of this Relationship does not by itself establish that a particular Action is authorized.
The scope and conditions of the Authority must be evaluated.
⸻
## 9. Actor → Capability
Relationship:
Actor → has_capability → Capability
Meaning:
The Actor or relevant system possesses a Capability.
Capability describes ability.
Authority describes permitted scope of action.
Therefore:
Capability ≠ Authority
An Actor may possess a Capability without being authorized to exercise it in a particular situation.
⸻
## 10. Intent → Entity
Relationship:
Intent → concerns → Entity
Meaning:
The Intent relates to one or more Entities that form its semantic subject or target.
Example:
Intent:
Renew Card
Intent
  └── concerns ──► Card#1234
An Intent may concern multiple Entities.
The exact cardinality depends on the Intent.
⸻
## 11. Intent → Context
Relationship:
Intent → occurs_within → Context
Meaning:
The Intent exists within a Context relevant to its interpretation or evaluation.
Example:
Intent:
Cancel Subscription
Context:
Authenticated Session
Context may contain information about:
- Actor;
- Entity state;
- time;
- location;
- environment;
- authentication;
- transaction state;
- other relevant facts.
Context supplies facts.
It does not itself constitute Policy or Trust.
⸻
## 12. Intent → Constraint
Relationship:
Intent → constrained_by → Constraint
Meaning:
A Constraint limits how an Intent may be fulfilled.
Example:
Intent:
Transfer Funds
Constraint:
Maximum transfer amount = $5,000
A Constraint may be associated directly with an Intent or derived from another governing concept.
⸻
## 13. Intent → Policy
Relationship:
Intent → governed_by → Policy
Meaning:
The Intent is subject to one or more applicable Policies.
Example:
Intent:
Delete Customer
Intent
  └── governed_by ──► LegalHoldDeletionPolicy
The Relationship establishes Policy applicability.
It does not itself constitute the resulting Policy Decision or Trust Decision.
⸻
## 14. Intent → Action
Relationship:
Intent → fulfilled_by → Action
Meaning:
An Action represents an operation intended to fulfill an Intent.
An Intent may be fulfilled by:
- one Action;
- multiple Actions;
- alternative Actions;
- conditional Actions.
Example:
Intent:
Onboard Employee
Intent
  ├── fulfilled_by ──► CreateEmployee
  ├── fulfilled_by ──► CreateEmail
  └── fulfilled_by ──► AssignPermissions
The Relationship does not guarantee that the Action succeeds or that the Intent is ultimately satisfied.
⸻
## 15. Intent → Intent Decomposition
Relationship:
Intent → decomposes_into → Intent
Meaning:
A higher-level Intent is represented by one or more subordinate Intents.
Example:
OnboardEmployee
   ├── decomposes_into ──► CreateEmployee
   ├── decomposes_into ──► ProvisionEmail
   └── decomposes_into ──► AssignPermissions
Child Intents remain semantically distinct from their parent Intent.
⸻
## 16. Intent Derivation
Relationship:
Intent → derives_from → Intent
Meaning:
One Intent was derived from another Intent.
Example:
Principal Intent:
Keep inventory above 100 units.
Derived Intent:
Order 50 units.
DerivedIntent
  └── derives_from ──► PrincipalIntent
This Relationship preserves semantic lineage.
It does not by itself establish that the derived Intent is correct, authorized, or executable.
⸻
## 17. Intent Dependency
Relationship:
Intent → depends_on → Intent
Meaning:
The fulfillment or resolution of one Intent semantically depends upon another Intent.
Example:
ActivateAccount
  └── depends_on ──► CreateAccount
A dependency is not necessarily an implementation sequence.
The distinction between semantic dependency and execution ordering must be preserved.
⸻
## 18. Action → Capability
Relationship:
Action → enabled_by → Capability
Meaning:
A Capability provides the ability required to perform an Action.
Example:
RenewCard
  └── enabled_by ──► card.renew
The Capability describes what can be done.
The Action describes the specific operation being performed.
Therefore:
Capability ≠ Action
⸻
## 19. Action → Entity
Relationship:
Action → affects → Entity
Meaning:
The Action operates upon or changes one or more Entities.
Example:
DeactivateAccount
  └── affects ──► Account#123
An Action may affect multiple Entities.
This Relationship does not by itself describe the resulting state.
⸻
## 20. Action → Constraint
Relationship:
Action → constrained_by → Constraint
Meaning:
A Constraint limits the execution or valid parameters of an Action.
Example:
TransferFunds
  └── constrained_by ──► MaxTransferAmount
Constraints may therefore apply at both Intent and Action levels.
⸻
## 21. Action → Policy
Relationship:
Action → governed_by → Policy
Meaning:
A Policy applies to the Action.
Example:
DeleteCustomer
  └── governed_by ──► LegalHoldPolicy
A Policy may therefore be relevant at more than one stage of the lifecycle.
Applicability and evaluation remain distinct from the Relationship itself.
⸻
## 22. Action → Authority
Relationship:
Action → authorized_by → Authority
Meaning:
The Action is associated with the Authority under which it may be performed.
Example:
ApproveExpense
  └── authorized_by ──► ManagerApprovalAuthority
This Relationship does not by itself establish that all conditions of the Authority are satisfied.
⸻
## 23. Trust → Action
Relationship:
Trust → permits → Action
Meaning:
A Trust Decision permits an Action to cross the execution boundary.
Example:
Trust Decision:
PERMIT
Trust
  └── permits ──► TransferFunds
A Trust Decision that does not permit the Action must not be represented as permitting execution.
The exact Trust state vocabulary belongs to the Trust specification.
⸻
## 24. Trust → Policy
Relationship:
Trust → evaluates → Policy
Meaning:
A Trust evaluation incorporates applicable Policy information.
The Relationship should preserve which Policy or Policy versions contributed to the evaluation where such provenance is required.
Trust does not create or redefine the Policy.
⸻
## 25. Trust → Authority
Relationship:
Trust → evaluates → Authority
Meaning:
Authority relevant to the proposed Action participates in Trust evaluation.
Example:
Actor:
SupportAgent
Authority:
Refund ≤ $1,000
Intent:
Refund $5,000
Trust evaluates whether the applicable Authority supports the proposed operation.
⸻
## 26. Trust → Constraint
Relationship:
Trust → evaluates → Constraint
Meaning:
Trust evaluation considers Constraints applicable to the Intent or Action.
Example:
Constraint:
amount ≤ 5,000
Trust evaluates whether the Constraint is satisfied by the available facts.
⸻
## 27. Trust → Context
Relationship:
Trust → evaluates → Context
Meaning:
Context supplies facts relevant to Trust evaluation.
Examples include:
- Actor context;
- Entity state;
- authentication state;
- time;
- environment;
- location;
- transaction state.
Trust evaluates the relevant Context; it does not become the Context.
⸻
## 28. Trust → Evidence
Relationship:
Trust → based_on → Evidence
Meaning:
Evidence provides support for facts used in a Trust evaluation.
Example:
Trust Decision:
PERMIT
Evidence:
VerifiedIdentityEvidence
The Relationship should preserve which Evidence materially contributed to the decision.
⸻
## 29. Policy → Constraint
Relationship:
Policy → defines → Constraint
Meaning:
A Policy may establish a concrete condition applicable to an Intent or Action.
Example:
ExpensePolicy
  └── defines ──► MaximumExpenseConstraint
Conceptually:
Policy
   ↓
Constraint
   ↓
Evaluation
Not every Constraint originates from a Policy.
Constraints may also originate from:
- Intent;
- Actor preference;
- Capability;
- Resource limitations;
- Context;
- technical requirements.
⸻
## 30. Policy → Policy
Policies may have semantic relationships with other Policies.
Foundational relationships include:
Policy → refines → Policy
Policy → supersedes → Policy
Policy → depends_on → Policy
These relationships preserve policy lineage and governance structure.
Policy precedence and conflict resolution are not defined by the existence of these Relationships alone.
⸻
## 31. Policy → Authority
Relationship:
Policy → requires → Authority
Meaning:
A Policy may require an Authority or authority-bearing actor for an operation to proceed.
Example:
HighValueRefundPolicy
  └── requires ──► ManagerApprovalAuthority
The Policy establishes the requirement.
Authority determines whether the relevant Actor possesses the necessary authority.
⸻
## 32. Capability → Capability
Relationship:
Capability → requires → Capability
Meaning:
One Capability depends upon another Capability.
Example:
international.transfer
  └── requires ──► beneficiary.verify
This allows Capability dependencies to be represented explicitly.
⸻
## 33. Capability → Action
Relationship:
Capability → enables → Action
This is the inverse semantic relationship of:
Action → enabled_by → Capability
Example:
card.renew
  └── enables ──► RenewCard
The inverse need not be physically stored if it can be derived reliably.
⸻
## 34. Execution → Action
Relationship:
Execution → executes → Action
Meaning:
An Execution represents an attempt or instance of performing an Action.
An Action may therefore have multiple Executions.
Example:
Action
  ├── Execution 1
  ├── Execution 2
  └── Execution 3
This is important for retries, failures, and operational history.
An Execution is not itself an Action.
⸻
## 35. Execution → Outcome
Relationship:
Execution → produces → Outcome
Meaning:
An Execution may produce one or more observable Outcomes.
Possible cases include:
- one Outcome;
- multiple Outcomes;
- intermediate Outcomes;
- no immediately observable Outcome.
Execution success must not be inferred merely from the existence of an Execution.
⸻
## 36. Outcome → Intent
Relationship:
Outcome → evaluated_against → Intent
Meaning:
An Outcome is evaluated in relation to the Intent whose fulfillment it is intended to establish.
Example:
Intent:
Renew Card
Outcome:
CardRenewed
Outcome
  └── evaluated_against ──► Intent
This Relationship supports determination of Intent satisfaction.
The Outcome and Satisfaction remain distinct semantic concepts.
⸻
## 37. Outcome → Evidence
Relationship:
Outcome → supported_by → Evidence
Meaning:
Evidence provides support for claims represented by an Outcome.
Example:
PaymentCompleted
  └── supported_by ──► PaymentProviderReceipt
Evidence supports the interpretation of the Outcome.
Evidence is not automatically identical to the Outcome.
⸻
## 38. Evidence → Outcome
Relationship:
Evidence → supports → Outcome
This is the inverse of:
Outcome → supported_by → Evidence
Example:
PaymentProviderReceipt
  └── supports ──► PaymentCompleted
The Evidence may support an Outcome without itself being an Outcome.
⸻
## 39. Evidence → Entity
Relationship:
Evidence → concerns → Entity
Meaning:
Evidence may establish or support facts concerning an Entity.
Example:
IdentityVerificationRecord
  └── concerns ──► Customer#123
This Relationship allows Evidence to participate in Entity resolution and Trust evaluation.
⸻
## 40. Outcome → Entity
Relationship:
Outcome → affects → Entity
Meaning:
An Outcome may describe a change involving one or more Entities.
Example:
AccountActivated
  └── affects ──► Account#123
This Relationship does not collapse Outcome into Entity State.
⸻
## 41. Outcome → State
Relationship:
Outcome → changes → State
Meaning:
An Outcome may correspond to a State transition.
Example:
CardRenewed
  └── changes ──► Card.status
Outcome and State remain distinct.
Outcome represents what resulted from an Execution.
State represents the resulting condition of an Entity or system.
⸻
## 42. Outcome → Outcome
Outcomes may have temporal or semantic relationships.
Examples:
Outcome → precedes → Outcome
Outcome → depends_on → Outcome
Outcome → supersedes → Outcome
Example:
PaymentCompleted
      ↓
PaymentReversed
PaymentReversed
  └── supersedes ──► PaymentCompleted
Supersession does not erase the historical Outcome.
It establishes a new semantic interpretation or later state.
⸻
## 43. Entity → Entity
Entities may have domain relationships with other Entities.
Examples:
Customer
  └── owns ──► Account
Account
  └── contains ──► Transaction
Employee
  └── belongs_to ──► Organization
Card
  └── belongs_to ──► Account
These relationships form the domain graph against which Intents may be interpreted.
The precise Entity relationship vocabulary belongs to the relevant domain ontology.
⸻
## 44. Entity → Concept
Relationship:
Entity → instance_of → Concept
Meaning:
A concrete Entity is an instance of a canonical Concept.
Example:
Card#1234
  └── instance_of ──► PaymentCard
This establishes the semantic type of the Entity.
⸻
## 45. Concept → Concept
Relationship:
Concept → subtype_of → Concept
Meaning:
One Concept is semantically specialized from another Concept.
Example:
CreditCard
  └── subtype_of ──► PaymentCard
This provides the conceptual taxonomy of the ontology.
⸻
## 46. Context → Entity
Relationship:
Context → references → Entity
Meaning:
A Context may contain references to Entities relevant to interpretation or evaluation.
Example:
CurrentSession
  └── references ──► Customer#123
The existence of a reference does not by itself establish ownership, Authority, or permission.
⸻
## 47. Context → Context
Relationship:
Context → contains → Context
Meaning:
A Context may contain a more specific or subordinate Context.
Example:
RequestContext
  └── contains ──► AuthenticationContext
This permits structured contextual composition.
⸻
## 48. Constraint → Entity
Relationship:
Constraint → applies_to → Entity
Meaning:
A Constraint may directly limit an Entity or resource.
Example:
TransferLimit
  └── applies_to ──► Account#123
⸻
## 49. Constraint → Action
Relationship:
Constraint → limits → Action
Meaning:
The Constraint limits the permitted form or execution of an Action.
Example:
DailyTransferLimit
  └── limits ──► TransferFunds
This is the inverse semantic perspective of:
Action → constrained_by → Constraint
⸻
## 50. Constraint → Intent
Relationship:
Constraint → limits → Intent
Meaning:
The Constraint limits how an Intent may be fulfilled.
Example:
Intent:
Book Flight
Constraint:
Direct flights only
The Constraint does not become part of the Intent itself.
⸻
## 51. Authority → Actor
Relationship:
Authority → grants_to → Actor
This is the inverse perspective of:
Actor → holds → Authority
Example:
RefundApprovalAuthority
  └── grants_to ──► FinanceManager
The Authority remains scoped and conditional according to its definition.
⸻
## 52. Authority → Capability
Relationship:
Authority → covers → Capability
Meaning:
An Authority may authorize the exercise of a particular Capability.
Example:
RefundAuthority
  └── covers ──► refund.payment
Capability describes ability.
Authority establishes permitted exercise within its scope.
⸻
## 53. Authority → Entity
Relationship:
Authority → scoped_to → Entity
Meaning:
An Authority may apply only to specified Entities or resources.
Example:
AccountManagerAuthority
  └── scoped_to ──► Account#123
Scope may also be expressed through other ontology dimensions where applicable.
⸻
## 54. Authority Delegation
Authority may be delegated between Actors.
Conceptually:
Actor
   │
   └── delegates_to ──► Actor
            │
            └── receives scoped Authority
A delegation must preserve, where applicable:
- delegator;
- delegate;
- Authority;
- scope;
- conditions;
- effective period;
- provenance.
Delegation must not silently transfer unrestricted Authority.
⸻
## 55. Relationship Cardinality
Relationship cardinality should be defined where it is semantically meaningful.
Examples:
Actor
  └── expresses ──► Intent
Intent
  └── concerns ──► one or more Entities where applicable
Intent
  └── fulfilled_by ──► one or more Actions where applicable
Action
  └── may have ──► one or more Executions
Execution
  └── produces ──► zero, one, or multiple Outcomes
Cardinality must reflect domain semantics rather than database convenience.
⸻
## 56. Relationship Inverses
Where an inverse has clear semantic value, Noema may define it explicitly.
| Relationship | Inverse |
|---|---|
| expresses | expressed_by |
| concerns | concerned_by |
| references | referenced_by |
| targets | targeted_by |
| occurs_within | contains |
| constrained_by | constrains |
| governed_by | governs |
| enabled_by | enables |
| authorized_by | authorizes |
| fulfilled_by | fulfills |
| derives_from | source_of |
| depends_on | dependency_of |
| produces | produced_by |
| supported_by | supports |
| affects | affected_by |
| holds | grants_to |
| delegates_to | delegated_from |
| supersedes | superseded_by |
| evaluated_against | evaluation_target_of |
An inverse does not necessarily need to be physically stored.
It may be derived from the canonical directed Relationship.
⸻
## 57. Relationship Attributes
Some Relationships require additional semantic attributes.
Example:
Actor
  └── expresses ──► Intent
        │
        ├── expressed_at
        ├── channel
        └── provenance
Another:
Actor
  └── holds ──► Authority
        │
        ├── valid_from
        ├── valid_until
        └── provenance
Another:
Policy
  └── governs ──► Action
        │
        ├── policy_version
        └── effective_period
Relationship attributes belong to the Relationship.
They should not be placed on an endpoint merely because the implementation makes that convenient.
⸻
## 58. Temporal Validity
Relationships may be temporally valid.
Conceptually:
Relationship
├── valid_from
└── valid_until
Examples include:
- Actor holds Authority;
- Actor belongs to Organization;
- Policy governs an operation;
- Entity ownership;
- Delegation;
- temporary permissions.
Historical validity must be preserved.
A Relationship that is no longer current should not necessarily be deleted from the semantic record.
⸻
## 59. Conditional Relationships
Some Relationships may depend upon explicit conditions.
Example:
Actor
  └── authorized_for ──► Action
        │
        └── condition:
             amount <= $10,000
Conditions should be represented explicitly when they are semantically consequential.
They should not be hidden inside application code or prompts.
⸻
## 60. Relationship Provenance
A consequential Relationship may require provenance.
Example:
Actor
  └── holds ──► ApprovalAuthority
Provenance:
HR authorization record
Observed:
2026-08-23
Provenance is particularly important for Relationships concerning:
- Authority;
- ownership;
- identity;
- Policy applicability;
- approval;
- delegation.
The provenance of a Relationship is distinct from the provenance of either endpoint.
⸻
## 61. Relationship Evidence
Where a Relationship materially affects Trust, the Relationship should be supportable by appropriate Evidence.
Example:
Actor
  └── holds ──► ApprovalAuthority
                    │
                    └── supported_by ──► HRAuthorizationRecord
Conceptually:
Relationship
      ↓
Evidence
      ↓
Trust Evaluation
The ontology should preserve this support relationship where required.
⸻
## 62. Relationship Confidence
Some Relationships may initially be inferred rather than authoritative.
Example:
Actor
  └── likely_belongs_to ──► Organization
Noema must distinguish:
Authoritative Relationship
from:
Inferred Relationship
An inferred Relationship must not automatically be treated as sufficient evidence for a consequential Trust decision.
Confidence is therefore not equivalent to Authority or Evidence sufficiency.
⸻
## 63. Relationship Conflicts
Noema may encounter conflicting Relationships.
Example:
System A:
Alice → Manager
System B:
Alice → Employee
The ontology should preserve the existence and provenance of the conflicting claims rather than silently selecting one.
Resolution may depend upon:
- source authority;
- provenance;
- temporal validity;
- Policy;
- reconciliation rules.
The Relationship model represents the conflict.
The relevant resolution system determines how that conflict is handled.
⸻
## 64. Relationship Lifecycle
Relationship lifecycle depends on Relationship type.
Possible states include:
PROPOSED
ACTIVE
SUSPENDED
EXPIRED
REVOKED
SUPERSEDED
For example:
An Authority relationship may be REVOKED.
An historical expression relationship may remain a valid historical fact.
Lifecycle semantics should therefore be defined by Relationship type rather than universally imposed.
⸻
## 65. Historical Relationship Integrity
Historical Relationships must not be silently rewritten.
Example:
2025:
Alice
  └── holds ──► ManagerAuthority
2026:
ManagerAuthority
  └── revoked
The historical fact remains:
Alice held ManagerAuthority during 2025.
The current Relationship may become inactive without erasing the historical Relationship.
⸻
## 66. Relationship Resolution
Noema may resolve a relevant Relationship graph around an Intent.
Conceptually:
Candidate Relationships
        ↓
Resolution
        ↓
Relevant Relationships
        ↓
Intent Subgraph
Resolution may use:
- authoritative sources;
- Entity identity;
- temporal validity;
- Context;
- provenance;
- Policy;
- Evidence.
Relationship resolution must preserve uncertainty where the Relationship cannot be established.
Unknown must not silently become established.
⸻
## 67. Relevant Relationship Subgraph
Noema does not necessarily need the entire enterprise graph for every Trust evaluation.
It needs the relevant canonical subgraph.
Example:
Actor
   │
   ▼
Intent
 / | \
/  |  \
Entity Policy Constraint
       │
       ▼
    Authority
       │
       ▼
     Trust
       │
       ▼
     Action
The resolved subgraph becomes the semantic context for subsequent evaluation.
⸻
## 68. Minimal Intent Subgraph
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
Only when the relationships required for the consequential decision are sufficiently resolved should the Trust boundary be crossed.
⸻
## 69. Execution Subgraph
Following Trust and Action formation:
Intent
   ↓
Action
   ↓
Execution
   ↓
Outcome
With supporting relationships:
Action
  ├── enabled_by ──► Capability
  ├── affects ─────► Entity
  └── executed_as ─► Execution
                         │
                         └── produces ──► Outcome
This separates:
- intended operation;
- executable operation;
- execution attempt;
- resulting Outcome.
⸻
## 70. Outcome Subgraph
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
This closes the semantic loop.
The resulting Outcome can therefore be evaluated against the originating Intent without conflating execution with satisfaction.
⸻
## 71. Relationship Validation
Before consequential execution, Noema should validate relationships required by the relevant decision.
Example:
Intent
  ├── expressed_by Actor ✓
  ├── concerns Entity ✓
  ├── governed_by Policy ✓
  ├── constrained_by Constraint ✓
  ├── fulfilled_by Action ✓
  └── authorized_by Authority ✗
Result:
The required relationship is unresolved.
Trust must therefore handle the missing relationship according to its canonical decision semantics.
Noema must not silently assume that the missing relationship exists.
⸻
## 72. Relationship Integrity
Noema should enforce semantic integrity for canonical Relationships.
For example:
Action
  └── enabled_by ──► Capability
requires the referenced Capability to be identifiable.
Likewise:
Outcome
  └── evaluated_against ──► Intent
must identify the Intent against which the Outcome is evaluated.
Broken or unresolved Relationships should remain distinguishable from established Relationships.
⸻
## 73. Relationship and Natural Language
Critical Relationships must not exist only inside natural-language prompts.
Bad:
"The user is the account owner, so let them refund it."
The semantic Relationship should instead be represented explicitly:
Actor
  └── owns ──► Account
Likewise:
"She is authorized to approve this."
should resolve to structured Authority information.
Natural language may provide evidence from which a Relationship is proposed or resolved, but consequential Relationships should ultimately be represented canonically.
⸻
## 74. Relationship and Model Reasoning
A Model may assist with:
- Relationship extraction;
- Entity resolution;
- candidate Relationship generation;
- semantic interpretation;
- classification.
The Model should not silently establish consequential Relationships merely because they appear plausible.
The boundary is:
Model
   ↓
Candidate Relationship
   ↓
Evidence / Resolution
   ↓
Canonical Relationship
   ↓
Trust Evaluation
Where sufficient evidence is unavailable, the Relationship remains unresolved or uncertain.
⸻
## 75. Relationship and Trust
Relationships provide the semantic structure required for Trust evaluation.
Conceptually:
Actor
  +
Intent
  +
Entity
  +
Context
  +
Constraint
  +
Policy
  +
Authority
  +
Evidence
        │
        ▼
      Trust
        │
        ▼
      Action
Trust therefore depends not only on individual objects but on the relationships connecting them.
A missing or uncertain consequential Relationship may prevent Trust from establishing that an Action is permitted.
⸻
## 76. Relationship and Execution
Relationships establish semantic prerequisites for execution but do not themselves execute anything.
The distinction is:
Relationship:
Action → enabled_by → Capability
Trust:
Action → permitted
Execution:
Execution → executes → Action
Outcome:
Execution → produces → Outcome
These are separate semantic dimensions.
⸻
## 77. Relationship and Outcome
Relationships preserve the semantic lineage from request through execution and result.
The canonical chain is:
Actor
  ↓
Intent
  ↓
Action
  ↓
Execution
  ↓
Outcome
With supporting relationships:
Intent
  ├── concerns ──► Entity
  ├── occurs_within ──► Context
  ├── constrained_by ──► Constraint
  └── governed_by ──► Policy
Action
  ├── enabled_by ──► Capability
  ├── authorized_by ──► Authority
  └── affects ──► Entity
Outcome
  ├── supported_by ──► Evidence
  └── evaluated_against ──► Intent
This chain preserves semantic lineage without collapsing the concepts into one object.
⸻
## 78. Core Relationship Graph
The foundational Noema relationship graph is:
Actor
  │
  └── expresses ───────────► Intent
                               │
                               ├── concerns ───────► Entity
                               │
                               ├── occurs_within ──► Context
                               │
                               ├── constrained_by ─► Constraint
                               │
                               ├── governed_by ────► Policy
                               │
                               └── fulfilled_by ───► Action
                                                        │
                                                        ├── enabled_by ──► Capability
                                                        │
                                                        ├── affects ─────► Entity
                                                        │
                                                        └── executed_as ─► Execution
                                                                               │
                                                                               └── produces ──► Outcome
                                                                                                  │
                                                                                                  ├── supported_by ──► Evidence
                                                                                                  │
                                                                                                  └── evaluated_against ──► Intent
Governance:
Actor
  └── holds ──► Authority
                   │
                   ├── covers ──► Capability
                   └── scoped_to ──► Entity
Policy
  └── defines ──► Constraint
Trust
  ├── evaluates ──► Policy
  ├── evaluates ──► Authority
  ├── evaluates ──► Constraint
  ├── evaluates ──► Context
  ├── based_on ──► Evidence
  └── permits ──► Action
⸻
## 79. Relationship Categories
For consistency, canonical Relationships may be grouped into semantic categories.
### Expression
expresses
expressed_by
### Reference
concerns
concerned_by
references
targets
### Context
occurs_within
contains
### Governance
governed_by
governs
constrained_by
constrains
authorized_by
authorizes
### Capability
enabled_by
enables
requires
### Fulfillment
fulfilled_by
fulfills
decomposes_into
derives_from
### Execution
executes
executed_as
produces
produced_by
### Evidence
supported_by
supports
verified_by
### Authority
holds
grants_to
covers
scoped_to
delegates_to
delegated_from
### Causality
depends_on
affects
changes
results_in
### Temporal
precedes
follows
supersedes
superseded_by
### Taxonomy
instance_of
subtype_of
belongs_to
### Evaluation
evaluates
evaluated_by
evaluated_against
satisfies
These categories are organizational aids and do not themselves create additional semantic concepts.
⸻
## 80. Relationship Naming Rules
Canonical Relationship predicates should:
1. Use clear semantic verbs.
2. Describe the relationship from Subject → Object.
3. Avoid implementation terminology.
4. Avoid ambiguous predicates where a more precise predicate exists.
5. Prefer domain meaning over storage terminology.
6. Define inverses where they provide semantic value.
7. Define cardinality where semantically meaningful.
8. Define temporal semantics where applicable.
9. Preserve the distinction between ability, permission, governance, and execution.
10. Avoid predicates whose meaning depends entirely on application-specific interpretation.
Prefer:
Actor → expresses → Intent
over:
Actor → has → Intent
Prefer:
Actor → holds → Authority
over:
Actor → has → Authority
Prefer:
Action → enabled_by → Capability
over:
Action → uses → Capability
because "uses" does not establish whether the Capability enables the Action, is merely referenced, or is actually exercised.
⸻
## 81. Relationship Anti-Patterns
### Generic `has`
Avoid:
Actor has Intent
Actor has Authority
Action has Capability
These relationships collapse distinct semantics.
Prefer:
Actor expresses Intent
Actor holds Authority
Action enabled_by Capability
### Implicit Relationships
Do not rely on naming conventions to imply relationships.
Bad:
action.customer_refund
with an assumption that it corresponds to:
intent.refund_customer
The Relationship should be explicit.
### Prompt-Only Relationships
Do not encode critical relationships only in prompts.
Bad:
"The user owns this account."
Prefer:
Actor → owns → Account
with appropriate Evidence and provenance.
### Inferred-as-Authoritative Relationships
Do not treat a plausible inference as an established consequential fact.
Bad:
"Likely manager" → treated as ManagerAuthority.
Instead:
Candidate Relationship
   ↓
Evidence / Resolution
   ↓
Canonical Relationship
### Hidden Relationship Conditions
Do not encode consequential conditions only in application code.
Bad:
application logic silently assumes:
amount <= authority.limit
Prefer explicit scoped or conditional Relationship semantics where appropriate.
⸻
## 82. Relationship Resolution and Uncertainty
Noema must preserve the difference between:
ESTABLISHED
INFERRED
CONFLICTING
UNKNOWN
A Relationship that cannot currently be established should not silently become an established Relationship.
Example:
Actor
  └── holds ──► Authority
If the available Evidence does not establish this Relationship:
Authority status:
UNKNOWN
not:
Authority:
PRESENT
This distinction is particularly important at the Trust boundary.
⸻
## 83. Relationship Provenance and Authority
Provenance answers:
> Where did this Relationship come from?
Authority answers:
> Why is that source entitled to establish or assert this Relationship?
Example:
Relationship:
FinanceManager → holds → RefundApprovalAuthority
Provenance:
Finance authorization record
Source authority:
Finance governance authority
These concepts must remain distinct.
⸻
## 84. Relationship Versioning
Relationships may change over time.
Where historical reproducibility matters, changes should preserve the relevant historical state rather than silently mutating the past.
Example:
2025:
Alice → holds → ManagerAuthority
2026:
Alice → holds → DirectorAuthority
The system should retain sufficient temporal information to determine which Relationship was valid at a given time.
Relationship versioning must not be confused with Policy versioning.
⸻
## 85. Relationship Supersession
A later Relationship may supersede an earlier Relationship without erasing it.
Example:
Authority A
  └── superseded_by ──► Authority B
or:
Relationship B
  └── supersedes ──► Relationship A
Supersession preserves historical lineage.
It does not imply that the earlier Relationship never existed.
⸻
## 86. Relationship Simulation
Noema may resolve and evaluate Relationships without executing an Action.
Example:
Question:
"What Relationships would exist if this employee attempted to approve a $50,000 expense?"
Noema could construct the relevant semantic subgraph and evaluate its implications without performing the Action.
This supports:
- testing;
- administration;
- debugging;
- compliance;
- workflow design.
Simulation must remain distinguishable from actual execution.
⸻
## 87. Relationship Impact
Changes to consequential Relationships may affect Trust decisions.
Examples:
- Authority revoked;
- Entity ownership changed;
- Policy applicability changed;
- Capability removed;
- Constraint changed;
- Evidence invalidated.
Therefore:
Resolved Intent
      ↓
Relationship Change
      ↓
Relevant subgraph changed
      ↓
Trust re-evaluation may be required
The Intent remains historically valid.
Its execution eligibility may change.
⸻
## 88. Relationship Re-evaluation
Material changes to relevant Relationships may require re-evaluation before consequential execution.
Examples:
- Actor → holds → Authority changes;
- Intent → governed_by → Policy changes;
- Policy → defines → Constraint changes;
- Evidence → supports → Outcome becomes invalid;
- Entity relationship changes;
- Context relationship changes.
Noema should not assume that a previously resolved Relationship graph remains valid indefinitely.
⸻
## 89. Relationship Integrity at the Trust Boundary
Before an Action crosses the Trust boundary, Noema should be able to identify the relationships required to support the decision.
Conceptually:
Actor
  ↓
expresses
  ↓
Intent
  ├── concerns ──► Entity
  ├── occurs_within ──► Context
  ├── constrained_by ──► Constraint
  ├── governed_by ──► Policy
  └── fulfilled_by ──► Action
                         ├── enabled_by ──► Capability
                         └── authorized_by ──► Authority
Evidence supports the relevant claims.
Trust evaluates the resolved structure.
Only then:
Trust
  ↓
permits
  ↓
Action
The relationship graph therefore forms part of the semantic boundary preceding execution.
⸻
## 90. Canonical Relationship Invariants
The following are foundational invariants:
1. Relationships are semantic facts, not implementation details.
2. Canonical Relationships have explicit direction.
3. Relationship predicates use controlled semantic vocabulary.
4. Actor expresses Intent.
5. Intent may concern one or more Entities.
6. Intent occurs within Context.
7. Intent may be constrained by Constraints.
8. Intent may be governed by Policies.
9. Intent may be fulfilled by one or more Actions.
10. Action is enabled by Capability.
11. Action may affect one or more Entities.
12. Action may be governed by Policy.
13. Action may require Authority.
14. Trust evaluates relevant Policies, Constraints, Authority, Context, and Evidence.
15. Trust may permit an Action.
16. Execution executes an Action.
17. Execution may produce one or more Outcomes.
18. Outcome may affect or describe changes involving Entities.
19. Outcome may be supported by Evidence.
20. Outcome may be evaluated against the originating Intent.
21. Intent may decompose into subordinate Intents.
22. Intent may derive from another Intent.
23. Intent may depend on another Intent.
24. Policy may define a Constraint.
25. Capability may require another Capability.
26. Authority may cover a Capability.
27. Authority may be scoped to an Entity or other defined scope.
28. Authority may be delegated between Actors.
29. Relationships may have provenance.
30. Relationships may have temporal validity.
31. Consequential Relationships should be supported by sufficient Evidence.
32. Inferred Relationships must remain distinguishable from authoritative Relationships.
33. Unknown Relationships must not silently become established facts.
34. Conflicting Relationships must remain representable.
35. Historical Relationships must not be silently overwritten.
36. Relationship supersession must preserve historical lineage.
37. Relationship metadata belongs to the Relationship where semantically applicable.
38. Relationship semantics must remain independent of storage technology.
39. Natural-language prompts must not be the sole representation of consequential Relationships.
40. The Model may assist in Relationship extraction and resolution but must not silently establish consequential Relationships without sufficient grounding.
⸻
## 91. Canonical Relationship Chain
The primary Noema relationship chain is:
Actor
  │
  │ expresses
  ▼
Intent
  │
  ├── concerns ───────► Entity
  │
  ├── occurs_within ──► Context
  │
  ├── constrained_by ─► Constraint
  │
  ├── governed_by ────► Policy
  │
  └── fulfilled_by ───► Action
                            │
                            ├── enabled_by ──► Capability
                            ├── affects ─────► Entity
                            └── executed_as ─► Execution
                                                   │
                                                   └── produces ─► Outcome
                                                                      │
                                                                      ├── supported_by ─► Evidence
                                                                      │
                                                                      └── evaluated_against ─► Intent
Governance:
Actor
  │
  └── holds ──► Authority
                  │
                  ├── covers ──► Capability
                  └── scoped_to ──► Entity
Policy
  │
  └── defines ──► Constraint
Trust
  ├── evaluates ──► Policy
  ├── evaluates ──► Constraint
  ├── evaluates ──► Authority
  ├── evaluates ──► Context
  ├── based_on ──► Evidence
  └── permits ──► Action
⸻
## 92. Canonical Principle
Noema's ontology is not merely a collection of concepts.
It is a typed semantic model in which Relationships establish:
- who expressed an Intent;
- what the Intent concerns;
- where and under what Context it exists;
- what Constraints apply;
- which Policies govern it;
- what Authority is relevant;
- which Capability enables the Action;
- what Action fulfills the Intent;
- what Execution occurred;
- what Outcome resulted;
- what Evidence supports the relevant claims;
- and how the Outcome relates back to the originating Intent.
The fundamental semantic chain is:
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
   ↓
Satisfaction
Relationships therefore constitute the connective structure of Noema's canonical model.
They connect the ontology without collapsing its concepts into one another.
The canonical boundary is:
Concepts
   +
Relationships
   +
Context
   +
Evidence
       ↓
Resolution
       ↓
Trust
       ↓
Execution
       ↓
Outcome
Noema should preserve this distinction throughout the architecture.