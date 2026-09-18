Context

Status: Reference Workflow
Version: 0.2
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/context.md

⸻

1. Definition

Context is the typed, execution-scoped set of information available to Noema at a particular point in an execution journey for understanding, resolving, authorizing, planning, executing, verifying, recovering, and explaining an Intent.

Context provides the information required to determine:

* who is asking
* which Principal is represented
* what the Principal intends
* which Resources are relevant
* which enterprise state has been observed
* what Evidence supports those observations
* what information is derived or model-generated
* what authority and Policy apply
* what Trust conditions exist
* what Action requirements remain
* what has already happened in the execution journey

Context is not itself:

* Intent
* Truth
* Business State
* Evidence
* Trust
* Policy
* Action
* Outcome

Context is the execution information envelope. It carries facts, references, candidates, evidence, state, and constraints while preserving their classifications, provenance, authority, freshness, and scope.

Conceptually:

Principal
   │
   ▼
Intent
   │
   ▼
Context Assembly
   │
   ├── Identity
   ├── Resources
   ├── Enterprise State
   ├── Evidence
   ├── Derived Data
   ├── User Input
   ├── Model Candidates
   ├── Permissions
   ├── Policy
   ├── Temporal State
   └── Execution State
           │
           ▼
      Trust + Action

⸻

2. Purpose

The purpose of Context is to give Noema enough grounded information to safely execute the resolved Intent without granting the system unrestricted access to enterprise information.

Context should answer:

What does Noema need to know, at this point in the execution, to make the next permitted decision?

The answer should be:

minimum sufficient context

rather than:

maximum available customer data

Context therefore acts as both an execution resource and a security boundary.

⸻

3. Core Principle

Context is execution-scoped, Action-aware, typed, and provenance-preserving.

A Customer Account Inquiry should receive only the information required for its current Intent, Policy, and Action path.

For example:

Intent:
"What is my account balance?"
Required Context may include:
    principal_id
    account_reference
    authorization_context
    required_freshness

It does not automatically require:

full transaction history
home address
employment information
unrelated accounts
complete customer profile

The governing principle is:

Context must be sufficient for the current execution step, but no broader than necessary.

⸻

4. Context Is Not Truth

Context may contain information from multiple semantic classes:

Context
├── Canonical Data
├── Evidence
├── Derived Data
├── User Input
├── Model Interpretation
├── Model Candidate
├── Historical Data
├── Policy
├── Permissions
└── Noema Execution State

These categories do not have equal authority.

Context does not upgrade the authority of the information it contains.

Therefore:

Context ≠ Truth
Context ≠ Authority
Context ≠ Evidence

A value remains subject to its own semantic classification while inside Context.

⸻

5. Context and Canonical Data

Canonical Data represents authoritative enterprise information within a defined authority boundary.

Context may carry Canonical Data or a reference to it.

Example:

Context
   │
   └── account.balance
          │
          ├── source = Ledger
          ├── authority = canonical
          └── observed_at = timestamp

Context carries the observation.

The enterprise System of Record establishes its authority.

Noema must not create canonical authority merely by storing or transmitting a value.

⸻

6. Context and Evidence

Evidence is information that supports a proposition, state classification, authorization decision, execution decision, or verification result.

Context may contain Evidence references or evidence records.

Example:

Ledger
   ↓
observed account balance
   ↓
Evidence
   ↓
Context

Evidence must preserve sufficient provenance to establish:

* source
* observation time
* Resource
* relevant version
* authority
* result or observation

Therefore:

Context contains Evidence

does not mean:

Context becomes Evidence

⸻

7. Context and Intent

Intent describes what the Principal wants to accomplish.

Context supplies information required to resolve and execute that Intent.

Example:

Intent:
"How much do I have?"
Context:
    principal_id = ...
    account_id = ...
    currency = NGN
    authentication_state = AUTHENTICATED

Together:

Intent + Context
       ↓
Resolution
       ↓
Trust / Policy
       ↓
Action

Context does not replace Intent and must not silently rewrite it.

⸻

8. Context and Principal

The Principal is the identity under whose authority the request is being evaluated.

Context may contain:

principal_id
actor_id
authentication_state
session_id
tenant
organization
delegation_reference

where required.

The Principal must be grounded against enterprise identity information when consequential access is involved.

An authenticated identity is not automatically an authorized identity for every Resource or Action.

⸻

9. Context and Identity Resolution

Natural-language requests frequently contain identity references that require resolution.

Example:

“Show my account balance.”

The phrase my account must resolve to an authorized enterprise Resource.

Conceptually:

Actor
   ↓
Principal
   ↓
Identity Resolution
   ↓
Customer
   ↓
Account

If multiple materially different candidates remain:

Ambiguity
   ↓
CLARIFY / ESCALATE

Context must preserve unresolved candidates rather than silently converting a candidate into a canonical identity.

⸻

10. Context and Resource Resolution

Resources may include:

* Customer
* Account
* Transaction
* Statement
* Support Case

Context should contain only Resource references relevant to the current execution step.

For example:

get_account_balance
    ↓
account_reference

while:

create_complaint
    ↓
customer_reference
related_transaction_reference
related_account_reference

Resource references must preserve sufficient scope to prevent cross-resource or cross-tenant confusion.

⸻

11. Context and Account Scope

An account identifier must not be treated as globally sufficient where enterprise identifiers may collide.

Conceptually:

Account {
    tenant
    organization
    account_id
}

The relevant boundary may also include:

environment
legal_entity
business_unit

The important property is:

identifier + authority scope

rather than:

identifier alone

⸻

12. Context and Authorization

Context may carry authorization-relevant information:

principal_id
account_id
relationship
permissions
organization
tenant
scope
delegation

But the presence of authorization Context does not itself constitute an authorization decision.

Authorization remains a distinct evaluation:

Principal
    +
Action
    +
Resource
    +
Scope
    +
Policy
    ↓
Authorization Decision

A Resource appearing in Context does not imply that the Principal is authorized to access it.

⸻

13. Context and Permissions

Permissions constrain what Actions may be performed with the available Context.

For example, a Customer may be permitted to:

* read balance
* read transactions
* retrieve statements
* create complaints

while not being permitted to:

* access another customer’s account
* modify account ownership
* execute financial transfers

Context must never be used as a mechanism to bypass enterprise authorization.

⸻

14. Context and Business State

Business State belongs to the enterprise systems that own the relevant domain.

For example:

Ledger
   ↓
Account Balance

Noema may retrieve that state into Context.

It does not thereby become the owner of the balance.

Therefore:

Enterprise Business State
          ↓
       Context

not:

Context
   ↓
new canonical Noema Business State

⸻

15. Context and Noema State

Noema owns state about the execution journey.

Examples:

intent_status
trust_status
authorization_status
action_status
execution_status
intervention_status
outcome_status

Enterprise state and Noema execution state must remain semantically distinct.

Enterprise State
       +
Noema Execution State
       ↓
Context

Context may reference both without conflating them.

⸻

16. Context and Temporal State

Temporal interpretation must become explicit before an Action that depends on time is executed.

Context may contain:

request_time
current_time
effective_time
observed_at
date_from
date_to
timezone
temporal_resolution

For:

“transactions from yesterday”

Noema should establish an explicit interval:

Natural Language
       ↓
Temporal Resolution
       ↓
date_from + date_to + timezone

The resolved interval, rather than the unresolved phrase, should be supplied to the Action.

⸻

17. Context and Historical State

Previous interactions may be relevant:

* previous clarification
* previous Action
* previous failure
* previous customer response
* previous execution attempt

Historical Context must remain distinguishable from current enterprise state.

Historical information must not silently override current canonical state.

When historical information conflicts with current authoritative state, authority and Policy determine the resolution.

⸻

18. Context and Freshness

Context facts may differ in freshness.

Example:

Ledger observation:
10 seconds old
Transaction projection:
5 minutes old
Customer-provided information:
2 hours old

Freshness must be represented where it affects Trust, Action eligibility, or verification.

Freshness and authority are independent:

fresh ≠ canonical
canonical ≠ necessarily fresh

A fresh projection does not become canonical merely because it is newer.

⸻

19. Context and Provenance

Consequential Context facts should preserve provenance.

Conceptually:

ContextFact {
    value
    classification
    source
    authority
    observed_at
    effective_at
    version
    scope
    freshness
}

This allows Noema to answer:

* Where did this information come from?
* What kind of information is it?
* When was it observed?
* What Resource does it describe?
* Who is authoritative for it?
* Was it current enough for the Action?

⸻

20. Context Assembly

Context should be assembled from relevant sources according to the requirements of the resolved Intent, Action, and Policy.

Conceptually:

Intent
   ↓
Context Requirements
   │
   ├── Identity
   ├── Resource
   ├── Enterprise State
   ├── Evidence
   ├── Permissions
   ├── Temporal State
   ├── Policy
   └── Execution State
          ↓
       Context

Context assembly must be deterministic at the boundary where a consequential decision depends on the resulting values.

The model may propose interpretations or candidates; the Context layer must preserve their classification until grounded.

⸻

21. Context Should Be Minimal

Noema should prefer:

minimum sufficient context

over:

maximum available context

This reduces:

* privacy exposure
* security risk
* reasoning complexity
* latency
* unnecessary model input
* data leakage
* accidental scope expansion

Context minimization is therefore both an architectural and security principle.

⸻

22. Context Expansion

Context may expand during execution when a new requirement is established.

Example:

Initial Context
    ↓
principal_id
    ↓
account resolution required
    ↓
account_id
    ↓
statement requested
    ↓
statement period

Expansion must be requirement-driven.

Noema should not pre-load unrelated enterprise data merely because it may become useful.

⸻

23. Context Reduction

Context should support controlled reduction.

Information no longer required by a downstream Action should not automatically propagate.

For example:

Identity Resolution
    ↓
customer_id established

An internal identity-resolution artifact does not need to be passed to every enterprise capability.

Context propagation must therefore be explicit rather than ambient.

⸻

24. Context and Data Boundaries

Context assembly must respect:

* tenant boundaries
* organizational boundaries
* legal boundaries
* environment boundaries
* permission boundaries
* purpose boundaries
* Resource boundaries

For example, Customer Account Inquiry does not automatically authorize access to:

* internal fraud models
* employee records
* other customers
* restricted operational data

Context must not become a side channel around enterprise data controls.

⸻

25. Context and Data Minimization

Context requirements depend on the Action.

For:

get_account_balance

the Context may require:

principal_id
account_reference
authorization_context
freshness_requirement

For:

search_transactions

it may additionally require:

date_range
filters

For:

create_complaint

it may require:

customer_reference
complaint_description
related_resource
idempotency_key

The Action contract determines the required Context.

⸻

26. Context and Action Selection

Context supports Action selection but does not independently authorize execution.

Example:

Intent:
"How much did I spend last month?"
Context:
    principal = customer
    account = resolved
    period = previous calendar month

This supports resolution to:

get_spending_summary

when the resolved Intent requires an aggregate result.

The Action must still pass Trust, Policy, authorization, and Precondition checks.

⸻

27. Context and Planning

Planning uses Context to establish dependencies and determine what information must be acquired next.

Example:

Context:
    customer_id = 123
    account_id = unknown
    period = 2026-08

The plan may require:

resolve account
      ↓
search transactions
      ↓
get spending summary

Context evolves with the plan.

Planning must not treat missing Context as permission to invent values.

⸻

28. Context and Preconditions

Preconditions consume Context.

Example:

Precondition:
Principal authorized for Account

may require:

principal_id
account_id
authorization information
tenant
scope

If required Context is absent:

Precondition
      ↓
cannot evaluate
      ↓
BLOCKED

Missing information is not equivalent to a satisfied Precondition.

⸻

29. Context and Postconditions

Postcondition verification may add new Context.

Example:

create_complaint
      ↓
case_id
      ↓
verification
      ↓
case.status

The resulting state may become:

* Context
* Evidence
* Outcome input

but the Support System remains authoritative for the case.

⸻

30. Context and Trust

Trust evaluates whether the information in Context is sufficient and reliable enough for the requested decision.

Context may contain:

canonical account reference
authenticated principal
authorization evidence
temporal resolution
state observations
provenance
freshness

If Context contains unresolved ambiguity:

Trust
   ↓
INSUFFICIENT
   ↓
CLARIFY / ESCALATE

Trust must not manufacture certainty from incomplete Context.

⸻

31. Context and Model Output

The model may contribute information to Context, including:

* interpreted Intent
* extracted merchant
* extracted date range
* candidate Resource
* candidate Action
* candidate classification

These values must retain their semantic classification.

For example:

model_candidate_account

must not silently become:

canonical_account_id

The model proposes.

Grounding establishes.

Policy and Trust determine whether the grounded information may support execution.

The POC specification explicitly requires that free-form model output never reach an execution pathway and that schema validation exist before model output can participate in execution. NOEMA POC Specification_1.pdf

⸻

32. Context and User Input

User-provided information may be included in Context.

Example:

“I made a payment to Netflix yesterday.”

This may produce:

merchant = Netflix
date_reference = yesterday

These remain user-provided information or model interpretation until grounded.

They are not automatically canonical enterprise facts.

Where the Action depends on canonical state, enterprise data must establish the relevant fact.

⸻

33. Context and Derived Data

Context may contain derived information.

Example:

spending_last_month = ₦450,000

If calculated from transactions, it should be classified as derived.

Noema must preserve the distinction between:

canonical transaction

and:

derived spending summary

A derived value must not be represented as an authoritative ledger fact unless the enterprise explicitly defines it as such.

⸻

34. Context and Multiple Sources

Context may contain information from several enterprise systems.

Example:

Identity System
      ↓
principal_id
Account System
      ↓
account_id
Ledger
      ↓
balance
Transaction System
      ↓
transactions
Support System
      ↓
existing cases

Noema must preserve:

* source
* authority
* timestamp
* version
* scope
* classification

Agreement between sources does not automatically establish authority.

⸻

35. Context Conflicts

Context may contain conflicting observations.

Example:

Account System:
account status = ACTIVE
Projection:
account status = CLOSED

Noema must not resolve the conflict through model preference.

Instead:

Conflict
   ↓
Authority Resolution
   ↓
State Reconstruction
   ↓
Trust / Policy
   ↓
Continue / CLARIFY / ESCALATE / REJECT

Where enterprise state is materially contradictory, Context must preserve the contradiction rather than collapsing it into a guessed value.

The POC specifically treats contradictory enterprise state as a first-class condition requiring reconstruction rather than best-guess resolution. NOEMA POC Specification_1.pdf

⸻

36. Context Unavailability

Required Context may be unavailable.

Example:

Ledger unavailable

If the Action requires current authoritative balance:

Context incomplete
       ↓
Trust / Policy
       ↓
RETRY / CLARIFY / ESCALATE / REJECT

A missing authoritative fact must not be silently replaced with an uncertain value when Policy requires the authoritative fact.

⸻

37. Context and Read Operations

The initial Customer Account Inquiry workflow is primarily read-oriented.

Typical Context requirements include:

* identity
* Resource
* scope
* filters
* time
* authorization
* freshness

The Phase 1 boundary does not authorize financial movement.

The POC specification makes prohibited monetary actions architecturally impossible and restricts safe execution to bounded, non-monetary capabilities. NOEMA POC Specification_1.pdf

⸻

38. Context and Complaint Logging

create_complaint is the principal support-state-changing Action in this workflow.

Its Context may include:

customer_reference
complaint_description
related_transaction_reference
related_account_reference
relevant prior interaction
idempotency_key

Only relevant information should be passed to the Support System.

Noema must not attach the customer’s entire Context automatically.

⸻

39. Context and Compound Intent

A Customer may issue:

“Show me what I spent last month and open a complaint about the Netflix transaction.”

This may require:

customer identity
account
period
transaction
merchant
complaint description

But Context must remain partitionable by Action:

Compound Intent
       ↓
Action A Context
       +
Action B Context

Not every Action receives every Context field.

⸻

40. Context Partitioning

Context should be partitioned according to execution boundaries.

Example:

Global Execution Context
        │
        ├── Identity Context
        ├── Account Context
        ├── Transaction Context
        └── Support Context

An enterprise integration receives only the portion required by its Action.

Partitioning is a security property as well as an architectural property.

⸻

41. Context and External Integrations

Integrations translate typed Noema Context into enterprise-specific requests.

Conceptually:

Noema Context
      ↓
Action Contract
      ↓
Integration
      ↓
Enterprise API

The Integration must not invent missing Context.

If required information is absent, execution stops according to Policy.

The Action remains the semantic execution unit; the enterprise API remains an implementation interface.

⸻

42. Context and Execution State

Context may reference the current execution position.

Example:

Action:
search_transactions
Execution State:
EXECUTING

After execution:

Action:
search_transactions
Execution State:
SUCCEEDED

Execution state belongs to Noema.

Transaction state belongs to the enterprise.

These must never be conflated.

⸻

43. Context and Recovery

When execution fails or becomes uncertain, sufficient Context must be retained to determine whether recovery is possible.

Example:

Action:
retrieve_statement
Execution:
TIMEOUT

Recovery may require:

action_id
action_version
statement_id
account_id
request_id
attempt
idempotency_key
execution_state

Recovery must not depend on reconstructing critical information from model memory.

A timeout must remain distinguishable from a confirmed failure or success until the relevant enterprise state has been verified. The POC explicitly defines timeout as EXECUTION_OUTCOME_UNKNOWN until verification resolves it. NOEMA POC Specification PDF.pdf

⸻

44. Context and Idempotency

For state-changing Actions, Context may contain the idempotency key.

Example:

create_complaint
      ↓
idempotency_key

The key must be created before the external call and remain stable across retries of the same logical Action execution.

Noema must distinguish:

new logical execution

from:

retry / replay of existing logical execution

The POC requires idempotency to be established before execution and duplicate/replay handling to produce exactly one effect. NOEMA POC Specification_1.pdf

⸻

45. Context and Auditability

For consequential execution, Noema should preserve a Context snapshot or sufficient references to reconstruct the relevant Context.

The record should allow Noema to answer:

* What did Noema know?
* When did it know it?
* Where did each relevant fact come from?
* What was canonical?
* What was derived?
* What was merely a model candidate?
* What Action did the Context enable?
* Which Policy version applied?
* What was executed?
* What was verified?

The objective is not indefinite retention of every available datum.

The objective is deterministic reconstruction of the relevant decision and execution path.

The POC requires consequential decisions to be reconstructable from the audit store and treats causal provenance as a core proof requirement. NOEMA POC Specification_1.pdf

⸻

46. Context Lifecycle

Context evolves through the execution lifecycle:

REQUEST
   ↓
INITIAL CONTEXT
   ↓
IDENTITY / RESOURCE RESOLUTION
   ↓
ENRICHED CONTEXT
   ↓
STATE RECONSTRUCTION
   ↓
TRUST + POLICY
   ↓
ACTION
   ↓
EXECUTION EVIDENCE
   ↓
UPDATED CONTEXT
   ↓
POSTCONDITION / VERIFICATION
   ↓
OUTCOME

Context is therefore dynamic.

It is not necessarily one immutable object created at request time.

⸻

47. Context Snapshot

At important execution boundaries, Noema may create Context Snapshots.

Examples:

* pre-resolution snapshot
* pre-trust snapshot
* pre-action snapshot
* post-action snapshot
* postcondition snapshot
* recovery snapshot

Snapshots support:

* audit
* debugging
* recovery
* incident analysis
* causal reconstruction

The persistence strategy is an implementation concern; the semantic requirement is reconstructability.

⸻

48. Context Freshness Requirements

Freshness requirements should be explicit where the validity of a Context fact changes materially over time.

For example:

balance observed at 09:00

may no longer satisfy an Action at:

09:30

if the Action requires current authoritative state.

Freshness requirements belong to the Action and Policy, not to a generic assumption that all Context is equally current.

⸻

49. Context Expiration

Context should support expiration semantics where required.

Conceptually:

ContextFact {
    value
    observed_at
    expires_at
}

Not every fact requires expiration.

Only facts whose validity materially changes with time require explicit expiration or freshness handling.

Expired Context must not silently satisfy a freshness-sensitive Precondition.

⸻

50. Context and Environment

Context must preserve environment boundaries.

Example:

environment = production

must remain distinct from:

environment = staging

Production execution must never be satisfied using staging Context merely because the values appear plausible.

Environment is part of the execution boundary.

⸻

51. Context and Tenancy

Context must preserve tenant boundaries.

Example:

tenant = A
account_id = 123

must remain distinct from:

tenant = B
account_id = 123

The identifier alone is insufficient.

Tenant identity is part of the Resource and authorization boundary.

⸻

52. Context and Organizational Boundaries

Where the enterprise contains multiple organizational scopes, Context should preserve relevant:

* organization
* business unit
* legal entity
* environment

These may affect:

* Resource visibility
* authorization
* Policy
* available Actions
* authority

Context must not collapse these boundaries.

⸻

53. Context Model

Conceptually:

Context {
    execution_id
    actor
    principal
    tenant
    organization
    environment
    intent
    resources
    canonical_data
    observations
    evidence
    derived_data
    user_input
    model_candidates
    permissions
    policy
    policy_version
    temporal_state
    freshness_requirements
    trust_state
    authorization_state
    execution_state
    action_state
    outcome_state
    provenance
    idempotency
    recovery
}

This is a semantic model rather than a requirement for a literal database schema.

The important property is preservation of semantic classification and provenance.

⸻

54. Context Relationships

Context
   │
   ├── references → Intent
   ├── references → Actor / Principal
   ├── references → Resources
   ├── contains → Canonical Data
   ├── contains → Observations
   ├── contains → Evidence
   ├── contains → Derived Data
   ├── contains → User Input
   ├── contains → Model Candidates
   ├── contains → Permissions
   ├── contains → Policy + Policy Version
   ├── contains → Temporal State
   ├── contains → Trust State
   ├── contains → Authorization State
   └── contains → Execution State

These relationships do not imply equal authority.

A Context field must retain its classification independently of where it is stored.

⸻

55. Context Invariants

Invariant 1

Context must be scoped to a specific execution journey.

Invariant 2

Context must not be treated as inherently authoritative.

Invariant 3

Canonical Data retains its authority independently of Context.

Invariant 4

Evidence retains its provenance independently of Context.

Invariant 5

Model-generated information must retain its classification as interpretation or hypothesis until appropriately grounded.

Invariant 6

User-provided information must not automatically become canonical enterprise data.

Invariant 7

Context must contain the minimum information necessary for the relevant execution step.

Invariant 8

Context must respect enterprise data, tenant, organizational, legal, environment, and permission boundaries.

Invariant 9

Resource identifiers must retain sufficient scope to prevent accidental cross-resource execution.

Invariant 10

Missing required Context must not be treated as a satisfied Precondition.

Invariant 11

Ambiguous Context must not be resolved through probabilistic guessing where Policy requires deterministic resolution.

Invariant 12

Context freshness must be considered whenever freshness affects the Action or Trust decision.

Invariant 13

Authority and freshness are independent properties of Context data.

Invariant 14

Context may contain information from multiple sources without making those sources equally authoritative.

Invariant 15

Conflicting Context must be resolved according to authority and Policy rather than model preference.

Invariant 16

Noema must not create competing canonical Business State merely by maintaining Context.

Invariant 17

Context passed to an enterprise integration must be limited to the data required by the Action.

Invariant 18

Context must preserve sufficient provenance for consequential decisions.

Invariant 19

Context must preserve the distinction between enterprise Business State and Noema Execution State.

Invariant 20

Context must support deterministic reconstruction of relevant execution decisions where required.

Invariant 21

Context should evolve as execution requirements change rather than being populated indiscriminately.

Invariant 22

Context must not silently cross environment boundaries.

Invariant 23

Context must not silently cross tenant or organizational boundaries.

Invariant 24

Context associated with a retry must preserve the identity of the original logical Action execution.

Invariant 25

Context is an execution resource, not a substitute for enterprise authority.

Invariant 26

A model candidate must never silently become a canonical Resource, enterprise fact, authorization result, or executable Action input.

Invariant 27

A Context value used for a consequential decision must retain enough classification and provenance to determine whether it is canonical, observed, derived, user-provided, historical, or model-generated.

Invariant 28

Contradictory enterprise observations must remain representable as contradictory until resolved through authority, state reconstruction, Trust, and Policy.

Invariant 29

A timeout or unavailable source must not cause Context to manufacture a successful or failed enterprise state.

Invariant 30

Policy-sensitive Context must preserve the governing Policy version used for the decision.

Invariant 31

Context must not cause an Action to execute merely because the required fields can be syntactically populated.

Invariant 32

Context must preserve the distinction between a Resource candidate and a resolved Resource.

Invariant 33

Context must preserve the distinction between execution Outcome and enterprise Business State.

Invariant 34

Context required for recovery must be sufficient to distinguish a new logical execution from retry, replay, or verification of an existing execution.

Invariant 35

Context must never be used as an implicit authorization bypass or confused-deputy channel.

⸻

56. Final Definition

Context is the minimum sufficient, typed, execution-scoped information envelope through which Noema carries the information required to understand, resolve, authorize, plan, execute, verify, recover, and explain a specific Intent while preserving the authority, provenance, freshness, scope, and semantic classification of every consequential fact.

For the Customer Account Inquiry workflow:

ACTOR / PRINCIPAL
        │
        ▼
      INTENT
        │
        ▼
 CONTEXT ASSEMBLY
        │
        ├── Identity
        ├── Resource References
        ├── Canonical Data
        ├── Observations
        ├── Evidence
        ├── Derived Data
        ├── User Input
        ├── Model Candidates
        ├── Permissions
        ├── Policy + Version
        ├── Temporal State
        ├── Freshness
        └── Execution State
        │
        ▼
 STATE RECONSTRUCTION
        │
        ▼
   TRUST + POLICY
        │
        ▼
      ACTION
        │
        ▼
 ENTERPRISE CAPABILITY
        │
        ▼
 ENTERPRISE STATE
        │
        ▼
 EXECUTION EVIDENCE
        │
        ▼
   VERIFICATION
        │
        ▼
      OUTCOME

And the architectural rule is:

Noema should know enough to execute safely, but Context must never cause Noema to confuse what it knows with what is authoritative, what is current, what is resolved, what is permitted, or what the model merely proposed.

The deeper rule is:

Context carries information; authority remains with the system, evidence, policy, or state that establishes it.

This update also aligns the Context contract with the POC’s explicit requirements for deterministic execution, typed boundaries, state reconstruction, policy-versioned decisions, unknown execution outcomes, idempotency, and causal auditability. NOEMA POC Specification_1.pdf