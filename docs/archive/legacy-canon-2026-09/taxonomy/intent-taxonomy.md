> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Taxonomy

Status: Foundational
Version: 0.1
Domain: Taxonomy
Canonical Path: taxonomy/intent-taxonomy.md

⸻

1. Definition

The Intent Taxonomy is Noema’s canonical classification system for the semantic forms of Intent that an Actor may express.

It provides a controlled vocabulary for classifying Intent without conflating:

* what the Actor wants
* how the Intent is interpreted
* how the Intent is validated
* whether the Intent is trusted
* how the Intent is executed
* what Actions are required
* what Outcome occurs

The taxonomy therefore describes semantic Intent, not execution strategy.

The canonical relationship is:

Actor Expression
      ↓
Interpretation
      ↓
Intent
      ↓
Intent Taxonomy
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Execution
      ↓
Outcome

The taxonomy provides semantic classification within the Intent layer.

It does not authorize execution.

⸻

2. Purpose

The Intent Taxonomy exists to provide a stable semantic vocabulary through which Noema can classify and reason about Intent.

It supports:

* Intent interpretation
* Intent resolution
* semantic validation
* capability discovery
* Action Graph construction
* policy evaluation
* analytics
* observability
* provenance
* domain modeling
* interoperability
* testing
* deterministic processing
* future taxonomy evolution

The taxonomy must remain sufficiently abstract to represent Intent across domains while allowing domain-specific extensions.

⸻

3. Core Principle

An Intent describes an Actor’s desired objective.

The taxonomy describes the semantic class of that objective.

For example:

Intent:
"Send ₦50,000 to John."
Taxonomic classification:
TRANSFER

The classification does not determine:

* whether the Actor is authorized
* whether the transfer is permitted
* which payment capability will execute it
* which Action Graph is selected
* whether the transfer succeeds

Therefore:

Intent Classification
        ≠
Authorization
        ≠
Execution
        ≠
Outcome

⸻

4. Taxonomy vs Ontology

The Intent Ontology defines the semantic structure of Intent.

The Intent Taxonomy classifies Intent within that structure.

Conceptually:

Intent Ontology
      │
      ├── Actor
      ├── Objective
      ├── Action
      ├── Subject
      ├── Parameters
      ├── Constraints
      ├── Desired Outcome
      └── Provenance
             │
             ▼
       Intent Taxonomy
             │
             ├── Inquiry
             ├── Retrieval
             ├── Creation
             ├── Modification
             ├── Deletion
             ├── Transfer
             ├── Communication
             └── ...

The taxonomy must not become a substitute for the underlying semantic representation.

⸻

5. Taxonomic Classification

An Intent may be classified according to several semantic dimensions.

A canonical classification may include:

1. Intent Family
2. Intent Type
3. Target
4. Operation
5. Objective
6. Temporal Character
7. Constraint Profile
8. Composition
9. Interaction Requirement
10. Execution Characteristics

These dimensions should remain distinguishable.

For example:

Family:
TRANSFER
Operation:
MOVE
Target:
FUNDS
Temporal Character:
IMMEDIATE
Interaction Requirement:
NONE

The exact representation belongs to the Intent ontology.

⸻

6. Intent Family

An Intent Family is a broad semantic category describing the primary nature of an Actor’s objective.

Canonical families may include:

INQUIRE
RETRIEVE
CREATE
MODIFY
DELETE
TRANSFER
COMMUNICATE
AUTHORIZE
APPROVE
REJECT
CANCEL
SCHEDULE
MONITOR
VERIFY
COMPARE
DISCOVER
NAVIGATE
CONFIGURE
SUBSCRIBE
UNSUBSCRIBE

The taxonomy may evolve as additional domains are modeled.

The family should describe semantic purpose rather than implementation.

⸻

7. Inquiry Intent

An Inquiry Intent seeks information, explanation, status, or understanding without necessarily requesting a state-changing Action.

Examples:

"What is my account balance?"
"Why was my payment declined?"
"What does this charge mean?"

The taxonomy should distinguish information-seeking from execution-seeking Intent.

An Inquiry does not inherently imply permission to modify state.

⸻

8. Retrieval Intent

A Retrieval Intent requests access to an identifiable piece of information or resource.

Examples:

"Show my recent transactions."
"Get my latest statement."
"Find my insurance policy."

Retrieval may require authorization and Trust.

The taxonomy does not establish that the Actor is entitled to access the requested information.

⸻

9. Creation Intent

A Creation Intent seeks to create a new resource, record, relationship, or state.

Examples:

"Create a new account."
"Open a support ticket."
"Create a payment."

Creation may result in multiple Actions.

For example:

Intent:
Create account
Action Graph:
Verify identity
      ↓
Validate eligibility
      ↓
Create account
      ↓
Confirm creation

The taxonomy classifies the objective, not the resulting execution graph.

⸻

10. Modification Intent

A Modification Intent seeks to change an existing resource or state.

Examples:

"Change my delivery address."
"Update my notification settings."
"Increase my transfer limit."

Modification should be distinguished from creation and deletion even where the underlying system implements them through similar APIs.

⸻

11. Deletion Intent

A Deletion Intent seeks to remove or terminate an existing resource, relationship, or state.

Examples:

"Delete this document."
"Remove this beneficiary."
"Close my account."

Deletion may be irreversible or consequential.

The taxonomy identifies the semantic objective.

Trust, policy, confirmation, and Action Contracts determine whether execution is permissible.

⸻

12. Transfer Intent

A Transfer Intent seeks to move ownership, value, control, location, or another transferable resource from one context to another.

Examples:

"Send ₦50,000 to John."
"Move these funds to my savings account."
"Transfer ownership of the document."

Transfer semantics should identify:

source
destination
resource
amount or quantity
constraints

where applicable.

Transfer does not imply financial transfer specifically.

The taxonomy should support broader transfer semantics.

⸻

13. Communication Intent

A Communication Intent seeks to communicate information to one or more recipients.

Examples:

"Send the report to John."
"Notify me when the package arrives."
"Email the customer."

Communication may involve:

* recipient resolution
* channel selection
* content construction
* timing
* delivery requirements

These are semantic properties of the Intent where relevant, not necessarily separate Intent families.

⸻

14. Authorization Intent

An Authorization Intent seeks to establish or modify permission, consent, delegation, or authority.

Examples:

"Allow John to access the account."
"Give the finance team permission to approve payments."

Authorization Intent must not be confused with the Trust system.

The Actor may express an Intent concerning authorization, while the Trust and governance layers determine what authority actually exists.

⸻

15. Approval Intent

An Approval Intent expresses a decision to approve a previously presented operation, request, or condition.

Example:

"Approve the transfer."

Approval is distinct from execution.

Conceptually:

Approval Intent
      ↓
Approval State
      ↓
Trust / Governance Evaluation
      ↓
Action Execution

An approval must not automatically imply execution.

⸻

16. Rejection Intent

A Rejection Intent expresses that an Actor or authorized authority rejects a proposal, request, or operation.

Example:

"Reject this payment request."

Rejection may produce downstream state changes, but the taxonomy classifies the Actor’s objective rather than prescribing those changes.

⸻

17. Cancellation Intent

A Cancellation Intent seeks to stop, revoke, withdraw, or terminate an existing pending objective or operation.

Examples:

"Cancel my transfer."
"Cancel the subscription."
"Stop the shipment."

Cancellation must remain distinct from deletion.

Deletion concerns the target resource or state.

Cancellation concerns an ongoing, pending, or previously requested operation or commitment.

⸻

18. Scheduling Intent

A Scheduling Intent seeks to establish when an Action or objective should occur.

Examples:

"Send the report tomorrow."
"Schedule the payment for Friday."

Scheduling may be represented as:

Intent
+
Temporal Constraint

rather than as an independent objective where appropriate.

The taxonomy must preserve the distinction between:

what should happen

and:

when it should happen

⸻

19. Monitoring Intent

A Monitoring Intent seeks continued observation of a resource, condition, or event.

Examples:

"Watch the delivery status."
"Let me know if the price changes."
"Monitor this account."

Monitoring may result in a durable execution relationship rather than a single Action.

Its execution semantics therefore belong to the relevant architecture for loops and durable execution.

⸻

20. Verification Intent

A Verification Intent seeks to establish whether a claim, state, identity, condition, or property is true.

Examples:

"Verify my identity."
"Check whether the payment went through."
"Confirm that the address is correct."

Verification may be:

* semantic
* informational
* identity-related
* business-state-related
* execution-result-related

The taxonomy should preserve the distinction between verification as an Actor objective and validation as an internal Noema control.

⸻

21. Discovery Intent

A Discovery Intent seeks to identify available entities, resources, capabilities, or options.

Examples:

"Find available flights."
"Show me payment methods."
"Find a suitable account."

Discovery may precede another Intent.

For example:

DISCOVER
   ↓
SELECT
   ↓
EXECUTE

Discovery must not automatically imply selection.

⸻

22. Comparison Intent

A Comparison Intent seeks to evaluate multiple identified or discovered alternatives according to specified attributes or constraints.

Example:

"Compare these three insurance plans."

Comparison is primarily informational unless the Intent explicitly includes a subsequent selection or execution objective.

The taxonomy should therefore distinguish:

COMPARE

from:

SELECT

and:

PURCHASE

⸻

23. Selection Intent

A Selection Intent seeks to choose an option, resource, capability, or alternative from a defined set.

Example:

"Use the standard delivery option."

Selection may influence later Action Graph construction.

Selection does not itself imply execution unless the Intent explicitly contains that objective.

⸻

24. Configuration Intent

A Configuration Intent seeks to establish or modify system, account, resource, or operational configuration.

Examples:

"Set my notification preference to email."
"Configure automatic payments."

Configuration differs from general Modification when the semantic objective specifically concerns operational configuration.

⸻

25. Subscription Intent

A Subscription Intent seeks to establish an ongoing relationship with a service, resource, or recurring process.

Examples:

"Subscribe me to the service."
"Turn on monthly billing."

The taxonomy should distinguish establishing an ongoing relationship from performing a single transaction.

⸻

26. Unsubscription Intent

An Unsubscription Intent seeks to terminate an ongoing subscription or recurring relationship.

Example:

"Cancel my monthly subscription."

Where the semantic objective is specifically termination of a subscription relationship, the taxonomy may classify it as:

UNSUBSCRIBE

rather than generic:

DELETE

or:

CANCEL

The exact classification precedence should be determined by canonical taxonomy rules.

⸻

27. Objective vs Operation

The taxonomy must distinguish semantic objective from operational Action.

For example:

Intent:
Renew my card.
Objective:
Maintain valid card access.
Operational Actions:
Check eligibility
Verify account
Request replacement
Confirm replacement

Therefore:

Intent Taxonomy
        ≠
Action Taxonomy

The same Intent Type may result in different Action Graphs depending on capabilities, policies, context, and contracts.

⸻

28. Target Taxonomy

Intent classification may include the semantic target of the objective.

Examples:

ACCOUNT
CARD
PAYMENT
DOCUMENT
MESSAGE
PERSON
SUBSCRIPTION
TRANSFER
ORDER
RESOURCE
CAPABILITY
CONFIGURATION

Target classification should be extensible.

The target identifies what the Intent concerns.

It does not necessarily identify the system that owns the target.

⸻

29. Resource Identity

Where an Intent concerns a specific resource, its identity should be represented separately from its taxonomic type.

Example:

Target Type:
CARD
Target Identity:
card_123

The taxonomy must not encode individual business resources as taxonomy members.

Therefore:

CARD

is a taxonomic category.

card_123

is a resource identity.

⸻

30. Intent Polarity

Intent may express different semantic directions.

Examples include:

CREATE
ENABLE
ACTIVATE
INCREASE
ADD

versus:

DELETE
DISABLE
DEACTIVATE
DECREASE
REMOVE

The taxonomy should preserve these semantic distinctions where they affect interpretation or execution.

⸻

31. State-Transition Intent

Some Intents can be understood as requests to move a target from one state to another.

Example:

subscription:
ACTIVE → CANCELLED

or:

card:
EXPIRED → REPLACEMENT_REQUESTED

The Intent may encode:

target
desired_state
constraints

The external authoritative system remains responsible for determining actual business state.

⸻

32. Temporal Taxonomy

Intent may contain temporal semantics.

Canonical temporal characteristics may include:

IMMEDIATE
SCHEDULED
DEADLINE
DURATIONAL
RECURRING
CONDITIONAL
CONTINUOUS

For example:

"Send the report tomorrow."

contains:

Communication Intent
+
Scheduled temporal constraint

The temporal dimension should not be confused with execution scheduling mechanics.

⸻

33. Conditional Intent

An Intent may be conditional.

Example:

"Send me the report if the balance falls below ₦10,000."

The semantic structure includes:

Objective:
notify_actor
Condition:
balance < ₦10,000

The condition is part of the Intent semantics.

The execution mechanism belongs to the appropriate downstream architecture.

⸻

34. Recurring Intent

An Intent may express a recurring objective.

Example:

"Send me my statement every month."

The Intent contains:

Objective:
retrieve and communicate statement
Temporal Character:
RECURRING
Recurrence:
monthly

Recurring execution should be represented through explicit durable semantics rather than hidden scheduler behavior.

⸻

35. Composite Intent

An Intent may contain multiple semantic objectives.

Example:

"Close my account, transfer the balance,
and send me confirmation."

Possible components:

1. CLOSE_ACCOUNT
2. TRANSFER_FUNDS
3. COMMUNICATE

The taxonomy must preserve the component relationship.

Composite classification must not erase:

* ordering
* dependency
* atomicity
* partial-execution semantics
* provenance

⸻

36. Intent Composition

Composite Intent may be represented as:

Composite Intent
       │
       ├── Intent A
       ├── Intent B
       └── Intent C

or through a structured Intent containing multiple objectives.

The canonical representation belongs to the Intent ontology.

The taxonomy should classify the components independently where necessary.

⸻

37. Atomic Intent

An Intent may contain an explicit requirement that its objectives be treated as a unit.

Example:

"Transfer the funds only if the account is successfully closed."

The semantic relationship may require atomic or conditionally coupled execution.

The taxonomy does not itself establish atomicity.

Atomicity is an Intent constraint that downstream execution semantics must respect.

⸻

38. Informational vs Consequential Intent

A useful semantic distinction is between:

INFORMATIONAL

and:

CONSEQUENTIAL

Informational Intent primarily seeks information.

Consequential Intent seeks to cause an external state change.

Examples:

"What is my balance?"

→ informational

"Transfer ₦50,000."

→ consequential

The distinction is important for downstream Trust and execution controls.

It does not itself determine Trust.

⸻

39. Read vs Write Semantics

Intent may also be classified by whether it seeks:

READ

or:

WRITE

A retrieval request is generally read-oriented.

A creation or modification request is generally write-oriented.

However, classification must remain semantic rather than dependent on the implementation method.

A technically read-only API may still participate in a consequential Intent.

⸻

40. External-Effect Classification

Intent may be classified according to whether fulfillment produces an external effect.

Examples:

NO_EXTERNAL_EFFECT
EXTERNAL_STATE_CHANGE
EXTERNAL_COMMUNICATION
FINANCIAL_EFFECT
AUTHORITY_CHANGE
RESOURCE_CREATION
RESOURCE_DELETION

These are semantic characteristics, not permission decisions.

⸻

41. Risk-Relevant Classification

Certain Intent types may require additional governance because of their potential consequences.

Examples may include:

financial transfer
account deletion
credential modification
authority delegation
high-impact external communication

The taxonomy may provide classification signals for Trust and policy systems.

It must not itself assign risk scores or authorization outcomes unless explicitly defined by another canonical specification.

Therefore:

Intent Type
      ↓
Policy / Risk Evaluation

not:

Intent Type
      ↓
Automatically Trusted

⸻

42. Domain Taxonomy

The core taxonomy should remain domain-independent.

Domain-specific taxonomies may extend it.

For example:

Core Intent:
TRANSFER
Banking Extension:
TRANSFER_FUNDS
Logistics Extension:
TRANSFER_SHIPMENT
Document Extension:
TRANSFER_OWNERSHIP

The extension must preserve the semantics of the parent category.

⸻

43. Taxonomy Hierarchy

The taxonomy may use hierarchical relationships.

Example:

INTENT
│
├── INFORMATIONAL
│   ├── INQUIRE
│   ├── RETRIEVE
│   ├── VERIFY
│   ├── DISCOVER
│   └── COMPARE
│
└── CONSEQUENTIAL
    ├── CREATE
    ├── MODIFY
    ├── DELETE
    ├── TRANSFER
    ├── COMMUNICATE
    ├── AUTHORIZE
    ├── APPROVE
    ├── REJECT
    ├── CANCEL
    ├── SCHEDULE
    ├── CONFIGURE
    ├── SUBSCRIBE
    └── UNSUBSCRIBE

This is a conceptual hierarchy.

The canonical taxonomy may evolve as Noema’s ontology develops.

⸻

44. Multiple Classification Dimensions

An Intent may belong to multiple semantic classifications without being multiple unrelated Intents.

Example:

"Send ₦50,000 to John tomorrow."
Primary Family:
TRANSFER
Target:
FUNDS
Temporal:
SCHEDULED
Effect:
FINANCIAL
Direction:
OUTBOUND

These dimensions should not be collapsed into one label.

A single classification field should not be expected to encode the full semantic structure.

⸻

45. Primary Intent Type

Where one primary taxonomic type is required, Noema should identify the type corresponding to the Actor’s principal objective.

For example:

"Please send the report to John tomorrow."
Primary:
COMMUNICATE
Secondary semantic attributes:
recipient = John
temporal = tomorrow
resource = report

The primary classification should not be determined merely by whichever downstream Action happens to be most consequential.

⸻

46. Secondary Characteristics

Secondary characteristics may describe:

* temporal behavior
* target class
* direction
* recurrence
* conditions
* composition
* external effect
* interaction requirements
* constraints

These characteristics provide semantic precision without fragmenting the primary Intent type.

⸻

47. Intent Taxonomy and Clarification

Taxonomy can identify the type of missing semantic information required for clarification.

Example:

Intent Type:
TRANSFER
Missing:
RECIPIENT
Status:
CLARIFICATION_REQUIRED

The taxonomy should therefore help identify semantic requirements without guessing their values.

⸻

48. Ambiguous Taxonomic Classification

An expression may itself be ambiguous.

Example:

"Stop my account."

Potential interpretations:

CANCEL
CLOSE_ACCOUNT
DISABLE
SUSPEND

The Intent Engine must preserve the ambiguity until canonical semantics can be established.

The taxonomy must not force premature classification.

⸻

49. Taxonomy Does Not Resolve Ambiguity

The taxonomy provides categories.

The Intent Engine establishes which category applies to a particular Intent.

Therefore:

Expression
   ↓
Candidate Classifications
   ↓
Intent Resolution
   ↓
Canonical Classification

A model’s highest-probability classification is not automatically canonical.

⸻

50. Classification Provenance

Material taxonomic classification should retain provenance.

Conceptually:

classification:
    TRANSFER
source:
    deterministic_rule
rule_version:
    2.1
evidence:
    intent.objective = transfer_funds

Possible sources include:

ACTOR
MODEL
DETERMINISTIC_RULE
CONTEXT
EXTERNAL_EVIDENCE
CLARIFICATION

Classification provenance supports auditability and re-evaluation.

⸻

51. Model Classification

A model may propose:

candidate_type = TRANSFER
confidence = 0.97

This is candidate information.

The canonical Intent Taxonomy classification is established only after the Intent Engine’s resolution process.

Therefore:

Model Confidence ≠ Canonical Classification

⸻

52. Taxonomy Determinism

Where classification is governed by deterministic rules, the result should be reproducible from:

Intent
+
Context
+
Evidence
+
Taxonomy Version
+
Classification Rules

The taxonomy must therefore be versioned.

Changes to classification rules should be reconstructible.

⸻

53. Taxonomy Versioning

Taxonomy definitions should have explicit versions.

Example:

Taxonomy Version:
0.1

A classification record may therefore contain:

intent_id
intent_version
taxonomy_version
classification
classification_provenance

Historical Intent records must remain interpretable against the taxonomy version under which they were classified.

⸻

54. Taxonomy Evolution

Taxonomy evolution may introduce:

new categories
renamed categories
split categories
merged categories
deprecated categories
domain extensions

Changes must preserve historical interpretability.

A historical classification should not become meaningless merely because the taxonomy evolves.

⸻

55. Taxonomy Deprecation

A taxonomy member may become deprecated.

Deprecation means:

No new Intent should normally receive this classification.

It does not mean:

Historical Intents are rewritten.

Historical classification remains part of provenance.

⸻

56. Taxonomy Migration

When a classification changes materially, migration should be explicit.

Example:

OLD_TYPE
   ↓
taxonomy migration rule
   ↓
NEW_TYPE

Migration must preserve:

* original classification
* taxonomy version
* migration rule
* migration timestamp
* resulting classification

Noema must not silently rewrite historical semantic state.

⸻

57. Unknown Classification

The taxonomy must support explicit uncertainty.

Possible states include:

CLASSIFIED
UNCLASSIFIED
AMBIGUOUS
UNKNOWN
UNSUPPORTED

Unknown must not be silently mapped to a generic category merely to allow processing.

⸻

58. Unsupported Intent

An Intent may be semantically clear but not represented by the current taxonomy.

Example:

Intent:
OBJECTIVE = previously unsupported domain operation

The result may be:

UNSUPPORTED

rather than an inaccurate classification.

This preserves semantic integrity.

⸻

59. Taxonomy Validation

Taxonomy validation may establish:

* classification exists
* classification belongs to the active taxonomy version
* hierarchy relationships are valid
* required classification dimensions are present
* deprecated categories are handled correctly
* incompatible classifications are rejected
* extensions preserve parent semantics

Taxonomy validation does not establish Trust.

⸻

60. Classification Constraints

The taxonomy may define incompatibilities.

For example, an Intent should not simultaneously be classified as:

CREATE

and:

DELETE

as its single primary operation unless the Intent is explicitly composite.

Likewise:

INFORMATIONAL

and:

CONSEQUENTIAL

may coexist as different dimensions but should not be confused as a single mutually exclusive classification field.

The exact compatibility rules belong to the taxonomy specification.

⸻

61. Taxonomy and Composite Intent

Composite Intents should preserve classifications for each component.

Example:

Composite Intent
│
├── CLOSE_ACCOUNT
│
├── TRANSFER_FUNDS
│
└── COMMUNICATE

The composite itself may be classified:

COMPOSITE

while retaining component classifications.

This prevents loss of semantic information.

⸻

62. Taxonomy and Action Graph

The Intent Taxonomy may influence Action Graph construction.

Conceptually:

Intent Type:
TRANSFER
        ↓
Required semantic properties:
source
destination
resource
amount
        ↓
Candidate Actions
        ↓
Action Graph

The taxonomy does not prescribe the exact Action Graph.

Different capabilities and domains may produce different graphs for the same Intent type.

⸻

63. Taxonomy and Capability Discovery

Intent classification may support capability discovery.

Example:

Intent:
TRANSFER_FUNDS
        ↓
Required Capability Class:
fund.transfer

Capability discovery identifies possible mechanisms.

Capability availability does not establish authorization.

Therefore:

Intent Taxonomy
      ↓
Capability Discovery
      ↓
Capability Binding

remains distinct from Trust.

⸻

64. Taxonomy and Policy

Policy may be expressed against taxonomic categories.

For example:

IF Intent.Type = TRANSFER
AND amount > threshold
THEN approval required

The taxonomy therefore provides a stable semantic reference for policy.

However, policy evaluation remains a separate responsibility.

The taxonomy does not encode the resulting policy decision.

⸻

65. Taxonomy and Trust

Trust may consume Intent classification as one input.

For example:

Intent Type
      +
Actor
      +
Context
      +
Policy
      +
Evidence
      ↓
Trust Evaluation

The taxonomy does not produce:

TRUSTED

or:

BLOCKED

Those remain Trust states.

⸻

66. Taxonomy and Execution

The taxonomy does not specify execution.

For example:

TRANSFER

does not specify:

* API
* provider
* database
* tool
* execution sequence
* retry strategy
* compensation
* consumer

Those concerns belong to Action Graph, Action Contract, execution, and engineering specifications.

⸻

67. Taxonomy and Outcome

Intent classification must not be inferred from execution outcome.

For example:

Intent Type:
TRANSFER
Execution:
FAILED

remains a Transfer Intent.

Likewise:

Intent Type:
TRANSFER
Execution:
COMPLETED

does not change the Intent type.

Intent describes the objective.

Outcome describes what happened.

⸻

68. Intent Type vs Outcome

The following must remain distinct:

Intent:
TRANSFER
Trust:
READY
Graph:
EXECUTING
Execution:
FAILED
Outcome:
UNKNOWN

Each represents a different architectural dimension.

Taxonomy belongs to the Intent dimension.

⸻

69. Semantic Direction

Some Intent families require directional attributes.

For example:

TRANSFER

may include:

INBOUND
OUTBOUND
INTERNAL
EXTERNAL

Direction should be represented as a semantic property where applicable.

It should not create unnecessary duplicate taxonomy members such as:

TRANSFER_INBOUND
TRANSFER_OUTBOUND
TRANSFER_INTERNAL

unless the ontology explicitly requires those categories.

⸻

70. Actor-Relative Intent

Intent classification must remain relative to the Actor’s objective.

For example:

"Receive my salary into this account."

may involve an external transfer from the Actor’s perspective.

The taxonomy should classify the semantic objective rather than infer domain semantics solely from the technical direction of an underlying transaction.

⸻

71. Goal-Oriented Classification

Where possible, classification should reflect the Actor’s goal rather than implementation details.

Example:

"Make sure my card remains usable."

may result in Actions involving:

* status checks
* replacement
* activation
* verification

The Intent should not be classified merely as:

CARD_REPLACEMENT

unless replacement is actually established as the Actor’s objective.

The semantic goal remains primary.

⸻

72. Avoiding Action Leakage

The taxonomy must not become an Action catalogue.

For example:

CHECK_CARD_STATUS
CREATE_REPLACEMENT_REQUEST
SEND_NOTIFICATION

are Actions.

They should not automatically become Intent types.

The corresponding Intent may be:

MAINTAIN_CARD_ACCESS

or another canonical objective defined by the Intent ontology.

This distinction is fundamental.

⸻

73. Avoiding Implementation Leakage

Taxonomy members should not encode:

* API names
* database tables
* provider names
* tool names
* model names
* HTTP methods
* internal service names

For example:

STRIPE_CREATE_PAYMENT

is not an appropriate generic Intent taxonomy member.

A semantic classification such as:

CREATE_PAYMENT

can later bind to a capability.

⸻

74. Domain Extensions

Domain taxonomies may specialize core categories.

Example:

CORE
TRANSFER
   │
   ├── FINANCIAL_TRANSFER
   │     ├── TRANSFER_FUNDS
   │     └── TRANSFER_PAYMENT
   │
   └── OWNERSHIP_TRANSFER
         └── TRANSFER_ASSET

Domain extensions must preserve the parent semantic contract.

They must not redefine a parent category in a contradictory manner.

⸻

75. Taxonomy Names

Canonical taxonomy identifiers should be:

* stable
* machine-readable
* unambiguous
* semantically meaningful
* independent of natural-language phrasing
* independent of implementation

Examples:

TRANSFER
CREATE
MODIFY
DELETE
RETRIEVE
COMMUNICATE
VERIFY
CANCEL
SCHEDULE

Human-readable descriptions may accompany canonical identifiers.

Descriptions do not replace identifiers.

⸻

76. Synonyms

Natural-language expressions may map to the same taxonomy member.

For example:

"send money"
"move funds"
"transfer ₦50,000"

may all resolve to:

TRANSFER

The mapping must depend on semantic resolution rather than keyword matching alone.

⸻

77. Polysemy

The same expression may map to different Intent types depending on context.

Example:

"Stop the service."

may mean:

CANCEL_SUBSCRIPTION

or:

DISABLE_SERVICE

The taxonomy therefore cannot independently resolve language.

The Intent Engine must establish the canonical meaning.

⸻

78. Taxonomy and Natural Language

Natural language is not the taxonomy.

The taxonomy is a canonical semantic representation.

Therefore:

Natural Language
        ↓
Interpretation
        ↓
Canonical Intent
        ↓
Taxonomic Classification

not:

Keyword
   ↓
Intent Type

A keyword can provide evidence.

It cannot by itself establish semantic authority.

⸻

79. Taxonomy and Clarification Loops

If taxonomic classification cannot be established because the Actor’s objective is ambiguous, the Clarification Loop may be invoked.

Conceptually:

Expression
    ↓
Candidate Intent
    ↓
Ambiguous Classification
    ↓
Clarification
    ↓
Resolved Intent
    ↓
Canonical Classification

The loop terminates when the required semantic uncertainty is resolved or the Intent is otherwise terminated.

⸻

80. Taxonomy and Operational Learning

Operational observations may reveal new Intent patterns.

For example:

Observed Expressions
        ↓
Repeated semantic pattern
        ↓
Taxonomy candidate
        ↓
Formal taxonomy review
        ↓
Taxonomy version

Operational learning must not silently modify the canonical taxonomy at runtime.

Taxonomy changes require explicit governance.

⸻

81. Taxonomy Governance

Changes to the canonical taxonomy should be:

* versioned
* reviewed
* documented
* backwards-considered
* provenance-preserving
* testable

A model must not dynamically invent permanent taxonomy members during execution.

⸻

82. Taxonomy as a Control Vocabulary

The taxonomy serves as a controlled vocabulary between architectural components.

For example:

Intent Engine
      ↓
Intent Type = TRANSFER
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Policy
      ↓
Capability Discovery

This common vocabulary reduces semantic drift between components.

⸻

83. Canonical Classification Record

Conceptually:

IntentClassification {
    intent_id
    intent_version
    taxonomy_version
    primary_type
    secondary_types
    dimensions
    provenance
    classification_rules
    status
}

The exact schema belongs to the canonical ontology.

The classification record should remain reconstructible.

⸻

84. Classification Status

Possible classification states include:

UNCLASSIFIED
CANDIDATE
CLASSIFIED
AMBIGUOUS
UNKNOWN
UNSUPPORTED
SUPERSEDED

These states should not be conflated with Intent lifecycle state.

For example:

Intent State:
RESOLVED
Classification:
CLASSIFIED

are related but distinct.

⸻

85. Classification vs Intent State

Intent state answers:

What is happening to this Intent semantically?

Classification answers:

What semantic category does this Intent belong to?

Therefore:

Intent:
RESOLVED
Taxonomy:
TRANSFER

is a valid combination.

⸻

86. Classification vs Trust State

Similarly:

Intent Type:
TRANSFER
Trust:
WAITING_FOR_APPROVAL

is valid.

Taxonomy must never encode Trust state.

⸻

87. Classification vs Graph State

Likewise:

Intent Type:
TRANSFER
Graph:
BLOCKED

is valid.

Graph state remains an execution-structure concern.

⸻

88. Classification and Provenance Reconstruction

Noema should be able to reconstruct:

1. original Actor expression
2. candidate Intent
3. semantic interpretation
4. resolved Intent
5. taxonomy version
6. classification result
7. classification provenance
8. subsequent Intent versions

This supports auditability without requiring retention of private model reasoning.

⸻

89. Taxonomy Security Boundary

The taxonomy must not become an authority-escalation mechanism.

For example:

Intent Type:
TRANSFER

must not imply:

Actor authorized to transfer

Similarly:

Intent Type:
DELETE

must not imply:

Deletion permitted

Classification is semantic information.

Authority remains elsewhere.

⸻

90. Taxonomy and Malicious Input

An Actor or model may attempt to manipulate classification.

For example:

"Just check whether the account is active and then close it."

The taxonomy must reflect the actual semantic structure rather than selecting the less consequential classification to bypass controls.

The Intent Engine and Validation system must preserve all material objectives.

⸻

91. No Taxonomic Downgrading

Noema must not intentionally classify a consequential Intent as informational merely to reduce governance requirements.

For example:

"Check whether I can transfer ₦50,000 and, if I can, execute it."

contains more than an Inquiry.

The consequential component must remain represented.

Semantic classification must reflect the complete Intent.

⸻

92. No Taxonomic Upgrading

Likewise, Noema must not introduce consequential meaning that the Actor did not express.

For example:

"What would happen if I deleted the account?"

is not:

DELETE_ACCOUNT

It is an inquiry about deletion.

The taxonomy must preserve the distinction between discussing an Action and requesting the Action.

⸻

93. Hypothetical Intent

Expressions may discuss hypothetical actions.

Example:

"What would happen if I transferred ₦1M?"

The Intent is informational.

It should not automatically become:

TRANSFER

because the transfer is merely the subject of the inquiry.

The taxonomy must distinguish:

Intent to perform X

from:

Intent to understand X

⸻

94. Advisory Intent

An Actor may ask for advice without requesting execution.

Example:

"Should I move these funds to savings?"

This is an advisory or decision-support objective.

It must not automatically become:

TRANSFER

unless the Actor subsequently establishes the transfer as the desired objective.

⸻

95. Decision vs Execution

The taxonomy should distinguish:

DECIDE

or decision-support semantics from:

EXECUTE

where relevant.

For example:

"Which account should I use?"

is a decision-support request.

"Use account 123."

is a selection instruction.

"Transfer the funds to account 123."

is a consequential Intent.

These distinctions are important for semantic resolution.

⸻

96. Delegated Intent

An Actor may express an Intent concerning another principal or resource.

Example:

"Send the report to my manager."

The recipient is not necessarily the Actor.

The taxonomy must preserve:

Actor
Target
Recipient
Affected Party

as distinct semantic roles where applicable.

⸻

97. Intent Roles

Taxonomic classification may be accompanied by semantic roles such as:

ACTOR
TARGET
SOURCE
DESTINATION
RECIPIENT
BENEFICIARY
AFFECTED_PARTY
RESOURCE
AUTHORITY

These are semantic roles rather than taxonomy members.

They help instantiate the taxonomy against a concrete Intent.

⸻

98. Negated Intent

Natural language may contain negation.

Example:

"Do not send the report."

The semantic objective may be to prevent a previously contemplated communication.

Negation must be represented explicitly.

Noema must not treat:

"Don't transfer the funds."

as equivalent to:

"Transfer the funds."

The canonical ontology should define the representation of negative or prohibitive Intent.

⸻

99. Prohibitive Intent

An Actor may express a prohibition:

"Never send notifications by SMS."

This is semantically distinct from a one-time cancellation.

It may represent a constraint or standing preference.

The taxonomy should preserve whether the expression establishes:

* a one-time objective
* a standing constraint
* a preference
* a prohibition

rather than collapsing them into ordinary Actions.

⸻

100. Preference vs Intent

A preference is not necessarily an Intent.

Example:

"I prefer email."

This may establish a preference.

"Send the report by email."

establishes an actionable objective.

The taxonomy and ontology should distinguish these semantic forms.

Preferences may later constrain Intent resolution without becoming the Intent themselves.

⸻

101. Constraint vs Objective

Constraints limit how an Intent may be fulfilled.

Example:

"Send the report tomorrow by email."

Primary objective:

COMMUNICATE

Constraints:

time = tomorrow
channel = email

The taxonomy should not create separate primary Intent types merely for every constraint.

⸻

102. Canonical Taxonomy Flow

The canonical classification flow is:

Actor Expression
       ↓
AI Interpretation
       ↓
Candidate Intent
       ↓
Intent Construction
       ↓
Semantic Resolution
       ↓
Taxonomic Classification
       ↓
Canonical Intent
       ↓
Validation
       ↓
Trust
       ↓
Action Graph
       ↓
Execution

If classification remains uncertain:

Candidate Intent
       ↓
Ambiguous Classification
       ↓
Clarification
       ↓
Re-resolution

⸻

103. Taxonomy Invariants

Invariant 1

The Intent Taxonomy classifies semantic Intent; it does not define execution.

Invariant 2

Taxonomic classification does not establish authorization.

Invariant 3

Taxonomic classification does not establish Trust.

Invariant 4

Taxonomic classification does not guarantee execution success.

Invariant 5

A model-generated classification is not automatically canonical.

Invariant 6

Material ambiguity must remain explicit until resolved.

Invariant 7

Unknown classification must not silently become a known classification.

Invariant 8

Taxonomy identifiers must be stable and machine-readable.

Invariant 9

Taxonomy members must represent semantic concepts rather than implementation details.

Invariant 10

Actions must not automatically become Intent taxonomy members.

Invariant 11

Intent classification must preserve the Actor’s actual objective.

Invariant 12

Consequential Intent must not be downgraded to informational Intent to bypass governance.

Invariant 13

Informational Intent must not be upgraded into consequential Intent without semantic establishment.

Invariant 14

Composite Intents must preserve component classifications.

Invariant 15

Taxonomy versions must be reconstructible.

Invariant 16

Historical classifications must not be silently rewritten.

Invariant 17

Taxonomy evolution must preserve semantic provenance.

Invariant 18

Domain-specific extensions must preserve the semantics of their parent categories.

Invariant 19

Taxonomy classification and Intent lifecycle state are separate dimensions.

Invariant 20

Taxonomy classification and Trust state are separate dimensions.

Invariant 21

Taxonomy classification and Action Graph state are separate dimensions.

Invariant 22

Taxonomy must never be used as an authority-escalation mechanism.

⸻

104. Canonical Mental Model

The Intent Taxonomy can be reduced to five questions:

1. What is the Actor trying to accomplish?
2. What semantic family does that objective belong to?
3. What target, operation, and semantic dimensions characterize it?
4. Is the classification established or still ambiguous?
5. Which downstream systems need the classification?

This produces:

Actor Expression
      ↓
Intent
      ↓
Semantic Objective
      ↓
Taxonomic Classification
      ↓
Semantic Dimensions
      ↓
Validation / Trust / Action Graph

⸻

105. Canonical Relationship to Noema

The Intent Taxonomy fits into Noema as follows:

                         ACTOR
                           │
                           ▼
                    HUMAN EXPRESSION
                           │
                           ▼
                    INTERPRETATION
                           │
                           ▼
                    INTENT ENGINE
                           │
                           ▼
                    CANONICAL INTENT
                           │
                           ▼
                    INTENT TAXONOMY
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          OBJECTIVE      TARGET      CONSTRAINTS
              │
              ▼
          VALIDATION
              │
              ▼
            TRUST
              │
              ▼
         ACTION GRAPH
              │
              ▼
        ACTION CONTRACT
              │
              ▼
          EXECUTION
              │
              ▼
           OUTCOME

Each layer retains its own authority and responsibility.

⸻

106. Fundamental Boundary

The Intent Taxonomy answers:

What kind of Intent is this?

It does not answer:

Is this Intent valid?

Validation answers that.

It does not answer:

May this Intent proceed?

Trust answers that.

It does not answer:

How will this Intent be fulfilled?

The Action Graph answers that.

It does not answer:

What operation is contractually executable?

Action Contracts answer that.

It does not answer:

What actually happened?

Execution and Outcome answer that.

Therefore:

Taxonomy
    ↓
Semantic Classification
Validation
    ↓
Structural / Semantic Validity
Trust
    ↓
Execution Eligibility
Action Graph
    ↓
Execution Structure
Action Contract
    ↓
Executable Authority Boundary
Execution
    ↓
Actual Operation
Outcome
    ↓
Observed Result

⸻

107. Final Definition

The Intent Taxonomy is Noema’s canonical classification system for the semantic forms, families, dimensions, and characteristics of Actor Intent.

It provides a stable vocabulary for classifying what an Actor intends without conflating semantic classification with validation, authorization, Trust, execution planning, Action Contracts, or execution outcomes.

Its central invariant is:

Noema classifies what the Actor intends without allowing the classification itself to become authority over what Noema may execute.

The canonical boundary is:

Expression
      ↓
Interpretation
      ↓
Intent Engine
      ↓
Canonical Intent
      ↓
Intent Taxonomy
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contract
      ↓
Execution
      ↓
Outcome

The taxonomy therefore provides the semantic classification layer of Intent, while preserving the architectural separation between meaning, validity, authority, execution structure, execution, and observed result.