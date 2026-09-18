Intent

Status: Foundational
Version: 1.0
Domain: Ontology
Canonical Path: ontology/intent.md

⸻

1. Definition

An Intent is the canonical semantic representation of an Actor’s desired objective: what the Actor is trying to accomplish, concerning which targets, with which parameters, under which Actor-expressed constraints, and with which temporal requirements.

Intent answers:

What does the Actor want to accomplish?

Intent is a semantic object, not an implementation instruction, authorization, action, plan, or outcome.

Actor
  │
  │ expresses
  ▼
Intent Expression
  │
  │ resolved
  ▼
Canonical Intent

Example:

Actor:
  Customer
Intent:
  Renew Card
Target:
  card_1234

The expression:

“Please renew my card.”

is an Intent Expression. It becomes a Canonical Intent only after Noema has established the relevant semantics with sufficient resolution.

⸻

2. Semantic Role in Noema

Intent occupies the boundary between an Actor’s expressed objective and Noema’s governed progression toward execution.

Actor / Principal
       │
       ▼
Intent Expression
       │
       ▼
Interpretation
       │
       ▼
Candidate Intent
       │
       ├── Context
       ├── Evidence
       ├── Entity Resolution
       ├── Parameter Resolution
       └── Constraint Identification
       │
       ▼
Canonical Intent
       │
       ▼
Validation
       │
       ▼
State / Context Resolution
       │
       ▼
Trust Decision
       │
       ▼
Action Planning
       │
       ▼
Action Contract
       │
       ▼
Bounded Capability
       │
       ▼
Execution
       │
       ▼
Verification
       │
       ▼
Outcome

The central semantic boundary is:

Intent establishes what the Actor wants. It does not establish what Noema may do.

The Noema POC therefore separates probabilistic interpretation from deterministic governance and execution. The Intent Engine may propose a draft Intent, but that proposal must cross the canonical schema and resolution boundaries before downstream governance can rely upon it.

⸻

3. Intent Expression

An Intent Expression is a representation through which an Actor communicates an objective.

It may be:

* natural language;
* text;
* voice or transcribed speech;
* an API request;
* an event;
* an instruction originating from another system;
* an Agent-produced representation.

Examples:

"Renew my card."
"Why did this transfer fail?"
"Show me what I spent last month."
"Should I send it again?"
"Move ₦500 to savings."

An Intent Expression may be:

* incomplete;
* ambiguous;
* indirect;
* contextual;
* colloquial;
* code-switched;
* contradictory;
* underspecified.

Therefore:

Intent Expression ≠ Canonical Intent

The expression is an input to Intent Resolution.

⸻

4. Intent Is Not Natural Language

Natural language can communicate an objective without uniquely determining its semantics.

Example:

“Fix my card.”

Possible interpretations include:

RenewCard
ReplaceCard
UnblockCard
CancelCard

The expression alone does not establish which objective the Actor intended.

Noema may use permitted Context, Evidence, Entity relationships, prior clarification, explicit constraints, and authoritative enterprise information to resolve the expression.

Where material ambiguity remains, Noema must preserve that ambiguity rather than manufacture certainty.

Ambiguity is a system state, not permission to guess.

⸻

5. Intent Is Not Model Output

The Intent Engine is where probabilistic interpretation may occur.

Its output is a proposal until it passes Noema’s canonical validation and resolution boundaries.

Actor Expression
       │
       ▼
Intent Engine / Model
       │
       ▼
Draft / Candidate Intent
       │
       ▼
Schema Validation
       │
       ▼
Context + Evidence + Entity Resolution
       │
       ▼
Canonical Intent

Therefore:

Model Proposal     ≠ Canonical Intent
Model Confidence   ≠ Intent Resolution
Model Probability  ≠ Semantic Truth

A model selecting one interpretation with the highest probability does not by itself establish canonical meaning where material ambiguity remains.

The model has no direct authority to execute an Intent.

⸻

6. Intent Is Not Action

An Intent represents the desired objective.

An Action is a concrete operation selected to achieve that objective.

Intent:
  Renew Card
Action:
  RenewCard(card_1234)

One Intent may result in one or multiple Actions.

Intent
  │
  ├── Action A
  ├── Action B
  └── Action C

Therefore:

Intent ≠ Action

⸻

7. Intent Is Not Action Plan

Intent establishes what the Actor wants.

An Action Plan establishes how Noema proposes to achieve it.

Example:

Intent:
  Onboard Employee
Action Plan:
  1. Create Employee
  2. Provision Account
  3. Assign Permissions
  4. Send Welcome Message

The plan may change while the underlying Intent remains stable.

Intent ≠ Action Plan

⸻

8. Intent Is Not Capability

A Capability is a registered, bounded ability to perform an Action.

Example:

Intent:
  Renew Card
Capability:
  card.renew

Capability matching answers:

What registered ability could potentially satisfy this objective?

It does not establish:

* that the capability should be selected;
* that it is currently available;
* that the Actor is authorized;
* that the target is correct;
* that Policy permits execution;
* that current business state satisfies the Action Contract;
* that Trust permits progression.

Therefore:

Intent ≠ Capability
Capability ≠ Authority

Noema’s execution boundary is registry-based. Arbitrary HTTP, SQL, or free-form tool instructions are not capabilities.

⸻

9. Intent Is Not Authority

An Actor may express an Intent without possessing the Authority necessary to cause the corresponding Action.

Example:

Actor:
  Employee
Intent:
  Approve ₦100,000 payment
Authority:
  Maximum approval = ₦50,000

The Intent remains a representation of what the Actor requested.

Authority determines whether the relevant Action may proceed.

Therefore:

Intent ≠ Authority
Intent ≠ Permission

Authorization must attach to the fully resolved business Action rather than merely to general capability invocation.

⸻

10. Intent Is Not Trust

A resolved Intent does not automatically become trusted.

Trust concerns whether progression from a resolved Intent toward a specific consequential Action is permissible under the relevant circumstances.

Conceptually:

Canonical Intent
      +
Resolved Target
      +
Current Enterprise State
      +
Evidence
      +
Authority
      +
Policy
      +
Constraints
      +
Action Contract
      +
Risk
      │
      ▼
Trust Decision

The POC Trust Engine is deterministic and performs no model inference.

Trust is therefore a decision boundary, not permanent semantic meaning attached to an Intent.

Resolved Intent ≠ Trusted Execution

⸻

11. Intent Is Not Context

Context is information used to interpret, validate, or execute an Intent.

Example:

Previous:
  "Let's talk about my Pro subscription."
Current:
  "Cancel it."

Conversation Context may establish that “it” refers to the Pro subscription.

But:

Context ≠ Intent

Enterprise Context is likewise not permanently embedded into Intent meaning.

Intent Identity    ≠ Context Snapshot
Intent Persistence ≠ Context Freshness

An Intent may remain unchanged while the enterprise state surrounding its execution changes.

⸻

12. Intent Is Not Evidence

Evidence supports a proposition concerning an Intent or relevant enterprise state.

Examples include:

* Actor statements;
* timestamped enterprise API responses;
* policy rules;
* user confirmations;
* execution results;
* explicitly marked inferences.

Evidence supports resolution, validation, or Trust. It is not the Intent itself.

Evidence → supports resolution / validation / trust
Evidence ≠ Intent

A model assertion alone is not sufficient provenance for a material Trust Decision.

⸻

13. Intent Is Not Entity

An Intent may reference one or more Entities, but the semantic objective and referenced Entity are distinct.

Intent:
  Renew Card
Target:
  card_1234

Therefore:

Intent ≠ Entity

A target reference may initially be unresolved:

"my card"
"the account we discussed"
"it"
"that subscription"

Noema distinguishes:

Target Reference
      ↓
Candidate Entities
      ↓
Entity Resolution
      ↓
Resolved Target

Material target ambiguity must not be silently collapsed into one Entity.

⸻

14. Canonical Intent Object

For the Noema POC, the Intent Object is a strictly typed and versioned object.

The canonical POC shape is:

{
  "intent_id": "int_9f3a2e1c",
  "schema_version": "1.0",
  "created_at": "2026-08-20T09:47:03Z",
  "principal": {
    "user_id": "usr_88213",
    "auth_method": "session_token",
    "session_id": "sess_7a1b",
    "verified": true
  },
  "raw_expression": {
    "modality": "text",
    "language_detected": "en-pidgin-mixed",
    "text": "I sent 20k to Tunde this morning, e never enter."
  },
  "intent_class": "TRANSACTION_EXCEPTION",
  "operation": "INVESTIGATE_AND_RESOLVE",
  "entities": {
    "amount": {
      "value": 20000,
      "currency": "NGN",
      "confidence": 0.97
    },
    "recipient_raw": {
      "value": "Tunde",
      "confidence": 0.99
    },
    "time_reference": {
      "value": "this_morning",
      "resolved_window": [
        "2026-08-20T06:00:00Z",
        "2026-08-20T09:00:00Z"
      ]
    },
    "transaction_reference": null
  },
  "ambiguity_flags": [
    "RECIPIENT_MULTIPLE_MATCH"
  ],
  "desired_outcome": "EXPLAIN_STATUS_AND_RESOLVE",
  "evidence": [
    {
      "type": "user_statement",
      "ref": "raw_expression"
    }
  ],
  "constraints": {
    "action_classes_permitted": [
      "READ",
      "RECOMMEND",
      "CONFIRM",
      "ESCALATE"
    ]
  },
  "policy_requirements": {
    "requires_confirmation_if": [
      "multiple_transaction_candidates",
      "amount_above_confirmation_threshold"
    ]
  },
  "provenance": {
    "produced_by": "intent-engine-v1",
    "model_reference": "intent-model-2026-08"
  },
  "correlation_id": "corr_4c21f9",
  "supersedes": null,
  "status": "DRAFT"
}

The implementation schema is authoritative for serialization.

This ontology defines the semantic meaning and boundaries of the fields.

⸻

15. Intent Object Immutability

Once an Intent Object has crossed a consequential governance boundary, it must not be mutated in place.

A material change creates a new Intent version:

Intent 123
   │
   ├── v1
   │
   ├── v2 supersedes v1
   │
   └── v3 supersedes v2

Amendments are explicit, auditable events.

Never silently overwrite a material Intent.

This preserves:

* provenance;
* lineage;
* decision reproducibility;
* historical reconstruction;
* auditability.

⸻

16. Core Intent Fields

Conceptually:

Intent
├── identity
├── originating principal / actor
├── objective
├── targets / references
├── parameters
├── intent constraints
├── temporal requirements
├── priority
├── provenance
├── schema version
└── lifecycle state

The Noema POC additionally carries machine-relevant fields such as:

* raw expression;
* intent class;
* operation;
* ambiguity flags;
* desired outcome;
* correlation ID;
* supersession reference;
* resolution provenance.

The following remain related but distinct concepts:

Context
Evidence
Policy
Authority
Capability
Trust
Action Contract
Action
Outcome

They are not absorbed into the semantic definition of Intent merely because they participate in its lifecycle.

⸻

17. Principal and Originating Actor

The Principal is the Actor whose objective the Intent represents.

The Actor may be:

* a human;
* an organization;
* a service;
* a system process;
* an Agent acting under explicit delegation.

Authentication establishes identity. It does not by itself establish business Authority for every Action.

Principal
   │
   ▼
Intent

The Principal is not the Intent.

⸻

18. Acting Agent and Delegation

Where an Agent acts on behalf of a Principal, Noema must preserve both identities.

Principal
    │
    │ delegates
    ▼
Acting Agent
    │
    │ expresses
    ▼
Intent

Delegation should preserve, where applicable:

* Principal identity;
* Agent identity;
* delegation scope;
* duration;
* permitted Actions;
* permitted Resources;
* applicable constraints.

The fact that an Agent produced an Intent does not grant the Agent unrestricted Authority.

Agent Capability ≠ Agent Authority
Agent Reasoning  ≠ Principal Authorization

⸻

19. Objective

The Objective is the semantic result the Actor seeks.

Prefer:

Renew Card

over:

POST /cards/123/renew

The former represents domain semantics.

The latter represents implementation.

An Objective should be specific enough for deterministic downstream processing without collapsing into an API invocation.

⸻

20. Targets and Target Resolution

A Target identifies the Entity or Entities to which the Intent applies.

Example:

Intent:
  Renew Card
Target:
  card_1234

Resolution may proceed through:

Reference
   ↓
Candidate Entities
   ↓
Context + Evidence
   ↓
Entity Resolution
   ↓
Resolved Target

If material ambiguity remains:

Target = AMBIGUOUS / UNRESOLVED

Noema must not select an Entity merely because a model assigns it the highest probability.

The POC requires ambiguous candidates to be surfaced using distinguishing, user-verifiable information rather than internal identifiers.

⸻

21. Parameters

Parameters provide information necessary to express or fulfill the Objective.

Example:

Intent:
  Book Flight
Parameters:
  origin      = Lagos
  destination = London
  date        = 2026-09-12
  passengers  = 1

Each parameter has its own semantic and epistemic status.

Parameters may be:

EXPLICIT
INFERRED
RETRIEVED
DEFAULTED
UNRESOLVED
UNKNOWN

One resolved parameter does not imply that all parameters are resolved.

⸻

22. Parameter Provenance and Uncertainty

Noema must preserve the source and epistemic status of material parameters.

Example:

amount:
  source = actor_expression
  status = explicit
destination:
  source = conversation_context
  status = inferred
account:
  source = enterprise_lookup
  status = resolved
recipient:
  status = ambiguous

Unknown must remain distinguishable from inferred.

Prefer:

destination = UNKNOWN

to:

destination = probably_account_123

where the distinction is consequential.

Model confidence may support candidate generation but is not itself canonical semantic certainty.

⸻

23. Intent Constraints

An Intent Constraint is a condition expressed by the Actor as part of the requested objective.

Example:

“Book the cheapest direct flight under ₦800,000.”

Objective:
  Book Flight
Intent Constraints:
  direct = true
  price <= ₦800,000

Intent Constraints must remain distinct from constraints introduced by:

* Policy;
* Authority;
* Action Contracts;
* enterprise rules;
* system requirements.

A Policy must not be represented as though it were an Actor preference.

⸻

24. Constraint Composition

Downstream execution may depend on several constraint sources:

Intent Constraints
        +
Policy Constraints
        +
Authority Constraints
        +
Action Contract Constraints
        +
System Constraints
        ↓
Executable Conditions

The provenance of each material constraint must remain identifiable.

⸻

25. Temporal Requirements

An Intent may contain temporal semantics including:

* start time;
* deadline;
* scheduled time;
* recurrence;
* duration;
* expiration;
* effective time.

Examples:

"Send this tomorrow."
"Cancel my subscription at the end of the month."
"Transfer ₦500 every Friday."

Material temporal ambiguity must be resolved before consequential execution.

Temporal validity of an Intent is distinct from freshness of Context.

⸻

26. Priority

Priority may be represented when explicitly expressed by the Actor or established by domain semantics.

Examples:

urgent
high
normal
low

Priority does not override:

* Authority;
* Policy;
* Action Contract;
* Trust;
* safety conditions.

Example:

Actor:
  "This is urgent. Transfer it now."
Policy:
  Approval required.

Urgency does not remove the approval requirement.

⸻

27. Intent Classes

For the POC, intent_class is a fixed semantic enum and is not an arbitrary model-generated free-form value.

Canonical POC values:

TRANSACTION_EXCEPTION
POLICY_INQUIRY
OUT_OF_SCOPE

Additional domain-specific classes may be introduced only through versioned schema and ontology governance.

The Intent Engine may classify an expression, but downstream systems consume the fixed canonical vocabulary.

⸻

28. Operation and Desired Outcome

The POC separates broad Intent classification from the operation and desired outcome.

Example:

intent_class:
  TRANSACTION_EXCEPTION
operation:
  INVESTIGATE_AND_RESOLVE
desired_outcome:
  EXPLAIN_STATUS_AND_RESOLVE

This allows one class of customer problem to cover manifestations such as:

* locate;
* explain;
* resolve;
* route;
* reconstruct.

These represent manifestations of the transaction-exception resolution problem rather than necessarily independent products or intent systems.

⸻

29. Intent Resolution

Intent Resolution transforms an Intent Expression and permitted supporting information into a Canonical Intent.

Intent Expression
       │
       ▼
Candidate Intent Set
       │
       ├── Context
       ├── Evidence
       ├── Entity Candidates
       ├── Parameter Candidates
       └── Constraints
       │
       ▼
Resolution
       │
  ┌────┴────┐
  ▼         ▼
Canonical   Ambiguous /
Intent      Incomplete
              │
              ▼
          Clarification

Intent Resolution establishes what the Actor means.

It does not authorize execution.

⸻

30. Candidate Intent

A Candidate Intent is a possible semantic interpretation generated during resolution.

Example:

Expression:
  "Fix my card."
Candidates:
  RenewCard
  ReplaceCard
  UnblockCard
  CancelCard

Candidate generation may be probabilistic.

Resolution determines whether a candidate can be accepted as canonical under the available evidence and rules.

Candidate ≠ Canonical Intent

⸻

31. Ambiguity Resolution

Ambiguity is a first-class system state.

The POC resolution flow is:

Candidate Generation
       ↓
Candidate Ranking
       ↓
Threshold Check
       ↓
Clarification / Resolution
       ↓
Clarification Response Binding
       ↓
Contradiction Handling
       ↓
New Intent Version

Candidate ranking may consider:

* recency;
* amount match;
* recipient-name match;
* prior interaction frequency.

Exact ranking thresholds are implementation/configuration decisions, not ontology semantics.

The POC safety rule is:

An unresolved material ambiguity must not yield an ALLOW decision.

Where material ambiguity remains, Noema must:

CLARIFY
or
ESCALATE

Clarification must use distinguishing, user-verifiable information and must not expose internal identifiers or unauthorized information.

⸻

32. Minimal Clarification

Clarification should request the minimum information necessary to resolve material uncertainty.

Poor:

“Please provide your complete account information, address, identity information, and transaction history.”

Better:

“Which account should receive the ₦500?”

The objective is:

Minimum Information
       ↓
Sufficient Resolution

Clarification itself remains subject to Authority and information-disclosure boundaries.

⸻

33. Completeness

An Intent is complete when the information required for its current semantic and downstream purpose has been sufficiently established.

Grammatical completeness is not the criterion.

Example:

"Show my account."

may be complete if exactly one relevant account exists.

But:

"Transfer money."

may be incomplete because material parameters are absent.

Therefore:

Intent Completeness
=
Requirements of the Relevant Downstream Operation

An Intent may be semantically valid while remaining non-executable.

⸻

34. Resolution, Context, and Evidence

Context and Evidence may contribute to resolution without becoming semantic components of the objective.

Example:

User:
  "Show my transactions."
Noema:
  "Which account?"
User:
  "My current account."

The second expression depends on conversation Context.

But:

Conversation Context ≠ Enterprise Truth

Likewise:

User:
  "My card ending in 1234 is expired. Renew it."

The statement is an Actor expression and may constitute Evidence for interpretation. It does not automatically become authoritative enterprise state.

Authoritative enterprise systems remain the source of truth for enterprise facts.

⸻

35. Multi-Source Grounding

For consequential interpretation, Intent Resolution should be grounded against permitted sources rather than relying solely on the expression or model inference.

Conceptually:

Expression
    +
Conversation Context
    +
Enterprise Context
    +
Evidence
    +
Entity Relationships
    +
Resolved Parameters
    +
Constraints
        ↓
Candidate Intents
        ↓
Canonical Intent

The purpose of grounding is not to place every retrieved fact into the Intent.

Its purpose is to establish the minimum semantic information required to resolve the Actor’s objective correctly while preserving provenance for material decisions.

External systems and retrieved content remain untrusted inputs.

Retrieved Information
       ↓
Evidence to Evaluate
       ≠
Instruction to Execute

⸻

36. Intent Determinism

Once the relevant canonical inputs have been established, material Intent resolution should become deterministic.

Established Expression
+
Established Context
+
Established Entity Resolution
+
Established Parameters
+
Established Constraints
        ↓
Canonical Intent

Probabilistic models may participate in:

* interpretation;
* candidate generation;
* candidate ranking.

They must not silently become the final authority where material ambiguity remains.

⸻

37. Intent Lifecycle

Intent has both semantic identity and lifecycle state.

A conceptual lifecycle is:

RECEIVED
   ↓
INTERPRETING
   ↓
DRAFT / CANDIDATE
   ↓
PARTIALLY_RESOLVED
   ↓
CLARIFICATION_REQUIRED
   ↓
RESOLVED
   ↓
VALIDATED
   ↓
READY_FOR_PLANNING
   ↓
PLANNED
   ↓
TRUST_EVALUATION
   ↓
ACTION_AUTHORIZED
   ↓
EXECUTING
   ↓
COMPLETED

Possible terminal or exceptional states include:

REJECTED
FAILED
CANCELLED
SUPERSEDED
EXPIRED
ESCALATED

The authoritative lifecycle state machine belongs to the lifecycle specification.

⸻

38. Intent State Is Not Intent

Intent and Intent State are distinct.

Intent:
  Renew card_1234
State:
  RESOLVED

The Intent represents the semantic objective.

The State represents the Intent’s position in the Noema lifecycle.

Intent ≠ Intent State

⸻

39. Resolved Intent

A Resolved Intent is an Intent for which the material semantic interpretation has been established sufficiently for deterministic downstream processing.

Resolution may establish:

* objective;
* target;
* required parameters;
* material constraints;
* temporal requirements.

A Resolved Intent is not necessarily:

* validated;
* authorized;
* trusted;
* executable.

⸻

40. Validated Intent

A Validated Intent has passed applicable structural and semantic validation.

Validation may establish:

* valid canonical objective;
* valid schema;
* resolved required references;
* required parameters;
* semantically valid values;
* internally consistent constraints;
* valid temporal requirements.

Validation does not establish Authority or Trust.

⸻

41. Execution-Ready Intent

An Intent is execution-ready only when the requirements necessary to construct a valid downstream Action have been established.

Conceptually:

Resolved Intent
      +
Resolved Target
      +
Required Parameters
      +
Relevant Context
      +
Applicable Constraints
      +
Required Capability
      +
Action Contract Requirements
      ↓
Execution-Ready

Execution readiness is not equivalent to authorization.

⸻

42. Trust Decision Outcomes

Trust is represented separately from Intent.

The POC defines a fixed TrustDecision vocabulary:

ALLOW
CLARIFY
CONFIRM
WAIT
ESCALATE
REJECT
UNKNOWN

These are decision outcomes, not Intent states.

Examples:

Material ambiguity
  → CLARIFY
Insufficient authority
  → REJECT
External state not yet settled
  → WAIT
Material uncertainty that cannot safely be resolved
  → UNKNOWN / ESCALATE

An unresolved material ambiguity must not be represented as ALLOW.

⸻

43. Authorization Boundary

Noema distinguishes three authorization layers:

Layer	Question
Technical authorization	Can this Principal invoke this Capability at all?
Policy authorization	Does this parameterization satisfy a static Policy rule?
Business authorization	Given the fully resolved business object and current state, should this specific outcome be permitted now?

The critical Noema boundary is:

Authorization must attach to:
Actor
+
Action
+
Resolved Target
+
Relevant State

It must not attach merely to:

Actor + Tool

A technically authorized call against the wrong resolved Entity constitutes a confused-deputy risk.

⸻

44. Intent and Bounded Autonomy

Noema distinguishes:

Principal Objective
        ≠
Agent-Selected Means

An Agent may select intermediate Actions or Derived Intents within an explicit delegation boundary.

However:

Agent Reasoning   ≠ Principal Authorization
Agent Capability  ≠ Agent Authority

The Agent must not expand delegated scope through its own reasoning.

⸻

45. Derived Intent

A Derived Intent is a new semantic objective generated while attempting to satisfy an originating Intent.

Example:

Principal Intent:
  Keep inventory above 100 units.
Agent reasoning:
  ↓
Derived Intent:
  Order 50 units from Supplier A.

The Derived Intent is not identical to the Principal Intent.

Principal Intent
       ↓
Reasoning / Planning
       ↓
Derived Intent

The Derived Intent remains subject to:

* delegation;
* Authority;
* Policy;
* Capability;
* Constraints;
* Action Contract;
* Trust.

A Derived Intent must not silently redefine the Principal’s objective.

⸻

46. Compound and Composite Intent

One expression may contain multiple objectives.

Example:

“Cancel my old subscription and move me to Pro.”

This may resolve into:

Composite Intent
├── Cancel Subscription
└── Upgrade Subscription

Each component retains:

* identity;
* objective;
* targets;
* dependencies;
* constraints;
* provenance;
* originating Principal.

Where ordering or dependency matters, it must be explicit.

⸻

47. Intent Decomposition

One high-level Intent may produce multiple Actions.

Example:

Intent:
  Onboard Employee
Action Plan:
  Create Employee
      ↓
  Create Account
      ↓
  Assign Permissions
      ↓
  Send Welcome Message

The Actor expressed one objective.

Noema may decompose it into multiple consequential operations.

Each Action retains lineage to the originating Intent and is governed by its own Action Contract and Trust requirements.

⸻

48. Intent Revision

A material change creates a new Intent version.

Example:

v1:
  Transfer ₦500
v2:
  Transfer ₦700
v3:
  Transfer ₦700 to Account B

Material revisions require:

* lineage;
* explicit amendment;
* revalidation;
* re-evaluation of downstream decisions where required.

An Intent must never be silently mutated after crossing a consequential decision boundary.

⸻

49. Supersession

A newer Intent may supersede an earlier Intent.

Example:

Intent A:
  Transfer ₦500.
Intent B:
  Actually, transfer ₦700 instead.

Intent B may supersede Intent A.

Noema must not execute both merely because both were previously resolved.

SUPERSEDED ≠ CANCELLED

⸻

50. Cancellation

Intent cancellation is the withdrawal of an Intent before or independently of Action cancellation.

Example:

“Never mind. Cancel that.”

This is distinct from cancelling an Action that is already executing.

Intent Cancellation ≠ Action Cancellation

The semantics of Action cancellation depend on the relevant Action Contract and external system.

⸻

51. Expiration and Temporal Validity

An Intent may become temporally invalid.

Examples:

"Book the flight for tomorrow."

after the relevant booking window has passed.

or:

"Cancel this offer before Friday."

after the deadline.

Expiration is distinct from:

* cancellation;
* supersession.

Intent temporal validity must not be confused with Context freshness.

⸻

52. Recurring Intent

A Recurring Intent expresses a repeated objective.

Example:

"Transfer ₦500 to my savings account every Friday."

Conceptually:

Objective:
  Transfer Money
Parameters:
  amount = ₦500
  destination = savings account
Temporal Requirement:
  recurrence = weekly
  day = Friday

Recurring Intent requires explicit semantics for:

* recurrence;
* expiration;
* modification;
* cancellation;
* each resulting execution;
* per-execution Trust and Action requirements.

A recurring Intent is not unlimited Authority.

⸻

53. Conditional Intent

A Conditional Intent specifies a condition under which an objective should be pursued.

Example:

"If my balance drops below ₦1,000, transfer ₦500."

Conceptually:

Trigger Condition:
  balance < ₦1,000
Objective:
  Transfer ₦500

The condition and objective are distinct:

Condition ≠ Objective

The condition does not itself authorize execution.

⸻

54. Intent and Transaction-Exception Resolution

The initial Noema commercial and POC wedge is transaction exception resolution:

Failed, delayed, ambiguous, stuck, or disputed financial transactions where the enterprise already possesses the underlying information across multiple systems, but no single system converts that information into a trustworthy answer without human cross-referencing.

The canonical customer question is:

“Where is my money?”

Representative expressions include:

"I sent ₦20,000 yesterday and they haven't received it."
"Wetin happen to the 20k wey I send this morning?"
"I sent ₦50k to Tunde but he hasn't received it."
"The money left my account but the person hasn't gotten it."
"Why did this transfer fail?"
"Should I try again?"
"Has the money been reversed?"

These are not merely conversational queries. They require Noema to reconstruct enterprise state and establish a trustworthy resolution.

The five manifestations are:

Moment	Customer problem	Capability demonstrated
LOCATE	“I don’t know where my money is.”	State reconstruction across conflicting systems
EXPLAIN	“I don’t know why this failed.”	Correct diagnosis
RESOLVE	“I don’t know how to fix this.”	Governed next-action recommendation
ROUTE	“I don’t know who needs to act.”	Correct case ownership
RECONSTRUCT	“I don’t know what happened.”	Evidence-backed timeline reconstruction

These are manifestations of one resolution problem, not necessarily five separate products.

⸻

55. Intent in the POC Scope

The POC is deliberately read/diagnosis-first.

Allowed writes are governed, non-monetary operations such as:

* structured internal escalation tickets;
* compliant complaint-reference logging;
* routing to the correct internal owner or queue;
* non-monetary case-state updates;
* investigation evidence recording.

The POC prohibits:

* transfers;
* refunds;
* reversals;
* balance adjustments;
* payment instructions;
* financial movement of any kind.

This is an architectural capability boundary, not merely a prompt instruction.

Therefore an Intent such as:

"Send ₦20,000 to Tunde."

may be semantically representable as an Actor request, but the POC does not thereby acquire the Capability or Authority to execute it.

⸻

56. Worked Intent Fixtures

These fixtures define important semantic and safety behavior.

A — Unique, unambiguous status request

"Check my transfer of ₦15,000 to my landlord yesterday."

One matching transaction exists.

Resolution:

LOCATE → EXPLAIN

The corresponding Trust outcome may be:

ALLOW

because the material transaction reference is unambiguous and the operation is within the POC’s governed read/diagnostic scope.

⸻

B — Ambiguous recipient

"The ₦20k I sent to Tunde."

Two candidate transactions involve different Tundes, with the same amount and close timestamps.

Resolution:

CLARIFY

Candidates must be distinguished using user-verifiable information such as time or account tail, never internal identifiers.

⸻

C — Missing reference

"That money I sent yesterday didn't enter."

No amount, recipient, or transaction reference is provided.

Candidate generation may return prior-day transactions.

If the candidate set remains above the configured threshold, Noema escalates rather than force an unreliable guess.

⸻

D — Dangerous retry follow-up

"Should I send it again?"

Noema must resolve current transaction state before answering.

A prior failure-like signal does not establish that a duplicate transaction is safe.

⸻

E — Authorization boundary

A user requests investigation into an account for which they are not a verified party.

The appropriate result is rejection at the identity/Authority boundary before Entity matching can expose protected transaction information.

⸻

57. Code-Switched and Local-Language Expressions

Intent Resolution must preserve semantic meaning across the language and register in which the Actor naturally communicates.

The POC includes Nigerian code-switched and local-language expressions as testable inputs.

Examples:

"E never enter"
  → desired outcome / credit-not-confirmed hypothesis
"Sharp-sharp"
  → urgency modifier, not a financial instruction
"Abeg check am"
  → investigate / resolve imperative
"Ó ti jáde ní ẹgbẹrún méjìlélógún"
  → amount extraction
"Kudin ya fita amma bai isa ba"
  → money-left-but-not-arrived state hypothesis

System codes must likewise be mapped semantically rather than interpreted as natural-language instructions.

Example:

09 — Pending
  → SETTLEMENT_PENDING
96 — System Malfunction
  → EXECUTION_OUTCOME_UNKNOWN
  → verify before retry

For the POC, deterministic lexicon/configuration provides a testable coverage layer around the Intent Engine.

A specialist intent model is a later capability, not a prerequisite for the semantic boundary.

⸻

58. Intent and Enterprise State

Intent establishes what the Actor wants.

Enterprise State establishes what is true in authoritative systems.

They are coupled during resolution and execution but remain distinct objects.

Intent:
  Transfer ₦500
Context at T1:
  balance = ₦1,000
Context at T2:
  balance = ₦400

The Intent may remain unchanged while enterprise state changes.

Noema therefore distinguishes:

Intent
State Snapshot
Context Freshness

Enterprise systems remain authoritative for enterprise state.

Noema reconstructs state; it does not create a shadow source of truth through inference.

⸻

59. Intent and State Reconstruction

For the transaction-exception wedge, Intent Resolution identifies the business object to investigate.

State Reconstruction then gathers evidence from relevant enterprise systems.

Conceptually:

Canonical Intent
       ↓
Resolve User
       ↓
Identify Account
       ↓
Generate Transaction Candidates
       ↓
Resolve Ambiguity
       ↓
Query Relevant Systems
       ↓
Reconcile State
       ↓
Trust Decision

Every reconstructed fact should retain an explicit epistemic state such as:

KNOWN
INFERRED
AMBIGUOUS
UNAVAILABLE
STALE
CONTRADICTORY
UNKNOWN
UNAUTHORIZED

A weak or conflicting enterprise signal must not be silently converted into false certainty.

⸻

60. Intent and Unknown

Unknown is a valid first-class state.

Examples:

target = UNKNOWN
amount = UNKNOWN
destination = UNRESOLVED
transaction_state = UNKNOWN

Noema should not convert uncertainty into an optimistic guess merely to produce a smoother user experience.

Depending on its source and nature, material uncertainty may result in:

CLARIFY
WAIT
ESCALATE
REJECT
UNKNOWN

⸻

61. Intent and Policy

Policy governs the conditions under which an Intent may be fulfilled.

Example:

Intent:
  Refund Customer
Policy:
  Refunds above ₦10,000,000 require manager approval.

Policy does not alter the Actor’s objective.

It changes the conditions under which the objective may proceed.

For the POC, Policy evaluation is deterministic and versioned.

A Trust Decision records the Policy version governing the decision.

⸻

62. Intent and Action Contracts

An Action Contract specifies the requirements and guarantees of a concrete Action.

Intent
   ↓
Action Selection
   ↓
Action Contract
   ├── Inputs
   ├── Preconditions
   ├── Constraints
   ├── Authorization
   ├── Side Effects
   ├── Failure Conditions
   └── Expected Outcome

Intent must not be treated as an implementation-level Action Contract.

The Action Contract becomes relevant when Noema moves from semantic objective toward a specific operation.

⸻

63. Intent and Outcome

Intent represents the desired objective.

Outcome represents what actually happened.

Intent:
  Refund Payment
Observed Outcome:
  Refund rejected because payment was already settled.

Therefore:

Intent ≠ Outcome

Technical API success is not equivalent to semantic Intent satisfaction.

Example:

Intent:
  Transfer ₦500 to Account B.
API:
  HTTP 200.
Observed Outcome:
  ₦500 went to Account C.

The Intent was not satisfied.

⸻

64. Intent Satisfaction

Intent Satisfaction evaluates whether observed reality fulfills the semantic objective.

Intent
   ↓
Action
   ↓
Execution
   ↓
Observed Outcome
   ↓
Verification
   ↓
Satisfaction Evaluation
   ├── SATISFIED
   └── UNSATISFIED

For compound Intents, satisfaction may be partial.

Example:

Intent:
  Cancel old subscription and create Pro subscription.
Outcome:
  Cancel succeeded.
  Pro creation failed.

This is not a simple overall SUCCESS.

Component outcomes and dependencies must remain visible.

⸻

65. Intent and Execution Failure

Failure must remain classified by layer.

Interpretation Failure
  → No sufficiently reliable Intent
Resolution Failure
  → Material ambiguity cannot be resolved
Validation Failure
  → Semantic/schema requirements invalid
Trust Failure
  → Noema does not permit progression
Execution Failure
  → Action cannot be completed
Outcome Failure
  → Action occurred but did not satisfy Intent

These failure classes are not interchangeable.

⸻

66. Intent and Recovery

An execution failure does not necessarily mean that the Intent permanently failed.

Example:

Intent:
  Transfer ₦500
Execution:
  Timeout

A timeout does not establish whether the external system accepted the Action.

Noema must distinguish:

EXECUTION_OUTCOME_UNKNOWN

from:

FAILED

Recovery may require:

Fresh State Verification
       ↓
Reconciliation
       ↓
Determine Outcome
       ↓
Continue / Retry / Escalate

Retries must never be blind.

⸻

67. Intent Identity and Idempotency Lineage

Intent identity contributes to causal lineage but does not replace Action or Execution identity.

intent_id
    ↓
action_id
    ↓
execution_attempt_id
    ↓
audit_event_id

A single Intent may result in multiple execution attempts.

Idempotency belongs primarily to Action and Execution semantics.

Intent provides higher-level causal lineage.

⸻

68. Intent and Audit / Provenance

Intent provenance must allow Noema to reconstruct how the Canonical Intent was established.

Material provenance may include:

* originating Actor;
* raw expression;
* modality;
* detected language/register;
* model proposal;
* Context references;
* Entity Resolution;
* parameter sources;
* Evidence references;
* clarification responses;
* validation result;
* schema version;
* timestamp;
* Intent revision;
* supersession lineage.

Noema does not require hidden model chain-of-thought for semantic auditability.

The relevant questions are:

What was intended?

What was ambiguous?

How was the ambiguity resolved?

What evidence supported the resolution?

What downstream decision depended upon it?

⸻

69. Historical Intent Reconstruction

Historical Intent must remain distinguishable from Current Intent.

Likewise:

Historical Context ≠ Current Context
Historical Evidence ≠ Current Evidence

A historical reconstruction should use the information available at the relevant time.

Historical Expression
       +
Historical Context References
       +
Historical Evidence
       +
Historical Resolution
       ↓
Historical Canonical Intent

Present state must not silently rewrite historical semantic meaning.

⸻

70. Intent Security

Intent representations may contain sensitive information.

Noema should minimize unnecessary exposure of:

* financial information;
* personal information;
* credentials;
* private relationships;
* sensitive targets;
* unnecessary parameters.

Intent Objects remain subject to:

* principal-scoped access;
* tenant isolation;
* data minimization;
* redaction;
* appropriate retention;
* enterprise security policy.

Credentials do not belong in model context.

User-provided, model-generated, and retrieved content must be treated as untrusted inputs.

⸻

71. Intent and Prompt Injection

Enterprise text and retrieved content may contain instructions that are malicious, irrelevant, or unrelated to the Actor’s objective.

Therefore:

Retrieved Content
    ≠
Instruction

Tool responses are evidence, not commands.

The Intent Engine must not allow retrieved content to silently redefine the Actor’s Intent.

The consequence boundary must hold even when model interpretation is manipulated.

⸻

72. Intent Reuse

An Intent should not automatically be reused for a new consequential execution when material conditions have changed.

Relevant changes include:

* target;
* amount;
* Authority;
* Policy;
* Capability;
* enterprise state;
* risk;
* freshness;
* temporal validity;
* material constraints.

A material change requires appropriate re-evaluation and, where applicable, a new Intent version.

⸻

73. Intent and Multiple Actions / Outcomes

One Intent may result in multiple Actions:

Intent
 ├── Action A
 ├── Action B
 └── Action C

and multiple Outcomes:

Action A → Outcome A
Action B → Outcome B
Action C → Outcome C

Each Action must retain lineage to the originating Intent.

Composite satisfaction must evaluate the relevant collection of Outcomes rather than merely whether an API returned success.

⸻

74. Intent and Minimal Visibility

Noema should know enough to resolve and govern the requested objective, but no more than necessary.

This supports:

* privacy;
* least privilege;
* reduced attack surface;
* controlled data access.

Intent Resolution should distinguish between:

Information necessary for resolution

and:

Information merely available

Availability of enterprise data is not itself justification for exposing or persisting it.

⸻

75. Intent and Operational Memory

Operational Memory is not the Intent itself.

For the POC, Operational Memory is a minimal structured record of cases, evidence, decisions, and outcomes sufficient to answer:

* what happened;
* why;
* what was known at the time;
* what was authorized;
* what happened after execution;
* what should happen next.

It is not a general-purpose AI memory system and does not replace Intent provenance.

⸻

76. Canonical Intent-to-Execution Model

ACTOR / PRINCIPAL
       │
       ▼
INTENT EXPRESSION
       │
       ▼
MODEL / INTERPRETATION
       │
       ▼
CANDIDATE INTENT
       │
       ├── Context
       ├── Evidence
       ├── Entity Candidates
       ├── Parameter Candidates
       └── Constraints
       │
       ▼
SCHEMA VALIDATION GATE
       │
       ▼
INTENT RESOLUTION
       │
       ├── Canonical Intent
       └── Clarification / Escalation
       │
       ▼
STATE / CONTEXT RECONSTRUCTION
       │
       ▼
VALIDATION
       │
       ▼
TRUST DECISION
       │
   ┌───┼────────────────┐
   ▼   ▼                ▼
CLARIFY WAIT/UNKNOWN   PROCEED
                         │
                         ▼
                  ACTION PLANNING
                         │
                         ▼
                   ACTION CONTRACT
                         │
                         ▼
                     CAPABILITY
                         │
                         ▼
                     EXECUTION
                         │
                         ▼
                    VERIFICATION
                         │
                         ▼
                      OUTCOME
                         │
                         ▼
                   SATISFACTION

⸻

77. Agentic Intent Model

For bounded autonomy:

PRINCIPAL INTENT
       │
       ▼
AGENT REASONING
       │
       ▼
DERIVED INTENT / ACTION PLAN
       │
       ├── Delegation
       ├── Authority
       ├── Policy
       ├── Capability
       ├── Constraints
       └── Action Contract
              │
              ▼
         TRUST DECISION
              │
              ▼
           EXECUTION

The Principal Intent remains the semantic anchor.

The Agent may select means only within the delegated boundary.

The Agent cannot promote its own inference into unrestricted Principal authorization.

⸻

78. Intent and Noema Architecture

The POC establishes a hard process boundary:

INPUT
  ↓
INTENT ENGINE
  ↓
SCHEMA VALIDATION GATE
  ↓
CONTEXT / ENTITY RESOLUTION
  ↓
STATE RECONSTRUCTION
  ↓
DETERMINISTIC TRUST ENGINE
  ↓
ACTION GRAPH / PLANNER
  ↓
EXECUTION CONTROLLER
  ↓
VERIFICATION
  ↓
EXPLANATION
  ↓
AUDIT / PROVENANCE

Every consequential boundary is serialized, logged, and versioned.

The model cannot:

* directly execute an Intent;
* authorize itself;
* select an open-ended tool;
* construct an arbitrary call;
* judge its own Trust.

⸻

79. Intent and Read Operations

Read operations still require semantic resolution.

Example:

"Show my transactions from August."

Potential requirements include:

Principal
Account
Date Range
Transaction Scope
Authorization

Read-only does not mean semantically trivial.

For the POC, read-only diagnostic depth may include:

* cross-system investigation;
* state reconciliation;
* Policy evaluation;
* SLA computation;
* Evidence collection;
* explanation.

⸻

80. Intent and Higher-Risk Operations

A future write such as:

"Transfer ₦9,000 to John."

may require resolution of:

Principal
Source Account
Recipient
Destination
Amount
Currency
Temporal Requirements
Actor Constraints

Downstream Trust may additionally require:

Authority
Fresh Business State
Policy
Risk
Confirmation
Capability
Action Contract
Execution Preconditions
Outcome Verification

These execution-specific requirements must not be embedded into the semantic definition of the Intent primitive.

⸻

81. Intent Invariants

The following are canonical Noema invariants.

Semantic invariants

1. An Intent represents an Actor’s desired objective.
2. Intent Expression is not necessarily Canonical Intent.
3. Model output is a proposal, not automatic canonical meaning.
4. Intent and Action are distinct.
5. Intent and Action Plan are distinct.
6. Intent and Capability are distinct.
7. Intent does not imply Authority.
8. Intent does not imply Trust.
9. Intent does not imply execution.
10. Intent does not imply Outcome.
11. Intent is semantic, not an API call or implementation command.
12. Intent may be semantically valid without being executable.

Resolution invariants

13. Material ambiguity must never be silently guessed.
14. Material unresolved parameters prevent execution readiness.
15. Material target references must be sufficiently resolved before consequential execution.
16. Context used for resolution remains distinguishable from Intent.
17. Evidence supporting resolution remains distinguishable from Intent.
18. Actor-provided information does not automatically become authoritative enterprise state.
19. Conversation history may support resolution but cannot override authoritative enterprise state.
20. Model probability cannot silently establish material canonical meaning.
21. Once canonical inputs are established, material semantic resolution should be deterministic.
22. Unknown must remain explicitly unknown until established.
23. Clarification should request the minimum information necessary.

Governance invariants

24. Intent Constraints remain distinct from Policy, Authority, and Action Contract constraints.
25. A resolved Intent is not necessarily validated.
26. A validated Intent is not necessarily authorized.
27. Execution readiness does not itself establish Trust.
28. Trust is a decision about progression, not permanent semantic meaning.
29. Authority is specific to Actor, Action, Target, and relevant state.
30. Capability is not permission.
31. Agent Capability does not establish Agent Authority.
32. Agent reasoning does not expand delegated Authority.
33. Derived Intent must remain bounded by delegation and downstream governance.

Lifecycle invariants

34. Intent State is distinct from Intent.
35. Material Intent changes create new versions after consequential admission.
36. Intent revision preserves lineage.
37. Supersession is distinct from cancellation.
38. Intent cancellation is distinct from Action cancellation.
39. Material revisions require appropriate revalidation.
40. Superseded Intents must not execute as though still current.
41. Historical Intent must remain distinguishable from Current Intent.
42. Intent identity remains distinct from Actor, Entity, Action, and Execution identity.

Execution and outcome invariants

43. Technical execution success does not establish Intent satisfaction.
44. Expected Outcome is distinct from Observed Outcome.
45. Intent may produce multiple Actions and multiple Outcomes.
46. Compound Intent dependencies must remain explicit.
47. A timeout does not establish execution failure; fresh verification is required.
48. Recovery must not blindly resend a potentially successful consequential operation.
49. Each consequential Action remains governed by its own Action Contract.
50. Intent lineage must survive decomposition into Actions and execution attempts.

Security and audit invariants

51. External systems and model outputs are untrusted inputs.
52. Retrieved enterprise content is Evidence, not instruction.
53. Credentials do not belong in model context.
54. Arbitrary HTTP and arbitrary SQL are not Capabilities.
55. Enterprise systems remain authoritative for enterprise state.
56. Material Intent Resolution must be reconstructable from explicit provenance.
57. Hidden model chain-of-thought is not required for auditability.
58. Sensitive Intent data is subject to least-privilege access and data minimization.
59. Every consequential Outcome must be causally reconstructable.
60. Every failure relevant to a material decision must be reproducible.

⸻

82. Canonical Semantic Distinctions

Noema must preserve the following distinctions:

Intent Expression
        ≠
Intent
Model Proposal
        ≠
Canonical Intent
Intent
        ≠
Action
Intent
        ≠
Action Plan
Intent
        ≠
Capability
Intent
        ≠
Authority
Intent
        ≠
Trust
Intent
        ≠
Outcome
Intent
        ≠
Context
Intent
        ≠
Evidence
Intent
        ≠
Entity
Intent
        ≠
Policy
Intent
        ≠
Constraint
Principal Intent
        ≠
Derived Intent
Intent State
        ≠
Intent
Intent Cancellation
        ≠
Action Cancellation
Intent Supersession
        ≠
Intent Cancellation
Intent Identity
        ≠
Actor Identity
        ≠
Entity Identity
        ≠
Action Identity
        ≠
Execution Identity

⸻

83. Canonical Semantic Summary

An Intent is a structured semantic representation of an Actor’s desired objective.

It establishes:

WHO
  ↓
Principal / Actor
WANTS WHAT
  ↓
Objective
CONCERNING WHAT
  ↓
Targets / Entity References
WITH WHICH PARAMETERS
  ↓
Parameters
UNDER WHICH ACTOR-EXPRESSED CONDITIONS
  ↓
Intent Constraints
WHEN
  ↓
Temporal Requirements

Intent Resolution may use:

Context
Evidence
Entity Resolution
Parameter Resolution
Conversation
Relationships
Enterprise State

to establish the Canonical Intent.

Those supporting sources do not thereby become the Intent.

The resulting architectural boundary is:

Actor Expression
       ↓
What does the Actor mean?
       ↓
Canonical Intent
       ↓
What is true now?
       ↓
Context / State / Evidence
       ↓
What may Noema do?
       ↓
Authority / Policy / Trust
       ↓
How should it be done?
       ↓
Action Plan / Action Contract / Capability
       ↓
What actually happened?
       ↓
Execution / Verification / Outcome
       ↓
Was the objective satisfied?
       ↓
Intent Satisfaction

For bounded agentic execution:

Principal Intent
       ↓
Agent Reasoning
       ↓
Derived Intent / Action Plan
       ↓
Delegation + Authority + Policy
       + Capability + Action Contract
       ↓
Trust
       ↓
Execution

The Principal Intent remains the semantic anchor. Agent reasoning may determine means within the delegated boundary but cannot expand the Principal’s authorization.

The governing principle is:

Intent establishes what the Actor wants. It does not establish what Noema may do.

The critical architectural boundary is:

The model may propose what the Actor probably means; Noema must establish the Canonical Intent before consequential behavior can be governed or authorized.