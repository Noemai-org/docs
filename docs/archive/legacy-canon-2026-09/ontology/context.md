> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Context

Status: Foundational
Version: 0.2
Domain: Ontology
Canonical Path: ontology/context.md

Update basis: This revision preserves the full semantic coverage, 66-section structure, terminology, distinctions, examples, and invariants of the supplied context.md, while tightening the ontology around the current Noema Canon—particularly the separation between Context, Enterprise State, State Reconstruction, Evidence, Intent, Trust, Authority, Policy, and Execution. The current Noema architecture explicitly treats Context as the layer that enriches an Intent with identity, permissions, history, session, device, and candidate resolution, while State Reconciliation reconstructs authoritative truth from potentially conflicting or stale enterprise systems. Noema Master Company Document FINAL.pdf

⸻

1. Definition

Context is the bounded, purpose-scoped, authority-aware set of information relevant to interpreting an Intent, resolving ambiguity, evaluating Trust, planning an Action, executing that Action, or verifying its Outcome.

Context answers:

“What information is relevant and available for this decision or execution at this point in time?”

Context is not synonymous with:

* Enterprise State
* Canonical Data
* Reconstructed State
* Evidence
* Intent
* Business State
* Model Input
* Model Output
* Conversation History
* Authority
* Policy
* Trust

Context is the information made available to Noema for a particular execution journey.

Conceptually:

Enterprise Systems
       │
       ▼
Relevant Information
       │
       ▼
     Context
       │
       ├── Intent Resolution
       ├── State Reconstruction
       ├── Trust Evaluation
       ├── Planning
       ├── Execution
       └── Verification

Context therefore functions as an information boundary around a particular Noema decision or execution journey.

It does not itself establish that every fact within it is authoritative, current, permitted, or sufficient.

⸻

2. Purpose

The purpose of Context is to provide Noema with enough relevant information to make an explicit and bounded decision.

Context allows Noema to establish things such as:

* Who is acting?
* What is being requested?
* What Resource is involved?
* What is the relevant current state?
* Which policies apply?
* What permissions exist?
* What evidence supports a proposition?
* What happened previously?
* What Constraints apply?
* What information is missing?
* What ambiguity remains?
* What information must be refreshed before execution?

Context should therefore be decision-oriented, rather than indiscriminately comprehensive.

The objective is not to maximize the amount of information available to the model or execution system.

The objective is to establish the information required to safely perform the relevant operation.

⸻

3. Core Principle

Context is relevant information within a defined scope.

More context does not necessarily produce better decisions.

Excess context can introduce:

* irrelevant information
* stale information
* conflicting information
* privacy exposure
* authorization complexity
* unnecessary data dependencies
* model confusion
* increased attack surface
* ambiguous authority
* unnecessary retrieval cost

Therefore:

Noema should retrieve and expose the minimum Context necessary for the current decision or Action, subject to the information required by Trust, Policy, and verification.

Data minimization must not, however, result in omission of a fact that is material to the decision.

The correct principle is:

Minimum necessary Context, not minimum possible Context.

⸻

4. Context Is Scoped

Context always exists within a scope.

Relevant dimensions may include:

* Intent
* Workflow
* Action
* Resource
* Principal
* Tenant
* Organization
* Environment
* Time
* Policy
* Authority
* Execution State
* Risk
* Purpose

For example:

Context for:

“Show my balance.”

may differ substantially from:

“Transfer $9,000.”

even when both involve the same customer and account.

The second operation may require additional Context concerning:

* current balance
* transfer limits
* beneficiary state
* authorization
* risk
* policy
* confirmation
* freshness

Context is therefore purpose-bound.

⸻

5. Context Is Dynamic

Context is not necessarily static for the lifetime of an Intent.

Enterprise state may change.

Policies may change.

Permissions may change.

Risk may change.

Execution state may change.

Resource identity may change.

External conditions may change.

Therefore:

Context(T1)
      ≠
Context(T2)

in general.

Noema must determine when Context remains valid and when it must be refreshed.

A Context Snapshot may remain historically valid without remaining suitable for current execution.

This distinction is essential.

⸻

6. Context vs Canonical Data

Canonical Data is authoritative information within a defined enterprise authority boundary.

Context is information assembled for Noema’s reasoning or execution.

Therefore:

Canonical Data
       ↓
     Context

may be valid.

But:

Context
       ↓
Canonical Data

must not happen automatically.

For example:

Ledger:
balance = $10,000
Noema Context:
balance = $10,000

The Context contains the value.

The Ledger remains authoritative for the underlying Business State.

Noema must not create a competing canonical record merely because it stores or transforms a value into Context.

This preserves the enterprise system-of-record boundary that is central to Noema’s architecture. NOEMA POC Specification_1.pdf

⸻

7. Context vs Business State

Business State belongs to the enterprise systems that own the relevant business domain.

Examples:

Account.balance
Payment.status
Card.status
Customer.status
Inventory.quantity

Noema may observe these values through Context.

It does not thereby become their owner.

Conceptually:

Enterprise System
       │
       ▼
Business State
       │
       ▼
     Context
       │
       ▼
     Noema

Context is therefore a representation of relevant information, not ownership of the underlying enterprise state.

⸻

8. Context vs Noema State

Noema also has its own state.

Examples:

* Intent State
* Trust State
* Action State
* Execution State
* Intervention State
* Outcome State
* Investigation State

These are canonical within Noema’s execution domain.

Therefore two different authority domains can coexist:

Enterprise Canonical State
        │
        │
        ▼
     Context
        │
        │
        ▼
Noema Execution State

Neither should silently replace the other.

A Noema execution state such as:

execution.status = AWAITING_VERIFICATION

does not imply:

account.status = ACTIVE

or any other enterprise state.

⸻

9. Context vs Intent

Intent represents what a Principal is trying to accomplish.

Context provides information that helps Noema understand and act upon that Intent.

Example:

Intent:
"Show me my transactions from last month."
Context:
customer_id
account_id
available accounts
date
transaction access permissions

Context helps resolve the Intent.

It does not become the Intent itself.

An account identifier discovered through Context is not automatically part of the original Intent; it may be a resolution of an Intent reference.

⸻

10. Context vs Evidence

Evidence supports a proposition, decision, or conclusion.

Context is the information available for reasoning or execution.

For example:

Context:
account.balance = $10,000

Evidence may record:

Source:
Ledger
Observed:
2026-09-01T10:15:00
Value:
account.balance = $10,000
Version:
482

Therefore:

Context
   +
Provenance
   ↓
Evidence

may describe why a Context fact can be relied upon.

However, Context and Evidence remain semantically distinct.

A value can exist in Context without being sufficient Evidence for a consequential Trust decision.

⸻

11. Context vs Model Input

Context may be provided to a model.

But:

Model Input ⊂ Context

is often more appropriate than:

Model Input = Entire Context

The model should receive only the information necessary for its particular task.

For example, Intent Resolution may require:

* User request
* Relevant account identifiers
* Available Resources
* Relevant conversation history

It may not require:

* Full transaction history
* Unrelated customer data
* Internal security metadata
* Unrelated organizational information

Context is therefore broader than any individual model input.

⸻

12. Context vs Model Output

Model output may add interpretations to the execution journey.

Examples:

“The user is asking for a spending summary.”

“Account 123 is probably the intended account.”

“The user may mean transactions from August.”

These are model-derived interpretations.

They are not automatically canonical Context.

They must retain their appropriate semantic classification.

Conceptually:

Model Output
      ↓
Candidate Interpretation
      ↓
Validation / Grounding
      ↓
Context

where applicable.

The model may propose.

It does not establish enterprise truth merely by generating a statement.

This follows Noema’s separation of duties: probabilistic interpretation is permitted upstream, while deterministic systems establish whether consequential execution may proceed. NOEMA POC Specification HTML.html

⸻

13. Context Components

Context may contain several categories of information.

Conceptually:

Context
   │
   ├── Identity
   ├── Intent
   ├── Resources
   ├── Business State
   ├── Reconstructed State
   ├── Policy
   ├── Authority
   ├── Permissions
   ├── Constraints
   ├── Evidence
   ├── Temporal State
   ├── Organizational State
   ├── Conversation
   └── Execution State

Not every execution requires every category.

The presence of a category does not mean every element within that category is applicable.

Context composition must remain purpose- and Action-specific.

⸻

14. Identity Context

Identity Context establishes the Principal relevant to the execution.

Examples:

principal_id
customer_id
organization_id
tenant_id
authentication state
identity verification state

Identity Context is especially important when an Intent references:

* “my account”
* “my transactions”
* “my statement”
* “our organization”

Identity must be grounded appropriately before consequential execution.

An asserted identity and a verified identity must remain distinguishable where the distinction is material.

⸻

15. Resource Context

Resource Context identifies the enterprise Resources relevant to the Intent.

Examples:

* account
* payment
* transaction
* invoice
* customer
* order
* subscription
* case

For example:

Intent:
"Show my balance."
Context:
customer_id = C-123
account_id = A-456

If multiple Resources are possible, Context may expose the ambiguity rather than resolving it arbitrarily.

For example:

Candidate Resources:
A-456
A-789
A-901

does not justify silently selecting one.

⸻

16. Business-State Context

Business-State Context represents relevant enterprise state.

Examples:

account.status
account.balance
payment.status
transaction.amount
transaction.date

The underlying state remains owned by the appropriate enterprise System of Record.

Context is the representation consumed by Noema.

Where multiple systems provide state, Context may contain the observations required for State Reconciliation.

⸻

17. Policy Context

Policy Context contains rules relevant to the current decision.

Examples:

* access policy
* transaction limits
* retention policy
* approval requirements
* risk thresholds
* execution constraints
* escalation requirements

Policy Context must be temporally and organizationally scoped.

A Policy applicable to one tenant or environment must not silently apply to another.

Policy Context may also determine which Constraints become applicable to the current execution.

⸻

18. Authorization Context

Authorization Context contains information necessary to determine whether a Principal may perform an Action against a Resource.

Examples:

Principal
Role
Permissions
Resource
Tenant
Organization
Delegation
Action

Context provides the information.

The Trust Engine determines whether authorization requirements are satisfied.

The fact that Noema can technically retrieve a Resource does not establish that the Principal is authorized to act upon it.

⸻

19. Temporal Context

Many decisions depend on time.

Temporal Context may include:

* current time
* effective time
* observation time
* Resource timestamps
* Policy validity
* execution time
* historical state
* expiry
* freshness requirements

For example:

Current Time:
2026-09-01
Transaction Range:
2026-08-01 → 2026-08-31

Temporal Context should use the appropriate timezone and enterprise semantics.

Where an Action is consequential, the distinction between:

observed_at

and:

effective_at

must be preserved.

⸻

20. Historical Context

Historical information may be relevant to an execution.

Examples:

* previous Intent
* previous clarification
* previous Action
* previous execution attempt
* previous approval
* previous failure
* previous Policy version
* previous Resource state

Historical Context should not automatically override current canonical Business State.

Its purpose is to provide relevant temporal information.

Historical information may explain how the current execution arrived at its present state without becoming current enterprise truth.

⸻

21. Conversation Context

Conversation history may be part of Context.

Example:

User:
"Show my transactions."
Noema:
"Which account?"
User:
"My current account."

The second message depends on the first.

Conversation Context can therefore contribute to Intent Resolution.

However:

Conversation history is not authoritative enterprise state.

Conversation may establish what a Principal said.

It does not, by itself, establish what is true in an enterprise system.

⸻

22. Execution Context

Execution Context represents the current Noema execution journey.

Examples:

workflow_id
intent_id
action_id
current execution state
previous attempts
pending Actions
completed Actions
failure state
intervention state

This is distinct from enterprise Business State.

For example:

Noema:
execution.status = AWAITING_VERIFICATION
Enterprise:
account.status = ACTIVE

Both may be valid simultaneously.

Execution Context therefore represents Noema’s own processing state around an enterprise operation.

⸻

23. Context and Ambiguity

Context can reduce ambiguity.

It can also reveal ambiguity.

Example:

Intent:
"Show my account."
Context:
Account A
Account B
Account C

The Context establishes that multiple candidates exist.

It does not justify guessing.

Therefore:

Ambiguity
    ↓
Clarification

may be the correct next state.

This follows a fundamental Noema principle:

Ambiguity is a state, not an invitation to guess.

The Context layer should expose ambiguity rather than conceal it.

⸻

24. Context and Determinism

Context is one of the inputs to deterministic decision-making.

Conceptually:

Intent
   +
Context
   +
Evidence
   +
Policy
   +
Authorization
   +
Risk
   +
Constraints
   ↓
Trust Decision

The model may help construct or interpret Context.

The final execution decision must be governed by deterministic rules and enterprise constraints.

This distinction is central to Noema’s architecture: the Trust Engine is explicitly a deterministic evaluator rather than a model-based self-authorization mechanism. NOEMA POC Specification HTML.html

⸻

25. Context and Trust

Trust evaluates whether the available Context is sufficient and reliable enough for the intended Action.

Trust may consider:

* authority
* freshness
* provenance
* authorization
* policy
* risk
* completeness
* ambiguity
* validation
* state consistency
* constraints

Therefore:

Context
   ↓
Trust

does not mean that all Context is automatically trusted.

Context supplies information.

Trust determines whether the information and conditions are sufficient for the relevant decision.

⸻

26. Context Completeness

Context completeness is Action-specific.

For one Action:

“Show my balance.”

the required Context may be:

* identity
* account
* balance
* authorization

For another:

“Find my transactions from August.”

it may require:

* identity
* account
* date range
* transaction access
* transaction data

Therefore:

Context is complete when it contains the information required for the current decision, not when it contains everything known about the Principal or Resource.

Completeness is therefore relative to the Action, not an absolute property of the Context as a whole.

⸻

27. Context Freshness

Context may become stale.

Example:

10:00
Context:
balance = $10,000
10:05
Enterprise:
balance = $8,000

The original Context may still be historically accurate.

It may no longer be suitable for a consequential Action.

Therefore Context must distinguish:

correct when observed

from:

current enough for this Action

Freshness is consequently an Action-specific property.

A fact can be authoritative but too old for the operation being contemplated.

⸻

28. Context Refresh

Noema may refresh Context when:

* Action risk is high
* freshness requirement has expired
* enterprise state may have changed
* Policy requires current state
* Preconditions require fresh data
* postconditions require verification
* an execution failure may have changed external state
* an uncertain outcome requires reconciliation

Conceptually:

Existing Context
       ↓
Freshness Check
       ↓
Refresh Required
       ↓
Enterprise System
       ↓
Updated Context

Refreshing Context does not mean replacing historical Context.

Both may need to remain available for audit and reconstruction.

⸻

29. Context Snapshots

Noema may create a Context Snapshot representing the information used for a particular decision.

Conceptually:

ContextSnapshot {
    intent
    principal
    resources
    facts
    policies
    evidence
    timestamp
    versions
}

Snapshots support:

* auditability
* reconstruction
* debugging
* decision explanation
* historical analysis
* reproducibility

A snapshot does not become the current enterprise truth.

A Trust decision should be traceable to the relevant Context Snapshot where required.

The current POC architecture similarly requires a decision to reference the exact reconstructed state snapshot against which it was made. NOEMA POC Specification_1.pdf

⸻

30. Context and Preconditions

Preconditions depend on Context.

Example:

Precondition:
account.status = ACTIVE

Context supplies the relevant state:

account.status = ACTIVE

Trust evaluates whether that information is sufficiently authoritative and current to satisfy the Precondition.

Context therefore supplies the factual basis.

The Precondition defines the required condition.

Trust determines whether the available information establishes that the requirement is met.

⸻

31. Context and Postconditions

Postconditions may require Context after an Action.

Example:

Action:
retrieve_statement
Postcondition:
statement successfully retrieved

Noema may need new Context after execution to establish the Outcome.

For state-changing Actions, this distinction becomes even more important:

Action
   ↓
Enterprise State Change
   ↓
Fresh Context
   ↓
Postcondition
   ↓
Outcome

An API response alone does not necessarily establish the postcondition.

⸻

32. Context and Planning

Planning uses Context to determine the feasible execution path.

Example:

Intent:
"Show my spending for August."
Context:
customer
accounts
transactions
date range
permissions

The Planner may determine:

resolve account
→ retrieve transactions
→ aggregate spending
→ return result

Planning must operate within the Authority, Policy, Constraint, and Trust boundaries established elsewhere in the Canon.

Context provides the information required to construct the feasible path; it does not itself authorize execution.

⸻

33. Context and Execution

Execution consumes the Context required by the Action Contract.

For example:

Action:
search_transactions

may require:

principal_id
account_id
start_date
end_date
authorization

The Action should not receive arbitrary enterprise data merely because it exists in the broader Context.

This establishes a second boundary:

Broad Context
      ↓
Action-required Context
      ↓
Action Contract
      ↓
Execution

This supports least-privilege execution and limits unnecessary data exposure.

⸻

34. Context and Read Operations

Noema’s initial commercial wedge emphasizes read and support operations.

Examples:

* balance inquiries
* statement retrieval
* transaction search
* spending summaries
* complaint logging

Even these apparently simple operations require Context.

For example:

“How much did I spend last month?”

may require:

* identity
* account
* date range
* transactions
* currency
* authorization

The fact that an operation is read-oriented does not eliminate Trust requirements.

Noema’s POC similarly treats context resolution, state reconstruction, Trust, and verification as part of the core loop rather than limiting Trust to monetary writes. NOEMA POC Specification_1.pdf

⸻

35. Context and Financial Writes

Future financial write operations may require substantially stronger Context guarantees.

For example:

“Transfer $9,000 to John.”

may require:

* identity
* recipient identity
* source account
* destination account
* balance
* limits
* authorization
* risk
* policy
* confirmation
* freshness
* beneficiary state
* relevant transaction state

The Context requirements therefore scale with Action risk.

Higher-consequence operations require stronger guarantees around the information against which the decision is made.

⸻

36. Context and Data Minimization

Noema should apply the principle:

Retrieve what is necessary for the decision, and no more.

For example, a transaction search may require:

* account_id
* date range
* transaction fields

It does not automatically require:

* full customer profile
* home address
* unrelated accounts
* complete account history
* unrelated financial information

Context should therefore be purpose-bound.

Data minimization is not merely a privacy concern.

It also improves:

* authorization clarity
* model reliability
* reasoning boundaries
* auditability
* integration simplicity
* security posture

⸻

37. Context and Data Boundaries

Context must respect enterprise data boundaries.

These may include:

* tenant
* organization
* legal entity
* business unit
* environment
* data classification
* resource ownership
* geographic boundary
* regulatory boundary

Noema must not construct a Context that crosses these boundaries implicitly.

Cross-boundary Context requires the relevant authority and policy.

⸻

38. Context and Permissions

The fact that Noema can technically retrieve information does not mean that information should enter Context.

Access must remain bounded by:

* authorization
* purpose
* scope
* data policy
* tenant boundary
* Resource ownership

Therefore:

Accessible Data
      ≠
Permitted Context

Technical reachability is not semantic authorization.

⸻

39. Context and Provenance

Consequential Context should preserve provenance where required.

Conceptually:

ContextFact {
    name
    value
    source
    authority
    observed_at
    effective_at
    classification
    version
    provenance
}

This allows Noema to determine:

* Where did this information come from?
* When was it observed?
* Who or what is authoritative?
* Which version was used?
* What classification applies?
* When does it expire?
* How was it derived?

Provenance is therefore part of the semantics of consequential Context, not merely an audit feature.

⸻

40. Context and Conflicting Information

Context may contain conflicting values.

Example:

Ledger:
balance = $10,000
Cache:
balance = $8,000

Noema should not resolve the conflict through:

* model confidence
* majority vote
* arbitrary source selection
* recency alone
* frequency
* convenience

Instead, it should apply the authority model.

If the conflict remains consequential:

CONFLICT
   ↓
Trust / Policy
   ↓
Clarify / Escalate / Reject

as appropriate.

This is consistent with Noema’s State Reconciliation model, which explicitly treats disagreement, staleness, incompleteness, and uncertainty as states to be represented rather than hidden. Noema Master Company Document FINAL.pdf

⸻

41. Context and Missing Information

Required Context may be unavailable.

Example:

Identity available
Account available
Policy available
Balance unavailable

If the Action requires current balance:

Context Incomplete
       ↓
Trust
       ↓
Retry / Clarify / Escalate / Reject

Noema should not invent the missing value.

Missing Context is a first-class state.

⸻

42. Context and Human Intervention

A human may supply additional information or make a decision when automated Context is insufficient.

Example:

Automated Context
       ↓
Insufficient
       ↓
Human Review
       ↓
Additional Evidence / Decision
       ↓
Updated Context

The human intervention itself becomes part of the execution record and should preserve:

* identity
* authority
* scope
* decision
* reason
* timestamp
* applicable Policy

Human intervention does not erase the prior uncertainty.

It adds an authoritative event or decision within a defined scope.

⸻

43. Context and Events

Events may contribute to Context.

Example:

Enterprise System
       ↓
account.balance.changed
       ↓
Event
       ↓
Noema
       ↓
Context Update

An event represents an observation or notification of change.

It does not necessarily establish the complete current canonical state.

Where required, Noema should verify against the System of Record.

An event may therefore update Context without becoming the authoritative state itself.

⸻

44. Context and Eventual Consistency

Context may originate from eventually consistent projections.

Therefore:

System of Record
       ↓
Event
       ↓
Projection
       ↓
Context

may produce temporarily stale information.

Noema must understand the consistency semantics before using such Context for consequential decisions.

Where a decision requires authoritative current state, a projection may be insufficient even when it is available and internally consistent.

⸻

45. Context and Idempotency

Execution Context may contain information about previous attempts.

Example:

workflow_id = W-123
action_id = A-456
attempt = 2
previous_result = UNKNOWN

This information can help determine whether an Action should be retried or whether its prior execution must first be reconciled.

An unknown prior outcome must not be treated as equivalent to a confirmed failure.

This is particularly important for preventing duplicate execution.

⸻

46. Context and Failure

Failure Context records information relevant to understanding an unsuccessful or uncertain execution.

Examples:

* Action attempted
* failure type
* source system
* timestamp
* attempt number
* enterprise response
* last known state
* correlation identifiers
* relevant Context Snapshot

This information supports:

* retry
* recovery
* compensation
* reconciliation
* human intervention
* audit

Failure Context should preserve uncertainty where the external outcome is unknown.

⸻

47. Context and Recovery

Recovery may require Context different from the Context used for the original attempt.

For example:

Attempt 1
   ↓
Timeout
   ↓
Enterprise state may have changed
   ↓
Refresh Context
   ↓
Re-evaluate
   ↓
Retry / Reconcile / Escalate

Noema must not assume that stale Context remains valid after failure.

This is particularly important where a timeout creates an unknown outcome rather than a confirmed failure.

Noema’s current architecture explicitly requires safe handling of partial failure, timeout, and unknown outcomes rather than blind retry. Noema Master Company Document FINAL.pdf

⸻

48. Context and Auditability

For consequential execution, Noema should preserve enough Context to reconstruct the decision.

Relevant information may include:

* Principal
* Intent
* Resources
* Relevant enterprise facts
* Reconstructed state
* Policy
* Constraints
* Evidence
* Authorization
* Trust decision
* Action
* timestamp
* versions
* Context Snapshot
* Outcome

Sensitive data should be subject to applicable retention and access policies.

Auditability does not require indiscriminately retaining every piece of enterprise data.

It requires preserving enough relevant information to establish what Noema knew, what it relied upon, what decision was made, and what happened.

⸻

49. Context and Reconstruction

A historical execution should be reconstructable without pretending that historical Context is today’s Context.

Conceptually:

Historical Intent
       +
Historical Context
       +
Historical Evidence
       +
Historical Policy
       +
Historical State
       ↓
Historical Decision

This is essential for auditability.

The reconstruction target is:

What was known, authoritative, applicable, and permitted at the time the decision was made?

It is not:

What does the system say today?

This distinction is essential for a trustworthy audit record.

⸻

50. Context Lifecycle

Context may move through several semantic states:

REQUESTED
    ↓
ASSEMBLED
    ↓
VALIDATED
    ↓
AVAILABLE
    ↓
CONSUMED
    ↓
REFRESHED
    ↓
EXPIRED

These are conceptual states.

A particular implementation may represent them differently.

Context lifecycle state must not be confused with:

* fact status
* enterprise state
* Trust outcome
* Action state
* Context freshness
* Context validity

⸻

51. Context Expiration

Context should be considered expired when its freshness or validity no longer satisfies the requirements of the current decision.

Expiration may result from:

* time
* enterprise state change
* Policy change
* permission change
* Resource change
* workflow transition
* risk change
* invalidated credentials
* changed execution conditions

Expired Context may remain useful historically.

It should not necessarily be used for current execution.

Expiration therefore means:

No longer valid for the current purpose

not necessarily:

Factually false.

⸻

52. Context Partitioning

Large Context should be partitionable by purpose.

For example:

Intent Context
      │
      ├── Identity Context
      ├── Resource Context
      └── Conversation Context
Trust Context
      │
      ├── Authorization
      ├── Policy
      ├── Evidence
      ├── Constraints
      └── Risk
Execution Context
      │
      ├── Action
      ├── Preconditions
      ├── Attempts
      ├── Capabilities
      └── Outcomes

This reduces unnecessary data exposure and makes semantic ownership clearer.

Partitioning does not mean the underlying facts cease to be related.

It means each consumer receives the Context relevant to its responsibility.

⸻

53. Context and Authority

Every consequential Context fact should have an identifiable authority where applicable.

The authority hierarchy should not be replaced by:

* recency
* frequency
* model confidence
* source count
* convenience
* majority vote

For example:

Ledger
   ↓
Canonical Balance
Analytics DB
   ↓
Derived Balance

Both may appear in Context.

They do not have equivalent authority.

Authority is a property of the information source and enterprise semantics, not of how confidently a model interprets the information.

⸻

54. Context and Confidence

Context should not be reduced to one global confidence score.

Different Context elements may have different semantic status:

* Canonical
* Derived
* Observed
* User-provided
* Model-inferred
* Historical
* Stale
* Unknown
* Conflicting
* Unverified

For example:

account_id
→ canonical
spending_category
→ derived
user statement
→ user-provided
intent interpretation
→ model-derived

The system should preserve these distinctions.

A high-confidence model inference must not become equivalent to a canonical enterprise fact merely because its confidence score is high.

⸻

55. Context and Uncertainty

Uncertainty should be represented explicitly.

For example:

account_id = UNKNOWN

is preferable to:

account_id = probably 123

when the account identifier is consequential.

Likewise:

Context:
multiple candidate accounts

is preferable to silently selecting one.

Noema should preserve uncertainty until it can be resolved according to deterministic rules, Policy, authoritative evidence, or explicit user confirmation.

The current Noema architecture explicitly defines unknown and ambiguous states as valid system states rather than failures to be hidden. Noema Master Company Document FINAL.pdf

⸻

56. Context and Clarification

Clarification is a mechanism for completing Context when information required for Intent or Action remains unresolved.

Example:

User:
"Show my statement."
Context:
Account A
Account B
        ↓
Clarification:
"Which account would you like the statement for?"

The answer becomes additional Context.

This allows the execution journey to progress without guessing.

Clarification should therefore be treated as a legitimate transition in the execution journey, not merely a conversational fallback.

⸻

57. Context and Enterprise Integration

Integrations provide mechanisms for acquiring Context.

Examples:

* REST APIs
* GraphQL APIs
* event streams
* databases
* identity providers
* policy systems
* enterprise applications
* message queues
* internal services

The integration mechanism is not itself Context.

It is the mechanism through which Context may be acquired.

An API response is therefore an input to Context construction, not automatically canonical Context.

⸻

58. Context and Integration Failure

If an integration fails:

Enterprise API
      ↓
Unavailable
      ↓
Required Context Missing

Noema must apply the relevant Trust and Policy rules.

It should not silently substitute arbitrary information merely to keep the Workflow moving.

Possible states may include:

RETRY
UNKNOWN
CLARIFY
ESCALATE
REJECT

depending on the nature and materiality of the missing information.

⸻

59. Context Model

Conceptually:

Context {
    principal
    intent
    resources
    facts
    reconstructed_state
    policies
    permissions
    authority
    constraints
    evidence
    temporal_state
    organizational_state
    conversation
    execution_state
}

This is a semantic model.

It does not require a literal database object with these exact fields.

The important property is preservation of semantic distinctions.

⸻

60. Context Fact

An individual Context fact may be represented conceptually as:

ContextFact {
    subject
    attribute
    value
    source
    authority
    classification
    status
    observed_at
    effective_at
    expires_at
    version
    provenance
}

Not every field is required for every fact.

The model exists to preserve the semantics necessary for Trust and execution.

In particular, a ContextFact should be capable of distinguishing:

* what the value is
* what it refers to
* where it came from
* who or what is authoritative
* when it was observed
* when it became effective
* whether it remains valid
* what semantic status it has

⸻

61. Context Relationships

Context connects the major Noema concepts:

Principal
    │
    ▼
Intent
    │
    ▼
Context
    │
    ├── references → Resource
    ├── contains → Facts
    ├── includes → Policy
    ├── includes → Evidence
    ├── includes → Authority
    ├── constrained_by → Permissions
    ├── bounded_by → Organization
    ├── scoped_by → Time
    ├── informed_by → State Reconstruction
    └── tracks → Execution

Context therefore acts as a semantic bridge between Intent and enterprise execution.

It is not the owner of the concepts it references.

⸻

62. Context in the Noema Execution Model

The broader Noema flow is:

USER
 │
 ▼
INTENT
 │
 ▼
INTENT RESOLUTION
 │
 ▼
CONTEXT
 │
 ▼
STATE RECONSTRUCTION
 │
 ▼
TRUST
 │
 ├── Clarify
 ├── Confirm
 ├── Escalate
 ├── Reject
 ├── Wait
 └── Execute
          │
          ▼
       ACTION
          │
          ▼
      ENTERPRISE
          │
          ▼
   FRESH CONTEXT
          │
          ▼
    POSTCONDITION
          │
          ▼
       OUTCOME

Context therefore participates throughout the execution journey rather than existing only at the beginning.

Context may be assembled, updated, partitioned, refreshed, consumed, and reconstructed at multiple stages.

This reflects the current Noema architecture in which Context, State Reconstruction, Trust, Action Graph, Execution, Verification, Recovery, and Audit form a continuous trusted-execution path. Noema Master Company Document FINAL.pdf

⸻

63. Context and Noema’s Commercial Wedge

Noema’s initial commercial wedge focuses on read and support operations:

* balance inquiries
* statement retrieval
* transaction search
* spending summaries
* complaint logging

Even these apparently simple operations require Context.

For example:

“How much did I spend last month?”

requires Noema to establish:

Principal
Account
Date Range
Relevant Transactions
Currency
Authorization

The value of Noema is therefore not merely retrieving data.

It is resolving natural-language Intent into a bounded, authorized, trustworthy enterprise operation.

The POC deliberately proves this broader execution discipline against a realistic enterprise environment rather than treating simple retrieval as equivalent to trusted execution. Noema Master Company Document FINAL.pdf

⸻

64. Context and Future Expansion

The Context model should support future higher-risk operations without assuming that they belong to the initial wedge.

Future Actions may require stronger guarantees around:

* authorization
* freshness
* confirmation
* risk
* policy
* identity
* financial state
* beneficiary state
* execution verification
* state reconciliation
* idempotency

The Context model should therefore be extensible while preserving the same authority boundaries.

The initial POC’s prohibited-action boundary does not constrain the ontology from representing future higher-risk execution requirements; it constrains what the POC is permitted to execute. NOEMA POC Specification HTML.html

⸻

65. Context Invariants

Invariant 1

Context is bounded information relevant to a particular decision or execution.

Invariant 2

Context is not synonymous with enterprise Business State.

Invariant 3

Context does not become canonical merely because Noema stores or consumes it.

Invariant 4

Enterprise Systems of Record remain authoritative for their respective Business State.

Invariant 5

Context must preserve the authority semantics of the information it contains.

Invariant 6

Context must be scoped by the relevant Principal, Resource, Action, organization, tenant, environment, and time where applicable.

Invariant 7

Context should contain the minimum information necessary for the current decision.

Invariant 8

Context completeness is Action-specific.

Invariant 9

Context freshness is independent of authority.

Invariant 10

Stale Context must not be used for consequential execution when freshness requirements are not satisfied.

Invariant 11

Model-generated interpretations must remain distinguishable from authoritative enterprise facts.

Invariant 12

User-provided information is not canonical by default.

Invariant 13

Derived information is not canonical by default.

Invariant 14

Evidence and Context are related but semantically distinct.

Invariant 15

Conversation history may contribute to Context but cannot redefine enterprise Business State.

Invariant 16

Conflicting Context must not be resolved through probabilistic guessing when authoritative resolution is required.

Invariant 17

Missing consequential Context must remain explicitly represented.

Invariant 18

Ambiguity revealed by Context must remain an explicit state until deterministically resolved.

Invariant 19

Context used for consequential execution should retain sufficient provenance for audit and reconstruction.

Invariant 20

Context may need to be refreshed between planning, execution, retry, and verification.

Invariant 21

Historical Context must remain distinguishable from current Context.

Invariant 22

Context must respect enterprise authorization, privacy, tenancy, organizational, legal, and environment boundaries.

Invariant 23

Noema must not create shadow canonical Business State merely by maintaining Context.

Invariant 24

Context should be partitioned according to purpose and least-privilege requirements.

Invariant 25

The model may use Context probabilistically, but consequential execution must be governed by deterministic Trust and Policy.

Invariant 26

Context availability does not imply Context validity.

Invariant 27

Context authority does not imply permission to access or use the underlying information.

Invariant 28

Events may contribute to Context without necessarily establishing current canonical state.

Invariant 29

Context snapshots may support auditability without becoming the current enterprise truth.

Invariant 30

When required Context cannot be established, Noema must preserve the uncertainty rather than manufacture certainty.

Invariant 31

Context must preserve the distinction between an observed enterprise fact and a Noema-derived interpretation of that fact.

Invariant 32

A Context fact’s authority must not be inferred solely from source availability, recency, frequency, or model confidence.

Invariant 33

Context freshness must be evaluated against the requirements of the specific Action or decision.

Invariant 34

Context expiration does not necessarily mean that the underlying fact was historically incorrect.

Invariant 35

Context assembled from multiple enterprise systems must preserve sufficient source and authority information for reconciliation.

Invariant 36

An event or projection may contribute Context without becoming the enterprise System of Record.

Invariant 37

An unknown external outcome must remain distinguishable from a confirmed failure.

Invariant 38

A Context Snapshot must represent the information relied upon at a particular decision point without becoming current enterprise truth.

Invariant 39

Context supplied to an Action must be bounded by the Action’s requirements and applicable authorization.

Invariant 40

Technical access to enterprise data does not establish semantic permission for that data to enter Context.

Invariant 41

Context must not silently cross tenant, organization, Resource-ownership, legal, or environment boundaries.

Invariant 42

A model-generated candidate interpretation must not become authoritative merely because it is represented inside Context.

Invariant 43

Human-provided information must preserve its source and authority semantics when incorporated into Context.

Invariant 44

Human intervention does not retroactively convert previously uncertain Context into historically certain Context.

Invariant 45

Context required for a consequential Action must be sufficient for the applicable Preconditions, Constraints, Authority, Policy, and Trust decision.

Invariant 46

The absence of a required Context fact must remain distinguishable from a fact whose value is false.

Invariant 47

Conflicting Context must preserve the competing observations until authoritative resolution occurs.

Invariant 48

Context must not be reduced to a single confidence score.

Invariant 49

Semantic status such as canonical, derived, observed, inferred, stale, unknown, and conflicting must remain distinguishable where material.

Invariant 50

Historical Context must remain available for reconstruction where required without being mistaken for current Context.

Invariant 51

Context refresh must not destroy the historical Context against which a prior decision was made.

Invariant 52

Context partitioning must not weaken the authority or provenance semantics of the underlying information.

Invariant 53

Noema must not manufacture missing Context merely to satisfy a downstream Action Contract.

Invariant 54

Noema must not use stale Context to bypass a current freshness requirement.

Invariant 55

Context may inform Trust, but Context itself is not a Trust decision.

Invariant 56

Context may contain Policy and Constraint information, but Context itself is not Policy or Constraint.

Invariant 57

Context may contain Authority and Permission information, but possession of that information does not itself constitute authorization.

Invariant 58

Context may contain State Reconstruction results, but a reconstructed view does not replace the underlying enterprise Systems of Record.

Invariant 59

Consequential execution must be traceable to the relevant Context and state against which the Trust decision was made.

Invariant 60

Context must preserve sufficient temporal semantics to distinguish observation time, effective time, execution time, and validity where those distinctions affect a decision.

⸻

66. Final Definition

Context is the bounded, relevant, purpose-scoped, authority-aware information available to Noema for interpreting Intent, resolving ambiguity, reconstructing relevant state, evaluating Trust, planning Actions, executing against enterprise systems, and verifying Outcomes.

The fundamental relationship is:

ENTERPRISE SYSTEMS
       │
       ▼
RELEVANT FACTS
       │
       ▼
     CONTEXT
       │
       ├───────────────┐
       ▼               ▼
INTENT RESOLUTION   STATE RECONSTRUCTION
       │               │
       └───────┬───────┘
               ▼
             TRUST
               │
               ├── Clarify
               ├── Confirm
               ├── Escalate
               ├── Reject
               └── Execute
                      │
                      ▼
                   ACTION
                      │
                      ▼
             ENTERPRISE SYSTEM
                      │
                      ▼
               FRESH CONTEXT
                      │
                      ▼
                POSTCONDITION
                      │
                      ▼
                   OUTCOME

And the architectural rule is:

Context is what Noema needs to know to make and execute a decision—not everything the enterprise knows.

A second rule is equally important:

Context is not truth merely because it is present.

Noema may assemble, store, transform, partition, refresh, and reason over Context, but it must preserve the authority, provenance, scope, freshness, classification, uncertainty, and ownership of the information from which that Context is derived.

The resulting conceptual distinction is:

Enterprise Systems
        │
        ▼
Enterprise State
        │
        ▼
Observations / Facts
        │
        ▼
Context
        │
        ├── may contain ──► Evidence
        ├── may contain ──► Policy
        ├── may contain ──► Authority
        ├── may contain ──► Permissions
        ├── may contain ──► Constraints
        └── may contain ──► Reconstructed State
                              │
                              ▼
                            Trust
                              │
                              ▼
                            Action
                              │
                              ▼
                         Execution
                              │
                              ▼
                         Verification

The deepest ontology-level principle is therefore:

Context is the bounded information boundary through which Noema understands and acts upon the world, while preserving the distinction between what is known, what is authoritative, what is inferred, what is permitted, what is current, and what remains uncertain.

That distinction is what prevents Context from becoming a hidden substitute for enterprise truth, a container for unverified model assumptions, or an implicit authorization mechanism. It is also what allows Noema’s deterministic Trust layer to make a defensible decision from the exact information available at the time of execution. NOEMA POC Specification_1.pdf