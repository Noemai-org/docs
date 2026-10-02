> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Composition

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-composition.md

⸻

1. Definition

Intent Composition is the process by which multiple related Intents are represented together with the semantic relationships, dependencies, conditions, constraints, and expected Outcomes that connect them to a larger Actor objective, without losing the identity of the individual Intents.

Composition exists because a human request may express more than one semantic goal.

For example:

"Close my old account and move the remaining balance to my new account."

This may contain at least two Intents:

Intent A:
TransferBalance
Intent B:
CloseAccount

with a semantic relationship:

TransferBalance
      ↓
   PRECEDES
      ↓
CloseAccount

The composed structure represents the Actor’s larger objective while preserving the individual semantic units.

Composition is therefore a semantic relationship layer over multiple Intents. It does not replace Intent resolution, Executable Intent, Trust, Action, or Execution.

⸻

2. Why Intent Composition Exists

Real-world requests frequently contain:

* multiple Actions
* multiple Outcomes
* dependencies
* conditions
* sequences
* parallel goals
* nested goals
* alternatives
* optional goals
* shared Context
* shared Constraints

Examples:

"Create a project, add Sarah, and send her the invitation."
"Refund the payment and notify the customer."
"Update my address everywhere."
"Book a flight and add it to my calendar."

Treating each semantic goal as an isolated Intent would lose relationships between the requested operations.

Noema therefore needs a canonical representation for:

What goals exist?
How are they related?
Which goals depend on others?
Which may proceed independently?
Which are conditional?
Which are optional?
What constitutes satisfaction of the larger objective?

⸻

3. Composition Does Not Mean Merging Everything

Composition must not collapse multiple Intents into one indistinguishable object.

For example:

"Refund the payment and email the customer."

contains at least two semantic objectives:

Intent A:
RefundPayment
Intent B:
NotifyCustomer

They may be composed:

Composite
├── RefundPayment
└── NotifyCustomer

but each constituent Intent retains its own:

* Identity
* Version
* Actor
* Resources
* Parameters
* Scope
* Constraints
* Expected Outcome
* Resolution state
* Trust requirements
* Lifecycle
* Outcome

Therefore:

Composition creates structure between Intents; it does not erase their identity.

⸻

4. Atomic Intent

An Atomic Intent is an Intent that Noema treats as a single semantic objective for the relevant abstraction level and lifecycle.

Examples:

RenewCard(Card#123)
RefundPayment(Payment#8291)

Atomicity is contextual.

An Intent that is atomic from the Actor’s perspective may require multiple lower-level Actions.

For example:

Intent:
RenewCard
Possible Actions:
VerifyEligibility
CreateReplacement
DeactivateOldCard
UpdateAccount

These Actions do not automatically become separate user-level Intents.

Therefore:

Intent atomicity is semantic, not equivalent to implementation atomicity or Action count.

⸻

5. Composite Intent

A Composite Intent is a semantic composition containing multiple related Intents whose relationship contributes to a larger Actor objective.

Example:

Composite:
PrepareEmployeeOnboarding
├── CreateEmployeeAccount
├── GrantRequiredAccess
├── CreateEmailMailbox
└── NotifyEmployee

A composition may define:

* Ordering
* Dependency
* Parallelism
* Conditions
* Alternatives
* Optionality
* Shared Context
* Shared Constraints
* Expected Outcomes

The constituent Intents remain independently identifiable.

⸻

6. Composition Is Semantic, Not Merely Procedural

A workflow is primarily concerned with execution steps.

Intent Composition is concerned with semantic goals and the relationships between them.

For example:

"Transfer the balance and then close the account."

contains the semantic relationship:

CloseAccount
requires
TransferBalance
to have completed

The exact API calls, retries, queues, transactions, and timing are execution concerns.

Therefore:

Intent Composition is not a workflow definition.

The composition constrains execution without becoming the execution workflow itself.

⸻

7. Composition Relationships

A Composite Intent may contain explicit relationships such as:

* PRECEDES
* DEPENDS_ON
* PARALLEL_WITH
* CONDITIONAL_ON
* OPTIONAL
* ALTERNATIVE_TO
* ENABLES
* REQUIRES
* NESTED_WITHIN
* SHARES_CONTEXT_WITH

The exact relationship vocabulary is implementation-specific, but the semantic relationship must be explicit wherever it affects resolution, Trust, planning, execution, or Outcome evaluation.

Noema should not repeatedly infer consequential relationships from the original natural-language expression downstream.

⸻

8. Sequential Composition

Sequential composition expresses an ordering or prerequisite relationship.

Example:

"Create the account and then send me the credentials."

Semantic structure:

CreateAccount
      ↓
   PRECEDES
      ↓
SendCredentials

The second Intent depends on a semantic condition established by the first.

The relationship does not prescribe a particular API sequence or execution mechanism.

⸻

9. Parallel Composition

Some Intents can be pursued independently.

Example:

"Update my address and change my notification preferences."

Conceptually:

UpdateAddress      ChangePreferences
       │                   │
       └──── independent ──┘

Parallel composition means that neither Intent semantically depends on the completion of the other.

It does not require simultaneous execution.

Execution may serialize, batch, queue, or otherwise schedule the Actions while preserving the semantic independence.

⸻

10. Dependency Composition

An Intent may depend on another Intent without requiring a specific low-level execution sequence.

Example:

CreateProject
      ↓
  DEPENDS_ON
      ↓
AddMembers

The dependency is semantic:

The Project must exist before the member relationship can be established.

It does not mean:

API call A must finish exactly before API call B begins.

The Planner and Execution Controller determine the concrete implementation sequence within the composition’s semantic constraints.

⸻

11. Conditional Composition

An Intent may depend on a condition established by another Intent or by reconciled state.

Example:

"If the payment failed, retry it; otherwise send the receipt."

Conceptually:

Payment State
      ↓
 ┌────┴────┐
 │         │
Failed   Successful
 │         │
 ▼         ▼
Retry    SendReceipt

The condition is part of the semantic composition.

Execution logic determines how the condition is evaluated using authoritative or reconciled state.

A Model must not be relied upon to reinterpret the condition during execution.

⸻

12. Optional Composition

An Intent may contain an optional subordinate Intent.

Example:

"Book the flight and, if possible, add it to my calendar."

Conceptually:

BookFlight
    │
    └── OPTIONAL → AddToCalendar

Optionality means that failure or non-execution of the optional constituent does not necessarily invalidate the primary semantic objective.

The exact parent Outcome semantics must define whether an optional child contributes to complete, partial, or degraded satisfaction.

⸻

13. Alternative Composition

An Intent may express alternatives rather than simultaneous objectives.

Example:

"Either renew my card or issue a replacement, whichever is appropriate."

Conceptually:

          Card State
              │
       ┌──────┴──────┐
       ▼             ▼
  RenewCard    IssueReplacement

The alternatives are not two Actions to execute independently.

Noema must establish the selection condition through applicable Intent semantics, current state, Constraints, and Policy.

If multiple alternatives remain materially valid and the Actor’s preference is consequential, the ambiguity must be resolved rather than silently selecting one.

⸻

14. Nested Intent

An Intent may contain subordinate semantic Intents.

Example:

PrepareEmployeeOnboarding
├── CreateAccount
├── ProvisionEmail
├── GrantAccess
└── NotifyEmployee

The parent represents the larger semantic objective.

The children represent constituent semantic goals.

Nested structure does not make the children mere implementation steps. Each child retains its own semantic identity and lifecycle.

⸻

15. Parent and Child Intent

A parent Intent defines a broader semantic objective.

A child Intent represents a subordinate objective that contributes to satisfying the parent.

Example:

Parent:
OnboardEmployee
Children:
CreateEmployeeAccount
GrantAccess
SendWelcomeEmail

The relationship between parent and child is semantic.

A child may have its own:

* Actor
* Authority
* Constraints
* Policy
* Resources
* Trust evaluation
* Outcome

The parent does not automatically inherit or grant these properties.

⸻

16. Composition Must Preserve Intent Identity

Each constituent Intent should retain its own identity.

Conceptually:

Composite: CI-100
Intent: I-101
Intent: I-102
Intent: I-103

This allows Noema to independently track:

* Resolution
* Clarification
* Version
* Trust
* Action
* Execution
* Verification
* Outcome
* Failure
* Recovery
* Retry

for each constituent Intent.

The composition relationship itself should also be identifiable and auditable.

⸻

17. Shared Actor

Multiple Intents may share the same Actor.

Example:

"Update my address and change my phone number."
Actor:
Alice
Intent A:
UpdateAddress
Intent B:
UpdatePhoneNumber

The Actor may be shared without merging the Intents.

Actor identity remains an explicit property of each Intent.

⸻

18. Different Actors

A composition may involve multiple Actors where the domain permits it.

Example:

"Ask Sarah to approve the invoice and then notify the customer."

Potential structure:

Intent A:
RequestApproval
Actor:
Alice / System
Intent B:
ApproveInvoice
Actor:
Sarah
Intent C:
NotifyCustomer
Actor:
System

The Actor associated with each constituent Intent must remain explicit.

Noema must not assume that the Actor of the parent automatically becomes the Actor of every child.

Likewise, a parent Actor cannot manufacture Authority for another Actor.

⸻

19. Shared Resources

Multiple Intents may operate on the same Resource.

Example:

"Update the customer's address and notify them."
Resource:
Customer#123
Intent A:
UpdateAddress
Intent B:
NotifyCustomer

The shared Resource relationship may be represented explicitly.

This prevents downstream systems from independently resolving the same reference and potentially binding the Intents to different Resources.

⸻

20. Resource Dependencies

One Intent may create or transform a Resource required by another Intent.

Example:

CreateInvoice
      ↓
   ENABLES
      ↓
SendInvoice

The output Resource of the first Intent may become an input Resource of the second.

The dependency should be represented semantically rather than reconstructed from execution logs.

⸻

21. Shared Constraints

A Composite Intent may have Constraints applying to multiple constituent Intents.

Example:

"Update everything before the end of the business day."
Composite Constraint:
Deadline = Today 17:00
├── UpdateAddress
├── UpdatePhone
└── UpdatePreferences

Child Intents may have additional Constraints.

Therefore:

Composite Constraints
+
Child Constraints

must be evaluated according to their defined scope.

A parent Constraint must not silently override a more specific Constraint unless the applicable semantic model explicitly permits it.

⸻

22. Shared Context

A Composite Intent may establish Context that applies to multiple children.

Example:

"For the Acme account, update the billing contact and notify the finance team."
Shared Context:
Account = Acme
├── UpdateBillingContact
└── NotifyFinance

Shared Context reduces repeated resolution.

However:

Shared Context is not automatically authoritative.

Each constituent Intent must use Context only to the extent that it is relevant, valid, scoped, fresh, and sufficiently authoritative for the claim being resolved.

⸻

23. Composition and Clarification

A Composite Intent may contain one unresolved constituent while others are fully resolved.

Example:

Composite
├── UpdateAddress       RESOLVED
├── UpdatePhone         RESOLVED
└── NotifyEmployer      AMBIGUOUS

Noema should not necessarily discard the entire composition.

Instead:

Composite
   ↓
Child Intent C
   ↓
Material Ambiguity
   ↓
Targeted Clarification

The unresolved constituent can be clarified independently where the composition semantics permit it.

Clarification must preserve the identity and version lineage of the affected Intent.

⸻

24. Composition and Partial Resolution

Intent Composition supports partial resolution.

For example:

Intent A:
RESOLVED
Intent B:
RESOLVED
Intent C:
CLARIFICATION_REQUIRED

The Composite is not fully executable while a required constituent remains materially unresolved.

However, independent constituents may still progress if:

1. their own semantics are sufficiently resolved,
2. their dependencies are satisfied,
3. their execution does not violate the composition,
4. their independent execution is permitted by Trust and Policy,
5. doing so does not create an unintended consequence if another constituent later fails or changes.

Partial execution must therefore be a semantic property of the composition, not an accidental consequence of execution order.

⸻

25. Composition and Executable Intent

Each constituent Intent must independently satisfy the requirements for Executable Intent before it can proceed toward consequential Action.

Conceptually:

Composite
├── Intent A → Executable Intent
├── Intent B → Executable Intent
└── Intent C → Executable Intent

The composition itself may also have unresolved semantic conditions, dependencies, or required constituent Outcomes.

Therefore:

A collection of executable child Intents is not automatically an executable composition.

The composition must remain consistent with its own dependencies, Constraints, conditions, and Expected Outcome semantics.

⸻

26. Composition and Trust

Trust is evaluated against the relevant Intent and Action semantics.

A composite structure does not create a single blanket authorization.

Example:

Composite:
TransferAndCloseAccount
├── TransferBalance
└── CloseAccount

The Actor may satisfy the applicable authority conditions for one constituent but not the other.

Therefore:

Trust(TransferBalance)
Trust(CloseAccount)

may produce different Trust outcomes.

A parent-level Trust result must not automatically authorize every child Intent.

The canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Confirmation or approval requirements are control conditions, not additional Trust outcomes.

⸻

27. Composition and Policy

Policies may apply at different semantic scopes:

* Composite level
* Child Intent level
* Action level
* Resource level
* Capability level

Example:

Composite:
EmployeeOffboarding
Policy:
All access must be revoked.
Child:
RevokeGitHubAccess
Policy:
Requires Security approval.
Child:
RevokeEmail
Policy:
No additional approval required.

Each constituent retains its own applicable Policy requirements.

Policy scope must be explicit enough to determine which conditions apply to which constituent.

⸻

28. Composition and Authority

Authority is evaluated according to the resolved Actor, Action, Resource, Scope, and applicable authorization conditions of each constituent Intent.

A user may be authorized to:

UpdateCustomerAddress

but not:

DeleteCustomerAccount

even when both appear inside one Composite Intent.

Therefore:

Composition does not aggregate, transfer, or inherit Authority.

A parent Intent cannot confer Authority that its constituent Actor does not otherwise possess.

⸻

29. Composition and Failure

Constituent Intents may have different execution and Outcome states.

Example:

CreateAccount
GrantAccess
SendWelcomeEmail

Results:

Account creation = successful
Access grant = successful
Email delivery = failed

The Composite may therefore be partially satisfied.

Noema must distinguish:

Intent State
Action State
Execution State
Outcome State
Composite Outcome

A child failure does not automatically determine the parent Outcome unless the composition semantics make that child outcome required.

⸻

30. Composition and Compensation

Some compositions may require compensating Actions when a later constituent fails.

Example:

CreateSubscription
      ↓
ChargeCustomer
      ↓
ProvisionService

If provisioning fails after payment succeeds, a compensating Action may be required:

RefundPayment

Compensation is primarily an execution concern.

Intent Composition should expose the semantic dependencies and required Outcomes necessary for the execution layer to determine whether compensation is required.

The existence of a dependency does not by itself guarantee that compensation is possible.

⸻

31. Composition Is Not Transactionality

Two or more Intents being composed does not mean they form one atomic transaction.

For example:

UpdateCRM
+
SendEmail

may have no distributed transactional boundary.

Composition defines semantic relationships.

The execution substrate determines whether underlying Actions support:

* Atomicity
* Rollback
* Compensation
* Retry
* Idempotency
* Eventual consistency
* Durable recovery

Therefore:

Intent Composition is not a distributed transaction.

⸻

32. Composition and Outcome

A Composite Intent may have:

1. individual constituent Outcomes, and
2. a Composite Outcome.

Example:

Parent:
OnboardEmployee
Child Outcomes:
Account created
Email created
Access granted
Welcome email sent
Composite Outcome:
Employee successfully onboarded

The Composite Outcome should be derived from the semantic requirements of the composition.

It must not be inferred solely from technical execution responses such as HTTP status codes.

Actual Outcome requires execution evidence and verification against the relevant enterprise state where necessary.

⸻

33. Composition and Outcome Dependencies

Some Composite Outcomes require specific constituent Outcomes.

Example:

Composite:
TransferAndCloseAccount
Required Outcomes:
Transfer completed
AND
Account closed

If only the transfer succeeds:

Composite Outcome:
Not satisfied

The transfer may still have a successful constituent Outcome.

Therefore:

Constituent success and Composite satisfaction are distinct semantic states.

⸻

34. Composition Graph

A useful canonical representation is a directed semantic graph:

             Composite Intent
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   Intent A     Intent B      Intent C
       │            │            │
       ▼            │            ▼
   Outcome A        │        Outcome C
                    │
                    ▼
                Outcome B

Edges represent semantic relationships such as:

PRECEDES
DEPENDS_ON
ENABLES
REQUIRES
CONDITIONAL_ON
OPTIONAL
ALTERNATIVE_TO

The graph expresses semantic constraints and relationships.

It does not itself prescribe the complete execution workflow.

⸻

35. Composition Must Be Explicit

Noema should not reconstruct consequential composition from execution logs after the fact.

If the Actor expressed:

"Transfer the balance and then close the account."

the semantic relationship should exist before execution:

TransferBalance
      ↓
   PRECEDES
      ↓
CloseAccount

The Planner and Execution Controller consume this relationship when determining an executable plan.

⸻

36. Composition and Natural Language

Natural language can encode composition through expressions such as:

and
then
after
before
unless
if
otherwise
also
as well as
while
until
either

For example:

"Update my address and notify my employer."
UpdateAddress
AND
NotifyEmployer
"Update my address, then notify my employer."
UpdateAddress
PRECEDES
NotifyEmployer
"Notify my employer if the address update succeeds."
NotifyEmployer
CONDITIONAL_ON
UpdateAddress.Success

The linguistic relationship should be translated into canonical semantic structure.

The original expression should not need to be reinterpreted by downstream execution components.

⸻

37. Composition Must Preserve Human Intent

Noema should not create unnecessary composition merely because one Intent requires multiple internal Actions.

For example:

"Renew my card."

The execution system may perform:

VerifyEligibility
CreateReplacement
UpdateAccount
DeactivateOldCard

These do not automatically become four user-level Intents.

They may simply be Actions required to satisfy one Intent.

Therefore:

Intent Composition is driven by semantic goals, not implementation step count.

⸻

38. Composition vs Action Decomposition

These concepts must remain distinct.

Intent Composition

Multiple semantic goals:

RefundPayment
+
NotifyCustomer

Action Decomposition

One semantic goal requiring multiple operations:

RenewCard
    ↓
VerifyEligibility
    ↓
CreateCard
    ↓
UpdateAccount

Intent Composition operates at the semantic-goal level.

Action decomposition operates at the execution level.

This distinction is critical to maintaining Noema’s abstraction boundary.

⸻

39. Composition and User Expression

A single expression may contain:

* one Intent,
* multiple Intents,
* one Intent with multiple Actions,
* multiple Intents with dependencies.

Conversely, multiple expressions may represent one Intent.

Example:

"I need to replace my card. It's expired."

This may represent one Intent:

ReplaceCard

with the second sentence providing Context or supporting Evidence.

Therefore:

Intent boundaries are semantic, not grammatical.

⸻

40. Composition and Context

A previous Intent may establish Context for a subsequent Intent.

Example:

User:
"Create a project called Noema."
Intent A:
CreateProject
User:
"Add Sarah to it."
Intent B:
AddMember
Context:
Project = newly created Noema project

The second Intent may be independently identifiable but contextually linked to the first.

The relationship should be preserved where it affects semantic resolution, resource binding, dependencies, or auditability.

Context must still satisfy the normal requirements for relevance, scope, freshness, and authority.

⸻

41. Composition Across Turns

Intent composition may span multiple conversational turns.

Example:

Turn 1:
"Book me a flight to London."
Turn 2:
"And put it on my calendar."
Turn 3:
"Also send the itinerary to Sarah."

This may produce:

Composite
├── BookFlight
├── AddToCalendar
└── SendItinerary

with relevant dependencies and shared Context.

Composition therefore operates over the Intent lifecycle and conversational context, not merely over a single user message.

Each new constituent remains subject to validation, resolution, versioning, Trust, and execution controls.

⸻

42. Composition and Cancellation

A Composite Intent may be partially cancelled.

Example:

Composite:
BookFlight
+
AddToCalendar
+
NotifySarah

Actor:

"Actually, don't notify Sarah."

The resulting semantic state may be:

BookFlight
AddToCalendar
NotifySarah → CANCELLED

The remaining Intents retain their own identity and state.

Cancellation is a lifecycle/control state and is not one of the canonical Trust outcomes.

⸻

43. Composition and Modification

The Actor may modify one constituent Intent.

Example:

"Book the flight and add it to my calendar."
"Actually, don't add it to my calendar."

Noema may produce:

BookFlight
AddToCalendar → CANCELLED

provided no dependency requires the cancelled constituent.

A material semantic modification must create the appropriate new Intent version rather than silently mutating an admitted historical version.

The parent composition must be re-evaluated if the modification changes dependencies, Constraints, required Outcomes, or other material semantics.

⸻

44. Composition and Reuse

A resolved Intent may provide a Resource or Context dependency for another Intent.

Example:

CreateCustomer
      ↓
   ENABLES
      ↓
SendWelcomeEmail

The first Intent may establish:

Customer ID
Email address
Customer Context

for the second.

This allows Noema to construct semantic chains without requiring every downstream Intent to rediscover already resolved relationships.

The reused information remains subject to validity, scope, freshness, and authority requirements.

⸻

45. Composition and Idempotency

Each constituent Intent should have its own stable identity.

This allows Noema to determine:

Intent A → already satisfied
Intent B → pending
Intent C → failed

rather than treating the entire Composite as an opaque unit.

This is important for:

* Retries
* Recovery
* Partial completion
* Verification
* Duplicate prevention
* Causal audit

Intent identity and Action idempotency remain distinct concerns.

⸻

46. Composition and Audit

The audit trail should preserve:

* Parent or Composite identity
* Constituent Intent identities
* Intent versions
* Composition relationships
* Resolution history
* Clarification history
* Trust decisions
* Actions
* Execution state
* Verification evidence
* Constituent Outcomes
* Composite Outcome

Example:

Composite: OffboardEmployee#123
├── RevokeGitHubAccess
│   ├── Trust: EXECUTE
│   └── Outcome: Verified
│
├── DisableEmail
│   ├── Trust: EXECUTE
│   └── Outcome: Verified
│
└── NotifyManager
    ├── Trust: EXECUTE
    └── Outcome: UNKNOWN

This provides a semantic and operational history without requiring private Model chain-of-thought.

⸻

47. Composition and Re-evaluation

If a constituent Intent changes materially, the parent composition may require re-evaluation.

Example:

Parent:
TransferAndCloseAccount
Child:
TransferBalance

If the transfer destination changes:

TransferBalance
Resource / Parameter changed

the parent may need to be revalidated because:

* the dependency may have changed,
* the required Outcome may have changed,
* Policy applicability may have changed,
* Authority may need reevaluation,
* the closing Action may no longer be safe or valid.

Composition is therefore not merely static structure.

⸻

48. Composition and Determinism

The composition graph should be explicit enough that downstream deterministic components can establish:

* Which Intents exist
* Which Intent versions are active
* Which Intents depend on which
* Which Intents may proceed independently
* Which are conditional
* Which are optional
* Which are alternatives
* Which Resources are shared
* Which Constraints are shared
* Which Outcomes are required
* Which constituent Outcomes determine Composite satisfaction

without asking the Model to reinterpret the original request.

This supports the hard boundary between probabilistic interpretation and deterministic Trust and execution.

⸻

49. Canonical Composition Model

Conceptually:

CompositeIntent
├── identity
├── version
├── source
├── parent_actor
├── shared_context
├── shared_constraints
├── intents[]
│   ├── identity
│   ├── version
│   ├── actor
│   ├── intent
│   ├── resources
│   ├── parameters
│   ├── scope
│   ├── constraints
│   ├── expected_outcome
│   └── resolution
├── relationships[]
│   ├── type
│   ├── source
│   ├── target
│   └── condition
└── expected_outcome

This is a conceptual model, not a required implementation schema.

A Composite Intent must not imply that all constituents share the same Actor, Authority, Policy, Resource, Trust decision, or lifecycle.

⸻

50. Composition and Intent Versioning

Composition itself must be version-aware.

If a material change occurs to:

* a constituent Intent,
* a dependency,
* a condition,
* a Constraint,
* a required Outcome,
* a Resource binding,

the affected semantic structure must be represented through explicit versioning rather than silently changing historical meaning.

Conceptually:

Composite v1
      ↓
Material modification
      ↓
Composite v2
      ↓
supersedes v1

Constituent Intent versions must remain independently traceable.

Historical execution must therefore remain bound to the exact composition and Intent versions under which it was authorized and executed.

⸻

51. Canonical Composition Rules

Noema should follow these rules:

Rule 1 — Preserve Intent Identity

Composing Intents must not erase their individual identities or versions.

Rule 2 — Composition Is Semantic

Composition represents relationships between semantic goals, not merely execution steps.

Rule 3 — Intent Boundaries Are Semantic

Sentence boundaries do not determine Intent boundaries.

Rule 4 — Dependencies Must Be Explicit

If one Intent depends on another, that dependency must be represented.

Rule 5 — Trust Is Not Automatically Inherited

A parent Trust decision does not automatically authorize every constituent Intent.

Rule 6 — Authority Is Not Aggregated

Composition does not transfer or aggregate Authority between Actors or constituents.

Rule 7 — Partial Resolution Is Permitted

Constituent Intents may resolve independently where the composition permits.

Rule 8 — Partial Execution Is Not Automatically Failure

The semantic meaning of partial completion depends on the composition’s requirements.

Rule 9 — Parent Outcome Must Be Explicit

The Composite Outcome must define what constitutes satisfaction of the larger objective.

Rule 10 — Implementation Steps Are Not Automatically Intents

Action decomposition remains distinct from Intent Composition.

Rule 11 — Composition Must Survive Execution

Consequential composition relationships must remain available to the Planner and Execution Controller.

Rule 12 — Composition Must Be Auditable

The relationship between constituent Intents, their versions, Trust decisions, Actions, and Outcomes must survive through the lifecycle.

Rule 13 — Material Changes Require Versioning

A material modification must not silently mutate historical semantic meaning.

⸻

52. Canonical Example

Human:

"Close my old bank account, transfer the remaining balance to my savings account, and email me the confirmation."

Noema may construct:

Composite Intent
│
├── TransferBalance
│     Resource: OldAccount
│     Destination: SavingsAccount
│
├── CloseAccount
│     Resource: OldAccount
│
└── SendConfirmation
      Recipient: Actor

Relationships:

TransferBalance
    PRECEDES
CloseAccount
CloseAccount
    ENABLES
SendConfirmation

Expected Composite Outcome:

Remaining balance transferred
AND
old account closed
AND
confirmation delivered

Each constituent Intent remains independently subject to:

Resolution
Executable Intent
Trust
Action Contracts
Execution
Verification
Outcome

This is substantially richer than generating three API calls because it preserves the semantic structure of the Actor’s objective.

⸻

53. The Key Architectural Distinction

Noema should maintain the following conceptual hierarchy:

Actor Expression
       ↓
Intent Detection / Decomposition
       ↓
Intent Composition
       ↓
Intent Resolution
       ↓
Executable Intent(s)
       ↓
Trust
       ↓
Action
       ↓
Execution
       ↓
Verification
       ↓
Outcome

Where:

Intent

represents a semantic goal.

Intent Composition

represents semantic relationships between multiple goals.

Executable Intent

represents a sufficiently resolved individual goal that can be evaluated deterministically by Trust and potentially acted upon.

Action

represents an operation that the system performs to satisfy an Intent.

Outcome

represents the verified result of execution relative to the requested or expected semantic objective.

Composition therefore sits above individual Executable Intents while constraining how they relate. It does not become a replacement for them.

⸻

54. What Intent Composition Protects Against

Intent Composition protects against:

* Lost dependencies
* Incorrect ordering
* Unintended partial execution
* Semantic drift between related operations
* Incorrect parent/child relationships
* Repeated reinterpretation of shared Context
* Loss of Actor-stated conditions
* Loss of alternative or optional semantics
* Incorrect Composite Outcome evaluation
* Treating independent Intents as one atomic operation

It gives Noema a formal semantic representation of multi-intent objectives.

⸻

55. What Intent Composition Does Not Do

Intent Composition does not:

* Execute Actions
* Authorize Actors
* Replace Trust
* Replace Policy
* Replace Constraints
* Resolve unresolved Intent semantics by itself
* Define implementation workflows
* Guarantee transactionality
* Guarantee atomicity
* Guarantee Outcome success
* Transfer Authority between Actors
* Make a constituent Intent Executable
* Make an Action permissible

Its purpose is to represent the semantic structure and relationships among multiple related Intents.

⸻

56. Final Definition

Intent Composition is the canonical representation of multiple semantically related Intents and the dependencies, ordering, conditions, alternatives, shared Context, Constraints, and Outcome relationships that connect them into a larger Actor objective while preserving the identity, version, lifecycle, Authority, Trust requirements, and Outcomes of each constituent Intent.

The essential pipeline is:

Actor Expression
       ↓
Intent Detection / Decomposition
       ↓
Intent Composition
       │
       ├── Intent A
       │      ↓
       │   Resolution
       │      ↓
       │   Executable Intent
       │
       ├── Intent B
       │      ↓
       │   Resolution
       │      ↓
       │   Executable Intent
       │
       └── Intent C
              ↓
           Resolution
              ↓
          Executable Intent
                │
                ↓
        Composition Constraints
        and Relationships
                ↓
              Trust
                ↓
             Actions
                ↓
           Verification
                ↓
             Outcomes

The shortest canonical formulation is:

Intent Composition preserves what the Actor wants as multiple semantic goals while making explicit how those goals relate to one another.